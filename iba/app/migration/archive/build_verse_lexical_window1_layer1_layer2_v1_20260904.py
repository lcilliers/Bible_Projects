"""build_verse_lexical_window1_layer1_layer2_v1_20260904.py — ONE-OFF, idempotent.

Escalation #1383 (26 versions, researcher-approved-in-principle A-G across v4-v21, full build
specification filed as `iba/docs/1383-verse-lexical-window1-full-build-specification-v1-20260904.md`
sections (a)-(i)). Researcher instruction, verbatim, this chat turn (Developer Mode session,
2026-09-04): "you will now complete the outstanding build work in escallation 1383 and 1444."

This migration builds the SCHEMA + CONFIG half of the full build spec: 8 new `verse_lexical`
columns (§B.5), 2 new `passage` columns (§B.6), the new `verse_lexical_note` table (§B.7) and
`cfg_lexical_code_class` table (§B.8), 4 new `cfg_enum` groups/28 values (§B.9, incl. the 2 extra
`note_type` values §1446 §2c added at §B.18), 1 new `cfg_setting`-class row (§B.10 — corrected below,
not `cfg_setting`), `lexical.build`'s revised `does` text + 4 new `cfg_step` rows (§B.11-B.12),
19 new `cfg_method_rule` rows (§B.13-B.15 + B.18), 2 new `cfg_write_grant` rows (§B.16), `cfg_utility`
updates (§B.17), 2 new `cfg_report`/`cfg_report_section` rows for the exception report (§G.1), plus
the H0853 role fix (§B.13 h0853-function-word-exception, applied to all 10,521 pre-existing rows)
and a full backfill of the 8 new Layer-1 columns across every already-live `verse_lexical` row
(552,353 at migration time — the whole corpus was already built by an earlier full-Bible pass;
those existing rows would otherwise sit NULL on the new columns until their book's next
`lexical.build` re-run, which is not scheduled by this migration).

**Corrections made against the design document while building it, not silently followed as
written** (each is a small, low-risk implementation-shape choice the document itself left open or
got wrong against the LIVE schema — not a new judgement call; see escalation #1383 resolution for
the full list and reasoning):

1. **§B.10's `passage.max_verses` goes into `cfg_passage`, not `cfg_setting`.** Checked live:
   EVERY existing `passage.*` setting (`max_single_verse_pct`, `max_avg_verses_per_passage`,
   `quality_report_path`, ...) already lives in `cfg_passage`, a dedicated per-module settings
   table (`governance.module.config`) — none are in `cfg_setting`. The design doc's own §B.10
   table header said "cfg_setting" generically; this migration follows the table's OWN established
   sibling convention instead, matching `Cfg.required_module_setting("cfg_passage", ...)`'s
   existing call shape in `handlers/passage.py:validate`.
2. **`passage.genre`/`lexical_complete_at` land at ordinal 20/21, not the doc's assumed 24/25.**
   Checked live `cfg_column` for `(iba, passage)`: only ordinals 0-19 are registered, even though
   the live table DDL has 24 columns (0-23) — 4 columns (`feasibility_note`, `open_decisions_note`,
   `phenomena_complete_at`, `story_summary`) exist in the live schema with NO `cfg_column` row at
   all (a pre-existing registration gap, same class as `config-updated-same-unit-of-work-as-change`
   already names elsewhere — found here, not fixed here; flagged in the escalation resolution as
   its own item, out of this build's scope). This migration's own 2 new columns get real ordinals
   (20, 21) that don't collide with anything live, rather than reproducing the doc's mistaken
   24/25 guess.
3. **`cfg_lexical_code_class` seeded with the 3 evidence-proven lexicons already demonstrated
   live** (negator: 7 codes; connective: 6 codes across 3 classes; divine-name/`party_divine`:
   7 codes) — sourced verbatim from `1383-verse-lexical-window1-method-and-drift-mitigation-v1-
   20260903.md`'s own proven script output (negator/connective) and escalation #1383 v32's
   checked-live divine-name list, not re-derived. `party_human`/`party_angelic` are deliberately
   left EMPTY this pass — item 7 of the build spec's own open-items list names them as "not built,"
   "not a blocker for the rest of this build" — `T4.3.1`/`T4.4.1`/`T4.6.1`/`T4.6.2a`/`T4.6.3a`
   stay correctly `party_kind=NULL`/unanswerable until a future `configmaint.propose` grows those
   two classes.
4. **Open item 5 (where `lexical.enrich`'s code lives) resolved: new module
   `iba/app/lib/lexicalenrich.py`**, not appended to `lib/lexical.py` — keeps the mechanical
   Layer-1 engine and the judgement-bearing Layer-2 engine in separate files matching the
   document's own C.1/C.2 split, and avoids growing `lexical.py` past its current, focused scope.
5. **Open item 6 (which PS surface) resolved: `VerseLexical.ps1` extended**, matching the design
   doc's own concrete assumption in §F.
6. **Open item 1 (audit-trail coverage) resolved: `verse_lexical_note` stays on its own simple
   soft-delete convention, NOT added to `debate_change_detail`.** Matches the design doc's own §E.4
   reasoning verbatim ("no downstream FK dependent yet, unlike phenomenon") — the same reasoning
   that makes `verse_lexical` itself unlogged already.
7. **Open item 8 (a new note_type for "verb triggered-by/impacts") left OPEN, not resolved.** The
   design doc names `chain`/`connective`/`entity_link` as partial coverage and explicitly does not
   force a decision — this migration adds no new note_type for it, matching that.

Everything else follows the full build specification's own row content verbatim — every
`cfg_method_rule`/`cfg_column`/`cfg_enum` row below is transcribed from the document's own tables,
not re-derived.

    python -m iba.app.migration.build_verse_lexical_window1_layer1_layer2_v1_20260904
"""

from __future__ import annotations

import datetime
import sqlite3
import sys

from ..lib.cfg import DB_PATH

_SELF_PATH = ("iba/app/migration/"
              "build_verse_lexical_window1_layer1_layer2_v1_20260904.py")


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _has_column(conn: sqlite3.Connection, table: str, col: str) -> bool:
    return any(r[1] == col for r in conn.execute(f'PRAGMA table_info("{table}")'))


def _has_table(conn: sqlite3.Connection, table: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)).fetchone() is not None


