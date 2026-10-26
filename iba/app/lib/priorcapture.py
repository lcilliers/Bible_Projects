"""priorcapture.py -- the capture of prior study documents into ib_observation and ib_node (escalation #2305; design
`outputs/escalation/2305-prior-work-capture-design-v2-20261026.md`; method rules CP-01 to CP-10 on prior_capture.record).

A migration, not part of the standard analytic process. Per document, three steps:
  prepare(): the lines of the document that name a verse (reading_ref), the verses resolved, the M- and T-coded words
             of each verse with their clusters and subgroups, and the October ids already recorded: one JSON.
  (Claude fills the JSON in a chat session: "findings", and an "answer" on every line.)
  record():  checks the filled JSON and writes it whole -- the observations, their nodes, the answer to every line and
             the document's capture_status -- or refuses it whole. Nothing is added to, checked in or corrected in
             what the document says (CP-02).

The filled JSON:
  "findings": [{"key": "f1", "kind": <the eight kinds or "unfitted">, "text": "...", "meaning": "...",
                "implication": "...", "basis": "stated|read", "route": "A|B|C", "stable_key": "fear:FE-50",
                "flag": "an open question the document carries (kept in revisit_note)",
                "nodes": [{"verse": "Job 23:15", "strong": "H0926", "surface": "terrified", "cluster": "M24",
                           "role": "characteristic|qualifier|standalone", "disposition": "told|claim|held|data|context",
                           "disposition_note": "...", "traced": <observation id or finding key>}]}]
  line "answer": {"captured": ["f1"], "already_recorded": [<observation id>]}
              or {"not_an_observation": "<reason_class>", "reason": "why"}
A node names the word (strong) and the verse; its cluster, subgroup, occurrence and surface come from the tables
(CP-07). A node with a verse and no strong, or with an untagged word, takes the document's cluster.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import pathlib

from . import narrativeregister as nr
from . import observationrecord as orec
from . import recordingpass
from . import strandreading as sr
from . import surfacemap as sm

Refused = nr.Refused
CHUNK = 400


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _file(conn, root: pathlib.Path, ident) -> tuple:
    """The reading_file row for a repo-relative path or an id, and the document's lines as the index counted them."""
    ident = str(ident or "").strip().replace("\\", "/")
    if not ident:
        raise Refused("-File is required: the document's repo-relative path (or its reading_file id)")
    row = conn.execute("SELECT * FROM reading_file WHERE removed=0 AND (path=? OR id=?)",
                       (ident, int(ident) if ident.isdigit() else -1)).fetchone()
    if row is None:
        raise Refused(f"{ident!r} is not a document in the reading index (reading_file): run Reading-Index.ps1 -Step "
                      f"Build if it is new")
    path = root / row["path"]
    if not path.is_file():
        raise Refused(f"{row['path']} is no longer on disk")
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != row["sha256"]:
        raise Refused(f"{row['path']} changed since the reading index was built: run Reading-Index.ps1 -Step Build "
                      f"first, so its line numbers hold")
    return row, data.decode("utf-8").replace("\r", "").split("\n")


def _ref_lines(conn, file_id: int) -> dict[int, list]:
    out: dict[int, list] = {}
    for r in conn.execute(
            "SELECT r.line_no, r.line_kind, r.section_id, r.ref_as_written, r.kind, r.verse_id, v.osisId "
            "FROM reading_ref r LEFT JOIN verse v ON v.id=r.verse_id WHERE r.file_id=? AND r.deleted=0 "
            "ORDER BY r.line_no, r.id", (file_id,)):
        out.setdefault(r["line_no"], []).append(r)
    return out


