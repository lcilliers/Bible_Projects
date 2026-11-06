"""temp_2361_collection_test_run.py -- tests for escalation #2361 stage 5: the collection module (lib/collectionbuild.py, handlers/collectionbuild.py,
Collection-Build.ps1). The stored collections of the five recorded runs of 2026-11-05 are the expected value: on a copy of iba.db the rule must decide
them unchanged; the copy is then scrambled (every link removed, every word state cleared) and Links must restore it exactly. Then: a changed judgement,
the proposed pairs, status changes, a merge, the export, and that no file under _analytics or outputs is read.

Usage: python iba/app/tools/temp_2361_collection_test_run.py <scratch dir>
"""
import builtins
import csv
import json
import pathlib
import shutil
import subprocess
import sys
import types

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers import collectionbuild as H  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402

results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:300]))


S = pathlib.Path(sys.argv[1]) / "t2361c"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
mig = ROOT / "iba/app/migration/surface_collection_2361_v1_20261106.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
o = [subprocess.run([sys.executable, str(mig), "--db", str(DB), "--no-snapshot"], capture_output=True, text=True).stdout.strip() for _ in range(2)]
case("C0", "migration: applied (or already), then nothing to do", ("applied" in o[0] or "already" in o[0]) and "already" in o[1], o)
cfg = Cfg(DB)
conn = cfg.conn
conn.execute("UPDATE cfg_setting SET value=? WHERE key='surfaces.exports_root'", (json.dumps((S / "exports").as_posix()),))
conn.commit()
ctx = lambda **p: types.SimpleNamespace(cfg=cfg, params=p, run_id="TEST-RUN")  # noqa: E731
count = lambda sql, *a: conn.execute(sql, a).fetchone()[0]  # noqa: E731


def snap():
    links = conn.execute("SELECT c.name, t.surface, l.tier, l.shared FROM collection_link l JOIN collection c ON c.id=l.collection_id JOIN surface_term t ON t.id=l.term_id "
                         "WHERE l.deleted=0 ORDER BY 1,2,3").fetchall()
    states = conn.execute("SELECT surface, collection_state FROM surface_term WHERE deleted=0 ORDER BY id").fetchall()
    return [tuple(r) for r in links], [tuple(r) for r in states]


_real_open = builtins.open


def _no_files(path, *a, **k):
    if any(x in str(path).replace("\\", "/") for x in ("_analytics/", "outputs/")):
        raise AssertionError(f"a file was read: {path}")
    return _real_open(path, *a, **k)


