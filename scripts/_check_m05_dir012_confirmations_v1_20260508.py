"""_check_m05_dir012_confirmations_v1_20260508.py — read-only.

Runs the Completion Confirmation queries (Q1..Q7) plus the G-code
resolution queries (Q8) from DIR-20260507-M05-012, and emits results
to stdout for the application report.
"""
from __future__ import annotations

import os
import sqlite3
import sys

DB_PATH = os.path.join("database", "bible_research.db")


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    out = sys.stdout

    def section(title):
        out.write("\n" + "=" * 60 + "\n")
        out.write(f"  {title}\n")
        out.write("=" * 60 + "\n")

    # Q1 — schema confirmation
    section("Q1 — Schema confirmation")
    r = cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' "
        "  AND name='cluster_finding'"
    ).fetchone()
    out.write(f"  cluster_finding table exists: {bool(r)}\n")
    n = cur.execute(
        "SELECT COUNT(*) FROM wa_obs_question_catalogue "
        " WHERE catalogue_version='v2-2026-04-29' AND COALESCE(deleted,0)=0"
    ).fetchone()[0]
    out.write(f"  catalogue_version='v2-2026-04-29' rows: {n} (expected 189)\n")

    # Q2 — finding_status distribution
    section("Q2 — Row counts by finding_status (M05)")
    out.write("  finding_status            n\n")
    out.write("  -" * 30 + "\n")
    for r in cur.execute(
        "SELECT finding_status, COUNT(*) AS n FROM cluster_finding "
        " WHERE cluster_code='M05' AND COALESCE(delete_flagged,0)=0 "
        " GROUP BY finding_status ORDER BY finding_status"
    ):
        out.write(f"  {r['finding_status']:24s} {r['n']:5d}\n")
    total = cur.execute(
        "SELECT COUNT(*) FROM cluster_finding "
        " WHERE cluster_code='M05' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    out.write(f"  TOTAL                    {total:5d}\n")

    # Q3 — per-sub-group counts
    section("Q3 — Per sub-group row counts (M05)")
    out.write("  subgroup        label                                   n\n")
    out.write("  " + "-" * 60 + "\n")
    for r in cur.execute(
        """
        SELECT cs.subgroup_code, cs.label, COUNT(cf.id) AS n
          FROM cluster_subgroup cs
          LEFT JOIN cluster_finding cf
            ON cf.cluster_subgroup_id = cs.id
           AND cf.cluster_code='M05'
           AND COALESCE(cf.delete_flagged,0)=0
         WHERE cs.cluster_code='M05'
           AND COALESCE(cs.delete_flagged,0)=0
         GROUP BY cs.subgroup_code
         ORDER BY cs.subgroup_code
        """
    ):
        out.write(f"  {r['subgroup_code']:14s} {r['label'][:40]:40s} {r['n']:5d}\n")
    n_null = cur.execute(
        "SELECT COUNT(*) FROM cluster_finding "
        " WHERE cluster_code='M05' AND cluster_subgroup_id IS NULL "
        "   AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    out.write(f"  CLUSTER-LEVEL  (cluster_subgroup_id IS NULL)            {n_null:5d}\n")

    # Q4 — gap rows
    section("Q4 — Gap-status rows (M05)")
    rows = list(cur.execute(
        """
        SELECT cf.id, q.question_code,
               CASE WHEN cf.cluster_subgroup_id IS NULL THEN 'CLUSTER'
                    ELSE cs.subgroup_code END AS scope,
               SUBSTR(cf.finding_text, 1, 200) AS excerpt
          FROM cluster_finding cf
          LEFT JOIN wa_obs_question_catalogue q ON q.obs_id=cf.obs_id
          LEFT JOIN cluster_subgroup cs ON cs.id=cf.cluster_subgroup_id
         WHERE cf.cluster_code='M05'
           AND cf.finding_status='gap'
           AND COALESCE(cf.delete_flagged,0)=0
         ORDER BY q.question_code, scope
        """
    ))
    out.write(f"  Gap rows total: {len(rows)}\n\n")
    for r in rows:
        out.write(f"  cf.id={r['id']:5d}  q={r['question_code']:8s}  scope={r['scope']}\n")
        out.write(f"    excerpt: {r['excerpt']}\n\n")

    # Q5 — 3-row representative sample
    section("Q5 — 3-row representative sample")
    rows = list(cur.execute(
        """
        SELECT q.question_code, cs.subgroup_code, cf.finding_status,
               SUBSTR(cf.finding_text, 1, 300) AS excerpt, cf.source_file
          FROM cluster_finding cf
          JOIN wa_obs_question_catalogue q ON q.obs_id=cf.obs_id
          JOIN cluster_subgroup cs ON cs.id=cf.cluster_subgroup_id
         WHERE cf.cluster_code='M05'
           AND q.question_code IN ('T0.1.1','T2.1.1','T5.1.1')
           AND cs.subgroup_code IN ('M05-A','M05-D','M05-G')
           AND COALESCE(cf.delete_flagged,0)=0
         ORDER BY q.question_code, cs.subgroup_code
        """
    ))
    out.write(f"  Rows returned: {len(rows)}\n\n")
    for r in rows:
        out.write(f"  q={r['question_code']}  sg={r['subgroup_code']}  "
                  f"status={r['finding_status']}\n")
        out.write(f"    source: {r['source_file']}\n")
        out.write(f"    excerpt: {r['excerpt']}\n\n")

    # Q6 — wa_session_b_findings unchanged
    section("Q6 — wa_session_b_findings count (M05 registries)")
    n = cur.execute(
        """
        SELECT COUNT(*) FROM wa_session_b_findings
         WHERE registry_id IN (
           SELECT DISTINCT owning_registry_fk
             FROM mti_terms WHERE cluster_code='M05'
         )
        """
    ).fetchone()[0]
    out.write(f"  Session B findings linked to any M05-owning registry: {n}\n")
    out.write("  (Pre-directive count not snapshotted; we did not write to "
              "wa_session_b_findings in this directive.)\n")

    # Q7 — VCREVISE confirmation
    section("Q7 — VCREVISE patch result (Amo 5:21 + 2Pe 1:3)")
    for vrid, mti in ((192566, 6209), (215044, 6845)):
        r = cur.execute(
            """
            SELECT vc.id AS vc_id, vc.verse_record_id, vc.mti_term_id,
                   vc.is_relevant, vc.group_id, vc.set_aside_reason,
                   b.short_code||' '||vr.chapter||':'||vr.verse_num AS ref
              FROM verse_context vc
              JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
              JOIN books b ON b.id=vr.book_id
             WHERE vc.verse_record_id=? AND vc.mti_term_id=?
            """, (vrid, mti)
        ).fetchone()
        if r:
            out.write(f"  vr={vrid} mti={mti} ({r['ref']}): "
                      f"is_rel={r['is_relevant']} grp={r['group_id']} "
                      f"sar={r['set_aside_reason']}\n")
        else:
            out.write(f"  vr={vrid} mti={mti}: NOT FOUND\n")

    # Q8 — G-code resolutions (informational)
    section("Q8 — G-code T6.4.3: cross-registry chesed (H2617A) distribution")
    rows = list(cur.execute(
        """
        SELECT mt.owning_registry_fk AS registry_id,
               COUNT(vc.id) AS verse_context_rows
          FROM mti_terms mt
          JOIN verse_context vc ON vc.mti_term_id=mt.id
         WHERE mt.strongs_number='H2617A'
           AND mt.status IN ('extracted','extracted_thin','extracted_theological_anchor')
           AND COALESCE(mt.delete_flagged,0)=0
           AND COALESCE(vc.delete_flagged,0)=0
         GROUP BY mt.owning_registry_fk
         ORDER BY verse_context_rows DESC
        """
    ))
    out.write(f"  Rows: {len(rows)}\n")
    for r in rows:
        wr = cur.execute(
            "SELECT word FROM word_registry WHERE no=?",
            (r['registry_id'],)
        ).fetchone()
        word = wr['word'] if wr else ""
        out.write(f"  registry={r['registry_id']} ({word}): "
                  f"vc_rows={r['verse_context_rows']}\n")

    section("Q8 — G-code T6.6.3: M05 anchor-verse cross-cluster overlap")
    rows = list(cur.execute(
        """
        SELECT vc.verse_record_id,
               b.short_code||' '||vr.chapter||':'||vr.verse_num AS ref,
               COUNT(DISTINCT vcg.mti_term_id) AS term_count,
               COUNT(DISTINCT mt.cluster_code) AS cluster_count,
               GROUP_CONCAT(DISTINCT mt.cluster_code) AS clusters
          FROM verse_context vc
          JOIN verse_context_group vcg ON vcg.id=vc.group_id
          JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
          JOIN books b ON b.id=vr.book_id
          JOIN mti_terms mt ON mt.id=vcg.mti_term_id
         WHERE vc.is_anchor=1
           AND vc.verse_record_id IN (
             SELECT vc2.verse_record_id FROM verse_context vc2
              JOIN verse_context_group vcg2 ON vcg2.id=vc2.group_id
              JOIN mti_terms mt2 ON mt2.id=vcg2.mti_term_id
             WHERE vc2.is_anchor=1 AND mt2.cluster_code='M05'
               AND COALESCE(vc2.delete_flagged,0)=0
               AND COALESCE(vcg2.delete_flagged,0)=0
               AND COALESCE(mt2.delete_flagged,0)=0
           )
           AND COALESCE(vc.delete_flagged,0)=0
           AND COALESCE(vcg.delete_flagged,0)=0
           AND COALESCE(mt.delete_flagged,0)=0
         GROUP BY vc.verse_record_id
         HAVING cluster_count>1 OR term_count>1
         ORDER BY cluster_count DESC, ref
        """
    ))
    out.write(f"  M05 anchor verses appearing in other clusters/terms: {len(rows)}\n")
    for r in rows[:25]:
        out.write(f"  vr={r['verse_record_id']:6d} {r['ref']:14s} "
                  f"terms={r['term_count']} clusters={r['cluster_count']} "
                  f"({r['clusters']})\n")
    if len(rows) > 25:
        out.write(f"  ... ({len(rows)-25} more rows truncated)\n")

    section("Q8 — G-code T6.7.3: prompts with both subgroup + synthesis")
    rows = list(cur.execute(
        """
        SELECT q.question_code,
               COUNT(cf.id) AS total_rows,
               SUM(CASE WHEN cf.cluster_subgroup_id IS NULL THEN 1 ELSE 0 END)
                 AS synthesis_rows,
               SUM(CASE WHEN cf.cluster_subgroup_id IS NOT NULL THEN 1 ELSE 0 END)
                 AS subgroup_rows
          FROM cluster_finding cf
          JOIN wa_obs_question_catalogue q ON q.obs_id=cf.obs_id
         WHERE cf.cluster_code='M05'
           AND cf.finding_status IN ('finding','cluster_synthesis')
           AND cf.finding_text NOT LIKE '[Sub-group not separately%'
           AND COALESCE(cf.delete_flagged,0)=0
         GROUP BY q.question_code
        HAVING synthesis_rows>0 AND subgroup_rows>0
         ORDER BY q.question_code
        """
    ))
    out.write(f"  Prompts with both: {len(rows)}\n")
    for r in rows:
        out.write(f"  {r['question_code']:8s} total={r['total_rows']:3d} "
                  f"synthesis={r['synthesis_rows']} "
                  f"subgroup={r['subgroup_rows']}\n")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
