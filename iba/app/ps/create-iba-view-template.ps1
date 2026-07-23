param(
    [string]$DbPath = "C:\Bible_study_projects\iba\app\db\iba.db",
    [string]$ViewName = "vw_cfg_table_catalogue",
    [switch]$Apply,
    [switch]$ReplaceExisting
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $DbPath)) {
    throw "Database file not found: $DbPath"
}

$viewSql = @'
CREATE VIEW vw_cfg_table_catalogue AS
SELECT
    name,
    grain,
    use
FROM cfg_table
ORDER BY name;
'@

$pythonCode = @'
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


def main(db_path: str, view_name: str, apply_flag: str, replace_existing_flag: str, view_sql: str):
    apply_mode = apply_flag.lower() == 'true'
    replace_existing = replace_existing_flag.lower() == 'true'

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    try:
        cur.execute('BEGIN')

        if replace_existing:
            cur.execute(f'DROP VIEW IF EXISTS {q(view_name)}')

        cur.execute(view_sql)

        stored_sql = fetch_view_sql(cur, view_name)
        if not stored_sql:
            raise RuntimeError(f'View {view_name!r} was not found in sqlite_master after CREATE VIEW')

        cur.execute(f'SELECT * FROM {q(view_name)} LIMIT 0')

        if apply_mode:
            conn.commit()
            print(f'APPLIED: {view_name}')
        else:
            conn.rollback()
            print(f'DRY-RUN ONLY: {view_name}')

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

$result = $pythonCode | python - $DbPath $ViewName $Apply.IsPresent $ReplaceExisting.IsPresent $viewSql
$result
