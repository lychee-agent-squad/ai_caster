# 42177 TTS Director Exports Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 42177 的 2 倍速解说改成更自然、更具职业游戏解说起伏的统一正文，并派生通用 SSML 1.1 与自然语言导演提示两种配音输入。

**Architecture:** 以新版 UI 对应稿中的 `**解说：**` 段落作为唯一正文主源；纯配音稿、SSML 和导演提示稿全部从这 30 段正文派生并接受逐字同步检查。原始 2 倍速稿只做带哈希校验的备份，不覆盖。

**Tech Stack:** UTF-8 Markdown、SSML 1.1/XML、PowerShell、Python 版 `audit_commentary.py`、Git。

## Global Constraints

- 保留现有 30 段时间范围，首段 `00:00`，末段 `06:18`。
- 不改变回放事实、事件顺序、画面说明、回放锚点、正式队名、数值、比分或胜者。
- 总文字量相对原稿压缩 8%–12%，目标平均密度为 4.30–4.45 口播单位/秒。
- SSML 只使用 `<speak>`、`<p>`、`<s>`、`<prosody>`、`<emphasis>`、`<break>` 标准标签。
- 不在通用 SSML 中使用厂商专属 emotion、style、role 或 effect 标签。
- UI 主稿是唯一正文主源，其余三个版本不得独立改词。
- 原始 UI、纯配音和审计文件必须先备份并通过 SHA-256 一致性校验。
- 清理模板化排比、解释过满、机械转折、连续同句式和助手式引导语。

---

### Task 1: Preserve The Accepted 2x Edition

**Files:**
- Copy: `00_0720_回放/解说稿/42177/42177_2x_ui_synced.md`
- Copy: `00_0720_回放/解说稿/42177/42177_2x_voice_only.md`
- Copy: `00_0720_回放/解说稿/42177/42177_2x_audit.json`
- Create: `00_0720_回放/解说稿/42177/backups/2x_20260721_tts/42177_2x_ui_synced.md`
- Create: `00_0720_回放/解说稿/42177/backups/2x_20260721_tts/42177_2x_voice_only.md`
- Create: `00_0720_回放/解说稿/42177/backups/2x_20260721_tts/42177_2x_audit.json`
- Create: `00_0720_回放/解说稿/42177/backups/2x_20260721_tts/sha256.txt`

**Interfaces:**
- Consumes: the accepted UI, voice-only, and audit files.
- Produces: a byte-identical backup set and a three-entry SHA-256 manifest.

- [ ] **Step 1: Prove the target backup set does not already contain an unchecked replacement**

Run:

```powershell
$backup = 'C:\Users\Administrator\Documents\AI解说\00_0720_回放\解说稿\42177\backups\2x_20260721_tts'
Get-ChildItem -LiteralPath $backup -File -ErrorAction SilentlyContinue
```

Expected: no files, or files whose hashes can be checked against the originals before reuse.

- [ ] **Step 2: Create the backup directory and copy the three originals**

Use `New-Item -ItemType Directory` for the exact backup directory and `Copy-Item -LiteralPath` for each named source. Do not copy the whole `42177` directory and do not delete any existing files.

- [ ] **Step 3: Write the SHA-256 manifest**

Calculate each original and backup with `Get-FileHash -Algorithm SHA256`. Write six labeled lines to `sha256.txt` with `apply_patch`, pairing every source hash with its backup hash.

- [ ] **Step 4: Verify each original/backup pair**

Run a PowerShell comparison that loads all three pairs and throws if any hash differs.

Expected: `BACKUP_HASH_OK=3` and exit code 0.

- [ ] **Step 5: Commit only the backup manifest**

Do not commit the copied accepted scripts unless the repository policy already tracks the match directory. Stage only `sha256.txt` if the three copies remain user delivery artifacts.

---

### Task 2: Create The Revised Canonical UI And Voice Scripts

**Files:**
- Read: `00_0720_回放/解说稿/42177/42177_2x_ui_synced.md`
- Create: `00_0720_回放/解说稿/42177/42177_2x_tts_ui_synced.md`
- Create: `00_0720_回放/解说稿/42177/42177_2x_tts_voice_only.md`
- Create: `00_0720_回放/解说稿/42177/42177_2x_tts_audit.json`

**Interfaces:**
- Consumes: 30 original UI segments and the approved writing constraints.
- Produces: one canonical UI master and one mechanically matching pure voice script.

- [ ] **Step 1: Run the expected-failure existence check**

Run:

