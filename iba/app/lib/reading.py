"""reading.py -- the reading process (escalation #2228; on the phases of the analytic process, #2273, design
`outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md`; Analysis_phase_1, #2320, spec
`outputs/escalation/2318-analysis-phase-1-specification-v4-20261027.md`).

A reading is the work on one scope with its objective, served by the escalation that anchors it. Its findings are
written through observationrecord (#2274): one observation per finding, applied by nodes.

Analysis_phase_1 (steps 1 to 3) is the verse understanding:
  open      0.C: one subgroup (or a segment of it); the JSON that indexes the verses (reference, route, progress); the reading
  observe   the next verses in hand: each verse's sheet is read from the tables NOW (its surfaces, its existing observations and
            nodes, the ledger faces) and set in the JSON for the reading to fill
  record    the filled sheets checked whole, then written in one transaction: every surface's evaluation kept in the JSON, every
            existing observation and node accepted, modified (in place) or soft deleted, the new findings written
  check     the Observe gate (at open): every verse done and the evaluations still agree with the live nodes; open -> observed;
            the verses marked analysed
The later steps (claims, narrate, publish, account) are unchanged:
  synergy   D4 claims input: the synergy JSON built from the tables: the reading's findings with their nodes, the
            claims, the matched open items (B:114)
  apply     D4 claims written: claims (strandreading.derive_core), each node's disposition, open items settled
  narrate   D4 narrate written: tellings, holds, blocks rewritten (narrativeregister.rewrite); nodes told
  publish   the touched chapters published from the database, copied to the learning4comfort inbox, byte-identical
  account   the reading from the tables (read-only)

Writes go through narrativeregister.Writer (cfg_write_grant). Every write step validates first and raises Refused
with nothing written.
"""
from __future__ import annotations

import contextlib
import datetime
import hashlib
import io
import json
import pathlib
import re

from . import escalation
from . import narrativecopy
from . import narrativeregister as nr
from . import observationrecord as orec
from . import openitem
from . import strandreading as sr
from . import surfacemap
from . import versecollate as vc
from . import versemeta
from . import versescope as vs
from .db import Db

Refused = nr.Refused
STATES = ("open", "gathered", "observed", "synergised", "narrated", "published")
NOT_SCOPE = ("Label", "Escalation", "Home", "By", "File", "Note", "Objective")
SETTLE = ("closed", "withdrawn", "superseded", "forward", "touched")
PART_MARK = "read in part"      # a gate 2 `touched` response: the item reaches past the reading (#2250 option A)
DISPOSE = ("claim", "held", "data", "context", "withdrawn")   # set at Apply; 'told' is set at Narrate


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ══ lookups ═════════════════════════════════════════════════════════════════════════════════════
def _setting(cfg, key: str):
    v = cfg.required_setting(key)
    return json.loads(v) if isinstance(v, str) else v


def gap_types(cfg) -> dict:
    """{type: {"phase", "records_in", "guide"}} in enum order; every enum value has its entry and no more."""
    spec = _setting(cfg, "reading.gap_types")
    names = cfg.enum("reading_gap_type")
    if set(names) != set(spec):
        raise Refused(f"cfg_enum reading_gap_type {sorted(names)} and cfg_setting reading.gap_types "
                      f"{sorted(spec)} disagree")
    return {n: spec[n] for n in names}


def reading(conn, label: str | None):
    if not (label or "").strip():
        raise Refused("-Label (the reading's name) is required")
    r = conn.execute("SELECT * FROM reading WHERE label=?", (label.strip(),)).fetchone()
    if r is None:
        raise Refused(f"reading {label!r} does not exist (Reading.ps1 -Step Open)")
    return r


def _at(conn, label, state: str):
    r = reading(conn, label)
    if r["state"] != state:
        raise Refused(f"reading {r['label']} is {r['state']}; this step needs it {state}")
    return r


def out_dir(cfg, root: pathlib.Path, label: str) -> pathlib.Path:
    return root / cfg.required_setting("reading.output_dir") / label


def _rel(root: pathlib.Path, p: pathlib.Path) -> str:
    return p.relative_to(root).as_posix() if p.is_relative_to(root) else p.as_posix()


def _path(root: pathlib.Path, path: str | None) -> pathlib.Path:
    f = pathlib.Path(path or "")
    return f if f.is_absolute() else root / f


def _load(root: pathlib.Path, path: str | None, what: str) -> dict:
    f = _path(root, path)
    if not path or not f.is_file():
        raise Refused(f"{what} {path!r} not found")
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise Refused(f"{what} is not valid JSON: {exc}") from exc


