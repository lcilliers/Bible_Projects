"""temp_2637_failure_log_test_run.py -- #2637 plan v3 X5 and X8: the read and record commands keep every refusal and crash in read_failure, and a message that
only names the next command is an ok outcome, not a refusal (catalogue K7, K10: outputs/escalation/2637-known-failures-catalogue-v1-20261126.md).

Runs on a COPY of iba.db, never the live database: applies the migration encode_2637_failure_log_v1_20261126 to the copy, then calls the handlers of
iba/app/handlers/collectionbuild.py with a context on the copy, and reads the routing from the copy's cfg_on_fail.

Usage: python iba/app/tools/temp_2637_failure_log_test_run.py <db copy> <scratch dir>
"""
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers import collectionbuild as h  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402
from iba.app.lib import readcommands as rc  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
MIG = ROOT / "iba" / "app" / "migration" / "archive" / "encode_2637_failure_log_v1_20261126.py"
results = []


def case(cid, desc, passed, evidence=""):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:300]))
    print(f"[{results[-1][2]}] {cid}: {desc} -- {results[-1][3][:200]}", flush=True)


def ctx(cfg, step, **params):
    return Ctx(db=None, cfg=cfg, step=None, run_id=f"TEST-2637-X8-{step}", word="", word_id=None, params=params, step_id=step)


def failures(conn, step):
    return conn.execute("SELECT kind, collection, subgroup, file, problems, rule_keys FROM read_failure WHERE step=? ORDER BY id", (step,)).fetchall()


def main(db, scratch):
    if pathlib.Path(db).resolve() == LIVE.resolve():
        sys.exit("refused: this test runs on a copy, never the live database")
    scratch = pathlib.Path(scratch)
    out = [subprocess.run([sys.executable, str(MIG), "--db", db], capture_output=True, text=True).stdout.strip() for _ in range(2)]
    case("F1", "the migration applies on the copy, and a second apply writes nothing", "applied" in out[0] and "already applied: 0" in out[1], " / ".join(out))
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    cols = [r[1] for r in conn.execute("PRAGMA table_info(read_failure)")]
    case("F2", "read_failure exists with the columns of its cfg_column rows", cols == [r[0] for r in conn.execute("SELECT name FROM cfg_column WHERE table_name='read_failure' ORDER BY ordinal")], cols)
    routed = conn.execute("SELECT step, path FROM cfg_on_fail WHERE condition='refused' AND step IN (SELECT writer FROM cfg_write_grant WHERE table_name='read_failure')").fetchall()
    case("F3", "every step that may write read_failure routes refused to report-continue (no escalation)", len(routed) == 19 and all(p == "report-continue" for _, p in routed), f"{len(routed)} steps")

    # F4: a unit already read: ReadNext is an ok outcome and nothing is logged (boast / boasting is through S1 on live, 2026-11-26)
    o = h.read_words(ctx(cfg, "collection.read_words", Collection="boast", Subgroup="boasting"))
    case("F4", "ReadWords on a subgroup whose words are all read returns ok naming the next command, and logs nothing", o.condition == "ok" and "next" in o.message.lower()
         and not failures(conn, "collection.read_words"), f"{o.condition}: {o.message[:160]}")

    # F5: a usage refusal (no subgroup) is refused and logged with the collection
    o = h.read_words(ctx(cfg, "collection.read_words", Collection="boast"))
    f = failures(conn, "collection.read_words")
    case("F5", "a read with a missing parameter is refused and kept in read_failure with its collection", o.condition == "refused" and len(f) == 1 and f[0][0] == "refused" and f[0][1] == "boast", f)

    # F6: a record refusal from a real answer file: the collection and subgroup are read from the file, the full problem list is kept
    bad = scratch / "temp-2637-bad-answer.json"
    bad.write_text(json.dumps({"command": "ReadWords", "collection": "boast", "subgroup": "boasting", "step": "S1", "rows": [{"ledger_id": 999999999, "fill": {}}]}), encoding="utf-8")
    o = h.record_words(ctx(cfg, "collection.record_words", File=str(bad)))
    f = failures(conn, "collection.record_words")
    case("F6", "a refused answer file is kept with the collection and subgroup of the file, the file and the full message", o.condition == "refused" and len(f) == 1
         and f[0][1:4] == ("boast", "boasting", str(bad)) and f[0][4] == o.message, (f[0][:4] if f else None, o.message[:200]))

    # F7: an unreadable answer file is refused and kept
    o = h.record_words(ctx(cfg, "collection.record_words", File=str(scratch / "no-such-file.json")))
    f = failures(conn, "collection.record_words")
    case("F7", "an answer file that cannot be read is refused and kept", o.condition == "refused" and len(f) == 2 and "cannot read" in f[1][4], f[-1][4][:120] if f else o.message)

    # F8: the rule keys a message names are kept for the count by rule (synthetic message carrying the keys of catalogue K2 and K3)
    h._log_failure(ctx(cfg, "collection.record_structure", Collection="boast", Subgroup="boasting"), "refused",
                   "row 1: the text restates the verse Psa 10:3 ('x'); say what the word does in it (B:131, RW-04)\nrow 2: RS-08 grounds; RO11 one row; XRW-041 is no key")
    f = failures(conn, "collection.record_structure")
    case("F8", "the rule keys named in a message are kept (B:131, RO11, RS-08, RW-04), and no other text is taken for a key", f and f[-1][5] == "B:131,RO11,RS-08,RW-04", f[-1][5] if f else None)

    # F9: a crash in a read is kept as crash with its traceback and still raised, so run.py raises its escalation
    real = rc.read_senses
    rc.read_senses = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("synthetic crash for #2637 X8"))
    try:
        raised = False
        try:
            h.read_senses(ctx(cfg, "collection.read_senses", Collection="boast", Subgroup="boasting"))
        except RuntimeError:
            raised = True
    finally:
        rc.read_senses = real
    f = failures(conn, "collection.read_senses")
    case("F9", "a crash is kept as crash with its traceback and re-raised", raised and bool(f) and f[-1][0] == "crash" and "Traceback" in f[-1][4], (raised, f[-1][0] if f else None))

    # F10: the evidence gate: a message whose checks do not pass stays a refusal (it is a fault), one that passes is next
    src = (ROOT / "iba" / "app" / "lib" / "readcommands.py").read_text(encoding="utf-8")
    case("F10", "the evidence gate raises ReadNext only when the code checks pass", 'raise (ReadNext if chk["passes"] else ReadError)' in src, "source line present")

    # F11: no escalation is written by any of the handler calls above (the handlers never raise one; routing is cfg_on_fail's)
    n = conn.execute("SELECT count(*) FROM escalation WHERE run_id LIKE 'TEST-2637-X8-%'").fetchone()[0]
    case("F11", "no escalation was raised by the refusals", n == 0, n)
    bad.unlink(missing_ok=True)
    passed = sum(r[2] == "PASS" for r in results)
    print(f"{passed} of {len(results)} passed")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
