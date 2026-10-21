"""OT-05.26 / OT-05.30 (#2160): R0 pull for Ch 2 'The body raised' (read-only).

Researcher, chat 2026-10-19 (verbatim): "OT-05.26: R0 of The body raised over the 76 cited verses
plus the resurrection/perishable/mortal words (not the glory or generic raise handles). Read and
report the impact."

Set = (a) the verses the section and its subsections cite (narrative_citation, live rows) and
(b) every verse carrying a resurrection / perishable / mortal word (verse_lexical). The raise verbs
G1453 / G0450 count only where they stand with nekros G3498 ("from the dead"); their generic uses
are the excluded handles. Writes the CSV beside this script.
"""
import csv
import pathlib
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).parent
DB = "file:iba/app/db/iba.db?mode=ro"
OUT = HERE / "life-death-ot05-26-body-raised-r0-pull-v1-20261019.csv"

WORDS = {
    "G0386": "anastasis resurrection", "G1815": "exanastasis resurrection",
    "G1454": "egersis resurrection", "G4891": "synegeiro raised with",
    "G1825": "exegeiro raise", "G5349": "phthartos perishable",
    "G0862": "aphthartos imperishable", "G0861": "aphtharsia imperishability",
    "G5356": "phthora corruption", "G2349": "thnetos mortal",
    "G0110": "athanasia immortality",
}
WITH_NEKROS = {"G1453": "egeiro raise", "G0450": "anistemi arise"}
SECTIONS = ("The body raised", "Sown and raised", "Christ first", "Changed", "Waited for",
            "Life, and judgment")

c = sqlite3.connect(DB, uri=True)
ch2 = c.execute("SELECT id FROM narrative_chapter WHERE chapter_no='02'").fetchone()[0]
sec_ids = {r[0]: r[1] for r in c.execute(
    f"SELECT id, heading FROM narrative_section WHERE chapter_id=? AND heading IN "
    f"({','.join('?' * len(SECTIONS))}) AND last_version IS NULL", (ch2, *SECTIONS))}

def codes_in(vid):
    return {r[0] for r in c.execute(
        "SELECT DISTINCT strong FROM verse_lexical WHERE verse_id=? AND deleted=0", (vid,))}

rows = {}
for vid, sid in c.execute(
        f"SELECT DISTINCT verse_id, section_id FROM narrative_citation WHERE chapter_id=? AND "
        f"section_id IN ({','.join('?' * len(sec_ids))}) AND last_version IS NULL AND verse_id IS NOT NULL",
        (ch2, *sec_ids)):
    rows.setdefault(vid, {"cited_here": set(), "words": set()})["cited_here"].add(sec_ids[sid])

for code in WORDS:
    for (vid,) in c.execute("SELECT DISTINCT verse_id FROM verse_lexical WHERE strong=? AND deleted=0", (code,)):
        rows.setdefault(vid, {"cited_here": set(), "words": set()})["words"].add(code)
for code in WITH_NEKROS:
    for (vid,) in c.execute("SELECT DISTINCT verse_id FROM verse_lexical WHERE strong=? AND deleted=0", (code,)):
        if "G3498" in codes_in(vid):
            rows.setdefault(vid, {"cited_here": set(), "words": set()})["words"].add(code + "+G3498")

def sort_key(vid):
    o = c.execute("SELECT osisId FROM verse WHERE id=?", (vid,)).fetchone()[0]
    b, ch, v = o.split(".")
    rank = c.execute("SELECT ordinal FROM cfg_book_order WHERE book=?", (b,)).fetchone()
    return (rank[0] if rank else 999, int(ch), int(v))

out = []
for vid in sorted(rows, key=sort_key):
    ref, text = c.execute("SELECT reference, text FROM verse WHERE id=?", (vid,)).fetchone()
    elsewhere = sorted({f"{r[0]} {r[1]}" for r in c.execute(
        "SELECT ch.chapter_no, s.heading FROM narrative_citation nc JOIN narrative_chapter ch ON ch.id=nc.chapter_id "
        "LEFT JOIN narrative_section s ON s.id=nc.section_id WHERE nc.verse_id=? AND nc.last_version IS NULL", (vid,))
        if not (r[0] == "02" and r[1] in SECTIONS)})
    claims = sorted({r[0] for r in c.execute(
        "SELECT cl.claim_ref FROM narrative_claim_source s JOIN narrative_claim cl ON cl.id=s.claim_id "
        "WHERE s.verse_id=? AND cl.status != 'withdrawn'", (vid,))})
    d = rows[vid]
    out.append({"ref": ref, "verse_id": vid, "cited_in_section": "; ".join(sorted(d["cited_here"])),
                "words": " ".join(sorted(d["words"])), "cited_elsewhere": "; ".join(elsewhere),
                "claims": " ".join(claims), "text": text})

with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0]))
    w.writeheader()
    w.writerows(out)

cited = [r for r in out if r["cited_in_section"]]
worded = [r for r in out if r["words"]]
print(f"sections found: {sorted(sec_ids.values())}")
print(f"verses: {len(out)} | cited in the section: {len(cited)} | with a set word: {len(worded)}")
print(f"  cited, no set word: {sum(1 for r in cited if not r['words'])}")
print(f"  set word, not cited in section: {sum(1 for r in worded if not r['cited_in_section'])}"
      f" (of which cited elsewhere: {sum(1 for r in worded if not r['cited_in_section'] and r['cited_elsewhere'])})")
print(f"  cited in section with a claim source: {sum(1 for r in cited if r['claims'])}")
print(f"-> {OUT.name}")