def _save(path: pathlib.Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def verse_ids(conn, rid: int) -> list[int]:
    return [r[0] for r in conn.execute("SELECT verse_id FROM reading_verse WHERE reading_id=? ORDER BY verse_id", (rid,))]


def _thread_item(conn, ref: str):
    """'OT-nn.n' -> (thread row, item row), the thread open or not."""
    m = re.fullmatch(r"(OT-\d+)\.(\d+)", (ref or "").strip(), re.I)
    if not m:
        raise Refused(f"{ref!r} is not a thread item (OT-nn.n)")
    t = conn.execute("SELECT * FROM escalation e WHERE type='thread' AND CAST(substr(alias, 4) AS INTEGER)=? AND "
                     "version=(SELECT MAX(version) FROM escalation x WHERE x.id=e.id)",
                     (int(m.group(1)[3:]),)).fetchone()
    it = t and conn.execute("SELECT * FROM escalation_thread_item WHERE escalation_id=? AND item_no=?",
                            (t["id"], int(m.group(2)))).fetchone()
    if not it:
        raise Refused(f"thread item {ref} does not exist")
    return t, it


def _gate_fail(r, name: str, gaps: list[str]):
    raise Refused("\n  ".join([f"reading {r['label']} is not past the {name} gate ({len(gaps)} gap(s)):"] + gaps[:60]
                              + ([f"... and {len(gaps) - 60} more"] if len(gaps) > 60 else [])))


# ══ the verse loop (Analysis_phase_1, #2320; spec outputs/escalation/2318-analysis-phase-1-specification-v4-20261027.md) ═══
# The JSON is the index of the verses in scope (reference, route, progress, the evaluation of the surfaces). The surfaces,
# the existing observations and the nodes are read from the tables when a verse is worked, never copied into the JSON.
SEGMENT_PARAMS = ("Surface", "Verse")
NOT_FOR_OPEN = ("Cluster", "Strand", "Word", "Strong", "Chapter", "Section", "Claim", "Observation", "Item", "Thread",
                "OnlyStrong", "File")


def _setting_loop(cfg) -> dict:
    return orec.loop_setting(cfg)


def _norm(s) -> str:
    return (s or "").strip().lower()


def _index_path(cfg, root: pathlib.Path, label: str) -> pathlib.Path:
    return out_dir(cfg, root, label) / f"{label}.json"


def _save_atomic(path: pathlib.Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    tmp.replace(path)


def _index(cfg, root: pathlib.Path, r) -> tuple[pathlib.Path, dict]:
    path = _path(root, r["gap_file"])
    data = _load(root, r["gap_file"], "the scope JSON")
    if data.get("reading_id") != r["id"]:
        raise Refused(f"the scope JSON {r['gap_file']} is not reading {r['label']}'s")
    return path, data


def open_(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path, file_request: dict | None) -> str:
    """-Label -Escalation -Objective -Subgroup [-Surface a,b | -Verse "Mat 7:8; ..."] [-Reviewed]: the scope, indexed in
    the JSON (spec 1.1 to 1.8). Exactly one subgroup, or a segment of it; the home is the subgroup; no -Home."""
    conn = cfg.conn
    loop = _setting_loop(cfg)
    label = (p.get("Label") or "").strip()
    if not label or label != label.lower() or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", label):
        raise Refused("-Label is the reading's name, lowercase-hyphenated (e.g. m21-asking)")
    if conn.execute("SELECT 1 FROM reading WHERE label=?", (label,)).fetchone():
        raise Refused(f"reading {label} already exists")
    objective = (p.get("Objective") or "").strip()
    if len(objective) < loop["min_reason_chars"]:
        raise Refused("-Objective is the scope's objective, in words (0.C: it defines the home of what is recorded)")
    try:
        eid = int(str(p.get("Escalation") or "").lstrip("#"))
    except ValueError:
        raise Refused("-Escalation (the task or issue that anchors the reading) is required") from None
    e = conn.execute("SELECT type, state FROM escalation e WHERE id=? AND version=(SELECT MAX(version) FROM escalation "
                     "x WHERE x.id=e.id)", (eid,)).fetchone()
    if e is None or e["type"] not in ("task", "issue") or e["state"] in escalation.state_group(conn, "terminal"):
        raise Refused(f"escalation #{eid} is not an open task or issue")
    if (p.get("Home") or "").strip():
        raise Refused("-Home is not given: the home is the subgroup, and its cluster is the subgroup's (spec 1.2)")
    other = [k for k in NOT_FOR_OPEN if (p.get(k) or "").strip()]
    if other:
        raise Refused(f"Analysis_phase_1 takes one -Subgroup (with -Surface or -Verse to segment it), not -{', -'.join(other)}")
    subs = vs._split(p.get("Subgroup"))
    if len(subs) != 1:
        raise Refused("-Subgroup: exactly one subgroup (spec 1.1)")
    sg = conn.execute("SELECT subgroup_code, cluster_code, kind FROM cluster_subgroup WHERE subgroup_code=? AND "
                      "coalesce(delete_flagged,0)=0", (subs[0],)).fetchone()
    if sg is None:
        raise Refused(f"subgroup {subs[0]!r} is not a live cluster subgroup")
    if sg["kind"] == "qualifier":
        raise Refused(f"subgroup {sg['subgroup_code']} is a qualifier group and is never a home (spec 1.2)")
    home = sg["cluster_code"]
    unmapped = surfacemap.reading_refusal(conn, home)
    if unmapped:
        raise Refused(unmapped)
    request = {"subgroup": [sg["subgroup_code"]], "home": [sg["subgroup_code"]]}
    if (p.get("Reviewed") or "").strip():
        request["reviewed"] = p["Reviewed"].strip()
    try:
        scope = vs.resolve(cfg, request)
    except vs.ScopeError as exc:
        raise Refused(str(exc)) from exc
    verses = scope["verses"]
    segment = None
    surf = [_norm(x) for x in vs._split(p.get("Surface"))]
    if surf:
        verses = [v for v in verses if any(o.get("in_scope") and _norm(o["surface"]) in surf for o in v["occurrences"])]
        segment = {"surfaces": surf}
    if (p.get("Verse") or "").strip():
        want = {x.verse_id for x in nr.parse_refs(p["Verse"], nr.VerseIndex(cfg)) if x.verse_id}
        verses = [v for v in verses if v["verse_id"] in want]
        segment = {**(segment or {}), "verses": p["Verse"].strip()}
    if not verses:
        raise Refused("the scope holds no verse" + (" after the segment" if segment else ""))
    folder = out_dir(cfg, root, label)
    path = folder / f"{label}.json"
    if path.exists():
        raise Refused(f"{_rel(root, path)} is already on disk")

    def go():
        rid = w.insert("reading", {"label": label, "escalation_id": eid, "home_cluster": home, "objective": objective,
                                   "request": json.dumps(scope["request"], ensure_ascii=False),
                                   "gap_file": _rel(root, path), "note": p.get("Note"), "run_id": run_id})
        # reading_verse: still written because the claims steps read it (not read by Analysis_phase_1; #2320 flag)
        for v in verses:
            w.insert("reading_verse", {"reading_id": rid, "verse_id": v["verse_id"],
                                       "routes": json.dumps(v["routes"], ensure_ascii=False)})
        return rid
    rid = nr._atomic(conn, go)
    data = {"reading": label, "reading_id": rid, "escalation": eid, "subgroup": sg["subgroup_code"], "home": home,
            "segment": segment, "objective": objective, "opened": _now(),
            "how": "The index of the verses in scope. Reading.ps1 -Step Observe puts the next verses in hand (a sheet each: the "
                   "surfaces, the existing observations and nodes, the ledger faces, read from the tables then); fill the "
                   "sheets; Reading.ps1 -Step Record writes them and marks the verses done; Reading.ps1 -Step Check passes the "
                   "gate when every verse is done.",
            "counts": {"verses": len(verses), "done": 0},
            "verses": [{"verse": v["reference"], "osis": v["osis"], "verse_id": v["verse_id"], "routes": v["routes"],
                        "status": "waiting"} for v in verses]}
    _save_atomic(path, data)
    return (f"reading {label} opened (#{eid}, subgroup {sg['subgroup_code']}, home {home}): {len(verses)} verse(s) indexed"
            + (f", segment {segment}" if segment else "") + f"\n  -> {_rel(root, path)}")


# ── the sheet of one verse: read from the tables when the verse is worked ─────────────────────────
def _sheets(cfg, conn, items: list[dict]) -> dict:
    """{verse_id: sheet} for the verses in hand, with set-based queries over the batch (B:71)."""
    loop = _setting_loop(cfg)
    fw = _setting(cfg, "reading.focus_words")
    never = _setting(cfg, "reading.non_characteristic_strongs")
    ids = [it["verse_id"] for it in items]
    J = json.dumps(ids)
    osis_of = {it["verse_id"]: it["osis"] for it in items}
    rows = conn.execute("SELECT id, verse_id, position, surface, strong, morph_code, testament, is_negator FROM verse_lexical "
                        "WHERE deleted=0 AND verse_id IN (SELECT value FROM json_each(?)) ORDER BY verse_id, position, id",
                        (J,)).fetchall()
    strongs = sorted({r["strong"] for r in rows})
    SJ = json.dumps(strongs)
    clusters: dict = {}
    for s, cl in conn.execute("SELECT strong, cluster_code FROM cluster_strong WHERE deleted=0 AND strong IN "
                              "(SELECT value FROM json_each(?)) ORDER BY cluster_code", (SJ,)):
        clusters.setdefault(s, []).append(cl)
    subs: dict = {}
    for s, surface, sgc in conn.execute(
            "SELECT s.strong, s.surface, g.subgroup_code FROM surface_subgroup s JOIN cluster_subgroup g ON "
            "g.id=s.cluster_subgroup_id WHERE s.deleted=0 AND s.strong IN (SELECT value FROM json_each(?)) "
            "ORDER BY g.subgroup_code", (SJ,)):
        subs.setdefault((s, surface), []).append(sgc)
    by_verse: dict = {i: [] for i in ids}
    for r in rows:
        by_verse[r["verse_id"]].append(r)
    sheets = {}
    for it in items:
        vid = it["verse_id"]
        groups: dict = {}
        for r in by_verse[vid]:
            key = (r["strong"], _norm(r["surface"]))
            g = groups.get(key)
            if g is None:
                prefix = ((r["morph_code"] or "")[:2] if r["testament"] == "OT" else (r["morph_code"] or "").split("-")[0])
                hint = []
                if prefix in fw["function_word_morph"].get(r["testament"], []):
                    hint.append("grammar by its morph")
                if r["is_negator"] or any(t in clusters.get(r["strong"], []) for t in fw["keep_tags"]):
                    hint.append("negator or connective")
                if any(c.startswith("M") for c in clusters.get(r["strong"], [])):
                    hint.append("M-coded")
                if r["strong"] in never:
                    hint.append("never a characteristic: " + never[r["strong"]])
                g = groups[key] = {"occurrences": [], "word": f"{r['surface']} ({r['strong']})", "strong": r["strong"],
                                   "surface": r["surface"], "morph": r["morph_code"], "position": r["position"],
                                   "clusters": clusters.get(r["strong"], []),
                                   "subgroups": subs.get((r["strong"], _norm(r["surface"])), []), "hint": hint,
                                   "evaluation": None}
            g["occurrences"].append(r["id"])
        sheets[vid] = {"surfaces": list(groups.values())}
    # the existing observations and nodes on the verses (every stage, not filtered by subgroup)
    OJ = json.dumps([it["osis"] for it in items])
    obs: dict = {}
    for o in conn.execute("SELECT DISTINCT o.* FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE "
                          "o.status<>'withdrawn' AND n.verse_reference IN (SELECT value FROM json_each(?)) AND "
                          "(n.disposition IS NULL OR n.disposition<>'withdrawn') ORDER BY o.id", (OJ,)):
        obs[o["id"]] = o
    nodes: dict = {}
    for n in conn.execute("SELECT n.* FROM ib_node n WHERE n.verse_reference IN (SELECT value FROM json_each(?)) AND "
                          "(n.disposition IS NULL OR n.disposition<>'withdrawn') ORDER BY n.observation_id, n.id", (OJ,)):
        nodes.setdefault((n["observation_id"], n["verse_reference"]), []).append(n)
    elsewhere = {r[0]: r[1] for r in conn.execute(
        "SELECT observation_id, count(*) FROM ib_node WHERE observation_id IN (SELECT value FROM json_each(?)) AND "
        "(verse_reference NOT IN (SELECT value FROM json_each(?)) OR verse_reference IS NULL) AND "
        "(disposition IS NULL OR disposition<>'withdrawn') GROUP BY observation_id", (json.dumps(sorted(obs)), OJ))}
    ledger: dict = {}
    for h in conn.execute("SELECT h.id, h.verse_id, s.code, h.strong, h.surface, h.face FROM reading_strand_hit h JOIN "
                          "reading_strand s ON s.id=h.strand_id WHERE h.verse_id IN (SELECT value FROM json_each(?)) AND "
                          "coalesce(h.face,'')<>'' AND h.observation_id IS NULL", (J,)):
        ledger.setdefault(h["verse_id"], []).append(
            {"hit": h["id"], "strand": h["code"], "word": f"{h['surface']} ({h['strong']})", "face": h["face"],
             "link": None})
    for it in items:
        vid, osis = it["verse_id"], it["osis"]
        occ_by_key = {(g["strong"], _norm(g["surface"])): g["occurrences"] for g in sheets[vid]["surfaces"]}
        occ_ids = {i for g in sheets[vid]["surfaces"] for i in g["occurrences"]}
        existing = []
        for (oid, ref), ns in nodes.items():
            if ref != osis or oid not in obs:      # a node of a withdrawn observation is not shown
                continue
            o = obs[oid]
            nl = []
            for n in ns:
                if n["verse_lexical_id"] in occ_ids:
                    counts = n["verse_lexical_id"]
                else:
                    same = occ_by_key.get((n["strong"], _norm(n["surface"]))) if n["surface"] else None
                    counts = same[0] if same and len(same) == 1 else None
                suggest = {}
                if counts and n["verse_lexical_id"] is None:
                    suggest["verse_lexical_id"] = counts
                if counts and not n["cluster_subgroup_code"] and n["strong"]:
                    code = orec.subgroup_code(conn, n["cluster_code"], n["strong"], n["surface"])
                    if code:
                        suggest["cluster_subgroup_code"] = code
                nl.append({"node": n["id"], "word": f"{n['surface']} ({n['strong']})", "role": n["role"],
                           "occurrence": n["verse_lexical_id"], "counts_for": counts, "cluster": n["cluster_code"],
                           "subgroup": n["cluster_subgroup_code"], "reading_id": n["reading_id"],
                           "suggest": suggest or None, "action": None})
            existing.append({"observation": oid, "stage": o["stage"], "kind": o["tag"], "text": o["obs_text"],
                             "meaning": o["meaning"], "implication": o["implication"], "basis": o["basis"],
                             "route": o["route"], "parts": json.loads(o["parts"]) if o["parts"] else None,
                             "nodes_on_other_verses": elsewhere.get(oid, 0), "nodes": nl, "action": None})
        sheets[vid].update({
            "passage": _passage(conn, osis, loop["passage_window"]), "existing": existing,
            "ledger_faces": ledger.get(vid, []), "findings": [], "fill_nodes": False, "drop_non_relevant_nodes": False,
            "how": "Evaluate every surface: evaluation {\"result\": \"relevant\" (the characteristic, or a qualifier of it) | "
                   "\"bears_on\" (the object, party or outward act of a relevant act: a node of that act's observation) | "
                   "\"not_relevant\", \"reason\": \"...\"} (reason: the tests of the lexical work; a surface with no "
                   "inner-being role gets no observation). `drop_non_relevant_nodes`: true soft deletes every existing node on a "
                   "not_relevant surface. Check every existing observation: "
                   "action {\"action\": \"accept\"|\"modify\"|\"delete\", \"reason\": \"...\" (modify, delete), \"set\": {...} "
                   "(modify), \"nodes\": [{\"node\": id, \"action\": ..., \"reason\": ..., \"set\": {...}}]}; \"fill_nodes\": true "
                   "applies every node `suggest` as a modify. A new finding goes in `findings` (observationrecord's shape, plus "
                   "`parts`; each node names its `occurrence` id and a `role` from reading.node_roles). `ledger_faces[].link`: "
                   "{\"observation\": id} or {\"reason\": \"...\"}."})
        sheets[vid]["verse"] = it["verse"]
        sheets[vid]["osis"] = osis
        sheets[vid]["text"] = conn.execute("SELECT text FROM verse WHERE id=?", (vid,)).fetchone()[0]
    return sheets


def observe(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    """-Label [-Count n] [-Verse ref]: put the next verses in hand: their sheets are read from the tables now and set in the
    JSON for the reading to fill."""
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "open")
    path, data = _index(cfg, root, r)
    loop = _setting_loop(cfg)
    n = int(p.get("Count") or loop["verses_per_sheet"])
    want = None
    if (p.get("Verse") or "").strip():
        want = {x.verse_id for x in nr.parse_refs(p["Verse"], nr.VerseIndex(cfg)) if x.verse_id}
    hand = [v for v in data["verses"] if v["status"] == "in_hand"]
    pick = [v for v in data["verses"] if v["status"] == "waiting" and (want is None or v["verse_id"] in want)]
    room = max(0, n - len(hand)) if want is None else len(pick)
    pick = pick[:room]
    if not hand and not pick:
        return f"reading {r['label']}: no verse waiting or in hand ({data['counts']['done']} done)"
    if pick:
        sheets = _sheets(cfg, conn, pick)      # new sheets only: a sheet already in hand keeps what was filled in it
        for v in pick:
            v["status"] = "in_hand"
            v["sheet"] = sheets[v["verse_id"]]
    batch = hand + pick
    built = _now()
    data["built_at"] = built
    data["counts"]["done"] = sum(1 for v in data["verses"] if v["status"] == "done")
    _save_atomic(path, data)
    nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {"observe_file": _rel(root, path),
                                                                    "observe_built_at": built, "run_id": run_id}))
    return (f"reading {r['label']}: {len(batch)} verse(s) in hand ({', '.join(v['verse'] for v in batch)}; "
            f"{len(pick)} new sheet(s)); "
            f"{data['counts']['done']} of {data['counts']['verses']} done\n  sheets in {_rel(root, path)}")


