"""bootstrap_lexicon_parsed_layer.py — ONE-OFF: register the lexicon-parsed layer as a real,
config-governed part of the app — brand-new mechanism (4 new tables, a new work package, 3 new
steps, a new report, a new cfg_enum value), so bootstrap-direct like
bootstrap_new_reports_phase1.py/bootstrap_configuration_maintenance.py, not configmaint.propose
(propose only writes rows on already-existing tables/columns).

WHY this layer exists. This session's exploratory work (iba/app/tools/build_meaning_tree_extract.py,
build_lsj_sense_extract.py, build_mounce_lexicon_extract.py, build_strong_related_extract.py)
found and fixed real parsing bugs in how strong_meaning_tree.sense_text / strong_lexicon.lsj /
strong_lexicon.mounce get read (comma/semicolon were wrongly treated as sense separators; a
multi-<b>-span row's refs/notes were pooled across the whole row instead of scoped per span) and
added a wholly new source — STEP's relatedNos, fetched live, not stored anywhere before. That
output only ever lived in outputs/csv|json/ — exploratory, not part of the app. This migration
brings the CORRECTED parse permanently into iba.db as its own layer, sitting on the raw layer
exactly the way strong_sense already does (cfg_table.strong.use: "the meaning is normalised out
(O4): it lives in strong_sense / strong_meaning_tree / strong_lexicon") — one more normalised-out
piece, not a new pattern.

  strong_meaning_parsed  — parsed strong_meaning_tree.sense_text, keyed by lemma_key (base only,
                           matching strong_meaning_tree's own key — it never carries a sub-entry
                           letter).
  strong_lsj_parsed      — parsed strong_lexicon.lsj, keyed by strong (the FULL code, matching
                           strong.strongNumber/strong_lexicon.strong exactly).
  strong_mounce_parsed   — parsed strong_lexicon.mounce, keyed by strong (full code).
  strong_related         — STEP's relatedNos, fetched live per full strong code. NOT part of
                           raw.detail's governed pull (discovery.follow_related is a different,
                           unrelated, currently-disabled hook — controls whether raw.discover
                           EXPANDS a new word's seed strongs by following relatedNos; this is
                           reference metadata on already-selected strongs, a distinct concern).
                           related_strong is NOT FK'd to strong.strongNumber — STEP can name a
                           code never onboarded here.

New work package `lexicon-parse` (standalone, not chained — like candidate-quality/passage-quality,
each step invoked independently, not a fixed sequence):
  lexicon.parse    — strong_meaning_tree + strong_lexicon -> the 3 parsed tables. No network,
                     deterministic, safe to re-run (clears and rebuilds).
  lexicon.related  — strong -> strong_related, one live STEP getInfo call per row. Per-code
                     failures are counted and reported, not fatal; STEP being unreachable at all is
                     ('unreachable', report-stop).
  lexicon.validate — read-only quality check (coverage: does every strong_lexicon/strong row have
                     produced parsed/related rows; value-quality via lib.valuequality on the parsed
                     gloss columns) + persists iba/app/reports/lexicon-parse.md every run
                     (governance.reports_must_persist) + escalates only if findings exist (same
                     shape as candidate.validate/passage.validate).

Physical tables are NOT hand-written CREATE TABLE here — cfg_column IS the schema (lib/db.py:
build_data_tables reads it to CREATE TABLE); this migration inserts the describing rows, then calls
that same function, so the DDL can never drift from what cfg_column says.

    python -m iba.app.migration.bootstrap_lexicon_parsed_layer --dry-run
    python -m iba.app.migration.bootstrap_lexicon_parsed_layer
"""
from __future__ import annotations

import argparse
import sqlite3
import sys

from ..lib.cfg import Cfg, DB_PATH
from ..lib.db import build_data_tables

REPORT: list[str] = []


def _table(conn, name, grain, use):
    if not conn.execute("SELECT 1 FROM cfg_table WHERE name=?", (name,)).fetchone():
        conn.execute("INSERT INTO cfg_table VALUES (?,?,?)", (name, grain, use))
        REPORT.append(f"cfg_table {name!r} added")
    else:
        REPORT.append(f"cfg_table {name!r} already present")