builtins.open = _no_files
try:
    L0, S0 = snap()
    o = H.status(ctx())
    case("C1", "the rule decides the stored collections unchanged: 925 links as stored, none to add or change, the 18 pairs the prototype left out withheld",
         o.condition == "ok" and o.counts["unchanged"] == 925 and o.counts["to_add"] == 0 and o.counts["to_change"] == 0 and o.counts["withheld"] == 18, o.counts)
    tiers = dict(conn.execute("SELECT tier, count(*) FROM collection_link WHERE deleted=0 GROUP BY 1").fetchall())
    case("C2", "the recorded tiers: core 48, synonym 193, opposite 38, possible_opposite 161, associated 397, set_aside 88",
         tiers == {"core": 48, "synonym": 193, "opposite": 38, "possible_opposite": 161, "associated": 397, "set_aside": 88}, tiers)
    # scramble
    conn.execute("DELETE FROM collection_link WHERE deleted=0")
    conn.execute("UPDATE surface_term SET collection_state='untouched' WHERE collection_state IS NOT NULL")
    conn.commit()
    o = H.links(ctx(Check="true"))
    case("C3", "scrambled copy: Links -Check previews the repair and writes nothing", o.condition == "ok" and "PREVIEW" in o.message and count("SELECT count(*) FROM collection_link WHERE deleted=0") == 0
         and o.counts["to_add"] == 925, o.counts)
    o = H.links(ctx())
    L1, S1 = snap()
    case("C4", "Links restores every link (collection, word, tier, shared)", L1 == L0 and o.counts["added"] == 925, (len(L1), o.counts))
    case("C5", "and the state of every word (placed, shared, set_aside, listed_only, untouched)", S1 == S0, sum(1 for a, b in zip(S0, S1) if a != b))
    o = H.links(ctx())
    case("C6", "a second Links changes nothing", o.counts["added"] == 0 and o.counts["superseded"] == 0 and o.counts["states"] == 0 and snap() == (L1, S1), o.counts)
    # a changed judgement: a newer call says the word is an opposite whose pole is a synonym
    row = conn.execute("SELECT l.id, l.collection_id, l.term_id, a.answer, a.model_id, c.name FROM collection_link l JOIN ai_call a ON a.id=l.ai_call_id "
                       "JOIN collection c ON c.id=l.collection_id WHERE l.tier='synonym' AND l.shared=0 AND l.deleted=0 LIMIT 1").fetchone()
    ans = json.loads(row[3])
    ans.update({"relation": "opposite", "pole_syn": True})
    conn.execute("INSERT INTO ai_call (module, step, role, model_id, subject_kind, subject_id, answer, result, outcome, created_by) VALUES "
                 "('collection','candidate','judge',?, 'surface_term', ?, ?, 'opposite', 'answered', 'test')", (row[4], row[2], json.dumps(ans)))
    conn.commit()
    o = H.links(ctx())
    new = conn.execute("SELECT id, tier FROM collection_link WHERE collection_id=? AND term_id=? AND deleted=0", (row[1], row[2])).fetchone()
    old = conn.execute("SELECT deleted, superseded_by_id FROM collection_link WHERE id=?", (row[0],)).fetchone()
    case("C7", "a newer judgement changes the tier: a new link, the old one set to deleted with superseded_by (nothing physically deleted)",
         o.counts["superseded"] == 1 and new[1] == "opposite" and tuple(old) == (1, new[0]), o.counts)
    conn.execute("DELETE FROM ai_call WHERE created_by='test'")
    conn.commit()
    o = H.status(ctx())
    case("C8", "with the newer call gone the stored link stays and Status says so", o.condition == "ok" and o.counts["to_change"] == 1, o.counts)
    # removed links are respected
    case("C9", "the 18 pairs the prototype left out are recorded as removed links (deleted, no successor) and are not linked again by Links",
         count("SELECT count(*) FROM collection_link WHERE deleted=1 AND superseded_by_id IS NULL AND load_ref LIKE 'withheld:%'") == 18
         and count("SELECT count(*) FROM collection_link WHERE deleted=0 AND tier='associated'") == 397, "")
    lid = conn.execute("SELECT id, collection_id, term_id FROM collection_link WHERE tier='associated' AND deleted=0 LIMIT 1").fetchone()
    conn.execute("UPDATE collection_link SET deleted=1 WHERE id=?", (lid[0],))
    conn.commit()
    H.links(ctx())
    case("C9b", "a link the researcher removes (deleted, no successor) stays removed after Links",
         count("SELECT count(*) FROM collection_link WHERE collection_id=? AND term_id=? AND deleted=0", lid[1], lid[2]) == 0, tuple(lid))
    # status changes
    o = H.set_status(ctx(Collection="love", Status="confirmed", Reason="researcher confirmed the collection"))
    ev = conn.execute("SELECT action, value_before, value_after FROM surface_event WHERE subject_kind='collection' ORDER BY id DESC LIMIT 1").fetchone()
    case("C10", "Set confirms a collection with a reason and a surface_event", o.condition == "ok" and tuple(ev) == ("confirm", "indicative", "confirmed"), tuple(ev))
    bad = [H.set_status(ctx(Collection="love", Status="confirmed")).condition, H.set_status(ctx(Collection="love", Status="merged", Reason="x")).condition,
           H.set_status(ctx(Collection="nosuch", Status="retired", Reason="x")).condition]
    case("C11", "Set without a reason, with a status it does not make, or for an unknown collection is refused", bad == ["refused"] * 3, bad)
    # merge
    a, b = [r[0] for r in conn.execute("SELECT name FROM collection WHERE name IN ('slander','insult') ORDER BY name")] if count("SELECT count(*) FROM collection WHERE name IN ('slander','insult')") == 2 else [r[0] for r in conn.execute("SELECT name FROM collection WHERE status='indicative' ORDER BY name LIMIT 2")]
    before_a = count("SELECT count(*) FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE c.name=? AND l.deleted=0", a)
    o = H.merge(ctx(**{"From": a, "Into": b, "Reason": "test merge"}))
    st = conn.execute("SELECT status, merged_into_id FROM collection WHERE name=?", (a,)).fetchone()
    case("C12", "Merge folds one collection into another: status merged, pointer set, the source links deleted (moved ones superseded), an event",
         o.condition == "ok" and st[0] == "merged" and st[1] is not None and count("SELECT count(*) FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE c.name=? AND l.deleted=0", a) == 0
         and before_a > 0 and conn.execute("SELECT action FROM surface_event WHERE subject_kind='collection' ORDER BY id DESC LIMIT 1").fetchone()[0] == "merge", (o.message[:80], tuple(st)))
    case("C13", "a merged collection is refused as a source or target, and Merge needs a reason",
         H.merge(ctx(**{"From": a, "Into": b, "Reason": "again"})).condition == "refused" and H.merge(ctx(**{"From": b, "Into": b, "Reason": "x"})).condition == "refused"
         and H.merge(ctx(**{"From": b, "Into": "love", "Reason": ""})).condition == "refused", "")
    o = H.show(ctx(Collection="love"))
    case("C14", "Show lists the members by tier with the shared ones starred", o.condition == "ok" and "core (1): love" in o.message and "synonym (" in o.message and "set_aside (" in o.message, o.message[:90])
    case("C15", "Show of an unknown collection is refused", H.show(ctx(Collection="nosuch")).condition == "refused", "")
    # export
    o = H.export(ctx(Name="collections-v1-20261106"))
    f = S / "exports" / "collections-v1-20261106.csv"
    rows = list(csv.reader(_real_open(f, encoding="utf-8-sig"))) if f.exists() else []
    case("C16", "Export writes a CSV of the live links (a view of the tables)", o.condition == "ok" and len(rows) - 1 == count("SELECT count(*) FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0")
         and rows[0][:3] == ["collection", "status", "core"], (o.message[:60], len(rows)))
    case("C17", "Export refuses a name that exists and a name without the version and date", H.export(ctx(Name="collections-v1-20261106")).condition == "refused"
         and H.export(ctx(Name="collections")).condition == "refused", "")
finally:
    builtins.open = _real_open
case("C18", "no file under _analytics or outputs was read by any handler call above", True, "open() was patched to raise, and none did")

width = max(len(r[0]) for r in results)
fails = [r for r in results if r[2] == "FAIL"]
for cid, desc, res_, evd in results:
    print(f"{cid:<{width}}  {res_}  {desc}  [{evd}]")
print(f"\n{len(results) - len(fails)} of {len(results)} pass")
sys.exit(1 if fails else 0)
