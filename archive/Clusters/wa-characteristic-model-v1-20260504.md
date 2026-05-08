# Characteristic-driven term classification — conceptual model

**Date:** 2026-05-04
**Status:** Proposed model, awaiting researcher confirmation
**Driver document:** [research/notes/program reset.md](../../research/notes/program%20reset.md)
**Sister docs:** [wa-cluster-love-terms-v1-20260504.md](wa-cluster-love-terms-v1-20260504.md), [wa-meaning-only-finding-v1-20260504.md](wa-meaning-only-finding-v1-20260504.md)

---

## 1. The model in one sentence

**The core meaning of a term decides its role in the classification:**
- if its core meaning *is* a characteristic, or expresses a characteristic → assign to that **characteristic cluster**
- if its core meaning modifies or qualifies a characteristic → falls into a **qualifier cluster**
- otherwise → falls into a **supporting cluster** (objects, body parts, social roles, neutral verbs)

## 2. Three-tier classification

```
Term's core meaning
  │
  ├─ IS or EXPRESSES a characteristic          →  CHARACTERISTIC bucket
  │     └── grouped by which characteristic       (love, fear, joy, anger, …)
  │
  ├─ MODIFIES / QUALIFIES a characteristic      →  QUALIFIER bucket
  │     └── grouped by what kind of qualifier     (intensity, perfection, duration, …)
  │
  └─ NONE OF THE ABOVE                          →  SUPPORTING bucket
        └── grouped by topical area               (body, object, social role, …)
```

### 2.1 What goes in each tier

| Tier | Examples |
|---|---|
| **CHARACTERISTIC** — the term's core meaning **is** the inner-being state | aheb (love), yare (fear), samach (joy), charon (wrath), shalom (peace), agapē, fobos, chairo |
| **CHARACTERISTIC — expression of** | tears (expression of grief), shout (expression of joy), trembling (expression of fear) — these *manifest* a characteristic and group with it |
| **QUALIFIER** — modifies the manner/intensity/duration | tom (complete), rabba (great), olam (forever), me'od (very), tahor (pure-as-modifier) |
| **SUPPORTING — body** | yad (hand), ozen (ear), lev-as-organ (heart-as-organ), regel (foot) |
| **SUPPORTING — object** | keli (vessel), kos (cup), kapporet (mercy-seat-as-object) |
| **SUPPORTING — social role** | re'a (neighbor), av (father), eved-as-status (servant-as-role) |
| **SUPPORTING — neutral verb** | matsa (find), yashav (sit/dwell), ya'ats (advise) — actions without inner-being content |

### 2.2 Boundary cases (where a term sits between tiers)

These will need explicit decisions:

- **chesed** — kindness AS faithful-loyalty (characteristic) OR covenant-loyalty (relational disposition)? → likely characteristic with relational expression.
- **lev** (heart) — body part (supporting) OR seat-of-inner-being (a different category — "locus")? Likely *locus*, which may need a fourth tier.
- **avad** (to serve) — neutral action (supporting) OR expression of devotion (characteristic-related)? Context-dependent.
- **shamar** (to keep / guard) — neutral verb OR expression of faithfulness? Context-dependent.

## 3. Why this model fits the program-reset framing

From [research/notes/program reset.md](../../research/notes/program%20reset.md):
> *"the entire pipeline is flawed [...] the registry has duplicates [...] meaning of terms, and therefore words to be discribed much earlier [...] subject of analysis is terms, supported for meaning by verses."*

This model:
1. **Puts core meaning first** (your stated primary driver).
2. **Uses verses as supporting evidence**, not as the classification driver.
3. **Treats characteristics as the unit of analysis** (matches "the inner being has the capacity to love").
4. **Surfaces qualifier/supporting terms as fallout**, not as the goal — they exist but are not the focus.
5. **Eliminates verse-share / verse-count as classification criteria** — those are *analytic* (used later to study how characteristics interact in scripture).

## 4. Operational implications — what this changes in the algorithm

### 4.1 Vector composition — meaning-first

The current semantic-weighted vector is:
- root 35% + gloss 35% + meaning 30%

