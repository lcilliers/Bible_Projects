param(
    [string]$DbPath = "C:\Bible_study_projects\iba\app\db\iba.db",
    [string]$OutDir = "C:\Bible_study_projects\docs",
    [string]$BaseName = "iba-db-schema-overview"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $DbPath)) {
    throw "Database file not found: $DbPath"
}

if (-not (Test-Path -LiteralPath $OutDir)) {
    New-Item -ItemType Directory -Path $OutDir -Force | Out-Null
}

$dateTag = Get-Date -Format "yyyyMMdd"
$pattern = "^" + [regex]::Escape($BaseName) + "-v(\d+)-\d{8}\.md$"
$existing = Get-ChildItem -LiteralPath $OutDir -File -Filter "$BaseName-v*-*.md"
$maxVersion = 0

foreach ($file in $existing) {
    $m = [regex]::Match($file.Name, $pattern)
    if ($m.Success) {
        $v = [int]$m.Groups[1].Value
        if ($v -gt $maxVersion) {
            $maxVersion = $v
        }
    }
}

$nextVersion = $maxVersion + 1
$outFile = Join-Path $OutDir ("{0}-v{1}-{2}.md" -f $BaseName, $nextVersion, $dateTag)

$pythonCode = @'
import sqlite3
import sys
from datetime import datetime, timezone


def quote_ident(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'


def fetch_rows(cur, sql, params=()):
    return [dict(r) for r in cur.execute(sql, params).fetchall()]


def index_columns(cur, table_name: str, index_name: str):
    # index_xinfo covers expression/hidden columns; fallback to index_info when needed
    rows = fetch_rows(cur, f"PRAGMA index_xinfo({quote_ident(index_name)})")
    if not rows:
        rows = fetch_rows(cur, f"PRAGMA index_info({quote_ident(index_name)})")
    cols = []
    for r in rows:
        # key=1 means part of index key in index_xinfo; index_info doesn't include key
        if 'key' in r and r['key'] == 0:
            continue
        col_name = r.get('name')
        if col_name is None:
            col_name = "<expression>"
        cols.append((r.get('seqno', 0), col_name))
    cols.sort(key=lambda x: x[0])
    return [c for _, c in cols]


def build_report(db_path: str) -> str:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    objects = fetch_rows(
        cur,
        """
        SELECT type, name, tbl_name, sql
        FROM sqlite_master
        WHERE type IN ('table', 'view', 'index', 'trigger')
        ORDER BY type, name
        """,
    )

    tables = [o['name'] for o in objects if o['type'] == 'table' and not o['name'].startswith('sqlite_')]
    views = [o['name'] for o in objects if o['type'] == 'view']
    triggers = [o['name'] for o in objects if o['type'] == 'trigger']
    indexes = [o['name'] for o in objects if o['type'] == 'index']

    generated_at = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    lines = []
    lines.append('# IBA DB Schema Overview')
    lines.append('')
    lines.append(f'- Database: {db_path}')
    lines.append(f'- Generated (UTC): {generated_at}')
    lines.append(f'- Tables: {len(tables)}')
    lines.append(f'- Views: {len(views)}')
    lines.append(f'- Triggers: {len(triggers)}')
    lines.append(f'- Indexes: {len(indexes)}')
    lines.append('')

    lines.append('## Tables')
    lines.append('')

    for table in tables:
        cols = fetch_rows(cur, f"PRAGMA table_info({quote_ident(table)})")
        fks = fetch_rows(cur, f"PRAGMA foreign_key_list({quote_ident(table)})")
        idxs = fetch_rows(cur, f"PRAGMA index_list({quote_ident(table)})")

        lines.append(f'### {table}')
        lines.append('')

        pk_cols = [c['name'] for c in sorted(cols, key=lambda c: c['pk']) if c['pk'] > 0]
        lines.append(f'- Columns: {len(cols)}')
        lines.append(f"- Primary key: {', '.join(pk_cols) if pk_cols else '(none)'}")
        lines.append(f"- Foreign keys: {len(fks)}")
        lines.append(f"- Indexes: {len(idxs)}")
        lines.append('')

        lines.append('| Column | Type | Not Null | Default | PK Ordinal |')
        lines.append('|---|---|---:|---|---:|')
        for c in cols:
            col_type = c['type'] if c['type'] else '(unspecified)'
            default = c['dflt_value'] if c['dflt_value'] is not None else ''
            lines.append(
                f"| {c['name']} | {col_type} | {c['notnull']} | {default} | {c['pk']} |"
            )
        lines.append('')

        if fks:
            lines.append('Foreign keys:')
            lines.append('')
            lines.append('| From | To Table | To Column | On Update | On Delete | Match |')
            lines.append('|---|---|---|---|---|---|')
            for fk in fks:
                lines.append(
                    f"| {fk['from']} | {fk['table']} | {fk['to']} | {fk['on_update']} | {fk['on_delete']} | {fk['match']} |"
                )
            lines.append('')

        if idxs:
            lines.append('Indexes:')
            lines.append('')
            lines.append('| Name | Unique | Origin | Partial | Columns |')
            lines.append('|---|---:|---|---:|---|')
            for idx in idxs:
                idx_name = idx['name']
                idx_cols = index_columns(cur, table, idx_name)
                lines.append(
                    f"| {idx_name} | {idx['unique']} | {idx['origin']} | {idx['partial']} | {', '.join(idx_cols) if idx_cols else '(none)'} |"
                )
            lines.append('')

    lines.append('## Views')
    lines.append('')
    if not views:
        lines.append('- None')
    else:
        for v in views:
            row = cur.execute(
                "SELECT sql FROM sqlite_master WHERE type='view' AND name=?", (v,)
            ).fetchone()
            view_sql = (row['sql'] or '').replace('\n', ' ')
            lines.append(f'- {v}: {view_sql}')
    lines.append('')

    lines.append('## Triggers')
    lines.append('')
    if not triggers:
        lines.append('- None')
    else:
        for t in triggers:
            row = cur.execute(
                "SELECT sql FROM sqlite_master WHERE type='trigger' AND name=?", (t,)
            ).fetchone()
            trigger_sql = (row['sql'] or '').replace('\n', ' ')
            lines.append(f'- {t}: {trigger_sql}')
    lines.append('')

    conn.close()
    return '\n'.join(lines)


if __name__ == '__main__':
    db_path = sys.argv[1]
    out_path = sys.argv[2]
    content = build_report(db_path)
    with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print(out_path)
'@

$createdPath = $pythonCode | python - $DbPath $outFile
$createdPath = $createdPath.Trim()
Write-Output "Schema report written: $createdPath"
