"""conceptedit handlers -- work package `concept-edit` (#2355), one step per Concept-Edit.ps1 action.

List reads the concept grouping; Describe, AddDomain and SetDeleted change it (lib/conceptedit.py). Describe takes
its parameters or -File (a JSON list of {level, id, description}); each write action runs as one unit: any refusal
writes nothing and is the routed condition 'refused'."""
from __future__ import annotations

import json
import pathlib

from ..lib import conceptedit as ce
from ..lib import narrativeregister as nr
from .base import Ctx, Outcome, fail, ok


def _int(params: dict, name: str, required: bool = True) -> int | None:
    value = params.get(name)
    if value in (None, ""):
        if required:
            raise ce.EditError(f"-{name} is required")
        return None
    try:
        return int(value)
    except ValueError:
        raise ce.EditError(f"-{name} is a whole number, not {value!r}") from None


def _who(ctx: Ctx) -> str:
    who = ctx.params.get("By") or "Claude"
    if who not in ("Claude", "Researcher"):
        raise ce.EditError("-By is Claude or Researcher")
    return who


def _unit(ctx: Ctx, fn) -> Outcome:
    conn = ctx.cfg.conn
    conn.execute("SAVEPOINT concept_edit")
    try:
        lines = fn(nr.Writer(conn, ctx.step_id, _who(ctx)), _who(ctx))
    except (ce.EditError, PermissionError, ValueError) as exc:
        conn.execute("ROLLBACK TO concept_edit")
        conn.execute("RELEASE concept_edit")
        return fail("refused", str(exc))
    conn.execute("RELEASE concept_edit")
    conn.commit()
    return ok("\n  ".join(lines), changes=len(lines))


def list_(ctx: Ctx) -> Outcome:
    try:
        lines = ce.list_rows(ctx.cfg.conn, ctx.params.get("Level") or None, _int(ctx.params, "DomainId", False),
                             ctx.params.get("IncludeDeleted") == "1")
    except ce.EditError as exc:
        return fail("refused", str(exc))
    return ok("\n  ".join(lines) if lines else "no rows", rows=len(lines))


def _describe_specs(ctx: Ctx) -> list[dict]:
    f = ctx.params.get("File")
    if not f:
        return [{"level": ctx.params.get("Level"), "id": _int(ctx.params, "Id"),
                 "description": ctx.params.get("Description")}]
    p = pathlib.Path(f)
    if not p.is_file():
        raise ce.EditError(f"-File not found: {p.as_posix()}")
    data = json.loads(p.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not all(isinstance(x, dict) for x in data):
        raise ce.EditError("-File holds a JSON list of {level, id, description}")
    return data


def describe(ctx: Ctx) -> Outcome:
    def run(w, who):
        try:
            specs = _describe_specs(ctx)
        except json.JSONDecodeError as exc:
            raise ce.EditError(f"-File is not valid JSON: {exc}") from None
        return [ce.describe(w, s.get("level"), int(s.get("id") or 0), s.get("description"), ctx.run_id)
                for s in specs]
    return _unit(ctx, run)


def add_domain(ctx: Ctx) -> Outcome:
    return _unit(ctx, lambda w, who: [ce.add_domain(w, ctx.params.get("Name"), _int(ctx.params, "Ordinal", False),
                                                    ctx.params.get("Description"), who, ctx.run_id)])


def set_deleted(ctx: Ctx) -> Outcome:
    return _unit(ctx, lambda w, who: [ce.set_deleted(w, _int(ctx.params, "Id"), _int(ctx.params, "Deleted"),
                                                     ctx.run_id)])
