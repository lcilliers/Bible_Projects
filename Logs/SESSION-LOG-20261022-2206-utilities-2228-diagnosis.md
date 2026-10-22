# Session log 2026-10-22: #2206/#2207 utilities, study re-opened and held again, #2228 diagnosis

Session: `45f739ba-488f-4dd4-99f0-7e1b7d8da374` (standard mode). Compliance file:
`Logs/compliance/COMPLIANCE-20261022-45f739ba.md`.

## 1. Scope

2026-10-22. #2177 closed. The last four utilities with no config were settled in standard mode
(#2206/#2207 item 2, BUILD.md sec 390). #2171 was taken back. The study was re-opened, and the 31
anger inner-seat rows were read for basis (26 recorded). The researcher found the reading process
unfit for subset work (#2228, diagnosed in v2), and the study was put on hold again.

## 2. Escalations

- #2177: completed (v29), on the researcher's "do A and close".
- #2206: off hold (v13); five decisions put (v14); approved (v15); build handed over (v17); completed (v18).
- #2207: approved item 2 (v27); progress (v28); back on hold (v29); approvals recorded (v30).
- #2221, #2222, #2223, #2224, #2225: raised by Propose, approved by the researcher, applied, completed (v4).
- #2171: taken back to Claude and on hold (v12-v15).
- #2226, #2227: study re-opened. Raised, approved, applied, completed (v4).
- #2172: stale resolution corrected (v32); seat rows recorded and faces decision put (v33); taken back (v34-v35); on hold behind #2228 (v36); message recorded (v37).
- #2216: five ungrounded seat rows listed (v4).
- #2217, #2218: noted as waiting on #2228 (v4).
- #2220: fix options put to the researcher (v2).
- #2228: raised (v1); diagnosis v1 (v2); researcher correction (v3); v2 diagnosis (v4); researcher ruling (v5); messages recorded (v6).
- #2229, #2230: study on hold again. Raised, approved, applied, completed (v4).

## 3. Files

- `scripts/backup_db_to_nas.py`: settings from `cfg_setting backup.nas_db_backup`, with a built-in fallback.
- `iba/app/lib/clusterfamilyscan.py` -> `iba/app/lib/archive/clusterfamilyscan.py`.
- `iba/app/BUILD.md`: sec 390.
- `outputs/escalation/2172-anger-seat-basis-v1-20261022.md` and `outputs/escalation/2172-anger-seat-basis-v1-20261022/anger-seat-import.json`.
- `outputs/escalation/2172-life-death-seat-faces-decision-v1-20261022.md` (withdrawn from decision, #2172 v34).
- `outputs/escalation/2228-subset-rebuild-diagnosis-v2-20261022.md`; v1 at `outputs/escalation/archive/2228-subset-rebuild-diagnosis-v1-20261022.md`.
- `outputs/strand-reading/anger/anger-gather-v1-20261022.md`.
- `Logs/compliance/COMPLIANCE-20261022-45f739ba.md`.
- iba.db: `cfg_utility` (lexicalscope, handlers_catalogue, clusterfamilyscan, scripts_backup_db_to_nas); `cfg_setting` (backup.nas_db_backup, behaviour.study_state, governance.study_status); `ib_observation` 12453-12478 with their `ib_node` rows.

## 4. Decisions

The researcher's:
- Close #2177 under option A: #2177 v29.
- #2206 off hold: #2206 v13.
- #2207 item 2, option a on decisions 1 to 5: #2206 v15.
- Build in standard mode, through Propose: #2207 v28.
- Re-open the study: #2226 v4, #2227 v4.
- The reading process is wrong for subset work: #2228 v3.
- Break #2228 down in a Developer Mode session, and put the study on hold: #2228 v5, #2230 v4.

Claude's:
- #2171 taken back rather than approved: #2171 v12.
- #2172 stale resolution corrected: #2172 v32.
- The basis of the 31 seat rows set by reading their verses: `outputs/escalation/2172-anger-seat-basis-v1-20261022.md`.
- The faces decision withdrawn as not ready: #2172 v34.

## 5. Open items

For the researcher:
- #2220: SC16 fix, option A, B or C.

For Claude, in a Developer Mode session:
- #2228: break down the analysis design before anything is built.

Waiting behind #2228:
- #2172: catch-up C; the 26 seat observations stay at draft.
- #2216, #2217.
- #2218 (OT-108).
- #2171: the shame strand.

Parked:
- #2207: items 3 and 4.

## 6. Git

Written after the first commit.
