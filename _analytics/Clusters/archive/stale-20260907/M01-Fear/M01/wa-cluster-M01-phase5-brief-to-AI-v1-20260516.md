# M01 Phase 5 brief — sub-group formation from meanings

**Audience:** Claude AI
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_0-20260515.md](../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_0-20260515.md) §8 (Phase 5)
**Date:** 2026-05-16

---

## State of M01 at Phase 5 open

| Item | Count / value |
|---|---|
| Active terms in M01 | **81** (94 − 13 transferred in Phase 4) |
| Verses with Phase 2 meanings | **~948** (every is_relevant active vc row has `analysis_note`) |
| cluster.status | `Analysis - In Progress` |
| Sub-groups currently defined | **0** — this phase creates them |
| Inherited VCGs visible | **0** in your input — suppressed per v2_0 §2.3 |

Phases 1–4 complete. Phase 5 produces the sub-group structure.

---

## Your task per v2_0 §8.3

Read every Phase 2 meaning across the 81 terms. Identify clusters of meaning — groups of verses (from any term) whose inner-being content is substantially similar. Each cluster becomes a sub-group. The sub-group is named by what its meanings collectively name.

**The non-negotiable:** sub-groups emerge from the meaning corpus — not from gloss-list interpretation, not from prior session inherited VCGs (which are not visible), not from your memory of how fear-cluster might be structured.

---

## Inputs

### Primary input

[Sessions/Session_Clusters/M01/wa-cluster-M01-constitution-v1-20260516.md](wa-cluster-M01-constitution-v1-20260516.md) — regenerated post-Phase-4. Contains:

- §1 — Cluster characteristic statement + gloss list (81 terms)
- §2 — Per-term identity + meaning corpus, one line per is_relevant verse (≈948 lines total)
- §3 — Cross-term meaning-vocabulary signals (Jaccard ≥ 0.30)
- §4 — Programme cluster catalogue (for reference only — no transfers in Phase 5)

### Decisions already made (do not re-debate)

**12 BOUNDARY terms — already verdicted in Phase 3. Create `M01-BOUNDARY` sub-group; place these 12 in it.** Source: WA-M01-dir-001-term-transfer-applied-v1-20260516.md §What stays in M01.

| BOUNDARY term | mti_id | Phase 3 question |
|---|---:|---|
| G0085 ademoneo | 2 | Anguished heaviness — M03 or M24? |
| G2285 thambos | 1245 | Pure wonder-amazement, no destination cluster |
| H2189 za.a.vah | 1162 | All verses set aside — empty corpus |
| H3735 ke.ra | 152 | Spirit-level distress, thin corpus |
| H4867 mish.bar | 4814 | Overwhelming divine pressure — M01 or M24? |
| H6125 a.qah | 5157 | Crushed by hostile force — M01 or M24? |
| H7661 sha.vats | 240 | Agony of dying — M24 likely |
| H8312 sar.ap.pim | 349 | Anxious ruminating thoughts — M01 or M20? |
| H8539 ta.mah | 289 | Astonishment-bewilderment split — M01 or M20? |
| H8047G sham.mah | 1161 | All verses set aside — empty corpus |
| H6178 a.ruts | 1777 | All verses set aside — empty corpus |
| H6426 pa.lats | 1719 | All verses set aside — empty corpus |

**3 STAYS terms not verdicted in Phase 3 — treat as STAYS, place in regular sub-groups per their corpus.** These were not reached in either pass; their meaning corpora ARE in the §2 of the new constitution report.

| Term | mti_id |
|---|---:|
| H0367 e.mah (terror) | 284 |
| G5156 tromos (trembling) | 308 |
| H0366 a.yom (terrible) | 1722 |

---

## Output expected from you

### 1. Sub-group design document

File: `Sessions/Session_Clusters/M01/WA-M01-subgroup-design-v1-20260516.md`.

For each sub-group:

