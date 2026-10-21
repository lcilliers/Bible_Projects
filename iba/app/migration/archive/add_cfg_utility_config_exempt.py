"""add_cfg_utility_config_exempt.py — ONE-OFF: `cfg_utility` gains `config_exempt`/
`config_exempt_reason` so `find_utility_config_density`'s "zero config usage" finding can
distinguish a genuinely exempt module (its caller resolves config for it, or it IS the config
layer — can't call its own accessor) from a real completeness gap, declaratively, instead of
re-litigating the same 11 modules on every `configmaint.validate` run.

Schema is DDL (two new columns), so — same class of exception as every other schema addition in
this app (`bootstrap_inactive_column.py`, `bootstrap_cfg_utility.py`, `bootstrap_step_kind.py`) — a
direct, documented, idempotent bootstrap, not a `configmaint.propose` call. The 11 exemptions below
are a one-time classification backfill from the researcher's own 2026-07-30 read of
`reports/cfg-utility-density-check-review-20260730.md`; changing a module's exemption going
forward goes through the normal `configmaint.propose` path like any other `cfg_utility` value.

Deliberately NOT exempted here: `db.py`/`dbsnapshot.py` (the check's OWN pattern-detection was the
bug — both genuinely use config, see the fix in `lib/cfgquality.find_utility_config_density`, not
an exemption) and `lexiconparse.py` (the one real, still-open gap — six regexes/a hardcoded
tag-set with zero `Cfg` reference at all).

    python -m iba.app.migration.add_cfg_utility_config_exempt
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

# module -> reason (recorded so the "why" travels with the flag, not just memory/a report file).
# Every reason cites the actual mechanism, not a vague "seems fine" — pulled directly from
# cfg-utility-density-check-review-20260730.md's per-module verdicts.
_EXEMPT = {
    "cfg": "defines .setting()/.enum() itself — the config reader; cannot call its own accessor.",
    "cfgquality": "works directly against a raw sqlite3.Connection (not a Cfg wrapper), by design "
                 "— usable from both configmaint.py (has a Cfg) and cfgreport.py (doesn't); "
                 "queries cfg_setting/cfg_enum via raw SQL, not Cfg's convenience methods. Found "
                 "2026-07-30 only after fixing this same check's own text-collision false negative "
                 "for this file — same class of legitimate zero as the other 11, not an oversight.",
    "cfgcheck": "validates the raw seed dict before any Cfg/DB object exists — structurally "
               "cannot call .setting()/.enum().",
    "cfgload": "writes the seed INTO the cfg_* tables (creates + populates them) — same class as "
              "migration/ scripts, already excluded from usage-checks for the same reason.",
    "cfgreport": "generates reports by querying cfg_* tables directly; the paths it needs "
                "(out_path/db_path) are resolved by its caller (configmaint.report), not read here.",
    "passagetrack": "receives an already-open cfg/connection from its caller; only checks "
                    "cfg.may_write(), no settings/enums of its own.",
    "registryreport": "receives cfg.conn from its caller; no settings/enums of its own.",
    "retention": "receives cfg.conn from its caller; its own setting "
                "(retention.snapshot_keep_count) is read by dbsnapshot.py, not here.",
    "schemareport": "receives cfg.conn from its caller; no settings/enums of its own.",
    "seedreport": "receives cfg.conn from its caller; no settings/enums of its own.",
    "spanreport": "receives cfg.conn from its caller; no settings/enums of its own.",
    "strongreport": "receives cfg.conn from its caller; no settings/enums of its own.",
}


def _add_columns(conn: sqlite3.Connection, report: list[str]) -> None:
    cols = {r[1] for r in conn.execute("PRAGMA table_info(cfg_utility)")}
    if "config_exempt" not in cols:
        conn.execute("ALTER TABLE cfg_utility ADD COLUMN config_exempt INTEGER NOT NULL DEFAULT 0")
        report.append("cfg_utility.config_exempt column added (physical ALTER)")
    else:
        report.append("cfg_utility.config_exempt already present")

    if "config_exempt_reason" not in cols:
        conn.execute("ALTER TABLE cfg_utility ADD COLUMN config_exempt_reason TEXT")
        report.append("cfg_utility.config_exempt_reason column added (physical ALTER)")
    else:
        report.append("cfg_utility.config_exempt_reason already present")

    for name, use, dflt in (
        ("config_exempt", "1 = a legitimate zero for config-setting/enum usage (caller resolves "
                          "it, or this module IS the config layer) — declared, not re-derived "
                          "every validate run. 0 = subject to the usual finding.", "0"),
        ("config_exempt_reason", "why this module is exempt — required whenever config_exempt=1 "
                                 "so the flag never sits undocumented.", None),
    ):
        if not conn.execute(
                "SELECT 1 FROM cfg_column WHERE table_name='cfg_utility' AND name=?", (name,)
        ).fetchone():
            ordinal = conn.execute(
                "SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_column WHERE table_name='cfg_utility'"
            ).fetchone()[0]
            conn.execute(
                'INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, "notnull", '
                "is_unique, dflt, fk, use, expectation, source, filled_by) "
                "VALUES ('cfg_utility',?,?,?,0,?,0,?,NULL,?,NULL,NULL,"
                "'migration/add_cfg_utility_config_exempt.py')",
                (name, ordinal, "INTEGER" if name == "config_exempt" else "TEXT",
                 1 if name == "config_exempt" else 0, dflt, use))
            report.append(f"cfg_column row for cfg_utility.{name} added")
        else:
            report.append(f"cfg_column row for cfg_utility.{name} already present")


def _classify(conn: sqlite3.Connection, report: list[str]) -> None:
    known = {r[0] for r in conn.execute("SELECT module FROM cfg_utility")}
    for module, reason in _EXEMPT.items():
        if module not in known:
            report.append(f"SKIPPED {module!r} — not a known cfg_utility module (list is stale, "
                          f"fix the migration, not the DB)")
            continue
        already = conn.execute(
            "SELECT config_exempt FROM cfg_utility WHERE module=?", (module,)).fetchone()
        if already and already[0]:
            report.append(f"{module!r} already exempt — left alone")
            continue
        conn.execute("UPDATE cfg_utility SET config_exempt=1, config_exempt_reason=? "
                    "WHERE module=?", (reason, module))
        report.append(f"{module!r} -> config_exempt=1")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    _add_columns(conn, report)
    _classify(conn, report)

    conn.commit()
    conn.close()

    print("cfg_utility config_exempt bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
