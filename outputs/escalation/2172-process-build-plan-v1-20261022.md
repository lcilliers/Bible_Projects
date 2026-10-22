# 2172 — Build plan for the reading process, steps 1 to 7

Escalation: #2172. Status: the build plan for your approval. Nothing is built. It implements
section 2 of `outputs/escalation/2172-reading-process-design-v2-20261022.md` (approved 2026-10-22,
option B: the narrative register in iba.db). Step A (`narrative_section.block_text`, BUILD.md
sec 384) is live.

Researcher, chat 2026-10-22 (verbatim): "Start on the #2172 process steps 1 to 7 from
outputs/escalation/2172-reading-process-design-v2-20261022.md."

**Why a plan first.** The design settles the process. Building it raises five points the design
does not settle (section 4). Under rule 44 each one is a new decision, so I stop here and do not
answer them inline. Everything else below follows from decisions you have already made.

## 1. What exists today (checked in iba.db, 2026-10-22)

| Need | What is there | Gap |
|---|---|---|
| Observation rows | `ib_observation` 11,480 (6,527 draft, 4,953 withdrawn), `ib_node` 12,909; single writer `iba/app/lib/recordingpass.py` `record_batch` | no columns for the October parts; no `strand-reading` stage; no run_id |
| A strand | `narrative_update.strand` is free text (about 80 distinct spellings, e.g. "anger", "anger (M02; #1920)") | the word family a strand reads is stored nowhere |
| A hit's face | in October md ledgers only | no table |
| Claim sources | `narrative_claim_source` kinds lexical, science, study file, verse (1,851 rows) | no `observation` kind, no observation column |
| Tellings | `narrative_claim_telling` 432, keyed on `passage_id` (NOT NULL, UNIQUE with claim) | a block is a section, so a telling cannot name a block |
| The narrative | `narrative_section.block_text` (step A); the chapter file is still the edit source (Record, Tell and AddChapter read it) | the block cannot be written in the database |
| Coverage | `verse_meta.status` NULL on all 29,762 rows; enum `verse_meta_status` = analysed, citated, exclude | nothing writes it |
| Open items | `escalation_thread_item` 496, matched by kind cluster, strong, verse | no strand view |
| Quote check | `iba/app/lib/quotecheck.py` (step `narrative_register.quote_check`) | reused as is |

## 2. What is built

**One tool, one work package.** `iba\app\ps\Strand-Reading.ps1 -Step <step> -Strand <code>`,
work package `strand-reading`, handlers in `iba/app/handlers/strandreading.py`, the logic in
`iba/app/lib/strandreading.py`. The block write, the telling change and the export go into
`iba/app/lib/narrativeregister.py`, the existing writer of those tables. Observations are written
only through `recordingpass.record_batch`. Each step is a `cfg_step` row; each write is checked
against `cfg_write_grant`.

| Step | `-Step` | Input | What the app does | Refuses when |
|---|---|---|---|---|
| 1 Context | `Context` | the strand | writes `outputs/strand-reading/<strand>/context-v<n>-<date>.md`: every hit (verse text, strong, surface, morph, gloss), every live observation on those strongs and verses (September drafts included), open thread items matched by strong, verse or cluster, and each verse's `verse_meta.status` | the strand has no words |
| 2 Read and record | `Record` | my JSON: observations (parts as columns, verses, strongs) and one face or reason per hit | `record_batch` (grounded through `ib_node`); quote check on every quoted part; each hit's face written; read verses → `analysed` | any hit with neither a face nor a reason; an unresolved verse or strong; a quote not in its verse |
| 3 Gather | `Gather` | the strand | writes `gather-v<n>-<date>.md`: every block related by its cited verses, by claims resting on those verses, or by claims the new observations touch, each with its full text and current tellings | — |
| 4 Map | `Map` | my JSON: per block, each statement either told claim(s) or unclaimed (see decision 4) | records the tellings at block level | a block in the gather left unmapped |
| 5 Derive | `Derive` | my JSON: new, adjusted and withdrawn claims, each naming the observations and verses it rests on | through `add_claim`, `edit`, `withdraw`; observation sources as `source_kind='observation'` | a new or adjusted claim with no observation or verse source |
| 6 Rewrite | `Rewrite` | my JSON: per block, the new text, the claims it tells, and for every claim the old block told: kept, moved (to which block) or withdrawn | replaces `block_text` whole (history trigger keeps the old one); re-derives the block's citations from the text; quote check; tellings; cited verses → `citated`; renders the chapter file | any claim the old block told left unaccounted (safeguard 3); a quote not in its verse |
| 7 Account | `Account` | the strand | writes `account-v<n>-<date>.md` from the tables: each observation and its disposition; each claim and the block that tells it; each verse and its status; gaps as text | — |

