# Master index — the `role` column: design, debate, and backfill (2026-07-07)

> Records the whiteboard debate that led to putting a per-span **role** onto the master index (`verse_span_index`), the decisions taken, and the backfill from `ve_lexical`. Written for clarity before/while acting. Companion to the per-book corrective method (`Workflow/Instructions/wa-per-book-corrective-method-authoritative-v1-20260707.md`). **These backfilled roles are the EXISTING, known-imperfect roles — imported so we can analyse them, NOT because they are trusted** (see §6).

---

## 1. The problem we were circling
The master index `verse_span_index` is the term-verse-span table every other layer points to. But it had **no notion of "characteristic."** You cannot tell from the master whether a span is an inner-being characteristic, a qualifier, or standalone — that verdict lives only in `ve_lexical` (`ve_nr=115`, the `role` item), assigned during the lexical sanity-check. So "which spans matter" is an *output* of the lexical, discoverable only by joining it — not an indexed property of the master.

This surfaced while questioning whether Psalms/Proverbs re-reading sits on a sound substrate (roles ~50% wrong; lexicals incomplete on characteristics; ~905 Psalms verse-records unlinked). See `wa-session-log-20260706-07-...md` and the substrate-risk discussion.

## 2. What the master is (as-built, verified)
- **Granularity:** one row per **morphological word** (`verse_span_index` is 1:1 with `verse_morphology`; 325,474 ≈ 325,507). Every particle included.
- **Keys:** a span is **globally unique** by `id`, and equivalently by `(verse_id, word_index)`. `word_index` alone is verse-relative (restarts at 0).
- **The strong is NOT a key:** `primary_strong` is one head strong per row, but it repeats — 19,391 `(verse, strong)` groups have the strong on >1 span of the same verse; `H3068` sits on 5,979 spans corpus-wide. So role must key on the **span id**, never on the strong.
- **Links point IN, not out:** `wa_verse_records.verse_span_id` and `ve_lexical.verse_span_id` reference the master; the master holds no `mti_term_id` / `verse_record_id` / `ve_lexical_id` / role column. The `mti_terms` tie is by strong-string and partial (of 2,131 distinct Psalms real-strongs, only 832 have a study term).

## 3. The decision — role becomes a column on the master
Add a per-span **role** to `verse_span_index`, written by the lexical evaluation of the verse. Rationale, agreed on the whiteboard:
- Role is **one-per-span**, uniquely keyed on `verse_span_index.id` → a natural column, not a join.
- A **column enforces the uniqueness** that the current row-storage does not: today 16 spans carry *two* active `ve_nr=115` role rows (drift a column makes structurally impossible).
- It makes "is this a characteristic?" an **indexed property** of the master — the thing the corrective method needs to decide what must be tracked/read.
- It **unlocks the intended model:** once role lives on the master, a standalone/qualifier span no longer needs a `ve_lexical` row merely to record its role. The master becomes the **census of all spans + their role**; `ve_lexical` can be reserved for the **rich dimensional analysis of characteristics only** ("only characteristic spans have a ve-lexical").

## 4. Three design decisions (surfaced; researcher's call)
1. **Single source of truth** — target: the master becomes the authoritative home for role; the lexical process writes it; the `ve_nr=115` role item is retired or becomes a mirror. *(Not yet enacted — this backfill is the first step; the old `ve_nr=115` rows are left in place for now.)*
2. **Updatable, not write-once** — role gets revised (the whole ch1–6 reassessment). Column carries `role_provenance` + `role_set_at`; `role IS NULL` = "not yet assessed" worklist.
3. **Backfill now for analysis** — researcher directed: import all current roles from `ve_lexical` so we can analyse them. Done verbatim; **not** a trust statement (§6).

## 5. Schema + backfill (M64 → 3.38.0)
New columns on `verse_span_index`:
| column | meaning |
|---|---|
| `role` | the role value, copied verbatim from the span's active `ve_nr=115` row |
| `role_provenance` | that row's `source_provenance` (`lexical-model-2026` / `role-reassess-2026` / `leviticus-lexical-v1`), or `CONFLICT` |
| `role_set_at` | timestamp this backfill wrote it |
| `role_source_ve_id` | the `ve_lexical.id` it came from (traceability) |

Backfill rules:
- Span with **exactly one** active `ve_nr=115` role → copy value + provenance + source id.
- Span with **>1** active role (the **16 conflict spans**, all Leviticus) → `role=NULL`, `role_provenance='CONFLICT'` — reported, not arbitrated.
- Span with **no** active role → left NULL (unassessed; the bulk — only ~87.8k of 325k spans carry any role).

## 6. Honest status of the imported roles (do not over-read)
- **~50% of roles are wrong** (researcher's assessment; ch7 corroborated a large error rate). This backfill imports them **as-is** to be analysed, not to be trusted.
- **Vocabulary is not clean.** Real values include the intended `characteristic / process-qualifier / standalone`, but also `qualifier` (role-reassess drift vs `process-qualifier`) and a large **Leviticus free-text taxonomy** (`ritual-mechanical`, `the-sinner`, `mistag-not-ib`, `offering-quality`, …). Backfilled verbatim; normalising it is a separate decision.
- **The standalone/qualifier boundary is still open** (the 16-dimension rule; ch7 role reassessment remains **paused**). Nothing here resolves it.
- These caveats are exactly why the column is added **empty-of-trust**: it is a working surface for analysis, and the corrected role process will overwrite it.

## 7. Artefacts
- Script: `scripts/_apply_add_role_to_master_index_v1_20260707.py` (dry-run default; `--live`).
- Pre-op backup + integrity snapshots recorded at run.
- Distribution + the 16 conflicts reported back to chat for the analysis step.
