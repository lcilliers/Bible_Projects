# M04 Phase 5 brief v2 — Sub-group design (RESUBMISSION after distribution gate trip)

**Audience:** Claude AI
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_3-20260517.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_3-20260517.md) §8 (Phase 5) — note **§8.6 distribution hard gate** added 2026-05-17
**Date:** 2026-05-17
**Supersedes:** [Phase 5 brief v1 (rejected — see files phase 5 rejected v1/)](files%20phase%205%20rejected%20v1/WA-M04-phase5-brief-to-AI-v1-20260517.md)

---

## ⛔ Why this is a resubmission

The first Phase 5 design (v1) was **rejected** by the new §8.6 distribution hard gate. AI's v1 design placed 661 of 816 substantive verses (**81%**) into one sub-group (M04-A "Exultant Joy in the LORD"), well above the 40% threshold.

**Phase 6 rollback applied** ([WA-M04-dir-002-rollback-applied-v1-20260517.md](WA-M04-dir-002-rollback-applied-v1-20260517.md)): all M04 cluster_subgroup, mti_term_subgroup, and verse_context.cluster_subgroup_id assignments soft-deleted. Cluster.status remains `Analysis - In Progress`. The 58 active terms (43 STAYS + 15 BOUNDARY) and their Phase 2 meanings are intact.

The AI's v1 analytical work is preserved in `files phase 5 rejected v1/` for reference. **Do not re-use v1's structure directly** — the issue was sub-group granularity, not the underlying analysis.

---

## State of M04 at Phase 5 v2 open

| Item | Count |
|---|---|
| Active terms (post-Phase-4) | **58** (43 STAYS + 15 BOUNDARY) |
| Active is_relevant verses | **1138** (816 STAYS + 322 BOUNDARY) |
| `verse_context.analysis_note` coverage | 100% for OWNER verses |
| `cluster.status` | `Analysis - In Progress` |

---

## §1. The §8.6 distribution hard gate

**Rule:** no single substantive (non-BOUNDARY) sub-group may hold more than **40%** of the cluster's substantive verses. If exceeded, CC rejects Phase 5 and AI must re-submit with finer-grained splits.

**Benchmark across closed clusters** (biggest substantive sub-group share):

| Cluster | Biggest SG share | Status |
|---|---:|---|
| M01 Fear | 35% (M01-A Reverential Fear of God) | passes |
| M02 Anger | 47% (M02-B Burning Rage) | borderline / would fail gate retroactively |
| M03 Grief | 33% (M03-A Weeping) | passes |
| **M04 v1 (REJECTED)** | **81%** (M04-A Exultant Joy in the LORD) | **failed gate** |

Target for v2: every substantive sub-group ≤ 40% of substantive corpus (816 v). That means no sub-group bigger than **~326 verses**. Realistically, the largest substantive sub-group in v2 should sit around 200–280 verses.

---

## §2. What the distribution preview tells us (post-Phase-4)

Register-family rollup of the 43 STAYS terms (see [WA-M04-phase4-distribution-preview-v1-20260517.md](WA-M04-phase4-distribution-preview-v1-20260517.md) for the full preview):

| Register family | Terms | Verses | % of STAYS corpus |
|---|---:|---:|---:|
| **Joy / Rejoicing** (R097 joy + R132 rejoicing) | 21 | **539** | **66.1%** ← must split |
| Delight / Pleasure (R042 delight + R043 desire) | 13 | 178 | 21.8% |
| Wonder / Marvel (R175 wonder) | 3 | 77 | 9.4% |
| Pleasantness (R103 love → na.im) | 1 | 11 | 1.3% |
| Cheer / Encouragement (R187, R035, R033, R183) | 2 | 6 | 0.7% |
| Gladness / Cheer (R186 gladness) | 3 | 5 | 0.6% |

