"""Register `purge.audit` -- the app-wide soft-delete purge audit (escalation #1766, researcher
approved build 2026-09-19: "Approve to build. Do not run a purge as yet.").

Read-only report tool: per table with a registered soft-delete column (`cfg_column.name` IN
`deleted`/`delete_flagged`, across BOTH `iba` and `bible_research`), counts soft-deleted rows and,
for any table over `purge.unsafe_check_min_soft_deleted`, checks whether a live (non-deleted) row
elsewhere still references one of its soft-deleted PKs (via `cfg_column.fk`) -- flags that table
UNSAFE if so. Mirrors `spine.check`/`lexical.readiness`'s own registration shape (cfg_setting report
path, cfg_report + cfg_report_section, cfg_step, cfg_utility).

Deliberately does NOT register anything for actual row removal -- that's a separate, not-yet-
designed capability (dependency-aware purge order / retention window still open, escalation #1766
v3/v5). This migration is the audit half only.

Safe to re-run: every insert is guarded, no-ops if already present.

Usage:
    python iba/app/migration/register_purge_audit_step_v1_20260919.py [--db PATH] [--dry-run]
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
                          ("purge.audit_report_path",)):
            cur.execute(
                "INSERT INTO cfg_setting (key, value, use, module, inactive) VALUES (?,?,?,?,0)",
                ("purge.audit_report_path", '"research/discovery/purge-audit.md"',
                 "where purge.audit persists its findings -- escalation #1766", "validation"))
            report.append("cfg_setting purge.audit_report_path inserted")
        else:
            report.append("cfg_setting purge.audit_report_path already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_setting WHERE key=?",
                          ("purge.unsafe_check_min_soft_deleted",)):
            cur.execute(
                "INSERT INTO cfg_setting (key, value, use, module, inactive) VALUES (?,?,?,?,0)",
                ("purge.unsafe_check_min_soft_deleted", "10",
                 "a table with more than this many soft-deleted rows gets a live-dependency check "
                 "before being listed as safe to purge -- escalation #1766 v2, researcher's own "
                 "threshold ('for each table with > 10 softdelete records check the dependencies'). "
                 "Was a hardcoded constant in the escalation's own ad-hoc audit; made config-driven "
                 "here per the same pattern already fixed twice this session (#1753 B3, #1761).",
                 "validation"))
            report.append("cfg_setting purge.unsafe_check_min_soft_deleted inserted")
        else:
            report.append("cfg_setting purge.unsafe_check_min_soft_deleted already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_report WHERE step=?", ("purge.audit",)):
            cur.execute(
                "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
                "naming_scheme, archive_dir, inactive) VALUES (?,?,?,?,?,?,?,0)",
                ("purge.audit", "Soft-delete purge audit (app-wide, #1766)", 1, None, "md",
                 "stable", "archive"))
            report.append("cfg_report purge.audit inserted")
        else:
            report.append("cfg_report purge.audit already present — skipped")

        for ordinal, key, heading in (
            (0, "summary", "## Summary"),
            (1, "safe", "## Safe to purge"),
            (2, "unsafe", "## Unsafe -- live dependency risk"),
        ):
            if not row_exists(cur, "SELECT 1 FROM cfg_report_section WHERE step=? AND "
                                    "section_key=?", ("purge.audit", key)):
                cur.execute(
                    "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, "
                    "toc_label, include, inactive) VALUES (?,?,?,?,?,1,0)",
                    ("purge.audit", ordinal, key, heading, heading.lstrip("# ")))
                report.append(f"cfg_report_section purge.audit/{key} inserted")
            else:
                report.append(f"cfg_report_section purge.audit/{key} already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_work_package WHERE name=?", ("purge-audit",)):
            cur.execute(
                "INSERT INTO cfg_work_package (name, ps_script, runs_over, chained, "
                "complete_message, next_step_hint, paused_message, inactive) "
                "VALUES (?,?,?,?,?,?,?,0)",
                ("purge-audit", "iba/app/ps/Purge-SoftDeletes.ps1", "none", 0, None, None, None))
            report.append("cfg_work_package purge-audit inserted")
        else:
            report.append("cfg_work_package purge-audit already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_step WHERE step=?", ("purge.audit",)):
            cur.execute(
                "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                "inactive, kind) VALUES (?,?,?,?,?,?,0,?)",
                ("purge-audit", 0, "purge.audit", "iba.app.handlers.purge:audit", "none",
                 "Read-only, app-wide: for every table with a registered soft-delete column "
                 "(cfg_column.name IN deleted/delete_flagged, both databases), counts soft-deleted "
                 "rows; for any table over purge.unsafe_check_min_soft_deleted, checks cfg_column.fk "
                 "for a live row elsewhere still referencing one of its soft-deleted PKs and flags "
                 "the table UNSAFE if so. Persists a report every run "
                 "(governance.reports_must_persist). Does not remove any row -- audit only.",
                 "operations"))
            report.append("cfg_step purge.audit inserted")
        else:
            report.append("cfg_step purge.audit already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_utility WHERE file_path=?",
                          ("iba/app/handlers/purge.py",)):
            cur.execute(
                "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt, "
                "config_exempt_reason, crash_escalation_reviewed, crash_escalation_note) "
                "VALUES (?,?,?,0,0,NULL,0,NULL)",
                ("purge", "iba/app/handlers/purge.py",
                 "purge.py -- app-wide soft-delete purge audit (escalation #1766): per-table "
                 "soft-deleted counts + live-dependency safety check across both databases. "
                 "Read-only, always persists a report."))
            report.append("cfg_utility purge inserted")
        else:
            report.append("cfg_utility purge already present — skipped")

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
