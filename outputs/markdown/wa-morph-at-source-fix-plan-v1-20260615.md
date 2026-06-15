# Fix plan — populate morph at the SOURCE (the generic STEP fetch), not via a separate backfill

> Researcher (2026-06-15): *"scripts for general use should always handle downstream values correctly… I am uneasy that audit_word doesn't trigger a morph update, and I'm not sure if there's a generic get-STEP routine this applies to."* There is, and it does. This is the root fix; the backfill becomes a one-off/repair tool, not the only way morph ever gets set.

## The finding
`scripts/analytics/step_client.py:get_verse_records()` is the generic verse fetch. For each verse it already parses the `preview` HTML for `esv_text` and `target_word` (lines 274–289) — **but throws away the `morph='…'` span that is in the same HTML** (the very spans `_apply_morph_backfill.py` re-fetches and parses). Consequences:

| create-path | source of verses | morph today |
|---|---|---|
| `audit_word.py:1043` | extract JSON ← `extract_word_data` ← `get_verse_records` | **NULL** (morph never reaches it) |
| `gap_fill.py:235 / 835` | `get_verse_records_with_html` (holds morph HTML) | **NULL** (HTML used only for span confirm) |
| `new_word.py:476` | `get_verse_records_with_html` | **NULL** (same) |

So every newly-audited/added word gets verses with **no morph → no stem, no mode, prefix-only language**, until someone remembers the backfill. That violates "a general routine must leave its downstream values correct."

## The fix (morph at the source → all paths inherit it)
1. **Centralise the parser.** Move `morph_for(html, strong)` (currently in `_apply_morph_backfill.py`) into a shared place (`morph_util` or step_client). `stem` already derivable via `morph_util.morph_stem`.
2. **`get_verse_records()` returns morph.** Add `morph_code` (+ `stem`) to each record dict, parsed from the preview HTML it already holds. `get_verse_records_with_html` inherits it ("same list").
3. **Carry it through the extract.** `extract_word_data` → the Step-1 extract JSON gains a `morph_code`/`stem` per verse (confirm the exact JSON producer audit_word ingests).
4. **All 4 INSERT sites write it.** `audit_word:1043`, `gap_fill:235/835`, `new_word:476` add `morph_code`, `stem` to the INSERT from the fetched record.
5. **Cascade the derivations at insert.** Because morph is now present when the verse is created, call `reconcile_language()` at the end of `audit_word` / `gap_fill` / `new_word` (this is the morph-update trigger the researcher wanted in `audit_word` — now valid, because morph exists there). stem is written inline; the mode finding (future) hangs on the same point.
6. **Backfill demoted to a repair/one-off tool** — `_apply_morph_backfill.py` stays for the existing backlog and as a reconciliation/repair path, not the sole way morph is ever set.

## Why this is the correct shape
- **One source of truth for the fetch.** Every caller of the generic routine (engine + `word_study_extract` + future) gets morph for free; no path can silently create morph-less verses.
- **Additive + safe.** New dict keys / new columns in the INSERT; existing callers unaffected.
- **Self-consistent derivations.** morph set at creation → stem + language + (later) mode derive immediately, no deferred-backfill gap.

## Risks / to verify before coding
- Confirm the exact **Step-1 extract JSON producer** that `audit_word` ingests carries the new field (step 3) — if it's a separate exporter, it needs the change too.
- `get_verse_records` morph parse must match the backfill's `(strong, base-strong)` span-matching exactly, so new and backfilled morph agree.
- A fresh `audit_word --dry-run` on one registry to confirm verses arrive with morph + stem + correct language before going live.

## Scope of existing data — investigated (do existing verses need a re-run? **No.**)
Facts (2026-06-15), so this isn't guessed:
- **229,957** verse rows → **167,204 soft-deleted (left untouched, as instructed)** → **62,753 active**.
- Active **with** morph: **58,654**. Active **missing**: **4,099**, all accounted for:
  - **170 T2 particles** — function words, correctly blank (no morphology to have).
  - **6 content-cluster strays** — STEP returned no morph for those exact verses (M21/M04/M05/M38/M23). Genuinely un-parseable; not a backfill gap.
  - **3,923 with `mti_term_id` NULL** — **not linked to the MTI model**, so outside the cluster/finding analytical scope entirely. Concentrated in **registries 213 (2,888) and 214 (907)** — recently-extracted words **not yet processed** into the MTI/cluster model (their term_ids already have 945 active *linked* rows elsewhere). They are **pending processing, not wrong data**.
- **Conclusion:** the active analytical scope is already correct; **no re-run of existing verses is needed.** The source fix is **forward-looking** — it guarantees verses (e.g. registries 213/214 when they're processed, and every future audit) get morph at creation, so they never land morph-less again. (Side note: 213/214 sitting unlinked is a separate processing-backlog item, not a morph issue.)

## Recommendation
Implement 1–6 as the proper generic fix. It is bounded (1 shared parser + 1 fetch change + extract carry + 4 INSERT edits + reconcile wiring) and removes the morph-less-verse class of bug entirely. **Confirm and I'll proceed** — I'll verify the extract-JSON producer first, then implement with a dry-run on one registry.