```powershell
$root = 'C:\Users\Administrator\Documents\AI解说\00_0720_回放\解说稿\42177'
Test-Path -LiteralPath "$root\42177_2x_tts_ui_synced.md"
Test-Path -LiteralPath "$root\42177_2x_tts_voice_only.md"
```

Expected before creation: both results are `False`.

- [ ] **Step 2: Rewrite the 30 commentary passages in the UI master**

Create the UI master with `apply_patch`. Preserve every heading, time range, `画面` field, and `回放锚点` field. Replace only the 30 `解说` passages. Apply this per-segment delivery curve:

- `00:00-00:48`: confident setup at medium pace; establish teams, objective, and route split without over-explaining.
- `00:48-02:28`: alternate scoring bursts with calmer route analysis; stress score changes and quality loss.
- `02:28-03:04`: tighten the approach to 潼关 and lower the amount of rule exposition.
- `03:04-03:40`: first major crescendo; short active clauses for set, block, score response, and three-wave weakening.
- `03:40-04:16`: release intensity and clearly reset route position, score, and next pressure point.
- `04:16-05:18`: build terminal tension; let waiting and weathering sound restrained rather than continuously loud.
- `05:18-05:52`: relief at the first guard expiry, immediate shock at the second guard, then the fastest decisive action chain.
- `05:52-06:18`: announce delivery with force, slow down for the itemized score, pause, and land the final winner.

- [ ] **Step 3: Derive the pure voice script mechanically**

Copy each revised `**解说：**` passage from the UI master in order into the pure voice file. Keep one blank line between paragraphs. Add no title, timecode, UI description, anchor, source note, or director metadata.

- [ ] **Step 4: Run the commentary audit**

Run:

```powershell
python 'C:\Users\Administrator\.codex\skills\lychee-replay-esports-commentator\scripts\audit_commentary.py' `
  --ui 'C:\Users\Administrator\Documents\AI解说\00_0720_回放\解说稿\42177\42177_2x_tts_ui_synced.md' `
  --voice 'C:\Users\Administrator\Documents\AI解说\00_0720_回放\解说稿\42177\42177_2x_tts_voice_only.md' `
  --max-rate 5.5 `
  --max-average-rate 4.45 `
  --min-segments 30 `
  --max-segments 30 `
  --require '宫宴冲刺' `
  --json 'C:\Users\Administrator\Documents\AI解说\00_0720_回放\解说稿\42177\42177_2x_tts_audit.json'
```

Expected: exit code 0, 30 segments, 30 voice paragraphs, no density or parity failures.

- [ ] **Step 5: Run the manual de-AI scan**

Search the two new Markdown files for `下面我们来|我们可以看到|总的来说|真正重要的是|不是.*而是|不只是.*更是`. Review every `先.*再` match and retain it only when the verified event order changes the result.

Expected: no assistant route markers or unjustified template shells.

- [ ] **Step 6: Commit the canonical scripts and audit**

Stage only the three new `42177_2x_tts_*` files and commit with message `feat: refine 42177 commentary for TTS`.

---

### Task 3: Create And Validate The Generic SSML Export

**Files:**
- Read: `00_0720_回放/解说稿/42177/42177_2x_tts_voice_only.md`
- Create: `00_0720_回放/解说稿/42177/42177_2x_tts_ssml.xml`

**Interfaces:**
- Consumes: the 30 canonical voice paragraphs in order.
- Produces: one XML-valid SSML 1.1 document whose spoken text is identical after tag removal.

- [ ] **Step 1: Run the expected-failure parse check**

Run `[xml](Get-Content -Raw -LiteralPath 'C:\Users\Administrator\Documents\AI解说\00_0720_回放\解说稿\42177\42177_2x_tts_ssml.xml')` before creation.

Expected: file-not-found failure.

- [ ] **Step 2: Create the SSML document**

Use `apply_patch`. Create one `<p xml:id="seg-01">` through `<p xml:id="seg-30">` per segment. Wrap complete sentences in `<s>`. Use `<prosody>` values inside these limits:

- calm setup/analysis: `rate="92%"` to `rate="99%"`, `pitch="-1st"` to `pitch="+0st"`, `volume="medium"`;
- scoring and momentum: `rate="101%"` to `rate="106%"`, `pitch="+1st"`, `volume="medium"`;
- short confrontation bursts: `rate="108%"` to `rate="114%"`, `pitch="+1st"` to `pitch="+2st"`, `volume="loud"`;
- settlement numbers: `rate="92%"` to `rate="96%"`, `pitch="+0st"`, `volume="medium"`.

