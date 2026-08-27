---
name: feedback_l1_l2_is_multi_angle_report_then_synthesise
description: The L1/L2 cycle is the CRUCIAL, failure-prone, ITERATIVE core of the study (verse meaning = gravest data risk). V3_2 must be built as a MULTI-ANGLE REPORT PIPELINE, not one mechanical pass: each angle (morph/stem · sense-branch · keyword · keyword-digestion · scenario-typing · span-attach) emits an independently reviewable/honable report; L1 narrows + surfaces residues; a SYNTHESIS step builds on ALL angle results + the verse read to produce the single DB update; two researcher review gates bracket it.
metadata:
  type: feedback
---

**Researcher reflection after the 2026-06-08 P1/P2 prototyping session.** Three governing realisations:

a. **The L1/L2 cycle is crucial and the most likely point of failure/oversight in the earlier research** —
   verse meaning is the data; getting it wrong silently corrupts everything downstream
   ([[project_next_action_audit_surface_verses]]).
b. **It is iterative between CC and researcher** — several review rounds per cluster, partly to **hone the
   scripts**, partly to **handle the many variations / situational differences**. Not a one-shot. Every
   prototype pass surfaced a real variation a review round caught (homonym, within-stem shade, keyword
   source-scope, qualifier co-presence).
c. **V3_2 must (i) emit reports on the different angles, then (ii) build on ALL the angle results to generate
   the final DB update.**

**Architecture (report-per-angle → review → synthesise → DB):**
- **L1 = mechanical angles, each emits a per-cluster REPORT** (A morph→stem · B sense-branch parse · C
  keyword+self-check · E scenario-typing S0–S6 · relevance gate). L1 **narrows** (stem branch, type-vector,
  clean keywords) and **surfaces/counts residues** as a worklist; it does NOT decide them.
- **REVIEW GATE 1** — researcher inspects angle reports; scripts honed; variations captured as handled cases.
- **L2 = SYNTHESIS** — build on ALL angle results + the verse read to resolve residues (within-stem shade
  fear↔reverence · qualifier-route · cross-cluster reciprocal · homonym · multi-term pairing) → final
  per-verse output.
- **REVIEW GATE 2** — researcher inspects synthesis → then the single **DB UPDATE** writes.

**Build implications:** each angle is an independently runnable/honable sub-command (re-hone a weak angle
without re-running the cluster); residues are first-class L1 outputs (precise L2 worklist, never a blank
verse); the **synthesis is the only DB writer** (angles never write — keeps the meaning write auditable
against the reports that justified it); iteration is designed-in (several rounds early; a handled-variation
catalogue grows; speed comes from the catalogue, not from skipping the read). Extends
[[project_p2_l2_decision_architecture]] (type→modules→synthesise, now fed by explicit angle reports + two
gates). Detail: `research/investigations/wa-v3_2-l1-l2-architecture-synthesis-v1-20260608.md`. Folds into the
V3_2 instruction/rollup-design at the planned reread→update step.
