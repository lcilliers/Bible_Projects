# 2172 — One reading process (v2): findings, claims, and the narrative told in blocks

Escalation: #2172. Status: a design for your decision. Nothing is built. v1 is archived; v2 takes in
your change.

**Your change (2026-10-22, verbatim):** "after the read pulled the lexical, existing observations,
relevant open items, it produces to updated/new ib_observations, then it reads all the existing
related narrative paragraphs and map it to claims register, it then use the new ib_observations,
existing narrative and claims, to derive new or adjusted claims.  The new and adjusted claims are then
written back into the narrative, replacing all the previous paragraphs.  This will ensure that the
narrative is not fixed line by line, but in blocks, which will make much more sense.  The narrative is
not a listing of the claims, it is the story of the claims.  I would not be surprised if you decide to
keep the narrative in the database (most logical place is the prose_section), the push to
learning4comfort then becomes an extract from the prose section and the process of managing the
narrative is in the database, rather than reading through everything. the prose section could have a
cross reference to the claims."

## 1. The principle (unchanged from v1)

- **I do the reading and the writing, in the session.** The app gives me everything already known,
  records the results as rows, and checks facts.
- **Where judgement is needed, the app shows the texts side by side.** It refuses only on a fact.

**New in v2:** the narrative itself lives in the database. A chapter file becomes an export, not the
thing that is edited.

## 2. The process: seven steps

| # | Step | Who | What happens |
|---|---|---|---|
| 1 | **Context** | app | For the strand it writes one context file: every hit with its text and lexical data; every existing observation on those strongs and verses (September's drafts included); the matching open thread items; each verse's `verse_meta.status`. |
| 2 | **Read and record** | me, then app | I read (the October method) and produce new and updated observations. `record_batch` writes them to `ib_observation`/`ib_node`, grounded and quote-checked. Each verse read is marked `analysed`. Every hit needs a face or a stated reason. |
| 3 | **Gather the narrative** | app | Every narrative block related to the strand: by the verses it cites, the claims resting on those verses, and the claims the new observations touch. Each block comes with its full text and the claims it now tells. |
| 4 | **Map the narrative to the claims** | me | I read those blocks and map what they say to the claims register. Each statement in a block is either a told claim, or a statement with no claim, which I name as a new claim or flag. The app records the mapping. |
| 5 | **Derive the claims** | me, then app | From the new observations, the existing narrative and the existing claims, I derive new and adjusted claims, and withdraw any that no longer stand. Each claim names the observations and verses it rests on. Written through the register (`add_claim`, `edit`, `withdraw`). |
| 6 | **Rewrite the blocks** | me, then app | Each affected block is written anew as the story of its claims, not as a list of them, and replaces the previous block whole. The app keeps the previous version in history, re-derives the block's citations from its text, runs the quote check, records which claims the block tells, and marks the cited verses `citated`. |
| 7 | **Account** | app | One page per strand, from the tables: every observation and the claim it went into, or why not; every claim and the block that tells it; every verse and its status. Gaps are shown as text. |

**Then publish.** The chapter files for learning4comfort are produced from the database. The
existing `narrativeregister.export` already writes the register files; chapters are added to it.

## 3. Safeguards (where a fact can be checked)

1. **No reading without a face for every hit.** Each hit has a face or a stated reason (step 2).
2. **No observation without a disposition.** Each one is carried by a claim (named), held as a
   thread item, silent (with why), or withdrawn (with why).
3. **No claim lost in a rewrite.** A block rewrite must account for every claim the old block
   told: still told, moved (to which block), or withdrawn. This is the guard that block rewriting
   needs. Without it, a whole paragraph and its claims could vanish quietly.
4. **No quote that is not in its verse.**
5. **No close while 1 to 3 are open.** The strand's escalation cannot close until they are settled.
   Everything else in the account is shown for judgement, not gated.

## 4. Where the narrative lives: two options

| | A. `prose_section` (bible_research.db), as you suggested | B. The narrative register in iba.db, extended |
|---|---|---|
| What is there now | 1,036 sections of earlier prose (findings 583, design, programme, glossary, essays); versioning through `record_change_log`; a type vocabulary with book, chapter and section order; full-text search; `prose_section_verse_link` (empty). Last written 2026-09-18. The write path (ImportChapter) depends on a retired script (#2212). | `narrative_chapter` (38), `narrative_section` (403 live), `narrative_passage` (385), with history triggers already logging every change, and the claim tellings and citations linked by FK |
| A block | one `prose_section` row per narrative section | the `narrative_section` row gains the block's text |
| Link to claims | across databases (claims are in iba.db): a link with no FK, joined by ATTACH | inside one database, with FKs, as tellings are now |
| History | `record_change_log` | the existing `trg_narrative_*` triggers and `narrative_claim_change` |
| Governance | fits `governance.scope_research_db` (research_db is prose-only) | needs a governance setting: the study's narrative is kept with its claims in iba.db |
| Work to make it the home | a narrative section type; a working write path; the cross-database link; history | one column (block text); export of chapters; retire the passage-level split where a block replaces it |

**Claude recommends B, with care.** The account and the safeguards (steps 3 to 7) are joins between
observations, claims, blocks and verses. In one database they are plain SQL with foreign keys. Across
two, every check depends on a link the database cannot enforce. The narrative register was built to
hold exactly this, and its history already works. B needs your ruling on governance, because it puts
narrative prose in iba.db. If you prefer A, the design is the same, and only the block's home and
the link change.

## 5. Catch-up of the September and October gaps (same methods)

**Moving the narrative into the database:**
- **A. Import the current chapters into blocks**, once: 38 chapters, using the existing
  `parse_chapter`. Each block keeps its claims (the tellings already exist).
- **After A, the chapter files are exports only.**

**Catching up the readings:**
- **B. Import the October ledgers into `ib_observation`:** about 840 rows (AG 240, LD 227, FE 205,
  AN 167 and others) through `record_batch`. A row that does not parse cleanly is listed for me to
  fix, not guessed. The batch readings in other formats are recorded through step 2, file by file.
- **C. Link the existing claims to observations:** proposed by shared verses, side by side, and
  confirmed by me on meaning. A shared verse alone never makes a link.
- **D. Run the account:** it shows the real gaps strand by strand, as text:
  - flesh and body (#2162);
  - the unapplied corrections (Heb 10:22, 1Co 6:19b-20, Neh 6:13, Psa 69:9);
  - claims with no observation behind them;
  - the 46 claims with no live telling and the 13 with no verse source;
  - the 306 open thread items.
- **E. September's drafts** are offered in step 1 wherever a strand touches them, then confirmed,
  corrected or withdrawn there.

**F. The redo** runs each gap through steps 1 to 7, in the order you set. It is study work, so it
waits until you re-open the study. A to D read nothing new.

## 6. Decisions

| # | Decision | Claude recommends |
|---|---|---|
| 1 | The process as in section 2 (your change included) | approve |
| 2 | The narrative's home: A `prose_section` or B the iba.db register | B, with the governance ruling it needs |
| 3 | The October ledger row is an `ib_observation` row, its parts (setting, meaning, implication, chain, basis, parties) as columns, a stage `strand-reading`, and a `run_id` | yes |
| 4 | A claim may name observations as sources (`narrative_claim_source_kind` value `observation`) | yes |
| 5 | Dispositions on the existing `ib_observation.status` values | yes |
| 6 | The safeguards in section 3, with the one close gate | yes |
| 7 | Build order: the narrative into the database (A), the process (steps 1 to 7), then catch-up B to D | as listed |
