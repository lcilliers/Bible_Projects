"""threadaudit.py -- quality, validity and integrity of the open threads (#2173 P5): findings that
lead to disclosure, not counts.

Read-only. Every finding is named by its thread item (OT-nn.n) or thread (OT-nn) with its reason:

  T-a  handle resolves   cluster: in `cluster`; strong: a live `strong`; verse: resolves with the
                         narrative register's own parser; chapter: an active narrative_chapter;
                         escalation: an escalation that exists
  T-b  handle note       an open item with no note saying what to pick up (OT-05 ruling #2006)
  T-c  referred work     an open escalation: item whose escalation is closed
  T-d  should be cleared an open cluster:/strong: item on a strand already worked; worked =
                         every escalation listed for that cluster in cfg_setting
                         escalation.worked_strand_escalations is completed (from state, not memory)
  T-e  already told      an open verse: item whose verse a current narrative citation tells
  T-f  thread shape      an open thread with no open item; with no comes-back-when; a superseded
                         item or thread whose successor (OT-nn[.n] / #nnnn) does not exist
  T-g  register current  open-threads-register.md differs from what Export would write now
"""

from __future__ import annotations

import datetime
import pathlib
import re

from . import escalation as esc, reportkit
from .narrativeregister import VerseIndex, parse_refs

_SUCC_RE = re.compile(r"\bOT-(\d+)(?:\.(\d+))?\b|#(\d+)")


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _chapter_key(v: str) -> str:
    """'02' and '2' are the same chapter; '10.1' stays '10.1'."""
    head, _, rest = v.strip().partition(".")
    if head.isdigit():
        head = head.lstrip("0") or "0"
    return f"{head}.{rest}" if rest else head


def _worked_clusters(cfg, db) -> dict[str, list[int]]:
    """{cluster: [escalation ids]} for every strand whose listed escalations are all completed."""
    spec = cfg.required_setting("escalation.worked_strand_escalations")
    done = set(esc.state_group(db, "terminal"))
    worked = {}
    for cluster, ids in spec.items():
        states = [r["state"] for r in db.rows(
            f"SELECT state FROM escalation WHERE id IN ({','.join('?' * len(ids))})", ids)]
        if len(states) == len(ids) and all(s == "completed" and s in done for s in states):
            worked[cluster] = ids
    return worked


