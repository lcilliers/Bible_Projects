# M10 — Next-phase decision: synthesis now, or defer until related clusters are done?

- **File:** wa-m10-next-phase-decision-synthesis-timing-v1-20260623.md · **v1 · 2026-06-23 · Author:** Claude Code.
- **Question (researcher, 2026-06-23):** do we run an M10 synergy/synthesis phase now, or **leave it until the other clusters are completed** and come back to sin with the related clusters available?
- **Recommendation: DEFER M10 synthesis.** Park M10 at "evidence-complete + object-kinds + register"; return for synthesis once the partner clusters are analysed. Reasoning below is grounded in what the pass already produced.

## Why defer (grounded in our own outputs)

1. **The deferred register is almost entirely cross-cluster-gated.** Of SDX-01…10, the substantive synthesis questions *cannot* be closed inside M10:
   - atonement/resolution → **M11 / M38 / M12** (SDX-02, SDX-09)
   - the dual-view consistency → **M27** + programme-wide (SDX-04)
   - the pole-pairs → **M26 / M12 / M13 / M31** (SDX-05)
   - home-call relocations → **M06 / M13 / M31 / M26 / M14 / M08 / M03 / M07 / M23 / M35** (SDX-06)
   - external agency → the **spiritual-being interface** (SDX-07)
   - the NT resolution (Group 7's missing piece) → **M11 / M38 / M45** + redemption terms (SDX-09)
   - To synthesise M10 now would mean **forcing closure on questions whose evidence lives elsewhere** — exactly the premature-synthesis failure this whole rework was correcting.

2. **The objects are HALF of pairs.** The dual-view / pole-pair finding means M10's objects are one side of a relation — sin↔righteousness (M26), defilement↔purity (M12), faithlessness↔faith (M13/M31), wicked↔righteous, the operation-view↔characteristic-view (M10b↔M27). **You cannot synthesise one pole without its partner.**

3. **The characteristic's full description needs its resolution.** Group 7 showed a characteristic is only fully described *with* its transformation/renewal (the bi-level resolution) — which lives in **M11/M38/M45**. The characteristic trio (#20/#21/#27) is literally incomplete until then.

4. **It matches the programme's own principle.** Interdependent clusters are finalised *together*; roll the cycle through clusters *before* distilling; don't pay for rework by closing early. The researcher's instinct here is the established discipline, not a deviation.

## What M10 is parked AT (a clean handoff state)
M10 is left in a **complete, self-standing, synthesis-ready** state — nothing lost by waiting:
- **Evidence:** 32 units, self-standing per-unit evidence files (full lexical), index, gap register.
- **Understanding:** 8 grounded, bias-guarded **object-kinds** + two structural hypotheses (characteristic-as-generative-centre; bi-level resolution).
- **External check:** the Logos study cross-checked + woven (corroborates the object-kinds).
- **Open work captured:** the **SDX-01…10** register (in the DB as SD_POINTER) — every deferred question is recorded, so returning later is a lookup, not a re-derivation.

## The ONE nuance to decide separately — the §10 object-kind typology
The **§10 definitional gate** (define characteristic vs status vs condition vs record vs identity vs expression vs mechanism vs remedy vs agency) is *different* from M10 synthesis:
- It is **not M10-specific** — it is a candidate **programme-level lens** (SDX-03). If the eight object-kinds generalise, **defining them now would sharpen the analysis of every remaining cluster** (each cluster read with the same "what kind of object is this?" discipline).
- **Two options:**
  - **(a) Draft a PROVISIONAL §10 typology now** (from the M10 evidence), apply it as the lens going forward, finalise it later when more clusters supply test-cases. *Benefit: every subsequent cluster gets the lens; M10 did the hard discovery, so it's cheap to provisionalise now. Risk: provisional, will evolve.*
  - **(b) Defer §10 too** — keep M10 fully parked; revisit the typology when more clusters give more cases. *Benefit: no premature framework; Risk: the rest of the programme proceeds without the lens M10 surfaced.*
- **My lean: (a)** — a *provisional, explicitly-held-open* typology, because it is the one piece of M10's work that is **generative for the whole programme** (it's a method, not a sin-conclusion). But it is genuinely your call on appetite for a provisional framework now.

## Recommendation summary
1. **Defer M10 synthesis/synergy** → return after M26 · M11 · M38 · M12 · M27 · M13 · M31 · M45 (+ M03/M06) are analysed. (Strong.)
2. **Decide separately on §10:** draft a *provisional* object-kind typology now as a programme lens (my lean), or defer it with the synthesis.
3. **Proceed to the next cluster** in the rework queue (M11 is the natural next — it is both the next cluster *and* M10's primary resolution-partner, which directly feeds the eventual M10 return).

## M11 → M10 FEEDBACK LOOP (researcher, 2026-06-23)
M10 is parked, but **not frozen** — working the partner clusters will **reach back into M10 incrementally**: add observations, **close Session-D (SDX) points**, and **build out the M10 story base**. So the "return for synthesis" is fed continuously, not all-at-once. **Operationalise:**
- **Close SDX points as partners resolve them.** When M11 (etc.) answers an SDX item, set the DB flag `resolved=1` + `resolved_date` + `resolved_note` (the `M10-SDX-NN` rows in `wa_session_research_flags`), and mark it resolved in the register `.md`. *(M11 is poised to close **SDX-02** atonement-home and contribute to **SDX-09** OT→NT.)*
- **Accrue M11-derived observations back into the M10 story base** — into the relevant M10 unit/family file (or a running "M10 story-base" accrual), tagged with the source cluster, so M10's evidence grows as partners are read.
- **The SDX register is the ledger of this loop** — each partner cluster's analysis checks the register for M10 points it can close.

## NARRATIVE STRATEGY — cross-cluster, not per-cluster (researcher, 2026-06-23)
**Narratives are not produced per cluster.** Neither M10 nor M11 gets a standalone cluster narrative/essay. Instead:
- Each cluster produces **evidence + synthesis** (the analytical integration — e.g. `wa-m11-cluster-synthesis-v1`), which is **input**, not a product.
- On completion of **all** (related) clusters, **M10 + M11 + the other related clusters are considered as a whole** to prepare the narrative — **largely around how *sin and salvation* impact the inner-being system**.
- So the deferral (above) is not only of M10's *synthesis* but of the **narrative**, which is a **cross-cluster thematic assembly** at the end. The "sin-and-salvation" group (M10 sin · M11 resolution · M12 purity · M38 salvation · M26 righteousness · M45 renewal · …) is one such narrative grouping.
- Implication: per-cluster work optimises for **feeding the joint narrative** (clean evidence, synthesis, closed SDX points, the M10 story base), not for a self-contained essay. (Consistent with the §d end-point: an evidenced findings corpus → multiple products, reference + narrative.)

*Decision record — defer M10 *full* synthesis AND narrative; narratives are cross-cluster (the sin-and-salvation assembly); M10 parked but fed incrementally via the M11→M10 loop; §10-typology timing is the open sub-question.*
