"""Generate the AI input framework file for a cluster's Session C publication.

Usage:
    python scripts/_generate_cluster_session_c_framework_v1_20260512.py --cluster M15

Produces one Markdown file with:
  - Front-matter (jargon discipline, citation discipline, tier→theme mapping)
  - Every chapter's structure laid out with explicit AI-WRITE zones
  - Every key verse quoted verbatim
  - Every finding pre-extracted from cluster_finding, grouped by tier and SG
  - Term inventories for every SG (key) and cluster (supportive — BOUNDARY)
  - Appendices fully populated from DB

The output is the input to Claude AI: AI reads this file, writes prose into
every AI-WRITE zone, and returns the file for finalisation.

Read-only against bible_research.db.
"""
import sqlite3, sys, os, argparse, textwrap
from collections import defaultdict
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB_PATH = "database/bible_research.db"

TIER_THEME = {
    "T0": "The divine pattern — what Scripture says about God in this characteristic",
    "T1": "What the characteristic is (definition, name, kind, boundary, modes)",
    "T2": "Where the characteristic lives in the inner person",
    "T3": "Which inner capacities the characteristic engages",
    "T4": "How the characteristic moves — between God and the person, between persons",
    "T5": "How the characteristic is formed, deepens, is tested, is transformed",
    "T6": "How the characteristic relates to other inner characteristics",
    "T7": "The view from outside Scripture — what physical and clinical sciences observe",
}

# Length guidance per chapter (per characteristic where applicable)
LENGTH_GUIDE = {
    "ch1":  "~300-500 words total",
    "ch2":  "~200-300 words per characteristic",
    "ch3":  "~1500-2500 words total (cluster-wide + per-characteristic paragraphs)",
    "ch4":  "~800-1500 words per characteristic",
    "ch5":  "~800-1500 words per characteristic",
    "ch6":  "~400-800 words per characteristic",
    "ch7":  "~400-500 words per characteristic (or grouped)",
    "ch8":  "~200-400 words total",
}


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def fetch_cluster(conn, code):
    r = conn.execute(
        "SELECT * FROM cluster WHERE cluster_code = ?", (code,)
    ).fetchone()
    if not r:
        raise SystemExit(f"Cluster {code} not found")
    return dict(r)


def fetch_subgroups(conn, code):
    """Return list of active sub-groups, ordered by subgroup_code with BOUNDARY last."""
    rows = conn.execute("""
        SELECT * FROM cluster_subgroup
         WHERE cluster_code = ? AND COALESCE(delete_flagged,0)=0
         ORDER BY CASE WHEN subgroup_code='BOUNDARY' THEN 'ZZZZ' ELSE subgroup_code END
    """, (code,)).fetchall()
    return [dict(r) for r in rows]


def fetch_sg_terms(conn, sg_id):
    """Terms placed in this sub-group."""
    rows = conn.execute("""
        SELECT mt.id, mt.strongs_number, mt.transliteration, mt.gloss,
               mt.language, mt.owning_word, mt.anchor_note,
               mts.placement_note
          FROM mti_term_subgroup mts
          JOIN mti_terms mt ON mt.id = mts.mti_term_id
         WHERE mts.cluster_subgroup_id = ?
           AND COALESCE(mts.delete_flagged,0)=0
           AND COALESCE(mt.delete_flagged,0)=0
         ORDER BY mt.language DESC, mt.strongs_number
    """, (sg_id,)).fetchall()
    return [dict(r) for r in rows]


def fetch_sg_vcgs_with_anchors(conn, sg_id, cluster_code):
    """Returns ordered list of {vcg_dict, anchor_verses: [...]}."""
    vcgs = conn.execute(f"""
        SELECT DISTINCT vcg.id, vcg.group_code, vcg.context_description
          FROM verse_context_group vcg
          JOIN verse_context vc ON vc.group_id = vcg.id
         WHERE vc.cluster_subgroup_id = ?
           AND vcg.group_code LIKE ?
           AND COALESCE(vcg.delete_flagged,0)=0
           AND COALESCE(vc.delete_flagged,0)=0
         ORDER BY vcg.group_code
    """, (sg_id, f"{cluster_code}-%-VCG%")).fetchall()
    out = []
    for vcg in vcgs:
        anchors = conn.execute("""
            SELECT vc.id AS vc_id, vc.analysis_note, vc.notes,
                   vr.reference, vr.verse_text, vr.testament,
                   mt.strongs_number, mt.transliteration, mt.gloss, mt.language
              FROM verse_context vc
              JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
              JOIN mti_terms mt ON mt.id = vc.mti_term_id
             WHERE vc.group_id = ? AND vc.is_anchor = 1
               AND COALESCE(vc.delete_flagged,0)=0
             ORDER BY vr.book_id, vr.chapter, vr.verse_num
        """, (vcg["id"],)).fetchall()
        out.append({"vcg": dict(vcg), "anchors": [dict(a) for a in anchors]})
    return out


