"""debateaudit.py — the shared per-row CRUD audit trail for every debate writer (`hib.set`,
`passage.build`, `phenomenon.set`, `operation.set`, `closing.set`). Researcher direction,
2026-08-08: "each entry (insert, update, delete) must have entries in the table to be able to trace
the changes to the run... full CRUD is required for all table update controls."

Writes to `debate_change_detail` (`run_id, writer, table_name, op, where_json, set_json,
before_json, applied_at`) — mirrors `cfg_change_detail`'s own shape exactly (the existing per-row
audit trail for `configmaint.propose` writes), kept as a separate table since this is data-write
audit, not config-write audit. Originally built as `hib_change_detail` (BUILD.md §81, `hib.set`
only), renamed once its scope broadened to every debate writer
(`migration/rename_hib_change_detail_to_debate_change_detail_20260808.py`).

Centralised here rather than duplicated per-handler (unlike this app's own small `_may`/`_now`
helpers, which each handler file defines locally) because the audit shape must stay byte-identical
across all 5 writers — a meatier, more error-prone thing to keep in sync by hand five times than a
three-line helper.
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
