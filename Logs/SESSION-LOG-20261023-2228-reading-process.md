# Session log — 2026-10-22/23 — the reading process built, thread items worded, the study re-opened

Session id: `17ac2129-4964-4787-9bc5-5c1c32d28250` (Developer Mode). Close report:
`iba/app/reports/session-close-v169-20261023.md` (and its re-runs). Compliance file:
`Logs/compliance/COMPLIANCE-20261022-17ac2129.md`.

## 1. Scope

2026-10-22 to 2026-10-23, Developer Mode:

- **#2228 (the reading process), discovery to build:**
  - the scope resolver (Verse-Scope);
  - the cluster reading index (Reading-Index);
  - the collation (Verse-Collate);
  - the reading process design v2, then the build: Reading.ps1, three gates, with the strand steps retired.
- **#2236 (open items):** the Open-Item tool, and every open-item thread reworded.
- **Smaller items:**
  - #2220 (SC16 designed stops);
  - #2231 and #2232 (the observation use, manifest archive);
  - #2233 (the bare-strong rule).
- **Close:** #2235 held as exception handling; the study re-opened on the researcher's instruction.

## 2. Escalations

- #2228: decisions D-a to D-d recorded (v29), the build approved (v30), put for approval (v31), approved and completed (v32).
- #2236: open items designed and built (BUILD.md s395-s397); judgement calls approved; completed (v12).
- #2220: decision B approved and built (s394); completed.
- #2231, #2232, #2233, #2234: raised and resolved this session (s391-s393).
- #2235: key words of a scope and reverse lookup. Held as exception handling; the key words are judged in use (v3, v4). On hold.
- #2237: raised from OT-101, the narrative style guide v3 (task, on hold).
- #2238: note recording two of the researcher's instructions verbatim.
- #2217: comment (v5). Unread strand hits are now the reading's `hit_unread` gap.
- Threads reworded or settled: OT-97, OT-105, OT-106, OT-05, OT-107, OT-108, OT-01, OT-91, OT-92, OT-94, OT-11, OT-99, OT-98, OT-102, OT-12, OT-104, OT-03, OT-07 and OT-100.
- Completed on their last item: OT-93, OT-06, OT-09 and OT-101.

## 3. Files

**Code (new):**
- `iba/app/lib/versescope.py`, `iba/app/handlers/versescope.py`, `iba/app/ps/Verse-Scope.ps1`
- `iba/app/lib/readingindex.py`, `iba/app/handlers/readingindex.py`, `iba/app/ps/Reading-Index.ps1`
- `iba/app/lib/versecollate.py`, `iba/app/handlers/versecollate.py`, `iba/app/ps/Verse-Collate.ps1`
- `iba/app/lib/openitem.py`, `iba/app/handlers/openitem.py`, `iba/app/ps/Open-Item.ps1`
- `iba/app/lib/reading.py`, `iba/app/handlers/reading.py`, `iba/app/ps/Reading.ps1`

**Code (changed):**
- `iba/app/lib/strandreading.py`, `iba/app/lib/escalation.py`, `iba/app/lib/narrativeregister.py`
- `iba/app/lib/versemeta.py`, `iba/app/lib/manifest.py`, `iba/app/lib/sessionwindow.py`
- `iba/app/handlers/session_close.py`, `iba/app/ps/Narrative-Register.ps1`

**Retired:** `iba/app/handlers/archive/strandreading.py`, `iba/app/ps/archive/Strand-Reading.ps1`

**Migrations:** `iba/app/migration/archive/` (the files dated 20261022-20261023, ending with
`reading_process_2228_v1_20261023.py` and `study_active_2228_v1_20261023.py`)

**Tests:** `iba/app/tools/temp_2228_*`, `temp_2236_open_item_test_run.py`, `temp_2231_2232_test_run.py`,
`temp_2220_sc16_test_run.py`

**Docs:**
- `iba/app/BUILD.md` s391-s399, `iba/app/USER-GUIDE.md`
- `iba/docs/ps tools worksheet.xlsx`
- `outputs/escalation/2228-*`, `outputs/escalation/2236-*`
- `outputs/open-items/`

## 4. Decisions

- #2228 design v2: D-a retires the strand steps (read as all eight), D-b, D-c and D-d yes. Recorded in #2228 v29.
- #2228 reading process accepted as built. Recorded in #2228 v32.
- #2236 judgement calls stand (OT-05 B1/B2 not carried, OT-93 withdrawn, OT-101 to #2237, OT-06.1 and OT-09.1 superseded). Recorded in #2236 v12.
- #2220 decision B. Recorded in #2220 v4.
- #2235: reverse lookup held as exception handling, key words judged in use. Recorded in #2235 v4.
- The study re-opened. Recorded in cfg_setting governance.study_status and #2238 v1.

## 5. Open items

- 295 open thread items, 284 worded (`outputs/open-items/open-items-review-v4-20261023.md`). OT-108.3-.9 await recording through readings.
- Claude-held: #2171, #2172, #2216 (study work, now that the study is active); #2235 (on hold).
- #2237: style guide v3 (on hold, with the researcher).

## 6. Git

- Branch: `main`.
- Commit: `990ae00b`, "session 20261023: #2228 the reading process built and closed -- ...".
- Push: `To https://github.com/lcilliers/Bible_Projects.git  5215b0e8..990ae00b  main -> main`.
- This section is committed alone as "session 20261023: session log git confirmation".
