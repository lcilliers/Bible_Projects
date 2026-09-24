"""purge.py -- app-wide soft-delete purge audit + execute (escalation #1766, researcher approved
build 2026-09-19: "Approve to build. Do not run a purge as yet."; execute half built 2026-09-24,
escalation #1868, researcher instruction "proceed with the safe to purge"; retire_database added
2026-09-24, researcher ruling "all the finding related tables in research DB should be inactive
and... all the records in those table are no longer relevant and can be purged").

`audit(ctx)` -- read-only. For every table with a registered soft-delete column (`cfg_column.name`
IN `deleted`/`delete_flagged`, across BOTH `iba` and `bible_research`), counts soft-deleted rows;
for any table over `purge.unsafe_check_min_soft_deleted`, checks `cfg_column.fk` for a live row
elsewhere still referencing one of its soft-deleted PKs and flags the table UNSAFE if so. Persists
a report every run (governance.reports_must_persist). Removes nothing.

`execute(ctx)` -- recomputes the same safe/unsafe split fresh (never trusts a cached audit report --
data may have changed since it was written), intersects it with `cfg_write_grant` (writer=
'purge.execute') so only explicitly allow-listed tables are ever touched, then either previews
(`-Preview` default true: counts only, nothing written) or actually deletes every soft-deleted row
in each granted-and-currently-safe table, one transaction per database, and verifies each table
reads back 0 soft-deleted rows afterward. A table that is UNSAFE (or ungranted) is always skipped
and reported as skipped, never silently included. Persists a report every run.

bible_research.db is in scope for both functions -- `cfg_behaviour_rule`
'bible-research-db-excluded-from-iba-results' explicitly exempts registered DB-hygiene/maintenance
utilities (amended 2026-09-24, escalation #1868/#1870) from the general exclusion, since this is
administrative housekeeping, not analytical investigation.
"""

from __future__ import annotations

import pathlib
import sqlite3

from .base import Ctx, Outcome, ok
from ..lib import reportkit


def _soft_delete_tables(conn: sqlite3.Connection, database: str) -> list[tuple[str, str]]:
    return [(r["table_name"], r["name"]) for r in conn.execute(
        "SELECT table_name, name FROM cfg_column WHERE database=? AND name IN "
        "('deleted','delete_flagged') AND inactive=0", (database,))]


def _pk_col(conn: sqlite3.Connection, database: str, table: str) -> str:
    r = conn.execute("SELECT name FROM cfg_column WHERE database=? AND table_name=? AND is_pk=1",
                     (database, table)).fetchone()
    return r["name"] if r else "id"


def _delete_col_for(conn: sqlite3.Connection, database: str, table: str) -> str | None:
    r = conn.execute("SELECT name FROM cfg_column WHERE database=? AND table_name=? AND name IN "
                     "('deleted','delete_flagged') AND inactive=0", (database, table)).fetchone()
    return r["name"] if r else None


def _fk_referencing(conn: sqlite3.Connection, database: str, target_table: str) -> list[tuple[str, str]]:
    return [(r["table_name"], r["name"]) for r in conn.execute(
        "SELECT table_name, name FROM cfg_column WHERE database=? AND fk LIKE ?",
        (database, f"{target_table}.%"))]


def _audit_database(iba_conn: sqlite3.Connection, data_conn: sqlite3.Connection, database: str,
                    unsafe_threshold: int) -> dict:
    """`iba_conn` always reads cfg_column (config lives in iba.db regardless of which database's
    data is being audited); `data_conn` reads the actual row counts, which for database='bible_research'
    is a SEPARATE connection to that file (sqlite3 does not enforce FKs across attached databases,
    so this checks logical references via cfg_column.fk, not a real FK constraint)."""
    safe: list[dict] = []
    unsafe: list[dict] = []
    for table, col in _soft_delete_tables(iba_conn, database):
        try:
            cnt = data_conn.execute(f'SELECT COUNT(*) FROM "{table}" WHERE "{col}"=1').fetchone()[0]
        except sqlite3.OperationalError:
            continue
        if cnt == 0:
            continue
        pk = _pk_col(iba_conn, database, table)
        if cnt <= unsafe_threshold:
            safe.append({"table": table, "count": cnt, "pk": pk, "checked": False})
            continue
        refs = _fk_referencing(iba_conn, database, table)
        unsafe_refs = []
        for ref_table, ref_col in refs:
            ref_del_col = _delete_col_for(iba_conn, database, ref_table)
            live_clause = f'AND "{ref_del_col}"=0' if ref_del_col else ""
            try:
                at_risk = data_conn.execute(
                    f'SELECT COUNT(*) FROM "{ref_table}" r WHERE r."{ref_col}" IN '
                    f'(SELECT "{pk}" FROM "{table}" WHERE "{col}"=1) {live_clause}'
                ).fetchone()[0]
            except sqlite3.OperationalError:
                continue
            if at_risk > 0:
                unsafe_refs.append({"ref_table": ref_table, "ref_col": ref_col, "at_risk": at_risk})
        row = {"table": table, "count": cnt, "pk": pk, "checked": True}
        if unsafe_refs:
            row["unsafe_refs"] = unsafe_refs
            unsafe.append(row)
        else:
            safe.append(row)
    return {"safe": safe, "unsafe": unsafe}


