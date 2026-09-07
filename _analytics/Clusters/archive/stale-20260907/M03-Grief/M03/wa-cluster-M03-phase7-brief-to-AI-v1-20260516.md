# M03 Phase 7 brief — VCG design within sub-groups

**Audience:** Claude AI
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) §10 (Phase 7)
**Date:** 2026-05-16

---

## State of M03 at Phase 7 open

| Item | Count / value |
|---|---|
| Active terms in M03 | 78 |
| Active sub-groups | **8** (M03-A · M03-B · M03-C · M03-D · M03-E · M03-F · M03-G · M03-BOUNDARY) |
| `mti_term_subgroup` links | 82 (49 primary + 5 secondary + 28 boundary) |
| is_relevant verses routed to sub-groups | **691** |
| Inherited VCGs in DB | 114 — **NOT visible to you** (suppressed per v2_2 §2.3); Phase 8 will dissolve them after your work lands |
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

[Sessions/Session_Clusters/M03/wa-cluster-M03-subgroup-meanings-v1-20260516.md](wa-cluster-M03-subgroup-meanings-v1-20260516.md) — per-sub-group, every is_relevant verse with reference, term, and Phase 2 meaning. Canonical Bible order within each sub-group. **This is the only analytical material you need for Phase 7.**

### Reference (do not re-debate, but useful to know what's been decided)

- [WA-M03-dir-002-subgroup-routing-applied-v1-20260516.md](WA-M03-dir-002-subgroup-routing-applied-v1-20260516.md) — Phase 6 applied report.
- [files phase 5/WA-M03-subgroup-design-v1-20260516.md](files%20phase%205/WA-M03-subgroup-design-v1-20260516.md) — Phase 5 AI design (sub-group descriptions).

### Suppressed by design

Inherited VCGs (114 in DB) are NOT in your input. Per v2_2 §2.3 (structural enforcement of the inherited-structure contamination guard), you design new VCGs purely from the meaning corpus. CC dissolves the old VCGs in Phase 8 with a researcher comparison report.

---

## Decisions already made — do NOT re-debate

1. **Sub-group structure** (8 sub-groups: 7 substantive + BOUNDARY) is final. Don't propose renaming, merging, or splitting sub-groups at Phase 7. If you find a verse whose meaning fits a different sub-group than where it's currently routed, that's a Phase 7 cross-routing observation — note it; don't change sub-group structure.
2. **Term-to-sub-group placements** (82 links: 49 primary + 5 secondary + 28 boundary) are final. Don't re-debate which term belongs in which sub-group.
3. **The 78 terms are M03's term set.** 11 terms were transferred out at Phase 4 (apobolē→M11, basanismos→M35, basanistēs→M27, diafthora→M25, pikria→M02, pikros→M28, be.ha.lah→M01, de.a.vah→M01, dak.kah→M24, ra.ah-evil→M27, te.u.nim→M36). Don't propose adding terms back.
4. **BOUNDARY terms** (28) have their `M03-BOUNDARY` sub-group placement set. Per M01/M02 precedent, BOUNDARY gets a **single aggregating VCG** — no characteristic-bearing VCG design at Phase 7.

---

## Sub-group sizes — VCG-count expectations

These are guidelines, not constraints. Your judgment from the meaning corpus governs.

