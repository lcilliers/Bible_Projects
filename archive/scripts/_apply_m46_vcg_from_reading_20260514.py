"""Apply wa-cluster-M46-patch-vcg-from-reading-v1-20260514.json — Stage 2 of 2.

Operations (single transaction):
  - 12 RETAIN_REVISE: UPDATE verse_context_group.context_description
    (one entry — vcg_id 51 / 111-002 — is marked "No change"; skip)
  - 22 CREATE: INSERT new verse_context_group rows with derived group_code

Sub-group routing (Phase 7) is NOT performed here — verse_context.group_id
remains unchanged for now. The patch creates the VCG structure; Phase 7
routes verses into them.
"""
from __future__ import annotations
import argparse, json, os, shutil, sqlite3, sys
from datetime import datetime, timezone

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DB = "database/bible_research.db"
BACKUP_DIR = "backups"
PATCH_ID = "wa-cluster-M46-patch-vcg-from-reading-v1-20260514"
INPUT_JSON = "Sessions/Session_Clusters/M46/wa-cluster-M46-patch-vcg-from-reading-v1-20260514.json"


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        spec = json.load(f)

    ops = spec["vcg_operations"]
    retain = [o for o in ops if o["action"] == "RETAIN_REVISE"]
    create = [o for o in ops if o["action"] == "CREATE"]

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    ts = now_iso()

    print("=" * 72)
    print(f"  M46 VCG patch from reading — stage 2 of 2")
    print(f"  Mode: {'LIVE' if args.live else 'DRY-RUN'}")
    print(f"  RETAIN_REVISE: {len(retain)}  CREATE: {len(create)}")
    print("=" * 72)

    # ── PRE-FLIGHT ────────────────────────────────────────────────────────
    print("\nPRE-FLIGHT")
    print("-" * 72)
    ok = True

    # RETAIN_REVISE: verify each vcg_id + group_code matches existing row
    skip_unchanged = []
    revise_targets = []
    for op in retain:
        r = conn.execute(
            "SELECT id, group_code, context_description "
            "FROM verse_context_group WHERE id=? "
            "AND COALESCE(delete_flagged,0)=0",
            (op["vcg_id"],)
        ).fetchone()
        if not r:
            print(f"  ✗ RETAIN_REVISE vcg_id={op['vcg_id']} not found"); ok = False; continue
        if r["group_code"] != op["vcg_code"]:
            print(f"  ✗ vcg_id={op['vcg_id']} group_code mismatch: "
                  f"DB={r['group_code']!r} patch={op['vcg_code']!r}"); ok = False; continue
        # Check if description differs
        if r["context_description"] == op["description"]:
            skip_unchanged.append(op["vcg_id"])
        else:
            revise_targets.append(op)
    print(f"  RETAIN_REVISE verified: {len(retain)}")
    print(f"    Description unchanged (skip UPDATE): {len(skip_unchanged)} → {skip_unchanged}")
    print(f"    Description revision: {len(revise_targets)}")

    # CREATE: verify each new group_code is not already in use
    print(f"\n  CREATE pre-check:")
    for op in create:
        r = conn.execute(
            "SELECT id FROM verse_context_group WHERE group_code=? "
            "AND COALESCE(delete_flagged,0)=0",
            (op["vcg_code"],)
        ).fetchone()
        if r:
            print(f"    ✗ {op['vcg_code']} already exists at vcg_id={r['id']}"); ok = False; continue
        # Verify mti_id exists
        mt = conn.execute(
            "SELECT id, strongs_number FROM mti_terms WHERE id=?", (op["mti_id"],)
        ).fetchone()
        if not mt:
            print(f"    ✗ mti_id={op['mti_id']} for {op['vcg_code']} not found"); ok = False; continue
    print(f"    CREATE codes: {len(create)} ready")

    if not ok:
        print("\nPRE-FLIGHT FAILED")
        return 1

    if not args.live:
        print("\n[DRY-RUN] no changes. Re-run with --live.")
        return 0

    # ── LIVE APPLY ────────────────────────────────────────────────────────
    os.makedirs(BACKUP_DIR, exist_ok=True)
    bp = os.path.join(BACKUP_DIR,
                      f"bible_research_pre_m46_vcg_patch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db")
    shutil.copy2(DB, bp)
    print(f"\nBackup: {bp}\n")

    try:
        conn.execute("BEGIN")
        cur = conn.cursor()

        # 1. UPDATE verse_context_group.context_description for revise targets
        for op in revise_targets:
            cur.execute(
                "UPDATE verse_context_group SET context_description=? WHERE id=?",
                (op["description"], op["vcg_id"])
            )
            if cur.rowcount != 1:
                raise RuntimeError(f"RETAIN_REVISE vcg_id={op['vcg_id']}: {cur.rowcount}")
        print(f"  ✓ UPDATEd {len(revise_targets)} verse_context_group descriptions")

        # 2. INSERT new verse_context_group rows
        new_vcg_ids = []
        for op in create:
            cur.execute(
                "INSERT INTO verse_context_group "
                "  (group_code, context_description, notes, delete_flagged, "
                "   vertical_pass_flag) "
                "VALUES (?, ?, ?, 0, 0)",
                (op["vcg_code"], op["description"],
                 f"{PATCH_ID}: subgroup={op.get('subgroup','?')} — {op.get('note','')}")
            )
            new_vcg_ids.append((cur.lastrowid, op["vcg_code"]))
        print(f"  ✓ INSERTed {len(new_vcg_ids)} new verse_context_group rows")

        # FK check + commit
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {fkv[:3]}")
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"\nROLLED BACK: {e}")
        return 1

    # ── VERIFICATION ──────────────────────────────────────────────────────
    print("\nVERIFICATION")
    print("-" * 72)

    print(f"\n  New VCG rows (sample):")
    for vcg_id, code in new_vcg_ids[:5]:
        print(f"    vcg_id={vcg_id} {code}")
    if len(new_vcg_ids) > 5:
        print(f"    ... and {len(new_vcg_ids) - 5} more")

    # Per-subgroup VCG count summary (informational — VCGs aren't directly
    # linked to sub-groups in the schema; the patch's `subgroup` field is
    # documentary for Phase 7 routing)
    print(f"\n  VCGs by intended sub-group (per patch authoring):")
    from collections import Counter
    by_sg = Counter()
    for op in retain:
        by_sg[op.get("subgroup", "?")] += 1
    for op in create:
        by_sg[op.get("subgroup", "?")] += 1
    for sg, n in sorted(by_sg.items()):
        print(f"    {sg:<8} {n}")

    # Total M46-relevant VCGs (term-prefixed group_code matching M46 mti_ids)
    n_total = conn.execute("""
        SELECT COUNT(*) FROM verse_context_group vcg
         WHERE COALESCE(vcg.delete_flagged,0)=0
           AND EXISTS (
             SELECT 1 FROM mti_terms mt
              WHERE mt.cluster_code='M46'
                AND COALESCE(mt.delete_flagged,0)=0
                AND vcg.group_code LIKE mt.id || '-%'
           )
    """).fetchone()[0]
    print(f"\n  Total M46-term VCGs in DB now: {n_total}")

    conn.close()
    print(f"\n[LIVE] VCG patch applied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
