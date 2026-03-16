"""Audit all STEP reference codes vs books.short_code to map variants needed."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()

ver = conn.execute("SELECT sqlite_version()").fetchone()[0]
print(f"SQLite version: {ver}")

step_codes = conn.execute("""
    SELECT SUBSTR(reference, 1, INSTR(reference, ' ')-1) AS code, COUNT(*) AS cnt
    FROM wa_verse_records
    WHERE reference IS NOT NULL
    GROUP BY code ORDER BY code
""").fetchall()

all_books = [dict(r) for r in conn.execute("SELECT id, name, short_code FROM books ORDER BY id").fetchall()]
sc_to_id   = {b["short_code"]: b["id"]   for b in all_books}
id_to_book = {b["id"]: b               for b in all_books}

print(f"\nDistinct STEP codes in reference ({len(step_codes)} total):")
print(f"  {'Code':<10}  {'Count':>6}  {'Match?':<8}  books.name")

mismatches = []
for row in step_codes:
    code, cnt = row[0], row[1]
    book_id = sc_to_id.get(code)
    if book_id:
        name = id_to_book[book_id]["name"]
        print(f"  {code:<10}  {cnt:>6}  YES       {name}")
    else:
        mismatches.append((code, cnt))
        print(f"  {code:<10}  {cnt:>6}  NO MATCH  <<<")

print(f"\nCodes with no direct short_code match: {len(mismatches)}")
for code, cnt in mismatches:
    print(f"  {code}  ({cnt} rows)")

conn.close()
