# Directive DIR-20260420-002 — Dimension-label canonicalisation for 110 non-canonical rows

> Produced by: wa-directive-instruction-v1_1-20260418
> Governed by: wa-global-general-rules-v2_11-20260418
> Registry: global (cross-cluster, 110 rows in wa_dimension_index)
> Produced date: 2026-04-20
> Researcher approval: PENDING
> Related: `outputs/investigations/dimension-label-canonicalisation-plan-20260420.md`

---

## Motivation

Researcher direction 2026-04-20 established the **DimReview instruction §7.7** (currently v3.3) as the canonical source for dimension labels. Any patch-applied label outside the 11-label canonical set must be rejected by CC and reworked by Claude AI — this control is now in place via `CANONICAL_DIMENSIONS` in `apply_session_patch.py`.

A one-off mechanical migration ran on 2026-04-20 that canonicalised 3,139 rows across 23 source labels. **110 rows in 7 non-canonical labels remain** — these could not be mechanically mapped for two reasons:

- **Ambiguous (69 rows, 3 labels):** a single legacy label spans what the current vocabulary splits into 2+ dimensions. Per-group content reading is required to pick the correct canonical label.
- **No-clean-mapping (41 rows, 4 labels — including two spacing variants of the same name):** no obvious canonical counterpart. Candidates either for best-fit into existing §7.7 or for new-dimension proposal.

This directive asks Claude AI to produce a per-group proposed canonical mapping for the 110 rows. The output is a directive-result markdown; CC will encode the approved mappings as a DIMREVIEW patch in a subsequent step.

---

## Scope

**Read-only inputs:**

- `outputs/dim-label-noncanonical-rows-20260420.json` — 110 rows. Fields: `wdi_id`, `legacy_label`, `registry_no`, `word`, `group_code`, `context_description`, `dominant_subject`, `manual_override`.
- `wa-dimensionreview-instruction-v3_3-20260418.md` §7.7 — canonical vocabulary (11 dimensions).
- `wa-reference-v5_7-20260420.md` §4.3 — mirror reference; uses canonical form post-update 2026-04-20.

**Target rows by legacy label:**

| Legacy label | Rows | Nature |
|---|---:|---|
| `Affective/Emotional` | 32 | Ambiguous — split by valence (01 vs 02) |
| `Moral/Conscience` | 31 | Ambiguous — 05 (majority) vs 03 (conscience-as-awareness) |
| `Character/Disposition` | 6 | Ambiguous — 05 vs 06 per orientation |
| `Spiritual/God-ward` | 19 | No-clean-mapping — candidate for Dimension 12 OR best-fit to 11/10/04/06 |
| `Identity/Selfhood` | 8 | No-clean-mapping — candidate for new dimension OR best-fit |
| `Identity / Selfhood` | 8 | Same (spacing variant — analytically identical) |
| `Somatic/Embodied` | 6 | No-clean-mapping — candidate for 07 Vitality/Existence OR new dimension |

**Registry scope:** cross-cluster. Affected registries surface on read of the JSON input.

---

## Outcome required

A markdown file: `outputs/wa-global-dirresult-002-dim-label-proposals-v1-20260420.md`.

For each of the 110 rows, produce:

1. **`wdi_id`** (from input JSON — unchanged)
2. **Current legacy label** (from input JSON — unchanged)
3. **Proposed canonical label** — one of the 11 from §7.7
4. **One-sentence rationale** grounded in `context_description` content
5. **Confidence marker:** `HIGH` (clear mapping from context) · `MEDIUM` (defensible but analyst-judgement) · `LOW` (proposed best-fit; flag for researcher review)

For the **no-clean-mapping labels** (Spiritual/God-ward, Identity/Selfhood, Somatic/Embodied), additionally:

- Note whether a new dimension (Dim 12+) is warranted versus best-fit
- If new-dimension candidacy: propose a name + one-sentence scope statement for researcher ratification (would require DimReview instruction §7.7 revision)

**Summary table at top** — counts per proposed canonical label, confidence distribution, number of new-dimension candidates.

**Do NOT produce a patch in this directive.** The output is analyst proposals. CC will encode accepted proposals as a DIMREVIEW patch in a subsequent cycle (with researcher approval on any LOW-confidence / new-dimension entries).

---

## Completion confirmation

The directive-result file is the deliverable. CC pre-validates:

1. Every `wdi_id` from the input JSON is present in the output
2. Every proposed canonical label is in `CANONICAL_DIMENSIONS` (or declared as a new-dimension proposal with explicit justification)
3. Confidence markers present on every row

---

## Notes

**Why this is a directive rather than a patch:**

The dimension assignment requires analyst judgement (same class as Phase C work). CC cannot author the assignment without re-running the Phase B/C pattern per group, which is Claude AI's role. The directive delivers the raw material; the patch is produced after researcher accepts the proposals.

**Integration with §7.7 vocabulary evolution:**

If Claude AI proposes one or more new dimensions (12+), these are researcher-decision items per DR-13. The proposed mappings in this directive result should be expressed as "pending researcher approval of Dimension N" — Claude AI may propose both a best-fit under current vocabulary AND a candidate for an extended vocabulary.

**Coexistence with C01 Phase C output:**

r112 + r183 are DR=Complete under the canonical v3_3 vocabulary. The 110 rows are in OTHER registries (mostly legacy-anchored clusters with Complete-under-prior-versions status). This directive's output enables a programme-wide harmonisation without re-opening the C01 r112/r183 work.

**Linkage to other OT items:**

- **OT-DBR-015** (vocabulary vintage) — this directive resolves the backlog side. Forward side resolved by validator (Task 1 of the canonicalisation plan).
- Phase A observations (2026-04-20) anticipated these three "no-clean-mapping" labels as candidate new dimensions. Claude AI's proposals can cite those observations directly.

---

*Directive DIR-20260420-002 — produced 2026-04-20. 110-row dim-label canonicalisation proposals requested.*
