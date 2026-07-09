"""Generate per-chapter AI input files for a cluster's Session C publication.

Splits the monolithic framework approach into one input file per chapter.
Each input file is self-contained:
  - Preamble pointing to shared style/method instruction and this chapter's instruction
  - Brief profile of every characteristic (for cross-chapter consistency)
  - Only the evidence this chapter needs
  - AI-WRITE zones for this chapter's sections

Usage:
    python scripts/_generate_cluster_session_c_inputs_v2_20260512.py --cluster M15
    python scripts/_generate_cluster_session_c_inputs_v2_20260512.py --cluster M15 --chapter 4
    python scripts/_generate_cluster_session_c_inputs_v2_20260512.py --cluster M15 --only ch4,ch5

Outputs to: Sessions/Session_Clusters/{CODE}/inputs/wa-cluster-{CODE}-ch{N}-input-v1-{date}.md
"""
import sqlite3, sys, os, re, argparse
from collections import defaultdict
from datetime import datetime
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB_PATH = "database/bible_research.db"


# ---------- DB layer ----------

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def fetch_cluster(conn, code):
    r = conn.execute("SELECT * FROM cluster WHERE cluster_code = ?", (code,)).fetchone()
    if not r:
        raise SystemExit(f"Cluster {code} not found")
    return dict(r)


def fetch_subgroups(conn, code):
    rows = conn.execute("""
        SELECT * FROM cluster_subgroup
         WHERE cluster_code = ? AND COALESCE(delete_flagged,0)=0
         ORDER BY CASE WHEN subgroup_code='BOUNDARY' THEN 'ZZZZ' ELSE subgroup_code END
    """, (code,)).fetchall()
    return [dict(r) for r in rows]


def fetch_sg_terms(conn, sg_id):
    rows = conn.execute("""
        SELECT mt.id, mt.strongs_number, mt.transliteration, mt.gloss,
               mt.language, mt.owning_word, mt.anchor_note, mts.placement_note
          FROM mti_term_subgroup mts
          JOIN mti_terms mt ON mt.id = mts.mti_term_id
         WHERE mts.cluster_subgroup_id = ?
           AND COALESCE(mts.delete_flagged,0)=0
           AND COALESCE(mt.delete_flagged,0)=0
         ORDER BY mt.language DESC, mt.strongs_number
    """, (sg_id,)).fetchall()
    return [dict(r) for r in rows]


def fetch_sg_vcgs_with_anchors(conn, sg_id, cluster_code):
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
    # v3_0 model: per-characteristic findings keyed by characteristic_id, mapped
    # to cluster_subgroup_id via characteristic_subgroup link table.
    # Legacy model: keyed by cluster_subgroup_id directly.
    # COALESCE both so per-char and per-sg findings land in the same sg_id-keyed
    # buckets the rest of the generator expects.
    rows = conn.execute("""
        SELECT cf.id AS cf_id,
               COALESCE(cf.cluster_subgroup_id, cs.cluster_subgroup_id) AS sg_id,
               cf.finding_status, cf.finding_text, cf.notes,
               q.question_code, q.tier, q.section,
               q.component_code, q.component_title, q.question_text
          FROM cluster_finding cf
          JOIN wa_obs_question_catalogue q ON q.obs_id = cf.obs_id
          LEFT JOIN characteristic_subgroup cs
            ON cs.characteristic_id = cf.characteristic_id
           AND COALESCE(cs.delete_flagged, 0) = 0
         WHERE cf.cluster_code = ?
           AND COALESCE(cf.delete_flagged,0)=0
         ORDER BY q.question_code, cf.id
    """, (cluster_code,)).fetchall()
    by_sg_tier = defaultdict(list)
    cluster_syn = defaultdict(list)
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


# ---------- Formatting helpers ----------

def fmt_findings(findings, label):
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


