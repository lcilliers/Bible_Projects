"""debateaudit.py — the shared per-row CRUD audit trail for every debate writer (`hib.set`,
`passage.build`, `phenomenon.set`, `operation.set`, `closing.set`): every insert, update and delete
is traceable to its run.

Writes `debate_change_detail` (`run_id, writer, table_name, op, where_json, set_json, before_json,
applied_at`), the same shape as `cfg_change_detail` but for data writes. One shared module, so the
audit shape stays identical across all five writers.
"""

from __future__ import annotations

import datetime
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:      # avoid a lib -> handlers runtime dependency; no other lib module has one
    from ..handlers.base import Ctx


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def log_change(ctx: Ctx, writer: str, table_name: str, op: str, where: dict,
              set_: dict | None = None, before: dict | None = None) -> None:
    """One row per data row `writer` inserts, updates, or soft-deletes. Caller is responsible for
    its own `_may(ctx, writer, "debate_change_detail")` write-grant check, up front alongside its
    other tables — not re-checked on every call here (matches every other writer's own convention
    of checking every grant it needs before touching any row)."""
    ctx.db.write("debate_change_detail", {
        "run_id": ctx.run_id, "writer": writer, "table_name": table_name, "op": op,
        "where_json": json.dumps(where), "set_json": json.dumps(set_) if set_ is not None else None,
        "before_json": json.dumps(before) if before is not None else None, "applied_at": _now()})
