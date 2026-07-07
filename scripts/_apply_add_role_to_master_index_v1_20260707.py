"""_apply_add_role_to_master_index_v1_20260707.py — M64: add per-span `role` to the master index
and backfill it verbatim from ve_lexical (ve_nr=115).

Design + debate: verse-analysis/_reports/wa-master-index-role-column-design-and-debate-20260707.md

Adds columns to verse_span_index: role, role_provenance, role_set_at, role_source_ve_id.
Backfill (verbatim; these roles are known-imperfect, imported for analysis):
  - span with exactly ONE active ve_nr=115 role  -> copy value + source_provenance + ve_lexical.id
  - span with >1 active role (16 conflict spans)  -> role NULL, role_provenance='CONFLICT'
  - span with no active role                      -> left NULL (unassessed)
Records schema_version M64 -> 3.38.0 (append to migration_history, bump version_code).

Idempotent: re-run re-backfills in place (columns created only if absent; M64 appended only once).
Read-only unless --live.
"""
import sqlite3, os, sys, json, shutil, datetime

DB = os.path.join('database', 'bible_research.db')
LIVE = '--live' in sys.argv
NOW = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

def main():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row; cur = c.cursor()

    cols = [r['name'] for r in cur.execute('PRAGMA table_info(verse_span_index)')]
    have_cols = all(x in cols for x in ('role', 'role_provenance', 'role_set_at', 'role_source_ve_id'))

    # counts for the plan
    total_spans = cur.execute('SELECT COUNT(*) n FROM verse_span_index').fetchone()['n']
    single = cur.execute('''SELECT COUNT(*) n FROM (
        SELECT verse_span_id FROM ve_lexical WHERE ve_nr=115 AND COALESCE(delete_flagged,0)=0 AND verse_span_id IS NOT NULL
        GROUP BY verse_span_id HAVING COUNT(*)=1)''').fetchone()['n']
    conflict = cur.execute('''SELECT COUNT(*) n FROM (
        SELECT verse_span_id FROM ve_lexical WHERE ve_nr=115 AND COALESCE(delete_flagged,0)=0 AND verse_span_id IS NOT NULL
        GROUP BY verse_span_id HAVING COUNT(*)>1)''').fetchone()['n']

    print('M64 add role to master index')
    print('  verse_span_index total spans   : {}'.format(total_spans))
    print('  columns already present        : {}'.format(have_cols))
    print('  spans with 1 active role (fill): {}'.format(single))
    print('  spans with >1 role (CONFLICT)  : {}'.format(conflict))
    print('  spans left NULL (unassessed)   : {}'.format(total_spans - single - conflict))

    if not LIVE:
        print('\nDRY-RUN. Re-run with --live.')
        c.close(); return

    # pre-op backup
    bpath = 'backups/bible_research.pre-role-master-{}.db'.format(NOW.replace(':', '').replace('-', ''))
    os.makedirs('backups', exist_ok=True)
    shutil.copy2(DB, bpath)
    print('  backup: {}'.format(bpath))

    # 1. schema
    if not have_cols:
        for ddl in (
            "ALTER TABLE verse_span_index ADD COLUMN role TEXT",
            "ALTER TABLE verse_span_index ADD COLUMN role_provenance TEXT",
            "ALTER TABLE verse_span_index ADD COLUMN role_set_at TEXT",
            "ALTER TABLE verse_span_index ADD COLUMN role_source_ve_id INTEGER",
        ):
            cur.execute(ddl)
        print('  columns added.')
    else:
        print('  columns already present; skipping ALTER.')

    # 2. reset role fields (idempotent re-backfill), then fill
    cur.execute("UPDATE verse_span_index SET role=NULL, role_provenance=NULL, role_set_at=NULL, role_source_ve_id=NULL")

    # single-role spans -> verbatim copy
    cur.execute("""
        UPDATE verse_span_index
        SET role = (SELECT x.value FROM ve_lexical x
                    WHERE x.verse_span_id = verse_span_index.id AND x.ve_nr=115 AND COALESCE(x.delete_flagged,0)=0),
            role_provenance = (SELECT x.source_provenance FROM ve_lexical x
                    WHERE x.verse_span_id = verse_span_index.id AND x.ve_nr=115 AND COALESCE(x.delete_flagged,0)=0),
            role_source_ve_id = (SELECT x.id FROM ve_lexical x
                    WHERE x.verse_span_id = verse_span_index.id AND x.ve_nr=115 AND COALESCE(x.delete_flagged,0)=0),
            role_set_at = ?
        WHERE id IN (
            SELECT verse_span_id FROM ve_lexical
            WHERE ve_nr=115 AND COALESCE(delete_flagged,0)=0 AND verse_span_id IS NOT NULL
            GROUP BY verse_span_id HAVING COUNT(*)=1)
    """, (NOW,))
    filled = cur.execute("SELECT COUNT(*) n FROM verse_span_index WHERE role IS NOT NULL").fetchone()['n']

    # conflict spans -> flag
    cur.execute("""
        UPDATE verse_span_index
        SET role=NULL, role_provenance='CONFLICT', role_set_at=?
        WHERE id IN (
            SELECT verse_span_id FROM ve_lexical
            WHERE ve_nr=115 AND COALESCE(delete_flagged,0)=0 AND verse_span_id IS NOT NULL
            GROUP BY verse_span_id HAVING COUNT(*)>1)
    """, (NOW,))
    flagged = cur.execute("SELECT COUNT(*) n FROM verse_span_index WHERE role_provenance='CONFLICT'").fetchone()['n']

    # 3. schema_version M64 -> 3.38.0
    row = cur.execute('SELECT id, migration_history FROM schema_version ORDER BY rowid DESC LIMIT 1').fetchone()
    hist = json.loads(row['migration_history'])
    if not any(e.get('version') == 'M64' for e in hist):
        hist.append({"version": "M64",
                     "description": "Add per-span role to master index (verse_span_index.role/role_provenance/role_set_at/role_source_ve_id); backfill verbatim from ve_lexical ve_nr=115 (single-role spans; 16 conflicts flagged). 3.37.0 -> 3.38.0",
                     "applied_at": NOW})
        cur.execute('UPDATE schema_version SET version_code=?, applied_at=?, migration_history=? WHERE id=?',
                    ('3.38.0', NOW, json.dumps(hist), row['id']))
        print('  schema_version -> 3.38.0 (M64 recorded).')
    else:
        print('  M64 already in schema_version; not re-appending.')

    c.commit()
    print('  LIVE: role filled on {} spans; {} flagged CONFLICT.'.format(filled, flagged))
    c.close()

if __name__ == '__main__':
    main()
