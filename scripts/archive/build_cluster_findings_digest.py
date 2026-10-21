"""Read-only: dump a cluster's active findings as a navigable markdown digest.

Per characteristic -> sub-group, lists each cluster_finding (status + text + the verses
it cites), so the cluster's actual analytical conclusions are reviewable as the backdrop
for comment-evaluation. NEVER writes the DB.

  python scripts/build_cluster_findings_digest.py --cluster M38
  -> Sessions/Session_Clusters/{CODE}/wa-cluster-{CODE}-findings-digest-v1-{date}.md
"""
import argparse, os, sqlite3, sys
from datetime import datetime, timezone

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DB = os.path.join("database", "bible_research.db")
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--status", default=None, help="filter finding_status (e.g. finding)")
    a = ap.parse_args()
    code = a.cluster
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    cur = c.cursor()

    desc = cur.execute("SELECT description FROM cluster WHERE cluster_code=?", (code,)).fetchone()
    cites = {}
    for r in cur.execute("SELECT fc.source_id sid, GROUP_CONCAT(DISTINCT fc.citation_value) v FROM finding_citation fc JOIN cluster_finding cf ON cf.id=fc.source_id AND fc.source_table='cluster_finding' WHERE cf.cluster_code=? AND fc.citation_type='verse' AND COALESCE(cf.delete_flagged,0)=0 GROUP BY fc.source_id", (code,)):
        cites[r["sid"]] = r["v"]

    L = [f"# {code} — findings digest ({desc['description'] if desc else ''})", "",
         f"**Read-only · generated {DATE}.** The cluster's active `cluster_finding` rows, by "
         "characteristic. This is the analytical backdrop for evaluating incoming comments "
         "(A6/A7/D2) — does a comment confirm, extend, or duplicate what is already here?", ""]

    chars = cur.execute("SELECT id, char_seq, short_name FROM characteristic WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 ORDER BY char_seq", (code,)).fetchall()
    total = 0
    for ch in chars:
        rows = cur.execute("SELECT id, finding_status, finding_text FROM cluster_finding WHERE characteristic_id=? AND cluster_code=? AND COALESCE(delete_flagged,0)=0" + (" AND finding_status=?" if a.status else "") + " ORDER BY id", ((ch["id"], code, a.status) if a.status else (ch["id"], code))).fetchall()
        L.append(f"## char {ch['char_seq']} — {ch['short_name']} ({len(rows)} findings)")
        L.append("")
        for r in rows:
            total += 1
            cv = cites.get(r["id"], "")
            L.append(f"- **[{r['id']} · {r['finding_status']}]** {r['finding_text'].strip()}")
            if cv:
                L.append(f"  - _cites:_ {cv}")
        L.append("")

    synth = cur.execute("SELECT id, finding_text FROM cluster_finding WHERE cluster_code=? AND finding_status='cluster_synthesis' AND COALESCE(delete_flagged,0)=0 ORDER BY id", (code,)).fetchall()
    if synth:
        L.append(f"## cluster synthesis ({len(synth)} rows)")
        L.append("")
        for r in synth:
            L.append(f"- **[{r['id']}]** {r['finding_text'].strip()}")
        L.append("")

    out = os.path.join("Sessions", "Session_Clusters", code, f"wa-cluster-{code}-findings-digest-v1-{DATE}.md")
    open(out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"wrote {out} ({total} char-findings + {len(synth)} synthesis)")
    c.close()


if __name__ == "__main__":
    main()
