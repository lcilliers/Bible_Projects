# WA-M03-phase7-validation-v1-20260516

**Phase 7 validation report — AI VCG creation JSON**

**Source JSON:** [files phase 7/WA-M03-vcg-creation-v1-20260516.json](files%20phase%207/WA-M03-vcg-creation-v1-20260516.json)
**Validated against:** `database/bible_research.db` post-Phase-6 routing (691 is_relevant vc rows, 8 sub-groups)
**Date:** 2026-05-17

---

## §1. Summary

AI delivered **25 VCGs** across 8 sub-groups (A:5, B:4, C:3, D:5, E:3, F:3, G:1, BOUNDARY:1). Declared total in JSON `notes` reads 21 — actual count is 25 (notes string error, not structural).

**Coverage assessment vs DB routing:**

| Sub-group | DB verses | AI verses | AI-only (invalid) | DB-only (missing) |
|---|---:|---:|---:|---:|
| M03-A | 170 | 169 | 0 | 1 |
| M03-B | 117 | 115* | 0 | 2 |
| M03-C | 46 | 46 | 0 | 0 |
| M03-D | 105 | 106* | 3 | 2 |
| M03-E | 31 | 31 | 0 | 0 |
| M03-F | 36 | 36 | 0 | 0 |
| M03-G | 8 | 8 | 0 | 0 |
| M03-BOUNDARY | 178 | 175 | 0 | 3 |
| **TOTAL** | **691** | **686 unique** | **3** | **8** |

*Counts include duplicates within sub-group (see §4).

---

## §2. Invalid entries (3) — DROP

| AI placement | vc_id | Reason |
|---|---:|---|
| M03-D-VCG-01 | 1492 | Does not exist in DB (hallucination) |
| M03-D-VCG-04 | 65109 | Job 38:23 tsar — `is_relevant=0` Phase 1 set-aside ("tsar used for time of battle/war, not inner-being") |
| M03-D-VCG-05 | 96 | Rom 1:18 G3709 orgē — **M02 anger term, not M03**. Routed in DB to M02-A. AI cross-cluster error. |

Action: remove these vc_ids from their VCG member lists in the apply patch. Drop, don't reassign.

---

## §3. Missing verses (8) — ADD via primary routing

DB has these as `is_relevant=1` with sub-group routing applied at Phase 6, but AI's JSON omitted them. Each is auto-assigned to its sub-group's best-fit VCG based on Phase 2 meaning + VCG description.

| vc_id | Reference | Strong's | Translit | Sub-group | Target VCG | Rationale (from Phase 2 meaning) |
|---:|---|---|---|---|---|---|
| 54599 | Jer 3:21 | H1065 | be.khi | M03-A | `M03-A-VCG-02` | "Weeping over Israel's own spiritual perversion and forgetting of God" — penitential/contrition register |
| 18529 | Est 6:12 | H0057 | a.vel | M03-B | `M03-B-VCG-01` | Haman's mourning posture (head covered, hurried home) — fits personal mourning-rite pattern |
| 29990 | Mic 1:8 | H5594 | sa.phad | M03-B | `M03-B-VCG-02` | Prophet's anticipatory lament over coming national devastation |
| 12781 | Isa 8:22 | H6695B | tsu.qah | M03-BOUNDARY | `M03-BOUNDARY-VCG-01` | Single aggregating VCG |
| 12782 | Pro 1:27 | H6695B | tsu.qah | M03-BOUNDARY | `M03-BOUNDARY-VCG-01` | Single aggregating VCG |
| 28984 | Psa 142:2 | H7879 | si.ach | M03-BOUNDARY | `M03-BOUNDARY-VCG-01` | Single aggregating VCG |
| 91 | Luk 2:48 | G3600 | odunaō | M03-D | `M03-D-VCG-05` | NT anguish vocabulary (parental anguish over missing Jesus) — fits VCG-05 NT-anguish register |
| 1359 | Jon 2:2 | H6869B | tsa.rah | M03-D | `M03-D-VCG-01` | "Jonah called out to God from within personal distress" — textbook VCG-01 (distress drives prayer, God answers) |

---

## §4. Duplicate assignments (7) — primary + secondary

7 verses appear in multiple VCG member lists. Resolution: pick primary VCG (consistent with anchor + description), record other as `secondary_vcg` note for `verse_context.notes`.