def fetch_findings(conn, cluster_code):
    """All findings for cluster, joined to catalogue. Returns dict keyed by (sg_id, tier)."""
    rows = conn.execute("""
        SELECT cf.id AS cf_id, cf.cluster_subgroup_id AS sg_id,
               cf.finding_status, cf.finding_text, cf.notes,
               q.question_code, q.tier, q.section,
               q.component_code, q.component_title, q.question_text
          FROM cluster_finding cf
          JOIN wa_obs_question_catalogue q ON q.obs_id = cf.obs_id
         WHERE cf.cluster_code = ?
           AND COALESCE(cf.delete_flagged,0)=0
         ORDER BY q.question_code, cf.id
    """, (cluster_code,)).fetchall()
    by_sg_tier = defaultdict(list)
    cluster_syn = defaultdict(list)   # by tier, for sg_id IS NULL
    gaps = []
    silents_by_sg_tier = defaultdict(list)
    for r in rows:
        d = dict(r)
        if d["finding_status"] == "cluster_synthesis":
            cluster_syn[d["tier"]].append(d)
        elif d["finding_status"] == "gap":
            gaps.append(d)
        elif d["finding_status"] == "silent":
            silents_by_sg_tier[(d["sg_id"], d["tier"])].append(d)
        else:
            by_sg_tier[(d["sg_id"], d["tier"])].append(d)
    return {
        "by_sg_tier": by_sg_tier,
        "cluster_syn": cluster_syn,
        "gaps": gaps,
        "silents_by_sg_tier": silents_by_sg_tier,
    }


# ---------- Markdown helpers ----------

def header(level, text):
    return f"{'#' * level} {text}\n"


def evidence_block(title, body, kind="EVIDENCE"):
    fence = "<!-- " + kind + ": " + title + " -->\n"
    end = "<!-- /" + kind + " -->\n"
    return fence + body + ("\n" if not body.endswith("\n") else "") + end


def ai_write(zone_id, focus, length, cite_verses=None, avoid=None, source_note=None):
    lines = [
        f"<!-- AI WRITE: {zone_id}",
        f"     LENGTH: {length}",
    ]
    if focus:
        lines.append(f"     FOCUS: {focus}")
    if cite_verses:
        v = "; ".join(cite_verses)
        lines.append(f"     CITE (must quote at least 2 verbatim): {v}")
    if source_note:
        lines.append(f"     SOURCE: {source_note}")
    if avoid:
        lines.append(f"     AVOID: {avoid}")
    lines.append("-->")
    return "\n".join(lines) + "\n"


def format_findings_block(findings, label):
    if not findings:
        return f"_No findings of type {label}._\n"
    lines = []
    by_section = defaultdict(list)
    for f in findings:
        by_section[f.get("section") or "(unsectioned)"].append(f)
    for section, items in by_section.items():
        lines.append(f"\n**{section}**\n")
        for f in items:
            qcode = f.get("question_code", "")
            qtext = f.get("question_text") or ""
            ftxt = f.get("finding_text") or ""
            qtext_short = qtext[:140] + ("…" if len(qtext) > 140 else "")
            lines.append(f"- *{qcode}* — _{qtext_short}_")
            lines.append(f"  → {ftxt.strip()}")
    return "\n".join(lines) + "\n"


