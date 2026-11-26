"""encode_2637_g3_c4_v1_20261126.py -- escalation #2637, plan v3 section 5 (outputs/escalation/2637-build-plan-v3-20261126.md).

G3, decided by the researcher (#2637 v7): a 3.1 qualification finding may hold the partner words of the subgroup's 2.1 qualifier observations
where the reading judges the qualifier bears on the working (lib/layerinner.py _qualifier_partners); IB-02 says so.
C4, conformed under B:98 and approved with the plan: a merge is for an observation saying the same, not only the same text
(cfg_setting reading.observation_rules merge_same_text_only false; observationrecord.merge_observation).
Through configmaint.apply_logged; archived after the live apply. Idempotent.
Usage: python iba/app/migration/encode_2637_g3_c4_v1_20261126.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged, archive_migration  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2637-G3C4-20261126"
MODULE = "encode_2637_g3_c4_v1_20261126"
G3 = (" In 3.1 a qualification finding may also hold, with the role qualifier, the occurrences of the partner words the subgroup's 2.1 qualifier "
      "observations name, where the reading judges the qualifier bears on the working; a qualifier that does not bear on it is declared in "
      "not_used with its reason, never forced into a finding.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = []
    rid, text = conn.execute("SELECT id, rule_text FROM cfg_method_rule WHERE rule_key LIKE 'IB-02 %' AND active=1").fetchone()
    if G3.strip() not in text:
        ops.append(("cfg_method_rule", "update", {"id": rid}, {"rule_text": text.rstrip() + G3}))
    r = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='reading.observation_rules'").fetchone()[0])
    if r.get("merge_same_text_only") is not False:
        r["merge_same_text_only"] = False
        ops.append(("cfg_setting", "update", {"key": "reading.observation_rules"}, {"value": json.dumps(r, ensure_ascii=False)}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py", "purpose": "migration of #2637 G3 (IB-02) and C4 (merge on meaning)",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "a one-off migration; its values are the config it writes",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s)")
        return 0
    for t, op, where, set_ in ops:
        apply_logged(conn, RUN_ID, t, op, where, set_)
    conn.commit()
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    if pathlib.Path(a.db).resolve() == DEFAULT_DB.resolve():
        print(f"archived: {archive_migration(conn, RUN_ID, __file__)}")
        conn.commit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