# ═══════════════════════════════════════════════════════════════════════════════════════════
# 1. Schema DDL
# ═══════════════════════════════════════════════════════════════════════════════════════════

_VL_NEW_COLUMNS = [
    # name, sql type (nullable at the SQL level -- cfg_column.notnull documents the intended
    # value-level guarantee once a row is actually built/backfilled; matches passage's own
    # existing additive columns, none of which are SQL-level NOT NULL either)
    ("position", "INTEGER"), ("surface", "TEXT"), ("language", "TEXT"), ("testament", "TEXT"),
    ("is_negator", "INTEGER"), ("narrative_morph", "TEXT"),
    ("gloss_consistent_in_verse", "INTEGER"), ("party_kind", "TEXT"),
]

_PASSAGE_NEW_COLUMNS = [("genre", "TEXT"), ("lexical_complete_at", "TEXT")]

_CREATE_VERSE_LEXICAL_NOTE = '''
CREATE TABLE "verse_lexical_note" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "verse_lexical_id" INTEGER NOT NULL,
  "verse_id" INTEGER NOT NULL,
  "passage_id" INTEGER NOT NULL,
  "note_type" TEXT NOT NULL,
  "resolution_status" TEXT NOT NULL,
  "target_verse_lexical_id" INTEGER,
  "related_verse_lexical_ids" TEXT,
  "value_text" TEXT,
  "evidence_text" TEXT,
  "created_at" TEXT NOT NULL,
  "deleted" INTEGER NOT NULL DEFAULT 0,
  FOREIGN KEY ("verse_lexical_id") REFERENCES "verse_lexical"("id"),
  FOREIGN KEY ("verse_id") REFERENCES "verse"("id"),
  FOREIGN KEY ("passage_id") REFERENCES "passage"("id"),
  FOREIGN KEY ("target_verse_lexical_id") REFERENCES "verse_lexical"("id")
)
'''

_CREATE_CFG_LEXICAL_CODE_CLASS = '''
CREATE TABLE "cfg_lexical_code_class" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "strong_code" TEXT NOT NULL,
  "class" TEXT NOT NULL,
  "evidence_note" TEXT NOT NULL,
  "active" INTEGER NOT NULL DEFAULT 1,
  FOREIGN KEY ("strong_code") REFERENCES "strong"("strongNumber")
)
'''


def _ddl(conn: sqlite3.Connection, report: list[str]) -> None:
    for name, sqltype in _VL_NEW_COLUMNS:
        if _has_column(conn, "verse_lexical", name):
            report.append(f"verse_lexical.{name} already exists — skipped")
        else:
            conn.execute(f'ALTER TABLE "verse_lexical" ADD COLUMN "{name}" {sqltype}')
            report.append(f"verse_lexical.{name} added ({sqltype})")

    for name, sqltype in _PASSAGE_NEW_COLUMNS:
        if _has_column(conn, "passage", name):
            report.append(f"passage.{name} already exists — skipped")
        else:
            conn.execute(f'ALTER TABLE "passage" ADD COLUMN "{name}" {sqltype}')
            report.append(f"passage.{name} added ({sqltype})")

    if _has_table(conn, "verse_lexical_note"):
        report.append("verse_lexical_note table already exists — skipped")
    else:
        conn.execute(_CREATE_VERSE_LEXICAL_NOTE)
        report.append("verse_lexical_note table created")

    if _has_table(conn, "cfg_lexical_code_class"):
        report.append("cfg_lexical_code_class table already exists — skipped")
    else:
        conn.execute(_CREATE_CFG_LEXICAL_CODE_CLASS)
        report.append("cfg_lexical_code_class table created")
    conn.commit()


# ═══════════════════════════════════════════════════════════════════════════════════════════
# 2. cfg_table / cfg_column
# ═══════════════════════════════════════════════════════════════════════════════════════════

def _cfg_table_rows(conn: sqlite3.Connection, report: list[str]) -> None:
    rows = [
        ("verse_lexical_note",
         "one row per (verse_lexical_id, note_type) — the judgement-bearing Layer-2 finding for "
         "one code, one test",
         "Stage 1 Layer 2 output. Written by lexical.enrich, one passage-block at a time. FK to "
         "verse_lexical; passage_id/verse_id denormalized matching phenomenon's own precedent. "
         "NOT read by Window 2's phenomenon/operation writers (no FK link this increment — "
         "Window 2's own future design decision, #1383 v23).",
         "data"),
        ("cfg_lexical_code_class",
         "one row per (strong_code, class) — a code-classification lexicon entry",
         "The single home for every mechanical code-classification lookup this build needs "
         "(negator, connective-type, party-kind lexicons) — governance.rules_must_be_config_"
         "driven; queried by lexical.build/lexicalenrich.py, never hardcoded. Rows are "
         "configmaint.propose-gated, same as every other cfg_* table.",
         "rule"),
    ]
    for name, grain, use, category in rows:
        exists = conn.execute(
            "SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", (name,)).fetchone()
        if exists:
            report.append(f"cfg_table {name!r} already present — skipped")
            continue
        conn.execute(
            "INSERT INTO cfg_table (database, name, grain, use, inactive, category) "
            "VALUES ('iba',?,?,?,0,?)", (name, grain, use, category))
        report.append(f"cfg_table {name!r} added (category={category!r})")


