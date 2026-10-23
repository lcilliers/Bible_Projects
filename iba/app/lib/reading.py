"""reading.py -- the reading process (escalation #2228; design
`outputs/escalation/2228-reading-process-design-v2-20261023.md`, decisions D-a to D-d of 2026-10-23).

A reading is the work on one scope, served by the escalation that anchors it. It passes three gates in
order, each checked from the tables by the tool, not asserted:

  open      the scope resolved (versescope, its 2,500 review), its verses kept (reading_verse), the scope
            collated (versecollate), and the gap JSON written: one section per recording gap type
            (cfg_enum reading_gap_type, cfg_setting reading.gap_types), each with its guide text
  record    gate 1 work: each item's `record` written -- {"new": ...} to its table, {"table", "id"} an
            existing row, {"reason": ...} nothing to record -- and the ids written back into the file;
            new open items through the open-item tool (D-b)
  check     the gate the reading is at: gate 1 (every item has an id that exists or a reason; the verses
            are then marked analysed, D-c) or gate 2 (every observation on the scope carried by a claim or
            disposed, every claim told or held, every matched open item settled)
  synergy   gate 2 input: the synergy JSON built by reading all the tables for the scope, never memory (B:114)
  apply     gate 2 work: claims and dispositions (strandreading.derive_core), tellings, blocks rewritten
            (narrativeregister.rewrite), open items settled or carried forward (D-b)
  publish   gate 3: the touched chapters published from the database, copied to the learning4comfort inbox,
            checked byte-identical
  account   the reading from the tables (read-only)

Open items are read at gate 1 and closed only at gate 2 (design v2). Writes go through
narrativeregister.Writer (cfg_write_grant); observations through recordingpass; thread items through
escalation and openitem. Every write step validates first and raises Refused with nothing written.
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
from . import openitem
from . import recordingpass
from . import strandreading as sr
from . import versecollate as vc
from . import versemeta
from . import versescope as vs
from .db import Db

Refused = nr.Refused
STATES = ("open", "recorded", "synergised", "published")
GAP_OF = {"not read": "not_read", "read in files only": "read_in_files_only", "hit unread": "hit_unread",
          "meaning missing": "meaning_missing", "open item": "open_item"}
NOT_SCOPE = ("Label", "Escalation", "Home", "By", "File", "Note")
SETTLE = ("closed", "withdrawn", "superseded", "forward", "touched")
PART_MARK = "read in part"      # a gate 2 `touched` response: the item reaches past the reading (#2250 option A)


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ══ lookups ═════════════════════════════════════════════════════════════════════════════════════
def gap_types(cfg) -> dict:
    """{type: {"phase", "records_in", "guide"}} in enum order; every enum value has its entry and no more."""
    spec = cfg.required_setting("reading.gap_types")
    spec = json.loads(spec) if isinstance(spec, str) else spec
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


def _load(root: pathlib.Path, path: str | None, what: str) -> dict:
    f = pathlib.Path(path or "")
    if not f.is_absolute():
        f = root / f
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
    """(section, index, item) for every item of the gap JSON."""
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


# ══ open ════════════════════════════════════════════════════════════════════════════════════════
def open_(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path, file_request: dict | None) -> str:
    """-Label -Escalation -Home <scope selectors as Verse-Scope.ps1> [-Reviewed] [-File request]."""
    conn = cfg.conn
    label = (p.get("Label") or "").strip()
    if not label or label != label.lower() or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", label):
        raise Refused("-Label is the reading's name, lowercase-hyphenated (e.g. anger-bosom)")
    if conn.execute("SELECT 1 FROM reading WHERE label=?", (label,)).fetchone():
        raise Refused(f"reading {label} already exists")
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
        raise Refused(f"-Home {home!r} is not a cluster (the cluster new observations are grounded under)")
    types = gap_types(cfg)
    request = vs.normalise_request({k: v for k, v in p.items() if k not in NOT_SCOPE}, file_request)
    try:
        col = vc.collate(cfg, request, root)
    except (vs.ScopeError, vc.CollateError) as exc:
        raise Refused(str(exc)) from exc
    sections = {t: {"guide": x["guide"], "records_in": x["records_in"], "items": []}
                for t, x in types.items() if x["phase"] == "recording"}
    meaning: dict[str, dict] = {}
    items: dict[str, dict] = {}
    for v in col["verses"]:
        words = sorted({f"{x['surface']} ({x['strong']}, {x['cluster']})" for x in v["words"]})
        gaps = set(v["gaps"])
        if "read in files only" in gaps and "read_in_files_only" in sections:
            sections["read_in_files_only"]["items"].append({
                "verse": v["reference"], "words": words, "text": v["text"],
                "file_lines": [f"{x['file']}:{x['line']} {x['text']}" for x in v["file_lines"]], "record": None})
        elif "not read" in gaps and "not_read" in sections:
            sections["not_read"]["items"].append({"verse": v["reference"], "words": words, "text": v["text"],
                                                  "known": f"file lines: {len(v['file_lines'])}", "record": None})
        for h in v["strand_hits"]:
            if not h["face"] and not h["reason"] and "hit_unread" in sections:
                sections["hit_unread"]["items"].append({"verse": v["reference"], "strand": h["strand"],
                                                        "strong": h["strong"], "surface": h["surface"], "record": None})
        for x in v["words"]:
            lx = col["lexicon"].get(x["strong"], {})
            miss = [m for m, gone in (("meaning senses", not lx.get("meaning")),
                                      ("Mounce", x["strong"].startswith("G") and not lx.get("mounce"))) if gone]
            if miss:
                meaning.setdefault(x["strong"], {"strong": x["strong"], "missing": miss, "verses": [], "record": None})
                if v["reference"] not in meaning[x["strong"]]["verses"]:
                    meaning[x["strong"]]["verses"].append(v["reference"])
        for o in v["open_items"]:
            it = items.setdefault(o["item"], {"item": o["item"], "value": o["value"], "read_for": None,
                                              "note": o["note"], "verses": [], "record": None})
            if v["reference"] not in it["verses"]:
                it["verses"].append(v["reference"])
    for ref, it in items.items():
        _, row = _thread_item(conn, ref)
        it["read_for"] = row["read_for"]
    if "meaning_missing" in sections:
        sections["meaning_missing"]["items"] = list(meaning.values())
    if "open_item" in sections:
        sections["open_item"]["items"] = list(items.values())
    folder = out_dir(cfg, root, label)
    gap_path = folder / f"{label}-gaps.json"
    if gap_path.exists():
        raise Refused(f"{_rel(root, gap_path)} is already on disk")

    def go():
        rid = w.insert("reading", {"label": label, "escalation_id": eid, "home_cluster": home,
                                   "request": json.dumps(col["scope"]["request"], ensure_ascii=False),
                                   "gap_file": _rel(root, gap_path), "note": p.get("Note"), "run_id": run_id})
        for v in col["verses"]:
            w.insert("reading_verse", {"reading_id": rid, "verse_id": v["verse_id"],
                                       "routes": json.dumps(v["routes"], ensure_ascii=False)})
        return rid
    rid = nr._atomic(conn, go)
    data = {"reading": label, "reading_id": rid, "escalation": eid, "home": home, "opened": _now(),
            "scope": col["scope"]["selectors"],
            "how": "Fill each item's `record` with one of {\"new\": {...}}, {\"table\": \"...\", \"id\": n} or "
                   "{\"reason\": \"...\"}, then Reading.ps1 -Step Record -Label " + label + " -File <this file>. "
                   "New open items go in `new_items` (the Open-Item.ps1 -Action Add shape, D-b).",
            "new_items": [], "sections": sections}
    _save(gap_path, data)
    _save(folder / f"{label}-collation.json", {"label": label, "run_id": run_id, **col})
    n = {k: len(s["items"]) for k, s in sections.items()}
    return (f"reading {label} opened (#{eid}, home {home}): {len(col['verses'])} verse(s); gaps "
            + ", ".join(f"{k} {v}" for k, v in n.items()) + f"\n  -> {_rel(root, gap_path)}")


# ══ record (gate 1 work) ════════════════════════════════════════════════════════════════════════
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


def record(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    """-Label -File <gap JSON>: every filled `record` written or checked; nothing is written if any is wrong."""
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "open")
    path = pathlib.Path(p.get("File") or r["gap_file"])
    path = path if path.is_absolute() else root / path
    data = _load(root, str(path), "-File")
    if data.get("reading_id") != r["id"]:
        raise Refused(f"the file is the gap JSON of reading {data.get('reading')!r} (id {data.get('reading_id')}), "
                      f"not {r['label']} (id {r['id']})")
    types = gap_types(cfg)
    vx = nr.VerseIndex(cfg)
    items = _ReadingItems(cfg, w)
    errors, quotes, plan, obs_entries = [], [], [], []
    for sec, i, it in _items_of(data):
        rec, at = it.get("record"), f"{sec}[{i}] ({it.get('verse') or it.get('strong') or it.get('item')})"
        if rec is None or (isinstance(rec, dict) and rec.get("run_id") and rec.get("id") is not None):
            continue                                   # not yet, or written by an earlier Record (checked at Check)
        if not isinstance(rec, dict) or len([k for k in ("new", "reason", "table") if rec.get(k)]) != 1:
            errors.append(f"{at}: record is one of {{\"new\": ...}}, {{\"table\", \"id\"}} or {{\"reason\"}}")
            continue
        if rec.get("reason"):
            if len(rec["reason"].strip()) < 10:
                errors.append(f"{at}: a reason says why, in words (10 characters or more)")
            continue
        if rec.get("table"):
            if rec["table"] not in types[sec]["records_in"]:
                errors.append(f"{at}: {sec} records into {types[sec]['records_in']}, not {rec['table']}")
            elif not _row_exists(conn, rec["table"], rec.get("id")):
                errors.append(f"{at}: {rec['table']} {rec.get('id')} does not exist")
            continue
        new = rec["new"]
        if sec in ("not_read", "read_in_files_only") or (sec == "open_item" and "text" in new):
            key = f"{sec}:{i}"
            obs_entries.append((at, {**new, "key": key}))
            plan.append(("obs", it, key, sec))
        elif sec == "open_item":
            if len((new.get("response") or "").strip()) < 10:
                errors.append(f"{at}: new is an observation (text, meaning, basis, verses) or {{\"response\": "
                              f"what the reading found}}")
                continue
            try:
                _thread_item(conn, it["item"])
            except Refused as exc:
                errors.append(f"{at}: {exc}")
                continue
            plan.append(("touch", it, new["response"].strip(), sec))
        elif sec == "hit_unread":
            hit = conn.execute("SELECT h.id FROM reading_strand_hit h JOIN reading_strand s ON s.id=h.strand_id JOIN "
                               "verse v ON v.id=h.verse_id WHERE s.code=? AND h.strong=? AND v.reference=?",
                               (it.get("strand"), it.get("strong"), it.get("verse"))).fetchone()
            if hit is None:
                errors.append(f"{at}: no strand hit {it.get('strand')} {it.get('strong')} at {it.get('verse')}")
                continue
            if bool((new.get("face") or "").strip()) == bool((new.get("reason") or "").strip()):
                errors.append(f"{at}: give a face or a reason, one of them")
            ob = new.get("observation")
            if ob is not None and not conn.execute("SELECT 1 FROM ib_observation WHERE id=? AND status<>'withdrawn'",
                                                   (ob,)).fetchone():
                errors.append(f"{at}: observation {ob} is not a live observation")
            plan.append(("hit", it, (hit["id"], new), sec))
        else:
            errors.append(f"{at}: {sec} takes no new row here -- pull it through its own route and name the row "
                          f"({{\"table\", \"id\"}}), or give a reason")
    obs = sr.check_observations(cfg, vx, obs_entries, errors, quotes)
    new_items = [(f"new_items[{i}]", items.check(s, f"new_items[{i}]", errors))
                 for i, s in enumerate(data.get("new_items") or []) if not (isinstance(s, dict) and s.get("added"))]
    if errors or quotes:
        raise Refused("\n  ".join(["the reading is not recorded:"] + errors + (
            ["quotation(s) not found in the ESV text:"] + quotes if quotes else [])))
    if not plan and not new_items:
        raise Refused("nothing to record: no item has a new record, and no new item is listed")

    def go():
        w._grant("ib_observation")
        w._grant("ib_node")
        ids = recordingpass.record_strand_observations(conn, r["home_cluster"], run_id, obs) if obs else {}
        for kind, it, x, sec in plan:
            if kind == "obs":
                it["record"] = {"table": "ib_observation", "id": ids[x], "run_id": run_id, "new": it["record"]["new"]}
            elif kind == "touch":
                t, row = _thread_item(conn, it["item"])
                try:
                    escalation.update(cfg, Db(cfg), t["id"], item_refs=[str(row["item_no"])], response_kind="touched",
                                      respond=f"{x} (reading {r['label']}, #2228 gate 1)", via=r["escalation_id"],
                                      originator=w.who)
                except ValueError as exc:
                    raise Refused(f"{it['item']}: {exc}") from exc
                resp = conn.execute("SELECT MAX(id) FROM escalation_thread_item_response WHERE item_id=?",
                                    (row["id"],)).fetchone()[0]
                it["record"] = {"table": "escalation_thread_item_response", "id": resp, "run_id": run_id,
                                "new": it["record"]["new"]}
            else:
                hid, new = x
                w.update("reading_strand_hit", {"id": hid}, {"face": new.get("face"), "reason": new.get("reason"),
                                                             "parties": new.get("parties"),
                                                             "observation_id": new.get("observation"), "run_id": run_id})
                it["record"] = {"table": "reading_strand_hit", "id": hid, "run_id": run_id, "new": new}
        added = []
        for at, spec in new_items:
            ref = items.raise_(spec, f"{at} (reading {r['label']})")
            spec["added"] = ref
            added.append(ref)
        w.update("reading", {"id": r["id"]}, {"run_id": run_id})
        return len(ids), added
    n_obs, added = nr._atomic(conn, go)
    _save(path, data)
    left = sum(1 for _, _, it in _items_of(data) if it.get("record") is None)
    return (f"reading {r['label']}: {len(plan)} record(s) written ({n_obs} observation(s)); {len(added)} open item(s) "
            f"added ({', '.join(added) or '-'}); {left} item(s) still without a record\n  ids written back to "
            f"{_rel(root, path)}")


# ══ check (gates 1 and 2) ═══════════════════════════════════════════════════════════════════════
def gate1_gaps(conn, root: pathlib.Path, r) -> list[str]:
    data = _load(root, r["gap_file"], "the gap JSON")
    out = []
    for sec, i, it in _items_of(data):
        rec, at = it.get("record"), f"{sec}[{i}] {it.get('verse') or it.get('strong') or it.get('item')}"
        if not isinstance(rec, dict):
            out.append(f"{at}: no record")
        elif rec.get("reason"):
            continue
        elif not rec.get("table") or not _row_exists(conn, rec["table"], rec.get("id")):
            out.append(f"{at}: record {rec.get('table')} {rec.get('id')} is not a row that exists"
                       + (" (run Record)" if rec.get("new") and not rec.get("id") else ""))
    for i, s in enumerate(data.get("new_items") or []):
        if not (isinstance(s, dict) and s.get("added")):
            out.append(f"new_items[{i}]: not added (run Record)")
    return out


def scope_observations(conn, rid: int) -> list:
    return conn.execute(
        "SELECT DISTINCT o.* FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id JOIN verse v ON "
        "v.osisId=n.verse_reference JOIN reading_verse rv ON rv.verse_id=v.id WHERE rv.reading_id=? AND "
        "o.status<>'withdrawn' ORDER BY o.id", (rid,)).fetchall()


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
                        "LIKE ?", (row["id"], f"%(reading {label}, #2228 gate 2, {PART_MARK})%")).fetchone() is not None


def gate2_gaps(cfg, root: pathlib.Path, r) -> list[str]:
    """Every observation on the scope carried by a current claim or disposed (open = held on an item, silent);
    every current claim on the scope told; every open item matched to the scope settled, or, when its target
    reaches past the reading, recorded as read in part (#2250)."""
    conn = cfg.conn
    out = []
    obs = scope_observations(conn, r["id"])
    for o in obs:
        if not _carried(conn, o["id"]) and o["status"] not in ("open", "silent"):
            out.append(f"observation {o['id']} ({o['status']}): no current claim carries it and it has no disposition")
    for c in scope_claims(conn, r["id"], [o["id"] for o in obs]):
        if c["status"] == "current" and not c["in_narrative"]:
            out.append(f"{c['claim_ref']}: current and told in no block (tell it, or hold it)")
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


def check(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    conn = cfg.conn
    r = reading(conn, p.get("Label"))
    if r["state"] == "open":
        gaps = gate1_gaps(conn, root, r)
        if gaps:
            raise Refused("\n  ".join([f"reading {r['label']} is not past gate 1 ({len(gaps)} gap(s)):"] + gaps[:60]
                                      + ([f"... and {len(gaps) - 60} more"] if len(gaps) > 60 else [])))

        def go():
            w.update("reading", {"id": r["id"]}, {"state": "recorded", "recorded_at": _now(), "run_id": run_id})
            w._grant("verse_meta")
            return versemeta.mark(conn, verse_ids(conn, r["id"]), "analysed")
        marked = nr._atomic(conn, go)
        return f"reading {r['label']}: gate 1 passed -- recorded; {marked} verse(s) marked analysed (D-c)"
    if r["state"] == "recorded":
        if not r["synergy_file"]:
            raise Refused(f"reading {r['label']} has no synergy JSON yet (Reading.ps1 -Step Synergy, then Apply)")
        gaps = gate2_gaps(cfg, root, r)
        if gaps:
            raise Refused("\n  ".join([f"reading {r['label']} is not past gate 2 ({len(gaps)} gap(s)):"] + gaps[:60]
                                      + ([f"... and {len(gaps) - 60} more"] if len(gaps) > 60 else [])))
        nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]},
                                          {"state": "synergised", "synergised_at": _now(), "run_id": run_id}))
        return f"reading {r['label']}: gate 2 passed -- synergised (Reading.ps1 -Step Publish next)"
    raise Refused(f"reading {r['label']} is {r['state']}; Check runs at gate 1 (open) or gate 2 (recorded)")


