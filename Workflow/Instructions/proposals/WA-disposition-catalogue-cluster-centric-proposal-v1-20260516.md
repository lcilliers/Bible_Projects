# Proposal — Cluster-centric Phase 10 disposition catalogue (v2_0 → v2_1)

**Author:** CC, on researcher direction (2026-05-16)
**Trigger:** M01 Phase 10 reconciliation showed AI placing 20 of 24 items into `CARRY-TO-SESSION-D`, of which only ~4 are genuinely cross-cluster phenomena.
**Target document:** [Workflow/Instructions/wa-sessionb-cluster-instruction-v2_0-20260515.md](../wa-sessionb-cluster-instruction-v2_0-20260515.md) §13.2
**Status:** PROPOSAL — awaiting researcher approval before applying as v2_1

---

## 1. The problem

The current v2_0 §13.2 catalogue lumps two distinct things under `CARRY-TO-SESSION-D`:

> `CARRY-TO-SESSION-D` — the finding is cross-cluster / **cross-registry** and belongs to Session D, not this cluster

Two issues:

1. **"Cross-registry" terminology is obsolete.** Registries have been dissolved into clusters. The methodological unit is now the M-cluster, not the registry.
2. **The bucket conflates two routings.** A finding can belong to:
   - **(a)** another cluster's Session B (because it's about that cluster's characteristic), OR
   - **(b)** Session D's truly cross-cluster scope (≥3 clusters, programme-wide pattern, methodological)

These have different downstream consequences and cannot share one bucket.

## 2. The corollary about T6

T6 — Structural Relationships with Other Characteristics — is 24 prompts (T6.1 to T6.7) inside Phase 9. It already captures:

- T6.1 Co-occurrence with other characteristics
- T6.2 Sequential relationships
- T6.3 Causal/constitutive relationships
- T6.4 Vocabulary and root sharing
- T6.5 Distinctions / boundaries between characteristics
- T6.6 Shared verse anchors
- T6.7 Dimensional sharing

These prompts answer **bilateral cluster relationships** (this cluster ↔ another cluster) inside each cluster's own Phase 9. So strict Session D scope should be:

- **Programme-wide patterns** that span ≥3 clusters and cannot be fully expressed inside any one cluster's T6.
- **Methodological / structural observations** about how inner-being characteristics operate generally (e.g. spirit/soul/heart boundary findings, divine-pathos attribution patterns, commanded-inner-state grammar).

Session D should therefore be **few and very specific** — by intent, not by accident.

## 3. Proposed disposition catalogue (v2_1)

Replace the v2_0 §13.2 table with:

| Disposition | Meaning |
|---|---|
| `RESOLVED-BY-CATALOGUE` | The finding is already captured in one of the new cluster_finding rows (T0–T7) — name the cluster_finding T-code(s) + scope(s). |
| `FOLD-INTO-PROMPT` | The finding adds new evidence to an existing cluster_finding — name target T-code + scope; provide a 1–2 sentence fold note. |
| `NEW-CLUSTER-FINDING` | The finding is real new evidence that doesn't fit any existing prompt in *this cluster* — name a target T-code; provide canonical finding text. |
| `SUPERSEDED` | The finding was authored under the pre-cluster-pivot lens and is no longer relevant — name the replacing cluster_finding (or note "no replacement — characteristic moved" / "data error already corrected"). |
| **`ROUTE-TO-CLUSTER`** (new) | The finding's content belongs to **another cluster's Session B / Phase 9**. Name target cluster code (e.g. `M02-Anger`) if known; otherwise name the source registry and note "cluster not yet built." Status stays open; finding will be picked up when target cluster runs its Phase 10. |
| **`CARRY-TO-SESSION-D`** (reframed) | **Strict criterion:** a genuine cross-cluster phenomenon spanning **≥3 clusters** or a **programme-wide methodological** observation that no single cluster's T6 prompts can fully capture. Should be few and very specific. |
| `RESEARCHER-DECISION` | AI cannot decide; surface for researcher review. |

