# The IBA `passage`/`verse_passage` system — retirement record

> One-off historical record, not a recurring report. Written 2026-07-26, before any data was
> touched, so what existed and what it produced is not lost. `governance.oneoff_report_dir`
> (`iba/app/reports/`) — same convention as every other one-off investigation in this app.

## Why

Researcher's own words, 2026-07-26: *"the past use, and rules have moved on. The assembly of the
passages is no longer based on the same premise. I do see a future for the passage tables, but is
still busy working out how it would fit together. However the current data is no longer relevant
and is getting in the way. The new way forward will emerge as we go on. For now, I simply want to
record the passages that have been generated, and the outcomes of those passages. There is nothing
to migrate from the old to the new. The effort of reconciling the old data with potential new data
is not worth it."*

This directly answers the open question three separate `passage.validate` escalations (`#195`,
`#256`, `#262` — full text below) had been asking, unresolved, since 2026-07-21: *"is this
distribution acceptable as the char-continuity rule stands, or does the passage rule need
revisiting?"* — yes, it needs revisiting; the whole assembly premise is superseded, not just the
threshold.

## What this system was

`handlers/passage.py`'s own docstring: *"A passage's sole purpose is to extend a characteristic's
context to its adjacent verses so movement/process/qualifying spans can be assessed with that
context — NOT a thematic unit. Boundaries come from the candidate stamp: a maximal run of
consecutive same-chapter candidate-bearing verses, broken when consecutive verses stop sharing a
candidate base-Strong's (char-continuity) unless -Rule maximal."*

