"""temp_2637_check_answer_test_run.py -- #2637 plan v3 X3: CheckAnswer lists every problem of an answer at once, each with its rule, and writes
nothing (handlers/collectionbuild.py check_answer; the collect mode of lib/readcommands.py, lib/layerreading.py, lib/layerinner.py,
lib/collectionvalidate.py; migration encode_2637_check_answer_v1_20261126).

Runs on a COPY of iba.db, never the live database. Applies the migration to the copy (and again), opens S1 of boast / boastful (unread on live,
2026-11-26) with ReadWords, builds answers from the package it writes, and compares RecordWords -Check (which stops at the first stage that
fails) with CheckAnswer. The packages and answers it writes are deleted at the end.

Usage: python iba/app/tools/temp_2637_check_answer_test_run.py <db copy> <scratch dir>
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
from iba.app.lib import refusalrules  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
MIG = next(p for p in [ROOT / "iba" / "app" / "migration" / "encode_2637_check_answer_v1_20261126.py",
                       ROOT / "iba" / "app" / "migration" / "archive" / "encode_2637_check_answer_v1_20261126.py"] if p.exists())
READS = ["words", "senses", "enrichment", "structure", "sweep", "evidence", "elements", "behaviours"]
results = []
made = []


def case(cid, desc, passed, evidence=""):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:500]))
    print(f"[{results[-1][2]}] {cid}: {desc} -- {results[-1][3][:400]}", flush=True)


def ctx(cfg, step, **params):
    return Ctx(db=None, cfg=cfg, step=None, run_id=f"TEST-2637-X3-{step}", word="", word_id=None, params=params, step_id=step)


def counts(conn):
    return tuple(conn.execute(f"SELECT count(*) FROM {t}").fetchone()[0] for t in ("ib_observation", "ib_node", "ib_observation_change")) + \
        (conn.execute("SELECT group_concat(state || validated) FROM collection_layer_item WHERE collection_id=(SELECT id FROM collection WHERE lower(name)='boast' AND deleted=0)").fetchone()[0],)


def answer(pkg, scratch, name, edit):
    """An answer built from the package: one reading of each word holding all its occurrences, a text naming its verses, grounds copied from the
    first verse, each older observation kept as evidence; then `edit` changes it."""
    rows = []
    for w in pkg["words"]:
        refs = sorted({o["reference"] for o in w["occurrences"]})
        verse = w["occurrences"][0]["verse"].split()
        rows.append({"ledger_id": w["ledger_id"], "readings": [{
            "kind": "term", "basis": "read", "grounds": next(" ".join(verse[:k]) for k in range(3, 8) if len(" ".join(verse[:k])) >= 15 or k == 7),
            "obs_text": f"In {', '.join(refs)} the word {w['word'].split('|')[0]} ({w['strong']}) names a trait listed among others in a catalogue of conduct.",
            "occurrences": [o["occurrence"] for o in w["occurrences"]]}],
            "older": [{"observation": o["observation"], "action": "keep", "nature": "evidence",
                       "reason": "it states what the verse shows of the word, tied to its verse"} for o in w["older"]]})
    a = {"command": "ReadWords", "collection": pkg["collection"], "subgroup": pkg["subgroup"], "step": pkg["step"], "rows": rows}
    edit(a)
    f = scratch / f"temp-2637-x3-{name}.json"
    f.write_text(json.dumps(a, ensure_ascii=False), encoding="utf-8")
    made.append(f)
    return f


def keys(msg):
    return sorted(set(re.findall(r"\[([A-Z]{2}-\d{2}|B:\d+|RO\d+)\]", msg)))


def main(db, scratch):
    if pathlib.Path(db).resolve() == LIVE.resolve():
        sys.exit("refused: this test runs on a copy, never the live database")
    scratch = pathlib.Path(scratch)
    out = [subprocess.run([sys.executable, str(MIG), "--db", db], capture_output=True, text=True) for _ in range(2)]
    case("C1", "the migration applies on the copy, and a second apply writes nothing",
         ("applied" in out[0].stdout or "already applied" in out[0].stdout) and "already applied: 0" in out[1].stdout, " / ".join((o.stdout + o.stderr).strip()[:150] for o in out))
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    st = conn.execute("SELECT handler FROM cfg_step WHERE step='collection.check_answer' AND inactive=0").fetchone()
    route = conn.execute("SELECT path FROM cfg_on_fail WHERE step='collection.check_answer' AND condition='refused'").fetchone()
    grants = {r[0] for r in conn.execute("SELECT table_name FROM cfg_write_grant WHERE writer='collection.check_answer' AND inactive=0")}
    case("C2", "collection.check_answer is a step with its handler, refused routed to report-continue, and the grants of the Record steps",
         st and st[0].endswith("check_answer") and route and route[0] == "report-continue" and {"ib_observation", "ib_node", "read_failure"} <= grants, (st, route, sorted(grants)))
    reg = refusalrules.load(conn)
    rebuilt, unkeyed, dead, n = refusalrules.build(ROOT, reg)
    case("C3", "the refusal registry rebuilds from config: every site keyed, no unused entry, the stored reads as rebuilt",
         not unkeyed and not dead and rebuilt["entries"] == reg["entries"], f"{n} sites; unkeyed {[(s['site'], s['line']) for s in unkeyed][:5]}; dead {dead[:3]}")
    rt = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.read_types'").fetchone()[0])
    miss = [r for r in READS if not any("-Action CheckAnswer" in w for w in rt[r]["write"])]
    case("C4", "the write instruction of all 8 reads names CheckAnswer before the Record command", not miss, miss or "all 8")

    o = h.check_answer(ctx(cfg, "collection.check_answer"))
    o2 = h.check_answer(ctx(cfg, "collection.check_answer", File=str(scratch / "no-such-answer.json")))
    bad = scratch / "temp-2637-x3-no-command.json"
    bad.write_text(json.dumps({"command": "LayerRecord", "rows": []}), encoding="utf-8")
    made.append(bad)
    o3 = h.check_answer(ctx(cfg, "collection.check_answer", File=str(bad)))
    case("C5", "usage: no -File [PC-01], an unreadable file [PC-01], an answer of no read [PC-02], each refused",
         o.condition == o2.condition == o3.condition == "refused" and "[PC-01]" in o.message and "[PC-01]" in o2.message and "[PC-02]" in o3.message,
         (o.message[:80], o2.message[:80], o3.message[:120]))

    # the package of an unread subgroup on the copy
    r = h.read_words(ctx(cfg, "collection.read_words", Collection="boast", Subgroup="boastful"))
    m = re.search(r"(_analytics/\S+?\.json)", r.message)
    pkgf = ROOT / m.group(1) if m else None
    if pkgf:
        made.append(pkgf)
        made.extend(pkgf.parent.glob(pkgf.stem + "*.md"))      # its readable view (X1)
    pkg = json.loads(pkgf.read_text(encoding="utf-8")) if pkgf else None
    case("C6", "ReadWords writes the package of boast / boastful on the copy", r.condition == "ok" and pkg is not None, r.message[:200])
    if pkg is None:
        return report(scratch)
    other = conn.execute("SELECT id FROM ib_observation WHERE deleted=0 AND id NOT IN (%s) ORDER BY id LIMIT 1"
                         % ",".join(str(x["observation"]) for w in pkg["words"] for x in w["older"]) or "0").fetchone()[0]

    def two_stage(a):
        v = pkg["words"][1]["occurrences"][0]["verse"].split()
        a["rows"][1]["readings"][0]["obs_text"] = f"In {pkg['words'][1]['occurrences'][0]['reference']}: " + " ".join(v[:10])
        for row in a["rows"]:
            if row["older"]:
                row["older"][0] = {"observation": row["older"][0]["observation"], "action": "merge", "into": 999999999,
                                   "reason": "it says the same as the observation it is merged into"}
                break
    f2 = answer(pkg, scratch, "two-stages", two_stage)
    before = counts(conn)
    rec = h.record_words(ctx(cfg, "collection.record_words", File=str(f2), Check="1"))
    chk = h.check_answer(ctx(cfg, "collection.check_answer", File=str(f2)))
    after = counts(conn)
    case("C7", "RecordWords -Check on a two-stage answer stops at the first stage: it names the copied text [RW-04] and not the merge",
         rec.condition == "refused" and "RW-04" in keys(rec.message) and "different live observations" not in rec.message, rec.message[:400])
    case("C8", "CheckAnswer on the same answer lists both stages in one refusal: the copied text [RW-04] and the merge into no live observation",
         chk.condition == "refused" and "RW-04" in keys(chk.message) and any("merge" in ln and ln.strip().startswith("[") for ln in chk.message.split(chr(10))),
         chk.message.replace(chr(10), " / ")[:600])
    case("C9", "CheckAnswer writes nothing: observations, nodes, change log and ledger states as before", before == after, (before[:3], after[:3]))
    unkeyed_lines = [ln for ln in chk.message.split("\n")[1:] if ln.strip() and not ln.strip().startswith("[")]
    case("C10", "every problem line of the CheckAnswer refusal carries its rule key", not unkeyed_lines, unkeyed_lines[:4])

    f3 = answer(pkg, scratch, "clean", lambda a: None)
    chk3 = h.check_answer(ctx(cfg, "collection.check_answer", File=str(f3)))
    after3 = counts(conn)
    case("C11", "an answer with no problem: CheckAnswer says so, names the Record command, and writes nothing",
         chk3.condition == "ok" and "-Action RecordWords" in chk3.message and after3 == before, chk3.message[:600])
    rec3 = h.record_words(ctx(cfg, "collection.record_words", File=str(f3), Check="1"))
    case("C12", "the answer CheckAnswer passes also passes RecordWords -Check (the two agree)", rec3.condition == "ok", rec3.message[:300])

    # the validation sheet: collect lists every action's problem, one to a line; without collect the first form problems still refuse whole
    sheet = {"collection": "boast", "actions": [{"action": "no_such_action"}, {"action": "restate", "oid": 999999999, "new_text": "x" * 30, "checked": "y" * 30, "reason": "z" * 30},
                                                 {"action": "restate", "oid": 999999998, "new_text": "x" * 30, "checked": "y" * 30, "reason": "z" * 30, "nature": "evidence"}]}
    try:
        cv.record(conn, cfg, "TEST-2637-X3-CV", sheet, keep=False, collect=True)
        msg = ""
    except cv.ValidateError as exc:
        msg = str(exc)
    conn.rollback()
    lines = [x.strip() for x in msg.split("\n") if x.strip()]
    case("C13", "a validation sheet under collect: the unknown action, the unknown parameter and the restate of an observation that does not exist, one to a line",
         len(lines) == 3 and "is not an action of the validation" in lines[0] and "unknown parameter(s)" in msg and "action 2 (restate)" in msg, lines)
    return report(scratch)


def report(scratch):
    for f in made:
        try:
            f.unlink()
        except OSError:
            pass
    rep = scratch / "temp-2637-x3-results.md"
    rep.write_text("| case | what | result | evidence |\n|---|---|---|---|\n" + "\n".join(f"| {c} | {d} | {r} | {e} |" for c, d, r, e in results) + "\n", encoding="utf-8")
    n = sum(1 for r in results if r[2] == "PASS")
    print(f"{n} of {len(results)} passed; results: {rep}")
    return 0 if n == len(results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
