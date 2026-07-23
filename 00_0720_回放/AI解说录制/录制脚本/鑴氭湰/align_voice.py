import json, re, difflib
SCR="/private/tmp/claude-501/-Users-lunayuan------Unity-Project-My-project/45d41eac-2071-4e7c-87d5-22d0c17f1395/scratchpad"
tr=json.load(open(f"{SCR}/rec/transcript.json"))
sc=json.load(open(f"{SCR}/rec/script_short.json"))
sents=sc["sents"]

# 1) whisper char stream with per-char times
wchars=[]; wtimes=[]
for seg in tr:
    words=seg.get("words") or []
    if words:
        for wd in words:
            w=re.sub(r'\s','',wd["w"]); s=wd["s"]; e=wd["e"]
            n=len(w)
            for i,ch in enumerate(w):
                wchars.append(ch); wtimes.append(s+(e-s)*(i/max(1,n)))
    else:
        t=re.sub(r'\s','',seg["text"]); s=seg["start"]; e=seg["end"]; n=len(t)
        for i,ch in enumerate(t):
            wchars.append(ch); wtimes.append(s+(e-s)*(i/max(1,n)))
wstr="".join(wchars)

# 2) script char stream, keep each char's sentence index; strip punctuation for matching
schars=[]; sidx=[]
for i,st in enumerate(sents):
    for ch in re.sub(r'[，。！？、；：,.!?\s]','',st["text"]):
        schars.append(ch); sidx.append(i)
sstr="".join(schars)

# 3) align script->whisper via matching blocks; map script pos -> whisper time
sm=difflib.SequenceMatcher(None, sstr, wstr, autojunk=False)
blocks=sm.get_matching_blocks()  # (a=script pos, b=whisper pos, size)
# build sorted anchor list of (script_pos -> whisper_time)
anchors=[]
for a,b,size in blocks:
    for k in range(size):
        anchors.append((a+k, wtimes[b+k]))
anchors.sort()
def script_time(pos):
    # nearest-neighbor / linear interp on anchors
    if not anchors: return None
    lo,hi=0,len(anchors)-1
    if pos<=anchors[0][0]: return anchors[0][1]
    if pos>=anchors[-1][0]: return anchors[-1][1]
    import bisect
    xs=[a[0] for a in anchors]
    j=bisect.bisect_left(xs,pos)
    if xs[j]==pos: return anchors[j][1]
    (p0,t0),(p1,t1)=anchors[j-1],anchors[j]
    return t0+(t1-t0)*(pos-p0)/max(1,(p1-p0))

# 4) each sentence's start = script_time at its first char pos
sent_start_pos=[]; pos=0
for i,st in enumerate(sents):
    sent_start_pos.append(pos); pos+=len(re.sub(r'[，。！？、；：,.!?\s]','',st["text"]))
cues=[]
for i,st in enumerate(sents):
    t0=script_time(sent_start_pos[i])
    t1=script_time(sent_start_pos[i+1]) if i+1<len(sents) else wtimes[-1]+0.5
    cues.append({"sec":st["sec"],"anchor":st["anchor"],"text":st["text"],"s":round(t0,2),"e":round(max(t1,t0+0.6),2)})
# enforce monotonic
for i in range(1,len(cues)):
    if cues[i]["s"]<cues[i-1]["s"]: cues[i]["s"]=cues[i-1]["s"]
    if cues[i-1]["e"]>cues[i]["s"]: cues[i-1]["e"]=cues[i]["s"]
json.dump(cues, open(f"{SCR}/rec/voice_cues.json","w"), ensure_ascii=False, indent=1)
print(f"aligned {len(cues)} sentence cues; span {cues[0]['s']}..{cues[-1]['e']}s  (audio~383s)")
for c in cues[:6]+cues[-3:]: print(f"  {c['s']:6.1f}-{c['e']:6.1f}  {c['text'][:30]}")
