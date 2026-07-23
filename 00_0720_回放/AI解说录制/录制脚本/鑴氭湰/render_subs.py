import re, os, json
from PIL import Image, ImageDraw, ImageFont
SCR="/private/tmp/claude-501/-Users-lunayuan------Unity-Project-My-project/45d41eac-2071-4e7c-87d5-22d0c17f1395/scratchpad"
SUBS=f"{SCR}/subs_png"; os.makedirs(SUBS,exist_ok=True)
for x in os.listdir(SUBS): os.remove(os.path.join(SUBS,x))
FONT="/System/Library/AssetsV2/com_apple_MobileAsset_Font8/86ba2c91f017a3749571a82f2c6d890ac7ffb2fb.asset/AssetData/PingFang.ttc"
font=ImageFont.truetype(FONT, 46, index=0)
W=1920; PANEL_H=230; MAXCHARS=26
def parse_srt(p):
    cues=[]; blk=open(p,encoding="utf-8").read().strip().split("\n\n")
    for b in blk:
        L=b.strip().split("\n")
        if len(L)<3: continue
        m=re.search(r'(\d+):(\d+):(\d+),(\d+)\s*-->\s*(\d+):(\d+):(\d+),(\d+)',L[1])
        if not m: continue
        s=int(m.group(1))*3600+int(m.group(2))*60+int(m.group(3))+int(m.group(4))/1000
        e=int(m.group(5))*3600+int(m.group(6))*60+int(m.group(7))+int(m.group(8))/1000
        cues.append((s,e,"".join(L[2:])))
    return cues
def wrap(t):
    lines=[]; 
    while len(t)>MAXCHARS:
        lines.append(t[:MAXCHARS]); t=t[MAXCHARS:]
    lines.append(t); return lines[:3]
cues=parse_srt(f"{SCR}/rec/42177_aligned.srt")
meta=[]
for i,(s,e,txt) in enumerate(cues):
    im=Image.new("RGBA",(W,PANEL_H),(0,0,0,0)); d=ImageDraw.Draw(im)
    lines=wrap(txt); lh=58; total=len(lines)*lh; y0=PANEL_H-total-6
    for j,ln in enumerate(lines):
        bb=d.textbbox((0,0),ln,font=font,stroke_width=4); w=bb[2]-bb[0]
        d.text(((W-w)//2, y0+j*lh), ln, font=font, fill=(255,255,255,255),
               stroke_width=4, stroke_fill=(0,0,0,235))
    fn=f"{SUBS}/cue_{i:03d}.png"; im.save(fn)
    meta.append({"i":i,"s":round(s,3),"e":round(e,3),"png":fn})
json.dump(meta, open(f"{SCR}/subs_meta.json","w"))
print(f"rendered {len(meta)} subtitle PNGs, panel {W}x{PANEL_H}")
