"""_apply_finding_verse_term_index_v1_20260829.py

Researcher-directed 2026-08-29 (following the finding-tables landscape review and the
verse_context_id/mti_term_id index analysis, outputs/escalation/1007-finding-fk-columns-index-
analysis-20260829.md and .../1007-finding-verse-term-index-plan-20260829.md):

1. Creates `finding_verse_index` (bible_research.db) -- a proper finding<->verse M:N table
   pointing DIRECTLY at `iba.verse.id`, replacing the incomplete `finding_verse_link` (only 73 of
   3,659 rows ever resolved to a real verse) and the multi-hop `verse_context`/`wa_verse_records`
   chain (both already `inactive=1` in cfg_table -- used here only as a one-time read source).
2. Pass 1 (structural): every VERSE-level finding's primary verse, resolved via
   verse_context.verse_record_id -> wa_verse_records.id -> wa_verse_records.verse_id -> iba.verse.id.
3. Pass 2: migrates finding_verse_link's own 3,659 rows, resolved via their `reference` TEXT
   (their numeric verse_record_id is confirmed unreliable) -- built via osisId, not the inconsistent
   `reference` abbreviation scheme, using a book-crosswalk verified by CANONICAL POSITION
   (bible_research.books.book_order - 1 == iba.cfg_book_order.ordinal, confirmed live, not
   string-matched) rather than trying to reconcile two different abbreviation conventions directly.
4. Term side: finding.strong_number (new TEXT column, replacing finding.mti_term_id) backfilled via
   mti_terms.strongs_number -> iba.strong.strongNumber (99.99% coverage, verified: 435,169/435,193).

Pass 3 (text-mining finding_value for embedded verse references) is SAMPLE-TESTED only by this
script (--sample-pass3 N) -- not run at full scale here, per the plan: show real match examples
before committing to all 458k rows.

Usage:
    python scripts/_apply_finding_verse_term_index_v1_20260829.py --dry-run
    python scripts/_apply_finding_verse_term_index_v1_20260829.py --live
    python scripts/_apply_finding_verse_term_index_v1_20260829.py --sample-pass3 500
"""
from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from datetime import datetime, timezone

BR_DB = "database/bible_research.db"
IBA_DB = "iba/app/db/iba.db"


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _ensure_columns(conn: sqlite3.Connection, table: str, columns: list[tuple[str, str]]) -> list[str]:
    existing = {r[1] for r in conn.execute(f"PRAGMA table_info({table})")}
    added = []
    for name, sql_type in columns:
        if name in existing:
            continue
        conn.execute(f"ALTER TABLE {table} ADD COLUMN {name} {sql_type}")
        added.append(name)
    return added


