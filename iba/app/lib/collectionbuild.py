"""collectionbuild -- module 5 of 5 of the surface cycle: the members of each collection, decided from the AI judgements (escalation #2361, stage 5).

A collection has a core word (a surface term). The AI step judged each candidate word against the core (step `candidate`: synonym, opposite
or distinct; for an opposite, `pole_syn` says whether the word is a synonym of the core's pole) and, for the words that are neither, whether the
word is still associated by meaning (step `associated`). The model also listed words of its own (collection_listing); a listed synonym the judge
refused is a word the model offered and the study does not bind. This module is the rule that turns those judgements into collection_link
rows, reproducing the five recorded runs of 2026-11-05 (iba/app/tools/temp_2361_collection_test_run.py):

  core ................ the collection's own core term
  synonym ............. the latest candidate call says synonym
  opposite ............ the latest call says opposite and pole_syn is true (the word is a synonym of the core's pole)
  possible_opposite ... the latest call says opposite and pole_syn is not true (a lead, never a member)
  set_aside ........... the call says distinct (or there is none), the model listed the word as a synonym and the judge refused it, and the
                        word is not a core, synonym or opposite of another collection
  associated .......... none of the above, and the latest associated call says true
The latest call of a (collection, word) pair decides. A link is shared when its word is a core, synonym or opposite of more than one
collection. The state of a word (surface_term.collection_state) follows from its links. The prototype left 18 associated-true pairs unlinked
(chosen by hand while reviewing); they are PROPOSED here and linked only with -Associate. Nothing is deleted: a link that changes is set to
deleted = 1 with superseded_by_id. Every judgement is inferential until the researcher confirms it (B:4). Reads only tables.
"""
from __future__ import annotations

import datetime
import json
import re

STRONG = ("core", "synonym", "opposite")
SEED = re.compile(r'Core word: "([^"]+)"')


class CollectionError(Exception):
    """A usage problem: routed as 'refused', nothing written."""


def _seed_of(answer, request):
    try:
        s = (json.loads(answer) or {}).get("seed") if answer else None
    except ValueError:
        s = None
    if s:
        return s
    m = SEED.search(request or "")
    return m.group(1) if m else None


CAND = re.compile(r'Candidate word: "([^"]+)"')


def load(conn, threshold=None) -> dict:
    """Everything the rule reads, from the tables. threshold is cfg_setting collection.score_threshold (None: no score rule)."""
    cols = {r[0]: dict(id=r[0], core=r[1], seed=r[2], status=r[3]) for r in conn.execute(
        "SELECT c.id, c.core_term_id, t.surface, c.status FROM collection c JOIN surface_term t ON t.id=c.core_term_id "
        "WHERE c.deleted=0 AND c.status IN ('indicative','confirmed')")}
    by_seed = {c["seed"]: c["id"] for c in cols.values()}
    tid = {r[0]: r[1] for r in conn.execute("SELECT surface, id FROM surface_term WHERE deleted=0")}
    cand, assoc, score, pole = {}, {}, {}, {}
    for cid, step, skind, sid, ans, req, outcome in conn.execute(
            "SELECT id, step, subject_kind, subject_id, answer, request, outcome FROM ai_call WHERE module='collection' AND "
            "step IN ('candidate','associated','score','pole_check') AND deleted=0 ORDER BY id"):
        if outcome != "answered":
            continue
        a = json.loads(ans)
        if skind == "collection":                      # a call made by the AI client: the collection is the subject, the word is in the request
            col = sid if sid in cols else None
            m = CAND.search(req or "")
            term = tid.get(m.group(1)) if m else None
        else:                                          # a loaded prototype call: the word is the subject, the seed is in the answer
            col, term = by_seed.get(_seed_of(ans, req)), sid
        if col is None or term is None:
            continue
        k = (col, term)
        if step == "candidate":
            cand[k] = dict(call=cid, relation=a.get("relation"), pole_syn=a.get("pole_syn"), composite="syn_said" in a)
        elif step == "associated":
            assoc[k] = dict(call=cid, associated=a.get("associated") is True)
        elif step == "score":
            score[k] = a.get("score")
        else:
            pole[k] = a.get("relation") == "synonym"
    for k, v in cand.items():                          # the rules of a call made by the AI client: a high score makes a distinct word a synonym,
        if v["composite"]:                             # the pole check makes an opposite a real opposite (a loaded call already holds both)
            continue
        if v["relation"] == "distinct" and threshold is not None and isinstance(score.get(k), (int, float)) and score[k] >= threshold:
            v["relation"] = "synonym"
        if v["relation"] == "opposite":
            v["pole_syn"] = pole.get(k)
    refused = {(r[0], r[1]) for r in conn.execute(
        "SELECT collection_id, term_id FROM collection_listing WHERE deleted=0 AND kind='synonym' AND outcome='refused' AND term_id IS NOT NULL")}
    return {"cols": cols, "cand": cand, "assoc": assoc, "refused": refused}


