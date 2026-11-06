"""collectionask -- the front of module 5 of 5: seeding a collection and asking the AI for its members (escalation #2361, stage 5).

seed_collection(): a core word of collection a becomes a collection (status indicative). The AI client is asked for its POLE (prompt
collection.pole: the one word that is its direct opposite), whether the pole is a real English word (collection.real_word), the pole of the pole
(reciprocal when it names the core again), and the model's own LIST of synonyms and opposites (collection.list). The listed words are stored in
collection_listing (outcome unjudged, or not_in_pool when no surface of collection a is that word).

ask_collection(): the candidates of a collection are the words of collection a nearest to the core in the embedding space (the shortlist, size
collection.shortlist_size; the vectors are a regenerable cache beside the working files) plus the listed words not yet judged. Each candidate is judged
against the core (collection.synonym: synonym, opposite or distinct, step candidate). A distinct word is scored (collection.score, step score): a
score of collection.score_threshold or more makes it a synonym (lib/collectionbuild reads this). An opposite is checked against the pole (the same
question with the pole as the core, step pole_check). A word that is neither a synonym nor an opposite is asked for association by meaning
(collection.associated, step associated). A listed word's outcome becomes bound (judged as listed) or refused. Every call is one ai_call row of module
collection with the collection as subject; the word is in the stored request. Afterwards run Collection-Build.ps1 -Action Links.
Every judgement is inferential until the researcher confirms it (B:4).
"""
from __future__ import annotations

import json
import math
import pathlib
import re

SETTING_KEYS = ["collection.shortlist_size", "collection.score_threshold", "collection.embed_cache", "collection.embed_role", "collection.list_max"]
WORD = re.compile(r"[a-z]+(-[a-z]+)*")
RELATIONS = ("synonym", "opposite", "distinct")


class AskError(Exception):
    """A usage problem or a missing setting: routed as 'refused', nothing written."""


def read_settings(cfg) -> dict:
    vals = {k: cfg.setting(k) for k in SETTING_KEYS}
    missing = [k for k, v in vals.items() if v is None]
    if missing:
        raise AskError(f"cfg_setting missing: {missing}")
    root = cfg.setting("surfaces.working_files_root")
    if not root:
        raise AskError("cfg_setting surfaces.working_files_root is missing")
    vals["cache_dir"] = pathlib.Path(root) / vals["collection.embed_cache"]
    scope = cfg.setting("surfaces.scope_groups")
    if not scope or "a" not in scope:
        raise AskError("cfg_setting surfaces.scope_groups is missing or has no collection a")
    vals["scope_a"] = scope["a"]
    return vals


# ---- checks of the answers --------------------------------------------------------------------------------------------------------------
def check_relation(a):
    return [] if isinstance(a, dict) and a.get("relation") in RELATIONS else [f"relation {a.get('relation') if isinstance(a, dict) else a!r}"]


def check_score(a):
    ok = isinstance(a, dict) and isinstance(a.get("score"), (int, float)) and not isinstance(a.get("score"), bool) and 0 <= a["score"] <= 10
    return [] if ok else ["score is not a number from 0 to 10"]


def check_assoc(a):
    return [] if isinstance(a, dict) and isinstance(a.get("associated"), bool) else ["associated is not true or false"]


def check_real(a):
    return [] if isinstance(a, dict) and isinstance(a.get("real"), bool) else ["real is not true or false"]


def check_pole(a):
    if not isinstance(a, dict) or "opposite" not in a:
        return ["no opposite key"]
    o = a["opposite"]
    return [] if o is None or (isinstance(o, str) and WORD.fullmatch(o.strip().lower())) else [f"opposite {o!r} is not one word"]


def check_list(a):
    if not isinstance(a, dict) or not all(isinstance(a.get(k), list) and all(isinstance(w, str) for w in a[k]) for k in ("synonyms", "opposites")):
        return ["synonyms and opposites must be lists of words"]
    return []


