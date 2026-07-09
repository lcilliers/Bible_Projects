"""Build a per-characteristic Phase 9 AI package for M10.

Per researcher direction 2026-05-18: Phase 9 findings authored at
CHARACTERISTIC scope (not sub-group). Each AI session works through the
189-prompt catalogue for ONE characteristic, citing evidence from the
characteristic's constituent sub-groups + their VCGs + member verses.

Usage:
    python scripts/_build_m10_characteristic_phase9_package_20260523.py --char-seq 1
    python scripts/_build_m10_characteristic_phase9_package_20260523.py --char-seq 2
    ...

Outputs (per characteristic):
    Sessions/Session_Clusters/M10/wa-cluster-M10-phase9-char{N}-{short_name}-brief-v1-{date}.md
    Sessions/Session_Clusters/M10/wa-cluster-M10-phase9-char{N}-{short_name}-input-v1-{date}.md
"""
from __future__ import annotations
import argparse
import sqlite3
from collections import defaultdict
from datetime import datetime
from pathlib import Path

DB = Path("database/bible_research.db")
TODAY = datetime.now().strftime("%Y%m%d")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--char-seq", type=int, required=True, help="Characteristic sequence number (1-22 for M10)")
    args = ap.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # Get the characteristic
    char = conn.execute(
        "SELECT * FROM characteristic WHERE cluster_code='M10' AND char_seq=? AND COALESCE(delete_flagged,0)=0",
        (args.char_seq,),
    ).fetchone()
    if not char:
        raise SystemExit(f"No M10 characteristic with seq={args.char_seq}")

    short = char["short_name"]
    safe_short = short.replace(" ", "-").replace("/", "-")

    # Sub-groups linked to this characteristic
    subgroups = conn.execute(
        """
        SELECT cs.id AS sg_id, cs.subgroup_code, cs.label, cs.core_description,
               chs.qualifier_note, chs.is_partial, chs.partial_register_note,
               (SELECT COUNT(*) FROM verse_context vc
                WHERE vc.cluster_subgroup_id = cs.id AND vc.is_relevant = 1
                AND COALESCE(vc.delete_flagged, 0) = 0) AS verse_count
        FROM characteristic_subgroup chs
        JOIN cluster_subgroup cs ON cs.id = chs.cluster_subgroup_id
        WHERE chs.characteristic_id = ? AND COALESCE(chs.delete_flagged, 0) = 0
        ORDER BY cs.sort_order
        """,
        (char["id"],),
    ).fetchall()

    # Carry-forward observations targeting Phase 9 for this characteristic (or unscoped at cluster level)
    observations = conn.execute(
        """
        SELECT id, observation_type, title, description, target_phase, status,
               characteristic_id, cluster_subgroup_id
        FROM cluster_observation
        WHERE cluster_code='M10'
          AND target_phase='phase_9_findings'
          AND status='open'
          AND COALESCE(delete_flagged, 0) = 0
          AND (characteristic_id = ? OR characteristic_id IS NULL)
        ORDER BY id
        """,
        (char["id"],),
    ).fetchall()

    # 189-prompt catalogue grouped by tier
    prompts = conn.execute(
        """
        SELECT obs_id, question_code, question_text, tier, component_code, component_title
        FROM wa_obs_question_catalogue
        WHERE tier IN ('T0','T1','T2','T3','T4','T5','T6','T7')
          AND COALESCE(deleted, 0) = 0
        ORDER BY tier, component_code, prompt_seq
        """
    ).fetchall()
    by_tier = defaultdict(list)
    for p in prompts:
        by_tier[p["tier"]].append(p)

    # Verses per sub-group with Pass A meanings + VCG placement
    verses_by_sg = defaultdict(list)
    for sg in subgroups:
        # If sub-group is "partial" (M04-E case), filter by VCG so we only get this characteristic's register
        # For v1 of this package, we include ALL of M04-E's verses but flag the split in the brief.
        # Researcher / AI will use the VCG context_description to distinguish registers.
        vs = conn.execute(
            """
            SELECT vc.id AS vc_id, vc.group_id, mt.strongs_number, mt.transliteration,
                   vr.reference, vr.verse_text, vr.context_before, vr.context_after,
                   vc.analysis_note,
                   vcg.group_code AS vcg_code, vcg.context_description AS vcg_desc
            FROM verse_context vc
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
            LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id
            WHERE vc.cluster_subgroup_id = ? AND vc.is_relevant = 1
              AND COALESCE(vc.delete_flagged, 0) = 0
            ORDER BY vr.book_id, vr.chapter, vr.verse_num
            """,
            (sg["sg_id"],),
        ).fetchall()
        verses_by_sg[sg["subgroup_code"]] = [dict(v) for v in vs]

    # Cluster meta
    cluster = conn.execute(
        "SELECT description, gloss FROM cluster WHERE cluster_code='M10'"
    ).fetchone()

    # ===== File paths =====
    BRIEF = Path(f"Sessions/Session_Clusters/M10/wa-cluster-M10-phase9-char{args.char_seq}-{safe_short}-brief-v1-{TODAY}.md")
    INPUT = Path(f"Sessions/Session_Clusters/M10/wa-cluster-M10-phase9-char{args.char_seq}-{safe_short}-input-v1-{TODAY}.md")

    total_verses = sum(sg["verse_count"] or 0 for sg in subgroups)

    # ===== Brief =====
    B = []
    B.append(f"# M10 Phase 9 — Characteristic {args.char_seq} ({short}) — brief")
    B.append("")
    B.append(f"**Cluster:** M10 — {cluster['description']}")
    B.append(f"**Characteristic:** {args.char_seq} — {short}")
    B.append(f"**Verses in scope:** ~{total_verses} across {len(subgroups)} sub-group(s)")
    B.append(f"**Task date:** {datetime.now().strftime('%Y-%m-%d')}")
    B.append(f"**Audience:** Claude AI session")
    B.append("")
    B.append("**Read this brief first.** Structural input is in a separate file referenced below.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Required inputs")
    B.append("")
    B.append("| # | Document | Purpose |")
    B.append("|---|---|---|")
    B.append(f"| 1 | **This brief** — `Sessions/Session_Clusters/M10/{BRIEF.name}` | Primary task instructions |")
    B.append(f"| 2 | **Structural input** — `Sessions/Session_Clusters/M10/{INPUT.name}` | Characteristic definition + sub-groups + VCGs + verses + 189 prompts + carry-forward observations |")
    B.append("| 3 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` | §12 Phase 9 disciplines; §12.4 parser-safe form |")
    B.append("| 4 | **Science extract** — `Workflow/Sciences/wa-m10-guilt-scienceextract-v1_0-20260513.md` | Programme-curated scientific lens for T7.3 (human science framework) prompts — ensures consistent framing across clusters and reviewers |")
    B.append("| 5 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260506.md` Ch.1 'Defining Inner Being' | Inner-being scope definition (background) |")
    B.append("| 6 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |")
    B.append("")
    B.append("> The full 189-prompt T0–T7 catalogue is reproduced inside the structural input (§4). No separate catalogue file required.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Context")
    B.append("")
    B.append(f"M10 has 22 inner-being characteristics. You are processing **Characteristic {args.char_seq} ({short})**. Per researcher direction 2026-05-18 (carried forward to M10 under v2_8 §8.0):")
    B.append("")
    B.append("> *\"sub groups is purely a capacity organiser, the evaluating unit is the characteristic or group of sub groups.\"*")
    B.append("")
    B.append("All your findings author at **characteristic scope** — NOT at sub-group scope. Sub-groups organise the evidence for navigation; they don't carry the analytical unit.")
    B.append("")
    B.append("Cluster-scope synthesis (across all 6 characteristics) happens in a separate session at the end. **Don't author cluster-scope findings here.**")
    B.append("")
    B.append("---")
    B.append("")
    B.append(f"## Characteristic {args.char_seq} — {short}: definition")
    B.append("")
    B.append(f"> {char['definition']}")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Your task")
    B.append("")
    B.append(f"For each of the **189 catalogue prompts** (8 tiers, T0–T7), author a finding at characteristic scope for Characteristic {args.char_seq} ({short}). Use the verse evidence in the structural input.")
    B.append("")
    B.append("Output format per prompt (one block per prompt; parser-safe form per v2_8 §12.4):")
    B.append("")
    B.append("```")
    B.append("**T#.#.# — question text excerpt (optional)**")
    B.append("")
    B.append(f"**[CHAR-{args.char_seq}]** E — Finding text. Cite specific verses / VCGs / sub-groups from the evidence in §3 of the structural input. Quote the specific verse phrases that evidence the answer. The finding must be self-contained for a Session C reader.")
    B.append("")
    B.append("---")
    B.append("```")
    B.append("")
    B.append("Outcome codes:")
    B.append("")
    B.append("- **E** — evidenced; cite specific verses / VCGs")
    B.append("- **S** — silent; describe the analytical significance of the absence")
    B.append("- **G** — gap; describe what data would be needed to answer")
    B.append("")
    B.append(f"Scope marker is `**[CHAR-{args.char_seq}]**` (CC's loader maps this to characteristic_id={char['id']} for this characteristic).")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## ⚠️ TIER-BY-TIER STAGED EXECUTION — MANDATORY ⚠️")
    B.append("")
    B.append("**Known prior failure mode (M04 / M07, and the first M07 / M08 attempts):** AI held all 189 prompts in working memory and produced them as a continuous pass. It drifted — carried prior-tier reasoning into later tiers, skipped prompts \"to come back later\", performed inter-tier analysis, and produced fluency-without-citation. **Do not repeat that pattern.**")
    B.append("")
    B.append(f"This task is **8 segments**, one per tier. Each segment must be **authored, written to disk, self-evaluated, and only then proceed to the next tier**. **One tier per response.**")
    B.append("")
    B.append("### Hard procedural sequence (per tier)")
    B.append("")
    B.append("For each of T0 → T1 → T2 → T3 → T4 → T5 → T6 → T7, in order, you MUST:")
    B.append("")
    B.append("1. **OPEN TIER** — announce: *\"Starting Tier T{N} — {tier title}.\"*")
    B.append("2. **READ EVIDENCE FRESH** — re-read §3 of the structural input (the verse-meanings). Do not rely on memorised summaries from prior tiers; re-read for the current tier's lens.")
    B.append("3. **AUTHOR THIS TIER'S PROMPTS** — every prompt in the tier gets one finding block (parser-safe form above). Tier sizes: **T0=12, T1=24, T2=31, T3=33, T4=24, T5=21, T6=24, T7=20.** No skipping. No \"summarise the rest\".")
    B.append("4. **WRITE TO DISK** — emit the tier's complete section as a single contiguous markdown block (with the `## T{N} — {title}` header and all prompt blocks below it). On the first tier this CREATES the findings file; on subsequent tiers it APPENDS to it. Show the file path in the output so the reader can append manually if needed.")
    B.append("5. **SELF-EVALUATE the tier** — run the self-evaluation gate (see below) before announcing the tier complete.")
    B.append("6. **CONFIRM + PROCEED (or ALERT)** —")
    B.append(f"   - If self-evaluation passes: announce *\"Tier T{{N}} written: {{file_path}}, {{n}}/{{n}} prompts, [CHAR-{args.char_seq}] markers verified, self-evaluation PASS. Proceeding to Tier T{{N+1}}.\"* — then immediately begin Tier T{{N+1}} in the SAME response (re-read §3 fresh; start from step 1).")
    B.append("   - If self-evaluation fails or surfaces a researcher-review item: announce *\"Tier T{N} written but self-evaluation surfaced: {issue}. ALERT — pausing for researcher review.\"* — then STOP. Do not begin the next tier; wait for the next prompt.")
    B.append("")
    B.append("**Between tiers, your working memory must reset.** Do not carry T{N}'s reasoning or finding patterns into T{N+1}'s prompts. The next tier starts fresh from the verse evidence, with the next tier's analytical lens.")
    B.append("")
    B.append("### Self-evaluation gate (run after every tier)")
    B.append("")
    B.append("Quickly check these items. If all pass, proceed to the next tier in the same response. If any fail, ALERT and stop.")
    B.append("")
    B.append("| # | Check | PASS criterion | If FAIL |")
    B.append("|---|---|---|---|")
    B.append("| 1 | **Prompt count** | Every prompt in the tier has a finding block (T0=12, T1=24, T2=31, T3=33, T4=24, T5=21, T6=24, T7=20) | ALERT — name the missing prompts |")
    B.append(f"| 2 | **Scope marker** | Every `[CHAR-N]` marker in this tier is `[CHAR-{args.char_seq}]` | ALERT — name the wrong-marker prompts |")
    B.append("| 3 | **Citation discipline** | Every E finding cites at least one verse-reference or VCG code (e.g. `Pro 16:5`, `M10-J-VCG-01`) | ALERT — name the uncited E prompts; do NOT proceed |")
    B.append("| 4 | **No cross-tier mixing** | This tier's findings do not reference findings from a later tier (e.g. \"see T7\" before T7 is authored) | ALERT — name the cross-tier references |")
    B.append("| 5 | **Distinct evidence per prompt** | No two prompts share an identical 80-character opening (a bulk-classification signal) | ALERT — name the prompts with shared openings |")
    B.append("| 6 | **Verse-corpus validity** | Verse references look like they belong to this characteristic's evidence corpus (cross-check from §3 of the input; if you cited a verse not in §3, flag it) | ALERT — name the phantom-ref prompts |")
    B.append("")
    B.append("Document the self-evaluation result inline at the end of the tier block — one sentence per check, PASS or FAIL. If everything passes, the next tier follows immediately in the same response.")
    B.append("")
    B.append("### What NOT to do (each is a drift signal)")
    B.append("")
    B.append("- Authoring prompts from a tier you have not announced as OPEN")
    B.append("- Holding multiple tiers' worth of unwritten findings in your response (the file write is per-tier, even though tiers can chain in one response)")
    B.append("- Skipping prompts \"to come back later\" — every prompt in a tier is answered before the tier's self-evaluation")
    B.append("- Cross-tier analysis or summary while a tier is in flight (e.g. *\"now that I see T2, I notice T1 should have said…\"*) — cross-tier patterns belong in the **final** Self-check after T7")
    B.append("- Substituting fluency for citation — every E must name verses / VCGs from §3")
    B.append("- Bulk-classifying multiple prompts with the same evidence pattern from a sample — each prompt is its own analytical pass")
    B.append("")
    B.append("### Recovery if drift surfaces mid-tier")
    B.append("")
    B.append("If during a tier you notice you have skipped prompts, mixed scope markers, or carried analysis from another tier in: **STOP**, announce the issue, abandon the half-written tier, and restart that tier from scratch (re-read §3, re-author from the first prompt). It is faster to restart a tier cleanly than to patch a contaminated one.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Discipline (per v2_8 §12)")
    B.append("")
    B.append("1. **One tier per response.** See the staged execution protocol above. The STOP gate is structural — it's how you avoid the prior-failure mode.")
    B.append("2. **Read every verse-meaning in the structural input** at the start of each tier. No sampling. The Pass A meanings condense each verse's inner-being content — read them all.")
    B.append("3. **Per prompt, ground in specific evidence.** Every E finding names verses, VCGs, or sub-groups. The test for a good answer is *can I name what evidences this?*")
    B.append("4. **Fluency is not a quality signal** (v2_8 §2.4). Plausible-sounding text without specific citations is rejected.")
    B.append("5. **No sub-group-scope findings.** All findings at characteristic scope. Where evidence differs by sub-group within the characteristic (e.g. CHAR-1 spans multiple sub-groups), the finding text names the sub-group(s) inline.")
    B.append("6. **No cluster-scope findings.** Cluster synthesis runs after all 6 characteristics finish.")
    B.append("7. **No inter-tier analysis** while a tier is in flight. Reserve cross-tier observations for the Self-check at the end.")
    B.append("8. **Self-check at the end** — after T7 is written, in a separate response, post the self-check block (counts + carry-forward observations addressed + unexpected patterns).")
    B.append("")
    B.append("---")
    B.append("")
    if observations:
        B.append("## Carry-forward observations (apply to this characteristic)")
        B.append("")
        B.append("These analytical hints were raised at characteristic-mapping time and are queued for Phase 9 attention:")
        B.append("")
        for o in observations:
            B.append(f"### {o['observation_type']} — {o['title']}")
            B.append("")
            B.append(f"> {o['description']}")
            B.append("")
            B.append("**At Phase 9 end:** flag whether this observation surfaced in the findings as expected; mark in your final summary so CC can update status open → confirmed/refined.")
            B.append("")
        B.append("---")
        B.append("")
    else:
        B.append("## Carry-forward observations")
        B.append("")
        B.append("No carry-forward observations are linked to this specific characteristic. If you surface unexpected analytical patterns during the 189-prompt pass, write them in the final summary so CC can record them as new cluster_observation rows.")
        B.append("")
        B.append("---")
        B.append("")
    B.append("## Output structure — built incrementally, tier-by-tier")
    B.append("")
    B.append(f"Target filename: `Sessions/Session_Clusters/M10/wa-cluster-M10-phase9-char{args.char_seq}-{safe_short}-findings-v1-{TODAY}.md`")
    B.append("")
    B.append("The file is built tier-by-tier. **Tier 0 (T0) creates the file with the header + T0 section. Each subsequent tier appends its `## T{N} — …` section.** Tiers chain automatically when self-evaluation passes; ALERT and stop only when self-evaluation surfaces an issue. At the end, after T7's self-evaluation passes, write the final Self-check block.")
    B.append("")
    B.append("### Tier 0 (first response) — file header + T0 section + self-eval + (proceed to T1)")
    B.append("")
    B.append("```markdown")
    B.append(f"# M10 Phase 9 — Characteristic {args.char_seq} ({short}) — findings")
    B.append("")
    B.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}")
    B.append(f"**Characteristic_id:** {char['id']}")
    B.append("**Tiers complete:** T0 ✓  T1 ☐  T2 ☐  T3 ☐  T4 ☐  T5 ☐  T6 ☐  T7 ☐")
    B.append("")
    B.append("## T0 — Divine Image and Created Design (12 prompts)")
    B.append("")
    B.append("**T0.1.1 — [question text]**")
    B.append("")
    B.append(f"**[CHAR-{args.char_seq}]** E — finding text with verse citations…")
    B.append("")
    B.append("---")
    B.append("")
    B.append("**T0.1.2 — …**")
    B.append("")
    B.append("…")
    B.append("```")
    B.append("")
    B.append("After T0's 12 prompt blocks, post the self-evaluation:")
    B.append("")
    B.append("```")
    B.append("T0 self-evaluation:")
    B.append(f"  1. Prompt count:       12/12 ✓")
    B.append(f"  2. Scope marker:       12× [CHAR-{args.char_seq}] ✓")
    B.append("  3. Citation discipline: <N>/<E_count> E findings cite evidence ✓ (or list uncited)")
    B.append("  4. No cross-tier refs:  ✓")
    B.append("  5. Distinct openings:   ✓")
    B.append("  6. Verse-corpus check:  ✓ (or list phantom refs)")
    B.append("  → PASS. Proceeding to Tier T1.")
    B.append("```")
    B.append("")
    B.append("Then immediately begin Tier T1 in the same response (re-read §3 fresh, author T1's 24 prompts, append the new `## T1 — Inner Being Faculty in Operation (24 prompts)` section, self-evaluate, decide PASS/ALERT).")
    B.append("")
    B.append("### Tiers T1..T7 — chain by default, ALERT on issues")
    B.append("")
    B.append("Each tier follows the same pattern: re-read §3 fresh → author prompts → write tier section → self-evaluate → (if PASS) proceed immediately to next tier; (if ALERT) stop for researcher review. The findings file grows by one tier section per cycle.")
    B.append("")
    B.append("If a single response would be too long to hold a tier + the next one, you may split at a tier boundary (announce *\"...PASS. Proceeding in next response.\"* and resume on the next prompt). The next-tier handoff is the same — re-read §3, author, evaluate, decide. Splitting mid-tier is forbidden.")
    B.append("")
    B.append("### After T7's self-evaluation passes — final Self-check block")
    B.append("")
    B.append("Append a final Self-check block at the end of the findings file (after T7's section):")
    B.append("")
    B.append("```markdown")
    B.append("## Self-check")
    B.append("")
    B.append("- Prompts answered: 189 / 189 ✓ (12+24+31+33+24+21+24+20)")
    B.append("- E findings naming specific evidence: <count>")
    B.append("- S findings: <count>")
    B.append("- G findings: <count>")
    B.append("- Carry-forward observations addressed: <list>")
    B.append("- Unexpected analytical patterns surfaced (across tiers): <list>")
    B.append("- Tiers complete: T0 ✓ T1 ✓ T2 ✓ T3 ✓ T4 ✓ T5 ✓ T6 ✓ T7 ✓")
    B.append("- Per-tier self-evaluations: all PASS (or list ALERTs that were resolved)")
    B.append("```")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## After T7 + Self-check")
    B.append("")
    B.append(f"1. Confirm the findings file is on disk with all 8 tier sections + the final Self-check block.")
    B.append(f"2. Ping CC: \"M10 Char {args.char_seq} ({short}) Phase 9 findings ready\"")
    B.append("3. CC parses, validates evidence-grounding + completeness, applies to cluster_finding with characteristic_id set.")
    B.append(f"4. Move to next characteristic (Char {args.char_seq + 1 if args.char_seq < 6 else '(cluster synthesis)'}).")
    B.append("")
    B.append("---")
    B.append("")
    B.append("*End of brief. Load the structural input (#2) and begin **Tier T0** in your first response. Chain tiers when self-evaluation passes; ALERT only on issues.*")

    BRIEF.write_text("\n".join(B), encoding="utf-8")

    # ===== Structural input =====
    S = []
    S.append(f"# M10 Phase 9 — Characteristic {args.char_seq} ({short}) — structural input")
    S.append("")
    S.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}")
    S.append("")
    S.append("---")
    S.append("")
    S.append("## Required inputs (read brief first)")
    S.append("")
    S.append("| # | Document | Purpose |")
    S.append("|---|---|---|")
    S.append(f"| 1 | **Brief (read first)** — `Sessions/Session_Clusters/M10/{BRIEF.name}` | Primary task instructions |")
    S.append(f"| 2 | **This document** — `Sessions/Session_Clusters/M10/{INPUT.name}` | Characteristic definition + sub-groups + VCGs + verses + 189 prompts |")
    S.append("| 3 | Governing instruction — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` | §12 Phase 9 disciplines |")
    S.append("")
    S.append("---")
    S.append("")
    S.append(f"## §1 — Characteristic {args.char_seq} ({short})")
    S.append("")
    S.append(f"**Short name:** {short}")
    S.append(f"**Characteristic_id:** {char['id']}")
    S.append(f"**Definition:**")
    S.append("")
    S.append(f"> {char['definition']}")
    S.append("")
    S.append(f"**Constituent sub-groups:** {len(subgroups)}")
    S.append(f"**Total verses in scope:** ~{total_verses}")
    S.append("")
    S.append("---")
    S.append("")
    S.append("## §2 — Sub-groups (capacity organisers — not the analytical unit)")
    S.append("")
    for sg in subgroups:
        marker = " *(partial — this sub-group also serves another characteristic; see VCG details to identify which verses belong to the current characteristic)*" if sg["is_partial"] else ""
        S.append(f"### {sg['subgroup_code']} — {sg['label']}{marker}")
        S.append("")
        S.append(f"**core_description:** {sg['core_description']}")
        S.append("")
        S.append(f"**Role under {short}:** {sg['qualifier_note']}")
        S.append("")
        if sg["is_partial"]:
            S.append(f"**Partial register note:** {sg['partial_register_note']}")
            S.append("")
        S.append(f"**Verses in this sub-group:** {sg['verse_count']}")
        S.append("")
        # VCG list for this sub-group
        vcg_summary = defaultdict(int)
        for v in verses_by_sg[sg["subgroup_code"]]:
            vcg_summary[v["vcg_code"] or "(no VCG)"] += 1
        if vcg_summary:
            S.append("**VCGs within this sub-group:**")
            S.append("")
            for vcg_code, count in vcg_summary.items():
                # Get vcg description
                desc_row = conn.execute(
                    "SELECT context_description FROM verse_context_group WHERE group_code = ?",
                    (vcg_code,),
                ).fetchone()
                desc = (desc_row["context_description"] if desc_row else "")[:180]
                S.append(f"- `{vcg_code}` ({count} verses) — {desc}")
            S.append("")
        S.append("---")
        S.append("")

    S.append("## §3 — Verses in scope (per sub-group, canonical Bible order)")
    S.append("")
    for sg in subgroups:
        S.append(f"### {sg['subgroup_code']} — {sg['label']}")
        S.append("")
        for v in verses_by_sg[sg["subgroup_code"]]:
            S.append(f"#### vc={v['vc_id']} — {v['reference']} ({v['strongs_number']} {v['transliteration']}) — VCG `{v['vcg_code']}`")
            S.append("")
            text = (v["verse_text"] or "").strip()
            ctx_before = (v["context_before"] or "").strip()
            ctx_after = (v["context_after"] or "").strip()
            if ctx_before:
                S.append(f"> _… {ctx_before}_")
            S.append(f"> **{text}**")
            if ctx_after:
                S.append(f"> _{ctx_after} …_")
            S.append("")
            S.append(f"**Pass A meaning:** {v['analysis_note']}")
            S.append("")
        S.append("---")
        S.append("")

    S.append("## §4 — Catalogue prompts (T0–T7, 189 total)")
    S.append("")
    for tier in ("T0", "T1", "T2", "T3", "T4", "T5", "T6", "T7"):
        tier_prompts = by_tier.get(tier, [])
        if not tier_prompts:
            continue
        # Get tier title from first prompt
        first = tier_prompts[0]
        S.append(f"### {tier} ({len(tier_prompts)} prompts)")
        S.append("")
        # Component grouping
        current_component = None
        for p in tier_prompts:
            comp = p["component_code"] or ""
            if comp != current_component:
                S.append(f"\n**{comp} — {p['component_title'] or ''}**")
                S.append("")
                current_component = comp
            S.append(f"- **{p['question_code']}** — {p['question_text']}")
        S.append("")
        S.append("---")
        S.append("")

    INPUT.write_text("\n".join(S), encoding="utf-8")
    print(f"Brief: {BRIEF}")
    print(f"Input: {INPUT}")
    print(f"Characteristic {args.char_seq} ({short}): {len(subgroups)} sub-group(s), ~{total_verses} verses")
    conn.close()


if __name__ == "__main__":
    main()