def _column(conn, table, name, ordinal, type_, is_pk=0, notnull=0, is_unique=0, dflt=None,
           fk=None, use="", expectation=None, source=None, filled_by=None):
    if not conn.execute("SELECT 1 FROM cfg_column WHERE table_name=? AND name=?",
                        (table, name)).fetchone():
        conn.execute(
            'INSERT INTO cfg_column ("table_name","name","ordinal","type","is_pk","notnull",'
            '"is_unique","dflt","fk","use","expectation","source","filled_by") '
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (table, name, ordinal, type_, is_pk, notnull, is_unique, dflt, fk, use, expectation,
             source, filled_by))
        REPORT.append(f"cfg_column ({table}, {name}) added")
    else:
        REPORT.append(f"cfg_column ({table}, {name}) already present")


def _grant(conn, writer, table):
    if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?",
                        (writer, table)).fetchone():
        conn.execute("INSERT INTO cfg_write_grant (writer, table_name, inactive) VALUES (?,?,0)",
                    (writer, table))
        REPORT.append(f"cfg_write_grant ({writer} -> {table}) added")
    else:
        REPORT.append(f"cfg_write_grant ({writer} -> {table}) already present")


def _work_package(conn, name, ps_script):
    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?", (name,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_work_package (name, ps_script, runs_over, chained, complete_message, "
            "next_step_hint, paused_message, inactive) VALUES (?,?,'none',0,NULL,NULL,NULL,0)",
            (name, ps_script))
        REPORT.append(f"cfg_work_package {name!r} added")
    else:
        REPORT.append(f"cfg_work_package {name!r} already present")


def _step(conn, wp, ordinal, step, handler, does):
    if not conn.execute("SELECT 1 FROM cfg_step WHERE work_package=? AND step=?",
                        (wp, step)).fetchone():
        conn.execute(
            "INSERT INTO cfg_step (work_package,ordinal,step,handler,scope,does,inactive) "
            "VALUES (?,?,?,?,'none',?,0)", (wp, ordinal, step, handler, does))
        REPORT.append(f"cfg_step {step!r} added")
    else:
        REPORT.append(f"cfg_step {step!r} already present")


def _on_fail(conn, step, condition, path, message, route):
    if not conn.execute("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?",
                        (step, condition)).fetchone():
        conn.execute(
            "INSERT INTO cfg_on_fail (step,condition,path,resolver,message,route,inactive) "
            "VALUES (?,?,?,NULL,?,?,0)", (step, condition, path, message, route))
        REPORT.append(f"cfg_on_fail ({step}, {condition}) added")
    else:
        REPORT.append(f"cfg_on_fail ({step}, {condition}) already present")


def _setting(conn, key, value, use, module):
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
        conn.execute("INSERT INTO cfg_setting (key,value,use,module,inactive) VALUES (?,?,?,?,0)",
                    (key, value, use, module))
        REPORT.append(f"cfg_setting {key!r} added")
    else:
        REPORT.append(f"cfg_setting {key!r} already present")


def _enum(conn, name, value, ordinal):
    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name=? AND value=?",
                        (name, value)).fetchone():
        conn.execute("INSERT INTO cfg_enum (name,value,ordinal,inactive) VALUES (?,?,?,0)",
                    (name, value, ordinal))
        REPORT.append(f"cfg_enum ({name}={value}) added")
    else:
        REPORT.append(f"cfg_enum ({name}={value}) already present")


