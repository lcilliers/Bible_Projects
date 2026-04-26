"""Generate a programme snapshot report.

Produces a markdown snapshot of the inner-being-words research programme:

  1. Summary metrics (registries, statuses, term/verse counts, clusters)
  2. Words by Cluster (all 22 clusters with status indicators)
  3. Phase 1 Excluded Registries
  4. In Progress (Phase 1 or Verse Context)
  5. Alphabetical Index - Registry Words (214 rows)
  6. Alphabetical Index - Strong's Terms (active analytical terms only)

Read-only against `data/bible_research.db`. Output is a self-contained markdown
file - no external assets, no DB writes.

Usage:
    python scripts/generate_programme_snapshot.py
    python scripts/generate_programme_snapshot.py --registry-only
    python scripts/generate_programme_snapshot.py --strongs-only
    python scripts/generate_programme_snapshot.py --out path/to/file.md
    python scripts/generate_programme_snapshot.py --date 20260425

Default output: outputs/markdown/programme-snapshot-{YYYYMMDD}.md
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import sqlite3
import sys

DB_PATH = os.path.join('data', 'bible_research.db')
DEFAULT_OUT_DIR = os.path.join('outputs', 'markdown')

SB_SHORT = {
    'Verse Context Reset': 'VC-Reset',
    'Ready for Analysis': 'Ready',
    'Pre-Analysis Complete': 'PreAn',
    'Analysis Complete': 'Analysis',
    'Session B Complete': 'Done',
}


def vc_icon(s):
    return {'Complete': 'OK', 'In Progress': 'WIP'}.get(s, '-' if s is None else s)


def p1_icon(s):
    return {'Complete': 'OK', 'In Progress': 'WIP', 'Excluded': 'EX'}.get(s, '-' if s is None else s)


def md_escape(s):
    if s is None:
        return ''
    return str(s).replace('|', '\\|').replace('\n', ' ').strip()


def get_schema_version(cur):
    try:
        cur.execute('SELECT version FROM schema_version ORDER BY id DESC LIMIT 1')
        row = cur.fetchone()
        return row['version'] if row else 'unknown'
    except sqlite3.OperationalError:
        return 'unknown'


def fetch_registry_rows(cur):
    cur.execute("""
        SELECT no, word, cluster_assignment, phase1_status, verse_context_status, session_b_status,
               phase1_term_count, phase1_verse_count, unique_term_count, shared_term_count,
               term_sharing_ratio, dimensions, sb_classification, carry_forward, word_synopsis
        FROM word_registry
        ORDER BY no
    """)
    return [dict(r) for r in cur.fetchall()]


def fetch_term_counts(cur):
    cur.execute("""
        SELECT wr.no,
               SUM(CASE WHEN ti.term_owner_type='OWNER' AND ti.delete_flagged=0 THEN 1 ELSE 0 END) terms_owner,
               SUM(CASE WHEN ti.term_owner_type='XREF'  AND ti.delete_flagged=0 THEN 1 ELSE 0 END) terms_xref
        FROM word_registry wr
        LEFT JOIN wa_file_index fi ON fi.word_registry_fk = wr.id
        LEFT JOIN wa_term_inventory ti ON ti.file_id = fi.id
        GROUP BY wr.no
    """)
    return {r['no']: dict(r) for r in cur.fetchall()}


def fetch_verse_counts(cur):
    cur.execute("""
        SELECT wr.no, COUNT(DISTINCT vr.id) verses_active
        FROM word_registry wr
        LEFT JOIN wa_file_index fi ON fi.word_registry_fk = wr.id
        LEFT JOIN wa_term_inventory ti ON ti.file_id = fi.id
            AND ti.term_owner_type='OWNER' AND ti.delete_flagged=0
        LEFT JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged=0
        GROUP BY wr.no
    """)
    return {r['no']: r['verses_active'] for r in cur.fetchall()}


def fetch_strongs_index(cur):
    cur.execute("""
        SELECT mt.strongs_number, mt.transliteration, mt.gloss, mt.language,
               mt.owning_registry_fk, mt.owning_word, mt.status,
               wr.no AS owner_no, wr.word AS owner_registry_word
        FROM mti_terms mt
        LEFT JOIN word_registry wr ON wr.id = mt.owning_registry_fk
        WHERE mt.delete_flagged = 0
          AND mt.status IN ('extracted','extracted_thin','extracted_theological_anchor')
        ORDER BY LOWER(COALESCE(mt.transliteration,'')), mt.strongs_number
    """)
    return [dict(r) for r in cur.fetchall()]


def render(registry_rows, term_counts, verse_counts, strongs_rows,
           snapshot_date, schema_version, include_registry, include_strongs):
    L = []
    L.append('# Programme Snapshot - Inner-Being Words Research')
    L.append('')
    L.append(f'**Snapshot date:** {snapshot_date}  ')
    L.append(f'**Source:** `data/bible_research.db` (schema v{schema_version})  ')
    L.append(f'**Total registries:** {len(registry_rows)}')
    L.append('')

    if include_registry:
        cluster_words = {}
        for r in registry_rows:
            c = r['cluster_assignment'] or '(none)'
            cluster_words.setdefault(c, []).append(r['word'])

        p1c = sum(1 for r in registry_rows if r['phase1_status'] == 'Complete')
        p1ex = sum(1 for r in registry_rows if r['phase1_status'] == 'Excluded')
        p1ip = sum(1 for r in registry_rows if r['phase1_status'] == 'In Progress')
        vcc = sum(1 for r in registry_rows if r['verse_context_status'] == 'Complete')
        vcip = sum(1 for r in registry_rows if r['verse_context_status'] == 'In Progress')
        vcnu = sum(1 for r in registry_rows if r['verse_context_status'] is None)
        sbreset = sum(1 for r in registry_rows if r['session_b_status'] == 'Verse Context Reset')
        sbready = sum(1 for r in registry_rows if r['session_b_status'] == 'Ready for Analysis')
        sbnull = sum(1 for r in registry_rows if r['session_b_status'] is None)

        total_owner = sum((term_counts.get(r['no'], {}) or {}).get('terms_owner', 0) or 0 for r in registry_rows)
        total_xref = sum((term_counts.get(r['no'], {}) or {}).get('terms_xref', 0) or 0 for r in registry_rows)
        total_vers = sum(verse_counts.get(r['no'], 0) or 0 for r in registry_rows)
        n_clusters = len([k for k in cluster_words if k != '(none)'])

        L.append('## Summary')
        L.append('')
        L.append('| Metric | Value |')
        L.append('|---|---|')
        L.append(f'| Registries (total) | {len(registry_rows)} |')
        L.append(f'| Phase 1: Complete / In Progress / Excluded | {p1c} / {p1ip} / {p1ex} |')
        L.append(f'| Verse Context: Complete / In Progress / NULL | {vcc} / {vcip} / {vcnu} |')
        L.append(f'| Session B: VC-Reset / Ready / NULL | {sbreset} / {sbready} / {sbnull} |')
        L.append(f'| OWNER terms (active) | {total_owner} |')
        L.append(f'| XREF terms (active) | {total_xref} |')
        L.append(f'| OWNER verse records (active) | {total_vers} |')
        L.append(f'| Clusters | {n_clusters} |')
        L.append('')
        L.append('## Legend')
        L.append('')
        L.append('- **P1** Phase 1: `OK`=Complete · `WIP`=In Progress · `EX`=Excluded · `-`=NULL')
        L.append('- **VC** Verse Context: `OK`=Complete · `WIP`=In Progress · `-`=NULL (excluded or out-of-scope)')
        L.append('- **SB** Session B short codes: VC-Reset · Ready · PreAn · Analysis · Done')
        L.append('- **Terms (O/X)** = active OWNER / XREF term counts · **Verses** = active OWNER verse records')
        L.append('')

        L.append('## Words by Cluster')
        L.append('')
        for c in sorted(cluster_words.keys(), key=lambda x: (x == '(none)', x)):
            cluster_rows = [r for r in registry_rows if (r['cluster_assignment'] or '(none)') == c]
            cluster_rows.sort(key=lambda r: r['no'])
            label = c if c != '(none)' else 'Unclustered'
            L.append(f'### {label} ({len(cluster_rows)} words)')
            L.append('')
            L.append('| # | Word | P1 | VC | SB | Terms (O/X) | Verses | Dimensions |')
            L.append('|---:|---|:--:|:--:|---|---:|---:|---|')
            for r in cluster_rows:
                tc = term_counts.get(r['no'], {}) or {}
                sb_short = SB_SHORT.get(r['session_b_status'], '-' if r['session_b_status'] is None else r['session_b_status'])
                dims = (r['dimensions'] or '').strip().replace('\n', ' ').replace('|', '/')
                if len(dims) > 60:
                    dims = dims[:57] + '...'
                L.append(
                    f"| {r['no']} | {r['word']} | {p1_icon(r['phase1_status'])} | "
                    f"{vc_icon(r['verse_context_status'])} | {sb_short} | "
                    f"{tc.get('terms_owner', 0)}/{tc.get('terms_xref', 0)} | "
                    f"{verse_counts.get(r['no'], 0)} | {dims} |"
                )
            L.append('')

        excluded = [r for r in registry_rows if r['phase1_status'] == 'Excluded']
        L.append('## Phase 1 Excluded Registries')
        L.append('')
        L.append(f'_{len(excluded)} registries excluded from automation (no STEP extract; no analysis pipeline)._')
        L.append('')
        L.append('| # | Word | Cluster |')
        L.append('|---:|---|---|')
        for r in excluded:
            L.append(f"| {r['no']} | {r['word']} | {r['cluster_assignment'] or '-'} |")
        L.append('')

        in_prog = [r for r in registry_rows
                   if r['phase1_status'] == 'In Progress' or r['verse_context_status'] == 'In Progress']
        if in_prog:
            L.append('## In Progress')
            L.append('')
            for r in in_prog:
                L.append(
                    f"- **{r['no']} {r['word']}** ({r['cluster_assignment']}) - "
                    f"P1={r['phase1_status']}, VC={r['verse_context_status']}"
                )
            L.append('')

        L.append('## Alphabetical Index - Registry Words')
        L.append('')
        alpha = sorted(registry_rows, key=lambda r: (r['word'] or '').lower())
        L.append('| Word | # | Cluster | P1 | VC |')
        L.append('|---|---:|---|:--:|:--:|')
        for r in alpha:
            L.append(
                f"| {r['word']} | {r['no']} | {r['cluster_assignment'] or '-'} | "
                f"{p1_icon(r['phase1_status'])} | {vc_icon(r['verse_context_status'])} |"
            )
        L.append('')

    if include_strongs:
        L.append("## Alphabetical Index - Strong's Terms")
        L.append('')
        L.append(
            f"_{len(strongs_rows)} active analytical terms "
            "(status: extracted, extracted_thin, extracted_theological_anchor; delete_flagged=0). "
            "Sorted alphabetically by transliteration. "
            "**English word** = canonical gloss from `mti_terms.gloss`. "
            "**Owner registry** = the registry that owns this Strong's number "
            "(`mti_terms.owning_registry_fk` -> `word_registry`)._"
        )
        L.append('')
        L.append('| Transliteration | Strong | Lang | English Word (gloss) | Owner Registry |')
        L.append('|---|---|:--:|---|---|')
        for s in strongs_rows:
            lang = (s['language'] or '')[:1].upper()
            if s.get('owner_no') is not None:
                owner = f"{s['owner_no']} {s['owner_registry_word']}"
            else:
                owner = s['owning_word'] or '-'
            L.append(
                f"| {md_escape(s['transliteration']) or '-'} | "
                f"{md_escape(s['strongs_number'])} | {lang} | "
                f"{md_escape(s['gloss']) or '-'} | {md_escape(owner)} |"
            )
        L.append('')

    return '\n'.join(L)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a programme snapshot markdown report.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--registry-only', action='store_true',
                       help="Emit registry sections only; omit Strong's index.")
    group.add_argument('--strongs-only', action='store_true',
                       help="Emit Strong's index only; omit registry sections.")
    parser.add_argument('--out', default=None,
                        help='Output path. Default: outputs/markdown/programme-snapshot-{YYYYMMDD}.md')
    parser.add_argument('--date', default=None,
                        help='Snapshot date (YYYYMMDD). Default: today.')
    parser.add_argument('--db', default=DB_PATH,
                        help=f'Database path (default: {DB_PATH}).')
    args = parser.parse_args()

    if args.date:
        try:
            snapshot_dt = dt.datetime.strptime(args.date, '%Y%m%d').date()
        except ValueError:
            sys.exit(f"--date must be YYYYMMDD; got {args.date!r}")
    else:
        snapshot_dt = dt.date.today()
    snapshot_str = snapshot_dt.isoformat()
    date_compact = snapshot_dt.strftime('%Y%m%d')

    if args.out:
        out_path = args.out
    else:
        out_path = os.path.join(DEFAULT_OUT_DIR, f'programme-snapshot-{date_compact}.md')

    if not os.path.exists(args.db):
        sys.exit(f"Database not found: {args.db}")

    include_registry = not args.strongs_only
    include_strongs = not args.registry_only

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    try:
        cur = conn.cursor()
        schema_version = get_schema_version(cur)
        registry_rows = fetch_registry_rows(cur) if include_registry else []
        term_counts = fetch_term_counts(cur) if include_registry else {}
        verse_counts = fetch_verse_counts(cur) if include_registry else {}
        strongs_rows = fetch_strongs_index(cur) if include_strongs else []
    finally:
        conn.close()

    md = render(registry_rows, term_counts, verse_counts, strongs_rows,
                snapshot_str, schema_version, include_registry, include_strongs)

    os.makedirs(os.path.dirname(out_path) or '.', exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(md)

    line_count = md.count('\n') + 1
    print(f'Wrote: {out_path}')
    print(f'Lines: {line_count}')
    if include_registry:
        print(f'Registries: {len(registry_rows)}')
    if include_strongs:
        print(f"Strong's terms: {len(strongs_rows)}")


if __name__ == '__main__':
    main()
