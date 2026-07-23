import json
from faster_whisper import WhisperModel
SCR="/private/tmp/claude-501/-Users-lunayuan------Unity-Project-My-project/45d41eac-2071-4e7c-87d5-22d0c17f1395/scratchpad"
m=WhisperModel("large-v3", device="cpu", compute_type="int8")
print("transcribing 42177_full.wav...", flush=True)
segs,info=m.transcribe("/Users/lunayuan/回放/42177_full.wav", language="zh", word_timestamps=True, vad_filter=True,
  initial_prompt="荔枝贡运对抗赛。红队神经突触突击队,蓝队代码即答案。朱雀门,潼关驿,兴庆宫,岭南果园,秦岭栈道,洞庭水驿,洛阳驿,武关,灞桥驿。皇榜任务,鲜度,好果,设卡,核验,冰鉴,快马,栈道复核,码头争船,清障,疾行令。")
out=[{"start":round(s.start,3),"end":round(s.end,3),"text":s.text.strip(),
      "words":[{"w":w.word,"s":round(w.start,3),"e":round(w.end,3)} for w in (s.words or [])]} for s in segs]
json.dump(out, open(f"{SCR}/rec/transcript_full.json","w"), ensure_ascii=False, indent=1)
print(f"done {len(out)} segments", flush=True)
