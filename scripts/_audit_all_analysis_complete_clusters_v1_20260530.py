"""Run the cluster input coverage audit on every Analysis Complete cluster
and aggregate the results into a single summary report.

Identifies all clusters with status containing 'Analysis Complete' (case
insensitive), invokes the v2 audit script per cluster, captures the
per-section pass/fail and counts, and writes a single matrix report to
outputs/markdown/publishing_readiness_programme_v1_{date}.md.
"""
from __future__ import annotations
import sqlite3, sys, subprocess, re
from pathlib import Path
from datetime import datetime

try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB_PATH = "database/bible_research.db"
AUDIT_SCRIPT = "scripts/_audit_cluster_input_coverage_v2_20260530.py"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def fetch_analysis_complete_clusters(conn):
    rows = conn.execute("""
        SELECT cluster_code, short_name, status
          FROM cluster
         WHERE LOWER(status) LIKE '%analysis complete%'
            OR LOWER(status) LIKE '%publication%'
         ORDER BY cluster_code
    """).fetchall()
    return [dict(r) for r in rows]


def has_inputs(code):
    p = Path(f"Sessions/Session_Clusters/{code}/inputs")
    if not p.exists():
        return False
    return any(p.glob(f"wa-cluster-{code}-ch*-input-v*.md"))


def run_audit(code):
    """Run the audit on a cluster, parse stdout for the summary numbers."""
    try:
        result = subprocess.run(
            ["python", AUDIT_SCRIPT, "--cluster", code],
            capture_output=True, text=True, encoding="utf-8", timeout=120
        )
    except subprocess.TimeoutExpired:
        return {"error": "timeout"}
    text = result.stdout + result.stderr
    return parse_audit_stdout(text)


def parse_audit_stdout(text):
    """Extract structured numbers from the audit's console summary."""
    out = {
        "inputs_count": None,
        "coverage_pass": None,
        "exclusion_pass": None,
        "boundary_pass": None,
        "stray_pass": None,
        "overall_pass": None,
        "missing_findings": None,
        "missing_subgroups": None,
        "missing_characteristics": None,
        "missing_vcgs": None,
        "missing_anchors": None,
        "missing_pub_obs": None,
        "leaked_gap": None,
        "leaked_nonpub_obs": None,
        "stray_sb": None,
        "stray_flags": None,
        "sd_runs": None,
        "boundary_issues": [],
        "raw": text,
    }
    m = re.search(r"Inputs audited:\s*(\d+)\s*files", text)
    if m: out["inputs_count"] = int(m.group(1))
    m = re.search(r"A\. COVERAGE:\s*(PASS|FAIL)", text)
    if m: out["coverage_pass"] = (m.group(1) == "PASS")
    m = re.search(r"B\. EXCLUSION:\s*(PASS|FAIL)", text)
    if m: out["exclusion_pass"] = (m.group(1) == "PASS")
    m = re.search(r"C\. BOUNDARY READINESS:\s*(PASS|FAIL)", text)
    if m: out["boundary_pass"] = (m.group(1) == "PASS")
    m = re.search(r"D\. STRAY SB/SD FINDINGS:\s*(PASS|FAIL)", text)
    if m: out["stray_pass"] = (m.group(1) == "PASS")
    m = re.search(r"Verdict:\s*(PASS|FAIL)", text)
    if m: out["overall_pass"] = (m.group(1) == "PASS")
    for label, key in [
        ("Findings missing", "missing_findings"),
        ("Sub-groups missing", "missing_subgroups"),
        ("Characteristics missing", "missing_characteristics"),
        ("VCG codes missing", "missing_vcgs"),
        ("Anchor verses missing", "missing_anchors"),
        ("Pub observations missing", "missing_pub_obs"),
        ("Gap findings leaked", "leaked_gap"),
        ("Non-pub obs leaked", "leaked_nonpub_obs"),
        ("Stray SB findings", "stray_sb"),
        ("Stray SB/SD research flags", "stray_flags"),
        ("session_d_runs referencing", "sd_runs"),
    ]:
        m = re.search(rf"{re.escape(label)}[:\s]*\D*?(\d+)", text)
        if m:
            out[key] = int(m.group(1))
    # Boundary issue lines start with "   - "
    out["boundary_issues"] = re.findall(r"^\s+- (.+)$", text, flags=re.MULTILINE)
    return out


def emit(line, lines):
    lines.append(line)