def fmt_anchor(anchor, vcg_code=None):
    ref = anchor.get("reference", "")
    verse_text = (anchor.get("verse_text") or "").strip()
    translit = anchor.get("transliteration", "")
    strongs = anchor.get("strongs_number", "")
    note = anchor.get("analysis_note") or ""
    lines = [f"**{ref}** ({strongs} {translit})" + (f" [{vcg_code}]" if vcg_code else "")]
    lines.append(f"> {verse_text}")
    if note:
        lines.append(f"_Meaning of the term here:_ {note}")
    return "\n".join(lines) + "\n"


def fmt_term_table(terms):
    if not terms:
        return "_No terms._\n"
    out = ["| Strong's | H/G | Translit. | Gloss | Owning word |",
           "|---|---|---|---|---|"]
    for t in terms:
        gloss = (t.get("gloss") or "")[:80].replace("|", "\\|")
        translit = (t.get("transliteration") or "").replace("|", "\\|")
        owning = (t.get("owning_word") or "").replace("|", "\\|")
        lang = t.get("language") or ""
        lang_disp = "H" if lang.lower().startswith("h") else ("G" if lang.lower().startswith("g") else "")
        out.append(f"| {t['strongs_number']} | {lang_disp} | {translit} | {gloss} | {owning} |")
    return "\n".join(out) + "\n"


def ai_write_zone(zone_id, focus, length, cite_verses=None, source_note=None, avoid="all jargon from the shared instruction's avoid-list"):
    lines = [
        f"<!-- AI WRITE: {zone_id}",
        f"     LENGTH: {length}",
        f"     FOCUS: {focus}",
    ]
    if cite_verses:
        v = "; ".join(cite_verses)
        lines.append(f"     CITE (must quote verbatim, minimum 2): {v}")
    if source_note:
        lines.append(f"     SOURCE: {source_note}")
    lines.append(f"     AVOID: {avoid}")
    lines.append("-->")
    lines.append("")
    lines.append("_[AI: replace this placeholder and the marker above with finished prose.]_")
    lines.append("")
    return "\n".join(lines) + "\n"


def evidence_block(title, body):
    return f"<!-- EVIDENCE: {title} -->\n{body}{'' if body.endswith(chr(10)) else chr(10)}<!-- /EVIDENCE -->\n"


def first_n_refs(vcg_entries, n=3):
    refs = []
    for vcg_entry in vcg_entries:
        for a in vcg_entry["anchors"]:
            refs.append(a["reference"])
            if len(refs) >= n:
                return refs
    return refs


# ---------- Preamble blocks shared across chapter inputs ----------

def chapter_preamble(cluster, chapter_num, chapter_title, instruction_doc, subgroups):
    short = cluster.get("short_name") or cluster["cluster_code"]
    desc = cluster.get("description") or short
    out = []
    out.append(f"# {desc} — Chapter {chapter_num} input\n")
    out.append(f"## {chapter_title}\n\n")
    out.append(f"**Cluster:** {cluster['cluster_code']} ({short})\n")
    out.append(f"**Chapter:** {chapter_num} — {chapter_title}\n")
    out.append(f"**Style and method:** [wa-sessionc-cluster-style-method-v1_1-20260512.md](../../../Workflow/Instructions/wa-sessionc-cluster-style-method-v1_1-20260512.md)\n")
    out.append(f"**Chapter instruction:** [{instruction_doc}](../../../Workflow/Instructions/{instruction_doc})\n")
    out.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
    out.append("---\n\n")
    out.append("## Cross-chapter consistency: characteristics in this study\n\n")
    out.append(
        "Use these one-line profiles for cross-section consistency. The full profile of each "
        "characteristic is established in Chapter 2 — your chapter does not re-establish them, "
        "only refers to them by the characteristic name as you see them here.\n\n"
    )
    for sg in subgroups:
        if sg["subgroup_code"] == "BOUNDARY":
            continue
        desc_full = sg.get("core_description") or "(description pending)"
        # Split at sentence boundary (period+whitespace) — not at every period.
        # Guards against tokens like "ka.phar" being mistaken for sentence ends.
        desc1 = re.split(r"\.\s", desc_full, maxsplit=1)[0]
        out.append(f"- **{sg['label']}** — {desc1}.\n")
    out.append("\n---\n\n")
    return "".join(out)


# ---------- Per-chapter builders ----------

