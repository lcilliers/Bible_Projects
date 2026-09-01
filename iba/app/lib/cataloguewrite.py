"""cataloguewrite.py — validated partial UPDATE of `wa_obs_question_catalogue`
(bible_research.db), by `obs_id`. Escalation #1007, researcher instruction (verbatim, this chat
turn): "start to build the table update tool... auto fill (catalogue version, last_modified
etc)... allow for resetting any column except (obs_id); key obs_id; [for a] column not specified
then ignore, else set old value with new value. I dont think there is any history control on this
table and I don't think it is necessary."

No change-log/history table — deliberate, per the researcher's own instruction above (contrast
`record_change_log`/`cfg_change_detail`, which DO exist for the tables that need them). A plain
`UPDATE`, not a propose/approve cycle — `configmaint.propose`'s approval gate is specific to
`cfg_*` rows (`governance.config_control`); this table is ordinary content, same class as
`prosestore.run_flag`'s direct write to `wa_data_quality_flags`.

Two columns are auto-filled when the caller doesn't name them in `-Set` (still overridable by
naming them explicitly — the "resetting any column except obs_id" instruction covers these too):

- `last_modified` — always `datetime.now(UTC)`, ISO-8601, matching the project-wide date
  convention (SQLite has no native DATETIME affinity).
- `catalogue_version` — `f"v2-{today}"`, matching the dominant live convention (188/424 rows use
  exactly the `v2-YYYY-MM-DD` shape — see `report.obs_catalogue`'s "naming schemes" section). The
  column has 6 different conventions in the live data with no single correct answer, so this
  default is a judgment call, not a fact — flagged as such when this tool was delivered, easy to
  override per-call by naming `catalogue_version` in `-Set`.
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
        # Bounded retry on a transient lock — same pattern/rationale as
        # reportkit.archive_before_write (escalation #1320): a genuinely held-open connection
        # (e.g. a SQLite viewer with bible_research.db open) still surfaces the real
        # OperationalError after these retries, uncaught, exactly as before -- this only clears a
        # moment's contention, seen twice live testing this tool in one session.
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