def audit(cfg, db) -> list[dict]:
    """[{check, ref, reason}] -- one per finding."""
    conn = db.conn
    vx = VerseIndex(cfg)
    clusters = {r[0] for r in conn.execute("SELECT cluster_code FROM cluster WHERE deleted=0")}
    strongs = {r[0] for r in conn.execute("SELECT strongNumber FROM strong WHERE deleted=0")}
    chapters = {_chapter_key(r[0]) for r in conn.execute(
        "SELECT chapter_no FROM narrative_chapter WHERE inactive=0")}
    esc_state = {r[0]: r[1] for r in conn.execute("SELECT id, state FROM escalation")}
    aliases = {r[0] for r in conn.execute("SELECT alias FROM escalation WHERE alias IS NOT NULL")}
    items_by_ref = {f"{r[0]}.{r[1]}" for r in conn.execute(
        "SELECT e.alias, i.item_no FROM escalation_thread_item i JOIN escalation e "
        "ON e.id=i.escalation_id")}
    told = {r[0] for r in conn.execute(
        "SELECT nc.verse_id FROM narrative_citation nc JOIN narrative_chapter ch ON "
        "ch.id=nc.chapter_id AND ch.inactive=0 WHERE nc.last_version IS NULL AND nc.verse_id IS "
        "NOT NULL")}
    strong_cluster: dict[str, set[str]] = {}
    for s, cl in conn.execute("SELECT strong, cluster_code FROM cluster_strong WHERE deleted=0"):
        strong_cluster.setdefault(s, set()).add(cl)
    worked = _worked_clusters(cfg, db)
    terminal = set(esc.state_group(db, "terminal"))
    live = set(esc.live_states(db))

    def succ_exists(text: str) -> bool | None:
        refs = list(_SUCC_RE.finditer(text or ""))
        if not refs:
            return None
        for m in refs:
            if m.group(3):
                if int(m.group(3)) not in esc_state:
                    return False
            elif m.group(2):
                if f"OT-{int(m.group(1)):02d}.{m.group(2)}" not in items_by_ref \
                        and f"OT-{m.group(1)}.{m.group(2)}" not in items_by_ref:
                    return False
            elif f"OT-{int(m.group(1)):02d}" not in aliases and f"OT-{m.group(1)}" not in aliases:
                return False
        return True

    F: list[dict] = []
    add = lambda check, ref, reason: F.append(dict(check=check, ref=ref, reason=reason))
    threads = conn.execute("SELECT * FROM escalation WHERE type='thread' "
                           "ORDER BY CAST(substr(alias, 4) AS INTEGER)").fetchall()
    for t in threads:
        items = conn.execute("SELECT * FROM escalation_thread_item WHERE escalation_id=? "
                             "ORDER BY item_no", (t["id"],)).fetchall()
        open_items = [i for i in items if i["status"] == "open"]
        if t["state"] in live:
            if not open_items:
                add("T-f", t["alias"], f"open thread ({t['state']}) with no open item")
            if not (t["comes_back_when"] or "").strip():
                add("T-f", t["alias"], "open thread with no 'comes back when'")
        if t["state"] == "supersede":
            text = " ".join(filter(None, (t["resolution"], t["comment"])))
            if succ_exists(text) is False:
                add("T-f", t["alias"], "superseded thread names a successor that does not exist")
        for i in items:
            ref = f"{t['alias']}.{i['item_no']}"
            if i["status"] == "superseded":
                resp = conn.execute("SELECT text FROM escalation_thread_item_response WHERE "
                                    "item_id=? AND kind='superseded' ORDER BY id DESC LIMIT 1",
                                    (i["id"],)).fetchone()
                if resp and succ_exists(resp[0]) is False:
                    add("T-f", ref, "superseded item names a successor that does not exist")
            if i["status"] != "open":
                continue
            kind, val = i["kind"], (i["value"] or "").strip()
            if not (i["note"] or "").strip():
                add("T-b", ref, f"{kind}:{val} has no note saying what to pick up")
            if kind == "cluster":
                if val not in clusters:
                    add("T-a", ref, f"cluster {val!r} is not a live cluster")
                elif val in worked:
                    add("T-d", ref, f"cluster {val} is a worked strand "
                                    f"(#{', #'.join(map(str, worked[val]))} completed); the item is "
                                    f"still open")
            elif kind == "strong":
                # a base code (H6942) stands for its lettered variants (H6942A, H6942H)
                codes = [val] if val in strongs else [
                    s for s in strongs if s.startswith(val) and s[len(val):].isalpha()]
                if not codes:
                    add("T-a", ref, f"strong {val!r} is not a live strong (nor the base of one)")
                else:
                    hit = sorted(set().union(*(strong_cluster.get(x, set()) for x in codes))
                                 & set(worked))
                    if hit:
                        add("T-d", ref, f"strong {val} belongs to worked strand(s) "
                                        f"{', '.join(hit)}; the item is still open")
            elif kind == "verse":
                refs = [r for r in parse_refs(val, vx) if r.verse_id]
                if not refs:
                    add("T-a", ref, f"verse {val!r} does not resolve to a verse")
                elif any(r.verse_id in told for r in refs):
                    add("T-e", ref, f"verse {val} is told in the narrative now -- done and not "
                                    f"closed, or the telling does not cover what the item asks")
            elif kind == "chapter":
                if _chapter_key(val) not in chapters:
                    add("T-a", ref, f"chapter {val!r} is not an active narrative chapter")
            elif kind == "escalation":
                m = re.search(r"\d+", val)
                if not m or int(m.group()) not in esc_state:
                    add("T-a", ref, f"escalation {val!r} does not exist")
                elif esc_state[int(m.group())] in terminal:
                    add("T-c", ref, f"escalation #{m.group()} is {esc_state[int(m.group())]}; the "
                                    f"item is still open (close it or carry it on)")
    # T-g
    path = pathlib.Path(cfg.required_setting("escalation.thread_register_path"))
    L, _ = esc.render_thread_register(cfg, db)
    want = "\n".join(L) + "\n"
    have = path.read_text(encoding="utf-8") if path.is_file() else None
    if have != want:
        add("T-g", path.as_posix(), "the register file differs from the escalation table "
                                    "(run Escalation.ps1 -Action Export -Type thread)"
            if have is not None else "the register file does not exist")
    return F


def write_report(cfg, db, path: pathlib.Path) -> tuple[pathlib.Path, list[dict]]:
    F = audit(cfg, db)
    worked = _worked_clusters(cfg, db)
    by: dict[str, list[dict]] = {}
    for f in F:
        by.setdefault(f["check"], []).append(f)
    intro = [f"> Generated {_now()} by `Escalation.ps1 -Action ThreadAudit` (#2173 P5). Read-only. "
             f"Each finding is named by its thread item with its reason; a check with no "
             f"findings is not listed.", "",
             f"- worked strands (all listed escalations completed, "
             f"`escalation.worked_strand_escalations`): "
             + (", ".join(f"{k} (#{', #'.join(map(str, v))})" for k, v in sorted(worked.items()))
                or "none"),
             f"- findings: **{len(F)}** "
             + ("(" + ", ".join(f"{k} {len(v)}" for k, v in sorted(by.items())) + ")" if F else ""),
             ""]
    labels = {"T-a": "handle does not resolve", "T-b": "handle has no note",
              "T-c": "referred work closed, item open", "T-d": "should have been cleared",
              "T-e": "verse already told", "T-f": "thread shape", "T-g": "register file current"}
    body: list[str] = []
    for k in sorted(by):
        body += [f"### {k} {labels[k]} ({len(by[k])})", ""]
        body += [f"- **{f['ref']}**: {f['reason']}" for f in by[k]]
        body.append("")
    if not F:
        body = ["_no findings_"]
    L = reportkit.render_scaffold(db.conn, "escalation.thread_audit", {"findings": body},
                                  intro=intro)
    out = reportkit.write_report(db.conn, "escalation.thread_audit", path, L)
    return out, F
