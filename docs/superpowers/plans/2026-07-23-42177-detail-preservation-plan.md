# 42177 Detail-Preserving 330-Second Commentary Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 C 地图 42177 重构为严格 05:30、动态事件分段、对战细节完整的 2 倍速 UI 对应稿和纯配音稿。

**Architecture:** `42177_2x_tts_ui_synced.md` 是唯一母稿；路线与事件事实来自 `map4_config.json`、`replay.txt`、现有时间线和 500ms UI 帧证据。纯配音稿由现有导出工具机械提取，审计结果由解说 skill 的确定性检查器生成。

**Tech Stack:** UTF-8 Markdown、JSON、PowerShell、Python 3、`lychee-replay-esports-commentator` scripts。

## Global Constraints

- 节目时间轴从 `00:00` 连续到严格 `05:30`。
- 开场动画、对战面板/岭南果园、首次行动与选路分别成段。
- 兴庆宫送达过程与最终结算看板分别成段。
- 不删除任何改变路线、资源、任务分、鲜度、通行权或交付结果的事件。
- 使用实际事件和画面切换动态分段，不使用固定 16 秒网格。
- UI 对应稿是唯一母稿；纯配音稿只能机械派生。
- 不修改 `replay.txt`、`data.csv`、截图和捕获清单。

---

### Task 1: 保存当前正式稿并建立细节覆盖清单

**Files:**
- Create: `00_0720_回放/解说稿/42177/backups/2x_20260723_before_detail_restore/42177_2x_tts_ui_synced.md`
- Create: `00_0720_回放/解说稿/42177/backups/2x_20260723_before_detail_restore/42177_2x_tts_voice_only.md`
- Create: `00_0720_回放/解说稿/42177/backups/2x_20260723_before_detail_restore/sha256.txt`
- Modify: `00_0720_回放/解说稿/42177/42177_evidence.md`

**Interfaces:**
- Consumes: 当前活动 UI 稿、纯配音稿、旧版详细稿、330 秒裁剪报告。
- Produces: 可恢复的哈希备份；六个已删除段与用户新增门禁的逐项覆盖表。

- [ ] **Step 1: 复制两份活动稿到专用备份目录**

Run:

```powershell
$src = 'C:\Users\Administrator\Documents\AI解说\00_0720_回放\解说稿\42177'
$dst = Join-Path $src 'backups\2x_20260723_before_detail_restore'
New-Item -ItemType Directory -Force -Path $dst
Copy-Item -LiteralPath (Join-Path $src '42177_2x_tts_ui_synced.md') -Destination $dst
Copy-Item -LiteralPath (Join-Path $src '42177_2x_tts_voice_only.md') -Destination $dst
```

Expected: 备份目录中出现两份同名文件。

- [ ] **Step 2: 生成并验证 SHA-256**

Run:

```powershell
$src = 'C:\Users\Administrator\Documents\AI解说\00_0720_回放\解说稿\42177'
$dst = Join-Path $src 'backups\2x_20260723_before_detail_restore'
$names = @('42177_2x_tts_ui_synced.md','42177_2x_tts_voice_only.md')
$rows = foreach ($name in $names) {
  $a = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $src $name)).Hash.ToLower()
  $b = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $dst $name)).Hash.ToLower()
  if ($a -ne $b) { throw "backup hash mismatch: $name" }
  "$a  $name"
}
Set-Content -Encoding utf8 -LiteralPath (Join-Path $dst 'sha256.txt') -Value $rows
```

Expected: 命令成功，原件与备份逐对一致。

- [ ] **Step 3: 在证据文件中追加覆盖表**

Use `apply_patch` to add rows for route split, first bad-fruit threshold, palace-front scout/transfer, first gate weathering, first gate removal, delivery/settlement separation, and the task/resource/freshness/squad/guard/window/same-round/waiting gates.

Expected: 每个要求都有 `回放锚点`、`UI 证据`、`主稿段名` 和 `状态` 字段。

### Task 2: 重建 32 段动态节目时间轴

**Files:**
- Modify: `00_0720_回放/解说稿/42177/42177_2x_tts_ui_synced.md`
- Read: `00_0720_回放/解说稿/42177/replay.txt`
- Read: `00_0720_回放/解说稿/42177/42177_timeline.md`
- Read: `00_0720_回放/LycheeReplay_WebGL_20260720_181945_Linux/LycheeReplay_WebGL_20260720_181945_Linux/StreamingAssets/Tournament/map4_config.json`

**Interfaces:**
- Consumes: Task 1 覆盖表和备份；旧版详细稿中的已验证事件链。
- Produces: 严格 05:30、约 32 段、源画面范围递增的 UI 母稿。

- [ ] **Step 1: 核对开场三种画面和本场路线配置**

Inspect the 500ms opening frames and extract the active C-map edge values for E15, E01, E12, E16, E17, E19, E05, E06, E24 and every route named in the script.

Expected: 对每次重要选路能回答路线边、目标站点、类型、距离、移动消耗、鲜度消耗和沿线处理。

- [ ] **Step 2: 建立连续动态时间码**

Use these structural anchors while allowing event-sized durations between them:

```text
00:00-00:04 开场动画与正式队名
00:04-00:08 对战面板与岭南果园目标
00:08-00:22 首次行动与开局分路
05:13-05:18 宫门验核、疾行令与进宫
05:18-05:22 兴庆宫送达
05:22-05:30 最终结算看板
```

