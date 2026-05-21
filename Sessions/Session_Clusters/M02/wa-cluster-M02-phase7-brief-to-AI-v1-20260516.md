# M02 Phase 7 brief — VCG design within sub-groups

**Audience:** Claude AI
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) §10 (Phase 7)
**Date:** 2026-05-16

---

## State of M02 at Phase 7 open

| Item | Count / value |
|---|---|
| Active terms in M02 | 43 |
| Active sub-groups | **7** (M02-A · M02-B · M02-C · M02-D · M02-E · M02-F · M02-BOUNDARY) |
| `mti_term_subgroup` links | 52 (43 primary + 9 secondary) |
| is_relevant verses routed to sub-groups | **641** |
| Inherited VCGs in DB | 73 — **NOT visible to you** (suppressed per v2_2 §2.3); Phase 8 will dissolve them after your work lands |
| Existing new VCGs | 0 — this phase creates them |
| `cluster.status` | `Analysis - In Progress` |

Phases 1–6 complete. Phase 7 produces the new VCG structure for each sub-group.

---

## Your task per v2_2 §10.2

Per sub-group, read the verse-meaning list. Cluster meanings into provisional VCGs — groups of verses with substantively similar inner-being content within this sub-group's register. Each VCG names a distinct inner-being phenomenon within the sub-group's characteristic.

For each VCG you design:

- `group_code` (suggested format: `{subgroup_code}-VCG-{seq}` — CC will assign final ids on apply)
- `context_description` written from the meanings (one paragraph)
- Member verses (by `vc_id`)
- **Anchor verse** — the one verse that most directly and definitionally evidences the phenomenon
- Dual-membership notes — verses that legitimately belong to two VCGs

---

## Inputs

### Primary input

[Sessions/Session_Clusters/M02/wa-cluster-M02-subgroup-meanings-v1-20260516.md](wa-cluster-M02-subgroup-meanings-v1-20260516.md) — per-sub-group, every is_relevant verse with reference, term, and Phase 2 meaning. Canonical Bible order within each sub-group. **This is the only analytical material you need for Phase 7.**

### Reference (do not re-debate, but useful to know what's been decided)

- [WA-M02-dir-002-subgroup-routing-applied-v1-20260516.md](WA-M02-dir-002-subgroup-routing-applied-v1-20260516.md) — Phase 6 applied report.

### Suppressed by design

Inherited VCGs (73 in DB) are NOT in your input. Per v2_2 §2.3 (structural enforcement of the inherited-structure contamination guard), you design new VCGs purely from the meaning corpus. CC dissolves the old VCGs in Phase 8 with a researcher comparison report.

---

## Decisions already made — do NOT re-debate

1. **Sub-group structure** (7 sub-groups) is final. Don't propose renaming, merging, or splitting sub-groups at Phase 7. If you find a verse whose meaning fits a different sub-group than where it's currently routed, that's a Phase 7 cross-routing observation — note it; don't change sub-group structure.
2. **Term-to-sub-group placements** (52 links: 43 primary + 9 secondary) are final. Don't re-debate which term belongs in which sub-group.
3. **The 43 terms are M02's term set.** 4 terms were transferred out at Phase 4 (eritheia→M28, zid→M08, ma.rar→M03, tsa.rah→M24). Don't propose adding terms back.
4. **BOUNDARY** terms (6) have their `M02-BOUNDARY` sub-group placement set. They typically get a single aggregating VCG, or per-term VCGs if their corpora warrant — your judgment.

---

## Sub-group sizes — VCG-count expectations

These are guidelines, not constraints. Your judgment from the meaning corpus governs.

