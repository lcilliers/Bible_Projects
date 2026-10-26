"""temp_2295_scope_resolver_test_run.py -- the test of escalation #2295 (#2286 U5): the occurrence-shaped scope resolver
(lib/versescope.py) and its callers. Runs on a copy of iba.db made with lib/dbsnapshot.copy_db, with the migration
applied to the copy and every output redirected to the scratch directory. Expected values are computed by plain SQL on
the copy, not by the resolver. The settlement observations here are synthetic: they test the resolver, not a reading.

Usage: python iba/app/tools/temp_2295_scope_resolver_test_run.py <scratch dir>
"""
import json
import os
import pathlib
import shutil
import sqlite3
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import Db  # noqa: E402
from iba.app.lib import versescope as vs  # noqa: E402
from iba.app.lib import versecollate as vc  # noqa: E402
from iba.app.lib import cfgquality as cq  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2295"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"}
mig = ROOT / "iba/app/migration/scope_resolver_2295_v1_20261026.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
mo = [(lambda r: (r.stdout or r.stderr).strip())(subprocess.run([sys.executable, str(mig), "--db", str(DB)] + x,
                                                                 capture_output=True, text=True, env=env))
      for x in (["--dry-run"], [], [])]
c = sqlite3.connect(DB)
for key, val in (("reading.output_dir", str(S / "reading")), ("verse_scope.output_dir", str(S / "scope")),
                 ("verse_collate.output_dir", str(S / "collate"))):
    c.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(val), key))
for (k, v) in c.execute("SELECT key, value FROM cfg_setting WHERE key LIKE 'database.%.path' AND inactive=0").fetchall():
    c.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(str(ROOT / json.loads(v))), k))
c.commit()
c.close()
cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
from iba.app.handlers import versescope as hv  # noqa: E402
from iba.app.handlers import reading as hr  # noqa: E402
results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/").replace("\n", " ")[:600]))
    print(f"{cid} {'PASS' if passed else 'FAIL'}" + ("" if passed else f"  {str(evidence)[:900]}"), flush=True)


def ctx(step_id, **params):
    return Ctx(db=db, cfg=cfg, step=None, run_id=f"RUN-TEST-{step_id}", word="", word_id=None,
               params={k: v for k, v in params.items() if v is not None}, step_id=step_id)


def q(sql, *a):
    return conn.execute(sql, a).fetchall()


def run(**req):
    return vs.resolve(cfg, vs.normalise_request(req))


def refused(**req):
    try:
        run(**req)
    except vs.ScopeError as exc:
        return str(exc)
    return None


def in_scope(out):
    return {o["id"] for v in out["verses"] for o in v["occurrences"] + v["context"] if o["in_scope"]}


def pair_occ(where, arg):
    return {r[0]: r[1] for r in q("SELECT v.id, v.verse_id FROM surface_subgroup s JOIN verse_lexical v ON "
                                  "v.strong=s.strong AND lower(trim(coalesce(v.surface,'')))=s.surface AND v.deleted=0 "
                                  "WHERE s.deleted=0 AND " + where, arg)}


def sg_id(code):
    return q("SELECT id FROM cluster_subgroup WHERE subgroup_code=?", code)[0][0]


def ok(o):
    return o.condition == "ok"


# ── T1 subgroup: exact to the occurrence ─────────────────────────────────────────────────────────────────────────────
o = run(Subgroup="M18_desire")
want = pair_occ("s.cluster_subgroup_id=?", sg_id("M18_desire"))
case("T1", "-Subgroup M18_desire: the verses and in-scope occurrences are exactly its pairs' occurrences; it is the "
     "home; version 2", {v["verse_id"] for v in o["verses"]} == set(want.values()) and in_scope(o) == set(want) and
     o["home"] == ["M18_desire"] and o["version"] == 2 and o["counts"]["home"] == len(want),
     (len(o["verses"]), len(want), o["counts"]))