def _validate_sheet(cfg, conn, v: dict, errors: list) -> dict | None:
    """Check one filled sheet whole; returns the plan (what to write), or None with the errors added."""
    loop = _setting_loop(cfg)
    groups_roles = orec.node_role_groups(cfg)
    roles = orec.node_roles(cfg)
    minc = loop["min_reason_chars"]
    sh = v["sheet"]
    at = v["verse"]
    ok_reason = lambda s: len((s or "").strip()) >= minc
    # surfaces
    rel_groups, bear_groups, non_groups = [], [], []
    for k, g in enumerate(sh["surfaces"]):
        ev = g.get("evaluation")
        if not isinstance(ev, dict) or ev.get("result") not in loop["evaluation_results"] or not ok_reason(ev.get("reason")):
            errors.append(f"{at}: surface {g['word']} needs an evaluation {{\"result\": one of {loop['evaluation_results']}, "
                          f"\"reason\": ...}} (a reason of {minc} characters or more)")
            continue
        {"relevant": rel_groups, "bears_on": bear_groups, "not_relevant": non_groups}[ev["result"]].append(g)
    occ_group = {i: g for g in sh["surfaces"] for i in g["occurrences"]}
    # existing observations
    plan = {"obs": [], "nodes": [], "fill": [], "links": [], "findings": []}
    live_after = []        # (occurrence group id, role) of nodes that stay
    for e in sh["existing"]:
        a = e.get("action")
        if not isinstance(a, dict) or a.get("action") not in loop["existing_actions"]:
            errors.append(f"{at}: observation {e['observation']} needs an action {loop['existing_actions']}")
            continue
        if a["action"] in ("modify", "delete") and not ok_reason(a.get("reason")):
            errors.append(f"{at}: observation {e['observation']}: a {a['action']} needs its reason ({minc} characters or more)")
            continue
        if a["action"] == "modify" and not a.get("set") and not a.get("nodes"):
            errors.append(f"{at}: observation {e['observation']}: a modify names what is set (`set`) or the nodes changed")
            continue
        plan["obs"].append((e["observation"], a))
        deleted_obs = a["action"] == "delete"
        by_node = {x.get("node"): x for x in (a.get("nodes") or []) if isinstance(x, dict)}
        for n in e["nodes"]:
            na = by_node.get(n["node"])
            role, gone = n["role"], deleted_obs
            if not na and sh.get("drop_non_relevant_nodes") and not deleted_obs and n["counts_for"] in occ_group and any(
                    occ_group[n["counts_for"]] is x for x in non_groups):
                na = {"action": "delete", "reason": "the surface has no inner-being role (its evaluation, #2320)"}
            if na:
                if na.get("action") not in loop["existing_actions"]:
                    errors.append(f"{at}: node {n['node']} needs an action {loop['existing_actions']}")
                    continue
                if na["action"] in ("modify", "delete") and not ok_reason(na.get("reason")):
                    errors.append(f"{at}: node {n['node']}: a {na['action']} needs its reason")
                    continue
                if na["action"] == "delete":
                    gone = True
                if na["action"] == "modify":
                    role = (na.get("set") or {}).get("role", role)
                plan["nodes"].append((n["node"], na))
            elif sh.get("fill_nodes") and n["suggest"] and not deleted_obs:
                plan["fill"].append((n["node"], n["suggest"]))
            if not gone and n["counts_for"] in occ_group and role is not None:
                live_after.append((id(occ_group[n["counts_for"]]), role))
    for f in sh.get("findings") or []:
        plan["findings"].append(f)
        for nd in (f.get("nodes") or []):
            if isinstance(nd, dict) and nd.get("strong") and nd.get("occurrence") not in occ_group:
                errors.append(f"{at}: a finding node names the occurrence id of the word in this verse (`occurrence`)")
            g = occ_group.get(nd.get("occurrence")) if isinstance(nd, dict) else None
            if g is not None and nd.get("role"):
                live_after.append((id(g), nd["role"]))
    for hit in sh.get("ledger_faces") or []:
        lk = hit.get("link")
        if lk is None:
            continue
        if not (isinstance(lk, dict) and ((lk.get("observation") and conn.execute(
                "SELECT 1 FROM ib_observation WHERE id=? AND status<>'withdrawn'", (lk["observation"],)).fetchone())
                or ok_reason(lk.get("reason")))):
            errors.append(f"{at}: ledger face {hit['hit']}: link is {{\"observation\": a live id}} or {{\"reason\": ...}}")
        else:
            plan["links"].append((hit["hit"], lk))
    # coverage (spec 4.4): relevant -> a live node with a characteristic or qualifier role; bears_on -> a live node with an
    # object, relational target or enactment role; not_relevant -> no live node at all
    def has(g, kind):
        return any(gid == id(g) and role in groups_roles[kind] for gid, role in live_after)
    for g in rel_groups:
        if not has(g, "relevant"):
            errors.append(f"{at}: {g['word']} is relevant, but no live node with a role from {groups_roles['relevant']} names it")
    for g in bear_groups:
        if not has(g, "bears_on"):
            errors.append(f"{at}: {g['word']} bears on the act, but no live node with a role from {groups_roles['bears_on']} "
                          f"names it")
    for g in non_groups:
        if any(gid == id(g) for gid, _ in live_after):
            errors.append(f"{at}: {g['word']} has no inner-being role (evaluation) but a node still names it: delete the "
                          f"node, set `drop_non_relevant_nodes`, or change the evaluation")
    return plan


