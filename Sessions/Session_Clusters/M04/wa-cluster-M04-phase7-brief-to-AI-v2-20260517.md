# M04 Phase 7 v2 brief — VCG design within sub-groups

**Audience:** Claude AI
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_3-20260517.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_3-20260517.md) §10 (Phase 7)
**Date:** 2026-05-17
**Supersedes:** [Phase 7 v1 brief (rejected — see files phase 7 rejected v1/)](files%20phase%207%20rejected%20v1/WA-M04-phase7-brief-to-AI-v1-20260517.md)

---

## ⛔ Why this is a resubmission — read this section first

The first Phase 7 attempt (v1) had four serious analytical errors. **You must not repeat any of them.**

| v1 error | Magnitude | Required v2 behaviour |
|---|---:|---|
| **1. JSON used `key_verses` (sample) instead of full `verses` per VCG** | 23 VCGs incomplete | Every VCG's `verses` array must list **every member vc_id**. Sampling is forbidden. |
| **2. 287 of 661 M04-A verses (43%) not enumerated in any VCG's member list** | 287 verses orphaned | Every is_relevant vc_id in the input report must appear in **exactly one** VCG's member list. |
| **3. 15 cross-cluster vc_ids included** (M42 rin.nah / ra.nan — owned by R208 shouting, not M04) | 15 phantoms | Use **only the vc_ids that appear in the meanings report**. No external references. |
| **4. 7 non-existent vc_ids invented** (hallucinated numbers) | 7 phantoms | Every vc_id you write must come from the meanings report. Don't invent. |

These errors caused Phase 5 to be rejected and rolled back. v2 starts from a properly-decomposed 10-sub-group structure (33.5% biggest, passes §8.6 gate). v2's Phase 7 must complete cleanly.

---

## 🔴 The no-sampling / read-every-verse rule (absolute)

**Every single is_relevant verse in every sub-group must be read and assigned to exactly one VCG.** No exceptions. No samples. No "representative members." No "et cetera." No "the rest go here implicitly."

- Open the meanings report. Find the sub-group section. Count the verses listed (e.g. M04-B has 273 rows).
- Design your VCGs against those meanings.
- For each VCG, list every member `vc_id` explicitly in `key_verses` array AND in the JSON `verses` array.
- Before finalising each sub-group's output: **sum the member counts across that sub-group's VCGs.** The total **MUST EQUAL** the verse count in the input report. If your sum is short, you have skipped verses. Add them — don't release the design.

You will report this verification at the end of every sub-group section:

```
VCG total verses: 273 (matches M04-B input count of 273 — verified)
```

If your sum doesn't match, write what's missing and fix it. Don't move on.

---

## State of M04 at Phase 7 v2 open

| Item | Count |
|---|---|
| Active terms in M04 | 58 |
| Active sub-groups | **11** (10 substantive + M04-BOUNDARY) |
| `mti_term_subgroup` links | 75 (43 primary + 17 secondary + 15 boundary) |
| is_relevant verses routed to sub-groups | **1138** |
| Inherited VCGs (suppressed) | 86 |
| `cluster.status` | `Analysis - In Progress` |
| §8.6 distribution validation | **PASS** (biggest substantive 33.5%, ratio 1.9×) |

Phases 1–6 v2 complete. Phase 7 v2 produces the new VCG structure for each sub-group.

---

## Required per-sub-group VCG output

Per the meanings report's exact counts:

| Sub-group | Label | Verses | Expected VCGs |
|---|---|---:|---|
| M04-A | Exultation in YHWH (Vertical) | 84 | 2–3 VCGs |
| **M04-B** | **Communal and Festive Rejoicing** | **273** | **5–7 VCGs** — biggest substantive; needs granular splits within communal joy register |
| M04-C | NT Joy in Christ and the Spirit | 143 | 4–5 VCGs |
| M04-D | Shared Communal Rejoicing (sunchairo) | 10 | 1 VCG |
| M04-E | Promised and Eschatological Joy | 35 | 2 VCGs |
| M04-F | Cheerfulness Under Adversity | 4 | 1 VCG |
| M04-G | Delight in God's Word, Law, Wisdom | 26 | 1–2 VCGs |
| M04-H | Volitional Delight (cha.phets / will-pleasure) | 136 | 4–5 VCGs |
| M04-I | Wonder at God's Marvellous Works | 77 | 2–3 VCGs |
| M04-J | Pleasantness and Relational Delight | 28 | 1–2 VCGs |
| M04-BOUNDARY | Boundary Terms | 322 | **1 aggregating VCG** (structural only — see §"M04-BOUNDARY") |
| **TOTAL** | | **1138** | **~24–32 VCGs** |

