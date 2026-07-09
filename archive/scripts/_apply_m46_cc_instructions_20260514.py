"""Apply WA-M46-cc-instructions-v1-20260514 action groups 1-4.

Group 5 (Session A extraction for 8 new wealth/poverty terms) is queued
separately — see outputs/markdown/m46-session-a-extraction-brief-v1-20260514.md.

Pre-flight resolutions applied:
  - H4924 → H4924B (DB uses suffixed form)
  - G842  → G0842  (DB uses leading-zero Greek)
  - H7961 → BLOCKED (DB has 'sha.lev' not 'shal.a.nan'; directive's VERIFY flag warranted)
  - H8080 mti=4697 (translit drift 'sha.men' vs 'sha.man'; Strong's + gloss match)
  - Action group 2 vc_ids: directive listed vr_ids; real vc_ids are 61187, 61188
  - Action group 3 vc_id: directive listed vr_id 58191; real vc_id is 531
"""
from __future__ import annotations
import argparse, os, shutil, sqlite3, sys
from datetime import datetime, timezone

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DB = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
DIRECTIVE_LABEL = "M46_CC_INSTR_D1-D7_20260514"

# Group 1 — resolved (mti_id, strongs, translit) - 7 confirmed; H7961 blocked
GROUP_1_REBINDS = [
    (4695, "H8082",  "sha.men"),
    (4697, "H8080",  "sha.men"),   # directive says 'sha.man'; DB has 'sha.men'; gloss matches
    (4696, "H4924B", "mish.man"),  # directive said H4924; DB uses suffixed H4924B
    (4898, "G0842",  "autarkēs"),  # directive said G842; DB uses leading-zero
    (3836, "H5727",  "a.dan"),
    (7109, "H2630",  "cha.san"),
    (4702, "G3045",  "liparos"),
]
GROUP_1_BLOCKED = [
    ("H7961", "shal.a.nan",
     "DB has H7961='sha.lev' (at ease) not 'shal.a.nan'. No term matching 'shal.a.nan' "
     "found by Strong's or translit search. Directive's VERIFY flag warranted; "
     "researcher to provide correct Strong's or correct the translit assumption."),
]

# Group 2 — M46 → M22 ke.vud.dah
GROUP_2_TERM_MTI = 1870  # H3520B ke.vud.dah
GROUP_2_FROM = "M46"
GROUP_2_TO   = "M22"

# Group 3 — VCG 51 (111-002) cross-cluster: route Psa 23:5 vc row to M39-A
# Term (mti=111 da.shen) stays in M46; only the verse routing changes.
GROUP_3_VC_ID = 531
GROUP_3_TARGET_SUBGROUP_ID = 42  # M39-A
GROUP_3_NOTE = (
    "Cross-cluster VCG split per WA-M46-cc-instructions D7A: "
    "H1878 da.shen group 111-002 (anointing) routed to M39-A while term remains in M46. "
    "Verse: Psa 23:5 — anointing oil as emblem of divine blessing upon the inner person."
)