def _cfg_column_rows(conn: sqlite3.Connection, report: list[str]) -> None:
    def _add(table: str, name: str, ordinal: int, coltype: str, notnull: int, dflt, fk,
             use: str, filled_by: str) -> None:
        exists = conn.execute(
            "SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?",
            (table, name)).fetchone()
        if exists:
            report.append(f"cfg_column {table}.{name} already present — skipped")
            return
        conn.execute(
            "INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "
            "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by, inactive) "
            "VALUES ('iba',?,?,?,?,0,?,0,?,?,?,NULL,?,?,0)",
            (table, name, ordinal, coltype, notnull, dflt, fk, use,
             "1383-verse-lexical-window1-full-build-specification-v1-20260904.md", filled_by))
        report.append(f"cfg_column {table}.{name} added (ordinal={ordinal})")

    # verse_lexical, ordinals 12-19 (§B.5)
    _add("verse_lexical", "position", 12, "INTEGER", 1, None, None,
         "span.position, denormalized — mechanical, no judgement", "lexical.build")
    _add("verse_lexical", "surface", 13, "TEXT", 0, None, None,
         "span.surface, denormalized — the literal text at this span, independent of sense "
         "(never confused with resolved_sense)", "lexical.build")
    _add("verse_lexical", "language", 14, "TEXT", 1, None, "strong.language",
         "strong.language, denormalized — 'Hebrew'/'Greek'/'Aramaic'", "lexical.build")
    _add("verse_lexical", "testament", 15, "TEXT", 1, None, None,
         "derived: 'OT' if cfg_book_order.ordinal<=38 else 'NT' (Mal=38/Matt=39 boundary) — "
         "pure ordinal derivation, no reference table", "lexical.build")
    _add("verse_lexical", "is_negator", 16, "INTEGER", 0, None, None,
         "1 if strong is in cfg_lexical_code_class WHERE class='negator' AND active=1, else "
         "NULL (never 0 — NULL means 'not in the lexicon')", "lexical.build")
    _add("verse_lexical", "narrative_morph", 17, "TEXT", 0, None, None,
         "Hebrew wayyiqtol / az+imperfect flag, derived from morph_code pattern — NULL "
         "unconditionally for language != 'Hebrew'", "lexical.build")
    _add("verse_lexical", "gloss_consistent_in_verse", 18, "INTEGER", 1, None, None,
         "1 unless this (strong, morph_code) pair carries >1 distinct resolved_sense value "
         "among this verse's own rows — mechanical data-quality check", "lexical.build")
    _add("verse_lexical", "party_kind", 19, "TEXT", 0, None, None,
         "'divine'/'human'/'non_human' — set ONLY when this code IS ITSELF a name "
         "(cfg_lexical_code_class class IN party_divine/party_human/party_angelic); a "
         "pronoun's own party_kind is NOT stored here, it derives via its entity_link note's "
         "target_verse_lexical_id (two-hop join, Window 2's own future join)", "lexical.build")

    # passage, ordinals 20-21 (§B.6, ordinal corrected — see module docstring §2)
    _add("passage", "genre", 20, "TEXT", 0, None, None,
         "manual, set as part of lexical.enrich's own first move for this passage; no "
         "controlled vocabulary yet — free text this round. NOT ported from "
         "bible_research.db.verse.genre (book-level, confirmed too coarse).", "lexical.enrich")
    _add("passage", "lexical_complete_at", 21, "TEXT", 0, None, None,
         "NULL until every verse in this passage has a verse_lexical row for every code AND "
         "(for judgement-bearing codes) a verse_lexical_note disposition — set only by an "
         "explicit control check (mirrors phenomena_complete_at)", "lexical.enrich")

    # verse_lexical_note, full table (§B.7)
    vln_cols = [
        ("id", 0, "INTEGER PK", 1, None, "surrogate PK"),
        ("verse_lexical_id", 1, "INTEGER", 1, "verse_lexical.id", "the code-row this note is about"),
        ("verse_id", 2, "INTEGER", 1, "verse.id", "denormalized, matches phenomenon's own precedent"),
        ("passage_id", 3, "INTEGER", 1, "passage.id", "denormalized, matches phenomenon's own precedent"),
        ("note_type", 4, "TEXT", 1, None,
         "cfg_enum note_type — idiom / pronoun_resolution / noun_relational / noun_severity / "
         "chain / connective / related_word / polarity / entity_link / inert / "
         "structural_pattern / recurrence_role_shift / cross_lemma_shared_gloss"),
        ("resolution_status", 5, "TEXT", 1, None,
         "cfg_enum resolution_status — resolved / unresolved / unclassified / "
         "not_supported_this_language / checked_empty"),
        ("target_verse_lexical_id", 6, "INTEGER", 0, "verse_lexical.id",
         "same-verse OR cross-verse (within the loaded passage-block) resolution target "
         "(pronoun/noun/entity-link), NULL if unresolved"),
        ("related_verse_lexical_ids", 7, "TEXT", 0, None,
         "JSON array of ids — structural_pattern/recurrence_role_shift rows only"),
        ("value_text", 8, "TEXT", 0, None,
         "the finding itself, free text — content shape varies too much by note_type for typed "
         "columns yet"),
        ("evidence_text", 9, "TEXT", 0, None,
         "what in the verse's own data supports it (morph marker, related-word pull, etc.)"),
        ("created_at", 10, "TEXT", 1, None, "ISO-8601 UTC"),
        ("deleted", 11, "INTEGER", 1, None,
         "version-aware soft-delete, same convention as every other iba.db table"),
    ]
    for name, ordinal, coltype, notnull, fk, use in vln_cols:
        _add("verse_lexical_note", name, ordinal, coltype, notnull, None, fk, use, "lexical.enrich")

    # cfg_lexical_code_class, full table (§B.8)
    clc_cols = [
        ("id", 0, "INTEGER PK", 1, None, "surrogate PK"),
        ("strong_code", 1, "TEXT", 1, "strong.strongNumber", "the code this classification applies to"),
        ("class", 2, "TEXT", 1, None,
         "cfg_enum lexical_code_class — negator / connective_causal / connective_coordinating / "
         "connective_purpose / party_divine / party_human / party_angelic"),
        ("evidence_note", 3, "TEXT", 1, None,
         "why this code is classed this way — traceable-by-construction, never a bare assertion"),
        ("active", 4, "INTEGER", 1, None,
         "1 = live lookup row; 0 = retired classification, kept for history"),
    ]
    for name, ordinal, coltype, notnull, fk, use in clc_cols:
        _add("cfg_lexical_code_class", name, ordinal, coltype, notnull, None, fk, use,
             "configmaint.propose")
    conn.commit()


# ═══════════════════════════════════════════════════════════════════════════════════════════
# 3. cfg_enum (§B.9, incl. §B.18's 2 extra note_type values)
# ═══════════════════════════════════════════════════════════════════════════════════════════

