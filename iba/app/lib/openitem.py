"""openitem.py -- registering open items to a clear purpose (escalation #2236; design
outputs/escalation/2236-open-item-design-v2-20261023.md, on the researcher's decisions of 2026-10-23).

An open item is a pointer from the analysis in hand to related work that does not interrupt it. A worded item
(kind 'scope') carries: its thread (the purpose of the read), its origin (the escalation) and anchor (strong,
verse, observation, claim or block of that analysis), its target -- a target cluster with target term(s) read
against the source term(s), or verses -- the target verses computed and kept (escalation_thread_item_verse), what
to read for, why it is open, and when it comes back. An item without a clear purpose is refused; a target over
open_item.max_verses is refused, to be split into separate items, one purpose each.

Thread changes go through escalation.update (item added, history, lifecycle E:18); the worded fields and the
target verses are written by the step's own grants. Reword keeps the earlier wording in the item's history (a
'note' response), so the live row holds only the current wording.
"""
from __future__ import annotations

import datetime
import json
import re

from . import escalation
from . import versescope as vs

ANCHOR_KINDS = ("strong", "verse", "observation", "claim", "block")
TEXT_FIELDS = ("read_for", "why", "comes_back_when")


class ItemError(ValueError):
    """An item that cannot be registered as given."""


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _list(v) -> list[str]:
    if v is None:
        return []
    if isinstance(v, (list, tuple)):
        return [str(x).strip() for x in v if str(x).strip()]
    return [x.strip() for x in str(v).split(",") if x.strip()]


def spec_from(params: dict) -> dict:
    """PS parameters (any case) or a request-file object as one item spec."""
    p = {k.lower(): v for k, v in params.items()}
    return {"thread": p.get("thread"), "item": p.get("item"), "origin": p.get("origin"), "anchor": p.get("anchor"),
            "source": _list(p.get("source")), "target_cluster": (p.get("targetcluster") or p.get("target_cluster") or "").strip() or None,
            "target_terms": _list(p.get("targetterms") or p.get("target_terms")), "verse": p.get("verse"),
            "read_for": (p.get("readfor") or p.get("read_for") or "").strip(), "why": (p.get("why") or "").strip(),
            "comes_back_when": (p.get("comesbackwhen") or p.get("comes_back_when") or "").strip()}


def _thread(conn, ref: str):
    m = re.fullmatch(r"OT-0*(\d+)", (ref or "").strip(), re.I)
    if not m:
        raise ItemError(f"-Thread {ref!r} is not a thread (OT-nn)")
    row = conn.execute("SELECT * FROM escalation WHERE type='thread' AND CAST(substr(alias, 4) AS INTEGER)=?",
                       (int(m.group(1)),)).fetchone()
    if row is None:
        raise ItemError(f"thread {ref!r} does not exist")
    if row["state"] not in ("on-hold", "in-progress"):
        raise ItemError(f"thread {row['alias']} is {row['state']}; an item goes on an open thread")
    return row


def _item(conn, ref: str):
    m = re.fullmatch(r"(OT-\d+)\.(\d+)", (ref or "").strip(), re.I)
    if not m:
        raise ItemError(f"-Item {ref!r} is not a thread item (OT-nn.n)")
    t = _thread(conn, m.group(1))
    it = conn.execute("SELECT * FROM escalation_thread_item WHERE escalation_id=? AND item_no=?",
                      (t["id"], int(m.group(2)))).fetchone()
    if it is None:
        raise ItemError(f"item {ref} does not exist")
    if it["status"] != "open":
        raise ItemError(f"item {ref} is {it['status']}; only an open item is reworded or split")
    return t, it


def _check_anchor(cfg, r: vs.Resolver, anchor: str) -> str:
    kind, _, value = (anchor or "").partition(":")
    kind, value = kind.strip().lower(), value.strip()
    if kind not in ANCHOR_KINDS or not value:
        raise ItemError(f"-Anchor {anchor!r} must be one of {', '.join(k + ':<value>' for k in ANCHOR_KINDS)}")
    conn = cfg.conn
    if kind == "strong":
        value = ",".join(r.decompose(value))
    elif kind == "verse":
        if not [x for x in vs.nr.parse_refs(value, r.vx) if x.verse_id]:
            raise ItemError(f"-Anchor verse {value!r} does not resolve to a verse")
    elif kind == "observation":
        if not conn.execute("SELECT 1 FROM ib_observation WHERE id=?", (value,)).fetchone():
            raise ItemError(f"-Anchor observation {value} does not exist")
    elif kind == "claim":
        if not conn.execute("SELECT 1 FROM narrative_claim WHERE claim_ref=?", (value,)).fetchone():
            raise ItemError(f"-Anchor claim {value} is not in the register")
    else:
        ch, _, head = value.partition("/")
        try:
            r.chapter(ch.strip(), head.strip() or None)
        except vs.ScopeError as exc:
            raise ItemError(f"-Anchor block {value!r}: {exc}") from exc
    return f"{kind}:{value}"


