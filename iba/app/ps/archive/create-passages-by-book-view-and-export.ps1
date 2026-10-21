param(
    [string]$DbPath = "C:\Bible_study_projects\iba\app\db\iba.db",
    [string]$ViewName = "vw_passages_by_book",
    [string]$Book = "Rom",
    [string]$OutDir = "C:\Bible_study_projects\iba\app\config\views",
    [string]$CsvFileName,
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

if (-not $CsvFileName) {
    $CsvFileName = "$ViewName-$Book.csv"
}
$csvPath = Join-Path $OutDir $CsvFileName

# Generic, book-agnostic view: one row per verse-within-passage.
#   book | all passage.* columns | verse_reference | verse_text
#   | candidate_chars = comma-delimited DISTINCT candidate tags for that verse
$selectSql = @'
SELECT
    p.*,
    v.reference AS verse_reference,
    v.text      AS verse_text,
    (
        SELECT GROUP_CONCAT(cc.candidate_tag, ', ')
        FROM (
            SELECT DISTINCT sc.candidate_tag
            FROM span s
            JOIN span_candidate sc ON sc.span_id = s.id AND sc.deleted = 0
            WHERE s.verse_id = v.id AND s.deleted = 0
            ORDER BY sc.candidate_tag
        ) cc
    ) AS candidate_chars
FROM passage p
JOIN verse_passage vp ON vp.passage_id = p.id AND vp.deleted = 0
JOIN verse v          ON v.id = vp.verse_id AND v.deleted = 0
WHERE p.deleted = 0
ORDER BY p.book, p.start_chapter, p.start_verse, v.id
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


def export_csv(cur, query: str, params, csv_path: str):
    rows = cur.execute(query, params).fetchall()
    headers = [d[0] for d in cur.description]
    with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for row in rows:
            writer.writerow(list(row))
    return len(rows), headers


def main(db_path, view_name, create_view_sql, csv_path, book, dry_run_flag):
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
            raise RuntimeError(f'View {view_name!r} not found in sqlite_master after CREATE VIEW')

        export_query = f'SELECT * FROM {q(view_name)} WHERE book = ?'
        preview_rows = cur.execute(export_query + ' LIMIT 5', (book,)).fetchall()
        preview_cols = [d[0] for d in cur.description]

        if dry_run:
            conn.rollback()
            print(f'DRY-RUN ONLY: {view_name}  (book={book})')
            print(f'PREVIEW ROWS: {len(preview_rows)}')
            print('COLUMNS: ' + ', '.join(preview_cols))
            print('---VIEW-SQL---')
            print(stored_sql)
            return

        conn.commit()
        count, headers = export_csv(cur, export_query, (book,), csv_path)
        print(f'APPLIED: {view_name}')
        print(f'BOOK: {book}')
        print(f'CSV: {csv_path}')
        print(f'EXPORTED ROWS: {count}')
        print('CSV COLUMNS: ' + ', '.join(headers))
        print('---VIEW-SQL---')
        print(stored_sql)
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == '__main__':
    main(*sys.argv[1:7])
'@

$result = $pythonCode | python - $DbPath $ViewName $createViewSql $csvPath $Book $DryRun.IsPresent
$result