### Authoring guidance accompanying the catalogue (new §13.2.1)

> **Decision tree for AI:**
>
> 1. Is the finding's content already in a Phase 9 cluster_finding? → `RESOLVED-BY-CATALOGUE`
> 2. Does it add evidence to an existing Phase 9 finding in THIS cluster? → `FOLD-INTO-PROMPT`
> 3. Is it new evidence relevant to THIS cluster but missed in Phase 9? → `NEW-CLUSTER-FINDING`
> 4. Was it authored under a pre-cluster lens and is now obsolete? → `SUPERSEDED`
> 5. Does it concern ANOTHER cluster's characteristic / inner-being content? → `ROUTE-TO-CLUSTER`
> 6. Does it concern a pattern spanning ≥3 clusters or a programme-wide methodological observation? → `CARRY-TO-SESSION-D`
> 7. Unable to decide between two of the above? → `RESEARCHER-DECISION`
>
> **Important: bilateral cluster relationships (this cluster ↔ one other) are handled by T6 inside Phase 9, not by Session D.** If a finding raises a bilateral relationship not yet captured in this cluster's T6 findings, use `NEW-CLUSTER-FINDING` (target T6.x) rather than carrying to Session D.

## 4. Required apply-script changes (§13.4 Op A status mapping)

The Op A status mapping must be extended:

| Disposition | New `wa_session_b_findings.status` |
|---|---|
| `RESOLVED-BY-CATALOGUE` | `resolved` |
| `FOLD-INTO-PROMPT` | `folded` |
| `NEW-CLUSTER-FINDING` | `promoted` |
| `SUPERSEDED` | `superseded` |
| **`ROUTE-TO-CLUSTER`** | **`routed_cluster`** (new value; `resolution_note` records target cluster) |
| `CARRY-TO-SESSION-D` | `routed_session_d` |
| `RESEARCHER-DECISION` | `open` (with researcher_decision flag in resolution_note) |

`wa_session_research_flags` resolved-state semantics follow the same pattern (analogous columns).

## 5. Re-classification of M01 Phase 10 items under the strict catalogue

Of AI's 20 `CARRY-TO-SESSION-D` items, **16 should be `ROUTE-TO-CLUSTER` and only 4 are truly Session D.**

### `ROUTE-TO-CLUSTER` (16)

| Source | Target cluster | Rationale |
|---|---|---|
| sbf.71 R=anger | Anger cluster | Anger governance vocabulary |
| sbf.72 R=anger | Anger cluster | Compound anger-grief inner state |
| sbf.65 R=anxiety | Anxiety cluster | merimnaō dual register |
| sbf.60 R=brokenness | Brokenness cluster | Dimensional uniformity finding |
| sbf.31 R=distress | Distress cluster | riv group analytical question |
| sbf.62 R=distress | Distress cluster | Vocabulary scope note |
| sbf.47 R=wonder | Wonder/Astonishment cluster | Wonder cluster Session B work |
| sbf.106 R=abomination | Abomination cluster (T6) | Bilateral: abomination ↔ new-covenant transformation — Abomination's T6.3 (causal/constitutive) |
| srf.13 R=anger | Anger cluster (T6) | Bilateral: anger ↔ spirit governance — Anger's T6.5 (distinctions) |
| srf.14 R=anger | Anger cluster (T6) | Bilateral: anger ↔ abomination (za.am family) — Anger's T6.5 |
| srf.15 R=anger | Anger cluster (T7) | NT eschatological wrath theology — Anger's T7.2 / T7.3 |
| srf.16 R=anger | Anger cluster | Data completeness (G3709 orgē verse coverage) |
| srf.18 R=anger | Anger cluster (T6) | Bilateral: paroxusmos dual valence (conflict ↔ catalysis) — Anger's T6.3 |
| srf.27 R=anxiety | Anxiety cluster | Data completeness (G4329 prosdokia) |
| srf.28 R=anxiety | Anxiety cluster | Data completeness (G4328 prosdokaō) |
| srf.142 R=abomination | Abomination cluster (T6) | Bilateral: abomination ↔ redemption via XREF mechanism — Abomination's T6.4 (vocabulary sharing) |

