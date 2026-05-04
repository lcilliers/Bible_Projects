"""_repair_h7965_r117_recovery_v1_20260501.py

Recover the H7965 shalom family for R117 peace.

Background: All H7965 sub-forms (G/H/I/J/K/L) were marked status='delete' in
wa_session_b_findings on 2026-03-26 14:46:32Z (no exclusion_reason recorded).
The original Phase 1 extract (2026-03-17, file_id=48) had shalom under R117
peace; a 2026-03-18 BULK_GAP_FILL run created OWNER copies under R34 covenant
(file_id=80). The 2026-03-26 sweep deleted both. Verse records (209 total)
remain in DB, all delete_flagged=1.

Per researcher decision (2026-05-01): un-flag the existing data and re-OWN
H7965 to R117 peace, preparing the registry for a Verse Context re-run.

Actions (all non-destructive — no rows deleted; flags toggled, statuses set):

  1. mti_terms × 6 primary rows: status='delete' → 'extracted' (or
     'extracted_thin' for low-volume forms <20 verses); owning_registry_fk
     set to 117; vc_status reset to NULL.

  2. wa_term_inventory: term_owner_type re-allocated so the R117 part-1
     file (file_id=48) holds OWNER for all 6 sub-forms; the R34 BULK_GAP_FILL
     file (file_id=80) is demoted to XREF; R163 file (file_id=192) stays
     XREF. ti 617 (H7965H in file_id=48, currently NULL/flagged) is
     promoted to OWNER and un-flagged.

  3. wa_verse_records: un-flag the 209 OWNER-side verses (one ti per
     sub-form). XREF copies remain delete_flagged=1 per the OWNER/XREF
     architecture.

  4. word_registry: verse_context_status='Complete' → 'In Progress' so
     VC re-runs to classify the recovered H7965 terms. session_b_status
     stays 'Verse Context Reset'. dim_review_status stays 'Complete'
     (new groups created during VC will need dimension assignment as a
     follow-up).

Backup is taken before any write. All changes performed inside a single
transaction; rollback on any failure.

Usage:
  python scripts/_repair_h7965_r117_recovery_v1_20260501.py            # dry-run
  python scripts/_repair_h7965_r117_recovery_v1_20260501.py --live     # commit

Output: Sessions/Patches/wa-117-peace-h7965-recovery-v1-{date}.json — patch
record (provenance: which IDs were touched, before/after values), written
on both dry-run (preview) and live (record).
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
PATCH_DIR = os.path.join("Sessions", "Patches")
THIN_DATA_THRESHOLD = 20  # CLAUDE.md THIN_DATA_THRESHOLD

# Recovery scope, exact IDs (verified 2026-05-01 from live DB)
SCOPE = [
    # (strongs, primary_mti_id, r117_owner_ti_id, r34_xref_ti_id, expected_verses)
    {"strongs": "H7965G", "mti_id": 2508, "r117_ti": 2646, "r34_ti": 3425,
     "verses": 148, "gloss": "peace"},
    {"strongs": "H7965H", "mti_id": 406,  "r117_ti": 617,  "r34_ti": 3433,
     "verses": 1,   "gloss": "Peace [God]"},
    {"strongs": "H7965I", "mti_id": 2509, "r117_ti": 2647, "r34_ti": 3427,
     "verses": 46,  "gloss": "peace: well-being"},
    {"strongs": "H7965J", "mti_id": 2510, "r117_ti": 2648, "r34_ti": 3430,
     "verses": 5,   "gloss": "peace: friendship"},
    {"strongs": "H7965K", "mti_id": 2511, "r117_ti": 2649, "r34_ti": 3429,
     "verses": 8,   "gloss": "peace: greeting"},
    {"strongs": "H7965L", "mti_id": 2512, "r117_ti": 2650, "r34_ti": 3434,
     "verses": 1,   "gloss": "peace: completely"},
]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def backup_db() -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(
        BACKUP_DIR, f"bible_research_pre_h7965_recovery_{stamp}.db"
    )
    shutil.copy2(DB_PATH, backup_path)
    return backup_path


def status_for(verses: int, gloss: str) -> str:
    """Choose mti_terms.status based on verse count + gloss conventions."""
    # H7965H 'Peace [God]' is a divine-name fragment; thin but kept active.
    if verses < THIN_DATA_THRESHOLD:
        return "extracted_thin"
    return "extracted"


def collect_before_state(conn: sqlite3.Connection) -> dict:
    """Snapshot current state of every row this script will touch."""
    state = {"timestamp": now_iso(), "scope": []}
    for s in SCOPE:
        before = {"strongs": s["strongs"]}
        # mti_terms primary
        r = conn.execute(
            "SELECT id, status, owning_registry, owning_registry_fk, "
            "       owning_word, vc_status, last_changed "
            "FROM mti_terms WHERE id = ?",
            (s["mti_id"],),
        ).fetchone()
        before["mti_primary"] = dict(r) if r else None
        # term inventory rows
        before["ti_r117"] = dict(conn.execute(
            "SELECT id, term_owner_type, delete_flagged, file_id "
            "FROM wa_term_inventory WHERE id = ?",
            (s["r117_ti"],),
        ).fetchone() or {})
        before["ti_r34"] = dict(conn.execute(
            "SELECT id, term_owner_type, delete_flagged, file_id "
            "FROM wa_term_inventory WHERE id = ?",
            (s["r34_ti"],),
        ).fetchone() or {})
        # verse counts
        n_active = conn.execute(
            "SELECT COUNT(*) FROM wa_verse_records "
            "WHERE term_inv_id = ? AND (delete_flagged = 0 OR delete_flagged IS NULL)",
            (s["r117_ti"],),
        ).fetchone()[0]
        n_flagged = conn.execute(
            "SELECT COUNT(*) FROM wa_verse_records "
            "WHERE term_inv_id = ? AND delete_flagged = 1",
            (s["r117_ti"],),
        ).fetchone()[0]
        before["r117_verses_active"] = n_active
        before["r117_verses_flagged"] = n_flagged
        state["scope"].append(before)

    # Registry
    state["registry_before"] = dict(conn.execute(
        "SELECT no, word, verse_context_status, session_b_status, "
        "       dim_review_status FROM word_registry WHERE no = 117"
    ).fetchone())
    return state


def apply_changes(conn: sqlite3.Connection, ts: str) -> dict:
    """Execute the recovery ops; return per-op rowcounts."""
    counts = {
        "mti_reactivated": 0,
        "ti_promoted_owner": 0,
        "ti_demoted_xref": 0,
        "ti_unflagged": 0,
        "verses_unflagged": 0,
        "registry_updated": 0,
    }
    for s in SCOPE:
        new_status = status_for(s["verses"], s["gloss"])
        # 1. mti_terms primary — reactivate + repoint to R117
        # vc_status column is NOT NULL; use 'not_done' to mark VC as pending
        # for the recovered term (per controlled vocabulary in CLAUDE.md §14).
        cur = conn.execute(
            "UPDATE mti_terms "
            "   SET status = ?, owning_registry = ?, owning_registry_fk = ?, "
            "       vc_status = 'not_done', vc_status_updated_at = ?, "
            "       vc_status_note = ?, last_changed = ? "
            " WHERE id = ?",
            (
                new_status, "117", 117, ts,
                "H7965 recovery 2026-05-01: status reactivated from 'delete' to "
                f"'{new_status}'; ownership confirmed to R117 peace; VC reset to 'not_done'.",
                ts, s["mti_id"],
            ),
        )
        counts["mti_reactivated"] += cur.rowcount

        # 2. wa_term_inventory — promote R117 ti to OWNER (un-flag if needed)
        cur = conn.execute(
            "UPDATE wa_term_inventory "
            "   SET term_owner_type = 'OWNER', delete_flagged = 0, "
            "       last_changed = ? "
            " WHERE id = ?",
            (ts, s["r117_ti"]),
        )
        counts["ti_promoted_owner"] += cur.rowcount
        # If ti_r117 was previously delete_flagged=1, count separately
        # (we already cleared the flag above; tracking is informational).

        # Demote R34 ti to XREF
        cur = conn.execute(
            "UPDATE wa_term_inventory "
            "   SET term_owner_type = 'XREF', last_changed = ? "
            " WHERE id = ?",
            (ts, s["r34_ti"]),
        )
        counts["ti_demoted_xref"] += cur.rowcount

        # 3. wa_verse_records — un-flag OWNER copies (R117 ti)
        cur = conn.execute(
            "UPDATE wa_verse_records "
            "   SET delete_flagged = 0, updated_at = ? "
            " WHERE term_inv_id = ? AND delete_flagged = 1",
            (ts, s["r117_ti"]),
        )
        counts["verses_unflagged"] += cur.rowcount

    # 4. word_registry — flip VC status so VC re-runs for the new terms
    cur = conn.execute(
        "UPDATE word_registry "
        "   SET verse_context_status = 'In Progress' "
        " WHERE no = 117 AND verse_context_status = 'Complete'"
    )
    counts["registry_updated"] = cur.rowcount

    return counts


def write_patch_record(state_before: dict, state_after: dict,
                        counts: dict, mode: str) -> str:
    os.makedirs(PATCH_DIR, exist_ok=True)
    path = os.path.join(
        PATCH_DIR, f"wa-117-peace-h7965-recovery-v1-{today_compact()}.json"
    )
    payload = {
        "patch_id": f"PATCH-{today_compact()}-H7965-RECOVERY-V1",
        "registry_no": 117,
        "registry_word": "peace",
        "rationale": (
            "Recover H7965 shalom family for R117 peace. The 2026-03-26 "
            "delete sweep removed shalom from active inventory without an "
            "exclusion_reason. The R117 description and Phase 1 strongs_list "
            "both attest H7965 was originally extracted under R117. STEP "
            "extract on 2026-05-01 confirmed the same 209-verse footprint. "
            "This patch un-flags the existing data and re-OWNs to R117 to "
            "enable Verse Context re-run."
        ),
        "mode": mode,
        "before": state_before,
        "after": state_after,
        "counts": counts,
        "scope": SCOPE,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False, default=str)
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true",
                    help="Commit changes (default is dry-run)")
    ap.add_argument("--db", default=DB_PATH)
    args = ap.parse_args()

    print(f"=== H7965 Recovery for R117 peace — {now_iso()} ===")
    print(f"  DB: {args.db}")
    print(f"  Mode: {'LIVE' if args.live else 'DRY-RUN'}")
    print(f"  Scope: {len(SCOPE)} sub-forms; {sum(s['verses'] for s in SCOPE)} verses\n")

    if args.live:
        backup = backup_db()
        print(f"  Backup written: {backup}\n")

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    conn.isolation_level = None  # manual transaction control
    conn.execute("BEGIN")

    try:
        state_before = collect_before_state(conn)
        ts = now_iso()
        counts = apply_changes(conn, ts)
        state_after = collect_before_state(conn)  # reads inside same txn

        if args.live:
            conn.execute("COMMIT")
        else:
            conn.execute("ROLLBACK")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"  FAIL: {e}")
        return 1

    print("=== Counts ===")
    for k, v in counts.items():
        print(f"  {k}: {v}")
    print()

    print("=== Per-sub-form before → after ===")
    for b, a in zip(state_before["scope"], state_after["scope"]):
        s = b["strongs"]
        mb = b["mti_primary"] or {}
        ma = a["mti_primary"] or {}
        print(f"  {s}: status {mb.get('status')!r} → {ma.get('status')!r}; "
              f"fk {mb.get('owning_registry_fk')!r} → {ma.get('owning_registry_fk')!r}; "
              f"verses_active {b['r117_verses_active']} → {a['r117_verses_active']} "
              f"({b['r117_verses_flagged']}→{a['r117_verses_flagged']} flagged)")

    print()
    print(f"=== Registry: VC status "
          f"{state_before['registry_before']['verse_context_status']!r} → "
          f"{state_after['registry_before']['verse_context_status']!r} ===")

    patch_path = write_patch_record(
        state_before, state_after, counts,
        "LIVE" if args.live else "DRY-RUN",
    )
    print(f"\nPatch record: {patch_path}")
    if not args.live:
        print("\n[DRY-RUN] No changes committed. Re-run with --live to apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
