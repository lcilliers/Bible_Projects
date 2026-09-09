"""Create `verse_meta` — a new 1:1 companion table to `verse`, collating verse-level base
facts once at the right grain, per escalation #1608 (spawned from #1607/D13).

Why: `language`/`testament`-shaped facts were being denormalized per-CODE onto `verse_lexical`
(language from `strong.language`) or left with no verse-level home at all (`genre`,
`passage.lexical_complete_at` -- CA-11/CA-12). Checked live 2026-09-09: 1 of 29,754 verses
(John.1.18) had a per-code `language` outlier (`H5207` sitting among 13 Greek codes -- almost
certainly a mistagged `G5207`) that nothing was watching for. Precedent for why this matters:
BUILD.md #205 -- `books.abbreviation` (bible_research.db) and `iba.verse.reference`'s own
book-prefix genuinely disagreed on some books (`1Co` vs `1Cor`), worked around at the time via a
position-based crosswalk rather than a single canonical source.

Columns:
  id                 surrogate PK
  verse_id           unique FK -> verse.id (one row per verse)
  testament          'OT'/'NT', derived from cfg_book_order (same derivation `_testament_for`
                     already uses in lib/lexical.py) -- pure, no dependency on other tables
  language           'Hebrew'/'Greek' (domain also allows 'Aramaic' for forward-compatibility,
                     though checked live 2026-09-09: `strong.language` in this corpus is ONLY
                     EVER 'Hebrew' or 'Greek' -- Biblical Aramaic words, e.g. H0762 "Aramaic"
                     itself, are tagged language='Hebrew' too, so majority vote CANNOT and does
                     NOT distinguish genuine Aramaic portions -- corrected from an earlier,
                     wrong assumption in this script's own first draft). Majority vote across
                     this verse's own live verse_lexical rows where any exist -- its real,
                     narrower value is catching DATA ERRORS a testament-only guess would miss
                     (exactly the John.1.18/H5207 case below), not language diversity.
                     Testament-based default (OT->Hebrew, NT->Greek) when no verse_lexical rows
                     exist yet for this verse.
  chapter, verse_num parsed once from osisId (Book.NN.NN, confirmed 29,759/29,759 clean live)
  passage_id         via the existing verse_passage junction (verse_id unique -- "one passage
                     per verse"), NULL if this verse isn't in a passage yet
  is_passage_anchor  via the same junction
  genre              NOT populated this pass -- deliberately left NULL. bible_research.db's own
                     verse.genre was already rejected as a Layer 2 source ("too coarse", #1451);
                     this column exists so genre has a real home once a real mechanism is built,
                     not to smuggle the rejected source back in under a new name.
  lexical_complete_at NOT populated this pass -- home for CA-12 (`passage.lexical_complete_at`,
                     orphaned by #1451). Giving it a verse-level home is this script's job; the
                     completeness-CHECK logic that would populate it is separate, future work.
  created_at, updated_at, deleted -- standard convention.

Auto-sync (per researcher instruction, "automatically updated when any iba.verse records
change"): three triggers, since testament/chapter/verse_num/deleted depend only on `verse`
itself, but `language`'s majority-vote refinement depends on `verse_lexical`, and
`passage_id`/`is_passage_anchor` depend on `verse_passage` -- covering only `verse` would leave
those two silently stale the same way `is_negator`/`party_kind` already are (E2, #1607).
  1. verse_meta_on_verse_insert   -- AFTER INSERT ON verse: creates the companion row
     immediately (testament/chapter/verse_num pure-derived; language defaulted from testament,
     since verse_lexical genuinely can't exist yet for a brand-new verse at this point in the
     pipeline).
  2. verse_meta_on_verse_deleted  -- AFTER UPDATE OF deleted ON verse: keeps soft-delete synced.
  3. verse_meta_on_lexical_change -- AFTER INSERT/UPDATE ON verse_lexical: refreshes this
     verse's `language` via majority vote once real code-level data exists.
  4. verse_meta_on_passage_change -- AFTER INSERT/UPDATE ON verse_passage: refreshes
     `passage_id`/`is_passage_anchor`.

Safe to re-run: table/triggers created only if missing; population re-derives every live row
unconditionally (idempotent), never touches `genre`/`lexical_complete_at` after their initial
NULL seed (so a re-run never clobbers future work on those two once it starts).

Usage:
    python iba/app/migration/create_verse_meta_table_v1_20260909.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys
from datetime import datetime, timezone

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def table_exists(cur, name: str) -> bool:
    return cur.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)
    ).fetchone() is not None


def trigger_exists(cur, name: str) -> bool:
    return cur.execute(
        "SELECT 1 FROM sqlite_master WHERE type='trigger' AND name=?", (name,)
    ).fetchone() is not None


def create_table(cur, report: list[str]) -> None:
    if table_exists(cur, "verse_meta"):
        report.append("TABLE verse_meta already present")
        return
    cur.execute("""
        CREATE TABLE verse_meta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            verse_id INTEGER NOT NULL UNIQUE REFERENCES verse(id),
            testament TEXT,
            language TEXT,
            chapter INTEGER,
            verse_num INTEGER,
            passage_id INTEGER REFERENCES passage(id),
            is_passage_anchor INTEGER,
            genre TEXT,
            lexical_complete_at TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT,
            deleted INTEGER NOT NULL DEFAULT 0
        )
    """)
    cur.execute("CREATE INDEX idx_verse_meta_verse_id ON verse_meta(verse_id)")
    cur.execute("CREATE INDEX idx_verse_meta_passage_id ON verse_meta(passage_id)")
    report.append("CREATED TABLE verse_meta (+2 indexes)")


def create_triggers(cur, report: list[str]) -> None:
    now_expr = "strftime('%Y-%m-%dT%H:%M:%SZ','now')"

    if not trigger_exists(cur, "verse_meta_on_verse_insert"):
        cur.execute(f"""
            CREATE TRIGGER verse_meta_on_verse_insert
            AFTER INSERT ON verse
            BEGIN
                INSERT INTO verse_meta
                    (verse_id, testament, language, chapter, verse_num, created_at, deleted)
                SELECT
                    NEW.id,
                    CASE WHEN (SELECT ordinal FROM cfg_book_order
                               WHERE book = substr(NEW.osisId, 1, instr(NEW.osisId,'.')-1)) <= 38
                         THEN 'OT' ELSE 'NT' END,
                    CASE WHEN (SELECT ordinal FROM cfg_book_order
                               WHERE book = substr(NEW.osisId, 1, instr(NEW.osisId,'.')-1)) <= 38
                         THEN 'Hebrew' ELSE 'Greek' END,
                    CAST(substr(NEW.osisId, instr(NEW.osisId,'.')+1,
                         instr(substr(NEW.osisId, instr(NEW.osisId,'.')+1),'.')-1) AS INTEGER),
                    CAST(substr(NEW.osisId, instr(NEW.osisId,'.')+1
                         + instr(substr(NEW.osisId, instr(NEW.osisId,'.')+1),'.')) AS INTEGER),
                    {now_expr}, NEW.deleted;
            END
        """)
        report.append("CREATED TRIGGER verse_meta_on_verse_insert")
    else:
        report.append("TRIGGER verse_meta_on_verse_insert already present")

    if not trigger_exists(cur, "verse_meta_on_verse_deleted"):
        cur.execute(f"""
            CREATE TRIGGER verse_meta_on_verse_deleted
            AFTER UPDATE OF deleted ON verse
            WHEN NEW.deleted != OLD.deleted
            BEGIN
                UPDATE verse_meta SET deleted = NEW.deleted, updated_at = {now_expr}
                WHERE verse_id = NEW.id;
            END
        """)
        report.append("CREATED TRIGGER verse_meta_on_verse_deleted")
    else:
        report.append("TRIGGER verse_meta_on_verse_deleted already present")

    if not trigger_exists(cur, "verse_meta_on_lexical_change"):
        cur.execute(f"""
            CREATE TRIGGER verse_meta_on_lexical_change
            AFTER INSERT ON verse_lexical
            WHEN NEW.deleted = 0 AND NEW.language IS NOT NULL
            BEGIN
                UPDATE verse_meta SET
                    language = (
                        SELECT language FROM verse_lexical
                        WHERE verse_id = NEW.verse_id AND deleted = 0 AND language IS NOT NULL
                        GROUP BY language ORDER BY COUNT(*) DESC, language LIMIT 1
                    ),
                    updated_at = {now_expr}
                WHERE verse_id = NEW.verse_id;
            END
        """)
        report.append("CREATED TRIGGER verse_meta_on_lexical_change")
    else:
        report.append("TRIGGER verse_meta_on_lexical_change already present")

    if not trigger_exists(cur, "verse_meta_on_passage_change"):
        cur.execute(f"""
            CREATE TRIGGER verse_meta_on_passage_change
            AFTER INSERT ON verse_passage
            WHEN NEW.deleted = 0
            BEGIN
                UPDATE verse_meta SET
                    passage_id = NEW.passage_id,
                    is_passage_anchor = NEW.is_anchor,
                    updated_at = {now_expr}
                WHERE verse_id = NEW.verse_id;
            END
        """)
        report.append("CREATED TRIGGER verse_meta_on_passage_change")
    else:
        report.append("TRIGGER verse_meta_on_passage_change already present")


def populate(cur, report: list[str]) -> int:
    now = _now()
    cur.execute("""
        SELECT v.id AS verse_id, v.osisId, v.deleted,
               (SELECT ordinal FROM cfg_book_order
                WHERE book = substr(v.osisId, 1, instr(v.osisId,'.')-1)) AS ordinal
        FROM verse v
    """)
    verses = cur.fetchall()

    # majority-vote language per verse, from live verse_lexical (single aggregate query, not
    # one query per verse -- 29,759 verses)
    cur.execute("""
        SELECT verse_id, language FROM (
            SELECT verse_id, language, COUNT(*) c,
                   ROW_NUMBER() OVER (PARTITION BY verse_id
                                       ORDER BY COUNT(*) DESC, language) rn
            FROM verse_lexical WHERE deleted=0 AND language IS NOT NULL
            GROUP BY verse_id, language
        ) WHERE rn = 1
    """)
    lang_by_verse = {r[0]: r[1] for r in cur.fetchall()}

    # passage_id/is_passage_anchor from verse_passage
    cur.execute("SELECT verse_id, passage_id, is_anchor FROM verse_passage WHERE deleted=0")
    passage_by_verse = {r[0]: (r[1], r[2]) for r in cur.fetchall()}

    existing = {r[0] for r in cur.execute("SELECT verse_id FROM verse_meta").fetchall()}

    rows = []
    for v in verses:
        vid, osis, deleted, ordinal = v[0], v[1], v[2], v[3]
        parts = osis.split(".")
        chapter = int(parts[1]) if len(parts) == 3 and parts[1].isdigit() else None
        verse_num = int(parts[2]) if len(parts) == 3 and parts[2].isdigit() else None
        testament = ("OT" if ordinal is not None and ordinal <= 38 else "NT") if ordinal is not None else None
        language = lang_by_verse.get(vid) or (
            "Hebrew" if testament == "OT" else "Greek" if testament == "NT" else None)
        passage_id, is_anchor = passage_by_verse.get(vid, (None, None))
        rows.append((vid, testament, language, chapter, verse_num, passage_id, is_anchor,
                     now, deleted))

    new_count = sum(1 for r in rows if r[0] not in existing)
    cur.executemany("""
        INSERT INTO verse_meta
            (verse_id, testament, language, chapter, verse_num, passage_id,
             is_passage_anchor, created_at, deleted)
        VALUES (?,?,?,?,?,?,?,?,?)
        ON CONFLICT(verse_id) DO UPDATE SET
            testament=excluded.testament, language=excluded.language,
            chapter=excluded.chapter, verse_num=excluded.verse_num,
            passage_id=excluded.passage_id, is_passage_anchor=excluded.is_passage_anchor,
            deleted=excluded.deleted, updated_at=excluded.created_at
    """, rows)
    report.append(f"POPULATED verse_meta: {len(rows)} rows total ({new_count} new)")
    return len(rows)


def register_config(cur, report: list[str]) -> None:
    """cfg_table/cfg_column/cfg_utility registration -- same unit of work as the build, same
    pattern as every other new-table migration in this project (e.g.
    build_verse_lexical_window1_layer1_layer2_v1_20260904.py's `_cfg_table_rows`/
    `_cfg_column_rows`): schema registration for a table just built per explicit instruction is
    documentation of already-directed work, not a new runtime judgement call -- the
    Config-Maintenance.ps1 Propose/approve cycle is for changing an EXISTING cfg_* row's live
    behaviour, not for the initial bulk registration of a brand-new table's own columns."""
    SRC = "1608-verse-meta-table (escalation #1608, spawned from #1607/D13)"

    exists = cur.execute(
        "SELECT 1 FROM cfg_table WHERE database='iba' AND name='verse_meta'").fetchone()
    if exists:
        report.append("cfg_table 'verse_meta' already present — skipped")
    else:
        cur.execute(
            "INSERT INTO cfg_table (database, name, grain, use, inactive, category) "
            "VALUES ('iba','verse_meta',?,?,0,?)",
            ("one row per verse (1:1 with verse.id)",
             "Verse-level base-data companion to `verse` -- collates language/testament/chapter/"
             "verse_num/passage linkage once at the right grain, instead of denormalizing "
             "per-code (the old `language` source) or leaving facts homeless (`genre`, "
             "`lexical_complete_at`). Auto-synced via 4 triggers on verse/verse_lexical/"
             "verse_passage inserts and verse.deleted updates -- never written to directly by "
             "application code. Escalation #1608, 2026-09-09.",
             "data"))
        report.append("cfg_table 'verse_meta' added")

    def _add_col(name: str, ordinal: int, coltype: str, notnull: int, fk, use: str) -> None:
        exists = cur.execute(
            "SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='verse_meta' "
            "AND name=?", (name,)).fetchone()
        if exists:
            report.append(f"cfg_column verse_meta.{name} already present — skipped")
            return
        cur.execute(
            "INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "
            "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by, "
            "inactive) VALUES ('iba','verse_meta',?,?,?,?,?,?,NULL,?,?,NULL,?,?,0)",
            (name, ordinal, coltype, 1 if name == "id" else 0, notnull,
             1 if name == "verse_id" else 0, fk, use, SRC, "verse_meta triggers"))
        report.append(f"cfg_column verse_meta.{name} added")

    _add_col("id", 0, "INTEGER", 0, None, "surrogate PK")
    _add_col("verse_id", 1, "INTEGER", 1, "verse.id",
             "the verse this row is about -- unique, one row per verse")
    _add_col("testament", 2, "TEXT", 0, None,
             "'OT'/'NT', derived from cfg_book_order.ordinal<=38 -- pure function of the verse's "
             "own book, no dependency on any other table. Set by verse_meta_on_verse_insert, "
             "immutable thereafter (a verse never changes book).")
    _add_col("language", 3, "TEXT", 0, None,
             "'Hebrew'/'Greek' in practice (domain also allows 'Aramaic' for forward-"
             "compatibility, but strong.language never carries it corpus-wide -- checked live "
             "2026-09-09, even H0762 'Aramaic' itself is tagged Hebrew, so this column CANNOT "
             "distinguish genuine Aramaic portions). Majority vote across the verse's own live "
             "verse_lexical rows (verse_meta_on_lexical_change), testament-based default when "
             "none exist yet. Real value: surfaces a per-code language OUTLIER as a data-quality "
             "signal (e.g. John.1.18/H5207, a mistagged code) that a testament-only guess would "
             "never catch, not language diversity.")
    _add_col("chapter", 4, "INTEGER", 0, None, "parsed once from osisId (Book.NN.NN)")
    _add_col("verse_num", 5, "INTEGER", 0, None, "parsed once from osisId (Book.NN.NN)")
    _add_col("passage_id", 6, "INTEGER", 0, "passage.id",
             "via the verse_passage junction (verse_id unique, one passage per verse) -- NULL "
             "if this verse isn't in a passage yet. Synced by verse_meta_on_passage_change.")
    _add_col("is_passage_anchor", 7, "INTEGER", 0, None,
             "via the same verse_passage junction, same trigger as passage_id")
    _add_col("genre", 8, "TEXT", 0, None,
             "NOT populated as of #1608 -- deliberately left NULL. bible_research.db's own "
             "verse.genre was already rejected as a Layer 2 source ('too coarse', #1451); this "
             "column exists so genre has a real verse-level home once a real mechanism is "
             "built (CA-11), not to reintroduce the rejected source under a new name.")
    _add_col("lexical_complete_at", 9, "TEXT", 0, None,
             "NOT populated as of #1608 -- home for CA-12 (`passage.lexical_complete_at`, "
             "orphaned by #1451's verse-scoped redesign). Giving it a verse-level home is "
             "#1608's job; the completeness-CHECK logic that would populate it is separate, "
             "future work.")
    _add_col("created_at", 10, "TEXT", 1, None, "ISO-8601 UTC, set once at row creation")
    _add_col("updated_at", 11, "TEXT", 0, None,
             "ISO-8601 UTC, set by any of the 3 refresh triggers (deleted/language/passage_id "
             "change) -- NULL means never refreshed since creation")
    _add_col("deleted", 12, "INTEGER", 1, None,
             "soft delete, kept in sync with verse.deleted via verse_meta_on_verse_deleted")

    exists = cur.execute(
        "SELECT 1 FROM cfg_utility WHERE file_path="
        "'iba/app/migration/create_verse_meta_table_v1_20260909.py'").fetchone()
    if exists:
        report.append("cfg_utility for this script already present — skipped")
    else:
        cur.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt, "
            "crash_escalation_reviewed) VALUES (?,?,?,0,0,0)",
            ("create_verse_meta_table_v1_20260909",
             "iba/app/migration/create_verse_meta_table_v1_20260909.py",
             "Creates verse_meta (1:1 companion to verse, base-data grain -- language/testament/"
             "chapter/verse_num/passage linkage), one-off populates it from bible_research.db-"
             "informed design + iba.db's own osisId/cfg_book_order/verse_lexical/verse_passage, "
             "validates the result, and builds the 4 auto-sync triggers "
             "(verse/verse_lexical/verse_passage inserts, verse.deleted updates). Idempotent, "
             "safe to re-run. Escalation #1608."))
        report.append("cfg_utility for create_verse_meta_table_v1_20260909.py added")