def _filled(sh: dict) -> bool:
    return (any(g.get("evaluation") for g in sh["surfaces"]) or any(e.get("action") for e in sh["existing"])
            or bool(sh.get("findings")) or any(h.get("link") for h in sh.get("ledger_faces") or []))


def record(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    """-Label: write the filled sheets of the verses in hand: evaluations kept in the JSON, existing observations and nodes
    accepted, modified or soft deleted, new findings written -- all or nothing; the verses written are marked done."""
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "open")
    path, data = _index(cfg, root, r)
    if data.get("built_at") != r["observe_built_at"] and r["observe_built_at"]:
        raise Refused("the JSON was changed after Observe built the sheets: run Observe")
    hand = [v for v in data["verses"] if v["status"] == "in_hand" and v.get("sheet")]
    todo = [v for v in hand if _filled(v["sheet"])]
    if not todo:
        raise Refused("nothing to record: no verse in hand has a filled sheet (Reading.ps1 -Step Observe)")
    errors, quotes = [], []
    plans = {}
    for v in todo:
        pl = _validate_sheet(cfg, conn, v, errors)
        if pl is not None:
            plans[v["verse_id"]] = pl
    # new findings: checked by observationrecord across the whole batch (unique keys)
    specs = []
    for v in todo:
        for k, f in enumerate((plans.get(v["verse_id"]) or {}).get("findings", [])):
            if isinstance(f, dict):
                specs.append((f"{v['verse']} findings[{k}] ({f.get('key')})", {**f, "key": f"{v['verse_id']}:{f.get('key')}"}))
    fplan = orec.check(cfg, specs, errors, quotes) if specs else []
    if errors or quotes:
        raise Refused("\n  ".join(["the sheets are not recorded:"] + errors + (
            ["quotation(s) not found in the ESV text:"] + quotes if quotes else [])))
    loop = _setting_loop(cfg)

    def go():
        _grant_findings(w)
        w._grant("reading_strand_hit")
        summary = {}
        for v in todo:
            pl = plans[v["verse_id"]]
            cnt = {"accepted": 0, "modified": 0, "deleted": 0, "nodes_modified": 0, "nodes_deleted": 0, "links": 0}
            for oid, a in pl["obs"]:
                if a["action"] == "accept":
                    cnt["accepted"] += 1
                elif a["action"] == "delete":
                    orec.withdraw_observation(conn, oid, a["reason"].strip(), r["id"], run_id, w.who)
                    cnt["deleted"] += 1
                else:
                    if a.get("set"):
                        orec.modify_observation(cfg, conn, oid, a["set"], a["reason"].strip(), r["id"], run_id, w.who)
                    cnt["modified"] += 1
            for nid, na in pl["nodes"]:
                if na["action"] == "delete":
                    orec.set_disposition(conn, nid, "withdrawn", na["reason"].strip(), r["id"], run_id, w.who)
                    cnt["nodes_deleted"] += 1
                elif na["action"] == "modify":
                    orec.modify_node(cfg, conn, nid, na.get("set") or {}, na["reason"].strip(), r["id"], run_id, w.who)
                    cnt["nodes_modified"] += 1
            for nid, sug in pl["fill"]:
                orec.modify_node(cfg, conn, nid, sug, "completed from verse_lexical and surface_subgroup when the verse was "
                                 "worked (#2308 D2)", r["id"], run_id, w.who)
                cnt["nodes_modified"] += 1
            for hid, lk in pl["links"]:
                if lk.get("observation"):
                    w.update("reading_strand_hit", {"id": hid}, {"observation_id": lk["observation"], "run_id": run_id})
                else:
                    w.update("reading_strand_hit", {"id": hid}, {"reason": lk["reason"].strip(), "run_id": run_id})
                cnt["links"] += 1
            summary[v["verse_id"]] = cnt
        written = orec.write(conn, fplan, r["id"], run_id) if fplan else {}
        w.update("reading", {"id": r["id"]}, {"run_id": run_id})
        return summary, written
    summary, written = nr._atomic(conn, go)
    at = _now()
    for v in todo:
        sh = v.pop("sheet")
        v["status"] = "done"
        v["result"] = {
            "at": at, "run_id": run_id, "existing": summary[v["verse_id"]],
            "surfaces": [{"word": g["word"], "occurrences": g["occurrences"], "result": g["evaluation"]["result"],
                          "reason": g["evaluation"]["reason"].strip()} for g in sh["surfaces"]],
            "written": {"observations": [x["observation"] for k, x in written.items() if k.startswith(f"{v['verse_id']}:")],
                        "nodes": sum(len(x["nodes"]) for k, x in written.items() if k.startswith(f"{v['verse_id']}:"))}}
    data["counts"]["done"] = sum(1 for x in data["verses"] if x["status"] == "done")
    data.pop("built_at", None)
    _save_atomic(path, data)
    nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {"observe_built_at": None, "run_id": run_id}))
    new_o = sum(1 for x in written.values() if x["new"])
    return (f"reading {r['label']}: {len(todo)} verse(s) done ({data['counts']['done']} of {data['counts']['verses']}); "
            f"{sum(s['accepted'] for s in summary.values())} accepted, {sum(s['modified'] for s in summary.values())} "
            f"modified, {sum(s['deleted'] for s in summary.values())} deleted; {new_o} finding(s) new, "
            f"{sum(len(x['nodes']) for x in written.values())} node(s)\n  evaluations and results in {_rel(root, path)}")


