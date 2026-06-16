"""_apply_cause_from_api.py (2026-06-16) — apply the cause-resolution API output back into ve_lexical.

Input: the API's JSON array [{"vcid": <int>, "cause": "<phrase>" | "NONE"}].
For each: a real cause REPLACES the 'pending-read' candidate (provenance -> cause_read_api); "NONE" means
the verse states no cause -> the 'pending-read' candidate is SOFT-deleted (cause becomes NONE). The
cause_clause hint is left in place for audit. Reversible (pending-read rows are soft-deleted, not lost).

  python scripts/_apply_cause_from_api.py --input api-output.json --dry-run
  python scripts/_apply_cause_from_api.py --input api-output.json --live
"""
import argparse, json, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "2026-06-16T00:00:00Z"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    data = json.load(open(a.input, encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("items") or data.get("results") or data.get("data") or []
    conn = sqlite3.connect(DB, timeout=600); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    resolved = none = missing = 0
    for it in data:
        vcid = it.get("vcid"); cause = (it.get("cause") or "").strip()
        row = cur.execute("SELECT id FROM ve_lexical WHERE verse_context_id=? AND ve_label='cause' "
                          "AND value='pending-read' AND COALESCE(delete_flagged,0)=0", (vcid,)).fetchone()
        if not row:
            missing += 1; continue
        if cause and cause.upper() != "NONE":
            resolved += 1
            if a.live:
                cur.execute("UPDATE ve_lexical SET value=?, source_provenance='cause_read_api', "
                            "notes='resolved by cause read pass', created_at=? WHERE id=?", (cause[:140], STAMP, row["id"]))
        else:
            none += 1
            if a.live:   # NONE marker must carry a *_read_api provenance so it SURVIVES engine rebuilds
                cur.execute("UPDATE ve_lexical SET delete_flagged=1, notes='read pass: NONE', source_provenance='cause_read_api' WHERE id=?", (row["id"],))
    if a.live:
        conn.commit()
    print(f"{'LIVE' if a.live else 'DRY-RUN'}: {len(data):,} API results · resolved {resolved:,} · NONE {none:,} · "
          f"no-pending-row {missing:,}")
    if a.dry_run:
        print("  (no writes — re-run with --live to apply)")


if __name__ == "__main__":
    main()