other = {x["subgroup"] for v in o["verses"] for x in v["occurrences"] if not x["home"]}
case("T1b", "the other subgroups in the verses are shown, not in scope, and add no verse (B:120)",
     bool(other) and all(not x["in_scope"] for v in o["verses"] for x in v["occurrences"] if not x["home"]),
     (len(other), sorted(o for o in other if o)[:5]))

# ── T2 a mapped M cluster ────────────────────────────────────────────────────────────────────────────────────────────
o = run(Cluster="M18")
codes = [r[0] for r in q("SELECT strong FROM cluster_strong WHERE cluster_code='M18' AND deleted=0")]
allv = {r[0] for r in q("SELECT DISTINCT verse_id FROM verse_lexical WHERE deleted=0 AND strong IN "
                        "(SELECT value FROM json_each(?))", json.dumps(codes))}
case("T2", "-Cluster M18 (fully mapped): through its pairs, every verse of its codes (1,370), 1,510 occurrences in "
     "scope, nothing unresolved; entered_by surface pairs",
     {v["verse_id"] for v in o["verses"]} == allv and o["counts"]["in_scope"] == 1510 and not o["not_resolved"] and
     o["selectors"][0]["entered_by"] == "surface pairs", (len(o["verses"]), len(allv), o["counts"]))

# ── T3 a T cluster enters by its codes, and is not a home ────────────────────────────────────────────────────────────
o = run(Cluster="T15")
case("T3", "-Cluster T15: entered by its codes; no home; its occurrences in scope are context",
     o["selectors"][0]["entered_by"] == "codes" and o["home"] == [] and o["counts"]["in_scope"] > 0 and
     all(x["in_scope"] for v in o["verses"] for x in v["context"] if "T15" in x["clusters"]),
     (o["counts"], o["selectors"][0].get("entered_by")))

# ── T4 a pair taken away: its occurrences leave the cluster scope, reported ──────────────────────────────────────────
pid, pst, psf = q("SELECT id, strong, surface FROM surface_subgroup WHERE cluster_code='M67' AND deleted=0 ORDER BY id "
                  "LIMIT 1")[0]
conn.execute("UPDATE surface_subgroup SET deleted=1 WHERE id=?", (pid,))
n_loose = q("SELECT count(*) FROM verse_lexical WHERE deleted=0 AND strong=? AND lower(trim(coalesce(surface,'')))=?",
            pst, psf)[0][0]
loose_v = q("SELECT v.reference FROM verse_lexical l JOIN verse v ON v.id=l.verse_id WHERE l.deleted=0 AND l.strong=? AND "
            "lower(trim(coalesce(l.surface,'')))=? LIMIT 1", pst, psf)[0][0]
o = run(Cluster="M67", Verse=loose_v)
case("T4", "a cluster with an unpaired occurrence: the occurrence is left out and named in not_resolved, with the "
     "next step", any(f"{n_loose} occurrence" in x["reason"] and "Surface-Map.ps1" in x["reason"]
                      for x in o["not_resolved"]), (n_loose, o["not_resolved"]))
unpl = [x for v in o["verses"] for x in v["occurrences"] if x.get("unplaced")]
case("T4b", "the unpaired occurrence is listed in its verse (brought in by -Verse) as unplaced, in the home cluster",
     len(unpl) >= 1 and all(x["subgroup"] is None and x["home"] for x in unpl), unpl[:2])
conn.execute("UPDATE surface_subgroup SET deleted=0 WHERE id=?", (pid,))
conn.execute("UPDATE surface_subgroup SET deleted=1 WHERE cluster_code='M49'")
o = run(Cluster="M49")
case("T4c", "a cluster with no live pair enters by its codes (as before the mapping)",
     o["selectors"][0]["entered_by"] == "codes" and bool(o["verses"]), o["selectors"][0])
conn.rollback()

