"""M10c Phase 6 — sub-group structural apply + verse routing.

Per v2_8 §9. Per directive wa-cluster-M10c-dir-001-phase6-subgroup-assign-v1-20260526.md.

Operations (single transaction):
- Op A: INSERT 5 cluster_subgroup rows (M10c-A..E)
- Op B: INSERT mti_term_subgroup rows (primary + secondary placements)
- Op C: UPDATE verse_context.cluster_subgroup_id for all 263 active is_relevant rows
- Op D: cluster.status 'Data - In Progress' → 'Analysis - In Progress'

Source: Sessions/Session_Clusters/M10c/wa-cluster-M10c-subgroup-mapping-v1_0-20260526.json

Per-verse-range resolution: 4 terms (akathartos, ta.me verb, ta.me adj, nid.dah)
distribute verses across multiple sub-groups via verse_ranges. 4 other terms
(akatharsia, miasmos, molunō, molusmos) are term-level.

Mapping-doc gap fix (3 verses missing from any verse_ranges entry, resolved
from Pass A meaning content):
  - vc=21468 Num 5:3 (ta.me verb) → M10c-D (camp defilement, divine presence)
  - vc=21583 Hag 2:13 (ta.me adj) → M10c-A (bodily-contact death contagion)
  - vc=21706 Zec 13:1 (nid.dah) → M10c-D (corporate-prophetic cleansing)

Resolved flat mapping written for audit:
  Sessions/Session_Clusters/M10c/wa-cluster-M10c-subgroup-mapping-resolved-v1-20260526.json
"""
from __future__ import annotations
import argparse, io, json, shutil, sqlite3, sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DIRECTIVE_ID = "wa-cluster-M10c-dir-001-phase6-subgroup-assign-v1-20260526"
MAPPING_PATH = REPO / "Sessions" / "Session_Clusters" / "M10c" / "wa-cluster-M10c-subgroup-mapping-v1_0-20260526.json"
RESOLVED_PATH = REPO / "Sessions" / "Session_Clusters" / "M10c" / "wa-cluster-M10c-subgroup-mapping-resolved-v1-20260526.json"

CLUSTER = "M10c"

# 3 documented gap fixes (refs not in any AI verse_ranges)
GAP_FIXES = {
    (5581, "Num 5:3"): "M10c-D",     # ta.me verb mti=5581
    (920,  "Hag 2:13"): "M10c-A",    # ta.me adj mti=920
    (918,  "Zec 13:1"): "M10c-D",    # nid.dah mti=918
}

# Sub-group definitions: (code, label, core_description, sort_order)
SUBGROUPS = [
    ("M10c-A", "Bodily-contact defilement-state",
     "The inner-being condition of ritual uncleanness acquired through physical contact with a defiling agent "
     "(corpse, discharge, carcass, fluid). Time-bound; transmitted by touch, carrying, or proximity; resolved "
     "by washing and waiting. Inner content: awareness of contamination incurred, duty of bodily watchfulness, "
     "distress at worship exclusion, conscience responding to violation. Structural opposite: M12 purity.",
     1),
    ("M10c-B", "Categorical/classificatory unclean-state",
     "The inner-being condition of uncleanness determined by authoritative examination and verdict (priestly "
     "diagnosis of skin disease) or by inherent categorical designation (animals, objects). May be permanent, "
     "progressive, or resolved by clearance. Inner content: active moral-spiritual discernment required of "
     "those who distinguish clean from unclean; enforced communal isolation; public self-declaration of "
     "contamination; grief at worship exclusion; conscience formed by purity categories. Structural opposite: "
     "M12 purity/discernment.",
     2),
    ("M10c-C", "Moral-inner defilement-state",
     "Defilement as the inner condition of moral corruption — conscience, will, and heart corrupted by desire, "
     "habitual sin, and idolatrous attachment. Locus of defilement is the inner person itself, not external "
     "contact. Primary NT register (all Greek terms); Hebrew metaphorical extension (Isa 64:6, Hag 2:14, "
     "Job 14:4, Isa 6:5). Inner content: defiled conscience (1Cor 8:7); body and spirit defiled (2Cor 7:1); "
     "impurity as prior master of the will (Rom 6:19); heart allegiance disorder (Eph 5:5); constitutional "
     "human moral uncleanness (Job 14:4). Structural opposite: M12 purity/holiness of the inner person.",
     3),
    ("M10c-D", "Corporate/covenantal defilement",
     "Defilement extending from persons or community to land, sanctuary, and the divine name through moral "
     "defection. Includes covenantal-relational defilement (sexual betrayal, ordeal law, Nazirite violation) "
     "and the prophetic corporate register (idolatry defiling sanctuary and land; persistent unfaithfulness "
     "contaminating sacred space). Inner-being content: corporate will in defection; hearts unfaithful in "
     "covenant; memory of defilement as mechanism of repentance (Eze 20:43); community's inner corruption "
     "rendering offerings worthless (Hag 2:14). Structural opposite: M12 purity/holiness of sacred space, "
     "divine name, covenant relationship.",
     4),
    ("M10c-E", "Defilement by external spiritual agency",
     "The inner-being condition of defilement produced by an unclean spirit inhabiting, controlling, and "
     "corrupting a person from without. The unclean force dominates will, suppresses faculties, and severs "
     "communal access. Restoration is treated as wholeness (Luk 6:18). The spirits recognise divine authority "
     "and resist expulsion. Structurally distinct from bodily-mechanism and from moral self-defilement — the "
     "agency is external. Structural opposite: M12 purity/wholeness — the restored state after expulsion.",
     5),
]


