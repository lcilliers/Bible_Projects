# Test plan and results: the surface judging tool (#2354, rule B:46)

Tool: `iba/app/ps/Surface-Judge.ps1` (work package `surface-judge`, steps `surface_judge.status` and `surface_judge.run`), library `iba/app/lib/surfacejudge.py`, handlers `iba/app/handlers/surfacejudge.py`. Test script (re-runnable, throwaway `temp_` prefix): `iba/app/staging/surface_judge_tests/temp_2354_surface_judge_tests.py`. Run 2026-11-02 against a copy of `iba.db` with the migration applied, a stub Ollama server for the deterministic cases and the real server (`qwen3:30b`) for 3 surfaces; then the PowerShell front on the live database.

**Result: 57 of 57 cases pass on the copy (46 at the first build, 11 added 2026-11-03 for prompt v3 and the server check); the live PowerShell checks below pass.** One case set (list, order) passed only after two corrections to the tests themselves, listed at the end.

## A. Settings (library `settings()`)

| Case | What it covers | Result |
|---|---|---|
| S1 | the four groups and the prompt read from the copy; prompt has `{surface}` | pass |
| S2 | a missing setting (`ollama.model`) stops the run and names it | pass |
| S3 | an empty groups list stops the run | pass |
| S4 | a prompt without `{surface}` stops the run | pass |

## B. Checking an answer (`check_word`)

| Case | What it covers | Result |
|---|---|---|
| C1 | a valid group passes | pass |
| C2 | an unknown group (`qualifier`, no longer allowed in the first split) is refused | pass |
| C3 | an answer that is not an object is refused | pass |
| C4 | an answer with no group is refused | pass |

## C. Judging one surface (`judge_word`, stub server)

| Case | What it covers | Result |
|---|---|---|
| J1 | a good answer is recorded with model name, token counts, no errors | pass |
| J2 | a bad group then a good one: retried once, recorded, the first error kept | pass |
| J3 | two bad answers: `group` null, two errors, `judged_by` null | pass |
| J4 | answers that are not JSON (twice): `group` null, call-failed errors | pass |
| J5 | `other` with its reason | pass |
| J6 | a surface containing a quote mark is sent whole | pass |
| J7 | server unreachable: `group` null, two errors, no crash | pass |

## D. The list and the status

| Case | What it covers | Result |
|---|---|---|
| L1 | the list is the distinct live non-blank surfaces of `surface_subgroup`: 6,069 (the 4 live rows with a blank surface are left out) | pass |
| L2 | most rows first, then alphabetical, for every neighbouring pair (first three: strong 28, right 26, desire 24) | pass |
| L3 | no empty or null surface in the list | pass |
| T1 | status with no file: nothing judged, all 6,069 left | pass |
| T2 | status after 2 judged: counts per group, 6,067 left | pass |
| T3 | a batch with no failures reports 0 failed | pass |

## E. Running a batch (`run_words`)

| Case | What it covers | Result |
|---|---|---|
| R1 | `limit` 4 judges 4 and writes 4 lines | pass |
| R2 | run again: only the 2 not yet judged are sent | pass |
| R3 | run again when all are done: nothing is sent | pass |
| R4 | a word with no usable answer is recorded with `group` null (1 judged, 1 failed) | pass |
| R5 | the next run tries only the failed word again | pass |
| R6 | the last record of a word is the one read | pass |
| R7 | Ctrl+C: the run stops, the word in hand is already written | pass |

## F. The handlers (copy, scratch batch folder)

| Case | What it covers | Result |
|---|---|---|
| H1 | status without `-Batch` is refused | pass |
| H2 | refused batch names: capital letters, underscore, no version, `v0`, short date, `../` path | pass (6 of 6) |
| H3 | status of a batch with no file says "no file yet" | pass |
| H4 | `-Limit` of `0`, `-1`, `abc`, `1.5` is refused | pass (4 of 4) |
| H5 | run `-Limit 3` judges 3, writes the file in `batch_dir`, 6,066 left | pass |
| H6 | run again carries on with the next surfaces, not the first ones again | pass |
| H7 | status after the two runs: 5 judged | pass |
| H8 | a missing setting is refused and nothing is written | pass |

## G. The real server (copy)

| Case | What it covers | Result |
|---|---|---|

Timing seen: the first call took 136.9 s (the model loading), the next two 6.8 s and 6.1 s.

## H. The registered tool on the live database (PowerShell)

| Case | Command | Result |
|---|---|---|
| P1 | `Surface-Judge.ps1 -Action Status -Batch first-split-v1-20261102` | pass: no file yet, list 6,069, left 6,069, exit 0 |
| P2 | `-Action Status -Batch Bad_Name` | pass: refused with the naming rule, nothing written |
| P3 | `-Action Run -Batch first-split-v1-20261102 -Limit 0` | pass: refused, nothing written |
| P4 | `-Action Run -Batch first-split-v1-20261102 -Limit 3` | pass: strong = inner_being_state (11.3 s), right = inner_being_state (11.0 s), desire = behaviour (7.1 s); progress lines on the terminal, the result line intact, 6,066 left; 3 lines written to `outputs/concept-mapping/surface-group/first-split-v1-20261102.jsonl` |
| P5 | `Config-Maintenance.ps1 -Step Validate` | pass: the only finding about this tool (no tab in the ps tools worksheet) was fixed in the same unit; the next run shows none |