def _words(conn, osis: list[str]) -> dict[str, list]:
    """Per verse: its M- and T-coded words (verse_lexical) with their clusters and surface subgroups."""
    clusters: dict[str, list] = {}
    for r in conn.execute("SELECT strong, cluster_code FROM cluster_strong WHERE COALESCE(deleted,0)=0 AND "
                          "(cluster_code LIKE 'M%' OR cluster_code LIKE 'T%') ORDER BY cluster_code"):
        clusters.setdefault(r[0], []).append(r[1])
    sub = {(r[0], r[1], r[2]): r[3] for r in conn.execute(
        "SELECT ss.cluster_code, ss.strong, ss.surface, cs.subgroup_code FROM surface_subgroup ss JOIN "
        "cluster_subgroup cs ON cs.id=ss.cluster_subgroup_id WHERE ss.deleted=0")}
    out: dict[str, list] = {}
    for i in range(0, len(osis), CHUNK):
        part = osis[i:i + CHUNK]
        for r in conn.execute(
                f"SELECT vl.id, vl.strong, vl.surface, vl.morph_code, v.osisId FROM verse_lexical vl JOIN verse v ON "
                f"v.id=vl.verse_id WHERE vl.deleted=0 AND v.osisId IN ({','.join('?' * len(part))}) "
                f"ORDER BY v.osisId, vl.position", part):
            cl = clusters.get(r["strong"])
            if cl:
                out.setdefault(r["osisId"], []).append({
                    "verse_lexical_id": r["id"], "strong": r["strong"], "surface": r["surface"],
                    "morph": r["morph_code"], "clusters": cl,
                    "subgroups": {c: sub[(c, r["strong"], sm.norm(r["surface"]))] for c in cl
                                  if (c, r["strong"], sm.norm(r["surface"])) in sub}})
    return out


def october_ids(conn, path: str) -> dict:
    """The live observations that name the document in revisit_note and carry a stable_key (CP-05)."""
    named = {r[0]: r[1] for r in conn.execute(
        "SELECT stable_key, id FROM ib_observation WHERE status<>'withdrawn' AND stable_key IS NOT NULL AND "
        "revisit_note LIKE ? ORDER BY id", (f"%{path}%",))}
    return named


def october_same_prefix(conn, named: dict) -> dict:
    """Live observations whose stable_key shares a prefix with the document's own ids but whose revisit_note does not
    name the file: the document's id may be among them (Record refuses a stable_key already live)."""
    out = {}
    for pre in {k.split(":")[0] for k in named if ":" in k}:
        for k, i in conn.execute("SELECT stable_key, id FROM ib_observation WHERE status<>'withdrawn' AND "
                                 "stable_key LIKE ? ORDER BY id", (f"{pre}:%",)):
            if k not in named:
                out[k] = i
    return out


def prepare(conn, root: pathlib.Path, ident) -> dict:
    row, text = _file(conn, root, ident)
    if row["capture_status"] in ("captured", "nothing to capture"):
        raise Refused(f"{row['path']} is already {row['capture_status']} (run {row['capture_run_id']})")
    secs = conn.execute("SELECT id, heading, line_start, line_end FROM reading_section WHERE file_id=? AND deleted=0 "
                        "ORDER BY ordinal", (row["id"],)).fetchall()
    by_line = _ref_lines(conn, row["id"])
    osis = sorted({r["osisId"] for rs in by_line.values() for r in rs if r["osisId"]})
    lines, unresolved = [], []
    for n in sorted(by_line):
        sec = next((s["heading"] for s in secs if s["line_start"] <= n <= (s["line_end"] or n)), None)
        refs = [{"as_written": r["ref_as_written"], "kind": r["kind"], "verse": r["osisId"]} for r in by_line[n]]
        unresolved += [{"line_no": n, "ref": r["as_written"], "kind": r["kind"]} for r in refs if not r["verse"]]
        lines.append({"line_no": n, "line_kind": by_line[n][0]["line_kind"], "section": sec,
                      "text": text[n - 1] if 0 < n <= len(text) else None, "refs": refs, "answer": None})
    return {"kind": "prior-capture", "version": 1, "built_at": _now(),
            "file": {"id": row["id"], "path": row["path"], "cluster": row["cluster"], "sha256": row["sha256"]},
            "fill": "findings: one per material observation the document makes about a verse (CP-01 to CP-07); "
                    "lines[].answer: every line answered (captured / already_recorded / not_an_observation)",
            "counts": {"lines": len(lines), "verses": len(osis), "unresolved_refs": len(unresolved)},
            "october": (oct_ := october_ids(conn, row["path"])), "october_same_prefix": october_same_prefix(conn, oct_),
            "unresolved": unresolved,
            "verse_words": _words(conn, osis), "lines": lines, "findings": []}


