"""collection_merge_batch2_2491_v1_20261112.py -- escalation #2491, plan v3 step 2, second batch.

Researcher, 2026-11-13: 'Yes, apply them' (sections A and B of _analytics/surfaces/exports/collection-merge-proposals-batch2-v1-20261112.md).
Sections C and D (medium-confidence matters, regroups) are NOT applied here.
Every change is a rule of that file, written as explicit lists so it can be read:
  PRE_DROPS   a named link is set deleted because another collection holds the word (section B: a word sits once; an opposite entry that is a
              member of the paired collection comes off), and the opposites of defile, the command/seize words of compel and the command words of govern.
  TERM_MOVES  named terms move from one collection to another before any whole combination (the placing of the words of flee, dread and dreaded
              from doom, the words of saying, ask and majesty that belong elsewhere). Where the target already holds the word the link is dropped;
              where it holds it in a weaker tier it is upgraded.
  MERGES      a collection is combined into another: each live link of the combined collection (every tier) moves to the kept collection (a new live
              link, the old one set deleted with superseded_by_id), the core of the combined collection becomes a synonym; where the kept collection
              already holds the term the stronger tier is kept. The combined collection gets status merged and merged_into_id.
Then: surface_term.collection_state for every touched term, and ib_node.collection_id for the nodes whose surface changed or that pointed at a
combined collection (the exactly-one rule). A coverage check (a surface covered before is covered after, own row or base) and a stranded-link
check stop the run. Every change is kept: surface_event for each link and collection, ib_observation_change for each node. Nothing is physically
deleted. The run rolls back unless the counts equal the prediction. Idempotent.
    python -m iba.app.migration.collection_merge_batch2_2491_v1_20261112 [--db PATH] [--dry-run]   (run from the project root)
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
RUN_ID = "DEVMODE-2491-COLLECTION-BATCH2-20261112"
WHO = "devmode-2491"
RANK = ["core", "synonym", "opposite", "gathered", "phrase", "associated", "possible_opposite", "set_aside"]
MEMBER = ("core", "synonym", "opposite", "gathered", "phrase")
SRC = "researcher 2026-11-13 (#2491): proposals file batch 2, sections A and B"

# (collection, [terms], tiers or None for any, reason)
PRE_DROPS = [
    ("whisper", ["murmured", "murmur"], None, "murmur words stay in mutter (grumbling)"),
    ("mutter", ["whisper"], None, "whisper stays in whisper"),
    ("mutter", ["uttered"], None, "uttered goes to aloud"),
    ("mutter", ["silent", "silence"], ("opposite",), "an opposite sits once: mute holds silence and silent"),
    ("aloud", ["quiet", "silent"], ("opposite",), "an opposite sits once: mute holds quiet and silent"),
    ("cleanse", ["remove", "removing"], None, "remove holds them"),
    ("remove", ["purge"], None, "cleanse holds purge"),
    ("cleanse", ["defile", "impure"], ("opposite",), "an opposite sits once: unclean holds defile and impure"),
    ("righteous", ["fair"], None, "fair stays in impartial"),
    ("impartial", ["just"], None, "just stays in righteous"),
    ("righteous", ["evil", "sinful", "unrighteous", "wicked"], ("opposite",), "an opposite sits once: evildoer holds them"),
    ("evildoer", ["righteous", "upright"], ("opposite",), "an opposite sits once: righteous holds them"),
    ("godly", ["sinful", "wicked"], ("opposite",), "an opposite sits once: evildoer holds them"),
    ("cruel", ["evil", "malicious", "vile"], None, "evildoer holds them"),
    ("cruel", ["detestable", "dreadful", "loathsome"], None, "abominable holds them"),
    ("cruel", ["torment", "tormenting"], None, "persecute holds them"),
    ("cruel", ["kind", "kindly", "kindness"], ("opposite",), "an opposite sits once: tenderhearted holds them"),
    ("command", ["instruct", "instructed", "instruction", "instructs"], None, "teach holds them"),
    ("quarrel", ["fight"], None, "fight goes to combat"),
    ("combat", ["conflict", "peace"], None, "conflict goes to quarrel; the opposite peace stays in quarrel"),
    ("increase", ["strengthen", "strengthened", "strengthening"], None, "strengthen holds them"),
    ("repay", ["return"], None, "return stays in return"),
    ("majesty", ["mighty"], None, "mighty stays in mighty"),
    ("mighty", ["majestic"], None, "majestic is glory: majesty holds it"),
    ("govern", ["command", "direct"], MEMBER, "command and direct stay in command (a non-member association stays)"),
    ("defile", ["clean", "pure", "purify"], ("opposite",), "the opposites of defile come off: unclean and cleanse hold them"),
    ("compel", ["command", "commanded"], MEMBER, "command holds them (a non-member association stays)"),
    ("compel", ["seize"], None, "seize is held by snatch"),
]
# (to, from, [terms], tier, reason)
TERM_MOVES = [
    ("fear", "doom", ["dread", "dreaded"], "synonym", "dread and dreaded are fright, held by fear"),
    ("preach", "saying", ["proclaim", "proclaiming", "proclaims", "proclaimed"], "synonym", "the proclaim words are preaching"),
    ("supplication", "ask", ["entreat", "request", "requesting"], "synonym", "entreat and request are supplication"),
    ("chief", "majesty", ["authority", "supreme", "kingly", "exalt", "exalted", "exaltation"], "synonym", "authority and exaltation are chief, not glory"),
    ("depart", "flee", ["depart", "leave", "going"], "synonym", "leaving is depart, not flight"),
    ("forsake", "flee", ["abandon"], "synonym", "abandon is forsake"),
    ("hear", "flee", ["deaf"], "opposite", "deaf is the opposite of hear"),
    ("endure", "flee", ["remain", "stay", "settled", "settles", "lodges"], "synonym", "remaining is endure (abide, remain)"),
]
MERGES = [  # (kept, [combined...], reason)
    ("change", ["amend"], "change and reform: one concept"),
    ("offer", ["deal"], "deal and agreement: gift and offering"),
    ("destruction", ["doom"], "doom and ruin: destruction"),
    ("dedicate", ["ordain"], "setting apart: consecrate, appointed"),
    ("govern", ["reign"], "ruling: reign and rule"),
    ("unclean", ["filth", "defile"], "the state of uncleanness and defilement"),
    ("compel", ["require"], "compulsion and demand"),
    ("persecute", ["harass"], "oppression and persecution"),
    ("scoff", ["insult"], "contempt and ridicule: contempt shown"),
    ("escape", ["flee"], "flight and escape"),
]


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
    merged_names = {r["name"] for r in q("SELECT name FROM collection WHERE deleted=0 AND status IN ('merged','retired')")}
    text_of = {r["id"]: r["surface"] for r in q("SELECT id, surface FROM surface_term WHERE deleted=0")}
    need = {k for k, _, _ in MERGES} | {c for _, xs, _ in MERGES for c in xs} | {c for c, _, _, _ in PRE_DROPS} | {t for t, _, _, _, _ in TERM_MOVES} | {f for _, f, _, _, _ in TERM_MOVES}
    missing = sorted(n for n in need if n not in cname and n not in merged_names)
    if missing:
        raise Stop("collections not found: %s" % missing)

    cache = {}

    def live_links(col):
        if col not in cache:
            cache[col] = q("SELECT * FROM collection_link WHERE collection_id=? AND deleted=0", col)
        return cache[col]

    def find(col, s, tiers=None):
        return [l for l in live_links(col) if text_of.get(l["term_id"]) == s and (tiers is None or l["tier"] in tiers)]

    actions = []
    pending_ins = {}
    drops_planned = set()

    def tier_of(col, t):
        if (col, t) in pending_ins:
            return pending_ins[(col, t)]
        for l in live_links(col):
            if l["term_id"] == t and l["id"] not in drops_planned:
                return l["tier"]
        return None

    def plan_drop(link, reason):
        if link["id"] in drops_planned:
            return
        drops_planned.add(link["id"]); actions.append(("drop", link["id"], reason))

    def plan_move(src_link, to_col, reason, tier=None):
        if src_link["id"] in drops_planned:
            return
        t = src_link["term_id"]
        tr = tier or src_link["tier"]
        have = tier_of(to_col, t)
        drops_planned.add(src_link["id"])
        if have is None:
            actions.append(("move", src_link["id"], to_col, t, tr, reason)); pending_ins[(to_col, t)] = tr
        elif RANK.index(tr) < RANK.index(have):
            actions.append(("upgrade", src_link["id"], to_col, t, tr, reason)); pending_ins[(to_col, t)] = tr
        else:
            actions.append(("drop", src_link["id"], reason + " (the kept collection already holds it)"))

    for col, ts, tiers, why in PRE_DROPS:
        if col in cname:
            for s in ts:
                for l in find(cname[col], s, tiers):
                    plan_drop(l, "%s: %s" % (col, why))
    for to, fr, ts, tier, why in TERM_MOVES:
        if fr in cname and to in cname:
            for s in ts:
                for l in find(cname[fr], s):
                    plan_move(l, cname[to], "%s to %s: %s" % (fr, to, why), tier)
    collections_to_mark = []
    for kept, xs, why in MERGES:
        if kept not in cname:
            continue
        for x in xs:
            if x not in cname:
                continue
            for l in live_links(cname[x]):
                tier = "synonym" if l["tier"] == "core" else l["tier"]
                plan_move(l, cname[kept], "combined %s into %s: %s" % (x, kept, why), tier)
            collections_to_mark.append((cname[x], "merged", kept, "combined into %s: %s" % (kept, why)))

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
    live_links_before = one("SELECT count(*) FROM collection_link WHERE deleted=0")
    to_mark = [m for m in collections_to_mark if one("SELECT status FROM collection WHERE id=?", m[0]) not in ("merged", "retired")]
    n_ins = kinds["move"] + kinds["upgrade"]
    n_del = kinds["move"] + 2 * kinds["upgrade"] + kinds["drop"]
    pred = dict(actions=dict(kinds), collections_marked=len(to_mark), live_links_after=live_links_before + n_ins - n_del)
    print("predicted:", pred)
    if len(actions) < 12:
        for act in actions:
            print("  action:", act)
    marked_before = one("SELECT count(*) FROM collection WHERE deleted=0 AND status IN ('merged','retired') AND run_id=?", RUN_ID)
    if not actions and not to_mark:
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

        def new_link(col, t, tier, reason):
            cur = conn.execute("INSERT INTO collection_link (collection_id, term_id, tier, superseded_by_id, shared, reason, run_id, created_by) VALUES (?,?,?,NULL,0,?,?,?)",
                               (col, t, tier, reason, RUN_ID, WHO))
            return cur.lastrowid

        def kill(old_id, new_id):
            conn.execute("UPDATE collection_link SET deleted=1, superseded_by_id=?, updated_at=" + now_sql + ", run_id=? WHERE id=?", (new_id, RUN_ID, old_id))

        for act in actions:
            if act[0] in ("move", "upgrade"):
                _, old, to_col, t, tier, reason = act
                oc = one("SELECT collection_id FROM collection_link WHERE id=?", old)
                if act[0] == "upgrade":
                    cur = conn.execute("SELECT id FROM collection_link WHERE collection_id=? AND term_id=? AND deleted=0", (to_col, t)).fetchone()
                    if cur:
                        kill(cur[0], None)
                        nl = new_link(to_col, t, tier, reason)
                        conn.execute("UPDATE collection_link SET superseded_by_id=? WHERE id=?", (nl, cur[0]))
                        ev("collection_link", nl, "set_tier", str(cur[0]), str(nl), reason)
                        kill(old, nl); ev("collection_link", old, "move", cid_name.get(oc), cid_name.get(to_col), reason)
                        touched_terms.add(t); continue
                nl = new_link(to_col, t, tier, reason)
                kill(old, nl); ev("collection_link", nl, "move", cid_name.get(oc), cid_name.get(to_col), reason); touched_terms.add(t)
            elif act[0] == "drop":
                _, old, reason = act
                oc, t = conn.execute("SELECT collection_id, term_id FROM collection_link WHERE id=?", (old,)).fetchone()
                kill(old, None); ev("collection_link", old, "remove", cid_name.get(oc), None, reason); touched_terms.add(t)
        for cid, status, into_name, reason in to_mark:
            into = cname.get(into_name)
            if into is None:
                raise Stop("merge target %r not found" % into_name)
            conn.execute("UPDATE collection SET status=?, merged_into_id=?, updated_at=" + now_sql + ", run_id=? WHERE id=?", (status, into, RUN_ID, cid))
            ev("collection", cid, "merge", None, into_name, reason)
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
        ids = touched_terms | derived
        surf_touched = {r["surface"] for r in q("SELECT surface FROM surface_term WHERE id IN (%s)" % ",".join(str(x) for x in ids or {0}))}
        changed_nodes = 0
        for n in q("SELECT id, observation_id, collection_id, lower(trim(surface)) AS s FROM ib_node WHERE deleted=0 AND surface IS NOT NULL AND trim(surface)<>''"):
            if n["s"] in surf_touched or n["collection_id"] in retired_ids:
                cs = carry(n["s"])
                new = next(iter(cs)) if len(cs) == 1 else None
                if new != n["collection_id"]:
                    orec.log(conn, n["observation_id"], n["id"], "collection_id", n["collection_id"], new,
                             "the collections were combined and sorted (researcher 2026-11-13, #2491); the node carries the one collection of its surface, or none where it has none or several", None, RUN_ID, "Claude")
                    conn.execute("UPDATE ib_node SET collection_id=? WHERE id=?", (new, n["id"])); changed_nodes += 1
        got = dict(collections_marked=one("SELECT count(*) FROM collection WHERE deleted=0 AND status IN ('merged','retired') AND run_id=?", RUN_ID) - marked_before,
                   live_links_after=one("SELECT count(*) FROM collection_link WHERE deleted=0"))
        print("actual:   ", got, "| nodes whose collection changed:", changed_nodes)
        bad = [k for k in ("collections_marked", "live_links_after") if got[k] != pred[k]]
        stranded = conn.execute(
            "SELECT count(*) FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.status IN ('merged','retired') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), MEMBER).fetchone()[0]
        lost = sorted(text_of[t] for t in covered_before - covered_set() if t in text_of)
        print("member links still on a merged or retired collection:", stranded)
        print("surfaces covered before and not after:", len(lost), lost[:60])
        if bad or stranded or lost:
            raise Stop("actual differs from predicted (%s), links stranded or coverage lost: rolled back" % bad)
        if a.dry_run:
            conn.execute("ROLLBACK TO w"); print("dry run: rolled back")
        else:
            conn.execute("RELEASE w"); conn.commit(); print("committed")
    except Exception:
        conn.execute("ROLLBACK TO w"); conn.commit(); raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
