"""valuequality.py — the generic column-level VALUE-QUALITY engine: checks that a column's actual
values serve what it is declared for (`cfg_column.use`), beyond structure (row exists, FK resolves,
not-null, dedup key). Driven by `cfg_column.expectation`, three forms:

    notblank        value is not NULL and not empty/whitespace after trim
    nohtml          value contains no '<' character (catches leftover markup / an unsplit tree)
    pattern:<key>   value matches the regex stored at cfg_setting <key> (reuses an existing
                    setting, e.g. candidate.tag_clean_pattern -- never a parallel constant)

One column, one rule, one scan: a column is covered by setting its `cfg_column.expectation`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class ValueFinding:
    table: str
    column: str
    rule: str
    total: int          # rows considered (non-null, where relevant)
    violations: int
    samples: list = field(default_factory=list)   # every distinct violating (value, count), most
                                                    # frequent first, not capped (the persisted report
                                                    # is the review artifact); truncate only for display


def _has_deleted(cfg, table: str) -> bool:
    return "deleted" in cfg.column_names(table)


def _where_live(cfg, table: str) -> str:
    return "WHERE deleted=0" if _has_deleted(cfg, table) else ""


def _scope(live: str, extra_where: str) -> str:
    """Combine the standard deleted=0 live-filter with an optional caller-supplied scope
    clause (e.g. restricting to one word's strongs, or one book's verses)."""
    parts = [p for p in (live.replace("WHERE ", "", 1), extra_where) if p]
    return ("WHERE " + " AND ".join(parts)) if parts else ""


def _scan_notblank(cfg, table: str, column: str, extra_where: str = "", params: tuple = ()) -> ValueFinding:
    where = _scope(_where_live(cfg, table), extra_where)
    total = cfg.conn.execute(f'SELECT COUNT(*) FROM "{table}" {where}', params).fetchone()[0]
    cond = f'"{column}" IS NULL OR trim("{column}")=\'\''
    where2 = _scope(_where_live(cfg, table), f"({cond})" + (f" AND {extra_where}" if extra_where else ""))
    n = cfg.conn.execute(f'SELECT COUNT(*) FROM "{table}" {where2}', params).fetchone()[0]
    return ValueFinding(table, column, "notblank", total, n, [])


def _scan_nohtml(cfg, table: str, column: str, extra_where: str = "", params: tuple = ()) -> ValueFinding:
    where = _scope(_where_live(cfg, table), extra_where)
    total = cfg.conn.execute(f'SELECT COUNT(*) FROM "{table}" {where}', params).fetchone()[0]
    cond = f'"{column}" LIKE \'%<%\'' + (f" AND {extra_where}" if extra_where else "")
    where2 = _scope(_where_live(cfg, table), cond)
    rows = cfg.conn.execute(f'SELECT "{column}" FROM "{table}" {where2}', params).fetchall()
    samples = [(r[0] or "")[:200] for r in rows]   # every violating value, not just the first 10
    return ValueFinding(table, column, "nohtml", total, len(rows), samples)


def _scan_pattern(cfg, table: str, column: str, setting_key: str,
                  extra_where: str = "", params: tuple = ()) -> ValueFinding:
    pattern = re.compile(cfg.setting(setting_key, r"^[A-Za-z][A-Za-z' -]*$"))
    cond = f'"{column}" IS NOT NULL' + (f" AND {extra_where}" if extra_where else "")
    where = _scope(_where_live(cfg, table), cond)
    total = cfg.conn.execute(f'SELECT COUNT(*) FROM "{table}" {where}', params).fetchone()[0]
    rows = cfg.conn.execute(
        f'SELECT "{column}" v, COUNT(*) n FROM "{table}" {where} GROUP BY "{column}"', params).fetchall()
    messy = [(r["v"], r["n"]) for r in rows if not pattern.match(r["v"] or "")]
    violations = sum(n for _, n in messy)
    samples = sorted(messy, key=lambda t: -t[1])   # every distinct violating value, not just top 10
    return ValueFinding(table, column, f"pattern:{setting_key}", total, violations, samples)


def scan_column(cfg, table: str, column: str, expectation: str,
                extra_where: str = "", params: tuple = ()) -> ValueFinding | None:
    """Scan ONE column against a given expectation string, optionally scoped (e.g. to one word's
    rows or one book's verses) — the piece validation.py's per-word/per-book reports reuse so a
    reviewer sees value-quality findings scoped to what they're actually looking at, not just the
    whole-table picture in candidate-quality.md."""
    if expectation == "notblank":
        return _scan_notblank(cfg, table, column, extra_where, params)
    if expectation == "nohtml":
        return _scan_nohtml(cfg, table, column, extra_where, params)
    if expectation.startswith("pattern:"):
        return _scan_pattern(cfg, table, column, expectation[len("pattern:"):], extra_where, params)
    return None    # enum.* — structural, see find_enum_violations


def find_value_quality_findings(cfg) -> list[ValueFinding]:
    """Every cfg_column row with a non-null expectation matching notblank/nohtml/pattern:*,
    scanned whole-table against the live data. Skips enum.* (handled separately, structurally, in
    handlers/configmaint.py — a coherence check, not a value-quality judgement call)."""
    out: list[ValueFinding] = []
    for r in cfg.conn.execute(
            "SELECT table_name, name, expectation FROM cfg_column WHERE expectation IS NOT NULL"):
        f = scan_column(cfg, r["table_name"], r["name"], r["expectation"])
        if f:
            out.append(f)
    return out


def find_enum_violations(conn) -> list[str]:
    """Every cfg_column row whose expectation is enum.<name>: every live value in that column must be a
    member of the cfg_enum set. A structural coherence check: a violation is a hard fault, report-stop.
    Each column is read from its own database (`cfg_column.database`, one cached connection per
    database), and soft-deleted rows (`deleted` or `delete_flagged`) are excluded."""
    out: list[str] = []
    other_conns: dict[str, object] = {}

    def _conn_for(database: str):
        if database in (None, "iba"):
            return conn
        if database not in other_conns:
            # Same lookup Cfg.database_path() does (database.<name>.path), read directly off the
            # already-open iba.db connection rather than opening a second Cfg/connection just to
            # make that one call -- this connection already has everything the lookup needs.
            import json
            import pathlib
            import sqlite3 as _sqlite3
            row = conn.execute(
                "SELECT value FROM cfg_setting WHERE key=? AND inactive=0",
                (f"database.{database}.path",)).fetchone()
            if row is None:
                raise KeyError(f"no database.{database}.path setting -- is {database!r} a "
                               f"registered project_database?")
            repo_root = pathlib.Path(conn.execute("PRAGMA database_list").fetchone()[2]
                                     ).resolve().parent.parent.parent.parent
            target_conn = _sqlite3.connect(repo_root / json.loads(row["value"]))
            target_conn.row_factory = conn.row_factory
            other_conns[database] = target_conn
        return other_conns[database]

    try:
        for r in conn.execute(
                "SELECT database, table_name, name, expectation FROM cfg_column "
                "WHERE expectation LIKE 'enum.%'"):
            database, table, column = r["database"], r["table_name"], r["name"]
            enum_name = r["expectation"][len("enum."):]
            valid = {v[0] for v in conn.execute(
                "SELECT value FROM cfg_enum WHERE name=?", (enum_name,))}
            if not valid:
                out.append(f"value-quality: {table}.{column} declares expectation "
                           f"enum.{enum_name!r} but that enum has no members in cfg_enum")
                continue
            target = _conn_for(database)
            dead_col = None
            for candidate in ("deleted", "delete_flagged"):
                if target.execute(
                        "SELECT 1 FROM pragma_table_info(?) WHERE name=?",
                        (table, candidate)).fetchone():
                    dead_col = candidate
                    break
            live = f"WHERE {dead_col}=0" if dead_col else ""
            rows = target.execute(f'SELECT DISTINCT "{column}" v FROM "{table}" {live}').fetchall()
            bad = sorted({r2["v"] for r2 in rows if r2["v"] is not None and r2["v"] not in valid})
            if bad:
                out.append(f"value-quality: {table}.{column} has value(s) outside "
                           f"enum.{enum_name} {sorted(valid)}: {bad}")
    finally:
        for c in other_conns.values():
            c.close()
    return out