def gate_observe(cfg, root: pathlib.Path, r) -> list[str]:
    """The Observe gate (spec 4.4), checked from the JSON and the tables: every verse done; every surface evaluated in the
    JSON still agrees with the live nodes (relevant: a characteristic or qualifier node; bears_on: an object, relational
    target or enactment node; not_relevant: no live node); every node of this reading holds its role."""
    conn = cfg.conn
    groups_roles = orec.node_role_groups(cfg)
    try:
        _, data = _index(cfg, root, r)
    except Refused as exc:
        return [str(exc)]
    out = []
    for v in data["verses"]:
        if v["status"] != "done":
            out.append(f"{v['verse']}: {v['status']}, not done")
            continue
        occ_nodes: dict = {}
        for n in conn.execute("SELECT n.verse_lexical_id, n.strong, n.surface, n.role FROM ib_node n JOIN ib_observation o "
                              "ON o.id=n.observation_id WHERE n.verse_reference=? AND o.status<>'withdrawn' AND "
                              "(n.disposition IS NULL OR n.disposition<>'withdrawn')", (v["osis"],)):
            occ_nodes.setdefault(n["verse_lexical_id"], []).append(n)
        for g in v["result"]["surfaces"]:
            nodes = [n for i in g["occurrences"] for n in occ_nodes.get(i, [])]
            res = g["result"]
            if res in groups_roles and not any(n["role"] in groups_roles[res] for n in nodes):
                out.append(f"{v['verse']} {g['word']}: {res}, but no live node with a role from {groups_roles[res]} names it")
            if res == "not_relevant" and nodes:
                out.append(f"{v['verse']} {g['word']}: no inner-being role, but a live node names it")
    for n in conn.execute("SELECT id, observation_id FROM ib_node WHERE reading_id=? AND strong IS NOT NULL AND "
                          "verse_reference IS NOT NULL AND role IS NULL", (r["id"],)):
        out.append(f"node {n['id']} (observation {n['observation_id']}): no role")
    return out


# ── helpers the claims steps use (open items, grants, the passage) ──────────────────────────────────
class _ReadingItems:
    """New open items (D-b): the Open-Item.ps1 -Action Add shape, through openitem.add."""

    def __init__(self, cfg, w):
        self.cfg, self.w = cfg, w

    def check(self, spec, at: str, errors: list):
        if not isinstance(spec, dict) or not spec.get("thread"):
            errors.append(f"{at}: a new item is the Open-Item add shape (thread, origin, anchor, a target, read_for, "
                          f"why, comes_back_when)")
            return None
        try:
            openitem._validate(self.cfg, openitem.spec_from(spec), vs.Resolver(self.cfg))
            openitem.resolve_target(self.cfg, openitem.spec_from(spec))
        except (openitem.ItemError, vs.ScopeError) as exc:
            errors.append(f"{at}: {exc}")
            return None
        return spec

    def raise_(self, spec, where: str) -> str:
        try:
            out = openitem.add(self.cfg, Db(self.cfg), self.w, openitem.spec_from(spec), self.w.who)
        except (openitem.ItemError, vs.ScopeError, ValueError) as exc:
            raise Refused(f"{where}: the open item could not be added: {exc}") from exc
        return out.split(" ", 1)[0]


def _grant_findings(w: nr.Writer) -> None:
    for t in ("ib_observation", "ib_node", "ib_observation_change"):
        w._grant(t)


def _passage(conn, osis: str, window: int = 2) -> list[dict]:
    book, ch, v = osis.split(".")
    want = [f"{book}.{ch}.{n}" for n in range(max(1, int(v) - window), int(v) + window + 1)]
    rows = {r[0]: r for r in conn.execute("SELECT osisId, reference, text FROM verse WHERE deleted=0 AND osisId IN "
                                          f"({','.join('?' * len(want))})", want)}
    return [{"verse": rows[o][1], "text": rows[o][2]} for o in want if o in rows]


def _item_exists(conn, ref: str) -> bool:
    ref = str(ref or "")
    kind = "escalation" if ref.startswith("#") else "thread item" if "." in ref else "thread"
    return bool(ref) and nr._escalation_exists(conn, kind, ref)


# ══ synergy and apply (D4 claims, with 0.GAP post) ══════════════════════════════════════════════
def scope_observations(conn, rid: int) -> list:
    return conn.execute(
        "SELECT DISTINCT o.* FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id JOIN verse v ON "
        "v.osisId=n.verse_reference JOIN reading_verse rv ON rv.verse_id=v.id WHERE rv.reading_id=? AND "
        "o.status<>'withdrawn' ORDER BY o.id", (rid,)).fetchall()


def reading_nodes(conn, rid: int) -> list:
    """The live nodes this reading applied, of live findings."""
    return conn.execute("SELECT n.* FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.reading_id=? "
                        "AND o.status<>'withdrawn' AND (n.disposition IS NULL OR n.disposition<>'withdrawn') "
                        "ORDER BY n.observation_id, n.id", (rid,)).fetchall()


def scope_claims(conn, rid: int, obs_ids: list[int]) -> list:
    return conn.execute(
        f"SELECT DISTINCT c.* FROM narrative_claim c JOIN narrative_claim_source cs ON cs.claim_id=c.id WHERE "
        f"c.status IN ('current', 'held') AND (cs.verse_id IN (SELECT verse_id FROM reading_verse WHERE reading_id=?) "
        f"OR cs.observation_id IN ({','.join('?' * len(obs_ids)) or 'NULL'})) ORDER BY c.id",
        (rid, *obs_ids)).fetchall()


def _carried(conn, oid: int) -> bool:
    return conn.execute("SELECT 1 FROM narrative_claim_source cs JOIN narrative_claim c ON c.id=cs.claim_id WHERE "
                        "cs.observation_id=? AND c.status='current'", (oid,)).fetchone() is not None


def _reaches_past(cfg, row, vids) -> bool:
    """True when a thread item's target holds a verse outside the reading's verses (#2250): it may then be settled
    as read in part. A worded item's target is its verses; any other kind is resolved as Verse-Scope -Item does."""
    if row["kind"] == "scope":
        target = {x[0] for x in cfg.conn.execute(
            "SELECT verse_id FROM escalation_thread_item_verse WHERE item_id=? AND deleted=0", (row["id"],))}
    else:
        res = vs.Resolver(cfg)
        res._item(row["kind"], (row["value"] or "").strip(), "item")
        target = set(res.routes)
    return bool(target - set(vids))


def _read_in_part(conn, row, label: str) -> bool:
    return conn.execute("SELECT 1 FROM escalation_thread_item_response WHERE item_id=? AND kind='touched' AND text "
                        "LIKE ?", (row["id"], f"%(reading {label}, claims gate, {PART_MARK})%")).fetchone() is not None


def _mine(conn, rid: int) -> list[int]:
    return sorted({n["observation_id"] for n in reading_nodes(conn, rid)} |
                  {o["id"] for o in scope_observations(conn, rid)})


def synergy(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    """The synergy JSON, built from the tables (B:114): the reading's findings with their nodes, the claims on the
    scope, the open items matched to it, each with the field to fill."""
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "observed")
    vids = verse_ids(conn, r["id"])
    nodes = reading_nodes(conn, r["id"])
    F, by_obs = [], {}
    for n in nodes:
        by_obs.setdefault(n["observation_id"], []).append(n)
    for oid, ns in by_obs.items():
        o = conn.execute("SELECT * FROM ib_observation WHERE id=?", (oid,)).fetchone()
        cl = [x[0] for x in conn.execute("SELECT DISTINCT c.claim_ref FROM narrative_claim_source cs JOIN narrative_claim "
                                         "c ON c.id=cs.claim_id WHERE cs.observation_id=? AND c.status='current'", (oid,))]
        F.append({"observation": oid, "kind": o["tag"], "text": o["obs_text"], "meaning": o["meaning"],
                  "carried_by": cl, "nodes": [{"node": n["id"], "verse": n["verse_reference"], "strong": n["strong"],
                                               "role": n["role"], "disposition": n["disposition"]} for n in ns],
                  "dispose": None})
    claims = scope_claims(conn, r["id"], _mine(conn, r["id"]))
    C = [{"claim": c["claim_ref"], "status": c["status"], "text": c["claim_text"],
          "rests_on_findings": bool(conn.execute("SELECT 1 FROM narrative_claim_source WHERE claim_id=? AND "
                                                 "observation_id IS NOT NULL", (c["id"],)).fetchone()),
          "edit": None, "withdraw": None} for c in claims]
    gap = _load(root, r["gap_file"], "the pre-gap JSON")
    found = {it["item"]: it.get("record") for it in (gap.get("sections", {}).get("open_item", {}).get("items") or [])}
    J = json.dumps(vids)
    refs = [x[0] for x in conn.execute("SELECT reference FROM verse WHERE id IN (SELECT value FROM json_each(?))", (J,))]
    for t, it, _ in escalation.match_open_items(Db(cfg), verses=refs, home=False):
        found.setdefault(f"{t['alias']}.{it['item_no']}", None)
    I = []
    for ref, rec in found.items():
        _, row = _thread_item(conn, ref)
        if row["status"] == "open":
            I.append({"item": ref, "value": row["value"], "read_for": row["read_for"] or row["note"],
                      "pre_gate": rec, "settle": None})
    built = _now()
    data = {"reading": r["label"], "reading_id": r["id"], "built_at": built, "built_from": "the tables (B:114)",
            "how": "Fill: findings[].dispose -- one object, or a list each with \"nodes\": [ids] (default: all this "
                   "reading's nodes of the finding): {\"as\": \"claim\", \"claim\": \"C-n|<new_claims key>\"} | "
                   "{\"as\": \"held\", \"item\": \"OT-nn.n|#n\"} | {\"as\": \"held\", \"new_item\": {Open-Item add "
                   "shape}} | {\"as\": \"data|context|withdrawn\", \"reason\"}; claims[].edit {text, beyond_text, "
                   "verdict, sources, observations}, .withdraw \"<why>\"; new_claims [{key, text, beyond_text, verdict, "
                   "sources, observations}]; open_items[].settle {\"as\": \"closed\", \"answer\"} | {\"as\": "
                   "\"withdrawn\", \"reason\"} | {\"as\": \"superseded\", \"by\"} | {\"as\": \"forward\", \"new_item\": "
                   "{...}} | {\"as\": \"touched\", \"found\"} (only for an item whose target reaches past the reading). "
                   "Tellings and blocks are written at Narrate. Then Reading.ps1 -Step Apply.",
            "findings": F, "claims": C, "new_claims": [], "open_items": I}
    path = out_dir(cfg, root, r["label"]) / f"{r['label']}-synergy.json"
    if path.exists():
        path.replace(path.with_name(f"{r['label']}-synergy-{built.replace(':', '').replace('-', '')}.json"))
    _save(path, data)
    nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {
        "synergy_file": _rel(root, path), "synergy_built_at": built, "run_id": run_id}))
    return (f"reading {r['label']}: synergy built from the tables -- {len(F)} finding(s) with {len(nodes)} node(s) of "
            f"this reading, {len(C)} claim(s), {len(I)} open item(s)\n  -> {_rel(root, path)}")


