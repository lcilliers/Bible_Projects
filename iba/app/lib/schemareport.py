"""schemareport.py — the IBA app's own DATA-schema snapshot, one of the four "missing reports"
from PLAN-reports-config-governance-v1-20260722.md §3.4. There was no equivalent of the Bible-study
side's `DBSchema.json`/`build_dbschema.py` for the IBA app's data tables (only `cfgreport.py` §8
documents the config-governed `cfg_*` tables). Introspects the live DB directly (`PRAGMA table_info` /
`foreign_key_list` / `index_list`) — no CSV pairing: this report already *is* the schema, a CSV of
it would just be the same information reformatted.

escalation #1306 (recovered 2026-08-31 -- the researcher's actual feedback crashed into #1341
instead of landing here, sat unapplied for hours): "I suspect the data comes straight from the DB
schema. However, the report should merge the data and the DB schema extract and show the
comparison. I can spot some that will show discrepancies. This applies for both the table level
and column level data and applies to both IBA and Bible research." Both `write_report()` (IBA) and
`write_report_bible_research()` below now merge live introspection against `cfg_table`/`cfg_column`
(governance.tables / governance.table_columns' own governing registries -- `database` is a real
column on both, already carrying rows for 'iba' and 'bible_research') and flag discrepancies at
both levels, instead of a pure live-only snapshot. This also retires the old hand-maintained
`DATA_TABLES` tuple (41 entries, chronically stale -- escalations #396 and #1306 both caught it
short of the live table count) in favour of cfg_table itself as the one curated table list, so it
can no longer silently drift out of sync with a second, code-resident copy of the same fact.
"""

from __future__ import annotations

import datetime
import pathlib
import sqlite3

from . import reportkit


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# Tables the researcher has formally retired at the DATA level (soft-deleted `deleted=1` on
# effectively every row via `migration/retract_passage_system.py`) — NOT the same thing as the
# 2026-07-23 candidate-system retraction, which only retracted CONFIG (cfg_step/cfg_work_package/
# etc. — see `migration/retract_candidate_system.py`) and left `candidate_seed`/`span_candidate`'s
# actual DATA untouched. Kept as an explicit, named fact (escalation #394, "tables marked as
# deleted or not applicable") rather than inferred from a deleted-row percentage, which would be a
# fragile, ever-changing signal for any table with ordinary per-row curation.
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
        # This report's own declared scope is the DATA tables only -- `cfg_%` rule/log tables are
        # deliberately excluded from `live_tables` above (same predicate the live-table query
        # uses), so they must be excluded from the cfg_table merge set too, or every real cfg_*
        # rule table (category='rule'/'log', not '%data%') falsely shows up as "NO LIVE TABLE" --
        # found live while first testing this build, not a hypothetical. CONFIG-REPORT.md is the
        # report that covers cfg_* tables; this one stays DATA-only, per its own module docstring.
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

    # Escalation #393 (2026-07-30): this report had no generated-at timestamp at all — every
    # sibling report (retention.py, cfgreport.py) states one, this one only named the step. Fixed
    # to match the same "> Generated <ts> ..." convention `retention.write_report` uses.
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
    """The `bible_research.db` counterpart to `write_report()` above -- escalation #1306, 2026-08-31
    (researcher: "There is no report for Bible_Research_db and no handle in the excel tools for
    this report"). Deliberately mirrors that function's shape (same helpers, same rendering, same
    cfg_table/cfg_column merge -- see #1306's recovered follow-up feedback in the module docstring),
    not a separate design: introspects the live DB directly via `PRAGMA`, no separately-maintained
    register to go stale (unlike `iba/config/DBSchema/DBSchema.json`/`build_dbschema.py`, which
    profiles column VALUES and needs an explicit rebuild -- this stays deliberately lighter,
    structure-only, always current by construction, same trade-off `schemareport.py`'s own
    docstring already made for the IBA side).

    Every real `bible_research.db` table is shown (~113), matched against `cfg_table`/`cfg_column`
    rows where `database='bible_research'` -- no curated allowlist here, `cfg_table` itself is now
    the one curated list, same as the IBA side. `conn` for introspection is a second, separate
    connection to `bible_research.db` (`cfg.database_path('bible_research')`, the same pattern
    `cataloguereport.py`/`table_export` already use); `cfg.conn` (iba.db) is still what
    `render_scaffold`/`write_report` read `cfg_report`/`cfg_report_section` from, and is also where
    `cfg_table`/`cfg_column` themselves live regardless of which database the report is ABOUT."""
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