def main():
    conn = get_conn()
    clusters = fetch_analysis_complete_clusters(conn)
    print(f"Found {len(clusters)} Analysis Complete cluster(s) to audit.\n")

    results = []
    for cl in clusters:
        code = cl["cluster_code"]
        has_inp = has_inputs(code)
        print(f"  [{code:6}] {cl['status']:35} {cl['short_name']:20} ... ", end="", flush=True)
        if not has_inp:
            results.append({**cl, "inputs": False})
            print("(no inputs)")
            continue
        audit = run_audit(code)
        results.append({**cl, "inputs": True, "audit": audit})
        v = audit.get("overall_pass")
        print("PASS" if v else "FAIL" if v is False else "?")

    # ---------- Report ----------
    out_path = Path("outputs/markdown") / f"publishing_readiness_programme_v1_{datetime.now():%Y%m%d}.md"
    lines = []
    lines.append("# Programme-level publishing readiness — Analysis Complete clusters")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now():%Y-%m-%d %H:%M}")
    lines.append("")
    lines.append(f"Coverage audit run across all {len(clusters)} clusters whose status contains "
                "'Analysis Complete' or 'Publication'. Per-cluster reports are at "
                "`outputs/markdown/cluster_input_coverage_{CODE}_v2_{date}.md`.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Headline matrix
    lines.append("## Headline matrix")
    lines.append("")
    lines.append("| Cluster | Status | Word | Inputs? | Coverage | Exclusion | BOUNDARY | Stray SB/SD | Verdict |")
    lines.append("|---|---|---|---|---|---|---|---|---|")

    def fmt(v):
        if v is None: return "?"
        return "PASS" if v else "FAIL"

    counters = {"verdict_pass": 0, "verdict_fail": 0, "no_inputs": 0,
                "cov_fail": 0, "exc_fail": 0, "bnd_fail": 0, "str_fail": 0}

    for r in results:
        code = r["cluster_code"]
        word = r["short_name"]
        status = r["status"]
        if not r.get("inputs"):
            lines.append(f"| {code} | {status} | {word} | NO | — | — | — | — | NO INPUTS |")
            counters["no_inputs"] += 1
            continue
        a = r["audit"]
        if a.get("overall_pass"):
            counters["verdict_pass"] += 1
        else:
            counters["verdict_fail"] += 1
            if a.get("coverage_pass") is False: counters["cov_fail"] += 1
            if a.get("exclusion_pass") is False: counters["exc_fail"] += 1
            if a.get("boundary_pass") is False: counters["bnd_fail"] += 1
            if a.get("stray_pass") is False: counters["str_fail"] += 1
        lines.append(f"| {code} | {status} | {word} | YES | "
                    f"{fmt(a.get('coverage_pass'))} | {fmt(a.get('exclusion_pass'))} | "
                    f"{fmt(a.get('boundary_pass'))} | {fmt(a.get('stray_pass'))} | "
                    f"{fmt(a.get('overall_pass'))} |")
    lines.append("")

    # Counters
    lines.append("**Summary:**")
    lines.append("")
    lines.append(f"- Verdicts: PASS {counters['verdict_pass']} · FAIL {counters['verdict_fail']} "
                f"· no inputs {counters['no_inputs']}")
    lines.append(f"- Coverage failures: {counters['cov_fail']}")
    lines.append(f"- Exclusion failures: {counters['exc_fail']}")
    lines.append(f"- BOUNDARY readiness failures: {counters['bnd_fail']}")
    lines.append(f"- Stray SB / SD findings failures: {counters['str_fail']}")
    lines.append("")

    # Detail matrix
    lines.append("---")
    lines.append("")
    lines.append("## Detail counts")
    lines.append("")
    lines.append("| Cluster | Miss find | Miss SG | Miss char | Miss VCG | Miss anchor | Miss obs | Leak gap | Leak obs | Stray SB | Stray flags | SD runs |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in results:
        code = r["cluster_code"]
        if not r.get("inputs"):
            lines.append(f"| {code} | — | — | — | — | — | — | — | — | — | — | — |")
            continue
        a = r["audit"]
        def n(k): return a.get(k) if a.get(k) is not None else "?"
        lines.append(f"| {code} | {n('missing_findings')} | {n('missing_subgroups')} "
                    f"| {n('missing_characteristics')} | {n('missing_vcgs')} | {n('missing_anchors')} "
                    f"| {n('missing_pub_obs')} | {n('leaked_gap')} | {n('leaked_nonpub_obs')} "
                    f"| {n('stray_sb')} | {n('stray_flags')} | {n('sd_runs')} |")
    lines.append("")

    # Per-cluster BOUNDARY issue text
    lines.append("---")
    lines.append("")
    lines.append("## BOUNDARY-readiness issue text per cluster")
    lines.append("")
    for r in results:
        if not r.get("inputs"): continue
        issues = r["audit"].get("boundary_issues", [])
        if not issues: continue
        lines.append(f"**{r['cluster_code']} ({r['short_name']}):**")
        for i in issues:
            lines.append(f"- {i}")
        lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")

    # Console summary
    print()
    print(f"Verdicts: PASS={counters['verdict_pass']}  FAIL={counters['verdict_fail']}  "
          f"NO_INPUTS={counters['no_inputs']}")
    print(f"Failures by category: coverage={counters['cov_fail']}  "
          f"exclusion={counters['exc_fail']}  boundary={counters['bnd_fail']}  "
          f"stray={counters['str_fail']}")
    print()
    print(f"Programme summary: {out_path}")


if __name__ == "__main__":
    main()
