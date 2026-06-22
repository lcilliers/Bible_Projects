"""_apply_truncation_recover_term_20260622.py — recover cap-truncated verses for a confirmed term.

Generalises the H7563 repair to any sweep-confirmed truncation term. Adds ONLY the truncation-tail
absent verses (STEP refs beyond the DB's chapter-reach in their book — the contiguous tail the old
client never pulled); within-range absent verses (possible span-filter) are EXCLUDED and reported.
Per-term template constants are read from an existing active row (file_id, term_inv_id, registry).
Adds 1 active wa_verse_records + verse_context shell per recovered ref (fits the resolved 1-active-per-ref
pattern; creates no new duplicates). verse_id left NULL -> set by _apply_ingest_verse_morphology.py.

  python scripts/_apply_truncation_recover_term_20260622.py --strong H5315G --mti 1381 --dry-run|--live
"""
import argparse, os, re, sqlite3, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "analytics"))
from step_client import StepClient
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "2026-06-22T00:00:00Z"


def ch_of(ref):
    m = re.match(r"\S+\s+(\d+):", ref); return int(m.group(1)) if m else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strong", required=True)
    ap.add_argument("--mti", type=int, required=True)
    ap.add_argument("--full", action="store_true",
                    help="recover ALL absent occurrences (not just the truncation-tail) — needed so the "
                         "term is picked up as a CO-TERM in other clusters' verse fan-outs")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    ap.add_argument("--vcids-out", default="outputs/_tmp_recover_vcids.txt")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # map by the reference-prefix actually used in the corpus (e.g. 'Song'), not books.short_code ('Son'),
    # then fall back to short_code for any prefix not yet present.
    bmap = {r["short_code"]: r["id"] for r in cur.execute("SELECT id, short_code FROM books")}
    for r in cur.execute("SELECT DISTINCT reference, book_id FROM wa_verse_records WHERE book_id IS NOT NULL AND reference LIKE '% %'"):
        bmap.setdefault(r["reference"].split(" ")[0], r["book_id"])

    # template from an existing active row for this mti_term
    tpl = cur.execute("""SELECT file_id, term_inv_id, term_id, transliteration, testament, translation, word_registry_fk
        FROM wa_verse_records WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0 LIMIT 1""", (a.mti,)).fetchone()
    if not tpl:
        print("no template row for mti", a.mti); return 2
    tpl = dict(tpl)
    print(f"template: {tpl}")

    sc = StepClient()
    step = {r["ref"]: r for r in sc.get_verse_records(a.strong)}
    active = {r["reference"] for r in cur.execute(
        "SELECT DISTINCT reference FROM wa_verse_records WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (a.mti,))}
    dbmax = {}
    for ref in active:
        b = ref.split()[0]; dbmax[b] = max(dbmax.get(b, 0), ch_of(ref))
    tail, within = [], []
    for ref in step:
        if ref in active:
            continue
        b = ref.split()[0]
        (tail if (b not in dbmax or ch_of(ref) > dbmax[b]) else within).append(ref)
    def vs_of(r):
        m = re.search(r":(\d+)", r); return int(m.group(1)) if m else (int(r.split()[-1]) if r.split()[-1].isdigit() else 0)
    recover = (tail + within) if a.full else tail        # --full: all absent (co-term coverage); else tail only
    recover.sort(key=lambda r: (r.split()[0], ch_of(r), vs_of(r)))
    from collections import Counter
    mode = "FULL (all absent — co-term coverage)" if a.full else "truncation-tail only"
    print(f"STEP={len(step)} active={len(active)} | mode={mode} · to add={len(recover)} {dict(Counter(r.split()[0] for r in recover))}"
          f" | (truncation-tail={len(tail)} within-range={len(within)}{'' if a.full else ' EXCLUDED'})")

    if a.dry_run:
        print("[DRY-RUN] no changes."); return 0

    new_vcids = []
    for ref in recover:
        r = step[ref]; b3 = ref.split()[0]; bid = bmap.get(b3)
        if bid is None:
            print("  no book_id for", ref); continue
        vt = r["esv_text"] if r["esv_text"].startswith(ref) else f"{ref} {r['esv_text']}"
        row = dict(file_id=tpl["file_id"], term_inv_id=tpl["term_inv_id"], term_id=tpl["term_id"],
                   transliteration=tpl["transliteration"], testament=tpl["testament"], translation=tpl["translation"],
                   word_registry_fk=tpl["word_registry_fk"], mti_term_id=a.mti, reference=ref, last_changed=STAMP,
                   book_id=bid, chapter=r["chapter"], verse_num=r["verse_num"], target_word=r["target_word"],
                   span_strong_match=1, delete_flagged=0, morph_code=r["morph_code"], stem=(r["stem"] or None),
                   verse_id=None, verse_text=vt, created_at=STAMP, updated_at=STAMP)
        cols = ",".join(row); ph = ",".join("?" * len(row))
        cur.execute(f"INSERT INTO wa_verse_records ({cols}) VALUES ({ph})", list(row.values()))
        vrid = cur.lastrowid
        cur.execute("""INSERT INTO verse_context (verse_record_id, mti_term_id, is_anchor, is_relevant, is_related, delete_flagged)
            VALUES (?, ?, 0, 1, 0, 0)""", (vrid, a.mti))
        new_vcids.append(cur.lastrowid)
    conn.commit()
    open(a.vcids_out, "w").write(",".join(str(v) for v in new_vcids))
    tot = cur.execute("SELECT COUNT(DISTINCT reference) n FROM wa_verse_records WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (a.mti,)).fetchone()["n"]
    dup = cur.execute("""SELECT COUNT(*) n FROM (SELECT reference FROM wa_verse_records WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0
        GROUP BY reference HAVING COUNT(*)>1)""", (a.mti,)).fetchone()["n"]
    print(f"LIVE: +{len(new_vcids)} verses · {a.strong} active now {tot} · duplicate-ref groups {dup} · vcids->{a.vcids_out}")
    print("integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
