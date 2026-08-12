"""bootstrap_cluster_tables_20260811.py — ONE-OFF: create the `cluster` and `cluster_strong`
tables and load them from the old project's cluster taxonomy — brand-new tables, so bootstrap-
direct like bootstrap_lexicon_parsed_layer.py, not configmaint.propose (propose only writes rows
on already-existing tables/columns; it cannot create a table).

WHY this exists. Recovered raw-data-integrity plan (power-failure session, 2026-08-11), stage b
("Strong relevance") — researcher direction: adopt the OLD project's cluster model into IBA
wholesale rather than build bespoke IBA filters. Every Strong's code IBA knows about should carry
a cluster assignment (an M-code, FLAG, or T2); T2 becomes the landing zone for codes that should
not be included in analysis. This is Fork (a) (BUILD.md sec101) merged into Fork (b)'s build.

**Cluster membership is a property of the STRONG'S CODE, not of any word that happens to
reference it** (researcher correction, this session — the old DB's own `mti_terms.cluster_code`
is keyed by Strong's number with no reference to word membership; IBA's `word_strong` junction is
a different, unrelated axis). So this migration scopes against IBA's FULL `strong` table (15,293
active rows, this session's count) — not the subset currently linked via `word_strong` — and the
new `cluster_strong` link table has no FK/dependency on `word_strong`/`word_registry` at all.

  cluster         — the 49-row taxonomy (M01-M46 + FLAG + T2), migrated from the old project's
                    `bible_research.db` cluster table. Only the taxonomy fields are carried over
                    (cluster_code/short_name/description/gloss) — the old table's own workflow-
                    progress columns (bucket/status/source/version/last_updated_date/
                    char_structure) describe THAT project's session state, not a property of the
                    cluster itself, and are not migrated.
  cluster_strong  — one row per (strong, cluster_code) assignment. `source` distinguishes how a
                    row was populated (`old-system-migration` for this pass; later passes, e.g.
                    the still-to-be-designed LLM-assisted allocation for codes with no old-system
                    match, will use their own source value) — never overwritten in place, so
                    provenance survives.

Seed data (Fork (a)'s own checkpoint superseded by a fresh live query this session — the
17-day-old CSV export was close but not exact; queried `bible_research.db` directly instead):
2,709 of IBA's 15,293 strong codes have an old-cluster match (92 map to 2, none to more);
12,584 have none — the "outstanding" set for the LLM allocation step, not built in this pass.

    python -m iba.app.migration.bootstrap_cluster_tables_20260811 --dry-run
    python -m iba.app.migration.bootstrap_cluster_tables_20260811
"""
from __future__ import annotations

import argparse
import csv
import datetime
import sqlite3
import sys

from ..lib.cfg import Cfg, DB_PATH
from ..lib.db import build_data_tables

OLD_DB_PATH = "database/bible_research.db"
CLUSTER_MASTER_CSV = "iba/app/reports/cluster-master-20260811.csv"

REPORT: list[str] = []


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _table(conn, name, grain, use):
    if not conn.execute("SELECT 1 FROM cfg_table WHERE name=?", (name,)).fetchone():
        conn.execute("INSERT INTO cfg_table VALUES (?,?,?)", (name, grain, use))
        REPORT.append(f"cfg_table {name!r} added")
    else:
        REPORT.append(f"cfg_table {name!r} already present")


def _column(conn, table, name, ordinal, type_, is_pk=0, notnull=0, is_unique=0, dflt=None,
            fk=None, use="", expectation=None, source=None, filled_by=None):
    if not conn.execute("SELECT 1 FROM cfg_column WHERE table_name=? AND name=?",
                         (table, name)).fetchone():
        conn.execute(
            'INSERT INTO cfg_column ("table_name","name","ordinal","type","is_pk","notnull",'
            '"is_unique","dflt","fk","use","expectation","source","filled_by") '
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (table, name, ordinal, type_, is_pk, notnull, is_unique, dflt, fk, use, expectation,
             source, filled_by))
        REPORT.append(f"cfg_column ({table}, {name}) added")
    else:
        REPORT.append(f"cfg_column ({table}, {name}) already present")


def _grant(conn, writer, table):
    if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?",
                         (writer, table)).fetchone():
        conn.execute("INSERT INTO cfg_write_grant (writer, table_name, inactive) VALUES (?,?,0)",
                      (writer, table))
        REPORT.append(f"cfg_write_grant ({writer} -> {table}) added")
    else:
        REPORT.append(f"cfg_write_grant ({writer} -> {table}) already present")