def format_term_table(terms, label="Terms"):
    if not terms:
        return f"_No terms in this layer._\n"
    out = [f"| Strong's | Hebrew/Greek | Translit. | Gloss | Owning word |",
           f"|---|---|---|---|---|"]
    for t in terms:
        gloss = (t.get("gloss") or "")[:80].replace("|", "\\|")
        translit = (t.get("transliteration") or "").replace("|", "\\|")
        owning = (t.get("owning_word") or "").replace("|", "\\|")
        lang = t.get("language") or ""
        lang_disp = "H" if lang.lower().startswith("h") else ("G" if lang.lower().startswith("g") else lang)
        out.append(f"| {t['strongs_number']} | {lang_disp} | {translit} | {gloss} | {owning} |")
    return "\n".join(out) + "\n"


def format_anchor(anchor, vcg_code=None):
    ref = anchor.get("reference", "")
    verse_text = (anchor.get("verse_text") or "").strip()
    translit = anchor.get("transliteration", "")
    strongs = anchor.get("strongs_number", "")
    note = anchor.get("analysis_note") or ""
    lines = [f"**{ref}** ({strongs} {translit})"]
    if vcg_code:
        lines[-1] += f" [{vcg_code}]"
    lines.append(f"> {verse_text}")
    if note:
        lines.append(f"_Meaning of the term here:_ {note}")
    return "\n".join(lines) + "\n"


# ---------- Section builders ----------

def build_front_matter(cluster):
    title = cluster.get("description") or cluster.get("short_name")
    out = []
    out.append(f"# {title}\n")
    out.append(f"_A study of how Scripture treats the inner life of {cluster.get('short_name','').lower()}_\n\n")
    out.append("---\n\n")
    out.append("<!-- BEGIN FRAMEWORK PREAMBLE — strip on finalisation -->\n\n")
    out.append("## Author's brief (for the AI writing this study)\n\n")
    out.append(
        "This is the framework for a plain-English published study of a family of related "
        "inner-being characteristics from Scripture. You are writing for an intelligent "
        "reader who has no familiarity with this project's analytical vocabulary. Every "
        "AI-WRITE zone below carries length, focus, citation, and avoid instructions. "
        "Read each zone's instructions carefully and write directly into the zone in place "
        "of its current placeholder.\n\n"
    )
    out.append("### Words to avoid in the published prose\n\n")
    out.append(
        "| Avoid | Use instead |\n"
        "|---|---|\n"
        "| cluster | \"this study\", \"these related characteristics\" |\n"
        "| sub-group | \"characteristic\", \"facet\", \"form\" |\n"
        "| VCG / verse context group | \"meaning group\" (rare) or describe inline |\n"
        "| anchor verse | \"key verse\", \"central verse\" |\n"
        "| finding | \"what the evidence shows\", \"the pattern\" |\n"
        "| tier / T0 / T1 … | thematic names (see below) |\n"
        "| catalogue prompt | not exposed |\n"
        "| constitutional location | \"where this lives in the inner person\" |\n"
        "| inner faculty | \"the inner capacity\" |\n"
        "| sub-group code / VCG code | not in prose (appendix only if at all) |\n"
        "| domain, findings | not exposed |\n\n"
    )
    out.append("### Citation discipline\n\n")
    out.append(
        "Every analytical claim must be grounded by a quoted verse. When making a claim:\n"
        "1. Name the verse in the prose (biblical citation, e.g. \"as Pro 16:23 makes plain…\")\n"
        "2. Quote it verbatim, inline or in an indented block\n"
        "3. Where the meaning-group context matters, name it (e.g. \"in the verses where "
        "wisdom is named as God's own attribute…\")\n"
        "Never cite finding-id, tier code, VCG code, or prompt code in the prose. The "
        "framework provides verse text inline for every key verse you should quote.\n\n"
    )
    out.append("### Thematic names for analytical lenses\n\n")
    out.append("| Internal code (do NOT use in prose) | Thematic lens (you may use this language) |\n|---|---|\n")
    for code, theme in TIER_THEME.items():
        out.append(f"| {code} | {theme} |\n")
    out.append("\n")
    out.append("<!-- END FRAMEWORK PREAMBLE -->\n\n---\n\n")
    return "".join(out)