def resolve_target(cfg, spec: dict) -> dict:
    """The item's target: verse ids and how they were found. Refused when it does not resolve, holds no verse,
    or is wider than open_item.max_verses."""
    r = vs.Resolver(cfg)
    limit = int(cfg.required_setting("open_item.max_verses"))
    conn = cfg.conn
    with_terms = bool(spec.get("target_cluster") or spec.get("target_terms"))
    if spec.get("verse") and with_terms and not (spec.get("source") and spec.get("target_cluster") and spec.get("target_terms")):
        raise ItemError("-Verse with a cluster target needs all of -Source, -TargetCluster and -TargetTerms")
    if spec.get("verse"):
        try:
            r.verse(str(spec["verse"]))
        except vs.ScopeError as exc:
            raise ItemError(str(exc)) from exc
        verses, label = sorted(r.routes), str(spec["verse"]).strip()
        if len(label) > 60:                # a long list is labelled by its first reference and its size
            label = f"{re.split(r'[;,]', label)[0].strip()} and {len(verses) - 1} more verses"
        out = {"source_terms": None, "target_cluster": None, "target_terms": None}
        if with_terms:     # a purpose's own verses, read for its source and target terms (#2236)
            try:
                src, tgt = r._expand_codes(spec["source"]), r._expand_codes(spec["target_terms"])
            except vs.ScopeError as exc:
                raise ItemError(str(exc)) from exc
            cl = spec["target_cluster"]
            members = {x[0] for x in conn.execute("SELECT strong FROM cluster_strong WHERE cluster_code=? AND deleted=0", (cl,))}
            outside = [t for t in tgt if t not in members]
            if not members or outside:
                raise ItemError(f"-TargetCluster {cl!r} is not a live cluster" if not members
                                else f"target term(s) {outside} are not in cluster {cl}")
            short = lambda xs: "+".join(xs[:3]) + ("+..." if len(xs) > 3 else "")  # noqa: E731
            label = f"{cl}: {short(src)} x {short(tgt)} ({len(verses)} verses)"
            out = {"source_terms": ",".join(src), "target_cluster": cl, "target_terms": ",".join(tgt)}
    else:
        if not (spec.get("source") and spec.get("target_cluster") and spec.get("target_terms")):
            raise ItemError("a cluster item needs -Source (the source analysis's strong), -TargetCluster and "
                            "-TargetTerms (the related term(s) in that cluster); or give -Verse")
        try:
            src = r._expand_codes(spec["source"])
            tgt = r._expand_codes(spec["target_terms"])
        except vs.ScopeError as exc:
            raise ItemError(str(exc)) from exc
        cl = spec["target_cluster"]
        members = {x[0] for x in conn.execute("SELECT strong FROM cluster_strong WHERE cluster_code=? AND deleted=0",
                                              (cl,))}
        if not members:
            raise ItemError(f"-TargetCluster {cl!r} is not a live cluster")
        outside = [t for t in tgt if t not in members]
        if outside:
            raise ItemError(f"target term(s) {outside} are not in cluster {cl}")
        verses = sorted({x[0] for x in conn.execute(
            "SELECT DISTINCT a.verse_id FROM verse_lexical a JOIN verse_lexical b ON b.verse_id=a.verse_id AND b.deleted=0 "
            "AND b.strong IN (SELECT value FROM json_each(?)) WHERE a.deleted=0 AND a.strong IN (SELECT value FROM json_each(?))",
            (json.dumps(tgt), json.dumps(src)))})
        label = f"{cl}: {'+'.join(src)} x {'+'.join(tgt)}"
        out = {"source_terms": ",".join(src), "target_cluster": cl, "target_terms": ",".join(tgt)}
    if not verses:
        raise ItemError(f"the target {label!r} holds no verse" + ("" if spec.get("verse") else
                        " (the source and target terms never stand in the same verse)"))
    if len(verses) > limit:
        raise ItemError(f"the target {label!r} holds {len(verses)} verses, over open_item.max_verses {limit}: "
                        f"split it into separate items, one purpose each")
    return {**out, "verses": verses, "label": label}


