"""_apply_language_reconcile.py — make mti_terms.language / wa_term_inventory.language
MORPH-AUTHORITATIVE. The morph code is the linguistic fact; the Strong's prefix (used at
step_client.py:200 and audit_word.py:778) is blind to Aramaic. This reconciles language from the
morph for every term that appears in the text, and LEAVES morph-less (text-less) terms untouched
(their Aramaic-vs-Hebrew status needs the STEP lexicon tag, not a guess — flagged separately).

Idempotent + self-healing. `reconcile_language(conn)` is imported by `_apply_morph_backfill.py` and
runs after every live morph write, so the fix follows the morph (its source) and never reverts.
Run standalone for a one-time / on-demand reconciliation:

  python scripts/_apply_language_reconcile.py --dry-run
  python scripts/_apply_language_reconcile.py --live
"""
import argparse, os, sqlite3, sys
from collections import defaultdict
sys.path.insert(0, os.path.join("scripts", "analytics"))
sys.stdout.reconfigure(encoding="utf-8")
from morph_util import term_language
DB = os.path.join("database", "bible_research.db")


def reconcile_language(conn, registry_id=None, dry_run=False):
    """Set mti_terms.language + wa_term_inventory.language from the dominant morph of each term's
    active occurrences. Only touches morph-bearing terms (text-less terms are left as-is).
    Returns a list of (strongs, old, new) changes. If registry_id is given, limit to that registry's terms."""
    cur = conn.cursor()
    where = "AND m.owning_registry_fk = ?" if registry_id is not None else ""
    params = (registry_id,) if registry_id is not None else ()
    rows = cur.execute(
        f"""SELECT m.id, m.strongs_number sn, m.language lang, vr.morph_code mc
            FROM mti_terms m JOIN wa_verse_records vr ON vr.mti_term_id = m.id
            WHERE COALESCE(vr.delete_flagged,0)=0 AND COALESCE(m.delete_flagged,0)=0
              AND vr.morph_code IS NOT NULL AND vr.morph_code != '' {where}""",
        params,
    ).fetchall()

    morphs = defaultdict(list)
    meta = {}
    for r in rows:
        morphs[r["id"]].append(r["mc"])
        meta[r["id"]] = (r["sn"], r["lang"])

    changes = []
    for tid, codes in morphs.items():
        sn, old = meta[tid]
        new = term_language(codes)
        if new and new != old:
            changes.append((sn, old, new))
            if not dry_run:
                cur.execute("UPDATE mti_terms SET language = ? WHERE id = ?", (new, tid))
                cur.execute(
                    "UPDATE wa_term_inventory SET language = ? "
                    "WHERE strongs_number = ? AND COALESCE(delete_flagged,0)=0",
                    (new, sn),
                )
    if not dry_run:
        conn.commit()
    return changes


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=60)
    conn.row_factory = sqlite3.Row
    changes = reconcile_language(conn, dry_run=a.dry_run)
    from collections import Counter
    by = Counter((o, n) for _, o, n in changes)
    print(f"{'DRY-RUN' if a.dry_run else 'LIVE'} — terms whose language changes: {len(changes)}")
    for (o, n), c in by.most_common():
        print(f"  {o} -> {n}: {c}")
    print("  sample:", [c[0] for c in changes[:12]])


if __name__ == "__main__":
    main()