def build_ch1(cluster, subgroups, findings):
    out = []
    out.append("## 1. What this study is\n\n")
    out.append(ai_write(
        zone_id="Chapter 1 opening prose",
        length=LENGTH_GUIDE["ch1"],
        focus=(
            "Name what these characteristics are, what they cover together, why they "
            "belong together, what they share, how they depend on each other. End with "
            "a one-sentence preview of what follows."
        ),
        source_note=(
            "T0 + T1 cluster-synthesis findings below; the characteristic labels and "
            "their core descriptions in Chapter 2; the divine-image pattern that runs "
            "across the whole study."
        ),
        avoid="all jargon in the table above",
    ))
    out.append("\n**Evidence: cluster-wide claims from the analytical record**\n\n")
    syn_T0 = findings["cluster_syn"].get("T0", [])
    syn_T1 = findings["cluster_syn"].get("T1", [])
    out.append(evidence_block(
        "Ch1 — T0 cluster-synthesis findings",
        format_findings_block(syn_T0, "T0 cluster-synthesis"),
    ))
    out.append("\n")
    out.append(evidence_block(
        "Ch1 — T1 cluster-synthesis findings",
        format_findings_block(syn_T1, "T1 cluster-synthesis"),
    ))
    out.append("\n**Evidence: the characteristics being studied (orientation only)**\n\n")
    sg_orient = []
    for sg in subgroups:
        if sg["subgroup_code"] == "BOUNDARY":
            continue
        sg_orient.append(f"- **{sg['label']}** — {sg.get('core_description') or '(description pending)'}")
    out.append(evidence_block(
        "Ch1 — characteristic labels and brief descriptions",
        "\n".join(sg_orient) + "\n",
    ))
    out.append("\n---\n\n")
    return "".join(out)


def build_ch2(cluster, subgroups, sg_terms_map, sg_vcgs_map):
    out = []
    out.append("## 2. The characteristics in this study\n\n")
    out.append(ai_write(
        zone_id="Chapter 2 opening (1-2 sentences)",
        length="~50-80 words",
        focus=(
            "Brief opening saying that the Bible's vocabulary for this inner-life "
            "domain organises into N related characteristics, each a distinct way the "
            "inner person manifests this aspect of inner life."
        ),
        source_note="The N below is the count of non-BOUNDARY characteristics.",
        avoid="jargon",
    ))
    out.append("\n")
    sec_index = 0
    non_boundary = [sg for sg in subgroups if sg["subgroup_code"] != "BOUNDARY"]
    boundary = [sg for sg in subgroups if sg["subgroup_code"] == "BOUNDARY"]
    for sg in non_boundary:
        sec_index += 1
        out.append(f"### 2.{sec_index} {sg['label']}\n\n")
        out.append(ai_write(
            zone_id=f"Chapter 2 §2.{sec_index} ({sg['label']})",
            length=LENGTH_GUIDE["ch2"],
            focus=(
                f"Describe this characteristic in plain English. Name it, characterise it, "
                f"and say how it differs from the others in this study. Use one or two key "
                f"verses to anchor the description."
            ),
            cite_verses=_first_n_anchor_refs(sg_vcgs_map.get(sg["id"], []), n=2),
            source_note="Sub-group description and key verses below.",
            avoid="jargon",
        ))
        out.append("\n**Sub-group description (from analytical record):**\n\n")
        out.append(f"> {sg.get('core_description') or '_(description pending)_'}\n\n")
        out.append("**Key verses for this characteristic:**\n\n")
        for vcg_entry in sg_vcgs_map.get(sg["id"], []):
            for a in vcg_entry["anchors"]:
                out.append(format_anchor(a, vcg_code=vcg_entry["vcg"]["group_code"]))
                out.append("\n")
        out.append("\n")
    # BOUNDARY treatment
    if boundary:
        sec_index += 1
        out.append(f"### 2.{sec_index} Supporting characteristics\n\n")
        out.append(ai_write(
            zone_id=f"Chapter 2 §2.{sec_index} (Supporting characteristics)",
            length="~150 words",
            focus=(
                "Briefly acknowledge a set of supporting characteristics that play a part "
                "in this inner-life domain without themselves being inner-being "
                "characteristics. Note that they are not treated at full depth in chapters "
                "4-7."
            ),
            source_note="BOUNDARY description and terms below.",
            avoid="jargon",
        ))
        out.append("\n**Description of supporting characteristics:**\n\n")
        for sg in boundary:
            out.append(f"> {sg.get('core_description') or '_(description pending)_'}\n\n")
    out.append("\n---\n\n")
    return "".join(out)


