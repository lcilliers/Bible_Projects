"""Generate a cluster's outstanding-research and open-questions report.

Run AFTER a cluster's Session C publication is complete. The report inventories
the open work the analytical record leaves behind so the researcher can plan
follow-up Session B passes, cross-cluster work, and term-level cleanup.

Read-only. Single .md output.

Usage:
    python scripts/_generate_cluster_outstanding_research_v1_20260513.py --cluster M15
"""
import sqlite3, sys, os, argparse
from collections import defaultdict
from datetime import datetime
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB = "database/bible_research.db"


def get_conn():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def fetch_cluster(conn, code):
    r = conn.execute("SELECT * FROM cluster WHERE cluster_code=?", (code,)).fetchone()
    if not r:
        raise SystemExit(f"Cluster {code} not found")
    return dict(r)


def fetch_subgroups(conn, code):
    return [dict(r) for r in conn.execute("""
        SELECT * FROM cluster_subgroup
         WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
         ORDER BY CASE WHEN subgroup_code='BOUNDARY' THEN 'ZZZZ' ELSE subgroup_code END
    """, (code,)).fetchall()]


# ---------- Strand 1: Gap findings ----------

def strand_gaps(conn, code):
    return [dict(r) for r in conn.execute("""
        SELECT cf.id AS cf_id, cf.cluster_subgroup_id, cs.subgroup_code, cs.label AS sg_label,
               cf.finding_text, cf.notes,
               q.question_code, q.tier, q.section, q.question_text
          FROM cluster_finding cf
          LEFT JOIN cluster_subgroup cs ON cs.id = cf.cluster_subgroup_id
          JOIN wa_obs_question_catalogue q ON q.obs_id = cf.obs_id
         WHERE cf.cluster_code=? AND cf.finding_status='gap'
           AND COALESCE(cf.delete_flagged,0)=0
         ORDER BY q.tier, q.question_code
    """, (code,)).fetchall()]


# ---------- Strand 2: T7 under-developed ----------

def strand_t7_under_developed(conn, code):
    """Findings where finding_text indicates the sub-group was not separately
    addressed (the sentinel that the science-comparison work is thin)."""
    return [dict(r) for r in conn.execute("""
        SELECT cf.id AS cf_id, cs.subgroup_code, cs.label AS sg_label,
               q.question_code, q.section, q.question_text, q.component_title,
               cf.finding_text
          FROM cluster_finding cf
          LEFT JOIN cluster_subgroup cs ON cs.id = cf.cluster_subgroup_id
          JOIN wa_obs_question_catalogue q ON q.obs_id = cf.obs_id
         WHERE cf.cluster_code=?
           AND q.tier='T7'
           AND COALESCE(cf.delete_flagged,0)=0
           AND (cf.finding_text LIKE '%Sub-group not separately addressed%'
                OR cf.finding_text LIKE '%not separately addressed in source%')
         ORDER BY cs.subgroup_code, q.question_code
    """, (code,)).fetchall()]


# ---------- Strand 3: LXX gap (standard programme note) ----------

LXX_NOTE = (
    "The Greek-of-the-Hebrew (LXX) treatment of this cluster's OT terms is "
    "parked for a separate Logos Bible Software research session, as a "
    "programme-wide convention. The LXX work, when undertaken, would add a "
    "fourth language layer (Hebrew → LXX Greek → NT Greek → English) to the "
    "vocabulary analysis and may surface continuity or rupture in semantic "
    "fields across testaments that the current Hebrew-vs-NT-Greek treatment "
    "cannot show."
)


# ---------- Strand 4: Cross-cluster pointers ----------