- `subgroup_code` — e.g. `M01-A`, `M01-B`, …, `M01-BOUNDARY`
- `label` — short human-readable name (e.g. "Reverential Fear / Fear of God")
- `core_description` — one paragraph written from the meanings, naming the inner-being phenomenon the sub-group's verses collectively evidence
- Term roster: list of terms (Strong's + transliteration + mti_id) primary to this sub-group
- Multi-faceted terms: terms whose meanings span more than one sub-group — note the primary placement and the secondary/other sub-groups they touch

`M01-BOUNDARY` sub-group is mandatory (12 terms listed above; description = "Terms with analytical question or empty corpus, held for researcher decision").

### 2. Verse-to-sub-group mapping (only where needed)

Per the v2_0 §2.7 principle (atomic-per-row work uses JSON templates; synthesis stays in chat) and our prior conversation: **for terms whose corpus is uniform in sub-group placement, the term's primary sub-group placement carries all its verses mechanically** — CC handles the routing in Phase 6 without per-verse decisions.

You only need to flag the **multi-faceted terms** where some verses go to one sub-group and other verses go to another. For these, list:

- Term Strong's
- Primary sub-group (most verses)
- For each verse going to a non-primary sub-group: `vc_id` + reference + sub-group destination + one-line rationale

If after reading the corpus you find that all 81 terms are single-sub-group (no cross-listings), say so and CC handles the entire routing mechanically. If you find cross-listings, list them.

### 3. Obslog entries

Phase 5 reasoning recorded in the cluster obslog — each provisional sub-group with its T1 framework checks (per the cluster instruction's T1 framework still in force).

---

## Discipline reminders

1. **No inherited VCG visible in your input.** Suppressed by design per v2_0 §2.3. If you find yourself trying to recall existing VCG labels — stop. Read the meaning corpus.

2. **Sub-group design is meaning-grounded.** Each sub-group's `core_description` must be writeable from the meanings under that sub-group. If you can't write the description without referring to the gloss list, the sub-group isn't characteristic-bearing.

3. **Don't prematurely route every verse.** CC handles verse-to-sub-group routing mechanically in Phase 6. Your job is the structure — the sub-groups themselves — not per-verse decisions for the 948 verses (with the exception of multi-faceted-term cross-listings noted above).

4. **Output format matters.** If you produce a JSON output for the multi-faceted cross-listings, use a flat list: `[{vc_id, reference, term_strongs, primary_sg, secondary_sg, rationale}, ...]`. CC parses this directly.

5. **Phase 5 is not exhaustive analysis.** This phase is structural. Phase 7 designs VCGs within each sub-group. Phase 9 does the catalogue prompts. Don't try to write findings during Phase 5.

---

## When you're done

Return the sub-group design document. CC will:

- Apply the structure to the DB in Phase 6 (`cluster_subgroup` INSERTs + `mti_term_subgroup` INSERTs + `verse_context.cluster_subgroup_id` UPDATEs mechanical from term-primary placement + your multi-faceted cross-listings).
- Produce the Phase 7 input report (per-sub-group verses + meanings).

Then you receive that report for Phase 7 VCG design within each sub-group.

---

## Provenance

- Constitution report: [wa-cluster-M01-constitution-v1-20260516.md](wa-cluster-M01-constitution-v1-20260516.md) (221 KB; 81 terms; ~948 meaning entries)
- Phase 4 applied: [WA-M01-dir-001-term-transfer-applied-v1-20260516.md](WA-M01-dir-001-term-transfer-applied-v1-20260516.md)
- Phase 3 debate: [wa-M01-constitution-debate-v1-20260516.md](wa-M01-constitution-debate-v1-20260516.md) + [addendum](wa-cluster-M01-constitution-focused-rereadgreek-v1-20260516.md)
- Pass A meanings applied: [WA-M01-passa-meanings-applied-v1-20260515.md](WA-M01-passa-meanings-applied-v1-20260515.md)
- Governing instruction: [wa-sessionb-cluster-instruction-v2_0-20260515.md](../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_0-20260515.md)

---

*End of Phase 5 brief.*
