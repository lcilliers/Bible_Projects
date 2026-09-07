# M09 Phase 7 — VCG design within sub-groups — brief

**Date:** 2026-05-22
**Cluster:** M09 — Humility, Meekness and Submission
**Phase:** 7 (VCG design within sub-groups)
**Audience:** Claude AI session (chat)
**Governing instruction:** `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §10

**Read this brief first.** The structural input is the per-sub-group meanings report below.

---

## Required inputs

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M09/wa-cluster-M09-phase7-vcg-brief-v1-20260522.md` | Primary task instructions |
| 2 | **Per-sub-group meanings report** — `Sessions/Session_Clusters/M09/wa-cluster-M09-subgroup-meanings-v1-20260522.md` | Per sub-group, every is_relevant verse with its term + Phase 2 meaning, in canonical Bible order. **The only analytical material for VCG design** (inherited VCGs / anchors / findings explicitly suppressed per §2.3) |
| 3 | **Phase 5 sub-group design** — `Sessions/Session_Clusters/M09/wa-cluster-M09-subgroup-design-v1-20260521.md` | Sub-group definitions (characteristic-representations), volume-split rationale, cross-register flags |
| 4 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §10 (Phase 7 disciplines; §10.7 staged write-out; §10.8 no-sampling pre-submission checklist) |
| 5 | **Science extract** — `Workflow/Sciences/wa-m09-humility-scienceextract-v1_0-20260513.md` | Programme-curated scientific framing (humility, meekness, dignity, submission) |
| 6 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-{current}.md` Ch.1 'Defining Inner Being' | Inner-being scope definition |
| 7 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |

---

## Context

M09's sub-group structure landed at Phase 6 (applied 2026-05-22): **8 sub-groups, 109 is_relevant verses** distributed cleanly (largest M09-A at 33.9%, well under 40% gate). Each sub-group represents a characteristic per v2_8 §8.0; M09-A/B are a CHAR-1 volume-split (HUMILITY) and M09-C/D are a CHAR-2 volume-split (SUBMISSION); the others are 1:1.

| Sub-group | Characteristic | Verses | Cross-register flag |
|---|---|---:|---|
| M09-A | CHAR-1a Humility — willed self-lowering | 37 | — |
| M09-B | CHAR-1b Lowliness — experienced/imposed state | 13 | — |
| M09-C | CHAR-2a Submission — inner disposition of will | 17 | **M30** (obedience adjacent) |
| M09-D | CHAR-2b Submission — relational pattern of obedience | 30 | **M30** (obedience adjacent) · **11 PHASE_8_5_FLAG** (diatassō) |
| M09-E | CHAR-3 Contrition — crushed and broken spirit | 2 | — |
| M09-F | CHAR-4 Meekness — calibrated restraint and gentleness | 2 | — |
| M09-G | CHAR-5 Dignity — grounded moral gravity | 3 | **M08** (structural opposite) |
| M09-H | CHAR-6 Willing-heartedness — the freely-moved spirit | 5 | **M04, M29** (joy + volition) |
| **Total** | | **109** | |

Phase 7's task is to design **VCGs (verse_context_groups)** within each sub-group — finer-grained units that cluster verses with substantively similar inner-being content inside the sub-group's register.

**Important: 11 PHASE_8_5_FLAG verses in M09-D** (all G1299 diatassō except Luk 17:10 which is in M09-C). These verses have no M09 inner-being content per Pass A; they're provisionally placed for Phase 5/6 structural integrity. Group them into a **single dedicated VCG** within M09-D (e.g. `M09-D-VCG-08` titled "PHASE_8_5_FLAG: diatassō non-M09 verses pending resolution") to keep the substantive VCGs clean.

**Phase 5.5 candidate: Luk 3:5 G5013 tapeinoō** in M09-A — single-verse outlier (mountains-made-low). Group with other tapeinoō self-lowering verses in M09-A's first VCG; the Phase 5.5 set-aside (if applied) is a separate operation.

---

## Your task — per sub-group, design VCGs

For each sub-group (in code order: M09-A → M09-B → M09-C → M09-D → M09-E → M09-F → M09-G → M09-H), produce:

1. **VCG definitions** — provisional `group_code`, `context_description`, member verse list, one anchor verse.
2. **Per-sub-group design document** written to disk **immediately** after designing that sub-group (mandatory per §10.7 staged write-out — clears working context before moving on).
3. **Per-sub-group sum verification** — total member vc_ids across the sub-group's VCGs must equal the sub-group's verse count from the meanings report.

After all sub-groups are processed, produce the **unified VCG creation JSON** (one file covering all sub-groups).

---

## Process per sub-group (§10.2 + §10.7 staged write-out)

1. **Read** every verse-meaning in the sub-group's section of the meanings report. **Every row. No skipping. No sampling.**
2. **Cluster meanings into provisional VCGs.** A VCG groups verses with substantively similar inner-being content within the sub-group's characteristic. Typical sub-groups produce 1–5 VCGs (M09 sub-groups are small; some have only 2-5 verses and may need only 1 VCG).
3. **Name each VCG** with a provisional code (format: `M09-{X}-VCG-{seq}`, e.g. `M09-A-VCG-01`) and a one-paragraph `context_description`.
4. **Designate ONE anchor verse per VCG** — the verse that most directly and definitionally evidences the phenomenon the VCG names. The anchor's vc_id must be in the VCG's member list.
5. **Note dual-membership verses** — verses that legitimately belong to two VCGs (rare; usually within the same sub-group). Flag explicitly.
6. **Write the per-sub-group design document to disk immediately:**
   `Sessions/Session_Clusters/M09/wa-cluster-M09-{subgroup_code}-vcg-design-v1-20260522.md`
7. **Verify sum.** Members must equal input count.
8. Move to next sub-group; repeat.

---

## Special VCG handling

### M09-D PHASE_8_5_FLAG VCG (mandatory)

The 11 diatassō verses in M09-D with `PHASE_8_5_FLAG=true` MUST go into a **single dedicated VCG** for Phase 8.5 resolution. Suggested:

- code: `M09-D-VCG-{last_seq}`
- label/context_description: "PHASE_8_5_FLAG — G1299 diatassō non-M09 verses pending Phase 8.5 resolution. Provisionally routed here for structural integrity; Phase 8.5 will SET-ASIDE or ROUTE-TO-M23. Verses (11): Mat 11:1; Luk 3:13; Luk 17:9; Act 7:44; Act 18:2; 1Cor 7:17; 1Cor 9:14; 1Cor 11:34; 1Cor 16:1; Gal 3:19; Tit 1:5."
- anchor: any of the 11 (e.g. Mat 11:1)

This keeps the substantive M09-D VCGs (obedience-to-gospel, family obedience, etc.) clean.

### Cross-register flag preservation

- **M09-C and M09-D (M30 flag)** — context_descriptions should note "submission of will to authority — register-adjacent with M30 (Obedience)".
- **M09-G (M08 flag)** — context_description should note "dignity as inner-grounded worth; structural opposite of M08 (Pride) proud self-display".
- **M09-H (M04, M29 flags)** — context_description should note willing-hearted disposition's overlap with M04 joy/delight and M29 volition.

---

## Output structure

### Per sub-group design document

`Sessions/Session_Clusters/M09/wa-cluster-M09-{subgroup_code}-vcg-design-v1-20260522.md`

### Unified VCG creation JSON

After all sub-groups: `Sessions/Session_Clusters/M09/wa-cluster-M09-vcg-creation-v1-20260522.json`

```json
{
  "_meta": {
    "cluster": "M09",
    "phase": 7,
    "date": "2026-05-22",
    "total_subgroups": 8,
    "total_vcgs": <N>,
    "total_verses": 109
  },
  "subgroups": {
    "M09-A": {
      "vcgs": [
        {
          "provisional_code": "M09-A-VCG-01",
          "description": "...",
          "verses": [<every vc_id>],
          "anchor_vc_id": <vc_id>
        }
      ]
    }
  }
}
```

Field name **must** be `verses` (not `key_verses`, not `members` — complete arrays per §10.8).

---

## Discipline (§10.7 + §10.8)

1. **Read every verse-meaning** for each sub-group. No sampling.
2. **Stage by sub-group.** Don't try to hold all 8 sub-groups in working memory. After M09-A: write design doc, verify sum, move to M09-B. Repeat.
3. **Sum verification per sub-group.** Members must equal input count.
4. **Anchor in members.** Every `anchor_vc_id` must be in its VCG's `verses` array.
5. **No phantom vc_ids.** Every vc_id used must be in the meanings report.
6. **No vc_id in two VCGs** unless explicitly dual-membership flagged.
7. **PHASE_8_5_FLAG VCG isolation** — keep the 11 diatassō verses in a single dedicated VCG within M09-D; do NOT mix them with substantive M09-D verses.
8. **Preserve cross-register flags** in M09-C, M09-D, M09-G, M09-H VCG descriptions.

---

## Pre-submission checklist (§10.8, AI verifies before declaring complete)

- [ ] 8 design documents on disk (one per sub-group).
- [ ] Each design doc carries a sum-verification line.
- [ ] Unified JSON written with field name `verses` (complete arrays).
- [ ] Every `anchor_vc_id` is in its VCG's `verses` array.
- [ ] Union of all `verses` per sub-group equals input count (37 / 13 / 17 / 30 / 2 / 2 / 3 / 5).
- [ ] Total `verses` across cluster = 109.
- [ ] No vc_id in two VCGs (unless dual-membership flagged).
- [ ] M09-D has a dedicated PHASE_8_5_FLAG VCG holding the 11 diatassō verses; the remaining 19 M09-D verses distributed across substantive VCGs.

CC will validate every item before applying. Failures send Phase 7 back for resubmission with a delta report.

---

## After you finish

1. Confirm pre-submission checklist passes.
2. Ping CC: "M09 Phase 7 VCG design ready" with the file list.
3. CC validates against the DB (§10.9), then builds the Phase 7 directive.

---

*End of brief. Load the meanings report (#2). Process sub-groups in code order. Stage write-outs.*
