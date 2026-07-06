"""Read-only: for each of the 97 gate1 orphan strongs, find its natural registry home.

Classifies each strong by what already exists in the (rolled-back) live DB:
  - active OWNER wa_term_inventory row      -> Group A (home registry known)
  - XREF-only wa_term_inventory row         -> Group B (cross-ref home known, needs OWNER promotion)
  - no inventory row at all                 -> Group C (truly new; needs registry assignment)
Also reports any active/deleted mti_terms for the strong and candidate word_registry
words matching the gloss, to support the per-strong registry proposal.

Source of the 97 strongs+glosses = the safety backup taken before rollback.
Emits JSON to stdout. No writes.
"""
import sqlite3, json, sys

LIVE = 'database/bible_research.db'
BK   = 'backups/bible_research.pre-gate1-ROLLBACK-20260706T141152Z.db'

def base(s):
    # strip a trailing sub-entry letter (H0205H, H6121A) to the base strong
    return s[:-1] if (len(s) > 1 and s[-1].isalpha() and s[0] in 'HG') else s

bk = sqlite3.connect(BK); bk.row_factory = sqlite3.Row
terms = [dict(r) for r in bk.execute(
    "SELECT strongs_number, owning_word AS gloss, anchor_note FROM mti_terms "
    "WHERE anchor_note LIKE 'gate1-psalms-2026%' ORDER BY strongs_number").fetchall()]
bk.close()

c = sqlite3.connect(LIVE); c.row_factory = sqlite3.Row

def reg_word(fk):
    if fk is None: return None
    r = c.execute("SELECT word FROM word_registry WHERE id=?", (fk,)).fetchone()
    return r['word'] if r else None

out = []
for t in terms:
    s = t['strongs_number']; b = base(s)
    # inventory rows for exact strong or base strong
    inv = c.execute(
        "SELECT ti.strongs_number, ti.term_owner_type, ti.delete_flagged, ti.word_registry_fk, "
        "       fi.word_registry_fk AS file_reg_fk "
        "FROM wa_term_inventory ti LEFT JOIN wa_file_index fi ON fi.id=ti.file_id "
        "WHERE ti.strongs_number IN (?,?)", (s, b)).fetchall()
    owners = sorted({reg_word(r['word_registry_fk'] or r['file_reg_fk'])
                     for r in inv if (r['term_owner_type']=='OWNER' and not r['delete_flagged'])} - {None})
    xrefs  = sorted({reg_word(r['word_registry_fk'] or r['file_reg_fk'])
                     for r in inv if (r['term_owner_type']=='XREF' and not r['delete_flagged'])} - {None})
    # active mti for this strong (post-rollback, so gate1 rows gone)
    mti = c.execute(
        "SELECT strongs_number, owning_word, owning_registry_fk, delete_flagged, cluster_code "
        "FROM mti_terms WHERE strongs_number IN (?,?)", (s, b)).fetchall()
    mti_active = [dict(m) for m in mti if not m['delete_flagged']]
    mti_deleted = [dict(m) for m in mti if m['delete_flagged']]
    # candidate registry words by gloss token match
    g = (t['gloss'] or '').lower().replace('to ','').replace('be ','').strip()
    cand = [dict(r) for r in c.execute(
        "SELECT id, word FROM word_registry WHERE lower(word) LIKE ?", (f'%{g}%',)).fetchall()] if g else []

    if owners:   group = 'A_owner'
    elif xrefs:  group = 'B_xref'
    else:        group = 'C_new'

    out.append({
        'strong': s, 'gloss': t['gloss'], 'reactivated': t['anchor_note'].endswith('reactivated'),
        'group': group,
        'owner_registries': owners, 'xref_registries': xrefs,
        'mti_active': [{'reg': reg_word(m['owning_registry_fk']), 'cluster': m['cluster_code']} for m in mti_active],
        'mti_deleted': [{'reg': reg_word(m['owning_registry_fk']), 'cluster': m['cluster_code']} for m in mti_deleted],
        'gloss_reg_candidates': [r['word'] for r in cand][:6],
    })

c.close()
summary = {'A_owner': 0, 'B_xref': 0, 'C_new': 0}
for r in out: summary[r['group']] += 1
print(json.dumps({'summary': summary, 'terms': out}, ensure_ascii=False, indent=1))
