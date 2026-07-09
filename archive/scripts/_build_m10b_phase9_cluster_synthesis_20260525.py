"""Build the M10b Phase 9 cluster-synthesis (7th) session package.

Per researcher direction:
- Source structural input: per-prompt synthesis matrix - for each of the
  189 prompts (T0.1.1...T7.3.4), the {N} characteristics' findings are
  stacked side-by-side (verbatim from cluster_finding).
- Output expected: BOTH 189 cluster-scope rows AND a free-form
  synthesis prose appendix.
- Science extract is a required input (per feedback_phase9_science_extract_required).

Reads cluster_finding directly from the DB to assemble the per-prompt
matrix; no dependency on the markdown findings files.

Outputs:
  Sessions/Session_Clusters/M10b/wa-cluster-M10b-phase9-cluster-synthesis-brief-v1-{date}.md
  Sessions/Session_Clusters/M10b/wa-cluster-M10b-phase9-cluster-synthesis-input-v1-{date}.md
"""
from __future__ import annotations

import sqlite3
from collections import defaultdict
from datetime import datetime
from pathlib import Path

DB = Path("database/bible_research.db")
CLUSTER = "M10b"
TODAY = datetime.now().strftime("%Y%m%d")
TODAY_ISO = datetime.now().strftime("%Y-%m-%d")
SCIENCE = "Workflow/Sciences/wa-m10-guilt-scienceextract-v1_0-20260513.md"

