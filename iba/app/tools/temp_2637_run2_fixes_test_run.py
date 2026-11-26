"""temp_2637_run2_fixes_test_run.py -- #2637 v20, the findings of the strive run: K1 (the subgroup evidence gate agrees with the 3.1 open gate;
a repairs-only package; repairs in the answer), K2 (Cycle patterns), K3 (grouping under the read contract), K4 (reports registered), K5
(grounds in several runs), K6 (limits in the packet), K7 (validation actions with parameters). Runs on a COPY of iba.db; prints only failures and
the count (B:20); deletes the files it causes.
Usage: python iba/app/tools/temp_2637_run2_fixes_test_run.py <db copy> <scratch dir>
"""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers import collectionbuild as h  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402
from iba.app.lib import collectionvalidate as cv  # noqa: E402
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib import manifest  # noqa: E402
from iba.app.lib import readcommands as rc  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
MIG = next(p for p in [ROOT / "iba" / "app" / "migration" / n / "encode_2637_run2_fixes_v1_20261126.py" for n in ("", "archive")] if p.exists())
res, made = [], []


def case(cid, ok, ev=""):
    res.append(bool(ok))
    if not ok:
        print(f"[FAIL] {cid}: {str(ev)[:500]}")


def ctx(cfg, step, **p):
    return Ctx(db=None, cfg=cfg, step=None, run_id=f"TEST-2637-R2-{step}", word="", word_id=None, params=p, step_id=step)


def pkg_of(o):
    m = re.search(r"(_analytics/\S+?\.json)", o.message)
    if not m:
        return None
    p = ROOT / m.group(1)
    made.extend([p] + list(p.parent.glob(p.stem + "*.md")))
    return json.loads(p.read_text(encoding="utf-8"))


