"""temp_2325_node_move_test_run.py -- escalation #2325 test plan, on a COPY of the live iba.db (never the live DB): moving a node to
another observation (specification 4.1, the words that bear on an act are nodes of the act's observation) through Record, end to end,
with the exact sheet that failed (reading m21-gen43-27-b, Gen 43:27: the nodes of welfare, father and well moved to observation
20607, which already holds a node at seq 1). Usage: python iba/app/tools/temp_2325_node_move_test_run.py <scratch dir>.
Prints PASS/FAIL per case."""
import json
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
from iba.app.handlers.base import Ctx  # noqa: E402
from iba.app.handlers import reading as hr  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402

LABEL = "m21-gen43-27-b"
S = pathlib.Path(sys.argv[1]) / "t2325run"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
# the failed sheet: the reading's folder as the failed Record left it (nothing was written)
SRC = ROOT / "outputs/reading" / LABEL
FAILED = ROOT / "backups/m21-gen43-27-b-failed-record-20261028.json"
if not FAILED.exists():
    FAILED.parent.mkdir(exist_ok=True)
    shutil.copy(SRC / f"{LABEL}.json", FAILED)
LIVE = ROOT / "backups/iba-pre-2325-seq-move-20261028.db"           # the live database before the fix, kept as the test source
if not LIVE.exists():
    copy_db(LIVE, ROOT / "iba/app/db/iba.db")           # the backup API: a plain file copy of a WAL database misses what is in the WAL