_ENUM_ROWS = [
    ("note_type", "idiom", 0), ("note_type", "pronoun_resolution", 1),
    ("note_type", "noun_relational", 2), ("note_type", "noun_severity", 3),
    ("note_type", "chain", 4), ("note_type", "connective", 5),
    ("note_type", "related_word", 6), ("note_type", "polarity", 7),
    ("note_type", "entity_link", 8), ("note_type", "inert", 9),
    ("note_type", "structural_pattern", 10), ("note_type", "recurrence_role_shift", 11),
    ("note_type", "cross_lemma_shared_gloss", 12),
    ("resolution_status", "resolved", 0), ("resolution_status", "unresolved", 1),
    ("resolution_status", "unclassified", 2),
    ("resolution_status", "not_supported_this_language", 3),
    ("resolution_status", "checked_empty", 4),
    ("lexical_code_class", "negator", 0), ("lexical_code_class", "connective_causal", 1),
    ("lexical_code_class", "connective_coordinating", 2),
    ("lexical_code_class", "connective_purpose", 3),
    ("lexical_code_class", "party_divine", 4), ("lexical_code_class", "party_human", 5),
    ("lexical_code_class", "party_angelic", 6),
    ("party_kind", "divine", 0), ("party_kind", "human", 1), ("party_kind", "non_human", 2),
]


def _cfg_enum_rows(conn: sqlite3.Connection, report: list[str]) -> None:
    for name, value, ordinal in _ENUM_ROWS:
        exists = conn.execute(
            "SELECT 1 FROM cfg_enum WHERE name=? AND value=?", (name, value)).fetchone()
        if exists:
            report.append(f"cfg_enum {name}={value!r} already present — skipped")
            continue
        conn.execute("INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)",
                    (name, value, ordinal))
        report.append(f"cfg_enum {name}={value!r} added (ordinal={ordinal})")
    conn.commit()


# ═══════════════════════════════════════════════════════════════════════════════════════════
# 4. cfg_passage setting (§B.10, corrected home — see module docstring §1)
# ═══════════════════════════════════════════════════════════════════════════════════════════

def _cfg_passage_setting(conn: sqlite3.Connection, report: list[str]) -> None:
    exists = conn.execute(
        "SELECT 1 FROM cfg_passage WHERE key='passage.max_verses'").fetchone()
    if exists:
        report.append("cfg_passage passage.max_verses already present — skipped")
        return
    conn.execute(
        "INSERT INTO cfg_passage (key, value, use, inactive) VALUES (?,?,?,0)",
        ("passage.max_verses", "20",
         "hard ceiling decided #1379 v7 — a passage/reading-block payload exceeding this many "
         "verses is refused before any write (too-many-verses), never silently truncated or "
         "auto-split. Read via required_module_setting('cfg_passage', 'passage.max_verses'), "
         "same call shape as every other cfg_passage row."))
    report.append("cfg_passage passage.max_verses added (20)")
    conn.commit()


# ═══════════════════════════════════════════════════════════════════════════════════════════
# 5. cfg_step (§B.11-B.12)
# ═══════════════════════════════════════════════════════════════════════════════════════════

def _cfg_step_rows(conn: sqlite3.Connection, report: list[str]) -> None:
    # B.11 — revise lexical.build's own `does` text (append, not replace)
    row = conn.execute(
        "SELECT does FROM cfg_step WHERE work_package='verse-lexical' AND step='lexical.build'"
    ).fetchone()
    addition = (
        "; from this build onward, also denormalizes position/surface/language/testament and "
        "computes is_negator/narrative_morph/gloss_consistent_in_verse/party_kind via "
        "cfg_lexical_code_class lookups, unconditionally for every row, no selection "
        "(method-and-drift-mitigation doc §2 Layer 1). Also applies the H0853 classify_role "
        "exception (design doc §4).")
    if row and addition not in (row["does"] or ""):
        conn.execute(
            "UPDATE cfg_step SET does=? WHERE work_package='verse-lexical' AND step='lexical.build'",
            ((row["does"] or "") + addition,))
        report.append("cfg_step lexical.build does-text revised")
    else:
        report.append("cfg_step lexical.build does-text already revised or row missing — skipped")

    new_steps = [
        ("verse-lexical", 2, "lexical.enrich", "iba.app.handlers.lexical:enrich", "passage",
         "Stage 1 Layer 2 — JSON-payload-driven, one passage-block at a time (≤20 verses). "
         "Writes verse_lexical_note rows and passage.genre; sets passage.lexical_complete_at "
         "once every applicable code in the block has a disposition. Requires lexical.build to "
         "have already run for every verse in the block.", "operations"),
        ("build-passages", 1, "passage.suggest_boundary",
         "iba.app.handlers.passage:suggest_boundary", "verse",
         "Proposes the next candidate passage boundary (≤20 verses) from the next un-passaged "
         "verse, using cheap mechanical proxy signals only (narrative_morph density, legacy "
         "book-level genre tag, paragraph/chapter markers) — NOT a genre determination. Output "
         "is a proposal for the PS entry point to surface for researcher confirm/adjust; never "
         "auto-registers.", "operations"),
        ("verse-lexical", 3, "report.lexical_exceptions",
         "iba.app.handlers.reports:lexical_exceptions_report", "passage",
         "Per-run exception report — every unresolved/unclassified/checked_empty/UNCLASSIFIED-"
         "connective disposition and every genuine judgement call from the most recent "
         "lexical.enrich run for this passage, laid out for researcher review. Read-only "
         "against verse_lexical/verse_lexical_note, never an independent write.", "operations"),
        ("verse-lexical", 4, "report.lexical_extract",
         "iba.app.handlers.reports:lexical_extract", "none",
         "Multi-filter JSON extract over verse_lexical/verse_lexical_note — passage/verse/"
         "surface/strong/lemma filters, each accepting a list or range. Read-only, JSON output, "
         "feeds Phase 2 (Stage 2) input assembly.", "reports"),
    ]
    for wp, ordinal, step, handler, scope, does, kind in new_steps:
        exists = conn.execute(
            "SELECT 1 FROM cfg_step WHERE work_package=? AND step=?", (wp, step)).fetchone()
        if exists:
            report.append(f"cfg_step {step!r} already present — skipped")
            continue
        conn.execute(
            "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
            "inactive, kind) VALUES (?,?,?,?,?,?,0,?)",
            (wp, ordinal, step, handler, scope, does, kind))
        report.append(f"cfg_step {step!r} added ({wp}, ordinal={ordinal}, kind={kind})")
    conn.commit()