# Group 4 — autarkeia (G0841, mti=743) shared with M46: 2 new vc rows
GROUP_4_MTI = 743  # G0841 autarkeia
GROUP_4_NEW_ROWS = [
    # (verse_record_id, reference_for_log, rationale)
    (148147, "1Ti 6:6",
     "Godliness with contentment (autarkeia) is great gain — wealth-domain framing; "
     "M46 shared-term row. Term remains in M15 cluster (mti.cluster_code unchanged); "
     "this is a parallel vc row registering the verse to M46 scope."),
    (15117,  "2Cor 9:8",
     "Having all sufficiency (autarkeia) in all things so that you may abound in every "
     "good work — material sufficiency enabling generosity; M46 shared-term row. "
     "Term remains in M15 cluster (mti.cluster_code unchanged); this is a parallel "
     "vc row registering the verse to M46 scope."),
]


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def take_backup():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    p = os.path.join(BACKUP_DIR, f"bible_research_pre_m46_cc_instr_{ts}.db")
    shutil.copy2(DB, p)
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    ts = now_iso()

    print("=" * 72)
    print(f"  WA-M46-cc-instructions-v1-20260514 — action groups 1-4")
    print(f"  Mode: {'LIVE' if args.live else 'DRY-RUN'}")
    print("=" * 72)

    # ── PRE-FLIGHT ─────────────────────────────────────────────────────────
    print("\nPRE-FLIGHT")
    print("-" * 72)
    ok = True

    # Group 1 verification
    print("\n  Group 1 (T2 → M46): 7 confirmed, 1 blocked")
    for mti, strongs, translit in GROUP_1_REBINDS:
        r = conn.execute(
            "SELECT id, strongs_number, transliteration, cluster_code "
            "FROM mti_terms WHERE id=? AND COALESCE(delete_flagged,0)=0",
            (mti,)
        ).fetchone()
        if not r:
            print(f"    ✗ mti={mti} {strongs} NOT FOUND"); ok = False; continue
        if r["strongs_number"] != strongs:
            print(f"    ✗ mti={mti} expected {strongs} got {r['strongs_number']}"); ok = False; continue
        if r["cluster_code"] != "T2":
            print(f"    ✗ mti={mti} {strongs} cluster={r['cluster_code']} (expected T2)"); ok = False; continue
        print(f"    ✓ mti={mti:<5} {strongs:<7} '{r['transliteration']}' T2 → M46")
    for strongs, translit, reason in GROUP_1_BLOCKED:
        print(f"    ⚠ {strongs:<7} BLOCKED: {reason}")

    # Group 2
    print("\n  Group 2 (M46 → M22): ke.vud.dah mti=1870")
    r = conn.execute("SELECT strongs_number, cluster_code FROM mti_terms WHERE id=?",
                     (GROUP_2_TERM_MTI,)).fetchone()
    if not r or r["strongs_number"] != "H3520B" or r["cluster_code"] != "M46":
        print(f"    ✗ pre-state mismatch: {r and dict(r)}"); ok = False
    else:
        print(f"    ✓ mti=1870 H3520B in M46")

    # Group 3
    print("\n  Group 3 (VCG 111-002 routed to M39-A): vc_id=531")
    r = conn.execute("""SELECT vc.verse_record_id, vc.mti_term_id, vc.group_id,
                               vc.cluster_subgroup_id, vr.reference
                        FROM verse_context vc
                        JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
                        WHERE vc.id=?""", (GROUP_3_VC_ID,)).fetchone()
    if not r or r["mti_term_id"] != 111 or r["group_id"] != 51:
        print(f"    ✗ pre-state mismatch: {r and dict(r)}"); ok = False
    else:
        print(f"    ✓ vc_id=531 ({r['reference']}) mti=111 group_id=51 "
              f"current cluster_subgroup_id={r['cluster_subgroup_id']}")

    # Verify M39-A sub-group exists
    sg = conn.execute("SELECT cluster_code, subgroup_code FROM cluster_subgroup WHERE id=?",
                      (GROUP_3_TARGET_SUBGROUP_ID,)).fetchone()
    if not sg or sg["cluster_code"] != "M39" or sg["subgroup_code"] != "M39-A":
        print(f"    ✗ M39-A sub-group not at id={GROUP_3_TARGET_SUBGROUP_ID}"); ok = False
    else:
        print(f"    ✓ target sub-group M39-A id={GROUP_3_TARGET_SUBGROUP_ID}")

    # Group 4
    print("\n  Group 4 (autarkeia G0841 shared with M46): 2 new vc rows")
    r = conn.execute(
        "SELECT strongs_number, cluster_code FROM mti_terms WHERE id=?",
        (GROUP_4_MTI,)
    ).fetchone()
    if not r or r["strongs_number"] != "G0841":
        print(f"    ✗ mti=743 not G0841: {r and dict(r)}"); ok = False
    else:
        print(f"    ✓ mti=743 G0841 cluster={r['cluster_code']} (unchanged; M46 row is parallel)")
    for vr_id, ref, _rationale in GROUP_4_NEW_ROWS:
        r = conn.execute("SELECT reference FROM wa_verse_records WHERE id=?", (vr_id,)).fetchone()
        if not r:
            print(f"    ✗ vr={vr_id} NOT FOUND"); ok = False
        else:
            print(f"    ✓ vr={vr_id} '{r['reference']}'")

    n_m46_before = conn.execute(
        "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M46' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    n_t2_before = conn.execute(
        "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='T2' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"\n  Pre-state: M46={n_m46_before} active terms; T2={n_t2_before} active terms")

    if not ok:
        print("\nPRE-FLIGHT FAILED")
        return 1

    if not args.live:
        print("\n[DRY-RUN] no changes. Re-run with --live.")
        return 0

    # ── LIVE APPLY ─────────────────────────────────────────────────────────
    backup = take_backup()
    print(f"\nBackup: {backup}\n")

    try:
        conn.execute("BEGIN")
        cur = conn.cursor()

        # Group 1 — TERM_REBIND T2 → M46 (7 terms)
        print("Group 1 — T2 → M46 rebind (7 terms)")
        for mti, strongs, translit in GROUP_1_REBINDS:
            cur.execute(
                "UPDATE mti_terms SET cluster_code='M46', last_changed=? WHERE id=?",
                (ts, mti)
            )
            if cur.rowcount != 1:
                raise RuntimeError(f"mti={mti} UPDATE affected {cur.rowcount}")
        print(f"  ✓ 7 mti_terms.cluster_code rebinds")

        # Group 2 — TERM_REBIND M46 → M22 (ke.vud.dah). VCG + verses follow term.
        print("Group 2 — M46 → M22 rebind (ke.vud.dah)")
        cur.execute(
            "UPDATE mti_terms SET cluster_code='M22', last_changed=? WHERE id=?",
            (ts, GROUP_2_TERM_MTI)
        )
        if cur.rowcount != 1:
            raise RuntimeError(f"ke.vud.dah rebind affected {cur.rowcount}")
        print(f"  ✓ mti=1870 H3520B M46 → M22")

        # Group 3 — VCG 111-002 cross-cluster route (Psa 23:5 → M39-A)
        print("Group 3 — VCG 111-002 cross-cluster route to M39-A")
        cur.execute(
            "UPDATE verse_context "
            "   SET cluster_subgroup_id=?, "
            "       notes=COALESCE(notes,'') || ?, "
            "       analysis_note=? "
            " WHERE id=?",
            (GROUP_3_TARGET_SUBGROUP_ID,
             f" | {GROUP_3_NOTE}",
             GROUP_3_NOTE,
             GROUP_3_VC_ID)
        )
        if cur.rowcount != 1:
            raise RuntimeError(f"vc={GROUP_3_VC_ID} UPDATE affected {cur.rowcount}")
        print(f"  ✓ vc_id=531 cluster_subgroup_id → M39-A; cross-cluster note recorded")

        # Group 4 — autarkeia parallel vc rows for M46
        print("Group 4 — autarkeia G0841 parallel vc rows for M46")
        for vr_id, ref, rationale in GROUP_4_NEW_ROWS:
            cur.execute(
                "INSERT INTO verse_context "
                "  (verse_record_id, mti_term_id, group_id, cluster_subgroup_id, "
                "   is_anchor, is_relevant, is_related, "
                "   notes, analysis_note, delete_flagged) "
                "VALUES (?, ?, NULL, NULL, 0, 1, 0, ?, ?, 0)",
                (vr_id, GROUP_4_MTI,
                 f"M46 shared-term VCNEW per WA-M46-cc-instructions D3 (parallel to M15 row); "
                 f"ref={ref}",
                 rationale)
            )
            print(f"  ✓ INSERT vc for vr={vr_id} ({ref}) mti=743 — id={cur.lastrowid}")

        # FK check + commit
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {fkv[:3]}")
        conn.commit()
        print("\nCommit OK.\n")

        # ── VERIFICATION ───────────────────────────────────────────────────
        print("VERIFICATION")
        print("-" * 72)
        n_m46_after = conn.execute(
            "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M46' AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        n_t2_after = conn.execute(
            "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='T2' AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        n_m22_after = conn.execute(
            "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M22' AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        print(f"  M46: {n_m46_before} → {n_m46_after} (Δ {n_m46_after - n_m46_before})")
        print(f"  T2:  {n_t2_before} → {n_t2_after} (Δ {n_t2_after - n_t2_before})")
        print(f"  M22: → {n_m22_after}")

        print("\n  M46 active terms after:")
        for r in conn.execute("""SELECT id, strongs_number, transliteration, gloss
                                 FROM mti_terms WHERE cluster_code='M46'
                                   AND COALESCE(delete_flagged,0)=0
                                 ORDER BY strongs_number"""):
            print(f"    mti={r['id']:<5} {r['strongs_number']:<8} {r['transliteration']:<14} {(r['gloss'] or '')[:30]}")

        # Group 3 verify
        r = conn.execute("SELECT cluster_subgroup_id, analysis_note FROM verse_context WHERE id=?",
                         (GROUP_3_VC_ID,)).fetchone()
        print(f"\n  Group 3 vc_id=531 post-state: cluster_subgroup_id={r['cluster_subgroup_id']}")

        # Group 4 verify
        n_autarkeia = conn.execute(
            "SELECT COUNT(*) FROM verse_context WHERE mti_term_id=743 AND COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        print(f"  Group 4: autarkeia vc rows total now: {n_autarkeia} (was 2, +2 = 4 expected)")

    except Exception as e:
        conn.rollback()
        print(f"\nROLLED BACK: {e}")
        return 1

    conn.close()
    print(f"\n[LIVE] Action groups 1-4 applied.")
    print(f"\nBLOCKED items requiring researcher resolution:")
    for strongs, translit, reason in GROUP_1_BLOCKED:
        print(f"  {strongs} '{translit}' — {reason}")
    print(f"\nAction group 5 (Session A extraction) — see brief at:")
    print(f"  outputs/markdown/m46-session-a-extraction-brief-v1-20260514.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