def _write_report(ctx: Ctx, results: dict) -> str:
    intro = [
        f"> Generated by `purge.audit` (escalation #1766). Read-only -- counts soft-deleted rows "
        f"per registered soft-delete column across both databases, flags a table UNSAFE to bulk-"
        f"purge if a live row elsewhere still references one of its soft-deleted PKs. Removes "
        f"nothing.",
    ]
    lines_safe = ["| database | table | soft_deleted | pk | dependency-checked |",
                  "|---|---|---|---|---|"]
    lines_unsafe = ["| database | table | soft_deleted | referenced by (table.column) | live rows at risk |",
                    "|---|---|---|---|---|"]
    total_safe = total_unsafe = 0
    for database, r in results.items():
        for row in sorted(r["safe"], key=lambda x: -x["count"]):
            lines_safe.append(f"| {database} | {row['table']} | {row['count']:,} | {row['pk']} | "
                              f"{'yes' if row['checked'] else 'no (at/under threshold)'} |")
            total_safe += 1
        for row in sorted(r["unsafe"], key=lambda x: -x["count"]):
            first = True
            for ref in row["unsafe_refs"]:
                table_cell = f"**{row['table']}**" if first else ""
                db_cell = database if first else ""
                cnt_cell = f"{row['count']:,}" if first else ""
                lines_unsafe.append(f"| {db_cell} | {table_cell} | {cnt_cell} | "
                                    f"{ref['ref_table']}.{ref['ref_col']} | {ref['at_risk']:,} |")
                first = False
            total_unsafe += 1
    sections = {
        "summary": [f"{total_safe} table(s) safe to purge, {total_unsafe} table(s) UNSAFE "
                    f"(live dependency risk)."],
        "safe": lines_safe,
        "unsafe": lines_unsafe if total_unsafe else ["_(none)_"],
    }
    path = ctx.cfg.required_setting("purge.audit_report_path")
    L = reportkit.render_scaffold(ctx.db.conn, "purge.audit", sections, intro=intro)
    written = reportkit.write_report(ctx.db.conn, "purge.audit", pathlib.Path(path), L)
    return str(written)


def audit(ctx: Ctx) -> Outcome:
    threshold = int(ctx.cfg.setting("purge.unsafe_check_min_soft_deleted", 10))
    iba_conn = ctx.db.conn

    results = {}
    results["iba"] = _audit_database(iba_conn, iba_conn, "iba", threshold)

    research_path = ctx.cfg.database_path("bible_research")
    research_conn = sqlite3.connect(research_path)
    research_conn.row_factory = sqlite3.Row
    try:
        results["bible_research"] = _audit_database(iba_conn, research_conn, "bible_research",
                                                     threshold)
    finally:
        research_conn.close()

    report_path = _write_report(ctx, results)
    total_safe = sum(len(r["safe"]) for r in results.values())
    total_unsafe = sum(len(r["unsafe"]) for r in results.values())
    return ok(f"{total_safe} table(s) safe to purge, {total_unsafe} UNSAFE -- report written to "
             f"{report_path}", safe_count=total_safe, unsafe_count=total_unsafe)


def _granted_tables(conn: sqlite3.Connection, database: str) -> set[str]:
    return {r["table_name"] for r in conn.execute(
        "SELECT table_name FROM cfg_write_grant WHERE writer='purge.execute' AND database=? "
        "AND inactive=0", (database,))}