Between `00:22` and `05:13`, allocate event-sized segments to every verified gameplay beat. Do not use a fixed 16-second grid.

Expected: First start `00:00`, final end `05:30`, adjacent boundaries equal, 30–34 total segments.

- [ ] **Step 3: Rewrite the UI master with complete event chains**

Use `apply_patch` to replace the current 24-segment script. Restore all six dropped source segments and preserve task, resource, freshness, squad, guard, waiting, verification and delivery chains under the spec.

Expected: No headings combine opening animation with match panel/orchard, or delivery with settlement board.

- [ ] **Step 4: Run a structural pre-audit**

Run:

```powershell
python 'C:\Users\Administrator\.codex\skills\lychee-replay-esports-commentator\scripts\audit_commentary.py' --ui 'C:\Users\Administrator\Documents\AI解说\00_0720_回放\解说稿\42177\42177_2x_tts_ui_synced.md' --voice 'C:\Users\Administrator\Documents\AI解说\00_0720_回放\解说稿\42177\42177_2x_tts_voice_only.md' --max-rate 5.5 --max-average-rate 4.8 --max-timeline-seconds 330 --min-segments 30 --max-segments 34 --require-live-style --team-roster 'C:\Users\Administrator\.codex\skills\lychee-replay-esports-commentator\references\team-roster.md' --team-id 2707 --team-id 2804 --winner-id 2707 --ui-alias AAAA --ui-alias litchi-runner --require '宫宴冲刺'
```

Expected: parity may fail before Task 3; timeline, segment count and per-segment density must already pass.

### Task 3: 机械派生纯配音稿并运行确定性审计

**Files:**
- Modify: `00_0720_回放/解说稿/42177/42177_2x_tts_voice_only.md`
- Modify: `00_0720_回放/解说稿/42177/42177_2x_tts_export_checks.json`
- Modify: `00_0720_回放/解说稿/42177/42177_2x_tts_audit.json`

**Interfaces:**
- Consumes: Task 2 完成的 UI 母稿。
- Produces: 与母稿逐字一致的纯配音稿和机器审计结果。

- [ ] **Step 1: Mechanical voice derivation**

Run:

```powershell
python 'C:\Users\Administrator\Documents\AI解说\tools\generate_lychee_tts_exports.py' --match-id 42177 --ui 'C:\Users\Administrator\Documents\AI解说\00_0720_回放\解说稿\42177\42177_2x_tts_ui_synced.md' --voice 'C:\Users\Administrator\Documents\AI解说\00_0720_回放\解说稿\42177\42177_2x_tts_voice_only.md' --report 'C:\Users\Administrator\Documents\AI解说\00_0720_回放\解说稿\42177\42177_2x_tts_export_checks.json' --voice-only
```

Expected: report shows commentary parity and voice cleanliness pass.

- [ ] **Step 2: Full commentary audit**

Run the Task 2 audit command with `--json` and write stdout to `42177_2x_tts_audit.json`.

Expected: audit exits 0; timeline end 330, segments 30–34, max rate ≤ 5.5, average rate ≤ 4.8, team and winner checks pass.

- [ ] **Step 3: Run export tool tests**

Run:

```powershell
python -m unittest 'C:\Users\Administrator\Documents\AI解说\tools\tests\test_generate_lychee_tts_exports.py'
```

Expected: all tests pass.

### Task 4: Manual detail gate and status update

**Files:**
- Modify: `00_0720_回放/解说稿/42177/42177_evidence.md`
- Modify: `00_0720_回放/解说稿/42177/42177_status.md`

**Interfaces:**
- Consumes: audited UI/voice editions from Task 3.
- Produces: completed evidence coverage and accurate delivery status.

- [ ] **Step 1: Read the full voice script in order**

Verify every adjacent paragraph advances a visible state; every route claim has a baseline; every resource change has a cause; every unfinished guard, transfer, waiting and movement process reaches a verified exit state.

Expected: zero ambiguous subjects, bare score changes, unbounded intent claims or off-screen conclusions.

- [ ] **Step 2: Check user-specific forbidden compressions**

Run:

```powershell
rg -n '双方继续推进|连续出现数次平局|连续出现四次平局|已经决定全程|送达与最终结算|开场与队伍介绍' 'C:\Users\Administrator\Documents\AI解说\00_0720_回放\解说稿\42177\42177_2x_tts_ui_synced.md' 'C:\Users\Administrator\Documents\AI解说\00_0720_回放\解说稿\42177\42177_2x_tts_voice_only.md'
```

Expected: zero hits.

- [ ] **Step 3: Complete evidence and status**

Use `apply_patch` to mark every coverage row `PASS` and state that the active editions are 05:30, dynamically segmented, detail-preserving and derived from the same UI master.

Expected: status agrees with actual audit results and does not claim unperformed recapture.

- [ ] **Step 4: Inspect final diff**

Run:

```powershell
git diff --check -- '00_0720_回放/解说稿/42177' 'docs/superpowers/specs/2026-07-23-42177-detail-preservation-design.md' 'docs/superpowers/plans/2026-07-23-42177-detail-preservation-plan.md'
git diff --stat -- '00_0720_回放/解说稿/42177' 'docs/superpowers/specs/2026-07-23-42177-detail-preservation-design.md' 'docs/superpowers/plans/2026-07-23-42177-detail-preservation-plan.md'
```

Expected: no whitespace errors; only 42177 commentary/evidence/status plus the approved spec and plan changed.
