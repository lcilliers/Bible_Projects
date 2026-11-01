"""temp_2355_concept_edit_test_run.py -- test plan for the concept-edit tool (escalation #2355), run on a COPY of
iba.db (never the live one). Applies the registration migration to the copy, then calls the handlers.

    python iba/app/tools/temp_2355_concept_edit_test_run.py <copy-of-iba.db>
"""
import json
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers import conceptedit as h  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

db = pathlib.Path(sys.argv[1])
if db.resolve() == (ROOT / "iba" / "app" / "db" / "iba.db").resolve():
    sys.exit("refusing to test on the live database")
MIG = str(ROOT / "iba/app/migration/concept_edit_2355_v1_20261101.py")
if not pathlib.Path(MIG).is_file():
    MIG = str(ROOT / "iba/app/migration/archive/concept_edit_2355_v1_20261101.py")
subprocess.run([sys.executable, MIG, "--db", str(db)], check=True)
again = subprocess.run([sys.executable, MIG, "--db", str(db)], capture_output=True, text=True).stdout.strip()
cfg = Cfg(db)
conn = cfg.conn
results = []


def ctx(step, **params):
    return Ctx(db=None, cfg=cfg, step=None, run_id="TEST-2355", word="", word_id=None, params=params,
               step_id=f"concept_edit.{step}")


def check(name, cond, detail=""):
    results.append(bool(cond))
    print(f"{'PASS' if cond else 'FAIL'}  {name}  {detail}")


def val(sql, *a):
    return conn.execute(sql, a).fetchone()[0]


check("migration is idempotent", again.startswith("already applied"), again)
check("4 steps, 4 refused rows, 4 write grants",
      val("select count(*) from cfg_step where work_package='concept-edit'") == 4
      and val("select count(*) from cfg_on_fail where step like 'concept_edit.%'") == 4
      and val("select count(*) from cfg_write_grant where writer like 'concept_edit.%'") == 4)
check("no grant on concept_subgroup", val("select count(*) from cfg_write_grant where writer like 'concept_edit.%' "
                                          "and table_name='concept_subgroup'") == 0)
n_con = val("select count(*) from concept")

o = h.list_(ctx("list", Level="Domain"))
check("list domains", o.condition == "ok" and o.counts["rows"] == 14, o.counts)
o = h.list_(ctx("list", Level="Concept", DomainId="1"))
check("list concepts of domain 1", o.counts["rows"] == 4, o.counts)

o = h.describe(ctx("describe", Level="Domain", Id="3", Description="  Fear and awe.  "))
check("describe domain", o.condition == "ok" and "was empty" in o.message, o.message)
check("description trimmed; updated_at and run_id set",
      val("select description from concept_domain where id=3") == "Fear and awe."
      and val("select updated_at from concept_domain where id=3")
      and val("select run_id from concept_domain where id=3") == "TEST-2355")
o = h.describe(ctx("describe", Level="Domain", Id="3", Description="Fear, dread and awe."))
check("an edit shows the wording replaced", "was: Fear and awe." in o.message, o.message)
o = h.describe(ctx("describe", Level="Concept", Id="5", Description="A concept."))
check("describe concept", o.condition == "ok" and val("select description from concept where id=5") == "A concept.")
check("describe refuses empty", h.describe(ctx("describe", Level="Concept", Id="5", Description="  ")).condition == "refused")
check("describe refuses unknown id", h.describe(ctx("describe", Level="Concept", Id="99999", Description="x")).condition == "refused")
check("describe refuses a bad level", h.describe(ctx("describe", Level="Subgroup", Id="1", Description="x")).condition == "refused")
check("describe refuses a non-number id", h.describe(ctx("describe", Level="Concept", Id="abc", Description="x")).condition == "refused")

tmp = pathlib.Path(tempfile.mkdtemp()) / "d.json"
tmp.write_text(json.dumps([{"level": "Concept", "id": 6, "description": "six"},
                           {"level": "Domain", "id": 4, "description": "four"}]), encoding="utf-8")
o = h.describe(ctx("describe", File=str(tmp)))
check("describe from -File, both levels", o.condition == "ok" and o.counts["changes"] == 2
      and val("select description from concept where id=6") == "six")