def main(db, scratch):
    if pathlib.Path(db).resolve() == LIVE.resolve():
        sys.exit("refused: runs on a copy only")
    scratch = pathlib.Path(scratch)
    out = [subprocess.run([sys.executable, str(MIG), "--db", db], capture_output=True, text=True).stdout for _ in range(2)]
    case("R1 migration and re-run", "write(s)" in out[0] and "already applied: 0" in out[1], out)
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn

    # K1: on strive / exertion toward an end, the subgroup gate names what the 3.1 open gate names
    cid, gid, g = rc._subgroup(conn, "strive", "exertion toward an end")
    L = lr.load(conn, cfg, "strive", pairs=False, subgroup=g)
    sub = rc.evidence_check(conn, cfg, L, cid, gid)["findings"]["word_missing"]
    col = sorted(set(cv.check(conn, cfg, cid)["open_evidence"].get("word_missing", [])))
    case("R2 K1 the subgroup gate names 6310 and 6311, as the collection gate does", {6310, 6311} <= set(sub) and {6310, 6311} <= set(col), (sub, col))
    o = h.read_evidence(ctx(cfg, "collection.read_evidence", Collection="strive", Subgroup="exertion toward an end"))
    pk = pkg_of(o)
    case("R3 K1 K7 ReadEvidence writes a package with the repairs slot and every validation action with its parameters",
         pk is not None and "repairs" in pk["answer"] and "node_id" in pk["validation_actions"].get("complete_node", []), o.message[:300])
    if pk:
        role = "characteristic"
        fix = lambda nid: {"action": "complete_node", "node_id": nid, "role": role, "collection_id": 26, "reason": "the word is the characteristic of the verse"}
        ans = {**pk["answer"], "repairs": []}
        ans["observations"] = [{"observation": x["observation"], "verdict": "true", "why": "it states what its verse shows, tied to the verse", "actions": []} for x in pk["observations"]]
        for x in ans["observations"]:
            if x["observation"] == 6310:
                x.update(verdict="repair", why="its word node on 1Cor 14:12 has no role", actions=[fix(7438)])
        if not any(x["observation"] == 6310 for x in ans["observations"]):
            ans["repairs"].append(fix(7438))
        ans["repairs"].append(fix(7439))
        f = scratch / "temp-2637-r2-evidence.json"
        f.write_text(json.dumps(ans), encoding="utf-8")
        made.append(f)
        c = h.check_answer(ctx(cfg, "collection.check_answer", File=str(f)))
        case("R4 K1 the repairs of both nodes pass CheckAnswer", c.condition == "ok" or ("7438" not in c.message and "7439" not in c.message), c.message[:600])

    # K5: grounds in two runs of Heb 12:14 (the refused grounds of the run) are words of the verse; a run not in the verse is not
    vt = "Strive for peace with everyone, and for the holiness without which no one will see the Lord."
    runs = [lr._words(x) for x in re.split(r";|\.\.\.|…", "Strive for peace with everyone; the holiness without which no one will see the Lord")]
    bad = [lr._words(x) for x in re.split(r";", "Strive for peace with everyone; the holiness of the Lord")]
    case("R5 K5 two runs of the verse are its words; a run not in it is not", all(r in lr._words(vt) for r in runs) and not all(r in lr._words(vt) for r in bad), runs)

    # K6: the limits the recorder applies are in the instruction
    ins = rc.instruction(conn, rc.settings(cfg)["structure"])
    case("R6 K6 the instruction states the limits (grounds 10, text 40, verse words 7)", list(ins["limits"].values()) == [10, 40, 7], ins.get("limits"))

    # K3: GroupPull of an ungrouped collection writes the grouping under the contract; CheckAnswer checks it, every line keyed
    c0 = conn.execute("SELECT c.name FROM collection c WHERE c.deleted=0 AND NOT EXISTS (SELECT 1 FROM collection_subgroup s WHERE s.collection_id=c.id AND s.deleted=0) "
                      "ORDER BY c.id LIMIT 1").fetchone()
    o = h.group_pull(ctx(cfg, "collection.group_pull", Collection=c0[0])) if c0 else None
    gp = pkg_of(o) if o and o.condition == "ok" else None
    if gp is None:
        print(f"note: GroupPull not run to a file ({o.message[:200] if o else 'no ungrouped collection'}); R7, R8 not run")
    else:
        keep = [k["rule"].split(" ")[0] for k in gp.get("instruction", {}).get("keep", [])]
        case("R7 K3 the grouping file has its command, the GP rules, its refusals and a view", gp.get("command") == "GroupPull" and {"GP-01", "GP-04"} <= set(keep)
             and gp["instruction"].get("refused_when") and any(p.suffix == ".md" and p.name.startswith("group-") for p in made), keep)
        gf = next(p for p in made if p.name.startswith("group-") and p.suffix == ".json")
        c = h.check_answer(ctx(cfg, "collection.check_answer", File=str(gf)))
        lines = [x for x in c.message.split("\n")[1:] if x.strip()]
        case("R8 K3 CheckAnswer checks a grouping file and keys every problem line", c.condition in ("ok", "refused") and "this is not the answer of a read" not in c.message
             and all(x.strip().startswith("[") for x in lines), c.message[:500])

    # K2: ValidatePull's working file and a grouping view are package files for the Cycle audit
    pats = [re.compile(p.replace("{c}", "strive")) for p in json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.cycle'").fetchone()[0])["package_patterns"]]
    case("R9 K2 validate-strive.json and a grouping view are package files", any(p.match("validate-strive.json") for p in pats) and any(p.match("group-strive-20261126.md") for p in pats))

    # K4: a report is registered in file_manifest, and removed when it is gone
    t = ROOT / "_analytics" / "surfaces" / "exports" / "temp-2637-r2-register-v1-20261126.md"
    t.write_text("x", encoding="utf-8")
    manifest.register_files(cfg, [t])
    have = conn.execute("SELECT 1 FROM file_manifest WHERE path=?", (t.relative_to(ROOT).as_posix(),)).fetchone()
    t.unlink()
    manifest.register_files(cfg, [t])
    gone = conn.execute("SELECT 1 FROM file_manifest WHERE path=?", (t.relative_to(ROOT).as_posix(),)).fetchone()
    conn.rollback()
    case("R10 K4 a report is registered, and removed once gone", have and not gone, (have, gone))

    for p in made:
        try:
            p.unlink()
        except OSError:
            pass
    print(f"{sum(res)} of {len(res)} passed")
    return 0 if all(res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
