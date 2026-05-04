"""_apply_synthesis_schema_v1_20260430.py

Schema migration for wa-sessionb-analysis-output-v1_8 Stage 2c synthesis pass.

Required by Actions 1 + 2 in:
  research/investigations/wa-sessionb-v1_8-stage2c-compliance-20260430.md

Adds 5 columns to `wa_session_b_findings`:
  - synthesis_outcome       TEXT  (D | F | N)
  - tiers_engaged           TEXT  (comma-separated T{n} codes)
  - structural_relationship TEXT  (causal | enabling | sequential | constitutive | tension | parallel | N/A)
  - session_c_chapter       TEXT  (Ch1..Ch5 or N/A, comma-joined)
  - sd_pointer_ref          TEXT  (SP-{NNN}-{seq} or NULL)

Plus optional vocab registration in wa_vocab_set / wa_vocab_member for the
controlled-vocabulary fields, so that a future validator can enforce the
allowed values without changing this script.

Idempotent: each ALTER is gated on column-existence; vocab inserts are gated
on label uniqueness.

Pre-write backup taken automatically.

Usage:
  python scripts/archive/_apply_synthesis_schema_v1_20260430.py
  python scripts/archive/_apply_synthesis_schema_v1_20260430.py --live
"""
from __future__ import annotations

import argparse
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"

NEW_COLUMNS = [
    ("synthesis_outcome",       "TEXT"),
    ("tiers_engaged",           "TEXT"),
    ("structural_relationship", "TEXT"),
    ("session_c_chapter",       "TEXT"),
    ("sd_pointer_ref",          "TEXT"),
]

VOCAB_SETS = [
    {
        "set_code": "stage2c_synthesis_outcome",
        "name": "Stage 2c — Synthesis Outcome",
        "applies_to": "wa_session_b_findings.synthesis_outcome",
        "description": (
            "v1.8 Stage 2c synthesis-entry outcome. D = Described (substantive "
            "synthesis finding citing >=2 Stage 2b Q&A entries). F = Further "
            "research required (always pairs with an SD pointer). N = Not "
            "applicable (one-sentence rationale required)."
        ),
        "members": [
            ("D", "Described — substantive synthesis finding"),
            ("F", "Further research required — SD pointer raised"),
            ("N", "Not applicable — rationale recorded"),
        ],
    },
    {
        "set_code": "stage2c_synthesis_finding_type",
        "name": "Stage 2c — Synthesis Finding Type",
        "applies_to": "wa_session_b_findings.finding_type (synthesis subset)",
        "description": (
            "v1.8 finding_type values for Stage 2c synthesis entries written "
            "to wa_session_b_findings. Each registry produces 7 intra-tier "
            "(T1-T7) + 21 inter-tier (T1-T7 unique pairs) = 28 entries."
        ),
        "members": [
            ("SYNTHESIS_INTRA_TIER", "Single-tier synthesis (T1, T2, ... T7)"),
            ("SYNTHESIS_INTER_TIER", "Tier-pair synthesis (T1xT2, ... T6xT7)"),
        ],
    },
    {
        "set_code": "stage2c_structural_relationship",
        "name": "Stage 2c — Structural Relationship",
        "applies_to": "wa_session_b_findings.structural_relationship",
        "description": (
            "v1.8 inter-tier D-outcome synthesis entries name the type of "
            "structural connection between the two tiers. N/A is reserved "
            "for intra-tier or non-D entries where the field does not apply."
        ),
        "members": [
            ("causal",       "One tier produces or causes the other"),
            ("enabling",     "One tier enables or makes possible the other"),
            ("sequential",   "Tiers operate in temporal/process sequence"),
            ("constitutive", "One tier constitutes or defines the other"),
            ("tension",      "Tiers stand in analytical tension"),
            ("parallel",     "Tiers operate in parallel without dependency"),
            ("N/A",          "Field does not apply (intra-tier, F or N outcome)"),
        ],
    },
]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def column_exists(conn: sqlite3.Connection, table: str, col: str) -> bool:
    rows = conn.execute(f"PRAGMA table_info({table})").fetchall()
    return any(r[1] == col for r in rows)


