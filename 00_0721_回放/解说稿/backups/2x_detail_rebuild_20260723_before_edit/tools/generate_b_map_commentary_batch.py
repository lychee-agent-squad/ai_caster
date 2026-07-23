#!/usr/bin/env python3
"""Generate replay-grounded 2x commentary drafts for the B-map batch."""

from __future__ import annotations

import argparse
import importlib.util
import math
import re
from pathlib import Path
from typing import Any


ROSTER = {
    "2707": "神经突触突击队",
    "2804": "代码即答案",
    "2639": "疾风速递",
    "2982": "OneTrace",
    "2751": "虎先锋",
    "2749": "让联看看哪个事",
    "2714": "SixSixSix",
    "2810": "荔争上游",
    "2625": "我想见贵妃",
    "2621": "一心想赢",
    "2743": "不知道对不队",
    "2814": "V2搬荔枝小队",
    "2744": "荔挽狂澜",
    "2735": "随便搞搞",
    "2738": "404 NOT FOUND",
    "2971": "用AI加油",
}

NODE_NAMES = {
    "S01": "岭南果园",
    "S02": "南岭驿",
    "S03": "梅关驿",
    "S04": "江南码头",
    "S05": "洞庭水驿",
    "S06": "五岭山道",
    "S07": "荆襄大驿",
    "S08": "秦岭栈道",
    "S09": "洛阳驿",
    "S10": "武关",
    "S11": "潼关驿",
    "S12": "关中平原",
    "S13": "灞桥驿",
    "S14": "朱雀门",
    "S15": "兴庆宫",
}

WINDOWS = [
    (0, 15),
    (15, 31),
    (31, 47),
    (47, 63),
    (63, 79),
    (79, 95),
    (95, 111),
    (111, 127),
    (127, 143),
    (143, 159),
    (159, 175),
    (175, 191),
    (191, 207),
    (207, 223),
    (223, 239),
    (239, 255),
    (255, 271),
    (271, 287),
    (287, 302),
    (302, 315),
    (315, 330),
]

HIGH_PRIORITY = {
    "TACTICAL_GUARD_TRIGGER": 97,
    "DELIVER_SUCCESS": 100,
    "VERIFY_GATE_COMPLETE": 95,
    "FORCED_PASS_END": 94,
    "PASS_CONTEST_WIN": 93,
    "PASS_CONTEST_DEFENDED": 92,
    "WINDOW_CONTEST_END": 91,
    "GUARD_BREAK": 90,
    "GUARD_SET": 89,
    "TACTICAL_GUARD_STANDOFF": 85,
    "SQUAD_WEAKEN": 88,
    "SQUAD_REINFORCE": 87,
    "ACTION_REJECTED": 86,
    "TASK_COMPLETE": 82,
    "RESOURCE_USE": 80,
    "NODE_ENTER": 76,
    "SQUAD_CLEAR": 74,
    "OBSTACLE_CLEAR": 74,
    "SQUAD_DISPATCH": 72,
    "SQUAD_FAILED": 70,
    "GOOD_TO_BAD": 68,
    "GUARD_WEATHERING": 64,
    "BOUNTY_CLAIM": 63,
    "RUSH_START": 60,
}


def replay_player_label(player: dict[str, Any]) -> str:
    player_id = str(player.get("playerId") or player.get("id") or "")
    team = str(player.get("teamId") or "")
    visible_name = str(player.get("name") or player_id)
    return f"{team} {visible_name} ({player_id})"


def record_player(record: dict[str, Any], target_id: str) -> dict[str, Any] | None:
    return next(
        (
            player
            for player in record.get("players") or []
            if str(player.get("playerId") or player.get("id") or "") == target_id
        ),
        None,
    )


def guard_active(record: dict[str, Any], node_id: str) -> bool:
    node = next((item for item in record.get("nodes") or [] if str(item.get("nodeId") or "") == node_id), None)
    guard = (node or {}).get("guard") or {}
    return bool(guard.get("active")) and int(guard.get("defense") or 0) > 0


