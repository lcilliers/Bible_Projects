# v3_0 Phase B — control design

> **SUPERSEDED (2026-06-14)** by the v3_2 cluster-rollup model — `wa-cluster-rollup-design.md` / `wa-cluster-rollup-instruction-v3_2-DRAFT-20260607.md`. Retained for reference (v3_0 design phase); see `outputs/markdown/project-reconstruction/04-open-loops-and-incomplete-methodology-20260614.md` §4. Archiving pending the cleanup register.

**Date:** 2026-05-27
**Status:** Addresses procedural anomaly raised by researcher 2026-05-27. Supplements [v3_0 final review](wa-v3_0-final-review-v1-20260527.md) and [cycle comparison](wa-v2_9-vs-v3_0-cycle-comparison-v1-20260527.md).
**Trigger question:** *"on what basis is it fed into phase B — all the verses together? then phase B reads the terms to decide in the sub groups. All the terms in one go? what is the control to check AI has not gone off the rails. I assume next is to group the sub groups into characteristics? how do we prevent overload when it starts to read the verses to prepare the VCGs?"*

---

## §1. The procedural anomaly

The v3_0 final review described Phase B as *"Meaning grouping (constitution debate + sub-group design + VCG design + apply, in ONE AI session)"*. **That framing is wrong as a single-session design.** The work has three different input shapes, three different output shapes, three different validation gates. Trying to do it in one undifferentiated session produces exactly the overload risk the researcher named.

The right framing: **Phase B is one logical pipeline-stage with three internal stage-gates** (B.1 → B.2 → B.3). Each stage has its own input pack, its own AI output, its own CC validator, and its own researcher review. The "saving" relative to v2_9 is not session-count reduction — it is shared input scaffolding, single directive build, and a single structural apply at the end. The AI's analytical context can build progressively across the three stages instead of being rebuilt each phase.

---

## §2. Three stages — input / output / control

### §2.1 B.1 — Constitution debate (term-level verdicts)

**Question being answered:** for each cluster term, does its evidence corpus belong here? (STAYS / TRANSFERS-TO-{cluster} / BOUNDARY)

| Field | Detail |
|---|---|
| **Input pack** | Constitution report (CC-generated from DB). Per-term section: Strong's identity, gloss, verse counts, **every Pass A meaning for the term's IB-verses, one line per verse**. Plus §1 cluster characteristic statement and §4 programme cluster catalogue (for naming transfer targets). |
| **Input volume** | Term count × per-term IB-verse count. Typical: 15–30 terms × 5–200 verses. Worst case M05: ~30 terms × ~45 verses = ~1,300 meaning lines. Heavy but **structured** — AI walks term-by-term, not as one undifferentiated read. |
| **AI working pattern** | Sequential per-term. For each term: read all its Pass A meanings, judge against cluster characteristic statement, write verdict + rationale to obslog. The constitution report imposes the per-term ordering. |
| **AI output** | `WA-{code}-constitution-debate-v1-{date}.md` — one verdict block per term with rationale citing specific meanings. Decision summary table at end. |
| **CC stage gate (mandatory before B.2 starts)** | Existing v2_9 §6.3.1 + §6.3.2 pre-checks: <ul><li>Every term has a verdict.</li><li>Every BOUNDARY verdict cites one of the three valid reasons (not forbidden grounds).</li><li>Every TRANSFERS verdict's rationale establishes that **no verse in the corpus** evidences source-cluster relational content (the verse-level relationship test).</li><li>Every STAYS with cross-register flag names the other-register destination.</li></ul> Failure → resubmit; do not advance to B.2. |
| **Researcher review** | After CC pre-check passes. The constitution-debate file is the artefact. Researcher may push back on individual verdicts; CC applies the corrections inline before B.2. |
| **Overload control** | The per-term sectioning of the input report — AI doesn't try to absorb all ~1,300 meaning lines simultaneously. It walks term-by-term. The constitution-report builder is what makes this tractable. |

### §2.2 B.2 — Sub-group design (= characteristic design)

**Question being answered:** how does the (now stable) cluster's evidence split into sub-groups that each name an inner-being characteristic? (Default 1:1 sub-group : characteristic.)

**One clarification before the rest of the section, because it answers your question directly:**

> *"I assume next is to group the sub groups into characteristics?"*

**No — under v2_8+ design (which v3_0 inherits), sub-groups ARE characteristics.** The default is 1 sub-group : 1 characteristic. The "characteristic mapping" step (old Phase 8.7) is **silent CC mechanical** that copies sub-group label + core_description into the `characteristic` row. There is no second AI session that groups sub-groups into characteristics.

