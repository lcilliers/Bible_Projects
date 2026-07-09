"""Generate a durable preservation archive of inherited VCGs before dissolution.

For each inherited VCG (id < new_vcg_min_id, still active), capture:
  - group_code, context_description, notes
  - Term linkages (mti_term_id, strongs, translit)
  - Pre-Phase-7 member verses: vc_id, reference, term, current analysis_note
  - Where members went post-Phase-7 (current group_id → new VCG code)
  - Pre-Phase-7 anchor verses (from backup DB)

Output: a readable markdown archive of every inherited VCG's full analytical content.
This is the human-readable counterpart to the DB row (which stays soft-deleted but
queryable). The archive captures meanings inline so future analytical work can refer
back to what each inherited VCG actually held.

Inputs:
  --m-cluster {code}
  --new-vcg-min-id N
  --pre-routing-snapshot PATH      JSON snapshot for member resolution
  --backup-db PATH (optional)      Backup DB for pre-Phase-7 anchor state recovery

Output:
  Sessions/Session_Clusters/{code}/WA-{code}-inherited-vcg-archive-v1-{date}.md
"""
from __future__ import annotations
import argparse, json, sqlite3, sys
from collections import defaultdict, Counter
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"


def fetch_inherited_vcgs(conn, cluster_code: str, new_min_id: int) -> list[dict]:
    """Return inherited VCG rows (id < new_min_id, active, linked to cluster's terms)."""
    rows = conn.execute("""
        SELECT DISTINCT vcg.id, vcg.group_code, vcg.context_description, vcg.notes,
               vcg.delete_flagged
        FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code=? AND vcg.id < ? AND COALESCE(vcg.delete_flagged,0)=0
        ORDER BY vcg.id
    """, (cluster_code, new_min_id)).fetchall()
    return [dict(r) for r in rows]


def fetch_vcg_term_links(conn, vcg_id: int) -> list[dict]:
    rows = conn.execute("""
        SELECT vt.mti_term_id, mt.strongs_number, mt.transliteration, mt.gloss, mt.language,
               vt.placement_note
        FROM vcg_term vt
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE vt.vcg_id=? AND COALESCE(vt.delete_flagged,0)=0
        ORDER BY mt.strongs_number
    """, (vcg_id,)).fetchall()
    return [dict(r) for r in rows]


def fetch_vc_details(conn, vc_ids: list[int]) -> dict[int, dict]:
    if not vc_ids:
        return {}
    placeholders = ",".join("?" * len(vc_ids))
    rows = conn.execute(f"""
        SELECT vc.id AS vc_id, vc.mti_term_id, vc.is_relevant, vc.is_anchor,
               vc.delete_flagged, vc.group_id, vc.cluster_subgroup_id, vc.analysis_note,
               vr.reference, vr.book_id, vr.chapter, vr.verse_num,
               mt.strongs_number, mt.transliteration, mt.gloss,
               cs.subgroup_code, vcg.group_code AS current_vcg_code
        FROM verse_context vc
        LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        LEFT JOIN mti_terms mt ON mt.id = vc.mti_term_id
        LEFT JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id
        WHERE vc.id IN ({placeholders})
    """, vc_ids).fetchall()
    return {r["vc_id"]: dict(r) for r in rows}


def fetch_pre_phase7_anchors(backup_db: Path, vc_ids: list[int]) -> set[int]:
    """Return set of vc_ids that had is_anchor=1 in the backup DB (pre-Phase-7)."""
    if not vc_ids or not backup_db.exists():
        return set()
    conn = sqlite3.connect(backup_db)
    conn.row_factory = sqlite3.Row
    placeholders = ",".join("?" * len(vc_ids))
    rows = conn.execute(f"""
        SELECT id FROM verse_context
        WHERE id IN ({placeholders}) AND is_anchor=1 AND COALESCE(delete_flagged,0)=0
    """, vc_ids).fetchall()
    conn.close()
    return {r["id"] for r in rows}


