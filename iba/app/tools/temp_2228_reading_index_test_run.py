"""temp_2228_reading_index_test_run.py -- test plan for escalation #2228 tool 2, the cluster reading index
(outputs/escalation/2228-cluster-reading-index-design-v1-20261023.md section 3) and the guard added to the
scope resolver (researcher 2026-10-23). Run on a copy of iba.db made with lib/dbsnapshot.copy_db with the
migration applied to the copy; the files are a scratch copy of _analytics/Clusters, never the live ones
(except the handler case, which reads the live files and writes only the copy).

Usage: python iba/app/tools/temp_2228_reading_index_test_run.py <scratch dir>
"""
import importlib.util
import json
import os
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
from iba.app.lib import narrativeregister as nr  # noqa: E402
from iba.app.lib import readingindex as ri  # noqa: E402
from iba.app.lib import versescope as vs  # noqa: E402
from iba.app.handlers import readingindex as hr  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2228ri"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
env = {**os.environ, "PYTHONPATH": str(ROOT)}
mig = ROOT / "iba/app/migration/reading_index_2228_v1_20261023.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
mo = [subprocess.run([sys.executable, str(mig), "--db", str(DB)], capture_output=True, text=True, env=env)
      for _ in range(2)]
mo = [(r.stdout or r.stderr).strip() for r in mo]
REPO = S / "repo"
shutil.copytree(ROOT / "_analytics" / "Clusters", REPO / "_analytics" / "Clusters")
c = sqlite3.connect(DB)
c.execute("UPDATE cfg_setting SET value=? WHERE key='reading_index.output_dir'", (json.dumps(str(S / "out")),))
c.commit()
c.close()

cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
vx = nr.VerseIndex(cfg)
results = []


def case(cid, desc, passed, evidence, secs=None):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:400],
                    f"{secs:.1f}" if secs is not None else ""))
    print(f"{cid} {'PASS' if passed else 'FAIL'} {time.strftime('%H:%M:%S')}", flush=True)


def q(sql, *a):
    return conn.execute(sql, a).fetchall()


def setting(key, value):
    conn.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(value), key))
    conn.commit()


def W():
    return nr.Writer(conn, "reading_index.build", "Claude")


case("R0", "migration: applied (or already), then skipped", ("applied" in mo[0] or "already" in mo[0]) and "already" in mo[1], mo)

# --- the guard on the scope resolver -----------------------------------------------------------
def resolve(req):
    return vs.resolve(cfg, vs.normalise_request(req))


for cid, req, desc in (("G1", {"Thread": "OT-108"}, "-Thread OT-108 (29,743 verses): refused as too wide, selectors listed"),
                       ("G2", {"Cluster": "T2"}, "-Cluster T2: refused as too wide")):
    try:
        resolve(req)
        case(cid, desc, False, "not refused")
    except vs.ScopeError as e:
        case(cid, desc, "too wide" in str(e) and "against the limit" in str(e), str(e)[:300])
limit = int(q("SELECT value FROM cfg_setting WHERE key='verse_scope.max_verses'")[0][0])
try:
    resolve({"Cluster": "M72"})
    held = False
except vs.ScopeError:
    held = True
out = resolve({"Cluster": "M72", "Reviewed": "test review"})
case("G3", f"-Cluster M72 (3,972 verses): held for review when over the limit ({limit}); allowed with -Reviewed",
     held == (3972 > limit) and out["counts"]["verses"] == 3972, f"held {held}; {out['counts']}")
try:
    resolve({"Cluster": "M72,M02"})
    case("G4a", "-Cluster M72,M02 (over 4,000): refused", False, "not refused")
except vs.ScopeError as e:
    case("G4a", "-Cluster M72,M02 (over 4,000): refused", "too wide" in str(e), str(e)[:200])
out = resolve({"Cluster": "M72,M02", "OnlyStrong": "H3708A"})
case("G4b", "-Cluster M72,M02 -OnlyStrong H3708A: allowed (the size is checked after the filter)",
     0 < out["counts"]["verses"] <= 4000, out["counts"])
setting("verse_scope.max_seconds", 0)
try:
    resolve({"Cluster": "M02"})
    case("G5", "time guard (max_seconds 0 on the copy): refused", False, "not refused")
except vs.ScopeError as e:
    case("G5", "time guard (max_seconds 0 on the copy): refused", "time limit" in str(e), str(e)[:200])
setting("verse_scope.max_seconds", 30)

# --- parse_refs default unchanged ----------------------------------------------------------------
old_src = subprocess.run(["git", "show", "HEAD:iba/app/lib/narrativeregister.py"], cwd=ROOT, capture_output=True,
                         text=True, encoding="utf-8").stdout
