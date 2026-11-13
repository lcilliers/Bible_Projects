"""collection_derived_step5b_2491_v1_20261113.py -- escalation #2491, plan v3 step 5, correction and the node column by the own-row rule.

After the step 5 run the check of the node column showed 145 nodes whose surface was in two collections under the old rule of the node column (the
collections of the surface's own row UNITED with those of its base). With members being surfaces (step 5) the rule is now: a surface's own row decides;
only a surface with no link of its own is read through its base. That rule is applied here to every live node with a surface (no other rule is used again).
Four placements of step 5 disagreed with the forms already in a collection and are aligned by meaning (inferential, B:4): foolish and fools go to folly with
fool and fool's (they were opposites in wise); sorrow goes to tribulation with sorrowful (it had been placed in pain); carefully goes to care with care (it was
gathered in ask); mind goes to heart with minds (it had been placed in thought).
Every link change is kept in surface_event (a link set deleted keeps its row; a new link is a new row); every node change in ib_observation_change.
Nothing is physically deleted. The run stops and rolls back unless, after the write, every node with a collection carries exactly the one collection of
its surface by the own-row rule and every node whose surface has exactly one collection carries it. Idempotent.
    python -m iba.app.migration.collection_derived_step5b_2491_v1_20261113 [--db PATH] [--dry-run]   (from the project root)
"""
import argparse
import collections
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.lib import observationrecord as orec  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2491-DERIVED-STEP5B-20261113"
WHO = "devmode-2491"
MEMBER = ("core", "synonym", "opposite", "gathered", "phrase")
SRC = "researcher 2026-11-13 (#2491): step 5"
ALIGN = {"folly": ["foolish", "fools", "fool", "fool’s"], "tribulation": ["sorrow"], "care": ["carefully"], "heart": ["mind"]}


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
    cname = {r["name"]: r["id"] for r in q("SELECT id, name FROM collection WHERE deleted=0 AND status IN ('indicative','confirmed')")}
    cid_name = {v: k for k, v in cname.items()}
    conn.execute("SAVEPOINT w")
    try:
        now_sql = "strftime('%Y-%m-%dT%H:%M:%SZ','now')"

        def ev(subject, sid, action, before, after, reason):
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                         "VALUES (?,?,?,?,?,?,?,?,?,?)", (subject, sid, action, "collection_id", before, after, "Claude", "%s (%s)" % (reason, SRC), RUN_ID, WHO))
        terms = {r["id"]: r for r in q("SELECT id, surface, base_id FROM surface_term WHERE deleted=0")}
        ids_of = collections.defaultdict(list)
        for t, r in terms.items():
            ids_of[r["surface"]].append(t)
        moved = 0
        for kc, words in ALIGN.items():
            k = cname[kc]
            for w in words:
                for tid in ids_of.get(w, []):
                    cur = q("SELECT l.id, l.collection_id, l.tier FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.term_id=? AND l.deleted=0 "
                            "AND c.status IN ('indicative','confirmed') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), tid, *MEMBER)
                    if any(c_["collection_id"] == k for c_ in cur):
                        for c_ in cur:
                            if c_["collection_id"] != k:
                                conn.execute("UPDATE collection_link SET deleted=1, updated_at=" + now_sql + ", run_id=? WHERE id=?", (RUN_ID, c_["id"]))
                                ev("collection_link", c_["id"], "remove", cid_name.get(c_["collection_id"]), None, "%s sits once, in %s (step 5 alignment)" % (w, kc)); moved += 1
                        continue
                    tier = cur[0]["tier"] if cur else "synonym"
                    for c_ in cur:
                        conn.execute("UPDATE collection_link SET deleted=1, updated_at=" + now_sql + ", run_id=? WHERE id=?", (RUN_ID, c_["id"]))
                        ev("collection_link", c_["id"], "remove", cid_name.get(c_["collection_id"]), None, "%s sits once, in %s (step 5 alignment)" % (w, kc))
                    old = conn.execute("SELECT id FROM collection_link WHERE collection_id=? AND term_id=? AND deleted=0", (k, tid)).fetchone()
                    if old:
                        conn.execute("UPDATE collection_link SET deleted=1, updated_at=" + now_sql + ", run_id=? WHERE id=?", (RUN_ID, old[0]))
                    nl = conn.execute("INSERT INTO collection_link (collection_id, term_id, tier, superseded_by_id, shared, reason, run_id, created_by) VALUES (?,?,?,NULL,0,?,?,?)",
                                      (k, tid, "synonym" if tier == "core" else tier, "%s sits once, in %s (step 5 alignment)" % (w, kc), RUN_ID, WHO)).lastrowid
                    ev("collection_link", nl, "move", ",".join(cid_name.get(c_["collection_id"], "") for c_ in cur) or None, kc, "%s sits once, in %s (step 5 alignment)" % (w, kc)); moved += 1
        # collection_state for every term whose links changed in this run
        touched = {r[0] for r in q("SELECT DISTINCT term_id FROM collection_link WHERE run_id=?", RUN_ID)}
        for t in touched:
            ls = q("SELECT l.collection_id, l.tier FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.term_id=? AND l.deleted=0 AND c.status IN ('indicative','confirmed')", t)
            strong = {r["collection_id"] for r in ls if r["tier"] in ("core", "synonym", "opposite")}
            st = "shared" if len(strong) > 1 else ("placed" if any(r["tier"] in MEMBER for r in ls) else ("listed_only" if ls else "untouched"))
            conn.execute("UPDATE surface_term SET collection_state=? WHERE id=? AND COALESCE(collection_state,'~')<>?", (st, t, st))
        # the node column by the own-row rule: own links decide; a surface with none is read through its base
        cols_now = collections.defaultdict(set)
        for r in q("SELECT l.term_id, l.collection_id FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 "
                   "AND c.status IN ('indicative','confirmed') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER):
            cols_now[r[0]].add(r[1])
        by_surface = collections.defaultdict(list)
        for r in q("SELECT id, surface, base_id FROM surface_term WHERE deleted=0"):
            by_surface[r["surface"]].append((r["id"], r["base_id"]))

        def carry(s):
            o = set()
            for sid, b in by_surface.get(s, []):
                o |= cols_now.get(sid) or (cols_now.get(b, set()) if b else set())
            return o
        changed = 0
        for n in q("SELECT id, observation_id, collection_id, lower(trim(surface)) AS s FROM ib_node WHERE deleted=0 AND surface IS NOT NULL AND trim(surface)<>''"):
            cs = carry(n["s"])
            new = next(iter(cs)) if len(cs) == 1 else None
            if new != n["collection_id"]:
                orec.log(conn, n["observation_id"], n["id"], "collection_id", n["collection_id"], new,
                         "members are surfaces (researcher 2026-11-13, #2491 step 5): the node carries the one collection of its surface by the own-row rule (a surface with a link of its own is read by it; one without, through its base), or none where it has none or several", None, RUN_ID, "Claude")
                conn.execute("UPDATE ib_node SET collection_id=? WHERE id=?", (new, n["id"])); changed += 1
        bad = 0
        for n in q("SELECT collection_id, lower(trim(surface)) AS s FROM ib_node WHERE deleted=0 AND surface IS NOT NULL AND trim(surface)<>''"):
            cs = carry(n["s"])
            if (len(cs) == 1 and n["collection_id"] not in cs) or (len(cs) != 1 and n["collection_id"] is not None):
                bad += 1
        dead = one("SELECT count(*) FROM ib_node n JOIN collection c ON c.id=n.collection_id WHERE n.deleted=0 AND c.status NOT IN ('indicative','confirmed')")
        print("links changed:", moved, "| nodes changed:", changed, "| nodes not matching the own-row rule after the write:", bad, "| nodes on a merged or retired collection:", dead)
        if bad or dead:
            raise Stop("a node does not match the own-row rule: rolled back")
        if a.dry_run:
            conn.execute("ROLLBACK TO w"); print("dry run: rolled back")
        else:
            conn.execute("RELEASE w"); conn.commit(); print("committed")
    except Exception:
        conn.execute("ROLLBACK TO w"); conn.commit(); raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
