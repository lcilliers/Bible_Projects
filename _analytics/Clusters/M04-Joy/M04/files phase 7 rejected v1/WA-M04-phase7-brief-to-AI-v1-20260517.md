# M04 Phase 7 brief — VCG design within sub-groups

**Audience:** Claude AI
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) §10 (Phase 7)
**Date:** 2026-05-17

---

## State of M04 at Phase 7 open

| Item | Count / value |
|---|---|
| Active terms in M04 | 58 |
| Active sub-groups | **7** (M04-A · B · C · D · E · F · M04-BOUNDARY) |
| `mti_term_subgroup` links | 86 (43 primary + 28 secondary + 15 boundary) |
| is_relevant verses routed to sub-groups | **1138** |
| Inherited VCGs in DB | 86 — **NOT visible to you** (suppressed per v2_2 §2.3); Phase 8 will dissolve them after your work lands |
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

[Sessions/Session_Clusters/M04/wa-cluster-M04-subgroup-meanings-v1-20260517.md](wa-cluster-M04-subgroup-meanings-v1-20260517.md) — per-sub-group, every is_relevant verse with reference, term, and Phase 2 meaning. Canonical Bible order within each sub-group. **This is the only verse-level analytical material you use for Phase 7.**

### Reference (do not re-debate)

- [WA-M04-dir-002-subgroup-routing-applied-v1-20260517.md](WA-M04-dir-002-subgroup-routing-applied-v1-20260517.md) — Phase 6 applied report.
- [files phase 5/WA-M04-subgroup-design-v1-20260517.md](files%20phase%205/WA-M04-subgroup-design-v1-20260517.md) — Phase 5 AI design (sub-group descriptions).

### Suppressed by design

Inherited VCGs (86 in DB) are NOT in your input. Per v2_2 §2.3 (structural enforcement of the inherited-structure contamination guard), you design new VCGs purely from the meaning corpus. CC dissolves the old VCGs in Phase 8 with a researcher comparison report.

---

## Decisions already made — do NOT re-debate

1. **Sub-group structure** (7 sub-groups: 6 substantive + BOUNDARY) is final. Don't propose renaming, merging, or splitting sub-groups at Phase 7.
2. **Term-to-sub-group placements** (86 links: 43 primary + 28 secondary + 15 boundary) are final. CC reconciled 4 label inconsistencies from AI's Phase 5 design at apply time (see Phase 6 applied report §"Primary-label reconciliation").
3. **The 58 terms are M04's term set.** 5 terms were transferred out at Phase 4 (hēdonē→M28, tharseō ×2→M23, ga.vah→M08, mar.ge.ah→M33). Don't propose adding terms back.
4. **BOUNDARY terms** (15) have their `M04-BOUNDARY` sub-group placement set. Per M01/M02/M03 precedent, BOUNDARY gets a **single aggregating VCG** — no characteristic-bearing VCG design at Phase 7.

---

## Sub-group sizes — VCG-count expectations

These are guidelines, not constraints. Your judgment from the meaning corpus governs.

| Sub-group | Verses | Likely VCG count |
|---|---:|---|
| **M04-A Exultant Joy in the LORD** | 661 | **8–12 VCGs** — by far the largest sub-group; will need fine distinctions (joy in YHWH's salvation, joy of the heart, NT joy in Christ, communal exultation, joy in worship/song, joy as fruit of Spirit, joy in suffering paradox, etc.) |
| M04-B Communal and Festive Rejoicing | 10 | 1–2 VCGs |
| M04-C Delight in God's Word and Law | 16 | 1–2 VCGs |
| M04-D Promised and Eschatological Joy | 24 | 2 VCGs (OT promise vs NT eschatological consummation) |
| M04-E Pleasantness and Relational Delight | 28 | 2–3 VCGs (divine delight in his people / pleasantness register / relational delight) |
| M04-F Wonder at God's Marvellous Works | 77 | 3–4 VCGs (God's marvellous deeds as object of wonder, marvelling response, wonder-as-difficult/extraordinary, NT thaumazō register) |
| M04-BOUNDARY | 322 | **1 aggregating VCG** (placeholder; researcher disposition at Phase 12) |
| **Estimated total** | | **~18–25 new VCGs** |