def build_ch1(cluster, subgroups, sg_vcgs_map, findings):
    out = [chapter_preamble(cluster, 1, "What this study is",
                            "wa-sessionc-cluster-ch1-instruction-v1_0-20260512.md", subgroups)]
    out.append("## 1. What this study is\n\n")
    out.append(ai_write_zone(
        zone_id="Chapter 1 opening prose",
        length="~300-500 words total",
        focus=(
            "Name what these characteristics are, what they cover together, why they belong "
            "together, what they share, how they depend on each other. End with a one-sentence "
            "preview of what follows."
        ),
        source_note="cluster-wide claims below, and the brief profiles in the preamble",
    ))
    out.append("\n**Evidence: cluster-wide claims from the analytical record**\n\n")
    out.append(evidence_block(
        "Ch1 — cluster-wide claims at T0 (the divine pattern)",
        fmt_findings(findings["cluster_syn"].get("T0", []), "T0 cluster-synthesis"),
    ))
    out.append("\n")
    out.append(evidence_block(
        "Ch1 — cluster-wide claims at T1 (what these characteristics are)",
        fmt_findings(findings["cluster_syn"].get("T1", []), "T1 cluster-synthesis"),
    ))
    return "".join(out)


def build_ch2(cluster, subgroups, sg_vcgs_map):
    out = [chapter_preamble(cluster, 2, "The characteristics in this study",
                            "wa-sessionc-cluster-ch2-instruction-v1_0-20260512.md", subgroups)]
    out.append("## 2. The characteristics in this study\n\n")
    out.append(ai_write_zone(
        zone_id="Chapter 2 opening (1-2 sentences)",
        length="~50-80 words",
        focus=(
            "Brief opening saying that the Bible's vocabulary for this inner-life domain "
            "organises into N related characteristics, each a distinct way the inner person "
            "manifests this aspect of inner life."
        ),
    ))
    sec_index = 0
    non_b = [sg for sg in subgroups if sg["subgroup_code"] != "BOUNDARY"]
    boundary = [sg for sg in subgroups if sg["subgroup_code"] == "BOUNDARY"]
    for sg in non_b:
        sec_index += 1
        out.append(f"\n### 2.{sec_index} {sg['label']}\n\n")
        out.append(ai_write_zone(
            zone_id=f"§2.{sec_index} ({sg['label']})",
            length="~200-300 words",
            focus=(
                "Describe this characteristic in plain English. Name it, characterise it, "
                "say how it differs from the others in this study. Anchor with one or two key verses."
            ),
            cite_verses=first_n_refs(sg_vcgs_map.get(sg["id"], []), n=2),
            source_note="sub-group description and key verses below",
        ))
        out.append("\n**Sub-group description (from analytical record):**\n\n")
        out.append(f"> {sg.get('core_description') or '_(description pending — flag in chapter notes)_'}\n\n")
        out.append("**Key verses for this characteristic:**\n\n")
        for vcg_entry in sg_vcgs_map.get(sg["id"], []):
            for a in vcg_entry["anchors"]:
                out.append(fmt_anchor(a, vcg_code=vcg_entry["vcg"]["group_code"]))
                out.append("\n")
    if boundary:
        sec_index += 1
        out.append(f"\n### 2.{sec_index} Supporting characteristics\n\n")
        out.append(ai_write_zone(
            zone_id=f"§2.{sec_index} (Supporting characteristics)",
            length="~150 words",
            focus=(
                "Briefly acknowledge supporting characteristics that play a part in this "
                "inner-life domain without themselves being inner-being characteristics. "
                "Note that they are not treated at full depth in chapters 4-7."
            ),
        ))
        for sg in boundary:
            out.append("\n**Description:**\n\n")
            out.append(f"> {sg.get('core_description') or '_(description pending)_'}\n\n")
    return "".join(out)