BRIEF = Path(f"Sessions/Session_Clusters/M10b/wa-cluster-M10b-phase9-cluster-synthesis-brief-v1-{TODAY}.md")
INPUT = Path(f"Sessions/Session_Clusters/M10b/wa-cluster-M10b-phase9-cluster-synthesis-input-v1-{TODAY}.md")


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

    # Pull all cluster_finding rows for the cluster's characteristics, joined to the
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

    # Sanity: every q_code should have one entry per M10b characteristic
    EXPECTED_CHAR_COUNT = 6
    bad = {qc: len(lst) for qc, lst in by_qcode.items() if len(lst) != EXPECTED_CHAR_COUNT}
    if bad:
        print(f"WARNING: {len(bad)} prompts do not have {EXPECTED_CHAR_COUNT} findings. Sample: {dict(list(bad.items())[:3])}")

    # =====
    # BRIEF
    # =====
    B = []
    B.append(f"# {CLUSTER} Phase 9 — Cluster Synthesis (7th session) — brief")
    B.append("")
    B.append(f"**Cluster:** {CLUSTER} — {cluster['description']}")
    B.append(f"**Session:** 7 (cluster-scope synthesis — final Phase 9 session)")
    B.append(f"**Task date:** {TODAY_ISO}")
    B.append("**Audience:** Claude AI session")
    B.append("")
    char_names = [c['short_name'] for c in chars]
    B.append(f"This is the final Phase 9 session for {CLUSTER}. The {len(chars)} characteristic-scope batches ({', '.join(char_names)}) are complete; each authored 189 findings citing specific verses. This session looks ACROSS those {len(chars)} sets to author the cluster-scope findings — patterns, divergences, and shared anchors that emerge only when they are compared side-by-side.")
    B.append("")
    B.append("**Read this brief first.** Structural input is in a separate file referenced below.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Required inputs")
    B.append("")
    B.append("| # | Document | Purpose |")
    B.append("|---|---|---|")
    B.append(f"| 1 | **This brief** — `Sessions/Session_Clusters/M10b/{BRIEF.name}` | Primary task instructions |")
    B.append(f"| 2 | **Structural input** — `Sessions/Session_Clusters/M10b/{INPUT.name}` | Per-prompt synthesis matrix: for each of the 189 prompts, all {len(chars)} characteristics' findings stacked side-by-side (verbatim from `cluster_finding`); plus open observations |")
    B.append("| 3 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` | §12 Phase 9 disciplines; §12.4 parser-safe form |")
    B.append(f"| 4 | **Science extract** — `{SCIENCE}` (Section 3 only) | Programme-curated scientific lens for T7.3. **Note:** the doc was authored pre-split and covers M10/M10b/M10c siblings; for M10b only Section 3 (Evil/Wickedness) is in scope. Sections 1–2 belong to M10. |")
    B.append("| 5 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260506.md` Ch.1 'Defining Inner Being' | Inner-being scope definition (background) |")
    B.append("| 6 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## What you are producing")
    B.append("")
    B.append(f"For the {CLUSTER} cluster as a whole, two output forms are required (per researcher direction):")
    B.append("")
    B.append("### Output A — 189 cluster-scope findings (parser-safe rows)")
    B.append("")
    B.append(f"For each of the 189 catalogue prompts, author ONE cluster-scope finding examining what surfaces when all {len(chars)} characteristics' findings are compared. The cluster-scope finding answers: *what does the {CLUSTER} cluster — across its {len(chars)} characteristics — reveal about this question?* It is the comparative-integrative layer above the per-characteristic answers.")
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
    B.append(f"- **E** — evidenced; all {len(chars)} characteristics' findings provide enough comparative evidence to author a cluster-scope answer")
    B.append("- **S** — silent; the cluster's combined evidence reveals no meaningful cluster-level pattern beyond the per-char answers")
    B.append(f"- **G** — gap; the cluster-level pattern would require evidence all {len(chars)} characteristics' findings don't supply")
    B.append("")
    B.append("### Output B — Synthesis prose appendix (free-form)")
    B.append("")
    B.append(f"After the 189-row block, write a free-form prose appendix capturing the emergent themes that surface across the {len(chars)} characteristics — themes that the 189-prompt structure does not fully capture. Suggested themes (drawn from M10b's Phase 3 verdicts, Phase 7 polysemy notes, and characteristic-mapping carry-forwards):")
    B.append("")
    B.append("- **The wicked-righteous structural opposite (M26).** Most M10b characteristics define themselves by explicit contrast with the righteous — across Job, Psalms, Proverbs, Sermon on the Mount, Romans. How does the M10b cluster collectively position M26 (Righteousness) as its structural foil? The T6 cross-characteristic findings will have surfaced this; consolidate.")
    B.append("- **The three-part abomination mechanism.** The keyword analytics surfaced a `act defiling + boundary transgressed + divine revulsion` co-occurrence triad across the to.e.vah / shiq.quts / bdelugma corpus. How do CHAR-3 (moral-character abomination) and CHAR-4 (idolatrous abomination) share this mechanism — and where do they diverge?")
    B.append("- **M10b ↔ M27 boundary (idolatry / cosmic-evil / concrete-evil-thing).** M27 is a sibling cluster carrying idolatrous-object + ruin/desolation + cosmic-evil-agent register. M10b carries the *moral-character* side of the same triple-noun. CHAR-4 (idolatrous abomination), CHAR-2's cosmic-evil sub-corpus (M10b-B-VCG-01, INTEGRATION_NOTE #81), and CHAR-1's forensic-verdict sub-corpus (M10b-A-VCG-01, INTEGRATION_NOTE #80) all sit on this seam. Synthesise the cross-cluster pattern.")
    B.append("- **OT vs NT vocabulary arcs.** ra.sha + re.sha + mir.sha.at carry the OT wicked-person tradition (CHAR-1); ponēros + kakia + ponēria + adikia carry the NT constitutional-bent analysis (CHAR-2 + CHAR-6). What does each tradition emphasise that the other does not? Where do they converge?")
    B.append("- **Polysemy hot-spots across the cluster.** Three explicit polysemy splits at Phase 7 VCG level:")
    B.append("  - **a.ven** (CHAR-5): iniquity-scheming agent vs trouble-suffered victim (INTEGRATION_NOTE #82, M03/M27 flag)")
    B.append("  - **ponēros** (CHAR-2): personal-evil-character vs cosmic-evil-agent (INTEGRATION_NOTE #81, M27 flag)")
    B.append("  - **ra.sha** (CHAR-1): inner-moral-character vs forensic-verdict legal-label (INTEGRATION_NOTE #80, M10 flag)")
    B.append("  How does the cluster as a whole carry these polysemies? Are they signs of a coherent inner-being category operating across distinct registers, or signs that the post-split design should be re-examined?")
    B.append("- **The will-conscience-heart triad as the inner location of evil.** The keyword analytics surfaced `will` (193 tokens), `inner` (176), `heart` (89), `conscience` (68) as the dominant locus terms. Trace how each characteristic locates evil — does the same faculty appear across all six, or does each characteristic have a primary inner-locus signature?")
    B.append("- **Blasphemy as the M10b ↔ M06 bridge.** CHAR-6 (Evil expressed through speech) carries blasfēmeō with an M06 (contempt) cross-register flag. The Rev 16 hardened-defiance sub-corpus + Rom 2:24 conduct-causing-others-to-blaspheme illustrate the bridge. How does evil-as-character pass through speech into contempt-against-God territory?")
    B.append("- **Divine response patterns.** `divine revulsion` (14), `divine judgment` (5), `divine rejection` (5), `divine disgust` (5), `divine hatred` (4) are all top keywords. What evidence patterns provoke each response, and how do they differ across the six characteristics?")
    B.append("- **Constitutional vs volitional evil.** CHAR-2 (constitutional inner nature) treats evil as the default output of fallen human nature; CHAR-1 (settled person-identity) treats it as a stable inner alignment by choice and habit; CHAR-5 (active inner scheming) treats it as generated moment-by-moment. Is there a coherent ontology of evil across the six, or three distinct theological accounts?")
    B.append("- **Hardening, suppression, defiance** — the trajectories of moral failure. Top keywords include `conscience suppressed` (8), `will refusing` (9), `will defiant` (6), `hardening` and similar. Where do these trajectories show up across the six characteristics, and what does the evidence say about reversibility vs settled-finality?")
    B.append("- Any **unexpected** cross-characteristic patterns you surface during the 189-row pass (especially in T6 Structural Relationships With Other Characteristics — the per-char T6 findings will already have flagged some).")
    B.append("")
    B.append("Suggested length: 2,000–4,000 words for the appendix. Use sub-headings per theme. Cite the per-characteristic findings (e.g. \"Char 5 T6.1.1's finding that contempt produces pride across 11 exoutheneō verses\") rather than re-citing verses already cited in the structural input.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Discipline")
    B.append("")
    B.append(f"1. **Per-prompt comparative reading.** For each T#.#.# block in §3 of the structural input, read all {len(chars)} characteristics' findings stacked together before authoring the cluster-scope row. The test for a good cluster-scope answer is: *what does seeing all {len(chars)} side-by-side reveal that no single characteristic's answer reveals?*")
    B.append("2. **Cite by characteristic.** The cluster-scope finding names which characteristics contribute what — e.g., \"Humility (Char 1) and Submission (Char 2) co-occur in many verses but with different agencies — Char 1 names the dispositional posture; Char 2 names the volitional act of transgression.\"")
    B.append("3. **Don't restate the per-char findings.** The cluster-scope row is the INTEGRATION across them, not a summary of each.")
    B.append("4. **Fluency is not a quality signal.** Plausible-sounding integration without specific cross-characteristic naming is rejected.")
    B.append("5. **Use [CLUSTER] scope marker only.** Do NOT use [CHAR-N] markers; this is the cluster-scope layer.")
    B.append(f"6. **Honour the open observations.** The {len(observations)} cluster_observation rows (see §2 of structural input) were raised at Phase 8.7 characteristic-mapping time and remain `status='open'` — they flag VCG-level polysemy splits and cross-register signals the Phase 9 Stage A findings should have addressed. Confirm/refine them in your output.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Open cluster observations (status before this session)")
    B.append("")
    B.append(f"All {len(observations)} are status `open` (raised at Phase 8.7; awaiting Stage B confirmation/refinement):")
    B.append("")
    for o in observations:
        char_label = f"Char {o['characteristic_id']}" if o['characteristic_id'] else "Cluster-wide"
        B.append(f"- **#{o['id']} {o['observation_type']}** ({char_label}) — {o['title']}")
    B.append("")
    B.append("Each links to a VCG-level cross-register signal flagged at Phase 7. See §2 of the structural input for full descriptions.")
    B.append("")
    B.append("---")
    B.append("")
    B.append("## Output structure (recommended)")
    B.append("")
    B.append("```markdown")
    B.append(f"# {CLUSTER} Phase 9 — Cluster Synthesis — findings")
    B.append("")
    B.append(f"**Date:** {TODAY_ISO}")
    B.append(f"**Scope:** Cluster {CLUSTER} ({cluster['description']}) — across {len(chars)} characteristics")
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
    B.append(f"1. Save the output as `Sessions/Session_Clusters/M10b/wa-cluster-M10b-phase9-cluster-synthesis-findings-v1-{TODAY}.md`.")
    B.append(f"2. If segmenting by tier-pair: filename pattern `wa-cluster-{CLUSTER}-phase9-cluster-synthesis-findings-seg{{N}}-T#T#-v1-{TODAY}.md` in a sub-folder.")
    B.append(f"3. Ping CC: \"{CLUSTER} cluster synthesis Phase 9 findings ready\".")
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
    S.append(f"{CLUSTER} ({cluster['description']}) holds {len(chars)} inner-being characteristics:")
    S.append("")
    S.append("| Char | Short name | One-line definition |")
    S.append("|---:|---|---|")
    for c in chars:
        defn_short = (c["definition"] or "").split(".")[0]
        S.append(f"| {c['char_seq']} | {c['short_name']} | {defn_short}. |")
    S.append("")
    S.append(f"Each characteristic produced 189 findings in its Phase 9 Stage A batch ({189 * len(chars)} rows total in `cluster_finding`).")
    S.append("")
    S.append("---")
    S.append("")
    # §2 — confirmed observations with resolution notes
    S.append("## §2 — Open cluster observations (raised at Phase 8.7)")
    S.append("")
    S.append(f"These {len(observations)} observations were raised at characteristic-mapping time and link to VCG-level polysemy splits / cross-register signals from Phase 7. All remain `status='open'`; the Stage B synthesis should address each (confirm or refine).")
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
    S.append(f"For each of the 189 prompts (T0.1.1 … T7.3.4), all {len(chars)} characteristics' findings are stacked verbatim below. Read all {len(chars)} before authoring the cluster-scope row in your output.")
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
