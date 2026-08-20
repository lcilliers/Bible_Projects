"""escalation.py — util.escalation. The authoritative record of open items in the project: errors,
issues, and building tasks. NOT a run-logging mechanism — a standard operational routine (run
through an already-approved app PS script) is logged by the engine (`run.state`/`resume_point`/
`outcome`) and escalates only on genuine error. A DEVELOPMENT/DESIGN control — anything that
changes the app's own behaviour, above all a `configmaint.propose` config write — keeps a real,
gated approval here (researcher, 2026-08-19/20; full record `iba/docs/escalation-redesign-plan-v3-
20260819.md` + `BUILD.md` §152/§153).

**Redesign v2, 2026-08-20** (supersedes the 2026-08-16 reset). Root cause of the whole rebuild:
escalation #715's updates were silently overwritten with no trace — `comment`/`next_action`/etc.
were single mutable fields, never a history. Fixed at the root: `escalation` is now CURRENT STATE
ONLY, `escalation_history` is a real APPEND-ONLY table, one FULL SNAPSHOT row per update, every
column's value at that version, never updated or deleted once written.

**Two shapes now share this mechanism, each with its own vocabulary — deliberately NOT unified**,
because they answer genuinely different questions:

  - **dispatcher-tied** (`run_id` set) — a real pipeline pause, e.g. `configmaint.propose`/
    `validate`, `candidate.validate`, `passage.build`/`validate`, `lexicon.validate`. Vocabulary
    UNCHANGED from the pre-redesign shape (`approve | reject | revise | hold | noted`) so the 9
    existing handler call sites (`answered_for_run()["next_action"]`/`["comment"]`) needed zero
    changes — verified by reading every one of them, not assumed compatible. `raise_()` /
    `pending_for_run()` / `answered_for_run()` / `answer_for_run()` are this shape's functions.

  - **manual** (`run_id` is `MANUAL-...`, no real `run` row) — the researcher/Claude backlog-of-
    work-and-issues workflow the three plan-review rounds designed. Vocabulary: `ready_for_approval
    | approved | reject | revise | noted | review` — a two-stage handshake for approval
    (`ready_for_approval` -> `approved` -> system-validated `completed`, producing two real history
    rows), auto-state rules evaluated in priority order (plan v3 §3). `raise_new()` / `update()`
    are this shape's functions.

Both write through the SAME full-snapshot mechanism (`_snapshot()`), so both get real history for
free — including dispatcher-tied items, which never had it before either.

CLI (module path: iba.app.lib.escalation, invoked as `python -m iba.app.lib.escalation`):
    python -m iba.app.lib.escalation list
    python -m iba.app.lib.escalation answer-run <run_id> <approve|reject|revise|hold|noted>
        [--by=Claude|Researcher] [--resolution=...] [comment words...]
    python -m iba.app.lib.escalation raise <question...>
        [--source=claude|researcher] [--assigned-to=Claude|Researcher] [--type=task|...]
        [--related-activity=...]
    python -m iba.app.lib.escalation update <id> [--next-action=...] [--assigned-to=...]
        [--state=on-hold|in-progress|closed|withdraw|supersede] [--resolution=...]
        [--related-activity=...] [--tried=...] [comment/context words...]
"""

from __future__ import annotations

import datetime
import json
import pathlib
import sys

from . import reportkit
from .cfg import Cfg
from .db import Db

_OPEN_STATES = ("raised", "re-assigned", "on-hold", "in-progress")

# every business column on `escalation` / `escalation_history` (id/version/escalation_id excluded
# -- those are structural, not part of a snapshot's business content)
_COLS = ("run_id", "source", "at_step", "type", "short_description", "context", "comment", "tried",
        "state", "next_action", "next_action_assigned_to", "originator", "resolution",
        "related_activity", "raised_at", "answered_at")


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _grant(cfg: Cfg, table: str):
    if table not in cfg.may_write("escalation"):
        raise PermissionError(f"write-grant violation: 'escalation' may not write {table!r}")


