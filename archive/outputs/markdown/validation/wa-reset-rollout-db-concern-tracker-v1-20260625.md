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
| 2026-06-25 | (c) L1-reset increment 2: **fidelity fixes baked** into `_ve_engine_v2.derive()` (object-fidelity · from-source incl. `H9006` · tense · quality-bearer · operation) + read-only before/after validation on 6 reviewed + 5 new verses (`_read_ve_pilot_compare_20260625.py`) | unchanged | — | — | **no DB write** (engine code + read-only compare only); 6 reviewed errors corrected (2 new mis-fires caught + fixed in 2nd pass); validation: `wa-ve-reset-fidelity-fixes-validation-v1-20260625.md` |
| 2026-06-25 | (c) L1-reset increment 3: **remaining mechanical deltas baked** (possessive-object · intransitive-stative suppression · instrument/dia · purpose/telos · adjacency-isolable; transition deliberately NOT baked → synthesis). Crash-tested over **all 1,686 M12 units → 0 errors** | unchanged | 0 | — | **no DB write** (read-only derive + harness); several mis-fires caught+fixed (inline-prefix `_gov`, degenerate transition); validation §5 updated. **Next = wire runner to persist new fields + isolable adjacent-ref, then gated sweep** |
| 2026-06-26 | **RESET CORPUS SWEEP — first DB WRITE** (researcher-directed while out). Wired the 7 new reset fields into the runner `_apply_generate_ve_lexical_v2.py` (`VE_MAP` ve_nr 23–29: from-source · instrument · purpose · quality-bearer · operation · isolable · discovery; tiers PROVISIONAL best-fit) + extended `narrate()` + bumped STAMP→2026-06-26. Ran `--live` over **all 42,076 units → 40,308 generated** (1,768 T2-grammatical skipped), **452,885 ve_lexical rows**, **31,908 l2_meaning narrations regenerated**. | 231890 (unchanged) | 0 | **none** | **VALIDATED CLEAN.** Fresh backup `backups/bible_research_pre-reset-sweep_20260626.db`. read-API overlays **all preserved** (val 30571·div 14646·obj 12104·cause 7743·loc 1336 — unchanged); faculty-map-v1 preserved (26386) + 2,819 v2 faculty **gap-fill on unmapped terms, 0 true duplicates**; new-field rows present (from-source 8831·instrument 715·purpose 6338·quality-bearer 2088·operation 634·isolable 5399·discovery 40308); l2_meaning active stable 32005 (old soft-deleted). Integrity = before-start baseline exactly. Assessment: `wa-reset-sweep-outcome-and-honest-assessment-v1-20260626.md`. |

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
