"""_apply_excluded_registry_cascade.py — D1 rule (2026-06-15): when a registry is phase1_status='Excluded',
its ENTIRE downstream is soft-deleted (delete_flagged=1), not just filtered out — verses, term_inventory,
owned mti_terms, verse_context, findings.

Reversible + auditable: --live records every touched row id to a sidecar JSON; --reverse <json> undoes
exactly those ids. Only ever flips rows currently delete_flagged=0 (so reversal can't un-delete pre-existing
soft-deletes). Verified safe: excluded-owned mti_terms have 0 active references from non-excluded registries.

  python scripts/_apply_excluded_registry_cascade.py --dry-run --out <file>.md
  python scripts/_apply_excluded_registry_cascade.py --live    --out <file>.md      # also writes <file>.ids.json
  python scripts/_apply_excluded_registry_cascade.py --reverse <file>.ids.json
"""
import argparse, json, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
TABLES = ["wa_verse_records", "wa_term_inventory", "mti_terms", "verse_context", "finding"]


def _ph(ids):
    return ",".join("?" * len(ids))


def collect(cur):
    """Return (excluded_registry_ids, {table: [active row ids to soft-delete]})."""
    exc = [r[0] for r in cur.execute("SELECT id FROM word_registry WHERE phase1_status='Excluded'")]
    sets = {t: [] for t in TABLES}
    if not exc:
        return exc, sets
    eph = _ph(exc)
    fids = [r[0] for r in cur.execute(f"SELECT id FROM wa_file_index WHERE registry_id IN ({eph})", exc)]
    mti = [r[0] for r in cur.execute(
        f"SELECT id FROM mti_terms WHERE owning_registry_fk IN ({eph}) AND COALESCE(delete_flagged,0)=0", exc)]
    sets["mti_terms"] = mti
    if fids:
        fph = _ph(fids)
        sets["wa_verse_records"] = [r[0] for r in cur.execute(
            f"SELECT id FROM wa_verse_records WHERE file_id IN ({fph}) AND COALESCE(delete_flagged,0)=0", fids)]
        sets["wa_term_inventory"] = [r[0] for r in cur.execute(
            f"SELECT id FROM wa_term_inventory WHERE file_id IN ({fph}) AND COALESCE(delete_flagged,0)=0", fids)]
    # verse_context tied to the excluded verses OR the excluded-owned terms
    vc = set()
    if sets["wa_verse_records"]:
        vr = sets["wa_verse_records"]
        vc |= {r[0] for r in cur.execute(
            f"SELECT id FROM verse_context WHERE verse_record_id IN ({_ph(vr)}) AND COALESCE(delete_flagged,0)=0", vr)}
    if mti:
        vc |= {r[0] for r in cur.execute(
            f"SELECT id FROM verse_context WHERE mti_term_id IN ({_ph(mti)}) AND COALESCE(delete_flagged,0)=0", mti)}
    sets["verse_context"] = sorted(vc)
    # findings tied to the excluded-owned terms OR the excluded verse_context
    fnd = set()
    if mti:
        fnd |= {r[0] for r in cur.execute(
            f"SELECT id FROM finding WHERE mti_term_id IN ({_ph(mti)}) AND COALESCE(delete_flagged,0)=0", mti)}
    if sets["verse_context"]:
        vcl = sets["verse_context"]
        fnd |= {r[0] for r in cur.execute(
            f"SELECT id FROM finding WHERE verse_context_id IN ({_ph(vcl)}) AND COALESCE(delete_flagged,0)=0", vcl)}
    sets["finding"] = sorted(fnd)
    return exc, sets


def apply_flag(conn, sets, value):
    cur = conn.cursor()
    n = 0
    for t, ids in sets.items():
        for i in range(0, len(ids), 400):
            chunk = ids[i:i + 400]
            cur.execute(f"UPDATE {t} SET delete_flagged=? WHERE id IN ({_ph(chunk)})", [value] + chunk)
            n += cur.rowcount
    conn.commit()
    return n


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--live", action="store_true")
    g.add_argument("--reverse", metavar="IDS_JSON")
    ap.add_argument("--out")
    a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=60)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    if a.reverse:
        sets = json.load(open(a.reverse, encoding="utf-8"))
        n = apply_flag(conn, sets, 0)
        print(f"REVERSED: un-soft-deleted {n} rows from {a.reverse}")
        return

    exc, sets = collect(cur)
    L = [f"# D1 — excluded-registry cascade soft-delete ({'DRY-RUN' if a.dry_run else 'LIVE'})", "",
         f"Excluded registries: {len(exc)}.  Soft-deletes (active rows only):", "",
         "| table | rows |", "|---|---|"]
    for t in TABLES:
        L.append(f"| {t} | {len(sets[t])} |")
    total = sum(len(v) for v in sets.values())
    L.append(f"| **total** | **{total}** |")
    print("\n".join(L[3:]))

    if a.live:
        n = apply_flag(conn, sets, 1)
        ids_path = (a.out or "d1") + ".ids.json"
        json.dump(sets, open(ids_path, "w", encoding="utf-8"))
        L.append(f"\n**LIVE: soft-deleted {n} rows.** Reversal set recorded → `{ids_path}` (`--reverse` to undo).")
        print(f"LIVE: soft-deleted {n} rows; reversal ids → {ids_path}")
    else:
        L.append("\n**DRY-RUN — no writes.**")
    if a.out:
        os.makedirs(os.path.dirname(a.out), exist_ok=True)
        open(a.out, "w", encoding="utf-8").write("\n".join(L))
        print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
