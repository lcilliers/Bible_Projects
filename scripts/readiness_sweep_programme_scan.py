"""Programme-wide readiness sweep scan.

Runs phases R.A through R.H (read-only) across all carry_forward=1 registries.
Produces an aggregated assessment with cluster/phase/path breakdowns and a
prioritised action list.

Usage:
    python scripts/readiness_sweep_programme_scan.py

Output:
    outputs/reports/wa-global-readinesssweep-programme-scan-20260419.md
    outputs/reports/wa-global-readinesssweep-programme-scan-raw-20260419.json
"""
from __future__ import annotations

import json
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, ".")
sys.stdout.reconfigure(encoding="utf-8")

# Reuse phase implementations from the pilot
from scripts.readiness_sweep_pilot import (
    SweepState,
    phase_ra_registry,
    phase_rb_terms,
    phase_rc_verses,
    phase_rd_groups,
    phase_re_dimensions,
    phase_rf_flags,
    phase_rg_supporting,
    phase_rh_prose,
)

DB = "database/bible_research.db"
DATE_STR = datetime.now(timezone.utc).strftime("%Y%m%d")
OUT_MD = Path(f"outputs/reports/wa-global-readinesssweep-programme-scan-{DATE_STR}.md")
OUT_JSON = Path(f"outputs/reports/wa-global-readinesssweep-programme-scan-raw-{DATE_STR}.json")


