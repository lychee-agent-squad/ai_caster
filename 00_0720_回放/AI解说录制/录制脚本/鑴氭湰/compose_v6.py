import json
import math
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
MATCH_ID = sys.argv[1] if len(sys.argv) > 1 else "42177"
INPUT = ROOT / "待录制对战输入"
OUT = ROOT / "录制输出" / MATCH_ID
RAW = OUT / f"{MATCH_ID}_native_2x_raw.mp4"
RAW_CLEAN = OUT / f"{MATCH_ID}_native_2x_raw_clean.mp4"
OPENING = OUT / f"{MATCH_ID}_opening_4k.mp4"
VOICE = INPUT / f"{MATCH_ID}_full.wav"
AVATAR = ROOT / "贵妃讲解_透明抠像.mov"
FONT = SCRIPT_DIR / "fonts" / "LXGWWenKai-Regular.ttf"
CUES_FILE = OUT / "voice_cues_full.json"
FINAL = OUT / f"{MATCH_ID}_final_4k_smooth_blackbar.mp4"

W, H = 3840, 2160
BAR_H, AVATAR_W, AVATAR_H = 272, 280, 252
CANVAS_H = H + BAR_H

ffmpeg = shutil.which("ffmpeg")
ffprobe = shutil.which("ffprobe")
if not ffmpeg:
    packages = Path.home() / "AppData" / "Local" / "Microsoft" / "WinGet" / "Packages"
    ffmpeg = str(next(packages.glob("Gyan.FFmpeg*/ffmpeg-*/bin/ffmpeg.exe")))
    ffprobe = str(Path(ffmpeg).with_name("ffprobe.exe"))


def run(command):
    print(" ".join(str(x) for x in command[:8]), "...", flush=True)
    return subprocess.run([str(x) for x in command]).returncode


