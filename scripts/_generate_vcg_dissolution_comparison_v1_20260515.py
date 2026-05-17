"""Generate the VCG dissolution comparison report (Phase 8 input — researcher review).

Per wa-sessionb-cluster-instruction-v2_0-20260515 §11.3 — for each inherited (pre-Phase-7)
VCG, this report shows where its old member verses landed under the new (Phase 7) VCG
structure. The researcher reviews this report before approving the soft-delete of the
inherited VCGs.

Inputs required:
  --m-cluster {code}
  --new-vcg-min-id N        smallest verse_context_group.id of the Phase 7 directive's
                            INSERTed rows. VCGs with id < N are inherited; id >= N are new.
  --pre-routing-snapshot PATH JSON file produced by the Phase 7 apply script, capturing
                            {vc_id: old_group_id} for every is_relevant vc row in the
                            cluster BEFORE the Phase 7 routing UPDATE was applied.

Snapshot format (Phase 7 apply script's responsibility):
  {
    "captured_at": "2026-05-15T18:00:00Z",
    "cluster_code": "M01",
    "vc_to_old_group": {
      "<vc_id>": <old_group_id_or_null>,
      ...
    }
  }

Output:
  Sessions/Session_Clusters/{code}/WA-{code}-vcg-dissolution-comparison-v{N}-{date}.md
"""
from __future__ import annotations
import argparse, json, re, sqlite3, sys
from collections import defaultdict, Counter
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"


def next_version_for(out_dir: Path, prefix: str, date_str: str) -> str:
    pat = re.compile(rf"^{re.escape(prefix)}-v(\d+)-{date_str}\.md$")
    max_v = 0
    if out_dir.exists():
        for p in out_dir.iterdir():
            m = pat.match(p.name)
            if m:
                max_v = max(max_v, int(m.group(1)))
    return f"v{max_v + 1}"


def fetch_vcgs_for_cluster(conn, cluster_code: str) -> dict[int, dict]:
    """Return {vcg_id: {id, group_code, context_description, delete_flagged}}."""
    out: dict[int, dict] = {}
    for r in conn.execute("""
        SELECT DISTINCT vcg.id, vcg.group_code, vcg.context_description, vcg.delete_flagged
        FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vt.delete_flagged,0)=0
    """, (cluster_code,)):
        out[r["id"]] = dict(r)
    return out


def fetch_current_routing(conn, cluster_code: str) -> dict[int, dict]:
    """Return {vc_id: {vc_id, mti_term_id, group_id, reference, strongs, transliteration}}."""
    out: dict[int, dict] = {}
    for r in conn.execute("""
        SELECT vc.id AS vc_id, vc.mti_term_id, vc.group_id, vc.is_relevant,
               vr.book_id, vr.chapter, vr.verse_num, vr.reference,
               mt.strongs_number, mt.transliteration
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
          AND mt.status IN ('extracted','extracted_thin') AND COALESCE(mt.delete_flagged,0)=0
          AND vc.is_relevant=1
    """, (cluster_code,)):
        out[r["vc_id"]] = dict(r)
    return out


def classify_disposition(old_vcg_id: int, member_vc_ids: list[int],
                          new_routing: dict[int, int | None]) -> str:
    """Determine disposition tag for an inherited VCG given new routings of its members."""
    if not member_vc_ids:
        return "ORPHAN-NO-MEMBERS"
    # Where do members now route?
    targets: list[int | None] = [new_routing.get(vc, None) for vc in member_vc_ids]
    distinct_new = {t for t in targets if t is not None and t != old_vcg_id}
    still_in_old = sum(1 for t in targets if t == old_vcg_id)
    unrouted = sum(1 for t in targets if t is None)
    if unrouted > 0:
        return "UNROUTED"
    if still_in_old == len(targets):
        return "ORPHAN-NO-MEMBERS-MOVED"
    if len(distinct_new) == 1:
        return "KEEP-EQUIVALENT"
    if len(distinct_new) > 1:
        # If members of OTHER old VCGs also joined this new VCG, classify as MERGED;
        # else SPLIT.
        # For v1 of the tool, distinguish by counts; refinement deferred to v2.
        return "SPLIT"
    return "OBSOLETE"