def _settle_plan(cfg, conn, r, data, items, errors) -> list:
    settle = []
    for i, it in enumerate(data.get("open_items") or []):
        at = f"open_items[{i}] ({it.get('item')})"
        s = it.get("settle")
        if not s:
            continue
        how = s.get("as")
        if how not in SETTLE:
            errors.append(f"{at}: settle.as is one of {SETTLE}")
            continue
        text = {"closed": s.get("answer"), "withdrawn": s.get("reason"), "superseded": s.get("by"),
                "touched": s.get("found")}.get(how)
        if how != "forward" and len((text or "").strip()) < (2 if how == "superseded" else 10):
            errors.append(f"{at}: {how} needs " + {"closed": "answer", "withdrawn": "reason", "superseded": "by",
                                                   "touched": "found"}[how])
        if how == "superseded" and not re.search(r"OT-\d+\.\d+|#\d+", s.get("by") or ""):
            errors.append(f"{at}: superseded names the item or escalation that carries it (OT-nn.n or #nnnn)")
        if how == "forward":
            s = {**s, "checked": items.check(s.get("new_item"), at, errors)}
        try:
            _, row = _thread_item(conn, it.get("item"))
            if how == "touched" and not _reaches_past(cfg, row, verse_ids(conn, r["id"])):
                errors.append(f"{at}: its target lies wholly inside the reading -- settle it closed, withdrawn, "
                              f"superseded or forward (touched is for an item read in part, #2250)")
        except Refused as exc:
            errors.append(f"{at}: {exc}")
        settle.append((it["item"], how, s))
    return settle


def apply(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "observed")
    path = _path(root, p.get("File") or r["synergy_file"] or "")
    data = _load(root, str(path), "-File")
    if data.get("reading_id") != r["id"] or not r["synergy_built_at"] or data.get("built_at") != r["synergy_built_at"]:
        raise Refused(f"the file is not the synergy JSON built from the tables for reading {r['label']} "
                      f"(built_at {data.get('built_at')!r}, the reading's {r['synergy_built_at']!r}): run Synergy")
    mine = set(_mine(conn, r["id"]))
    my_nodes = {n["id"]: n for n in reading_nodes(conn, r["id"])}
    items = _ReadingItems(cfg, w)
    errors, derive = [], {"claims": [], "dispositions": []}
    new_keys = set()
    for n in data.get("new_claims") or []:
        new_keys.add(n.get("key"))
        derive["claims"].append({"key": n.get("key"), "new": {k: n.get(k) for k in (
            "text", "beyond_text", "verdict", "sources", "observations")}})
    for c in data.get("claims") or []:
        if c.get("withdraw"):
            derive["claims"].append({"claim": c["claim"], "withdraw": c["withdraw"]})
        elif c.get("edit"):
            derive["claims"].append({"claim": c["claim"], "edit": c["edit"]})
    dispose = []                                       # (node ids, observation, spec)
    for i, f in enumerate(data.get("findings") or []):
        d = f.get("dispose")
        if not d:
            continue
        for k, spec in enumerate(d if isinstance(d, list) else [d]):
            at = f"findings[{i}] (observation {f.get('observation')}) dispose[{k}]"
            ids = spec.get("nodes") or [n["node"] for n in f.get("nodes") or []]
            bad = [x for x in ids if x not in my_nodes or my_nodes[x]["observation_id"] != f.get("observation")]
            if bad:
                errors.append(f"{at}: node(s) {bad} are not this reading's live nodes of observation "
                              f"{f.get('observation')}")
                continue
            how = spec.get("as")
            if how == "claim":
                if spec.get("claim") not in new_keys:
                    try:
                        nr._claim(conn, spec.get("claim"))
                    except Refused as exc:
                        errors.append(f"{at}: {exc}")
            elif how == "held":
                if bool(spec.get("item")) == bool(spec.get("new_item")):
                    errors.append(f"{at}: held needs an existing item (OT-nn.n, OT-nn or #nnnn) or a new_item, one")
                elif spec.get("new_item"):
                    spec = {**spec, "checked": items.check(spec["new_item"], at, errors)}
                elif not _item_exists(conn, spec["item"]):
                    errors.append(f"{at}: held item {spec['item']} does not exist")
            elif how in ("data", "context", "withdrawn"):
                if len((spec.get("reason") or "").strip()) < 10:
                    errors.append(f"{at}: {how} needs its reason, in words")
            else:
                errors.append(f"{at}: 'as' must be one of {DISPOSE}")
            dispose.append((ids, f.get("observation"), spec))
    settle = _settle_plan(cfg, conn, r, data, items, errors)
    if errors:
        raise Refused("\n  ".join(["the synergy is not applied:"] + errors))
    if not (derive["claims"] or dispose or settle):
        raise Refused("nothing to apply: the synergy JSON has no filled field")
    provenance = f"Reading.ps1 -Step Apply -Label {r['label']}"

    def go():
        made, n = (sr.derive_core(cfg, w, derive, run_id, mine, provenance, items, "the reading's")
                   if derive["claims"] else ([], {"new": 0, "edit": 0, "withdraw": 0, "keys": {}}))
        _grant_findings(w)
        for ids, oid, spec in dispose:
            how = spec["as"]
            if how == "claim":
                cid = n["keys"].get(spec["claim"]) or nr._claim(conn, spec["claim"])["id"]
                if not conn.execute("SELECT 1 FROM narrative_claim_source WHERE claim_id=? AND observation_id=?",
                                    (cid, oid)).fetchone():
                    w.insert("narrative_claim_source", {"claim_id": cid, **sr._obs_source(conn, oid)})
                note = "carried by " + conn.execute("SELECT claim_ref FROM narrative_claim WHERE id=?", (cid,)).fetchone()[0]
            elif how == "held":
                item = spec.get("item") or items.raise_(spec["checked"], f"Apply, observation {oid}")
                note = f"held: {item}"
            else:
                note = spec["reason"].strip()
            for nid in ids:
                orec.set_disposition(conn, nid, how, note, r["id"], run_id, w.who)
        settled = []
        for ref, how, s in settle:
            t, row = _thread_item(conn, ref)
            if how == "forward":
                new_ref = items.raise_(s["checked"], f"{ref} carried forward")
                how, text = "superseded", f"carried forward to {new_ref} (reading {r['label']}, claims gate)"
            elif how == "touched":
                text = f"{s['found']} (reading {r['label']}, claims gate, {PART_MARK})"
            else:
                text = {"closed": s.get("answer"), "withdrawn": s.get("reason"),
                        "superseded": s.get("by")}[how] + f" (reading {r['label']}, claims gate)"
            try:
                escalation.update(cfg, Db(cfg), t["id"], item_refs=[str(row["item_no"])], response_kind=how,
                                  respond=text, via=r["escalation_id"], originator=w.who)
            except ValueError as exc:
                raise Refused(f"{ref}: {exc}") from exc
            settled.append(f"{ref} {how}")
        w.update("reading", {"id": r["id"]}, {"run_id": run_id})
        return made, n, settled
    conn.execute("SAVEPOINT reading_apply")
    try:
        made, n, settled = go()
    except BaseException:
        conn.execute("ROLLBACK TO reading_apply")
        conn.execute("RELEASE reading_apply")
        raise
    conn.execute("RELEASE reading_apply")
    return (f"reading {r['label']}: {n['new']} new claim(s) ({', '.join(made) or '-'}), {n['edit']} adjusted, "
            f"{n['withdraw']} withdrawn; {sum(len(x[0]) for x in dispose)} node(s) disposed; {len(settled)} open "
            f"item(s) settled ({', '.join(settled) or '-'}). Next: Reading.ps1 -Step Check")


