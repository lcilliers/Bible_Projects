# Narrative claim register in iba.db: detail specification (v1, for review — round 5)

**Date:** 2026-10-13 · **Escalation:** #2110 · **Author:** Claude Code · **Status:** specification for the researcher's review, revised in place after rounds 1 to 4. **No questions remain open; for approval.** Nothing is built. No config, schema or narrative file has been changed.
**Goes with:** `wa-essay-narrative-claim-sample-v1-20261013.md` (narrative and claims, worked on Chapter 8 and the opening of 10.12).
**Precedent:** the open threads register, moved into the escalation table under #2000 (`_analytics/cross-cluster-web/open-threads-table-proposal-v3-20261012.md`; GOVERNANCE.md §93).

---

## 0. Instructions and rulings

**Researcher, chat 2026-10-13 (verbatim):** *"should the claims register be properly recorded in the database instead of a md file that is increasingly difficult to search and control and get specific updates."*

**Researcher, chat 2026-10-13 (verbatim):** *"proceed with #2110. The DB is IBA.db. prepare a detail specification for review"*.

### Round 1 (researcher, chat 2026-10-13, verbatim)

> *"the claims register should include a) the original opening claims b) every additional new claim (I think there is a separate document for it ) c) pre and post of every update / change to the claim. every row should be cross referenced to the chapter and section in the chapter. other columns to be derived from the current claims register."*
>
> *"Q2 the claims register table should include the full history in as far as it is possible to reconstruct it from the filed files and archives."*
>
> *"Q3 in my view the index is intrinsic in the design of the claims register, the register is by implication the index."*
>
> *"Q-A the change log seems to be a one to many relationship with the index (main claims)"*
>
> *"Q-B if the files are git controlled then one name is better - it will work more seeemlessly with the publishing site learning4comfort."*
>
> *"Q-C yes. this is the citation index by implication."*
>
> *"Q-D this does not make sense. the index cannot be static, it must be editable."*

### Round 2 (researcher, chat 2026-10-13, verbatim)

> *"Q-E yes, Q-F the information in the change log must be sufficient for me to review the impact of the change pre and post, Q-G separate files; Q-D as suggested; all claims in the narrative not in the claims file should be imported into the new claims register in this table creation process. This means the 33 narrative files must be correlated to the claims register. I am not sure what you view as a 'claim' and what not. you may need to show me the narrative for a few files and highlight what you would regard as the 'claims' in each narrative. Note that the register may have claims that will not be in the narrative, but there should be a column that clearly allows filtering claims not included."*

### Round 3 (researcher, chat 2026-10-13, verbatim)

> *"let me be clear: the narrative is the story. It is written to give context, readability, and the story of the section. it needs to read as a whole, across sections and chapters. It is not a listing of claims. Claims are the factual statements in the story that is based or derived from sources (verses in the main, but also will include science). I would imagine that if the narrative make a statement that is derived and not explicitely stated in verses that it would have correlated claims. I can also imagine that a statement may draw from several claims. I can also imagine that a claim may be narrated in different sections (e.g. the heart narration my have a section of a claim while the remainder of the claim is in the feeling section). Your S1-S3 is a good illustration that you do not have a grip on what is narrative, and what are claims. by the way - just quoting the verse is not a claim, the interpretation of the verse or verses beyond the mere text of the verse, is the actual claim."*
>
> *"only the narrative goes to learning4comfort."*
>
> *"Q-I - i can well imagine a disconnect between the claims register and the narrative - part of this migration is to update the claims register to align with the narrative and highlight any gaps or discrepancies"*

### Round 4 (researcher, chat 2026-10-13, verbatim)

> *"B1 agreed - the narrative can interpret e.g. your example as long as the underlying paragraphs - supported by claims - supports it. ; Q-J as recommended - I would not be surprised if this excercise lead to a re-organisation of the chapters, the current chapters of the narrative is not fixed, they will morph as more clusters are being read; Q-K remove it. this index is now replaced. the copy in learning4comfort can be removed."*

