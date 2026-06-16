"""_apply_ingest_verse_morphology.py (2026-06-16) — populate the persisted MEASURE LAYER (M60).

Steps (idempotent / resumable):
  1. populate `verse` (canonical, one row per active reference) + set `wa_verse_records.verse_id`;
  2. for each verse not yet ingested, fetch its full-verse interlinear from STEP, parse every word
     (surface · strongs · morph · derived lang/pos/stem/person) -> `verse_morphology`; keep raw html;
  3. enrich `lexicon` (original-language unicode · transliteration · gloss · medium_def) per Strong's.

Per-verse TIMING + a CIRCUIT-BREAKER abort (VE_MAX_SEC, default 30s) — the trigger to stop a bulk run.
Resumable: re-running continues where it stopped (skips verses already in verse_morphology).

  python scripts/_apply_ingest_verse_morphology.py --dry-run [--limit 20]
  python scripts/_apply_ingest_verse_morphology.py --live [--limit N]
"""
import argparse, os, re, sqlite3, sys, time
import requests
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "analytics"))
from step_client import StepClient
import morph_util
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
SPAN = re.compile(r"<span\s+morph='([^']*)'\s+strong='([^']*)'>([^<]*)</span>", re.I)
NOW = "2026-06-16T00:00:00Z"
BASE = os.getenv("STEP_LOCAL_URL", "http://localhost:8989").rstrip("/")
VER = os.getenv("STEP_VERSION", "ESV_th")


def fetch_verse(ref):
    """Direct passage fetch by reference (robust, no search-cap). Returns (osisId, html)."""
    dotted = ref.replace(" ", ".").replace(":", ".")
    try:
        d = requests.get(f"{BASE}/rest/bible/getBibleText/{VER}/{dotted}", timeout=30).json()
        return d.get("osisId"), d.get("value", "")
    except Exception:
        return None, ""


def b(s):
    m = re.match(r"^([HG]\d+)", s or "")
    return m.group(1) if m else (s or "")


def person(morph):
    morph = morph or ""
    if "-" in morph:
        m = re.search(r"([123])[SP]", morph); return int(m.group(1)) if m else None
    m = re.search(r"[123]", morph); return int(m.group(0)) if m else None


def parse_words(html, verse_id):
    rows = []
    for i, (morphs, strongs, text) in enumerate(SPAN.findall(html or "")):
        m0 = morphs.split()[0] if morphs.split() else ""
        rows.append((verse_id, i, text.strip(), strongs, b(strongs.split()[0]) if strongs.split() else None,
                     morphs, morph_util.morph_language(m0), morph_util.morph_category(m0),
                     morph_util.morph_stem(m0), person(m0), "STEP", NOW))
    return rows


