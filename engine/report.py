"""
report.py
─────────
Word overview report — engine.py --report [--registry=N]

Prints a structured summary of a word's data to stdout.
Optionally exports to Markdown or CSV.

Sections:
  1 — Registry header (word, status, cluster, pipeline position)
  2 — Term inventory (OWNER/XREF, strongs, gloss, evidential status)
  3 — Verse Context summary (groups, anchors, set-aside, dimension profile)
  4 — Quality flags & Phase 2 flags
  5 — Audit state (latest word_run_state)
  6 — Session B readiness assessment
"""

from __future__ import annotations

import json
from datetime import datetime, timezone


def print_word_report(conn, registry_id: int,
                      format: str = "text",
                      out=None) -> None:
    """Print a complete word overview report.

    Args:
        conn:         Open database connection.
        registry_id:  word_registry.no for the target word.
        format:       'text' (default) or 'markdown'.
        out:          File-like object; defaults to sys.stdout.
    """
    import sys
    out = out or sys.stdout

    def p(line: str = "") -> None:
        print(line, file=out)

    def h1(title: str) -> None:
        if format == "markdown":
            p(f"# {title}")
        else:
            p(f"\n{'='*70}")
            p(f"  {title}")
            p(f"{'='*70}")

    def h2(title: str) -> None:
        if format == "markdown":
            p(f"\n## {title}")
        else:
            p(f"\n── {title} {'─' * (60 - len(title))}")

    def kv(key: str, val) -> None:
        if val is None:
            val = "(null)"
        p(f"  {key:<28} {val}")

    # ── Section 1: Registry ────────────────────────────────────────────────────
    reg_row = conn.execute(
        "SELECT * FROM word_registry WHERE no = ?", (registry_id,)
    ).fetchone()
    if not reg_row:
        p(f"[ERROR] No word_registry row for no={registry_id}")
        return

    h1(f"Word Report — {reg_row['word']} (registry no={registry_id})")
    p(f"  Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')} UTC")

    h2("Registry")
    kv("word", reg_row["word"])
    kv("registry no", reg_row["no"])
    kv("cluster", reg_row["cluster_assignment"])
    kv("phase1_status", reg_row["phase1_status"])
    kv("session_b_status", reg_row["session_b_status"])
    kv("verse_context_status", reg_row["verse_context_status"])
    kv("phase1_term_count", reg_row["phase1_term_count"])
    kv("phase1_verse_count", reg_row["phase1_verse_count"])
    kv("dimensions", reg_row["dimensions"])
    kv("source_list", reg_row["source_list"])

    # Sharing stats
    kv("unique_term_count", reg_row["unique_term_count"])
    kv("shared_term_count", reg_row["shared_term_count"])
    ratio = reg_row["term_sharing_ratio"]
    kv("term_sharing_ratio", f"{ratio:.0%}" if ratio is not None else "(null)")

    # ── Section 2: Terms ──────────────────────────────────────────────────────
    fi_rows = conn.execute(
        "SELECT id FROM wa_file_index WHERE word_registry_fk = ? ORDER BY id",
        (reg_row["id"],),
    ).fetchall()

    if not fi_rows:
        h2("Terms")
        p("  (no file_index entries)")
        return

    file_ids = [fi["id"] for fi in fi_rows]

    terms = conn.execute(
        """SELECT ti.id, ti.strongs_number, ti.term_id, ti.language,
                  ti.transliteration, ti.step_search_gloss, ti.occurrence_count,
                  ti.testament, ti.term_owner_type, ti.delete_flagged,
                  ti.evidential_status, ti.retention_note,
                  mt.status as mti_status, mt.id as mti_term_id,
                  (SELECT COUNT(*) FROM wa_verse_records vr
                   WHERE vr.term_inv_id = ti.id AND vr.delete_flagged = 0) AS active_verses,
                  (SELECT COUNT(*) FROM verse_context_group vcg
                   WHERE vcg.mti_term_id = mt.id AND vcg.delete_flagged = 0) AS vc_groups,
                  (SELECT COUNT(*) FROM verse_context vc
                   WHERE vc.mti_term_id = mt.id AND vc.is_anchor = 1 AND vc.delete_flagged = 0) AS anchors,
                  (SELECT COUNT(*) FROM verse_context vc
                   WHERE vc.mti_term_id = mt.id AND vc.is_relevant = 0 AND vc.delete_flagged = 0) AS set_aside
           FROM wa_term_inventory ti
           LEFT JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
               AND mt.status IN ('extracted', 'extracted_thin')
           WHERE ti.file_id IN ({})
           ORDER BY ti.term_owner_type DESC, ti.delete_flagged, ti.strongs_number""".format(
            ",".join("?" * len(file_ids))),
        file_ids,
    ).fetchall()

    # Separate OWNER and XREF
    owner_terms = [t for t in terms if t["term_owner_type"] == "OWNER" and t["delete_flagged"] == 0]
    xref_terms = [t for t in terms if t["term_owner_type"] == "XREF" and t["delete_flagged"] == 0]
    deleted_terms = [t for t in terms if t["delete_flagged"] == 1]

    h2(f"OWNER Terms ({len(owner_terms)})")
    for t in owner_terms:
        strongs = t["strongs_number"] or t["term_id"]
        ev = f" [{t['evidential_status']}]" if t["evidential_status"] else ""
        mti = f" mti={t['mti_term_id']}" if t["mti_term_id"] else ""
        p(f"  {strongs:12} {t['transliteration']:20} '{t['step_search_gloss']}'"
          f"  ({t['language']}){ev}{mti}")
        p(f"    verses: {t['active_verses']}  groups: {t['vc_groups']}"
          f"  anchors: {t['anchors']}  set-aside: {t['set_aside']}"
          f"  mti_status: {t['mti_status']}")

    if xref_terms:
        h2(f"XREF Terms ({len(xref_terms)})")
        for t in xref_terms:
            strongs = t["strongs_number"] or t["term_id"]
            p(f"  {strongs:12} {t['transliteration']:20} '{t['step_search_gloss']}'"
              f"  ({t['language']})  mti_status: {t['mti_status']}")

    if deleted_terms:
        p(f"\n  ({len(deleted_terms)} delete_flagged terms not shown)")

    # ── Section 3: Verse Context Summary ─────────────────────────────────────
    h2("Verse Context Summary")

    # Aggregate across OWNER terms
    fid_placeholders = ",".join("?" * len(file_ids))
    vc_stats = conn.execute(
        f"""SELECT
            COUNT(DISTINCT vcg.id) as total_groups,
            SUM(CASE WHEN vc.is_anchor = 1 THEN 1 ELSE 0 END) as total_anchors,
            SUM(CASE WHEN vc.is_relevant = 1 THEN 1 ELSE 0 END) as total_relevant,
            SUM(CASE WHEN vc.is_relevant = 0 THEN 1 ELSE 0 END) as total_set_aside
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
          AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
        LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id AND vcg.delete_flagged = 0
        WHERE ti.file_id IN ({fid_placeholders}) AND vc.delete_flagged = 0
        """,
        file_ids,
    ).fetchone()

    if vc_stats and vc_stats["total_groups"]:
        kv("contextual groups", vc_stats["total_groups"])
        kv("anchor verses", vc_stats["total_anchors"])
        kv("relevant verses", vc_stats["total_relevant"])
        kv("set-aside verses", vc_stats["total_set_aside"])
    else:
        p("  (no verse context data)")

    # Dimension profile from wa_dimension_index
    dims = conn.execute(
        """SELECT di.dimension, COUNT(*) as c
        FROM wa_dimension_index di
        JOIN wa_term_inventory ti ON ti.strongs_number = di.strongs_number
          AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
        WHERE ti.file_id IN ({}) AND di.dimension IS NOT NULL AND di.delete_flagged = 0
        GROUP BY di.dimension ORDER BY c DESC""".format(
            ",".join("?" * len(file_ids))),
        file_ids,
    ).fetchall()

    if dims:
        p("\n  Dimension profile:")
        for d in dims:
            p(f"    {d['dimension']:>30}: {d['c']} groups")

    # Top groups by verse count
    top_groups = conn.execute(
        """SELECT vcg.group_code, vcg.context_description, di.dimension,
            (SELECT COUNT(*) FROM verse_context vc WHERE vc.group_id = vcg.id
             AND vc.delete_flagged = 0) as verse_count
        FROM verse_context_group vcg
        JOIN mti_terms mt ON mt.id = vcg.mti_term_id
        JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
          AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
        LEFT JOIN wa_dimension_index di ON di.verse_context_group_id = vcg.id AND di.delete_flagged = 0
        WHERE ti.file_id IN ({}) AND vcg.delete_flagged = 0
        ORDER BY verse_count DESC LIMIT 10""".format(
            ",".join("?" * len(file_ids))),
        file_ids,
    ).fetchall()

    if top_groups:
        p("\n  Top contextual groups:")
        for g in top_groups:
            dim = f" [{g['dimension']}]" if g["dimension"] else ""
            desc = g["context_description"][:80]
            p(f"    {g['group_code']:12} ({g['verse_count']:3d}v){dim}  {desc}")

    # ── Section 4: Quality flags ───────────────────────────────────────────────
    flags = conn.execute(
        """SELECT dqf.term_id, qft.flag_group, qft.flag_code, dqf.description
           FROM wa_data_quality_flags dqf
           JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id
           WHERE dqf.file_id IN ({})
           ORDER BY qft.flag_group, qft.flag_code""".format(
            ",".join("?" * len(file_ids))),
        file_ids,
    ).fetchall()

    h2(f"Quality Flags ({len(flags)})")
    if flags:
        for fl in flags:
            t_id = fl["term_id"] or "(file-level)"
            p(f"  [{fl['flag_group']}] {fl['flag_code']:35} term: {t_id}")
    else:
        p("  (none)")

    # ── Section 5: Audit state ─────────────────────────────────────────────────
    audit_row = conn.execute(
        """SELECT run_id, phase_reached, audit_result, audit_detail, stop_reason
           FROM word_run_state WHERE registry_id = ?
           ORDER BY id DESC LIMIT 1""",
        (str(registry_id).zfill(3),),
    ).fetchone()

    h2("Latest Audit")
    if audit_row:
        kv("run_id", audit_row["run_id"])
        kv("phase_reached", audit_row["phase_reached"])
        kv("audit_result", audit_row["audit_result"])
        if audit_row["stop_reason"]:
            kv("stop_reason", audit_row["stop_reason"])
        if audit_row["audit_detail"]:
            try:
                checks = json.loads(audit_row["audit_detail"])
                non_pass = {k: v for k, v in checks.items() if v.get("r") != "PASS"}
                if non_pass:
                    p("  Non-PASS checks:")
                    for check_id, info in non_pass.items():
                        p(f"    {check_id}: [{info.get('r')}] {info.get('d', '')}")
            except (json.JSONDecodeError, TypeError, AttributeError):
                pass
    else:
        p("  (no audit run recorded)")

    # ── Section 6: Session B Readiness ────────────────────────────────────────
    h2("Session B Readiness")

    vc_status = reg_row["verse_context_status"]
    sb_status = reg_row["session_b_status"]
    ev_count = conn.execute(
        """SELECT COUNT(*) FROM wa_term_inventory
        WHERE file_id IN ({}) AND evidential_status IS NOT NULL AND delete_flagged = 0""".format(
            ",".join("?" * len(file_ids))),
        file_ids,
    ).fetchone()[0]

    kv("verse_context_status", vc_status)
    kv("session_b_status", sb_status)
    kv("terms with evidential_status", ev_count)

    if vc_status == "Complete" and sb_status in (None, "Verse Context Reset"):
        p("  → Ready for DataPrep (verse context complete, awaiting pre-analysis)")
    elif sb_status == "Pre-Analysis Complete":
        p("  → Ready for pool-based Analysis")
    elif sb_status == "Analysis Complete":
        p("  → Ready for Extraction")
    elif sb_status == "Session B Complete":
        p("  → Session B cycle complete")
    else:
        p(f"  → Pipeline position: {sb_status or 'not started'}")

    p()
