# Session close (#1875, rebuilt #2173)

> Generated 2026-11-06T17:37:37Z by `session.close` (#1875, rebuilt #2173). Detection only; remediation is Claude's (`.claude/commands/session-close.md`). A finding is cleared by fixing it, or by a disposition in the compliance file's `## Close dispositions` that the check accepts. **The commit is blocked while any finding is open.**

- session: `325129d4-3704-424e-9f5b-0f131a1db2ab` (CLAUDE_CODE_SESSION_ID); started 2026-11-04T18:06:55Z; window base commit `6362537fd32195cf71d8c17189ea3f6514179336`
- compliance file: `Logs/compliance/COMPLIANCE-20261104-325129d4.md`; session log: `--`
- **open findings: 154**; cleared by disposition: 0


## Contents

- [Summary](#summary)
- [SC1](#sc1-session-and-window)
- [SC2](#sc2-spine-fatal)
- [SC3](#sc3-researchers-words-recorded)
- [SC4](#sc4-open-items-in-the-register)
- [SC5](#sc5-analysis-integrity)
- [SC6](#sc6-rule-compliance)
- [SC8](#sc8-session-log)
- [SC9](#sc9-decisions-reached-their-targets)
- [SC10](#sc10-buildmd-coverage)
- [SC12](#sc12-publish)
- sc15
- sc16

<a id="summary"></a>
## Summary

154 open finding(s); SC2 6, SC3 80, SC4 4, SC6 38, SC8 1, SC10 16, SC15 7, SC16 2

<a id="sc1-session-and-window"></a>
## SC1 Session and window

_no finding_

<a id="sc2-spine-fatal"></a>
## SC2 Spine (FATAL)

- **OPEN** `SC2:unverified:G0001G`: G0001G: local gap in strong_lexicon.mounce not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))
- **OPEN** `SC2:unverified:G4528H`: G4528H: local gap in strong_lexicon.mounce not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))
- **OPEN** `SC2:unverified:G6094`: G6094: local gap in strong_lexicon.mounce not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))
- **OPEN** `SC2:unverified:H0430H`: H0430H: local gap in strong_meaning_tree not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))
- **OPEN** `SC2:unverified:H1121A`: H1121A: local gap in strong_meaning_tree not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))
- **OPEN** `SC2:unverified:H5945H`: H5945H: local gap in strong_meaning_tree not verified against STEP (ConnectionError: HTTPConnectionPool(host='localhost', port=8989): Max retries exceeded with url: /rest/module/getInfo/ESV_th//H5945H// (Caused by NewConnectionError("HTTPConnection(host='localhost', port=8989): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it")))

<a id="sc3-researchers-words-recorded"></a>
## SC3 Researcher's words recorded

- **OPEN** `SC3:12999f62`: researcher message 2026-11-04T18:51 is in no escalation comment written this session: "<task-notification>
<task-id>bq7hb4do0</task-id>
<summary>Monitor event: "embedding job finish or error"</summary>
<event>[Monitor expired after 15m with no eve"
- **OPEN** `SC3:02bc427c`: researcher message 2026-11-04T19:06 is in no escalation comment written this session: "<task-notification>
<task-id>b2skpx36a</task-id>
<summary>Monitor event: "last embedding config finishes or errors"</summary>
<event>[Monitor expired after 15m "
- **OPEN** `SC3:735f27fd`: researcher message 2026-11-04T19:08 is in no escalation comment written this session: "<task-notification>
<task-id>bk85ga4hq</task-id>
<tool-use-id>toolu_01T6tSymgbXASrKkRgFK5WzC</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:2919030b`: researcher message 2026-11-04T19:11 is in no escalation comment written this session: "<task-notification>
<task-id>b6se43jcv</task-id>
<tool-use-id>toolu_01Vy5ithhRcVssJE3zVUghuf</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:7eb7313f`: researcher message 2026-11-04T19:41 is in no escalation comment written this session: "<task-notification>
<task-id>brx8485nq</task-id>
<summary>Monitor event: "pair judge done, halted or crashed"</summary>
<event>[Monitor expired after 30m with n"
- **OPEN** `SC3:70f9052a`: researcher message 2026-11-04T20:12 is in no escalation comment written this session: "<task-notification>
<task-id>bcjcf7211</task-id>
<summary>Monitor event: "pair judge done, halted or crashed"</summary>
<event>[Monitor expired after 30m with n"
- **OPEN** `SC3:8dfa1c93`: researcher message 2026-11-04T20:18 is in no escalation comment written this session: "how is it going, is it done"
- **OPEN** `SC3:822ba66d`: researcher message 2026-11-04T20:19 is in no escalation comment written this session: "thanks, will look at it in the morning"
- **OPEN** `SC3:9b5325d8`: researcher message 2026-11-04T20:42 is in no escalation comment written this session: "<task-notification>
<task-id>brryfgl6f</task-id>
<summary>Monitor event: "pair judge done, halted or crashed"</summary>
<event>[Monitor expired after 30m with n"
- **OPEN** `SC3:02fa45ef`: researcher message 2026-11-05T03:51 is in no escalation comment written this session: "<task-notification>
<task-id>bq7hb4do0</task-id>
<task-id>b2skpx36a</task-id>
<task-id>brx8485nq</task-id>
<task-id>bcjcf7211</task-id>
<task-id>brryfgl6f</task"
- **OPEN** `SC3:55c42cc0`: researcher message 2026-11-05T03:51 is too short to be matched; name where it is recorded: "check for completion"
- **OPEN** `SC3:d6457aa4`: researcher message 2026-11-05T03:54 is in no escalation comment written this session: "I will go along with your judgement to move towards the outcome. continue"
- **OPEN** `SC3:b653a39b`: researcher message 2026-11-05T04:19 is in no escalation comment written this session: "<task-notification>
<task-id>benfvvvmz</task-id>
<tool-use-id>toolu_01FGyfZmSQLWTJByfZMYxU9K</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:0dd16394`: researcher message 2026-11-05T04:48 is in no escalation comment written this session: "<task-notification>
<task-id>b5og1le1o</task-id>
<tool-use-id>toolu_01CX6LSqJeQzgT87pCo1g1Cr</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:91e9d425`: researcher message 2026-11-05T05:22 is in no escalation comment written this session: "<task-notification>
<task-id>bifx5z9gy</task-id>
<summary>Monitor event: "batch done, halted or crashed"</summary>
<event>[Monitor expired after 30m with no eve"
- **OPEN** `SC3:2a37fd78`: researcher message 2026-11-05T05:43 is in no escalation comment written this session: "<task-notification>
<task-id>b5tq2okd1</task-id>
<tool-use-id>toolu_01AXb1RMNidQnkG37kPFHSof</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:8c8b6613`: researcher message 2026-11-05T05:48 is in no escalation comment written this session: "<task-notification>
<task-id>bjv2f1hs5</task-id>
<tool-use-id>toolu_01W9nPFMR9muZXedLV6YdPAh</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:21e209f7`: researcher message 2026-11-05T05:51 is in no escalation comment written this session: "<task-notification>
<task-id>b02k0dn0z</task-id>
<tool-use-id>toolu_01DUtLBQHgH2Ev2cFJxtMXmj</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:745cd427`: researcher message 2026-11-05T06:22 is in no escalation comment written this session: "<task-notification>
<task-id>bw7bw4sld</task-id>
<summary>Monitor event: "batch 2 done or crashed"</summary>
<event>[Monitor expired after 30m with no events de"
- **OPEN** `SC3:c5fdc114`: researcher message 2026-11-05T06:52 is in no escalation comment written this session: "<task-notification>
<task-id>b18f416gl</task-id>
<summary>Monitor event: "batch 2 done or crashed"</summary>
<event>[Monitor expired after 30m with no events de"
- **OPEN** `SC3:a5b37754`: researcher message 2026-11-05T07:23 is in no escalation comment written this session: "<task-notification>
<task-id>b0gic6xgb</task-id>
<summary>Monitor event: "fixed batch done or crashed"</summary>
<event>[Monitor expired after 30m with no event"
- **OPEN** `SC3:69f4cc2a`: researcher message 2026-11-05T07:53 is in no escalation comment written this session: "<task-notification>
<task-id>b4yu7c0f3</task-id>
<summary>Monitor event: "fixed batch done or crashed"</summary>
<event>[Monitor expired after 30m with no event"
- **OPEN** `SC3:9aae28c3`: researcher message 2026-11-05T08:14 is in no escalation comment written this session: "<task-notification>
<task-id>b15igagpu</task-id>
<tool-use-id>toolu_011VQeAB82PwcxvLFPDEZ41P</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:63ec1892`: researcher message 2026-11-05T08:25 is in no escalation comment written this session: "<task-notification>
<task-id>btf6z0eo1</task-id>
<tool-use-id>toolu_01XcqY1HQg52GTAJqcj2J6o1</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:e2c246c4`: researcher message 2026-11-05T08:35 is in no escalation comment written this session: "<task-notification>
<task-id>b4lt7majg</task-id>
<tool-use-id>toolu_01FE9oaqPNC25Pyh5QGGreLC</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:04150b6b`: researcher message 2026-11-05T09:06 is in no escalation comment written this session: "<task-notification>
<task-id>bwx2nny9e</task-id>
<summary>Monitor event: "batch 4 done or crashed"</summary>
<event>[Monitor expired after 30m with no events de"
- **OPEN** `SC3:c31185d7`: researcher message 2026-11-05T09:36 is in no escalation comment written this session: "<task-notification>
<task-id>b5dre9aw8</task-id>
<summary>Monitor event: "batch 4 done or crashed"</summary>
<event>[Monitor expired after 30m with no events de"
- **OPEN** `SC3:867ec6d3`: researcher message 2026-11-05T09:44 is in no escalation comment written this session: "how are we doing"
- **OPEN** `SC3:c675143c`: researcher message 2026-11-05T10:06 is in no escalation comment written this session: "<task-notification>
<task-id>bwwikourq</task-id>
<summary>Monitor event: "batch 4 done or crashed"</summary>
<event>[Monitor expired after 30m with no events de"
- **OPEN** `SC3:d610448a`: researcher message 2026-11-05T10:19 is in no escalation comment written this session: "<task-notification>
<task-id>bocri535d</task-id>
<tool-use-id>toolu_01R1UCa2E7mF4TFo7GBrvV6u</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:7698a899`: researcher message 2026-11-05T10:51 is in no escalation comment written this session: "<task-notification>
<task-id>bmc8fimxc</task-id>
<summary>Monitor event: "batch 5 done or crashed"</summary>
<event>[Monitor expired after 30m with no events de"
- **OPEN** `SC3:a9212a95`: researcher message 2026-11-05T11:16 is too short to be matched; name where it is recorded: "great work"
- **OPEN** `SC3:f14af3a1`: researcher message 2026-11-05T11:21 is in no escalation comment written this session: "<task-notification>
<task-id>bftofz6rc</task-id>
<summary>Monitor event: "batch 5 done or crashed"</summary>
<event>[Monitor expired after 30m with no events de"
- **OPEN** `SC3:9ba0615d`: researcher message 2026-11-05T11:51 is in no escalation comment written this session: "<task-notification>
<task-id>bjlheccx1</task-id>
<summary>Monitor event: "batch 5 done or crashed"</summary>
<event>[Monitor expired after 30m with no events de"
- **OPEN** `SC3:ac4471ed`: researcher message 2026-11-05T12:03 is in no escalation comment written this session: "<task-notification>
<task-id>b8l7xrllt</task-id>
<tool-use-id>toolu_01PXaxB4kJDBYGPSoxxaj1US</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:d043ae73`: researcher message 2026-11-05T12:28 is in no escalation comment written this session: "<task-notification>
<task-id>br6x2c1r6</task-id>
<summary>Monitor event: "fix tests finish or crash"</summary>
<event>[Monitor expired after 15m with no events "
- **OPEN** `SC3:a340cc12`: researcher message 2026-11-05T12:34 is in no escalation comment written this session: "<task-notification>
<task-id>boafqpajm</task-id>
<summary>Monitor event: "batch 3 done or crashed"</summary>
<event>[Monitor expired after 30m with no events de"
- **OPEN** `SC3:45df7bdf`: researcher message 2026-11-05T12:43 is in no escalation comment written this session: "<task-notification>
<task-id>bc2bp8qj0</task-id>
<tool-use-id>toolu_01QiGFuMkifGTHBvZ7hxupU6</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:c06bb104`: researcher message 2026-11-05T13:13 is in no escalation comment written this session: "<task-notification>
<task-id>bt11pmmv3</task-id>
<summary>Monitor event: "reasoning test finishes or crashes"</summary>
<event>[Monitor expired after 30m with n"
- **OPEN** `SC3:56930e9c`: researcher message 2026-11-05T13:45 is in no escalation comment written this session: "<task-notification>
<task-id>b6uy3uu11</task-id>
<summary>Monitor event: "re-run batch done or crashed"</summary>
<event>[Monitor expired after 30m with no even"
- **OPEN** `SC3:0d33c7fd`: researcher message 2026-11-05T14:08 is in no escalation comment written this session: "<task-notification>
<task-id>bkka4w2x4</task-id>
<summary>Monitor event: "both running jobs finish or one crashes"</summary>
<event>[Monitor expired after 30m w"
- **OPEN** `SC3:b285ad42`: researcher message 2026-11-05T14:15 is in no escalation comment written this session: "<task-notification>
<task-id>bztugcuin</task-id>
<summary>Monitor event: "both running jobs finish or one crashes"</summary>
<event>[Monitor expired after 30m w"
- **OPEN** `SC3:3eb42064`: researcher message 2026-11-05T14:38 is in no escalation comment written this session: "<task-notification>
<task-id>bctesg9yj</task-id>
<summary>Monitor event: "both running jobs finish or one crashes"</summary>
<event>[Monitor expired after 30m w"
- **OPEN** `SC3:49ec3c4b`: researcher message 2026-11-05T14:45 is in no escalation comment written this session: "<task-notification>
<task-id>bmld3x5sy</task-id>
<summary>Monitor event: "both running jobs finish or one crashes"</summary>
<event>[Monitor expired after 30m w"
- **OPEN** `SC3:a302b3d8`: researcher message 2026-11-05T15:09 is in no escalation comment written this session: "<task-notification>
<task-id>b3ex27t5o</task-id>
<summary>Monitor event: "both running jobs finish or one crashes"</summary>
<event>[Monitor expired after 30m w"
- **OPEN** `SC3:0152f827`: researcher message 2026-11-05T15:16 is in no escalation comment written this session: "<task-notification>
<task-id>bngf3ptxv</task-id>
<summary>Monitor event: "both running jobs finish or one crashes"</summary>
<event>[Monitor expired after 30m w"
- **OPEN** `SC3:b390bda9`: researcher message 2026-11-05T15:39 is in no escalation comment written this session: "<task-notification>
<task-id>boicqclag</task-id>
<summary>Monitor event: "both running jobs finish or one crashes"</summary>
<event>[Monitor expired after 30m w"
- **OPEN** `SC3:c1692316`: researcher message 2026-11-05T15:46 is in no escalation comment written this session: "<task-notification>
<task-id>b8yosytur</task-id>
<summary>Monitor event: "both running jobs finish or one crashes"</summary>
<event>[Monitor expired after 30m w"
- **OPEN** `SC3:a9e97a94`: researcher message 2026-11-05T15:46 is in no escalation comment written this session: "<task-notification>
<task-id>bpzqnvar2</task-id>
<tool-use-id>toolu_01Psz62LFQtr2ZkajJUm2qfN</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:d42a36d0`: researcher message 2026-11-05T15:51 is in no escalation comment written this session: "I will wait for these runs to complete and then assess the status"
- **OPEN** `SC3:71b01e12`: researcher message 2026-11-05T16:09 is in no escalation comment written this session: "<task-notification>
<task-id>bvh312iys</task-id>
<summary>Monitor event: "both running jobs finish or one crashes"</summary>
<event>[Monitor expired after 30m w"
- **OPEN** `SC3:053514b7`: researcher message 2026-11-05T16:17 is in no escalation comment written this session: "<task-notification>
<task-id>b8r86xfcm</task-id>
<summary>Monitor event: "re-run 1 and batch 4 finish or one crashes"</summary>
<event>[Monitor expired after 30"
- **OPEN** `SC3:93851241`: researcher message 2026-11-05T16:39 is in no escalation comment written this session: "<task-notification>
<task-id>b25gwrips</task-id>
<summary>Monitor event: "re-run 1 and batch 4 finish or one crashes"</summary>
<event>[Monitor expired after 30"
- **OPEN** `SC3:dba5c54a`: researcher message 2026-11-05T16:47 is in no escalation comment written this session: "<task-notification>
<task-id>bpnu8zo31</task-id>
<summary>Monitor event: "re-run 1 and batch 4 finish or one crashes"</summary>
<event>[Monitor expired after 30"
- **OPEN** `SC3:9cc9d948`: researcher message 2026-11-05T17:10 is in no escalation comment written this session: "<task-notification>
<task-id>b7ue5ckf8</task-id>
<summary>Monitor event: "re-run 1 and batch 4 finish or one crashes"</summary>
<event>[Monitor expired after 30"
- **OPEN** `SC3:8208c65b`: researcher message 2026-11-05T17:17 is in no escalation comment written this session: "<task-notification>
<task-id>b9fkfd928</task-id>
<summary>Monitor event: "re-run 1 and batch 4 finish or one crashes"</summary>
<event>[Monitor expired after 30"
- **OPEN** `SC3:96fdf2e8`: researcher message 2026-11-05T17:40 is in no escalation comment written this session: "<task-notification>
<task-id>bv9p6iwxi</task-id>
<summary>Monitor event: "re-run 1 and batch 4 finish or one crashes"</summary>
<event>[Monitor expired after 30"
- **OPEN** `SC3:4336312e`: researcher message 2026-11-05T17:47 is in no escalation comment written this session: "<task-notification>
<task-id>br0wgb7l5</task-id>
<summary>Monitor event: "re-run 1 and batch 4 finish or one crashes"</summary>
<event>[Monitor expired after 30"
- **OPEN** `SC3:bacf5ad2`: researcher message 2026-11-05T18:10 is in no escalation comment written this session: "<task-notification>
<task-id>bjw58l3am</task-id>
<summary>Monitor event: "re-run 1 and batch 4 finish or one crashes"</summary>
<event>[Monitor expired after 30"
- **OPEN** `SC3:5151bed8`: researcher message 2026-11-05T18:18 is in no escalation comment written this session: "<task-notification>
<task-id>b5feytywp</task-id>
<summary>Monitor event: "re-run 1 and batch 4 finish or one crashes"</summary>
<event>[Monitor expired after 30"
- **OPEN** `SC3:8c05761f`: researcher message 2026-11-05T18:40 is in no escalation comment written this session: "<task-notification>
<task-id>bp3vyqn1m</task-id>
<summary>Monitor event: "re-run 1 and batch 4 finish or one crashes"</summary>
<event>[Monitor expired after 30"
- **OPEN** `SC3:6819b7a2`: researcher message 2026-11-05T18:48 is in no escalation comment written this session: "<task-notification>
<task-id>bhr3q9z34</task-id>
<summary>Monitor event: "re-run 1 and batch 4 finish or one crashes"</summary>
<event>[Monitor expired after 30"
- **OPEN** `SC3:5f8e2c4d`: researcher message 2026-11-05T19:11 is in no escalation comment written this session: "<task-notification>
<task-id>bthkzbbv2</task-id>
<summary>Monitor event: "batch 4 finishes or crashes"</summary>
<event>[Monitor expired after 30m with no event"
- **OPEN** `SC3:04181528`: researcher message 2026-11-05T19:18 is in no escalation comment written this session: "<task-notification>
<task-id>b3vwg3ani</task-id>
<summary>Monitor event: "batch 4 finishes or crashes"</summary>
<event>[Monitor expired after 30m with no event"
- **OPEN** `SC3:932f425f`: researcher message 2026-11-05T19:41 is in no escalation comment written this session: "<task-notification>
<task-id>bq356408d</task-id>
<summary>Monitor event: "batch 4 finishes or crashes"</summary>
<event>[Monitor expired after 30m with no event"
- **OPEN** `SC3:74bf87ed`: researcher message 2026-11-05T19:48 is in no escalation comment written this session: "<task-notification>
<task-id>bm09s99yv</task-id>
<tool-use-id>toolu_01CwXzrVaJTTqTGQ6NG4rA6c</tool-use-id>
<output-file>C:\Users\lerouxc\AppData\Local\Temp\clau"
- **OPEN** `SC3:8eafbf75`: researcher message 2026-11-06T04:30 is in no escalation comment written this session: "<task-notification>
<task-id>bifx5z9gy</task-id>
<task-id>bw7bw4sld</task-id>
<task-id>b18f416gl</task-id>
<task-id>b0gic6xgb</task-id>
<task-id>b4yu7c0f3</task"
- **OPEN** `SC3:9d10447b`: researcher message 2026-11-06T06:07 is too short to be matched; name where it is recorded: "A: leave them"
- **OPEN** `SC3:e217c0d0`: researcher message 2026-11-06T06:20 is too short to be matched; name where it is recorded: "proceed"
- **OPEN** `SC3:8c844523`: researcher message 2026-11-06T09:58 is too short to be matched; name where it is recorded: "proceed with 1c"
- **OPEN** `SC3:60a9c1ae`: researcher message 2026-11-06T13:54 is too short to be matched; name where it is recorded: "proceed with 1c"
- **OPEN** `SC3:7b2b3c11`: researcher message 2026-11-06T14:28 is in no escalation comment written this session: "it sounds like you are still in mid stream on building all the stages"
- **OPEN** `SC3:3eeeb43a`: researcher message 2026-11-06T14:30 is too short to be matched; name where it is recorded: "continue"
- **OPEN** `SC3:f1554ed5`: researcher message 2026-11-06T14:51 is in no escalation comment written this session: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"
- **OPEN** `SC3:7a53bb88`: researcher message 2026-11-06T16:32 is too short to be matched; name where it is recorded: "Yes, continue"
- **OPEN** `SC3:23308121`: researcher message 2026-11-06T16:47 is too short to be matched; name where it is recorded: "Yes, continue"
- **OPEN** `SC3:3aa35ae4`: researcher message 2026-11-06T16:59 is too short to be matched; name where it is recorded: "Yes, continue"
- **OPEN** `SC3:0abc637c`: researcher message 2026-11-06T17:10 is too short to be matched; name where it is recorded: "Yes, build it"
- **OPEN** `SC3:e5a9ca22`: researcher message 2026-11-06T17:25 is too short to be matched; name where it is recorded: "Yes, stage 6"
- **OPEN** `SC3:c051eeda`: researcher message 2026-11-06T17:36 is too short to be matched; name where it is recorded: "Close session"

<a id="sc4-open-items-in-the-register"></a>
## SC4 Open items in the register

- **OPEN** `SC4b:3c29898c`: researcher message 2026-11-04T18:32 holds, defers or asks to check something; name its register item: "D1 - bases with similar meaning (synonyms) should be group together in the same collections. items with the same base will all go to the same collection.  D2 - "
- **OPEN** `SC4b:55c42cc0`: researcher message 2026-11-05T03:51 holds, defers or asks to check something; name its register item: "check for completion"
- **OPEN** `SC4b:81cbff84`: researcher message 2026-11-06T04:44 holds, defers or asks to check something; name its register item: "good work.  what you now need to do is to a) capture the collection process into the the framework of the study (configs, governance, documentation) b) flush th"
- **OPEN** `SC4b:f1554ed5`: researcher message 2026-11-06T14:51 holds, defers or asks to check something; name its register item: "This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.


Summar"

<a id="sc5-analysis-integrity"></a>
## SC5 Analysis integrity

Chapters changed: none; quote parts checked: 0; register check findings now: 42.

_no finding_

<a id="sc6-rule-compliance"></a>
## SC6 Rule compliance

- **OPEN** `SC6:G:governance.escalation.scope`: engaged, with no evidence
- **OPEN** `SC6:G:governance.past_precedent_investigation_signals_missing_config`: engaged, with no evidence
- **OPEN** `SC6:G:governance.primary_responsibility`: engaged, with no evidence
- **OPEN** `SC6:G:governance.project_change_rule`: engaged, with no evidence
- **OPEN** `SC6:G:governance.rules_must_be_config_driven`: engaged, with no evidence
- **OPEN** `SC6:B:1`: engaged, with no evidence
- **OPEN** `SC6:B:2`: engaged, with no evidence
- **OPEN** `SC6:B:4`: engaged, with no evidence
- **OPEN** `SC6:B:10`: engaged, with no evidence
- **OPEN** `SC6:B:16`: engaged, with no evidence
- **OPEN** `SC6:B:17`: engaged, with no evidence
- **OPEN** `SC6:B:18`: engaged, with no evidence
- **OPEN** `SC6:B:19`: engaged, with no evidence
- **OPEN** `SC6:B:20`: engaged, with no evidence
- **OPEN** `SC6:B:21`: engaged, with no evidence
- **OPEN** `SC6:B:22`: engaged, with no evidence
- **OPEN** `SC6:B:23`: engaged, with no evidence
- **OPEN** `SC6:B:24`: engaged, with no evidence
- **OPEN** `SC6:B:25`: engaged, with no evidence
- **OPEN** `SC6:B:27`: engaged, with no evidence
- **OPEN** `SC6:B:28`: engaged, with no evidence
- **OPEN** `SC6:B:31`: engaged, with no evidence
- **OPEN** `SC6:B:34`: engaged, with no evidence
- **OPEN** `SC6:B:36`: engaged, with no evidence
- **OPEN** `SC6:B:40`: engaged, with no evidence
- **OPEN** `SC6:B:44`: engaged, with no evidence
- **OPEN** `SC6:B:83`: engaged, with no evidence
- **OPEN** `SC6:B:97`: engaged, with no evidence
- **OPEN** `SC6:B:98`: engaged, with no evidence
- **OPEN** `SC6:B:99`: engaged, with no evidence
- **OPEN** `SC6:B:100`: engaged, with no evidence
- **OPEN** `SC6:B:101`: engaged, with no evidence
- **OPEN** `SC6:B:102`: engaged, with no evidence
- **OPEN** `SC6:B:105`: engaged, with no evidence
- **OPEN** `SC6:B:123`: engaged, with no evidence
- **OPEN** `SC6:B:125`: engaged, with no evidence
- **OPEN** `SC6:E:4`: engaged, with no evidence
- **OPEN** `SC6:E:5`: engaged, with no evidence

<a id="sc8-session-log"></a>
## SC8 Session log

- **OPEN** `SC8:log`: no session log in Logs/ names this session (325129d4-3704-424e-9f5b-0f131a1db2ab); write it (governance.session_log_required_content)

<a id="sc9-decisions-reached-their-targets"></a>
## SC9 Decisions reached their targets

_no finding_

<a id="sc10-buildmd-coverage"></a>
## SC10 BUILD.md coverage

- **OPEN** `SC10:iba/app/handlers/configmaint.py`: `iba/app/handlers/configmaint.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/lib/cfgreport.py`: `iba/app/lib/cfgreport.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/ai_client_2361_v1_20261106.py`: `iba/app/migration/archive/ai_client_2361_v1_20261106.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/surface_collection_2361_v1_20261106.py`: `iba/app/migration/archive/surface_collection_2361_v1_20261106.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/surface_collection_ask_2361_v1_20261106.py`: `iba/app/migration/archive/surface_collection_ask_2361_v1_20261106.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/surface_collection_fix_2361_v1_20261106.py`: `iba/app/migration/archive/surface_collection_fix_2361_v1_20261106.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/surface_cycle_ambiguous_2361_v1_20261106.py`: `iba/app/migration/archive/surface_cycle_ambiguous_2361_v1_20261106.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/surface_exempt_2361_v1_20261106.py`: `iba/app/migration/archive/surface_exempt_2361_v1_20261106.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/surface_group_2361_v1_20261106.py`: `iba/app/migration/archive/surface_group_2361_v1_20261106.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/surface_hygiene_2361_v1_20261106.py`: `iba/app/migration/archive/surface_hygiene_2361_v1_20261106.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/surface_maps_2361_v1_20261106.py`: `iba/app/migration/archive/surface_maps_2361_v1_20261106.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/surface_maps_fix_2361_v1_20261106.py`: `iba/app/migration/archive/surface_maps_fix_2361_v1_20261106.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/surface_resolve_2361_v1_20261106.py`: `iba/app/migration/archive/surface_resolve_2361_v1_20261106.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/migration/archive/surface_structure_2361_v1_20261106.py`: `iba/app/migration/archive/surface_structure_2361_v1_20261106.py` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/ps/Surface-Base.ps1`: `iba/app/ps/Surface-Base.ps1` changed this session and is not named in what BUILD.md gained this session
- **OPEN** `SC10:iba/app/tools/archive/temp_2359_surface_base_test_run.py`: `iba/app/tools/archive/temp_2359_surface_base_test_run.py` changed this session and is not named in what BUILD.md gained this session

<a id="sc12-publish"></a>
## SC12 Publish

- narrative copy: not needed (no chapter changed)
- threads register export: not needed (no thread row changed)

- **OPEN** `SC15:iba/app/USER-GUIDE.md:1050:Surface-Group.ps1`: `iba/app/USER-GUIDE.md` line 1050 names `Surface-Group.ps1`, which does not resolve
- **OPEN** `SC15:iba/app/USER-GUIDE.md:1051:Surface-Structure.ps1`: `iba/app/USER-GUIDE.md` line 1051 names `Surface-Structure.ps1`, which does not resolve
- **OPEN** `SC15:iba/app/USER-GUIDE.md:1053:Surface-Resolve.ps1`: `iba/app/USER-GUIDE.md` line 1053 names `Surface-Resolve.ps1`, which does not resolve
- **OPEN** `SC15:iba/app/USER-GUIDE.md:1054:Collection-Build.ps1`: `iba/app/USER-GUIDE.md` line 1054 names `Collection-Build.ps1`, which does not resolve
- **OPEN** `SC15:iba/app/USER-GUIDE.md:1055:Ai-Control.ps1`: `iba/app/USER-GUIDE.md` line 1055 names `Ai-Control.ps1`, which does not resolve
- **OPEN** `SC15:iba/app/USER-GUIDE.md:1080:Surface-Structure.ps1`: `iba/app/USER-GUIDE.md` line 1080 names `Surface-Structure.ps1`, which does not resolve
- **OPEN** `SC15:iba/app/USER-GUIDE.md:1082:Surface-Resolve.ps1`: `iba/app/USER-GUIDE.md` line 1082 names `Surface-Resolve.ps1`, which does not resolve

- **OPEN** `SC16:Escalation.ps1_-Action_Update`: Escalation.ps1 -Action Update failed 4 times this session: [31;1mInvoke-Expression: [31;1mUnexpected token 's' in expression or statement.[0m; Update needs -AnsweredBy Claude|Researcher -- no default (escalation rebuild 2026-08-20: a silent 'Researcher' default p; error: decision_required items may only move to approved from a CURRENT next_action of ready_for_approval -- no shortcut; escalation #2360 v3 -> state='in-progress', next_action='review', assigned_to='Claude'
- **OPEN** `SC16:Config-Maintenance.ps1_-Step_Validate`: Config-Maintenance.ps1 -Step Validate failed 2 times this session: + function Write-IbaPaused {; work package : configuration-maintenance
