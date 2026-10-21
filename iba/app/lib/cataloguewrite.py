"""cataloguewrite.py — validated partial UPDATE of `wa_obs_question_catalogue` (bible_research.db) by
`obs_id` (#1007): any column except `obs_id` can be set; columns not named are untouched. A plain
`UPDATE` with no history table and no approval cycle (configmaint.propose governs `cfg_*` rows only;
this is ordinary content).

Auto-filled unless named in `-Set`:
- `last_modified` -- `datetime.now(UTC)`, ISO-8601.
- `catalogue_version` -- `f"v2-{today}"`, the most common live convention (`v2-YYYY-MM-DD`); the
  column has several conventions, so name it in `-Set` to override.
"""

from __future__ import annotations

import datetime
import sqlite3
import time

_TABLE = "wa_obs_question_catalogue"
_KEY = "obs_id"
_LOCK_RETRIES = 3
_LOCK_RETRY_DELAY = 0.3


def _now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _today() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")


def _open_db(cfg) -> sqlite3.Connection:
    conn = sqlite3.connect(cfg.database_path("bible_research"))
    conn.row_factory = sqlite3.Row
    return conn


def run_update(cfg, obs_id: int, set_: dict) -> dict:
    """Update one `wa_obs_question_catalogue` row. `set_` is a dict of {column: new_value};
    `obs_id` (the key) must not appear in it. Any column not named is left untouched. Raises
    ValueError on a bad obs_id, an unknown column, or obs_id in `set_` — the caller (the handler)
    turns that into a routed `fail("bad-params", ...)`, not an uncaught crash."""
    if obs_id is None:
        raise ValueError("obs_catalogue.update needs -ObsId")
    if _KEY in set_:
        raise ValueError(f"{_KEY!r} is the key, not a settable column — remove it from -Set")

    conn = _open_db(cfg)
    try:
        cols = {r[1] for r in conn.execute(f'PRAGMA table_info("{_TABLE}")')}
        bad = set(set_) - cols
        if bad:
            raise ValueError(
                f"unknown column(s) {sorted(bad)} — live columns are {sorted(cols)}")

        before = conn.execute(f'SELECT * FROM "{_TABLE}" WHERE {_KEY}=?', (obs_id,)).fetchone()
        if not before:
            raise ValueError(f"no {_TABLE} row with {_KEY}={obs_id}")
        before = dict(before)

        final = dict(set_)
        final.setdefault("last_modified", _now_iso())
        final.setdefault("catalogue_version", f"v2-{_today()}")

        ssql = ", ".join(f'"{k}"=?' for k in final)
        # bounded retry on a transient lock (as reportkit.archive_before_write); a connection held open
        # longer still raises OperationalError
        for attempt in range(_LOCK_RETRIES):
            try:
                conn.execute(f'UPDATE "{_TABLE}" SET {ssql} WHERE {_KEY}=?',
                            list(final.values()) + [obs_id])
                break
            except sqlite3.OperationalError as e:
                if attempt == _LOCK_RETRIES - 1 or "locked" not in str(e):
                    raise
                time.sleep(_LOCK_RETRY_DELAY)
        conn.commit()

        after = dict(conn.execute(f'SELECT * FROM "{_TABLE}" WHERE {_KEY}=?', (obs_id,)).fetchone())
        changed = {k: {"old": before.get(k), "new": after.get(k)} for k in final}
        return {"obs_id": obs_id, "changed": changed}
    finally:
        conn.close()