# ── T5 word: through the surface, never word_strong ──────────────────────────────────────────────────────────────────
o = run(Word="seek")
want = {r[0] for r in q("SELECT id FROM verse_lexical WHERE deleted=0 AND lower(trim(surface))='seek'")}
case("T5", "-Word seek: the in-scope occurrences are exactly those whose surface is 'seek' (any case); near surfaces "
     "listed, not taken", in_scope(o) == want and bool(o["selectors"][0]["near_surfaces_not_taken"]) and
     o["selectors"][0]["entered_by"] == "surface",
     (len(in_scope(o)), len(want), o["selectors"][0]["near_surfaces_not_taken"][:3]))
reg = q("SELECT w.word FROM word_registry w WHERE w.deleted=0 AND EXISTS (SELECT 1 FROM word_strong ws WHERE "
        "ws.word_id=w.id AND ws.deleted=0) AND EXISTS (SELECT 1 FROM verse_lexical v WHERE v.deleted=0 AND "
        "lower(trim(v.surface))=lower(w.word)) ORDER BY w.word LIMIT 1")[0][0]
codes = [r[0] for r in q("SELECT ws.strong FROM word_strong ws JOIN word_registry w ON w.id=ws.word_id WHERE w.word=? "
                         "AND ws.deleted=0", reg)]
via_codes = {r[0] for r in q("SELECT id FROM verse_lexical WHERE deleted=0 AND strong IN (SELECT value FROM json_each(?))",
                             json.dumps(codes))}
o = run(Word=reg)
surf = {r[0] for r in q("SELECT id FROM verse_lexical WHERE deleted=0 AND lower(trim(surface))=lower(?)", reg)}
case("T5b", f"a registry word ({reg}): its occurrences by surface, not its word_strong codes' occurrences",
     in_scope(o) == surf and surf != via_codes, (reg, len(surf), len(via_codes)))
r5 = refused(Word="seekx")
case("T5c", "a word that is no surface is refused, naming the rule", r5 is not None and "cfg_behaviour_rule 119" in r5, r5)
o = run(Word="SEEKING")
case("T5d", "a word not in word_registry still enters by its surface (case aside)",
     in_scope(o) == {r[0] for r in q("SELECT id FROM verse_lexical WHERE deleted=0 AND lower(trim(surface))='seeking'")},
     o["counts"])

# ── T6 a Strong's entry lands in every subgroup of its surfaces (S5) ─────────────────────────────────────────────────
o = run(Strong="H2896A")
want = sorted({r[0] for r in q("SELECT g.subgroup_code FROM surface_subgroup s JOIN cluster_subgroup g ON "
                               "g.id=s.cluster_subgroup_id WHERE s.deleted=0 AND s.strong='H2896A'")})
case("T6", "-Strong H2896A: the selector names every subgroup its occurrences fall in", o["selectors"][0]["subgroups"] ==
     want and len(want) > 1, (o["selectors"][0]["subgroups"], want))

# ── T7 the home (B:120) ──────────────────────────────────────────────────────────────────────────────────────────────
r7 = {k: refused(**v) for k, v in {"qual_sel": {"Subgroup": "M18_good"},
                                   "qual_home": {"Cluster": "M18", "Home": "M18_good"},
                                   "t_home": {"Cluster": "M18", "Home": "T2"},
                                   "bad_home": {"Cluster": "M18", "Home": "Mzz"}}.items()}
case("T7", "refused: a qualifier group as a subgroup selector or a home, a T cluster as a home, an unknown home",
     all(r7.values()) and "qualifier" in r7["qual_sel"] and "qualifier" in r7["qual_home"] and
     "not an M cluster" in r7["t_home"] and "neither" in r7["bad_home"], r7)
o = run(Cluster="M18", Home="M18_desire")
hm = {x["subgroup"] for v in o["verses"] for x in v["occurrences"] if x["home"]}
case("T7b", "-Cluster M18 -Home M18_desire: only the desire occurrences are home, the rest of M18 in scope but not home",
     hm == {"M18_desire"} and o["home"] == ["M18_desire"] and o["counts"]["in_scope"] == 1510, (hm, o["counts"]))
