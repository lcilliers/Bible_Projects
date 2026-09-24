"""Register `purge.execute` -- the app-wide soft-delete purge REMOVAL step (escalation #1766 part
c, researcher instruction 2026-09-24: "my aim today is to clean out bible_research_db of all soft
deleted rows... proceed with the safe to purge").

Adds the removal half `register_purge_audit_step_v1_20260919.py` deliberately left unbuilt. Same
work package (`purge-audit`), second step (`purge.execute`, ordinal 1). `-Preview` (default true)
recomputes the safe/unsafe split fresh every run and previews counts only; `-Live` actually
deletes, one transaction per database, verifying each table reads back 0 afterward. Only ever
touches a table that is BOTH currently safe (recomputed, not cached) AND explicitly present in
`cfg_write_grant` for writer='purge.execute' -- an intentional allow-list, not "every table the
live audit happens to call safe today". Grants are seeded here for the 34 tables the 2026-09-24
audit (research/discovery/purge-audit-v4-20260924.md) found safe; a table that becomes safe later
needs its own added grant (a fresh researcher check-in point, not an automatic escalation).

bible_research.db is in scope: `cfg_behaviour_rule` 'bible-research-db-excluded-from-iba-results'
was amended 2026-09-24 (escalation #1868/#1870) to exempt registered DB-hygiene/maintenance
utilities from the general exclusion -- this is that exemption's first real use.

Safe to re-run: every insert is guarded, no-ops if already present.

Usage:
    python iba/app/migration/register_purge_execute_step_v1_20260924.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

# (database, table) -- the 34 tables research/discovery/purge-audit-v4-20260924.md found safe
# (zero live dependency risk; a handful are below purge.unsafe_check_min_soft_deleted and were
# never dependency-checked, same as the audit's own "no (at/under threshold)" rows).
GRANTED_TABLES = [
    ("iba", "verse_passage"), ("iba", "passage"), ("iba", "span"), ("iba", "cluster_strong"),
    ("iba", "strong_related"), ("iba", "candidate_seed"), ("iba", "strong_meaning_tree"),
    ("iba", "word_strong"), ("iba", "strong"), ("iba", "strong_sense"), ("iba", "verse_hib"),
    ("iba", "strong_lexicon"), ("iba", "operation_party"), ("iba", "operation"),
    ("iba", "phenomenon"), ("iba", "hib"), ("iba", "cluster"), ("iba", "hib_referent_option"),
    ("iba", "wa_obs_question_catalogue"), ("iba", "passage_emergent_question"),
    ("bible_research", "ve_lexical"), ("bible_research", "ve_lexical_legacy"),
    ("bible_research", "vcg_term"), ("bible_research", "cluster_finding"),
    ("bible_research", "wa_finding_catalogue_links"), ("bible_research", "finding_question_link"),
    ("bible_research", "mti_term_subgroup"), ("bible_research", "segment_unit"),
    ("bible_research", "wa_dimension_index"), ("bible_research", "wa_term_root_family"),
    ("bible_research", "cluster_subgroup"), ("bible_research", "finding_verse_link"),
    ("bible_research", "ve_lexical_faculty_backup"), ("bible_research", "wa_term_phase2_flags"),
]


def row_exists(cur, sql, params) -> bool:
    return cur.execute(sql, params).fetchone() is not None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")

        if not row_exists(cur, "SELECT 1 FROM cfg_setting WHERE key=?",
                          ("purge.execute_report_path",)):
            cur.execute(
                "INSERT INTO cfg_setting (key, value, use, module, inactive) VALUES (?,?,?,?,0)",
                ("purge.execute_report_path", '"research/discovery/purge-execute.md"',
                 "where purge.execute persists its findings -- escalation #1766/#1868",
                 "validation"))
            report.append("cfg_setting purge.execute_report_path inserted")
        else:
            report.append("cfg_setting purge.execute_report_path already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_report WHERE step=?", ("purge.execute",)):
            cur.execute(
                "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
                "naming_scheme, archive_dir, inactive) VALUES (?,?,?,?,?,?,?,0)",
                ("purge.execute", "Soft-delete purge execute (app-wide, #1766/#1868)", 1, None,
                 "md", "stable", "archive"))
            report.append("cfg_report purge.execute inserted")
        else:
            report.append("cfg_report purge.execute already present — skipped")

        for ordinal, key, heading in (
            (0, "summary", "## Summary"),
            (1, "purged", "## Purged"),
            (2, "skipped", "## Skipped"),
        ):
            if not row_exists(cur, "SELECT 1 FROM cfg_report_section WHERE step=? AND "
                                    "section_key=?", ("purge.execute", key)):
                cur.execute(
                    "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, "
                    "toc_label, include, inactive) VALUES (?,?,?,?,?,1,0)",
                    ("purge.execute", ordinal, key, heading, heading.lstrip("# ")))
                report.append(f"cfg_report_section purge.execute/{key} inserted")
            else:
                report.append(f"cfg_report_section purge.execute/{key} already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_step WHERE step=?", ("purge.execute",)):
            cur.execute(
                "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                "inactive, kind) VALUES (?,?,?,?,?,?,0,?)",
                ("purge-audit", 1, "purge.execute", "iba.app.handlers.purge:execute", "none",
                 "Recomputes the safe/unsafe split fresh (never trusts a cached audit), "
                 "intersects with cfg_write_grant (writer='purge.execute') so only explicitly "
                 "allow-listed tables are ever touched. -Preview (default true) counts only, "
                 "nothing written. -Live actually deletes every soft-deleted row in each "
                 "granted-and-currently-safe table, one transaction per database, and verifies "
                 "each table reads back 0 soft-deleted rows afterward. A table that is UNSAFE or "
                 "ungranted is always skipped and reported, never silently included.",
                 "operations"))
            report.append("cfg_step purge.execute inserted")
        else:
            report.append("cfg_step purge.execute already present — skipped")

        for database, table in GRANTED_TABLES:
            if not row_exists(cur, "SELECT 1 FROM cfg_write_grant WHERE writer=? AND "
                                    "table_name=? AND database=?",
                              ("purge.execute", table, database)):
                cur.execute(
                    "INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
                    "VALUES (?,?,?,0)", ("purge.execute", table, database))
                report.append(f"cfg_write_grant purge.execute/{database}.{table} inserted")
            else:
                report.append(f"cfg_write_grant purge.execute/{database}.{table} already "
                              f"present — skipped")

        cur.execute(
            "UPDATE cfg_utility SET purpose=? WHERE file_path=?",
            ("purge.py -- app-wide soft-delete purge audit + execute (escalation #1766/#1868): "
             "per-table soft-deleted counts + live-dependency safety check across both databases "
             "(audit, read-only), plus allow-listed row removal against tables both currently "
             "safe and granted (execute, preview-then-live). Both always persist a report.",
             "iba/app/handlers/purge.py"))
        report.append("cfg_utility purge purpose updated")

        if args.dry_run:
            conn.rollback()
            report.append("DRY-RUN: rolled back")
        else:
            conn.commit()
            report.append("COMMITTED")

        print("\n".join(report))
        return 0
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