tmp = S / "_nr_old_tmp.py"        # in scratch; the module name gives it its package for the relative imports
spec = importlib.util.spec_from_file_location("iba.app.lib._nr_old", tmp)
tmp.write_text(old_src, encoding="utf-8")
try:
    old = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = old
    spec.loader.exec_module(old)
    texts = [r[0] for r in q("SELECT block_text FROM narrative_section WHERE last_version IS NULL AND block_text IS NOT NULL")]
    texts += [p.read_text(encoding="utf-8", errors="replace") for p in (REPO / "_analytics/Clusters").rglob("*.md")]
    norm = lambda refs: [(r.as_written, r.normalised, r.verse_id, r.kind, r.start) for r in refs]  # noqa: E731
    diff = sum(1 for t in texts if norm(nr.parse_refs(t, vx)) != norm(old.parse_refs(t, vx)))
    case("R8", "parse_refs with its default arguments: identical to the committed version over every current narrative "
         "block and every cluster file", diff == 0, f"{len(texts)} texts, {diff} differ")
finally:
    tmp.unlink()

# --- build ---------------------------------------------------------------------------------------
t0 = time.time()
m1 = ri.build(cfg, W(), REPO)
s1 = time.time() - t0
nfiles = len(ri.files_in_roots(REPO, ["_analytics/Clusters"]))
expected = 0
bare = 0
for rel in ri.files_in_roots(REPO, ["_analytics/Clusters"]):
    t = (REPO / rel).read_text(encoding="utf-8", errors="replace")
    expected += len(nr.parse_refs(t, vx, bare_follow_ons=False))
    bare += len(nr.parse_refs(t, vx)) - len(nr.parse_refs(t, vx, bare_follow_ons=False))
got = q("SELECT count(*) FROM reading_ref WHERE deleted=0")[0][0]
case("R1", "build over a scratch copy of _analytics/Clusters: every file, every reference less the bare follow-ons",
     q("SELECT count(*) FROM reading_file WHERE removed=0")[0][0] == nfiles and got == expected,
     f"{nfiles} files; {got} refs = parser {expected} ({bare} bare follow-on refs left out); {m1}", s1)
t0 = time.time()
before = conn.total_changes
m2 = ri.build(cfg, W(), REPO)
case("R2", "build again, nothing changed: no file read, no row written", m2.startswith("0 file(s) indexed")
     and conn.total_changes == before, m2, time.time() - t0)

f3 = REPO / "_analytics/Clusters/M02 - anger-wrath" / sorted(p.name for p in (REPO / "_analytics/Clusters/M02 - anger-wrath").glob("*.md"))[0]
fid3 = q("SELECT id FROM reading_file WHERE path=?", f3.relative_to(REPO).as_posix())[0][0]
old_rows = q("SELECT count(*) FROM reading_ref WHERE file_id=? AND deleted=0", fid3)[0][0]
f3.write_text(f3.read_text(encoding="utf-8") + "\n\n## Added for the test\n\n- the bosom (Ecc 7:9)\n", encoding="utf-8")
m3 = ri.build(cfg, W(), REPO)
new_live = q("SELECT count(*) FROM reading_ref WHERE file_id=? AND deleted=0", fid3)[0][0]
retired = q("SELECT count(*) FROM reading_ref WHERE file_id=? AND deleted=1", fid3)[0][0]
ecc = q("SELECT count(*) FROM reading_ref x JOIN verse v ON v.id=x.verse_id WHERE x.file_id=? AND x.deleted=0 AND v.osisId='Eccl.7.9' AND x.line_kind='bullet'", fid3)[0][0]
case("R3", "one file edited: only it re-read; its earlier rows kept as deleted; the new reference found",
     m3.startswith("1 file(s) indexed") and new_live == old_rows + 1 and retired == old_rows and ecc >= 1,
     f"{m3}; rows {old_rows} -> {new_live} live, {retired} deleted")

files = sorted((REPO / "_analytics/Clusters/M01 - fear-awe").glob("*.md"))
gone, moved = files[0], files[1]
gone.unlink()
(moved.parent / "archive").mkdir(exist_ok=True)
moved.replace(moved.parent / "archive" / moved.name)
m4 = ri.build(cfg, W(), REPO)
rem = q("SELECT path FROM reading_file WHERE removed=1")
leftover = q("SELECT count(*) FROM reading_ref x JOIN reading_file f ON f.id=x.file_id WHERE f.removed=1 AND x.deleted=0")[0][0]
case("R4", "one file deleted, one moved into archive/: both marked removed, their rows deleted",
     len(rem) == 2 and leftover == 0 and "2 marked removed" in m4, f"{m4}; {rem}")

syn = REPO / "_analytics/Clusters/zz-synthetic-test.md"
syn.write_text("\n".join([
    "# Synthetic", "", "Opening names Jer 8:18 and then (8:21) and (v. 22) and a count (220).",
    "", "## Table", "", "| word | count |", "|---|---|", "| anger | Psa 10:2 |",
    "", "## Bullets", "", "- a range Luk 14:12-14", "- a list Rom 8:5, 6", "- a chapter Psa 51",
    "- past the end Gen 1:99", "- no verse row Neh 10:35", "", "### Heading ref Ecc 7:9", ""]), encoding="utf-8")
