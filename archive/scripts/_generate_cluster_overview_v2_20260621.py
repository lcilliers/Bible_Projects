"""_generate_cluster_overview_v2_20260621.py — read-only. Successor to _generate_cluster_overview_v1_20260508.py.

Corrects the verse metric. The v1 report's "Verses" column counted `verse_context`
rows — i.e. TERM-IN-VERSE OCCURRENCES (a verse with 3 cluster terms counted 3×) — and
never excluded set-asides, so it overstated verses badly against the reworked, set-aside
corpus (e.g. M08 showed 680 where the live in-scope corpus is 253). This version reports,
per cluster:
  - **Verses (in-scope)** — DISTINCT verses (references), active, set_aside_reason IS NULL.
    This is the count the ve_lexical extracts carry.
  - **Set-aside** — DISTINCT verses with at least one set_aside occurrence (out-of-scope).
  - **Occ** — term-in-verse occurrences (active vc rows) — what v1 mislabelled "Verses".
Everything else (status, terms, sub-groups, anchors, findings, Session C, glosses) is as v1.

Output: Workflow/Clusters/wa-cluster-overview-{date}.md
"""
from __future__ import annotations
import os, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("Workflow", "Clusters")
CLUSTER_FOLDERS = Path("Sessions") / "Session_Clusters"
SESSION_C_INPUT_COUNT_EXPECTED = 10
SC_CHAPTER_CODES = ("sc_v2_ch1", "sc_v2_ch2", "sc_v2_ch3", "sc_v2_ch4", "sc_v2_ch5", "sc_v2_ch6", "sc_v2_ch7")


def session_c_status(cluster_code, cluster_status, chapter_codes_in_db):
    folder = CLUSTER_FOLDERS / cluster_code
    inputs_dir = folder / "inputs"
    eligible = cluster_status == "Analysis Completed"
    if inputs_dir.exists():
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
    n_present = len(chapter_codes_in_db & set(SC_CHAPTER_CODES))
    if n_present == len(SC_CHAPTER_CODES):
        published = "✓"
    elif n_present > 0:
        published = f"◐ {n_present}/{len(SC_CHAPTER_CODES)}"
    else:
        published = "·" if (inputs.startswith("✓") or inputs.startswith("◐")) else "—"
    return inputs, published