def word_source(word: str) -> str:
    return f"new-word: {word}"


def _check_state(db: Db, state: str) -> str:
    valid = db.cfg.enum("escalation_state")
    if state not in valid:
        raise ValueError(f"{state!r} is not a member of cfg_enum 'escalation_state' ({valid!r})")
    return state


def _check_type(db: Db, etype: str) -> str:
    valid = db.cfg.enum("escalation_type")
    if etype not in valid:
        raise ValueError(f"{etype!r} is not a member of cfg_enum 'escalation_type' ({valid!r})")
    return etype


def _check_next_action(db: Db, next_action: str | None) -> str | None:
    if next_action is None:
        return None
    valid = db.cfg.enum("escalation_next_action")
    if next_action not in valid:
        raise ValueError(f"{next_action!r} is not a member of cfg_enum 'escalation_next_action' "
                         f"({valid!r})")
    return next_action


def _check_assignee(db: Db, who: str | None, required: bool = True) -> str | None:
    if who is None:
        if required:
            raise ValueError("originator is required — must be 'Claude' or 'Researcher'")
        return None
    normalised = who.strip().capitalize()
    valid = db.cfg.enum("escalation_assignee")
    if normalised not in valid:
        raise ValueError(f"{who!r} is not a member of cfg_enum 'escalation_assignee' ({valid!r})")
    return normalised


# ── the shared core: every write, either shape, goes through this ───────────────────────────────
def _current(db: Db, escalation_id: int) -> dict:
    rows = db.rows("SELECT * FROM escalation WHERE id=?", (escalation_id,))
    if not rows:
        raise ValueError(f"no escalation #{escalation_id}")
    return dict(rows[0])


def _grant_both(cfg: Cfg) -> None:
    """Every write touches BOTH `escalation` and `escalation_history` -- check both grants
    explicitly, every time, rather than relying on one check to stand in for the other (escalation
    #745, 2026-08-20: `escalation_history` had no grant row at all and nothing ever caught it,
    because only `escalation`'s grant was ever checked here)."""
    _grant(cfg, "escalation")
    _grant(cfg, "escalation_history")


def _create(cfg: Cfg, db: Db, **fields) -> int:
    """New item, version 1. `fields` must already have every _COLS value resolved (raised_at set,
    defaults applied by the caller) -- this just writes it, snapshot included."""
    _grant_both(cfg)
    row = {"version": 1, **{k: fields.get(k) for k in _COLS}}
    new_id = db.write("escalation", row)
    db.write("escalation_history", {"escalation_id": new_id, "version": 1,
                                    **{k: fields.get(k) for k in _COLS}})
    return new_id


def _snapshot(cfg: Cfg, db: Db, escalation_id: int, changes: dict, originator: str) -> dict:
    """Merge `changes` onto the current row, write the new full-snapshot history row, update
    `escalation` to match -- both in the caller's open transaction (single commit). Returns the
    merged row."""
    _grant_both(cfg)
    cur = _current(db, escalation_id)
    merged = {**cur, **changes}
    merged["version"] = cur["version"] + 1
    merged["originator"] = originator
    merged["answered_at"] = _now()
    db.write("escalation_history", {"escalation_id": escalation_id, "version": merged["version"],
                                    **{k: merged[k] for k in _COLS}})
    db.update("escalation", {"id": escalation_id}, version=merged["version"],
              **{k: merged[k] for k in _COLS})
    return merged


def _append(current: str | None, addition: str | None) -> str | None:
    """Cumulative field convention (plan v3 §2): the caller supplies only the increment; storage
    holds the running full text."""
    if not addition:
        return current
    return f"{current}\n{addition}" if current else addition


# ── DISPATCHER-TIED shape (run_id set) -- vocabulary/semantics UNCHANGED from pre-redesign ──────
def _terminal_state_for(next_action: str) -> str:
    """Dispatcher-tied decision -> state. Unchanged from the pre-redesign function of the same
    name (run-scoped branch only -- the is_manual branch doesn't apply here, manual items use
    `update()`'s auto-state rules instead, see plan v3 §3)."""
    if next_action == "hold":
        return "on-hold"
    if next_action == "noted":
        return "closed"
    return "completed"


