"""_repair_homonym_mistarget_set_aside_v1_20260503.py

Sets aside the homonym-mistarget cohort: Strong's that are content nouns by
OSHM morphology but are clearly not analytically relevant to their owning
registry's English concept (place names, divine epithets, sea/cordage and
animal homonyms).

Cohort = bracketed-gloss content nouns + curated non-bracketed homonyms
named in prior analysis. EXCLUDES the alternate-form allowlist (e.g.
'fool[ish]', 'guilt [offering]', 'to cut: make [covenant]') and EXCLUDES
H0935G 'to come [in]: come' (borderline content verb).

Per Strong's, in a single transaction:
  1. UPDATE mti_terms      status='excluded', exclusion_reason=audit_note
  2. UPDATE wa_term_inventory  delete_flagged=1 (OWNER ti row)
  3. UPDATE wa_dimension_index delete_flagged=1 (rows tied to this term's groups)
  4. UPDATE verse_context_group delete_flagged=1
  5. UPDATE verse_context  is_relevant=0, is_anchor=0, is_related=0,
                           group_id=NULL, set_aside_reason='no_inner_being',
                           notes='auto_homonym_mistarget:{category}|2026-05-03'

Usage:
  python scripts/_repair_homonym_mistarget_set_aside_v1_20260503.py            # dry-run
  python scripts/_repair_homonym_mistarget_set_aside_v1_20260503.py --live     # apply
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
POS_JSON = os.path.join("outputs", "markdown", "step-pos-lookup-20260503.json")
NOW_ISO = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# Bracketed-gloss alternate-form allowlist (KEEP — not mistargets)
ALT_FORM_PATTERNS = [
    re.compile(r"^to\s+\w+:.*\[[a-z]+\]\s*$"),         # 'to cut: make [covenant]'
    re.compile(r"^\w+\[(?:ish|er|s|y|ed|ing|al)\]$"),  # fool[ish], labour[er]
    re.compile(r"^\w+\s+\[(?:offering|sacrifice)\]$"), # guilt [offering]
    re.compile(r"^\[Obj\.\]$"),                         # [Obj.] object marker
]

# Strong's specifically excluded from auto cohort even if pattern matches
HARD_EXCLUDE = {
    "H0935G",  # 'to come [in]: come' — content verb; debatable mistarget; manual review
}

# Curated non-bracketed homonyms named in prior no-primary-registries analysis
CURATED_HOMONYMS = {
    # R002 agony — sea/cordage homonyms of c-b-l root
    "H2256C", "H2258A", "H2258B", "H2259", "H2260", "H4865",
    # R074 hardness — animal/place homonyms of az/oz roots
    "H5796", "H5808", "H5822",
    # R178 wrath — wall/bottle/place homonyms
    "H2346G", "H2573", "H2579",
}


def collect_cohort(conn: sqlite3.Connection, pos_lookup: dict) -> list[dict]:
    """Build the mistarget cohort."""
    rows = conn.execute("""
        SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration, mt.gloss,
               mt.language, mt.status,
               ti.id AS ti_id, ti.term_owner_type,
               wr.no AS reg_no, wr.word AS reg_word, wr.id AS reg_id
          FROM mti_terms mt
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                    AND ti.term_owner_type = 'OWNER'
                                    AND ti.delete_flagged = 0
          JOIN wa_file_index fi ON fi.id = ti.file_id
          JOIN word_registry wr ON wr.id = fi.word_registry_fk
         WHERE mt.delete_flagged = 0
           AND mt.status NOT IN ('delete', 'excluded')
           AND (mt.gloss LIKE '%[%' OR mt.gloss LIKE '%]-%')
    """).fetchall()

    cohort = []
    seen = set()
    for r in rows:
        s = r["strongs_number"]
        if s in HARD_EXCLUDE:
            continue
        gloss = (r["gloss"] or "").strip()
        if any(p.search(gloss) for p in ALT_FORM_PATTERNS):
            continue
        pos = pos_lookup.get(s)
        # Skip pronoun/particle/etc — already Tier-1 patched
        if pos in ("pronoun", "pronoun-personal", "particle",
                   "preposition", "conjunction", "interjection", "article",
                   "suffix"):
            continue
        d = dict(r)
        d["pos"] = pos
        d["category"] = "bracketed_proper_noun_or_homonym"
        cohort.append(d)
        seen.add(s)

    # Add curated non-bracketed homonyms
    for s in sorted(CURATED_HOMONYMS):
        if s in seen:
            continue
        r = conn.execute("""
            SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration,
                   mt.gloss, mt.language, mt.status,
                   ti.id AS ti_id, ti.term_owner_type,
                   wr.no AS reg_no, wr.word AS reg_word, wr.id AS reg_id
              FROM mti_terms mt
              JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                        AND ti.term_owner_type = 'OWNER'
                                        AND ti.delete_flagged = 0
              JOIN wa_file_index fi ON fi.id = ti.file_id
              JOIN word_registry wr ON wr.id = fi.word_registry_fk
             WHERE mt.delete_flagged = 0 AND mt.strongs_number = ?
        """, (s,)).fetchone()
        if r:
            d = dict(r)
            d["pos"] = pos_lookup.get(s)
            d["category"] = "curated_homonym"
            cohort.append(d)

    return cohort


def per_strong_counts(conn, mti_id: int) -> dict:
    """Return per-Strong's vc/group/dim counts before the patch."""
    return {
        "vc_active": conn.execute("""
            SELECT COUNT(*) FROM verse_context
             WHERE mti_term_id = ? AND delete_flagged = 0
        """, (mti_id,)).fetchone()[0],
        "vc_anchor": conn.execute("""
            SELECT COUNT(*) FROM verse_context
             WHERE mti_term_id = ? AND delete_flagged = 0 AND is_anchor = 1
        """, (mti_id,)).fetchone()[0],
        "groups_active": conn.execute("""
            SELECT COUNT(*) FROM verse_context_group
             WHERE mti_term_id = ? AND delete_flagged = 0
        """, (mti_id,)).fetchone()[0],
        "dim_active": conn.execute("""
            SELECT COUNT(*) FROM wa_dimension_index di
              JOIN verse_context_group g ON g.id = di.verse_context_group_id
             WHERE g.mti_term_id = ? AND di.delete_flagged = 0
        """, (mti_id,)).fetchone()[0],
    }


