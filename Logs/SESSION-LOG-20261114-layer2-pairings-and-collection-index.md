# Session log 2026-11-14: layer 2 pairings in the evidence report, and the collection subgroup index

Session id: `296c9026-f9d4-49cf-8904-f04be58876e3` (Developer Mode, started 2026-11-14T04:14:57Z).

## 1. Scope

The researcher's layered claim reading (layer 1: what the words of a collection do for the inner being; layer 2: what the words that live with them in their verses do) was compared with the current claim reading and #2486; the thought evidence report was found to lack the layer 2 base data and was extended (verse view, typed pairings with distance, side and qualifier candidates, counts at each level); the concept chain and the collections data structure were read; the researcher decided to leave the concept rows alone and approved a new index of collection, surface and subgroup, which was built, applied live (3,437 unplaced rows) and tested. The researcher closes the session and restarts tomorrow morning to verify the new reports.

## 2. Escalations

- **#2463** (Collection (search) analysis): v16 to v34, researcher instructions and answers recorded verbatim; the comparison, gap, pairing, concept, collections-structure, scope-rules and index-design papers recorded; session-close comment (v34). In progress, assigned to Claude.
- **#2502** (Evidence report: layer 2 pairing sheets): raised and built; v3. In progress.
- **#2503** (Collection subgroup index: build): raised and built, applied live; v3. In progress.
- **#2504** (No stated procedure for adding a data table): raised, on hold (design for the researcher).
- **#2448** (Record: final reading is based on collections): on hold, assigned to Claude, acknowledged at every Stop-hook check, not touched.
- **#2486** read for the comparison; not changed.

## 3. Files

- Code: `iba/app/lib/collectionevidence.py`, `iba/app/lib/collectionevidencereport.py`, `iba/app/lib/collectionindex.py` (new), `iba/app/handlers/collectionbuild.py`, `iba/app/ps/Collection-Build.ps1`, `iba/docs/ps tools worksheet.xlsx` (tab Collection-Build).
- Migrations: `iba/app/migration/archive/collection_evidence_pairs_2502_v1_20261114.py`, `iba/app/migration/archive/collection_subgroup_index_2503_v1_20261114.py`.
- Tests: `iba/app/tools/temp_2502_evidence_pairs_test_run.py`, `iba/app/tools/temp_2503_collection_index_test_run.py`.
- Docs: `iba/app/BUILD.md` (entries 528 and 529), `iba/app/USER-GUIDE.md` (Evidence pairings, collection index and subgroups).
- Reports: `_analytics/surfaces/exports/collection-evidence-thought-v3-20261114.md` and `.xlsx` (v1 and v2 archived), `_analytics/surfaces/exports/collection-index-check-v1-20261114.md`.
- Working papers in `outputs/escalation/`: `2463-layered-vs-current-claim-reading-comparison-v4-20261114.md`, `2463-scope-rules-b119-b120-draft-v2-20261114.md`, `2463-layer-2-foundation-gap-v2-20261114.md`, `2463-pairing-meaning-questions-and-illustration-v1-20261114.md`, `2463-concept-level-in-the-database-v1-20261114.md`, `2463-collections-data-structure-v1-20261114.md`, `2463-collection-subgroup-index-design-v1-20261114.md`; superseded versions and the unused `2463-concept-rows-destroy-and-reform-plan-v1-20261114.md` are in `outputs/escalation/archive/`.
- Database (`iba/app/db/iba.db`, not in git): `cfg_setting` `collection.evidence_pairs` and `collection.index_check_name`, cfg rows for the two new tables and three steps, tables `collection_subgroup` and `collection_subgroup_surface` (3,437 index rows); rollback snapshots `pre-2502`, `pre-2502-collection-evidence-pairs`, `pre-2503-collection-subgroup-index` in `iba/app/db/snapshots/kept/`.
- Records: `Logs/compliance/COMPLIANCE-20261114-296c9026.md`, this log, the close report, the manifest v22, the config report v784.

## 4. Decisions

Researcher's own:
- The claim reading is built in layers, each ending in observations with nodes; lexical work and claims readings do not run concurrently (recorded in #2463 v16 and v20; `outputs/escalation/2463-layered-vs-current-claim-reading-comparison-v4-20261114.md`).
- Conflicts (a) to (e) of the first comparison are not conflicts; "B120" meant B:130; B:120 is no longer active or is to be modified for collections (#2463 v18 and v20; `outputs/escalation/2463-scope-rules-b119-b120-draft-v2-20261114.md`).
- Faces are lexical work; what they do for the inner being is layer 2 (#2463 v22; `outputs/escalation/2463-layered-vs-current-claim-reading-comparison-v4-20261114.md`).
- Update the reports first so the data can be dissected; qualifiers are a critical part of pairs (#2463 v26 and `iba/app/BUILD.md` entry 528).
- The analysis must be at concept level (word groupings), asking what each pairing means individually and collectively (#2463 v28; `outputs/escalation/2463-pairing-meaning-questions-and-illustration-v1-20261114.md`).
- Leave the concepts alone; create a new index of collection, surface and subgroup; "Approve, build it" with the recommendations of the design (#2503 v1; `outputs/escalation/2463-collection-subgroup-index-design-v1-20261114.md`; `iba/app/BUILD.md` entry 529).
- Close the session and verify the new reports tomorrow (#2463 v34).

Claude, self-correctable (fixed and recorded):
- Text starting with `=` was stored as a formula in the workbook (the Excel repair the researcher reported); fixed in `iba/app/lib/collectionevidencereport.py` (`iba/app/BUILD.md` entry 528).
- A misreading of RG-09 (face work against the layers) and one wrong adjacency statement in the pairing paper were corrected in `outputs/escalation/2463-layered-vs-current-claim-reading-comparison-v4-20261114.md` and `outputs/escalation/2463-pairing-meaning-questions-and-illustration-v1-20261114.md`; the not_this_sense count was corrected in `outputs/escalation/2463-concept-level-in-the-database-v1-20261114.md` (#2463 v30).
- The test column letter of the #2502 test was corrected after the #2503 change (`iba/app/tools/temp_2502_evidence_pairs_test_run.py`).

## 5. Open items

- #2463: the B:119 and B:120 rewrite for collections (four decisions in `outputs/escalation/2463-scope-rules-b119-b120-draft-v2-20261114.md`), the third rule (lexical and claims readings separate), the blur allowance and RG-09 wording, capturing the researcher's answers as rules (B:31), points f, g and i of the comparison, the pairing paper's four decisions (group source, clause boundary, verse profile, build order); the layer 1 placement of the thought surfaces in subgroups on the researcher's instruction; verify the thought report v3 (assigned to the researcher's review tomorrow).
- #2502 and #2503: awaiting the researcher's review of the reports.
- #2503: the 274 live links flagged `shared` with no second live link (`_analytics/surfaces/exports/collection-index-check-v1-20261114.md`), not changed.
- #2504: no stated procedure for adding a data table (on hold).
- #2448: on hold, assigned to Claude; the reading by collections depends on the layer 1 decisions above.

## 6. Git

Branch `main`. First commit `21fee662` ("session 20261114: layer 2 pairings in the evidence report (#2502), collection subgroup index (#2503), claim reading comparison and working papers (#2463), close report, session log, compliance"). Push output: `To https://github.com/lcilliers/Bible_Projects.git` / `4cda524f..21fee662  main -> main`.