So passage assembly was **entirely candidate-driven** (`span_candidate`, itself produced by the
`set-candidates` work package). `set-candidates`/`candidate-quality`/`candidate-curation`/
`seed-candidate-report` were already retracted 2026-07-23 (GOVERNANCE.md §15D — "a substantial mess
up over the past few days," retracted together as one surface). `build-passages`/`passage-quality`
were NOT retracted at that time (a real inconsistency: passage kept running config-live on top of a
now-frozen, no-longer-maintained candidate stamp) — closed now, in this pass.

## The data, as it stood before retirement (verbatim CSV export preserved)

- **`passage`**: 18,504 rows (65 books)
- **`verse_passage`**: 24,763 rows
- Full verbatim export (every column, every row, both tables): [`passage-retirement-export-20260726/`](passage-retirement-export-20260726/) (`passage.csv`, `verse_passage.csv`) — the actual historical record, not just this summary.

### Per-book breakdown (passages / verses-in-a-passage), all `char-continuity` rule except where noted

| book | passages | verses |
| --- | --- | --- |
| Ps | 2015 | 2305 |
| Isa | 928 | 1203 |
| Jer | 900 | 1270 |
| Job | 894 | 965 |
| Gen | 819 | 1279 |
| Ezek | 745 | 1102 |
| Prov | 685 | 782 |
| Num | 626 | 907 |
| Exod | 621 | 1008 |
| Luke | 607 | 693 |
| Deut | 605 | 850 |
| Acts | 587 | 633 |
| Matt | 519 | 601 |
| 2Chr | 501 | 719 |
| Lev | 464 | 764 |
| 1Sam | 449 | 750 |
| John | 429 | 527 |
| 1Kgs | 400 | 680 |
| 2Kgs | 372 | 636 |
| 2Sam | 371 | 598 |
| Judg | 348 | 562 |
| Mark | 329 | 384 |
| 1Chr | 320 | 424 |
| Josh | 293 | 396 |
| Rom | 276 | 363 |
| Rev | 243 | 294 |
| 1Cor | 220 | 276 |
| Heb | 193 | 222 |
| Dan | 189 | 293 |
| 2Cor | 168 | 194 |
| Hos | 162 | 188 |
| Neh | 157 | 256 |
| Zech | 136 | 198 |
| Eccl | 136 | 214 |
| Lam | 120 | 143 |
| Eph | 109 | 119 |
| Esth | 108 | 154 |
| Ezra | 103 | 134 |
| Amos | 100 | 130 |
| Mic | 85 | 98 |
| Gal | 82 | 98 |
| 1Tim | 78 | 86 |
| 1Pet | 77 | 92 |
| Jas | 74 | 85 |
| Phil | 73 | 78 |
| Col | 69 | 72 |
| 1Thess | 62 | 72 |
| 2Tim | 61 | 65 |
| 1John | 57 | 93 |
| Song | 56 | 83 |
| Joel | 53 | 66 |
| Hab | 50 | 54 |
| Zeph | 44 | 50 |
| Nah | 42 | 44 |
| 2Pet | 41 | 46 |
| Titus | 37 | 37 |
| Ruth | 34 | 74 |
| 2Thess | 33 | 37 |
| Jonah | 31 | 48 |
| Mal | 23 | 53 |
| Hag | 23 | 35 |
| Jude | 21 | 23 |
| Obad | 16 | 19 |
| Phlm | 15 | 17 |
| 3John | 12 | 13 |
| 2John | 8 | 9 |

Data span: earliest `passage.created_at` 2026-07-19T06:29:06Z, latest 2026-07-22T19:44:22Z — nothing
written since; the surface was already effectively stalled 4 days before this retirement.

## The outcomes — what the quality check found, never acted on

`passage.validate`'s finding, raised identically three times (2026-07-21, twice more 2026-07-22),
none of them ever answered:

> Passage distribution across all books: 18,571 passages, average 1.34 verses/passage, 15,027 (81%)
> are single-verse. `passage.review_over` only flags passages that are too LONG — nothing flags
> this. Is this distribution acceptable as the char-continuity rule stands, or does the passage
> rule need revisiting?

(The 18,571/15,027 figures are from the escalation's own run-time count, taken before the final
2026-07-22 `build-passages` run for Prov; the 18,504-row figure above is the table's final resting
state after that run.)

| escalation | run_id | raised | state after this session |
| --- | --- | --- | --- |
| `#195` | `RUN-20260721_163620_949-PASSAGE-QUALITY` | 2026-07-21 | answered `reject` — see below |
| `#256` | `RUN-smoketest-0b-passage` | 2026-07-21 | answered `reject` — see below |
| `#262` | `RUN-20260722_204223_295-PASSAGE-QUALITY` | 2026-07-22 | answered `reject` — see below |

**Resolution**: answered `reject` (closest fit among approve/reject/revise for a dispatcher-tied
escalation — not "the finding was wrong," but "no action needed on the char-continuity threshold
itself, because the system that produced it is being retired, not tuned"), comment: *"superseded —
passage system retired 2026-07-26, see
reports/passage-system-retirement-record-20260726.md. Not a rule-tuning decision; the whole
assembly premise has moved on."*

## `build-passages` run history (all completed runs, char-continuity vs. maximal comparison)

| run_id | started | outcome |
| --- | --- | --- |
| `RUN-20260718_103244_008-BUILD-PASSAGES` | 2026-07-18T09:32:44Z | 56 passage(s) over 57 candidate verse(s) in Prov (char-continuity) |
| `RUN-MAX-TEST` | 2026-07-18T09:33:20Z | 53 passage(s) over 57 candidate verse(s) in Prov (maximal) |
| `RUN-RESTORE` | 2026-07-18T09:33:20Z | 56 passage(s) over 57 candidate verse(s) in Prov (char-continuity) |
| `R2` | 2026-07-18T09:33:42Z | 81 passage(s) over 89 candidate verse(s) in Ps (maximal) |
| `R3` | 2026-07-18T09:34:55Z | 87 passage(s) over 89 candidate verse(s) in Ps (char-continuity) |
| `RUN-20260722_204421_560-BUILD-PASSAGES` | 2026-07-22T19:44:22Z | 685 passage(s) over 782 candidate verse(s) in Prov (char-continuity) |

## What was retired (config), full inventory

Per `migration/retract_passage_system.py` (mirrors `retract_candidate_system.py`'s shape,
GOVERNANCE.md §15D):

- **Data**: `passage` (18,504 rows), `verse_passage` (24,763 rows) — soft-deleted (`deleted=1`),
  not physically dropped; the CSV export above is the durable record.
- **Work packages**: `build-passages`, `passage-quality` → `inactive=1`
- **Steps**: `passage.build`, `passage.validate` → `inactive=1`
- **Settings** (module `passage`, 5 rows): `passage.default_rule`, `passage.cross_chapter`,
  `passage.min_shared_strongs`, `passage.review_over`, `passage.quality_report_path` → `inactive=1`
- **Report registration**: `cfg_report` (`passage.validate`), its 2 `cfg_report_section` rows
  (`dist`, `by_book`) → `inactive=1`
- **`cfg_on_fail`** (4 rows): `passage.build`/`no-candidates`, `passage.validate`/
  `findings-rejected`, `passage.validate`/`needs-review`, `passage.validate`/`needs-revision` →
  `inactive=1`
- **`cfg_write_grant`** (2 rows): `passage.build` → `passage`, `passage.build` → `verse_passage` →
  `inactive=1`

**Not touched**: `span_candidate` (83,914 rows) and the rest of the candidate surface — already
covered by the 2026-07-23 candidate retraction (§15D); out of scope for this pass, which is
specifically the passage tables the researcher named.

## What comes next — explicitly NOT decided here

No new passage design is proposed, assumed, or scaffolded in this pass. The researcher is still
working out how a future passage concept fits together (possibly related to the main Bible-study
programme's newer, unrelated "passage = maximal run of consecutive verses" verse-first concept —
`verse.passage_id`, a different table in a different database — but that reconciliation is
explicitly not being attempted now either). This record exists so that whenever the new design
does emerge, the old data's shape, volume, and the exact question that stalled it are still
findable — without carrying the retired schema/config forward as if it were still live.
