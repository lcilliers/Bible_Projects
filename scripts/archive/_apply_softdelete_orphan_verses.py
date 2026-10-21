"""_apply_softdelete_orphan_verses.py — D2b option A (2026-06-15): soft-delete ACTIVE verses that are
orphans of an already-deleted term — i.e. mti_term_id IS NULL and term_id matches NO live mti_terms row
(its canonical term was soft-deleted / delete-marked in a prior pass). These are missing soft-deletes;
the verses should follow their term. Cascades to verse_context + findings. Reversible via sidecar JSON.

  python scripts/_apply_softdelete_orphan_verses.py --dry-run --out <f>.md
  python scripts/_apply_softdelete_orphan_verses.py --live    --out <f>.md   # writes <f>.ids.json
  python scripts/_apply_softdelete_orphan_verses.py --reverse <f>.ids.json
"""
import argparse, json, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")


def _ph(ids):
    return ",".join("?" * len(ids))


def collect(cur):
    vr = [r[0] for r in cur.execute("""
        SELECT vr.id FROM wa_verse_records vr
        WHERE COALESCE(vr.delete_flagged,0)=0 AND vr.mti_term_id IS NULL AND vr.term_id IS NOT NULL
          AND NOT EXISTS (SELECT 1 FROM mti_terms m WHERE m.strongs_number=vr.term_id
                            AND COALESCE(m.delete_flagged,0)=0 AND COALESCE(m.status,'')<>'delete')""")]
    vc, fnd = [], []
    if vr:
        for i in range(0, len(vr), 400):
            ch = vr[i:i + 400]
            vc += [r[0] for r in cur.execute(
                f"SELECT id FROM verse_context WHERE verse_record_id IN ({_ph(ch)}) AND COALESCE(delete_flagged,0)=0", ch)]
    if vc:
        for i in range(0, len(vc), 400):
            ch = vc[i:i + 400]
            fnd += [r[0] for r in cur.execute(
                f"SELECT id FROM finding WHERE verse_context_id IN ({_ph(ch)}) AND COALESCE(delete_flagged,0)=0", ch)]
    return {"wa_verse_records": vr, "verse_context": vc, "finding": fnd}


def flag(conn, sets, value):
    cur = conn.cursor(); n = 0
    for t, ids in sets.items():
        for i in range(0, len(ids), 400):
            ch = ids[i:i + 400]
            cur.execute(f"UPDATE {t} SET delete_flagged=? WHERE id IN ({_ph(ch)})", [value] + ch)
            n += cur.rowcount
    conn.commit(); return n


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    g.add_argument("--reverse", metavar="IDS_JSON")
    ap.add_argument("--out")
    a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=120); conn.row_factory = sqlite3.Row
    if a.reverse:
        print("REVERSED:", flag(conn, json.load(open(a.reverse, encoding="utf-8")), 0), "rows"); return
    sets = collect(conn.cursor())
    L = [f"# D2b-A — soft-delete orphan verses ({'DRY-RUN' if a.dry_run else 'LIVE'})", "",
         f"- wa_verse_records: {len(sets['wa_verse_records'])}",
         f"- verse_context: {len(sets['verse_context'])}",
         f"- finding: {len(sets['finding'])}"]
    print("\n".join(L[2:]))
    if a.live:
        n = flag(conn, sets, 1)
        ids = (a.out or "d2b") + ".ids.json"; json.dump(sets, open(ids, "w", encoding="utf-8"))
        L.append(f"\n**LIVE: soft-deleted {n} rows.** Reversal → `{ids}`."); print(f"LIVE: {n} rows; reversal → {ids}")
    else:
        L.append("\n**DRY-RUN — no writes.**")
    if a.out:
        os.makedirs(os.path.dirname(a.out), exist_ok=True); open(a.out, "w", encoding="utf-8").write("\n".join(L))


if __name__ == "__main__":
    main()
