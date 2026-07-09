"""Apply M10 → M10/M10b/M10c 3-way split.

Steps:
  1. INSERT cluster rows for M10b and M10c
  2. UPDATE cluster row M10 (new description / short_name)
  3. UPDATE mti_terms.cluster_code for 17 terms moving to M10b
  4. UPDATE mti_terms.cluster_code for 8 terms moving to M10c
  5. Regenerate gloss strings for M10/M10b/M10c
  6. Verify totals

Pre-check: M10 cluster row has status='Not started' and no derivative work has begun.
Post-check: 88 OWNER terms preserved (63 M10 + 17 M10b + 8 M10c).

Companion: Sessions/Session_Clusters/M10/wa-cluster-M10-split-design-v1-20260522.md
"""
import sqlite3
import sys
import io
import os

if os.name == 'nt':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DB = 'database/bible_research.db'
TODAY = '2026-05-22T00:00:00Z'

# Registry -> target cluster (M10b/M10c only; M10 stays default)
M10B_REGISTRIES = {1, 57, 151, 172}
M10C_REGISTRIES = {41, 86, 115}

# Cluster row metadata for new siblings + revised M10
CLUSTER_ROWS = {
    'M10': {
        'description': 'Sin, Guilt and Transgression',
        'short_name': 'Sin',
        'source': 'meaning_v2',
        'bucket': 'NAMED',
        'status': 'Not started',
        'version': 'v6',
    },
    'M10b': {
        'description': 'Wickedness, Evil and Abomination',
        'short_name': 'Wickedness',
        'source': 'meaning_v2_split_20260522',
        'bucket': 'NAMED',
        'status': 'Not started',
        'version': 'v6',
    },
    'M10c': {
        'description': 'Defilement and Impurity',
        'short_name': 'Defilement',
        'source': 'meaning_v2_split_20260522',
        'bucket': 'NAMED',
        'status': 'Not started',
        'version': 'v6',
    },
}


def regenerate_gloss(cur, cluster_code):
    """Build gloss string from current member terms."""
    rows = cur.execute(
        """SELECT mt.gloss, mt.transliteration FROM mti_terms mt
           WHERE mt.cluster_code = ? AND COALESCE(mt.delete_flagged,0)=0
           ORDER BY mt.gloss, mt.transliteration""",
        (cluster_code,)
    ).fetchall()
    parts = []
    for gloss, tr in rows:
        if gloss and tr:
            parts.append(f'{gloss} ({tr})')
        elif gloss:
            parts.append(gloss)
        elif tr:
            parts.append(tr)
    return ', '.join(parts)


