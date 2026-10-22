"""narrative_blocks_2172_v1_20261022.py -- escalation #2172, build step A (design v2, approved
2026-10-22 with option B: "sounds good to proceed with the build"). The narrative's text moves into
the register: each current narrative_section row holds its block verbatim (narrative_section.
block_text: its heading line and every line up to the next heading; the opening row holds the title
line and the opening), so the database renders every chapter file exactly
(narrativeregister.render_chapter). From here a recorded weave keeps the blocks current
(Record -> _sync_bodies), and Check reports any chapter whose file differs from the database.

Also aligns the section rows with the files, through the register's own _sync_sections: a heading
may now repeat under different parents (Ch 10.1 has 'The words' under Fear and under Anxiety; the
second had no row). Current passages are re-placed under the section their text sits in, and their
citations follow.

Schema: ALTER TABLE narrative_section ADD COLUMN block_text TEXT, registered in cfg_column.
Registers itself (inactive, at its own archive path) in the same transaction. cfg_* writes through
configmaint.apply_logged(); narrative writes through narrativeregister.Writer ('migration' grant).
Idempotent. One transaction.

Usage:
    python iba/app/migration/narrative_blocks_2172_v1_20261022.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib import narrativeregister as nr  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2172-NARRATIVE-BLOCKS-20261022"
MODULE = "narrative_blocks_2172_v1_20261022"
COLUMN = {
    "database": "iba", "table_name": "narrative_section", "name": "block_text", "ordinal": 11,
    "type": "TEXT", "is_pk": 0, "notnull": 0, "is_unique": 0, "dflt": None, "fk": None,
    "use": "the section's block of the chapter, verbatim: its heading line and every line up to the next "
           "heading (the opening row: the title line and the opening). The chapters render from these "
           "blocks in ordinal order (narrativeregister.render_chapter); NULL on a row that is no longer "
           "current",
    "expectation": None, "source": "escalation #2172, reading process design v2 (option B)",
    "filled_by": "iba/app/lib/narrativeregister.py (_sync_bodies, from Record and AddChapter); "
                 "iba/app/migration/archive/narrative_blocks_2172_v1_20261022.py",
    "inactive": 0}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    has_col = any(r[1] == "block_text" for r in conn.execute("PRAGMA table_info(narrative_section)"))
    chapters = conn.execute("SELECT * FROM narrative_chapter WHERE inactive=0 AND current_file IS NOT NULL "
                            "ORDER BY reading_order").fetchall()
    print(f"column present: {has_col}; chapters with a file: {len(chapters)}")
    if a.dry_run:
        return 0
    w = nr.Writer(conn, "migration", "migration")
    report = []
    try:
        conn.execute("SAVEPOINT blocks")
        if not has_col:
            conn.execute('ALTER TABLE "narrative_section" ADD COLUMN "block_text" TEXT')
        if not conn.execute("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='narrative_section' "
                            "AND name='block_text'").fetchone():
            apply_logged(conn, RUN_ID, "cfg_column", "insert", {}, COLUMN)
        for ch in chapters:
            path = nr.chapter_dir(cfg) / ch["current_file"]
            text = path.read_text(encoding="utf-8")
            _, sections, passages = nr.parse_chapter(text)
            before = conn.execute("SELECT COUNT(*) FROM narrative_section WHERE chapter_id=? AND "
                                  "last_version IS NULL", (ch["id"],)).fetchone()[0]
            ids = nr._sync_sections(conn, w, ch, sections, ch["current_version"])
            nr._sync_bodies(w, ch, text, ids)
            moved = 0
            for prow in conn.execute("SELECT id, anchor_text, section_id FROM narrative_passage WHERE "
                                     "chapter_id=? AND last_version IS NULL", (ch["id"],)).fetchall():
                hit = nr.find_passage(passages, prow["anchor_text"])
                if len(hit) == 1 and ids.get(hit[0].section) not in (None, prow["section_id"]):
                    w.update("narrative_passage", {"id": prow["id"]}, {"section_id": ids[hit[0].section]})
                    w.update("narrative_citation", {"passage_id": prow["id"]}, {"section_id": ids[hit[0].section]})
                    moved += 1
            after = len(ids)
            if after != before or moved:
                report.append(f"Ch {ch['chapter_no']}: sections {before} -> {after}, passages re-placed {moved}")
        if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
            apply_logged(conn, RUN_ID, "cfg_utility", "insert", {}, {
                "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
                "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
                "through configmaint.apply_logged, same class as the other Developer Mode migrations",
                "purpose": f"ONE-OFF migration -- escalation #2172 step A: narrative_section.block_text, each "
                           f"chapter's blocks from its current file, run_id {RUN_ID}. inactive=1 once applied."})
        bad = [ch["chapter_no"] for ch in chapters
               if nr.render_chapter(conn, ch["id"]) != (nr.chapter_dir(cfg) / ch["current_file"]).read_text(encoding="utf-8")]
        if bad:
            raise nr.Refused(f"chapters that do not render exactly: {bad}")
        conn.execute("RELEASE blocks")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO blocks")
        conn.execute("RELEASE blocks")
        raise
    for line in report:
        print("  " + line)
    print(f"{len(chapters)} chapters render exactly from the database (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