The only exception is the **§8.6 volume-split**: when a single characteristic's evidence corpus exceeds 40% of the cluster's substantive verses, the characteristic is split into multiple sub-groups by a documented split-axis. In that case multiple sub-groups bind back to ONE characteristic via `characteristic_subgroup` rows (CC-mechanical at the end of Phase C). The split-axis is documented in each sub-group's `core_description`. M04 v2 has Joy split across vertical-Joy / horizontal-Joy / corrupt-Joy sub-groups under one Joy characteristic — that pattern.

This is the discipline from [feedback_phase5_subgroups_represent_characteristics] — Phase 5/B.2 must be designed for characteristic representation from the start, not for raw meaning clustering.

Back to B.2 design:

| Field | Detail |
|---|---|
| **Input pack** | Post-constitution meaning corpus (STAYS terms only — TRANSFERS-OUT removed, BOUNDARY designated separately) **+** the cluster's keyword analytics report (`wa-cluster-{code}-keyword-analytics-v{V}-{date}.md`). Keyword analytics is the structural scaffolding that lets AI identify candidate sub-group axes without re-reading all 1,300 meaning lines from scratch. |
| **Input volume** | STAYS Pass A meanings (typically 80–95% of B.1 input volume) + keyword analytics (~5 KB). For M05: ~1,200 meaning lines + keyword analytics. |
| **AI working pattern** | Two-step internal: <ol><li>**Identify characteristics from keywords + sampled meanings.** Read keyword analytics to identify candidate characteristic axes. For each candidate, sample a handful of representative meanings to confirm.</li><li>**Assign every verse.** Walk the full STAYS meaning corpus, assigning each verse to a sub-group (= characteristic). Multi-faceted terms get primary + secondary. Apply §8.6 distribution check internally.</li></ol> |
| **AI output** | <ul><li>`WA-{code}-subgroup-design-v1-{date}.md` — list of sub-groups with code, label, core_description, evidence basis.</li><li>`WA-{code}-subgroup-mapping-v1-{date}.json` — `{vc_id: subgroup_code}` for every IB verse.</li></ul> |
| **CC stage gate (mandatory before B.3 starts)** | <ol><li>Every IB vc_id has a sub-group assignment.</li><li>Every sub-group has a core_description written from meanings.</li><li>**§8.6 distribution gate** — no substantive sub-group holds more than 40% of cluster's substantive verses. Pass/fail validator already exists: `scripts/_validate_cluster_phase5_distribution_v1_20260517.py`.</li><li>BOUNDARY sub-group, if present, contains only verses of BOUNDARY-verdict terms (the §8.4.1 anti-parking-lot check).</li></ol> Failure on any → resubmit; do not advance to B.3. |
| **Researcher review** | After CC pre-check passes. The sub-group-design file is the artefact. Researcher confirms each sub-group represents a coherent inner-being characteristic. |
| **Overload control** | **Keyword analytics as the scaffolding.** Without it, AI would need to derive sub-group axes from raw meaning reading — which on a 1,300-line corpus exceeds reliable working context. With keyword analytics, AI starts from a structured frequency/co-occurrence summary and confirms with targeted re-reads. This is the [feedback_phase2_passa_emits_keywords] payoff — the keyword scaffolding makes B.2 tractable. |

### §2.3 B.3 — VCG design within sub-groups

**Question being answered:** within each sub-group, what are the distinct verse-meaning groupings (VCGs) that name finer-grained phenomena under the sub-group's characteristic?

