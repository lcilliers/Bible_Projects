# Meaning-only clustering — what changes when verse-share is dropped

**Date:** 2026-05-04
**Hypothesis tested:** Drop verse-share + verse-count from the clustering signal. Use only meaning (root + gloss + meaning, weighted). Does this produce coherent named characteristics?
**Method:** Re-clustered all 2,491 OWNER terms across both languages on the existing semantic-weighted vector (`term-semantic-weighted-vectors-20260504.npz`) — no co-occurrence input.
**Source:** [outputs/markdown/wa-meaning-only-clusters-20260504.json](wa-meaning-only-clusters-20260504.json)
**Sister doc (the problem we're trying to solve):** [outputs/markdown/wa-cluster-love-terms-v1-20260504.md](wa-cluster-love-terms-v1-20260504.md)

---

## 1. Headline result

**Your instinct was right** — dropping verse-share dramatically reduces fragmentation:

| Concept | Original (verse-share + meaning) | Meaning-only k=120 |
|---|---:|---:|
| Love-faculty | 11 clusters + FLAG | 4 main clusters (+ outliers) |
| Fear-faculty | 5 clusters | **3 clusters** |
| Anger-faculty | 5 clusters | **2 main clusters** (+ outliers) |
| Hope-faculty | 5 clusters | 4 main clusters |

And the meaning-only run produced **35 cross-language clusters** (out of 120) — Hebrew and Greek terms with similar meanings actually cluster together, which the original couldn't do because the co-occurrence signal was language-locked.

## 2. The deeper finding — sub-faculty vs umbrella faculty

Meaning-only clustering does **not** produce a single "love characteristic". It produces **clean semantic sub-faculties**:

### Love @ k=120 — 4 coherent sub-faculties + outliers

| Cluster | Terms | What it is |
|---|---:|---|
| **cl 31** | 21 | Greek phil- family — *phileō, philos, philia, philadelphia, filēma, etc.* |
| **cl 91** | 43 | Hebrew love-attachment — *aheb, ahavah, ahav, dod, yadid, yedidut* (all together) |
| **cl 39** | 85 | Greek agapē-family — *agapaō, agapē, agapētos* |
| **cl 51** | 52 | Hebrew racham-compassion — *racham, rachamim, rachum, rachamani, rachamin (Aramaic)* |
| **cl 109** | 11 | Cross-language compassion — *chemlah + oiktirmos* |
| **outliers** | — | chesed alone, machmal alone, chamal alone (3 terms in unrelated clusters) |

This is an *honest* taxonomy. The algorithm is saying: at the level of meaning, **phil-affection, agapē-covenantal-love, Hebrew-aheb-attachment, and racham-compassion are different things** — they share a family resemblance but the language-specific lexical fields really do carve up "love" differently.

### Fear @ k=120 — 3 coherent sub-faculties

| Cluster | Terms | What it is |
|---|---|---|
| cl 7 | yare/pachad/charad/dread family | Hebrew "fear-as-reverence" |
| cl 37 | charad + ragaz + tromos | Cross-language **trembling** (H+G) |
| cl 96 | fobos / fobeō / foberos | Greek phobos family |

### Anger @ k=120 — 2 main + outliers

| Cluster | Terms | What it is |
|---|---|---|
| **cl 100** | Hebrew charon/qetseph/anaph + Greek orgē/orgizō | **Cross-language wrath cluster** ✓ |
| cl 34 | qana, qinah | jealousy sub-faculty |

The cross-language wrath cluster is a real win — it shows meaning-only clustering can identify "this is the same characteristic across both languages" when the meanings really do match.

## 3. The structural choice you now face

The meaning-only run resolves the criteria-conflict you identified, but it surfaces a different question: **what granularity counts as a "named characteristic"?**

Two coherent paths:

### Path A — Sub-faculty granularity (let the data speak)

Accept the ~120 clusters as fine-grained named-characteristic units. *"Love"* becomes 4 named sub-characteristics:
- **Phil-affection** (Greek phil- family)
- **Hebrew-attachment-love** (aheb / ahavah / dod / yadid)
- **Agapē-covenantal-love** (agapē / agapaō / agapētos)
- **Racham-compassion** (Hebrew racham + Greek oiktirmos / chemlah)

Pros: respects how the languages actually carve up the concepts; the bilingual finding (one Hebrew-side, one Greek-side, one cross-language compassion) is informative; researcher can study each sub-characteristic without forcing artificial unity.

Cons: more granular than the program-reset note implied ("the inner being has the capacity to love" — singular).

### Path B — Anchor-driven umbrella characteristics (theory first)

Define the named characteristics theologically/anthropologically (you supply the list — e.g., love, fear, joy, anger, hope, peace, faith, hate, sorrow, ...). For each, supply 3-5 anchor terms. Compute a centroid in the same meaning vector space. Assign every term to its nearest characteristic.

This puts **theory before data**: the *characteristic* is researcher-defined; the *term assignment* is algorithmic.

Concretely for love: you supply *love = {aheb, ahavah, chesed, racham, agapē, agapaō, fileō, dod}*. Algorithm computes a centroid. Every term in the corpus gets a "distance to love" score. Terms within threshold (e.g., cosine sim > 0.5) join the love characteristic. Sub-faculties surface naturally as *clusters within the assigned set* if you want them — but the umbrella is fixed.

Pros: matches "the inner being has the capacity to love" framing; produces exactly N characteristics where N is what you decide; easy to extend.

Cons: assignments depend on which anchor terms you pick (sensitivity to the 3-5 chosen seeds); cross-cluster terms (e.g., *chesed* is between love and faithfulness) need explicit decision rules.

## 4. Recommendation

I think **Path B is what you actually want.** Here's why:

- The phrase *"the inner being has the capacity to love"* in [research/notes/program reset.md](../../research/notes/program%20reset.md) is theory-first. You already know what the characteristics are; you don't need the algorithm to discover them.
- The clustering ecosystem (Path A) is genuinely useful but as a *diagnostic backdrop*, not as the unit of analysis. *"Where do the love-characteristic terms sit in the cluster ecosystem?"* is a different question from *"What is the love characteristic?"*
- Path B is much cheaper to iterate on. Add a characteristic, list 3 anchors, re-run. If you don't like the assignments, change the anchors.
- Path B produces a **deliverable named-characteristic catalogue** — which is what you said you're trying to arrive at.

## 5. Suggested next concrete step

If you agree with Path B:

1. You list the named characteristics you want — start with maybe 20-30. Suggested seed list:
   - love, fear, anger, joy, sorrow, hope, peace, faith, doubt, pride, humility, jealousy, compassion, hate, desire, contentment, courage, despair, gratitude, shame, kindness, patience, self-control, trust, contempt, awe / reverence, longing, regret, contrition, zeal …
2. For each, you supply 3-5 anchor terms (preferably one Hebrew + one Greek + 1-2 supporters).
3. I build the script that computes centroids and assigns every OWNER term, with a confidence score. Output: per-characteristic term list with glosses, plus a "low-confidence" review queue for terms that don't strongly match any characteristic.

This becomes the foundation for the program-reset pipeline: **terms grouped by characteristic, with cluster-ecosystem as backdrop.** Want me to scaffold it?
