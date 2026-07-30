# Full config extract — everything that governs `passage`

> Generated 2026-07-29 for a holistic review, at the researcher's request. Every `cfg_*` table was
> searched for any row with `passage` in any column (all 19 `cfg_*` tables checked; 12 had hits).
> Read-only extract — no code/config changed. All rows shown, active and inactive, in full.

## Contents
1. [cfg_work_package](#1-cfg_work_package) — the routines
2. [cfg_step](#2-cfg_step) — steps within each routine
3. [cfg_setting](#3-cfg_setting) — parameters
4. [cfg_write_grant](#4-cfg_write_grant) — which step may write which table
5. [cfg_on_fail](#5-cfg_on_fail) — failure/pause routing per step+condition
6. [cfg_report / cfg_report_section / cfg_report_csv_table](#6-cfg_report--cfg_report_section--cfg_report_csv_table) — report shape
7. [cfg_column](#7-cfg_column) — table/column definitions for `passage` and `verse_passage`
8. [cfg_enum](#8-cfg_enum) — controlled vocabularies touching passage
9. [cfg_table](#9-cfg_table) — table-level grain/purpose
10. [cfg_unique](#10-cfg_unique) — uniqueness constraints
11. [cfg_change_detail](#11-cfg_change_detail) — recent change history (audit trail, not a live rule)
12. Tables checked with **no** passage-related rows

---

## 1. `cfg_work_package`

| name | ps_script | runs_over | chained | complete_message | inactive |
|---|---|---|---|---|---|
| `set-candidates` | `Set-Candidates.ps1` | book | 1 | "candidates set for '{book}'. Next: Build-Passages.ps1 -Book {book}" | **1** |
| `build-passages` | `Build-Passages.ps1` | book | 1 | "passages built for '{book}'." | **1** |
| `passage-quality` | `Passage-Quality.ps1` | none | 0 | — | 0 |
| `passage-debate-report` | `PassageDebate-Report.ps1` | book | 0 | — | 0 |

`set-candidates` is included because its own `complete_message` chains into `build-passages` — both
retired together.

## 2. `cfg_step`

| work_package | step | handler | scope | does | inactive |
|---|---|---|---|---|---|
| `build-passages` | `passage.build` | `handlers/passage.py:build` | book | recompute the book's passages from `span_candidate` (char-continuity\|maximal); flag >review_over as needs_review | **1** |
| `passage-quality` | `passage.validate` | `handlers/passage.py:validate` | none | read-only quality check: passage verse_count distribution — one escalation per invocation, standalone (not part of build-passages) | 0 |
| `passage-debate-report` | `report.passage_debate` | `handlers/reports.py:passage_debate_report` | book | passage-debate scaffold generator — verifies the base verse-span-meaning extract and current method docs exist, resolves output path/naming, writes a debate-document SKELETON; does not generate interpretive content itself | 0 |
| `whole-book-read` | `report.whole_book_read` | `handlers/reports.py:whole_book_read_report` | book | gathers every `debate_status='filled'` passage row in reading order, extracts Emergent-questions/Passage-level-linkages sections, lays out per-passage with an empty Resolution slot | 0 |
| `raw-backfill` | `raw.backfill_meaning` | `handlers/raw.py:backfill_meaning` | book | pulls missing strong meanings for a book/range — "passage-driven DB coverage growth" in its own description, listed here for that phrase only; not a passage-boundary step | 0 |

## 3. `cfg_setting`

**Retired (inactive=1) — the old boundary/sizing rule:**

| key | value | use |
|---|---|---|
| `passage.default_rule` | `"char-continuity"` | boundary rule when `-Rule` not given: run continues while consecutive verses share ≥1 candidate base-strong |
| `passage.cross_chapter` | `false` | passages do not cross a chapter boundary |
| `passage.min_shared_strongs` | `1` | char-continuity threshold: verses must share at least this many candidate base-strongs to stay in one run |
| `passage.review_over` | `10` | a passage longer than this is flagged needs_review. Set to 10: "the IB role is only assessable read as a full passage, so only very long runs warrant a manual second look" |

**Live (inactive=0) — path/naming/method pointers, no boundary logic:**

| key | value | use | module |
|---|---|---|---|
| `validation.show_passages` | `true` | book report: include the passages section | validation |
| `passage.quality_report_path` | `"iba/app/reports/passage-quality.md"` | where `passage.validate` persists its findings | passage |
| `report.passage_debate_naming_pattern` | `"WA-{book}-{range}-debate.md"` | filename pattern for `report.passage_debate` | report |
| `report.whole_book_read_naming_pattern` | `"WA-{book}-whole-book-read.md"` | filename pattern for `report.whole_book_read` | report |
| `method.passage_read_guidance_path` | `"iba/docs/WA-passage-read-guidance-v1.4-2026-07-28.md"` | current version of the passage *reading* method (steps 1-5) — the scaffold/AI must follow this exact file | method |
| `method.interpretation_questions_path` | `"iba/docs/WA-interpretation-questions-v1.3-2026-07-28.md"` | current version of the Q1-Q10 interrogative + Part B guidance | method |
| `governance.verse_gap_by_design` | (long text) | 2026-07-29 ruling: missing verse rows are by-design, not a bug; both report steps note the gap inline and skip | governance |
| `report.verse_gap_note` | (template text) | inline note both report steps insert wherever a verse gap is detected | report |
| `notification.paused_banner_guided` | (template) | PAUSED banner for non-chained single-step packages incl. `passage-quality` | notification |
| `notification.paused_banner_passthrough` | (template) | PAUSED banner for chained packages incl. `build-passages` | notification |
| `notification.stopped_banner` | (template) | STOPPED banner, uniform across chained packages incl. `build-passages` | notification |

## 4. `cfg_write_grant`

| writer | table_name | inactive |
|---|---|---|
| `passage.build` | `passage` | **1** |
| `passage.build` | `verse_passage` | **1** |
| `report.verse_span_meaning` | `passage` | 0 |
| `report.verse_span_meaning` | `verse_passage` | 0 |
| `report.passage_debate` | `passage` | 0 |
| `report.passage_debate` | `verse_passage` | 0 |

Confirms who may write the tables today: only the two verse-fanout report steps — not `passage.build`.

## 5. `cfg_on_fail`

| step | condition | path | route | message | inactive |
|---|---|---|---|---|---|
| `passage.build` | `no-candidates` | report-stop | terminal | the book has no candidate spans — run set-candidates first | **1** |
| `passage.validate` | `needs-review` | pause-continue | terminal | passage verse_count distribution needs researcher judgement | 0 |
| `passage.validate` | `findings-rejected` | report-stop | terminal | researcher flagged the passage distribution as needing the rule revisited | 0 |
| `passage.validate` | `needs-revision` | report-stop | terminal | researcher asked for more specific investigation (see comment) | 0 |
| `report.passage_debate` | `base-extract-missing` | report-stop | terminal | base verse-span-meaning extract for this exact book/range not found | 0 |
| `report.passage_debate` | `guidance-doc-missing` | report-stop | terminal | `method.passage_read_guidance_path`/`method.interpretation_questions_path` points to a file that doesn't exist on disk | 0 |
| `report.whole_book_read` | `no-debates-found` | report-stop | terminal | no `debate_status='filled'` passage row exists yet for this book | 0 |

Note `passage.validate`'s `findings-rejected` message still literally says *"the rule"* — worded
when a rule existed to revisit; today there's no rule behind that wording either.

## 6. `cfg_report` / `cfg_report_section` / `cfg_report_csv_table`

**cfg_report**

| step | title | show_toc | output_kind | naming_scheme | inactive |
|---|---|---|---|---|---|
| `passage.validate` | Passage quality report | 1 | md+csv | stable | 0 |
| `report.passage_debate` | `{book} {range} -- Passage Debate` | 1 | md | stable | 0 |

**cfg_report_section**

| step | ordinal | section_key | heading | inactive |
|---|---|---|---|---|
| `passage.validate` | 0 | dist | ## verse_count distribution | 0 |
| `passage.validate` | 1 | by_book | ## By book | 0 |
| `validation.book` | 2 | passages | ## 4. Passages | 0 |
| `report.passage_debate` | 0 | preliminaries | ## Preliminaries | 0 |
| `report.passage_debate` | 1 | verses | ## Per-verse debate | 0 |
| `report.passage_debate` | 2 | linkages | ## Passage-level linkages (Q7) | 0 |
| `report.passage_debate` | 3 | insufficiencies | ## Insufficiencies register | 0 |
| `report.passage_debate` | 4 | emergent | ## Emergent questions log | 0 |
| `report.passage_debate` | 5 | open_decisions | ## Open decisions / next steps | 0 |
| `report.whole_book_read` | 1 | carried_forward | ## Carried forward per passage | 0 |

**cfg_report_csv_table**

| step | table_name | join_note | inactive |
|---|---|---|---|
| `passage.validate` | `passage` | — | 0 |
| `passage.validate` | `verse_passage` | — | 0 |
| `validation.book` | `passage` | book-scoped | 0 |
| `validation.book` | `verse_passage` | book-scoped | 0 |

## 7. `cfg_column` — `passage` (14 cols) and `verse_passage` (6 cols)

**`passage`**

| col | type | notnull | use | expectation | filled_by |
|---|---|---|---|---|---|
| id | INTEGER | | surrogate key | | |
| book | TEXT | 1 | OSIS book code | | derived:verse.osisId |
| anchor_verse_id | INTEGER | 1 | first verse of the run — the anchor | | |
| start_chapter | INTEGER | | range start chapter | | `passage.build` |
| start_verse | INTEGER | | range start verse | | `passage.build` |
| end_chapter | INTEGER | | range end chapter | | `passage.build` |
| end_verse | INTEGER | | range end verse | | `passage.build` |
| ref | TEXT | | human range | | `passage.build` |
| verse_count | INTEGER | | ≥1 | | `passage.build` |
| rule | TEXT | | char-continuity \| maximal | `enum.passage_rule` | `passage.build` |
| source | TEXT | | passage-build \| single-verse-emergent | `enum.passage_source` | `passage.build` |
| needs_review | INTEGER | | 1 when verse_count > `passage.review_over` | | `passage.build` |
| created_at | TEXT | | when built | | `passage.build` |
| deleted | INTEGER | | soft delete (dflt 0) | | |
| book_label | TEXT | | human-facing subfolder name, defaults to `book` | | `report.verse_span_meaning` |
| verse_span_meaning_path | TEXT | | path to this range's extract output | | `report.verse_span_meaning` |
| verse_span_meaning_written_at | TEXT | | UTC timestamp of last extract write | | `report.verse_span_meaning` |
| debate_path | TEXT | | path to this range's debate output | | `report.passage_debate` |
| debate_written_at | TEXT | | UTC timestamp of last debate write | | `report.passage_debate` |
| debate_status | TEXT | | 'scaffold' or 'filled' — coarse mechanical signal only, NOT a digestion of analytical content | `enum.passage_debate_status` | `report.passage_debate` |

**Note:** `rule`, `source`, `needs_review`, and the `filled_by: passage.build` columns are **stale
metadata** — `passage.build` is inactive and no live row has these populated (confirmed empirically
2026-07-29: every live Dan row has `rule=NULL, source=NULL`). `cfg_column` itself was not updated
when `passage.build` was retired, so it still describes the old regime as if live.

**`verse_passage`**

| col | type | notnull/unique | use | filled_by |
|---|---|---|---|---|
| id | INTEGER | pk | surrogate key | |
| passage_id | INTEGER | notnull, fk passage.id | the passage | |
| verse_id | INTEGER | notnull, **unique**, fk verse.id | the verse (one passage per verse) | |
| is_anchor | INTEGER | | 1 on the anchor verse | `passage.build` (stale — actually set by `passagetrack.py` today) |
| created_at | TEXT | | when built | `passage.build` (stale, ditto) |
| deleted | INTEGER | dflt 0 | soft delete | |

## 8. `cfg_enum`

| name | value | ordinal | inactive |
|---|---|---|---|
| `passage_rule` | char-continuity | 0 | 0 |
| `passage_rule` | maximal | 1 | 0 |
| `passage_source` | passage-build | 0 | 0 |
| `passage_source` | single-verse-emergent | 1 | 0 |
| `passage_debate_status` | scaffold | 0 | 0 |
| `passage_debate_status` | filled | 1 | 0 |
| `config_module` | passage | 5 | 0 |

All still `inactive=0` — i.e. these enum vocabularies are still "live" by config even though the
only columns that would ever hold `passage_rule`/`passage_source` values (`passage.rule`,
`passage.source`) are never populated by anything running today.

## 9. `cfg_table`

| name | grain | use |
|---|---|---|
| `passage` | one row per passage — a reading frame (global, per book) | extends a characteristic's context to adjacent verses for assessing movement/process/qualifying spans; NOT a thematic unit |
| `verse_passage` | one row per verse-in-a-passage — passage membership (L4b), keeps the raw verse pristine | which passage a verse belongs to; a verse is in at most one passage |

Both descriptions are the *original* (candidate-driven) framing from before the 2026-07-27
repurposing to a completion-tracking record — not updated to describe the current use.

## 10. `cfg_unique`

| table_name | col | ordinal |
|---|---|---|
| `passage` | book | 0 |
| `passage` | start_chapter | 1 |
| `passage` | start_verse | 2 |
| `passage` | end_chapter | 3 |
| `passage` | end_verse | 4 |

Composite uniqueness on (book, start_chapter, start_verse, end_chapter, end_verse) — this is what
`passagetrack.py:_find_live_passage()` relies on to upsert rather than duplicate a range.

## 11. `cfg_change_detail` (audit trail, not a live rule — included for completeness)

8 rows touch a passage-related key/table, all *after* the 2026-07-26 retirement:

| applied_at | table_name | op | what changed |
|---|---|---|---|
| 2026-07-23T08:15:21Z | `cfg_work_package` | update | `passage-quality.ps_script` path corrected |
| 2026-07-27T05:20:38Z | `cfg_setting` | update | `method.interpretation_questions_path` v1.0→v1.1 |
| 2026-07-27T09:02:58Z | `cfg_setting` | update | `method.passage_read_guidance_path` v1.2→v1.3 |
| 2026-07-27T09:03:58Z | `cfg_setting` | update | `method.interpretation_questions_path` v1.1→v1.2 |
| 2026-07-28T16:02:25Z | `cfg_setting` | update | `method.passage_read_guidance_path` v1.3→v1.4 |
| 2026-07-28T16:02:26Z | `cfg_setting` | update | `method.interpretation_questions_path` v1.2→v1.3 |
| 2026-07-29T06:32:35Z | `cfg_setting` | insert | `governance.verse_gap_by_design` added |
| 2026-07-29T06:32:47Z | `cfg_setting` | insert | `report.verse_gap_note` added |

All recent activity is **method-doc version bumps and the verse-gap ruling** — nothing has touched
a boundary/sizing rule since the 2026-07-26 retirement.

## 12. Tables checked with no passage-related rows

`cfg_api`, `cfg_book_order`, `cfg_candidate_rule`, `cfg_change_log`, `cfg_connection`, `cfg_meta`,
`cfg_status_flow` — searched, zero hits.

---

## Observations for the review (facts only, no action taken)

- **Stale-but-live metadata**: `cfg_column` (rule/source/filled_by on `passage`), `cfg_table`
  (both tables' grain/use text), and `cfg_enum` (`passage_rule`/`passage_source`) all still
  describe the pre-2026-07-26 candidate-driven regime and were never updated when that regime was
  retired or when the tables were repurposed 2026-07-27. They are `inactive=0` (i.e. "current" by
  the config's own flag) but describe a mechanism that no longer runs.
- **`cfg_on_fail`'s `findings-rejected` message** ("...needing the rule revisited") is worded for a
  rule that no longer exists.
- **`cfg_write_grant` is internally consistent** with the current regime: only `report.
  verse_span_meaning` and `report.passage_debate` may write `passage`/`verse_passage` today;
  `passage.build`'s grants are correctly `inactive=1`.
- **No config item anywhere defines how large a passage/debate range should be** or where one
  should end — that is a judgement call made per-debate, not backed by any `cfg_*` row, active or
  inactive-but-referenced.