def gate_post(cfg, root: pathlib.Path, r) -> list[str]:
    """Every node of this reading disposed, a claim disposition carried by a current claim; every current claim on
    the scope resting on a finding; every open item matched to the scope settled, or read in part (#2250)."""
    conn = cfg.conn
    out = []
    for n in reading_nodes(conn, r["id"]):
        if not n["disposition"]:
            out.append(f"node {n['id']} (observation {n['observation_id']}, {n['verse_reference']} {n['strong']}): no "
                       f"disposition (observed_no_claim)")
        elif n["disposition"] in ("claim", "told") and not _carried(conn, n["observation_id"]):
            out.append(f"node {n['id']}: disposed as {n['disposition']}, but no current claim carries observation "
                       f"{n['observation_id']}")
    for c in scope_claims(conn, r["id"], _mine(conn, r["id"])):
        if c["status"] == "current" and not conn.execute(
                "SELECT 1 FROM narrative_claim_source WHERE claim_id=? AND observation_id IS NOT NULL", (c["id"],)
        ).fetchone():
            out.append(f"{c['claim_ref']}: rests on verses only, no finding behind it (claim_without_observation)")
    if not r["synergy_file"]:
        return out + ["no synergy JSON yet (Reading.ps1 -Step Synergy, then Apply)"]
    data = _load(root, r["synergy_file"], "the synergy JSON")
    for it in data.get("open_items") or []:
        try:
            _, row = _thread_item(conn, it.get("item"))
        except Refused as exc:
            out.append(str(exc))
            continue
        if row["status"] == "open" and not _read_in_part(conn, row, r["label"]):
            out.append(f"{it['item']}: still open (settle it: closed, withdrawn, superseded or forward; or touched "
                       f"when its target reaches past the reading)")
    return out


# ══ narrate (D4 narrate) ════════════════════════════════════════════════════════════════════════
def _build_narrate(cfg, root: pathlib.Path, r) -> pathlib.Path:
    conn = cfg.conn
    vids = verse_ids(conn, r["id"])
    claims = scope_claims(conn, r["id"], _mine(conn, r["id"]))
    C = [{"claim": c["claim_ref"], "status": c["status"], "text": c["claim_text"],
          "told_in": nr._told_in(conn, c["id"]), "tell": None, "hold": None} for c in claims]
    cids = [c["id"] for c in claims]
    B = []
    for b in conn.execute(
            f"SELECT DISTINCT s.id, s.heading, s.block_text, ch.chapter_no, ps.heading parent FROM narrative_section s "
            f"JOIN narrative_chapter ch ON ch.id=s.chapter_id AND ch.inactive=0 LEFT JOIN narrative_section ps ON "
            f"ps.id=s.parent_section_id WHERE s.last_version IS NULL AND (s.id IN (SELECT section_id FROM "
            f"narrative_citation WHERE last_version IS NULL AND verse_id IN (SELECT value FROM json_each(?))) OR s.id IN "
            f"(SELECT section_id FROM narrative_claim_telling WHERE status='current' AND claim_id IN "
            f"({','.join('?' * len(cids)) or 'NULL'}))) ORDER BY ch.reading_order, s.ordinal", (json.dumps(vids), *cids)):
        B.append({"chapter": b["chapter_no"], "section": f"{b['parent']} > {b['heading']}" if b["parent"] else b["heading"],
                  "text": b["block_text"]})
    built = _now()
    data = {"reading": r["label"], "reading_id": r["id"], "built_at": built, "built_from": "the tables (B:114)",
            "how": "Fill: claims[].tell [{\"chapter\", \"section\", \"kind\", \"part\"}], .hold \"<reason>\"; rewrite: "
                   "the Narrative rewrite shape (update, refs, blocks) or null. The style is the narrative rules "
                   "(RN-01 onward, step reading.narrate). Then Reading.ps1 -Step Narrate -Label " + r["label"] + ".",
            "claims": C, "blocks": B, "rewrite": None}
    path = out_dir(cfg, root, r["label"]) / f"{r['label']}-narrate.json"
    if path.exists():
        path.replace(path.with_name(f"{r['label']}-narrate-{built.replace(':', '').replace('-', '')}.json"))
    _save(path, data)
    return path


def narrate(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "synergised")
    path = _path(root, p.get("File") or r["narrate_file"] or "")
    data = _load(root, str(path), "-File")
    if data.get("reading_id") != r["id"]:
        raise Refused(f"the file is not the narrate JSON of reading {r['label']}")
    kinds = cfg.enum("narrative_telling_kind")
    errors, tell_plan, holds = [], [], []
    for i, c in enumerate(data.get("claims") or []):
        at = f"claims[{i}] ({c.get('claim')})"
        if c.get("hold") and c.get("tell"):
            errors.append(f"{at}: hold stands alone (not with tell)")
        if c.get("hold"):
            holds.append(c["claim"])
        for t in c.get("tell") or []:
            try:
                ch = nr._chapter(conn, str(t.get("chapter")))
                sec = nr._block(conn, ch, t.get("section"))
                kind = t.get("kind") or "in full"
                nr._check_enum(kinds, kind, f"{at} kind")
                if kind == "in part" and not (t.get("part") or "").strip():
                    raise Refused("told 'in part' with no part")
                tell_plan.append((c["claim"], sec, kind, t.get("part"), ch["chapter_no"]))
            except Refused as exc:
                errors.append(f"{at} tell: {exc}")
    if errors:
        raise Refused("\n  ".join(["the narrative is not written:"] + errors))
    if not (tell_plan or holds or data.get("rewrite")):
        raise Refused("nothing to narrate: no telling, no hold, no rewrite")
    provenance = f"Reading.ps1 -Step Narrate -Label {r['label']}"

    def go():
        since = nr._max_change_id(conn)
        chapters = set()
        for ref, sec, kind, part, chno in tell_plan:
            cid = nr._claim(conn, ref)["id"]
            t = nr._block_telling(conn, cid, sec["id"])
            if not (t and t["status"] == "current" and t["kind"] == kind and t["part_told"] == part):
                nr.tell_block(w, cid, sec["id"], kind, part)
            chapters.add(str(chno))
        for ref in holds:
            w.update("narrative_claim", {"id": nr._claim(conn, ref)["id"]}, {"status": "held"})
        w.mark_changes(since, provenance)
        rw = None
        if data.get("rewrite"):
            rw_data = data["rewrite"]
            refs = rw_data.setdefault("refs", [])
            if not any(x.get("kind") == "escalation" and str(x.get("value")).lstrip("#") == str(r["escalation_id"])
                       for x in refs):
                refs.append({"kind": "escalation", "value": str(r["escalation_id"])})
            rw = nr.rewrite(cfg, w, rw_data, provenance)
            w._grant("verse_meta")
            versemeta.mark(conn, rw["cited_verse_ids"], "citated")
            chapters |= {str(c) for c in rw["chapters"]}
        w._grant("ib_node")
        w._grant("ib_observation_change")
        told = 0
        for n in reading_nodes(conn, r["id"]):
            if n["disposition"] != "claim":
                continue
            refs_told = [x[0] for x in conn.execute(
                "SELECT DISTINCT c.claim_ref FROM narrative_claim_source cs JOIN narrative_claim c ON c.id=cs.claim_id "
                "WHERE cs.observation_id=? AND c.status='current' AND c.in_narrative=1", (n["observation_id"],))]
            if refs_told:
                orec.set_disposition(conn, n["id"], "told", "told: " + ", ".join(refs_told), r["id"], run_id, w.who)
                told += 1
        prev = set(json.loads(r["chapters"] or "[]"))
        w.update("reading", {"id": r["id"]}, {"chapters": json.dumps(sorted(prev | chapters)), "run_id": run_id})
        return rw, told
    rw, told = nr._atomic(conn, go)
    return (f"reading {r['label']}: {len(tell_plan)} telling(s), {len(holds)} held; "
            f"{'blocks rewritten (update ' + str(rw['update_id']) + ')' if rw else 'no block rewritten'}; {told} node(s) "
            f"told. Next: Reading.ps1 -Step Check")


