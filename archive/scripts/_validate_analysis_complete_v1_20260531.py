"""Validate the Analysis-Complete gate across all clusters at/beyond Analysis Complete.

Implements the two-condition gate (Workflow/methodology/wa-cluster-readiness-gate-design.md §3):
  Condition 1 — verse/tier findings captured.
  Condition 2 — every leftover (boundary / flag / Session B/D pointer) resolved
                to a validated observation or deleted after review.

For each target cluster it runs the checks, writes a per-cluster failure detail
report, and (only with --apply) RESETS a failing cluster's status to
'Analysis - In Progress'. Ends with a cross-cluster summary by failure type.

DEFAULT IS DRY-RUN (report only; no DB writes). Pass --apply to perform resets.

Each leftover source notes its link-method to the cluster, because that linkage
differs by source (some are cluster-direct, some go via registry and are
non-exclusive — see the readiness-gate design §3.2).

Usage:
  python scripts/_validate_analysis_complete_v1_20260531.py            # dry-run
  python scripts/_validate_analysis_complete_v1_20260531.py --apply     # reset failures
"""
import argparse
import os
import sqlite3
import sys

DB = os.path.join("database", "bible_research.db")

# ---- configurable defaults (still-open §6 questions; adjust here, not in code) ----
TARGET_STATUSES = ("Analysis Complete", "Analysis Completed", "Analysis Completed (Terms Added)")
RESET_TO_STATUS = "Analysis - In Progress"
# Condition-2 gating flag codes (§6 q2 proposal). Informational codes excluded.
GATING_FLAG_CODES = ("SD_POINTER", "SB_FINDING", "BOUNDARY_DECISION_PENDING",
                     "PH2_CROSS_REGISTRY_REQUIRED", "PH2_DATA_SPLIT_REQUIRED",
                     "PH2_EXEGETICAL_STUDY_REQUIRED", "PH2_THEOLOGICAL_DEPTH_REQUIRED",
                     "PH2_ESCHATOLOGICAL_STUDY_REQUIRED", "PH2_DATA_ERROR")
# Condition-2 actionable observation types (§6 q3 proposal). All others informational/exempt.
ACTIONABLE_OBS_TYPES = ("CROSS_CLUSTER_HANDOFF", "SELF_CHECK_OBSERVATION")


def get_conn():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------- checks ----------------
# Each returns (severity, count, detail_lines). severity: 'HARD' blocks (→ demote), 'ADVISORY' reports only.

def chk_findings_present(conn, code):
    n = conn.execute("SELECT COUNT(*) FROM cluster_finding WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
                     (code,)).fetchone()[0]
    if n == 0:
        return "HARD", 1, ["No active cluster_finding rows — Condition 1 not met (no captured findings)."]
    return None, 0, [f"{n} active findings present."]


def chk_synthesis_as_gap(conn, code):
    rows = conn.execute("""
        SELECT id, SUBSTR(finding_text,1,120) t FROM cluster_finding
         WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
           AND finding_status='cluster_synthesis'
           AND (finding_text LIKE '%gap%' OR finding_text LIKE '%could not%'
                OR finding_text LIKE '%not able%' OR finding_text LIKE '%unable to%'
                OR finding_text LIKE '%no T%null%')
    """, (code,)).fetchall()
    if rows:
        return "ADVISORY", len(rows), [f"id={r['id']}: {r['t']}" for r in rows[:10]]
    return None, 0, []


def chk_boundary_members(conn, code):
    sg = conn.execute("""SELECT id, label FROM cluster_subgroup
                         WHERE cluster_code=? AND subgroup_code='BOUNDARY' AND COALESCE(delete_flagged,0)=0""",
                      (code,)).fetchone()
    if not sg:
        return None, 0, []
    v = conn.execute("SELECT COUNT(*) FROM verse_context WHERE cluster_subgroup_id=? AND COALESCE(delete_flagged,0)=0",
                     (sg["id"],)).fetchone()[0]
    t = conn.execute("SELECT COUNT(*) FROM mti_term_subgroup WHERE cluster_subgroup_id=? AND COALESCE(delete_flagged,0)=0",
                     (sg["id"],)).fetchone()[0]
    g = conn.execute("""SELECT COUNT(DISTINCT vc.group_id) FROM verse_context vc
                          JOIN verse_context_group vcg ON vcg.id=vc.group_id
                         WHERE vc.cluster_subgroup_id=? AND COALESCE(vc.delete_flagged,0)=0
                           AND COALESCE(vcg.delete_flagged,0)=0""", (sg["id"],)).fetchone()[0]
    if v or t or g:
        return "HARD", v + t + g, [f"BOUNDARY sub-group '{sg['label']}' still has {v} verses, {t} terms, {g} VCGs (cluster-direct link)."]
    return None, 0, []


