"""stage_wording_2528_v1_20261121.py -- escalation #2528 (build brief B3, finding F3 and F8 of outputs/escalation/2526-stages-1-to-4-readiness-audit-v1-20261121.md).

One wording of which steps of the layered reading belong to which stage of the study, the Programme book's (Programme flow): stage 1 the lexical analysis is step S1; stage 2 the grouping of
the surfaces (GroupPull, GroupRecord); stage 3 the verse-lexical observations are steps 1.1, 1.2 and 2.1; stage 4 the inner-being analysis is steps 3.1, 3.2 and 3.3; stage 5 undecided. Written to:
  - cfg_setting layer.reading: a `stage` on each step (the study stage it belongs to), so the mapping is config and not prose;
  - cfg_behaviour_rule 132 collection-reading-runs-in-layers: the stage 2 and stage 3 sentences and the stage 4 sentence; the layers named in the steps are 1 to 3;
  - cfg_method_rule GP-01 meaning-from-the-dictionary: the grouping is judged from the dictionary meaning without the verses, as the Programme book states (The analytical grouping).
Every write is apply_logged. Idempotent.

Usage:
    python iba/app/migration/stage_wording_2528_v1_20261121.py [--db PATH]
After a live run, move this file to iba/app/migration/archive/ (rule 96).
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2528-STAGE-WORDING-20261121"
STAGE_OF = {"S1": 1, "1.1": 3, "1.2": 3, "2.1": 3, "3.1": 4, "3.2": 4, "3.3": 4}

R132_OLD = ("(Collection-Build.ps1 GroupPull and GroupRecord; Subgroup for the researcher's corrections); step 1.1 records each group as an observation of the meaning its surfaces share. "
            "Stage 3, verse-lexical only (steps 1.2 and 2.1): each group's Strong's codes are studied and the grouping validated; then what the other words of the verse show with each group "
            "(pairings, qualifiers and the words they reach, entities, direction, the relation between groups, a double meaning), each an observation with its nodes. "
            "Stage 4, the inner-being analysis made from the stage 3 observations, is not yet built; stage 5, the claim formulation, is not yet decided.")
R132_NEW = ("(Collection-Build.ps1 GroupPull and GroupRecord; Subgroup for the researcher's corrections). "
            "Stage 3, verse-lexical only (steps 1.1, 1.2 and 2.1, which open only when the grouping is finished; the stage of each step is `stage` in cfg_setting layer.reading): step 1.1 records each group as an observation "
            "of the meaning its surfaces share; step 1.2 studies each group's Strong's codes and validates the grouping; step 2.1 records what the other words of the verse show with each group "
            "(pairings, qualifiers and the words they reach, entities, direction, the relation between groups, a double meaning), each an observation with its nodes. "
            "Stage 4, the inner-being analysis made from the stage 3 observations, is required and is the steps 3.1 (specific behaviours), 3.2 (groups of behaviours) and 3.3 (across subgroups and collections), "
            "which open only when stage 3 is closed for the collection (lib/layerinner.py; rules IB-01 to IB-06); stage 5, the claim formulation, is not yet decided.")
R132_LAYERS_OLD = "The layers 1 and 2 named in the steps are the collection reading's"
R132_LAYERS_NEW = "The layers 1 to 3 named in the steps are the collection reading's"
GP01_OLD = " A verse is read only where the dictionary leaves two groups open."
GP01_NEW = " The grouping is judged without the verses (Programme book, The analytical grouping)."


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = 0
    with conn:
        lay = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.reading'").fetchone()[0])
        before = json.dumps(lay, sort_keys=True)
        for st in lay["steps"]:
            st["stage"] = STAGE_OF[st["key"]]
        if json.dumps(lay, sort_keys=True) != before:
            use = conn.execute("SELECT use FROM cfg_setting WHERE key='layer.reading'").fetchone()[0]
            if "`stage`" not in use:
                use += " Each step carries `stage`, the stage of the study it belongs to: S1 stage 1, 1.1, 1.2 and 2.1 stage 3, 3.1 to 3.3 stage 4 (the Programme book, Programme flow; stage 2 is the grouping, GroupRecord)."
            apply_logged(conn, RUN_ID, "cfg_setting", "update", {"key": "layer.reading"}, {"value": json.dumps(lay, ensure_ascii=False), "use": use})
            n += 1
        t = conn.execute("SELECT rule_text FROM cfg_behaviour_rule WHERE id=132").fetchone()[0]
        t2 = t.replace(R132_OLD, R132_NEW).replace(R132_LAYERS_OLD, R132_LAYERS_NEW)
        if t2 != t:
            apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "update", {"id": 132}, {"rule_text": t2})
            n += 1
        g = conn.execute("SELECT rule_text FROM cfg_method_rule WHERE id=243").fetchone()[0]
        g2 = g.replace(GP01_OLD, GP01_NEW)
        if g2 != g:
            apply_logged(conn, RUN_ID, "cfg_method_rule", "update", {"id": 243}, {"rule_text": g2})
            n += 1
    print(f"{n} cfg write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
