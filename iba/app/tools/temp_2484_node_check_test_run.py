"""temp_2484_node_check_test_run.py -- test plan of lib/nodecheck.py (escalation #2484, behaviour rule development.test-plan-per-module-utility).

Runs on a COPY of iba.db (made with the backup API), never the live database: bad rows are planted in the copy and each check must find exactly them. Then the
read-only property (the run works on a read-only connection and no table changes) and the agreement with figures counted independently.
    python -m iba.app.tools.temp_2484_node_check_test_run"""
import hashlib
import pathlib
import sqlite3
import sys
import tempfile

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.lib import dbsnapshot  # noqa: E402
from iba.app.lib import nodecheck as nck  # noqa: E402

RESULTS = []


def case(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""))


def checksum(c):
    h = hashlib.sha1()
    for t in ("ib_node", "ib_observation", "collection", "collection_link", "surface_term"):
        h.update(str(tuple(c.execute(f"SELECT count(*), coalesce(max(rowid),0), coalesce(sum(deleted),0) FROM {t}").fetchone())).encode())
    return h.hexdigest()


def main():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="nodecheck-"))
    db = tmp / "copy.db"
    dbsnapshot.copy_db(db)
    c = sqlite3.connect(str(db))
    c.row_factory = sqlite3.Row
    base = nck.run(c)
    bad = {r[0] for k, rows in base["findings"].items() if k.startswith("N-") for r in rows if r[0] is not None}
    donor = c.execute("SELECT * FROM ib_node WHERE deleted=0 AND verse_lexical_id IS NOT NULL AND collection_id IS NOT NULL AND role IS NOT NULL "
                      "AND id NOT IN (%s) LIMIT 1" % ",".join(map(str, sorted(bad)) or "0")).fetchone()
    case("T0 a clean donor node exists in the copy", donor is not None)
    tag = c.execute("SELECT tag FROM ib_observation WHERE deleted=0 LIMIT 1").fetchone()[0]
    cols = [r[1] for r in c.execute("PRAGMA table_info(ib_node)")]

    def new_obs(text, stage="reading", deleted=0):
        oid = c.execute("SELECT max(id)+1 FROM ib_observation").fetchone()[0]
        c.execute("INSERT INTO ib_observation (id, stage, tag, obs_text, status, created_at, deleted) VALUES (?,?,?,?,?,?,?)",
                  (oid, stage, tag, text, "draft", "2026-11-13T00:00:00Z", deleted))
        return oid

    def new_node(oid, **kw):
        d = {k: donor[k] for k in cols if k != "id"}
        d.update(observation_id=oid, deleted=0, seq=int(c.execute("SELECT coalesce(max(seq),0)+1 FROM ib_node WHERE observation_id=?", (oid,)).fetchone()[0]))
        d.update(kw)
        c.execute("INSERT INTO ib_node (%s) VALUES (%s)" % (",".join(d), ",".join("?" * len(d))), list(d.values()))
        return c.execute("SELECT last_insert_rowid()").fetchone()[0]

    words = c.execute("SELECT text FROM verse WHERE osisId=?", (donor["verse_reference"],)).fetchone()[0].split()
    text_ok = "An interpretive statement about the word and what it does here, in other words than the verse."
    ok_obs = new_obs(text_ok)
    n_ok = new_node(ok_obs)
    dup_obs = new_obs(text_ok)
    new_node(dup_obs)
    gone_obs = new_obs("deleted observation text", deleted=1)
    n_gone = new_node(gone_obs)
    nosurf_obs = new_obs("observation with a node without surface")
    n_nosurf = new_node(nosurf_obs, surface=None, verse_lexical_id=None, strong=None, morph_code=None, role=None)
    n_dup = new_node(ok_obs)
    n_badrole = new_node(new_obs("observation bad role"), role="foo")
    n_mis = new_node(new_obs("observation mismatch"), surface="zzzqqq")
    nocol_obs = new_obs("observation whose node has no collection")
    n_nocol = new_node(nocol_obs, collection_id=None)
    other = c.execute("SELECT id FROM collection WHERE deleted=0 AND status='confirmed' AND id<>? LIMIT 1", (donor["collection_id"],)).fetchone()[0]
    n_wrongcol = new_node(new_obs("observation wrong collection"), collection_id=other)
    copy_obs = new_obs(" ".join(words[:10]) if len(words) >= 10 else " ".join(words))
    new_node(copy_obs)
    lone_obs = new_obs("an observation with no node at all")
    c.commit()
    res = nck.run(c)
    f = res["findings"]
    ids = lambda k: {r[0] for r in f[k] if r[0] is not None}  # noqa: E731
    oids = lambda k: {r[1] for r in f[k]}  # noqa: E731
    node_hits = {r[0] for k, rows in f.items() if k.startswith("N-") for r in rows}
    case("T1 the planted clean node has no node finding", n_ok not in node_hits, f"node {n_ok}")
    case("T2 a node on a deleted observation is N-no-live-observation", n_gone in ids("N-no-live-observation"))
    case("T3 a node with no surface is N-no-surface, not N-no-strong or N-no-role",
         n_nosurf in ids("N-no-surface") and n_nosurf not in ids("N-no-strong") and n_nosurf not in ids("N-no-role"))
    case("T4 a node whose surface differs from its verse_lexical row is N-occurrence-mismatch", n_mis in ids("N-occurrence-mismatch"))
    case("T5 a second node with the same indexing columns is N-duplicate, the first is not", n_dup in ids("N-duplicate") and n_ok not in ids("N-duplicate"))
    case("T6 a role outside the enum is N-no-role", n_badrole in ids("N-no-role"))
    case("T7 a node with a collection that is not its surface's is N-collection-disagrees", n_wrongcol in ids("N-collection-disagrees"))
    case("T8 an in-scope collection-surface node with no collection is N-no-collection, derivable",
         any(r[0] == n_nocol and "derivable" in r[4] for r in f["N-no-collection"]))
    case("T9 an observation with no node is O-no-live-node", lone_obs in oids("O-no-live-node"))
    case("T10 an observation with the same text as another is O-duplicate-text, the first is not", dup_obs in oids("O-duplicate-text") and ok_obs not in oids("O-duplicate-text"))
    case("T11 an observation whose only node has no surface is O-not-tied", nosurf_obs in oids("O-not-tied"))
    case("T12 an observation copying the verse words is O-verse-copy (candidate)", copy_obs in oids("O-verse-copy"))
    case("T13 an observation none of whose nodes has a collection is O-no-collection", nocol_obs in oids("O-no-collection"))
    case("T14 every check has a result list and a count", set(res["counts"]) == {k for k, _, _ in nck.CHECKS} and all(res["counts"][k] == len(f[k]) for k in f))
    case("T15 nodes with and without a finding add up to the live nodes",
         res["totals"]["live nodes with a finding"] + res["totals"]["live nodes with no finding"] == res["totals"]["live nodes"])
    c.close()
    # the read-only property and the agreement with independent counts, on an unmodified copy
    fresh = tmp / "fresh.db"
    dbsnapshot.copy_db(fresh)
    ro = sqlite3.connect(f"file:{fresh.as_posix()}?mode=ro", uri=True)
    ro.row_factory = sqlite3.Row
    before = checksum(ro)
    r0 = nck.run(ro)
    case("T16 the checker runs on a read-only connection and no table changes", before == checksum(ro))
    one = lambda sql: ro.execute(sql).fetchone()[0]  # noqa: E731
    live = one("SELECT count(*) FROM ib_node WHERE deleted=0")
    case("T17 live nodes equal the count of the table", r0["totals"]["live nodes"] == live, str(live))
    unmapped = one("SELECT count(*) FROM ib_node WHERE deleted=0 AND collection_id IS NULL AND trim(coalesce(surface,''))<>''")
    case("T18 N-no-collection equals the nodes with a surface and no collection (independent count)", r0["counts"]["N-no-collection"] == unmapped, str(unmapped))
    case("T19 N-no-occurrence equals the nodes with no verse_lexical_id (independent count)",
         r0["counts"]["N-no-occurrence"] == one("SELECT count(*) FROM ib_node WHERE deleted=0 AND verse_lexical_id IS NULL"))
    case("T20 N-no-role equals the nodes with a surface and no role (independent count)",
         r0["counts"]["N-no-role"] == one("SELECT count(*) FROM ib_node WHERE deleted=0 AND trim(coalesce(surface,''))<>'' AND role IS NULL"))
    case("T21 O-no-live-node equals the live observations with no live node (independent count)",
         r0["counts"]["O-no-live-node"] == one("SELECT count(*) FROM ib_observation o WHERE deleted=0 AND NOT EXISTS "
                                               "(SELECT 1 FROM ib_node n WHERE n.observation_id=o.id AND n.deleted=0)"))
    case("T22 the report lists every check", all(k in "\n".join(nck.report_lines(r0, "TEST", "now")) for k, _, _ in nck.CHECKS))
    failed = [n for n, ok, _ in RESULTS if not ok]
    print(f"\n{len(RESULTS) - len(failed)} of {len(RESULTS)} pass")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
