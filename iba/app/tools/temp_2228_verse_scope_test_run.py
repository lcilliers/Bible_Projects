"""temp_2228_verse_scope_test_run.py -- test plan for escalation #2228 tool 1, the scope resolver
(outputs/escalation/2228-scope-resolver-design-v1-20261022.md section 4, cases 1-17). Run on a copy of
iba.db made with lib/dbsnapshot.copy_db, with both migrations (#2233, #2228) applied to the copy; output
files go to the scratch folder, never to the live outputs/.

Expected values are computed independently by plain SQL on the copy, not by the resolver.

Usage: python iba/app/tools/temp_2228_verse_scope_test_run.py <scratch dir>
"""
import json
import pathlib
import shutil
import sqlite3
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import Db  # noqa: E402
from iba.app.lib import versescope as vs  # noqa: E402
from iba.app.handlers import versescope as hv  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2228"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
mig_out = []
env = {**__import__("os").environ, "PYTHONPATH": str(ROOT)}     # an archived migration imports iba.app from ROOT
for m in ("bare_strong_rule_2233_v1_20261022.py", "verse_scope_2228_v1_20261022.py",
          "reading_index_2228_v1_20261023.py",            # carries the guard settings
          "guard_review_sc16_2228_2220_v1_20261023.py"):   # the size guard at 2500, held for review
    mp = ROOT / "iba/app/migration" / m
    mp = mp if mp.exists() else ROOT / "iba/app/migration/archive" / m
    for _ in range(2):
        r = subprocess.run([sys.executable, str(mp), "--db", str(DB)], capture_output=True, text=True, env=env)
        mig_out.append((r.stdout or r.stderr).strip())
c = sqlite3.connect(DB)
c.execute("UPDATE cfg_setting SET value=? WHERE key='verse_scope.output_dir'", (json.dumps(str(S / "out")),))
# synthetic stale code (copy only): a code with no occurrence and no derivative in a word's list (T13d)
c.execute("INSERT INTO word_strong (word_id, strong, deleted) SELECT id, 'H9998', 0 FROM word_registry "
          "WHERE word='courage' AND deleted=0")
# lib/valuequality finds the other database relative to the iba.db file; on a scratch copy that is wrong,
# so the copy (only) names it absolutely (T19)
for (k, v) in c.execute("SELECT key, value FROM cfg_setting WHERE key LIKE 'database.%.path' AND inactive=0").fetchall():
    c.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(str(ROOT / json.loads(v))), k))
c.commit()
c.close()

cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
results = []


def case(cid, desc, passed, evidence, secs=None):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:400],
                    f"{secs:.2f}" if secs is not None else ""))


def q(sql, *a):
    return conn.execute(sql, a).fetchall()


def run(request):
    t0 = time.time()
    out = vs.resolve(cfg, vs.normalise_request(request))
    return out, time.time() - t0


def ids(out):
    return [v["verse_id"] for v in out["verses"]]


def verses_of(codes):
    return {r[0] for r in q("SELECT DISTINCT verse_id FROM verse_lexical WHERE deleted=0 AND strong IN "
                            "(SELECT value FROM json_each(?))", json.dumps(codes))}


def cluster_codes(cl):
    return [r[0] for r in q("SELECT strong FROM cluster_strong WHERE cluster_code=? AND deleted=0", cl)]


case("T0", "migrations: applied (or already applied on the live source), then skipped on a re-run",
     all(("write(s) applied" in mig_out[i] or "already" in mig_out[i]) and "already" in mig_out[i + 1]
         for i in (0, 2, 4, 6)), " / ".join(mig_out))
changes_before = conn.total_changes

# 1 cluster
out, s = run({"Cluster": "M25"})
want = verses_of(cluster_codes("M25"))
case("T1", "-Cluster M25: the verses of its live strongs; every route names an M25 strong",
     set(ids(out)) == want and all(r["via"] in cluster_codes("M25") for v in out["verses"] for r in v["routes"]),
     f"{len(ids(out))} verses, SQL {len(want)}", s)

# 2 two clusters (2,672 verses: over the 2,500 review limit, so given with a review)
try:
    run({"Cluster": "M25,M02"})
    case("T2a", "-Cluster M25,M02 (2,672 verses, over 2,500): held for review", False, "not held")
