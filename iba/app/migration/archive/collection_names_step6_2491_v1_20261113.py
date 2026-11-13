"""collection_names_step6_2491_v1_20261113.py -- escalation #2491, plan v3 step 6 (names).

Researcher, 2026-11-13: 'Yes, step 6'. Each of the 226 collections' names was read against its members (word members by tier, listed with their forms):
the name stays where it is a suitable base for the members, and is reconsidered where it is not (researcher, #2491 v12: the name is formed from all the members
as a concept covering them; the base is the name where suitable). 216 names stay. Ten are changed (RENAME), for two reasons: seven are an inflected form
where every other name is a base word (consumed, covered, quaked, realized, rescued, mastered, torn), and three do not stand for their members
(deeply holds the sighing and groaning words; distinction holds doubt and doubting; tenderhearted holds compassion, pity and kindness and also the
discerning words). Rulings are inferential (B:4). No chapter number or title is designed here (researcher, #2491 v12). A name is only the collection's
label: nothing stores it by value (the node column, the listing log and collection_state key the collection by id), and the core term, the members, the
status and the id are not changed. The old name is kept in surface_event (value_before). The run stops and rolls back unless every new name is free (no
live, merged or retired collection has it) and every collection still has a different name. Idempotent.
    python -m iba.app.migration.collection_names_step6_2491_v1_20261113 [--db PATH] [--dry-run]   (from the project root)
"""
import argparse
import pathlib
import sqlite3
import sys

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2491-NAMES-STEP6-20261113"
WHO = "devmode-2491"
SRC = "researcher 2026-11-13 (#2491): step 6"
RENAME = {   # old name: (new name, reason)
    "consumed": ("consume", "an inflected form among base words: consumed, consumes, devour, finished"),
    "covered": ("conceal", "an inflected form among base words: the members hide, conceal and veil"),
    "quaked": ("tremble", "an inflected form among base words: quake, shake, shudder and tremble"),
    "realized": ("realize", "an inflected form among base words: realize, comprehend, conclude and grasp"),
    "rescued": ("rescue", "an inflected form among base words: rescue, deliver, free and save"),
    "mastered": ("master", "an inflected form among base words"),
    "torn": ("tear", "an inflected form among base words"),
    "deeply": ("sigh", "the members are the sighing and groaning words (groaned, sighed, sighing), not depth"),
    "distinction": ("doubt", "the members are doubt, doubting and doubts as well as distinction"),
    "tenderhearted": ("compassion", "most members are compassion, pity, gentleness and kindness (the discerning words are a second matter for the member review)"),
}


class Stop(Exception):
    pass


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    conn.row_factory = sqlite3.Row
    q = lambda s, *p: conn.execute(s, p).fetchall()
    one = lambda s, *p: conn.execute(s, p).fetchone()[0]
    todo = []
    for old, (new, why) in RENAME.items():
        r = q("SELECT id FROM collection WHERE deleted=0 AND name=? AND status IN ('indicative','confirmed')", old)
        if not r:
            continue
        if q("SELECT 1 FROM collection WHERE name=?", new):
            raise Stop("the name %r is already used by a collection" % new)
        todo.append((r[0]["id"], old, new, why))
    print("predicted: %d renames" % len(todo), [(o, n) for _, o, n, _ in todo])
    if not todo:
        print("nothing to do (already applied)")
        return 0
    conn.execute("SAVEPOINT w")
    try:
        for cid, old, new, why in todo:
            conn.execute("UPDATE collection SET name=?, updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), run_id=? WHERE id=?", (new, RUN_ID, cid))
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                         "VALUES ('collection',?,'rename','name',?,?,'Claude',?,?,?)", (cid, old, new, "%s (%s)" % (why, SRC), RUN_ID, WHO))
        dup = one("SELECT count(*) FROM (SELECT name FROM collection WHERE deleted=0 GROUP BY name HAVING count(*)>1)")
        got = one("SELECT count(*) FROM surface_event WHERE run_id=? AND action='rename'", RUN_ID)
        print("actual: %d renames | duplicate names:" % got, dup)
        if got != len(todo) or dup:
            raise Stop("actual differs from predicted or a name is duplicated: rolled back")
        if a.dry_run:
            conn.execute("ROLLBACK TO w"); print("dry run: rolled back")
        else:
            conn.execute("RELEASE w"); conn.commit(); print("committed")
    except Exception:
        conn.execute("ROLLBACK TO w"); conn.commit(); raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
