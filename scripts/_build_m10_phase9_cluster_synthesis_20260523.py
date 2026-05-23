"""Build the M10 Phase 9 cluster-synthesis (8th) session package.

Per researcher direction:
- Source structural input: per-prompt synthesis matrix - for each of the
  189 prompts (T0.1.1...T7.3.4), the 6 characteristics' findings are
  stacked side-by-side (verbatim from cluster_finding).
- Output expected: BOTH 189 cluster-scope rows AND a free-form
  synthesis prose appendix.
- Science extract is a required input (per feedback_phase9_science_extract_required).

Reads cluster_finding directly from the DB to assemble the per-prompt
matrix; no dependency on the markdown findings files.

Outputs:
  Sessions/Session_Clusters/M10/wa-cluster-M10-phase9-cluster-synthesis-brief-v1-{date}.md
  Sessions/Session_Clusters/M10/wa-cluster-M10-phase9-cluster-synthesis-input-v1-{date}.md
"""
from __future__ import annotations

import sqlite3
from collections import defaultdict
from datetime import datetime
from pathlib import Path

DB = Path("database/bible_research.db")
CLUSTER = "M10"
TODAY = datetime.now().strftime("%Y%m%d")
TODAY_ISO = datetime.now().strftime("%Y-%m-%d")
SCIENCE = "Workflow/Sciences/wa-m10-guilt-scienceextract-v1_0-20260513.md"