except vs.ScopeError as e:
    case("T2a", "-Cluster M25,M02 (2,672 verses, over 2,500): held for review", "held for review" in str(e)
         and "-Reviewed" in str(e), str(e)[:200])
out, s = run({"Cluster": "M25,M02", "Reviewed": "test review"})
want2 = want | verses_of(cluster_codes("M02"))
both = want & verses_of(cluster_codes("M02"))
two = [v for v in out["verses"] if v["verse_id"] in both]
case("T2", "-Cluster M25,M02 -Reviewed: the union, the review recorded; a verse in both carries routes from both",
     set(ids(out)) == want2 and both and out.get("reviewed") == "test review"
     and all({r["value"] for r in v["routes"]} == {"M25", "M02"} for v in two),
     f"{len(ids(out))} verses, SQL {len(want2)}; {len(both)} in both; reviewed {out.get('reviewed')!r}", s)
out, s = run({"Cluster": "M25", "Reviewed": "not needed"})
case("T2b", "-Cluster M25 (2,027, under the limit) with -Reviewed: no review recorded (none was needed)",
     "reviewed" not in out, out["counts"], s)

# 3 bare strong decomposed
derived = sorted(r[0] for r in q("SELECT DISTINCT strong FROM verse_lexical WHERE deleted=0 AND strong GLOB 'H0430[A-Za-z]*'"))
out, s = run({"Strong": "H0430"})
got = [x["code"] for x in out["selectors"][0]["strongs"]]
case("T3", "-Strong H0430 (bare): decomposed to every derivative that occurs",
     got == derived and set(ids(out)) == verses_of(derived), f"derivatives {got}; {len(ids(out))} verses", s)

# 3b bare written short, and a bare code that occurs itself
out, s = run({"Strong": "H430"})
case("T3b", "-Strong H430: zero-padded to H0430, same derivatives", [x["code"] for x in out["selectors"][0]["strongs"]] == derived,
     out["selectors"][0]["strongs"], s)
bare_self = q("SELECT strong FROM verse_lexical WHERE deleted=0 AND strong GLOB '[HG][0-9][0-9][0-9][0-9]' LIMIT 1")[0][0]
out, s = run({"Strong": bare_self})
case("T3c", f"-Strong {bare_self} (a bare code that occurs itself): taken as it is",
     [x["code"] for x in out["selectors"][0]["strongs"]] == [bare_self], out["selectors"][0]["strongs"], s)

# 4 suffixed
out, s = run({"Strong": "H0430H"})
case("T4", "-Strong H0430H: only that code", set(ids(out)) == verses_of(["H0430H"])
     and [x["code"] for x in out["selectors"][0]["strongs"]] == ["H0430H"], f"{len(ids(out))} verses", s)

# 5 occurs nowhere
for cid, code in (("T5", "H9999"), ("T5b", "H0430Q")):
    try:
        run({"Strong": code})
        case(cid, f"-Strong {code} (occurs nowhere): refused", False, "no error")
    except vs.ScopeError as e:
        case(cid, f"-Strong {code} (occurs nowhere): refused, naming it", code in str(e), e)

# 6 filter
out, s = run({"Cluster": "M02", "OnlyStrong": "H3708A"})
want6 = verses_of(cluster_codes("M02")) & verses_of(["H3708A"])
case("T6", "-Cluster M02 -OnlyStrong H3708A: only the M02 verses holding H3708A",
     set(ids(out)) == want6 and out["only_strong"]["verses_dropped"] == len(verses_of(cluster_codes("M02"))) - len(want6),
     f"{len(ids(out))} verses, SQL {len(want6)}; dropped {out['only_strong']['verses_dropped']}", s)

# 7 verse references, canonical order
rom8 = {r[0] for r in q("SELECT id FROM verse WHERE deleted=0 AND osisId LIKE 'Rom.8.%'")}
out, s = run({"Verse": "Rom 8"})
case("T7a", "-Verse \"Rom 8\": the whole chapter", set(ids(out)) == rom8, f"{len(ids(out))} verses, SQL {len(rom8)}", s)
out, s = run({"Verse": "Luk 14:12-14; Psa 10:2"})
refs = [v["reference"] for v in out["verses"]]
case("T7b", "-Verse \"Luk 14:12-14; Psa 10:2\": 4 verses, Psalms before Luke", len(refs) == 4 and refs[0].startswith("Psa"),
     refs, s)