def status_marker(status):
    return {"Analysis Completed": "✓", "Analysis Completed (Terms Added)": "✓+",
            "Analysis - In Progress": "▶", "Data - In Progress": "◐",
            "Not started": "·", "Parked - Methodology Review": "⏸"}.get(status, "?")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    conn = sqlite3.connect(DB_PATH); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    clusters = list(cur.execute(
        "SELECT cluster_code, short_name, description, gloss, status, bucket, version, last_updated_date FROM cluster ORDER BY cluster_code"))

    term_counts = {}
    for r in cur.execute("SELECT cluster_code, language, COUNT(*) AS n FROM mti_terms WHERE COALESCE(delete_flagged,0)=0 AND cluster_code IS NOT NULL GROUP BY cluster_code, language"):
        term_counts.setdefault(r["cluster_code"], {})[r["language"]] = r["n"]

    sg_counts = {}
    for r in cur.execute("SELECT cluster_code, COUNT(*) AS n FROM cluster_subgroup WHERE COALESCE(delete_flagged,0)=0 GROUP BY cluster_code"):
        sg_counts[r["cluster_code"]] = r["n"]

    # CORRECTED verse metrics: distinct verses (references), split in-scope vs set-aside; plus occurrences.
    inscope, setaside, occ, anchor_counts = {}, {}, {}, {}
    for r in cur.execute(
        "SELECT mt.cluster_code, "
        "  COUNT(DISTINCT CASE WHEN vc.set_aside_reason IS NULL THEN vr.reference END) AS n_in, "
        "  COUNT(DISTINCT CASE WHEN vc.set_aside_reason IS NOT NULL THEN vr.reference END) AS n_sa, "
        "  COUNT(DISTINCT vc.id) AS n_occ, "
        "  SUM(CASE WHEN vc.is_anchor=1 THEN 1 ELSE 0 END) AS n_anchor "
        "FROM verse_context vc "
        "JOIN mti_terms mt ON mt.id=vc.mti_term_id "
        "JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0 "
        "WHERE COALESCE(vc.delete_flagged,0)=0 AND COALESCE(mt.delete_flagged,0)=0 AND mt.cluster_code IS NOT NULL "
        "GROUP BY mt.cluster_code"):
        inscope[r["cluster_code"]] = r["n_in"] or 0
        setaside[r["cluster_code"]] = r["n_sa"] or 0
        occ[r["cluster_code"]] = r["n_occ"] or 0
        anchor_counts[r["cluster_code"]] = r["n_anchor"] or 0

    finding_counts = {}
    for r in cur.execute("SELECT cluster_code, finding_status, COUNT(*) AS n FROM cluster_finding WHERE COALESCE(delete_flagged,0)=0 GROUP BY cluster_code, finding_status"):
        finding_counts.setdefault(r["cluster_code"], {})[r["finding_status"]] = r["n"]

    chapter_codes_by_cluster = {}
    for r in cur.execute(
        "SELECT DISTINCT ps.cluster_code, pst.code FROM prose_section ps JOIN prose_section_type pst ON pst.id=ps.section_type_id "
        "WHERE ps.cluster_code IS NOT NULL AND COALESCE(ps.delete_flagged,0)=0 AND pst.code IN ('sc_v2_ch1','sc_v2_ch2','sc_v2_ch3','sc_v2_ch4','sc_v2_ch5','sc_v2_ch6','sc_v2_ch7')"):
        chapter_codes_by_cluster.setdefault(r["cluster_code"], set()).add(r["code"])

    post_closure_changes = {}
    for r in cur.execute(
        "SELECT c.cluster_code, COUNT(DISTINCT mt.id) AS n_terms, MAX(mt.last_changed) AS latest FROM cluster c "
        "JOIN mti_terms mt ON mt.cluster_code=c.cluster_code WHERE c.status LIKE 'Analysis Completed%' AND c.last_updated_date IS NOT NULL "
        "AND mt.last_changed IS NOT NULL AND mt.last_changed > c.last_updated_date AND COALESCE(mt.delete_flagged,0)=0 GROUP BY c.cluster_code"):
        post_closure_changes[r["cluster_code"]] = {"n_terms": r["n_terms"], "latest": r["latest"]}

    today = datetime.now(timezone.utc).strftime("%Y%m%d")
    out_path = Path(OUT_DIR) / f"wa-cluster-overview-{today}.md"
    Path(OUT_DIR).mkdir(parents=True, exist_ok=True)

    L = []
    L.append("# Cluster Overview — programme-wide snapshot")
    L.append("")
    L.append(f"_Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}_  ")
    L.append("_Source: `database/bible_research.db`_  ")
    L.append("_Generator: `scripts/_generate_cluster_overview_v2_20260621.py` (corrected verse metric)_")
    L.append("")
    L.append("> **Verse-metric correction (v2).** The prior overview's *Verses* column counted "
             "`verse_context` rows — term-in-verse **occurrences** (a verse with N cluster terms counted N times) — "
             "and did not exclude set-asides, so it overstated verses against the reworked corpus "
             "(e.g. M08 read 680 where the in-scope corpus is 253). This version reports **distinct in-scope verses** "
             "(active, not set aside — the count the ve_lexical extracts carry), with separate **Set-aside** and "
             "**Occ** (occurrences) columns. Set-asides only exist for clusters taken through the ve_lexical rework "
             "(M01–M08 to date); not-yet-reworked clusters show all verses in-scope.")
    L.append("")

    by_status = {}
    for c in clusters:
        by_status[c["status"]] = by_status.get(c["status"], 0) + 1
    L.append("## Status roll-up")
    L.append("")
    L.append("| Status | Count |")
    L.append("|---|---:|")
    for s in ("Analysis Completed", "Analysis - In Progress", "Parked - Methodology Review", "Not started"):
        if s in by_status:
            L.append(f"| {status_marker(s)} {s} | {by_status[s]} |")
    other = {k: v for k, v in by_status.items() if k not in ("Analysis Completed", "Analysis - In Progress", "Parked - Methodology Review", "Not started")}
    for k, v in sorted(other.items()):
        L.append(f"| {k} | {v} |")
    L.append(f"| **Total clusters** | **{len(clusters)}** |")
    L.append("")

    tot_terms = sum(sum(d.values()) for d in term_counts.values())
    tot_in = sum(inscope.values()); tot_sa = sum(setaside.values()); tot_occ = sum(occ.values())
    tot_anchor = sum(anchor_counts.values())
    tot_find = sum(sum(d.values()) for d in finding_counts.values())
    L.append("## Programme totals")
    L.append("")
    L.append(f"- Active terms (cluster-assigned): **{tot_terms:,}**")
    L.append(f"- **In-scope verses** (distinct, not set aside): **{tot_in:,}**")
    L.append(f"- Set-aside verses (distinct): **{tot_sa:,}**")
    L.append(f"- Term-in-verse occurrences: **{tot_occ:,}**")
    L.append(f"- Anchor verses set: **{tot_anchor:,}**")
    L.append(f"- `cluster_finding` rows (active): **{tot_find:,}**")
    L.append("")

    silent_drift = {k: v for k, v in post_closure_changes.items()
                    if not ("Terms Added" in (next((c["status"] for c in clusters if c["cluster_code"] == k), "")))}
    if silent_drift:
        L.append("## ⚠ Post-closure activity detected (status string out of sync)")
        L.append("")
        L.append("These clusters have `mti_terms.last_changed > cluster.last_updated_date` but the status string does not carry the `(Terms Added)` suffix.")
        L.append("")
        L.append("| Cluster | Current status | Terms changed post-closure | Latest change |")
        L.append("|---|---|---:|---|")
        for code in sorted(silent_drift):
            current = next((c["status"] for c in clusters if c["cluster_code"] == code), "?")
            info = silent_drift[code]
            L.append(f"| `{code}` | {current} | {info['n_terms']} | {(info['latest'] or '')[:10]} |")
        L.append("")

    L.append("## Per-cluster detail")
    L.append("")
    L.append("| | Code | Short | Description | Status | Terms (OT+NT) | Sub-grps | Verses (in-scope) | Set-aside | Occ | Anchors | Findings (s/f/g/syn) | SC inputs | SC published | Updated |")
    L.append("|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|:-:|:-:|---|")
    sc_inputs_total = sc_published_total = 0
    for c in clusters:
        code = c["cluster_code"]
        tc = term_counts.get(code, {}); ot = tc.get("Hebrew", 0); nt = tc.get("Greek", 0)
        terms_total = ot + nt
        terms_str = f"{terms_total} ({ot}+{nt})" if terms_total else "—"
        sg = sg_counts.get(code, 0)
        vin = inscope.get(code, 0); vsa = setaside.get(code, 0); voc = occ.get(code, 0); a = anchor_counts.get(code, 0)
        fc = finding_counts.get(code, {})
        if fc:
            f_str = f"{fc.get('silent',0)}/{fc.get('finding',0)}/{fc.get('gap',0)}/{fc.get('cluster_synthesis',0)}"
            f_cell = f"{sum(fc.values())} ({f_str})"
        else:
            f_cell = "—"
        sc_in, sc_pub = session_c_status(code, c["status"], chapter_codes_by_cluster.get(code, set()))
        if sc_in.startswith("✓"):
            sc_inputs_total += 1
        if sc_pub == "✓":
            sc_published_total += 1
        updated = (c["last_updated_date"] or "")[:10]
        L.append(f"| {status_marker(c['status'])} | **{code}** | {c['short_name'] or ''} | {c['description'] or ''} | {c['status']} "
                 f"| {terms_str} | {sg} | {vin} | {vsa if vsa else '—'} | {voc} | {a} | {f_cell} | {sc_in} | {sc_pub} | {updated} |")
    L.append("")
    L.append(f"_Session C totals: **{sc_inputs_total}** clusters with full inputs on file · **{sc_published_total}** clusters published._")
    L.append("")

    L.append("## Cluster glosses (full term-gloss lists)")
    L.append("")
    L.append("The full `cluster.gloss` field for each cluster — the complete list of primary terms (with parenthetical transliterations) covered by the cluster.")
    L.append("")
    for c in clusters:
        code = c["cluster_code"]; short = c["short_name"] or ""; desc = c["description"] or ""
        gloss = (c["gloss"] or "").strip()
        header_tail = f" — {desc}" if desc else ""; header_short = f" ({short})" if short else ""
        L.append(f"### {code}{header_tail}{header_short}")
        L.append("")
        L.append(gloss if gloss else "_(no gloss recorded)_")
        L.append("")
        L.append("---")
        L.append("")

    L.append("## Notation")
    L.append("")
    L.append("- **Status markers:** ✓ completed · ✓+ completed (terms added) · ▶ in progress · ⏸ parked · · not started")
    L.append("- **Terms (OT+NT):** active `mti_terms` split by language (Hebrew + Greek)")
    L.append("- **Verses (in-scope):** DISTINCT verses (references), active, `set_aside_reason IS NULL` — the ve_lexical extract corpus")
    L.append("- **Set-aside:** DISTINCT verses with at least one set-aside (out-of-scope) occurrence; `—` = none set aside (cluster not yet reworked, or nothing excluded)")
    L.append("- **Occ:** term-in-verse occurrences (active `verse_context` rows) — what the prior overview mislabelled 'Verses'")
    L.append("- **Anchors:** `verse_context.is_anchor=1` active rows")
    L.append("- **Findings (s/f/g/syn):** `silent` / `finding` / `gap` / `cluster_synthesis` counts (total in parens)")
    L.append("- **SC inputs / SC published:** Session-C per-chapter inputs on disk / chapter prose in `prose_section`")
    L.append("")

    out_path.write_text("\n".join(L), encoding="utf-8")
    print(f"Wrote: {out_path}")
    print(f"Clusters: {len(clusters)} | in-scope verses: {tot_in:,} | set-aside: {tot_sa:,} | occ: {tot_occ:,}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
