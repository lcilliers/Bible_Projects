"""_apply_softdelete_excluded_empty_terms.py (2026-06-15) — ground the canonical term list:
soft-delete (the CONCEPT — term + its whole downstream) every active mti_terms row that is
  (a) status='excluded', OR
  (b) has 0 active verses (an empty canonical row — incl. the orphan duplicate copies),
and cascade to its verse_records -> verse_context -> findings. Reversible via sidecar JSON.

  python scripts/_apply_softdelete_excluded_empty_terms.py --dry-run --out <f>.md
  python scripts/_apply_softdelete_excluded_empty_terms.py --live    --out <f>.md   # writes <f>.ids.json
  python scripts/_apply_softdelete_excluded_empty_terms.py --reverse <f>.ids.json
"""
import argparse, json, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")


def _ph(ids):
    return ",".join("?" * len(ids))


def _flag(cur, table, ids, val):
    n = 0
    for i in range(0, len(ids), 400):
        ch = ids[i:i + 400]
        cur.execute(f"UPDATE {table} SET delete_flagged=? WHERE id IN ({_ph(ch)})", [val] + ch)
        n += cur.rowcount
    return n


def collect(cur):
    # the term set: active mti_terms that are excluded OR have no active verse
    terms = [r[0] for r in cur.execute("""
        SELECT m.id FROM mti_terms m
        WHERE COALESCE(m.delete_flagged,0)=0
          AND (m.status='excluded'
               OR NOT EXISTS (SELECT 1 FROM wa_verse_records vr
                              WHERE vr.mti_term_id=m.id AND COALESCE(vr.delete_flagged,0)=0))""")]
    # downstream of those terms (active only)
    vr, vc, fnd = [], [], []
    for i in range(0, len(terms), 400):
        ch = terms[i:i + 400]
        vr += [r[0] for r in cur.execute(f"SELECT id FROM wa_verse_records WHERE mti_term_id IN ({_ph(ch)}) AND COALESCE(delete_flagged,0)=0", ch)]
        fnd += [r[0] for r in cur.execute(f"SELECT id FROM finding WHERE mti_term_id IN ({_ph(ch)}) AND COALESCE(delete_flagged,0)=0", ch)]
    for i in range(0, len(vr), 400):
        ch = vr[i:i + 400]
        vc += [r[0] for r in cur.execute(f"SELECT id FROM verse_context WHERE verse_record_id IN ({_ph(ch)}) AND COALESCE(delete_flagged,0)=0", ch)]
    for i in range(0, len(vc), 400):
        ch = vc[i:i + 400]
        fnd += [r[0] for r in cur.execute(f"SELECT id FROM finding WHERE verse_context_id IN ({_ph(ch)}) AND COALESCE(delete_flagged,0)=0", ch)]
    return {"mti_terms": terms, "wa_verse_records": vr, "verse_context": sorted(set(vc)), "finding": sorted(set(fnd))}


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    g.add_argument("--reverse", metavar="IDS_JSON")
    ap.add_argument("--out")
    a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=120); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    if a.reverse:
        d = json.load(open(a.reverse, encoding="utf-8"))
        n = sum(_flag(cur, t, ids, 0) for t, ids in d.items()); conn.commit()
        print(f"REVERSED: restored {n} rows"); return

    sets = collect(cur)
    # breakdown of the term set
    ts = sets["mti_terms"]
    exc = cur.execute(f"SELECT COUNT(*) FROM mti_terms WHERE id IN ({_ph(ts)}) AND status='excluded'", ts).fetchone()[0] if ts else 0
    print(f"term set: {len(ts)}  (excluded={exc}, of which/also 0-active-verse)")
    print(f"cascade: wa_verse_records {len(sets['wa_verse_records'])} · verse_context {len(sets['verse_context'])} · finding {len(sets['finding'])}")
    if a.live:
        tot = sum(_flag(cur, t, ids, 1) for t, ids in sets.items()); conn.commit()
        ids_path = (a.out or "x") + ".ids.json"; json.dump(sets, open(ids_path, "w", encoding="utf-8"))
        print(f"LIVE: soft-deleted {tot} rows; reversal -> {ids_path}")
    else:
        print("DRY-RUN — no writes.")


if __name__ == "__main__":
    main()
