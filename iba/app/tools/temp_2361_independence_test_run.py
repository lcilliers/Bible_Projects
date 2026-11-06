"""temp_2361_independence_test_run.py -- the independence test of escalation #2361 (design v3, section 9): with the working files moved away, every module of
the surface cycle still runs from the tables. A copy of iba.db is made with lib/dbsnapshot.copy_db, the working-files and exports folders are pointed at
empty folders, open() is patched to refuse any path under _analytics or outputs, and the status, show, export and re-run (preview) steps of the five modules
and the AI control are run. Then the generated sections of the config report (the surface cycle and the AI use map) are made.

Usage: python iba/app/tools/temp_2361_independence_test_run.py <scratch dir>
"""
import builtins
import json
import pathlib
import shutil
import subprocess
import sys
import types

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers import ai as HA  # noqa: E402
from iba.app.handlers import collectionbuild as HC  # noqa: E402
from iba.app.handlers import surfacegroup as HG  # noqa: E402
from iba.app.handlers import surfaceresolve as HR  # noqa: E402
from iba.app.handlers import surfacestructure as HS  # noqa: E402
from iba.app.lib import surfacecyclemap  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402

results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:300]))


S = pathlib.Path(sys.argv[1]) / "t2361i"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
for name in ("surface_structure_2361_v1_20261106.py", "surface_group_2361_v1_20261106.py", "surface_resolve_2361_v1_20261106.py", "ai_client_2361_v1_20261106.py",
             "surface_collection_2361_v1_20261106.py", "surface_collection_ask_2361_v1_20261106.py", "surface_maps_2361_v1_20261106.py", "surface_maps_fix_2361_v1_20261106.py", "surface_hygiene_2361_v1_20261106.py"):
    m = ROOT / "iba/app/migration" / name
    m = m if m.exists() else ROOT / "iba/app/migration/archive" / name
    subprocess.run([sys.executable, str(m), "--db", str(DB), "--no-snapshot"], capture_output=True, text=True)
cfg = Cfg(DB)
conn = cfg.conn
empty_wf, empty_ex = S / "no_working_files", S / "no_exports"
empty_wf.mkdir()
conn.execute("UPDATE cfg_setting SET value=? WHERE key='surfaces.working_files_root'", (json.dumps(empty_wf.as_posix()),))
conn.execute("UPDATE cfg_setting SET value=? WHERE key='surfaces.exports_root'", (json.dumps(empty_ex.as_posix()),))
conn.commit()
ctx = lambda **p: types.SimpleNamespace(cfg=cfg, params=p, run_id="TEST-RUN")  # noqa: E731

_real_open = builtins.open
touched = []


def _no_files(path, *a, **k):
    p = str(path).replace("\\", "/")
    if any(x in p for x in ("_analytics/", "outputs/")):
        touched.append(p)
        raise AssertionError(f"a working file was read: {p}")
    return _real_open(path, *a, **k)


builtins.open = _no_files
try:
    runs = [
        ("structure status", lambda: HS.status(ctx())), ("structure match -Check", lambda: HS.match(ctx(Check="true"))), ("structure show", lambda: HS.show(ctx(Surface="hides"))),
        ("group status", lambda: HG.status(ctx())), ("group repoint -Check", lambda: HG.repoint(ctx(Check="true"))),
        ("resolve status", lambda: HR.status(ctx())), ("resolve run -Check", lambda: HR.run(ctx(Check="true"))), ("resolve show", lambda: HR.show(ctx(Surface="hides"))),
        ("collection status", lambda: HC.status(ctx())), ("collection links -Check", lambda: HC.links(ctx(Check="true"))), ("collection show", lambda: HC.show(ctx(Collection="love"))),
        ("collection export", lambda: HC.export(ctx(Name="collections-v1-20261106"))),
        ("ai status", lambda: HA.status(ctx())), ("ai prompts", lambda: HA.prompts(ctx())), ("ai compare", lambda: HA.compare(ctx(Step="base"))),
    ]
    for i, (label, fn) in enumerate(runs, 1):
        o = fn()
        case(f"I{i:02d}", f"{label}: runs from the tables with no working file", o.condition == "ok", o.message.split(chr(10))[0][:90])
finally:
    builtins.open = _real_open
case("I99a", "no file under _analytics or outputs was opened by any of them", not touched, touched[:2])
case("I99b", "the export wrote its file to the exports folder (a view, regenerable)", (empty_ex / "collections-v1-20261106.csv").exists(), "")

conn.row_factory = __import__("sqlite3").Row
q = lambda sql, p=(): conn.execute(sql, p).fetchall()  # noqa: E731
cyc = surfacecyclemap.surface_cycle_map(q)
aim = surfacecyclemap.ai_use_map(q)
txt = "\n".join(cyc)
case("M1", "the generated cycle map names the six work packages, their steps and the tables each may write",
     all(w in txt for w in ("surface-group", "surface-structure", "surface-base", "surface-resolve", "collection-build", "ai-control"))
     and "collection.ask" in txt and "ai_call" in txt and "State of the study tables" in txt, len(cyc))
txt = "\n".join(aim)
case("M2", "the AI use map names the models by role, the prompts with their active version, and the modules and steps that called the AI",
     "qwen3:30b" in txt and "base.word" in txt and "ai_base" in txt and "group" in txt and "surface_base.ask" in txt, len(aim))
case("M3", "the retired file route is not in the map of the cycle's steps (surface_base.run, surface_base.status)", "surface_base.run" not in "\n".join(cyc) and "surface_base.status" not in "\n".join(cyc), "")
sec = q("SELECT section_key FROM cfg_report_section WHERE step='configmaint.report' AND include=1 AND inactive=0 ORDER BY ordinal")
case("M4", "sections 16 and 17 are registered for configmaint.report", [r[0] for r in sec][-2:] == ["surface_cycle_map", "ai_use_map"], [r[0] for r in sec][-3:])

from iba.app.lib import surfacehygiene  # noqa: E402
root = S / "proj"
(root / "_analytics" / "surfaces" / "working_files").mkdir(parents=True)
(root / "_analytics" / "surfaces" / "exports").mkdir()
(root / "_analytics" / "surfaces" / "discarded").mkdir()
conn.execute("UPDATE cfg_setting SET value=? WHERE key='surfaces.working_files_root'", (json.dumps("_analytics/surfaces/working_files"),))
conn.execute("UPDATE cfg_setting SET value=? WHERE key='surfaces.exports_root'", (json.dumps("_analytics/surfaces/exports"),))
conn.commit()
(root / "_analytics" / "surfaces" / "working_files" / "ok.json").write_text("{}")
clean = surfacehygiene.find_surface_hygiene(cfg, root)
case("H1", "hygiene: the live data has no junk surface and a file in a root is allowed", clean == [], clean[:2])
(root / "_analytics" / "surfaces" / "stray.csv").write_text("x")
conn.execute("INSERT INTO surface_term (surface, form, origin) VALUES ('what?!', 'phrase', 'surface')")
conn.commit()
bad = surfacehygiene.find_surface_hygiene(cfg, root)
case("H2", "hygiene: a junk surface not marked deleted and a stray file under _analytics/surfaces are both found",
     len(bad) == 2 and any("junk rule" in b for b in bad) and any("stray.csv" in b for b in bad), bad)

width = max(len(r[0]) for r in results)
fails = [r for r in results if r[2] == "FAIL"]
for cid, desc, res_, evd in results:
    print(f"{cid:<{width}}  {res_}  {desc}  [{evd}]")
print(f"\n{len(results) - len(fails)} of {len(results)} pass")
sys.exit(1 if fails else 0)
