"""temp_2637_refusal_keys_test_run.py -- #2637 plan v3 X4: every refusal of the reading package keyed to a configured rule and printed in the
packet of each read that can meet it (lib/refusalrules.py, cfg_setting layer.refusals, migration encode_2637_refusal_keys_v1_20261126).

Runs on a COPY of iba.db, never the live database: applies the migration to the copy (and again, to show it writes nothing), then holds the
registry to the source and to the config, builds each read's instruction, sends refused answers through the handlers, and keys the historical
problem lines of the known-failures catalogue (outputs/escalation/2637-known-failures-catalogue-v1-20261126.md: the first version of every
escalation raised by a collection.* step).

Usage: python iba/app/tools/temp_2637_refusal_keys_test_run.py <db copy> <scratch dir>
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
from iba.app.lib import refusalrules  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
MIG = next(p for p in [ROOT / "iba" / "app" / "migration" / "encode_2637_refusal_keys_v1_20261126.py",
                       ROOT / "iba" / "app" / "migration" / "archive" / "encode_2637_refusal_keys_v1_20261126.py"] if p.exists())
READS = ["words", "senses", "enrichment", "structure", "sweep", "evidence", "elements", "behaviours"]
results = []


def case(cid, desc, passed, evidence=""):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:400]))
    print(f"[{results[-1][2]}] {cid}: {desc} -- {results[-1][3][:300]}", flush=True)


def ctx(cfg, step, **params):
    return Ctx(db=None, cfg=cfg, step=None, run_id=f"TEST-2637-X4-{step}", word="", word_id=None, params=params, step_id=step)


def active(conn, key):
    if key.startswith("B:"):
        return conn.execute("SELECT 1 FROM cfg_behaviour_rule WHERE active=1 AND id=?", (int(key[2:]),)).fetchone() is not None
    return conn.execute("SELECT 1 FROM cfg_method_rule WHERE active=1 AND (rule_key=? OR rule_key LIKE ?)", (key, key + " %")).fetchone() is not None


def main(db, scratch):
    if pathlib.Path(db).resolve() == LIVE.resolve():
        sys.exit("refused: this test runs on a copy, never the live database")
    scratch = pathlib.Path(scratch)
    out = [subprocess.run([sys.executable, str(MIG), "--db", db], capture_output=True, text=True) for _ in range(2)]
    case("K1", "the migration applies on the copy, and a second apply writes nothing",
         ("applied (run" in out[0].stdout or "already applied: 0" in out[0].stdout) and "already applied: 0" in out[1].stdout, " / ".join((o.stdout + o.stderr).strip()[:150] for o in out))
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    pc = [r[0] for r in conn.execute("SELECT rule_key FROM cfg_method_rule WHERE active=1 AND rule_key LIKE 'PC-0%' ORDER BY rule_key")]
    case("K2", "the read contract PC-01..PC-07 is active in cfg_method_rule", len(pc) == 7, pc)

    reg = refusalrules.load(conn)
    sites = refusalrules.scan(ROOT, reg)
    unkeyed = [s for s in sites if not s["wrapper"] and refusalrules.key_of(reg, s["template"], s["site"]) is None]
    case("K3", "every refusal site of the scanned modules is keyed by an entry (a wrapper passes on a keyed message)", sites and not unkeyed,
         f"{len(sites)} sites ({sum(s['wrapper'] for s in sites)} wrappers), unkeyed: {[(s['site'], s['line']) for s in unkeyed][:8]}")
    bad = sorted({e["key"] for e in reg["entries"] if not active(conn, e["key"])})
    case("K4", "every entry's key is an active rule (cfg_method_rule, or cfg_behaviour_rule for B:<id>)", not bad, bad or f"{len({e['key'] for e in reg['entries']})} keys")
    rt = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.read_types'").fetchone()[0])
    gaps = [(e["key"], r) for e in reg["entries"] for r in e["reads"] if e["key"] not in rt[r]["rules"]]
    case("K5", "every entry's key is among the rules of each read it names, so the packet prints the rule's text", not gaps, gaps[:8])
    keyed = set()
    for s in sites:
        keyed.add(next((i for i, e in enumerate(reg["entries"]) if (not e.get("site") or e["site"] == s["site"]) and e["match"] in s["template"]), None))
    dead = [e for i, e in enumerate(reg["entries"]) if i not in keyed]
    noread = [e for e in reg["entries"] if not e.get("reads")]
    case("K6", "no entry keys no site, and every entry names the reads that meet it", not dead and not noread, (dead + noread)[:5])

    # K7: the instruction of every read prints its refusals by rule, and the text of each of those rules
    probs = []
    for r in READS:
        ins = rc.instruction(conn, rt[r])
        kept = {k["rule"].split(" ")[0] for k in ins["keep"]}
        rw = ins.get("refused_when") or {}
        if not rw:
            probs.append(f"{r}: no refusals printed")
        missing = [k for k in rw if k not in kept]
        if missing:
            probs.append(f"{r}: refusals of {missing} printed without the rule's text")
        if rw != refusalrules.for_read(reg, r):
            probs.append(f"{r}: refused_when differs from the registry")
    case("K7", "each of the 8 reads prints its refusals by rule, and keeps the text of every rule it prints", not probs,
         probs or {r: len(refusalrules.for_read(reg, r)) for r in READS})

    # K8: annotate keys a refusal line by line; a heading and an unknown line are left as they are
    msg = ("the file is refused, nothing written; problems:\n  row 2: the same text as row 1 -- one finding, many nodes\n"
           "  row 3 nodes[0]: a node is an object\n  something no rule names")
    a = refusalrules.annotate(conn, msg).split("\n")
    case("K8", "a synthetic refusal: the heading and an unknown line unkeyed, the two problems keyed [RW-03] and [PC-02]",
         a[0] == msg.split("\n")[0] and a[1].startswith("  [RW-03] row 2") and a[2].startswith("  [PC-02] row 3") and a[3] == "  something no rule names", a)

    # K9, K10: real refusals through the handler: the message shown is keyed and read_failure keeps the keys
    wrong = scratch / "temp-2637-x4-wrong-command.json"
    wrong.write_text(json.dumps({"command": "ReadSenses", "collection": "boast", "subgroup": "boasting", "rows": []}), encoding="utf-8")
    o = h.record_words(ctx(cfg, "collection.record_words", File=str(wrong)))
    f = conn.execute("SELECT problems, rule_keys FROM read_failure WHERE run_id=? ORDER BY id DESC LIMIT 1", ("TEST-2637-X4-collection.record_words",)).fetchone()
    case("K9", "RecordWords given another read's answer: refused, the line keyed [PC-02], read_failure keeps PC-02",
         o.condition == "refused" and "[PC-02]" in o.message and f is not None and "PC-02" in (f[1] or ""), (o.condition, o.message[:200], f[1] if f else None))
    ghost = scratch / "temp-2637-x4-ghost-ledger.json"
    ghost.write_text(json.dumps({"command": "ReadWords", "collection": "boast", "subgroup": "boasting", "step": "S1",
                                 "rows": [{"ledger_id": 999999999, "fill": {}}]}), encoding="utf-8")
    o = h.record_words(ctx(cfg, "collection.record_words", File=str(ghost)))
    case("K10", "RecordWords naming a ledger row the packet did not offer: refused, the line keyed [PC-03]",
         o.condition == "refused" and "[PC-03]" in o.message, o.message[:300])

    # K11: the historical problem lines of the catalogue (first version of every collection.* escalation), each keyed by the registry
    lines, crash, nxt = [], 0, 0
    heads = [hd.split("{}")[-1].strip() for hd in reg["scan"]["headings"]]
    for (ctxj,) in conn.execute("SELECT context FROM escalation e WHERE at_step LIKE 'collection.%' AND version=(SELECT min(version) FROM escalation e2 WHERE e2.id=e.id)"):
        try:
            full = (json.loads(ctxj) or {}).get("full_message") or ""
        except Exception:
            full = ctxj or ""
        if "Traceback" in full or "Error(" in full or "locked" in full or " crashed:" in full:
            crash += 1
            continue
        for ln in full.split("\n"):
            ln = ln.strip()
            for hd in heads:
                if ln.startswith(hd) or ln.endswith(hd):
                    ln = ln.replace(hd, "").strip()
            if not ln:
                continue
            if "next:" in ln.lower() or "nothing to read" in ln.lower() or "is read and validated" in ln:
                nxt += 1
                continue
            lines.append(ln)
    miss = sorted({ln for ln in lines if refusalrules.key_of(reg, ln) is None})
    case("K11", "every historical problem line of the catalogue is keyed (crashes and next-step messages apart)", lines and not miss,
         f"{len(lines)} lines, {crash} crashes and {nxt} next-step lines apart; unkeyed {len(miss)}: {[m[:90] for m in miss[:8]]}")

    rep = scratch / "temp-2637-x4-results.md"
    rep.write_text("| case | what | result | evidence |\n|---|---|---|---|\n" + "\n".join(f"| {c} | {d} | {r} | {e} |" for c, d, r, e in results) + "\n", encoding="utf-8")
    n = sum(1 for r in results if r[2] == "PASS")
    print(f"{n} of {len(results)} passed; results: {rep}")
    return 0 if n == len(results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
