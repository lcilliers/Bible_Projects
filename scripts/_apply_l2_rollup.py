"""_apply_l2_rollup.py — roll the VERSE-level L2 findings up to CLUSTER-level findings (the "characteristic =
roll-up over findings"). Per tier question, aggregates the cluster's verse findings (value distribution +
ANSWERED/STATED_SILENT/STATED_UNRESOLVED counts) into one CLUSTER-level `finding` (level=CLUSTER,
provenance='l2_rollup'), linked to the tier question. Surfaces the D5 rarity (e.g. a locus named in only a
few of N verses is itself significant). Idempotent / reversible.

Usage:  python scripts/_apply_l2_rollup.py --cluster M01 --dry-run|--live --out <file>.md
"""
import argparse, os, sqlite3, sys
from collections import Counter, defaultdict
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--cluster", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    ap.add_argument("--out", required=True); a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()
    now = c.execute("SELECT datetime('now')").fetchone()[0]
    mids = [r[0] for r in c.execute("SELECT id FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (a.cluster,))]
    qm = ",".join("?" * len(mids))

    # aggregate verse findings per tier question
    rows = c.execute(
        f"SELECT l.question_id qid, q.question_code qc, q.component_title ct, f.finding_status st, f.finding_value v "
        f"FROM finding f JOIN finding_question_link l ON l.finding_id=f.id "
        f"JOIN wa_obs_question_catalogue q ON q.obs_id=l.question_id "
        f"WHERE f.provenance='l2_mechanical' AND f.level='VERSE' AND f.mti_term_id IN ({qm})", mids).fetchall()
    by_q = defaultdict(lambda: {"status": Counter(), "vals": Counter(), "code": "", "title": ""})
    for r in rows:
        d = by_q[r["qid"]]; d["code"] = r["qc"]; d["title"] = r["ct"]
        d["status"][r["st"]] += 1
        if r["st"] == "ANSWERED":
            d["vals"][(r["v"] or "")[:60]] += 1

    already = {r[0] for r in c.execute(
        "SELECT q.obs_id FROM finding f JOIN finding_question_link l ON l.finding_id=f.id "
        "JOIN wa_obs_question_catalogue q ON q.obs_id=l.question_id "
        "WHERE f.provenance='l2_rollup' AND f.cluster_code=?", (a.cluster,))}

    L = [f"# L2 roll-up — VERSE findings → CLUSTER findings: {a.cluster} ({'LIVE' if a.live else 'DRY-RUN'})", ""]
    L.append("> `scripts/_apply_l2_rollup.py`. Aggregates the cluster's verse findings per tier into a "
             "CLUSTER-level finding. The rarity of a positive finding (few ANSWERED among many STATED_SILENT) "
             "is itself significant (D5). Idempotent / reversible (provenance='l2_rollup').")
    L.append("")
    nwrote = 0
    for qid, d in sorted(by_q.items(), key=lambda x: x[1]["code"]):
        tot = sum(d["status"].values())
        ans = d["status"]["ANSWERED"]; sil = d["status"]["STATED_SILENT"]; unr = d["status"]["STATED_UNRESOLVED"]
        top = d["vals"].most_common(6)
        dist = "; ".join(f"{v}×{n}" for v, n in top)
        summary = (f"[{d['code']} {d['title']}] {a.cluster}: {ans}/{tot} answered, {sil} silent, {unr} unresolved. "
                   + (f"Top: {dist}." if dist else "")
                   + (f" RARE POSITIVE — answered in only {ans}/{tot} ({100*ans/tot:.0f}%)." if 0 < ans <= tot * 0.15 else ""))
        L.append(f"## {d['code']} — {d['title']}")
        L.append(f"- answered **{ans}** · silent **{sil}** · unresolved **{unr}** (of {tot})")
        if top:
            L.append(f"- value distribution: {dist}")
        L.append("")
        if a.live and qid not in already:
            cur = c.execute("INSERT INTO finding (level, cluster_code, finding_value, finding_status, provenance, "
                            "created_at, last_updated_date, delete_flagged) VALUES ('CLUSTER',?,?,?,?,?,?,0)",
                            (a.cluster, summary, "RESOLVED", "l2_rollup", now, now))
            c.execute("INSERT INTO finding_question_link (finding_id, question_id, coverage, created_at, delete_flagged) "
                      "VALUES (?,?,?,?,0)", (cur.lastrowid, qid, "rollup", now))
            nwrote += 1
    if a.live:
        conn.commit()
    L.insert(4, f"**{len(by_q)} tiers rolled up · {nwrote if a.live else len(by_q)-len(already)} cluster findings "
             f"{'written' if a.live else 'to write'} ({len(already)} already present).**\n")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{'LIVE' if a.live else 'DRY'}: {a.cluster} {len(by_q)} tiers rolled up; wrote {nwrote if a.live else 0} cluster findings; {a.out}")


if __name__ == "__main__":
    main()