| Field | Detail |
|---|---|
| **Input pack** | Per-sub-group verse-and-meaning report (CC builds from B.2 output + DB). One report per sub-group, containing just that sub-group's verses with Pass A meanings. |
| **Input volume** | Per sub-group: 30–400 verses typically (the §8.6 gate caps any sub-group at 40% of cluster). Worst case a near-cap sub-group could approach 600 verses, but those would have triggered §8.6 split before reaching B.3. |
| **AI working pattern** | **Sequential per-sub-group, with mandatory write-out** (v2_9 §10.7 discipline preserved verbatim): <ol><li>Read all verse-meanings in sub-group N's section.</li><li>Design VCGs for sub-group N (typically 2–5 VCGs).</li><li>Write design document + sum-verification line to disk **immediately**.</li><li>Append obslog entries for sub-group N's VCG decisions.</li><li>Verify per-sub-group sum (VCG members = sub-group verse count). Do not advance until sum verifies.</li><li>Move to sub-group N+1; repeat.</li></ol> This is the heart of the overload protection — working memory clears between sub-groups; durable artefacts produced even if a later sub-group needs re-attempting. |
| **AI output** | <ul><li>One `WA-{code}-{subgroup_code}-vcg-design-v1-{date}.md` per sub-group (N files for N sub-groups).</li><li>One unified `WA-{code}-vcg-creation-v1-{date}.json` after all sub-groups complete.</li><li>Cross-routing flags document if any verses surfaced needing routing review.</li></ul> |
| **CC stage gate (before structural apply)** | Existing v2_9 §10.8 no-sampling pre-submission checklist verified mechanically by CC: every anchor in its VCG's members, sum per sub-group equals input count, total across cluster equals cluster's IB count, no phantom vc_ids, no cross-sub-group leakage unless dual-membership flagged, BOUNDARY-VCG carries all BOUNDARY terms' verses. Plus the v2_9 §10.9 DB-join validation (every vc_id exists with is_relevant=1, delete_flagged=0, cluster_code matches). Failure → resubmit per-sub-group delta report. |
| **Researcher review** | After CC checklist + DB validation pass. Researcher reviews the unified VCG design (or per-sub-group if she prefers). |
| **Overload control** | **Sub-group-by-sub-group with disk write between each.** Same as v2_9 §10.7. The mandatory write-out is non-negotiable — it is the only thing that keeps AI from holding the whole cluster's VCG design in working memory simultaneously. |

---

## §3. Phase C — the structural apply that follows Phase B

Phase B produces three artefacts. Phase C is the **single CC structural apply** that consumes all three:

| Op | Source | DB write |
|---|---|---|
| C.1 — Term transfers + BOUNDARY designation | B.1 constitution-debate file | `wa_term_inventory.cluster_code` updates for TRANSFERS; `wa_term_inventory.boundary_flag=1` for BOUNDARY; cross-register flag → `wa_term_inventory.cross_register_target` |
| C.2 — Sub-group create + verse routing | B.2 mapping JSON | INSERT `cluster_subgroup` rows; UPDATE `verse_context.cluster_subgroup_id` |
| C.3 — Inherited-VCG soft-delete | (no AI input — silent CC mechanical) | UPDATE `verse_context_group.delete_flagged=1` for inherited VCGs; UPDATE `verse_context.group_id=NULL` for affected vc rows |
| C.4 — VCG create + verse routing | B.3 unified VCG JSON | INSERT new `verse_context_group` rows; INSERT `vcg_term` links; UPDATE `verse_context.group_id` to new VCGs; UPDATE `is_anchor` |
| C.5 — Characteristic load (silent, 1:1 default) | Derived from B.2 (sub-group → characteristic 1:1; volume-splits bind via `characteristic_subgroup`) | INSERT `characteristic` rows; INSERT `characteristic_subgroup` rows |

**Single directive, single apply, single validation report.** Phase C is heavy in DB terms but mechanical — no AI involvement, no researcher gate (researcher already approved the three B artefacts).

---

## §4. The cycle accounting — corrected

The v2_9 vs v3_0 cycle comparison (v1) framed Phase B as a single AI session. With this design, that framing is wrong. Corrected accounting:

| Layer | v2_9 cycle | v3_0 (with B.1/B.2/B.3 staging) | Δ |
|---|---:|---:|---:|
| AI sessions for grouping work (P3+P5+P7 / B.1+B.2+B.3) | 3 | 3 | 0 |
| Researcher review gates within grouping work | 3 | 3 | 0 |
| CC directives within grouping work (P4 + P6 + P7 apply) | 3 | 1 (Phase C) | **−2** |
| Input pack builds (one per AI session) | 3 | 3 (but share governing instruction + global rules + science extract loading) | 0 nominally; *less wall-time* in practice |

So the **AI-session reduction in Phase B vs v2_9 Phase 3+5+7 is zero**. The savings are:

1. **Single structural apply at end** instead of three (Phase 4, Phase 6, Phase 7-apply).
2. **Shared input scaffolding** — the constitution report, keyword analytics, and Pass A meanings load once and are referenced across B.1/B.2/B.3.
3. **Analytical continuity** — AI's working understanding of the cluster builds from B.1 → B.2 → B.3 without three sessions of cold-start.
4. **One v3_0 phase boundary instead of three v2_9 phase boundaries** — cleaner status discipline, simpler obslog.

