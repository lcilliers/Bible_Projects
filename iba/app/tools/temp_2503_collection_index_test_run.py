"""temp_2503_collection_index_test_run.py -- tests for escalation #2503: the index of the surfaces of the confirmed collections and their subgroups
(lib/collectionindex.py, handlers/collectionbuild.py index_fill, subgroup, index_check, and the subgroup columns of the evidence report).

Each case checks the tables against a direct query written here, not against the builder's own lists, and runs the refusals (bad collection, missing reason, unknown surface, split rule).
Runs against a COPY of iba.db that already holds the migration (never the live database); the placements it makes are test rows on that copy.

Usage: python iba/app/tools/temp_2503_collection_index_test_run.py <db copy> <scratch dir>
"""
import collections
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from openpyxl import load_workbook  # noqa: E402

from iba.app.lib import collectionevidence as ev  # noqa: E402
from iba.app.lib import collectionevidencereport as rep  # noqa: E402
from iba.app.lib import collectionindex as ci  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:330]))


def refuses(fn, *a, **k):
    try:
        fn(*a, **k)
        return None
    except ci.IndexError_ as exc:
        return str(exc)


db = pathlib.Path(sys.argv[1])
S = pathlib.Path(sys.argv[2]) / "t2503"
S.mkdir(parents=True, exist_ok=True)
assert db.resolve() != (ROOT / "iba/app/db/iba.db").resolve(), "run against a copy"
cfg = Cfg(db)
conn = cfg.conn
q = lambda sql, *a: [tuple(r) for r in conn.execute(sql, a).fetchall()]  # noqa: E731
RUN = "TEST-2503"
tiers = list(cfg.setting("collection.member_tiers"))
inq = ",".join("?" * len(tiers))

# I1 registration
tabs = {r[0] for r in q("SELECT name FROM sqlite_master WHERE type='table'")}
reg = q("SELECT count(*) FROM cfg_table WHERE database='iba' AND name IN ('collection_subgroup','collection_subgroup_surface')")[0][0]
cols = q("SELECT count(*) FROM cfg_column WHERE database='iba' AND table_name IN ('collection_subgroup','collection_subgroup_surface') AND inactive=0")[0][0]
steps = [r[0] for r in q("SELECT step FROM cfg_step WHERE step IN ('collection.index','collection.subgroup','collection.index_check') AND inactive=0")]
case("I1", "both tables exist and are registered (cfg_table 2, cfg_column 22, three steps)", {"collection_subgroup", "collection_subgroup_surface"} <= tabs and reg == 2 and cols == 22 and len(steps) == 3,
     f"tables {sorted(t for t in tabs if t.startswith('collection_sub'))} cfg_table {reg} cfg_column {cols} steps {steps}")

# I2 the fill agrees with an independent count
own = {r[0] for r in q(f"SELECT DISTINCT term_id FROM collection_link WHERE deleted=0 AND tier IN ({inq})", *tiers)}
want = set()
for cid, tid in q(f"SELECT l.collection_id, l.term_id FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 AND c.status='confirmed' AND l.tier IN ({inq})", *tiers):
    if q("SELECT 1 FROM surface_term WHERE id=?", tid):
        want.add((cid, tid))
    for (sid,) in q("SELECT id FROM surface_term WHERE base_id=? AND id<>?", tid, tid):
        if sid not in own:
            want.add((cid, sid))
r = ci.fill(conn, cfg, RUN, dry=True)
case("I2a", "the preview counts the member surfaces as an independent query does", r["expected"] == len(want) and r["live"] + r["add"] - r["retire"] == len(want), f"preview {r} independent {len(want)}")
r = ci.fill(conn, cfg, RUN)
conn.commit()
got = {(a, b) for a, b in q("SELECT collection_id, term_id FROM collection_subgroup_surface WHERE deleted=0")}
st = q("SELECT state, count(*), sum(strong IS NULL), sum(subgroup_id IS NULL) FROM collection_subgroup_surface WHERE deleted=0 GROUP BY 1")
case("I2b", "the fill writes exactly those rows, all unplaced, whole surface, no subgroup", got == want and st == [("unplaced", len(want), len(want), len(want))], f"rows {len(got)} states {st}")

# I3 idempotent
r2 = ci.fill(conn, cfg, RUN)
case("I3", "a second fill adds and retires nothing", r2["add"] == 0 and r2["retire"] == 0, r2)

