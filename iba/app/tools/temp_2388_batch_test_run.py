"""temp_2388_batch_test_run.py -- tests for Engagement in batches (escalation #2388): lib/engagement.batch_plan and pull(batch=), handlers/engagement.pull -Batch,
on a COPY of iba.db (lib/dbsnapshot.copy_db), never the live one. Usage: python iba/app/tools/temp_2388_batch_test_run.py <scratch dir>"""
import json
import pathlib
import sqlite3
import sys
from types import SimpleNamespace

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers import engagement as he  # noqa: E402
from iba.app.lib import dbsnapshot, engagement as eg  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

scratch = pathlib.Path(sys.argv[1]) / "t2388batch"
scratch.mkdir(parents=True, exist_ok=True)
copy = scratch / "iba-copy.db"
copy.exists() and copy.unlink()
dbsnapshot.copy_db(copy)
cn = sqlite3.connect(copy)
for key, val in (("engagement.working_dir", scratch / "work"), ("engagement.report_path", scratch / "reports")):
    cn.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(val.as_posix()), key))
cn.execute("INSERT OR REPLACE INTO cfg_setting (key, value, use, module, inactive) VALUES ('engagement.batch_size','150','items in one batch','engagement',0)")
cn.commit()
cn.close()
cfg = Cfg(copy)
conn = cfg.conn
res = []


def case(cid, what, ok_, detail=""):
    res.append(bool(ok_))
    print(f"{cid} {'PASS' if ok_ else 'FAIL'} {what}" + ("" if ok_ else f"  -- {detail}"), flush=True)


def call(**params):
    return he.pull(SimpleNamespace(cfg=cfg, params=params, run_id="RUN-TEST-BATCH"))


# ---- batch_plan on made-up surfaces
mk = lambda *ns: [{"items": list(range(n))} for n in ns]  # noqa: E731
p = eg.batch_plan(mk(40, 50, 60, 10), 100)
case("B1", "whole surfaces fill a batch up to the size, the next starts a new one", [[(si, a, b) for si, a, b in x] for x in p] == [[(0, 0, 40), (1, 0, 50)], [(2, 0, 60), (3, 0, 10)]], p)
p = eg.batch_plan(mk(30, 250, 20), 100)
case("B2", "a surface over the size is split in verse order and the next surface joins its last part", p == [[(0, 0, 30)], [(1, 0, 100)], [(1, 100, 200)], [(1, 200, 250), (2, 0, 20)]], p)
every = sorted((si, i) for x in p for si, a, b in x for i in range(a, b))
case("B3", "every item is in exactly one batch", every == sorted((si, i) for si, s in enumerate(mk(30, 250, 20)) for i in range(len(s["items"]))), "")
case("B4", "a surface of exactly the size is one batch", eg.batch_plan(mk(100), 100) == [[(0, 0, 100)]])
try:
    eg.batch_plan(mk(1), 0)
    case("B5", "a size below 1 is refused", False)
except eg.EngagementError:
    case("B5", "a size below 1 is refused", True)

# ---- the real collection (on the copy)
full = eg.pull(conn, cfg, "uncovered-words")
total = sum(len(s["items"]) for s in full["surfaces"])
case("B6", "the whole pull is unchanged (no batch key content)", full["batch"] is None and total == 2369 and len(full["existing_observations"]) == 2549, (total, len(full["existing_observations"])))
b1 = eg.pull(conn, cfg, "uncovered-words", batch=1)
n_b = b1["batch"]["of"]
case("B7", "batch 1 holds at most the batch size and says its place", b1["batch"]["n"] == 1 and 0 < b1["batch"]["items"] <= 150 and n_b >= 16, b1["batch"])
seen, items, ex = set(), 0, {}
okv = True
for k in range(1, n_b + 1):
    b = eg.pull(conn, cfg, "uncovered-words", batch=k)
    for s in b["surfaces"]:
        for it in s["items"]:
            key = (s["surface"], it["vl_id"])
            okv = okv and key not in seen
            seen.add(key)
            items += 1
    for a in b["existing_observations"]:
        ex[a] = ex.get(a, 0) + 1
case("B8", "the batches together hold every item exactly once", okv and items == total == len(seen), (items, total))
case("B9", "every existing observation is in exactly one batch", len(ex) == 2549 and set(ex.values()) == {1}, (len(ex), set(ex.values())))
put = [(k, s) for k in range(1, n_b + 1) for s in eg.pull(conn, cfg, "uncovered-words", batch=k)["surfaces"] if s["surface"] == "put"]
refs = [(it["osisId"], it["vl_id"]) for _, s in put for it in s["items"]]
case("B10", "put (491 items) is split over 4 or more batches, in verse order", len(put) >= 4 and refs == sorted(refs, key=lambda r: r[0] or ""), len(put))
for bad in ("0", "x", "9999"):
    r = call(Collection="uncovered-words", Batch=bad)
    case(f"B11-{bad}", f"-Batch {bad} is refused and no file is written", r.condition == "refused" and not list((scratch / "work").glob("*")) if (scratch / "work").exists() else r.condition == "refused", r.message)
r = call(Collection="uncovered-words", Batch="2")
f = next((scratch / "work").glob("engagement-uncovered-words-pull-batch2-*.json"), None)
case("B12", "the handler writes the batch file named for it and reports the batch", r.condition == "ok" and f is not None and "batch 2 of" in r.message, r.message)
r = call(Collection="uncovered-words")
case("B13", "without -Batch the whole pull is written as before", r.condition == "ok" and " of " not in r.message.split(": ")[1].split(",")[0] and "batch " not in r.message.split(": ",1)[1][:12], r.message[:160])
print(f"\n{sum(res)} of {len(res)} pass")
cfg.conn.close()
