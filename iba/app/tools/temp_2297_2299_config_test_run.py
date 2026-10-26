"""temp_2297_2299_config_test_run.py -- the test of escalations #2297 and #2299 (#2286 U7, U9, config only). Runs on a
copy of iba.db made with lib/dbsnapshot.copy_db; the migration is applied to the copy only.

Usage: python iba/app/tools/temp_2297_2299_config_test_run.py <scratch dir>
"""
import json
import os
import pathlib
import shutil
import sqlite3
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib import cfgquality as cq  # noqa: E402
from iba.app.handlers import configmaint as cm  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2297"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
# from the pre-run snapshot, so the copy is as live was before the migration
DB = copy_db(S / "iba.db", ROOT / "iba/app/db/snapshots/iba-20261026T0900Z-pre-2295-2297-2299.db")
env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"}


def migrate(name):
    m = ROOT / "iba/app/migration" / name
    m = m if m.exists() else ROOT / "iba/app/migration/archive" / name
    return [(lambda r: (r.stdout or r.stderr).strip())(subprocess.run([sys.executable, str(m), "--db", str(DB)] + x,
                                                                      capture_output=True, text=True, env=env))
            for x in (["--dry-run"], [], [])]


mo = migrate("t_word_and_retire_2297_2299_v1_20261026.py")
mg = migrate("retire_grants_2299_v1_20261026.py")
conn = sqlite3.connect(DB)
for (k, v) in conn.execute("SELECT key, value FROM cfg_setting WHERE key LIKE 'database.%.path' AND inactive=0").fetchall():
    conn.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(str(ROOT / json.loads(v))), k))
conn.commit()
conn.row_factory = sqlite3.Row
live = sqlite3.connect(f"file:{(ROOT / 'iba/app/db/iba.db').as_posix()}?mode=ro", uri=True)
live.row_factory = sqlite3.Row
results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/").replace("\n", " ")[:500]))
    print(f"{cid} {'PASS' if passed else 'FAIL'}" + ("" if passed else f"  {str(evidence)[:700]}"), flush=True)


case("C1", "each migration: dry run, apply (8 writes; 11 grants + 1 registration), re-run writes nothing",
     "DRY RUN -- 8 write(s)" in mo[0] and mo[1].startswith("8 write") and mo[2].startswith("0 write") and
     "DRY RUN -- 12 write(s)" in mg[0] and mg[1].startswith("12 write") and mg[2].startswith("0 write"), (mo, mg))
r = conn.execute("SELECT step, ordinal, active FROM cfg_method_rule WHERE rule_key='RA-01 t-word-joins-cluster'").fetchone()
case("C2", "U7: RA-01 on reading.apply, active, ordinal 69", r is not None and tuple(r) == ("reading.apply", 69, 1),
     r and tuple(r))
st = dict(conn.execute("SELECT step, inactive FROM cfg_step WHERE step IN ('cluster.subgroup','cluster.reading',"
                       "'cluster.answer')").fetchall())
sc = conn.execute("SELECT count(*) FROM cfg_rule_scope WHERE scope_value='ClusterSubgroup.ps1' AND inactive=0").fetchone()[0]
b = conn.execute("SELECT enforcement_status FROM cfg_behaviour_rule WHERE id=117").fetchone()[0]
case("C3", "U9: the three pipeline steps inactive, no live rule scope on ClusterSubgroup.ps1, B:117 enforced",
     set(st.values()) == {1} and sc == 0 and b == "mechanically_enforced", (st, sc, b))
n = conn.execute("SELECT count(*) FROM cfg_change_detail WHERE run_id IN ('DEVMODE-2297-2299-T-WORD-RETIRE-20261026', "
                 "'DEVMODE-2299-RETIRE-GRANTS-20261026')").fetchone()[0]
g = conn.execute("SELECT count(*) FROM cfg_write_grant WHERE writer IN ('cluster.subgroup', 'cluster.reading', "
                 "'cluster.answer') AND inactive=0").fetchone()[0]
case("C4", "every write logged to cfg_change_detail (20); no live grant left on a retired step", n == 20 and g == 0, (n, g))
AP = ROOT / "iba/app"
checks = {"coherence": cm._validate_live, "scope_gaps": lambda x: cq.find_rule_scope_gaps(x, AP), "hedge": cq.find_hedge_phrases_in_active_config,
          "orphan": lambda x: cq.find_orphan_configs(x, AP), "no_ps": cq.find_steps_without_ps_script,
          "report_rows": cq.find_missing_cfg_report_rows}
new = {k: [x for x in fn(conn) if x not in fn(live)] for k, fn in checks.items()}
case("C5", "validate checks on the copy: no new finding", not any(new.values()), new)
new_live = {k: fn(live) for k, fn in (("coherence", cm._validate_live),)}
case("C6", "the coherence check on the copy is clean", not cm._validate_live(conn), cm._validate_live(conn))
out = S / "results.md"
out.write_text("| case | what | result | evidence |\n|---|---|---|---|\n" +
               "\n".join(f"| {a} | {b_} | {r_} | {e} |" for a, b_, r_, e in results) + "\n", encoding="utf-8")
print(f"{sum(x[2] == 'PASS' for x in results)} of {len(results)} pass -> {out}")