def _write_execute_report(ctx: Ctx, purged: list[dict], skipped: list[dict], preview: bool) -> str:
    intro = [
        f"> Generated by `purge.execute` (escalation #1766/#1868). "
        f"{'PREVIEW -- nothing written.' if preview else 'LIVE run -- rows physically deleted.'} "
        f"Recomputes safety fresh every run (never trusts a cached audit) and only ever touches a "
        f"table both currently safe AND explicitly allow-listed in `cfg_write_grant`.",
    ]
    verb = "would purge" if preview else "purged"
    lines_purged = [f"| database | table | soft_deleted | {verb} | verified 0 remaining |",
                    "|---|---|---|---|---|"]
    for row in sorted(purged, key=lambda x: -x["count"]):
        verified = "" if preview else ("yes" if row.get("verified") else "**NO -- see below**")
        lines_purged.append(f"| {row['database']} | {row['table']} | {row['count']:,} | "
                            f"{row.get('deleted', row['count']):,} | {verified} |")
    lines_skipped = ["| database | table | reason |", "|---|---|---|"]
    for row in sorted(skipped, key=lambda x: (x["database"], x["table"])):
        lines_skipped.append(f"| {row['database']} | {row['table']} | {row['reason']} |")
    total = sum(row.get("deleted", row["count"]) for row in purged)
    sections = {
        "summary": [f"{len(purged)} table(s) {verb}, {total:,} row(s) total; "
                    f"{len(skipped)} table(s) skipped (unsafe and/or not granted)."],
        "purged": lines_purged if purged else ["_(none)_"],
        "skipped": lines_skipped if skipped else ["_(none)_"],
    }
    path = ctx.cfg.required_setting("purge.execute_report_path")
    L = reportkit.render_scaffold(ctx.db.conn, "purge.execute", sections, intro=intro)
    written = reportkit.write_report(ctx.db.conn, "purge.execute", pathlib.Path(path), L)
    return str(written)


def execute(ctx: Ctx) -> Outcome:
    preview_raw = str(ctx.params.get("Preview", "true")).strip().lower()
    preview = preview_raw not in ("false", "0", "no")
    threshold = int(ctx.cfg.setting("purge.unsafe_check_min_soft_deleted", 10))
    iba_conn = ctx.db.conn

    research_path = ctx.cfg.database_path("bible_research")
    research_conn = sqlite3.connect(research_path)
    research_conn.row_factory = sqlite3.Row
    try:
        audits = {
            "iba": _audit_database(iba_conn, iba_conn, "iba", threshold),
            "bible_research": _audit_database(iba_conn, research_conn, "bible_research", threshold),
        }
        conns = {"iba": iba_conn, "bible_research": research_conn}

        purged: list[dict] = []
        skipped: list[dict] = []
        for database, result in audits.items():
            granted = _granted_tables(iba_conn, database)
            data_conn = conns[database]
            for row in result["unsafe"]:
                skipped.append({"database": database, "table": row["table"],
                                "reason": f"UNSAFE -- live dependency risk ({row['count']:,} "
                                          f"soft-deleted)"})
            for row in result["safe"]:
                table = row["table"]
                if table not in granted:
                    skipped.append({"database": database, "table": table,
                                    "reason": f"not in cfg_write_grant for purge.execute "
                                              f"({row['count']:,} soft-deleted, otherwise safe)"})
                    continue
                col = _delete_col_for(iba_conn, database, table)
                entry = {"database": database, "table": table, "count": row["count"]}
                if not preview:
                    cur = data_conn.execute(f'DELETE FROM "{table}" WHERE "{col}"=1')
                    entry["deleted"] = cur.rowcount
                    remaining = data_conn.execute(
                        f'SELECT COUNT(*) FROM "{table}" WHERE "{col}"=1').fetchone()[0]
                    entry["verified"] = remaining == 0
                purged.append(entry)

        if not preview:
            iba_conn.commit()
            research_conn.commit()
    except Exception:
        if not preview:
            iba_conn.rollback()
            research_conn.rollback()
        raise
    finally:
        research_conn.close()

    report_path = _write_execute_report(ctx, purged, skipped, preview)
    total = sum(row.get("deleted", row["count"]) for row in purged)
    verb = "would purge" if preview else "purged"
    unverified = [row["table"] for row in purged if not preview and not row.get("verified")]
    msg = (f"PREVIEW: {len(purged)} table(s), {total:,} row(s) {verb} -- nothing written. "
          f"Re-run with -Live to execute." if preview else
          f"{verb} {total:,} row(s) across {len(purged)} table(s), {len(skipped)} skipped.")
    if unverified:
        msg += f" WARNING: {len(unverified)} table(s) did not verify to 0 remaining: {unverified}."
    return ok(f"{msg} Report: {report_path}", table_count=len(purged), row_count=total,
             skipped_count=len(skipped))


# (database, active_table, column, references_table) -- FK columns on a RETAINED active table
# that point at a table being retired. Nulled (not left dangling) before the retire sweep.
_DANGLING_FK_CLEANUP = [
    ("bible_research", "prose_section", "registry_id", "word_registry"),
    ("bible_research", "wa_prose_section_citations", "cited_finding_id", "wa_session_b_findings"),
    ("bible_research", "wa_prose_section_citations", "cited_qa_link_id", "wa_finding_catalogue_links"),
    ("bible_research", "wa_prose_section_citations", "cited_sd_pointer_id", "wa_session_research_flags"),
]