gen = {r[0] for r in q("SELECT id FROM verse WHERE deleted=0 AND osisId IN ('Gen.1.30','Gen.1.31','Gen.2.1','Gen.2.2')")}
out, s = run({"Verse": "Gen 1:30-2:2"})
case("T7c", "-Verse \"Gen 1:30-2:2\": a range across chapters", set(ids(out)) == gen, [v["reference"] for v in out["verses"]], s)

# 8 a verse with no verse row: a Nehemiah verse whose neighbours exist
osis = {r[0] for r in q("SELECT osisId FROM verse WHERE deleted=0 AND osisId LIKE 'Neh.%'")}
missing = None
for o in sorted(osis):
    b, ch, v = o.split(".")
    if f"Neh.{ch}.{int(v) + 1}" not in osis and f"Neh.{ch}.{int(v) + 2}" in osis:
        missing = f"Neh {ch}:{int(v) + 1}"
        break
out, s = run({"Verse": missing})
case("T8", f"-Verse \"{missing}\" (no verse row): listed as not resolved, by design",
     not out["verses"] and out["not_resolved"] and "by design" in out["not_resolved"][0]["reason"], out["not_resolved"], s)

# 9 chapter and one block
cid, CH = q("SELECT ch.id, ch.chapter_no FROM narrative_chapter ch JOIN narrative_section s ON s.chapter_id=ch.id AND "
            "s.last_version IS NULL WHERE ch.inactive=0 AND EXISTS (SELECT 1 FROM narrative_citation c WHERE "
            "c.section_id=s.id AND c.last_version IS NULL AND c.verse_id IS NOT NULL) GROUP BY ch.id "
            "ORDER BY count(*) DESC LIMIT 1")[0]
want9 = {r[0] for r in q("SELECT DISTINCT c.verse_id FROM narrative_citation c JOIN narrative_section s ON s.id=c.section_id "
                         "WHERE s.chapter_id=? AND s.last_version IS NULL AND c.last_version IS NULL AND c.verse_id IS NOT NULL", cid)}
nocite = q("SELECT count(*) FROM narrative_section s WHERE s.chapter_id=? AND s.last_version IS NULL AND NOT EXISTS "
           "(SELECT 1 FROM narrative_citation c WHERE c.section_id=s.id AND c.last_version IS NULL AND c.verse_id IS NOT NULL)", cid)[0][0]
out, s = run({"Chapter": CH})
blocks_missed = [x for x in out["not_resolved"] if x["kind"] == "block"]
case("T9a", f"-Chapter {CH}: the cited verses of its current blocks; blocks that cite none listed",
     set(ids(out)) == want9 and len(blocks_missed) == nocite,
     f"{len(ids(out))} verses, SQL {len(want9)}; {len(blocks_missed)} blocks with no citation, SQL {nocite}", s)
sid, head = q("SELECT s.id, s.heading FROM narrative_section s WHERE s.chapter_id=? AND s.last_version IS NULL AND EXISTS "
              "(SELECT 1 FROM narrative_citation c WHERE c.section_id=s.id AND c.last_version IS NULL AND c.verse_id IS NOT NULL) "
              "ORDER BY s.ordinal LIMIT 1 OFFSET 1", cid)[0]
want9b = {r[0] for r in q("SELECT DISTINCT verse_id FROM narrative_citation WHERE section_id=? AND last_version IS NULL "
                          "AND verse_id IS NOT NULL", sid)}
out, s = run({"Chapter": CH, "Section": head})
case("T9b", f"-Chapter {CH} -Section \"{head}\": that block's cited verses only", set(ids(out)) == want9b,
     f"{len(ids(out))} verses, SQL {len(want9b)}", s)
try:
    run({"Chapter": CH, "Section": "no such heading"})
    case("T9c", "-Section that does not exist: refused", False, "no error")
except vs.ScopeError as e:
    case("T9c", "-Section that does not exist: refused", True, e)