def chk_boundary_pending_flags(conn, code):
    rows = conn.execute("""SELECT id, flag_label FROM wa_session_research_flags
                           WHERE flag_code='BOUNDARY_DECISION_PENDING' AND COALESCE(resolved,0)=0
                             AND flag_label LIKE ?""", (code + "%",)).fetchall()
    if rows:
        return "HARD", len(rows), [f"id={r['id']} {r['flag_label']}" for r in rows[:15]] + ["(link: flag_label prefix)"]
    return None, 0, []


def chk_gating_flags(conn, code):
    """Unresolved gating flags on registries whose terms are in this cluster.
    LINK CAVEAT: registry->cluster is non-exclusive (a registry's terms span clusters);
    a pointer counted here may also count against other clusters. Definitive
    attribution is the A1 conversion session's job."""
    codes = ",".join("?" for _ in GATING_FLAG_CODES)
    rows = conn.execute(f"""
        SELECT f.flag_code, COUNT(*) n FROM wa_session_research_flags f
         WHERE COALESCE(f.resolved,0)=0 AND f.flag_code IN ({codes})
           AND f.flag_code != 'BOUNDARY_DECISION_PENDING'
           AND f.registry_id IN (SELECT DISTINCT owning_registry_fk FROM mti_terms
                                  WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0)
         GROUP BY f.flag_code ORDER BY n DESC
    """, (*GATING_FLAG_CODES, code)).fetchall()
    total = sum(r["n"] for r in rows)
    if total:
        det = [f"{r['flag_code']}: {r['n']}" for r in rows]
        det.append("(link: registry→cluster, NON-EXCLUSIVE — resolved globally by the A1 session)")
        return "HARD", total, det
    return None, 0, []


def chk_stray_sb_findings(conn, code):
    """wa_session_b_findings still pending/open, linked precisely via term→sub-group→cluster."""
    try:
        rows = conn.execute("""
            SELECT COUNT(DISTINCT sbf.id) n FROM wa_session_b_findings sbf
              JOIN mti_terms mt ON mt.owning_registry_fk = sbf.registry_id AND COALESCE(mt.delete_flagged,0)=0
              JOIN mti_term_subgroup mts ON mts.mti_term_id = mt.id AND COALESCE(mts.delete_flagged,0)=0
              JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
             WHERE cs.cluster_code=? AND sbf.status IN ('pending','open')
        """, (code,)).fetchone()
        n = rows["n"]
    except sqlite3.OperationalError as e:
        return "ADVISORY", 0, [f"(could not check wa_session_b_findings: {e})"]
    if n:
        return "HARD", n, [f"{n} stray Session-B findings (status pending/open; link: term→sub-group→cluster)."]
    return None, 0, []


def chk_unconfirmed_actionable_obs(conn, code):
    types = ",".join("?" for _ in ACTIONABLE_OBS_TYPES)
    rows = conn.execute(f"""
        SELECT id, observation_type, status, SUBSTR(title,1,80) t FROM cluster_observation
         WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
           AND observation_type IN ({types})
           AND COALESCE(status,'') != 'confirmed'
    """, (code, *ACTIONABLE_OBS_TYPES)).fetchall()
    if rows:
        return "HARD", len(rows), [f"id={r['id']} {r['observation_type']} [{r['status']}] {r['t']}" for r in rows[:15]]
    return None, 0, []


def chk_orphan_findings(conn, code):
    n = conn.execute("""SELECT COUNT(*) FROM cluster_finding
                        WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
                          AND finding_status NOT IN ('cluster_synthesis')
                          AND characteristic_id IS NULL AND cluster_subgroup_id IS NULL""",
                     (code,)).fetchone()[0]
    if n:
        return "ADVISORY", n, [f"{n} non-synthesis findings with no characteristic AND no sub-group (dangling)."]
    return None, 0, []


CHECKS = [
    ("C1 findings present", "Condition 1", chk_findings_present),
    ("C1 synthesis-as-gap (heuristic)", "Condition 1", chk_synthesis_as_gap),
    ("C2 active BOUNDARY members", "Condition 2", chk_boundary_members),
    ("C2 BOUNDARY_DECISION_PENDING flags", "Condition 2", chk_boundary_pending_flags),
    ("C2 unresolved gating flags (SB/SD/PH2)", "Condition 2", chk_gating_flags),
    ("C2 stray Session-B findings", "Condition 2", chk_stray_sb_findings),
    ("C2 unconfirmed actionable observations", "Condition 2", chk_unconfirmed_actionable_obs),
    ("C2 orphan findings", "Condition 2", chk_orphan_findings),
]


