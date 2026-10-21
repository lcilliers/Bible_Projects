"""schemareport.py — the data-schema snapshot of iba.db (`write_report()`) and of bible_research.db
(`write_report_bible_research()`). Introspects the live DB (`PRAGMA table_info` /
`foreign_key_list` / `index_list`) and merges it against `cfg_table`/`cfg_column` (the curated
registries, governance.tables / governance.table_columns), flagging discrepancies at table and column
level (#1306). No CSV pairing: the report already is the schema.
"""

from __future__ import annotations

import datetime
import pathlib
import sqlite3

from . import reportkit


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# Tables retired at the DATA level (soft-deleted on effectively every row,
# migration/retract_passage_system.py), named explicitly (#394) rather than inferred from a
# deleted-row percentage.
RETIRED_TABLES = {
    "passage": "reports/archive/passage-system-retirement-record-20260726.md",
    "verse_passage": "reports/archive/passage-system-retirement-record-20260726.md",
}


def _live_count(conn, table: str) -> int:
    """Row count excluding soft-deleted rows (`deleted=1`) where the column exists — escalation
    #395 ("record counts of deleted rows"): a raw COUNT(*) was showing e.g. `passage` as 18,528
    rows when only 24 are actually live, the other 18,504 soft-deleted by the retirement above."""
    cols = {r[1] for r in conn.execute(f'PRAGMA table_info("{table}")')}
    if "deleted" in cols:
        return conn.execute(f'SELECT COUNT(*) FROM "{table}" WHERE deleted=0').fetchone()[0]
    return conn.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]


def _tbl(headers, rows):
    L = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        L.append("| " + " | ".join(str(c) if c is not None else "" for c in r) + " |")
    return L


def _cfg_tables(cfg_conn: sqlite3.Connection, database: str) -> dict[str, dict]:
    """cfg_table rows for one `database` value, keyed by table name -- the governing registry
    behind `governance.tables` ("each table in the project must be listed in cfg_table with a
    proper use text. This applies to all databases.")."""
    cur = cfg_conn.execute(
        'SELECT name, grain, "use", inactive, category FROM cfg_table WHERE database=?', (database,))
    cols = [d[0] for d in cur.description]
    return {row[0]: dict(zip(cols, row)) for row in cur.fetchall()}


def _cfg_columns(cfg_conn: sqlite3.Connection, database: str, table: str) -> dict[str, dict]:
    """cfg_column rows for one `database`+`table`, keyed by column name -- `governance.
    table_columns`'s registry ("each column in each table... must be listed in cfg_column with a
    proper use text")."""
    cur = cfg_conn.execute(
        'SELECT name, type, is_pk, "notnull", fk, "use" FROM cfg_column '
        "WHERE database=? AND table_name=?", (database, table))
    cols = [d[0] for d in cur.description]
    return {row[0]: dict(zip(cols, row)) for row in cur.fetchall()}


def _table_discrepancy(cfg_row: dict | None, in_live: bool, live_count: int) -> str:
    if cfg_row is None:
        return "**NOT IN cfg_table**"
    if not in_live:
        return "**NO LIVE TABLE** (stale cfg_table row)"
    if cfg_row["inactive"] and live_count:
        return "**inactive in cfg_table but has live rows**"
    if not (cfg_row["use"] or "").strip():
        return "**no use text**"
    return ""


def _column_discrepancy(cfg_col: dict | None, live_type: str) -> str:
    if cfg_col is None:
        return "**NOT IN cfg_column**"
    cfg_type = (cfg_col["type"] or "").strip()
    if cfg_type and live_type and cfg_type.upper() != live_type.upper():
        return f"**type mismatch** (cfg={cfg_type})"
    if not (cfg_col["use"] or "").strip():
        return "no use text"
    return ""