**These counts are the AUTHORITATIVE per-sub-group totals.** Your VCG member sums must match them exactly.

---

## Inputs

### Primary input — read every line

[Sessions/Session_Clusters/M04/wa-cluster-M04-subgroup-meanings-v2-20260517.md](wa-cluster-M04-subgroup-meanings-v2-20260517.md) — per-sub-group, every is_relevant vc with reference, term, and Phase 2 meaning. Canonical Bible order within each sub-group. **This is the only verse-level analytical material you use for Phase 7.**

There are 1138 vc rows. Read every one before assigning. The meanings report includes 19 verses (in M04-A, B, C, D, J) flagged `_(missing — re-run Phase 2)_` because they are XREF copies. Treat them as siblings of their OWNER copies (same term + reference + sub-group); assign them to the appropriate VCG by inference from the OWNER text.

### Phase 5 v2 design (sub-group rationale)

[Sessions/Session_Clusters/M04/files phase 5/WA-M04-subgroup-design-v2-20260517.md](files%20phase%205/WA-M04-subgroup-design-v2-20260517.md) — the 10 sub-group descriptions you should design VCGs against.

### Phase 6 v2 applied report

[WA-M04-dir-003-subgroup-routing-applied-v2-20260517.md](WA-M04-dir-003-subgroup-routing-applied-v2-20260517.md) — DB state confirmation.

### Reference — what NOT to do

