# M04 Step 5 — VCG design for new/changed sub-groups (brief)

**Cluster:** M04 — Joy, Gladness and Delight
**Phase:** 7-equivalent (VCG design, bounded scope)
**Task date:** 2026-05-18
**Audience:** Claude AI session
**Read this brief first.** The structural input (existing VCG catalogue + new verses per sub-group) is in a separate file.

---

## Required inputs (load all before reading further)

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M04/WA-M04-step5-vcg-design-brief-v1-20260518.md` | Primary instructions — read first |
| 2 | **Structural input** — `Sessions/Session_Clusters/M04/WA-M04-step5-vcg-design-input-v1-20260518.md` | Existing VCG catalogue + new verses per sub-group needing VCG assignment |
| 3 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_5-20260518.md` — read §10 (Phase 7 VCG design), §10.2, §10.7 staged write-out, §18 disposition vocabulary | VCG design discipline + structural rules |
| 4 | **Global rules** — `wa-global-general-rules` [current] | Programme-wide discipline |
| 5 | **Step 4 outcome** — `Sessions/Session_Clusters/M04/WA-M04-step4-boundary-resolution-applied-v1-20260518.md` | Context — which verses were promoted in Step 4 |

---

## Context and pre-decisions

1. **Preserve all existing VCGs in M04-A through M04-J.** This is researcher direction 2026-05-18. The 30 existing VCGs across these sub-groups are stable and not open for redesign. Your job is to assign NEW verses (verses with `group_id = NULL`) to either an existing VCG or a new one — not to restructure the existing landscape.

2. **6 brand-new sub-groups need full VCG design.** M04-K (Material/Sensory), M04-L (Evaluative Goodness), M04-M (Pleasing as Obedience), M04-N (Horizontal Relational), M04-O (Circumstantial Gladness), M04-P (Corrupt/Illicit Delight) were created in Step 3 for register families v2_5 §1.1 brings into inner-being scope. They have no VCGs yet. Design VCGs for them from scratch, per §10.2.

3. **6 existing sub-groups need bounded VCG work** for newly-promoted verses only: M04-B (8 new), M04-C (16 new — all eucharistia + 1 eucharistos), M04-G (7 new), M04-H (51 new — mostly tov 'seems good' formula), M04-I (7 new), M04-J (3 new + 1 special-case 2Sa 23:1).

4. **M04-BOUNDARY is empty.** Step 4 dispositioned all 257 BOUNDARY verses to substantive sub-groups. There is no BOUNDARY-VCG work in this step.

5. **The 77 HOLD verses are out of scope.** They are `is_relevant=0` and you will not see them.

---

## Your task

For each of the **322 verses with `group_id = NULL`** in the structural input, propose exactly one disposition:

### Disposition vocabulary

**ASSIGN-EXISTING-VCG {group_code}** — the verse's analytical phenomenon is already named by an existing VCG. The existing VCG may be IN THE SAME sub-group OR IN ANOTHER sub-group (cross-sub-group VCG sharing is permitted under v2_5; see schema note in §A1).

**CREATE-NEW-VCG {provisional_code} : {context_description} : anchor={reference}** — no existing VCG captures the phenomenon. Create a new VCG within the verse's current sub-group. Format:
- `provisional_code` follows convention `{subgroup_code}-VCG-{NN}` (e.g. `M04-K-VCG-01`). Sequential within the sub-group, starting at 01.
- `context_description` is a one-paragraph statement of the inner-being phenomenon the VCG names, written from the meanings.
- `anchor` is the reference of one verse in the new VCG that most directly evidences the phenomenon. CC will mark `is_anchor=1` on that verse.

**Forbidden:** PARK, DEFER, HOLD, RESEARCHER-DECISION-LATER. Every vc_id must receive ASSIGN-EXISTING-VCG or CREATE-NEW-VCG.

### Consolidation flag (per new sub-group, end of session)

After dispositioning all verses in a brand-new sub-group (M04-K, L, M, N, O, or P), tally the results. If **most (>50%) or all of the verses end up ASSIGN-EXISTING-VCG to VCGs in another sub-group**, write a CONSOLIDATE-SUBGROUP flag at the end of that sub-group's section:

```
CONSOLIDATE-SUBGROUP {sg_code} → {target_sg_code} — rationale: {N/total} verses fit existing {target_sg_code} VCGs; the new sub-group may be redundant. Researcher should review consolidation.
```

This signals to the researcher that the Step 3 sub-group design may have been over-fine; the verses could be folded back into an existing sub-group. The researcher decides whether to consolidate.

---

## Decision tree (per verse)

1. **Read the verse text + context + Pass A meaning.**
2. **Review the verse's current sub-group's existing VCGs** (if any). Does the verse fit one? → ASSIGN-EXISTING-VCG to that VCG.
3. **If no fit in same sub-group, scan VCGs in other sub-groups.** Does the verse fit one elsewhere? → ASSIGN-EXISTING-VCG (cross-sub-group share).
4. **If still no fit, CREATE-NEW-VCG** within the verse's current sub-group. Designate an anchor.
5. **Group new-VCG creates within the same sub-group** — don't make every verse its own VCG. Look for clusters of related meanings and create a VCG covering several verses with one anchor.

