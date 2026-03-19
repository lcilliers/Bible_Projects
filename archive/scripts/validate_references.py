"""Validate all reference values in wa_verse_records."""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

rows = conn.execute("""
    SELECT id, term_id, file_id, reference, book_id, chapter, verse_num
    FROM wa_verse_records
""").fetchall()
rows = [dict(r) for r in rows]
total = len(rows)

# NULL reference
null_ref = [r for r in rows if not r["reference"]]
print(f"Total rows   : {total}")
print(f"NULL reference: {len(null_ref)}")
for r in null_ref:
    print(f"  id={r['id']}  term={r['term_id']}  reference={r['reference']}  book_id={r['book_id']}")

print()

# Format validity — allow digit-prefixed codes like 1Ki, 2Ch, 1Co, 1Sa
std_pattern = re.compile(r'^[A-Za-z0-9]{2,5} \d+:\d+$')   # e.g. "Gen 3:16", "1Ki 14:24"
sc_pattern  = re.compile(r'^[A-Za-z0-9]{2,5} \d+$')         # e.g. "Obd 17", "Jude 16"
bad_format = [r for r in rows if r["reference"] and
              not std_pattern.match(r["reference"]) and
              not sc_pattern.match(r["reference"])]
print(f"Bad format references: {len(bad_format)}")
for r in bad_format[:20]:
    print(f"  id={r['id']}  reference={repr(r['reference'])}")

print()

# Validate short_code in reference matches books table
books_sc = {b["id"]: b["short_code"] for b in
            [dict(r) for r in conn.execute("SELECT id, short_code FROM books").fetchall()]}

code_mismatch = []
for r in rows:
    if not r["reference"] or not r["book_id"]:
        continue
    ref_code = r["reference"].split(" ")[0]
    expected = books_sc.get(r["book_id"])
    if expected and ref_code != expected:
        code_mismatch.append((r["id"], r["reference"], r["book_id"], ref_code, expected))

print(f"Reference code vs book_id short_code mismatches: {len(code_mismatch)}")
for row in code_mismatch[:20]:
    print(f"  id={row[0]}  reference={row[1]:20s}  book_id={row[2]}  ref_code={row[3]:8s}  expected={row[4]}")

conn.close()
