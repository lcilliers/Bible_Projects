# SESSION LOG — 2026-08-11 — old-system cluster mapping built and corrected; `word_registry`/`word_strong` false alarm run to ground; candidate-cycle cleanup gap found and fixed; `blindness` built out; session closed with two forks queued

Two main threads, closed deliberately at the researcher's instruction to contain scope. Grouped in
the order they happened.

## 1. Old-system (`bible_research.db`) cluster allocation mapped onto IBA's registry

Researcher: the old project/DB has a table allocating Strong's numbers to clusters (M-codes,
`mti_terms.cluster_code`) — map IBA's word/Strong's data onto it.

**First pass** (word-level, "dominant cluster" reduction): joined `word_strong` (4,848 active rows,
178 words) against `mti_terms.cluster_code` (aggregating the 1,782 duplicate-`strongs_number` groups
in the old DB — a known unresolved issue, OT-DBR-009 — by unioning distinct codes rather than picking
one), collapsed each word down to its single most-common old cluster + a ranked breakdown of every
cluster its Strong's touched. `word-strong-cluster-mapping-20260810.md/.csv`.

**Corrected same day**, researcher: "that is not what I asked for... accepting that a strongNumber
can be mapped to more than one cluster" — the dominant-cluster reduction was the wrong shape. Rebuilt
flat: every row of the `word_registry.csv` export against every old cluster it hits, one output row
per hit, unmapped rows kept with blank cluster fields rather than dropped (so the file is a complete
accounting, not a filtered match-only list). `word-registry-strong-cluster-mapping-20260811.md/.csv`
— 4,972 rows. Coverage: 2,994 of 4,849 registry rows produce ≥1 old-cluster match; of 3,447 distinct
Strong's numbers, 1,771 map to exactly one old cluster, 71 to two (never more), 1,605 to none.

Added `stepTransliteration` (from IBA's own `strong` table, not reconstructed from the old DB's messy
free-text `cluster.gloss` blob, which was checked and found to be a single flattened "gloss
(transliteration), gloss (transliteration), ..." string per cluster, not structured data).

**30 blank-`strongNumber` rows investigated, not left as a loose end.** Traced to two distinct real
causes, not one: (a) `blindness` (word_registry id 183) genuinely has **zero** `word_strong` rows at
all; (b) the other 29 are real `word_strong` rows (e.g. `contempt`→`H2048`/`H5607`) whose Strong's
number has **no row in IBA's own `strong` reference table** (15,291 rows) — confirmed by direct
lookup, not deleted, never loaded. Cross-checked all 29 against the old DB: 28 don't exist there
either; one (`H5258`) does, `status=extracted`, not deleted, `cluster_code=T2`. This 30-row
investigation is what led directly into thread 2.

`cluster-master-20260811.csv` — the old DB's 49-row `cluster` table (M01–M47+FLAG+T2), exported for
reference alongside the mapping.

## 2. `word_registry`/`word_strong` "false alarm" run to ground; candidate-cycle cleanup gap found

Researcher, looking at the (misleadingly-named) `word_registry.csv` export, concluded the table had
degenerated into a Strong's table (the same failure the *old* project's own `word_registry` suffered)
and asked to (b) validate `word_strong` vs `word_registry`, fixing any real gap, then (c) reset
`word_registry` to a plain ~200-word list with no Strong's columns.

**Checked the live table directly instead of trusting the export.** `word_registry`: 179 rows, 179
distinct words, zero duplicates, columns `id/word/source/status/created_at/deleted` only — no
Strong's column ever existed. `word_strong`→`word_registry` integrity: zero orphaned junction rows.
**The table was never broken.**

**Root cause: `registryreport.py`'s two CSVs were named backwards relative to content.** The LEFT
JOIN pairing (word×Strong's, one row per pair) was named `word_registry.csv` — reading exactly like a
table dump, which is precisely the false read both the researcher and Claude independently made. The
genuine one-row-per-word dump was named `registry.csv`.

**Fixed via `configmaint.propose`** (2 renames, approved on the researcher's chat instruction,
`cfg_change_detail` logged): pairing export `word_registry`→`word_registry_strong_pairing`; plain
listing `registry`→`word_registry`. Code (`registryreport.py`) updated to match, old orphaned
`registry.csv` archived (not deleted), report regenerated (`registry-v7-20260811.md`), verified live.

**Second finding, from re-checking the whole pipeline per the researcher's own instruction (the
"isolation and removal of the candidate cycle was incomplete" ask):** `New-Word.ps1` carried a
leftover "coupling" call into `set-candidates`/`candidate.seed` after every word build — dead code
from before that work package's full, deliberate retraction (`retract_candidate_system.py`,
escalations #306/#310, 2026-07-23). The config-side retraction was thorough and correctly enforced
(`run.py`'s inactive-package check is what turned this into the traceback seen live during the
`blindness` build); the code-side caller was simply never cleaned up, firing on every word build since
2026-07-23. Removed the block entirely (not gated — permanent retraction, live replacement since
2026-08-05).

