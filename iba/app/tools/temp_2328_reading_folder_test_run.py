"""temp_2328_reading_folder_test_run.py -- escalation #2328 test plan, on a COPY of the live iba.db and of the reading files (never the live
database or files): a reading is filed in its home cluster's folder, resolved from the configs. Real data: the 95 live clusters (every
folder name by the convention must be the folder that already exists under _analytics/Clusters) and the nine existing readings (M21 and
M64). Synthetic: a setting without the placeholder is used as it stands, an unknown cluster is refused, a second run and a target folder
that already holds files are refused. Usage: python iba/app/tools/temp_2328_reading_folder_test_run.py <scratch dir>.
Prints PASS/FAIL per case."""
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
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import Db  # noqa: E402
from iba.app.lib import filingkit  # noqa: E402
from iba.app.lib import reading as rd  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402
from iba.app.handlers import reading as hr  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2328run"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
_pre = ROOT / "backups/iba-pre-2328-folders-20261028.db"                 # the database before the folders moved (backup API copy)
DB = copy_db(S / "iba.db", _pre if _pre.exists() else ROOT / "iba/app/db/iba.db")
R = S / "root"                                                    # the scratch project root
# the readings as they were filed before the move: rebuilt from the record of the move (old path <- new path)
_rec = ROOT / "outputs/escalation/2328-reading-folder-moves-v1-20261028.tsv"
for _l in _rec.read_text(encoding="utf-8").splitlines()[1:]:
    _label, _old, _new = _l.split("	")
    (R / _old).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT / _new, R / _old)