def main():
    dry = '--dry-run' in sys.argv
    conn = sqlite3.connect(DB)
    conn.execute('PRAGMA foreign_keys=ON')
    cur = conn.cursor()

    # Pre-check 1: M10 status
    m10 = cur.execute("SELECT status FROM cluster WHERE cluster_code='M10'").fetchone()
    assert m10 is not None, 'M10 cluster row missing'
    assert m10[0] in ('Not started', 'Not Started'), \
        f"M10 status is {m10[0]!r} — split before analysis only"

    # Pre-check 2: M10b/M10c rows must not already exist
    for code in ('M10b', 'M10c'):
        existing = cur.execute(
            'SELECT cluster_code FROM cluster WHERE cluster_code=?', (code,)
        ).fetchone()
        assert existing is None, f'{code} already exists — split already applied?'

    # Pre-check 3: count current M10 OWNER terms
    base_count = cur.execute(
        "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M10' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    assert base_count == 88, f'Expected 88 M10 OWNER terms, found {base_count}'

    # Collect target term IDs by registry
    rows = cur.execute("""
        SELECT id, owning_registry_fk, transliteration, strongs_number
        FROM mti_terms
        WHERE cluster_code='M10' AND COALESCE(delete_flagged,0)=0
    """).fetchall()
    to_m10b = [r for r in rows if _reg_no(cur, r[1]) in M10B_REGISTRIES]
    to_m10c = [r for r in rows if _reg_no(cur, r[1]) in M10C_REGISTRIES]
    to_m10 = [r for r in rows if r not in to_m10b and r not in to_m10c]

    print(f'Pre-check counts: M10={base_count} (target M10={len(to_m10)}, '
          f'M10b={len(to_m10b)}, M10c={len(to_m10c)})')
    assert len(to_m10b) == 17, f'Expected 17 M10b terms, got {len(to_m10b)}'
    assert len(to_m10c) == 8, f'Expected 8 M10c terms, got {len(to_m10c)}'
    assert len(to_m10) == 63, f'Expected 63 M10 (stay) terms, got {len(to_m10)}'

    print()
    print('--- Step 1+2: cluster rows ---')
    # INSERT M10b
    m10b = CLUSTER_ROWS['M10b']
    print(f'INSERT cluster M10b ({m10b["description"]})')
    # INSERT M10c
    m10c = CLUSTER_ROWS['M10c']
    print(f'INSERT cluster M10c ({m10c["description"]})')
    # UPDATE M10
    m10rev = CLUSTER_ROWS['M10']
    print(f'UPDATE cluster M10 description -> {m10rev["description"]!r}, short_name -> {m10rev["short_name"]!r}')

    print()
    print('--- Step 3: 17 terms -> M10b ---')
    for tid, reg_fk, tr, st in to_m10b:
        print(f'  id={tid:5d} {st:10s} {tr or "":<25s} (reg_no={_reg_no(cur, reg_fk)})')

    print()
    print('--- Step 4: 8 terms -> M10c ---')
    for tid, reg_fk, tr, st in to_m10c:
        print(f'  id={tid:5d} {st:10s} {tr or "":<25s} (reg_no={_reg_no(cur, reg_fk)})')

    if dry:
        print('\nDRY-RUN — no writes performed.')
        conn.close()
        return

    # Live writes
    print('\nApplying writes...')
    # INSERT M10b
    cur.execute("""
        INSERT INTO cluster
        (cluster_code, description, gloss, source, bucket, status, version, last_updated_date, short_name)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, ('M10b', m10b['description'], '', m10b['source'], m10b['bucket'],
          m10b['status'], m10b['version'], TODAY, m10b['short_name']))
    # INSERT M10c
    cur.execute("""
        INSERT INTO cluster
        (cluster_code, description, gloss, source, bucket, status, version, last_updated_date, short_name)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, ('M10c', m10c['description'], '', m10c['source'], m10c['bucket'],
          m10c['status'], m10c['version'], TODAY, m10c['short_name']))
    # UPDATE M10
    cur.execute("""
        UPDATE cluster
        SET description=?, short_name=?, last_updated_date=?
        WHERE cluster_code='M10'
    """, (m10rev['description'], m10rev['short_name'], TODAY))

    # UPDATE mti_terms.cluster_code -> M10b
    b_ids = [r[0] for r in to_m10b]
    cur.execute(
        f"UPDATE mti_terms SET cluster_code='M10b', last_changed=? "
        f"WHERE id IN ({','.join('?'*len(b_ids))})",
        [TODAY] + b_ids
    )
    # UPDATE mti_terms.cluster_code -> M10c
    c_ids = [r[0] for r in to_m10c]
    cur.execute(
        f"UPDATE mti_terms SET cluster_code='M10c', last_changed=? "
        f"WHERE id IN ({','.join('?'*len(c_ids))})",
        [TODAY] + c_ids
    )

    # Regenerate gloss for all three
    for code in ('M10', 'M10b', 'M10c'):
        new_gloss = regenerate_gloss(cur, code)
        cur.execute('UPDATE cluster SET gloss=? WHERE cluster_code=?', (new_gloss, code))
        print(f'  gloss[{code}]: {len(new_gloss)} chars')

    conn.commit()

    # Post-check
    print('\n--- Post-check ---')
    for code in ('M10', 'M10b', 'M10c'):
        n = cur.execute(
            "SELECT COUNT(*) FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
            (code,)
        ).fetchone()[0]
        print(f'  {code}: {n} OWNER terms')
    total = cur.execute(
        "SELECT COUNT(*) FROM mti_terms WHERE cluster_code IN ('M10','M10b','M10c') "
        "AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    assert total == 88, f'Total drifted: {total} (expected 88)'
    print(f'  TOTAL preserved: {total} (88 expected)')

    conn.close()
    print('\nDone.')


_REG_CACHE = {}


def _reg_no(cur, registry_fk):
    """Map word_registry.id -> word_registry.no, cached."""
    if not _REG_CACHE:
        _REG_CACHE.update({
            r[0]: r[1]
            for r in cur.execute('SELECT id, no FROM word_registry').fetchall()
        })
    return _REG_CACHE[registry_fk]


if __name__ == '__main__':
    main()