# ═══════════════════════════════════════════════════════════════════════════════════════════
# 6. cfg_method_rule (§B.13-B.15 + B.18)
# ═══════════════════════════════════════════════════════════════════════════════════════════

_METHOD_RULES = [
    # step, rule_key, rule_text, source_doc, ordinal
    ("lexical.build", "language-testament-derivation",
     "language and testament are denormalized onto verse_lexical unconditionally, at build "
     "time — language = strong.language (verbatim copy); testament = 'OT' if "
     "cfg_book_order.ordinal<=38 else 'NT'. Both mechanical, no judgement, run on every row.",
     "design doc §5.1/§3.E", 0),
    ("lexical.build", "h0853-function-word-exception",
     "H0853 (the Hebrew direct-object marker, stepGloss='[Obj.]') is classified role='function' "
     "— classify_role's H9xxx regex gets an explicit, evidence-commented exception set "
     "(starting with H0853), not a widened range.", "design doc §4", 1),
    ("lexical.build", "lexical-code-class-lookup-not-hardcoded",
     "Every code-classification lexicon (negator, connective-type, party_kind's divine/human/"
     "angelic classes) is a queried row in cfg_lexical_code_class, never a hardcoded list/dict "
     "in a handler. A code absent from the table is reported UNCLASSIFIED/NULL — never guessed, "
     "never silently defaulted.", "catalogue-finishing doc §4; governance.rules_must_be_config_driven", 2),
    ("lexical.build", "mechanical-columns-run-on-every-code-no-selection",
     "position/surface/language/testament/is_negator/narrative_morph/gloss_consistent_in_verse/"
     "party_kind are computed for every verse_lexical row, unconditionally — none is selectively "
     "computed based on whether a code 'looks interesting.' Direct structural fix for the "
     "selective-attention drift found live 2026-09-03 (Gal 5:16-17, the G1063/G1937-G1939 misses).",
     "method-and-drift-mitigation doc §1-2", 3),
    ("lexical.build", "narrative-morph-hebrew-only",
     "narrative_morph is derived only for language='Hebrew' rows; Greek rows get NULL "
     "unconditionally — no guessed Greek chain-test equivalent exists yet.", "design doc §3.G", 4),

    ("lexical.enrich", "one-integrated-read-genre-first",
     "Genre/language/testament are this read's own first move for the block, not a separate "
     "prior pass. One integrated technical read; the only split is Layer1-mechanical/"
     "Layer2-judgement within it.", "checklist doc correction 2026-09-02; design doc §1", 0),
    ("lexical.enrich", "twenty-verse-cap",
     "A payload exceeding 20 verses is refused (too-many-verses) before any row is written — "
     "never silently split or truncated.", "#1379 v7", 1),
    ("lexical.enrich", "unresolved-not-guessed",
     "Where a test cannot resolve from the current block's own data, resolution_status="
     "'unresolved' is recorded explicitly — never guessed, never resolved by reaching outside "
     "the block. Genuine cross-verse cruxes stay Window 2's job.", "checklist doc; design doc §1", 2),
    ("lexical.enrich", "related-word-pull-total-sorting-manual",
     "Every content-role code gets a full, unconditional strong_related pull as "
     "note_type='related_word' rows. The pull is mechanical/total; same-concept-vs-coincidental "
     "sorting is Layer 2, resolution_status='unclassified' until sorted.",
     "checklist doc; design doc §3.F", 3),
    ("lexical.enrich", "genre-manual-this-round",
     "passage.genre is set manually as part of the same integrated read — not auto-derived, "
     "not ported from bible_research.db.verse.genre.", "design doc §3.D", 4),
    ("lexical.enrich", "structural-pattern-detect-only",
     "A structural_pattern note records that a rhetorical relationship exists and which spans "
     "— detection only. Interpreting what it means is Stage 2's job, out of this table's scope "
     "entirely.", "capture-design doc §6; #1443", 5),
    ("lexical.enrich", "phase-separation-layer1-before-layer2",
     "Layer 1's complete mechanical output for every code in the block must exist before any "
     "Layer 2 note is written for any code in it — mirrors phenomenon.set/phase-separation, "
     "rescoped to Layer1/Layer2 within one block.", "method-and-drift-mitigation doc", 6),
    ("lexical.enrich", "completeness-by-code-count",
     "A block's Layer-2 pass is complete only when every non-inert code has ≥1 note row (a "
     "finding, or an explicit checked_empty/not_supported_this_language/unresolved) — a known, "
     "checkable total, not trust. Mirrors phenomenon.set/control-total.",
     "method-and-drift-mitigation doc §2; capture-design doc §4", 7),
    ("lexical.enrich", "recurrence-role-shift-is-judgement-not-mechanical",
     "A recurrence_role_shift note is written only when the same-code recurrence's role change "
     "is judged rhetorically significant (e.g. contributes to the verse's own argument or "
     "imagery), not for every mechanical repetition of a code — plain repeated function words "
     "(e.g. repeated H9003 prepositional prefixes) never qualify. resolution_status is "
     "'resolved' when the shift is judged significant, 'checked_empty' when the same code "
     "recurs with no meaningful role shift (recorded, not silently skipped).",
     "1446 §2c; validation-applied doc, John 1:1/1:4", 8),
    ("lexical.enrich", "cross-lemma-shared-gloss-requires-related-word-check",
     "A cross_lemma_shared_gloss note may only be written after the related-word pull for both "
     "codes has been checked (confirming they are genuinely distinct lemmas, not a data-entry "
     "duplicate) — mirrors the discipline that caught G1937/G1939 in the first place.",
     "1446 §2c; #1383 v9 calibration doc", 9),
    ("lexical.enrich", "related-word-sorting-language-aware",
     "Sorting a related_word pull into same-concept/genuine-relative/coincidental is judged "
     "differently by language: Hebrew families skew toward root-sharing; Greek families skew "
     "toward compound-morphology relationships. The sorting judgement must account for this "
     "difference explicitly, not apply one shape's heuristic to the other language's data.",
     "1446 §2c; validation-applied doc, Deut 6:5 (H3824) vs. John 1:1 (G3056/G2316)", 10),
    ("lexical.enrich", "boundary-ambiguity-recorded-honestly",
     "Where a passage/reading-block's own extent is genuinely ambiguous, the ambiguity is "
     "recorded explicitly as a judgement call on record — never silently resolved either way "
     "by picking the more convenient boundary.",
     "1446 §2c; validation-applied doc, Passage 2 summary", 11),

    ("passage.suggest_boundary", "proxy-signals-not-genre-determination",
     "The suggester proposes a candidate end-point using cheap mechanical proxy signals only "
     "(narrative_morph density, legacy book-level genre tag, paragraph/chapter markers) — "
     "explicitly NOT the real genre determination, which still happens as lexical.enrich's own "
     "first move once the passage is confirmed. No circularity.", "design doc §5.4", 0),
    ("passage.suggest_boundary", "human-confirmation-gate",
     "Suggester proposes → researcher confirms/adjusts → passage.build registers unchanged from "
     "its own existing mechanism. The suggester never auto-registers.", "design doc §5.4", 1),
]