ri.build(cfg, W(), REPO)
sid = q("SELECT id FROM reading_file WHERE path='_analytics/Clusters/zz-synthetic-test.md'")[0][0]
rows = {(r[0], r[1], r[2], r[3], r[4]) for r in q("SELECT ref_normalised, found_by, line_kind, kind, coalesce(reason,'') FROM reading_ref WHERE file_id=? AND deleted=0", sid)}
want = {("Jer 8:18", "explicit", "paragraph", "verse", ""), ("Jer 8:21", "follow-on c:v", "paragraph", "verse", ""),
        ("Jer 8:22", "follow-on v.", "paragraph", "verse", ""), ("Psa 10:2", "explicit", "table row", "verse", ""),
        ("Luk 14:12", "explicit", "bullet", "verse", ""), ("Luk 14:13", "explicit", "bullet", "verse", ""),
        ("Luk 14:14", "explicit", "bullet", "verse", ""), ("Rom 8:5", "explicit", "bullet", "verse", ""),
        ("Rom 8:6", "explicit", "bullet", "verse", ""), ("Psa 51", "explicit", "bullet", "whole chapter", ""),
        ("Gen 1:99", "explicit", "bullet", "verse", "verse past the end of the chapter"),
        ("Neh 10:35", "explicit", "bullet", "verse", "no verse row (by design: governance.verse_gap_by_design)"),
        ("Ecc 7:9", "explicit", "heading", "verse", "")}
case("R5", "synthetic file: each written form recorded with found_by, line kind and kind; the bare '(220)' not taken",
     rows == want, f"missing {sorted(want - rows)}; extra {sorted(rows - want)}")
lines = q("SELECT ref_normalised, line_no FROM reading_ref WHERE file_id=? AND deleted=0 AND ref_normalised IN ('Jer 8:18','Psa 10:2','Ecc 7:9')", sid)
case("R5b", "line numbers", dict(lines) == {"Jer 8:18": 3, "Psa 10:2": 9, "Ecc 7:9": 19}, lines)
case("R6", "unresolved references kept with their reason", ("Gen 1:99", "explicit", "bullet", "verse", "verse past the end of the chapter") in rows, "see R5")

coll = resolve({"Cluster": "M02", "OnlyStrong": "H3708A"})
vids = [v["verse_id"] for v in coll["verses"]]
t0 = time.time()
hit = q("SELECT DISTINCT x.verse_id FROM reading_ref x JOIN reading_file f ON f.id=x.file_id AND f.removed=0 "
        "WHERE x.deleted=0 AND x.verse_id IN (SELECT value FROM json_each(?))", json.dumps(vids))
case("R7", "query by a verse collection (M02 -OnlyStrong H3708A, 22 verses): one query", len(hit) > 0,
     f"{len(hit)} of {len(vids)} verses named in the cluster files", time.time() - t0)

# --- time guard on the build ----------------------------------------------------------------------
c2 = sqlite3.connect(DB)
c2.execute("UPDATE reading_file SET sha256='x'")                 # every file looks changed
c2.commit()
c2.close()
setting("reading_index.max_seconds", 0)
m9 = ri.build(cfg, W(), REPO)
setting("reading_index.max_seconds", 120)
m10 = ri.build(cfg, W(), REPO)
case("R9", "time guard on the build (max_seconds 0): stops between files, says how many are left; the next build "
     "carries on", "stopped at the time limit" in m9 and "still to index" not in m10 and "file(s) indexed" in m10,
     f"{m9} // {m10}")

# --- report and handler ---------------------------------------------------------------------------
o = hr.report(Ctx(db=db, cfg=cfg, step=None, run_id="RUN-TEST-RI", word="", word_id=None, params={},
                  step_id="reading_index.report"))
rp = pathlib.Path(o.counts["path"])
txt = rp.read_text(encoding="utf-8")
tot = q("SELECT count(*) FROM reading_ref x JOIN reading_file f ON f.id=x.file_id WHERE f.removed=0 AND x.deleted=0")[0][0]
case("R10", "report written to the setting's folder; its total equals the tables", o.condition == "ok"
     and f"**References:** {tot}:" in txt, f"{rp.name}; {tot}")

from iba.app.handlers import configmaint as cm  # noqa: E402
from iba.app.lib import cfgquality  # noqa: E402
for (k, v) in sqlite3.connect(DB).execute("SELECT key, value FROM cfg_setting WHERE key LIKE 'database.%.path' AND inactive=0").fetchall():
    setting(k, str(ROOT / json.loads(v)))
errs = cm._validate_live(conn) + cfgquality.find_rule_scope_gaps(conn, ROOT / "iba" / "app") + [
    e for e in cfgquality.find_unregistered_project_scripts(conn, ROOT) if "iba/app/migration/" not in e]
case("R11", "configmaint.validate hard checks on the copy (a migration not yet archived set aside)", not errs, errs or "none")
case("R12", "speed: full build within a minute", s1 < 60, f"{s1:.1f}s")

lines = ["| # | case | result | evidence | s |", "|---|---|---|---|---|"] + [f"| {a} | {b} | {r} | {e} | {t} |" for a, b, r, e, t in results]
(S / "results.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
print(f"\n{sum(r[2] == 'PASS' for r in results)}/{len(results)} PASS")
