# Compound handling + cause — analysis (2026-06-16)

> Response to the M01 extract review (`extracts/WA-m01-lexical-extract-review-v1.0-2026-06-16.md`). The lexical-quality fixes are done + rebuilt; this records the two design questions the review raised: **how to handle the compound**, and **how to resolve cause**.

## A. Compound — the analysis

**The problem (researcher + AI):** the compound on a term says "combines with *sha.ma* (M41)", but *sha.ma*'s full lexical record sits in a *different* term-in-verse record (and, in a cluster-extract, a different file). So the synergy you'd analyse — how fear and hearing interact in Gen 3:10 — isn't in the payload. The M-code is the co-term's cluster tag — noise to the analysis.

**Grounding:** every co-occurring term IS fully analysed — in Gen 3:10, *ya.re*, *et*, *sha.ma*, *e.rom* each have their own complete ve_lexical record (12/9/11/9 rows). Nothing is missing; it's just **not co-located**.

**Conclusion — two-level fix:**
1. **Lexical level (done):** the compound is a clean, resolvable *reference* — co-term `translit "gloss" — role`, with the M-code **demoted** to the citation. It carries the co-term's gloss (useful) and a role, and identifies the co-term so it can be joined.
2. **Extract level (next, the real fix):** stop compiling JSON by *cluster-term* and compile **by verse, including every co-occurring term's full record**. Then the compound web is **self-contained** — every co-term it references is in the same verse payload with its full profile, so synergy is analysable without joining other files, and the M-code becomes irrelevant (you have the co-term's actual lexical). The cluster becomes a *tag*, not the compilation unit — consistent with the occurrence-as-unit direction.

*(Deferred, optional: type the compound edge grammatically — governs / co-seated / qualifies — and model it once per edge rather than reciprocally on both terms. Revisit after the verse-based extract.)*

## B. Cause — the open decision (NOT resolved this pass)

**The fact:** cause is resolved on ~1% of occurrences; UNRESOLVED where flagged. The trigger of an inner state is usually a **narrative clause** ("because I was naked"), not a morphological relation — so the mechanical engine structurally cannot supply it well. It is the same class as purpose/typology: **interpretive, not lexical.**

**Options (researcher decision needed before analytics is called complete):**
- **A — cause is a READ field:** resolved by a targeted AI pass over the verse + surrounding context (honest, but a per-verse read = cost).
- **B — richer mechanical patterns:** the *ki/hoti/gar* causal-clause content + the object of perception → lifts coverage from ~1% toward ~15–20%, flags the rest UNRESOLVED for the read.
- **C — cause is a synthesis-layer question,** not a per-verse lexical field at all.

**Recommendation:** **B then A** — squeeze the mechanically-recoverable causes, treat the residue as a deliberate read field. But this is the researcher's call, and per the review it must be settled before the layer is declared analysis-ready.

## What was fixed this pass (lexical, rebuilt over all 40,739 units)
- **Faculty de-circularised** — from each term's OWN meaning (lemma-classified), R1-only; the trigger's faculty belongs to how/cause/compound, not the term. M01 → affect ~99% (correct), small real minorities; boundary-misfits (anankē) get no faculty.
- **Verb-term gating** — a term that is itself a verb no longer gets a spurious neighbouring "how"; its object/experiencer come from its own clause.
- **Sense** — clean per-occurrence value (no verbose inline lemma; lemma lives in the `lexicon` table).
- **Compound** — M-code demoted (A.1 above).

**Still open:** cause (B); R2-faculty removed (was noise); the verse-based extract (A.2); the *ankē*-type boundary-misfit review (now surfaceable via "no faculty in a faculty cluster").