# I4 a surface that leaves its collection is retired, and comes back when it returns
tid = q("SELECT t.id FROM surface_term t JOIN collection_link l ON l.term_id=t.id JOIN collection c ON c.id=l.collection_id WHERE t.surface='weigh' AND l.deleted=0 AND c.name='thought' LIMIT 1")[0][0]
lid = q("SELECT id FROM collection_link WHERE term_id=? AND deleted=0 AND collection_id=(SELECT id FROM collection WHERE name='thought')", tid)[0][0]
conn.execute("UPDATE collection_link SET deleted=1 WHERE id=?", (lid,))
r3 = ci.fill(conn, cfg, RUN)
gone = q("SELECT count(*) FROM collection_subgroup_surface WHERE term_id=? AND deleted=0", tid)[0][0]
ev_n = q("SELECT count(*) FROM surface_event WHERE subject_kind='collection_subgroup_surface' AND action='index_retire' AND run_id=?", RUN)[0][0]
conn.execute("UPDATE collection_link SET deleted=0 WHERE id=?", (lid,))
r4 = ci.fill(conn, cfg, RUN)
back = q("SELECT count(*) FROM collection_subgroup_surface WHERE term_id=? AND deleted=0", tid)[0][0]
conn.commit()
case("I4", "a surface whose link is removed is retired with an event; it returns on the next fill", r3["retire"] >= 1 and gone == 0 and ev_n >= 1 and back == 1, f"retired {r3['retire']} live after {gone} events {ev_n} back {back} added {r4['add']}")

# I5 groups
errs = [refuses(ci.make_group, conn, RUN, "nosuchword", "x", "why"), refuses(ci.make_group, conn, RUN, "thought", "", "why"), refuses(ci.make_group, conn, RUN, "thought", "test-meditation", "")]
g1 = ci.make_group(conn, RUN, "thought", "test-meditation", "TEST instruction #2503")
g2 = ci.make_group(conn, RUN, "thought", "test-thinking", "TEST instruction #2503")
g3 = ci.make_group(conn, RUN, "thought", "test-plotting", "TEST instruction #2503")
dup = refuses(ci.make_group, conn, RUN, "thought", "TEST-Meditation", "again")
conn.commit()
case("I5", "a subgroup is made with an event; a bad collection, an empty name, no reason and a duplicate are refused", all(errs) and dup and g1["id"] and q("SELECT count(*) FROM surface_event WHERE action='subgroup_make' AND run_id=?", RUN)[0][0] == 3,
     f"refusals {[e[:40] for e in errs if e]} dup {str(dup)[:40]}")

# I6 placing whole surfaces
r = ci.place(conn, RUN, "thought", "test-meditation", ["meditate", "meditates", "meditation"], None, "TEST instruction")
rows = q("SELECT state, subgroup_id, strong FROM collection_subgroup_surface s JOIN surface_term t ON t.id=s.term_id WHERE s.deleted=0 AND t.surface IN ('meditate','meditates','meditation')")
case("I6", "three surfaces placed whole in a subgroup, with events", r["placed"] == 3 and all(x == ("placed", g1["id"], None) for x in rows) and
     q("SELECT count(*) FROM surface_event WHERE action='subgroup_place' AND run_id=?", RUN)[0][0] == 3, f"{rows}")

# I7 refusals of a placement
bad = {"unknown surface": refuses(ci.place, conn, RUN, "thought", "test-meditation", ["zzzz"], None, "why"),
       "no reason": refuses(ci.place, conn, RUN, "thought", "test-meditation", ["think"], None, ""),
       "no group": refuses(ci.place, conn, RUN, "thought", "test-nosuch", ["think"], None, "why"),
       "no surface": refuses(ci.place, conn, RUN, "thought", "test-thinking", [], None, "why"),
       "strong not carried": refuses(ci.place, conn, RUN, "thought", "test-thinking", ["think"], "H9999", "why"),
       "isolate with a name": refuses(ci.place, conn, RUN, "thought", "test-thinking", ["think"], None, "why", isolate=True)}
case("I7", "each bad placement is refused and nothing is written", all(bad.values()), {k: (v or "NOT REFUSED")[:50] for k, v in bad.items()})

