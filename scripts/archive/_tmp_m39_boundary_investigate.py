"""Investigate M39 BOUNDARY terms: H2868 te.ev, G1435 dōron, H7862 shay.

Per v1_11 §13.6, every BOUNDARY term must exit before cluster closure.
Gather: verse list, current VC classifications, groups, findings,
adjacent cluster candidates for reassignment.
"""
import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')
c = sqlite3.connect('database/bible_research.db')
c.row_factory = sqlite3.Row


def divider(s):
    print(f"\n{'=' * 72}\n  {s}\n{'=' * 72}")


def section(s):
    print(f"\n--- {s} ---")


for strongs, label in [("H2868", "te.ev (gladness?)"),
                       ("G1435", "dōron (gift)"),
                       ("H7862", "shay (tribute)")]:
    divider(f"{strongs} — {label}")

    # Identity
    r = c.execute("""SELECT id, strongs_number, transliteration, gloss, language,
                            status, vc_status, cluster_code, owning_word,
                            owning_registry_fk, anchor_note
                     FROM mti_terms WHERE strongs_number=?""", (strongs,)).fetchone()
    if not r:
        print(f"  not found"); continue
    mti_id = r['id']
    print(f"  mti_id={mti_id}")
    print(f"  gloss={r['gloss']!r} language={r['language']}")
    print(f"  status={r['status']} vc_status={r['vc_status']}")
    print(f"  cluster_code={r['cluster_code']} owning_word={r['owning_word']!r}")
    print(f"  anchor_note={r['anchor_note']}")

    # Active verse count + verse list
    section("Active verses (with VC state)")
    rows = list(c.execute("""
        SELECT vr.id vr_id, vr.reference, vr.target_word, vr.span_strong_match,
               vc.id vc_id, vc.group_id, vc.is_anchor, vc.is_relevant,
               vc.set_aside_reason,
               vcg.group_code, SUBSTR(vcg.context_description, 1, 100) as group_desc
        FROM wa_verse_records vr
        LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id
                                   AND vc.mti_term_id = vr.mti_term_id
        LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id
        WHERE vr.mti_term_id = ? AND COALESCE(vr.delete_flagged,0)=0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, (mti_id,)))
    print(f"  Total active verses: {len(rows)}")
    for r in rows:
        state = ('SET_ASIDE' if r['set_aside_reason']
                 else 'RELEVANT' if r['is_relevant'] == 1
                 else 'UT' if r['vc_id'] is None
                 else 'other')
        anchor = '★' if r['is_anchor'] else ' '
        gc = r['group_code'] or '-'
        print(f"  {anchor} vr={r['vr_id']:<7} {r['reference']:<14} target={r['target_word']!s:<15} "
              f"span={r['span_strong_match']}  {state:<10}  {gc}")
        if r['group_desc']:
            print(f"        group: {r['group_desc']}")
        if r['set_aside_reason']:
            print(f"        set_aside: {r['set_aside_reason']}")

    # Existing verse_context_group rows for this term
    section("Existing VCGs for this term (mti_term_id-prefixed)")
    for r in c.execute("""
        SELECT id, group_code, SUBSTR(context_description, 1, 150) as desc,
               COALESCE(delete_flagged,0) deleted
        FROM verse_context_group
        WHERE group_code LIKE ?
        ORDER BY group_code
    """, (f"{mti_id}-%",)):
        marker = " [DELETED]" if r['deleted'] else ""
        print(f"  vcg_id={r['id']:<5} {r['group_code']!s:<14}{marker}")
        print(f"        {r['desc']}")

    # Session research flags for this term's registry
    section("Session research flags (registry-level)")
    registry_id = c.execute("""SELECT owning_registry_fk FROM mti_terms WHERE id=?""",
                            (mti_id,)).fetchone()['owning_registry_fk']
    fl = list(c.execute("""
        SELECT flag_code, flag_label, strongs_reference, priority, resolved,
               SUBSTR(description, 1, 200) as desc
        FROM wa_session_research_flags
        WHERE registry_id=? AND (strongs_reference LIKE ? OR description LIKE ?)
        ORDER BY priority DESC, flag_code
        LIMIT 8
    """, (registry_id, f'%{strongs}%', f'%{strongs}%')))
    print(f"  registry_id={registry_id}, flags filtering by {strongs}: {len(fl)}")
    for r in fl:
        print(f"  [{r['flag_code']:<22}] pri={r['priority']!s:<3} resolved={r['resolved']}  {r['strongs_reference']}")
        if r['desc']:
            print(f"      {r['desc']}")


# Cluster landscape — what clusters could absorb these terms?
divider("Cluster landscape — potential reassignment targets")
print()
print("Clusters with 'glad' / 'joy' / 'gift' / 'reverence' in gloss/short_name:")
for r in c.execute("""
    SELECT cluster_code, short_name, status, gloss
    FROM cluster
    WHERE LOWER(gloss) LIKE '%glad%' OR LOWER(gloss) LIKE '%joy%'
       OR LOWER(gloss) LIKE '%merry%' OR LOWER(gloss) LIKE '%gift%'
       OR LOWER(gloss) LIKE '%reverence%' OR LOWER(gloss) LIKE '%awe%'
       OR LOWER(gloss) LIKE '%worship%'
       OR LOWER(short_name) LIKE '%joy%' OR LOWER(short_name) LIKE '%glad%'
       OR LOWER(short_name) LIKE '%reverence%' OR LOWER(short_name) LIKE '%awe%'
       OR LOWER(short_name) LIKE '%worship%' OR LOWER(short_name) LIKE '%fear%'
    ORDER BY cluster_code
"""):
    g = (r['gloss'] or '')[:120]
    print(f"  {r['cluster_code']:<5} {r['short_name']:<22} status={r['status']:<22} gloss={g}")

# Also check whether te.ev's adjacent terms (other gladness terms in M39 or elsewhere) are placed
divider("Adjacent gladness/joy terms in DB (search 'glad' / 'rejoice' / 'merry')")
for r in c.execute("""
    SELECT id, strongs_number, transliteration, gloss, cluster_code
    FROM mti_terms
    WHERE (LOWER(gloss) LIKE '%glad%' OR LOWER(gloss) LIKE '%rejoice%'
        OR LOWER(gloss) LIKE '%merry%' OR LOWER(gloss) LIKE '%joy%')
      AND COALESCE(delete_flagged,0)=0
    ORDER BY cluster_code, strongs_number
    LIMIT 30
"""):
    print(f"  mti={r['id']:<5} {r['strongs_number']:<8} {r['transliteration']!s:<14} {r['gloss']!s:<22} cluster={r['cluster_code']}")
