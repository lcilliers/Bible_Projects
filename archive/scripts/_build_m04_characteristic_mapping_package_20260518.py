"""Build the M04 characteristic-mapping AI package (brief + structural input).

Per researcher direction 2026-05-18: M04 has 16 sub-groups; multiple sub-groups
can map to ONE characteristic. Task — examine the 16 sub-groups and ask:
- How many distinct characteristics does M04 represent?
- Which sub-groups map to each characteristic?
- Are any of the 16 sub-groups sub-components-split-for-size of the SAME
  characteristic (in which case they share a characteristic), or are they
  genuinely distinct characteristics?

After AI returns the characteristic map, the 189-question Phase 9 sweep runs
per characteristic (across its sub-groups), not per sub-group individually.

Outputs:
- Sessions/Session_Clusters/M04/WA-M04-characteristic-mapping-brief-v1-{date}.md
- Sessions/Session_Clusters/M04/WA-M04-characteristic-mapping-input-v1-{date}.md
"""
from __future__ import annotations
import sqlite3
from datetime import datetime
from pathlib import Path

DB = Path("database/bible_research.db")
TODAY = datetime.now().strftime("%Y%m%d")
BRIEF = Path(f"Sessions/Session_Clusters/M04/WA-M04-characteristic-mapping-brief-v1-{TODAY}.md")
INPUT = Path(f"Sessions/Session_Clusters/M04/WA-M04-characteristic-mapping-input-v1-{TODAY}.md")


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    cluster = conn.execute(
        "SELECT cluster_code, description, gloss, short_name FROM cluster WHERE cluster_code='M04'"
    ).fetchone()

    subgroups = conn.execute(
        """
        SELECT cs.subgroup_code, cs.label, cs.core_description,
               SUM(CASE WHEN vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0 THEN 1 ELSE 0 END) AS rel,
               (SELECT COUNT(DISTINCT vc2.mti_term_id) FROM verse_context vc2
                WHERE vc2.cluster_subgroup_id=cs.id AND vc2.is_relevant=1
                AND COALESCE(vc2.delete_flagged,0)=0) AS term_count
        FROM cluster_subgroup cs
        LEFT JOIN verse_context vc ON vc.cluster_subgroup_id = cs.id
        WHERE cs.cluster_code='M04' AND COALESCE(cs.delete_flagged,0)=0
          AND cs.subgroup_code != 'M04-BOUNDARY'
        GROUP BY cs.id ORDER BY cs.sort_order
        """
    ).fetchall()

    # ----- Brief -----
    B = []
    B.append("# M04 characteristic mapping — brief")
    B.append("")
    B.append(f"**Cluster:** M04 — {cluster['description']}")
    B.append("**Task date:** 2026-05-18")
    B.append("**Audience:** Claude AI session")
    B.append("**Read this brief first.** Structural input is in a separate file referenced below.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Required inputs")
    B.append("")
    B.append("| # | Document | Purpose |")
    B.append("|---|---|---|")
    B.append(f"| 1 | **This brief** — `Sessions/Session_Clusters/M04/{BRIEF.name}` | Primary task instructions |")
    B.append(f"| 2 | **Structural input** — `Sessions/Session_Clusters/M04/{INPUT.name}` | M04 cluster description + 16 sub-groups (code, label, core_description, verse count, term count) |")
    B.append("| 3 | **Programme prose extract** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260506.md` Chapter 1 'Defining Inner Being' | The canonical definition of an inner-being characteristic |")
    B.append("| 4 | **Structural-terms clarification** — `Workflow/methodology/WA-structural-terms-clarification-v1-20260518.md` | The corrected hierarchy: characteristic → registry → term → cluster → sub-group → VCG → tier |")
    B.append("| 5 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Context")
    B.append("")
    B.append("M04 (Joy, Gladness and Delight) has 16 substantive sub-groups. Per the programme's working definition, an inner-being characteristic is:")
    B.append("")
    B.append("> *\"the non-physical, internal states, capacities, and expressions that constitute a person's invisible life — encompassing how a person thinks, feels, chooses, relates, and orients themselves toward meaning, others, and God.\"*")
    B.append("")
    B.append("Under the corrected hierarchy:")
    B.append("")
    B.append("- A **cluster** groups *similar characteristics* for joint analysis.")
    B.append("- A **sub-group** within a cluster represents *a characteristic, or a sub-component of a characteristic*.")
    B.append("- Sub-groups may be split for verse-volume reasons; in that case, **multiple sub-groups can map to ONE characteristic**.")
    B.append("- The 189 Tier prompts apply per **characteristic** (across whatever sub-groups form it), not per sub-group individually.")
    B.append("")
    B.append("Your task is to examine M04's 16 sub-groups and map them onto distinct characteristics.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Your task")
    B.append("")
    B.append("For each of the 16 M04 sub-groups in the structural input, decide:")
    B.append("")
    B.append("- Does this sub-group represent **a distinct characteristic** in its own right?")
    B.append("- OR does it share a characteristic with one or more other M04 sub-groups (i.e., it is a sub-component, split for verse-volume reasons)?")
    B.append("")
    B.append("Then produce a **characteristic map** for M04:")
    B.append("")
    B.append("```")
    B.append("Characteristic 1 — <short name> — <one-paragraph definition tied to the inner-being scope>")
    B.append("  Sub-groups: M04-X, M04-Y, ...")
    B.append("  Rationale: why these sub-groups share this characteristic (and not others)")
    B.append("")
    B.append("Characteristic 2 — <short name> — <one-paragraph definition>")
    B.append("  Sub-groups: M04-Z")
    B.append("  Rationale: ...")
    B.append("")
    B.append("...")
    B.append("```")
    B.append("")
    B.append("Each sub-group appears in exactly one characteristic. Every sub-group must be mapped (none left out).")
    B.append("")
    B.append("### Quality expectations")
    B.append("")
    B.append("1. **Each characteristic must be a true inner-being phenomenon** per the working definition — not just a register or stylistic variant. \"Joy directed toward God\" is a characteristic; \"morning joy versus evening joy\" is not. Test: can you state the characteristic as a distinct inner-being state/capacity/expression?")
    B.append("2. **Sub-groups grouped under one characteristic must share the same analytical phenomenon**, differing only by verse-volume / corpus-section / register-of-expression. If they differ in WHAT inner-being phenomenon they evidence, they're distinct characteristics.")
    B.append("3. **Cite specific sub-group features** in your rationale — quote from `core_description` to show why a grouping holds.")
    B.append("4. **Default to keeping sub-groups distinct.** Only group two or more sub-groups into one characteristic when the evidence forces it. The bias should be toward distinct characteristics; consolidation requires positive evidence of sub-component status.")
    B.append("5. **No more than ~10 characteristics for M04 likely**, but no upper or lower cap — let the analysis drive the count.")
    B.append("")
    B.append("### Anti-patterns to avoid")
    B.append("")
    B.append("- Don't group sub-groups together just because they share a Hebrew/Greek term family. Term overlap does not imply characteristic identity.")
    B.append("- Don't group sub-groups together just because they are in the same testament or have similar verse counts.")
    B.append("- Don't propose hyper-fine characteristics like \"Joy at sunrise\" — characteristics are analytical phenomena, not narrative details.")
    B.append("- Don't propose characteristics that don't match the inner-being-scope definition — every characteristic must be a non-physical internal state/capacity/expression.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Output format")
    B.append("")
    B.append("Write the characteristic map as a markdown document. Use this structure:")
    B.append("")
    B.append("```markdown")
    B.append("# M04 characteristic map — proposed")
    B.append("")
    B.append("## Summary")
    B.append("")
    B.append("M04 represents N distinct inner-being characteristics, mapped across the 16 sub-groups as below.")
    B.append("")
    B.append("## Characteristic 1 — <short name>")
    B.append("")
    B.append("**Definition:** <one paragraph tying the characteristic to the inner-being working definition>")
    B.append("")
    B.append("**Sub-groups in this characteristic:** M04-X, M04-Y, M04-Z")
    B.append("")
    B.append("**Rationale:** <why these sub-groups share this characteristic — cite specific phrases from core_descriptions; explain whether grouping is for verse-volume reasons or analytical kinship>")
    B.append("")
    B.append("## Characteristic 2 — ...")
    B.append("```")
    B.append("")
    B.append("Then at the end:")
    B.append("")
    B.append("```markdown")
    B.append("## Cross-check")
    B.append("")
    B.append("All 16 sub-groups accounted for:")
    B.append("- M04-A → Characteristic <n>")
    B.append("- M04-B → Characteristic <n>")
    B.append("- ...")
    B.append("- M04-P → Characteristic <n>")
    B.append("")
    B.append("## Observations and open questions")
    B.append("")
    B.append("- <any sub-groups where the mapping is ambiguous and needs researcher decision>")
    B.append("- <any sub-groups that don't fit the M04 cluster analytically (rare)>")
    B.append("```")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## After you finish")
    B.append("")
    B.append("1. Drop the output in `Sessions/Session_Clusters/M04/` as `WA-M04-characteristic-map-v1-20260518.md`.")
    B.append("2. Ping CC: \"M04 characteristic map ready: <path>\".")
    B.append("3. CC presents the map to researcher for review.")
    B.append("4. If approved, the map drives Phase 9: the 189 prompts run per characteristic (across its sub-groups), not per sub-group individually.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("*End of brief. Now load the structural input (#2 in Required inputs) and begin.*")

    BRIEF.write_text("\n".join(B), encoding="utf-8")

    # ----- Structural input -----
    S = []
    S.append("# M04 characteristic mapping — structural input")
    S.append("")
    S.append("**Date:** 2026-05-18")
    S.append("")
    S.append("---")
    S.append("")
    S.append("## Required inputs (read brief first)")
    S.append("")
    S.append("| # | Document | Purpose |")
    S.append("|---|---|---|")
    S.append(f"| 1 | **Brief (read first)** — `Sessions/Session_Clusters/M04/{BRIEF.name}` | Primary task instructions |")
    S.append(f"| 2 | **This document** — `Sessions/Session_Clusters/M04/{INPUT.name}` | M04 cluster description + 16 sub-groups with core_descriptions |")
    S.append("| 3 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260506.md` Ch.1 'Defining Inner Being' | Canonical characteristic definition |")
    S.append("| 4 | **Structural-terms clarification** — `Workflow/methodology/WA-structural-terms-clarification-v1-20260518.md` | Corrected hierarchy |")
    S.append("")
    S.append("---")
    S.append("")
    S.append("## §1 — M04 cluster description")
    S.append("")
    S.append(f"**Cluster code:** {cluster['cluster_code']}")
    S.append(f"**Short name:** {cluster['short_name']}")
    S.append(f"**Description:** {cluster['description']}")
    S.append("")
    S.append("**Gloss (term overview):**")
    S.append("")
    S.append(f"> {cluster['gloss']}")
    S.append("")
    S.append("---")
    S.append("")
    S.append("## §2 — The 16 substantive sub-groups")
    S.append("")
    S.append("Each sub-group is listed with its code, label, current verse count, term count, and `core_description`. Decide for each whether it is a distinct characteristic or shares a characteristic with one or more others.")
    S.append("")
    for sg in subgroups:
        S.append(f"### {sg['subgroup_code']} — {sg['label']}")
        S.append("")
        S.append(f"**Verses:** {sg['rel'] or 0}  |  **Distinct terms:** {sg['term_count'] or 0}")
        S.append("")
        S.append(f"**core_description:**")
        S.append("")
        S.append(f"> {sg['core_description']}")
        S.append("")
        S.append("---")
        S.append("")

    S.append("## §3 — Summary table")
    S.append("")
    S.append("| Sub-group | Label | Verses | Terms |")
    S.append("|---|---|---:|---:|")
    for sg in subgroups:
        S.append(f"| {sg['subgroup_code']} | {sg['label']} | {sg['rel'] or 0} | {sg['term_count'] or 0} |")
    S.append("")
    S.append(f"**Total:** {len(subgroups)} sub-groups, {sum(sg['rel'] or 0 for sg in subgroups)} relevant verses")
    S.append("")
    S.append("---")
    S.append("")
    S.append("*End of structural input.*")

    INPUT.write_text("\n".join(S), encoding="utf-8")
    print(f"Brief: {BRIEF}")
    print(f"Input: {INPUT}")
    conn.close()


if __name__ == "__main__":
    main()
