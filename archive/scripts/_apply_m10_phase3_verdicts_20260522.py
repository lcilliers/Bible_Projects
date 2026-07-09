"""Apply M10 Phase 3 constitution-debate verdicts.

Verdicts (per `Sessions/Session_Clusters/M10/wa-m10-phase3-constitution-verdicts-v1-20260522.md`):
  STAYS (no flag):              44 terms
  STAYS (with cross-register):  14 terms
  BOUNDARY:                      8 terms (4 empty-corpus, 1 single-verse, 1 small corpus, 1 corrected — see below)
  TRANSFERS:                     0 terms
  TOTAL:                        63 terms (chet H2399 is in the report; AI flagged a false gap)

Actions:
  1. Mic 2:10 cha.val (vr_id=232182) — Phase 1 borderline; parent verdict is STAYS.
     INSERT vc row with is_relevant=1 so Pass A can pick it up. Then run Pass A
     to author the meaning.
  2. Pro 12:21 a.ven (vr_id=157151) — Phase 1 borderline; parent verdict is BOUNDARY.
     LEAVE PARKED. No DB action. Will be addressed at Phase 8.5 with parent term.
  3. 8 BOUNDARY terms — record cluster_observation entries (one per term) for
     Phase 8.5 to resolve. observation_type='INTEGRATION_NOTE',
     source_phase='phase_3_constitution_debate',
     target_phase='phase_8_5_boundary_resolution'.
  4. Cross-register flags — recorded in the obslog narrative only (per v2_8 §6:
     flags travel via narrative + meta-fields, not as cluster_observation rows
     except where Phase 5/7 explicitly elevates them).
  5. NO mti_terms.cluster_code changes (no TRANSFERS).
"""
import sqlite3
import sys
import io
import os

if os.name == 'nt':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DB = 'database/bible_research.db'
TODAY = '2026-05-22T00:00:00Z'
PHASE3_FILE = 'Sessions/Session_Clusters/M10/wa-m10-phase3-constitution-verdicts-v1-20260522.md'

# Mic 2:10 cha.val — Phase 1 borderline that becomes relevant per AI verdict
MIC_2_10_CHAVAL = {
    "vr_id": 232182,
    "mti_id": 4648,
    "reference": "Mic 2:10",
    "strongs": "H2254B",
}

# 8 BOUNDARY terms per the AI verdict
BOUNDARY_TERMS = [
    {
        "mti_id": 75, "strongs": "H0205H", "translit": "a.ven",
        "rationale": (
            "4 active relevant meanings cover mixed content (Deu 26:14, Job 5:6, "
            "Psa 90:10, Pro 22:8). Corpus is thin and semantically mixed between "
            "moral-evil-trouble and circumstantial-suffering. Term sits between "
            "M10 (iniquity), M03 (grief), and M20 (distress). No clear primary "
            "M10 register established. Pro 12:21 borderline verse remains parked "
            "with parent. §6.3.1 reason 1 — cluster-membership undecided."
        ),
    },
    {
        "mti_id": 4646, "strongs": "H2256D", "translit": "che.vel",
        "rationale": (
            "1 verse — Mic 2:10 (destruction as active moral force arising from "
            "land's uncleanness). Sits at intersection of M10 (sin-pollution "
            "produces destruction) and M10c (defilement-produces-destruction). "
            "Single verse insufficient to confirm M10 primary over M10c. "
            "§6.3.1 reason 1."
        ),
    },
    {
        "mti_id": 6136, "strongs": "H2475", "translit": "cha.loph",
        "rationale": (
            "Zero active relevant verses (1 set_aside, 0 relevant). No meaning "
            "corpus on which to base verdict. §6.3.1 reason 1 — corpus empty."
        ),
    },
    {
        "mti_id": 746, "strongs": "H4889", "translit": "mash.chit",
        "rationale": (
            "Zero relevant verses (12 set_aside). All Pass A meanings determined "
            "physical-destruction sense outside M10 moral-failure register. "
            "§6.3.1 reason 1 — corpus has no inner-being content."
        ),
    },
    {
        "mti_id": 4904, "strongs": "H4892", "translit": "mash.chet",
        "rationale": (
            "Zero relevant verses (1 set_aside). No meaning corpus. §6.3.1 reason 1."
        ),
    },
    {
        "mti_id": 4906, "strongs": "H4893B", "translit": "ma.she.chat",
        "rationale": (
            "Zero relevant verses (1 set_aside). No meaning corpus. §6.3.1 reason 1."
        ),
    },
]


