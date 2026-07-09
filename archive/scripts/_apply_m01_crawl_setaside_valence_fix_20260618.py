"""_apply_m01_crawl_setaside_valence_fix_20260618.py — researcher-directed corrections (2026-06-18):
  (1) SET ASIDE H2119B from M01 — both M01 occurrences (Mic 7:17 'crawling', Deu 32:24 'crawl') are the
      serpent/crawl homonym, not fear. Remove the term from M01 (cluster_code->NULL), mark set_aside_reason,
      dispose its lexical + narration. Persists across reruns (engine skips cluster_code IS NULL).
  (2) CORRECT valence: Jos 4:14 + 1Ki 3:28 'stood in awe' of a human leader: righteous -> neutral
      (kept as valence_read_api so the base rerun preserves it).
Reversible. Run: python scripts/_apply_m01_crawl_setaside_valence_fix_20260618.py --live|--dry-run
"""
import argparse, sqlite3, os, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
CRAWL_VCIDS = (17236, 64479)          # H2119B in M01 (Mic 7:17, Deu 32:24)
VALENCE_FIX = {4264: "Jos 4:14", 4266: "1Ki 3:28"}   # 'stood in awe' of human leader -> neutral
REASON = "homonym: 'crawl/crawling' = the serpent crawling (Mic 7:17, Deu 32:24), not fear — set aside from M01 [researcher 2026-06-18]"


def main():
    g = argparse.ArgumentParser(); m = g.add_mutually_exclusive_group(required=True)
    m.add_argument("--live", action="store_true"); m.add_argument("--dry-run", action="store_true")
    a = g.parse_args()
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row; cur = c.cursor()
    print("(1) SET ASIDE H2119B from M01")
    before = cur.execute("SELECT id, cluster_code FROM mti_terms WHERE strongs_number='H2119B'").fetchall()
    print("    mti_terms H2119B:", [dict(r) for r in before])
    lex = cur.execute(f"SELECT COUNT(*) FROM ve_lexical WHERE verse_context_id IN {CRAWL_VCIDS} AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    nar = cur.execute(f"SELECT COUNT(*) FROM finding WHERE verse_context_id IN {CRAWL_VCIDS} AND provenance='l2_meaning' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    print(f"    will: cluster_code->NULL · set_aside_reason on {len(CRAWL_VCIDS)} units · soft-delete {lex} ve_lexical + {nar} narration")
    print("(2) CORRECT valence -> neutral:")
    for vcid, ref in VALENCE_FIX.items():
        cur_val = cur.execute("SELECT value FROM ve_lexical WHERE verse_context_id=? AND ve_label='valence' AND COALESCE(delete_flagged,0)=0", (vcid,)).fetchone()
        print(f"    {ref} (vcid={vcid}): {cur_val['value'] if cur_val else None} -> neutral")
    if a.dry_run:
        print("DRY-RUN — no changes."); return
    cur.execute("UPDATE mti_terms SET cluster_code=NULL WHERE strongs_number='H2119B'")
    cur.execute(f"UPDATE verse_context SET set_aside_reason=? WHERE id IN {CRAWL_VCIDS}", (REASON,))
    cur.execute(f"UPDATE ve_lexical SET delete_flagged=1, notes='set aside: crawl homonym' WHERE verse_context_id IN {CRAWL_VCIDS} AND COALESCE(delete_flagged,0)=0")
    cur.execute(f"UPDATE finding SET delete_flagged=1, last_updated_date='2026-06-18T00:00:00Z' WHERE verse_context_id IN {CRAWL_VCIDS} AND provenance='l2_meaning' AND COALESCE(delete_flagged,0)=0")
    for vcid in VALENCE_FIX:
        cur.execute("UPDATE ve_lexical SET value='neutral', notes='researcher correction: reverence of a human leader, not Godward' "
                    "WHERE verse_context_id=? AND ve_label='valence' AND COALESCE(delete_flagged,0)=0", (vcid,))
    c.commit()
    print("LIVE: applied.")


if __name__ == "__main__":
    main()
