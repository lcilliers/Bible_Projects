"""_apply_obs_catalogue_v2_migration_v1_20260430.py

Migrate observation-question catalogue from v1 (grace-derived universal
questions + word-specific Extensions + Q-COV) to v2 (tier-and-component
prompt structure aligned to the WA Observation Framework T0-T7).

Source for v2 prompts:
  research/investigations/ai_question_test_bundle_20260429/WA-obs-question-catalogue-v2-2026-04-29.json

Operations (transactional, with backup):
  1. Schema: add four columns to `wa_obs_question_catalogue` if absent —
     tier, component_code, component_title, prompt_seq.
  2. Retire the 159 old generic questions (Sections 1-5 + Q-COV) by setting
     status='redundant_v1' AND deleted=1 with an explanatory review_note.
     Existing wa_finding_catalogue_links rows pointing to those questions
     are NOT touched — they remain as historical record of the v1 analysis
     against the old prompts.
  3. Insert 189 new prompts as new catalogue rows tagged with tier,
     component_code, component_title, prompt_seq.
  4. Word-specific Extensions (Compassion / Forgiveness / Goodness / Love /
     Mercy Extensions, 53 rows) are NOT touched — they're not generic.

Idempotency: checked on the presence of any catalogue_version='v2-2026-04-29'
rows. If any already present, the script aborts cleanly.

Usage:
  python scripts/archive/_apply_obs_catalogue_v2_migration_v1_20260430.py
  python scripts/archive/_apply_obs_catalogue_v2_migration_v1_20260430.py --live
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
CATALOGUE_JSON = os.path.join(
    "research", "investigations", "ai_question_test_bundle_20260429",
    "WA-obs-question-catalogue-v2-2026-04-29.json",
)
CATALOGUE_VERSION = "v2-2026-04-29"
RETIRED_STATUS = "redundant_v1"
RETIRED_NOTE = (
    " [2026-04-30: retired as part of catalogue v2 migration. "
    "Replaced by tier-and-component prompt structure aligned to the WA "
    "Observation Framework T0-T7. Historical wa_finding_catalogue_links "
    "rows preserved for analytic provenance.]"
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def column_exists(conn: sqlite3.Connection, table: str, col: str) -> bool:
    rows = conn.execute(f"PRAGMA table_info({table})").fetchall()
    return any(r[1] == col for r in rows)


def add_column_if_absent(conn: sqlite3.Connection, table: str, col_decl: str) -> bool:
    """col_decl like 'tier TEXT'. Returns True if added."""
    col = col_decl.split()[0]
    if column_exists(conn, table, col):
        return False
    conn.execute(f"ALTER TABLE {table} ADD COLUMN {col_decl}")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--catalogue", default=CATALOGUE_JSON)
    args = ap.parse_args()

    # Load v2 catalogue JSON
    with open(args.catalogue, encoding="utf-8") as f:
        cat = json.load(f)

    # Flatten prompts: list of dicts with all metadata for each prompt
    new_rows: list[dict] = []
    for tier in cat["tiers"]:
        tier_code = tier["tier"]
        tier_title = tier["title"]
        for comp in tier["components"]:
            comp_code = comp["code"]
            comp_title = comp["title"]
            for seq, prompt in enumerate(comp["prompts"], start=1):
                question_code = f"{comp_code}.{seq}"
                new_rows.append({
                    "question_code": question_code,
                    "section": f"{tier_code} — {tier_title}",
                    "source_word": "Programme",
                    "source_registry_no": None,
                    "question_text": prompt,
                    "pattern_type": None,
                    "scope": "universal",
                    "status": "active",
                    "deleted": 0,
                    "catalogue_version": CATALOGUE_VERSION,
                    "review_note": None,
                    "tier": tier_code,
                    "component_code": comp_code,
                    "component_title": comp_title,
                    "prompt_seq": seq,
                })

    print(f"v2 catalogue: {len(cat['tiers'])} tiers, "
          f"{cat['meta']['total_components']} components, "
          f"{cat['meta']['total_prompts']} prompts (meta) / {len(new_rows)} prompts (actual)")

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(
            BACKUP_DIR, f"bible_research_pre_obs_catalogue_v2_{today_compact()}.db"
        )
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    if args.live:
        conn.execute("BEGIN")

    try:
        # === Idempotency ===
        existing_v2 = conn.execute(
            "SELECT COUNT(*) FROM wa_obs_question_catalogue WHERE catalogue_version = ?",
            (CATALOGUE_VERSION,),
        ).fetchone()[0]
        if existing_v2:
            print(
                f"[idempotent] {existing_v2} catalogue_version='{CATALOGUE_VERSION}' rows already exist. "
                f"Aborting to avoid duplication."
            )
            return 0

        # === Pre-state ===
        old_generic_q = conn.execute(
            """
            SELECT obs_id, section
            FROM wa_obs_question_catalogue
            WHERE (deleted = 0 OR deleted IS NULL)
            AND (section LIKE 'Section %' OR section = 'Evidence-Flag Research Questions')
            """
        ).fetchall()
        n_old_generic = len(old_generic_q)
        sections = {}
        for r in old_generic_q:
            sections[r["section"]] = sections.get(r["section"], 0) + 1
        print(f"=== Pre-state ===")
        print(f"  {n_old_generic} active old-generic questions to retire:")
        for sec, n in sorted(sections.items()):
            print(f"    {sec}: {n}")

        n_links_against_old = conn.execute(
            """
            SELECT COUNT(*) FROM wa_finding_catalogue_links l
            JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
            WHERE (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
            AND (q.deleted = 0 OR q.deleted IS NULL)
            AND (q.section LIKE 'Section %' OR q.section = 'Evidence-Flag Research Questions')
            """,
        ).fetchone()[0]
        print(f"  {n_links_against_old} active wa_finding_catalogue_links rows currently point at these (preserved as historical record)")

        n_extensions = conn.execute(
            """
            SELECT COUNT(*) FROM wa_obs_question_catalogue
            WHERE (deleted = 0 OR deleted IS NULL) AND section LIKE '%Extensions'
            """,
        ).fetchone()[0]
        print(f"  {n_extensions} word-specific Extensions rows untouched")
        print(f"\n  {len(new_rows)} new v2 prompts to insert")

        if not args.live:
            print("\n[DRY-RUN] would:")
            print(f"  · ALTER TABLE wa_obs_question_catalogue ADD COLUMN tier TEXT")
            print(f"  · ALTER TABLE wa_obs_question_catalogue ADD COLUMN component_code TEXT")
            print(f"  · ALTER TABLE wa_obs_question_catalogue ADD COLUMN component_title TEXT")
            print(f"  · ALTER TABLE wa_obs_question_catalogue ADD COLUMN prompt_seq INTEGER")
            print(f"  · UPDATE {n_old_generic} old-generic rows: status='{RETIRED_STATUS}', deleted=1, review_note appended")
            print(f"  · INSERT {len(new_rows)} new v2 prompt rows (catalogue_version='{CATALOGUE_VERSION}')")
            return 0

        # === Schema additions ===
        added = []
        for col_decl in [
            "tier TEXT",
            "component_code TEXT",
            "component_title TEXT",
            "prompt_seq INTEGER",
        ]:
            if add_column_if_absent(conn, "wa_obs_question_catalogue", col_decl):
                added.append(col_decl)
        if added:
            print(f"  Added columns: {', '.join(added)}")
        else:
            print("  All target columns already exist — skipping schema additions")

        # === Retire old generic ===
        cur = conn.execute(
            f"""
            UPDATE wa_obs_question_catalogue
               SET status = ?,
                   deleted = 1,
                   review_note = COALESCE(review_note, '') || ?
             WHERE (deleted = 0 OR deleted IS NULL)
               AND (section LIKE 'Section %' OR section = 'Evidence-Flag Research Questions')
            """,
            (RETIRED_STATUS, RETIRED_NOTE),
        )
        print(f"  Retired {cur.rowcount} old-generic rows (status='{RETIRED_STATUS}', deleted=1)")

        # === Insert new v2 prompts ===
        insert_sql = """
            INSERT INTO wa_obs_question_catalogue
                (question_code, section, source_word, source_registry_no,
                 question_text, pattern_type, scope, status, deleted,
                 date_added, catalogue_version, review_note,
                 tier, component_code, component_title, prompt_seq)
            VALUES
                (:question_code, :section, :source_word, :source_registry_no,
                 :question_text, :pattern_type, :scope, :status, :deleted,
                 :date_added, :catalogue_version, :review_note,
                 :tier, :component_code, :component_title, :prompt_seq)
        """
        added_at = now_iso()
        for r in new_rows:
            r["date_added"] = added_at
        conn.executemany(insert_sql, new_rows)
        print(f"  Inserted {len(new_rows)} new v2 prompts")

        conn.commit()
        print("\n[LIVE] committed.")

        # Post-state verification
        v2_count = conn.execute(
            "SELECT COUNT(*) FROM wa_obs_question_catalogue WHERE catalogue_version = ?",
            (CATALOGUE_VERSION,),
        ).fetchone()[0]
        retired_count = conn.execute(
            "SELECT COUNT(*) FROM wa_obs_question_catalogue WHERE status = ?",
            (RETIRED_STATUS,),
        ).fetchone()[0]
        active_count = conn.execute(
            "SELECT COUNT(*) FROM wa_obs_question_catalogue WHERE deleted = 0 OR deleted IS NULL"
        ).fetchone()[0]
        print(f"\n=== Post-state ===")
        print(f"  v2 prompts inserted:        {v2_count}")
        print(f"  old generic retired:        {retired_count}")
        print(f"  active catalogue total:     {active_count}")

    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
