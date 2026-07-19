param(
    [string]$DbPath = "C:\Bible_study_projects\iba\app\db\iba.db",
    [string]$ViewName = "vw_passage_verse_top10",
    [string]$OutDir = "C:\Bible_study_projects\iba\app\config",
    [string]$CsvFileName = "vw_passage_verse_top10.csv",
    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $DbPath)) {
    throw "Database file not found: $DbPath"
}

if (-not (Test-Path -LiteralPath $OutDir)) {
    New-Item -ItemType Directory -Path $OutDir -Force | Out-Null
}

$csvPath = Join-Path $OutDir $CsvFileName

$selectSql = @'
SELECT
    p.*, 
    v.reference,
    v.preview
FROM passage p
INNER JOIN verse_passage vp ON p.id = vp.passage_id
INNER JOIN verse v ON vp.verse_id = v.id
LIMIT 10
'@

$createViewSql = @"
CREATE VIEW $ViewName AS
$selectSql;
"@

$pythonCode = @'
import csv
import sqlite3
import sys


def q(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'


def fetch_view_sql(cur, view_name: str):
    row = cur.execute(
        "SELECT sql FROM sqlite_master WHERE type='view' AND name=?",
        (view_name,),
    ).fetchone()
    return row[0] if row else None


def export_csv(cur, query: str, csv_path: str):
    rows = cur.execute(query).fetchall()
    headers = [d[0] for d in cur.description]
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for row in rows:
            writer.writerow(list(row))
    return len(rows), headers


def main(db_path: str, view_name: str, create_view_sql: str, csv_path: str, dry_run_flag: str):
    dry_run = dry_run_flag.lower() == 'true'
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    try:
        cur.execute('BEGIN')
        cur.execute(f'DROP VIEW IF EXISTS {q(view_name)}')
        cur.execute(create_view_sql)

        stored_sql = fetch_view_sql(cur, view_name)
        if not stored_sql:
            raise RuntimeError(f'View {view_name!r} was not found in sqlite_master after CREATE VIEW')

        test_query = f'SELECT * FROM {q(view_name)} LIMIT 5'
        test_rows = cur.execute(test_query).fetchall()
        test_columns = [d[0] for d in cur.description]

        if dry_run:
            conn.rollback()
            print(f'DRY-RUN ONLY: {view_name}')
            print(f'TEST ROWS: {len(test_rows)}')
            print('TEST COLUMNS: ' + ', '.join(test_columns))
            print('---VIEW-SQL---')
            print(stored_sql)
            return

        conn.commit()
        export_count, export_headers = export_csv(cur, f'SELECT * FROM {q(view_name)}', csv_path)

        print(f'APPLIED: {view_name}')
        print(f'CSV: {csv_path}')
        print(f'EXPORTED ROWS: {export_count}')
        print('CSV COLUMNS: ' + ', '.join(export_headers))
        print('---VIEW-SQL---')
        print(stored_sql)
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == '__main__':
    main(*sys.argv[1:6])
'@

$result = $pythonCode | python - $DbPath $ViewName $createViewSql $csvPath $DryRun.IsPresent
$result