def _table_section(cfg_conn, live_conn, database: str, live_tables: list[str],
                   counts: dict[str, int]) -> tuple[list[str], list[str]]:
    """Shared table-inventory + per-table-detail builder, merging live introspection against
    cfg_table/cfg_column for one `database`. Returns (overview_lines, tables_lines)."""
    cfg_tables = _cfg_tables(cfg_conn, database)
    if database == "iba":
        # DATA tables only: `cfg_%` tables are excluded from the cfg_table merge set too, as from
        # live_tables (CONFIG-REPORT.md covers them)
        cfg_tables = {k: v for k, v in cfg_tables.items() if not k.startswith("cfg_")}
    all_names = sorted(set(live_tables) | set(cfg_tables))
    gap_count = sum(1 for t in all_names
                    if _table_discrepancy(cfg_tables.get(t), t in live_tables,
                                          counts.get(t, 0)))

    overview = _tbl(["table", "rows (live)", "cfg use", "category", "discrepancy"], [
        [t, counts.get(t, "—") if t in live_tables else "—",
         (cfg_tables.get(t, {}).get("use") or "")[:80],
         cfg_tables.get(t, {}).get("category") or "",
         ("**RETIRED**" if t in RETIRED_TABLES else "")
         + _table_discrepancy(cfg_tables.get(t), t in live_tables, counts.get(t, 0))]
        for t in all_names])
    overview += ["", f"- {len(live_tables)} live table(s), {len(cfg_tables)} registered in "
                     f"`cfg_table` (database='{database}'), **{gap_count} discrepanc{'y' if gap_count == 1 else 'ies'}**."]
    if RETIRED_TABLES and database == "iba":
        overview += ["", f"**Retired** ({len(RETIRED_TABLES)}) — soft-deleted at the data level, "
                         f"kept for the historical record, not part of the live system: "
                     + "; ".join(f"`{t}` (see `{rec}`)" for t, rec in RETIRED_TABLES.items())]

    tables_lines: list[str] = []
    for t in live_tables:
        retired_note = " — RETIRED, see note above" if t in RETIRED_TABLES else ""
        tables_lines.append(f"### {t} ({counts.get(t, 0)} row(s){retired_note})")
        tables_lines.append("")
        cfg_row = cfg_tables.get(t)
        if cfg_row and (cfg_row.get("use") or "").strip():
            tables_lines.append(f"cfg_table.use: {cfg_row['use']}")
            tables_lines.append("")
        cols = list(live_conn.execute(f'PRAGMA table_info("{t}")'))
        fks = {r[3]: f"{r[2]}.{r[4]}" for r in live_conn.execute(f'PRAGMA foreign_key_list("{t}")')}
        idx = [r[1] for r in live_conn.execute(f'PRAGMA index_list("{t}")')]
        cfg_cols = _cfg_columns(cfg_conn, database, t)
        col_names_live = {c[1] for c in cols}
        tables_lines += _tbl(["column", "type", "pk", "notnull", "fk", "cfg use", "discrepancy"], [
            [c[1], c[2], "✓" if c[5] else "", "✓" if c[3] else "", fks.get(c[1], ""),
             (cfg_cols.get(c[1], {}).get("use") or "")[:60],
             _column_discrepancy(cfg_cols.get(c[1]), c[2])]
            for c in cols])
        stale_cols = sorted(set(cfg_cols) - col_names_live)
        if stale_cols:
            tables_lines.append(f"cfg_column rows with no live column (stale, table {t!r}): "
                                + ", ".join(stale_cols))
        if idx:
            tables_lines.append(f"indexes: {', '.join(idx)}")
        tables_lines.append("")

    return overview, tables_lines


def write_report(cfg, path: pathlib.Path) -> pathlib.Path:
    conn = cfg.conn
    live = sorted(r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'cfg_%' "
        "AND name NOT LIKE 'sqlite_%'"))
    counts = {t: _live_count(conn, t) for t in live}

    overview, tables_lines = _table_section(conn, conn, "iba", live, counts)

    # "> Generated <ts> ..." line, as retention.write_report does
    intro = [
        f"> Generated {_now()} by `report.schema_overview`. Introspects the live DB directly and "
        f"merges it against `cfg_table`/`cfg_column` (database='iba') — always current, never "
        f"hand-maintained.", "",
        f"- data tables: **{len(live)}** live",
    ]

    sections = {"overview": overview, "tables": tables_lines}
    L = reportkit.render_scaffold(conn, "report.schema_overview", sections, intro=intro)
    path = reportkit.write_report(conn, "report.schema_overview", path, L)
    return path


def write_report_bible_research(cfg, path: pathlib.Path) -> pathlib.Path:
    """The `bible_research.db` counterpart to `write_report()` (#1306): same helpers, rendering and
    cfg_table/cfg_column merge (rows where `database='bible_research'`), structure only, always current.
    Introspection uses a second connection (`cfg.database_path('bible_research')`); `cfg.conn` (iba.db)
    supplies `cfg_report`/`cfg_report_section` and `cfg_table`/`cfg_column`."""
    research_conn = sqlite3.connect(cfg.database_path("bible_research"))
    try:
        live = sorted(r[0] for r in research_conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"))
        counts = {t: _live_count(research_conn, t) for t in live}

        overview, tables_lines = _table_section(cfg.conn, research_conn, "bible_research", live,
                                                counts)

        intro = [
            f"> Generated {_now()} by `report.schema_overview_bible_research`. Introspects the "
            f"live DB directly and merges it against `cfg_table`/`cfg_column` "
            f"(database='bible_research') — always current, never hand-maintained. For per-column "
            f"value profiles, see `iba/config/DBSchema/DBSchema.json` "
            f"(`iba/scripts/build_dbschema.py --db bible_research`).",
            "",
            f"- tables: **{len(live)}** live",
        ]

        sections = {"overview": overview, "tables": tables_lines}
        L = reportkit.render_scaffold(cfg.conn, "report.schema_overview_bible_research", sections,
                                      intro=intro)
        path = reportkit.write_report(cfg.conn, "report.schema_overview_bible_research", path, L)
        return path
    finally:
        research_conn.close()
