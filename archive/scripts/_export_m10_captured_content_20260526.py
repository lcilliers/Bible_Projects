"""Export everything currently captured in the DB for M10.

Two output files (in Sessions/Session_Clusters/M10/):
  - wa-cluster-M10-captured-content-overview-v1-{date}.md  (structural + observations + meanings)
  - wa-cluster-M10-captured-content-findings-v1-{date}.md  (4,158 cluster_finding rows verbatim)

Purpose: baseline for comparing what's IN the DB against what's on disk in
the M10 folder. Per researcher direction 2026-05-26: M10 followed a non-standard
process (single-theme cluster, ~2,000+ verses pre-split, adhoc analysis); we
need to know what's captured before deciding what's missing.

Pulls from every table that holds analytical content for M10:
  - cluster (description, gloss, source, status, version)
  - mti_terms (cluster_code='M10')
  - cluster_subgroup (core_description per subgroup)
  - characteristic (definition per characteristic)
  - characteristic_subgroup (qualifier_note + partial flags)
  - verse_context_group (context_description per VCG, joined via vcg_term)
  - vcg_term (term ↔ VCG links)
  - cluster_observation (155 rows, all observation_types)
  - verse_context (analysis_note + keywords for 1,325 is_relevant rows;
                   set_aside_reason for is_relevant=0 rows)
  - cluster_finding (4,158 char-scope rows verbatim)
  - finding_citation (citation counts summary)
"""
from __future__ import annotations
import io, sqlite3, sys, json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
CLUSTER = "M10"

OUT_DIR = REPO / "Sessions" / "Session_Clusters" / CLUSTER
OVERVIEW_PATH = OUT_DIR / f"wa-cluster-M10-captured-content-overview-v1-{DATE}.md"
FINDINGS_PATH = OUT_DIR / f"wa-cluster-M10-captured-content-findings-v1-{DATE}.md"


