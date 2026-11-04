"""temp_2359_surface_base_test_run.py -- the test plan of the base-form tool (escalation #2359), run on a COPY of
iba.db (never the live database). Cases:
 M1 migration dry run, apply, second apply (idempotent)      S1 settings load; each missing setting refused
 S2 a bad prompt, relations or pattern refused               I1 input list: missing, bad JSON, not a list, duplicates
 A1-A9 check_answer: every usable and unusable shape         R1-R5 run_words with a stub server: all answered, resume,
 retry of a failed word, halt after N in a row, -Limit       T1 status counts
 L1 two real calls to the Ollama server (sought, lying)
Usage: python iba/app/tools/temp_2359_surface_base_test_run.py [--no-server]
"""
import contextlib
import json
import pathlib
import shutil
import sqlite3
import subprocess
import sys
import tempfile

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.lib import surfacebase as sb  # noqa: E402
from iba.app.lib import surfacejudge as sj  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
MIG = ROOT / "iba" / "app" / "migration" / "archive" / "surface_base_2359_v1_20261104.py"
results = []


def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
    print(("PASS " if cond else "FAIL ") + name + (f"  [{detail}]" if detail else ""))


def mig(db, *flags):
    p = subprocess.run([sys.executable, str(MIG), "--db", str(db), *flags], capture_output=True, text=True, cwd=ROOT)
    return p.returncode, (p.stdout + p.stderr).strip()


def raises(fn, *a):
    try:
        fn(*a)
    except sb.BaseError as exc:
        return str(exc)
    return None


