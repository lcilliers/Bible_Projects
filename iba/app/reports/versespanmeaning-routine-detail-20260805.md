# `report.verse_span_meaning` — full routine detail

Verified live against `iba/app/db/iba.db` schema + `iba/app/lib/versespanmeaningreport.py` +
`iba/app/handlers/reports.py` + `iba/app/handlers/raw.py` + `cfg_work_package`/`cfg_step`/
`cfg_setting`, 2026-08-05. Scope: **this one routine only** — not `report.passage_debate`, though
that report reuses several of this routine's functions (noted where relevant, not expanded).

## 1. What it is, and how you currently reach it

- **Step name:** `report.verse_span_meaning`. **Handler:** `handlers/reports.py:
  verse_span_meaning_report`. **Algorithm:** `lib/versespanmeaningreport.py` (`write_report` +
  helpers). **PS entry point (registered, live):** `Chapter-Generate.ps1 -Book <b>
  -Chapters/-Range <r> -BookLabel <l>` — chained work package `chapter-generate`, ordinal 0 (this
  step), ordinal 1 `report.passage_debate`. One `-RunId` covers both.
- **Not** reachable via the old standalone `VerseSpanMeaning-Report.ps1` any more — that work
  package (`verse-analysis-report`) and its `cfg_step` row were deliberately retired 2026-08-02
  (`BUILD.md` §54) purely to resolve a step-name-registered-twice violation once the step was
  folded into `chapter-generate`; the underlying handler/algorithm is unchanged and still live, only
  the entry point moved. Calling the retired PS script now refuses: *"work package '...' is
  inactive (retired) or unknown — refusing to run."*
- Can also be invoked directly, one step at a time, via `python -m iba.app.run chapter-generate
  --step report.verse_span_meaning ...` if you don't want `report.passage_debate` to fire in the
  same call.

## 2. What is config-driven vs. what is code — direct answer to "presumed covered by configs"

**Partially.** Config rows govern *metadata* — where output goes, what it's named, fixed text, and
a couple of on/off switches. The actual **meaning-resolution algorithm** (which table wins, when a
code counts as ambiguous, when to burn a live STEP call) is **plain Python logic in
`versespanmeaningreport.py`, not data in any `cfg_*` table.** No `cfg_setting` row encodes "try
exact-variant first, fall back to base" or the ambiguity heuristic — that's hardcoded control flow.

| Governed by config | `cfg_setting` key | Governed by code only |
| --- | --- | --- |
| Output folder | `report.verse_analysis_output_dir` (`iba/app/verse-analysis`) | Exact-variant vs. base-fallback resolution order |
| Output filename pattern | `report.verse_analysis_output_pattern` (`{book}-{range}-verse-span-meaning.md`) | Sibling-code lookup (`sibling_variant_codes`) |
| Verse-gap inline note text | `report.verse_gap_note` | Ambiguity test itself (`gloss_supported_by_tree` — shared-token heuristic) |
| Strong's base/sub-letter split regex | `raw.strong_base_pattern` (`^([HG]\d+)([A-Z]?)$`) | Particle exclusion from coverage stats (`is_particle` check) |
| Whether STEP is mandatory | `step.required_for_runs` (default `true`) | Compound-tag splitting (space-joined `strong_variant` codes) |
| Whether a coverage gap auto-backfills before render | `report.auto_backfill_before_render` (default `true`) | Live-STEP-result caching per run (`live_cache` dict, not persisted) |
| Section headings/order | `cfg_report_section` rows for this step | Greek-only branch for LSJ/Mounce |

