"""_tmp_build_cluster_status_report.py

Build a per-cluster Session B progression report — the run-through tracking
mechanism. For each C-segment (C01..C22), list every registry, its current
session_b_status, verse_context_status, dim_review_status, plus key Session B
counts (synthesis findings, v2 Q&A coverage, open SD pointers).

Output: Workflow/Programme/Program_reports/wa-cluster-status-{date}.md
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("Workflow", "Programme", "Program_reports")


def now_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def status_marker(reg_status: str | None) -> str:
    if not reg_status:
        return "—"
    if reg_status == "Analysis Complete":
        return "✅"
    if reg_status == "Pre-Analysis Complete":
        return "🟦"
    if reg_status == "Ready for Analysis":
        return "🟨"
    if reg_status == "Verse Context Reset":
        return "🟧"
    if reg_status == "In Progress":
        return "🟪"
    if reg_status == "Session B Complete":
        return "✅"
    return "·"


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Pull every registry with its key status fields
    rows = conn.execute(
        """
        SELECT no, id, word, cluster_assignment, sb_classification,
               phase1_status, verse_context_status, session_b_status,
               dim_review_status, dim_review_version,
               phase1_term_count, phase1_verse_count
        FROM word_registry
        ORDER BY cluster_assignment, no
        """
    ).fetchall()

    # Per-registry session B counts (computed)
    by_reg: dict[int, dict] = {}
    for r in rows:
        no = r["no"]
        reg_id = r["id"]
        n_synth = conn.execute(
            "SELECT COUNT(*) FROM wa_session_b_findings "
            "WHERE registry_id=? AND finding_type LIKE 'SYNTHESIS_%' AND delete_flag=0",
            (no,),
        ).fetchone()[0]
        n_v18 = conn.execute(
            "SELECT COUNT(*) FROM wa_session_b_findings "
            "WHERE registry_id=? AND session_b_instruction LIKE '%v1_8%' AND delete_flag=0",
            (no,),
        ).fetchone()[0]
        n_v2qa = conn.execute(
            """SELECT COUNT(DISTINCT l.question_id) FROM wa_finding_catalogue_links l
               JOIN wa_session_b_findings f ON f.id=l.finding_id
               JOIN wa_obs_question_catalogue q ON q.obs_id=l.question_id
               WHERE f.registry_id=? AND q.catalogue_version='v2-2026-04-29'
               AND (l.delete_flagged=0 OR l.delete_flagged IS NULL)""",
            (no,),
        ).fetchone()[0]
        n_sd = conn.execute(
            """SELECT COUNT(*) FROM wa_session_research_flags
               WHERE registry_id=? AND flag_code='SD_POINTER'
               AND (resolved=0 OR resolved IS NULL)""",
            (reg_id,),
        ).fetchone()[0]
        # Stage 2c-eligible? Need: VC complete + Dim Review complete + Stage 2b ≥ 189 prompts
        # Approximation: status sound for analysis + has v2 Q&A + has groups
        by_reg[no] = {
            "n_synth": n_synth,
            "n_v18": n_v18,
            "n_v2qa": n_v2qa,
            "n_sd": n_sd,
            "row": r,
        }

    # Group by cluster
    by_cluster: dict[str, list] = {}
    for r in rows:
        cl = r["cluster_assignment"] or "(unassigned)"
        by_cluster.setdefault(cl, []).append(r)

    P: list[str] = []
    P.append(f"# Registry Status Report — Cluster View\n")
    P.append(f"**Generated:** {now_iso()} from `database/bible_research.db`")
    P.append(f"**Total registries:** {len(rows)}")
    P.append(f"**Clusters:** {len([c for c in by_cluster if c != '(unassigned)'])}\n")

    P.append("**Status legend:** ✅ Analysis Complete · 🟦 Pre-Analysis Complete · 🟨 Ready for Analysis · 🟧 Verse Context Reset · 🟪 In Progress · — NULL/unknown\n")

    # Programme-wide rollups
    n_complete = sum(1 for r in rows if r["session_b_status"] == "Analysis Complete")
    n_pre = sum(1 for r in rows if r["session_b_status"] == "Pre-Analysis Complete")
    n_ready = sum(1 for r in rows if r["session_b_status"] == "Ready for Analysis")
    n_reset = sum(1 for r in rows if r["session_b_status"] == "Verse Context Reset")
    n_in_progress = sum(1 for r in rows if r["session_b_status"] == "In Progress")
    n_null = sum(1 for r in rows if r["session_b_status"] is None)
    n_other = len(rows) - n_complete - n_pre - n_ready - n_reset - n_in_progress - n_null

    P.append("## Programme-wide rollup\n")
    P.append("| `session_b_status` | Count | %  |")
    P.append("| --- | ---: | ---: |")
    P.append(f"| ✅ Analysis Complete | {n_complete} | {100*n_complete/len(rows):.1f}% |")
    P.append(f"| 🟦 Pre-Analysis Complete | {n_pre} | {100*n_pre/len(rows):.1f}% |")
    P.append(f"| 🟨 Ready for Analysis | {n_ready} | {100*n_ready/len(rows):.1f}% |")
    P.append(f"| 🟧 Verse Context Reset | {n_reset} | {100*n_reset/len(rows):.1f}% |")
    P.append(f"| 🟪 In Progress | {n_in_progress} | {100*n_in_progress/len(rows):.1f}% |")
    if n_other:
        P.append(f"| Other | {n_other} | {100*n_other/len(rows):.1f}% |")
    if n_null:
        P.append(f"| (no status) | {n_null} | {100*n_null/len(rows):.1f}% |")
    P.append("")

    # v1.8-captured words (those with synthesis findings)
    v18_words = [r for r in rows if by_reg[r["no"]]["n_synth"] >= 28]
    P.append(f"\n**v1.8 fully captured (28 synthesis findings each):** {len(v18_words)} words")
    if v18_words:
        labels = ", ".join(f"R{r['no']:03d} {r['word']}" for r in v18_words)
        P.append(f"  · {labels}\n")

    # Cluster summary
    P.append("\n## Cluster summary — sequencing prioritisation\n")
    P.append("Clusters ranked by progress on Session B Analysis Complete. Use this to decide which cluster to run next.\n")
    P.append("| Cluster | Total | ✅ AC | 🟦 PreAC | 🟨 Ready | 🟧 Reset | 🟪 InProg | — | Top words to run |")
    P.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |")

    # Sort clusters by registry count desc; unassigned last
    sorted_clusters = sorted(
        by_cluster.keys(),
        key=lambda c: (c == "(unassigned)", -len(by_cluster[c]), c),
    )
    for cl in sorted_clusters:
        regs = by_cluster[cl]
        ac = sum(1 for r in regs if r["session_b_status"] == "Analysis Complete")
        pre = sum(1 for r in regs if r["session_b_status"] == "Pre-Analysis Complete")
        rdy = sum(1 for r in regs if r["session_b_status"] == "Ready for Analysis")
        rst = sum(1 for r in regs if r["session_b_status"] == "Verse Context Reset")
        ipg = sum(1 for r in regs if r["session_b_status"] == "In Progress")
        nul = sum(1 for r in regs if r["session_b_status"] is None)
        # Suggest next words (Pre-Analysis Complete first, then Ready, then Reset)
        next_words: list[str] = []
        for status_priority in ("Pre-Analysis Complete", "Ready for Analysis",
                                "Verse Context Reset", "In Progress"):
            for r in regs:
                if r["session_b_status"] == status_priority and len(next_words) < 3:
                    next_words.append(f"R{r['no']:03d} {r['word']}")
        next_str = "; ".join(next_words) if next_words else "(all complete or unspecified)"
        P.append(
            f"| {cl} | {len(regs)} | {ac} | {pre} | {rdy} | {rst} | {ipg} | {nul} | {next_str} |"
        )
    P.append("")

    # Per-cluster detail
    P.append("\n## Per-cluster detail\n")
    for cl in sorted_clusters:
        regs = by_cluster[cl]
        n_total = len(regs)
        n_ac = sum(1 for r in regs if r["session_b_status"] == "Analysis Complete")
        progress_pct = (100 * n_ac / n_total) if n_total else 0
        P.append(f"\n### {cl} — {n_total} registries · {n_ac} ✅ Analysis Complete ({progress_pct:.0f}%)\n")
        P.append("| | Reg | Word | session_b_status | VC | DimRev | v18 findings | synth | v2 Q&A | open SD |")
        P.append("| :-: | ---: | --- | --- | :-: | :-: | ---: | ---: | ---: | ---: |")
        for r in regs:
            no = r["no"]
            d = by_reg[no]
            vc = "✓" if r["verse_context_status"] == "Complete" else (r["verse_context_status"] or "—")
            dr = "✓" if r["dim_review_status"] == "Complete" else (r["dim_review_status"] or "—")
            n_synth = d["n_synth"]
            synth_marker = f"{n_synth}" + (" ✓" if n_synth >= 28 else "")
            v18 = d["n_v18"] or "—"
            v2qa = d["n_v2qa"] or "—"
            sd = d["n_sd"]
            P.append(
                f"| {status_marker(r['session_b_status'])} | R{no:03d} | {r['word']} | "
                f"{r['session_b_status'] or '—'} | {vc} | {dr} | {v18} | "
                f"{synth_marker} | {v2qa} | {sd} |"
            )

    # Words ready to run next (across all clusters)
    P.append("\n\n## Programme run-queue — words ready for Session B v1.8\n")
    P.append("Words that have completed Stage 1 (Pre-Analysis Complete or Ready for Analysis) and are ready to feed AI for the v1.8 analysis output. Sorted by cluster, then by registry no.\n")

    ready_words = [
        r for r in rows
        if r["session_b_status"] in ("Pre-Analysis Complete", "Ready for Analysis")
    ]
    if ready_words:
        ready_by_cluster: dict[str, list] = {}
        for r in ready_words:
            cl = r["cluster_assignment"] or "(unassigned)"
            ready_by_cluster.setdefault(cl, []).append(r)
        P.append(f"**Total ready: {len(ready_words)}** across {len(ready_by_cluster)} cluster(s).\n")
        P.append("| Cluster | Reg | Word | VC status | DimRev status | Verse count |")
        P.append("| --- | ---: | --- | :-: | :-: | ---: |")
        for cl in sorted(ready_by_cluster.keys()):
            for r in sorted(ready_by_cluster[cl], key=lambda x: x["no"]):
                vc = "✓" if r["verse_context_status"] == "Complete" else (r["verse_context_status"] or "—")
                dr = "✓" if r["dim_review_status"] == "Complete" else (r["dim_review_status"] or "—")
                P.append(
                    f"| {cl} | R{r['no']:03d} | {r['word']} | {vc} | {dr} | "
                    f"{r['phase1_verse_count'] or '—'} |"
                )
    else:
        P.append("_No words currently in Pre-Analysis Complete or Ready for Analysis state._")

    # Words still needing earlier-stage work
    P.append("\n\n## Words not yet ready for Session B\n")
    not_ready = [
        r for r in rows
        if r["session_b_status"] not in ("Analysis Complete", "Pre-Analysis Complete",
                                          "Ready for Analysis", "Session B Complete")
    ]
    nr_by_status: dict[str, list] = {}
    for r in not_ready:
        nr_by_status.setdefault(r["session_b_status"] or "(NULL)", []).append(r)
    if nr_by_status:
        for status, regs in sorted(nr_by_status.items()):
            P.append(f"\n### `session_b_status = {status}` — {len(regs)} registries\n")
            for r in sorted(regs, key=lambda x: (x["cluster_assignment"] or "ZZ", x["no"])):
                cl = r["cluster_assignment"] or "(unassigned)"
                P.append(f"- {cl} · R{r['no']:03d} {r['word']}")
    else:
        P.append("_All registries are at Pre-Analysis Complete or beyond._")

    P.append("\n---\n")
    P.append(f"*Source: SQLite `database/bible_research.db` (schema v3.17.0). Companion JSON: `wa-registry-overview-{now_compact()}.json`. Generated by `scripts/_tmp_build_cluster_status_report.py`.*")

    out_path = os.path.join(OUT_DIR, f"wa-cluster-status-{now_compact()}.md")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(P))
    print(f"Wrote {out_path} ({sum(len(p) for p in P):,} chars / {len(P)} lines)")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
