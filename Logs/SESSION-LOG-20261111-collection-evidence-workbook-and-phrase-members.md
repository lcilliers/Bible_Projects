# Session log 2026-11-11 — collection evidence report as a reading plus workbook (#2477), phrases as members with engagement (#2479) (Developer Mode)

Session id: ec78b300-661e-4b1f-9b90-33ec44710796 (started 2026-11-11 12:53 UTC, closed 2026-11-11).

## 1. Scope

Developer Mode session. Built #2477: the collection evidence report is now a Markdown reading built up from the Strong's codes behind the members, plus an Excel workbook of 20 sheets (one for each listing) in place of the CSV (1,935 lines against 38,195). Built #2479 on the researcher's decision: phrases attached to a collection are members of it (`collection.member_tiers`), `Engagement.ps1 -Action Pull -Missing`, the evidence report counts the phrases, and the 45 phrase rows of `search` were assessed and recorded as engagement observations (inferential, B:4). Config validation kept clean through two notices.

## 2. Escalations

- #2463: updated (v7), left in progress; waits on #2477.
- #2477: updated (v2 in progress, v3 handed over for approval, v4 researcher's words recorded); with the researcher.
- #2478: a code-raised config finding (a stale worksheet column), withdrawn (v3).
- #2479: raised, plan handed over, researcher's decision and approval recorded, built, handed over, completed (v8).
- #2480: a code-raised config finding (the new worksheet flag), withdrawn (v3).
- #2481: raised on hold (engagement of the phrase rows of the other 37 collections).
- #2482: raised (six phrases moved to the group other), handed over, completed (v4) on option A.
- Read and left untouched: #2448 (parked), #2376, #2377.

## 3. Files

- Code: `iba/app/lib/collectionevidencereport.py` (new), `iba/app/lib/collectionevidence.py`, `iba/app/lib/collectionexport.py`, `iba/app/lib/engagement.py`, `iba/app/handlers/collectionbuild.py`, `iba/app/handlers/engagement.py`, `iba/app/ps/Collection-Build.ps1`, `iba/app/ps/Engagement.ps1`.
- Tests: `iba/app/tools/temp_2477_evidence_report_test_run.py` (18 cases), `iba/app/tools/temp_2479_phrase_members_test_run.py` (10 cases).
- Migrations (archive): `iba/app/migration/archive/collection_evidence_report_2477_v1_20261111.py`, `iba/app/migration/archive/phrase_members_2479_v1_20261111.py`.
- Documents: `iba/app/BUILD.md` (sections 491, 492), `iba/app/USER-GUIDE.md`, `iba/docs/ps tools worksheet.xlsx` (`Collection-Build` and `Engagement` tabs), `outputs/escalation/2477-evidence-report-plan.md`, `outputs/escalation/2479-phrases-as-members-plan.md`.
- Outputs: `_analytics/surfaces/exports/collection-evidence-search-v7-20261111.md` and `.xlsx`, `_analytics/surfaces/exports/verse-evidence-mat-11-29-v1-20261111.md` and `.xlsx`, `_analytics/surfaces/exports/engagement-search-check-20261111.md`, `_analytics/surfaces/working_files/engagement/engagement-search-pull-missing-20261111.json`, `_analytics/surfaces/working_files/engagement/engagement-search-assessment-phrases-20261111.json`; earlier evidence files archived under `_analytics/surfaces/exports/archive/`.
- Config: `cfg_setting` `collection.member_tiers`, `collection.evidence_catalogue_stages`, `collection.evidence_text_chars`; `cfg_step` descriptions; `cfg_utility` rows; the manifest and config report rebuilt.
- Data: 30 `ib_observation` rows (stage engagement) with 45 `ib_node` rows for the phrase rows of `search`; 21 `surface_term` groups set by the engagement group rule.
- Records: `Logs/compliance/COMPLIANCE-20261111-ec78b300.md`, `iba/app/reports/session-close-v347-20261111.md`.

## 4. Decisions

- Researcher: build #2477 as a reading plus an Excel workbook, the Markdown fixing the problems found — recorded in `outputs/escalation/2477-evidence-report-plan.md` and #2477 v4.
- Researcher: phrases are members unless a repeat of another member, and the other phrases get their own observations and engagement — recorded in #2479 v3.
- Researcher: approved the plan for phrases as members, row-level reading — recorded in #2479 v5.
- Researcher: accept the phrases build and keep the six group-other phrases linked (option A) — recorded in #2479 v7 and #2482 v3.
- Claude, own design choice inside the approved plan: a separate `collection.member_tiers` so `attach_phrases` never matches phrases against phrases — recorded in `cfg_setting` `collection.member_tiers` and `iba/app/BUILD.md` section 492.
- Claude, self-correctable: two wrong test assertions corrected (the export has no row id; the attach preview was not empty) — recorded in `iba/app/tools/temp_2479_phrase_members_test_run.py` and #2479 v6.
- Claude, self-correctable: the worksheet columns brought in line with the scripts (`-ByType` removed, `-Missing` added) — recorded in `iba/docs/ps tools worksheet.xlsx`, #2478 v3 and #2480 v3.
- Claude, self-correctable: the engagement of the 45 phrase rows recorded as inferential observations per the approved plan — recorded in `ib_observation` and `ib_node` and #2479 v6.

## 5. Open items

- #2477: the rebuilt report awaits the researcher's acceptance (researcher).
- #2481: engagement of the phrase rows of the other 37 collections, 1,862 distinct rows, on hold for the researcher to schedule (Claude, when scheduled).
- #2463: collection search analysis, in progress (Claude, after #2477).
- #2448: parked.
- Surface-Resolve `-Action Run -Check` would change 9 surfaces after the group step; not examined (carried in #2481).

## 6. Git

- Branch: main.
- Commit: 2f4086b3 `session 20261111: collection evidence report as a Markdown reading plus a 20-sheet Excel workbook (#2477), phrases are members of their collections with engagement and Pull -Missing (#2479), ...` (60 files).
- Push: `To https://github.com/lcilliers/Bible_Projects.git   395d0aaf..2f4086b3  main -> main`.
- Final commit: this log's git section, committed alone as `session 20261111: session log git confirmation`.