def detect_guard_timing_events(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Detect a verified wait -> opponent move -> immediate guard timing chain."""
    rounds = [record for record in records if record.get("type") == "round"]
    events: list[dict[str, Any]] = []
    for complete_index, record in enumerate(rounds):
        for message in record.get("messages") or []:
            if str(message.get("type") or "") != "GUARD_SET":
                continue
            payload = message.get("payload") or {}
            defender_id = str(payload.get("playerId") or "")
            node_id = str(payload.get("nodeId") or "")
            defender = record_player(record, defender_id)
            opponents = [
                player
                for player in record.get("players") or []
                if str(player.get("playerId") or player.get("id") or "") != defender_id
            ]
            if not defender or len(opponents) != 1:
                continue
            attacker = opponents[0]
            attacker_id = str(attacker.get("playerId") or attacker.get("id") or "")
            if attacker.get("state") != "MOVING" or str(attacker.get("nextNodeId") or "") != node_id:
                continue

            move_index = None
            for index in range(complete_index, max(0, complete_index - 12) - 1, -1):
                current_attacker = record_player(rounds[index], attacker_id)
                previous_attacker = record_player(rounds[index - 1], attacker_id) if index > 0 else None
                if not current_attacker or current_attacker.get("state") != "MOVING":
                    continue
                if str(current_attacker.get("nextNodeId") or "") != node_id:
                    continue
                if not previous_attacker or previous_attacker.get("state") != "MOVING" or str(previous_attacker.get("nextNodeId") or "") != node_id:
                    move_index = index
                    break
            if move_index is None or move_index == 0:
                continue

            wait_end_index = move_index - 1
            wait_end = rounds[wait_end_index]
            end_defender = record_player(wait_end, defender_id)
            end_attacker = record_player(wait_end, attacker_id)
            if not end_defender or not end_attacker:
                continue
            defender_node = str(end_defender.get("currentNodeId") or "")
            attacker_node = str(end_attacker.get("currentNodeId") or "")
            if defender_node != node_id or attacker_node == node_id:
                continue

            wait_start_index = wait_end_index
            while wait_start_index >= 0:
                candidate = rounds[wait_start_index]
                candidate_defender = record_player(candidate, defender_id)
                candidate_attacker = record_player(candidate, attacker_id)
                if not candidate_defender or not candidate_attacker:
                    break
                if candidate_defender.get("state") != "WAITING" or candidate_attacker.get("state") != "WAITING":
                    break
                if str(candidate_defender.get("currentNodeId") or "") != defender_node:
                    break
                if str(candidate_attacker.get("currentNodeId") or "") != attacker_node:
                    break
                wait_start_index -= 1
            wait_start_index += 1
            wait_start_round = int(rounds[wait_start_index].get("round") or 0)
            wait_end_round = int(wait_end.get("round") or 0)
            if wait_end_round - wait_start_round + 1 < 8:
                continue

            had_active_guard = any(
                guard_active(candidate, node_id) for candidate in rounds[wait_start_index : wait_end_index + 1]
            )
            guard_mode = "replacement" if had_active_guard else "fresh"
            common = {
                "player": replay_player_label(defender),
                "attacker": replay_player_label(attacker),
                "defenderNodeId": defender_node,
                "attackerNodeId": attacker_node,
                "guardNodeId": node_id,
                "waitStartRound": wait_start_round,
                "waitEndRound": wait_end_round,
                "moveRound": int(rounds[move_index].get("round") or 0),
                "guardMode": guard_mode,
                "defense": int(payload.get("defense") or payload.get("defenseValue") or 0),
                "progressPermille": int(attacker.get("edgeProgressPermille") or 0),
            }
            if guard_mode == "fresh":
                events.append(
                    {
                        **common,
                        "type": "TACTICAL_GUARD_STANDOFF",
                        "title": "设卡时机博弈",
                        "round": min(wait_end_round, wait_start_round + 1),
                        "detail": f"{NODE_NAMES.get(attacker_node, attacker_node)} 等待；{NODE_NAMES.get(defender_node, defender_node)} 等待",
                    }
                )
            events.append(
                {
                    **common,
                    "type": "TACTICAL_GUARD_TRIGGER",
                    "title": "卡准上路时机设卡",
                    "round": int(record.get("round") or 0),
                    "detail": f"{NODE_NAMES.get(node_id, node_id)}({node_id}) 设卡时机链",
                }
            )
    return events


def load_extractor(path: Path):
    spec = importlib.util.spec_from_file_location("lychee_extract_timeline", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load timeline extractor: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def mmss(seconds: int) -> str:
    return f"{seconds // 60:02d}:{seconds % 60:02d}"


def cn_int(value: Any) -> str:
    try:
        number = int(float(value))
    except (TypeError, ValueError):
        return str(value)
    digits = "零一二三四五六七八九"
    if number < 0:
        return "负" + cn_int(-number)
    if number < 10:
        return digits[number]
    if number < 20:
        return "十" + (digits[number % 10] if number % 10 else "")
    if number < 100:
        return digits[number // 10] + "十" + (digits[number % 10] if number % 10 else "")
    if number < 1000:
        hundreds, rest = divmod(number, 100)
        if not rest:
            return digits[hundreds] + "百"
        return digits[hundreds] + "百" + ("零" if rest < 10 else "") + cn_int(rest)
    thousands, rest = divmod(number, 1000)
    if not rest:
        return cn_int(thousands) + "千"
    return cn_int(thousands) + "千" + ("零" if rest < 100 else "") + cn_int(rest)


def cn_decimal(value: Any) -> str:
    try:
        text = f"{float(value):.2f}".rstrip("0").rstrip(".")
    except (TypeError, ValueError):
        return str(value)
    if "." not in text:
        return cn_int(text)
    whole, fraction = text.split(".", 1)
    digits = "零一二三四五六七八九"
    return cn_int(whole) + "点" + "".join(digits[int(ch)] for ch in fraction)


def player_id(label: str) -> str:
    match = re.search(r"\((\d+)\)$", label or "")
    return match.group(1) if match else ""


def team_side(label: str) -> str:
    if (label or "").startswith("RED "):
        return "红队"
    if (label or "").startswith("BLUE "):
        return "蓝队"
    return ""


def team_name(label: str) -> str:
    return ROSTER.get(player_id(label), team_side(label) or "该队")


def node_from_detail(detail: str) -> str:
    match = re.search(r"([\u4e00-\u9fff]+)\(S\d+\)", detail or "")
    return match.group(1) if match else "目标点"


def task_name(detail: str) -> str:
    match = re.search(r"完成\s+([^，]+)", detail or "")
    name = match.group(1).strip() if match else "皇榜"
    if "复核" in name and not name.endswith("任务"):
        name += "任务"
    elif not name.endswith("任务"):
        name += "任务"
    return name


def transition(detail: str) -> tuple[str, str]:
    match = re.search(r"(?:防守值\s*)?(\d+)->(\d+)", detail or "")
    return match.groups() if match else ("", "")


def event_sentence(event: dict[str, Any], start: int = 0) -> str:
    kind = event.get("type", "")
    detail = str(event.get("detail", ""))
    side = team_side(str(event.get("player", "")))
    name = team_name(str(event.get("player", "")))
    node = node_from_detail(detail)

    if kind == "TACTICAL_GUARD_STANDOFF":
        defender_side = side
        attacker_side = team_side(str(event.get("attacker") or ""))
        defender_node = NODE_NAMES.get(str(event.get("defenderNodeId") or ""), "前方站点")
        attacker_node = NODE_NAMES.get(str(event.get("attackerNodeId") or ""), "后方站点")
        return (
            f"{defender_side}守在前方{defender_node}，没有继续走，也没有提前设卡；"
            f"{attacker_side}留在{attacker_node}，同样不肯先动。看来两边都在等对手先动。"
        )
    if kind == "TACTICAL_GUARD_TRIGGER":
        defender_side = side
        attacker_side = team_side(str(event.get("attacker") or ""))
        attacker_node = NODE_NAMES.get(str(event.get("attackerNodeId") or ""), "后方站点")
        guard_node = NODE_NAMES.get(str(event.get("guardNodeId") or ""), node)
        defense = cn_int(event.get("defense") or 0)
        progress = cn_decimal(float(event.get("progressPermille") or 0) / 10)
        if event.get("guardMode") == "replacement":
            return (
                f"原有关卡刚刚失效，{attacker_side}马上从{attacker_node}启程；{defender_side}看到车队上路，"
                f"立刻补设{defense}点关卡。关卡生效时，{attacker_side}推进到百分之{progress}，再次被挡住！"
            )
        return (
            f"{attacker_side}先动了！主车刚从{attacker_node}驶向{guard_node}，{defender_side}立刻开始设卡。"
            f"{defense}点关卡抢在进站前生效，{attacker_side}推进到百分之{progress}就被挡住！"
        )

    if kind == "SQUAD_DISPATCH":
        action_match = re.search(r"派遣队伍(清障|侦察|增援|削弱)", detail)
        action = action_match.group(1) if action_match else "处理"
        action_text = {"清障": "清理障碍", "侦察": "探查", "增援": "增援设卡", "削弱": "削弱关卡"}.get(action, action)
        return f"{side}派出小分队前往{node}{action_text}。"
    if kind in {"SQUAD_CLEAR", "OBSTACLE_CLEAR"}:
        return f"{side}完成{node}清障，前方通路打开了。"
    if kind == "SQUAD_FAILED":
        return f"{side}派往{node}的小分队没有完成目标，这笔人手投入没能兑现。"
    if kind == "NODE_ENTER":
        return f"{side}主车进入{node}。"
    if kind == "TASK_COMPLETE":
        score_match = re.search(r"任务分\s*(\d+)", detail)
        score = cn_int(score_match.group(1)) if score_match else "新的"
        return f"{side}完成{task_name(detail)}，任务分累计{score}！"
    if kind == "RESOURCE_USE":
        if "快马" in detail:
            return f"{side}马上使用快马加速，主车继续抢时间。"
        if "短驿马" in detail:
            return f"{side}开启短驿马加速，推进速度提起来了。"
        if "冰鉴" in detail:
            values = re.search(r"状态\s*([\d.]+)->([\d.]+)", detail)
            if values:
                return f"{side}使用冰鉴，鲜度从{cn_decimal(values.group(1))}回升到{cn_decimal(values.group(2))}。"
            return f"{side}使用冰鉴，及时补回鲜度。"
        return f"{side}使用路线资源，开始加快后续节奏。"
    if kind == "GUARD_SET":
        defense = re.search(r"防守值\s*(\d+)", detail)
        points = cn_int(defense.group(1)) if defense else ""
        return f"{side}在{node}完成{points}点设卡！"
    if kind == "SQUAD_WEAKEN":
        before, after = transition(detail)
        if before and after:
            return f"{side}的小分队完成削弱，{node}防守从{cn_int(before)}点降到{cn_int(after)}点。"
        return f"{side}的小分队开始削弱{node}关卡。"
    if kind == "SQUAD_REINFORCE":
        before, after = transition(detail)
        if before and after:
            return f"{side}立刻派队增援，{node}防守从{cn_int(before)}点回升到{cn_int(after)}点！"
        return f"{side}派出小分队增援{node}关卡。"
    if kind == "GUARD_BREAK":
        return f"{side}正面攻坚成功，{node}关卡被拆掉了！"
    if kind == "GUARD_WEATHERING":
        before, after = transition(detail)
        if before and after:
            return f"{node}关卡开始风化，防守从{cn_int(before)}点降到{cn_int(after)}点。"
        return f"{node}关卡正在风化。"
    if kind == "ACTION_REJECTED":
        if "设卡阻挡" == event.get("title") or "MOVE_BLOCKED_BY_GUARD" in detail or "推进被阻断" in detail:
            progress = re.search(r"进度\s*([\d.]+)%", detail)
            suffix = f"，受阻时已经走到百分之{cn_decimal(progress.group(1))}" if progress else ""
            variants = [
                f"{side}向{node}的推进被关卡挡住{suffix}。",
                f"封锁还在继续，{side}再次尝试进点，依然被{node}关卡拦下{suffix}。",
                f"{node}关卡仍然生效，{side}的推进继续被挡{suffix}，时间和鲜度都在流失。",
                f"{side}还没能穿过{node}，关卡持续阻断进点{suffix}。",
            ]
            return variants[(start // 16) % len(variants)]
        if "必经处理尚未完成" in detail:
            return f"{side}还没完成当前站点流程，离站动作没有生效。"
        return ""
    if kind == "GOOD_TO_BAD":
        bad = re.search(r"坏果\s*(\d+)", detail)
        bad_text = cn_int(bad.group(1)) if bad else "新的"
        return f"哎呀，{side}鲜度越过阈值，坏果增至{bad_text}篓。"
    if kind == "WINDOW_CONTEST_START":
        return f"{node}的窗口争夺开启，双方开始正面对抗！"
    if kind == "WINDOW_CONTEST_END":
        winner = re.search(r"胜方\s*(RED|BLUE)", detail)
        if winner:
            winner_side = "红队" if winner.group(1) == "RED" else "蓝队"
            return f"窗口争夺结束，{winner_side}拿下处理权！"
        return "窗口争夺结束，双方都要重新安排下一步行动。"
    if kind == "PASS_CONTEST_WIN":
        return f"{side}赢下强制通行争夺，通行流程正式启动！"
    if kind == "PASS_CONTEST_DEFENDED":
        return f"设卡方守住了强制通行，进攻车队这一次没能通过。"
    if kind == "FORCED_PASS_START":
        return f"{side}开始执行强制通行，主车持续向{node}推进。"
    if kind == "FORCED_PASS_RECALCULATE":
        return f"{node}关卡状态变化，{side}的强制通行成本重新计算。"
    if kind == "FORCED_PASS_END":
        return f"漂亮，{side}完成强制通行，主车进入{node}！"
    if kind == "VERIFY_GATE_COMPLETE":
        return f"{side}完成朱雀门核验，进宫资格拿到了！"
    if kind == "DELIVER_SUCCESS":
        good = re.search(r"好果\s*(\d+)", detail)
        freshness = re.search(r"新鲜度\s*([\d.]+)", detail)
        score = re.search(r"总分\s*(\d+)", detail)
        return (
            f"{side}进入兴庆宫，送达成功！保住{cn_int(good.group(1)) if good else ''}篓好果，"
            f"鲜度{cn_decimal(freshness.group(1)) if freshness else ''}，总分{cn_int(score.group(1)) if score else ''}。"
        )
    if kind == "RUSH_START":
        return "冲刺阶段开启啦，朱雀门前的终局节奏开始加快！"
    if kind == "BOUNTY_CLAIM":
        return f"{side}拆掉{node}关卡，还拿到了破关悬赏。"
    return ""


def snapshot_for_round(records: list[dict[str, Any]], round_value: int) -> dict[str, Any]:
    latest: dict[str, Any] | None = None
    for record in records:
        if record.get("type") != "round":
            continue
        current = int(record.get("round") or 0)
        if current > round_value:
            break
        latest = record
    return latest or records[0]


def short_player_status(player: dict[str, Any], prefix: str = "") -> str:
    side = "红队" if str(player.get("teamId")) == "RED" else "蓝队"
    current = NODE_NAMES.get(str(player.get("currentNodeId") or ""), str(player.get("currentNodeId") or "当前节点"))
    next_node = NODE_NAMES.get(str(player.get("nextNodeId") or ""), str(player.get("nextNodeId") or ""))
    if player.get("delivered"):
        return f"{prefix}{side}已经完成交付。"
    if str(player.get("state") or "") == "MOVING" and next_node:
        return f"{prefix}{side}正从{current}前往{next_node}。"
    return f"{prefix}{side}仍在{current}，没有切换路线。"


def contextual_status(record: dict[str, Any], chosen: list[dict[str, Any]]) -> str:
    event_sides = {team_side(str(event.get("player") or "")) for event in chosen}
    event_sides.discard("")
    players = record.get("players") or []
    if len(event_sides) == 1:
        other_side = "蓝队" if "红队" in event_sides else "红队"
        other = next((player for player in players if ("红队" if str(player.get("teamId")) == "RED" else "蓝队") == other_side), None)
        return short_player_status(other, "与此同时，") if other else ""
    if not event_sides and len(players) == 2:
        return "".join(short_player_status(player, "再看，" if index == 0 else "") for index, player in enumerate(players))
    return ""


def state_sentence(record: dict[str, Any], start: int) -> str:
    parts: list[str] = []
    stationary: list[tuple[str, str]] = []
    delivered: list[str] = []
    for player in record.get("players") or []:
        side = "红队" if str(player.get("teamId")) == "RED" else "蓝队"
        if player.get("delivered"):
            delivered.append(side)
            parts.append(f"{side}已经完成交付")
            continue
        current = NODE_NAMES.get(str(player.get("currentNodeId") or ""), str(player.get("currentNodeId") or "当前节点"))
        next_node = NODE_NAMES.get(str(player.get("nextNodeId") or ""), str(player.get("nextNodeId") or ""))
        state = str(player.get("state") or "")
        if state == "MOVING" and next_node:
            progress = round(float(player.get("edgeProgressPermille") or 0) / 10, 1)
            parts.append(f"{side}正从{current}前往{next_node}，路线推进约百分之{cn_decimal(progress)}")
        elif player.get("verified"):
            parts.append(f"{side}已经完成朱雀门核验")
        elif state in {"PROCESSING", "RESTING"}:
            action = "处理站点流程" if state == "PROCESSING" else "等待休整结束"
            parts.append(f"{side}还在{current}{action}")
        else:
            stationary.append((side, current))
            parts.append(f"{side}继续停在{current}，没有切换路线")
    if not parts:
        return "双方继续执行当前策略。"
    if len(stationary) == 2:
        red_node = next(node for side, node in stationary if side == "红队")
        blue_node = next(node for side, node in stationary if side == "蓝队")
        variants = [
            f"红队继续停在{red_node}，蓝队留在{blue_node}，双方都没有切换路线。",
            f"等待还在继续，红队守在{red_node}，蓝队留在{blue_node}，两支主车都没有起步。",
            f"双方依旧没有切换行动。红队在{red_node}，蓝队在{blue_node}，看来还在观察对手的选择。",
            f"这段等待还没结束，红队停在{red_node}，蓝队停在{blue_node}。路线没有推进，鲜度却仍在下降。",
        ]
        return variants[(start // 16) % len(variants)]
    if len(delivered) == 2:
        variants = [
            "两队都已经完成交付，路线争夺结束，等待最终结算。",
            "双方果量和鲜度已经锁定，接下来只看各项结算分数。",
            "终局流程已经结束，画面没有新的路线行动，胜负很快揭晓。",
            "双方成绩已经确认，最后的分项对比马上出来了。",
            "两支车队都已进宫交付，终局数据不会再发生变化。",
            "交付环节全部结束，双方正在等待结算页确认胜方。",
        ]
        return variants[(start // 16) % len(variants)]
    if len(delivered) == 1 and len(stationary) == 1:
        waiting_side, waiting_node = stationary[0]
        delivered_side = delivered[0]
        variants = [
            f"{delivered_side}已经完成交付，{waiting_side}仍停在{waiting_node}，没有继续推进。",
            f"{waiting_side}还留在{waiting_node}，而{delivered_side}的成绩已经锁定，追赶时间越来越少。",
            f"终点一侧已经完成交付，{waiting_side}依旧停在{waiting_node}，后续核验和进宫都赶不上了。",
            f"比赛接近结束，{waiting_side}没有离开{waiting_node}，{delivered_side}正在等待最终结算。",
            f"{delivered_side}已经锁定送达数据，{waiting_side}还在{waiting_node}，终局路线没有继续推进。",
            f"剩余时间越来越少，{waiting_side}仍停留在{waiting_node}，已经无法走完核验和交付流程。",
        ]
        return variants[(start // 16) % len(variants)]
    return "；".join(parts) + "。这段时间没有新的任务结算。"


def compose_sentences(chosen: list[dict[str, Any]], start: int) -> list[str]:
    utterances: list[tuple[int, int, str]] = []
    consumed: set[int] = set()

    for index, event in enumerate(chosen):
        if event.get("type") != "TACTICAL_GUARD_TRIGGER":
            continue
        trigger_round = int(event.get("round") or 0)
        trigger_node = str(event.get("guardNodeId") or "")
        for other_index, other in enumerate(chosen):
            if other_index == index or other.get("type") not in {"GUARD_SET", "ACTION_REJECTED"}:
                continue
            if abs(int(other.get("round") or 0) - trigger_round) > 2:
                continue
            other_node = node_from_detail(str(other.get("detail") or ""))
            if other_node == NODE_NAMES.get(trigger_node, trigger_node):
                consumed.add(other_index)

    for index, event in enumerate(chosen):
        if event.get("type") != "NODE_ENTER":
            continue
        side = team_side(str(event.get("player") or ""))
        node = node_from_detail(str(event.get("detail") or ""))
        if any(
            other_index != index
            and team_side(str(other.get("player") or "")) == side
            and node_from_detail(str(other.get("detail") or "")) == node
            and other.get("type") in {"DELIVER_SUCCESS", "FORCED_PASS_END", "VERIFY_GATE_COMPLETE"}
            for other_index, other in enumerate(chosen)
        ):
            consumed.add(index)

    for kind, action_word in (("SQUAD_DISPATCH", "派队"), ("SQUAD_CLEAR", "清障")):
        groups: dict[str, list[tuple[int, dict[str, Any]]]] = {}
        for index, event in enumerate(chosen):
            if event.get("type") != kind:
                continue
            side = team_side(str(event.get("player") or ""))
            groups.setdefault(side, []).append((index, event))
        for side, grouped in groups.items():
            if len(grouped) < 2:
                continue
            targets = []
            for index, event in grouped:
                target = node_from_detail(str(event.get("detail") or ""))
                if target not in targets:
                    targets.append(target)
                consumed.add(index)
            target_text = "和".join(targets[:2])
            if kind == "SQUAD_DISPATCH":
                details = [str(event.get("detail") or "") for _, event in grouped]
                if all("派遣队伍清障" in detail for detail in details):
                    action_text = "清障"
                elif all("派遣队伍侦察" in detail for detail in details):
                    action_text = "探查"
                else:
                    action_text = "分别执行清障和探查"
                connector = "" if action_text.startswith("分别") else "分别前往"
                utterances.append((min(int(event.get("round") or 0) for _, event in grouped), 0, f"{side}接连派出小分队，{connector}{target_text}{action_text}。"))
            else:
                utterances.append((min(int(event.get("round") or 0) for _, event in grouped), 0, f"{side}派出的队伍完成{target_text}清障，两处通路都打开了。"))

    node_groups: dict[tuple[int, str], list[tuple[int, dict[str, Any]]]] = {}
    for index, event in enumerate(chosen):
        if event.get("type") != "NODE_ENTER":
            continue
        node = node_from_detail(str(event.get("detail") or ""))
        node_groups.setdefault((int(event.get("round") or 0), node), []).append((index, event))
    for (_, node), grouped in node_groups.items():
        sides = {team_side(str(event.get("player") or "")) for _, event in grouped}
        if len(sides) == 2:
            utterances.append((min(int(event.get("round") or 0) for _, event in grouped), 0, f"红蓝两队同时进入{node}！"))
            consumed.update(index for index, _ in grouped)

    bad_events = [(index, event) for index, event in enumerate(chosen) if event.get("type") == "GOOD_TO_BAD"]
    if len({team_side(str(event.get("player") or "")) for _, event in bad_events}) == 2:
        bad_variants = [
            "哎呀，双方鲜度先后越过阈值，好果数量都受到影响。",
            "两队又先后越过下一道鲜度阈值，好果数量继续下降。",
            "鲜度压力还在增加，红蓝双方都再次出现果品折损。",
        ]
        utterances.append((min(int(event.get("round") or 0) for _, event in bad_events), 0, bad_variants[(start // 16) % len(bad_variants)]))
        consumed.update(index for index, _ in bad_events)

    pass_wins = [(index, event) for index, event in enumerate(chosen) if event.get("type") == "PASS_CONTEST_WIN"]
    if len(pass_wins) > 1:
        side = team_side(str(pass_wins[0][1].get("player") or ""))
        utterances.append((min(int(event.get("round") or 0) for _, event in pass_wins), 0, f"{side}连续赢下强制通行争夺，通行流程持续推进！"))
        consumed.update(index for index, _ in pass_wins)

    contest_ends = [(index, event) for index, event in enumerate(chosen) if event.get("type") == "WINDOW_CONTEST_END"]
    if len(contest_ends) > 1:
        winner_events = [(index, event) for index, event in contest_ends if re.search(r"胜方\s*(RED|BLUE)", str(event.get("detail") or "")) and "胜方 DRAW" not in str(event.get("detail") or "")]
        draw_count = len(contest_ends) - len(winner_events)
        if winner_events and not pass_wins:
            winner = re.search(r"胜方\s*(RED|BLUE)", str(winner_events[0][1].get("detail") or ""))
            winner_side = "红队" if winner and winner.group(1) == "RED" else "蓝队"
            utterances.append((int(winner_events[0][1].get("round") or 0), 0, f"窗口争夺结束，{winner_side}拿到这一轮处理权！"))
        if draw_count:
            count_text = "两" if draw_count == 2 else cn_int(draw_count)
            utterances.append((max(int(event.get("round") or 0) for _, event in contest_ends), 0, f"随后连续出现{count_text}次平局，双方都没能继续扩大优势。"))
        consumed.update(index for index, _ in contest_ends)

    for index, event in enumerate(chosen):
        if index in consumed:
            continue
        sentence = event_sentence(event, start)
        if sentence:
            utterances.append((int(event.get("round") or 0), index + 1, sentence))
    ordered = [sentence for _, _, sentence in sorted(utterances)]
    unique: list[str] = []
    for sentence in ordered:
        if sentence not in unique:
            unique.append(sentence)
    return unique


def dedupe_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    repeat_sensitive = {"DELIVER_SUCCESS", "VERIFY_GATE_COMPLETE", "TASK_COMPLETE", "GUARD_SET", "RESOURCE_USE"}
    for event in events:
        kind = str(event.get("type") or "")
        key = (kind, str(event.get("player") or ""), str(event.get("detail") or ""))
        if kind in repeat_sensitive and key in seen:
            continue
        seen.add(key)
        result.append(event)
    return result


def pick_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    chosen: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    rejected_seen: set[str] = set()
    for event in sorted(events, key=lambda item: (int(item.get("round") or 0), -HIGH_PRIORITY.get(str(item.get("type")), 0))):
        kind = str(event.get("type") or "")
        if kind not in HIGH_PRIORITY:
            continue
        side = team_side(str(event.get("player") or ""))
        node = node_from_detail(str(event.get("detail") or ""))
        key = (kind, side, node)
        if kind == "ACTION_REJECTED":
            reject_key = side + node
            if reject_key in rejected_seen:
                continue
            rejected_seen.add(reject_key)
        if key in seen and kind in {"NODE_ENTER", "GUARD_WEATHERING", "SQUAD_DISPATCH"}:
            continue
        seen.add(key)
        chosen.append(event)
    ranked = sorted(chosen, key=lambda item: (-HIGH_PRIORITY.get(str(item.get("type")), 0), int(item.get("round") or 0)))[:4]
    return sorted(ranked, key=lambda item: (int(item.get("round") or 0), -HIGH_PRIORITY.get(str(item.get("type")), 0)))


def event_title(event: dict[str, Any]) -> str:
    kind = str(event.get("type") or "")
    title = str(event.get("title") or kind)
    if kind == "ACTION_REJECTED":
        return "动作被拒绝"
    return title.replace("验关", "核验")


def segment_title(chosen: list[dict[str, Any]], commentary: str) -> str:
    if chosen:
        primary = max(chosen, key=lambda item: HIGH_PRIORITY.get(str(item.get("type")), 0))
        side = team_side(str(primary.get("player") or ""))
        title = event_title(primary)
        node = node_from_detail(str(primary.get("detail") or ""))
        if primary.get("type") in {"GUARD_SET", "GUARD_BREAK", "VERIFY_GATE_COMPLETE", "DELIVER_SUCCESS"}:
            return f"{side}{node}{title}".replace("目标点", "")
        return f"{side}{title}" if side else title
    if "没有切换路线" in commentary:
        return "双方保持当前行动"
    return "路线继续推进"


def build_segment(
    events: list[dict[str, Any]],
    records: list[dict[str, Any]],
    start: int,
    end: int,
    over_round: int,
) -> tuple[str, str, int]:
    round_start = max(1, math.ceil((start - 15) * 2))
    round_end = min(over_round, max(1, math.floor((end - 15) * 2)))
    in_window = [event for event in events if round_start <= int(event.get("round") or 0) <= round_end]
    chosen = pick_events(in_window)
    sentences = compose_sentences(chosen, start)
    if not sentences:
        sentences = [state_sentence(snapshot_for_round(records, round_end), start)]
    text = "".join(sentences)
    if len(text) > 82:
        essential = sorted(
            sorted(chosen, key=lambda item: -HIGH_PRIORITY.get(str(item.get("type")), 0))[:2],
            key=lambda item: int(item.get("round") or 0),
        )
        sentences = compose_sentences(essential, start)
        text = "".join(sentences)
    if len(text) > 82:
        text = text[:81].rstrip("，；") + "。"
    critical_types = {str(event.get("type") or "") for event in chosen}
    if chosen and len(text) < 42 and not critical_types.intersection({"DELIVER_SUCCESS", "VERIFY_GATE_COMPLETE", "FORCED_PASS_END"}):
        context_text = contextual_status(snapshot_for_round(records, round_end), chosen)
        if context_text:
            text += context_text
    if len(text) > 82:
        text = text[:81].rstrip("，；") + "。"
    if start in {47, 207} and "等等" not in text:
        text = "等等，" + text
    if start == 271 and "哎呀" not in text:
        text = "哎呀，" + text
    if start == 287 and not any(word in text for word in ("终于", "漂亮", "送达成功")):
        text += "最后结果马上见分晓！"
    anchor = "；".join(f"R{event['round']} {event_title(event)}" for event in chosen) or f"R{round_end} 状态截面"
    image_round = max([int(event.get("round") or 0) for event in chosen] or [round_end])
    return text, anchor, min(max(1, image_round), over_round)


def result_lookup(summary: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for item in summary.get("resultPlayers") or []:
        result[player_id(str(item.get("player") or ""))] = item
    return result


def build_document(match_id: str, records: list[dict[str, Any]], summary: dict[str, Any], events: list[dict[str, Any]]) -> str:
    events = dedupe_events(events + detect_guard_timing_events(records))
    start_record = records[0]
    players = start_record.get("players") or []
    red = next(player for player in players if str(player.get("teamId")) == "RED")
    blue = next(player for player in players if str(player.get("teamId")) == "BLUE")
    red_id, blue_id = str(red.get("playerId") or red.get("id")), str(blue.get("playerId") or blue.get("id"))
    red_name, blue_name = ROSTER.get(red_id, red_id), ROSTER.get(blue_id, blue_id)
    results = result_lookup(summary)
    red_result, blue_result = results[red_id], results[blue_id]
    over_round = int(summary.get("durationRound") or 600)
    final_record = records[-1]
    winner_id = str(final_record.get("winnerPlayerId") or "")
    winner_name = ROSTER.get(winner_id, winner_id or "胜方")

    lines = [
        f"# {match_id} 荔枝争运战 2倍速 UI 同步解说稿",
        "",
        f"> 红队：{red_name}（{red_id}）  蓝队：{blue_name}（{blue_id}）",
        "> 播放标准：2倍速；500ms取图；成片上限05:30。",
        "",
    ]

    for index, (start, end) in enumerate(WINDOWS):
        if index == 0:
            title = "双方启程"
            image_round = 1
            anchor = "R1 双方从岭南果园出发"
            commentary = (
                f"欢迎来到荔枝争运战！红队{red_name}对阵蓝队{blue_name}。双方各带一百篓好果，鲜度全满，"
                "从岭南果园出发。穿过朱雀门，把荔枝送进兴庆宫！比赛开始啦！"
            )
            source = "双方车队从岭南果园出发，初始果量和鲜度一致。"
        elif index == len(WINDOWS) - 1:
            title = "最终结算"
            image_round = over_round
            anchor = (
                f"红队总分{red_result['score']}，交付{'完成' if red_result['delivered'] else '未完成'}；"
                f"蓝队总分{blue_result['score']}，交付{'完成' if blue_result['delivered'] else '未完成'}"
            )
            red_status = "完成交付" if red_result["delivered"] else "未能交付"
            blue_status = "完成交付" if blue_result["delivered"] else "未能交付"
            commentary = (
                f"最终比分，红队{red_name}{cn_int(red_result['score'])}，{red_status}；"
                f"蓝队{blue_name}{cn_int(blue_result['score'])}，{blue_status}。"
                f"恭喜{winner_name}，拿下本场胜利！"
            )
            source = "结算页显示双方最终分数、交付状态与胜方。"
        else:
            commentary, anchor, image_round = build_segment(events, records, start, end, over_round)
            source = commentary.replace("！", "，").replace("。", "；").rstrip("；") + "。"
            round_start = max(1, math.ceil((start - 15) * 2))
            round_end = min(over_round, max(1, math.floor((end - 15) * 2)))
            chosen = pick_events([event for event in events if round_start <= int(event.get("round") or 0) <= round_end])
            title = segment_title(chosen, commentary)
        image_file = (
            "frame_final_settlement.jpg"
            if index == len(WINDOWS) - 1
            else f"frame_{image_round:04d}_{image_round * 500:06d}ms.jpg"
        )
        lines.extend(
            [
                f"## {mmss(start)}-{mmss(end)} | {title}",
                "",
                f"**源画面：** {source}",
                "",
                f"**UI图片：** `frames/{image_file}`",
                "",
                f"**回放锚点：** {anchor}",
                "",
                f"**解说：** {commentary}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--extractor", required=True, type=Path)
    parser.add_argument("--start", type=int, default=43249)
    parser.add_argument("--end", type=int, default=43268)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    extractor = load_extractor(args.extractor)
    failures: list[str] = []
    for numeric_id in range(args.start, args.end + 1):
        match_id = str(numeric_id)
        match_dir = args.root / match_id
        replay_path = match_dir / "replay.txt"
        output_path = match_dir / f"{match_id}_2x_ui_synced.md"
        try:
            if output_path.exists() and not args.overwrite:
                print(f"SKIP {match_id}: output exists")
                continue
            records = extractor.load_replay(replay_path)
            context = extractor.collect_context(records)
            summary = extractor.summarize(records, context)
            events = extractor.extract_events(records, context, False)
            output_path.write_text(build_document(match_id, records, summary, events), encoding="utf-8")
            print(f"OK {match_id}: {output_path}")
        except Exception as exc:  # Continue the requested batch on per-match failures.
            failures.append(f"{match_id}: {exc}")
            print(f"ERROR {match_id}: {exc}")
    if failures:
        print("FAILURES")
        for failure in failures:
            print(failure)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
