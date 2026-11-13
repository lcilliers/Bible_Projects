"""collection_verify_fix_2491_v1_20261113.py -- escalation #2491, plan v3 step 7 correction after the verification by lists: what the list of surfaces without a collection showed.

Researcher, 2026-11-13: 'Yes, both' (step 7 verification). After the review of uncovered-words 20 forms whose base is now in one collection, and 8 phrases and 18 words and phrases read by meaning, were still without a collection of their own. The inherit rule of step 5 (a derived form takes the one collection of its base, minus the forms whose sense is not the base's) is applied to the 20; the phrases are placed or regrouped by meaning. The node column follows the own-row rule. The members of a collection are surfaces; the base is only an instrument. A study surface (a word of the groups
behaviour or inner_being_state with a verse) that has no link of its own but whose base is a member of exactly one collection now has its own link in that
collection (INHERIT; tier opposite where the base's own link is an opposite, otherwise synonym). I read the whole list of such forms (624) by meaning and
took out those whose sense is not the base's (EXCLUDE: for example fasting and fasten are not the speed of fast; presence is not present; contention is not
content; born, lain, easy, freely, deadly, acts), and the forms whose base sits only in the gathered collection uncovered-words (not an analytic collection)
are not extended. Forms and words placed by meaning in another collection are in PLACE; the generic ones whose base is of group other, and a few
generic words with no base, are regrouped to other (REGROUP). Every ruling is inferential (B:4). Nothing is physically deleted. Then
surface_term.collection_state and ib_node.collection_id (the exactly-one rule). Stops and rolls back unless predicted equals actual, no surface loses
coverage, and every form given a link is in exactly one collection. Idempotent.
    python -m iba.app.migration.collection_verify_fix_2491_v1_20261113 [--db PATH] [--dry-run]   (from the project root)
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
RUN_ID = "DEVMODE-2491-VERIFY-FIX-20261113"
WHO = "devmode-2491"
MEMBER = ("core", "synonym", "opposite", "gathered", "phrase")
SRC = "researcher 2026-11-13 (#2491): step 5"
STUDY = ("behaviour", "inner_being_state")

EXCLUDE = set("deadly easy freely presence lain born contention contentious fasten fasting acted actions acts breakers law-breakers brokenhearted quick-tempered".split())
PLACE_LINES = """
search: avenge myself; not avenged
astray: be wanderers
condemn: bring judgment
impartial: bring justice
crime: deals corruptly
bold: good courage
preach: good news
"""
REGROUP_WORDS = ["burning heat", "cannot succeed", "heights", "highest", "maturity", "not consider", "not revoke", "putting", "rightly handling", "rouses", "spirit in", "spiritual things", "spiritual truths", "stirred", "stirs", "they were like those", "useless", "exchanged"]
REGROUP_WHY = "a generic word (its base is of group other, or it is a plain action, place, time or measure word), not a behaviour or an inner-being state (researcher 2026-11-13, #2491 step 5)"
PLACE = {}
for line in PLACE_LINES.strip().splitlines():
    col, ws = line.split(":", 1)
    for w in ws.split(";"):
        if w.strip():
            PLACE[w.strip()] = col.strip()


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
    both = sorted(set(PLACE) & set(REGROUP_WORDS))
    if both:
        raise Stop("word in both lists: %s" % both)
    verse_words = {r[0] for r in q("SELECT DISTINCT lower(surface) FROM verse_lexical WHERE deleted=0 AND surface_kind<>'gloss'")}
    terms = {r["id"]: r for r in q("SELECT id, surface, base_id, surface_group FROM surface_term WHERE deleted=0")}
    ids_of = collections.defaultdict(list)
    for t, r in terms.items():
        ids_of[r["surface"]].append(t)
    own = collections.defaultdict(list)   # term -> [(collection id, tier)]
    for r in q("SELECT l.term_id, l.collection_id, l.tier FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 "
               "AND c.status IN ('indicative','confirmed') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER):
        own[r[0]].append((r[1], r[2]))
    uncovered = cname.get("uncovered-words")
    adds = []       # (term, collection, tier, reason)
    inherit_n = 0
    for tid, r in sorted(terms.items()):
        s = r["surface"]
        if " " in s or r["surface_group"] not in STUDY or s.lower() not in verse_words or own.get(tid) or s in EXCLUDE or s in PLACE or s in REGROUP_WORDS:
            continue
        b = r["base_id"]
        if b and b != tid and b in terms:
            bl = own.get(b, [])
            cols = {c for c, _ in bl}
            if len(cols) == 1 and uncovered not in cols:
                c, tier = bl[0]
                adds.append((tid, c, "opposite" if tier == "opposite" else "synonym",
                             "%s is a surface of its own: it takes the one collection of its base %s (step 7 correction)" % (s, terms[b]["surface"]))); inherit_n += 1
    for w, kc in PLACE.items():
        for tid in ids_of.get(w, []):
            if terms[tid]["surface_group"] in STUDY + ("other",) and not own.get(tid):
                adds.append((tid, cname[kc], "phrase" if " " in w else "synonym", "%s is placed in %s by meaning (step 7 correction)" % (w, kc)))
    regroup = []
    for w in REGROUP_WORDS:
        for tid in ids_of.get(w, []):
            if terms[tid]["surface_group"] != "other":
                regroup.append((tid, w, terms[tid]["surface_group"], REGROUP_WHY))
    existing = {(r[0], r[1]): r[2] for r in q("SELECT collection_id, term_id, id FROM collection_link WHERE deleted=0")}   # a non-member association is made a member
    replaced = [existing[(c, t)] for t, c, _, _ in adds if (c, t) in existing]
    regroup_ids = {t for t, _, _, _ in regroup}
    drops = [(l, "the surface %s is regrouped to other" % terms[tid]["surface"]) for tid in regroup_ids
             for l in q("SELECT id FROM collection_link WHERE term_id=? AND deleted=0 AND tier IN (%s)" % ",".join("?" * len(MEMBER)), tid, *MEMBER)]

    def covered_set():
        o = {r[0] for r in q("SELECT DISTINCT l.term_id FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 "
                             "AND c.status IN ('indicative','confirmed') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER)}
        out = set(o)
        for r in q("SELECT id, base_id FROM surface_term WHERE deleted=0"):
            if r["id"] in o or (r["base_id"] and r["base_id"] in o):
                out.add(r["id"])
        return out
    covered_before = covered_set()
    live_before = one("SELECT count(*) FROM collection_link WHERE deleted=0")
    pred = dict(inherited=inherit_n, placed=len(adds) - inherit_n, regrouped=len(regroup), links_deleted=len(drops),
                links_made_member=len(replaced), live_links_after=live_before + len(adds) - len(drops) - len(replaced))
    print("predicted:", pred)
    if not adds and not regroup:
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
        for tid, col, tier, reason in adds:
            old = existing.get((col, tid))
            if old:
                conn.execute("UPDATE collection_link SET deleted=1, updated_at=" + now_sql + ", run_id=? WHERE id=?", (RUN_ID, old))
            nl = conn.execute("INSERT INTO collection_link (collection_id, term_id, tier, superseded_by_id, shared, reason, run_id, created_by) VALUES (?,?,?,NULL,0,?,?,?)",
                              (col, tid, tier, reason, RUN_ID, WHO)).lastrowid
            if old:
                conn.execute("UPDATE collection_link SET superseded_by_id=? WHERE id=?", (nl, old))
                ev("collection_link", nl, "set_tier", str(old), str(nl), reason, "collection_id")
            else:
                ev("collection_link", nl, "add", None, cid_name.get(col), reason, "collection_id")
            touched.add(tid)
        for (lid,), reason in drops:
            oc, t = conn.execute("SELECT collection_id, term_id FROM collection_link WHERE id=?", (lid,)).fetchone()
            conn.execute("UPDATE collection_link SET deleted=1, updated_at=" + now_sql + ", run_id=? WHERE id=?", (RUN_ID, lid))
            ev("collection_link", lid, "remove", cid_name.get(oc), None, reason, "collection_id"); touched.add(t)
        for tid, w, before, why in regroup:
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
                o |= cols_now.get(sid) or (cols_now.get(b, set()) if b else set())
            return o
        surf_touched = {terms[t]["surface"] for t in touched if t in terms}
        changed_nodes = 0
        for n in q("SELECT id, observation_id, collection_id, lower(trim(surface)) AS s FROM ib_node WHERE deleted=0 AND surface IS NOT NULL AND trim(surface)<>''"):
            if n["s"] in surf_touched:
                cs = carry(n["s"])
                new = next(iter(cs)) if len(cs) == 1 else None
                if new != n["collection_id"]:
                    orec.log(conn, n["observation_id"], n["id"], "collection_id", n["collection_id"], new,
                             "members are surfaces (researcher 2026-11-13, #2491 step 5); the node carries the one collection of its surface, or none where it has none or several", None, RUN_ID, "Claude")
                    conn.execute("UPDATE ib_node SET collection_id=? WHERE id=?", (new, n["id"])); changed_nodes += 1
        got = dict(regrouped=one("SELECT count(*) FROM surface_event WHERE run_id=? AND action='set_group'", RUN_ID) - regrouped_before,
                   live_links_after=one("SELECT count(*) FROM collection_link WHERE deleted=0"))
        print("actual:   ", got, "| nodes whose collection changed:", changed_nodes)
        bad = [k for k in ("regrouped", "live_links_after") if got[k] != pred[k]]
        stranded = one("SELECT count(*) FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.status IN ('merged','retired') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER)
        lost = sorted(terms[t]["surface"] for t in covered_before - covered_set() if t in terms and t not in regroup_ids)
        notone = sorted({terms[t]["surface"] for t, _, _, _ in adds if len(cols_now.get(t, set())) != 1})
        print("member links on a merged or retired collection:", stranded, "| surfaces losing coverage (not regrouped):", len(lost), lost[:40],
              "| given a link and not in exactly one collection:", len(notone), notone[:20])
        if bad or stranded or lost or notone:
            raise Stop("actual differs from predicted (%s), links stranded, coverage lost or a form not in one collection: rolled back" % bad)
        if a.dry_run:
            conn.execute("ROLLBACK TO w"); print("dry run: rolled back")
        else:
            conn.execute("RELEASE w"); conn.commit(); print("committed")
    except Exception:
        conn.execute("ROLLBACK TO w"); conn.commit(); raise
    return 0


if __name__ == "__main__":
    sys.exit(main())

