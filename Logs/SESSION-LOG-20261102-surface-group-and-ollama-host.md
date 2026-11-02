# Session log 2026-11-02: surface group column, Ollama host and the judging library (#2354)

Session id: 9ee0965a-ede0-48ed-84c4-d23054fdfb69 (Developer Mode, started 2026-11-01, closed 2026-11-02).

## 1. Scope
Entered Developer Mode to work on #2354 (Reset narrative, the concepts retry at surface grain). Added the `surface_group` column and its five values to `surface_subgroup`; recorded the workings and the researcher's rulings in a living log; measured the corpus (544,667 live occurrences, 18,249 distinct surface strings); set up access to the researcher's Ollama server (SSH key, settings, model `qwen3:30b`); found that multi-code spans share the span's English among their codes (52.4 percent of rows); built the table `surface_pair_verdict` and the Ollama settings; wrote a judging library; the first (pair-based) pilot failed and was stopped; the researcher corrected the design to one verdict per surface string; the session closes there so the researcher can restart from a different angle. No verdict was written to any table.

## 2. Escalations
- #2354 (Reset narrative): updated v14 and v15 (v15 carries the researcher's words verbatim and the hand-over); assigned to the Researcher, ready_for_approval, needs follow-up 1; not completed.
- #2357 (open escalation of config advisories): findings changed after my settings were added (recorded on it as a new version by `configmaint.validate`); not touched by hand.
- #2355, #2356: completed in the previous session; not touched.

## 3. Files
- `iba/app/db/iba.db`: column `surface_subgroup.surface_group`; table `surface_pair_verdict` (empty); `cfg_*` rows through `apply_logged` (runs DEVMODE-2354-SURFACE-GROUP-20261101, DEVMODE-2354-SURFACE-GROUP-QUALIFIER-20261102, DEVMODE-2354-PAIR-VERDICT-20261102, DEVMODE-2354-CONFIG-MODULES-20261102).
- `iba/app/migration/archive/add_surface_group_2354_v1_20261101.py`, `add_surface_group_qualifier_2354_v1_20261102.py`, `surface_pair_verdict_2354_v1_20261102.py`, `add_config_modules_2354_v1_20261102.py`: the four migrations.
- `iba/app/lib/surfacejudge.py`: the judging library (pair functions, unused; per-surface functions, not run).
- `iba/app/staging/surface_judge_pilot_2354/temp_2354_pilot.py`: throwaway pilot script.
- `outputs/escalation/2354-working-log.md`: the living log (rulings 1 to 18, findings 1 to 30). `outputs/escalation/2354-concepts-retry-plan-v5-20261102.md`: plan v5 (v4 moved to `outputs/escalation/archive/`). `outputs/escalation/2354-session-close-comment-20261102.md`: the v15 comment. `outputs/concept-mapping/surface-group/pilot-2354-v1-20261102.jsonl`: the 7 surfaces of the failed pair pilot.
- `iba/app/BUILD.md`: sections 443 to 446. Rollback snapshots in `iba/app/db/snapshots/kept/`: `iba-20261101T175014Z-2354.db`, `iba-20261102T045042Z-2354-qualifier.db`, `iba-20261102T104709Z-2354-pair-verdict.db`.
- `Logs/compliance/COMPLIANCE-20261101-9ee0965a.md`, the config and escalation reports under `outputs/configs/` and `outputs/escalation/`, and the close report.
- Outside the project: a new ssh key pair `~/.ssh/id_ed25519_iba` (public half installed on the server by the researcher); the user PATH change was the researcher's own.

## 4. Decisions
- Researcher: no layer column on `surface_subgroup`; the kinds of being are concept domains, not values of the column; recorded in #2354 v15 and `outputs/escalation/2354-working-log.md` (rulings 2, 3).
- Researcher: a qualifier is a value of `surface_group`; the use that makes it one is what matters, not a marker for which group it supports; recorded in #2354 v15 and `iba/app/BUILD.md` (section 444).
- Researcher: ignore the take-out list; all surfaces of the corpus are considered; each surface is processed once; use the Ollama server; the story mapping is the next work package; recorded in #2354 v15 and `outputs/escalation/2354-working-log.md` (rulings 11 to 15).
- Researcher: "Use my approach" for multi-code spans (particle codes are qualifiers by rule, own pairs judged, span-shared pairs judged as a unit and listed for inspection); recorded in `outputs/escalation/2354-working-log.md` (ruling 16) and #2354 v15. Superseded in practice by ruling 18.
- Researcher: pronouns are qualifiers; recorded in `outputs/escalation/2354-working-log.md` (ruling 17) and #2354 v15.
- Researcher: P2 (the use list) and P3 (the verdict table) are left to Claude's judgement; recorded in #2354 v15.
- Researcher: apply the test to the list of surfaces, one verdict per surface; recorded in `outputs/escalation/2354-working-log.md` (ruling 18, finding 30) and #2354 v15.
- Claude, design calls: the 13-value use list and the per-pair table `surface_pair_verdict`; recorded in `iba/app/BUILD.md` (section 445) and `cfg_table`. The per-pair design is withdrawn in practice; its replacement is an open decision.
- Claude, self-correctable: added the modules `ollama` and `surface_judge` to `enum.config_module` after `configmaint.validate` reported 9 coherence errors from my first migration; recorded in `iba/app/BUILD.md` (section 445).

## 5. Open items
- #2354 (Researcher): restart from the researcher's chosen angle; decide whether `surface_pair_verdict` is replaced by a per-surface table; the per-surface functions in `iba/app/lib/surfacejudge.py` are not run, not tested, not registered as a tool.
- #2354 (Researcher): whether the multi-code span rule of BUILD 428 (particles keep the span's English) and a head marker in `verse_lexical` are raised as their own escalation (working log finding 28).
- #2354 (Claude): the story mapping (Q4) is the next work package after this one; the five open questions of `outputs/concept-mapping/inner-being-story-fit-v2-20261101.md` are unanswered.
- #2357 (Claude): config advisories; the new `ollama.*` and `surface_judge.batch_dir` settings are read by no registered code yet.
- #2354 (Researcher): the Ollama server is being reconfigured by the researcher (CPUs and memory); the address in `ollama.host` may change.

## 6. Git
Branch: main. First commit: 3e591fe9, `session 20261102: surface group qualifier value (#2354), pair verdict table and Ollama settings, judging library and pilot, BUILD 443-446, working log, plan v5, session log, compliance file and close reports`. The first push failed with `fatal: unable to access 'https://github.com/lcilliers/Bible_Projects.git/': Could not resolve host: github.com`; the retry gave `To https://github.com/lcilliers/Bible_Projects.git` / `6eb805b8..3e591fe9  main -> main`. The researcher's own edit to `scripts/SQLite/IBA_DB/explore-concepts-1.sqlite3-query` (extra select statements) was included in the first commit.
