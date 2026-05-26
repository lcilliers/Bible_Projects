"""_generate_cluster_overview_v1_20260508.py — read-only.

Programme-wide cluster overview report. One row per cluster, summarising:
  - cluster_code, description, status
  - active term count, OT/NT split
  - sub-group count
  - active verse count (across all cluster terms)
  - anchor count (is_anchor=1 active rows)
  - cluster_finding count by status (synthesis / finding / silent / gap)
  - Session C inputs (10 per-chapter inputs on disk?)
  - Session C published (publication PDF on disk?)
  - last_updated_date

Output: Workflow/Clusters/wa-cluster-overview-{date}.md
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("Workflow", "Clusters")
CLUSTER_FOLDERS = Path("Sessions") / "Session_Clusters"
SESSION_C_INPUT_COUNT_EXPECTED = 10  # 7 chapters + 3 appendices, per the Session C overview spec


def session_c_status(cluster_code: str, cluster_status: str) -> tuple[str, str]:
    """Return (inputs_marker, published_marker) for a cluster.

    Inputs marker:
      ✓  — inputs/ directory exists with the expected 10 per-chapter input files
      ◐  — inputs/ exists but is incomplete (< 10 input files)
      ·  — no inputs/ directory (eligible but not yet generated)
      —  — cluster not yet 'Analysis Completed' (not eligible)

    Published marker (any one signal is sufficient — handles M15's PDF
    convention AND M03's combined-DOCX convention):
      ✓  — publication PDF at cluster root, OR combined-draft DOCX/PDF,
           OR at least 5 of 7 chapter draft files (ch1..ch7) anywhere
           in the cluster folder (`published/`, `files published/`,
           or directly under the cluster folder).
      ·  — eligible (inputs present) but no publication artefact yet
      —  — not yet eligible (no inputs / cluster not completed)
    """
    folder = CLUSTER_FOLDERS / cluster_code
    inputs_dir = folder / "inputs"

    eligible = cluster_status == "Analysis Completed"

    if inputs_dir.exists():
        # Count Session C per-chapter input files (filename pattern from the generator).
        input_files = [p for p in inputs_dir.iterdir()
                       if p.is_file() and p.name.startswith(f"wa-cluster-{cluster_code}-")
                       and "-input-" in p.name and p.suffix == ".md"]
        if len(input_files) >= SESSION_C_INPUT_COUNT_EXPECTED:
            inputs = "✓"
        elif len(input_files) > 0:
            inputs = f"◐ {len(input_files)}/{SESSION_C_INPUT_COUNT_EXPECTED}"
        else:
            inputs = "·" if eligible else "—"
    else:
        inputs = "·" if eligible else "—"

    # Publication detection — multiple signals (any one is sufficient)
    pub_signals: list[str] = []

    # Signal 1: M15-style top-level publication PDF
    if list(folder.glob(f"wa-cluster-{cluster_code}-publication-v*.pdf")):
        pub_signals.append("publication.pdf")

    # Signal 2: Combined-draft DOCX/PDF (M03's convention) — case-insensitive,
    # may be at cluster root or in a published/ subfolder
    for pattern_dir in (folder, folder / "published", folder / "files published"):
        if not pattern_dir.exists():
            continue
        for ext in ("docx", "pdf"):
            # Match e.g. WA-cluster-M03-Grief-combined-draft-v1-2026-05-17.docx
            for p in pattern_dir.glob(f"*[Cc]luster-{cluster_code}-*combined-draft*.{ext}"):
                pub_signals.append(p.name)
                break

    # Signal 3: presence of chapter drafts (ch1..ch7) somewhere in the cluster folder
    chapter_drafts_found: set[int] = set()
    candidate_dirs = [folder]
    for sub in ("published", "files published"):
        if (folder / sub).exists():
            candidate_dirs.append(folder / sub)
    for d in candidate_dirs:
        for n in range(1, 8):
            # Match e.g. WA-M15-ch3-draft-v1-20260512.md OR wa-cluster-M03-ch3-draft-v1-2026-05-17.md
            found = list(d.glob(f"*ch{n}-draft-*.md"))
            if found:
                chapter_drafts_found.add(n)
    if len(chapter_drafts_found) >= 5:
        pub_signals.append(f"chapters={sorted(chapter_drafts_found)}")

    if pub_signals:
        published = "✓"
    else:
        # If inputs are present (even partial), publication is "pending"
        if inputs.startswith("✓") or inputs.startswith("◐"):
            published = "·"
        else:
            published = "—"

    return inputs, published


def now_compact():
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def status_marker(status):
    return {
        "Analysis Completed": "✓",
        "Analysis Completed (Terms Added)": "✓+",
        "Analysis - In Progress": "▶",
        "Data - In Progress": "◐",
        "Not started": "·",
        "Parked - Methodology Review": "⏸",
    }.get(status, "?")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    clusters = list(cur.execute(
        "SELECT cluster_code, short_name, description, gloss, status, bucket, "
        "       version, last_updated_date "
        "  FROM cluster ORDER BY cluster_code"
    ))

    # Pre-compute per-cluster aggregates in single passes to avoid per-row SQL
    term_counts = {}
    for r in cur.execute(
        "SELECT cluster_code, language, COUNT(*) AS n "
        "  FROM mti_terms "
        " WHERE COALESCE(delete_flagged,0)=0 AND cluster_code IS NOT NULL "
        " GROUP BY cluster_code, language"
    ):
        term_counts.setdefault(r["cluster_code"], {})[r["language"]] = r["n"]

    sg_counts = {}
    for r in cur.execute(
        "SELECT cluster_code, COUNT(*) AS n "
        "  FROM cluster_subgroup "
        " WHERE COALESCE(delete_flagged,0)=0 "
        " GROUP BY cluster_code"
    ):
        sg_counts[r["cluster_code"]] = r["n"]

    verse_counts = {}
    anchor_counts = {}
    for r in cur.execute(
        # Post-M47: vcg ↔ term is m:n. Use vc.mti_term_id directly to
        # determine the cluster (vc has its own mti_term_id, not derived
        # from the vcg).
        "SELECT mt.cluster_code, "
        "       COUNT(DISTINCT vc.id) AS n_vc, "
        "       SUM(CASE WHEN vc.is_anchor=1 THEN 1 ELSE 0 END) AS n_anchor "
        "  FROM verse_context vc "
        "  JOIN mti_terms mt ON mt.id=vc.mti_term_id "
        " WHERE COALESCE(vc.delete_flagged,0)=0 "
        "   AND COALESCE(mt.delete_flagged,0)=0 "
        "   AND mt.cluster_code IS NOT NULL "
        " GROUP BY mt.cluster_code"
    ):
        verse_counts[r["cluster_code"]] = r["n_vc"] or 0
        anchor_counts[r["cluster_code"]] = r["n_anchor"] or 0

    finding_counts = {}
    for r in cur.execute(
        "SELECT cluster_code, finding_status, COUNT(*) AS n "
        "  FROM cluster_finding "
        " WHERE COALESCE(delete_flagged,0)=0 "
        " GROUP BY cluster_code, finding_status"
    ):
        finding_counts.setdefault(r["cluster_code"], {})[r["finding_status"]] = r["n"]

    # Post-closure-activity detection: clusters whose mti_terms have
    # last_changed > cluster.last_updated_date — terms moved in/out after closure
    # without the status string being updated. Catches the M05-precedent case.
    post_closure_changes = {}  # cluster_code -> {'n_terms': N, 'latest': iso_date}
    for r in cur.execute(
        """
        SELECT c.cluster_code, COUNT(DISTINCT mt.id) AS n_terms, MAX(mt.last_changed) AS latest
        FROM cluster c
        JOIN mti_terms mt ON mt.cluster_code = c.cluster_code
        WHERE c.status LIKE 'Analysis Completed%'
          AND c.last_updated_date IS NOT NULL
          AND mt.last_changed IS NOT NULL
          AND mt.last_changed > c.last_updated_date
          AND COALESCE(mt.delete_flagged, 0) = 0
        GROUP BY c.cluster_code
        """
    ):
        post_closure_changes[r["cluster_code"]] = {
            "n_terms": r["n_terms"],
            "latest": r["latest"],
        }

    # Build report
    today = now_compact()
    out_path = Path(OUT_DIR) / f"wa-cluster-overview-{today}.md"
    Path(OUT_DIR).mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append(f"# Cluster Overview — programme-wide snapshot")
    lines.append("")
    lines.append(f"_Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}_  ")
    lines.append(f"_Source: `database/bible_research.db`_")
    lines.append("")

    # Status roll-up
    by_status = {}
    for c in clusters:
        by_status[c["status"]] = by_status.get(c["status"], 0) + 1
    lines.append("## Status roll-up")
    lines.append("")
    lines.append("| Status | Count |")
    lines.append("|---|---:|")
    for s in ("Analysis Completed", "Analysis - In Progress", "Parked - Methodology Review", "Not started"):
        if s in by_status:
            lines.append(f"| {status_marker(s)} {s} | {by_status[s]} |")
    other = {k: v for k, v in by_status.items()
             if k not in ("Analysis Completed", "Analysis - In Progress", "Parked - Methodology Review", "Not started")}
    for k, v in sorted(other.items()):
        lines.append(f"| {k} | {v} |")
    lines.append(f"| **Total clusters** | **{len(clusters)}** |")
    lines.append("")

    # Programme totals
    total_terms = sum(sum(d.values()) for d in term_counts.values())
    total_verses = sum(verse_counts.values())
    total_anchors = sum(anchor_counts.values())
    total_findings = sum(sum(d.values()) for d in finding_counts.values())
    lines.append("## Programme totals")
    lines.append("")
    lines.append(f"- Active terms (cluster-assigned): **{total_terms:,}**")
    lines.append(f"- Active verses (in cluster groups): **{total_verses:,}**")
    lines.append(f"- Anchor verses set: **{total_anchors:,}**")
    lines.append(f"- `cluster_finding` rows (active): **{total_findings:,}**")
    lines.append("")

    # Parked-clusters callout
    parked = [c for c in clusters if c["status"] == "Parked - Methodology Review"]
    if parked:
        lines.append("## ⏸ Parked clusters (methodology review)")
        lines.append("")
        lines.append("These clusters were started but parked pending researcher review of a methodological question. Phase work is paused; the cluster's DB content (terms, verses, Pass A meanings, keywords) is preserved. See each cluster folder for the park-notice document with the reason for parking and the question to resolve.")
        lines.append("")
        lines.append("| Cluster | Short | Description | Park notice |")
        lines.append("|---|---|---|---|")
        for c in parked:
            code = c["cluster_code"]
            notice = f"Sessions/Session_Clusters/{code}/wa-cluster-{code}-park-notice-v1-*.md"
            lines.append(f"| `{code}` | {c['short_name'] or ''} | {c['description'] or ''} | `{notice}` |")
        lines.append("")

    # Post-closure-activity callout (table-level, before per-cluster)
    silent_drift = {k: v for k, v in post_closure_changes.items()
                    if not ("Terms Added" in (next((c["status"] for c in clusters if c["cluster_code"] == k), "")))}
    if silent_drift:
        lines.append("## ⚠ Post-closure activity detected (status string out of sync)")
        lines.append("")
        lines.append("These clusters have `mti_terms.last_changed > cluster.last_updated_date` but the status string does not carry the `(Terms Added)` suffix. The status should be amended to reflect the post-closure changes.")
        lines.append("")
        lines.append("| Cluster | Current status | Terms changed post-closure | Latest change |")
        lines.append("|---|---|---:|---|")
        for code in sorted(silent_drift):
            current = next((c["status"] for c in clusters if c["cluster_code"] == code), "?")
            info = silent_drift[code]
            lines.append(f"| `{code}` | {current} | {info['n_terms']} | {(info['latest'] or '')[:10]} |")
        lines.append("")

    # Per-cluster table
    lines.append("## Per-cluster detail")
    lines.append("")
    lines.append(
        "| | Code | Short | Description | Status | Terms (OT+NT) | Sub-grps | Verses | Anchors | Findings (s/f/g/syn) | SC inputs | SC published | Updated |"
    )
    lines.append(
        "|---|---|---|---|---|---:|---:|---:|---:|---|:-:|:-:|---|"
    )
    sc_inputs_total = 0
    sc_published_total = 0
    for c in clusters:
        code = c["cluster_code"]
        tc = term_counts.get(code, {})
        ot = tc.get("Hebrew", 0)
        nt = tc.get("Greek", 0)
        terms_total = ot + nt
        terms_str = f"{terms_total} ({ot}+{nt})" if terms_total else "—"
        sg = sg_counts.get(code, 0)
        v = verse_counts.get(code, 0)
        a = anchor_counts.get(code, 0)
        fc = finding_counts.get(code, {})
        if fc:
            f_str = (
                f"{fc.get('silent',0)}/{fc.get('finding',0)}/"
                f"{fc.get('gap',0)}/{fc.get('cluster_synthesis',0)}"
            )
            f_total = sum(fc.values())
            f_cell = f"{f_total} ({f_str})"
        else:
            f_cell = "—"
        sc_in, sc_pub = session_c_status(code, c["status"])
        if sc_in.startswith("✓"):
            sc_inputs_total += 1
        if sc_pub == "✓":
            sc_published_total += 1
        updated = (c["last_updated_date"] or "")[:10]
        lines.append(
            f"| {status_marker(c['status'])} "
            f"| **{code}** "
            f"| {c['short_name'] or ''} "
            f"| {c['description'] or ''} "
            f"| {c['status']} "
            f"| {terms_str} "
            f"| {sg} "
            f"| {v} "
            f"| {a} "
            f"| {f_cell} "
            f"| {sc_in} "
            f"| {sc_pub} "
            f"| {updated} |"
        )
    lines.append("")
    lines.append(
        f"_Session C totals: **{sc_inputs_total}** clusters with full inputs on file · "
        f"**{sc_published_total}** clusters published._"
    )
    lines.append("")

    # Per-cluster gloss listing (full term-gloss text for each cluster)
    lines.append("## Cluster glosses (full term-gloss lists)")
    lines.append("")
    lines.append(
        "The full `cluster.gloss` field for each cluster — the complete list of "
        "primary terms (with parenthetical transliterations) covered by the cluster. "
        "Intended as parseable input for downstream processes."
    )
    lines.append("")
    for c in clusters:
        code = c["cluster_code"]
        short = c["short_name"] or ""
        desc = c["description"] or ""
        gloss = (c["gloss"] or "").strip()
        header_tail = f" — {desc}" if desc else ""
        header_short = f" ({short})" if short else ""
        lines.append(f"### {code}{header_tail}{header_short}")
        lines.append("")
        if gloss:
            lines.append(gloss)
        else:
            lines.append("_(no gloss recorded)_")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Footer key
    lines.append("## Notation")
    lines.append("")
    lines.append("- **Status markers:** ✓ completed · ▶ in progress · ⏸ parked (methodology review) · · not started")
    lines.append("- **Terms (OT+NT):** active mti_terms split by language (Hebrew + Greek)")
    lines.append("- **Verses:** active `verse_context` rows for terms in this cluster")
    lines.append("- **Anchors:** `verse_context.is_anchor=1` rows in cluster groups")
    lines.append("- **Findings (s/f/g/syn):** `silent` / `finding` / `gap` / `cluster_synthesis` row counts; total in parens")
    lines.append(
        f"- **SC inputs:** Session C per-chapter input files at "
        f"`Sessions/Session_Clusters/{{CODE}}/inputs/` "
        f"(✓ = all {SESSION_C_INPUT_COUNT_EXPECTED} present · ◐ = partial · · = eligible but not generated · — = not yet eligible)"
    )
    lines.append(
        "- **SC published:** any of (a) publication PDF at cluster root, "
        "(b) `*combined-draft*.{docx,pdf}` (in cluster root or `published/`), "
        "or (c) ≥5 of 7 chapter draft files (`*ch1-draft*` … `*ch7-draft*.md`). "
        "(✓ = present · · = eligible but not published · — = not yet eligible)"
    )
    lines.append(
        "- **Post-closure activity callout (⚠):** detects clusters whose `mti_terms.last_changed > cluster.last_updated_date` "
        "but whose status string lacks the `(Terms Added)` suffix. Catches silent post-closure drift (M05 precedent, "
        "where M07 transferred 2 terms in 2026-05-19 but M05's status was not updated)."
    )
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out_path}")
    print(f"Clusters: {len(clusters)}")
    print(f"  Completed:    {by_status.get('Analysis Completed', 0)}")
    print(f"  In progress:  {by_status.get('Analysis - In Progress', 0)}")
    print(f"  Not started:  {by_status.get('Not started', 0)}")
    print(f"Session C:")
    print(f"  Full inputs on file: {sc_inputs_total}")
    print(f"  Published (PDF):     {sc_published_total}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
