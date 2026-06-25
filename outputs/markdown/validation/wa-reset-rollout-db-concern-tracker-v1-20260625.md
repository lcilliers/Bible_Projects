# Reset roll-out — DB concern tracker + check log (living)

- **File:** wa-reset-rollout-db-concern-tracker-v1-20260625.md · **2026-06-25 · Author:** Claude Code.
- **Purpose (researcher directive d):** check the database **before start, at intervals**, and **track concerns** through the reset roll-out (the M12–M20 embed and beyond). The governing rule **still stands: all results, all of the baseline, all interim artifacts must be in the DB** (single source of truth) — chat/files are alerts + workings; the DB is the record.

## Safeguards in place (2026-06-25, before start)
- **KEEP milestone backup (local):** `backups/bible_research_KEEP-RESET-baseline-changeover_20260625.db` (498 MB) — in the manual-milestone dir, not auto-rotated.
- **KEEP backup (NAS, off-machine):** `bible_research_20260625T060950Z_KEEP-RESET-baseline-changeover.db` — verified on NAS. *(Note: the NAS daily folder rotates at retention=10; the durable keep is the local milestone copy + the full-folder mirror.)*
- **git:** working tree clean; **pushed to origin** (`…→239c9e1`), 79 commits up to date on GitHub.
- **faculty pre-reset backup:** `ve_lexical_faculty_backup` table (the pre-lemma-map faculty rows) retained in-DB.

## Before-start integrity baseline (`scripts/_integrity_full_check.py`, 2026-06-25)
```
total_rows 231890 · orphan_file_id 0 · orphan_term_inv_id 0 · orphan_book_id 0
null_file_id 0 · null_book_id 1 · null_chapter 0 · null_verse_num 0
null_term_inv_id 0 · null_term_id 1 · null_reference 0 · null_testament 0 · null_verse_text 0
span_strong_match_null 3258 · target_word_null 3198
```
**Read:** clean — 0 orphans, 0 nulls on key fields; the 2 stray single nulls + the span/target_word nulls are **pre-existing known gaps**, not new corruption. This is the baseline to compare interval checks against.

## Interval check log
> Run `_integrity_full_check.py` (and the relevant `_check_*`) before/after each DB-writing step of the roll-out; record deltas vs the baseline here.

| When | Step | total_rows | orphans | new nulls vs baseline | notes |
|---|---|---|---|---|---|
| 2026-06-25 | before start (baseline) | 231890 | 0 | — | healthy |
| 2026-06-25 | (c) L1-reset increment 1: `discovery` field added to engine + piloted M12 (read-only) | unchanged | — | — | no DB write (pilot via derive() print); engine confirmed functional + lookout surfaces gaps |

## Concern register
> Any anomaly, unexpected delta, or risk surfaced during the roll-out. Each: concern · when · severity · status.

| # | Concern | When | Severity | Status |
|---|---|---|---|---|
| _none yet_ | | | | |

## Standing rules for the roll-out
- **All-in-DB:** every result / baseline value / interim artifact lands in the DB (the movement layer, the lexical considerations, the pointers, the registers). Files are workings + alerts only.
- **Before any DB write:** dry-run → inspect → live; integrity check after; log the delta here.
- **Soft-quarantine, never hard-delete** the set-aside superstructure (provenance retained).
- **Interval cadence:** check before start (done), after each generator build/run on a cluster batch, and at each phase boundary (dissection tune · synthesis-B build · pilot · sweep).

*DB concern tracker — safeguards triple-covered; before-start integrity clean; the all-in-DB rule stands; checks + concerns logged here through the roll-out.*
