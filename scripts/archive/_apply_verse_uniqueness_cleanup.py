"""_apply_verse_uniqueness_cleanup.py (2026-06-15) — move wa_verse_records toward "one active row per
(reference, term_id)". Two deterministic, safe sweeps (cascaded soft-delete → verse_context → findings):
  (A) ORPHANS  — active verses whose mti_term is soft-deleted (term gone; pre-existing cruft).
  (B) XREF-DUPS — the XREF copy in a (reference, term_id) pair that also has an active OWNER copy
                  (keep the OWNER; drop the XREF).
Leaves the sole-copy XREF verses (owner-missing) UNTOUCHED — those need the owner re-derivation, not deletion.
Reversible via sidecar JSON.

  python scripts/_apply_verse_uniqueness_cleanup.py --dry-run --out <f>.md
  python scripts/_apply_verse_uniqueness_cleanup.py --live    --out <f>.md
  python scripts/_apply_verse_uniqueness_cleanup.py --reverse <f>.ids.json
"""
import argparse, json, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")


def _ph(ids):
    return ",".join("?" * len(ids))


def _flag(cur, table, ids, val):
    nn = 0
    for i in range(0, len(ids), 400):
        ch = ids[i:i + 400]
        cur.execute(f"UPDATE {table} SET delete_flagged=? WHERE id IN ({_ph(ch)})", [val] + ch)
        nn += cur.rowcount
    return nn


def collect(cur):
    # (A) orphan verses — mti_term soft-deleted
    orphans = [r[0] for r in cur.execute(
        "SELECT vr.id FROM wa_verse_records vr WHERE COALESCE(vr.delete_flagged,0)=0 "
        "AND vr.mti_term_id IN (SELECT id FROM mti_terms WHERE delete_flagged=1)")]
    # (B) XREF-dup verses — XREF copy where an active OWNER copy exists for the same (reference, term_id)
    dups = cur.execute("""SELECT reference, term_id FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0
        GROUP BY reference, term_id HAVING COUNT(*)>1""").fetchall()
    xref_drop = []
    for d in dups:
        rows = cur.execute("""SELECT vr.id, ti.term_owner_type ot FROM wa_verse_records vr
            JOIN wa_term_inventory ti ON ti.id=vr.term_inv_id
            WHERE COALESCE(vr.delete_flagged,0)=0 AND vr.reference=? AND vr.term_id=?""", (d["reference"], d["term_id"])).fetchall()
        ots = [r["ot"] for r in rows]
        if ots.count("OWNER") == 1 and ots.count("XREF") == (len(ots) - 1) and len(ots) > 1:
            xref_drop += [r["id"] for r in rows if r["ot"] == "XREF"]
        # else: ambiguous (e.g. no OWNER, or >1 OWNER) — leave for the owner re-derivation
    verses = sorted(set(orphans) | set(xref_drop))
    # cascade downstream
    vc, fnd = [], []
    for i in range(0, len(verses), 400):
        ch = verses[i:i + 400]
        vc += [r[0] for r in cur.execute(f"SELECT id FROM verse_context WHERE verse_record_id IN ({_ph(ch)}) AND COALESCE(delete_flagged,0)=0", ch)]
        fnd += [r[0] for r in cur.execute(f"SELECT id FROM finding WHERE verse_context_id IN (SELECT id FROM verse_context WHERE verse_record_id IN ({_ph(ch)})) AND COALESCE(delete_flagged,0)=0", ch)]
    return {"orphans": orphans, "xref_drop": xref_drop,
            "sets": {"wa_verse_records": verses, "verse_context": sorted(set(vc)), "finding": sorted(set(fnd))}}


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
        print("REVERSED:", sum(_flag(cur, t, ids, 0) for t, ids in d.items()), "rows"); conn.commit(); return
    info = collect(cur); sets = info["sets"]
    print(f"(A) orphan verses: {len(info['orphans'])}  ·  (B) XREF-dup copies to drop: {len(info['xref_drop'])}")
    print(f"cascade total: verses {len(sets['wa_verse_records'])} · verse_context {len(sets['verse_context'])} · findings {len(sets['finding'])}")
    if a.live:
        tot = sum(_flag(cur, t, ids, 1) for t, ids in sets.items()); conn.commit()
        ids_path = (a.out or "x") + ".ids.json"; json.dump(sets, open(ids_path, "w", encoding="utf-8"))
        print(f"LIVE: soft-deleted {tot} rows; reversal -> {ids_path}")
    else:
        print("DRY-RUN — no writes.")


if __name__ == "__main__":
    main()