o = run(Cluster="M18,T15")
case("T7c", "the home taken from the selectors: an M cluster named is home, a T cluster named is not", o["home"] == ["M18"],
     o["home"])

# ── T8 settlements (rule 122) ────────────────────────────────────────────────────────────────────────────────────────
dl, fv = sg_id("M18_delight"), sg_id("M18_favour")
occ = q("SELECT v.id, v.verse_id, v.strong, v.surface, vv.osisId FROM surface_subgroup s JOIN verse_lexical v ON "
        "v.strong=s.strong AND lower(trim(coalesce(v.surface,'')))=s.surface AND v.deleted=0 JOIN verse vv ON "
        "vv.id=v.verse_id WHERE s.deleted=0 AND s.cluster_subgroup_id=? ORDER BY v.id LIMIT 1", dl)[0]


def settle(sg, status="draft", sup=None, tag="subgroup-settlement"):
    cur = conn.execute("INSERT INTO ib_observation (cluster_code, cluster_subgroup_id, stage, tag, strong, obs_text, "
                       "status, supersedes_observation_id, created_at) VALUES ('M18', ?, 'verse-reading', ?, ?, ?, ?, ?, "
                       "'2026-10-26T00:00:00Z')", (sg, tag, occ[2], "test settlement (#2295)", status, sup))
    conn.execute("INSERT INTO ib_node (observation_id, cluster_code, strong, verse_reference, surface, verse_lexical_id, "
                 "source_stage, seq, created_at) VALUES (?, 'M18', ?, ?, ?, ?, 'verse-reading', 1, '2026-10-26T00:00:00Z')",
                 (cur.lastrowid, occ[2], occ[4], occ[3], occ[0]))
    return cur.lastrowid


s1 = settle(fv)
a, b = run(Subgroup="M18_delight"), run(Subgroup="M18_favour")
shown = [x for v in b["verses"] for x in v["occurrences"] if x["id"] == occ[0]]
case("T8", "a current settlement moves its occurrence: out of M18_delight's scope, into M18_favour's, marked settled_by",
     occ[0] not in in_scope(a) and occ[0] in in_scope(b) and bool(shown) and shown[0].get("settled_by") == s1 and
     shown[0]["subgroup"] == "M18_favour", (occ[0], shown))
conn.execute("UPDATE ib_observation SET status='withdrawn' WHERE id=?", (s1,))
case("T8b", "a withdrawn settlement is not applied", occ[0] in in_scope(run(Subgroup="M18_delight")), s1)
conn.execute("UPDATE ib_observation SET status='draft' WHERE id=?", (s1,))
settle(fv, sup=s1, tag="key-statement")
case("T8c", "a superseded settlement is not applied (the resolver reads only the current one)",
     occ[0] in in_scope(run(Subgroup="M18_delight")), s1)
conn.rollback()

# ── T9 thread items: kind scope gives its stored verses (#2287) ──────────────────────────────────────────────────────
iid = q("SELECT i.id FROM escalation_thread_item i JOIN escalation e ON e.id=i.escalation_id WHERE e.alias='OT-01' AND "
        "i.item_no=3 AND e.version=(SELECT max(version) FROM escalation x WHERE x.id=e.id)")[0][0]
want = {r[0] for r in q("SELECT verse_id FROM escalation_thread_item_verse WHERE item_id=? AND deleted=0", iid)}
o = run(Item="OT-01.3")
case("T9", "-Item OT-01.3 (kind scope): its stored verses, not 'names no verse'",
     {v["verse_id"] for v in o["verses"]} == want and not o["not_resolved"], (len(want), o["not_resolved"]))
o = run(Thread="OT-01")
case("T9b", "-Thread OT-01: its scope items resolved; no scope item is reported as naming no verse",
     not any("'scope' names no verse" in x["reason"] for x in o["not_resolved"]), o["not_resolved"][:3])

