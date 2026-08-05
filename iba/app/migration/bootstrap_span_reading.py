"""bootstrap_span_reading.py — ONE-OFF, idempotent: registers the `span_reading` table and the
`verse-span-reading` work package (steps `span_reading.build` + `report.span_reading`).

Schema is DDL (new table), so — same class of exception as `bootstrap_cfg_utility.py`/
`bootstrap_inactive_column.py`/`bootstrap_configuration_maintenance.py` (GOVERNANCE.md §9B/§14) —
this is a direct, documented, idempotent bootstrap, not a `configmaint.propose` call:
`configmaint.propose` can only write rows on already-existing tables/columns, not create either.
The work package/step registration follows `bootstrap_passage_debate_sync.py`'s established
direct-insert pattern (infrastructure registration, not row-by-row `propose` — the researcher's own
extensive design-review-and-approval across the 2026-08-05 session IS the up-front design approval
that carve-out requires).

**What this replaces.** `report.verse_span_meaning` fetches `morph_code` and compound
`strong_variant` codes but never uses them: multi-code spans render as disconnected dictionary
dumps, and morph-driven stem/voice selection never happens — every downstream reading pass was
forced to silently reconstruct that structural work itself, ad hoc, un-persisted, every verse (see
`iba/app/reports/t1-t3-design-decisions-20260805.md` for the full diagnosis and design record).
`span_reading` is the fix: one row PER CODE within a span (not per span), holding a mechanically
resolved — never interpreted — reading: which stem/voice the code's own morph settles on, whether
the code is a genuine lexical entry or a grammatical formative (and therefore correctly has no
independent sense, not a data gap), and, only when the sibling/base-fallback ambiguity check
already used by `versespanmeaningreport.meaning_for_code` actually fires, a named-not-resolved
ambiguity note.

**Role classification — the mechanical rule, not a guess.** Hebrew: STEP reserves the `H9000-H9999`
number range specifically for grammatical formatives (definite article, prefixed prepositions/
conjunctions, pronominal suffixes, directional-he) — confirmed against every function-word code
seen in this session's working files (H9002=and, H9003=in, H9005=to/for, H9009=the, H9011=
directional-he, H9020/9028/9030/9033/9038/9040=suffixes). Codes in that range are NOT independent
lexical entries by STEP's own convention — **but they DO carry a real `stepGloss` and a real
`strong_meaning_parsed` row** (H9002='and', H9009='[the]', "Prefix beth: in, among, with," etc.) —
an earlier version of this migration/module claimed otherwise and skipped resolving them entirely;
wrong, not checked at the time, caught by the researcher and corrected same day (see
`lib/spanreading.py`'s role-classification comment block for the fix). `role` is classification
metadata only — it does not gate resolution; every code, content or function, is resolved the same
way. Non-H9xxx Hebrew function-*looking* words like `H0413` "to," which DOES carry real lexical
content, are classified `content`. Greek has no equivalent reserved-number-range convention, so it
relies on `morph_code`'s own part-of-speech family alone — see `lib/spanreading.py:classify_role`
for the exact rule.

**Stem/voice selection — empirically verified against this DB, not asserted from memory.** No
morph-code legend exists anywhere in this repo (checked). The Hebrew binyan-letter-to-stem-name
mapping (`morph_code[2]` for `HV...` codes) was built by cross-checking real verbs' English glosses
against their own `(Qal)`/`(Niphal)`/etc.-labeled `strong_meaning_parsed` text, for every letter
actually occurring in `span.morph_code` (queried 2026-08-05):
q=Qal (H7971G "sends"), N=Niphal (H3811 "weary"), p=Piel (H1288 "bless"), P=Pual (H1878 "gorged" —
fat/passive sense; weaker fit on H5647G "serve," flagged in code), h=Hiphil (H5337 "deliver"),
H=Hophal (H2986 "rescued"/borne), t=Hithpael (H6419 "prayed"), c=Tiphel (H8474, rare stem, matches
its rarity — 2 occurrences total), u=Hothpael (H1878's own rare last-listed stem, 1 occurrence
total). v (13 occurrences, all `H7812` "bow/worship," the textbook Hishtaphel root) could not be
confirmed against an explicitly `(Hishtaphel)`-labeled text segment — the source text lumps it under
`(Hithpael)`; `classify_role`/`resolve_content_sense` fail safe on this one letter (full available
text presented, not a guessed single-stem extraction) rather than assert an unverified mapping.
Greek voice (`V-TVM-...` Robinson/Byzantine tagging) is decoded by the well-documented standard
convention, not re-derived from scratch — lower re-verification depth than Hebrew, flagged in code.

    python -m iba.app.migration.bootstrap_span_reading
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

TABLE = "span_reading"

WP = "verse-span-reading"
PS_SCRIPT = "iba/app/ps/VerseSpanReading.ps1"

STEP_BUILD = "span_reading.build"
HANDLER_BUILD = "iba.app.handlers.spanreading:build"
DOES_BUILD = (
    "verse : span_reading extract — mechanical T1-T3 engine: for every code in a span's "
    "(possibly compound) strong_variant, classifies role (content lexical entry vs. grammatical "
    "formative), stem/voice-selects the operative sense from strong_meaning_parsed via morph_code "
    "(not the whole six-stem/voice paradigm), and flags — never resolves — the sibling/base-"
    "fallback ambiguity case versespanmeaningreport.meaning_for_code already detects. Runs "
    "independent of T4-T9/passage_debate. Version-aware: soft-deletes the superseded row and "
    "inserts fresh on rewrite, same convention every other iba.db table already uses. Replaces "
    "report.verse_span_meaning (retired, see BUILD.md)."
)

STEP_REPORT = "report.span_reading"
HANDLER_REPORT = "iba.app.handlers.reports:span_reading_report"
DOES_REPORT = (
    "on-demand MD report, generated from span_reading (never an independent write) — EV verse "
    "text and the resolved lexical reading placed together, per book/passage range. Requires "
    "span_reading.build to have already run for this exact range."
)


def _create_table(conn: sqlite3.Connection, report: list[str]) -> None:
    existing = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    if TABLE not in existing:
        conn.execute(f"""
            CREATE TABLE {TABLE} (
                id             INTEGER PRIMARY KEY,
                span_id        INTEGER NOT NULL,
                verse_id       INTEGER NOT NULL,
                code_ordinal   INTEGER NOT NULL,
                strong         TEXT,
                morph_code     TEXT,
                role           TEXT NOT NULL,
                status         TEXT NOT NULL,
                resolved_sense TEXT,
                ambiguity_note TEXT,
                created_at     TEXT NOT NULL,
                deleted        INTEGER NOT NULL DEFAULT 0
            )
        """)
        report.append(f"table {TABLE} created")
    else:
        report.append(f"table {TABLE} already present")

    # (name, ordinal, type, is_pk, notnull, dflt, fk, use)
    cols = [
        ("id", 0, "INTEGER", 1, 1, None, None, "surrogate PK"),
        ("span_id", 1, "INTEGER", 0, 1, None, "span.id",
         "which span this reading is for — a span may carry several code_ordinal rows here "
         "(one per code in its compound strong_variant)"),
        ("verse_id", 2, "INTEGER", 0, 1, None, "verse.id",
         "denormalized from span, matches verse_passage's own precedent — query without joining "
         "through span"),
        ("code_ordinal", 3, "INTEGER", 0, 1, None, None,
         "position of this code within the span's space-joined strong_variant, 0-based"),
        ("strong", 4, "TEXT", 0, 0, None, "strong.strongNumber",
         "the single code this row resolves — may be NULL only if strong_variant itself is empty "
         "(should not occur in practice)"),
        ("morph_code", 5, "TEXT", 0, 0, None, None,
         "this code's own morph slice (space-split from span.morph_code in the same order)"),
        ("role", 6, "TEXT", 0, 1, None, None,
         "'content' (an independent lexical item) or 'function' (a grammatical formative, e.g. "
         "Hebrew H9xxx — see classify_role). Purely classification metadata: does NOT gate "
         "resolution (corrected 2026-08-05 — H9xxx codes DO carry a real stepGloss/"
         "strong_meaning_parsed row, an earlier version wrongly skipped resolving them)"),
        ("status", 7, "TEXT", 0, 1, None, None,
         "'resolved' (strong row found, sense pulled — applies to content AND function roles "
         "alike) or 'unregistered' (no strong row yet — a genuine coverage gap, regardless of "
         "role)"),
        ("resolved_sense", 8, "TEXT", 0, 0, None, None,
         "stem/voice-selected sense text for 'resolved' rows (content or function role alike); "
         "NULL only for 'unregistered' rows — a real gap, not a hedge — see "
         "feedback_no_hedge_pointers_in_complete_records"),
        ("ambiguity_note", 9, "TEXT", 0, 0, None, None,
         "set only when the sibling/base-fallback ambiguity check fires — live senses named, not "
         "resolved (T4's job, not this table's)"),
        ("created_at", 10, "TEXT", 0, 1, None, None, "ISO-8601 UTC"),
        ("deleted", 11, "INTEGER", 0, 1, "0", None,
         "version-aware soft-delete — rewriting a (span_id, code_ordinal) inserts a fresh row and "
         "flips the superseded row's deleted to 1, same convention as verse/span/strong"),
    ]
    for name, ordinal, type_, is_pk, notnull, dflt, fk, use in cols:
        if not conn.execute(
                f"SELECT 1 FROM cfg_column WHERE table_name='{TABLE}' AND name=?",
                (name,)).fetchone():
            conn.execute(
                'INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, "notnull", '
                'is_unique, dflt, fk, use, expectation, source, filled_by) '
                f"VALUES ('{TABLE}',?,?,?,?,?,0,?,?,?,NULL,NULL,"
                "'migration/bootstrap_span_reading.py')",
                (name, ordinal, type_, is_pk, notnull, dflt, fk, use))
            report.append(f"cfg_column row for {TABLE}.{name} added")
        else:
            report.append(f"cfg_column row for {TABLE}.{name} already present")

    if not conn.execute(f"SELECT 1 FROM cfg_table WHERE name='{TABLE}'").fetchone():
        conn.execute(
            "INSERT INTO cfg_table (name, grain, use) VALUES (?,?,?)",
            (TABLE, "one row per Strong's code within a span (span_id, code_ordinal) — a "
                    "compound span yields several rows, one per component code",
             "L4b — DERIVED, version-aware. The mechanical T1-T3 reading: role classification + "
             "stem/voice-selected sense + named-not-resolved ambiguity, per code. Read by "
             "report.span_reading and, downstream, by T4-T9 — never by re-deriving from span/"
             "strong/strong_meaning_parsed directly."))
        report.append(f"cfg_table row for {TABLE} added")
    else:
        report.append(f"cfg_table row for {TABLE} already present")

    for col, ordinal in (("span_id", 0), ("code_ordinal", 1)):
        if not conn.execute(
                "SELECT 1 FROM cfg_unique WHERE table_name=? AND col=?", (TABLE, col)).fetchone():
            conn.execute("INSERT INTO cfg_unique VALUES (?,?,?)", (TABLE, col, ordinal))
            report.append(f"cfg_unique ({TABLE}, {col}) added")
        else:
            report.append(f"cfg_unique ({TABLE}, {col}) already present")


def _grant(conn: sqlite3.Connection, writer: str, table: str, report: list[str]) -> None:
    if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?",
                        (writer, table)).fetchone():
        conn.execute("INSERT INTO cfg_write_grant (writer, table_name, inactive) VALUES (?,?,0)",
                    (writer, table))
        report.append(f"cfg_write_grant ({writer}, {table}) added")
    else:
        report.append(f"cfg_write_grant ({writer}, {table}) already present")


def _register_work_package(conn: sqlite3.Connection, report: list[str]) -> None:
    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?", (WP,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_work_package (name, ps_script, runs_over, chained, "
            "complete_message, next_step_hint, paused_message, inactive) "
            "VALUES (?,?,'book',1,?,NULL,NULL,0)",
            (WP, PS_SCRIPT, "span_reading built and rendered for '{book}'."))
        report.append(f"cfg_work_package {WP!r} added")
    else:
        report.append(f"cfg_work_package {WP!r} already present")

    steps = [
        (0, STEP_BUILD, HANDLER_BUILD, DOES_BUILD),
        (1, STEP_REPORT, HANDLER_REPORT, DOES_REPORT),
    ]
    for ordinal, step, handler, does in steps:
        if not conn.execute("SELECT 1 FROM cfg_step WHERE work_package=? AND step=?",
                            (WP, step)).fetchone():
            conn.execute(
                "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                "inactive, kind) VALUES (?,?,?,?,?,?,0,?)",
                (WP, ordinal, step, handler, "book", does, "operations"))
            report.append(f"cfg_step {step!r} added")
        else:
            report.append(f"cfg_step {step!r} already present")

    on_fail = [
        (STEP_BUILD, "unreachable", "report-stop",
         "STEP is down and step.required_for_runs is true — cannot resolve any content-role "
         "code's sense without it.", "terminal"),
        (STEP_REPORT, "no-readings", "report-stop",
         "no span_reading rows exist yet for this exact book/range — run span_reading.build "
         "first (it is ordinal 0 of this same work package, run automatically before this step "
         "unless called standalone).", "terminal"),
    ]
    for step, condition, path, message, route in on_fail:
        if not conn.execute("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?",
                            (step, condition)).fetchone():
            conn.execute(
                "INSERT INTO cfg_on_fail (step, condition, path, resolver, message, route, "
                "inactive) VALUES (?,?,?,?,?,?,0)",
                (step, condition, path, None, message, route))
            report.append(f"cfg_on_fail ({step}, {condition}) added")
        else:
            report.append(f"cfg_on_fail ({step}, {condition}) already present")


def _register_report(conn: sqlite3.Connection, report: list[str]) -> None:
    if not conn.execute("SELECT 1 FROM cfg_report WHERE step=?", (STEP_REPORT,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
            "naming_scheme, archive_dir, inactive) VALUES (?,?,1,NULL,'md','stable','archive',0)",
            (STEP_REPORT, "{book} {range} — verse : span_reading extract"))
        report.append(f"cfg_report row for {STEP_REPORT} added")
    else:
        report.append(f"cfg_report row for {STEP_REPORT} already present")

    sections = [
        (0, "coverage", "## Reading coverage (content-role codes, this range)",
         "Reading coverage (content-role codes, this range)"),
        (1, "verses", "## Verses", "Verses"),
    ]
    for ordinal, key, heading, toc in sections:
        if not conn.execute(
                "SELECT 1 FROM cfg_report_section WHERE step=? AND section_key=?",
                (STEP_REPORT, key)).fetchone():
            conn.execute(
                "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, "
                "toc_label, include, inactive) VALUES (?,?,?,?,?,1,0)",
                (STEP_REPORT, ordinal, key, heading, toc))
            report.append(f"cfg_report_section ({STEP_REPORT}, {key}) added")
        else:
            report.append(f"cfg_report_section ({STEP_REPORT}, {key}) already present")


def _register_settings(conn: sqlite3.Connection, report: list[str]) -> None:
    import json
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?",
                        ("report.span_reading_output_pattern",)).fetchone():
        conn.execute(
            "INSERT INTO cfg_setting (key, value, use, module, inactive) VALUES (?,?,?,?,0)",
            ("report.span_reading_output_pattern", json.dumps("{book}-{range}-span-reading.md"),
             "filename pattern for report.span_reading ({book}/{range} substituted) — reuses "
             "report.verse_analysis_output_dir for the base folder, same as report.verse_span_"
             "meaning did", "report"))
        report.append("cfg_setting report.span_reading_output_pattern added")
    else:
        report.append("cfg_setting report.span_reading_output_pattern already present")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    _create_table(conn, report)
    _register_work_package(conn, report)
    _register_report(conn, report)
    _register_settings(conn, report)
    _grant(conn, STEP_BUILD, TABLE, report)

    conn.commit()
    conn.close()

    print("span_reading bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