def build_ch3(cluster, subgroups, sg_vcgs_map, findings):
    out = [chapter_preamble(cluster, 3, "The divine pattern",
                            "wa-sessionc-cluster-ch3-instruction-v1_0-20260512.md", subgroups)]
    out.append("## 3. The divine pattern\n\n")
    out.append(ai_write_zone(
        zone_id="Chapter 3 cluster-wide spine + per-characteristic variation paragraphs",
        length="~1500-2500 words total",
        focus=(
            "Write the cluster-wide arc on how Scripture attributes these characteristics to "
            "God. Then for each non-BOUNDARY characteristic, write a short paragraph noting "
            "where its divine treatment differs from the cluster-wide pattern. Where Scripture "
            "is silent on God in a characteristic, name that silence."
        ),
        source_note="cluster-wide T0 below, then per-characteristic T0 blocks",
    ))
    out.append("\n**Evidence: cluster-wide T0 (the cluster's divine-image pattern)**\n\n")
    out.append(evidence_block(
        "Ch3 — cluster-wide T0",
        fmt_findings(findings["cluster_syn"].get("T0", []), "T0 cluster-synthesis"),
    ))
    out.append("\n**Evidence per characteristic: T0 findings + the divine-pattern key verses**\n\n")
    for sg in subgroups:
        if sg["subgroup_code"] == "BOUNDARY":
            continue
        out.append(f"\n#### {sg['label']}\n\n")
        out.append(evidence_block(
            f"Ch3 — T0 findings for {sg['label']}",
            fmt_findings(findings["by_sg_tier"].get((sg["id"], "T0"), []), "T0"),
        ))
        out.append("\n")
        silents = findings["silents_by_sg_tier"].get((sg["id"], "T0"), [])
        if silents:
            out.append(evidence_block(
                f"Ch3 — T0 silences for {sg['label']}",
                fmt_findings(silents, "T0 silent"),
            ))
            out.append("\n")
        out.append("\n_Divine-pattern key verses (typically VCG01-02):_\n\n")
        for vcg_entry in sg_vcgs_map.get(sg["id"], []):
            code = vcg_entry["vcg"]["group_code"]
            if code.endswith("VCG01") or code.endswith("VCG02"):
                for a in vcg_entry["anchors"][:2]:
                    out.append(fmt_anchor(a, vcg_code=code))
                    out.append("\n")
    return "".join(out)


def _per_sg_chapter(cluster, subgroups, sg_vcgs_map, findings,
                    chapter_num, title, instruction_doc, tiers, length_per_section,
                    focus_text):
    out = [chapter_preamble(cluster, chapter_num, title, instruction_doc, subgroups)]
    out.append(f"## {chapter_num}. {title}\n\n")
    out.append(ai_write_zone(
        zone_id=f"Chapter {chapter_num} opening (1-2 sentences)",
        length="~40-80 words",
        focus="Brief opening framing what this chapter covers. Do not name the analytical lens by code.",
    ))
    sec_index = 0
    non_b = [sg for sg in subgroups if sg["subgroup_code"] != "BOUNDARY"]
    for sg in non_b:
        sec_index += 1
        out.append(f"\n### {chapter_num}.{sec_index} {sg['label']}\n\n")
        cite = first_n_refs(sg_vcgs_map.get(sg["id"], []), n=4)
        out.append(ai_write_zone(
            zone_id=f"§{chapter_num}.{sec_index} ({sg['label']})",
            length=length_per_section,
            focus=focus_text,
            cite_verses=cite,
            source_note="all evidence for this characteristic on this lens is below",
        ))
        out.append("\n")
        for tier in tiers:
            sg_findings = findings["by_sg_tier"].get((sg["id"], tier), [])
            sg_silent = findings["silents_by_sg_tier"].get((sg["id"], tier), [])
            if sg_findings:
                out.append(evidence_block(
                    f"Ch{chapter_num} — {tier} findings for {sg['label']}",
                    fmt_findings(sg_findings, tier),
                ))
                out.append("\n")
            if sg_silent:
                out.append(evidence_block(
                    f"Ch{chapter_num} — {tier} silences for {sg['label']}",
                    fmt_findings(sg_silent, f"{tier} silent"),
                ))
                out.append("\n")
        out.append(f"\n**Key verses for {sg['label']}:**\n\n")
        for vcg_entry in sg_vcgs_map.get(sg["id"], []):
            for a in vcg_entry["anchors"]:
                out.append(fmt_anchor(a, vcg_code=vcg_entry["vcg"]["group_code"]))
                out.append("\n")
    return "".join(out)