def duration(path):
    result = subprocess.run(
        [
            ffprobe,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=nk=1:nw=1",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def atempo_chain(value):
    values = []
    while value > 2.0:
        values.append(2.0)
        value /= 2.0
    while value < 0.5:
        values.append(0.5)
        value /= 0.5
    values.append(value)
    return ",".join(f"atempo={item:.8f}" for item in values)


required = [RAW, OPENING, VOICE, AVATAR, FONT, CUES_FILE]
missing = [str(path) for path in required if not path.exists()]
if missing:
    raise FileNotFoundError("missing inputs: " + "; ".join(missing))

payload = json.loads(CUES_FILE.read_text(encoding="utf-8"))
if not payload.get("text_exact"):
    raise RuntimeError("subtitle text is not an exact copy of the narration markdown")
cues = payload["cues"]
sections = payload["sections"]
audio_duration = float(payload["audio_duration"])

font = ImageFont.truetype(str(FONT), 62)
for character in "鉴杀杂稳":
    if font.getbbox(character) is None:
        raise RuntimeError(f"LXGW WenKai does not cover required glyph: {character}")

def ass_time(value):
    hours = int(value // 3600)
    minutes = int((value % 3600) // 60)
    seconds = value % 60
    return f"{hours}:{minutes:02d}:{seconds:05.2f}"


def ass_text(value):
    value = value.replace("\\", r"\\").replace("{", r"\{").replace("}", r"\}")
    if len(value) > 30:
        split_at = math.ceil(len(value) / 2)
        value = value[:split_at] + r"\N" + value[split_at:]
    return value


ass_path = OUT / f"{MATCH_ID}_kaiti.ass"
ass_lines = [
    "[Script Info]",
    "ScriptType: v4.00+",
    f"PlayResX: {W-AVATAR_W}",
    f"PlayResY: {BAR_H}",
    "WrapStyle: 0",
    "ScaledBorderAndShadow: yes",
    "",
    "[V4+ Styles]",
    "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, "
    "OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, "
    "ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
    "Alignment, MarginL, MarginR, MarginV, Encoding",
    "Style: Default,LXGW WenKai,62,&H00FFFFFF,&H000000FF,&H00000000,"
    "&H00000000,0,0,0,0,100,100,0,0,1,4,0,5,40,40,0,1",
    "",
    "[Events]",
    "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, "
    "Effect, Text",
]
for cue in cues:
    ass_lines.append(
        f"Dialogue: 0,{ass_time(float(cue['s']))},{ass_time(float(cue['e']))},"
        f"Default,,0,0,0,,{ass_text(cue['text'])}"
    )
ass_path.write_text("\n".join(ass_lines) + "\n", encoding="utf-8-sig")

if not RAW_CLEAN.exists() or RAW_CLEAN.stat().st_mtime < RAW.stat().st_mtime:
    clean_common = [
        ffmpeg,
        "-y",
        "-fflags",
        "+discardcorrupt",
        "-err_detect",
        "ignore_err",
        "-i",
        RAW,
        "-vf",
        "fps=30",
        "-af",
        "aresample=async=1:first_pts=0",
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-movflags",
        "+faststart",
    ]
    rc = run(
        clean_common[:-4]
        + ["-c:v", "h264_qsv", "-preset", "faster", "-global_quality", "18"]
        + clean_common[-4:]
        + [RAW_CLEAN]
    )
    if rc:
        rc = run(
            clean_common[:-4]
            + ["-c:v", "libx264", "-preset", "fast", "-crf", "18"]
            + clean_common[-4:]
            + [RAW_CLEAN]
        )
    if rc:
        raise RuntimeError("error-conceal source re-encode failed")

args = [
    ffmpeg,
    "-y",
    "-loglevel",
    "error",
    "-stats",
    "-init_hw_device",
    "qsv=hw,child_device_type=d3d11va",
    "-filter_hw_device",
    "hw",
    "-filter_complex_threads",
    "8",
    "-i",
    OPENING,
    "-i",
    RAW_CLEAN,
    "-stream_loop",
    "-1",
    "-i",
    AVATAR,
    "-i",
    VOICE,
]

game_sections = sections[1:]
audio_labels = "".join(f"[ga{index}]" for index in range(len(game_sections)))
filters = [
    f"[1:a]asplit={len(game_sections)}{audio_labels}",
]

intro_duration = float(sections[0]["target_end"])
intro_factor = intro_duration / 10.0
filters += [
    f"[0:v]trim=4:14,setpts={intro_factor:.8f}*(PTS-STARTPTS),"
    f"scale={W}:{H}:flags=lanczos,setsar=1,fps=30[intro_v]",
    f"[0:a]atrim=4:14,asetpts=PTS-STARTPTS,{atempo_chain(1/intro_factor)},"
    "aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo[intro_a]",
]

game_a = []
video_mappings = []
for index, section in enumerate(game_sections):
    source_start = max(0.0, float(section["source_start"]) - 10.0)
    source_end = max(source_start + 0.1, float(section["source_end"]) - 10.0)
    target_duration = float(section["target_end"]) - float(section["target_start"])
    factor = target_duration / (source_end - source_start)
    target_start = float(section["target_start"]) - intro_duration
    input_time = "(PTS-STARTPTS)*TB"
    video_mappings.append(
        (
            source_end,
            f"{target_start:.8f}+({input_time}-{source_start:.6f})*{factor:.8f}",
        )
    )
    filters.append(
        f"[ga{index}]atrim={source_start:.6f}:{source_end:.6f},"
        f"asetpts=PTS-STARTPTS,{atempo_chain(1/factor)},"
        "aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo"
        f"[as{index}]"
    )
    game_a.append(f"[as{index}]")

video_pts = video_mappings[-1][1]
for source_end, mapping in reversed(video_mappings[:-1]):
    video_pts = f"if(lt((PTS-STARTPTS)*TB,{source_end:.6f}),{mapping},{video_pts})"
last_video_end = video_mappings[-1][0]
filters.append(
    f"[1:v]trim=0:{last_video_end:.6f},"
    f"setpts='({video_pts})/TB',setsar=1,fps=30[game_v]"
)

filters += [
    "[intro_v][game_v]concat=n=2:v=1:a=0[base]",
    "[intro_a]" + "".join(game_a) + f"concat=n={1+len(game_a)}:v=0:a=1,"
    "volume=0.22[bgm]",
    f"[base]pad={W}:{CANVAS_H}:0:0:black[canvas]",
    f"[2:v]format=rgba,scale=-1:{AVATAR_H},fps=30,setpts=PTS-STARTPTS[avatar]",
]

ass_filter_path = ass_path.resolve().as_posix().replace(":", r"\:").replace("'", r"\'")
font_filter_path = FONT.parent.resolve().as_posix().replace(":", r"\:").replace("'", r"\'")
filters += [
    f"color=c=black:s={W-AVATAR_W}x{BAR_H}:r=30:d={audio_duration:.6f},"
    "format=rgba[caption_source]",
    f"[caption_source]subtitles=filename='{ass_filter_path}':"
    f"fontsdir='{font_filter_path}'[caption_bar]",
    f"[canvas][caption_bar]overlay={AVATAR_W}:{H}:shortest=1[barred]",
    f"[barred][avatar]overlay=25:{H+(BAR_H-AVATAR_H)//2}:shortest=0[finalv]",
    "[finalv]format=nv12,hwupload[qsvout]",
]
previous = "qsvout"

filters += [
    "[3:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,"
    "volume=1.0[voice]",
    "[voice][bgm]amix=inputs=2:normalize=0:duration=first[aout]",
]

common = [
    "-filter_complex",
    ";".join(filters),
    "-map",
    f"[{previous}]",
    "-map",
    "[aout]",
    "-t",
    f"{audio_duration:.6f}",
    "-c:a",
    "aac",
    "-b:a",
    "192k",
    "-ar",
    "48000",
    "-ac",
    "2",
    "-movflags",
    "+faststart",
]

print(
    f"compose {MATCH_ID}: {len(cues)} exact-text kaiti cues, "
    f"{len(sections)} video/audio warp segments, {audio_duration:.3f}s",
    flush=True,
)
rc = run(
    args
    + common
    + ["-c:v", "h264_qsv", "-preset", "veryfast", "-global_quality", "21", FINAL]
)
if rc:
    raise SystemExit(rc)
print(f"done: {FINAL}", flush=True)