class Cache:
    def __init__(s): s.sc = StepClient(); s.h = {}; s.v = {}
    def fetch(s, strong):
        k = b(strong)
        if k not in s.h:
            try: s.h[k] = s.sc.get_verse_records_with_html(k)
            except Exception: s.h[k] = ([], {})
        return s.h[k]
    def vocab(s, strong):
        if strong not in s.v:
            try: s.v[strong] = s.sc.get_vocab_info(strong)
            except Exception: s.v[strong] = {}
        return s.v[strong]


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    MAX_SEC = float(os.environ.get("VE_MAX_SEC", "30"))
    conn = sqlite3.connect(DB, timeout=600); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cache = Cache()

    # 1. populate verse + verse_id (fast, pure DB) — live only
    if a.live:
        cur.execute("""INSERT OR IGNORE INTO verse (reference, book_id, chapter, verse_num, testament, verse_text, created_at)
            SELECT reference, MIN(book_id), MIN(chapter), MIN(verse_num), MIN(testament), MIN(verse_text), ?
            FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0 GROUP BY reference""", (NOW,))
        cur.execute("""UPDATE wa_verse_records SET verse_id =
            (SELECT id FROM verse WHERE verse.reference = wa_verse_records.reference) WHERE verse_id IS NULL""")
        conn.commit()
    nverse = cur.execute("SELECT COUNT(*) FROM verse").fetchone()[0]
    linked = cur.execute("SELECT COUNT(*) FROM wa_verse_records WHERE verse_id IS NOT NULL AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    print(f"verse rows: {nverse:,} · wa_verse_records linked: {linked:,}")

    # 2. ingest morphology for verses not yet done
    if a.live:
        todo = cur.execute("""SELECT v.id, v.reference FROM verse v
            WHERE NOT EXISTS (SELECT 1 FROM verse_morphology m WHERE m.verse_id = v.id) ORDER BY v.id""").fetchall()
    else:  # dry: sample distinct active refs
        todo = cur.execute("""SELECT MIN(id) id, reference FROM verse GROUP BY reference ORDER BY id""").fetchall() \
            if nverse else [sqlite3.Row]  # fallback handled below
        if not nverse:
            todo = [(None, r["reference"]) for r in cur.execute(
                "SELECT DISTINCT reference FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0 LIMIT ?", (a.limit or 20,))]
    if a.limit:
        todo = todo[:a.limit]
    print(f"verses to ingest this run: {len(todo):,}{' (dry-run: parse only, no writes)' if a.dry_run else ''}\n")

    done = miss = wordtot = 0
    timings = []
    for row in todo:
        vid = row[0] if not isinstance(row, sqlite3.Row) else row["id"]
        ref = row[1] if not isinstance(row, sqlite3.Row) else row["reference"]
        t0 = time.time()
        osis, html = fetch_verse(ref)
        if not html or "morph='" not in html:
            miss += 1; print(f"  MISS {ref}"); continue
        rows = parse_words(html, vid)
        wordtot += len(rows)
        if a.live:
            cur.executemany("""INSERT INTO verse_morphology
                (verse_id, word_index, surface, strongs, primary_strong, morph_code, language, pos, stem, person, source, fetched_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""", rows)
            cur.execute("INSERT OR REPLACE INTO verse_morphology_raw (verse_id, html, fetched_at) VALUES (?,?,?)", (vid, html, NOW))
            cur.execute("UPDATE verse SET osis_id=? WHERE id=? AND osis_id IS NULL", (osis, vid))
            conn.commit()
        done += 1
        dt = time.time() - t0
        timings.append(dt)
        if done <= 6 or a.dry_run:
            print(f"  {ref}: {len(rows)} words, {dt:.2f}s  e.g. " +
                  ", ".join(f"{r[2]}[{r[5]}]" for r in rows[:4]))
        if dt > MAX_SEC:
            print(f"\n⛔ CIRCUIT-BREAKER: {ref} took {dt:.1f}s > {MAX_SEC}s — aborting."); break

    # 3. lexicon enrichment (distinct content strongs not yet in lexicon) — live only
    if a.live:
        strongs = [r["primary_strong"] for r in cur.execute(
            """SELECT DISTINCT primary_strong FROM verse_morphology
               WHERE primary_strong IS NOT NULL AND primary_strong NOT LIKE 'H9%'
               AND primary_strong NOT IN (SELECT strong FROM lexicon)""").fetchall()]
        if a.limit:
            strongs = strongs[:a.limit * 8]
        lex = 0
        for st in strongs:
            vi = cache.vocab(st)
            if not vi: continue
            cur.execute("""INSERT OR REPLACE INTO lexicon
                (strong, original_unicode, transliteration, gloss, medium_def, language, occurrence_count, source, fetched_at)
                VALUES (?,?,?,?,?,?,?,?,?)""",
                (st, vi.get("hebrew_unicode") or vi.get("greek_unicode") or vi.get("original"),
                 vi.get("transliteration"), vi.get("gloss"), vi.get("medium_def"),
                 vi.get("language"), vi.get("occurrence_count"), "STEP", NOW))
            lex += 1
        conn.commit()
        print(f"\nlexicon enriched: +{lex} Strong's")

    if timings:
        tot = sum(timings); n = len(timings)
        remaining = cur.execute("""SELECT COUNT(*) FROM verse v WHERE NOT EXISTS
            (SELECT 1 FROM verse_morphology m WHERE m.verse_id=v.id)""").fetchone()[0] if a.live else "—"
        print(f"\nDONE: {done} verses ({wordtot:,} words), {miss} missed · {tot:.1f}s · {tot/n:.3f}s/verse")
        if a.live:
            print(f"remaining un-ingested verses: {remaining:,}  (re-run --live to continue; est ~{(remaining or 0)*tot/n/60:.0f} min)")
    print("DRY-RUN — no writes." if a.dry_run else "LIVE.")


if __name__ == "__main__":
    main()
