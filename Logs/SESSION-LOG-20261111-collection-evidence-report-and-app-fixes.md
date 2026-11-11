# Session log 2026-11-11 — collection evidence report, verse report, Strong's entries, app fixes (Developer Mode)

Session id: 8ca87189-3e9b-46d2-9a09-37aaa09ed647 (started 2026-11-11 05:28 UTC, closed 2026-11-11).

## 1. Scope

Developer Mode session opened on #2463 (collection search analysis). Built the collection evidence report (`Collection-Build.ps1 -Action Evidence`), extended it to verses (`-Verse`), two layouts (`-ByType`), Scripture order, nodes shown with their observation and a Strong's entry for each code; cleaned up the config errors of #2465; fixed SC4a (#2462) and SC16 (#2458); investigated #2457; prepared #2456, #2457, #2387 for approval. Ended on the researcher's instruction to close every escalation except #2376, #2377, #2448 and #2463.

## 2. Escalations

- #2463: read and left in progress (its first report, #2464, was built).
- #2464: updated (v2 in progress, v3 handed over, v4 completed on the researcher's approval).
- #2465: resolved (self_correctable, v2): enum values registered, `engagementask` retired.
- #2466: raised (nodes on deleted observations; nodes without an occurrence), withdrawn on the researcher's instruction.
- #2467: raised (verse report, orderings), updated, completed (v3).
- #2468: a run_error of this session (a locked file), resolved self_correctable (v2).
- #2469: raised (nodes in context, Strong's entries), completed (v4).
- #2470: a code-raised config finding, withdrawn on the researcher's instruction.
- #2471: raised (verse table gaps), withdrawn on the researcher's instruction.
- #2472, #2473, #2474: raised as the three parts of #2387, withdrawn on the researcher's instruction.
- #2462: updated (v2 to v5), design handed over, completed (v6).
- #2458: updated (v2 to v5), design handed over, completed (v6).
- #2457, #2456, #2387: prepared for approval (v2, v3), completed on the researcher's approval (v4).
- #2460: updated (v6 plan handed over), closed (v7) on the researcher's instruction; the plan was not built.
- #2412: withdrawn (v31) on the researcher's instruction.
- Read and left untouched: #2448, #2376, #2377.

## 3. Files

- Code: `iba/app/lib/collectionevidence.py` (new), `iba/app/handlers/collectionbuild.py`, `iba/app/ps/Collection-Build.ps1`, `iba/app/lib/sessionwindow.py`, `iba/app/handlers/session_close.py`.
- Docs: `iba/app/BUILD.md` (sections 482 to 487), `iba/app/USER-GUIDE.md` (8.14 and the SC4 and SC16 rows), `iba/docs/ps tools worksheet.xlsx` (Collection-Build tab).
- Migrations (config writes through apply_logged, all in `iba/app/migration/archive/`): `collection_evidence_2464_v1_20261111.py`, `collection_evidence_verse_2467_v1_20261111.py`, `collection_evidence_strongs_2469_v1_20261111.py`, `cfg_cleanup_2465_v1_20261111.py`, `cfg_sc4a_own_log_2462_v1_20261111.py`, `cfg_sc16_hook_refusal_2458_v1_20261111.py`.
- Retired to archive: `iba/app/lib/archive/engagementask.py`, `iba/app/tools/archive/temp_2412_triage_test.py`.
- Reports: `outputs/reports/collection-evidence/` (evidence reports and CSVs of discord, console, search by type, and a verse list in both layouts).
- Plans and findings: `outputs/escalation/2464-collection-evidence-report-plan-v1-20261111.md`, `outputs/escalation/2467-evidence-report-by-verse-plan-v1-20261111.md`, `outputs/escalation/2469-evidence-report-nodes-in-context-strongs-plan-v1-20261111.md`, `outputs/escalation/2457-stored-verse-counts-vs-step-findings-v1-20261111.md`, `outputs/escalation/2458-sc16-false-failures-findings-and-design-v1-20261111.md`, `outputs/escalation/2462-sc4a-other-sessions-logs-findings-and-design-v1-20261111.md`, `outputs/escalation/2460-engagement-reason-and-test-per-verse-plan-v1-20261111.md`.
- `Logs/compliance/COMPLIANCE-20261111-8ca87189.md` and the session-close reports in `iba/app/reports/`.

## 4. Decisions

- Researcher: build #2464, the evidence report of a collection, approved on the plan. Recorded in iba/app/BUILD.md section 482 and #2464 v4.
- Researcher: a switch for a verse or list of verses, organised by verse in Scripture order, two orderings (by word then type, or by type), build it. Recorded in iba/app/BUILD.md section 483.
- Researcher: show nodes with their observation and the full Strong's data; approved on the plan. Recorded in iba/app/BUILD.md section 484 and #2469 v4.
- Researcher: 'cleanup 2465'. Recorded in #2465 v2 and iba/app/BUILD.md section 485.
- Researcher: SC4a option A (a session log is checked only when it names this session). Recorded in iba/app/BUILD.md section 486 and #2462 v6.
- Researcher: SC16 option A (a hook refusal is not a failure; a script is attributed only when run). Recorded in iba/app/BUILD.md section 487 and #2458 v6.
- Researcher: 2457 and 2458 to be investigated, not left. Recorded in #2457 v2 and #2458 v2.
- Researcher: #2457, #2456 and #2387 approved (option A, the three parts of #2387 carried), #2460 'approved'. Recorded in #2457 v4, #2456 v4, #2387 v4 and #2460 v5.
- Researcher: close every escalation except #2376, #2377, #2448 and #2463 (remnants or Claude's own generated work). Recorded in #2412 v31 and #2460 v7.
- Claude, self-correctable: #2468 (a locked previous report file made the run crash) fixed so the run refuses and writes nothing. Recorded in #2468 v2 and iba/app/BUILD.md section 483.

## 5. Open items

- #2463 (Claude): the next analysis step is the researcher's to name; also not done from this session: the default-layout `search` evidence report (its previous CSV was open in another program) and `Manifest-Rebuild.ps1` for the new report files.
- #2448 (Claude): on hold, untouched this session.

## 6. Git

Branch: main. Commit 2212e826b5e831480fda6aa3c0c3c039eccf21b4 (session 20261111: collection evidence report (-Verse, -ByType, nodes in context, Strong's entries), SC4a and SC16 fixes, #2465 cleanup, escalations closed on instruction, session log, compliance file, close reports).

Push output: `To https://github.com/lcilliers/Bible_Projects.git   72fa544f..2212e826  main -> main`.

Not staged: Logs/compliance/COMPLIANCE-20261111-bb3e2920.md, the compliance file of another session (left untracked by the previous close as well).