def execute_one(conn, item: dict) -> dict:
    """Execute the 5 updates for a single Strong's. Returns counts."""
    cur = conn.cursor()
    s = item["strongs_number"]
    mti_id = item["mti_id"]
    ti_id = item["ti_id"]
    cat = item["category"]
    audit_exc = (
        f"homonym_mistarget|{cat}|gloss='{(item['gloss'] or '')[:50]}'|"
        f"reg=R{item['reg_no']:03d}_{item['reg_word']}|2026-05-03"
    )
    audit_vc = f"auto_homonym_mistarget:{cat}|2026-05-03"

    # 5. verse_context first (clear flags before group goes)
    cur.execute("""
        UPDATE verse_context
           SET is_relevant=0, is_anchor=0, is_related=0, group_id=NULL,
               set_aside_reason='no_inner_being',
               notes = CASE
                 WHEN COALESCE(notes,'') = '' THEN ?
                 ELSE ? || ' | (original: ' || SUBSTR(notes, 1, 160) || ')'
               END
         WHERE mti_term_id = ? AND delete_flagged = 0
           AND (is_relevant = 1 OR is_anchor = 1 OR is_related = 1
                OR group_id IS NOT NULL
                OR set_aside_reason IS NULL OR set_aside_reason = '')
    """, (audit_vc, audit_vc, mti_id))
    vc_updated = cur.rowcount

    # 4. wa_dimension_index — delete-flag rows tied to this term's groups
    cur.execute("""
        UPDATE wa_dimension_index
           SET delete_flagged = 1
         WHERE verse_context_group_id IN (
                 SELECT id FROM verse_context_group
                  WHERE mti_term_id = ? AND delete_flagged = 0
               )
           AND delete_flagged = 0
    """, (mti_id,))
    dim_updated = cur.rowcount

    # 3. verse_context_group — delete-flag
    cur.execute("""
        UPDATE verse_context_group
           SET delete_flagged = 1
         WHERE mti_term_id = ? AND delete_flagged = 0
    """, (mti_id,))
    group_updated = cur.rowcount

    # 2. wa_term_inventory — delete-flag OWNER ti
    cur.execute("""
        UPDATE wa_term_inventory
           SET delete_flagged = 1, last_changed = ?
         WHERE id = ? AND delete_flagged = 0
    """, (NOW_ISO, ti_id))
    ti_updated = cur.rowcount

    # 1. mti_terms — status=excluded
    cur.execute("""
        UPDATE mti_terms
           SET status = 'excluded',
               exclusion_reason = ?,
               last_changed = ?
         WHERE id = ?
    """, (audit_exc, NOW_ISO, mti_id))
    mti_updated = cur.rowcount

    return {
        "vc": vc_updated, "dim": dim_updated, "group": group_updated,
        "ti": ti_updated, "mti": mti_updated,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="Apply changes (default: dry-run)")
    ap.add_argument("--db", default=DB_PATH)
    args = ap.parse_args()

    with open(POS_JSON, encoding="utf-8") as f:
        pos_data = json.load(f)
    pos_lookup = {k: v.get("pos") for k, v in pos_data["results"].items()}

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(BACKUP_DIR,
                              f"bible_research_pre_homonym_mistarget_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.db")
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    cohort = collect_cohort(conn, pos_lookup)
    print(f"Mistarget cohort: {len(cohort)} Strong's\n")

    # Pre-flight: count what would change
    pre = {"vc_active": 0, "vc_anchor": 0, "groups": 0, "dim": 0}
    affected_regs = set()
    for item in cohort:
        c = per_strong_counts(conn, item["mti_id"])
        pre["vc_active"] += c["vc_active"]
        pre["vc_anchor"] += c["vc_anchor"]
        pre["groups"] += c["groups_active"]
        pre["dim"] += c["dim_active"]
        affected_regs.add((item["reg_no"], item["reg_word"]))

    print(f"Pre-flight totals (active rows that will be touched):")
    print(f"  Strong's to set status=excluded:      {len(cohort)}")
    print(f"  wa_term_inventory ti to delete-flag:  {len(cohort)}")
    print(f"  verse_context rows to set aside:      {pre['vc_active']}")
    print(f"  verse_context anchors removed:        {pre['vc_anchor']}")
    print(f"  verse_context_group to delete-flag:   {pre['groups']}")
    print(f"  wa_dimension_index to delete-flag:    {pre['dim']}")
    print(f"  Registries affected:                  {len(affected_regs)}")
    print()

    # Per-registry summary
    per_reg = defaultdict(lambda: {"strongs": 0, "vc": 0, "anchors": 0})
    for item in cohort:
        c = per_strong_counts(conn, item["mti_id"])
        key = (item["reg_no"], item["reg_word"])
        per_reg[key]["strongs"] += 1
        per_reg[key]["vc"] += c["vc_active"]
        per_reg[key]["anchors"] += c["vc_anchor"]

    print("Per-registry impact (registries touched):")
    print(f"  {'reg':>4} {'word':<16} {'#str':>5} {'vc':>5} {'anc':>4}")
    for (no, word), v in sorted(per_reg.items(), key=lambda x: -x[1]["anchors"]):
        if v["strongs"] > 0:
            print(f"  {no:>4} {word:<16} {v['strongs']:>5} {v['vc']:>5} {v['anchors']:>4}")
    print()

    # Execute
    print("--- Executing ---")
    conn.execute("BEGIN")
    totals = {"vc": 0, "dim": 0, "group": 0, "ti": 0, "mti": 0}
    for item in cohort:
        counts = execute_one(conn, item)
        for k, v in counts.items():
            totals[k] += v

    if args.live:
        conn.commit()
        print("[LIVE] Committed.")
    else:
        conn.rollback()
        print("[DRY-RUN] Rolled back.")

    print()
    print("Update totals:")
    for k, v in totals.items():
        print(f"  {k}: {v}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
