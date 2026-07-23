# Lychee Replay Commentary Timeline

Source: `C:\Users\Administrator\Documents\AI解说\00_0721_回放\解说稿\43266\replay.txt`
Duration: 600 rounds

## Teams

- RED: AAAA / v1.0
- BLUE: 路人女主队 / 1.0

## Result

- RED AAAA/v1.0(2707): 60 points, good fruit 92, freshness 60.23, delivered False
- BLUE 路人女主队/1.0(2735): 612 points, good fruit 99, freshness 80.4, delivered True

## Commentary Events

| Round | Time | Priority | Event | Player | UI detail |
| --- | --- | --- | --- | --- | --- |
| R1 | 00:01 | HIGH | 派遣 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 派遣队伍清障 五岭山道(S06)，预计 R7 完成 |
| R1 | 00:01 | HIGH | 窗口争夺开始 |  | 五岭山道(S06) 开启OBSTACLE争夺，目标  |
| R1 | 00:01 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.95, "before": 100.0, "loss": 0.05, "playerId": 2735} |
| R1 | 00:01 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.95, "before": 100.0, "loss": 0.05, "playerId": 2707} |
| R1 | 00:01 | MED | 任务刷新 |  | T_001 刷新在 梅关驿(S03)，路线 ROAD，截止 R221 |
| R1 | 00:01 | MED | 任务刷新 |  | T_002 刷新在 江南码头(S04)，路线 WATER，截止 R221 |
| R1 | 00:01 | MED | 任务刷新 |  | T_003 刷新在 秦岭栈道(S08)，路线 MOUNTAIN，截止 R221 |
| R2 | 00:02 | MED | 争夺亮牌 |  | 第 1 轮亮牌：红 XIAN_GONG / 蓝 ABSTAIN，结果 RED |
| R2 | 00:02 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.9, "before": 99.95, "loss": 0.05, "playerId": 2707} |
| R2 | 00:02 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.9, "before": 99.95, "loss": 0.05, "playerId": 2735} |
| R3 | 00:03 | MED | 争夺亮牌 |  | 第 2 轮亮牌：红 XIAN_GONG / 蓝 ABSTAIN，结果 RED |
| R3 | 00:03 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.85, "before": 99.9, "loss": 0.05, "playerId": 2707} |
| R3 | 00:03 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.85, "before": 99.9, "loss": 0.05, "playerId": 2735} |
| R4 | 00:04 | MED | 争夺亮牌 |  | 第 3 轮亮牌：红 ABSTAIN / 蓝 ABSTAIN，结果 DRAW |
| R4 | 00:04 | MED | OBSTACLE_CONTEST_WIN | RED AAAA/v1.0(2707) | {"contestId": "C_001_001", "playerId": 2707, "sourceAction": "CLEAR", "targetNodeId": "S06"} |
| R4 | 00:04 | HIGH | 窗口争夺结束 |  | 争夺结束，胜方 RED，红蓝消耗 2/0 |
| R4 | 00:04 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.8, "before": 99.85, "loss": 0.05, "playerId": 2735} |
| R4 | 00:04 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.8, "before": 99.85, "loss": 0.05, "playerId": 2707} |
| R5 | 00:05 | HIGH | 业务拒绝 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 的动作未生效：目标正在被处理，目标 五岭山道(S06)；不计普通非法动作 |
| R5 | 00:05 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.75, "before": 99.8, "loss": 0.05, "playerId": 2735} |
| R5 | 00:05 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 5, "targetNodeId": "S06"} |
| R5 | 00:05 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.75, "before": 99.8, "loss": 0.05, "playerId": 2707} |
| R6 | 00:06 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 4, "targetNodeId": "S06"} |
| R6 | 00:06 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.7, "before": 99.75, "loss": 0.05, "playerId": 2707} |
| R6 | 00:06 | HIGH | 业务拒绝 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 的动作未生效：目标正在被处理，目标 五岭山道(S06)；不计普通非法动作 |
| R6 | 00:06 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.7, "before": 99.75, "loss": 0.05, "playerId": 2735} |
| R7 | 00:07 | HIGH | 清障完成 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 完成 五岭山道(S06) 清障 |
| R7 | 00:07 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 3, "targetNodeId": "S06"} |
| R7 | 00:07 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.65, "before": 99.7, "loss": 0.05, "playerId": 2707} |
| R7 | 00:07 | HIGH | 业务拒绝 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 的动作未生效：OBSTACLE_NOT_FOUND，目标 ；不计普通非法动作 |
| R7 | 00:07 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.65, "before": 99.7, "loss": 0.05, "playerId": 2735} |
| R8 | 00:08 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 1000, "edgeProgressPermille": 12, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.012484394506866416, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R8 | 00:08 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.58, "before": 99.65, "loss": 0.07, "playerId": 2735} |
| R8 | 00:08 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 2, "targetNodeId": "S06"} |
| R8 | 00:08 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.6, "before": 99.65, "loss": 0.05, "playerId": 2707} |
| R9 | 00:09 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 2000, "edgeProgressPermille": 24, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.024968789013732832, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R9 | 00:09 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.51, "before": 99.58, "loss": 0.07, "playerId": 2735} |
| R9 | 00:09 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 1, "targetNodeId": "S06"} |
| R9 | 00:09 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.55, "before": 99.6, "loss": 0.05, "playerId": 2707} |
| R10 | 00:10 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 0, "targetNodeId": "S06"} |
| R10 | 00:10 | HIGH | 业务拒绝 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 的动作未生效：OBSTACLE_NOT_FOUND，目标 ；不计普通非法动作 |
| R10 | 00:10 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.5, "before": 99.55, "loss": 0.05, "playerId": 2707} |
| R10 | 00:10 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 3000, "edgeProgressPermille": 37, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.03745318352059925, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R10 | 00:10 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.44, "before": 99.51, "loss": 0.07, "playerId": 2735} |
| R11 | 00:11 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 21, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.021312872975277068, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R11 | 00:11 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.45, "before": 99.5, "loss": 0.055, "playerId": 2707} |
| R11 | 00:11 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 4000, "edgeProgressPermille": 49, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.049937578027465665, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R11 | 00:11 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.37, "before": 99.44, "loss": 0.07, "playerId": 2735} |
| R12 | 00:12 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 5000, "edgeProgressPermille": 62, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.062421972534332085, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R12 | 00:12 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.3, "before": 99.37, "loss": 0.07, "playerId": 2735} |
| R12 | 00:12 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 42, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.042625745950554135, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R12 | 00:12 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.4, "before": 99.45, "loss": 0.055, "playerId": 2707} |
| R13 | 00:13 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 6000, "edgeProgressPermille": 74, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.0749063670411985, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R13 | 00:13 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.23, "before": 99.3, "loss": 0.07, "playerId": 2735} |
| R13 | 00:13 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 63, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.0639386189258312, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R13 | 00:13 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.35, "before": 99.4, "loss": 0.055, "playerId": 2707} |
| R14 | 00:14 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 85, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.08525149190110827, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R14 | 00:14 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.29, "before": 99.35, "loss": 0.055, "playerId": 2707} |
| R14 | 00:14 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 7000, "edgeProgressPermille": 87, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.08739076154806492, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R14 | 00:14 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.16, "before": 99.23, "loss": 0.07, "playerId": 2735} |
| R15 | 00:15 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 106, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.10656436487638533, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R15 | 00:15 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.24, "before": 99.29, "loss": 0.055, "playerId": 2707} |
| R15 | 00:15 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 8000, "edgeProgressPermille": 99, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.09987515605493133, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R15 | 00:15 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.09, "before": 99.16, "loss": 0.07, "playerId": 2735} |
| R16 | 00:16 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 9000, "edgeProgressPermille": 112, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.11235955056179775, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R16 | 00:16 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 99.02, "before": 99.09, "loss": 0.07, "playerId": 2735} |
| R16 | 00:16 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 127, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.1278772378516624, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R16 | 00:16 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.18, "before": 99.24, "loss": 0.055, "playerId": 2707} |
| R17 | 00:17 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 10000, "edgeProgressPermille": 124, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.12484394506866417, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R17 | 00:17 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 98.95, "before": 99.02, "loss": 0.07, "playerId": 2735} |
| R17 | 00:17 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 149, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.14919011082693948, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R17 | 00:17 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.13, "before": 99.18, "loss": 0.055, "playerId": 2707} |
| R18 | 00:18 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 170, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.17050298380221654, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R18 | 00:18 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.07, "before": 99.13, "loss": 0.055, "playerId": 2707} |
| R18 | 00:18 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 11000, "edgeProgressPermille": 137, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.1373283395755306, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R18 | 00:18 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 98.88, "before": 98.95, "loss": 0.07, "playerId": 2735} |
| R19 | 00:19 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 191, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.1918158567774936, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R19 | 00:19 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 99.01, "before": 99.07, "loss": 0.055, "playerId": 2707} |
| R19 | 00:19 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 12000, "edgeProgressPermille": 149, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.149812734082397, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R19 | 00:19 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 98.81, "before": 98.88, "loss": 0.07, "playerId": 2735} |
| R20 | 00:20 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 13000, "edgeProgressPermille": 162, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.16229712858926343, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R20 | 00:20 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 98.74, "before": 98.81, "loss": 0.07, "playerId": 2735} |
| R20 | 00:20 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 213, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.21312872975277067, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R20 | 00:20 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.96, "before": 99.01, "loss": 0.055, "playerId": 2707} |
| R21 | 00:21 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 14000, "edgeProgressPermille": 174, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.17478152309612985, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R21 | 00:21 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 98.67, "before": 98.74, "loss": 0.07, "playerId": 2735} |
| R21 | 00:21 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 234, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.23444160272804773, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R21 | 00:21 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.9, "before": 98.96, "loss": 0.055, "playerId": 2707} |
| R22 | 00:22 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 12000, "edgeProgressPermille": 255, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.2557544757033248, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R22 | 00:22 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.85, "before": 98.9, "loss": 0.055, "playerId": 2707} |
| R22 | 00:22 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 15000, "edgeProgressPermille": 187, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.18726591760299627, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R22 | 00:22 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 98.6, "before": 98.67, "loss": 0.07, "playerId": 2735} |
| R23 | 00:23 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 13000, "edgeProgressPermille": 277, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.2770673486786019, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R23 | 00:23 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.79, "before": 98.85, "loss": 0.055, "playerId": 2707} |
| R23 | 00:23 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 16000, "edgeProgressPermille": 199, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.19975031210986266, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R23 | 00:23 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 98.53, "before": 98.6, "loss": 0.07, "playerId": 2735} |
| R24 | 00:24 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 17000, "edgeProgressPermille": 212, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.21223470661672908, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R24 | 00:24 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 98.46, "before": 98.53, "loss": 0.07, "playerId": 2735} |
| R24 | 00:24 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 298, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.29838022165387895, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R24 | 00:24 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.74, "before": 98.79, "loss": 0.055, "playerId": 2707} |
| R25 | 00:25 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 18000, "edgeProgressPermille": 224, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.2247191011235955, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R25 | 00:25 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 98.39, "before": 98.46, "loss": 0.07, "playerId": 2735} |
| R25 | 00:25 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 15000, "edgeProgressPermille": 319, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.319693094629156, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R25 | 00:25 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.68, "before": 98.74, "loss": 0.055, "playerId": 2707} |
| R26 | 00:26 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 16000, "edgeProgressPermille": 341, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.3410059676044331, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R26 | 00:26 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.63, "before": 98.68, "loss": 0.055, "playerId": 2707} |
| R26 | 00:26 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 19000, "edgeProgressPermille": 237, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.23720349563046192, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R26 | 00:26 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 98.32, "before": 98.39, "loss": 0.07, "playerId": 2735} |
| R27 | 00:27 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 17000, "edgeProgressPermille": 362, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.36231884057971014, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R27 | 00:27 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.57, "before": 98.63, "loss": 0.055, "playerId": 2707} |
| R27 | 00:27 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 20000, "edgeProgressPermille": 249, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.24968789013732834, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R27 | 00:27 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 98.25, "before": 98.32, "loss": 0.07, "playerId": 2735} |
| R28 | 00:28 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 21000, "edgeProgressPermille": 262, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.26217228464419473, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R28 | 00:28 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 98.18, "before": 98.25, "loss": 0.07, "playerId": 2735} |
| R28 | 00:28 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 18000, "edgeProgressPermille": 383, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.3836317135549872, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R28 | 00:28 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.51, "before": 98.57, "loss": 0.055, "playerId": 2707} |
| R29 | 00:29 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 22000, "edgeProgressPermille": 274, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.2746566791510612, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R29 | 00:29 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 98.11, "before": 98.18, "loss": 0.07, "playerId": 2735} |
| R29 | 00:29 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 19000, "edgeProgressPermille": 404, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.40494458653026427, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R29 | 00:29 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.46, "before": 98.51, "loss": 0.055, "playerId": 2707} |
| R30 | 00:30 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 20000, "edgeProgressPermille": 426, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.42625745950554134, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R30 | 00:30 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.4, "before": 98.46, "loss": 0.055, "playerId": 2707} |
| R30 | 00:30 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 23000, "edgeProgressPermille": 287, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.28714107365792757, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R30 | 00:30 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 98.04, "before": 98.11, "loss": 0.07, "playerId": 2735} |
| R30 | 00:30 | MED | 任务刷新 |  | T_004 刷新在 梅关驿(S03)，路线 ROAD，截止 R210 |
| R31 | 00:31 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 21000, "edgeProgressPermille": 447, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.4475703324808184, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R31 | 00:31 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.35, "before": 98.4, "loss": 0.055, "playerId": 2707} |
| R31 | 00:31 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 24000, "edgeProgressPermille": 299, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.299625468164794, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R31 | 00:31 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 97.97, "before": 98.04, "loss": 0.07, "playerId": 2735} |
| R32 | 00:32 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 25000, "edgeProgressPermille": 312, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.3121098626716604, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R32 | 00:32 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 97.9, "before": 97.97, "loss": 0.07, "playerId": 2735} |
| R32 | 00:32 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 22000, "edgeProgressPermille": 468, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.46888320545609546, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R32 | 00:32 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.29, "before": 98.35, "loss": 0.055, "playerId": 2707} |
| R33 | 00:33 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 26000, "edgeProgressPermille": 324, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.32459425717852686, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R33 | 00:33 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 97.83, "before": 97.9, "loss": 0.07, "playerId": 2735} |
| R33 | 00:33 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 23000, "edgeProgressPermille": 490, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.49019607843137253, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R33 | 00:33 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.24, "before": 98.29, "loss": 0.055, "playerId": 2707} |
| R34 | 00:34 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 24000, "edgeProgressPermille": 511, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5115089514066496, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R34 | 00:34 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.18, "before": 98.24, "loss": 0.055, "playerId": 2707} |
| R34 | 00:34 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 27000, "edgeProgressPermille": 337, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.33707865168539325, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R34 | 00:34 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 97.76, "before": 97.83, "loss": 0.07, "playerId": 2735} |
| R35 | 00:35 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 25000, "edgeProgressPermille": 532, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5328218243819267, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R35 | 00:35 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.13, "before": 98.18, "loss": 0.055, "playerId": 2707} |
| R35 | 00:35 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 28000, "edgeProgressPermille": 349, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.3495630461922597, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R35 | 00:35 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 97.69, "before": 97.76, "loss": 0.07, "playerId": 2735} |
| R36 | 00:36 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 29000, "edgeProgressPermille": 362, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.3620474406991261, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R36 | 00:36 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 97.62, "before": 97.69, "loss": 0.07, "playerId": 2735} |
| R36 | 00:36 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 26000, "edgeProgressPermille": 554, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5541346973572038, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R36 | 00:36 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.07, "before": 98.13, "loss": 0.055, "playerId": 2707} |
| R37 | 00:37 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 30000, "edgeProgressPermille": 374, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.37453183520599254, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R37 | 00:37 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 97.55, "before": 97.62, "loss": 0.07, "playerId": 2735} |
| R37 | 00:37 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 27000, "edgeProgressPermille": 575, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5754475703324808, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R37 | 00:37 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 98.01, "before": 98.07, "loss": 0.055, "playerId": 2707} |
| R38 | 00:38 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 28000, "edgeProgressPermille": 596, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5967604433077579, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R38 | 00:38 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.96, "before": 98.01, "loss": 0.055, "playerId": 2707} |
| R38 | 00:38 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 31000, "edgeProgressPermille": 387, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.38701622971285893, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R38 | 00:38 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 97.48, "before": 97.55, "loss": 0.07, "playerId": 2735} |
| R39 | 00:39 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 29000, "edgeProgressPermille": 618, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.618073316283035, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R39 | 00:39 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.9, "before": 97.96, "loss": 0.055, "playerId": 2707} |
| R39 | 00:39 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 32000, "edgeProgressPermille": 399, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.3995006242197253, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R39 | 00:39 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 97.41, "before": 97.48, "loss": 0.07, "playerId": 2735} |
| R40 | 00:40 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 33000, "edgeProgressPermille": 411, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.41198501872659177, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R40 | 00:40 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 97.34, "before": 97.41, "loss": 0.07, "playerId": 2735} |
| R40 | 00:40 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 30000, "edgeProgressPermille": 639, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.639386189258312, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R40 | 00:40 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.85, "before": 97.9, "loss": 0.055, "playerId": 2707} |
| R41 | 00:41 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 34000, "edgeProgressPermille": 424, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.42446941323345816, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R41 | 00:41 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 97.27, "before": 97.34, "loss": 0.07, "playerId": 2735} |
| R41 | 00:41 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 31000, "edgeProgressPermille": 660, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6606990622335891, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R41 | 00:41 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.79, "before": 97.85, "loss": 0.055, "playerId": 2707} |
| R42 | 00:42 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 32000, "edgeProgressPermille": 682, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6820119352088662, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R42 | 00:42 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.74, "before": 97.79, "loss": 0.055, "playerId": 2707} |
| R42 | 00:42 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 35000, "edgeProgressPermille": 436, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.4369538077403246, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R42 | 00:42 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 97.2, "before": 97.27, "loss": 0.07, "playerId": 2735} |
| R43 | 00:43 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 33000, "edgeProgressPermille": 703, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7033248081841432, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R43 | 00:43 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.68, "before": 97.74, "loss": 0.055, "playerId": 2707} |
| R43 | 00:43 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 36000, "edgeProgressPermille": 449, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.449438202247191, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R43 | 00:43 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 97.13, "before": 97.2, "loss": 0.07, "playerId": 2735} |
| R44 | 00:44 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 37000, "edgeProgressPermille": 461, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.46192259675405745, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R44 | 00:44 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 97.06, "before": 97.13, "loss": 0.07, "playerId": 2735} |
| R44 | 00:44 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 34000, "edgeProgressPermille": 724, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7246376811594203, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R44 | 00:44 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.63, "before": 97.68, "loss": 0.055, "playerId": 2707} |
| R45 | 00:45 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 38000, "edgeProgressPermille": 474, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.47440699126092384, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R45 | 00:45 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 96.99, "before": 97.06, "loss": 0.07, "playerId": 2735} |
| R45 | 00:45 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 35000, "edgeProgressPermille": 745, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7459505541346974, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R45 | 00:45 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.57, "before": 97.63, "loss": 0.055, "playerId": 2707} |
| R46 | 00:46 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 36000, "edgeProgressPermille": 767, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7672634271099744, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R46 | 00:46 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.51, "before": 97.57, "loss": 0.055, "playerId": 2707} |
| R46 | 00:46 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 39000, "edgeProgressPermille": 486, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.4868913857677903, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R46 | 00:46 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 96.92, "before": 96.99, "loss": 0.07, "playerId": 2735} |
| R47 | 00:47 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 37000, "edgeProgressPermille": 788, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7885763000852515, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R47 | 00:47 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.46, "before": 97.51, "loss": 0.055, "playerId": 2707} |
| R47 | 00:47 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 40000, "edgeProgressPermille": 499, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.4993757802746567, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R47 | 00:47 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 96.85, "before": 96.92, "loss": 0.07, "playerId": 2735} |
| R48 | 00:48 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 41000, "edgeProgressPermille": 511, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.5118601747815231, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R48 | 00:48 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 96.78, "before": 96.85, "loss": 0.07, "playerId": 2735} |
| R48 | 00:48 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 38000, "edgeProgressPermille": 809, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8098891730605285, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R48 | 00:48 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.4, "before": 97.46, "loss": 0.055, "playerId": 2707} |
| R49 | 00:49 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 42000, "edgeProgressPermille": 524, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.5243445692883895, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R49 | 00:49 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 96.71, "before": 96.78, "loss": 0.07, "playerId": 2735} |
| R49 | 00:49 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 39000, "edgeProgressPermille": 831, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8312020460358056, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R49 | 00:49 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.35, "before": 97.4, "loss": 0.055, "playerId": 2707} |
| R50 | 00:50 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 40000, "edgeProgressPermille": 852, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8525149190110827, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R50 | 00:50 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.29, "before": 97.35, "loss": 0.055, "playerId": 2707} |
| R50 | 00:50 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 43000, "edgeProgressPermille": 536, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.5368289637952559, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R50 | 00:50 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 96.64, "before": 96.71, "loss": 0.07, "playerId": 2735} |
| R51 | 00:51 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 41000, "edgeProgressPermille": 873, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8738277919863597, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R51 | 00:51 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.24, "before": 97.29, "loss": 0.055, "playerId": 2707} |
| R51 | 00:51 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 44000, "edgeProgressPermille": 549, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.5493133583021224, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R51 | 00:51 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 96.57, "before": 96.64, "loss": 0.07, "playerId": 2735} |
| R52 | 00:52 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 45000, "edgeProgressPermille": 561, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.5617977528089888, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R52 | 00:52 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 96.5, "before": 96.57, "loss": 0.07, "playerId": 2735} |
| R52 | 00:52 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 42000, "edgeProgressPermille": 895, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8951406649616368, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R52 | 00:52 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.18, "before": 97.24, "loss": 0.055, "playerId": 2707} |
| R53 | 00:53 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 46000, "edgeProgressPermille": 574, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.5742821473158551, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R53 | 00:53 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 96.43, "before": 96.5, "loss": 0.07, "playerId": 2735} |
| R53 | 00:53 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 43000, "edgeProgressPermille": 916, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9164535379369139, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R53 | 00:53 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.13, "before": 97.18, "loss": 0.055, "playerId": 2707} |
| R54 | 00:54 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 44000, "edgeProgressPermille": 937, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9377664109121909, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R54 | 00:54 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.07, "before": 97.13, "loss": 0.055, "playerId": 2707} |
| R54 | 00:54 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 47000, "edgeProgressPermille": 586, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.5867665418227216, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R54 | 00:54 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 96.36, "before": 96.43, "loss": 0.07, "playerId": 2735} |
| R55 | 00:55 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 45000, "edgeProgressPermille": 959, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.959079283887468, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R55 | 00:55 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 97.01, "before": 97.07, "loss": 0.055, "playerId": 2707} |
| R55 | 00:55 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 48000, "edgeProgressPermille": 599, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.599250936329588, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R55 | 00:55 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 96.29, "before": 96.36, "loss": 0.07, "playerId": 2735} |
| R56 | 00:56 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 49000, "edgeProgressPermille": 611, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.6117353308364545, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R56 | 00:56 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 96.22, "before": 96.29, "loss": 0.07, "playerId": 2735} |
| R56 | 00:56 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 46000, "edgeProgressPermille": 980, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9803921568627451, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R56 | 00:56 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.96, "before": 97.01, "loss": 0.055, "playerId": 2707} |
| R57 | 00:57 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 50000, "edgeProgressPermille": 624, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.6242197253433208, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R57 | 00:57 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 96.15, "before": 96.22, "loss": 0.07, "playerId": 2735} |
| R57 | 00:57 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 46920, "edgeProgressPermille": 1000, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 1.0, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R57 | 00:57 | HIGH | 进点 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 进入 南岭驿(S02) |
| R57 | 00:57 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.9, "before": 96.96, "loss": 0.055, "playerId": 2707} |
| R58 | 00:58 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 21, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.021312872975277068, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R58 | 00:58 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.85, "before": 96.9, "loss": 0.055, "playerId": 2707} |
| R58 | 00:58 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 51000, "edgeProgressPermille": 636, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.6367041198501873, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R58 | 00:58 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 96.08, "before": 96.15, "loss": 0.07, "playerId": 2735} |
| R59 | 00:59 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 42, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.042625745950554135, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R59 | 00:59 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.79, "before": 96.85, "loss": 0.055, "playerId": 2707} |
| R59 | 00:59 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 52000, "edgeProgressPermille": 649, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.6491885143570537, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R59 | 00:59 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 96.01, "before": 96.08, "loss": 0.07, "playerId": 2735} |
| R60 | 01:00 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 53000, "edgeProgressPermille": 661, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.66167290886392, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R60 | 01:00 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 95.94, "before": 96.01, "loss": 0.07, "playerId": 2735} |
| R60 | 01:00 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 63, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.0639386189258312, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R60 | 01:00 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.74, "before": 96.79, "loss": 0.055, "playerId": 2707} |
| R60 | 01:00 | MED | 任务刷新 |  | T_005 刷新在 五岭山道(S06)，路线 MOUNTAIN，截止 R240 |
| R61 | 01:01 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 54000, "edgeProgressPermille": 674, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.6741573033707865, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R61 | 01:01 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 95.87, "before": 95.94, "loss": 0.07, "playerId": 2735} |
| R61 | 01:01 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 85, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.08525149190110827, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R61 | 01:01 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.68, "before": 96.74, "loss": 0.055, "playerId": 2707} |
| R62 | 01:02 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 106, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.10656436487638533, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R62 | 01:02 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.63, "before": 96.68, "loss": 0.055, "playerId": 2707} |
| R62 | 01:02 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 55000, "edgeProgressPermille": 686, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.686641697877653, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R62 | 01:02 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 95.8, "before": 95.87, "loss": 0.07, "playerId": 2735} |
| R63 | 01:03 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 127, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.1278772378516624, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R63 | 01:03 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.57, "before": 96.63, "loss": 0.055, "playerId": 2707} |
| R63 | 01:03 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 56000, "edgeProgressPermille": 699, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.6991260923845194, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R63 | 01:03 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 95.73, "before": 95.8, "loss": 0.07, "playerId": 2735} |
| R64 | 01:04 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 57000, "edgeProgressPermille": 711, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.7116104868913857, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R64 | 01:04 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 95.66, "before": 95.73, "loss": 0.07, "playerId": 2735} |
| R64 | 01:04 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 149, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.14919011082693948, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R64 | 01:04 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.51, "before": 96.57, "loss": 0.055, "playerId": 2707} |
| R65 | 01:05 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 58000, "edgeProgressPermille": 724, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.7240948813982522, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R65 | 01:05 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 95.59, "before": 95.66, "loss": 0.07, "playerId": 2735} |
| R65 | 01:05 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 170, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.17050298380221654, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R65 | 01:05 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.46, "before": 96.51, "loss": 0.055, "playerId": 2707} |
| R66 | 01:06 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 191, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.1918158567774936, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R66 | 01:06 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.4, "before": 96.46, "loss": 0.055, "playerId": 2707} |
| R66 | 01:06 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 59000, "edgeProgressPermille": 736, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.7365792759051186, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R66 | 01:06 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 95.52, "before": 95.59, "loss": 0.07, "playerId": 2735} |
| R67 | 01:07 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 213, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.21312872975277067, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R67 | 01:07 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.35, "before": 96.4, "loss": 0.055, "playerId": 2707} |
| R67 | 01:07 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 60000, "edgeProgressPermille": 749, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.7490636704119851, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R67 | 01:07 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 95.45, "before": 95.52, "loss": 0.07, "playerId": 2735} |
| R68 | 01:08 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 61000, "edgeProgressPermille": 761, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.7615480649188514, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R68 | 01:08 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 95.38, "before": 95.45, "loss": 0.07, "playerId": 2735} |
| R68 | 01:08 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 234, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.23444160272804773, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R68 | 01:08 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.29, "before": 96.35, "loss": 0.055, "playerId": 2707} |
| R69 | 01:09 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 62000, "edgeProgressPermille": 774, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.7740324594257179, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R69 | 01:09 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 95.31, "before": 95.38, "loss": 0.07, "playerId": 2735} |
| R69 | 01:09 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 12000, "edgeProgressPermille": 255, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.2557544757033248, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R69 | 01:09 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.24, "before": 96.29, "loss": 0.055, "playerId": 2707} |
| R70 | 01:10 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 13000, "edgeProgressPermille": 277, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.2770673486786019, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R70 | 01:10 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.18, "before": 96.24, "loss": 0.055, "playerId": 2707} |
| R70 | 01:10 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 63000, "edgeProgressPermille": 786, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.7865168539325843, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R70 | 01:10 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 95.24, "before": 95.31, "loss": 0.07, "playerId": 2735} |
| R71 | 01:11 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 298, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.29838022165387895, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R71 | 01:11 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.13, "before": 96.18, "loss": 0.055, "playerId": 2707} |
| R71 | 01:11 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 64000, "edgeProgressPermille": 799, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.7990012484394506, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R71 | 01:11 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 95.17, "before": 95.24, "loss": 0.07, "playerId": 2735} |
| R72 | 01:12 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 65000, "edgeProgressPermille": 811, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.8114856429463171, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R72 | 01:12 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 95.1, "before": 95.17, "loss": 0.07, "playerId": 2735} |
| R72 | 01:12 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 15000, "edgeProgressPermille": 319, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.319693094629156, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R72 | 01:12 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.07, "before": 96.13, "loss": 0.055, "playerId": 2707} |
| R73 | 01:13 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 66000, "edgeProgressPermille": 823, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.8239700374531835, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R73 | 01:13 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 95.03, "before": 95.1, "loss": 0.07, "playerId": 2735} |
| R73 | 01:13 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 16000, "edgeProgressPermille": 341, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.3410059676044331, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R73 | 01:13 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 96.01, "before": 96.07, "loss": 0.055, "playerId": 2707} |
| R74 | 01:14 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 17000, "edgeProgressPermille": 362, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.36231884057971014, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R74 | 01:14 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.96, "before": 96.01, "loss": 0.055, "playerId": 2707} |
| R74 | 01:14 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 67000, "edgeProgressPermille": 836, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.83645443196005, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R74 | 01:14 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.96, "before": 95.03, "loss": 0.07, "playerId": 2735} |
| R75 | 01:15 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 18000, "edgeProgressPermille": 383, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.3836317135549872, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R75 | 01:15 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.9, "before": 95.96, "loss": 0.055, "playerId": 2707} |
| R75 | 01:15 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 68000, "edgeProgressPermille": 848, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.8489388264669163, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R75 | 01:15 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.89, "before": 94.96, "loss": 0.07, "playerId": 2735} |
| R76 | 01:16 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 69000, "edgeProgressPermille": 861, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.8614232209737828, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R76 | 01:16 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.82, "before": 94.89, "loss": 0.07, "playerId": 2735} |
| R76 | 01:16 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 19000, "edgeProgressPermille": 404, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.40494458653026427, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R76 | 01:16 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.85, "before": 95.9, "loss": 0.055, "playerId": 2707} |
| R77 | 01:17 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 70000, "edgeProgressPermille": 873, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.8739076154806492, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R77 | 01:17 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.75, "before": 94.82, "loss": 0.07, "playerId": 2735} |
| R77 | 01:17 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 20000, "edgeProgressPermille": 426, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.42625745950554134, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R77 | 01:17 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.79, "before": 95.85, "loss": 0.055, "playerId": 2707} |
| R78 | 01:18 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 21000, "edgeProgressPermille": 447, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.4475703324808184, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R78 | 01:18 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.74, "before": 95.79, "loss": 0.055, "playerId": 2707} |
| R78 | 01:18 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 71000, "edgeProgressPermille": 886, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.8863920099875156, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R78 | 01:18 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.68, "before": 94.75, "loss": 0.07, "playerId": 2735} |
| R79 | 01:19 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 22000, "edgeProgressPermille": 468, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.46888320545609546, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R79 | 01:19 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.68, "before": 95.74, "loss": 0.055, "playerId": 2707} |
| R79 | 01:19 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 72000, "edgeProgressPermille": 898, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.898876404494382, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R79 | 01:19 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.61, "before": 94.68, "loss": 0.07, "playerId": 2735} |
| R80 | 01:20 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 73000, "edgeProgressPermille": 911, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.9113607990012484, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R80 | 01:20 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.54, "before": 94.61, "loss": 0.07, "playerId": 2735} |
| R80 | 01:20 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 23000, "edgeProgressPermille": 490, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.49019607843137253, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R80 | 01:20 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.63, "before": 95.68, "loss": 0.055, "playerId": 2707} |
| R81 | 01:21 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 74000, "edgeProgressPermille": 923, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.9238451935081149, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R81 | 01:21 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.47, "before": 94.54, "loss": 0.07, "playerId": 2735} |
| R81 | 01:21 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 24000, "edgeProgressPermille": 511, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.5115089514066496, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R81 | 01:21 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.57, "before": 95.63, "loss": 0.055, "playerId": 2707} |
| R82 | 01:22 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 25000, "edgeProgressPermille": 532, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.5328218243819267, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R82 | 01:22 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.51, "before": 95.57, "loss": 0.055, "playerId": 2707} |
| R82 | 01:22 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 75000, "edgeProgressPermille": 936, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.9363295880149812, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R82 | 01:22 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.4, "before": 94.47, "loss": 0.07, "playerId": 2735} |
| R83 | 01:23 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 26000, "edgeProgressPermille": 554, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.5541346973572038, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R83 | 01:23 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.46, "before": 95.51, "loss": 0.055, "playerId": 2707} |
| R83 | 01:23 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 76000, "edgeProgressPermille": 948, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.9488139825218477, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R83 | 01:23 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.33, "before": 94.4, "loss": 0.07, "playerId": 2735} |
| R84 | 01:24 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 77000, "edgeProgressPermille": 961, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.9612983770287141, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R84 | 01:24 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.26, "before": 94.33, "loss": 0.07, "playerId": 2735} |
| R84 | 01:24 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 27000, "edgeProgressPermille": 575, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.5754475703324808, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R84 | 01:24 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.4, "before": 95.46, "loss": 0.055, "playerId": 2707} |
| R85 | 01:25 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 78000, "edgeProgressPermille": 973, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.9737827715355806, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R85 | 01:25 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.19, "before": 94.26, "loss": 0.07, "playerId": 2735} |
| R85 | 01:25 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 28000, "edgeProgressPermille": 596, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.5967604433077579, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R85 | 01:25 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.35, "before": 95.4, "loss": 0.055, "playerId": 2707} |
| R86 | 01:26 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 29000, "edgeProgressPermille": 618, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.618073316283035, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R86 | 01:26 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.29, "before": 95.35, "loss": 0.055, "playerId": 2707} |
| R86 | 01:26 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 79000, "edgeProgressPermille": 986, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.9862671660424469, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R86 | 01:26 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.12, "before": 94.19, "loss": 0.07, "playerId": 2735} |
| R87 | 01:27 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 30000, "edgeProgressPermille": 639, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.639386189258312, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R87 | 01:27 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.24, "before": 95.29, "loss": 0.055, "playerId": 2707} |
| R87 | 01:27 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 80000, "edgeProgressPermille": 998, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 0.9987515605493134, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R87 | 01:27 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.05, "before": 94.12, "loss": 0.07, "playerId": 2735} |
| R88 | 01:28 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 80100, "edgeProgressPermille": 1000, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2735, "progress": 1.0, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R88 | 01:28 | HIGH | 进点 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 进入 五岭山道(S06) |
| R88 | 01:28 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.95, "before": 94.05, "loss": 0.10500000000000001, "playerId": 2735} |
| R88 | 01:28 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 31000, "edgeProgressPermille": 660, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.6606990622335891, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R88 | 01:28 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.16, "before": 95.24, "loss": 0.0825, "playerId": 2707} |
| R89 | 01:29 | MED | PROCESS_PROGRESS | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "processType": "CLAIM_RESOURCE", "remainingRound": 1, "targetNodeId": "S06"} |
| R89 | 01:29 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.88, "before": 93.95, "loss": 0.07500000000000001, "playerId": 2735} |
| R89 | 01:29 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 32000, "edgeProgressPermille": 682, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.6820119352088662, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R89 | 01:29 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.08, "before": 95.16, "loss": 0.0825, "playerId": 2707} |
| R90 | 01:30 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 33000, "edgeProgressPermille": 703, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.7033248081841432, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R90 | 01:30 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 95.0, "before": 95.08, "loss": 0.0825, "playerId": 2707} |
| R90 | 01:30 | MED | PROCESS_PROGRESS | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "processType": "CLAIM_RESOURCE", "remainingRound": 0, "targetNodeId": "S06"} |
| R90 | 01:30 | MED | 资源领取 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 在 五岭山道(S06) 领取冰鉴 |
| R90 | 01:30 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.8, "before": 93.88, "loss": 0.07500000000000001, "playerId": 2735} |
| R91 | 01:31 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 34000, "edgeProgressPermille": 724, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.7246376811594203, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R91 | 01:31 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 94.92, "before": 95.0, "loss": 0.0825, "playerId": 2707} |
| R91 | 01:31 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 1000, "edgeProgressPermille": 9, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.009856003784705454, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R91 | 01:31 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.7, "before": 93.8, "loss": 0.10500000000000001, "playerId": 2735} |
| R92 | 01:32 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 2000, "edgeProgressPermille": 19, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.019712007569410907, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R92 | 01:32 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.6, "before": 93.7, "loss": 0.10500000000000001, "playerId": 2735} |
| R92 | 01:32 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 35000, "edgeProgressPermille": 745, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.7459505541346974, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R92 | 01:32 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 94.84, "before": 94.92, "loss": 0.0825, "playerId": 2707} |
| R93 | 01:33 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 3000, "edgeProgressPermille": 29, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.02956801135411636, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R93 | 01:33 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.49, "before": 93.6, "loss": 0.10500000000000001, "playerId": 2735} |
| R93 | 01:33 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 36000, "edgeProgressPermille": 767, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.7672634271099744, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R93 | 01:33 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 94.76, "before": 94.84, "loss": 0.0825, "playerId": 2707} |
| R94 | 01:34 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 37000, "edgeProgressPermille": 788, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.7885763000852515, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R94 | 01:34 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 94.68, "before": 94.76, "loss": 0.0825, "playerId": 2707} |
| R94 | 01:34 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 4000, "edgeProgressPermille": 39, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.039424015138821815, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R94 | 01:34 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.38, "before": 93.49, "loss": 0.10500000000000001, "playerId": 2735} |
| R95 | 01:35 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 38000, "edgeProgressPermille": 809, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.8098891730605285, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R95 | 01:35 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 94.6, "before": 94.68, "loss": 0.0825, "playerId": 2707} |
| R95 | 01:35 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 5000, "edgeProgressPermille": 49, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.04928001892352726, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R95 | 01:35 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.27, "before": 93.38, "loss": 0.10500000000000001, "playerId": 2735} |
| R96 | 01:36 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 6000, "edgeProgressPermille": 59, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.05913602270823272, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R96 | 01:36 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.16, "before": 93.27, "loss": 0.10500000000000001, "playerId": 2735} |
| R96 | 01:36 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 39000, "edgeProgressPermille": 831, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.8312020460358056, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R96 | 01:36 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 94.52, "before": 94.6, "loss": 0.0825, "playerId": 2707} |
| R97 | 01:37 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 7000, "edgeProgressPermille": 68, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.06899202649293817, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R97 | 01:37 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.05, "before": 93.16, "loss": 0.10500000000000001, "playerId": 2735} |
| R97 | 01:37 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 40000, "edgeProgressPermille": 852, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.8525149190110827, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R97 | 01:37 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 94.44, "before": 94.52, "loss": 0.0825, "playerId": 2707} |
| R98 | 01:38 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 41000, "edgeProgressPermille": 873, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.8738277919863597, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R98 | 01:38 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 94.36, "before": 94.44, "loss": 0.0825, "playerId": 2707} |
| R98 | 01:38 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 8000, "edgeProgressPermille": 78, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.07884803027764363, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R98 | 01:38 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.95, "before": 93.05, "loss": 0.10500000000000001, "playerId": 2735} |
| R99 | 01:39 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 42000, "edgeProgressPermille": 895, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.8951406649616368, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R99 | 01:39 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 94.28, "before": 94.36, "loss": 0.0825, "playerId": 2707} |
| R99 | 01:39 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 9000, "edgeProgressPermille": 88, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.08870403406234909, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R99 | 01:39 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.85, "before": 92.95, "loss": 0.10500000000000001, "playerId": 2735} |
| R100 | 01:40 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 10000, "edgeProgressPermille": 98, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.09856003784705453, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R100 | 01:40 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.74, "before": 92.85, "loss": 0.10500000000000001, "playerId": 2735} |
| R100 | 01:40 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 43000, "edgeProgressPermille": 916, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.9164535379369139, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R100 | 01:40 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 94.2, "before": 94.28, "loss": 0.0825, "playerId": 2707} |
| R100 | 01:40 | MED | 任务刷新 |  | T_006 刷新在 江南码头(S04)，路线 WATER，截止 R320 |
| R100 | 01:40 | MED | 任务刷新 |  | T_007 刷新在 荆襄大驿(S07)，路线 ROAD，截止 R320 |
| R100 | 01:40 | MED | 任务刷新 |  | T_008 刷新在 洛阳驿(S09)，路线 WATER，截止 R320 |
| R100 | 01:40 | MED | 任务刷新 |  | T_009 刷新在 秦岭栈道(S08)，路线 MOUNTAIN，截止 R320 |
| R101 | 01:41 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 11000, "edgeProgressPermille": 108, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.10841604163175998, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R101 | 01:41 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.63, "before": 92.74, "loss": 0.10500000000000001, "playerId": 2735} |
| R101 | 01:41 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 44000, "edgeProgressPermille": 937, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.9377664109121909, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R101 | 01:41 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 94.12, "before": 94.2, "loss": 0.0825, "playerId": 2707} |
| R102 | 01:42 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 45000, "edgeProgressPermille": 959, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.959079283887468, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R102 | 01:42 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 94.04, "before": 94.12, "loss": 0.0825, "playerId": 2707} |
| R102 | 01:42 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 12000, "edgeProgressPermille": 118, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.11827204541646544, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R102 | 01:42 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.52, "before": 92.63, "loss": 0.10500000000000001, "playerId": 2735} |
| R103 | 01:43 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 46000, "edgeProgressPermille": 980, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 0.9803921568627451, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R103 | 01:43 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 93.96, "before": 94.04, "loss": 0.0825, "playerId": 2707} |
| R103 | 01:43 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 13000, "edgeProgressPermille": 128, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.1281280492011709, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R103 | 01:43 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.41, "before": 92.52, "loss": 0.10500000000000001, "playerId": 2735} |
| R104 | 01:44 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 14000, "edgeProgressPermille": 137, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.13798405298587635, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R104 | 01:44 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.3, "before": 92.41, "loss": 0.10500000000000001, "playerId": 2735} |
| R104 | 01:44 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 46920, "edgeProgressPermille": 1000, "edgeTotalMs": 46920, "fromNodeId": "S02", "playerId": 2707, "progress": 1.0, "routeEdgeId": "E01", "toNodeId": "S01"} |
| R104 | 01:44 | HIGH | 进点 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 进入 岭南果园(S01) |
| R104 | 01:44 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 93.88, "before": 93.96, "loss": 0.0825, "playerId": 2707} |
| R105 | 01:45 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 15000, "edgeProgressPermille": 147, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.1478400567705818, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R105 | 01:45 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.2, "before": 92.3, "loss": 0.10500000000000001, "playerId": 2735} |
| R105 | 01:45 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 12, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.012484394506866416, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R105 | 01:45 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 93.77, "before": 93.88, "loss": 0.10500000000000001, "playerId": 2707} |
| R106 | 01:46 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 24, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.024968789013732832, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R106 | 01:46 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 93.66, "before": 93.77, "loss": 0.10500000000000001, "playerId": 2707} |
| R106 | 01:46 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 16000, "edgeProgressPermille": 157, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.15769606055528726, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R106 | 01:46 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.1, "before": 92.2, "loss": 0.10500000000000001, "playerId": 2735} |
| R107 | 01:47 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 37, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.03745318352059925, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R107 | 01:47 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 93.55, "before": 93.66, "loss": 0.10500000000000001, "playerId": 2707} |
| R107 | 01:47 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 17000, "edgeProgressPermille": 167, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.1675520643399927, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R107 | 01:47 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.99, "before": 92.1, "loss": 0.10500000000000001, "playerId": 2735} |
| R108 | 01:48 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 18000, "edgeProgressPermille": 177, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.17740806812469817, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R108 | 01:48 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.88, "before": 91.99, "loss": 0.10500000000000001, "playerId": 2735} |
| R108 | 01:48 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 49, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.049937578027465665, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R108 | 01:48 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 93.45, "before": 93.55, "loss": 0.10500000000000001, "playerId": 2707} |
| R109 | 01:49 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 19000, "edgeProgressPermille": 187, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.1872640719094036, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R109 | 01:49 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.77, "before": 91.88, "loss": 0.10500000000000001, "playerId": 2735} |
| R109 | 01:49 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 62, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.062421972534332085, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R109 | 01:49 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 93.35, "before": 93.45, "loss": 0.10500000000000001, "playerId": 2707} |
| R110 | 01:50 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 74, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.0749063670411985, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R110 | 01:50 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 93.24, "before": 93.35, "loss": 0.10500000000000001, "playerId": 2707} |
| R110 | 01:50 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 20000, "edgeProgressPermille": 197, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.19712007569410905, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R110 | 01:50 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.66, "before": 91.77, "loss": 0.10500000000000001, "playerId": 2735} |
| R111 | 01:51 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 87, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.08739076154806492, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R111 | 01:51 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 93.13, "before": 93.24, "loss": 0.10500000000000001, "playerId": 2707} |
| R111 | 01:51 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 21000, "edgeProgressPermille": 206, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.20697607947881452, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R111 | 01:51 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.55, "before": 91.66, "loss": 0.10500000000000001, "playerId": 2735} |
| R112 | 01:52 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 22000, "edgeProgressPermille": 216, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.21683208326351996, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R112 | 01:52 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.45, "before": 91.55, "loss": 0.10500000000000001, "playerId": 2735} |
| R112 | 01:52 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 99, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.09987515605493133, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R112 | 01:52 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 93.02, "before": 93.13, "loss": 0.10500000000000001, "playerId": 2707} |
| R113 | 01:53 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 23000, "edgeProgressPermille": 226, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.22668808704822543, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R113 | 01:53 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.35, "before": 91.45, "loss": 0.10500000000000001, "playerId": 2735} |
| R113 | 01:53 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 112, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.11235955056179775, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R113 | 01:53 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 92.91, "before": 93.02, "loss": 0.10500000000000001, "playerId": 2707} |
| R114 | 01:54 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 124, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.12484394506866417, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R114 | 01:54 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 92.8, "before": 92.91, "loss": 0.10500000000000001, "playerId": 2707} |
| R114 | 01:54 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 24000, "edgeProgressPermille": 236, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.23654409083293088, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R114 | 01:54 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.24, "before": 91.35, "loss": 0.10500000000000001, "playerId": 2735} |
| R115 | 01:55 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 137, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.1373283395755306, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R115 | 01:55 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 92.7, "before": 92.8, "loss": 0.10500000000000001, "playerId": 2707} |
| R115 | 01:55 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 25000, "edgeProgressPermille": 246, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.24640009461763634, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R115 | 01:55 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.13, "before": 91.24, "loss": 0.10500000000000001, "playerId": 2735} |
| R116 | 01:56 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 26000, "edgeProgressPermille": 256, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.2562560984023418, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R116 | 01:56 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.02, "before": 91.13, "loss": 0.10500000000000001, "playerId": 2735} |
| R116 | 01:56 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 12000, "edgeProgressPermille": 149, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.149812734082397, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R116 | 01:56 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 92.6, "before": 92.7, "loss": 0.10500000000000001, "playerId": 2707} |
| R117 | 01:57 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 27000, "edgeProgressPermille": 266, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.26611210218704723, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R117 | 01:57 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.91, "before": 91.02, "loss": 0.10500000000000001, "playerId": 2735} |
| R117 | 01:57 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 13000, "edgeProgressPermille": 162, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.16229712858926343, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R117 | 01:57 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 92.49, "before": 92.6, "loss": 0.10500000000000001, "playerId": 2707} |
| R118 | 01:58 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 174, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.17478152309612985, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R118 | 01:58 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 92.38, "before": 92.49, "loss": 0.10500000000000001, "playerId": 2707} |
| R118 | 01:58 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 28000, "edgeProgressPermille": 275, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.2759681059717527, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R118 | 01:58 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.8, "before": 90.91, "loss": 0.10500000000000001, "playerId": 2735} |
| R119 | 01:59 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 15000, "edgeProgressPermille": 187, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.18726591760299627, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R119 | 01:59 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 92.27, "before": 92.38, "loss": 0.10500000000000001, "playerId": 2707} |
| R119 | 01:59 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 29000, "edgeProgressPermille": 285, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.28582410975645817, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R119 | 01:59 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.7, "before": 90.8, "loss": 0.10500000000000001, "playerId": 2735} |
| R120 | 02:00 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 30000, "edgeProgressPermille": 295, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.2956801135411636, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R120 | 02:00 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.6, "before": 90.7, "loss": 0.10500000000000001, "playerId": 2735} |
| R120 | 02:00 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 16000, "edgeProgressPermille": 199, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.19975031210986266, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R120 | 02:00 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 92.16, "before": 92.27, "loss": 0.10500000000000001, "playerId": 2707} |
| R121 | 02:01 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 31000, "edgeProgressPermille": 305, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.30553611732586905, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R121 | 02:01 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.49, "before": 90.6, "loss": 0.10500000000000001, "playerId": 2735} |
| R121 | 02:01 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 17000, "edgeProgressPermille": 212, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.21223470661672908, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R121 | 02:01 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 92.05, "before": 92.16, "loss": 0.10500000000000001, "playerId": 2707} |
| R122 | 02:02 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 18000, "edgeProgressPermille": 224, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.2247191011235955, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R122 | 02:02 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 91.95, "before": 92.05, "loss": 0.10500000000000001, "playerId": 2707} |
| R122 | 02:02 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 32000, "edgeProgressPermille": 315, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.3153921211105745, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R122 | 02:02 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.38, "before": 90.49, "loss": 0.10500000000000001, "playerId": 2735} |
| R123 | 02:03 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 19000, "edgeProgressPermille": 237, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.23720349563046192, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R123 | 02:03 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 91.85, "before": 91.95, "loss": 0.10500000000000001, "playerId": 2707} |
| R123 | 02:03 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 33000, "edgeProgressPermille": 325, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.32524812489527993, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R123 | 02:03 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.27, "before": 90.38, "loss": 0.10500000000000001, "playerId": 2735} |
| R124 | 02:04 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 34000, "edgeProgressPermille": 335, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.3351041286799854, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R124 | 02:04 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.16, "before": 90.27, "loss": 0.10500000000000001, "playerId": 2735} |
| R124 | 02:04 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 20000, "edgeProgressPermille": 249, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.24968789013732834, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R124 | 02:04 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 91.74, "before": 91.85, "loss": 0.10500000000000001, "playerId": 2707} |
| R125 | 02:05 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 35000, "edgeProgressPermille": 344, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.34496013246469087, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R125 | 02:05 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.05, "before": 90.16, "loss": 0.10500000000000001, "playerId": 2735} |
| R125 | 02:05 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 21000, "edgeProgressPermille": 262, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.26217228464419473, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R125 | 02:05 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 91.63, "before": 91.74, "loss": 0.10500000000000001, "playerId": 2707} |
| R126 | 02:06 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 22000, "edgeProgressPermille": 274, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.2746566791510612, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R126 | 02:06 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 91.52, "before": 91.63, "loss": 0.10500000000000001, "playerId": 2707} |
| R126 | 02:06 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 36000, "edgeProgressPermille": 354, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.35481613624939634, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R126 | 02:06 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.95, "before": 90.05, "loss": 0.10500000000000001, "playerId": 2735} |
| R126 | 02:06 | HIGH | 果品折损 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 好果跌破阈值 90，坏果 1 |
| R127 | 02:07 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 23000, "edgeProgressPermille": 287, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.28714107365792757, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R127 | 02:07 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 91.41, "before": 91.52, "loss": 0.10500000000000001, "playerId": 2707} |
| R127 | 02:07 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 37000, "edgeProgressPermille": 364, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.36467214003410175, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R127 | 02:07 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.85, "before": 89.95, "loss": 0.10500000000000001, "playerId": 2735} |
| R128 | 02:08 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 38000, "edgeProgressPermille": 374, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.3745281438188072, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R128 | 02:08 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.74, "before": 89.85, "loss": 0.10500000000000001, "playerId": 2735} |
| R128 | 02:08 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 24000, "edgeProgressPermille": 299, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.299625468164794, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R128 | 02:08 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 91.3, "before": 91.41, "loss": 0.10500000000000001, "playerId": 2707} |
| R129 | 02:09 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 39000, "edgeProgressPermille": 384, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.3843841476035127, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R129 | 02:09 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.63, "before": 89.74, "loss": 0.10500000000000001, "playerId": 2735} |
| R129 | 02:09 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 25000, "edgeProgressPermille": 312, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.3121098626716604, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R129 | 02:09 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 91.2, "before": 91.3, "loss": 0.10500000000000001, "playerId": 2707} |
| R130 | 02:10 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 26000, "edgeProgressPermille": 324, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.32459425717852686, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R130 | 02:10 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 91.1, "before": 91.2, "loss": 0.10500000000000001, "playerId": 2707} |
| R130 | 02:10 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 40000, "edgeProgressPermille": 394, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.3942401513882181, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R130 | 02:10 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.52, "before": 89.63, "loss": 0.10500000000000001, "playerId": 2735} |
| R131 | 02:11 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 27000, "edgeProgressPermille": 337, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.33707865168539325, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R131 | 02:11 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 90.99, "before": 91.1, "loss": 0.10500000000000001, "playerId": 2707} |
| R131 | 02:11 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 41000, "edgeProgressPermille": 404, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.4040961551729236, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R131 | 02:11 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.41, "before": 89.52, "loss": 0.10500000000000001, "playerId": 2735} |
| R132 | 02:12 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 42000, "edgeProgressPermille": 413, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.41395215895762905, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R132 | 02:12 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.3, "before": 89.41, "loss": 0.10500000000000001, "playerId": 2735} |
| R132 | 02:12 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 28000, "edgeProgressPermille": 349, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.3495630461922597, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R132 | 02:12 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 90.88, "before": 90.99, "loss": 0.10500000000000001, "playerId": 2707} |
| R133 | 02:13 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 43000, "edgeProgressPermille": 423, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.4238081627423345, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R133 | 02:13 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.2, "before": 89.3, "loss": 0.10500000000000001, "playerId": 2735} |
| R133 | 02:13 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 29000, "edgeProgressPermille": 362, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.3620474406991261, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R133 | 02:13 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 90.77, "before": 90.88, "loss": 0.10500000000000001, "playerId": 2707} |
| R134 | 02:14 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 30000, "edgeProgressPermille": 374, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.37453183520599254, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R134 | 02:14 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 90.66, "before": 90.77, "loss": 0.10500000000000001, "playerId": 2707} |
| R134 | 02:14 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 44000, "edgeProgressPermille": 433, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.43366416652703993, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R134 | 02:14 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.1, "before": 89.2, "loss": 0.10500000000000001, "playerId": 2735} |
| R135 | 02:15 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 31000, "edgeProgressPermille": 387, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.38701622971285893, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R135 | 02:15 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 90.55, "before": 90.66, "loss": 0.10500000000000001, "playerId": 2707} |
| R135 | 02:15 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 45000, "edgeProgressPermille": 443, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.4435201703117454, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R135 | 02:15 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.99, "before": 89.1, "loss": 0.10500000000000001, "playerId": 2735} |
| R136 | 02:16 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 46000, "edgeProgressPermille": 453, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.45337617409645087, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R136 | 02:16 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.88, "before": 88.99, "loss": 0.10500000000000001, "playerId": 2735} |
| R136 | 02:16 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 32000, "edgeProgressPermille": 399, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.3995006242197253, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R136 | 02:16 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 90.45, "before": 90.55, "loss": 0.10500000000000001, "playerId": 2707} |
| R137 | 02:17 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 47000, "edgeProgressPermille": 463, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.4632321778811563, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R137 | 02:17 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.77, "before": 88.88, "loss": 0.10500000000000001, "playerId": 2735} |
| R137 | 02:17 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 33000, "edgeProgressPermille": 411, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.41198501872659177, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R137 | 02:17 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 90.35, "before": 90.45, "loss": 0.10500000000000001, "playerId": 2707} |
| R138 | 02:18 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 34000, "edgeProgressPermille": 424, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.42446941323345816, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R138 | 02:18 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 90.24, "before": 90.35, "loss": 0.10500000000000001, "playerId": 2707} |
| R138 | 02:18 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 48000, "edgeProgressPermille": 473, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.47308818166586175, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R138 | 02:18 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.66, "before": 88.77, "loss": 0.10500000000000001, "playerId": 2735} |
| R139 | 02:19 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 35000, "edgeProgressPermille": 436, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.4369538077403246, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R139 | 02:19 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 90.13, "before": 90.24, "loss": 0.10500000000000001, "playerId": 2707} |
| R139 | 02:19 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 49000, "edgeProgressPermille": 482, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.4829441854505672, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R139 | 02:19 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.55, "before": 88.66, "loss": 0.10500000000000001, "playerId": 2735} |
| R140 | 02:20 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 50000, "edgeProgressPermille": 492, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.4928001892352727, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R140 | 02:20 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.45, "before": 88.55, "loss": 0.10500000000000001, "playerId": 2735} |
| R140 | 02:20 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 36000, "edgeProgressPermille": 449, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.449438202247191, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R140 | 02:20 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 90.02, "before": 90.13, "loss": 0.10500000000000001, "playerId": 2707} |
| R141 | 02:21 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 51000, "edgeProgressPermille": 502, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.5026561930199781, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R141 | 02:21 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.35, "before": 88.45, "loss": 0.10500000000000001, "playerId": 2735} |
| R141 | 02:21 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 37000, "edgeProgressPermille": 461, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.46192259675405745, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R141 | 02:21 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 89.91, "before": 90.02, "loss": 0.10500000000000001, "playerId": 2707} |
| R141 | 02:21 | HIGH | 果品折损 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 好果跌破阈值 90，坏果 1 |
| R142 | 02:22 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 38000, "edgeProgressPermille": 474, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.47440699126092384, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R142 | 02:22 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 89.8, "before": 89.91, "loss": 0.10500000000000001, "playerId": 2707} |
| R142 | 02:22 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 52000, "edgeProgressPermille": 512, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.5125121968046836, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R142 | 02:22 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.24, "before": 88.35, "loss": 0.10500000000000001, "playerId": 2735} |
| R143 | 02:23 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 39000, "edgeProgressPermille": 486, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.4868913857677903, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R143 | 02:23 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 89.7, "before": 89.8, "loss": 0.10500000000000001, "playerId": 2707} |
| R143 | 02:23 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 53000, "edgeProgressPermille": 522, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.522368200589389, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R143 | 02:23 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.13, "before": 88.24, "loss": 0.10500000000000001, "playerId": 2735} |
| R144 | 02:24 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 54000, "edgeProgressPermille": 532, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.5322242043740945, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R144 | 02:24 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.02, "before": 88.13, "loss": 0.10500000000000001, "playerId": 2735} |
| R144 | 02:24 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 40000, "edgeProgressPermille": 499, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.4993757802746567, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R144 | 02:24 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 89.6, "before": 89.7, "loss": 0.10500000000000001, "playerId": 2707} |
| R145 | 02:25 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 55000, "edgeProgressPermille": 542, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.5420802081588, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R145 | 02:25 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.91, "before": 88.02, "loss": 0.10500000000000001, "playerId": 2735} |
| R145 | 02:25 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 41000, "edgeProgressPermille": 511, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5118601747815231, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R145 | 02:25 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 89.49, "before": 89.6, "loss": 0.10500000000000001, "playerId": 2707} |
| R146 | 02:26 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 42000, "edgeProgressPermille": 524, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5243445692883895, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R146 | 02:26 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 89.38, "before": 89.49, "loss": 0.10500000000000001, "playerId": 2707} |
| R146 | 02:26 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 56000, "edgeProgressPermille": 551, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.5519362119435054, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R146 | 02:26 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.8, "before": 87.91, "loss": 0.10500000000000001, "playerId": 2735} |
| R147 | 02:27 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 43000, "edgeProgressPermille": 536, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5368289637952559, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R147 | 02:27 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 89.27, "before": 89.38, "loss": 0.10500000000000001, "playerId": 2707} |
| R147 | 02:27 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 57000, "edgeProgressPermille": 561, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.5617922157282108, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R147 | 02:27 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.7, "before": 87.8, "loss": 0.10500000000000001, "playerId": 2735} |
| R148 | 02:28 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 58000, "edgeProgressPermille": 571, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.5716482195129163, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R148 | 02:28 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.63, "before": 87.7, "loss": 0.07, "playerId": 2735} |
| R148 | 02:28 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 44000, "edgeProgressPermille": 549, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5493133583021224, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R148 | 02:28 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 89.2, "before": 89.27, "loss": 0.07, "playerId": 2707} |
| R149 | 02:29 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 59000, "edgeProgressPermille": 581, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.5815042232976217, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R149 | 02:29 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.56, "before": 87.63, "loss": 0.07, "playerId": 2735} |
| R149 | 02:29 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 45000, "edgeProgressPermille": 561, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5617977528089888, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R149 | 02:29 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 89.13, "before": 89.2, "loss": 0.07, "playerId": 2707} |
| R150 | 02:30 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 46000, "edgeProgressPermille": 574, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5742821473158551, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R150 | 02:30 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 89.06, "before": 89.13, "loss": 0.07, "playerId": 2707} |
| R150 | 02:30 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 60000, "edgeProgressPermille": 591, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.5913602270823272, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R150 | 02:30 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.49, "before": 87.56, "loss": 0.07, "playerId": 2735} |
| R151 | 02:31 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 47000, "edgeProgressPermille": 586, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5867665418227216, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R151 | 02:31 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 88.99, "before": 89.06, "loss": 0.07, "playerId": 2707} |
| R151 | 02:31 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 61000, "edgeProgressPermille": 601, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.6012162308670327, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R151 | 02:31 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.42, "before": 87.49, "loss": 0.07, "playerId": 2735} |
| R152 | 02:32 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 62000, "edgeProgressPermille": 611, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.6110722346517381, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R152 | 02:32 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.35, "before": 87.42, "loss": 0.07, "playerId": 2735} |
| R152 | 02:32 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 48000, "edgeProgressPermille": 599, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.599250936329588, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R152 | 02:32 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 88.92, "before": 88.99, "loss": 0.07, "playerId": 2707} |
| R153 | 02:33 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 63000, "edgeProgressPermille": 620, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.6209282384364435, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R153 | 02:33 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.28, "before": 87.35, "loss": 0.07, "playerId": 2735} |
| R153 | 02:33 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 49000, "edgeProgressPermille": 611, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6117353308364545, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R153 | 02:33 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 88.85, "before": 88.92, "loss": 0.07, "playerId": 2707} |
| R154 | 02:34 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 50000, "edgeProgressPermille": 624, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6242197253433208, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R154 | 02:34 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 88.78, "before": 88.85, "loss": 0.07, "playerId": 2707} |
| R154 | 02:34 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 64000, "edgeProgressPermille": 630, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.630784242221149, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R154 | 02:34 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.21, "before": 87.28, "loss": 0.07, "playerId": 2735} |
| R155 | 02:35 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 51000, "edgeProgressPermille": 636, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6367041198501873, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R155 | 02:35 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 88.71, "before": 88.78, "loss": 0.07, "playerId": 2707} |
| R155 | 02:35 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 65000, "edgeProgressPermille": 640, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.6406402460058545, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R155 | 02:35 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.14, "before": 87.21, "loss": 0.07, "playerId": 2735} |
| R156 | 02:36 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 66000, "edgeProgressPermille": 650, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.6504962497905599, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R156 | 02:36 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.07, "before": 87.14, "loss": 0.07, "playerId": 2735} |
| R156 | 02:36 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 52000, "edgeProgressPermille": 649, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6491885143570537, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R156 | 02:36 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 88.64, "before": 88.71, "loss": 0.07, "playerId": 2707} |
| R157 | 02:37 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 67000, "edgeProgressPermille": 660, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.6603522535752654, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R157 | 02:37 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.0, "before": 87.07, "loss": 0.07, "playerId": 2735} |
| R157 | 02:37 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 53000, "edgeProgressPermille": 661, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.66167290886392, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R157 | 02:37 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 88.57, "before": 88.64, "loss": 0.07, "playerId": 2707} |
| R158 | 02:38 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 54000, "edgeProgressPermille": 674, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6741573033707865, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R158 | 02:38 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 88.5, "before": 88.57, "loss": 0.07, "playerId": 2707} |
| R158 | 02:38 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 68000, "edgeProgressPermille": 670, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.6702082573599708, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R158 | 02:38 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.93, "before": 87.0, "loss": 0.07, "playerId": 2735} |
| R159 | 02:39 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 55000, "edgeProgressPermille": 686, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.686641697877653, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R159 | 02:39 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 88.43, "before": 88.5, "loss": 0.07, "playerId": 2707} |
| R159 | 02:39 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 69000, "edgeProgressPermille": 680, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.6800642611446763, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R159 | 02:39 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.86, "before": 86.93, "loss": 0.07, "playerId": 2735} |
| R160 | 02:40 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 70000, "edgeProgressPermille": 689, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.6899202649293817, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R160 | 02:40 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.79, "before": 86.86, "loss": 0.07, "playerId": 2735} |
| R160 | 02:40 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 56000, "edgeProgressPermille": 699, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6991260923845194, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R160 | 02:40 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 88.36, "before": 88.43, "loss": 0.07, "playerId": 2707} |
| R161 | 02:41 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 71000, "edgeProgressPermille": 699, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.6997762687140872, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R161 | 02:41 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.72, "before": 86.79, "loss": 0.07, "playerId": 2735} |
| R161 | 02:41 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 57000, "edgeProgressPermille": 711, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7116104868913857, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R161 | 02:41 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 88.29, "before": 88.36, "loss": 0.07, "playerId": 2707} |
| R162 | 02:42 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 58000, "edgeProgressPermille": 724, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7240948813982522, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R162 | 02:42 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 88.22, "before": 88.29, "loss": 0.07, "playerId": 2707} |
| R162 | 02:42 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 72000, "edgeProgressPermille": 709, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.7096322724987927, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R162 | 02:42 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.65, "before": 86.72, "loss": 0.07, "playerId": 2735} |
| R163 | 02:43 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 59000, "edgeProgressPermille": 736, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7365792759051186, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R163 | 02:43 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 88.15, "before": 88.22, "loss": 0.07, "playerId": 2707} |
| R163 | 02:43 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 73000, "edgeProgressPermille": 719, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.7194882762834981, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R163 | 02:43 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.58, "before": 86.65, "loss": 0.07, "playerId": 2735} |
| R164 | 02:44 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 74000, "edgeProgressPermille": 729, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.7293442800682035, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R164 | 02:44 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.51, "before": 86.58, "loss": 0.07, "playerId": 2735} |
| R164 | 02:44 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 60000, "edgeProgressPermille": 749, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7490636704119851, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R164 | 02:44 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 88.08, "before": 88.15, "loss": 0.07, "playerId": 2707} |
| R165 | 02:45 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 75000, "edgeProgressPermille": 739, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.739200283852909, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R165 | 02:45 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.44, "before": 86.51, "loss": 0.07, "playerId": 2735} |
| R165 | 02:45 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 61000, "edgeProgressPermille": 761, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7615480649188514, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R165 | 02:45 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 88.01, "before": 88.08, "loss": 0.07, "playerId": 2707} |
| R166 | 02:46 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 62000, "edgeProgressPermille": 774, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7740324594257179, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R166 | 02:46 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 87.94, "before": 88.01, "loss": 0.07, "playerId": 2707} |
| R166 | 02:46 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 76000, "edgeProgressPermille": 749, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.7490562876376144, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R166 | 02:46 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.37, "before": 86.44, "loss": 0.07, "playerId": 2735} |
| R167 | 02:47 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 63000, "edgeProgressPermille": 786, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7865168539325843, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R167 | 02:47 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 87.87, "before": 87.94, "loss": 0.07, "playerId": 2707} |
| R167 | 02:47 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 77000, "edgeProgressPermille": 758, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.7589122914223199, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R167 | 02:47 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.3, "before": 86.37, "loss": 0.07, "playerId": 2735} |
| R168 | 02:48 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 78000, "edgeProgressPermille": 768, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.7687682952070254, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R168 | 02:48 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.23, "before": 86.3, "loss": 0.07, "playerId": 2735} |
| R168 | 02:48 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 64000, "edgeProgressPermille": 799, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7990012484394506, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R168 | 02:48 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 87.8, "before": 87.87, "loss": 0.07, "playerId": 2707} |
| R169 | 02:49 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 79000, "edgeProgressPermille": 778, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.7786242989917308, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R169 | 02:49 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.16, "before": 86.23, "loss": 0.07, "playerId": 2735} |
| R169 | 02:49 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 65000, "edgeProgressPermille": 811, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8114856429463171, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R169 | 02:49 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 87.73, "before": 87.8, "loss": 0.07, "playerId": 2707} |
| R170 | 02:50 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 66000, "edgeProgressPermille": 823, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8239700374531835, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R170 | 02:50 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 87.66, "before": 87.73, "loss": 0.07, "playerId": 2707} |
| R170 | 02:50 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 80000, "edgeProgressPermille": 788, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.7884803027764362, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R170 | 02:50 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.09, "before": 86.16, "loss": 0.07, "playerId": 2735} |
| R171 | 02:51 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 67000, "edgeProgressPermille": 836, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.83645443196005, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R171 | 02:51 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 87.59, "before": 87.66, "loss": 0.07, "playerId": 2707} |
| R171 | 02:51 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 81000, "edgeProgressPermille": 798, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.7983363065611417, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R171 | 02:51 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.02, "before": 86.09, "loss": 0.07, "playerId": 2735} |
| R172 | 02:52 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 82000, "edgeProgressPermille": 808, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.8081923103458472, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R172 | 02:52 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.95, "before": 86.02, "loss": 0.07, "playerId": 2735} |
| R172 | 02:52 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 68000, "edgeProgressPermille": 848, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8489388264669163, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R172 | 02:52 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 87.52, "before": 87.59, "loss": 0.07, "playerId": 2707} |
| R173 | 02:53 | HIGH | 派遣 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 派遣队伍侦察 秦岭栈道(S08)，预计 R188 完成 |
| R173 | 02:53 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 83000, "edgeProgressPermille": 818, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.8180483141305527, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R173 | 02:53 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.88, "before": 85.95, "loss": 0.07, "playerId": 2735} |
| R173 | 02:53 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 69000, "edgeProgressPermille": 861, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8614232209737828, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R173 | 02:53 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 87.45, "before": 87.52, "loss": 0.07, "playerId": 2707} |
| R174 | 02:54 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 70000, "edgeProgressPermille": 873, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8739076154806492, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R174 | 02:54 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 87.38, "before": 87.45, "loss": 0.07, "playerId": 2707} |
| R174 | 02:54 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 84000, "edgeProgressPermille": 827, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.8279043179152581, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R174 | 02:54 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.81, "before": 85.88, "loss": 0.07, "playerId": 2735} |
| R175 | 02:55 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 71000, "edgeProgressPermille": 886, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8863920099875156, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R175 | 02:55 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 87.31, "before": 87.38, "loss": 0.07, "playerId": 2707} |
| R175 | 02:55 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 85000, "edgeProgressPermille": 837, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.8377603216999635, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R175 | 02:55 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.74, "before": 85.81, "loss": 0.07, "playerId": 2735} |
| R176 | 02:56 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 86000, "edgeProgressPermille": 847, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.847616325484669, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R176 | 02:56 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.67, "before": 85.74, "loss": 0.07, "playerId": 2735} |
| R176 | 02:56 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 72000, "edgeProgressPermille": 898, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.898876404494382, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R176 | 02:56 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 87.24, "before": 87.31, "loss": 0.07, "playerId": 2707} |
| R177 | 02:57 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 87000, "edgeProgressPermille": 857, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.8574723292693744, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R177 | 02:57 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.6, "before": 85.67, "loss": 0.07, "playerId": 2735} |
| R177 | 02:57 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 73000, "edgeProgressPermille": 911, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9113607990012484, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R177 | 02:57 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 87.17, "before": 87.24, "loss": 0.07, "playerId": 2707} |
| R178 | 02:58 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 74000, "edgeProgressPermille": 923, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9238451935081149, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R178 | 02:58 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 87.1, "before": 87.17, "loss": 0.07, "playerId": 2707} |
| R178 | 02:58 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 88000, "edgeProgressPermille": 867, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.8673283330540799, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R178 | 02:58 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.53, "before": 85.6, "loss": 0.07, "playerId": 2735} |
| R179 | 02:59 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 75000, "edgeProgressPermille": 936, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9363295880149812, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R179 | 02:59 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 87.03, "before": 87.1, "loss": 0.07, "playerId": 2707} |
| R179 | 02:59 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 89000, "edgeProgressPermille": 877, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.8771843368387854, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R179 | 02:59 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.46, "before": 85.53, "loss": 0.07, "playerId": 2735} |
| R180 | 03:00 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 90000, "edgeProgressPermille": 887, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.8870403406234908, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R180 | 03:00 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.39, "before": 85.46, "loss": 0.07, "playerId": 2735} |
| R180 | 03:00 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 76000, "edgeProgressPermille": 948, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9488139825218477, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R180 | 03:00 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 86.96, "before": 87.03, "loss": 0.07, "playerId": 2707} |
| R181 | 03:01 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 91000, "edgeProgressPermille": 896, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.8968963444081962, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R181 | 03:01 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.32, "before": 85.39, "loss": 0.07, "playerId": 2735} |
| R181 | 03:01 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 77000, "edgeProgressPermille": 961, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9612983770287141, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R181 | 03:01 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 86.89, "before": 86.96, "loss": 0.07, "playerId": 2707} |
| R182 | 03:02 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 78000, "edgeProgressPermille": 973, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9737827715355806, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R182 | 03:02 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 86.82, "before": 86.89, "loss": 0.07, "playerId": 2707} |
| R182 | 03:02 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 92000, "edgeProgressPermille": 906, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.9067523481929017, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R182 | 03:02 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.25, "before": 85.32, "loss": 0.07, "playerId": 2735} |
| R183 | 03:03 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 79000, "edgeProgressPermille": 986, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9862671660424469, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R183 | 03:03 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 86.75, "before": 86.82, "loss": 0.07, "playerId": 2707} |
| R183 | 03:03 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 93000, "edgeProgressPermille": 916, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.9166083519776071, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R183 | 03:03 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.18, "before": 85.25, "loss": 0.07, "playerId": 2735} |
| R184 | 03:04 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 94000, "edgeProgressPermille": 926, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.9264643557623126, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R184 | 03:04 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.11, "before": 85.18, "loss": 0.07, "playerId": 2735} |
| R184 | 03:04 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 80000, "edgeProgressPermille": 998, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9987515605493134, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R184 | 03:04 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 86.68, "before": 86.75, "loss": 0.07, "playerId": 2707} |
| R185 | 03:05 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 95000, "edgeProgressPermille": 936, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.9363203595470181, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R185 | 03:05 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.04, "before": 85.11, "loss": 0.07, "playerId": 2735} |
| R185 | 03:05 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 80100, "edgeProgressPermille": 1000, "edgeTotalMs": 80100, "fromNodeId": "S01", "playerId": 2707, "progress": 1.0, "routeEdgeId": "E15", "toNodeId": "S06"} |
| R185 | 03:05 | HIGH | 进点 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 进入 五岭山道(S06) |
| R185 | 03:05 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 86.61, "before": 86.68, "loss": 0.07, "playerId": 2707} |
| R186 | 03:06 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 12, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.012484394506866416, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R186 | 03:06 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 86.54, "before": 86.61, "loss": 0.07, "playerId": 2707} |
| R186 | 03:06 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 96000, "edgeProgressPermille": 946, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.9461763633317235, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R186 | 03:06 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.97, "before": 85.04, "loss": 0.07, "playerId": 2735} |
| R187 | 03:07 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 24, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.024968789013732832, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R187 | 03:07 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 86.47, "before": 86.54, "loss": 0.07, "playerId": 2707} |
| R187 | 03:07 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 97000, "edgeProgressPermille": 956, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.956032367116429, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R187 | 03:07 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.9, "before": 84.97, "loss": 0.07, "playerId": 2735} |
| R188 | 03:08 | MED | SCOUT_MARKER_ADD | BLUE 路人女主队/1.0(2735) | {"expireRound": 233, "playerId": 2735, "remainingTriggers": 1, "targetNodeId": "S08"} |
| R188 | 03:08 | MED | 侦察回报 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 侦察 秦岭栈道(S08)：无障碍，资源 短驿马、通关凭证 |
| R188 | 03:08 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 98000, "edgeProgressPermille": 965, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.9658883709011344, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R188 | 03:08 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.83, "before": 84.9, "loss": 0.07, "playerId": 2735} |
| R188 | 03:08 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 37, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.03745318352059925, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R188 | 03:08 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 86.4, "before": 86.47, "loss": 0.07, "playerId": 2707} |
| R189 | 03:09 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 99000, "edgeProgressPermille": 975, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.9757443746858399, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R189 | 03:09 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.76, "before": 84.83, "loss": 0.07, "playerId": 2735} |
| R189 | 03:09 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 49, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.049937578027465665, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R189 | 03:09 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 86.33, "before": 86.4, "loss": 0.07, "playerId": 2707} |
| R190 | 03:10 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 62, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.062421972534332085, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R190 | 03:10 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 86.26, "before": 86.33, "loss": 0.07, "playerId": 2707} |
| R190 | 03:10 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 100000, "edgeProgressPermille": 985, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.9856003784705454, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R190 | 03:10 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.69, "before": 84.76, "loss": 0.07, "playerId": 2735} |
| R191 | 03:11 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 74, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.0749063670411985, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R191 | 03:11 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 86.19, "before": 86.26, "loss": 0.07, "playerId": 2707} |
| R191 | 03:11 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 101000, "edgeProgressPermille": 995, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 0.9954563822552508, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R191 | 03:11 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.62, "before": 84.69, "loss": 0.07, "playerId": 2735} |
| R192 | 03:12 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 101461, "edgeProgressPermille": 1000, "edgeTotalMs": 101461, "fromNodeId": "S06", "playerId": 2735, "progress": 1.0, "routeEdgeId": "E16", "toNodeId": "S08"} |
| R192 | 03:12 | HIGH | 进点 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 进入 秦岭栈道(S08) |
| R192 | 03:12 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.55, "before": 84.62, "loss": 0.07, "playerId": 2735} |
| R192 | 03:12 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 87, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.08739076154806492, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R192 | 03:12 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 86.12, "before": 86.19, "loss": 0.07, "playerId": 2707} |
| R193 | 03:13 | MED | SCOUT_MARKER_APPLY | BLUE 路人女主队/1.0(2735) | {"afterRound": 2, "beforeRound": 4, "playerId": 2735, "processType": "CLAIM_TASK", "targetNodeId": "S08"} |
| R193 | 03:13 | MED | PROCESS_PROGRESS | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "processType": "CLAIM_TASK", "remainingRound": 1, "targetNodeId": "S08"} |
| R193 | 03:13 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.5, "before": 84.55, "loss": 0.05, "playerId": 2735} |
| R193 | 03:13 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 99, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.09987515605493133, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R193 | 03:13 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 86.05, "before": 86.12, "loss": 0.07, "playerId": 2707} |
| R194 | 03:14 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 112, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.11235955056179775, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R194 | 03:14 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 85.98, "before": 86.05, "loss": 0.07, "playerId": 2707} |
| R194 | 03:14 | MED | PROCESS_PROGRESS | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "processType": "CLAIM_TASK", "remainingRound": 0, "targetNodeId": "S08"} |
| R194 | 03:14 | HIGH | 任务完成 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 完成 栈道复核，+30 分，任务分 30 |
| R194 | 03:14 | MED | SCOUT_MARKER_CONSUME | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "remainingTriggers": 0, "targetNodeId": "S08"} |
| R194 | 03:14 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.45, "before": 84.5, "loss": 0.05, "playerId": 2735} |
| R195 | 03:15 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 124, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.12484394506866417, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R195 | 03:15 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 85.91, "before": 85.98, "loss": 0.07, "playerId": 2707} |
| R195 | 03:15 | MED | PROCESS_PROGRESS | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "processType": "CLAIM_TASK", "remainingRound": 3, "targetNodeId": "S08"} |
| R195 | 03:15 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.4, "before": 84.45, "loss": 0.05, "playerId": 2735} |
| R196 | 03:16 | MED | PROCESS_PROGRESS | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "processType": "CLAIM_TASK", "remainingRound": 2, "targetNodeId": "S08"} |
| R196 | 03:16 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.35, "before": 84.4, "loss": 0.05, "playerId": 2735} |
| R196 | 03:16 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 137, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.1373283395755306, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R196 | 03:16 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 85.84, "before": 85.91, "loss": 0.07, "playerId": 2707} |
| R197 | 03:17 | MED | PROCESS_PROGRESS | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "processType": "CLAIM_TASK", "remainingRound": 1, "targetNodeId": "S08"} |
| R197 | 03:17 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.3, "before": 84.35, "loss": 0.05, "playerId": 2735} |
| R197 | 03:17 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 12000, "edgeProgressPermille": 149, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.149812734082397, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R197 | 03:17 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 85.77, "before": 85.84, "loss": 0.07, "playerId": 2707} |
| R198 | 03:18 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 13000, "edgeProgressPermille": 162, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.16229712858926343, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R198 | 03:18 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 85.7, "before": 85.77, "loss": 0.07, "playerId": 2707} |
| R198 | 03:18 | MED | PROCESS_PROGRESS | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "processType": "CLAIM_TASK", "remainingRound": 0, "targetNodeId": "S08"} |
| R198 | 03:18 | HIGH | 任务完成 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 完成 栈道复核，+30 分，任务分 60 |
| R198 | 03:18 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.25, "before": 84.3, "loss": 0.05, "playerId": 2735} |
| R199 | 03:19 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 174, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.17478152309612985, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R199 | 03:19 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 85.63, "before": 85.7, "loss": 0.07, "playerId": 2707} |
| R199 | 03:19 | HIGH | 资源使用 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 使用冰鉴，状态 84.25->94.25 |
| R199 | 03:19 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.2, "before": 94.25, "loss": 0.05, "playerId": 2735} |
| R200 | 03:20 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 1000, "edgeProgressPermille": 7, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.007168458781362007, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R200 | 03:20 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.14, "before": 94.2, "loss": 0.065, "playerId": 2735} |
| R200 | 03:20 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 15000, "edgeProgressPermille": 187, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.18726591760299627, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R200 | 03:20 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 85.56, "before": 85.63, "loss": 0.07, "playerId": 2707} |
| R200 | 03:20 | MED | 任务刷新 |  | T_010 刷新在 洞庭水驿(S05)，路线 WATER，截止 R420 |
| R200 | 03:20 | MED | 任务刷新 |  | T_011 刷新在 江南码头(S04)，路线 WATER，截止 R420 |
| R200 | 03:20 | MED | 任务刷新 |  | T_012 刷新在 梅关驿(S03)，路线 ROAD，截止 R420 |
| R201 | 03:21 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 2000, "edgeProgressPermille": 14, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.014336917562724014, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R201 | 03:21 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.08, "before": 94.14, "loss": 0.065, "playerId": 2735} |
| R201 | 03:21 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 16000, "edgeProgressPermille": 199, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.19975031210986266, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R201 | 03:21 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 85.49, "before": 85.56, "loss": 0.07, "playerId": 2707} |
| R202 | 03:22 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 17000, "edgeProgressPermille": 212, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.21223470661672908, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R202 | 03:22 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 85.42, "before": 85.49, "loss": 0.07, "playerId": 2707} |
| R202 | 03:22 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 3000, "edgeProgressPermille": 21, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.021505376344086023, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R202 | 03:22 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 94.02, "before": 94.08, "loss": 0.065, "playerId": 2735} |
| R203 | 03:23 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 18000, "edgeProgressPermille": 224, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.2247191011235955, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R203 | 03:23 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 85.35, "before": 85.42, "loss": 0.07, "playerId": 2707} |
| R203 | 03:23 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 4000, "edgeProgressPermille": 28, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.02867383512544803, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R203 | 03:23 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.96, "before": 94.02, "loss": 0.065, "playerId": 2735} |
| R204 | 03:24 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 5000, "edgeProgressPermille": 35, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.035842293906810034, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R204 | 03:24 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.9, "before": 93.96, "loss": 0.065, "playerId": 2735} |
| R204 | 03:24 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 19000, "edgeProgressPermille": 237, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.23720349563046192, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R204 | 03:24 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 85.28, "before": 85.35, "loss": 0.07, "playerId": 2707} |
| R205 | 03:25 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 6000, "edgeProgressPermille": 43, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.043010752688172046, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R205 | 03:25 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.84, "before": 93.9, "loss": 0.065, "playerId": 2735} |
| R205 | 03:25 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 20000, "edgeProgressPermille": 249, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.24968789013732834, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R205 | 03:25 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 85.21, "before": 85.28, "loss": 0.07, "playerId": 2707} |
| R206 | 03:26 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 21000, "edgeProgressPermille": 262, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.26217228464419473, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R206 | 03:26 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 85.14, "before": 85.21, "loss": 0.07, "playerId": 2707} |
| R206 | 03:26 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 7000, "edgeProgressPermille": 50, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.05017921146953405, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R206 | 03:26 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.78, "before": 93.84, "loss": 0.065, "playerId": 2735} |
| R207 | 03:27 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 22000, "edgeProgressPermille": 274, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.2746566791510612, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R207 | 03:27 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 85.07, "before": 85.14, "loss": 0.07, "playerId": 2707} |
| R207 | 03:27 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 8000, "edgeProgressPermille": 57, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.05734767025089606, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R207 | 03:27 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.72, "before": 93.78, "loss": 0.065, "playerId": 2735} |
| R208 | 03:28 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 9000, "edgeProgressPermille": 64, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.06451612903225806, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R208 | 03:28 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.66, "before": 93.72, "loss": 0.065, "playerId": 2735} |
| R208 | 03:28 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 23000, "edgeProgressPermille": 287, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.28714107365792757, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R208 | 03:28 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 85.0, "before": 85.07, "loss": 0.07, "playerId": 2707} |
| R209 | 03:29 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 10000, "edgeProgressPermille": 71, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.07168458781362007, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R209 | 03:29 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.6, "before": 93.66, "loss": 0.065, "playerId": 2735} |
| R209 | 03:29 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 24000, "edgeProgressPermille": 299, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.299625468164794, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R209 | 03:29 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 84.93, "before": 85.0, "loss": 0.07, "playerId": 2707} |
| R210 | 03:30 | MED | 任务过期 |  | T_004 在 梅关驿(S03) 过期 |
| R210 | 03:30 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 25000, "edgeProgressPermille": 312, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.3121098626716604, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R210 | 03:30 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 84.86, "before": 84.93, "loss": 0.07, "playerId": 2707} |
| R210 | 03:30 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 11000, "edgeProgressPermille": 78, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.07885304659498207, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R210 | 03:30 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.54, "before": 93.6, "loss": 0.065, "playerId": 2735} |
| R211 | 03:31 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 26000, "edgeProgressPermille": 324, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.32459425717852686, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R211 | 03:31 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 84.79, "before": 84.86, "loss": 0.07, "playerId": 2707} |
| R211 | 03:31 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 12000, "edgeProgressPermille": 86, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.08602150537634409, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R211 | 03:31 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.48, "before": 93.54, "loss": 0.065, "playerId": 2735} |
| R212 | 03:32 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 13000, "edgeProgressPermille": 93, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.0931899641577061, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R212 | 03:32 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.42, "before": 93.48, "loss": 0.065, "playerId": 2735} |
| R212 | 03:32 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 27000, "edgeProgressPermille": 337, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.33707865168539325, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R212 | 03:32 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 84.72, "before": 84.79, "loss": 0.07, "playerId": 2707} |
| R213 | 03:33 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 14000, "edgeProgressPermille": 100, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.1003584229390681, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R213 | 03:33 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.36, "before": 93.42, "loss": 0.065, "playerId": 2735} |
| R213 | 03:33 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 28000, "edgeProgressPermille": 349, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.3495630461922597, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R213 | 03:33 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 84.65, "before": 84.72, "loss": 0.07, "playerId": 2707} |
| R214 | 03:34 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 29000, "edgeProgressPermille": 362, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.3620474406991261, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R214 | 03:34 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 84.58, "before": 84.65, "loss": 0.07, "playerId": 2707} |
| R214 | 03:34 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 15000, "edgeProgressPermille": 107, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.10752688172043011, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R214 | 03:34 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.3, "before": 93.36, "loss": 0.065, "playerId": 2735} |
| R215 | 03:35 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 30000, "edgeProgressPermille": 374, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.37453183520599254, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R215 | 03:35 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 84.51, "before": 84.58, "loss": 0.07, "playerId": 2707} |
| R215 | 03:35 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 16000, "edgeProgressPermille": 114, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.11469534050179211, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R215 | 03:35 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.24, "before": 93.3, "loss": 0.065, "playerId": 2735} |
| R216 | 03:36 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 17000, "edgeProgressPermille": 121, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.12186379928315412, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R216 | 03:36 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.18, "before": 93.24, "loss": 0.065, "playerId": 2735} |
| R216 | 03:36 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 31000, "edgeProgressPermille": 387, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.38701622971285893, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R216 | 03:36 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 84.44, "before": 84.51, "loss": 0.07, "playerId": 2707} |
| R217 | 03:37 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 18000, "edgeProgressPermille": 129, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.12903225806451613, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R217 | 03:37 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.12, "before": 93.18, "loss": 0.065, "playerId": 2735} |
| R217 | 03:37 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 32000, "edgeProgressPermille": 399, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.3995006242197253, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R217 | 03:37 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 84.37, "before": 84.44, "loss": 0.07, "playerId": 2707} |
| R218 | 03:38 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 33000, "edgeProgressPermille": 411, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.41198501872659177, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R218 | 03:38 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 84.3, "before": 84.37, "loss": 0.07, "playerId": 2707} |
| R218 | 03:38 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 19000, "edgeProgressPermille": 136, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.13620071684587814, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R218 | 03:38 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.06, "before": 93.12, "loss": 0.065, "playerId": 2735} |
| R219 | 03:39 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 34000, "edgeProgressPermille": 424, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.42446941323345816, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R219 | 03:39 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 84.23, "before": 84.3, "loss": 0.07, "playerId": 2707} |
| R219 | 03:39 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 20000, "edgeProgressPermille": 143, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.14336917562724014, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R219 | 03:39 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 93.0, "before": 93.06, "loss": 0.065, "playerId": 2735} |
| R220 | 03:40 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 21000, "edgeProgressPermille": 150, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.15053763440860216, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R220 | 03:40 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.94, "before": 93.0, "loss": 0.065, "playerId": 2735} |
| R220 | 03:40 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 35000, "edgeProgressPermille": 436, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.4369538077403246, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R220 | 03:40 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 84.16, "before": 84.23, "loss": 0.07, "playerId": 2707} |
| R221 | 03:41 | MED | 任务过期 |  | T_001 在 梅关驿(S03) 过期 |
| R221 | 03:41 | MED | 任务过期 |  | T_002 在 江南码头(S04) 过期 |
| R221 | 03:41 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 22000, "edgeProgressPermille": 157, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.15770609318996415, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R221 | 03:41 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.88, "before": 92.94, "loss": 0.065, "playerId": 2735} |
| R221 | 03:41 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 36000, "edgeProgressPermille": 449, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.449438202247191, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R221 | 03:41 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 84.09, "before": 84.16, "loss": 0.07, "playerId": 2707} |
| R222 | 03:42 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 37000, "edgeProgressPermille": 461, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.46192259675405745, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R222 | 03:42 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 84.02, "before": 84.09, "loss": 0.07, "playerId": 2707} |
| R222 | 03:42 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 23000, "edgeProgressPermille": 164, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.16487455197132617, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R222 | 03:42 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.82, "before": 92.88, "loss": 0.065, "playerId": 2735} |
| R223 | 03:43 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 38000, "edgeProgressPermille": 474, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.47440699126092384, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R223 | 03:43 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 83.95, "before": 84.02, "loss": 0.07, "playerId": 2707} |
| R223 | 03:43 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 24000, "edgeProgressPermille": 172, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.17204301075268819, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R223 | 03:43 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.76, "before": 92.82, "loss": 0.065, "playerId": 2735} |
| R224 | 03:44 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 25000, "edgeProgressPermille": 179, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.17921146953405018, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R224 | 03:44 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.7, "before": 92.76, "loss": 0.065, "playerId": 2735} |
| R224 | 03:44 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 39000, "edgeProgressPermille": 486, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.4868913857677903, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R224 | 03:44 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 83.88, "before": 83.95, "loss": 0.07, "playerId": 2707} |
| R225 | 03:45 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 26000, "edgeProgressPermille": 186, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.1863799283154122, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R225 | 03:45 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.64, "before": 92.7, "loss": 0.065, "playerId": 2735} |
| R225 | 03:45 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 40000, "edgeProgressPermille": 499, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.4993757802746567, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R225 | 03:45 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 83.81, "before": 83.88, "loss": 0.07, "playerId": 2707} |
| R226 | 03:46 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 41000, "edgeProgressPermille": 511, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5118601747815231, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R226 | 03:46 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 83.74, "before": 83.81, "loss": 0.07, "playerId": 2707} |
| R226 | 03:46 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 27000, "edgeProgressPermille": 193, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.1935483870967742, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R226 | 03:46 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.58, "before": 92.64, "loss": 0.065, "playerId": 2735} |
| R227 | 03:47 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 42000, "edgeProgressPermille": 524, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5243445692883895, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R227 | 03:47 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 83.67, "before": 83.74, "loss": 0.07, "playerId": 2707} |
| R227 | 03:47 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 28000, "edgeProgressPermille": 200, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.2007168458781362, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R227 | 03:47 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.52, "before": 92.58, "loss": 0.065, "playerId": 2735} |
| R228 | 03:48 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 29000, "edgeProgressPermille": 207, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.2078853046594982, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R228 | 03:48 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.46, "before": 92.52, "loss": 0.065, "playerId": 2735} |
| R228 | 03:48 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 43000, "edgeProgressPermille": 536, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5368289637952559, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R228 | 03:48 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 83.6, "before": 83.67, "loss": 0.07, "playerId": 2707} |
| R229 | 03:49 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 30000, "edgeProgressPermille": 215, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.21505376344086022, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R229 | 03:49 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.4, "before": 92.46, "loss": 0.065, "playerId": 2735} |
| R229 | 03:49 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 44000, "edgeProgressPermille": 549, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5493133583021224, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R229 | 03:49 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 83.53, "before": 83.6, "loss": 0.07, "playerId": 2707} |
| R230 | 03:50 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 45000, "edgeProgressPermille": 561, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5617977528089888, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R230 | 03:50 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 83.46, "before": 83.53, "loss": 0.07, "playerId": 2707} |
| R230 | 03:50 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 31000, "edgeProgressPermille": 222, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.2222222222222222, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R230 | 03:50 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.34, "before": 92.4, "loss": 0.065, "playerId": 2735} |
| R231 | 03:51 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 46000, "edgeProgressPermille": 574, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5742821473158551, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R231 | 03:51 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 83.39, "before": 83.46, "loss": 0.07, "playerId": 2707} |
| R231 | 03:51 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 32000, "edgeProgressPermille": 229, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.22939068100358423, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R231 | 03:51 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.28, "before": 92.34, "loss": 0.065, "playerId": 2735} |
| R232 | 03:52 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 33000, "edgeProgressPermille": 236, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.23655913978494625, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R232 | 03:52 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.22, "before": 92.28, "loss": 0.065, "playerId": 2735} |
| R232 | 03:52 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 47000, "edgeProgressPermille": 586, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.5867665418227216, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R232 | 03:52 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 83.32, "before": 83.39, "loss": 0.07, "playerId": 2707} |
| R233 | 03:53 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 34000, "edgeProgressPermille": 243, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.24372759856630824, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R233 | 03:53 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.16, "before": 92.22, "loss": 0.065, "playerId": 2735} |
| R233 | 03:53 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 48000, "edgeProgressPermille": 599, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.599250936329588, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R233 | 03:53 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 83.25, "before": 83.32, "loss": 0.07, "playerId": 2707} |
| R234 | 03:54 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 49000, "edgeProgressPermille": 611, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6117353308364545, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R234 | 03:54 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 83.18, "before": 83.25, "loss": 0.07, "playerId": 2707} |
| R234 | 03:54 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 35000, "edgeProgressPermille": 250, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.25089605734767023, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R234 | 03:54 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.1, "before": 92.16, "loss": 0.065, "playerId": 2735} |
| R235 | 03:55 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 50000, "edgeProgressPermille": 624, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6242197253433208, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R235 | 03:55 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 83.11, "before": 83.18, "loss": 0.07, "playerId": 2707} |
| R235 | 03:55 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 36000, "edgeProgressPermille": 258, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.25806451612903225, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R235 | 03:55 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 92.04, "before": 92.1, "loss": 0.065, "playerId": 2735} |
| R236 | 03:56 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 37000, "edgeProgressPermille": 265, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.26523297491039427, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R236 | 03:56 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.98, "before": 92.04, "loss": 0.065, "playerId": 2735} |
| R236 | 03:56 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 51000, "edgeProgressPermille": 636, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6367041198501873, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R236 | 03:56 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 83.04, "before": 83.11, "loss": 0.07, "playerId": 2707} |
| R237 | 03:57 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 38000, "edgeProgressPermille": 272, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.2724014336917563, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R237 | 03:57 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.92, "before": 91.98, "loss": 0.065, "playerId": 2735} |
| R237 | 03:57 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 52000, "edgeProgressPermille": 649, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6491885143570537, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R237 | 03:57 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 82.97, "before": 83.04, "loss": 0.07, "playerId": 2707} |
| R238 | 03:58 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 53000, "edgeProgressPermille": 661, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.66167290886392, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R238 | 03:58 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 82.9, "before": 82.97, "loss": 0.07, "playerId": 2707} |
| R238 | 03:58 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 39000, "edgeProgressPermille": 279, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.27956989247311825, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R238 | 03:58 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.86, "before": 91.92, "loss": 0.065, "playerId": 2735} |
| R239 | 03:59 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 54000, "edgeProgressPermille": 674, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6741573033707865, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R239 | 03:59 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 82.83, "before": 82.9, "loss": 0.07, "playerId": 2707} |
| R239 | 03:59 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 40000, "edgeProgressPermille": 286, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.2867383512544803, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R239 | 03:59 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.8, "before": 91.86, "loss": 0.065, "playerId": 2735} |
| R240 | 04:00 | MED | 任务过期 |  | T_005 在 五岭山道(S06) 过期 |
| R240 | 04:00 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 41000, "edgeProgressPermille": 293, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.2939068100358423, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R240 | 04:00 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.74, "before": 91.8, "loss": 0.065, "playerId": 2735} |
| R240 | 04:00 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 55000, "edgeProgressPermille": 686, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.686641697877653, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R240 | 04:00 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 82.76, "before": 82.83, "loss": 0.07, "playerId": 2707} |
| R241 | 04:01 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 42000, "edgeProgressPermille": 301, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.3010752688172043, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R241 | 04:01 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.68, "before": 91.74, "loss": 0.065, "playerId": 2735} |
| R241 | 04:01 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 56000, "edgeProgressPermille": 699, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.6991260923845194, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R241 | 04:01 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 82.69, "before": 82.76, "loss": 0.07, "playerId": 2707} |
| R242 | 04:02 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 57000, "edgeProgressPermille": 711, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7116104868913857, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R242 | 04:02 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 82.62, "before": 82.69, "loss": 0.07, "playerId": 2707} |
| R242 | 04:02 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 43000, "edgeProgressPermille": 308, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.30824372759856633, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R242 | 04:02 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.62, "before": 91.68, "loss": 0.065, "playerId": 2735} |
| R243 | 04:03 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 58000, "edgeProgressPermille": 724, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7240948813982522, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R243 | 04:03 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 82.55, "before": 82.62, "loss": 0.07, "playerId": 2707} |
| R243 | 04:03 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 44000, "edgeProgressPermille": 315, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.3154121863799283, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R243 | 04:03 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.56, "before": 91.62, "loss": 0.065, "playerId": 2735} |
| R244 | 04:04 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 45000, "edgeProgressPermille": 322, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.3225806451612903, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R244 | 04:04 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.5, "before": 91.56, "loss": 0.065, "playerId": 2735} |
| R244 | 04:04 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 59000, "edgeProgressPermille": 736, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7365792759051186, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R244 | 04:04 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 82.48, "before": 82.55, "loss": 0.07, "playerId": 2707} |
| R245 | 04:05 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 46000, "edgeProgressPermille": 329, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.32974910394265233, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R245 | 04:05 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.44, "before": 91.5, "loss": 0.065, "playerId": 2735} |
| R245 | 04:05 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 60000, "edgeProgressPermille": 749, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7490636704119851, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R245 | 04:05 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 82.41, "before": 82.48, "loss": 0.07, "playerId": 2707} |
| R246 | 04:06 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 61000, "edgeProgressPermille": 761, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7615480649188514, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R246 | 04:06 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 82.34, "before": 82.41, "loss": 0.07, "playerId": 2707} |
| R246 | 04:06 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 47000, "edgeProgressPermille": 336, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.33691756272401435, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R246 | 04:06 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.38, "before": 91.44, "loss": 0.065, "playerId": 2735} |
| R247 | 04:07 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 62000, "edgeProgressPermille": 774, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7740324594257179, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R247 | 04:07 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 82.27, "before": 82.34, "loss": 0.07, "playerId": 2707} |
| R247 | 04:07 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 48000, "edgeProgressPermille": 344, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.34408602150537637, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R247 | 04:07 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.32, "before": 91.38, "loss": 0.065, "playerId": 2735} |
| R248 | 04:08 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 49000, "edgeProgressPermille": 351, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.35125448028673834, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R248 | 04:08 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.26, "before": 91.32, "loss": 0.065, "playerId": 2735} |
| R248 | 04:08 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 63000, "edgeProgressPermille": 786, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7865168539325843, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R248 | 04:08 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 82.2, "before": 82.27, "loss": 0.07, "playerId": 2707} |
| R249 | 04:09 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 50000, "edgeProgressPermille": 358, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.35842293906810035, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R249 | 04:09 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.2, "before": 91.26, "loss": 0.065, "playerId": 2735} |
| R249 | 04:09 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 64000, "edgeProgressPermille": 799, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.7990012484394506, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R249 | 04:09 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 82.13, "before": 82.2, "loss": 0.07, "playerId": 2707} |
| R250 | 04:10 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 65000, "edgeProgressPermille": 811, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.8114856429463171, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R250 | 04:10 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 82.06, "before": 82.13, "loss": 0.07, "playerId": 2707} |
| R250 | 04:10 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 51000, "edgeProgressPermille": 365, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.3655913978494624, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R250 | 04:10 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.14, "before": 91.2, "loss": 0.065, "playerId": 2735} |
| R251 | 04:11 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 66000, "edgeProgressPermille": 823, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.8239700374531835, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R251 | 04:11 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 81.99, "before": 82.06, "loss": 0.07, "playerId": 2707} |
| R251 | 04:11 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 52000, "edgeProgressPermille": 372, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.3727598566308244, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R251 | 04:11 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.08, "before": 91.14, "loss": 0.065, "playerId": 2735} |
| R252 | 04:12 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 53000, "edgeProgressPermille": 379, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.37992831541218636, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R252 | 04:12 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 91.02, "before": 91.08, "loss": 0.065, "playerId": 2735} |
| R252 | 04:12 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 67000, "edgeProgressPermille": 836, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.83645443196005, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R252 | 04:12 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 81.92, "before": 81.99, "loss": 0.07, "playerId": 2707} |
| R253 | 04:13 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 54000, "edgeProgressPermille": 387, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.3870967741935484, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R253 | 04:13 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.96, "before": 91.02, "loss": 0.065, "playerId": 2735} |
| R253 | 04:13 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 68000, "edgeProgressPermille": 848, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.8489388264669163, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R253 | 04:13 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 81.85, "before": 81.92, "loss": 0.07, "playerId": 2707} |
| R254 | 04:14 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 69000, "edgeProgressPermille": 861, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.8614232209737828, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R254 | 04:14 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 81.78, "before": 81.85, "loss": 0.07, "playerId": 2707} |
| R254 | 04:14 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 55000, "edgeProgressPermille": 394, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.3942652329749104, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R254 | 04:14 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.9, "before": 90.96, "loss": 0.065, "playerId": 2735} |
| R255 | 04:15 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 70000, "edgeProgressPermille": 873, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.8739076154806492, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R255 | 04:15 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 81.71, "before": 81.78, "loss": 0.07, "playerId": 2707} |
| R255 | 04:15 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 56000, "edgeProgressPermille": 401, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.4014336917562724, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R255 | 04:15 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.84, "before": 90.9, "loss": 0.065, "playerId": 2735} |
| R256 | 04:16 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 57000, "edgeProgressPermille": 408, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.40860215053763443, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R256 | 04:16 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.78, "before": 90.84, "loss": 0.065, "playerId": 2735} |
| R256 | 04:16 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 71000, "edgeProgressPermille": 886, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.8863920099875156, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R256 | 04:16 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 81.64, "before": 81.71, "loss": 0.07, "playerId": 2707} |
| R257 | 04:17 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 58000, "edgeProgressPermille": 415, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.4157706093189964, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R257 | 04:17 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.72, "before": 90.78, "loss": 0.065, "playerId": 2735} |
| R257 | 04:17 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 72000, "edgeProgressPermille": 898, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.898876404494382, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R257 | 04:17 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 81.57, "before": 81.64, "loss": 0.07, "playerId": 2707} |
| R258 | 04:18 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 73000, "edgeProgressPermille": 911, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9113607990012484, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R258 | 04:18 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 81.5, "before": 81.57, "loss": 0.07, "playerId": 2707} |
| R258 | 04:18 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 59000, "edgeProgressPermille": 422, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.4229390681003584, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R258 | 04:18 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.66, "before": 90.72, "loss": 0.065, "playerId": 2735} |
| R259 | 04:19 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 74000, "edgeProgressPermille": 923, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9238451935081149, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R259 | 04:19 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 81.43, "before": 81.5, "loss": 0.07, "playerId": 2707} |
| R259 | 04:19 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 60000, "edgeProgressPermille": 430, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.43010752688172044, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R259 | 04:19 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.6, "before": 90.66, "loss": 0.065, "playerId": 2735} |
| R260 | 04:20 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 61000, "edgeProgressPermille": 437, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.43727598566308246, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R260 | 04:20 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.54, "before": 90.6, "loss": 0.065, "playerId": 2735} |
| R260 | 04:20 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 75000, "edgeProgressPermille": 936, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9363295880149812, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R260 | 04:20 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 81.36, "before": 81.43, "loss": 0.07, "playerId": 2707} |
| R261 | 04:21 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 62000, "edgeProgressPermille": 444, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.4444444444444444, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R261 | 04:21 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.48, "before": 90.54, "loss": 0.065, "playerId": 2735} |
| R261 | 04:21 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 76000, "edgeProgressPermille": 948, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9488139825218477, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R261 | 04:21 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 81.29, "before": 81.36, "loss": 0.07, "playerId": 2707} |
| R262 | 04:22 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 77000, "edgeProgressPermille": 961, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9612983770287141, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R262 | 04:22 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 81.22, "before": 81.29, "loss": 0.07, "playerId": 2707} |
| R262 | 04:22 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 63000, "edgeProgressPermille": 451, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.45161290322580644, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R262 | 04:22 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.42, "before": 90.48, "loss": 0.065, "playerId": 2735} |
| R263 | 04:23 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 78000, "edgeProgressPermille": 973, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9737827715355806, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R263 | 04:23 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 81.15, "before": 81.22, "loss": 0.07, "playerId": 2707} |
| R263 | 04:23 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 64000, "edgeProgressPermille": 458, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.45878136200716846, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R263 | 04:23 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.36, "before": 90.42, "loss": 0.065, "playerId": 2735} |
| R264 | 04:24 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 65000, "edgeProgressPermille": 465, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.4659498207885305, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R264 | 04:24 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.3, "before": 90.36, "loss": 0.065, "playerId": 2735} |
| R264 | 04:24 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 79000, "edgeProgressPermille": 986, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9862671660424469, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R264 | 04:24 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 81.08, "before": 81.15, "loss": 0.07, "playerId": 2707} |
| R265 | 04:25 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 66000, "edgeProgressPermille": 473, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.4731182795698925, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R265 | 04:25 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.24, "before": 90.3, "loss": 0.065, "playerId": 2735} |
| R265 | 04:25 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 80000, "edgeProgressPermille": 998, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 0.9987515605493134, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R265 | 04:25 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 81.01, "before": 81.08, "loss": 0.07, "playerId": 2707} |
| R266 | 04:26 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 80100, "edgeProgressPermille": 1000, "edgeTotalMs": 80100, "fromNodeId": "S06", "playerId": 2707, "progress": 1.0, "routeEdgeId": "E15", "toNodeId": "S01"} |
| R266 | 04:26 | HIGH | 进点 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 进入 岭南果园(S01) |
| R266 | 04:26 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.94, "before": 81.01, "loss": 0.07, "playerId": 2707} |
| R266 | 04:26 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 67000, "edgeProgressPermille": 480, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.48028673835125446, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R266 | 04:26 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.18, "before": 90.24, "loss": 0.065, "playerId": 2735} |
| R267 | 04:27 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 21, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.021312872975277068, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R267 | 04:27 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.88, "before": 80.94, "loss": 0.055, "playerId": 2707} |
| R267 | 04:27 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 68000, "edgeProgressPermille": 487, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.4874551971326165, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R267 | 04:27 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.12, "before": 90.18, "loss": 0.065, "playerId": 2735} |
| R268 | 04:28 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 69000, "edgeProgressPermille": 494, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.4946236559139785, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R268 | 04:28 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.06, "before": 90.12, "loss": 0.065, "playerId": 2735} |
| R268 | 04:28 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 42, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.042625745950554135, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R268 | 04:28 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.82, "before": 80.88, "loss": 0.055, "playerId": 2707} |
| R269 | 04:29 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 70000, "edgeProgressPermille": 501, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.5017921146953405, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R269 | 04:29 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 90.0, "before": 90.06, "loss": 0.065, "playerId": 2735} |
| R269 | 04:29 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 63, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.0639386189258312, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R269 | 04:29 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.76, "before": 80.82, "loss": 0.055, "playerId": 2707} |
| R270 | 04:30 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 85, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.08525149190110827, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R270 | 04:30 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.71, "before": 80.76, "loss": 0.055, "playerId": 2707} |
| R270 | 04:30 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 71000, "edgeProgressPermille": 508, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.5089605734767025, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R270 | 04:30 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.94, "before": 90.0, "loss": 0.065, "playerId": 2735} |
| R271 | 04:31 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 106, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.10656436487638533, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R271 | 04:31 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.65, "before": 80.71, "loss": 0.055, "playerId": 2707} |
| R271 | 04:31 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 72000, "edgeProgressPermille": 516, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.5161290322580645, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R271 | 04:31 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.88, "before": 89.94, "loss": 0.065, "playerId": 2735} |
| R272 | 04:32 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 73000, "edgeProgressPermille": 523, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.5232974910394266, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R272 | 04:32 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.82, "before": 89.88, "loss": 0.065, "playerId": 2735} |
| R272 | 04:32 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 127, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.1278772378516624, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R272 | 04:32 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.6, "before": 80.65, "loss": 0.055, "playerId": 2707} |
| R273 | 04:33 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 74000, "edgeProgressPermille": 530, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.5304659498207885, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R273 | 04:33 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.76, "before": 89.82, "loss": 0.065, "playerId": 2735} |
| R273 | 04:33 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 149, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.14919011082693948, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R273 | 04:33 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.54, "before": 80.6, "loss": 0.055, "playerId": 2707} |
| R274 | 04:34 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 170, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.17050298380221654, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R274 | 04:34 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.49, "before": 80.54, "loss": 0.055, "playerId": 2707} |
| R274 | 04:34 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 75000, "edgeProgressPermille": 537, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.5376344086021505, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R274 | 04:34 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.7, "before": 89.76, "loss": 0.065, "playerId": 2735} |
| R275 | 04:35 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 191, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.1918158567774936, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R275 | 04:35 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.43, "before": 80.49, "loss": 0.055, "playerId": 2707} |
| R275 | 04:35 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 76000, "edgeProgressPermille": 544, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.5448028673835126, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R275 | 04:35 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.64, "before": 89.7, "loss": 0.065, "playerId": 2735} |
| R276 | 04:36 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 77000, "edgeProgressPermille": 551, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.5519713261648745, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R276 | 04:36 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.58, "before": 89.64, "loss": 0.065, "playerId": 2735} |
| R276 | 04:36 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 213, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.21312872975277067, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R276 | 04:36 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.38, "before": 80.43, "loss": 0.055, "playerId": 2707} |
| R277 | 04:37 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 78000, "edgeProgressPermille": 559, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.5591397849462365, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R277 | 04:37 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.52, "before": 89.58, "loss": 0.065, "playerId": 2735} |
| R277 | 04:37 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 234, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.23444160272804773, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R277 | 04:37 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.32, "before": 80.38, "loss": 0.055, "playerId": 2707} |
| R278 | 04:38 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 12000, "edgeProgressPermille": 255, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.2557544757033248, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R278 | 04:38 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.26, "before": 80.32, "loss": 0.055, "playerId": 2707} |
| R278 | 04:38 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 79000, "edgeProgressPermille": 566, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.5663082437275986, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R278 | 04:38 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.46, "before": 89.52, "loss": 0.065, "playerId": 2735} |
| R279 | 04:39 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 13000, "edgeProgressPermille": 277, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.2770673486786019, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R279 | 04:39 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.21, "before": 80.26, "loss": 0.055, "playerId": 2707} |
| R279 | 04:39 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 80000, "edgeProgressPermille": 573, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.5734767025089605, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R279 | 04:39 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.4, "before": 89.46, "loss": 0.065, "playerId": 2735} |
| R280 | 04:40 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 81000, "edgeProgressPermille": 580, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.5806451612903226, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R280 | 04:40 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.34, "before": 89.4, "loss": 0.065, "playerId": 2735} |
| R280 | 04:40 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 298, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.29838022165387895, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R280 | 04:40 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.15, "before": 80.21, "loss": 0.055, "playerId": 2707} |
| R281 | 04:41 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 82000, "edgeProgressPermille": 587, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.5878136200716846, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R281 | 04:41 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.28, "before": 89.34, "loss": 0.065, "playerId": 2735} |
| R281 | 04:41 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 15000, "edgeProgressPermille": 319, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.319693094629156, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R281 | 04:41 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.1, "before": 80.15, "loss": 0.055, "playerId": 2707} |
| R282 | 04:42 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 16000, "edgeProgressPermille": 341, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.3410059676044331, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R282 | 04:42 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 80.04, "before": 80.1, "loss": 0.055, "playerId": 2707} |
| R282 | 04:42 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 83000, "edgeProgressPermille": 594, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.5949820788530465, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R282 | 04:42 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.22, "before": 89.28, "loss": 0.065, "playerId": 2735} |
| R283 | 04:43 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 17000, "edgeProgressPermille": 362, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.36231884057971014, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R283 | 04:43 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.99, "before": 80.04, "loss": 0.055, "playerId": 2707} |
| R283 | 04:43 | HIGH | 果品折损 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 好果跌破阈值 80，坏果 2 |
| R283 | 04:43 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 84000, "edgeProgressPermille": 602, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.6021505376344086, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R283 | 04:43 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.16, "before": 89.22, "loss": 0.065, "playerId": 2735} |
| R284 | 04:44 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 85000, "edgeProgressPermille": 609, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.6093189964157706, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R284 | 04:44 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.1, "before": 89.16, "loss": 0.065, "playerId": 2735} |
| R284 | 04:44 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 18000, "edgeProgressPermille": 383, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.3836317135549872, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R284 | 04:44 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.93, "before": 79.99, "loss": 0.055, "playerId": 2707} |
| R285 | 04:45 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 86000, "edgeProgressPermille": 616, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.6164874551971327, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R285 | 04:45 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 89.04, "before": 89.1, "loss": 0.065, "playerId": 2735} |
| R285 | 04:45 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 19000, "edgeProgressPermille": 404, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.40494458653026427, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R285 | 04:45 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.88, "before": 79.93, "loss": 0.055, "playerId": 2707} |
| R286 | 04:46 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 20000, "edgeProgressPermille": 426, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.42625745950554134, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R286 | 04:46 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.82, "before": 79.88, "loss": 0.055, "playerId": 2707} |
| R286 | 04:46 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 87000, "edgeProgressPermille": 623, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.6236559139784946, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R286 | 04:46 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.98, "before": 89.04, "loss": 0.065, "playerId": 2735} |
| R287 | 04:47 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 21000, "edgeProgressPermille": 447, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.4475703324808184, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R287 | 04:47 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.76, "before": 79.82, "loss": 0.055, "playerId": 2707} |
| R287 | 04:47 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 88000, "edgeProgressPermille": 630, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.6308243727598566, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R287 | 04:47 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.92, "before": 88.98, "loss": 0.065, "playerId": 2735} |
| R288 | 04:48 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 89000, "edgeProgressPermille": 637, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.6379928315412187, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R288 | 04:48 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.86, "before": 88.92, "loss": 0.065, "playerId": 2735} |
| R288 | 04:48 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 22000, "edgeProgressPermille": 468, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.46888320545609546, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R288 | 04:48 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.71, "before": 79.76, "loss": 0.055, "playerId": 2707} |
| R289 | 04:49 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 90000, "edgeProgressPermille": 645, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.6451612903225806, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R289 | 04:49 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.8, "before": 88.86, "loss": 0.065, "playerId": 2735} |
| R289 | 04:49 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 23000, "edgeProgressPermille": 490, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.49019607843137253, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R289 | 04:49 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.65, "before": 79.71, "loss": 0.055, "playerId": 2707} |
| R290 | 04:50 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 24000, "edgeProgressPermille": 511, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5115089514066496, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R290 | 04:50 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.6, "before": 79.65, "loss": 0.055, "playerId": 2707} |
| R290 | 04:50 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 91000, "edgeProgressPermille": 652, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.6523297491039427, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R290 | 04:50 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.74, "before": 88.8, "loss": 0.065, "playerId": 2735} |
| R291 | 04:51 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 25000, "edgeProgressPermille": 532, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5328218243819267, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R291 | 04:51 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.54, "before": 79.6, "loss": 0.055, "playerId": 2707} |
| R291 | 04:51 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 92000, "edgeProgressPermille": 659, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.6594982078853047, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R291 | 04:51 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.68, "before": 88.74, "loss": 0.065, "playerId": 2735} |
| R292 | 04:52 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 93000, "edgeProgressPermille": 666, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.6666666666666666, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R292 | 04:52 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.62, "before": 88.68, "loss": 0.065, "playerId": 2735} |
| R292 | 04:52 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 26000, "edgeProgressPermille": 554, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5541346973572038, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R292 | 04:52 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.49, "before": 79.54, "loss": 0.055, "playerId": 2707} |
| R293 | 04:53 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 94000, "edgeProgressPermille": 673, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.6738351254480287, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R293 | 04:53 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.56, "before": 88.62, "loss": 0.065, "playerId": 2735} |
| R293 | 04:53 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 27000, "edgeProgressPermille": 575, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5754475703324808, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R293 | 04:53 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.43, "before": 79.49, "loss": 0.055, "playerId": 2707} |
| R294 | 04:54 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 28000, "edgeProgressPermille": 596, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.5967604433077579, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R294 | 04:54 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.38, "before": 79.43, "loss": 0.055, "playerId": 2707} |
| R294 | 04:54 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 95000, "edgeProgressPermille": 681, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.6810035842293907, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R294 | 04:54 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.5, "before": 88.56, "loss": 0.065, "playerId": 2735} |
| R295 | 04:55 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 29000, "edgeProgressPermille": 618, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.618073316283035, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R295 | 04:55 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.32, "before": 79.38, "loss": 0.055, "playerId": 2707} |
| R295 | 04:55 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 96000, "edgeProgressPermille": 688, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.6881720430107527, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R295 | 04:55 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.44, "before": 88.5, "loss": 0.065, "playerId": 2735} |
| R296 | 04:56 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 97000, "edgeProgressPermille": 695, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.6953405017921147, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R296 | 04:56 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.38, "before": 88.44, "loss": 0.065, "playerId": 2735} |
| R296 | 04:56 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 30000, "edgeProgressPermille": 639, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.639386189258312, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R296 | 04:56 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.26, "before": 79.32, "loss": 0.055, "playerId": 2707} |
| R297 | 04:57 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 98000, "edgeProgressPermille": 702, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.7025089605734767, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R297 | 04:57 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.32, "before": 88.38, "loss": 0.065, "playerId": 2735} |
| R297 | 04:57 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 31000, "edgeProgressPermille": 660, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6606990622335891, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R297 | 04:57 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.21, "before": 79.26, "loss": 0.055, "playerId": 2707} |
| R298 | 04:58 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 32000, "edgeProgressPermille": 682, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.6820119352088662, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R298 | 04:58 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.15, "before": 79.21, "loss": 0.055, "playerId": 2707} |
| R298 | 04:58 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 99000, "edgeProgressPermille": 709, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.7096774193548387, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R298 | 04:58 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.26, "before": 88.32, "loss": 0.065, "playerId": 2735} |
| R299 | 04:59 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 33000, "edgeProgressPermille": 703, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7033248081841432, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R299 | 04:59 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.1, "before": 79.15, "loss": 0.055, "playerId": 2707} |
| R299 | 04:59 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 100000, "edgeProgressPermille": 716, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.7168458781362007, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R299 | 04:59 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.2, "before": 88.26, "loss": 0.065, "playerId": 2735} |
| R300 | 05:00 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 101000, "edgeProgressPermille": 724, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.7240143369175627, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R300 | 05:00 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.14, "before": 88.2, "loss": 0.065, "playerId": 2735} |
| R300 | 05:00 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 34000, "edgeProgressPermille": 724, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7246376811594203, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R300 | 05:00 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 79.04, "before": 79.1, "loss": 0.055, "playerId": 2707} |
| R300 | 05:00 | MED | 任务刷新 |  | T_013 刷新在 五岭山道(S06)，路线 MOUNTAIN，截止 R520 |
| R300 | 05:00 | MED | 任务刷新 |  | T_014 刷新在 洞庭水驿(S05)，路线 WATER，截止 R520 |
| R300 | 05:00 | MED | 任务刷新 |  | T_015 刷新在 洛阳驿(S09)，路线 WATER，截止 R520 |
| R300 | 05:00 | MED | 任务刷新 |  | T_016 刷新在 荆襄大驿(S07)，路线 ROAD，截止 R520 |
| R301 | 05:01 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 102000, "edgeProgressPermille": 731, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.7311827956989247, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R301 | 05:01 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.08, "before": 88.14, "loss": 0.065, "playerId": 2735} |
| R301 | 05:01 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 35000, "edgeProgressPermille": 745, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7459505541346974, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R301 | 05:01 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.99, "before": 79.04, "loss": 0.055, "playerId": 2707} |
| R302 | 05:02 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 36000, "edgeProgressPermille": 767, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7672634271099744, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R302 | 05:02 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.93, "before": 78.99, "loss": 0.055, "playerId": 2707} |
| R302 | 05:02 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 103000, "edgeProgressPermille": 738, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.7383512544802867, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R302 | 05:02 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 88.02, "before": 88.08, "loss": 0.065, "playerId": 2735} |
| R303 | 05:03 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 37000, "edgeProgressPermille": 788, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.7885763000852515, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R303 | 05:03 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.88, "before": 78.93, "loss": 0.055, "playerId": 2707} |
| R303 | 05:03 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 104000, "edgeProgressPermille": 745, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.7455197132616488, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R303 | 05:03 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.96, "before": 88.02, "loss": 0.065, "playerId": 2735} |
| R304 | 05:04 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 105000, "edgeProgressPermille": 752, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.7526881720430108, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R304 | 05:04 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.9, "before": 87.96, "loss": 0.065, "playerId": 2735} |
| R304 | 05:04 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 38000, "edgeProgressPermille": 809, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8098891730605285, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R304 | 05:04 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.82, "before": 78.88, "loss": 0.055, "playerId": 2707} |
| R305 | 05:05 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 106000, "edgeProgressPermille": 759, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.7598566308243727, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R305 | 05:05 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.84, "before": 87.9, "loss": 0.065, "playerId": 2735} |
| R305 | 05:05 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 39000, "edgeProgressPermille": 831, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8312020460358056, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R305 | 05:05 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.76, "before": 78.82, "loss": 0.055, "playerId": 2707} |
| R306 | 05:06 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 40000, "edgeProgressPermille": 852, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8525149190110827, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R306 | 05:06 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.71, "before": 78.76, "loss": 0.055, "playerId": 2707} |
| R306 | 05:06 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 107000, "edgeProgressPermille": 767, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.7670250896057348, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R306 | 05:06 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.78, "before": 87.84, "loss": 0.065, "playerId": 2735} |
| R307 | 05:07 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 41000, "edgeProgressPermille": 873, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8738277919863597, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R307 | 05:07 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.65, "before": 78.71, "loss": 0.055, "playerId": 2707} |
| R307 | 05:07 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 108000, "edgeProgressPermille": 774, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.7741935483870968, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R307 | 05:07 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.72, "before": 87.78, "loss": 0.065, "playerId": 2735} |
| R308 | 05:08 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 109000, "edgeProgressPermille": 781, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.7813620071684588, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R308 | 05:08 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.66, "before": 87.72, "loss": 0.065, "playerId": 2735} |
| R308 | 05:08 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 42000, "edgeProgressPermille": 895, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.8951406649616368, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R308 | 05:08 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.6, "before": 78.65, "loss": 0.055, "playerId": 2707} |
| R309 | 05:09 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 110000, "edgeProgressPermille": 788, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.7885304659498208, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R309 | 05:09 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.6, "before": 87.66, "loss": 0.065, "playerId": 2735} |
| R309 | 05:09 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 43000, "edgeProgressPermille": 916, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9164535379369139, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R309 | 05:09 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.54, "before": 78.6, "loss": 0.055, "playerId": 2707} |
| R310 | 05:10 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 44000, "edgeProgressPermille": 937, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9377664109121909, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R310 | 05:10 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.49, "before": 78.54, "loss": 0.055, "playerId": 2707} |
| R310 | 05:10 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 111000, "edgeProgressPermille": 795, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.7956989247311828, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R310 | 05:10 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.54, "before": 87.6, "loss": 0.065, "playerId": 2735} |
| R311 | 05:11 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 45000, "edgeProgressPermille": 959, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.959079283887468, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R311 | 05:11 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.43, "before": 78.49, "loss": 0.055, "playerId": 2707} |
| R311 | 05:11 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 112000, "edgeProgressPermille": 802, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.8028673835125448, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R311 | 05:11 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.48, "before": 87.54, "loss": 0.065, "playerId": 2735} |
| R312 | 05:12 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 113000, "edgeProgressPermille": 810, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.8100358422939068, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R312 | 05:12 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.42, "before": 87.48, "loss": 0.065, "playerId": 2735} |
| R312 | 05:12 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 46000, "edgeProgressPermille": 980, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 0.9803921568627451, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R312 | 05:12 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.38, "before": 78.43, "loss": 0.055, "playerId": 2707} |
| R313 | 05:13 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 114000, "edgeProgressPermille": 817, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.8172043010752689, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R313 | 05:13 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.36, "before": 87.42, "loss": 0.065, "playerId": 2735} |
| R313 | 05:13 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 46920, "edgeProgressPermille": 1000, "edgeTotalMs": 46920, "fromNodeId": "S01", "playerId": 2707, "progress": 1.0, "routeEdgeId": "E01", "toNodeId": "S02"} |
| R313 | 05:13 | HIGH | 进点 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 进入 南岭驿(S02) |
| R313 | 05:13 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.32, "before": 78.38, "loss": 0.055, "playerId": 2707} |
| R314 | 05:14 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 27, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.027870680044593088, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R314 | 05:14 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.26, "before": 78.32, "loss": 0.055, "playerId": 2707} |
| R314 | 05:14 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 115000, "edgeProgressPermille": 824, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.8243727598566308, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R314 | 05:14 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.3, "before": 87.36, "loss": 0.065, "playerId": 2735} |
| R315 | 05:15 | HIGH | 派遣 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 派遣队伍清障 荆襄大驿(S07)，预计 R326 完成 |
| R315 | 05:15 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 55, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.055741360089186176, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R315 | 05:15 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.21, "before": 78.26, "loss": 0.055, "playerId": 2707} |
| R315 | 05:15 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 116000, "edgeProgressPermille": 831, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.8315412186379928, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R315 | 05:15 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.24, "before": 87.3, "loss": 0.065, "playerId": 2735} |
| R316 | 05:16 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 117000, "edgeProgressPermille": 838, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.8387096774193549, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R316 | 05:16 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.18, "before": 87.24, "loss": 0.065, "playerId": 2735} |
| R316 | 05:16 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 83, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.08361204013377926, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R316 | 05:16 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.15, "before": 78.21, "loss": 0.055, "playerId": 2707} |
| R317 | 05:17 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 118000, "edgeProgressPermille": 845, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.8458781362007168, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R317 | 05:17 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.12, "before": 87.18, "loss": 0.065, "playerId": 2735} |
| R317 | 05:17 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 111, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.11148272017837235, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R317 | 05:17 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.1, "before": 78.15, "loss": 0.055, "playerId": 2707} |
| R318 | 05:18 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 139, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.13935340022296544, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R318 | 05:18 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 78.04, "before": 78.1, "loss": 0.055, "playerId": 2707} |
| R318 | 05:18 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 119000, "edgeProgressPermille": 853, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.8530465949820788, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R318 | 05:18 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.06, "before": 87.12, "loss": 0.065, "playerId": 2735} |
| R319 | 05:19 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 167, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.16722408026755853, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R319 | 05:19 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.99, "before": 78.04, "loss": 0.055, "playerId": 2707} |
| R319 | 05:19 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 120000, "edgeProgressPermille": 860, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.8602150537634409, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R319 | 05:19 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 87.0, "before": 87.06, "loss": 0.065, "playerId": 2735} |
| R320 | 05:20 | MED | 任务过期 |  | T_006 在 江南码头(S04) 过期 |
| R320 | 05:20 | MED | 任务过期 |  | T_007 在 荆襄大驿(S07) 过期 |
| R320 | 05:20 | MED | 任务过期 |  | T_008 在 洛阳驿(S09) 过期 |
| R320 | 05:20 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 121000, "edgeProgressPermille": 867, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.8673835125448028, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R320 | 05:20 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.94, "before": 87.0, "loss": 0.065, "playerId": 2735} |
| R320 | 05:20 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 195, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.19509476031215162, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R320 | 05:20 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.93, "before": 77.99, "loss": 0.055, "playerId": 2707} |
| R321 | 05:21 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 122000, "edgeProgressPermille": 874, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.8745519713261649, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R321 | 05:21 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.88, "before": 86.94, "loss": 0.065, "playerId": 2735} |
| R321 | 05:21 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 222, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.2229654403567447, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R321 | 05:21 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.88, "before": 77.93, "loss": 0.055, "playerId": 2707} |
| R322 | 05:22 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 250, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.2508361204013378, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R322 | 05:22 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.82, "before": 77.88, "loss": 0.055, "playerId": 2707} |
| R322 | 05:22 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 123000, "edgeProgressPermille": 881, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.8817204301075269, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R322 | 05:22 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.82, "before": 86.88, "loss": 0.065, "playerId": 2735} |
| R323 | 05:23 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 278, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.2787068004459309, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R323 | 05:23 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.76, "before": 77.82, "loss": 0.055, "playerId": 2707} |
| R323 | 05:23 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 124000, "edgeProgressPermille": 888, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.8888888888888888, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R323 | 05:23 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.76, "before": 86.82, "loss": 0.065, "playerId": 2735} |
| R324 | 05:24 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 125000, "edgeProgressPermille": 896, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.8960573476702509, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R324 | 05:24 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.7, "before": 86.76, "loss": 0.065, "playerId": 2735} |
| R324 | 05:24 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 306, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.30657748049052397, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R324 | 05:24 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.71, "before": 77.76, "loss": 0.055, "playerId": 2707} |
| R325 | 05:25 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 126000, "edgeProgressPermille": 903, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.9032258064516129, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R325 | 05:25 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.64, "before": 86.7, "loss": 0.065, "playerId": 2735} |
| R325 | 05:25 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 12000, "edgeProgressPermille": 334, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.33444816053511706, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R325 | 05:25 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.65, "before": 77.71, "loss": 0.055, "playerId": 2707} |
| R326 | 05:26 | HIGH | 清障完成 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 完成 荆襄大驿(S07) 清障 |
| R326 | 05:26 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 13000, "edgeProgressPermille": 362, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.36231884057971014, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R326 | 05:26 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.6, "before": 77.65, "loss": 0.055, "playerId": 2707} |
| R326 | 05:26 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 127000, "edgeProgressPermille": 910, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.910394265232975, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R326 | 05:26 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.58, "before": 86.64, "loss": 0.065, "playerId": 2735} |
| R327 | 05:27 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 390, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.39018952062430323, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R327 | 05:27 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.54, "before": 77.6, "loss": 0.055, "playerId": 2707} |
| R327 | 05:27 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 128000, "edgeProgressPermille": 917, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.9175627240143369, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R327 | 05:27 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.52, "before": 86.58, "loss": 0.065, "playerId": 2735} |
| R328 | 05:28 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 129000, "edgeProgressPermille": 924, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.9247311827956989, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R328 | 05:28 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.46, "before": 86.52, "loss": 0.065, "playerId": 2735} |
| R328 | 05:28 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 15000, "edgeProgressPermille": 418, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.4180602006688963, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R328 | 05:28 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.49, "before": 77.54, "loss": 0.055, "playerId": 2707} |
| R329 | 05:29 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 130000, "edgeProgressPermille": 931, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.931899641577061, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R329 | 05:29 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.4, "before": 86.46, "loss": 0.065, "playerId": 2735} |
| R329 | 05:29 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 16000, "edgeProgressPermille": 445, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.4459308807134894, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R329 | 05:29 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.43, "before": 77.49, "loss": 0.055, "playerId": 2707} |
| R330 | 05:30 | HIGH | 派遣 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 派遣队伍侦察 潼关驿(S11)，预计 R335 完成 |
| R330 | 05:30 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 17000, "edgeProgressPermille": 473, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.4738015607580825, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R330 | 05:30 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.38, "before": 77.43, "loss": 0.055, "playerId": 2707} |
| R330 | 05:30 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 131000, "edgeProgressPermille": 939, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.9390681003584229, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R330 | 05:30 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.34, "before": 86.4, "loss": 0.065, "playerId": 2735} |
| R330 | 05:30 | MED | 任务刷新 |  | T_017 刷新在 洛阳驿(S09)，路线 WATER，截止 R510 |
| R331 | 05:31 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 18000, "edgeProgressPermille": 501, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.5016722408026756, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R331 | 05:31 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.32, "before": 77.38, "loss": 0.055, "playerId": 2707} |
| R331 | 05:31 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 132000, "edgeProgressPermille": 946, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.946236559139785, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R331 | 05:31 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.28, "before": 86.34, "loss": 0.065, "playerId": 2735} |
| R332 | 05:32 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 133000, "edgeProgressPermille": 953, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.953405017921147, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R332 | 05:32 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.22, "before": 86.28, "loss": 0.065, "playerId": 2735} |
| R332 | 05:32 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 19000, "edgeProgressPermille": 529, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.5295429208472687, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R332 | 05:32 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.26, "before": 77.32, "loss": 0.055, "playerId": 2707} |
| R333 | 05:33 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 134000, "edgeProgressPermille": 960, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.9605734767025089, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R333 | 05:33 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.16, "before": 86.22, "loss": 0.065, "playerId": 2735} |
| R333 | 05:33 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 20000, "edgeProgressPermille": 557, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.5574136008918618, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R333 | 05:33 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.21, "before": 77.26, "loss": 0.055, "playerId": 2707} |
| R334 | 05:34 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 21000, "edgeProgressPermille": 585, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.5852842809364549, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R334 | 05:34 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.15, "before": 77.21, "loss": 0.055, "playerId": 2707} |
| R334 | 05:34 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 135000, "edgeProgressPermille": 967, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.967741935483871, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R334 | 05:34 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.1, "before": 86.16, "loss": 0.065, "playerId": 2735} |
| R335 | 05:35 | MED | SCOUT_MARKER_ADD | BLUE 路人女主队/1.0(2735) | {"expireRound": 380, "playerId": 2735, "remainingTriggers": 1, "targetNodeId": "S11"} |
| R335 | 05:35 | MED | 侦察回报 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 侦察 潼关驿(S11)：无障碍，资源 无明显资源 |
| R335 | 05:35 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 22000, "edgeProgressPermille": 613, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.6131549609810479, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R335 | 05:35 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.1, "before": 77.15, "loss": 0.055, "playerId": 2707} |
| R335 | 05:35 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 136000, "edgeProgressPermille": 974, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.974910394265233, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R335 | 05:35 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 86.04, "before": 86.1, "loss": 0.065, "playerId": 2735} |
| R336 | 05:36 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 137000, "edgeProgressPermille": 982, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.982078853046595, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R336 | 05:36 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.98, "before": 86.04, "loss": 0.065, "playerId": 2735} |
| R336 | 05:36 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 23000, "edgeProgressPermille": 641, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.6410256410256411, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R336 | 05:36 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 77.04, "before": 77.1, "loss": 0.055, "playerId": 2707} |
| R337 | 05:37 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 138000, "edgeProgressPermille": 989, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.989247311827957, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R337 | 05:37 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.92, "before": 85.98, "loss": 0.065, "playerId": 2735} |
| R337 | 05:37 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 24000, "edgeProgressPermille": 668, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.6688963210702341, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R337 | 05:37 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.99, "before": 77.04, "loss": 0.055, "playerId": 2707} |
| R338 | 05:38 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 25000, "edgeProgressPermille": 696, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.6967670011148273, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R338 | 05:38 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.93, "before": 76.99, "loss": 0.055, "playerId": 2707} |
| R338 | 05:38 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 139000, "edgeProgressPermille": 996, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 0.996415770609319, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R338 | 05:38 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.86, "before": 85.92, "loss": 0.065, "playerId": 2735} |
| R339 | 05:39 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 26000, "edgeProgressPermille": 724, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.7246376811594203, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R339 | 05:39 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.88, "before": 76.93, "loss": 0.055, "playerId": 2707} |
| R339 | 05:39 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 139500, "edgeProgressPermille": 1000, "edgeTotalMs": 139500, "fromNodeId": "S08", "playerId": 2735, "progress": 1.0, "routeEdgeId": "E17", "toNodeId": "S11"} |
| R339 | 05:39 | HIGH | 进点 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 进入 潼关驿(S11) |
| R339 | 05:39 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.8, "before": 85.86, "loss": 0.065, "playerId": 2735} |
| R340 | 05:40 | MED | SCOUT_MARKER_APPLY | BLUE 路人女主队/1.0(2735) | {"afterRound": 2, "beforeRound": 4, "playerId": 2735, "processType": "PASS_TRANSFER", "targetNodeId": "S11"} |
| R340 | 05:40 | MED | PROCESS_PROGRESS | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "processType": "PASS_TRANSFER", "remainingRound": 1, "targetNodeId": "S11"} |
| R340 | 05:40 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.75, "before": 85.8, "loss": 0.05, "playerId": 2735} |
| R340 | 05:40 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 27000, "edgeProgressPermille": 752, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.7525083612040134, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R340 | 05:40 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.82, "before": 76.88, "loss": 0.055, "playerId": 2707} |
| R341 | 05:41 | MED | PROCESS_PROGRESS | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "processType": "PASS_TRANSFER", "remainingRound": 0, "targetNodeId": "S11"} |
| R341 | 05:41 | MED | SCOUT_MARKER_CONSUME | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "remainingTriggers": 0, "targetNodeId": "S11"} |
| R341 | 05:41 | MED | 处理完成 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 在 潼关驿(S11) 完成关口转运 |
| R341 | 05:41 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.7, "before": 85.75, "loss": 0.05, "playerId": 2735} |
| R341 | 05:41 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 28000, "edgeProgressPermille": 780, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.7803790412486065, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R341 | 05:41 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.76, "before": 76.82, "loss": 0.055, "playerId": 2707} |
| R342 | 05:42 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 29000, "edgeProgressPermille": 808, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.8082497212931996, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R342 | 05:42 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.71, "before": 76.76, "loss": 0.055, "playerId": 2707} |
| R342 | 05:42 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 1000, "edgeProgressPermille": 18, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.018975332068311195, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R342 | 05:42 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.64, "before": 85.7, "loss": 0.065, "playerId": 2735} |
| R343 | 05:43 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 30000, "edgeProgressPermille": 836, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.8361204013377926, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R343 | 05:43 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.65, "before": 76.71, "loss": 0.055, "playerId": 2707} |
| R343 | 05:43 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 2000, "edgeProgressPermille": 37, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.03795066413662239, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R343 | 05:43 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.58, "before": 85.64, "loss": 0.065, "playerId": 2735} |
| R344 | 05:44 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 3000, "edgeProgressPermille": 56, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.056925996204933584, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R344 | 05:44 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.52, "before": 85.58, "loss": 0.065, "playerId": 2735} |
| R344 | 05:44 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 31000, "edgeProgressPermille": 863, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.8639910813823858, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R344 | 05:44 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.6, "before": 76.65, "loss": 0.055, "playerId": 2707} |
| R345 | 05:45 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 4000, "edgeProgressPermille": 75, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.07590132827324478, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R345 | 05:45 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.46, "before": 85.52, "loss": 0.065, "playerId": 2735} |
| R345 | 05:45 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 32000, "edgeProgressPermille": 891, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.8918617614269788, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R345 | 05:45 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.54, "before": 76.6, "loss": 0.055, "playerId": 2707} |
| R346 | 05:46 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 33000, "edgeProgressPermille": 919, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.919732441471572, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R346 | 05:46 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.49, "before": 76.54, "loss": 0.055, "playerId": 2707} |
| R346 | 05:46 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 5000, "edgeProgressPermille": 94, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.09487666034155598, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R346 | 05:46 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.4, "before": 85.46, "loss": 0.065, "playerId": 2735} |
| R347 | 05:47 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 34000, "edgeProgressPermille": 947, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.947603121516165, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R347 | 05:47 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.43, "before": 76.49, "loss": 0.055, "playerId": 2707} |
| R347 | 05:47 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 6000, "edgeProgressPermille": 113, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.11385199240986717, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R347 | 05:47 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.34, "before": 85.4, "loss": 0.065, "playerId": 2735} |
| R348 | 05:48 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 7000, "edgeProgressPermille": 132, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.13282732447817835, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R348 | 05:48 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.28, "before": 85.34, "loss": 0.065, "playerId": 2735} |
| R348 | 05:48 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 35000, "edgeProgressPermille": 975, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 0.9754738015607581, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R348 | 05:48 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.38, "before": 76.43, "loss": 0.055, "playerId": 2707} |
| R349 | 05:49 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 8000, "edgeProgressPermille": 151, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.15180265654648956, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R349 | 05:49 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.18, "before": 85.28, "loss": 0.0975, "playerId": 2735} |
| R349 | 05:49 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 35880, "edgeProgressPermille": 1000, "edgeTotalMs": 35880, "fromNodeId": "S02", "playerId": 2707, "progress": 1.0, "routeEdgeId": "E02", "toNodeId": "S03"} |
| R349 | 05:49 | HIGH | 进点 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 进入 梅关驿(S03) |
| R349 | 05:49 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.3, "before": 76.38, "loss": 0.0825, "playerId": 2707} |
| R350 | 05:50 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 2, "targetNodeId": "S03"} |
| R350 | 05:50 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.23, "before": 76.3, "loss": 0.07500000000000001, "playerId": 2707} |
| R350 | 05:50 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 9000, "edgeProgressPermille": 170, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.17077798861480076, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R350 | 05:50 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 85.08, "before": 85.18, "loss": 0.0975, "playerId": 2735} |
| R351 | 05:51 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 1, "targetNodeId": "S03"} |
| R351 | 05:51 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.16, "before": 76.23, "loss": 0.07500000000000001, "playerId": 2707} |
| R351 | 05:51 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 10000, "edgeProgressPermille": 189, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.18975332068311196, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R351 | 05:51 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.98, "before": 85.08, "loss": 0.0975, "playerId": 2735} |
| R352 | 05:52 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 11000, "edgeProgressPermille": 208, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.20872865275142316, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R352 | 05:52 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.88, "before": 84.98, "loss": 0.0975, "playerId": 2735} |
| R352 | 05:52 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 0, "targetNodeId": "S03"} |
| R352 | 05:52 | HIGH | 任务完成 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 完成 限时过关，+30 分，任务分 30 |
| R352 | 05:52 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.09, "before": 76.16, "loss": 0.07500000000000001, "playerId": 2707} |
| R353 | 05:53 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 12000, "edgeProgressPermille": 227, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.22770398481973433, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R353 | 05:53 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.78, "before": 84.88, "loss": 0.0975, "playerId": 2735} |
| R353 | 05:53 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 13, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.013935340022296544, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R353 | 05:53 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 76.01, "before": 76.09, "loss": 0.0825, "playerId": 2707} |
| R354 | 05:54 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 27, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.027870680044593088, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R354 | 05:54 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 75.93, "before": 76.01, "loss": 0.0825, "playerId": 2707} |
| R354 | 05:54 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 13000, "edgeProgressPermille": 246, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.24667931688804554, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R354 | 05:54 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.68, "before": 84.78, "loss": 0.0975, "playerId": 2735} |
| R355 | 05:55 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 41, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.04180602006688963, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R355 | 05:55 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 75.85, "before": 75.93, "loss": 0.0825, "playerId": 2707} |
| R355 | 05:55 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 14000, "edgeProgressPermille": 265, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.2656546489563567, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R355 | 05:55 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.58, "before": 84.68, "loss": 0.0975, "playerId": 2735} |
| R356 | 05:56 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 15000, "edgeProgressPermille": 284, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.2846299810246679, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R356 | 05:56 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.48, "before": 84.58, "loss": 0.0975, "playerId": 2735} |
| R356 | 05:56 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 55, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.055741360089186176, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R356 | 05:56 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 75.77, "before": 75.85, "loss": 0.0825, "playerId": 2707} |
| R357 | 05:57 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 16000, "edgeProgressPermille": 303, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.3036053130929791, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R357 | 05:57 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.38, "before": 84.48, "loss": 0.0975, "playerId": 2735} |
| R357 | 05:57 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 69, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.06967670011148272, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R357 | 05:57 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 75.69, "before": 75.77, "loss": 0.0825, "playerId": 2707} |
| R358 | 05:58 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 83, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.08361204013377926, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R358 | 05:58 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 75.61, "before": 75.69, "loss": 0.0825, "playerId": 2707} |
| R358 | 05:58 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 17000, "edgeProgressPermille": 322, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.3225806451612903, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R358 | 05:58 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.28, "before": 84.38, "loss": 0.0975, "playerId": 2735} |
| R359 | 05:59 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 97, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.09754738015607581, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R359 | 05:59 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 75.53, "before": 75.61, "loss": 0.0825, "playerId": 2707} |
| R359 | 05:59 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 18000, "edgeProgressPermille": 341, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.3415559772296015, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R359 | 05:59 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.18, "before": 84.28, "loss": 0.0975, "playerId": 2735} |
| R360 | 06:00 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 19000, "edgeProgressPermille": 360, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.3605313092979127, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R360 | 06:00 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 84.08, "before": 84.18, "loss": 0.0975, "playerId": 2735} |
| R360 | 06:00 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 111, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.11148272017837235, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R360 | 06:00 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 75.45, "before": 75.53, "loss": 0.0825, "playerId": 2707} |
| R360 | 06:00 | MED | 任务刷新 |  | T_018 刷新在 秦岭栈道(S08)，路线 MOUNTAIN，截止 R540 |
| R360 | 06:00 | MED | 任务刷新 |  | T_019 刷新在 洛阳驿(S09)，路线 WATER，截止 R540 |
| R361 | 06:01 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 20000, "edgeProgressPermille": 379, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.3795066413662239, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R361 | 06:01 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 83.98, "before": 84.08, "loss": 0.0975, "playerId": 2735} |
| R361 | 06:01 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 125, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.1254180602006689, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R361 | 06:01 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 75.37, "before": 75.45, "loss": 0.0825, "playerId": 2707} |
| R362 | 06:02 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 139, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.13935340022296544, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R362 | 06:02 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 75.29, "before": 75.37, "loss": 0.0825, "playerId": 2707} |
| R362 | 06:02 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 21000, "edgeProgressPermille": 398, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.3984819734345351, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R362 | 06:02 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 83.88, "before": 83.98, "loss": 0.0975, "playerId": 2735} |
| R363 | 06:03 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 153, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.15328874024526198, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R363 | 06:03 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 75.21, "before": 75.29, "loss": 0.0825, "playerId": 2707} |
| R363 | 06:03 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 22000, "edgeProgressPermille": 417, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.4174573055028463, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R363 | 06:03 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 83.78, "before": 83.88, "loss": 0.0975, "playerId": 2735} |
| R364 | 06:04 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 23000, "edgeProgressPermille": 436, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.4364326375711575, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R364 | 06:04 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 83.68, "before": 83.78, "loss": 0.0975, "playerId": 2735} |
| R364 | 06:04 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 12000, "edgeProgressPermille": 167, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.16722408026755853, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R364 | 06:04 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 75.13, "before": 75.21, "loss": 0.0825, "playerId": 2707} |
| R365 | 06:05 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 24000, "edgeProgressPermille": 455, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.45540796963946867, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R365 | 06:05 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 83.58, "before": 83.68, "loss": 0.0975, "playerId": 2735} |
| R365 | 06:05 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 13000, "edgeProgressPermille": 181, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.18115942028985507, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R365 | 06:05 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 75.05, "before": 75.13, "loss": 0.0825, "playerId": 2707} |
| R366 | 06:06 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 195, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.19509476031215162, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R366 | 06:06 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 74.97, "before": 75.05, "loss": 0.0825, "playerId": 2707} |
| R366 | 06:06 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 25000, "edgeProgressPermille": 474, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.47438330170777987, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R366 | 06:06 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 83.48, "before": 83.58, "loss": 0.0975, "playerId": 2735} |
| R367 | 06:07 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 15000, "edgeProgressPermille": 209, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.20903010033444816, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R367 | 06:07 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 74.89, "before": 74.97, "loss": 0.0825, "playerId": 2707} |
| R367 | 06:07 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 26000, "edgeProgressPermille": 493, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.49335863377609107, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R367 | 06:07 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 83.38, "before": 83.48, "loss": 0.0975, "playerId": 2735} |
| R368 | 06:08 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 27000, "edgeProgressPermille": 512, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.5123339658444023, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R368 | 06:08 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 83.28, "before": 83.38, "loss": 0.0975, "playerId": 2735} |
| R368 | 06:08 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 16000, "edgeProgressPermille": 222, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.2229654403567447, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R368 | 06:08 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 74.81, "before": 74.89, "loss": 0.0825, "playerId": 2707} |
| R369 | 06:09 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 28000, "edgeProgressPermille": 531, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.5313092979127134, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R369 | 06:09 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 83.18, "before": 83.28, "loss": 0.0975, "playerId": 2735} |
| R369 | 06:09 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 17000, "edgeProgressPermille": 236, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.23690078037904125, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R369 | 06:09 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 74.73, "before": 74.81, "loss": 0.0825, "playerId": 2707} |
| R370 | 06:10 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 18000, "edgeProgressPermille": 250, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.2508361204013378, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R370 | 06:10 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 74.65, "before": 74.73, "loss": 0.0825, "playerId": 2707} |
| R370 | 06:10 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 29000, "edgeProgressPermille": 550, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.5502846299810247, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R370 | 06:10 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 83.08, "before": 83.18, "loss": 0.0975, "playerId": 2735} |
| R371 | 06:11 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 19000, "edgeProgressPermille": 264, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.26477146042363436, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R371 | 06:11 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 74.57, "before": 74.65, "loss": 0.0825, "playerId": 2707} |
| R371 | 06:11 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 30000, "edgeProgressPermille": 569, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.5692599620493358, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R371 | 06:11 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 82.98, "before": 83.08, "loss": 0.0975, "playerId": 2735} |
| R372 | 06:12 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 31000, "edgeProgressPermille": 588, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.5882352941176471, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R372 | 06:12 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 82.88, "before": 82.98, "loss": 0.0975, "playerId": 2735} |
| R372 | 06:12 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 20000, "edgeProgressPermille": 278, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.2787068004459309, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R372 | 06:12 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 74.49, "before": 74.57, "loss": 0.0825, "playerId": 2707} |
| R373 | 06:13 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 32000, "edgeProgressPermille": 607, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.6072106261859582, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R373 | 06:13 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 82.78, "before": 82.88, "loss": 0.0975, "playerId": 2735} |
| R373 | 06:13 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 21000, "edgeProgressPermille": 292, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.29264214046822745, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R373 | 06:13 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 74.41, "before": 74.49, "loss": 0.0825, "playerId": 2707} |
| R374 | 06:14 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 22000, "edgeProgressPermille": 306, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.30657748049052397, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R374 | 06:14 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 74.33, "before": 74.41, "loss": 0.0825, "playerId": 2707} |
| R374 | 06:14 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 33000, "edgeProgressPermille": 626, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.6261859582542695, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R374 | 06:14 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 82.68, "before": 82.78, "loss": 0.0975, "playerId": 2735} |
| R375 | 06:15 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 23000, "edgeProgressPermille": 320, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.32051282051282054, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R375 | 06:15 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 74.25, "before": 74.33, "loss": 0.0825, "playerId": 2707} |
| R375 | 06:15 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 34000, "edgeProgressPermille": 645, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.6451612903225806, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R375 | 06:15 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 82.58, "before": 82.68, "loss": 0.0975, "playerId": 2735} |
| R376 | 06:16 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 35000, "edgeProgressPermille": 664, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.6641366223908919, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R376 | 06:16 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 82.48, "before": 82.58, "loss": 0.0975, "playerId": 2735} |
| R376 | 06:16 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 24000, "edgeProgressPermille": 334, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.33444816053511706, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R376 | 06:16 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 74.17, "before": 74.25, "loss": 0.0825, "playerId": 2707} |
| R377 | 06:17 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 36000, "edgeProgressPermille": 683, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.683111954459203, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R377 | 06:17 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 82.38, "before": 82.48, "loss": 0.0975, "playerId": 2735} |
| R377 | 06:17 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 25000, "edgeProgressPermille": 348, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.34838350055741363, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R377 | 06:17 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 74.09, "before": 74.17, "loss": 0.0825, "playerId": 2707} |
| R378 | 06:18 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 26000, "edgeProgressPermille": 362, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.36231884057971014, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R378 | 06:18 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 74.01, "before": 74.09, "loss": 0.0825, "playerId": 2707} |
| R378 | 06:18 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 37000, "edgeProgressPermille": 702, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.7020872865275142, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R378 | 06:18 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 82.28, "before": 82.38, "loss": 0.0975, "playerId": 2735} |
| R379 | 06:19 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 27000, "edgeProgressPermille": 376, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.3762541806020067, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R379 | 06:19 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 73.93, "before": 74.01, "loss": 0.0825, "playerId": 2707} |
| R379 | 06:19 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 38000, "edgeProgressPermille": 721, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.7210626185958254, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R379 | 06:19 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 82.18, "before": 82.28, "loss": 0.0975, "playerId": 2735} |
| R380 | 06:20 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 39000, "edgeProgressPermille": 740, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.7400379506641366, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R380 | 06:20 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 82.08, "before": 82.18, "loss": 0.0975, "playerId": 2735} |
| R380 | 06:20 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 28000, "edgeProgressPermille": 390, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.39018952062430323, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R380 | 06:20 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 73.85, "before": 73.93, "loss": 0.0825, "playerId": 2707} |
| R381 | 06:21 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 40000, "edgeProgressPermille": 759, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.7590132827324478, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R381 | 06:21 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 81.98, "before": 82.08, "loss": 0.0975, "playerId": 2735} |
| R381 | 06:21 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 29000, "edgeProgressPermille": 404, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.4041248606465998, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R381 | 06:21 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 73.77, "before": 73.85, "loss": 0.0825, "playerId": 2707} |
| R382 | 06:22 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 30000, "edgeProgressPermille": 418, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.4180602006688963, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R382 | 06:22 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 73.69, "before": 73.77, "loss": 0.0825, "playerId": 2707} |
| R382 | 06:22 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 41000, "edgeProgressPermille": 777, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.777988614800759, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R382 | 06:22 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 81.88, "before": 81.98, "loss": 0.0975, "playerId": 2735} |
| R383 | 06:23 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 31000, "edgeProgressPermille": 431, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.4319955406911929, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R383 | 06:23 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 73.61, "before": 73.69, "loss": 0.0825, "playerId": 2707} |
| R383 | 06:23 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 42000, "edgeProgressPermille": 796, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.7969639468690702, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R383 | 06:23 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 81.78, "before": 81.88, "loss": 0.0975, "playerId": 2735} |
| R384 | 06:24 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 43000, "edgeProgressPermille": 815, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.8159392789373814, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R384 | 06:24 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 81.68, "before": 81.78, "loss": 0.0975, "playerId": 2735} |
| R384 | 06:24 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 32000, "edgeProgressPermille": 445, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.4459308807134894, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R384 | 06:24 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 73.53, "before": 73.61, "loss": 0.0825, "playerId": 2707} |
| R385 | 06:25 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 44000, "edgeProgressPermille": 834, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.8349146110056926, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R385 | 06:25 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 81.58, "before": 81.68, "loss": 0.0975, "playerId": 2735} |
| R385 | 06:25 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 33000, "edgeProgressPermille": 459, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.459866220735786, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R385 | 06:25 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 73.45, "before": 73.53, "loss": 0.0825, "playerId": 2707} |
| R386 | 06:26 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 34000, "edgeProgressPermille": 473, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.4738015607580825, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R386 | 06:26 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 73.37, "before": 73.45, "loss": 0.0825, "playerId": 2707} |
| R386 | 06:26 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 45000, "edgeProgressPermille": 853, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.8538899430740038, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R386 | 06:26 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 81.48, "before": 81.58, "loss": 0.0975, "playerId": 2735} |
| R387 | 06:27 | HIGH | 派遣 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 派遣队伍侦察 朱雀门(S14)，预计 R390 完成 |
| R387 | 06:27 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 35000, "edgeProgressPermille": 487, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.48773690078037907, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R387 | 06:27 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 73.29, "before": 73.37, "loss": 0.0825, "playerId": 2707} |
| R387 | 06:27 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 46000, "edgeProgressPermille": 872, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.872865275142315, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R387 | 06:27 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 81.38, "before": 81.48, "loss": 0.0975, "playerId": 2735} |
| R388 | 06:28 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 47000, "edgeProgressPermille": 891, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.8918406072106262, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R388 | 06:28 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 81.28, "before": 81.38, "loss": 0.0975, "playerId": 2735} |
| R388 | 06:28 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 36000, "edgeProgressPermille": 501, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.5016722408026756, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R388 | 06:28 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 73.21, "before": 73.29, "loss": 0.0825, "playerId": 2707} |
| R389 | 06:29 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 48000, "edgeProgressPermille": 910, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.9108159392789373, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R389 | 06:29 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 81.18, "before": 81.28, "loss": 0.0975, "playerId": 2735} |
| R389 | 06:29 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 37000, "edgeProgressPermille": 515, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.5156075808249722, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R389 | 06:29 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 73.13, "before": 73.21, "loss": 0.0825, "playerId": 2707} |
| R390 | 06:30 | MED | SCOUT_MARKER_ADD | BLUE 路人女主队/1.0(2735) | {"expireRound": 435, "playerId": 2735, "remainingTriggers": 1, "targetNodeId": "S14"} |
| R390 | 06:30 | MED | 侦察回报 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 侦察 朱雀门(S14)：无障碍，资源 无明显资源 |
| R390 | 06:30 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 38000, "edgeProgressPermille": 529, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.5295429208472687, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R390 | 06:30 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 73.05, "before": 73.13, "loss": 0.0825, "playerId": 2707} |
| R390 | 06:30 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 49000, "edgeProgressPermille": 929, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.9297912713472486, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R390 | 06:30 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 81.08, "before": 81.18, "loss": 0.0975, "playerId": 2735} |
| R391 | 06:31 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 39000, "edgeProgressPermille": 543, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.5434782608695652, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R391 | 06:31 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 72.97, "before": 73.05, "loss": 0.0825, "playerId": 2707} |
| R391 | 06:31 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 50000, "edgeProgressPermille": 948, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.9487666034155597, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R391 | 06:31 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 80.98, "before": 81.08, "loss": 0.0975, "playerId": 2735} |
| R392 | 06:32 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 51000, "edgeProgressPermille": 967, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.967741935483871, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R392 | 06:32 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 80.88, "before": 80.98, "loss": 0.0975, "playerId": 2735} |
| R392 | 06:32 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 40000, "edgeProgressPermille": 557, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.5574136008918618, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R392 | 06:32 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 72.89, "before": 72.97, "loss": 0.0825, "playerId": 2707} |
| R393 | 06:33 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 52000, "edgeProgressPermille": 986, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 0.9867172675521821, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R393 | 06:33 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 80.78, "before": 80.88, "loss": 0.0975, "playerId": 2735} |
| R393 | 06:33 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 41000, "edgeProgressPermille": 571, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.5713489409141583, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R393 | 06:33 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 72.81, "before": 72.89, "loss": 0.0825, "playerId": 2707} |
| R394 | 06:34 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 42000, "edgeProgressPermille": 585, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.5852842809364549, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R394 | 06:34 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 72.73, "before": 72.81, "loss": 0.0825, "playerId": 2707} |
| R394 | 06:34 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 52700, "edgeProgressPermille": 1000, "edgeTotalMs": 52700, "fromNodeId": "S11", "playerId": 2735, "progress": 1.0, "routeEdgeId": "E23", "toNodeId": "S14"} |
| R394 | 06:34 | HIGH | 进点 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 进入 朱雀门(S14) |
| R394 | 06:34 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 80.68, "before": 80.78, "loss": 0.0975, "playerId": 2735} |
| R395 | 06:35 | HIGH | 冲刺开始 |  | 比赛进入冲刺阶段，触发回合 R395 |
| R395 | 06:35 | MED | RUSH_TACTIC_USE | RED AAAA/v1.0(2707) | {"durationRound": 15, "playerId": 2707, "rushTactic": "RUSH_SPEED"} |
| R395 | 06:35 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 43300, "edgeProgressPermille": 603, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.6034002229654404, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R395 | 06:35 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 72.63, "before": 72.73, "loss": 0.10312500000000001, "playerId": 2707} |
| R395 | 06:35 | MED | SCOUT_MARKER_APPLY | BLUE 路人女主队/1.0(2735) | {"afterRound": 3, "beforeRound": 6, "playerId": 2735, "processType": "VERIFY", "targetNodeId": "S14"} |
| R395 | 06:35 | MED | PROCESS_PROGRESS | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "processType": "VERIFY_GATE", "remainingRound": 2, "targetNodeId": "S14"} |
| R395 | 06:35 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 80.61, "before": 80.68, "loss": 0.07500000000000001, "playerId": 2735} |
| R396 | 06:36 | MED | PROCESS_PROGRESS | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "processType": "VERIFY_GATE", "remainingRound": 1, "targetNodeId": "S14"} |
| R396 | 06:36 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 80.54, "before": 80.61, "loss": 0.07500000000000001, "playerId": 2735} |
| R396 | 06:36 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 44600, "edgeProgressPermille": 621, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.6215161649944259, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R396 | 06:36 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 72.53, "before": 72.63, "loss": 0.10312500000000001, "playerId": 2707} |
| R397 | 06:37 | MED | PROCESS_PROGRESS | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "processType": "VERIFY_GATE", "remainingRound": 0, "targetNodeId": "S14"} |
| R397 | 06:37 | MED | SCOUT_MARKER_CONSUME | BLUE 路人女主队/1.0(2735) | {"playerId": 2735, "remainingTriggers": 0, "targetNodeId": "S14"} |
| R397 | 06:37 | HIGH | 验关完成 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 通过 朱雀门(S14) 验关 |
| R397 | 06:37 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 80.47, "before": 80.54, "loss": 0.07500000000000001, "playerId": 2735} |
| R397 | 06:37 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 45900, "edgeProgressPermille": 639, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.6396321070234113, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R397 | 06:37 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 72.43, "before": 72.53, "loss": 0.10312500000000001, "playerId": 2707} |
| R398 | 06:38 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 47200, "edgeProgressPermille": 657, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.6577480490523969, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R398 | 06:38 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 72.33, "before": 72.43, "loss": 0.10312500000000001, "playerId": 2707} |
| R398 | 06:38 | MED | RUSH_TACTIC_USE | BLUE 路人女主队/1.0(2735) | {"durationRound": 30, "playerId": 2735, "rushTactic": "RUSH_PROTECT"} |
| R398 | 06:38 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 80.46, "before": 80.47, "loss": 0.015000000000000003, "playerId": 2735} |
| R399 | 06:39 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 48500, "edgeProgressPermille": 675, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.6758639910813824, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R399 | 06:39 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 72.23, "before": 72.33, "loss": 0.10312500000000001, "playerId": 2707} |
| R399 | 06:39 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 1000, "edgeProgressPermille": 362, "edgeTotalMs": 2760, "fromNodeId": "S14", "playerId": 2735, "progress": 0.36231884057971014, "routeEdgeId": "E10", "toNodeId": "S15"} |
| R399 | 06:39 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 80.44, "before": 80.46, "loss": 0.0165, "playerId": 2735} |
| R400 | 06:40 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 2000, "edgeProgressPermille": 724, "edgeTotalMs": 2760, "fromNodeId": "S14", "playerId": 2735, "progress": 0.7246376811594203, "routeEdgeId": "E10", "toNodeId": "S15"} |
| R400 | 06:40 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 80.42, "before": 80.44, "loss": 0.0165, "playerId": 2735} |
| R400 | 06:40 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 49800, "edgeProgressPermille": 693, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.6939799331103679, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R400 | 06:40 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 72.13, "before": 72.23, "loss": 0.10312500000000001, "playerId": 2707} |
| R401 | 06:41 | MED | MOVE_PROGRESS | BLUE 路人女主队/1.0(2735) | {"edgeProgressMs": 2760, "edgeProgressPermille": 1000, "edgeTotalMs": 2760, "fromNodeId": "S14", "playerId": 2735, "progress": 1.0, "routeEdgeId": "E10", "toNodeId": "S15"} |
| R401 | 06:41 | HIGH | 进点 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 进入 兴庆宫(S15) |
| R401 | 06:41 | MED | FRESHNESS_DROP | BLUE 路人女主队/1.0(2735) | {"after": 80.4, "before": 80.42, "loss": 0.0165, "playerId": 2735} |
| R401 | 06:41 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 51100, "edgeProgressPermille": 712, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.7120958751393534, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R401 | 06:41 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 72.03, "before": 72.13, "loss": 0.10312500000000001, "playerId": 2707} |
| R402 | 06:42 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 52400, "edgeProgressPermille": 730, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.7302118171683389, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R402 | 06:42 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 71.93, "before": 72.03, "loss": 0.10312500000000001, "playerId": 2707} |
| R402 | 06:42 | HIGH | 送达成功 | BLUE 路人女主队/1.0(2735) | BLUE 路人女主队/1.0(2735) 成功送达，好果 99，新鲜度 80.4，总分 612 |
| R403 | 06:43 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 53700, "edgeProgressPermille": 748, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.7483277591973244, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R403 | 06:43 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 71.83, "before": 71.93, "loss": 0.10312500000000001, "playerId": 2707} |
| R404 | 06:44 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 55000, "edgeProgressPermille": 766, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.7664437012263099, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R404 | 06:44 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 71.73, "before": 71.83, "loss": 0.10312500000000001, "playerId": 2707} |
| R405 | 06:45 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 56300, "edgeProgressPermille": 784, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.7845596432552955, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R405 | 06:45 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 71.63, "before": 71.73, "loss": 0.10312500000000001, "playerId": 2707} |
| R406 | 06:46 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 57600, "edgeProgressPermille": 802, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.802675585284281, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R406 | 06:46 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 71.53, "before": 71.63, "loss": 0.10312500000000001, "playerId": 2707} |
| R407 | 06:47 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 58900, "edgeProgressPermille": 820, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.8207915273132664, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R407 | 06:47 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 71.43, "before": 71.53, "loss": 0.10312500000000001, "playerId": 2707} |
| R408 | 06:48 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 60200, "edgeProgressPermille": 838, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.8389074693422519, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R408 | 06:48 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 71.33, "before": 71.43, "loss": 0.10312500000000001, "playerId": 2707} |
| R409 | 06:49 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 61500, "edgeProgressPermille": 857, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.8570234113712375, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R409 | 06:49 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 71.26, "before": 71.33, "loss": 0.06875, "playerId": 2707} |
| R410 | 06:50 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 62500, "edgeProgressPermille": 870, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.870958751393534, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R410 | 06:50 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 71.21, "before": 71.26, "loss": 0.055, "playerId": 2707} |
| R411 | 06:51 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 63500, "edgeProgressPermille": 884, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.8848940914158305, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R411 | 06:51 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 71.15, "before": 71.21, "loss": 0.055, "playerId": 2707} |
| R412 | 06:52 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 64500, "edgeProgressPermille": 898, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.8988294314381271, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R412 | 06:52 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 71.1, "before": 71.15, "loss": 0.055, "playerId": 2707} |
| R413 | 06:53 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 65500, "edgeProgressPermille": 912, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.9127647714604237, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R413 | 06:53 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 71.04, "before": 71.1, "loss": 0.055, "playerId": 2707} |
| R414 | 06:54 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 66500, "edgeProgressPermille": 926, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.9267001114827201, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R414 | 06:54 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.99, "before": 71.04, "loss": 0.055, "playerId": 2707} |
| R415 | 06:55 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 67500, "edgeProgressPermille": 940, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.9406354515050167, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R415 | 06:55 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.93, "before": 70.99, "loss": 0.055, "playerId": 2707} |
| R416 | 06:56 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 68500, "edgeProgressPermille": 954, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.9545707915273133, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R416 | 06:56 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.88, "before": 70.93, "loss": 0.055, "playerId": 2707} |
| R417 | 06:57 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 69500, "edgeProgressPermille": 968, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.9685061315496098, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R417 | 06:57 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.82, "before": 70.88, "loss": 0.055, "playerId": 2707} |
| R418 | 06:58 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 70500, "edgeProgressPermille": 982, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.9824414715719063, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R418 | 06:58 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.76, "before": 70.82, "loss": 0.055, "playerId": 2707} |
| R419 | 06:59 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 71500, "edgeProgressPermille": 996, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 0.9963768115942029, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R419 | 06:59 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.71, "before": 70.76, "loss": 0.055, "playerId": 2707} |
| R420 | 07:00 | MED | 任务过期 |  | T_010 在 洞庭水驿(S05) 过期 |
| R420 | 07:00 | MED | 任务过期 |  | T_011 在 江南码头(S04) 过期 |
| R420 | 07:00 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 71760, "edgeProgressPermille": 1000, "edgeTotalMs": 71760, "fromNodeId": "S03", "playerId": 2707, "progress": 1.0, "routeEdgeId": "E03", "toNodeId": "S07"} |
| R420 | 07:00 | HIGH | 进点 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 进入 荆襄大驿(S07) |
| R420 | 07:00 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.65, "before": 70.71, "loss": 0.055, "playerId": 2707} |
| R421 | 07:01 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 3, "targetNodeId": "S07"} |
| R421 | 07:01 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.6, "before": 70.65, "loss": 0.05, "playerId": 2707} |
| R422 | 07:02 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 2, "targetNodeId": "S07"} |
| R422 | 07:02 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.55, "before": 70.6, "loss": 0.05, "playerId": 2707} |
| R423 | 07:03 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 1, "targetNodeId": "S07"} |
| R423 | 07:03 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.5, "before": 70.55, "loss": 0.05, "playerId": 2707} |
| R424 | 07:04 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLAIM_TASK", "remainingRound": 0, "targetNodeId": "S07"} |
| R424 | 07:04 | HIGH | 任务完成 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 完成 抵驿催运，+30 分，任务分 60 |
| R424 | 07:04 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.45, "before": 70.5, "loss": 0.05, "playerId": 2707} |
| R425 | 07:05 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 5, "targetNodeId": "S05"} |
| R425 | 07:05 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.4, "before": 70.45, "loss": 0.05, "playerId": 2707} |
| R426 | 07:06 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 4, "targetNodeId": "S05"} |
| R426 | 07:06 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.35, "before": 70.4, "loss": 0.05, "playerId": 2707} |
| R427 | 07:07 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 3, "targetNodeId": "S05"} |
| R427 | 07:07 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.3, "before": 70.35, "loss": 0.05, "playerId": 2707} |
| R428 | 07:08 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 2, "targetNodeId": "S05"} |
| R428 | 07:08 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.25, "before": 70.3, "loss": 0.05, "playerId": 2707} |
| R429 | 07:09 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 1, "targetNodeId": "S05"} |
| R429 | 07:09 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.2, "before": 70.25, "loss": 0.05, "playerId": 2707} |
| R430 | 07:10 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "CLEAR_OBSTACLE", "remainingRound": 0, "targetNodeId": "S05"} |
| R430 | 07:10 | HIGH | 障碍清除 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 清除 洞庭水驿(S05) 障碍 |
| R430 | 07:10 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.15, "before": 70.2, "loss": 0.05, "playerId": 2707} |
| R431 | 07:11 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 7, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.007501875468867217, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R431 | 07:11 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.09, "before": 70.15, "loss": 0.065, "playerId": 2707} |
| R432 | 07:12 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 15, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.015003750937734433, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R432 | 07:12 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 70.03, "before": 70.09, "loss": 0.065, "playerId": 2707} |
| R433 | 07:13 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 22, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.02250562640660165, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R433 | 07:13 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.97, "before": 70.03, "loss": 0.065, "playerId": 2707} |
| R433 | 07:13 | HIGH | 果品折损 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 好果跌破阈值 70，坏果 3 |
| R434 | 07:14 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 30, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.030007501875468866, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R434 | 07:14 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.91, "before": 69.97, "loss": 0.065, "playerId": 2707} |
| R435 | 07:15 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 37, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.037509377344336084, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R435 | 07:15 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.85, "before": 69.91, "loss": 0.065, "playerId": 2707} |
| R436 | 07:16 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 45, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.0450112528132033, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R436 | 07:16 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.79, "before": 69.85, "loss": 0.065, "playerId": 2707} |
| R437 | 07:17 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 52, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.05251312828207052, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R437 | 07:17 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.73, "before": 69.79, "loss": 0.065, "playerId": 2707} |
| R438 | 07:18 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 60, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.06001500375093773, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R438 | 07:18 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.67, "before": 69.73, "loss": 0.065, "playerId": 2707} |
| R439 | 07:19 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 67, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.06751687921980495, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R439 | 07:19 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.61, "before": 69.67, "loss": 0.065, "playerId": 2707} |
| R440 | 07:20 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 75, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.07501875468867217, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R440 | 07:20 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.55, "before": 69.61, "loss": 0.065, "playerId": 2707} |
| R441 | 07:21 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 82, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.08252063015753938, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R441 | 07:21 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.49, "before": 69.55, "loss": 0.065, "playerId": 2707} |
| R442 | 07:22 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 12000, "edgeProgressPermille": 90, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.0900225056264066, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R442 | 07:22 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.43, "before": 69.49, "loss": 0.065, "playerId": 2707} |
| R443 | 07:23 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 13000, "edgeProgressPermille": 97, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.09752438109527382, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R443 | 07:23 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.37, "before": 69.43, "loss": 0.065, "playerId": 2707} |
| R444 | 07:24 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 105, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.10502625656414104, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R444 | 07:24 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.31, "before": 69.37, "loss": 0.065, "playerId": 2707} |
| R445 | 07:25 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 15000, "edgeProgressPermille": 112, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.11252813203300825, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R445 | 07:25 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.25, "before": 69.31, "loss": 0.065, "playerId": 2707} |
| R446 | 07:26 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 16000, "edgeProgressPermille": 120, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.12003000750187547, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R446 | 07:26 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.19, "before": 69.25, "loss": 0.065, "playerId": 2707} |
| R447 | 07:27 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 17000, "edgeProgressPermille": 127, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.1275318829707427, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R447 | 07:27 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.13, "before": 69.19, "loss": 0.065, "playerId": 2707} |
| R448 | 07:28 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 18000, "edgeProgressPermille": 135, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.1350337584396099, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R448 | 07:28 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.07, "before": 69.13, "loss": 0.065, "playerId": 2707} |
| R449 | 07:29 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 19000, "edgeProgressPermille": 142, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.14253563390847712, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R449 | 07:29 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 69.01, "before": 69.07, "loss": 0.065, "playerId": 2707} |
| R450 | 07:30 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 20000, "edgeProgressPermille": 150, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.15003750937734434, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R450 | 07:30 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.95, "before": 69.01, "loss": 0.065, "playerId": 2707} |
| R451 | 07:31 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 21000, "edgeProgressPermille": 157, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.15753938484621155, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R451 | 07:31 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.89, "before": 68.95, "loss": 0.065, "playerId": 2707} |
| R452 | 07:32 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 22000, "edgeProgressPermille": 165, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.16504126031507876, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R452 | 07:32 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.83, "before": 68.89, "loss": 0.065, "playerId": 2707} |
| R453 | 07:33 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 23000, "edgeProgressPermille": 172, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.17254313578394598, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R453 | 07:33 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.77, "before": 68.83, "loss": 0.065, "playerId": 2707} |
| R454 | 07:34 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 24000, "edgeProgressPermille": 180, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.1800450112528132, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R454 | 07:34 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.71, "before": 68.77, "loss": 0.065, "playerId": 2707} |
| R455 | 07:35 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 25000, "edgeProgressPermille": 187, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.18754688672168043, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R455 | 07:35 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.65, "before": 68.71, "loss": 0.065, "playerId": 2707} |
| R456 | 07:36 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 26000, "edgeProgressPermille": 195, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.19504876219054765, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R456 | 07:36 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.59, "before": 68.65, "loss": 0.065, "playerId": 2707} |
| R457 | 07:37 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 27000, "edgeProgressPermille": 202, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.20255063765941486, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R457 | 07:37 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.53, "before": 68.59, "loss": 0.065, "playerId": 2707} |
| R458 | 07:38 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 28000, "edgeProgressPermille": 210, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.21005251312828208, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R458 | 07:38 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.47, "before": 68.53, "loss": 0.065, "playerId": 2707} |
| R459 | 07:39 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 29000, "edgeProgressPermille": 217, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.2175543885971493, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R459 | 07:39 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.41, "before": 68.47, "loss": 0.065, "playerId": 2707} |
| R460 | 07:40 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 30000, "edgeProgressPermille": 225, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.2250562640660165, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R460 | 07:40 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.35, "before": 68.41, "loss": 0.065, "playerId": 2707} |
| R461 | 07:41 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 31000, "edgeProgressPermille": 232, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.23255813953488372, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R461 | 07:41 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.29, "before": 68.35, "loss": 0.065, "playerId": 2707} |
| R462 | 07:42 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 32000, "edgeProgressPermille": 240, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.24006001500375093, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R462 | 07:42 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.23, "before": 68.29, "loss": 0.065, "playerId": 2707} |
| R463 | 07:43 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 33000, "edgeProgressPermille": 247, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.24756189047261815, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R463 | 07:43 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.17, "before": 68.23, "loss": 0.065, "playerId": 2707} |
| R464 | 07:44 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 34000, "edgeProgressPermille": 255, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.2550637659414854, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R464 | 07:44 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.11, "before": 68.17, "loss": 0.065, "playerId": 2707} |
| R465 | 07:45 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 35000, "edgeProgressPermille": 262, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.2625656414103526, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R465 | 07:45 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 68.05, "before": 68.11, "loss": 0.065, "playerId": 2707} |
| R466 | 07:46 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 36000, "edgeProgressPermille": 270, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.2700675168792198, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R466 | 07:46 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.99, "before": 68.05, "loss": 0.065, "playerId": 2707} |
| R467 | 07:47 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 37000, "edgeProgressPermille": 277, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.27756939234808703, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R467 | 07:47 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.93, "before": 67.99, "loss": 0.065, "playerId": 2707} |
| R468 | 07:48 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 38000, "edgeProgressPermille": 285, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.28507126781695424, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R468 | 07:48 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.87, "before": 67.93, "loss": 0.065, "playerId": 2707} |
| R469 | 07:49 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 39000, "edgeProgressPermille": 292, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.29257314328582146, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R469 | 07:49 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.81, "before": 67.87, "loss": 0.065, "playerId": 2707} |
| R470 | 07:50 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 40000, "edgeProgressPermille": 300, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.30007501875468867, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R470 | 07:50 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.75, "before": 67.81, "loss": 0.065, "playerId": 2707} |
| R471 | 07:51 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 41000, "edgeProgressPermille": 307, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.3075768942235559, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R471 | 07:51 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.69, "before": 67.75, "loss": 0.065, "playerId": 2707} |
| R472 | 07:52 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 42000, "edgeProgressPermille": 315, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.3150787696924231, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R472 | 07:52 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.63, "before": 67.69, "loss": 0.065, "playerId": 2707} |
| R473 | 07:53 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 43000, "edgeProgressPermille": 322, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.3225806451612903, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R473 | 07:53 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.57, "before": 67.63, "loss": 0.065, "playerId": 2707} |
| R474 | 07:54 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 44000, "edgeProgressPermille": 330, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.3300825206301575, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R474 | 07:54 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.51, "before": 67.57, "loss": 0.065, "playerId": 2707} |
| R475 | 07:55 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 45000, "edgeProgressPermille": 337, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.33758439609902474, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R475 | 07:55 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.45, "before": 67.51, "loss": 0.065, "playerId": 2707} |
| R476 | 07:56 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 46000, "edgeProgressPermille": 345, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.34508627156789196, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R476 | 07:56 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.39, "before": 67.45, "loss": 0.065, "playerId": 2707} |
| R477 | 07:57 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 47000, "edgeProgressPermille": 352, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.35258814703675917, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R477 | 07:57 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.33, "before": 67.39, "loss": 0.065, "playerId": 2707} |
| R478 | 07:58 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 48000, "edgeProgressPermille": 360, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.3600900225056264, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R478 | 07:58 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.27, "before": 67.33, "loss": 0.065, "playerId": 2707} |
| R479 | 07:59 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 49000, "edgeProgressPermille": 367, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.3675918979744936, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R479 | 07:59 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.21, "before": 67.27, "loss": 0.065, "playerId": 2707} |
| R480 | 08:00 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 50000, "edgeProgressPermille": 375, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.37509377344336087, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R480 | 08:00 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.15, "before": 67.21, "loss": 0.065, "playerId": 2707} |
| R481 | 08:01 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 51000, "edgeProgressPermille": 382, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.3825956489122281, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R481 | 08:01 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.09, "before": 67.15, "loss": 0.065, "playerId": 2707} |
| R482 | 08:02 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 52000, "edgeProgressPermille": 390, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.3900975243810953, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R482 | 08:02 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 67.03, "before": 67.09, "loss": 0.065, "playerId": 2707} |
| R483 | 08:03 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 53000, "edgeProgressPermille": 397, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.3975993998499625, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R483 | 08:03 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.97, "before": 67.03, "loss": 0.065, "playerId": 2707} |
| R484 | 08:04 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 54000, "edgeProgressPermille": 405, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.4051012753188297, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R484 | 08:04 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.91, "before": 66.97, "loss": 0.065, "playerId": 2707} |
| R485 | 08:05 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 55000, "edgeProgressPermille": 412, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.41260315078769694, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R485 | 08:05 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.85, "before": 66.91, "loss": 0.065, "playerId": 2707} |
| R486 | 08:06 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 56000, "edgeProgressPermille": 420, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.42010502625656415, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R486 | 08:06 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.79, "before": 66.85, "loss": 0.065, "playerId": 2707} |
| R487 | 08:07 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 57000, "edgeProgressPermille": 427, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.42760690172543137, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R487 | 08:07 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.73, "before": 66.79, "loss": 0.065, "playerId": 2707} |
| R488 | 08:08 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 58000, "edgeProgressPermille": 435, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.4351087771942986, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R488 | 08:08 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.67, "before": 66.73, "loss": 0.065, "playerId": 2707} |
| R489 | 08:09 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 59000, "edgeProgressPermille": 442, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.4426106526631658, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R489 | 08:09 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.61, "before": 66.67, "loss": 0.065, "playerId": 2707} |
| R490 | 08:10 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 60000, "edgeProgressPermille": 450, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.450112528132033, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R490 | 08:10 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.55, "before": 66.61, "loss": 0.065, "playerId": 2707} |
| R491 | 08:11 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 61000, "edgeProgressPermille": 457, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.4576144036009002, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R491 | 08:11 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.49, "before": 66.55, "loss": 0.065, "playerId": 2707} |
| R492 | 08:12 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 62000, "edgeProgressPermille": 465, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.46511627906976744, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R492 | 08:12 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.43, "before": 66.49, "loss": 0.065, "playerId": 2707} |
| R493 | 08:13 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 63000, "edgeProgressPermille": 472, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.47261815453863465, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R493 | 08:13 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.37, "before": 66.43, "loss": 0.065, "playerId": 2707} |
| R494 | 08:14 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 64000, "edgeProgressPermille": 480, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.48012003000750186, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R494 | 08:14 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.31, "before": 66.37, "loss": 0.065, "playerId": 2707} |
| R495 | 08:15 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 65000, "edgeProgressPermille": 487, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.4876219054763691, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R495 | 08:15 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.25, "before": 66.31, "loss": 0.065, "playerId": 2707} |
| R496 | 08:16 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 66000, "edgeProgressPermille": 495, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.4951237809452363, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R496 | 08:16 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.19, "before": 66.25, "loss": 0.065, "playerId": 2707} |
| R497 | 08:17 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 67000, "edgeProgressPermille": 502, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.5026256564141035, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R497 | 08:17 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.13, "before": 66.19, "loss": 0.065, "playerId": 2707} |
| R498 | 08:18 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 68000, "edgeProgressPermille": 510, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.5101275318829708, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R498 | 08:18 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.07, "before": 66.13, "loss": 0.065, "playerId": 2707} |
| R499 | 08:19 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 69000, "edgeProgressPermille": 517, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.5176294073518379, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R499 | 08:19 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 66.01, "before": 66.07, "loss": 0.065, "playerId": 2707} |
| R500 | 08:20 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 70000, "edgeProgressPermille": 525, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.5251312828207052, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R500 | 08:20 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.95, "before": 66.01, "loss": 0.065, "playerId": 2707} |
| R501 | 08:21 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 71000, "edgeProgressPermille": 532, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.5326331582895724, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R501 | 08:21 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.89, "before": 65.95, "loss": 0.065, "playerId": 2707} |
| R502 | 08:22 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 72000, "edgeProgressPermille": 540, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.5401350337584396, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R502 | 08:22 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.83, "before": 65.89, "loss": 0.065, "playerId": 2707} |
| R503 | 08:23 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 73000, "edgeProgressPermille": 547, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.5476369092273068, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R503 | 08:23 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.77, "before": 65.83, "loss": 0.065, "playerId": 2707} |
| R504 | 08:24 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 74000, "edgeProgressPermille": 555, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.5551387846961741, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R504 | 08:24 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.71, "before": 65.77, "loss": 0.065, "playerId": 2707} |
| R505 | 08:25 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 75000, "edgeProgressPermille": 562, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.5626406601650412, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R505 | 08:25 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.65, "before": 65.71, "loss": 0.065, "playerId": 2707} |
| R506 | 08:26 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 76000, "edgeProgressPermille": 570, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.5701425356339085, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R506 | 08:26 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.59, "before": 65.65, "loss": 0.065, "playerId": 2707} |
| R507 | 08:27 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 77000, "edgeProgressPermille": 577, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.5776444111027756, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R507 | 08:27 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.53, "before": 65.59, "loss": 0.065, "playerId": 2707} |
| R508 | 08:28 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 78000, "edgeProgressPermille": 585, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.5851462865716429, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R508 | 08:28 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.47, "before": 65.53, "loss": 0.065, "playerId": 2707} |
| R509 | 08:29 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 79000, "edgeProgressPermille": 592, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.5926481620405101, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R509 | 08:29 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.41, "before": 65.47, "loss": 0.065, "playerId": 2707} |
| R510 | 08:30 | MED | 任务过期 |  | T_017 在 洛阳驿(S09) 过期 |
| R510 | 08:30 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 80000, "edgeProgressPermille": 600, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.6001500375093773, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R510 | 08:30 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.35, "before": 65.41, "loss": 0.065, "playerId": 2707} |
| R511 | 08:31 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 81000, "edgeProgressPermille": 607, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.6076519129782446, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R511 | 08:31 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.29, "before": 65.35, "loss": 0.065, "playerId": 2707} |
| R512 | 08:32 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 82000, "edgeProgressPermille": 615, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.6151537884471118, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R512 | 08:32 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.23, "before": 65.29, "loss": 0.065, "playerId": 2707} |
| R513 | 08:33 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 83000, "edgeProgressPermille": 622, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.622655663915979, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R513 | 08:33 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.17, "before": 65.23, "loss": 0.065, "playerId": 2707} |
| R514 | 08:34 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 84000, "edgeProgressPermille": 630, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.6301575393848462, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R514 | 08:34 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.11, "before": 65.17, "loss": 0.065, "playerId": 2707} |
| R515 | 08:35 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 85000, "edgeProgressPermille": 637, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.6376594148537135, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R515 | 08:35 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 65.05, "before": 65.11, "loss": 0.065, "playerId": 2707} |
| R516 | 08:36 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 86000, "edgeProgressPermille": 645, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.6451612903225806, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R516 | 08:36 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.99, "before": 65.05, "loss": 0.065, "playerId": 2707} |
| R517 | 08:37 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 87000, "edgeProgressPermille": 652, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.6526631657914479, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R517 | 08:37 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.93, "before": 64.99, "loss": 0.065, "playerId": 2707} |
| R518 | 08:38 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 88000, "edgeProgressPermille": 660, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.660165041260315, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R518 | 08:38 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.87, "before": 64.93, "loss": 0.065, "playerId": 2707} |
| R519 | 08:39 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 89000, "edgeProgressPermille": 667, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.6676669167291823, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R519 | 08:39 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.81, "before": 64.87, "loss": 0.065, "playerId": 2707} |
| R520 | 08:40 | MED | 任务过期 |  | T_013 在 五岭山道(S06) 过期 |
| R520 | 08:40 | MED | 任务过期 |  | T_014 在 洞庭水驿(S05) 过期 |
| R520 | 08:40 | MED | 任务过期 |  | T_015 在 洛阳驿(S09) 过期 |
| R520 | 08:40 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 90000, "edgeProgressPermille": 675, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.6751687921980495, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R520 | 08:40 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.75, "before": 64.81, "loss": 0.065, "playerId": 2707} |
| R521 | 08:41 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 91000, "edgeProgressPermille": 682, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.6826706676669168, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R521 | 08:41 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.69, "before": 64.75, "loss": 0.065, "playerId": 2707} |
| R522 | 08:42 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 92000, "edgeProgressPermille": 690, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.6901725431357839, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R522 | 08:42 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.63, "before": 64.69, "loss": 0.065, "playerId": 2707} |
| R523 | 08:43 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 93000, "edgeProgressPermille": 697, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.6976744186046512, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R523 | 08:43 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.57, "before": 64.63, "loss": 0.065, "playerId": 2707} |
| R524 | 08:44 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 94000, "edgeProgressPermille": 705, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.7051762940735183, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R524 | 08:44 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.51, "before": 64.57, "loss": 0.065, "playerId": 2707} |
| R525 | 08:45 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 95000, "edgeProgressPermille": 712, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.7126781695423856, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R525 | 08:45 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.45, "before": 64.51, "loss": 0.065, "playerId": 2707} |
| R526 | 08:46 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 96000, "edgeProgressPermille": 720, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.7201800450112528, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R526 | 08:46 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.39, "before": 64.45, "loss": 0.065, "playerId": 2707} |
| R527 | 08:47 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 97000, "edgeProgressPermille": 727, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.72768192048012, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R527 | 08:47 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.33, "before": 64.39, "loss": 0.065, "playerId": 2707} |
| R528 | 08:48 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 98000, "edgeProgressPermille": 735, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.7351837959489872, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R528 | 08:48 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.27, "before": 64.33, "loss": 0.065, "playerId": 2707} |
| R529 | 08:49 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 99000, "edgeProgressPermille": 742, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.7426856714178545, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R529 | 08:49 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.21, "before": 64.27, "loss": 0.065, "playerId": 2707} |
| R530 | 08:50 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 100000, "edgeProgressPermille": 750, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.7501875468867217, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R530 | 08:50 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.15, "before": 64.21, "loss": 0.065, "playerId": 2707} |
| R531 | 08:51 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 101000, "edgeProgressPermille": 757, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.7576894223555889, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R531 | 08:51 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.09, "before": 64.15, "loss": 0.065, "playerId": 2707} |
| R532 | 08:52 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 102000, "edgeProgressPermille": 765, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.7651912978244562, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R532 | 08:52 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 64.03, "before": 64.09, "loss": 0.065, "playerId": 2707} |
| R533 | 08:53 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 103000, "edgeProgressPermille": 772, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.7726931732933233, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R533 | 08:53 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.97, "before": 64.03, "loss": 0.065, "playerId": 2707} |
| R534 | 08:54 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 104000, "edgeProgressPermille": 780, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.7801950487621906, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R534 | 08:54 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.91, "before": 63.97, "loss": 0.065, "playerId": 2707} |
| R535 | 08:55 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 105000, "edgeProgressPermille": 787, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.7876969242310577, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R535 | 08:55 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.85, "before": 63.91, "loss": 0.065, "playerId": 2707} |
| R536 | 08:56 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 106000, "edgeProgressPermille": 795, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.795198799699925, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R536 | 08:56 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.79, "before": 63.85, "loss": 0.065, "playerId": 2707} |
| R537 | 08:57 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 107000, "edgeProgressPermille": 802, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.8027006751687922, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R537 | 08:57 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.73, "before": 63.79, "loss": 0.065, "playerId": 2707} |
| R538 | 08:58 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 108000, "edgeProgressPermille": 810, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.8102025506376594, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R538 | 08:58 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.67, "before": 63.73, "loss": 0.065, "playerId": 2707} |
| R539 | 08:59 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 109000, "edgeProgressPermille": 817, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.8177044261065266, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R539 | 08:59 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.61, "before": 63.67, "loss": 0.065, "playerId": 2707} |
| R540 | 09:00 | MED | 任务过期 |  | T_018 在 秦岭栈道(S08) 过期 |
| R540 | 09:00 | MED | 任务过期 |  | T_019 在 洛阳驿(S09) 过期 |
| R540 | 09:00 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 110000, "edgeProgressPermille": 825, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.8252063015753939, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R540 | 09:00 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.55, "before": 63.61, "loss": 0.065, "playerId": 2707} |
| R541 | 09:01 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 111000, "edgeProgressPermille": 832, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.832708177044261, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R541 | 09:01 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.49, "before": 63.55, "loss": 0.065, "playerId": 2707} |
| R542 | 09:02 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 112000, "edgeProgressPermille": 840, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.8402100525131283, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R542 | 09:02 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.43, "before": 63.49, "loss": 0.065, "playerId": 2707} |
| R543 | 09:03 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 113000, "edgeProgressPermille": 847, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.8477119279819955, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R543 | 09:03 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.37, "before": 63.43, "loss": 0.065, "playerId": 2707} |
| R544 | 09:04 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 114000, "edgeProgressPermille": 855, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.8552138034508627, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R544 | 09:04 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.31, "before": 63.37, "loss": 0.065, "playerId": 2707} |
| R545 | 09:05 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 115000, "edgeProgressPermille": 862, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.8627156789197299, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R545 | 09:05 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.25, "before": 63.31, "loss": 0.065, "playerId": 2707} |
| R546 | 09:06 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 116000, "edgeProgressPermille": 870, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.8702175543885972, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R546 | 09:06 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.19, "before": 63.25, "loss": 0.065, "playerId": 2707} |
| R547 | 09:07 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 117000, "edgeProgressPermille": 877, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.8777194298574643, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R547 | 09:07 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.13, "before": 63.19, "loss": 0.065, "playerId": 2707} |
| R548 | 09:08 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 118000, "edgeProgressPermille": 885, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.8852213053263316, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R548 | 09:08 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.07, "before": 63.13, "loss": 0.065, "playerId": 2707} |
| R549 | 09:09 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 119000, "edgeProgressPermille": 892, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.8927231807951987, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R549 | 09:09 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 63.01, "before": 63.07, "loss": 0.065, "playerId": 2707} |
| R550 | 09:10 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 120000, "edgeProgressPermille": 900, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.900225056264066, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R550 | 09:10 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.95, "before": 63.01, "loss": 0.065, "playerId": 2707} |
| R551 | 09:11 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 121000, "edgeProgressPermille": 907, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.9077269317329333, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R551 | 09:11 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.89, "before": 62.95, "loss": 0.065, "playerId": 2707} |
| R552 | 09:12 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 122000, "edgeProgressPermille": 915, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.9152288072018004, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R552 | 09:12 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.83, "before": 62.89, "loss": 0.065, "playerId": 2707} |
| R553 | 09:13 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 123000, "edgeProgressPermille": 922, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.9227306826706677, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R553 | 09:13 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.77, "before": 62.83, "loss": 0.065, "playerId": 2707} |
| R554 | 09:14 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 124000, "edgeProgressPermille": 930, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.9302325581395349, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R554 | 09:14 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.71, "before": 62.77, "loss": 0.065, "playerId": 2707} |
| R555 | 09:15 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 125000, "edgeProgressPermille": 937, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.9377344336084021, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R555 | 09:15 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.65, "before": 62.71, "loss": 0.065, "playerId": 2707} |
| R556 | 09:16 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 126000, "edgeProgressPermille": 945, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.9452363090772693, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R556 | 09:16 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.59, "before": 62.65, "loss": 0.065, "playerId": 2707} |
| R557 | 09:17 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 127000, "edgeProgressPermille": 952, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.9527381845461366, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R557 | 09:17 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.53, "before": 62.59, "loss": 0.065, "playerId": 2707} |
| R558 | 09:18 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 128000, "edgeProgressPermille": 960, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.9602400600150037, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R558 | 09:18 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.47, "before": 62.53, "loss": 0.065, "playerId": 2707} |
| R559 | 09:19 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 129000, "edgeProgressPermille": 967, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.967741935483871, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R559 | 09:19 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.41, "before": 62.47, "loss": 0.065, "playerId": 2707} |
| R560 | 09:20 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 130000, "edgeProgressPermille": 975, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.9752438109527382, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R560 | 09:20 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.35, "before": 62.41, "loss": 0.065, "playerId": 2707} |
| R561 | 09:21 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 131000, "edgeProgressPermille": 982, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.9827456864216054, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R561 | 09:21 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.29, "before": 62.35, "loss": 0.065, "playerId": 2707} |
| R562 | 09:22 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 132000, "edgeProgressPermille": 990, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.9902475618904726, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R562 | 09:22 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.23, "before": 62.29, "loss": 0.065, "playerId": 2707} |
| R563 | 09:23 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 133000, "edgeProgressPermille": 997, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 0.9977494373593399, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R563 | 09:23 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.17, "before": 62.23, "loss": 0.065, "playerId": 2707} |
| R564 | 09:24 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 133300, "edgeProgressPermille": 1000, "edgeTotalMs": 133300, "fromNodeId": "S07", "playerId": 2707, "progress": 1.0, "routeEdgeId": "E13", "toNodeId": "S05"} |
| R564 | 09:24 | HIGH | 进点 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 进入 洞庭水驿(S05) |
| R564 | 09:24 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.11, "before": 62.17, "loss": 0.065, "playerId": 2707} |
| R565 | 09:25 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "WATER_TRANSFER", "remainingRound": 5, "targetNodeId": "S05"} |
| R565 | 09:25 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.06, "before": 62.11, "loss": 0.05, "playerId": 2707} |
| R566 | 09:26 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "WATER_TRANSFER", "remainingRound": 4, "targetNodeId": "S05"} |
| R566 | 09:26 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 62.01, "before": 62.06, "loss": 0.05, "playerId": 2707} |
| R567 | 09:27 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "WATER_TRANSFER", "remainingRound": 3, "targetNodeId": "S05"} |
| R567 | 09:27 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.96, "before": 62.01, "loss": 0.05, "playerId": 2707} |
| R568 | 09:28 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "WATER_TRANSFER", "remainingRound": 2, "targetNodeId": "S05"} |
| R568 | 09:28 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.91, "before": 61.96, "loss": 0.05, "playerId": 2707} |
| R569 | 09:29 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "WATER_TRANSFER", "remainingRound": 1, "targetNodeId": "S05"} |
| R569 | 09:29 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.86, "before": 61.91, "loss": 0.05, "playerId": 2707} |
| R570 | 09:30 | MED | PROCESS_PROGRESS | RED AAAA/v1.0(2707) | {"playerId": 2707, "processType": "WATER_TRANSFER", "remainingRound": 0, "targetNodeId": "S05"} |
| R570 | 09:30 | MED | 处理完成 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 在 洞庭水驿(S05) 完成水路转运 |
| R570 | 09:30 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.81, "before": 61.86, "loss": 0.05, "playerId": 2707} |
| R571 | 09:31 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 88, "edgeTotalMs": 11250, "fromNodeId": "S05", "playerId": 2707, "progress": 0.08888888888888889, "routeEdgeId": "E12", "toNodeId": "S04"} |
| R571 | 09:31 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.77, "before": 61.81, "loss": 0.045, "playerId": 2707} |
| R572 | 09:32 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 177, "edgeTotalMs": 11250, "fromNodeId": "S05", "playerId": 2707, "progress": 0.17777777777777778, "routeEdgeId": "E12", "toNodeId": "S04"} |
| R572 | 09:32 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.73, "before": 61.77, "loss": 0.045, "playerId": 2707} |
| R573 | 09:33 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 266, "edgeTotalMs": 11250, "fromNodeId": "S05", "playerId": 2707, "progress": 0.26666666666666666, "routeEdgeId": "E12", "toNodeId": "S04"} |
| R573 | 09:33 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.68, "before": 61.73, "loss": 0.045, "playerId": 2707} |
| R574 | 09:34 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 355, "edgeTotalMs": 11250, "fromNodeId": "S05", "playerId": 2707, "progress": 0.35555555555555557, "routeEdgeId": "E12", "toNodeId": "S04"} |
| R574 | 09:34 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.64, "before": 61.68, "loss": 0.045, "playerId": 2707} |
| R575 | 09:35 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 444, "edgeTotalMs": 11250, "fromNodeId": "S05", "playerId": 2707, "progress": 0.4444444444444444, "routeEdgeId": "E12", "toNodeId": "S04"} |
| R575 | 09:35 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.6, "before": 61.64, "loss": 0.045, "playerId": 2707} |
| R576 | 09:36 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 533, "edgeTotalMs": 11250, "fromNodeId": "S05", "playerId": 2707, "progress": 0.5333333333333333, "routeEdgeId": "E12", "toNodeId": "S04"} |
| R576 | 09:36 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.56, "before": 61.6, "loss": 0.045, "playerId": 2707} |
| R577 | 09:37 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 622, "edgeTotalMs": 11250, "fromNodeId": "S05", "playerId": 2707, "progress": 0.6222222222222222, "routeEdgeId": "E12", "toNodeId": "S04"} |
| R577 | 09:37 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.52, "before": 61.56, "loss": 0.045, "playerId": 2707} |
| R578 | 09:38 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 711, "edgeTotalMs": 11250, "fromNodeId": "S05", "playerId": 2707, "progress": 0.7111111111111111, "routeEdgeId": "E12", "toNodeId": "S04"} |
| R578 | 09:38 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.48, "before": 61.52, "loss": 0.045, "playerId": 2707} |
| R579 | 09:39 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 800, "edgeTotalMs": 11250, "fromNodeId": "S05", "playerId": 2707, "progress": 0.8, "routeEdgeId": "E12", "toNodeId": "S04"} |
| R579 | 09:39 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.43, "before": 61.48, "loss": 0.045, "playerId": 2707} |
| R580 | 09:40 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 888, "edgeTotalMs": 11250, "fromNodeId": "S05", "playerId": 2707, "progress": 0.8888888888888888, "routeEdgeId": "E12", "toNodeId": "S04"} |
| R580 | 09:40 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.39, "before": 61.43, "loss": 0.045, "playerId": 2707} |
| R581 | 09:41 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 977, "edgeTotalMs": 11250, "fromNodeId": "S05", "playerId": 2707, "progress": 0.9777777777777777, "routeEdgeId": "E12", "toNodeId": "S04"} |
| R581 | 09:41 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.35, "before": 61.39, "loss": 0.045, "playerId": 2707} |
| R582 | 09:42 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 11250, "edgeProgressPermille": 1000, "edgeTotalMs": 11250, "fromNodeId": "S05", "playerId": 2707, "progress": 1.0, "routeEdgeId": "E12", "toNodeId": "S04"} |
| R582 | 09:42 | HIGH | 进点 | RED AAAA/v1.0(2707) | RED AAAA/v1.0(2707) 进入 江南码头(S04) |
| R582 | 09:42 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.31, "before": 61.35, "loss": 0.045, "playerId": 2707} |
| R583 | 09:43 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 1000, "edgeProgressPermille": 8, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.008960493185544932, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R583 | 09:43 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.25, "before": 61.31, "loss": 0.065, "playerId": 2707} |
| R584 | 09:44 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 2000, "edgeProgressPermille": 17, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.017920986371089864, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R584 | 09:44 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.19, "before": 61.25, "loss": 0.065, "playerId": 2707} |
| R585 | 09:45 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 3000, "edgeProgressPermille": 26, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.026881479556634797, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R585 | 09:45 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.13, "before": 61.19, "loss": 0.065, "playerId": 2707} |
| R586 | 09:46 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 4000, "edgeProgressPermille": 35, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.03584197274217973, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R586 | 09:46 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.07, "before": 61.13, "loss": 0.065, "playerId": 2707} |
| R587 | 09:47 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 5000, "edgeProgressPermille": 44, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.04480246592772466, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R587 | 09:47 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 61.01, "before": 61.07, "loss": 0.065, "playerId": 2707} |
| R588 | 09:48 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 6000, "edgeProgressPermille": 53, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.053762959113269594, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R588 | 09:48 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 60.95, "before": 61.01, "loss": 0.065, "playerId": 2707} |
| R589 | 09:49 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 7000, "edgeProgressPermille": 62, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.06272345229881453, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R589 | 09:49 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 60.89, "before": 60.95, "loss": 0.065, "playerId": 2707} |
| R590 | 09:50 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 8000, "edgeProgressPermille": 71, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.07168394548435945, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R590 | 09:50 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 60.83, "before": 60.89, "loss": 0.065, "playerId": 2707} |
| R591 | 09:51 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 9000, "edgeProgressPermille": 80, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.0806444386699044, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R591 | 09:51 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 60.77, "before": 60.83, "loss": 0.065, "playerId": 2707} |
| R592 | 09:52 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 10000, "edgeProgressPermille": 89, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.08960493185544932, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R592 | 09:52 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 60.71, "before": 60.77, "loss": 0.065, "playerId": 2707} |
| R593 | 09:53 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 11000, "edgeProgressPermille": 98, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.09856542504099426, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R593 | 09:53 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 60.65, "before": 60.71, "loss": 0.065, "playerId": 2707} |
| R594 | 09:54 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 12000, "edgeProgressPermille": 107, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.10752591822653919, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R594 | 09:54 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 60.59, "before": 60.65, "loss": 0.065, "playerId": 2707} |
| R595 | 09:55 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 13000, "edgeProgressPermille": 116, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.11648641141208411, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R595 | 09:55 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 60.53, "before": 60.59, "loss": 0.065, "playerId": 2707} |
| R596 | 09:56 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 14000, "edgeProgressPermille": 125, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.12544690459762906, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R596 | 09:56 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 60.47, "before": 60.53, "loss": 0.065, "playerId": 2707} |
| R597 | 09:57 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 15000, "edgeProgressPermille": 134, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.13440739778317398, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R597 | 09:57 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 60.41, "before": 60.47, "loss": 0.065, "playerId": 2707} |
| R598 | 09:58 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 16000, "edgeProgressPermille": 143, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.1433678909687189, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R598 | 09:58 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 60.35, "before": 60.41, "loss": 0.065, "playerId": 2707} |
| R599 | 09:59 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 17000, "edgeProgressPermille": 152, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.15232838415426386, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R599 | 09:59 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 60.29, "before": 60.35, "loss": 0.065, "playerId": 2707} |
| R600 | 10:00 | MED | MOVE_PROGRESS | RED AAAA/v1.0(2707) | {"edgeProgressMs": 18000, "edgeProgressPermille": 161, "edgeTotalMs": 111601, "fromNodeId": "S04", "playerId": 2707, "progress": 0.1612888773398088, "routeEdgeId": "E21", "toNodeId": "S07"} |
| R600 | 10:00 | MED | FRESHNESS_DROP | RED AAAA/v1.0(2707) | {"after": 60.23, "before": 60.29, "loss": 0.065, "playerId": 2707} |
