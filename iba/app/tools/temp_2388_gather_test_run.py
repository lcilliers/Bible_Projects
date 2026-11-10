"""temp_2388_gather_test_run.py -- tests for Collection-Build -Action Gather (escalation #2388): lib/collectionbuild.gather on a scratch COPY of iba.db,
never the live database. Usage: python iba/app/tools/temp_2388_gather_test_run.py <scratch dir>"""
import pathlib
import shutil
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import collectionbuild as cb  # noqa: E402

S = pathlib.Path(sys.argv[1])
S.mkdir(parents=True, exist_ok=True)
copy = S / "iba_gather_copy.db"
src = sqlite3.connect(f"file:{ROOT / 'iba/app/db/iba.db'}?mode=ro", uri=True)
dst = sqlite3.connect(copy)
src.backup(dst)
src.close()
c = dst
res = []


def case(cid, desc, ok_, ev=""):
    res.append((cid, desc, "PASS" if ok_ else "FAIL", str(ev).replace("|", "/")[:200]))


def refused(*a, **k):
    try:
        cb.gather(c, "T", *a, **k)
    except cb.CollectionError as e:
        return str(e)
    return None


w = [r[0] for r in c.execute("SELECT surface FROM surface_term WHERE deleted=0 AND collection_state='untouched' AND form='word' ORDER BY id LIMIT 4")]
placed = c.execute("SELECT surface FROM surface_term WHERE deleted=0 AND collection_state='placed' LIMIT 1").fetchone()[0]
n0 = [c.execute(f"SELECT count(*) FROM {t}").fetchone()[0] for t in ("collection", "collection_link", "surface_event")]
plan0 = cb.plan(c)
case("G1", "an empty name is refused", bool(refused("", w, "r")), refused("", w, "r"))
case("G2", "no reason is refused", bool(refused("g", w, " ")), refused("g", w, " "))
case("G3", "no surface is refused", bool(refused("g", [" "], "r")))
case("G4", "an unknown word is refused and named", "zzznotaword" in (refused("g", ["zzznotaword"], "r") or ""), refused("g", ["zzznotaword"], "r"))
case("G5", "a word already in a collection is refused and named", placed in (refused("g", [placed, w[0]], "r") or ""), refused("g", [placed, w[0]], "r"))
case("G6", "a word named twice is refused", bool(refused("g", [w[0], w[0].upper()], "r")))
case("G7", "an existing collection name is refused", bool(refused("love", w, "r")))
r = cb.gather(c, "T", "g-dry", w, "r", dry=True)
case("G8", "a dry run writes nothing", r["members"] == 4 and [c.execute(f"SELECT count(*) FROM {t}").fetchone()[0] for t in ("collection", "collection_link", "surface_event")] == n0, r)
r = cb.gather(c, "T", "gathered-test", w, "the researcher: test (#2388)")
n1 = [c.execute(f"SELECT count(*) FROM {t}").fetchone()[0] for t in ("collection", "collection_link", "surface_event")]
case("G9", "one collection, one link per word and one event are written", n1 == [n0[0] + 1, n0[1] + 4, n0[2] + 1] and r["members"] == 4, n1)
case("G10", "every link is tier gathered with the reason, and no core link", c.execute("SELECT count(*) FROM collection_link WHERE collection_id=? AND tier='gathered' AND reason LIKE '%#2388%'", (r["collection"],)).fetchone()[0] == 4
     and c.execute("SELECT count(*) FROM collection_link WHERE collection_id=? AND tier='core'", (r["collection"],)).fetchone()[0] == 0)
case("G11", "the anchor is the first word and every word is placed", c.execute("SELECT t.surface FROM collection k JOIN surface_term t ON t.id=k.core_term_id WHERE k.id=?", (r["collection"],)).fetchone()[0] == w[0]
     and c.execute("SELECT count(*) FROM surface_term WHERE surface IN (%s) AND collection_state='placed'" % ",".join("?" * 4), w).fetchone()[0] == 4)
plan1 = cb.plan(c)
case("G12", "Links ignores the gathered collection (no core link made from its anchor)", (len(plan1["add"]), len(plan1["change"])) == (len(plan0["add"]), len(plan0["change"])), ((len(plan0["add"]), len(plan0["change"])), (len(plan1["add"]), len(plan1["change"]))))
case("G13", "a second Gather of the same words is refused (no longer untouched)", bool(refused("gathered-test-2", w, "r")))
print("| case | what | result | evidence |\n|---|---|---|---|")
for x in res:
    print("| " + " | ".join(x) + " |")
bad = [x for x in res if x[2] == "FAIL"]
print("\nALL PASS" if not bad else f"\n{len(bad)} FAIL", len(res))
c.close()
copy.unlink()
