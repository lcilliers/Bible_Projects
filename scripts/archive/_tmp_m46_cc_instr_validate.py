"""Validate WA-M46-cc-instructions-v1-20260514: resolve mti_ids, check pre-state."""
import sqlite3, sys, json
sys.stdout.reconfigure(encoding='utf-8')
c = sqlite3.connect('database/bible_research.db')
c.row_factory = sqlite3.Row


def divider(s):
    print(f"\n{'=' * 72}\n  {s}\n{'=' * 72}")


# Action group 1 — T2 → M46 (8 terms by Strong's only)
divider("Action group 1 — T2→M46: resolve mti_ids for 8 Strong's")
ag1 = [
    ("H8082", "sha.men"),
    ("H8080", "sha.man"),
    ("H4924", "mish.man"),
    ("G842",  "autarkēs"),
    ("H5727", "a.dan"),
    ("H7961", "shal.a.nan"),  # VERIFY flagged
    ("H2630", "cha.san"),
    ("G3045", "liparos"),
]
ag1_resolved = []
for strongs, expected_translit in ag1:
    rows = list(c.execute("""SELECT id, strongs_number, transliteration, gloss, cluster_code,
                                    vc_status, md_version, COALESCE(delete_flagged,0) deleted
                             FROM mti_terms
                             WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0""",
                          (strongs,)))
    if len(rows) == 1:
        r = rows[0]
        translit_ok = (r['transliteration'] or '').lower() == expected_translit.lower()
        cluster_ok = r['cluster_code'] == 'T2'
        marker = "✓" if (translit_ok and cluster_ok) else "⚠"
        print(f"  {marker} {strongs:<7} mti={r['id']:<6} '{r['transliteration']}' "
              f"cluster={r['cluster_code']} vc={r['vc_status']} md={r['md_version']}")
        if not translit_ok:
            print(f"      [WARN] expected translit '{expected_translit}', got '{r['transliteration']}'")
        if not cluster_ok:
            print(f"      [WARN] expected cluster T2, got '{r['cluster_code']}'")
        ag1_resolved.append((r['id'], strongs, r['transliteration'], r['cluster_code']))
    elif len(rows) == 0:
        print(f"  ✗ {strongs:<7} NOT FOUND")
    else:
        print(f"  ✗ {strongs:<7} MULTIPLE MATCHES ({len(rows)})")
        for r in rows:
            print(f"      mti={r['id']} '{r['transliteration']}' cluster={r['cluster_code']}")


# Action group 2 — M46 → M22 ke.vud.dah (mti_id=1870 stated)
divider("Action group 2 — M46→M22 ke.vud.dah (mti_id=1870 given)")
r = c.execute("""SELECT id, strongs_number, transliteration, cluster_code, vc_status
                 FROM mti_terms WHERE id=1870""").fetchone()
if r:
    marker = "✓" if (r['strongs_number'] == 'H3520B' and r['cluster_code'] == 'M46') else "⚠"
    print(f"  {marker} mti=1870 {r['strongs_number']} '{r['transliteration']}' "
          f"cluster={r['cluster_code']} vc={r['vc_status']}")
# Verify VCG 3422
vcg = c.execute("""SELECT id, group_code, COALESCE(delete_flagged,0) deleted
                   FROM verse_context_group WHERE id=3422""").fetchone()
print(f"  VCG 3422: group_code='{vcg['group_code']}' deleted={vcg['deleted']}" if vcg else "  VCG 3422 NOT FOUND")
# Verify the 2 verse rows
print("  Verses listed in directive:")
for vc_id in (143931, 143932):
    r = c.execute("""SELECT id, verse_record_id, mti_term_id, group_id,
                            is_relevant, cluster_subgroup_id
                     FROM verse_context WHERE id=?""", (vc_id,)).fetchone()
    if r:
        vr = c.execute("SELECT reference FROM wa_verse_records WHERE id=?", (r['verse_record_id'],)).fetchone()
        ref = vr['reference'] if vr else '?'
        print(f"    vc={r['id']} vr={r['verse_record_id']} ({ref}) mti={r['mti_term_id']} "
              f"group_id={r['group_id']} cluster_subgroup_id={r['cluster_subgroup_id']}")
    else:
        print(f"    vc={vc_id} NOT FOUND")