---

## Special handling for M04

### 1. M04-A is the dominant sub-group — careful granular VCG design

661 verses (~58% of the substantive corpus). M04-A holds the joy-in-YHWH core register: sa.mach (147 OWNER verses), sim.chah (89), chairō (58), chara (57), gil_verb (44), su.s (23), sa.me.ach (21), ma.s.vo.s (16), agalliao (11), gil (8), sunchairo (7), agalliasis (5), re.na.nah (4), euthumeō (3), eufrosune (2), gi.lah (2), ched.vah ×2 (2+1), oninemi (1), sa.lad (1), mav.li.git (1) — 22 primary terms.

Within this corpus, distinct registers visible:
- **Joy in YHWH / vertical exultation** (Psa 16:11; Phil 4:4; Hab 3:18; 1Sa 2:1; Isa 61:10) — joy specifically anchored in YHWH or his salvation
- **Joy in YHWH's works / deliverance** (Exo 15; Psa 9; Psa 92; Hab 3) — celebrating what God has done
- **Joy of the heart / inner gladness** (Pro 15:13; Pro 15:15; Pro 17:22; Psa 4:7; Psa 19:8; Psa 119:111) — locating joy in the heart/inner being
- **NT joy in Christ / joy of the Spirit** (Joh 15:11; 16:22; Rom 14:17; Gal 5:22; Phil 1:25; Phil 4:4; 1Th 1:6) — joy as gospel/Spirit-given
- **Joy in suffering paradox** (Mat 5:12; Rom 5:3; Jam 1:2; 1Pe 1:6,8; 4:13; Phil 1:18; 2Cor 6:10) — NT-distinctive register
- **Joy of the redeemed / eschatological** (overlaps with M04-D but corpus-grounded distinctions may exist)
- **Worship-joy / praise-as-joy** (Psa 33:1; Psa 100; 2Sa 6:14; 1Ch 15:25; Neh 12:43) — joy expressed in worship

Design VCGs that capture these distinctions — likely 8–12 VCGs in this sub-group alone. Use VCG-level scope markers (v2_2 §14.4) for findings later.

### 2. M04-F Wonder corpus — pa.la verb dominates

77 verses across pa.la (63), pe.le (13), miph.la.ah (1). The pa.la verb register splits:
- **God's marvellous works as object** — Israel marvelling at YHWH's wonders (Exo 15:11; Psa 9:1; Psa 26:7; Psa 96:3; Psa 105:2)
- **Wonder as "too difficult / extraordinary"** — Gen 18:14 ("is anything too hard for the LORD?"); Deu 17:8; Jer 32:17,27
- **Wonder as the human inner response of marvelling** — Job 9:10; Mat/Mar/Luk thaumazō (which is BOUNDARY, not here)

The first register dominates. Design 3–4 VCGs.

### 3. Programme scope reminder — divine joy in scope

M04 routinely shows God rejoicing, delighting, taking pleasure: Zep 3:17 (he will exult over you with loud singing); Isa 62:5 (as a bridegroom rejoices over the bride); Mat 3:17 / Luk 12:32; Pro 11:20 (the upright are his delight); Eph 1:5 (according to the good pleasure of his will). These are **characteristic-in-operation** descriptions — joy/delight enacted by God toward his people — and they STAY in M04 per M01/M02/M03 precedent.

The narrow set-aside criterion (per Phase 7 review): verses where God's joy is described as an *independent divine inner life event* (analogous to M01 Deu 32:27, Job 25:2). Watch for these. M04 likely has few strict candidates.

### 4. M04-BOUNDARY — single aggregating VCG

Per M01/M02/M03 precedent, BOUNDARY gets one aggregating VCG (e.g. `M04-BOUNDARY-VCG-01`) with a brief context description naming the analytical question. The 322 verses (15 terms) route to it. Researcher disposition at Phase 12.

