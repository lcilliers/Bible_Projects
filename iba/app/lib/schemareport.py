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
