"""D6 — capture a contributor source (Logos / AI-Chat) into prose_section, strip it
from the raw fanout file, and leave a cross-reference. 'Capture once → route many':
this captures the raw block verbatim (the source); routing segments to observations
is a later, separate step.

First use: the Gen 6:5 Logos block. Parameterised for reuse.

  python scripts/_apply_d6_capture_contributor_source.py \
      --file verse-analysis/Gen/wa-gen-006-005-fanout-v1-20260627.md \
      --provenance logos --start "Logos extracts" --end "researcher comments" \
      --topic "the heart: meaning, transformation, guarding (reference extracts)" \
      --origin "Gen 6:5" --cluster M47
"""
import sqlite3, os, argparse, datetime, json

DB = os.path.join('database', 'bible_research.db')

TYPES = {  # code -> label  (created on demand)
 'src_logos': 'Contributor source — Logos extract (capture once → route many)',
 'src_aichat': 'Contributor source — AI-Chat extract (capture once → route many)'}

def ensure_types(c):
    nxt = (c.execute('SELECT max(id) FROM prose_section_type').fetchone()[0] or 0) + 1
    ids = {}
    for code, label in TYPES.items():
        row = c.execute('SELECT id FROM prose_section_type WHERE code=?', (code,)).fetchone()
        if row:
            ids[code] = row[0]
        else:
            c.execute("""INSERT INTO prose_section_type (id,code,label,source_stage,lifecycle_tag,sort_order,delete_flagged,created_at)
                VALUES (?,?,?,?,?,?,0,?)""",
                (nxt, code, label, 'contributor', 'source', 900+nxt, _now()))
            ids[code] = nxt; nxt += 1
            print(f"created type {code} (id {ids[code]})")
    return ids

def _now(): return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--file', required=True)
    ap.add_argument('--provenance', default='logos', choices=['logos','aichat'])
    ap.add_argument('--start', required=True, help='marker line where the block begins')
    ap.add_argument('--end', required=True, help='marker line where the block ends (exclusive)')
    ap.add_argument('--topic', required=True)
    ap.add_argument('--origin', required=True, help='origin verse ref')
    ap.add_argument('--cluster', default=None)
    a = ap.parse_args()

    with open(a.file, encoding='utf-8') as fh: text = fh.read()
    si = text.find(a.start)
    ei = text.find(a.end)
    if si < 0 or ei < 0 or ei <= si:
        print(f"markers not found cleanly (start={si}, end={ei})"); return
    block = text[si:ei].strip()
    prefix = text[:si]
    suffix = text[ei:]

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()
    code = 'src_' + a.provenance
    tid = ensure_types(c)[code]
    heading = f"{a.origin} — {a.provenance.upper()}: {a.topic}"
    meta = json.dumps({"contributor": a.provenance, "origin_verse": a.origin,
                       "topic": a.topic, "captured": datetime.date.today().isoformat(),
                       "source_file": os.path.basename(a.file)})
    c.execute("""INSERT INTO prose_section
        (section_type_id,heading,body,word_count,status,version,author,created_at,source_file,metadata_json,cluster_code,delete_flagged)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,0)""",
        (tid, heading, block, len(block.split()), 'approved', 1, 'researcher',
         _now(), os.path.basename(a.file), meta, a.cluster))
    pid = c.lastrowid
    conn.commit()
    print(f"captured prose_section #{pid} ({code}, {len(block.split())} words) — {heading}")

    # rewrite the fanout: strip the block, leave a cross-reference
    xref = (f"## Contributor sources (D6)\n"
            f"- **{a.provenance.upper()} extract** — *{a.topic}* — captured verbatim to "
            f"`prose_section #{pid}` (type `{code}`, provenance `{a.provenance}`"
            + (f", cluster {a.cluster}" if a.cluster else "") + f", origin {a.origin}). "
            f"Searchable via `prose_section_fts`. **Stripped from this raw file** (D6: capture once → route many); "
            f"segments route to observations on demand.\n\n")
    new = prefix + xref + suffix
    new = new.replace("(Logos + AI-chat contributions to be added.)",
                      "(Contributor extracts captured via D6 — see Contributor sources below.)")
    with open(a.file, 'w', encoding='utf-8') as fh: fh.write(new)
    print(f"rewrote {a.file}: block stripped, cross-reference to #{pid} left in place")
    conn.close()

if __name__ == '__main__': main()