def _first_n_anchor_refs(vcg_entries, n=2):
    refs = []
    for vcg_entry in vcg_entries:
        for a in vcg_entry["anchors"]:
            refs.append(a["reference"])
            if len(refs) >= n:
                return refs
    return refs


def build_ch3(cluster, subgroups, sg_vcgs_map, findings):
    out = []
    out.append("## 3. The divine pattern\n\n")
    out.append(ai_write(
        zone_id="Chapter 3 cluster-wide spine",
        length=LENGTH_GUIDE["ch3"],
        focus=(
            "Write the cluster-wide arc on how Scripture attributes these characteristics "
            "to God. Then, for each non-BOUNDARY characteristic in turn, write a short "
            "paragraph (1-3 sentences) noting where its divine treatment differs from the "
            "cluster-wide pattern. Where Scripture is silent on God in a particular "
            "characteristic, name that silence as itself meaningful."
        ),
        source_note="T0 cluster-synthesis below, then T0 per-characteristic blocks.",
        avoid="jargon",
    ))
    out.append("\n**Evidence: T0 cluster-synthesis (the cluster-wide pattern)**\n\n")
    out.append(evidence_block(
        "Ch3 — T0 cluster-synthesis findings",
        format_findings_block(findings["cluster_syn"].get("T0", []), "T0 cluster-synthesis"),
    ))
    out.append("\n**Evidence per characteristic: T0 findings**\n\n")
    for sg in subgroups:
        if sg["subgroup_code"] == "BOUNDARY":
            continue
        out.append(f"\n#### {sg['label']}\n\n")
        sg_t0 = findings["by_sg_tier"].get((sg["id"], "T0"), [])
        sg_t0_silent = findings["silents_by_sg_tier"].get((sg["id"], "T0"), [])
        out.append(evidence_block(
            f"Ch3 — T0 findings for {sg['label']}",
            format_findings_block(sg_t0, "T0 sub-group"),
        ))
        if sg_t0_silent:
            out.append("\n_Silences:_\n\n")
            out.append(evidence_block(
                f"Ch3 — T0 silences for {sg['label']}",
                format_findings_block(sg_t0_silent, "T0 silent"),
            ))
        # Key T0 anchor verses (the "God's own attribute" verses, typically VCG01)
        out.append("\n_T0-related key verses:_\n\n")
        for vcg_entry in sg_vcgs_map.get(sg["id"], []):
            code = vcg_entry["vcg"]["group_code"]
            # Heuristic: VCG01 is typically the divine-image VCG; include first 1-2 anchors
            if code.endswith("VCG01") or code.endswith("VCG02"):
                for a in vcg_entry["anchors"][:2]:
                    out.append(format_anchor(a, vcg_code=code))
                    out.append("\n")
    out.append("\n---\n\n")
    return "".join(out)


def build_chapter_per_sg(chapter_num, title, tiers, length_key, subgroups, sg_vcgs_map, findings, focus_text, anchor_filter=None):
    out = []
    out.append(f"## {chapter_num}. {title}\n\n")
    out.append(ai_write(
        zone_id=f"Chapter {chapter_num} opening (1-2 sentences)",
        length="~40-80 words",
        focus="Brief opening framing what this chapter covers, without naming the analytical lens by code.",
        avoid="jargon",
    ))
    out.append("\n")
    sec_index = 0
    non_boundary = [sg for sg in subgroups if sg["subgroup_code"] != "BOUNDARY"]
    for sg in non_boundary:
        sec_index += 1
        out.append(f"### {chapter_num}.{sec_index} {sg['label']}\n\n")
        # Build cite_verses list: take first 3-4 anchor refs across SG's VCGs
        cite = _first_n_anchor_refs(sg_vcgs_map.get(sg["id"], []), n=4)
        out.append(ai_write(
            zone_id=f"Chapter {chapter_num} §{chapter_num}.{sec_index} ({sg['label']})",
            length=LENGTH_GUIDE[length_key],
            focus=focus_text,
            cite_verses=cite,
            source_note=f"All evidence for this characteristic on this lens is in the blocks below.",
            avoid="jargon; do not cite finding-id, tier code, or VCG code in the prose",
        ))
        out.append("\n")
        # Findings per tier for this SG
        for tier in tiers:
            sg_findings = findings["by_sg_tier"].get((sg["id"], tier), [])
            sg_silent = findings["silents_by_sg_tier"].get((sg["id"], tier), [])
            if sg_findings:
                out.append(evidence_block(
                    f"Ch{chapter_num} — {tier} findings for {sg['label']}",
                    format_findings_block(sg_findings, f"{tier} sub-group"),
                ))
                out.append("\n")
            if sg_silent:
                out.append(evidence_block(
                    f"Ch{chapter_num} — {tier} silences for {sg['label']}",
                    format_findings_block(sg_silent, f"{tier} silent"),
                ))
                out.append("\n")
        # Key verses for this SG
        out.append(f"\n**Key verses for {sg['label']}:**\n\n")
        for vcg_entry in sg_vcgs_map.get(sg["id"], []):
            for a in vcg_entry["anchors"]:
                out.append(format_anchor(a, vcg_code=vcg_entry["vcg"]["group_code"]))
                out.append("\n")
        out.append("\n")
    out.append("\n---\n\n")
    return "".join(out)