def main():
    conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row

    registries = conn.execute("""
        SELECT * FROM word_registry
        WHERE carry_forward = 1
        ORDER BY no
    """).fetchall()

    print(f"Scanning {len(registries)} registries...")

    per_registry = []
    phase_aggregate = Counter()
    path_aggregate = Counter()
    cluster_aggregate = defaultdict(lambda: {"registries": 0, "findings": 0,
                                              "path_1": 0, "path_2": 0, "path_3": 0,
                                              "path_4": 0, "path_5": 0})
    error_registries = []

    for i, wr in enumerate(registries, 1):
        if i % 20 == 0:
            print(f"  [{i}/{len(registries)}] r{wr['no']} {wr['word']}...")

        try:
            file_ids = [r[0] for r in conn.execute(
                "SELECT id FROM wa_file_index WHERE word_registry_fk = ?",
                (wr["id"],)
            ).fetchall()]

            state = SweepState(wr["no"])
            state.summary["registry_id"] = wr["id"]
            state.summary["file_id_count"] = len(file_ids)

            phase_ra_registry(conn, state, wr)
            phase_rb_terms(conn, state, wr["id"], file_ids)
            phase_rc_verses(conn, state, file_ids)
            phase_rd_groups(conn, state, wr["id"])
            phase_re_dimensions(conn, state, wr["id"])
            phase_rf_flags(conn, state, wr["id"])
            phase_rg_supporting(conn, state, file_ids, wr["id"])
            phase_rh_prose(conn, state, wr["id"])

        except Exception as e:
            error_registries.append((wr["no"], wr["word"], str(e)))
            continue

        # Aggregate
        by_path = state.by_path()
        by_phase = state.by_phase()

        p_counts = {p: len(by_path.get(p, [])) for p in range(1, 6)}
        total = sum(p_counts.values())

        per_registry.append({
            "no": wr["no"],
            "word": wr["word"],
            "cluster": wr["cluster_assignment"],
            "session_b_status": wr["session_b_status"],
            "verse_context_status": wr["verse_context_status"],
            "dim_review_status": wr["dim_review_status"],
            "owner_terms": state.summary.get("owner_terms", 0),
            "xref_terms": state.summary.get("xref_terms", 0),
            "active_verses": state.summary.get("active_verse_records", 0),
            "active_groups": state.summary.get("active_groups", 0),
            "active_dimensions": state.summary.get("active_dimension_rows", 0),
            "null_dimension": state.summary.get("null_dimension", 0),
            "automated_confidence": state.summary.get("automated_confidence", 0),
            "path_1": p_counts[1],
            "path_2": p_counts[2],
            "path_3": p_counts[3],
            "path_4": p_counts[4],
            "path_5": p_counts[5],
            "total_findings": total,
            "findings": [
                {"phase": f.phase, "path": f.path, "target": f.target,
                 "issue": f.issue, "action": f.action}
                for f in state.findings
            ],
        })

        # Aggregates
        for phase, items in by_phase.items():
            phase_aggregate[phase] += len(items)
        for p, count in p_counts.items():
            path_aggregate[p] += count

        cluster = wr["cluster_assignment"] or "(none)"
        ca = cluster_aggregate[cluster]
        ca["registries"] += 1
        ca["findings"] += total
        for p in range(1, 6):
            ca[f"path_{p}"] += p_counts[p]

    conn.close()

    print(f"\nScan complete. Processed {len(per_registry)} registries; {len(error_registries)} errors.")

    # Write raw JSON
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSON.open("w", encoding="utf-8") as f:
        json.dump({
            "scan_date": datetime.now(timezone.utc).isoformat(),
            "schema_version": "3.10.0",
            "instruction": "wa-global-readiness-sweep-instruction-v1_0-20260419.md",
            "registries_scanned": len(per_registry),
            "errors": error_registries,
            "phase_aggregate": dict(phase_aggregate),
            "path_aggregate": dict(path_aggregate),
            "cluster_aggregate": {k: v for k, v in cluster_aggregate.items()},
            "per_registry": per_registry,
        }, f, indent=2, ensure_ascii=False)
    print(f"Wrote {OUT_JSON} ({OUT_JSON.stat().st_size:,} bytes)")

    # Write assessment markdown
    L = []
    E = L.append

    E("# Readiness Sweep — Programme-Wide Assessment")
    E("")
    E("| Field | Value |")
    E("| --- | --- |")
    E(f"| Scan date | {datetime.now(timezone.utc).isoformat()} |")
    E("| Schema version | 3.10.0 (post-DBR) |")
    E("| Instruction | wa-global-readiness-sweep-instruction-v1_0-20260419.md |")
    E("| Mode | Read-only (phases R.A–R.H via pilot) |")
    E(f"| Registries scanned | {len(per_registry)} |")
    if error_registries:
        E(f"| Errors | {len(error_registries)} |")
    E("")
    E("---")
    E("")

    # Programme summary
    E("## 1. Programme Summary")
    E("")
    total_findings = sum(path_aggregate.values())
    E(f"**Total findings across programme:** {total_findings:,}")
    E("")
    E("### By path")
    E("")
    E("| Path | Count | Share | Description |")
    E("| --- | --- | --- | --- |")
    path_desc = {
        1: "Mechanical patch (CC can fix automatically)",
        2: "Sub-process directive (re-extract / VC / DimReview)",
        3: "Deferred to per-word Stage 1",
        4: "RESEARCHER_DECISION",
        5: "Outstanding task — beyond CC skill",
    }
    for p in sorted(path_aggregate.keys()):
        n = path_aggregate[p]
        pct = (n / total_findings * 100) if total_findings else 0
        E(f"| {p} | {n:,} | {pct:.1f}% | {path_desc.get(p, '?')} |")
    E("")

    # By phase
    E("### By phase")
    E("")
    E("| Phase | Finding count | Focus |")
    E("| --- | --- | --- |")
    phase_focus = {
        "R.A": "Registry state (status, cluster, counts)",
        "R.B": "Term inventory (OWNER/XREF/deleted; three-number diagnostic)",
        "R.C": "Verse record quality (NULL text, span_strong_match)",
        "R.D": "Verse context groups (group_code, anchor count, dominant_subject)",
        "R.E": "Dimension assignments (NULL/AUTOMATED confidence, vocab drift)",
        "R.F": "Flags/findings/catalogue (situational)",
        "R.G": "Supporting term data (meaning parse, root, related)",
        "R.H": "Prose coverage (Session A/B/C/D sections)",
    }
    for ph in sorted(phase_aggregate.keys()):
        E(f"| {ph} | {phase_aggregate[ph]:,} | {phase_focus.get(ph, '?')} |")
    E("")

    E("### Distribution of registries by findings count")
    E("")
    bins = {"clean (≤2)": 0, "light (3–10)": 0, "moderate (11–30)": 0,
            "heavy (31–70)": 0, "critical (>70)": 0}
    for r in per_registry:
        n = r["total_findings"]
        if n <= 2:
            bins["clean (≤2)"] += 1
        elif n <= 10:
            bins["light (3–10)"] += 1
        elif n <= 30:
            bins["moderate (11–30)"] += 1
        elif n <= 70:
            bins["heavy (31–70)"] += 1
        else:
            bins["critical (>70)"] += 1
    E("| Bin | Registries |")
    E("| --- | --- |")
    for k, v in bins.items():
        E(f"| {k} | {v} |")
    E("")
    E("---")
    E("")

    # Cluster breakdown
    E("## 2. Cluster Breakdown")
    E("")
    E("Registries grouped by `cluster_assignment`; sorted by total findings per cluster.")
    E("")
    E("| Cluster | Registries | Findings | Path 1 | Path 2 | Path 3 | Path 4 | Path 5 | Avg per registry |")
    E("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    sorted_clusters = sorted(cluster_aggregate.items(),
                              key=lambda kv: kv[1]["findings"], reverse=True)
    for cluster, agg in sorted_clusters:
        avg = agg["findings"] / agg["registries"] if agg["registries"] else 0
        E(f"| {cluster} | {agg['registries']} | {agg['findings']} | "
          f"{agg['path_1']} | {agg['path_2']} | {agg['path_3']} | "
          f"{agg['path_4']} | {agg['path_5']} | {avg:.1f} |")
    E("")
    E("---")
    E("")

    # Top 20 highest-findings registries
    E("## 3. Top 20 Registries by Findings (triage priority)")
    E("")
    E("High-findings registries likely benefit most from pre-processing before the full sweep runs. Typical remediations:")
    E("")
    E("- Many Path 2 (span filter / zero extraction) → re-extract + audit_word re-run")
    E("- Many Path 2 (NULL dimension / AUTOMATED confidence) → run Dimension Review on cluster")
    E("- Many Path 4 on group-level NULL dominant_subject → run Verse Context anchor pass")
    E("")
    top = sorted(per_registry, key=lambda r: r["total_findings"], reverse=True)[:20]
    E("| no | word | cluster | VC | DimRev | SB status | OWN terms | Findings | P1 | P2 | P3 | P4 | P5 | Notable |")
    E("| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |")
    for r in top:
        notable = []
        if r.get("null_dimension", 0) > 0:
            notable.append(f"NULL dim:{r['null_dimension']}")
        if r.get("automated_confidence", 0) > 0:
            notable.append(f"AUTO conf:{r['automated_confidence']}")
        notable_s = "; ".join(notable) if notable else ""
        vc = r["verse_context_status"] or "—"
        dr = r["dim_review_status"] or "—"
        sb = r["session_b_status"] or "—"
        E(f"| {r['no']} | {r['word']} | {r['cluster']} | {vc} | {dr} | {sb} | "
          f"{r['owner_terms']} | {r['total_findings']} | "
          f"{r['path_1']} | {r['path_2']} | {r['path_3']} | {r['path_4']} | {r['path_5']} | {notable_s} |")
    E("")
    E("---")
    E("")

    # Pre-process recommendations
    E("## 4. Pre-Process Recommendations")
    E("")

    # Registries with span filter failures (Path 2 items in R.B)
    E("### 4.1 — Registries with probable span filter failure / zero extraction")
    E("")
    E("Candidates for `audit_word` re-run (blocked on OT-DBR-001 until audit_word.py rewrite lands).")
    E("")
    span_fail_registries = []
    for r in per_registry:
        span_items = [f for f in r["findings"]
                      if f["phase"] == "R.B" and f["path"] == 2
                      and ("span filter" in f["issue"] or "zero extraction" in f["issue"])]
        if span_items:
            span_fail_registries.append((r, len(span_items)))
    span_fail_registries.sort(key=lambda x: x[1], reverse=True)
    E(f"**{len(span_fail_registries)} registries affected**, involving "
      f"{sum(n for _, n in span_fail_registries):,} term-level Path 2 items total.")
    E("")
    if span_fail_registries:
        E("| no | word | cluster | affected terms |")
        E("| ---: | --- | --- | ---: |")
        for r, n in span_fail_registries[:25]:
            E(f"| {r['no']} | {r['word']} | {r['cluster']} | {n} |")
        if len(span_fail_registries) > 25:
            E(f"| … {len(span_fail_registries)-25} more | | | |")
    E("")

    # Registries with NULL dimension or AUTOMATED confidence (dim review needed)
    E("### 4.2 — Registries needing Dimension Review")
    E("")
    E("NULL dimension OR non-reviewed confidence on multiple groups → benefit from Dimension Review pre-process (cluster-wide approach).")
    E("")
    dimreview_needed = []
    for r in per_registry:
        null_dim = r.get("null_dimension", 0)
        auto_conf = r.get("automated_confidence", 0)
        if null_dim > 0 or auto_conf > 5:
            dimreview_needed.append((r, null_dim + auto_conf))
    dimreview_needed.sort(key=lambda x: x[1], reverse=True)
    E(f"**{len(dimreview_needed)} registries affected**.")
    E("")
    if dimreview_needed:
        E("| no | word | cluster | NULL dim | AUTO conf | total |")
        E("| ---: | --- | --- | ---: | ---: | ---: |")
        for r, tot in dimreview_needed[:25]:
            E(f"| {r['no']} | {r['word']} | {r['cluster']} | "
              f"{r['null_dimension']} | {r['automated_confidence']} | {tot} |")
        if len(dimreview_needed) > 25:
            E(f"| … {len(dimreview_needed)-25} more | | | | | |")
    E("")

    # Registries with verse_context_status != Complete
    E("### 4.3 — Registries needing Verse Context completion")
    E("")
    vc_incomplete = [r for r in per_registry
                     if r["verse_context_status"] != "Complete"]
    E(f"**{len(vc_incomplete)} registries** have `verse_context_status != 'Complete'`.")
    E("")
    if vc_incomplete:
        E("| no | word | cluster | VC status | SB status |")
        E("| ---: | --- | --- | --- | --- |")
        for r in vc_incomplete[:25]:
            E(f"| {r['no']} | {r['word']} | {r['cluster']} | "
              f"{r['verse_context_status'] or '—'} | {r['session_b_status'] or '—'} |")
        if len(vc_incomplete) > 25:
            E(f"| … {len(vc_incomplete)-25} more | | | | |")
    E("")

    # Registries with dim_review_status != Complete
    E("### 4.4 — Registries needing Dim Review completion (status flag)")
    E("")
    dr_incomplete = [r for r in per_registry
                     if r["dim_review_status"] != "Complete"]
    E(f"**{len(dr_incomplete)} registries** have `dim_review_status != 'Complete'`.")
    E("")
    E("Note: the dimensions extract (2026-04-19) showed 172 registries have actual dimension data; the status flag has lagged. Path 4 'hard gate' findings are predominantly this flag mismatch, not actual missing data. Bulk-status-update may be warranted if a sample confirms dimension data is present.")
    E("")

    # Clean registries (candidates to run Stage 1 immediately)
    E("### 4.5 — Clean registries (ready for Stage 1 once OT-DBR-001 lands)")
    E("")
    clean = [r for r in per_registry if r["total_findings"] <= 2]
    E(f"**{len(clean)} registries** have ≤2 findings (just word_synopsis + Session A extract gaps, both deferred).")
    E("")
    if clean:
        # Group by cluster
        by_cluster = defaultdict(list)
        for r in clean:
            by_cluster[r["cluster"] or "(none)"].append(r)
        for cluster in sorted(by_cluster.keys()):
            regs = by_cluster[cluster]
            reg_list = ", ".join(f"{r['no']} {r['word']}" for r in regs)
            E(f"- **{cluster}** ({len(regs)}): {reg_list}")
    E("")
    E("---")
    E("")

    # Aggregate recommended pre-process ordering
    E("## 5. Suggested Pre-Process Sequence")
    E("")
    E("Based on the scan, the most efficient unlock sequence is:")
    E("")
    E("1. **OT-DBR-001 rewrite (audit_word.py)** — unblocks Path 2 re-extraction directives across the programme.")
    E(f"2. **Bulk re-extraction for {len(span_fail_registries)} registries** with span filter failure / zero extraction — reclaims hundreds of analytical term-verse rows.")
    E(f"3. **Dimension Review on {len(dimreview_needed)} registries** — most via cluster-level batch (C01 legacy vocab also needs normalisation; see dimensions extract).")
    E(f"4. **Verse Context completion for {len(vc_incomplete)} registries** — some are at 'In Progress' already (e.g. suffering r214).")
    E("5. **Dim Review status flag normalisation** — bulk patch setting `dim_review_status = 'Complete'` where `wa_dimension_index` has reviewed content (status flag has lagged the data).")
    E(f"6. **Session A extract generator** — unblocks prose coverage Path 5 for all {len(per_registry)} registries.")
    E("")
    E("Completing 1–5 would likely **drop programme findings count by 60–80%** and place a sizable cohort at 'ready for Stage 1' state.")
    E("")
    E("---")
    E("")

    # Per-registry detail (condensed — just the numbers)
    E("## 6. Per-Registry Detail (full list)")
    E("")
    E("Sorted by total findings descending. Full raw data in `wa-global-readinesssweep-programme-scan-raw-{date}.json`.")
    E("")
    E("| no | word | cluster | VC | DimRev | SB status | OWN | XREF | V | G | Dim | ΣF | P1 | P2 | P3 | P4 | P5 |")
    E("| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    sorted_all = sorted(per_registry, key=lambda r: r["total_findings"], reverse=True)
    for r in sorted_all:
        vc = (r["verse_context_status"] or "—")[:8]
        dr = (r["dim_review_status"] or "—")[:8]
        sb = (r["session_b_status"] or "—")[:16]
        E(f"| {r['no']} | {r['word']} | {r['cluster']} | {vc} | {dr} | {sb} | "
          f"{r['owner_terms']} | {r['xref_terms']} | {r['active_verses']} | "
          f"{r['active_groups']} | {r['active_dimensions']} | "
          f"{r['total_findings']} | {r['path_1']} | {r['path_2']} | "
          f"{r['path_3']} | {r['path_4']} | {r['path_5']} |")
    E("")

    # Errors
    if error_registries:
        E("---")
        E("")
        E("## 7. Scan Errors")
        E("")
        E("| no | word | error |")
        E("| --- | --- | --- |")
        for no, word, err in error_registries:
            E(f"| {no} | {word} | `{err[:80]}` |")
        E("")

    E("---")
    E("")
    E("*End of programme-wide scan — 2026-04-19*")

    OUT_MD.write_text("\n".join(L), encoding="utf-8")
    print(f"Wrote {OUT_MD} ({OUT_MD.stat().st_size:,} bytes, {len(L)} lines)")


if __name__ == "__main__":
    main()