**What round 3 changed.** Round 2's design treated a claim as a unit of narrative text, tied to one section. That was wrong, and S1 to S3 are withdrawn. In this round:
- a **claim** is a statement derived from sources, beyond their mere text, with its own wording;
- the **narrative** is the story; it is recorded only as the passages that tell claims;
- the two are joined **many to many** (§3.5);
- the sample is rewritten on this basis.

### Where each ruling goes

| Ruling | Where it goes |
|---|---|
| Q1 iba.db | Throughout |
| (a)(b)(c) original claims, every new claim, pre and post of every change | §3.3 claims; §3.7 change log |
| Every row cross-referenced to chapter and section | §3.5: each place a claim is told carries chapter and section; §3.3 also holds the claim's main place |
| Columns from the current register | §3.3 and §3.7 map each column to the register column it comes from |
| Q2 full history, as far as it can be reconstructed | §6 |
| Q3 the register is the index | §7 |
| Q-A change log one-to-many with the claims | §3.7 |
| Q-B one fixed name per file | §8 |
| Q-C / Q-E the citation index, from the chapter text too | §3.8 |
| Q-D editable; the rule as suggested | §5 |
| Q-F the change log is enough to review the impact before and after | §3.7: the claim wording and the passage, before and after |
| Q-G separate files | §8 |
| All narrative claims imported; the 33 files correlated to the register | §6, R0 and the correlation |
| A clear filter for claims not in the narrative | §3.3, `in_narrative` |
| Narrative is the story; claims are derived statements; many to many; a quotation is not a claim | §3.3 to §3.5; the sample |
| Only the narrative goes to learning4comfort | §8: the register files sit outside the copied folder |
| Q-I the register is aligned to the narrative; gaps and discrepancies highlighted | §6, *Alignment and discrepancies* |
| B1 the narrative may interpret where the claim-supported passages under it support it | §3.3 |
| Q-J reading order as recommended; the chapters are not fixed and will change | §6 R0; §3.1 *Chapters change* |
| Q-K the old index is replaced; remove the learning4comfort copy | §8; §10 step 7 |

**On (b), "a separate document" for the new claims:** no document lists them. The new claims are recorded inside the claim register's own strand-update sections (*"the narrative's own statements this strand changed"*, v51 line 170). Three filed documents carry related material, and the reconstruction uses all three: the digest §4, the imputed-readings audit (#1921) and the M25 tracking note.

---

## 1. Facts, measured 2026-10-13

