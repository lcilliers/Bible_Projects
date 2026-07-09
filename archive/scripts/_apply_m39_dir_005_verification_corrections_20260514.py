"""Apply DIR-20260514-005 — M39 Phase 10 verification-corrections + closure.

Per v1_11 §13.7 / §13.9 packaged-directive discipline: single transaction
carrying all Phase 10 operations including the Analysis Completed status
flip as the final operation.

Operations (all in one transaction):
  1. BOUNDARY exit: H2868 te.ev → cluster reassignment to M04
  2. BOUNDARY exit: G1435 dōron → promote to M39-A
  3. BOUNDARY exit: H7862 shay → set aside (3 verse_context rows)
  4. cluster_finding INSERT: shay-specific BOUNDARY characterisation at T1.2.1
  5. cluster_finding INSERT: 2 T5.7.2 rows (M39-A finding, M39-B silent)
  6. cluster_finding UPDATE (append): dōron supplementary findings to existing
     M39-A rows at 7 prompts (T0.4.1, T1.2.1, T2.3.1, T2.6.1, T3.9.1, T4.2.1, T6.3.1)
  7. cluster_finding gap resolution: T6.7.1 [A] + T6.7.1 [B] UPDATEs;
     T6.7.3 [CLUSTER] INSERT (no existing CLUSTER-scope row to UPDATE)
  8. cluster.status: 'Analysis - In Progress' → 'Analysis Completed'

Schema deviations from directive text (applied per actual schema):
  - wa_obs_question_catalogue.prompt_code → actual: question_code
  - cluster_finding unique constraint: (obs_id, cluster_code, cluster_subgroup_id, version)
  - Op 7 Step 4: T6.7.3 [CLUSTER] is missing in DB — INSERT rather than UPDATE
  - Op 6 dōron supplementary: APPEND to existing finding_text (single row per
    prompt × scope) rather than INSERT-with-new-version
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
DIRECTIVE_ID = "DIR-20260514-005"
CLUSTER_CODE = "M39"

# Resolved ids (verified by preflight):
SG_A = 42
SG_B = 43
SG_BOUNDARY = 44
OBS = {
    "T1.2.1": 239, "T5.7.2": 367, "T6.7.1": 390, "T6.7.3": 392,
    "T0.4.1": 233, "T2.3.1": 267, "T2.6.1": 276, "T3.9.1": 315,
    "T4.2.1": 328, "T6.3.1": 375,
}

# Op 3 — shay set-aside (3 verses)
SHAY_SET_ASIDE_REASON = (
    "H7862 shay names tribute/homage brought to God expressing reverence and "
    "acknowledgment of supremacy — inner-being register is reverence/awe rather "
    "than grace or goodness; outside M39 characteristic scope."
)

# Op 4 — shay-specific BOUNDARY characterisation
SHAY_BOUNDARY_TEXT = (
    "H7862 shay (gift/tribute): structural role in M39 economy — quality marker "
    "of reverence. Three verses (Psa 68:29; Psa 76:11; Isa 18:7) all name "
    "tribute/gift brought to God from peoples and kings as the expression of "
    "inner homage and acknowledgment of divine supremacy. The inner-being content "
    "is reverence and subordination, not grace or goodness. The term functions as "
    "a marker of the reverential inner posture from which gift-bringing flows, "
    "making its inner-being register adjacent to fear/awe (M01) rather than M39. "
    "All three verses set aside within M39 (is_relevant=0)."
)

# Op 5 — T5.7.2 rows
T572_A_TEXT = (
    "Generational consequence is explicitly evidenced in M39-A. The Abrahamic "
    "blessing-deposit (ba.rakh group 1299-001 — Gen 12:3; 22:18; 26:4; 28:14) "
    "passes generationally through the offspring, constituting subsequent "
    "generations' identity and vocation: \"in your offspring all the families of "
    "the earth shall be blessed\" (Gen 22:18). The charisma-deposit (1301-001 — "
    "Rom 11:29: \"the gifts and the calling of God are irrevocable\") names the "
    "charismata as permanently carried forward beyond the individual — not "
    "diminished by use or time. The generational deposit is forward-scoped by "
    "design: what God gives in grace to one generation constitutes the inherited "
    "standing of those who follow."
)
T572_B_TEXT = (
    "S — T2.8 found no constitutional body deposit for the goodness "
    "characteristic in M39-B's verse set. T5.7.2 is accordingly closed. No "
    "generational deposit evidenced for goodness in M39-B."
)

# Op 6 — dōron supplementary additions (to APPEND to existing M39-A rows)
DORON_APPEND = {
    "T0.4.1": (
        "Heb 11:4 (6837-001): Abel's gift accepted by God and Cain's not — the "
        "gift-offering as a typological site where right inner orientation "
        "determines divine acceptance (ra.tsah). The accepted offering points "
        "to the one whose inner trust makes the gift acceptable; the rejected "
        "offering points to the absence of that orientation."
    ),
    "T1.2.1": (
        "G1435 dōron adds the material-offering mode: the gift-as-enacted-object "
        "is the grace-characteristic in its liturgical and devotional form — the "
        "physical vehicle through which the inner disposition of grace-toward-God "
        "is enacted."
    ),
    "T2.3.1": (
        "Mat 5:23–24 (6837-002): \"if you are offering your gift at the altar "
        "and there remember that your brother has something against you, leave "
        "your gift there before the altar and go. First be reconciled to your "
        "brother, and then come and offer your gift.\" The conscience's voice "
        "interrupts the gift-act — the inner moral claim of relational "
        "obligation overrides the external offering. The heart's awareness of "
        "broken relationship takes precedence over liturgical performance."
    ),
    "T2.6.1": (
        "The dōron corpus (6837-001 through 6837-006) is consistently embodied: "
        "the term names the material object the hands bring to the altar. The "
        "hands are the implicit body-part agent of the offering-act. The "
        "grace-characteristic in its gift-offering form is enacted through the "
        "hands as the physical mediating instrument."
    ),
    "T3.9.1": (
        "Heb 9:9 (6837-004): \"gifts and sacrifices are offered that cannot "
        "perfect the conscience of the worshipper.\" This is the definitive "
        "dōron-conscience text within M39-A: the grace-vocabulary's external "
        "form (gift/dōron) is explicitly named as insufficient to address the "
        "conscience. Grace in its fullest form (charis — Eph 2:8) is what the "
        "conscience requires; external gift-offerings cannot deliver it."
    ),
    "T4.2.1": (
        "Luk 21:4 (6837-006): \"she out of her poverty put in all she had to "
        "live on.\" The widow's total self-offering from inner trust is the "
        "most complete human-to-God giving-act in the dōron corpus — complete "
        "inner surrender expressed through complete material offering. "
        "Mat 2:11 (6837-001): the Magi's gifts as an act of inner worship and "
        "prostration before the child. Both verses evidence the human-to-God "
        "direction of grace enacted through material gift."
    ),
    "T6.3.1": (
        "Mat 15:5 / Mar 7:11 (6837-003 — Corban): \"whatever you would have "
        "gained from me is given to God.\" The grace-vocabulary of gift-to-God "
        "(dōron/korban) is here deployed to evade the obligation of care for "
        "parents — the gift-to-God designation cancels the debt-to-parents. "
        "This is the corrupted gift-characteristic: grace-vocabulary "
        "weaponised as the instrument of moral evasion. The characteristic "
        "produces its opposite through legal exploitation of its form."
    ),
}

# Op 7 — dimensional sharing resolution
T671_A_TEXT = (
    "M39-A's 23 active VCGs carry 5 of the programme's 11 analytical dimensions: "
    "06 — Relational Disposition (14 VCGs — dominant), 05 — Moral Character (4), "
    "11 — Divine-Human Correspondence (3), 04 — Volition (1), 01 — Emotion — "
    "Positive (1). The sub-group's dimensional signature is relational "
    "disposition: more than half of M39-A's VCGs sit in that register, consistent "
    "with grace as constitutively a disposition of one party toward another. The "
    "full 5-dimension set is shared with 14+ other M-clusters (M02, M03, M04, M05, "
    "M08, M09, M10, M18, M19, M22, M23, M26, M27, M28); M39-A occupies the core "
    "inner-being dimensional space rather than a rare corner."
)
T671_B_TEXT = (
    "M39-B's 4 active VCGs carry 3 dimensions: 01 — Emotion — Positive (2 VCGs — "
    "dominant), 05 — Moral Character (1), 03 — Cognition (1). The sub-group's "
    "dimensional signature is positive emotion, consistent with the affective-"
    "gladness pole of tov/ya.tav. All 3 dimensions are shared with 15+ other "
    "M-clusters; M39-B sits in the affective register that M04 (Joy), M22 (Praise), "
    "and M33 (Peace) also occupy."
)
T673_CLUSTER_TEXT = (
    "M39 carries 6 of the programme's 11 dimensions across its sub-groups; shares "
    "≥1 dimension with 45 other M-clusters. 19 clusters share all 6 of M39's "
    "dimensions, placing M39 firmly in the core inner-being dimensional register, "
    "not at a rare-dimension corner. The discriminating signal is at sub-group "
    "level rather than cluster level: M39-A on 06 — Relational Disposition, "
    "M39-B on 01 — Emotion — Positive. The lowest-sharing M-clusters with M39 "
    "are M15 (wisdom — 1 shared dimension: 03 — Cognition) and M20 "
    "(doubt/despair/anxiety — 1 shared dimension: 05 — Moral Character); these "
    "two complete clusters sit furthest from grace and goodness on the "
    "dimensional axis."
)


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def take_backup():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    p = os.path.join(BACKUP_DIR, f"bible_research_pre_m39_dir005_{ts}.db")
    shutil.copy2(DB, p)
    return p


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    if not args.dry_run and not args.live:
        print("ERROR: pass --dry-run or --live", file=sys.stderr)
        return 2

    print("=" * 72)
    print(f"{DIRECTIVE_ID} apply — M39 Phase 10 verification-corrections + closure")
    print(f"Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print("=" * 72)

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    ts = now_iso()

    # ── PRE-FLIGHT ────────────────────────────────────────────────────────
    print("\nPRE-FLIGHT")
    print("-" * 72)
    ok = True

    # cluster status pre-state
    cs = conn.execute("SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER_CODE,)).fetchone()
    print(f"  cluster.status: {cs['status']!r}")
    if cs["status"] != "Analysis - In Progress":
        print(f"  [ERR] expected 'Analysis - In Progress'")
        ok = False

    # BOUNDARY terms pre-state
    for mti_id, expected_strong in [(633, "H2868"), (6837, "G1435"), (2976, "H7862")]:
        r = conn.execute(
            "SELECT id, strongs_number, cluster_code FROM mti_terms WHERE id=?",
            (mti_id,)).fetchone()
        if not r or r["strongs_number"] != expected_strong or r["cluster_code"] != "M39":
            print(f"  [ERR] mti={mti_id} expected {expected_strong} in M39")
            ok = False
        else:
            print(f"  ✓ mti={mti_id} {r['strongs_number']} in M39")

    # shay verses pre-state
    shay_vc = list(conn.execute(
        "SELECT id, verse_record_id, is_relevant FROM verse_context "
        "WHERE mti_term_id=2976 AND COALESCE(delete_flagged,0)=0"))
    print(f"  shay verse_context rows: {len(shay_vc)} (expected 3)")
    for r in shay_vc:
        if r["is_relevant"] != 1:
            print(f"  [WARN] shay vr={r['verse_record_id']} is_relevant={r['is_relevant']} (expected 1)")
    if len(shay_vc) != 3:
        ok = False

    # gap rows pre-state
    gap_rows = list(conn.execute("""
        SELECT cf.id, q.question_code, cf.cluster_subgroup_id
        FROM cluster_finding cf
        JOIN wa_obs_question_catalogue q ON q.obs_id=cf.obs_id
        WHERE cf.cluster_code='M39' AND cf.finding_status='gap'
        ORDER BY q.question_code, cf.cluster_subgroup_id"""))
    print(f"  M39 gap rows: {len(gap_rows)}")
    for r in gap_rows:
        print(f"    cf_id={r['id']} {r['question_code']} sg_id={r['cluster_subgroup_id']}")

    # dōron supplementary target rows pre-state (must exist for APPEND)
    for q in DORON_APPEND:
        r = conn.execute("""
            SELECT cf.id, LENGTH(cf.finding_text) AS text_len
            FROM cluster_finding cf
            WHERE cf.cluster_code='M39' AND cf.obs_id=? AND cf.cluster_subgroup_id=?
        """, (OBS[q], SG_A)).fetchone()
        if not r:
            print(f"  [ERR] M39-A {q}: no row to APPEND to")
            ok = False

    # T6.7.3 [CLUSTER] absence — INSERT will be required
    cl_t673 = conn.execute("""
        SELECT id FROM cluster_finding
        WHERE cluster_code='M39' AND obs_id=? AND cluster_subgroup_id IS NULL
    """, (OBS["T6.7.3"],)).fetchone()
    print(f"  T6.7.3 [CLUSTER] row exists: {cl_t673 is not None} (expected False → INSERT)")

    if not ok:
        print("\nPRE-FLIGHT FAILED")
        return 1

    # baseline counts
    wsrf_before = conn.execute("""
        SELECT COUNT(*) FROM wa_session_research_flags wsrf
        JOIN mti_terms mt ON mt.owning_registry_fk=wsrf.registry_id
        WHERE mt.cluster_code='M39' AND COALESCE(mt.delete_flagged,0)=0
    """).fetchone()[0]
    cf_before = conn.execute(
        "SELECT COUNT(*) FROM cluster_finding WHERE cluster_code='M39'").fetchone()[0]
    print(f"  baseline: wa_session_research_flags (M39 regs)={wsrf_before}, cluster_finding(M39)={cf_before}")

    if args.dry_run:
        print("\n[DRY-RUN] no changes. Re-run with --live.")
        return 0

    # ── LIVE APPLY ────────────────────────────────────────────────────────
    backup = take_backup()
    print(f"\nBackup: {backup}\n")

    try:
        conn.execute("BEGIN")
        cur = conn.cursor()

        # Op 1 — te.ev cluster reassign
        print("Op 1 — te.ev (mti=633) cluster reassign to M04")
        cur.execute(
            "UPDATE mti_terms SET cluster_code='M04', last_changed=? WHERE id=633",
            (ts,)
        )
        if cur.rowcount != 1:
            raise RuntimeError(f"te.ev UPDATE affected {cur.rowcount} rows (expected 1)")
        cur.execute("""
            UPDATE mti_term_subgroup
               SET delete_flagged=1, last_updated_date=?
             WHERE mti_term_id=633 AND cluster_subgroup_id=?
               AND COALESCE(delete_flagged,0)=0
        """, (ts, SG_BOUNDARY))
        if cur.rowcount != 1:
            raise RuntimeError(f"te.ev placement soft-delete affected {cur.rowcount} rows (expected 1)")
        print("  ✓ mti_terms.cluster_code=M04; mti_term_subgroup row soft-deleted")

        # Op 2 — dōron promote to M39-A
        print("Op 2 — dōron (mti=6837) promote to M39-A")
        cur.execute("""
            UPDATE mti_term_subgroup
               SET cluster_subgroup_id=?, last_updated_date=?
             WHERE mti_term_id=6837 AND cluster_subgroup_id=?
               AND COALESCE(delete_flagged,0)=0
        """, (SG_A, ts, SG_BOUNDARY))
        if cur.rowcount != 1:
            raise RuntimeError(f"dōron promote affected {cur.rowcount} rows (expected 1)")
        print("  ✓ mti_term_subgroup moved BOUNDARY→A")

        # Op 3 — shay set-aside
        print("Op 3 — shay (mti=2976) set aside (3 verses)")
        cur.execute("""
            UPDATE verse_context
               SET is_relevant=0, set_aside_reason=?
             WHERE mti_term_id=2976 AND COALESCE(delete_flagged,0)=0
        """, (SHAY_SET_ASIDE_REASON,))
        if cur.rowcount != 3:
            raise RuntimeError(f"shay set-aside affected {cur.rowcount} rows (expected 3)")
        print("  ✓ 3 verse_context rows set is_relevant=0 with set_aside_reason")

        # Op 4 — shay BOUNDARY characterisation INSERT at T1.2.1
        print("Op 4 — shay BOUNDARY characterisation at T1.2.1")
        cur.execute("""
            INSERT INTO cluster_finding
              (obs_id, cluster_code, cluster_subgroup_id, finding_status,
               finding_text, source_file, version, notes,
               delete_flagged, created_at, last_updated_date)
            VALUES (?, ?, ?, 'finding', ?, ?, 'v1-phase10',
                    ?, 0, ?, ?)
        """, (OBS["T1.2.1"], CLUSTER_CODE, SG_BOUNDARY,
              SHAY_BOUNDARY_TEXT,
              "WA-M39-consolidated-findings-v1-20260514-part1.md (phase 10 addition)",
              f"{DIRECTIVE_ID} — shay-specific BOUNDARY characterisation post-exit",
              ts, ts))
        print(f"  ✓ INSERT id={cur.lastrowid}")

        # Op 5 — T5.7.2 INSERTs
        print("Op 5 — T5.7.2 INSERTs (M39-A finding, M39-B silent)")
        cur.execute("""
            INSERT INTO cluster_finding
              (obs_id, cluster_code, cluster_subgroup_id, finding_status,
               finding_text, source_file, version, notes,
               delete_flagged, created_at, last_updated_date)
            VALUES (?, ?, ?, 'finding', ?, ?, 'v1',
                    ?, 0, ?, ?)
        """, (OBS["T5.7.2"], CLUSTER_CODE, SG_A,
              T572_A_TEXT,
              "WA-M39-consolidated-findings-v1-20260514-part4-T5-T7.md (phase 10 addition)",
              f"{DIRECTIVE_ID} — T5.7.2 coverage gap closed",
              ts, ts))
        cur.execute("""
            INSERT INTO cluster_finding
              (obs_id, cluster_code, cluster_subgroup_id, finding_status,
               finding_text, source_file, version, notes,
               delete_flagged, created_at, last_updated_date)
            VALUES (?, ?, ?, 'silent', ?, ?, 'v1',
                    ?, 0, ?, ?)
        """, (OBS["T5.7.2"], CLUSTER_CODE, SG_B,
              T572_B_TEXT,
              "WA-M39-consolidated-findings-v1-20260514-part4-T5-T7.md (phase 10 addition)",
              f"{DIRECTIVE_ID} — T5.7.2 coverage gap closed (silent for M39-B)",
              ts, ts))
        print("  ✓ 2 INSERTs (A finding + B silent)")

        # Op 6 — dōron supplementary APPEND to existing M39-A rows
        print("Op 6 — dōron supplementary APPEND to M39-A rows at 7 prompts")
        append_count = 0
        for q, dōron_text in DORON_APPEND.items():
            existing = conn.execute("""
                SELECT id, finding_text, notes FROM cluster_finding
                WHERE cluster_code='M39' AND obs_id=? AND cluster_subgroup_id=?
            """, (OBS[q], SG_A)).fetchone()
            if not existing:
                raise RuntimeError(f"Op 6: no M39-A row at {q}")
            new_text = (
                existing["finding_text"].rstrip()
                + "\n\n---\n\nDŌRON SUPPLEMENTARY (Phase 10, 2026-05-14):\n\n"
                + dōron_text
            )
            new_notes = (existing["notes"] or "") + f"; {DIRECTIVE_ID} dōron supplementary appended"
            cur.execute("""
                UPDATE cluster_finding
                   SET finding_text=?, notes=?, last_updated_date=?
                 WHERE id=?
            """, (new_text, new_notes, ts, existing["id"]))
            if cur.rowcount != 1:
                raise RuntimeError(f"Op 6 UPDATE at {q}: {cur.rowcount} rows")
            append_count += 1
        print(f"  ✓ {append_count} rows appended with dōron supplementary text")

        # Op 7 — T6.7 gap resolution
        print("Op 7 — T6.7 dimensional sharing resolution")
        # T6.7.1 [A] — UPDATE existing gap row
        cur.execute("""
            UPDATE cluster_finding
               SET finding_status='finding',
                   finding_text=?,
                   notes=COALESCE(notes,'') || '; gap resolved by dim-share analysis 2026-05-14',
                   last_updated_date=?
             WHERE cluster_code='M39' AND obs_id=? AND cluster_subgroup_id=?
               AND finding_status='gap'
        """, (T671_A_TEXT, ts, OBS["T6.7.1"], SG_A))
        if cur.rowcount != 1:
            raise RuntimeError(f"Op 7 T6.7.1 [A] UPDATE: {cur.rowcount} rows")
        # T6.7.1 [B] — UPDATE existing gap row
        cur.execute("""
            UPDATE cluster_finding
               SET finding_status='finding',
                   finding_text=?,
                   notes=COALESCE(notes,'') || '; gap resolved by dim-share analysis 2026-05-14',
                   last_updated_date=?
             WHERE cluster_code='M39' AND obs_id=? AND cluster_subgroup_id=?
               AND finding_status='gap'
        """, (T671_B_TEXT, ts, OBS["T6.7.1"], SG_B))
        if cur.rowcount != 1:
            raise RuntimeError(f"Op 7 T6.7.1 [B] UPDATE: {cur.rowcount} rows")
        # T6.7.3 [CLUSTER] — INSERT (no existing CLUSTER-scope row)
        cur.execute("""
            INSERT INTO cluster_finding
              (obs_id, cluster_code, cluster_subgroup_id, finding_status,
               finding_text, source_file, version, notes,
               delete_flagged, created_at, last_updated_date)
            VALUES (?, ?, NULL, 'cluster_synthesis', ?, ?, 'v1-phase10',
                    ?, 0, ?, ?)
        """, (OBS["T6.7.3"], CLUSTER_CODE,
              T673_CLUSTER_TEXT,
              "Phase 10 dim-share analysis 2026-05-14",
              f"{DIRECTIVE_ID} — T6.7.3 CLUSTER synthesis inserted (no prior CLUSTER row)",
              ts, ts))
        print(f"  ✓ T6.7.1 [A] UPDATE; T6.7.1 [B] UPDATE; T6.7.3 [CLUSTER] INSERT id={cur.lastrowid}")

        # Op 8 — cluster.status flip
        print("Op 8 — cluster.status → 'Analysis Completed'")
        cur.execute("""
            UPDATE cluster SET status='Analysis Completed', last_updated_date=?
             WHERE cluster_code=?
        """, (ts, CLUSTER_CODE))
        if cur.rowcount != 1:
            raise RuntimeError(f"Op 8 cluster status: {cur.rowcount} rows")
        print("  ✓ status flipped")

        # FK check + commit
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {fkv[:3]}")
        conn.commit()
        print("\nCommit OK.\n")

        # ── COMPLETION CONFIRMATION ───────────────────────────────────────
        print("COMPLETION CONFIRMATION")
        print("-" * 72)

        # Q1 — BOUNDARY exit state
        print("  Q1 — BOUNDARY exit state:")
        for mti_id in (633, 6837, 2976):
            r = conn.execute("""
                SELECT mt.id, mt.strongs_number, mt.cluster_code,
                       (SELECT cs.subgroup_code FROM cluster_subgroup cs
                          JOIN mti_term_subgroup mts ON mts.cluster_subgroup_id=cs.id
                         WHERE mts.mti_term_id=mt.id AND COALESCE(mts.delete_flagged,0)=0
                         LIMIT 1) AS sg
                FROM mti_terms mt WHERE mt.id=?
            """, (mti_id,)).fetchone()
            print(f"    mti={r['id']} {r['strongs_number']} cluster={r['cluster_code']} subgroup={r['sg']}")

        # Q2 — shay verses
        n_aside = conn.execute("""
            SELECT COUNT(*) FROM verse_context
             WHERE mti_term_id=2976 AND is_relevant=0
               AND set_aside_reason IS NOT NULL
        """).fetchone()[0]
        print(f"  Q2 — shay verses set aside: {n_aside}/3")

        # Q3 — cluster_finding by status
        print("  Q3 — cluster_finding by status:")
        for r in conn.execute("""
            SELECT finding_status, COUNT(*) AS n FROM cluster_finding
             WHERE cluster_code='M39' GROUP BY finding_status ORDER BY finding_status
        """):
            print(f"    {r['finding_status']:25s} {r['n']}")

        # Q4 — T5.7.2 rows
        print("  Q4 — T5.7.2 rows:")
        for r in conn.execute("""
            SELECT cs.subgroup_code, cf.finding_status, LENGTH(cf.finding_text) AS len
              FROM cluster_finding cf
              JOIN cluster_subgroup cs ON cs.id=cf.cluster_subgroup_id
              JOIN wa_obs_question_catalogue q ON q.obs_id=cf.obs_id
             WHERE cf.cluster_code='M39' AND q.question_code='T5.7.2'
        """):
            print(f"    {r['subgroup_code']:<14} {r['finding_status']:<10} len={r['len']}")

        # Q5 — T6.7.3 [CLUSTER] row
        r = conn.execute("""
            SELECT id, finding_status, LENGTH(finding_text) AS len
              FROM cluster_finding
             WHERE cluster_code='M39' AND obs_id=? AND cluster_subgroup_id IS NULL
        """, (OBS["T6.7.3"],)).fetchone()
        print(f"  Q5 — T6.7.3 [CLUSTER]: id={r['id']} status={r['finding_status']} len={r['len']}")

        # Q6 — M39-A term count (12 after dōron promotion)
        n_a = conn.execute("""
            SELECT COUNT(*) FROM mti_term_subgroup mts
              JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id
             WHERE cs.cluster_code='M39' AND cs.subgroup_code='M39-A'
               AND COALESCE(mts.delete_flagged,0)=0
        """).fetchone()[0]
        print(f"  Q6 — M39-A term count: {n_a} (expected 12)")

        # Q7 — cluster status
        r = conn.execute("SELECT status FROM cluster WHERE cluster_code='M39'").fetchone()
        print(f"  Q7 — cluster.status: {r['status']!r}")

        # Q8 — gap rows remaining
        n_gap = conn.execute(
            "SELECT COUNT(*) FROM cluster_finding "
            "WHERE cluster_code='M39' AND finding_status='gap'").fetchone()[0]
        print(f"  Q8 — remaining gap rows in M39: {n_gap}")

        # Q9 — wa_session_research_flags unchanged
        wsrf_after = conn.execute("""
            SELECT COUNT(*) FROM wa_session_research_flags wsrf
            JOIN mti_terms mt ON mt.owning_registry_fk=wsrf.registry_id
            WHERE mt.cluster_code='M39' AND COALESCE(mt.delete_flagged,0)=0
        """).fetchone()[0]
        # Note: this query's count drops by te.ev's registry flags after Op 1 (te.ev moved to M04).
        # Use a per-registry comparison instead: the actual flag table is untouched, just the join changes.
        wsrf_total = conn.execute("SELECT COUNT(*) FROM wa_session_research_flags").fetchone()[0]
        print(f"  Q9 — wa_session_research_flags rows total: {wsrf_total} (table untouched)")
        print(f"        M39-cluster-join count: before={wsrf_before} after={wsrf_after} "
              f"(may differ — te.ev moved registries to M04)")

    except Exception as e:
        conn.rollback()
        print(f"\nROLLED BACK: {e}")
        return 1

    conn.close()
    print(f"\n[LIVE] {DIRECTIVE_ID} applied successfully.")
    print("\nM39 cluster closure complete. Status: 'Analysis Completed'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
