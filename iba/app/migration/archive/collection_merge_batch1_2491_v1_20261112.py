"""collection_merge_batch1_2491_v1_20261112.py -- escalation #2491, plan v3 step 2, first batch.

Researcher, 2026-11-12: 'Yes, apply them' (sections A, B and D of _analytics/surfaces/exports/collection-merge-proposals-pairs-v2-20261112.md).
Every change is a rule of that file, written as explicit lists so it can be read:
  MERGES   a collection is combined into another: each live link of the combined collection (every tier) moves to the kept collection (a new
           live link, the old one set deleted with superseded_by_id), the core of the combined collection becomes a synonym; where the kept
           collection already holds the term the stronger tier is kept. The combined collection gets status merged and merged_into_id.
  MOVES    named terms move from one collection to another (the splits of instruct, awe and flatter).
  DROPS    a named link is set deleted (an opposite that sits in its own collection, a word regrouped out).
  OPP      an opposite is removed from a collection when the term is a core or synonym of the paired collection.
  NEW      the reverence collection, made from named terms.
  REGROUP  surfaces whose group becomes other (came, the visit family): group corrected, their member links set deleted.
Not done here, by the researcher's matters still open or by their dependence on them: flee into escape (the leave words), the section C
matters, the regroup of please (where pleased, pleasing and pleases go), the regroup of excellent and great (plan step 0).
Then: surface_term.collection_state for every touched term, and ib_node.collection_id for the nodes whose surface changed (the exactly-one rule).
Every change is kept: surface_event for each link and collection, ib_observation_change for each node. Nothing is physically deleted. The run
stops and rolls back unless the counts equal the prediction. Idempotent.
    python iba/app/migration/collection_merge_batch1_2491_v1_20261112.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2491-COLLECTION-BATCH1-20261112"
WHO = "devmode-2491"
RANK = ["core", "synonym", "opposite", "gathered", "phrase", "associated", "possible_opposite", "set_aside"]
MEMBER = ("core", "synonym", "opposite", "gathered", "phrase")
SRC = "researcher 2026-11-12 (#2491): proposals file v2"

MERGES = [  # (kept, [combined...], reason)
    ("supplication", ["pray", "beg"], "asking God or another: one concept"),
    ("insult", ["slander", "mock"], "ridicule and abuse of a person: one concept"),
    ("fast", ["quick"], "speed: one concept"),
    ("covered", ["hid"], "concealment: one concept"),
    ("snatch", ["seize"], "grasping by force: one concept"),
    ("unclean", ["polluted"], "the state of defilement: one concept"),
    ("cleanse", ["purge"], "the act of cleansing: one concept"),
    ("continual", ["always"], "unbroken time: one concept"),
    ("trial", ["test"], "testing and being tried: one concept"),
    ("skill", ["competent"], "ability: one concept"),
    ("amazement", ["marvel", "wonders"], "astonishment and wonder: one concept"),
    ("tenderhearted", ["sympathize"], "compassion and sympathy: one concept"),
    ("greed", ["self-seeking"], "covetousness and greed: one concept"),
    ("teach", ["doctrine"], "teaching as what is taught"),
    ("dedicate", ["committed"], "dedication and devotion"),
    ("firm", ["establishes", "irrevocable"], "firmness: established, steadfast"),
    ("majesty", ["splendor"], "glory and splendor"),
    ("mutter", ["murmur"], "grumbling"),
]
# collections combined only for named terms: (kept, combined, [terms], reason); the combined collection ends merged into kept
SPLITS = [
    ("teach", "instruct", ["instruct", "instructed", "instruction", "instructions", "instructs", "guide", "impart", "explain", "inform", "train"],
     "the teaching words of instruct"),
    ("command", "instruct", ["assign", "tell", "direct", "order", "command"], "the command words of instruct"),
    ("deceive", "flatter", ["flatter"], "flattery is deceitful speech; extol and praise stay in commend"),
    ("reverence", "awe", ["awe", "reverence", "reverent"], "the reverence words of awe"),
    ("majesty", "awe", ["majestic"], "majestic is glory"),
    ("scoff", "awe", ["contempt"], "contempt is the despising of scoff, scorn and disdain"),
    ("roar", "howl", ["howl"], "the loud cry"),
    ("lament", "howl", ["wailed", "wailing"], "the wail words are lament"),
]
# terms of a combined collection that are dropped, not moved (already members elsewhere, or not a member any more)
DROP_ON_COMBINE = {
    "awe": ["amazed", "amazement", "astonishment", "astounded", "awe-inspiring", "marveling", "wondrous"],   # amazement holds them
    "flatter": ["extol", "praise"],                                                                          # commend holds them
}
# terms moved into the new reverence collection from named collections: (from, [terms])
REVERENCE_FROM = [("offer", ["kneeling", "knelt", "worshiped", "worshiping", "worships"]), ("fear", ["worship"]), ("honor", ["revere"])]
DROPS = [("offer", ["came"], "a plain motion word, regrouped out"), ("visit", ["leave", "visit"], "the visit family is regrouped out"),
         ("taste", ["abhor", "loathe"], "taste is not the pole of loathing")]
OPP = [("lament", "gladden"), ("hope", "doom"), ("faint", "mighty"), ("commend", "chide"), ("shut", "open"), ("empty", "fill"),
       ("faithless", "loyalty"), ("offer", "reject")]
OPP_ALSO = [("offer", ["deny", "refuse", "refuses"])]   # an opposite of offer is removed where the word is a member elsewhere (rule R4)
REGROUP = [("other", ["came", "visit", "visits", "visited", "visiting"],
            "not a behaviour or an inner-being state (researcher 2026-11-12, #2491): a motion word, and God's visiting or an ordinary action")]
RETIRE = [("visit", "retired")]
NEW = {"name": "reverence", "core": "reverence"}


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
    term = {}
    for r in q("SELECT id, surface FROM surface_term WHERE deleted=0"):
        term.setdefault(r["surface"], r["id"])
    new_exists = NEW["name"] in cname
    need_c = {k for k, _, _ in MERGES for k in [k]} | {x for _, xs, _ in MERGES for x in xs} | {k for k, _, _, _ in SPLITS} | {x for _, x, _, _ in SPLITS}
    need_c |= {f for f, _ in REVERENCE_FROM} | {c for c, _, _ in DROPS} | {x for p in OPP for x in p} | {c for c, _ in RETIRE} | {"commend", "chide"}
    need_c.discard(NEW["name"])
    live_after_first_run = {n for n in need_c if n not in cname}
    # a second run: combined collections are already merged; they are not an error
    merged_names = {r["name"] for r in q("SELECT name FROM collection WHERE deleted=0 AND status IN ('merged','retired')")}
    missing = sorted(live_after_first_run - merged_names)
    if missing:
        raise Stop("collections not found: %s" % missing)

    def live_links(col):
        return {r["term_id"]: r for r in q("SELECT * FROM collection_link WHERE collection_id=? AND deleted=0", col)}

    actions = []   # ('move', from_link_id, to_collection, term, tier, reason) | ('drop', link_id, reason) | ('insert', collection, term, tier, reason)
    pending_ins = {}   # (collection, term) -> tier chosen in this plan
    drops_planned = set()

    def tier_of(col, t):
        if (col, t) in pending_ins:
            return pending_ins[(col, t)]
        r = conn.execute("SELECT tier FROM collection_link WHERE collection_id=? AND term_id=? AND deleted=0", (col, t)).fetchone()
        return r[0] if r else None

    def plan_move(src_link, to_col, reason, tier=None):
        t = src_link["term_id"]
        tr = tier or src_link["tier"]
        have = tier_of(to_col, t)
        if src_link["id"] in drops_planned:
            return
        drops_planned.add(src_link["id"])
        if have is None:
            actions.append(("move", src_link["id"], to_col, t, tr, reason)); pending_ins[(to_col, t)] = tr
        elif RANK.index(tr) < RANK.index(have):
            actions.append(("upgrade", src_link["id"], to_col, t, tr, reason)); pending_ins[(to_col, t)] = tr
        else:
            actions.append(("drop", src_link["id"], reason + " (the kept collection already holds it)"))

    def plan_drop(link, reason):
        if link["id"] in drops_planned:
            return
        drops_planned.add(link["id"]); actions.append(("drop", link["id"], reason))

    collections_to_mark = []   # (collection id, status, merged_into id or None, reason)
    for kept, xs, why in MERGES:
        if kept not in cname:
            continue
        for x in xs:
            if x not in cname:
                continue
            for t, l in live_links(cname[x]).items():
                tier = "synonym" if l["tier"] == "core" else l["tier"]
                plan_move(l, cname[kept], "combined %s into %s: %s" % (x, kept, why), tier)
            collections_to_mark.append((cname[x], "merged", kept, "combined into %s: %s" % (kept, why)))
    # the reverence collection (new): the core and the named terms
    if not new_exists:
        core = term[NEW["core"]]
        actions.append(("newcol", NEW["name"], core))
    rev = cname.get(NEW["name"])
    new_terms = set()

    def add_tonew(link, t, tier, why):
        if link["id"] in drops_planned:
            return
        if t in new_terms:
            plan_drop(link, why + " (the new collection already holds it)")
            return
        new_terms.add(t)
        actions.append(("tonew", link["id"], t, tier, why)); drops_planned.add(link["id"])
    for fr, ts in REVERENCE_FROM:
        if fr in cname:
            lk = live_links(cname[fr])
            for s in ts:
                if term[s] in lk:
                    add_tonew(lk[term[s]], term[s], "synonym", "the reverence and worship concept: %s from %s" % (s, fr))
    for kept, x, ts, why in SPLITS:
        if x not in cname:
            continue
        lk = live_links(cname[x])
        for s in ts:
            if term[s] in lk:
                if kept == "reverence" and (rev is None):
                    if s == NEW["core"]:
                        plan_drop(lk[term[s]], "%s: %s (the new collection takes it as its core)" % (x, why))
                    else:
                        add_tonew(lk[term[s]], term[s], "synonym", "%s: %s" % (x, why))
                else:
                    plan_move(lk[term[s]], cname[kept], "%s: %s" % (x, why), "synonym")
    for x, ts in DROP_ON_COMBINE.items():
        if x in cname:
            lk = live_links(cname[x])
            for s in ts:
                if term[s] in lk:
                    plan_drop(lk[term[s]], "word of %s that another collection holds" % x)
    # what remains of the split collections: the rest of its links are dropped (they are held elsewhere or belong nowhere in it)
    # what remains in a split collection moves to the kept collection (coverage is never reduced), with by-meaning overrides
    default_to = {"awe": "reverence", "flatter": "deceive", "instruct": "teach", "howl": "roar"}
    override = {"forbidden": "command", "kneel": "reverence", "announce": "preach"}
    text_of = {v: k for k, v in term.items()}
    for x in ("awe", "flatter", "instruct", "howl"):
        if x in cname:
            collections_to_mark.append((cname[x], "merged", default_to[x], "combined by named terms (see the batch file)"))
            for t, l in live_links(cname[x]).items():
                if l["id"] in drops_planned:
                    continue
                s = text_of.get(t, "")
                target = override.get(s) or ("command" if x == "instruct" and (s.startswith("tell ") or s.startswith("told ")) else default_to[x])
                tier = "synonym" if l["tier"] == "core" else l["tier"]
                why = "the rest of %s moves to %s (%s)" % (x, target, "by meaning" if target != default_to[x] else "the kept collection")
                if target == "reverence" and rev is None:
                    add_tonew(l, t, tier, why)
                else:
                    plan_move(l, cname[target], why, tier)
    for col, ts, why in DROPS:
        if col in cname:
            lk = live_links(cname[col])
            for s in ts:
                if term[s] in lk:
                    plan_drop(lk[term[s]], why)
    for x, kind in RETIRE:
        if x in cname:
            collections_to_mark.append((cname[x], kind, None, "the concept is not a behaviour or inner-being state"))
            for t, l in live_links(cname[x]).items():
                plan_drop(l, "the %s collection is retired" % x)
    # opposites: removed from a collection where the term is a core or synonym of the paired collection
    for a_, b_ in OPP:
        if a_ in cname and b_ in cname:
            for (x, y) in ((a_, b_), (b_, a_)):
                lx, ly = live_links(cname[x]), live_links(cname[y])
                for t, l in lx.items():
                    if l["tier"] == "opposite" and t in ly and ly[t]["tier"] in ("core", "synonym"):
                        plan_drop(l, "an opposite sits once: the term is a member of %s" % y)
    for col, ts in OPP_ALSO:
        if col in cname:
            lk = live_links(cname[col])
            for s in ts:
                if term.get(s) in lk and lk[term[s]]["tier"] == "opposite":
                    other = q("SELECT 1 FROM collection_link WHERE term_id=? AND deleted=0 AND collection_id<>? AND tier IN ('core','synonym')", term[s], cname[col])
                    if other:
                        plan_drop(lk[term[s]], "an opposite sits once: the word is a member elsewhere")
    # regroup: group other, and every live member link of the term set deleted
    regroup_terms = []
    for grp, ss, why in REGROUP:
        for s in ss:
            r = conn.execute("SELECT id, surface_group FROM surface_term WHERE deleted=0 AND surface=?", (s,)).fetchone()
            if r and r["surface_group"] != grp:
                regroup_terms.append((r["id"], s, r["surface_group"], grp, why))
                for l in q("SELECT * FROM collection_link WHERE term_id=? AND deleted=0 AND tier IN (%s)" % ",".join("?" * len(MEMBER)), r["id"], *MEMBER):
                    plan_drop(l, "the surface %s is regrouped to %s" % (s, grp))

    kinds = collections.Counter(a_[0] for a_ in actions)
    live_links_before = one("SELECT count(*) FROM collection_link WHERE deleted=0")
    to_mark = [m for m in collections_to_mark if one("SELECT status FROM collection WHERE id=?", m[0]) not in ("merged", "retired")]
    n_ins = kinds["move"] + kinds["upgrade"] + kinds["tonew"]
    n_del = kinds["move"] + 2 * kinds["upgrade"] + kinds["tonew"] + kinds["drop"]
    pred = dict(actions=dict(kinds), collections_marked=len(to_mark), new_collection=int(any(a_[0] == "newcol" for a_ in actions)),
                regrouped=len(regroup_terms), live_links_after=live_links_before + n_ins + kinds["newcol"] - n_del)
    print("predicted:", pred)
    if not actions and not to_mark and not regroup_terms:
        print("nothing to do (already applied)")
        return 0
    conn.execute("SAVEPOINT w")
    try:
        now_sql = "strftime('%Y-%m-%dT%H:%M:%SZ','now')"
        touched_terms = set()

        def ev(subject, sid, action, before, after, reason):
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                         "VALUES (?,?,?,?,?,?,?,?,?,?)", (subject, sid, action, "collection_id" if subject == "collection_link" else None, before, after, "Claude",
                                                           "%s (%s)" % (reason, SRC), RUN_ID, WHO))

        def new_link(col, t, tier, reason, old_id):
            cur = conn.execute("INSERT INTO collection_link (collection_id, term_id, tier, superseded_by_id, shared, reason, run_id, created_by) VALUES (?,?,?,NULL,0,?,?,?)",
                               (col, t, tier, reason, RUN_ID, WHO))
            return cur.lastrowid

        def kill(old_id, new_id):
            conn.execute("UPDATE collection_link SET deleted=1, superseded_by_id=?, updated_at=" + now_sql + ", run_id=? WHERE id=?", (new_id, RUN_ID, old_id))

        newcol_id = None
        for act in actions:
            if act[0] == "newcol":
                cur = conn.execute("INSERT INTO collection (core_term_id, name, status, run_id, created_by) VALUES (?,?, 'confirmed', ?, ?)", (act[2], act[1], RUN_ID, WHO))
                newcol_id = cur.lastrowid
                cname[act[1]] = newcol_id; cid_name[newcol_id] = act[1]
                ev("collection", newcol_id, "move", None, act[1], "new collection: the reverence and worship concept")
                nl = new_link(newcol_id, act[2], "core", "the core of the new collection", None)
                touched_terms.add(act[2])
        if newcol_id is None and NEW["name"] in cname:
            newcol_id = cname[NEW["name"]]
        for act in actions:
            if act[0] in ("move", "upgrade"):
                _, old, to_col, t, tier, reason = act
                oc = one("SELECT collection_id FROM collection_link WHERE id=?", old)
                if act[0] == "upgrade":
                    cur = conn.execute("SELECT id FROM collection_link WHERE collection_id=? AND term_id=? AND deleted=0", (to_col, t)).fetchone()
                    if cur:
                        kill(cur[0], None)
                        nl = new_link(to_col, t, tier, reason, cur[0])
                        conn.execute("UPDATE collection_link SET superseded_by_id=? WHERE id=?", (nl, cur[0]))
                        ev("collection_link", nl, "set_tier", str(cur[0]), str(nl), reason)
                        kill(old, nl); ev("collection_link", old, "move", cid_name.get(oc), cid_name.get(to_col), reason)
                        touched_terms.add(t); continue
                nl = new_link(to_col, t, tier, reason, old)
                kill(old, nl); ev("collection_link", nl, "move", cid_name.get(oc), cid_name.get(to_col), reason); touched_terms.add(t)
            elif act[0] == "tonew":
                _, old, t, tier, reason = act
                oc = one("SELECT collection_id FROM collection_link WHERE id=?", old)
                nl = new_link(newcol_id, t, tier, reason, old)
                kill(old, nl); ev("collection_link", nl, "move", cid_name.get(oc), cid_name.get(newcol_id), reason); touched_terms.add(t)
            elif act[0] == "drop":
                _, old, reason = act
                oc, t = conn.execute("SELECT collection_id, term_id FROM collection_link WHERE id=?", (old,)).fetchone()
                kill(old, None); ev("collection_link", old, "remove", cid_name.get(oc), None, reason); touched_terms.add(t)
        for cid, status, into_name, reason in to_mark:
            into = cname.get(into_name) if into_name else None
            if status == "merged" and into is None:
                raise Stop("merge target %r not found" % into_name)
            conn.execute("UPDATE collection SET status=?, merged_into_id=?, updated_at=" + now_sql + ", run_id=? WHERE id=?", (status, into, RUN_ID, cid))
            ev("collection", cid, "merge" if status == "merged" else "retire", None, into_name, reason)
        for tid, s, before, grp, why in regroup_terms:
            conn.execute("UPDATE surface_term SET surface_group=?, group_state='corrected', group_judged_by='Claude (researcher direction, #2491)', group_reason=?, "
                         "updated_at=" + now_sql + ", run_id=? WHERE id=?", (grp, why, RUN_ID, tid))
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) VALUES "
                         "('surface_term',?,'set_group','surface_group',?,?,'Claude',?,?,?)", (tid, before, grp, why, RUN_ID, WHO))
            touched_terms.add(tid)
        # collection_state of every touched term, and of the terms derived from them
        derived = set()
        for t in list(touched_terms):
            derived |= {r[0] for r in q("SELECT id FROM surface_term WHERE deleted=0 AND base_id=?", t)}
        for t in touched_terms | derived:
            ls = q("SELECT collection_id, tier FROM collection_link WHERE term_id=? AND deleted=0", t)
            strong = {r["collection_id"] for r in ls if r["tier"] in ("core", "synonym", "opposite")}
            if not ls:
                st = "untouched" if one("SELECT count(*) FROM surface_term WHERE id=? AND collection_state IS NOT NULL", t) else None
            elif len(strong) > 1:
                st = "shared"
            elif any(r["tier"] in MEMBER for r in ls):
                st = "placed"
            elif any(r["tier"] == "set_aside" for r in ls):
                st = "set_aside"
            else:
                st = "listed_only"
            conn.execute("UPDATE surface_term SET collection_state=? WHERE id=? AND COALESCE(collection_state,'~')<>COALESCE(?,'~')", (st, t, st))
        # the node column: the exactly-one rule for the nodes whose surface changed or that pointed at a combined collection
        cols_now = collections.defaultdict(set)
        for r in q("SELECT l.term_id, l.collection_id FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 "
                   "AND c.status IN ('indicative','confirmed') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER):
            cols_now[r[0]].add(r[1])
        st_by_surface = collections.defaultdict(list)
        for r in q("SELECT id, surface, base_id FROM surface_term WHERE deleted=0"):
            st_by_surface[r["surface"]].append((r["id"], r["base_id"]))

        def carry(s):
            o = set()
            for sid, b in st_by_surface.get(s, []):
                o |= cols_now.get(sid, set()) | (cols_now.get(b, set()) if b else set())
            return o
        retired_ids = {c[0] for c in collections_to_mark}
        surf_touched = {r["surface"] for r in q("SELECT surface FROM surface_term WHERE id IN (%s)" % ",".join(str(x) for x in (touched_terms | derived) or {0}))}
        changed_nodes = 0
        for n in q("SELECT id, observation_id, collection_id, lower(trim(surface)) AS s FROM ib_node WHERE deleted=0 AND surface IS NOT NULL AND trim(surface)<>''"):
            if n["s"] in surf_touched or n["collection_id"] in retired_ids:
                cs = carry(n["s"])
                new = next(iter(cs)) if len(cs) == 1 else None
                if new != n["collection_id"]:
                    orec.log(conn, n["observation_id"], n["id"], "collection_id", n["collection_id"], new,
                             "the collections were combined and sorted (researcher 2026-11-12, #2491); the node carries the one collection of its surface, or none where it has none or several", None, RUN_ID, "Claude")
                    conn.execute("UPDATE ib_node SET collection_id=? WHERE id=?", (new, n["id"])); changed_nodes += 1
        got = dict(collections_marked=one("SELECT count(*) FROM collection WHERE deleted=0 AND status IN ('merged','retired') AND run_id=?", RUN_ID),
                   new_collection=int(newcol_id is not None and one("SELECT count(*) FROM collection WHERE id=? AND run_id=?", newcol_id, RUN_ID) > 0),
                   regrouped=one("SELECT count(*) FROM surface_event WHERE run_id=? AND action='set_group'", RUN_ID),
                   live_links_after=one("SELECT count(*) FROM collection_link WHERE deleted=0"))
        print("actual:   ", got, "| nodes whose collection changed:", changed_nodes)
        cmp_keys = ("collections_marked", "new_collection", "regrouped", "live_links_after")
        bad = [k for k in cmp_keys if got[k] != pred[k]]
        stranded = conn.execute(
            "SELECT count(*) FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.status IN ('merged','retired') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), MEMBER).fetchone()[0]
        print("member links still on a merged or retired collection:", stranded)
        if bad or stranded:
            raise Stop("actual differs from predicted (%s) or links are stranded: rolled back" % bad)
        if a.dry_run:
            conn.execute("ROLLBACK TO w"); print("dry run: rolled back")
        else:
            conn.execute("RELEASE w"); conn.commit(); print("committed")
    except Exception:
        conn.execute("ROLLBACK TO w"); conn.commit(); raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