# ══ record ══════════════════════════════════════════════════════════════════════════════════════
def _node(conn, cfg, vx, fkind, fcluster, n, at, roles, dispositions, errors, notes):
    """One node spec -> the row to write, or None (an error is recorded)."""
    if not isinstance(n, dict):
        errors.append(f"{at}: a node is an object")
        return None
    out = {"at": at, "role": n.get("role"), "disposition": n.get("disposition"),
           "disposition_note": n.get("disposition_note"), "traced": n.get("traced"), "strong": None, "surface": None,
           "morph_code": None, "verse_reference": None, "verse_lexical_id": None, "cluster": None, "subgroup": None}
    if out["role"] is not None and out["role"] not in roles:
        errors.append(f"{at}: role must be one of {roles}")
    if out["disposition"] is not None and out["disposition"] not in dispositions:
        errors.append(f"{at}: disposition must be one of {dispositions} (the document's W is told)")
    strong, verse = n.get("strong"), n.get("verse")
    if verse:
        try:
            out["verse_reference"] = sr._verse(conn, vx, verse)["osisId"]
        except Refused as exc:
            errors.append(f"{at}: {exc}")
            return None
    if n.get("traced") is not None and not strong and not verse:
        out["cluster"] = n.get("cluster") or fcluster
    elif not strong:
        if not verse:
            errors.append(f"{at}: a node names a verse, a word (strong) or the finding it is about (traced)")
            return None
        out["cluster"] = n.get("cluster") or fcluster
    else:
        clusters = [c for c in orec.word_clusters(conn, strong) if c[0] in "MT"]
        rows = conn.execute(
            "SELECT vl.id, vl.surface, vl.morph_code FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id "
            "WHERE vl.deleted=0 AND vl.strong=? AND v.osisId=? ORDER BY vl.position",
            (strong, out["verse_reference"])).fetchall() if out["verse_reference"] else []
        if out["verse_reference"] and not rows:
            errors.append(f"{at}: {strong} does not occur in {out['verse_reference']} (verse_lexical)")
            return None
        if not clusters:
            notes.append(f"{at}: {strong} is in no M or T cluster: the node is the verse alone, the word stays in the "
                         f"text")
            out["cluster"] = n.get("cluster") or fcluster
        else:
            cl = n.get("cluster")
            if cl and cl not in clusters:
                errors.append(f"{at}: cluster must be one of {strong}'s own {clusters}")
                return None
            ms = [c for c in clusters if c.startswith("M")]
            cl = cl or (clusters[0] if len(clusters) == 1 else fcluster if fcluster in clusters else
                        ms[0] if len(ms) == 1 else None)
            if cl is None:
                errors.append(f"{at}: {strong} is in {clusters}: name the cluster")
                return None
            out.update(strong=strong, cluster=cl)
            if out["verse_reference"]:
                want = sm.norm(n.get("surface"))
                hit = [r for r in rows if want and sm.norm(r["surface"]) == want] or (rows if len(rows) == 1 else [])
                if len(hit) == 1:
                    out.update(verse_lexical_id=hit[0]["id"], surface=hit[0]["surface"], morph_code=hit[0]["morph_code"])
                    out["subgroup"] = conn.execute(
                        "SELECT cs.subgroup_code FROM surface_subgroup ss JOIN cluster_subgroup cs ON "
                        "cs.id=ss.cluster_subgroup_id WHERE ss.deleted=0 AND ss.cluster_code=? AND ss.strong=? AND "
                        "ss.surface=?", (cl, strong, sm.norm(hit[0]["surface"]))).fetchone()
                    out["subgroup"] = out["subgroup"][0] if out["subgroup"] else None
                else:
                    out.update(surface=n.get("surface"), morph_code=rows[0]["morph_code"])
                    notes.append(f"{at}: {strong} occurs {len(rows)} times in {out['verse_reference']} and the surface "
                                 f"{n.get('surface')!r} picks none: no verse_lexical_id (for the anomaly group, B:121)")
            elif fkind != "term":
                errors.append(f"{at}: only a term finding applies to a word with no verse")
                return None
    if not out["cluster"]:
        errors.append(f"{at}: no cluster for this node (the document has none): name one")
        return None
    return out


