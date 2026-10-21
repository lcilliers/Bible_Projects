"""apply_2199_2201_decisions_v1_20261021.py -- escalations #2199 and #2201 (elements of the IBA app
reset, #2177), the researcher's approved decisions.

#2199 (the filename templates in docs/file-organisation-rules.md are no longer used: retire): the
cfg_behaviour_class descriptions drop their pointers to archived documents and their dated
population notes (rule 96), and governance.oneoff_report_naming_pattern's use text drops its
pointer.

#2201:
  2. report.cluster's backfill_typology section and its three CSVs are registered
     (cfg_report_section; cfg_report_csv_table virtual rows).
  3. the JSON seed loader is retired: lib/cfgload.py and lib/cfgcheck.py move to lib/archive/.
  4. the word-audit work package is retired (replaced): work package and steps inactive,
     handlers/wordaudit.py and ps/Word-Audit.ps1 to archive.
  5. lib/narrativegenerate.py and lib/wordregistryspanreport.py are retired (non-compliant), with
     the work packages that used them (book-narrative, word-registry-span-report), handlers/
     narrative.py and their PS scripts; the settings and enum group only they read go inactive.
  6. passage.suggest_boundary is retired.
For every retired step, the cfg_report / cfg_report_section / cfg_report_csv_table / cfg_on_fail
rows naming it and the cfg_write_grant rows for it as writer go inactive (validate requires an active
step for each). Moved files get inactive cfg_utility rows at their archive paths.

Registers itself (inactive, at its own archive path). Written through configmaint.apply_logged().
Idempotent. One transaction.

Usage:
    python iba/app/migration/apply_2199_2201_decisions_v1_20261021.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2201-DECISIONS-20261021"
MODULE = "apply_2199_2201_decisions_v1_20261021"
RETIRED_EXEMPT = "retired script (#2201): kept for reference only; use needs the researcher's approval"

CLASS_TEXT = {  # class -> (old substring, new substring)
    "chat": (" Populated 2026-08-18 (escalation #715 cycle 3, 9 rules) from docs/interaction-preferences.md,"
             " CLAUDE.md sec9, and confirmed feedback_* memory.", ""),
    "development": (" Added 2026-08-18, escalation #732.", ""),
    "documentation": ("BUILD.md, README.md, CLAUDE.md, docs/interaction-preferences.md, Workflow/Instructions/*",
                      "BUILD.md, CLAUDE.md, Workflow/Instructions/*"),
    "filing": (" and from any one methodology's own artefact-specific filename templates, which stay legacy"
               " prose in docs/file-organisation-rules.md, not encoded here. Added 2026-08-28, escalation"
               " #971 (carries forward #863/#736's unbuilt scope).", "."),
    "study_method": (" Added 2026-10-21, escalation #2181, when CLAUDE.md's study rules moved to config.", ""),
}
ONEOFF_KEY = "governance.oneoff_report_naming_pattern"
ONEOFF_USE = ("filename pattern for one-off reports ({topic}/{YYYYMMDD}/{format} substituted); same-day "
              "collisions get -v2/-v3/... appended by oneoff_path() itself")

SECTION = {"step": "report.cluster", "ordinal": 4, "section_key": "backfill_typology",
           "heading": "## Backfill vocabulary outside the cluster taxonomy",
           "toc_label": "Backfill vocabulary (outside clusters)", "include": 1, "inactive": 0}
CSVS = {
    "backfill_typology": "every untagged backfill strong with its heuristic type (proper_noun / "
                         "grammatical_marker / closed_class / candidate_vocabulary)",
    "backfill_crossmatch": "untagged backfill strongs whose gloss keywords match a clustered strong's or "
                           "a registry word's",
    "backfill_residual": "untagged backfill strongs with no cross-match, with their gloss stem key",
}

RETIRE_WP = ("word-audit", "book-narrative", "word-registry-span-report")
RETIRE_STEPS = ("passage.suggest_boundary",)          # plus every step of RETIRE_WP
MOVES = {  # live path -> archive path
    "iba/app/lib/cfgload.py": "iba/app/lib/archive/cfgload.py",
    "iba/app/lib/cfgcheck.py": "iba/app/lib/archive/cfgcheck.py",
    "iba/app/handlers/wordaudit.py": "iba/app/handlers/archive/wordaudit.py",
    "iba/app/ps/Word-Audit.ps1": "iba/app/ps/archive/Word-Audit.ps1",
    "iba/app/lib/narrativegenerate.py": "iba/app/lib/archive/narrativegenerate.py",
    "iba/app/lib/wordregistryspanreport.py": "iba/app/lib/archive/wordregistryspanreport.py",
    "iba/app/handlers/narrative.py": "iba/app/handlers/archive/narrative.py",
    "iba/app/ps/Book-Narrative.ps1": "iba/app/ps/archive/Book-Narrative.ps1",
    "iba/app/ps/WordRegistrySpan-Report.ps1": "iba/app/ps/archive/WordRegistrySpan-Report.ps1",
}
SETTINGS_OFF = ("method.inner_being_narrative_guidance_path", "method.narrative_hard_constraints_path",
                "narrative.scope_check_report_path", "narrative.generate_model",
                "narrative.generate_max_output_tokens", "narrative.generate_max_cost",
                "narrative.rate_input_per_million", "narrative.rate_output_per_million",
                "narrative.output_pattern", "narrative.usage_log_path")
ENUM_OFF = ("narrative_required_channel",)


def plan(conn) -> list[tuple]:
    ops = []
    for cls, (old, new) in CLASS_TEXT.items():
        d = conn.execute("SELECT description FROM cfg_behaviour_class WHERE class=?", (cls,)).fetchone()
        if d and old in d[0]:
            ops.append(("cfg_behaviour_class", "update", {"class": cls}, {"description": d[0].replace(old, new)}))
    u = conn.execute("SELECT use FROM cfg_setting WHERE key=?", (ONEOFF_KEY,)).fetchone()
    if u and u[0] != ONEOFF_USE:
        ops.append(("cfg_setting", "update", {"key": ONEOFF_KEY}, {"use": ONEOFF_USE}))
    if not conn.execute("SELECT 1 FROM cfg_report_section WHERE step=? AND section_key=?",
                        (SECTION["step"], SECTION["section_key"])).fetchone():
        ops.append(("cfg_report_section", "insert", {}, dict(SECTION)))
    for name, note in CSVS.items():
        if not conn.execute("SELECT 1 FROM cfg_report_csv_table WHERE step='report.cluster' AND table_name=?",
                            (name,)).fetchone():
            ops.append(("cfg_report_csv_table", "insert", {}, {"step": "report.cluster", "table_name": name,
                        "join_note": note, "inactive": 0, "virtual": 1}))
    steps = set(RETIRE_STEPS)
    for wp in RETIRE_WP:
        row = conn.execute("SELECT inactive, ps_script FROM cfg_work_package WHERE name=?", (wp,)).fetchone()
        if row:
            set_ = {}
            if row[0] != 1:
                set_["inactive"] = 1
            ps = (row[1] or "").replace("\\", "/")
            if ps in MOVES:
                set_["ps_script"] = MOVES[ps]
            if set_:
                ops.append(("cfg_work_package", "update", {"name": wp}, set_))
        steps |= {r[0] for r in conn.execute("SELECT step FROM cfg_step WHERE work_package=?", (wp,))}
    for wp, step, handler, inactive in conn.execute(
            "SELECT work_package, step, handler, inactive FROM cfg_step WHERE step IN (%s)"
            % ",".join("?" * len(steps)), sorted(steps)):
        set_ = {}
        if inactive != 1:
            set_["inactive"] = 1
        mod = (handler or "").split(":")[0].replace(".", "/") + ".py"
        if mod in MOVES:
            set_["handler"] = MOVES[mod][:-3].replace("/", ".") + ":" + handler.split(":", 1)[1]
        if set_:
            ops.append(("cfg_step", "update", {"work_package": wp, "step": step}, set_))
    for table, col, keys in (("cfg_report", "step", ("step",)),
                             ("cfg_report_section", "step", ("step", "ordinal")),
                             ("cfg_report_csv_table", "step", ("step", "table_name")),
                             ("cfg_on_fail", "step", ("step", "condition")),
                             ("cfg_write_grant", "writer", ("writer", "table_name", "database"))):
        for row in conn.execute(f"SELECT {', '.join(keys)} FROM {table} WHERE {col} IN (%s) AND inactive=0"
                                % ",".join("?" * len(steps)), sorted(steps)):
            ops.append((table, "update", dict(zip(keys, row)), {"inactive": 1}))
    for key in SETTINGS_OFF:
        if conn.execute("SELECT 1 FROM cfg_setting WHERE key=? AND inactive=0", (key,)).fetchone():
            ops.append(("cfg_setting", "update", {"key": key}, {"inactive": 1}))
    for name in ENUM_OFF:
        for (value,) in conn.execute("SELECT value FROM cfg_enum WHERE name=? AND inactive=0", (name,)):
            ops.append(("cfg_enum", "update", {"name": name, "value": value}, {"inactive": 1}))
    rows = {r[0]: (r[1], r[2]) for r in conn.execute("SELECT file_path, module, inactive FROM cfg_utility")}
    modules = {r[0] for r in conn.execute("SELECT module FROM cfg_utility")}
    for old, new in MOVES.items():
        if new in rows:
            continue
        if old in rows:
            ops.append(("cfg_utility", "update", {"module": rows[old][0]}, {"file_path": new, "inactive": 1}))
            continue
        mod = new.rsplit(".", 1)[0].replace("/", "_").lower()
        while mod in modules:
            mod += "_r"
        modules.add(mod)
        ops.append(("cfg_utility", "insert", {}, {"module": mod, "file_path": new, "inactive": 1,
                    "config_exempt": 1, "config_exempt_reason": RETIRED_EXEMPT,
                    "purpose": f"Retired (#2201). Was {old}."}))
    if MODULE not in modules:
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalations #2199/#2201: the researcher's approved decisions, "
                       f"through configmaint.apply_logged under run_id {RUN_ID}. inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    counts = {}
    for t, op, _, _ in ops:
        counts[f"{t} {op}"] = counts.get(f"{t} {op}", 0) + 1
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s): {counts}")
        return 0
    if not ops:
        print("already applied -- skipped")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail): {counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