def validate_cluster(conn, code):
    results = []
    for name, cond, fn in CHECKS:
        sev, count, detail = fn(conn, code)
        results.append({"name": name, "condition": cond, "severity": sev, "count": count, "detail": detail})
    hard = [r for r in results if r["severity"] == "HARD"]
    verdict = "FAIL" if hard else "PASS"
    return verdict, results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Reset failing clusters to '%s' (default: dry-run)" % RESET_TO_STATUS)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    conn = get_conn()
    clusters = conn.execute(
        "SELECT cluster_code, status FROM cluster WHERE status IN (%s) ORDER BY cluster_code"
        % ",".join("?" for _ in TARGET_STATUSES), TARGET_STATUSES).fetchall()

    out_path = args.out or os.path.join("outputs", "markdown", "cluster_ac_validation_v1_20260531.md")
    L = []
    L.append("# Analysis-Complete validation report")
    L.append("")
    L.append(f"**Mode:** {'APPLY (resets performed)' if args.apply else 'DRY-RUN (no DB writes)'}")
    L.append(f"**Target statuses:** {', '.join(TARGET_STATUSES)} — {len(clusters)} clusters")
    L.append(f"**Gate:** Workflow/methodology/wa-cluster-readiness-gate-design.md §3 (two-condition gate)")
    L.append(f"**Reset target on FAIL:** `{RESET_TO_STATUS}`")
    L.append("")
    L.append("> HARD checks gate completion (a single HARD failure → cluster is not validly complete → reset). "
             "ADVISORY checks are reported for review but do not by themselves demote.")
    L.append("")

    type_tally = {}     # failure name -> [clusters]
    cond_tally = {"Condition 1": [], "Condition 2": []}
    verdicts = {}
    to_reset = []

    L.append("## Per-cluster detail")
    for c in clusters:
        code = c["cluster_code"]
        verdict, results = validate_cluster(conn, code)
        verdicts[code] = verdict
        if verdict == "FAIL":
            to_reset.append(code)
        L.append("")
        L.append(f"### {code} — current `{c['status']}` → **{verdict}**")
        L.append("")
        L.append("| Check | Condition | Severity | Count | Detail |")
        L.append("|---|---|---|---:|---|")
        for r in results:
            if r["severity"] is None:
                continue
            det = "<br>".join(d.replace("|", "\\|") for d in r["detail"]) if r["detail"] else ""
            L.append(f"| {r['name']} | {r['condition']} | {r['severity']} | {r['count']} | {det} |")
            if r["severity"] == "HARD":
                type_tally.setdefault(r["name"], []).append(code)
                if code not in cond_tally[r["condition"]]:
                    cond_tally[r["condition"]].append(code)
        if all(r["severity"] is None for r in results):
            L.append("| (all checks passed) | | | | |")

    # apply resets
    reset_done = []
    if args.apply and to_reset:
        cur = conn.cursor()
        cur.execute("BEGIN")
        try:
            for code in to_reset:
                cur.execute("UPDATE cluster SET status=?, last_updated_date=datetime('now') WHERE cluster_code=?",
                            (RESET_TO_STATUS, code))
                reset_done.append(code)
            conn.commit()
        except Exception:
            conn.rollback()
            raise

    # cross-cluster summary
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Cross-cluster summary")
    L.append("")
    npass = sum(1 for v in verdicts.values() if v == "PASS")
    nfail = sum(1 for v in verdicts.values() if v == "FAIL")
    L.append(f"- Clusters validated: **{len(clusters)}** — PASS **{npass}**, FAIL **{nfail}**.")
    L.append(f"- Failing on Condition 1 (findings): **{len(cond_tally['Condition 1'])}** — {', '.join(cond_tally['Condition 1']) or 'none'}")
    L.append(f"- Failing on Condition 2 (leftovers): **{len(cond_tally['Condition 2'])}** — {', '.join(cond_tally['Condition 2']) or 'none'}")
    if args.apply:
        L.append(f"- **Reset to `{RESET_TO_STATUS}`:** {len(reset_done)} — {', '.join(reset_done) or 'none'}")
    else:
        L.append(f"- **Would reset (dry-run):** {len(to_reset)} — {', '.join(to_reset) or 'none'}")
    L.append("")
    L.append("### Failures by type")
    L.append("")
    L.append("| Failure type (HARD) | # clusters | Clusters |")
    L.append("|---|---:|---|")
    for name in sorted(type_tally, key=lambda k: -len(type_tally[k])):
        cl = type_tally[name]
        L.append(f"| {name} | {len(cl)} | {', '.join(cl)} |")
    if not type_tally:
        L.append("| (no HARD failures) | 0 | |")

    conn.close()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

    # stdout summary
    print(f"{'APPLY' if args.apply else 'DRY-RUN'}: {len(clusters)} clusters | PASS {npass} | FAIL {nfail}")
    if args.apply:
        print(f"Reset to '{RESET_TO_STATUS}': {len(reset_done)} ({', '.join(reset_done) or 'none'})")
    else:
        print(f"Would reset: {len(to_reset)} ({', '.join(to_reset) or 'none'})")
    print(f"Report: {out_path}")


if __name__ == "__main__":
    main()