# ══ synergy (gate 2 input) ══════════════════════════════════════════════════════════════════════
def synergy(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    """The synergy JSON, built by reading the tables for the scope (B:114): observations, claims, blocks and the
    open items matched to the scope, each with the field to fill."""
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "recorded")
    vids = verse_ids(conn, r["id"])
    obs = scope_observations(conn, r["id"])
    oids = [o["id"] for o in obs]
    O = []
    for o in obs:
        vs_ = [x[0] for x in conn.execute("SELECT DISTINCT verse_reference FROM ib_node WHERE observation_id=? AND "
                                          "verse_reference IS NOT NULL ORDER BY seq", (o["id"],))]
        cl = [x[0] for x in conn.execute("SELECT DISTINCT c.claim_ref FROM narrative_claim_source cs JOIN narrative_claim "
                                         "c ON c.id=cs.claim_id WHERE cs.observation_id=? AND c.status='current'",
                                         (o["id"],))]
        O.append({"observation": o["id"], "stage": o["stage"], "status": o["status"], "text": o["obs_text"],
                  "meaning": o["meaning"], "verses": vs_, "carried_by": cl, "claim": None, "disposition": None})
    claims = scope_claims(conn, r["id"], oids)
    C = [{"claim": c["claim_ref"], "status": c["status"], "text": c["claim_text"],
          "told_in": nr._told_in(conn, c["id"]), "tell": None, "hold": None, "edit": None, "withdraw": None}
         for c in claims]
    cids = [c["id"] for c in claims]
    J = json.dumps(vids)
    B = []
    for b in conn.execute(
            f"SELECT DISTINCT s.id, s.heading, s.block_text, ch.chapter_no, ps.heading parent FROM narrative_section s "
            f"JOIN narrative_chapter ch ON ch.id=s.chapter_id AND ch.inactive=0 LEFT JOIN narrative_section ps ON "
            f"ps.id=s.parent_section_id WHERE s.last_version IS NULL AND (s.id IN (SELECT section_id FROM "
            f"narrative_citation WHERE last_version IS NULL AND verse_id IN (SELECT value FROM json_each(?))) OR s.id IN "
            f"(SELECT section_id FROM narrative_claim_telling WHERE status='current' AND claim_id IN "
            f"({','.join('?' * len(cids)) or 'NULL'}))) ORDER BY ch.reading_order, s.ordinal", (J, *cids)):
        B.append({"chapter": b["chapter_no"], "section": f"{b['parent']} > {b['heading']}" if b["parent"] else b["heading"],
                  "text": b["block_text"]})
    gap = _load(root, r["gap_file"], "the gap JSON")
    found = {it["item"]: it.get("record") for it in (gap.get("sections", {}).get("open_item", {}).get("items") or [])}
    refs = [x[0] for x in conn.execute("SELECT reference FROM verse WHERE id IN (SELECT value FROM json_each(?))", (J,))]
    for t, it, _ in escalation.match_open_items(Db(cfg), verses=refs, home=False):
        found.setdefault(f"{t['alias']}.{it['item_no']}", None)
    I = []
    for ref, rec in found.items():
        _, row = _thread_item(conn, ref)
        if row["status"] == "open":
            I.append({"item": ref, "value": row["value"], "read_for": row["read_for"] or row["note"],
                      "gate1": rec, "settle": None})
    built = _now()
    data = {"reading": r["label"], "reading_id": r["id"], "built_at": built, "built_from": "the tables (B:114)",
            "how": "Fill: observations[].claim (a claim ref or a new_claims key) or .disposition {\"as\": \"held\", "
                   "\"item\": \"OT-nn.n|#n\"} | {\"as\": \"held\", \"new_item\": {Open-Item add shape}} | {\"as\": "
                   "\"silent|withdrawn\", \"reason\"}; claims[].tell [{\"chapter\", \"section\", \"kind\", \"part\"}], "
                   ".hold \"<reason>\", .edit {text, beyond_text, verdict, sources, observations}, .withdraw "
                   "\"<why>\"; new_claims [{key, text, beyond_text, verdict, sources, observations, tell}]; rewrite: "
                   "the Narrative rewrite shape (update, refs, blocks) or null; open_items[].settle {\"as\": "
                   "\"closed\", \"answer\"} | {\"as\": \"withdrawn\", \"reason\"} | {\"as\": \"superseded\", \"by\"} | "
                   "{\"as\": \"forward\", \"new_item\": {Open-Item add shape}} | {\"as\": \"touched\", \"found\"} "
                   "(only for an item whose target reaches past the reading: it stays open). Then Reading.ps1 "
                   "-Step Apply.",
            "observations": O, "claims": C, "new_claims": [], "blocks": B, "rewrite": None, "open_items": I}
    path = out_dir(cfg, root, r["label"]) / f"{r['label']}-synergy.json"
    if path.exists():
        path.replace(path.with_name(f"{r['label']}-synergy-{built.replace(':', '').replace('-', '')}.json"))
    _save(path, data)
    nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {
        "synergy_file": _rel(root, path), "synergy_built_at": built, "run_id": run_id}))
    return (f"reading {r['label']}: synergy built from the tables -- {len(O)} observation(s), {len(C)} claim(s), "
            f"{len(B)} block(s), {len(I)} open item(s)\n  -> {_rel(root, path)}")


