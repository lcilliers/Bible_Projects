# Session log 2026-10-26: the scope resolver finished (#2286 closed), and the reading cycle prototyped then parked

**Session:** 79681341-a96b-488b-9db3-0294fa19cd47 · Developer Mode · compliance file `Logs/compliance/COMPLIANCE-20261026-79681341.md`

## 1. Scope

2026-10-26, one line: the remaining #2286 units were finished (U5 the occurrence-shaped scope resolver with #2287, U7 as a method rule, U9 as config only; U6 put on hold), #2286 was closed, the reading cycle on one JSON was designed and prototyped on M18_thirst (#2304), and #2304 was parked so that prior reading work is captured first (#2305).

## 2. Escalations

| Escalation | Outcome this session |
|---|---|
| #2286 | updated v45 to v49 (the researcher's instructions), completed v50 |
| #2295 | in progress v2, ready v3, approved and completed v4 (U5) |
| #2287 | ready v3, approved and completed v4 (fixed in U5) |
| #2296 | put on hold v2 (U6: actioned when a reading reaches its clusters) |
| #2297 | in progress v2, ready v3, approved and completed v4 (U7) |
| #2299 | in progress v2, ready v3, approved and completed v4 (U9) |
| #2303 | raised, on hold (no tool writes cluster_strong for a T-a addition) |
| #2304 | raised; design v1 to v3 and the prototype, v2 to v7; parked on hold v8; comment v9 |
| #2305 | raised (capture prior reading work into ib_observation) |
| #2270 | updated by configmaint.validate (advisory findings changed) |

## 3. Files

- `iba/app/lib/versescope.py`, `iba/app/handlers/versescope.py`, `iba/app/ps/Verse-Scope.ps1`, `iba/app/lib/reading.py`, `iba/app/lib/versecollate.py` (U5)
- `iba/app/migration/archive/scope_resolver_2295_v1_20261026.py`, `iba/app/migration/archive/t_word_and_retire_2297_2299_v1_20261026.py`, `iba/app/migration/archive/retire_grants_2299_v1_20261026.py`
- `iba/app/tools/temp_2295_scope_resolver_test_run.py`, `iba/app/tools/temp_2297_2299_config_test_run.py`, `iba/app/tools/temp_2304_reading_cycle_prototype.py`
- `iba/app/BUILD.md` (sections 416 to 418), `iba/app/USER-GUIDE.md` (sections 7 and 8.3), `iba/docs/ps tools worksheet.xlsx` (tab Verse-Scope)
- `outputs/escalation/2295-u5-scope-resolver-test-v1-20261026.md`, `outputs/escalation/2297-2299-config-test-v1-20261026.md`
- `outputs/escalation/2304-reading-cycle-one-json-design-v3-20261026.md` (v1 and v2 in `outputs/escalation/archive/`), `outputs/escalation/2304-prototype-m18-thirst-results-v1-20261026.md`, `outputs/escalation/2304-prototype/`
- `outputs/verse-scope/m18-desire-2295-20261026.json`, `outputs/verse-scope/m18-thirst-0c-sample-20261026.json`
- `iba/app/db/snapshots/iba-20261026T0900Z-pre-2295-2297-2299.db` (pre-run snapshot)
- `Logs/compliance/COMPLIANCE-20261026-79681341.md`

## 4. Decisions

The researcher's decisions:
- "finish off 2286": recorded in #2286 v45.
- No whole-database sweep; U6 has no build now; U7 a simple config; U9 configs only: recorded in #2286 v46 and #2296 v2.
- U5 closed, U7 as a method rule on reading.apply, U9 as config only: recorded in #2297 v2 and #2299 v2.
- #2295, #2287, #2297 and #2299 approved; #2286 closed with U6 on hold: recorded in #2286 v49.
- The reading cycle on one JSON (0.C, 0.GAP pre, observe) to be designed: recorded in #2304 v1.
- D1 to D5 ruled, and the cluster documents adopted with precedence: recorded in #2304 v3 and #2304 v4.
- D7 b, and the prototype on M18: recorded in #2304 v5.
- #2304 parked; prior work to be recorded first: recorded in #2304 v8 and #2305.

Self-correctable fixes Claude made and closed:
- the resolver matched surfaces without `surfacemap.norm` (37 M18 occurrences missed): fixed in `iba/app/lib/versescope.py`;
- `-Home` collided with PowerShell's HOME: renamed `-HomeScope` with alias in `iba/app/ps/Verse-Scope.ps1`;
- the retired steps' write grants were left live (3 coherence errors): fixed by `iba/app/migration/archive/retire_grants_2299_v1_20261026.py`;
- design v3 overstated the existing nodes on home words: corrected in `outputs/escalation/2304-reading-cycle-one-json-design-v3-20261026.md`.

## 5. Open items

- #2305: capture prior reading work into ib_observation, for Claude once the researcher sets it going.
- #2304: the reading cycle, parked; P1 to P3 with the researcher when it comes back.
- #2296: U6, for Claude when a reading reaches its clusters.
- #2303: a tool to write cluster_strong for a T-a addition, on hold.
- #2268 and its items (#2260 to #2267, #2275 to #2285): parked.

## 6. Git

- Branch: `main`
- Commit: `864e1a4285ffb6ed3813a58c14a9dd38e614204f` ("session 20261026: #2286 finished and closed: ...")
- Push output: `To https://github.com/lcilliers/Bible_Projects.git` / `e89dca6a..864e1a42  main -> main`