def gate_narrate(cfg, r) -> list[str]:
    """Every current claim on the scope told or held; every verse of the reading cited in a block has a finding or a
    claim behind it."""
    conn = cfg.conn
    out = []
    for c in scope_claims(conn, r["id"], _mine(conn, r["id"])):
        if c["status"] == "current" and not c["in_narrative"]:
            out.append(f"{c['claim_ref']}: current and told in no block (tell it, or hold it) (claim_not_told)")
    for vid, ref, osis in conn.execute(
            "SELECT DISTINCT v.id, v.reference, v.osisId FROM narrative_citation ci JOIN verse v ON v.id=ci.verse_id "
            "JOIN narrative_section s ON s.id=ci.section_id AND s.last_version IS NULL WHERE ci.last_version IS NULL "
            "AND ci.verse_id IN (SELECT verse_id FROM reading_verse WHERE reading_id=?)", (r["id"],)):
        if not conn.execute("SELECT 1 FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE "
                            "n.verse_reference=? AND o.status<>'withdrawn'", (osis,)).fetchone() and \
                not conn.execute("SELECT 1 FROM narrative_claim_source WHERE verse_id=?", (vid,)).fetchone():
            out.append(f"{ref}: cited in a block with no finding and no claim behind it (citation_without_record)")
    return out


# ══ check (the gates) ═══════════════════════════════════════════════════════════════════════════
def check(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    conn = cfg.conn
    r = reading(conn, p.get("Label"))
    if r["state"] == "open":
        gaps = gate_observe(cfg, root, r)
        if gaps:
            _gate_fail(r, "observe", gaps)
        _, data = _index(cfg, root, r)
        vids = [v["verse_id"] for v in data["verses"]]

        def go():
            w.update("reading", {"id": r["id"]}, {"state": "observed", "observed_at": _now(), "run_id": run_id})
            w._grant("verse_meta")
            return versemeta.mark(conn, vids, "analysed")
        marked = nr._atomic(conn, go)
        return f"reading {r['label']}: observe gate passed -- observed; {marked} verse(s) marked analysed"
    if r["state"] == "gathered":
        raise Refused(f"reading {r['label']} was gathered under the earlier process (a gap file); Analysis_phase_1 "
                      f"(#2320) opens a reading at state open")
    if r["state"] == "observed":
        gaps = gate_post(cfg, root, r)
        if gaps:
            _gate_fail(r, "claims", gaps)
        path = _build_narrate(cfg, root, r)
        nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {
            "state": "synergised", "synergised_at": _now(), "narrate_file": _rel(root, path), "run_id": run_id}))
        return (f"reading {r['label']}: claims gate passed -- synergised; narrate JSON built from the tables\n  -> "
                f"{_rel(root, path)}")
    if r["state"] == "synergised":
        gaps = gate_narrate(cfg, r)
        if gaps:
            _gate_fail(r, "narrate", gaps)
        nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {"state": "narrated", "narrated_at": _now(),
                                                                      "run_id": run_id}))
        return f"reading {r['label']}: narrate gate passed -- narrated (Reading.ps1 -Step Publish next)"
    raise Refused(f"reading {r['label']} is {r['state']}; Check runs at open, gathered, observed or synergised")


# ══ publish ═════════════════════════════════════════════════════════════════════════════════════
def _sha(path: pathlib.Path) -> str | None:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def publish(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "narrated")
    nos = json.loads(r["chapters"] or "[]")
    published = []

    def go():
        for no in nos:
            ch = nr._chapter(conn, str(no))
            cur = nr.chapter_dir(cfg) / (ch["current_file"] or "")
            if not ch["current_file"] or not cur.is_file() or cur.read_text(encoding="utf-8") != nr.render_chapter(conn, ch["id"]):
                published.append(nr.publish_chapter(cfg, w, ch, (ch["current_version"] or 0) + 1).name)
        return published
    nr._atomic(conn, go)
    source = root / cfg.required_setting("narrative.copy_source_dir")
    target = pathlib.Path(cfg.required_setting("narrative.learning4comfort_inbox_dir"))
    report = io.StringIO()          # the copy prints its report; stdout carries run.py's JSON reply (#2252)
    with contextlib.redirect_stdout(report):
        rc = narrativecopy.run(str(source), str(target), False, narrativecopy.chapter_files(conn))
    if rc:
        raise Refused(f"the copy to the learning4comfort inbox failed (narrativecopy rc {rc}); the reading stays "
                      f"narrated\n  {report.getvalue().strip()}")
    bad = []
    for no in nos:
        ch = nr._chapter(conn, str(no))
        src = nr.chapter_dir(cfg) / ch["current_file"]
        if _sha(src) is None or _sha(src) != _sha(target / ch["current_file"]):
            bad.append(f"Ch {no} {ch['current_file']}")
    if bad:
        raise Refused(f"not byte-identical in the inbox: {', '.join(bad)}; the reading stays narrated")
    nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {"state": "published", "published_at": _now(),
                                                                  "run_id": run_id}))
    return (f"reading {r['label']}: published; {len(nos)} chapter(s) touched ({', '.join(map(str, nos)) or '-'}), "
            f"{len(published)} newly published ({', '.join(published) or '-'}); all in the inbox byte-identical")


# ══ account ═════════════════════════════════════════════════════════════════════════════════════
def gate_message(conn, escalation_id: int) -> str | None:
    """None when every reading anchored on this escalation is published or withdrawn; else which are not."""
    open_ = [f"{r['label']} ({r['state']})" for r in conn.execute(
        "SELECT label, state FROM reading WHERE escalation_id=? AND state NOT IN ('published', 'withdrawn')",
        (escalation_id,))]
    return f"reading(s) not published: {', '.join(open_)}" if open_ else None


def account(cfg, p: dict, root: pathlib.Path) -> tuple[list[str], str]:
    conn = cfg.conn
    r = reading(conn, p.get("Label"))
    n = len(verse_ids(conn, r["id"]))
    nodes = reading_nodes(conn, r["id"])
    L = [f"# Reading account: {r['label']}", "",
         f"Escalation #{r['escalation_id']} · home {r['home_cluster']} · {n} verse(s) · state **{r['state']}**", "",
         f"Objective: {r['objective'] or 'before #2273 (none recorded)'}", "",
         "| Gate | Passed |", "|---|---|",
         f"| Observe | {r['observed_at'] or '—'} |",
         f"| Claims | {r['synergised_at'] or '—'} |", f"| Narrate | {r['narrated_at'] or '—'} |",
         f"| Published | {r['published_at'] or '—'} |", "",
         f"- Scope JSON: `{r['gap_file']}`",
         f"- Synergy JSON: `{r['synergy_file'] or '—'}`", f"- Narrate JSON: `{r['narrate_file'] or '—'}`",
         f"- Findings applied by this reading: {len({x['observation_id'] for x in nodes})}, on {len(nodes)} node(s)",
         f"- Chapters touched: {', '.join(json.loads(r['chapters'] or '[]')) or '—'}", ""]
    gaps, name = [], None
    if r["state"] == "open":
        gaps, name = gate_observe(cfg, root, r), "Observe"
    elif r["state"] == "observed":
        gaps, name = gate_post(cfg, root, r), "Claims"
    elif r["state"] == "synergised":
        gaps, name = gate_narrate(cfg, r), "Narrate"
    elif r["state"] == "narrated":
        L += ["## Publish", "", "Publish the touched chapters and copy them to the inbox (Reading.ps1 -Step Publish)."]
    if name:
        L += [f"## {name} gate gaps ({len(gaps)})", ""] + [f"- {g}" for g in gaps]
    data = _load(root, r["gap_file"], "the scope JSON")
    L += ["", "## Scope JSON (the index of the verses)", "", "| Status | Verses |", "|---|---|"]
    for st in ("waiting", "in_hand", "done"):
        L.append(f"| {st} | {sum(1 for v in data.get('verses') or [] if v.get('status') == st)} |")
    return L, f"reading {r['label']}: {r['state']}; {len(gaps)} gap(s) at the current gate"