BRIEF = Path(f"Sessions/Session_Clusters/M10/wa-cluster-M10-phase9-cluster-synthesis-brief-v1-{TODAY}.md")
INPUT = Path(f"Sessions/Session_Clusters/M10/wa-cluster-M10-phase9-cluster-synthesis-input-v1-{TODAY}.md")


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    cluster = conn.execute("SELECT description, gloss FROM cluster WHERE cluster_code=?", (CLUSTER,)).fetchone()

    chars = conn.execute(
        "SELECT id, char_seq, short_name, definition "
        "FROM characteristic WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 "
        "ORDER BY char_seq",
        (CLUSTER,),
    ).fetchall()

    observations = conn.execute(
        "SELECT id, characteristic_id, observation_type, title, description, "
        "       status, resolution_note "
        "FROM cluster_observation WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 "
        "ORDER BY id",
        (CLUSTER,),
    ).fetchall()

    # Pull all cluster_finding rows for the 6 characteristics, joined to the
    # catalogue so we have tier/component/question for grouping.
    rows = conn.execute(
        """
        SELECT q.question_code, q.tier, q.component_code, q.component_title,
               q.question_text,
               cf.characteristic_id, c.char_seq, c.short_name,
               cf.finding_status, cf.finding_text
        FROM cluster_finding cf
        JOIN wa_obs_question_catalogue q ON q.obs_id = cf.obs_id
        JOIN characteristic c ON c.id = cf.characteristic_id
        WHERE cf.cluster_code = ?
          AND cf.characteristic_id IS NOT NULL
          AND COALESCE(cf.delete_flagged, 0) = 0
        ORDER BY q.tier, q.component_code, q.prompt_seq, c.char_seq
        """,
        (CLUSTER,),
    ).fetchall()

    # Group findings by question_code -> list of (char_seq, short_name, finding_status, finding_text)
    by_qcode = defaultdict(list)
    qmeta = {}
    for r in rows:
        qc = r["question_code"]
        if qc not in qmeta:
            qmeta[qc] = (r["tier"], r["component_code"], r["component_title"], r["question_text"])
        by_qcode[qc].append((r["char_seq"], r["short_name"], r["finding_status"], r["finding_text"]))

    # Sanity: every q_code should have 5 entries (one per M10 characteristic)
    EXPECTED_CHAR_COUNT = 6
    bad = {qc: len(lst) for qc, lst in by_qcode.items() if len(lst) != EXPECTED_CHAR_COUNT}
    if bad:
        print(f"WARNING: {len(bad)} prompts do not have {EXPECTED_CHAR_COUNT} findings. Sample: {dict(list(bad.items())[:3])}")

    # =====
    # BRIEF
    # =====
    B = []
    B.append(f"# {CLUSTER} Phase 9 — Cluster Synthesis (8th session) — brief")
    B.append("")
    B.append(f"**Cluster:** {CLUSTER} — {cluster['description']}")
    B.append(f"**Session:** 8 (cluster-scope synthesis — final Phase 9 session)")
    B.append(f"**Task date:** {TODAY_ISO}")
    B.append("**Audience:** Claude AI session")
    B.append("")
    B.append("This is the final Phase 9 session for M10. The 22 characteristic-scope batches (Humility, Submission, Contrition, Meekness and gentleness, Dignity, Willing-heartedness) are complete; each authored 189 findings citing specific verses. This session looks ACROSS those five sets to author the cluster-scope findings — patterns, divergences, and shared anchors that emerge only when the five are compared.")
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
    B.append(f"| 2 | **Structural input** — `Sessions/Session_Clusters/M10/{INPUT.name}` | Per-prompt synthesis matrix: for each of the 189 prompts, the 6 characteristics' findings stacked side-by-side (verbatim from `cluster_finding`); plus confirmed observations |")
    B.append("| 3 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` | §12 Phase 9 disciplines; §12.4 parser-safe form |")
    B.append(f"| 4 | **Science extract** — `{SCIENCE}` | Programme-curated scientific lens for T7.3 prompts — ensures consistent framing |")
    B.append("| 5 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260506.md` Ch.1 'Defining Inner Being' | Inner-being scope definition (background) |")
    B.append("| 6 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## What you are producing")
    B.append("")
    B.append(f"For the M10 cluster as a whole, two output forms are required (per researcher direction):")
    B.append("")
    B.append("### Output A — 189 cluster-scope findings (parser-safe rows)")
    B.append("")
    B.append("For each of the 189 catalogue prompts, author ONE cluster-scope finding examining what surfaces when the 6 characteristics' findings are compared. The cluster-scope finding answers: *what does the M10 cluster — across its 6 characteristics — reveal about this question?* It is the comparative-integrative layer above the per-characteristic answers.")
    B.append("")
    B.append("Use the SAME parser-safe format as the per-characteristic sessions:")
    B.append("")
    B.append("```")
    B.append("**T#.#.# — question text excerpt (optional)**")
    B.append("")
    B.append("**[CLUSTER]** E — Cluster-scope finding text. Cite specific characteristics by name and the specific patterns/divergences/anchors they reveal when compared. Quote shared anchor verses where multiple characteristics point to the same evidence. The finding must be self-contained for a Session C reader.")
    B.append("")
    B.append("---")
    B.append("```")
    B.append("")
    B.append("**Scope marker** is `**[CLUSTER]**` (CC's loader will map this to characteristic_id=NULL, finding_status='cluster_synthesis'). Do NOT use [CHAR-N] markers in this output.")
    B.append("")
    B.append("**Outcome codes:**")
    B.append("- **E** — evidenced; the 6 characteristics' findings provide enough comparative evidence to author a cluster-scope answer")
    B.append("- **S** — silent; the cluster's combined evidence reveals no meaningful cluster-level pattern beyond the per-char answers")
    B.append("- **G** — gap; the cluster-level pattern would require evidence the 6 characteristics' findings don't supply")
    B.append("")
    B.append("### Output B — Synthesis prose appendix (free-form)")
    B.append("")
    B.append("After the 189-row block, write a free-form prose appendix capturing the emergent themes that surface across the five characteristics — themes that the 189-prompt structure does not fully capture. Suggested themes (drawn from the M10 carry-forward observations + analytical hints surfaced through Phase 3–8.5):")
    B.append("")
    B.append("- The **CHAR-1 volume-split** across split sub-groups (e.g. M10-T/M10-V for sin family) / M10-C (divine encounter) — what coherent characteristic identity holds the three registers together, and where do they genuinely diverge?")
    B.append("- The **M06 ↔ M10 contempt-pride relational pair** — CHAR-5 holds the pride-recipient face; M06 holds the contempt-projection source. The cross-cluster dynamic in detail.")
    B.append("- The **M12 ↔ M10 innocence-purity polarity** — CHAR-6's innocence-as-shield-against-pride; the inner moral state that protects against guilt-pride.")
    B.append("- **OT vs NT vocabulary arcs** across the cluster — where does each characteristic's vocabulary tradition concentrate?")
    B.append("- **Vertical vs horizontal pride** — pride before God (M10-C) vs pride between humans (much of M10-A, M10-B, M10-D, M10-E, M10-G); what shifts across the registers?")
    B.append("- **Pride removed vs pride imposed** — the divine reversal of pride (e.g. Isa 49:23, 1Pe 2:6) vs God's putting-to-pride (Psa 25:3, 1Cor 1:27); when is each operative?")
    B.append("- **Christological convergence points** — Heb 12:2 (\"despising the pride\"); 1Pe 2:6 (\"will not be put to pride\"); Phili 3:19 (inverted glory-in-pride); Isa 50:7 (servant set face like flint against pride); Rom 9:33 (cornerstone faith vs disgrace).")
    B.append("- **Communal vs solitary** registers across the 7")
    B.append("- **Eschatological orientation** — degree to which each characteristic is forward-leaning")
    B.append("- **Inversions and corruptions** — how each characteristic's healthy register relates to its corrupt/absent register")
    B.append("- Any **unexpected** cross-characteristic patterns you surface during the 189-row pass")
    B.append("")
    B.append("Suggested length: 2,000–4,000 words for the appendix. Use sub-headings per theme. Cite the per-characteristic findings (e.g. \"Char 5 T6.1.1's finding that contempt produces pride across 11 exoutheneō verses\") rather than re-citing verses already cited in the structural input.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Discipline")
    B.append("")
    B.append("1. **Per-prompt comparative reading.** For each T#.#.# block in §3 of the structural input, read the 6 characteristics' findings stacked together before authoring the cluster-scope row. The test for a good cluster-scope answer is: *what does seeing the 5 side-by-side reveal that no single characteristic's answer reveals?*")
    B.append("2. **Cite by characteristic.** The cluster-scope finding names which characteristics contribute what — e.g., \"Humility (Char 1) and Submission (Char 2) co-occur in many verses but with different agencies — Char 1 names the dispositional posture; Char 2 names the volitional act of transgression.\"")
    B.append("3. **Don't restate the per-char findings.** The cluster-scope row is the INTEGRATION across them, not a summary of each.")
    B.append("4. **Fluency is not a quality signal.** Plausible-sounding integration without specific cross-characteristic naming is rejected.")
    B.append("5. **Use [CLUSTER] scope marker only.** Do NOT use [CHAR-N] markers; this is the cluster-scope layer.")
    B.append("6. **Honour the confirmed observations.** The four cluster_observations (see §2 of structural input) are inputs to your synthesis — they name the boundaries the researcher already validated.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Confirmed cluster observations (status before this session)")
    B.append("")
    B.append("All four are status `confirmed` (validated via per-characteristic Phase 9 self-checks):")
    B.append("")
    for o in observations:
        char_label = f"Char {o['characteristic_id']}" if o['characteristic_id'] else "Cluster-wide"
        B.append(f"- **#{o['id']} {o['observation_type']}** ({char_label}) — {o['title']}")
    B.append("")
    B.append("Reference the resolution notes in §2 of the structural input for the validated analytical findings.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Output structure (recommended)")
    B.append("")
    B.append("```markdown")
    B.append(f"# {CLUSTER} Phase 9 — Cluster Synthesis — findings")
    B.append("")
    B.append(f"**Date:** {TODAY_ISO}")
    B.append("**Scope:** Cluster M10 (Humility, Meekness and Submission) — across 6 characteristics")
    B.append("**Prompts answered:** 189 / 189")
    B.append("")
    B.append("## T0 — Divine Image and Created Design")
    B.append("")
    B.append("**T0.1.1 — [question excerpt]**")
    B.append("")
    B.append("**[CLUSTER]** E — Cluster-scope finding citing specific characteristics and patterns.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("...")
    B.append("")
    B.append("## Self-check")
    B.append("")
    B.append("- Cluster-scope prompts answered: 189 / 189 ✓")
    B.append("- E / S / G counts: <numbers>")
    B.append("- Themes covered in appendix: <list>")
    B.append("- New cross-characteristic patterns discovered (not surfaced in per-char self-checks): <list>")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Appendix — Synthesis prose")
    B.append("")
    B.append("### Theme 1 — [name]")
    B.append("")
    B.append("Prose text…")
    B.append("```")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## After you finish")
    B.append("")
    B.append(f"1. Save the output as `Sessions/Session_Clusters/M10/wa-cluster-M10-phase9-cluster-synthesis-findings-v1-{TODAY}.md`.")
    B.append(f"2. If segmenting by tier-pair: filename pattern `wa-cluster-M10-phase9-cluster-synthesis-findings-seg{{N}}-T#T#-v1-{TODAY}.md` in a sub-folder.")
    B.append("3. Ping CC: \"M10 cluster synthesis Phase 9 findings ready\".")
    B.append("4. CC parses, validates 189 [CLUSTER] rows, applies to cluster_finding with finding_status='cluster_synthesis' and characteristic_id=NULL; appendix saved as standalone artefact.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("*End of brief. Load the structural input (#2) and begin.*")
    BRIEF.write_text("\n".join(B), encoding="utf-8")

    # =====
    # INPUT (per-prompt synthesis matrix)
    # =====
    S = []
    S.append(f"# {CLUSTER} Phase 9 — Cluster Synthesis — structural input")
    S.append("")
    S.append(f"**Date:** {TODAY_ISO}")
    S.append(f"**Cluster:** {CLUSTER} — {cluster['description']}")
    S.append("")
    S.append("---")
    S.append("")
    # §1 — cluster overview
    S.append("## §1 — Cluster overview")
    S.append("")
    S.append("M10 (Humility, Meekness and Submission) holds 6 inner-being characteristics:")
    S.append("")
    S.append("| Char | Short name | One-line definition |")
    S.append("|---:|---|---|")
    for c in chars:
        defn_short = (c["definition"] or "").split(".")[0]
        S.append(f"| {c['char_seq']} | {c['short_name']} | {defn_short}. |")
    S.append("")
    S.append("Each characteristic produced 189 findings in its Phase 9 batch (1,323 rows total in `cluster_finding`).")
    S.append("")
    S.append("---")
    S.append("")
    # §2 — confirmed observations with resolution notes
    S.append("## §2 — Confirmed cluster observations (with resolution notes)")
    S.append("")
    S.append("These four observations were raised at characteristic-mapping time and confirmed during Phase 9. They name the boundaries already validated and are direct inputs to the synthesis.")
    S.append("")
    for o in observations:
        char_label = f"linked to Char {o['characteristic_id']}" if o['characteristic_id'] else "cluster-wide"
        S.append(f"### Observation #{o['id']} — {o['observation_type']} ({char_label})")
        S.append("")
        S.append(f"**Title:** {o['title']}")
        S.append("")
        S.append(f"**Description:**")
        S.append("")
        S.append(f"> {o['description']}")
        S.append("")
        if o['resolution_note']:
            S.append(f"**Confirmed resolution:**")
            S.append("")
            S.append(f"> {o['resolution_note']}")
            S.append("")
        S.append("---")
        S.append("")

    # §3 — per-prompt synthesis matrix
    S.append("## §3 — Per-prompt synthesis matrix")
    S.append("")
    S.append("For each of the 189 prompts (T0.1.1 … T7.3.4), the 6 characteristics' findings are stacked verbatim below. Read all 5 before authoring the cluster-scope row in your output.")
    S.append("")

    # Order: by tier, by component, by prompt_seq
    qcode_order = sorted(by_qcode.keys(), key=lambda q: (q.split('.')[0], int(q.split('.')[1]), int(q.split('.')[2])))

    current_tier = None
    current_component = None
    for qc in qcode_order:
        tier, comp_code, comp_title, q_text = qmeta[qc]
        if tier != current_tier:
            S.append(f"### {tier}")
            S.append("")
            current_tier = tier
            current_component = None
        if comp_code != current_component:
            S.append(f"#### {comp_code} — {comp_title or ''}")
            S.append("")
            current_component = comp_code

        S.append(f"##### {qc} — {q_text}")
        S.append("")
        findings = sorted(by_qcode[qc], key=lambda x: x[0])  # by char_seq
        for char_seq, short_name, status, body in findings:
            status_short = {'finding': 'E', 'silent': 'S', 'gap': 'G', 'cluster_synthesis': 'C'}.get(status, status)
            S.append(f"**[CHAR-{char_seq}] {short_name}** ({status_short})")
            S.append("")
            # Body verbatim - the body already includes the **[CHAR-N]** E - prefix
            # Strip the leading marker since we just labelled it above
            body_clean = body.strip()
            if body_clean.startswith(f"**[CHAR-{char_seq}]**"):
                # Remove the marker prefix and any leading "E -" / "S -" / "G -"
                body_clean = body_clean.split(" — ", 1)[-1] if " — " in body_clean else body_clean
            S.append(body_clean)
            S.append("")
        S.append("---")
        S.append("")

    INPUT.write_text("\n".join(S), encoding="utf-8")
    print(f"Brief: {BRIEF}")
    print(f"Input: {INPUT}")
    print(f"Brief size: {BRIEF.stat().st_size:,} bytes")
    print(f"Input size: {INPUT.stat().st_size:,} bytes")
    print(f"Prompts in matrix: {len(qcode_order)}")
    print(f"Findings stacked: {sum(len(by_qcode[q]) for q in qcode_order)}")
    conn.close()


if __name__ == "__main__":
    main()