The **headline cycle reduction from §2.2 of the v2_9 vs v3_0 comparison still holds for**:
- Session C → CC assembly + Phase E findings-driven prose: 7–8 verse-corpus reads eliminated.
- Phase F (combined P10+P11+P12): conditional AI session removed in normal case.

But Phase B does not contribute to the cycle reduction. **Its contribution is structural cleanliness, not cycle-count.** The cycle comparison v1 needs a corrigendum.

---

## §5. Answers to the specific questions

> *"on what basis is it fed into phase B — all the verses together?"*

**B.1 input** = constitution report (per-term sections, each containing that term's Pass A meanings). All verses present, but **structured term-by-term**, not flat.

**B.2 input** = post-constitution STAYS meaning corpus + keyword analytics. All STAYS verses' meanings, **structured by term**, with keyword analytics as the candidate-axis scaffolding.

**B.3 input** = per-sub-group reports. **One sub-group at a time.** AI never sees the whole cluster's verse corpus at B.3.

> *"then phase B reads the terms to decide in the sub groups. All the terms in one go?"*

**B.1**: yes, all terms in one input — but processed term-by-term sequentially. The structure protects against undifferentiated reading.

**B.2**: yes, all STAYS terms' meanings in one input — but the keyword analytics provides the structural scaffolding so AI doesn't derive characteristics from raw 1,300-line scan.

> *"what is the control to check AI has not gone off the rails?"*

Four checkpoints (already-existing in v2_9, preserved as stage gates inside Phase B):

1. **B.1 → B.2 gate.** CC pre-checks the constitution-debate file: every verdict present; BOUNDARY grounds valid (not forbidden); TRANSFERS pass the verse-level relationship test; STAYS-with-flag names destination + relationship. Failure → resubmit before B.2 starts.
2. **B.2 → B.3 gate.** CC runs the §8.6 distribution validator (40% ceiling), the §8.4.1 BOUNDARY-not-a-parking-lot check, and the every-verse-assigned check. Failure → resubmit before B.3 starts.
3. **B.3 → C gate.** CC runs the §10.8 no-sampling checklist + §10.9 DB-join validation. Failure → resubmit (per-sub-group delta report tells AI exactly what's missing).
4. **Researcher review** after each CC pre-check passes. Three review gates inside Phase B — same as v2_9 had.

> *"I assume next is to group the sub groups into characteristics?"*

**No.** Sub-groups ARE characteristics — 1:1 default, designed for characteristic representation from B.2 onward (per [feedback_phase5_subgroups_represent_characteristics]). The "characteristic load" step is silent CC mechanical (C.5) — it copies sub-group attributes into `characteristic` rows. No AI session, no merge logic, no separate grouping question.

The only exception is the **§8.6 volume-split**: when one characteristic has too many verses for one sub-group, B.2 splits it into multiple sub-groups under one characteristic identity. The splits bind back via `characteristic_subgroup` rows in C.5. This is rare (M04 Joy precedent) and is decided AT B.2, not as a separate post-B step.

> *"how do we prevent overload when it starts to read the verses to prepare the VCGs?"*

B.3 already inherits v2_9 §10.7's discipline verbatim:

- **One sub-group at a time.**
- **Mandatory disk write after each sub-group** (design document + sum-verification line).
- **Append to obslog after each sub-group.**
- **Sum-verification must pass before advancing.**
- **Working memory clears between sub-groups.**

This is the most-tested overload protection in the v2_9 pipeline (M04 / M07 / M08 precedent). It is not changed in v3_0.

If a single sub-group exceeds ~400 verses (rare given §8.6 would have caught it), B.3 falls back to per-tier segmentation within the sub-group — same pattern as Phase 9 segmentation.

---

## §6. What this means for v3_0 instruction text

The v3_0 instruction needs to write Phase B not as one section but as **§6.0 Phase B overview + §6.1 B.1 + §6.2 B.2 + §6.3 B.3 + §7 Phase C apply**. Each B.x sub-section reproduces (with light editing) the existing v2_9 §6 / §8 / §10 specifications, including the §6.3.1/§6.3.2/§8.4.1/§8.6/§10.7/§10.8/§10.9 disciplines. The novelty in v3_0 is purely the consolidation under one phase identity and the single Phase C apply at the end — the analytical controls are unchanged.

The v2_9 vs v3_0 cycle comparison v1 needs §2.1 corrected: **AI session count in the grouping work is 3 in both v2_9 and v3_0**. The cycle savings come from elsewhere (Session C collapse, CC op consolidation).

---

*v1 — 2026-05-27. Pre-write design for v3_0 §6 (Phase B).*