# 10 claim with no verse source, and one with verses
cref = q("SELECT c.claim_ref FROM narrative_claim c WHERE c.status='current' AND NOT EXISTS (SELECT 1 FROM narrative_claim_source s "
         "WHERE s.claim_id=c.id AND s.source_kind='verse' AND s.verse_id IS NOT NULL) LIMIT 1")[0][0]
out, s = run({"Claim": cref})
case("T10a", f"-Claim {cref} (no verse source): zero verses, with the reason",
     not out["verses"] and any(x["kind"] == "claim" for x in out["not_resolved"]), out["not_resolved"], s)
out, s = run({"Claim": "C-330"})
want10 = {r[0] for r in q("SELECT verse_id FROM narrative_claim_source s JOIN narrative_claim c ON c.id=s.claim_id "
                          "WHERE c.claim_ref='C-330' AND s.source_kind='verse' AND s.verse_id IS NOT NULL")}
case("T10b", "-Claim C-330: its verse sources", set(ids(out)) == want10, f"{len(ids(out))} verses, SQL {len(want10)}", s)

# 11 observation with no node, and one with
oid = q("SELECT o.id FROM ib_observation o WHERE o.status='draft' AND NOT EXISTS (SELECT 1 FROM ib_node n WHERE n.observation_id=o.id) LIMIT 1")[0][0]
out, s = run({"Observation": str(oid)})
case("T11a", f"-Observation {oid} (no node): zero verses, with the reason", not out["verses"] and out["not_resolved"],
     out["not_resolved"], s)
out, s = run({"Observation": "12478"})
case("T11b", "-Observation 12478: Ecc 7:9", [v["osis"] for v in out["verses"]] == ["Eccl.7.9"], ids(out), s)

# 12 thread
tid = q("SELECT id FROM escalation WHERE type='thread' AND alias='OT-108'")[0][0]
items = q("SELECT item_no, kind FROM escalation_thread_item WHERE escalation_id=? AND status='open'", tid)
try:
    run({"Thread": "OT-108"})
    case("T12g", "-Thread OT-108 under the guard (verse_scope.max_verses 4000): refused as too wide", False, "not refused")
except vs.ScopeError as e:
    case("T12g", "-Thread OT-108 under the guard (verse_scope.max_verses 2500): held for review", "too wide" in str(e),
         str(e)[:200])
# the thread's resolution itself, given with a review
out, s = run({"Thread": "OT-108", "Reviewed": "test: resolve the whole thread"})
seen_items = {x.get("item") for x in out["selectors"]} | {str(x["value"]).split(" ")[0] for x in out["not_resolved"] if x["kind"] == "item"}
every = all(f"OT-108.{no}" in seen_items for no, _ in items)
noverse = [f"OT-108.{no}" for no, k in items if k not in ("verse", "cluster", "strong", "chapter", "strand")]
reported = all(any(x["kind"] == "item" and str(x["value"]).startswith(i) for x in out["not_resolved"]) for i in noverse)
case("T12", "-Thread OT-108 -Reviewed: every open item resolved or reported; kinds that name no verse reported",
     every and reported, f"{len(items)} open items ({', '.join(sorted({k for _, k in items}))}); {len(ids(out))} verses; "
     f"{len(noverse)} with no verse kind", s)
out, s = run({"Item": f"OT-108.{items[0][0]}"})
case("T12b", f"-Item OT-108.{items[0][0]}: one item", bool(out["selectors"] or out["not_resolved"]), out["counts"], s)

# 13 strand, subgroup, word
for cid13, req, codes in (
        ("T13a", {"Strand": "anger"}, [r[0] for r in q("SELECT strong FROM reading_strand_strong s JOIN reading_strand r ON r.id=s.strand_id WHERE r.code='anger'")]),
        ("T13b", {"Subgroup": "A_thanksgiving_act"}, [r[0] for r in q("SELECT s.strong FROM cluster_subgroup_strong s JOIN cluster_subgroup g ON g.id=s.cluster_subgroup_id WHERE g.subgroup_code='A_thanksgiving_act' AND coalesce(s.delete_flagged,0)=0")])):
    out, s = run(req)
    case(cid13, f"{req}: the verses of its word family", set(ids(out)) == verses_of(codes),
         f"{len(ids(out))} verses, SQL {len(verses_of(codes))}", s)
