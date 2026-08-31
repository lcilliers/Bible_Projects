"""schemareport.py — the IBA app's own DATA-schema snapshot, one of the four "missing reports"
from PLAN-reports-config-governance-v1-20260722.md §3.4. There was no equivalent of the Bible-study
side's `DBSchema.json`/`build_dbschema.py` for the IBA app's 17 data tables (only `cfgreport.py` §8
documents the config-governed tables). Introspects the live DB directly (`PRAGMA table_info` /
`foreign_key_list` / `index_list`) — no CSV pairing: this report already *is* the schema, a CSV of
it would just be the same information reformatted.
"""

from __future__ import annotations

import datetime
import pathlib
import sqlite3

from . import reportkit


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# the app's own data tables — everything that isn't a cfg_* config-store table. Kept as an explicit
# list (not "every non-cfg_ table") so a genuinely new data table gets a deliberate decision to add
# it here, the same discipline REPORT_STEPS/QUALITY_CHECK_REPORT_PATH already apply elsewhere.
# Escalation #396 (2026-07-30, "does not include all the active tables eg parse tables"): the four
# `strong_*_parsed`/`strong_related` tables were live and populated (10k-34k rows each) but missing
# here — they only ever showed up as a footnote ("live but not in DATA_TABLES"), never actually
# documented in the per-table detail section. Added as the deliberate decision this list requires.
DATA_TABLES = (
    "candidate_seed", "escalation", "lemma_inventory", "passage", "run", "span", "span_candidate",
    "strong", "strong_lexicon", "strong_lsj_parsed", "strong_meaning_parsed", "strong_meaning_tree",
    "strong_mounce_parsed", "strong_related", "strong_sense", "strong_verse",
    "validation_result", "verse", "verse_passage", "word_registry", "word_strong",
    # Added 2026-08-31 (escalation #1306, researcher: "the schema report for IBA is simply wrong
    # and incomplete") -- 19 live tables sitting in the "live but not in DATA_TABLES" footnote,
    # same class of gap escalation #396 already fixed once for the strong_*_parsed tables. Every
    # one checked live (real, populated tables, not test debris) before adding, same discipline
    # #396 itself named.
    "cluster", "cluster_strong", "content_index", "content_index_scan", "debate_change_detail",
    "escalation_history", "escalations_old", "file_manifest", "folder_purpose", "hib",
    "hib_referent_option", "operation", "operation_party", "passage_emergent_question",
    "passage_insufficiency", "passage_linkage", "passage_validation_note", "phenomenon",
    "verse_hib", "verse_lexical",
)

# Tables the researcher has formally retired at the DATA level (soft-deleted `deleted=1` on
# effectively every row via `migration/retract_passage_system.py`) — NOT the same thing as the
# 2026-07-23 candidate-system retraction, which only retracted CONFIG (cfg_step/cfg_work_package/
# etc. — see `migration/retract_candidate_system.py`) and left `candidate_seed`/`span_candidate`'s
# actual DATA untouched. Kept as an explicit, named fact (same discipline `DATA_TABLES` itself
# already uses) rather than inferred from a deleted-row percentage, which would be a fragile,
# ever-changing signal for any table with ordinary per-row curation (e.g. `candidate_seed` has 281
# individually-rejected rows out of 2087 — real but unrelated to a whole-table retirement).
# Escalation #394 ("tables marked as deleted or not applicable"). Record:
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


