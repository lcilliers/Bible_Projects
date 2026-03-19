import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection
conn = get_connection()

# 1. Check linked_registry_id — TEXT or real FK?
print("=== linked_registry_id: does it match word_registry.id? ===")
wr_ids = {r[0] for r in conn.execute("SELECT id FROM word_registry").fetchall()}
wr_words = {r[0]: r[1] for r in conn.execute("SELECT id, word FROM word_registry").fetchall()}
rows = [dict(r) for r in conn.execute("SELECT * FROM wa_cross_registry_links ORDER BY id").fetchall()]

matched   = [r for r in rows if r["linked_registry_id"] is not None and int(r["linked_registry_id"]) in wr_ids]
unmatched = [r for r in rows if r["linked_registry_id"] is None or int(r["linked_registry_id"]) not in wr_ids]
print(f"  Total rows: {len(rows)}")
print(f"  Matched to word_registry.id: {len(matched)}")
print(f"  Unmatched / NULL: {len(unmatched)}")
if unmatched:
    for r in unmatched:
        print(f"    id={r['id']} linked_registry_id={r['linked_registry_id']!r} linked_word={r['linked_word']!r}")

# 2. Does linked_word match word_registry.word for the matched rows?
print()
print("=== linked_word vs word_registry.word ===")
mismatches = []
for r in matched:
    rid = int(r["linked_registry_id"])
    expected = wr_words.get(rid, "")
    if r["linked_word"] and r["linked_word"].lower() != expected.lower():
        mismatches.append((r["id"], r["linked_word"], expected))
print(f"  Mismatches: {len(mismatches)}")
for m in mismatches[:10]:
    print(f"    row_id={m[0]}  linked_word={m[1]!r}  word_registry.word={m[2]!r}")

# 3. What is in file_id — one row per term or one row per file/registry entry?
print()
print("=== file_id: does it link to a specific term or just a file? ===")
for r in conn.execute("""
    SELECT crl.file_id, fi.word, crl.linked_word, crl.connection_type,
           crl.connecting_term, crl.linked_registry_id
    FROM wa_cross_registry_links crl
    JOIN wa_file_index fi ON fi.id = crl.file_id
    ORDER BY crl.file_id, crl.id
    LIMIT 30
""").fetchall():
    print(f"  file={r[0]:3d}  word={str(r[1]):15s}  linked={str(r[2]):15s}  "
          f"type={str(r[3]):20s}  term={str(r[4]):20s}  reg_id={r[5]}")

# 4. Is there a term_inv_id / term_id on this table — or is it registry-level only?
print()
print("=== any term-level column on this table? ===")
cols = [c[1] for c in conn.execute("PRAGMA table_info(wa_cross_registry_links)").fetchall()]
print(f"  Columns: {cols}")
print("  'connecting_term' appears to be a TEXT description, not an FK")

# 5. How many distinct file_ids, and how many links per file?
print()
print("=== Links per file ===")
for r in conn.execute("""
    SELECT crl.file_id, fi.word, COUNT(*) cnt
    FROM wa_cross_registry_links crl
    JOIN wa_file_index fi ON fi.id = crl.file_id
    GROUP BY crl.file_id
    ORDER BY cnt DESC
    LIMIT 15
""").fetchall():
    print(f"  file={r[0]:3d}  word={str(r[1]):20s}  links={r[2]}")

conn.close()