## Not covered

- A full run of the 6,069 surfaces, and its total time.
- The server going away part-way through a long run is covered only as J7 (unreachable) and R4/R5 (failed word, tried again).
- The quality of the model's answers. This plan tests that the tool works, not that the groups are right; every answer is inferential until confirmed.

## Two corrections to the tests themselves

1. J6 first failed because my stub server cut the English at the first quote mark; the stub was changed, the library was not.
2. L1 first failed (6,069 against 6,070) because the table has 4 live rows with a blank surface; the library skips them (there is nothing to ask the model), and the test now says so.

## Observation, not a defect

The model gives a long `reason` for `inner_being_state` and `behaviour` answers although the prompt asks for a reason only for `other` (for example for "good": a sentence citing Luke 8:15). The tool records the answer as given and does not trim it.

## I. Prompt v3 and the check before a run (added 2026-11-03)

| Case | What it covers | Result |
|---|---|---|
| S1, S6 | the groups include other, every stored-as key is a group (a key that is not a group stops the run), the prompt has {surface} | pass |
| C5 | the stored name being is not accepted from the model (it is told entity) | pass |
| J2 | an answer entity is recorded as the stored name being | pass |
| PF1 | the check passes when the server answers and has the model | pass |
| PF2 | nothing listening: refused, names the host, says nothing was run | pass |
| PF3 | a model the server does not have: refused, names the models it has | pass |
| PF4 | a run against a dead server stops before the first surface and writes no file | pass |
| PF5 | an address that never answers: gives up within the 2 s set (2.0 s) | pass |
| PF7 | 3 surfaces in a row with no answer halt the run, 3 lines written, not 5 attempts | pass |
| PF8 | 2 fail, 1 passes, 2 fail: the count resets, no halt | pass |
| H9 | the handler refuses a dead server, names it, writes no file | pass |
| H10 | the handler reports a halt as the condition halted | pass |
| P6 | live tool, `-Action Run -Batch first-split-v3-20261103 -Limit 23`, server not answering | pass: refused in 11.1 s, nothing written, file unchanged (16 lines) |

Three test fixtures needed correcting for the new settings and the new `halted` key in the run result (S6, R1, R4); the library was not wrong.

## J. The ssh tunnel (added 2026-11-03)

| Case | What it covers | Result |
|---|---|---|
| TN1 | no tunnel port set: the values pass through unchanged | pass |
| TN2 | a tunnel port without ssh_target and ssh_key stops the run | pass |
| TN3 | a tunnel that cannot be opened (unknown key) refuses, naming the target and key, nothing run | pass |
| TN4 | the failed tunnel leaves nothing listening on its local port | pass |
| TN5 | run_words with an unopenable tunnel writes no file | pass |
| TN6 | the copy carries ollama.tunnel_local_port (11435) | pass |
| TN7 | the real server answers through the tunnel and has qwen3:30b | pass |
| TN8 | the tunnel is closed after the block | pass |
| P7 | live tool, `-Action Run -Batch first-split-v3-20261103 -Limit 23`: 23 judged, 0 failed, tunnel opened and closed by the run | pass |

The stub cases run without a tunnel (their settings carry no tunnel port). Whole plan on the copy: 70 of 70.

## K. The cycle (added 2026-11-03)

| Case | What it covers | Result |
|---|---|---|
| CY0, CY9a to CY9e | the four cycle settings read from the copy (60, 10, 10, 3); a missing, zero, text or true value stops the cycle; a cool-down of 0 is allowed | pass |
| CY1, CY1b | 10 surfaces across 2 work periods end finished, each judged once; a rest is taken between periods | pass |
| CY2 | while it runs the progress file moves: state, judged, per group, mean seconds, estimated finish | pass |
| CY3, CY3b | a stop flag ends it after the surface in hand (3 judged); running it again clears the flag, resumes, finishes, no surface twice | pass |
| CY4 | a stop flag during a rest ends the cycle at once | pass |
| CY5 | no server: 2 periods with no progress end the cycle halted, naming the address, nothing written | pass |
| CY6 | the server comes back during the wait: the cycle finishes, halt count back to 0 | pass |
| CY7, CY7b | a second cycle on a batch with fresh progress is refused; a progress file an hour old (interrupted cycle) does not block a restart | pass |
| CY8 | a surface that never answers: the others are judged, the cycle ends halted with 1 failed | pass |
| CY10a to CY10h | handlers: Progress with no file, on a stalled file (says NOT running), on a live file (resume time, estimated finish); Stop with no cycle, with a live one; Cycle refused on a live batch; Cycle through the handler finishes the list | pass |
| CYR1 | the cycle on the real server through the tunnel judges 3 surfaces and finishes | pass |
| P8 | live, PowerShell: `Cycle` on a throwaway batch; `Progress` from a second command while it ran; `Stop`; state stopped; `Cycle` again resumed | pass, after the database-lock fix (see BUILD 452) |

Whole plan on a fresh copy of iba.db (a copy is single-use): 92 of 92.

Not covered: the quality of the answers beyond the 23 labelled surfaces (see the escalation); a cool-down measured against the server's temperature (the cool-down is a fixed time).
