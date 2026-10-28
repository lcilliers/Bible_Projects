"""temp_2326_surface_migration_test_run.py -- escalation #2326 test plan, on a COPY of the live iba.db (never the live DB): the surface of

a code in a multi-code span (verse_lexical.surface set to the code's own STEP gloss where the untagged English before the span is exactly

that gloss), the build rule (lexical.build_for_verse) and the migration over the rows already built. Real case: Gen 43:27 (H5750 is

'still', H2416A stays 'alive'). Synthetic bad inputs: a multi-word gloss ('to be ashamed') must not take the word 'be'; a particle never

takes a word; a code whose gloss is the span's word keeps it. Usage: python iba/app/tools/temp_2326_surface_migration_test_run.py <scratch dir>.

Prints PASS/FAIL per case."""

import pathlib

import shutil

import sqlite3

import subprocess

import sys



ROOT = pathlib.Path(__file__).resolve().parents[3]

sys.path.insert(0, str(ROOT))

from iba.app.lib.dbsnapshot import copy_db  # noqa: E402

from iba.app.lib import lexical  # noqa: E402



S = pathlib.Path(sys.argv[1]) / "t2326run"

if S.exists():

    shutil.rmtree(S)

S.mkdir(parents=True)

_pre = ROOT / "backups/iba-pre-2326-surface-20261028.db"                 # the database before the migration (backup API copy)

DB = copy_db(S / "iba.db", _pre if _pre.exists() else ROOT / "iba/app/db/iba.db")

