"""Migrate `wa_obs_question_catalogue` from `bible_research.db` into `iba.db` — escalation #1696
(design-complete, CSV reviewed, "migration can proceed"), #1706 Phase D item 19, build session
2026-09-16.

**Content scope, per researcher's own Phase 5 review** (`1704-catalogue-content-decisions-v1-
20260916.md`): 98 live source rows − 8 dropped − ... + 2 new T2.11 rows = **92 rows**.

Dropped (8 question codes, per the Phase 5 review):
    T0.4.1, T5.4.1, T5.4.2, T5.5.1, T5.6.1, T7.2.2a, T7.2.2b, T7.2.4

Text revision (1 code): T7.1.3 — expanded to prompt for idiom/analogy/implied meaning
    (`1704-catalogue-content-decisions-v1-20260916.md` item 8).

Added (2 new rows, #1701 `1701-faculty-engagement-catalogue-addition-v1-20260916.md`):
    T2.11.1, T2.11.2 ("Faculty Engagement") — content copied verbatim from that document's own
    table, not re-derived here.

Creates `wa_obs_question_catalogue` in `iba.db` (same shape as the `bible_research.db` source, a
fresh `obs_id` sequence — not copied from source, per both source docs' own instruction: "obs_id,
date_added, and last_modified are set at actual migration/insert time, not backdated"). Retargets
the table's `cfg_table` registration to `iba` (was `bible_research`) and flags the
`bible_research.db` copy `inactive=1` (source stays physically present, per the project's own
retire-don't-delete convention — not read by any live routine going forward).

`ib_observation.question_code`/`ib_node.question_code`'s real FK restoration (both currently
un-enforced, #1691/#1692's own noted gap) is a SEPARATE follow-up, not done by this script — SQLite
FKs are declared at CREATE TABLE time; adding one after the fact needs a table rebuild on both
`ib_observation` and `ib_node`, left for when those tables' actual write paths are built (Phase F).

Safe to re-run: guarded, no-ops if the destination table already has rows.

Usage:
    python iba/app/migration/migrate_obs_question_catalogue_to_iba_v1_20260916.py [--dry-run]
"""
import argparse
import sqlite3
import sys

IBA_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RESEARCH_DB = r"C:\Bible_study_projects\database\bible_research.db"

_DROPPED_CODES = ("T0.4.1", "T5.4.1", "T5.4.2", "T5.5.1", "T5.6.1",
                  "T7.2.2a", "T7.2.2b", "T7.2.4")

_T7_1_3_REVISED_TEXT = (
    "What is the semantic range of the primary term — across what breadth of meaning does it "
    "operate, including any idiomatic, analogical, or otherwise implied meaning carried by its "
    "use in combination with other terms?"
)

# T2.11.1/T2.11.2 — verbatim from 1701-faculty-engagement-catalogue-addition-v1-20260916.md's own
# table. Columns match wa_obs_question_catalogue's shape (obs_id/date_added/last_modified set at
# insert time below, not hardcoded here).
_T2_11_ROWS = [
    {
        "question_code": "T2.11.1",
        "section": "T2 — Constitutional Location and Boundaries",
        "source_word": "Programme",
        "source_registry_no": None,
        "question_text": (
            "In this verse, does the characteristic engage or is affected by specific faculties — "
            "the inner senses (hearing, sight, taste, touch, smell), spiritual discernment, the "
            "cognitive faculty (knowing, understanding, discerning), the memory faculty (the "
            "holding and retrieving of inner-being reality across time), the affective faculty "
            "(feeling and emotional experience), the creative faculty (imagination and the "
            "capacity to originate), the volitional faculty (the capacity to choose), the agency "
            "faculty (the capacity to act, initiate, and make happen), the moral-evaluation "
            "faculty (the capacity to assess against a standard of right, wrong, good, and true), "
            "conscience (the acute inner witness of sin, guilt, and conviction), conscientiousness "
            "(the integrated response of moral awareness, volition, and action), or relational "
            "capacity (the constitutional equipment for genuine connection with another person) — "
            "and if so, which faculty/faculties and how? Record none if it does not."),
        "pattern_type": "faculty-engagement-reflection",
        "scope": "Verse-context",
        "status": "active",
        "deleted": 0,
        "catalogue_version": "v2-2026-09-16",
        "review_note": (
            "Added 2026-09-16, escalation #1701 — consolidates the retired T3 (Inner Faculties) "
            "tier's 11 per-faculty questions into one engagement question per subgroup read, per "
            "#1704 §5 decision 4. Not the same axis as T2.1 (constitutional location) — a "
            "genuinely separate component, confirmed with the researcher before placement."),
        "tier": "T2", "component_code": "T2.11", "component_title": "Faculty Engagement",
        "prompt_seq": 1, "source": None,
    },
    {
        "question_code": "T2.11.2",
        "section": "T2 — Constitutional Location and Boundaries",
        "source_word": "Programme",
        "source_registry_no": None,
        "question_text": (
            "Across the verses, what does the pattern of engagement and non-engagement with the "
            "faculties indicate about the characteristic's nature?"),
        "pattern_type": "faculty-engagement-reflection",
        "scope": "Characteristic (HIB behaviour)",
        "status": "active",
        "deleted": 0,
        "catalogue_version": "v2-2026-09-16",
        "review_note": (
            "Added 2026-09-16, escalation #1701 — consolidates the retired T3 (Inner Faculties) "
            "tier's 11 per-faculty questions into one engagement question per subgroup read, per "
            "#1704 §5 decision 4. Not the same axis as T2.1 (constitutional location) — a "
            "genuinely separate component, confirmed with the researcher before placement."),
        "tier": "T2", "component_code": "T2.11", "component_title": "Faculty Engagement",
        "prompt_seq": 2, "source": None,
    },
]