out, s = run({"Word": "corruption"})
codes13 = [x["code"] for x in out["selectors"][0]["strongs"]]
case("T13c", "-Word corruption (real: its list holds the bare H4654): decomposed to H4654A, H4654B, nothing unresolved",
     {"H4654A", "H4654B"} <= set(codes13) and "H4654" not in codes13 and not out["not_resolved"], codes13, s)
out, s = run({"Word": "courage"})
case("T13d", "-Word courage (synthetic: H9998 added to its list on the copy): the stale code reported, the rest resolved",
     bool(out["verses"]) and any("H9998" in str(x["value"]) for x in out["not_resolved"]), out["not_resolved"], s)

# 14 request file, through the handler
req = S / "request.json"
req.write_text(json.dumps({"cluster": ["M02"], "only_strong": ["H3708A"]}), encoding="utf-8")


def handler(params, run_id="RUN-TEST-VERSESCOPE"):
    return hv.resolve(Ctx(db=db, cfg=cfg, step=None, run_id=run_id, word="", word_id=None, params=params,
                          step_id="verse_scope.resolve"))


o14 = handler({"Label": "t14", "File": str(req)})
p14 = pathlib.Path(o14.counts["path"])
d14 = json.loads(p14.read_text(encoding="utf-8"))
case("T14", "-File {cluster M02, only_strong H3708A} through the handler: same verses as T6",
     o14.condition == "ok" and {v["verse_id"] for v in d14["verses"]} == want6, f"{p14.name}: {d14['counts']}")

# 15 same label twice
o15a = handler({"Label": "t15", "Cluster": "M07"})
o15b = handler({"Label": "t15", "Cluster": "M07"})
live = sorted(x.name for x in (S / "out").glob("t15-*.json"))
arch = sorted(x.name for x in (S / "out" / "archive").glob("t15-*.json"))
case("T15", "same label twice in a day: v2 live, the first archived", live == [pathlib.Path(o15b.counts["path"]).name]
     and live[0].endswith("-v2.json") and len(arch) == 1, f"live {live}; archive {arch}")
o15c = handler({"Label": "t15c"})
case("T15b", "no selector: refused, no file", o15c.condition == "refused" and not list((S / "out").glob("t15c*")), o15c.message)
o15d = handler({"Label": "t15d", "File": str(S / "nofile.json")})
case("T15c", "-File that does not exist: refused", o15d.condition == "refused", o15d.message)

# 16 read-only
case("T16", "read-only: no row written on the copy by any case", conn.total_changes == changes_before,
     f"total_changes {changes_before} -> {conn.total_changes}")

# 17 speed
slow = [r for r in results if r[4] and float(r[4]) > 5]
case("T17", "every case within 5 seconds", not slow,
     f"slowest {max((float(r[4]) for r in results if r[4]), default=0):.2f}s")

# the rule row (#2233)
rule = q("SELECT id, class, enforcement_status FROM cfg_behaviour_rule WHERE rule_key='bare-strong-decomposed-to-derivatives'")
scopes = q("SELECT scope_kind, scope_value FROM cfg_rule_scope WHERE rule_ref=? AND inactive=0", f"B:{rule[0][0]}") if rule else []
case("T18", "#2233: the rule row and its two point-of-use scopes", bool(rule) and len(scopes) == 2,
     f"{[tuple(r) for r in rule]} {[tuple(r) for r in scopes]}")

# the validator's hard checks on the copy (what configmaint.validate report-stops on)
from iba.app.handlers import configmaint as cm  # noqa: E402
from iba.app.lib import cfgquality  # noqa: E402
errs = cm._validate_live(conn) + cfgquality.find_unregistered_project_scripts(conn, ROOT) \
    + cfgquality.find_rule_scope_gaps(conn, ROOT / "iba" / "app")
case("T19", "configmaint.validate hard checks on the copy: no coherence error", not errs, errs or "none")

lines = ["| # | case | result | evidence | s |", "|---|---|---|---|---|"]
lines += [f"| {a} | {b} | {c} | {d} | {e} |" for a, b, c, d, e in results]
(S / "results.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
print(f"\n{sum(r[2] == 'PASS' for r in results)}/{len(results)} PASS")
