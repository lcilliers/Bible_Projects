# M08 Phase 7 — VCG design within sub-groups — brief

**Date:** 2026-05-20
**Cluster:** M08 — Pride, Arrogance and Boasting
**Phase:** 7 (VCG design within sub-groups)
**Audience:** Claude AI session (chat)
**Governing instruction:** `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §10

**Read this brief first.** The structural input is the per-sub-group meanings report below.

---

## Required inputs

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M08/WA-M08-phase7-vcg-brief-v1-20260520.md` | Primary task instructions |
| 2 | **Per-sub-group meanings report** — `Sessions/Session_Clusters/M08/wa-cluster-M08-subgroup-meanings-v1-20260520.md` | Per sub-group, every is_relevant verse with its term + Phase 2 meaning, in canonical Bible order. **The only analytical material for VCG design** (inherited VCGs / anchors / findings explicitly suppressed per §2.3) |
| 3 | **Phase 5 v2 sub-group design** — `Sessions/Session_Clusters/M08/WA-M08-subgroup-design-v2-20260520.md` | Sub-group definitions (characteristic-representations), seat-of-pride split axis, cross-register flags, BOUNDARY notes |
| 4 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §10 (Phase 7 disciplines; §10.7 staged write-out; §10.8 no-sampling pre-submission checklist) |
| 5 | **Science extract** — `Workflow/Sciences/wa-m08-pride-scienceextract-v1_0-20260513.md` | Programme-curated scientific framing of pride |
| 6 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-{current}.md` Ch.1 'Defining Inner Being' | Inner-being scope definition |
| 7 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |

---

## Context

M08's sub-group structure landed at Phase 6 (applied 2026-05-20T19:04:22Z): **9 sub-groups** (8 substantive + BOUNDARY), **296 is_relevant verses** distributed cleanly (largest substantive M08-C at 23.7% — well under the 40% gate). Each sub-group represents a characteristic per v2_8 §8.0; the four M08-A sub-groups are a volume-split of CHAR-1 by **seat-of-pride** axis (heart / eyes-bearing / national-collective / general-dispositional).

| Sub-group | Characteristic | Verses | Cross-register flag |
|---|---|---:|---|
| M08-A1 | CHAR-1 Arrogant self-elevation (seat: **heart**) | 32 | — |
| M08-A2 | CHAR-1 Arrogant self-elevation (seat: **eyes & outward bearing**) | 11 | — |
| M08-A3 | CHAR-1 Arrogant self-elevation (seat: **national / collective**) | 40 | — |
| M08-A4 | CHAR-1 Arrogant self-elevation (seat: **general dispositional**) | 68 | — |
| M08-B | CHAR-2 Presumptuous defiance | 45 | — |
| M08-C | CHAR-3 Boasting and self-display | 70 | **M22** (praise/glory) |
| M08-D | CHAR-4 Vain conceit | 12 | — |
| M08-E | CHAR-5 Pride of power and position | 17 | **M23** (strength/dominion) |
| M08-BOUNDARY | (G0193 akratēs — qualifying/supportive register) | 1 | — |
| **Total** | | **296** | |

Phase 7's task is to design **VCGs (verse_context_groups)** within each sub-group — finer-grained units that cluster verses with substantively similar inner-being content inside the sub-group's register.

**Note on Phase 5.5 set-aside (researcher direction, Option 2):** 174 verses formerly held in M08-F (122 M22-register polysemic-residual) and M08-G (52 narrative-marker / neutral-assertiveness) were set_aside via Phase 5.5 patch and do NOT appear in this report. The 296 verses you see are the substantive M08 inner-being corpus.

---

## Your task — per sub-group, design VCGs

For each sub-group (in code order: M08-A1 → M08-A2 → M08-A3 → M08-A4 → M08-B → M08-C → M08-D → M08-E → M08-BOUNDARY), produce:

1. **VCG definitions** — provisional `group_code`, `context_description`, member verse list, one anchor verse.
2. **Per-sub-group design document** written to disk **immediately** after designing that sub-group (mandatory per §10.7 staged write-out — clears working context before moving on).
3. **Per-sub-group sum verification** — total member vc_ids across the sub-group's VCGs must equal the sub-group's verse count from the meanings report.

After all sub-groups are processed, produce the **unified VCG creation JSON** (one file covering all sub-groups).

---

## Process per sub-group (§10.2 + §10.7 staged write-out)

1. **Read** every verse-meaning in the sub-group's section of the meanings report. **Every row. No skipping. No sampling.**
2. **Cluster meanings into provisional VCGs.** A VCG groups verses with substantively similar inner-being content within the sub-group's characteristic. Typical sub-groups produce 2–8 VCGs.
3. **Name each VCG** with a provisional code (suggested format: `{subgroup_code}-VCG-{seq}`, e.g. `M08-A1-VCG-01`) and a one-paragraph `context_description` written from the meanings.
4. **Designate ONE anchor verse per VCG** — the verse that most directly and definitionally evidences the phenomenon the VCG names. The anchor's vc_id must be in the VCG's member list.
5. **Note dual-membership verses** — verses that legitimately belong to two VCGs (within the same sub-group, or rarely across sub-groups). Flag explicitly.
6. **Write the per-sub-group design document to disk immediately:**
   `Sessions/Session_Clusters/M08/WA-M08-{subgroup_code}-vcg-design-v1-20260520.md`
7. **Verify sum.** Sum member vc_ids across the sub-group's VCGs. Must equal the sub-group's count from the meanings report. Record verification line at end of the document:

   ```
   **Verification**: VCG member sums = N1 + N2 + ... + Nk = TOTAL, matches M08-{X} input count of TOTAL ✓
   ```

8. Move to next sub-group; repeat.

---

## Cross-register flags — preserve at VCG level

**M08-C (Boasting and self-display, M22 flag, 70 verses):** This is the most analytically demanding sub-group for Phase 7. The kauchaomai family + ha.lal-self-boasting subset span three distinct registers that need VCG-level separation:

1. **Condemned self-directed boasting** — boasting of wisdom / might / wealth, premature self-glorification (1Ki 20:11; Pro 27:1; Jer 9:23; Jam 4:13–16). The straightforward M08 register.
2. **Pauline examined boasting discourse** — Paul's complex engagement with what constitutes legitimate vs illegitimate boasting (1Co 1:31; 2Co 10:13–17; 2Co 11–12 weakness boasting; Gal 6:14 cross-boasting). The reflective inversion that boasts only in the Lord / in weakness / in the cross — pride's inversion through grace.
3. **God-directed glorying** — kauchaomai with God as object (Rom 5:11; 5:2; 2Co 7:14 etc.) and ha.lal as praise-of-God (Psa 34:2; 44:8; 105:3 etc., where ha.lal in this sense survived to is_relevant). The M22 register that lives inside M08's vocabulary by linguistic accident.

Design at least one VCG per register so Phase 9 can address them as distinct phenomena. The M22 cross-register flag carries into the context_description of the God-directed VCG and the Pauline VCG.

**M08-E (Pride of power and position, M23 flag, 17 verses):** Three sub-registers within: (a) national/collective proud-might (ga.on ×7); (b) wealth-pride (ga.vah Eze 28:5 + hupsēlofroneō 1Ti 6:17); (c) domineering-authority + imperious self-will (archō Mar 10:42, shal.le.tet, a.din, ma.rom power-height ×4, qo.mah Eze 19:11). The M23 flag's relational dynamic — strength-as-misuse — should be visible in each VCG's context_description.

---

## M08-A family — seat-of-pride VCG design notes

The four M08-A sub-groups share CHAR-1 identity, split by anatomical / framing axis. Within each, look for sub-axes:

- **M08-A1 (heart, 32V)** — likely 2–3 VCGs: (a) prosperity-induced heart-elevation (Deu 8:14; 2Ch 32:25; Hos 13:6; Eze 28:5); (b) royal/throne heart-elevation (Deu 17:20; 2Ch 26:16; Dan 11:12; Eze 28:2; Eze 28:17; Eze 31:10; Dan 5:20); (c) heart-of-pride as defining condition of moral collapse (Pro 16:5; Psa 101:5; Jer 48:29).
- **M08-A2 (eyes & outward bearing, 11V)** — likely 1–2 VCGs: (a) haughty-eyes vocabulary proper (Psa 18:27; Pro 6:17; Pro 30:13; Psa 131:1; Isa 5:15); (b) wider outward-display (Psa 73:6 necklace; Isa 3:16 daughters of Zion; Psa 10:4 face-posture; Job 10:16 head-lifted).
- **M08-A3 (national/collective, 40V)** — likely 3–4 VCGs by national subject: Moab cluster, Babylon cluster, Israel/Ephraim cluster, day-of-the-LORD cosmic-collective cluster. Or by mode: pride-as-self-description vs pride-target-of-judgment.
- **M08-A4 (general dispositional, 68V)** — likely 3–5 VCGs by mode: (a) Wisdom maxims of pride's self-defeat (Pro 16:18; Pro 29:23; etc.); (b) NT vice catalogues (Rom 1:30; 2Ti 3:2; Jam 4:6; 1Pe 5:5); (c) psalmic enemy portraits (Psa 36:11; Psa 123:4); (d) general individual pride-as-disposition (rum, ga.on, ga.a.vah individual verses); (e) self-love as root (filautos 2Ti 3:2).

These are starters — let the meanings drive the actual VCG count.

---

## BOUNDARY sub-group (M08-BOUNDARY)

1 verse only (G0193 akratēs at 2Ti 3:3). Single aggregating VCG: `M08-BOUNDARY-VCG-01` holding the 1 vc_id with a context_description naming the BOUNDARY status. Anchor: that same vc_id.

---

## Output structure

### Per sub-group design document

`Sessions/Session_Clusters/M08/WA-M08-{subgroup_code}-vcg-design-v1-20260520.md`

```markdown
# M08-{X} VCG design — {sub-group label}

