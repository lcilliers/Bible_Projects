"""observe_prompts_2507_v6_20261115.py -- escalation #2507 (design v4 D8: the lexical prompts leave the inner-being reading).

cfg_setting reading.observe_prompts gave the 53 one-verse catalogue questions to the inner-being reading under the kind of finding each serves. The 14 lexical questions
(M0.1.1 to 3, M0.4.1, M0.5.1 to 9, M0.5.11) and the 3 structural ones (M0.6.1, M0.6.5, M0.6.6) are the prompts of the lexical analysis (cfg_setting layer.reading, items prompts and asks)
and stage 3; they are taken out here, 36 remain (the inner-being questions M0.7, M0.8.1, D*, F0.1.1). Checked 2026-11-15: no live code reads this setting (only the test
temp_2273_reading_phases_test_run.py M7 does), so nothing changes for a reading. Through configmaint.apply_logged(). Idempotent. A named snapshot is taken before a live apply.
"""
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

RUN_ID = "DEVMODE-2507-OBSERVE-PROMPTS-20261115"
MODULE = "observe_prompts_2507_v6_20261115"
LEAVE = {"M0.1.1", "M0.1.2", "M0.1.3", "M0.4.1", "M0.5.1", "M0.5.2", "M0.5.3", "M0.5.4", "M0.5.5", "M0.5.6", "M0.5.7", "M0.5.8", "M0.5.9", "M0.5.11", "M0.6.1", "M0.6.5", "M0.6.6"}
USE = ("the inner-being catalogue questions of one verse given in the observe JSON as prompts, under the kind of finding each serves; a prompt that does not apply is not answered (RG-17; #2273). "
       "The lexical questions (M0.1, M0.4, M0.5) and the structural ones (M0.6.1, M0.6.5, M0.6.6) are not here: they are the prompts of the lexical analysis and the verse-lexical observations "
       "(cfg_setting layer.reading, #2507). Read by no live code: only the reading test checks it")


def main() -> int:
    cfg = Cfg(pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db"))
    conn = cfg.conn
    cur = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='reading.observe_prompts' AND inactive=0").fetchone()[0])
    new = {k: [c for c in v if c not in LEAVE] for k, v in cur.items()}
    ops = []
    if new != cur:
        ops.append(("cfg_setting", "update", {"key": "reading.observe_prompts"}, {"value": json.dumps(new, ensure_ascii=False), "use": USE}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "purpose": f"ONE-OFF migration -- escalation #2507: the lexical prompts leave reading.observe_prompts; run_id {RUN_ID}.",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    if not ops:
        print("already applied: nothing changed")
        return 0
    if "--no-snapshot" not in sys.argv:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2507-prompts', named=True)}")
    conn.execute("SAVEPOINT prompts_2507")
    for t, op, where, set_ in ops:
        apply_logged(conn, RUN_ID, t, op, where, set_)
    conn.execute("RELEASE prompts_2507")
    conn.commit()
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); prompts left: {sum(len(v) for v in new.values())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
