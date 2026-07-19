# Romans: passage-build & candidate-seeding diagnosis

> v1 · 2026-07-19 · triggered by researcher inspection of Romans. Evidence pulled live from
> `iba/app/db/iba.db`. Two independent defects confirmed; neither is fit for purpose as it stands.
> This is a diagnosis + options doc — **no changes made**. Awaiting a methodology decision on both.

---

## TL;DR

1. **Passage build shatters continuous text into single verses.** 230 of 276 Romans passages (83%)
   are single-verse, and **221 of those 230 (96%) sit directly next to another candidate-bearing
   verse** — i.e. the context existed and the rule split it off. The stated purpose of a passage
   (extend a characteristic's context to its neighbours) is structurally *not delivered*.
2. **The candidate basis is the migrated substrate, not an independent inner-being net.** Of 1,732
   candidate lemmas, **1,353 (78%) are `layer='registry-direct'`** — the explicitly-rejected
   "registry imputes candidacy" route, still present from the migration and never purged. At the
   same time genuine IB terms with no registry word are **missing**: e.g. **G2168 "to thank" /
   G2169 "thankfulness"** are in `lemma_inventory` but are *not* candidates — thanksgiving is
   invisible across Rom 1:8, 1:21, 7:25, 14:6, 16:4.

The basis is thus simultaneously **over-inclusive** (registry noise) and **under-inclusive**
(misses real IB movements) — the exact double failure the "double control" was meant to catch, but
the control is recorded and not acted on.

---

## Defect 1 — passage build does not deliver context

**Purpose (from `handlers/passage.py` docstring):** "A passage's sole purpose is to extend a
characteristic's context to its adjacent verses so movement / process / qualifying spans can be
assessed with that context."

**What the code actually does** (`passage.build`): forms runs of *consecutive candidate-bearing
verses* and **breaks the run whenever two adjacent verses do not share ≥1 identical base-Strong's**
(`passage.min_shared_strongs=1`, rule `char-continuity`). Non-candidate neighbour verses are never
pulled in at all.

**Why that shatters the text:** in discursive prose (an epistle) adjacent verses almost never
repeat the *same* lemma — each verse advances a different characteristic. So the continuity key is
satisfied only by rare lexical repetition, and the run breaks at nearly every verse.

**Romans measurements:**

| Metric | Value |
|---|---|
| Verses in Romans | 424 |
| Verses bearing ≥1 candidate | 363 (86%) |
| Candidate spans | 845 |
| Passages built | 276 |
| — single-verse | **230 (83%)** |
| — 2-verse | 27 · 3-verse 8 · 4-verse 6 · 5-verse 3 · 6-verse 1 · 10-verse 1 |
| Single-verse passages **adjacent to another candidate verse** (context split off) | **221 / 230 (96%)** |
| Single-verse passages truly isolated | 9 |

**Worked example — Rom 1:3–1:9** (seven consecutive candidate-bearing verses, split into ~five
single-verse passages):

```
1:3  G4561 flesh
1:4  G1411 power · G4151 spirit · G0042 holiness · G3498 dead
1:5  G5485 grace · G5218 obedience · G4102 faith · G3686 name
1:7  G0027 beloved · G5485 grace · G1515 peace
1:8  G4102 faith            ← "I thank my God…"; the candidate captured is faith, not the thanks
1:9  G4151 spirit
```

Every one of these is a continuous argument, yet each verse becomes its own "passage" with no
neighbour context — because no two adjacent verses repeat the same Strong's. The one thing the
passage was for (context) is precisely what is missing.

**Root cause:** the boundary key is *lexical repetition of one candidate*, but the goal is
*continuity of context*. Those are different things. A passage that is meant to supply context
cannot be bounded by "same word repeats."

---

## Defect 2 — candidate seeding is not an independent, complete IB net

**Design intent** (`handlers/candidate.py` docstring): candidacy is *meaning-based only* — the
independent net (gloss/synonym/IB-judgement/read-emergent) plus editable `cfg_candidate_rule`
inputs. Registry coverage (`word_strong`) is **not** a candidacy route; it is only recorded as
`registry_match` (the double control: a candidate with NULL match = a candidate missing a registry
word).

**Actual state of `candidate_seed`:**

| layer | candidates | note |
|---|---|---|
| `registry-direct` | **1,353** | the rejected "registry imputes candidacy" route — migrated in, never purged |
| `ib-judgement` | 202 | independent (legitimate) |
| `read-emergent` | 177 | independent (legitimate) |
| **total** | **1,732** | |

- **`cfg_candidate_rule` is empty** (0 synonym/accept/reject rows). So `seed()` today does *nothing
  but refresh `registry_match`* — there is no live independent net driving candidacy. The whole
  1,732 came from the migration.
- The 07-19 "double-control-only" fix stopped `seed()` from *creating* new registry candidates, but
  **the 1,353 pre-existing `registry-direct` candidates were never removed.** So 78% of the working
  basis is still the rejected route.

**Incompleteness (the "thank" case):**

```
G2168 "to thank"       lemma_inventory ✔   candidate_seed ✘   (NOT a candidate)
G2169 "thankfulness"   lemma_inventory ✔   candidate_seed ✘   (NOT a candidate)
G5485 "grace"          lemma_inventory ✔   candidate_seed ✔   layer = registry-direct
```

Thanksgiving is a genuine inner-being movement, present and untagged across **Rom 1:8, 1:21, 7:25,
14:6, 16:4**. It has no registry word, so the registry-driven migration never allocated it — the
double-control signal (missing registry word) exists but nothing reads it, so the term simply falls
out. Meanwhile "grace" is *in* only because a registry word carries G5485 — the wrong reason.

Net: the basis is over-inclusive on registry noise and under-inclusive on real IB terms. Not a
sound basis to read from.

---

## Options (for decision — no work started)

### A. Passage build

- **A1 — group all consecutive candidate verses; drop the same-Strong's break.** Boundary =
  a maximal run of consecutive candidate-bearing verses in a chapter, full stop. Removes the
  shattering. (Passages get longer; `review_over` flags the long ones.)
- **A2 — anchor + context window.** Keep candidate verses as anchors but pad each with *N*
  neighbour verses (candidate or not) so context is physically present; merge overlapping windows.
  This directly implements the stated purpose.
- **A3 — argument/paragraph boundaries.** Passage = the containing paragraph/pericope (from a
  paragraph source or a punctuation/discourse heuristic), candidates ride inside it.

My read: **A1 is the smallest correct step** and matches the docstring's "maximal run"; A2 layers
context padding on top if A1's runs are still too tight. A3 is a bigger build. Recommend A1, then
review Romans, then decide whether A2 padding is needed.

### B. Candidate seeding

- **B1 — purge the registry-direct route from the basis; keep only independently-justified
  candidates** (`ib-judgement` + `read-emergent` + curated rules), and use `registry_match` purely
  as the completeness control it was designed to be.
- **B2 — completeness pass over `lemma_inventory`** to recover IB terms currently missing (thanks,
  and whatever else the gloss net surfaces), feeding `cfg_candidate_rule`
  (synonym/accept) so the net is *reproducible from config*, not from a one-off migration.
- **B1 + B2 together** rebuild the basis as intended: independent, complete, config-driven, with
  registry coverage as a cross-check rather than a source.

My read: do **B1 + B2**. Without B1 the basis stays 78% noise; without B2 it keeps missing real
terms. Both are needed before any book is worth reading.

---

## Recommended sequence (pending approval)

1. **B1** — reclassify/withdraw registry-direct-only candidates; confirm the surviving independent
   basis size and its Romans footprint.
2. **B2** — gloss-net completeness pass → populate `cfg_candidate_rule`; re-seed; re-stamp Romans.
3. **A1** — change the passage boundary to "maximal consecutive candidate run"; rebuild Romans
   passages; re-measure the single-verse ratio.
4. Review Romans again; decide if **A2** context-padding is warranted.

All four are small, independent, config-governed steps. Nothing here is started — this doc is for
the go/no-go and the A-option / B-option choices.
