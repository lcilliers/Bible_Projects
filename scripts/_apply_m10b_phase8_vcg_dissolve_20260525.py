"""M10b Phase 8 — Dissolve inherited VCGs.

Per v2_8 §11. Per directive wa-cluster-M10b-dir-003-phase8-vcg-dissolve-v1-20260525.md.

Identifies inherited VCGs (linked to M10b terms via vcg_term, but NOT new
M10b-{X}-VCG-{NN}) and soft-deletes them along with their vcg_term links.

Operations:
- Op A: UPDATE verse_context_group SET delete_flagged=1, notes=<audit text>
        WHERE id IN (<inherited VCG ids>) AND delete_flagged=0.
- Op B: UPDATE vcg_term SET delete_flagged=1
        WHERE vcg_id IN (<inherited VCG ids>) AND delete_flagged=0.

Pre-check (mandatory): every inherited VCG has 0 active is_relevant
verse_context rows still referencing it. (Phase 7 should have re-routed
all such rows to the new M10b-{X}-VCG-{NN} VCGs.) If any are still
referenced, Phase 8 aborts.

Comparison report (researcher-informational; not approval-required for
post-M01 clusters per §11.4):
  Sessions/Session_Clusters/M10b/wa-cluster-M10b-vcg-dissolution-comparison-v1-20260525.md
"""
from __future__ import annotations
import argparse, io, shutil, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
NOW_DATE = NOW.split("T")[0]
CLUSTER = "M10b"
DIRECTIVE_ID = "wa-cluster-M10b-dir-003-phase8-vcg-dissolve-v1-20260525"
REPORT_PATH = REPO / "Sessions" / "Session_Clusters" / CLUSTER / f"wa-cluster-{CLUSTER}-vcg-dissolution-comparison-v1-20260525.md"


def fetch_inherited_vcgs(conn) -> list[dict]:
    """Return inherited VCGs for M10b (group_code NOT LIKE 'M10b-%-VCG-%')."""
    rows = conn.execute(f"""
        SELECT vcg.id, vcg.group_code, vcg.context_description,
               COUNT(DISTINCT vt.mti_term_id) AS n_m10b_terms,
               (SELECT COUNT(*) FROM vcg_term vt2
                 WHERE vt2.vcg_id = vcg.id AND COALESCE(vt2.delete_flagged,0)=0) AS n_total_terms,
               (SELECT COUNT(*) FROM verse_context vc
                 WHERE vc.group_id = vcg.id AND vc.is_relevant=1
                   AND COALESCE(vc.delete_flagged,0)=0) AS n_active_vc
        FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id AND COALESCE(vt.delete_flagged,0)=0
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code = ?
          AND COALESCE(vcg.delete_flagged, 0) = 0
          AND vcg.group_code NOT LIKE ?
        GROUP BY vcg.id
        ORDER BY vcg.group_code
    """, (CLUSTER, f"{CLUSTER}-%-VCG-%")).fetchall()
    return [dict(r) for r in rows]


