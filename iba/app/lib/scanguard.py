"""scanguard.py -- protection against a long scan of a large table (escalation #2538; researcher, 2026-11-24: every scan for related data is pinpointed and direct).

Two protections, both read from cfg_setting layer.scan (no value is in the code):
  budget(conn, label)       a context manager: the statements run inside it are stopped, with ScanBudgetExceeded naming `label`, once they have used more than
                            `max_vm_ops` virtual-machine steps of SQLite (a pinpointed lookup uses a few thousand; a scan of ib_node uses hundreds of thousands)
  full_scans(conn, cfg, sql) the SCAN lines of the query plan of a statement, for the tests: a statement that searches by an index returns none
A statement that is run once for each item of a list is also refused by design: the lookups of the build take a chunk of ids (`chunk`) and use `chunks()`.
"""
from __future__ import annotations

import contextlib
import json


class ScanBudgetExceeded(Exception):
    """A statement used more work than cfg_setting layer.scan allows: a scan where a lookup by index was meant."""


def settings(cfg) -> dict:
    v = cfg.required_setting("layer.scan")
    return json.loads(v) if isinstance(v, str) else v


def chunks(seq, cfg_or_settings, key: str = "chunk"):
    st = cfg_or_settings if isinstance(cfg_or_settings, dict) else settings(cfg_or_settings)
    seq = list(seq)
    n = st[key]
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


@contextlib.contextmanager
def budget(conn, cfg, label: str, max_ops: int | None = None):
    st = settings(cfg)
    limit = max_ops or st["max_vm_ops"]
    step = st["progress_step"]
    used = [0]

    def tick():
        used[0] += step
        return 1 if used[0] > limit else 0          # a non-zero return aborts the running statement

    conn.set_progress_handler(tick, step)
    try:
        yield
    except Exception as exc:
        if used[0] > limit and "interrupted" in str(exc).lower():
            raise ScanBudgetExceeded(f"{label}: the statement used more than {limit} steps (a scan where a lookup by index was meant); nothing is written") from exc
        raise
    finally:
        conn.set_progress_handler(None, 0)


def full_scans(conn, cfg, sql: str, args=()) -> list[str]:
    """The lines of the query plan of a statement that SCAN a table instead of searching it by an index. A scan of a small driving list (cfg_setting layer.scan
    scan_ok: the temporary tables that hold the ids or pairs being looked up) is allowed; any other SCAN is returned, so the tests fail a statement that walks a large
    table (a SCAN names the alias of the table when the statement gives one)."""
    ok = settings(cfg)["scan_ok"]
    return [str(r[3]) for r in conn.execute("EXPLAIN QUERY PLAN " + sql, args) if str(r[3]).startswith("SCAN ") and not any(x in str(r[3]) for x in ok)]
