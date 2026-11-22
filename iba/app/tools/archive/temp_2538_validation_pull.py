"""temp_2538_validation_pull.py -- TEMPORARY pilot of the validation after stage 4 of a collection: the read-only pull and structural tests (#2538).

Temporary script (governance.scripts_and_routines): it is promoted to a registered library module and step with the full build of the validation,
or retired. The plan is outputs/escalation/2538-validation-step-plan-v8-20261122.md. It writes nothing to any database; run it against a COPY:

    python -m iba.app.tools.temp_2538_validation_pull <db path> <collection name or id>

Scope (principle 1): every live observation related to the collection, by
  a) a live node that carries the collection (ib_node.collection_id),
  b) a live node on a verse of the collection (the verses of the live nodes that carry it),
  c) a live node on a member surface with its own lettered Strong's code (the surface|strong subjects of the S1 word-lexical ledger rows);
  d) its meaning relates to the collection: found by reading, not by this script.
Deleted observations and nodes are excluded. Nodes that reach into other collections are counted (`reach_in`).

Node kinds (cfg_column.use, B:130; lib/layerinner.py): a word node names an occurrence (verse_lexical_id set); a traced node names another
observation (traced_observation_id set) and carries no word column by design. The structural tests:
  - word_missing: a word node lacking verse_reference, verse_lexical_id, surface, strong, morph_code, role or collection_id;
  - subgroup_empty: a word node with no subgroup_id (empty is right where the surface is not placed: reported, not judged);
  - traced_dead: a live traced node whose observation is deleted (principle 9), with whether a valid trace stands in its place;
  - no_node: a live observation with no live node;
  - duplicate_text: two live observations of the same stage with the same text (the exact-text candidate; the meaning test is by reading).
"""

from __future__ import annotations

import sqlite3
import sys
from collections import Counter, defaultdict

WORD_COLUMNS = ("verse_reference", "verse_lexical_id", "surface", "strong", "morph_code", "role", "collection_id")
CHUNK = 400


def _chunks(seq, n=CHUNK):
    seq = list(seq)
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


def _qm(items) -> str:
    return ",".join("?" * len(items))


def collection_id(conn: sqlite3.Connection, name_or_id) -> int:
    if str(name_or_id).isdigit():
        return int(name_or_id)
    row = conn.execute("SELECT id FROM collection WHERE name=? AND deleted=0", (name_or_id,)).fetchone()
    if row is None:
        raise ValueError(f"no live collection named {name_or_id!r}")
    return row[0]


def scope(conn: sqlite3.Connection, cid: int) -> dict:
    a = {r[0] for r in conn.execute(
        "SELECT DISTINCT n.observation_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id AND o.deleted=0 "
        "WHERE n.deleted=0 AND n.collection_id=?", (cid,))}
    verses = [r[0] for r in conn.execute(
        "SELECT DISTINCT n.verse_reference FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id AND o.deleted=0 "
        "WHERE n.deleted=0 AND n.collection_id=? AND n.verse_reference IS NOT NULL", (cid,))]
    b = set()
    for ch in _chunks(verses):
        b |= {r[0] for r in conn.execute(
            f"SELECT DISTINCT n.observation_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id AND o.deleted=0 "
            f"WHERE n.deleted=0 AND n.verse_reference IN ({_qm(ch)})", ch)}
    pairs = []
    for (subj,) in conn.execute("SELECT DISTINCT subject FROM collection_layer_item WHERE collection_id=? AND step='S1' "
                                "AND item='word-lexical' AND deleted=0", (cid,)):
        s, _, k = subj.partition("|")
        if s and k:
            pairs.append((s, k))
    c = set()
    for s, k in pairs:
        c |= {r[0] for r in conn.execute(
            "SELECT DISTINCT n.observation_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id AND o.deleted=0 "
            "WHERE n.deleted=0 AND n.strong=? AND n.surface=?", (k, s))}
    # an observation with no live node cannot be found through nodes (B:130 says there should be none): it is in scope by c) when its own
    # strong is one of the collection's lettered codes; the others are counted and left to the reading (d)
    pair_strongs = {k for _, k in pairs}
    orphans = conn.execute("SELECT o.id, o.strong FROM ib_observation o WHERE o.deleted=0 AND NOT EXISTS "
                           "(SELECT 1 FROM ib_node n WHERE n.observation_id=o.id AND n.deleted=0)").fetchall()
    c |= {oid for oid, st in orphans if st in pair_strongs}
    unplaced = [oid for oid, st in orphans if st not in pair_strongs]
    return {"a": a, "b": b, "c": c, "union": a | b | c, "verses": len(verses), "pairs": len(pairs), "orphans_unplaced": unplaced}


