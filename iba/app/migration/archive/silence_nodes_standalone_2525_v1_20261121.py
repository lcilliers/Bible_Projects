"""silence_nodes_standalone_2525_v1_20261121.py -- escalation #2525 (researcher ruling, 2026-11-21).

A surface judged standalone in a verse is written to the observation, so the engagement step's no-bearing nodes
carry the role standalone (and a re-evaluation of the verse reconsiders it). This migration:
  - adds cfg_setting engagement.no_bearing_role = "standalone" (apply_logged);
  - sets the role standalone on every live node of a live engagement silence observation that has none, each change
    kept in ib_observation_change with its reason (observationrecord.log). A node that already has a role is not touched.
Idempotent.

Usage:
    python iba/app/migration/silence_nodes_standalone_2525_v1_20261121.py [--db PATH]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2525-SILENCE-NODES-STANDALONE-20261121"
KEY = "engagement.no_bearing_role"
REASON = ("researcher ruling on #2525, 2026-11-21: a surface judged standalone in a verse is written to the "
          "observation with the role standalone; the engagement silence node had no role")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n_cfg = n_nodes = 0
    with conn:
        if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (KEY,)).fetchone():
            apply_logged(conn, RUN_ID, "cfg_setting", "insert", {},
                         {"key": KEY, "value": json.dumps("standalone"), "module": "engagement", "inactive": 0,
                          "use": ("the role a node takes when its surface was judged to have no bearing in the verse "
                                  "(the no-bearing kind of observation): the word was read and holds nothing for the "
                                  "inner being (cfg_setting reading.node_roles, recognised). Escalation #2525.")})
            n_cfg += 1
        stage = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='engagement.stage'").fetchone()[0])
        kind = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='engagement.no_bearing_kind'").fetchone()[0])
        rows = conn.execute("SELECT n.id, n.observation_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id "
                            "WHERE n.deleted=0 AND o.deleted=0 AND o.stage=? AND o.tag=? AND n.role IS NULL",
                            (stage, kind)).fetchall()
        for nid, oid in rows:
            orec.log(conn, oid, nid, "role", None, "standalone", REASON, None, RUN_ID, "claude_code")
            conn.execute("UPDATE ib_node SET role='standalone' WHERE id=?", (nid,))
            n_nodes += 1
    print(f"{n_cfg} cfg write(s), {n_nodes} node(s) set to standalone (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
