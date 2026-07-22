# C 地图 330 秒解说稿刷新实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 C 地图 42177–42204 的正式 2 倍速解说重构为不超过 330 秒的可剪辑节目稿，删除不再需要的旧版、SSML 和导演稿，并为每局补齐源 `replay.txt`、`data.csv`。

**Architecture:** 以现有 `_2x_tts_ui_synced.md` 为事实完整稿，先生成可回退备份，再通过逐段优先级和人工连续性复核构建剪辑时间轴。节目段保留原始 2 倍速源范围，纯口播从主稿机械派生；批量审计独立验证时长、密度、身份、赛果、文件清洁度和源文件哈希。

**Tech Stack:** Python 3、PowerShell、Markdown、JSON、现有 `lychee-replay-esports-commentator` 审计器、unittest。

## Global Constraints

- 每局节目时间轴从 `00:00` 连续开始，终点不得超过 `05:30`。
- 开场和结算合计约 30 秒，比赛主体使用原始 2 倍速素材且约 5 分钟。
- 不得按比例缩放旧时间码或改变源回放速度。
- 每段必须保留时间递增的原始 2 倍速源范围或截图锚点。
- 平均口播密度不超过 4.8，单段不超过 5.5 个口播单位/秒。
- 修改或删除前必须完成 SHA-256 备份校验。
- 最终只保留 `_2x_tts_ui_synced.md`、`_2x_tts_voice_only.md` 和相关审计，不保留旧版 UI/口播、SSML、导演稿。
- 每局根目录必须包含与源文件哈希一致的 `replay.txt`、`data.csv`。

---

### Task 1: 建立 330 秒批处理安全工具

**Files:**
- Create: `tools/refresh_c_map_330s.py`
- Create: `tools/tests/test_refresh_c_map_330s.py`

**Interfaces:**
- Consumes: C 地图输出根目录、源场次根目录、每局现有 UI 稿。
- Produces: `parse_ui(path) -> list[Segment]`、`build_cut_timeline(segments, limit=330) -> list[Segment]`、`backup_files(...)`、`copy_source_files(...)` 和安全删除清单。

- [ ] **Step 1: 写失败测试**

```python
def test_cut_timeline_is_contiguous_and_at_most_330_seconds():
    result = build_cut_timeline(sample_segments, limit=330)
    assert result[0].program_start == 0
    assert result[-1].program_end <= 330
    assert all(a.program_end == b.program_start for a, b in zip(result, result[1:]))

def test_backup_hash_must_match_before_delete():
    manifest = backup_files([source], backup_root)
    assert manifest[0]["source_sha256"] == manifest[0]["backup_sha256"]

def test_copied_replay_and_data_match_sources():
    copied = copy_source_files(source_match, output_match)
    assert copied["replay.txt"]["matched"] is True
    assert copied["data.csv"]["matched"] is True
```

- [ ] **Step 2: 运行测试确认失败**

Run: `python -m unittest tools.tests.test_refresh_c_map_330s -v`

Expected: FAIL，因为 `refresh_c_map_330s` 尚不存在。

- [ ] **Step 3: 实现解析、剪辑、备份、复制和删除保护**

实现不可变 `Segment` 数据结构；剪辑优先保留开场、送达、结算、对抗、任务、资源阈值和结果变化，优先移除重复等待和无事件移动。任何删除必须接收已通过哈希验证的备份清单。

- [ ] **Step 4: 运行测试确认通过**

Run: `python -m unittest tools.tests.test_refresh_c_map_330s -v`

Expected: PASS。

### Task 2: 增加 C 地图纯口播派生模式

**Files:**
- Modify: `tools/generate_lychee_tts_exports.py`
- Modify: `tools/tests/test_generate_lychee_tts_exports.py`

**Interfaces:**
- Consumes: 完成后的 `_2x_tts_ui_synced.md`。
- Produces: `_2x_tts_voice_only.md` 和只包含口播一致性/清洁度的 export checks；原有 B 地图 SSML/导演稿参数行为保持兼容。

- [ ] **Step 1: 写失败测试**

```python
def test_voice_only_mode_does_not_create_ssml_or_director(self):
    result = run_generator("--voice-only")
    self.assertEqual(result.returncode, 0)
    self.assertTrue(voice.exists())
    self.assertFalse(ssml.exists())
    self.assertFalse(director.exists())
```