def check(cfg, root: pathlib.Path, data: dict) -> dict:
    """The filled JSON -> the plan record() writes. Raises Refused listing every problem."""
    conn = cfg.conn
    errors, notes, quotes = [], [], []
    if not isinstance(data, dict) or data.get("kind") != "prior-capture":
        raise Refused("the file is not a prior-capture JSON (-Step Prepare builds it)")
    row, _ = _file(conn, root, (data.get("file") or {}).get("id"))
    if (data["file"].get("sha256") or "") != row["sha256"]:
        raise Refused(f"the JSON was built from another version of {row['path']}: run Prepare again")
    if row["capture_status"] in ("captured", "nothing to capture"):
        raise Refused(f"{row['path']} is already {row['capture_status']} (run {row['capture_run_id']})")
    kinds = orec.kinds(cfg) + [cfg.required_setting("prior_capture.unfitted_tag")]
    bases, routes, roles = cfg.enum("ib_observation.basis"), cfg.enum("observation_route"), cfg.enum("observation_role")
    dispositions = cfg.enum("observation_disposition")
    classes, vx = cfg.enum("prior_capture_line.reason_class"), nr.VerseIndex(cfg)
    fcluster = row["cluster"]
    # the lines: exactly the ones the index holds
    live_lines = set(_ref_lines(conn, row["id"]))
    got = {l.get("line_no") for l in data.get("lines") or []}
    if got != live_lines:
        errors.append(f"lines: the JSON's lines differ from the index's: missing {sorted(live_lines - got)[:10]}, "
                      f"not in the index {sorted(got - live_lines)[:10]}")
    # the findings
    plan, keys, stable = [], {}, {}
    for i, f in enumerate(data.get("findings") or []):
        where = f"findings[{i}] ({f.get('key') if isinstance(f, dict) else '?'})"
        if not isinstance(f, dict) or not f.get("key") or f["key"] in keys:
            errors.append(f"{where}: an object with a unique key")
            continue
        keys[f["key"]] = where
        text = (f.get("text") or "").strip()
        if f.get("kind") not in kinds:
            errors.append(f"{where}: kind must be one of {kinds}")
        if not text:
            errors.append(f"{where}: text is required")
        else:
            try:
                recordingpass._validate_obs_text(conn, text)
            except recordingpass.InvalidObservationText as exc:
                errors.append(f"{where}: {exc}")
        if f.get("basis") not in bases:
            errors.append(f"{where}: basis must be one of {bases}")
        route = f.get("route")
        if f.get("kind") in orec.ROUTE_REQUIRED and route not in routes:
            errors.append(f"{where}: a {f.get('kind')} finding carries its route, one of {routes}")
        elif route is not None and (f.get("kind") not in orec.ROUTE_ALLOWED or route not in routes):
            errors.append(f"{where}: route ({routes}) is held only on a party or link finding")
        sk = f.get("stable_key")
        if sk:
            live = conn.execute("SELECT id FROM ib_observation WHERE stable_key=? AND status<>'withdrawn'",
                                (sk,)).fetchone()
            if live or sk in stable:
                errors.append(f"{where}: stable_key {sk} is already recorded"
                              + (f" as observation {live[0]}: answer its line already_recorded" if live else
                                 " by another finding of this file"))
            stable[sk] = where
        quotes += sr._quote_check(conn, cfg, [f.get(k) for k in ("text", "meaning", "implication")], where)
        nodes = []
        for j, n in enumerate(f.get("nodes") or []):
            nd = _node(conn, cfg, vx, f.get("kind"), fcluster, n, f"{where} nodes[{j}]", roles, dispositions, errors,
                       notes)
            if nd:
                nodes.append(nd)
        if not f.get("nodes"):
            errors.append(f"{where}: at least one node (what the finding applies to)")
        plan.append({"key": f["key"], "where": where, "spec": f, "nodes": nodes})
    # the answers
    answers, used = [], set()
    for l in data.get("lines") or []:
        n, a = l.get("line_no"), l.get("answer")
        at = f"line {n}"
        if not isinstance(a, dict) or not a:
            errors.append(f"{at}: no answer (CP-01)")
            continue
        if "not_an_observation" in a:
            if len(a) > 2 or a["not_an_observation"] not in classes or not (a.get("reason") or "").strip():
                errors.append(f"{at}: not_an_observation is one of {classes} with a reason, and nothing else")
            else:
                answers.append({"line_no": n, "answer": "not an observation", "class": a["not_an_observation"],
                                "reason": a["reason"].strip()})
            continue
        if not (a.get("captured") or a.get("already_recorded")):
            errors.append(f"{at}: answer is captured, already_recorded or not_an_observation")
        for k in a.get("captured") or []:
            if k not in keys:
                errors.append(f"{at}: captured names {k!r}, which is not a finding")
            else:
                used.add(k)
                answers.append({"line_no": n, "answer": "captured", "key": k})
        for oid in a.get("already_recorded") or []:
            if not conn.execute("SELECT 1 FROM ib_observation WHERE id=? AND status<>'withdrawn'", (oid,)).fetchone():
                errors.append(f"{at}: already_recorded names observation {oid}, which is not live")
            else:
                answers.append({"line_no": n, "answer": "already recorded", "observation": oid})
    for k in keys:
        if k not in used:
            errors.append(f"{keys[k]}: no line answers captured for it (a finding comes from a line)")
    if errors:
        raise Refused("\n  ".join(["the capture is not recorded:"] + errors[:60]
                                  + ([f"... and {len(errors) - 60} more"] if len(errors) > 60 else [])))
    return {"file": row, "plan": plan, "answers": answers, "notes": notes, "quotes": quotes,
            "unresolved": data.get("unresolved") or []}


