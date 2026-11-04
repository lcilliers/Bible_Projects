# Session log 2026-11-04: the surface judging run, its cycle, and the rule for long jobs (#2354)

Session id: 7631fc39-0dd9-4993-9a5b-cdc06793adce (Developer Mode, started 2026-11-03, closed 2026-11-04).

## 1. Scope
Developer Mode on #2354 (Reset narrative, the first split of the concept surfaces into behaviour, inner_being_state, being and other, judged one surface at a time by the Ollama server, model `qwen3:30b`). Found the working route (ssh, the batch key without passphrase) and made the run open its own ssh tunnel; tested prompt v3 on the 23 labelled surfaces (13 of 23, accepted by the researcher); built the unattended cycle (work periods, cool-down, progress file, stop and restart) and fixed a database write-lock held by long steps; pruned obsolete tests (92 of 92 on a copy); started the full run of 6,069 surfaces; exported the results to CSV and Excel and wrote a progress report; found that the cycle died at 22:57 UTC on 2026-11-03 when the machine slept and the Claude app closed its session (the cycle had been started in a Claude terminal tab); relaunched it outside the app and added rule B:125 so a long job is always started outside the session. At close the cycle is still running (about 5,300 of 6,069 judged, 0 failed, finish estimated about 08:12 UTC) and is not stopped by the close. Nothing was written to the study tables; every group is the model's inferential answer.

## 2. Escalations
- #2354 (Reset narrative): updated v34, v35, v36, v37 (v37 carries the researcher's messages of the session verbatim); assigned to the Researcher, ready_for_approval; not completed.
- #2357 (open escalation of config advisories): `configmaint.validate` found the same findings and did not re-raise; not touched by hand.

## 3. Files
- `iba/app/db/iba.db`: cfg rows through `apply_logged`: `ollama.ssh_target`, `ollama.ssh_key` (run DEVMODE-2354-EXTERNAL-SERVICE-ACCESS-20261103), the preflight settings, prompt v2 and v3, `ollama.tunnel_local_port` (DEVMODE-2354-SSH-TUNNEL-20261103), the four cycle settings and the steps cycle, progress and stop (DEVMODE-2354-SURFACE-JUDGE-CYCLE-20261103), behaviour rule B:125 with its scope row (DEVMODE-2354-LONG-RUNNING-JOB-20261104). Named snapshots in `iba/app/db/snapshots/kept/` before each.
- Migrations in `iba/app/migration/archive/`: `external_service_access_2354_v1_20261103.py`, `surface_judge_preflight_2354_v1_20261103.py`, `surface_judge_prompt_2354_v2_20261102.py`, `surface_judge_prompt_2354_v3_20261103.py`, `surface_judge_tool_2354_v1_20261102.py`, `ssh_tunnel_2354_v1_20261103.py`, `surface_judge_cycle_2354_v1_20261103.py`, `long_running_job_2354_v1_20261104.py`.
- Code: `iba/app/lib/surfacejudge.py`, `iba/app/handlers/surfacejudge.py`, `iba/app/ps/Surface-Judge.ps1`.
- Throwaway scripts: `iba/app/staging/surface_judge_tests/temp_2354_surface_judge_tests.py` (92 cases), `iba/app/staging/surface_judge_tests/temp_2354_export_batch.py`; the pilot moved to `iba/app/staging/archive/surface_judge_pilot_2354/temp_2354_pilot.py`.
- Documents: `iba/app/BUILD.md` (sections 450 to 454), `iba/app/USER-GUIDE.md` (section 8.8, including Running a long job), `iba/app/GOVERNANCE.md` (section 3), `iba/docs/ps tools worksheet.xlsx` (tab Surface-Judge), `outputs/escalation/2354-surface-judge-test-plan-v1-20261102.md`.
- Results: `outputs/concept-mapping/surface-group/first-split-v3-20261103.jsonl` (still being appended by the running cycle), its `.progress.json`, `first-split-labels-v1-20261102.csv`, `first-split-v1-20261102.jsonl`, `first-split-v2-20261102.jsonl`, the CSV and Excel exports, `first-split-v3-progress-report-v1-20261103.md`, and `archive/` (the throwaway cycle check).
- `Logs/surface-judge-cycle-20261104.log` (output of the cycle relaunched outside the session), `Logs/compliance/COMPLIANCE-20261103-7631fc39.md`, config reports `outputs/configs/CONFIG-REPORT-v687-20261103.md` and later versions.

## 4. Decisions
- The researcher: the batch key without a passphrase is used for the server; recorded in #2354 v37.
- The researcher: the splits between state and behaviour are accepted; the border is settled in context and downstream; prompt v3 stays; `being` is hard for the model and the researcher will deal with it separately; recorded in #2354 v37.
- The researcher: one unattended cycle with cooling, progress reporting, stop and restart; recorded in iba/app/BUILD.md section 452.
- The researcher: the 60 and 10 minute timings stay unchanged (the server temperature held steady); recorded in #2354 v37.
- The researcher: `rows_in_surface_subgroup` is not a weight; the column is `rows_for_word`; recorded in #2354 v37 and iba/app/BUILD.md section 454.
- The researcher: update the config so a long job is never started in a way that depends on the Claude session; recorded in `cfg_behaviour_rule` (id 125) and iba/app/BUILD.md section 453.
- Self-corrected by Claude: the write lock held by long steps (the two handlers commit first), the speed and finish estimates, and the way the cycle was launched (relaunched through Win32_Process.Create); recorded in iba/app/BUILD.md sections 452 and 453.

## 5. Open items
- #2354, with the Researcher: whether `Cycle` should launch itself detached in code; whether a killed job should leave its run row at `running`; the machine's sleep setting (60 minutes on mains power, the researcher's to change); design and approval of the load of confirmed groups into `surface_subgroup.surface_group` (a database write), which must allow for one group per word applied to many rows; the second pass over `other`; the behaviour and state analysis after the run; the `being` group.
- The running cycle: if Windows sleeps it ends; resume with the command in iba/app/USER-GUIDE.md section 8.8. #2357 (config advisories) remains with the Researcher.

## 6. Git
Branch: main. Commit 56abe80f853fb01285973538f99a7e5edefc93ff, `session 20261104: surface judging cycle and progress, ssh tunnel, rule B:125 for long-running jobs, #2354 record (v34-v37), BUILD 450-454, exports and progress report, session log, compliance file and close reports`.
Push output: `To https://github.com/lcilliers/Bible_Projects.git   1fc77d4a..56abe80f  main -> main`.
The batch file `first-split-v3-20261103.jsonl` and its progress file were committed as they stood: the cycle was still running outside the session and keeps appending, so the next session commits them again.