# ── T10 claim through its observation sources; observation to occurrences ───────────────────────────────────────────
o = run(Claim="C-88")
obs = [r[0] for r in q("SELECT observation_id FROM narrative_claim_source s JOIN narrative_claim c ON c.id=s.claim_id "
                       "WHERE c.claim_ref='C-88' AND s.source_kind='observation'")]
ov = {r[0] for r in q("SELECT DISTINCT v.id FROM ib_node n JOIN verse v ON v.osisId=n.verse_reference AND v.deleted=0 "
                      "WHERE n.observation_id IN (SELECT value FROM json_each(?))", json.dumps(obs))}
case("T10", "-Claim C-88: its observation sources followed to their verses (#2287), none listed as not a verse",
     bool(ov) and ov <= {v["verse_id"] for v in o["verses"]} and
     not any("observation, not a verse" in x["reason"] for x in o["not_resolved"]), (len(ov), o["not_resolved"][:2]))
oid = q("SELECT observation_id FROM ib_node GROUP BY observation_id HAVING count(*) BETWEEN 3 AND 8 LIMIT 1")[0][0]
o = run(Observation=str(oid))
nodes = vs.node_occurrences(conn, "n.observation_id=?", (oid,))
case("T10b", "-Observation: each node placed on its one occurrence is in scope; its verses as before",
     {n[3] for n in nodes if n[3]} <= in_scope(o) and {v["verse_id"] for v in o["verses"]} == {n[1] for n in nodes},
     (oid, len(nodes)))
amb = q("SELECT n.id FROM ib_node n JOIN verse v ON v.osisId=n.verse_reference WHERE (SELECT count(*) FROM verse_lexical x "
        "WHERE x.deleted=0 AND x.verse_id=v.id AND x.strong=n.strong AND coalesce(x.surface,'')=coalesce(n.surface,''))>1 "
        "LIMIT 1")[0][0]
na = vs.node_occurrences(conn, "n.id=?", (amb,))
case("T10c", "a node that matches several occurrences is placed on none (rule 121), with its candidates listed",
     na[0][3] is None and len(na[0][4]) > 1, na)

# ── T11 the shape ────────────────────────────────────────────────────────────────────────────────────────────────────
o = run(Verse="Gen 3:6", Home="M18")
v = o["verses"][0]
n_lex = q("SELECT count(*) FROM verse_lexical WHERE deleted=0 AND verse_id=?", v["verse_id"])[0][0]
n_unclustered = q("SELECT count(*) FROM verse_lexical l WHERE l.deleted=0 AND l.verse_id=? AND NOT EXISTS (SELECT 1 FROM "
                  "cluster_strong c WHERE c.strong=l.strong AND c.deleted=0)", v["verse_id"])[0][0]
case("T11", "-Verse Gen 3:6: every clustered occurrence listed once, M words with subgroup, the rest as context; a "
     "verse selector puts no occurrence in scope", len(v["occurrences"]) + len(v["context"]) == n_lex - n_unclustered and
     all(x["subgroup"] for x in v["occurrences"]) and not in_scope(o) and
     any(x["home"] for x in v["occurrences"]), (len(v["occurrences"]), len(v["context"]), n_lex, n_unclustered))

# ── T12 callers: handler, collation, reading.open ────────────────────────────────────────────────────────────────────
h = hv.resolve(ctx("verse_scope.resolve", Label="t2295", Subgroup="M18_desire"))
f = json.loads(pathlib.Path(h.counts["path"]).read_text(encoding="utf-8")) if ok(h) else {}
case("T12", "Verse-Scope handler: writes the version 2 file to the setting's folder and reports home and occurrences",
     ok(h) and f.get("version") == 2 and "home: M18_desire" in h.message and
     pathlib.Path(h.counts["path"]).is_relative_to(S / "scope"), h.message)
