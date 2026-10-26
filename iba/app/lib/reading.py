"""reading.py -- the reading process (escalation #2228; on the phases of the analytic process, #2273, design
`outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md`).

A reading is the work on one scope with its objective, served by the escalation that anchors it. Its findings are
written through observationrecord (#2274): one observation per finding, applied by nodes. It passes four gates in
order, each checked from the tables by the tool, not asserted:

  open      0.C: the scope resolved (versescope, its 2,500 review), its objective, its verses kept (reading_verse),
            the scope collated (versecollate), and the pre-gap JSON written: one section per gap type of phase pre
            (cfg_setting reading.gap_types), each found by its detector in PRE. Refused when the home is an M
            cluster with unallocated or stale surface pairs (surfacemap.reading_refusal, #2294)
  gather    0.GAP pre written: each pre-gap item's record -- {"finding": ...}, {"table", "id"}, a face on a strand
            hit, a response on an open item, or {"reason": ...} -- and new open items; the ids written back
  check     the gate the reading is at: pre (open -> gathered), observe (gathered -> observed; the verses marked
            analysed), claims (observed -> synergised; the narrate JSON built) or narrate (synergised -> narrated)
  observe   D3 and D4 input: the observe JSON built from the tables -- per verse its passage, every finding applied to
            it with its nodes, the words in focus (reading.focus_words) -- with the claims on the scope and the
            catalogue prompts by kind (reading.observe_prompts)
  record    D4 observe written: the findings (observationrecord), withdrawals with their reasons, each word's open
            item or reason
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


def _items_of(data: dict):
    """(section, index, item) for every item of the pre-gap JSON."""
    for sec, s in (data.get("sections") or {}).items():
        for i, it in enumerate(s.get("items") or []):
            yield sec, i, it


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


def _row_exists(conn, table: str, rid) -> bool:
    if not re.fullmatch(r"[a-z_]+", table or ""):
        return False
    if not conn.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)).fetchone():
        return False
    try:
        return conn.execute(f'SELECT 1 FROM "{table}" WHERE id=?', (rid,)).fetchone() is not None
    except Exception:  # noqa: BLE001 -- a table with no id column cannot hold the record
        return False


def _gate_fail(r, name: str, gaps: list[str]):
    raise Refused("\n  ".join([f"reading {r['label']} is not past the {name} gate ({len(gaps)} gap(s)):"] + gaps[:60]
                              + ([f"... and {len(gaps) - 60} more"] if len(gaps) > 60 else [])))


# ══ open (0.C and the pre-gaps) ═════════════════════════════════════════════════════════════════
def _pre_read_in_files_only(col, v, acc):
    if v["file_lines"] and not v["observations"]:
        acc.setdefault("read_in_files_only", []).append({
            "verse": v["reference"], "words": sorted({f"{x['surface']} ({x['strong']}, {x['cluster']})"
                                                      for x in v["words"]}), "text": v["text"],
            "file_lines": [f"{x['file']}:{x['line']} {x['text']}" for x in v["file_lines"]], "record": None})


def _pre_face_not_gathered(col, v, acc):
    for h in v["strand_hits"]:
        if not h["face"] and not h["reason"]:
            acc.setdefault("face_not_gathered", []).append({"verse": v["reference"], "strand": h["strand"],
                                                           "strong": h["strong"], "surface": h["surface"],
                                                           "record": None})


def _pre_meaning_missing(col, v, acc):
    found = acc.setdefault("meaning_missing", {})
    for x in v["words"]:
        lx = col["lexicon"].get(x["strong"], {})
        miss = [m for m, gone in (("meaning senses", not lx.get("meaning")),
                                  ("Mounce", x["strong"].startswith("G") and not lx.get("mounce"))) if gone]
        if miss:
            found.setdefault(x["strong"], {"strong": x["strong"], "missing": miss, "verses": [], "record": None})
            if v["reference"] not in found[x["strong"]]["verses"]:
                found[x["strong"]]["verses"].append(v["reference"])


def _pre_open_item(col, v, acc):
    found = acc.setdefault("open_item", {})
    for o in v["open_items"]:
        it = found.setdefault(o["item"], {"item": o["item"], "value": o["value"], "read_for": None,
                                          "note": o["note"], "verses": [], "record": None})
        if v["reference"] not in it["verses"]:
            it["verses"].append(v["reference"])


# The pre-gap detectors by gap type. A pre gap type with no detector gets an empty section (build B6, #2278).
PRE = {"read_in_files_only": _pre_read_in_files_only, "face_not_gathered": _pre_face_not_gathered,
       "meaning_missing": _pre_meaning_missing, "open_item": _pre_open_item}


def open_(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path, file_request: dict | None) -> str:
    """-Label -Escalation -Home -Objective <scope selectors as Verse-Scope.ps1> [-Reviewed] [-File request]."""
    conn = cfg.conn
    label = (p.get("Label") or "").strip()
    if not label or label != label.lower() or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", label):
        raise Refused("-Label is the reading's name, lowercase-hyphenated (e.g. anger-bosom)")
    if conn.execute("SELECT 1 FROM reading WHERE label=?", (label,)).fetchone():
        raise Refused(f"reading {label} already exists")
    objective = (p.get("Objective") or "").strip()
    if len(objective) < 10:
        raise Refused("-Objective is the scope's objective, in words (0.C: it defines the home of what is recorded)")
    try:
        eid = int(str(p.get("Escalation") or "").lstrip("#"))
    except ValueError:
        raise Refused("-Escalation (the task or issue that anchors the reading) is required") from None
    e = conn.execute("SELECT type, state FROM escalation e WHERE id=? AND version=(SELECT MAX(version) FROM escalation "
                     "x WHERE x.id=e.id)", (eid,)).fetchone()
    if e is None or e["type"] not in ("task", "issue") or e["state"] in ("completed", "closed", "withdrawn"):
        raise Refused(f"escalation #{eid} is not an open task or issue")
    home = (p.get("Home") or "").strip()
    if not conn.execute("SELECT 1 FROM cluster WHERE cluster_code=?", (home,)).fetchone():
        raise Refused(f"-Home {home!r} is not a cluster (the cluster the scope is anchored on)")
    unmapped = surfacemap.reading_refusal(conn, home)
    if unmapped:
        raise Refused(unmapped)
    types = gap_types(cfg)
    request = vs.normalise_request({k: v for k, v in p.items() if k not in NOT_SCOPE}, file_request)
    # the home (B:120): the request's subgroups of the home cluster, else the home cluster itself
    request["home"] = [s for s in request.get("subgroup", []) if conn.execute(
        "SELECT 1 FROM cluster_subgroup WHERE subgroup_code=? AND cluster_code=?", (s, home)).fetchone()] or [home]
    try:
        col = vc.collate(cfg, request, root)
    except (vs.ScopeError, vc.CollateError) as exc:
        raise Refused(str(exc)) from exc
    acc: dict = {}
    pre = [t for t, x in types.items() if x["phase"] == "pre"]
    for v in col["verses"]:
        for t in pre:
            if t in PRE:
                PRE[t](col, v, acc)
    sections = {}
    for t in pre:
        items = acc.get(t, [])
        if isinstance(items, dict):
            items = list(items.values())
        if t == "open_item":
            for it in items:
                it["read_for"] = _thread_item(conn, it["item"])[1]["read_for"]
        sections[t] = {"guide": types[t]["guide"], "records_in": types[t]["records_in"], "items": items}
    folder = out_dir(cfg, root, label)
    gap_path = folder / f"{label}-gaps.json"
    if gap_path.exists():
        raise Refused(f"{_rel(root, gap_path)} is already on disk")

    def go():
        rid = w.insert("reading", {"label": label, "escalation_id": eid, "home_cluster": home, "objective": objective,
                                   "request": json.dumps(col["scope"]["request"], ensure_ascii=False),
                                   "gap_file": _rel(root, gap_path), "note": p.get("Note"), "run_id": run_id})
        for v in col["verses"]:
            w.insert("reading_verse", {"reading_id": rid, "verse_id": v["verse_id"],
                                       "routes": json.dumps(v["routes"], ensure_ascii=False)})
        return rid
    rid = nr._atomic(conn, go)
    data = {"reading": label, "reading_id": rid, "escalation": eid, "home": home, "objective": objective,
            "opened": _now(), "scope": col["scope"]["selectors"],
            "how": "Fill each item's `record` with one of {\"finding\": <a finding: observationrecord's shape>}, "
                   "{\"table\": \"...\", \"id\": n} or {\"reason\": \"...\"}; a face_not_gathered item may take "
                   "{\"face\", \"parties\", \"observation\"}; an open_item may take {\"response\": what the reading "
                   "found}. Then Reading.ps1 -Step Gather -Label " + label + ". New open items go in `new_items` (the "
                   "Open-Item.ps1 -Action Add shape).",
            "new_items": [], "sections": sections}
    _save(gap_path, data)
    _save(folder / f"{label}-collation.json", {"label": label, "run_id": run_id, **col})
    n = {k: len(s["items"]) for k, s in sections.items()}
    return (f"reading {label} opened (#{eid}, home {home}): {len(col['verses'])} verse(s); pre-gaps "
            + ", ".join(f"{k} {v}" for k, v in n.items()) + f"\n  -> {_rel(root, gap_path)}")


# ══ gather (0.GAP pre written) ══════════════════════════════════════════════════════════════════
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


def _new_items(items: _ReadingItems, data: dict, errors: list) -> list:
    return [(f"new_items[{i}]", items.check(s, f"new_items[{i}]", errors))
            for i, s in enumerate(data.get("new_items") or []) if not (isinstance(s, dict) and s.get("added"))]


def _grant_findings(w: nr.Writer) -> None:
    for t in ("ib_observation", "ib_node", "ib_observation_change"):
        w._grant(t)


def gather(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    """-Label [-File <pre-gap JSON>]: every filled `record` written or checked; nothing is written if any is wrong."""
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "open")
    path = _path(root, p.get("File") or r["gap_file"])
    data = _load(root, str(path), "-File")
    if data.get("reading_id") != r["id"]:
        raise Refused(f"the file is the pre-gap JSON of reading {data.get('reading')!r} (id {data.get('reading_id')}), "
                      f"not {r['label']} (id {r['id']})")
    types = gap_types(cfg)
    items = _ReadingItems(cfg, w)
    errors, quotes, plan, specs = [], [], [], []
    for sec, i, it in _items_of(data):
        rec, at = it.get("record"), f"{sec}[{i}] ({it.get('verse') or it.get('strong') or it.get('item')})"
        if rec is None or (isinstance(rec, dict) and rec.get("run_id") and rec.get("id") is not None):
            continue                                   # not yet, or written by an earlier Gather (checked at Check)
        kinds_given = [k for k in ("finding", "reason", "table", "response", "face") if rec.get(k)] \
            if isinstance(rec, dict) else []
        if sec == "face_not_gathered" and isinstance(rec, dict) and rec.get("reason") and not rec.get("face"):
            kinds_given = ["face"]                     # a strand hit's reason is the hit's own record
        if len(kinds_given) != 1:
            errors.append(f"{at}: record is one of {{\"finding\": ...}}, {{\"table\", \"id\"}} or {{\"reason\"}} "
                          f"(face_not_gathered: or a face; open_item: or a response)")
            continue
        how = kinds_given[0]
        if how == "reason":
            if len(rec["reason"].strip()) < 10:
                errors.append(f"{at}: a reason says why, in words (10 characters or more)")
            continue
        if how == "table":
            if rec["table"] not in types[sec]["records_in"]:
                errors.append(f"{at}: {sec} records into {types[sec]['records_in']}, not {rec['table']}")
            elif not _row_exists(conn, rec["table"], rec.get("id")):
                errors.append(f"{at}: {rec['table']} {rec.get('id')} does not exist")
            continue
        if how == "finding":
            if "ib_observation" not in types[sec]["records_in"]:
                errors.append(f"{at}: {sec} does not record into a finding")
                continue
            key = f"{sec}:{i}"
            specs.append((at, {**rec["finding"], "key": key}))
            plan.append(("finding", it, key))
        elif how == "response":
            if sec != "open_item" or len(rec["response"].strip()) < 10:
                errors.append(f"{at}: a response is what the reading found, on an open item (10 characters or more)")
                continue
            try:
                _thread_item(conn, it["item"])
            except Refused as exc:
                errors.append(f"{at}: {exc}")
                continue
            plan.append(("touch", it, rec["response"].strip()))
        else:                                          # a face on a strand hit
            if sec != "face_not_gathered":
                errors.append(f"{at}: a face is recorded on a face_not_gathered item")
                continue
            hit = conn.execute("SELECT h.id FROM reading_strand_hit h JOIN reading_strand s ON s.id=h.strand_id JOIN "
                               "verse v ON v.id=h.verse_id WHERE s.code=? AND h.strong=? AND v.reference=?",
                               (it.get("strand"), it.get("strong"), it.get("verse"))).fetchone()
            if hit is None:
                errors.append(f"{at}: no strand hit {it.get('strand')} {it.get('strong')} at {it.get('verse')}")
                continue
            if bool((rec.get("face") or "").strip()) == bool((rec.get("reason") or "").strip()):
                errors.append(f"{at}: give a face or a reason, one of them")
            ob = rec.get("observation")
            if ob is not None and not conn.execute("SELECT 1 FROM ib_observation WHERE id=? AND status<>'withdrawn'",
                                                   (ob,)).fetchone():
                errors.append(f"{at}: observation {ob} is not a live observation")
            plan.append(("hit", it, (hit["id"], rec)))
    fplan = orec.check(cfg, specs, errors, quotes) if specs else []
    new_items = _new_items(items, data, errors)
    if errors or quotes:
        raise Refused("\n  ".join(["the pre-gaps are not gathered:"] + errors + (
            ["quotation(s) not found in the ESV text:"] + quotes if quotes else [])))
    if not plan and not new_items:
        raise Refused("nothing to gather: no item has a new record, and no new item is listed")

    def go():
        _grant_findings(w)
        written = orec.write(conn, fplan, r["id"], run_id) if fplan else {}
        for kind, it, x in plan:
            rec = it["record"]
            if kind == "finding":
                it["record"] = {**rec, "table": "ib_observation", "id": written[x]["observation"],
                                "nodes": written[x]["nodes"], "run_id": run_id}
            elif kind == "touch":
                t, row = _thread_item(conn, it["item"])
                try:
                    escalation.update(cfg, Db(cfg), t["id"], item_refs=[str(row["item_no"])], response_kind="touched",
                                      respond=f"{x} (reading {r['label']}, pre gate)", via=r["escalation_id"],
                                      originator=w.who)
                except ValueError as exc:
                    raise Refused(f"{it['item']}: {exc}") from exc
                resp = conn.execute("SELECT MAX(id) FROM escalation_thread_item_response WHERE item_id=?",
                                    (row["id"],)).fetchone()[0]
                it["record"] = {**rec, "table": "escalation_thread_item_response", "id": resp, "run_id": run_id}
            else:
                hid, h = x
                w.update("reading_strand_hit", {"id": hid}, {"face": h.get("face"), "reason": h.get("reason"),
                                                             "parties": h.get("parties"),
                                                             "observation_id": h.get("observation"), "run_id": run_id})
                it["record"] = {**rec, "table": "reading_strand_hit", "id": hid, "run_id": run_id}
        added = []
        for at, spec in new_items:
            spec["added"] = items.raise_(spec, f"{at} (reading {r['label']})")
            added.append(spec["added"])
        w.update("reading", {"id": r["id"]}, {"run_id": run_id})
        return written, added
    written, added = nr._atomic(conn, go)
    _save(path, data)
    left = sum(1 for _, _, it in _items_of(data) if it.get("record") is None)
    return (f"reading {r['label']}: {len(plan)} record(s) written ({sum(1 for x in written.values() if x['new'])} "
            f"finding(s) new, {sum(len(x['nodes']) for x in written.values())} node(s)); {len(added)} open item(s) "
            f"added ({', '.join(added) or '-'}); {left} item(s) still without a record\n  ids written back to "
            f"{_rel(root, path)}")


def gate_pre(conn, root: pathlib.Path, r) -> list[str]:
    data = _load(root, r["gap_file"], "the pre-gap JSON")
    out = []
    for sec, i, it in _items_of(data):
        rec, at = it.get("record"), f"{sec}[{i}] {it.get('verse') or it.get('strong') or it.get('item')}"
        if not isinstance(rec, dict):
            out.append(f"{at}: no record")
        elif rec.get("reason") and not rec.get("id"):
            continue
        elif not rec.get("table") or not _row_exists(conn, rec["table"], rec.get("id")):
            out.append(f"{at}: record {rec.get('table')} {rec.get('id')} is not a row that exists (run Gather)")
    for i, s in enumerate(data.get("new_items") or []):
        if not (isinstance(s, dict) and s.get("added")):
            out.append(f"new_items[{i}]: not added (run Gather)")
    return out


# ══ observe (D3 and D4 input) ═══════════════════════════════════════════════════════════════════
def _focus(cfg, conn, vid: int) -> list[dict]:
    """The words in focus in one verse (reading.focus_words, #2273 D8): every M-coded word, every word in
    reading.non_characteristic_strongs, every word tagged T2 (not a function word) or T5."""
    spec = _setting(cfg, "reading.focus_words")
    never = set(_setting(cfg, "reading.non_characteristic_strongs"))
    out, seen = [], set()
    for pos, surface, strong, morph, testament in conn.execute(
            "SELECT position, surface, strong, morph_code, testament FROM verse_lexical WHERE verse_id=? AND deleted=0 "
            "ORDER BY position, id", (vid,)):
        clusters = orec.word_clusters(conn, strong)
        why = []
        if any(c.startswith("M") for c in clusters):
            why.append("M-code")
        if strong in never:
            why.append("never a characteristic (RG-23)")
        for tag in spec["tags"]:
            if tag in clusters:
                prefix = (morph or "")[:2] if testament == "OT" else (morph or "").split("-")[0]
                if tag == "T2" and prefix in spec["function_word_morph"].get(testament, []):
                    continue
                why.append("qualifier (T2)" if tag == "T2" else f"tagged {tag}")
        if why and (strong, pos) not in seen:
            seen.add((strong, pos))
            out.append({"word": f"{surface} ({strong})", "strong": strong, "surface": surface, "morph": morph,
                        "position": pos, "clusters": clusters, "in_focus_as": why, "record": None})
    return out


def _passage(conn, osis: str) -> list[dict]:
    book, ch, v = osis.split(".")
    want = [f"{book}.{ch}.{n}" for n in range(max(1, int(v) - 2), int(v) + 3)]
    rows = {r[0]: r for r in conn.execute("SELECT osisId, reference, text FROM verse WHERE deleted=0 AND osisId IN "
                                          f"({','.join('?' * len(want))})", want)}
    return [{"verse": rows[o][1], "text": rows[o][2]} for o in want if o in rows]


def _findings_on(conn, osis: str) -> list[dict]:
    out = []
    for o in conn.execute("SELECT DISTINCT o.* FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE "
                          "n.verse_reference=? AND o.status<>'withdrawn' ORDER BY o.id", (osis,)):
        nodes = [dict(n) for n in conn.execute(
            "SELECT id node, strong, surface, cluster_code cluster, role, reading_id, disposition FROM ib_node WHERE "
            "observation_id=? AND verse_reference=? AND (disposition IS NULL OR disposition<>'withdrawn')",
            (o["id"], osis))]
        out.append({"observation": o["id"], "stage": o["stage"], "kind": o["tag"], "text": o["obs_text"],
                    "meaning": o["meaning"], "basis": o["basis"], "route": o["route"], "nodes": nodes})
    return out


def observe(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    """The observe JSON, built from the tables once the reading is gathered (RO2: every finding into focus)."""
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "gathered")
    V = []
    for vid in verse_ids(conn, r["id"]):
        v = conn.execute("SELECT osisId, reference, text FROM verse WHERE id=?", (vid,)).fetchone()
        V.append({"verse": v["reference"], "osis": v["osisId"], "text": v["text"], "passage": _passage(conn, v["osisId"]),
                  "findings_in_focus": _findings_on(conn, v["osisId"]), "words": _focus(cfg, conn, vid)})
    in_focus = sorted({f["observation"] for v in V for f in v["findings_in_focus"]})
    C = [{"claim": c["claim_ref"], "status": c["status"], "text": c["claim_text"]}
         for c in scope_claims(conn, r["id"], in_focus)]
    prompts = {}
    for kind, codes in _setting(cfg, "reading.observe_prompts").items():
        prompts[kind] = [{"code": q, "question": t} for q, t in conn.execute(
            f"SELECT question_code, question_text FROM wa_obs_question_catalogue WHERE deleted=0 AND question_code IN "
            f"({','.join('?' * len(codes)) or 'NULL'}) ORDER BY prompt_seq", codes)]
    built = _now()
    data = {"reading": r["label"], "reading_id": r["id"], "objective": r["objective"], "built_at": built,
            "built_from": "the tables (B:114)",
            "how": "Read each verse in its passage with every finding in focus (RO1, RO2). Record findings in "
                   "`findings` (observationrecord's shape: key, kind, text, meaning, implication, basis, route on a "
                   "party or link finding, nodes [{verse, strong, cluster, role}]; a description already live is named "
                   "as existing and gains nodes). Every word in focus needs a node of this reading, or its `record`: "
                   "{\"reason\": ...}, {\"item\": \"OT-nn.n|#n\"} or {\"new_item\": <Open-Item add shape>}. A finding "
                   "no longer supported: `withdraw` [{\"node\": id, \"reason\"} | {\"observation\": id, \"reason\"}]. "
                   "The prompts are the catalogue's questions by kind: a prompt that does not apply is not answered "
                   "(RG-17). Then Reading.ps1 -Step Record -Label " + r["label"] + ".",
            "kinds": orec.kinds(cfg), "prompts": prompts, "claims": C, "verses": V,
            "findings": [], "withdraw": []}
    path = out_dir(cfg, root, r["label"]) / f"{r['label']}-observe.json"
    if path.exists():
        path.replace(path.with_name(f"{r['label']}-observe-{built.replace(':', '').replace('-', '')}.json"))
    _save(path, data)
    nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {
        "observe_file": _rel(root, path), "observe_built_at": built, "run_id": run_id}))
    n_words = sum(len(v["words"]) for v in V)
    return (f"reading {r['label']}: observe JSON built from the tables -- {len(V)} verse(s), {n_words} word(s) in "
            f"focus, {len(in_focus)} finding(s) in focus, {len(C)} claim(s)\n  -> {_rel(root, path)}")


# ══ record (D4 observe written) ═════════════════════════════════════════════════════════════════
def _item_exists(conn, ref: str) -> bool:
    ref = str(ref or "")
    kind = "escalation" if ref.startswith("#") else "thread item" if "." in ref else "thread"
    return bool(ref) and nr._escalation_exists(conn, kind, ref)


def record(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    """-Label [-File <observe JSON>]: the findings, withdrawals and word records written; nothing if any is wrong."""
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "gathered")
    path = _path(root, p.get("File") or r["observe_file"] or "")
    data = _load(root, str(path), "-File")
    if data.get("reading_id") != r["id"] or not r["observe_built_at"] or data.get("built_at") != r["observe_built_at"]:
        raise Refused(f"the file is not the observe JSON built from the tables for reading {r['label']} "
                      f"(built_at {data.get('built_at')!r}, the reading's {r['observe_built_at']!r}): run Observe")
    items = _ReadingItems(cfg, w)
    errors, quotes = [], []
    todo = [(f"findings[{i}] ({f.get('key')})", f) for i, f in enumerate(data.get("findings") or [])
            if isinstance(f, dict) and not f.get("written")]
    fplan = orec.check(cfg, todo, errors, quotes) if todo else []
    raise_words = []
    for v in data.get("verses") or []:
        for j, wd in enumerate(v.get("words") or []):
            rec, at = wd.get("record"), f"{v['verse']} words[{j}] {wd.get('word')}"
            if not rec or (isinstance(rec, dict) and rec.get("added")):
                continue
            if not isinstance(rec, dict) or len([k for k in ("reason", "item", "new_item") if rec.get(k)]) != 1:
                errors.append(f"{at}: record is one of {{\"reason\"}}, {{\"item\"}} or {{\"new_item\"}}")
            elif rec.get("reason") and len(rec["reason"].strip()) < 10:
                errors.append(f"{at}: a reason says why, in words (10 characters or more)")
            elif rec.get("item") and not _item_exists(conn, rec["item"]):
                errors.append(f"{at}: item {rec['item']} does not exist")
            elif rec.get("new_item"):
                if items.check(rec["new_item"], at, errors):
                    raise_words.append((at, wd))
    wd_plan = []
    for i, x in enumerate(data.get("withdraw") or []):
        at = f"withdraw[{i}]"
        if not isinstance(x, dict) or x.get("done"):
            continue
        if len((x.get("reason") or "").strip()) < 10:
            errors.append(f"{at}: a withdrawal needs its reason, in words (RW-01)")
        elif x.get("node") is not None:
            if not conn.execute("SELECT 1 FROM ib_node WHERE id=? AND (disposition IS NULL OR disposition<>'withdrawn')",
                                (x["node"],)).fetchone():
                errors.append(f"{at}: node {x['node']} is not a live node")
            else:
                wd_plan.append(x)
        elif x.get("observation") is not None:
            if not conn.execute("SELECT 1 FROM ib_observation WHERE id=? AND status<>'withdrawn'",
                                (x["observation"],)).fetchone():
                errors.append(f"{at}: observation {x['observation']} is not a live observation")
            else:
                wd_plan.append(x)
        else:
            errors.append(f"{at}: name the node or the observation withdrawn")
    if errors or quotes:
        raise Refused("\n  ".join(["the reading is not recorded:"] + errors + (
            ["quotation(s) not found in the ESV text:"] + quotes if quotes else [])))
    if not fplan and not raise_words and not wd_plan:
        raise Refused("nothing to record: no new finding, no word with a new item, no withdrawal")

    def go():
        _grant_findings(w)
        written = orec.write(conn, fplan, r["id"], run_id) if fplan else {}
        for x in wd_plan:
            if x.get("node") is not None:
                orec.set_disposition(conn, x["node"], "withdrawn", x["reason"].strip(), r["id"], run_id, w.who)
            else:
                orec.withdraw_observation(conn, x["observation"], x["reason"].strip(), r["id"], run_id, w.who)
        added = []
        for at, wd in raise_words:
            wd["record"]["added"] = items.raise_(wd["record"]["new_item"], f"{at} (reading {r['label']})")
            added.append(wd["record"]["added"])
        w.update("reading", {"id": r["id"]}, {"run_id": run_id})
        return written, added
    written, added = nr._atomic(conn, go)
    for f in data.get("findings") or []:
        if isinstance(f, dict) and f.get("key") in written:
            f["written"] = {"observation": written[f["key"]]["observation"], "nodes": written[f["key"]]["nodes"],
                            "run_id": run_id}
    for x in wd_plan:
        x["done"] = run_id
    _save(path, data)
    return (f"reading {r['label']}: {sum(1 for x in written.values() if x['new'])} finding(s) new, "
            f"{sum(1 for x in written.values() if not x['new'])} existing applied, "
            f"{sum(len(x['nodes']) for x in written.values())} node(s); {len(wd_plan)} withdrawal(s); {len(added)} open "
            f"item(s) added ({', '.join(added) or '-'})\n  ids written back to {_rel(root, path)}")


def gate_observe(conn, root: pathlib.Path, r) -> list[str]:
    """Every word in focus has a live node of this reading, an open item or a reason (#2273 D8); every finding in the
    file written; every node of this reading on a word holds its role."""
    if not r["observe_file"]:
        return ["no observe JSON yet (Reading.ps1 -Step Observe, then Record)"]
    data = _load(root, r["observe_file"], "the observe JSON")
    out = []
    for v in data.get("verses") or []:
        for wd in v.get("words") or []:
            if conn.execute("SELECT 1 FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE "
                            "n.reading_id=? AND n.verse_reference=? AND n.strong=? AND o.status<>'withdrawn' AND "
                            "(n.disposition IS NULL OR n.disposition<>'withdrawn')",
                            (r["id"], v["osis"], wd["strong"])).fetchone():
                continue
            rec = wd.get("record") or {}
            if (rec.get("reason") and len(rec["reason"].strip()) >= 10) or rec.get("item") or rec.get("added"):
                continue
            out.append(f"{v['verse']} {wd.get('word')} ({', '.join(wd.get('in_focus_as') or [])}): no finding of this "
                       f"reading applied, no open item, no reason (not_read)")
    for i, f in enumerate(data.get("findings") or []):
        if isinstance(f, dict) and not f.get("written"):
            out.append(f"findings[{i}] ({f.get('key')}): not written (run Record)")
    for n in conn.execute("SELECT id, observation_id FROM ib_node WHERE reading_id=? AND strong IS NOT NULL AND "
                          "verse_reference IS NOT NULL AND role IS NULL", (r["id"],)):
        out.append(f"node {n['id']} (observation {n['observation_id']}): no role (observation_part_missing)")
    return out


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
        gaps = gate_pre(conn, root, r)
        if gaps:
            _gate_fail(r, "pre", gaps)
        nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {"state": "gathered", "gathered_at": _now(),
                                                                      "run_id": run_id}))
        return f"reading {r['label']}: pre gate passed -- gathered (Reading.ps1 -Step Observe next)"
    if r["state"] == "gathered":
        gaps = gate_observe(conn, root, r)
        if gaps:
            _gate_fail(r, "observe", gaps)

        def go():
            w.update("reading", {"id": r["id"]}, {"state": "observed", "observed_at": _now(), "run_id": run_id})
            w._grant("verse_meta")
            return versemeta.mark(conn, verse_ids(conn, r["id"]), "analysed")
        marked = nr._atomic(conn, go)
        return f"reading {r['label']}: observe gate passed -- observed; {marked} verse(s) marked analysed"
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
         f"| Pre | {r['gathered_at'] or r['recorded_at'] or '—'} |", f"| Observe | {r['observed_at'] or '—'} |",
         f"| Claims | {r['synergised_at'] or '—'} |", f"| Narrate | {r['narrated_at'] or '—'} |",
         f"| Published | {r['published_at'] or '—'} |", "",
         f"- Pre-gap JSON: `{r['gap_file']}`", f"- Observe JSON: `{r['observe_file'] or '—'}`",
         f"- Synergy JSON: `{r['synergy_file'] or '—'}`", f"- Narrate JSON: `{r['narrate_file'] or '—'}`",
         f"- Findings applied by this reading: {len({x['observation_id'] for x in nodes})}, on {len(nodes)} node(s)",
         f"- Chapters touched: {', '.join(json.loads(r['chapters'] or '[]')) or '—'}", ""]
    gaps, name = [], None
    if r["state"] == "open":
        gaps, name = gate_pre(conn, root, r), "Pre"
    elif r["state"] == "gathered":
        gaps, name = gate_observe(conn, root, r), "Observe"
    elif r["state"] == "observed":
        gaps, name = gate_post(cfg, root, r), "Claims"
    elif r["state"] == "synergised":
        gaps, name = gate_narrate(cfg, r), "Narrate"
    elif r["state"] == "narrated":
        L += ["## Publish", "", "Publish the touched chapters and copy them to the inbox (Reading.ps1 -Step Publish)."]
    if name:
        L += [f"## {name} gate gaps ({len(gaps)})", ""] + [f"- {g}" for g in gaps]
    data = _load(root, r["gap_file"], "the pre-gap JSON")
    L += ["", "## Pre-gap records", "", "| Section | Items | Written | Named | Reason | None |", "|---|---|---|---|---|---|"]
    for sec, s in (data.get("sections") or {}).items():
        its = s.get("items") or []
        rec = [it.get("record") or {} for it in its]
        L.append(f"| {sec} | {len(its)} | {sum(1 for x in rec if (x.get('new') or x.get('finding')) and x.get('id'))} | "
                 f"{sum(1 for x in rec if x.get('id') and not (x.get('new') or x.get('finding')))} | "
                 f"{sum(1 for x in rec if x.get('reason') and not x.get('id'))} | "
                 f"{sum(1 for it in its if it.get('record') is None)} |")
    return L, f"reading {r['label']}: {r['state']}; {len(gaps)} gap(s) at the current gate"
