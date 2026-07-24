import difflib
import json
import re
import sys
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MATCH_ID = sys.argv[1] if len(sys.argv) > 1 else "42177"
INPUT = ROOT / "待录制对战输入"
OUT = ROOT / "录制输出" / MATCH_ID
SCRIPT = INPUT / f"{MATCH_ID}_2x_tts_ui_synced口语化v5.md"
VOICE = INPUT / f"{MATCH_ID}_full.wav"
TRANSCRIPT = OUT / "transcript_full.json"
RESULT = OUT / "voice_cues_full.json"


def clock_seconds(value):
    parts = [int(x) for x in value.strip().split(":")]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def normalized(value):
    return re.sub(r"[\W_]+", "", value, flags=re.UNICODE)


def subtitle_chunks(text, limit=34):
    sentences = [x for x in re.split(r"(?<=[。！？])", text) if x]
    chunks = []
    for sentence in sentences:
        if len(sentence) <= limit:
            chunks.append(sentence)
            continue
        clauses = [x for x in re.findall(r"[^，；。！？]+[，；。！？]?", sentence) if x]
        current = ""
        for clause in clauses:
            if current and len(current) + len(clause) > limit:
                chunks.append(current)
                current = clause
            else:
                current += clause
        if current:
            chunks.append(current)
    return chunks


def parse_sections(markdown):
    headings = list(re.finditer(r"^##\s+(.+)$", markdown, flags=re.M))
    sections = []
    for index, heading in enumerate(headings):
        block_end = headings[index + 1].start() if index + 1 < len(headings) else len(markdown)
        block = markdown[heading.end():block_end]
        narration_match = re.search(r"\*\*解说：\*\*\s*(.+?)(?:\r?\n\r?\n|\Z)", block, flags=re.S)
        source_match = re.search(
            r"\*\*源画面：\*\*.*?(\d{2}:\d{2})(?:\s*-\s*(\d{2}:\d{2}))?",
            block,
        )
        anchor_match = re.search(r"\*\*回放锚点：\*\*\s*(.+?)(?:\r?\n\r?\n|\Z)", block, flags=re.S)
        if not narration_match or not source_match:
            continue
        source_start = clock_seconds(source_match.group(1))
        source_end = clock_seconds(source_match.group(2)) if source_match.group(2) else None
        sections.append(
            {
                "label": heading.group(1).strip(),
                "narration": re.sub(r"\s+", "", narration_match.group(1)),
                "source_start": source_start,
                "source_end": source_end,
                "round_anchor": re.sub(r"\s+", " ", anchor_match.group(1)).strip()
                if anchor_match
                else "",
            }
        )
    for index, section in enumerate(sections):
        if section["source_end"] is None:
            section["source_end"] = (
                sections[index + 1]["source_start"] if index + 1 < len(sections) else 330.0
            )
    return sections


markdown = SCRIPT.read_text(encoding="utf-8")
sections = parse_sections(markdown)
transcript = json.loads(TRANSCRIPT.read_text(encoding="utf-8"))

with wave.open(str(VOICE), "rb") as handle:
    audio_duration = handle.getnframes() / handle.getframerate()

whisper_chars = []
whisper_times = []
for segment in transcript:
    words = segment.get("words") or []
    if not words:
        words = [{"w": segment["text"], "s": segment["start"], "e": segment["end"]}]
    for word in words:
        chars = list(normalized(word["w"]))
        for index, char in enumerate(chars):
            whisper_chars.append(char)
            whisper_times.append(
                float(word["s"])
                + (float(word["e"]) - float(word["s"])) * index / max(1, len(chars))
            )

cues = []
script_chars = []
cue_ranges = []
for section_index, section in enumerate(sections):
    section["cue_start"] = len(cues)
    for text in subtitle_chunks(section["narration"]):
        clean = normalized(text)
        start = len(script_chars)
        script_chars.extend(clean)
        cue_ranges.append((start, len(script_chars)))
        cues.append({"section": section_index, "sec": section["label"], "text": text})
    section["cue_end"] = len(cues)

matcher = difflib.SequenceMatcher(
    None, "".join(script_chars), "".join(whisper_chars), autojunk=False
)
anchors = []
for script_pos, whisper_pos, size in matcher.get_matching_blocks():
    for offset in range(size):
        anchors.append((script_pos + offset, whisper_times[whisper_pos + offset]))
anchors.sort()
anchor_positions = [item[0] for item in anchors]


def script_time(position):
    import bisect

    if position <= anchor_positions[0]:
        return anchors[0][1]
    if position >= anchor_positions[-1]:
        return anchors[-1][1]
    right = bisect.bisect_left(anchor_positions, position)
    if anchor_positions[right] == position:
        return anchors[right][1]
    p0, t0 = anchors[right - 1]
    p1, t1 = anchors[right]
    return t0 + (t1 - t0) * (position - p0) / max(1, p1 - p0)


starts = [script_time(start) for start, end in cue_ranges]
for index in range(1, len(starts)):
    starts[index] = max(starts[index], starts[index - 1] + 0.18)
for index, cue in enumerate(cues):
    start = starts[index]
    end = starts[index + 1] if index + 1 < len(starts) else audio_duration
    cue["s"] = round(max(0.0, start), 3)
    cue["e"] = round(end, 3)

for index, section in enumerate(sections):
    section["target_start"] = cues[section["cue_start"]]["s"]
    section["target_end"] = (
        cues[sections[index + 1]["cue_start"]]["s"]
        if index + 1 < len(sections)
        else round(audio_duration, 3)
    )
    section.pop("narration")

original_text = "".join(
    re.sub(r"\s+", "", match.group(1))
    for match in re.finditer(
        r"\*\*解说：\*\*\s*(.+?)(?:\r?\n\r?\n|\Z)", markdown, flags=re.S
    )
)
cue_text = "".join(cue["text"] for cue in cues)
text_exact = normalized(original_text) == normalized(cue_text)
if not text_exact:
    raise RuntimeError("subtitle cue text differs from the original narration")

payload = {
    "match_id": MATCH_ID,
    "audio_duration": round(audio_duration, 6),
    "text_exact": text_exact,
    "matched_characters": sum(size for _, _, size in matcher.get_matching_blocks()),
    "script_characters": len(script_chars),
    "cues": cues,
    "sections": sections,
}
RESULT.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
print(
    f"aligned {len(cues)} cues / {len(sections)} sections; "
    f"text_exact={text_exact}; span={cues[0]['s']:.3f}..{cues[-1]['e']:.3f}",
    flush=True,
)