def resolve_mapping(conn) -> tuple[dict[int, str], dict[int, dict[str, int]]]:
    """Return (vc_id_to_subgroup_code, per_term_per_subgroup_count)."""
    mapping = json.loads(MAPPING_PATH.read_text(encoding="utf-8"))

    rows = list(conn.execute("""
        SELECT vc.id AS vc_id, vc.mti_term_id, vr.reference
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE mt.cluster_code = ?
          AND COALESCE(mt.delete_flagged, 0) = 0
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND COALESCE(vr.delete_flagged, 0) = 0
    """, (CLUSTER,)).fetchall())

    # Build resolver
    term_default: dict[int, str] = {}
    per_verse_rules: dict[int, dict[str, str]] = {}
    for t in mapping["term_assignments"]:
        mti = t["mti_id"]
        term_default[mti] = t["primary_subgroup"]
        if t.get("assignment_type") == "per_verse_range":
            d: dict[str, str] = {}
            for rng in t.get("verse_ranges", []):
                sg = rng["subgroup"]
                for ref in rng["verses"]:
                    d[ref] = sg
            per_verse_rules[mti] = d

    vc_to_sg: dict[int, str] = {}
    per_term_per_sg: dict[int, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    gap_resolved = 0
    for r in rows:
        mti = r["mti_term_id"]
        ref = r["reference"]
        if mti in per_verse_rules:
            sg = per_verse_rules[mti].get(ref)
            if sg is None:
                # gap-fix lookup
                sg = GAP_FIXES.get((mti, ref))
                if sg is not None:
                    gap_resolved += 1
                else:
                    raise RuntimeError(f"Unassigned vc_id={r['vc_id']} mti={mti} ref={ref}")
        else:
            sg = term_default[mti]
        vc_to_sg[r["vc_id"]] = sg
        per_term_per_sg[mti][sg] += 1

    print(f"Resolved {len(vc_to_sg)} vc rows; gap-fix applied for {gap_resolved} verses")
    return vc_to_sg, per_term_per_sg


def fetch_term_info(conn, mti_ids: list[int]) -> dict[int, dict]:
    rows = conn.execute(
        f"SELECT id, strongs_number, transliteration FROM mti_terms WHERE id IN "
        f"({','.join('?'*len(mti_ids))})", mti_ids
    ).fetchall()
    return {r["id"]: {"strongs": r["strongs_number"], "translit": r["transliteration"]} for r in rows}


def main(live: bool) -> int:
    print(f"=== M10c Phase 6 apply — mode={'LIVE' if live else 'DRY-RUN'} ===")

    if live:
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        backup = REPO / "backups" / f"bible_research_backup_{ts}_M10c-phase6-subgroup-assign.db"
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(DB, backup)
        print(f"Backup: {backup.relative_to(REPO)}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    pre_cluster = conn.execute("SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)).fetchone()
    print(f"Pre cluster status: {pre_cluster['status']}")

    n_existing_sg = conn.execute(
        "SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchone()[0]
    if n_existing_sg:
        print(f"ERROR: {n_existing_sg} existing cluster_subgroup rows for {CLUSTER} — aborting.")
        return 1

    vc_to_sg, per_term_per_sg = resolve_mapping(conn)
    sg_counter = Counter(vc_to_sg.values())
    print()
    print("Per sub-group totals:")
    for sg_code, *_ in SUBGROUPS:
        print(f"  {sg_code}: {sg_counter[sg_code]} verses")

    term_info = fetch_term_info(conn, list(per_term_per_sg.keys()))
    print("\nPer-term sub-group assignment:")
    for mti in sorted(per_term_per_sg.keys(), key=lambda k: -sum(per_term_per_sg[k].values())):
        info = term_info[mti]
        sgs = ", ".join(f"{sg}={n}" for sg, n in sorted(per_term_per_sg[mti].items()))
        n_total = sum(per_term_per_sg[mti].values())
        print(f"  {info['strongs']:8s} {info['translit']:18s} (mti={mti}, V={n_total}): {sgs}")

    resolved = {
        "_meta": {
            "cluster_code": CLUSTER,
            "directive_id": DIRECTIVE_ID,
            "generated_at": NOW,
            "source_mapping": MAPPING_PATH.name,
            "total_verses": len(vc_to_sg),
            "gap_fixes_applied": [
                {"mti_term_id": mti, "reference": ref, "subgroup": sg}
                for (mti, ref), sg in GAP_FIXES.items()
            ],
        },
        "vc_to_subgroup": {str(k): v for k, v in sorted(vc_to_sg.items())},
        "per_subgroup_counts": {sg: sg_counter[sg] for sg, *_ in SUBGROUPS},
        "per_term_per_subgroup": {
            str(mti): dict(per_term_per_sg[mti]) for mti in sorted(per_term_per_sg.keys())
        },
    }
    if live:
        RESOLVED_PATH.write_text(json.dumps(resolved, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
        print(f"\nResolved mapping: {RESOLVED_PATH.relative_to(REPO)}")
    else:
        print(f"\n(Resolved mapping would be: {RESOLVED_PATH.relative_to(REPO)})")

    if not live:
        print("\n[DRY-RUN — no DB writes]")
        conn.close()
        return 0

    conn.execute("BEGIN")
    try:
        sg_id_by_code: dict[str, int] = {}
        for code, label, desc, sort_order in SUBGROUPS:
            cur = conn.execute(
                "INSERT INTO cluster_subgroup "
                "(cluster_code, subgroup_code, label, core_description, sort_order, "
                " status, version, source, delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, ?, ?, 'active', 'v1', ?, 0, ?, ?)",
                (CLUSTER, code, label, desc, sort_order, DIRECTIVE_ID, NOW, NOW),
            )
            sg_id_by_code[code] = cur.lastrowid
        print(f"\nOp A: created {len(sg_id_by_code)} cluster_subgroup rows")

        n_ms = 0
        for mti, sg_counts in per_term_per_sg.items():
            sg_sorted = sorted(sg_counts.items(), key=lambda x: -x[1])
            for i, (sg_code, n) in enumerate(sg_sorted):
                placement = f"[{'primary' if i == 0 else 'secondary'}] {n} verses"
                conn.execute(
                    "INSERT INTO mti_term_subgroup "
                    "(mti_term_id, cluster_subgroup_id, placement_note, "
                    " delete_flagged, created_at, last_updated_date) "
                    "VALUES (?, ?, ?, 0, ?, ?)",
                    (mti, sg_id_by_code[sg_code], placement, NOW, NOW),
                )
                n_ms += 1
        print(f"Op B: created {n_ms} mti_term_subgroup rows")

        n_vc = 0
        for vc_id, sg_code in vc_to_sg.items():
            cur = conn.execute(
                "UPDATE verse_context SET cluster_subgroup_id=? "
                "WHERE id=? AND COALESCE(delete_flagged,0)=0",
                (sg_id_by_code[sg_code], vc_id),
            )
            n_vc += cur.rowcount
        print(f"Op C: updated {n_vc} verse_context.cluster_subgroup_id")

        cur = conn.execute(
            "UPDATE cluster SET status='Analysis - In Progress', last_updated_date=? "
            "WHERE cluster_code=? AND status='Data - In Progress'",
            (NOW, CLUSTER),
        )
        print(f"Op D: cluster status flipped ({cur.rowcount} row updated)")

        unrouted = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE mt.cluster_code = ? AND vc.is_relevant = 1
              AND COALESCE(vc.delete_flagged, 0) = 0
              AND vc.cluster_subgroup_id IS NULL
        """, (CLUSTER,)).fetchone()[0]
        if unrouted:
            raise RuntimeError(f"Post-check failed: {unrouted} unrouted is_relevant rows")
        print(f"Post-check: 0 unrouted is_relevant rows ✓")

        new_status = conn.execute("SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)).fetchone()["status"]
        if new_status != "Analysis - In Progress":
            raise RuntimeError(f"Post-check failed: status is {new_status!r}")
        print(f"Post-check: cluster status = {new_status} ✓")

        conn.commit()
        print("\nCOMMITTED")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise
    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="Apply (default: dry-run)")
    args = ap.parse_args()
    sys.exit(main(args.live))
