"""narrative_claim_register_config_v1_20261013.py -- escalation #2110, build steps 1 and 2: the
config and the schema of the narrative claim register in iba.db.

Specification (approved 2026-10-13, round 5):
  _analytics/essay/spirit_soul_body/wa-essay-narrative-record-db-specification-v1-20261013.md
  (sec3 the tables, sec4 config first, sec5 editing and the behaviour rule, sec8 published files).
Test plan: iba/docs/2110-narrative-claim-register-test-plan-v1-20261013.md (sec1, sec2).
Researcher, chat 2026-10-13 (verbatim): "proceed to create all the configs and comply fully with
the governance to build and migrate the claims as per 2110".

Developer Mode: every cfg_* write goes through configmaint.apply_logged (cfg_behaviour_rule 75
devmode-config-writes-are-audited), run_id DEVMODE-2110-CONFIG-20261013, so cfg_change_detail
records each row with its prior state.

Step 1, config:
  cfg_trigger      new rule table (a trigger is schema, like a column or an index), registered in
                   cfg_table/cfg_column/cfg_unique/cfg_table_purpose/cfg_write_grant; the 9 live
                   triggers that already exist (4 iba, 5 bible_research) are registered in it
  cfg_enum         10 enums (sec3)
  cfg_setting      the three published paths (sec8), narrative.book_alias_map, the report folder
  cfg_behaviour_rule  the sec5 rule, word for word as approved
  cfg_work_package / cfg_step / cfg_on_fail / cfg_report   Narrative-Register.ps1, run.py-dispatched
  cfg_write_grant  each write step on the tables it writes; migration on all 11 (the import)
  cfg_utility      the library, the handler, the PS script, this migration
Step 2, schema:
  cfg_table / cfg_column / cfg_unique / cfg_index / cfg_trigger for the 11 tables, then the tables,
  indexes and triggers are created from that config through lib/db.py (table_ddl, trigger_ddl) --
  never a second hand-written DDL.

Idempotent: every row is checked before it is written; a table or trigger that exists is skipped.
One transaction.

Usage:
    python -m iba.app.migration.narrative_claim_register_config_v1_20261013 [--db PATH] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sqlite3
import sys

from iba.app.handlers.configmaint import apply_logged
from iba.app.lib.cfg import Cfg, DB_PATH
from iba.app.lib.db import table_ddl, trigger_ddl

RUN_ID = "DEVMODE-2110-CONFIG-20261013"
SRC = "escalation #2110, specification v1 (wa-essay-narrative-record-db-specification-v1-20261013.md)"
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[3]
WP = "narrative-register"
PS = "iba/app/ps/Narrative-Register.ps1"
LIB = "iba/app/lib/narrativeregister.py"
HANDLER = "iba/app/handlers/narrativeregister.py"
THIS = "iba/app/migration/narrative_claim_register_config_v1_20261013.py"
NOW_SQL = "strftime('%Y-%m-%dT%H:%M:%SZ','now')"

# ── enums (spec sec3; test plan 1.3) ───────────────────────────────────────────────────────────
ENUMS = {
    "narrative_chapter_state": ["draft", "draft + held", "empty", "deferred"],
    "narrative_claim_origin": ["original essay", "narrative"],
    "narrative_claim_verdict": ["Stands", "Widened", "Restated", "Withdrawn", "Held", "Added",
                                "New", "Removed", "Corrected"],
    "narrative_claim_status": ["current", "withdrawn", "held"],
    "narrative_claim_source_kind": ["verse", "lexical", "science", "study file"],
    "narrative_telling_kind": ["in full", "in part", "pointer"],
    "narrative_telling_status": ["current", "removed"],
    "narrative_claim_change_kind": ["claim created", "claim restated", "verdict changed",
                                    "claim withdrawn", "telling added", "telling changed",
                                    "telling removed", "passage moved", "renumbered", "edited"],
    "narrative_change_basis": ["recorded", "reconstructed", "direct edit"],
    "narrative_update_ref_kind": ["escalation", "thread", "thread item"],
}

# ── book alias map (spec sec3.8, sec4; test plan sec3) ─────────────────────────────────────────
# value = the book code iba.db `verse.reference` uses. Keys are matched after lower-casing and
# removing spaces and dots, so "1 Samuel", "1Sa" and "1 sa." are one key.
_BOOKS = [  # verse code, full name, other spellings in use (chapters, register, OSIS)
    ("Gen", "Genesis", []), ("Exo", "Exodus", ["Exod", "Ex"]), ("Lev", "Leviticus", []),
    ("Num", "Numbers", []), ("Deu", "Deuteronomy", ["Deut", "Dt"]), ("Jos", "Joshua", ["Josh"]),
    ("Judg", "Judges", ["Jdg", "Jdgs"]), ("Rut", "Ruth", []), ("1Sa", "1 Samuel", ["1Sam"]),
    ("2Sa", "2 Samuel", ["2Sam"]), ("1Ki", "1 Kings", ["1Kgs", "1Kin"]),
    ("2Ki", "2 Kings", ["2Kgs", "2Kin"]), ("1Ch", "1 Chronicles", ["1Chr", "1Chron"]),
    ("2Ch", "2 Chronicles", ["2Chr", "2Chron"]), ("Ezr", "Ezra", []), ("Neh", "Nehemiah", []),
    ("Est", "Esther", ["Esth"]), ("Job", "Job", []),
    ("Psa", "Psalms", ["Psalm", "Ps", "Pss"]), ("Pro", "Proverbs", ["Prov", "Prv"]),
    ("Ecc", "Ecclesiastes", ["Eccl", "Qoh"]),
    ("Song", "Song of Songs", ["Song of Solomon", "SoS", "Sng", "Canticles"]),
    ("Isa", "Isaiah", []), ("Jer", "Jeremiah", []), ("Lam", "Lamentations", []),
    ("Eze", "Ezekiel", ["Ezek", "Ezk"]), ("Dan", "Daniel", []), ("Hos", "Hosea", []),
    ("Joe", "Joel", ["Jol"]), ("Amo", "Amos", []), ("Obd", "Obadiah", ["Obad", "Oba"]),
    ("Jon", "Jonah", []), ("Mic", "Micah", []), ("Nah", "Nahum", []), ("Hab", "Habakkuk", []),
    ("Zep", "Zephaniah", ["Zeph"]), ("Hag", "Haggai", []), ("Zec", "Zechariah", ["Zech"]),
    ("Mal", "Malachi", []), ("Mat", "Matthew", ["Matt", "Mt"]), ("Mar", "Mark", ["Mrk", "Mk"]),
    ("Luk", "Luke", ["Lk"]), ("Joh", "John", ["Jn", "Jhn"]), ("Act", "Acts", []),
    ("Rom", "Romans", []), ("1Cor", "1 Corinthians", ["1Co"]), ("2Cor", "2 Corinthians", ["2Co"]),
    ("Gal", "Galatians", []), ("Eph", "Ephesians", []),
    ("Phili", "Philippians", ["Phil", "Php", "Phi"]), ("Col", "Colossians", []),
    ("1Th", "1 Thessalonians", ["1Thess", "1Thes"]), ("2Th", "2 Thessalonians", ["2Thess", "2Thes"]),
    ("1Ti", "1 Timothy", ["1Tim"]), ("2Ti", "2 Timothy", ["2Tim"]), ("Tit", "Titus", []),
    ("Phile", "Philemon", ["Phlm", "Phm"]), ("Heb", "Hebrews", []), ("Jam", "James", ["Jas"]),
    ("1Pe", "1 Peter", ["1Pet"]), ("2Pe", "2 Peter", ["2Pet"]), ("1Jo", "1 John", ["1John", "1Jn"]),
    ("2Jo", "2 John", ["2John", "2Jn"]), ("3Jo", "3 John", ["3John", "3Jn"]),
    ("Jude", "Jude", ["Jud"]), ("Rev", "Revelation", ["Rv"]),
]


def _alias_key(s: str) -> str:
    return s.lower().replace(" ", "").replace(".", "")


def book_alias_map() -> dict[str, str]:
    m: dict[str, str] = {}
    for code, full, others in _BOOKS:
        for a in [code, full, *others]:
            k = _alias_key(a)
            if k in m and m[k] != code:
                raise ValueError(f"alias {a!r} maps to both {m[k]} and {code}")
            m[k] = code
    return m


SETTINGS = [
    ("narrative.claim_register_path", '"_analytics/essay/spirit_soul_body/narrative-claim-register.md"',
     "the published claim register (Narrative-Register.ps1 -Action Export): index notes, chapters "
     "with their sections and the claims told there, the original essay claims, the claims not in "
     "the narrative, the Tally. One fixed name, outside inner-being-narrative/, so it is never "
     "copied to learning4comfort (escalation #2110, spec sec8)"),
    ("narrative.claim_changes_path", '"_analytics/essay/spirit_soul_body/narrative-claim-changes.md"',
     "the published change log, by update, newest first, and the Structure log (Export; "
     "escalation #2110, spec sec8)"),
    ("narrative.citation_index_path", '"_analytics/essay/spirit_soul_body/narrative-citation-index.md"',
     "the published citation index: every verse cited in the narrative, in canonical order, with "
     "where it is cited and which claims rest on it (Export; escalation #2110, spec sec8)"),
    ("narrative.register_report_dir", '"outputs/narrative-register"',
     "where Narrative-Register.ps1 -Action Find/History/Check write their dated reports "
     "(escalation #2110)"),
    ("narrative.book_alias_map", json.dumps(book_alias_map(), ensure_ascii=False, sort_keys=True),
     "book name or abbreviation -> the book code iba.db verse.reference uses. Keys are lower case "
     "with spaces and dots removed (lib/narrativeregister.py parse_refs normalises the same way). "
     "The chapters write full names (2 Corinthians), the register short codes (2Co), verse uses "
     "its own (2Cor) -- escalation #2110, spec sec1, sec3.8"),
]

BEHAVIOUR_RULE = (
    "chat", "narrative-claim-register-kept-in-iba-db",
    "The narrative claim register is kept in iba.db. It is edited there, through "
    "`Narrative-Register.ps1` or directly, and every change keeps its before and after. The "
    "register file is the published copy, regenerated from the database after each change; an "
    "edit made only in that file is not kept.",
    "Researcher, chat 2026-10-13 (#2110), round 2, verbatim: \"Q-D as suggested\" (the rule as "
    "suggested in the specification, sec5); round 1: \"Q-D this does not make sense. the index "
    "cannot be static, it must be editable.\"",
    "Narrative-Register.ps1 (work package narrative-register); history triggers on "
    "narrative_claim, narrative_claim_telling, narrative_passage and narrative_chapter "
    "(cfg_trigger); -Action Export regenerates the three published files",
    "partially_enforced",
)

# ── the work package and its steps (cfg_behaviour_rule 43: dispatched through run.py) ───────────
STEPS = [  # step, does, tables written
    ("add_claim", "a new claim with its sources (-Text -BeyondText -Source)",
     ["narrative_claim", "narrative_claim_source", "narrative_claim_change"]),
    ("edit", "changes a claim's wording, verdict or sources; the trigger logs it",
     ["narrative_claim", "narrative_claim_source", "narrative_claim_change"]),
    ("tell", "links a claim to the passage that tells it (-Chapter -Passage <opening words>)",
     ["narrative_passage", "narrative_claim_telling", "narrative_claim_change", "narrative_claim"]),
    ("untell", "removes a claim's telling from a passage (status removed; the row stays)",
     ["narrative_claim_telling", "narrative_claim_change", "narrative_claim"]),
    ("withdraw", "withdraws a claim (the row stays, with its history)",
     ["narrative_claim", "narrative_claim_change"]),
    ("edit_note", "edits one block of the index text", ["narrative_index_note"]),
    ("edit_chapter", "edits a chapter row (number, title, state, current file)",
     ["narrative_chapter", "narrative_claim_change"]),
    ("edit_section", "edits a section row (heading, level, parent, order); a rename keeps the old "
                     "row and moves its current passages to the new one",
     ["narrative_section", "narrative_passage", "narrative_claim_change"]),
    ("record", "records a weave's whole update from a JSON file, then compares the chapter versions "
               "passage by passage and lists what the JSON does not account for",
     ["narrative_update", "narrative_update_ref", "narrative_chapter", "narrative_section",
      "narrative_passage", "narrative_claim", "narrative_claim_source", "narrative_claim_telling",
      "narrative_claim_change", "narrative_citation"]),
    ("find", "read-only search (-Verse -Chapter -Section -Claim -Text -Escalation -Thread -Verdict "
             "-NotInNarrative -ToldInMoreThanOne)", []),
    ("history", "read-only: every change to a claim and to the passages that tell it", []),
    ("check", "read-only: chapters, sections and passage anchors against the files on disk", []),
    ("export", "regenerates the three published files (spec sec8)", []),
]
REPORT_STEPS = {"find": "Narrative register search", "history": "Narrative claim history",
                "check": "Narrative register check"}

# ── the 11 tables (spec sec3) ──────────────────────────────────────────────────────────────────
# (name, type, is_pk, notnull, is_unique, dflt, fk, use, expectation)
_ID = ("id", "INTEGER", 1, 1, 0, None, None, "surrogate PK", "assigned by SQLite")
_CREATED = [
    ("created_at", "TEXT", 0, 1, 0, f"({NOW_SQL})", None, "when the row was written (ISO-8601 UTC)",
     "historical date for imported rows; now for new rows"),
    ("created_by", "TEXT", 0, 1, 0, "'direct edit'", None,
     "who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, "
     "for a row inserted outside the tool)", "never NULL"),
]
CH = "narrative_chapter.id"
SEC = "narrative_section.id"

TABLES: dict[str, tuple[str, str, list[tuple]]] = {
    "narrative_chapter": (
        "one row per chapter or sub-chapter",
        "One row per chapter or sub-chapter of the inner-being narrative. A renumbering changes "
        "chapter_no on the row and is logged; every record keeps its link to the chapter, so the "
        "history follows the chapter, not the number. Chapters may be added, split, merged, "
        "renamed, renumbered or retired (inactive). escalation #2110, spec sec3.1",
        [_ID,
         ("chapter_no", "TEXT", 0, 1, 0, None, None, "02, 10.7, 13.1",
          "unique among active rows (trigger trg_narrative_chapter_no_bi/_bu)"),
         ("title", "TEXT", 0, 1, 0, None, None, "the chapter heading, e.g. Choosing and setting direction", None),
         ("reading_order", "INTEGER", 0, 1, 0, None, None, "order in the book", None),
         ("file_stem", "TEXT", 0, 1, 0, None, None, "e.g. 10-07-choosing-and-setting-direction", None),
         ("current_version", "INTEGER", 0, 0, 0, None, None, "the current chapter file's version, e.g. 27", None),
         ("current_file", "TEXT", 0, 0, 0, None, None, "the current chapter file name", "matches a file on disk (Check)"),
         ("state", "TEXT", 0, 1, 0, None, None, "cfg_enum narrative_chapter_state", None),
         ("replaces_original", "TEXT", 0, 0, 0, None, None, "the index column 'Replaces or absorbs (original)'", None),
         ("built_from", "TEXT", 0, 0, 0, None, None, "the index column 'Built from'", None),
         ("inactive", "INTEGER", 0, 1, 0, "0", None, "1 for a retired chapter number (old Ch 13 Under God's anger)", None),
         *_CREATED]),
    "narrative_section": (
        "one row per section heading in a chapter",
        "One row per section heading in a chapter, current or past. A chapter's opening, before "
        "any heading, has its own row (level 0). escalation #2110, spec sec3.2",
        [_ID,
         ("chapter_id", "INTEGER", 0, 1, 0, None, CH, "the chapter", None),
         ("heading", "TEXT", 0, 1, 0, None, None, "the heading text as written; '(opening)' for the opening", None),
         ("level", "INTEGER", 0, 1, 0, None, None, "heading level 2-4; 0 for the opening", None),
         ("parent_section_id", "INTEGER", 0, 0, 0, None, SEC, "the section it sits in", None),
         ("ordinal", "INTEGER", 0, 1, 0, None, None, "order in the chapter", None),
         ("first_version", "INTEGER", 0, 0, 0, None, None, "the first chapter version that has the heading", None),
         ("last_version", "INTEGER", 0, 0, 0, None, None, "the last chapter version that has it; NULL while current", None),
         ("renamed_from_id", "INTEGER", 0, 0, 0, None, SEC, "when a heading is renamed, the old row", None),
         *_CREATED]),
    "narrative_claim": (
        "one row per claim",
        "The register: one row per claim. A claim is a statement derived from sources (verses, "
        "later science) that goes beyond their mere text, held in its own plain wording. A "
        "quotation is not a claim. escalation #2110, spec sec3.3 (researcher, round 3)",
        [_ID,
         ("claim_ref", "TEXT", 0, 0, 1, None, None,
          "original claims keep the register's id (I-1, 2-5, K-2); new claims are C-{id}, set by "
          "trigger trg_narrative_claim_ref_ai when left empty", "unique"),
         ("origin", "TEXT", 0, 1, 0, None, None, "cfg_enum narrative_claim_origin", None),
         ("claim_text", "TEXT", 0, 1, 0, None, None, "the claim in its own plain wording, apart from how the narrative tells it", None),
         ("beyond_text", "TEXT", 0, 0, 0, None, None, "what the claim adds to its sources: why it is a claim and not a quotation", None),
         ("i_read", "INTEGER", 0, 1, 0, "0", None, "1 when the narrative marks it as the narrator's reading ('I read')", None),
         ("verdict", "TEXT", 0, 0, 0, None, None, "cfg_enum narrative_claim_verdict, the register's own words", None),
         ("part_verdict", "TEXT", 0, 0, 0, None, None, "the second verdict of a split verdict, e.g. Held in 9-1", None),
         ("part_scope", "TEXT", 0, 0, 0, None, None, "what each part of a split verdict covers", None),
         ("original_chapter", "TEXT", 0, 0, 0, None, None, "for original claims: the essay chapter heading", None),
         ("original_wording", "TEXT", 0, 0, 0, None, None, "for original claims: the claim as the essay made it", None),
         ("main_chapter_id", "INTEGER", 0, 0, 0, None, CH, "the chapter that tells the claim most fully", None),
         ("main_section_id", "INTEGER", 0, 0, 0, None, SEC, "the section that tells it most fully", None),
         ("in_narrative", "INTEGER", 0, 1, 0, "0", None,
          "1 if at least one current passage tells the claim (a pointer does not count); 0 if none. "
          "The filter for claims not included", "kept by the telling and passage triggers"),
         ("status", "TEXT", 0, 1, 0, "'current'", None, "cfg_enum narrative_claim_status", None),
         *_CREATED]),
    "narrative_claim_source": (
        "one row per source of a claim",
        "What a claim rests on: a verse (one row per verse; ranges and lists expanded), a lexical "
        "source, science (later), or a study file. escalation #2110, spec sec3.4",
        [_ID,
         ("claim_id", "INTEGER", 0, 1, 0, None, "narrative_claim.id", "the claim", None),
         ("source_kind", "TEXT", 0, 1, 0, None, None, "cfg_enum narrative_claim_source_kind", None),
         ("verse_id", "INTEGER", 0, 0, 0, None, "verse.id", "for kind verse; NULL where the verse has no row",
          "a non-NULL value must name a verse row (trigger trg_narrative_claim_source_verse_bi/_bu)"),
         ("ref_as_written", "TEXT", 0, 0, 0, None, None, "the reference as written, e.g. 1 Samuel 24:5", None),
         ("ref_normalised", "TEXT", 0, 0, 0, None, None, "in verse.reference form, e.g. 1Sa 24:5", None),
         ("source_text", "TEXT", 0, 0, 0, None, None, "for the other kinds: the word with its gloss, the science reference, or the file path", None),
         ("note", "TEXT", 0, 0, 0, None, None, "how the source bears on the claim, where it is not plain", None),
         *_CREATED]),
    "narrative_passage": (
        "one row per passage that tells at least one claim",
        "One row per passage of the story (a paragraph or a bullet as it stands in the chapter) "
        "that tells at least one claim. passage_text is edited in place; the triggers log the "
        "before and after for every claim it tells. escalation #2110, spec sec3.5",
        [_ID,
         ("chapter_id", "INTEGER", 0, 1, 0, None, CH, "the chapter", None),
         ("section_id", "INTEGER", 0, 0, 0, None, SEC, "the section", None),
         ("ordinal", "INTEGER", 0, 1, 0, None, None, "its place in the section", None),
         ("anchor_text", "TEXT", 0, 1, 0, None, None, "its opening words, so the tool can find it in the file", "found in the current chapter file (Check)"),
         ("passage_text", "TEXT", 0, 1, 0, None, None, "the passage as it now reads", None),
         ("first_version", "INTEGER", 0, 0, 0, None, None, "the first chapter version that holds it", None),
         ("last_version", "INTEGER", 0, 0, 0, None, None, "the last chapter version that holds it; NULL while current", None),
         *_CREATED]),
    "narrative_claim_telling": (
        "one row per claim told in a passage",
        "The link between a claim and a passage that tells it (many to many). escalation #2110, "
        "spec sec3.5",
        [_ID,
         ("claim_id", "INTEGER", 0, 1, 0, None, "narrative_claim.id", "the claim", None),
         ("passage_id", "INTEGER", 0, 1, 0, None, "narrative_passage.id", "the passage", None),
         ("kind", "TEXT", 0, 1, 0, None, None, "cfg_enum narrative_telling_kind: in full, in part, pointer", None),
         ("part_told", "TEXT", 0, 0, 0, None, None, "which part of the claim this passage tells", None),
         ("status", "TEXT", 0, 1, 0, "'current'", None, "cfg_enum narrative_telling_status: current, removed", None),
         *_CREATED]),
    "narrative_update": (
        "one row per weave or recorded pass",
        "One row per weave or recorded pass on the narrative, with its instruction, sources, notes "
        "and quote check. Imported updates keep the register version that added them. "
        "escalation #2110, spec sec3.6",
        [_ID,
         ("update_date", "TEXT", 0, 1, 0, None, None, "ISO date of the update", None),
         ("title", "TEXT", 0, 1, 0, None, None, "the update's heading", None),
         ("strand", "TEXT", 0, 0, 0, None, None, "e.g. anger (M02)", None),
         ("researcher_instruction", "TEXT", 0, 0, 0, None, None, "verbatim", None),
         ("method", "TEXT", 0, 0, 0, None, None, "method or rule named (e.g. rule 73)", None),
         ("source_files", "TEXT", 0, 0, 0, None, None, "one path per line", None),
         ("scripts", "TEXT", 0, 0, 0, None, None, "one path per line", None),
         ("claims_changed_note", "TEXT", 0, 0, 0, None, None, "'Original claims changed', verbatim", None),
         ("not_woven_note", "TEXT", 0, 0, 0, None, None, "'Not woven' / 'Kept out', verbatim", None),
         ("structure_change", "TEXT", 0, 0, 0, None, None, "filled when the book's shape changed (the Structure log)", None),
         ("structure_reason", "TEXT", 0, 0, 0, None, None, "the reason for the structure change", None),
         ("quote_parts", "INTEGER", 0, 0, 0, None, None, "the quote check: parts checked", None),
         ("quote_failures", "INTEGER", 0, 0, 0, None, None, "the quote check: failures", None),
         ("quote_note", "TEXT", 0, 0, 0, None, None, "the quote check note, verbatim", None),
         ("notes", "TEXT", 0, 0, 0, None, None, "any other paragraph, verbatim", None),
         ("legacy_register_version", "INTEGER", 0, 0, 0, None, None, "for imported updates, the register version that added it", None),
         *_CREATED]),
    "narrative_update_ref": (
        "one row per escalation or thread an update names",
        "The escalations, threads and thread items an update names. escalation #2110, spec sec3.6",
        [_ID,
         ("update_id", "INTEGER", 0, 1, 0, None, "narrative_update.id", "the update", None),
         ("kind", "TEXT", 0, 1, 0, None, None, "cfg_enum narrative_update_ref_kind", None),
         ("value", "TEXT", 0, 1, 0, None, None, "1998, OT-29, OT-29.1", None),
         *_CREATED]),
    "narrative_claim_change": (
        "one row per change to a claim or to a passage that tells it",
        "The change log, many rows per claim: every change to a claim, and to each passage that "
        "tells it, with enough before and after to review the impact without opening another file "
        "(Q-F). A change to one passage that tells three claims writes three rows. escalation "
        "#2110, spec sec3.7",
        [_ID,
         ("claim_id", "INTEGER", 0, 1, 0, None, "narrative_claim.id", "the claim", None),
         ("passage_id", "INTEGER", 0, 0, 0, None, "narrative_passage.id", "the passage, for a change in how the claim is told", None),
         ("update_id", "INTEGER", 0, 0, 0, None, "narrative_update.id", "the update that made it; NULL for a direct edit", None),
         ("change_date", "TEXT", 0, 1, 0, None, None, "ISO date", None),
         ("change_kind", "TEXT", 0, 1, 0, None, None, "cfg_enum narrative_claim_change_kind", None),
         ("claim_before", "TEXT", 0, 0, 0, None, None, "the claim's wording before", None),
         ("claim_after", "TEXT", 0, 0, 0, None, None, "the claim's wording after", None),
         ("verdict_before", "TEXT", 0, 0, 0, None, None, "the verdict before", None),
         ("verdict_after", "TEXT", 0, 0, 0, None, None, "the verdict after", None),
         ("passage_before", "TEXT", 0, 0, 0, None, None, "the full passage before, as it read in the chapter", None),
         ("passage_after", "TEXT", 0, 0, 0, None, None, "the full passage after", None),
         ("chapter_id", "INTEGER", 0, 0, 0, None, CH, "where", None),
         ("section_id", "INTEGER", 0, 0, 0, None, SEC, "where", None),
         ("section_before_id", "INTEGER", 0, 0, 0, None, SEC, "where from, for a move", None),
         ("chapter_version_from", "INTEGER", 0, 0, 0, None, None, "e.g. 7", None),
         ("chapter_version_to", "INTEGER", 0, 0, 0, None, None, "e.g. 8", None),
         ("file_before", "TEXT", 0, 0, 0, None, None, "the chapter file before", None),
         ("file_after", "TEXT", 0, 0, 0, None, None, "the chapter file after", None),
         ("note", "TEXT", 0, 0, 0, None, None, "the verdict cell verbatim, or any remark", None),
         ("basis", "TEXT", 0, 1, 0, None, None, "cfg_enum narrative_change_basis: recorded, reconstructed, direct edit", None),
         ("provenance", "TEXT", 0, 0, 0, None, None, "the file(s) the row came from, or the trigger that wrote it", None),
         *_CREATED]),
    "narrative_citation": (
        "one row per verse cited in a passage of the story",
        "The citation index: every verse cited anywhere in the story, by passage. With "
        "narrative_claim_source it answers, for any verse, where it is cited and which claims rest "
        "on it. A reference that cannot be resolved is kept with verse_id NULL, never dropped. "
        "escalation #2110, spec sec3.8",
        [_ID,
         ("chapter_id", "INTEGER", 0, 1, 0, None, CH, "where it is cited", None),
         ("section_id", "INTEGER", 0, 0, 0, None, SEC, "where it is cited", None),
         ("passage_id", "INTEGER", 0, 0, 0, None, "narrative_passage.id", "NULL if the passage tells no claim", None),
         ("verse_id", "INTEGER", 0, 0, 0, None, "verse.id", "NULL where the verse has no row",
          "a non-NULL value must name a verse row (trigger trg_narrative_citation_verse_bi/_bu)"),
         ("ref_as_written", "TEXT", 0, 1, 0, None, None, "as written in the chapter", None),
         ("ref_normalised", "TEXT", 0, 0, 0, None, None, "in verse.reference form", None),
         ("quoted", "INTEGER", 0, 1, 0, "0", None, "1 when the verse's words are quoted, 0 when it is only referred to", None),
         ("first_version", "INTEGER", 0, 0, 0, None, None, "the first chapter version that cites it", None),
         ("last_version", "INTEGER", 0, 0, 0, None, None, "the last chapter version that cites it; NULL while current", None),
         *_CREATED]),
    "narrative_index_note": (
        "one row per block of index text",
        "The parts of the old narrative index that are text, not tables (researcher direction, "
        "theme and frame, rules applied, how later work updates the narrative, source files, verse "
        "check), one row per block, editable. escalation #2110, spec sec3.9",
        [_ID,
         ("heading", "TEXT", 0, 1, 0, None, None, "the block heading", None),
         ("text", "TEXT", 0, 1, 0, None, None, "the block text (markdown)", None),
         ("ordinal", "INTEGER", 0, 1, 0, None, None, "order in the published register", None),
         *_CREATED]),
}

CFG_UNIQUE = {"narrative_claim_telling": ["claim_id", "passage_id"],
              "narrative_update_ref": ["update_id", "kind", "value"]}

# ── history triggers (spec sec5; test plan 2.3-2.9) ────────────────────────────────────────────
_IN_NARR = ("(SELECT EXISTS (SELECT 1 FROM narrative_claim_telling t JOIN narrative_passage p "
            "ON p.id = t.passage_id WHERE t.claim_id = narrative_claim.id AND t.status = 'current' "
            "AND t.kind <> 'pointer' AND p.last_version IS NULL))")
_CHG_COLS = "claim_id, passage_id, change_date, change_kind, "


def _trig(name: str, head: str, body: str) -> str:
    return f"CREATE TRIGGER {name} {head}\nBEGIN\n{body}\nEND"


def _change_insert(trigger: str, cols: str, values: str) -> str:
    """One INSERT into narrative_claim_change. `values` is either 'VALUES (e1, e2, ...' (no closing
    parenthesis) or 'SELECT e1, e2, ... [FROM ...]'; the audit columns (basis, provenance,
    created_by) are appended to the expression list -- for SELECT, before the outer FROM."""
    audit = f"'direct edit', 'trigger {trigger}', 'trigger'"
    head = f"  INSERT INTO narrative_claim_change ({cols}, basis, provenance, created_by)" + "\n  "
    if values.startswith("VALUES ("):
        return f"{head}{values}, {audit});"
    depth, cut = 0, None
    for i, ch in enumerate(values):
        depth += (ch == "(") - (ch == ")")
        if depth == 0 and values.startswith(" FROM ", i):
            cut = i
            break
    if cut is None:
        return f"{head}{values}, {audit};"
    return f"{head}{values[:cut]}, {audit}{values[cut:]};"


def _recompute(where: str) -> str:
    return f"  UPDATE narrative_claim SET in_narrative = {_IN_NARR} WHERE {where};"


TRIGGERS: list[tuple[str, str, str, str]] = []   # (table, name, sql, use)


def _add(table: str, name: str, head: str, body: str, use: str) -> None:
    TRIGGERS.append((table, name, _trig(name, head, body), use))


_add("narrative_claim", "trg_narrative_claim_ref_ai",
     "AFTER INSERT ON narrative_claim WHEN NEW.claim_ref IS NULL",
     "  UPDATE narrative_claim SET claim_ref = 'C-' || NEW.id WHERE id = NEW.id;",
     "a new claim with no claim_ref is given C-{id} (spec sec3.3)")
_add("narrative_claim", "trg_narrative_claim_ai", "AFTER INSERT ON narrative_claim",
     _change_insert("trg_narrative_claim_ai",
                    "claim_id, change_date, change_kind, claim_after, verdict_after, chapter_id, section_id",
                    "VALUES (NEW.id, substr(NEW.created_at, 1, 10), 'claim created', NEW.claim_text, "
                    "NEW.verdict, NEW.main_chapter_id, NEW.main_section_id"),
     "every new claim writes its 'claim created' change row")
_add("narrative_claim", "trg_narrative_claim_text_au",
     "AFTER UPDATE OF claim_text ON narrative_claim WHEN OLD.claim_text IS NOT NEW.claim_text",
     _change_insert("trg_narrative_claim_text_au",
                    "claim_id, change_date, change_kind, claim_before, claim_after",
                    "VALUES (NEW.id, date('now'), 'edited', OLD.claim_text, NEW.claim_text"),
     "a change to a claim's wording writes its before and after (test plan 2.4)")
_add("narrative_claim", "trg_narrative_claim_verdict_au",
     "AFTER UPDATE OF verdict ON narrative_claim WHEN OLD.verdict IS NOT NEW.verdict",
     _change_insert("trg_narrative_claim_verdict_au",
                    "claim_id, change_date, change_kind, verdict_before, verdict_after",
                    "VALUES (NEW.id, date('now'), 'verdict changed', OLD.verdict, NEW.verdict"),
     "a change of verdict writes its before and after (test plan 2.5)")
_add("narrative_claim", "trg_narrative_claim_status_au",
     "AFTER UPDATE OF status ON narrative_claim WHEN OLD.status IS NOT NEW.status",
     _change_insert("trg_narrative_claim_status_au",
                    "claim_id, change_date, change_kind, claim_before, claim_after, note",
                    "VALUES (NEW.id, date('now'), CASE NEW.status WHEN 'withdrawn' THEN "
                    "'claim withdrawn' ELSE 'edited' END, NEW.claim_text, NEW.claim_text, "
                    "'status: ' || OLD.status || ' -> ' || NEW.status"),
     "a change of status (withdrawn, held, current) is logged")
_add("narrative_passage", "trg_narrative_passage_text_au",
     "AFTER UPDATE OF passage_text ON narrative_passage WHEN OLD.passage_text IS NOT NEW.passage_text",
     _change_insert("trg_narrative_passage_text_au",
                    _CHG_COLS + "passage_before, passage_after, chapter_id, section_id",
                    "SELECT t.claim_id, NEW.id, date('now'), 'telling changed', OLD.passage_text, "
                    "NEW.passage_text, NEW.chapter_id, NEW.section_id FROM narrative_claim_telling t "
                    "WHERE t.passage_id = NEW.id AND t.status = 'current'"),
     "a change to a passage writes one row per claim it tells, with the passage before and after "
     "(test plan 2.6)")
_add("narrative_passage", "trg_narrative_passage_move_au",
     "AFTER UPDATE OF chapter_id, section_id ON narrative_passage WHEN (OLD.chapter_id IS NOT "
     "NEW.chapter_id OR OLD.section_id IS NOT NEW.section_id) AND NOT (OLD.chapter_id IS "
     "NEW.chapter_id AND (SELECT renamed_from_id FROM narrative_section WHERE id = NEW.section_id) "
     "IS OLD.section_id)",
     _change_insert("trg_narrative_passage_move_au",
                    _CHG_COLS + "passage_after, chapter_id, section_id, section_before_id, note",
                    "SELECT t.claim_id, NEW.id, date('now'), 'passage moved', NEW.passage_text, "
                    "NEW.chapter_id, NEW.section_id, OLD.section_id, 'moved from chapter id ' || "
                    "OLD.chapter_id FROM narrative_claim_telling t WHERE t.passage_id = NEW.id AND "
                    "t.status = 'current'"),
     "a passage moved to another chapter or section keeps its row and its claims; the move is "
     "logged with where from (spec sec3.1). A heading renamed in place (the new section row's "
     "renamed_from_id is the old one) is not a move")
_add("narrative_passage", "trg_narrative_passage_retire_au",
     "AFTER UPDATE OF last_version ON narrative_passage WHEN (OLD.last_version IS NULL) <> "
     "(NEW.last_version IS NULL)",
     _recompute("id IN (SELECT claim_id FROM narrative_claim_telling WHERE passage_id = NEW.id)"),
     "a passage that leaves (or returns to) the current narrative updates in_narrative of the "
     "claims it tells (test plan 2.9)")
_add("narrative_claim_telling", "trg_narrative_telling_ai", "AFTER INSERT ON narrative_claim_telling",
     _change_insert("trg_narrative_telling_ai",
                    _CHG_COLS + "passage_after, chapter_id, section_id, note",
                    "SELECT NEW.claim_id, NEW.passage_id, substr(NEW.created_at, 1, 10), "
                    "'telling added', p.passage_text, p.chapter_id, p.section_id, NEW.kind || "
                    "COALESCE(': ' || NEW.part_told, '') FROM narrative_passage p WHERE p.id = "
                    "NEW.passage_id") + "\n" + _recompute("id = NEW.claim_id"),
     "a new telling writes 'telling added' and updates in_narrative (test plan 2.7, 2.9)")
_add("narrative_claim_telling", "trg_narrative_telling_status_au",
     "AFTER UPDATE OF status ON narrative_claim_telling WHEN OLD.status IS NOT NEW.status",
     _change_insert("trg_narrative_telling_status_au",
                    _CHG_COLS + "passage_before, passage_after, chapter_id, section_id, note",
                    "SELECT NEW.claim_id, NEW.passage_id, date('now'), CASE NEW.status WHEN "
                    "'removed' THEN 'telling removed' ELSE 'telling added' END, CASE NEW.status "
                    "WHEN 'removed' THEN p.passage_text END, CASE NEW.status WHEN 'removed' THEN "
                    "NULL ELSE p.passage_text END, p.chapter_id, p.section_id, 'status: ' || "
                    "OLD.status || ' -> ' || NEW.status FROM narrative_passage p WHERE p.id = "
                    "NEW.passage_id") + "\n" + _recompute("id = NEW.claim_id"),
     "a telling removed (or restored) is logged and updates in_narrative (test plan 2.7, 2.9)")
_add("narrative_claim_telling", "trg_narrative_telling_kind_au",
     "AFTER UPDATE OF kind, part_told ON narrative_claim_telling WHEN OLD.kind IS NOT NEW.kind OR "
     "OLD.part_told IS NOT NEW.part_told",
     _change_insert("trg_narrative_telling_kind_au",
                    _CHG_COLS + "passage_after, chapter_id, section_id, note",
                    "SELECT NEW.claim_id, NEW.passage_id, date('now'), 'telling changed', "
                    "p.passage_text, p.chapter_id, p.section_id, 'kind: ' || OLD.kind || ' -> ' || "
                    "NEW.kind || '; part: ' || COALESCE(OLD.part_told, '-') || ' -> ' || "
                    "COALESCE(NEW.part_told, '-') FROM narrative_passage p WHERE p.id = "
                    "NEW.passage_id") + "\n" + _recompute("id = NEW.claim_id"),
     "a change to how a passage tells a claim (kind, part told) is logged")
_add("narrative_claim_telling", "trg_narrative_telling_ad", "AFTER DELETE ON narrative_claim_telling",
     _change_insert("trg_narrative_telling_ad",
                    _CHG_COLS + "passage_before, note",
                    "SELECT OLD.claim_id, OLD.passage_id, date('now'), 'telling removed', "
                    "(SELECT passage_text FROM narrative_passage WHERE id = OLD.passage_id), "
                    "'telling row deleted'") + "\n" + _recompute("id = OLD.claim_id"),
     "a deleted telling row (the tool never deletes; Untell sets status removed) is still logged")
_add("narrative_chapter", "trg_narrative_chapter_no_bi",
     "BEFORE INSERT ON narrative_chapter WHEN NEW.inactive = 0 AND EXISTS (SELECT 1 FROM "
     "narrative_chapter WHERE chapter_no = NEW.chapter_no AND inactive = 0)",
     "  SELECT RAISE(ABORT, 'narrative_chapter: chapter_no is already used by an active chapter');",
     "chapter_no unique among active rows (test plan 2.3)")
_add("narrative_chapter", "trg_narrative_chapter_no_bu",
     "BEFORE UPDATE OF chapter_no, inactive ON narrative_chapter WHEN NEW.inactive = 0 AND EXISTS "
     "(SELECT 1 FROM narrative_chapter WHERE chapter_no = NEW.chapter_no AND inactive = 0 AND id "
     "<> NEW.id)",
     "  SELECT RAISE(ABORT, 'narrative_chapter: chapter_no is already used by an active chapter');",
     "chapter_no unique among active rows (test plan 2.3)")
_add("narrative_chapter", "trg_narrative_chapter_renumber_au",
     "AFTER UPDATE OF chapter_no ON narrative_chapter WHEN OLD.chapter_no IS NOT NEW.chapter_no",
     _change_insert("trg_narrative_chapter_renumber_au",
                    "claim_id, change_date, change_kind, chapter_id, note",
                    "SELECT DISTINCT t.claim_id, date('now'), 'renumbered', NEW.id, 'Ch ' || "
                    "OLD.chapter_no || ' -> Ch ' || NEW.chapter_no FROM narrative_claim_telling t "
                    "JOIN narrative_passage p ON p.id = t.passage_id WHERE p.chapter_id = NEW.id "
                    "AND t.status = 'current'"),
     "a renumbered chapter is logged on every claim it tells (spec sec3.1)")
for _tbl, _short in (("narrative_claim_source", "claim_source"), ("narrative_citation", "citation")):
    for _ev, _head in (("bi", f"BEFORE INSERT ON {_tbl}"), ("bu", f"BEFORE UPDATE OF verse_id ON {_tbl}")):
        _add(_tbl, f"trg_narrative_{_short}_verse_{_ev}",
             f"{_head} WHEN NEW.verse_id IS NOT NULL AND NOT EXISTS (SELECT 1 FROM verse WHERE id "
             f"= NEW.verse_id)",
             f"  SELECT RAISE(ABORT, '{_tbl}: verse_id has no verse row');",
             "a verse_id that names no verse row is refused (test plan 2.2); NULL is allowed")

# ── cfg_trigger itself (new rule table) ────────────────────────────────────────────────────────
CFG_TRIGGER_TABLE = (
    "one row per trigger",
    "Every SQLite trigger in either database, with its full CREATE TRIGGER statement. A trigger is "
    "schema exactly like a column or an index: lib/db.py:trigger_ddl() rebuilds it from here, and "
    "cfgquality.find_unregistered_triggers (configmaint.validate) checks the live databases "
    "against it. escalation #2110, 2026-10-13",
    [("database", "TEXT", 0, 1, 0, None, None, "iba or bible_research", None),
     ("table_name", "TEXT", 0, 1, 0, None, None, "the table the trigger is on", None),
     ("name", "TEXT", 0, 1, 0, None, None, "the trigger name (unique per database)", None),
     ("ordinal", "INTEGER", 0, 1, 0, "0", None, "creation order within a table", None),
     ("sql", "TEXT", 0, 1, 0, None, None, "the full CREATE TRIGGER statement", "equal to sqlite_master.sql, whitespace ignored"),
     ("use", "TEXT", 0, 0, 0, None, None, "what the trigger does and why", None),
     ("inactive", "INTEGER", 0, 1, 0, "0", None, "1 for a retired trigger", None)])
CFG_TRIGGER_PURPOSE = [
    ("purpose", "Every SQLite trigger the project's two databases carry -- table, name and full "
                "CREATE TRIGGER statement -- so a table rebuilt from config gets its triggers back."),
    ("success", "Every live trigger in iba.db and bible_research.db has a row here with the same "
                "SQL, and every active row names a live trigger "
                "(cfgquality.find_unregistered_triggers)."),
]
EXISTING_TRIGGER_USE = {
    "verse_meta_on_verse_insert": "keeps verse_meta in step when a verse row is inserted",
    "verse_meta_on_verse_deleted": "keeps verse_meta in step when a verse is soft-deleted",
    "verse_meta_on_passage_change": "keeps verse_meta in step when verse_passage changes",
    "verse_meta_on_lexical_change": "keeps verse_meta in step when verse_lexical changes",
    "wa_verse_records_updated_at": "stamps wa_verse_records.updated_at on update",
    "wa_quality_flag_types_cascade_delete": "removes a quality flag type's flags with it",
    "prose_section_ad": "keeps prose_section_fts in step on delete",
    "prose_section_ai": "keeps prose_section_fts in step on insert",
    "prose_section_au": "keeps prose_section_fts in step on update",
}


# ── helpers ────────────────────────────────────────────────────────────────────────────────────
def _exists(conn, sql: str, params) -> bool:
    return conn.execute(sql, params).fetchone() is not None


def _put(conn, report: list[str], table: str, key: dict, row: dict, label: str) -> None:
    """Ensure the row `key`+`row` through apply_logged: insert it when no row matches `key`; update
    the columns that differ when one does (a correction made in this file reaches the live config,
    audited); otherwise skip."""
    where = " AND ".join(f'"{k}"=?' for k in key)
    cur = conn.execute(f'SELECT * FROM "{table}" WHERE {where}', list(key.values()))
    found = cur.fetchone()
    if found is None:
        apply_logged(conn, RUN_ID, table, "insert", {}, {**key, **row})
        report.append(f"  {table} {label}: inserted")
        return
    have = dict(zip([d[0] for d in cur.description], found))
    diff = {k: v for k, v in row.items() if have.get(k) != v}
    if diff:
        apply_logged(conn, RUN_ID, table, "update", key, diff)
        report.append(f"  {table} {label}: updated {sorted(diff)}")
    else:
        report.append(f"  {table} {label}: present -- skipped")


def _register_table(conn, report, name, grain, use, cols, category) -> None:
    _put(conn, report, "cfg_table", {"database": "iba", "name": name},
         {"grain": grain, "use": use, "inactive": 0, "category": category}, name)
    for ordinal, (cname, ctype, is_pk, notnull, is_unique, dflt, fk, cuse, expect) in enumerate(cols):
        _put(conn, report, "cfg_column", {"database": "iba", "table_name": name, "name": cname},
             {"ordinal": ordinal, "type": ctype, "is_pk": is_pk, "notnull": notnull,
              "is_unique": is_unique, "dflt": dflt, "fk": fk, "use": cuse, "expectation": expect,
              "source": SRC, "filled_by": f"{LIB}; {THIS}", "inactive": 0}, f"{name}.{cname}")


# ── step 1: config ─────────────────────────────────────────────────────────────────────────────
def config(cfg: Cfg, report: list[str]) -> None:
    conn = cfg.conn
    report.append("cfg_trigger (new rule table)")
    _register_table(conn, report, "cfg_trigger", *CFG_TRIGGER_TABLE, category="rule")
    for i, col in enumerate(("database", "name")):
        _put(conn, report, "cfg_unique", {"database": "iba", "table_name": "cfg_trigger", "col": col},
             {"ordinal": i}, f"cfg_trigger.{col}")
    for kind, text in CFG_TRIGGER_PURPOSE:
        _put(conn, report, "cfg_table_purpose", {"table_name": "cfg_trigger", "kind": kind},
             {"text": text}, f"cfg_trigger {kind}")
    _put(conn, report, "cfg_write_grant", {"writer": "configmaint.propose", "table_name": "cfg_trigger",
                                           "database": "iba"}, {"inactive": 0}, "configmaint.propose")
    if not _exists(conn, "SELECT 1 FROM sqlite_master WHERE type='table' AND name='cfg_trigger'", ()):
        create_sql, index_sql = table_ddl(cfg, "cfg_trigger")
        conn.execute(create_sql)
        for s in index_sql:
            conn.execute(s)
        report.append("  table cfg_trigger created from config")
    else:
        report.append("  table cfg_trigger exists -- skipped")

    report.append("cfg_trigger: the triggers that already exist")
    br_path = PROJECT_ROOT / json.loads(conn.execute(
        "SELECT value FROM cfg_setting WHERE key='database.bible_research.path'").fetchone()[0])
    for db_key, live in (("iba", conn), ("bible_research", sqlite3.connect(f"file:{br_path}?mode=ro", uri=True))):
        for i, (name, tbl, sql) in enumerate(live.execute(
                "SELECT name, tbl_name, sql FROM sqlite_master WHERE type='trigger' AND name NOT "
                "LIKE 'trg_narrative_%' ORDER BY rowid")):
            _put(conn, report, "cfg_trigger", {"database": db_key, "name": name},
                 {"table_name": tbl, "ordinal": i, "sql": sql, "inactive": 0,
                  "use": EXISTING_TRIGGER_USE.get(name, "registered as found live, escalation #2110")},
                 f"{db_key}.{name}")
        if db_key != "iba":
            live.close()

    report.append("cfg_enum")
    for name, values in ENUMS.items():
        for i, v in enumerate(values):
            _put(conn, report, "cfg_enum", {"name": name, "value": v}, {"ordinal": i, "inactive": 0},
                 f"{name}={v}")

    report.append("cfg_setting")
    for key, value, use in SETTINGS:
        _put(conn, report, "cfg_setting", {"key": key},
             {"value": value, "use": use, "module": "narrative", "inactive": 0}, key)

    report.append("cfg_behaviour_rule")
    cls, key, text, source, enforced, status = BEHAVIOUR_RULE
    _put(conn, report, "cfg_behaviour_rule", {"rule_key": key},
         {"class": cls, "rule_text": text, "source": source, "enforced_by": enforced,
          "added_at": "2026-10-13T00:00:00Z", "active": 1, "enforcement_status": status}, key)

    report.append("cfg_work_package / cfg_step / cfg_on_fail / cfg_report / cfg_write_grant")
    _put(conn, report, "cfg_work_package", {"name": WP},
         {"ps_script": PS, "runs_over": "none", "chained": 0, "complete_message": None,
          "next_step_hint": None, "paused_message": None, "inactive": 0}, WP)
    for ordinal, (action, does, writes) in enumerate(STEPS):
        step = f"narrative_register.{action}"
        _put(conn, report, "cfg_step", {"work_package": WP, "step": step},
             {"ordinal": ordinal, "handler": f"iba.app.handlers.narrativeregister:{action}",
              "scope": "none", "does": f"{does} -- see lib/narrativeregister.py (escalation #2110)",
              "inactive": 0, "kind": "utility"}, step)
        _put(conn, report, "cfg_on_fail", {"step": step, "condition": "refused"},
             {"path": "report-continue", "resolver": None, "inactive": 0, "route": "terminal",
              "message": "refused, nothing written -- the reason follows (a usage outcome, not "
                         "recorded as an escalation)"}, f"{step}/refused")
        if action in REPORT_STEPS:
            _put(conn, report, "cfg_report", {"step": step},
                 {"title": REPORT_STEPS[action], "show_toc": 0, "footer_text": None,
                  "output_kind": "md", "naming_scheme": "dated", "archive_dir": "archive",
                  "inactive": 0}, step)
        for t in writes:
            _put(conn, report, "cfg_write_grant", {"writer": step, "table_name": t, "database": "iba"},
                 {"inactive": 0}, f"{step} -> {t}")
    for t in TABLES:
        _put(conn, report, "cfg_write_grant", {"writer": "migration", "table_name": t, "database": "iba"},
             {"inactive": 0}, f"migration -> {t}")

    report.append("cfg_utility")
    utilities = [
        ("narrativeregister", LIB,
         "narrativeregister.py -- the narrative claim register in iba.db (escalation #2110): the "
         "reference parser and book-alias map, the register actions (AddClaim, Edit, Tell, Untell, "
         "Withdraw, EditNote, EditChapter, EditSection, Record, Find, History, Check) and Export of "
         "the three published files. See USER-GUIDE.md and GOVERNANCE.md for #2110.", 0, 0, None),
        ("handlers_narrativeregister", HANDLER,
         "handlers/narrativeregister.py -- the run.py handlers for work package narrative-register "
         "(one per Narrative-Register.ps1 action); the logic is in lib/narrativeregister.py "
         "(escalation #2110).", 0, 0, None),
        ("Narrative-Register.ps1", PS,
         "PS entry point for the narrative claim register (escalation #2110); every action "
         "dispatches through run.py, work package narrative-register.", 0, 1,
         "thin wrapper; config is read by the handlers through run.py"),
        ("narrative_claim_register_config_v1_20261013", THIS,
         "ONE-OFF migration -- escalation #2110, build steps 1 and 2: config (cfg_trigger new; "
         "enums, settings, behaviour rule, work package narrative-register, steps, grants, on_fail, "
         "reports, utilities) and schema (11 narrative_* tables, indexes, 19 history triggers, all "
         "from config through lib/db.py), every cfg_* write through configmaint.apply_logged under "
         "run_id DEVMODE-2110-CONFIG-20261013. inactive=1 once applied -- a one-off, not a reusable "
         "routine.", 1, 0, None),
        ("narrative_claim_register_import_v1_20261013",
         "iba/app/migration/narrative_claim_register_import_v1_20261013.py",
         "ONE-OFF import -- escalation #2110, build steps 6 and 7 (spec sec6): --preview reads the claim "
         "register v1-v51 (R1), its 53 dated sections (R2), the narrative index (R3), the imputed-readings "
         "audit (R5) and digest sec4 (R6), plus the current chapter headings and citations, and writes the "
         "preview JSON/md and the review list beside the specification -- no DB write. --apply "
         "--preview-file imports the APPROVED preview as it stands (writer migration), once; it refuses a "
         "second run. Applied 2026-10-13 (researcher: \"process the import\"): 81 claims, 129 updates, "
         "35 chapters, 347 sections, 6,267 citations. inactive=1 once applied.", 1, 0, None),
    ]
    for module, path, purpose, inactive, exempt, reason in utilities:
        _put(conn, report, "cfg_utility", {"module": module},
             {"file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt,
              "config_exempt_reason": reason, "crash_escalation_reviewed": 0,
              "crash_escalation_note": None}, module)


# ── step 2: schema ─────────────────────────────────────────────────────────────────────────────
def schema(cfg: Cfg, report: list[str]) -> None:
    conn = cfg.conn
    report.append("cfg_table / cfg_column / cfg_unique / cfg_index / cfg_trigger for the 11 tables")
    for name, (grain, use, cols) in TABLES.items():
        _register_table(conn, report, name, grain, use, cols, category="data")
        for i, col in enumerate(CFG_UNIQUE.get(name, [])):
            _put(conn, report, "cfg_unique", {"database": "iba", "table_name": name, "col": col},
                 {"ordinal": i}, f"{name}.{col}")
        for c in cols:
            if c[6]:   # every FK column gets an index, idx_{table}_{col}
                _put(conn, report, "cfg_index", {"table_name": name, "name": f"idx_{name}_{c[0]}"},
                     {"col": c[0], "ordinal": 0}, f"idx_{name}_{c[0]}")
    per_table: dict[str, int] = {}
    for table, name, sql, use in TRIGGERS:
        row = {"table_name": table, "ordinal": per_table.setdefault(table, 0), "sql": sql,
               "use": f"{use} -- escalation #2110", "inactive": 0}
        cur = conn.execute("SELECT sql, use FROM cfg_trigger WHERE database='iba' AND name=?",
                           (name,)).fetchone()
        if cur and (cur[0] != sql or cur[1] != row["use"]):
            # a corrected trigger: the config row is updated (audited) and the live trigger is
            # dropped here, to be recreated from config below
            apply_logged(conn, RUN_ID, "cfg_trigger", "update", {"database": "iba", "name": name},
                         {"sql": sql, "use": row["use"]})
            conn.execute(f'DROP TRIGGER IF EXISTS "{name}"')
            report.append(f"  cfg_trigger {name}: updated (sql or use changed) -- live trigger rebuilt")
        else:
            _put(conn, report, "cfg_trigger", {"database": "iba", "name": name}, row, name)
        per_table[table] += 1

    report.append("tables, indexes, triggers -- from config (lib/db.py)")
    for name in TABLES:
        if _exists(conn, "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)):
            report.append(f"  table {name} exists -- skipped")
            continue
        create_sql, index_sql = table_ddl(cfg, name)
        conn.execute(create_sql)
        for s in index_sql:
            conn.execute(s)
        report.append(f"  table {name} created ({len(index_sql)} index(es))")
    for name in TABLES:
        for sql in trigger_ddl(cfg, name):
            conn.execute(sql.replace("CREATE TRIGGER ", "CREATE TRIGGER IF NOT EXISTS ", 1))
    report.append(f"  triggers ensured: {len(TRIGGERS)}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DB_PATH))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    cfg = Cfg(pathlib.Path(args.db))
    conn = cfg.conn
    conn.isolation_level = None          # explicit transaction control
    report: list[str] = [f"db: {args.db}", f"run_id: {RUN_ID}"]
    try:
        conn.execute("BEGIN")
        before = conn.execute("SELECT COUNT(*) FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone()[0]
        config(cfg, report)
        schema(cfg, report)
        written = conn.execute("SELECT COUNT(*) FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone()[0] - before
        if args.dry_run:
            conn.execute("ROLLBACK")
            report.append(f"DRY RUN -- {written} cfg_* row(s) would be written; rolled back")
        elif written == 0 and not any(r.endswith(("created", "inserted")) or " created (" in r
                                      or "rebuilt" in r or ": updated" in r for r in report):
            conn.execute("ROLLBACK")
            report.append("nothing to write -- every row already current")
        else:
            conn.execute("COMMIT")
            report.append(f"committed under {RUN_ID}: {written} cfg_* row(s) written")
    except Exception:
        conn.execute("ROLLBACK")
        raise
    finally:
        cfg.close()
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