def build_report(conn, cluster_code: str, new_vcg_min_id: int,
                  snapshot: dict) -> str:
    cluster = conn.execute(
        "SELECT * FROM cluster WHERE cluster_code=?", (cluster_code,)
    ).fetchone()
    if not cluster:
        raise RuntimeError(f"cluster {cluster_code} not found")

    all_vcgs = fetch_vcgs_for_cluster(conn, cluster_code)
    inherited_ids = sorted([vid for vid in all_vcgs if vid < new_vcg_min_id and not all_vcgs[vid]["delete_flagged"]])
    new_ids = sorted([vid for vid in all_vcgs if vid >= new_vcg_min_id and not all_vcgs[vid]["delete_flagged"]])

    # Build new_routing: {vc_id: current group_id}
    current = fetch_current_routing(conn, cluster_code)
    new_routing: dict[int, int | None] = {vc_id: r["group_id"] for vc_id, r in current.items()}

    # Build {old_vcg_id: [vc_ids that were in it pre-Phase-7]} from snapshot
    snapshot_routing = {int(k): v for k, v in snapshot.get("vc_to_old_group", {}).items()}
    old_members_by_vcg: dict[int, list[int]] = defaultdict(list)
    for vc_id, old_gid in snapshot_routing.items():
        if old_gid is None:
            continue
        old_members_by_vcg[old_gid].append(vc_id)

    # Compute disposition + new-VCG distribution per inherited VCG
    dispositions: Counter = Counter()
    per_vcg_analysis: list[dict] = []
    for vid in inherited_ids:
        members = old_members_by_vcg.get(vid, [])
        disposition = classify_disposition(vid, members, new_routing)
        # New routing distribution
        new_dist: Counter = Counter()
        for vc in members:
            new_gid = new_routing.get(vc)
            key = new_gid if new_gid is not None else "UNROUTED"
            new_dist[key] += 1
        per_vcg_analysis.append({
            "old_vcg": all_vcgs[vid],
            "old_members": members,
            "new_dist": new_dist,
            "disposition": disposition,
        })
        dispositions[disposition] += 1

    # Compute unrouted count
    total_unrouted = sum(1 for vc, g in new_routing.items() if g is None)

    # ===== Render =====
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines: list[str] = []
    lines.append(f"# {cluster_code} {cluster['description']} — VCG dissolution comparison")
    lines.append("")
    lines.append(f"**Generated:** {now_iso}  ")
    lines.append(f"**Cluster:** `{cluster_code}` ({cluster['short_name']}) · status={cluster['status']} · version={cluster['version']}  ")
    lines.append(f"**Governing instruction:** wa-sessionb-cluster-instruction-v2_0-20260515 §11 (Phase 8 — Dissolve old VCGs)  ")
    lines.append(f"**Snapshot:** captured at {snapshot.get('captured_at','?')}; {len(snapshot_routing)} vc rows  ")
    lines.append(f"**Source:** `database/bible_research.db`  ")
    lines.append("")
    lines.append("**Scope:** for each inherited (pre-Phase-7) VCG linked to this cluster's terms, this report shows where its member verses landed under the new (Phase 7) VCG structure. **Researcher reviews and approves dissolution before CC executes the soft-delete directive.**")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Header summary")
    lines.append("")
    lines.append(f"- Inherited VCGs (id < {new_vcg_min_id}): **{len(inherited_ids)}**")
    lines.append(f"- New VCGs (id ≥ {new_vcg_min_id}): **{len(new_ids)}**")
    lines.append(f"- Verses currently unrouted (vc.group_id IS NULL): **{total_unrouted}**")
    lines.append("")
    lines.append("**Disposition counts:**")
    lines.append("")
    lines.append("| Disposition | Count |")
    lines.append("|---|---:|")
    for disp in ("KEEP-EQUIVALENT","SPLIT","MERGED","OBSOLETE","UNROUTED","ORPHAN-NO-MEMBERS","ORPHAN-NO-MEMBERS-MOVED"):
        lines.append(f"| `{disp}` | {dispositions.get(disp, 0)} |")
    lines.append("")
    lines.append("**Dissolution gate:** any inherited VCG with `UNROUTED` disposition must retain `delete_flagged=0` until its remaining members are routed (Phase 7 follow-up). All other inherited VCGs are eligible for soft-delete on researcher approval.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Per-inherited-VCG detail")
    lines.append("")

    if not inherited_ids:
        lines.append("_(No inherited VCGs found — either this is a fresh cluster with no inherited structure, or the `--new-vcg-min-id` boundary excluded all VCGs.)_")
        lines.append("")

    # Group analyses by disposition for readability
    new_vcgs = {vid: all_vcgs[vid] for vid in new_ids}
    for entry in sorted(per_vcg_analysis, key=lambda e: (e["disposition"], e["old_vcg"]["group_code"])):
        old = entry["old_vcg"]
        members = entry["old_members"]
        disp = entry["disposition"]
        new_dist = entry["new_dist"]
        lines.append(f"### Old VCG `{old['group_code']}` (id={old['id']}) — `{disp}`")
        lines.append("")
        lines.append(f"**Old description:** {old['context_description']!r}")
        lines.append("")
        lines.append(f"**Old member verses:** {len(members)}")
        if members:
            sample = []
            for vc in members[:5]:
                r = current.get(vc)
                if r:
                    sample.append(f"{r['reference']} ({r['strongs_number']})")
            if sample:
                lines.append(f"  Sample: {', '.join(sample)}" + (f", ... +{len(members)-5} more" if len(members) > 5 else ""))
        lines.append("")
        lines.append("**New routing of old members:**")
        lines.append("")
        if new_dist:
            lines.append("| Target | Verses | New VCG code | New description (excerpt) |")
            lines.append("|---|---:|---|---|")
            for target, n in sorted(new_dist.items(), key=lambda x: -x[1]):
                if target == "UNROUTED":
                    lines.append(f"| _(unrouted — vc.group_id IS NULL)_ | {n} | — | — |")
                else:
                    new_vcg = new_vcgs.get(target) or all_vcgs.get(target)
                    if new_vcg:
                        excerpt = (new_vcg["context_description"] or "")[:120].replace("|","\\|").replace("\n"," ")
                        lines.append(f"| New VCG id={target} | {n} | `{new_vcg['group_code']}` | {excerpt} |")
                    else:
                        lines.append(f"| Target id={target} (deleted?) | {n} | — | — |")
        else:
            lines.append("_(no member-routing data available)_")
        lines.append("")
        # Side-by-side description text for KEEP-EQUIVALENT
        if disp == "KEEP-EQUIVALENT" and new_dist:
            top_new_id = next(iter(new_dist))
            new_vcg = new_vcgs.get(top_new_id)
            if new_vcg:
                lines.append("**Side-by-side (KEEP-EQUIVALENT QA):**")
                lines.append("")
                lines.append(f"- Old: {old['context_description']}")
                lines.append(f"- New: {new_vcg['context_description']}")
                lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## Researcher approval section")
    lines.append("")
    lines.append("Approve dissolution by marking the inherited VCGs eligible for soft-delete:")
    lines.append("")
    lines.append("- ☐ **Approve all** non-UNROUTED inherited VCGs for soft-delete")
    lines.append("- ☐ **Approve selectively** — list any VCG ids to retain past dissolution: ____________")
    lines.append("- ☐ **Pause** — researcher will review individual cases before approval")
    lines.append("")
    lines.append("On approval, CC executes `wa-cluster-{code}-dir-NNN-vcg-dissolve-v1-{date}.md` (Phase 8 dissolution directive) which soft-deletes the approved inherited VCGs + their vcg_term links.")
    lines.append("")
    lines.append("*End of comparison report.*")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True)
    ap.add_argument("--new-vcg-min-id", type=int, required=True,
                    help="Smallest verse_context_group.id of the Phase 7 directive's INSERTed rows.")
    ap.add_argument("--pre-routing-snapshot", required=True,
                    help="JSON file with pre-Phase-7 {vc_id: old_group_id} routing.")
    args = ap.parse_args()

    code = args.m_cluster.strip()
    snapshot_path = Path(args.pre_routing_snapshot)
    if not snapshot_path.exists():
        print(f"ERROR: snapshot file not found: {snapshot_path}")
        return 1
    snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    try:
        report = build_report(conn, code, args.new_vcg_min_id, snapshot)
        out_dir = REPO / "Sessions" / "Session_Clusters" / code
        out_dir.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
        version = next_version_for(out_dir, f"WA-{code}-vcg-dissolution-comparison", date_str)
        out_path = out_dir / f"WA-{code}-vcg-dissolution-comparison-{version}-{date_str}.md"
        out_path.write_text(report, encoding="utf-8")
        print(f"Wrote: {out_path.relative_to(REPO)}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
