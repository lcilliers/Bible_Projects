"""
_extract_word_terms.py
──────────────────────
Phase 2 — Word Term Extraction  (full CRUD sync)

Reads the decisions JSON produced by _apply_term_decisions.py and
synchronises the database so its state exactly matches the triage decisions:

  INCLUDE terms
    • Upsert wa_term_inventory          (STEP fields overwritten; researcher
                                         fields preserved on UPDATE)
    • Replace wa_term_related_words     (delete-all + re-insert)
    • Replace wa_term_root_family       (delete-all + re-insert from cluster)
    • Re-run meaning parser             (idempotent; rebuilds wa_meaning_parsed,
                                         wa_meaning_sense, wa_meaning_stem,
                                         wa_lsj_parsed; updates parsed_meaning_id)
    • Fetch verse records from STEP     (fully paginated)

  EXCLUDE terms (any action != 'include')
    • Cascade-delete all dependent rows (wa_verse_term_links, meaning chain,
                                         wa_term_related_words, wa_term_root_family)
    • Delete wa_term_inventory row

  VERSE RECORDS (deduped globally across all include terms)
    • Upsert wa_verse_records           (keyed on file_id + book_id + chapter + verse_num)
    • Rebuild wa_verse_term_links       (junction table; cleared then re-inserted)
    • Delete orphaned wa_verse_records  (rows with no remaining junction links)

NOTE: wa_term_phase2_flags is NOT touched — owned exclusively by audit_word.py.
NOTE: Researcher fields in wa_term_inventory that are preserved:
        word_analysis_gloss, god_as_subject, somatic_link, status_note

Usage:
  python scripts/_extract_word_terms.py \\
      --decisions data/discovery/soul_term_decisions_20260323.json

  # Dry run (no DB writes, API calls still made)
  python scripts/_extract_word_terms.py \\
      --decisions data/discovery/soul_term_decisions_20260323.json --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, datetime, timezone

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from analytics.step_client import StepClient
from engine.db import get_connection, get_book_id
from engine.meaning_parser import run_parser


# ── Helpers ────────────────────────────────────────────────────────────────


def p(msg: str = "") -> None:
    print(msg, flush=True)


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")


def _today() -> str:
    return date.today().strftime("%Y%m%d")


def _lang(code: str) -> str:
    return "Greek" if code.startswith("G") else "Hebrew"


# ── Junction table creation ────────────────────────────────────────────────


_CREATE_JUNCTION_SQL = """
CREATE TABLE IF NOT EXISTS wa_verse_term_links (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    verse_id            INTEGER NOT NULL REFERENCES wa_verse_records(id) ON DELETE CASCADE,
    term_inv_id         INTEGER NOT NULL REFERENCES wa_term_inventory(id) ON DELETE CASCADE,
    step_subgloss_code  TEXT,
    step_subgloss_label TEXT,
    span_strong_match   INTEGER,
    target_word         TEXT,
    created_at          TEXT DEFAULT (strftime('%Y-%m-%dT%H:%M:%S','now')),
    UNIQUE (verse_id, term_inv_id)
);
CREATE INDEX IF NOT EXISTS idx_vtl_verse ON wa_verse_term_links (verse_id);
CREATE INDEX IF NOT EXISTS idx_vtl_term  ON wa_verse_term_links (term_inv_id);
"""


def ensure_junction_table(conn) -> None:
    for stmt in _CREATE_JUNCTION_SQL.strip().split(";"):
        s = stmt.strip()
        if s:
            conn.execute(s)
    conn.commit()
    p("  [schema] wa_verse_term_links ensured")


# ── File ID resolution ─────────────────────────────────────────────────────


def find_file_id(conn, english_word: str) -> int:
    """Return the most recent wa_file_index.id for this word study.

    Raises RuntimeError if no file record exists — the word study must have
    been registered via audit_word.py or the new pipeline before extraction.
    """
    reg = conn.execute(
        "SELECT id FROM word_registry WHERE LOWER(word) = LOWER(?)",
        (english_word,),
    ).fetchone()
    if not reg:
        raise RuntimeError(
            f"No word_registry entry found for word='{english_word}'. "
            "Register the word study first."
        )
    registry_pk = reg["id"]

    file_row = conn.execute(
        "SELECT id FROM wa_file_index WHERE word_registry_fk = ? ORDER BY id DESC LIMIT 1",
        (registry_pk,),
    ).fetchone()
    if not file_row:
        raise RuntimeError(
            f"No wa_file_index entry found for word='{english_word}' "
            f"(word_registry.id={registry_pk}). Create the file record first."
        )
    return file_row["id"]


# ── Excluded term purge ────────────────────────────────────────────────────


def purge_excluded_term(conn, file_id: int, strongs_number: str) -> bool:
    """Delete all DB rows for a term that is excluded by the triage.

    Safe to call even if the term is not in the DB (returns False then).
    Cascade order:
      1. wa_verse_term_links (via term_inv_id)
      2. wa_meaning_sense / wa_meaning_stem / wa_lsj_parsed (via wa_meaning_parsed)
      3. wa_meaning_parsed
      4. wa_term_related_words
      5. wa_term_root_family
      6. wa_term_inventory
    Orphaned verse records are handled globally after all terms are processed.
    """
    row = conn.execute(
        "SELECT id, parsed_meaning_id FROM wa_term_inventory "
        "WHERE file_id = ? AND strongs_number = ?",
        (file_id, strongs_number),
    ).fetchone()
    if not row:
        return False

    term_inv_id = row["id"]
    parsed_id = row["parsed_meaning_id"]

    conn.execute("DELETE FROM wa_verse_term_links WHERE term_inv_id = ?", (term_inv_id,))

    if parsed_id:
        conn.execute("DELETE FROM wa_meaning_sense WHERE parsed_meaning_id = ?", (parsed_id,))
        conn.execute("DELETE FROM wa_meaning_stem  WHERE parsed_meaning_id = ?", (parsed_id,))
    conn.execute("DELETE FROM wa_lsj_parsed    WHERE term_inv_id = ?", (term_inv_id,))
    conn.execute("DELETE FROM wa_meaning_parsed WHERE term_inv_id = ?", (term_inv_id,))
    conn.execute("DELETE FROM wa_term_related_words WHERE term_inv_id = ?", (term_inv_id,))
    conn.execute("DELETE FROM wa_term_root_family   WHERE term_inv_id = ?", (term_inv_id,))
    conn.execute("DELETE FROM wa_term_inventory WHERE id = ?", (term_inv_id,))
    return True


# ── Term inventory upsert ──────────────────────────────────────────────────


# Researcher-owned fields — these are NEVER overwritten on UPDATE.
_RESEARCHER_FIELDS = {"word_analysis_gloss", "god_as_subject", "somatic_link", "status_note"}


def upsert_term_inventory(conn, file_id: int, term: dict, vocab: dict) -> int:
    """Insert or update a row in wa_term_inventory.

    Keyed on (file_id, strongs_number).
    On INSERT: researcher fields default to NULL.
    On UPDATE: researcher fields are left unchanged; all STEP fields overwritten.

    Returns the term_inv_id.
    """
    strongs = vocab.get("strong_number") or term["code"]
    lang = vocab.get("language") or _lang(term["code"])
    now = _now()

    # Derive testament from language
    testament = "NT" if lang == "Greek" else "OT"

    existing = conn.execute(
        "SELECT id FROM wa_term_inventory WHERE file_id = ? AND strongs_number = ?",
        (file_id, strongs),
    ).fetchone()

    if existing:
        term_inv_id = existing["id"]
        conn.execute(
            """UPDATE wa_term_inventory SET
                language              = ?,
                term_id               = ?,
                strongs_number        = ?,
                transliteration       = ?,
                step_search_gloss     = ?,
                occurrence_count      = ?,
                meaning               = ?,
                meaning_numbered      = ?,
                lsj_entry             = ?,
                testament             = ?,
                short_def_mounce      = ?,
                causative_form_present = ?,
                last_changed          = ?
               WHERE id = ?""",
            (
                lang,
                strongs,
                strongs,
                vocab.get("transliteration", ""),
                vocab.get("gloss", ""),
                vocab.get("occurrence_count", 0),
                vocab.get("medium_def", ""),
                "1" if vocab.get("meaning_numbered") else "0",
                vocab.get("lsj_entry", ""),
                testament,
                vocab.get("short_def_mounce", ""),
                1 if vocab.get("causative_form_present") else 0,
                now,
                term_inv_id,
            ),
        )
    else:
        # MAX(id)+1 to avoid autoincrement gaps in a busy transaction
        next_id = conn.execute("SELECT MAX(id) FROM wa_term_inventory").fetchone()[0] or 0
        next_id += 1
        conn.execute(
            """INSERT INTO wa_term_inventory
               (id, file_id, language, term_id, strongs_number, transliteration,
                step_search_gloss, occurrence_count, meaning, meaning_numbered,
                lsj_entry, testament, short_def_mounce, causative_form_present,
                last_changed)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                next_id, file_id, lang, strongs, strongs,
                vocab.get("transliteration", ""),
                vocab.get("gloss", ""),
                vocab.get("occurrence_count", 0),
                vocab.get("medium_def", ""),
                "1" if vocab.get("meaning_numbered") else "0",
                vocab.get("lsj_entry", ""),
                testament,
                vocab.get("short_def_mounce", ""),
                1 if vocab.get("causative_form_present") else 0,
                now,
            ),
        )
        term_inv_id = next_id

    return term_inv_id