Also read (not this routine's own settings, shared elsewhere): none beyond the table above — this
routine reads no other `cfg_setting` rows.

## 3. DB tables **read**

| Table | Columns read | Filter |
| --- | --- | --- |
| `verse` | `id, osisId, reference, text` | `osisId LIKE '{book}.%'`, `deleted=0`, then chapter/verse parsed from `osisId` and range-filtered in Python |
| `span` | `position, surface, strong_variant, morph_code, is_particle` | `verse_id=?`, `deleted=0`, `ORDER BY position` |
| `strong` | `strongNumber, language, stepGloss` | `strongNumber=?` (per code, one lookup per span-code) |
| `strong_meaning_parsed` | `gloss` | `strong_variant=? ORDER BY sort, id` (exact-variant pass); falls back to `lemma_key=? AND strong_variant=?` both `=base` (legacy-only pass) |
| `strong_lsj_parsed` | `gloss` | `strong=? AND row_type='lookup' ORDER BY id` — **Greek codes only** |
| `strong_mounce_parsed` | `mounce_parsed` | `strong=? ORDER BY id` — **Greek codes only** |
| `strong` (again) | `strongNumber` | sibling lookup: `strongNumber = base OR strongNumber LIKE 'base_' AND strongNumber != code` — feeds the ambiguity check |

Not read by this routine at all: `strong_lexicon` (raw HTML — upstream of the parsed tables, not
touched here), `strong_sense`, `strong_related`, `lemma_inventory`, `strong_verse`,
`strong_meaning_tree` (the raw/unparsed sense text — superseded here by `strong_meaning_parsed`).

## 4. DB tables **written** — this routine has real side effects, it is not purely read-only

Two separate write paths fire on a normal call:

**(a) Coverage backfill, before rendering** (`report.auto_backfill_before_render`, default on).
For every span in the requested range whose `strong_variant` code has no `strong` row yet, calls
the same pull `raw.backfill_meaning` does (`handlers/raw.py:backfill_meaning_for`):
1. `handlers/raw.py:detail_one` — one live STEP `call2_getInfo` per missing code, writes:
   - `strong` (new row: `strongNumber, accentedUnicode, stepGloss, stepTransliteration, language,
     count, freqList, created_at, deleted`)
   - `strong_sense` (new row: `strong, head, is_own_lemma, deleted`)
   - `strong_meaning_tree` (new rows, one per sense, only if no row already exists for that exact
     `(lemma_key, strong_variant)` — never overwrites a sibling's own tree)
   - `strong_lexicon` (new row, if STEP returned `lsjDefs`/`shortDefMounce`: `strong, lsj, mounce`)
2. `lib/lexicon.py:rebuild_parsed_tables` — **clears and rebuilds `strong_meaning_parsed`,
   `strong_lsj_parsed`, `strong_mounce_parsed` in full**, deterministically, from the current
   `strong_meaning_tree`/`strong_lexicon` content (no network call). This is a full rebuild of all
   three tables every time it runs, not an incremental append — safe (source data persists) but
   means a backfill triggered by one book's render touches these three tables' entire content, not
   just the new codes.
3. `lib/lexicon.py:fetch_related_for` — one live STEP call per newly-registered code, writes new
   `strong_related` rows only for those codes (`clear_first=False` — does not touch existing rows).

**(b) Passage tracking, after rendering** (`lib/passagetrack.py:record_extract`, always fires):
- `passage` — upserts one row per distinct book+range identity: `book, book_label,
  anchor_verse_id, start_chapter, start_verse, end_chapter, end_verse, ref, verse_count, rule,
  source, needs_review, created_at, deleted, verse_span_meaning_path, verse_span_meaning_written_at`.
  This is a **status/pointer record** ("this range's extract lives at this path, written at this
  time") — it does **not** store the per-span meaning content itself.
- `verse_passage` — one row per verse in the range: `passage_id, verse_id, is_anchor, created_at,
  deleted`.

Net: the routine is not a pure lookup. Running it can silently pull live data from STEP, permanently
add rows to `strong`/`strong_sense`/`strong_meaning_tree`/`strong_lexicon`/`strong_related`, rebuild
three parsed tables in full, and always upserts a `passage`/`verse_passage` tracking row — all
before the MD file is even written.

## 5. Processing rules — step by step, per call

Given `-Book`, one of `-Chapters`/`-Range`, optional `-BookLabel`:

1. **STEP preflight.** `Step(cfg).up()`. If unreachable and `step.required_for_runs=true` (the
   default), the whole run refuses (`StepUnavailable` → `fail("unreachable", ...)`). If the setting
   is `false`, proceeds STEP-down; any span needing live disambiguation later gets a DB-only note
   instead of a resolved sense.
2. **Coverage backfill** (§4a), if `report.auto_backfill_before_render` is true — runs first, so
   the render below sees fresh data for any code that was missing.
3. **Fetch verses** in range (`fetch_verses`): pulls all `verse` rows for the book, filters to
   `lo..hi` chapters (and `verse_lo..verse_hi` if `-Range` was used) by parsing `osisId`
   numerically — table-id order is not used, reading order is chapter/verse order.
4. **Detect verse gaps** (`detect_verse_gaps`): DB-only, no STEP. Per chapter actually touched,
   finds a leading gap (chapter's first fetched verse isn't verse 1, or isn't the `-Range` start)
   and any internal gap between two fetched verses. Cannot detect a chapter's own trailing missing
   verse(s) (no external verse-count reference exists in `iba.db`) — a known, accepted limitation,
   not a bug (`governance.verse_gap_by_design`).
5. **Merge verses + gaps** (`merge_verses_and_gaps`) into one reading-order sequence. A gap renders
   the `report.verse_gap_note` template inline (with `{ref}` filled) and the loop moves to the next
   available verse — not an error, not a stop.
6. **Per verse:** fetch its `span` rows (`fetch_spans`, ordered by `position`). For coverage
   accounting, only `is_particle=0` spans count toward `per_chapter_total`/`per_chapter_covered`.
7. **Per span, resolve meaning** (`meaning_for` → `meaning_for_code` per code in
   `strong_variant.split()` — a space-joined `strong_variant` is a compound STEP tag, each code
   resolved independently and rendered as `**CODE**: text` when there's more than one):
   - a. `strong` row for the exact code — if none, meaning is `(not yet registered)`, "not covered."
   - b. Anchor line: `stepGloss: {strong.stepGloss or '(none)'}`.
   - c. `strong_meaning_parsed` rows for the **exact** `strong_variant`, ordered by `sort` — this is
     "exact_variant" coverage. If none exist (pre-split legacy data only), falls back to rows keyed
     by the **base** code (`lemma_key=base AND strong_variant=base`).
   - d. **Ambiguity check** — only reachable via the base-fallback path (never on an exact-variant
     hit): if sibling sub-lettered codes sharing the same base exist
     (`sibling_variant_codes`), and the fallback meaning text does **not** share real vocabulary
     with this code's own `stepGloss` (`gloss_supported_by_tree` — lowercases, strips stopwords,
     checks for any shared token ≥3 chars), it's flagged `[AMBIGUOUS - base shared with ...]` and a
     **live STEP `call2_getInfo`** is fetched for that exact code (`live_step_meaning`, cached per
     run in `live_cache` — never persisted to DB). Most sub-lettered siblings (measured 77% in a
     2026-07-26 audit) are same-root/different-stem entries where the shared tree text already
     overlaps `stepGloss` — those are NOT flagged, to avoid paying for a STEP call that answers a
     question `stepGloss` already answers.
   - e. **Greek-only:** appends `lsj:` from `strong_lsj_parsed` (`row_type='lookup'`) and `mounce:`
     from `strong_mounce_parsed`, both joined on the exact code, both `(none)` if empty.
   - f. Lines are joined with `<br>` into one `meaning` cell.
8. **Render.** Per verse: heading (`### {reference}`), verse text, then a table `| # | surface |
   strong | morph | particle | meaning |` — one row per span in `position` order (including
   particles, unlike the coverage count). A per-chapter coverage table (`covered/total/%`) is
   built from step 6/7's counts and placed before the verses section (`cfg_report_section` ordinals
   0 = `coverage`, 1 = `verses`).
9. **Write file** to `{report.verse_analysis_output_dir}/{book_label or book}/
   {book.lower()}-{range}-verse-span-meaning.md` (`reportkit.write_report` — archives the prior
   version on regenerate, doesn't overwrite silently).
10. **Track** (§4b): `passagetrack.record_extract` upserts the `passage`/`verse_passage` rows.

## 6. What this means for "is it a lookup or a script"

It is a script, not a lookup — confirmed. A DB-only "lookup" would be a single join; this has
branching control flow (exact vs. fallback, ambiguity heuristic, Greek-only fields, gap handling),
a live external-service dependency (STEP) that fires conditionally, and — via the auto-backfill
path — can write new rows to five different tables before it even starts rendering. Nothing about
its output is reproducible from `iba.db` alone without also running this exact code: the ambiguity
flag, the STEP-live-resolved text for flagged spans, and the coverage percentages are all computed,
not stored.