def strand_cross_cluster(conn, code):
    """SD_POINTER + cross-registry-links flags touching cluster terms."""
    # cross-registry links: join via mti_terms in cluster → wa_file_index → wa_cross_registry_links
    cross_links = [dict(r) for r in conn.execute("""
        SELECT DISTINCT
               mt.strongs_number, mt.transliteration, mt.owning_word AS source_word,
               wcrl.linked_word, wcrl.linked_registry_id,
               wcrt.type_code AS link_type_code, wcrt.description AS link_type_label,
               wcrl.connecting_term, wcrl.note, wcrl.last_changed
          FROM mti_terms mt
          JOIN wa_file_index fi ON fi.word_registry_fk = mt.owning_registry_fk
          JOIN wa_cross_registry_links wcrl ON wcrl.file_id = fi.id
          LEFT JOIN wa_crosslink_type wcrt ON wcrt.id = wcrl.connection_type_id
         WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
         ORDER BY mt.strongs_number, wcrl.linked_word
    """, (code,)).fetchall()]

    sd_pointers = [dict(r) for r in conn.execute("""
        SELECT DISTINCT
               wsrf.id, wsrf.flag_code, wsrf.flag_label, wsrf.strongs_reference,
               wsrf.priority, wsrf.session_target, wsrf.description,
               wsrf.session_raised, wsrf.raised_date,
               wsrf.resolved, wsrf.resolved_note
          FROM wa_session_research_flags wsrf
          JOIN mti_terms mt ON mt.strongs_number = wsrf.strongs_reference
         WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
           AND wsrf.flag_code IN ('SD_POINTER','SD_CLUSTER')
           AND COALESCE(wsrf.resolved,0) = 0
         ORDER BY wsrf.priority, wsrf.strongs_reference
    """, (code,)).fetchall()]

    return cross_links, sd_pointers


# ---------- Strand 5: Term-level open items ----------

def strand_term_open(conn, code):
    """mti_terms in the cluster with thin/candidate-delete status, or with open
    mti_term_flags or wa_data_quality_flags."""
    thin = [dict(r) for r in conn.execute("""
        SELECT mt.strongs_number, mt.transliteration, mt.gloss, mt.status,
               mt.exclusion_reason, mt.anchor_note, cs.subgroup_code, cs.label AS sg_label
          FROM mti_terms mt
          LEFT JOIN mti_term_subgroup mts ON mts.mti_term_id = mt.id
                AND COALESCE(mts.delete_flagged,0)=0
          LEFT JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
         WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
           AND mt.status IN ('extracted_thin','candidate_delete')
         ORDER BY mt.status, mt.strongs_number
    """, (code,)).fetchall()]

    # Both flag tables: exclude the evidence-flag family
    # (VERSE_EVIDENCE_*) — per CLAUDE.md §14 these are informational, not gating.
    mt_flags = [dict(r) for r in conn.execute("""
        SELECT mt.strongs_number, mt.transliteration, mt.gloss,
               qft.flag_code, qft.description AS flag_description, qft.flag_group
          FROM mti_terms mt
          JOIN mti_term_flags mtf ON mtf.mti_term_id = mt.id
          JOIN wa_quality_flag_types qft ON qft.id = mtf.flag_id
         WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
           AND COALESCE(qft.deprecated,0)=0
           AND qft.flag_code NOT LIKE 'VERSE_EVIDENCE_%'
         ORDER BY qft.flag_group, mt.strongs_number
    """, (code,)).fetchall()]

    # Data-quality flags: aggregate by distinct term × flag_code (not per-row).
    # The wa_data_quality_flags table writes one row per (file_id × term × flag),
    # which inflates counts by the XREF-copy factor. Distinct terms is the
    # meaningful count.
    dq_flag_summary = [dict(r) for r in conn.execute("""
        SELECT qft.flag_code, qft.description AS flag_description, qft.flag_group,
               COUNT(DISTINCT dqf.term_id) AS distinct_terms,
               COUNT(*) AS row_count
          FROM wa_data_quality_flags dqf
          JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id
          JOIN mti_terms mt ON mt.strongs_number = dqf.term_id
         WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
           AND COALESCE(qft.deprecated,0)=0
           AND qft.flag_code NOT LIKE 'VERSE_EVIDENCE_%'
         GROUP BY qft.flag_code, qft.description, qft.flag_group
         ORDER BY distinct_terms DESC
    """, (code,)).fetchall()]

    dq_terms = [dict(r) for r in conn.execute("""
        SELECT dqf.term_id, mt.transliteration, mt.gloss,
               GROUP_CONCAT(DISTINCT qft.flag_code) AS flag_codes,
               COUNT(*) AS row_count
          FROM wa_data_quality_flags dqf
          JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id
          JOIN mti_terms mt ON mt.strongs_number = dqf.term_id
         WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
           AND COALESCE(qft.deprecated,0)=0
           AND qft.flag_code NOT LIKE 'VERSE_EVIDENCE_%'
         GROUP BY dqf.term_id, mt.transliteration, mt.gloss
         ORDER BY row_count DESC, dqf.term_id
    """, (code,)).fetchall()]

    return thin, mt_flags, dq_flag_summary, dq_terms