def _cfg_method_rule_rows(conn: sqlite3.Connection, report: list[str]) -> None:
    for step, rule_key, rule_text, source_doc, ordinal in _METHOD_RULES:
        exists = conn.execute(
            "SELECT 1 FROM cfg_method_rule WHERE step=? AND rule_key=?",
            (step, rule_key)).fetchone()
        if exists:
            report.append(f"cfg_method_rule {step}/{rule_key} already present — skipped")
            continue
        conn.execute(
            "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, enforced_by, "
            "ordinal, active) VALUES (?,?,?,?,NULL,?,1)",
            (step, rule_key, rule_text, source_doc, ordinal))
        report.append(f"cfg_method_rule {step}/{rule_key} added")
    conn.commit()


# ═══════════════════════════════════════════════════════════════════════════════════════════
# 7. cfg_write_grant (§B.16) + cfg_utility (§B.17)
# ═══════════════════════════════════════════════════════════════════════════════════════════

def _cfg_write_grant_rows(conn: sqlite3.Connection, report: list[str]) -> None:
    for writer, table in (("lexical.enrich", "verse_lexical_note"), ("lexical.enrich", "passage")):
        exists = conn.execute(
            "SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'",
            (writer, table)).fetchone()
        if exists:
            report.append(f"cfg_write_grant ({writer!r}, {table!r}) already present — skipped")
            continue
        conn.execute(
            "INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
            "VALUES (?,?,'iba',0)", (writer, table))
        report.append(f"cfg_write_grant ({writer!r}, {table!r}) added")
    conn.commit()


def _cfg_utility_rows(conn: sqlite3.Connection, report: list[str]) -> None:
    row = conn.execute("SELECT purpose FROM cfg_utility WHERE file_path='iba/app/lib/lexical.py'"
                       ).fetchone()
    addition = (" Extended 2026-09-04 (escalation #1383): also computes position/surface/"
               "language/testament/is_negator/narrative_morph/gloss_consistent_in_verse/"
               "party_kind and applies the H0853 role exception.")
    if row and addition not in (row["purpose"] or ""):
        conn.execute("UPDATE cfg_utility SET purpose=? WHERE file_path='iba/app/lib/lexical.py'",
                    ((row["purpose"] or "") + addition,))
        report.append("cfg_utility iba/app/lib/lexical.py purpose text extended")
    else:
        report.append("cfg_utility iba/app/lib/lexical.py already extended or missing — skipped")

    new_utils = [
        ("lexicalenrich", "iba/app/lib/lexicalenrich.py",
         "Stage 1 Layer 2 engine: verse_lexical_note capture + passage.genre/"
         "lexical_complete_at, JSON-payload-driven. Escalation #1383."),
    ]
    for module, path, purpose in new_utils:
        exists = conn.execute("SELECT 1 FROM cfg_utility WHERE file_path=?", (path,)).fetchone()
        if exists:
            report.append(f"cfg_utility {path!r} already present — skipped")
            continue
        conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt) "
            "VALUES (?,?,?,0,0)", (module, path, purpose))
        report.append(f"cfg_utility {path!r} added")
    conn.commit()


# ═══════════════════════════════════════════════════════════════════════════════════════════
# 8. cfg_report / cfg_report_section for report.lexical_exceptions (§G.1)
# ═══════════════════════════════════════════════════════════════════════════════════════════

def _cfg_report_rows(conn: sqlite3.Connection, report: list[str]) -> None:
    exists = conn.execute(
        "SELECT 1 FROM cfg_report WHERE step='report.lexical_exceptions'").fetchone()
    if not exists:
        conn.execute(
            "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
            "naming_scheme, archive_dir, inactive) VALUES (?,?,1,NULL,'md','stable','archive',0)",
            ("report.lexical_exceptions", "{book} {range} — lexical.enrich exception report"))
        report.append("cfg_report report.lexical_exceptions added")
    else:
        report.append("cfg_report report.lexical_exceptions already present — skipped")

    sections = [
        ("layer1_tally", "## Layer 1 tally (mechanical, complete enumeration)",
         "Layer 1 tally (mechanical)", 0),
        ("layer2_dispositions", "## Layer 2 dispositions (judgement, complete against Layer 1's total)",
         "Layer 2 dispositions", 1),
        ("judgement_calls", "## Judgement calls made this run, each labelled",
         "Judgement calls", 2),
    ]
    for key, heading, toc_label, ordinal in sections:
        exists = conn.execute(
            "SELECT 1 FROM cfg_report_section WHERE step='report.lexical_exceptions' AND "
            "section_key=?", (key,)).fetchone()
        if exists:
            report.append(f"cfg_report_section report.lexical_exceptions/{key} already present — skipped")
            continue
        conn.execute(
            "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, toc_label, "
            "include, inactive) VALUES ('report.lexical_exceptions',?,?,?,?,1,0)",
            (ordinal, key, heading, toc_label))
        report.append(f"cfg_report_section report.lexical_exceptions/{key} added")

    # report.lexical_extract's own persisted-path settings (governance.reports_must_persist) —
    # JSON output, not markdown, so no cfg_report/render_scaffold row (that machinery is
    # markdown-specific) — same "config-defined path, not a hardcoded one" discipline via
    # cfg_setting instead, matching word.export/prose.extract's own JSON-output precedent
    # (design doc §G.2).
    for key, value, use in (
        ("report.lexical_extract_output_dir", "_analytics/lexical-extracts",
         "output directory for report.lexical_extract's JSON output (governance.reports_must_persist)"),
        ("report.lexical_extract_output_pattern", "lexical-extract-{run_id}.json",
         "filename pattern for report.lexical_extract's JSON output"),
    ):
        exists = conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone()
        if exists:
            report.append(f"cfg_setting {key} already present — skipped")
            continue
        conn.execute(
            "INSERT INTO cfg_setting (key, value, use, module, inactive) VALUES (?,?,?,?,0)",
            (key, f'"{value}"', use, "report"))
        report.append(f"cfg_setting {key} added")
    conn.commit()