# Action group 3 — VCG 51 (111-002) migrate; vc_id=58191
divider("Action group 3 — VCG 51 (111-002) migrate M46→M39 (term stays in M46)")
r = c.execute("""SELECT id, strongs_number, transliteration, cluster_code
                 FROM mti_terms WHERE id=111""").fetchone()
print(f"  mti=111 (H1878 da.shen): cluster_code={r['cluster_code']}")
vcg = c.execute("""SELECT id, group_code, SUBSTR(context_description,1,80) AS desc
                   FROM verse_context_group WHERE id=51""").fetchone()
print(f"  VCG 51: group_code='{vcg['group_code']}'  desc={vcg['desc']}")
vc = c.execute("""SELECT id, verse_record_id, mti_term_id, group_id,
                         is_relevant, cluster_subgroup_id
                  FROM verse_context WHERE id=58191""").fetchone()
if vc:
    vr = c.execute("SELECT reference FROM wa_verse_records WHERE id=?", (vc['verse_record_id'],)).fetchone()
    print(f"  vc=58191 vr={vc['verse_record_id']} ({vr['reference'] if vr else '?'}) "
          f"mti={vc['mti_term_id']} group_id={vc['group_id']} "
          f"cluster_subgroup_id={vc['cluster_subgroup_id']}")
# How many vc rows belong to vcg_id=51?
n_in_51 = c.execute("SELECT COUNT(*) FROM verse_context WHERE group_id=51 AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f"  Total active vc rows in group_id=51: {n_in_51}")


# Action group 4 — autarkeia (G841) shared with M46
divider("Action group 4 — autarkeia G841 VCNEW_SHARED for M46")
r = c.execute("""SELECT id, strongs_number, transliteration, gloss, cluster_code, vc_status
                 FROM mti_terms WHERE strongs_number='G841'""").fetchone()
if r:
    print(f"  G841 {r['transliteration']!r}: mti={r['id']} cluster={r['cluster_code']} vc={r['vc_status']}")
else:
    print(f"  G841 NOT FOUND in mti_terms")
# Verify 1 Tim 6:6 and 2 Cor 9:8 wa_verse_records exist for G841
for ref in ("1Ti 6:6", "1Tim 6:6", "2Co 9:8", "2Cor 9:8"):
    rows = list(c.execute("""SELECT id, reference, mti_term_id FROM wa_verse_records
                             WHERE reference LIKE ? AND COALESCE(delete_flagged,0)=0
                             LIMIT 6""", (f"%{ref}%",)))
    if rows:
        print(f"  Search '{ref}': {len(rows)} matches")
        for vr in rows[:3]:
            mt = c.execute("SELECT strongs_number FROM mti_terms WHERE id=?", (vr['mti_term_id'],)).fetchone()
            print(f"    vr={vr['id']} '{vr['reference']}' mti={vr['mti_term_id']} ({mt['strongs_number'] if mt else '?'})")


# M46 current state
divider("M46 current state pre-application")
n = c.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M46' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f"  M46 active terms: {n}")
for r in c.execute("""SELECT id, strongs_number, transliteration, gloss
                      FROM mti_terms WHERE cluster_code='M46' AND COALESCE(delete_flagged,0)=0
                      ORDER BY strongs_number"""):
    print(f"    mti={r['id']:<5} {r['strongs_number']:<8} {r['transliteration']:<14} {(r['gloss'] or '')[:30]}")


# T2 current
divider("T2 current state pre-application (will lose 8 terms)")
n_t2 = c.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code='T2' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f"  T2 active terms: {n_t2}")