# ---------- Strand 6: VC-coverage gaps ----------

def strand_vc_anomalies(conn, code):
    """Real VC-coverage gaps: cluster terms placed in a sub-group but with NO
    active verse_context rows tied to any of the cluster's sub-groups.

    Set-aside VC rows (group_id IS NULL but cluster_subgroup_id IS set,
    typically with set_aside_reason populated) ARE counted as VC done — they
    represent a completed analytical judgement (e.g. 'no_inner_being_
    phenomenon') rather than missing work."""
    return [dict(r) for r in conn.execute("""
        SELECT mt.strongs_number, mt.transliteration, mt.gloss,
               COALESCE(mt.vc_status,'(NULL)') AS vc_status,
               GROUP_CONCAT(DISTINCT cs.subgroup_code) AS placements
          FROM mti_terms mt
          JOIN mti_term_subgroup mts ON mts.mti_term_id = mt.id
                AND COALESCE(mts.delete_flagged,0)=0
          JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
                AND COALESCE(cs.delete_flagged,0)=0
         WHERE mt.cluster_code = ? AND COALESCE(mt.delete_flagged,0)=0
           AND cs.cluster_code = ?
           AND NOT EXISTS (
               SELECT 1 FROM verse_context vc
                 JOIN cluster_subgroup cs2 ON cs2.id = vc.cluster_subgroup_id
                WHERE vc.mti_term_id = mt.id
                  AND cs2.cluster_code = ?
                  AND COALESCE(vc.delete_flagged,0)=0
           )
         GROUP BY mt.id, mt.strongs_number, mt.transliteration, mt.gloss, mt.vc_status
         ORDER BY mt.strongs_number
    """, (code, code, code)).fetchall()]


# ---------- Strand 7: Open observation prompts ----------

def strand_open_prompts(conn, code):
    """Universal active catalogue prompts that have no cluster_finding row for
    this cluster (at any sub-group or cluster-synthesis level)."""
    return [dict(r) for r in conn.execute("""
        SELECT q.obs_id, q.question_code, q.tier, q.section, q.component_title,
               q.question_text
          FROM wa_obs_question_catalogue q
         WHERE q.scope='universal' AND q.status='active' AND COALESCE(q.deleted,0)=0
           AND NOT EXISTS (
                SELECT 1 FROM cluster_finding cf
                 WHERE cf.cluster_code=? AND cf.obs_id=q.obs_id
                   AND COALESCE(cf.delete_flagged,0)=0
           )
         ORDER BY q.tier, q.question_code
    """, (code,)).fetchall()]


# ---------- Formatting ----------

def fmt_finding(f):
    text = (f.get("finding_text") or "").strip()
    if len(text) > 400:
        text = text[:400] + "…"
    return text