def raise_(db: Db, run_id: str, source: str, at_step: str, question: str,
          preset: dict, tried: str, etype: str = "task", assigned_to: str = "Researcher") -> int:
    """Record a pause -- called by run.py at a real dispatcher pause point. `source` is the
    caller's own choice (word_source(word) for a word-scoped step, _source_for_step(step_id)
    otherwise) -- this function no longer derives it, since run.py's 3 call sites need both
    shapes and only one of them is word-scoped."""
    now = _now()
    fields = {
        "run_id": run_id, "source": source, "at_step": at_step,
        "type": _check_type(db, etype), "short_description": question, "context": json.dumps(preset),
        "tried": tried, "state": _check_state(db, "raised"), "next_action": None,
        "answered_at": now, "raised_at": now,     # answered_at = this row's own write time, not
        "resolution": None, "related_activity": at_step,          # a decision date -- never null
        "next_action_assigned_to": _check_assignee(db, assigned_to), "originator": None}
    return _create(db.cfg, db, **fields)


def pending_for_run(db: Db, run_id: str):
    return db.rows(
        "SELECT * FROM escalation WHERE run_id=? AND state='raised' "
        "ORDER BY id DESC LIMIT 1", (run_id,))


def answered_for_run(db: Db, run_id: str, at_step: str):
    """The latest COMPLETED escalation for a run at a step, or None -- unchanged signature/
    semantics from pre-redesign. `hold`/`noted` deliberately never resolve to `state='completed'`,
    so they never match here: the underlying run correctly stays paused (see _terminal_state_for)."""
    rows = db.rows(
        "SELECT * FROM escalation WHERE run_id=? AND at_step=? AND state='completed' "
        "ORDER BY id DESC LIMIT 1", (run_id, at_step))
    return rows[0] if rows else None


def open_duplicate(db: Db, at_step: str, stable_key: str):
    rows = db.rows(
        "SELECT * FROM escalation WHERE at_step=? AND state='raised' AND short_description LIKE ? "
        "ORDER BY id DESC LIMIT 1", (at_step, f"%{stable_key}%"))
    return rows[0] if rows else None


def _resolve_id(db: Db, ident: str) -> int:
    """Accept either the bare `escalation.id` or (legacy convenience) a digit string."""
    return int(ident)


def answer_for_run(cfg: Cfg, db: Db, run_id: str, decision: str, comment: str | None = None,
                   answered_by: str = "Researcher", resolution: str | None = None) -> str:
    """Record the decision on a run-scoped (dispatcher-tied) escalation. decision: approve | reject
    | revise | hold | noted -- UNCHANGED vocabulary/state-mapping from pre-redesign."""
    decision = decision.lower()
    valid = ("approve", "reject", "revise", "hold", "noted")
    if decision not in valid:
        return f"invalid decision {decision!r} — must be one of {valid!r}"
    rows = pending_for_run(db, run_id)
    if not rows:
        return f"no pending escalation for run {run_id!r}"
    esc_row = rows[0]
    who = _check_assignee(db, answered_by)
    new_state = _terminal_state_for(decision)
    merged = _snapshot(cfg, db, esc_row["id"], {
        "state": _check_state(db, new_state), "next_action": decision,
        "comment": _append(esc_row["comment"], comment), "resolution": resolution}, who)
    return (f"escalation {esc_row['id']} (run {run_id!r}, step {esc_row['at_step']!r}) answered "
           f"{decision!r} -> {new_state}" + (f" — {comment!r}" if comment else ""))


