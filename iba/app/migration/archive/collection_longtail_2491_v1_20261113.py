"""collection_longtail_2491_v1_20261113.py -- escalation #2491, plan v3 step 2, the long tail (the story test of the whole list).

Researcher, 2026-11-13: 'Yes, long tail'. After the overlaps (entries 498, 499) every one of the 226 collections was read with all its word members and
judged by meaning: do the members share one concept, is the collection small enough to be grouped with like-minded ones, and does each member belong.
Explicit lists, so each can be read (every ruling is inferential, B:4; none is made by a script rule):
  MOVES     a word that does not belong where it is goes to the collection of its sense (a word is in one collection only), or to OTHER (regrouped to
            group other: a generic word that is not a behaviour or an inner-being state).
  MERGES    a small collection is combined into a like-minded one (every link, every tier, moves; the core becomes a synonym; the combined collection is
            marked merged with merged_into_id). Opposite words stay opposite.
  RETIRE    a collection that held only generic words is dissolved (status retired).
Nothing is physically deleted (links are set deleted, a moved link is a new row with the old row superseded). The members of every collection
changed are recomputed in surface_term.collection_state and the node column follows the own-row rule (a surface with a link of its own is read by it;
one without, through its base). Stops and rolls back unless predicted equals actual, no surface other than the regrouped words and their derived forms
loses its collection, every moved word is in exactly one collection, and every node matches the rule. Idempotent.
    python -m iba.app.migration.collection_longtail_2491_v1_20261113 [--db PATH] [--dry-run]   (from the project root)
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
RUN_ID = "DEVMODE-2491-LONGTAIL-20261113"
WHO = "devmode-2491"
RANK = ["core", "synonym", "opposite", "gathered", "phrase", "associated", "possible_opposite", "set_aside"]
MEMBER = ("core", "synonym", "opposite", "gathered", "phrase")
SRC = "researcher 2026-11-13 (#2491): long tail of step 2"
OTHER = "OTHER"

MOVE_LINES = """
care: cautious
thought: musing opinion reasoned reasoning
OTHER: gather gathered lacked promote adorned answers appeared beat exceeding invites manifest read reads multiply own like goes shows way well caused character come see appear excellencies nature lack holding joined sit collect enclose ever-flowing measure surpasses dim go leanness aroma refined spiritual condition cause lose loses falling feel set reserved rotten vision doing intimate fleeting lifetime look looking trying breathe breathes practiced cannot causes standing alone burst looked looks defer get bound considering likeness inspire showing held marked performed possible deeply deeper thoroughly long lengthen felt saw contrary render rendered throw throws cast casts thrust thrusting press pressed adornment fitting receive received receives send sent settle
gladden: merry-hearted dance
compassion: softened touched
forgive: excused reconcile reconciled reconciliation reconciling atone atoned atonement atoning
promise: swear swore sworn
endure: burden
guard: enclosed
united: join fellowship
search: revenge
entice: ensnare
compel: insisting
intend: meant purpose purposed purposes
submission: yield surrendered obeyed obedient
willful: unwilling
doubt: double
dedicate: resolved
folly: senseless
pain: grief griefs sadness bitter
chide: chastisement
wise: judgment discern discerned discerning discernment discretion distinguish intelligence intelligent perceive perceives perceiving reasonableness understand understanding understands understood
plot: designs design
quarrel: brawler
righteous: virtue
fear: anxious shake foreboding
crime: violated violates
quarrel: rivalry
jealous: rivalry
condemn: accused blame convicts guilt accuse
save: helped recovered restoring heal healing
rich: flourish
combat: besiege besieged
lament: forlorn
mute: repose rested rests
know: realizes interpret
anger: displeased unappeasable fierce displeasing impatient hostile provocation
evildoer: depraved
share: grant bestow endow endowed
supplication: invoke
supply: nourishes
choose: determine
impartial: justice
tribulation: overwhelmed overwhelms troubling
self-control: abstain refrained stop stopped
disease: health
benefit: profit
love: embrace embraces
cruel: severe severity
conceal: secret secrets
unclean: blemished
sin: errors
adultery: whoredom
justify: acquittal
repent: regret relent relented relenting relents
comfort: relief
bondage: slavery
count: credit
honor: worthily worthy
fulfill: finished
desire: longed longs
trust: leaned leans
"""
KEEP_LEFT = ""   # words not listed are not touched
MERGES = [  # (kept, combined)
    ("honor", "blush"), ("fulfill", "content"), ("evildoer", "degenerate"), ("reward", "deserts"), ("reward", "pay"), ("reward", "repay"),
    ("quarrel", "discord"), ("doubt", "double-minded"), ("skill", "master"), ("shatter", "tear"), ("adultery", "whoring"), ("compel", "duty"),
    ("mighty", "might"), ("roar", "aloud"), ("open", "shut"), ("gladden", "feast"), ("command", "charge"), ("count", "account"), ("comfort", "console"),
    ("plot", "conspire"), ("destruction", "consume"), ("teach", "counsel"), ("deceive", "crafty"), ("lament", "sigh"), ("fill", "empty"),
    ("impartial", "equity"), ("impartial", "partial"), ("thought", "imagine"), ("thought", "meditate"), ("love", "kiss"), ("love", "precious"),
    ("serve", "minister"), ("refresh", "new"), ("oppress", "persecute"), ("preach", "prophesy"), ("fear", "tremble"), ("know", "realize"), ("know", "study"),
    ("believe", "religion"), ("save", "rescue"), ("desire", "sensual"), ("self-control", "sober"), ("disease", "sound"), ("mute", "still"),
    ("guard", "stronghold"), ("stumble", "failing"), ("submission", "subject"), ("faint", "weary"), ("rebel", "wayward"),
]
RETIRE = ["contrary", "render", "throw", "thrust", "press", "send", "long"]
OPPOSITE_TIER = {"blush", "shut", "close", "closed", "fastened"}
WHY_OTHER = "a generic word (motion, place, time, measure or plain action), not a behaviour or an inner-being state (researcher 2026-11-13, #2491 long tail of step 2)"
MOVE = {}
for line in MOVE_LINES.strip().splitlines():
    tgt, ws = line.split(":", 1)
    for w in ws.split():
        if w in MOVE and MOVE[w] != tgt.strip():
            if tgt.strip() == "jealous":
                continue   # rivalry: jealous (the quarrel line is overruled by it)
            if MOVE[w] == "jealous":
                MOVE[w] = tgt.strip()
            else:
                raise SystemExit("word ruled twice: %s (%s, %s)" % (w, MOVE[w], tgt))
        MOVE[w] = tgt.strip()
MOVE["rivalry"] = "jealous"
PHRASE_LINES = """
save: deliver me; delivered my life
desire: long for; longed for
abase: cast down; casts down
scoff: cast contempt
reject: cast off
wait: delay long
OTHER: pressed out; sent him away
"""
for line in PHRASE_LINES.strip().splitlines():
    tgt, ps = line.split(":", 1)
    for p in ps.split(";"):
        MOVE[p.strip()] = tgt.strip()


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
    done_names = {r["name"] for r in q("SELECT name FROM collection WHERE deleted=0 AND status IN ('merged','retired')")}
    need = {t for t in MOVE.values() if t != OTHER} | {k for k, _ in MERGES} | {c for _, c in MERGES} | set(RETIRE)
    missing = sorted(n for n in need if n not in cname and n not in done_names)
    if missing:
        raise Stop("collections not found: %s" % missing)
    terms = {r["id"]: r for r in q("SELECT id, surface, base_id, surface_group FROM surface_term WHERE deleted=0")}
    ids_of = collections.defaultdict(list)
    for t, r in terms.items():
        ids_of[r["surface"]].append(t)
    cache = {}

    def live_links(col):
        if col not in cache:
            cache[col] = q("SELECT * FROM collection_link WHERE collection_id=? AND deleted=0", col)
        return cache[col]

    def own_member_links(tid):
        return q("SELECT l.* FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.term_id=? AND l.deleted=0 AND c.deleted=0 "
                 "AND c.status IN ('indicative','confirmed') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), tid, *MEMBER)
    actions, pending, planned = [], {}, set()

    def tier_of(col, t):
        if (col, t) in pending:
            return pending[(col, t)]
        for l in live_links(col):
            if l["term_id"] == t and l["id"] not in planned:
                return l["tier"]
        return None

    def plan_drop(l, why):
        if l["id"] not in planned:
            planned.add(l["id"]); actions.append(("drop", l["id"], why))

    def plan_move(l, to, why, tier):
        if l["id"] in planned or l["collection_id"] == to:
            return
        t = l["term_id"]
        have = tier_of(to, t)
        planned.add(l["id"])
        if have is None:
            actions.append(("move", l["id"], to, t, tier, why)); pending[(to, t)] = tier
        elif RANK.index(tier) < RANK.index(have):
            actions.append(("upgrade", l["id"], to, t, tier, why)); pending[(to, t)] = tier
        else:
            actions.append(("drop", l["id"], why + " (the collection already holds it)"))

    absent, regroup, regroup_ids = [], [], set()
    # 1. words
    for w, tgt in sorted(MOVE.items()):
        rows = ids_of.get(w, [])
        links = [l for t in rows for l in own_member_links(t)]
        if not rows or (not links and tgt != OTHER):
            absent.append(w); continue
        for t in rows:
            if tgt == OTHER:
                regroup_ids.add(t)
                if terms[t]["surface_group"] != "other":
                    regroup.append((t, w, terms[t]["surface_group"]))
        for l in links:
            if tgt == OTHER:
                plan_drop(l, "the word %s is regrouped to other: %s" % (w, WHY_OTHER))
            else:
                plan_move(l, cname[tgt] if tgt in cname else None, "%s does not belong where it was: it goes to %s (long tail)" % (w, tgt), "phrase" if " " in w else "synonym")
    # 2. whole collections
    to_mark = []
    for kept, x in MERGES:
        if x not in cname or kept not in cname:
            continue
        for l in live_links(cname[x]):
            s = terms[l["term_id"]]["surface"] if l["term_id"] in terms else ""
            tier = "opposite" if (s in OPPOSITE_TIER and l["tier"] in ("core", "synonym", "opposite")) else ("synonym" if l["tier"] == "core" else l["tier"])
            plan_move(l, cname[kept], "combined %s into %s: like-minded, small (long tail)" % (x, kept), tier)
        to_mark.append((cname[x], "merged", cname[kept], "combined into %s (long tail)" % kept))
    for n in RETIRE:
        if n in cname:
            to_mark.append((cname[n], "retired", None, "dissolved: its members are generic words, regrouped or placed (long tail)"))
            for l in live_links(cname[n]):
                plan_drop(l, "the %s collection is dissolved" % n)

    def covered_set():
        o = {r[0] for r in q("SELECT DISTINCT l.term_id FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 "
                             "AND c.status IN ('indicative','confirmed') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER)}
        out = set(o)
        for r in q("SELECT id, base_id FROM surface_term WHERE deleted=0"):
            if r["id"] in o or (r["base_id"] and r["base_id"] in o):
                out.add(r["id"])
        return out
    covered_before = covered_set()
    allowed = set(regroup_ids)
    for t, r in terms.items():
        if r["base_id"] in regroup_ids:
            allowed.add(t)
    kinds = collections.Counter(a_[0] for a_ in actions)
    live_before = one("SELECT count(*) FROM collection_link WHERE deleted=0")
    to_mark = [m for m in to_mark if one("SELECT status FROM collection WHERE id=?", m[0]) not in ("merged", "retired")]
    pred = dict(actions=dict(kinds), collections_marked=len(to_mark), regrouped=len(regroup),
                live_links_after=live_before + kinds["move"] + kinds["upgrade"] - kinds["move"] - 2 * kinds["upgrade"] - kinds["drop"])
    print("predicted:", pred, "| words ruled:", len(MOVE), "| not found as a member:", absent)
    if not actions and not to_mark and not regroup:
        print("nothing to do (already applied)")
        return 0
    marked_before = one("SELECT count(*) FROM collection WHERE deleted=0 AND status IN ('merged','retired') AND run_id=?", RUN_ID)
    regrouped_before = one("SELECT count(*) FROM surface_event WHERE run_id=? AND action='set_group'", RUN_ID)
    conn.execute("SAVEPOINT w")
    try:
        now_sql = "strftime('%Y-%m-%dT%H:%M:%SZ','now')"
        touched = set()

        def ev(subject, sid, action, before, after, reason, field=None):
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                         "VALUES (?,?,?,?,?,?,?,?,?,?)", (subject, sid, action, field, before, after, "Claude", "%s (%s)" % (reason, SRC), RUN_ID, WHO))

        killed = collections.Counter()

        def kill(old, new):
            killed[old] += 1
            conn.execute("UPDATE collection_link SET deleted=1, superseded_by_id=?, updated_at=" + now_sql + ", run_id=? WHERE id=?", (new, RUN_ID, old))

        def new_link(col, t, tier, why):
            return conn.execute("INSERT INTO collection_link (collection_id, term_id, tier, superseded_by_id, shared, reason, run_id, created_by) VALUES (?,?,?,NULL,0,?,?,?)",
                                (col, t, tier, why, RUN_ID, WHO)).lastrowid
        for act in actions:
            if act[0] == "drop":
                _, old, why = act
                oc, t = conn.execute("SELECT collection_id, term_id FROM collection_link WHERE id=?", (old,)).fetchone()
                kill(old, None); ev("collection_link", old, "remove", cid_name.get(oc), None, why, "collection_id"); touched.add(t)
            else:
                _, old, to, t, tier, why = act
                oc = one("SELECT collection_id FROM collection_link WHERE id=?", old)
                if act[0] == "upgrade":
                    cur = conn.execute("SELECT id FROM collection_link WHERE collection_id=? AND term_id=? AND deleted=0", (to, t)).fetchone()
                    if cur:
                        kill(cur[0], None)
                        nl = new_link(to, t, tier, why)
                        conn.execute("UPDATE collection_link SET superseded_by_id=? WHERE id=?", (nl, cur[0]))
                        ev("collection_link", nl, "set_tier", str(cur[0]), str(nl), why, "collection_id")
                        kill(old, nl); ev("collection_link", old, "move", cid_name.get(oc), cid_name.get(to), why, "collection_id"); touched.add(t); continue
                kill(old, None)
                nl = new_link(to, t, tier, why)
                conn.execute("UPDATE collection_link SET superseded_by_id=? WHERE id=?", (nl, old))
                ev("collection_link", nl, "move", cid_name.get(oc), cid_name.get(to), why, "collection_id"); touched.add(t)
        for cid, status, into, why in to_mark:
            conn.execute("UPDATE collection SET status=?, merged_into_id=?, updated_at=" + now_sql + ", run_id=? WHERE id=?", (status, into, RUN_ID, cid))
            ev("collection", cid, "merge" if status == "merged" else "retire", None, cid_name.get(into) if into else None, why)
        for t, w, before in regroup:
            conn.execute("UPDATE surface_term SET surface_group='other', group_state='corrected', group_judged_by='Claude (researcher direction, #2491)', group_reason=?, "
                         "updated_at=" + now_sql + ", run_id=? WHERE id=?", (WHY_OTHER, RUN_ID, t))
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) VALUES "
                         "('surface_term',?,'set_group','surface_group',?,'other','Claude',?,?,?)", (t, before, WHY_OTHER + " (" + SRC + ")", RUN_ID, WHO))
            touched.add(t)
        derived = set()
        for t in list(touched):
            derived |= {r[0] for r in q("SELECT id FROM surface_term WHERE deleted=0 AND base_id=?", t)}
        for t in touched | derived:
            ls = q("SELECT l.collection_id, l.tier FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.term_id=? AND l.deleted=0 AND c.status IN ('indicative','confirmed')", t)
            strong = {r["collection_id"] for r in ls if r["tier"] in ("core", "synonym", "opposite")}
            st = "shared" if len(strong) > 1 else ("placed" if any(r["tier"] in MEMBER for r in ls) else ("listed_only" if ls else "untouched"))
            conn.execute("UPDATE surface_term SET collection_state=? WHERE id=? AND COALESCE(collection_state,'~')<>?", (st, t, st))
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
        changed, bad_nodes = 0, 0
        for n in q("SELECT id, observation_id, collection_id, lower(trim(surface)) AS s FROM ib_node WHERE deleted=0 AND surface IS NOT NULL AND trim(surface)<>''"):
            cs = carry(n["s"])
            new = next(iter(cs)) if len(cs) == 1 else None
            if new != n["collection_id"]:
                orec.log(conn, n["observation_id"], n["id"], "collection_id", n["collection_id"], new,
                         "the collections were read as a whole, small ones combined and misplaced words moved (researcher 2026-11-13, #2491 long tail); the node carries the one collection of its surface by the own-row rule, or none", None, RUN_ID, "Claude")
                conn.execute("UPDATE ib_node SET collection_id=? WHERE id=?", (new, n["id"])); changed += 1
        for n in q("SELECT collection_id, lower(trim(surface)) AS s FROM ib_node WHERE deleted=0 AND surface IS NOT NULL AND trim(surface)<>''"):
            cs = carry(n["s"])
            if (len(cs) == 1 and n["collection_id"] not in cs) or (len(cs) != 1 and n["collection_id"] is not None):
                bad_nodes += 1
        got = dict(collections_marked=one("SELECT count(*) FROM collection WHERE deleted=0 AND status IN ('merged','retired') AND run_id=?", RUN_ID) - marked_before,
                   regrouped=one("SELECT count(*) FROM surface_event WHERE run_id=? AND action='set_group'", RUN_ID) - regrouped_before,
                   live_links_after=one("SELECT count(*) FROM collection_link WHERE deleted=0"))
        print("actual:   ", got, "| nodes changed:", changed, "| nodes not matching the own-row rule:", bad_nodes,
              "| links made live this run:", one("SELECT count(*) FROM collection_link WHERE run_id=? AND deleted=0", RUN_ID),
              "| links deleted this run:", one("SELECT count(*) FROM collection_link WHERE run_id=? AND deleted=1", RUN_ID),
              "| predicted made/deleted:", kinds["move"] + kinds["upgrade"], kinds["move"] + 2 * kinds["upgrade"] + kinds["drop"])
        twice = [(i, conn.execute("SELECT c.name, t.surface, l.tier FROM collection_link l JOIN collection c ON c.id=l.collection_id JOIN surface_term t ON t.id=l.term_id WHERE l.id=?", (i,)).fetchone()[:] ) for i, n_ in killed.items() if n_ > 1]
        print("links set deleted twice by the plan:", [(i, tuple(r)) for i, r in twice])
        bad = [k for k in ("collections_marked", "regrouped", "live_links_after") if got[k] != pred[k]]
        stranded = one("SELECT count(*) FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.status IN ('merged','retired') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER)
        lost = sorted(terms[t]["surface"] for t in covered_before - covered_set() if t in terms and t not in allowed)
        multi = sorted({terms[t]["surface"] for t, cs in cols_now.items() if len(cs) > 1 and t in terms})
        print("member links on a merged or retired collection:", stranded, "| surfaces losing coverage (not regrouped):", len(lost), lost[:60],
              "| surfaces in two or more collections:", len(multi), multi[:40])
        if bad or stranded or lost or multi or bad_nodes:
            raise Stop("actual differs from predicted (%s), links stranded, coverage lost, a surface in two collections or a node not matching: rolled back" % bad)
        if a.dry_run:
            conn.execute("ROLLBACK TO w"); print("dry run: rolled back")
        else:
            conn.execute("RELEASE w"); conn.commit(); print("committed")
    except Exception:
        conn.execute("ROLLBACK TO w"); conn.commit(); raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