def write(conn, p: dict, run_id: str) -> dict:
    """Write a checked plan in the caller's transaction. Returns the counts and the per-finding observation ids."""
    row, now, ids = p["file"], _now(), {}
    stage = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='prior_capture.stage'").fetchone()[0])
    lines_of = {}
    for a in p["answers"]:
        if a["answer"] == "captured":
            lines_of.setdefault(a["key"], []).append(a["line_no"])
    new = reused = nodes = 0
    for f in p["plan"]:
        s = f["spec"]
        text = s["text"].strip()
        dup = orec.live_text(conn, text)
        if dup:
            oid, reused = dup["id"], reused + 1                     # CP-04: identical live description
        else:
            ls = lines_of[f["key"]]
            note = f"Captured from {row['path']} lines {min(ls)}-{max(ls)} (#2305)"
            if s.get("flag"):
                note += f"; flag: {s['flag'].strip()}"
            oid = conn.execute(
                "INSERT INTO ib_observation (cluster_code, stage, tag, obs_text, meaning, implication, basis, route, "
                "meaning_source, status, stable_key, revisit_note, run_id, created_at) "
                "VALUES (NULL,?,?,?,?,?,?,?,?,'draft',?,?,?,?)",
                (stage, s["kind"], text, s.get("meaning"), s.get("implication"), s["basis"], s.get("route"),
                 "observations" if any(n.get("traced") is not None for n in f["nodes"]) else "verse-text",
                 s.get("stable_key"), note, run_id, now)).lastrowid
            new += 1
        ids[f["key"]] = oid
    for f in p["plan"]:
        oid = ids[f["key"]]
        seq = conn.execute("SELECT COALESCE(MAX(seq), -1) FROM ib_node WHERE observation_id=?", (oid,)).fetchone()[0]
        for n in f["nodes"]:
            t = n["traced"]
            t = ids.get(t, t) if t is not None else None
            seq += 1
            conn.execute(
                "INSERT INTO ib_node (observation_id, cluster_code, cluster_subgroup_code, strong, verse_reference, "
                "surface, morph_code, traced_observation_id, source_stage, seq, created_at, role, disposition, "
                "disposition_note, verse_lexical_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (oid, n["cluster"], n["subgroup"], n["strong"], n["verse_reference"], n["surface"], n["morph_code"],
                 t, stage, seq, now, n["role"], n["disposition"], n["disposition_note"], n["verse_lexical_id"]))
            nodes += 1
    for a in p["answers"]:
        oid = ids[a["key"]] if a["answer"] == "captured" else a.get("observation")
        conn.execute("INSERT INTO prior_capture_line (file_id, line_no, answer, reason_class, reason, observation_id, "
                     "run_id, created_by) VALUES (?,?,?,?,?,?,?,'Claude')",
                     (row["id"], a["line_no"], a["answer"], a.get("class"), a.get("reason"), oid, run_id))
    status = "captured" if any(a["answer"] != "not an observation" for a in p["answers"]) else "nothing to capture"
    conn.execute("UPDATE reading_file SET capture_status=?, capture_run_id=? WHERE id=?", (status, run_id, row["id"]))
    return {"status": status, "observations_new": new, "observations_reused": reused, "nodes": nodes,
            "lines": len({a["line_no"] for a in p["answers"]}), "answers": len(p["answers"]), "ids": ids}


