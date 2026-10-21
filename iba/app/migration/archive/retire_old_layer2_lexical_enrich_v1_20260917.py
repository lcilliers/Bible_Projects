"""Complete the old Layer 2 lexical.enrich retirement the researcher instructed on 2026-09-15
(escalation #1719, researcher challenge same day): *"the old Layer 1 [and Layer 2] configuration
... must be explicitly retired as its own step, not left to drift alongside the new one."*

2026-09-16's rebuild (BUILD.md #267, Phase B item 5) marked `cfg_step lexical.enrich` inactive and
dropped 3 dead `cfg_column` rows on `verse_lexical` -- but checked live 2026-09-17 (researcher
directly doubted the retirement was real, correctly): that was only PART of the surface.

1. `cfg_step lexical.run` was NEVER touched -- still `inactive=0`, still live in `cfg_step`. Its
   handler (`handlers/lexical.py:run`, mode `Layer1AndLayer2`/`Layer2Only`) is a SECOND, separate
   entry point onto the exact same retired mechanism (`lexicalenrich.enrich_passage`, writing
   `verse_lexical_note`) -- by DEFAULT it auto-calls an LLM and writes, no flag needed. No live PS
   script currently reaches it (checked: no `.ps1` under `iba/app/ps/` references `lexical.run`),
   but it was fully callable via `python -m iba.app.run verse-lexical --step lexical.run ...`
   the whole time -- a real, reachable gap, not a hypothetical one.
2. `cfg_table verse_lexical_note` was still `inactive=0` ("active data").
3. Both `cfg_write_grant` rows onto it (`lexical.enrich`, `lexical.run`) were still `inactive=0`.

Data itself was never at risk in practice (173 live rows, last written 2026-09-05, well before
this rebuild -- nothing new was actually written to the old table this whole time), but the
CONFIGURATION genuinely still described it as live, which is exactly what the researcher's
original instruction said must not be left to drift. This migration closes that gap: `lexical.run`,
`verse_lexical_note` (`cfg_table`), and both its write grants -> `inactive=1`. `cfg_column` rows
for `verse_lexical_note` are left as historical record (the table-level flag is the authoritative
signal; #1706 Phase B's own precedent only dropped columns still live on an otherwise-active
table, not a whole retired table's columns).

Not touched (flagged, not fixed, here -- a separate, smaller residual): `report.lexical_exceptions`
(`cfg_report`) still describes itself as a `lexical.enrich` exception report and is still
`inactive=0` -- read-only, no write risk, still reachable via `VerseLexical.ps1 -Step
report.lexical_exceptions`, would just report against stale/historical data if run. Left for a
separate pass since it's not a write-path risk and out of scope for what was actually raised.

Safe to re-run: idempotent.

Usage:
    python iba/app/migration/retire_old_layer2_lexical_enrich_v1_20260917.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    before = {}
    before["cfg_step.lexical.run"] = conn.execute(
        "SELECT inactive FROM cfg_step WHERE step='lexical.run' AND work_package='verse-lexical'"
    ).fetchone()["inactive"]
    before["cfg_table.verse_lexical_note"] = conn.execute(
        "SELECT inactive FROM cfg_table WHERE name='verse_lexical_note' AND database='iba'"
    ).fetchone()["inactive"]
    grants = conn.execute(
        "SELECT writer, inactive FROM cfg_write_grant "
        "WHERE table_name='verse_lexical_note' AND database='iba'").fetchall()
    before["cfg_write_grant"] = {r["writer"]: r["inactive"] for r in grants}

    print("Before:", before)

    if args.dry_run:
        print("--dry-run: no changes made.")
        conn.close()
        return 0

    conn.execute(
        "UPDATE cfg_step SET inactive=1 WHERE step='lexical.run' AND work_package='verse-lexical'")
    conn.execute(
        "UPDATE cfg_table SET inactive=1 WHERE name='verse_lexical_note' AND database='iba'")
    conn.execute(
        "UPDATE cfg_write_grant SET inactive=1 "
        "WHERE table_name='verse_lexical_note' AND database='iba'")
    conn.commit()

    after = {}
    after["cfg_step.lexical.run"] = conn.execute(
        "SELECT inactive FROM cfg_step WHERE step='lexical.run' AND work_package='verse-lexical'"
    ).fetchone()["inactive"]
    after["cfg_table.verse_lexical_note"] = conn.execute(
        "SELECT inactive FROM cfg_table WHERE name='verse_lexical_note' AND database='iba'"
    ).fetchone()["inactive"]
    grants = conn.execute(
        "SELECT writer, inactive FROM cfg_write_grant "
        "WHERE table_name='verse_lexical_note' AND database='iba'").fetchall()
    after["cfg_write_grant"] = {r["writer"]: r["inactive"] for r in grants}
    print("After:", after)

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