def _validate(cfg, spec: dict, r: vs.Resolver) -> tuple[str, int]:
    for f in TEXT_FIELDS:
        if len(spec.get(f) or "") < 15:
            raise ItemError(f"-{ {'read_for': 'ReadFor', 'why': 'Why', 'comes_back_when': 'ComesBackWhen'}[f] } is "
                            f"required and states it in words (an item without a clear purpose is refused)")
    origin = str(spec.get("origin") or "").lstrip("#")
    if not origin.isdigit() or not cfg.conn.execute("SELECT 1 FROM escalation WHERE id=? AND type IN ('task','issue')",
                                                    (int(origin),)).fetchone():
        raise ItemError(f"-Origin {spec.get('origin')!r} must be the task or issue of the analysis that raises the item")
    return _check_anchor(cfg, r, spec.get("anchor")), int(origin)


def _write_worded(w, conn, item_id: int, spec: dict, anchor: str, origin: int, tgt: dict) -> None:
    w.update("escalation_thread_item", {"id": item_id}, {
        "kind": "scope", "value": tgt["label"], "note": spec["read_for"], "origin_escalation_id": origin,
        "anchor": anchor, "source_terms": tgt["source_terms"], "target_cluster": tgt["target_cluster"],
        "target_terms": tgt["target_terms"], "read_for": spec["read_for"], "why": spec["why"],
        "comes_back_when": spec["comes_back_when"], "target_verses": len(tgt["verses"]), "worded_at": _now()})
    w.update("escalation_thread_item_verse", {"item_id": item_id, "deleted": 0}, {"deleted": 1})
    for vid in tgt["verses"]:
        w.insert("escalation_thread_item_verse", {"item_id": item_id, "verse_id": vid})


def _shown(tgt: dict) -> str:
    n = f"({len(tgt['verses'])} verses)"
    return tgt["label"] if tgt["label"].endswith(n) else f"{tgt['label']} {n}"


def _duplicate(conn, thread_id: int, label: str, read_for: str, skip: int | None = None):
    return conn.execute("SELECT item_no FROM escalation_thread_item WHERE escalation_id=? AND status='open' AND "
                        "kind='scope' AND value=? AND read_for=? AND id<>?",
                        (thread_id, label, read_for, skip or -1)).fetchone()


def add(cfg, db, w, spec: dict, who: str) -> str:
    conn = cfg.conn
    t = _thread(conn, spec.get("thread"))
    r = vs.Resolver(cfg)
    anchor, origin = _validate(cfg, spec, r)
    tgt = resolve_target(cfg, spec)
    if _duplicate(conn, t["id"], tgt["label"], spec["read_for"]):
        raise ItemError(f"{t['alias']} already has an open item on {tgt['label']!r} reading for the same thing")
    if conn.execute("SELECT 1 FROM escalation_thread_item WHERE escalation_id=? AND kind='scope' AND value=? COLLATE NOCASE",
                    (t["id"], tgt["label"])).fetchone():
        tgt["label"] = f"{tgt['label']} ({spec['read_for'][:40]})"     # same target, another purpose
    escalation.update(cfg, db, t["id"], originator=who, add_items=[("scope", tgt["label"], spec["read_for"])],
                      via=origin)
    it = conn.execute("SELECT id, item_no FROM escalation_thread_item WHERE escalation_id=? AND kind='scope' AND value=?",
                      (t["id"], tgt["label"])).fetchone()
    _write_worded(w, conn, it["id"], spec, anchor, origin, tgt)
    return f"{t['alias']}.{it['item_no']} added: {_shown(tgt)}"