Note: many srf rows previously labeled "cross-registry" are actually **bilateral cluster relationships** that the target cluster's T6 prompts will capture. They are not Session D items.

### `CARRY-TO-SESSION-D` strict (4)

| Source | Phenomenon | Why truly Session D |
|---|---|---|
| sbf.59 R=anguish | Divine pathos — God attributed inner affective response | Programme-wide pattern — applies across multiple clusters (anguish, anger, compassion, grief, sorrow). No single cluster's T6 can capture the full attribution pattern. |
| sbf.61 R=distress | Spirit-soul boundary / demonological-psychological interface | Methodological — concerns how spirit-level findings are framed across ALL clusters. No single cluster owns this. |
| srf.122 R=awe | Commanded-inner-state pattern across registries 11, 97, 42, "and likely others" | Programme-wide ≥3 clusters explicitly named. Not bilateral. |
| srf.130 R=fear | Tripartite dimension pattern (orientation / affect / will-collapse) | Programme-wide methodological — asks if this dimensional pattern recurs across other negative-state clusters. ≥3 clusters by implication. |

## 6. Implementation options

### Option I — Amend v2_0 to v2_1 now, re-author M01 Phase 10

- Bump instruction to v2_1 with the new catalogue + Op A status mapping.
- Update inherited-findings report template (cosmetic — "cluster" terminology in headers).
- Provide the strict-catalogue brief to AI; AI re-classifies the 20 items.
- Apply Phase 10 with the new dispositions.

**Cost:** one AI re-classification round-trip + small DB schema decision (whether to add `routed_cluster` status value to schema enum, or store target cluster in `resolution_note` only).

**Benefit:** every future cluster Phase 10 uses the correct catalogue from the start. M01 is the test case for v2_1.

### Option II — Apply M01 as v2_0 + amend v2_1 for future clusters

- Apply Phase 10 with the existing 20 `routed_session_d` statuses.
- Bump v2_1 with the new catalogue.
- Session D triage (eventually) re-classifies the 16 mis-routed items as `routed_cluster`.

**Cost:** Session D has to do clean-up later; M01's Phase 10 record carries the conflation.

**Benefit:** no AI re-classification round-trip now.

### Option III — Hand-edit M01 reconciliation JSON, apply v2_0 with extended apply-script

- CC manually splits the 20 into 16 route + 4 session-d in the reconciliation JSON.
- Apply-script handles both status values.
- Bump v2_1 for future clusters.

**Cost:** CC manual edit (well-defined; the classification above is the edit).
**Benefit:** no AI round-trip; M01 lands clean; v2_1 in place for next cluster.

## 7. Recommendation

**Option III** is the cleanest: CC owns the catalogue interpretation given researcher's explicit guidance; no need to ask AI to re-author what is essentially a categorisation refinement. The reclassification table in §5 is the working draft. Researcher confirms; CC produces the edited JSON; apply-script gets the new status value; v2_1 lands as the governing instruction for future clusters.

## 8. Scope NOT covered by this proposal

- The 189-prompt catalogue (T0–T7) was audited for registry-centric phrasing and is clean. No changes required.
- The schema columns (`registry_id`, `owning_registry`, `owning_registry_fk`) remain — they're historical DB structure, not analytical methodology. Renaming them is a separate concern (DB migration / OT-DBR).
- M46 (the prior cluster run) used v2_0 — its Phase 10 may have the same conflation, but is closed. Not in scope here.

---

*End of proposal.*