def decide(data: dict) -> dict:
    """Pure: {(collection, term): (tier, ai_call id or None)} for every pair the rule links, and 'proposed' pairs that the prototype left out are
    marked by the caller against the stored links."""
    cols, cand, assoc, refused = data["cols"], data["cand"], data["assoc"], data["refused"]
    out: dict = {}
    for c in cols.values():
        out[(c["id"], c["core"])] = ("core", None)
    for k, v in cand.items():
        if k in out:
            continue
        if v["relation"] == "synonym":
            out[k] = ("synonym", v["call"])
        elif v["relation"] == "opposite":
            out[k] = ("opposite" if v["pole_syn"] is True else "possible_opposite", v["call"])
    strong: dict = {}
    for (col, term), (tier, _) in out.items():
        if tier in STRONG:
            strong.setdefault(term, set()).add(col)
    pairs = set(cand) | set(assoc) | refused
    for k in sorted(pairs):
        if k in out or k[0] not in cols:
            continue
        col, term = k
        if k in refused and not (strong.get(term, set()) - {col}):
            out[k] = ("set_aside", cand[k]["call"] if k in cand else None)
        elif assoc.get(k, {}).get("associated"):
            out[k] = ("associated", assoc[k]["call"])
    return out


def shared_terms(decided: dict) -> set:
    strong: dict = {}
    for (col, term), (tier, _) in decided.items():
        if tier in STRONG:
            strong.setdefault(term, set()).add(col)
    return {t for t, s in strong.items() if len(s) > 1}


def term_states(decided: dict, shared: set) -> dict:
    """{term: collection_state} for the terms with a link; other terms are untouched."""
    tiers: dict = {}
    for (col, term), (tier, _) in decided.items():
        tiers.setdefault(term, set()).add(tier)
    out = {}
    for term, ts in tiers.items():
        if term in shared:
            out[term] = "shared"
        elif ts & set(STRONG):
            out[term] = "placed"
        elif "set_aside" in ts:
            out[term] = "set_aside"
        else:
            out[term] = "listed_only"
    return out


def stored(conn) -> dict:
    return {(r[0], r[1]): (r[2], r[3], r[4]) for r in conn.execute(
        "SELECT collection_id, term_id, tier, shared, id FROM collection_link WHERE deleted=0")}


def removed_pairs(conn) -> set:
    """Pairs with no live link whose latest link row was removed on purpose (deleted = 1, superseded_by_id NULL)."""
    live = {(r[0], r[1]) for r in conn.execute("SELECT collection_id, term_id FROM collection_link WHERE deleted=0")}
    return {(r[0], r[1]) for r in conn.execute("SELECT collection_id, term_id FROM collection_link WHERE deleted=1 AND superseded_by_id IS NULL")} - live


def plan(conn, threshold=None) -> dict:
    """What a run would change: add, supersede (tier changed), reshare; and the decided pairs withheld because their link was removed."""
    data = load(conn, threshold)
    decided = decide(data)
    sh = shared_terms(decided)
    have = stored(conn)
    gone = removed_pairs(conn)
    add, change, same, proposed, orphans, reshare = [], [], 0, [], [], []
    for k, (tier, call) in sorted(decided.items()):
        s = have.get(k)
        want_shared = int(tier in STRONG and k[1] in sh)
        if s is None:
            if k in gone:
                proposed.append((k, call))
            else:
                add.append((k, tier, call, want_shared))
        elif s[0] != tier:
            change.append((k, tier, call, want_shared, s[2]))
        elif s[1] != want_shared:
            reshare.append((s[2], want_shared))
        else:
            same += 1
    for k, s in have.items():
        if k not in decided:
            orphans.append((k, s[0]))
    held = {k for k, _ in proposed}
    states = term_states({k: v for k, v in decided.items() if k not in held}, sh)
    cur = {r[0]: r[1] for r in conn.execute("SELECT id, collection_state FROM surface_term WHERE deleted=0")}
    state_changes = [(t, v) for t, v in sorted(states.items()) if cur.get(t) != v]
    return {"decided": decided, "add": add, "change": change, "reshare": reshare, "same": same, "proposed": proposed, "orphans": orphans,
            "state_changes": state_changes, "n_cols": len(data["cols"])}


def write(conn, run_id: str, pl: dict) -> dict:
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    done = {"added": 0, "superseded": 0, "reshared": 0, "states": 0}
    for (col, term), tier, call, shared, old in pl["change"]:
        conn.execute("UPDATE collection_link SET deleted=1, updated_at=?, run_id=? WHERE id=?", (now, run_id, old))  # first: one live link per pair
        cur = conn.execute("INSERT INTO collection_link (collection_id, term_id, tier, shared, ai_call_id, run_id, created_by) VALUES (?,?,?,?,?,?,'collection-build')",
                           (col, term, tier, shared, call, run_id))
        conn.execute("UPDATE collection_link SET superseded_by_id=? WHERE id=?", (cur.lastrowid, old))
        done["superseded"] += 1
    for (col, term), tier, call, shared in pl["add"]:
        conn.execute("INSERT INTO collection_link (collection_id, term_id, tier, shared, ai_call_id, reason, run_id, created_by) VALUES (?,?,?,?,?,?,?,'collection-build')",
                     (col, term, tier, shared, call, "the seed" if tier == "core" else None, run_id))
        done["added"] += 1
    for lid, sh in pl["reshare"]:
        conn.execute("UPDATE collection_link SET shared=?, updated_at=?, run_id=? WHERE id=?", (sh, now, run_id, lid))
        done["reshared"] += 1
    for term, state in pl["state_changes"]:
        conn.execute("UPDATE surface_term SET collection_state=?, updated_at=?, run_id=? WHERE id=?", (state, now, run_id, term))
        done["states"] += 1
    return done
