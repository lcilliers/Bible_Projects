"""PILOT: whole-Bible span coverage, Leviticus only (2026-06-28).
Goal: validate the extraction, MEASURE volume, show the orphan-delta — WITHOUT contaminating
the study corpus. Writes to a SEGREGATED table `verse_coverage_morphology` (parsed spans only,
NO raw html). Study tables (verse, verse_morphology, verse_span_index) are NOT touched.
Idempotent: DELETE coverage rows for the book before re-insert. Reversible: DROP TABLE.
"""
import os, re, sqlite3, sys, time, requests
sys.stdout.reconfigure(encoding="utf-8")
DB=os.path.join("database","bible_research.db")
BASE=os.getenv("STEP_LOCAL_URL","http://localhost:8989").rstrip("/"); VER="ESV_th"
SPAN=re.compile(r"<span\s+morph='([^']*)'\s+strong='([^']*)'>([^<]*)</span>", re.I)
import argparse
_ap=argparse.ArgumentParser(); _ap.add_argument("--book",default="Lev"); _ap.add_argument("--name",default="Leviticus"); _ap.add_argument("--nch",type=int,default=27)
_a=_ap.parse_args()
BOOK=_a.book; NAME=_a.name; NCH=_a.nch   # full run walks lastChapter; pilot passes chapter count

def prim(strongs):  # first lexical code (skip STEP grammar codes H9xxx)
    for code in strongs.split():
        m=re.match(r"^([HG])(\d+)", code)
        if m and int(m.group(2))<9000: return f"{m.group(1)}{int(m.group(2)):04d}"
    return None

def fetch(ref):
    dotted=ref.replace(" ",".").replace(":",".")
    try: return requests.get(f"{BASE}/rest/bible/getBibleText/{VER}/{dotted}",timeout=30).json().get("value","")
    except Exception: return ""

def vcount(ch):
    return fetch(f"{BOOK}.{ch}").count("class='verse ltrDirection'")

c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; cur=c.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS verse_coverage_morphology(
  id INTEGER PRIMARY KEY, reference TEXT, word_index INTEGER, surface TEXT,
  strongs TEXT, primary_strong TEXT, morph_code TEXT, built_at TEXT DEFAULT (datetime('now')))""")
cur.execute("DELETE FROM verse_coverage_morphology WHERE reference LIKE ?", (f"{BOOK} %",))
study=set(r["reference"] for r in c.execute("SELECT reference FROM verse WHERE reference LIKE ?", (f"{BOOK} %",)))
t0=time.time(); missing=[]; canon=0
for ch in range(1,NCH+1):
    n=vcount(ch); canon+=n
    for v in range(1,n+1):
        ref=f"{BOOK} {ch}:{v}"
        if ref not in study: missing.append(ref)
print(f"{NAME}: canon={canon}  study={len(study)}  MISSING={len(missing)}")
rows=0
for ref in missing:
    html=fetch(ref); wi=0
    for morph,strongs,surf in SPAN.findall(html):
        wi+=1
        cur.execute("INSERT INTO verse_coverage_morphology(reference,word_index,surface,strongs,primary_strong,morph_code) VALUES(?,?,?,?,?,?)",
                    (ref,wi,surf.strip(),strongs,prim(strongs),morph))
        rows+=1
c.commit()
print(f"coverage verses ingested={len(missing)}  spans={rows}  elapsed={time.time()-t0:.0f}s")
# volume (approx bytes from content lengths)
b=c.execute("SELECT SUM(LENGTH(reference)+LENGTH(COALESCE(surface,''))+LENGTH(COALESCE(strongs,''))+LENGTH(COALESCE(morph_code,''))+24) FROM verse_coverage_morphology").fetchone()[0]
print(f"coverage table content bytes (approx)={b}  (~{(b or 0)/1e6:.2f} MB for {NAME})")
