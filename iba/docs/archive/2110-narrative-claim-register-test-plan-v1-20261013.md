# #2110 Narrative claim register: test plan (v1)

**Date:** 2026-10-13 · **Escalation:** #2110 · **Author:** Claude Code · **Status:** written, not run. Results are filled in as each build step is run.
**Specification (approved 2026-10-13):** `_analytics/essay/spirit_soul_body/wa-essay-narrative-record-db-specification-v1-20261013.md` (round 5). Section numbers below (§) refer to it.
**Researcher, chat 2026-10-13 (verbatim):** *"approve #2110, proceed with the test plan"*.
**Rule:** `governance.module_utility_test_plan`. Every meaningful action, parameter and option combination is covered. The plan is kept current in the same unit of work as any change to the tool. The actual results go into #2110's resolution.

---

## 0. How the tests are run

- **Developer mode.** Steps 1 to 6 run against a **copy** of iba.db (`iba/app/db/iba-2110-test.db`, made fresh at the start of each run and deleted after). Nothing touches the live iba.db until step 7, and then only after you approve the preview.
- **Fixtures** (built in step 2, kept for re-runs). The repo has no test-fixture folder yet; the proposed home is `iba/app/validation/fixtures/2110/`, **to be confirmed by the researcher before step 2**:
  - `chapters/`: two small test chapters, each in three versions, holding:
    - a claim told in both chapters;
    - a passage that tells two claims;
    - a heading renamed between versions;
    - a passage moved from one chapter to the other;
    - a passage removed;
    - a chapter opening with no heading.
  - `register/`: a three-version cut-down claim register, with:
    - four original claims, one of them split-verdict;
    - two dated sections in different table shapes (**Where · Before · After · Kind** and **Section · Added or changed · Verdict**);
    - one in-place edit to an original claim between versions.
  - `update-*.json`: weave records, good and bad (§5).
- **Live data is read-only** in steps 1 to 6: the 33 chapter files, the 373 archives and the 51 register versions are only read.
- A result is **Pass** only with the evidence written beside it (a count, the message, the row). "Ran without error" is not a result.

---

## 1. Config (build step 1)

| # | Check | Expected | Result |
|---|---|---|---|
| 1.1 | `cfg_table` read-back | 11 rows, database `iba`, category `data`: `narrative_chapter`, `_section`, `_claim`, `_claim_source`, `_passage`, `_claim_telling`, `_update`, `_update_ref`, `_claim_change`, `_citation`, `_index_note` | |
| 1.2 | `cfg_column` read-back | Every column in §3, with use, expectation, source `escalation #2110, specification v1`, filled_by | |
| 1.3 | `cfg_enum` read-back | `narrative_chapter_state` (4), `narrative_claim_origin` (2), `narrative_claim_verdict` (9), `narrative_claim_status` (3), `narrative_claim_source_kind` (4), `narrative_telling_kind` (3), `narrative_claim_change_kind` (10), `narrative_change_basis` (3), ref kinds (3) | |
| 1.4 | `cfg_write_grant` | The register tool may write the 11 tables; no other writer has a grant on them | |
| 1.5 | `cfg_setting` | The three published paths (§8) point outside `inner-being-narrative/`; `narrative.book_alias_map` present | |
| 1.6 | `cfg_behaviour_rule` | The §5 rule, word for word as approved, active | |
| 1.7 | `cfg_utility` | `Narrative-Register.ps1` registered | |
| 1.8 | Unregistered check (`cfgquality.find_unregistered_tables_and_columns`) | 0 after step 2 | |

## 2. Schema and history triggers (build step 2)

| # | Check | Expected | Result |
|---|---|---|---|
| 2.1 | `PRAGMA table_info` on all 11 tables | Matches `cfg_column` exactly (names, types, order, not-null, FKs) | |
| 2.2 | FKs | `narrative_claim_source.verse_id` and `narrative_citation.verse_id` → `verse.id`; NULL allowed. A non-existent `verse_id` is refused | |
| 2.3 | Unique keys | `narrative_chapter.chapter_no` unique among active rows; `narrative_claim.claim_ref` unique; one telling per (claim, passage) | |
| 2.4 | Trigger: claim | A direct `UPDATE narrative_claim SET claim_text = …` writes one `narrative_claim_change` row: kind `edited`, `claim_before` / `claim_after`, `basis = direct edit` | |
| 2.5 | Trigger: verdict | A direct verdict change writes `verdict_before` / `verdict_after`, kind `verdict changed` | |
| 2.6 | Trigger: passage | A direct `UPDATE narrative_passage SET passage_text = …` on a passage telling **two** claims writes **two** change rows, one per claim, each with `passage_before` / `passage_after` | |
| 2.7 | Trigger: telling | Inserting a telling writes `telling added`; setting it `removed` writes `telling removed` | |
| 2.8 | Trigger: no change | An `UPDATE` that sets a column to its current value writes nothing | |
| 2.9 | `in_narrative` | Follows the tellings: 1 after the first current telling, 0 when the last is removed; kept by the tool and by direct edits | |
| 2.10 | Rebuild from config | `lib/db.py:table_ddl()` generates DDL equal to the live tables, triggers included | |