# ---- embeddings ---------------------------------------------------------------------------------------------------------------------
def cosine(a, b):
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    return sum(x * y for x, y in zip(a, b)) / (na * nb) if na and nb else 0.0


def embeddings(client, vals: dict, words: list) -> dict:
    """{word: vector} for the words, from the cache beside the working files or from the embedding model (the cache is regenerable, never an
    input of a decision other than this ranking). One file per model digest."""
    role = vals["collection.embed_role"]
    model = client.model(role)
    cache_dir = vals["cache_dir"]
    path = cache_dir / f"{model[1].replace(':', '_')}-{(model[2] or 'nodigest')[:12]}.json"
    have = {}
    if path.exists():
        try:
            have = json.loads(path.read_text(encoding="utf-8"))
        except ValueError:
            have = {}
    need = [w for w in words if w not in have]
    if need:
        for w, v in zip(need, client.embed(role, need)):
            have[w] = v
        cache_dir.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(have), encoding="utf-8")
    return {w: have[w] for w in words}


def pool_words(conn, vals: dict) -> dict:
    """{surface: term id} the words of collection a that can be candidates (single words)."""
    marks = ",".join("?" * len(vals["scope_a"]))
    return {r[0]: r[1] for r in conn.execute(
        f"SELECT surface, id FROM surface_term WHERE deleted=0 AND origin='surface' AND form='word' AND surface_group IN ({marks})", vals["scope_a"])}


def shortlist(core_vec, vecs: dict, k: int, exclude: set) -> list:
    ranked = sorted(((cosine(core_vec, v), w) for w, v in vecs.items() if w not in exclude), key=lambda x: (-x[0], x[1]))
    return [w for _, w in ranked[:k]]


def forms_of(conn, term_id: int, surface: str) -> str:
    """The forms in the text of a candidate: the surfaces whose base it is, or itself."""
    forms = [r[0] for r in conn.execute("SELECT surface FROM surface_term WHERE base_id=? AND deleted=0 AND id!=? ORDER BY surface", (term_id, term_id))]
    return ", ".join(forms[:8]) if forms else surface


# ---- seeding -----------------------------------------------------------------------------------------------------------------------
def seed_collection(conn, client, vals: dict, word: str, run_id: str) -> dict:
    word = word.strip().lower()
    pool = pool_words(conn, vals)
    if word not in pool:
        raise AskError(f"{word!r} is not a single word of collection a (a live surface of the groups {vals['scope_a']})")
    if conn.execute("SELECT 1 FROM collection WHERE core_term_id=? AND deleted=0 AND status!='retired'", (pool[word],)).fetchone():
        raise AskError(f"{word!r} already has a collection")
    cid = conn.execute("INSERT INTO collection (core_term_id, name, status, run_id, created_by) VALUES (?,?, 'indicative', ?, 'collection-seed')",
                       (pool[word], word, run_id)).lastrowid
    conn.commit()
    sub = ("collection", cid)

    def ask(key, variables, check, step):
        return client.call("judge", key, variables, sub, check=check, step=step)

    pole = pole2 = None
    real = None
    r = ask("collection.pole", {"a": word}, check_pole, "pole")
    if r["outcome"] == "answered" and r["answer"].get("opposite"):
        pole = r["answer"]["opposite"].strip().lower()
        rr = ask("collection.real_word", {"w": pole}, check_real, "real_word")
        real = int(rr["answer"]["real"]) if rr["outcome"] == "answered" else None
        r2 = ask("collection.pole", {"a": pole}, check_pole, "pole")
        pole2 = (r2["answer"].get("opposite") or "").strip().lower() or None if r2["outcome"] == "answered" else None
    conn.execute("UPDATE collection SET pole_word=?, pole_of_pole=?, pole_reciprocal=?, pole_real_word=?, updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now') WHERE id=?",
                 (pole, pole2, int(pole2 == word) if pole2 else (0 if pole else None), real, cid))
    lst = ask("collection.list", {"a": word}, check_list, "listing")
    n_listed = 0
    if lst["outcome"] == "answered":
        mx = int(vals["collection.list_max"])
        seen = set()
        for kind, key in (("synonym", "synonyms"), ("opposite", "opposites")):
            for w in lst["answer"][key][:mx]:
                w = w.strip().lower()
                if not w or w in seen or w == word or not WORD.fullmatch(w):
                    continue
                seen.add(w)
                tid = pool.get(w)
                conn.execute("INSERT INTO collection_listing (collection_id, word, kind, term_id, outcome, ai_call_id, run_id, created_by) VALUES (?,?,?,?,?,?,?,'collection-seed')",
                             (cid, w, kind, tid, "unjudged" if tid else "not_in_pool", lst["call_id"], run_id))
                n_listed += 1
    conn.commit()
    return {"collection": cid, "pole": pole, "pole_of_pole": pole2, "real": real, "listed": n_listed}