**Special note**: H2896A tov accounts for 230 of these 322 verses. AI's Phase 3 cross-routing flag 4 provided a 6-sub-register map for Phase 12 split (creation-assessment / inner-delight / wellbeing / moral-quality / volitional-deference / property-good). Do **not** decompose tov at Phase 7 — single aggregating BOUNDARY VCG only.

Anchor verse for M04-BOUNDARY-VCG-01: pick the verse with the most analytically clear inner-being content. Candidates: Psa 16:11 (path of life — joy and pleasures); Pro 15:15 (cheerful heart is a continual feast); a tov inner-delight verse.

### 5. Multi-faceted (secondary) terms — 28 placements

28 secondary placements across sub-groups (per the Phase 6 reconciliation). These are at the **term** level only. A verse's primary VCG comes from its **term's primary sub-group**. If a verse's meaning straddles two VCGs (within or across sub-groups), record it as **dual-membership** at the verse level in your Phase 7 design — CC applies primary-VCG routing + records secondary VCGs in `verse_context.notes`.

The reconciliation adjusted 4 terms' primary labels:
- mti=3844 sha.a → primary M04-C (secondary M04-A)
- mti=790 sha.a.shu.im → primary M04-C (secondary M04-A)
- mti=3837 ed.nah → primary M04-E (secondary M04-A)
- mti=361 sa.s.von → primary M04-D (secondary M04-A)

These four terms have verses routed to their primary sub-group; design VCGs accordingly.

### 6. Anchor designation — one per VCG

Each VCG gets exactly one AI-designated anchor verse (the most directly definitional verse). After your design, CC may add **provisional anchors per term** (R4 rule — every term with is_relevant verses must have ≥1 anchor; if your designated VCG anchors don't cover all of a VCG's terms, CC fills the gap with provisional anchors).

### 7. Cross-routing flags

If during the VCG design you notice a verse whose meaning fits better in a different sub-group than where Phase 6 routed it, flag it in a cross-routing document — CC may apply small corrections alongside the Phase 7 directive. Don't change sub-group structure at Phase 7; just note the observation.

### 8. Missing meanings (19 verses)

19 verses lack a Pass A meaning — all are XREF copies (vc rows linked to `vr.delete_flagged=1` verse_records). They appear in the grouped report with `_(missing — re-run Phase 2)_`. They are XREF inheritances from OWNER copies elsewhere; don't let them dominate any VCG. Assign each to a VCG based on its term + reference (similar to OWNER siblings).

| Sub-group | Missing meanings (XREF) |
|---|---:|
| M04-A | 15 |
| M04-B | 2 |
| M04-E | 2 |
| **TOTAL** | **19** |

---

## Output expected from you

### 1. VCG design document per sub-group

For each substantive sub-group (M04-A through M04-F), one document:

`Sessions/Session_Clusters/M04/WA-M04-{subgroup_code}-vcg-design-v1-20260517.md`

Per VCG, list:

- Provisional `group_code` (e.g. `M04-A-VCG-01`)
- `context_description` (one paragraph)
- Member verses (vc_id + reference + term)
- Anchor verse (single vc_id with rationale)
- Dual-membership flags (verses also belonging to a second VCG)

For M04-BOUNDARY: a single section with the 15 BOUNDARY terms and a note that no full VCG design is warranted (one aggregating VCG covers all 322 verses).

### 2. VCG creation JSON

`Sessions/Session_Clusters/M04/WA-M04-vcg-creation-v1-20260517.json` — machine-readable form of the design, for CC to apply:

```json
{
  "cluster_code": "M04",
  "M04-A": {
    "vcgs": [
      {
        "provisional_code": "M04-A-VCG-01",
        "description": "...",
        "verses": [12345, 12346, ...],
        "anchor_vc_id": 12345
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
        "description": "Aggregating VCG for BOUNDARY terms — pending researcher disposition at Phase 12. Members: 15 terms spanning thanksgiving, wonder-mixed-with-shock, blessedness, pleasing/pleasantness, refined-luxury, priestly soothing-aroma, predatory exultation, and the 230-verse tov sub-register map awaiting Phase 12 split.",
        "verses": [...],
        "anchor_vc_id": ...
      }
    ]
  }
}
```