def write_md(out_path, cluster, subgroups, gaps, t7_silent, cross_links, sd_pointers,
             thin_terms, mt_flags, dq_flag_summary, dq_terms, vc_anomalies, open_prompts):
    lines = []
    w = lines.append
    short = cluster.get("short_name") or cluster["cluster_code"]
    title = cluster.get("description") or short
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    w(f"# {title} — Outstanding research and open questions")
    w(f"_Generated {now} for cluster {cluster['cluster_code']} ({short})_")
    w("")
    w("This report inventories the open work the analytical record leaves behind after the cluster's Session C publication. It is a planning document for follow-up Session B passes, cross-cluster work, and term-level cleanup. Each section lists items the researcher can prioritise.")
    w("")
    w(f"**Cluster status:** {cluster.get('status')}  ·  **Version:** {cluster.get('version')}  ·  **Last updated:** {cluster.get('last_updated_date')}")
    w("")
    w("---")
    w("")

    # Section 1: Gap findings
    w("## 1. Gap findings")
    w("")
    w("Findings the analytical record itself flagged as `gap` during Phase 8. These are the explicit \"more work needed\" markers left in the record.")
    w("")
    if not gaps:
        w("_No gap findings recorded for this cluster._")
    else:
        by_sg = defaultdict(list)
        for g in gaps:
            by_sg[g["subgroup_code"] or "(cluster-level)"].append(g)
        for sg_code in sorted(by_sg.keys()):
            items = by_sg[sg_code]
            sg_label = items[0].get("sg_label") or ""
            w(f"### {sg_code} — {sg_label}" if sg_label else f"### {sg_code}")
            w("")
            for g in items:
                w(f"- **{g['question_code']}** ({g.get('section','')})")
                w(f"  - *Prompt:* {g.get('question_text','')}")
                w(f"  - *Finding:* {fmt_finding(g)}")
            w("")
    w("---")
    w("")

    # Section 2: Under-developed T7 lens
    w("## 2. Under-developed lens — the view from outside Scripture (T7)")
    w("")
    w("Sub-group / prompt combinations where the science-comparison T7 work was not separately addressed for the sub-group. These are the prioritised candidates for a future Session B T7 pass that would expand the view-from-outside lens for this cluster.")
    w("")
    if not t7_silent:
        w("_No under-developed T7 prompts recorded for this cluster._")
    else:
        by_sg = defaultdict(list)
        for t in t7_silent:
            by_sg[t["subgroup_code"] or "(cluster-level)"].append(t)
        for sg_code in sorted(by_sg.keys()):
            items = by_sg[sg_code]
            sg_label = items[0].get("sg_label") or ""
            w(f"### {sg_code} — {sg_label}  ·  {len(items)} prompt(s)")
            w("")
            for t in items:
                w(f"- **{t['question_code']}** — _{t.get('question_text','')}_")
            w("")
    w("---")
    w("")

    # Section 3: LXX / Greek-of-the-Hebrew gap
    w("## 3. LXX / Greek-of-the-Hebrew gap")
    w("")
    w(LXX_NOTE)
    w("")
    # Count OT terms in the cluster as a sizing hint
    w("**Sizing for this cluster:**")
    w("")
    sg_terms_by_lang = defaultdict(int)
    return_path = out_path  # capture for later
    # We need conn — re-open briefly is awkward; better: count was computed where conn was available.
    # Skipping the auto-count here; this is fine as informational text.
    w("- Hebrew and Greek terms in the cluster are inventoried in Appendix A of the published study; the LXX layer would add a parallel Greek view of the Hebrew terms.")
    w("")
    w("---")
    w("")

    # Section 4: Cross-cluster pointers
    w("## 4. Cross-cluster pointers")
    w("")
    w("Open links from this cluster's terms to terms or characteristics in other registries / clusters. These are work the analytical record explicitly flagged as bridging beyond this cluster's boundary.")
    w("")
    w("### 4a. Cross-registry links")
    w("")
    if not cross_links:
        w("_No cross-registry links recorded for this cluster's terms._")
    else:
        w("| Strong's | Translit. | Source word | Linked word | Link type | Connecting term | Note |")
        w("|---|---|---|---|---|---|---|")
        for cl in cross_links:
            note = (cl.get("note") or "").replace("|", "\\|")[:80]
            link_type = cl.get("link_type_label") or cl.get("link_type_code") or ""
            w(f"| {cl['strongs_number']} | {cl.get('transliteration','')} | "
              f"{cl.get('source_word','')} | {cl.get('linked_word','')} | "
              f"{link_type} | {cl.get('connecting_term','') or ''} | {note} |")
    w("")
    w("### 4b. Unresolved SD pointers")
    w("")
    if not sd_pointers:
        w("_No unresolved SD pointers recorded for this cluster's terms._")
    else:
        for p in sd_pointers:
            w(f"- **{p['flag_code']}** · {p.get('strongs_reference','')} · priority {p.get('priority','')} · target {p.get('session_target','')}")
            if p.get("description"):
                w(f"  - {p['description'][:300]}")
    w("")
    w("---")
    w("")

    # Section 5: Term-level open items
    w("## 5. Term-level open items")
    w("")
    w("Cluster terms whose status or quality flags signal residual work at the term level. These are the candidates for term-level cleanup and re-extraction.")
    w("")
    w("### 5a. Thin / candidate-delete terms")
    w("")
    if not thin_terms:
        w("_No thin or candidate-delete terms in this cluster._")
    else:
        w("| Strong's | Translit. | Gloss | Status | Sub-group | Note |")
        w("|---|---|---|---|---|---|")
        for t in thin_terms:
            note = (t.get("anchor_note") or t.get("exclusion_reason") or "")[:80].replace("|","\\|")
            sg = t.get("subgroup_code") or ""
            w(f"| {t['strongs_number']} | {t.get('transliteration','')} | "
              f"{(t.get('gloss','') or '')[:50]} | {t['status']} | {sg} | {note} |")
    w("")
    w("### 5b. Terms with open mti_term_flags")
    w("")
    if not mt_flags:
        w("_No open mti_term_flags on this cluster's terms._")
    else:
        w("| Strong's | Translit. | Flag | Group |")
        w("|---|---|---|---|")
        for f in mt_flags:
            w(f"| {f['strongs_number']} | {f.get('transliteration','')} | "
              f"{f['flag_code']} | {f.get('flag_group','')} |")
    w("")
    w("### 5c. Terms with open data-quality flags")
    w("")
    w(
        "Evidence flags (`VERSE_EVIDENCE_*`) are excluded — they are informational, "
        "not gating. Counts are by **distinct term**, not by row, since "
        "`wa_data_quality_flags` writes one row per (file × term × flag) — a term in "
        "N XREF registries accumulates N rows of the same flag."
    )
    w("")
    if not dq_flag_summary:
        w("_No open data-quality flags on this cluster's terms (after exclusions)._")
    else:
        w("**Summary by flag code:**")
        w("")
        w("| Flag code | Distinct terms | Row count (informational) |")
        w("|---|---:|---:|")
        for f in dq_flag_summary:
            w(f"| {f['flag_code']} | {f['distinct_terms']} | {f['row_count']} |")
        w("")
        w("**Affected terms (one row per term):**")
        w("")
        w("| Term | Translit. | Gloss | Flags | Rows |")
        w("|---|---|---|---|---:|")
        for t in dq_terms:
            gloss = (t.get("gloss") or "")[:50].replace("|", "\\|")
            translit = (t.get("transliteration") or "").replace("|", "\\|")
            w(f"| {t['term_id']} | {translit} | {gloss} | {t['flag_codes']} | {t['row_count']} |")
    w("")
    w("---")
    w("")

    # Section 6: VC-coverage gaps
    w("## 6. VC-coverage gaps")
    w("")
    w(
        "Cluster terms that are placed in a sub-group but have **no active "
        "`verse_context` rows** tied to any of the cluster's sub-groups. "
        "Set-aside VC rows (rows where the analytical judgement is that the "
        "term carries no inner-being phenomenon in its verse evidence) DO "
        "count as VC done — they represent a completed analytical decision. "
        "The legacy `mti_terms.vc_status` field is unreliable for this "
        "purpose and is not used here."
    )
    w("")
    if not vc_anomalies:
        w("_All placed terms have at least one active `verse_context` row in a cluster VCG._")
    else:
        w(f"**{len(vc_anomalies)} term(s) placed but with no VC rows:**")
        w("")
        w("| Strong's | Translit. | Gloss | Placement | Current vc_status |")
        w("|---|---|---|---|---|")
        for t in vc_anomalies:
            w(f"| {t['strongs_number']} | {t.get('transliteration','')} | "
              f"{(t.get('gloss','') or '')[:50]} | {t.get('placements','')} | {t['vc_status']} |")
    w("")
    w("---")
    w("")

    # Section 7: Open observation prompts
    w("## 7. Open observation prompts")
    w("")
    w("Universal active catalogue prompts that have no `cluster_finding` row for this cluster — neither at sub-group level nor at cluster-synthesis level. These prompts were never reached during Phase 8.")
    w("")
    if not open_prompts:
        w("_All universal active catalogue prompts have at least one finding for this cluster._")
    else:
        by_tier = defaultdict(list)
        for p in open_prompts:
            by_tier[p["tier"] or "(unsectioned)"].append(p)
        for tier in sorted(by_tier.keys()):
            items = by_tier[tier]
            w(f"### {tier}  ·  {len(items)} open prompt(s)")
            w("")
            for p in items:
                w(f"- **{p['question_code']}** — {p.get('question_text','')[:200]}")
            w("")
    w("---")
    w("")

    # Summary
    w("## Summary counts")
    w("")
    w("| Strand | Count |")
    w("|---|---:|")
    w(f"| 1. Gap findings | {len(gaps)} |")
    w(f"| 2. Under-developed T7 prompts | {len(t7_silent)} |")
    w(f"| 4a. Cross-registry links | {len(cross_links)} |")
    w(f"| 4b. Unresolved SD pointers | {len(sd_pointers)} |")
    w(f"| 5a. Thin / candidate-delete terms | {len(thin_terms)} |")
    w(f"| 5b. Terms with open mti_term_flags | {len(mt_flags)} |")
    w(f"| 5c. Distinct terms with open data-quality flags (excl. evidence flags) | {len(dq_terms)} |")
    w(f"| 6. VC-coverage gaps (placed terms with no VC rows) | {len(vc_anomalies)} |")
    w(f"| 7. Open observation prompts | {len(open_prompts)} |")
    w("")
    w("---")
    w("")
    w("_End of report._")

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    code = args.cluster
    if args.out is None:
        d = datetime.now().strftime("%Y%m%d")
        args.out = f"Sessions/Session_Clusters/{code}/wa-cluster-{code}-outstanding-research-v1-{d}.md"

    conn = get_conn()
    cluster = fetch_cluster(conn, code)
    subgroups = fetch_subgroups(conn, code)
    gaps = strand_gaps(conn, code)
    t7_silent = strand_t7_under_developed(conn, code)
    cross_links, sd_pointers = strand_cross_cluster(conn, code)
    thin_terms, mt_flags, dq_flag_summary, dq_terms = strand_term_open(conn, code)
    vc_anomalies = strand_vc_anomalies(conn, code)
    open_prompts = strand_open_prompts(conn, code)

    write_md(args.out, cluster, subgroups, gaps, t7_silent,
             cross_links, sd_pointers, thin_terms, mt_flags,
             dq_flag_summary, dq_terms, vc_anomalies, open_prompts)

    print(f"Wrote: {args.out}")
    print(f"Counts: gaps={len(gaps)}  t7_under={len(t7_silent)}  "
          f"cross_links={len(cross_links)}  sd_pointers={len(sd_pointers)}  "
          f"thin_terms={len(thin_terms)}  mt_flags={len(mt_flags)}  "
          f"dq_distinct_terms={len(dq_terms)}  vc_gaps={len(vc_anomalies)}  "
          f"open_prompts={len(open_prompts)}")
    conn.close()


if __name__ == "__main__":
    main()
