# L4 — source vs derived, and the fixes

> **2026-07-17.** Fixes the two L4 mistakes, then answers the design question: extend the source
> table, or keep source pure and derive separately.

---

## 1. The fixes

**a) `morph_code` — add it.** It is a raw parse output (the preview gives `morph`, `strong`,
`surface`), it is the grammatical layer, and the list dropped it while keeping `gloss`/`transliteration`,
which are not the span's at all.

**b) "char and role = all the related columns."** So the analytical overlay in full:
`candidate_char` · `char_candidate_tag` · `characteristic` · `ib_char_id` · `cluster` · `role` ·
`role_provenance` · `role_set_at` · `role_source_ve_id`.

That is nine derived columns — which is what makes the design question below unavoidable.

---

## 2. The design question

> *"use the table that originates with the source and just extend it for the other values as the
> study progresses, OR keep the source pure and create another table for the derived values."*

### The principle

**Put data in one table when it shares a source-of-truth AND a lifecycle. Split it when either
differs.** Here, both differ:

| | the span (raw) | the overlay (derived) |
|---|---|---|
| **source of truth** | STEP — "what the text is" | our analysis — "what we judged" |
| **written** | at raw time, per word | after ALL words built → seeding → analytics |
| **written by** | the parse | the seeding stage, then the lexical stage, then role-reassignment |
| **volatility** | immutable — STEP said it once | **re-run repeatedly, and it has FAILED** |
| **on a re-run** | must not be touched | dropped and rebuilt from scratch |

When one half is a fixed source and the other is a volatile judgement, they do not belong in the
same row.

### This is not a general opinion — the project already ruled it, and the old master is the named violation

The config's own rules say separate, in three places:

- **`raw.immutable`** — raw is writable ONLY by its source; no downstream layer may mutate it.
- **`raw.no-analytical-values`** — its stated purpose: *"prevent the specific failure where
  interpretation was stamped onto mechanical tables (role / char_candidate / characteristic written
  onto `verse_span_index`)."* **That is exactly the "extend the source table" option, named as the
  failure.**
- **`gate.base.regenerable`** — base must reproduce from raw exactly. You cannot regenerate the
  source half of a mixed table without destroying the derived half.

`verse_span_index` **is** the extend-in-place design, and it is the thing the migration strips.

### The evidence it costs, in this project specifically

`verse_span_index.role_provenance` holds `'lexical-model-2026'`, `'read-2026'`,
`'role-reassign'` — **three campaigns that overwrote the same column.** Every re-run of the
analytics wrote to the same 325,474 rows that hold the source `morph_code` and `strong`. The
lexical layer failed acceptance (8/18 dimensions) and was re-run many times. Each re-run put the
irreplaceable source spans at risk to rewrite a judgement.

**With a separate derived table, the analysis is dropped and rebuilt with a single `DELETE`, and
the 325k source spans are never touched.** That is not a hypothetical benefit here — it is the
exact operation the project performed repeatedly, dangerously, on one table.

### The cost of separating

One join, on `(verse, position)` or a span id, both indexed. At 325k rows that is negligible —
and the old design already paid it internally: `verse_span_index` is itself a *copy* of
`verse_morphology` (`source='verse_morphology'` on every row), so the "one table" was never one
table — it was two, with the copy carrying the overlay.

### It also fixes the mistake in §1

In a **source-pure** span table, `gloss` and `transliteration` would never have been added — they
are the strong's (L2), read through the strong FK — and `morph_code` would never have been dropped,
because it is the span's own. The confusion in the L4 list (keep the strong's fields, drop the
span's own) is exactly what a mixed table invites: it stops being obvious which column is source
and which is derived.

---

## 3. Recommendation

**Keep the source pure. Derive separately.** Two tables, 1:1 on the span key:

**`span`** — raw, immutable, built by the parse:

| column | from |
|---|---|
| `id` · `verse_fk` · `position` · `deleted` | ours |
| `strong_variant` | parse |
| `surface` | parse |
| **`morph_code`** | parse |
| `built_at` | ours (raw time) |

`language` · `stem` · `pos` · `person` derive from `morph_code` — compute on read.
`gloss` · `transliteration` are **not here** — read from L2 via `strong_variant`.

**`span_analysis`** — derived, mutable, filled after later stages, 1:1 with `span`:

| column | filled by |
|---|---|
| `span_fk` · `deleted` | — |
| `candidate_char` · `char_candidate_tag` | seeding |
| `role` · `role_provenance` · `role_set_at` · `role_source_ve_id` | analytics |
| `characteristic` · `ib_char_id` · `cluster` | analytics |

Raw creates `span`. Seeding and analytics create/fill `span_analysis`. A failed analytics run
truncates `span_analysis` and rebuilds it; `span` is never in scope.

**This means L4 is two tables, not one** — which departs from "L4 is the old master". But the old
master is the design the whole rework exists to undo, and the split is what makes raw immutable and
the analysis re-runnable. If you would rather one table for simplicity, the honest trade is: you
re-accept the exact coupling that put source data at risk through every one of the lexical re-runs.

### The general rule, for the other layers too

The same test decides every table: **does this column share a source-of-truth and a lifecycle with
the row's key?** L1/L2/L3 are all single-source and single-lifecycle, so each is one table. L4 is
the only place raw and judgement meet — so it is the only place that splits.