# ═══════════════════════════════════════════════════════════════════════════════════════════
# 9. cfg_lexical_code_class seed content (§corrections item 3 above)
# ═══════════════════════════════════════════════════════════════════════════════════════════

_NEGATOR_EVIDENCE = ("proven live, method-and-drift-mitigation doc §2 (script run against Gal "
                     "5:16-17, unmodified iba.db, read-only) — NEGATOR_LEXICON.")
_CONNECTIVE_EVIDENCE = ("proven live, method-and-drift-mitigation doc §2 (script run against Gal "
                        "5:16-17) — CONNECTIVE_LEXICON.")
_DIVINE_EVIDENCE = ("checked live, escalation #1383 v32 — distinguishable from lowercase generic "
                    "lord/god codes.")

_LEXICON_SEED = (
    [("negator", c, _NEGATOR_EVIDENCE) for c in
     ("H0408", "H3808", "H3809", "G3756", "G3361", "G3760", "G3761")]
    + [("connective_causal", c, _CONNECTIVE_EVIDENCE) for c in ("H3588A", "G1063")]
    + [("connective_coordinating", c, _CONNECTIVE_EVIDENCE) for c in ("H9002", "G2532", "G1161")]
    + [("connective_purpose", c, _CONNECTIVE_EVIDENCE) for c in ("G2443",)]
    + [("party_divine", c, _DIVINE_EVIDENCE) for c in
       ("H0430", "H0410", "H3068", "G2316", "G2962", "G5547", "G2424")]
)


def _seed_lexicon(conn: sqlite3.Connection, report: list[str]) -> None:
    for cls, code, evidence in _LEXICON_SEED:
        exists = conn.execute(
            "SELECT 1 FROM cfg_lexical_code_class WHERE strong_code=? AND class=?",
            (code, cls)).fetchone()
        if exists:
            report.append(f"cfg_lexical_code_class {code}/{cls} already present — skipped")
            continue
        conn.execute(
            "INSERT INTO cfg_lexical_code_class (strong_code, class, evidence_note, active) "
            "VALUES (?,?,?,1)", (code, cls, evidence))
        report.append(f"cfg_lexical_code_class {code}/{cls} added")
    conn.commit()


# ═══════════════════════════════════════════════════════════════════════════════════════════
# 10. H0853 role fix + full Layer-1 backfill of existing live verse_lexical rows
# ═══════════════════════════════════════════════════════════════════════════════════════════

def _fix_h0853_role(conn: sqlite3.Connection, report: list[str]) -> None:
    n = conn.execute(
        "SELECT COUNT(*) FROM verse_lexical WHERE strong='H0853' AND role='content' AND deleted=0"
    ).fetchone()[0]
    if n == 0:
        report.append("H0853 role fix: no content-role H0853 rows remain — already applied")
        return
    conn.execute("UPDATE verse_lexical SET role='function' WHERE strong='H0853' AND deleted=0")
    conn.commit()
    report.append(f"H0853 role fix: {n} row(s) role 'content' -> 'function'")