# ══ apply (gate 2 work) ═════════════════════════════════════════════════════════════════════════
def apply(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "recorded")
    path = pathlib.Path(p.get("File") or r["synergy_file"] or "")
    path = path if path.is_absolute() else root / path
    data = _load(root, str(path), "-File")
    if data.get("reading_id") != r["id"] or not r["synergy_built_at"] or data.get("built_at") != r["synergy_built_at"]:
        raise Refused(f"the file is not the synergy JSON built from the tables for reading {r['label']} "
                      f"(built_at {data.get('built_at')!r}, the reading's {r['synergy_built_at']!r}): run Synergy")
    mine = {o["id"] for o in scope_observations(conn, r["id"])}
    items = _ReadingItems(cfg, w)
    errors, derive = [], {"claims": [], "dispositions": []}
    tells = []
    for i, n in enumerate(data.get("new_claims") or []):
        derive["claims"].append({"key": n.get("key"), "new": {k: n.get(k) for k in (
            "text", "beyond_text", "verdict", "sources", "observations")}})
        tells += [(f"new_claims[{i}]", n.get("key"), t) for t in n.get("tell") or []]
    for i, c in enumerate(data.get("claims") or []):
        at = f"claims[{i}] ({c.get('claim')})"
        if c.get("withdraw"):
            derive["claims"].append({"claim": c["claim"], "withdraw": c["withdraw"]})
        elif c.get("edit"):
            derive["claims"].append({"claim": c["claim"], "edit": c["edit"]})
        if c.get("hold") and (c.get("tell") or c.get("withdraw")):
            errors.append(f"{at}: hold stands alone (not with tell or withdraw)")
        tells += [(at, c["claim"], t) for t in c.get("tell") or []]
    for i, o in enumerate(data.get("observations") or []):
        at = f"observations[{i}] ({o.get('observation')})"
        if o.get("claim") and o.get("disposition"):
            errors.append(f"{at}: give claim or disposition, not both")
        elif o.get("claim"):
            derive["dispositions"].append({"observation": o["observation"], "as": "claim", "claim": o["claim"]})
        elif o.get("disposition"):
            derive["dispositions"].append({"observation": o["observation"], **o["disposition"]})
    kinds = cfg.enum("narrative_telling_kind")
    tell_plan = []
    for at, ref, t in tells:
        try:
            ch = nr._chapter(conn, str(t.get("chapter")))
            sec = nr._block(conn, ch, t.get("section"))
            kind = t.get("kind") or "in full"
            nr._check_enum(kinds, kind, f"{at} kind")
            if kind == "in part" and not (t.get("part") or "").strip():
                raise Refused("told 'in part' with no part")
            tell_plan.append((ref, sec, kind, t.get("part"), ch["chapter_no"]))
        except Refused as exc:
            errors.append(f"{at} tell: {exc}")
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
    if errors:
        raise Refused("\n  ".join(["the synergy is not applied:"] + errors))
    provenance = f"Reading.ps1 -Step Apply -Label {r['label']}"
    holds = [c["claim"] for c in data.get("claims") or [] if c.get("hold")]
    if not (derive["claims"] or derive["dispositions"] or tell_plan or holds or settle or data.get("rewrite")):
        raise Refused("nothing to apply: the synergy JSON has no filled field")

    def go():
        made, n = (sr.derive_core(cfg, w, derive, run_id, mine, provenance, items, "the reading's")
                   if derive["claims"] or derive["dispositions"] else ([], {"new": 0, "edit": 0, "withdraw": 0,
                                                                          "disposed": 0, "keys": {}}))
        since = nr._max_change_id(conn)
        chapters = set()
        for ref, sec, kind, part, chno in tell_plan:
            cid = n["keys"].get(ref) or nr._claim(conn, ref)["id"]
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
        settled = []
        for ref, how, s in settle:
            t, row = _thread_item(conn, ref)
            if how == "forward":
                new_ref = items.raise_(s["checked"], f"{ref} carried forward")
                how, text = "superseded", f"carried forward to {new_ref} (reading {r['label']}, #2228 gate 2)"
            elif how == "touched":
                text = f"{s['found']} (reading {r['label']}, #2228 gate 2, {PART_MARK})"
            else:
                text = {"closed": s.get("answer"), "withdrawn": s.get("reason"),
                        "superseded": s.get("by")}[how] + f" (reading {r['label']}, #2228 gate 2)"
            try:
                escalation.update(cfg, Db(cfg), t["id"], item_refs=[str(row["item_no"])], response_kind=how,
                                  respond=text, via=r["escalation_id"], originator=w.who)
            except ValueError as exc:
                raise Refused(f"{ref}: {exc}") from exc
            settled.append(f"{ref} {how}")
        prev = set(json.loads(r["chapters"] or "[]"))
        w.update("reading", {"id": r["id"]}, {"chapters": json.dumps(sorted(prev | chapters)), "run_id": run_id})
        return made, n, len(tell_plan), rw, settled
    conn.execute("SAVEPOINT reading_apply")
    try:
        made, n, told, rw, settled = go()
    except BaseException:
        conn.execute("ROLLBACK TO reading_apply")
        conn.execute("RELEASE reading_apply")
        raise
    conn.execute("RELEASE reading_apply")
    return (f"reading {r['label']}: {n['new']} new claim(s) ({', '.join(made) or '-'}), {n['edit']} adjusted, "
            f"{n['withdraw']} withdrawn, {len(holds)} held; {n['disposed']} observation(s) disposed; {told} telling(s); "
            f"{'blocks rewritten (update ' + str(rw['update_id']) + ')' if rw else 'no block rewritten'}; "
            f"{len(settled)} open item(s) settled ({', '.join(settled) or '-'}). Next: Reading.ps1 -Step Check")