def vocab_set_columns(conn: sqlite3.Connection) -> list[str]:
    return [r[1] for r in conn.execute("PRAGMA table_info(wa_vocab_set)").fetchall()]


def vocab_member_columns(conn: sqlite3.Connection) -> list[str]:
    return [r[1] for r in conn.execute("PRAGMA table_info(wa_vocab_member)").fetchall()]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--db", default=DB_PATH)
    args = ap.parse_args()

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(
            BACKUP_DIR, f"bible_research_pre_synthesis_schema_{today_compact()}.db"
        )
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    if args.live:
        conn.execute("BEGIN")

    try:
        # === Pre-state ===
        print("=== Pre-state ===")
        existing = []
        missing = []
        for name, _type in NEW_COLUMNS:
            if column_exists(conn, "wa_session_b_findings", name):
                existing.append(name)
            else:
                missing.append((name, _type))
        if existing:
            print(f"  {len(existing)} column(s) already present (idempotent skip): " + ", ".join(existing))
        if missing:
            print(f"  {len(missing)} column(s) to add:")
            for name, _type in missing:
                print(f"    + ALTER TABLE wa_session_b_findings ADD COLUMN {name} {_type}")

        # Inspect vocab tables
        vs_cols = vocab_set_columns(conn)
        vm_cols = vocab_member_columns(conn)
        print(f"\n  wa_vocab_set columns:    {vs_cols}")
        print(f"  wa_vocab_member columns: {vm_cols}")

        if not args.live:
            print(f"\n[DRY-RUN] would also:")
            print(f"  · INSERT 3 vocab sets ({sum(len(s['members']) for s in VOCAB_SETS)} members) if not present")
            print(f"\n[DRY-RUN] No DB changes made.")
            return 0

        # === Live: ALTER TABLE ===
        added = 0
        for name, _type in missing:
            conn.execute(f"ALTER TABLE wa_session_b_findings ADD COLUMN {name} {_type}")
            added += 1
            print(f"  + Added column wa_session_b_findings.{name} {_type}")

        # === Live: vocab registration ===
        # wa_vocab_set has fixed shape on this DB:
        # id, set_code (NOT NULL UNIQUE), name, description, governing_doc, applies_to, deprecated, ...
        sets_added = 0
        members_added = 0
        for vset in VOCAB_SETS:
            existing_set = conn.execute(
                "SELECT id FROM wa_vocab_set WHERE set_code = ?",
                (vset["set_code"],),
            ).fetchone()
            if existing_set:
                set_id = existing_set["id"]
            else:
                cur = conn.execute(
                    """
                    INSERT INTO wa_vocab_set
                        (set_code, name, description, applies_to, governing_doc, created_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        vset["set_code"], vset["name"], vset["description"],
                        vset.get("applies_to"),
                        "wa-sessionb-analysis-output-v1_8-20260430.md",
                        now_iso(),
                    ),
                )
                set_id = cur.lastrowid
                sets_added += 1

            # wa_vocab_member has fixed shape:
            # id, set_id, value, label, description, sort_order, deprecated, ...
            for sort_order, (value, label) in enumerate(vset["members"], start=1):
                existing_m = conn.execute(
                    "SELECT 1 FROM wa_vocab_member WHERE set_id = ? AND value = ?",
                    (set_id, value),
                ).fetchone()
                if existing_m:
                    continue
                conn.execute(
                    """
                    INSERT INTO wa_vocab_member
                        (set_id, value, label, sort_order, created_at)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (set_id, value, label, sort_order, now_iso()),
                )
                members_added += 1
        print(f"  + Registered {sets_added} vocab set(s), {members_added} member(s)")

        conn.commit()
        print("\n[LIVE] committed.")

        # === Post-state verification ===
        print("\n=== Post-state ===")
        for name, _type in NEW_COLUMNS:
            present = column_exists(conn, "wa_session_b_findings", name)
            print(f"  wa_session_b_findings.{name:25s} {'present' if present else 'MISSING'}")

        # Confirm existing rows untouched
        n_existing = conn.execute(
            "SELECT COUNT(*) FROM wa_session_b_findings WHERE delete_flag = 0"
        ).fetchone()[0]
        print(f"\n  Active wa_session_b_findings rows (unchanged): {n_existing}")

    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
