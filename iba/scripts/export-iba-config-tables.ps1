param(
    [string]$DbPath = "C:\Bible_study_projects\iba\app\db\iba.db",
    [string]$OutDir = "C:\Bible_study_projects\iba\app\config",
    [string]$ReportFileName = "cfg-table-csv-index.md",
    [string]$TableLike = "cfg_%"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $DbPath)) {
    throw "Database file not found: $DbPath"
}

if (-not (Test-Path -LiteralPath $OutDir)) {
    New-Item -ItemType Directory -Path $OutDir -Force | Out-Null
}

$outFile = Join-Path $OutDir $ReportFileName

$pythonCode = @'
import sqlite3
import sys
from datetime import datetime, timezone
import csv
import os


def quote_ident(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'


def esc_cell(value) -> str:
    if value is None:
        return ""
    s = str(value)
    s = s.replace("|", "\\|")
    s = s.replace("\n", " ")
    return s


def markdown_table(headers, rows):
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("|" + "---|" * len(headers))
    for row in rows:
        out.append("| " + " | ".join(esc_cell(v) for v in row) + " |")
    return out


def write_table_csv(cur, out_dir: str, table_name: str):
    q_table = quote_ident(table_name)
    cols = [dict(r) for r in cur.execute(f"PRAGMA table_info({q_table})").fetchall()]
    col_names = [c['name'] for c in cols]
    csv_name = f"{table_name}.csv"
    csv_path = os.path.join(out_dir, csv_name)

    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(col_names)
        for row in cur.execute(f"SELECT * FROM {q_table}").fetchall():
            writer.writerow(list(row))

    row_count = cur.execute(f"SELECT COUNT(*) AS n FROM {q_table}").fetchone()['n']
    return table_name, csv_name, len(col_names), row_count


def build_report(db_path: str, out_dir: str, table_like: str) -> str:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    tables = [
        r["name"]
        for r in cur.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table' AND name LIKE ?
            ORDER BY name
            """,
            (table_like,),
        ).fetchall()
    ]

    generated_at = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    lines = []
    lines.append('# IBA Config Tables CSV Index')
    lines.append('')
    lines.append(f'- Database: {db_path}')
    lines.append(f'- Output folder: {out_dir}')
    lines.append(f'- Generated (UTC): {generated_at}')
    lines.append(f'- Table filter: {table_like}')
    lines.append(f'- Matched tables: {len(tables)}')
    lines.append('')

    if not tables:
        lines.append('No tables matched the filter.')
        conn.close()
        return '\n'.join(lines) + '\n'

    # Remove previous cfg CSV dumps so each run leaves a clean overwrite set.
    for name in os.listdir(out_dir):
        lower_name = name.lower()
        if lower_name.startswith('cfg_') and lower_name.endswith('.csv'):
            os.remove(os.path.join(out_dir, name))

    lines.append('## Table to CSV Mapping')
    lines.append('')
    lines.extend(markdown_table(
        ['table', 'csv_file', 'columns', 'rows'],
        [write_table_csv(cur, out_dir, t) for t in tables],
    ))
    lines.append('')

    conn.close()
    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    db_path = sys.argv[1]
    out_path = sys.argv[2]
    table_like = sys.argv[3]
    out_dir = sys.argv[4]
    content = build_report(db_path, out_dir, table_like)
    with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print(out_path)
'@

$createdPath = $pythonCode | python - $DbPath $outFile $TableLike $OutDir
$createdPath = $createdPath.Trim()
Write-Output "Config dump written: $createdPath"
