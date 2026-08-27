# M01 Phase 7 brief — VCG design within sub-groups

**Audience:** Claude AI
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_0-20260515.md](../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_0-20260515.md) §10 (Phase 7)
**Date:** 2026-05-16

---

## State of M01 at Phase 7 open

| Item | Count / value |
|---|---|
| Active terms in M01 | 81 |
| Active sub-groups | **8** (M01-A · M01-B · M01-C · M01-D · M01-E · M01-F · M01-G · M01-BOUNDARY) |
| `mti_term_subgroup` links | 106 (81 primary + 14 secondary + 11 BOUNDARY) |
| is_relevant verses routed to sub-groups | **951** |
| **P-status verses (is_relevant=1, no VCG)** | **31** — your job to assign to new VCGs |
| Inherited VCGs in DB | 116 — **NOT visible to you** (suppressed per v2_0 §2.3); Phase 8 will dissolve them after your work lands |
| Existing new VCGs | 0 — this phase creates them |
| cluster.status | `Analysis - In Progress` |

Phases 1–6 complete. Phase 7 produces the new VCG structure for each sub-group.

---

## Your task per v2_0 §10.2

Per sub-group, read the verse-meaning list. Cluster meanings into provisional VCGs — groups of verses with substantively similar inner-being content within this sub-group's register. Each VCG names a distinct inner-being phenomenon within the sub-group's characteristic.

For each VCG you design:

- `group_code` (suggested format: `{primary_term_mti_id}-{seq}` or `{subgroup_code}-VCG-{seq}` — CC assigns final ids on apply)
- `context_description` written from the meanings (one paragraph)
- Member verses (by `vc_id`)
- **Anchor verse** — the one verse that most directly and definitionally evidences the phenomenon
- Dual-membership notes — verses that legitimately belong to two VCGs

---

## Inputs

### Primary input

[Sessions/Session_Clusters/M01/wa-cluster-M01-subgroup-meanings-v1-20260516.md](wa-cluster-M01-subgroup-meanings-v1-20260516.md) — per-sub-group, every is_relevant verse with reference, term, and Phase 2 meaning. Canonical Bible order within each sub-group. **This is the only analytical material you need.**

### Reference (do not re-debate, but useful to know what's been decided)

- [WA-M01-dir-002-subgroup-routing-applied-v1-20260516.md](WA-M01-dir-002-subgroup-routing-applied-v1-20260516.md) — Phase 6 applied report. **Don't read for Phase 7 work; named here only so you can cite "CC Phase 6 §X" if you need to query a routing decision.**

### Suppressed by design

Inherited VCGs (116 in DB) are NOT in your input. Per v2_0 §2.3 (structural enforcement of the inherited-structure contamination guard), you design new VCGs purely from the meaning corpus. CC dissolves the old VCGs in Phase 8 with a researcher comparison report.

---

## Decisions already made — do NOT re-debate

1. **Sub-group structure** (8 sub-groups) is final. Don't propose renaming, merging, or splitting sub-groups at Phase 7. If you find a verse whose meaning fits a different sub-group than where it's currently routed, that's a Phase 7 cross-routing observation (note it, don't change sub-group structure).
2. **Term-to-sub-group placements** (106 links) are final. Don't re-debate which term belongs in which sub-group.
3. **BOUNDARY terms** (12) have their `M01-BOUNDARY` sub-group placement set. They typically get a single aggregating VCG, or per-term VCGs if their corpora warrant — your judgment.

---

## Special-handling flags from Phase 6

### 1. Deu 32:27 *gur* (mti=290) — divine inner state, set-aside candidate