def _backfill_layer1(conn: sqlite3.Connection, report: list[str]) -> None:
    """Fills the 8 new columns for every existing live verse_lexical row, so already-built books
    (the whole corpus, per module docstring) don't sit NULL until their next lexical.build
    re-run. Skips rows that already have `position` populated (idempotent — position is the
    cheapest non-NULL indicator that this backfill already ran for a row; every field is set
    together in one UPDATE per row-class below, so partial-fill can't happen)."""
    already = conn.execute(
        "SELECT COUNT(*) FROM verse_lexical WHERE deleted=0 AND position IS NOT NULL"
    ).fetchone()[0]
    total = conn.execute("SELECT COUNT(*) FROM verse_lexical WHERE deleted=0").fetchone()[0]
    if already == total and total > 0:
        report.append(f"Layer-1 backfill: all {total} live row(s) already backfilled — skipped")
        return

    # position/surface — straight copy from span
    conn.execute('''
        UPDATE verse_lexical SET
          position = (SELECT s.position FROM span s WHERE s.id = verse_lexical.span_id),
          surface  = (SELECT s.surface  FROM span s WHERE s.id = verse_lexical.span_id)
        WHERE deleted=0 AND position IS NULL
    ''')
    # language — straight copy from strong
    conn.execute('''
        UPDATE verse_lexical SET
          language = (SELECT st.language FROM strong st WHERE st.strongNumber = verse_lexical.strong)
        WHERE deleted=0 AND language IS NULL AND strong IS NOT NULL
    ''')
    # testament — book-ordinal derivation via verse.osisId's book prefix -> cfg_book_order
    conn.execute('''
        UPDATE verse_lexical SET
          testament = CASE WHEN (
            SELECT bo.ordinal FROM verse v JOIN cfg_book_order bo
              ON bo.book = SUBSTR(v.osisId, 1, INSTR(v.osisId, '.') - 1)
            WHERE v.id = verse_lexical.verse_id
          ) <= 38 THEN 'OT' ELSE 'NT' END
        WHERE deleted=0 AND testament IS NULL
          AND EXISTS (SELECT 1 FROM verse v JOIN cfg_book_order bo
                      ON bo.book = SUBSTR(v.osisId, 1, INSTR(v.osisId, '.') - 1)
                      WHERE v.id = verse_lexical.verse_id)
    ''')
    # is_negator / party_kind — cfg_lexical_code_class lookups, matched by BASE code (a live
    # `strong` value carries an optional single trailing variant letter — H3068G, H0430G — per
    # versespanmeaningreport._BASE_RE_FALLBACK, `^([HG]\d+)([A-Z]?)$`; the seeded lexicon rows are
    # bare base codes, so the match must strip that one optional letter, not compare exact
    # strings — caught live testing this migration against Exod.15.2's H3068G/H0430G, both of
    # which silently failed to match under an exact IN() comparison).
    conn.execute('''
        UPDATE verse_lexical SET is_negator = 1
        WHERE deleted=0 AND is_negator IS NULL AND EXISTS (
          SELECT 1 FROM cfg_lexical_code_class c WHERE c.class='negator' AND c.active=1
            AND (verse_lexical.strong = c.strong_code
                 OR verse_lexical.strong GLOB (c.strong_code || '[A-Z]')))
    ''')
    conn.execute('''
        UPDATE verse_lexical SET party_kind = 'divine'
        WHERE deleted=0 AND party_kind IS NULL AND EXISTS (
          SELECT 1 FROM cfg_lexical_code_class c WHERE c.class='party_divine' AND c.active=1
            AND (verse_lexical.strong = c.strong_code
                 OR verse_lexical.strong GLOB (c.strong_code || '[A-Z]')))
    ''')
    conn.execute('''
        UPDATE verse_lexical SET party_kind = 'human'
        WHERE deleted=0 AND party_kind IS NULL AND EXISTS (
          SELECT 1 FROM cfg_lexical_code_class c WHERE c.class='party_human' AND c.active=1
            AND (verse_lexical.strong = c.strong_code
                 OR verse_lexical.strong GLOB (c.strong_code || '[A-Z]')))
    ''')
    conn.execute('''
        UPDATE verse_lexical SET party_kind = 'non_human'
        WHERE deleted=0 AND party_kind IS NULL AND EXISTS (
          SELECT 1 FROM cfg_lexical_code_class c WHERE c.class='party_angelic' AND c.active=1
            AND (verse_lexical.strong = c.strong_code
                 OR verse_lexical.strong GLOB (c.strong_code || '[A-Z]')))
    ''')
    # narrative_morph — Hebrew only. wayyiqtol: this row's own morph_code is 'HV<stem><TAM>...'
    # with TAM='w' at 0-based index 3 (i.e. 2 fixed chars 'HV' + 1 stem-letter wildcard + 'w').
    # az_imperfect_opening: same shape with TAM='i' (imperfect) AND some OTHER code in the SAME
    # span has a base strong of H0227 ("az"/"then") — verified live against Exod.15.1 (span
    # position 3: H7891 HVqi3ms + H0227A HD, same span_id). LIKE patterns corrected to a single
    # stem-letter wildcard (an earlier version of this migration had one wildcard too many —
    # 'HV__w%' checks index 4, not index 3 — caught live: it silently matched nothing against
    # Exod.14.31/15.1's own already-hand-verified wayyiqtol cases).
    conn.execute('''
        UPDATE verse_lexical SET narrative_morph = 'wayyiqtol'
        WHERE deleted=0 AND narrative_morph IS NULL AND language='Hebrew'
          AND morph_code LIKE 'HV_w%'
    ''')
    conn.execute('''
        UPDATE verse_lexical SET narrative_morph = 'az_imperfect_opening'
        WHERE deleted=0 AND narrative_morph IS NULL AND language='Hebrew'
          AND morph_code LIKE 'HV_i%'
          AND EXISTS (SELECT 1 FROM verse_lexical sib
                      WHERE sib.span_id = verse_lexical.span_id AND sib.deleted=0
                        AND sib.strong LIKE 'H0227%')
    ''')
    conn.execute('''
        UPDATE verse_lexical SET narrative_morph = NULL
        WHERE deleted=0 AND language != 'Hebrew' AND narrative_morph IS NOT NULL
    ''')
    # gloss_consistent_in_verse — 0 where the same (verse_id, strong, morph_code) triple carries
    # more than one distinct resolved_sense among this verse's own live rows; 1 everywhere else.
    conn.execute('''
        UPDATE verse_lexical SET gloss_consistent_in_verse = 1
        WHERE deleted=0
    ''')
    conn.execute('''
        UPDATE verse_lexical SET gloss_consistent_in_verse = 0
        WHERE deleted=0 AND (verse_id, strong, morph_code) IN (
          SELECT verse_id, strong, morph_code FROM verse_lexical
          WHERE deleted=0 AND strong IS NOT NULL AND morph_code IS NOT NULL
          GROUP BY verse_id, strong, morph_code
          HAVING COUNT(DISTINCT resolved_sense) > 1
        )
    ''')
    conn.commit()
    now_total = conn.execute(
        "SELECT COUNT(*) FROM verse_lexical WHERE deleted=0 AND position IS NOT NULL").fetchone()[0]
    report.append(f"Layer-1 backfill: {now_total}/{total} live row(s) now carry the 8 new columns")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    report: list[str] = []

    _ddl(conn, report)
    _cfg_table_rows(conn, report)
    _cfg_column_rows(conn, report)
    _cfg_enum_rows(conn, report)
    _cfg_passage_setting(conn, report)
    _cfg_step_rows(conn, report)
    _cfg_method_rule_rows(conn, report)
    _cfg_write_grant_rows(conn, report)
    _cfg_utility_rows(conn, report)
    _cfg_report_rows(conn, report)
    _seed_lexicon(conn, report)
    _fix_h0853_role(conn, report)
    _backfill_layer1(conn, report)

    if not conn.execute("SELECT 1 FROM cfg_utility WHERE file_path=?", (_SELF_PATH,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt) "
            "VALUES (?,?,?,1,0)",
            ("build_verse_lexical_window1_layer1_layer2_v1_20260904", _SELF_PATH,
             "ONE-OFF migration, escalation #1383 -- builds the verse_lexical Window-1 Layer-1/"
             "Layer-2 schema+config (verse_lexical +8 cols, passage +2 cols, verse_lexical_note "
             "and cfg_lexical_code_class new tables, cfg_enum/cfg_method_rule/cfg_step/"
             "cfg_write_grant/cfg_report rows), seeds the negator/connective/party_divine "
             "lexicon, fixes the H0853 role bug, and backfills the 8 new columns across the "
             "whole existing corpus. inactive=1 once applied -- a one-off, not a reusable "
             "routine."))
        report.append(f"cfg_utility (self) {_SELF_PATH!r} added")
    else:
        report.append(f"cfg_utility (self) {_SELF_PATH!r} already present")
    conn.commit()
    conn.close()

    print("verse_lexical Window 1 Layer 1/Layer 2 build:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