# ── Related words ──────────────────────────────────────────────────────────


def replace_related_words(conn, term_inv_id: int, vocab: dict) -> int:
    """Delete-all + re-insert wa_term_related_words for one term."""
    conn.execute("DELETE FROM wa_term_related_words WHERE term_inv_id = ?", (term_inv_id,))
    count = 0
    for rw in vocab.get("related_words", []):
        strong = rw.get("strong", "")
        if not strong:
            continue
        conn.execute(
            """INSERT INTO wa_term_related_words
               (term_inv_id, gloss, transliteration, strongs_number, relationship_note)
               VALUES (?, ?, ?, ?, ?)""",
            (
                term_inv_id,
                rw.get("gloss", ""),
                rw.get("translit", ""),
                strong,
                "STEP relatedNos",
            ),
        )
        count += 1
    return count


# ── Root family ────────────────────────────────────────────────────────────


def replace_root_family(conn, term_inv_id: int, term: dict, vocab: dict) -> int:
    """Delete-all + re-insert wa_term_root_family for one term.

    Root data is derived from the decisions JSON cluster structure:
      - sub_gloss terms:   root = step_parent_code (the primary sub-gloss base)
      - related_term:      root = step_parent_code (the primary that pulled it in)
      - primary:           if the term IS a root (e.g. H5314), record itself as root
    """
    conn.execute("DELETE FROM wa_term_root_family WHERE term_inv_id = ?", (term_inv_id,))

    parent_code = term.get("step_parent_code", "")
    section_type = term.get("step_section_type", "")
    code = term["code"]
    lang = _lang(code)

    # Determine root_code and root_gloss
    if section_type == "primary":
        # This IS the root form; record a self-reference note
        root_code = code
        root_gloss = vocab.get("gloss", "")
        note = "primary code — self-reference"
    elif parent_code and parent_code != code:
        root_code = parent_code
        root_gloss = ""       # parent gloss not available here without extra API call
        note = f"derived from STEP cluster parent ({section_type})"
    else:
        # Fallback: record the code itself
        root_code = code
        root_gloss = vocab.get("gloss", "")
        note = "auto-populated from STEP term cluster discovery"

    conn.execute(
        """INSERT INTO wa_term_root_family
           (term_inv_id, root_code, root_language, root_gloss, note)
           VALUES (?, ?, ?, ?, ?)""",
        (term_inv_id, root_code, lang, root_gloss, note),
    )
    return 1


