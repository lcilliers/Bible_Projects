"""restructure_configmaint_report_sections.py — ONE-OFF: split CONFIG-REPORT.md's §0 "Findings —
needing researcher judgement" so it holds ONLY items that actually need a decision.

Researcher's own read, 2026-07-30: "the section 0 Finding for researcher action should only
include items that need my decision. The list of soft deleted items does not belong there." Before
this, `lib/cfgreport.py`'s "findings" section bundled the genuine judgement-call findings together
with "Inactive configs" — a historical, already-decided record explicitly excluded from validation
(its own heading says so) — so a reader had to mentally filter which of §0's bullets were real
asks and which were just an audit trail.

Two new sections carved out of §0, everything after renumbered to stay sequential:
  0. Findings — needing researcher judgement          (unchanged content, informational block removed)
  1. Inactive configs — historical record, not a decision   (NEW — the block that moved out of §0)
  2. Utilities registry                                     (NEW — full cfg_utility listing, the
                                                              researcher's own ask: "the contents
                                                              page ... does not include the
                                                              utility table")
  3. Connection (STEP)                    [was 1]
  4. Settings ...                         [was 2]
  5. STEP apis                            [was 3]
  6. Work packages & steps ...            [was 4]
  7. on_fail ...                          [was 5]
  8. Write grants ...                     [was 6]
  9. Status flow                          [was 7]
  10. Schema ...                          [was 8]
  11. Enums                               [was 9]
  12. Book order                          [was 10]
  13. Change-log ...                      [was 11]
  14. Reports — full governance per report [was 12]

`cfg_report_section` is a normal cfg_* DATA row (no DDL) — still done as a direct migration, not
`configmaint.propose`, per the researcher's standing instruction not to approve mechanical
infrastructure registration row-by-row (same class as every other `bootstrap_*`/`restructure_*`
script). The actual `lib/cfgreport.py` code change (which content lands in which section) is a
separate, ordinary code edit — this script only fixes the CONFIG (ordinals/headings/labels).

    python -m iba.app.migration.restructure_configmaint_report_sections
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_STEP = "configmaint.report"

# (section_key, new_ordinal, new_heading, new_toc_label)
_RENUMBER = (
    ("connection", 3, "## 3. Connection (STEP)", "3. Connection (STEP)"),
    ("settings", 4, "## 4. Settings — every rule / threshold, grouped by owning module",
     "4. Settings — every rule / threshold, grouped by owning module"),
    ("apis", 5, "## 5. STEP apis", "5. STEP apis"),
    ("work_packages", 6, "## 6. Work packages & steps (the sequence)",
     "6. Work packages & steps (the sequence)"),
    ("on_fail", 7, "## 7. on_fail — condition -> path (the fork rules)",
     "7. on_fail — condition -> path (the fork rules)"),
    ("write_grants", 8, "## 8. Write grants — who may write what",
     "8. Write grants — who may write what"),
    ("status_flow", 9, "## 9. Status flow", "9. Status flow"),
    ("schema", 10, "## 10. Schema — data tables built from config",
     "10. Schema — data tables built from config"),
    ("enums", 11, "## 11. Enums", "11. Enums"),
    ("book_order", 12, "## 12. Book order", "12. Book order"),
    ("change_log", 13, "## 13. Change-log — every accepted load (audit)",
     "13. Change-log — every accepted load (audit)"),
    ("report_governance", 14, "## 14. Reports — full governance per report",
     "Reports — full governance per report"),
)

# (section_key, ordinal, heading, toc_label) — the two NEW sections
_NEW_SECTIONS = (
    ("inactive_configs", 1, "## 1. Inactive configs — historical record, not a decision",
     "1. Inactive configs — historical record, not a decision"),
    ("utilities", 2, "## 2. Utilities registry", "2. Utilities registry"),
)


def _renumber(conn: sqlite3.Connection, report: list[str]) -> None:
    for key, ordinal, heading, toc_label in _RENUMBER:
        row = conn.execute(
            "SELECT ordinal, heading FROM cfg_report_section WHERE step=? AND section_key=?",
            (_STEP, key)).fetchone()
        if not row:
            report.append(f"SKIPPED {key!r} — no cfg_report_section row for {_STEP!r} (list is "
                          f"stale, fix the migration, not the DB)")
            continue
        if row[0] == ordinal and row[1] == heading:
            report.append(f"{key!r} already at ordinal {ordinal} with the target heading — "
                          f"left alone")
            continue
        conn.execute(
            "UPDATE cfg_report_section SET ordinal=?, heading=?, toc_label=? "
            "WHERE step=? AND section_key=?",
            (ordinal, heading, toc_label, _STEP, key))
        report.append(f"{key!r}: ordinal {row[0]}->{ordinal}, heading updated")


def _add_new_sections(conn: sqlite3.Connection, report: list[str]) -> None:
    for key, ordinal, heading, toc_label in _NEW_SECTIONS:
        if conn.execute(
                "SELECT 1 FROM cfg_report_section WHERE step=? AND section_key=?",
                (_STEP, key)).fetchone():
            report.append(f"cfg_report_section ({_STEP}, {key!r}) already present — left alone")
            continue
        conn.execute(
            "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, toc_label, "
            "include) VALUES (?,?,?,?,?,1)",
            (_STEP, ordinal, key, heading, toc_label))
        report.append(f"cfg_report_section ({_STEP}, {key!r}) added at ordinal {ordinal}")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    _add_new_sections(conn, report)
    _renumber(conn, report)

    conn.commit()
    conn.close()

    print("configmaint.report section restructure:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