_CREATE_SQL = """
    CREATE TABLE wa_obs_question_catalogue (
        obs_id              INTEGER PRIMARY KEY AUTOINCREMENT,
        question_code       TEXT NOT NULL UNIQUE,
        section             TEXT NOT NULL,
        source_word         TEXT,
        source_registry_no  INTEGER,
        question_text       TEXT NOT NULL,
        pattern_type        TEXT,
        scope               TEXT NOT NULL DEFAULT 'universal',
        status              TEXT NOT NULL DEFAULT 'active',
        deleted             INTEGER NOT NULL DEFAULT 0,
        date_added          TEXT NOT NULL,
        catalogue_version   TEXT NOT NULL,
        review_note         TEXT,
        tier                TEXT,
        component_code      TEXT,
        component_title     TEXT,
        prompt_seq          INTEGER,
        source              TEXT,
        last_modified       TEXT
    )
"""


def now() -> str:
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    src_conn = sqlite3.connect(RESEARCH_DB)
    src_conn.row_factory = sqlite3.Row
    dst_conn = sqlite3.connect(IBA_DB)
    dst_cur = dst_conn.cursor()
    report: list[str] = []
    try:
        dst_cur.execute("BEGIN")

        already = dst_cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND "
            "name='wa_obs_question_catalogue'").fetchone()
        if already:
            existing_rows = dst_cur.execute(
                "SELECT COUNT(*) FROM wa_obs_question_catalogue").fetchone()[0]
            if existing_rows:
                report.append(f"wa_obs_question_catalogue already exists in iba.db with "
                             f"{existing_rows} row(s) — migration already applied, skipping")
                print("\n".join(report))
                dst_conn.rollback()
                return 0
        else:
            dst_cur.execute(_CREATE_SQL)
            report.append("CREATED wa_obs_question_catalogue in iba.db")

        src_rows = src_conn.execute(
            "SELECT * FROM wa_obs_question_catalogue WHERE deleted=0 ORDER BY question_code"
        ).fetchall()
        report.append(f"source: {len(src_rows)} live row(s) in bible_research.db")

        ts = now()
        inserted, dropped, revised = 0, 0, 0
        for r in src_rows:
            if r["question_code"] in _DROPPED_CODES:
                dropped += 1
                continue
            question_text = r["question_text"]
            if r["question_code"] == "T7.1.3":
                question_text = _T7_1_3_REVISED_TEXT
                revised += 1
            dst_cur.execute(
                "INSERT INTO wa_obs_question_catalogue (question_code, section, source_word, "
                "source_registry_no, question_text, pattern_type, scope, status, deleted, "
                "date_added, catalogue_version, review_note, tier, component_code, "
                "component_title, prompt_seq, source, last_modified) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (r["question_code"], r["section"], r["source_word"], r["source_registry_no"],
                 question_text, r["pattern_type"], r["scope"], r["status"], 0, ts,
                 r["catalogue_version"], r["review_note"], r["tier"], r["component_code"],
                 r["component_title"], r["prompt_seq"], r["source"], ts))
            inserted += 1

        for row in _T2_11_ROWS:
            dst_cur.execute(
                "INSERT INTO wa_obs_question_catalogue (question_code, section, source_word, "
                "source_registry_no, question_text, pattern_type, scope, status, deleted, "
                "date_added, catalogue_version, review_note, tier, component_code, "
                "component_title, prompt_seq, source, last_modified) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (row["question_code"], row["section"], row["source_word"],
                 row["source_registry_no"], row["question_text"], row["pattern_type"],
                 row["scope"], row["status"], row["deleted"], ts, row["catalogue_version"],
                 row["review_note"], row["tier"], row["component_code"], row["component_title"],
                 row["prompt_seq"], row["source"], ts))
            inserted += 1

        report.append(f"migrated {inserted} row(s) ({dropped} dropped per Phase 5 review, "
                      f"{revised} text-revised (T7.1.3), 2 new T2.11 rows added)")

        final_count = dst_cur.execute(
            "SELECT COUNT(*) FROM wa_obs_question_catalogue").fetchone()[0]
        report.append(f"destination now has {final_count} row(s) "
                      f"({'matches expected 92' if final_count == 92 else 'MISMATCH — expected 92'})")

        # Register cfg_table (retarget to iba) + cfg_column.
        dst_cur.execute(
            "UPDATE cfg_table SET inactive=1, use=use || ' RETIRED 2026-09-16 (#1706 Phase D item "
            "19) -- migrated into iba.db, this bible_research.db copy is no longer the live "
            "source (kept, not deleted, per the project''s own retire-don''t-delete convention).' "
            "WHERE database='bible_research' AND name='wa_obs_question_catalogue'")
        report.append("cfg_table bible_research.wa_obs_question_catalogue marked inactive")

        if not dst_cur.execute("SELECT 1 FROM cfg_table WHERE database='iba' AND "
                               "name='wa_obs_question_catalogue'").fetchone():
            dst_cur.execute(
                "INSERT INTO cfg_table (database, name, grain, use, inactive, category) "
                "VALUES ('iba', 'wa_obs_question_catalogue', ?, ?, 0, 'data')",
                ("one row per catalogue question, the analytic-event question bank for the "
                 "cluster-reading pipeline",
                 "Migrated from bible_research.db 2026-09-16 (#1696, #1706 Phase D item 19) -- "
                 "92 rows (98 source - 8 dropped per Phase 5 content review + 2 new T2.11 rows). "
                 "ib_observation.question_code/ib_node.question_code both intend a real FK here "
                 "once their tables' write paths are built (Phase F) -- not enforced yet, SQLite "
                 "FKs are declare-at-create-time only."))
            report.append("cfg_table iba.wa_obs_question_catalogue registered")

        cols = [
            (0, "obs_id", "INTEGER", 1, 1, "surrogate PK, fresh sequence (not copied from source)"),
            (1, "question_code", "TEXT", 0, 1, "e.g. T1.1.1 -- unique, the catalogue's own stable key"),
            (2, "section", "TEXT", 0, 1, "the T-tier section heading"),
            (3, "source_word", "TEXT", 0, 0, "provenance"),
            (4, "source_registry_no", "INTEGER", 0, 0, "provenance"),
            (5, "question_text", "TEXT", 0, 1, "the actual catalogue question text"),
            (6, "pattern_type", "TEXT", 0, 0,
             "event-cross-reference column, ready-to-apply crosswalk per #1704 Phase 3 -- write "
             "now vs fold into this same migration was a sequencing question, resolved: folded in"),
            (7, "scope", "TEXT", 0, 1,
             "Word/term (lexical) | Verse-context | Characteristic | The HIB | etc -- #1682 SS4A's "
             "own scope-category list"),
            (8, "status", "TEXT", 0, 1, "active | retired"),
            (9, "deleted", "INTEGER", 0, 1, "soft-delete"),
            (10, "date_added", "TEXT", 0, 1, "ISO-8601 UTC, set at migration/insert time"),
            (11, "catalogue_version", "TEXT", 0, 1, "e.g. v2-2026-09-16"),
            (12, "review_note", "TEXT", 0, 0, "free text"),
            (13, "tier", "TEXT", 0, 0, "T0-T7"),
            (14, "component_code", "TEXT", 0, 0, "e.g. T2.11"),
            (15, "component_title", "TEXT", 0, 0, "e.g. Faculty Engagement"),
            (16, "prompt_seq", "INTEGER", 0, 0, "ordering within a component"),
            (17, "source", "TEXT", 0, 0, "descriptive provenance, not an invented code"),
            (18, "last_modified", "TEXT", 0, 0, "ISO-8601 UTC"),
        ]
        for ordinal, name, ctype, is_pk, notnull, use in cols:
            if not dst_cur.execute("SELECT 1 FROM cfg_column WHERE database='iba' AND "
                                   "table_name='wa_obs_question_catalogue' AND name=?",
                                   (name,)).fetchone():
                dst_cur.execute(
                    'INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, '
                    '"notnull", is_unique, dflt, fk, use, expectation, source, filled_by, '
                    'inactive) VALUES (\'iba\',\'wa_obs_question_catalogue\',?,?,?,?,?,0,NULL,'
                    'NULL,?,NULL,NULL,NULL,0)',
                    (name, ordinal, ctype, is_pk, notnull, use))
        report.append("cfg_column rows registered for wa_obs_question_catalogue (19 columns)")

        if args.dry_run:
            dst_conn.rollback()
            report.append("DRY-RUN: rolled back")
        else:
            dst_conn.commit()
            report.append("COMMITTED")

        print("\n".join(report))
        return 0
    except Exception:
        dst_conn.rollback()
        raise
    finally:
        src_conn.close()
        dst_conn.close()


if __name__ == "__main__":
    sys.exit(main())
