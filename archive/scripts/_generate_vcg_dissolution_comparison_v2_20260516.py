"""Generate the VCG dissolution comparison report (Phase 8 input — researcher review).

v2 (2026-05-16) — refinements vs v1:

  - Treats *set-aside* (is_relevant=0) and *soft-deleted* (delete_flagged=1) vc rows
    as VALID end-states for old members rather than tagging them UNROUTED.
  - Detects MERGED (a new VCG receives members from ≥2 distinct old VCGs).
  - Refined disposition algebra:
      KEEP-EQUIVALENT  = all active routed members land in a single new VCG that
                         receives members ONLY from this old VCG.
      KEEP-EQUIVALENT-OF-MERGE = all active routed members land in a single new
                         VCG that ALSO receives members from other old VCGs.
      SPLIT            = active routed members land in 2+ new VCGs.
      OBSOLETE         = no active routed members; all old members are set-aside
                         or soft-deleted.
      UNROUTED         = at least one old member is still active (is_relevant=1,
                         delete_flagged=0) AND has group_id IS NULL.

  - Reports MERGED groupings explicitly in a separate summary table.

Inputs:
  --m-cluster {code}
  --new-vcg-min-id N        smallest verse_context_group.id of the Phase 7 directive's
                            INSERTed rows. VCGs with id < N are inherited; id >= N are new.
  --pre-routing-snapshot PATH  JSON file with {vc_id: old_group_id} from a pre-Phase-7
                            state (typically reconstructed from the pre-apply backup DB).

Snapshot format:
  {
    "captured_at": "...",
    "cluster_code": "M01",
    "vc_to_old_group": { "<vc_id>": <old_group_id_or_null>, ... }
  }
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
    """Return {vcg_id: {id, group_code, context_description, delete_flagged}} for ALL
    VCGs linked (via vcg_term) to terms in the cluster, regardless of soft-delete."""
    out: dict[int, dict] = {}
    for r in conn.execute("""
        SELECT DISTINCT vcg.id, vcg.group_code, vcg.context_description, vcg.delete_flagged, vcg.notes
        FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code=?
    """, (cluster_code,)):
        out[r["id"]] = dict(r)
    return out


def fetch_vc_state(conn, cluster_code: str) -> dict[int, dict]:
    """Return {vc_id: {state, group_id, reference, strongs, transliteration, ...}} for
    EVERY vc row in the cluster, regardless of is_relevant or delete_flagged.
    state ∈ {ACTIVE_ROUTED, ACTIVE_UNROUTED, SET_ASIDE, SOFT_DELETED}."""
    out: dict[int, dict] = {}
    for r in conn.execute("""
        SELECT vc.id AS vc_id, vc.mti_term_id, vc.group_id, vc.is_relevant,
               vc.delete_flagged, vc.set_aside_reason,
               vr.book_id, vr.chapter, vr.verse_num, vr.reference,
               mt.strongs_number, mt.transliteration
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=?
          AND mt.status IN ('extracted','extracted_thin') AND COALESCE(mt.delete_flagged,0)=0
    """, (cluster_code,)):
        d = dict(r)
        if d["delete_flagged"]:
            d["state"] = "SOFT_DELETED"
        elif d["is_relevant"] == 0:
            d["state"] = "SET_ASIDE"
        elif d["group_id"] is None:
            d["state"] = "ACTIVE_UNROUTED"
        else:
            d["state"] = "ACTIVE_ROUTED"
        out[d["vc_id"]] = d
    return out


def build_report(conn, cluster_code: str, new_vcg_min_id: int,
                  snapshot: dict) -> str:
    cluster = conn.execute(
        "SELECT * FROM cluster WHERE cluster_code=?", (cluster_code,)
    ).fetchone()
    if not cluster:
        raise RuntimeError(f"cluster {cluster_code} not found")

    all_vcgs = fetch_vcgs_for_cluster(conn, cluster_code)
    # Inherited = id < boundary, not already soft-deleted
    inherited_ids = sorted([vid for vid in all_vcgs
                             if vid < new_vcg_min_id and not all_vcgs[vid]["delete_flagged"]])
    new_ids = sorted([vid for vid in all_vcgs
                       if vid >= new_vcg_min_id and not all_vcgs[vid]["delete_flagged"]])

    vc_state = fetch_vc_state(conn, cluster_code)

    # Snapshot: {old_vcg_id: [vc_ids]}
    snapshot_routing = {int(k): v for k, v in snapshot.get("vc_to_old_group", {}).items()}
    old_members_by_vcg: dict[int, list[int]] = defaultdict(list)
    for vc_id, old_gid in snapshot_routing.items():
        if old_gid is None:
            continue
        old_members_by_vcg[old_gid].append(vc_id)

    # Compute, per inherited VCG, where its members landed (per state)
    per_vcg_analysis: list[dict] = []
    for vid in inherited_ids:
        members = old_members_by_vcg.get(vid, [])
        dist: dict[str, Counter] = {
            "ACTIVE_ROUTED": Counter(),  # key = new_group_id
            "ACTIVE_UNROUTED": Counter(),  # key = "UNROUTED" placeholder
            "SET_ASIDE": Counter(),
            "SOFT_DELETED": Counter(),
            "MISSING": Counter(),  # vc_id not found in current DB (shouldn't happen)
        }
        for vc in members:
            r = vc_state.get(vc)
            if r is None:
                dist["MISSING"][vc] += 1
            elif r["state"] == "ACTIVE_ROUTED":
                dist["ACTIVE_ROUTED"][r["group_id"]] += 1
            elif r["state"] == "ACTIVE_UNROUTED":
                dist["ACTIVE_UNROUTED"]["UNROUTED"] += 1
            elif r["state"] == "SET_ASIDE":
                dist["SET_ASIDE"]["SET_ASIDE"] += 1
            elif r["state"] == "SOFT_DELETED":
                dist["SOFT_DELETED"]["SOFT_DELETED"] += 1
        per_vcg_analysis.append({
            "old_vcg": all_vcgs[vid],
            "old_members": members,
            "dist": dist,
        })

    # Detect MERGED: a new VCG that receives ACTIVE_ROUTED members from ≥2 distinct old VCGs
    new_vcg_sources: dict[int, set[int]] = defaultdict(set)
    for entry in per_vcg_analysis:
        for new_gid in entry["dist"]["ACTIVE_ROUTED"].keys():
            new_vcg_sources[new_gid].add(entry["old_vcg"]["id"])
    merged_new_vcgs = {nv: srcs for nv, srcs in new_vcg_sources.items() if len(srcs) >= 2}

    # Assign disposition to each inherited VCG
    dispositions: Counter = Counter()
    for entry in per_vcg_analysis:
        routed = entry["dist"]["ACTIVE_ROUTED"]
        unrouted = sum(entry["dist"]["ACTIVE_UNROUTED"].values())
        if unrouted > 0:
            disp = "UNROUTED"
        elif len(routed) == 0:
            disp = "OBSOLETE"  # all members are set-aside or soft-deleted
        elif len(routed) == 1:
            target = next(iter(routed.keys()))
            if target in merged_new_vcgs:
                disp = "KEEP-EQUIVALENT-OF-MERGE"
            else:
                disp = "KEEP-EQUIVALENT"
        else:
            disp = "SPLIT"
        entry["disposition"] = disp
        dispositions[disp] += 1

    # Active unrouted across cluster (excluding set-asides/soft-deleted)
    total_active_unrouted = sum(
        1 for r in vc_state.values() if r["state"] == "ACTIVE_UNROUTED"
    )
    total_active_routed = sum(
        1 for r in vc_state.values() if r["state"] == "ACTIVE_ROUTED"
    )
    total_set_aside = sum(1 for r in vc_state.values() if r["state"] == "SET_ASIDE")
    total_soft_deleted = sum(1 for r in vc_state.values() if r["state"] == "SOFT_DELETED")

    # Render
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines: list[str] = []
    lines.append(f"# {cluster_code} {cluster['description']} — VCG dissolution comparison (v2)")
    lines.append("")
    lines.append(f"**Generated:** {now_iso}  ")
    lines.append(f"**Cluster:** `{cluster_code}` ({cluster['short_name']}) · status={cluster['status']} · version={cluster['version']}  ")
    lines.append(f"**Governing instruction:** wa-sessionb-cluster-instruction-v2_0-20260515 §11 (Phase 8)  ")
    lines.append(f"**Snapshot:** {snapshot.get('captured_at','?')} — {len(snapshot_routing)} vc rows  ")
    lines.append(f"**Boundary:** new VCGs = id ≥ {new_vcg_min_id}; inherited = id < {new_vcg_min_id}  ")
    lines.append(f"**Source:** `database/bible_research.db`  ")
    lines.append("")
    lines.append("**Scope:** for each inherited (pre-Phase-7) VCG linked to this cluster's terms, "
                 "this report shows where its member verses landed under the new (Phase 7) VCG "
                 "structure. **Researcher reviews and approves dissolution before CC executes "
                 "the soft-delete directive.**")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 1. Header summary")
    lines.append("")
    lines.append(f"- Inherited VCGs: **{len(inherited_ids)}**")
    lines.append(f"- New VCGs: **{len(new_ids)}**")
    lines.append(f"- Active vc rows (routed to new VCGs): **{total_active_routed}**")
    lines.append(f"- Active vc rows (group_id IS NULL — needs Phase 7 follow-up): **{total_active_unrouted}**")
    lines.append(f"- Set-aside vc rows (is_relevant=0): **{total_set_aside}**")
    lines.append(f"- Soft-deleted vc rows (delete_flagged=1): **{total_soft_deleted}**")
    lines.append("")
    lines.append("### Disposition counts")
    lines.append("")
    lines.append("| Disposition | Count | Meaning |")
    lines.append("|---|---:|---|")
    meanings = {
        "KEEP-EQUIVALENT": "Old VCG maps 1:1 to a single new VCG that has no other source.",
        "KEEP-EQUIVALENT-OF-MERGE": "Old VCG maps to a single new VCG, but that new VCG also receives members from other old VCGs (consolidation).",
        "SPLIT": "Old VCG's members distributed across 2+ new VCGs.",
        "OBSOLETE": "Old VCG's members are all set-aside or soft-deleted; no active routed members.",
        "UNROUTED": "Old VCG has ≥1 member still active and unrouted (needs Phase 7 follow-up before dissolution).",
    }
    for disp, meaning in meanings.items():
        lines.append(f"| `{disp}` | {dispositions.get(disp, 0)} | {meaning} |")
    lines.append("")
    lines.append("**Dissolution gate:** inherited VCGs with `UNROUTED` disposition retain `delete_flagged=0` "
                 "until their remaining active members are routed. All other inherited VCGs are eligible "
                 "for soft-delete on researcher approval.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ===== MERGED summary =====
    lines.append("## 2. Consolidation map (new VCGs that absorbed multiple old VCGs)")
    lines.append("")
    if merged_new_vcgs:
        lines.append("These new VCGs each draw their members from 2+ old VCGs. "
                     "This is the most consequential change in structure — review carefully.")
        lines.append("")
        lines.append("| New VCG | # source old VCGs | Source old VCG codes (id) |")
        lines.append("|---|---:|---|")
        for new_gid in sorted(merged_new_vcgs.keys()):
            srcs = merged_new_vcgs[new_gid]
            new_vcg = all_vcgs.get(new_gid)
            new_code = new_vcg["group_code"] if new_vcg else f"(deleted id={new_gid})"
            src_strs = [f"`{all_vcgs[s]['group_code']}` (id={s})" for s in sorted(srcs)]
            lines.append(f"| `{new_code}` (id={new_gid}) | {len(srcs)} | {', '.join(src_strs)} |")
        lines.append("")
    else:
        lines.append("_(No consolidation — every new VCG draws from at most one old VCG.)_")
        lines.append("")
    lines.append("---")
    lines.append("")

    # ===== Per-inherited-VCG detail =====
    lines.append("## 3. Per-inherited-VCG detail")
    lines.append("")
    if not inherited_ids:
        lines.append("_(No inherited VCGs found.)_")
        lines.append("")

    new_vcgs = {vid: all_vcgs[vid] for vid in new_ids}

    # Sort: UNROUTED first (researcher attention), then SPLIT, then OBSOLETE, then merges, then 1:1
    disp_order = {"UNROUTED": 0, "OBSOLETE": 1, "SPLIT": 2, "KEEP-EQUIVALENT-OF-MERGE": 3, "KEEP-EQUIVALENT": 4}
    for entry in sorted(per_vcg_analysis,
                         key=lambda e: (disp_order.get(e["disposition"], 9), e["old_vcg"]["group_code"])):
        old = entry["old_vcg"]
        members = entry["old_members"]
        disp = entry["disposition"]
        dist = entry["dist"]
        lines.append(f"### Old VCG `{old['group_code']}` (id={old['id']}) — `{disp}`")
        lines.append("")
        desc = (old['context_description'] or '').replace('\n',' ')
        lines.append(f"**Old description:** {desc!r}")
        lines.append("")
        lines.append(f"**Old member verses:** {len(members)} total")
        if members:
            sample = []
            for vc in members[:5]:
                r = vc_state.get(vc)
                if r:
                    sample.append(f"{r['reference']} ({r['strongs_number']})")
            if sample:
                lines.append(f"  Sample: {', '.join(sample)}"
                             + (f", ... +{len(members)-5} more" if len(members) > 5 else ""))
        lines.append("")
        lines.append("**End-state distribution of old members:**")
        lines.append("")
        rows = []
        # ACTIVE_ROUTED
        for new_gid, n in sorted(dist["ACTIVE_ROUTED"].items(), key=lambda x: -x[1]):
            new_vcg = new_vcgs.get(new_gid) or all_vcgs.get(new_gid)
            if new_vcg:
                excerpt = (new_vcg["context_description"] or "")[:120].replace("|","\\|").replace("\n"," ")
                rows.append((n, "active → new", f"`{new_vcg['group_code']}` (id={new_gid})", excerpt))
            else:
                rows.append((n, "active → new", f"id={new_gid} (deleted?)", ""))
        # Other states
        if dist["ACTIVE_UNROUTED"].get("UNROUTED", 0):
            rows.append((dist["ACTIVE_UNROUTED"]["UNROUTED"], "active unrouted",
                         "_(vc.group_id IS NULL — Phase 7 follow-up needed)_", ""))
        if dist["SET_ASIDE"].get("SET_ASIDE", 0):
            rows.append((dist["SET_ASIDE"]["SET_ASIDE"], "set-aside (is_relevant=0)",
                         "_(no VCG; outside programme scope or other reason)_", ""))
        if dist["SOFT_DELETED"].get("SOFT_DELETED", 0):
            rows.append((dist["SOFT_DELETED"]["SOFT_DELETED"], "soft-deleted (duplicate row)",
                         "_(vc.delete_flagged=1; identical analytical content preserved on kept row)_", ""))
        if dist["MISSING"]:
            rows.append((sum(dist["MISSING"].values()), "missing", "_(vc_id absent from current DB)_", ""))

        lines.append("| Verses | End state | Target | Description excerpt |")
        lines.append("|---:|---|---|---|")
        for n, state, target, excerpt in rows:
            lines.append(f"| {n} | {state} | {target} | {excerpt} |")
        lines.append("")

        # QA side-by-side for KEEP-EQUIVALENT* dispositions
        if disp in ("KEEP-EQUIVALENT", "KEEP-EQUIVALENT-OF-MERGE") and dist["ACTIVE_ROUTED"]:
            top_new_id = next(iter(dist["ACTIVE_ROUTED"]))
            new_vcg = new_vcgs.get(top_new_id)
            if new_vcg:
                lines.append(f"**Side-by-side QA ({disp}):**")
                lines.append("")
                lines.append(f"- Old: {old['context_description']}")
                lines.append(f"- New: {new_vcg['context_description']}")
                if disp == "KEEP-EQUIVALENT-OF-MERGE":
                    other_sources = merged_new_vcgs[top_new_id] - {old['id']}
                    other_codes = [all_vcgs[s]['group_code'] for s in other_sources]
                    lines.append(f"- Co-source(s) into same new VCG: {', '.join(f'`{c}`' for c in other_codes)}")
                lines.append("")
        lines.append("---")
        lines.append("")

    # ===== Researcher approval =====
    lines.append("## 4. Researcher approval")
    lines.append("")
    eligible = [e for e in per_vcg_analysis if e["disposition"] != "UNROUTED"]
    blocked = [e for e in per_vcg_analysis if e["disposition"] == "UNROUTED"]
    lines.append(f"- Eligible for soft-delete on approval: **{len(eligible)}** inherited VCGs")
    lines.append(f"- Blocked (UNROUTED — fix Phase 7 follow-up first): **{len(blocked)}** inherited VCGs")
    lines.append("")
    lines.append("Approve dissolution by selecting one of the following:")
    lines.append("")
    lines.append("- ☐ **Approve all eligible** — soft-delete all non-UNROUTED inherited VCGs (preferred)")
    lines.append("- ☐ **Approve selectively** — list any eligible VCG ids to retain past dissolution: __________")
    lines.append("- ☐ **Pause** — researcher will review individual cases before approval")
    lines.append("")
    lines.append("On approval, CC executes `wa-cluster-{code}-dir-NNN-vcg-dissolve-v1-{date}.md` "
                 "which soft-deletes the approved inherited VCGs + their `vcg_term` links.")
    lines.append("")
    lines.append("*End of comparison report.*")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True)
    ap.add_argument("--new-vcg-min-id", type=int, required=True)
    ap.add_argument("--pre-routing-snapshot", required=True)
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