def build_archive(conn, cluster_code: str, new_min_id: int, snapshot: dict,
                   backup_db: Path | None) -> str:
    cluster = conn.execute("SELECT * FROM cluster WHERE cluster_code=?", (cluster_code,)).fetchone()

    inherited = fetch_inherited_vcgs(conn, cluster_code, new_min_id)
    snap = {int(k): v for k, v in snapshot.get("vc_to_old_group", {}).items()}
    old_members: dict[int, list[int]] = defaultdict(list)
    for vc_id, old_gid in snap.items():
        if old_gid is None:
            continue
        old_members[old_gid].append(vc_id)

    # Pre-Phase-7 anchors per VCG (from backup, if available)
    all_member_vc_ids = [vc for vcs in old_members.values() for vc in vcs]
    pre_anchors = fetch_pre_phase7_anchors(backup_db, all_member_vc_ids) if backup_db else set()

    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines: list[str] = []
    lines.append(f"# {cluster_code} {cluster['description']} — Inherited VCG preservation archive")
    lines.append("")
    lines.append(f"**Generated:** {now_iso}  ")
    lines.append(f"**Cluster:** `{cluster_code}` · status={cluster['status']}  ")
    lines.append(f"**Purpose:** durable human-readable record of every inherited VCG's full analytical content **before** Phase 8 soft-delete. Captures description, term linkages, member verses with their Phase 2 meanings, pre-Phase-7 anchor designations, and where each member is now routed under the Phase 7 structure.")
    lines.append("")
    lines.append("**Why this exists:** Phase 8 soft-deletes the 68 inherited VCG rows (delete_flagged=1). The rows remain queryable in the DB but go out of view for normal cluster operations. This archive is the **researcher-readable counterpart** preserving the analytical content as a flat document — so the inherited framings stay legible long after the new structure is in operation.")
    lines.append("")
    lines.append(f"**Boundary:** inherited VCGs have `id < {new_min_id}`; new VCGs from Phase 7 have `id ≥ {new_min_id}`.")
    lines.append("")
    if backup_db:
        lines.append(f"**Backup source for pre-Phase-7 anchor state:** `{backup_db.name}`")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Summary table
    lines.append("## Summary")
    lines.append("")
    lines.append("| # | group_code | Member verses (snapshot) | Pre-anchor count | Terms | Description (excerpt) |")
    lines.append("|---:|---|---:|---:|---:|---|")
    for i, vcg in enumerate(inherited, 1):
        members = old_members.get(vcg["id"], [])
        anchors = [vc for vc in members if vc in pre_anchors]
        terms = fetch_vcg_term_links(conn, vcg["id"])
        desc = (vcg["context_description"] or "").replace("\n", " ")[:80]
        lines.append(f"| {i} | `{vcg['group_code']}` (id={vcg['id']}) | {len(members)} | {len(anchors)} | {len(terms)} | {desc} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Per-VCG detail
    lines.append("## Per-inherited-VCG detail")
    lines.append("")

    for i, vcg in enumerate(inherited, 1):
        members = sorted(old_members.get(vcg["id"], []))
        terms = fetch_vcg_term_links(conn, vcg["id"])
        vc_details = fetch_vc_details(conn, members)

        lines.append(f"### {i}. `{vcg['group_code']}` (id={vcg['id']})")
        lines.append("")
        lines.append(f"**Description:** {(vcg['context_description'] or '').strip()}")
        lines.append("")
        if vcg.get("notes"):
            lines.append(f"**DB notes:** {vcg['notes'].strip()[:300]}")
            lines.append("")

        lines.append(f"**Term linkages (vcg_term):** {len(terms)}")
        if terms:
            lines.append("")
            lines.append("| mti_term_id | Strong's | Translit | Gloss | Language | placement_note |")
            lines.append("|---:|---|---|---|---|---|")
            for t in terms:
                pn = (t.get("placement_note") or "").replace("|","\\|")[:80]
                lines.append(f"| {t['mti_term_id']} | {t['strongs_number']} | {t['transliteration']} | {t.get('gloss','')} | {t.get('language','')} | {pn} |")
            lines.append("")

        lines.append(f"**Pre-Phase-7 member verses:** {len(members)}")
        if members:
            n_anchors = sum(1 for vc in members if vc in pre_anchors)
            lines.append(f"**Pre-Phase-7 anchors among these members:** {n_anchors}")
            lines.append("")
            lines.append("| vc_id | Ref | ⚓ | Term | Phase 2 meaning | Current new VCG |")
            lines.append("|---:|---|:---:|---|---|---|")
            for vc_id in members:
                d = vc_details.get(vc_id)
                if not d:
                    lines.append(f"| {vc_id} | _(vc row not retrievable)_ | | | | |")
                    continue
                anch = "⚓" if vc_id in pre_anchors else ""
                ref = d.get("reference") or "(no ref)"
                term = f"{d.get('strongs_number','')} {d.get('transliteration','')}"
                meaning = (d.get("analysis_note") or "")
                meaning = meaning.replace("|", "\\|").replace("\n", " ").strip()
                if len(meaning) > 280:
                    meaning = meaning[:277] + "…"
                cur_vcg = d.get("current_vcg_code") or "_(unrouted)_"
                # State flags
                state_bits = []
                if d.get("is_relevant") == 0: state_bits.append("set-aside")
                if d.get("delete_flagged") == 1: state_bits.append("soft-deleted")
                state_str = f" ({', '.join(state_bits)})" if state_bits else ""
                lines.append(f"| {vc_id} | {ref} | {anch} | {term} | {meaning} | `{cur_vcg}`{state_str} |")
            lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("*End of preservation archive.*")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True)
    ap.add_argument("--new-vcg-min-id", type=int, required=True)
    ap.add_argument("--pre-routing-snapshot", required=True)
    ap.add_argument("--backup-db", default=None,
                    help="Optional path to pre-Phase-7 backup DB for anchor state recovery")
    args = ap.parse_args()

    snap = json.loads(Path(args.pre_routing_snapshot).read_text(encoding="utf-8"))
    backup_path = Path(args.backup_db) if args.backup_db else None
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    try:
        rpt = build_archive(conn, args.m_cluster, args.new_vcg_min_id, snap, backup_path)
        out_dir = REPO / "Sessions" / "Session_Clusters" / args.m_cluster
        out_dir.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
        out_path = out_dir / f"WA-{args.m_cluster}-inherited-vcg-archive-v1-{date_str}.md"
        out_path.write_text(rpt, encoding="utf-8")
        print(f"Wrote: {out_path.relative_to(REPO)}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