# ── MANUAL shape -- the new two-transaction model (plan v3) ─────────────────────────────────────
def raise_new(cfg: Cfg, db: Db, short_description: str, source: str, etype: str = "task",
             comment: str | None = None, context: str | None = None,
             related_activity: str | None = None, assigned_to: str = "Claude",
             originator: str = "Researcher") -> int:
    """Raise -- a new MANUAL item. Required: short_description, source, type, comment (plan v3
    §6). Defaults: next_action_assigned_to=Claude, next_action=review, state=raised."""
    if not comment:
        raise ValueError("comment is required at Raise -- minimum: what the item is about")
    run_id = f"MANUAL-{datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d_%H%M%S_%f')}"
    now = _now()
    fields = {
        "run_id": run_id, "source": source, "at_step": "manual", "type": _check_type(db, etype),
        "short_description": short_description, "context": context, "comment": comment,
        "tried": None, "state": _check_state(db, "raised"), "next_action": "review",
        "answered_at": now, "raised_at": now, "resolution": None,
        "related_activity": related_activity,
        "next_action_assigned_to": _check_assignee(db, assigned_to),
        "originator": _check_assignee(db, originator)}
    return _create(cfg, db, **fields)


def _derive_state(cur: dict, next_action: str | None, explicit_state: str | None,
                  assignee_changed: bool) -> str:
    """Auto-state rules, priority order (plan v3 §3) -- first match wins."""
    if next_action == "approved" and (cur.get("resolution") or explicit_state):
        return "completed"
    if next_action == "reject":
        if explicit_state not in ("withdraw", "supersede"):
            raise ValueError("next_action='reject' requires state='withdraw' or 'supersede', "
                             "chosen explicitly by the caller (plan v3 §3)")
        return explicit_state
    if next_action == "revise":
        return "in-progress"
    if next_action == "noted":
        return "closed"
    if assignee_changed:
        return "re-assigned"
    return explicit_state or cur["state"]


def update(cfg: Cfg, db: Db, escalation_id: int, *, next_action: str | None = None,
          next_action_assigned_to: str | None = None, comment: str | None = None,
          context: str | None = None, tried: str | None = None, resolution: str | None = None,
          related_activity: str | None = None, state: str | None = None,
          originator: str = "Researcher") -> str:
    """Update -- every subsequent change to a MANUAL item, on any open state (plan v3 §6). Only
    fields given a value change; everything else carries forward from the current row (§2)."""
    cur = _current(db, escalation_id)
    if not cur["run_id"].startswith("MANUAL-"):
        return (f"escalation #{escalation_id} is dispatcher-tied (run_id {cur['run_id']!r}), not "
               f"manual -- answer it via AnswerRun, not Update")
    if cur["state"] not in _OPEN_STATES:
        return f"escalation #{escalation_id} is not open (state={cur['state']!r})"

    who = _check_assignee(db, originator)
    checked_action = _check_next_action(db, next_action)
    new_resolution = resolution if resolution is not None else cur["resolution"]
    if checked_action == "approved" and not new_resolution:
        return "next_action='approved' requires resolution to be filled in (plan v3 §3)"
    assignee_changed = bool(next_action_assigned_to) and next_action_assigned_to != cur["next_action_assigned_to"]
    new_state = _derive_state(cur, checked_action, state, assignee_changed)

    merged = _snapshot(cfg, db, escalation_id, {
        "next_action": checked_action if checked_action is not None else cur["next_action"],
        "next_action_assigned_to": _check_assignee(db, next_action_assigned_to, required=False) or cur["next_action_assigned_to"],
        "comment": _append(cur["comment"], comment),
        "context": _append(cur["context"], context),
        "tried": tried if tried is not None else cur["tried"],
        "resolution": new_resolution,
        "related_activity": related_activity if related_activity is not None else cur["related_activity"],
        "state": _check_state(db, new_state)}, who)
    return f"escalation #{escalation_id} v{merged['version']} -> state={new_state!r}"


def _context_gist(raw: str | None) -> str:
    if not raw:
        return ""
    return str(raw).replace("\n", " ")[:80]