def main():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="t2359_"))
    db = tmp / "iba_copy.db"
    src = sqlite3.connect(f"file:{LIVE.as_posix()}?mode=ro", uri=True)   # backup API: a plain file copy misses the WAL
    dst = sqlite3.connect(db)
    src.backup(dst)
    dst.close()
    src.close()
    print("copy:", db)
    # M1
    rc, out = mig(db, "--dry-run")
    check("M1a dry run writes nothing and lists the cfg writes", rc == 0 and "DRY RUN:" in out, out.splitlines()[0])
    cfg = Cfg(db)
    check("M1a no setting written by the dry run", cfg.setting("surface_judge.base_prompt") is None)
    rc, out = mig(db)
    check("M1b apply", rc == 0 and "applied" in out, out)
    rc, out = mig(db)
    check("M1c second apply changes nothing", rc == 0 and "already applied" in out, out)
    cfg = Cfg(db)
    check("M1d work package and both steps registered",
          cfg.conn.execute("select count(*) from cfg_step where work_package='surface-base' and inactive=0").fetchone()[0] == 2)
    check("M1e on_fail rows (refused x2, halted x1)",
          cfg.conn.execute("select count(*) from cfg_on_fail where step like 'surface_base.%'").fetchone()[0] == 3)
    # S1/S2
    vals = sb.settings(cfg)
    check("S1a settings load with the server keys and the base keys",
          vals["base_relations"] == ["inflection", "derivation", "none"] and "model" in vals)
    for key in ("base_prompt", "base_relations", "base_form_pattern", "base_input_suffix"):
        c2 = Cfg(db)
        c2.conn.execute("update cfg_setting set inactive=1 where key=?", ("surface_judge." + key,))
        c2.conn.commit()
        msg = raises(sb.settings, Cfg(db))
        check(f"S1b missing {key} refused", msg is not None and key in msg, (msg or "")[:80])
        c3 = Cfg(db)
        c3.conn.execute("update cfg_setting set inactive=0 where key=?", ("surface_judge." + key,))
        c3.conn.commit()
    orig = {k: Cfg(db).setting("surface_judge." + k) for k in ("base_prompt", "base_relations", "base_form_pattern")}
    for key, bad in (("base_prompt", json.dumps("no place")), ("base_relations", json.dumps(["inflection"])),
                     ("base_form_pattern", json.dumps("[a-z"))):
        c2 = Cfg(db)
        c2.conn.execute("update cfg_setting set value=? where key=?", (bad, "surface_judge." + key))
        c2.conn.commit()
        msg = raises(sb.settings, Cfg(db))
        check(f"S2 bad {key} refused", msg is not None, (msg or "")[:80])
        c2 = Cfg(db)
        c2.conn.execute("update cfg_setting set value=? where key=?", (json.dumps(orig[key]), "surface_judge." + key))
        c2.conn.commit()
    vals = sb.settings(Cfg(db))
    # I1
    out = tmp / "t-v1-20261104.jsonl"
    inp = tmp / ("t-v1-20261104" + vals["base_input_suffix"])
    check("I1a missing input list refused", raises(sb.input_words, vals, out) is not None)
    inp.write_text("{not json", encoding="utf-8")
    check("I1b bad JSON refused", raises(sb.input_words, vals, out) is not None)
    inp.write_text(json.dumps({"words": "sought"}), encoding="utf-8")
    check("I1c words not a list refused", raises(sb.input_words, vals, out) is not None)
    inp.write_text(json.dumps({"words": ["sought", "", "wept"]}), encoding="utf-8")
    check("I1d an empty string refused", raises(sb.input_words, vals, out) is not None)
    inp.write_text(json.dumps({"words": ["sought", "wept", "sought", "lying"]}), encoding="utf-8")
    check("I1e duplicates removed, order kept", sb.input_words(vals, out) == ["sought", "wept", "lying"])
    # A: check_answer
    ca = lambda a, w="sought": sb.check_answer(a, w, vals)  # noqa: E731
    check("A1 inflection accepted", ca({"base": "seek", "relation": "inflection", "reason": None}) == [])
    check("A2 derivation accepted", ca({"base": "wonder", "relation": "derivation"}, "wonderful") == [])
    check("A3 none with base = the word accepted", ca({"base": "sought", "relation": "none", "reason": None}) == [])
    check("A4 none with no base accepted", ca({"base": None, "relation": "none"}) == [])
    check("A5 none with another base refused", ca({"base": "seek", "relation": "none"}) != [])
    check("A6 unknown relation refused", ca({"base": "seek", "relation": "synonym"}) != [])
    check("A7 base with capital or space refused",
          ca({"base": "Seek", "relation": "inflection"}) != [] and ca({"base": "to seek", "relation": "inflection"}) != [])
    check("A8 inflection whose base is the word refused", ca({"base": "sought", "relation": "inflection"}) != [])
    check("A9 not an object refused", ca(["seek"]) != [] and ca({"base": "seek"}) != [])
    # R: run_words with a stub server
    saved = (sj.ask, sj.server_route, sj.preflight)
    calls = []
    script = {"sought": {"base": "seek", "relation": "inflection"}, "wept": {"base": "weep", "relation": "inflection"},
              "lying": {"base": "lying", "relation": "none", "reason": "not from lye"}}

    def stub_ask(v, prompt):
        word = prompt.split('English: "')[1].split('"')[0]
        calls.append(word)
        if word in script:
            return script[word], {"out_tokens": 5}
        raise RuntimeError("stub: no answer")

    @contextlib.contextmanager
    def stub_route(v):
        yield v
    sj.ask, sj.server_route, sj.preflight = stub_ask, stub_route, lambda v: ["m"]
    try:
        words = ["sought", "wept", "lying"]
        res = sb.run_words(vals, words, out)
        recs = sj.read_batch(out)
        check("R1 all answered, one line each",
              res == {"asked": 3, "failed": 0, "stopped": False, "halted": False} and len(out.read_text().splitlines()) == 3, str(res))
        check("R1b none keeps the word as base; relation stored",
              recs["lying"]["relation"] == "none" and recs["lying"]["base"] == "lying" and recs["sought"]["base"] == "seek")
        calls.clear()
        res = sb.run_words(vals, words, out)
        check("R2 resume: nothing asked again", calls == [] and res["asked"] == 0 and len(out.read_text().splitlines()) == 3)
        out2 = tmp / "t2-v1-20261104.jsonl"
        calls.clear()
        res = sb.run_words(vals, ["sought", "zzz", "wept"], out2)
        check("R3 a failed word is recorded with relation null; the run goes on",
              res["asked"] == 2 and res["failed"] == 1 and sj.read_batch(out2)["zzz"]["relation"] is None, str(res))
        script["zzz"] = {"base": "zz", "relation": "derivation"}
        calls.clear()
        res = sb.run_words(vals, ["sought", "zzz", "wept"], out2)
        check("R3b the failed word is tried again, the answered are not", calls == ["zzz"] and res["asked"] == 1, str(calls))
        del script["zzz"]
        out3 = tmp / "t3-v1-20261104.jsonl"
        n = int(vals["max_consecutive_failures"])
        res = sb.run_words(vals, [f"q{i}" for i in range(n + 3)], out3)
        check("R4 halts after max_consecutive_failures in a row",
              res["halted"] and res["failed"] == n and len(out3.read_text().splitlines()) == n, str(res))
        out4 = tmp / "t4-v1-20261104.jsonl"
        res = sb.run_words(vals, ["sought", "wept", "lying"], out4, limit=2)
        check("R5 -Limit stops after n", res["asked"] == 2 and len(out4.read_text().splitlines()) == 2, str(res))
        st = sb.status(vals, ["sought", "wept", "lying", "extra"], out4)
        check("T1 status: counts per relation, failed, left",
              st["answered"] == 2 and st["left"] == 2 and st["failed"] == 0 and st["per_relation"]["inflection"] == 2, str(st))
        st = sb.status(vals, ["q0", "q1", "q2", "q3"], out3)
        check("T1b status counts a failed word as failed, an untried word as left",
              st["failed"] == 3 and st["answered"] == 0 and st["left"] == 1, str(st))
    finally:
        sj.ask, sj.server_route, sj.preflight = saved
    # L1: the real server
    if "--no-server" not in sys.argv:
        out5 = tmp / "t5-v1-20261104.jsonl"
        try:
            res = sb.run_words(vals, ["sought", "lying"], out5, emit=print)
            recs = sj.read_batch(out5)
            check("L1 two real calls answered with a usable shape", res["asked"] == 2,
                  json.dumps({w: (r["relation"], r["base"]) for w, r in recs.items()}))
        except sb.BaseError as exc:
            check("L1 real server", False, str(exc)[:200])
    bad = [r for r in results if not r[1]]
    print(f"\n{len(results) - len(bad)} of {len(results)} cases pass")
    shutil.rmtree(tmp, ignore_errors=True)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