This verse sits in M01-A (gur's primary placement, mechanical routing). Its meaning describes God's inner apprehension about how enemies would misinterpret divine judgment — i.e., the divine inner life, not the human inner being. The programme's scope is **human inner being only**.

**What to do:** do not assign Deu 32:27 to any M01-A VCG. Instead, flag it in your Phase 7 output as a set-aside candidate (`is_relevant=0`, set_aside_reason= "Describes God's inner apprehension, not human inner state — outside programme scope"). CC will apply the set-aside as a separate small operation alongside the Phase 7 directive.

### 2. 31 P-status verses (is_relevant=1, `group_id IS NULL`)

These verses came from the Phase 1 UT review (API classification). They have meanings (Phase 2 wrote `analysis_note`) and are routed to sub-groups (Phase 6 set `cluster_subgroup_id`) but have no VCG yet. They appear in the meanings report in their sub-groups.

**What to do:** include them in your VCG design. Each P-status verse joins one of the new VCGs you create.

### 3. H3372H *ya.re-revere* (mti=1682) — defaulted entirely to M01-A

AI's Phase 5 design did not detail cross-listings for H3372H (only H3372G mti=298 was detailed). CC's mechanical routing placed all H3372H verses in M01-A. Some H3372H verses likely belong analytically in M01-B (acute fear context) — same pattern as H3372G's documented cross-listings.

**What to do:** during Phase 7 VCG design for M01-A, if you see H3372H verses whose meaning is clearly acute fear (not reverential orientation), flag them as cross-routing-to-M01-B candidates. CC will apply the corrections alongside the Phase 7 directive.

### 4. 18 cross-listing references that didn't match active vc rows

Mostly mti=829 (H6343 *pa.chad*-noun) — references like `Isa 33:14`, `Isa 44:8`, `Job 23:15`, etc. These likely belong to a different mti in the database (probably the verb form H6342). They fell back to term-primary M01-A under the mechanical routing.

**What to do:** during Phase 7 you'll see actual M01-A meanings; if a pa.chad-noun verse's meaning is clearly acute (M01-B) or anticipatory (M01-F), flag it as a cross-routing candidate.

---

## Output expected from you

### 1. VCG design document per sub-group

For each substantive sub-group (M01-A through M01-G), one document:

`Sessions/Session_Clusters/M01/WA-M01-{subgroup_code}-vcg-design-v1-20260516.md`

Per VCG, list:

- Provisional `group_code` (e.g. `M01-A-VCG-01` or `298-VCG-01`)
- `context_description` (one paragraph)
- Member verses (vc_id + reference + term)
- Anchor verse (single vc_id with rationale)
- Dual-membership flags (verses also belonging to a second VCG)

For M01-BOUNDARY: a single section with the 12 BOUNDARY terms and a note that no full VCG design is warranted (placeholder VCG or set-aside aggregate).

### 2. VCG creation JSON

`Sessions/Session_Clusters/M01/WA-M01-vcg-creation-v1-20260516.json` — machine-readable form of the design, for CC to apply:

```json
{
  "M01-A": {
    "vcgs": [
      {
        "provisional_code": "M01-A-VCG-01",
        "description": "...",
        "verses": [12345, 12346, ...],
        "anchor_vc_id": 12345
      },
      ...
    ]
  },
  "M01-B": { "vcgs": [ ... ] },
  ...
}
```

### 3. Cross-routing flags (if any surfaced)

`Sessions/Session_Clusters/M01/WA-M01-phase7-cross-routing-flags-v1-20260516.md` — list of verses whose meaning suggests a different sub-group than current placement (per §"Special-handling flags" items 3 and 4). CC reviews and may apply small corrections alongside the Phase 7 directive.

### 4. Set-aside flag for Deu 32:27 gur

Included in the cross-routing flags document or as a separate one-line note. CC will set is_relevant=0 + set_aside_reason on apply.

---

## Discipline reminders

1. **No inherited VCG visible in your input.** Suppressed structurally per v2_0 §2.3. Each new VCG you design is grounded in the meaning corpus alone.

2. **Anchor verse must be the most directly definitional.** Not the most popular reference; the one whose meaning best names what the VCG describes.

3. **Anchor R4 rule:** every term that has any relevant verse must have at least one anchor (i.e. one of its verses is the anchor of some VCG it lives in). If a term's verses are all routed to VCGs but none of those VCGs picked one of the term's verses as anchor, that breaks R4. CC will check on apply.

4. **Per v2_0 §10.4: NO Pass C reconciliation.** Do not compare new VCGs against inherited VCGs. The inherited VCGs are not in your input precisely because you should not reconcile.

5. **Don't conflate VCGs across sub-groups.** Each VCG belongs to one sub-group. If two sub-groups have similar inner-being content, that's interesting but they remain distinct VCGs in distinct sub-groups — they are not merged.

6. **Output to new files, not in-place edits.** Phase 3's debate file was edited-in-place by appending an addendum — please produce v1 documents per the filenames above, not in-place modifications.

---

## When you're done

CC will:

1. Parse your VCG creation JSON.
2. Apply the Phase 7 directive: INSERT `verse_context_group` rows (one per new VCG), INSERT `vcg_term` links, UPDATE `verse_context.group_id` to route every is_relevant verse to its new VCG, UPDATE `verse_context.is_anchor=1` for each VCG's anchor.
3. Apply the cross-routing corrections + the Deu 32:27 set-aside alongside the directive.
4. Generate Phase 8 inputs — VCG dissolution comparison report (you don't participate in Phase 8; CC handles old VCG soft-delete with researcher gate).
5. Generate Phase 9 input — grouped report for catalogue prompts (your next chat involvement).

---

## Provenance

- Meanings report (primary input): [wa-cluster-M01-subgroup-meanings-v1-20260516.md](wa-cluster-M01-subgroup-meanings-v1-20260516.md)
- Phase 6 applied: [WA-M01-dir-002-subgroup-routing-applied-v1-20260516.md](WA-M01-dir-002-subgroup-routing-applied-v1-20260516.md)
- AI Phase 5 design: [WA-M01-subgroup-design-v1-20260516.md](WA-M01-subgroup-design-v1-20260516.md)
- Governing instruction: [wa-sessionb-cluster-instruction-v2_0-20260515.md](../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_0-20260515.md)

---

*End of Phase 7 brief.*
