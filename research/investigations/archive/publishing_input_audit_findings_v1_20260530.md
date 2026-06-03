# Publishing input audit — findings + gate proposal

**Generated:** 2026-05-30
**Trigger:** researcher question — *do the 7 chapter input files include all DB evidence for the cluster?*

This document reports the audit run on two clusters (M38 = post-split characteristic-anchored cluster; M15 = older characteristic-anchored cluster with full term inventory), identifies the systematic coverage gaps, and proposes a gate control and inclusion contract for the publishing instruction.

---

## 1. Audit method

Script: [scripts/_audit_cluster_input_coverage_v1_20260530.py](../../scripts/_audit_cluster_input_coverage_v1_20260530.py)

For a cluster, the audit queries every active evidence row in the DB and checks whether each row's identifying token appears in at least one of the 7 chapter input files:

| Evidence | Identifying token in inputs |
|---|---|
| `cluster_finding` | `question_code` (e.g. `T0.1.1`) |
| `cluster_subgroup` | `label` |
| `characteristic` | `short_name` |
| `verse_context_group` | `group_code` (e.g. `M38-A-VCG01`) |
| `verse_context.is_anchor=1` | verse `reference` |
| `cluster_observation` | (none — not surfaced) |
| `mti_term_subgroup` | `strongs_number` |
| VCG `context_description` | first 60 chars of description |

A gap = DB row whose identifier does not appear in any of the 7 files.

---

## 2. Audit results

### M38 (post-split, 7 characteristics, freshly authored)

Detail report: [outputs/markdown/cluster_input_coverage_M38_v1_20260530.md](cluster_input_coverage_M38_v1_20260530.md)

| Evidence | In DB | Missing from inputs |
|---|---|---|
| `cluster_finding` scope-groups | 1,512 | 8 |
| `cluster_subgroup` | 7 | 0 |
| `characteristic` | 7 | 0 |
| `verse_context_group` | 45 | 0 |
| `verse_context.is_anchor=1` | 45 | 0 |
| `cluster_observation` | 17 | **17 (all)** |
| `mti_term_subgroup` links | 0 | 0 (no links exist) |
| VCG `context_description` | 45 | **45 (all)** |

Notes on M38 missing findings: all 8 are `T5.7.3` gap findings — Phase D itself recorded that T2.8 input was not supplied to the segment. The gap-status finding is essentially "we couldn't answer this because the dependency was missing". These are real evidence rows, but they are about Phase D's own scaffolding, not about Salvation.

Note on M38 term linkage: M38 sub-groups have **zero `mti_term_subgroup` rows** — a v3_0 post-split data issue. The terms exist in `wa_term_inventory` but were not linked to the post-split sub-groups when the cluster was constructed. Separate from publishing coverage; flagged as a data issue.

### M15 (pre-v3_0 cluster, 8 characteristics + 1 BOUNDARY)

Detail report: [outputs/markdown/cluster_input_coverage_M15_v1_20260530.md](cluster_input_coverage_M15_v1_20260530.md)

| Evidence | In DB | Missing from inputs |
|---|---|---|
| `cluster_finding` scope-groups | 1,701 | 9 |
| `cluster_subgroup` (non-BOUNDARY) | 8 | 0 |
| `cluster_subgroup` (BOUNDARY) | 1 | **1** |
| `characteristic` | 8 | 0 |
| `verse_context_group` | 55 | **1** |
| `verse_context.is_anchor=1` | 55 | **1** |
| `cluster_observation` | 0 | 0 |
| `mti_term_subgroup` links | 123 | **31 (25%)** |
| VCG `context_description` | 55 | **55 (all)** |

---

## 3. The systematic coverage gaps

Across both clusters, three gap-types are systematic and traceable to the v1_0 publishing baseline retiring the appendices and Chapter 8:

### Gap A — VCG `context_description` not surfaced anywhere in chapter inputs

Every VCG carries a `context_description` field — the canonical statement of what that meaning-group is about. The current generator surfaces only the VCG's anchor verses and their per-verse `analysis_note`. The meaning-group's defining description is **never** placed in chapter inputs.

