"""collection_regroup_step0_2491_v1_20261113.py -- escalation #2491, plan v3 step 0 and section D of the batch 2 file.

Researcher, 2026-11-13: 'Yes, both' (remove the computed words that are in no verse; go on to step 0 and section D).
Rule of the researcher (#2491 v12): a word that is neither a behaviour nor an inner-being state is not a surface of a collection. The words below
were read by meaning (not by a script) and every ruling is inferential (B:4). Explicit lists, so each can be read:
  REGROUP   surfaces whose group becomes other (surface_group other, group_state corrected, reason kept); every member link of the surface is
            set deleted.
  PLACE     a word is placed in the one collection named (section D): its links in the named collections move there, or it is added where it has
            no link of its own; a link in a retired collection is simply set deleted.
  DROPS     a named link is set deleted because the word sits in another collection.
  RETIRE    a collection is dissolved: its remaining links are set deleted and its status becomes retired. Every member is regrouped or placed
            elsewhere (checked: no surface other than the regrouped ones and their derived forms may lose its collection).
  COMPUTED  the computed base words that are in no verse (deem, foreknow, infirmity, qualify, reckon, regenerate, transfigure): their link in
            the gathered collection uncovered-words is set deleted (researcher 2026-11-12: surfaces without verses are removed from the lists).
            The base rows stay: they are the base of real surfaces (deemed, foreknew, ...). guarantee, respond and treat have verses and stay.
Link changes follow the convention of entries 498 and 499 (a new live link, the old one deleted with superseded_by_id; nothing physically
deleted). Then: surface_term.collection_state and ib_node.collection_id (the exactly-one rule) for what changed. Stops and rolls back unless
predicted equals actual and nothing outside the regrouped words loses its collection. Idempotent.
    python -m iba.app.migration.collection_regroup_step0_2491_v1_20261113 [--db PATH] [--dry-run]   (from the project root)
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
RUN_ID = "DEVMODE-2491-REGROUP-STEP0-20261113"
WHO = "devmode-2491"
RANK = ["core", "synonym", "opposite", "gathered", "phrase", "associated", "possible_opposite", "set_aside"]
MEMBER = ("core", "synonym", "opposite", "gathered", "phrase")
SRC = "researcher 2026-11-13 (#2491): step 0 and section D"

REGROUP = [  # (words, reason)
    ("good great greater greatly excellent excelled exceedingly wonderful delightful better".split(),
     "an evaluative word or intensifier, not a behaviour or an inner-being state"),
    (["ashes"], "a noun (the material), not a behaviour or an inner-being state"),
    ("become became becomes becoming cultivate grow grew".split(), "a copula or a plain change-of-quantity word, not an act or a state"),
    ("bring brought carry carried carrying move".split(),
     "a plain motion word (carry is physical in the verses; bearing a burden is endure)"),
    ("say said says saying sayings spoke speaks speak speaking spoken talk talked talking telling tell show showed shown".split(),
     "a plain speech or display verb, not a behaviour of the inner being"),
    ("increase increased more multiplied diminish rise higher".split(), "a quantity word, not a behaviour or an inner-being state"),
    ("grown risen tells told".split(), "a derived form of a regrouped word (grow, rise, tell): follows its base"),
    ("make made makes making".split(), "a generic making verb, not a behaviour or an inner-being state"),
    (["please"], "in most verses a polite request particle (Gen 44:18); the pleasing sense is carried by pleased, pleasing, pleases and favors"),
    (["ever", "within", "length", "span", "large", "small", "enlarged"], "a word of time, place or measure, not a behaviour or an inner-being state"),
]
PLACE = [  # (surface, to, tier, [collections it leaves]) -- the retired collections need not be named
    ("pleased", "delight", "synonym", []), ("pleases", "delight", "synonym", []), ("pleasing", "delight", "synonym", ["please", "beauty"]),
    ("favors", "delight", "synonym", ["please"]), ("implore", "supplication", "synonym", ["please"]), ("request", "supplication", "synonym", ["please"]),
    ("glorious", "majesty", "synonym", ["great", "excellent"]), ("greatness", "majesty", "synonym", ["great"]), ("majestic", "majesty", "synonym", ["great"]),
    ("exalted", "chief", "synonym", ["great", "mighty"]), ("mighty", "mighty", "core", ["great"]),
    ("marvelous", "amazement", "synonym", ["great", "excellent", "delight"]),
    ("perfect", "righteous", "synonym", ["great", "excellent", "partial"]), ("faultless", "innocent", "synonym", ["excellent"]),
    ("resolve", "dedicate", "synonym", ["excellent"]), ("untroubled", "fear", "opposite", ["excellent"]), ("esteemed", "honor", "synonym", ["excellent", "renown"]),
    ("wandered", "astray", "synonym", ["become"]), ("change", "change", "synonym", ["become"]), ("transform", "change", "synonym", ["become"]),
    ("turn", "turn", "core", ["become"]),
    ("answer", "profess", "synonym", ["saying"]), ("replied", "profess", "synonym", ["saying"]), ("answered", "profess", "synonym", ["teach"]),
    ("raise", "abase", "opposite", ["increase"]), ("raised", "abase", "opposite", ["increase"]), ("raises", "abase", "opposite", ["increase"]),
    ("lifts", "abase", "opposite", ["increase"]), ("nourishes", "care", "synonym", ["increase"]), ("contribute", "share", "synonym", ["increase"]),
    ("enlarge", "magnify", "synonym", ["increase"]), ("gain", "benefit", "synonym", ["increase"]),
    ("deliver", "rescued", "synonym", ["bring", "send"]), ("prepare", "build", "synonym", ["make"]), ("produce", "build", "synonym", ["make"]),
    ("build", "build", "core", ["make"]),
    ("pleased to", "delight", "phrase", ["please"]), ("pleasing sacrifices", "delight", "phrase", ["please"]),
    ("pleasing to", "delight", "phrase", ["please"]), ("well pleased", "delight", "phrase", ["please"]),
    ("goodness", "tenderhearted", "synonym", ["great", "excellent"]),
]
RETIRE = ["great", "excellent", "become", "bring", "carry", "increase", "saying", "please", "ever", "within", "length", "large", "make", "better"]
COMPUTED = "deem foreknow infirmity qualify reckon regenerate transfigure".split()


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
    retired_names = {r["name"] for r in q("SELECT name FROM collection WHERE deleted=0 AND status IN ('merged','retired')")}
    rows_by_text = collections.defaultdict(list)
    text_of = {}
    for r in q("SELECT id, surface, surface_group FROM surface_term WHERE deleted=0"):
        rows_by_text[r["surface"]].append(r)
        text_of[r["id"]] = r["surface"]
    need = {t for _, t, _, _ in PLACE} | {f for _, _, _, fs in PLACE for f in fs} | set(RETIRE) | {"uncovered-words"}
    missing = sorted(n for n in need if n not in cname and n not in retired_names)
    if missing:
        raise Stop("collections not found: %s" % missing)

    cache = {}

    def live_links(col):
        if col not in cache:
            cache[col] = q("SELECT * FROM collection_link WHERE collection_id=? AND deleted=0", col)
        return cache[col]

    def own_links(tid):
        return q("SELECT l.* FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.term_id=? AND l.deleted=0 AND c.deleted=0 "
                 "AND c.status IN ('indicative','confirmed')", tid)

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

    def plan_move(src, to_col, reason, tier):
        if src["id"] in drops_planned:
            return
        t = src["term_id"]
        have = tier_of(to_col, t)
        drops_planned.add(src["id"])
        if have is None:
            actions.append(("move", src["id"], to_col, t, tier, reason)); pending_ins[(to_col, t)] = tier
        elif RANK.index(tier) < RANK.index(have):
            actions.append(("upgrade", src["id"], to_col, t, tier, reason)); pending_ins[(to_col, t)] = tier
        else:
            actions.append(("drop", src["id"], reason + " (the collection already holds it)"))

    # 1. placements
    for s, to, tier, frm in PLACE:
        if to not in cname:
            continue
        for r in rows_by_text.get(s, []):
            t = r["id"]
            srcs = [l for l in own_links(t) if l["collection_id"] != cname[to] and l["tier"] in MEMBER
                    and (cid_name.get(l["collection_id"]) in frm or cid_name.get(l["collection_id"]) in RETIRE)]
            why = "%s is placed in %s (section D / step 0)" % (s, to)
            for l in srcs:
                plan_move(l, cname[to], why, tier)
            if not srcs and not any(l["tier"] in MEMBER for l in own_links(t)):
                cur = [l for l in live_links(cname[to]) if l["term_id"] == t and l["id"] not in drops_planned]
                if not cur:
                    actions.append(("add", cname[to], t, tier, why)); pending_ins[(cname[to], t)] = tier
                else:   # a non-member association of the target: made a member
                    drops_planned.add(cur[0]["id"]); actions.append(("tier", cur[0]["id"], cname[to], t, tier, why)); pending_ins[(cname[to], t)] = tier
    # 2. regroup
    regroup_terms = []   # (term id, surface, group before, reason)
    regroup_ids = set()
    for words, why in REGROUP:
        for s in words:
            for r in rows_by_text.get(s, []):
                regroup_ids.add(r["id"])
                for l in own_links(r["id"]):
                    if l["tier"] in MEMBER:
                        plan_drop(l, "the surface %s is regrouped to other: %s" % (s, why))
                if r["surface_group"] != "other":
                    regroup_terms.append((r["id"], s, r["surface_group"], why))
    # 3. retire collections
    to_mark = []
    for n in RETIRE:
        if n in cname:
            to_mark.append((cname[n], "retired", None, "dissolved: every member is regrouped or placed elsewhere (step 0, section D)"))
            for l in live_links(cname[n]):
                plan_drop(l, "the %s collection is dissolved" % n)
    # 4. computed words with no verse
    computed_ids = set()
    for s in COMPUTED:
        for r in rows_by_text.get(s, []):
            computed_ids.add(r["id"])
            for l in live_links(cname["uncovered-words"]):
                if l["term_id"] == r["id"]:
                    plan_drop(l, "a computed base with no verse is removed from the lists (researcher 2026-11-12)")

    def covered_set():
        own = {r[0] for r in q("SELECT DISTINCT l.term_id FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 "
                               "AND c.status IN ('indicative','confirmed') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER)}
        out = set(own)
        for r in q("SELECT id, base_id FROM surface_term WHERE deleted=0"):
            if r["id"] in own or (r["base_id"] and r["base_id"] in own):
                out.add(r["id"])
        return out
    covered_before = covered_set()
    allowed = set(regroup_ids) | computed_ids
    for r in q("SELECT id, base_id FROM surface_term WHERE deleted=0"):
        if r["base_id"] in allowed:
            allowed.add(r["id"])

    kinds = collections.Counter(a_[0] for a_ in actions)
    live_before = one("SELECT count(*) FROM collection_link WHERE deleted=0")
    to_mark = [m for m in to_mark if one("SELECT status FROM collection WHERE id=?", m[0]) not in ("merged", "retired")]
    n_ins = kinds["move"] + kinds["upgrade"] + kinds["add"] + kinds["tier"]
    n_del = kinds["move"] + 2 * kinds["upgrade"] + kinds["drop"] + kinds["tier"]
    pred = dict(actions=dict(kinds), collections_retired=len(to_mark), regrouped=len(regroup_terms), live_links_after=live_before + n_ins - n_del)
    print("predicted:", pred)
    if not actions and not to_mark and not regroup_terms:
        print("nothing to do (already applied)")
        return 0
    marked_before = one("SELECT count(*) FROM collection WHERE deleted=0 AND status='retired' AND run_id=?", RUN_ID)
    regrouped_before = one("SELECT count(*) FROM surface_event WHERE run_id=? AND action='set_group'", RUN_ID)
    conn.execute("SAVEPOINT w")
    try:
        now_sql = "strftime('%Y-%m-%dT%H:%M:%SZ','now')"
        touched = set()

        def ev(subject, sid, action, before, after, reason):
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                         "VALUES (?,?,?,?,?,?,?,?,?,?)", (subject, sid, action, "collection_id" if subject == "collection_link" else None, before, after, "Claude",
                                                           "%s (%s)" % (reason, SRC), RUN_ID, WHO))

        def new_link(col, t, tier, reason):
            return conn.execute("INSERT INTO collection_link (collection_id, term_id, tier, superseded_by_id, shared, reason, run_id, created_by) VALUES (?,?,?,NULL,0,?,?,?)",
                                (col, t, tier, reason, RUN_ID, WHO)).lastrowid

        def kill(old_id, new_id):
            conn.execute("UPDATE collection_link SET deleted=1, superseded_by_id=?, updated_at=" + now_sql + ", run_id=? WHERE id=?", (new_id, RUN_ID, old_id))

        for act in actions:
            if act[0] == "add":
                _, col, t, tier, reason = act
                nl = new_link(col, t, tier, reason); ev("collection_link", nl, "add", None, cid_name.get(col), reason); touched.add(t)
            elif act[0] == "tier":
                _, old, col, t, tier, reason = act
                kill(old, None)
                nl = new_link(col, t, tier, reason)
                conn.execute("UPDATE collection_link SET superseded_by_id=? WHERE id=?", (nl, old))
                ev("collection_link", nl, "set_tier", str(old), str(nl), reason); touched.add(t)
            elif act[0] in ("move", "upgrade"):
                _, old, to_col, t, tier, reason = act
                oc = one("SELECT collection_id FROM collection_link WHERE id=?", old)
                if act[0] == "upgrade":
                    cur = conn.execute("SELECT id FROM collection_link WHERE collection_id=? AND term_id=? AND deleted=0", (to_col, t)).fetchone()
                    if cur:
                        kill(cur[0], None)
                        nl = new_link(to_col, t, tier, reason)
                        conn.execute("UPDATE collection_link SET superseded_by_id=? WHERE id=?", (nl, cur[0]))
                        ev("collection_link", nl, "set_tier", str(cur[0]), str(nl), reason)
                        kill(old, nl); ev("collection_link", old, "move", cid_name.get(oc), cid_name.get(to_col), reason); touched.add(t); continue
                nl = new_link(to_col, t, tier, reason)
                kill(old, nl); ev("collection_link", nl, "move", cid_name.get(oc), cid_name.get(to_col), reason); touched.add(t)
            elif act[0] == "drop":
                _, old, reason = act
                oc, t = conn.execute("SELECT collection_id, term_id FROM collection_link WHERE id=?", (old,)).fetchone()
                kill(old, None); ev("collection_link", old, "remove", cid_name.get(oc), None, reason); touched.add(t)
        for cid, status, _, reason in to_mark:
            conn.execute("UPDATE collection SET status=?, merged_into_id=NULL, updated_at=" + now_sql + ", run_id=? WHERE id=?", (status, RUN_ID, cid))
            ev("collection", cid, "retire", None, None, reason)
        for tid, s, before, why in regroup_terms:
            conn.execute("UPDATE surface_term SET surface_group='other', group_state='corrected', group_judged_by='Claude (researcher direction, #2491)', group_reason=?, "
                         "updated_at=" + now_sql + ", run_id=? WHERE id=?", (why, RUN_ID, tid))
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) VALUES "
                         "('surface_term',?,'set_group','surface_group',?,'other','Claude',?,?,?)", (tid, before, why + " (" + SRC + ")", RUN_ID, WHO))
            touched.add(tid)
        derived = set()
        for t in list(touched):
            derived |= {r[0] for r in q("SELECT id FROM surface_term WHERE deleted=0 AND base_id=?", t)}
        for t in touched | derived:
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
        retired_ids = {c[0] for c in to_mark}
        ids = touched | derived
        surf_touched = {r["surface"] for r in q("SELECT surface FROM surface_term WHERE id IN (%s)" % ",".join(str(x) for x in ids or {0}))}
        changed_nodes = 0
        for n in q("SELECT id, observation_id, collection_id, lower(trim(surface)) AS s FROM ib_node WHERE deleted=0 AND surface IS NOT NULL AND trim(surface)<>''"):
            if n["s"] in surf_touched or n["collection_id"] in retired_ids:
                cs = carry(n["s"])
                new = next(iter(cs)) if len(cs) == 1 else None
                if new != n["collection_id"]:
                    orec.log(conn, n["observation_id"], n["id"], "collection_id", n["collection_id"], new,
                             "words were regrouped, placed and collections dissolved (researcher 2026-11-13, #2491); the node carries the one collection of its surface, or none where it has none or several", None, RUN_ID, "Claude")
                    conn.execute("UPDATE ib_node SET collection_id=? WHERE id=?", (new, n["id"])); changed_nodes += 1
        got = dict(collections_retired=one("SELECT count(*) FROM collection WHERE deleted=0 AND status='retired' AND run_id=?", RUN_ID) - marked_before,
                   regrouped=one("SELECT count(*) FROM surface_event WHERE run_id=? AND action='set_group'", RUN_ID) - regrouped_before,
                   live_links_after=one("SELECT count(*) FROM collection_link WHERE deleted=0"))
        print("actual:   ", got, "| nodes whose collection changed:", changed_nodes)
        bad = [k for k in ("collections_retired", "regrouped", "live_links_after") if got[k] != pred[k]]
        stranded = one("SELECT count(*) FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.status IN ('merged','retired') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER)
        lost = covered_before - covered_set()
        lost_phrases = sorted(text_of[t] for t in lost - allowed if t in text_of and " " in text_of[t])
        print("phrase surfaces whose only collection was a dissolved one (placed in step 4):", len(lost_phrases), lost_phrases)
        lost_other = sorted(text_of[t] for t in lost - allowed if t in text_of and " " not in text_of[t])
        lost_derived = sorted(text_of[t] for t in lost & allowed if t in text_of and t not in regroup_ids and t not in computed_ids)
        print("member links still on a merged or retired collection:", stranded)
        print("surfaces losing their collection that are not regrouped words or their derived forms:", len(lost_other), lost_other[:80])
        print("derived forms of regrouped or computed words that lose coverage through the base:", len(lost_derived), lost_derived[:80])
        if bad or stranded or lost_other:
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