## 3. Reference parser and alias map (build step 3)

| # | Input | Expected | Result |
|---|---|---|---|
| 3.1 | `1 Samuel 24:5` (full name, chapter text) | 1 row → `1Sa 24:5`, `verse_id` set | |
| 3.2 | `1Sa 24:5` (short code, register) | Same verse as 3.1 | |
| 3.3 | `2 Corinthians 1:12`; `2Co 1:12` | Both resolve to the `verse` row whose reference is `2Cor 1:12` | |
| 3.4 | `Philippians`, `Phi`, `James`, `Jam`, `1 John`, `1Jo` | Resolve through the alias map to `Phili`, `Jam`, `1Jo` | |
| 3.5 | Range `Lamentations 2:20–22` (en dash) and `Lam 2:20-22` (hyphen) | 3 rows each | |
| 3.6 | List `Deu 31:27, 29` | 2 rows | |
| 3.7 | Chain `2Sa 11:1–4; 12:9` | 5 rows; the second part keeps book 2Sa | |
| 3.8 | Across chapters `Mal 2:17–3:2` | Every verse from 2:17 to 3:2 (counted from `verse`) | |
| 3.9 | Bare follow-on `(8:12)` after `1 Corinthians 8:7` in the same passage | Takes book 1Co from the reference before it | |
| 3.10 | Bare verse `(5)` after `Ephesians 1:4` | Takes book and chapter from the reference before it | |
| 3.11 | Whole chapter `Isaiah 1` | Recorded as written, kind whole chapter, `verse_id` NULL, listed | |
| 3.12 | Single-chapter book `Jude 6`, `Jude 8–9` | 1 and 2 rows | |
| 3.13 | A verse with no `verse` row | Kept, `verse_id` NULL, on the unresolved list | |
| 3.14 | Unparseable text (e.g. `cf. above`) | Not a row; on the unresolved list with its passage | |
| 3.15 | Quoted or referred | `quoted = 1` where the passage quotes the verse's words, 0 where it only cites it | |

## 4. Tool actions and refusals (build step 4)

**Every refusal is tested for "nothing written":** the row counts of all 11 tables are the same before and after.