**Publishing.** `narrativeregister.export` gains the chapters: each chapter file is rendered from
the database (`render_chapter`, already exact for all 35 chapters). After this build the chapter
file is an export, as the design says.

## 3. Schema changes (from decisions already made)

Each one is a migration in `iba/app/migration/`, run first against a `dbsnapshot.copy_db` copy, with
its cfg rows written through `apply_logged`.

1. `ib_observation` gains `setting`, `meaning`, `implication`, `chain`, `basis`, `parties`, `run_id`
   (decision 3). `cfg_enum ib_observation.stage` gains `strand-reading`.
2. `narrative_claim_source` gains `observation_id` (FK `ib_observation`); `cfg_enum
   narrative_claim_source_kind` gains `observation` (decision 4).
3. Dispositions use the existing `ib_observation.status` values (decision 5): carried by a claim →
   `resolved` (the claim names it); held as a thread item → `open` (the item names it); silent →
   `silent`, reason in `revisit_note`; withdrawn → `withdrawn`, reason in `revisit_note`.

## 4. Decisions the build needs

| # | Decision | Options | Claude recommends |
|---|---|---|---|
| 1 | **Where a strand and its hits live.** | **A.** New tables `reading_strand` (code, title, escalation id, state), `reading_strand_strong` (its word family) and `reading_strand_hit` (one row per strong-in-verse hit: face, or reason, and the observation it went into). **B.** No new table: the word family as a cfg_setting per strand, faces as `ib_observation` rows with a tag. | **A.** A strand is project data, not config, and safeguard 1 (a face for every hit) is a plain join only if each hit is a row. B puts one row per hit into `ib_observation` and mixes faces with findings. |
| 2 | **Tellings at block level.** | **A.** `narrative_claim_telling` is rebuilt with `section_id` (the block) and `passage_id` made nullable; each current passage telling (432) is copied to its section; the passage rows stay as history. **B.** Keep passage tellings and re-derive the passages from each rewritten block. | **A.** The design tells claims per block. B would tie the new process to paragraph anchors, which is the line-by-line fixing you ruled out. |
| 3 | **A verse both read and cited.** `verse_meta.status` holds one value. | **A.** `citated` replaces `analysed` (the stronger state); `exclude` is never overwritten by the process. **B.** A second column. | **A.** |
| 4 | **A statement in a block that tells no claim** (step 4). | **A.** It must become a new claim (step 5) or an item on the strand's escalation; the Map step refuses otherwise. **B.** A new table of unclaimed statements. | **A.** It routes through the claims register and the open-item register that exist. |
| 5 | **The close gate** (safeguard 5, approved as design decision 6). | **A.** A new `cfg_escalation_requirement` check kind `strand_account_clean`: the strand's escalation cannot reach completed or closed while any hit has no face or reason, any observation has no disposition, or a rewrite left a claim unaccounted. **B.** The gate only in the Account step's output. | **A.** The same mechanism already gates threads (`no_open_thread_items`). |

## 5. Build order and test

1. The migrations in section 3 and decisions 1 and 2. Test on a copy: row counts before and after;
   the 432 tellings carried over one to one.
2. Steps 1 and 2 (Context, Record). Test on a copy with a small real strand (for example the
   anger words in one book): context complete; a JSON with one unfaced hit is refused; a clean JSON
   writes observations, nodes, faces and `analysed`.
3. Steps 3 and 4 (Gather, Map).
4. Steps 5 and 6 (Derive, Rewrite). Test: a rewrite that drops a told claim is refused; a clean
   rewrite renders the chapter exactly from the database and keeps the old block in history.
5. Step 7 (Account) and the close gate (decision 5). Test: the gate refuses a close with an open
   gap and allows it once settled.
6. Export of chapters; `configmaint.validate` clean; BUILD.md, USER-GUIDE.md and GOVERNANCE.md
   (the narrative home ruling) updated.

These tests use synthetic JSON on a copy. They exercise the controls, not a reading. No reading of
the study is done (the study is on hold). Catch-up B to D comes after, as the design orders.