### 3. Cross-routing flags (if any surfaced)

`Sessions/Session_Clusters/M04/WA-M04-phase7-cross-routing-flags-v1-20260517.md` — list of verses whose meaning suggests a different sub-group than current placement, plus any divine-inner-state set-aside candidates per §3 above.

### ⚠️ STAGED WRITE-OUT — mandatory

Same discipline as previous AI phases:

1. Process M04-A → write `WA-M04-M04-A-vcg-design-v1-20260517.md` to disk **immediately**.
2. Process M04-B → write to disk **immediately**.
3. Continue per sub-group (M04-C, D, E, F, BOUNDARY); each design document goes to disk as soon as it's complete.
4. After all 7 design docs are saved, derive the unified `WA-M04-vcg-creation-v1-20260517.json` and write to disk.
5. Cross-routing flags (if any) → write at the end.

Do NOT accumulate all 7 sub-group designs + JSON + flags in working context.

---

## Discipline reminders

1. **No inherited VCG visible in your input.** Suppressed structurally per v2_2 §2.3. Each new VCG you design is grounded in the meaning corpus alone.

2. **Anchor verse must be the most directly definitional.** Not the most popular reference; the one whose meaning best names what the VCG describes.

3. **Anchor R4 rule:** every term with is_relevant verses must have ≥1 anchor. CC enforces this; you focus on the VCG-level designation.

4. **Per v2_2 §10.4: NO Pass C reconciliation.** Do not compare new VCGs against inherited VCGs. The inherited VCGs are not in your input precisely because you should not reconcile.

5. **Don't conflate VCGs across sub-groups.** Each VCG belongs to one sub-group.

6. **Anchor citation discipline** — when writing an anchor verse rationale, cite the verse reference (e.g. `Psa 16:11`) and brief content. No backwards-referencing to inherited VCGs.

7. **Output to new files, not in-place edits.** Produce v1 documents per the filenames above.

8. **VCG creation JSON shape** — top-level keys are sub-group codes (`M04-A`, `M04-B`, ..., `M04-BOUNDARY`) per M03 precedent. Use `provisional_code` (not `group_code`), `description`, `verses` array, `anchor_vc_id`.

---

## When you're done

CC will:

1. Validate your per-sub-group designs against the verse list (every is_relevant vc routed to exactly one new VCG; every VCG has an anchor).
2. Build a unified VCG creation patch (with reconciliation for any missing verses or invalid entries per M03 precedent).
3. Apply the Phase 7 directive: INSERT verse_context_group rows, INSERT vcg_term links, UPDATE verse_context.group_id, UPDATE verse_context.is_anchor=1 per anchor designation.
4. Apply cross-routing corrections + divine-inner-state set-asides alongside.
5. Generate Phase 8 input — VCG dissolution (CC handles old VCG soft-delete; no AI involvement).
6. Phase 9 onwards: catalogue prompts, inherited findings reconciliation, cluster_finding load, closure.

---

## Provenance

- Per-sub-group meanings report (primary input): [wa-cluster-M04-subgroup-meanings-v1-20260517.md](wa-cluster-M04-subgroup-meanings-v1-20260517.md)
- Phase 6 applied: [WA-M04-dir-002-subgroup-routing-applied-v1-20260517.md](WA-M04-dir-002-subgroup-routing-applied-v1-20260517.md)
- Phase 5 AI sub-group design: [files phase 5/WA-M04-subgroup-design-v1-20260517.md](files%20phase%205/WA-M04-subgroup-design-v1-20260517.md)
- Phase 4 applied: [WA-M04-dir-001-term-transfer-applied-v1-20260517.md](WA-M04-dir-001-term-transfer-applied-v1-20260517.md)
- Governing instruction: [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md)
- Validation methodology: [Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md](../../../Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md)

---

*End of Phase 7 brief.*
