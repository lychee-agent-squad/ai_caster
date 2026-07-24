import json
import sys
from pathlib import Path

from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parents[2]
MATCH_ID = sys.argv[1] if len(sys.argv) > 1 else "42177"
VOICE = ROOT / "待录制对战输入" / f"{MATCH_ID}_full.wav"
OUT = ROOT / "录制输出" / MATCH_ID
OUT.mkdir(parents=True, exist_ok=True)

model = WhisperModel("small", device="cpu", compute_type="int8")
print(f"transcribing {VOICE.name} with word timestamps...", flush=True)
segments, info = model.transcribe(
    str(VOICE),
    language="zh",
    word_timestamps=True,
    vad_filter=True,
    initial_prompt=(
        "荔枝贡运对抗赛。红队神经突触突击队，蓝队代码即答案。"
        "朱雀门，潼关驿，兴庆宫，岭南果园，秦岭栈道，洞庭水驿，"
        "洛阳驿，武关，灞桥驿。皇榜任务，鲜度，好果，设卡，核验，"
        "冰鉴，快马，栈道复核，码头争船，清障，疾行令。"
    ),
)
data = [
    {
        "start": round(seg.start, 3),
        "end": round(seg.end, 3),
        "text": seg.text.strip(),
        "words": [
            {"w": word.word, "s": round(word.start, 3), "e": round(word.end, 3)}
            for word in (seg.words or [])
        ],
    }
    for seg in segments
]
with (OUT / "transcript_full.json").open("w", encoding="utf-8") as handle:
    json.dump(data, handle, ensure_ascii=False, indent=1)
print(f"done: {len(data)} segments, language={info.language}", flush=True)