h = hv.resolve(ctx("verse_scope.resolve", Label="t2295b", Cluster="M18", Home="T2"))
case("T12b", "the handler turns a home refusal into 'refused'", h.condition == "refused" and "not an M cluster" in h.message,
     h.message)
col = vc.collate(cfg, vs.normalise_request({"Subgroup": "M18_desire"}), ROOT)
case("T12c", "versecollate carries each verse's occurrences and the scope's version and home",
     col["scope"]["version"] == 2 and col["scope"]["home"] == ["M18_desire"] and
     all("occurrences" in r for r in col["verses"]), col["scope"]["home"])
eid = 2295
r = hr.open(ctx("reading.open", Label="t2295-desire", Escalation=str(eid), Home="M18", Subgroup="M18_desire",
                Objective="test of the occurrence-shaped scope (#2295)", By="Claude"))
row = q("SELECT request FROM reading WHERE label='t2295-desire'")
case("T12d", "reading.open: the home is the request's subgroup of the home cluster; the request is kept with it",
     ok(r) and bool(row) and json.loads(row[0][0])["home"] == ["M18_desire"], (r.message[:200], row))
r = hr.open(ctx("reading.open", Label="t2295-m18", Escalation=str(eid), Home="M18", Verse="Psa 37:4",
                Objective="test of the occurrence-shaped scope (#2295)", By="Claude"))
row = q("SELECT request FROM reading WHERE label='t2295-m18'")
case("T12e", "reading.open with no subgroup of the home: the home is the cluster",
     ok(r) and bool(row) and json.loads(row[0][0])["home"] == ["M18"], (r.message[:200], row))
r = hr.open(ctx("reading.open", Label="t2295-t", Escalation=str(eid), Home="T15", Verse="Psa 37:4",
                Objective="test of the occurrence-shaped scope (#2295)", By="Claude"))
case("T12f", "reading.open refuses a T cluster as the home (B:120), writing nothing",
     not ok(r) and "not an M cluster" in r.message and not q("SELECT 1 FROM reading WHERE label='t2295-t'"), r.message)

# ── T13 the migration and the registry ───────────────────────────────────────────────────────────────────────────────
rules = dict(q("SELECT rule_key, enforcement_status FROM cfg_behaviour_rule WHERE rule_key IN "
               "('scope-enters-through-surface', 'scope-home-and-multiplicity')"))
case("T13", "migration: dry run, apply, re-run writes nothing; B:119 enforced, B:120 partially",
     "DRY RUN" in mo[0] and "applied" in mo[1] and mo[2].startswith("0 write") and
     rules == {"scope-enters-through-surface": "mechanically_enforced",
               "scope-home-and-multiplicity": "partially_enforced"}, (mo, rules))
live = sqlite3.connect(f"file:{(ROOT / 'iba/app/db/iba.db').as_posix()}?mode=ro", uri=True)
live.row_factory = sqlite3.Row
AP = ROOT / "iba/app"
checks = {"scope_gaps": lambda x: cq.find_rule_scope_gaps(x, AP), "hedge": cq.find_hedge_phrases_in_active_config,
          "orphan": lambda x: cq.find_orphan_configs(x, AP), "no_ps": cq.find_steps_without_ps_script}
new = {k: [x for x in fn(conn) if x not in fn(live)] for k, fn in checks.items()}
case("T13b", "validate checks on the copy: no new finding; live untouched (its B:119 still buildable_not_built)",
     not any(new.values()) and live.execute("SELECT enforcement_status FROM cfg_behaviour_rule WHERE "
                                            "rule_key='scope-enters-through-surface'").fetchone()[0] == "buildable_not_built",
     new)

out = S / "results.md"
out.write_text("| case | what | result | evidence |\n|---|---|---|---|\n" +
               "\n".join(f"| {a} | {b} | {r_} | {e} |" for a, b, r_, e in results) + "\n", encoding="utf-8")
print(f"{sum(r_[2] == 'PASS' for r_ in results)} of {len(results)} pass -> {out}")
