# 解说视频制作脚本（归档参考）

配套说明见 `~/回放/录制解说视频_工作流说明.md`。

## 脚本清单
- `cdp.py` — Chrome 调试协议(CDP)驱动：eval / click / screenshot / key / navigate。所有录制驱动的底座。
- `record_v6.py` — **录制器**：干净开局 R5、H.264 硬件编码 4K + 游戏音、金占比检测结算自动停、单块整体上传。
- `align_voice.py` — 字幕对齐：把稿子原文按 whisper 字级时间戳贴到你的配音上（零错字）。
- `transcribe_full.py` — faster-whisper large-v3 转写（拿时间戳；也能纯转写当字幕）。
- `render_subs.py` / `prep_v2.py` — 字幕 PNG 渲染（无 libass，用 PIL 渲染 + overlay）。
- `compose_v6.py`（`compose_v4.py` 是基版）— **最终合成**：片头 + 放慢游戏 + 黑条 + 讲解员 + 字幕 + 配音 + 背景音 → 4K。
- `upload_server.py` — 本地上传接收（浏览器把录屏落盘到磁盘），端口 8091。

## ⚠️ 重要
这些是**参考脚本**，里面写死了：
1. 会话专属的临时目录路径（`SCR=/private/tmp/claude-501/.../scratchpad`）——换机器/会话要改。
2. 该局专属文件名（`42177_full.wav`、`m42177/`、FSPTS 数值等）——换局要改。

做新局时最省事的办法：把新的 `replay.txt`＋队名＋你的配音＋字幕稿给我，我在新会话里复用这套逻辑、改好路径直接跑。
