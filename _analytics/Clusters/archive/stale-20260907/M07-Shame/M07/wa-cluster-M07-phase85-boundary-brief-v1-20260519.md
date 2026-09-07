# M07 Phase 8.5 — BOUNDARY resolution — brief

**Date:** 2026-05-19
**Cluster:** M07 — Shame, Disgrace and Humiliation
**Phase:** 8.5 (BOUNDARY resolution pass)
**Audience:** Claude AI session (chat)
**Governing instruction:** `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §11A + §18.2

**Read this brief first.** Structural inputs referenced below.

---

## Required inputs

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M07/WA-M07-phase85-boundary-brief-v1-20260519.md` | Primary task instructions |
| 2 | **BOUNDARY content report** — `Sessions/Session_Clusters/M07/WA-M07-boundary-resolution-input-v1-20260519.md` | Per BOUNDARY term, every verse with Pass A meaning + current routing |
| 3 | **Co-occurrence list** — `Sessions/Session_Clusters/M07/WA-M07-boundary-cooccurrence-list-v1-20260519.md` | Informational: other-cluster terms at the same `wa_verse_records.id` |
| 4 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §11A (Phase 8.5 disciplines) + §18.2 (verse-level disposition vocabulary) |
| 5 | **Phase 3 verdict document** — `Sessions/Session_Clusters/M07/WA-M07-constitution-debate-v2-20260519.md` | Original BOUNDARY rationales (the analytical questions to resolve) |
| 6 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-{current}.md` Ch.1 'Defining Inner Being' | Inner-being scope definition |
| 7 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |

---

## Context

M07's 5 BOUNDARY terms (per Phase 3 v2) carry **27 is_relevant verses** that need per-verse dispositions before Phase 9 catalogue findings author. **BOUNDARY-pending is not a valid pre-Phase-9 state** (§11A purpose).

| Strong's | Translit | Gloss | Verses | Phase 3 question |
|---|---|---|---:|---|
| G2699 | katatomē | mutilation | 1 (Php 3:2) | Cluster-membership undecided — single verse, minimal inner-being content |
| H4893A | mish.chat | mutilation | 1 (Isa 52:14) | Outward physical disfigurement; no inner shame content named |
| H5206 | ni.dah | filth | 1 (Lam 1:8) | M07/M12 boundary — filth produces shame outcome |
| H8213 | sha.phel | to abase | 24 | **M07/M09 split — enforced humiliation of pride (M07) vs voluntary lowliness of spirit (M09); the most analytically significant BOUNDARY in this batch** |
| H8400 | te.val.lul | defect | 0 is_relevant (1 set_aside) | Data gap — no Pass A meanings; **assess for term-level disposition, not per-verse** |

---

## Your task — per-verse disposition

For each of the 27 is_relevant BOUNDARY verses (and one term-level decision for H8400 te.val.lul), assign exactly one of three dispositions per §18.2:

| Disposition | Meaning | DB effect |
|---|---|---|
| **SET-ASIDE** | The verse does NOT evidence inner-being content for this term in M07's register (or any other cluster's). Mark out of analytical scope. | `verse_context.is_relevant=0`, `set_aside_reason='<reason> — outside M07 inner-being scope'` |
| **ROUTE-TO-CLUSTER** | The verse evidences inner-being content for **another** cluster's characteristic. Name the target cluster code; the target cluster's existing `verse_context` row for the co-occurring term carries the verse for that cluster's analysis. The current M07 verse is set `is_relevant=0` with `set_aside_reason='routed to {target} via {target_term}'`. **Eligibility check:** the target cluster must already have a term at the same `wa_verse_records.id` (per the co-occurrence list). If no eligible target term exists, ROUTE-TO-CLUSTER is not available — use SET-ASIDE or PROMOTE-TO-SUBGROUP. |
| **PROMOTE-TO-SUBGROUP** | The verse DOES evidence M07's characteristic but in a register that warrants placement in a specific existing sub-group OR a new sub-group. Name the target: existing sub-group code (e.g. `M07-D`) OR a clearly-labelled new sub-group with its `core_description`. | `verse_context.cluster_subgroup_id` = target's id (existing) or new INSERT + cluster_subgroup_id update |

**Forbidden:** "PARK", "DEFER", or "RESEARCHER-DECISION-LATER" non-dispositions. Every BOUNDARY verse must receive one of the three. If you cannot decide, surface to the researcher with a **recommended** disposition; the researcher's decision is then one of the three.

---

## Specific guidance per term

### G2699 katatomē — Php 3:2 (1 verse)

Pass A meaning notes "inner-being content is minimal" — Paul's polemical attack on circumcision-as-mutilation. The verse is rhetorical about a bodily practice, not about an inner-being state. Most likely disposition: **SET-ASIDE** (the term doesn't carry inner-being shame content in this verse). If you see a relational dishonour/contempt dimension worth preserving, propose PROMOTE-TO-SUBGROUP with rationale.

### H4893A mish.chat — Isa 52:14 (1 verse)

The servant's disfigurement causing astonishment. Pass A explicitly notes outward physical state, not inner-being shame. Likely **SET-ASIDE**. If you read the disfigurement-as-public-disgrace as analytically significant in M07's register, propose PROMOTE-TO-SUBGROUP M07-D (humiliation as enforced abasement) — the visible-public-degradation dimension fits.

### H5206 ni.dah — Lam 1:8 (1 verse)

Jerusalem's filth produces "groan and hide her face in shame." Pass A names shame explicitly. The question is whether the term itself primarily names the filth (M12 purity register) or the shame outcome (M07). Likely either **ROUTE-TO-CLUSTER M12** (term's primary register is uncleanness) — but check the co-occurrence list for an M12 term at the same vr — or **PROMOTE-TO-SUBGROUP M07-B** (moral consequence and judgment — the shame falls because of moral filth).

### H8213 sha.phel — 24 verses (THE big decision)

The Phase 3 v2 rationale: corpus spans **enforced humiliation of pride (M07 register)** AND **voluntary lowliness of spirit (M09)**. Likely outcome is verse-by-verse split:

- Verses naming **God's abasement of the proud** (Isaiah's bring-low passages: 2:9, 2:11–12, 2:17, 5:15, 10:33, 13:11, 25:11, 26:5, 29:4; Psa 18:27, 75:7, 113:6, 147:6; 1Sa 2:7; 2Sa 22:28; Job 40:11) → **PROMOTE-TO-SUBGROUP M07-D** (humiliation as enforced abasement).
- Verses naming **voluntary lowliness as moral stance** (Pro 16:19 "lowly spirit with the poor"; Pro 29:23 "lowly of spirit"; possibly Pro 25:7 "better to be told 'come up here'"; Eze 17:24, 21:26 — God's reversals as lowering structure) → **ROUTE-TO-CLUSTER M09** (humility/meekness/submission). Eligibility check: M09's status is `Not started`; ROUTE-TO-CLUSTER requires an existing target term at the same verse. If M09 has no terms yet at these verses, the alternative is PROMOTE-TO-SUBGROUP within M07 (e.g., a new sub-group for voluntary-lowliness within the cluster's shame register — but this stretches the cluster's scope; SET-ASIDE may be more honest for the volitional-lowliness verses).

**The researcher's decision will calibrate this** — read each of the 24 verses and propose the disposition that best fits the verse content. Flag any verses where the split is ambiguous.

### H8400 te.val.lul — 0 is_relevant (data gap)

The term has 1 verse marked `set_aside` (Phase 1 classification) and no `is_relevant=1` verses. This is a **term-level disposition** rather than per-verse: should the term remain in M07 at all? Likely **SET-ASIDE the term entirely** (or recommend the researcher remove the mti_term from M07 — that's a different operation; flag for researcher review). No verse-level disposition needed.

---

## Output

Single document: `Sessions/Session_Clusters/M07/WA-M07-boundary-resolution-v1-20260519.md`

Structure:

```markdown
# M07 BOUNDARY resolution — verdicts