---

## Output format

Group output by sub-group. Within each sub-group, list dispositions in canonical Bible order. Use this format per line:

```
vc=<id> <DISPOSITION> <target> — <rationale, 1-2 sentences>
```

For CREATE-NEW-VCG, after all verses are listed, write a VCG-definition block per new VCG:

```
VCG: <provisional_code>
Description: <one-paragraph context_description>
Anchor: <reference>  (vc_id=<id>)
Members: vc=<id1>, vc=<id2>, vc=<id3>, ...
```

### Worked examples

Good (ASSIGN-EXISTING within same sub-group):
```
vc=18434 ASSIGN-EXISTING-VCG M04-C-VCG-03 — Act 24:3: diplomatic-public expression of gratitude as inner posture toward Felix; fits M04-C-VCG-03 'Pauline relational and community joy' register of gratitude-as-relational-orientation.
```

Good (ASSIGN-EXISTING cross-sub-group):
```
vc=23418 ASSIGN-EXISTING-VCG M04-B-VCG-02 — Ezr 6:16: temple-dedication corporate joy at sacred presence; fits the existing M04-B-VCG-02 sanctuary-and-ark joy register even though the verse now sits in M04-B (it was previously in M04-C).
```

Good (CREATE-NEW):
```
vc=9572 CREATE-NEW-VCG M04-P-VCG-01 — Job 20:18: wicked man's denied enjoyment of ill-gained profits; this is a 'denied/forfeit corrupt pleasure' phenomenon distinct from active illicit delight; new VCG within M04-P needed.

VCG: M04-P-VCG-01
Description: Denied or forfeited corrupt pleasure — the inner experience of being deprived of ill-gotten enjoyment, framed as judgment. Job 20:18 wicked-man-denied-trading-profits; Eze 23:12 lust toward Assyrians culminating in destruction.
Anchor: Job 20:18  (vc_id=9572)
Members: vc=9572, vc=10669, ...
```

Bad (rejected — too vague):
```
vc=18434 ASSIGN-EXISTING-VCG M04-C-VCG-03 — fits.
vc=9572 CREATE-NEW-VCG M04-P-VCG-01 — new VCG needed.
vc=23000 PARK — needs more thought.                ← forbidden disposition
```

---

## Discipline reminders

1. **Existing VCG descriptions are normative.** If you assign to an existing VCG, the verse must fit that VCG's `context_description`. Don't re-interpret an existing VCG to absorb a poorly-fitting verse.
2. **Each new VCG must have an anchor.** The anchor is one specific verse (by reference + vc_id) that most directly evidences the phenomenon.
3. **Read every verse individually.** The structural input lists each verse with its full text + context + Pass A meaning. Per-verse rationale required.
4. **Group related verses into shared new VCGs.** Don't create one VCG per verse — look for cohesion. A new VCG with 1 member is acceptable only if no other verse fits its phenomenon.
5. **Cross-sub-group VCG sharing is permitted.** Don't be reluctant to assign a verse to a VCG that lives in another sub-group when the phenomenon truly matches. The sub-group is the register; the VCG is the phenomenon-within-register. Phenomena can span sub-groups.
6. **Consolidation flag is end-of-section only.** After dispositioning a full sub-group's verses, check: if a new sub-group's verses end up >50% in existing VCGs from another sub-group, flag for researcher consolidation review.

---

## Suggested batching

322 verses across 12 sub-groups is too much for a single chat session. Suggested order (smallest first; gives rhythm and lets cross-sub-group VCG familiarity build):

| Batch | Sub-groups | Verses |
|---|---|---:|
| 1 | M04-N (5) + M04-J (3) + M04-G (7) + M04-I (7) + M04-B (8) + M04-P (9) | 39 |
| 2 | M04-M (16) + M04-C (16 eucharistia/eucharistos) | 32 |
| 3 | M04-O (50) | 50 |
| 4 | M04-H (51) | 51 |
| 5 | M04-K (67) | 67 |
| 6 | M04-L (83) | 83 |

Write disposition output for each batch as you complete it. One file per batch is fine, or one big file appended across batches.

---

## After you finish

1. Drop the batch output file(s) in `Sessions/Session_Clusters/M04/files vcg design/` (create the folder).
2. Ping CC: "M04 Step 5 output ready: <path>".
3. CC parses, validates (every existing VCG code exists; new VCG codes are unique; every new VCG has an anchor that's a member), builds + applies the bundled directive.
4. After Step 5: Step 6 (selective Phase 9 findings augmentation for changed sub-groups) — then STOP before Phase 10 per researcher direction.

---

*End of brief. Now load the structural input file (#2 in Required inputs) and begin.*