# ── Verse record upsert ────────────────────────────────────────────────────


def upsert_verse_record(
    conn,
    file_id: int,
    verse: dict,
    primary_term_inv_id: int,
    primary_vocab: dict,
) -> int:
    """Insert or update a row in wa_verse_records.

    Keyed on (file_id, book_id, chapter, verse_num).
    The primary_term_inv_id is the first include-term that matched this verse
    (preserved for backward compatibility; full relationship in wa_verse_term_links).

    Returns the verse_id.
    """
    book_code = verse["book_code"]
    book_id = get_book_id(conn, book_code)
    chapter = verse["chapter"]
    verse_num = verse["verse_num"]
    now = _now()

    target_word = verse.get("target_word", "")
    span_match = 1 if target_word else None

    existing = conn.execute(
        "SELECT id FROM wa_verse_records "
        "WHERE file_id = ? AND book_id = ? AND chapter = ? AND verse_num = ?",
        (file_id, book_id, chapter, verse_num),
    ).fetchone()

    if existing:
        verse_id = existing["id"]
        conn.execute(
            """UPDATE wa_verse_records SET
                term_inv_id       = ?,
                term_id           = ?,
                transliteration   = ?,
                testament         = ?,
                reference         = ?,
                verse_text        = ?,
                book_id           = ?,
                chapter           = ?,
                verse_num         = ?,
                translation       = 'ESV',
                target_word       = ?,
                span_strong_match = ?,
                last_changed      = ?
               WHERE id = ?""",
            (
                primary_term_inv_id,
                primary_vocab.get("strong_number", ""),
                primary_vocab.get("transliteration", ""),
                verse["testament"],
                verse["ref"],
                verse["esv_text"],
                book_id,
                chapter,
                verse_num,
                target_word,
                span_match,
                now,
                verse_id,
            ),
        )
    else:
        next_id = conn.execute("SELECT MAX(id) FROM wa_verse_records").fetchone()[0] or 0
        next_id += 1
        conn.execute(
            """INSERT INTO wa_verse_records
               (id, file_id, term_inv_id, term_id, transliteration, testament,
                reference, verse_text, book_id, chapter, verse_num, translation,
                target_word, span_strong_match, last_changed, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'ESV', ?, ?, ?, ?)""",
            (
                next_id, file_id,
                primary_term_inv_id,
                primary_vocab.get("strong_number", ""),
                primary_vocab.get("transliteration", ""),
                verse["testament"],
                verse["ref"],
                verse["esv_text"],
                book_id,
                chapter,
                verse_num,
                target_word,
                span_match,
                now,
                now,
            ),
        )
        verse_id = next_id

    return verse_id


