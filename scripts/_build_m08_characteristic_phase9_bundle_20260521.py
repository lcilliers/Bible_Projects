"""Build a multi-characteristic Phase 9 AI package (bundle).

Per researcher direction 2026-05-19: multiple characteristics may share
one structural input file, but their sub-group/VCG/verse data must stay
distinctly grouped per characteristic, and the brief must instruct the
AI to do SEPARATE 189-prompt passes per characteristic (no cross-mixing
of evidence across characteristics).

Output filenames:
    Sessions/Session_Clusters/M08/WA-M08-phase9-bundle-char{N1+N2+...}-brief-v1-{date}.md
    Sessions/Session_Clusters/M08/WA-M08-phase9-bundle-char{N1+N2+...}-input-v1-{date}.md

The AI is expected to produce ONE findings file per characteristic
(named WA-M08-phase9-char{N}-{short}-findings-v1-{date}.md). The
existing loader (`_apply_phase9_characteristic_findings_20260521.py`)
processes each findings file separately with --char-seq matching.

Usage:
    python scripts/_build_m04_characteristic_phase9_bundle_20260519.py --char-seqs 3,7
    python scripts/_build_m04_characteristic_phase9_bundle_20260519.py --char-seqs 5,6
"""
from __future__ import annotations

import argparse
import sqlite3
from collections import defaultdict
from datetime import datetime
from pathlib import Path

DB = Path("database/bible_research.db")
TODAY = datetime.now().strftime("%Y%m%d")


def fetch_characteristic(conn, char_seq: int):
    row = conn.execute(
        "SELECT * FROM characteristic WHERE cluster_code='M08' AND char_seq=? "
        "AND COALESCE(delete_flagged,0)=0",
        (char_seq,),
    ).fetchone()
    if not row:
        raise SystemExit(f"No M08 characteristic with seq={char_seq}")
    return row


def fetch_subgroups(conn, char_id: int):
    return conn.execute(
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
        (char_id,),
    ).fetchall()


def fetch_observations(conn, char_id: int):
    """Open + confirmed observations relevant to a characteristic.

    'open' observations need to be actioned in this batch; 'confirmed'
    observations carry analytical context that the current batch may
    still need (e.g. SPLIT_SUBGROUP was confirmed in Char 2, but Char 7
    still needs to know which M04-E verses are its evidence).
    """
    return conn.execute(
        """
        SELECT id, observation_type, title, description, target_phase, status,
               resolution_note, characteristic_id, cluster_subgroup_id
        FROM cluster_observation
        WHERE cluster_code='M08'
          AND target_phase='phase_9_findings'
          AND status IN ('open', 'confirmed')
          AND COALESCE(delete_flagged, 0) = 0
          AND (
            characteristic_id = ?
            OR (characteristic_id IS NULL AND description LIKE ?)
          )
        ORDER BY id
        """,
        (char_id, f"%Characteristic {char_id}%"),
    ).fetchall()


def fetch_verses_for_sg(conn, sg_id: int):
    return conn.execute(
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
        (sg_id,),
    ).fetchall()


def fetch_catalogue(conn):
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
    return by_tier


