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

## Scope of existing data — investigated, and CORRECTED (2026-06-15)

> An earlier draft called the 3,923 morph-less actives "pending, not wrong." **That was wrong** — investigation (prompted by the researcher) shows most are a genuine broken-link integrity gap that the fix must include.

Facts:
- **229,957** verse rows → **167,204 soft-deleted (left untouched)** → **62,753 active**.
- Active missing morph: **4,099** = **170 T2 particles** (correctly blank) + **6 STEP-blank content strays** + **3,923 with `mti_term_id` NULL**.
- **The 3,923 break down as:**
  - **3,636 are LINKABLE and SHOULD be linked** — their `term_id` matches an existing `mti_terms.strongs_number`; `mti_term_id` is just NULL. **Broken link, not pending.** Proof: registry **213 'listen' is `phase1=Complete` / cluster C02** (a *processed* word) — its 2,888 verses are simply unlinked. (Registry **214 'suffering' is `phase1=Excluded`** — its 907 are arguably out-of-scope but still unlinked.)
  - **287 are genuinely unregistered** — 22 Strong's with **no `mti_terms` row** (e.g. H0241G/H/I *ear* sub-entries, G3775 *ear*, H2266/H2267 *join/companion*). A separate registration gap.
- **Root, one layer below morph:** **nothing writes `wa_verse_records.mti_term_id`** — not `audit_word`, not `migrate.py`, no maintained script (every reference is a read/JOIN). `audit_word`'s INSERT (line 1043) sets `term_id` but leaves **both `mti_term_id` and `morph_code` NULL**. So the create-path leaks *two* downstream values, and the chain is: link (mti_term_id) → morph → stem/language — none wired in.

## The fix must therefore cover linkage too (expanded)
The morph-at-source fix is necessary but **not sufficient** — morph backfill keys on `mti_term_id`, so unlinked verses can't get morph regardless. Add:
- **A. `audit_word` (+ gap_fill/new_word) populate `mti_term_id` at insert** — match `term_id`→`mti_terms.strongs_number` when the verse is created. This is the missing maintained linkage (parallel to the morph-at-source change). Verses then arrive **linked + morphed**, and stem/language cascade.
- **B. One-time link backfill** for the **3,636** existing linkable records (set `mti_term_id` from the matching `mti_terms` row), then morph + language cascade over them.
## Decisions taken (researcher, 2026-06-15) + exact scope

**D1 — Excluded registry ⇒ soft-delete its entire downstream** (not ignore/filter). General rule, applies to all 42 excluded registries; only **12 have data**. Active downstream to soft-delete (`delete_flagged=1`, reversible):
- **928** `wa_verse_records` · **169** `wa_term_inventory` · **22** `mti_terms` (owned) · **276** `finding` · + their `verse_context` rows. (`wa_file_index` has no `delete_flagged` — mark via status / leave.)
- **SAFE: 0 sharing** — none of the 22 owned terms are referenced by active verses in non-excluded registries, so nothing live is harmed.
- **Engine rule:** when `audit_word`/`new_word` set a registry `Excluded`, cascade the soft-delete (today it just filters — that's the bug).

**D2 — Fix the unlinked records AND make the scripts maintain the field.** After D1, the active set is:
- **Link 2,731** records (set `mti_term_id` from the matching `mti_terms` row) — mostly **R213 'listen' (2,664)** + R130/R30/R62. Then morph + stem + language cascade.
- **Register + link 285** records — **21 Strong's** with no `mti_terms` row (H0241G/H/I *ear* 179 · G3775 *ear* 34 · H2266 *join* 25 · …). Create `mti_terms` rows, then link + cascade.
- **Engine rule:** the create-paths (`audit_word`/`gap_fill`/`new_word`) must **check and populate `mti_term_id`** at insert (match `term_id`→`mti_terms.strongs_number`), so this never recurs.

## Implementation order (all reversible; dry-run before each live step)
1. **D1 cascade** — reversible soft-delete script across the 5 tables for the 12 excluded registries (dry-run → live).
2. **D2 link backfill** — set `mti_term_id` for the 2,731 active linkable; **register** the 21 Strong's + link the 285.
3. **Morph + language cascade** over the newly-linked (run `_apply_morph_backfill` for their clusters/terms → `reconcile_language` auto-runs).
4. **Engine — source fix** (the original plan §"The fix"): `get_verse_records` returns morph; create-paths write `mti_term_id` + `morph_code` + `stem`; exclusion cascades soft-deletes. Dry-run on one registry.
5. **Verify** — 0 active mti-NULL in non-excluded registries; excluded downstream fully soft-deleted; a fresh audit produces linked+morphed verses.

## Recommendation
Implement 1–6 as the proper generic fix. It is bounded (1 shared parser + 1 fetch change + extract carry + 4 INSERT edits + reconcile wiring) and removes the morph-less-verse class of bug entirely. **Confirm and I'll proceed** — I'll verify the extract-JSON producer first, then implement with a dry-run on one registry.
