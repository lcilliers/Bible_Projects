"""Reusable applier for B7 analytical-residual citation extensions (per cluster).

The audit B7 aspect flags anchor verses that no finding cites. When the residual
is genuine (the anchor truly evidences the characteristic but no finding text uses
it), the correct fix is ANALYTICAL: extend the host finding's *text* with a faithful
exemplar sentence that references the verse in canonical `Book chap:verse` form, then
re-run the citation extractor (which re-derives finding_citation from finding text).
This applier performs only the text extension; it NEVER writes finding_citation rows
directly (no fabrication — the extractor remains the single source of citations).

Reads a spec JSON (Sessions/Session_Clusters/{CODE}/
wa-cluster-{CODE}-b7-citation-extension-v1-{date}.json):
  { "cluster": "M10b",
    "extensions": [
      { "finding_id": 18414,
        "verse_ref": "Hos 10:13",        # idempotency guard: skip if already in text
        "anchor": "<unique existing substring>",   # must occur exactly once
        "insert_text": "<faithful exemplar sentence, leading space>",
        "reason": "<evaluation>" } ] }

For each item: spliced immediately AFTER `anchor`. Guards: verse_ref must NOT already
be present (else skip, idempotent); anchor must occur exactly once (else ABORT); the
finished text must contain verse_ref (else ABORT). last_updated_date stamped.

DEFAULT DRY-RUN. --file PATH required. --apply to write.
"""
import argparse, json, sqlite3
from datetime import datetime, timezone

DB = "database/bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    d = json.load(open(a.file, encoding="utf-8"))
    items = d["extensions"]
    c = sqlite3.connect(DB, timeout=30)
    c.row_factory = sqlite3.Row
    cur = c.cursor()
    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: cluster={d.get('cluster')} extensions={len(items)}")

    plan = []  # (item, old_text, new_text, action)
    for it in items:
        fid = it["finding_id"]
        row = cur.execute("SELECT id, finding_text FROM cluster_finding WHERE id=?", (fid,)).fetchone()
        if row is None:
            raise SystemExit(f"ABORT: finding {fid} not found")
        txt = row["finding_text"]
        ref, anchor, ins = it["verse_ref"], it["anchor"], it["insert_text"]
        if ref in txt:
            plan.append((it, txt, txt, "SKIP (verse already cited)"))
            continue
        n = txt.count(anchor)
        if n != 1:
            raise SystemExit(f"ABORT: finding {fid} anchor occurs {n}x (need exactly 1): {anchor[:60]!r}")
        new = txt.replace(anchor, anchor + ins)
        if ref not in new:
            raise SystemExit(f"ABORT: finding {fid} insert did not introduce verse_ref {ref!r}")
        plan.append((it, txt, new, "EXTEND"))

    for it, old, new, action in plan:
        print(f"\n  finding {it['finding_id']} [{it['verse_ref']}] -> {action}")
        if action == "EXTEND":
            print(f"    + {it['insert_text'].strip()}")

    if not a.apply:
        c.close()
        return

    cur.execute("BEGIN")
    try:
        n = 0; expected = 0
        for it, old, new, action in plan:
            if action != "EXTEND":
                continue
            expected += 1
            cur.execute(
                "UPDATE cluster_finding SET finding_text=?, last_updated_date=? WHERE id=?",
                (new, NOW, it["finding_id"]))
            n += cur.rowcount
        if n != expected:
            c.rollback(); raise SystemExit(f"ABORT: wrote {n}!=expected {expected}")
        c.commit()
    except Exception:
        c.rollback(); raise
    print(f"\nAPPLIED: {n} finding(s) extended. Re-run the citation extractor (--cluster "
          f"{d.get('cluster')} --live) then re-audit to flip B7.")
    c.close()


if __name__ == "__main__":
    main()