tmp.write_text(json.dumps([{"level": "Concept", "id": 7, "description": "seven"},
                           {"level": "Concept", "id": 99999, "description": "x"}]), encoding="utf-8")
o = h.describe(ctx("describe", File=str(tmp)))
check("a refusal in -File writes nothing (unit)",
      o.condition == "refused" and val("select description from concept where id=7") is None, o.message)
tmp.write_text("{not json", encoding="utf-8")
check("bad JSON refused", h.describe(ctx("describe", File=str(tmp))).condition == "refused")

o = h.add_domain(ctx("add_domain", Name="Rest and peace", Description="Quiet.", By="Researcher"))
new = val("select max(id) from concept_domain")
check("add domain: next ordinal, writer, description",
      o.condition == "ok" and val("select ordinal from concept_domain where id=?", new) == 15
      and val("select created_by from concept_domain where id=?", new) == "Researcher"
      and val("select description from concept_domain where id=?", new) == "Quiet.", o.message)
check("new domain has no concepts and a NULL chapter",
      val("select count(*) from concept where domain_id=?", new) == 0
      and val("select narrative_chapter_id from concept_domain where id=?", new) is None)
check("add refuses a duplicate live name", h.add_domain(ctx("add_domain", Name="Rest and peace")).condition == "refused")
check("add refuses a taken ordinal", h.add_domain(ctx("add_domain", Name="Other", Ordinal="3")).condition == "refused")
check("add refuses empty name", h.add_domain(ctx("add_domain", Name=" ")).condition == "refused")
check("add refuses non-number ordinal", h.add_domain(ctx("add_domain", Name="Other", Ordinal="x")).condition == "refused")
o = h.add_domain(ctx("add_domain", Name="Chosen order", Ordinal="40"))
check("add with a given ordinal", o.condition == "ok"
      and val("select ordinal from concept_domain where name='Chosen order'") == 40)

o = h.set_deleted(ctx("set_deleted", Id="1", Deleted="1"))
check("delete refused while the domain holds live concepts, and names them",
      o.condition == "refused" and "4 live concept(s)" in o.message
      and val("select deleted from concept_domain where id=1") == 0, o.message[:120])
o = h.set_deleted(ctx("set_deleted", Id=str(new), Deleted="1"))
check("delete an empty domain", o.condition == "ok" and val("select deleted from concept_domain where id=?", new) == 1,
      o.message)
check("delete again refused", h.set_deleted(ctx("set_deleted", Id=str(new), Deleted="1")).condition == "refused")
check("describe refuses a deleted domain",
      h.describe(ctx("describe", Level="Domain", Id=str(new), Description="x")).condition == "refused")
check("list hides deleted; -IncludeDeleted shows it",
      h.list_(ctx("list", Level="Domain")).counts["rows"] == 15
      and h.list_(ctx("list", Level="Domain", IncludeDeleted="1")).counts["rows"] == 16)
h.add_domain(ctx("add_domain", Name="Rest and peace"))   # a live domain with the deleted one's name
check("a deleted name can be reused (live-unique index)",
      val("select count(*) from concept_domain where name='Rest and peace'") == 2)
check("restore refused when a live domain has the name",
      h.set_deleted(ctx("set_deleted", Id=str(new), Deleted="0")).condition == "refused")
check("deleted must be 0 or 1", h.set_deleted(ctx("set_deleted", Id="2", Deleted="2")).condition == "refused")
check("-By must be Claude or Researcher", h.add_domain(ctx("add_domain", Name="Z", By="Someone")).condition == "refused")

check("concept_subgroup untouched (411 rows)", val("select count(*) from concept_subgroup") == 411)
check("concept rows unchanged in number", val("select count(*) from concept") == n_con)
check("live domains: 14 + Chosen order + the second Rest and peace",
      val("select count(*) from concept_domain where deleted=0") == 16, val("select count(*) from concept_domain where deleted=0"))
conn.commit()
print(f"\n{sum(results)} of {len(results)} PASS")
sys.exit(0 if all(results) else 1)