[files phase 7 rejected v1/WA-M04-vcg-creation-v1-20260517.json](files%20phase%207%20rejected%20v1/WA-M04-vcg-creation-v1-20260517.json) — the rejected v1 output. Its analytical content (VCG-level register distinctions, especially for what was v1's M04-A) is useful for v2's M04-A, B, C, H VCG design. **But its structure (key_verses sampling, phantom vc_ids, cross-cluster misinclusions) is what we are explicitly avoiding.**

### Governing instruction

[wa-sessionb-cluster-instruction-v2_3-20260517.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_3-20260517.md) — §10 in particular.

---

## Suppressed by design

Inherited VCGs (86 in DB) are NOT in your input. Per v2_3 §2.3, you design new VCGs purely from the meaning corpus.

---

## Decisions already made — do NOT re-debate

1. **Sub-group structure (11)** is final. The §8.6 gate verified it.
2. **Term-to-sub-group placements (75)** are final. CC reconciled 1 intra-design dedup (mti=790 in M04-G).
3. **The 58 terms are M04's term set.** 5 terms transferred at Phase 4. Don't add back.
4. **BOUNDARY (15 terms)** — single aggregating VCG only.

---

## Special handling

### M04-B is the biggest substantive sub-group (273 verses)

This is the communal/festive joy register. Within it, you should see distinct VCGs around:

- **Festival worship joy** — Lev 23, Deu 12/14/16, Neh 8/12, 2Ch 30 — gladness at appointed feasts
- **Sanctuary / temple dedication joy** — 1Ch 15/29, 2Ch 7, Neh 12:43, Ezr 6:22
- **Coronation / national joy** — 1Sa 11:15, 1Ki 1:40, 2Ch 23:18
- **Family / wedding / harvest joy** — Gen 31:27, Deu 24:5, Jdg 16:23, Rut 3:7
- **Civic / city joy** — Pro 11:10, Est 8:15–17, communal rejoicing at public events
- **Prophetic call to corporate gladness** — Joe 2:21, Zec 9:9, Zep 3:14

Read all 273 verses; let the meaning corpus dictate the exact VCG splits. 5–7 VCGs likely.

### M04-H is the volitional delight register (136 verses)

cha.phets-as-will / cha.phets-as-delight. Within it, expect:

- **God's will / divine pleasure** — God doing what pleases him (Psa 115:3; 135:6; Isa 46:10; 53:10; 55:11; Eze 18:23, 32; 33:11)
- **Human consenting delight / volitional choice** — willing acceptance (Deu 21:14; 25:7; Rut 3:13; 1Sa 18:25; Est 6:6–11)
- **Object of delight as inner orientation** — Pro, Psa, Job texts about what one takes pleasure in
- **Negative volitional pleasure** — what God does NOT delight in (Psa 51:16; Hos 6:6; Pro 21:1)

4–5 VCGs likely.

### M04-C NT joy register (143 verses)

Distinct strands visible:
- **Synoptic joy** — Mat 13:44; Luk 1:14, 44; 2:10; 15:7, 10; 24:41, 52
- **Johannine joy** — Joh 3:29; 15:11; 16:20–24; 17:13
- **Pauline joy in Christ** — Rom 14:17; 15:13; Phil 1:4, 18, 25; 3:1; 4:4; 1Th 2:19; 1Cor 13:6
- **Joy as Spirit's fruit / Spirit-given** — Gal 5:22; 1Th 1:6; Rom 14:17
- **Joy under suffering** — chairō / agalliao paradoxical (1Pe 1:6, 8; 4:13; Jas 1:2; Mat 5:12; Rom 5:3)

4–5 VCGs likely.

### M04-I Wonder (77 verses)

pa.la verb + pe.le + miph.la.ah. Distinct registers:
- **Wonder as God's marvellous works (object)** — Psa 9:1; 26:7; 71:17; 75:1; 96:3; 105:2, 5; 106:22; Job 5:9; 9:10
- **Wonder as "too hard / extraordinary" (qualitative)** — Gen 18:14; Deu 17:8; Jer 32:17, 27; Job 42:3
- **Wonder as human inner marvelling response** — Psa 139:14; Job 9:10; Mic 7:15

2–3 VCGs.

### M04-BOUNDARY — structural only, 1 aggregating VCG

322 verses across 15 terms; H2896A tov is 230 of those. Single aggregating VCG (`M04-BOUNDARY-VCG-01`) covers all 322 vc_ids of all 15 BOUNDARY terms. Anchor: choose the most analytically clear inner-being vc from the BOUNDARY corpus (e.g. Psa 16:11 na.im / Gen 8:21 ni.cho.ach / Pro 15:15 tov "cheerful heart"). No characteristic-bearing analysis at Phase 7.

### Programme scope reminder — divine joy in scope

God's joy/delight/pleasure in his people (Zep 3:17; Isa 62:5; Mat 3:17; Eph 1:5; Pro 11:20) is **in scope** as characteristic-in-operation. Don't set aside. Narrow set-aside criterion only for verses describing God's joy as an independent divine inner life event (analogous to M01 Deu 32:27, Job 25:2).

### Missing meanings (19 XREF copies)

19 vc rows have analysis_note empty — all XREF copies (vr.delete_flagged=1). Per sub-group:

| Sub-group | XREF gaps |
|---|---:|
| M04-A | 1 |
| M04-C | 14 |
| M04-D | 2 |
| M04-J | 2 |

Each XREF row is a sibling of an OWNER row (same term + reference, different mti placement). Assign each XREF to the same VCG as its OWNER sibling. The meanings report flags them with `_(missing — re-run Phase 2)_`. Do not skip them — include them in member lists.

---

## Output expected from you

### 1. One design document per sub-group — 11 total files

For each of the 11 sub-groups (M04-A through M04-J + M04-BOUNDARY):

`Sessions/Session_Clusters/M04/WA-M04-{subgroup_code}-vcg-design-v2-20260517.md`

(11 separate files; do NOT combine into a single document.)

Per VCG within each document:

- Provisional `group_code` (e.g. `M04-B-VCG-01`)
- `context_description` (one paragraph written from the meanings)
- **Member verses (complete list)** — every vc_id in canonical order, with reference + term
- Anchor verse — single vc_id (must be a member of this VCG) with rationale
- Dual-membership flags — verses whose meaning genuinely fits two VCGs (cite which)

At the end of each sub-group document:

```
**Verification**: VCG member sums = N1 + N2 + ... = TOTAL, which matches M04-{X} input count of TOTAL ✓
```

If the verification doesn't match, fix it before moving on.

### 2. Unified VCG creation JSON — complete member arrays

`Sessions/Session_Clusters/M04/WA-M04-vcg-creation-v2-20260517.json`

```json
{
  "cluster_code": "M04",
  "phase": 7,
  "version": "v2",
  "M04-A": {
    "vcgs": [
      {
        "provisional_code": "M04-A-VCG-01",
        "description": "...",
        "verses": [vc1, vc2, vc3, ...],         // COMPLETE list, every member
        "anchor_vc_id": vc_anchor                // must be in `verses`
      },
      ...
    ]
  },
  "M04-B": { "vcgs": [ ... ] },
  ...
  "M04-BOUNDARY": {
    "vcgs": [
      {
        "provisional_code": "M04-BOUNDARY-VCG-01",
        "description": "Aggregating VCG holding all 322 verses of the 15 BOUNDARY terms. Researcher disposition at Phase 12.",
        "verses": [...all 322...],
        "anchor_vc_id": ...
      }
    ]
  }
}
```

**Critical requirements for the JSON:**

- `verses` must be a complete array, not `key_verses` sample. Use the field name `verses`.
- Every `anchor_vc_id` must be present in its VCG's `verses` array.
- Union of all `verses` across all VCGs in a sub-group = the sub-group's full member set (1138 total across all sub-groups).
- No vc_id appears in two different VCGs unless explicitly flagged as dual-membership in the design document. Default: each verse in exactly one VCG.

### 3. Cross-routing flags (if any)

`Sessions/Session_Clusters/M04/WA-M04-phase7-cross-routing-flags-v2-20260517.md` — verses whose meaning suggests a different sub-group than the Phase 6 routing; or divine-inner-state set-aside candidates.

### ⚠️ STAGED WRITE-OUT

1. Process M04-A → write `WA-M04-M04-A-vcg-design-v2-20260517.md` → **disk immediately + verify sum**.
2. Process M04-B → write → **disk + verify sum**.
3. Continue through M04-J and M04-BOUNDARY (11 files total). Each to disk immediately with sum verification.
4. After all 11 design docs are saved, derive the unified JSON and write to disk.
5. Cross-routing flags (if any) → write at the end.

Do NOT combine sub-groups into a single design document (the v1 attempt did this and the combined doc was harder to verify; resulting JSON was incomplete).

---

## Pre-submission checklist

Before declaring Phase 7 v2 complete, verify each:

- [ ] 11 design documents written (one per sub-group, no combinations)
- [ ] Each design document has a verification line: `VCG member sums = ... matches input count ✓`
- [ ] Unified JSON file written with field name `verses` (not `key_verses`)
- [ ] Every `anchor_vc_id` is in its VCG's `verses` array
- [ ] Sum of all VCG `verses` across the sub-group = sub-group's input count (1138 total)
- [ ] No vc_id appears in two different VCGs (except explicit dual-memberships)
- [ ] Every vc_id is from the meanings report — none invented, none from other clusters
- [ ] M04-BOUNDARY-VCG-01 has all 322 BOUNDARY verses

CC will validate all of these mechanically. If any fails, Phase 7 will be rejected and re-submitted.

---

## Discipline reminders

1. **No sampling.** Every is_relevant vc must appear in exactly one VCG. The meanings report is authoritative.
2. **No imagination.** Every vc_id must come from the meanings report. Don't invent numbers.
3. **No cross-cluster.** The meanings report contains only M04 vc_ids. Don't reach for vc_ids from other clusters even if their content is semantically adjacent.
4. **No combining sub-group documents.** 11 sub-groups = 11 design files.
5. **No incomplete `verses` arrays.** Every VCG's `verses` array is the COMPLETE member set, not a sample.
6. **Anchors must be members.** The anchor_vc_id must appear in the same VCG's `verses` array.
7. **Output to new files, not in-place edits.**

---

## When you're done

CC will:

1. Cross-validate every vc_id in your design against the meanings report (cluster scope, existence, no duplicates across VCGs).
2. Verify per-sub-group sums match the input counts.
3. Build the Phase 7 apply patch and apply (INSERT verse_context_group rows, INSERT vcg_term links, UPDATE verse_context.group_id, UPDATE verse_context.is_anchor=1 per VCG anchor).
4. Generate Phase 8 input (CC dissolves old VCGs; no AI involvement).
5. Phase 9 onwards: catalogue prompts, inherited findings reconciliation, cluster_finding load, closure.

---

## Provenance

- Per-sub-group meanings report (primary input): [wa-cluster-M04-subgroup-meanings-v2-20260517.md](wa-cluster-M04-subgroup-meanings-v2-20260517.md)
- Phase 6 v2 applied: [WA-M04-dir-003-subgroup-routing-applied-v2-20260517.md](WA-M04-dir-003-subgroup-routing-applied-v2-20260517.md)
- Phase 5 v2 design: [files phase 5/WA-M04-subgroup-design-v2-20260517.md](files%20phase%205/WA-M04-subgroup-design-v2-20260517.md)
- §8.6 validation: [WA-M04-phase5-distribution-validation-v2-20260517.md](WA-M04-phase5-distribution-validation-v2-20260517.md)
- v1 rejection report (what NOT to repeat): [WA-M04-phase7-validation-v1-20260517.md](WA-M04-phase7-validation-v1-20260517.md)
- v1 rejected outputs preserved: [files phase 7 rejected v1/](files%20phase%207%20rejected%20v1/)
- Governing instruction: [wa-sessionb-cluster-instruction-v2_3-20260517.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_3-20260517.md)

---

*End of Phase 7 v2 brief.*