def build_ch4(cluster, subgroups, sg_vcgs_map, findings):
    return _per_sg_chapter(
        cluster, subgroups, sg_vcgs_map, findings,
        chapter_num=4, title="Where each characteristic lives in the person",
        instruction_doc="wa-sessionc-cluster-ch4-instruction-v1_0-20260512.md",
        tiers=["T2", "T3"],
        length_per_section="~800-1500 words",
        focus_text=(
            "Where in the inner person this characteristic sits (heart, mind, will, conscience, "
            "soul, spirit, body) and which inner capacities it engages (perception, thought, "
            "memory, feeling, conscience, will, agency). Quote at least three key verses; the "
            "first must establish the primary inner location. Make divine-versus-human "
            "differences in location explicit where the evidence shows them. Name silences."
        ),
    )


def build_ch5(cluster, subgroups, sg_vcgs_map, findings):
    return _per_sg_chapter(
        cluster, subgroups, sg_vcgs_map, findings,
        chapter_num=5, title="How each characteristic works",
        instruction_doc="wa-sessionc-cluster-ch5-instruction-v1_0-20260512.md",
        tiers=["T4", "T5", "T1"],
        length_per_section="~800-1500 words",
        focus_text=(
            "How this characteristic moves between God and the human person, between persons, "
            "in covenant, against opposition; how it is formed, deepens, is tested, is "
            "transformed across time."
        ),
    )


def build_ch6(cluster, subgroups, sg_vcgs_map, findings):
    return _per_sg_chapter(
        cluster, subgroups, sg_vcgs_map, findings,
        chapter_num=6, title="How each characteristic relates to the others",
        instruction_doc="wa-sessionc-cluster-ch6-instruction-v1_0-20260512.md",
        tiers=["T6"],
        length_per_section="~400-800 words",
        focus_text=(
            "This characteristic's relationship to other inner characteristics in this study — "
            "what it is paired with, what it is opposed by, what produces it, what it itself produces."
        ),
    )


def build_ch7(cluster, subgroups, sg_vcgs_map, findings):
    out = [chapter_preamble(cluster, 7, "The view from outside Scripture",
                            "wa-sessionc-cluster-ch7-instruction-v1_0-20260512.md", subgroups)]
    out.append("## 7. The view from outside Scripture\n\n")
    out.append(ai_write_zone(
        zone_id="Chapter 7 opening note",
        length="~80-120 words",
        focus=(
            "Brief opening that names the purpose of this chapter — a short reflection on "
            "what human and clinical sciences observe about the corresponding inner capacities. "
            "Explicitly acknowledge that this view-from-outside is under-developed in the "
            "analytical record at present and is earmarked for future expansion."
        ),
    ))
    sec_index = 0
    non_b = [sg for sg in subgroups if sg["subgroup_code"] != "BOUNDARY"]
    for sg in non_b:
        sec_index += 1
        out.append(f"\n### 7.{sec_index} {sg['label']}\n\n")
        out.append(ai_write_zone(
            zone_id=f"§7.{sec_index} ({sg['label']})",
            length="~400-500 words",
            focus=(
                f"Short overview of what human / clinical sciences observe about the human "
                f"capacity corresponding to {sg['label']}. Reflect on synergies with the "
                f"biblical picture, gaps where science is silent on what Scripture emphasises, "
                f"and differences where the scientific framing diverges. Use general scientific "
                f"knowledge — the analytical record is thin on this lens. Note where the record "
                f"offers no view-from-outside material."
            ),
            source_note="T7 findings below (often sparse on the science-comparison prompts)",
            avoid="jargon; do not overclaim — be explicit where the analytical record is silent",
        ))
        out.append("\n")
        out.append(evidence_block(
            f"Ch7 — T7 findings for {sg['label']}",
            fmt_findings(findings["by_sg_tier"].get((sg["id"], "T7"), []), "T7"),
        ))
        out.append("\n")
        silents = findings["silents_by_sg_tier"].get((sg["id"], "T7"), [])
        if silents:
            out.append(evidence_block(
                f"Ch7 — T7 silences for {sg['label']}",
                fmt_findings(silents, "T7 silent"),
            ))
            out.append("\n")
    return "".join(out)