# ---- asking ------------------------------------------------------------------------------------------------------------------------
def candidates(conn, client, vals: dict, cid: int, limit: int | None) -> list:
    """[(word, term id)] still to judge for the collection: the unjudged listed words first, then the nearest words of the shortlist."""
    core = conn.execute("SELECT t.surface FROM collection c JOIN surface_term t ON t.id=c.core_term_id WHERE c.id=?", (cid,)).fetchone()[0]
    pool = pool_words(conn, vals)
    from . import collectionbuild as cb
    name = {r[0]: r[1] for r in conn.execute("SELECT id, surface FROM surface_term WHERE deleted=0")}
    judged = {name[k[1]] for k in cb.load(conn)["cand"] if k[0] == cid and k[1] in name}
    listed = [r[0] for r in conn.execute("SELECT word FROM collection_listing WHERE collection_id=? AND outcome='unjudged' AND term_id IS NOT NULL AND deleted=0 ORDER BY id", (cid,))]
    vecs = embeddings(client, vals, sorted(set(pool) | {core}))
    near = shortlist(vecs[core], {w: v for w, v in vecs.items() if w != core}, int(vals["collection.shortlist_size"]), judged | {core})
    out, seen = [], set()
    for w in [w for w in listed if w not in judged] + near:
        if w not in seen and w in pool and w != core:
            seen.add(w)
            out.append((w, pool[w]))
    return out[:limit] if limit else out


def judge_candidate(conn, client, vals: dict, cid: int, core: str, pole: str | None, word: str, tid: int) -> dict:
    sub = ("collection", cid)
    r = client.call("judge", "collection.synonym", {"a": core, "b": word}, sub, check=check_relation, step="candidate")
    if r["outcome"] != "answered":
        return {"outcome": r["outcome"], "relation": None}
    rel = r["answer"]["relation"]
    eff = rel
    if rel == "distinct":
        sc = client.call("judge", "collection.score", {"a": core, "b": word}, sub, check=check_score, step="score")
        if sc["outcome"] == "answered" and sc["answer"]["score"] >= vals["collection.score_threshold"]:
            eff = "synonym"
    elif rel == "opposite" and pole:
        client.call("judge", "collection.synonym", {"a": pole, "b": word}, sub, check=check_relation, step="pole_check")
    if eff == "distinct":
        client.call("judge", "collection.associated", {"a": core, "b": word, "bsf": forms_of(conn, tid, word)}, sub, check=check_assoc, step="associated")
    conn.execute("UPDATE collection_listing SET outcome=CASE WHEN kind=? THEN 'bound' ELSE 'refused' END, updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now') "
                 "WHERE collection_id=? AND term_id=? AND outcome='unjudged' AND deleted=0", (eff, cid, tid))
    conn.commit()
    return {"outcome": "answered", "relation": eff}