**Sub-group:** {code} ({characteristic})
**Verses in scope:** {N}
**Cross-register flag:** {M-something or None}

## VCG {code}-VCG-01 — {short name}

**Description:** {one-paragraph context_description from the meanings}

**Anchor:** vc_id={X} — {Reference} — {one-line rationale: why this verse anchors the VCG}

**Members ({N} verses):**
- vc=X — Reference — Strong's translit — {one-line meaning excerpt}
- ... (every member listed)

## VCG {code}-VCG-02 — {short name}

...

## Dual-membership notes

(Any verses flagged for dual VCG membership; usually empty)

**Verification**: VCG member sums = N1 + N2 + ... + Nk = TOTAL, matches M08-{X} input count of TOTAL ✓
```

### Unified VCG creation JSON

After all sub-groups: `Sessions/Session_Clusters/M08/WA-M08-vcg-creation-v1-20260520.json`

```json
{
  "_meta": {
    "cluster": "M08",
    "phase": 7,
    "date": "2026-05-20",
    "total_subgroups": 9,
    "total_vcgs": <N>,
    "total_verses": 296
  },
  "subgroups": {
    "M08-A1": {
      "vcgs": [
        {
          "provisional_code": "M08-A1-VCG-01",
          "description": "...",
          "verses": [<every vc_id>],
          "anchor_vc_id": <vc_id>
        }
      ]
    }
  }
}
```

Field name **must** be `verses` (not `key_verses`, not `members`, not "representative" — complete arrays per §10.8).

---

## Discipline (§10.7 + §10.8)

1. **Read every verse-meaning** for each sub-group. No sampling. No "representative members." No "the rest follow the same pattern." Discipline reading is enforced by the staged write-out pattern.
2. **Stage by sub-group.** Don't try to hold all 9 sub-groups in working memory. After M08-A1: write design doc to disk, verify sum, then move to M08-A2. Repeat.
3. **Sum verification per sub-group.** Members must sum to the input count exactly. If they don't, fix before moving on.
4. **Anchor in members.** Every `anchor_vc_id` must be in its VCG's `verses` array.
5. **No phantom vc_ids.** Every vc_id used in your output must be in the meanings report (i.e. a real M08 is_relevant vc).
6. **No vc_id in two VCGs** unless explicitly flagged as dual-membership in the design document.
7. **BOUNDARY VCG aggregating only** — single VCG covering the 1 BOUNDARY verse.
8. **Preserve cross-register flags** in M08-C and M08-E VCG descriptions where they shape the analytical content.

---

## Pre-submission checklist (§10.8, AI verifies before declaring complete)

- [ ] 9 design documents on disk (one per sub-group: 8 substantive + 1 BOUNDARY).
- [ ] Each design doc carries a sum-verification line.
- [ ] Unified JSON written with field name `verses` (complete arrays).
- [ ] Every `anchor_vc_id` is in its VCG's `verses` array.
- [ ] Union of all `verses` per sub-group equals the sub-group input count (32 / 11 / 40 / 68 / 45 / 70 / 12 / 17 / 1).
- [ ] Total `verses` across the cluster = 296.
- [ ] No vc_id in two VCGs (unless dual-membership flagged).
- [ ] Every vc_id used is a real M08 is_relevant vc from the meanings report.
- [ ] M08-C has at least one VCG explicitly carrying the M22 cross-register flag (God-directed glorying register).
- [ ] M08-E has the M23 cross-register flag visible in its VCG descriptions.

CC will validate every item before applying. Failures send Phase 7 back for resubmission with a delta report.

---

## After you finish

1. Confirm pre-submission checklist passes (run §10.8 yourself).
2. Ping CC: "M08 Phase 7 VCG design ready" with the file list.
3. CC validates against the DB (§10.9), then builds the Phase 7 directive (`wa-cluster-M08-dir-003-vcg-create-v1-20260520.md`).

---

*End of brief. Load the meanings report (#2). Process sub-groups in code order. Stage write-outs.*