def register(conn: sqlite3.Connection, physical_build: bool = True) -> None:
    # ── tables ────────────────────────────────────────────────────────────────────────────────
    _table(conn, "cluster",
           "one row per cluster (M01-M46 + FLAG + T2) — the inner-being dimension taxonomy",
           "Migrated from the old project's bible_research.db `cluster` table, 2026-08-11. "
           "cluster_code is the canonical key referenced everywhere else (cluster_strong, and any "
           "future dimension work). T2 is the landing zone for codes not included in analysis; "
           "FLAG is unresolved/needs-review; M01-M46 are the named inner-being characteristics.")
    _table(conn, "cluster_strong",
           "one row per (strong, cluster_code) assignment",
           "The strong<->cluster link. Cluster membership is a property of the Strong's code "
           "itself, independent of word_strong/word_registry — deliberately has no FK/dependency "
           "on either. `source` tracks provenance (old-system-migration now; future allocation "
           "passes get their own source value, never overwriting a prior row in place).")

    # ── columns: cluster ─────────────────────────────────────────────────────────────────────
    _column(conn, "cluster", "cluster_code", 0, "TEXT", is_pk=1,
            use="canonical key, e.g. M01, FLAG, T2", source="migrated:bible_research.db.cluster")
    _column(conn, "cluster", "short_name", 1, "TEXT",
            use="short display name, e.g. 'Fear'", source="migrated:bible_research.db.cluster")
    _column(conn, "cluster", "description", 2, "TEXT",
            use="one-line description, e.g. 'Fear, Dread and Terror'",
            source="migrated:bible_research.db.cluster")
    _column(conn, "cluster", "gloss", 3, "TEXT",
            use="worked-example term list for this cluster (comma-joined gloss(transliteration) "
                "pairs) — the associative signal for allocating an unmatched code",
            source="migrated:bible_research.db.cluster")
    _column(conn, "cluster", "deleted", 4, "INTEGER", dflt="0", use="soft delete")

    # ── columns: cluster_strong ──────────────────────────────────────────────────────────────
    _column(conn, "cluster_strong", "id", 0, "INTEGER", is_pk=1, use="surrogate key")
    _column(conn, "cluster_strong", "strong", 1, "TEXT", notnull=1, fk="strong.strongNumber",
            use="the full Strong's code this assignment is for")
    _column(conn, "cluster_strong", "cluster_code", 2, "TEXT", notnull=1, fk="cluster.cluster_code",
            use="the assigned cluster")
    _column(conn, "cluster_strong", "source", 3, "TEXT", notnull=1,
            use="provenance: 'old-system-migration' | (future) an LLM-allocation pass identifier")
    _column(conn, "cluster_strong", "created_at", 4, "TEXT", use="ISO-8601 UTC")
    _column(conn, "cluster_strong", "deleted", 5, "INTEGER", dflt="0", use="soft delete")

    conn.commit()

    if physical_build:
        cfg = Cfg(DB_PATH)
        built = build_data_tables(cfg, conn)
        for t in ("cluster", "cluster_strong"):
            REPORT.append(f"physical table {t!r} " +
                          ("built" if t in built else "NOT in build_data_tables output — check cfg_table"))
        cfg.close()
    else:
        REPORT.append("physical table build SKIPPED (--dry-run) — Cfg always reads DB_PATH directly")

    # ── write grants — reuse the existing 'migration' writer identity, same as every other
    # one-off migration script in this codebase (e.g. backfill_morphless_span_fix_20260810.py) ──
    _grant(conn, "migration", "cluster")
    _grant(conn, "migration", "cluster_strong")

    conn.commit()


def _seed_cluster_master(conn: sqlite3.Connection) -> None:
    if conn.execute("SELECT COUNT(*) FROM cluster WHERE deleted=0").fetchone()[0] > 0:
        REPORT.append("cluster master: already seeded, skipped")
        return
    n = 0
    with open(CLUSTER_MASTER_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            conn.execute(
                "INSERT INTO cluster (cluster_code, short_name, description, gloss, deleted) "
                "VALUES (?,?,?,?,0)",
                (row["cluster_code"], row["short_name"], row["description"], row["gloss"]))
            n += 1
    conn.commit()
    REPORT.append(f"cluster master: {n} rows loaded from {CLUSTER_MASTER_CSV}")


def _seed_cluster_strong(conn: sqlite3.Connection) -> None:
    if conn.execute("SELECT COUNT(*) FROM cluster_strong WHERE deleted=0").fetchone()[0] > 0:
        REPORT.append("cluster_strong: already seeded, skipped")
        return
    old = sqlite3.connect(OLD_DB_PATH)
    old_map: dict[str, set[str]] = {}
    for strongs_number, cluster_code in old.execute(
            "SELECT strongs_number, cluster_code FROM mti_terms "
            "WHERE cluster_code IS NOT NULL AND cluster_code != ''"):
        old_map.setdefault(strongs_number, set()).add(cluster_code)
    old.close()

    known_clusters = {r[0] for r in conn.execute("SELECT cluster_code FROM cluster WHERE deleted=0")}
    iba_strongs = [r[0] for r in conn.execute("SELECT strongNumber FROM strong WHERE deleted=0")]

    now = _now()
    n_rows, n_strongs, n_skipped_unknown_cluster = 0, 0, 0
    for s in iba_strongs:
        codes = old_map.get(s)
        if not codes:
            continue
        n_strongs += 1
        for code in sorted(codes):
            if code not in known_clusters:
                n_skipped_unknown_cluster += 1
                continue
            conn.execute(
                "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, deleted) "
                "VALUES (?,?,?,?,0)", (s, code, "old-system-migration", now))
            n_rows += 1
    conn.commit()
    REPORT.append(f"cluster_strong: {n_rows} rows inserted, covering {n_strongs} distinct "
                  f"IBA strongs (of {len(iba_strongs)} total) via old-system-migration"
                  + (f"; {n_skipped_unknown_cluster} skipped (cluster_code not in cluster master)"
                     if n_skipped_unknown_cluster else ""))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    if a.dry_run:
        conn2 = sqlite3.connect(":memory:")
        conn2.row_factory = sqlite3.Row
        conn.backup(conn2)
        register(conn2, physical_build=False)
        # can't physically seed without the real tables (dry-run skips physical_build) — just
        # report the registration step for a dry-run.
        print("--dry-run (against an in-memory copy, nothing written to iba.db):")
        for line in REPORT:
            print(f"  - {line}")
        conn2.close()
        conn.close()
        return 0

    register(conn)
    _seed_cluster_master(conn)
    _seed_cluster_strong(conn)
    print("cluster-tables bootstrap:")
    for line in REPORT:
        print(f"  - {line}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