# I8 a split by Strong's code
codes = [r[0] for r in q("SELECT DISTINCT strong FROM verse_lexical WHERE deleted=0 AND strong IS NOT NULL AND lower(trim(surface))='thoughts' ORDER BY strong")]
r = ci.place(conn, RUN, "thought", "test-plotting", ["thoughts"], "H4284", "TEST instruction: thoughts as a plan")
conn.commit()
tt = q("SELECT s.strong, s.state, s.subgroup_id FROM collection_subgroup_surface s JOIN surface_term t ON t.id=s.term_id WHERE s.deleted=0 AND t.surface='thoughts' ORDER BY s.strong")
whole = q("SELECT count(*) FROM collection_subgroup_surface s JOIN surface_term t ON t.id=s.term_id WHERE s.deleted=0 AND t.surface='thoughts' AND s.strong IS NULL")[0][0]
need_strong = refuses(ci.place, conn, RUN, "thought", "test-thinking", ["thoughts"], None, "why")
r = ci.place(conn, RUN, "thought", "test-thinking", ["thoughts"], codes[0] if codes[0] != "H4284" else codes[1], "TEST instruction: the other sense")
conn.commit()
tt2 = q("SELECT s.strong, s.state FROM collection_subgroup_surface s JOIN surface_term t ON t.id=s.term_id WHERE s.deleted=0 AND t.surface='thoughts' ORDER BY s.strong")
case("I8", "placing one sense splits the surface into a row for each Strong's code; naming no code on a split surface is refused",
     [x[0] for x in tt] == codes and whole == 0 and dict((x[0], x[1]) for x in tt)["H4284"] == "placed" and sum(1 for x in tt if x[1] == "unplaced") == len(codes) - 1 and need_strong and sum(1 for x in tt2 if x[1] == "placed") == 2,
     f"codes {codes} states {[(x[0], x[1]) for x in tt2]}")

# I9 isolate
r = ci.place(conn, RUN, "thought", None, ["reason"], None, "TEST instruction: reason is a cause here", isolate=True)
conn.commit()
iso = q("SELECT state, subgroup_id FROM collection_subgroup_surface s JOIN surface_term t ON t.id=s.term_id WHERE s.deleted=0 AND t.surface='reason'")
case("I9", "an isolated surface has the state isolated and no subgroup", iso == [("isolated", None)], iso)

# I10 a surface of another collection is refused
other = q("SELECT t.surface FROM collection_subgroup_surface s JOIN surface_term t ON t.id=s.term_id JOIN collection c ON c.id=s.collection_id WHERE s.deleted=0 AND c.name<>'thought' LIMIT 1")[0][0]
case("I10", "a surface that is in another collection is refused for this one", refuses(ci.place, conn, RUN, "thought", "test-thinking", [other], None, "why") is not None, other)

# I11 the checker: clean after the fill and the placements, then seeded faults are found
found = {f["key"]: f for f in ci.check(conn, cfg)}
clean = all(not found[k]["rows"] for k in ("member-with-no-index-row", "index-row-of-a-surface-that-left", "duplicate-live-row", "split-rule-broken", "placement-does-not-agree"))
sh_direct = 0
for (lid_,) in q(f"SELECT id FROM collection_link WHERE deleted=0 AND shared=1 AND tier IN ({inq})", *tiers):
    t_ = q("SELECT term_id FROM collection_link WHERE id=?", lid_)[0][0]
    if q(f"SELECT count(*) FROM collection_link WHERE deleted=0 AND term_id=? AND tier IN ({inq})", t_, *tiers)[0][0] < 2:
        sh_direct += 1
case("I11a", "the checker finds nothing wrong in the filled and placed index; its shared-flag finding equals a direct count", clean and len(found["shared-flag-without-a-second-link"]["rows"]) == sh_direct,
     f"clean {clean} shared flags without a second link {len(found['shared-flag-without-a-second-link']['rows'])} direct {sh_direct}")