def build_ch8(cluster, subgroups, findings):
    out = [chapter_preamble(cluster, 8, "What this study does not yet address",
                            "wa-sessionc-cluster-ch8-instruction-v1_0-20260512.md", subgroups)]
    out.append("## 8. What this study does not yet address\n\n")
    out.append(ai_write_zone(
        zone_id="Chapter 8 honest accounting",
        length="~200-400 words",
        focus=(
            "Plain-English accounting of: (a) gaps named in the analytical record, "
            "(b) meaningful silences in the verse evidence, (c) the view-from-outside being "
            "under-developed and earmarked for expansion, (d) any LXX / Greek-of-the-Hebrew "
            "work parked for a future research session."
        ),
        source_note="gap findings below; silences are summarised across chapters",
    ))
    out.append("\n**Evidence: gap findings (cluster-wide)**\n\n")
    out.append(evidence_block(
        "Ch8 — gap findings",
        fmt_findings(findings.get("gaps", []), "gap"),
    ))
    return "".join(out)


def build_app_a(cluster, subgroups, sg_terms_map):
    out = [chapter_preamble(cluster, "A", "Terms in this study",
                            "wa-sessionc-cluster-appa-instruction-v1_0-20260512.md", subgroups)]
    out.append("## Appendix A — Terms in this study\n\n")
    out.append(ai_write_zone(
        zone_id="Appendix A opening (1 sentence)",
        length="~30 words",
        focus="One sentence framing the appendix as the term inventory underlying the study.",
    ))
    sec_index = 0
    non_b = [sg for sg in subgroups if sg["subgroup_code"] != "BOUNDARY"]
    boundary = [sg for sg in subgroups if sg["subgroup_code"] == "BOUNDARY"]
    for sg in non_b:
        sec_index += 1
        terms = sg_terms_map.get(sg["id"], [])
        out.append(f"\n### A.{sec_index} {sg['label']} — key terms\n\n")
        out.append(fmt_term_table(terms))
        out.append("\n")
        out.append(ai_write_zone(
            zone_id=f"A.{sec_index} commentary",
            length="~60-120 words",
            focus=(
                "Briefly characterise what these terms together name in this study. Comment "
                "on the Hebrew/Greek split if notable. Do not list the terms again."
            ),
        ))
    if boundary:
        sec_index += 1
        out.append(f"\n### A.{sec_index} Supportive terms across this study\n\n")
        out.append(
            "These terms appear in the verse evidence supporting the study but do not "
            "themselves carry one of the core characteristics.\n\n"
        )
        for sg in boundary:
            terms = sg_terms_map.get(sg["id"], [])
            out.append(fmt_term_table(terms))
            out.append("\n")
    return "".join(out)


def build_app_b(cluster, subgroups, sg_vcgs_map):
    out = [chapter_preamble(cluster, "B", "Key verses",
                            "wa-sessionc-cluster-appb-instruction-v1_0-20260512.md", subgroups)]
    out.append("## Appendix B — Key verses\n\n")
    out.append("Every key verse cited in the chapters above.\n\n")
    out.append("| Characteristic | Meaning-group | Reference | Strong's | Translit. | Verse text | Meaning of the term in this study |\n")
    out.append("|---|---|---|---|---|---|---|\n")
    for sg in subgroups:
        for vcg_entry in sg_vcgs_map.get(sg["id"], []):
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
    out.append("\n")
    out.append(ai_write_zone(
        zone_id="Appendix B closing note",
        length="~40 words",
        focus=(
            "Optional one-sentence closing for the table — e.g. noting the total count and "
            "where readers can find the underlying meaning-group descriptions."
        ),
    ))
    return "".join(out)


