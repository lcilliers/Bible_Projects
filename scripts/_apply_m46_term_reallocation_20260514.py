"""M46 — term reallocation per researcher-directed extract.

Input: Sessions/Session_Clusters/M46/WA-M46-term-reallocation-v1-20260514.json

7 terms move out of M46 to destination clusters (primary_destination only):
  - H1433 go.del (mti=649)    → M22   (VCG 649-002 split to M08 flagged as OQ-R01)
  - H1420 ge.dul.lah (mti=6903) → M22
  - H8588 ta.a.nug (mti=792)   → M04
  - H4768 mar.bit (mti=2876)   → M23  (OQ-R04 — FLAG vs M23)
  - G0019 agathōsunē (mti=885) → M39  (vc_completed; 140+ R067 findings travel with term)
  - G2770 kerdainō (mti=1331)  → M37  (OQ-R02 — M37 vs M36)
  - H4766 mar.veh (mti=2879)   → M33  (OQ-R03 — M33 vs M18)

Mechanism: UPDATE mti_terms.cluster_code only. All term-keyed data (verse_context,
verse_context_group, vcg_term, mti_term_subgroup, findings) travels automatically.

Researcher open questions (OQ-R01..R04) surfaced in the application report.
"""
from __future__ import annotations
import argparse, os, shutil, sqlite3, sys, json
from datetime import datetime, timezone

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DB = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
DIRECTIVE_LABEL = "M46_TERM_REALLOC_20260514"
INPUT_JSON = os.path.join("Sessions", "Session_Clusters", "M46",
                          "WA-M46-term-reallocation-v1-20260514.json")


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def take_backup():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    p = os.path.join(BACKUP_DIR, f"bible_research_pre_m46_realloc_{ts}.db")
    shutil.copy2(DB, p)
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        spec = json.load(f)

    reallocs = spec["reallocations"]

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    ts = now_iso()

    print("=" * 72)
    print(f"  M46 term reallocation — {len(reallocs)} terms")
    print(f"  Mode: {'LIVE' if args.live else 'DRY-RUN'}")
    print("=" * 72)

    # ── PRE-FLIGHT ─────────────────────────────────────────────────────────
    print("\nPRE-FLIGHT")
    print("-" * 72)
    ok = True
    plan = []
    for r in reallocs:
        mti_id = r["mti_id"]
        strongs = r["strong"]
        target = r["reallocation"]["primary_destination_cluster"]
        target_name = r["reallocation"]["primary_destination_name"]

        # Verify current state
        row = conn.execute(
            "SELECT id, strongs_number, transliteration, cluster_code, "
            "       vc_status, md_version, COALESCE(delete_flagged,0) deleted "
            "FROM mti_terms WHERE id=?",
            (mti_id,)
        ).fetchone()
        if not row:
            print(f"  [ERR] mti={mti_id} {strongs} NOT FOUND")
            ok = False; continue
        if row["strongs_number"] != strongs:
            print(f"  [ERR] mti={mti_id} expected {strongs} found {row['strongs_number']}")
            ok = False; continue
        if row["cluster_code"] != "M46":
            print(f"  [ERR] mti={mti_id} {strongs} cluster_code={row['cluster_code']} (expected M46)")
            ok = False; continue
        if row["deleted"]:
            print(f"  [ERR] mti={mti_id} {strongs} delete_flagged=1")
            ok = False; continue

        # Verify destination cluster exists
        dest = conn.execute("SELECT cluster_code, status FROM cluster WHERE cluster_code=?",
                            (target,)).fetchone()
        if not dest:
            print(f"  [ERR] destination cluster {target} not found")
            ok = False; continue

        # Count term-attached data that will travel
        vr_count = conn.execute(
            "SELECT COUNT(*) FROM wa_verse_records WHERE mti_term_id=? "
            "AND COALESCE(delete_flagged,0)=0", (mti_id,)
        ).fetchone()[0]
        vc_count = conn.execute(
            "SELECT COUNT(*) FROM verse_context WHERE mti_term_id=? "
            "AND COALESCE(delete_flagged,0)=0", (mti_id,)
        ).fetchone()[0]
        vcg_count = conn.execute(
            "SELECT COUNT(*) FROM verse_context_group "
            "WHERE group_code LIKE ? AND COALESCE(delete_flagged,0)=0",
            (f"{mti_id}-%",)
        ).fetchone()[0]
        mts_count = conn.execute(
            "SELECT COUNT(*) FROM mti_term_subgroup WHERE mti_term_id=? "
            "AND COALESCE(delete_flagged,0)=0", (mti_id,)
        ).fetchone()[0]

        print(f"  ✓ mti={mti_id:<5} {strongs:<7} {row['transliteration']:<14} "
              f"M46→{target:<5} ({target_name})")
        print(f"      vr={vr_count} vc={vc_count} vcg={vcg_count} placements={mts_count} "
              f"vc_status={row['vc_status']} md_v={row['md_version']}")
        plan.append({
            "mti_id": mti_id, "strongs": strongs,
            "translit": row["transliteration"],
            "from": "M46", "to": target, "target_name": target_name,
            "vr_count": vr_count, "vc_count": vc_count,
            "vcg_count": vcg_count, "placement_count": mts_count,
        })

    if not ok:
        print("\nPRE-FLIGHT FAILED")
        return 1

    # Baseline counts
    n_m46_before = conn.execute(
        "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M46' "
        "AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"\n  M46 active term count (pre): {n_m46_before}")

    if not args.live:
        print("\n[DRY-RUN] no changes. Re-run with --live to apply.")
        return 0

    # ── LIVE APPLY ─────────────────────────────────────────────────────────
    backup = take_backup()
    print(f"\nBackup: {backup}\n")

    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        for p in plan:
            cur.execute(
                "UPDATE mti_terms SET cluster_code=?, last_changed=? WHERE id=?",
                (p["to"], ts, p["mti_id"])
            )
            if cur.rowcount != 1:
                raise RuntimeError(f"mti_id={p['mti_id']} UPDATE affected {cur.rowcount} rows")
            # If any mti_term_subgroup placement exists for M46 (shouldn't, but be safe)
            if p["placement_count"]:
                cur.execute("""
                    UPDATE mti_term_subgroup SET delete_flagged=1, last_updated_date=?
                     WHERE mti_term_id=?
                       AND cluster_subgroup_id IN (
                         SELECT id FROM cluster_subgroup WHERE cluster_code='M46'
                       )
                       AND COALESCE(delete_flagged,0)=0
                """, (ts, p["mti_id"]))

        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {fkv[:3]}")
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"\nROLLED BACK: {e}")
        return 1

    # ── VERIFICATION ───────────────────────────────────────────────────────
    print("VERIFICATION")
    print("-" * 72)

    n_m46_after = conn.execute(
        "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M46' "
        "AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"\n  M46 active term count: {n_m46_before} → {n_m46_after} "
          f"(Δ {n_m46_after - n_m46_before})")

    print(f"\n  Per-term verification:")
    for p in plan:
        r = conn.execute(
            "SELECT cluster_code FROM mti_terms WHERE id=?", (p["mti_id"],)
        ).fetchone()
        marker = "✓" if r["cluster_code"] == p["to"] else "✗"
        print(f"    {marker} mti={p['mti_id']:<5} {p['strongs']:<7} → {r['cluster_code']}")

    print(f"\n  Destination cluster term counts post-reallocation:")
    targets = sorted(set(p["to"] for p in plan))
    for t in targets:
        n = conn.execute(
            "SELECT COUNT(*) FROM mti_terms WHERE cluster_code=? "
            "AND COALESCE(delete_flagged,0)=0", (t,)
        ).fetchone()[0]
        gained = sum(1 for p in plan if p["to"] == t)
        print(f"    {t}: {n} terms (+{gained} from M46)")

    print(f"\n  Remaining M46 active terms:")
    for r in conn.execute("""
        SELECT id, strongs_number, transliteration, gloss, vc_status
          FROM mti_terms WHERE cluster_code='M46' AND COALESCE(delete_flagged,0)=0
         ORDER BY strongs_number
    """):
        print(f"    mti={r['id']:<5} {r['strongs_number']:<8} {r['transliteration']:<14} "
              f"{(r['gloss'] or '')[:30]:<30} vc_status={r['vc_status']}")

    conn.close()
    print(f"\n[LIVE] M46 term reallocation applied.")
    print(f"\nOpen questions for researcher (from input JSON):")
    print(f"  OQ-R01: H1433 go.del — VCG 649-002 split to M08 pending decision")
    print(f"  OQ-R02: G2770 kerdainō — M37 (applied) vs M36; confirm or revise")
    print(f"  OQ-R03: H4766 mar.veh — M33 (applied) vs M18 Hope; confirm or revise")
    print(f"  OQ-R04: H4768 mar.bit — M23 (applied) vs FLAG (extracted_thin); confirm or revise")
    return 0


if __name__ == "__main__":
    sys.exit(main())