def main() -> int:
    conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row

    # ===== OVERVIEW FILE =====
    O: list[str] = []
    O.append(f"# M10 — captured content (DB export)")
    O.append("")
    O.append(f"**Generated:** {NOW}")
    O.append(f"**Cluster:** {CLUSTER}")
    O.append(f"**Purpose:** baseline of what is currently in the database for M10. Compare against folder contents to identify uncaptured analytical content.")
    O.append("")
    O.append(f"**Companion file** (this export split for size): "
             f"`wa-cluster-M10-captured-content-findings-v1-{DATE}.md` — verbatim cluster_finding rows.")
    O.append("")
    O.append("---")
    O.append("")
    O.append("## TOC")
    O.append("")
    O.append("- §1. Cluster row")
    O.append("- §2. Term universe (mti_terms)")
    O.append("- §3. Sub-group structure")
    O.append("- §4. Characteristic structure")
    O.append("- §5. Characteristic ↔ Sub-group mapping")
    O.append("- §6. VCG structure (per sub-group)")
    O.append("- §7. Cluster observations (155 rows)")
    O.append("- §8. Pass A meanings + keywords (1,325 verses)")
    O.append("- §9. Set-aside reasons (Phase 1 + Phase 8.5)")
    O.append("- §10. Finding citations (summary)")
    O.append("- §11. Counts summary")
    O.append("")
    O.append("---")
    O.append("")

    # §1 Cluster row
    O.append("## §1. Cluster row")
    O.append("")
    c = conn.execute(
        "SELECT cluster_code, description, gloss, source, bucket, status, version, short_name, last_updated_date "
        "FROM cluster WHERE cluster_code=?", (CLUSTER,)
    ).fetchone()
    O.append("| field | value |")
    O.append("|---|---|")
    for k in ("cluster_code","description","short_name","status","version","source","bucket","last_updated_date"):
        O.append(f"| {k} | {c[k]} |")
    O.append("")
    O.append("**Gloss (term list):**")
    O.append("")
    O.append(f"> {c['gloss']}")
    O.append("")
    O.append("---")
    O.append("")

    # §2 Term universe
    O.append("## §2. Term universe (mti_terms for M10)")
    O.append("")
    terms = conn.execute("""
        SELECT id, strongs_number, transliteration, gloss, language, owning_registry,
               status, anchor_note, vc_status, md_version,
               (SELECT COUNT(*) FROM verse_context vc WHERE vc.mti_term_id=mti_terms.id AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0) AS n_relevant,
               (SELECT COUNT(*) FROM verse_context vc WHERE vc.mti_term_id=mti_terms.id AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0) AS n_anchor
        FROM mti_terms
        WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
        ORDER BY n_relevant DESC, strongs_number
    """, (CLUSTER,)).fetchall()
    O.append(f"**Total terms:** {len(terms)}")
    O.append("")
    O.append("| mti_id | Strong's | Translit | Gloss | Lang | Status | Reg | Relevant | Anchor | md_v |")
    O.append("|---:|---|---|---|---|---|---|---:|---:|---:|")
    for r in terms:
        O.append(f"| {r['id']} | {r['strongs_number']} | {r['transliteration'] or ''} | "
                 f"{(r['gloss'] or '')[:40]} | {r['language']} | {r['status']} | "
                 f"{r['owning_registry'] or ''} | {r['n_relevant']} | {r['n_anchor']} | {r['md_version']} |")
    O.append("")
    O.append("---")
    O.append("")

    # §3 Sub-groups
    O.append("## §3. Sub-group structure (cluster_subgroup)")
    O.append("")
    sgs = conn.execute("""
        SELECT id, subgroup_code, label, core_description, sort_order, status, version, source,
               (SELECT COUNT(*) FROM verse_context vc WHERE vc.cluster_subgroup_id=cluster_subgroup.id AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0) AS n_verses
        FROM cluster_subgroup
        WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
        ORDER BY sort_order
    """, (CLUSTER,)).fetchall()
    O.append(f"**Total sub-groups:** {len(sgs)}")
    O.append("")
    for sg in sgs:
        O.append(f"### {sg['subgroup_code']} — {sg['label']} ({sg['n_verses']} verses)")
        O.append("")
        O.append(f"- **sort_order:** {sg['sort_order']}  ·  **status:** {sg['status']}  ·  **version:** {sg['version']}")
        O.append(f"- **source:** `{sg['source']}`")
        O.append("")
        O.append("**core_description:**")
        O.append("")
        O.append(f"> {sg['core_description']}")
        O.append("")
    O.append("---")
    O.append("")

    # §4 Characteristics
    O.append("## §4. Characteristic structure (characteristic)")
    O.append("")
    chars = conn.execute("""
        SELECT id, char_seq, short_name, definition, source, version
        FROM characteristic
        WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
        ORDER BY char_seq
    """, (CLUSTER,)).fetchall()
    O.append(f"**Total characteristics:** {len(chars)}")
    O.append("")
    for ch in chars:
        O.append(f"### CHAR-{ch['char_seq']} (id={ch['id']}) — {ch['short_name']}")
        O.append("")
        O.append(f"- **source:** `{ch['source']}`  ·  **version:** {ch['version']}")
        O.append("")
        O.append("**definition:**")
        O.append("")
        O.append(f"> {ch['definition']}")
        O.append("")
    O.append("---")
    O.append("")

    # §5 Characteristic ↔ Sub-group mapping
    O.append("## §5. Characteristic ↔ Sub-group mapping (characteristic_subgroup)")
    O.append("")
    links = conn.execute("""
        SELECT ch.char_seq, ch.short_name AS char_name,
               cs.subgroup_code, cs.label AS sg_label,
               csg.qualifier_note, csg.is_partial, csg.partial_register_note
        FROM characteristic_subgroup csg
        JOIN characteristic ch ON ch.id = csg.characteristic_id
        JOIN cluster_subgroup cs ON cs.id = csg.cluster_subgroup_id
        WHERE ch.cluster_code=? AND COALESCE(csg.delete_flagged,0)=0
        ORDER BY ch.char_seq, cs.sort_order
    """, (CLUSTER,)).fetchall()
    O.append(f"**Total links:** {len(links)}")
    O.append("")
    for l in links:
        partial = " (PARTIAL)" if l["is_partial"] else ""
        O.append(f"### CHAR-{l['char_seq']} ({l['char_name']}) ↔ {l['subgroup_code']} ({l['sg_label']}){partial}")
        O.append("")
        if l["qualifier_note"]:
            O.append("**qualifier_note:**")
            O.append("")
            O.append(f"> {l['qualifier_note']}")
            O.append("")
        if l["partial_register_note"]:
            O.append(f"**partial_register_note:** {l['partial_register_note']}")
            O.append("")
    O.append("---")
    O.append("")

    # §6 VCGs (per sub-group)
    O.append("## §6. VCG structure (verse_context_group, per sub-group)")
    O.append("")
    # Pull VCGs joined to sub-groups via verse_context membership; use sub-group prefix in group_code
    vcgs = conn.execute("""
        SELECT vcg.id, vcg.group_code, vcg.context_description,
               (SELECT COUNT(DISTINCT vc.id) FROM verse_context vc WHERE vc.group_id=vcg.id AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0) AS n_verses,
               (SELECT COUNT(*) FROM vcg_term vt WHERE vt.vcg_id=vcg.id AND COALESCE(vt.delete_flagged,0)=0) AS n_terms,
               (SELECT vc.id FROM verse_context vc WHERE vc.group_id=vcg.id AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0 LIMIT 1) AS anchor_vc_id
        FROM verse_context_group vcg
        WHERE vcg.group_code LIKE 'M10-%' AND COALESCE(vcg.delete_flagged,0)=0
        ORDER BY vcg.group_code
    """).fetchall()
    O.append(f"**Total active VCGs:** {len(vcgs)}")
    O.append("")
    # Group by sub-group letter
    by_sg = defaultdict(list)
    for v in vcgs:
        # Pattern: M10-{X}-VCG-{NN}
        parts = v["group_code"].split("-")
        sg = parts[1] if len(parts) > 1 else "?"
        by_sg[sg].append(v)
    for sg_letter in sorted(by_sg.keys()):
        O.append(f"### Sub-group M10-{sg_letter}")
        O.append("")
        for v in sorted(by_sg[sg_letter], key=lambda x: x["group_code"]):
            O.append(f"#### {v['group_code']} ({v['n_verses']} V, {v['n_terms']} terms; anchor vc_id={v['anchor_vc_id']})")
            O.append("")
            O.append(f"> {v['context_description']}")
            O.append("")
    O.append("---")
    O.append("")

    # §7 Cluster observations
    O.append("## §7. Cluster observations (cluster_observation)")
    O.append("")
    obs = conn.execute("""
        SELECT id, observation_type, target_phase, source_phase, status,
               characteristic_id, cluster_subgroup_id,
               title, description, source_file, resolution_note,
               (SELECT char_seq FROM characteristic c WHERE c.id=cluster_observation.characteristic_id) AS char_seq,
               (SELECT subgroup_code FROM cluster_subgroup cs WHERE cs.id=cluster_observation.cluster_subgroup_id) AS subgroup_code
        FROM cluster_observation
        WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
        ORDER BY observation_type, id
    """, (CLUSTER,)).fetchall()
    O.append(f"**Total observations:** {len(obs)}")
    O.append("")
    # Group by type
    by_type = defaultdict(list)
    for o in obs:
        by_type[o["observation_type"]].append(o)
    O.append("**By type:**")
    O.append("")
    O.append("| Type | Count |")
    O.append("|---|---:|")
    for t in sorted(by_type.keys()):
        O.append(f"| {t} | {len(by_type[t])} |")
    O.append("")
    for t in sorted(by_type.keys()):
        O.append(f"### {t} ({len(by_type[t])})")
        O.append("")
        for o in by_type[t]:
            scope = ""
            if o["char_seq"]:
                scope = f" — CHAR-{o['char_seq']}"
            elif o["subgroup_code"]:
                scope = f" — {o['subgroup_code']}"
            O.append(f"#### obs #{o['id']}{scope} — {o['title']}")
            O.append("")
            O.append(f"- **status:** {o['status']}  ·  **target_phase:** {o['target_phase']}  ·  **source_phase:** {o['source_phase']}")
            if o["source_file"]:
                O.append(f"- **source_file:** `{o['source_file']}`")
            O.append("")
            O.append("**description:**")
            O.append("")
            # Indent body as blockquote
            body = (o["description"] or "").strip()
            for line in body.split("\n"):
                O.append(f"> {line}")
            O.append("")
            if o["resolution_note"]:
                O.append("**resolution_note:**")
                O.append(f"> {o['resolution_note']}")
                O.append("")
    O.append("---")
    O.append("")

    # §8 Pass A meanings + keywords
    O.append("## §8. Pass A meanings + keywords (verse_context, is_relevant=1)")
    O.append("")
    O.append("Per-verse meaning + atomic keywords from Pass A. Grouped by sub-group → VCG → canonical order.")
    O.append("")
    meanings = conn.execute("""
        SELECT vc.id AS vc_id, vc.verse_record_id, vc.mti_term_id,
               vc.is_anchor, vc.analysis_note, vc.keywords,
               vr.reference, vr.book_id, vr.chapter, vr.verse_num,
               mt.strongs_number, mt.transliteration,
               cs.subgroup_code, vcg.group_code AS vcg_code
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        LEFT JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id
        WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
          AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
        ORDER BY cs.sort_order, vcg.group_code, vr.book_id, vr.chapter, vr.verse_num
    """, (CLUSTER,)).fetchall()
    O.append(f"**Total meanings:** {len(meanings)}")
    O.append("")
    # Group by sub-group, then VCG
    by_sg_vcg = defaultdict(lambda: defaultdict(list))
    for m in meanings:
        by_sg_vcg[m["subgroup_code"] or "(none)"][m["vcg_code"] or "(none)"].append(m)
    for sg_code in sorted(by_sg_vcg.keys()):
        O.append(f"### {sg_code}")
        O.append("")
        for vcg_code in sorted(by_sg_vcg[sg_code].keys()):
            mlist = by_sg_vcg[sg_code][vcg_code]
            O.append(f"#### {vcg_code} ({len(mlist)} verses)")
            O.append("")
            for m in mlist:
                anchor = " ★" if m["is_anchor"] else ""
                kws_text = ""
                if m["keywords"]:
                    try:
                        kws = json.loads(m["keywords"])
                        kws_text = " — keywords: " + ", ".join(f"`{k}`" for k in kws)
                    except Exception:
                        kws_text = f" — keywords (raw): `{m['keywords']}`"
                O.append(f"- **vc={m['vc_id']}** {m['reference']} `{m['strongs_number']} {m['transliteration']}`{anchor}: {m['analysis_note']}{kws_text}")
            O.append("")
    O.append("---")
    O.append("")

    # §9 Set-aside reasons
    O.append("## §9. Set-aside reasons (Phase 1 + Phase 8.5)")
    O.append("")
    setasides = conn.execute("""
        SELECT vc.id AS vc_id, vc.set_aside_reason, vr.reference,
               mt.strongs_number, mt.transliteration
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
          AND vc.is_relevant=0
          AND COALESCE(vc.delete_flagged,0)=0
          AND vc.set_aside_reason IS NOT NULL
        ORDER BY mt.strongs_number, vr.book_id, vr.chapter, vr.verse_num
    """, (CLUSTER,)).fetchall()
    O.append(f"**Total set-aside verses with reason:** {len(setasides)}")
    O.append("")
    for s in setasides:
        O.append(f"- **vc={s['vc_id']}** {s['reference']} `{s['strongs_number']} {s['transliteration']}` — {s['set_aside_reason']}")
    O.append("")
    O.append("---")
    O.append("")

    # §10 Finding citations summary
    O.append("## §10. Finding citations (finding_citation, summary)")
    O.append("")
    cit_summary = conn.execute("""
        SELECT fc.citation_type, COUNT(*) AS n,
               COUNT(DISTINCT fc.citation_value) AS distinct_n
        FROM finding_citation fc
        JOIN cluster_finding cf ON cf.id = fc.source_id AND fc.source_table='cluster_finding'
        WHERE cf.cluster_code=? AND COALESCE(cf.delete_flagged,0)=0
        GROUP BY fc.citation_type
        ORDER BY n DESC
    """, (CLUSTER,)).fetchall()
    O.append("| citation_type | rows | distinct values |")
    O.append("|---|---:|---:|")
    total = 0
    for r in cit_summary:
        O.append(f"| {r['citation_type']} | {r['n']:,} | {r['distinct_n']:,} |")
        total += r["n"]
    O.append(f"| **TOTAL** | **{total:,}** | |")
    O.append("")
    # Top 20 per type
    for r in cit_summary:
        ct = r["citation_type"]
        O.append(f"### Top 20 most-cited `{ct}`")
        O.append("")
        top = conn.execute("""
            SELECT fc.citation_value, COUNT(*) AS n
            FROM finding_citation fc
            JOIN cluster_finding cf ON cf.id = fc.source_id AND fc.source_table='cluster_finding'
            WHERE cf.cluster_code=? AND fc.citation_type=? AND COALESCE(cf.delete_flagged,0)=0
            GROUP BY fc.citation_value
            ORDER BY n DESC
            LIMIT 20
        """, (CLUSTER, ct)).fetchall()
        for t in top:
            O.append(f"- `{t['citation_value']}`: {t['n']}")
        O.append("")
    O.append("---")
    O.append("")

    # §11 Counts summary
    O.append("## §11. Counts summary")
    O.append("")
    counts = {
        "mti_terms": len(terms),
        "cluster_subgroup": len(sgs),
        "characteristic": len(chars),
        "characteristic_subgroup": len(links),
        "verse_context_group (M10 VCGs)": len(vcgs),
        "cluster_observation": len(obs),
        "verse_context is_relevant=1": len(meanings),
        "verse_context set_aside_reason": len(setasides),
        "cluster_finding (char-scope)": conn.execute(
            "SELECT COUNT(*) FROM cluster_finding WHERE cluster_code=? AND characteristic_id IS NOT NULL AND COALESCE(delete_flagged,0)=0", (CLUSTER,)
        ).fetchone()[0],
        "cluster_finding (cluster-scope)": conn.execute(
            "SELECT COUNT(*) FROM cluster_finding WHERE cluster_code=? AND characteristic_id IS NULL AND COALESCE(delete_flagged,0)=0", (CLUSTER,)
        ).fetchone()[0],
        "finding_citation (total)": total,
    }
    O.append("| table | rows |")
    O.append("|---|---:|")
    for k, v in counts.items():
        O.append(f"| {k} | {v:,} |")
    O.append("")

    OVERVIEW_PATH.write_text("\n".join(O), encoding="utf-8")
    print(f"Overview: {OVERVIEW_PATH}  ({OVERVIEW_PATH.stat().st_size:,} bytes)")

    # ===== FINDINGS FILE (cluster_finding rows verbatim) =====
    F: list[str] = []
    F.append(f"# M10 — captured findings (cluster_finding rows verbatim)")
    F.append("")
    F.append(f"**Generated:** {NOW}")
    F.append(f"**Cluster:** {CLUSTER}")
    F.append("**Companion to:** `wa-cluster-M10-captured-content-overview-v1-{date}.md`")
    F.append("")
    F.append("---")
    F.append("")

    # cluster_finding rows, char-scope, grouped by char + tier + prompt
    findings = conn.execute("""
        SELECT cf.id AS cf_id, cf.finding_status, cf.finding_text, cf.version,
               cf.cluster_subgroup_id, cf.vcg_scope, cf.obs_id,
               q.question_code, q.tier, q.component_code, q.component_title,
               q.question_text,
               ch.char_seq, ch.short_name AS char_name
        FROM cluster_finding cf
        JOIN wa_obs_question_catalogue q ON q.obs_id = cf.obs_id
        LEFT JOIN characteristic ch ON ch.id = cf.characteristic_id
        WHERE cf.cluster_code=? AND COALESCE(cf.delete_flagged,0)=0
        ORDER BY ch.char_seq IS NULL, ch.char_seq, q.tier, q.component_code, q.prompt_seq
    """, (CLUSTER,)).fetchall()
    F.append(f"**Total cluster_finding rows:** {len(findings)}")
    F.append("")
    # Group by char (NULL = cluster-scope)
    by_char = defaultdict(list)
    for r in findings:
        key = (r["char_seq"], r["char_name"]) if r["char_seq"] else (None, "CLUSTER-SCOPE (synthesis)")
        by_char[key].append(r)

    for key in sorted(by_char.keys(), key=lambda k: (k[0] is None, k[0] or 0)):
        char_seq, char_name = key
        flist = by_char[key]
        e_n = sum(1 for r in flist if r["finding_status"] == "finding")
        s_n = sum(1 for r in flist if r["finding_status"] == "silent")
        g_n = sum(1 for r in flist if r["finding_status"] == "gap")
        cs_n = sum(1 for r in flist if r["finding_status"] == "cluster_synthesis")
        F.append(f"## CHAR-{char_seq or '∅'} — {char_name} ({len(flist)} rows: E={e_n} S={s_n} G={g_n} CS={cs_n})")
        F.append("")
        # Group by tier
        by_tier = defaultdict(list)
        for r in flist:
            by_tier[r["tier"]].append(r)
        for tier in sorted(by_tier.keys()):
            F.append(f"### {tier}")
            F.append("")
            for r in by_tier[tier]:
                status_marker = {"finding":"E","silent":"S","gap":"G","cluster_synthesis":"CS"}.get(r["finding_status"], r["finding_status"])
                F.append(f"#### {r['question_code']} (cf={r['cf_id']}, {status_marker}) — {r['question_text']}")
                F.append("")
                F.append((r["finding_text"] or "").strip())
                F.append("")
                F.append("---")
                F.append("")

    FINDINGS_PATH.write_text("\n".join(F), encoding="utf-8")
    print(f"Findings: {FINDINGS_PATH}  ({FINDINGS_PATH.stat().st_size:,} bytes)")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
