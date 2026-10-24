# Session log 2026-10-24: the reading on the phases and the observation record (#2273, #2274)

**Session:** 8e8a0eb9-e5eb-4c11-9e80-1516940a35ed · Developer Mode · compliance file `Logs/compliance/COMPLIANCE-20261024-8e8a0eb9.md`

## 1. Scope

2026-10-24, one line: #2268 builds B1 (Reading.ps1 on the phases) and B2 (the observation record) were designed through six versions on the researcher's corrections (the observation and node model, parties as findings, the ledgers and the catalogue compared, qualifiers), then built as one change set, tested 47/47 on a copy, applied live and accepted.

## 2. Escalations

| Escalation | Outcome this session |
|---|---|
| #2273 | updated v4 to v19: design v1 to v6 with the researcher's corrections recorded verbatim (v6, v8, v10, v12, v14), approved (v16), built and tested (v17), accepted (v18), completed (v19) |
| #2274 | updated v2 to v17, alongside #2273; completed (v17) |
| #2266 | updated (v3): the fragment observations and the node and parties findings of the inspection, for W-3 |
| #2268 | updated (v24): B1 and B2 done and accepted; the researcher's go-ahead for the comparison recorded |
| #2270 | updated by configmaint.validate (new version): the advisories down to 2 orphan configs and no worksheet drift; with the researcher |

## 3. Files

- `outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md` (v1 to v5 in `outputs/escalation/archive/`)
- `outputs/escalation/2273-ib-observation-and-node-usage-v2-20261024.md` (v1 archived)
- `outputs/escalation/2273-what-a-verse-reading-teases-out-v1-20261024.md`
- `outputs/escalation/2273-2274-test-results-v1-20261024.md`
- `iba/app/migration/archive/reading_phases_2273_v1_20261024.py`
- `iba/app/lib/observationrecord.py` (new), `iba/app/lib/reading.py`, `iba/app/handlers/reading.py`, `iba/app/ps/Reading.ps1`
- `iba/app/tools/temp_2273_reading_phases_test_run.py`
- `iba/app/BUILD.md` (section 408), `iba/app/USER-GUIDE.md` (section 8.2)
- `iba/docs/ps tools worksheet.xlsx` (tab Reading)
- `iba/app/db/snapshots/iba-20261024T165349Z-pre-2273-reading-phases.db` (the pre-run snapshot)
- `Logs/compliance/COMPLIANCE-20261024-8e8a0eb9.md`

## 4. Decisions

Researcher's decisions:
- Design B2 and B1 first, in one design: recorded in #2273 v4.
- The observation carries the description, the nodes apply it; inspect the two tables first: recorded in #2273 v6.
- A party's role is an observation, not a table: recorded in #2273 v8.
- Compare the ledgers with the catalogue before placing the parts: recorded in #2273 v10; the go-ahead in #2268 v24.
- D1 to D8 (one change set; kind as tag; route and setting on the finding; Narrate its own step; no reclassification; role per finding; a node on every word in focus) and the reading of qualifiers: recorded in #2273 v12.
- D9 (qualifiers evaluated for value, no fixed list): recorded in #2273 v14.
- D3 confirmed and the build approved: recorded in #2273 v16; applied to cfg_setting, cfg_enum, cfg_step, cfg_method_rule, cfg_column, cfg_table (iba/app/migration/archive/reading_phases_2273_v1_20261024.py).
- The build accepted as done: recorded in #2273 v18.

Claude's self-correctable fixes and execution choices (closed or recorded):
- The words in focus and the function-word rule held in config (reading.focus_words), and the prompts by kind (reading.observe_prompts): recorded in iba/app/BUILD.md section 408.
- Four config rows naming the old step or shape (B:76, governance.narrative_home, RN-15, cfg_control_home study_method) repointed: recorded in iba/app/BUILD.md section 408.
- The Reading.ps1 param comment reworded so the worksheet check no longer reads HOME as a parameter: recorded in iba/app/BUILD.md section 408.

## 5. Open items

- #2268: builds B3 to B12 (#2275 to #2284), each its own design first; Claude.
- #2276 (B4, the collation reading every observation) and #2278 (B6, the pre-gap detectors still empty) are the next pieces this build names; Claude.
- #2260 to #2267: restated in W-3 against the new record; Claude, after the builds.
- #2270: the validate advisories (2 orphan configs); the researcher.
- #2285: the last live Workflow instruction files; Claude.
- #2171, #2172, #2235, #2218 (OT-108): study work, on hold; Claude in a standard session.

## 6. Git
