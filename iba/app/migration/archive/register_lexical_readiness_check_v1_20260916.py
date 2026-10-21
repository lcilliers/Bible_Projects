"""Register `lexical.readiness` -- the 3-leg base-data readiness check (escalation #1606, Phase A
item 1 of the full lexical-stack rebuild, escalation #1706/#1711, built 2026-09-16).

Researcher's own framing, #1606: "lexical readiness is a precursor for the lexical reading stage,
which is a precursor for the sub group." Read-only check, mirrors `spine.check`'s own registration
shape (cfg_setting report path, cfg_report + cfg_report_section, cfg_step, cfg_method_rule) --
deliberately a SEPARATE check from spine.check, not merged into it: spine covers the whole-project
verse/span/strong spine; this is lexical-build-specific, and its Leg 3 (cluster_strong allocation)
is a precondition Layer 1's redesigned `role` column depends on directly, which spine.check has no
reason to know about.

Safe to re-run: every insert is guarded, no-ops if already present.

Usage:
    python iba/app/migration/register_lexical_readiness_check_v1_20260916.py [--db PATH] [--dry-run]
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
                          ("lexical.readiness_report_path",)):
            cur.execute(
                "INSERT INTO cfg_setting (key, value, use, module, inactive) VALUES (?,?,?,?,0)",
                ("lexical.readiness_report_path", '"research/discovery/lexical-readiness.md"',
                 "where lexical.readiness persists its findings -- #1606/#1706 Phase A",
                 "validation"))
            report.append("cfg_setting lexical.readiness_report_path inserted")
        else:
            report.append("cfg_setting lexical.readiness_report_path already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_report WHERE step=?", ("lexical.readiness",)):
            cur.execute(
                "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
                "naming_scheme, archive_dir, inactive) VALUES (?,?,?,?,?,?,?,0)",
                ("lexical.readiness", "Lexical readiness check (3-leg, #1606)", 1, None, "md",
                 "stable", "archive"))
            report.append("cfg_report lexical.readiness inserted")
        else:
            report.append("cfg_report lexical.readiness already present — skipped")

        for ordinal, key, heading in (
            (0, "summary", "## Summary"),
            (1, "detail", "## Detail"),
        ):
            if not row_exists(cur, "SELECT 1 FROM cfg_report_section WHERE step=? AND "
                                    "section_key=?", ("lexical.readiness", key)):
                cur.execute(
                    "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, "
                    "toc_label, include, inactive) VALUES (?,?,?,?,?,1,0)",
                    ("lexical.readiness", ordinal, key, heading, heading.lstrip("# ")))
                report.append(f"cfg_report_section lexical.readiness/{key} inserted")
            else:
                report.append(f"cfg_report_section lexical.readiness/{key} already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_step WHERE step=?", ("lexical.readiness",)):
            cur.execute(
                "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                "inactive, kind) VALUES (?,?,?,?,?,?,0,?)",
                ("verse-lexical", 0, "lexical.readiness",
                 "iba.app.handlers.lexical:readiness", "none",
                 "3-leg read-only precondition check for the Layer 1 rebuild (#1606): Leg1 every "
                 "live verse has >=1 live span; Leg2 every live span's strong_variant code "
                 "resolves to a live strong row (duplicates spine.check's own desync check "
                 "deliberately -- #1606's own framing is one cohesive 3-leg check); Leg3 every "
                 "live strong that actually occurs in a live span has >=1 live cluster_strong "
                 "allocation (the precondition Layer 1's redesigned role column, a JSON array of "
                 "cluster_strong.cluster_code, depends on directly). Persists a report every run "
                 "(governance.reports_must_persist), fails on any FATAL finding.",
                 "operations"))
            report.append("cfg_step lexical.readiness inserted")
        else:
            report.append("cfg_step lexical.readiness already present — skipped")

        if not row_exists(cur, "SELECT 1 FROM cfg_method_rule WHERE rule_key=?",
                          ("lexical-readiness-3leg-fatal",)):
            cur.execute(
                "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, "
                "enforced_by, ordinal, active) VALUES (?,?,?,?,?,?,1)",
                ("lexical.readiness", "lexical-readiness-3leg-fatal",
                 "Before any Layer 1 (verse_lexical) rebuild scope runs, the base data must pass "
                 "a 3-leg readiness check: every verse in scope has >=1 live span (Leg1); every "
                 "span's strong code resolves to a live strong row (Leg2); every occurring strong "
                 "has >=1 live cluster_strong allocation (Leg3). A FATAL finding on any leg blocks "
                 "the run -- fixed on discovery, not deferred. Researcher ruling, escalation "
                 "#1606, 2026-09-15: 'lexical readiness is a precursor for the lexical reading "
                 "stage, which is a precursor for the sub group.'",
                 "escalation #1606; #1706 Phase A item 1; #1711 build",
                 "lexical.readiness (handlers/lexical.py:readiness) -- registered and live "
                 "2026-09-16, run before every Layer 1 build/rebuild", 0))
            report.append("cfg_method_rule lexical-readiness-3leg-fatal inserted")
        else:
            report.append("cfg_method_rule lexical-readiness-3leg-fatal already present — skipped")

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