**Impact.** Whenever an AI authoring run needs to refer to a meaning-group, it has to infer the meaning-group's purpose from its anchor verses. The DB has the canonical description; the AI never sees it.

**Affected:** all 45 VCGs on M38, all 55 VCGs on M15 — 100% coverage gap.

### Gap B — Sub-group term inventory not in chapter inputs

The Strong's numbers, transliterations, and glosses that make up the cluster's vocabulary base were surfaced in Appendix A. The retirement of appendices in v1_0 made this evidence unreachable from chapter inputs.

**Impact.** AI authoring runs may quote a verse but have no canonical vocabulary record to ground the term — gloss, transliteration, language. This shows up especially in Chapter 2 ("introduce each characteristic") where naming the terms is part of the brief.

**Affected:** 31/123 (25%) on M15; M38 not measurable because of the upstream term-linkage data issue.

### Gap C — `cluster_observation` rows not routed to any chapter

The 17 M38 cluster observations include cross-register flags, characteristic emergence notes, BOUNDARY resolution decisions, and structural notes that the analytical phase wanted carried forward into publication thinking. None of them appear in any chapter input.

**Impact.** Evidence the analytical phase explicitly flagged as relevant to publication is silently dropped.

**Affected:** all 17 M38 observations; 0 on M15 (M15 predates the cluster_observation table).

### Gap D — Small per-chapter finding losses (~0.5%)

8/1512 findings on M38 and 9/1701 on M15 are not in inputs. On M38 they are all `T5.7.3` self-referential gaps. On M15 the pattern is similar (status-tier intersections that don't map to the current generator's per-chapter routing). Easy generator fix once we have a policy on whether `gap`-status findings should reach prose at all.

---

## 4. Proposed inclusion contract

The publishing instruction needs an explicit contract declaring which DB evidence MUST be in chapter inputs and which is excluded by policy. Without that contract, "missing from inputs" cannot be distinguished from "deliberately excluded".

### Category 1 — MUST appear in at least one chapter input (gate enforces ≥1 reference)

| Row type | Filter | Routes to |
|---|---|---|
| `cluster_finding` | `delete_flagged=0` AND `finding_status IN ('finding','silent','cluster_synthesis')` | Chapter routed by tier (see §4.1 below) |
| `cluster_subgroup` | `delete_flagged=0` AND `subgroup_code!='BOUNDARY'` | All per-characteristic chapters (Ch2..Ch7) |
| `cluster_subgroup` | `delete_flagged=0` AND `subgroup_code='BOUNDARY'` | Chapter 2 only (supporting-characteristics section) |
| `characteristic` | `delete_flagged=0` | Profile in cross-chapter scaffold; section header in Ch2..Ch7 |
| `verse_context_group` | active for the cluster | Chapter 2 (full description); chapter routed by tier (code only) |
| `verse_context` | active anchors only | Chapter routed by tier of the VCG's findings |
| `mti_term_subgroup` | active links | Chapter 2 (term inventory inline) |
| `cluster_observation` | `target_phase IN ('E','publication')` AND `status IN ('open','confirmed','refined')` | Routed by `observation_type` (see §4.2 below) |

### Category 2 — Excluded by policy (gate enforces 0 references)

| Row type | Filter | Reason |
|---|---|---|
| `cluster_finding` | `finding_status='gap'` | Analytical record says "no answer here". Absence is the finding; surfaced via the chapter's silence-principle prose, not as a finding row in EVIDENCE |
| `cluster_observation` | `target_phase NOT IN ('E','publication')` | Targeted at other phases (audit, follow-up) |
| anything | `delete_flagged=1` | Soft-deleted |

### Category 3 — Excluded by absence (gate ignores)

Row types not declared in Category 1 or 2 are out of scope for the gate. The instruction's §10 scripts-and-section-types section enumerates them.

---

## 5. Gate control specification

After Step 1 (input generation), CC runs:

```text
python scripts/_audit_cluster_input_coverage_v1_{date}.py --cluster {CODE} --strict
```

The `--strict` flag causes nonzero exit if any Category 1 row is not referenced or any Category 2 row is referenced.

A report is always written to `outputs/markdown/cluster_input_coverage_{CODE}_v{V}_{YYYYMMDD}.md` regardless of pass/fail.

