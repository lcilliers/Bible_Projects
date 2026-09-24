"""Mark every non-prose table in bible_research.db `inactive=1` in `cfg_table` (researcher ruling,
this chat, 2026-09-24, verbatim): "findings is the terminology in the old system that is replaced
by observations... all the finding related tables in research DB should be inactive and... all the
records in those table are no longer relevant and can be purged." Supersedes the prior
`governance.scope_research_db` framing ("home for prose and findings") -- bible_research.db is now
prose-only; every finding/analysis/legacy-cluster table there is superseded by `iba.db`'s
`ib_observation`/`ib_node` pipeline (evidenced live: escalation #737, "supersede -- option A...
The new ib_observation/ib_node pipeline already does what Window 2's research_db migration was
reaching for.").

Cross-checked live: all 113 bible_research.db tables ARE already registered in `cfg_table` (0
documentation gap there) -- the gap was the missing GOVERNANCE.md/cfg_setting record of this
scope decision, not missing table registration. 34 tables were still `inactive=0`; this migration
flips 33 of them (see TABLES below). Three tables deliberately excluded, not silently swept:
  - `schema_version` -- DB-infrastructure bookkeeping (migration history), not analytical content;
    "inactive"/"purgeable" doesn't apply to it the same way.
  - `record_change_log` -- prose's OWN change-log mechanism (`cfg_behaviour_rule`
    'record-change-log-choke-point': covers prose_section/prose_section_type), not a finding table.
  - `ib_characteristic` -- flagged to the researcher (escalation #1873 follow-on) rather than
    assumed; naming suggests a newer/parallel mechanism, status not independently confirmed here.
`wa_session_research_flags` IS included below despite escalation #833's prior explicit "stays as
is... incorporated in IBA" ruling -- that deferral was conditioned on "the analytics-phase restart"
(#833's own words), which today's ruling resolves (analytics restarted in IBA, not bible_research.db)
-- flagged to the researcher as a judgement call, not silently overridden.

Also updates `cfg_setting` `governance.scope_research_db` to reflect the corrected scope.

Safe to re-run: every update is guarded by a live inactive=0 check, no-ops if already applied.

Usage:
    python iba/app/migration/mark_bible_research_findings_inactive_v1_20260924.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

TABLES = [
    "book_code_variants", "books", "characteristic_subgroup", "cluster", "cluster_observation",
    "cluster_subgroup", "engine_run_log", "engine_stream_checkpoint", "finding", "finding_citation",
    "finding_question_link", "finding_revision", "finding_verse_index", "finding_verse_link",
    "passage", "prose_section_finding_link", "reread_worklist", "segment_unit",
    "segment_unit_verse", "session_d_observations", "session_d_runs", "session_d_term_links",
    "session_d_verse_links", "sources", "vcg_term", "verse_analysis_progress",
    "wa_data_quality_flags", "wa_finding_entity_links", "wa_label_pattern",
    "wa_quality_flag_types", "wa_session_research_flags", "wa_vocab_member", "wa_vocab_set",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")

        for table in TABLES:
            row = cur.execute(
                "SELECT inactive FROM cfg_table WHERE database='bible_research' AND name=?",
                (table,)).fetchone()
            if row is None:
                report.append(f"cfg_table {table}: NOT REGISTERED -- skipped, needs investigation")
                continue
            if row["inactive"] == 1:
                report.append(f"cfg_table {table}: already inactive=1 -- skipped")
                continue
            cur.execute("UPDATE cfg_table SET inactive=1 WHERE database='bible_research' AND name=?",
                       (table,))
            report.append(f"cfg_table {table}: inactive 0 -> 1")

        new_scope_text = (
            '"bible_research.db (research_db) is now prose-only -- the canonical, foundational '
            'authority on the programme\'s own governing concepts (governance.prose_canonical_authority). '
            'Findings/observations are fully owned by iba.db\'s ib_observation/ib_node pipeline; the '
            'old finding/analysis/legacy-cluster tables in bible_research.db are superseded, not a '
            'live parallel store. Superseded 2026-09-24 (researcher ruling, this chat, verbatim: '
            '\\"findings is the terminology in the old system that is replaced by observations... '
            'all the finding related tables in research DB should be inactive and... all the records '
            'in those table are no longer relevant and can be purged\\"), evidenced live by escalation '
            '#737 (2026-09-13/18 supersede decision). Prior text (superseded): the home for prose and '
            'findings with all the related enabling tables."'
        )
        cur.execute("SELECT value FROM cfg_setting WHERE key='governance.scope_research_db'")
        current = cur.fetchone()
        if current and current["value"] != new_scope_text:
            cur.execute("UPDATE cfg_setting SET value=? WHERE key='governance.scope_research_db'",
                       (new_scope_text,))
            report.append("cfg_setting governance.scope_research_db: updated")
        else:
            report.append("cfg_setting governance.scope_research_db: already current -- skipped")

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
