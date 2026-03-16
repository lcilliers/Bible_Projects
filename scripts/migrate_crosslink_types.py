"""
migrate_crosslink_types.py — 2026-03-16

Normalises wa_cross_registry_links:

1. Creates wa_crosslink_type lookup (id, type_code, description)
   - Merges 'antonym' (1 row) into SEMANTIC_OPPOSITION
   - 7 distinct codes

2. Rebuilds wa_cross_registry_links:
   - connection_type  TEXT → connection_type_id INTEGER NOT NULL FK → wa_crosslink_type
   - linked_registry_id TEXT → linked_registry_id INTEGER nullable FK → word_registry
     Attempts to resolve NULL / 'unknown' / 'TBD' values by matching
     linked_word (case-insensitive) to word_registry.word.
     Unresolvable rows (linked word not in registry yet) stay NULL.

linked_word and connecting_term remain TEXT — not touched.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()
conn.execute("PRAGMA foreign_keys=OFF")

# ── 1. Define type codes ───────────────────────────────────────────────────────
CROSSLINK_TYPES = [
    # (type_code, description)
    ("SHARED_TERM",
     "The same Hebrew or Greek term appears in both word studies"),
    ("SEMANTIC_OVERLAP",
     "The two registries share overlapping meaning space"),
    ("SHARED_ROOT",
     "The registries share a common etymological root"),
    ("SHARED_VERSE",
     "The same verse references appear in both word studies"),
    ("THEOLOGICAL",
     "The registries are connected by a theological concept or theme"),
    ("CO_OCCURRENCE",
     "Terms from the two registries frequently appear together in passages"),
    ("SEMANTIC_OPPOSITION",
     "The registries represent antonyms or semantic contrasts"),
]

# Map existing free-text values → type_code
TEXT_TO_CODE = {
    "shared_term":          "SHARED_TERM",
    "semantic_overlap":     "SEMANTIC_OVERLAP",
    "shared_root":          "SHARED_ROOT",
    "shared_verse":         "SHARED_VERSE",
    "theological":          "THEOLOGICAL",
    "co-occurrence":        "CO_OCCURRENCE",
    "semantic_opposition":  "SEMANTIC_OPPOSITION",
    "antonym":              "SEMANTIC_OPPOSITION",   # merge
}

# ── Show what we'll be resolving before committing ────────────────────────────
print("=== linked_registry_id resolution preview ===")
wr_word_to_id = {r[0].lower(): r[1] for r in conn.execute(
    "SELECT word, id FROM word_registry").fetchall()}

rows = [dict(r) for r in conn.execute(
    "SELECT * FROM wa_cross_registry_links ORDER BY id").fetchall()]

unresolvable = []
for r in rows:
    rid = r["linked_registry_id"]
    try:
        int(rid)   # already numeric string — will become INTEGER
    except (ValueError, TypeError):
        resolved = wr_word_to_id.get((r["linked_word"] or "").lower())
        status = f"→ resolved to {resolved}" if resolved else "→ stays NULL"
        print(f"  id={r['id']:4d}  linked_word={str(r['linked_word']):20s}  "
              f"reg_id={str(rid):8s}  {status}")
        if not resolved:
            unresolvable.append(r)

print(f"\n  Unresolvable (will be NULL): {len(unresolvable)}")
for r in unresolvable:
    print(f"    id={r['id']}  linked_word={r['linked_word']!r}")

# ── Migrate ───────────────────────────────────────────────────────────────────
conn.execute("BEGIN")
try:

    # 1. Create wa_crosslink_type
    conn.execute("""
        CREATE TABLE wa_crosslink_type (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            type_code   TEXT NOT NULL UNIQUE,
            description TEXT
        )
    """)
    conn.executemany(
        "INSERT INTO wa_crosslink_type (type_code, description) VALUES (?,?)",
        CROSSLINK_TYPES)
    code_to_id = {r[0]: r[1] for r in conn.execute(
        "SELECT type_code, id FROM wa_crosslink_type").fetchall()}
    print(f"\n[1] wa_crosslink_type created ({len(CROSSLINK_TYPES)} rows)")

    # 2. Build new rows
    new_rows = []
    for r in rows:
        # connection_type_id
        raw_type = (r["connection_type"] or "").strip()
        code = TEXT_TO_CODE.get(raw_type)
        if not code:
            raise ValueError(f"Unknown connection_type {raw_type!r} on row id={r['id']}")
        type_id = code_to_id[code]

        # linked_registry_id → INTEGER or NULL
        rid_raw = r["linked_registry_id"]
        try:
            rid_int = int(rid_raw)
        except (ValueError, TypeError):
            rid_int = wr_word_to_id.get((r["linked_word"] or "").lower())

        new_rows.append((
            r["file_id"],
            r["linked_word"],
            rid_int,
            type_id,
            r["connecting_term"],
            r["note"],
            r["last_changed"],
        ))

    # 3. Rebuild wa_cross_registry_links
    conn.execute("DROP TABLE wa_cross_registry_links")
    conn.execute("""
        CREATE TABLE wa_cross_registry_links (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            file_id             INTEGER NOT NULL REFERENCES wa_file_index(id),
            linked_word         TEXT,
            linked_registry_id  INTEGER REFERENCES word_registry(id),
            connection_type_id  INTEGER NOT NULL REFERENCES wa_crosslink_type(id),
            connecting_term     TEXT,
            note                TEXT,
            last_changed        TEXT
        )
    """)
    conn.execute("CREATE INDEX idx_wa_xrl_file ON wa_cross_registry_links (file_id)")
    conn.execute("CREATE INDEX idx_wa_xrl_linked ON wa_cross_registry_links (linked_registry_id)")
    conn.executemany("""
        INSERT INTO wa_cross_registry_links
            (file_id, linked_word, linked_registry_id, connection_type_id,
             connecting_term, note, last_changed)
        VALUES (?,?,?,?,?,?,?)
    """, new_rows)

    n = conn.execute("SELECT COUNT(*) FROM wa_cross_registry_links").fetchone()[0]
    print(f"[2] wa_cross_registry_links rebuilt ({n} rows)")

    conn.execute("COMMIT")
    print("\n✓ Migration complete")

except Exception as e:
    conn.execute("ROLLBACK")
    print(f"\n✗ ROLLED BACK: {e}")
    raise
finally:
    conn.execute("PRAGMA foreign_keys=ON")

# ── Post-migration summary ─────────────────────────────────────────────────────
print("\n=== wa_crosslink_type ===")
for r in conn.execute("SELECT id, type_code, description FROM wa_crosslink_type ORDER BY id").fetchall():
    cnt = conn.execute(
        "SELECT COUNT(*) FROM wa_cross_registry_links WHERE connection_type_id=?", (r[0],)).fetchone()[0]
    print(f"  {r[0]:3d}  {r[1]:22s}  uses={cnt:3d}  {r[2] or ''}")

print()
null_reg = conn.execute(
    "SELECT COUNT(*) FROM wa_cross_registry_links WHERE linked_registry_id IS NULL").fetchone()[0]
resolved = conn.execute(
    "SELECT COUNT(*) FROM wa_cross_registry_links WHERE linked_registry_id IS NOT NULL").fetchone()[0]
print(f"linked_registry_id resolved: {resolved}  NULL: {null_reg}")

conn.close()
