"""Pre-existence check for 8 Session A extraction targets (action group 5).

For each Strong's: does mti_terms already have it? If so, what state?
Also check for leading-zero variants and adjacent codes.
"""
import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')
c = sqlite3.connect('database/bible_research.db')
c.row_factory = sqlite3.Row

TARGETS = [
    # (Tier, Strong's-canonical, leading-zero variant, expected translit, gloss)
    ("1", "G4145", "G4145", "plousios", "rich"),
    ("1", "G4149", "G4149", "ploutos", "wealth, riches"),
    ("1", "G4147", "G4147", "ploutēō", "to be/become rich"),
    ("1", "G4148", "G4148", "ploutizō", "to make rich"),
    ("1", "G4434", "G4434", "ptōchos", "poor"),
    ("2", "H6239", "H6239", "o.sher", "riches"),
    ("2", "H6223", "H6223", "a.shir", "rich person"),
    ("2", "H6238", "H6238", "a.shar", "to become rich"),
]


def check(strongs_canonical, translit, gloss):
    # Look for exact match + suffixed variants (A/B/C)
    rows = list(c.execute("""
        SELECT id, strongs_number, transliteration, gloss, language,
               cluster_code, vc_status, status, owning_word, owning_registry_fk,
               COALESCE(delete_flagged,0) deleted
        FROM mti_terms
        WHERE strongs_number IN (?, ?||'A', ?||'B')
        ORDER BY strongs_number
    """, (strongs_canonical, strongs_canonical, strongs_canonical)))
    if rows:
        return rows
    # Translit fallback search (loose)
    rows = list(c.execute("""
        SELECT id, strongs_number, transliteration, gloss, language,
               cluster_code, vc_status, status, owning_word, owning_registry_fk,
               COALESCE(delete_flagged,0) deleted
        FROM mti_terms
        WHERE LOWER(transliteration) LIKE ?
        LIMIT 4
    """, (f"%{translit.lower().split('.')[0]}%",)))
    return rows


print(f"{'='*72}\n  Pre-existence check — 8 Session A targets\n{'='*72}\n")

found = []
not_found = []
for tier, strongs, _zerov, translit, gloss in TARGETS:
    rows = check(strongs, translit, gloss)
    label = f"Tier {tier}  {strongs:<7} {translit:<11}"
    if not rows:
        not_found.append((tier, strongs, translit, gloss))
        print(f"{label} ✗ NOT FOUND (needs STEP extraction)")
        continue
    for r in rows:
        marker = " "
        if r['strongs_number'] == strongs:
            marker = "✓"
        elif r['strongs_number'].startswith(strongs):
            marker = "≈"  # suffixed variant
        else:
            marker = "?"  # translit fallback hit
        del_flag = " [DELETED]" if r['deleted'] else ""
        print(f"{label} {marker} mti={r['id']:<5} {r['strongs_number']:<8} "
              f"'{r['transliteration']}' '{(r['gloss'] or '')[:25]}'{del_flag}")
        print(f"           cluster={r['cluster_code']!s:<10} vc_status={r['vc_status']!s:<14} "
              f"status={r['status']} owning_word={r['owning_word']}")
        if marker in ("✓", "≈") and not r['deleted']:
            n_vr = c.execute("SELECT COUNT(*) FROM wa_verse_records "
                             "WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0",
                             (r['id'],)).fetchone()[0]
            n_vc = c.execute("SELECT COUNT(*) FROM verse_context "
                             "WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0",
                             (r['id'],)).fetchone()[0]
            print(f"           wa_verse_records={n_vr}  verse_context={n_vc}")
            found.append((tier, strongs, translit, r['id'], r['strongs_number'],
                          r['cluster_code'], n_vr, n_vc))

print(f"\n{'='*72}\n  Summary\n{'='*72}")
print(f"  Found (active, exact or suffixed): {len(found)}")
for f in found:
    print(f"    Tier {f[0]}: {f[1]} {f[2]:<11} → mti={f[3]} ({f[4]}) cluster={f[5]} vr={f[6]} vc={f[7]}")
print(f"\n  Not found (need STEP extraction): {len(not_found)}")
for nf in not_found:
    print(f"    Tier {nf[0]}: {nf[1]} {nf[2]:<11} {nf[3]}")

# Also check word_registry for "wealth" or related
print(f"\n{'='*72}\n  word_registry check\n{'='*72}")
for r in c.execute("""SELECT no, word, source, COALESCE(phase1_status,'') AS p1,
                            COALESCE(verse_context_status,'') AS vcs
                     FROM word_registry
                     WHERE LOWER(word) IN ('wealth','rich','riches','poor','poverty','abundance','prosperity')
                     ORDER BY word"""):
    print(f"  no={r['no']:<3} {r['word']:<14} source={r['source']} "
          f"phase1={r['p1']!s:<14} vcs={r['vcs']}")