- [ ] **Step 2: 运行测试确认失败**

Run: `python -m unittest tools.tests.test_generate_lychee_tts_exports -v`

Expected: 新测试 FAIL，现有兼容测试 PASS。

- [ ] **Step 3: 实现 `--voice-only` 模式**

该模式只机械提取 `**解说：**` 段落并输出 `voice_parity`、AI 模板命中、歧义代词和长句检查；不创建 SSML 或导演稿。

- [ ] **Step 4: 运行完整工具测试**

Run: `python -m unittest discover tools/tests -v`

Expected: PASS。

### Task 3: 建立 500ms 回放帧证据门槛

**Files:**
- Modify: `tools/refresh_c_map_330s.py`
- Modify: `tools/tests/test_refresh_c_map_330s.py`
- Reuse: `tools/make_replay_contact_sheets.py`

**Interfaces:**
- Consumes: 每局保留段的原始 2 倍速源起止时间、现有截图时间戳。
- Produces: 每局帧覆盖报告；边界附近无可用帧的场次进入 500ms 重采集清单。

- [ ] **Step 1: 写失败测试**

```python
def test_frame_gap_over_threshold_requires_recapture():
    report = audit_frame_support([0, 2000, 4000], required_boundaries=[750])
    assert report.requires_recapture is True

def test_half_second_frames_cover_cut_boundaries():
    report = audit_frame_support(range(0, 5001, 500), required_boundaries=[750, 2750])
    assert report.requires_recapture is False
```

- [ ] **Step 2: 运行测试确认失败**

Run: `python -m unittest tools.tests.test_refresh_c_map_330s -v`

Expected: 新帧门槛测试 FAIL。

- [ ] **Step 3: 实现帧覆盖审计**

切点两侧必须能由现有帧和回放锚点确认；无法确认时才启动该场次 2 倍速、500ms 间隔重采集。重采集不得覆盖旧帧，写入独立目录和 capture manifest。

- [ ] **Step 4: 运行测试确认通过**

Run: `python -m unittest tools.tests.test_refresh_c_map_330s -v`

Expected: PASS。

### Task 4: 逐局生成并复核 330 秒主稿

**Files:**
- Modify: `00_0720_回放/解说稿/42177/42177_2x_tts_ui_synced.md` through `42204/42204_2x_tts_ui_synced.md`
- Create: `00_0720_回放/解说稿/C地图_330s_剪辑映射.json`

**Interfaces:**
- Consumes: 现有主稿、时间线、证据、回放帧、`replay.txt`、`data.csv`。
- Produces: 28 份连续、可追溯、不超过 330 秒的正式主稿和源范围映射。

- [ ] **Step 1: 生成候选剪辑映射**

Run: `python tools/refresh_c_map_330s.py plan --root "00_0720_回放/解说稿" --source-root "00_0720_回放/C地图对战结果/output_c_071805/LitchiDelivery_C" --limit 330`

Expected: 28 个候选映射，全部按源时间递增，无源事实改写。

- [ ] **Step 2: 完成内容连续性复核**

逐局检查双方动作、事件结果、直接后果、比分、平局/胜者；合并造成主语或因果缺失的段落必须重写，不能仅删除连接上下文。

- [ ] **Step 3: 执行帧证据审计和必要重采集**

Run: `python tools/refresh_c_map_330s.py frames --plan "00_0720_回放/解说稿/C地图_330s_剪辑映射.json" --interval-ms 500`

Expected: 现有证据足够的场次直接通过；不足场次写入明确重采集清单并在重采集后通过。

- [ ] **Step 4: 写入主稿**

Run: `python tools/refresh_c_map_330s.py apply --plan "00_0720_回放/解说稿/C地图_330s_剪辑映射.json"`

Expected: 28 份主稿时间连续、终点均不超过 330 秒。

### Task 5: 备份、复制、派生和清理活动目录