def write_report(cfg, path: pathlib.Path) -> pathlib.Path:
    conn = cfg.conn
    live = {r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'cfg_%' "
        "AND name NOT LIKE 'sqlite_%'")}
    missing = [t for t in DATA_TABLES if t not in live]
    extra = sorted(live - set(DATA_TABLES))

    counts = {t: _live_count(conn, t) for t in DATA_TABLES if t in live}

    # Escalation #393 (2026-07-30): this report had no generated-at timestamp at all — every
    # sibling report (retention.py, cfgreport.py) states one, this one only named the step. Fixed
    # to match the same "> Generated <ts> ..." convention `retention.write_report` uses.
    intro = [
        f"> Generated {_now()} by `report.schema_overview`. Introspects the live DB directly — "
        f"always current, never hand-maintained.", "",
        f"- data tables: **{len(DATA_TABLES)}** known, **{len(live)}** live",
    ]

    sections: dict[str, list[str]] = {}

    S = _tbl(["table", "rows (live)", "status"], [
        [t, counts.get(t, "—"), "**RETIRED**" if t in RETIRED_TABLES else ""]
        for t in DATA_TABLES])
    if RETIRED_TABLES:
        S += ["", f"**Retired** ({len(RETIRED_TABLES)}) — soft-deleted at the data level, kept for "
                 f"the historical record, not part of the live system: "
             + "; ".join(f"`{t}` (see `{rec}`)" for t, rec in RETIRED_TABLES.items())]
    if missing:
        S += ["", f"**In `DATA_TABLES` but not live** (schemareport.py's list is stale): "
                 + ", ".join(missing)]
    if extra:
        S += ["", f"**Live but not in `DATA_TABLES`** (a new table — add it to "
                 f"`schemareport.DATA_TABLES` deliberately): " + ", ".join(extra)]
    sections["overview"] = S

    S = []
    for t in DATA_TABLES:
        if t not in live:
            continue
        retired_note = " — RETIRED, see note above" if t in RETIRED_TABLES else ""
        S.append(f"### {t} ({counts.get(t, 0)} row(s){retired_note})")
        S.append("")
        cols = list(conn.execute(f'PRAGMA table_info("{t}")'))
        fks = {r[3]: f"{r[2]}.{r[4]}" for r in conn.execute(f'PRAGMA foreign_key_list("{t}")')}
        idx = [r[1] for r in conn.execute(f'PRAGMA index_list("{t}")')]
        S += _tbl(["column", "type", "pk", "notnull", "fk"], [
            [c[1], c[2], "✓" if c[5] else "", "✓" if c[3] else "", fks.get(c[1], "")]
            for c in cols])
        if idx:
            S.append(f"indexes: {', '.join(idx)}")
        S.append("")
    sections["tables"] = S

    L = reportkit.render_scaffold(conn, "report.schema_overview", sections, intro=intro)
    path = reportkit.write_report(conn, "report.schema_overview", path, L)
    return path


def write_report_bible_research(cfg, path: pathlib.Path) -> pathlib.Path:
    """The `bible_research.db` counterpart to `write_report()` above -- escalation #1306, 2026-08-31
    (researcher: "There is no report for Bible_Research_db and no handle in the excel tools for
    this report"). Deliberately mirrors that function's shape (same helpers, same rendering), not a
    separate design: introspects the live DB directly via `PRAGMA`, no separately-maintained
    register to go stale (unlike `iba/config/DBSchema/DBSchema.json`/`build_dbschema.py`, which
    profiles column VALUES and needs an explicit rebuild -- this stays deliberately lighter,
    structure-only, always current by construction, same trade-off `schemareport.py`'s own
    docstring already made for the IBA side).

    No curated `DATA_TABLES` allowlist here: `bible_research.db` has no cfg_*-style config/data
    split to filter out (every table there is a "data" table), so every real table is shown --
    ~113 of them, not a hand-picked subset. `conn` for introspection is a second, separate
    connection to `bible_research.db` (`cfg.database_path('bible_research')`, the same pattern
    `cataloguereport.py`/`table_export` already use); `cfg.conn` (iba.db) is still what
    `render_scaffold`/`write_report` read `cfg_report`/`cfg_report_section` from -- config lives in
    iba.db regardless of which database the report is ABOUT."""
    research_conn = sqlite3.connect(cfg.database_path("bible_research"))
    try:
        tables = sorted(r[0] for r in research_conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"))
        counts = {t: _live_count(research_conn, t) for t in tables}

        intro = [
            f"> Generated {_now()} by `report.schema_overview_bible_research`. Introspects the "
            f"live DB directly — always current, never hand-maintained. For per-column "
            f"descriptions and data profiles, see `iba/config/DBSchema/DBSchema.json` "
            f"(`iba/scripts/build_dbschema.py --db bible_research`).",
            "",
            f"- tables: **{len(tables)}**",
        ]

        sections: dict[str, list[str]] = {}
        sections["overview"] = _tbl(["table", "rows"], [[t, counts[t]] for t in tables])

        S = []
        for t in tables:
            S.append(f"### {t} ({counts[t]} row(s))")
            S.append("")
            cols = list(research_conn.execute(f'PRAGMA table_info("{t}")'))
            fks = {r[3]: f"{r[2]}.{r[4]}" for r in research_conn.execute(
                f'PRAGMA foreign_key_list("{t}")')}
            idx = [r[1] for r in research_conn.execute(f'PRAGMA index_list("{t}")')]
            S += _tbl(["column", "type", "pk", "notnull", "fk"], [
                [c[1], c[2], "✓" if c[5] else "", "✓" if c[3] else "", fks.get(c[1], "")]
                for c in cols])
            if idx:
                S.append(f"indexes: {', '.join(idx)}")
            S.append("")
        sections["tables"] = S

        L = reportkit.render_scaffold(cfg.conn, "report.schema_overview_bible_research", sections,
                                      intro=intro)
        path = reportkit.write_report(cfg.conn, "report.schema_overview_bible_research", path, L)
        return path
    finally:
        research_conn.close()
