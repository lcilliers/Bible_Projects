"""_apply_m02_dir002_c7_scope_20260619.py — apply directive DIR-20260619-002 (M02 C7 scope resolution).

Option-1 resolution (document/constrain, researcher-confirmed): C7 (Bitterness) is NT-pikria-only by design;
the OT mar/marah field is owned by M03 (Grief) via a principled sense-split. No membership change; M03 untouched.

Two writes:
  1. cluster_finding row (cluster_synthesis) recording the C7 scope resolution. obs_id = T7.1.8 (400, OT/NT
     vocabulary continuity — the question the directive's motivation cites). cluster_synthesis findings are
     cluster-level (no characteristic/subgroup link), so this does NOT require the not-yet-persisted c1-c7
     structure — C7 identity lives in the finding_text.
  2. wa_session_research_flags SD_POINTER (session_target='D') registering the M02 C7 <-> M03 bitterness seam,
     anchored registry 13 (bitterness) -> cross_registry 5 (anguish), cluster_link='M02,M03'.

Reversible: pre-run backup. No physical deletes. M02 active-term count + M03 rows asserted unchanged.

  python scripts/_apply_m02_dir002_c7_scope_20260619.py --dry-run
  python scripts/_apply_m02_dir002_c7_scope_20260619.py --live
"""
import argparse, os, shutil, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
SNAP = os.path.join("backups", "bible_research_pre-m02-dir002_20260619.db")
STAMP = "2026-06-19T00:00:00Z"

OBS_T718 = 400  # T7.1.8
FINDING_TEXT = (
    "C7 (Bitterness) is NT-pikria-only (G4088, 4 occ) by design. The OT bitterness-of-soul family "
    "(mar/marah — H4751, H4843, and the wider family) is owned and analysed in M03 (Grief). The English "
    "'bitterness' is split by sense: NT pikria/pikros = resentment/anger-bitterness (M02/M28); OT mar nephesh "
    "= grief/anguish-bitterness (M03). C7 is therefore not expanded; the OT field remains in M03."
)
CF_NOTES = ("DIR-20260619-002 (Option 1 resolution, researcher-confirmed); originating flag F-D / "
            "wa-m02-evidence-verification-v1_0-20260619.md")
SD_DESC = (
    "M02 C7 (Bitterness) <-> M03 (Grief) bitterness seam. The English 'bitterness' splits by sense: NT "
    "pikria/pikros (G4088 'bitterness', resentment/anger-bitterness; M02 C7 + M28) vs OT mar nephesh "
    "(H4751 mar, H4843 marar; grief/anguish-bitterness; owned by M03). C7 is NT-pikria-only by design; the OT "
    "field stays in M03. Surface this seam in cross-cluster synthesis. (DIR-20260619-002)"
)
SD_LABEL = "M02C7-SD001"


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    m02_before = cur.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M02' AND status IN ('extracted','extracted_thin')").fetchone()[0]
    m03_before = cur.execute("SELECT COUNT(*), COALESCE(SUM(delete_flagged),0) FROM mti_terms WHERE cluster_code='M03'").fetchone()
    dup_cf = cur.execute("SELECT COUNT(*) FROM cluster_finding WHERE cluster_code='M02' AND obs_id=? AND finding_status='cluster_synthesis' AND finding_text LIKE 'C7 (Bitterness) is NT-pikria-only%'", (OBS_T718,)).fetchone()[0]
    dup_sd = cur.execute("SELECT COUNT(*) FROM wa_session_research_flags WHERE flag_label=?", (SD_LABEL,)).fetchone()[0]
    print(f"M02 active-term count (before): {m02_before}")
    print(f"M03 mti_terms rows (before): {m03_before[0]} (delete_flagged sum {m03_before[1]})")
    print(f"existing dup cluster_finding: {dup_cf} · existing SD label '{SD_LABEL}': {dup_sd}")
    print(f"\n1. cluster_finding: M02 / obs_id={OBS_T718} (T7.1.8) / cluster_synthesis")
    print(f"   finding_text: {FINDING_TEXT[:90]}…")
    print(f"2. SD_POINTER: registry 13 (bitterness) -> cross_registry 5 (anguish) · cluster_link='M02,M03' · label={SD_LABEL}")

    if a.dry_run:
        print("\n[DRY-RUN] no changes written."); return 0
    if dup_cf or dup_sd:
        print("\nABORT: a target row already exists (idempotency guard)."); return 2

    if not os.path.exists(SNAP):
        os.makedirs("backups", exist_ok=True); shutil.copy2(DB, SNAP); print(f"\nsnapshot: {SNAP}")

    cur.execute("""INSERT INTO cluster_finding
        (obs_id, cluster_code, characteristic_id, cluster_subgroup_id, vcg_scope, finding_status,
         finding_text, source_file, version, notes, delete_flagged, created_at, last_updated_date)
        VALUES (?, 'M02', NULL, NULL, NULL, 'cluster_synthesis', ?, ?, 'v1-20260619', ?, 0, ?, ?)""",
        (OBS_T718, FINDING_TEXT, "wa-m02-marah-mar-bitterness-lookup-v1-20260619.md", CF_NOTES, STAMP, STAMP))
    cur.execute("""INSERT INTO wa_session_research_flags
        (registry_id, file_id, flag_code, flag_label, strongs_reference, cross_registry_id, priority,
         session_target, description, session_raised, raised_date, resolved, cluster_link, cluster_link_basis)
        VALUES (13, NULL, 'SD_POINTER', ?, 'G4088', 5, 'MEDIUM', 'D', ?, 'DIR-20260619-002', '2026-06-19', 0,
                'M02,M03', 'sense-split (pikria vs mar/marah)')""", (SD_LABEL, SD_DESC))
    conn.commit()

    m02_after = cur.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M02' AND status IN ('extracted','extracted_thin')").fetchone()[0]
    m03_after = cur.execute("SELECT COUNT(*), COALESCE(SUM(delete_flagged),0) FROM mti_terms WHERE cluster_code='M03'").fetchone()
    print(f"\nLIVE: cluster_finding +1, SD_POINTER +1.")
    print(f"  M02 active-term count after: {m02_after}  ({'UNCHANGED' if m02_after==m02_before else 'CHANGED!'})")
    print(f"  M03 mti_terms after: {m03_after[0]} (df {m03_after[1]})  ({'UNCHANGED' if tuple(m03_after)==tuple(m03_before) else 'CHANGED!'})")
    print(f"  integrity: {cur.execute('PRAGMA quick_check').fetchone()[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