Use 80–140 ms breaks inside action chains, 180–280 ms after a verified result, and 320–450 ms before the final winner line. Apply `<emphasis level="moderate">` or `strong` only to decisive actions, scores, and the official winner.

- [ ] **Step 3: Validate XML and allowed tags**

Parse with PowerShell `[xml]`. Enumerate all element local names and fail unless the distinct set is exactly within `speak,p,s,prosody,emphasis,break`.

Expected: `XML_OK=True`, 30 `<p>` nodes, and no vendor-specific elements.

- [ ] **Step 4: Validate spoken-text parity**

Read the XML DOM and extract text nodes while ignoring whitespace-only indentation. Normalize paragraph whitespace and compare the 30 resulting strings with the 30 paragraphs in `42177_2x_tts_voice_only.md`.

Expected: `SSML_PARITY_OK=30` and exit code 0.

- [ ] **Step 5: Commit the SSML export**

Stage only `42177_2x_tts_ssml.xml` and commit with message `feat: add generic SSML export for 42177`.

---

### Task 4: Create And Validate The Natural-Language Director Export

**Files:**
- Read: `00_0720_回放/解说稿/42177/42177_2x_tts_ui_synced.md`
- Create: `00_0720_回放/解说稿/42177/42177_2x_tts_director.md`

**Interfaces:**
- Consumes: each UI segment heading and canonical spoken paragraph.
- Produces: 30 director blocks with separate prompt and verbatim script fields.

- [ ] **Step 1: Run the expected-failure existence check**

Run `Test-Path` for the director file.

Expected before creation: `False`.

- [ ] **Step 2: Create the director document**

Use `apply_patch`. Begin with a short usage note: put `导演提示` in the tool's style/instruction field and put only `台词` in the speech field. For each segment, write:

```markdown
## 00:00-00:14 | 开场与队伍介绍

**导演提示：** 情绪、强度、语速、重音、停顿和句尾处理。

**台词：** 与 UI 主稿对应段落逐字一致。
```

Vary the prompts along the approved emotional curve. Do not repeat one generic prompt for all 30 segments. Keep production directions factual and speakable, avoiding imitation of a named real commentator.

- [ ] **Step 3: Validate director-script parity**

Extract all 30 `**台词：**` passages, normalize whitespace, and compare them in order with the 30 paragraphs in `42177_2x_tts_voice_only.md`.

Expected: `DIRECTOR_PARITY_OK=30` and exit code 0.

- [ ] **Step 4: Validate director coverage**

Check that every block includes all six guidance dimensions: emotion, strength, rate, emphasis, pause, and ending treatment. Confirm all 30 original time ranges occur once.

Expected: 30 blocks, 30 unique ranges, and no missing guidance field.

- [ ] **Step 5: Commit the director export**

Stage only `42177_2x_tts_director.md` and commit with message `feat: add natural-language director script for 42177`.

---

### Task 5: Run The Final Delivery Gate

**Files:**
- Verify: all files under `00_0720_回放/解说稿/42177/` named in Tasks 1–4.
- Update: `00_0720_回放/解说稿/42177/42177_2x_tts_audit.json` if the final audit output changes.

**Interfaces:**
- Consumes: backup manifest and all four new delivery files.
- Produces: a verified handoff with no content drift.

- [ ] **Step 1: Re-run the full commentary audit from Task 2**

Expected: exit code 0, `failure_count: 0`, 30 segments, average rate at or below 4.45.

- [ ] **Step 2: Re-run XML and both parity checks from Tasks 3–4**

Expected: `XML_OK=True`, `SSML_PARITY_OK=30`, and `DIRECTOR_PARITY_OK=30`.

- [ ] **Step 3: Re-run backup hash verification**

Expected: `BACKUP_HASH_OK=3`.

- [ ] **Step 4: Manually verify result-critical facts**

Confirm the opening names `神经突触袭击队` and `代码即答案`; the decisive sequence includes 潼关设卡、三轮削弱、朱雀门两次设卡、宫门验核 and 兴庆宫送达; the settlement states `725` to `80`; and the official winner is `神经突触袭击队`.

- [ ] **Step 5: Inspect exact repository changes**

Run `git status --short` and `git diff --stat HEAD`. Confirm no unrelated user files are staged or modified by this work.

- [ ] **Step 6: Commit any final audit-only correction**

If the final audit JSON changed after the previous commit, stage only that file and commit with message `test: verify 42177 TTS exports`. If it did not change, do not create an empty commit.
