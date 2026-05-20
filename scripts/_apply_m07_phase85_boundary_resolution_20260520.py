"""M07 Phase 8.5 — apply BOUNDARY-resolution dispositions.

Per directive WA-M07-dir-005-boundary-resolution-v1-20260520.

Researcher-confirmed dispositions (27 verses + 1 term):
- SET-ASIDE: 4 verses
- PROMOTE-TO-SUBGROUP M07-B (VCG-03): 1 verse (Lam 1:8 ni.dah)
- PROMOTE-TO-SUBGROUP M07-D: 22 verses (with VCG sub-routing)
- SET-ASIDE-TERM: H8400 te.val.lul (mti_id=4712)

Operations:
- Op A (SET-ASIDE): vc.is_relevant=0, set_aside_reason set, vc.group_id=NULL,
                   vc.cluster_subgroup_id=NULL
- Op C (PROMOTE-TO-SUBGROUP): vc.cluster_subgroup_id=target sub-group id
- Op E (VCG follow-on): vc.group_id=target VCG id
- Op F (Clear BOUNDARY flags): UPDATE wa_session_research_flags
- Op T (Term-level SET-ASIDE for H8400): mti_terms.status='excluded',
                                       delete_flagged=1
- Op B (Insert mti_term_subgroup links): if a promoted term doesn't yet
       link to the target sub-group, INSERT the link.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
DIRECTIVE = 'WA-M07-dir-005-boundary-resolution-v1-20260520'

# === Dispositions ===
# Each tuple: (vc_id, disposition, target/reason)
SET_ASIDE = [
    (49396, "Phili 3:2 katatomē",
     "Minimal inner-being content — term describes external physical practice being repudiated; no shame, disgrace, or humiliation evidenced — outside M07 inner-being scope."),
    (7266, "Isa 52:14 mish.chat",
     "Outward physical description only — extreme disfigurement causing observer-astonishment; no inner shame, disgrace, or humiliation evidenced — outside M07 inner-being scope."),
    (21170, "Psa 113:6 sha.phel",
     "sha.phel here describes God's own condescending lowering of his gaze — not a human inner-being state; no shame, disgrace, or humiliation of human persons evidenced — outside M07's human-inner-being scope."),
    (21172, "Pro 16:19 sha.phel",
     "sha.phel here names voluntary lowliness of spirit as a positive moral stance — M09 (humility/meekness) characteristic, not M07; no M09 target term available for routing — outside M07 inner-being scope. (M09 pickup note recorded.)"),
]

# PROMOTE M07-B
PROMOTE_TO_M07_B = [
    # (vc_id, target_subgroup_code, target_vcg_code, mti_id, label)
    (21682, "M07-B", "M07-B-VCG-03", 5573, "Lam 1:8 ni.dah → moral-filth-producing-shame"),
]

# PROMOTE M07-D (22 verses)
# VCG sub-routing per AI rationale: most go to VCG-03 (divine abasement of pride);
# Pro 25:7 + Jer 13:18 + Eze 21:26 go to VCG-01 (social/bodily); Eze 17:24 → VCG-03 (judicial reversal).
PROMOTE_TO_M07_D = [
    # vc_id, target_subgroup_code, target_vcg_code, mti_id, label
    (21164, "M07-D", "M07-D-VCG-03", 244, "1Sa 2:7 sha.phel — God brings low/exalts (sovereign abasement)"),
    (21165, "M07-D", "M07-D-VCG-03", 244, "2Sa 22:28 sha.phel — eyes on the haughty to bring them down"),
    (21166, "M07-D", "M07-D-VCG-03", 244, "Job 22:29 sha.phel — abasement of arrogant disposition"),
    (21167, "M07-D", "M07-D-VCG-03", 244, "Job 40:11 sha.phel — crush proud by divine force"),
    (21168, "M07-D", "M07-D-VCG-03", 244, "Psa 18:27 sha.phel — haughty eyes brought down"),
    (21169, "M07-D", "M07-D-VCG-03", 244, "Psa 75:7 sha.phel — God alone puts down/lifts up"),
    (21171, "M07-D", "M07-D-VCG-03", 244, "Psa 147:6 sha.phel — wicked cast to the ground"),
    (21173, "M07-D", "M07-D-VCG-01", 244, "Pro 25:7 sha.phel — public demotion to lower place"),
    (21162, "M07-D", "M07-D-VCG-03", 244, "Pro 29:23 sha.phel — pride brings him low (researcher promoted; M09 lowliness-honour half flagged for Phase 9 T6)"),
    (21174, "M07-D", "M07-D-VCG-03", 244, "Isa 2:9 sha.phel — God-imposed levelling"),
    (21163, "M07-D", "M07-D-VCG-03", 244, "Isa 2:11 sha.phel — haughty looks brought low"),
    (21175, "M07-D", "M07-D-VCG-03", 244, "Isa 2:12 sha.phel — Lord's day against proud"),
    (21176, "M07-D", "M07-D-VCG-03", 244, "Isa 2:17 sha.phel — haughtiness brought low"),
    (21177, "M07-D", "M07-D-VCG-03", 244, "Isa 5:15 sha.phel — eyes of haughty cast down"),
    (21178, "M07-D", "M07-D-VCG-03", 244, "Isa 10:33 sha.phel — God lopping down the lofty"),
    (21179, "M07-D", "M07-D-VCG-03", 244, "Isa 13:11 sha.phel — laying low pompous pride"),
    (21180, "M07-D", "M07-D-VCG-03", 244, "Isa 25:11 sha.phel — Moab's pomp brought low"),
    (21181, "M07-D", "M07-D-VCG-03", 244, "Isa 26:5 sha.phel — proud city cast to dust"),
    (21182, "M07-D", "M07-D-VCG-03", 244, "Isa 29:4 sha.phel — Jerusalem brought to dust"),
    (21183, "M07-D", "M07-D-VCG-01", 244, "Jer 13:18 sha.phel — king/queen take lowly seats (social demotion)"),
    (21184, "M07-D", "M07-D-VCG-03", 244, "Eze 17:24 sha.phel — high tree brought low (researcher promoted; judicial reversal)"),
    (21185, "M07-D", "M07-D-VCG-01", 244, "Eze 21:26 sha.phel — turban/crown removed (social/bodily demotion)"),
]

# Term-level SET-ASIDE
EXCLUDE_TERM_MTI = 4712  # H8400 te.val.lul

# === Apply ===
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Resolve sub-group codes to ids
sg_id = {r['subgroup_code']: r['id'] for r in cur.execute(
    "SELECT id, subgroup_code FROM cluster_subgroup WHERE cluster_code='M07' AND COALESCE(delete_flagged,0)=0"
).fetchall()}
print(f"Sub-group ids: {sg_id}")

# Resolve VCG codes to ids
vcg_id = {r['group_code']: r['id'] for r in cur.execute(
    "SELECT id, group_code FROM verse_context_group WHERE group_code LIKE 'M07%-VCG-%' AND COALESCE(delete_flagged,0)=0"
).fetchall()}
print(f"VCG codes loaded: {len(vcg_id)}")

# Pre-checks
print()
print("=== PRE-CHECKS ===")
all_vc_ids = [v[0] for v in SET_ASIDE] + [v[0] for v in PROMOTE_TO_M07_B] + [v[0] for v in PROMOTE_TO_M07_D]
assert len(all_vc_ids) == 27, f"Expected 27 vc_ids, got {len(all_vc_ids)}"
assert len(set(all_vc_ids)) == 27, "Duplicate vc_ids in disposition lists"

# Verify all currently in M07-BOUNDARY
ph = ','.join('?' * len(all_vc_ids))
in_boundary = cur.execute(
    f"""
    SELECT COUNT(*) FROM verse_context vc
    JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
    WHERE vc.id IN ({ph}) AND cs.subgroup_code='M07-BOUNDARY' AND vc.is_relevant=1
      AND COALESCE(vc.delete_flagged,0)=0
    """,
    all_vc_ids,
).fetchone()[0]
print(f"  Verses currently in M07-BOUNDARY with is_relevant=1: {in_boundary} (expected 27)")
assert in_boundary == 27

# Verify VCG codes exist
for v in PROMOTE_TO_M07_B + PROMOTE_TO_M07_D:
    if v[2] not in vcg_id:
        raise SystemExit(f"FAIL: VCG {v[2]} not in DB")
print(f"  All target VCG codes exist in DB")

# Verify te.val.lul mti
t = cur.execute("SELECT cluster_code, status, COALESCE(delete_flagged,0) FROM mti_terms WHERE id=?", (EXCLUDE_TERM_MTI,)).fetchone()
print(f"  mti_id={EXCLUDE_TERM_MTI} pre: cluster_code={t[0]!r} status={t[1]!r} del={t[2]}")
assert t[0] == 'M07' and t[2] == 0

# === Apply ===
print()
print("=== APPLYING ===")
cur.execute('BEGIN')
try:
    # Op A — SET-ASIDE (4 verses)
    for vc_id, label, reason in SET_ASIDE:
        cur.execute(
            "UPDATE verse_context SET is_relevant=0, set_aside_reason=?, "
            "cluster_subgroup_id=NULL, group_id=NULL, is_anchor=0 "
            "WHERE id=? AND COALESCE(delete_flagged,0)=0",
            (reason, vc_id),
        )
        assert cur.rowcount == 1
    print(f"  Op A: {len(SET_ASIDE)} verses set aside")

    # Op C + Op E — PROMOTE to M07-B and M07-D (23 verses) with VCG routing
    promote_links = set()  # for Op B mti_term_subgroup links
    for vc_id, target_sg, target_vcg, mti_id, label in PROMOTE_TO_M07_B + PROMOTE_TO_M07_D:
        cur.execute(
            "UPDATE verse_context SET cluster_subgroup_id=?, group_id=? "
            "WHERE id=? AND COALESCE(delete_flagged,0)=0",
            (sg_id[target_sg], vcg_id[target_vcg], vc_id),
        )
        assert cur.rowcount == 1
        promote_links.add((mti_id, sg_id[target_sg]))
    print(f"  Op C+E: 23 verses promoted to sub-groups + VCGs")

    # Op B — INSERT mti_term_subgroup links if needed
    inserted = 0
    for mti_id, sg_id_target in promote_links:
        # Does the link already exist?
        existing = cur.execute(
            "SELECT id FROM mti_term_subgroup WHERE mti_term_id=? AND cluster_subgroup_id=? "
            "AND COALESCE(delete_flagged,0)=0",
            (mti_id, sg_id_target),
        ).fetchone()
        if not existing:
            cur.execute(
                "INSERT INTO mti_term_subgroup (mti_term_id, cluster_subgroup_id, placement_note, "
                " created_at, last_updated_date) VALUES (?, ?, ?, ?, ?)",
                (mti_id, sg_id_target, '[Phase 8.5 promotion] from BOUNDARY', NOW, NOW),
            )
            inserted += 1
    print(f"  Op B: inserted {inserted} new mti_term_subgroup links")

    # Op T — Term-level SET-ASIDE for H8400 te.val.lul
    cur.execute(
        "UPDATE mti_terms SET status='excluded', exclusion_reason=?, delete_flagged=1, last_changed=? "
        "WHERE id=? AND cluster_code='M07' AND COALESCE(delete_flagged,0)=0",
        (f"Phase 8.5 SET-ASIDE-TERM: no is_relevant verses (Lev 21:20 set-aside at Phase 1 as physical bodily defect); no analytical basis for M07 retention. Per {DIRECTIVE}.",
         NOW, EXCLUDE_TERM_MTI),
    )
    assert cur.rowcount == 1
    print(f"  Op T: H8400 te.val.lul excluded (status='excluded', delete_flagged=1)")

    # Op F — Clear BOUNDARY_DECISION_PENDING flags for M07 (none expected for M07's terms;
    # the 9 stale flags on contributor registries are M01/M03 residue and not M07's responsibility)
    cur.execute(
        """
        UPDATE wa_session_research_flags
        SET resolved=1, resolved_date=?, resolved_note=?
        WHERE flag_code='BOUNDARY_DECISION_PENDING'
          AND COALESCE(resolved,0)=0
          AND registry_id IN (SELECT DISTINCT owning_registry_fk FROM mti_terms
                              WHERE cluster_code='M07' AND COALESCE(delete_flagged,0)=0)
          AND (strongs_reference LIKE 'G2699%' OR strongs_reference LIKE 'H4893%'
               OR strongs_reference LIKE 'H5206%' OR strongs_reference LIKE 'H8213%'
               OR strongs_reference LIKE 'H8400%')
        """,
        (NOW, f"Resolved at M07 Phase 8.5 via {DIRECTIVE}"),
    )
    n_flags_cleared = cur.rowcount
    print(f"  Op F: cleared {n_flags_cleared} BOUNDARY_DECISION_PENDING flags for M07's BOUNDARY terms")

    conn.commit()
    print(f"  Committed at {NOW}")
except Exception:
    conn.rollback()
    print("ROLLED BACK")
    raise

# === POST-CHECKS ===
print()
print("=== POST-CHECKS ===")

# M07-BOUNDARY active verses (should be 0)
n_boundary_active = cur.execute(
    """
    SELECT COUNT(*) FROM verse_context vc
    JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
    WHERE cs.cluster_code='M07' AND cs.subgroup_code='M07-BOUNDARY'
      AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
    """,
).fetchone()[0]
print(f"  M07-BOUNDARY active is_relevant verses: {n_boundary_active} (expected 0)")
assert n_boundary_active == 0

# M07-D verses (should be 50 + 22 = 72)
n_d = cur.execute(
    """
    SELECT COUNT(*) FROM verse_context vc
    JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
    WHERE cs.cluster_code='M07' AND cs.subgroup_code='M07-D'
      AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
    """,
).fetchone()[0]
print(f"  M07-D active is_relevant verses: {n_d} (expected 72 = 50 + 22)")

# M07-B verses (should be 110 + 1 = 111)
n_b = cur.execute(
    """
    SELECT COUNT(*) FROM verse_context vc
    JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
    WHERE cs.cluster_code='M07' AND cs.subgroup_code='M07-B'
      AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
    """,
).fetchone()[0]
print(f"  M07-B active is_relevant verses: {n_b} (expected 111 = 110 + 1)")

# Total M07 is_relevant (should be 363 - 4 = 359)
n_rel = cur.execute(
    """
    SELECT COUNT(*) FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    WHERE mt.cluster_code='M07' AND vc.is_relevant=1
      AND COALESCE(vc.delete_flagged,0)=0
    """,
).fetchone()[0]
print(f"  M07 total is_relevant: {n_rel} (expected 359 = 363 - 4 set-aside)")
assert n_rel == 359

# H8400 te.val.lul excluded
t_post = cur.execute("SELECT status, delete_flagged FROM mti_terms WHERE id=?", (EXCLUDE_TERM_MTI,)).fetchone()
print(f"  H8400 te.val.lul post: status={t_post[0]!r} delete_flagged={t_post[1]}")
assert t_post[0] == 'excluded' and t_post[1] == 1

# Cluster status (should remain Analysis - In Progress)
status = cur.execute("SELECT status FROM cluster WHERE cluster_code='M07'").fetchone()[0]
print(f"  Cluster M07 status: {status!r}")

print()
print("=== M07 PHASE 8.5 COMPLETE ===")
print(f"- 4 verses SET-ASIDE")
print(f"- 1 verse PROMOTED-TO-SUBGROUP M07-B")
print(f"- 22 verses PROMOTED-TO-SUBGROUP M07-D")
print(f"- H8400 te.val.lul excluded (term-level)")
print(f"- M07-BOUNDARY now empty (0 active is_relevant)")
print(f"- Total M07 is_relevant: 359 (Phase 9 corpus)")
print("Ready for Phase 8.7 — Characteristic mapping (v2_8 §11B).")
conn.close()