def report_lines(p: dict, w: dict) -> list[str]:
    """The run's report: what was taken, and everything the capture left for a reader to see (design sec 4, Q5)."""
    f = p["file"]
    out = [f"# Prior-work capture: {f['path']}", "",
           f"Status **{w['status']}**. {w['observations_new']} observation(s) written, {w['observations_reused']} "
           f"joined an identical live description, {w['nodes']} node(s); {w['lines']} line(s) answered "
           f"({w['answers']} answer rows).", ""]
    unf = [(x["spec"]["key"], x["where"]) for x in p["plan"] if x["spec"]["kind"] == "unfitted"]
    sections = [("Unfitted observations (tag unfitted, design 2.4)",
                 [f"observation {w['ids'][k]} ({k})" for k, _ in unf]),
                ("Flags the document carries (Q5)", [f"observation {w['ids'][x['key']]}: {x['spec']['flag']}"
                                                     for x in p["plan"] if x["spec"].get("flag")]),
                ("Node notes (no occurrence, untagged word)", p["notes"]),
                ("References that resolve to no single verse", [f"line {u['line_no']}: {u['ref']} ({u['kind']})"
                                                                for u in p["unresolved"]]),
                ("Quotations not found in the ESV text (captured as written)", p["quotes"])]
    for title, items in sections:
        out += [f"## {title}", ""] + ([f"- {i}" for i in items] if items else ["none"]) + [""]
    return out


def report(conn) -> tuple[list[str], str]:
    q = lambda sql: conn.execute(sql).fetchall()  # noqa: E731
    docs = q("SELECT capture_status, COUNT(*) FROM reading_file WHERE removed=0 GROUP BY 1 ORDER BY 1")
    obs = q("SELECT tag, COUNT(*) FROM ib_observation WHERE stage='prior-capture' AND status<>'withdrawn' "
            "GROUP BY 1 ORDER BY 2 DESC")
    ans = q("SELECT answer, COUNT(*) FROM prior_capture_line WHERE deleted=0 GROUP BY 1 ORDER BY 1")
    nodes = q("SELECT COUNT(*), SUM(verse_lexical_id IS NULL) FROM ib_node WHERE source_stage='prior-capture'")[0]
    lines = ["# Prior-work capture: where it stands", "", "## Documents by status", ""]
    lines += [f"- {s}: {n}" for s, n in docs] + ["", "## Observations by tag (stage prior-capture)", ""]
    lines += ([f"- {t}: {n}" for t, n in obs] or ["none"]) + ["", "## Line answers", ""]
    lines += [f"- {a}: {n}" for a, n in ans] or ["none"]
    lines += ["", f"## Nodes: {nodes[0]}, {nodes[1] or 0} without an occurrence (verse_lexical_id)"]
    done = {s: n for s, n in docs}
    return lines, (f"documents: {', '.join(f'{s} {n}' for s, n in docs)}; observations "
                   f"{sum(n for _, n in obs)}; captured {done.get('captured', 0)} of {sum(done.values())}")
