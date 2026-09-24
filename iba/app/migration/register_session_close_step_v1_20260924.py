"""Register `session.close` -- session-close checks: escalation update coverage, governance/
config/doc drift signal, and BUILD.md tracking-id coverage for the current Claude Code session
(escalation #1875, researcher design approval 2026-09-24, "verbatim/design debates/design
decisions/skipped-postponed-ignored" scope confirmed same chat).

Detection only -- the handler (`iba/app/handlers/session_close.py:check`) mechanically detects
gaps and always persists a report; it never writes a remediation itself. Its `gaps-found`
condition routes to `report-continue` (non-blocking, exit 0) -- per the researcher's explicit
instruction that remediation must not create an additional approval cycle. Remediation is a
separate slash command, `.claude/commands/session-close.md`.

New, standalone work package (not chained), like `spine-check`/`purge-audit`.

Safe to re-run: every insert is guarded, no-ops if already present.

Usage:
    python iba/app/migration/register_session_close_step_v1_20260924.py [--db PATH] [--dry-run]
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

        if not row_exists(cur, "SELECT 1 FROM cfg_utility WHERE module=?", ("session_close",)):
            cur.execute(
                "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt, "
                "config_exempt_reason, crash_escalation_reviewed, crash_escalation_note) "
                "VALUES (?,?,?,0,0,NULL,0,NULL)",
                ("session_close", "iba/app/handlers/session_close.py",
                 "session_close.py -- session-close checks: escalation-update coverage, "
                 "governance/config/doc drift signal, and BUILD.md tracking-id coverage for the "
                 "current Claude Code session (escalation #1875). Detection only -- always "
                 "persists a report; remediation is performed separately by Claude via "
                 ".claude/commands/session-close.md."))
            report.append("cfg_utility session_close inserted")
        else:
            report.append("cfg_utility session_close already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_work_package WHERE name=?", ("session-close",)):
            cur.execute(
                "INSERT INTO cfg_work_package (name, ps_script, runs_over, chained, "
                "complete_message, next_step_hint, paused_message, inactive) "
                "VALUES (?,?,?,0,NULL,NULL,NULL,0)",
                ("session-close", "iba/app/ps/Session-Close.ps1", "none"))
            report.append("cfg_work_package session-close inserted")
        else:
            report.append("cfg_work_package session-close already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_step WHERE step=?", ("session.close",)):
            cur.execute(
                "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                "inactive, kind) VALUES (?,?,?,?,?,?,0,?)",
                ("session-close", 0, "session.close",
                 "iba.app.handlers.session_close:check", "none",
                 "Read-only session-close detection (escalation #1875): (a) every escalation id "
                 "the session's own transcript shows touched via Escalation.ps1 has a matching "
                 "escalation_history row at that version; (b) reports which of GOVERNANCE.md/"
                 "CLAUDE.md/USER-GUIDE.md changed in the session's git diff window (drift "
                 "judgement itself is Claude's, not mechanically checked); (c) any iba/app/** "
                 "file changed this session with no matching BUILD.md change. Always persists a "
                 "report. Never blocks -- gaps-found routes to report-continue.",
                 "operations"))
            report.append("cfg_step session.close inserted")
        else:
            report.append("cfg_step session.close already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_setting WHERE key=?",
                          ("session_close.report_path",)):
            cur.execute(
                "INSERT INTO cfg_setting (key, value, use, module, inactive) VALUES (?,?,?,?,0)",
                ("session_close.report_path", '"iba/app/reports/session-close.md"',
                 "where session.close persists its findings -- escalation #1875", "validation"))
            report.append("cfg_setting session_close.report_path inserted")
        else:
            report.append("cfg_setting session_close.report_path already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_report WHERE step=?", ("session.close",)):
            cur.execute(
                "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
                "naming_scheme, archive_dir, inactive) VALUES (?,?,?,?,?,?,?,0)",
                ("session.close", "Session close — escalation update / governance drift / "
                 "BUILD.md coverage check (#1875)", 1, None, "md", "stable", "archive"))
            report.append("cfg_report session.close inserted")
        else:
            report.append("cfg_report session.close already present — skipped")

        for ordinal, key, heading in (
            (0, "summary", "## Summary"),
            (1, "escalation_gaps", "## Escalation update coverage"),
            (2, "governance_gaps", "## Governance / config / doc drift"),
            (3, "build_gaps", "## BUILD.md coverage"),
        ):
            if not row_exists(cur, "SELECT 1 FROM cfg_report_section WHERE step=? AND "
                                    "section_key=?", ("session.close", key)):
                cur.execute(
                    "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, "
                    "toc_label, include, inactive) VALUES (?,?,?,?,?,1,0)",
                    ("session.close", ordinal, key, heading, heading.lstrip("# ")))
                report.append(f"cfg_report_section session.close/{key} inserted")
            else:
                report.append(f"cfg_report_section session.close/{key} already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?",
                          ("session.close", "gaps-found")):
            cur.execute(
                "INSERT INTO cfg_on_fail (step, condition, path, resolver, message, route, "
                "inactive) VALUES (?,?,?,?,?,?,0)",
                ("session.close", "gaps-found", "report-continue", None,
                 "session-close detected one or more gaps — see report for detail; remediation "
                 "is Claude's own follow-up via .claude/commands/session-close.md, not a "
                 "blocking approval cycle", "terminal"))
            report.append("cfg_on_fail session.close/gaps-found inserted")
        else:
            report.append("cfg_on_fail session.close/gaps-found already present — skipped")

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
