"""bootstrap_setting_module_column.py — ONE-OFF: add cfg_setting.module + backfill it.

Same class of exception as bootstrap_configuration_maintenance.py: adding a COLUMN to an
existing physical table is DDL (ALTER TABLE), which configmaint.propose cannot do — it only
writes/updates/deletes ROWS on already-existing columns. So the column addition is a direct,
documented, idempotent bootstrap here.

The BACKFILL (assigning each of the 26 existing settings to its module) is content, not schema
— but it's categorising already-approved settings by their VERIFIED real consumer (grepped
against iba/app/**/*.py, not guessed from the key prefix, which turned out to be unreliable:
e.g. discovery.particle_pattern is prefixed 'discovery' but its real consumer is stepapi.py's
Step class, not raw.py's discover()). Treated as part of this same batch bootstrap rather than
26 separate configmaint.propose approvals, since it's re-labelling existing, already-approved
rows with metadata, not introducing new settings or values. Every NEW setting from here on goes
through configmaint.propose, which now requires a module (see handlers/configmaint.py).

    python -m iba.app.migration.bootstrap_setting_module_column
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

# key -> module, one row per verified consumer (not the key's own prefix — see docstring)
MODULE_OF = {
    "candidate.lemma_base_pattern": "candidate",
    "configmaint.auto_report": "configmaint",              # real consumer: Config-Maintenance.ps1
    "configmaint.reference_seed_dir": "configmaint",        # not yet consumed — staged for Layer 2
    "configmaint.report_path": "configmaint",
    "discovery.follow_related": "raw",
    "discovery.particle_pattern": "step",                  # consumed by Step.is_particle, not raw.py
    "language.greek_prefix": "raw",
    "meaning.head_marker": "raw",
    "passage.cross_chapter": "passage",                    # dead in passage.py AND validation.py
    "passage.default_rule": "passage",
    "passage.min_shared_strongs": "passage",
    "passage.review_over": "passage",
    "registry.strip_ends_pattern": "registry",              # consumed by lib/words.py, registry's rule
    "report.sample_verses": "report",
    "report.show_validation": "report",
    "report.show_verse_text": "report",
    "report.span_fields": "report",
    "report.strong_fields": "report",
    "step.cap": "step",
    "step.expect_gloss_contains": "step",
    "step.expect_min_verses": "step",
    "step.probe_strong": "step",
    "step.span_html": "step",
    "step.walk_end": "step",
    "step.walk_max_iter": "step",
    "step.walk_start": "step",
}

CONFIG_MODULES = ("registry", "raw", "step", "report", "candidate", "passage", "configmaint")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    have_cols = {r[1] for r in conn.execute("PRAGMA table_info(cfg_setting)")}
    if "module" not in have_cols:
        conn.execute("ALTER TABLE cfg_setting ADD COLUMN module TEXT")
        report.append("cfg_setting.module column added (physical ALTER)")
    else:
        report.append("cfg_setting.module column already present")

    if not conn.execute(
            "SELECT 1 FROM cfg_column WHERE table_name='cfg_setting' AND name='module'").fetchone():
        ordinal = conn.execute(
            "SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_column WHERE table_name='cfg_setting'"
        ).fetchone()[0]
        conn.execute(
            "INSERT INTO cfg_column VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            ("cfg_setting", "module", ordinal, "TEXT", 0, 1, 0, None, None,
             "which module/utility owns this setting — every setting must have one, per the "
             "researcher's 2026-07-21 rule against cfg_setting becoming a catch-all",
             "enum.config_module", None, "configmaint.propose"))
        report.append("cfg_column row for cfg_setting.module added")
    else:
        report.append("cfg_column row for cfg_setting.module already present")

    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name='config_module'").fetchone():
        for i, v in enumerate(CONFIG_MODULES):
            conn.execute("INSERT INTO cfg_enum VALUES (?,?,?)", ("config_module", v, i))
        report.append(f"cfg_enum group 'config_module' ({len(CONFIG_MODULES)} values) added")
    else:
        report.append("cfg_enum group 'config_module' already present")

    backfilled = 0
    unmapped = []
    for r in conn.execute("SELECT key, module FROM cfg_setting"):
        key, current = r
        if current:
            continue
        target = MODULE_OF.get(key)
        if not target:
            unmapped.append(key)
            continue
        conn.execute("UPDATE cfg_setting SET module=? WHERE key=?", (target, key))
        backfilled += 1
    report.append(f"backfilled module for {backfilled} existing setting(s)")
    if unmapped:
        report.append(f"WARNING — no verified module mapping for: {unmapped} (left NULL)")

    conn.commit()
    conn.close()

    print("cfg_setting.module bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
