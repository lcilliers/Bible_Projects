# The chapter table: proposal for review (v1)

> **Escalation #2155.** Researcher, chat 2026-10-18 (verbatim): *"got it, the chapter table was
> built with the claims register migration.  Yes, any the chapter build should be added to the
> chapter table. The use of the chapters should be clear from the chapter table and this table
> should be fully integrated into the governance and config"*.
>
> **Status: approved and built, 2026-10-18.** Researcher, verbatim: *"Approve #2155 as proposed: D1
> kinds as listed, D2 purposes as drafted, D3 publishing follows the table, D4 the behaviour rule.
> Proceed to test and build."* Built as BUILD.md §351 and GOVERNANCE.md §95. Tests: 16 of 16
> passed, and T10 gave 47 findings, unchanged. One deviation: T10 shows 0 `direct edit` notices, not
> 3, because the three hand inserts carry `created_by='Claude'` (see BUILD.md §351).

---

## 1. What the chapter table is today

`narrative_chapter` in iba.db holds one row per chapter. It was built on 2026-10-13 by the claims
register migration (#2110) from the chapter list in the old `00-index-and-status` file. There are
37 active rows (00 Introduction to Ch 15, plus the Part 10 heading and the deferred science
chapter) and one retired row (the old Ch 13 *Under God's anger*).

**What is already in place:**

- **Config.** The table and each of its columns are described in `cfg_table` and `cfg_column`. The
  state values (draft, draft + held, empty, deferred) are a `cfg_enum`. Two triggers refuse a
  chapter number that an active chapter already uses, and a third logs a renumbering against
  every claim told in the chapter.
- **The table matches the files on disk.** Checked 2026-10-18: every active chapter's current file
  exists, and every `.md` file in the narrative folder is some chapter's current file.
- **Tool actions.** `Narrative-Register.ps1 -Action EditChapter` changes an existing row (number,
  title, state, current file, version, reading order, retired). `EditSection` adds or changes
  section rows. `Check` compares the chapters and sections with the files.

**What is missing (the gaps #2155 is about):**

| # | Gap | Effect today |
|---|---|---|
| G1 | No action adds a chapter. | 10.14, 10.15 and 00 were inserted by hand, along with the reading-order shift for the later chapters. |
| G2 | The table does not say what each chapter is **for**. `title` names it. `built_from` says which work it came from, and `replaces_original` maps it to the old essay. Nothing says what belongs in it, or which ruling set it up. | The use of each chapter lives only in CLAUDE.md prose and in escalations. Examples: 10.12 holds the full account of fear (#1961), Ch 13 holds other beings (#1982), Ch 11 holds what has no other home (#1998). |
| G3 | The table does not separate kinds of row. A file-less part heading (row 10), a deferred placeholder (science), front matter (00) and a sub-chapter all look alike. | Readers and checks cannot tell them apart. |
| G4 | Adding a chapter is not always logged. The Structure log (in `narrative-claim-changes.md`) is fed by weave updates. 10.14 and 10.15 are there (updates 141, 143). **00 Introduction is not**, because it came with no weave. | A chapter can appear with no record of when or why. |
| G5 | The copy to learning4comfort takes every `.md` file at the top of the narrative folder, not the chapters in the table. | A stray file in the folder would be published. Nothing ties publishing to the table. |
| G6 | GOVERNANCE §94 and USER-GUIDE §12h say a chapter can be *"added, split, merged, renamed, renumbered or retired, each logged"*. | Adding and logging are not yet true (G1, G4). |

---

## 2. The proposal

### 2.1 The table says what each chapter is for (G2, G3)

I propose three new columns:

| Column | Holds | Example (10.12) |
|---|---|---|
| `kind` | One of a short list kept in config (`cfg_enum narrative_chapter_kind`, see D1). | `key characteristic` |
| `purpose` | In plain words: what the chapter holds, what belongs in it, and what goes elsewhere. | "The full account of fear as a key characteristic: its words, faces, other parties and outcomes. Other chapters carry fear only where it belongs to their own activity, and point here." |
| `purpose_ref` | The rulings that set the purpose: escalation numbers and dates. | `#1961 (2026-10-04)` |

`built_from` and `replaces_original` stay as they are; they record history, not use.

A draft of `kind`, `purpose` and `purpose_ref` for every row is in **Appendix A**. Each draft is
taken from a recorded ruling or from the chapter's own opening. Where I found no ruling, the draft
says so rather than inventing one.

### 2.2 Every chapter change goes through the tool (G1, G4, G6)

- **New action `AddChapter`.** It takes:
  - `-Chapter`, `-Title`, `-Kind`, `-Purpose`, `-PurposeRef`, `-State`
  - `-After <chapter>` (or `-ReadingOrder`)
  - `-CurrentFile`. This is required unless the kind is a part heading or a deferred placeholder.
  - `-BuiltFrom`, `-By`, `-Note`

  It then:
  1. refuses a number already in use, a file not on disk, or a kind or state not in config
  2. moves every later chapter down one place in the reading order
  3. writes the chapter's section rows from the file's own headings, which replaces the hand-run `EditSection` step
  4. writes a Structure log entry (a `narrative_update` row with `structure_change` and `structure_reason`)

  All four happen in one step: if any part fails, nothing is written.
- **`EditChapter` gains `-Kind`, `-Purpose`, `-PurposeRef` and `-After`.**
  - `-After` moves a chapter and closes the gap it leaves.
  - A change of number, title, kind, purpose, place or retirement also writes a Structure log entry. Today only a renumbering is logged, and only against the claims.
- **Split and merge** stay as a sequence of the actions above, each one logged. The split and merge
  cases have been rare (Ch 13 folded into 10.13), and a dedicated action would be engineering
  ahead of need.
- **Backfill.** On build I would add the missing Structure log entry for 00 Introduction (G4), dated
  2026-10-18, citing #2159.

### 2.3 Check guards the table (G5)

`Narrative-Register.ps1 -Action Check` gains these findings:
- an active chapter with no `kind` or `purpose`
- two active chapters with the same reading order
- a `.md` file in the narrative folder that is no active chapter's current file
- a chapter whose `created_by` is `direct edit`: inserted outside the tool. This is reported, not refused, so the three existing hand inserts stay visible as history and do not count as errors.

### 2.4 Publishing follows the table (G5, see D3)

`Copy-NarrativeToLearning4Comfort.ps1` would copy exactly the active chapters' current files, in
reading order, rather than whatever `.md` files sit in the folder. The table then decides what is
published. A file that is not a chapter is reported and not copied.

### 2.5 The published register shows it

`Export` opens `narrative-claim-register.md` with a **Chapters** table:
- number, title, kind and state
- purpose, and the ruling it rests on

This is the place to read what each chapter is for, without opening iba.db.

### 2.6 Governance and config (integration)

| Where | Change |
|---|---|
| `cfg_enum` | new `narrative_chapter_kind` (D1) |
| `cfg_column` | rows for `kind`, `purpose`, `purpose_ref`; `created_by` expectation notes that `direct edit` is flagged by Check |
| `cfg_table` | `narrative_chapter` use text: "the authority for which chapters exist, their order and what each is for; changed only through Narrative-Register.ps1" |
| `cfg_behaviour_rule` | new rule `narrative-chapters-change-only-through-the-register` (D4): every chapter is added, moved, renamed, renumbered, split, merged or retired through `Narrative-Register.ps1`, never by direct insert or update. Enforcement: `partially_enforced` (Check reports a direct insert; it cannot stop one). |
| GOVERNANCE.md | new §95: the chapter table is the authority for the book's chapters and their use (this ruling, verbatim) |
| USER-GUIDE.md §12h | `AddChapter`, the new `EditChapter` options, the new Check findings |
| BUILD.md | the build entry |
| CLAUDE.md | one line under the narrative banner: a new chapter is added with `AddChapter`, and the chapter's purpose is recorded in the table |

All config rows go in as one logged migration (`configmaint.apply_logged`), as for #2110.

---

## 3. Decisions for you

- **D1. The kinds.** Proposed list:
  - `front matter` (00)
  - `chapter` (a numbered chapter: 01–09, 11, 12, 14, 15)
  - `part heading` (row 10: a heading with no file of its own)
  - `opening` (10.0 and 13: the opening of a part)
  - `activity` (10.1–10.11)
  - `key characteristic` (10.12–10.15)
  - `other beings` (13.1–13.4)
  - `deferred` (science)

  You can change, merge or add kinds.
- **D2. The purposes in Appendix A.** Please correct any that misstate a chapter's use. Once
  approved they go into the table as written.
- **D3. Publishing follows the table (§2.4).** Recommended: yes. The alternative is to keep the
  folder copy, with Check reporting stray files.
- **D4. The behaviour rule (§2.6).** Recommended: yes.

---

## 4. Test plan

All tests run on a **copy** of iba.db and a scratch copy of the narrative folder, never on the live
ones. The live build runs only after every test passes.

| # | Test | Expected |
|---|---|---|
| T1 | `AddChapter -Chapter 10.16 -After 10.15` with a test file | row added at reading order 27; Ch 11 onward each +1; section rows match the file's headings; one Structure log entry |
| T2 | `AddChapter` with a number already active (10.15) | refused; nothing written |
| T3 | `AddChapter` with a file not on disk | refused; nothing written |
| T4 | `AddChapter` with a kind or state not in config | refused; nothing written |
| T5 | `AddChapter -Kind "part heading"` with no file | accepted |
| T6 | `EditChapter -Chapter 10.16 -After 10.11` | moved; the gap closed; reading orders unique; Structure log entry |
| T7 | `EditChapter -Purpose ..` | changed; Structure log entry with before and after |
| T8 | Check with a stray `.md` in the folder | one finding naming the file |
| T9 | Check with a chapter missing a purpose | one finding |
| T10 | Check on the live copy after the backfill | the 47 existing findings plus three `direct edit` notices (00, 10.14, 10.15); no new errors |
| T11 | Copy with the table-driven selection (if D3 = yes) | 35 files copied, matching the active chapters' current files; the stray test file not copied, reported |
| T12 | Export | the Chapters table appears, one row per active chapter, in reading order |
| T13 | Rerun T2–T4 and confirm the DB copy is byte-identical to before | nothing partial written |

---

## Appendix A. Draft kind and purpose for every chapter

Sources: CLAUDE.md narrative rulings, GOVERNANCE §90/§94, and each chapter's own opening.
"No recorded ruling" means the purpose is read from the chapter itself.

| No. | Title | Kind | Purpose (draft) | Ruling |
|---|---|---|---|---|
| 00 | Introduction | front matter | What the study is, where it began and how it is put together, for a reader coming to it new. Points to Ch 1 for the question. | #2159 (2026-10-18) |
| 01 | The question behind the words | chapter | How the question moved from "two parts or three?" to "how does the inner being work?", and the shape of the book. | No recorded ruling; reset 2026-09-30 (#1912/#1913) |
| 02 | Life, breath and death | chapter | Sets the scene: what life is about and what death means, as the setting in which the inner being works. Death is told by its kinds (dead in, dead to, death in the living). | #1936, #1937 (2026-10-02); OT-02 #2003 (2026-10-14) |
| 03 | One inner person, many words | chapter | How the words for the inner person relate: one person, spoken of from several sides. | No recorded ruling |
| 04 | The heart | chapter | The word *heart*: what Scripture shows the heart doing and undergoing. | No recorded ruling |
| 05 | The soul | chapter | The word *soul*, as for the heart. | No recorded ruling |
| 06 | The spirit | chapter | The human spirit, as for the heart. The Holy Spirit's own acts go to 13.1. | #1986 (2026-10-08) for the 13.1 boundary |
| 07 | Flesh | chapter | The word *flesh* as part of the inner person. | No recorded ruling |
| 08 | Conscience and the bosom | chapter | The words *conscience* and *bosom*. | No recorded ruling |
| 09 | Where the words part | chapter | The places where Scripture does draw the words apart. | No recorded ruling |
| 10 | Part 10 — The inner being at work | part heading | Heading for the activity chapters 10.0 to 10.15. No file. | #1918 (2026-09-30): Ch 10 designed to grow |
| 10.0 | The inner being at work | opening | How the activities work together, following the paths from a thought or a feeling to a deed; the map of Part 10. | No recorded ruling |
| 10.1 | Feeling | activity | Feeling as an activity, with **Delight**: a person's delight has its one account here. The "feeling" frame itself is an open question (OT-12). | M18 group B ruling (2026-10-09); OT-12 |
| 10.2 | Knowing and hearing | activity | Knowing and hearing, including what blocks hearing (pride, a famine of hearing). | No recorded ruling |
| 10.3 | Remembering and forgetting | activity | Remembering and forgetting. | #1920 (2026-10-01) |
| 10.4 | Thinking | activity | Thinking and where thought comes from. | No recorded ruling |
| 10.5 | Speaking | activity | Speaking and what speech carries from within. | No recorded ruling |
| 10.6 | Wanting | activity | Wanting and desire: the home for the desire words (M18), apart from delight (10.1). | M18 ruling (2026-10-09): *"10.6 is fine for M18"* |
| 10.7 | Choosing and setting direction | activity | Choosing, being chosen, planning, willing and taking the lower place: choosing as one account of setting direction. | #1978 (2026-10-08 reframe); #1986 |
| 10.8 | Right and wrong | activity | Knowing and doing right and wrong. | No recorded ruling |
| 10.9 | Relating to God | activity | The person's side of relating to God (God's own acts go to 13.1). | #1982 (2026-10-07) |
| 10.10 | Relating to others | activity | Relating to others, including holding authority over another and pride over another. | #1998 (2026-10-12) |
| 10.11 | Hiding and disclosing | activity | Concealment and disclosure, before God and before others, as one account. | #1931 (2026-10-02) |
| 10.12 | Fear | key characteristic | The full account of fear as a key characteristic. Other chapters carry fear only where it belongs to their own activity, and point here. | #1961 (2026-10-04) |
| 10.13 | Anger | key characteristic | The full account of anger, including living under God's anger (the old Ch 13, folded in). | #1963, #1977 (2026-10-05) |
| 10.14 | Humility | key characteristic | The full account of humility (*"humility is not a feeling"*). Each of its angles is also woven into its own chapter. | #2148 (2026-10-15) |
| 10.15 | Pride | key characteristic | The full account of pride. Ch 12 keeps pride as a way the inner being goes wrong and points here. | #2156 (2026-10-15) |
| 11 | Other sides of the inner being | chapter | A collection of inner-being elements that have no other home; the title carries no weight in the analysis. §4 is the cross-cutting account of how a word or act changes character. | #1998 (2026-10-12); #1919 (2026-10-01) |
| 12 | When the inner being goes wrong | chapter | What goes wrong in the inner being. Unchecked original material stays in Held sections. | No recorded ruling for the purpose; Held rule from the 2026-09-30 reset |
| 13 | Other beings | opening | The opening of Ch 13: other beings in their own right, routed here (verse routing A). | #1982 (2026-10-07); rule 72 |
| 13.1 | Divine | other beings | God in his own right, including the Spirit and Jesus, and how his character reaches the human inner being. | #1982; #1986 (2026-10-08); #2148 (2026-10-15) |
| 13.2 | Angels | other beings | Angels in their own right. | #1982 |
| 13.3 | Other spirits | other beings | Other spirits in their own right, including the devil. | #1982 |
| 13.4 | Nature | other beings | The physical world in its own right. | #1982 |
| 14 | Made new | chapter | How the inner being is made new. Unchecked original material stays in Held sections. | No recorded ruling |
| 15 | Beyond the named words | chapter | The inner life Scripture describes without naming heart, soul or spirit. | No recorded ruling |
| science | (science) | deferred | The science chapters, written after the biblical reading. | Reset 2026-09-30: *"Science chapters come later"* |