def pull(conn: sqlite3.Connection, cid: int) -> dict:
    sc = scope(conn, cid)
    ids = sorted(sc["union"])
    obs: dict[int, dict] = {}
    for ch in _chunks(ids):
        for r in conn.execute(f"SELECT id, stage, tag, obs_text FROM ib_observation WHERE deleted=0 AND id IN ({_qm(ch)})", ch):
            obs[r[0]] = {"id": r[0], "stage": r[1], "tag": r[2], "text": r[3] or ""}
    nodes = defaultdict(list)
    for ch in _chunks(ids):
        for r in conn.execute(
                f"SELECT id, observation_id, verse_reference, verse_lexical_id, surface, strong, morph_code, role, collection_id, subgroup_id, "
                f"traced_observation_id FROM ib_node WHERE deleted=0 AND observation_id IN ({_qm(ch)})", ch):
            nodes[r[1]].append(r)
    targets = {n[10] for ns in nodes.values() for n in ns if n[10] is not None}
    live = {}
    for ch in _chunks(sorted(targets)):
        for r in conn.execute(f"SELECT id, deleted FROM ib_observation WHERE id IN ({_qm(ch)})", ch):
            live[r[0]] = (r[1] == 0)
    has_nature = any(r[1] == "nature" for r in conn.execute("PRAGMA table_info(ib_observation)"))

    findings = defaultdict(list)
    by_stage, reach_in, missing_cols = Counter(), Counter(), Counter()
    word_nodes = traced_nodes = 0
    for oid, o in obs.items():
        by_stage[o["stage"]] += 1
        ns = nodes.get(oid, [])
        if not ns:
            findings["no_node"].append(oid)
            continue
        for n in ns:
            if n[10] is not None and n[3] is None:                      # a traced node
                traced_nodes += 1
                if not live.get(n[10], False):
                    findings["traced_dead"].append((oid, n[0], n[10]))
                continue
            word_nodes += 1
            miss = [c for c, v in zip(WORD_COLUMNS, (n[2], n[3], n[4], n[5], n[6], n[7], n[8])) if v is None]
            if miss:
                findings["word_missing"].append((oid, n[0], tuple(miss)))
                missing_cols.update(miss)
            if n[9] is None:
                findings["subgroup_empty"].append((oid, n[0]))
            if n[8] is not None and n[8] != cid:
                reach_in[n[8]] += 1
    seen = defaultdict(list)
    for oid, o in obs.items():
        key = (o["stage"], " ".join(o["text"].split()).lower())
        if key[1]:
            seen[key].append(oid)
    findings["duplicate_text"] = [v for v in seen.values() if len(v) > 1]
    dead_obs = {x[0] for x in findings["traced_dead"]}
    no_replacement = [oid for oid in sorted(dead_obs)
                      if not any(n[10] is not None and n[3] is None and live.get(n[10], False) for n in nodes.get(oid, []))]
    return {"collection_id": cid, "scope": {k: len(sc[k]) for k in ("a", "b", "c", "union")}, "verses": sc["verses"], "pairs": sc["pairs"],
            "observations": len(obs), "by_stage": dict(by_stage), "word_nodes": word_nodes, "traced_nodes": traced_nodes,
            "nature_column": has_nature, "missing_columns": dict(missing_cols), "findings": dict(findings),
            "dead_trace_without_replacement": no_replacement, "reach_in": dict(reach_in), "orphans_unplaced": len(sc["orphans_unplaced"])}


def report_lines(res: dict, sample: int = 8) -> list[str]:
    f = res["findings"]
    L = [f"# Validation pull: collection {res['collection_id']}", "",
         f"- scope: a {res['scope']['a']}, b {res['scope']['b']}, c {res['scope']['c']}, union {res['scope']['union']} live observations "
         f"({res['verses']} verses, {res['pairs']} surface|strong pairs); d by reading, not counted",
         f"- word nodes {res['word_nodes']}, traced nodes {res['traced_nodes']}; the `nature` column exists: {res['nature_column']}",
         "", "## Live observations by stored stage", ""]
    L += [f"- {k}: {v}" for k, v in sorted(res["by_stage"].items(), key=lambda kv: -kv[1])]
    L += ["", "## Structural findings", "",
          f"- no live node: {len(f.get('no_node', []))} observations in scope by their own strong; {res['orphans_unplaced']} other live observations "
          f"with no live node are in no collection's scope by structure and are left to the reading (d)",
          f"- word nodes missing a required column: {len(f.get('word_missing', []))} nodes; by column {res['missing_columns']}",
          f"- word nodes with no subgroup_id: {len(f.get('subgroup_empty', []))} (reported, not judged)",
          f"- live traced nodes pointing at a deleted observation: {len(f.get('traced_dead', []))} nodes on "
          f"{len({x[0] for x in f.get('traced_dead', [])})} observations; {len(res['dead_trace_without_replacement'])} have no valid trace in its place",
          f"- exact-text duplicate groups (same stage, same text): {len(f.get('duplicate_text', []))} groups, "
          f"{sum(len(g) for g in f.get('duplicate_text', []))} observations",
          f"- nodes reaching into other collections: {sum(res['reach_in'].values())} nodes in {len(res['reach_in'])} collections"]
    for k in ("no_node", "word_missing", "traced_dead", "duplicate_text"):
        if f.get(k):
            L += ["", f"### sample: {k}", ""] + [f"- {x}" for x in f[k][:sample]]
    return L


if __name__ == "__main__":
    db_path, coll = sys.argv[1], sys.argv[2]
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(report_lines(pull(con, collection_id(con, coll)))))