# ══ publish (gate 3) ════════════════════════════════════════════════════════════════════════════
def _sha(path: pathlib.Path) -> str | None:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def publish(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "synergised")
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
                      f"synergised\n  {report.getvalue().strip()}")
    bad = []
    for no in nos:
        ch = nr._chapter(conn, str(no))
        src = nr.chapter_dir(cfg) / ch["current_file"]
        if _sha(src) is None or _sha(src) != _sha(target / ch["current_file"]):
            bad.append(f"Ch {no} {ch['current_file']}")
    if bad:
        raise Refused(f"not byte-identical in the inbox: {', '.join(bad)}; the reading stays synergised")
    nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {"state": "published", "published_at": _now(),
                                                                  "run_id": run_id}))
    return (f"reading {r['label']}: gate 3 passed -- published; {len(nos)} chapter(s) touched "
            f"({', '.join(map(str, nos)) or '-'}), {len(published)} newly published ({', '.join(published) or '-'}); "
            f"all in the inbox byte-identical")


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
    L = [f"# Reading account: {r['label']}", "",
         f"Escalation #{r['escalation_id']} · home {r['home_cluster']} · {n} verse(s) · state **{r['state']}**", "",
         "| Gate | Passed |", "|---|---|",
         f"| 1 Recorded | {r['recorded_at'] or '—'} |", f"| 2 Synergised | {r['synergised_at'] or '—'} |",
         f"| 3 Published | {r['published_at'] or '—'} |", "",
         f"- Gap JSON: `{r['gap_file']}`", f"- Synergy JSON: `{r['synergy_file'] or '—'}`",
         f"- Chapters touched: {', '.join(json.loads(r['chapters'] or '[]')) or '—'}", ""]
    gaps = []
    if r["state"] == "open":
        gaps = gate1_gaps(conn, root, r)
        L += [f"## Gate 1 gaps ({len(gaps)})", ""] + [f"- {g}" for g in gaps]
    elif r["state"] == "recorded":
        gaps = gate2_gaps(cfg, root, r) if r["synergy_file"] else ["no synergy JSON yet (Reading.ps1 -Step Synergy)"]
        L += [f"## Gate 2 gaps ({len(gaps)})", ""] + [f"- {g}" for g in gaps]
    elif r["state"] == "synergised":
        L += ["## Gate 3", "", "Publish the touched chapters and copy them to the inbox (Reading.ps1 -Step Publish)."]
    data = _load(root, r["gap_file"], "the gap JSON")
    L += ["", "## Gate 1 records", "", "| Section | Items | Written | Named | Reason | None |", "|---|---|---|---|---|---|"]
    for sec, s in (data.get("sections") or {}).items():
        its = s.get("items") or []
        rec = [it.get("record") or {} for it in its]
        L.append(f"| {sec} | {len(its)} | {sum(1 for x in rec if x.get('new') and x.get('id'))} | "
                 f"{sum(1 for x in rec if x.get('id') and not x.get('new'))} | {sum(1 for x in rec if x.get('reason'))} | "
                 f"{sum(1 for it in its if it.get('record') is None)} |")
    return L, f"reading {r['label']}: {r['state']}; {len(gaps)} gap(s) at the current gate"
