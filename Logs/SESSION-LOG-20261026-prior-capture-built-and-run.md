# Session log 2026-10-26: the prior-work capture built, applied live, and run on M01, M02, M07, M08 and M09 (#2305)

**Session:** 5d0e964b-6c3b-463c-9979-16e6ce15295d · Developer Mode · model changed to Sonnet 5.5 at the researcher's instruction · compliance file `Logs/compliance/COMPLIANCE-20261026-5d0e964b.md`

## 1. Scope

2026-10-26, one line: the #2305 capture of prior study documents into `ib_observation` and `ib_node` was built (the `Prior-Capture.ps1` tool, its config and schema), piloted on a copy, applied to the live database after the researcher's approval, and then run live, one document per run, on every document of the clusters M01, M02, M07, M08 and M09: 62 of 235 documents done (52 captured, 10 with nothing to capture), 3,146 observations; the 5 other clusters and the no-cluster documents are not started.

## 2. Escalations

| Escalation | Outcome this session |
|---|---|
| #2305 | worked v10 to v19: build started (v11), handed over with the pilot and decisions D1 to D3 (v12), approved with D1 to D3 as recommended (v13), the live runs by cluster (v14 to v18), the unrecorded messages and the state at close (v19). Stays in-progress with Claude; next M10 |
| #2306 | raised by `Config-Maintenance.ps1 -Step Validate` after the live migration (5 coherence errors, all mine: a setting module missing from `config_module`, the script outside `archive/`); resolved self-correctable (v2) |
| #2302 | the 3 coherence errors reported earlier no longer exist (validate clean three times); resolved self-correctable (v2) |
| #2270 | advisory findings recorded by validate (new version); with the researcher |
| #2260, #2268 and the items they carry, #2171, #2172, #2235, #2285, #2296, #2303 | untouched: acknowledged each turn at the Stop hook |

## 3. Files

Code and config:
- `iba/app/lib/priorcapture.py` (new), `iba/app/handlers/priorcapture.py` (new), `iba/app/ps/Prior-Capture.ps1` (new)
- `iba/app/migration/archive/prior_capture_config_2305_v1_20261026.py` (new): table `prior_capture_line`, `reading_file.capture_status`, enums, work package `prior-capture`, method rules CP-01 to CP-10
- `iba/app/tools/temp_2305_prior_capture_test_run.py` (new, the test plan, 48 of 48)
- `iba/docs/ps tools worksheet.xlsx` (tab `Prior-Capture` and its Index row)
- `iba/app/USER-GUIDE.md` (section 7.2), `iba/app/BUILD.md` (entry 420)

Deliverables and records:
- `outputs/escalation/2305-prior-capture-test-v1-20261026.md`, `outputs/escalation/2305-prior-capture-pilot-v1-20261026.md`, `outputs/escalation/2305-pilot-files/`
- `outputs/prior-capture/` (the run reports and status reports) and `outputs/prior-capture/work/` (the fill helpers `cap.py`, `fill_block.py`, `fill_phen.py`, `fill_reading.py` and the per-document fills with their filled JSON)
- pre-run snapshot `iba/app/db/snapshots/iba-20261026T1131Z-pre-2305-prior-capture.db`
- `Logs/compliance/COMPLIANCE-20261026-5d0e964b.md`, this log

Live database: migration applied (63 writes); 3,146 observations, 62 documents' line answers and `capture_status` written through `prior_capture.record`.

## 4. Decisions

- Researcher, 2026-10-26: "this session is elevated into developer mode, and runs with sonnet. proceed with 2305": recorded in #2305 v11
- Researcher, 2026-10-26: "Approved: pilot accepted, D1 a, D2 a, D3 a. Take the pre-run snapshot, apply the migration live, then validate": D1 (RS and NS dispositions as told), D2 (clusterless documents last, only findings with a placeable M or T word), D3 (nodes on M-coded words only) are method rules CP-07, CP-09 and CP-10 in `cfg_method_rule`, and recorded in #2305 v13
- Researcher, 2026-10-26: "Start the live captures in cluster order, beginning with the M01 documents, one document per run", then the same for M02, M07, M08 and M09: recorded in #2305 v14 to v18
- Self-correctable, Claude: Prepare lists same-prefix October ids (FE-64 gap found in the pilot): `iba/app/lib/priorcapture.py` and test T1b2 in `outputs/escalation/2305-prior-capture-test-v1-20261026.md`
- Self-correctable, Claude: the migration's settings registered under a module missing from `config_module`, and the script outside `archive/` (5 coherence errors): #2306 v2
- Method, Claude: the large documents (ledgers, overviews, recovery data, phenomena readings, batch readings) were captured through table and claim passes with the pass-over lines checked and the observations sampled, not each read: recorded in #2305 v15, v16, v17 and v18
- Researcher, 2026-10-26: asked whether to close and restart in a new session, standard or developer; answer given (close now, continue in a fresh Developer Mode session, optionally register the fill helpers as a tool so the rest can run standard): recorded in #2305 v19

## 5. Open items

- **#2305** (Claude): the capture continues in a new Developer Mode session on Sonnet: M10 (19 documents), M18 (47), M20 (3), M25 (18), M47 (33), M53 (1), M64 (34), M72 (8), then the ten documents with no cluster last (CP-09)
- **#2305, to decide:** whether to register the fill helpers (`outputs/prior-capture/work/`) as a tool so that later runs can be standard sessions (CHARTER section 4 allows only registered modules there)
- **#2270** (researcher): the advisory findings of `Config-Maintenance.ps1 -Step Validate`
- **Data, carried in #2305:** the reading index mis-resolves some bare references (Est read as Ecc, chapter-less `12:1-7`), and `Esth.8.12` has no row in `verse` (see #1891)
- Held items unchanged: #2268 and the items it carries (#2260, #2261 to #2267, #2275 to #2284), #2171, #2172, #2235, #2285, #2296, #2303

## 6. Git

_(written after the first commit)_