def write_comparison_report(conn, inherited: list[dict]) -> None:
    """Build a brief comparison report per §11.3.

    For M10b (post-M01 cohort) this is researcher-informational rather than
    approval-required (§11.4). The dispositions are uniform OBSOLETE because
    M10b is a post-split fresh-design cluster — every inherited VCG's verses
    have been re-routed entirely to the new M10b-{X}-VCG-{NN} structure.
    """
    cur = conn.cursor()
    n_active = conn.execute(
        "SELECT COUNT(*) FROM verse_context vc "
        "JOIN mti_terms mt ON mt.id=vc.mti_term_id "
        "WHERE mt.cluster_code=? AND vc.is_relevant=1 "
        "AND COALESCE(vc.delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchone()[0]
    lines = [
        f"# M10b Phase 8 — VCG dissolution comparison report",
        "",
        f"**Date:** {NOW_DATE}",
        f"**Cluster:** {CLUSTER} — Wickedness, Evil and Abomination (post-split 2026-05-22)",
        f"**Phase:** 8 (Dissolve inherited VCGs)",
        f"**Governing instruction:** wa-sessionb-cluster-instruction-v2_8-20260519 §11",
        "",
        "## Context",
        "",
        "M10b is a fresh post-split cluster (created 2026-05-22 from the M10 split). "
        "Its 17 terms previously lived in M10's pre-cluster-pivot Session B structure, "
        "carrying legacy per-term VCG codes (pattern: `{mti_id}-NNN`). Phase 7 routed "
        f"all {n_active} active is_relevant verses to the new `M10b-{{X}}-VCG-{{NN}}` structure (36 VCGs).",
        "",
        "The inherited VCGs identified below are linked to M10b's terms via `vcg_term` "
        "but were NOT created by the Phase 7 directive. All have 0 active is_relevant "
        "verse_context rows still referencing them — Phase 7's re-routing was complete.",
        "",
        f"## Summary",
        "",
        f"- Inherited VCGs identified: **{len(inherited)}**",
        f"- Uniform disposition: **OBSOLETE** — every inherited VCG's old framing has no analogue in the new M10b-{{X}}-VCG-{{NN}} structure (post-split fresh design)",
        f"- Active vc rows still referencing inherited VCGs: **0** (across all {len(inherited)})",
        f"- Researcher gate (§11.4): **informational** for post-M01 cohort clusters; dissolution proceeds without per-VCG approval",
        "",
        "## Inherited VCG list (table format)",
        "",
        "| VCG id | group_code | M10b term-links | Total term-links | Active vc | Disposition |",
        "|---:|---|---:|---:|---:|---|",
    ]
    for v in inherited:
        lines.append(
            f"| {v['id']} | `{v['group_code']}` | {v['n_m10b_terms']} | "
            f"{v['n_total_terms']} | {v['n_active_vc']} | OBSOLETE |"
        )
    lines.append("")
    lines.append("## Dispositions")
    lines.append("")
    lines.append("- **OBSOLETE:** all 30 inherited VCGs. The pre-cluster-pivot per-term VCG "
                 "framing (`{mti_id}-NNN`) has been entirely replaced by the post-split "
                 "characteristic-aligned `M10b-{X}-VCG-{NN}` structure. No old → new mapping "
                 "is preserved because the framing has shifted: the pre-pivot VCGs were "
                 "per-term descriptive bins (one verse-cluster per Strong's number), whereas "
                 "the new VCGs are characteristic-aligned across terms.")
    lines.append("")
    lines.append("- **KEEP-EQUIVALENT / SPLIT / MERGED:** 0 — M10b has no inherited "
                 "characteristic-aligned VCG analogues to preserve.")
    lines.append("")
    lines.append("- **UNROUTED:** 0 — all M10b's is_relevant rows are routed to new VCGs.")
    lines.append("")
    lines.append("## Action")
    lines.append("")
    lines.append("Phase 8 directive applies Ops A + B: soft-delete the 30 inherited VCGs "
                 "and their 30 `vcg_term` links (single transaction). The descriptions "
                 "remain queryable post-soft-delete for future inspection (§11.4.1).")
    lines.append("")

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main(live: bool) -> int:
    print(f"=== M10b Phase 8 apply — mode={'LIVE' if live else 'DRY-RUN'} ===")

    if live:
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        backup = REPO / "backups" / f"bible_research_backup_{ts}_M10b-phase8-vcg-dissolve.db"
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(DB, backup)
        print(f"Backup: {backup.relative_to(REPO)}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    inherited = fetch_inherited_vcgs(conn)
    print(f"Inherited VCGs found: {len(inherited)}")
    if not inherited:
        print("No inherited VCGs — Phase 8 is a no-op.")
        write_comparison_report(conn, inherited)
        conn.close()
        return 0

    # Pre-check: 0 active vc references for each
    still_referenced = [v for v in inherited if v["n_active_vc"] > 0]
    if still_referenced:
        print(f"PRE-CHECK FAIL: {len(still_referenced)} inherited VCGs still have active is_relevant vc rows.")
        for v in still_referenced[:10]:
            print(f"  {v['group_code']}: {v['n_active_vc']} active vc rows")
        return 2

    print(f"Pre-check: 0 active vc rows still reference any inherited VCG ✓")

    # Write the comparison report
    write_comparison_report(conn, inherited)
    print(f"Wrote comparison report: {REPORT_PATH.relative_to(REPO)}")

    if not live:
        print("\n[DRY-RUN — no DB writes]")
        conn.close()
        return 0

    ids = [v["id"] for v in inherited]
    qmarks = ",".join("?" * len(ids))
    audit = f"Soft-deleted by {DIRECTIVE_ID} ({NOW}) — M10b Phase 8 dissolution; OBSOLETE per §11.3 (post-split fresh-design cluster)"

    conn.execute("BEGIN")
    try:
        cur = conn.execute(
            f"UPDATE verse_context_group "
            f"SET delete_flagged=1, notes=COALESCE(notes,'') || ? "
            f"WHERE id IN ({qmarks}) AND COALESCE(delete_flagged,0)=0",
            [f"\n{audit}", *ids],
        )
        n_vcg = cur.rowcount
        print(f"Op A: soft-deleted {n_vcg} verse_context_group rows")

        cur = conn.execute(
            f"UPDATE vcg_term SET delete_flagged=1 "
            f"WHERE vcg_id IN ({qmarks}) AND COALESCE(delete_flagged,0)=0",
            ids,
        )
        n_vt = cur.rowcount
        print(f"Op B: soft-deleted {n_vt} vcg_term rows")

        # Post-checks
        residual = conn.execute(
            f"SELECT COUNT(*) FROM verse_context_group "
            f"WHERE id IN ({qmarks}) AND COALESCE(delete_flagged,0)=0",
            ids,
        ).fetchone()[0]
        if residual:
            raise RuntimeError(f"Post-check failed: {residual} inherited VCGs still active")

        # Active VCG count for the cluster = Phase 7 VCG count (36)
        active_vcg_count = conn.execute(f"""
            SELECT COUNT(DISTINCT vcg.id)
            FROM verse_context_group vcg
            JOIN vcg_term vt ON vt.vcg_id = vcg.id AND COALESCE(vt.delete_flagged,0)=0
            JOIN mti_terms mt ON mt.id = vt.mti_term_id
            WHERE mt.cluster_code = ?
              AND COALESCE(vcg.delete_flagged, 0) = 0
        """, (CLUSTER,)).fetchone()[0]
        print(f"Post-check: active VCGs for M10b = {active_vcg_count} (expected 36)")
        if active_vcg_count != 36:
            raise RuntimeError(f"Active VCG count mismatch: got {active_vcg_count}, expected 36")

        conn.commit()
        print(f"\nCOMMITTED at {NOW}")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise
    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    sys.exit(main(args.live))