**Behavior on FAIL:**
- Exit code 1.
- Step 2 (chapter authoring) MUST NOT begin until either:
  - The input generator is amended to include the missing evidence, then Step 1 re-run.
  - The publishing instruction's inclusion contract is amended to move the relevant row type into Category 2 with a documented reason.

**Behavior on PASS:**
- Exit code 0.
- Step 2 begins.

The gate is mechanical — it does not judge prose quality. It only confirms that every claim the AI could ground in DB evidence has the evidence in its input file.

---

## 6. Recommended generator amendments to close the gaps

To reach 100% Category 1 coverage with the current generator architecture, three concrete amendments are needed:

### 6.1 Surface VCG context_description in chapter inputs

Add a `**Meaning-group context:**` block under each VCG's anchor verses in chapter inputs where the VCG's findings are referenced. The block carries the `context_description` field verbatim.

Generator change: small — extend `fetch_sg_vcgs_with_anchors` to include `context_description`; emit it in `fmt_anchor` neighbouring block.

### 6.2 Surface sub-group term inventory in Chapter 2

Add a `**Terms for this characteristic:**` block in each Chapter 2 per-characteristic section, listing Strong's + transliteration + gloss inline (the same table the retired Appendix A carried, condensed into Ch2's per-characteristic section).

Generator change: small — extend `build_ch2` to call `fetch_sg_terms` and emit a compact term table per sub-group section.

### 6.3 Route cluster_observation rows to chapters

Active observations with `target_phase IN ('E','publication')` get routed by `observation_type`:

- `cross-register flag` → Chapter 6 (inter-characteristic relationships)
- `boundary-resolution` → Chapter 2 (supporting characteristics section)
- `emergent-characteristic` → Chapter 2 (per-characteristic section it concerns)
- `distribution-flag` → Chapter 1 (cluster-wide pattern statement)
- `design-note` (catch-all) → Chapter 6 by default, unless `cluster_subgroup_id` is set (then to the chapter where that sub-group is treated)

Generator change: medium — new `route_observation_to_chapter` helper + per-chapter emission of routed observations.

### 6.4 Resolve the `T5.7.3` gap-finding routing

Decide policy: should `gap`-status findings appear in inputs or not? The instruction's silence-principle is the right home for absences. Recommendation: `gap` findings stay excluded (Category 2) but the generator emits a count of gaps per chapter at the top of the chapter input so the AI knows how many "expected answers" the analytical record could not produce.

Generator change: trivial — emit a `**Analytical-record gap count for this chapter:** {N}` line.

### 6.5 Resolve M38's missing `mti_term_subgroup` links

Data issue, not a publishing-instruction issue. The post-split cluster constructor for M38 did not link the inherited terms to the new sub-groups. Separate ticket: backfill `mti_term_subgroup` rows for M38 from the parent M01 / pre-split linkage record.

---

## 7. What to add to the publishing instruction

Suggested new section, placed between §4 (Step 1) and §5 (Step 2):

> **§4.1 Evidence inclusion contract.** [Category 1 / Category 2 / Category 3 tables from §4 above]
>
> **§4.2 Per-chapter routing.** [the routing rules — tier-to-chapter for findings, observation-type-to-chapter for observations]
>
> **§4.3 Gate.** [the gate specification from §5 above]

Plus the §6 generator amendments delivered before the next cluster is published under v1_0.

---

## 8. Recommended next steps

1. **Researcher review** of the proposed inclusion contract — specifically the Category 2 declarations (excluding `gap` findings and non-publication observations). These are policy calls, not technical defaults.

2. **Amend the publishing instruction** with §4.1, §4.2, §4.3 reflecting the agreed contract.

3. **Amend the input generator** with the four changes in §6 above.

4. **Re-run Step 1** on M38 and confirm the audit passes in `--strict` mode.

5. **Wire the gate** into any orchestration script that runs Step 1 (the gate runs automatically after generation; failure halts the pipeline).

6. **Backfill M38's term linkage** as a separate data-quality task before the next publication run.

---

*This document is a working report. The audit script is the source of truth for the current state; the inclusion contract is the proposed addition to the publishing instruction.*
