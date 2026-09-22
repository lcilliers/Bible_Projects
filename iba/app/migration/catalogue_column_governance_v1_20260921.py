"""catalogue_column_governance_v1_20260921.py — ONE-OFF migration, escalation #1818 v2, researcher
instruction verbatim: "the columns and the alignment of the data is for you to do. You should have
an explanation for what the columns should be in the config, and you should have enums for all the
values to understand, every column has a significance somewhere, and every row must be correct for
the purpose that is is designed for. if the column is redundant then remove it."

Four things, each grounded in what the column is actually used for (checked live, not guessed):

1. `prompt_seq` fix -- 9 live rows NULL (the #1712/#1723 newly-authored questions: D1.1.1/2,
   D2.1.1/2, D7.7.1, D9.1.1, D9.2.1, D11.2.1, D12.1.1). Confirmed live-consumed:
   `cataloguereport.py` orders its tiered listing by (tier, component_code, prompt_seq, obs_id), so
   NULL sorts first, displacing these 9 questions out of their intended in-component order. Every
   one of them is the sole (or first) member of a brand-new singleton component -- no ambiguity in
   what "1" (or "1, 2" for D1.1's two rows) means here.

2. `status` fix -- 4 live rows (the retired T7.3.x family) carry `status='active'` despite
   `deleted=1` -- the exact status/deleted disagreement `cfg_column`'s own historical note already
   flags as a known defect class in this table's prior (bible_research.db) life, now confirmed
   reproduced in the live iba.db copy too. `cfg_column`'s own registered `use` text for `status`
   already names the correct second value ("active | retired") -- it was simply never applied.

3. `cfg_enum` registered for 3 previously-uncontrolled columns (checked live: zero enum rows
   existed for any column of this table before this migration) -- `status`, `tier`, `scope` --
   each populated from the column's own live distinct values, not invented.

4. `cfg_column.use` upgraded from thin placeholders to real explanations for `section`,
   `prompt_seq`, `tier`, `scope`, `status` -- and `section` marked superseded/redundant, matching
   the EXACT precedent this same table's `cfg_column` rows already record for `pattern_type`/
   `source_word`/`source_registry_no` (all "DROPPED ... superseded by dimension/data_mechanism").
   `section` earns the same verdict on the same grounds: checked live, no stage-generator module
   (`versereadinggenerate.py`/`subgroupgenerate.py`/`charreadinggenerate.py`/
   `charanswergenerate.py`) ever reads it; its only live reader, `cataloguereport.py`, treats it
   purely as a documented DATA-QUALITY FINDING ("two competing section-naming schemes" -- the
   report's own module docstring), not a working classification. `dimension` (added #1712,
   confirmed clean across all 103 rows this same escalation) already does `section`'s original job
   -- which analytical bucket a question belongs to -- for the live D1-D12/M0/X0/F0 scheme.
   NOT dropping the column itself (cataloguereport.py still reads it for historical audit value,
   and a column drop is a bigger, unnecessary schema change) -- marked deprecated in cfg_column
   only, matching how the other 3 dropped columns were also documented rather than physically
   removed.

Idempotent throughout (checks live value/existing enum rows before writing).

    python -m iba.app.migration.catalogue_column_governance_v1_20260921
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_TABLE = "wa_obs_question_catalogue"

_PROMPT_SEQ_FIX = {
    "D1.1.1": 1, "D1.1.2": 2,
    "D2.1.1": 1, "D2.1.2": 2,
    "D7.7.1": 1,
    "D9.1.1": 1,
    "D9.2.1": 1,
    "D11.2.1": 1,
    "D12.1.1": 1,
}

_STATUS_FIX_CODES = ("T7.3.1", "T7.3.2", "T7.3.3", "T7.3.4")
_RETIRED_STATUS = "retired"

_ENUM_STATUS = ["active", "retired"]
_ENUM_TIER = ["M0", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D9", "D10", "D11", "D12", "X0",
             "F0", "T7"]
_ENUM_SCOPE = ["Word/term (lexical)", "Verse-context", "The verse", "Characteristic (HIB "
              "behaviour)", "Characteristic relational", "The HIB", "Other non-human beings"]

_COLUMN_USE = {
    "section": ("SUPERSEDED 2026-09-21, escalation #1818 -- redundant with `dimension` "
        "(#1712, 2026-09-17). Carries the OLD pre-realignment T0-T7 scheme label for 92 of 103 "
        "live rows; `dimension` already carries the live D1-D12/M0/X0/F0 classification for every "
        "row, confirmed clean. Checked live before deciding this: no stage-generator module "
        "(verse-reading/char-subgroup/char-reading/char-answers) ever reads `section` -- its only "
        "live reader is cataloguereport.py, which treats it purely as a documented data-quality "
        "finding ('two competing section-naming schemes'), not a working classification. Same "
        "verdict already applied in this table to `pattern_type`/`source_word`/"
        "`source_registry_no` -- kept for historical/audit value, not read as authoritative by any "
        "live code. Use `dimension` for the live classification instead."),
    "prompt_seq": ("Display-ordering only within (tier, component_code) -- confirmed live "
        "consumer: cataloguereport.py's own tiered listing (`ORDER BY tier, component_code, "
        "prompt_seq, obs_id`). NOT read by any of the 4 live LLM-calling stages (verse-reading/"
        "char-subgroup/char-reading/char-answers select question_code/question_text/scope only, "
        "never prompt_seq) -- it has zero effect on which questions get asked or in what order "
        "the LLM actually sees them within a stage's own prompt; it only affects this one human-"
        "facing report's display order. NULL sorts first in SQLite ASC order, so a NULL row "
        "displays out of its intended sequence, not absent -- checked and fixed for all 9 rows "
        "that had it (2026-09-21, escalation #1818)."),
    "tier": ("The live analytical bucket a question belongs to, post-#1712 realignment "
        "(2026-09-17): M0 (word-level battery), D1-D12 (the 12 goal-derived dimensions), X0 "
        "(cross-characteristic synergy-stage synthesis), F0 (faculty engagement), or T7 (legacy, "
        "retired-only -- the 4 deleted T7.3.x rows, never migrated since they're superseded, not "
        "live). Registered as cfg_enum wa_obs_question_catalogue.tier, 2026-09-21."),
    "scope": ("The stage-selection bucket a question answers at -- checked live against every "
        "stage-generator module's own selection query, 2026-09-21 (escalation #1806 coverage "
        "audit): 'Characteristic (HIB behaviour)'/'Characteristic relational'/'The HIB'/'Other "
        "non-human beings' select Stage 4 (char-answers); 'Word/term (lexical)'/'Verse-context'/"
        "'The verse' are NOT selected by any live stage's query at all (escalation #1806's own "
        "still-open ask -- 27 of 103 questions are structurally unreachable on this basis, "
        "tracked there, not a defect in this column itself). Registered as cfg_enum "
        "wa_obs_question_catalogue.scope, 2026-09-21."),
    "status": ("Lifecycle state: 'active' (live, presented to a stage per its scope/mechanism) "
        "or 'retired' (superseded, `deleted` should also be 1 -- checked live 2026-09-21, "
        "escalation #1818: found and fixed 4 rows, the T7.3.x family, that had deleted=1 but "
        "status still 'active', the exact status/deleted-disagreement defect class this table's "
        "own migration history already flagged as a known risk). Registered as cfg_enum "
        "wa_obs_question_catalogue.status, 2026-09-21."),
}


def fix_prompt_seq(conn: sqlite3.Connection) -> list[str]:
    report = []
    for code, seq in sorted(_PROMPT_SEQ_FIX.items()):
        row = conn.execute(
            f"SELECT prompt_seq FROM {_TABLE} WHERE question_code=? AND deleted=0", (code,)
        ).fetchone()
        if row is None:
            report.append(f"{code}: SKIPPED -- no live row found")
            continue
        if row[0] == seq:
            report.append(f"{code}: prompt_seq already {seq} -- no-op")
            continue
        conn.execute(
            f"UPDATE {_TABLE} SET prompt_seq=? WHERE question_code=? AND deleted=0", (seq, code))
        report.append(f"{code}: prompt_seq NULL -> {seq}")
    return report


def fix_status(conn: sqlite3.Connection) -> list[str]:
    report = []
    for code in _STATUS_FIX_CODES:
        row = conn.execute(
            f"SELECT status, deleted FROM {_TABLE} WHERE question_code=?", (code,)).fetchone()
        if row is None:
            report.append(f"{code}: SKIPPED -- no row found")
            continue
        status, deleted = row
        if status == _RETIRED_STATUS:
            report.append(f"{code}: status already 'retired' -- no-op")
            continue
        conn.execute(
            f"UPDATE {_TABLE} SET status=? WHERE question_code=?", (_RETIRED_STATUS, code))
        report.append(f"{code}: status 'active' -> 'retired' (deleted={deleted}, was disagreeing)")
    return report


def register_enums(conn: sqlite3.Connection) -> list[str]:
    report = []
    for enum_name, values in (
        (f"{_TABLE}.status", _ENUM_STATUS),
        (f"{_TABLE}.tier", _ENUM_TIER),
        (f"{_TABLE}.scope", _ENUM_SCOPE),
    ):
        existing = conn.execute(
            "SELECT COUNT(*) FROM cfg_enum WHERE name=?", (enum_name,)).fetchone()[0]
        if existing:
            report.append(f"{enum_name}: already has {existing} row(s) -- no-op")
            continue
        for i, value in enumerate(values, start=1):
            conn.execute(
                "INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)",
                (enum_name, value, i))
        report.append(f"{enum_name}: registered {len(values)} value(s)")
    return report


def update_column_use(conn: sqlite3.Connection) -> list[str]:
    report = []
    for column, use_text in _COLUMN_USE.items():
        row = conn.execute(
            "SELECT use FROM cfg_column WHERE database='iba' AND table_name=? AND name=?",
            (_TABLE, column)).fetchone()
        if row is None:
            report.append(f"{column}: SKIPPED -- no cfg_column row found for database='iba'")
            continue
        if row[0] == use_text:
            report.append(f"{column}: use text already current -- no-op")
            continue
        conn.execute(
            "UPDATE cfg_column SET use=? WHERE database='iba' AND table_name=? AND name=?",
            (use_text, _TABLE, column))
        report.append(f"{column}: cfg_column.use updated")
    return report


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        seq_report = fix_prompt_seq(conn)
        status_report = fix_status(conn)
        enum_report = register_enums(conn)
        column_report = update_column_use(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print("--- prompt_seq fix ---")
    print("\n".join(seq_report))
    print("\n--- status fix ---")
    print("\n".join(status_report))
    print("\n--- cfg_enum registration ---")
    print("\n".join(enum_report))
    print("\n--- cfg_column.use updates ---")
    print("\n".join(column_report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
