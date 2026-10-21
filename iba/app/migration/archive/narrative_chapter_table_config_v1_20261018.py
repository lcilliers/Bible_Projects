"""narrative_chapter_table_config_v1_20261018.py -- escalation #2155: the chapter table becomes the
authority for the book's chapters and what each one is for.

Proposal (approved 2026-10-18):
  _analytics/essay/spirit_soul_body/wa-essay-narrative-chapter-table-proposal-v1-20261018.md
Researcher, chat 2026-10-18 (verbatim): "got it, the chapter table was built with the claims
register migration.  Yes, any the chapter build should be added to the chapter table. The use of
the chapters should be clear from the chapter table and this table should be fully integrated into
the governance and config"; then "Approve #2155 as proposed: D1 kinds as listed, D2 purposes as
drafted, D3 publishing follows the table, D4 the behaviour rule. Proceed to test and build."

Developer Mode: every cfg_* write goes through configmaint.apply_logged (cfg_behaviour_rule 75),
run_id DEVMODE-2155-CHAPTER-20261018.

Config:
  cfg_enum          narrative_chapter_kind (D1)
  cfg_setting       narrative.chapter_kinds_without_file (the kinds AddChapter accepts with no file)
  cfg_column        narrative_chapter.kind / purpose / purpose_ref; created_by expectation
  cfg_table         narrative_chapter use: the authority for the chapters
  cfg_step          narrative_register.add_chapter (new); edit_chapter / check / export text
  cfg_on_fail       add_chapter refused -> report-continue
  cfg_write_grant   add_chapter on chapter, section, update, claim_change; edit_chapter on update
  cfg_behaviour_rule  narrative-chapters-change-only-through-the-register (D4)
  cfg_utility       narrativecopy purpose (D3); this migration
Schema: the three columns added from their cfg_column rows (lib/db.py _col_ddl).
Data (D2): kind, purpose and purpose_ref for every active chapter, as approved in Appendix A; one
Structure log entry for 00 Introduction (added 2026-10-18 by direct insert, #2159, no weave) and one
for the purposes themselves.

Idempotent: every row is checked before it is written. One transaction.

Usage:
    python -m iba.app.migration.narrative_chapter_table_config_v1_20261018 [--db PATH] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

from iba.app.handlers.configmaint import apply_logged
from iba.app.lib.cfg import Cfg, DB_PATH
from iba.app.lib.db import _col_ddl

RUN_ID = "DEVMODE-2155-CHAPTER-20261018"
SRC = "escalation #2155, proposal v1 (wa-essay-narrative-chapter-table-proposal-v1-20261018.md)"
LIB = "iba/app/lib/narrativeregister.py"
THIS = "iba/app/migration/narrative_chapter_table_config_v1_20261018.py"
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"

KINDS = ["front matter", "chapter", "part heading", "opening", "activity", "key characteristic",
         "other beings", "deferred"]
NO_FILE_KINDS = ["part heading", "deferred"]

COLUMNS = [  # name, ordinal, use, expectation
    ("kind", 13, "cfg_enum narrative_chapter_kind: what sort of chapter this is (front matter, "
                 "activity, key characteristic, ...)",
     "set on every active chapter (Check)"),
    ("purpose", 14, "what the chapter holds, what belongs in it and what goes elsewhere, in plain words",
     "set on every active chapter (Check); changed only through EditChapter, logged in the Structure log"),
    ("purpose_ref", 15, "the rulings that set the purpose: escalation numbers and dates",
     "may say 'No recorded ruling' where the purpose is read from the chapter itself"),
]

# D2, Appendix A of the proposal, as approved: chapter_no -> (kind, purpose, purpose_ref)
PURPOSES = {
    "00": ("front matter", "What the study is, where it began and how it is put together, for a reader coming to it new. Points to Ch 1 for the question.", "#2159 (2026-10-18)"),
    "01": ("chapter", "How the question moved from \"two parts or three?\" to \"how does the inner being work?\", and the shape of the book.", "No recorded ruling; reset 2026-09-30 (#1912/#1913)"),
    "02": ("chapter", "Sets the scene: what life is about and what death means, as the setting in which the inner being works. Death is told by its kinds (dead in, dead to, death in the living).", "#1936, #1937 (2026-10-02); OT-02 #2003 (2026-10-14)"),
    "03": ("chapter", "How the words for the inner person relate: one person, spoken of from several sides.", "No recorded ruling"),
    "04": ("chapter", "The word heart: what Scripture shows the heart doing and undergoing.", "No recorded ruling"),
    "05": ("chapter", "The word soul, as for the heart.", "No recorded ruling"),
    "06": ("chapter", "The human spirit, as for the heart. The Holy Spirit's own acts go to 13.1.", "#1986 (2026-10-08) for the 13.1 boundary"),
    "07": ("chapter", "The word flesh as part of the inner person.", "No recorded ruling"),
    "08": ("chapter", "The words conscience and bosom.", "No recorded ruling"),
    "09": ("chapter", "The places where Scripture does draw the words apart.", "No recorded ruling"),
    "10": ("part heading", "Heading for the activity chapters 10.0 to 10.15. No file.", "#1918 (2026-09-30): Ch 10 designed to grow"),
    "10.0": ("opening", "How the activities work together, following the paths from a thought or a feeling to a deed; the map of Part 10.", "No recorded ruling"),
    "10.1": ("activity", "Feeling as an activity, with Delight: a person's delight has its one account here. The \"feeling\" frame itself is an open question (OT-12).", "M18 group B ruling (2026-10-09); OT-12"),
    "10.2": ("activity", "Knowing and hearing, including what blocks hearing (pride, a famine of hearing).", "No recorded ruling"),
    "10.3": ("activity", "Remembering and forgetting.", "#1920 (2026-10-01)"),
    "10.4": ("activity", "Thinking and where thought comes from.", "No recorded ruling"),
    "10.5": ("activity", "Speaking and what speech carries from within.", "No recorded ruling"),
    "10.6": ("activity", "Wanting and desire: the home for the desire words (M18), apart from delight (10.1).", "M18 ruling (2026-10-09): \"10.6 is fine for M18\""),
    "10.7": ("activity", "Choosing, being chosen, planning, willing and taking the lower place: choosing as one account of setting direction.", "#1978 (2026-10-08 reframe); #1986"),
    "10.8": ("activity", "Knowing and doing right and wrong.", "No recorded ruling"),
    "10.9": ("activity", "The person's side of relating to God (God's own acts go to 13.1).", "#1982 (2026-10-07)"),
    "10.10": ("activity", "Relating to others, including holding authority over another and pride over another.", "#1998 (2026-10-12)"),
    "10.11": ("activity", "Concealment and disclosure, before God and before others, as one account.", "#1931 (2026-10-02)"),
    "10.12": ("key characteristic", "The full account of fear as a key characteristic. Other chapters carry fear only where it belongs to their own activity, and point here.", "#1961 (2026-10-04)"),
    "10.13": ("key characteristic", "The full account of anger, including living under God's anger (the old Ch 13, folded in).", "#1963, #1977 (2026-10-05)"),
    "10.14": ("key characteristic", "The full account of humility (\"humility is not a feeling\"). Each of its angles is also woven into its own chapter.", "#2148 (2026-10-15)"),
    "10.15": ("key characteristic", "The full account of pride. Ch 12 keeps pride as a way the inner being goes wrong and points here.", "#2156 (2026-10-15)"),
    "11": ("chapter", "A collection of inner-being elements that have no other home; the title carries no weight in the analysis. Section 4 is the cross-cutting account of how a word or act changes character.", "#1998 (2026-10-12); #1919 (2026-10-01)"),
    "12": ("chapter", "What goes wrong in the inner being. Unchecked original material stays in Held sections.", "No recorded ruling for the purpose; Held rule from the 2026-09-30 reset"),
    "13": ("opening", "The opening of Ch 13: other beings in their own right, routed here (verse routing A).", "#1982 (2026-10-07); rule 72"),
    "13.1": ("other beings", "God in his own right, including the Spirit and Jesus, and how his character reaches the human inner being.", "#1982; #1986 (2026-10-08); #2148 (2026-10-15)"),
    "13.2": ("other beings", "Angels in their own right.", "#1982"),
    "13.3": ("other beings", "Other spirits in their own right, including the devil.", "#1982"),
    "13.4": ("other beings", "The physical world in its own right.", "#1982"),
    "14": ("chapter", "How the inner being is made new. Unchecked original material stays in Held sections.", "No recorded ruling"),
    "15": ("chapter", "The inner life Scripture describes without naming heart, soul or spirit.", "No recorded ruling"),
    "science": ("deferred", "The science chapters, written after the biblical reading.", "Reset 2026-09-30: \"Science chapters come later\""),
}

RULE_KEY = "narrative-chapters-change-only-through-the-register"
RULE_TEXT = (
    "Every chapter of the inner-being narrative is added, moved, renamed, renumbered, split, merged "
    "or retired through Narrative-Register.ps1 (AddChapter, EditChapter), never by a direct insert or "
    "update of narrative_chapter. The chapter table is the authority for which chapters exist, their "
    "reading order and what each is for (kind, purpose, purpose_ref); a new chapter carries its "
    "purpose and the ruling that set it up. The copy to learning4comfort publishes exactly the active "
    "chapters' current files.")
RULE_SOURCE = (
    "Researcher, verbatim, chat 2026-10-18 (#2155): \"Yes, any the chapter build should be added to "
    "the chapter table. The use of the chapters should be clear from the chapter table and this table "
    "should be fully integrated into the governance and config\"; approved D4 the same day.")
RULE_ENFORCED = (
    "Partially enforced: AddChapter/EditChapter refuse an unknown kind or state, a number in use and a "
    "missing file, and log every structural change in the Structure log; Narrative-Register.ps1 Check "
    "reports a chapter with no kind or purpose, a duplicate reading order, a .md file in the narrative "
    "folder that is no chapter's current file, and every row whose created_by is 'direct edit'; "
    "narrativecopy.py copies only the active chapters' current files. A direct SQL insert cannot be "
    "stopped, only reported. GOVERNANCE.md section 95.")


def _put(conn, report: list[str], table: str, key: dict, row: dict, label: str) -> None:
    where = " AND ".join(f'"{k}"=?' for k in key)
    cur = conn.execute(f'SELECT * FROM "{table}" WHERE {where}', list(key.values()))
    found = cur.fetchone()
    if found is None:
        apply_logged(conn, RUN_ID, table, "insert", {}, {**key, **row})
        report.append(f"  {table} {label}: inserted")
        return
    have = dict(zip([d[0] for d in cur.description], found))
    diff = {k: v for k, v in row.items() if have.get(k) != v}
    if diff:
        apply_logged(conn, RUN_ID, table, "update", key, diff)
        report.append(f"  {table} {label}: updated {sorted(diff)}")
    else:
        report.append(f"  {table} {label}: present -- skipped")


def config(cfg: Cfg, report: list[str]) -> None:
    conn = cfg.conn
    report.append("config")
    for i, v in enumerate(KINDS):
        _put(conn, report, "cfg_enum", {"name": "narrative_chapter_kind", "value": v},
             {"ordinal": i, "inactive": 0}, f"narrative_chapter_kind {v!r}")
    _put(conn, report, "cfg_setting", {"key": "narrative.chapter_kinds_without_file"},
         {"value": json.dumps(NO_FILE_KINDS), "module": "narrative", "inactive": 0,
          "use": "Escalation #2155: the narrative_chapter kinds that have no chapter file of their own "
                 "(a part heading, a deferred placeholder). Narrative-Register.ps1 AddChapter accepts "
                 "these with no -CurrentFile; every other kind needs a file on disk."},
         "narrative.chapter_kinds_without_file")
    for name, ordinal, use, expect in COLUMNS:
        _put(conn, report, "cfg_column", {"database": "iba", "table_name": "narrative_chapter", "name": name},
             {"ordinal": ordinal, "type": "TEXT", "is_pk": 0, "notnull": 0, "is_unique": 0, "dflt": None,
              "fk": None, "use": use, "expectation": expect, "source": SRC,
              "filled_by": f"{LIB}; {THIS}", "inactive": 0}, f"narrative_chapter.{name}")
    _put(conn, report, "cfg_column", {"database": "iba", "table_name": "narrative_chapter", "name": "created_by"},
         {"expectation": "never NULL; 'direct edit' means the row was inserted outside the tool, which "
                         "Check reports (#2155)"}, "narrative_chapter.created_by")
    _put(conn, report, "cfg_table", {"database": "iba", "name": "narrative_chapter"},
         {"use": "One row per chapter or sub-chapter of the inner-being narrative, and the authority for "
                 "which chapters exist, their reading order and what each is for (kind, purpose, "
                 "purpose_ref). Changed only through Narrative-Register.ps1 (AddChapter, EditChapter); "
                 "every structural change is logged in the Structure log. A renumbering changes "
                 "chapter_no on the row; every record keeps its link to the chapter, so the history "
                 "follows the chapter, not the number. The copy to learning4comfort publishes the "
                 "active chapters' current files. escalation #2110 spec sec3.1; #2155"},
         "narrative_chapter")
    steps = [
        (13, "narrative_register.add_chapter", "add_chapter",
         "adds a chapter row (-Chapter -Title -Kind -Purpose -PurposeRef -After|-ReadingOrder "
         "-CurrentFile), moves the later chapters down, writes its section rows from the file and a "
         "Structure log entry -- see lib/narrativeregister.py (escalation #2155)"),
        (6, "narrative_register.edit_chapter", "edit_chapter",
         "edits a chapter row (number, title, kind, purpose, ruling, state, current file, place); a "
         "structural change is logged in the Structure log -- see lib/narrativeregister.py "
         "(escalation #2110, #2155)"),
        (11, "narrative_register.check", "check",
         "read-only: chapters, sections and passage anchors against the files on disk; chapters with no "
         "kind or purpose, duplicate reading orders, stray files, direct-edit rows -- see "
         "lib/narrativeregister.py (escalation #2110, #2155)"),
        (12, "narrative_register.export", "export",
         "regenerates the three published files (spec sec8), the register opening with the Chapters "
         "table -- see lib/narrativeregister.py (escalation #2110, #2155)"),
    ]
    for ordinal, step, fn, does in steps:
        _put(conn, report, "cfg_step", {"work_package": "narrative-register", "step": step},
             {"ordinal": ordinal, "handler": f"iba.app.handlers.narrativeregister:{fn}", "scope": "none",
              "does": does, "inactive": 0, "kind": "utility"}, step)
    _put(conn, report, "cfg_on_fail", {"step": "narrative_register.add_chapter", "condition": "refused"},
         {"path": "report-continue", "resolver": None, "message": REFUSED, "route": "terminal",
          "inactive": 0}, "add_chapter refused")
    for writer, table in (("narrative_register.add_chapter", "narrative_chapter"),
                          ("narrative_register.add_chapter", "narrative_section"),
                          ("narrative_register.add_chapter", "narrative_update"),
                          ("narrative_register.add_chapter", "narrative_claim_change"),
                          ("narrative_register.edit_chapter", "narrative_update")):
        _put(conn, report, "cfg_write_grant", {"writer": writer, "table_name": table, "database": "iba"},
             {"inactive": 0}, f"{writer} -> {table}")
    rid = conn.execute("SELECT id FROM cfg_behaviour_rule WHERE rule_key=?", (RULE_KEY,)).fetchone()
    rule = {"class": "sqlite", "rule_key": RULE_KEY, "rule_text": RULE_TEXT, "source": RULE_SOURCE,
            "enforced_by": RULE_ENFORCED, "active": 1, "enforcement_status": "partially_enforced"}
    if rid is None:
        apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "insert", {},
                     {**rule, "added_at": "2026-10-18T00:00:00Z"})
        report.append(f"  cfg_behaviour_rule {RULE_KEY}: inserted")
    else:
        _put(conn, report, "cfg_behaviour_rule", {"id": rid[0]}, rule, RULE_KEY)
    _put(conn, report, "cfg_utility", {"module": "narrativecopy"},
         {"purpose": "narrativecopy.py -- copies the active chapters' current files (narrative_chapter, "
                     "in reading order) from the narrative folder to the learning4comfort inbox; a .md "
                     "file in the folder that is no chapter's current file is reported and not copied "
                     "(#2155 D3). Earlier versions in the inbox are replaced; nothing else there is "
                     "touched; never runs git (#1941)."}, "narrativecopy")
    _put(conn, report, "cfg_utility", {"module": "narrative_chapter_table_config_v1_20261018"},
         {"file_path": THIS,
          "purpose": "ONE-OFF migration -- escalation #2155: the chapter table as the authority for the "
                     "chapters (kind/purpose/purpose_ref columns, enum, setting, add_chapter step, grants, "
                     "behaviour rule, the approved purposes, Structure log entries), every cfg_* write "
                     "through configmaint.apply_logged under run_id DEVMODE-2155-CHAPTER-20261018. "
                     "inactive=1 once applied.",
          "inactive": 1, "config_exempt": 0, "config_exempt_reason": None,
          "crash_escalation_reviewed": 0, "crash_escalation_note": None},
         "narrative_chapter_table_config_v1_20261018")


def schema(cfg: Cfg, report: list[str]) -> None:
    conn = cfg.conn
    report.append("schema")
    have = {r[1] for r in conn.execute("PRAGMA table_info(narrative_chapter)")}
    for name, *_ in COLUMNS:
        if name in have:
            report.append(f"  column narrative_chapter.{name} exists -- skipped")
            continue
        row = conn.execute("SELECT * FROM cfg_column WHERE database='iba' AND table_name='narrative_chapter' "
                           "AND name=?", (name,)).fetchone()
        conn.execute(f"ALTER TABLE narrative_chapter ADD COLUMN {_col_ddl(row)}")
        report.append(f"  column narrative_chapter.{name} created")


def data(cfg: Cfg, report: list[str]) -> None:
    conn = cfg.conn
    report.append("data (D2 purposes; Structure log)")
    active = {r["chapter_no"]: r for r in conn.execute("SELECT * FROM narrative_chapter WHERE inactive=0")}
    missing = sorted(set(active) - set(PURPOSES))
    extra = sorted(set(PURPOSES) - set(active))
    if missing or extra:
        raise SystemExit(f"purposes do not match the active chapters: missing {missing}, unknown {extra}")
    n = 0
    for no, (kind, purpose, ref) in PURPOSES.items():
        r = active[no]
        if (r["kind"], r["purpose"], r["purpose_ref"]) != (kind, purpose, ref):
            conn.execute("UPDATE narrative_chapter SET kind=?, purpose=?, purpose_ref=? WHERE id=?",
                         (kind, purpose, ref, r["id"]))
            n += 1
    report.append(f"  chapters given kind, purpose and ruling: {n}")
    entries = [
        ("00 Introduction added (recorded after the event)",
         "New front chapter 00 Introduction (front matter; reading order 0, before Ch 1; later chapters "
         "+1). Added 2026-10-18 by a direct insert, before AddChapter existed; this entry records it.",
         "#2159: the introduction placed as 00-introduction so it is published with the chapters "
         "(researcher, 2026-10-18)."),
        ("Each chapter's use recorded in the chapter table",
         "Every active chapter given a kind, a purpose and the ruling behind it (37 chapters), as "
         "approved in the proposal's Appendix A.",
         "#2155 (researcher, 2026-10-18): \"The use of the chapters should be clear from the chapter "
         "table\"; D2 approved as drafted."),
    ]
    for title, change, reason in entries:
        if conn.execute("SELECT 1 FROM narrative_update WHERE title=?", (title,)).fetchone():
            report.append(f"  Structure log {title!r}: present -- skipped")
            continue
        conn.execute("INSERT INTO narrative_update (update_date, title, structure_change, structure_reason, "
                     "source_files, scripts, created_by) VALUES ('2026-10-18', ?, ?, ?, ?, ?, 'migration')",
                     (title, change, reason,
                      "_analytics/essay/spirit_soul_body/wa-essay-narrative-chapter-table-proposal-v1-20261018.md",
                      THIS))
        report.append(f"  Structure log {title!r}: inserted")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DB_PATH))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    cfg = Cfg(pathlib.Path(args.db))
    conn = cfg.conn
    conn.isolation_level = None
    report: list[str] = [f"db: {args.db}", f"run_id: {RUN_ID}"]
    try:
        conn.execute("BEGIN")
        config(cfg, report)
        schema(cfg, report)
        data(cfg, report)
        written = conn.execute("SELECT COUNT(*) FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone()[0]
        if args.dry_run:
            conn.execute("ROLLBACK")
            report.append(f"DRY RUN -- rolled back ({written} cfg_* change row(s) in total under {RUN_ID})")
        else:
            conn.execute("COMMIT")
            report.append(f"committed under {RUN_ID}: {written} cfg_* change row(s) in total")
    except BaseException:
        conn.execute("ROLLBACK")
        raise
    finally:
        cfg.close()
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