def main():
    dry = '--dry-run' in sys.argv
    conn = sqlite3.connect(DB)
    conn.execute('PRAGMA foreign_keys=ON')
    cur = conn.cursor()

    # 0. Pre-checks
    cs = cur.execute("SELECT status FROM cluster WHERE cluster_code='M10'").fetchone()
    assert cs and cs[0] == 'Data - In Progress', f"M10.status unexpected: {cs}"

    # Confirm Mic 2:10 cha.val has no vc row yet
    n = cur.execute(
        "SELECT COUNT(*) FROM verse_context "
        "WHERE verse_record_id=? AND mti_term_id=? AND COALESCE(delete_flagged,0)=0",
        (MIC_2_10_CHAVAL["vr_id"], MIC_2_10_CHAVAL["mti_id"])
    ).fetchone()[0]
    print(f"Pre-check: Mic 2:10 cha.val vc rows = {n} (expected 0)")
    assert n == 0, "Mic 2:10 vc row already exists — was Phase 1 borderline applied?"

    # Confirm BOUNDARY observations don't already exist for these terms
    existing_obs = []
    for t in BOUNDARY_TERMS:
        r = cur.execute(
            "SELECT id FROM cluster_observation "
            "WHERE cluster_code='M10' AND source_phase='phase_3_constitution_debate' "
            "AND title LIKE ? AND COALESCE(delete_flagged,0)=0",
            (f"%{t['strongs']}%",)
        ).fetchone()
        if r:
            existing_obs.append((t['strongs'], r[0]))
    if existing_obs:
        print(f"WARNING: existing Phase 3 BOUNDARY observations: {existing_obs}")
        if not dry:
            raise SystemExit("BOUNDARY observations already recorded — patch already applied?")

    # Confirm chet (H2399) is in M10 (it IS — AI flagged it incorrectly as missing)
    chet = cur.execute(
        "SELECT id, strongs_number, transliteration FROM mti_terms "
        "WHERE strongs_number='H2399' AND cluster_code='M10' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()
    assert chet, "chet (H2399) not found in M10 as expected"
    print(f"chet confirmed: id={chet[0]} {chet[1]} {chet[2]}")
    print()

    # --- Action 1: Insert vc row for Mic 2:10 cha.val (is_relevant=1) ---
    print("Action 1: INSERT vc row Mic 2:10 cha.val (is_relevant=1)")
    if not dry:
        cur.execute("""
            INSERT INTO verse_context
            (verse_record_id, mti_term_id, group_id, cluster_subgroup_id,
             is_anchor, is_relevant, is_related, delete_flagged, vertical_pass_flag)
            VALUES (?, ?, NULL, NULL, 0, 1, 0, 0, 0)
        """, (MIC_2_10_CHAVAL["vr_id"], MIC_2_10_CHAVAL["mti_id"]))
        new_vc = cur.lastrowid
        print(f"  inserted vc_id={new_vc}")

    # --- Action 2: cluster_observation rows for 8 BOUNDARY terms ---
    print()
    print(f"Action 2: INSERT {len(BOUNDARY_TERMS)} cluster_observation rows for BOUNDARY terms")
    for t in BOUNDARY_TERMS:
        title = (f"Phase 3 BOUNDARY: {t['strongs']} {t['translit']} — "
                 f"awaiting Phase 8.5 resolution")
        if dry:
            print(f"  [DRY] {title}")
        else:
            cur.execute("""
                INSERT INTO cluster_observation
                (cluster_code, characteristic_id, cluster_subgroup_id,
                 source_phase, observation_type, target_phase, title, description,
                 status, raised_date, source_file, delete_flagged,
                 created_at, last_updated_date)
                VALUES (?, NULL, NULL, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?)
            """, (
                'M10',
                'phase_3_constitution_debate',
                'INTEGRATION_NOTE',
                'phase_8_5_boundary_resolution',
                title,
                t['rationale'],
                'open',
                TODAY,
                PHASE3_FILE,
                TODAY,
                TODAY,
            ))
            print(f"  inserted: {title}")

    if dry:
        print("\n[DRY-RUN — no writes]")
        conn.close()
        return

    conn.commit()
    print()
    print("Committed.")
    print()

    # --- Post-check ---
    n_new_rel = cur.execute(
        "SELECT COUNT(*) FROM verse_context vc JOIN mti_terms mt ON mt.id=vc.mti_term_id "
        "WHERE mt.cluster_code='M10' AND vc.is_relevant=1 "
        "AND COALESCE(mt.delete_flagged,0)=0 AND COALESCE(vc.delete_flagged,0)=0"
    ).fetchone()[0]
    n_new_obs = cur.execute(
        "SELECT COUNT(*) FROM cluster_observation "
        "WHERE cluster_code='M10' AND source_phase='phase_3_constitution_debate' "
        "AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"Post-check: M10 relevant vc rows = {n_new_rel} (was 1,324; expect 1,325)")
    print(f"Post-check: M10 Phase-3 BOUNDARY observations = {n_new_obs} (expect 6)")

    conn.close()
    print()
    print("NEXT STEP: run Pass A to author Mic 2:10 cha.val meaning:")
    print("  python scripts/_run_passa_via_api_v1_20260515.py --m-cluster M10")


if __name__ == '__main__':
    main()