# ── Junction link insert ───────────────────────────────────────────────────


def insert_verse_term_link(
    conn,
    verse_id: int,
    term_inv_id: int,
    term: dict,
    verse: dict,
) -> None:
    """Insert a row into wa_verse_term_links (INSERT OR IGNORE for safety)."""
    conn.execute(
        """INSERT OR IGNORE INTO wa_verse_term_links
           (verse_id, term_inv_id, step_subgloss_code, step_subgloss_label,
            span_strong_match, target_word, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (
            verse_id,
            term_inv_id,
            term["code"],
            term.get("gloss", ""),
            1 if verse.get("target_word") else None,
            verse.get("target_word", ""),
            _now(),
        ),
    )


# ── Summary writer ─────────────────────────────────────────────────────────


def write_summary(
    output_dir: str,
    word: str,
    stats: dict,
    dry_run: bool,
) -> str:
    today = _today()
    suffix = "_dryrun" if dry_run else ""
    path = os.path.join(output_dir, f"{word}_extraction_{today}{suffix}.md")

    lines = [
        f"# Phase 2 Extraction — \"{word}\"",
        "",
        f"Run date: {stats['run_at']}  |  Dry run: {'YES' if dry_run else 'no'}",
        "",
        "## Term Inventory",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Terms in decisions JSON (include) | {stats['include_count']} |",
        f"| Terms purged (exclude/review) | {stats['purge_count']} |",
        f"| Terms inserted (new) | {stats['terms_inserted']} |",
        f"| Terms updated (existing) | {stats['terms_updated']} |",
        f"| STEP API vocab calls | {stats['vocab_calls']} |",
        f"| STEP API verse calls | {stats['verse_calls']} |",
        "",
        "## Verse Records",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Total verse-term pairs fetched | {stats['verse_term_pairs']} |",
        f"| Unique verses (deduped) | {stats['unique_verses']} |",
        f"| Verse records inserted | {stats['verses_inserted']} |",
        f"| Verse records updated | {stats['verses_updated']} |",
        f"| Verse records orphaned + deleted | {stats['verses_deleted']} |",
        f"| Junction links written | {stats['links_written']} |",
        "",
        "## Per-Term Verse Counts",
        "",
        "| code | gloss | lang | verses_fetched |",
        "|------|-------|------|---------------|",
    ]
    for code, gloss, lang, vc in stats["per_term"]:
        lines.append(f"| {code} | {gloss} | {lang} | {vc} |")

    lines += [""]

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return path


# ── Main ───────────────────────────────────────────────────────────────────


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        description="Phase 2 — full CRUD sync of word term data to the database"
    )
    ap.add_argument(
        "--decisions", required=True,
        help="Path to soul_term_decisions_YYYYMMDD.json from _apply_term_decisions.py",
    )
    ap.add_argument(
        "--dry-run", action="store_true",
        help="Fetch all data and report counts but do NOT write to the database",
    )
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    dry_run = args.dry_run

    # ── Load decisions ─────────────────────────────────────────────────────
    decisions_path = os.path.abspath(args.decisions)
    if not os.path.exists(decisions_path):
        p(f"ERROR: decisions file not found: {decisions_path}")
        sys.exit(1)

    with open(decisions_path, encoding="utf-8") as f:
        decisions = json.load(f)

    english_word = decisions["meta"]["english_anchor"]
    include_terms = [t for t in decisions["terms"] if t["action"] == "include"]
    exclude_terms = [t for t in decisions["terms"] if t["action"] != "include"]
    include_codes = {t["code"] for t in include_terms}

    p()
    p(f"=== Phase 2 Extraction — '{english_word}' ===")
    p(f"  Decisions file : {os.path.basename(decisions_path)}")
    p(f"  Include terms  : {len(include_terms)}")
    p(f"  Exclude terms  : {len(exclude_terms)}")
    p(f"  Dry run        : {'YES' if dry_run else 'no'}")
    p()

    # ── Connect ────────────────────────────────────────────────────────────
    conn = get_connection()
    conn.execute("PRAGMA foreign_keys = OFF")  # manual cascade — FKs may be unregistered

    # ── Ensure junction table ──────────────────────────────────────────────
    p("[0] Ensuring wa_verse_term_links table...")
    if not dry_run:
        ensure_junction_table(conn)
    else:
        p("  [dry-run] skip")

    # ── Resolve file_id ────────────────────────────────────────────────────
    p(f"[1] Resolving file_id for '{english_word}'...")
    file_id = find_file_id(conn, english_word)
    p(f"  file_id = {file_id}")
    p()

    # ── Purge excluded terms ───────────────────────────────────────────────
    p(f"[2] Purging excluded terms ({len(exclude_terms)} candidates)...")
    purge_count = 0
    for t in exclude_terms:
        if not dry_run:
            removed = purge_excluded_term(conn, file_id, t["code"])
        else:
            row = conn.execute(
                "SELECT id FROM wa_term_inventory WHERE file_id = ? AND strongs_number = ?",
                (file_id, t["code"]),
            ).fetchone()
            removed = row is not None
        if removed:
            purge_count += 1
            p(f"  purged  {t['code']:12s}  {t.get('gloss', '')}")
    p(f"  → {purge_count} term rows removed from DB")
    p()

    # ── Process included terms ─────────────────────────────────────────────
    p(f"[3] Processing {len(include_terms)} include terms (STEP API + DB upsert)...")
    client = StepClient()
    term_inv_map: dict[str, int] = {}     # code → term_inv_id
    vocab_map: dict[str, dict] = {}        # code → vocab
    terms_inserted = 0
    terms_updated = 0
    vocab_calls = 0

    for i, term in enumerate(include_terms, 1):
        code = term["code"]
        p(f"  [{i:02d}/{len(include_terms)}] {code:12s}  {term.get('gloss', '')}")

        # Fetch vocab from STEP
        vocab = client.get_vocab_info(code)
        vocab_calls += 1
        if not vocab:
            p(f"    WARNING: no vocab returned for {code} — skipping")
            continue

        if dry_run:
            # In dry-run, check whether insert or update would occur
            existing = conn.execute(
                "SELECT id FROM wa_term_inventory WHERE file_id = ? AND strongs_number = ?",
                (file_id, vocab.get("strong_number") or code),
            ).fetchone()
            if existing:
                terms_updated += 1
                term_inv_map[code] = existing["id"]
            else:
                terms_inserted += 1
                term_inv_map[code] = -1  # placeholder
            vocab_map[code] = vocab
            continue

        # Check before upsert so we can track insert vs update
        existing_check = conn.execute(
            "SELECT id FROM wa_term_inventory WHERE file_id = ? AND strongs_number = ?",
            (file_id, vocab.get("strong_number") or code),
        ).fetchone()

        term_inv_id = upsert_term_inventory(conn, file_id, term, vocab)
        vocab_map[code] = vocab
        term_inv_map[code] = term_inv_id

        if existing_check:
            terms_updated += 1
        else:
            terms_inserted += 1

        # Related words
        rw_count = replace_related_words(conn, term_inv_id, vocab)

        # Root family
        replace_root_family(conn, term_inv_id, term, vocab)

        # Meaning parser (idempotent)
        run_parser(conn, term_inv_id, vocab)

        p(f"    term_inv_id={term_inv_id}  related_words={rw_count}")

    p(f"  → {terms_inserted} inserted, {terms_updated} updated")
    p()

    # ── Fetch verse records ────────────────────────────────────────────────
    p(f"[4] Fetching verse records from STEP ({len(include_terms)} codes)...")

    # verse_pool[osis_id] = {"verse": record, "terms": [(code, term_inv_id), ...]}
    verse_pool: dict[str, dict] = {}
    per_term_stats: list[tuple] = []
    verse_calls = 0

    for i, term in enumerate(include_terms, 1):
        code = term["code"]
        if code not in term_inv_map:
            continue  # was skipped due to empty vocab
        p(f"  [{i:02d}/{len(include_terms)}] {code:12s} — fetching verses...")
        records = client.get_verse_records(code)
        verse_calls += 1
        p(f"    {len(records)} verses")
        per_term_stats.append((code, term.get("gloss", ""), _lang(code), len(records)))

        for verse in records:
            osis = verse["osisId"]
            if osis not in verse_pool:
                verse_pool[osis] = {"verse": verse, "terms": []}
            verse_pool[osis]["terms"].append((code, term_inv_map[code]))

    unique_verses = len(verse_pool)
    verse_term_pairs = sum(len(v["terms"]) for v in verse_pool.values())
    p(f"  → {unique_verses} unique verses, {verse_term_pairs} verse-term pairs")
    p()

    if dry_run:
        p("[5] Dry-run: skipping DB verse writes")
        verses_inserted = verses_updated = verses_deleted = links_written = 0
    else:
        # ── Clear junction links for this file ────────────────────────────
        p("[5] Clearing existing junction links for this word study...")
        conn.execute(
            "DELETE FROM wa_verse_term_links "
            "WHERE verse_id IN (SELECT id FROM wa_verse_records WHERE file_id = ?)",
            (file_id,),
        )

        # ── Upsert verse records ──────────────────────────────────────────
        p("[6] Upserting verse records...")
        verses_inserted = 0
        verses_updated = 0
        verse_id_map: dict[str, int] = {}  # osis_id → verse_id

        for osis, entry in verse_pool.items():
            verse = entry["verse"]
            # Primary term = first in the ordered include list
            primary_code, primary_term_inv_id = entry["terms"][0]
            primary_vocab = vocab_map.get(primary_code, {})

            existing_check = conn.execute(
                "SELECT id FROM wa_verse_records "
                "WHERE file_id = ? AND book_id = ? AND chapter = ? AND verse_num = ?",
                (
                    file_id,
                    get_book_id(conn, verse["book_code"]),
                    verse["chapter"],
                    verse["verse_num"],
                ),
            ).fetchone()

            verse_id = upsert_verse_record(
                conn, file_id, verse, primary_term_inv_id, primary_vocab
            )
            verse_id_map[osis] = verse_id

            if existing_check:
                verses_updated += 1
            else:
                verses_inserted += 1

        p(f"  → {verses_inserted} inserted, {verses_updated} updated")

        # ── Insert junction links ─────────────────────────────────────────
        p("[7] Inserting verse-term junction links...")
        links_written = 0
        for osis, entry in verse_pool.items():
            verse = entry["verse"]
            verse_id = verse_id_map[osis]
            for code, term_inv_id in entry["terms"]:
                term_def = next((t for t in include_terms if t["code"] == code), {})
                insert_verse_term_link(conn, verse_id, term_inv_id, term_def, verse)
                links_written += 1
        p(f"  → {links_written} links written")

        # ── Delete orphaned verse records ─────────────────────────────────
        p("[8] Deleting orphaned verse records (from previous runs, no links remaining)...")
        conn.execute(
            """DELETE FROM wa_verse_records
               WHERE file_id = ?
               AND id NOT IN (SELECT DISTINCT verse_id FROM wa_verse_term_links)""",
            (file_id,),
        )
        deleted_cursor = conn.execute("SELECT changes()").fetchone()
        verses_deleted = deleted_cursor[0] if deleted_cursor else 0
        p(f"  → {verses_deleted} orphaned verse records deleted")

        # ── Commit ────────────────────────────────────────────────────────
        p("[9] Committing transaction...")
        conn.commit()
        p("  committed.")

    conn.close()
    p()

    # ── Write summary ──────────────────────────────────────────────────────
    stats = {
        "run_at":          _now(),
        "include_count":   len(include_terms),
        "purge_count":     purge_count,
        "terms_inserted":  terms_inserted,
        "terms_updated":   terms_updated,
        "vocab_calls":     vocab_calls,
        "verse_calls":     verse_calls,
        "verse_term_pairs": verse_term_pairs,
        "unique_verses":   unique_verses,
        "verses_inserted": verses_inserted,
        "verses_updated":  verses_updated,
        "verses_deleted":  verses_deleted,
        "links_written":   links_written,
        "per_term":        per_term_stats,
    }

    output_dir = os.path.join(_ROOT, "data", "discovery")
    summary_path = write_summary(output_dir, english_word, stats, dry_run)
    p(f"Summary written → {summary_path}")
    p()
    p("=== Done ===")


if __name__ == "__main__":
    main()
