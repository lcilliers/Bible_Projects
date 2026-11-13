"""collection_phrases_step4b_2491_v1_20261113.py -- escalation #2491, plan v3 step 4 (phrases), the eight left over.

The first run (collection_phrases_step4_2491_v1_20261113.py) left eight phrases in several collections because I had not written their ruling into its list: make known, clears away, exalted me above, highly exalted, refused him, reject him, richly supplied, set forth. This run gives each its one collection. Same rules and checks as the first run.

Researcher, 2026-11-13: 'Yes, step 4'. Rule of the researcher (#2491 v9/v11): a phrase is one concept, and the concept is placed in one collection;
it is not attached to the collections of each of its words. The phrase rule of #2437 (attach_phrases) put 3,134 phrase links into several collections;
here the 490 phrase surfaces that sat in two or more collections, the 34 whose only collection was dissolved, and the clear cases among the 106
study phrases in none were read by meaning, one by one, and each was given the one collection of its concept (PLACE) or, where it is a generic
phrase (set up, went up, come upon, lift up, to do) and not a behaviour or an inner-being state, was regrouped to other (OTHER). The lists are the ruling;
every ruling is inferential (B:4), none is made by a script rule. Phrases in exactly one collection are not touched. Phrases not listed stay as they are.
PLACE: the phrase keeps (or gets, as tier phrase) its link in the named collection and every other member link of the surface is set deleted.
OTHER: group other (group state corrected, reason kept) and every member link set deleted.
Then surface_term.collection_state and ib_node.collection_id (the exactly-one rule). Nothing is physically deleted. Stops and rolls back unless predicted
equals actual, every placed phrase is in exactly its one collection, and nothing except the regrouped phrases loses its collection. Idempotent.
    python -m iba.app.migration.collection_phrases_step4b_2491_v1_20261113 [--db PATH] [--dry-run]   (from the project root)
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
RUN_ID = "DEVMODE-2491-PHRASES-STEP4B-20261113"
WHO = "devmode-2491"
MEMBER = ("core", "synonym", "opposite", "gathered", "phrase")
SRC = "researcher 2026-11-13 (#2491): step 4"

PLACE_LINES = """
know: make known
remove: clears away
chief: exalted me above; highly exalted
reject: refused him; reject him
supply: richly supplied
preach: set forth
"""
OTHER = """"""
PLACE = {}
for line in PLACE_LINES.strip().splitlines():
    col, phrases = line.split(":", 1)
    for p in phrases.split(";"):
        p = p.strip()
        if p:
            if p in PLACE:
                raise SystemExit("phrase ruled twice: %s (%s, %s)" % (p, PLACE[p], col))
            PLACE[p] = col.strip()
OTHER_SET = {p.strip() for p in OTHER.replace("\n", " ").split(";") if p.strip()}
both = set(PLACE) & OTHER_SET
if both:
    raise SystemExit("phrase in both lists: %s" % sorted(both))


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
    missing = sorted({c for c in PLACE.values() if c not in cname})
    if missing:
        raise Stop("collections not found: %s" % missing)
    rows_by_text = collections.defaultdict(list)
    text_of = {}
    for r in q("SELECT id, surface, surface_group FROM surface_term WHERE deleted=0"):
        rows_by_text[r["surface"]].append(r)
        text_of[r["id"]] = r["surface"]
    absent = sorted(p for p in list(PLACE) + sorted(OTHER_SET) if p not in rows_by_text)
    links_of = collections.defaultdict(list)
    for r in q("SELECT l.* FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 AND c.status IN ('indicative','confirmed') "
               "AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER):
        links_of[r["term_id"]].append(r)

    actions = []   # ("add", col, term, reason) | ("drop", link id, reason)
    regroup = []   # (term id, surface, group before, reason)
    regroup_ids = set()
    for p, kc in PLACE.items():
        k = cname[kc]
        for r in rows_by_text.get(p, []):
            ls = links_of.get(r["id"], [])
            if not any(l["collection_id"] == k for l in ls):
                actions.append(("add", k, r["id"], "the phrase %s is one concept, placed in %s (step 4, by meaning)" % (p, kc)))
            for l in ls:
                if l["collection_id"] != k:
                    actions.append(("drop", l["id"], "the phrase %s sits once, in %s (step 4, by meaning)" % (p, kc)))
    why_o = "a generic phrase (a motion, placing or plain-action phrase), not a behaviour or an inner-being state (researcher 2026-11-13, #2491 step 4)"
    for p in sorted(OTHER_SET):
        for r in rows_by_text.get(p, []):
            regroup_ids.add(r["id"])
            for l in links_of.get(r["id"], []):
                actions.append(("drop", l["id"], "the phrase %s is regrouped to other: %s" % (p, why_o)))
            if r["surface_group"] != "other":
                regroup.append((r["id"], p, r["surface_group"], why_o))

    def covered_set():
        own = {r[0] for r in q("SELECT DISTINCT l.term_id FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 "
                               "AND c.status IN ('indicative','confirmed') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER)}
        out = set(own)
        for r in q("SELECT id, base_id FROM surface_term WHERE deleted=0"):
            if r["id"] in own or (r["base_id"] and r["base_id"] in own):
                out.add(r["id"])
        return out
    covered_before = covered_set()
    kinds = collections.Counter(a_[0] for a_ in actions)
    live_before = one("SELECT count(*) FROM collection_link WHERE deleted=0")
    pred = dict(actions=dict(kinds), regrouped=len(regroup), live_links_after=live_before + kinds["add"] - kinds["drop"])
    print("predicted:", pred, "| phrases placed:", len(PLACE), "| regrouped list:", len(OTHER_SET), "| not found as a surface:", absent)
    if not actions and not regroup:
        print("nothing to do (already applied)")
        return 0
    regrouped_before = one("SELECT count(*) FROM surface_event WHERE run_id=? AND action='set_group'", RUN_ID)
    conn.execute("SAVEPOINT w")
    try:
        now_sql = "strftime('%Y-%m-%dT%H:%M:%SZ','now')"
        touched = set()

        def ev(subject, sid, action, before, after, reason, field=None):
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                         "VALUES (?,?,?,?,?,?,?,?,?,?)", (subject, sid, action, field, before, after, "Claude", "%s (%s)" % (reason, SRC), RUN_ID, WHO))
        for act in actions:
            if act[0] == "add":
                _, col, t, reason = act
                nl = conn.execute("INSERT INTO collection_link (collection_id, term_id, tier, superseded_by_id, shared, reason, run_id, created_by) VALUES (?,?,'phrase',NULL,0,?,?,?)",
                                  (col, t, reason, RUN_ID, WHO)).lastrowid
                ev("collection_link", nl, "add", None, cid_name.get(col), reason, "collection_id"); touched.add(t)
            else:
                _, old, reason = act
                oc, t = conn.execute("SELECT collection_id, term_id FROM collection_link WHERE id=?", (old,)).fetchone()
                conn.execute("UPDATE collection_link SET deleted=1, updated_at=" + now_sql + ", run_id=? WHERE id=?", (RUN_ID, old))
                ev("collection_link", old, "remove", cid_name.get(oc), None, reason, "collection_id"); touched.add(t)
        for tid, p, before, why in regroup:
            conn.execute("UPDATE surface_term SET surface_group='other', group_state='corrected', group_judged_by='Claude (researcher direction, #2491)', group_reason=?, "
                         "updated_at=" + now_sql + ", run_id=? WHERE id=?", (why, RUN_ID, tid))
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) VALUES "
                         "('surface_term',?,'set_group','surface_group',?,'other','Claude',?,?,?)", (tid, before, why + " (" + SRC + ")", RUN_ID, WHO))
            touched.add(tid)
        for t in touched:
            ls = q("SELECT l.collection_id, l.tier FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.term_id=? AND l.deleted=0 AND c.status IN ('indicative','confirmed')", t)
            strong = {r["collection_id"] for r in ls if r["tier"] in ("core", "synonym", "opposite")}
            if not ls:
                st = "untouched" if one("SELECT count(*) FROM surface_term WHERE id=? AND collection_state IS NOT NULL", t) else None
            elif len(strong) > 1:
                st = "shared"
            elif any(r["tier"] in MEMBER for r in ls):
                st = "placed"
            else:
                st = "listed_only"
            conn.execute("UPDATE surface_term SET collection_state=? WHERE id=? AND COALESCE(collection_state,'~')<>COALESCE(?,'~')", (st, t, st))
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
                o |= cols_now.get(sid, set()) | (cols_now.get(b, set()) if b else set())
            return o
        surf_touched = {text_of[t] for t in touched if t in text_of}
        changed_nodes = 0
        for n in q("SELECT id, observation_id, collection_id, lower(trim(surface)) AS s FROM ib_node WHERE deleted=0 AND surface IS NOT NULL AND trim(surface)<>''"):
            if n["s"] in surf_touched:
                cs = carry(n["s"])
                new = next(iter(cs)) if len(cs) == 1 else None
                if new != n["collection_id"]:
                    orec.log(conn, n["observation_id"], n["id"], "collection_id", n["collection_id"], new,
                             "each phrase is one concept in one collection (researcher 2026-11-13, #2491 step 4); the node carries the one collection of its surface, or none where it has none or several", None, RUN_ID, "Claude")
                    conn.execute("UPDATE ib_node SET collection_id=? WHERE id=?", (new, n["id"])); changed_nodes += 1
        got = dict(regrouped=one("SELECT count(*) FROM surface_event WHERE run_id=? AND action='set_group'", RUN_ID) - regrouped_before,
                   live_links_after=one("SELECT count(*) FROM collection_link WHERE deleted=0"))
        print("actual:   ", got, "| nodes whose collection changed:", changed_nodes)
        bad = [k for k in ("regrouped", "live_links_after") if got[k] != pred[k]]
        stranded = one("SELECT count(*) FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.status IN ('merged','retired') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER)
        lost = sorted(text_of[t] for t in covered_before - covered_set() if t in text_of and t not in regroup_ids)
        notone = sorted(p for p in PLACE if rows_by_text.get(p) and any(len(cols_now.get(r["id"], set())) != 1 for r in rows_by_text[p]))
        print("member links on a merged or retired collection:", stranded, "| surfaces losing coverage (not regrouped):", len(lost), lost[:40],
              "| placed phrases not in exactly one collection:", len(notone), notone[:20])
        if bad or stranded or lost or notone:
            raise Stop("actual differs from predicted (%s), links stranded, coverage lost or a placed phrase not in one collection: rolled back" % bad)
        if a.dry_run:
            conn.execute("ROLLBACK TO w"); print("dry run: rolled back")
        else:
            conn.execute("RELEASE w"); conn.commit(); print("committed")
    except Exception:
        conn.execute("ROLLBACK TO w"); conn.commit(); raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