| # | Action and options | Expected | Result |
|---|---|---|---|
| 4.1 | `AddClaim -Text -BeyondText -Source "verse:1Sa 24:5" -Source "verse:Job 27:6"` | Claim row, `origin = narrative`, printed `C-n`; 2 source rows; `in_narrative = 0` (no telling yet); change row `claim created` | |
| 4.2 | `AddClaim` with `-Source "lexical:ḥêq, bosom, lap"`, `"study file:<path>"`, `"science:<ref>"` | One source row per kind | |
| 4.3 | `AddClaim` with no `-BeyondText` | Refused: a claim must say what goes beyond its sources | |
| 4.4 | `AddClaim` with no source | Refused | |
| 4.5 | `AddClaim` with an unknown source kind | Refused, naming the cfg_enum | |
| 4.6 | `Edit -Claim C-n -Text` | Change row with `claim_before` / `claim_after` | |
| 4.7 | `Edit -Claim 2-5 -Verdict Restated` (original claim) | `verdict_before` / `verdict_after` | |
| 4.8 | `Edit -Verdict Unknown` | Refused | |
| 4.9 | `Edit -Claim` that does not exist | Refused, naming the ref | |
| 4.10 | `Tell -Claim C-n -Chapter X -Passage "<opening words>" -Kind "in full"` | Telling row; `in_narrative = 1`; change row `telling added` | |
| 4.11 | `Tell -Kind "in part" -Part "<what part>"` | `part_told` stored | |
| 4.12 | `Tell -Kind "in part"` with no `-Part` | Refused | |
| 4.13 | `Tell -Kind pointer` | Telling of kind pointer; a claim told **only** by pointers keeps `in_narrative = 0` | |
| 4.14 | `Tell` with opening words that match no passage, or two passages | Refused, naming the matches | |
| 4.15 | `Tell` to a chapter or section that does not exist | Refused | |
| 4.16 | `Tell` the same claim to the same passage twice | Refused (one telling per pair) | |
| 4.17 | One claim told in three passages in two chapters (the K10 case) | 3 tellings; `Find -ToldInMoreThanOne` lists it | |
| 4.18 | One passage telling three claims (the 10.12 opening case) | 3 tellings; a passage edit writes 3 change rows (with 2.6) | |
| 4.19 | `Untell` the last current telling | `in_narrative = 0`; change row `telling removed` | |
| 4.20 | `Withdraw -Claim` | `status = withdrawn`, row kept, history kept; tellings kept as they are | |
| 4.21 | `EditNote` / `EditChapter` / `EditSection` | Each writes its row; chapter and section edits are logged | |
| 4.22 | `EditChapter -ChapterNo` (renumber, the #1936 case) | Number changes; every claim and passage keeps its link; change row `renumbered` | |
| 4.23 | Chapter **split** (a new chapter takes some sections) | Moved passages keep their rows and claims; each move logged `passage moved` with the chapter before | |
| 4.24 | Chapter **merge** (one chapter retired into another) | Old row `inactive = 1`; passages moved and logged; nothing orphaned | |
| 4.25 | Section renamed | New section row with `renamed_from_id`; passages follow | |
| 4.26 | `in_narrative` across all of 4.10–4.24 | Always equals "has at least one current telling of kind in full or in part" | |

### 4A. `Record` (§5.1)

| # | Case | Expected | Result |
|---|---|---|---|
| 4A.1 | Good record: one update, 2 refs (escalation, thread), 1 new claim told in 2 passages, 1 restated claim | Everything written in one transaction; files regenerated | |
| 4A.2 | Chapter version in the record ≠ the file on disk | Refused; nothing written | |
| 4A.3 | Unknown chapter, section or passage | Refused | |
| 4A.4 | Unknown claim ref | Refused | |
| 4A.5 | Unknown enum value | Refused | |
| 4A.6 | Escalation or thread that does not exist | Refused | |
| 4A.7 | An unresolved verse reference | Written, with the reference listed in the output | |
| 4A.8 | **Unaccounted change:** the chapter compare finds a changed passage that tells a claim, and the record does not mention it | Listed in the output (not refused) | |
| 4A.9 | **Other tellings:** the record changes one passage telling a claim that is also told elsewhere | The other passages are listed for a consistency read | |
| 4A.10 | The same record run twice | The second run is refused as already recorded; nothing doubled | |
| 4A.11 | A record failing half way (forced error after the first insert) | Rolled back; counts unchanged | |

## 5. Find, History, Check, Export (build step 5)

| # | Case | Expected | Result |
|---|---|---|---|
| 5.1 | `Find -Verse "1Sa 24:5"` and `-Verse "1 Samuel 24:5"` | The same result: the claims resting on it, and every passage citing it | |
| 5.2 | `Find -Chapter`, `-Section`, `-Claim`, `-Text`, `-Verdict` | Each returns the expected rows on the fixtures | |
| 5.3 | `Find -Escalation 1998`, `-Thread OT-29` | The updates carrying the ref, and their changes | |
| 5.4 | `Find -NotInNarrative` | Exactly the claims with `in_narrative = 0` | |
| 5.5 | `Find -ToldInMoreThanOne` | Exactly the claims with 2 or more current tellings | |
| 5.6 | Two filters together (e.g. `-Chapter X -Verdict Held`) | The intersection | |
| 5.7 | `History -Claim` | Every change to the claim and to each passage telling it, oldest first, with before and after | |
| 5.8 | `Check`, all well | No findings | |
| 5.9 | `Check`: a passage's opening words no longer in its chapter | Reported | |
| 5.10 | `Check`: the opening words now in a **different** chapter file | Reported as a move to confirm, not as a loss | |
| 5.11 | `Check`: a current claim with no current telling of kind in full or in part | Reported | |
| 5.12 | `Check`: chapter `current_version` ≠ the newest file on disk | Reported | |
| 5.13 | `Check` writes nothing | Counts unchanged | |
| 5.14 | `Export` | The three files written at the `cfg_setting` paths, fixed names, the "Published from iba.db" line first | |
| 5.15 | `Export` content | Register by chapter and section with each claim's other places; original claims in their tables; claims not in the narrative; the Tally **counted**. Changes newest first with passages before and after; the Structure log. Citation index in canonical order | |
| 5.16 | `Export` twice with no change | Byte-identical files | |
| 5.17 | None of the three files lands in `inner-being-narrative/` | Confirmed; a dry run of `Copy-NarrativeToLearning4Comfort.ps1` does not list them | |

## 6. Import preview: the original claims and the recorded history (build step 6)

Read-only on the live files. Writes a preview and a review list only.

| # | Check | Expected | Result |
|---|---|---|---|
| 6.1 | R1: register v1 → v51 | 50 comparisons. The 81 original claims as first recorded. Every in-place edit to an original claim found (3-9's "Corrected 2026-10-04 (#1950)" is one test case) | |
| 6.2 | Original claims | 81 rows; split verdicts (9-1, 9-5, 4-8) carried as `part_verdict`; "New ch" turned into tellings to confirm in R0 | |
| 6.3 | Tally recount | Counted from the 81; the difference from the stated 86 explained in the review list | |
| 6.4 | R2: the 53 dated sections | 53 updates. Every one of the 551 table lines either becomes a change row or is listed with a reason. The 16 table shapes each map | |
| 6.5 | Multi-chapter cells | Each split into one row per chapter, listed | |
| 6.6 | Old chapter numbers | Sections dated before 2026-10-02 mapped across the #1936 renumbering, listed | |
| 6.7 | R3: index version notes and Structure log | Every chapter version tied to an update, or listed as unexplained | |
| 6.8 | R5: imputed-readings audit and Correction section | 88 + 34 changes, each before and after | |
| 6.9 | R6: digest §4 | The 7 areas recorded | |
| 6.10 | Refs | Every escalation and thread named in the sections exists in the escalation table, or is listed | |
| 6.11 | Nothing written to iba.db | Live counts unchanged | |

## 7. Approved import and switch-over (build step 7, after you approve the preview)

| # | Check | Expected | Result |
|---|---|---|---|
| 7.1 | Backup | iba.db backed up before the import | |
| 7.2 | Import | Counts equal the approved preview | |
| 7.3 | `Check` | No findings beyond those already on the review list | |
| 7.4 | Freeze | The claim register v51 and `00-index-and-status-v1-20260930.md` moved to their `archive/` folders | |
| 7.5 | Inbox | `C:\learning4comfort\publication-inbox\the_inner_being\00-index-and-status-v1-20260930.md` removed (Q-K) | |
| 7.6 | Publish | `Export` writes the three files | |
| 7.7 | Next narrative copy | Run (or dry run) of `Copy-NarrativeToLearning4Comfort.ps1`: copies the chapter files only; the index is not copied back | |

## 8. First reading batch: the sample (build step 8)

| # | Check | Expected | Result |
|---|---|---|---|
| 8.1 | The 21 sample claims (Chapter 8; 10.12 lines 1–66) imported as approved | 21 claims; each with sources and `beyond_text` | |
| 8.2 | Tellings | K10 has 5 tellings, F6 has 6, F2 has 4; the 10.12 opening passage tells F1, F2 and F3 | |
| 8.3 | Correlation | Each matched to the register where it can be; the rest listed | |
| 8.4 | R4 history for the batch's passages | Each passage's first version found; each later change with the passage before and after | |

## 9. Reading batches, chapter by chapter (build step 9)

Run for each batch, in the approved order (10.1, 10.12, 10.13, Ch 4, Ch 11, then the rest).

| # | Check | Expected | Result |
|---|---|---|---|
| 9.1 | Prepared material | For the chapter: passages with citations, original claims naming it, its register change rows, and the other chapters citing the same verses | |
| 9.2 | Batch file for review | Every claim with its wording, sources, `beyond_text`, and every place it is told | |
| 9.3 | Reuse | A claim already drafted in an earlier batch is linked, not drafted again | |
| 9.4 | Correlation lists | In both / narrative only / register only, for the batch | |
| 9.5 | Discrepancy list | Each entry gives both sides word for word, with chapter, section and version; the narrative is not changed | |
| 9.6 | After import | `Check` clean; the batch's claims all have at least one telling or are listed | |
| 9.7 | End of all batches | Every chapter read; every original claim and every register change row correlated or listed | |

## 10. Documents and the live test (build step 10)

| # | Check | Expected | Result |
|---|---|---|---|
| 10.1 | `GOVERNANCE.md` §94, `BUILD.md`, `USER-GUIDE.md` | Written; `BUILD.md` carries tracking id #2110 | |
| 10.2 | `CLAUDE.md` | The strand rules no longer say a strand updates the claim register file | |
| 10.3 | Excel tool worksheet | `Narrative-Register.ps1` rows present (`find_escalation_worksheet_drift` / ps worksheet check clean) | |
| 10.4 | The next real weave | Recorded with `Record`; its unaccounted-change and other-tellings lists read; files regenerated | |
| 10.5 | One full session start and `/session-close` on the new path | No claim-register file edited by hand; session-close checks pass | |

---

## Results log

Filled in run by run: date, build step, cases run, pass and fail counts, defects found and their fix.
