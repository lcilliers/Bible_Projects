"""Reusable applier for evaluated pointer/finding dispositions (per cluster).

Reads a dispositions JSON (e.g. Sessions/Session_Clusters/{CODE}/
wa-cluster-{CODE}-pointer-dispositions-v1-{date}.json) where each item has been
EVALUATED on content (v3_0 §10.1 / v2_9 §18) and assigned an action:
  - set_aside (wa_session_b_findings): status='set_aside' + resolution_note
  - resolve   (wa_session_research_flags): resolved=1 + resolved_date + resolved_note
  - fold      (wa_session_b_findings): status='folded' + resolution_note (content captured by a tier finding)
Documented NO-OP actions (recorded for the audit report, no DB write) — action text
starting 'review' or 'surface': skipped (e.g. A2 false-positive review, B7 analytical
residual). Any other unrecognised action ABORTS (typo safety).
The reason text (the evaluation conclusion) is recorded on the row. Guarded.

DEFAULT DRY-RUN. --file PATH required. --apply to write.
"""
import argparse, json, sqlite3, os
DB="database/bible_research.db"
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--file",required=True); ap.add_argument("--apply",action="store_true"); a=ap.parse_args()
    d=json.load(open(a.file,encoding="utf-8")); items=d["dispositions"]
    c=sqlite3.connect(DB,timeout=30); cur=c.cursor()
    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: cluster={d.get('cluster')} dispositions={len(items)}")
    for it in items:
        print(f"  {it['table']} id={it['id']} -> {it['action']}: {it['reason'][:80]}")
    if not a.apply:
        c.close(); return
    cur.execute("BEGIN")
    try:
        n=0; expected=0; skipped=0
        for it in items:
            t,i,act,reason=it["table"],it["id"],it["action"],it["reason"]
            if t=="wa_session_b_findings" and act in ("set_aside","fold"):
                st="set_aside" if act=="set_aside" else "folded"
                cur.execute("UPDATE wa_session_b_findings SET status=?, resolution_note=? WHERE id=?",(st,reason,i)); n+=cur.rowcount; expected+=1
            elif t=="wa_session_research_flags" and act=="resolve":
                cur.execute("UPDATE wa_session_research_flags SET resolved=1, resolved_date=datetime('now'), resolved_note=? WHERE id=?",(reason,i)); n+=cur.rowcount; expected+=1
            elif act.lower().startswith(("review","surface")):
                skipped+=1  # documented no-op (rendered in the report; no DB change)
            else:
                c.rollback(); raise SystemExit(f"ABORT: unsupported {t}/{act}")
        if n!=expected:
            c.rollback(); raise SystemExit(f"ABORT: wrote {n}!=expected {expected}")
        c.commit()
    except Exception:
        c.rollback(); raise
    print(f"APPLIED: {n} dispositions written, {skipped} documented no-op(s) skipped.")
    c.close()
if __name__=="__main__": main()