| Sub-group | Verses | Likely VCG count |
|---|---:|---|
| M02-A Divine Wrath as Judicial Force | 109 | 4–6 VCGs (wrath as oath, wrath as eschatological judgment, divine vs human wrath, wrath as covenantal force, etc.) |
| M02-B Burning Rage and Inner Heat | 263 | 6–8 VCGs (largest sub-group — will need fine distinctions: divine vs human heat, inner state vs enacted, prophetic indictment vs Mosaic anger, jealousy-as-heat, etc.) |
| M02-C Indignation and Moral Displeasure | 36 | 2–3 VCGs |
| M02-D Provocation — Anger Aroused | 58 | 3–4 VCGs (provocation TO anger vs being provoked; intentional vs accidental) |
| M02-E Jealousy, Zeal and Possessive Passion | 77 | 3–4 VCGs (divine jealousy/zeal for God's people, human possessive jealousy, jealousy as competitive envy) |
| M02-F Strife, Quarrel and Contentious Anger | 16 | 1–2 VCGs |
| M02-BOUNDARY | 82 | **1 aggregating VCG** (placeholder; researcher disposition at Phase 12) |
| **Estimated total** | | **~20–28 new VCGs** |

---

## Special handling for M02

### 1. Programme scope reminder — human inner being

The programme's scope is **human inner being**. Anger, however, is heavily attributed to God in Scripture. Most divine-wrath verses describe **the characteristic in operation** (wrath as enacted force, judicial action, covenantal consequence) — these belong in the cluster and form their own VCGs.

The set-aside criterion (per M01 Phase 7 precedent) is narrower: verses that describe **God's internal emotional experience as a divine inner life event** — analogous to M01's Deu 32:27 (God's apprehension), Eze 16:43 (God's fury aroused), Job 25:2 (dread as attribute of God's dominion). Watch for verses where the verse content focuses on God *inwardly experiencing* anger as a passion/inner state rather than enacting it. Flag these as set-aside candidates — CC will apply.

Hint: very few of M02's verses meet this strict criterion. Most "God's wrath" verses are about wrath enacted or revealed, which is **in scope**. Don't over-apply.

### 2. M02-E Jealousy — design VCGs that respect the divine-zeal vs human-envy distinction

Phase 5 kept the qa.na / qin.ah / qan.na / qan.no family unified in one sub-group, but the corpus contains:

- **Divine zeal / protective jealousy** — God's jealousy *for* his people, *for* his name (Exo 20:5; Num 25:11; Deu 32:21; Eze 5:13; 23:25; 38:19; Joe 2:18; Zec 1:14; 8:2).
- **Human zeal-as-anger** — Phinehas zealous with God's zeal (Num 25:11); David zealous for God's house (Psa 69:9); Paul a Pharisee zealous (Phil 3:6; Act 22:3).
- **Human possessive jealousy / envy** — jealousy fiercer than wrath (Pro 27:4); jealousy as work-driver (Eccl 4:4); jealousy of brothers (Gen 26:14, 37:11).

At least 2–3 VCGs within M02-E to capture these registers cleanly.

### 3. M02-B Burning Rage and Inner Heat — large sub-group, will need granular VCGs

263 verses across 10 primary terms. The fire/heat metaphor unifies the sub-group, but within it there are distinct registers:

- Divine burning anger (wrath of YHWH burning against Israel; God's nose burning, etc.)
- Human-against-human burning anger (Moses' anger kindled; brothers' anger)
- Burning anger as motivator of action (Phinehas-style)
- Inner-state heat without enacted consequence (anger contained, restrained)
- Wrath as enduring divine attribute vs eruptive divine response

Design VCGs that capture these distinctions — likely 6–8 VCGs for this sub-group alone.

### 4. M02-BOUNDARY — single placeholder VCG

Per M01 precedent, BOUNDARY gets one aggregating VCG (e.g. `M02-BOUNDARY-VCG-01`) with a brief context description naming the analytical question. The 82 verses route to it. The 6 BOUNDARY terms (antilogia, erethizō, zestos, ka.a.s, riv, tsur) await researcher disposition at Phase 12.

Anchor verse for BOUNDARY-VCG-01: pick the verse with the most analytically clear content (likely from riv corpus given its larger size, or whichever term has the most concrete inner-being meaning).

### 5. Multi-faceted (secondary) terms — 9 placements

9 terms have secondary placements in additional sub-groups (set at Phase 6 per AI's design):

These secondary placements are at the **term** level only. A verse's primary VCG comes from its **term's primary sub-group**. If a verse's meaning straddles two VCGs (within or across sub-groups), record it as **dual-membership** at the verse level in your Phase 7 design — CC applies primary-VCG routing + records secondary VCGs in `verse_context.notes`.

### 6. Anchor designation — one per VCG

Each VCG gets exactly one AI-designated anchor verse (the most directly definitional verse). After your design, CC may add **provisional anchors per term** (R4 rule — every term with is_relevant verses must have ≥1 anchor; if your designated VCG anchors don't cover all of a VCG's terms, CC fills the gap with provisional anchors).

### 7. Cross-routing flags

If during the VCG design you notice a verse whose meaning fits better in a different sub-group than where Phase 6 routed it, flag it in a cross-routing document — CC may apply small corrections alongside the Phase 7 directive. Don't change sub-group structure at Phase 7; just note the observation.

---

## Output expected from you

### 1. VCG design document per sub-group

For each substantive sub-group (M02-A through M02-F), one document:

`Sessions/Session_Clusters/M02/WA-M02-{subgroup_code}-vcg-design-v1-20260516.md`

Per VCG, list:

- Provisional `group_code` (e.g. `M02-A-VCG-01`)
- `context_description` (one paragraph)
- Member verses (vc_id + reference + term)
- Anchor verse (single vc_id with rationale)
- Dual-membership flags (verses also belonging to a second VCG)

For M02-BOUNDARY: a single section with the 6 BOUNDARY terms and a note that no full VCG design is warranted (one aggregating VCG covers all 82 verses).

### 2. VCG creation JSON

`Sessions/Session_Clusters/M02/WA-M02-vcg-creation-v1-20260516.json` — machine-readable form of the design, for CC to apply:

```json
{
  "M02-A": {
    "vcgs": [
      {
        "provisional_code": "M02-A-VCG-01",
        "description": "...",
        "verses": [12345, 12346, ...],
        "anchor_vc_id": 12345
      },
      ...
    ]
  },
  "M02-B": { "vcgs": [ ... ] },
  ...
  "M02-BOUNDARY": {
    "vcgs": [
      {
        "provisional_code": "M02-BOUNDARY-VCG-01",
        "description": "Aggregating VCG for BOUNDARY terms — pending researcher disposition at Phase 12. Members: antilogia, erethizō, zestos, ka.a.s, riv, tsur.",
        "verses": [...],
        "anchor_vc_id": ...
      }
    ]
  }
}
```

### 3. Cross-routing flags (if any surfaced)

`Sessions/Session_Clusters/M02/WA-M02-phase7-cross-routing-flags-v1-20260516.md` — list of verses whose meaning suggests a different sub-group than current placement, plus any divine-inner-state set-aside candidates per §1 above.

### ⚠️ STAGED WRITE-OUT — mandatory

Same discipline as previous AI phases:

1. Process M02-A → write `WA-M02-M02-A-vcg-design-v1-20260516.md` to disk **immediately**.
2. Process M02-B → write to disk **immediately**.
3. Continue per sub-group; each design document goes to disk as soon as it's complete.
4. After all 7 design docs are saved, derive the unified `WA-M02-vcg-creation-v1-20260516.json` and write to disk.
5. Cross-routing flags (if any) → write at the end.

Do NOT accumulate all 7 sub-group designs + JSON + flags in working context.

---

## Discipline reminders

1. **No inherited VCG visible in your input.** Suppressed structurally per v2_2 §2.3. Each new VCG you design is grounded in the meaning corpus alone.

2. **Anchor verse must be the most directly definitional.** Not the most popular reference; the one whose meaning best names what the VCG describes.

3. **Anchor R4 rule:** every term with is_relevant verses must have ≥1 anchor. CC enforces this; you focus on the VCG-level designation.

4. **Per v2_2 §10.4: NO Pass C reconciliation.** Do not compare new VCGs against inherited VCGs. The inherited VCGs are not in your input precisely because you should not reconcile.

5. **Don't conflate VCGs across sub-groups.** Each VCG belongs to one sub-group. If two sub-groups have similar inner-being content (e.g. burning anger in M02-B and burning wrath in M02-A), that's interesting — but they remain distinct VCGs in distinct sub-groups.

6. **Anchor citation discipline** — when writing an anchor verse rationale, cite the verse reference (e.g. `Exo 32:19`) and brief content. No backwards-referencing to inherited VCGs.

7. **Output to new files, not in-place edits.** Produce v1 documents per the filenames above.

---

## When you're done

CC will:

1. Validate your per-sub-group designs against the verse list (every is_relevant vc routed to exactly one new VCG; every VCG has an anchor).
2. Build a unified VCG creation patch.
3. Apply the Phase 7 directive: INSERT verse_context_group rows, INSERT vcg_term links, UPDATE verse_context.group_id, UPDATE verse_context.is_anchor=1 per anchor designation.
4. Apply cross-routing corrections + divine-inner-state set-asides alongside.
5. Generate Phase 8 input — VCG dissolution comparison report (CC handles old VCG soft-delete; no AI involvement).
6. Phase 9 onwards: catalogue prompts, inherited findings reconciliation, cluster_finding load, closure.

---

## Provenance

- Per-sub-group meanings report (primary input): [wa-cluster-M02-subgroup-meanings-v1-20260516.md](wa-cluster-M02-subgroup-meanings-v1-20260516.md)
- Phase 6 applied: [WA-M02-dir-002-subgroup-routing-applied-v1-20260516.md](WA-M02-dir-002-subgroup-routing-applied-v1-20260516.md)
- Phase 5 AI sub-group design: [WA-M02-subgroup-design-v1-20260516.md](WA-M02-subgroup-design-v1-20260516.md)
- Phase 4 applied (term transfers): [WA-M02-dir-001-term-transfer-applied-v1-20260516.md](WA-M02-dir-001-term-transfer-applied-v1-20260516.md)
- Governing instruction: [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md)

---

*End of Phase 7 brief.*