## Summary

| Term | Verses | Disposition mix |
|---|---:|---|

## Per-term verdicts

### G2699 katatomē

#### vc=X — Reference

**Disposition:** SET-ASIDE / ROUTE-TO-CLUSTER M? / PROMOTE-TO-SUBGROUP M07-?

**Rationale:** 1-2 sentences citing the Pass A meaning. For ROUTE-TO-CLUSTER, name the eligible target term. For PROMOTE-TO-SUBGROUP-NEW, name the new sub-group code + core_description.

...

### H8213 sha.phel (24 verses)

(One block per verse OR group verses with shared disposition; same verdict format)

...

### H8400 te.val.lul

**Term-level disposition:** SET-ASIDE (term as a whole) / RECOMMEND-RESEARCHER-REVIEW

(No per-verse rows since no is_relevant verses exist.)

## Counts

- SET-ASIDE: N
- ROUTE-TO-CLUSTER {target}: N
- PROMOTE-TO-SUBGROUP {target}: N
- (Total = 27 verses + 1 term-level decision)
```

Also produce a JSON template (`Sessions/Session_Clusters/M07/WA-M07-boundary-resolution-v1-20260519.json`) for CC's mechanical apply:

```json
{
  "dispositions": [
    {"vc_id": <N>, "reference": "...", "term": "G2699 katatomē",
     "disposition": "SET-ASIDE",
     "set_aside_reason": "<reason>"
    },
    {"vc_id": <N>, "reference": "...", "term": "H8213 sha.phel",
     "disposition": "PROMOTE-TO-SUBGROUP",
     "target_subgroup_code": "M07-D"
    },
    {"vc_id": <N>, "reference": "...", "term": "H8213 sha.phel",
     "disposition": "ROUTE-TO-CLUSTER",
     "target_cluster_code": "M09",
     "target_term_at_verse": "<strongs+translit if known>"
    },
    ...
  ],
  "term_level_decisions": [
    {"mti_id": 4712, "term": "H8400 te.val.lul",
     "decision": "SET-ASIDE-TERM",
     "rationale": "..."
    }
  ]
}
```

---

## Discipline (§11A + §6.3.1 forbidden grounds — applies here too)

1. **Read every verse's Pass A meaning** before assigning a disposition. No shortcuts.
2. **Verse-level decisions.** Even within the same term, different verses may warrant different dispositions (especially H8213 sha.phel — that's the analytical point).
3. **ROUTE-TO-CLUSTER eligibility check** — only valid when a target-cluster term exists at the same `wa_verse_records.id` (per the co-occurrence list). The §18.2 rule.
4. **No disallowed BOUNDARY-style grounds** — SET-ASIDE may not be assigned solely because the meaning is horizontal-human, sensory-material, or morally-negative (§6.3.1).
5. **Surface ambiguous cases** as RECOMMEND-RESEARCHER-REVIEW with a recommended disposition; the researcher will decide on one of the three valid outcomes.

---

## After you finish

1. Save the verdict document + JSON to the paths above.
2. Ping CC: "M07 Phase 8.5 BOUNDARY dispositions ready".
3. CC validates ROUTE-TO-CLUSTER eligibility, builds the Phase 8.5 directive (`wa-cluster-M07-dir-005-boundary-resolution-v1-{date}.md`).
4. Researcher reviews + approves; CC applies.

---

*End of brief. Load the content report (#2) and the co-occurrence list (#3). Begin with G2699 (1 verse), then H4893A and H5206 (1 each), then H8213 (24 verses, the main work), then the H8400 term-level decision.*