| vc_id | Reference | Term | AI placements | Primary | Secondary | Rationale |
|---:|---|---|---|---|---|---|
| 18501 | Neh 1:4 | a.val | M03-B-VCG-02 ×2 | M03-B-VCG-02 | — | True duplicate within same VCG — collapse |
| 29992 | Zec 12:12 | sa.phad | M03-B-VCG-03, M03-B-VCG-04 | M03-B-VCG-03 | M03-B-VCG-04 | OT verse — primary fits OT divine-mourning agency |
| 38169 | Job 30:31 | e.vel | M03-B-VCG-01, M03-B-VCG-02 | M03-B-VCG-01 | M03-B-VCG-02 | Job's personal mourning — primary fits VCG-01 rites |
| 54598 | Isa 65:19 | be.khi | M03-A-VCG-03, M03-A-VCG-05 | M03-A-VCG-05 | M03-A-VCG-03 | Eschatological end-of-weeping — primary VCG-05 fits definitionally |
| 65102 | 2Sa 24:14 | tsar | M03-D-VCG-03 ×2 | M03-D-VCG-03 | — | True duplicate — collapse |
| 65106 | Job 7:11 | tsar | M03-D-VCG-01, M03-D-VCG-02 | **M03-D-VCG-02** | M03-D-VCG-01 | vc=65106 is the **anchor** of VCG-02 ("from the anguish of my spirit"); anchor must be a primary member |
| 65175 | Zep 1:15 | tsa.rah | M03-D-VCG-01, M03-D-VCG-04 | M03-D-VCG-04 | M03-D-VCG-01 | "day of distress" — prophetic-oracle register fits VCG-04 |

---

## §5. Anchor issue (1) — DUAL-MEMBERSHIP RESOLUTION

**M03-D-VCG-05** — anchor `vc_id=144` (2Cor 2:4 sunochē) is NOT listed in the VCG's member list `[96, 89, 92, 143, 90]`. **However, vc=144 IS in M03-D-VCG-02's member list** `[93, 94, 144, 65106, 65122, 65126]` (heart-located distress).

This is a legitimate dual-membership: 2Cor 2:4 sunochē is both heart-located anguish (VCG-02) AND quintessential NT anguish vocabulary (VCG-05). AI placed the verse in VCG-02 but designated it as VCG-05's anchor.

Action: treat as dual. **Primary = M03-D-VCG-05** (to honour the anchor designation: anchor must be a primary member); **secondary = M03-D-VCG-02**. Append to §4 dual-membership table:

| vc_id | Reference | Term | AI placements | Primary | Secondary | Rationale |
|---:|---|---|---|---|---|---|
| 144 | 2Cor 2:4 | sunochē | M03-D-VCG-02 member + M03-D-VCG-05 anchor | M03-D-VCG-05 | M03-D-VCG-02 | Anchor designation governs primary; heart-located is secondary |

Final M03-D-VCG-05 primary members: `[89, 90, 91, 92, 143, 144]` (with 91 added from §3, 96 dropped per §2). All six are NT anguish vocabulary.

---

## §6. JSON `notes` field correction

AI's `notes` field reads: `"21 VCGs across 8 sub-groups (5+4+3+5+3+3+1+1)"`. The sum is 5+4+3+5+3+3+1+1 = 25, not 21. Counted VCGs match the structural total of 25. Treated as cosmetic typo; no structural impact.

---

## §7. Reconciliation outcome — post-apply state

After applying §2–§5 fixes:

- **25 VCGs** inserted (8 sub-groups · 1 BOUNDARY)
- **691 verses** primary-routed (matches Phase 6 routing)
- **5 dual-membership notes** in `verse_context.notes` (vc 29992, 38169, 54598, 65106, 65175)
- **25 anchors** set (`is_anchor=1`), each a primary member of its VCG
- **3 invalid placements** dropped (vc 1492, 65109, 96)
- **8 missing verses** assigned via primary routing

Coverage will be 100% — every `is_relevant=1, delete_flagged=0, cluster_code=M03` vc row will have `group_id` set.

---

## §8. Decision rationale

Per researcher precedent (M02 Phase 7 recovery of 39 missing verses via CC reconciliation, and "small chunks over elaborate pipelines" principle): minor coverage gaps are reconciled at the CC level via primary-routing rather than re-sending the brief to AI. The 11 affected verses (8 missing + 3 invalid) represent ~1.6% of the corpus and have clear, low-risk assignments from Phase 2 meanings + VCG descriptions. Cross-cluster error (vc=96 orgē→M02) is a clean drop. Hallucination (vc=1492) is a clean drop. Set-aside leakage (vc=65109) is a clean drop.

Anchor fix for M03-D-VCG-05 (adding vc=144 to members) is structural — anchor must be a member, AI omitted it.

Duplicates are reconciled by primary-VCG selection (anchor-membership rule + definitional description fit) with secondary VCG recorded in `verse_context.notes`.

---

*End of Phase 7 validation report.*