for _m in ("analysis_phase_1_2320_v4_20261028.py",):               # the rules the build reads from config (settings the copy of the older database lacks)
    _p = ROOT / "iba/app/migration" / _m
    _p = _p if _p.exists() else ROOT / "iba/app/migration/archive" / _m
    subprocess.run([sys.executable, str(_p), "--db", str(DB)], capture_output=True, text=True, check=True,
                   env={**__import__("os").environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"})
import json as _json
RULE = _json.loads(sqlite3.connect(DB).execute("SELECT value FROM cfg_setting WHERE key='lexical.span_surface'").fetchone()[0])
MIG = ROOT / "iba/app/migration/verse_lexical_multi_code_span_surface_2326_v1_20261028.py"

MIG = MIG if MIG.exists() else ROOT / "iba/app/migration/archive" / MIG.name

res = []





def case(cid, desc, ok, ev=""):

    ok = bool(ok)

    res.append(ok)

    print(f"{cid} {'PASS' if ok else 'FAIL'} {desc}" + ("" if ok else f"  -- {str(ev)[:900]}"), flush=True)





def sh(*a):

    r = subprocess.run([sys.executable, str(MIG), "--db", str(DB), *a], capture_output=True, text=True,

                       env={**__import__("os").environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"})

    return (r.stdout or r.stderr).strip()





conn = sqlite3.connect(DB)

conn.row_factory = sqlite3.Row





def q(sql, *a):

    return conn.execute(sql, a).fetchall()





vid = q("SELECT id FROM verse WHERE osisId='Gen.43.27'")[0][0]

vl = lambda strong: q("SELECT id, surface FROM verse_lexical WHERE verse_id=? AND strong=? AND deleted=0", vid, strong)[0]

spans = [dict(r) for r in q("SELECT id, position, surface, strong_variant FROM span WHERE verse_id=? AND deleted=0 ORDER BY position", vid)]

# ── R: the rule ───────────────────────────────────────────────────────────────────────────────────

surf = lexical.span_code_surfaces(conn, vid, spans)

byid = {(vl_["id"]): s for (sid, o), s in surf.items() for vl_ in q("SELECT id FROM verse_lexical WHERE span_id=? AND code_ordinal=? AND deleted=0", sid, o)}

case("R1", "the rule gives H5750 in Gen 43:27 the surface 'still' and no other code of the verse a new one",

     byid == {vl("H5750")[0]: "still"}, byid)

case("R2", "H2416A (its gloss is the span's word) and the particles H9043, H9008 keep the span's word 'alive'",

     all(surf.get(k) is None for k in [(sp["id"], i) for sp in spans for i, c in enumerate(sp["strong_variant"].split()) if c in ("H2416A", "H9043", "H9008")]))

case("R3", "a multi-word gloss never takes one of its words: 'to be ashamed' (H0954) is not 'be' ('be put to shame')",

     lexical.gloss_alternatives("to be ashamed", RULE) == set() and lexical.gloss_alternatives("about/through/for", RULE) == {"about", "through", "for"}

     and lexical.gloss_alternatives("to provoke", RULE) == {"provoke"} and lexical.gloss_alternatives("peace: well-being", RULE) == {"peace", "well-being"})

bosh = q("SELECT vl.id, vl.surface, v.id AS vid FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.strong='H0954' AND vl.deleted=0 "

         "AND v.text LIKE '%be put to shame%' LIMIT 1")

if bosh:

    sp2 = [dict(r) for r in q("SELECT id, position, surface, strong_variant FROM span WHERE verse_id=? AND deleted=0", bosh[0]["vid"])]

    case("R4", "real case: H0954 in a verse with 'be put to shame' keeps the span's word",

         bosh[0]["id"] not in {r["id"] for (sid, o), s in lexical.span_code_surfaces(conn, bosh[0]["vid"], sp2).items()

                               for r in q("SELECT id FROM verse_lexical WHERE span_id=? AND code_ordinal=? AND deleted=0", sid, o)})

else:

    case("R4", "(no verse with 'be put to shame' found)", True)

# ── M: the migration on the copy ──────────────────────────────────────────────────────────────────

before = {r["id"]: r["surface"] for r in q("SELECT id, surface FROM verse_lexical")}

dry = sh("--dry-run")

after_dry = {r["id"]: r["surface"] for r in q("SELECT id, surface FROM verse_lexical")}

case("M1", "the dry run says how many it would change and writes nothing", dry.startswith("DRY RUN") and before == after_dry, dry)

n_planned = int(dry.split("--")[1].split("occurrence")[0].strip())

n_nodes_before = q("SELECT count(*) FROM ib_observation_change WHERE column_name='surface'")[0][0]

out = sh()

case("M2", "the apply changes the planned occurrences and reports nodes, strand hits and the held ones",

     "changed" in out and f"{n_planned} occurrence(s) changed" in out, out)

now = {r["id"]: r["surface"] for r in q("SELECT id, surface FROM verse_lexical")}

changed = [i for i in before if before[i] != now[i]]

case("M3", "exactly the planned rows changed and no id was added or removed (identity-stable)",

     len(changed) == n_planned and set(before) == set(now), (len(changed), n_planned))

case("M4", "Gen 43:27: H5750 is 'still', H2416A stays 'alive'", vl("H5750")[1] == "still" and vl("H2416A")[1] == "alive", (vl("H5750"), vl("H2416A")))

held = [l.split("\t") for l in (DB.with_suffix(".surface-changes.tsv")).read_text(encoding="utf-8").split("\n") if l.startswith("HELD")]

case("M5", "the M-coded rows whose new (code, surface) pair is not in surface_subgroup are held, unchanged, and listed",

     len(held) >= 1 and all(before[int(h[1])] == now[int(h[1])] for h in held), held[:3])

mc = {r[0] for r in q("SELECT DISTINCT strong FROM cluster_strong WHERE deleted=0 AND cluster_code LIKE 'M%'")}

pairs = {(r[0], (r[1] or "").lower()) for r in q("SELECT strong, surface FROM surface_subgroup WHERE deleted=0")}

bad = [i for i in changed if q("SELECT strong FROM verse_lexical WHERE id=?", i)[0][0] in mc

       and (q("SELECT strong FROM verse_lexical WHERE id=?", i)[0][0], now[i].lower()) not in pairs]

case("M6", "no changed row leaves an M-coded (code, surface) pair unallocated", not bad, bad[:5])

nodes_h5750 = q("SELECT n.id, n.surface FROM ib_node n WHERE n.verse_lexical_id=?", vl("H5750")[0])

case("M7", "the nodes on a changed occurrence follow, each change kept in ib_observation_change with its reason",

     all(n["surface"] == "still" for n in nodes_h5750)

     and q("SELECT count(*) FROM ib_observation_change WHERE column_name='surface'")[0][0] > n_nodes_before

     and all(q("SELECT count(*) FROM ib_observation_change WHERE node_id=? AND column_name='surface' AND new_value='still'", n["id"])[0][0] >= 1

             for n in nodes_h5750), [tuple(n) for n in nodes_h5750])

case("M8", "a second run is refused as already applied", sh().startswith("already applied"))

# ── B: the build agrees with the migration ────────────────────────────────────────────────────────

c = lexical.build_for_verse(conn, vid)

case("B1", "the build of Gen 43:27 after the migration finds nothing to update (it writes the same surface)", c["updated"] == 0 and c["inserted"] == 0, c)

conn.rollback()

conn.execute("UPDATE verse_lexical SET surface='alive' WHERE id=?", (vl("H5750")[0],))

c2 = lexical.build_for_verse(conn, vid)

case("B2", "a row built the old way is corrected by the build itself (the root fix, not only the migration)",

     c2["updated"] >= 1 and vl("H5750")[1] == "still", c2)

print(f"\n{sum(res)} of {len(res)} cases pass")

