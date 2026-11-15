"""layers_rule_text_2505_v2_20261115.py -- escalation #2505: the behaviour rule collection-reading-runs-in-layers distinguishes its layers from the Layer 1 and Layer 2 of the
verse_lexical build without naming the retired step (lexical.enrich) that the compliance check lists as a retired name; one cfg_behaviour_rule update through apply_logged.
Idempotent. Usage: python iba/app/migration/layers_rule_text_2505_v2_20261115.py [--db PATH]"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2505-LAYERS-RULE-TEXT-20261115"
MODULE = "layers_rule_text_2505_v2_20261115"
OLD = "(lexical.enrich)."
NEW = "."


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    a = ap.parse_args()
    conn = Cfg(pathlib.Path(a.db)).conn
    r = conn.execute("SELECT id, rule_text FROM cfg_behaviour_rule WHERE rule_key='collection-reading-runs-in-layers'").fetchone()
    if r is None or OLD not in r[1]:
        print("already applied: nothing changed")
        return 0
    conn.execute("SAVEPOINT rule_text")
    apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "update", {"id": r[0]}, {"rule_text": r[1].replace("verse_lexical build " + OLD, "verse_lexical build" + NEW)})
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        apply_logged(conn, RUN_ID, "cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "purpose": f"ONE-OFF migration -- escalation #2505: a rule text restated; run_id {RUN_ID}.", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "crash_escalation_reviewed": 0, "crash_escalation_note": None})
    conn.execute("RELEASE rule_text")
    conn.commit()
    print(f"applied (run {RUN_ID}): rule {r[0]} restated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