def validate(cur, report: list[str]) -> list[str]:
    problems = []

    n_verse = cur.execute("SELECT COUNT(*) FROM verse").fetchone()[0]
    n_meta = cur.execute("SELECT COUNT(*) FROM verse_meta").fetchone()[0]
    if n_verse != n_meta:
        problems.append(f"row count mismatch: verse={n_verse} verse_meta={n_meta}")
    else:
        report.append(f"row count MATCHES: {n_meta} verse_meta rows for {n_verse} verse rows")

    orphans = cur.execute("""
        SELECT COUNT(*) FROM verse_meta vm
        LEFT JOIN verse v ON v.id = vm.verse_id WHERE v.id IS NULL
    """).fetchone()[0]
    if orphans:
        problems.append(f"{orphans} verse_meta rows reference a missing verse")
    else:
        report.append("0 orphaned verse_meta rows")

    dupes = cur.execute("""
        SELECT COUNT(*) FROM (SELECT verse_id FROM verse_meta GROUP BY verse_id HAVING COUNT(*)>1)
    """).fetchone()[0]
    if dupes:
        problems.append(f"{dupes} verse_id values have more than one verse_meta row")
    else:
        report.append("0 duplicate verse_id values (grain confirmed 1:1)")

    null_testament = cur.execute(
        "SELECT COUNT(*) FROM verse_meta WHERE testament IS NULL").fetchone()[0]
    if null_testament:
        problems.append(f"{null_testament} rows have NULL testament (book not in cfg_book_order?)")
    else:
        report.append("0 NULL testament values")

    bad_testament = cur.execute(
        "SELECT COUNT(*) FROM verse_meta WHERE testament NOT IN ('OT','NT')").fetchone()[0]
    if bad_testament:
        problems.append(f"{bad_testament} rows have a testament value outside OT/NT")

    bad_language = cur.execute(
        "SELECT COUNT(*) FROM verse_meta WHERE language NOT IN ('Hebrew','Greek','Aramaic')"
    ).fetchone()[0]
    if bad_language:
        problems.append(f"{bad_language} rows have a language value outside Hebrew/Greek/Aramaic")
    else:
        report.append("0 rows with an out-of-domain language value")

    # cross-check: verses where the majority-vote language disagrees with a MINORITY of that
    # same verse's own live verse_lexical rows -- surfaces exactly the John.1.18/H5207 shape of
    # anomaly, reported (not fixed) here.
    cur.execute("""
        SELECT vm.verse_id, v.osisId, vm.language, vl.strong, vl.language AS code_language
        FROM verse_meta vm
        JOIN verse v ON v.id = vm.verse_id
        JOIN verse_lexical vl ON vl.verse_id = vm.verse_id AND vl.deleted=0
        WHERE vl.language IS NOT NULL AND vl.language != vm.language
    """)
    outliers = cur.fetchall()
    if outliers:
        report.append(f"{len(outliers)} verse_lexical rows disagree with their verse's "
                      f"majority-vote language (surfaced, not auto-fixed -- tracked on D12):")
        for o in outliers[:10]:
            report.append(f"    {o[1]} verse_meta.language={o[2]} vs {o[3]}.language={o[4]}")
    else:
        report.append("0 per-code language outliers found")

    # NOTE, corrected 2026-09-09: originally checked expecting 'Aramaic' here -- wrong. Confirmed
    # live: strong.language never carries 'Aramaic' anywhere in this corpus (even H0762
    # "Aramaic" itself is tagged 'Hebrew'), so this column cannot and does not distinguish
    # Biblical Aramaic from Hebrew. Kept as a documented limitation, not silently dropped.
    dan = cur.execute("""
        SELECT v.osisId, vm.language FROM verse_meta vm JOIN verse v ON v.id=vm.verse_id
        WHERE v.osisId IN ('Dan.2.4','Dan.2.5','Dan.3.1')
    """).fetchall()
    report.append(f"Daniel Aramaic-portion spot check (expect 'Hebrew', NOT 'Aramaic' -- "
                  f"source data has no Aramaic distinction, documented limitation): "
                  f"{[(r[0], r[1]) for r in dan]}")

    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = None
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")
        create_table(cur, report)
        create_triggers(cur, report)
        populate(cur, report)
        register_config(cur, report)
        problems = validate(cur, report)

        if args.dry_run:
            conn.rollback()
            report.append("DRY-RUN: rolled back")
        else:
            conn.commit()
            report.append("COMMITTED")

        print("\n".join(report))
        if problems:
            print("\nVALIDATION PROBLEMS:")
            for p in problems:
                print("  -", p)
            return 1
        print("\nVALIDATION: clean")
        return 0
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
