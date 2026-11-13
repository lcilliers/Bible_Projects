"""collection_one_place_step3_2491_v1_20261113.py -- escalation #2491, plan v3 step 3.

Researcher, 2026-11-13: 'Yes, step 3' (one collection for each remaining overlapping word). The 157 single words that were members of two or more
collections were read by meaning, each with the collections that hold it, and each is given the one collection below (KEEP). Every ruling is
inferential (B:4) and none is decided by script; the list is the ruling. For each word the member links in every other collection are set deleted
(new rows are not needed: the kept link stays as it is), except 'hallowed', which is placed in dedicate (it was in neither of its two collections'
sense) and so is moved there. Non-member links (associated, possible opposite, set aside) are left. Phrases are step 4 and are not touched.
Nothing is physically deleted (links are set deleted with the reason in surface_event). Then surface_term.collection_state for the touched
terms and ib_node.collection_id by the exactly-one rule. Stops and rolls back unless predicted equals actual, no word loses its collection,
no collection loses its core, and no member link is left on a merged or retired collection. Idempotent.
    python -m iba.app.migration.collection_one_place_step3_2491_v1_20261113 [--db PATH] [--dry-run]   (from the project root)
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
RUN_ID = "DEVMODE-2491-ONE-PLACE-STEP3-20261113"
WHO = "devmode-2491"
RANK = ["core", "synonym", "opposite", "gathered", "phrase", "associated", "possible_opposite", "set_aside"]
MEMBER = ("core", "synonym", "opposite", "gathered", "phrase")
SRC = "researcher 2026-11-13 (#2491): step 3"

KEEP_LINES = """
godly: ungodly unholy ungodliness | deceive: deceitful deceptive deceive | dedicate: devoted devotion consecrate dedicated determined consecrated committed hallowed
tribulation: affliction afflictions suffering | supplication: entreat implore | godly: god-fearing godly | righteous: righteousness righteous lawful
greed: covetous covetousness covet | honor: dignity noble | strengthen: weaken weakened strengthen | love: beloved cherish abhor
abase: exalt humble humiliate | abominable: accursed | evildoer: vile | loyalty: faithfulness steadfast | crime: transgression | faithless: unfaithful faithlessness
utter: uttered | reverence: awe reverent | wayward: wayward | astray: stray | bless: grace | majesty: splendor glory | believe: faith | trust: trust
forsake: forsake abandon | commend: extol approve | preach: proclaim declare proclaimed | fear: fearful | firm: firm frail | mighty: strong mighty stronger
bold: valiant | destruction: demolish destroy | build: erect | change: change transform | chide: censure reproach rebuke | chief: authority
cleanse: pure | guard: defend | tenderhearted: soft gentle tenderhearted | command: execute | compel: required demanding | exhort: urge exhort admonish
condemn: denounce | consent: agreement | continual: enduring unceasing | upright: steady upright | convince: persuade | earnest: sincere earnest wholehearted
real: honest genuine | skill: skillful skilled | sin: offense sinful | cruel: cruel | delight: delight joyful joy | depart: depart leave | live: live
fulfill: fulfill complete fulfilled | solemn: serious dignified | endure: withstand remain persevere | impartial: fair | loosen: release | faint: weak
sloth: slow | supply: supply provide | wise: wisdom | forgive: merciful | reject: reject renounce deny | watch: watch observe | harden: hardened
hear: ignore | partial: partial | innocent: blameless unstained | intend: plan | scoff: despise | realized: grasped realized | mute: silence
oppress: oppress | pain: torment | persecute: abuse persecution | quarrel: peace | ready: alert | rebel: disobedient | whisper: whisper
self-control: self-controlled | teach: impart | sober: sober | stronghold: fortified | submission: submissive | trial: trial
"""
KEEP = {}
for part in KEEP_LINES.replace("\n", " | ").split("|"):
    part = part.strip()
    if not part:
        continue
    col, words = part.split(":")
    for w in words.split():
        KEEP[w] = col.strip()


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
    core_of = {r["id"]: r["core_term_id"] for r in q("SELECT id, core_term_id FROM collection WHERE deleted=0")}
    missing = sorted({c for c in KEEP.values() if c not in cname})
    if missing:
        raise Stop("collections not found: %s" % missing)
    text_of = {r["id"]: r["surface"] for r in q("SELECT id, surface FROM surface_term WHERE deleted=0")}
    ids_of = collections.defaultdict(list)
    for t, s in text_of.items():
        ids_of[s].append(t)
    links_of = collections.defaultdict(list)
    for r in q("SELECT l.* FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 AND c.status IN ('indicative','confirmed') "
               "AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER):
        links_of[r["term_id"]].append(r)

    actions = []   # ("drop", link id, reason) | ("move", link id, to col, term, tier, reason)
    planned = set()
    for w, kc in sorted(KEEP.items()):
        k = cname[kc]
        rows = [l for t in ids_of.get(w, []) for l in links_of.get(t, [])]
        in_keep = [l for l in rows if l["collection_id"] == k]
        others = [l for l in rows if l["collection_id"] != k]
        why = "%s sits once, in %s (step 3, by meaning)" % (w, kc)
        if not in_keep and others:
            first = others[0]
            tier = "synonym" if first["tier"] == "core" else first["tier"]
            actions.append(("move", first["id"], k, first["term_id"], tier, why)); planned.add(first["id"])
            others = others[1:]
        for l in others:
            if core_of.get(l["collection_id"]) == l["term_id"]:
                raise Stop("%s is the core of %s: not dropped" % (w, cid_name.get(l["collection_id"])))
            actions.append(("drop", l["id"], why)); planned.add(l["id"])

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
    # a move inserts one link and deletes one (net 0); a drop deletes one
    pred = dict(actions=dict(kinds), live_links_after=live_before - kinds["drop"])
    print("predicted:", pred, "| words ruled:", len(KEEP))
    if not actions:
        print("nothing to do (already applied)")
        return 0
    conn.execute("SAVEPOINT w")
    try:
        now_sql = "strftime('%Y-%m-%dT%H:%M:%SZ','now')"
        touched = set()

        def ev(subject, sid, action, before, after, reason):
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                         "VALUES (?,?,?,?,?,?,?,?,?,?)", (subject, sid, action, "collection_id" if subject == "collection_link" else None, before, after, "Claude",
                                                           "%s (%s)" % (reason, SRC), RUN_ID, WHO))

        def kill(old_id, new_id):
            conn.execute("UPDATE collection_link SET deleted=1, superseded_by_id=?, updated_at=" + now_sql + ", run_id=? WHERE id=?", (new_id, RUN_ID, old_id))
        for act in actions:
            if act[0] == "drop":
                _, old, reason = act
                oc, t = conn.execute("SELECT collection_id, term_id FROM collection_link WHERE id=?", (old,)).fetchone()
                kill(old, None); ev("collection_link", old, "remove", cid_name.get(oc), None, reason); touched.add(t)
            else:
                _, old, to_col, t, tier, reason = act
                oc = one("SELECT collection_id FROM collection_link WHERE id=?", old)
                kill(old, None)
                nl = conn.execute("INSERT INTO collection_link (collection_id, term_id, tier, superseded_by_id, shared, reason, run_id, created_by) VALUES (?,?,?,NULL,0,?,?,?)",
                                  (to_col, t, tier, reason, RUN_ID, WHO)).lastrowid
                conn.execute("UPDATE collection_link SET superseded_by_id=? WHERE id=?", (nl, old))
                ev("collection_link", nl, "move", cid_name.get(oc), cid_name.get(to_col), reason); touched.add(t)
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
        ids = touched | derived
        surf_touched = {r["surface"] for r in q("SELECT surface FROM surface_term WHERE id IN (%s)" % ",".join(str(x) for x in ids or {0}))}
        changed_nodes = 0
        for n in q("SELECT id, observation_id, collection_id, lower(trim(surface)) AS s FROM ib_node WHERE deleted=0 AND surface IS NOT NULL AND trim(surface)<>''"):
            if n["s"] in surf_touched:
                cs = carry(n["s"])
                new = next(iter(cs)) if len(cs) == 1 else None
                if new != n["collection_id"]:
                    orec.log(conn, n["observation_id"], n["id"], "collection_id", n["collection_id"], new,
                             "each word sits in one collection (researcher 2026-11-13, #2491 step 3); the node carries the one collection of its surface, or none where it has several", None, RUN_ID, "Claude")
                    conn.execute("UPDATE ib_node SET collection_id=? WHERE id=?", (new, n["id"])); changed_nodes += 1
        got = dict(live_links_after=one("SELECT count(*) FROM collection_link WHERE deleted=0"))
        print("actual:   ", got, "| nodes whose collection changed:", changed_nodes)
        bad = [k for k in ("live_links_after",) if got[k] != pred[k]]
        stranded = one("SELECT count(*) FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.status IN ('merged','retired') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), *MEMBER)
        lost = sorted(text_of[t] for t in covered_before - covered_set() if t in text_of)
        still = [w for w in KEEP if len({l["collection_id"] for t in ids_of.get(w, []) for l in q("SELECT l.collection_id FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.term_id=? AND l.deleted=0 AND c.status IN ('indicative','confirmed') AND l.tier IN (%s)" % ",".join("?" * len(MEMBER)), t, *MEMBER)}) != 1]
        print("member links on a merged or retired collection:", stranded, "| surfaces losing coverage:", len(lost), lost[:40], "| ruled words not in exactly one collection:", still)
        if bad or stranded or lost or still:
            raise Stop("actual differs from predicted (%s), links stranded, coverage lost or a ruled word not in one collection: rolled back" % bad)
        if a.dry_run:
            conn.execute("ROLLBACK TO w"); print("dry run: rolled back")
        else:
            conn.execute("RELEASE w"); conn.commit(); print("committed")
    except Exception:
        conn.execute("ROLLBACK TO w"); conn.commit(); raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
