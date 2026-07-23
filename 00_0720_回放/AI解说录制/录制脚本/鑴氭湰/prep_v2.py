import json, subprocess, os, re
from PIL import Image, ImageDraw, ImageFont
SCR="/private/tmp/claude-501/-Users-lunayuan------Unity-Project-My-project/45d41eac-2071-4e7c-87d5-22d0c17f1395/scratchpad"
TTS=f"{SCR}/tts"
F=1.35; INTRO=10.5
align=json.load(open(f"{SCR}/rec/align.json")); secs=align["secs"]
# --- new timeline ---
new=[]
for i,s in enumerate(secs):
    if i==0: st,en=0.0, INTRO
    elif i==1: st=INTRO; en=INTRO + F*secs[2]["t"]
    else:
        st=INTRO + F*s["t"]
        en=(INTRO + F*secs[i+1]["t"]) if i+1<len(secs) else round(INTRO + F*s["end_t"],2)
    new.append({"i":i,"t":round(st,2),"end_t":round(en,2),"talk":s["talk"]})
VIDEO_END=new[-1]["end_t"]
json.dump({"F":F,"intro":INTRO,"video_end":VIDEO_END,"secs":new}, open(f"{SCR}/rec/align_v2.json","w"), ensure_ascii=False)

def dur(p):
    r=subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=nk=1:nw=1",p],capture_output=True,text=True)
    try:return float(r.stdout.strip())
    except:return 0.0

# --- narration v2 (catch-up controller, gentler cap) ---
placements=[]; cursor=0.0
for i,s in enumerate(new):
    nd=dur(f"{TTS}/sec_{i:02d}.aiff")
    start=max(s["t"],cursor)
    nextt=new[i+1]["t"] if i+1<len(new) else s["end_t"]
    gap=max(0.5, nextt-start)
    tempo=min(max(nd/gap,1.0),1.45)
    fit=nd/tempo
    placements.append((i,start,tempo,fit)); cursor=start+fit
inputs=[]; filt=[]
for k,(i,start,tempo,fit) in enumerate(placements):
    wav=f"{TTS}/v2_{i:02d}.wav"
    subprocess.run(["ffmpeg","-y","-i",f"{TTS}/sec_{i:02d}.aiff","-filter:a",f"atempo={tempo:.4f}","-ar","44100","-ac","2",wav,"-loglevel","error"])
    inputs+=["-i",wav]; d=int(start*1000); filt.append(f"[{k}]adelay={d}|{d}[a{k}]")
mix=";".join(filt)+";"+"".join(f"[a{k}]" for k in range(len(placements)))+f"amix=inputs={len(placements)}:normalize=0:duration=longest[out]"
subprocess.run(["ffmpeg","-y",*inputs,"-filter_complex",mix,"-map","[out]","-ar","44100","-ac","2",f"{SCR}/rec/narration_v2.wav","-loglevel","error"])
print("narration_v2 end=%.1fs  video_end=%.1fs"%(cursor,VIDEO_END))
print("max tempo:", max(p[2] for p in placements))

# --- subtitle cue PNGs (black-bar layout: full 1920 wide band) ---
SUBS=f"{SCR}/subs_v2"; os.makedirs(SUBS,exist_ok=True)
for x in os.listdir(SUBS): os.remove(os.path.join(SUBS,x))
FONT="/System/Library/AssetsV2/com_apple_MobileAsset_Font8/86ba2c91f017a3749571a82f2c6d890ac7ffb2fb.asset/AssetData/PingFang.ttc"
BARH=170; font=ImageFont.truetype(FONT,52,index=0); MAXC=30
def split_sent(t):
    p=re.findall(r'[^。！？]*[。！？]',t); r=re.sub(r'[^。！？]*[。！？]','',t).strip()
    if r:p.append(r)
    return [x.strip() for x in p if x.strip()]
def wrap(t):
    o=[]
    while len(t)>MAXC: o.append(t[:MAXC]); t=t[MAXC:]
    o.append(t); return o[:2]
meta=[]; idx=0
AVW=190  # avatar reserved width on left of bar
for s in new:
    sents=split_sent(s["talk"]); win=s["end_t"]-s["t"]
    if not sents or win<=0: continue
    W=sum(len(x) for x in sents); t=s["t"]
    for j,sent in enumerate(sents):
        e=s["end_t"] if j==len(sents)-1 else t+win*len(sent)/W
        im=Image.new("RGBA",(1920,BARH),(0,0,0,0)); d=ImageDraw.Draw(im)
        lines=wrap(sent); lh=60; tot=len(lines)*lh; y0=(BARH-tot)//2
        cx=AVW+(1920-AVW)//2   # center in area right of avatar
        for li,ln in enumerate(lines):
            bb=d.textbbox((0,0),ln,font=font,stroke_width=3); w=bb[2]-bb[0]
            d.text((cx-w//2,y0+li*lh),ln,font=font,fill=(255,255,255,255),stroke_width=3,stroke_fill=(0,0,0,255))
        fn=f"{SUBS}/c_{idx:03d}.png"; im.save(fn)
        meta.append({"s":round(t,3),"e":round(e,3),"png":fn}); idx+=1; t=e
json.dump(meta, open(f"{SCR}/subs_meta_v2.json","w"))
print("subtitle cues:",len(meta),"  bar height",BARH)