**Claim register** (`wa-essay-spirit-soul-body-claim-register-v51-20261013.md`):
- 1,405 lines, 181 KB. **Every version from v1 to v50 is in `archive/`.**
- The original claims: 81 rows in 11 chapter tables (**# · Original claim · Verdict · Evidence and restatement · New ch**). The Tally gives 15 + 8 + 37 + 15 + 11 = 86, counting part-held claims twice. The import recounts.
- The changes: 53 dated sections, 551 table lines, 16 table header shapes. The main ones are **Section · Added or changed · Verdict** (18), **Where · Before · After · Kind** (15), **Section · Was · Now · Verdict** (12), and **# · Before (verdict) · Evidence now read · Now / Proposed** (6).
- Each section also carries prose: the researcher's instruction (verbatim), sources, scripts, "Original claims changed", "Not woven", and the quote check.

**Narrative index** (`inner-being-narrative/00-index-and-status-v1-20260930.md`): 214 lines, 75 KB, edited in place; a chapters table (33 rows) and a Structure log. It names claim register v48; the current one is v51. **It is in the folder copied to learning4comfort, so it is published today** (`narrativecopy.py` copies every top-level `.md` in that folder).

**Chapter files:** 33 current files, 895 KB, with 323 section headings. 373 earlier versions are in `inner-being-narrative/archive/`.

**The sample** (Chapter 8 whole, and 10.12 lines 1–66):
- 21 claims (round 2's method gave 94 "claims" for the same text).
- K10, anger held and kept, is told in **five** places: Ch 4, Ch 8, 10.1, 10.13 and Ch 12. F6, fear's outer cause and inner reason, is told in six, and F2, one fear set in place of another, in four.
- No record today says that these places carry one claim.

**iba.db `verse`:** 29,760 rows; `reference` written `Psa 89:46`, with its own book codes (`2Cor`, `Phili`, `Jam`, `1Jo`). The narrative writes `2 Corinthians` in the chapters and `2Co` in the register, so an alias map is needed. About 1,300 verses have no row in `verse`.

---

## 2. The design in one paragraph

A **claim** is a statement derived from sources (verses, later science) that goes beyond their mere text, held in its own plain wording, with its sources. The **narrative** is the story; the register records only the **passages** of it that tell claims. A claim may be told in several passages, in different sections and chapters, each telling part of it. A passage may draw on several claims. Each claim has a **change log**: every change to its wording or verdict, and every change to a passage that tells it, before and after. The claims, by the chapters and sections that tell them, are the **index**. The verses behind the claims, and every verse cited in the story, are the **citation index**. All of it lives in iba.db and is editable there at any time. Three fixed-name files are regenerated after each change, outside the folder that goes to learning4comfort.

---

## 3. The tables (iba.db, category `data`)

Names follow the existing `escalation_thread_item` pattern. Every table has an integer surrogate `id`, `created_at` and `created_by`.

### 3.1 `narrative_chapter` — one row per chapter or sub-chapter

| Column | Use | From |
|---|---|---|
| `chapter_no` | `02`, `10.7`, `13.1` | index, # |
| `title` | *Choosing and setting direction* | chapter file heading |
| `reading_order` | order in the book | index row order |
| `file_stem` | `10-07-choosing-and-setting-direction` | index, File |
| `current_version` · `current_file` | 27 · `…-v27-20261012.md` | index, File |
| `state` | cfg_enum: `draft`, `draft + held`, `empty`, `deferred` | index, State |
| `replaces_original` · `built_from` | as the index columns | index |
| `inactive` | 1 for a retired number (old Ch 13 *Under God's anger*) | |

A renumbering (#1936 moved Ch 9 to Ch 2) changes `chapter_no` on the row and is logged. Every record keeps its link to the chapter, so the history follows the chapter, not the number.

**Chapters change (Q-J, round 4).** The researcher, verbatim: *"the current chapters of the narrative is not fixed, they will morph as more clusters are being read"*. Nothing in the design depends on the present chapters:
- a claim belongs to no chapter; it is joined to the passages that tell it;
- a chapter can be added, split, merged, renamed, renumbered or retired (`inactive`), each logged as a change;
- a passage that moves to another chapter or section keeps its row and its claims, and the move is logged (`passage moved`, with where from);
- `Check` finds a passage whose opening words now stand in a different file, and reports it as a move to confirm, not as a loss.

The reading (R0) may itself suggest a reorganisation. Any such suggestion goes on the discrepancy list for your decision; the reading does not reorganise the chapters.

### 3.2 `narrative_section` — one row per section heading in a chapter

| Column | Use |
|---|---|
| `chapter_id` | FK |
| `heading` · `level` · `parent_section_id` · `ordinal` | *Other parties*; 2–4; the section it sits in; order |
| `first_version` · `last_version` | the chapter versions in which the heading exists; `last_version` NULL while current |
| `renamed_from_id` | when a heading is renamed, the old row |

Built from the 323 current headings, and from the archives for headings that no longer exist. A chapter's opening, before any heading, has its own section row.

### 3.3 `narrative_claim` — the register: one row per claim

**What a claim is** (researcher, round 3): a factual statement in the story, based on or derived from sources, which goes **beyond the mere text** of those sources. A quotation is not a claim. The story's wording, order, transitions, the book's outline and pointers are not claims. Worked examples: the sample, §3 and §4.

**The narrative may interpret over claims (B1, round 4).** A heading or summary that generalises (10.12's "It flees", "It silences") needs no claim of its own when the passages under it, which are supported by claims, support it. Such a heading is told as part of the claim it summarises (F11 in the sample).

| Column | Use | From the current register |
|---|---|---|
| `claim_ref` | original claims keep the register's id (`I-1`, `2-5`, `K-2`); new claims are printed `C-412` from the row id | # |
| `origin` | cfg_enum: `original essay`, `narrative` | which part of the register |
| `claim_text` | **the claim in its own plain wording**, apart from how the narrative tells it (e.g. "Anger can be held and kept: it lodges, and it is cherished") | Original claim; Evidence and restatement; After / Now |
| `beyond_text` | what the claim adds to its sources, i.e. why it is a claim and not a quotation (e.g. "The verse does not use the word 'conscience'; linking it to conscience is the claim") | — (new) |
| `i_read` | 1 when the narrative marks it as the narrator's reading | Verdict ("I read marked") |
| `verdict` | cfg_enum, the register's own words: `Stands`, `Widened`, `Restated`, `Withdrawn`, `Held`, `Added`, `New`, `Removed`, `Corrected` | Verdict / Kind |
| `part_verdict` · `part_scope` | split verdicts, e.g. 9-1 "Restated (location) / **Held** (catalogue)" | Verdict |
| `original_chapter` | for original claims: `Chapter 2 — The five distinctions` | table heading |
| `original_wording` | for original claims: the original claim as the essay made it | Original claim |
| `main_chapter_id` · `main_section_id` | the place that tells the claim most fully | New ch (first named) / Where / Section |
| **`in_narrative`** | **1 if at least one current passage tells the claim; 0 if none.** The filter for claims not included: withdrawn originals, held claims, claims kept for the record. Kept up to date by the tool whenever a passage is linked or unlinked | — (new) |
| `status` | cfg_enum: `current`, `withdrawn`, `held` | |

### 3.4 `narrative_claim_source` — what a claim rests on

| Column | Use |
|---|---|
| `claim_id` | FK |
| `source_kind` | cfg_enum: `verse`, `lexical` (a Hebrew or Greek word and its renderings), `science`, `study file` (a reading, ledger or account the claim came from) |
| `verse_id` | FK → `verse.id`, for `verse`; NULL where the verse has no row |
| `ref_as_written` · `ref_normalised` | `1 Samuel 24:5` · `1Sa 24:5` (one row per verse; ranges and lists expanded) |
| `source_text` | for the other kinds: the word with its gloss, the science reference, or the file path |
| `note` | how the source bears on the claim, where it is not plain |

Science sources come later (the science chapters are deferred); the column is there so they need no new table.

### 3.5 `narrative_passage` and `narrative_claim_telling` — where a claim is told (many to many)

**`narrative_passage`**: one row per passage of the story that tells at least one claim. A passage is a paragraph or a bullet as it stands in the chapter.

| Column | Use |
|---|---|
| `chapter_id` · `section_id` | where the passage is |
| `ordinal` | its place in the section |
| `anchor_text` | its opening words, so the tool can find it in the file |
| `passage_text` | the passage as it now reads |
| `first_version` · `last_version` | the chapter versions that hold it; `last_version` NULL while current |

**`narrative_claim_telling`**: the link. One row per claim told in a passage.

| Column | Use |
|---|---|
| `claim_id` · `passage_id` | the claim and the passage |
| `kind` | cfg_enum: `in full`, `in part`, `pointer` (the passage only points to where the claim is told) |
| `part_told` | which part of the claim this passage tells (e.g. K10 in Ch 4: "anger held in the heart"; in 10.1: "as a course of feeling") |
| `status` | `current` / `removed` |

So one claim can be told in five passages (K10), and one passage can tell several claims (the opening of 10.12 tells F1, F2 and F3). Every claim is reached through its tellings by chapter and section.

### 3.6 `narrative_update` — one row per weave or recorded pass

| Column | Use |
|---|---|
| `update_date` · `title` · `strand` | `2026-10-13` · `anger (M02) pairings …` · `anger (M02)` |
| `researcher_instruction` | verbatim |
| `method` | method or rule named (e.g. rule 73) |
| `source_files` · `scripts` | one path per line |
| `claims_changed_note` · `not_woven_note` | "Original claims changed", "Not woven", "Kept out": verbatim |
| `structure_change` · `structure_reason` | filled when the book's shape changed (the Structure log) |
| `quote_parts` · `quote_failures` · `quote_note` | the quote check |
| `notes` | any other paragraph, verbatim |
| `legacy_register_version` | for imported updates, the register version that added it |

Junction **`narrative_update_ref`** (`update_id`, `kind`, `value`): `escalation` / `1998`, `thread` / `OT-29`, `thread item` / `OT-29.1`.

### 3.7 `narrative_claim_change` — the change log: many rows per claim

One row for each change to a claim, or to a passage that tells it. Each row holds enough to review the impact without opening another file (Q-F).

| Column | Use | From |
|---|---|---|
| `claim_id` | FK | |
| `passage_id` | the passage, for a change in how the claim is told; NULL for a change to the claim itself | |
| `update_id` | the update that made it; NULL for a direct edit | |
| `change_date` | ISO date | section date; register or chapter version date |
| `change_kind` | cfg_enum: `claim created`, `claim restated`, `verdict changed`, `claim withdrawn`, `telling added`, `telling changed`, `telling removed`, `passage moved`, `renumbered`, `edited` | Kind / Verdict |
| `claim_before` · `claim_after` | the claim's wording before and after | Before / After; Was / Now; register versions |
| `verdict_before` · `verdict_after` | | Before (verdict) / Now |
| `passage_before` · `passage_after` | **the full passage before and after**, as it read in the chapter | chapter archives (§6, R4) |
| `chapter_id` · `section_id` · `section_before_id` | where; and where from, for a move | Where / Section |
| `chapter_version_from` · `chapter_version_to` | e.g. 7 → 8 | "10.13 (v8)"; index version notes |
| `file_before` · `file_after` | the two chapter files, for a whole-file compare when wanted | archive |
| `note` | the verdict cell verbatim, or any remark | Verdict |
| `basis` | cfg_enum: `recorded` (stated in a filed record), `reconstructed` (found by comparing archived versions), `direct edit` | §6 |
| `provenance` | the file(s) the row came from | §6 |

A change to one passage that tells three claims writes one row for each of them, so each claim's own history is complete.

### 3.8 `narrative_citation` — the citation index (Q-C, Q-E)

Every verse cited **anywhere in the story**, by passage. With `narrative_claim_source` (§3.4) it makes the citation index: for any verse, where it is cited, and which claims rest on it.

| Column | Use |
|---|---|
| `chapter_id` · `section_id` · `passage_id` | where it is cited (`passage_id` NULL if the passage tells no claim) |
| `verse_id` | FK → `verse.id`; NULL where the verse has no row |
| `ref_as_written` · `ref_normalised` | as in §3.4 |
| `quoted` | 1 when the verse's words are quoted, 0 when it is only referred to |
| `first_version` · `last_version` | the chapter versions that cite it |

References are parsed by one shared function with the book-alias map in config (§4). A reference that cannot be parsed, or has no `verse` row, is kept with `verse_id` NULL and reported; it is never dropped.

### 3.9 `narrative_index_note` — the editable index text

The parts of today's index that are text, not tables: researcher direction, theme and frame, rules applied to the chapter text, how later work updates the narrative, source files, verse check. One row per block (`heading`, `text`, `ordinal`), editable like everything else.

---

## 4. Config first (through `Config-Maintenance.ps1 -Step Propose`)

| Config | Rows |
|---|---|
| `cfg_table` | the tables above (`narrative_chapter`, `_section`, `_claim`, `_claim_source`, `_passage`, `_claim_telling`, `_update`, `_update_ref`, `_claim_change`, `_citation`, `_index_note`), category `data` |
| `cfg_column` | every column, with use, expectation, source (`escalation #2110, specification v1`) and filled_by |
| `cfg_enum` | `narrative_chapter_state`, `narrative_claim_origin`, `narrative_claim_verdict`, `narrative_claim_status`, `narrative_claim_source_kind`, `narrative_telling_kind`, `narrative_claim_change_kind`, `narrative_change_basis`, ref kinds |
| `cfg_write_grant` | the register tool may write the tables |
| `cfg_setting` | the three published file paths (§8); `narrative.book_alias_map` |
| `cfg_behaviour_rule` | the rule in §5 |
| `cfg_utility` | registration of the tool |

---

## 5. Editing the register (Q-D)

The register **is editable at any time**, in iba.db, by you or by me. The `.md` files are the published copies, regenerated after every change.

**Every change keeps its before and after, however it is made.** SQLite triggers on `narrative_claim`, `narrative_claim_telling` and `narrative_passage` write `narrative_claim_change` rows on every update. An edit made directly in the database (e.g. in the VS Code SQLite extension) is recorded as `basis = direct edit`.

**The tool: `iba\app\ps\Narrative-Register.ps1`** (library `iba/app/lib/narrativeregister.py`):

| Action | What it does |
|---|---|
| `AddClaim -Text … -BeyondText … -Source …` | a new claim with its sources |
| `Edit -Claim C-412 -Text … / -Verdict …` | changes a claim; the trigger logs it |
| `Tell -Claim C-412 -Chapter 10.1 -Passage "<opening words>" -Kind "in part" -Part …` | links a claim to a passage that tells it; `Untell` removes the link |
| `Withdraw -Claim …` | withdraws a claim (the row stays, with its history; `in_narrative` follows its tellings) |
| `EditNote`, `EditChapter`, `EditSection` | the index text, a chapter row, a section row |
| `Record -File <update.json>` | a weave's whole update in one step (§5.1) |
| `Find -Verse / -Chapter / -Section / -Claim / -Text / -Escalation / -Thread / -Verdict / -NotInNarrative / -ToldInMoreThanOne` | read-only search |
| `History -Claim C-412` | every change to a claim and to the passages that tell it, before and after |
| `Check` | read-only: chapters, sections and passage anchors against the files on disk. Reports a passage whose opening words are no longer in its chapter, and a claim with no current telling that is still marked current |
| `Export` | regenerates the three files |

**Behaviour rule (approved as suggested, round 2):** *"The narrative claim register is kept in iba.db. It is edited there, through `Narrative-Register.ps1` or directly, and every change keeps its before and after. The register file is the published copy, regenerated from the database after each change; an edit made only in that file is not kept."*

### 5.1 How a weave records itself

The weave's chapter-file script is unchanged. The second script that edits the register and the index today (e.g. `m02-pairing-gaps-records-update-v1-20261013.py`) is replaced by a JSON file beside the weave: the update header; the claims created or changed, with their sources; and the tellings added, changed or removed, with the passages before and after. Then:

```
iba\app\ps\Narrative-Register.ps1 -Action Record -File "<path to the JSON>"
```

**Record also compares** the chapter versions before and after the weave, passage by passage, and lists:
- every changed passage that tells a claim, where the JSON does not account for the change;
- every claim told elsewhere in the narrative that a changed passage tells too, so that the other tellings can be read for consistency (the K10 case: one claim, five places).

**Refused, with the reason, when:** a chapter, section or passage does not exist; the chapter version does not match the file on disk; a claim named does not exist; an enum value is unknown; an escalation or thread named does not exist. Unresolved verse references do not refuse the record; they are listed.

---

## 6. Building the register: the claims, the correlation, and the history

Every row says which file it came from (`provenance`), and whether it is **recorded** or **reconstructed**. Nothing reconstructed is shown as recorded.

### R0. The claims the narrative tells (all 33 chapter files)

**This needs reading, not a script.** Deciding what goes beyond the text, and where else the same claim is told, is a judgement (sample §5). The work is done chapter by chapter, in batches, each batch reviewed by you before it is imported.

For each chapter:
1. **Prepared by script** (no judgement): the chapter's passages with their citations; the original claims whose "New ch" names the chapter; the register's change rows for the chapter (R2); and, for each verse the chapter cites, the other chapters that cite it too. Shared verses are how the other tellings were found in the sample.
2. **Read by me:** each passage is read for the claims it tells. Each claim is written in its own wording, with its sources and `beyond_text`. Each claim is linked to every passage that tells it, in this chapter and in the others found in step 1. Claims already drafted for an earlier chapter are reused, not repeated.
3. **Reviewed by you** as a batch file, in the sample's form: the claims, and where each is told.

**Cost.** The narrative is 895 KB. Reading it once, with the prepared material, is a large piece of work (several sessions). **Proposed order:** the chapters with the most cross-tellings first, since they set up claims that later chapters reuse: 10.1, 10.12, 10.13, Ch 4, Ch 11, then the rest. Approved as recommended (Q-J, round 4).

### Correlation with the register

As each chapter is read, its claims are matched to the register:
- **to an original claim**, where the original claim's "New ch" names the chapter and the claim carries it (e.g. Chapter 1's "close to 2,700 verses" carries I-2);
- **to the register's change rows** (R2), where a strand section recorded the claim being added or changed. That row's history is attached.

At the end there are three lists for your review:
- **in both**: the claim is told in the narrative and recorded in the register;
- **in the narrative only**: imported with history reconstructed from the archives (R4);
- **in the register only**: kept with `in_narrative = 0` (withdrawn originals, held claims, and any recorded addition that the narrative no longer tells; each of the last is listed, since it may be a loss).

### Alignment and discrepancies (Q-I)

The migration **aligns the register to the narrative as it now stands**. The narrative is not changed. Every gap or discrepancy found on the way is written to one **discrepancy list**, for your review:

| Kind | Example |
|---|---|
| The register records a claim that no passage now tells | a recorded addition later removed or rewritten away |
| The narrative tells a claim the register never recorded | most of the claims read in R0 |
| The register and the narrative say different things about the same claim | the register's summary of a change against the passage as it now reads |
| One claim told differently in different places | the tellings of K10 or F6, if two places disagree |
| An original claim's "New ch" names a chapter that does not tell it | |
| A statement of the book about itself that no longer matches the book | Chapter 1's outline of Chapters 10, 11 and 13 (#2111) |

Each entry gives both sides, word for word, with chapter, section and version. **The register is updated to match the narrative.** Whether the narrative should change is yours to decide, entry by entry; the list does not change it.

### History

| Step | Source | What it gives |
|---|---|---|
| **R1** | Claim register v1 → v51, each pair compared (50 comparisons) | The original 81 claims as first recorded. Every later edit to an original claim, before and after, dated by the version and tied to the escalation in the version note. The version in which each dated section first appears |
| **R2** | The 53 dated sections in v51 | One update each. Each table row is split by chapter and section into change rows, with the register's summary wording. Multi-chapter cells are split, one row per chapter |
| **R3** | The narrative index: version notes and Structure log | The update behind every chapter version, including versions with no register section (e.g. the 2026-09-30 reset; the Ch 10 split) |
| **R4** | The 373 chapter archives, each version compared with the next, **passage by passage** | For every passage that tells a claim: the version in which it first appears, and each later version in which it changed, with **the passage before and after** (Q-F). This also builds the section history and the citation history |
| **R5** | The imputed-readings audit (88 edits) and the register's Correction section (34 removals) | The 2026-10-01 changes (#1921), before and after |
| **R6** | Digest §4 (2026-09-30) | The new areas introduced at the reset, where no later record names them |

R4 gives the passages; R2, R3 and R5 give the reasons (who asked, which update). Where R4 finds a change that no record explains, the row is `reconstructed` with the instruction left empty, and it is listed.

**The limit of the reconstruction:**
- A claim's history can only start at the first archived version that tells it.
- Where a chapter was rewritten in one step (e.g. Ch 2 at #1937), the before and after are whole sections, not one passage.
- A claim's own wording is new in this build, so its earlier history is the history of the passages that tell it. The register's summaries give its earlier wording where they exist.

### Review and import (the #2000 pattern)

1. Scripts and readings write a **preview** per batch (JSON, plus a readable `.md`) and a **review list**. Nothing is written to iba.db before you approve.
2. The review list names: the correlation lists; changes found only by comparison; chapter numbers mapped across the 2026-10-02 renumbering (#1936); references that could not be parsed or have no `verse` row; the Tally recount (81 against 86).
3. Each approved batch is imported. After each, `Check` is run.

---

## 7. The register is the index (Q3)

The register, read by chapter and section, is the index of the narrative. For each chapter and section it shows:
- the claims it tells, each with any other places where the same claim is told;
- the chapter's current file and version.

It **replaces** both the current claim register file and `00-index-and-status-v1-20260930.md`. Both are frozen in `archive/` as the last hand-kept versions.

---

## 8. The published files (Q-B, Q-G, and "only the narrative goes to learning4comfort")

Three files, each with **one fixed name**, no version number and no dated copies (git holds the history; the database holds every change). They sit in `_analytics/essay/spirit_soul_body/`, **outside** `inner-being-narrative/`, so they are not copied to learning4comfort.

| File | Contents |
|---|---|
| `narrative-claim-register.md` | Index notes. The chapters in reading order, each with its sections and the claims told there, with any other places each is told. The original essay claims in their 11 tables, each with its verdict and where it is now told. The claims not in the narrative (`in_narrative = 0`). The Tally, counted |
| `narrative-claim-changes.md` | The change log by update, newest first: instruction, sources, refs and quote check; under it each claim change and each passage change, before and after. The Structure log |
| `narrative-citation-index.md` | Every verse, in canonical order, with where it is cited (chapter, section) and which claims rest on it |

Each opens with: *"Published from iba.db on {date}. Edit the register in the database (`Narrative-Register.ps1`); changes made only in this file are not kept."*

**Change to what is published today:** `00-index-and-status-v1-20260930.md` sits inside `inner-being-narrative/`, so it is copied to learning4comfort now. When it is frozen to `archive/` it will no longer be copied. **Q-K (round 4): the old index is replaced, and the copy in the learning4comfort inbox (`C:\learning4comfort\publication-inbox\the_inner_being\00-index-and-status-v1-20260930.md`) is removed.** It is removed in the same step that freezes the index to `archive/` (§10, step 7). Removing it earlier would not hold: while the index is still in `inner-being-narrative/`, the next narrative copy (at every `/session-close`) would put it back.

---

## 9. Documents that change with the build

- `iba/app/GOVERNANCE.md`: new section (§94) for the register and its rule
- `iba/app/BUILD.md`: build entry, tracking id #2110
- `iba/app/USER-GUIDE.md`: the tool and its actions
- `CLAUDE.md`: the strand rules that say each strand "updates `wa-essay-spirit-soul-body-claim-register-*` in the same pass" are restated
- The Excel tool worksheet (ps tools), per `governance.ps_worksheet_sync_on_change`
- Memory: the meaning of a claim (round 3), the register's location and the new path

---

## 10. Build order and tests (developer mode; a checkpoint after each step)

| Step | Build | Test |
|---|---|---|
| 1 | Config (§4) | `cfg_*` read-back |
| 2 | Schema and history triggers, on a copy of iba.db first | `cfg_column` matches `pragma table_info`; a direct `UPDATE` on a claim, a telling and a passage each writes its change rows with before and after |
| 3 | Reference parser and alias map | A fixed test set: full names (`2 Corinthians 1:12`) and short codes (`2Co 1:12`), ranges, lists, chains, across chapters (`Mal 2:17–3:2`), a verse with no `verse` row, an unparseable reference |
| 4 | Tool actions, with their refusals | Each action on a test set; each refusal writes nothing; `in_narrative` follows the tellings |
| 5 | Find, History, Check, Export | Each search on the test set; Check reports a moved anchor; Export of the test set matches the expected files |
| 6 | Import of the original claims and the register history (R1–R3, R5, R6) → preview and review list | All 81 claim rows, 53 sections and 551 table lines accounted for |
| 7 | **You review that preview**; import; freeze the old claim register and `00-index-and-status` to `archive/`; remove the index copy from the learning4comfort inbox (Q-K); publish the three register files | Check clean; the next narrative copy does not carry the index |
| 8 | The sample's 21 claims as the first R0 batch (Chapter 8, 10.12 opening) | Imported only after your review of the sample |
| 9 | R0 batches, chapter by chapter, each reviewed (§6); R4 history for each batch | Check clean after each |
| 10 | Documents (§9); the next real weave recorded through `Record` | The live test |

Steps 1 to 7 give a working register with the full recorded history before the reading of the narrative starts. A test plan file follows approval of this specification (`governance.module_utility_test_plan`).

---

## 11. For your decision (round 5)

All questions from rounds 1 to 4 are answered. **The specification is ready for your approval.** On approval:
1. a test plan file is written (`governance.module_utility_test_plan`);
2. the config is proposed through `Config-Maintenance.ps1 -Step Propose`;
3. the build starts in developer mode at §10 step 1, with a checkpoint after each step.

#2111 (Chapter 1's outline is out of date) is the first entry of the discrepancy list (§6). It stays on hold until you decide whether the narrative changes.

## 12. Your further comments

Added here, in place, until approval.