The **Joy / Rejoicing** family at 539 verses is the dominant problem. It must split into **multiple sub-groups** at the Phase 5 level (NOT at the VCG level — that's the v1 mistake).

---

## §3. Required splits — Joy / Rejoicing family

The Joy / Rejoicing register's 539 verses naturally split along these axes (visible in the term + meaning corpus, which v1 actually identified at the VCG level but kept all in one sub-group):

| Proposed sub-group axis | Approx verses | Sample terms / verses |
|---|---:|---|
| **Vertical: Joy/exultation directed AT YHWH** | ~120–150 | sa.mach + gil + chairō verses with "in the Lord" / "before the LORD" / "in his salvation" (Psa 5:11; 9:2; 13:5; 16:9; 35:9; 70:4; Hab 3:18; Phil 4:4) |
| **Communal: Worship-joy, festive rejoicing, gladness expressed in song/dance/feast** | ~80–110 | sim.chah + ma.s.vo.s + sa.mach festival contexts (Lev 23; Deu 12, 16; Neh 8, 12; 1Ch 15, 29; Psa 33, 100) |
| **Joy at God's saving acts / deliverance** | ~60–90 | sa.mach + gil + su.s deliverance-celebration verses (Exo 15; Psa 9; 92; 118; Isa 12) |
| **NT joy in Christ / Spirit / gospel** | ~50–80 | chairō + chara verses in Paul + John + the Synoptics (Joh 15:11; 16:22; Rom 14:17; Gal 5:22; Phil 1:18, 25; 1Th 1:6; 1Pe 1:6, 8) |
| **Joy in suffering paradox** | ~20–35 | chairō + agalliao counter-intuitive joy (Mat 5:12; Rom 5:3; Jam 1:2; 1Pe 1:6, 8; 4:13; 2Cor 6:10; Phil 1:18) |
| **Inverted / corrupt / hostile joy** | ~40–55 | sa.mach + ma.s.vo.s of enemies / wicked rejoicing (Pro 17:5; Eze 25:6; 26:2; 35:15; Psa 35:15, 19, 24; Lam 1:21; 4:21) |
| **Eschatological / promised joy** | ~30–50 | sim.chah + sa.s.von + ma.s.vo.s of restored Zion (Isa 35:10; 51:11; 60:15; 61:7, 10; 65:18–19; 66:10; Jer 31:13; Zec 8:19) |
| **Inner-location: heart-joy / heart-rejoicing** | ~20–40 | sa.mach + sim.chah verses with "heart" explicit (Pro 15:13, 15; 17:22; 23:15, 24; 27:9; Psa 4:7; 19:8; 119:111; Ecc 5:20) |
| **Divine joy / God rejoicing OVER his people** | ~30–55 | sa.mach + su.s where God is the subject of joy (Isa 62:5; 65:19; Zep 3:17; Deu 30:9; Jer 32:41) |

These axes are **suggestive**, not prescriptive. Read the meanings; let the splits emerge from the corpus. But the END STATE must have:
- No substantive sub-group > 40% of 816v (i.e. > 326v)
- Plausibly 5–8 sub-groups from the Joy / Rejoicing family alone
- Plus separate sub-groups for Delight/Pleasure (178v could itself split), Wonder (77v), Pleasantness (11v), Cheer (6v), Gladness (5v) — these mostly stay as in v1
- Plus M04-BOUNDARY (15 terms, 322 verses)

Expected total: **8–13 substantive sub-groups + M04-BOUNDARY** = 9–14 total.

---

## §4. Your task per v2_3 §8

For each verse-meaning in the constitution report's §2 meaning corpora:

1. **Read every verse-meaning across the 58-term cluster** (term by term).
2. **Identify provisional sub-groups of meaning** — splitting the dominant joy register per §3 above into MULTIPLE sub-groups.
3. **Name each provisional sub-group**: `subgroup_code` (`M04-A`, `M04-B`, ..., `M04-BOUNDARY`), `label`, `core_description` (one paragraph from meanings).
4. **Place each term** — primary sub-group + secondary placements where verses span.
5. **Map every is_relevant vc row** to its sub-group via `verse_assignments_by_term`.
6. **Design `M04-BOUNDARY`** as a single structural sub-group holding the 15 BOUNDARY terms.

---

## §5. Inputs

### Primary analytical input

[Sessions/Session_Clusters/M04/wa-cluster-M04-constitution-v3-20260517.md](wa-cluster-M04-constitution-v3-20260517.md) — constitution v3 (post-Phase-4) with 58 terms and complete meaning corpora.

### Supporting context

- [WA-M04-phase4-distribution-preview-v1-20260517.md](WA-M04-phase4-distribution-preview-v1-20260517.md) — register-family preview
- [WA-M04-phase5-distribution-validation-v1-20260517.md](WA-M04-phase5-distribution-validation-v1-20260517.md) — v1 rejection report
- [files phase 5 rejected v1/WA-M04-subgroup-design-v1-20260517.md](files%20phase%205%20rejected%20v1/WA-M04-subgroup-design-v1-20260517.md) — v1's analytical content (use for register identification; do not re-use its sub-group structure)

### Governing instruction

[wa-sessionb-cluster-instruction-v2_3-20260517.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_3-20260517.md) §8.

---

## §6. Output expected from you

### Sub-group design document

`Sessions/Session_Clusters/M04/WA-M04-subgroup-design-v2-20260517.md`

Per sub-group block:

```markdown
## M04-X — {label}

**Core description:** One paragraph written from the meanings.

**Terms (primary):** {list of mti_ids + strongs + translit}
**Terms (secondary, if any):** {multi-faceted terms with primary elsewhere}

**Representative meanings (3-5 verses):**
- {reference} — {meaning excerpt}
```

### Mapping JSON

`Sessions/Session_Clusters/M04/WA-M04-subgroup-mapping-v2-20260517.json`

```json
{
  "cluster_code": "M04",
  "subgroups": [
    {
      "subgroup_code": "M04-A",
      "label": "...",
      "core_description": "...",
      "sort_order": 1,
      "term_placements": [
        {"mti_term_id": N, "strongs": "...", "translit": "...", "placement": "primary"}
      ]
    }
  ],
  "verse_assignments_by_term": {
    "mti_term_id_to_subgroup": {
      "<mti_id>": "M04-X"
    }
  }
}
```

**Critical**: BOUNDARY terms use `placement: "boundary"` in `term_placements`; substantive terms use `placement: "primary"` or `"secondary"`.

### Obslog entries

Append to existing M04 obslog or write fresh Phase 5 v2 obslog.

### ⚠️ STAGED WRITE-OUT

1. Draft design document → **disk immediately.**
2. Derive mapping JSON → **disk immediately.**
3. Append obslog entries → **save.**

---

## §7. Critical discipline reminders

1. **The biggest substantive sub-group must be ≤ 326 verses (40% of 816).** CC will reject any mapping that violates this.

2. **Sub-groups emerge from meanings, not gloss-list categories.** A single term (e.g. sa.mach with 147 verses) WILL split across multiple sub-groups because its verses span multiple registers. Don't keep a term wholly inside one sub-group if its corpus genuinely spans registers — use primary + secondary placements.

3. **v1's 10 M04-A VCGs were correctly-distinguished registers.** Convert them into sub-group-level distinctions for v2. Don't put 10 different registers under one sub-group umbrella.

4. **Drop the 22 invalid vc_ids from v1**: 15 were M42 misinclusions (rin.nah H7440, ra.nan H7442B — owned by R208 shouting / M42 Speech, NOT M04); 7 don't exist in DB. v2 must not include these.

5. **No characteristic-bearing analysis of BOUNDARY at Phase 5.** Single aggregating sub-group with one-paragraph note.

6. **Mapping JSON is the source of truth for verse routing.** Multi-faceted terms get primary + secondary at the term level; each verse routes to one sub-group via the mapping.

---

## §8. When you're done

CC will:

1. Run the §8.6 distribution validator on the new mapping JSON. If it fails again, re-submit again.
2. If passes: build Phase 6 apply script, apply directive (INSERT cluster_subgroup, mti_term_subgroup, UPDATE verse_context.cluster_subgroup_id).
3. Generate Phase 7 input report and brief.

---

## §9. Provenance

- Updated constitution (primary input): [wa-cluster-M04-constitution-v3-20260517.md](wa-cluster-M04-constitution-v3-20260517.md)
- Distribution preview: [WA-M04-phase4-distribution-preview-v1-20260517.md](WA-M04-phase4-distribution-preview-v1-20260517.md)
- v1 rejection report: [WA-M04-phase5-distribution-validation-v1-20260517.md](WA-M04-phase5-distribution-validation-v1-20260517.md)
- Phase 7 validation (which surfaced the original gap): [WA-M04-phase7-validation-v1-20260517.md](WA-M04-phase7-validation-v1-20260517.md)
- Phase 4 applied: [WA-M04-dir-001-term-transfer-applied-v1-20260517.md](WA-M04-dir-001-term-transfer-applied-v1-20260517.md)
- Phase 6 rollback applied: see [WA-M04-dir-002-rollback-applied-v1-20260517.md](WA-M04-dir-002-rollback-applied-v1-20260517.md) (next)
- Rejected v1 inputs preserved: [files phase 5 rejected v1/](files%20phase%205%20rejected%20v1/)
- Governing instruction: [wa-sessionb-cluster-instruction-v2_3-20260517.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_3-20260517.md)

---

*End of Phase 5 brief v2.*