def _ensure_table(conn: sqlite3.Connection) -> None:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS finding_verse_index (
            id INTEGER PRIMARY KEY,
            finding_id INTEGER NOT NULL,
            verse_id INTEGER NOT NULL,       -- iba.verse.id (cross-database, not FK-enforced --
                                              -- same pattern wa_verse_records.verse_id already uses)
            reference_text TEXT,
            source TEXT NOT NULL,            -- structural | finding_verse_link | text_mined
            created_at TEXT
        )
    """)


def build_book_crosswalk(br_conn: sqlite3.Connection, iba_conn: sqlite3.Connection
                         ) -> dict[str, str]:
    """variant book code (any spelling in book_code_variants, plus full names) -> OSIS book code
    (cfg_book_order.book), via CANONICAL POSITION -- books.book_order - 1 == cfg_book_order.ordinal,
    verified live (both are the same 66-book Protestant-canon sequence) -- not string-matched
    against either database's own abbreviation scheme, which do NOT agree with each other
    (confirmed live: books.abbreviation gives '1Co' for 1 Corinthians, but iba.verse.reference's
    own prefix for the same book is '1Cor' -- a real mismatch, not a typo)."""
    osis_by_ordinal = dict(iba_conn.execute("SELECT ordinal, book FROM cfg_book_order"))
    order_by_id = dict(br_conn.execute("SELECT id, book_order FROM books"))
    crosswalk: dict[str, str] = {}
    for code, book_id in br_conn.execute("SELECT code, book_id FROM book_code_variants"):
        ordinal = order_by_id.get(book_id, 0) - 1
        if ordinal in osis_by_ordinal:
            crosswalk[code] = osis_by_ordinal[ordinal]
    # also index by the book's own name/full_name/abbreviation (covers "Romans", "Hebrews", etc.
    # -- found live in finding_verse_link.reference, not covered by book_code_variants alone)
    for row in br_conn.execute("SELECT id, name, abbreviation, full_name FROM books"):
        book_id, name, abbrev, full_name = row
        ordinal = order_by_id.get(book_id, 0) - 1
        osis = osis_by_ordinal.get(ordinal)
        if not osis:
            continue
        for key in (name, abbrev, full_name):
            if key:
                crosswalk[key] = osis
    return crosswalk


_REF_RE = re.compile(r"(\d?\s?[A-Za-z]+)\.?\s+(\d{1,3}):(\d{1,3})")


def extract_references(text: str) -> list[tuple[str, str, str]]:
    """Every (book_raw, chapter, verse) triple found in `text` -- a finding can name several
    verses in one paragraph (confirmed live, up to 6 in a single row), so this returns all
    matches, not just the first."""
    if not text:
        return []
    return [(m.group(1).replace(" ", ""), m.group(2), m.group(3)) for m in _REF_RE.finditer(text)]


def resolve_references(text: str, crosswalk: dict[str, str], verse_id_by_osis: dict[str, int]
                       ) -> list[tuple[int, str]]:
    """(verse_id, matched_reference_text) for every reference in `text` that resolves cleanly.
    Silently skips anything that doesn't resolve -- book not recognised or chapter:verse doesn't
    exist -- rather than guessing; the caller's own pass reports the miss rate."""
    out = []
    for book_raw, ch, vs in extract_references(text):
        osis_book = crosswalk.get(book_raw)
        if not osis_book:
            continue
        osis_id = f"{osis_book}.{ch}.{vs}"
        vid = verse_id_by_osis.get(osis_id)
        if vid:
            out.append((vid, f"{book_raw} {ch}:{vs}"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--sample-pass3", type=int, default=0,
                    help="sample-test the text-mining pass against N findings, report only, no writes")
    ap.add_argument("--pass3-live", action="store_true",
                    help="run the text-mining pass at full scale (all findings), deduplicated "
                        "against every existing finding_verse_index row")
    ap.add_argument("--fix-pass1", action="store_true",
                    help="purge all source='structural' rows (built via the broken wa_verse_"
                        "records.verse_id bridge, confirmed wrong for every row) and rebuild "
                        "Pass 1 via the corrected reference-text resolution. Report-only unless --live.")
    a = ap.parse_args()
    if not a.sample_pass3 and not a.pass3_live and not a.fix_pass1 and a.dry_run == a.live:
        print("pass exactly one of --dry-run or --live, or use --sample-pass3 N / --pass3-live")
        return 1

    br = sqlite3.connect(BR_DB)
    iba = sqlite3.connect(IBA_DB)
    live = a.live

    crosswalk = build_book_crosswalk(br, iba)
    verse_id_by_osis = dict(iba.execute("SELECT osisId, id FROM verse"))
    print(f"book crosswalk: {len(crosswalk)} entries; iba.verse loaded: {len(verse_id_by_osis)} rows")
    now = _now()

    if a.pass3_live:
        # Dedup, researcher instruction 2026-08-29: never insert a (finding_id, verse_id) pair
        # that already exists -- loaded once, in-memory, rather than a per-row SELECT (same class
        # of performance bug fixed earlier today in the cluster_finding migration).
        existing_pairs = set(br.execute("SELECT finding_id, verse_id FROM finding_verse_index"))
        print(f"existing (finding_id, verse_id) pairs loaded for dedup: {len(existing_pairs)}")
        rows = br.execute("SELECT id, finding_value FROM finding").fetchall()
        to_insert = []
        seen_this_pass = set()   # a finding whose text names the same verse twice in one pass
                                 # (a common pattern -- confirmed live, e.g. one finding cites
                                 # 'Job 16:4' twice in different paragraphs) must not double-insert
        for fid, text in rows:
            for vid, ref_text in resolve_references(text or "", crosswalk, verse_id_by_osis):
                key = (fid, vid)
                if key in existing_pairs or key in seen_this_pass:
                    continue
                seen_this_pass.add(key)
                to_insert.append((fid, vid, ref_text, now))
        print(f"Pass 3 (text-mining, full scale): {len(rows)} findings scanned, "
             f"{len(to_insert)} NEW finding_verse_index rows to insert (duplicates against "
             f"existing rows and within this pass both excluded)")
        if live:
            br.executemany(
                "INSERT INTO finding_verse_index (finding_id, verse_id, reference_text, source, "
                "created_at) VALUES (?, ?, ?, 'text_mined', ?)", to_insert)
            br.commit()
            print("committed")
        else:
            print("(pass3-live requires --live to actually write -- report only, nothing written)")
        return 0

    if a.sample_pass3:
        rows = br.execute(
            "SELECT id, finding_value FROM finding ORDER BY id LIMIT ?", (a.sample_pass3,)).fetchall()
        total_refs, resolved_refs, findings_with_any = 0, 0, 0
        examples = []
        for fid, text in rows:
            found = resolve_references(text or "", crosswalk, verse_id_by_osis)
            raw = extract_references(text or "")
            total_refs += len(raw)
            resolved_refs += len(found)
            if found:
                findings_with_any += 1
            if found and len(examples) < 8:
                examples.append((fid, found[:3]))
        print(f"sampled {len(rows)} findings: {total_refs} raw reference-shaped matches, "
             f"{resolved_refs} resolved to a real iba.verse row, "
             f"{findings_with_any} findings had >=1 resolved reference")
        print("examples:")
        for fid, found in examples:
            print(f"  finding {fid}: {found}")
        return 0

    if a.fix_pass1:
        purge_count = br.execute(
            "SELECT COUNT(*) FROM finding_verse_index WHERE source='structural'").fetchone()[0]
        print(f"would purge {purge_count} bad 'structural' rows")
        if live:
            br.execute("DELETE FROM finding_verse_index WHERE source='structural'")
            print("purged")
        existing_pairs = set(br.execute("SELECT finding_id, verse_id FROM finding_verse_index"))
        rows = br.execute("""
            SELECT f.id, wr.reference
            FROM finding f
            JOIN verse_context vc ON vc.id = f.verse_context_id
            JOIN wa_verse_records wr ON wr.id = vc.verse_record_id
            WHERE f.level='VERSE' AND wr.reference IS NOT NULL
        """).fetchall()
        p1_insert, p1_unresolved = [], 0
        for fid, reference in rows:
            found = resolve_references(reference, crosswalk, verse_id_by_osis)
            if not found:
                p1_unresolved += 1
                continue
            vid, ref_text = found[0]
            key = (fid, vid)
            if key in existing_pairs:
                continue
            existing_pairs.add(key)
            p1_insert.append((fid, vid, ref_text, now))
        print(f"Pass 1 (corrected): {len(rows)} candidate rows, {p1_unresolved} unresolved, "
             f"{len(p1_insert)} to insert")
        if live:
            br.executemany(
                "INSERT INTO finding_verse_index (finding_id, verse_id, reference_text, source, "
                "created_at) VALUES (?, ?, ?, 'structural', ?)", p1_insert)
            br.commit()
            print("committed")
        else:
            print("(report only -- pass --live to actually purge+rebuild)")
        return 0

    _ensure_table(br)
    finding_cols_added = _ensure_columns(br, "finding", [("strong_number", "TEXT")])
    print("finding columns added:", finding_cols_added)

    now = _now()

    # Dedup, researcher instruction 2026-08-29: never insert a (finding_id, verse_id) pair that
    # already exists in finding_verse_index -- loaded once, in-memory (not a per-row SELECT, the
    # same performance class of bug fixed earlier today), and updated as each pass builds its own
    # insert list so Pass 2 also dedupes against whatever Pass 1 just decided to write.
    existing_pairs = set(br.execute("SELECT finding_id, verse_id FROM finding_verse_index"))

    # ── Pass 1: structural (verse_context chain, one-time read only) ────────
    # CORRECTED 2026-08-29 (found live, researcher's own question: "if you take an index in the
    # old system does it point to the correct verse"): the original version of this pass resolved
    # via wa_verse_records.verse_id -- documented as a cross-database bridge into iba.verse, 93%
    # populated, and it looked right on a small manual sample. Checked at full scale after the
    # researcher's question: of 230,045 populated wa_verse_records.verse_id values, only 12,567
    # (5.5%) even point to the correct BOOK -- the bridge column itself is broken pre-existing
    # data, not something this session's work corrupted. Confirmed directly for one finding (id
    # 483437): its own text names Mar 7:25, its verse_context/wa_verse_records chain correctly
    # resolves to wa_verse_records.reference='Mar 7:25' -- but that row's own verse_id column
    # points to Gen.1.2, a wrong and unrelated verse. Fixed: resolve via wa_verse_records.
    # reference (TEXT), the same book-crosswalk mechanism already verified for Pass 2/3, never
    # the verse_id column. Re-checked full scale: 0 of 434,427 original rows matched this
    # corrected resolution -- the previous version of this pass was wrong for every row it wrote,
    # not a partial defect.
    rows = br.execute("""
        SELECT f.id, wr.reference
        FROM finding f
        JOIN verse_context vc ON vc.id = f.verse_context_id
        JOIN wa_verse_records wr ON wr.id = vc.verse_record_id
        WHERE f.level='VERSE' AND wr.reference IS NOT NULL
    """).fetchall()
    p1_insert = []
    p1_unresolved = 0
    for fid, reference in rows:
        found = resolve_references(reference, crosswalk, verse_id_by_osis)
        if not found:
            p1_unresolved += 1
            continue
        vid, ref_text = found[0]   # wa_verse_records.reference is always a single verse, not a list
        key = (fid, vid)
        if key in existing_pairs:
            continue
        existing_pairs.add(key)
        p1_insert.append((fid, vid, ref_text, now))
    print(f"Pass 1 (structural, corrected): {len(rows)} candidate rows, {p1_unresolved} "
         f"unresolved (reference text didn't parse/match), {len(p1_insert)} new after dedup")
    if live:
        br.executemany(
            "INSERT INTO finding_verse_index (finding_id, verse_id, reference_text, source, "
            "created_at) VALUES (?, ?, ?, 'structural', ?)", p1_insert)

    # ── Pass 2: migrate finding_verse_link via reference text ───────────────
    fvl_rows = br.execute(
        "SELECT id, finding_id, reference FROM finding_verse_link WHERE reference IS NOT NULL"
    ).fetchall()
    p2_matched, p2_unmatched = 0, 0
    p2_insert = []
    for _id, finding_id, reference in fvl_rows:
        found = resolve_references(reference, crosswalk, verse_id_by_osis)
        if found:
            p2_matched += 1
            for vid, ref_text in found:
                key = (finding_id, vid)
                if key in existing_pairs:
                    continue
                existing_pairs.add(key)
                p2_insert.append((finding_id, vid, ref_text, now))
        else:
            p2_unmatched += 1
    print(f"Pass 2 (finding_verse_link migration): {len(fvl_rows)} source rows, "
         f"{p2_matched} resolved (>=1 reference each), {p2_unmatched} unresolved, "
         f"{len(p2_insert)} NEW finding_verse_index rows after dedup")
    if live:
        br.executemany(
            "INSERT INTO finding_verse_index (finding_id, verse_id, reference_text, source, "
            "created_at) VALUES (?, ?, ?, 'finding_verse_link', ?)", p2_insert)

    # ── Term side: finding.strong_number backfill ────────────────────────────
    term_rows = br.execute("""
        SELECT COUNT(*) FROM finding f
        JOIN mti_terms mt ON mt.id = f.mti_term_id
        WHERE f.mti_term_id IS NOT NULL
    """).fetchone()[0]
    print(f"Term backfill candidate rows (finding.mti_term_id resolving via mti_terms): {term_rows}")
    if live:
        strong_numbers = set(r[0] for r in iba.execute("SELECT strongNumber FROM strong"))
        to_update = br.execute("""
            SELECT f.id, mt.strongs_number FROM finding f
            JOIN mti_terms mt ON mt.id = f.mti_term_id
            WHERE f.mti_term_id IS NOT NULL
        """).fetchall()
        matched = [(sn, fid) for fid, sn in to_update if sn in strong_numbers]
        br.executemany("UPDATE finding SET strong_number=? WHERE id=?", matched)
        print(f"Term backfill: {len(matched)}/{len(to_update)} resolved and written")

    if live:
        br.commit()
    else:
        br.rollback()
        print("(dry run -- rolled back, nothing written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