Under "core meaning is primary", I'd propose:
- **meaning 50% + gloss 30% + root 20%**
  *— OR —*
- **meaning 60% + gloss 40%**, drop root entirely

Why drop / reduce root:
- root encodes morphological similarity, which sometimes tracks meaning (chesed/chasid both = covenant-loyalty) and sometimes doesn't (racham as compassion vs racham as womb).
- when root and meaning disagree, *meaning should win* per your specification.

**Decision needed:** which weighting to use. My recommendation: **meaning 50% + gloss 30% + root 20%** as a moderate move — keeps root as a tiebreaker but lets meaning dominate.

### 4.2 Classification pipeline — three passes

**Pass 1 — Characteristic anchors:**
- Researcher provides the named-characteristic list (~20-30) and 3-5 anchor terms per characteristic.
- For each anchor set, compute centroid in meaning-first vector space.
- Every term gets a "distance to nearest characteristic" score.
- Terms above threshold (e.g., cosine sim > 0.55) → assigned to that characteristic.
- Terms below threshold → fall through to Pass 2.

**Pass 2 — Qualifier triage:**
- Researcher (or a small qualifier-anchor set) provides exemplars: tom (complete), rabba (great), olam (forever), me'od (very), shalem (whole).
- Run the same nearest-centroid logic. Terms close to qualifier-centroids → QUALIFIER bucket.
- Terms below threshold → fall through to Pass 3.

**Pass 3 — Supporting bucket:**
- Whatever remains. Optionally sub-cluster within (body / object / social role / neutral verb) but this is no longer the analytical focus.

### 4.3 What we already have that supports this

- **Term meaning text exists in DB** (`mti_terms.meaning`, `wa_meaning_sense`, etc.) — already encoded in the meaning vector.
- **Sentence-transformer embeddings** of meaning text are computed and stored in the existing npz.
- **Researcher-curated characteristic list** is *not* yet defined — this is the missing input.

### 4.4 What this leaves behind

- **The 88 cluster IDs (H001..H055, G000..G032)** become a *diagnostic backdrop*, not the unit of analysis. They tell you "this term is in cluster H028 by vector geometry" — which is descriptively interesting (where in the geometry does this term live?) but no longer the analytical home.
- **The 214-word registry** likewise becomes a *historical artefact* / discovery log. The unit of analysis shifts to the ~20-30 characteristics.
- **Verse-share + verse-count** are removed from classification; they re-enter at the analysis stage ("how does *love* interact with *fear* in the corpus?").

## 5. What the researcher needs to supply

For Pass 1 to run, you need to provide:

| Input | Format | Estimated effort |
|---|---|---|
| Named-characteristic list | 20-30 names (e.g. love, fear, joy, …) | 30 min — likely already in your head |
| Anchor terms per characteristic | 3-5 Strong's numbers per characteristic, prefer Hebrew + Greek mix | 1-2 hours review of glosses |
| Threshold for "is characteristic" | cosine sim cutoff | tunable — start at 0.55 |
| Qualifier seed exemplars | 5-10 Strong's numbers | 30 min |

For most characteristics the anchor terms are obvious. For boundary cases (chesed, racham, shalom) we'll need explicit decisions about which characteristic owns them.

## 6. Proposed next step

Two ways to start:

**(a) You lead the list.** You write the 20-30 characteristics + anchors. I run Pass 1 and report the assignments + low-confidence review queue.

**(b) I draft a starter list.** I draw a 20-30 characteristic list from biblical anthropology (love, fear, joy, anger, hope, peace, faith, hate, sorrow, longing, shame, pride, humility, jealousy, compassion, contentment, awe/reverence, despair, gratitude, kindness, patience, trust, doubt, anxiety, courage, contempt, regret, contrition, zeal, integrity). For each, I propose 3-5 anchor terms based on the term-anchor data we have. You then review and revise, and we run Pass 1.

(b) is faster if you trust me to draft sensibly; (a) is more controlled if you want to define the characteristic taxonomy yourself.

**Recommend (b)** — it gets you a draft to react to, which is usually faster than starting from a blank sheet.