Audited the rest of the active word/strong→verse-lexical path the same way (grepped every active
handler + gated `.ps1` for `candidate`/`span_candidate`/`candidate_seed`): confirmed
`passage.build`/`passage.validate`/`lexical.build` touch none of it — only comments/docstrings cite
the old system for context. Real current chain: `new-word` (raw) → *(researcher-dictated,
JSON-payload)* `operations-ingest` (`hib.set`→`phenomenon.set`→`operation.set`→`closing.set`) →
`build-passages` (off `verse_hib`, redefined 2026-08-05) → `passage-quality` → `verse-lexical`
(book/range-scoped, confirmed independent of passage/HIB entirely). One soft item flagged, not
touched: `SpanAnalysis-Report.ps1` (still active) reports `span_candidate` framed as "confirmed vs
candidate" — accurate but describing a now-frozen category; researcher's call whether to reword.

**`blindness` built out** (researcher: "~16 related words in strong with approx 300 verses... never
built... must be built using the App methods"). `New-Word.ps1 -Word blindness`: 16 seed Strong's
(matches the researcher's own STEP check exactly), 277 `strong_verse` rows (~ the "~300" estimate),
`raw-complete`, validated. Deliberately not taken further into `operations-ingest`/`build-passages`/
`verse-lexical` — real, researcher-paced work under the still-being-dictated v4 method, not
auto-continued.

**Correction found immediately after, recorded honestly, not silently left implied-fixed:** the
`word_registry`/`registry` rename resolved one instance of a pre-existing `configmaint.validate`
coherence gap (`cfg_report_csv_table.table_name` must name a real table — `registry` didn't, already
flagged-not-fixed in the 2026-08-10 log) but **relocated it, did not eliminate it** —
`word_registry_strong_pairing` isn't a real table either, and now fails the identical check. Verified
directly against `cfg_table`. Net position unchanged from before this session: one flagged row, just a
different one. Real fix needs a SQL `VIEW` + migration, correctly out of scope here.

## Session closed — two forks queued, not started

Researcher: contain scope, close this session, mark two threads for future sessions rather than
continue now.

- **Fork (a) — complete the old-system cluster comparison.** Checkpoint: `word-registry-strong-
  cluster-mapping-20260811.csv` (4,972 rows) + `cluster-master-20260811.csv` (49-row old `cluster`
  table), both live in `iba/app/reports/`. Scope beyond that checkpoint not yet defined.
- **Fork (b) — raw data integrity vs. completed analysis.** Re-check what `raw-complete` actually
  guarantees against what the full pipeline needs downstream, and what that implies for any word
  marked `raw-complete` but never carried further. Named test case: **`blindness` should fall out of
  that check as NOT complete** (raw layer only, §2 above) — how many other `raw-complete` words are in
  the same state is itself part of fork (b), not counted this session.

## Explicitly not included in this commit

- Any further build of `blindness` past the raw layer (operations-ingest/build-passages/verse-lexical)
  — fork (b)'s territory, not this session's.
- The `cfg_report_csv_table` coherence gap's actual fix (a SQL `VIEW` + migration) — flagged twice now
  (2026-08-10, 2026-08-11), still correctly out of scope for a `configmaint.propose` single-row change.
- `SpanAnalysis-Report.ps1`'s "confirmed vs candidate" framing — flagged, researcher's call.

## Files touched (this commit)

**Modified (code):** `iba/app/lib/registryreport.py` (CSV `row_filter` keys + docstring),
`iba/app/ps/New-Word.ps1` (dead candidate-seed coupling block removed), `iba/app/BUILD.md` (§100,
§101).

**Config (DB), via `configmaint.propose`, approved and applied:** `cfg_report_csv_table` × 2 rows
renamed (`word_registry`→`word_registry_strong_pairing`; `registry`→`word_registry`).

**Data (DB), via `New-Word.ps1` (sanctioned pipeline, not raw SQL):** `word_registry` id 183
(`blindness`) → `raw-complete`; +16 `word_strong` rows; +277 `strong_verse` rows.

**Reports/artefacts generated this session, kept live:** `iba/app/reports/word-registry-strong-
cluster-mapping-20260811.{md,csv}`, `iba/app/reports/cluster-master-20260811.csv`,
`iba/app/reports/registry-v7-20260811.md` + `export/word_registry.csv` +
`export/word_registry_strong_pairing.csv`.

**Reports archived (redundant, superseded same day):** `iba/app/reports/archive/word-strong-cluster-
mapping-20260810.{md,csv}` (word-level "dominant cluster" version, superseded by the flat mapping
above); `iba/app/reports/export/archive/registry-superseded-by-rename-20260811-060816.csv` (old
mis-named export, superseded by the CSV rename).

## Next

Fork (a) and fork (b) above — both queued for a future session, neither started. No other open item
from this session beyond the two already-flagged, correctly-out-of-scope items (`cfg_report_csv_table`
coherence gap; `SpanAnalysis-Report.ps1` framing).
