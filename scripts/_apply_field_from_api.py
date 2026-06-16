"""_apply_field_from_api.py (2026-06-16) — apply a field read API output back into ve_lexical.
Input: [{"vcid":int, "value":"<value>"|"NONE"}]. Marks rows source_provenance='<field>_read_api' so they
survive engine rebuilds (the generator preserves any *_read_api field). Reversible.

  python scripts/_apply_field_from_api.py --field location --input out.json --dry-run|--live
"""
import argparse, json, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "2026-06-16T00:00:00Z"
# field: (mode, ve_nr, related_tier, match-on-existing-row)
CFG = {
    "location": ("update", 5, "T2", "ve_label='location' AND value='UNRESOLVED'"),
    "divine-involvement": ("update", 8, "T0.1.2", "ve_label='divine-involvement'"),
    "object-type": ("update", 16, "T1.1.4", "ve_label='object-type' AND value='thing/abstract'"),
    "valence": ("insert", 21, "T0.3.1", "ve_label='valence'"),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--field", required=True, choices=list(CFG))
    ap.add_argument("--input", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    mode, ve_nr, tier, match = CFG[a.field]
    prov = a.field.replace("-", "_") + "_read_api"
    data = json.load(open(a.input, encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("items") or data.get("results") or data.get("data") or []
    conn = sqlite3.connect(DB, timeout=600); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    setv = none = miss = 0
    for it in data:
        vcid = it.get("vcid"); val = (it.get("value") or "").strip()
        is_none = (not val) or val.upper() == "NONE"
        if mode == "update":
            row = cur.execute(f"SELECT id FROM ve_lexical WHERE verse_context_id=? AND {match} "
                              "AND COALESCE(delete_flagged,0)=0 LIMIT 1", (vcid,)).fetchone()
            if not row:
                miss += 1; continue
            if is_none:
                none += 1
                if a.live:
                    cur.execute("UPDATE ve_lexical SET delete_flagged=1, notes='read pass: NONE', source_provenance=? WHERE id=?", (prov, row["id"]))
            else:
                setv += 1
                if a.live:
                    cur.execute("UPDATE ve_lexical SET value=?, source_provenance=?, notes='resolved by read pass', created_at=? WHERE id=?",
                                (val[:140], prov, STAMP, row["id"]))
        else:  # insert (valence): add a row, or a soft-deleted NONE marker (so rebuild skips the mechanical field)
            if is_none:
                none += 1
                if a.live:
                    cur.execute("INSERT INTO ve_lexical (verse_context_id, ve_nr, ve_label, related_tier, value, notes, source_provenance, delete_flagged, created_at) "
                                "VALUES (?,?,?,?,?, 'read pass: NONE', ?, 1, ?)", (vcid, ve_nr, a.field, tier, "NONE", prov, STAMP))
            else:
                setv += 1
                if a.live:
                    cur.execute("INSERT INTO ve_lexical (verse_context_id, ve_nr, ve_label, related_tier, value, notes, source_provenance, delete_flagged, created_at) "
                                "VALUES (?,?,?,?,?, 'resolved by read pass', ?, 0, ?)", (vcid, ve_nr, a.field, tier, val[:140], prov, STAMP))
    if a.live:
        conn.commit()
    print(f"{'LIVE' if a.live else 'DRY-RUN'} [{a.field}]: {len(data):,} results · set {setv:,} · NONE {none:,} · no-row {miss:,}")


if __name__ == "__main__":
    main()