def build_ch7(subgroups, sg_vcgs_map, findings):
    out = []
    out.append("## 7. The view from outside Scripture\n\n")
    out.append(ai_write(
        zone_id="Chapter 7 opening note",
        length="~80-120 words",
        focus=(
            "Brief opening that names the purpose of this chapter — a short reflection on "
            "what human and clinical sciences observe about the corresponding inner "
            "capacities (cognition, perception, knowledge representation, executive "
            "function, default-mode reflection, working memory, language processing). "
            "Explicitly acknowledge that this view-from-outside is under-developed in the "
            "analytical record at present and is earmarked for future expansion."
        ),
        avoid="jargon",
    ))
    out.append("\n")
    sec_index = 0
    non_boundary = [sg for sg in subgroups if sg["subgroup_code"] != "BOUNDARY"]
    for sg in non_boundary:
        sec_index += 1
        out.append(f"### 7.{sec_index} {sg['label']}\n\n")
        out.append(ai_write(
            zone_id=f"Chapter 7 §7.{sec_index} ({sg['label']})",
            length=LENGTH_GUIDE["ch7"],
            focus=(
                f"Short overview of what human / clinical sciences observe about the human "
                f"capacity corresponding to {sg['label']}. Reflect on (a) synergies with "
                f"the biblical picture, (b) gaps where science is silent on what Scripture "
                f"emphasises, (c) differences where the scientific framing diverges from the "
                f"biblical framing. Use general scientific knowledge — the analytical record "
                f"is thin on this lens. Note explicitly where the record offers no view-from-"
                f"outside material."
            ),
            source_note="T7 findings below (sparse).",
            avoid="jargon; do not overclaim — be explicit where the analytical record is silent",
        ))
        out.append("\n")
        sg_t7 = findings["by_sg_tier"].get((sg["id"], "T7"), [])
        sg_t7_silent = findings["silents_by_sg_tier"].get((sg["id"], "T7"), [])
        out.append(evidence_block(
            f"Ch7 — T7 findings for {sg['label']}",
            format_findings_block(sg_t7, "T7"),
        ))
        if sg_t7_silent:
            out.append("\n")
            out.append(evidence_block(
                f"Ch7 — T7 silences for {sg['label']}",
                format_findings_block(sg_t7_silent, "T7 silent"),
            ))
        out.append("\n")
    out.append("\n---\n\n")
    return "".join(out)


def build_ch8(findings):
    out = []
    out.append("## 8. What this study does not yet address\n\n")
    out.append(ai_write(
        zone_id="Chapter 8 honest accounting",
        length=LENGTH_GUIDE["ch8"],
        focus=(
            "Write honest plain-English accounting of (a) the gaps named in the analytical "
            "record, (b) the meaningful silences in the verse evidence, (c) the view-from-"
            "outside being under-developed, and (d) any LXX / Greek-of-the-Hebrew work that "
            "remains parked for a future research session."
        ),
        source_note="Gap findings below; silent findings are summarised across chapters; LXX gap noted in the standard programme."
    ))
    out.append("\n**Evidence: gap findings**\n\n")
    out.append(evidence_block(
        "Ch8 — gap findings (cluster-wide)",
        format_findings_block(findings.get("gaps", []), "gap"),
    ))
    out.append("\n---\n\n")
    return "".join(out)


