from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class SkillContractTests(unittest.TestCase):
    def test_requires_taskbook_interpretation_matrix(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        reference = ROOT / "references" / "taskbook-interpretation.md"

        self.assertTrue(reference.is_file(), "missing taskbook interpretation reference")
        text = reference.read_text(encoding="utf-8")
        self.assertIn("Task-Book Interpretation Gate", skill)
        self.assertIn("规则矩阵", text)
        for column in ("前置条件", "成功结果", "业务拒绝", "非法动作", "回放事件", "UI 证据", "解说含义"):
            self.assertIn(column, text)

    def test_requires_human_playback_states(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        playback = (ROOT / "references" / "playback-sync.md").read_text(encoding="utf-8")

        self.assertIn("Human Playback Gate", skill)
        for state in (
            "UI_NOT_OPEN",
            "WAITING_FOR_SPEED_CONFIRMATION",
            "WAITING_FOR_REPLAY_CONFIRMATION",
            "OBSERVING",
            "COVERAGE_AUDIT",
            "RECAPTURE_REQUIRED",
            "COMPLETE",
        ):
            self.assertIn(state, playback)
        self.assertIn("倍速已确认", playback)
        self.assertIn("已开始", playback)

    def test_commentary_style_requires_event_first_and_settlement_close(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(encoding="utf-8")

        self.assertIn("Event Before Judgment", style)
        self.assertIn("introduce an action before explaining its result", style)
        self.assertIn("Do not announce a decisive turning point before the decisive action happens", style)
        self.assertIn("End on settlement data and the official winner", style)
        self.assertIn("Do not add a post-match thematic summary unless the user requests one", style)

    def test_commentary_style_forbids_spoken_frame_callouts(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(encoding="utf-8")

        self.assertIn("No Spoken Frame Callouts", style)
        self.assertIn("Pure spoken commentary must not contain replay frame or round numbers", style)
        self.assertIn("Keep exact frame and round identifiers in evidence notes", style)

    def test_commentary_style_requires_lead_broadcast_persona_and_both_sides(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        style = (ROOT / "references" / "commentary-style.md").read_text(encoding="utf-8")
        events = (ROOT / "references" / "event-contract.md").read_text(encoding="utf-8")

        self.assertIn("lead Chinese esports play-by-play commentator and analyst", skill)
        self.assertIn("Lead Esports Broadcast Persona", style)
        self.assertIn("For every confrontation, state what both sides are doing", style)
        self.assertIn("A draw grants no handling right", style)
        self.assertIn("After a draw, inspect both teams' next verified actions", style)
        self.assertIn("Do not say that a team won or received the handling right", events)

    def test_commentary_style_requires_miller_inspired_research_model(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        style = (ROOT / "references" / "commentary-style.md").read_text(encoding="utf-8")
        study_path = ROOT / "references" / "lol-caster-study.md"

        self.assertTrue(study_path.is_file(), "missing researched LOL caster study")
        study = study_path.read_text(encoding="utf-8")
        self.assertIn("references/lol-caster-study.md", skill)
        self.assertIn("Miller-Inspired Lead Call Model", style)
        self.assertIn("setup -> trigger -> action chain -> result -> consequence -> reset", style)
        self.assertIn("Learn the method; never imitate signature lines", style)
        self.assertIn("米勒", study)
        self.assertIn("官方赛事样本", study)
        self.assertIn("play-by-play", study)
        self.assertIn("color commentary", study)
        self.assertIn("信息精简", study)

    def test_commentary_style_keeps_business_rejection_internal(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(encoding="utf-8")

        self.assertIn("Internal Rejection Terms Stay Off Air", style)
        self.assertIn("Never say `业务拒绝` in spoken commentary", style)
        self.assertIn("动作被拒绝", style)
        self.assertIn("这次尝试没有生效", style)
        self.assertIn("Do not explain whether it counts as an illegal action or direct penalty", style)
        self.assertIn("unless that classification changes the visible score or official result", style)

    def test_event_contract_derives_contest_costs_from_actual_cards(self) -> None:
        events = (ROOT / "references" / "event-contract.md").read_text(encoding="utf-8")

        self.assertIn("Contest Cost Accounting", events)
        self.assertIn("Three beats do not automatically mean three baskets of good fruit", events)
        self.assertIn("revealed card sequence", events)
        self.assertIn("player-state deltas", events)
        self.assertIn("Never reuse the cost sentence from an earlier replay", events)

    def test_event_contract_distinguishes_guard_timing_and_route_state(self) -> None:
        events = (ROOT / "references" / "event-contract.md").read_text(encoding="utf-8")

        self.assertIn("Guard Timing And Route State", events)
        self.assertIn("current node, movement state, target edge, and edge progress", events)
        self.assertIn("pre-emptive route denial", events)
        self.assertIn("mid-route block", events)
        self.assertIn("Do not say `被堵在半路`", events)

    def test_event_contract_supports_bounded_tactical_intent(self) -> None:
        events = (ROOT / "references" / "event-contract.md").read_text(encoding="utf-8")

        self.assertIn("Evidence-Backed Tactical Intent", events)
        self.assertIn("public opponent state, repeated `WAIT` choices, and an immediate counter-action", events)
        self.assertIn("tactical hold", events)
        self.assertIn("明显在留手", events)
        self.assertIn("Do not turn a supported inference into certainty", events)

    def test_event_contract_tracks_both_sides_until_they_exit_a_highlight(self) -> None:
        events = (ROOT / "references" / "event-contract.md").read_text(encoding="utf-8")

        self.assertIn("Confrontation Exit State", events)
        self.assertIn("defender's next process, repeated guard, wait, or departure", events)
        self.assertIn("attacker's rest, follow-up break, wait, or actual route entry", events)
        self.assertIn("route reopened", events)
        self.assertIn("does not mean the attacker immediately departed", events)

    def test_event_contract_preserves_same_round_parallel_actions(self) -> None:
        events = (ROOT / "references" / "event-contract.md").read_text(encoding="utf-8")

        self.assertIn("Same-Round Parallel Actions", events)
        self.assertIn("do not create a causal sequence from message order", events)
        self.assertIn("simultaneously", events)
        self.assertIn("without waiting for the opponent's result", events)

    def test_event_contract_separates_choice_from_mandatory_consequence(self) -> None:
        events = (ROOT / "references" / "event-contract.md").read_text(encoding="utf-8")

        self.assertIn("Choice Versus Mandatory Consequence", events)
        self.assertIn("chosen investment", events)
        self.assertIn("rule-forced consequence", events)
        self.assertIn("Do not describe mandatory rest as a voluntary strategy", events)

    def test_contract_distinguishes_voluntary_wait_and_requires_explicit_team_subjects(self) -> None:
        events = (ROOT / "references" / "event-contract.md").read_text(encoding="utf-8")
        style = (ROOT / "references" / "commentary-style.md").read_text(encoding="utf-8")

        self.assertIn("Voluntary Wait And Unknown Motivation", events)
        self.assertIn("`IDLE` followed by an explicit `WAIT`", events)
        self.assertIn("strategy choice rather than a rule restriction", events)
        self.assertIn("Do not invent the reason for waiting", events)
        self.assertIn("Explicit Team Subjects", style)
        self.assertIn("repeat `红队` or `蓝队`", style)
        self.assertIn("ambiguous pronouns", style)

    def test_commentary_style_supports_light_fact_anchored_banter(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(encoding="utf-8")

        self.assertIn("Light Broadcast Banter", style)
        self.assertIn("one short line", style)
        self.assertIn("蓝队已经具备通行条件，却没有马上驶向潼关", style)
        self.assertIn("这个选择看起来有些反常，但蓝队大概有自己的理由", style)
        self.assertIn("红队可没有停下来等待", style)
        self.assertIn("沿支路持续推进", style)
        self.assertIn("return immediately to the verified consequence", style)

    def test_commentary_style_builds_process_anchored_anticipation(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(encoding="utf-8")

        self.assertIn("Process-Anchored Anticipation", style)
        self.assertIn("current process -> current location -> opponent concern -> verified wait -> later confirmation", style)
        self.assertIn("红队正在进行潼关交接", style)
        self.assertIn("可能是在防红队交接完成后再次设卡", style)
        self.assertIn("红队果然在交接结束后立刻启动第二轮设卡", style)
        self.assertIn("Do not use standalone fillers", style)

    def test_commentary_style_has_natural_two_x_pacing_bands(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(encoding="utf-8")

        self.assertIn("`2x` natural delivery", style)
        self.assertIn("4.2-4.8", style)
        self.assertIn("5.0-5.5", style)
        self.assertIn("3.8-4.5", style)
        self.assertIn("overall average at or below 4.8", style)

    def test_commentary_style_enforces_live_knowledge_boundary(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(encoding="utf-8")

        self.assertIn("Live Knowledge Boundary", style)
        self.assertIn("Speak from what is visible at that moment", style)
        self.assertIn("`看起来`, `好像`, `似乎`, or `更像`", style)
        self.assertIn("Do not list uncommitted future stations", style)
        self.assertIn("Do not convert a completed replay route into a live prediction", style)

    def test_commentary_style_requires_earned_logical_connectors(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(encoding="utf-8")

        self.assertIn("Earn Every Logical Connector", style)
        self.assertIn("`却`, `但`, `反而`, or `仍然`", style)
        self.assertIn("actual expectation-and-result contrast", style)
        self.assertIn("梅关任务没分出胜负，两队随后各自行动", style)
        self.assertIn("蓝队已经具备通行条件，却没有马上驶向潼关", style)

    def test_commentary_style_requires_a_full_script_continuity_pass(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        style = (ROOT / "references" / "commentary-style.md").read_text(encoding="utf-8")

        self.assertIn("Whole-Script Continuity Audit", style)
        self.assertIn("Do not re-announce", style)
        self.assertIn("adjacent paragraphs", style)
        self.assertIn("full-script continuity pass", skill)

    def test_commentary_style_uses_audience_facing_failure_language(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(encoding="utf-8")

        self.assertIn("Audience-Facing Failure Language", style)
        self.assertNotIn("任务申请没有生效", style)
        self.assertIn("红队也想处理同一项任务，但蓝队已经占住目标，红队这一步没能执行", style)
        self.assertIn("action, visible cause, and immediate result", style)

    def test_commentary_style_distinguishes_resource_cost_from_conversion(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(encoding="utf-8")

        self.assertIn("Resource Change Attribution", style)
        self.assertIn("voluntary action cost", style)
        self.assertIn("freshness-threshold conversion", style)
        self.assertIn("per-team, per-squad, or combined", style)
        self.assertIn("因鲜度下降转坏的好果仍只有一篓", style)

    def test_event_contract_limits_scout_marker_claims_to_verified_triggers(self) -> None:
        events = (ROOT / "references" / "event-contract.md").read_text(encoding="utf-8")

        self.assertIn("remainingTriggers", events)
        self.assertIn("single marker may shorten only one eligible process", events)
        self.assertIn("SCOUT_MARKER_APPLY", events)
        self.assertIn("SCOUT_MARKER_CONSUME", events)

    def test_skill_resolves_spoken_team_names_by_numeric_id(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("Team Identity Resolution", skill)
        self.assertIn("exact numeric team ID", skill)
        self.assertIn("official spoken team name", skill)
        self.assertIn("UI alias", skill)
        self.assertIn("Never guess an unmapped team name", skill)

    def test_skill_defines_team_pronunciation_and_short_reference_policy(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("spoken pronunciation", skill)
        self.assertIn("opening and winner announcement", skill)
        self.assertIn("red/blue references during dense action", skill)
        self.assertIn("mixed Chinese, English, letters, or numerals", skill)

    def test_skill_uses_authoritative_20260722_team_roster_and_refresh_gate(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        roster_path = ROOT / "references" / "team-roster.md"

        self.assertTrue(roster_path.is_file(), "missing authoritative team roster reference")
        self.assertIn("references/team-roster.md", skill)
        self.assertIn("Roster Revision Gate", skill)
        self.assertIn("rename-only refresh", skill)

        roster = roster_path.read_text(encoding="utf-8")
        expected = {
            2707: "神经突触突击队",
            2804: "代码即答案",
            2639: "疾风速递",
            2982: "OneTrace",
            2751: "虎先锋",
            2749: "让联看看哪个事",
            2714: "SixSixSix",
            2810: "荔争上游",
            2625: "我想见贵妃",
            2621: "一心想赢",
            2743: "不知道对不队",
            2814: "V2搬荔枝小队",
            2744: "荔挽狂澜",
            2735: "随便搞搞",
            2738: "404 NOT FOUND",
            2971: "用AI加油",
        }
        for team_id, name in expected.items():
            self.assertIn(f"| {team_id} | {name} |", roster)

        for stale_name in (
            "神经突触袭击队",
            "疾风道递",
            "虎先降",
            "赛上游",
            "我想见嘉妃",
            "V2赛获小队",
            "赛获狂澜",
        ):
            self.assertNotIn(stale_name, roster)

    def test_skill_requires_duplicate_active_editions_to_stay_synchronized(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        output = (ROOT / "references" / "output-contract.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("Duplicate Edition Consistency Gate", skill)
        self.assertIn("all active editions of the same match", skill)
        self.assertIn("byte-identical", skill)
        self.assertIn("rebuild the voice-only edition", skill)
        self.assertIn("Do not generate SSML or director editions by default", skill)
        self.assertIn("archive or backup the superseded edition", skill)
        self.assertIn("Do not generate SSML, XML, or director editions by default", output)

    def test_commentary_style_requires_explicit_action_effect_chains(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("Action-Effect Naming Gate", style)
        self.assertIn("actor -> destination -> action -> result", style)
        self.assertIn("使用快马加速", style)
        self.assertIn("使用短程马加速", style)
        self.assertIn("障碍已被清除", style)
        self.assertIn("不再有可处理的障碍", style)
        self.assertIn("分别前往", style)

    def test_commentary_style_requires_post_contest_continuation(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("Post-Contest Continuation Gate", style)
        self.assertIn("what each side does next", style)
        self.assertIn("why another contest does or does not open", style)
        self.assertIn("cooldown or forced rest", style)

    def test_commentary_style_has_draw_to_divergence_checklist(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("Draw-to-Divergence Checklist", style)
        self.assertIn(
            "last draw -> forced rest -> restriction ends -> red action -> blue action",
            style,
        )
        self.assertIn("why the contest stops or reopens", style)
        self.assertIn("leaves the contested target", style)
        self.assertIn("different task instances", style)
        self.assertIn("new independent processing", style)

    def test_commentary_style_names_contests_and_score_changes(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("Contest And Score Naming Gate", style)
        self.assertIn("窗口争夺", style)
        self.assertIn("任务分累计六十", style)
        self.assertIn("任务分升至九十", style)
        self.assertIn("牌局", style)
        self.assertIn("来到三十", style)

    def test_commentary_style_requires_explicit_task_type(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("Task-Type Naming Gate", style)
        self.assertIn("official task name", style)
        self.assertIn("栈道复核任务", style)
        self.assertIn("这项任务", style)

    def test_playback_sync_classifies_post_edit_revalidation(self) -> None:
        playback = (ROOT / "references" / "playback-sync.md").read_text(encoding="utf-8")

        self.assertIn("Post-Edit Revalidation Matrix", playback)
        self.assertIn("wording, team-name, or deletion-only edit", playback)
        self.assertIn("event order, cue boundary, or commentary assignment", playback)
        self.assertIn("rule interpretation or result-critical fact", playback)

    def test_playback_sync_reuses_existing_frames_before_replay(self) -> None:
        playback = (ROOT / "references" / "playback-sync.md").read_text(encoding="utf-8")

        self.assertIn("Existing Capture Reuse", playback)
        self.assertIn("spoken claim -> visible UI -> replay anchor -> frame path", playback)
        self.assertIn("ask for another replay only after", playback)

    def test_output_contract_allows_settlement_hold_for_score_readout(self) -> None:
        output = (ROOT / "references" / "output-contract.md").read_text(encoding="utf-8")

        self.assertIn("Settlement Hold Window", output)
        self.assertIn("settlement appearance time", output)
        self.assertIn("commentary completion time", output)
        self.assertIn("static final panel", output)
        self.assertIn("--max-average-rate 4.8", output)

    def test_commentary_style_requires_live_oral_emotion_flow(self) -> None:
        style = (ROOT / "references" / "commentary-style.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("Live Oral Flow And Emotion Gate", style)
        self.assertIn("啦", style)
        self.assertIn("了", style)
        self.assertIn("呢", style)
        self.assertIn("啊", style)
        self.assertIn("event -> immediate reaction -> result -> consequence", style)
        self.assertIn("Do not reduce live delivery to a particle word list", style)

    def test_output_contract_requires_live_style_audit_for_new_scripts(self) -> None:
        output = (ROOT / "references" / "output-contract.md").read_text(encoding="utf-8")

        self.assertIn("--require-live-style", output)
        self.assertIn("Every new or fully refreshed commentary", output)

    def test_output_contract_uses_standard_two_x_program_clock(self) -> None:
        output = (ROOT / "references" / "output-contract.md").read_text(encoding="utf-8")

        self.assertIn("Standard 2x Program Clock", output)
        self.assertIn("600 rounds = about 300 seconds", output)
        self.assertIn("opening plus settlement = 30 seconds", output)
        self.assertIn("screenshot acquisition wall clock", output)
        self.assertIn("must not become the edited program clock", output)
        self.assertIn("双方各带一百篓好果", output)
        self.assertIn("比赛开始啦", output)


if __name__ == "__main__":
    unittest.main()
