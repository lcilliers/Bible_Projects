"""temp_2637_cycle_test_run.py -- #2637 X6, X7: Collection-Build.ps1 -Action Cycle (lib/cycleview.py) and the B:138 amendment. Runs on a COPY of
iba.db; prints only failures and the count (B:20). The reports and the stray file it causes are deleted at the end.
Usage: python iba/app/tools/temp_2637_cycle_test_run.py <db copy>
"""
import datetime
import json
import pathlib
import re
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers import collectionbuild as h  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
MIG = next(p for p in [ROOT / "iba" / "app" / "migration" / n / "encode_2637_cycle_v1_20261126.py" for n in ("", "archive")] if p.exists())
res, made = [], []


def case(cid, ok, ev=""):
    res.append(ok)
    if not ok:
        print(f"[FAIL] {cid}: {str(ev)[:400]}")


def ctx(cfg, **p):
    return Ctx(db=None, cfg=cfg, step=None, run_id="TEST-2637-CYCLE", word="", word_id=None, params=p, step_id="collection.cycle")


def report_of(o):
    m = re.search(r"report (\S+\.md)", o.message)
    p = ROOT / m.group(1) if m and not pathlib.Path(m.group(1)).is_absolute() else (pathlib.Path(m.group(1)) if m else None)
    if p:
        made.append(p)
    return p.read_text(encoding="utf-8") if p and p.exists() else ""


def main(db):
    if pathlib.Path(db).resolve() == LIVE.resolve():
        sys.exit("refused: runs on a copy only")
    out = [subprocess.run([sys.executable, str(MIG), "--db", db], capture_output=True, text=True).stdout for _ in range(2)]
    case("Y1 migration and re-run", "write(s)" in out[0] and "already applied: 0" in out[1], out)
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    case("Y2 B:138 allows the live reading audited by Cycle", "the live reading of that unit" in conn.execute("SELECT rule_text FROM cfg_behaviour_rule WHERE id=138").fetchone()[0])
    o = h.cycle(ctx(cfg))
    case("Y3 no -Collection is refused [PC-01]", o.condition == "refused" and "[PC-01]" in o.message, o.message)

    since = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    time.sleep(1.1)
    conn.execute("INSERT INTO read_failure (run_id, step, collection, subgroup, kind, file, problems, rule_keys) VALUES "
                 "('T','collection.record_words','boast','boastful','refused',NULL,?, 'RW-03')",
                 ("the answer is refused whole, nothing written:\n  [RW-03] row 1: the same text as row 2\n  row 3: a problem no rule names",))
    conn.execute("INSERT INTO read_failure (run_id, step, collection, subgroup, kind, file, problems, rule_keys) VALUES "
                 "('T','collection.read_senses','boast','boastful','crash',NULL,'RuntimeError(synthetic)', NULL)")
    conn.commit()
    wd = pathlib.Path(json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.working_dir'").fetchone()[0]))
    stray = wd / "temp-boast-boastful-scratch.json"
    stray.write_text("{}", encoding="utf-8")
    made.append(stray)
    o = h.cycle(ctx(cfg, Collection="boast", Subgroup="boastful", Since=since))
    rep = report_of(o)
    case("Y4 a run with an unkeyed line, a crash and a stray file FAILS, naming all three",
         "audit FAIL" in o.message and "a problem no rule names" in rep and "synthetic" in rep and stray.name in rep and "## Steps" in rep and "## Ledger" in rep, o.message + rep[-600:])
    case("Y5 a keyed line is not counted as unstated", "the same text as row 2" not in rep.split("## Audit")[-1], rep[-400:])
    stray.unlink()
    time.sleep(1.1)
    later = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    o = h.cycle(ctx(cfg, Collection="boast", Subgroup="boastful", Since=later))
    report_of(o)
    case("Y6 a clean window PASSES", "audit PASS" in o.message, o.message)
    arch = pathlib.Path(json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='governance.oneoff_report_archive_dir'").fetchone()[0]))
    made.extend(p_ for p_ in (ROOT / arch).rglob("collection-cycle-boast-boastful-*.md") if p_.stat().st_mtime > time.time() - 600)
    made.extend((ROOT / "_analytics" / "surfaces" / "exports" / "archive").glob("collection-cycle-boast-boastful-*.md"))
    for p in made:
        try:
            p.unlink()
        except OSError:
            pass
    print(f"{sum(res)} of {len(res)} passed")
    return 0 if all(res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
