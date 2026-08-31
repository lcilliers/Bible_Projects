"""build_schema_overview_report.py — human-readable schema overview for a captured DBSchema
register (escalation #1306, 2026-08-31: "There is no schema overview report for
Bible_research_DB").

Reads the ALREADY-CAPTURED register at iba/config/DBSchema/<file>.json (built/kept current by
iba/scripts/build_dbschema.py — this script never touches the live DB itself) and renders a
markdown digest: per-table row/column/key counts plus its captured description, sorted
alphabetically, with a flagged section for anything still undescribed. One-off/investigatory
report (procedural_document_taxonomy category a) — no cfg_step/cfg_report row, path/naming/
archiving come from governance.oneoff_* config via lib/reportkit.oneoff_path(), same convention
as manifest.py's manifest-search report and contentindex.py's content-index-search report.

Usage:
    python iba/app/tools/build_schema_overview_report.py --db bible_research
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

APP_ROOT = pathlib.Path(__file__).resolve().parent.parent          # iba/app
PROJECT_ROOT = APP_ROOT.parent.parent                               # repo root
sys.path.insert(0, str(APP_ROOT.parent.parent))

from iba.app.lib.cfg import Cfg                                     # noqa: E402
from iba.app.lib import reportkit                                   # noqa: E402

REGISTER_DIR = PROJECT_ROOT / "iba" / "config" / "DBSchema"
# database code -> register filename, mirrors DBSchema_maintenance.json's own
# ent.dbschema.database.spec.databases mapping (bible_research -> DBSchema.json, no db-code
# suffix, since it was the first/only one registered at build time).
REGISTER_FILE = {"bible_research": "DBSchema.json"}


def _load(db_code: str) -> dict:
    fname = REGISTER_FILE.get(db_code)
    if not fname:
        raise SystemExit(f"no DBSchema register known for db code {db_code!r} "
                          f"(see iba/config/utility/DBSchema_maintenance.json)")
    path = REGISTER_DIR / fname
    if not path.exists():
        raise SystemExit(f"register not found: {path} — run "
                          f"'python iba/scripts/build_dbschema.py --db {db_code}' first")
    return json.loads(path.read_text(encoding="utf-8"))


def _fmt_int(n: int) -> str:
    return f"{n:,}"


def render(reg: dict) -> str:
    tables: dict = reg["tables"]
    L = []
    L.append(f"# {reg['database']} — schema overview")
    L.append("")
    L.append(f"_Generated from the DBSchema register (`{reg['database_path']}`, "
             f"schema {reg['schema_version']}, register captured {reg['exported_date']}). "
             f"Escalation #1306._")
    L.append("")
    counts = reg.get("counts", {})
    L.append(f"**{counts.get('tables', len(tables))} tables · "
             f"{_fmt_int(counts.get('columns', 0))} columns · "
             f"{counts.get('pk_columns', 0)} PK columns · "
             f"{counts.get('foreign_keys', 0)} FKs · "
             f"{counts.get('checks', 0)} checks · "
             f"{counts.get('indexes', 0)} indexes · "
             f"{counts.get('triggers', 0)} triggers · "
             f"{counts.get('views', 0)} views**")
    L.append("")

    undescribed_tables = [n for n, t in tables.items() if not (t.get("description") or "").strip()]
    undescribed_cols = sum(
        1 for t in tables.values() for c in t.get("columns", [])
        if not (c.get("description") or "").strip())
    if undescribed_tables or undescribed_cols:
        L.append(f"> ⚠ {len(undescribed_tables)} table(s) and {undescribed_cols} column(s) "
                 f"still undescribed — see the flagged section at the end.")
        L.append("")

    L.append("## Tables")
    L.append("")
    L.append("| table | description | rows | cols | PK | FKs | idx |")
    L.append("|---|---|---:|---:|---|---:|---:|")
    for name in sorted(tables):
        t = tables[name]
        desc = (t.get("description") or "_(undescribed)_").strip().replace("\n", " ")
        if len(desc) > 140:
            desc = desc[:137] + "..."
        pk = ", ".join(t.get("primary_key") or []) or "—"
        L.append(f"| `{name}` | {desc} | {_fmt_int(t.get('row_count', 0))} | "
                 f"{len(t.get('columns', []))} | {pk} | {len(t.get('foreign_keys', []))} | "
                 f"{len(t.get('indexes', []))} |")
    L.append("")

    if undescribed_tables:
        L.append("## Undescribed tables")
        L.append("")
        for name in sorted(undescribed_tables):
            L.append(f"- `{name}` — {_fmt_int(tables[name].get('row_count', 0))} rows, "
                     f"{len(tables[name].get('columns', []))} columns")
        L.append("")

    L.append("---")
    L.append(f"_Rebuild the register with `python iba/scripts/build_dbschema.py "
             f"--db {reg['database'].split('/')[0] if '/' in reg['database'] else 'bible_research'} "
             f"--verify` before regenerating this report, if it may be stale._")
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="bible_research")
    a = ap.parse_args()

    reg = _load(a.db)
    body = render(reg)

    cfg = Cfg()
    try:
        out_path = reportkit.oneoff_path(cfg, f"schema-overview-{a.db}", ext="md")
    finally:
        cfg.conn.close()
    out_path.write_text(body, encoding="utf-8")
    print(f"[write] {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
