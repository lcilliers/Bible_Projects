"""encode_2637_run2_fixes_v1_20261126.py -- escalation #2637 v20: the findings of the B:138 run of collection strive.

  K3  the grouping under the read contract: cfg_setting layer.read_types gains `grouping` (its instruction and rules GP-01..GP-04);
      cfg_setting layer.refusals scans lib/collectiongroup.py, each of its refusals keyed, its reads `grouping`
  K2  cfg_setting layer.cycle: the grouping file's view and ValidatePull's working file are package files
  K4  cfg_write_grant file_manifest for every collection step whose handler now registers its report (handlers/collectionbuild.py _register)
Refuses (nothing written) where a refusal site is keyed by no entry or an entry keys no site. Through configmaint.apply_logged; archived after
the live apply. Idempotent. Usage: python iba/app/migration/encode_2637_run2_fixes_v1_20261126.py [--db PATH] [--dry-run]
"""
import argparse
import ast
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged, archive_migration  # noqa: E402
from iba.app.lib import refusalrules  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2637-RUN2FIXES-20261126"
MODULE = "encode_2637_run2_fixes_v1_20261126"
GROUPING = {
    "step": "grouping", "command": "GroupPull",
    "what": "The grouping of one collection (stage 2): every surface of the collection placed in a subgroup by its meaning in context, from the WordNet tables; no verse is read.",
    "read": ["Take one row at a time (`rows`): the surface, its base, its link to the collection, the WordNet evidence (its network group, its pairs in the collection) and the seed group.",
             "The word family is the default gathering; a form goes to another subgroup only with a stated difference in kind of meaning (GP-01, GP-04). A surface WordNet does not hold is a subgroup of its own."],
    "write": ["Fill `groups`: each subgroup's `name` and `definition` (the meaning its surfaces share). Fill each row's `fill`: `group` (one of `groups`), `certainty` decided or uncertain, and for uncertain `uncertain` (what is left open); a surface plainly not a member in meaning is set aside with its `reason`.",
              "A surface is placed whole, never by Strong's code; every surface of the collection is answered once.",
              "Then: Collection-Build.ps1 -Action CheckAnswer -File <the grouping file>: every problem at once, each with its rule, nothing written; correct the file until it finds none, then -Action GroupRecord -File <the grouping file>."],
    "rules": ["GP-01", "GP-02", "GP-03", "GP-04"]}
NEW_ENTRIES = [("PC-05", "has no index rows"), ("GP-01", "surfaces are split by Strong's code in the index"), ("GP-03", "a surface is placed whole, never by Strong's code"),
               ("PC-03", "not a surface of the index of"), ("GP-03", "an answer by code is not allowed"), ("GP-03", "a surface set aside gives its reason"),
               ("PC-03", "is not in the file's list of groups"), ("GP-04", "an uncertain placement says what is left open"), ("PC-04", "certainty is decided or uncertain"),
               ("GP-02", "surfaces are not answered")]
PATTERNS = {r"^group-{c}-\d{8}\.json$": r"^group-{c}-\d{8}\.(json|md)$"}
VALIDATE_PATTERN = r"^validate-{c}(-[a-z0-9-]+)?\.json$"


def registering_steps(conn) -> list[str]:
    tree = ast.parse((ROOT / "iba" / "app" / "handlers" / "collectionbuild.py").read_text(encoding="utf-8"))
    helpers = {f.name for f in tree.body if isinstance(f, ast.FunctionDef) and f.name.startswith("_") and f.name != "_register" and "_register(ctx" in ast.unparse(f)}
    names = [f.name for f in tree.body if isinstance(f, ast.FunctionDef) and f.name != "_register"
             and ("_register(ctx" in ast.unparse(f) or any(f"{h}(" in ast.unparse(f) for h in helpers if h != f.name))]
    return [r[0] for r in conn.execute("SELECT step FROM cfg_step WHERE inactive=0 AND handler IN (%s)" % ",".join("?" * len(names)),
                                       [f"iba.app.handlers.collectionbuild:{n}" for n in names])]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = []
    reg = json.loads(json.dumps(refusalrules.load(conn)))
    if "lib/collectiongroup" not in reg["scan"]["modules"]:
        reg["scan"]["modules"].append("lib/collectiongroup")
    reg["site_reads"]["collectiongroup"] = ["grouping"]
    if "grouping" not in reg["reads_order"]:
        reg["reads_order"] = ["grouping"] + reg["reads_order"]
    have = {(e["key"], e["match"]) for e in reg["entries"]}
    reg["entries"] += [{"key": k, "match": m} for k, m in NEW_ENTRIES if (k, m) not in have]
    reg, unkeyed, dead, n = refusalrules.build(ROOT, reg)
    if unkeyed or dead:
        raise SystemExit("refused, nothing written:\n" + "\n".join(f"  no entry keys {s['site']}:{s['line']} {s['template'][:100]!r}" for s in unkeyed)
                         + "".join(f"\n  entry keys no site: {e}" for e in dead))
    value = json.dumps(reg, ensure_ascii=False)
    if conn.execute("SELECT value FROM cfg_setting WHERE key=?", (refusalrules.SETTING,)).fetchone()[0] != value:
        ops.append(("cfg_setting", "update", {"key": refusalrules.SETTING}, {"value": value}))
    rt = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.read_types'").fetchone()[0])
    before = json.dumps(rt, sort_keys=True)
    rt.setdefault("grouping", GROUPING)
    for read in reg["reads_order"]:
        need = sorted({e["key"] for e in reg["entries"] if read in e["reads"]} - set(rt[read]["rules"]))
        rt[read]["rules"] = rt[read]["rules"] + need
    if json.dumps(rt, sort_keys=True) != before:
        ops.append(("cfg_setting", "update", {"key": "layer.read_types"}, {"value": json.dumps(rt, ensure_ascii=False)}))
    cyc = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.cycle'").fetchone()[0])
    pats = [PATTERNS.get(p, p) for p in cyc["package_patterns"]]
    if VALIDATE_PATTERN not in pats:
        pats.append(VALIDATE_PATTERN)
    if pats != cyc["package_patterns"]:
        cyc["package_patterns"] = pats
        ops.append(("cfg_setting", "update", {"key": "layer.cycle"}, {"value": json.dumps(cyc)}))
    for st in registering_steps(conn):
        if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name='file_manifest'", (st,)).fetchone():
            ops.append(("cfg_write_grant", "insert", {}, {"writer": st, "table_name": "file_manifest", "database": "iba", "inactive": 0}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py", "purpose": "migration of #2637 v20: the grouping under the read contract, Cycle patterns, manifest grants",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "a one-off migration; its values are the config it writes",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s); {n} refusal sites keyed")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or {k: str(v)[:50] for k, v in list(set_.items())[:2]})
        return 0
    for t, op, where, set_ in ops:
        apply_logged(conn, RUN_ID, t, op, where, set_)
    conn.commit()
    print(f"applied (run {RUN_ID}): {len(ops)} write(s); {n} refusal sites keyed")
    if pathlib.Path(a.db).resolve() == DEFAULT_DB.resolve():
        print(f"archived: {archive_migration(conn, RUN_ID, __file__)}")
        conn.commit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
