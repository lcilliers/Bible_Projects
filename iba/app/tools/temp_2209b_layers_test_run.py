"""temp_2209b_layers_test_run.py -- test plan for escalation #2209 part (b), rows 1 to 5: the start
delivers and the compliance file restates the general rules only (rows 1-3), the
undelivered-conversational-rules check is retired (row 4), and Escalation.ps1 -Action Context takes
-Id (row 5). Run on a copy of iba.db made with lib/dbsnapshot.copy_db; compliance files are written to
the scratch folder, not Logs/.

Usage: python iba/app/tools/temp_2209b_layers_test_run.py <scratch dir>
"""
import pathlib
import shutil
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import dbsnapshot, compliance, cfgquality, cfgreport, escalationcontext  # noqa: E402
from iba.app.lib import escalation as esc  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import Db  # noqa: E402
from iba.app.handlers import configmaint  # noqa: E402

scratch = pathlib.Path(sys.argv[1])
if scratch.exists():
    shutil.rmtree(scratch)
scratch.mkdir(parents=True)
results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:400]))


copy = dbsnapshot.copy_db(scratch / "iba.db")
cfg = Cfg(copy)
db = Db(cfg, copy)
conn = cfg.conn

dev, std = compliance.rules(conn, "developer"), compliance.rules(conn, "standard")
general = {r for (r,) in conn.execute("SELECT rule_ref FROM cfg_rule_scope WHERE inactive=0 AND scope_kind='general'")}
case("T1", "rows 1-2: only general rules are delivered (developer 41, standard 40)",
     len(dev) == 41 and len(std) == 40 and all(r["id"] in general for r in dev),
     f"developer {len(dev)}, standard {len(std)}")
lines = compliance.deliver_lines(conn, "developer")
case("T2", "the start print says how many rules come at their point of use",
     "122 more rules reach you at their point of use" in lines[-1], lines[-1])

conn.execute("ALTER TABLE cfg_rule_scope RENAME TO cfg_rule_scope_t3")
n_all = len(compliance.rules(conn, "developer"))
conn.execute("ALTER TABLE cfg_rule_scope_t3 RENAME TO cfg_rule_scope")
case("T3", "synthetic: with no cfg_rule_scope every rule is delivered (fails open to reading)",
     n_all > 130, f"{n_all} delivered")


def compliance_file(name, ids, extra=None):
    rows = "\n".join(f"| {i} | not engaged | test row {n} for case {name}, unique wording {n * 7} |  |"
                     for n, i in enumerate(ids + (extra or [])))
    p = scratch / f"{name}.md"
    p.write_text(f"# test\n\nMode: developer\n\n## Acknowledgement\n\n"
                 f"{cfg.required_setting('compliance.acknowledgement')}\n\n## Rules\n\n"
                 f"| id | status | requires / reason | evidence |\n|---|---|---|---|\n{rows}\n\n"
                 f"## Conflicts and rules not followed\n\n## Close dispositions\n", encoding="utf-8")
    return p


ids = [r["id"] for r in dev]
f4 = compliance.check_start(cfg, compliance_file("t4", ids))
case("T4", "row 2: a compliance file with the 41 general rows passes the start check", f4 == [], f4)
f5 = compliance.check_start(cfg, compliance_file("t5", ids, ["B:63"]))
case("T5", "synthetic: a row for an operation rule is a finding (not delivered at start)",
     len(f5) == 1 and f5[0]["key"] == "B:63", f5)
f6 = compliance.check_start(cfg, compliance_file("t6", ids[1:]))
case("T6", "synthetic: a missing general row is a finding", len(f6) == 1 and f6[0]["key"] == ids[0], f6)
f7 = compliance.check_close(cfg, compliance_file("t7", ids), None)
case("T7", "row 3: the close check (SC6) reads the file's rows only, so it covers the general rules",
     f7 == [], f7)

case("T8", "row 4: the undelivered-conversational-rules check is gone from cfgquality, validate and the report",
     not hasattr(cfgquality, "find_undelivered_conversational_rules")
     and "undelivered" not in pathlib.Path(configmaint.__file__).read_text(encoding="utf-8")
     and "undelivered" not in pathlib.Path(cfgreport.__file__).read_text(encoding="utf-8"), "absent")

one = escalationcontext.collect(cfg, db, 2209)
refs = [r["resolved"] or r["named"] for r in one[0]["refs"]] if one else []
case("T9", "row 5: Context -Id reads one escalation's files",
     len(one) == 1 and any("2209-layer-review" in (x or "") for x in refs), f"{len(one)} item, {len(refs)} files")
parked = conn.execute("SELECT id FROM escalation WHERE state='on-hold' AND type!='thread' ORDER BY id LIMIT 1").fetchone()[0]
one_p = escalationcontext.collect(cfg, db, parked)
case("T10", "row 5: -Id works for a parked item too (read when taken up)",
     len(one_p) == 1 and one_p[0]["escalation"]["id"] == parked, f"#{parked}")
all_open = escalationcontext.collect(cfg, db)
n_open = len(db.rows(f"SELECT id FROM escalation WHERE type!='thread' AND state IN "
                     f"({','.join('?' * len(esc.state_group(db, 'open')))})", esc.state_group(db, "open")))
case("T11", "without -Id it still covers every open escalation", len(all_open) == n_open,
     f"{len(all_open)} of {n_open}")
none = escalationcontext.collect(cfg, db, 999999)
case("T12", "synthetic: an unknown id gives no item, not an error", none == [], none)

cfg.close()
out = scratch / "results.md"
out.write_text("| case | what | result | evidence |\n|---|---|---|---|\n" +
               "\n".join(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in results) + "\n", encoding="utf-8")
print(out.read_text(encoding="utf-8"))
print(f"{sum(r[2] == 'PASS' for r in results)}/{len(results)} pass")
