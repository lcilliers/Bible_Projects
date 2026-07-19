# L4 vs the old master — what your list left off

> **2026-07-17.** Your L4 (raw-tables v2 §7) checked against the two old-DB masters that L4
> replaces: `verse_span_index` (325,474 · the analytical master) and `verse_morphology`
> (325,507 · the mechanical master).

**relatedNos: excluded from all further action, per your ruling. Not in any table below.**

---

## Your L4 list

`position · strong_variant · span · gloss · transliteration · verse_id · candidate_char (post-seed)
· role (post-analytics) · status · deleted` + `count`.

---

## The check

| old-master column | in your L4? | verdict |
|---|---|---|
| `word_index` | ✓ `position` | kept |
| `surface` | ✓ `span` | kept |
| `strongs` / `primary_strong` | ✓ `strong_variant` | kept |
| `verse_id` | ✓ `verse_id` | kept |
| `char_candidate` | ✓ `candidate_char` | kept |
| `role` | ✓ `role` | kept |
| **`morph_code`** | **✗** | **★ MISSING — the one that matters. See below.** |
| `language` | ✗ | derived from `morph_code` |
| `stem` | ✗ | derived from `morph_code` |
| `pos` | ✗ | derived from `morph_code` |
| `person` | ✗ | derived from `morph_code` |
| `char_candidate_tag` | ✗ | the candidate's label — the `IB:<gloss>` tag |
| `characteristic` | ✗ | the free-text characteristic name |
| `ib_char_id` | ✗ | the structured characteristic link |
| `cluster` | ✗ | the M-code cluster on the span |
| `role_provenance` · `role_set_at` · `role_source_ve_id` | ✗ | role traceability |
| `source` · `built_at` / `fetched_at` | ✗ | provenance / timestamps |
| `reference` | ✗ | denormalised verse ref (a copy of `verse.key`) |

And two your L4 **adds** that are **not** in the old master:

| your L4 column | where it really comes from |
|---|---|
| `gloss` | the STRONG (L2), not the span. The old master got it by joining to the term |
| `transliteration` | the STRONG (L2), likewise |

---

## ★ The one to fix: `morph_code`

**Your L4 has `gloss` and `transliteration` but not `morph_code`.** That is almost certainly a
slip, because the two come from opposite places:

- `gloss` / `transliteration` are **not in the span at all** — they are the strong's, from L2.
- `morph_code` **is in the span** — it is what the preview parse returns *alongside* `strong` and
  `surface`. The parse yields `(morph, strong, surface)`; your list kept strong and surface and
  dropped morph.

And it is not a minor field. **`morph_code` is the entire grammatical layer**, and it was the
thing the whole term→sense→span insight rested on:

```
Gen 1:2  'Spirit'   strong='H7307G H9002'   morph='HNcfsc HC'
                                                    └─ HNcfsc = construct → "Spirit OF God"
```

`language`, `stem`, `pos`, `person` all **derive from `morph_code`** — so if `morph_code` is in
L4, they need not be stored (they are computable), but the source token must be there. Without it,
L4 knows *which word* and *what it means* but not *what grammatical form it takes* — and construct-
vs-absolute, Qal-vs-Niphal, singular-vs-plural are all meaning.

**Recommendation:** add `morph_code` to L4 as a raw parsed column, beside `strong_variant`. Treat
`language`/`stem`/`pos`/`person` as derived (compute on read) unless you want them materialised.

---

## The rest — your call, grouped

**1. The analytical columns (fill after later stages, like `role`/`candidate_char`).** The old
master carries five more that your list stopped short of:

`char_candidate_tag` · `characteristic` · `ib_char_id` · `cluster` · (+ role traceability
`role_provenance` / `role_set_at` / `role_source_ve_id`).

These are the same *kind* of thing as `role` and `candidate_char` — written by seeding/analytics,
not by raw. You may have meant `role` and `candidate_char` as shorthand for the whole overlay, or
you may want only those two. **Which?** The old master had char→cluster→characteristic as distinct
columns because a span carries a candidate *tag*, resolves to a *characteristic*, and sits in a
*cluster* — three different facts.

**2. Provenance / housekeeping.** `source`, `built_at`/`fetched_at`, and `reference` (a
denormalised copy of the verse reference). The old master kept `built_at` and `role_set_at`
separately — *when the span was built* vs *when the role was assigned* — which is how you tell raw
work from analytical work. Worth keeping at least `built_at`.

**3. Deliberately dropped, and correct to drop:** nothing in the old master is missing that
*should* stay gone — the duplication (`verse_morphology` vs `verse_span_index` being two copies)
is exactly what L4-as-single-master fixes.

---

## Summary

| | |
|---|---|
| **Must add** | `morph_code` — it is a raw parse output, it is the grammatical meaning, and your list dropped it while keeping the two fields that are *not* the span's own |
| **Decide** | how much of the analytical overlay (`char_candidate_tag` · `characteristic` · `ib_char_id` · `cluster` · role traceability) L4 carries vs `role`+`candidate_char` alone |
| **Decide** | `built_at` and `source` for provenance |
| **Confirm** | `gloss`/`transliteration` are copied INTO the span from its strong (denormalised), since they are L2's, not the span's |