def write_list_report(cfg: Cfg, db: Db, path: pathlib.Path) -> tuple[pathlib.Path, list]:
    """Open items, grouped by related_activity, WITH full history inline underneath each one
    (plan v3 §5a -- the old report only ever showed current state)."""
    ph = ",".join("?" * len(_OPEN_STATES))
    rows = db.rows(f"SELECT * FROM escalation WHERE state IN ({ph}) "
                   f"ORDER BY related_activity, id", _OPEN_STATES)
    n_on_hold = sum(1 for r in rows if r["state"] == "on-hold")
    n_in_progress = sum(1 for r in rows if r["state"] == "in-progress")
    n_active = len(rows) - n_on_hold - n_in_progress
    objectives = cfg.setting("escalation.control_objectives", "")
    process = cfg.setting("escalation.control_process", "")
    L = ["# Open escalations", "",
        f"> {objectives}. {process}.".strip(), "",
        f"> Generated by `Escalation.ps1 -Action List`. {len(rows)} open escalation(s) "
        f"({n_active} active, {n_in_progress} in-progress, {n_on_hold} on-hold), grouped by "
        f"`related_activity`, full history inline.", ""]
    if not rows:
        L.append("_no open escalations_")
    for r in rows:
        hist = db.rows("SELECT * FROM escalation_history WHERE escalation_id=? ORDER BY version",
                       (r["id"],))
        L.append(f"## #{r['id']} v{r['version']} — {r['state']} — {r['short_description']}")
        L.append(f"type={r['type']} assigned_to={r['next_action_assigned_to']} "
                 f"related_activity={r['related_activity'] or ''}")
        L.append("")
        L.append("| v | state | next_action | originator | comment | at |")
        L.append("|---|---|---|---|---|---|")
        for h in hist:
            L.append(f"| {h['version']} | {h['state']} | {h['next_action'] or ''} | "
                     f"{h['originator'] or ''} | {_context_gist(h['comment'])} | {h['answered_at']} |")
        L.append("")

    resolved = db.rows(
        "SELECT id, state, related_activity, resolution, answered_at FROM escalation "
        "WHERE state IN ('completed','closed','withdraw','supersede') AND resolution IS NOT NULL "
        "ORDER BY answered_at DESC LIMIT 15")
    L += ["## Recently resolved (last 15)", ""]
    if not resolved:
        L.append("_none yet_")
    else:
        L += ["| # | state | related activity | resolution | answered |",
             "|---|---|---|---|---|"]
        for r in resolved:
            res = str(r["resolution"]).replace("|", "\\|").replace("\n", " ")
            if len(res) > 200:
                res = res[:200] + "… (full text in escalation.resolution, id " + str(r["id"]) + ")"
            L.append(f"| {r['id']} | {r['state']} | {r['related_activity']} | {res} | "
                     f"{r['answered_at']} |")

    reportkit.archive_before_write(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(L).rstrip() + "\n"
    path.write_text(text, encoding="utf-8")
    return path, rows


def write_history_report(cfg: Cfg, db: Db, escalation_id: int, path: pathlib.Path) -> pathlib.Path:
    """Deep-history report for one item (plan v3 §5b) -- its full history, plus the same for every
    item its related_activity text names or that names it back."""
    seen: set[int] = set()
    queue = [escalation_id]
    L = ["# Escalation deep history", ""]
    while queue:
        eid = queue.pop(0)
        if eid in seen:
            continue
        seen.add(eid)
        rows = db.rows("SELECT * FROM escalation WHERE id=?", (eid,))
        if not rows:
            continue
        r = rows[0]
        hist = db.rows("SELECT * FROM escalation_history WHERE escalation_id=? ORDER BY version",
                       (eid,))
        L.append(f"## #{eid} — {r['short_description']}")
        L.append(f"related_activity: {r['related_activity'] or ''}")
        L.append("")
        for h in hist:
            L.append(f"**v{h['version']}** ({h['answered_at']}, {h['originator'] or '?'}) "
                     f"state={h['state']} next_action={h['next_action'] or ''}")
            if h["comment"]:
                L.append(f"> {h['comment']}")
            L.append("")
        if r["related_activity"]:
            others = db.rows(
                "SELECT id FROM escalation WHERE related_activity LIKE ? AND id != ?",
                (f"%#{eid}%", eid))
            queue.extend(o["id"] for o in others)
            import re
            for m in re.findall(r"#(\d+)", r["related_activity"] or ""):
                queue.append(int(m))
    reportkit.archive_before_write(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(L).rstrip() + "\n", encoding="utf-8")
    return path


def _extract_flag(args: list[str], name: str) -> tuple[list[str], str | None]:
    prefix = f"--{name}="
    remaining, value = [], None
    for a in args:
        if a.startswith(prefix):
            value = a[len(prefix):]
        else:
            remaining.append(a)
    return remaining, value


def main() -> int:
    cfg = Cfg()
    db = Db(cfg)
    argv = sys.argv[1:]
    if len(argv) >= 1 and argv[0] == "list":
        path = pathlib.Path(cfg.setting("escalation.list_report_path",
                                        "iba/app/reports/escalation-list.md"))
        out, rows = write_list_report(cfg, db, path)
        print(f"  {len(rows)} open escalation(s) -> {out}")
    elif len(argv) >= 3 and argv[0] == "answer-run":
        rest, by = _extract_flag(argv[3:], "by")
        rest, resolution = _extract_flag(rest, "resolution")
        comment = " ".join(rest) or None
        print("  " + answer_for_run(cfg, db, argv[1], argv[2], comment,
                                    answered_by=by or "Researcher", resolution=resolution))
    elif len(argv) >= 2 and argv[0] == "raise":
        rest, source = _extract_flag(argv[1:], "source")
        rest, assigned_to = _extract_flag(rest, "assigned-to")
        rest, etype = _extract_flag(rest, "type")
        rest, related_activity = _extract_flag(rest, "related-activity")
        rest, originator = _extract_flag(rest, "originator")
        rest, comment = _extract_flag(rest, "comment")
        rest, context = _extract_flag(rest, "context")
        question = " ".join(rest)
        new_id = raise_new(cfg, db, question, source or "claude", etype=etype or "task",
                           comment=comment or question, context=context,
                           assigned_to=assigned_to or "Researcher",
                           related_activity=related_activity, originator=originator or "Researcher")
        print(f"  raised — #{new_id}. Update with: python -m iba.app.lib.escalation update {new_id} ...")
    elif len(argv) >= 2 and argv[0] == "update":
        rest, next_action = _extract_flag(argv[2:], "next-action")
        rest, assigned_to = _extract_flag(rest, "assigned-to")
        rest, state = _extract_flag(rest, "state")
        rest, resolution = _extract_flag(rest, "resolution")
        rest, related_activity = _extract_flag(rest, "related-activity")
        rest, tried = _extract_flag(rest, "tried")
        rest, originator = _extract_flag(rest, "originator")
        rest, context = _extract_flag(rest, "context")
        comment = " ".join(rest) or None
        print("  " + update(cfg, db, int(argv[1]), next_action=next_action,
                            next_action_assigned_to=assigned_to, comment=comment, context=context,
                            tried=tried, resolution=resolution, related_activity=related_activity,
                            state=state, originator=originator or "Researcher"))
    elif len(argv) >= 2 and argv[0] == "history":
        path = pathlib.Path(cfg.setting("escalation.history_report_dir",
                                        "iba/app/reports")) / f"escalation-{argv[1]}-history.md"
        out = write_history_report(cfg, db, int(argv[1]), path)
        print(f"  -> {out}")
    else:
        print("usage: python -m iba.app.lib.escalation list"
             " | history <id>"
             " | answer-run <run_id> <approve|reject|revise|hold|noted> [--by=...] "
             "[--resolution=...] [comment...]"
             " | raise <short_description...> --comment=... [--source=...] [--assigned-to=...] "
             "[--type=...] [--related-activity=...] [--context=...]"
             " | update <id> [--next-action=...] [--assigned-to=...] [--state=...] "
             "[--resolution=...] [--related-activity=...] [--tried=...] [--context=...] [comment...]")
    db.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