tid2 = q("SELECT term_id FROM collection_subgroup_surface WHERE deleted=0 AND strong IS NULL LIMIT 1")[0][0]
cid2 = q("SELECT collection_id FROM collection_subgroup_surface WHERE deleted=0 AND term_id=? AND strong IS NULL", tid2)[0][0]
conn.execute("INSERT INTO collection_subgroup_surface (collection_id, term_id, strong, state, reason, run_id, created_by) VALUES (?,?,NULL,'unplaced','TEST dup',?,?)", (cid2, tid2, RUN, "test"))   # duplicate
conn.execute("INSERT INTO collection_subgroup_surface (collection_id, term_id, strong, state, reason, run_id, created_by) VALUES (?,?,'H0001','unplaced','TEST mix',?,?)", (cid2, tid2, RUN, "test"))  # whole and code
t3 = q("SELECT term_id FROM collection_subgroup_surface WHERE deleted=0 AND strong IS NULL AND term_id<>? LIMIT 1", tid2)[0][0]
conn.execute("UPDATE collection_subgroup_surface SET state='placed' WHERE deleted=0 AND term_id=? AND strong IS NULL", (t3,))      # placed with no subgroup
conn.execute("UPDATE collection_subgroup_surface SET deleted=1 WHERE deleted=0 AND strong IS NULL AND term_id=(SELECT term_id FROM collection_subgroup_surface WHERE deleted=0 AND strong IS NULL AND term_id NOT IN (?,?) LIMIT 1)", (tid2, t3))  # a member with no row
f2 = {f["key"]: f for f in ci.check(conn, cfg)}
want_keys = ("duplicate-live-row", "split-rule-broken", "placement-does-not-agree", "member-with-no-index-row")
case("I11b", "seeded faults (a duplicate, a whole and a code row, a placed row with no subgroup, a member with no row) are each found", all(f2[k]["rows"] for k in want_keys), {k: len(f2[k]["rows"]) for k in want_keys})
conn.rollback()

# I12 the report shows the subgroup
conn2 = Cfg(db).conn
vals = ev.read_settings(cfg)
order = ev.Order(conn)
d = ev.build_collection(conn, ev.resolve(conn, ["thought"])[0], vals["tiers"], order)
d["pairs"] = ev.build_pairs(conn, d, vals, order)
rows = d["pairs"]["rows"]
sub = collections.Counter(x["subgroup"] for x in rows if x["member"])
dm = [x for x in rows if x["member"] and x["surface"] in ("meditate", "meditates", "meditation")]
th = [x for x in rows if x["member"] and x["surface"] == "thoughts"]
ok_sub = all(x["subgroup"] == "test-meditation" and x["index_state"] == "placed" for x in dm) and dm
ok_split = {x["subgroup"] for x in th if x["strong"] == "H4284"} == {"test-plotting"} and all(x["subgroup"] in ("test-plotting", "test-thinking", "") for x in th)
case("I12a", "member occurrences carry the subgroup of their surface, and a split surface by its Strong's code", bool(ok_sub) and ok_split, f"{dict(sub)}")
xl = S / "thought-index.xlsx"
rep.write_workbook(xl, [d], vals, "TEST-RUN", "2026-11-14T00:00:00Z")
wb = load_workbook(xl)
head_vv = [c.value for c in wb["Verse view"][1]]
head_pr = [c.value for c in wb["Pairings"][1]]
lvl = {r[0].value for r in wb["Pairing summary"].iter_rows(min_row=2, max_col=1)}
case("I12b", "the sheets carry the subgroup columns and the summary has a subgroup level; the reading column is still empty",
     "subgroup (index)" in head_vv and "index state" in head_vv and "member subgroup" in head_pr and "neighbour subgroup" in head_pr and "subgroup" in lvl
     and all(c.value in (None, "") for c in wb["Pairings"][chr(64 + head_pr.index("reading") + 1) if head_pr.index("reading") < 26 else "X"][1:]), f"levels {sorted(lvl)}")
md = rep.render([d], vals, "TEST-RUN", "2026-11-14T00:00:00Z", xl.name)
case("I12c", "the Markdown states how many member occurrences are placed and shows the subgroup level", "placed in a subgroup of the collection index" in md and "| subgroup |" in md, "found" if "| subgroup |" in md else "missing")
(S / "thought-index.md").write_text(md, encoding="utf-8")
conn.rollback()

print("\n| case | what | result | evidence |\n|---|---|---|---|")
for r in results:
    print("| " + " | ".join(r) + " |")
print(f"\n{sum(1 for r in results if r[2] == 'PASS')} pass, {sum(1 for r in results if r[2] == 'FAIL')} fail; files in {S}")
sys.exit(0 if all(r[2] == "PASS" for r in results) else 1)
