# Lychee Replay Commentary Timeline

Source: `C:\Users\Administrator\Documents\AI解说\00_0721_回放\解说稿\43252\replay.txt`
Duration: 600 rounds

## Teams

- BLUE: AAAA / v1.0
- RED: codex-py / 0.1

## Result

- BLUE AAAA/v1.0(2707): 80 points, good fruit 94, freshness 68.5, delivered False
- RED codex-py/0.1(2751): 578 points, good fruit 94, freshness 70.48, delivered True

## Commentary Events

| Round | Time | Priority | Event | Player | UI detail |
| --- | --- | --- | --- | --- | --- |
| R1 | 00:01 | HIGH | 派遣 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 派遣队伍清障 洞庭水驿(S05)，预计 R16 完成 |
| R1 | 00:01 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 1000, "edgeProgressPermille": 21, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.021312872975277068, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R1 | 00:01 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.95, "before": 100.0, "loss": 0.055, "playerId": 2751} |
| R1 | 00:01 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 5, "targetNodeId": "S06"} |
| R1 | 00:01 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.95, "before": 100.0, "loss": 0.05, "playerId": 2707} |
| R1 | 00:01 | MED | 任务刷新 |  | T_001 刷新在 梅关驿(S03)，路线 ROAD，截止 R221 |
| R1 | 00:01 | MED | 任务刷新 |  | T_002 刷新在 江南码头(S04)，路线 WATER，截止 R221 |
| R1 | 00:01 | MED | 任务刷新 |  | T_003 刷新在 秦岭栈道(S08)，路线 MOUNTAIN，截止 R221 |
| R2 | 00:02 | HIGH | 派遣 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 派遣队伍清障 武关(S10)，预计 R17 完成 |
| R2 | 00:02 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 4, "targetNodeId": "S06"} |
| R2 | 00:02 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.9, "before": 99.95, "loss": 0.05, "playerId": 2707} |
| R2 | 00:02 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 2000, "edgeProgressPermille": 42, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.042625745950554135, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R2 | 00:02 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.9, "before": 99.95, "loss": 0.055, "playerId": 2751} |
| R3 | 00:03 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 3, "targetNodeId": "S06"} |
| R3 | 00:03 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.85, "before": 99.9, "loss": 0.05, "playerId": 2707} |
| R3 | 00:03 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 3000, "edgeProgressPermille": 63, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.0639386189258312, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R3 | 00:03 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.85, "before": 99.9, "loss": 0.055, "playerId": 2751} |
| R4 | 00:04 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 4000, "edgeProgressPermille": 85, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.08525149190110827, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R4 | 00:04 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.79, "before": 99.85, "loss": 0.055, "playerId": 2751} |
| R4 | 00:04 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 2, "targetNodeId": "S06"} |
| R4 | 00:04 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.8, "before": 99.85, "loss": 0.05, "playerId": 2707} |
| R5 | 00:05 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 5000, "edgeProgressPermille": 106, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.10656436487638533, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R5 | 00:05 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.74, "before": 99.79, "loss": 0.055, "playerId": 2751} |
| R5 | 00:05 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 1, "targetNodeId": "S06"} |
| R5 | 00:05 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.75, "before": 99.8, "loss": 0.05, "playerId": 2707} |
| R6 | 00:06 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 0, "targetNodeId": "S06"} |
| R6 | 00:06 | HIGH | 障碍清除 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 清除 五岭山道(S06) 障碍 |
| R6 | 00:06 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.7, "before": 99.75, "loss": 0.05, "playerId": 2707} |
| R6 | 00:06 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 6000, "edgeProgressPermille": 127, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.1278772378516624, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R6 | 00:06 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.68, "before": 99.74, "loss": 0.055, "playerId": 2751} |
| R7 | 00:07 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 12, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.012484394506866416, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R7 | 00:07 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.63, "before": 99.7, "loss": 0.07, "playerId": 2707} |
| R7 | 00:07 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 7000, "edgeProgressPermille": 149, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.14919011082693948, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R7 | 00:07 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.63, "before": 99.68, "loss": 0.055, "playerId": 2751} |
| R8 | 00:08 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 8000, "edgeProgressPermille": 170, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.17050298380221654, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R8 | 00:08 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.57, "before": 99.63, "loss": 0.055, "playerId": 2751} |
| R8 | 00:08 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 24, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.024968789013732832, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R8 | 00:08 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.56, "before": 99.63, "loss": 0.07, "playerId": 2707} |
| R9 | 00:09 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 9000, "edgeProgressPermille": 191, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.1918158567774936, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R9 | 00:09 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.51, "before": 99.57, "loss": 0.055, "playerId": 2751} |
| R9 | 00:09 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 37, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.03745318352059925, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R9 | 00:09 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.49, "before": 99.56, "loss": 0.07, "playerId": 2707} |
| R10 | 00:10 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 49, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.049937578027465665, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R10 | 00:10 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.42, "before": 99.49, "loss": 0.07, "playerId": 2707} |
| R10 | 00:10 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 10000, "edgeProgressPermille": 213, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.21312872975277067, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R10 | 00:10 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.46, "before": 99.51, "loss": 0.055, "playerId": 2751} |
| R11 | 00:11 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 62, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.062421972534332085, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R11 | 00:11 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.35, "before": 99.42, "loss": 0.07, "playerId": 2707} |
| R11 | 00:11 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 11000, "edgeProgressPermille": 234, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.23444160272804773, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R11 | 00:11 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.4, "before": 99.46, "loss": 0.055, "playerId": 2751} |
| R12 | 00:12 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 12000, "edgeProgressPermille": 255, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.2557544757033248, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R12 | 00:12 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.35, "before": 99.4, "loss": 0.055, "playerId": 2751} |
| R12 | 00:12 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 74, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.0749063670411985, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R12 | 00:12 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.28, "before": 99.35, "loss": 0.07, "playerId": 2707} |
| R13 | 00:13 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 13000, "edgeProgressPermille": 277, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.2770673486786019, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R13 | 00:13 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.29, "before": 99.35, "loss": 0.055, "playerId": 2751} |
| R13 | 00:13 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 87, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.08739076154806492, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R13 | 00:13 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.21, "before": 99.28, "loss": 0.07, "playerId": 2707} |
| R14 | 00:14 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 99, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.09987515605493133, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R14 | 00:14 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.14, "before": 99.21, "loss": 0.07, "playerId": 2707} |
| R14 | 00:14 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 14000, "edgeProgressPermille": 298, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.29838022165387895, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R14 | 00:14 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.24, "before": 99.29, "loss": 0.055, "playerId": 2751} |
| R15 | 00:15 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 112, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.11235955056179775, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R15 | 00:15 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.07, "before": 99.14, "loss": 0.07, "playerId": 2707} |
| R15 | 00:15 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 15000, "edgeProgressPermille": 319, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.319693094629156, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R15 | 00:15 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.18, "before": 99.24, "loss": 0.055, "playerId": 2751} |
| R16 | 00:16 | HIGH | 清障完成 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 完成 洞庭水驿(S05) 清障 |
| R16 | 00:16 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 16000, "edgeProgressPermille": 341, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.3410059676044331, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R16 | 00:16 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.13, "before": 99.18, "loss": 0.055, "playerId": 2751} |
| R16 | 00:16 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 124, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.12484394506866417, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R16 | 00:16 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 99.0, "before": 99.07, "loss": 0.07, "playerId": 2707} |
| R17 | 00:17 | HIGH | 清障完成 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 完成 武关(S10) 清障 |
| R17 | 00:17 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 17000, "edgeProgressPermille": 362, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.36231884057971014, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R17 | 00:17 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.07, "before": 99.13, "loss": 0.055, "playerId": 2751} |
| R17 | 00:17 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 137, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.1373283395755306, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R17 | 00:17 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 98.93, "before": 99.0, "loss": 0.07, "playerId": 2707} |
| R18 | 00:18 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 12000, "edgeProgressPermille": 149, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.149812734082397, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R18 | 00:18 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 98.86, "before": 98.93, "loss": 0.07, "playerId": 2707} |
| R18 | 00:18 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 18000, "edgeProgressPermille": 383, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.3836317135549872, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R18 | 00:18 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 99.01, "before": 99.07, "loss": 0.055, "playerId": 2751} |
| R19 | 00:19 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 13000, "edgeProgressPermille": 162, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.16229712858926343, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R19 | 00:19 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 98.79, "before": 98.86, "loss": 0.07, "playerId": 2707} |
| R19 | 00:19 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 19000, "edgeProgressPermille": 404, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.40494458653026427, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R19 | 00:19 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.96, "before": 99.01, "loss": 0.055, "playerId": 2751} |
| R20 | 00:20 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 20000, "edgeProgressPermille": 426, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.42625745950554134, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R20 | 00:20 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.9, "before": 98.96, "loss": 0.055, "playerId": 2751} |
| R20 | 00:20 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 174, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.17478152309612985, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R20 | 00:20 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 98.72, "before": 98.79, "loss": 0.07, "playerId": 2707} |
| R21 | 00:21 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 21000, "edgeProgressPermille": 447, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.4475703324808184, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R21 | 00:21 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.85, "before": 98.9, "loss": 0.055, "playerId": 2751} |
| R21 | 00:21 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 15000, "edgeProgressPermille": 187, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.18726591760299627, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R21 | 00:21 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 98.65, "before": 98.72, "loss": 0.07, "playerId": 2707} |
| R22 | 00:22 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 16000, "edgeProgressPermille": 199, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.19975031210986266, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R22 | 00:22 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 98.58, "before": 98.65, "loss": 0.07, "playerId": 2707} |
| R22 | 00:22 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 22000, "edgeProgressPermille": 468, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.46888320545609546, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R22 | 00:22 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.79, "before": 98.85, "loss": 0.055, "playerId": 2751} |
| R23 | 00:23 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 17000, "edgeProgressPermille": 212, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.21223470661672908, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R23 | 00:23 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 98.51, "before": 98.58, "loss": 0.07, "playerId": 2707} |
| R23 | 00:23 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 23000, "edgeProgressPermille": 490, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.49019607843137253, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R23 | 00:23 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.74, "before": 98.79, "loss": 0.055, "playerId": 2751} |
| R24 | 00:24 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 24000, "edgeProgressPermille": 511, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.5115089514066496, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R24 | 00:24 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.68, "before": 98.74, "loss": 0.055, "playerId": 2751} |
| R24 | 00:24 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 18000, "edgeProgressPermille": 224, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.2247191011235955, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R24 | 00:24 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 98.44, "before": 98.51, "loss": 0.07, "playerId": 2707} |
| R25 | 00:25 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 25000, "edgeProgressPermille": 532, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.5328218243819267, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R25 | 00:25 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.63, "before": 98.68, "loss": 0.055, "playerId": 2751} |
| R25 | 00:25 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 19000, "edgeProgressPermille": 237, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.23720349563046192, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R25 | 00:25 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 98.37, "before": 98.44, "loss": 0.07, "playerId": 2707} |
| R26 | 00:26 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 20000, "edgeProgressPermille": 249, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.24968789013732834, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R26 | 00:26 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 98.3, "before": 98.37, "loss": 0.07, "playerId": 2707} |
| R26 | 00:26 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 26000, "edgeProgressPermille": 554, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.5541346973572038, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R26 | 00:26 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.57, "before": 98.63, "loss": 0.055, "playerId": 2751} |
| R27 | 00:27 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 21000, "edgeProgressPermille": 262, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.26217228464419473, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R27 | 00:27 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 98.23, "before": 98.3, "loss": 0.07, "playerId": 2707} |
| R27 | 00:27 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 27000, "edgeProgressPermille": 575, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.5754475703324808, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R27 | 00:27 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.51, "before": 98.57, "loss": 0.055, "playerId": 2751} |
| R28 | 00:28 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 28000, "edgeProgressPermille": 596, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.5967604433077579, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R28 | 00:28 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.46, "before": 98.51, "loss": 0.055, "playerId": 2751} |
| R28 | 00:28 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 22000, "edgeProgressPermille": 274, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.2746566791510612, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R28 | 00:28 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 98.16, "before": 98.23, "loss": 0.07, "playerId": 2707} |
| R29 | 00:29 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 29000, "edgeProgressPermille": 618, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.618073316283035, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R29 | 00:29 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.4, "before": 98.46, "loss": 0.055, "playerId": 2751} |
| R29 | 00:29 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 23000, "edgeProgressPermille": 287, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.28714107365792757, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R29 | 00:29 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 98.09, "before": 98.16, "loss": 0.07, "playerId": 2707} |
| R30 | 00:30 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 24000, "edgeProgressPermille": 299, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.299625468164794, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R30 | 00:30 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 98.02, "before": 98.09, "loss": 0.07, "playerId": 2707} |
| R30 | 00:30 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 30000, "edgeProgressPermille": 639, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.639386189258312, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R30 | 00:30 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.35, "before": 98.4, "loss": 0.055, "playerId": 2751} |
| R30 | 00:30 | MED | 任务刷新 |  | T_004 刷新在 梅关驿(S03)，路线 ROAD，截止 R210 |
| R31 | 00:31 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 25000, "edgeProgressPermille": 312, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.3121098626716604, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R31 | 00:31 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 97.95, "before": 98.02, "loss": 0.07, "playerId": 2707} |
| R31 | 00:31 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 31000, "edgeProgressPermille": 660, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.6606990622335891, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R31 | 00:31 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.29, "before": 98.35, "loss": 0.055, "playerId": 2751} |
| R32 | 00:32 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 32000, "edgeProgressPermille": 682, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.6820119352088662, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R32 | 00:32 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.24, "before": 98.29, "loss": 0.055, "playerId": 2751} |
| R32 | 00:32 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 26000, "edgeProgressPermille": 324, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.32459425717852686, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R32 | 00:32 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 97.88, "before": 97.95, "loss": 0.07, "playerId": 2707} |
| R33 | 00:33 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 33000, "edgeProgressPermille": 703, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.7033248081841432, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R33 | 00:33 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.18, "before": 98.24, "loss": 0.055, "playerId": 2751} |
| R33 | 00:33 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 27000, "edgeProgressPermille": 337, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.33707865168539325, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R33 | 00:33 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 97.81, "before": 97.88, "loss": 0.07, "playerId": 2707} |
| R34 | 00:34 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 28000, "edgeProgressPermille": 349, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.3495630461922597, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R34 | 00:34 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 97.74, "before": 97.81, "loss": 0.07, "playerId": 2707} |
| R34 | 00:34 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 34000, "edgeProgressPermille": 724, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.7246376811594203, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R34 | 00:34 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.13, "before": 98.18, "loss": 0.055, "playerId": 2751} |
| R35 | 00:35 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 29000, "edgeProgressPermille": 362, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.3620474406991261, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R35 | 00:35 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 97.67, "before": 97.74, "loss": 0.07, "playerId": 2707} |
| R35 | 00:35 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 35000, "edgeProgressPermille": 745, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.7459505541346974, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R35 | 00:35 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.07, "before": 98.13, "loss": 0.055, "playerId": 2751} |
| R36 | 00:36 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 36000, "edgeProgressPermille": 767, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.7672634271099744, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R36 | 00:36 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 98.01, "before": 98.07, "loss": 0.055, "playerId": 2751} |
| R36 | 00:36 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 30000, "edgeProgressPermille": 374, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.37453183520599254, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R36 | 00:36 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 97.6, "before": 97.67, "loss": 0.07, "playerId": 2707} |
| R37 | 00:37 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 37000, "edgeProgressPermille": 788, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.7885763000852515, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R37 | 00:37 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.96, "before": 98.01, "loss": 0.055, "playerId": 2751} |
| R37 | 00:37 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 31000, "edgeProgressPermille": 387, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.38701622971285893, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R37 | 00:37 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 97.53, "before": 97.6, "loss": 0.07, "playerId": 2707} |
| R38 | 00:38 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 32000, "edgeProgressPermille": 399, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.3995006242197253, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R38 | 00:38 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 97.46, "before": 97.53, "loss": 0.07, "playerId": 2707} |
| R38 | 00:38 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 38000, "edgeProgressPermille": 809, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.8098891730605285, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R38 | 00:38 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.9, "before": 97.96, "loss": 0.055, "playerId": 2751} |
| R39 | 00:39 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 33000, "edgeProgressPermille": 411, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.41198501872659177, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R39 | 00:39 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 97.39, "before": 97.46, "loss": 0.07, "playerId": 2707} |
| R39 | 00:39 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 39000, "edgeProgressPermille": 831, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.8312020460358056, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R39 | 00:39 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.85, "before": 97.9, "loss": 0.055, "playerId": 2751} |
| R40 | 00:40 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 40000, "edgeProgressPermille": 852, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.8525149190110827, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R40 | 00:40 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.79, "before": 97.85, "loss": 0.055, "playerId": 2751} |
| R40 | 00:40 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 34000, "edgeProgressPermille": 424, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.42446941323345816, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R40 | 00:40 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 97.32, "before": 97.39, "loss": 0.07, "playerId": 2707} |
| R41 | 00:41 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 41000, "edgeProgressPermille": 873, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.8738277919863597, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R41 | 00:41 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.74, "before": 97.79, "loss": 0.055, "playerId": 2751} |
| R41 | 00:41 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 35000, "edgeProgressPermille": 436, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.4369538077403246, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R41 | 00:41 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 97.25, "before": 97.32, "loss": 0.07, "playerId": 2707} |
| R42 | 00:42 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 36000, "edgeProgressPermille": 449, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.449438202247191, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R42 | 00:42 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 97.18, "before": 97.25, "loss": 0.07, "playerId": 2707} |
| R42 | 00:42 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 42000, "edgeProgressPermille": 895, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.8951406649616368, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R42 | 00:42 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.68, "before": 97.74, "loss": 0.055, "playerId": 2751} |
| R43 | 00:43 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 37000, "edgeProgressPermille": 461, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.46192259675405745, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R43 | 00:43 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 97.11, "before": 97.18, "loss": 0.07, "playerId": 2707} |
| R43 | 00:43 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 43000, "edgeProgressPermille": 916, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.9164535379369139, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R43 | 00:43 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.63, "before": 97.68, "loss": 0.055, "playerId": 2751} |
| R44 | 00:44 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 44000, "edgeProgressPermille": 937, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.9377664109121909, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R44 | 00:44 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.57, "before": 97.63, "loss": 0.055, "playerId": 2751} |
| R44 | 00:44 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 38000, "edgeProgressPermille": 474, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.47440699126092384, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R44 | 00:44 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 97.04, "before": 97.11, "loss": 0.07, "playerId": 2707} |
| R45 | 00:45 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 45000, "edgeProgressPermille": 959, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.959079283887468, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R45 | 00:45 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.51, "before": 97.57, "loss": 0.055, "playerId": 2751} |
| R45 | 00:45 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 39000, "edgeProgressPermille": 486, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.4868913857677903, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R45 | 00:45 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 96.97, "before": 97.04, "loss": 0.07, "playerId": 2707} |
| R46 | 00:46 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 40000, "edgeProgressPermille": 499, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.4993757802746567, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R46 | 00:46 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 96.9, "before": 96.97, "loss": 0.07, "playerId": 2707} |
| R46 | 00:46 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 46000, "edgeProgressPermille": 980, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 0.9803921568627451, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R46 | 00:46 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.46, "before": 97.51, "loss": 0.055, "playerId": 2751} |
| R47 | 00:47 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 41000, "edgeProgressPermille": 511, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5118601747815231, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R47 | 00:47 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 96.83, "before": 96.9, "loss": 0.07, "playerId": 2707} |
| R47 | 00:47 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 46920, "edgeProgressPermille": 1000, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2751, "progress": 1.0, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R47 | 00:47 | HIGH | 进点 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 进入 南岭驿(S02) |
| R47 | 00:47 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.4, "before": 97.46, "loss": 0.055, "playerId": 2751} |
| R48 | 00:48 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 1000, "edgeProgressPermille": 13, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.013175230566534914, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R48 | 00:48 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.35, "before": 97.4, "loss": 0.055, "playerId": 2751} |
| R48 | 00:48 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 42000, "edgeProgressPermille": 524, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5243445692883895, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R48 | 00:48 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 96.76, "before": 96.83, "loss": 0.07, "playerId": 2707} |
| R49 | 00:49 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 2000, "edgeProgressPermille": 26, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.026350461133069828, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R49 | 00:49 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.29, "before": 97.35, "loss": 0.055, "playerId": 2751} |
| R49 | 00:49 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 43000, "edgeProgressPermille": 536, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5368289637952559, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R49 | 00:49 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 96.69, "before": 96.76, "loss": 0.07, "playerId": 2707} |
| R50 | 00:50 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 44000, "edgeProgressPermille": 549, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5493133583021224, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R50 | 00:50 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 96.62, "before": 96.69, "loss": 0.07, "playerId": 2707} |
| R50 | 00:50 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 3000, "edgeProgressPermille": 39, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.039525691699604744, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R50 | 00:50 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.24, "before": 97.29, "loss": 0.055, "playerId": 2751} |
| R51 | 00:51 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 45000, "edgeProgressPermille": 561, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5617977528089888, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R51 | 00:51 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 96.55, "before": 96.62, "loss": 0.07, "playerId": 2707} |
| R51 | 00:51 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 4000, "edgeProgressPermille": 52, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.052700922266139656, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R51 | 00:51 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.18, "before": 97.24, "loss": 0.055, "playerId": 2751} |
| R52 | 00:52 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 5000, "edgeProgressPermille": 65, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.06587615283267458, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R52 | 00:52 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.13, "before": 97.18, "loss": 0.055, "playerId": 2751} |
| R52 | 00:52 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 46000, "edgeProgressPermille": 574, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5742821473158551, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R52 | 00:52 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 96.48, "before": 96.55, "loss": 0.07, "playerId": 2707} |
| R53 | 00:53 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 6000, "edgeProgressPermille": 79, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.07905138339920949, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R53 | 00:53 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.07, "before": 97.13, "loss": 0.055, "playerId": 2751} |
| R53 | 00:53 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 47000, "edgeProgressPermille": 586, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5867665418227216, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R53 | 00:53 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 96.41, "before": 96.48, "loss": 0.07, "playerId": 2707} |
| R54 | 00:54 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 48000, "edgeProgressPermille": 599, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.599250936329588, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R54 | 00:54 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 96.34, "before": 96.41, "loss": 0.07, "playerId": 2707} |
| R54 | 00:54 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 7000, "edgeProgressPermille": 92, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.0922266139657444, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R54 | 00:54 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 97.01, "before": 97.07, "loss": 0.055, "playerId": 2751} |
| R55 | 00:55 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 49000, "edgeProgressPermille": 611, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6117353308364545, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R55 | 00:55 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 96.27, "before": 96.34, "loss": 0.07, "playerId": 2707} |
| R55 | 00:55 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 8000, "edgeProgressPermille": 105, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.10540184453227931, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R55 | 00:55 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.96, "before": 97.01, "loss": 0.055, "playerId": 2751} |
| R56 | 00:56 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 9000, "edgeProgressPermille": 118, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.11857707509881422, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R56 | 00:56 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.9, "before": 96.96, "loss": 0.055, "playerId": 2751} |
| R56 | 00:56 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 50000, "edgeProgressPermille": 624, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6242197253433208, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R56 | 00:56 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 96.2, "before": 96.27, "loss": 0.07, "playerId": 2707} |
| R57 | 00:57 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 10000, "edgeProgressPermille": 131, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.13175230566534915, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R57 | 00:57 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.85, "before": 96.9, "loss": 0.055, "playerId": 2751} |
| R57 | 00:57 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 51000, "edgeProgressPermille": 636, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6367041198501873, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R57 | 00:57 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 96.13, "before": 96.2, "loss": 0.07, "playerId": 2707} |
| R58 | 00:58 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 52000, "edgeProgressPermille": 649, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6491885143570537, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R58 | 00:58 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 96.06, "before": 96.13, "loss": 0.07, "playerId": 2707} |
| R58 | 00:58 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 11000, "edgeProgressPermille": 144, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.14492753623188406, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R58 | 00:58 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.79, "before": 96.85, "loss": 0.055, "playerId": 2751} |
| R59 | 00:59 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 53000, "edgeProgressPermille": 661, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.66167290886392, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R59 | 00:59 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 95.99, "before": 96.06, "loss": 0.07, "playerId": 2707} |
| R59 | 00:59 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 12000, "edgeProgressPermille": 158, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.15810276679841898, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R59 | 00:59 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.74, "before": 96.79, "loss": 0.055, "playerId": 2751} |
| R60 | 01:00 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 13000, "edgeProgressPermille": 171, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.1712779973649539, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R60 | 01:00 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.68, "before": 96.74, "loss": 0.055, "playerId": 2751} |
| R60 | 01:00 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 54000, "edgeProgressPermille": 674, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6741573033707865, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R60 | 01:00 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 95.92, "before": 95.99, "loss": 0.07, "playerId": 2707} |
| R60 | 01:00 | MED | 任务刷新 |  | T_005 刷新在 五岭山道(S06)，路线 MOUNTAIN，截止 R240 |
| R61 | 01:01 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 14000, "edgeProgressPermille": 184, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.1844532279314888, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R61 | 01:01 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.63, "before": 96.68, "loss": 0.055, "playerId": 2751} |
| R61 | 01:01 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 55000, "edgeProgressPermille": 686, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.686641697877653, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R61 | 01:01 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 95.85, "before": 95.92, "loss": 0.07, "playerId": 2707} |
| R62 | 01:02 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 56000, "edgeProgressPermille": 699, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6991260923845194, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R62 | 01:02 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 95.78, "before": 95.85, "loss": 0.07, "playerId": 2707} |
| R62 | 01:02 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 15000, "edgeProgressPermille": 197, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.1976284584980237, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R62 | 01:02 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.57, "before": 96.63, "loss": 0.055, "playerId": 2751} |
| R63 | 01:03 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 57000, "edgeProgressPermille": 711, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7116104868913857, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R63 | 01:03 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 95.71, "before": 95.78, "loss": 0.07, "playerId": 2707} |
| R63 | 01:03 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 16000, "edgeProgressPermille": 210, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.21080368906455862, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R63 | 01:03 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.51, "before": 96.57, "loss": 0.055, "playerId": 2751} |
| R64 | 01:04 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 17000, "edgeProgressPermille": 223, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.22397891963109354, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R64 | 01:04 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.46, "before": 96.51, "loss": 0.055, "playerId": 2751} |
| R64 | 01:04 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 58000, "edgeProgressPermille": 724, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7240948813982522, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R64 | 01:04 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 95.64, "before": 95.71, "loss": 0.07, "playerId": 2707} |
| R65 | 01:05 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 18000, "edgeProgressPermille": 237, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.23715415019762845, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R65 | 01:05 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.4, "before": 96.46, "loss": 0.055, "playerId": 2751} |
| R65 | 01:05 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 59000, "edgeProgressPermille": 736, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7365792759051186, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R65 | 01:05 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 95.57, "before": 95.64, "loss": 0.07, "playerId": 2707} |
| R66 | 01:06 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 60000, "edgeProgressPermille": 749, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7490636704119851, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R66 | 01:06 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 95.5, "before": 95.57, "loss": 0.07, "playerId": 2707} |
| R66 | 01:06 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 19000, "edgeProgressPermille": 250, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.2503293807641634, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R66 | 01:06 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.35, "before": 96.4, "loss": 0.055, "playerId": 2751} |
| R67 | 01:07 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 61000, "edgeProgressPermille": 761, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7615480649188514, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R67 | 01:07 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 95.43, "before": 95.5, "loss": 0.07, "playerId": 2707} |
| R67 | 01:07 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 20000, "edgeProgressPermille": 263, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.2635046113306983, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R67 | 01:07 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.29, "before": 96.35, "loss": 0.055, "playerId": 2751} |
| R68 | 01:08 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 21000, "edgeProgressPermille": 276, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.2766798418972332, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R68 | 01:08 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.24, "before": 96.29, "loss": 0.055, "playerId": 2751} |
| R68 | 01:08 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 62000, "edgeProgressPermille": 774, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7740324594257179, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R68 | 01:08 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 95.36, "before": 95.43, "loss": 0.07, "playerId": 2707} |
| R69 | 01:09 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 22000, "edgeProgressPermille": 289, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.2898550724637681, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R69 | 01:09 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.18, "before": 96.24, "loss": 0.055, "playerId": 2751} |
| R69 | 01:09 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 63000, "edgeProgressPermille": 786, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7865168539325843, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R69 | 01:09 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 95.29, "before": 95.36, "loss": 0.07, "playerId": 2707} |
| R70 | 01:10 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 64000, "edgeProgressPermille": 799, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7990012484394506, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R70 | 01:10 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 95.22, "before": 95.29, "loss": 0.07, "playerId": 2707} |
| R70 | 01:10 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 23000, "edgeProgressPermille": 303, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.30303030303030304, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R70 | 01:10 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.13, "before": 96.18, "loss": 0.055, "playerId": 2751} |
| R71 | 01:11 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 65000, "edgeProgressPermille": 811, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8114856429463171, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R71 | 01:11 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 95.15, "before": 95.22, "loss": 0.07, "playerId": 2707} |
| R71 | 01:11 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 24000, "edgeProgressPermille": 316, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.31620553359683795, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R71 | 01:11 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.07, "before": 96.13, "loss": 0.055, "playerId": 2751} |
| R72 | 01:12 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 25000, "edgeProgressPermille": 329, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.32938076416337286, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R72 | 01:12 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 96.01, "before": 96.07, "loss": 0.055, "playerId": 2751} |
| R72 | 01:12 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 66000, "edgeProgressPermille": 823, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8239700374531835, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R72 | 01:12 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 95.08, "before": 95.15, "loss": 0.07, "playerId": 2707} |
| R73 | 01:13 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 26000, "edgeProgressPermille": 342, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.3425559947299078, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R73 | 01:13 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.96, "before": 96.01, "loss": 0.055, "playerId": 2751} |
| R73 | 01:13 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 67000, "edgeProgressPermille": 836, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.83645443196005, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R73 | 01:13 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 95.01, "before": 95.08, "loss": 0.07, "playerId": 2707} |
| R74 | 01:14 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 68000, "edgeProgressPermille": 848, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8489388264669163, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R74 | 01:14 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.94, "before": 95.01, "loss": 0.07, "playerId": 2707} |
| R74 | 01:14 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 27000, "edgeProgressPermille": 355, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.3557312252964427, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R74 | 01:14 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.9, "before": 95.96, "loss": 0.055, "playerId": 2751} |
| R75 | 01:15 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 69000, "edgeProgressPermille": 861, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8614232209737828, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R75 | 01:15 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.87, "before": 94.94, "loss": 0.07, "playerId": 2707} |
| R75 | 01:15 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 28000, "edgeProgressPermille": 368, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.3689064558629776, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R75 | 01:15 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.85, "before": 95.9, "loss": 0.055, "playerId": 2751} |
| R76 | 01:16 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 29000, "edgeProgressPermille": 382, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.3820816864295125, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R76 | 01:16 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.79, "before": 95.85, "loss": 0.055, "playerId": 2751} |
| R76 | 01:16 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 70000, "edgeProgressPermille": 873, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8739076154806492, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R76 | 01:16 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.8, "before": 94.87, "loss": 0.07, "playerId": 2707} |
| R77 | 01:17 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 30000, "edgeProgressPermille": 395, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.3952569169960474, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R77 | 01:17 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.74, "before": 95.79, "loss": 0.055, "playerId": 2751} |
| R77 | 01:17 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 71000, "edgeProgressPermille": 886, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8863920099875156, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R77 | 01:17 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.73, "before": 94.8, "loss": 0.07, "playerId": 2707} |
| R78 | 01:18 | HIGH | 派遣 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 派遣队伍侦察 洞庭水驿(S05)，预计 R91 完成 |
| R78 | 01:18 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 72000, "edgeProgressPermille": 898, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.898876404494382, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R78 | 01:18 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.66, "before": 94.73, "loss": 0.07, "playerId": 2707} |
| R78 | 01:18 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 31000, "edgeProgressPermille": 408, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.40843214756258234, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R78 | 01:18 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.68, "before": 95.74, "loss": 0.055, "playerId": 2751} |
| R79 | 01:19 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 73000, "edgeProgressPermille": 911, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9113607990012484, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R79 | 01:19 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.59, "before": 94.66, "loss": 0.07, "playerId": 2707} |
| R79 | 01:19 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 32000, "edgeProgressPermille": 421, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.42160737812911725, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R79 | 01:19 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.63, "before": 95.68, "loss": 0.055, "playerId": 2751} |
| R80 | 01:20 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 33000, "edgeProgressPermille": 434, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.43478260869565216, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R80 | 01:20 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.57, "before": 95.63, "loss": 0.055, "playerId": 2751} |
| R80 | 01:20 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 74000, "edgeProgressPermille": 923, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9238451935081149, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R80 | 01:20 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.52, "before": 94.59, "loss": 0.07, "playerId": 2707} |
| R81 | 01:21 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 34000, "edgeProgressPermille": 447, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.4479578392621871, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R81 | 01:21 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.51, "before": 95.57, "loss": 0.055, "playerId": 2751} |
| R81 | 01:21 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 75000, "edgeProgressPermille": 936, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9363295880149812, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R81 | 01:21 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.45, "before": 94.52, "loss": 0.07, "playerId": 2707} |
| R82 | 01:22 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 76000, "edgeProgressPermille": 948, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9488139825218477, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R82 | 01:22 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.38, "before": 94.45, "loss": 0.07, "playerId": 2707} |
| R82 | 01:22 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 35000, "edgeProgressPermille": 461, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.461133069828722, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R82 | 01:22 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.46, "before": 95.51, "loss": 0.055, "playerId": 2751} |
| R83 | 01:23 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 77000, "edgeProgressPermille": 961, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9612983770287141, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R83 | 01:23 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.31, "before": 94.38, "loss": 0.07, "playerId": 2707} |
| R83 | 01:23 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 36000, "edgeProgressPermille": 474, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.4743083003952569, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R83 | 01:23 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.4, "before": 95.46, "loss": 0.055, "playerId": 2751} |
| R84 | 01:24 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 37000, "edgeProgressPermille": 487, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.4874835309617918, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R84 | 01:24 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.35, "before": 95.4, "loss": 0.055, "playerId": 2751} |
| R84 | 01:24 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 78000, "edgeProgressPermille": 973, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9737827715355806, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R84 | 01:24 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.24, "before": 94.31, "loss": 0.07, "playerId": 2707} |
| R85 | 01:25 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 38000, "edgeProgressPermille": 500, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.5006587615283268, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R85 | 01:25 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.29, "before": 95.35, "loss": 0.055, "playerId": 2751} |
| R85 | 01:25 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 79000, "edgeProgressPermille": 986, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9862671660424469, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R85 | 01:25 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.17, "before": 94.24, "loss": 0.07, "playerId": 2707} |
| R86 | 01:26 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 80000, "edgeProgressPermille": 998, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9987515605493134, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R86 | 01:26 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.1, "before": 94.17, "loss": 0.07, "playerId": 2707} |
| R86 | 01:26 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 39000, "edgeProgressPermille": 513, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.5138339920948617, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R86 | 01:26 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.24, "before": 95.29, "loss": 0.055, "playerId": 2751} |
| R87 | 01:27 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 80100, "edgeProgressPermille": 1000, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 1.0, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R87 | 01:27 | HIGH | 进点 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 进入 五岭山道(S06) |
| R87 | 01:27 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.03, "before": 94.1, "loss": 0.07, "playerId": 2707} |
| R87 | 01:27 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 40000, "edgeProgressPermille": 527, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.5270092226613966, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R87 | 01:27 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.18, "before": 95.24, "loss": 0.055, "playerId": 2751} |
| R88 | 01:28 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 41000, "edgeProgressPermille": 540, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.5401844532279315, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R88 | 01:28 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.13, "before": 95.18, "loss": 0.055, "playerId": 2751} |
| R88 | 01:28 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_RESOURCE", "remainingRound": 1, "targetNodeId": "S06"} |
| R88 | 01:28 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.98, "before": 94.03, "loss": 0.05, "playerId": 2707} |
| R89 | 01:29 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 42000, "edgeProgressPermille": 553, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.5533596837944664, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R89 | 01:29 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.07, "before": 95.13, "loss": 0.055, "playerId": 2751} |
| R89 | 01:29 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_RESOURCE", "remainingRound": 0, "targetNodeId": "S06"} |
| R89 | 01:29 | MED | 资源领取 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 在 五岭山道(S06) 领取冰鉴 |
| R89 | 01:29 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.93, "before": 93.98, "loss": 0.05, "playerId": 2707} |
| R90 | 01:30 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 9, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.009856003784705454, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R90 | 01:30 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.86, "before": 93.93, "loss": 0.07, "playerId": 2707} |
| R90 | 01:30 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 43000, "edgeProgressPermille": 566, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.5665349143610013, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R90 | 01:30 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 95.01, "before": 95.07, "loss": 0.055, "playerId": 2751} |
| R91 | 01:31 | MED | SCOUT_MARKER_ADD | RED codex-py/0.1(2751) | {"expireRound": 136, "playerId": 2751, "remainingTriggers": 1, "targetNodeId": "S05"} |
| R91 | 01:31 | MED | 侦察回报 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 侦察 洞庭水驿(S05)：无障碍，资源 通关凭证 |
| R91 | 01:31 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 19, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.019712007569410907, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R91 | 01:31 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.79, "before": 93.86, "loss": 0.07, "playerId": 2707} |
| R91 | 01:31 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 44000, "edgeProgressPermille": 579, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.5797101449275363, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R91 | 01:31 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.96, "before": 95.01, "loss": 0.055, "playerId": 2751} |
| R92 | 01:32 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 45000, "edgeProgressPermille": 592, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.5928853754940712, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R92 | 01:32 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.9, "before": 94.96, "loss": 0.055, "playerId": 2751} |
| R92 | 01:32 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 29, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.02956801135411636, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R92 | 01:32 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.72, "before": 93.79, "loss": 0.07, "playerId": 2707} |
| R93 | 01:33 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 46000, "edgeProgressPermille": 606, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.6060606060606061, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R93 | 01:33 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.85, "before": 94.9, "loss": 0.055, "playerId": 2751} |
| R93 | 01:33 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 39, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.039424015138821815, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R93 | 01:33 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.65, "before": 93.72, "loss": 0.07, "playerId": 2707} |
| R94 | 01:34 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 49, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.04928001892352726, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R94 | 01:34 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.58, "before": 93.65, "loss": 0.07, "playerId": 2707} |
| R94 | 01:34 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 47000, "edgeProgressPermille": 619, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.619235836627141, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R94 | 01:34 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.79, "before": 94.85, "loss": 0.055, "playerId": 2751} |
| R95 | 01:35 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 59, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.05913602270823272, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R95 | 01:35 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.51, "before": 93.58, "loss": 0.07, "playerId": 2707} |
| R95 | 01:35 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 48000, "edgeProgressPermille": 632, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.6324110671936759, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R95 | 01:35 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.74, "before": 94.79, "loss": 0.055, "playerId": 2751} |
| R96 | 01:36 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 49000, "edgeProgressPermille": 645, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.6455862977602108, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R96 | 01:36 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.68, "before": 94.74, "loss": 0.055, "playerId": 2751} |
| R96 | 01:36 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 68, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.06899202649293817, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R96 | 01:36 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.44, "before": 93.51, "loss": 0.07, "playerId": 2707} |
| R97 | 01:37 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 50000, "edgeProgressPermille": 658, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.6587615283267457, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R97 | 01:37 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.63, "before": 94.68, "loss": 0.055, "playerId": 2751} |
| R97 | 01:37 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 78, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.07884803027764363, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R97 | 01:37 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.37, "before": 93.44, "loss": 0.07, "playerId": 2707} |
| R98 | 01:38 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 88, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.08870403406234909, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R98 | 01:38 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.3, "before": 93.37, "loss": 0.07, "playerId": 2707} |
| R98 | 01:38 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 51000, "edgeProgressPermille": 671, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.6719367588932806, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R98 | 01:38 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.57, "before": 94.63, "loss": 0.055, "playerId": 2751} |
| R99 | 01:39 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 98, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.09856003784705453, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R99 | 01:39 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.23, "before": 93.3, "loss": 0.07, "playerId": 2707} |
| R99 | 01:39 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 52000, "edgeProgressPermille": 685, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.6851119894598156, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R99 | 01:39 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.51, "before": 94.57, "loss": 0.055, "playerId": 2751} |
| R100 | 01:40 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 53000, "edgeProgressPermille": 698, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.6982872200263505, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R100 | 01:40 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.46, "before": 94.51, "loss": 0.055, "playerId": 2751} |
| R100 | 01:40 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 108, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.10841604163175998, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R100 | 01:40 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.16, "before": 93.23, "loss": 0.07, "playerId": 2707} |
| R100 | 01:40 | MED | 任务刷新 |  | T_006 刷新在 江南码头(S04)，路线 WATER，截止 R320 |
| R100 | 01:40 | MED | 任务刷新 |  | T_007 刷新在 荆襄大驿(S07)，路线 ROAD，截止 R320 |
| R100 | 01:40 | MED | 任务刷新 |  | T_008 刷新在 洛阳驿(S09)，路线 WATER，截止 R320 |
| R100 | 01:40 | MED | 任务刷新 |  | T_009 刷新在 秦岭栈道(S08)，路线 MOUNTAIN，截止 R320 |
| R101 | 01:41 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 54000, "edgeProgressPermille": 711, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.7114624505928854, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R101 | 01:41 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.4, "before": 94.46, "loss": 0.055, "playerId": 2751} |
| R101 | 01:41 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 12000, "edgeProgressPermille": 118, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.11827204541646544, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R101 | 01:41 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.09, "before": 93.16, "loss": 0.07, "playerId": 2707} |
| R102 | 01:42 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 13000, "edgeProgressPermille": 128, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.1281280492011709, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R102 | 01:42 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.02, "before": 93.09, "loss": 0.07, "playerId": 2707} |
| R102 | 01:42 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 55000, "edgeProgressPermille": 724, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.7246376811594203, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R102 | 01:42 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.35, "before": 94.4, "loss": 0.055, "playerId": 2751} |
| R103 | 01:43 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 137, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.13798405298587635, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R103 | 01:43 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.95, "before": 93.02, "loss": 0.07, "playerId": 2707} |
| R103 | 01:43 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 56000, "edgeProgressPermille": 737, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.7378129117259552, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R103 | 01:43 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.29, "before": 94.35, "loss": 0.055, "playerId": 2751} |
| R104 | 01:44 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 57000, "edgeProgressPermille": 750, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.7509881422924901, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R104 | 01:44 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.24, "before": 94.29, "loss": 0.055, "playerId": 2751} |
| R104 | 01:44 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 15000, "edgeProgressPermille": 147, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.1478400567705818, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R104 | 01:44 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.88, "before": 92.95, "loss": 0.07, "playerId": 2707} |
| R105 | 01:45 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 58000, "edgeProgressPermille": 764, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.764163372859025, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R105 | 01:45 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.18, "before": 94.24, "loss": 0.055, "playerId": 2751} |
| R105 | 01:45 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 16000, "edgeProgressPermille": 157, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.15769606055528726, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R105 | 01:45 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.81, "before": 92.88, "loss": 0.07, "playerId": 2707} |
| R106 | 01:46 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 17000, "edgeProgressPermille": 167, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.1675520643399927, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R106 | 01:46 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.74, "before": 92.81, "loss": 0.07, "playerId": 2707} |
| R106 | 01:46 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 59000, "edgeProgressPermille": 777, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.7773386034255599, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R106 | 01:46 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.13, "before": 94.18, "loss": 0.055, "playerId": 2751} |
| R107 | 01:47 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 18000, "edgeProgressPermille": 177, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.17740806812469817, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R107 | 01:47 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.67, "before": 92.74, "loss": 0.07, "playerId": 2707} |
| R107 | 01:47 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 60000, "edgeProgressPermille": 790, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.7905138339920948, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R107 | 01:47 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 94.07, "before": 94.13, "loss": 0.055, "playerId": 2751} |
| R108 | 01:48 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 61000, "edgeProgressPermille": 803, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.8036890645586298, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R108 | 01:48 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 93.99, "before": 94.07, "loss": 0.0825, "playerId": 2751} |
| R108 | 01:48 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 19000, "edgeProgressPermille": 187, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.1872640719094036, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R108 | 01:48 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.57, "before": 92.67, "loss": 0.10500000000000001, "playerId": 2707} |
| R109 | 01:49 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 62000, "edgeProgressPermille": 816, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.8168642951251647, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R109 | 01:49 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 93.91, "before": 93.99, "loss": 0.0825, "playerId": 2751} |
| R109 | 01:49 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 20000, "edgeProgressPermille": 197, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.19712007569410905, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R109 | 01:49 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.46, "before": 92.57, "loss": 0.10500000000000001, "playerId": 2707} |
| R110 | 01:50 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 21000, "edgeProgressPermille": 206, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.20697607947881452, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R110 | 01:50 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.35, "before": 92.46, "loss": 0.10500000000000001, "playerId": 2707} |
| R110 | 01:50 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 63000, "edgeProgressPermille": 830, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.8300395256916996, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R110 | 01:50 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 93.83, "before": 93.91, "loss": 0.0825, "playerId": 2751} |
| R111 | 01:51 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 22000, "edgeProgressPermille": 216, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.21683208326351996, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R111 | 01:51 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.24, "before": 92.35, "loss": 0.10500000000000001, "playerId": 2707} |
| R111 | 01:51 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 64000, "edgeProgressPermille": 843, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.8432147562582345, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R111 | 01:51 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 93.75, "before": 93.83, "loss": 0.0825, "playerId": 2751} |
| R112 | 01:52 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 65000, "edgeProgressPermille": 856, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.8563899868247694, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R112 | 01:52 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 93.67, "before": 93.75, "loss": 0.0825, "playerId": 2751} |
| R112 | 01:52 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 23000, "edgeProgressPermille": 226, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.22668808704822543, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R112 | 01:52 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.13, "before": 92.24, "loss": 0.10500000000000001, "playerId": 2707} |
| R113 | 01:53 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 66000, "edgeProgressPermille": 869, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.8695652173913043, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R113 | 01:53 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 93.59, "before": 93.67, "loss": 0.0825, "playerId": 2751} |
| R113 | 01:53 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 24000, "edgeProgressPermille": 236, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.23654409083293088, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R113 | 01:53 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.02, "before": 92.13, "loss": 0.10500000000000001, "playerId": 2707} |
| R114 | 01:54 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 25000, "edgeProgressPermille": 246, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.24640009461763634, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R114 | 01:54 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.91, "before": 92.02, "loss": 0.10500000000000001, "playerId": 2707} |
| R114 | 01:54 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 67000, "edgeProgressPermille": 882, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.8827404479578392, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R114 | 01:54 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 93.51, "before": 93.59, "loss": 0.0825, "playerId": 2751} |
| R115 | 01:55 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 26000, "edgeProgressPermille": 256, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.2562560984023418, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R115 | 01:55 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.8, "before": 91.91, "loss": 0.10500000000000001, "playerId": 2707} |
| R115 | 01:55 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 68000, "edgeProgressPermille": 895, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.8959156785243741, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R115 | 01:55 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 93.43, "before": 93.51, "loss": 0.0825, "playerId": 2751} |
| R116 | 01:56 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 69000, "edgeProgressPermille": 909, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.9090909090909091, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R116 | 01:56 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 93.35, "before": 93.43, "loss": 0.0825, "playerId": 2751} |
| R116 | 01:56 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 27000, "edgeProgressPermille": 266, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.26611210218704723, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R116 | 01:56 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.7, "before": 91.8, "loss": 0.10500000000000001, "playerId": 2707} |
| R117 | 01:57 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 70000, "edgeProgressPermille": 922, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.922266139657444, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R117 | 01:57 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 93.27, "before": 93.35, "loss": 0.0825, "playerId": 2751} |
| R117 | 01:57 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 28000, "edgeProgressPermille": 275, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.2759681059717527, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R117 | 01:57 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.6, "before": 91.7, "loss": 0.10500000000000001, "playerId": 2707} |
| R118 | 01:58 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 29000, "edgeProgressPermille": 285, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.28582410975645817, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R118 | 01:58 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.49, "before": 91.6, "loss": 0.10500000000000001, "playerId": 2707} |
| R118 | 01:58 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 71000, "edgeProgressPermille": 935, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.9354413702239789, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R118 | 01:58 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 93.19, "before": 93.27, "loss": 0.0825, "playerId": 2751} |
| R119 | 01:59 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 30000, "edgeProgressPermille": 295, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.2956801135411636, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R119 | 01:59 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.38, "before": 91.49, "loss": 0.10500000000000001, "playerId": 2707} |
| R119 | 01:59 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 72000, "edgeProgressPermille": 948, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.9486166007905138, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R119 | 01:59 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 93.11, "before": 93.19, "loss": 0.0825, "playerId": 2751} |
| R120 | 02:00 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 73000, "edgeProgressPermille": 961, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.9617918313570487, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R120 | 02:00 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 93.03, "before": 93.11, "loss": 0.0825, "playerId": 2751} |
| R120 | 02:00 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 31000, "edgeProgressPermille": 305, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.30553611732586905, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R120 | 02:00 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.27, "before": 91.38, "loss": 0.10500000000000001, "playerId": 2707} |
| R120 | 02:00 | MED | 任务刷新 |  | T_010 刷新在 洛阳驿(S09)，路线 WATER，截止 R300 |
| R121 | 02:01 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 74000, "edgeProgressPermille": 974, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.9749670619235836, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R121 | 02:01 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 92.95, "before": 93.03, "loss": 0.0825, "playerId": 2751} |
| R121 | 02:01 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 32000, "edgeProgressPermille": 315, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.3153921211105745, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R121 | 02:01 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.16, "before": 91.27, "loss": 0.10500000000000001, "playerId": 2707} |
| R122 | 02:02 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 33000, "edgeProgressPermille": 325, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.32524812489527993, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R122 | 02:02 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.05, "before": 91.16, "loss": 0.10500000000000001, "playerId": 2707} |
| R122 | 02:02 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 75000, "edgeProgressPermille": 988, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 0.9881422924901185, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R122 | 02:02 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 92.87, "before": 92.95, "loss": 0.0825, "playerId": 2751} |
| R123 | 02:03 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 34000, "edgeProgressPermille": 335, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.3351041286799854, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R123 | 02:03 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.95, "before": 91.05, "loss": 0.10500000000000001, "playerId": 2707} |
| R123 | 02:03 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 75900, "edgeProgressPermille": 1000, "edgeTotalMs": 75900, "fromNodeId": "S02", "playerId": 2751, "progress": 1.0, "routeEdgeId": "E11", "toNodeId": "S04"} |
| R123 | 02:03 | HIGH | 进点 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 进入 江南码头(S04) |
| R123 | 02:03 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 92.79, "before": 92.87, "loss": 0.0825, "playerId": 2751} |
| R124 | 02:04 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "CLAIM_TASK", "remainingRound": 3, "targetNodeId": "S04"} |
| R124 | 02:04 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 92.72, "before": 92.79, "loss": 0.07500000000000001, "playerId": 2751} |
| R124 | 02:04 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 35000, "edgeProgressPermille": 344, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.34496013246469087, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R124 | 02:04 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.85, "before": 90.95, "loss": 0.10500000000000001, "playerId": 2707} |
| R125 | 02:05 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "CLAIM_TASK", "remainingRound": 2, "targetNodeId": "S04"} |
| R125 | 02:05 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 92.65, "before": 92.72, "loss": 0.07500000000000001, "playerId": 2751} |
| R125 | 02:05 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 36000, "edgeProgressPermille": 354, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.35481613624939634, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R125 | 02:05 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.74, "before": 90.85, "loss": 0.10500000000000001, "playerId": 2707} |
| R126 | 02:06 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 37000, "edgeProgressPermille": 364, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.36467214003410175, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R126 | 02:06 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.63, "before": 90.74, "loss": 0.10500000000000001, "playerId": 2707} |
| R126 | 02:06 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "CLAIM_TASK", "remainingRound": 1, "targetNodeId": "S04"} |
| R126 | 02:06 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 92.58, "before": 92.65, "loss": 0.07500000000000001, "playerId": 2751} |
| R127 | 02:07 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 38000, "edgeProgressPermille": 374, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.3745281438188072, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R127 | 02:07 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.52, "before": 90.63, "loss": 0.10500000000000001, "playerId": 2707} |
| R127 | 02:07 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "CLAIM_TASK", "remainingRound": 0, "targetNodeId": "S04"} |
| R127 | 02:07 | HIGH | 任务完成 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 完成 码头争船，+30 分，任务分 30 |
| R127 | 02:07 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 92.51, "before": 92.58, "loss": 0.07500000000000001, "playerId": 2751} |
| R128 | 02:08 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 1000, "edgeProgressPermille": 88, "edgeTotalMs": 11250, "fromNodeId": "S04", "playerId": 2751, "progress": 0.08888888888888889, "routeEdgeId": "E12", "toNodeId": "S05"} |
| R128 | 02:08 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 92.44, "before": 92.51, "loss": 0.0675, "playerId": 2751} |
| R128 | 02:08 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 39000, "edgeProgressPermille": 384, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.3843841476035127, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R128 | 02:08 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.41, "before": 90.52, "loss": 0.10500000000000001, "playerId": 2707} |
| R129 | 02:09 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 2000, "edgeProgressPermille": 177, "edgeTotalMs": 11250, "fromNodeId": "S04", "playerId": 2751, "progress": 0.17777777777777778, "routeEdgeId": "E12", "toNodeId": "S05"} |
| R129 | 02:09 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 92.37, "before": 92.44, "loss": 0.0675, "playerId": 2751} |
| R129 | 02:09 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 40000, "edgeProgressPermille": 394, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.3942401513882181, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R129 | 02:09 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.3, "before": 90.41, "loss": 0.10500000000000001, "playerId": 2707} |
| R130 | 02:10 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 41000, "edgeProgressPermille": 404, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.4040961551729236, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R130 | 02:10 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.2, "before": 90.3, "loss": 0.10500000000000001, "playerId": 2707} |
| R130 | 02:10 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 3000, "edgeProgressPermille": 266, "edgeTotalMs": 11250, "fromNodeId": "S04", "playerId": 2751, "progress": 0.26666666666666666, "routeEdgeId": "E12", "toNodeId": "S05"} |
| R130 | 02:10 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 92.3, "before": 92.37, "loss": 0.0675, "playerId": 2751} |
| R131 | 02:11 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 42000, "edgeProgressPermille": 413, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.41395215895762905, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R131 | 02:11 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.1, "before": 90.2, "loss": 0.10500000000000001, "playerId": 2707} |
| R131 | 02:11 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 4000, "edgeProgressPermille": 355, "edgeTotalMs": 11250, "fromNodeId": "S04", "playerId": 2751, "progress": 0.35555555555555557, "routeEdgeId": "E12", "toNodeId": "S05"} |
| R131 | 02:11 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 92.23, "before": 92.3, "loss": 0.0675, "playerId": 2751} |
| R132 | 02:12 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 5000, "edgeProgressPermille": 444, "edgeTotalMs": 11250, "fromNodeId": "S04", "playerId": 2751, "progress": 0.4444444444444444, "routeEdgeId": "E12", "toNodeId": "S05"} |
| R132 | 02:12 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 92.16, "before": 92.23, "loss": 0.0675, "playerId": 2751} |
| R132 | 02:12 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 43000, "edgeProgressPermille": 423, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.4238081627423345, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R132 | 02:12 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.99, "before": 90.1, "loss": 0.10500000000000001, "playerId": 2707} |
| R132 | 02:12 | HIGH | 果品折损 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 好果跌破阈值 90，坏果 1 |
| R133 | 02:13 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 6000, "edgeProgressPermille": 533, "edgeTotalMs": 11250, "fromNodeId": "S04", "playerId": 2751, "progress": 0.5333333333333333, "routeEdgeId": "E12", "toNodeId": "S05"} |
| R133 | 02:13 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 92.09, "before": 92.16, "loss": 0.0675, "playerId": 2751} |
| R133 | 02:13 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 44000, "edgeProgressPermille": 433, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.43366416652703993, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R133 | 02:13 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.88, "before": 89.99, "loss": 0.10500000000000001, "playerId": 2707} |
| R134 | 02:14 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 45000, "edgeProgressPermille": 443, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.4435201703117454, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R134 | 02:14 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.77, "before": 89.88, "loss": 0.10500000000000001, "playerId": 2707} |
| R134 | 02:14 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 7000, "edgeProgressPermille": 622, "edgeTotalMs": 11250, "fromNodeId": "S04", "playerId": 2751, "progress": 0.6222222222222222, "routeEdgeId": "E12", "toNodeId": "S05"} |
| R134 | 02:14 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 92.02, "before": 92.09, "loss": 0.0675, "playerId": 2751} |
| R135 | 02:15 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 46000, "edgeProgressPermille": 453, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.45337617409645087, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R135 | 02:15 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.66, "before": 89.77, "loss": 0.10500000000000001, "playerId": 2707} |
| R135 | 02:15 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 8000, "edgeProgressPermille": 711, "edgeTotalMs": 11250, "fromNodeId": "S04", "playerId": 2751, "progress": 0.7111111111111111, "routeEdgeId": "E12", "toNodeId": "S05"} |
| R135 | 02:15 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 91.95, "before": 92.02, "loss": 0.0675, "playerId": 2751} |
| R136 | 02:16 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 9000, "edgeProgressPermille": 800, "edgeTotalMs": 11250, "fromNodeId": "S04", "playerId": 2751, "progress": 0.8, "routeEdgeId": "E12", "toNodeId": "S05"} |
| R136 | 02:16 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 91.88, "before": 91.95, "loss": 0.0675, "playerId": 2751} |
| R136 | 02:16 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 47000, "edgeProgressPermille": 463, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.4632321778811563, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R136 | 02:16 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.55, "before": 89.66, "loss": 0.10500000000000001, "playerId": 2707} |
| R137 | 02:17 | MED | SCOUT_MARKER_EXPIRE | RED codex-py/0.1(2751) | {"playerId": 2751, "targetNodeId": "S05"} |
| R137 | 02:17 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 10000, "edgeProgressPermille": 888, "edgeTotalMs": 11250, "fromNodeId": "S04", "playerId": 2751, "progress": 0.8888888888888888, "routeEdgeId": "E12", "toNodeId": "S05"} |
| R137 | 02:17 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 91.81, "before": 91.88, "loss": 0.0675, "playerId": 2751} |
| R137 | 02:17 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 48000, "edgeProgressPermille": 473, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.47308818166586175, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R137 | 02:17 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.45, "before": 89.55, "loss": 0.10500000000000001, "playerId": 2707} |
| R138 | 02:18 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 49000, "edgeProgressPermille": 482, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.4829441854505672, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R138 | 02:18 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.35, "before": 89.45, "loss": 0.10500000000000001, "playerId": 2707} |
| R138 | 02:18 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 11000, "edgeProgressPermille": 977, "edgeTotalMs": 11250, "fromNodeId": "S04", "playerId": 2751, "progress": 0.9777777777777777, "routeEdgeId": "E12", "toNodeId": "S05"} |
| R138 | 02:18 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 91.74, "before": 91.81, "loss": 0.0675, "playerId": 2751} |
| R139 | 02:19 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 50000, "edgeProgressPermille": 492, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.4928001892352727, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R139 | 02:19 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.24, "before": 89.35, "loss": 0.10500000000000001, "playerId": 2707} |
| R139 | 02:19 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 11250, "edgeProgressPermille": 1000, "edgeTotalMs": 11250, "fromNodeId": "S04", "playerId": 2751, "progress": 1.0, "routeEdgeId": "E12", "toNodeId": "S05"} |
| R139 | 02:19 | HIGH | 进点 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 进入 洞庭水驿(S05) |
| R139 | 02:19 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 91.67, "before": 91.74, "loss": 0.0675, "playerId": 2751} |
| R140 | 02:20 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "WATER_TRANSFER", "remainingRound": 5, "targetNodeId": "S05"} |
| R140 | 02:20 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 91.6, "before": 91.67, "loss": 0.07500000000000001, "playerId": 2751} |
| R140 | 02:20 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 51000, "edgeProgressPermille": 502, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5026561930199781, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R140 | 02:20 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.13, "before": 89.24, "loss": 0.10500000000000001, "playerId": 2707} |
| R141 | 02:21 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "WATER_TRANSFER", "remainingRound": 4, "targetNodeId": "S05"} |
| R141 | 02:21 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 91.52, "before": 91.6, "loss": 0.07500000000000001, "playerId": 2751} |
| R141 | 02:21 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 52000, "edgeProgressPermille": 512, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5125121968046836, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R141 | 02:21 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.02, "before": 89.13, "loss": 0.10500000000000001, "playerId": 2707} |
| R142 | 02:22 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 53000, "edgeProgressPermille": 522, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.522368200589389, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R142 | 02:22 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.91, "before": 89.02, "loss": 0.10500000000000001, "playerId": 2707} |
| R142 | 02:22 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "WATER_TRANSFER", "remainingRound": 3, "targetNodeId": "S05"} |
| R142 | 02:22 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 91.45, "before": 91.52, "loss": 0.07500000000000001, "playerId": 2751} |
| R143 | 02:23 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 54000, "edgeProgressPermille": 532, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5322242043740945, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R143 | 02:23 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.8, "before": 88.91, "loss": 0.10500000000000001, "playerId": 2707} |
| R143 | 02:23 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "WATER_TRANSFER", "remainingRound": 2, "targetNodeId": "S05"} |
| R143 | 02:23 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 91.38, "before": 91.45, "loss": 0.07500000000000001, "playerId": 2751} |
| R144 | 02:24 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "WATER_TRANSFER", "remainingRound": 1, "targetNodeId": "S05"} |
| R144 | 02:24 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 91.3, "before": 91.38, "loss": 0.07500000000000001, "playerId": 2751} |
| R144 | 02:24 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 55000, "edgeProgressPermille": 542, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5420802081588, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R144 | 02:24 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.7, "before": 88.8, "loss": 0.10500000000000001, "playerId": 2707} |
| R145 | 02:25 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "WATER_TRANSFER", "remainingRound": 0, "targetNodeId": "S05"} |
| R145 | 02:25 | MED | 处理完成 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 在 洞庭水驿(S05) 完成水路转运 |
| R145 | 02:25 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 91.23, "before": 91.3, "loss": 0.07500000000000001, "playerId": 2751} |
| R145 | 02:25 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 56000, "edgeProgressPermille": 551, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5519362119435054, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R145 | 02:25 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.6, "before": 88.7, "loss": 0.10500000000000001, "playerId": 2707} |
| R146 | 02:26 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 57000, "edgeProgressPermille": 561, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5617922157282108, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R146 | 02:26 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.49, "before": 88.6, "loss": 0.10500000000000001, "playerId": 2707} |
| R146 | 02:26 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 1000, "edgeProgressPermille": 12, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.012903225806451613, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R146 | 02:26 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 91.16, "before": 91.23, "loss": 0.0675, "playerId": 2751} |
| R147 | 02:27 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 58000, "edgeProgressPermille": 571, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5716482195129163, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R147 | 02:27 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.38, "before": 88.49, "loss": 0.10500000000000001, "playerId": 2707} |
| R147 | 02:27 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 2000, "edgeProgressPermille": 25, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.025806451612903226, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R147 | 02:27 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 91.09, "before": 91.16, "loss": 0.0675, "playerId": 2751} |
| R148 | 02:28 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 3000, "edgeProgressPermille": 38, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.03870967741935484, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R148 | 02:28 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 91.02, "before": 91.09, "loss": 0.0675, "playerId": 2751} |
| R148 | 02:28 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 59000, "edgeProgressPermille": 581, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5815042232976217, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R148 | 02:28 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.27, "before": 88.38, "loss": 0.10500000000000001, "playerId": 2707} |
| R149 | 02:29 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 4000, "edgeProgressPermille": 51, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.05161290322580645, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R149 | 02:29 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 90.95, "before": 91.02, "loss": 0.0675, "playerId": 2751} |
| R149 | 02:29 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 60000, "edgeProgressPermille": 591, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5913602270823272, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R149 | 02:29 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.16, "before": 88.27, "loss": 0.10500000000000001, "playerId": 2707} |
| R150 | 02:30 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 61000, "edgeProgressPermille": 601, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6012162308670327, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R150 | 02:30 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.05, "before": 88.16, "loss": 0.10500000000000001, "playerId": 2707} |
| R150 | 02:30 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 5000, "edgeProgressPermille": 64, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.06451612903225806, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R150 | 02:30 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 90.88, "before": 90.95, "loss": 0.0675, "playerId": 2751} |
| R150 | 02:30 | MED | 任务刷新 |  | T_011 刷新在 荆襄大驿(S07)，路线 ROAD，截止 R330 |
| R151 | 02:31 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 62000, "edgeProgressPermille": 611, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6110722346517381, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R151 | 02:31 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.95, "before": 88.05, "loss": 0.10500000000000001, "playerId": 2707} |
| R151 | 02:31 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 6000, "edgeProgressPermille": 77, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.07741935483870968, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R151 | 02:31 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 90.81, "before": 90.88, "loss": 0.0675, "playerId": 2751} |
| R152 | 02:32 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 7000, "edgeProgressPermille": 90, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.09032258064516129, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R152 | 02:32 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 90.74, "before": 90.81, "loss": 0.0675, "playerId": 2751} |
| R152 | 02:32 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 63000, "edgeProgressPermille": 620, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6209282384364435, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R152 | 02:32 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.85, "before": 87.95, "loss": 0.10500000000000001, "playerId": 2707} |
| R153 | 02:33 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 8000, "edgeProgressPermille": 103, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.1032258064516129, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R153 | 02:33 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 90.67, "before": 90.74, "loss": 0.0675, "playerId": 2751} |
| R153 | 02:33 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 64000, "edgeProgressPermille": 630, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.630784242221149, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R153 | 02:33 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.74, "before": 87.85, "loss": 0.10500000000000001, "playerId": 2707} |
| R154 | 02:34 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 65000, "edgeProgressPermille": 640, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6406402460058545, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R154 | 02:34 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.63, "before": 87.74, "loss": 0.10500000000000001, "playerId": 2707} |
| R154 | 02:34 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 9000, "edgeProgressPermille": 116, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.11612903225806452, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R154 | 02:34 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 90.6, "before": 90.67, "loss": 0.0675, "playerId": 2751} |
| R155 | 02:35 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 66000, "edgeProgressPermille": 650, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6504962497905599, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R155 | 02:35 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.52, "before": 87.63, "loss": 0.10500000000000001, "playerId": 2707} |
| R155 | 02:35 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 10000, "edgeProgressPermille": 129, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.12903225806451613, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R155 | 02:35 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 90.53, "before": 90.6, "loss": 0.0675, "playerId": 2751} |
| R156 | 02:36 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 11000, "edgeProgressPermille": 141, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.14193548387096774, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R156 | 02:36 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 90.46, "before": 90.53, "loss": 0.0675, "playerId": 2751} |
| R156 | 02:36 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 67000, "edgeProgressPermille": 660, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6603522535752654, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R156 | 02:36 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.41, "before": 87.52, "loss": 0.10500000000000001, "playerId": 2707} |
| R157 | 02:37 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 12000, "edgeProgressPermille": 154, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.15483870967741936, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R157 | 02:37 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 90.39, "before": 90.46, "loss": 0.0675, "playerId": 2751} |
| R157 | 02:37 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 68000, "edgeProgressPermille": 670, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6702082573599708, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R157 | 02:37 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.3, "before": 87.41, "loss": 0.10500000000000001, "playerId": 2707} |
| R158 | 02:38 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 69000, "edgeProgressPermille": 680, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6800642611446763, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R158 | 02:38 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.2, "before": 87.3, "loss": 0.10500000000000001, "playerId": 2707} |
| R158 | 02:38 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 13000, "edgeProgressPermille": 167, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.16774193548387098, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R158 | 02:38 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 90.32, "before": 90.39, "loss": 0.0675, "playerId": 2751} |
| R159 | 02:39 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 70000, "edgeProgressPermille": 689, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6899202649293817, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R159 | 02:39 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.1, "before": 87.2, "loss": 0.10500000000000001, "playerId": 2707} |
| R159 | 02:39 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 14000, "edgeProgressPermille": 180, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.18064516129032257, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R159 | 02:39 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 90.25, "before": 90.32, "loss": 0.0675, "playerId": 2751} |
| R160 | 02:40 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 15000, "edgeProgressPermille": 193, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.1935483870967742, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R160 | 02:40 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 90.18, "before": 90.25, "loss": 0.0675, "playerId": 2751} |
| R160 | 02:40 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 71000, "edgeProgressPermille": 699, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6997762687140872, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R160 | 02:40 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.99, "before": 87.1, "loss": 0.10500000000000001, "playerId": 2707} |
| R161 | 02:41 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 16000, "edgeProgressPermille": 206, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.2064516129032258, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R161 | 02:41 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 90.11, "before": 90.18, "loss": 0.0675, "playerId": 2751} |
| R161 | 02:41 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 72000, "edgeProgressPermille": 709, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7096322724987927, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R161 | 02:41 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.88, "before": 86.99, "loss": 0.10500000000000001, "playerId": 2707} |
| R162 | 02:42 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 73000, "edgeProgressPermille": 719, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7194882762834981, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R162 | 02:42 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.77, "before": 86.88, "loss": 0.10500000000000001, "playerId": 2707} |
| R162 | 02:42 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 17000, "edgeProgressPermille": 219, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.21935483870967742, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R162 | 02:42 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 90.04, "before": 90.11, "loss": 0.0675, "playerId": 2751} |
| R163 | 02:43 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 74000, "edgeProgressPermille": 729, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7293442800682035, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R163 | 02:43 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.66, "before": 86.77, "loss": 0.10500000000000001, "playerId": 2707} |
| R163 | 02:43 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 18000, "edgeProgressPermille": 232, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.23225806451612904, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R163 | 02:43 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.97, "before": 90.04, "loss": 0.0675, "playerId": 2751} |
| R163 | 02:43 | HIGH | 果品折损 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 好果跌破阈值 90，坏果 1 |
| R164 | 02:44 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 19000, "edgeProgressPermille": 245, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.24516129032258063, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R164 | 02:44 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.9, "before": 89.97, "loss": 0.0675, "playerId": 2751} |
| R164 | 02:44 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 75000, "edgeProgressPermille": 739, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.739200283852909, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R164 | 02:44 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.55, "before": 86.66, "loss": 0.10500000000000001, "playerId": 2707} |
| R165 | 02:45 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 20000, "edgeProgressPermille": 258, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.25806451612903225, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R165 | 02:45 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.83, "before": 89.9, "loss": 0.0675, "playerId": 2751} |
| R165 | 02:45 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 76000, "edgeProgressPermille": 749, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7490562876376144, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R165 | 02:45 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.45, "before": 86.55, "loss": 0.10500000000000001, "playerId": 2707} |
| R166 | 02:46 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 77000, "edgeProgressPermille": 758, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7589122914223199, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R166 | 02:46 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.35, "before": 86.45, "loss": 0.10500000000000001, "playerId": 2707} |
| R166 | 02:46 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 21000, "edgeProgressPermille": 270, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.2709677419354839, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R166 | 02:46 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.76, "before": 89.83, "loss": 0.0675, "playerId": 2751} |
| R167 | 02:47 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 78000, "edgeProgressPermille": 768, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7687682952070254, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R167 | 02:47 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.24, "before": 86.35, "loss": 0.10500000000000001, "playerId": 2707} |
| R167 | 02:47 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 22000, "edgeProgressPermille": 283, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.2838709677419355, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R167 | 02:47 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.69, "before": 89.76, "loss": 0.0675, "playerId": 2751} |
| R168 | 02:48 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 23000, "edgeProgressPermille": 296, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.2967741935483871, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R168 | 02:48 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.65, "before": 89.69, "loss": 0.045, "playerId": 2751} |
| R168 | 02:48 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 79000, "edgeProgressPermille": 778, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7786242989917308, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R168 | 02:48 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.17, "before": 86.24, "loss": 0.07, "playerId": 2707} |
| R169 | 02:49 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 24000, "edgeProgressPermille": 309, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.3096774193548387, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R169 | 02:49 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.61, "before": 89.65, "loss": 0.045, "playerId": 2751} |
| R169 | 02:49 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 80000, "edgeProgressPermille": 788, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7884803027764362, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R169 | 02:49 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.1, "before": 86.17, "loss": 0.07, "playerId": 2707} |
| R170 | 02:50 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 81000, "edgeProgressPermille": 798, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7983363065611417, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R170 | 02:50 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.03, "before": 86.1, "loss": 0.07, "playerId": 2707} |
| R170 | 02:50 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 25000, "edgeProgressPermille": 322, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.3225806451612903, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R170 | 02:50 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.57, "before": 89.61, "loss": 0.045, "playerId": 2751} |
| R171 | 02:51 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 82000, "edgeProgressPermille": 808, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.8081923103458472, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R171 | 02:51 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.96, "before": 86.03, "loss": 0.07, "playerId": 2707} |
| R171 | 02:51 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 26000, "edgeProgressPermille": 335, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.33548387096774196, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R171 | 02:51 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.52, "before": 89.57, "loss": 0.045, "playerId": 2751} |
| R172 | 02:52 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 27000, "edgeProgressPermille": 348, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.34838709677419355, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R172 | 02:52 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.48, "before": 89.52, "loss": 0.045, "playerId": 2751} |
| R172 | 02:52 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 83000, "edgeProgressPermille": 818, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.8180483141305527, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R172 | 02:52 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.89, "before": 85.96, "loss": 0.07, "playerId": 2707} |
| R173 | 02:53 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 28000, "edgeProgressPermille": 361, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.36129032258064514, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R173 | 02:53 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.44, "before": 89.48, "loss": 0.045, "playerId": 2751} |
| R173 | 02:53 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 84000, "edgeProgressPermille": 827, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.8279043179152581, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R173 | 02:53 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.82, "before": 85.89, "loss": 0.07, "playerId": 2707} |
| R174 | 02:54 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 85000, "edgeProgressPermille": 837, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.8377603216999635, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R174 | 02:54 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.75, "before": 85.82, "loss": 0.07, "playerId": 2707} |
| R174 | 02:54 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 29000, "edgeProgressPermille": 374, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.3741935483870968, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R174 | 02:54 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.4, "before": 89.44, "loss": 0.045, "playerId": 2751} |
| R175 | 02:55 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 86000, "edgeProgressPermille": 847, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.847616325484669, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R175 | 02:55 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.68, "before": 85.75, "loss": 0.07, "playerId": 2707} |
| R175 | 02:55 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 30000, "edgeProgressPermille": 387, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.3870967741935484, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R175 | 02:55 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.36, "before": 89.4, "loss": 0.045, "playerId": 2751} |
| R176 | 02:56 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 31000, "edgeProgressPermille": 400, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.4, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R176 | 02:56 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.32, "before": 89.36, "loss": 0.045, "playerId": 2751} |
| R176 | 02:56 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 87000, "edgeProgressPermille": 857, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.8574723292693744, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R176 | 02:56 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.61, "before": 85.68, "loss": 0.07, "playerId": 2707} |
| R177 | 02:57 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 32000, "edgeProgressPermille": 412, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.4129032258064516, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R177 | 02:57 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.27, "before": 89.32, "loss": 0.045, "playerId": 2751} |
| R177 | 02:57 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 88000, "edgeProgressPermille": 867, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.8673283330540799, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R177 | 02:57 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.54, "before": 85.61, "loss": 0.07, "playerId": 2707} |
| R178 | 02:58 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 89000, "edgeProgressPermille": 877, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.8771843368387854, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R178 | 02:58 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.47, "before": 85.54, "loss": 0.07, "playerId": 2707} |
| R178 | 02:58 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 33000, "edgeProgressPermille": 425, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.4258064516129032, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R178 | 02:58 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.23, "before": 89.27, "loss": 0.045, "playerId": 2751} |
| R179 | 02:59 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 90000, "edgeProgressPermille": 887, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.8870403406234908, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R179 | 02:59 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.4, "before": 85.47, "loss": 0.07, "playerId": 2707} |
| R179 | 02:59 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 34000, "edgeProgressPermille": 438, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.43870967741935485, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R179 | 02:59 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.19, "before": 89.23, "loss": 0.045, "playerId": 2751} |
| R180 | 03:00 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 35000, "edgeProgressPermille": 451, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.45161290322580644, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R180 | 03:00 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.15, "before": 89.19, "loss": 0.045, "playerId": 2751} |
| R180 | 03:00 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 91000, "edgeProgressPermille": 896, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.8968963444081962, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R180 | 03:00 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.33, "before": 85.4, "loss": 0.07, "playerId": 2707} |
| R181 | 03:01 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 36000, "edgeProgressPermille": 464, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.4645161290322581, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R181 | 03:01 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.11, "before": 89.15, "loss": 0.045, "playerId": 2751} |
| R181 | 03:01 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 92000, "edgeProgressPermille": 906, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9067523481929017, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R181 | 03:01 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.26, "before": 85.33, "loss": 0.07, "playerId": 2707} |
| R182 | 03:02 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 93000, "edgeProgressPermille": 916, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9166083519776071, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R182 | 03:02 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.19, "before": 85.26, "loss": 0.07, "playerId": 2707} |
| R182 | 03:02 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 37000, "edgeProgressPermille": 477, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.4774193548387097, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R182 | 03:02 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.07, "before": 89.11, "loss": 0.045, "playerId": 2751} |
| R183 | 03:03 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 94000, "edgeProgressPermille": 926, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9264643557623126, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R183 | 03:03 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.12, "before": 85.19, "loss": 0.07, "playerId": 2707} |
| R183 | 03:03 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 38000, "edgeProgressPermille": 490, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.49032258064516127, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R183 | 03:03 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 89.02, "before": 89.07, "loss": 0.045, "playerId": 2751} |
| R184 | 03:04 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 39000, "edgeProgressPermille": 503, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.5032258064516129, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R184 | 03:04 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.98, "before": 89.02, "loss": 0.045, "playerId": 2751} |
| R184 | 03:04 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 95000, "edgeProgressPermille": 936, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9363203595470181, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R184 | 03:04 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.05, "before": 85.12, "loss": 0.07, "playerId": 2707} |
| R185 | 03:05 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 40000, "edgeProgressPermille": 516, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.5161290322580645, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R185 | 03:05 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.94, "before": 88.98, "loss": 0.045, "playerId": 2751} |
| R185 | 03:05 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 96000, "edgeProgressPermille": 946, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9461763633317235, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R185 | 03:05 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.98, "before": 85.05, "loss": 0.07, "playerId": 2707} |
| R186 | 03:06 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 97000, "edgeProgressPermille": 956, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.956032367116429, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R186 | 03:06 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.91, "before": 84.98, "loss": 0.07, "playerId": 2707} |
| R186 | 03:06 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 41000, "edgeProgressPermille": 529, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.5290322580645161, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R186 | 03:06 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.9, "before": 88.94, "loss": 0.045, "playerId": 2751} |
| R187 | 03:07 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 98000, "edgeProgressPermille": 965, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9658883709011344, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R187 | 03:07 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.84, "before": 84.91, "loss": 0.07, "playerId": 2707} |
| R187 | 03:07 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 42000, "edgeProgressPermille": 541, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.5419354838709678, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R187 | 03:07 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.86, "before": 88.9, "loss": 0.045, "playerId": 2751} |
| R188 | 03:08 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 43000, "edgeProgressPermille": 554, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.5548387096774193, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R188 | 03:08 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.82, "before": 88.86, "loss": 0.045, "playerId": 2751} |
| R188 | 03:08 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 99000, "edgeProgressPermille": 975, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9757443746858399, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R188 | 03:08 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.77, "before": 84.84, "loss": 0.07, "playerId": 2707} |
| R189 | 03:09 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 44000, "edgeProgressPermille": 567, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.567741935483871, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R189 | 03:09 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.77, "before": 88.82, "loss": 0.045, "playerId": 2751} |
| R189 | 03:09 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 100000, "edgeProgressPermille": 985, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9856003784705454, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R189 | 03:09 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.7, "before": 84.77, "loss": 0.07, "playerId": 2707} |
| R190 | 03:10 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 101000, "edgeProgressPermille": 995, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9954563822552508, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R190 | 03:10 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.63, "before": 84.7, "loss": 0.07, "playerId": 2707} |
| R190 | 03:10 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 45000, "edgeProgressPermille": 580, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.5806451612903226, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R190 | 03:10 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.73, "before": 88.77, "loss": 0.045, "playerId": 2751} |
| R191 | 03:11 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 101461, "edgeProgressPermille": 1000, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2707, "progress": 1.0, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R191 | 03:11 | HIGH | 进点 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 进入 秦岭栈道(S08) |
| R191 | 03:11 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.56, "before": 84.63, "loss": 0.07, "playerId": 2707} |
| R191 | 03:11 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 46000, "edgeProgressPermille": 593, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.5935483870967742, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R191 | 03:11 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.69, "before": 88.73, "loss": 0.045, "playerId": 2751} |
| R192 | 03:12 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 47000, "edgeProgressPermille": 606, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.6064516129032258, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R192 | 03:12 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.65, "before": 88.69, "loss": 0.045, "playerId": 2751} |
| R192 | 03:12 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 3, "targetNodeId": "S08"} |
| R192 | 03:12 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.51, "before": 84.56, "loss": 0.05, "playerId": 2707} |
| R193 | 03:13 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 48000, "edgeProgressPermille": 619, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.6193548387096774, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R193 | 03:13 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.61, "before": 88.65, "loss": 0.045, "playerId": 2751} |
| R193 | 03:13 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 2, "targetNodeId": "S08"} |
| R193 | 03:13 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.46, "before": 84.51, "loss": 0.05, "playerId": 2707} |
| R194 | 03:14 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 1, "targetNodeId": "S08"} |
| R194 | 03:14 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.41, "before": 84.46, "loss": 0.05, "playerId": 2707} |
| R194 | 03:14 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 49000, "edgeProgressPermille": 632, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.632258064516129, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R194 | 03:14 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.57, "before": 88.61, "loss": 0.045, "playerId": 2751} |
| R195 | 03:15 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 0, "targetNodeId": "S08"} |
| R195 | 03:15 | HIGH | 任务完成 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 完成 栈道复核，+30 分，任务分 30 |
| R195 | 03:15 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.36, "before": 84.41, "loss": 0.05, "playerId": 2707} |
| R195 | 03:15 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 50000, "edgeProgressPermille": 645, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.6451612903225806, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R195 | 03:15 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.52, "before": 88.57, "loss": 0.045, "playerId": 2751} |
| R196 | 03:16 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 51000, "edgeProgressPermille": 658, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.6580645161290323, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R196 | 03:16 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.48, "before": 88.52, "loss": 0.045, "playerId": 2751} |
| R196 | 03:16 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 3, "targetNodeId": "S08"} |
| R196 | 03:16 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.31, "before": 84.36, "loss": 0.05, "playerId": 2707} |
| R197 | 03:17 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 52000, "edgeProgressPermille": 670, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.6709677419354839, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R197 | 03:17 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.44, "before": 88.48, "loss": 0.045, "playerId": 2751} |
| R197 | 03:17 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 2, "targetNodeId": "S08"} |
| R197 | 03:17 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.26, "before": 84.31, "loss": 0.05, "playerId": 2707} |
| R198 | 03:18 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 1, "targetNodeId": "S08"} |
| R198 | 03:18 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.21, "before": 84.26, "loss": 0.05, "playerId": 2707} |
| R198 | 03:18 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 53000, "edgeProgressPermille": 683, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.6838709677419355, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R198 | 03:18 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.4, "before": 88.44, "loss": 0.045, "playerId": 2751} |
| R199 | 03:19 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 0, "targetNodeId": "S08"} |
| R199 | 03:19 | HIGH | 任务完成 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 完成 栈道复核，+30 分，任务分 60 |
| R199 | 03:19 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.16, "before": 84.21, "loss": 0.05, "playerId": 2707} |
| R199 | 03:19 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 54000, "edgeProgressPermille": 696, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.6967741935483871, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R199 | 03:19 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.36, "before": 88.4, "loss": 0.045, "playerId": 2751} |
| R200 | 03:20 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 55000, "edgeProgressPermille": 709, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.7096774193548387, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R200 | 03:20 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.32, "before": 88.36, "loss": 0.045, "playerId": 2751} |
| R200 | 03:20 | HIGH | 资源使用 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 使用冰鉴，状态 84.16->94.16 |
| R200 | 03:20 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.11, "before": 94.16, "loss": 0.05, "playerId": 2707} |
| R200 | 03:20 | MED | 任务刷新 |  | T_012 刷新在 荆襄大驿(S07)，路线 ROAD，截止 R420 |
| R200 | 03:20 | MED | 任务刷新 |  | T_013 刷新在 武关(S10)，路线 WATER，截止 R420 |
| R201 | 03:21 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 56000, "edgeProgressPermille": 722, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.7225806451612903, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R201 | 03:21 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.27, "before": 88.32, "loss": 0.045, "playerId": 2751} |
| R201 | 03:21 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 7, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.007168458781362007, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R201 | 03:21 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 94.05, "before": 94.11, "loss": 0.065, "playerId": 2707} |
| R202 | 03:22 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 14, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.014336917562724014, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R202 | 03:22 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.99, "before": 94.05, "loss": 0.065, "playerId": 2707} |
| R202 | 03:22 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 57000, "edgeProgressPermille": 735, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.7354838709677419, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R202 | 03:22 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.23, "before": 88.27, "loss": 0.045, "playerId": 2751} |
| R203 | 03:23 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 21, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.021505376344086023, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R203 | 03:23 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.93, "before": 93.99, "loss": 0.065, "playerId": 2707} |
| R203 | 03:23 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 58000, "edgeProgressPermille": 748, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.7483870967741936, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R203 | 03:23 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.19, "before": 88.23, "loss": 0.045, "playerId": 2751} |
| R204 | 03:24 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 59000, "edgeProgressPermille": 761, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.7612903225806451, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R204 | 03:24 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.15, "before": 88.19, "loss": 0.045, "playerId": 2751} |
| R204 | 03:24 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 28, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.02867383512544803, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R204 | 03:24 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.87, "before": 93.93, "loss": 0.065, "playerId": 2707} |
| R205 | 03:25 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 60000, "edgeProgressPermille": 774, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.7741935483870968, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R205 | 03:25 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.11, "before": 88.15, "loss": 0.045, "playerId": 2751} |
| R205 | 03:25 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 35, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.035842293906810034, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R205 | 03:25 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.81, "before": 93.87, "loss": 0.065, "playerId": 2707} |
| R206 | 03:26 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 43, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.043010752688172046, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R206 | 03:26 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.75, "before": 93.81, "loss": 0.065, "playerId": 2707} |
| R206 | 03:26 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 61000, "edgeProgressPermille": 787, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.7870967741935484, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R206 | 03:26 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.07, "before": 88.11, "loss": 0.045, "playerId": 2751} |
| R207 | 03:27 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 50, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.05017921146953405, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R207 | 03:27 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.69, "before": 93.75, "loss": 0.065, "playerId": 2707} |
| R207 | 03:27 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 62000, "edgeProgressPermille": 800, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.8, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R207 | 03:27 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 88.02, "before": 88.07, "loss": 0.045, "playerId": 2751} |
| R208 | 03:28 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 63000, "edgeProgressPermille": 812, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.8129032258064516, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R208 | 03:28 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.98, "before": 88.02, "loss": 0.045, "playerId": 2751} |
| R208 | 03:28 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 57, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.05734767025089606, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R208 | 03:28 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.63, "before": 93.69, "loss": 0.065, "playerId": 2707} |
| R209 | 03:29 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 64000, "edgeProgressPermille": 825, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.8258064516129032, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R209 | 03:29 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.94, "before": 87.98, "loss": 0.045, "playerId": 2751} |
| R209 | 03:29 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 64, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.06451612903225806, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R209 | 03:29 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.57, "before": 93.63, "loss": 0.065, "playerId": 2707} |
| R210 | 03:30 | MED | 任务过期 |  | T_004 在 梅关驿(S03) 过期 |
| R210 | 03:30 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 71, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.07168458781362007, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R210 | 03:30 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.51, "before": 93.57, "loss": 0.065, "playerId": 2707} |
| R210 | 03:30 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 65000, "edgeProgressPermille": 838, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.8387096774193549, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R210 | 03:30 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.9, "before": 87.94, "loss": 0.045, "playerId": 2751} |
| R210 | 03:30 | MED | 任务刷新 |  | T_014 刷新在 灞桥驿(S13)，路线 MOUNTAIN，截止 R390 |
| R211 | 03:31 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 78, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.07885304659498207, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R211 | 03:31 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.45, "before": 93.51, "loss": 0.065, "playerId": 2707} |
| R211 | 03:31 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 66000, "edgeProgressPermille": 851, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.8516129032258064, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R211 | 03:31 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.86, "before": 87.9, "loss": 0.045, "playerId": 2751} |
| R212 | 03:32 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 67000, "edgeProgressPermille": 864, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.864516129032258, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R212 | 03:32 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.82, "before": 87.86, "loss": 0.045, "playerId": 2751} |
| R212 | 03:32 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 12000, "edgeProgressPermille": 86, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.08602150537634409, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R212 | 03:32 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.39, "before": 93.45, "loss": 0.065, "playerId": 2707} |
| R213 | 03:33 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 68000, "edgeProgressPermille": 877, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.8774193548387097, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R213 | 03:33 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.77, "before": 87.82, "loss": 0.045, "playerId": 2751} |
| R213 | 03:33 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 13000, "edgeProgressPermille": 93, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.0931899641577061, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R213 | 03:33 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.33, "before": 93.39, "loss": 0.065, "playerId": 2707} |
| R214 | 03:34 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 100, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.1003584229390681, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R214 | 03:34 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.27, "before": 93.33, "loss": 0.065, "playerId": 2707} |
| R214 | 03:34 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 69000, "edgeProgressPermille": 890, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.8903225806451613, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R214 | 03:34 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.73, "before": 87.77, "loss": 0.045, "playerId": 2751} |
| R215 | 03:35 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 15000, "edgeProgressPermille": 107, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.10752688172043011, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R215 | 03:35 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.21, "before": 93.27, "loss": 0.065, "playerId": 2707} |
| R215 | 03:35 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 70000, "edgeProgressPermille": 903, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.9032258064516129, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R215 | 03:35 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.69, "before": 87.73, "loss": 0.045, "playerId": 2751} |
| R216 | 03:36 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 71000, "edgeProgressPermille": 916, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.9161290322580645, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R216 | 03:36 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.65, "before": 87.69, "loss": 0.045, "playerId": 2751} |
| R216 | 03:36 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 16000, "edgeProgressPermille": 114, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.11469534050179211, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R216 | 03:36 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.15, "before": 93.21, "loss": 0.065, "playerId": 2707} |
| R217 | 03:37 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 72000, "edgeProgressPermille": 929, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.9290322580645162, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R217 | 03:37 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.61, "before": 87.65, "loss": 0.045, "playerId": 2751} |
| R217 | 03:37 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 17000, "edgeProgressPermille": 121, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.12186379928315412, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R217 | 03:37 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.09, "before": 93.15, "loss": 0.065, "playerId": 2707} |
| R218 | 03:38 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 18000, "edgeProgressPermille": 129, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.12903225806451613, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R218 | 03:38 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 93.03, "before": 93.09, "loss": 0.065, "playerId": 2707} |
| R218 | 03:38 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 73000, "edgeProgressPermille": 941, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.9419354838709677, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R218 | 03:38 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.57, "before": 87.61, "loss": 0.045, "playerId": 2751} |
| R219 | 03:39 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 19000, "edgeProgressPermille": 136, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.13620071684587814, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R219 | 03:39 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.97, "before": 93.03, "loss": 0.065, "playerId": 2707} |
| R219 | 03:39 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 74000, "edgeProgressPermille": 954, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.9548387096774194, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R219 | 03:39 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.52, "before": 87.57, "loss": 0.045, "playerId": 2751} |
| R220 | 03:40 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 75000, "edgeProgressPermille": 967, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.967741935483871, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R220 | 03:40 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.48, "before": 87.52, "loss": 0.045, "playerId": 2751} |
| R220 | 03:40 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 20000, "edgeProgressPermille": 143, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.14336917562724014, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R220 | 03:40 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.91, "before": 92.97, "loss": 0.065, "playerId": 2707} |
| R221 | 03:41 | MED | 任务过期 |  | T_001 在 梅关驿(S03) 过期 |
| R221 | 03:41 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 76000, "edgeProgressPermille": 980, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.9806451612903225, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R221 | 03:41 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.44, "before": 87.48, "loss": 0.045, "playerId": 2751} |
| R221 | 03:41 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 21000, "edgeProgressPermille": 150, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.15053763440860216, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R221 | 03:41 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.85, "before": 92.91, "loss": 0.065, "playerId": 2707} |
| R222 | 03:42 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 22000, "edgeProgressPermille": 157, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.15770609318996415, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R222 | 03:42 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.79, "before": 92.85, "loss": 0.065, "playerId": 2707} |
| R222 | 03:42 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 77000, "edgeProgressPermille": 993, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 0.9935483870967742, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R222 | 03:42 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.4, "before": 87.44, "loss": 0.045, "playerId": 2751} |
| R223 | 03:43 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 23000, "edgeProgressPermille": 164, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.16487455197132617, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R223 | 03:43 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.73, "before": 92.79, "loss": 0.065, "playerId": 2707} |
| R223 | 03:43 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 77500, "edgeProgressPermille": 1000, "edgeTotalMs": 77500, "fromNodeId": "S05", "playerId": 2751, "progress": 1.0, "routeEdgeId": "E19", "toNodeId": "S09"} |
| R223 | 03:43 | HIGH | 进点 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 进入 洛阳驿(S09) |
| R223 | 03:43 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.36, "before": 87.4, "loss": 0.045, "playerId": 2751} |
| R224 | 03:44 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "CLAIM_RESOURCE", "remainingRound": 1, "targetNodeId": "S09"} |
| R224 | 03:44 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.31, "before": 87.36, "loss": 0.05, "playerId": 2751} |
| R224 | 03:44 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 24000, "edgeProgressPermille": 172, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.17204301075268819, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R224 | 03:44 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.67, "before": 92.73, "loss": 0.065, "playerId": 2707} |
| R225 | 03:45 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "CLAIM_RESOURCE", "remainingRound": 0, "targetNodeId": "S09"} |
| R225 | 03:45 | MED | 资源领取 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 在 洛阳驿(S09) 领取快马 |
| R225 | 03:45 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.26, "before": 87.31, "loss": 0.05, "playerId": 2751} |
| R225 | 03:45 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 25000, "edgeProgressPermille": 179, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.17921146953405018, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R225 | 03:45 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.61, "before": 92.67, "loss": 0.065, "playerId": 2707} |
| R226 | 03:46 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 26000, "edgeProgressPermille": 186, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.1863799283154122, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R226 | 03:46 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.55, "before": 92.61, "loss": 0.065, "playerId": 2707} |
| R226 | 03:46 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "CLAIM_TASK", "remainingRound": 2, "targetNodeId": "S09"} |
| R226 | 03:46 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.21, "before": 87.26, "loss": 0.05, "playerId": 2751} |
| R227 | 03:47 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 27000, "edgeProgressPermille": 193, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.1935483870967742, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R227 | 03:47 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.49, "before": 92.55, "loss": 0.065, "playerId": 2707} |
| R227 | 03:47 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "CLAIM_TASK", "remainingRound": 1, "targetNodeId": "S09"} |
| R227 | 03:47 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.16, "before": 87.21, "loss": 0.05, "playerId": 2751} |
| R228 | 03:48 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "CLAIM_TASK", "remainingRound": 0, "targetNodeId": "S09"} |
| R228 | 03:48 | HIGH | 任务完成 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 完成 争马换乘，+30 分，任务分 60 |
| R228 | 03:48 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.11, "before": 87.16, "loss": 0.05, "playerId": 2751} |
| R228 | 03:48 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 28000, "edgeProgressPermille": 200, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.2007168458781362, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R228 | 03:48 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.43, "before": 92.49, "loss": 0.065, "playerId": 2707} |
| R229 | 03:49 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 1000, "edgeProgressPermille": 18, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.018115942028985508, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R229 | 03:49 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 87.05, "before": 87.11, "loss": 0.055, "playerId": 2751} |
| R229 | 03:49 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 29000, "edgeProgressPermille": 207, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.2078853046594982, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R229 | 03:49 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.37, "before": 92.43, "loss": 0.065, "playerId": 2707} |
| R230 | 03:50 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 30000, "edgeProgressPermille": 215, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.21505376344086022, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R230 | 03:50 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.31, "before": 92.37, "loss": 0.065, "playerId": 2707} |
| R230 | 03:50 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 2000, "edgeProgressPermille": 36, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.036231884057971016, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R230 | 03:50 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.99, "before": 87.05, "loss": 0.055, "playerId": 2751} |
| R231 | 03:51 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 31000, "edgeProgressPermille": 222, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.2222222222222222, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R231 | 03:51 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.25, "before": 92.31, "loss": 0.065, "playerId": 2707} |
| R231 | 03:51 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 3000, "edgeProgressPermille": 54, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.05434782608695652, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R231 | 03:51 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.93, "before": 86.99, "loss": 0.055, "playerId": 2751} |
| R232 | 03:52 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 4000, "edgeProgressPermille": 72, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.07246376811594203, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R232 | 03:52 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.88, "before": 86.93, "loss": 0.055, "playerId": 2751} |
| R232 | 03:52 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 32000, "edgeProgressPermille": 229, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.22939068100358423, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R232 | 03:52 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.19, "before": 92.25, "loss": 0.065, "playerId": 2707} |
| R233 | 03:53 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 5000, "edgeProgressPermille": 90, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.09057971014492754, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R233 | 03:53 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.82, "before": 86.88, "loss": 0.055, "playerId": 2751} |
| R233 | 03:53 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 33000, "edgeProgressPermille": 236, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.23655913978494625, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R233 | 03:53 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.13, "before": 92.19, "loss": 0.065, "playerId": 2707} |
| R234 | 03:54 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 34000, "edgeProgressPermille": 243, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.24372759856630824, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R234 | 03:54 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.07, "before": 92.13, "loss": 0.065, "playerId": 2707} |
| R234 | 03:54 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 6000, "edgeProgressPermille": 108, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.10869565217391304, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R234 | 03:54 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.76, "before": 86.82, "loss": 0.055, "playerId": 2751} |
| R235 | 03:55 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 35000, "edgeProgressPermille": 250, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.25089605734767023, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R235 | 03:55 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 92.01, "before": 92.07, "loss": 0.065, "playerId": 2707} |
| R235 | 03:55 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 7000, "edgeProgressPermille": 126, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.12681159420289856, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R235 | 03:55 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.71, "before": 86.76, "loss": 0.055, "playerId": 2751} |
| R236 | 03:56 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 8000, "edgeProgressPermille": 144, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.14492753623188406, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R236 | 03:56 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.65, "before": 86.71, "loss": 0.055, "playerId": 2751} |
| R236 | 03:56 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 36000, "edgeProgressPermille": 258, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.25806451612903225, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R236 | 03:56 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.95, "before": 92.01, "loss": 0.065, "playerId": 2707} |
| R237 | 03:57 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 9000, "edgeProgressPermille": 163, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.16304347826086957, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R237 | 03:57 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.6, "before": 86.65, "loss": 0.055, "playerId": 2751} |
| R237 | 03:57 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 37000, "edgeProgressPermille": 265, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.26523297491039427, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R237 | 03:57 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.89, "before": 91.95, "loss": 0.065, "playerId": 2707} |
| R238 | 03:58 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 38000, "edgeProgressPermille": 272, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.2724014336917563, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R238 | 03:58 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.83, "before": 91.89, "loss": 0.065, "playerId": 2707} |
| R238 | 03:58 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 10000, "edgeProgressPermille": 181, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.18115942028985507, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R238 | 03:58 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.54, "before": 86.6, "loss": 0.055, "playerId": 2751} |
| R239 | 03:59 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 39000, "edgeProgressPermille": 279, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.27956989247311825, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R239 | 03:59 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.77, "before": 91.83, "loss": 0.065, "playerId": 2707} |
| R239 | 03:59 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 11000, "edgeProgressPermille": 199, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.19927536231884058, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R239 | 03:59 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.49, "before": 86.54, "loss": 0.055, "playerId": 2751} |
| R240 | 04:00 | MED | 任务过期 |  | T_005 在 五岭山道(S06) 过期 |
| R240 | 04:00 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 12000, "edgeProgressPermille": 217, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.21739130434782608, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R240 | 04:00 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.43, "before": 86.49, "loss": 0.055, "playerId": 2751} |
| R240 | 04:00 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 40000, "edgeProgressPermille": 286, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.2867383512544803, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R240 | 04:00 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.71, "before": 91.77, "loss": 0.065, "playerId": 2707} |
| R240 | 04:00 | MED | 任务刷新 |  | T_015 刷新在 灞桥驿(S13)，路线 MOUNTAIN，截止 R420 |
| R241 | 04:01 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 13000, "edgeProgressPermille": 235, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.23550724637681159, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R241 | 04:01 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.38, "before": 86.43, "loss": 0.055, "playerId": 2751} |
| R241 | 04:01 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 41000, "edgeProgressPermille": 293, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.2939068100358423, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R241 | 04:01 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.65, "before": 91.71, "loss": 0.065, "playerId": 2707} |
| R242 | 04:02 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 42000, "edgeProgressPermille": 301, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.3010752688172043, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R242 | 04:02 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.59, "before": 91.65, "loss": 0.065, "playerId": 2707} |
| R242 | 04:02 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 14000, "edgeProgressPermille": 253, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.2536231884057971, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R242 | 04:02 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.32, "before": 86.38, "loss": 0.055, "playerId": 2751} |
| R243 | 04:03 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 43000, "edgeProgressPermille": 308, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.30824372759856633, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R243 | 04:03 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.53, "before": 91.59, "loss": 0.065, "playerId": 2707} |
| R243 | 04:03 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 15000, "edgeProgressPermille": 271, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.2717391304347826, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R243 | 04:03 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.26, "before": 86.32, "loss": 0.055, "playerId": 2751} |
| R244 | 04:04 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 16000, "edgeProgressPermille": 289, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.2898550724637681, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R244 | 04:04 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.21, "before": 86.26, "loss": 0.055, "playerId": 2751} |
| R244 | 04:04 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 44000, "edgeProgressPermille": 315, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.3154121863799283, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R244 | 04:04 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.47, "before": 91.53, "loss": 0.065, "playerId": 2707} |
| R245 | 04:05 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 17000, "edgeProgressPermille": 307, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.3079710144927536, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R245 | 04:05 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.15, "before": 86.21, "loss": 0.055, "playerId": 2751} |
| R245 | 04:05 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 45000, "edgeProgressPermille": 322, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.3225806451612903, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R245 | 04:05 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.41, "before": 91.47, "loss": 0.065, "playerId": 2707} |
| R246 | 04:06 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 46000, "edgeProgressPermille": 329, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.32974910394265233, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R246 | 04:06 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.35, "before": 91.41, "loss": 0.065, "playerId": 2707} |
| R246 | 04:06 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 18000, "edgeProgressPermille": 326, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.32608695652173914, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R246 | 04:06 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.1, "before": 86.15, "loss": 0.055, "playerId": 2751} |
| R247 | 04:07 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 47000, "edgeProgressPermille": 336, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.33691756272401435, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R247 | 04:07 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.29, "before": 91.35, "loss": 0.065, "playerId": 2707} |
| R247 | 04:07 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 19000, "edgeProgressPermille": 344, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.3442028985507246, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R247 | 04:07 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 86.04, "before": 86.1, "loss": 0.055, "playerId": 2751} |
| R248 | 04:08 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 20000, "edgeProgressPermille": 362, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.36231884057971014, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R248 | 04:08 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.99, "before": 86.04, "loss": 0.055, "playerId": 2751} |
| R248 | 04:08 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 48000, "edgeProgressPermille": 344, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.34408602150537637, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R248 | 04:08 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.23, "before": 91.29, "loss": 0.065, "playerId": 2707} |
| R249 | 04:09 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 21000, "edgeProgressPermille": 380, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.3804347826086957, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R249 | 04:09 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.93, "before": 85.99, "loss": 0.055, "playerId": 2751} |
| R249 | 04:09 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 49000, "edgeProgressPermille": 351, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.35125448028673834, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R249 | 04:09 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.17, "before": 91.23, "loss": 0.065, "playerId": 2707} |
| R250 | 04:10 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 50000, "edgeProgressPermille": 358, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.35842293906810035, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R250 | 04:10 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.11, "before": 91.17, "loss": 0.065, "playerId": 2707} |
| R250 | 04:10 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 22000, "edgeProgressPermille": 398, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.39855072463768115, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R250 | 04:10 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.88, "before": 85.93, "loss": 0.055, "playerId": 2751} |
| R251 | 04:11 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 51000, "edgeProgressPermille": 365, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.3655913978494624, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R251 | 04:11 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 91.05, "before": 91.11, "loss": 0.065, "playerId": 2707} |
| R251 | 04:11 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 23000, "edgeProgressPermille": 416, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.4166666666666667, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R251 | 04:11 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.82, "before": 85.88, "loss": 0.055, "playerId": 2751} |
| R252 | 04:12 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 24000, "edgeProgressPermille": 434, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.43478260869565216, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R252 | 04:12 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.76, "before": 85.82, "loss": 0.055, "playerId": 2751} |
| R252 | 04:12 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 52000, "edgeProgressPermille": 372, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.3727598566308244, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R252 | 04:12 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.99, "before": 91.05, "loss": 0.065, "playerId": 2707} |
| R253 | 04:13 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 25000, "edgeProgressPermille": 452, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.4528985507246377, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R253 | 04:13 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.71, "before": 85.76, "loss": 0.055, "playerId": 2751} |
| R253 | 04:13 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 53000, "edgeProgressPermille": 379, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.37992831541218636, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R253 | 04:13 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.93, "before": 90.99, "loss": 0.065, "playerId": 2707} |
| R254 | 04:14 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 54000, "edgeProgressPermille": 387, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.3870967741935484, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R254 | 04:14 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.87, "before": 90.93, "loss": 0.065, "playerId": 2707} |
| R254 | 04:14 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 26000, "edgeProgressPermille": 471, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.47101449275362317, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R254 | 04:14 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.65, "before": 85.71, "loss": 0.055, "playerId": 2751} |
| R255 | 04:15 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 55000, "edgeProgressPermille": 394, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.3942652329749104, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R255 | 04:15 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.81, "before": 90.87, "loss": 0.065, "playerId": 2707} |
| R255 | 04:15 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 27000, "edgeProgressPermille": 489, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.4891304347826087, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R255 | 04:15 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.6, "before": 85.65, "loss": 0.055, "playerId": 2751} |
| R256 | 04:16 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 28000, "edgeProgressPermille": 507, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.5072463768115942, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R256 | 04:16 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.54, "before": 85.6, "loss": 0.055, "playerId": 2751} |
| R256 | 04:16 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 56000, "edgeProgressPermille": 401, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.4014336917562724, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R256 | 04:16 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.75, "before": 90.81, "loss": 0.065, "playerId": 2707} |
| R257 | 04:17 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 29000, "edgeProgressPermille": 525, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.5253623188405797, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R257 | 04:17 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.49, "before": 85.54, "loss": 0.055, "playerId": 2751} |
| R257 | 04:17 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 57000, "edgeProgressPermille": 408, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.40860215053763443, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R257 | 04:17 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.69, "before": 90.75, "loss": 0.065, "playerId": 2707} |
| R258 | 04:18 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 58000, "edgeProgressPermille": 415, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.4157706093189964, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R258 | 04:18 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.63, "before": 90.69, "loss": 0.065, "playerId": 2707} |
| R258 | 04:18 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 30000, "edgeProgressPermille": 543, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.5434782608695652, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R258 | 04:18 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.43, "before": 85.49, "loss": 0.055, "playerId": 2751} |
| R259 | 04:19 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 59000, "edgeProgressPermille": 422, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.4229390681003584, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R259 | 04:19 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.57, "before": 90.63, "loss": 0.065, "playerId": 2707} |
| R259 | 04:19 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 31000, "edgeProgressPermille": 561, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.5615942028985508, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R259 | 04:19 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.38, "before": 85.43, "loss": 0.055, "playerId": 2751} |
| R260 | 04:20 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 32000, "edgeProgressPermille": 579, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.5797101449275363, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R260 | 04:20 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.32, "before": 85.38, "loss": 0.055, "playerId": 2751} |
| R260 | 04:20 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 60000, "edgeProgressPermille": 430, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.43010752688172044, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R260 | 04:20 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.51, "before": 90.57, "loss": 0.065, "playerId": 2707} |
| R261 | 04:21 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 33000, "edgeProgressPermille": 597, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.5978260869565217, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R261 | 04:21 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.26, "before": 85.32, "loss": 0.055, "playerId": 2751} |
| R261 | 04:21 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 61000, "edgeProgressPermille": 437, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.43727598566308246, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R261 | 04:21 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.45, "before": 90.51, "loss": 0.065, "playerId": 2707} |
| R262 | 04:22 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 62000, "edgeProgressPermille": 444, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.4444444444444444, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R262 | 04:22 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.39, "before": 90.45, "loss": 0.065, "playerId": 2707} |
| R262 | 04:22 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 34000, "edgeProgressPermille": 615, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.6159420289855072, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R262 | 04:22 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.21, "before": 85.26, "loss": 0.055, "playerId": 2751} |
| R263 | 04:23 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 63000, "edgeProgressPermille": 451, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.45161290322580644, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R263 | 04:23 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.33, "before": 90.39, "loss": 0.065, "playerId": 2707} |
| R263 | 04:23 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 35000, "edgeProgressPermille": 634, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.6340579710144928, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R263 | 04:23 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.15, "before": 85.21, "loss": 0.055, "playerId": 2751} |
| R264 | 04:24 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 36000, "edgeProgressPermille": 652, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.6521739130434783, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R264 | 04:24 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.1, "before": 85.15, "loss": 0.055, "playerId": 2751} |
| R264 | 04:24 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 64000, "edgeProgressPermille": 458, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.45878136200716846, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R264 | 04:24 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.27, "before": 90.33, "loss": 0.065, "playerId": 2707} |
| R265 | 04:25 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 37000, "edgeProgressPermille": 670, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.6702898550724637, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R265 | 04:25 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 85.04, "before": 85.1, "loss": 0.055, "playerId": 2751} |
| R265 | 04:25 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 65000, "edgeProgressPermille": 465, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.4659498207885305, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R265 | 04:25 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.21, "before": 90.27, "loss": 0.065, "playerId": 2707} |
| R266 | 04:26 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 66000, "edgeProgressPermille": 473, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.4731182795698925, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R266 | 04:26 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.15, "before": 90.21, "loss": 0.065, "playerId": 2707} |
| R266 | 04:26 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 38000, "edgeProgressPermille": 688, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.6884057971014492, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R266 | 04:26 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.99, "before": 85.04, "loss": 0.055, "playerId": 2751} |
| R267 | 04:27 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 67000, "edgeProgressPermille": 480, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.48028673835125446, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R267 | 04:27 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.09, "before": 90.15, "loss": 0.065, "playerId": 2707} |
| R267 | 04:27 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 39000, "edgeProgressPermille": 706, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.7065217391304348, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R267 | 04:27 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.93, "before": 84.99, "loss": 0.055, "playerId": 2751} |
| R268 | 04:28 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 40000, "edgeProgressPermille": 724, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.7246376811594203, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R268 | 04:28 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.88, "before": 84.93, "loss": 0.055, "playerId": 2751} |
| R268 | 04:28 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 68000, "edgeProgressPermille": 487, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.4874551971326165, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R268 | 04:28 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 90.03, "before": 90.09, "loss": 0.065, "playerId": 2707} |
| R269 | 04:29 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 41000, "edgeProgressPermille": 742, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.7427536231884058, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R269 | 04:29 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.82, "before": 84.88, "loss": 0.055, "playerId": 2751} |
| R269 | 04:29 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 69000, "edgeProgressPermille": 494, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.4946236559139785, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R269 | 04:29 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.97, "before": 90.03, "loss": 0.065, "playerId": 2707} |
| R270 | 04:30 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 70000, "edgeProgressPermille": 501, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5017921146953405, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R270 | 04:30 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.91, "before": 89.97, "loss": 0.065, "playerId": 2707} |
| R270 | 04:30 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 42000, "edgeProgressPermille": 760, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.7608695652173914, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R270 | 04:30 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.76, "before": 84.82, "loss": 0.055, "playerId": 2751} |
| R271 | 04:31 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 71000, "edgeProgressPermille": 508, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5089605734767025, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R271 | 04:31 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.85, "before": 89.91, "loss": 0.065, "playerId": 2707} |
| R271 | 04:31 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 43000, "edgeProgressPermille": 778, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.7789855072463768, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R271 | 04:31 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.71, "before": 84.76, "loss": 0.055, "playerId": 2751} |
| R272 | 04:32 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 44000, "edgeProgressPermille": 797, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.7971014492753623, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R272 | 04:32 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.65, "before": 84.71, "loss": 0.055, "playerId": 2751} |
| R272 | 04:32 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 72000, "edgeProgressPermille": 516, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5161290322580645, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R272 | 04:32 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.79, "before": 89.85, "loss": 0.065, "playerId": 2707} |
| R273 | 04:33 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 45000, "edgeProgressPermille": 815, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.8152173913043478, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R273 | 04:33 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.6, "before": 84.65, "loss": 0.055, "playerId": 2751} |
| R273 | 04:33 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 73000, "edgeProgressPermille": 523, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5232974910394266, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R273 | 04:33 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.73, "before": 89.79, "loss": 0.065, "playerId": 2707} |
| R274 | 04:34 | HIGH | 派遣 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 派遣队伍侦察 潼关驿(S11)，预计 R279 完成 |
| R274 | 04:34 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 74000, "edgeProgressPermille": 530, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5304659498207885, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R274 | 04:34 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.67, "before": 89.73, "loss": 0.065, "playerId": 2707} |
| R274 | 04:34 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 46000, "edgeProgressPermille": 833, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.8333333333333334, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R274 | 04:34 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.54, "before": 84.6, "loss": 0.055, "playerId": 2751} |
| R275 | 04:35 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 75000, "edgeProgressPermille": 537, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5376344086021505, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R275 | 04:35 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.61, "before": 89.67, "loss": 0.065, "playerId": 2707} |
| R275 | 04:35 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 47000, "edgeProgressPermille": 851, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.8514492753623188, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R275 | 04:35 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.49, "before": 84.54, "loss": 0.055, "playerId": 2751} |
| R276 | 04:36 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 48000, "edgeProgressPermille": 869, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.8695652173913043, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R276 | 04:36 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.43, "before": 84.49, "loss": 0.055, "playerId": 2751} |
| R276 | 04:36 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 76000, "edgeProgressPermille": 544, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5448028673835126, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R276 | 04:36 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.55, "before": 89.61, "loss": 0.065, "playerId": 2707} |
| R277 | 04:37 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 49000, "edgeProgressPermille": 887, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.8876811594202898, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R277 | 04:37 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.38, "before": 84.43, "loss": 0.055, "playerId": 2751} |
| R277 | 04:37 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 77000, "edgeProgressPermille": 551, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5519713261648745, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R277 | 04:37 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.49, "before": 89.55, "loss": 0.065, "playerId": 2707} |
| R278 | 04:38 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 78000, "edgeProgressPermille": 559, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5591397849462365, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R278 | 04:38 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.43, "before": 89.49, "loss": 0.065, "playerId": 2707} |
| R278 | 04:38 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 50000, "edgeProgressPermille": 905, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.9057971014492754, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R278 | 04:38 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.32, "before": 84.38, "loss": 0.055, "playerId": 2751} |
| R279 | 04:39 | MED | SCOUT_MARKER_ADD | RED codex-py/0.1(2751) | {"expireRound": 324, "playerId": 2751, "remainingTriggers": 1, "targetNodeId": "S11"} |
| R279 | 04:39 | MED | 侦察回报 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 侦察 潼关驿(S11)：无障碍，资源 无明显资源 |
| R279 | 04:39 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 79000, "edgeProgressPermille": 566, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5663082437275986, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R279 | 04:39 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.37, "before": 89.43, "loss": 0.065, "playerId": 2707} |
| R279 | 04:39 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 51000, "edgeProgressPermille": 923, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.9239130434782609, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R279 | 04:39 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.26, "before": 84.32, "loss": 0.055, "playerId": 2751} |
| R280 | 04:40 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 52000, "edgeProgressPermille": 942, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.9420289855072463, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R280 | 04:40 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.21, "before": 84.26, "loss": 0.055, "playerId": 2751} |
| R280 | 04:40 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 80000, "edgeProgressPermille": 573, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5734767025089605, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R280 | 04:40 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.31, "before": 89.37, "loss": 0.065, "playerId": 2707} |
| R281 | 04:41 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 53000, "edgeProgressPermille": 960, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.9601449275362319, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R281 | 04:41 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.15, "before": 84.21, "loss": 0.055, "playerId": 2751} |
| R281 | 04:41 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 81000, "edgeProgressPermille": 580, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5806451612903226, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R281 | 04:41 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.25, "before": 89.31, "loss": 0.065, "playerId": 2707} |
| R282 | 04:42 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 82000, "edgeProgressPermille": 587, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5878136200716846, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R282 | 04:42 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.19, "before": 89.25, "loss": 0.065, "playerId": 2707} |
| R282 | 04:42 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 54000, "edgeProgressPermille": 978, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.9782608695652174, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R282 | 04:42 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.1, "before": 84.15, "loss": 0.055, "playerId": 2751} |
| R283 | 04:43 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 83000, "edgeProgressPermille": 594, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5949820788530465, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R283 | 04:43 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.13, "before": 89.19, "loss": 0.065, "playerId": 2707} |
| R283 | 04:43 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 55000, "edgeProgressPermille": 996, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 0.9963768115942029, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R283 | 04:43 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 84.04, "before": 84.1, "loss": 0.055, "playerId": 2751} |
| R284 | 04:44 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 55200, "edgeProgressPermille": 1000, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2751, "progress": 1.0, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R284 | 04:44 | HIGH | 进点 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 进入 武关(S10) |
| R284 | 04:44 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.99, "before": 84.04, "loss": 0.055, "playerId": 2751} |
| R284 | 04:44 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 84000, "edgeProgressPermille": 602, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.6021505376344086, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R284 | 04:44 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.07, "before": 89.13, "loss": 0.065, "playerId": 2707} |
| R285 | 04:45 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 1000, "edgeProgressPermille": 25, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.025879917184265012, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R285 | 04:45 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.93, "before": 83.99, "loss": 0.055, "playerId": 2751} |
| R285 | 04:45 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 85000, "edgeProgressPermille": 609, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2707, "progress": 0.6093189964157706, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R285 | 04:45 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 89.01, "before": 89.07, "loss": 0.065, "playerId": 2707} |
| R286 | 04:46 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 9, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.009775171065493646, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R286 | 04:46 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.95, "before": 89.01, "loss": 0.065, "playerId": 2707} |
| R286 | 04:46 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 2000, "edgeProgressPermille": 51, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.051759834368530024, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R286 | 04:46 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.88, "before": 83.93, "loss": 0.055, "playerId": 2751} |
| R287 | 04:47 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 19, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.019550342130987292, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R287 | 04:47 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.89, "before": 88.95, "loss": 0.065, "playerId": 2707} |
| R287 | 04:47 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 3000, "edgeProgressPermille": 77, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.07763975155279502, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R287 | 04:47 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.82, "before": 83.88, "loss": 0.055, "playerId": 2751} |
| R288 | 04:48 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 4000, "edgeProgressPermille": 103, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.10351966873706005, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R288 | 04:48 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.76, "before": 83.82, "loss": 0.055, "playerId": 2751} |
| R288 | 04:48 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 29, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.02932551319648094, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R288 | 04:48 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.83, "before": 88.89, "loss": 0.065, "playerId": 2707} |
| R289 | 04:49 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 5000, "edgeProgressPermille": 129, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.12939958592132506, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R289 | 04:49 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.71, "before": 83.76, "loss": 0.055, "playerId": 2751} |
| R289 | 04:49 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 39, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.039100684261974585, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R289 | 04:49 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.77, "before": 88.83, "loss": 0.065, "playerId": 2707} |
| R290 | 04:50 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 48, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.04887585532746823, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R290 | 04:50 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.71, "before": 88.77, "loss": 0.065, "playerId": 2707} |
| R290 | 04:50 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 6000, "edgeProgressPermille": 155, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.15527950310559005, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R290 | 04:50 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.65, "before": 83.71, "loss": 0.055, "playerId": 2751} |
| R291 | 04:51 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 58, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.05865102639296188, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R291 | 04:51 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.65, "before": 88.71, "loss": 0.065, "playerId": 2707} |
| R291 | 04:51 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 7000, "edgeProgressPermille": 181, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.18115942028985507, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R291 | 04:51 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.6, "before": 83.65, "loss": 0.055, "playerId": 2751} |
| R292 | 04:52 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 8000, "edgeProgressPermille": 207, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.2070393374741201, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R292 | 04:52 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.54, "before": 83.6, "loss": 0.055, "playerId": 2751} |
| R292 | 04:52 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 68, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.06842619745845552, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R292 | 04:52 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.59, "before": 88.65, "loss": 0.065, "playerId": 2707} |
| R293 | 04:53 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 9000, "edgeProgressPermille": 232, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.2329192546583851, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R293 | 04:53 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.49, "before": 83.54, "loss": 0.055, "playerId": 2751} |
| R293 | 04:53 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 78, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.07820136852394917, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R293 | 04:53 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.53, "before": 88.59, "loss": 0.065, "playerId": 2707} |
| R294 | 04:54 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 87, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.08797653958944282, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R294 | 04:54 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.47, "before": 88.53, "loss": 0.065, "playerId": 2707} |
| R294 | 04:54 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 10000, "edgeProgressPermille": 258, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.2587991718426501, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R294 | 04:54 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.43, "before": 83.49, "loss": 0.055, "playerId": 2751} |
| R295 | 04:55 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 97, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.09775171065493646, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R295 | 04:55 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.41, "before": 88.47, "loss": 0.065, "playerId": 2707} |
| R295 | 04:55 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 11000, "edgeProgressPermille": 284, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.28467908902691513, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R295 | 04:55 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.38, "before": 83.43, "loss": 0.055, "playerId": 2751} |
| R296 | 04:56 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 12000, "edgeProgressPermille": 310, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.3105590062111801, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R296 | 04:56 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.32, "before": 83.38, "loss": 0.055, "playerId": 2751} |
| R296 | 04:56 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 107, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.10752688172043011, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R296 | 04:56 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.35, "before": 88.41, "loss": 0.065, "playerId": 2707} |
| R297 | 04:57 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 13000, "edgeProgressPermille": 336, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.3364389233954451, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R297 | 04:57 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.26, "before": 83.32, "loss": 0.055, "playerId": 2751} |
| R297 | 04:57 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 12000, "edgeProgressPermille": 117, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.11730205278592376, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R297 | 04:57 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.29, "before": 88.35, "loss": 0.065, "playerId": 2707} |
| R298 | 04:58 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 13000, "edgeProgressPermille": 127, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.1270772238514174, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R298 | 04:58 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.23, "before": 88.29, "loss": 0.065, "playerId": 2707} |
| R298 | 04:58 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 14000, "edgeProgressPermille": 362, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.36231884057971014, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R298 | 04:58 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.21, "before": 83.26, "loss": 0.055, "playerId": 2751} |
| R299 | 04:59 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 136, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.13685239491691104, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R299 | 04:59 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.17, "before": 88.23, "loss": 0.065, "playerId": 2707} |
| R299 | 04:59 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 15000, "edgeProgressPermille": 388, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.38819875776397517, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R299 | 04:59 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.15, "before": 83.21, "loss": 0.055, "playerId": 2751} |
| R300 | 05:00 | MED | 任务过期 |  | T_010 在 洛阳驿(S09) 过期 |
| R300 | 05:00 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 16000, "edgeProgressPermille": 414, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.4140786749482402, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R300 | 05:00 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.1, "before": 83.15, "loss": 0.055, "playerId": 2751} |
| R300 | 05:00 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 15000, "edgeProgressPermille": 146, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.1466275659824047, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R300 | 05:00 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.11, "before": 88.17, "loss": 0.065, "playerId": 2707} |
| R300 | 05:00 | MED | 任务刷新 |  | T_016 刷新在 梅关驿(S03)，路线 ROAD，截止 R520 |
| R300 | 05:00 | MED | 任务刷新 |  | T_017 刷新在 洞庭水驿(S05)，路线 WATER，截止 R520 |
| R300 | 05:00 | MED | 任务刷新 |  | T_018 刷新在 关中平原(S12)，路线 MOUNTAIN，截止 R520 |
| R301 | 05:01 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 17000, "edgeProgressPermille": 439, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.43995859213250516, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R301 | 05:01 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 83.04, "before": 83.1, "loss": 0.055, "playerId": 2751} |
| R301 | 05:01 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 16000, "edgeProgressPermille": 156, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.15640273704789834, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R301 | 05:01 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 88.05, "before": 88.11, "loss": 0.065, "playerId": 2707} |
| R302 | 05:02 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 17000, "edgeProgressPermille": 166, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.16617790811339198, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R302 | 05:02 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.99, "before": 88.05, "loss": 0.065, "playerId": 2707} |
| R302 | 05:02 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 18000, "edgeProgressPermille": 465, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.4658385093167702, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R302 | 05:02 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.99, "before": 83.04, "loss": 0.055, "playerId": 2751} |
| R303 | 05:03 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 18000, "edgeProgressPermille": 175, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.17595307917888564, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R303 | 05:03 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.93, "before": 87.99, "loss": 0.065, "playerId": 2707} |
| R303 | 05:03 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 19000, "edgeProgressPermille": 491, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.4917184265010352, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R303 | 05:03 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.93, "before": 82.99, "loss": 0.055, "playerId": 2751} |
| R304 | 05:04 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 20000, "edgeProgressPermille": 517, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.5175983436853002, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R304 | 05:04 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.88, "before": 82.93, "loss": 0.055, "playerId": 2751} |
| R304 | 05:04 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 19000, "edgeProgressPermille": 185, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.18572825024437928, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R304 | 05:04 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.87, "before": 87.93, "loss": 0.065, "playerId": 2707} |
| R305 | 05:05 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 21000, "edgeProgressPermille": 543, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.5434782608695652, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R305 | 05:05 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.82, "before": 82.88, "loss": 0.055, "playerId": 2751} |
| R305 | 05:05 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 20000, "edgeProgressPermille": 195, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.19550342130987292, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R305 | 05:05 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.81, "before": 87.87, "loss": 0.065, "playerId": 2707} |
| R306 | 05:06 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 21000, "edgeProgressPermille": 205, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.20527859237536658, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R306 | 05:06 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.75, "before": 87.81, "loss": 0.065, "playerId": 2707} |
| R306 | 05:06 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 22000, "edgeProgressPermille": 569, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.5693581780538303, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R306 | 05:06 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.76, "before": 82.82, "loss": 0.055, "playerId": 2751} |
| R307 | 05:07 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 22000, "edgeProgressPermille": 215, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.21505376344086022, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R307 | 05:07 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.69, "before": 87.75, "loss": 0.065, "playerId": 2707} |
| R307 | 05:07 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 23000, "edgeProgressPermille": 595, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.5952380952380952, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R307 | 05:07 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.71, "before": 82.76, "loss": 0.055, "playerId": 2751} |
| R308 | 05:08 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 24000, "edgeProgressPermille": 621, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.6211180124223602, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R308 | 05:08 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.65, "before": 82.71, "loss": 0.055, "playerId": 2751} |
| R308 | 05:08 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 23000, "edgeProgressPermille": 224, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.22482893450635386, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R308 | 05:08 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.63, "before": 87.69, "loss": 0.065, "playerId": 2707} |
| R309 | 05:09 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 25000, "edgeProgressPermille": 646, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.6469979296066253, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R309 | 05:09 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.6, "before": 82.65, "loss": 0.055, "playerId": 2751} |
| R309 | 05:09 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 24000, "edgeProgressPermille": 234, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.23460410557184752, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R309 | 05:09 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.57, "before": 87.63, "loss": 0.065, "playerId": 2707} |
| R310 | 05:10 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 25000, "edgeProgressPermille": 244, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.24437927663734116, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R310 | 05:10 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.51, "before": 87.57, "loss": 0.065, "playerId": 2707} |
| R310 | 05:10 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 26000, "edgeProgressPermille": 672, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.6728778467908902, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R310 | 05:10 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.54, "before": 82.6, "loss": 0.055, "playerId": 2751} |
| R311 | 05:11 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 26000, "edgeProgressPermille": 254, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.2541544477028348, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R311 | 05:11 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.45, "before": 87.51, "loss": 0.065, "playerId": 2707} |
| R311 | 05:11 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 27000, "edgeProgressPermille": 698, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.6987577639751553, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R311 | 05:11 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.49, "before": 82.54, "loss": 0.055, "playerId": 2751} |
| R312 | 05:12 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 28000, "edgeProgressPermille": 724, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.7246376811594203, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R312 | 05:12 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.43, "before": 82.49, "loss": 0.055, "playerId": 2751} |
| R312 | 05:12 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 27000, "edgeProgressPermille": 263, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.26392961876832843, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R312 | 05:12 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.39, "before": 87.45, "loss": 0.065, "playerId": 2707} |
| R313 | 05:13 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 29000, "edgeProgressPermille": 750, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.7505175983436853, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R313 | 05:13 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.38, "before": 82.43, "loss": 0.055, "playerId": 2751} |
| R313 | 05:13 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 28000, "edgeProgressPermille": 273, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.27370478983382207, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R313 | 05:13 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.33, "before": 87.39, "loss": 0.065, "playerId": 2707} |
| R314 | 05:14 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 29000, "edgeProgressPermille": 283, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.28347996089931576, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R314 | 05:14 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.27, "before": 87.33, "loss": 0.065, "playerId": 2707} |
| R314 | 05:14 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 30000, "edgeProgressPermille": 776, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.7763975155279503, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R314 | 05:14 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.32, "before": 82.38, "loss": 0.055, "playerId": 2751} |
| R315 | 05:15 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 30000, "edgeProgressPermille": 293, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.2932551319648094, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R315 | 05:15 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.21, "before": 87.27, "loss": 0.065, "playerId": 2707} |
| R315 | 05:15 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 31000, "edgeProgressPermille": 802, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.8022774327122153, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R315 | 05:15 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.26, "before": 82.32, "loss": 0.055, "playerId": 2751} |
| R316 | 05:16 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 32000, "edgeProgressPermille": 828, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.8281573498964804, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R316 | 05:16 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.21, "before": 82.26, "loss": 0.055, "playerId": 2751} |
| R316 | 05:16 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 31000, "edgeProgressPermille": 303, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.30303030303030304, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R316 | 05:16 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.15, "before": 87.21, "loss": 0.065, "playerId": 2707} |
| R317 | 05:17 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 33000, "edgeProgressPermille": 854, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.8540372670807453, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R317 | 05:17 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.15, "before": 82.21, "loss": 0.055, "playerId": 2751} |
| R317 | 05:17 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 32000, "edgeProgressPermille": 312, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.3128054740957967, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R317 | 05:17 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.09, "before": 87.15, "loss": 0.065, "playerId": 2707} |
| R318 | 05:18 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 33000, "edgeProgressPermille": 322, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.3225806451612903, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R318 | 05:18 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 87.03, "before": 87.09, "loss": 0.065, "playerId": 2707} |
| R318 | 05:18 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 34000, "edgeProgressPermille": 879, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.8799171842650103, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R318 | 05:18 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.1, "before": 82.15, "loss": 0.055, "playerId": 2751} |
| R319 | 05:19 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 34000, "edgeProgressPermille": 332, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.33235581622678395, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R319 | 05:19 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.97, "before": 87.03, "loss": 0.065, "playerId": 2707} |
| R319 | 05:19 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 35000, "edgeProgressPermille": 905, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.9057971014492754, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R319 | 05:19 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 82.04, "before": 82.1, "loss": 0.055, "playerId": 2751} |
| R320 | 05:20 | MED | 任务过期 |  | T_006 在 江南码头(S04) 过期 |
| R320 | 05:20 | MED | 任务过期 |  | T_007 在 荆襄大驿(S07) 过期 |
| R320 | 05:20 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 36000, "edgeProgressPermille": 931, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.9316770186335404, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R320 | 05:20 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 81.99, "before": 82.04, "loss": 0.055, "playerId": 2751} |
| R320 | 05:20 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 35000, "edgeProgressPermille": 342, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.3421309872922776, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R320 | 05:20 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.91, "before": 86.97, "loss": 0.065, "playerId": 2707} |
| R321 | 05:21 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 37000, "edgeProgressPermille": 957, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.9575569358178054, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R321 | 05:21 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 81.93, "before": 81.99, "loss": 0.055, "playerId": 2751} |
| R321 | 05:21 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 36000, "edgeProgressPermille": 351, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.3519061583577713, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R321 | 05:21 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.85, "before": 86.91, "loss": 0.065, "playerId": 2707} |
| R322 | 05:22 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 37000, "edgeProgressPermille": 361, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.3616813294232649, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R322 | 05:22 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.79, "before": 86.85, "loss": 0.065, "playerId": 2707} |
| R322 | 05:22 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 38000, "edgeProgressPermille": 983, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 0.9834368530020704, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R322 | 05:22 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 81.88, "before": 81.93, "loss": 0.055, "playerId": 2751} |
| R323 | 05:23 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 38000, "edgeProgressPermille": 371, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.37145650048875856, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R323 | 05:23 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.73, "before": 86.79, "loss": 0.065, "playerId": 2707} |
| R323 | 05:23 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 38640, "edgeProgressPermille": 1000, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2751, "progress": 1.0, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R323 | 05:23 | HIGH | 进点 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 进入 潼关驿(S11) |
| R323 | 05:23 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 81.82, "before": 81.88, "loss": 0.055, "playerId": 2751} |
| R324 | 05:24 | MED | SCOUT_MARKER_APPLY | RED codex-py/0.1(2751) | {"afterRound": 2, "beforeRound": 4, "playerId": 2751, "processType": "PASS_TRANSFER", "targetNodeId": "S11"} |
| R324 | 05:24 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "PASS_TRANSFER", "remainingRound": 1, "targetNodeId": "S11"} |
| R324 | 05:24 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 81.77, "before": 81.82, "loss": 0.05, "playerId": 2751} |
| R324 | 05:24 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 39000, "edgeProgressPermille": 381, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.3812316715542522, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R324 | 05:24 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.67, "before": 86.73, "loss": 0.065, "playerId": 2707} |
| R325 | 05:25 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "PASS_TRANSFER", "remainingRound": 0, "targetNodeId": "S11"} |
| R325 | 05:25 | MED | SCOUT_MARKER_CONSUME | RED codex-py/0.1(2751) | {"playerId": 2751, "remainingTriggers": 0, "targetNodeId": "S11"} |
| R325 | 05:25 | MED | 处理完成 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 在 潼关驿(S11) 完成关口转运 |
| R325 | 05:25 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 81.72, "before": 81.77, "loss": 0.05, "playerId": 2751} |
| R325 | 05:25 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 40000, "edgeProgressPermille": 391, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.39100684261974583, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R325 | 05:25 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.61, "before": 86.67, "loss": 0.065, "playerId": 2707} |
| R326 | 05:26 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 41000, "edgeProgressPermille": 400, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.40078201368523947, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R326 | 05:26 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.55, "before": 86.61, "loss": 0.065, "playerId": 2707} |
| R326 | 05:26 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 1000, "edgeProgressPermille": 18, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.018975332068311195, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R326 | 05:26 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 81.66, "before": 81.72, "loss": 0.065, "playerId": 2751} |
| R327 | 05:27 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 42000, "edgeProgressPermille": 410, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.41055718475073316, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R327 | 05:27 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.49, "before": 86.55, "loss": 0.065, "playerId": 2707} |
| R327 | 05:27 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 2000, "edgeProgressPermille": 37, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.03795066413662239, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R327 | 05:27 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 81.6, "before": 81.66, "loss": 0.065, "playerId": 2751} |
| R328 | 05:28 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 3000, "edgeProgressPermille": 56, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.056925996204933584, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R328 | 05:28 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 81.5, "before": 81.6, "loss": 0.0975, "playerId": 2751} |
| R328 | 05:28 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 43000, "edgeProgressPermille": 420, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.4203323558162268, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R328 | 05:28 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.39, "before": 86.49, "loss": 0.0975, "playerId": 2707} |
| R329 | 05:29 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 4000, "edgeProgressPermille": 75, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.07590132827324478, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R329 | 05:29 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 81.4, "before": 81.5, "loss": 0.0975, "playerId": 2751} |
| R329 | 05:29 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 44000, "edgeProgressPermille": 430, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.43010752688172044, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R329 | 05:29 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.29, "before": 86.39, "loss": 0.0975, "playerId": 2707} |
| R330 | 05:30 | MED | 任务过期 |  | T_011 在 荆襄大驿(S07) 过期 |
| R330 | 05:30 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 45000, "edgeProgressPermille": 439, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.4398826979472141, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R330 | 05:30 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.19, "before": 86.29, "loss": 0.0975, "playerId": 2707} |
| R330 | 05:30 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 5000, "edgeProgressPermille": 94, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.09487666034155598, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R330 | 05:30 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 81.3, "before": 81.4, "loss": 0.0975, "playerId": 2751} |
| R331 | 05:31 | HIGH | 派遣 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 派遣队伍侦察 朱雀门(S14)，预计 R334 完成 |
| R331 | 05:31 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 46000, "edgeProgressPermille": 449, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.4496578690127077, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R331 | 05:31 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 86.09, "before": 86.19, "loss": 0.0975, "playerId": 2707} |
| R331 | 05:31 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 6000, "edgeProgressPermille": 113, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.11385199240986717, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R331 | 05:31 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 81.2, "before": 81.3, "loss": 0.0975, "playerId": 2751} |
| R332 | 05:32 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 7000, "edgeProgressPermille": 132, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.13282732447817835, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R332 | 05:32 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 81.1, "before": 81.2, "loss": 0.0975, "playerId": 2751} |
| R332 | 05:32 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 47000, "edgeProgressPermille": 459, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.45943304007820135, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R332 | 05:32 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.99, "before": 86.09, "loss": 0.0975, "playerId": 2707} |
| R333 | 05:33 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 8000, "edgeProgressPermille": 151, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.15180265654648956, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R333 | 05:33 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 81.0, "before": 81.1, "loss": 0.0975, "playerId": 2751} |
| R333 | 05:33 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 48000, "edgeProgressPermille": 469, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.46920821114369504, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R333 | 05:33 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.89, "before": 85.99, "loss": 0.0975, "playerId": 2707} |
| R334 | 05:34 | MED | SCOUT_MARKER_ADD | RED codex-py/0.1(2751) | {"expireRound": 379, "playerId": 2751, "remainingTriggers": 1, "targetNodeId": "S14"} |
| R334 | 05:34 | MED | 侦察回报 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 侦察 朱雀门(S14)：无障碍，资源 无明显资源 |
| R334 | 05:34 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 49000, "edgeProgressPermille": 478, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.4789833822091887, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R334 | 05:34 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.79, "before": 85.89, "loss": 0.0975, "playerId": 2707} |
| R334 | 05:34 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 9000, "edgeProgressPermille": 170, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.17077798861480076, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R334 | 05:34 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 80.9, "before": 81.0, "loss": 0.0975, "playerId": 2751} |
| R335 | 05:35 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 50000, "edgeProgressPermille": 488, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.4887585532746823, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R335 | 05:35 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.69, "before": 85.79, "loss": 0.0975, "playerId": 2707} |
| R335 | 05:35 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 10000, "edgeProgressPermille": 189, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.18975332068311196, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R335 | 05:35 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 80.8, "before": 80.9, "loss": 0.0975, "playerId": 2751} |
| R336 | 05:36 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 11000, "edgeProgressPermille": 208, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.20872865275142316, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R336 | 05:36 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 80.7, "before": 80.8, "loss": 0.0975, "playerId": 2751} |
| R336 | 05:36 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 51000, "edgeProgressPermille": 498, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.49853372434017595, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R336 | 05:36 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.59, "before": 85.69, "loss": 0.0975, "playerId": 2707} |
| R337 | 05:37 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 12000, "edgeProgressPermille": 227, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.22770398481973433, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R337 | 05:37 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 80.6, "before": 80.7, "loss": 0.0975, "playerId": 2751} |
| R337 | 05:37 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 52000, "edgeProgressPermille": 508, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5083088954056696, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R337 | 05:37 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.49, "before": 85.59, "loss": 0.0975, "playerId": 2707} |
| R338 | 05:38 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 53000, "edgeProgressPermille": 518, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5180840664711632, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R338 | 05:38 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.39, "before": 85.49, "loss": 0.0975, "playerId": 2707} |
| R338 | 05:38 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 13000, "edgeProgressPermille": 246, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.24667931688804554, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R338 | 05:38 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 80.5, "before": 80.6, "loss": 0.0975, "playerId": 2751} |
| R339 | 05:39 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 54000, "edgeProgressPermille": 527, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5278592375366569, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R339 | 05:39 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.29, "before": 85.39, "loss": 0.0975, "playerId": 2707} |
| R339 | 05:39 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 14000, "edgeProgressPermille": 265, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.2656546489563567, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R339 | 05:39 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 80.4, "before": 80.5, "loss": 0.0975, "playerId": 2751} |
| R340 | 05:40 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 15000, "edgeProgressPermille": 284, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.2846299810246679, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R340 | 05:40 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 80.3, "before": 80.4, "loss": 0.0975, "playerId": 2751} |
| R340 | 05:40 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 55000, "edgeProgressPermille": 537, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5376344086021505, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R340 | 05:40 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.19, "before": 85.29, "loss": 0.0975, "playerId": 2707} |
| R341 | 05:41 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 16000, "edgeProgressPermille": 303, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.3036053130929791, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R341 | 05:41 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 80.2, "before": 80.3, "loss": 0.0975, "playerId": 2751} |
| R341 | 05:41 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 56000, "edgeProgressPermille": 547, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5474095796676441, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R341 | 05:41 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 85.09, "before": 85.19, "loss": 0.0975, "playerId": 2707} |
| R342 | 05:42 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 57000, "edgeProgressPermille": 557, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5571847507331378, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R342 | 05:42 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.99, "before": 85.09, "loss": 0.0975, "playerId": 2707} |
| R342 | 05:42 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 17000, "edgeProgressPermille": 322, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.3225806451612903, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R342 | 05:42 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 80.1, "before": 80.2, "loss": 0.0975, "playerId": 2751} |
| R343 | 05:43 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 58000, "edgeProgressPermille": 566, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5669599217986315, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R343 | 05:43 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.89, "before": 84.99, "loss": 0.0975, "playerId": 2707} |
| R343 | 05:43 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 18000, "edgeProgressPermille": 341, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.3415559772296015, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R343 | 05:43 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 80.0, "before": 80.1, "loss": 0.0975, "playerId": 2751} |
| R344 | 05:44 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 19000, "edgeProgressPermille": 360, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.3605313092979127, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R344 | 05:44 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 79.9, "before": 80.0, "loss": 0.0975, "playerId": 2751} |
| R344 | 05:44 | HIGH | 果品折损 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 好果跌破阈值 80，坏果 2 |
| R344 | 05:44 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 59000, "edgeProgressPermille": 576, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5767350928641252, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R344 | 05:44 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.79, "before": 84.89, "loss": 0.0975, "playerId": 2707} |
| R345 | 05:45 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 20000, "edgeProgressPermille": 379, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.3795066413662239, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R345 | 05:45 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 79.8, "before": 79.9, "loss": 0.0975, "playerId": 2751} |
| R345 | 05:45 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 60000, "edgeProgressPermille": 586, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5865102639296188, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R345 | 05:45 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.69, "before": 84.79, "loss": 0.0975, "playerId": 2707} |
| R346 | 05:46 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 61000, "edgeProgressPermille": 596, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.5962854349951124, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R346 | 05:46 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.59, "before": 84.69, "loss": 0.0975, "playerId": 2707} |
| R346 | 05:46 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 21000, "edgeProgressPermille": 398, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.3984819734345351, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R346 | 05:46 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 79.7, "before": 79.8, "loss": 0.0975, "playerId": 2751} |
| R347 | 05:47 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 62000, "edgeProgressPermille": 606, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.6060606060606061, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R347 | 05:47 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.49, "before": 84.59, "loss": 0.0975, "playerId": 2707} |
| R347 | 05:47 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 22000, "edgeProgressPermille": 417, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.4174573055028463, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R347 | 05:47 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 79.6, "before": 79.7, "loss": 0.0975, "playerId": 2751} |
| R348 | 05:48 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 23000, "edgeProgressPermille": 436, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.4364326375711575, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R348 | 05:48 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 79.5, "before": 79.6, "loss": 0.0975, "playerId": 2751} |
| R348 | 05:48 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 63000, "edgeProgressPermille": 615, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.6158357771260997, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R348 | 05:48 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.39, "before": 84.49, "loss": 0.0975, "playerId": 2707} |
| R349 | 05:49 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 24000, "edgeProgressPermille": 455, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.45540796963946867, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R349 | 05:49 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 79.4, "before": 79.5, "loss": 0.0975, "playerId": 2751} |
| R349 | 05:49 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 64000, "edgeProgressPermille": 625, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.6256109481915934, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R349 | 05:49 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.29, "before": 84.39, "loss": 0.0975, "playerId": 2707} |
| R350 | 05:50 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 65000, "edgeProgressPermille": 635, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.635386119257087, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R350 | 05:50 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.19, "before": 84.29, "loss": 0.0975, "playerId": 2707} |
| R350 | 05:50 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 25000, "edgeProgressPermille": 474, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.47438330170777987, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R350 | 05:50 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 79.3, "before": 79.4, "loss": 0.0975, "playerId": 2751} |
| R351 | 05:51 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 66000, "edgeProgressPermille": 645, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.6451612903225806, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R351 | 05:51 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 84.09, "before": 84.19, "loss": 0.0975, "playerId": 2707} |
| R351 | 05:51 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 26000, "edgeProgressPermille": 493, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.49335863377609107, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R351 | 05:51 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 79.2, "before": 79.3, "loss": 0.0975, "playerId": 2751} |
| R352 | 05:52 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 27000, "edgeProgressPermille": 512, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.5123339658444023, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R352 | 05:52 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 79.1, "before": 79.2, "loss": 0.0975, "playerId": 2751} |
| R352 | 05:52 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 67000, "edgeProgressPermille": 654, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.6549364613880743, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R352 | 05:52 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 83.99, "before": 84.09, "loss": 0.0975, "playerId": 2707} |
| R353 | 05:53 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 28000, "edgeProgressPermille": 531, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.5313092979127134, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R353 | 05:53 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 79.0, "before": 79.1, "loss": 0.0975, "playerId": 2751} |
| R353 | 05:53 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 68000, "edgeProgressPermille": 664, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.6647116324535679, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R353 | 05:53 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 83.89, "before": 83.99, "loss": 0.0975, "playerId": 2707} |
| R354 | 05:54 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 69000, "edgeProgressPermille": 674, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.6744868035190615, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R354 | 05:54 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 83.79, "before": 83.89, "loss": 0.0975, "playerId": 2707} |
| R354 | 05:54 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 29000, "edgeProgressPermille": 550, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.5502846299810247, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R354 | 05:54 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 78.9, "before": 79.0, "loss": 0.0975, "playerId": 2751} |
| R355 | 05:55 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 70000, "edgeProgressPermille": 684, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.6842619745845552, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R355 | 05:55 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 83.69, "before": 83.79, "loss": 0.0975, "playerId": 2707} |
| R355 | 05:55 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 30000, "edgeProgressPermille": 569, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.5692599620493358, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R355 | 05:55 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 78.8, "before": 78.9, "loss": 0.0975, "playerId": 2751} |
| R356 | 05:56 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 31000, "edgeProgressPermille": 588, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.5882352941176471, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R356 | 05:56 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 78.7, "before": 78.8, "loss": 0.0975, "playerId": 2751} |
| R356 | 05:56 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 71000, "edgeProgressPermille": 694, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.6940371456500489, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R356 | 05:56 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 83.59, "before": 83.69, "loss": 0.0975, "playerId": 2707} |
| R357 | 05:57 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 32000, "edgeProgressPermille": 607, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.6072106261859582, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R357 | 05:57 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 78.6, "before": 78.7, "loss": 0.0975, "playerId": 2751} |
| R357 | 05:57 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 72000, "edgeProgressPermille": 703, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.7038123167155426, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R357 | 05:57 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 83.49, "before": 83.59, "loss": 0.0975, "playerId": 2707} |
| R358 | 05:58 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 73000, "edgeProgressPermille": 713, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.7135874877810362, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R358 | 05:58 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 83.39, "before": 83.49, "loss": 0.0975, "playerId": 2707} |
| R358 | 05:58 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 33000, "edgeProgressPermille": 626, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.6261859582542695, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R358 | 05:58 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 78.5, "before": 78.6, "loss": 0.0975, "playerId": 2751} |
| R359 | 05:59 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 74000, "edgeProgressPermille": 723, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.7233626588465298, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R359 | 05:59 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 83.29, "before": 83.39, "loss": 0.0975, "playerId": 2707} |
| R359 | 05:59 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 34000, "edgeProgressPermille": 645, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.6451612903225806, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R359 | 05:59 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 78.4, "before": 78.5, "loss": 0.0975, "playerId": 2751} |
| R360 | 06:00 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 35000, "edgeProgressPermille": 664, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.6641366223908919, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R360 | 06:00 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 78.3, "before": 78.4, "loss": 0.0975, "playerId": 2751} |
| R360 | 06:00 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 75000, "edgeProgressPermille": 733, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.7331378299120235, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R360 | 06:00 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 83.19, "before": 83.29, "loss": 0.0975, "playerId": 2707} |
| R360 | 06:00 | MED | 任务刷新 |  | T_019 刷新在 武关(S10)，路线 ROAD，截止 R540 |
| R360 | 06:00 | MED | 任务刷新 |  | T_020 刷新在 关中平原(S12)，路线 WATER，截止 R540 |
| R360 | 06:00 | MED | 任务刷新 |  | T_021 刷新在 灞桥驿(S13)，路线 MOUNTAIN，截止 R540 |
| R361 | 06:01 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 36000, "edgeProgressPermille": 683, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.683111954459203, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R361 | 06:01 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 78.2, "before": 78.3, "loss": 0.0975, "playerId": 2751} |
| R361 | 06:01 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 76000, "edgeProgressPermille": 742, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.7429130009775171, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R361 | 06:01 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 83.09, "before": 83.19, "loss": 0.0975, "playerId": 2707} |
| R362 | 06:02 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 77000, "edgeProgressPermille": 752, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.7526881720430108, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R362 | 06:02 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 82.99, "before": 83.09, "loss": 0.0975, "playerId": 2707} |
| R362 | 06:02 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 37000, "edgeProgressPermille": 702, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.7020872865275142, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R362 | 06:02 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 78.1, "before": 78.2, "loss": 0.0975, "playerId": 2751} |
| R363 | 06:03 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 78000, "edgeProgressPermille": 762, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.7624633431085044, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R363 | 06:03 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 82.89, "before": 82.99, "loss": 0.0975, "playerId": 2707} |
| R363 | 06:03 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 38000, "edgeProgressPermille": 721, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.7210626185958254, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R363 | 06:03 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 78.0, "before": 78.1, "loss": 0.0975, "playerId": 2751} |
| R364 | 06:04 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 39000, "edgeProgressPermille": 740, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.7400379506641366, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R364 | 06:04 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 77.9, "before": 78.0, "loss": 0.0975, "playerId": 2751} |
| R364 | 06:04 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 79000, "edgeProgressPermille": 772, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.772238514173998, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R364 | 06:04 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 82.79, "before": 82.89, "loss": 0.0975, "playerId": 2707} |
| R365 | 06:05 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 40000, "edgeProgressPermille": 759, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.7590132827324478, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R365 | 06:05 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 77.8, "before": 77.9, "loss": 0.0975, "playerId": 2751} |
| R365 | 06:05 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 80000, "edgeProgressPermille": 782, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.7820136852394917, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R365 | 06:05 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 82.69, "before": 82.79, "loss": 0.0975, "playerId": 2707} |
| R366 | 06:06 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 81000, "edgeProgressPermille": 791, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.7917888563049853, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R366 | 06:06 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 82.59, "before": 82.69, "loss": 0.0975, "playerId": 2707} |
| R366 | 06:06 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 41000, "edgeProgressPermille": 777, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.777988614800759, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R366 | 06:06 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 77.7, "before": 77.8, "loss": 0.0975, "playerId": 2751} |
| R367 | 06:07 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 82000, "edgeProgressPermille": 801, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.8015640273704789, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R367 | 06:07 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 82.49, "before": 82.59, "loss": 0.0975, "playerId": 2707} |
| R367 | 06:07 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 42000, "edgeProgressPermille": 796, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.7969639468690702, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R367 | 06:07 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 77.6, "before": 77.7, "loss": 0.0975, "playerId": 2751} |
| R368 | 06:08 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 43000, "edgeProgressPermille": 815, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.8159392789373814, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R368 | 06:08 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 77.5, "before": 77.6, "loss": 0.0975, "playerId": 2751} |
| R368 | 06:08 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 83000, "edgeProgressPermille": 811, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.8113391984359726, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R368 | 06:08 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 82.39, "before": 82.49, "loss": 0.0975, "playerId": 2707} |
| R369 | 06:09 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 44000, "edgeProgressPermille": 834, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.8349146110056926, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R369 | 06:09 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 77.4, "before": 77.5, "loss": 0.0975, "playerId": 2751} |
| R369 | 06:09 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 84000, "edgeProgressPermille": 821, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.8211143695014663, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R369 | 06:09 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 82.29, "before": 82.39, "loss": 0.0975, "playerId": 2707} |
| R370 | 06:10 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 85000, "edgeProgressPermille": 830, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.83088954056696, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R370 | 06:10 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 82.19, "before": 82.29, "loss": 0.0975, "playerId": 2707} |
| R370 | 06:10 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 45000, "edgeProgressPermille": 853, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.8538899430740038, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R370 | 06:10 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 77.3, "before": 77.4, "loss": 0.0975, "playerId": 2751} |
| R371 | 06:11 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 86000, "edgeProgressPermille": 840, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.8406647116324536, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R371 | 06:11 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 82.09, "before": 82.19, "loss": 0.0975, "playerId": 2707} |
| R371 | 06:11 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 46000, "edgeProgressPermille": 872, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.872865275142315, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R371 | 06:11 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 77.2, "before": 77.3, "loss": 0.0975, "playerId": 2751} |
| R372 | 06:12 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 47000, "edgeProgressPermille": 891, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.8918406072106262, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R372 | 06:12 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 77.1, "before": 77.2, "loss": 0.0975, "playerId": 2751} |
| R372 | 06:12 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 87000, "edgeProgressPermille": 850, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.8504398826979472, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R372 | 06:12 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 81.99, "before": 82.09, "loss": 0.0975, "playerId": 2707} |
| R373 | 06:13 | HIGH | 派遣 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 派遣队伍清障 荆襄大驿(S07)，预计 R378 完成 |
| R373 | 06:13 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 48000, "edgeProgressPermille": 910, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.9108159392789373, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R373 | 06:13 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 77.0, "before": 77.1, "loss": 0.0975, "playerId": 2751} |
| R373 | 06:13 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 88000, "edgeProgressPermille": 860, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.8602150537634409, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R373 | 06:13 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 81.89, "before": 81.99, "loss": 0.0975, "playerId": 2707} |
| R374 | 06:14 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 89000, "edgeProgressPermille": 869, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.8699902248289345, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R374 | 06:14 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 81.79, "before": 81.89, "loss": 0.0975, "playerId": 2707} |
| R374 | 06:14 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 49000, "edgeProgressPermille": 929, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.9297912713472486, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R374 | 06:14 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 76.9, "before": 77.0, "loss": 0.0975, "playerId": 2751} |
| R375 | 06:15 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 90000, "edgeProgressPermille": 879, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.8797653958944281, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R375 | 06:15 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 81.69, "before": 81.79, "loss": 0.0975, "playerId": 2707} |
| R375 | 06:15 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 50000, "edgeProgressPermille": 948, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.9487666034155597, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R375 | 06:15 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 76.8, "before": 76.9, "loss": 0.0975, "playerId": 2751} |
| R376 | 06:16 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 51000, "edgeProgressPermille": 967, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.967741935483871, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R376 | 06:16 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 76.7, "before": 76.8, "loss": 0.0975, "playerId": 2751} |
| R376 | 06:16 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 91000, "edgeProgressPermille": 889, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.8895405669599218, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R376 | 06:16 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 81.59, "before": 81.69, "loss": 0.0975, "playerId": 2707} |
| R377 | 06:17 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 52000, "edgeProgressPermille": 986, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 0.9867172675521821, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R377 | 06:17 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 76.6, "before": 76.7, "loss": 0.0975, "playerId": 2751} |
| R377 | 06:17 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 92000, "edgeProgressPermille": 899, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.8993157380254154, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R377 | 06:17 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 81.49, "before": 81.59, "loss": 0.0975, "playerId": 2707} |
| R378 | 06:18 | HIGH | 清障完成 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 完成 荆襄大驿(S07) 清障 |
| R378 | 06:18 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 93000, "edgeProgressPermille": 909, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.9090909090909091, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R378 | 06:18 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 81.39, "before": 81.49, "loss": 0.0975, "playerId": 2707} |
| R378 | 06:18 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 52700, "edgeProgressPermille": 1000, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2751, "progress": 1.0, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R378 | 06:18 | HIGH | 进点 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 进入 朱雀门(S14) |
| R378 | 06:18 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 76.5, "before": 76.6, "loss": 0.0975, "playerId": 2751} |
| R379 | 06:19 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 94000, "edgeProgressPermille": 918, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.9188660801564027, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R379 | 06:19 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 81.29, "before": 81.39, "loss": 0.0975, "playerId": 2707} |
| R379 | 06:19 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R379 | 06:19 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 76.43, "before": 76.5, "loss": 0.07500000000000001, "playerId": 2751} |
| R380 | 06:20 | MED | SCOUT_MARKER_EXPIRE | RED codex-py/0.1(2751) | {"playerId": 2751, "targetNodeId": "S14"} |
| R380 | 06:20 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R380 | 06:20 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 76.36, "before": 76.43, "loss": 0.07500000000000001, "playerId": 2751} |
| R380 | 06:20 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 95000, "edgeProgressPermille": 928, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.9286412512218963, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R380 | 06:20 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 81.19, "before": 81.29, "loss": 0.0975, "playerId": 2707} |
| R381 | 06:21 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R381 | 06:21 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 76.29, "before": 76.36, "loss": 0.07500000000000001, "playerId": 2751} |
| R381 | 06:21 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 96000, "edgeProgressPermille": 938, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.9384164222873901, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R381 | 06:21 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 81.09, "before": 81.19, "loss": 0.0975, "playerId": 2707} |
| R382 | 06:22 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 97000, "edgeProgressPermille": 948, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.9481915933528837, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R382 | 06:22 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 80.99, "before": 81.09, "loss": 0.0975, "playerId": 2707} |
| R382 | 06:22 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R382 | 06:22 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 76.22, "before": 76.29, "loss": 0.07500000000000001, "playerId": 2751} |
| R383 | 06:23 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 98000, "edgeProgressPermille": 957, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.9579667644183774, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R383 | 06:23 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 80.89, "before": 80.99, "loss": 0.0975, "playerId": 2707} |
| R383 | 06:23 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R383 | 06:23 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 76.15, "before": 76.22, "loss": 0.07500000000000001, "playerId": 2751} |
| R384 | 06:24 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R384 | 06:24 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 76.08, "before": 76.15, "loss": 0.07500000000000001, "playerId": 2751} |
| R384 | 06:24 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 99000, "edgeProgressPermille": 967, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.967741935483871, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R384 | 06:24 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 80.79, "before": 80.89, "loss": 0.0975, "playerId": 2707} |
| R385 | 06:25 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R385 | 06:25 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 76.01, "before": 76.08, "loss": 0.07500000000000001, "playerId": 2751} |
| R385 | 06:25 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 100000, "edgeProgressPermille": 977, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.9775171065493646, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R385 | 06:25 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 80.69, "before": 80.79, "loss": 0.0975, "playerId": 2707} |
| R386 | 06:26 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 101000, "edgeProgressPermille": 987, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.9872922776148583, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R386 | 06:26 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 80.59, "before": 80.69, "loss": 0.0975, "playerId": 2707} |
| R386 | 06:26 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R386 | 06:26 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.94, "before": 76.01, "loss": 0.07500000000000001, "playerId": 2751} |
| R387 | 06:27 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 102000, "edgeProgressPermille": 997, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 0.9970674486803519, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R387 | 06:27 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 80.49, "before": 80.59, "loss": 0.0975, "playerId": 2707} |
| R387 | 06:27 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R387 | 06:27 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.87, "before": 75.94, "loss": 0.07500000000000001, "playerId": 2751} |
| R388 | 06:28 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R388 | 06:28 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.82, "before": 75.87, "loss": 0.05, "playerId": 2751} |
| R388 | 06:28 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 102300, "edgeProgressPermille": 1000, "edgeTotalMs": 102300, "fromNodeId": "S08", "playerId": 2707, "progress": 1.0, "routeEdgeId": "E22", "toNodeId": "S09"} |
| R388 | 06:28 | HIGH | 进点 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 进入 洛阳驿(S09) |
| R388 | 06:28 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 80.43, "before": 80.49, "loss": 0.065, "playerId": 2707} |
| R389 | 06:29 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R389 | 06:29 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.77, "before": 75.82, "loss": 0.05, "playerId": 2751} |
| R389 | 06:29 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 18, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.018115942028985508, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R389 | 06:29 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 80.38, "before": 80.43, "loss": 0.055, "playerId": 2707} |
| R390 | 06:30 | HIGH | 冲刺开始 |  | 比赛进入冲刺阶段，触发回合 R390 |
| R390 | 06:30 | MED | 任务过期 |  | T_014 在 灞桥驿(S13) 过期 |
| R390 | 06:30 | MED | RUSH_TACTIC_USE | BLUE AAAA/v1.0(2707) | {"durationRound": 15, "playerId": 2707, "rushTactic": "RUSH_SPEED"} |
| R390 | 06:30 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 2300, "edgeProgressPermille": 41, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.041666666666666664, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R390 | 06:30 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 80.31, "before": 80.38, "loss": 0.06875, "playerId": 2707} |
| R390 | 06:30 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "VERIFY_GATE", "remainingRound": 5, "targetNodeId": "S14"} |
| R390 | 06:30 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.72, "before": 75.77, "loss": 0.05, "playerId": 2751} |
| R391 | 06:31 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 3600, "edgeProgressPermille": 65, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.06521739130434782, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R391 | 06:31 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 80.24, "before": 80.31, "loss": 0.06875, "playerId": 2707} |
| R391 | 06:31 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "VERIFY_GATE", "remainingRound": 4, "targetNodeId": "S14"} |
| R391 | 06:31 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.67, "before": 75.72, "loss": 0.05, "playerId": 2751} |
| R392 | 06:32 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "VERIFY_GATE", "remainingRound": 3, "targetNodeId": "S14"} |
| R392 | 06:32 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.62, "before": 75.67, "loss": 0.05, "playerId": 2751} |
| R392 | 06:32 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 4900, "edgeProgressPermille": 88, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.08876811594202899, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R392 | 06:32 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 80.17, "before": 80.24, "loss": 0.06875, "playerId": 2707} |
| R393 | 06:33 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "VERIFY_GATE", "remainingRound": 2, "targetNodeId": "S14"} |
| R393 | 06:33 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.57, "before": 75.62, "loss": 0.05, "playerId": 2751} |
| R393 | 06:33 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 6200, "edgeProgressPermille": 112, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.11231884057971014, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R393 | 06:33 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 80.1, "before": 80.17, "loss": 0.06875, "playerId": 2707} |
| R394 | 06:34 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 7500, "edgeProgressPermille": 135, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.1358695652173913, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R394 | 06:34 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 80.03, "before": 80.1, "loss": 0.06875, "playerId": 2707} |
| R394 | 06:34 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "VERIFY_GATE", "remainingRound": 1, "targetNodeId": "S14"} |
| R394 | 06:34 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.52, "before": 75.57, "loss": 0.05, "playerId": 2751} |
| R395 | 06:35 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 8800, "edgeProgressPermille": 159, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.15942028985507245, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R395 | 06:35 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 79.96, "before": 80.03, "loss": 0.06875, "playerId": 2707} |
| R395 | 06:35 | HIGH | 果品折损 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 好果跌破阈值 80，坏果 2 |
| R395 | 06:35 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "VERIFY_GATE", "remainingRound": 0, "targetNodeId": "S14"} |
| R395 | 06:35 | HIGH | 验关完成 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 通过 朱雀门(S14) 验关 |
| R395 | 06:35 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.47, "before": 75.52, "loss": 0.05, "playerId": 2751} |
| R396 | 06:36 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R396 | 06:36 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.42, "before": 75.47, "loss": 0.05, "playerId": 2751} |
| R396 | 06:36 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 10100, "edgeProgressPermille": 182, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.18297101449275363, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R396 | 06:36 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 79.89, "before": 79.96, "loss": 0.06875, "playerId": 2707} |
| R397 | 06:37 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R397 | 06:37 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.37, "before": 75.42, "loss": 0.05, "playerId": 2751} |
| R397 | 06:37 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 11400, "edgeProgressPermille": 206, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.20652173913043478, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R397 | 06:37 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 79.82, "before": 79.89, "loss": 0.06875, "playerId": 2707} |
| R398 | 06:38 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 12700, "edgeProgressPermille": 230, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.23007246376811594, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R398 | 06:38 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 79.75, "before": 79.82, "loss": 0.06875, "playerId": 2707} |
| R398 | 06:38 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R398 | 06:38 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.32, "before": 75.37, "loss": 0.05, "playerId": 2751} |
| R399 | 06:39 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 253, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.2536231884057971, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R399 | 06:39 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 79.68, "before": 79.75, "loss": 0.06875, "playerId": 2707} |
| R399 | 06:39 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R399 | 06:39 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.27, "before": 75.32, "loss": 0.05, "playerId": 2751} |
| R400 | 06:40 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R400 | 06:40 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.22, "before": 75.27, "loss": 0.05, "playerId": 2751} |
| R400 | 06:40 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 15300, "edgeProgressPermille": 277, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.27717391304347827, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R400 | 06:40 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 79.61, "before": 79.68, "loss": 0.06875, "playerId": 2707} |
| R401 | 06:41 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R401 | 06:41 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.17, "before": 75.22, "loss": 0.05, "playerId": 2751} |
| R401 | 06:41 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 16600, "edgeProgressPermille": 300, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.3007246376811594, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R401 | 06:41 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 79.54, "before": 79.61, "loss": 0.06875, "playerId": 2707} |
| R402 | 06:42 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 17900, "edgeProgressPermille": 324, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.3242753623188406, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R402 | 06:42 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 79.47, "before": 79.54, "loss": 0.06875, "playerId": 2707} |
| R402 | 06:42 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R402 | 06:42 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.12, "before": 75.17, "loss": 0.05, "playerId": 2751} |
| R403 | 06:43 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 19200, "edgeProgressPermille": 347, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.34782608695652173, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R403 | 06:43 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 79.4, "before": 79.47, "loss": 0.06875, "playerId": 2707} |
| R403 | 06:43 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R403 | 06:43 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.07, "before": 75.12, "loss": 0.05, "playerId": 2751} |
| R404 | 06:44 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R404 | 06:44 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 75.02, "before": 75.07, "loss": 0.05, "playerId": 2751} |
| R404 | 06:44 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 20500, "edgeProgressPermille": 371, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.3713768115942029, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R404 | 06:44 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 79.33, "before": 79.4, "loss": 0.06875, "playerId": 2707} |
| R405 | 06:45 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R405 | 06:45 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.97, "before": 75.02, "loss": 0.05, "playerId": 2751} |
| R405 | 06:45 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 21500, "edgeProgressPermille": 389, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.3894927536231884, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R405 | 06:45 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 79.27, "before": 79.33, "loss": 0.055, "playerId": 2707} |
| R406 | 06:46 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 22500, "edgeProgressPermille": 407, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.4076086956521739, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R406 | 06:46 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 79.21, "before": 79.27, "loss": 0.055, "playerId": 2707} |
| R406 | 06:46 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R406 | 06:46 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.92, "before": 74.97, "loss": 0.05, "playerId": 2751} |
| R407 | 06:47 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 23500, "edgeProgressPermille": 425, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.4257246376811594, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R407 | 06:47 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 79.15, "before": 79.21, "loss": 0.055, "playerId": 2707} |
| R407 | 06:47 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R407 | 06:47 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.87, "before": 74.92, "loss": 0.05, "playerId": 2751} |
| R408 | 06:48 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R408 | 06:48 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.82, "before": 74.87, "loss": 0.05, "playerId": 2751} |
| R408 | 06:48 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 24500, "edgeProgressPermille": 443, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.4438405797101449, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R408 | 06:48 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 79.1, "before": 79.15, "loss": 0.055, "playerId": 2707} |
| R409 | 06:49 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R409 | 06:49 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.77, "before": 74.82, "loss": 0.05, "playerId": 2751} |
| R409 | 06:49 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 25500, "edgeProgressPermille": 461, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.46195652173913043, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R409 | 06:49 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 79.04, "before": 79.1, "loss": 0.055, "playerId": 2707} |
| R410 | 06:50 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 26500, "edgeProgressPermille": 480, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.48007246376811596, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R410 | 06:50 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.99, "before": 79.04, "loss": 0.055, "playerId": 2707} |
| R410 | 06:50 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R410 | 06:50 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.72, "before": 74.77, "loss": 0.05, "playerId": 2751} |
| R411 | 06:51 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 27500, "edgeProgressPermille": 498, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.49818840579710144, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R411 | 06:51 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.93, "before": 78.99, "loss": 0.055, "playerId": 2707} |
| R411 | 06:51 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R411 | 06:51 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.67, "before": 74.72, "loss": 0.05, "playerId": 2751} |
| R412 | 06:52 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R412 | 06:52 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.62, "before": 74.67, "loss": 0.05, "playerId": 2751} |
| R412 | 06:52 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 28500, "edgeProgressPermille": 516, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.5163043478260869, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R412 | 06:52 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.88, "before": 78.93, "loss": 0.055, "playerId": 2707} |
| R413 | 06:53 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R413 | 06:53 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.57, "before": 74.62, "loss": 0.05, "playerId": 2751} |
| R413 | 06:53 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 29500, "edgeProgressPermille": 534, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.5344202898550725, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R413 | 06:53 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.82, "before": 78.88, "loss": 0.055, "playerId": 2707} |
| R414 | 06:54 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 30500, "edgeProgressPermille": 552, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.552536231884058, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R414 | 06:54 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.76, "before": 78.82, "loss": 0.055, "playerId": 2707} |
| R414 | 06:54 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R414 | 06:54 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.52, "before": 74.57, "loss": 0.05, "playerId": 2751} |
| R415 | 06:55 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 31500, "edgeProgressPermille": 570, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.5706521739130435, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R415 | 06:55 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.71, "before": 78.76, "loss": 0.055, "playerId": 2707} |
| R415 | 06:55 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R415 | 06:55 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.47, "before": 74.52, "loss": 0.05, "playerId": 2751} |
| R416 | 06:56 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R416 | 06:56 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.42, "before": 74.47, "loss": 0.05, "playerId": 2751} |
| R416 | 06:56 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 32500, "edgeProgressPermille": 588, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.5887681159420289, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R416 | 06:56 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.65, "before": 78.71, "loss": 0.055, "playerId": 2707} |
| R417 | 06:57 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R417 | 06:57 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.37, "before": 74.42, "loss": 0.05, "playerId": 2751} |
| R417 | 06:57 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 33500, "edgeProgressPermille": 606, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.6068840579710145, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R417 | 06:57 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.6, "before": 78.65, "loss": 0.055, "playerId": 2707} |
| R418 | 06:58 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 34500, "edgeProgressPermille": 625, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.625, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R418 | 06:58 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.54, "before": 78.6, "loss": 0.055, "playerId": 2707} |
| R418 | 06:58 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R418 | 06:58 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.32, "before": 74.37, "loss": 0.05, "playerId": 2751} |
| R419 | 06:59 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 35500, "edgeProgressPermille": 643, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.6431159420289855, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R419 | 06:59 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.49, "before": 78.54, "loss": 0.055, "playerId": 2707} |
| R419 | 06:59 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R419 | 06:59 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.27, "before": 74.32, "loss": 0.05, "playerId": 2751} |
| R420 | 07:00 | MED | 任务过期 |  | T_012 在 荆襄大驿(S07) 过期 |
| R420 | 07:00 | MED | 任务过期 |  | T_013 在 武关(S10) 过期 |
| R420 | 07:00 | MED | 任务过期 |  | T_015 在 灞桥驿(S13) 过期 |
| R420 | 07:00 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R420 | 07:00 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.22, "before": 74.27, "loss": 0.05, "playerId": 2751} |
| R420 | 07:00 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 36500, "edgeProgressPermille": 661, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.6612318840579711, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R420 | 07:00 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.43, "before": 78.49, "loss": 0.055, "playerId": 2707} |
| R421 | 07:01 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R421 | 07:01 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.17, "before": 74.22, "loss": 0.05, "playerId": 2751} |
| R421 | 07:01 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 37500, "edgeProgressPermille": 679, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.6793478260869565, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R421 | 07:01 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.38, "before": 78.43, "loss": 0.055, "playerId": 2707} |
| R422 | 07:02 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 38500, "edgeProgressPermille": 697, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.697463768115942, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R422 | 07:02 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.32, "before": 78.38, "loss": 0.055, "playerId": 2707} |
| R422 | 07:02 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R422 | 07:02 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.12, "before": 74.17, "loss": 0.05, "playerId": 2751} |
| R423 | 07:03 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 39500, "edgeProgressPermille": 715, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.7155797101449275, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R423 | 07:03 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.26, "before": 78.32, "loss": 0.055, "playerId": 2707} |
| R423 | 07:03 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R423 | 07:03 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.07, "before": 74.12, "loss": 0.05, "playerId": 2751} |
| R424 | 07:04 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R424 | 07:04 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 74.02, "before": 74.07, "loss": 0.05, "playerId": 2751} |
| R424 | 07:04 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 40500, "edgeProgressPermille": 733, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.7336956521739131, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R424 | 07:04 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.21, "before": 78.26, "loss": 0.055, "playerId": 2707} |
| R425 | 07:05 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R425 | 07:05 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.97, "before": 74.02, "loss": 0.05, "playerId": 2751} |
| R425 | 07:05 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 41500, "edgeProgressPermille": 751, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.7518115942028986, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R425 | 07:05 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.15, "before": 78.21, "loss": 0.055, "playerId": 2707} |
| R426 | 07:06 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 42500, "edgeProgressPermille": 769, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.769927536231884, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R426 | 07:06 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.1, "before": 78.15, "loss": 0.055, "playerId": 2707} |
| R426 | 07:06 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R426 | 07:06 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.92, "before": 73.97, "loss": 0.05, "playerId": 2751} |
| R427 | 07:07 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 43500, "edgeProgressPermille": 788, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.7880434782608695, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R427 | 07:07 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 78.04, "before": 78.1, "loss": 0.055, "playerId": 2707} |
| R427 | 07:07 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R427 | 07:07 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.87, "before": 73.92, "loss": 0.05, "playerId": 2751} |
| R428 | 07:08 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R428 | 07:08 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.82, "before": 73.87, "loss": 0.05, "playerId": 2751} |
| R428 | 07:08 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 44500, "edgeProgressPermille": 806, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.8061594202898551, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R428 | 07:08 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.99, "before": 78.04, "loss": 0.055, "playerId": 2707} |
| R429 | 07:09 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R429 | 07:09 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.77, "before": 73.82, "loss": 0.05, "playerId": 2751} |
| R429 | 07:09 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 45500, "edgeProgressPermille": 824, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.8242753623188406, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R429 | 07:09 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.93, "before": 77.99, "loss": 0.055, "playerId": 2707} |
| R430 | 07:10 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 46500, "edgeProgressPermille": 842, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.842391304347826, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R430 | 07:10 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.88, "before": 77.93, "loss": 0.055, "playerId": 2707} |
| R430 | 07:10 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R430 | 07:10 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.72, "before": 73.77, "loss": 0.05, "playerId": 2751} |
| R431 | 07:11 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 47500, "edgeProgressPermille": 860, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.8605072463768116, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R431 | 07:11 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.82, "before": 77.88, "loss": 0.055, "playerId": 2707} |
| R431 | 07:11 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R431 | 07:11 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.67, "before": 73.72, "loss": 0.05, "playerId": 2751} |
| R432 | 07:12 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R432 | 07:12 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.62, "before": 73.67, "loss": 0.05, "playerId": 2751} |
| R432 | 07:12 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 48500, "edgeProgressPermille": 878, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.8786231884057971, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R432 | 07:12 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.76, "before": 77.82, "loss": 0.055, "playerId": 2707} |
| R433 | 07:13 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R433 | 07:13 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.57, "before": 73.62, "loss": 0.05, "playerId": 2751} |
| R433 | 07:13 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 49500, "edgeProgressPermille": 896, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.8967391304347826, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R433 | 07:13 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.71, "before": 77.76, "loss": 0.055, "playerId": 2707} |
| R434 | 07:14 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 50500, "edgeProgressPermille": 914, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.9148550724637681, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R434 | 07:14 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.65, "before": 77.71, "loss": 0.055, "playerId": 2707} |
| R434 | 07:14 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R434 | 07:14 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.52, "before": 73.57, "loss": 0.05, "playerId": 2751} |
| R435 | 07:15 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 51500, "edgeProgressPermille": 932, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.9329710144927537, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R435 | 07:15 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.6, "before": 77.65, "loss": 0.055, "playerId": 2707} |
| R435 | 07:15 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R435 | 07:15 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.47, "before": 73.52, "loss": 0.05, "playerId": 2751} |
| R436 | 07:16 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R436 | 07:16 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.42, "before": 73.47, "loss": 0.05, "playerId": 2751} |
| R436 | 07:16 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 52500, "edgeProgressPermille": 951, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.9510869565217391, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R436 | 07:16 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.54, "before": 77.6, "loss": 0.055, "playerId": 2707} |
| R437 | 07:17 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R437 | 07:17 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.37, "before": 73.42, "loss": 0.05, "playerId": 2751} |
| R437 | 07:17 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 53500, "edgeProgressPermille": 969, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.9692028985507246, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R437 | 07:17 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.49, "before": 77.54, "loss": 0.055, "playerId": 2707} |
| R438 | 07:18 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 54500, "edgeProgressPermille": 987, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 0.9873188405797102, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R438 | 07:18 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.43, "before": 77.49, "loss": 0.055, "playerId": 2707} |
| R438 | 07:18 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R438 | 07:18 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.32, "before": 73.37, "loss": 0.05, "playerId": 2751} |
| R439 | 07:19 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 55200, "edgeProgressPermille": 1000, "edgeTotalMs": 55200, "fromNodeId": "S09", "playerId": 2707, "progress": 1.0, "routeEdgeId": "E05", "toNodeId": "S10"} |
| R439 | 07:19 | HIGH | 进点 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 进入 武关(S10) |
| R439 | 07:19 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.38, "before": 77.43, "loss": 0.055, "playerId": 2707} |
| R439 | 07:19 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R439 | 07:19 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.27, "before": 73.32, "loss": 0.05, "playerId": 2751} |
| R440 | 07:20 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R440 | 07:20 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.22, "before": 73.27, "loss": 0.05, "playerId": 2751} |
| R440 | 07:20 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 3, "targetNodeId": "S10"} |
| R440 | 07:20 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.33, "before": 77.38, "loss": 0.05, "playerId": 2707} |
| R441 | 07:21 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R441 | 07:21 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.17, "before": 73.22, "loss": 0.05, "playerId": 2751} |
| R441 | 07:21 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 2, "targetNodeId": "S10"} |
| R441 | 07:21 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.28, "before": 77.33, "loss": 0.05, "playerId": 2707} |
| R442 | 07:22 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 1, "targetNodeId": "S10"} |
| R442 | 07:22 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.23, "before": 77.28, "loss": 0.05, "playerId": 2707} |
| R442 | 07:22 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R442 | 07:22 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.12, "before": 73.17, "loss": 0.05, "playerId": 2751} |
| R443 | 07:23 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 0, "targetNodeId": "S10"} |
| R443 | 07:23 | HIGH | 任务完成 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 完成 抵驿催运，+30 分，任务分 90 |
| R443 | 07:23 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.18, "before": 77.23, "loss": 0.05, "playerId": 2707} |
| R443 | 07:23 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R443 | 07:23 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.07, "before": 73.12, "loss": 0.05, "playerId": 2751} |
| R444 | 07:24 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R444 | 07:24 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 73.02, "before": 73.07, "loss": 0.05, "playerId": 2751} |
| R444 | 07:24 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 25, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.025879917184265012, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R444 | 07:24 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.13, "before": 77.18, "loss": 0.055, "playerId": 2707} |
| R445 | 07:25 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R445 | 07:25 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.97, "before": 73.02, "loss": 0.05, "playerId": 2751} |
| R445 | 07:25 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 51, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.051759834368530024, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R445 | 07:25 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.07, "before": 77.13, "loss": 0.055, "playerId": 2707} |
| R446 | 07:26 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 77, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.07763975155279502, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R446 | 07:26 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 77.01, "before": 77.07, "loss": 0.055, "playerId": 2707} |
| R446 | 07:26 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R446 | 07:26 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.92, "before": 72.97, "loss": 0.05, "playerId": 2751} |
| R447 | 07:27 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 103, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.10351966873706005, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R447 | 07:27 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.96, "before": 77.01, "loss": 0.055, "playerId": 2707} |
| R447 | 07:27 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R447 | 07:27 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.87, "before": 72.92, "loss": 0.05, "playerId": 2751} |
| R448 | 07:28 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R448 | 07:28 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.82, "before": 72.87, "loss": 0.05, "playerId": 2751} |
| R448 | 07:28 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 129, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.12939958592132506, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R448 | 07:28 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.9, "before": 76.96, "loss": 0.055, "playerId": 2707} |
| R449 | 07:29 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R449 | 07:29 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.77, "before": 72.82, "loss": 0.05, "playerId": 2751} |
| R449 | 07:29 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 155, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.15527950310559005, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R449 | 07:29 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.85, "before": 76.9, "loss": 0.055, "playerId": 2707} |
| R450 | 07:30 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 181, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.18115942028985507, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R450 | 07:30 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.79, "before": 76.85, "loss": 0.055, "playerId": 2707} |
| R450 | 07:30 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R450 | 07:30 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.72, "before": 72.77, "loss": 0.05, "playerId": 2751} |
| R451 | 07:31 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 207, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.2070393374741201, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R451 | 07:31 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.74, "before": 76.79, "loss": 0.055, "playerId": 2707} |
| R451 | 07:31 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R451 | 07:31 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.67, "before": 72.72, "loss": 0.05, "playerId": 2751} |
| R452 | 07:32 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R452 | 07:32 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.62, "before": 72.67, "loss": 0.05, "playerId": 2751} |
| R452 | 07:32 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 232, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.2329192546583851, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R452 | 07:32 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.68, "before": 76.74, "loss": 0.055, "playerId": 2707} |
| R453 | 07:33 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R453 | 07:33 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.57, "before": 72.62, "loss": 0.05, "playerId": 2751} |
| R453 | 07:33 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 258, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.2587991718426501, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R453 | 07:33 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.63, "before": 76.68, "loss": 0.055, "playerId": 2707} |
| R454 | 07:34 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 284, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.28467908902691513, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R454 | 07:34 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.57, "before": 76.63, "loss": 0.055, "playerId": 2707} |
| R454 | 07:34 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R454 | 07:34 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.52, "before": 72.57, "loss": 0.05, "playerId": 2751} |
| R455 | 07:35 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 12000, "edgeProgressPermille": 310, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.3105590062111801, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R455 | 07:35 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.51, "before": 76.57, "loss": 0.055, "playerId": 2707} |
| R455 | 07:35 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R455 | 07:35 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.47, "before": 72.52, "loss": 0.05, "playerId": 2751} |
| R456 | 07:36 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R456 | 07:36 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.42, "before": 72.47, "loss": 0.05, "playerId": 2751} |
| R456 | 07:36 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 13000, "edgeProgressPermille": 336, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.3364389233954451, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R456 | 07:36 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.46, "before": 76.51, "loss": 0.055, "playerId": 2707} |
| R457 | 07:37 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R457 | 07:37 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.37, "before": 72.42, "loss": 0.05, "playerId": 2751} |
| R457 | 07:37 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 362, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.36231884057971014, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R457 | 07:37 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.4, "before": 76.46, "loss": 0.055, "playerId": 2707} |
| R458 | 07:38 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 15000, "edgeProgressPermille": 388, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.38819875776397517, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R458 | 07:38 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.35, "before": 76.4, "loss": 0.055, "playerId": 2707} |
| R458 | 07:38 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R458 | 07:38 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.32, "before": 72.37, "loss": 0.05, "playerId": 2751} |
| R459 | 07:39 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 16000, "edgeProgressPermille": 414, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.4140786749482402, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R459 | 07:39 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.29, "before": 76.35, "loss": 0.055, "playerId": 2707} |
| R459 | 07:39 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R459 | 07:39 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.27, "before": 72.32, "loss": 0.05, "playerId": 2751} |
| R460 | 07:40 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R460 | 07:40 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.22, "before": 72.27, "loss": 0.05, "playerId": 2751} |
| R460 | 07:40 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 17000, "edgeProgressPermille": 439, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.43995859213250516, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R460 | 07:40 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.24, "before": 76.29, "loss": 0.055, "playerId": 2707} |
| R461 | 07:41 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R461 | 07:41 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.17, "before": 72.22, "loss": 0.05, "playerId": 2751} |
| R461 | 07:41 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 18000, "edgeProgressPermille": 465, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.4658385093167702, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R461 | 07:41 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.18, "before": 76.24, "loss": 0.055, "playerId": 2707} |
| R462 | 07:42 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 19000, "edgeProgressPermille": 491, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.4917184265010352, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R462 | 07:42 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.13, "before": 76.18, "loss": 0.055, "playerId": 2707} |
| R462 | 07:42 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R462 | 07:42 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.12, "before": 72.17, "loss": 0.05, "playerId": 2751} |
| R463 | 07:43 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 20000, "edgeProgressPermille": 517, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.5175983436853002, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R463 | 07:43 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.07, "before": 76.13, "loss": 0.055, "playerId": 2707} |
| R463 | 07:43 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R463 | 07:43 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.07, "before": 72.12, "loss": 0.05, "playerId": 2751} |
| R464 | 07:44 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R464 | 07:44 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 72.02, "before": 72.07, "loss": 0.05, "playerId": 2751} |
| R464 | 07:44 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 21000, "edgeProgressPermille": 543, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.5434782608695652, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R464 | 07:44 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 76.01, "before": 76.07, "loss": 0.055, "playerId": 2707} |
| R465 | 07:45 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R465 | 07:45 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.97, "before": 72.02, "loss": 0.05, "playerId": 2751} |
| R465 | 07:45 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 22000, "edgeProgressPermille": 569, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.5693581780538303, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R465 | 07:45 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.96, "before": 76.01, "loss": 0.055, "playerId": 2707} |
| R466 | 07:46 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 23000, "edgeProgressPermille": 595, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.5952380952380952, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R466 | 07:46 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.9, "before": 75.96, "loss": 0.055, "playerId": 2707} |
| R466 | 07:46 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R466 | 07:46 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.92, "before": 71.97, "loss": 0.05, "playerId": 2751} |
| R467 | 07:47 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 24000, "edgeProgressPermille": 621, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.6211180124223602, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R467 | 07:47 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.85, "before": 75.9, "loss": 0.055, "playerId": 2707} |
| R467 | 07:47 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R467 | 07:47 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.87, "before": 71.92, "loss": 0.05, "playerId": 2751} |
| R468 | 07:48 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R468 | 07:48 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.82, "before": 71.87, "loss": 0.05, "playerId": 2751} |
| R468 | 07:48 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 25000, "edgeProgressPermille": 646, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.6469979296066253, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R468 | 07:48 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.79, "before": 75.85, "loss": 0.055, "playerId": 2707} |
| R469 | 07:49 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R469 | 07:49 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.77, "before": 71.82, "loss": 0.05, "playerId": 2751} |
| R469 | 07:49 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 26000, "edgeProgressPermille": 672, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.6728778467908902, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R469 | 07:49 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.74, "before": 75.79, "loss": 0.055, "playerId": 2707} |
| R470 | 07:50 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 27000, "edgeProgressPermille": 698, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.6987577639751553, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R470 | 07:50 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.68, "before": 75.74, "loss": 0.055, "playerId": 2707} |
| R470 | 07:50 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R470 | 07:50 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.72, "before": 71.77, "loss": 0.05, "playerId": 2751} |
| R471 | 07:51 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 28000, "edgeProgressPermille": 724, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.7246376811594203, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R471 | 07:51 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.63, "before": 75.68, "loss": 0.055, "playerId": 2707} |
| R471 | 07:51 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R471 | 07:51 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.67, "before": 71.72, "loss": 0.05, "playerId": 2751} |
| R472 | 07:52 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R472 | 07:52 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.62, "before": 71.67, "loss": 0.05, "playerId": 2751} |
| R472 | 07:52 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 29000, "edgeProgressPermille": 750, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.7505175983436853, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R472 | 07:52 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.57, "before": 75.63, "loss": 0.055, "playerId": 2707} |
| R473 | 07:53 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R473 | 07:53 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.57, "before": 71.62, "loss": 0.05, "playerId": 2751} |
| R473 | 07:53 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 30000, "edgeProgressPermille": 776, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.7763975155279503, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R473 | 07:53 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.51, "before": 75.57, "loss": 0.055, "playerId": 2707} |
| R474 | 07:54 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 31000, "edgeProgressPermille": 802, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.8022774327122153, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R474 | 07:54 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.46, "before": 75.51, "loss": 0.055, "playerId": 2707} |
| R474 | 07:54 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R474 | 07:54 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.52, "before": 71.57, "loss": 0.05, "playerId": 2751} |
| R475 | 07:55 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 32000, "edgeProgressPermille": 828, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.8281573498964804, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R475 | 07:55 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.4, "before": 75.46, "loss": 0.055, "playerId": 2707} |
| R475 | 07:55 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R475 | 07:55 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.47, "before": 71.52, "loss": 0.05, "playerId": 2751} |
| R476 | 07:56 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R476 | 07:56 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.42, "before": 71.47, "loss": 0.05, "playerId": 2751} |
| R476 | 07:56 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 33000, "edgeProgressPermille": 854, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.8540372670807453, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R476 | 07:56 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.35, "before": 75.4, "loss": 0.055, "playerId": 2707} |
| R477 | 07:57 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R477 | 07:57 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.37, "before": 71.42, "loss": 0.05, "playerId": 2751} |
| R477 | 07:57 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 34000, "edgeProgressPermille": 879, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.8799171842650103, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R477 | 07:57 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.29, "before": 75.35, "loss": 0.055, "playerId": 2707} |
| R478 | 07:58 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 35000, "edgeProgressPermille": 905, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.9057971014492754, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R478 | 07:58 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.24, "before": 75.29, "loss": 0.055, "playerId": 2707} |
| R478 | 07:58 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R478 | 07:58 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.32, "before": 71.37, "loss": 0.05, "playerId": 2751} |
| R479 | 07:59 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 36000, "edgeProgressPermille": 931, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.9316770186335404, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R479 | 07:59 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.18, "before": 75.24, "loss": 0.055, "playerId": 2707} |
| R479 | 07:59 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R479 | 07:59 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.27, "before": 71.32, "loss": 0.05, "playerId": 2751} |
| R480 | 08:00 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R480 | 08:00 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.22, "before": 71.27, "loss": 0.05, "playerId": 2751} |
| R480 | 08:00 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 37000, "edgeProgressPermille": 957, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.9575569358178054, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R480 | 08:00 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.13, "before": 75.18, "loss": 0.055, "playerId": 2707} |
| R481 | 08:01 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R481 | 08:01 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.17, "before": 71.22, "loss": 0.05, "playerId": 2751} |
| R481 | 08:01 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 38000, "edgeProgressPermille": 983, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 0.9834368530020704, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R481 | 08:01 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.07, "before": 75.13, "loss": 0.055, "playerId": 2707} |
| R482 | 08:02 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 38640, "edgeProgressPermille": 1000, "edgeTotalMs": 38640, "fromNodeId": "S10", "playerId": 2707, "progress": 1.0, "routeEdgeId": "E06", "toNodeId": "S11"} |
| R482 | 08:02 | HIGH | 进点 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 进入 潼关驿(S11) |
| R482 | 08:02 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 75.01, "before": 75.07, "loss": 0.055, "playerId": 2707} |
| R482 | 08:02 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R482 | 08:02 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.12, "before": 71.17, "loss": 0.05, "playerId": 2751} |
| R483 | 08:03 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "PASS_TRANSFER", "remainingRound": 3, "targetNodeId": "S11"} |
| R483 | 08:03 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.96, "before": 75.01, "loss": 0.05, "playerId": 2707} |
| R483 | 08:03 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R483 | 08:03 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.07, "before": 71.12, "loss": 0.05, "playerId": 2751} |
| R484 | 08:04 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R484 | 08:04 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 71.02, "before": 71.07, "loss": 0.05, "playerId": 2751} |
| R484 | 08:04 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "PASS_TRANSFER", "remainingRound": 2, "targetNodeId": "S11"} |
| R484 | 08:04 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.91, "before": 74.96, "loss": 0.05, "playerId": 2707} |
| R485 | 08:05 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R485 | 08:05 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 70.97, "before": 71.02, "loss": 0.05, "playerId": 2751} |
| R485 | 08:05 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "PASS_TRANSFER", "remainingRound": 1, "targetNodeId": "S11"} |
| R485 | 08:05 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.86, "before": 74.91, "loss": 0.05, "playerId": 2707} |
| R486 | 08:06 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "PASS_TRANSFER", "remainingRound": 0, "targetNodeId": "S11"} |
| R486 | 08:06 | MED | 处理完成 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 在 潼关驿(S11) 完成关口转运 |
| R486 | 08:06 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.81, "before": 74.86, "loss": 0.05, "playerId": 2707} |
| R486 | 08:06 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R486 | 08:06 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 70.92, "before": 70.97, "loss": 0.05, "playerId": 2751} |
| R487 | 08:07 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 18, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2707, "progress": 0.018975332068311195, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R487 | 08:07 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.75, "before": 74.81, "loss": 0.065, "playerId": 2707} |
| R487 | 08:07 | MED | WAIT | RED codex-py/0.1(2751) | {"nodeId": "S14", "playerId": 2751} |
| R487 | 08:07 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 70.87, "before": 70.92, "loss": 0.05, "playerId": 2751} |
| R488 | 08:08 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "SET_GUARD", "remainingRound": 3, "targetNodeId": "S14"} |
| R488 | 08:08 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 70.82, "before": 70.87, "loss": 0.05, "playerId": 2751} |
| R488 | 08:08 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 37, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2707, "progress": 0.03795066413662239, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R488 | 08:08 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.69, "before": 74.75, "loss": 0.065, "playerId": 2707} |
| R489 | 08:09 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "SET_GUARD", "remainingRound": 2, "targetNodeId": "S14"} |
| R489 | 08:09 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 70.77, "before": 70.82, "loss": 0.05, "playerId": 2751} |
| R489 | 08:09 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 56, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2707, "progress": 0.056925996204933584, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R489 | 08:09 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.63, "before": 74.69, "loss": 0.065, "playerId": 2707} |
| R490 | 08:10 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 75, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2707, "progress": 0.07590132827324478, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R490 | 08:10 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.57, "before": 74.63, "loss": 0.065, "playerId": 2707} |
| R490 | 08:10 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "SET_GUARD", "remainingRound": 1, "targetNodeId": "S14"} |
| R490 | 08:10 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 70.72, "before": 70.77, "loss": 0.05, "playerId": 2751} |
| R491 | 08:11 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 94, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2707, "progress": 0.09487666034155598, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R491 | 08:11 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.51, "before": 74.57, "loss": 0.065, "playerId": 2707} |
| R491 | 08:11 | MED | PROCESS_PROGRESS | RED codex-py/0.1(2751) | {"playerId": 2751, "processType": "SET_GUARD", "remainingRound": 0, "targetNodeId": "S14"} |
| R491 | 08:11 | HIGH | 设卡完成 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 在 朱雀门(S14) 完成设卡，防守值 4 |
| R491 | 08:11 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 70.67, "before": 70.72, "loss": 0.05, "playerId": 2751} |
| R492 | 08:12 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 1000, "edgeProgressPermille": 362, "edgeTotalMs": 2760, "fromNodeId": "S14", "playerId": 2751, "progress": 0.36231884057971014, "routeEdgeId": "E10", "toNodeId": "S15"} |
| R492 | 08:12 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 70.62, "before": 70.67, "loss": 0.055, "playerId": 2751} |
| R492 | 08:12 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 55, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.055741360089186176, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R492 | 08:12 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.46, "before": 74.51, "loss": 0.055, "playerId": 2707} |
| R493 | 08:13 | MED | RUSH_TACTIC_USE | RED codex-py/0.1(2751) | {"durationRound": 15, "playerId": 2751, "rushTactic": "RUSH_SPEED"} |
| R493 | 08:13 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 2300, "edgeProgressPermille": 833, "edgeTotalMs": 2760, "fromNodeId": "S14", "playerId": 2751, "progress": 0.8333333333333334, "routeEdgeId": "E10", "toNodeId": "S15"} |
| R493 | 08:13 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 70.55, "before": 70.62, "loss": 0.06875, "playerId": 2751} |
| R493 | 08:13 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 111, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.11148272017837235, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R493 | 08:13 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.4, "before": 74.46, "loss": 0.055, "playerId": 2707} |
| R494 | 08:14 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 167, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.16722408026755853, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R494 | 08:14 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.35, "before": 74.4, "loss": 0.055, "playerId": 2707} |
| R494 | 08:14 | MED | MOVE_PROGRESS | RED codex-py/0.1(2751) | {"edgeProgressMs": 2760, "edgeProgressPermille": 1000, "edgeTotalMs": 2760, "fromNodeId": "S14", "playerId": 2751, "progress": 1.0, "routeEdgeId": "E10", "toNodeId": "S15"} |
| R494 | 08:14 | HIGH | 进点 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 进入 兴庆宫(S15) |
| R494 | 08:14 | MED | FRESHNESS_DROP | RED codex-py/0.1(2751) | {"after": 70.48, "before": 70.55, "loss": 0.06875, "playerId": 2751} |
| R495 | 08:15 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 222, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.2229654403567447, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R495 | 08:15 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.29, "before": 74.35, "loss": 0.055, "playerId": 2707} |
| R495 | 08:15 | HIGH | 送达成功 | RED codex-py/0.1(2751) | RED codex-py/0.1(2751) 成功送达，好果 94，新鲜度 70.48，总分 578 |
| R496 | 08:16 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 278, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.2787068004459309, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R496 | 08:16 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.24, "before": 74.29, "loss": 0.055, "playerId": 2707} |
| R497 | 08:17 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 334, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.33444816053511706, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R497 | 08:17 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.18, "before": 74.24, "loss": 0.055, "playerId": 2707} |
| R498 | 08:18 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 390, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.39018952062430323, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R498 | 08:18 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.13, "before": 74.18, "loss": 0.055, "playerId": 2707} |
| R499 | 08:19 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 445, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.4459308807134894, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R499 | 08:19 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.07, "before": 74.13, "loss": 0.055, "playerId": 2707} |
| R500 | 08:20 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 501, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.5016722408026756, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R500 | 08:20 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 74.01, "before": 74.07, "loss": 0.055, "playerId": 2707} |
| R501 | 08:21 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 557, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.5574136008918618, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R501 | 08:21 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.96, "before": 74.01, "loss": 0.055, "playerId": 2707} |
| R502 | 08:22 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 613, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.6131549609810479, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R502 | 08:22 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.9, "before": 73.96, "loss": 0.055, "playerId": 2707} |
| R503 | 08:23 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 12000, "edgeProgressPermille": 668, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.6688963210702341, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R503 | 08:23 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.85, "before": 73.9, "loss": 0.055, "playerId": 2707} |
| R504 | 08:24 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 13000, "edgeProgressPermille": 724, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.7246376811594203, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R504 | 08:24 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.79, "before": 73.85, "loss": 0.055, "playerId": 2707} |
| R505 | 08:25 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 780, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.7803790412486065, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R505 | 08:25 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.74, "before": 73.79, "loss": 0.055, "playerId": 2707} |
| R506 | 08:26 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 15000, "edgeProgressPermille": 836, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.8361204013377926, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R506 | 08:26 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.68, "before": 73.74, "loss": 0.055, "playerId": 2707} |
| R507 | 08:27 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 16000, "edgeProgressPermille": 891, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.8918617614269788, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R507 | 08:27 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.63, "before": 73.68, "loss": 0.055, "playerId": 2707} |
| R508 | 08:28 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 17000, "edgeProgressPermille": 947, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 0.947603121516165, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R508 | 08:28 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.57, "before": 73.63, "loss": 0.055, "playerId": 2707} |
| R509 | 08:29 | MED | MOVE_PROGRESS | BLUE AAAA/v1.0(2707) | {"edgeProgressMs": 17940, "edgeProgressPermille": 1000, "edgeTotalMs": 17940, "fromNodeId": "S11", "playerId": 2707, "progress": 1.0, "routeEdgeId": "E07", "toNodeId": "S12"} |
| R509 | 08:29 | HIGH | 进点 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 进入 关中平原(S12) |
| R509 | 08:29 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.51, "before": 73.57, "loss": 0.055, "playerId": 2707} |
| R510 | 08:30 | HIGH | 窗口争夺开始 |  | 朱雀门(S14) 开启PASS争夺，目标  |
| R510 | 08:30 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.46, "before": 73.51, "loss": 0.05, "playerId": 2707} |
| R511 | 08:31 | MED | 争夺亮牌 |  | 第 1 轮亮牌：红 ABSTAIN / 蓝 BING_ZHENG，结果 BLUE |
| R511 | 08:31 | HIGH | 窗口争夺开始 |  | 朱雀门(S14) 开启PASS争夺，目标  |
| R511 | 08:31 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.41, "before": 73.46, "loss": 0.05, "playerId": 2707} |
| R512 | 08:32 | MED | 争夺亮牌 |  | 第 2 轮亮牌：红 ABSTAIN / 蓝 BING_ZHENG，结果 BLUE |
| R512 | 08:32 | MED | 争夺亮牌 |  | 第 1 轮亮牌：红 ABSTAIN / 蓝 ABSTAIN，结果 DRAW |
| R512 | 08:32 | HIGH | 窗口争夺开始 |  | 朱雀门(S14) 开启PASS争夺，目标  |
| R512 | 08:32 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.36, "before": 73.41, "loss": 0.05, "playerId": 2707} |
| R513 | 08:33 | MED | 争夺亮牌 |  | 第 3 轮亮牌：红 ABSTAIN / 蓝 ABSTAIN，结果 DRAW |
| R513 | 08:33 | HIGH | 强通争夺胜出 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 赢下 朱雀门(S14) 的强制通行争夺 |
| R513 | 08:33 | HIGH | 窗口争夺结束 |  | 争夺结束，胜方 BLUE，红蓝消耗 0/2 |
| R513 | 08:33 | MED | 争夺亮牌 |  | 第 2 轮亮牌：红 ABSTAIN / 蓝 ABSTAIN，结果 DRAW |
| R513 | 08:33 | MED | 争夺亮牌 |  | 第 1 轮亮牌：红 ABSTAIN / 蓝 ABSTAIN，结果 DRAW |
| R513 | 08:33 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.31, "before": 73.36, "loss": 0.05, "playerId": 2707} |
| R514 | 08:34 | MED | 争夺亮牌 |  | 第 3 轮亮牌：红 ABSTAIN / 蓝 BING_ZHENG，结果 BLUE |
| R514 | 08:34 | HIGH | 强通争夺胜出 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 赢下 朱雀门(S14) 的强制通行争夺 |
| R514 | 08:34 | HIGH | 窗口争夺结束 |  | 争夺结束，胜方 BLUE，红蓝消耗 0/1 |
| R514 | 08:34 | MED | 争夺亮牌 |  | 第 2 轮亮牌：红 ABSTAIN / 蓝 ABSTAIN，结果 DRAW |
| R514 | 08:34 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.26, "before": 73.31, "loss": 0.05, "playerId": 2707} |
| R515 | 08:35 | MED | 争夺亮牌 |  | 第 3 轮亮牌：红 ABSTAIN / 蓝 BING_ZHENG，结果 BLUE |
| R515 | 08:35 | HIGH | 强通争夺胜出 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 赢下 朱雀门(S14) 的强制通行争夺 |
| R515 | 08:35 | HIGH | 窗口争夺结束 |  | 争夺结束，胜方 BLUE，红蓝消耗 0/1 |
| R515 | 08:35 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.21, "before": 73.26, "loss": 0.05, "playerId": 2707} |
| R516 | 08:36 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 78, "targetNodeId": "S14"} |
| R516 | 08:36 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.16, "before": 73.21, "loss": 0.05, "playerId": 2707} |
| R517 | 08:37 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 77, "targetNodeId": "S14"} |
| R517 | 08:37 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.11, "before": 73.16, "loss": 0.05, "playerId": 2707} |
| R518 | 08:38 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 76, "targetNodeId": "S14"} |
| R518 | 08:38 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.06, "before": 73.11, "loss": 0.05, "playerId": 2707} |
| R519 | 08:39 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 75, "targetNodeId": "S14"} |
| R519 | 08:39 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 73.01, "before": 73.06, "loss": 0.05, "playerId": 2707} |
| R520 | 08:40 | MED | 任务过期 |  | T_016 在 梅关驿(S03) 过期 |
| R520 | 08:40 | MED | 任务过期 |  | T_017 在 洞庭水驿(S05) 过期 |
| R520 | 08:40 | MED | 任务过期 |  | T_018 在 关中平原(S12) 过期 |
| R520 | 08:40 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 74, "targetNodeId": "S14"} |
| R520 | 08:40 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.96, "before": 73.01, "loss": 0.05, "playerId": 2707} |
| R521 | 08:41 | HIGH | 设卡风化 |  | 朱雀门(S14) 的设卡发生风化，防守值 4->3 |
| R521 | 08:41 | HIGH | 破关悬赏生成 |  | 朱雀门(S14) 的设卡形成破关悬赏，悬赏值 10 分 |
| R521 | 08:41 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 73, "targetNodeId": "S14"} |
| R521 | 08:41 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.91, "before": 72.96, "loss": 0.05, "playerId": 2707} |
| R522 | 08:42 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 72, "targetNodeId": "S14"} |
| R522 | 08:42 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.86, "before": 72.91, "loss": 0.05, "playerId": 2707} |
| R523 | 08:43 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 71, "targetNodeId": "S14"} |
| R523 | 08:43 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.81, "before": 72.86, "loss": 0.05, "playerId": 2707} |
| R524 | 08:44 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 70, "targetNodeId": "S14"} |
| R524 | 08:44 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.76, "before": 72.81, "loss": 0.05, "playerId": 2707} |
| R525 | 08:45 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 69, "targetNodeId": "S14"} |
| R525 | 08:45 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.71, "before": 72.76, "loss": 0.05, "playerId": 2707} |
| R526 | 08:46 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 68, "targetNodeId": "S14"} |
| R526 | 08:46 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.66, "before": 72.71, "loss": 0.05, "playerId": 2707} |
| R527 | 08:47 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 67, "targetNodeId": "S14"} |
| R527 | 08:47 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.61, "before": 72.66, "loss": 0.05, "playerId": 2707} |
| R528 | 08:48 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 66, "targetNodeId": "S14"} |
| R528 | 08:48 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.56, "before": 72.61, "loss": 0.05, "playerId": 2707} |
| R529 | 08:49 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 65, "targetNodeId": "S14"} |
| R529 | 08:49 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.51, "before": 72.56, "loss": 0.05, "playerId": 2707} |
| R530 | 08:50 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 64, "targetNodeId": "S14"} |
| R530 | 08:50 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.46, "before": 72.51, "loss": 0.05, "playerId": 2707} |
| R531 | 08:51 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 63, "targetNodeId": "S14"} |
| R531 | 08:51 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.41, "before": 72.46, "loss": 0.05, "playerId": 2707} |
| R532 | 08:52 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 62, "targetNodeId": "S14"} |
| R532 | 08:52 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.36, "before": 72.41, "loss": 0.05, "playerId": 2707} |
| R533 | 08:53 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 61, "targetNodeId": "S14"} |
| R533 | 08:53 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.31, "before": 72.36, "loss": 0.05, "playerId": 2707} |
| R534 | 08:54 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 60, "targetNodeId": "S14"} |
| R534 | 08:54 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.26, "before": 72.31, "loss": 0.05, "playerId": 2707} |
| R535 | 08:55 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 59, "targetNodeId": "S14"} |
| R535 | 08:55 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.21, "before": 72.26, "loss": 0.05, "playerId": 2707} |
| R536 | 08:56 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 58, "targetNodeId": "S14"} |
| R536 | 08:56 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.16, "before": 72.21, "loss": 0.05, "playerId": 2707} |
| R537 | 08:57 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 57, "targetNodeId": "S14"} |
| R537 | 08:57 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.11, "before": 72.16, "loss": 0.05, "playerId": 2707} |
| R538 | 08:58 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 56, "targetNodeId": "S14"} |
| R538 | 08:58 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.06, "before": 72.11, "loss": 0.05, "playerId": 2707} |
| R539 | 08:59 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 55, "targetNodeId": "S14"} |
| R539 | 08:59 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 72.01, "before": 72.06, "loss": 0.05, "playerId": 2707} |
| R540 | 09:00 | MED | 任务过期 |  | T_020 在 关中平原(S12) 过期 |
| R540 | 09:00 | MED | 任务过期 |  | T_021 在 灞桥驿(S13) 过期 |
| R540 | 09:00 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 54, "targetNodeId": "S14"} |
| R540 | 09:00 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.96, "before": 72.01, "loss": 0.05, "playerId": 2707} |
| R541 | 09:01 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 53, "targetNodeId": "S14"} |
| R541 | 09:01 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.91, "before": 71.96, "loss": 0.05, "playerId": 2707} |
| R542 | 09:02 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 52, "targetNodeId": "S14"} |
| R542 | 09:02 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.86, "before": 71.91, "loss": 0.05, "playerId": 2707} |
| R543 | 09:03 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 51, "targetNodeId": "S14"} |
| R543 | 09:03 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.81, "before": 71.86, "loss": 0.05, "playerId": 2707} |
| R544 | 09:04 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 50, "targetNodeId": "S14"} |
| R544 | 09:04 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.76, "before": 71.81, "loss": 0.05, "playerId": 2707} |
| R545 | 09:05 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 49, "targetNodeId": "S14"} |
| R545 | 09:05 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.71, "before": 71.76, "loss": 0.05, "playerId": 2707} |
| R546 | 09:06 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 48, "targetNodeId": "S14"} |
| R546 | 09:06 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.66, "before": 71.71, "loss": 0.05, "playerId": 2707} |
| R547 | 09:07 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 47, "targetNodeId": "S14"} |
| R547 | 09:07 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.61, "before": 71.66, "loss": 0.05, "playerId": 2707} |
| R548 | 09:08 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 46, "targetNodeId": "S14"} |
| R548 | 09:08 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.55, "before": 71.61, "loss": 0.065, "playerId": 2707} |
| R549 | 09:09 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 45, "targetNodeId": "S14"} |
| R549 | 09:09 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.49, "before": 71.55, "loss": 0.065, "playerId": 2707} |
| R550 | 09:10 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 44, "targetNodeId": "S14"} |
| R550 | 09:10 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.43, "before": 71.49, "loss": 0.065, "playerId": 2707} |
| R551 | 09:11 | HIGH | 设卡风化 |  | 朱雀门(S14) 的设卡发生风化，防守值 3->2 |
| R551 | 09:11 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 43, "targetNodeId": "S14"} |
| R551 | 09:11 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.37, "before": 71.43, "loss": 0.065, "playerId": 2707} |
| R552 | 09:12 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 42, "targetNodeId": "S14"} |
| R552 | 09:12 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.31, "before": 71.37, "loss": 0.065, "playerId": 2707} |
| R553 | 09:13 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 41, "targetNodeId": "S14"} |
| R553 | 09:13 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.25, "before": 71.31, "loss": 0.065, "playerId": 2707} |
| R554 | 09:14 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 40, "targetNodeId": "S14"} |
| R554 | 09:14 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.19, "before": 71.25, "loss": 0.065, "playerId": 2707} |
| R555 | 09:15 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 39, "targetNodeId": "S14"} |
| R555 | 09:15 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.13, "before": 71.19, "loss": 0.065, "playerId": 2707} |
| R556 | 09:16 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 38, "targetNodeId": "S14"} |
| R556 | 09:16 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.07, "before": 71.13, "loss": 0.065, "playerId": 2707} |
| R557 | 09:17 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 37, "targetNodeId": "S14"} |
| R557 | 09:17 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 71.01, "before": 71.07, "loss": 0.065, "playerId": 2707} |
| R558 | 09:18 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 36, "targetNodeId": "S14"} |
| R558 | 09:18 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.95, "before": 71.01, "loss": 0.065, "playerId": 2707} |
| R559 | 09:19 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 35, "targetNodeId": "S14"} |
| R559 | 09:19 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.89, "before": 70.95, "loss": 0.065, "playerId": 2707} |
| R560 | 09:20 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 34, "targetNodeId": "S14"} |
| R560 | 09:20 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.83, "before": 70.89, "loss": 0.065, "playerId": 2707} |
| R561 | 09:21 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 33, "targetNodeId": "S14"} |
| R561 | 09:21 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.77, "before": 70.83, "loss": 0.065, "playerId": 2707} |
| R562 | 09:22 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 32, "targetNodeId": "S14"} |
| R562 | 09:22 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.71, "before": 70.77, "loss": 0.065, "playerId": 2707} |
| R563 | 09:23 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 31, "targetNodeId": "S14"} |
| R563 | 09:23 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.65, "before": 70.71, "loss": 0.065, "playerId": 2707} |
| R564 | 09:24 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 30, "targetNodeId": "S14"} |
| R564 | 09:24 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.59, "before": 70.65, "loss": 0.065, "playerId": 2707} |
| R565 | 09:25 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 29, "targetNodeId": "S14"} |
| R565 | 09:25 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.53, "before": 70.59, "loss": 0.065, "playerId": 2707} |
| R566 | 09:26 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 28, "targetNodeId": "S14"} |
| R566 | 09:26 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.47, "before": 70.53, "loss": 0.065, "playerId": 2707} |
| R567 | 09:27 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 27, "targetNodeId": "S14"} |
| R567 | 09:27 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.41, "before": 70.47, "loss": 0.065, "playerId": 2707} |
| R568 | 09:28 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 26, "targetNodeId": "S14"} |
| R568 | 09:28 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.35, "before": 70.41, "loss": 0.065, "playerId": 2707} |
| R569 | 09:29 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 25, "targetNodeId": "S14"} |
| R569 | 09:29 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.29, "before": 70.35, "loss": 0.065, "playerId": 2707} |
| R570 | 09:30 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 24, "targetNodeId": "S14"} |
| R570 | 09:30 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.23, "before": 70.29, "loss": 0.065, "playerId": 2707} |
| R571 | 09:31 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 23, "targetNodeId": "S14"} |
| R571 | 09:31 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.17, "before": 70.23, "loss": 0.065, "playerId": 2707} |
| R572 | 09:32 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 22, "targetNodeId": "S14"} |
| R572 | 09:32 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.11, "before": 70.17, "loss": 0.065, "playerId": 2707} |
| R573 | 09:33 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 21, "targetNodeId": "S14"} |
| R573 | 09:33 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 70.05, "before": 70.11, "loss": 0.065, "playerId": 2707} |
| R574 | 09:34 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 20, "targetNodeId": "S14"} |
| R574 | 09:34 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.99, "before": 70.05, "loss": 0.065, "playerId": 2707} |
| R574 | 09:34 | HIGH | 果品折损 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 好果跌破阈值 70，坏果 3 |
| R575 | 09:35 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 19, "targetNodeId": "S14"} |
| R575 | 09:35 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.93, "before": 69.99, "loss": 0.065, "playerId": 2707} |
| R576 | 09:36 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 18, "targetNodeId": "S14"} |
| R576 | 09:36 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.87, "before": 69.93, "loss": 0.065, "playerId": 2707} |
| R577 | 09:37 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 17, "targetNodeId": "S14"} |
| R577 | 09:37 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.81, "before": 69.87, "loss": 0.065, "playerId": 2707} |
| R578 | 09:38 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 16, "targetNodeId": "S14"} |
| R578 | 09:38 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.75, "before": 69.81, "loss": 0.065, "playerId": 2707} |
| R579 | 09:39 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 15, "targetNodeId": "S14"} |
| R579 | 09:39 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.69, "before": 69.75, "loss": 0.065, "playerId": 2707} |
| R580 | 09:40 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 14, "targetNodeId": "S14"} |
| R580 | 09:40 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.63, "before": 69.69, "loss": 0.065, "playerId": 2707} |
| R581 | 09:41 | HIGH | 设卡风化 |  | 朱雀门(S14) 的设卡发生风化，防守值 2->1 |
| R581 | 09:41 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 13, "targetNodeId": "S14"} |
| R581 | 09:41 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.57, "before": 69.63, "loss": 0.065, "playerId": 2707} |
| R582 | 09:42 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 12, "targetNodeId": "S14"} |
| R582 | 09:42 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.51, "before": 69.57, "loss": 0.065, "playerId": 2707} |
| R583 | 09:43 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 11, "targetNodeId": "S14"} |
| R583 | 09:43 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.45, "before": 69.51, "loss": 0.065, "playerId": 2707} |
| R584 | 09:44 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 10, "targetNodeId": "S14"} |
| R584 | 09:44 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.39, "before": 69.45, "loss": 0.065, "playerId": 2707} |
| R585 | 09:45 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 9, "targetNodeId": "S14"} |
| R585 | 09:45 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.33, "before": 69.39, "loss": 0.065, "playerId": 2707} |
| R586 | 09:46 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 8, "targetNodeId": "S14"} |
| R586 | 09:46 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.27, "before": 69.33, "loss": 0.065, "playerId": 2707} |
| R587 | 09:47 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 7, "targetNodeId": "S14"} |
| R587 | 09:47 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.21, "before": 69.27, "loss": 0.065, "playerId": 2707} |
| R588 | 09:48 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 6, "targetNodeId": "S14"} |
| R588 | 09:48 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.15, "before": 69.21, "loss": 0.065, "playerId": 2707} |
| R589 | 09:49 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 5, "targetNodeId": "S14"} |
| R589 | 09:49 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.09, "before": 69.15, "loss": 0.065, "playerId": 2707} |
| R590 | 09:50 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 4, "targetNodeId": "S14"} |
| R590 | 09:50 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 69.03, "before": 69.09, "loss": 0.065, "playerId": 2707} |
| R591 | 09:51 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 3, "targetNodeId": "S14"} |
| R591 | 09:51 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 68.97, "before": 69.03, "loss": 0.065, "playerId": 2707} |
| R592 | 09:52 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 2, "targetNodeId": "S14"} |
| R592 | 09:52 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 68.91, "before": 68.97, "loss": 0.065, "playerId": 2707} |
| R593 | 09:53 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 1, "targetNodeId": "S14"} |
| R593 | 09:53 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 68.85, "before": 68.91, "loss": 0.065, "playerId": 2707} |
| R594 | 09:54 | MED | PROCESS_PROGRESS | BLUE AAAA/v1.0(2707) | {"playerId": 2707, "processType": "FORCED_PASS", "remainingRound": 0, "targetNodeId": "S14"} |
| R594 | 09:54 | HIGH | 强制通行完成 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 完成对 朱雀门(S14) 的强制通行并到达目标 |
| R594 | 09:54 | HIGH | 进点 | BLUE AAAA/v1.0(2707) | BLUE AAAA/v1.0(2707) 进入 朱雀门(S14) |
| R594 | 09:54 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 68.8, "before": 68.85, "loss": 0.05, "playerId": 2707} |
| R595 | 09:55 | MED | WAIT | BLUE AAAA/v1.0(2707) | {"nodeId": "S14", "playerId": 2707} |
| R595 | 09:55 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 68.75, "before": 68.8, "loss": 0.05, "playerId": 2707} |
| R596 | 09:56 | MED | WAIT | BLUE AAAA/v1.0(2707) | {"nodeId": "S14", "playerId": 2707} |
| R596 | 09:56 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 68.7, "before": 68.75, "loss": 0.05, "playerId": 2707} |
| R597 | 09:57 | MED | WAIT | BLUE AAAA/v1.0(2707) | {"nodeId": "S14", "playerId": 2707} |
| R597 | 09:57 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 68.65, "before": 68.7, "loss": 0.05, "playerId": 2707} |
| R598 | 09:58 | MED | WAIT | BLUE AAAA/v1.0(2707) | {"nodeId": "S14", "playerId": 2707} |
| R598 | 09:58 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 68.6, "before": 68.65, "loss": 0.05, "playerId": 2707} |
| R599 | 09:59 | MED | WAIT | BLUE AAAA/v1.0(2707) | {"nodeId": "S14", "playerId": 2707} |
| R599 | 09:59 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 68.55, "before": 68.6, "loss": 0.05, "playerId": 2707} |
| R600 | 10:00 | MED | WAIT | BLUE AAAA/v1.0(2707) | {"nodeId": "S14", "playerId": 2707} |
| R600 | 10:00 | MED | FRESHNESS_DROP | BLUE AAAA/v1.0(2707) | {"after": 68.5, "before": 68.55, "loss": 0.05, "playerId": 2707} |