def build_app_a(subgroups, sg_terms_map):
    out = []
    out.append("## Appendix A — Terms in this study\n\n")
    out.append(ai_write(
        zone_id="Appendix A opening (1 sentence)",
        length="~30 words",
        focus="One sentence framing the appendix as the term inventory underlying the study.",
        avoid="jargon",
    ))
    out.append("\n")
    sec_index = 0
    non_boundary = [sg for sg in subgroups if sg["subgroup_code"] != "BOUNDARY"]
    boundary = [sg for sg in subgroups if sg["subgroup_code"] == "BOUNDARY"]
    for sg in non_boundary:
        sec_index += 1
        terms = sg_terms_map.get(sg["id"], [])
        out.append(f"### A.{sec_index} {sg['label']} — key terms\n\n")
        out.append(format_term_table(terms))
        out.append("\n")
        out.append(ai_write(
            zone_id=f"Appendix A.{sec_index} commentary",
            length="~60-120 words",
            focus=(
                "Briefly characterise what these terms together name in this study. "
                "Say something about the breakdown between Hebrew and Greek vocabulary if "
                "notable. Do not list the terms again — comment on what they reveal as a group."
            ),
            avoid="jargon",
        ))
        out.append("\n")
    # BOUNDARY = supportive
    if boundary:
        sec_index += 1
        out.append(f"### A.{sec_index} Supportive terms across this study\n\n")
        out.append("These terms appear in the verse evidence supporting the study but do not themselves carry one of the core characteristics.\n\n")
        for sg in boundary:
            terms = sg_terms_map.get(sg["id"], [])
            out.append(format_term_table(terms))
            out.append("\n")
    out.append("\n---\n\n")
    return "".join(out)


def build_app_b(subgroups, sg_vcgs_map):
    out = []
    out.append("## Appendix B — Key verses\n\n")
    out.append("This table covers every key verse cited in the chapters above.\n\n")
    out.append("| Characteristic | Meaning-group | Reference | Strong's | Translit. | Verse text | Meaning of the term in this study |\n")
    out.append("|---|---|---|---|---|---|---|\n")
    for sg in subgroups:
        for vcg_entry in sg_vcgs_map.get(sg["id"], []):
            mg_code = vcg_entry["vcg"]["group_code"]
            mg_desc = (vcg_entry["vcg"].get("context_description") or "").replace("|", "\\|")
            mg_short = mg_desc[:80] + ("…" if len(mg_desc) > 80 else "")
            for a in vcg_entry["anchors"]:
                strongs = a.get("strongs_number") or ""
                translit = (a.get("transliteration") or "").replace("|", "\\|")
                ref = a.get("reference") or ""
                vt = (a.get("verse_text") or "").replace("|", "\\|").replace("\n", " ").strip()
                vt_short = vt[:180] + ("…" if len(vt) > 180 else "")
                meaning = (a.get("analysis_note") or "").replace("|", "\\|")
                if not meaning:
                    meaning = "_AI to fill from meaning-group context_"
                out.append(
                    f"| {sg['label']} | {mg_short} | {ref} | {strongs} | {translit} | {vt_short} | {meaning} |\n"
                )
    out.append("\n---\n\n")
    return "".join(out)


def build_app_c(cluster, findings):
    out = []
    out.append("## Appendix C — Method note\n\n")
    out.append(ai_write(
        zone_id="Appendix C method note",
        length="~150 words",
        focus=(
            "Plain-English paragraph acknowledging that the study draws from a structured "
            "analytical record covering the verse evidence for each characteristic, with key "
            "verses selected as evidential foundation. No claim in the chapters above is made "
            "without specific verse evidence behind it. Note the cluster status and version "
            "from the metadata below."
        ),
        avoid="jargon; do not name 'cluster' or 'tier' or 'finding' as terms",
    ))
    out.append("\n")
    out.append(evidence_block(
        "App C — Cluster metadata",
        f"- Cluster code: {cluster['cluster_code']}\n"
        f"- Short name: {cluster.get('short_name')}\n"
        f"- Description: {cluster.get('description')}\n"
        f"- Status: {cluster.get('status')}\n"
        f"- Version: {cluster.get('version')}\n"
        f"- Last updated: {cluster.get('last_updated_date')}\n"
        f"- Total findings underlying this study: "
        f"{sum(len(v) for v in findings['by_sg_tier'].values()) + sum(len(v) for v in findings['cluster_syn'].values()) + len(findings['gaps']) + sum(len(v) for v in findings['silents_by_sg_tier'].values())}\n"
    ))
    return "".join(out)


