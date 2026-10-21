"""Register `purge.retire_database` -- physically clears every row from every table a database has
marked `cfg_table.inactive=1` (researcher ruling, this chat, 2026-09-24: "findings is the
terminology in the old system that is replaced by observations... all the finding related tables
in research DB should be inactive and... all the records in those table are no longer relevant and
can be purged"). Scope is DYNAMIC -- read from `cfg_table` live at run time, never a hardcoded
table list -- so it always tracks whatever the config says is inactive, not a snapshot.

Before clearing, also nulls 3 known FK columns on RETAINED active tables that point into the
about-to-be-cleared set (`_DANGLING_FK_CLEANUP` in `handlers/purge.py`) so no active, kept row is
left holding a silently dangling reference: `prose_section.registry_id`,
`wa_prose_section_citations.cited_finding_id/cited_qa_link_id/cited_sd_pointer_id`.

Same work package as `purge.audit`/`purge.execute` (`purge-audit`), third step, ordinal 2.

Safe to re-run: every insert is guarded, no-ops if already present.

Usage:
    python iba/app/migration/register_purge_retire_database_step_v1_20260924.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"


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
                          ("purge.retire_database_report_path",)):
            cur.execute(
                "INSERT INTO cfg_setting (key, value, use, module, inactive) VALUES (?,?,?,?,0)",
                ("purge.retire_database_report_path", '"research/discovery/purge-retire-database.md"',
                 "where purge.retire_database persists its findings -- escalation #1868/#1872/#1873",
                 "validation"))
            report.append("cfg_setting purge.retire_database_report_path inserted")
        else:
            report.append("cfg_setting purge.retire_database_report_path already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_report WHERE step=?", ("purge.retire_database",)):
            cur.execute(
                "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
                "naming_scheme, archive_dir, inactive) VALUES (?,?,?,?,?,?,?,0)",
                ("purge.retire_database", "Database retirement — inactive tables cleared "
                 "(#1868/#1872/#1873)", 1, None, "md", "stable", "archive"))
            report.append("cfg_report purge.retire_database inserted")
        else:
            report.append("cfg_report purge.retire_database already present — skipped")

        for ordinal, key, heading in (
            (0, "summary", "## Summary"),
            (1, "fk-cleanup", "## Dangling FK cleanup on retained tables"),
            (2, "purged", "## Cleared"),
        ):
            if not row_exists(cur, "SELECT 1 FROM cfg_report_section WHERE step=? AND "
                                    "section_key=?", ("purge.retire_database", key)):
                cur.execute(
                    "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, "
                    "toc_label, include, inactive) VALUES (?,?,?,?,?,1,0)",
                    ("purge.retire_database", ordinal, key, heading, heading.lstrip("# ")))
                report.append(f"cfg_report_section purge.retire_database/{key} inserted")
            else:
                report.append(f"cfg_report_section purge.retire_database/{key} already present "
                              f"— skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_step WHERE step=?", ("purge.retire_database",)):
            cur.execute(
                "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                "inactive, kind) VALUES (?,?,?,?,?,?,0,?)",
                ("purge-audit", 2, "purge.retire_database", "iba.app.handlers.purge:retire_database",
                 "none",
                 "Physically clears every row from every table cfg_table marks inactive=1 for the "
                 "given -Database (default bible_research) -- scope read live from cfg_table every "
                 "run, never a hardcoded list. Before clearing, nulls known FK columns on RETAINED "
                 "active tables that point into the cleared set, so no kept row is left dangling. "
                 "-Preview (default true) counts only, nothing written. -Live actually deletes, one "
                 "transaction, verifying each table reads back 0 rows afterward.",
                 "operations"))
            report.append("cfg_step purge.retire_database inserted")
        else:
            report.append("cfg_step purge.retire_database already present — skipped")

        cur.execute(
            "UPDATE cfg_utility SET purpose=? WHERE file_path=?",
            ("purge.py -- app-wide soft-delete purge audit + execute + database retirement "
             "(escalation #1766/#1868/#1872/#1873): per-table soft-deleted counts + live-dependency "
             "safety check (audit, read-only); allow-listed soft-deleted-row removal (execute, "
             "preview-then-live); and full-table clearing of every cfg_table.inactive=1 table for a "
             "database, with dangling-FK cleanup on retained tables (retire_database, "
             "preview-then-live). All three always persist a report.",
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