def _write_retire_report(ctx: Ctx, database: str, cleaned: list[dict], purged: list[dict],
                          preview: bool) -> str:
    intro = [
        f"> Generated by `purge.retire_database` (escalation #1868/#1872/#1873, researcher ruling "
        f"2026-09-24). {'PREVIEW -- nothing written.' if preview else 'LIVE run -- rows physically deleted.'} "
        f"Scope is dynamic: every `{database}` table with `cfg_table.inactive=1` at run time -- "
        f"never a hardcoded list, so this always reflects the live config, not a snapshot.",
    ]
    verb = "would clear" if preview else "cleared"
    lines_cleaned = [f"| retained table.column | references | non-null rows {verb} |",
                     "|---|---|---|"]
    for row in cleaned:
        lines_cleaned.append(f"| {row['table']}.{row['column']} | {row['references']} | "
                            f"{row['count']:,} |")
    lines_purged = [f"| table | rows before | rows {verb} | verified 0 remaining |",
                    "|---|---|---|---|"]
    for row in sorted(purged, key=lambda x: -x["count"]):
        verified = "" if preview else ("yes" if row.get("verified") else "**NO -- see below**")
        lines_purged.append(f"| {row['table']} | {row['count']:,} | "
                            f"{row.get('deleted', row['count']):,} | {verified} |")
    total = sum(row.get("deleted", row["count"]) for row in purged)
    sections = {
        "summary": [f"{database}: {len(purged)} table(s) {verb}, {total:,} row(s) total; "
                    f"{len(cleaned)} retained-table FK column(s) {verb} of dangling references."],
        "fk-cleanup": lines_cleaned if cleaned else ["_(none)_"],
        "purged": lines_purged if purged else ["_(none)_"],
    }
    path = ctx.cfg.required_setting("purge.retire_database_report_path")
    L = reportkit.render_scaffold(ctx.db.conn, "purge.retire_database", sections, intro=intro)
    written = reportkit.write_report(ctx.db.conn, "purge.retire_database", pathlib.Path(path), L)
    return str(written)


def retire_database(ctx: Ctx) -> Outcome:
    preview_raw = str(ctx.params.get("Preview", "true")).strip().lower()
    preview = preview_raw not in ("false", "0", "no")
    database = ctx.params.get("Database", "bible_research")
    iba_conn = ctx.db.conn

    if database == "iba":
        data_conn = iba_conn
        owns_conn = False
    else:
        data_conn = sqlite3.connect(ctx.cfg.database_path(database))
        data_conn.row_factory = sqlite3.Row
        owns_conn = True

    try:
        tables = [r["name"] for r in iba_conn.execute(
            "SELECT name FROM cfg_table WHERE database=? AND inactive=1 ORDER BY name", (database,))]

        cleaned: list[dict] = []
        for db, table, col, ref in _DANGLING_FK_CLEANUP:
            if db != database:
                continue
            cnt = data_conn.execute(
                f'SELECT COUNT(*) FROM "{table}" WHERE "{col}" IS NOT NULL').fetchone()[0]
            if cnt == 0:
                continue
            entry = {"table": table, "column": col, "references": ref, "count": cnt}
            if not preview:
                data_conn.execute(f'UPDATE "{table}" SET "{col}"=NULL WHERE "{col}" IS NOT NULL')
            cleaned.append(entry)

        purged: list[dict] = []
        for table in tables:
            try:
                cnt = data_conn.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]
            except sqlite3.OperationalError:
                continue
            entry = {"table": table, "count": cnt}
            if not preview and cnt:
                cur = data_conn.execute(f'DELETE FROM "{table}"')
                entry["deleted"] = cur.rowcount
                remaining = data_conn.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]
                entry["verified"] = remaining == 0
            elif not preview:
                entry["deleted"] = 0
                entry["verified"] = True
            purged.append(entry)

        if not preview:
            data_conn.commit()
    except Exception:
        if not preview:
            data_conn.rollback()
        raise
    finally:
        if owns_conn:
            data_conn.close()

    report_path = _write_retire_report(ctx, database, cleaned, purged, preview)
    total = sum(row.get("deleted", row["count"]) for row in purged)
    verb = "would clear" if preview else "cleared"
    unverified = [row["table"] for row in purged if not preview and not row.get("verified")]
    msg = (f"PREVIEW ({database}): {len(purged)} table(s), {total:,} row(s) {verb}, "
          f"{len(cleaned)} FK column(s) with dangling refs -- nothing written. "
          f"Re-run with -Live to execute." if preview else
          f"{database}: {verb} {total:,} row(s) across {len(purged)} table(s), "
          f"{len(cleaned)} FK column(s) de-dangled.")
    if unverified:
        msg += f" WARNING: {len(unverified)} table(s) did not verify to 0 remaining: {unverified}."
    return ok(f"{msg} Report: {report_path}", table_count=len(purged), row_count=total,
             cleaned_count=len(cleaned))
