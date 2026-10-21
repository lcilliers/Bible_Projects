"""retire_cfg_prose_chapter_v1_20260827.py — ONE-OFF. Escalation #918 (researcher, verbatim,
2026-08-27): "cfg_prose_chapter is redundant. it must be removed. The prose_section [table] have
a status column with defined statuses. this should satisfy the prose_section.status destination
which should be updatable with a separate command via the prose method."

Background: `cfg_prose_chapter` (built 2026-08-18, `bootstrap_prose_authority_v1_20260818.py`,
escalation #714) held `status` (reviewed / not_yet_aligned) as a cfg_* row -- workflow DATA about
specific content's review state, not a rule about app behaviour. `bible_research.db`'s
`prose_section.status` (cfg_enum prose_section_status: draft/in_review/approved/archived) already
carries exactly this kind of lifecycle state, at the section grain (finer than the chapter grain
cfg_prose_chapter tracked), and `prose_section_type.chapter_no` already derives "which chapters
exist" without a separate index. Flipping cfg_prose_chapter.status therefore required the full
Config-Maintenance.ps1 -Step Propose / escalation-approval cycle for what is, underneath, an
ordinary content edit -- disproportionate, and confirmed live on escalations #912/#913/#914
(researcher rejected the mechanism, not just those three proposals). The companion fix --
`prose.set_status`, a dedicated Prose.ps1 step that sets/resets `prose_section.status` directly,
patch-gated the same way every other prose write is -- is built separately (see
`handlers/prose.py:set_status`, `lib/prosestore.py:run_set_status`, the new `set_status` operation
in `scripts/apply_session_patch.py`).

What this script does, all in one transaction, direct writes (consistent with how the bootstrap
script created these rows directly rather than through `configmaint.propose` -- schema bootstrap
and retirement are migration-script territory, `configmaint.propose` is for ongoing row-level rule
changes during normal operation, not schema evolution):

  1. DROP TABLE cfg_prose_chapter.
  2. Rebuild cfg_prose_concept WITHOUT its `REFERENCES cfg_prose_chapter(chapter)` clause (the
     clause was never enforced -- SQLite FK pragma is off project-wide -- but leaving it pointing
     at a dropped table is a stale schema declaration; `chapter` remains a plain INTEGER, still
     meaningful against `prose_section_type.chapter_no`). Its 2 existing rows are preserved as-is.
  3. Remove cfg_prose_chapter's own cfg_table / cfg_column / cfg_write_grant / cfg_enum
     (prose_chapter_status) rows -- the metadata that described a table which no longer exists.
  4. Update cfg_prose_concept's own cfg_column row for `chapter` (`use` text) to stop describing a
     live FK to a table that's gone.
  5. Update `governance.prose_canonical_authority` (cfg_setting) to stop citing cfg_prose_chapter
     and instead name the live mechanism (prose_section.status + prose_section_type.chapter_no).

Idempotent: every step checks before acting.

    python -m iba.app.migration.retire_cfg_prose_chapter_v1_20260827
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_NEW_GOVERNANCE_TEXT = (
    "The programme prose (Workflow/Programme/programme_prose/) is the canonical authority on what "
    "the project is about -- researcher, 2026-08-18. Chapters 0-3 are reviewed and final; chapters "
    "4-6 were realigned 2026-08-27 (escalations #739/#786). cfg_prose_concept points a key project "
    "concept (e.g. verse primacy, the inner-being definition) at the prose section that defines it, "
    "rather than restating the definition as a separate rule. Chapter-level review status is NOT "
    "tracked in cfg_* (cfg_prose_chapter was removed 2026-08-27, escalation #918 -- it was workflow "
    "DATA about content state, not a rule, and required the full config-approval cycle for what is "
    "an ordinary content edit) -- it lives where content state belongs: prose_section.status "
    "(cfg_enum prose_section_status), set per section via Prose.ps1 -Step SetStatus, rolled up per "
    "chapter via prose_section_type.chapter_no. A methodology/approach change that touches a "
    "concept named in cfg_prose_concept should flag whether the prose needs updating (part (f) -- "
    "the flagging MECHANISM is not yet built, this states the principle only)."
)


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    report: list[str] = []
    try:
        table_exists = conn.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='cfg_prose_chapter'"
        ).fetchone()

        if table_exists:
            # 1. Rebuild cfg_prose_concept without the stale REFERENCES clause, preserving rows.
            concept_rows = conn.execute("SELECT * FROM cfg_prose_concept").fetchall()
            conn.execute("ALTER TABLE cfg_prose_concept RENAME TO cfg_prose_concept_old_20260827")
            conn.execute("""
                CREATE TABLE cfg_prose_concept (
                    concept_key  TEXT PRIMARY KEY,
                    chapter      INTEGER NOT NULL,
                    section_hint TEXT NOT NULL,
                    description  TEXT NOT NULL,
                    source       TEXT NOT NULL,
                    added_at     TEXT NOT NULL
                )
            """)
            for r in concept_rows:
                conn.execute(
                    "INSERT INTO cfg_prose_concept (concept_key, chapter, section_hint, "
                    "description, source, added_at) VALUES (?,?,?,?,?,?)",
                    (r["concept_key"], r["chapter"], r["section_hint"], r["description"],
                     r["source"], r["added_at"]))
            conn.execute("DROP TABLE cfg_prose_concept_old_20260827")
            report.append(f"cfg_prose_concept rebuilt without FK to cfg_prose_chapter "
                          f"({len(concept_rows)} row(s) preserved)")

            # 2. Drop cfg_prose_chapter itself.
            conn.execute("DROP TABLE cfg_prose_chapter")
            report.append("cfg_prose_chapter table dropped")
        else:
            report.append("cfg_prose_chapter table already absent")

        # 3. Clean up its cfg_table / cfg_column / cfg_write_grant / cfg_enum rows.
        n = conn.execute(
            "DELETE FROM cfg_table WHERE database='iba' AND name='cfg_prose_chapter'").rowcount
        report.append(f"cfg_table rows removed: {n}")
        n = conn.execute(
            "DELETE FROM cfg_column WHERE database='iba' AND table_name='cfg_prose_chapter'"
        ).rowcount
        report.append(f"cfg_column rows removed: {n}")
        n = conn.execute(
            "DELETE FROM cfg_write_grant WHERE database='iba' AND table_name='cfg_prose_chapter'"
        ).rowcount
        report.append(f"cfg_write_grant rows removed: {n}")
        n = conn.execute("DELETE FROM cfg_enum WHERE name='prose_chapter_status'").rowcount
        report.append(f"cfg_enum 'prose_chapter_status' rows removed: {n}")

        # 4. Update cfg_prose_concept.chapter's own column description.
        n = conn.execute(
            "UPDATE cfg_column SET \"use\" = ? "
            "WHERE database='iba' AND table_name='cfg_prose_concept' AND name='chapter'",
            ("which chapter (0-6) this concept belongs to, per prose_section_type.chapter_no in "
             "bible_research.db -- no longer FK'd to a table; cfg_prose_chapter removed 2026-08-27, "
             "escalation #918",)
        ).rowcount
        report.append(f"cfg_column cfg_prose_concept.chapter description updated: {n}")

        # 5. Update the governance setting that used to cite cfg_prose_chapter.
        n = conn.execute(
            "UPDATE cfg_setting SET value = ? WHERE key = 'governance.prose_canonical_authority'",
            (_NEW_GOVERNANCE_TEXT,)
        ).rowcount
        report.append(f"cfg_setting 'governance.prose_canonical_authority' updated: {n}")

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print("retire_cfg_prose_chapter_v1_20260827:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