DB = copy_db(S / "iba.db", LIVE)
for _m in ("analysis_phase_1_2320_v4_20261028.py",):               # the rules the build reads from config (settings the older copy lacks)
    _p = ROOT / "iba/app/migration" / _m
    _p = _p if _p.exists() else ROOT / "iba/app/migration/archive" / _m
    subprocess.run([sys.executable, str(_p), "--db", str(DB)], capture_output=True, text=True, check=True,
                   env={**__import__("os").environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"})
(S / "reading" / LABEL).mkdir(parents=True)
shutil.copy(FAILED, S / "reading" / LABEL / f"{LABEL}.json")
c = sqlite3.connect(DB)
c.execute("UPDATE cfg_setting SET value=? WHERE key='reading.output_dir'", (json.dumps(str(S / "reading")),))
# the reading row names its JSON relative to the project root: point the COPY at the scratch file, so the live reading is never written
c.execute("UPDATE reading SET gap_file=?, observe_file=? WHERE label=?", (str(S / "reading" / LABEL / f"{LABEL}.json"),) * 2 + (LABEL,))
c.commit()
c.close()
cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
res = []


def case(cid, desc, ok, ev=""):
    ok = bool(ok)
    res.append(ok)
    print(f"{cid} {'PASS' if ok else 'FAIL'} {desc}" + ("" if ok else f"  -- {str(ev)[:900]}"), flush=True)


def q(sql, *a):
    return conn.execute(sql, a).fetchall()


def run(step, **params):
    params.setdefault("By", "Claude")
    return getattr(hr, step)(Ctx(db=db, cfg=cfg, step=None, run_id=f"RUN-TEST-{step}", word="", word_id=None,
                                 params={k: v for k, v in params.items() if v is not None}, step_id=f"reading.{step}"))


d = json.loads((S / "reading" / LABEL / f"{LABEL}.json").read_text(encoding="utf-8"))
sh = d["verses"][0]["sheet"]
moves = [(n["node"], na["set"]["observation_id"]) for e in sh["existing"] for n in e["nodes"]
         for na in ((e.get("action") or {}).get("nodes") or []) if na.get("node") == n["node"]
         and (na.get("set") or {}).get("observation_id")]
case("N0", "the failed sheet moves nodes onto an observation that already holds a node at seq 1",
     len(moves) >= 1 and all(q("SELECT count(*) FROM ib_node WHERE observation_id=? AND seq=1", tgt)[0][0] == 1 for _, tgt in moves), moves)
before = {nid: tuple(q("SELECT observation_id, seq FROM ib_node WHERE id=?", nid)[0]) for nid, _ in moves}
r = run("record", Label=LABEL)
case("N1", "Record no longer fails on the moved nodes' seq: the verse is recorded", r.condition == "ok", r.message[:400])
after = {nid: tuple(q("SELECT observation_id, seq, deleted FROM ib_node WHERE id=?", nid)[0]) for nid, _ in moves}
case("N2", "each moved node is on its target observation with a seq no other node of it holds",
     all(after[nid][0] == tgt for nid, tgt in moves)
     and all(q("SELECT count(*) FROM ib_node WHERE observation_id=? AND seq=?", tgt, after[nid][1])[0][0] == 1 for nid, tgt in moves),
     (before, after))
case("N3", "each move is kept in ib_observation_change with its reason (the observation and the seq)",
     all(q("SELECT count(*) FROM ib_observation_change WHERE node_id=? AND column_name='observation_id'", nid)[0][0] >= 1
         and q("SELECT count(*) FROM ib_observation_change WHERE node_id=? AND column_name='seq'", nid)[0][0] >= 1 for nid, _ in moves))
case("N4", "the observations the nodes left (no node now) are soft deleted, with nothing physically deleted",
     all(q("SELECT deleted FROM ib_observation WHERE id=?", b[0])[0][0] == 1 for b in before.values()
         if q("SELECT count(*) FROM ib_node WHERE observation_id=? AND deleted=0", b[0])[0][0] == 0))
# the unit: a second move onto the same observation in one go takes the next seq again
tgt0 = moves[0][1] if moves else None
nid_x = q("SELECT id FROM ib_node WHERE observation_id<>? AND deleted=0 AND verse_reference='Gen.43.27' LIMIT 1", tgt0)
if nid_x and tgt0:
    mx = q("SELECT max(seq) FROM ib_node WHERE observation_id=?", tgt0)[0][0]
    orec.modify_node(cfg, conn, nid_x[0][0], {"observation_id": tgt0}, "test: a node moved by the direct call", None, "T", "Claude")
    case("N5", "modify_node on its own gives a moved node the next seq of the target",
         q("SELECT seq FROM ib_node WHERE id=?", nid_x[0][0])[0][0] == mx + 1)
else:
    case("N5", "(no further node on this verse to move)", True)

# ── S: the surface of a code in a multi-code span (researcher: "according to STEP it is 'still' not alive") ─────────
from iba.app.lib import reading as rd  # noqa: E402
vid = q("SELECT id FROM verse WHERE osisId='Gen.43.27'")[0][0]
osr = orec.occurrence_surfaces(conn, [vid])
h5750 = q("SELECT id FROM verse_lexical WHERE verse_id=? AND strong='H5750' AND deleted=0", vid)[0][0]
h2416 = q("SELECT id FROM verse_lexical WHERE verse_id=? AND strong='H2416A' AND deleted=0", vid)[0][0]
case("S1", "the surface of H5750 in Gen 43:27 is STEP's 'still', that of H2416A stays 'alive', verse_lexical is not changed",
     osr[h5750]["surface_here"] == "still" and osr[h5750]["span_surface"] == "alive" and osr[h2416]["surface_here"] == "alive"
     and q("SELECT surface FROM verse_lexical WHERE id=?", h5750)[0][0] == "alive", (osr[h5750], osr[h2416]))
r = run("open", Label="t2325-s", Objective="surface (test)", Verse="Gen 43:27", Escalation="2325", Subgroup="M21_asking")
r = run("observe", Label="t2325-s")
dd = json.loads((S / "reading" / "t2325-s" / "t2325-s.json").read_text(encoding="utf-8"))
sheet = dd["verses"][0]["sheet"]
g5750 = next(g for g in sheet["surfaces"] if g["strong"] == "H5750")
case("S2", "the sheet names the word as STEP glosses it, with the span's word and the gloss beside it",
     g5750["word"] == "still (H5750)" and g5750["span_surface"] == "alive" and g5750["step_gloss"] == "still", g5750)
bad = [n for e in sheet["existing"] for n in e["nodes"] if n["word"].endswith("(H5750)") and n["word"].startswith("alive")]
case("S3", "an existing node of H5750 written 'alive' is flagged surface_differs with a proposed fix",
     bad and all(any(f["code"] == "surface_differs" for f in n["flags"]) and n["suggest"] and n["suggest"].get("surface") == "still" for n in bad),
     [(n["node"], n["flags"], n["suggest"]) for n in bad])
for e in sheet["existing"]:
    e["action"] = {"action": "accept"}
errs = []
plan = rd._validate_sheet(cfg, conn, dd["verses"][0], errs)
fills = [(nid, sug) for nid, sug in plan["fill"] if sug.get("surface")]
case("S4", "the fix is part of the check: a node surface suggestion is in what Record writes", len(fills) >= len(bad) and fills, fills)
sp = {"key": "f", "kind": "statement", "text": "test finding for the surface of still", "basis": "stated",
      "nodes": [{"strong": "H5750", "occurrence": h5750, "role": "qualifier", "cluster": "T2"}]}
e2, qt = [], []
pl2 = orec.check(cfg, [("t", sp)], e2, qt)
case("S5", "a new node on the occurrence takes the surface 'still' and keeps the span's word for the subgroup pair lookup",
     pl2 and pl2[0]["nodes"] and pl2[0]["nodes"][0]["surface"] == "still" and pl2[0]["nodes"][0]["pair_surface"] == "alive",
     (e2, pl2 and pl2[0]["nodes"]))

print(f"\n{sum(res)} of {len(res)} cases pass")