| Sub-group | Verses | Likely VCG count |
|---|---:|---|
| M03-A Weeping and Tears | 170 | 4–6 VCGs (bereavement weeping, penitential weeping, communal/national weeping, prophet's weeping for his people, eschatological weeping, etc.) |
| M03-B Mourning and Lamentation | 117 | 4–5 VCGs (mourning rites for the dead, mourning over national calamity, divinely commanded/withheld mourning, mourning as inner state in NT pen.the.o/penthos) |
| M03-C Sorrow and Inner Grief | 46 | 2–3 VCGs (soul/heart-located sorrow; godly grief leading to repentance; Spirit-grieved/Christ-grieved) |
| M03-D Anguish and Distress | 105 | 4–6 VCGs — **largest psalm-rich corpus**: tsa.rah (62v) + tsar (28v) drive multiple VCGs (psalmist's distress that drives prayer, God's deliverance from distress, distress as covenantal discipline, etc.) |
| M03-E Groaning and Sighing | 31 | 2–3 VCGs (slavery/oppression groaning; Spirit-and-creation groaning in Rom 8; travail-cry imagery) |
| M03-F Pain and Inner Ache | 36 | 2–3 VCGs (servant of Isaiah's bearing pain; unceasing inner pain as relational rupture; birth-pangs imagery as metaphor) |
| M03-G Bitterness of Soul | 8 | **1 VCG** (small corpus — likely one cohesive VCG: bitterness as inner experience of grief, suffering, divine dealings) |
| M03-BOUNDARY | 178 | **1 aggregating VCG** (placeholder; researcher disposition at Phase 12) |
| **Estimated total** | | **~20–28 new VCGs** |

---

## Special handling for M03

### 1. Programme scope reminder — human inner being

The programme's scope is **human inner being**. Grief, however, is also attributed to God and to the Spirit in Scripture (e.g. Eph 4:30 — the Spirit grieved; Gen 6:6 — God grieved in heart; Heb 3:10 — God grieved with the wilderness generation). Most of these describe **the characteristic in operation** (God's grief as relational response, the Spirit's grief at sin) — these belong in the cluster and form their own VCGs.

The set-aside criterion (per M01/M02 precedent) is narrower: verses that describe **God's internal emotional experience as a divine inner life event** — analogous to M01's Deu 32:27 (God's apprehension), Eze 16:43 (God's fury aroused), Job 25:2 (dread as attribute of God's dominion). Watch for verses where the verse content focuses on God or the Spirit *inwardly experiencing* grief as a passion/inner state rather than enacting it. Flag these as set-aside candidates — CC will apply.

Hint: M03 likely has a handful of strict candidates (Gen 6:6 if present; Psa 95:10 / Heb 3:10 if present; Eph 4:30 borderline). Don't over-apply — Jesus weeping at Lazarus' tomb, Jesus sorrowful unto death, Paul's grief over Israel are all inner-being-in-operation in scope.

### 2. M03-D Anguish and Distress — the dominant sub-group, will need granular VCGs

105 verses, but the bulk are from **tsa.rah (62v)** and **tsar (28v)** — both with strong psalmist-prayer corpora. Within the psalmist's distress vocabulary there are distinct registers:

- **Distress as occasion of prayer** — "in my distress I cried to YHWH and he answered me"
- **Distress as covenantal discipline** — distress sent because of sin, leading to repentance
- **Distress that finds the soul/spirit** — the explicit inner-located distress (Job 7:11; Psa 31:7)
- **Eschatological distress / day-of-distress** — prophetic distress oracles
- **NT anguish vocabulary** — sunochē (Paul's pastoral anguish at 2Cor 2:4), odunē (Rom 9:2), odunaō (Luke 16 afterlife anguish; Acts 20:38 relational anguish)

Expect 4–6 VCGs across this sub-group. Don't artificially split or collapse; let the meanings group.

### 3. M03-A Weeping and Tears — large NT+OT mixed corpus

170 verses across 9 terms (8 primary + a.na.qah secondary). The corpus spans:

- **Bereavement weeping** (Gen 23:2, 50:1; Jer 31:15 Rachel; Mat 2:18)
- **Penitential / repentant weeping** (Joe 2:12; Ezr 10:1; 2Ki 22:19; Luke 7:38 the sinful woman)
- **Communal weeping** (Deu 34:8; Num 20:29; Neh 1:4; Neh 8:9)
- **The prophet's weeping for his people** (Jer 9:1; Isa 16:9; Lam-corpus)
- **Eschatological weeping** — judgment (Mat 8:12, Luke 13:28) and end-of-tears (Isa 25:8, 65:19; Rev 21:4)

Expect 4–6 VCGs.

### 4. M03-G Bitterness of Soul — small but coherent

Only 8 verses across 6 primary terms (me.mer, mam.ror, mo.rah, mor.rah, ma.ror, pikrainō). The Phase 5 design positioned this as inner-bitterness arising from grief/suffering/divine dealings. Most likely **a single cohesive VCG** ("bitterness as the soul's experience of grief made sharp"), unless your corpus reading distinguishes:

- divinely-imposed bitterness (Job 9:18; Lam 3:15)
- relationally-inflicted bitterness (Pro 17:25 son to mother; Col 3:19 husband to wife)
- prophetic-judgment bitterness (Rev 10:9-10)

If you see two or more clean VCGs in just 8 verses, design them; otherwise 1 VCG.

### 5. M03-E Groaning and Sighing — Rom 8 cluster significant

31 verses but Rom 8:22-26 alone houses the most theologically dense groaning text in scripture (Spirit's groaning, creation's groaning together). Likely VCG split:

- **Slavery / oppression groaning** (Exo 2:23-24; Israel under affliction)
- **Spirit-and-creation groaning in Rom 8** (Rom 8:22-26 — sustenazō, stenagmos)
- **Travail / birth-cry imagery** (Gal 4:19; Rev 12:2; ōdinō corpus)

### 6. M03-F Pain and Inner Ache — Isa 53 servant + che.vel-B birth-pangs

36 verses. Two large meaning clusters within:

- **Servant of Isaiah** (Isa 53:3-4; makh.ov used distinctively here)
- **Unceasing inner pain as relational rupture / divine wound** (Jer 15:18; Psa 38:17)
- **Birth-pangs metaphor** (che.vel-B at Isa 13:8; 26:17; Jer 13:21; 22:23; 49:24)

Likely 2–3 VCGs.

### 7. M03-BOUNDARY — single aggregating VCG

Per M01/M02 precedent, BOUNDARY gets one aggregating VCG (e.g. `M03-BOUNDARY-VCG-01`) with a brief context description naming the analytical question. The 178 verses (28 terms) route to it. Researcher disposition at Phase 12.

Anchor verse for M03-BOUNDARY-VCG-01: pick the verse with the most analytically clear inner-being content (likely from one of the larger BOUNDARY corpora: ra.ah-harm, a.mal, ma.rar, or si.ach).

### 8. Multi-faceted (secondary) terms — 5 placements

5 secondary placements:
- pen.the.o (42, G3996) — primary M03-B; secondary M03-C (inner-grief register at Mat 5:4, Jam 4:9)
- penthos (43, G3997) — primary M03-B; secondary M03-C (Jam 4:9)
- a.na.qah (898, H0603) — secondary in both M03-A and M03-E (mapping routes its verses to M03-A)
- ōdinō (7472, G5605) — primary M03-E; secondary M03-D (Rev 12:2 anguish)

These secondary placements are at the **term** level only. A verse's primary VCG comes from its **term's primary sub-group** (verse routing per Phase 6). If a verse's meaning straddles two VCGs (within or across sub-groups), record it as **dual-membership** at the verse level in your Phase 7 design — CC applies primary-VCG routing + records secondary VCGs in `verse_context.notes`.

### 9. Anchor designation — one per VCG

Each VCG gets exactly one AI-designated anchor verse (the most directly definitional verse). After your design, CC may add **provisional anchors per term** (R4 rule — every term with is_relevant verses must have ≥1 anchor; if your designated VCG anchors don't cover all of a VCG's terms, CC fills the gap with provisional anchors).

### 10. Cross-routing flags

If during the VCG design you notice a verse whose meaning fits better in a different sub-group than where Phase 6 routed it, flag it in a cross-routing document — CC may apply small corrections alongside the Phase 7 directive. Don't change sub-group structure at Phase 7; just note the observation.

### 11. Missing meanings (9 verses)

9 verses lack a Pass A meaning (1 in M03-A, 8 in M03-BOUNDARY). The 8 in BOUNDARY are immaterial since BOUNDARY is structural-only. The 1 in M03-A will be visible in the meanings report as `_(missing — re-run Phase 2)_` — assign it to the most fitting M03-A VCG based on the term + reference + verse text (CC can pre-fill that meaning on follow-up if needed). Don't let it dominate any VCG.

---

## Output expected from you

### 1. VCG design document per sub-group

For each substantive sub-group (M03-A through M03-G), one document:

`Sessions/Session_Clusters/M03/WA-M03-{subgroup_code}-vcg-design-v1-20260516.md`

Per VCG, list:

- Provisional `group_code` (e.g. `M03-A-VCG-01`)
- `context_description` (one paragraph)
- Member verses (vc_id + reference + term)
- Anchor verse (single vc_id with rationale)
- Dual-membership flags (verses also belonging to a second VCG)

For M03-BOUNDARY: a single section with the 28 BOUNDARY terms and a note that no full VCG design is warranted (one aggregating VCG covers all 178 verses).

### 2. VCG creation JSON

`Sessions/Session_Clusters/M03/WA-M03-vcg-creation-v1-20260516.json` — machine-readable form of the design, for CC to apply:

```json
{
  "M03-A": {
    "vcgs": [
      {
        "provisional_code": "M03-A-VCG-01",
        "description": "...",
        "verses": [12345, 12346, ...],
        "anchor_vc_id": 12345
      },
      ...
    ]
  },
  "M03-B": { "vcgs": [ ... ] },
  ...
  "M03-BOUNDARY": {
    "vcgs": [
      {
        "provisional_code": "M03-BOUNDARY-VCG-01",
        "description": "Aggregating VCG for BOUNDARY terms — pending researcher disposition at Phase 12. Members: 28 terms spanning press/affliction, torment/judgment, labour-pain, faintness, toil-suffering, and mixed-register vocabulary.",
        "verses": [...],
        "anchor_vc_id": ...
      }
    ]
  }
}
```

### 3. Cross-routing flags (if any surfaced)

`Sessions/Session_Clusters/M03/WA-M03-phase7-cross-routing-flags-v1-20260516.md` — list of verses whose meaning suggests a different sub-group than current placement, plus any divine-inner-state set-aside candidates per §1 above.

### ⚠️ STAGED WRITE-OUT — mandatory

Same discipline as previous AI phases:

1. Process M03-A → write `WA-M03-M03-A-vcg-design-v1-20260516.md` to disk **immediately**.
2. Process M03-B → write to disk **immediately**.
3. Continue per sub-group (M03-C, D, E, F, G, BOUNDARY); each design document goes to disk as soon as it's complete.
4. After all 8 design docs are saved, derive the unified `WA-M03-vcg-creation-v1-20260516.json` and write to disk.
5. Cross-routing flags (if any) → write at the end.

Do NOT accumulate all 8 sub-group designs + JSON + flags in working context.

---

## Discipline reminders

1. **No inherited VCG visible in your input.** Suppressed structurally per v2_2 §2.3. Each new VCG you design is grounded in the meaning corpus alone.

2. **Anchor verse must be the most directly definitional.** Not the most popular reference; the one whose meaning best names what the VCG describes.

3. **Anchor R4 rule:** every term with is_relevant verses must have ≥1 anchor. CC enforces this; you focus on the VCG-level designation.

4. **Per v2_2 §10.4: NO Pass C reconciliation.** Do not compare new VCGs against inherited VCGs. The inherited VCGs are not in your input precisely because you should not reconcile.

5. **Don't conflate VCGs across sub-groups.** Each VCG belongs to one sub-group. If two sub-groups have similar inner-being content (e.g. anguish in M03-D and pain in M03-F), that's interesting — but they remain distinct VCGs in distinct sub-groups.

6. **Anchor citation discipline** — when writing an anchor verse rationale, cite the verse reference (e.g. `Mat 26:38`) and brief content. No backwards-referencing to inherited VCGs.

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

- Per-sub-group meanings report (primary input): [wa-cluster-M03-subgroup-meanings-v1-20260516.md](wa-cluster-M03-subgroup-meanings-v1-20260516.md)
- Phase 6 applied: [WA-M03-dir-002-subgroup-routing-applied-v1-20260516.md](WA-M03-dir-002-subgroup-routing-applied-v1-20260516.md)
- Phase 5 AI sub-group design: [files phase 5/WA-M03-subgroup-design-v1-20260516.md](files%20phase%205/WA-M03-subgroup-design-v1-20260516.md)
- Phase 4 applied (term transfers): [WA-M03-dir-001-term-transfer-applied-v1-20260516.md](WA-M03-dir-001-term-transfer-applied-v1-20260516.md)
- Governing instruction: [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md)
- Validation methodology: [Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md](../../../Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md)

---

*End of Phase 7 brief.*