for _m in ("analysis_phase_1_2320_v4_20261028.py",):               # the rules the build reads from config (settings the older copy lacks)
    _p = ROOT / "iba/app/migration" / _m
    _p = _p if _p.exists() else ROOT / "iba/app/migration/archive" / _m
    subprocess.run([sys.executable, str(_p), "--db", str(DB)], capture_output=True, text=True, check=True,
                   env={**__import__("os").environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"})
MIG = ROOT / "iba/app/migration/reading_folders_in_cluster_folder_2328_v1_20261028.py"
MIG = MIG if MIG.exists() else ROOT / "iba/app/migration/archive" / MIG.name
res = []


def case(cid, desc, ok, ev=""):
    ok = bool(ok)
    res.append(ok)
    print(f"{cid} {'PASS' if ok else 'FAIL'} {desc}" + ("" if ok else f"  -- {str(ev)[:900]}"), flush=True)


def mig(*a):
    r = subprocess.run([sys.executable, str(MIG), "--db", str(DB), "--root", str(R), *a], capture_output=True, text=True,
                       env={**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"})
    return (r.stdout or r.stderr).strip()


conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
q = lambda sql, *a: conn.execute(sql, a).fetchall()
# ── N: the folder name, from the cluster rows ─────────────────────────────────────────────────────
real = {p.name for p in (ROOT / "_analytics/Clusters").iterdir() if p.is_dir()}
codes = [r[0] for r in q("SELECT cluster_code FROM cluster WHERE coalesce(deleted,0)=0")]
names = {c: filingkit.cluster_folder_name(conn, c) for c in codes}
case("N1", "the convention gives, for every live cluster, the folder that already exists under _analytics/Clusters",
     len(codes) >= 90 and all(n in real for n in names.values()), [n for n in names.values() if n not in real][:5])
case("N2", "M21 is 'M21 - fasting-piety' and M64 is 'M64 - will-resolve'",
     names["M21"] == "M21 - fasting-piety" and names["M64"] == "M64 - will-resolve", (names["M21"], names["M64"]))
try:
    filingkit.cluster_folder_name(conn, "ZZ99")
    case("N3", "an unknown cluster is refused", False, "it returned a name")
except ValueError as exc:
    case("N3", "an unknown cluster is refused", "no folder name" in str(exc), str(exc))
# ── M: the migration over the existing readings ───────────────────────────────────────────────────
rows = q("SELECT id, label, home_cluster, gap_file, observe_file, synergy_file, narrate_file FROM reading ORDER BY id")
files_before = sorted(p.relative_to(R).as_posix() for p in (R / "outputs/reading").rglob("*") if p.is_file())
dry = mig("--dry-run")
case("M1", "the dry run names the folders and files to move and writes nothing",
     dry.startswith("DRY RUN") and f"{len(rows)} reading folder(s)" in dry
     and sorted(p.relative_to(R).as_posix() for p in (R / "outputs/reading").rglob("*") if p.is_file()) == files_before, dry[:300])
out = mig()
case("M2", "the apply moves every reading folder and reports it", f"{len(rows)} reading folder(s)" in out and f"{len(files_before)} file(s) moved" in out, out[:300])
conn.close()
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
files_after = sorted(p.relative_to(R).as_posix() for p in (R / "_analytics/Clusters").rglob("*") if p.is_file())
case("M3", "every file is in a home cluster folder under <label>/ and none is left in outputs/reading (nothing lost, nothing deleted)",
     len(files_after) == len(files_before) and not [p for p in (R / "outputs/reading").rglob("*") if p.is_file()]
     and all(f.startswith("_analytics/Clusters/M") for f in files_after), (len(files_before), len(files_after)))
rows2 = q("SELECT label, home_cluster, gap_file, observe_file, synergy_file, narrate_file FROM reading ORDER BY id")
ok_paths = all((R / (r[c])).is_file() for r in rows2 for c in ("gap_file", "observe_file", "synergy_file", "narrate_file") if r[c])
case("M4", "each reading row points at its moved files, and the files exist", ok_paths, [tuple(r) for r in rows2][:2])
case("M5", "the folder is the home cluster's by the convention",
     all(r["gap_file"].startswith(f"_analytics/Clusters/{names[r['home_cluster']]}/{r['label']}/") for r in rows2), [r["gap_file"] for r in rows2][:3])
case("M6", "a second run is refused as already applied", mig().startswith("already applied"))
# ── C: the code resolves the folder from the configs ──────────────────────────────────────────────
cfg = Cfg(DB)
case("C1", "reading.output_dir is the pattern with {cluster_folder}", cfg.required_setting("reading.output_dir") == "_analytics/Clusters/{cluster_folder}", cfg.required_setting("reading.output_dir"))
case("C2", "out_dir of an existing reading (m21-asking) is its home cluster's folder, from the reading row",
     rd.out_dir(cfg, R, "m21-asking").relative_to(R).as_posix() == "_analytics/Clusters/M21 - fasting-piety/m21-asking")
try:
    rd.out_dir(cfg, R, "no-such-reading")
    case("C3", "out_dir of a reading that does not exist is refused", False, "it returned a folder")
except rd.Refused as exc:
    case("C3", "out_dir of a reading that does not exist is refused", "does not exist" in str(exc), str(exc))
conn.execute("UPDATE cfg_setting SET value=? WHERE key='reading.output_dir'", (json.dumps("scratch-out"),))
conn.commit()
cfg_plain = Cfg(DB)
case("C4", "a setting without the placeholder is used as it stands (nothing to resolve)",
     rd.out_dir(cfg_plain, R, "m21-asking").relative_to(R).as_posix() == "scratch-out/m21-asking")
# ── O: Open files the JSON in the cluster folder (the handler, end to end) ────────────────────────
scratch_pattern = str(S / "Clusters" / "{cluster_folder}")                 # absolute, so the handler's project root does not matter
conn.execute("UPDATE cfg_setting SET value=? WHERE key='reading.output_dir'", (json.dumps(scratch_pattern),))
conn.commit()
cfg2 = Cfg(DB)
db2 = Db(cfg2, DB)


def run(step, **params):
    params.setdefault("By", "Claude")
    return getattr(hr, step)(Ctx(db=db2, cfg=cfg2, step=None, run_id=f"RUN-TEST-{step}", word="", word_id=None,
                                 params={k: v for k, v in params.items() if v is not None}, step_id=f"reading.{step}"))


r = run("open", Label="t2328-open", Objective="folder (test)", Verse="Gen 43:27", Escalation="2328", Subgroup="M21_asking")
want = S / "Clusters" / "M21 - fasting-piety" / "t2328-open" / "t2328-open.json"
case("O1", "Open files the JSON in the home cluster's folder, resolved from the subgroup's cluster", r.condition == "ok" and want.is_file(), (r.condition, r.message[:200]))
conn2 = sqlite3.connect(DB)
row = conn2.execute("SELECT gap_file FROM reading WHERE label='t2328-open'").fetchone()
case("O2", "the reading row names that file", row is not None and row[0].replace(chr(92), "/").endswith("M21 - fasting-piety/t2328-open/t2328-open.json"), row)
r2 = run("observe", Label="t2328-open")
case("O3", "Observe finds and fills the sheet in that folder", r2.condition == "ok", r2.message[:200])
r3 = run("account", Label="t2328-open")
case("O4", "Account writes its report in the same folder", r3.condition == "ok" and any((S / "Clusters" / "M21 - fasting-piety" / "t2328-open").glob("t2328-open-account*.md")), r3.message[:300])
# ── B: synthetic refusals ─────────────────────────────────────────────────────────────────────────
blocked = R / "_analytics/Clusters/M21 - fasting-piety/m21-blocked"
blocked.mkdir(parents=True)
(blocked / "x.json").write_text("{}", encoding="utf-8")
conn2.execute("UPDATE reading SET gap_file='outputs/reading/m21-blocked/m21-blocked.json' WHERE label='t2328-open'")
conn2.execute("DELETE FROM cfg_change_detail WHERE run_id='DEVMODE-2328-READING-FOLDERS-20261028'")
conn2.commit()
(R / "outputs/reading/m21-blocked").mkdir(parents=True)
(R / "outputs/reading/m21-blocked/m21-blocked.json").write_text("{}", encoding="utf-8")
conn2.execute("UPDATE reading SET label='m21-blocked' WHERE label='t2328-open'")
conn2.commit()
out2 = mig("--dry-run")
case("B1", "a target folder that already holds files is refused, nothing moved", out2.startswith("REFUSED") and (R / "outputs/reading/m21-blocked/m21-blocked.json").is_file(), out2[:300])
print(f"\n{sum(res)} of {len(res)} cases pass")
