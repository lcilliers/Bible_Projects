"""M04 retrofit Step 5: build VCG design AI input package (brief + structural input).

Researcher direction 2026-05-18: preserve existing VCGs in M04-A through M04-J;
for new verses, AI may ASSIGN-EXISTING-VCG (same sub-group OR another), or
CREATE-NEW-VCG. If a whole new sub-group's verses end up assigned to existing
VCGs from another sub-group, flag the new sub-group as a CONSOLIDATE-SUBGROUP
candidate.

Produces two files in Sessions/Session_Clusters/M04/:
- WA-M04-step5-vcg-design-brief-v1-{date}.md
- WA-M04-step5-vcg-design-input-v1-{date}.md

Both carry the Required-inputs declaration per feedback_ai_package_self_declaration.
"""
from __future__ import annotations
import sqlite3
from collections import defaultdict
from datetime import datetime
from pathlib import Path

DB = Path("database/bible_research.db")
TODAY = datetime.now().strftime("%Y%m%d")
BRIEF_OUT = Path(f"Sessions/Session_Clusters/M04/WA-M04-step5-vcg-design-brief-v1-{TODAY}.md")
INPUT_OUT = Path(f"Sessions/Session_Clusters/M04/WA-M04-step5-vcg-design-input-v1-{TODAY}.md")


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # All existing M04 VCGs with primary sub-group home + anchor
    vcgs = conn.execute("""
        SELECT vcg.id AS vcg_id, vcg.group_code, vcg.context_description,
               (SELECT cs.subgroup_code FROM verse_context vc2
                JOIN cluster_subgroup cs ON cs.id = vc2.cluster_subgroup_id
                JOIN mti_terms mt2 ON mt2.id = vc2.mti_term_id
                WHERE vc2.group_id = vcg.id AND mt2.cluster_code='M04'
                  AND vc2.is_relevant=1 AND COALESCE(vc2.delete_flagged,0)=0
                GROUP BY cs.subgroup_code
                ORDER BY COUNT(*) DESC LIMIT 1) AS primary_sg,
               (SELECT COUNT(*) FROM verse_context vc2
                JOIN mti_terms mt2 ON mt2.id = vc2.mti_term_id
                WHERE vc2.group_id = vcg.id AND mt2.cluster_code='M04'
                  AND vc2.is_relevant=1 AND COALESCE(vc2.delete_flagged,0)=0) AS member_count,
               (SELECT vr.reference FROM verse_context vc2
                JOIN wa_verse_records vr ON vr.id = vc2.verse_record_id
                WHERE vc2.group_id = vcg.id AND vc2.is_anchor=1
                  AND COALESCE(vc2.delete_flagged,0)=0 LIMIT 1) AS anchor_reference
        FROM verse_context_group vcg
        WHERE EXISTS (
            SELECT 1 FROM vcg_term vt
            JOIN mti_terms mt ON mt.id = vt.mti_term_id
            WHERE vt.vcg_id = vcg.id AND mt.cluster_code='M04'
              AND COALESCE(vt.delete_flagged,0)=0
        )
        AND COALESCE(vcg.delete_flagged,0)=0
          AND vcg.group_code != 'M04-BOUNDARY-VCG-01'
        ORDER BY primary_sg, vcg.group_code
    """).fetchall()

    # Sub-groups (all M04 active)
    subgroups = conn.execute("""
        SELECT id, subgroup_code, label, core_description, sort_order
        FROM cluster_subgroup
        WHERE cluster_code='M04' AND COALESCE(delete_flagged,0)=0
          AND subgroup_code != 'M04-BOUNDARY'
        ORDER BY sort_order
    """).fetchall()

    # Verses needing VCG (group_id IS NULL on is_relevant=1)
    pending = conn.execute("""
        SELECT vc.id AS vc_id, vc.mti_term_id, vc.cluster_subgroup_id,
               cs.subgroup_code,
               mt.strongs_number, mt.transliteration, mt.gloss,
               vr.reference, vr.verse_text, vr.context_before, vr.context_after,
               vc.analysis_note
        FROM verse_context vc
        JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE cs.cluster_code='M04'
          AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
          AND vc.group_id IS NULL
        ORDER BY cs.sort_order, vr.book_id, vr.chapter, vr.verse_num
    """).fetchall()

    by_sg = defaultdict(list)
    for r in pending:
        by_sg[r["subgroup_code"]].append(r)
    print(f"Total verses needing VCG assignment: {len(pending)}")
    for sg in subgroups:
        n = len(by_sg.get(sg["subgroup_code"], []))
        print(f"  {sg['subgroup_code']:18s} pending={n:4d}")

    # ----- Brief -----
    B = []
    B.append("# M04 Step 5 — VCG design for new/changed sub-groups (brief)")
    B.append("")
    B.append("**Cluster:** M04 — Joy, Gladness and Delight")
    B.append("**Phase:** 7-equivalent (VCG design, bounded scope)")
    B.append("**Task date:** 2026-05-18")
    B.append("**Audience:** Claude AI session")
    B.append("**Read this brief first.** The structural input (existing VCG catalogue + new verses per sub-group) is in a separate file.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Required inputs (load all before reading further)")
    B.append("")
    B.append("| # | Document | Purpose |")
    B.append("|---|---|---|")
    B.append(f"| 1 | **This brief** — `Sessions/Session_Clusters/M04/{BRIEF_OUT.name}` | Primary instructions — read first |")
    B.append(f"| 2 | **Structural input** — `Sessions/Session_Clusters/M04/{INPUT_OUT.name}` | Existing VCG catalogue + new verses per sub-group needing VCG assignment |")
    B.append("| 3 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_5-20260518.md` — read §10 (Phase 7 VCG design), §10.2, §10.7 staged write-out, §18 disposition vocabulary | VCG design discipline + structural rules |")
    B.append("| 4 | **Global rules** — `wa-global-general-rules` [current] | Programme-wide discipline |")
    B.append("| 5 | **Step 4 outcome** — `Sessions/Session_Clusters/M04/WA-M04-step4-boundary-resolution-applied-v1-20260518.md` | Context — which verses were promoted in Step 4 |")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Context and pre-decisions")
    B.append("")
    B.append("1. **Preserve all existing VCGs in M04-A through M04-J.** This is researcher direction 2026-05-18. The 30 existing VCGs across these sub-groups are stable and not open for redesign. Your job is to assign NEW verses (verses with `group_id = NULL`) to either an existing VCG or a new one — not to restructure the existing landscape.")
    B.append("")
    B.append("2. **6 brand-new sub-groups need full VCG design.** M04-K (Material/Sensory), M04-L (Evaluative Goodness), M04-M (Pleasing as Obedience), M04-N (Horizontal Relational), M04-O (Circumstantial Gladness), M04-P (Corrupt/Illicit Delight) were created in Step 3 for register families v2_5 §1.1 brings into inner-being scope. They have no VCGs yet. Design VCGs for them from scratch, per §10.2.")
    B.append("")
    B.append("3. **6 existing sub-groups need bounded VCG work** for newly-promoted verses only: M04-B (8 new), M04-C (16 new — all eucharistia + 1 eucharistos), M04-G (7 new), M04-H (51 new — mostly tov 'seems good' formula), M04-I (7 new), M04-J (3 new + 1 special-case 2Sa 23:1).")
    B.append("")
    B.append("4. **M04-BOUNDARY is empty.** Step 4 dispositioned all 257 BOUNDARY verses to substantive sub-groups. There is no BOUNDARY-VCG work in this step.")
    B.append("")
    B.append("5. **The 77 HOLD verses are out of scope.** They are `is_relevant=0` and you will not see them.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Your task")
    B.append("")
    B.append("For each of the **322 verses with `group_id = NULL`** in the structural input, propose exactly one disposition:")
    B.append("")
    B.append("### Disposition vocabulary")
    B.append("")
    B.append("**ASSIGN-EXISTING-VCG {group_code}** — the verse's analytical phenomenon is already named by an existing VCG. The existing VCG may be IN THE SAME sub-group OR IN ANOTHER sub-group (cross-sub-group VCG sharing is permitted under v2_5; see schema note in §A1).")
    B.append("")
    B.append("**CREATE-NEW-VCG {provisional_code} : {context_description} : anchor={reference}** — no existing VCG captures the phenomenon. Create a new VCG within the verse's current sub-group. Format:")
    B.append("- `provisional_code` follows convention `{subgroup_code}-VCG-{NN}` (e.g. `M04-K-VCG-01`). Sequential within the sub-group, starting at 01.")
    B.append("- `context_description` is a one-paragraph statement of the inner-being phenomenon the VCG names, written from the meanings.")
    B.append("- `anchor` is the reference of one verse in the new VCG that most directly evidences the phenomenon. CC will mark `is_anchor=1` on that verse.")
    B.append("")
    B.append("**Forbidden:** PARK, DEFER, HOLD, RESEARCHER-DECISION-LATER. Every vc_id must receive ASSIGN-EXISTING-VCG or CREATE-NEW-VCG.")
    B.append("")
    B.append("### Consolidation flag (per new sub-group, end of session)")
    B.append("")
    B.append("After dispositioning all verses in a brand-new sub-group (M04-K, L, M, N, O, or P), tally the results. If **most (>50%) or all of the verses end up ASSIGN-EXISTING-VCG to VCGs in another sub-group**, write a CONSOLIDATE-SUBGROUP flag at the end of that sub-group's section:")
    B.append("")
    B.append("```")
    B.append("CONSOLIDATE-SUBGROUP {sg_code} → {target_sg_code} — rationale: {N/total} verses fit existing {target_sg_code} VCGs; the new sub-group may be redundant. Researcher should review consolidation.")
    B.append("```")
    B.append("")
    B.append("This signals to the researcher that the Step 3 sub-group design may have been over-fine; the verses could be folded back into an existing sub-group. The researcher decides whether to consolidate.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Decision tree (per verse)")
    B.append("")
    B.append("1. **Read the verse text + context + Pass A meaning.**")
    B.append("2. **Review the verse's current sub-group's existing VCGs** (if any). Does the verse fit one? → ASSIGN-EXISTING-VCG to that VCG.")
    B.append("3. **If no fit in same sub-group, scan VCGs in other sub-groups.** Does the verse fit one elsewhere? → ASSIGN-EXISTING-VCG (cross-sub-group share).")
    B.append("4. **If still no fit, CREATE-NEW-VCG** within the verse's current sub-group. Designate an anchor.")
    B.append("5. **Group new-VCG creates within the same sub-group** — don't make every verse its own VCG. Look for clusters of related meanings and create a VCG covering several verses with one anchor.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Output format")
    B.append("")
    B.append("Group output by sub-group. Within each sub-group, list dispositions in canonical Bible order. Use this format per line:")
    B.append("")
    B.append("```")
    B.append("vc=<id> <DISPOSITION> <target> — <rationale, 1-2 sentences>")
    B.append("```")
    B.append("")
    B.append("For CREATE-NEW-VCG, after all verses are listed, write a VCG-definition block per new VCG:")
    B.append("")
    B.append("```")
    B.append("VCG: <provisional_code>")
    B.append("Description: <one-paragraph context_description>")
    B.append("Anchor: <reference>  (vc_id=<id>)")
    B.append("Members: vc=<id1>, vc=<id2>, vc=<id3>, ...")
    B.append("```")
    B.append("")
    B.append("### Worked examples")
    B.append("")
    B.append("Good (ASSIGN-EXISTING within same sub-group):")
    B.append("```")
    B.append("vc=18434 ASSIGN-EXISTING-VCG M04-C-VCG-03 — Act 24:3: diplomatic-public expression of gratitude as inner posture toward Felix; fits M04-C-VCG-03 'Pauline relational and community joy' register of gratitude-as-relational-orientation.")
    B.append("```")
    B.append("")
    B.append("Good (ASSIGN-EXISTING cross-sub-group):")
    B.append("```")
    B.append("vc=23418 ASSIGN-EXISTING-VCG M04-B-VCG-02 — Ezr 6:16: temple-dedication corporate joy at sacred presence; fits the existing M04-B-VCG-02 sanctuary-and-ark joy register even though the verse now sits in M04-B (it was previously in M04-C).")
    B.append("```")
    B.append("")
    B.append("Good (CREATE-NEW):")
    B.append("```")
    B.append("vc=9572 CREATE-NEW-VCG M04-P-VCG-01 — Job 20:18: wicked man's denied enjoyment of ill-gained profits; this is a 'denied/forfeit corrupt pleasure' phenomenon distinct from active illicit delight; new VCG within M04-P needed.")
    B.append("")
    B.append("VCG: M04-P-VCG-01")
    B.append("Description: Denied or forfeited corrupt pleasure — the inner experience of being deprived of ill-gotten enjoyment, framed as judgment. Job 20:18 wicked-man-denied-trading-profits; Eze 23:12 lust toward Assyrians culminating in destruction.")
    B.append("Anchor: Job 20:18  (vc_id=9572)")
    B.append("Members: vc=9572, vc=10669, ...")
    B.append("```")
    B.append("")
    B.append("Bad (rejected — too vague):")
    B.append("```")
    B.append("vc=18434 ASSIGN-EXISTING-VCG M04-C-VCG-03 — fits.")
    B.append("vc=9572 CREATE-NEW-VCG M04-P-VCG-01 — new VCG needed.")
    B.append("vc=23000 PARK — needs more thought.                ← forbidden disposition")
    B.append("```")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Discipline reminders")
    B.append("")
    B.append("1. **Existing VCG descriptions are normative.** If you assign to an existing VCG, the verse must fit that VCG's `context_description`. Don't re-interpret an existing VCG to absorb a poorly-fitting verse.")
    B.append("2. **Each new VCG must have an anchor.** The anchor is one specific verse (by reference + vc_id) that most directly evidences the phenomenon.")
    B.append("3. **Read every verse individually.** The structural input lists each verse with its full text + context + Pass A meaning. Per-verse rationale required.")
    B.append("4. **Group related verses into shared new VCGs.** Don't create one VCG per verse — look for cohesion. A new VCG with 1 member is acceptable only if no other verse fits its phenomenon.")
    B.append("5. **Cross-sub-group VCG sharing is permitted.** Don't be reluctant to assign a verse to a VCG that lives in another sub-group when the phenomenon truly matches. The sub-group is the register; the VCG is the phenomenon-within-register. Phenomena can span sub-groups.")
    B.append("6. **Consolidation flag is end-of-section only.** After dispositioning a full sub-group's verses, check: if a new sub-group's verses end up >50% in existing VCGs from another sub-group, flag for researcher consolidation review.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Suggested batching")
    B.append("")
    B.append("322 verses across 12 sub-groups is too much for a single chat session. Suggested order (smallest first; gives rhythm and lets cross-sub-group VCG familiarity build):")
    B.append("")
    B.append("| Batch | Sub-groups | Verses |")
    B.append("|---|---|---:|")
    B.append("| 1 | M04-N (5) + M04-J (3) + M04-G (7) + M04-I (7) + M04-B (8) + M04-P (9) | 39 |")
    B.append("| 2 | M04-M (16) + M04-C (16 eucharistia/eucharistos) | 32 |")
    B.append("| 3 | M04-O (50) | 50 |")
    B.append("| 4 | M04-H (51) | 51 |")
    B.append("| 5 | M04-K (67) | 67 |")
    B.append("| 6 | M04-L (83) | 83 |")
    B.append("")
    B.append("Write disposition output for each batch as you complete it. One file per batch is fine, or one big file appended across batches.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## After you finish")
    B.append("")
    B.append("1. Drop the batch output file(s) in `Sessions/Session_Clusters/M04/files vcg design/` (create the folder).")
    B.append("2. Ping CC: \"M04 Step 5 output ready: <path>\".")
    B.append("3. CC parses, validates (every existing VCG code exists; new VCG codes are unique; every new VCG has an anchor that's a member), builds + applies the bundled directive.")
    B.append("4. After Step 5: Step 6 (selective Phase 9 findings augmentation for changed sub-groups) — then STOP before Phase 10 per researcher direction.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("*End of brief. Now load the structural input file (#2 in Required inputs) and begin.*")

    BRIEF_OUT.write_text("\n".join(B), encoding="utf-8")
    print(f"\nBrief written: {BRIEF_OUT}")

    # ----- Structural input -----
    S = []
    S.append("# M04 Step 5 — VCG design structural input (existing VCG catalogue + new verses)")
    S.append("")
    S.append("**Date:** 2026-05-18")
    S.append("")
    S.append("---")
    S.append("")
    S.append("## Required inputs (read brief first)")
    S.append("")
    S.append("This is the **structural data** for M04 Step 5 — VCG design. Read **in conjunction with the brief**:")
    S.append("")
    S.append("| # | Document | Purpose |")
    S.append("|---|---|---|")
    S.append(f"| 1 | **Brief (read first)** — `Sessions/Session_Clusters/M04/{BRIEF_OUT.name}` | Primary instructions, decision vocabulary, output format, batching |")
    S.append(f"| 2 | **This document** — `Sessions/Session_Clusters/M04/{INPUT_OUT.name}` | Existing M04 VCG catalogue (30 VCGs) + 322 new verses needing assignment, grouped by sub-group |")
    S.append("| 3 | **Governing instruction** — §10 of wa-sessionb-cluster-instruction-v2_5-20260518 | VCG design discipline |")
    S.append("| 4 | **Global rules** — `wa-global-general-rules` [current] | |")
    S.append("")
    S.append("If you have not read the brief, **stop and read it first.** This document is data; the brief carries the instructions.")
    S.append("")
    S.append("---")
    S.append("")
    S.append("## §1 — Existing M04 VCG catalogue (30 VCGs) — preserve all of these")
    S.append("")
    S.append("These VCGs are stable and not open for redesign. Use them as ASSIGN-EXISTING-VCG targets (same-sub-group or cross-sub-group share).")
    S.append("")
    S.append("| group_code | Home sub-group | Members | Anchor | Description |")
    S.append("|---|---|---:|---|---|")
    for v in vcgs:
        desc = (v["context_description"] or "").replace("|", "\\|").replace("\n", " ")
        anchor = v["anchor_reference"] or "—"
        S.append(f"| `{v['group_code']}` | {v['primary_sg'] or '—'} | {v['member_count']} | {anchor} | {desc[:200]} |")
    S.append("")
    S.append("---")
    S.append("")
    S.append("## §2 — Sub-group definitions (all 16 M04 substantive sub-groups)")
    S.append("")
    for sg in subgroups:
        n_pending = len(by_sg.get(sg["subgroup_code"], []))
        n_existing_vcgs = sum(1 for v in vcgs if v["primary_sg"] == sg["subgroup_code"])
        marker = "**NEW** " if sg["subgroup_code"] in {"M04-K", "M04-L", "M04-M", "M04-N", "M04-O", "M04-P"} else ""
        S.append(f"### {marker}{sg['subgroup_code']} — {sg['label']}")
        S.append("")
        S.append(f"**core_description:** {sg['core_description']}")
        S.append("")
        S.append(f"**Existing VCGs:** {n_existing_vcgs}  |  **Verses pending VCG assignment:** {n_pending}")
        S.append("")
        S.append("---")
        S.append("")

    S.append("## §3 — Verses needing VCG assignment (per sub-group, canonical Bible order)")
    S.append("")
    for sg in subgroups:
        verses = by_sg.get(sg["subgroup_code"], [])
        if not verses:
            continue
        marker = " (NEW SUB-GROUP — full VCG design)" if sg["subgroup_code"] in {"M04-K", "M04-L", "M04-M", "M04-N", "M04-O", "M04-P"} else " (existing sub-group — assign to existing VCG or create new)"
        S.append(f"### {sg['subgroup_code']} — {sg['label']}{marker} ({len(verses)} verses)")
        S.append("")
        # List sub-group's existing VCGs for convenience (these are the within-sub-group ASSIGN targets)
        sg_vcgs = [v for v in vcgs if v["primary_sg"] == sg["subgroup_code"]]
        if sg_vcgs:
            S.append(f"**Existing VCGs in this sub-group (within-sub-group ASSIGN targets):**")
            S.append("")
            for v in sg_vcgs:
                desc = (v["context_description"] or "")[:150]
                S.append(f"- `{v['group_code']}` (anchor: {v['anchor_reference'] or '—'}, {v['member_count']} members): {desc}")
            S.append("")
        else:
            S.append("**No existing VCGs in this sub-group** — design VCG structure from scratch.")
            S.append("")

        S.append(f"**Verses to assign:**")
        S.append("")
        for v in verses:
            text = (v["verse_text"] or "").strip()
            ctx_before = (v["context_before"] or "").strip()
            ctx_after = (v["context_after"] or "").strip()
            S.append(f"#### vc={v['vc_id']} — {v['reference']} ({v['strongs_number']} {v['transliteration']})")
            S.append("")
            if ctx_before:
                S.append(f"> _… {ctx_before}_")
            S.append(f"> **{text}**")
            if ctx_after:
                S.append(f"> _{ctx_after} …_")
            S.append("")
            S.append(f"**Pass A meaning:** {v['analysis_note']}")
            S.append("")
            S.append(f"**Disposition:** _[ASSIGN-EXISTING-VCG <group_code>  /  CREATE-NEW-VCG <provisional_code>]_")
            S.append("**Rationale:** _[1-2 sentences]_")
            S.append("")
        S.append("---")
        S.append("")

    INPUT_OUT.write_text("\n".join(S), encoding="utf-8")
    print(f"Input doc written: {INPUT_OUT}")
    conn.close()


if __name__ == "__main__":
    main()