def safe(short: str) -> str:
    return short.replace(" ", "-").replace("/", "-")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--char-seqs", required=True,
                    help="Comma-separated characteristic sequence numbers, e.g. '3,7' or '5,6'")
    args = ap.parse_args()
    char_seqs = [int(s.strip()) for s in args.char_seqs.split(",") if s.strip()]
    if len(char_seqs) < 2:
        raise SystemExit("Use --char-seqs with 2+ values for bundles. For a single characteristic, use the single-char builder.")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    cluster = conn.execute("SELECT description FROM cluster WHERE cluster_code='M08'").fetchone()

    # Fetch per-characteristic data
    chars_data = []
    for seq in char_seqs:
        char = fetch_characteristic(conn, seq)
        subgroups = fetch_subgroups(conn, char["id"])
        observations = fetch_observations(conn, char["id"])
        verses_by_sg = {}
        for sg in subgroups:
            verses_by_sg[sg["subgroup_code"]] = [dict(v) for v in fetch_verses_for_sg(conn, sg["sg_id"])]
        total_verses = sum(sg["verse_count"] or 0 for sg in subgroups)
        chars_data.append({
            "seq": seq,
            "char": char,
            "short": char["short_name"],
            "safe_short": safe(char["short_name"]),
            "subgroups": subgroups,
            "observations": observations,
            "verses_by_sg": verses_by_sg,
            "total_verses": total_verses,
        })

    by_tier = fetch_catalogue(conn)

    bundle_tag = "char" + "+".join(str(s) for s in char_seqs)
    BRIEF = Path(f"Sessions/Session_Clusters/M08/WA-M08-phase9-bundle-{bundle_tag}-brief-v1-{TODAY}.md")
    INPUT = Path(f"Sessions/Session_Clusters/M08/WA-M08-phase9-bundle-{bundle_tag}-input-v1-{TODAY}.md")

    total_verses_all = sum(c["total_verses"] for c in chars_data)

    # ===== Brief =====
    B = []
    B.append(f"# M08 Phase 9 — Bundle ({bundle_tag}) — brief")
    B.append("")
    B.append(f"**Cluster:** M08 — {cluster['description']}")
    B.append("**Characteristics in this bundle:** " + ", ".join(
        f"{c['seq']} ({c['short']})" for c in chars_data
    ))
    B.append(f"**Total verses across the bundle:** ~{total_verses_all}")
    B.append(f"**Total prompts to author:** {189 * len(chars_data)} (= 189 × {len(chars_data)} separate passes)")
    B.append(f"**Task date:** {datetime.now().strftime('%Y-%m-%d')}")
    B.append("**Audience:** Claude AI session")
    B.append("")
    B.append("**Read this brief first.** Structural input is in a separate file referenced below.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Required inputs")
    B.append("")
    B.append("| # | Document | Purpose |")
    B.append("|---|---|---|")
    B.append(f"| 1 | **This brief** — `Sessions/Session_Clusters/M08/{BRIEF.name}` | Primary task instructions |")
    B.append(f"| 2 | **Structural input** — `Sessions/Session_Clusters/M08/{INPUT.name}` | Per-characteristic data blocks + shared 189-prompt catalogue + carry-forward observations |")
    B.append("| 3 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` | §12 Phase 9 disciplines; §12.4 parser-safe form |")
    B.append("| 4 | **Science extract** — `Workflow/Sciences/wa-m08-pride-scienceextract-v1_0-20260513.md` | Programme-curated scientific lens for T7.3 (human science framework) prompts — ensures consistent framing across clusters and reviewers |")
    B.append("| 5 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260506.md` Ch.1 'Defining Inner Being' | Inner-being scope definition (background) |")
    B.append("| 6 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |")
    B.append("")
    B.append("> The full 189-prompt T0–T7 catalogue is reproduced inside the structural input. No separate catalogue file required.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Why this is a bundle (not a single characteristic)")
    B.append("")
    B.append("This package covers **multiple characteristics** to save on session setup overhead. The data for each characteristic is kept distinct in the structural input — sub-groups, VCGs, and verses are grouped under their own characteristic block (§2.A, §2.B, …). **Do not pool evidence across characteristics.** Each 189-prompt pass uses ONLY that characteristic's evidence.")
    B.append("")
    B.append("> Per researcher direction 2026-05-19: *\"you can combine more than one characteristic in the dataset, but keep the grouping of the sub group distinctly separate into characteristics, and be clear in the guide to do separate batches of going through the catalogue.\"*")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## ⚠️ STAGED EXECUTION PROTOCOL — MANDATORY ⚠️")
    B.append("")
    B.append("**Known prior failure mode (M07 bundle, 2026-05-20):** the AI attempted to hold all 4 characteristics × 189 prompts in working memory and answer them as a continuous stream. It fell over twice — lost track of which batch was active, mixed evidence across characteristics, and produced inconsistent CHAR-N scope markers. **Do not repeat that pattern.**")
    B.append("")
    B.append("This bundle is **a series of independent batches**, not a single 4×189 pass. Each batch must be **completed, written to disk, and confirmed** before the next batch begins.")
    B.append("")
    B.append("### Hard procedural sequence")
    B.append("")
    B.append("**For each batch, in the order listed below, you MUST:**")
    B.append("")
    B.append("1. **OPEN BATCH** — announce: *\"Starting Batch N — Characteristic N (<name>)\"*.")
    B.append("2. **READ EVIDENCE** — read **every** verse-meaning in §3.{letter} of the structural input for THIS batch's characteristic. Do not look at any other §3 section.")
    B.append("3. **AUTHOR 189 PROMPTS** — work through T0..T7 in order. If a single response can't hold the whole batch, split by tier pair (T0+T1 → T2+T3 → T4+T5 → T6+T7) — but the batch is not finished until all 189 prompts have a finding row.")
    B.append("4. **WRITE THE FILE** — emit the complete findings document as a single contiguous markdown block, with the exact filename from the table below. Include the Self-check at the end.")
    B.append("5. **CONFIRM WRITTEN** — announce: *\"Batch N file written: WA-M08-phase9-charN-<name>-findings-v1-20260521.md, 189/189 prompts, [CHAR-N] markers verified\"*.")
    B.append("6. **STOP** — do not begin Batch N+1 in the same response. Wait for the next prompt from CC or the user. CC needs to validate Batch N's file before you start Batch N+1.")
    B.append("")
    B.append("**Between batches, your working memory must reset.** Do not carry verse-citation patterns, finding language, or evidence summaries from one batch into another. The next batch starts fresh from §3.{next-letter}.")
    B.append("")
    B.append("### Recovery if you find yourself drifting mid-batch")
    B.append("")
    B.append("If at any point you notice you have:")
    B.append("")
    B.append("- Cited evidence from another characteristic's §3 block,")
    B.append("- Mixed `[CHAR-N]` scope markers within one findings file,")
    B.append("- Skipped prompts \"to come back later\",")
    B.append("- Begun a second characteristic before the first file is written,")
    B.append("")
    B.append("then: **STOP** the current response, announce the issue, abandon the half-written batch, and restart that batch from scratch (re-read §3.{letter}, re-author from T0.1.1). It is faster to restart cleanly than to patch a contaminated batch.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Batch sequence")
    B.append("")
    B.append(f"You will do **{len(chars_data)} separate 189-prompt batches**, one per characteristic, in the order listed below. Each batch is fully bounded to its own characteristic.")
    B.append("")
    B.append("| Batch | Characteristic | Sub-groups | Verses | §3 section | Output file (you produce) |")
    B.append("|---|---|---|---:|---|---|")
    for idx, c in enumerate(chars_data, start=1):
        sg_codes = ", ".join(sg["subgroup_code"] for sg in c["subgroups"])
        out_name = f"WA-M08-phase9-char{c['seq']}-{c['safe_short']}-findings-v1-{TODAY}.md"
        letter = chr(ord("A") + idx - 1)
        B.append(f"| {idx} | Char {c['seq']} — {c['short']} | {sg_codes} | ~{c['total_verses']} | §3.{letter} | `Sessions/Session_Clusters/M08/{out_name}` |")
    B.append("")
    B.append("**The batch is not finished until the file is on disk.** CC validates each file (parser-safe form, completeness, CHAR-N scope marker consistency) before Batch N+1 begins.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Output format (applies to every batch)")
    B.append("")
    B.append("Per prompt, one block; parser-safe form per v2_8 §12.4:")
    B.append("")
    B.append("```")
    B.append("**T#.#.# — question text excerpt (optional)**")
    B.append("")
    B.append("**[CHAR-N]** E — Finding text. Cite specific verses / VCGs / sub-groups from the characteristic's evidence block. Quote verse phrases that evidence the answer. The finding must be self-contained for a Session C reader.")
    B.append("")
    B.append("---")
    B.append("```")
    B.append("")
    B.append("**Scope marker** is `**[CHAR-N]**` where **N is the characteristic number for that batch** (e.g., `**[CHAR-2]**` for the Presumptuous-defiance batch, `**[CHAR-3]**` for the Boasting batch). CC's loader uses this to set characteristic_id on each row, so it MUST match the current batch's characteristic — and never reference a characteristic that isn't this bundle's set (M08 has only CHAR-1..CHAR-5; CHAR-1 is a separate session, not in this bundle).")
    B.append("")
    B.append("**Outcome codes:**")
    B.append("- **E** — evidenced; cite specific verses / VCGs")
    B.append("- **S** — silent; describe the analytical significance of the absence")
    B.append("- **G** — gap; describe what data would be needed to answer")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Discipline (per v2_8 §12)")
    B.append("")
    B.append("1. **One batch per response (or one tier-pair segment per response for an oversized batch).** Never start a second characteristic in the same response that finished the first. The STOP gate is structural — it's how you avoid the prior-failure mode.")
    B.append("2. **Read every verse-meaning in the structural input for the current batch.** No sampling. The Pass A meanings condense each verse's inner-being content — read them all for the batch's characteristic.")
    B.append("3. **Per prompt, ground in specific evidence.** Every E finding names verses, VCGs, or sub-groups. The test for a good answer is *can I name what evidences this?*")
    B.append("4. **Fluency is not a quality signal** (v2_8 §2.4). Plausible-sounding text without specific citations is rejected.")
    B.append("5. **No sub-group-scope findings.** All findings at characteristic scope. Where evidence differs by sub-group within a characteristic, the finding text names the sub-group(s) inline.")
    B.append("6. **No cross-characteristic mixing.** Evidence from another characteristic's block is OFF-LIMITS for the current batch. If a cross-characteristic observation is significant, note it in the Self-check for that batch — do NOT embed cross-batch findings.")
    B.append("7. **No cluster-scope findings.** Cluster synthesis runs after all 5 characteristics finish.")
    B.append("8. **Self-check before submitting each batch** — confirm 189 prompts have rows; confirm every E names evidence; confirm every `[CHAR-N]` marker matches the batch's characteristic number, not another batch's.")
    B.append("")
    B.append("---")
    B.append("")
    # Per-characteristic carry-forward observations
    any_obs = any(c["observations"] for c in chars_data)
    if any_obs:
        B.append("## Carry-forward observations (apply per-batch)")
        B.append("")
        B.append("These analytical hints were raised at characteristic-mapping time. Two statuses are shown: **OPEN** means action and flag at end of batch; **CONFIRMED** means already validated by an earlier Phase 9 batch — included here as context that may matter for the current batch's evidence selection.")
        B.append("")
        for c in chars_data:
            if not c["observations"]:
                continue
            B.append(f"### For Characteristic {c['seq']} ({c['short']})")
            B.append("")
            for o in c["observations"]:
                status_tag = "**OPEN**" if o["status"] == "open" else "**CONFIRMED (context only)**"
                B.append(f"**{o['observation_type']} — {o['title']}** — {status_tag}")
                B.append("")
                B.append(f"> {o['description']}")
                B.append("")
                if o["status"] == "confirmed" and o["resolution_note"]:
                    B.append(f"_Earlier-batch resolution:_ {o['resolution_note']}")
                    B.append("")
                if o["status"] == "open":
                    B.append("At end of this batch, flag whether the observation surfaced as expected.")
                    B.append("")
        B.append("---")
        B.append("")
    else:
        B.append("## Carry-forward observations")
        B.append("")
        B.append("No carry-forward observations are linked to the characteristics in this bundle. If you surface unexpected analytical patterns during any batch, write them in that batch's final summary so CC can record them as new cluster_observation rows.")
        B.append("")
        B.append("---")
        B.append("")

    B.append("## Self-check template (use at the end of EACH batch's findings file)")
    B.append("")
    B.append("```markdown")
    B.append("## Self-check")
    B.append("")
    B.append("- Prompts answered: 189 / 189 ✓")
    B.append("- E findings naming specific evidence: <count>")
    B.append("- S findings: <count>")
    B.append("- G findings: <count>")
    B.append("- Carry-forward observations addressed: <list>")
    B.append("- Unexpected analytical patterns surfaced: <list>")
    B.append("```")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## After you finish each batch — the STOP gate")
    B.append("")
    B.append("1. **Write the batch's findings to its own file** using the exact filename from the batch sequence table.")
    B.append("2. **Self-check inside the file** — confirm 189 prompts have rows; confirm every E names evidence; confirm every `[CHAR-N]` marker matches the batch's characteristic number.")
    B.append("3. **Announce file written** — *\"Batch N file written: <filename>, 189/189 prompts, [CHAR-N] markers verified\"*.")
    B.append("4. **STOP**. Do not begin Batch N+1 in the same response. Wait for the next prompt.")
    B.append("5. CC validates and applies the batch's findings to `cluster_finding` with the right characteristic_id.")
    B.append("6. When CC confirms validation, you may begin Batch N+1 in a new response — starting from step 1 of the staged execution protocol (re-read §3.{next-letter} fresh).")
    B.append("")
    B.append("If a single batch is too large to fit in one response, split that batch's authorship by tier-pair (T0+T1 → T2+T3 → T4+T5 → T6+T7) — but the batch is still ONE file with ONE filename. Don't fragment one batch across multiple files.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("*End of brief. Load the structural input (#2) and begin Batch 1 (and only Batch 1).*")

    BRIEF.write_text("\n".join(B), encoding="utf-8")

    # ===== Structural input =====
    S = []
    S.append(f"# M08 Phase 9 — Bundle ({bundle_tag}) — structural input")
    S.append("")
    S.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}")
    S.append("")
    S.append("---")
    S.append("")
    S.append("## Required inputs (read brief first)")
    S.append("")
    S.append("| # | Document | Purpose |")
    S.append("|---|---|---|")
    S.append(f"| 1 | **Brief (read first)** — `Sessions/Session_Clusters/M08/{BRIEF.name}` | Primary task instructions |")
    S.append(f"| 2 | **This document** — `Sessions/Session_Clusters/M08/{INPUT.name}` | Per-characteristic data blocks + 189-prompt catalogue |")
    S.append("| 3 | Governing instruction — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` | §12 Phase 9 disciplines |")
    S.append("")
    S.append("---")
    S.append("")
    # Index
    S.append("## §1 — Bundle index")
    S.append("")
    S.append("This bundle contains the following characteristics. **Each batch uses ONLY its own block.**")
    S.append("")
    S.append("| Batch | Characteristic_id | Short name | Sub-groups | Verses | Section in this file |")
    S.append("|---|---|---|---|---:|---|")
    for idx, c in enumerate(chars_data, start=1):
        letter = chr(ord("A") + idx - 1)
        sg_codes = ", ".join(sg["subgroup_code"] for sg in c["subgroups"])
        S.append(f"| {c['seq']} | {c['char']['id']} | {c['short']} | {sg_codes} | ~{c['total_verses']} | §2.{letter}, §3.{letter} |")
    S.append("")
    S.append("---")
    S.append("")

    # §2 — per-characteristic definition + sub-groups
    S.append("## §2 — Characteristic definitions + sub-groups (per batch)")
    S.append("")
    for idx, c in enumerate(chars_data, start=1):
        letter = chr(ord("A") + idx - 1)
        S.append(f"### §2.{letter} — Characteristic {c['seq']} ({c['short']})")
        S.append("")
        S.append(f"**Characteristic_id:** {c['char']['id']}")
        S.append(f"**Definition:**")
        S.append("")
        S.append(f"> {c['char']['definition']}")
        S.append("")
        S.append(f"**Constituent sub-groups:** {len(c['subgroups'])}")
        S.append(f"**Total verses:** ~{c['total_verses']}")
        S.append("")
        for sg in c["subgroups"]:
            marker = " *(partial — also serves another characteristic; see VCG details)*" if sg["is_partial"] else ""
            S.append(f"#### {sg['subgroup_code']} — {sg['label']}{marker}")
            S.append("")
            S.append(f"**core_description:** {sg['core_description']}")
            S.append("")
            S.append(f"**Role under {c['short']}:** {sg['qualifier_note']}")
            S.append("")
            if sg["is_partial"]:
                S.append(f"**Partial register note:** {sg['partial_register_note']}")
                S.append("")
            S.append(f"**Verses in this sub-group:** {sg['verse_count']}")
            S.append("")
            # VCG list
            vcg_summary = defaultdict(int)
            for v in c["verses_by_sg"][sg["subgroup_code"]]:
                vcg_summary[v["vcg_code"] or "(no VCG)"] += 1
            if vcg_summary:
                S.append("**VCGs within this sub-group:**")
                S.append("")
                for vcg_code, count in vcg_summary.items():
                    desc_row = conn.execute(
                        "SELECT context_description FROM verse_context_group WHERE group_code = ?",
                        (vcg_code,),
                    ).fetchone()
                    desc = (desc_row["context_description"] if desc_row else "")[:180]
                    S.append(f"- `{vcg_code}` ({count} verses) — {desc}")
                S.append("")
        S.append("---")
        S.append("")

    # §3 — verses per characteristic
    S.append("## §3 — Verses in scope (per characteristic, canonical Bible order)")
    S.append("")
    for idx, c in enumerate(chars_data, start=1):
        letter = chr(ord("A") + idx - 1)
        S.append(f"### §3.{letter} — Verses for Characteristic {c['seq']} ({c['short']})")
        S.append("")
        for sg in c["subgroups"]:
            S.append(f"#### {sg['subgroup_code']} — {sg['label']}")
            S.append("")
            for v in c["verses_by_sg"][sg["subgroup_code"]]:
                S.append(f"##### vc={v['vc_id']} — {v['reference']} ({v['strongs_number']} {v['transliteration']}) — VCG `{v['vcg_code']}`")
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
            S.append("")
        S.append("---")
        S.append("")

    # §4 — shared catalogue
    S.append("## §4 — Catalogue prompts (T0–T7, 189 total) — shared across all batches")
    S.append("")
    for tier in ("T0", "T1", "T2", "T3", "T4", "T5", "T6", "T7"):
        tier_prompts = by_tier.get(tier, [])
        if not tier_prompts:
            continue
        S.append(f"### {tier} ({len(tier_prompts)} prompts)")
        S.append("")
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
    print(f"Bundle: {len(chars_data)} characteristics, ~{total_verses_all} verses total")
    for c in chars_data:
        print(f"  Char {c['seq']} ({c['short']}): {len(c['subgroups'])} sub-group(s), ~{c['total_verses']} verses")
    conn.close()


if __name__ == "__main__":
    main()
