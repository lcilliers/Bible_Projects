"""_apply_persist_narration_finding_v1.py (2026-06-15) — persist the templated narration as the single
`l2_meaning` finding per term-in-verse (researcher decision: narration is a FINDING, not a ve_lexical row).

The narration is the deterministic view (01b §1f) composed from ve_lexical (+ mode column). It replaces the
old NARRATED-PROSE l2_meaning findings (the un-traceable prose this reform deprecates): those are
soft-deleted and linked via `supersedes_id`. Scope = M-cluster units (T2 excluded from standalone meaning).

Reversible: new rows carry source_legacy_ref='ve-narration-v1-20260615' (deletable); old l2_meaning are
soft-deleted (delete_flagged=1), restorable.

  python scripts/_apply_persist_narration_finding_v1.py --dry-run
  python scripts/_apply_persist_narration_finding_v1.py --live
"""
import argparse, os, sqlite3, sys, importlib.util
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "ve-narration-v1-20260615"
CREATED = "2026-06-15T00:00:00Z"

spec = importlib.util.spec_from_file_location("nar", os.path.join(os.path.dirname(__file__), "_produce_ve_narration_v1.py"))
nar = importlib.util.module_from_spec(spec); spec.loader.exec_module(nar)


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=600); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # M-cluster units (T2 excluded from standalone meaning)
    units = cur.execute("""
        SELECT vc.id vcid, vc.mti_term_id mti, m.cluster_code cc,
               vr.reference ref, vr.transliteration translit, m.gloss gloss, vr.morph_code morph, vr.stem stem
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
        JOIN mti_terms m ON m.id = vc.mti_term_id
        WHERE COALESCE(vc.delete_flagged,0)=0 AND m.cluster_code IS NOT NULL AND m.cluster_code <> 'T2'
    """).fetchall()

    # ve_lexical grouped per unit
    lexmap = {}
    for r in cur.execute("SELECT verse_context_id v, ve_nr, value FROM ve_lexical WHERE COALESCE(delete_flagged,0)=0 ORDER BY ve_nr, id"):
        lexmap.setdefault(r["v"], {}).setdefault(r["ve_nr"], []).append(r["value"])

    # old active l2_meaning per verse_context (to supersede + soft-delete)
    old = {r["verse_context_id"]: r["id"] for r in cur.execute(
        "SELECT id, verse_context_id FROM finding WHERE provenance='l2_meaning' AND COALESCE(delete_flagged,0)=0")}

    inserts = []
    for u in units:
        lex = lexmap.get(u["vcid"], {})
        text = nar.narrate(dict(u), lex)
        inserts.append((u["vcid"], u["mti"], u["cc"], text, old.get(u["vcid"])))
    superseded = sum(1 for x in inserts if x[4] is not None)
    old_to_delete = len(old)

    print(f"M-cluster units                 : {len(units):,}")
    print(f"narration findings to insert    : {len(inserts):,}")
    print(f"  of which supersede an old one : {superseded:,}")
    print(f"old active l2_meaning to soft-del: {old_to_delete:,}")
    print(f"sample: {inserts[0][3][:160]}")

    if a.live:
        cur.execute("UPDATE finding SET delete_flagged=1, last_updated_date=? WHERE provenance='l2_meaning' AND COALESCE(delete_flagged,0)=0", (CREATED,))
        nd = cur.rowcount
        cur.executemany(
            "INSERT INTO finding (level, verse_context_id, mti_term_id, cluster_code, finding_value, finding_status, "
            "provenance, supersedes_id, source_legacy_ref, created_at, last_updated_date, delete_flagged) "
            "VALUES ('VERSE', ?, ?, ?, ?, 'ANSWERED', 'l2_meaning', ?, ?, ?, ?, 0)",
            [(vc, mti, cc, text, sup, STAMP, CREATED, CREATED) for (vc, mti, cc, text, sup) in inserts])
        conn.commit()
        n_new = cur.execute("SELECT COUNT(*) FROM finding WHERE source_legacy_ref=? AND COALESCE(delete_flagged,0)=0", (STAMP,)).fetchone()[0]
        print(f"\nLIVE: soft-deleted {nd:,} old l2_meaning · inserted {len(inserts):,} narration findings ({n_new:,} active with stamp)")
    else:
        print("\nDRY-RUN — no writes.")


if __name__ == "__main__":
    main()
