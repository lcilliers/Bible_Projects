"""temp_2637_view_form_test_run.py -- #2637 X1 (readable view), X2 (judgement-only form: "all", rests_on with role), #2628 (uncarried keys on
every path) and #2621 (LayerNext on a collection not grouped). Runs on a COPY of iba.db; prints only failures and the count (B:20).
Usage: python iba/app/tools/temp_2637_view_form_test_run.py <db copy> <scratch dir>
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
from iba.app.lib import layerinner as li  # noqa: E402
from iba.app.lib import layerloop  # noqa: E402
from iba.app.lib import readcommands as rc  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
MIG = next(p for p in [ROOT / "iba" / "app" / "migration" / n / "encode_2637_view_and_form_v1_20261126.py" for n in ("", "archive")] if p.exists())
res, made = [], []


def case(cid, ok, ev=""):
    res.append(ok)
    if not ok:
        print(f"[FAIL] {cid}: {str(ev)[:400]}")


def ctx(cfg, step, **p):
    return Ctx(db=None, cfg=cfg, step=None, run_id=f"TEST-2637-VF-{step}", word="", word_id=None, params=p, step_id=step)


def main(db, scratch):
    if pathlib.Path(db).resolve() == LIVE.resolve():
        sys.exit("refused: runs on a copy only")
    scratch = pathlib.Path(scratch)
    out = [subprocess.run([sys.executable, str(MIG), "--db", db], capture_output=True, text=True).stdout for _ in range(2)]
    case("V1 migration and re-run", "write(s)" in out[0] and "already applied: 0" in out[1], out)
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    r = h.read_words(ctx(cfg, "collection.read_words", Collection="boast", Subgroup="boastful"))
    m = re.search(r"(_analytics/\S+?\.json)", r.message)
    pkgf = ROOT / m.group(1) if m else None
    views = sorted(pkgf.parent.glob(pkgf.stem + "*.md")) if pkgf else []
    made.extend([pkgf] + views if pkgf else [])
    case("V2 package and its view", pkgf and views and "## Refused when (by rule)" in views[0].read_text(encoding="utf-8")
         and "## The answer form" in views[-1].read_text(encoding="utf-8"), r.message[:300])
    if not pkgf:
        return done()
    pkg = json.loads(pkgf.read_text(encoding="utf-8"))
    real = rc.settings_of
    rc.settings_of = lambda c: {"limits": {"view_max_chars": 3000}}
    parts = rc.view(conn, pkg)
    rc.settings_of = real
    case("V3 a view over its limit is split, each part within it but one line", len(parts) > 1 and all(len(p) < 3000 + 2500 for p in parts), [len(p) for p in parts])

    rows = []
    for w in pkg["words"]:
        refs = sorted({o["reference"] for o in w["occurrences"]})
        v = w["occurrences"][0]["verse"].split()
        rows.append({"ledger_id": w["ledger_id"], "readings": [{"kind": "term", "basis": "read",
                     "grounds": next(" ".join(v[:k]) for k in range(3, 8) if len(" ".join(v[:k])) >= 15 or k == 7),
                     "obs_text": f"In {', '.join(refs)} the word {w['word'].split('|')[0]} ({w['strong']}) names a trait listed among others in a catalogue of conduct.",
                     "occurrences": "all"}],
                     "older": [{"observation": o["observation"], "action": "keep", "nature": "evidence", "reason": "it states what the verse shows of the word, tied to its verse"} for o in w["older"]]})
    ans = {"command": "ReadWords", "collection": "boast", "subgroup": "boastful", "step": "S1", "rows": rows}
    f = scratch / "temp-2637-vf-all.json"
    f.write_text(json.dumps(ans), encoding="utf-8")
    made.append(f)
    o = h.check_answer(ctx(cfg, "collection.check_answer", File=str(f)))
    case("V4 readings with occurrences \"all\" pass CheckAnswer", o.condition == "ok", o.message[:500])

    # #2628: a consume whose uncarried occurrences are JSON string keys is matched (the words path)
    w0 = next(w for w in pkg["words"] if any(x["observation"] == 15159 for x in w["older"]))
    mine = {x["occurrence"] for x in w0["occurrences"]}
    occ15159 = [r_[0] for r_ in conn.execute("SELECT verse_lexical_id FROM ib_node WHERE observation_id=15159 AND deleted=0 AND verse_lexical_id IS NOT NULL")]
    row = next(r_ for r_ in rows if r_["ledger_id"] == w0["ledger_id"])
    row["older"] = [{"observation": 15159, "action": "consume", "carriers": ["this"], "mapping": "the reading states the word in its catalogue; the rest of the old text is the setting",
                     "uncarried": {str(x): "a word of the setting the reading of this word does not state" for x in occ15159 if x not in mine},
                     "reason": "the reading of the word carries what the old observation says of it"}]
    f.write_text(json.dumps(ans), encoding="utf-8")
    o = h.check_answer(ctx(cfg, "collection.check_answer", File=str(f)))
    case("V5 #2628 uncarried named with string keys is matched", "not named as uncarried" not in o.message, o.message[:500])

    # #2621: a collection with no subgroup is sent to the grouping
    c = conn.execute("SELECT name FROM collection c WHERE deleted=0 AND NOT EXISTS (SELECT 1 FROM collection_subgroup s WHERE s.collection_id=c.id AND s.deleted=0) LIMIT 1").fetchone()
    na = layerloop.next_action(conn, cfg, c[0]) if c else {}
    case("V6 #2621 an ungrouped collection is sent to GroupPull", c is None or (na.get("step") == "grouping" and "GroupPull" in na["commands"][0]), na)

    # X2: rests_on and role expand to a traced node on each and an occurrence node on each covered occurrence the row may name
    cov = li._covered(conn, [15159])
    fx = li._expand_nodes(conn, {"key": "f1", "rests_on": [15159], "role": "characteristic", "roles": {str(min(cov)): ""}}, {15159}, cov)
    occ_nodes = [n["occurrence"] for n in fx["nodes"] if "occurrence" in n]
    case("V7 rests_on with role expands, an exception left out", {"traced": 15159} in fx["nodes"] and set(occ_nodes) == cov - {min(cov)}
         and all(n.get("role") == "characteristic" for n in fx["nodes"] if "occurrence" in n) and "rests_on" not in fx, fx)
    return done()


def done():
    for p in made:
        try:
            p.unlink()
        except OSError:
            pass
    print(f"{sum(res)} of {len(res)} passed")
    return 0 if all(res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