def _report(conn, step, title, output_kind):
    if not conn.execute("SELECT 1 FROM cfg_report WHERE step=?", (step,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_report (step,title,show_toc,footer_text,output_kind,naming_scheme,"
            "archive_dir,inactive) VALUES (?,?,1,NULL,?,'stable','archive',0)",
            (step, title, output_kind))
        REPORT.append(f"cfg_report {step!r} added")
    else:
        REPORT.append(f"cfg_report {step!r} already present")


def _report_section(conn, step, ordinal, key, heading):
    if not conn.execute("SELECT 1 FROM cfg_report_section WHERE step=? AND section_key=?",
                        (step, key)).fetchone():
        conn.execute(
            "INSERT INTO cfg_report_section (step,ordinal,section_key,heading,toc_label,include,"
            "inactive) VALUES (?,?,?,?,?,1,0)",
            (step, ordinal, key, heading, heading.lstrip("# ").strip()))
        REPORT.append(f"cfg_report_section ({step}, {key}) added")
    else:
        REPORT.append(f"cfg_report_section ({step}, {key}) already present")


def _report_csv(conn, step, table, join_note):
    if not conn.execute("SELECT 1 FROM cfg_report_csv_table WHERE step=? AND table_name=?",
                        (step, table)).fetchone():
        conn.execute(
            "INSERT INTO cfg_report_csv_table (step,table_name,join_note,inactive) VALUES "
            "(?,?,?,0)", (step, table, join_note))
        REPORT.append(f"cfg_report_csv_table ({step}, {table}) added")
    else:
        REPORT.append(f"cfg_report_csv_table ({step}, {table}) already present")


def register(conn: sqlite3.Connection, physical_build: bool = True) -> None:
    # ── tables ────────────────────────────────────────────────────────────────
    _table(conn, "strong_meaning_parsed",
          "one row per gloss segment of a strong_meaning_tree lemma (2026-07-25 corrected parse)",
          "L2b — the parsed meaning layer over strong_meaning_tree (raw). Segment-scoped: refs/"
          "note belong to the exact <b> span they followed, not pooled across the whole source "
          "row (the original extract's bug, fixed before this table existed). Comma/semicolon are "
          "NOT sense separators here — only a literal line break splits a gloss further.")
    _table(conn, "strong_lsj_parsed",
          "one row per LSJ sense of a strong_lexicon.lsj entry (2026-07-25 corrected parse)",
          "L2b — the parsed classical-Greek lexicon layer over strong_lexicon.lsj (raw). Sense "
          "blocks split on LSJ's own <LevelN>/<br> structure; gloss kept whole within a block, not "
          "exploded on internal commas.")
    _table(conn, "strong_mounce_parsed",
          "one row per Mounce sense of a strong_lexicon.mounce entry (2026-07-25 corrected parse)",
          "L2b — the parsed Greek lexicon layer over strong_lexicon.mounce (raw). Split ONLY on "
          "<br> (the source's real line breaks); comma/semicolon within one line are punctuation "
          "inside a sense, not sense separators.")
    _table(conn, "strong_related",
          "one row per (strong, related strong) pair STEP's getInfo returned (fetched 2026-07-25)",
          "L2b — NOT derived from any raw table; fetched live from STEP per full strong code "
          "(lib.stepapi.Step.call2_getInfo, vocabInfos[0].relatedNos) since no raw table captures "
          "this. related_strong is unconstrained — STEP can name a code this app has never "
          "onboarded via raw.detail.")

    # ── columns: strong_meaning_parsed (base-keyed, matches strong_meaning_tree.lemma_key) ─────
    _column(conn, "strong_meaning_parsed", "id", 0, "INTEGER", is_pk=1, use="surrogate key")
    _column(conn, "strong_meaning_parsed", "lemma_key", 1, "TEXT", notnull=1,
           use="the base code this parsed sense belongs to (never a sub-entry letter)",
           source="derived:strong_meaning_tree.lemma_key", filled_by="lexicon.parse")
    _column(conn, "strong_meaning_parsed", "sort", 2, "INTEGER",
           use="order within the source sense tree", source="parsed:strong_meaning_tree.sort",
           filled_by="lexicon.parse")
    _column(conn, "strong_meaning_parsed", "sense_code", 3, "TEXT",
           use="the tree position, e.g. 1a1a) — or the sense_code column value verbatim",
           source="parsed:strong_meaning_tree.sense_code", filled_by="lexicon.parse")
    _column(conn, "strong_meaning_parsed", "gloss", 4, "TEXT", expectation="notblank",
           use="one exploded gloss term, kept whole (no comma/semicolon splitting)",
           source="parsed:strong_meaning_tree.sense_text", filled_by="lexicon.parse")
    _column(conn, "strong_meaning_parsed", "verse_refs", 5, "TEXT",
           use="verse citations scoped to this gloss's own <b> span, semicolon-joined",
           source="parsed:strong_meaning_tree.sense_text", filled_by="lexicon.parse")
    _column(conn, "strong_meaning_parsed", "note", 6, "TEXT",
           use="commentary scoped to this gloss's own segment, not pooled across the row",
           source="parsed:strong_meaning_tree.sense_text", filled_by="lexicon.parse")
    _column(conn, "strong_meaning_parsed", "row_type", 7, "TEXT",
           use="lookup / description / not applicable — lexicon_split_common.classify_row()",
           source="derived:gloss", filled_by="lexicon.parse")
    _column(conn, "strong_meaning_parsed", "deleted", 8, "INTEGER", dflt="0", use="soft delete")

    # ── columns: strong_lsj_parsed (full-code-keyed, matches strong.strongNumber) ──────────────
    _column(conn, "strong_lsj_parsed", "id", 0, "INTEGER", is_pk=1, use="surrogate key")
    _column(conn, "strong_lsj_parsed", "strong", 1, "TEXT", notnull=1, fk="strong.strongNumber",
           use="the full strong code this LSJ sense belongs to",
           source="derived:strong_lexicon.strong", filled_by="lexicon.parse")
    _column(conn, "strong_lsj_parsed", "sense_label", 2, "TEXT",
           use="LSJ sense position, e.g. I / I.2 / II.2.b, or 'headword'",
           source="parsed:strong_lexicon.lsj", filled_by="lexicon.parse")
    _column(conn, "strong_lsj_parsed", "gloss", 3, "TEXT",
           use="the sense's bold-span gloss text, kept whole (no comma splitting); may legitimately "
               "be blank when a block carries only dialect/citation notes",
           source="parsed:strong_lexicon.lsj", filled_by="lexicon.parse")
    _column(conn, "strong_lsj_parsed", "note", 4, "TEXT",
           use="dialect/grammar labels, connective prose — everything in the block but the gloss",
           source="parsed:strong_lexicon.lsj", filled_by="lexicon.parse")
    _column(conn, "strong_lsj_parsed", "row_type", 5, "TEXT",
           use="headword for the entry's own headword row(s), lookup for every sense row",
           source="derived:sense_label", filled_by="lexicon.parse")
    _column(conn, "strong_lsj_parsed", "deleted", 6, "INTEGER", dflt="0", use="soft delete")

    # ── columns: strong_mounce_parsed (full-code-keyed) ─────────────────────────────────────────
    _column(conn, "strong_mounce_parsed", "id", 0, "INTEGER", is_pk=1, use="surrogate key")
    _column(conn, "strong_mounce_parsed", "strong", 1, "TEXT", notnull=1, fk="strong.strongNumber",
           use="the full strong code this Mounce line belongs to",
           source="derived:strong_lexicon.strong", filled_by="lexicon.parse")
    _column(conn, "strong_mounce_parsed", "mounce_parsed", 2, "TEXT",
           use="one <br>-delimited line of Mounce's entry, kept whole (no comma splitting)",
           source="parsed:strong_lexicon.mounce", filled_by="lexicon.parse")
    _column(conn, "strong_mounce_parsed", "row_type", 3, "TEXT",
           use="lookup / description — lexicon_split_common.classify_row()",
           source="derived:mounce_parsed", filled_by="lexicon.parse")
    _column(conn, "strong_mounce_parsed", "deleted", 4, "INTEGER", dflt="0", use="soft delete")

    # ── columns: strong_related (full-code-keyed; related_strong unconstrained) ────────────────
    _column(conn, "strong_related", "id", 0, "INTEGER", is_pk=1, use="surrogate key")
    _column(conn, "strong_related", "strong", 1, "TEXT", notnull=1, fk="strong.strongNumber",
           use="the full code of the SOURCE term STEP was asked about",
           source="fetched:STEP.getInfo", filled_by="lexicon.related")
    _column(conn, "strong_related", "related_strong", 2, "TEXT", notnull=1,
           use="the full code of the RELATED term — may have no strong row of its own yet",
           source="fetched:STEP.getInfo.relatedNos.strongNumber", filled_by="lexicon.related")
    _column(conn, "strong_related", "related_form", 3, "TEXT",
           use="the related term's native-script form",
           source="fetched:STEP.getInfo.relatedNos.matchingForm", filled_by="lexicon.related")
    _column(conn, "strong_related", "related_transliteration", 4, "TEXT",
           use="the related term's transliteration",
           source="fetched:STEP.getInfo.relatedNos.stepTransliteration", filled_by="lexicon.related")
    _column(conn, "strong_related", "related_gloss", 5, "TEXT",
           use="the related term's own short gloss",
           source="fetched:STEP.getInfo.relatedNos.gloss", filled_by="lexicon.related")
    _column(conn, "strong_related", "deleted", 6, "INTEGER", dflt="0", use="soft delete")

    conn.commit()

    # ── physically build the tables FROM cfg_column — no hand-written DDL. Only meaningful
    # against the REAL db file: Cfg always opens its own connection from DB_PATH, so this is
    # skipped in the --dry-run (in-memory) path via the caller's `physical_build` flag. ──────────
    if physical_build:
        cfg = Cfg(DB_PATH)
        built = build_data_tables(cfg, conn)
        for t in ("strong_meaning_parsed", "strong_lsj_parsed", "strong_mounce_parsed", "strong_related"):
            REPORT.append(f"physical table {t!r} " + ("built" if t in built else "NOT in build_data_tables output — check cfg_table"))
        cfg.close()
    else:
        REPORT.append("physical table build SKIPPED (--dry-run) — Cfg always reads DB_PATH directly, "
                      "not the in-memory dry-run copy")

    # ── write grants ─────────────────────────────────────────────────────────────────────────
    _grant(conn, "lexicon.parse", "strong_meaning_parsed")
    _grant(conn, "lexicon.parse", "strong_lsj_parsed")
    _grant(conn, "lexicon.parse", "strong_mounce_parsed")
    _grant(conn, "lexicon.related", "strong_related")

    # ── config_module enum gains 'lexicon' (a new VALUE on an EXISTING group — same bootstrap
    # batch as the rest of this brand-new mechanism, not configmaint.propose'd separately) ──────
    _enum(conn, "config_module", "lexicon", 13)

    # ── work package + steps ─────────────────────────────────────────────────────────────────
    _work_package(conn, "lexicon-parse", "iba/app/ps/Lexicon-Parse.ps1")
    _step(conn, "lexicon-parse", 0, "lexicon.parse", "iba.app.handlers.lexicon:parse",
         "strong_meaning_tree + strong_lexicon -> strong_meaning_parsed/strong_lsj_parsed/"
         "strong_mounce_parsed (corrected 2026-07-25 parse); no network, deterministic, clears "
         "and rebuilds")
    _step(conn, "lexicon-parse", 1, "lexicon.related", "iba.app.handlers.lexicon:related",
         "strong -> strong_related; one live STEP getInfo call per row (relatedNos)")
    _step(conn, "lexicon-parse", 2, "lexicon.validate", "iba.app.handlers.lexicon:validate",
         "read-only coverage + value-quality check across all 4 tables; persists "
         "lexicon.quality_report_path every run; escalates only if findings exist")

    # ── on_fail (mirrors passage.validate's live shape exactly) ────────────────────────────────
    _on_fail(conn, "lexicon.related", "unreachable", "report-stop",
            "STEP is not reachable — lexicon.related cannot fetch relatedNos at all", "terminal")
    _on_fail(conn, "lexicon.validate", "findings-rejected", "report-stop",
            "researcher flagged lexicon-parse quality findings as needing action", "terminal")
    _on_fail(conn, "lexicon.validate", "needs-review", "pause-continue",
            "lexicon-parse coverage/value-quality findings need researcher judgement", "terminal")
    _on_fail(conn, "lexicon.validate", "needs-revision", "report-stop",
            "researcher asked for more specific investigation (see comment)", "terminal")

    # ── report path setting + cfg_report/section/csv ────────────────────────────────────────────
    _setting(conn, "lexicon.quality_report_path", '"iba/app/reports/lexicon-parse.md"',
            "where lexicon.validate persists its findings", "lexicon")
    _report(conn, "lexicon.validate", "Lexicon-parse quality report", "md+csv")
    _report_section(conn, "lexicon.validate", 0, "summary", "## Summary")
    _report_section(conn, "lexicon.validate", 1, "coverage", "## Coverage — strong_lexicon/strong rows with no parsed/related output")
    _report_section(conn, "lexicon.validate", 2, "value_quality", "## Value quality — gloss findings")
    _report_csv(conn, "lexicon.validate", "strong_meaning_parsed", None)
    _report_csv(conn, "lexicon.validate", "strong_lsj_parsed", None)
    _report_csv(conn, "lexicon.validate", "strong_mounce_parsed", None)
    _report_csv(conn, "lexicon.validate", "strong_related", None)

    conn.commit()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    if a.dry_run:
        conn2 = sqlite3.connect(":memory:")
        conn2.row_factory = sqlite3.Row
        conn.backup(conn2)
        register(conn2, physical_build=False)
        conn2.close()
        print("--dry-run (against an in-memory copy, nothing written to iba.db):")
    else:
        register(conn)
        print("lexicon-parsed-layer bootstrap:")

    for line in REPORT:
        print(f"  - {line}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