**Files:**
- Create: `00_0720_回放/解说稿/backups/2x_330s_20260722_before_edit/backup_manifest.json`
- Create: 每局 `replay.txt`、`data.csv`
- Modify: 每局 `_2x_tts_voice_only.md`、`_2x_tts_export_checks.json`
- Delete after verified backup: 旧版 `_2x_ui_synced.md`、旧版 `_2x_voice_only.md`、旧版 `_2x_audit.json`、全部 `_2x_tts_ssml.xml`、全部 `_2x_tts_director.md`

**Interfaces:**
- Consumes: 已批准的正式主稿和源 server 文件。
- Produces: 精简后的活动目录和可恢复备份。

- [ ] **Step 1: 创建并验证备份**

Run: `python tools/refresh_c_map_330s.py backup --root "00_0720_回放/解说稿"`

Expected: 所有 source/backup SHA-256 相同，零失败。

- [ ] **Step 2: 复制源回放文件**

Run: `python tools/refresh_c_map_330s.py copy-sources --source-root "00_0720_回放/C地图对战结果/output_c_071805/LitchiDelivery_C" --root "00_0720_回放/解说稿"`

Expected: 28 份 `replay.txt` 和 28 份 `data.csv` 哈希匹配。

- [ ] **Step 3: 派生纯口播和检查文件**

Run: `python tools/refresh_c_map_330s.py derive --root "00_0720_回放/解说稿"`

Expected: 28/28 UI/口播一致。

- [ ] **Step 4: 执行受保护清理**

Run: `python tools/refresh_c_map_330s.py clean --root "00_0720_回放/解说稿" --manifest "00_0720_回放/解说稿/backups/2x_330s_20260722_before_edit/backup_manifest.json"`

Expected: 只删除清单内且已验证备份的精确文件。

### Task 6: 更新并运行 C 地图批量审计

**Files:**
- Modify: `tools/audit_lychee_tts_batch.py`
- Modify: `00_0720_回放/解说稿/C地图_2x_tts_批量审计汇总.json`
- Modify: `00_0720_回放/解说稿/C地图_42177-42204_批量制作验收报告.md`

**Interfaces:**
- Consumes: 28 份正式 UI 主稿、口播、源身份和复制文件。
- Produces: 新批量汇总和人工验收报告。

- [ ] **Step 1: 为新审计条件写测试或 dry-run 断言**

断言命令包含 `--max-timeline-seconds 330`、`--require-live-style`，并且不再读取 SSML/导演稿字段。

- [ ] **Step 2: 更新批量审计器**

段数范围改为 18–26；汇总新增 `timeline_end_seconds`、`voice_spoken_units`、平均/最大密度和源文件哈希状态。

- [ ] **Step 3: 运行批量审计**

Run: `python tools/audit_lychee_tts_batch.py`

Expected: `matches_total=28`、`passed=28`、`failed=0`。

- [ ] **Step 4: 运行最终文件清洁度检查**

Run: `python tools/refresh_c_map_330s.py verify --root "00_0720_回放/解说稿" --source-root "00_0720_回放/C地图对战结果/output_c_071805/LitchiDelivery_C"`

Expected: 28 个时间轴通过、56 个源文件哈希通过、旧版/SSML/导演稿活动文件计数为零、备份哈希零失败。

### Task 7: 最终人工复核与交付

**Files:**
- Review: 28 份 `_2x_tts_ui_synced.md`
- Review: 批量审计汇总、剪辑映射、备份清单和验收报告

**Interfaces:**
- Consumes: 自动审计通过的完整批次。
- Produces: 可交付结论和异常清单（必须为空才能宣称完成）。

- [ ] **Step 1: 抽查最短、最长、平局、结果反转和高对抗局**

检查源顺序、双方动作、比分、胜者、片段衔接和节目节奏。

- [ ] **Step 2: 核对 28 局结束时间分布**

所有终点应自然落在关键结算完成处且不超过 330 秒，不为凑整强行填充空段。

- [ ] **Step 3: 运行全套工具测试和最终验证**

Run: `python -m unittest discover tools/tests -v`

Run: `python tools/audit_lychee_tts_batch.py`

Run: `python tools/refresh_c_map_330s.py verify --root "00_0720_回放/解说稿" --source-root "00_0720_回放/C地图对战结果/output_c_071805/LitchiDelivery_C"`

Expected: 所有测试通过，批量审计 28/28，通过项无失败。