def build_app_c(cluster, subgroups, findings):
    out = [chapter_preamble(cluster, "C", "Method note",
                            "wa-sessionc-cluster-appc-instruction-v1_0-20260512.md", subgroups)]
    out.append("## Appendix C — Method note\n\n")
    out.append(ai_write_zone(
        zone_id="Appendix C method note",
        length="~150 words",
        focus=(
            "Plain-English paragraph acknowledging that the study draws from a structured "
            "analytical record covering the verse evidence for each characteristic, with key "
            "verses selected as evidential foundation. No claim in the chapters above is made "
            "without specific verse evidence behind it."
        ),
    ))
    out.append("\n")
    total = (sum(len(v) for v in findings["by_sg_tier"].values())
             + sum(len(v) for v in findings["cluster_syn"].values())
             + len(findings["gaps"])
             + sum(len(v) for v in findings["silents_by_sg_tier"].values()))
    out.append(evidence_block(
        "App C — Cluster metadata",
        f"- Cluster code: {cluster['cluster_code']}\n"
        f"- Short name: {cluster.get('short_name')}\n"
        f"- Description: {cluster.get('description')}\n"
        f"- Status: {cluster.get('status')}\n"
        f"- Version: {cluster.get('version')}\n"
        f"- Last updated: {cluster.get('last_updated_date')}\n"
        f"- Total findings underlying this study: {total}\n",
    ))
    return "".join(out)


CHAPTER_BUILDERS = {
    "ch1": ("1", build_ch1),
    "ch2": ("2", build_ch2),
    "ch3": ("3", build_ch3),
    "ch4": ("4", build_ch4),
    "ch5": ("5", build_ch5),
    "ch6": ("6", build_ch6),
    "ch7": ("7", build_ch7),
    "appa": ("A", build_app_a),
    "appb": ("B", build_app_b),
    "appc": ("C", build_app_c),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--only", default=None, help="Comma-separated chapter keys (ch1..ch8, appa, appb, appc). Default: all")
    args = ap.parse_args()

    code = args.cluster
    only = set(args.only.split(",")) if args.only else None

    conn = get_conn()
    cluster = fetch_cluster(conn, code)
    subgroups = fetch_subgroups(conn, code)
    sg_terms_map = {sg["id"]: fetch_sg_terms(conn, sg["id"]) for sg in subgroups}
    sg_vcgs_map = {sg["id"]: fetch_sg_vcgs_with_anchors(conn, sg["id"], code) for sg in subgroups}
    findings = fetch_findings(conn, code)

    out_dir = f"Sessions/Session_Clusters/{code}/inputs"
    os.makedirs(out_dir, exist_ok=True)
    d = datetime.now().strftime("%Y%m%d")

    written = []
    for key, (num, builder) in CHAPTER_BUILDERS.items():
        if only and key not in only:
            continue
        # Call builder with whatever subset of args it needs (signature varies)
        if key == "ch1":
            content = builder(cluster, subgroups, sg_vcgs_map, findings)
        elif key == "ch2":
            content = builder(cluster, subgroups, sg_vcgs_map)
        elif key == "ch3":
            content = builder(cluster, subgroups, sg_vcgs_map, findings)
        elif key in ("ch4", "ch5", "ch6"):
            content = builder(cluster, subgroups, sg_vcgs_map, findings)
        elif key == "ch7":
            content = builder(cluster, subgroups, sg_vcgs_map, findings)
        elif key == "ch8":
            content = builder(cluster, subgroups, findings)
        elif key == "appa":
            content = builder(cluster, subgroups, sg_terms_map)
        elif key == "appb":
            content = builder(cluster, subgroups, sg_vcgs_map)
        elif key == "appc":
            content = builder(cluster, subgroups, findings)
        else:
            continue
        fname = f"wa-cluster-{code}-{key}-input-v1-{d}.md"
        path = os.path.join(out_dir, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        written.append((path, len(content)))

    print(f"Wrote {len(written)} files to {out_dir}:")
    for path, n in written:
        print(f"  {os.path.basename(path):60s}  {n:>9,} chars (~{n//6:>7,} words)")
    conn.close()


if __name__ == "__main__":
    main()
