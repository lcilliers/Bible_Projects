# Session log 2026-11-13: the re-read of the prior study documents, and cluster and subgroup retired from nodes and observations

Session 92d853ef-815a-4baa-9714-7fb3744fb09d (Developer Mode, started by session local_98402aa4-bb7b-45f0-8183-b6b9a26d806b). Compliance file `Logs/compliance/COMPLIANCE-20261113-92d853ef.md`.

## 1. Scope

Task from the starting session: design, for the researcher's decision, the re-read of the prior study documents into proper observations (#2484 ruling of 2026-11-13). It became: the design (v1 to v4), two sample drafts as JSON, the processing of those two documents into the observation record (a loader, a live run), roles for 29 live fear findings, the requirement for the collection reading recorded on its own escalation, the closing of #2484, and then corrective action on #2493, #2494 and #2495 (glossary, behaviours, and cluster and subgroup retired from the node and observation code and config). The researcher closed #2494 and #2495 and asked for the two sessions of this group to be closed.

## 2. Escalations

- #2498 raised (re-read of the prior documents), updated v1 to v11; closed (completed) by the researcher.
- #2484 updated v19 to v21; closed as completed on the researcher's instruction; its remaining classes handed to #2448.
- #2448 updated v11 to v14 (the collection-reading requirement, the classes from #2484, the cluster-reading rules that retire with the collection Open, the researcher's words recorded verbatim); stays on hold.
- #2463 updated v15 (pointer to the requirement on #2448).
- #2493 resolved (stale: enum values already added). #2496, #2497 and #2499 resolved (folder_purpose rows exist). #2500 and #2501 raised by validate after my own changes, resolved the same session.
- #2494 updated v2 to v6, closed by the researcher. #2495 updated v2 to v3, closed by the researcher.

## 3. Files

- Design and drafts: `outputs/escalation/2498-prior-reread-by-collection-design-v4-20261113.md` (v1 to v3 in `outputs/escalation/archive/`), `outputs/escalation/2498-pilot-sample-m18-group-g-reading-draft-v1-20261113.json`, `outputs/escalation/2498-pilot-sample-fear-ledger-unit2-draft-v1-20261113.json`, `outputs/escalation/2498-pilot-processing-plan-v1-20261113.json`, `outputs/escalation/2498-pilot-load-v1-20261113.json`, `outputs/escalation/2498-pilot-rehearsal-readback-v1-20261113.md`, `outputs/escalation/2498-fear-roles-load-v1-20261113.json`, `outputs/escalation/2498-fear-roles-proposal-v1-20261113.md`, `outputs/escalation/2495-retire-cluster-and-subgroup-from-nodes-and-observations-design-v1-20261113.md`.
- New code: `iba/app/lib/draftapply.py`, `iba/app/handlers/draftapply.py`, `iba/app/ps/Draft-Apply.ps1`, migrations in `iba/app/migration/archive/` (`draft_apply_config_2498_v1_20261113.py`, `ib_node_cluster_nullable_2495_v1_20261113.py`, `node_observation_cluster_retire_2495_v1_20261113.py`, `node_observation_cluster_retire_2495_v2_20261113.py`).
- Changed code: `iba/app/lib/observationrecord.py`, `iba/app/lib/reading.py`, `iba/app/lib/engagement.py`, `iba/app/lib/cfgquality.py`, `iba/app/tools/temp_2320_analysis_phase_1_test_run.py`.
- Moved to `archive/` (retired): the capture, node-sweep and subgroup-map scripts, handlers and libraries (BUILD 527 names each).
- Documents: `iba/app/USER-GUIDE.md` (7.1, 7.5, 8.2), `iba/app/BUILD.md` (524 to 527), `iba/docs/ps tools worksheet.xlsx` (tabs for `Node-Check` and `Draft-Apply`, retired scripts marked).
- Database (live, each after a named snapshot): 35 observations enriched in place, 4 added, 97 nodes added, 12 roles corrected (pilot); 132 roles set on the 29 fear findings; `ib_node.cluster_code` made nullable; cfg_* rows (step, grants, method rules, retirement of rules 66, 117, 118, enforcement text of 121, 130, 131); 14 glossary entries amended and approved in `database/bible_research.db` through `Prose.ps1`.
- Reports and records: `_analytics/reading-tools/prior-reread/` (reports of the draft check and apply), `Workflow/Programme/prose-edits/prose-edit-word-index-and-glossary-chapter-1-v1-20261113.md`.

## 4. Decisions

Researcher's own:
- The re-read enriches, corrects and adds; it does not replace; collection gaps are listed (2026-11-13): recorded in `outputs/escalation/2498-prior-reread-by-collection-design-v4-20261113.md` and #2448 v14.
- The documents' work is folded into the collection reading, read only for the verses in scope, no bulk re-read before it: `outputs/escalation/2498-prior-reread-by-collection-design-v4-20261113.md` and #2448 v12.
- Process the two prepared drafts (Q1), run them live, set the fear roles, apply live: BUILD entries 524 and 525 in `iba/app/BUILD.md`.
- Close #2484 and hand its remaining classes to the collection reading: #2484 v21 and #2448 v13.
- Cluster and subgroup retired from nodes and observations, applied rather than handed back; glossary and behaviours updated rather than handed back: BUILD entries 526 and 527 in `iba/app/BUILD.md` and cfg_change_detail runs `DEVMODE-2495-RETIRE-CLUSTER-SUBGROUP-20261113`.

Claude's own (self-correctable or engineering choices, recorded):
- A loader changes an existing observation's text only (its kind and basis stay): `iba/app/lib/draftapply.py` and BUILD 524.
- A node on an out-of-scope verse, or with no collection to carry it, is not written: `iba/app/lib/draftapply.py` and the read-back `outputs/escalation/2498-pilot-rehearsal-readback-v1-20261113.md`.
- `ib_node.cluster_code` nullable (not kept NOT NULL), the node sweep, old capture tool and subgroup map retired whole: `iba/app/migration/archive/ib_node_cluster_nullable_2495_v1_20261113.py` and BUILD 527.
- Behaviour rules 119 and 120 and RO13, RM-03, RO8 stay until the collection Open exists (`Reading.ps1 -Step Open` has no other way to open a reading): #2448 v12.
- `iba/app/lib/narrativeregister.py` exempted from the hand-rolled versioning check (the version is the database's): `iba/app/lib/cfgquality.py` and BUILD 527.
- The 14 programme-glossary entries amended and approved; `role` (contentious) left draft, the researcher's to settle: recorded in `iba/app/BUILD.md` entry 527 and `outputs/configs/CONFIG-REPORT.md`.
- Eccl 12:3 set standalone (a judgement call) and node 80340 left for the node cleanup: `outputs/escalation/2498-fear-roles-proposal-v1-20261113.md` and #2448 v13.

## 5. Open items

- #2448: the collection reading (Observe sheet with the documents' lines and the gap list, `collection_id` on new nodes, per-line accounting, the cluster-reading rules that retire with the collection Open, the validation flag, the classes handed over from the closed node work, node 80340, the Eccl 12:3 judgement call, and the contentious glossary entry `role`, draft, the researcher's to settle under B:126). On hold, for the researcher.
- #2463: the collection (search) analysis, Claude.
- #2486: cross-linking every claim to its collection, Claude (needs a design first, B:105).

## 6. Git

_(written after the first commit)_
