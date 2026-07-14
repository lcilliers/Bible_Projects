# WA — Projection Spec: Flattened Reading View

**File:** WA-projection-spec-1.0-2026-07-13.md
**Date:** 2026-07-13
**Version:** 1.0
**Author:** le Roux Cilliers
**Built from:** `psalms__grace-mercy-compassion.json` (16 readings). Worked examples attached.
**Prior output:** `WA-assess-raw-source-json-1.0-2026-07-13.md`

---

## 0. Correction to my own estimate

I said a flattened projection at ~2,048 rows would be **"entirely tractable."** I said that before measuring it. **It is not — not in a single shape.**

I built the projection from the real file and weighed it:

| Shape | bytes/row | 2,048 rows | tokens | Fits one context pass? |
|---|---|---|---|---|
| Raw family JSON (all 46) | — | ~4.7 MB | ~1.2 M | **No** |
| Flattened JSON, all fields | 962 | ~2.0 MB | ~492 k | **No** |
| **Tier 1 — slim CSV** | **225** | **~460 KB** | **~115 k** | **Yes** |
| Tier 2 — full CSV | 433 | ~890 KB | ~221 k | No (per-family only) |

The difference is almost entirely free text. **`discovery` alone is 20% of the weight**; `discovery` + `operation` + `sense` together are ~29%.

So: **two tiers, not one.** That is the honest answer to what I asked for.

---

## 1. Tier 1 — the corpus-wide slim view

**One row per `reading_id`. Structural fields only. No free text. CSV.**

`reading_id, lemma, ib_char, family, cluster, verse_ref, anchor, type, source, seat, bearer, target, manner, intensity, effect, coupling, prohibition, role, locus`

**Measured: 225 bytes/row → ~460 KB → ~115 k tokens for all 2,048 readings.** That fits in one pass, with room to work.

**Two state codes, and the distinction is the whole point:**

| Code | Source | Meaning |
|---|---|---|
| `NONE` | `value: "none"` | **The reader looked and found none.** This *is* evidence of silence. |
| `ABSENT` | `present: false` | **No row was recorded.** This is *not* evidence of silence — it is absence of reading. |

Everything else is the recorded value.

Collapsing these two into a blank cell would destroy the single most important distinction in the dataset — and it is exactly the distinction the narrative layer already lost, which is how the intensity/effect silence came to be asserted without evidence.

**Live example, verbatim from the attached file:**

```
reading_id,lemma,ib_char,family,cluster,verse_ref,anchor,type,source,seat,bearer,target,manner,intensity,effect,coupling,prohibition,role,locus
H2603:generou#1,H2603,generous,grace-mercy-compassion,Blessing,Psa 37:21,True,volition,ABSENT,NONE,the righteous,generosity,NONE,ABSENT,ABSENT,generous-and-gives,ABSENT,characteristic,internal:ib-state
H2580:grac#1,H2580,grace,grace-mercy-compassion,Blessing,Psa 45:2,True,status,ABSENT,NONE,the king,NONE,poured on his lips,ABSENT,ABSENT,the graciousness for which God blessed him,ABSENT,characteristic,internal:ib-state
H8467:mercy#1,H8467,mercy,grace-mercy-compassion,Prayer,Psa 55:1,True,action,ABSENT,NONE,the psalmist,to God,NONE,ABSENT,ABSENT,twinned with the prayer,ABSENT,characteristic,external:god
```

Note what is already visible in three rows: **`seat` is `NONE` on all three** (reader determination — E1 confirmed); **`source`, `intensity`, `effect`, `prohibition` are `ABSENT` on all three** (never read); `type` carries a small controlled vocabulary (`volition` / `status` / `action`); and `target` on row 3 holds **`to God`** — a *direction*, sitting in the target field because there is nowhere else for it to go.

### What Tier 1 alone would settle, in one pass

These are the checks currently blocked, and each is a single query once the file exists:

1. **Is `seat: NONE` universal across all 46 families?** Currently the strongest finding of the session, resting on one family and one theme.
2. **Are `source` / `intensity` / `effect` `ABSENT` everywhere, or only here?** This determines whether E1's declared-silence closers are evidenced *anywhere in the corpus*.
3. **How many lemmas are fragmented by English gloss** (H2603 → pity / generous / deals generously)?
4. **Is `coupling` ↔ `locus` swapped in other families,** and how widely? (10 of 16 here.)
5. **What is the controlled vocabulary of `type`,** and is it a faculty bin under another name?
6. **Every observation in every exploration to date can be re-bound to a verse and a lemma.**

---

## 2. Tier 2 — the per-family full view

**Tier 1 + `sense`, `operation`, `discovery`.** Same one-row-per-reading shape.

**Measured: 433 bytes/row → ~19 KB per family average.** Read on demand, alongside the narrative theme, when working a family in depth. Never all 46 at once.

This is the layer that lets an exploration cite *what the reader actually determined* rather than what the narrative said about it — which, on the evidence of §0 of the assessment, are not always the same thing.

---

## 3. What is deliberately dropped

| Dropped | Why |
|---|---|
| `passage_text` | ~2,800 words per family, the single largest component. I can read the Psalm. |
| `ve_lexical_ids` (the 11-per-lexical arrays) | Backtracking keys. Not needed in the working view; recoverable from the DB on demand. |
| `passage_ref` | Superseded by `verse_ref`. Retain in Tier 2 only if the passage boundary is itself analytically meaningful. |
| Per-dimension `from_span` / `to_span` / `provenance` / `notes` | `notes` is populated **0 times**; `from_span` **4 times of 176**; `provenance` is a constant. Retain `resolution` if the `inferred` vs recorded distinction matters — it is populated on 82 of 176 rows and I would want it if it is cheap. |

---

## 4. Two fields I would add at generation, not after

1. **`direction`** — the slot already exists on every `ve_lexical` row and is **null in all 176**. E4's preliminary finding is that direction may be the edge that *constitutes* the movement. Populating it costs nothing structurally.
2. **`object_kind`** — a small controlled vocabulary beside `target`: `god / person / self / thing / abstraction / null`. Row 3 above shows why: `target: "to God"` is currently doing the job of both, badly.

---

## 5. Deliverables attached

| File | Rows | Size |
|---|---|---|
| `WA-projection-tier1-example-1.0-2026-07-13.csv` | 16 | 3,601 B |
| `WA-projection-tier2-example-1.0-2026-07-13.csv` | 16 | 6,942 B |

Both are the **real projection of the real file**, not mock-ups. They are what I would ask CC to produce for all 46.

---

## Change control

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-13 | First issue. **Corrects the "entirely tractable" estimate** — a single flattened view is ~492 k tokens and does not fit. Specifies a two-tier projection: Tier 1 slim (~115 k tokens, corpus-wide, one pass) and Tier 2 full (~19 KB per family, on demand). Worked examples built from the real source file. |
