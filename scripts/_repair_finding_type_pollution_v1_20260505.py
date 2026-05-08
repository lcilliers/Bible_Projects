"""_repair_finding_type_pollution_v1_20260505.py — DB-modifying.

Cleans the wa_session_b_findings.finding_type column where it has been
overloaded with multi-line tier-completion annotations. The first line is
the actual finding_type value (one of the canonical 20 enum values); the
rest is a tier-completion marker block that was wrongly appended.

Action:
  - finding_type ← first non-empty line (canonical value)
  - resolution_note ← prepend the extracted tier-marker block
                      (or replace if resolution_note is NULL)

Idempotent: the regex looks for newlines in finding_type. After repair,
no rows match and the script is a no-op.

Backed up before changes.
"""
from __future__ import annotations

import os
import re
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db() -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(
        BACKUP_DIR, f"bible_research_{ts}_pre_finding_type_repair.db"
    )
    shutil.copy2(DB_PATH, dest)
    return dest


# Canonical finding_type enum (from current clean rows)
CANONICAL_TYPES = {
    "OBSERVATION", "THEOLOGICAL_NOTE", "SYNTHESIS_INTER_TIER",
    "DIMENSION_REVIEW", "MEANING_OBSERVATION", "SPIRIT_SOUL_BODY",
    "VERSE_PATTERN", "SYNTHESIS_INTRA_TIER", "CROSS_REGISTRY",
    "ETYMOLOGY", "VERSE_ANNOTATION", "SOMATIC_EVIDENCE",
    "DIMENSIONAL_PATTERN", "TERM_BEHAVIOUR", "DATA_ANOMALY_QA_GAP",
    "ROOT_FINDING", "GROUP_INTEGRITY", "DIMENSION_PATTERN",
    "TEMPORAL_OPERATION", "STRUCTURAL_DISPOSITION", "N/A",
}


def split_polluted(raw):
    """Return (clean_type, tier_marker_block).

    Strategy: take the first non-empty line as the type. Validate against
    the canonical set. Strip surrounding triple-backtick code fences from
    the remainder.
    """
    if not raw:
        return None, None
    lines = raw.splitlines()
    # First non-empty line
    first = ""
    rest_start = 0
    for i, line in enumerate(lines):
        if line.strip():
            first = line.strip()
            rest_start = i + 1
            break
    rest_lines = lines[rest_start:]
    # Strip leading/trailing fences
    while rest_lines and rest_lines[0].strip() in ("", "```", "---"):
        rest_lines.pop(0)
    while rest_lines and rest_lines[-1].strip() in ("", "```", "---"):
        rest_lines.pop()
    rest = "\n".join(rest_lines).strip()
    return first, rest


def main() -> int:
    print(f"DB: {DB_PATH}")
    print(f"Backing up...", flush=True)
    bak = backup_db()
    print(f"  -> {bak}\n")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT id, finding_id, finding_type, resolution_note
          FROM wa_session_b_findings
         WHERE finding_type LIKE '%' || char(10) || '%'
    """).fetchall()
    print(f"Polluted rows: {len(rows)}")

    if not rows:
        print("Nothing to repair.")
        conn.close()
        return 0

    # Plan + validate before touching
    plan = []
    invalid_types = set()
    for r in rows:
        clean, marker = split_polluted(r["finding_type"])
        if clean and clean not in CANONICAL_TYPES:
            invalid_types.add(clean)
        plan.append({
            "id": r["id"],
            "finding_id": r["finding_id"],
            "old_type": r["finding_type"],
            "new_type": clean,
            "marker_block": marker,
            "old_resolution": r["resolution_note"],
        })

    if invalid_types:
        print(f"⚠ Some extracted first-lines are not in canonical type "
              f"set: {invalid_types}")
        print("Aborting — manual review required.")
        return 2

    # Show preview
    print("\nSample of repairs (first 3):")
    for p in plan[:3]:
        print(f"  {p['finding_id']}:")
        print(f"    OLD type: {repr(p['old_type'][:60])}…")
        print(f"    NEW type: '{p['new_type']}'")
        print(f"    Marker  : {repr(p['marker_block'][:80])}"
              + ("…" if len(p['marker_block']) > 80 else ""))
        print()

    # Apply
    print("Applying repairs...", flush=True)
    try:
        conn.execute("BEGIN")
        n = 0
        for p in plan:
            # Build new resolution_note: prepend marker if present
            if p["marker_block"]:
                if p["old_resolution"]:
                    new_note = (p["marker_block"]
                                + "\n\n--- prior resolution_note ---\n"
                                + p["old_resolution"])
                else:
                    new_note = p["marker_block"]
            else:
                new_note = p["old_resolution"]
            conn.execute("""
                UPDATE wa_session_b_findings
                   SET finding_type = ?,
                       resolution_note = ?
                 WHERE id = ?
            """, (p["new_type"], new_note, p["id"]))
            n += 1
        conn.execute("COMMIT")
        print(f"  ✓ {n} rows repaired and committed.")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"  ✗ ERROR — rolled back: {e}")
        raise

    # Verify
    print("\nVerification:")
    multiline_after = conn.execute("""
        SELECT COUNT(*) FROM wa_session_b_findings
         WHERE finding_type LIKE '%' || char(10) || '%'
    """).fetchone()[0]
    print(f"  Polluted rows remaining: {multiline_after}")
    print(f"  Distinct finding_type values: ")
    for r in conn.execute("""
        SELECT finding_type, COUNT(*) c
          FROM wa_session_b_findings
         GROUP BY finding_type
         ORDER BY c DESC
    """).fetchall():
        print(f"    [{r['c']:4d}] {r['finding_type']}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