# ---------- Main ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True, help="Cluster code, e.g. M15")
    ap.add_argument("--out", default=None, help="Output path. Default: Sessions/Session_Clusters/{CODE}/wa-cluster-{CODE}-publication-framework-v1-{date}.md")
    args = ap.parse_args()

    code = args.cluster
    out_path = args.out
    if not out_path:
        from datetime import datetime
        d = datetime.now().strftime("%Y%m%d")
        out_path = f"Sessions/Session_Clusters/{code}/wa-cluster-{code}-publication-framework-v1-{d}.md"

    conn = get_conn()
    cluster = fetch_cluster(conn, code)
    subgroups = fetch_subgroups(conn, code)
    sg_terms_map = {sg["id"]: fetch_sg_terms(conn, sg["id"]) for sg in subgroups}
    sg_vcgs_map = {sg["id"]: fetch_sg_vcgs_with_anchors(conn, sg["id"], code) for sg in subgroups}
    findings = fetch_findings(conn, code)

    # Build pieces
    parts = []
    parts.append(build_front_matter(cluster))
    parts.append(build_ch1(cluster, subgroups, findings))
    parts.append(build_ch2(cluster, subgroups, sg_terms_map, sg_vcgs_map))
    parts.append(build_ch3(cluster, subgroups, sg_vcgs_map, findings))
    parts.append(build_chapter_per_sg(
        4, "Where each characteristic lives in the person",
        tiers=["T2", "T3"], length_key="ch4",
        subgroups=subgroups, sg_vcgs_map=sg_vcgs_map, findings=findings,
        focus_text=(
            "Write a deep-dive on where in the inner person this characteristic sits "
            "(heart, mind, will, conscience, soul, spirit, faculty, body) and which inner "
            "capacities it engages (perception, thought, memory, feeling, conscience, will, "
            "agency). Use the evidence below. Quote the key verses verbatim where they "
            "carry the claim."
        ),
    ))
    parts.append(build_chapter_per_sg(
        5, "How each characteristic works",
        tiers=["T4", "T5", "T1"], length_key="ch5",
        subgroups=subgroups, sg_vcgs_map=sg_vcgs_map, findings=findings,
        focus_text=(
            "Write on how this characteristic moves — between God and the human person, "
            "between persons, in covenant, against opposition — and how it is formed, "
            "deepens, is tested, is transformed across time. Use the evidence below."
        ),
    ))
    parts.append(build_chapter_per_sg(
        6, "How each characteristic relates to the others",
        tiers=["T6"], length_key="ch6",
        subgroups=subgroups, sg_vcgs_map=sg_vcgs_map, findings=findings,
        focus_text=(
            "Write on this characteristic's relationship to other inner characteristics — "
            "what it is paired with, what it is opposed by, what produces it, what it "
            "itself produces. Use the evidence below."
        ),
    ))
    parts.append(build_ch7(subgroups, sg_vcgs_map, findings))
    parts.append(build_ch8(findings))
    parts.append(build_app_a(subgroups, sg_terms_map))
    parts.append(build_app_b(subgroups, sg_vcgs_map))
    parts.append(build_app_c(cluster, findings))

    md = "".join(parts)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Wrote: {out_path}")
    print(f"Size: {len(md):,} chars  (~{len(md.split()):,} words)")
    # Quick stats
    sg_count = len([sg for sg in subgroups if sg["subgroup_code"] != "BOUNDARY"])
    anchor_count = sum(len(v["anchors"]) for vlist in sg_vcgs_map.values() for v in vlist)
    finding_count = (sum(len(v) for v in findings["by_sg_tier"].values())
                     + sum(len(v) for v in findings["cluster_syn"].values())
                     + len(findings["gaps"])
                     + sum(len(v) for v in findings["silents_by_sg_tier"].values()))
    print(f"Characteristics: {sg_count} (+ BOUNDARY)")
    print(f"Anchor verses:   {anchor_count}")
    print(f"Findings loaded: {finding_count}")
    conn.close()


if __name__ == "__main__":
    main()