def reword(cfg, db, w, spec: dict, who: str) -> str:
    conn = cfg.conn
    t, it = _item(conn, spec.get("item"))
    r = vs.Resolver(cfg)
    anchor, origin = _validate(cfg, spec, r)
    tgt = resolve_target(cfg, spec)
    if _duplicate(conn, t["id"], tgt["label"], spec["read_for"], skip=it["id"]):
        raise ItemError(f"{t['alias']} already has an open item on {tgt['label']!r} reading for the same thing; "
                        f"supersede this one by it instead")
    clash = conn.execute("SELECT item_no FROM escalation_thread_item WHERE escalation_id=? AND kind='scope' AND value=? "
                         "COLLATE NOCASE AND id<>?", (t["id"], tgt["label"], it["id"])).fetchone()
    if clash:
        tgt["label"] = f"{tgt['label']} ({spec['read_for'][:40]})"
    was = f"{it['kind']}:{it['value']}" + (f" :: {it['note']}" if it["note"] else "")
    if it["worded_at"]:
        was += f" | read for: {it['read_for']} | why: {it['why']} | comes back when: {it['comes_back_when']}"
    _write_worded(w, conn, it["id"], spec, anchor, origin, tgt)
    escalation.update(cfg, db, t["id"], originator=who, item_refs=[f"{t['alias']}.{it['item_no']}"],
                      response_kind="note", respond=f"reworded (#2236); was: {was}", via=origin)
    return f"{t['alias']}.{it['item_no']} reworded: {_shown(tgt)}"


def split(cfg, db, w, item_ref: str, parts: list[dict], who: str) -> str:
    conn = cfg.conn
    t, it = _item(conn, item_ref)
    if len(parts) < 2:
        raise ItemError("a split gives two or more items (-File with a list)")
    made = []
    for p in parts:
        p = {**p, "thread": p.get("thread") or t["alias"]}
        made.append(add(cfg, db, w, p, who).split(" ")[0])
    escalation.update(cfg, db, t["id"], originator=who, item_refs=[f"{t['alias']}.{it['item_no']}"],
                      response_kind="superseded", respond=f"split into {', '.join(made)} (#2236): one purpose per item")
    return f"{t['alias']}.{it['item_no']} split into {', '.join(made)}"


def due(cfg, home: str) -> list[dict]:
    """The open worded items that come back when `home` (a cluster) is worked."""
    return [dict(r) for r in cfg.conn.execute(
        "SELECT e.alias || '.' || i.item_no AS item, i.value, i.read_for, i.why, i.comes_back_when, i.target_verses "
        "FROM escalation_thread_item i JOIN escalation e ON e.id=i.escalation_id WHERE i.status='open' AND "
        "i.kind='scope' AND i.target_cluster=? ORDER BY i.escalation_id, i.item_no", (home,))]


def review(cfg) -> tuple[list[str], str]:
    """The stragglers report: open items not yet worded, worded items past open_item.review_age_days, open threads
    with no open item."""
    conn = cfg.conn
    age = int(cfg.required_setting("open_item.review_age_days"))
    cutoff = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=age)).strftime("%Y-%m-%dT%H:%M:%SZ")
    threads = conn.execute("SELECT id, alias, short_description, state FROM escalation WHERE type='thread' AND "
                           "state IN ('on-hold','in-progress') ORDER BY CAST(substr(alias, 4) AS INTEGER)").fetchall()
    L = ["# Open items -- review", "",
         f"> Generated by `Open-Item.ps1 -Action Review` (escalation #2236). An item is worded when it carries a target, "
         f"what to read for, why it is open and when it comes back; older than {age} days is a straggler to deal with.", "",
         "| thread | purpose | open | worded | not worded | worded, older than the review age |", "|---|---|---|---|---|---|"]
    tot = [0, 0, 0, 0]
    empty = []
    for t in threads:
        rows = conn.execute("SELECT kind, worded_at, opened_at FROM escalation_thread_item WHERE escalation_id=? AND "
                            "status='open'", (t["id"],)).fetchall()
        worded = sum(1 for x in rows if x["worded_at"])
        old = sum(1 for x in rows if x["worded_at"] and (x["worded_at"] < cutoff))
        if not rows:
            empty.append(t["alias"])
        tot = [tot[0] + len(rows), tot[1] + worded, tot[2] + len(rows) - worded, tot[3] + old]
        L.append(f"| {t['alias']} | {(t['short_description'] or '').replace('|', '/')} | {len(rows)} | {worded} | "
                 f"{len(rows) - worded} | {old} |")
    L.append(f"| **total** | | **{tot[0]}** | **{tot[1]}** | **{tot[2]}** | **{tot[3]}** |")
    if empty:
        L += ["", f"Open threads with no open item: {', '.join(empty)}"]
    return L, f"{tot[0]} open items: {tot[1]} worded, {tot[2]} not yet worded, {tot[3]} past {age} days"
