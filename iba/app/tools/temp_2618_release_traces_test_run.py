"""temp_2618_release_traces_test_run.py -- escalation #2618: a deleted observation releases the traces other observations hold to it.

Runs on a COPY of iba.db (dbsnapshot.copy_db of live into <scratch dir>), never the live database. Each case builds its own observations
through observationrecord on the copy, deletes or merges one, and reads the nodes back:
  R1 a plain delete drops a live trace another observation holds to it, logged on the holder with the reason
  R2 a merge moves the trace to the observation merged into
  R3 a holder that already traces the target keeps one trace (the old one is dropped, not duplicated)
  R4 a delete with two targets moves the trace to the first and adds a trace to the second
  R5 the holder's own word nodes are untouched
  R6 the evidence check finds no dead trace on the holders (collectionvalidate / readcommands use the same join)
  R7 the 3.1 path: layerinner's existing delete calls soft_delete_observation, so it releases traces (code read)
Usage: python iba/app/tools/temp_2618_release_traces_test_run.py <scratch dir>. Prints PASS/FAIL per case.
"""
import inspect
import pathlib
import sys
import time

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402
from iba.app.lib import layerinner  # noqa: E402

LIVE = ROOT / "iba" / "app" / "db" / "iba.db"
RESULTS = []


def case(code, what, ok, detail=""):
    RESULTS.append((code, what, bool(ok), detail))
    print(f"| {code} | {what} | {'PASS' if ok else 'FAIL'} | {detail} |")


def main(scratch):
    t0 = time.monotonic()
    S = pathlib.Path(scratch) / "t2618run"
    S.mkdir(parents=True, exist_ok=True)
    for f in S.glob("iba.db*"):     # a fresh copy each run
        f.unlink()
    db = copy_db(S / "iba.db", LIVE)
    if pathlib.Path(db).resolve() == LIVE.resolve():
        sys.exit("refused: this test runs on a copy, never the live database")
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    vl = conn.execute("SELECT id, verse_ref FROM verse_lexical LIMIT 1").fetchone() if conn.execute(
        "SELECT 1 FROM pragma_table_info('verse_lexical') WHERE name='verse_ref'").fetchone() else conn.execute("SELECT id FROM verse_lexical LIMIT 1").fetchone()
    vlid = vl[0]

    def obs(text):
        oid = conn.execute("INSERT INTO ib_observation (stage, tag, obs_text, status, deleted, created_at, updated_at) VALUES "
                           "('layer-3', 'statement', ?, 'draft', 0, datetime('now'), datetime('now'))", (text,)).lastrowid
        conn.execute("INSERT INTO ib_node (observation_id, verse_lexical_id, verse_reference, source_stage, seq, created_at) VALUES (?,?,'Gen 1:1','layer-3',1,datetime('now'))", (oid, vlid))
        return oid

    def trace(holder, target):
        seq = conn.execute("SELECT COALESCE(MAX(seq), 0) + 1 FROM ib_node WHERE observation_id=?", (holder,)).fetchone()[0]
        return conn.execute("INSERT INTO ib_node (observation_id, traced_observation_id, source_stage, seq, created_at) VALUES (?,?,'layer-3',?,datetime('now'))",
                            (holder, target, seq)).lastrowid

    def live_traces(holder):
        return sorted(r[0] for r in conn.execute("SELECT traced_observation_id FROM ib_node WHERE observation_id=? AND deleted=0 "
                                                 "AND traced_observation_id IS NOT NULL", (holder,)))

    # R1 drop
    a, h = obs("test 2618 R1 deleted"), obs("test 2618 R1 holder")
    n = trace(h, a)
    orec.soft_delete_observation(conn, a, "test: deleted at 3.1, restated", None, "T2618", "Claude")
    dropped = conn.execute("SELECT deleted FROM ib_node WHERE id=?", (n,)).fetchone()[0] == 1
    logged = conn.execute("SELECT count(*) FROM ib_observation_change WHERE observation_id=? AND node_id=? AND reason LIKE ?",
                          (h, n, f"traced observation {a} deleted%")).fetchone()[0]
    case("R1", "a plain delete drops the trace another observation holds, logged on the holder", dropped and logged and live_traces(h) == [], f"dropped {dropped}, logged {logged}")
    case("R5", "the holder's word node is untouched", conn.execute("SELECT count(*) FROM ib_node WHERE observation_id=? AND deleted=0 AND verse_lexical_id IS NOT NULL", (h,)).fetchone()[0] == 1)

    # R2 merge moves
    d, k, h2 = obs("test 2618 R2 same text"), obs("test 2618 R2 same text"), obs("test 2618 R2 holder")
    trace(h2, d)
    orec.merge_observation(conn, d, k, "test: the same description", None, "T2618", "Claude")
    case("R2", "a merge moves the trace to the observation merged into", live_traces(h2) == [k], f"traces {live_traces(h2)}")

    # R3 already traces the target
    d3, k3, h3 = obs("test 2618 R3 same"), obs("test 2618 R3 same"), obs("test 2618 R3 holder")
    trace(h3, d3)
    trace(h3, k3)
    orec.merge_observation(conn, d3, k3, "test: the same description", None, "T2618", "Claude")
    case("R3", "a holder already tracing the target keeps one trace", live_traces(h3) == [k3], f"traces {live_traces(h3)}")

    # R4 two targets
    d4, c1, c2, h4 = obs("test 2618 R4 deleted"), obs("test 2618 R4 c1"), obs("test 2618 R4 c2"), obs("test 2618 R4 holder")
    trace(h4, d4)
    orec.soft_delete_observation(conn, d4, "test: went into two", None, "T2618", "Claude", into=[c1, c2])
    case("R4", "a delete into two targets moves to the first and adds the second", live_traces(h4) == sorted([c1, c2]), f"traces {live_traces(h4)}")

    # R6 no dead trace on the holders
    dead = conn.execute("SELECT count(*) FROM ib_node n JOIN ib_observation t ON t.id=n.traced_observation_id WHERE n.deleted=0 AND t.deleted=1 "
                        "AND n.observation_id IN (?,?,?,?)", (h, h2, h3, h4)).fetchone()[0]
    case("R6", "no live trace on the holders points at a deleted observation", dead == 0, f"dead {dead}")

    # R7 the 3.1 path
    src = inspect.getsource(layerinner.record)
    case("R7", "the 3.1 existing delete goes through soft_delete_observation (so it releases traces)",
         'orec.soft_delete_observation(conn, oid, e["reason"].strip()' in src)
    conn.rollback()
    secs = round(time.monotonic() - t0, 1)
    n_ok = sum(1 for r in RESULTS if r[2])
    print(f"\n{n_ok} of {len(RESULTS)} pass ({secs} s)")
    return 0 if n_ok == len(RESULTS) else 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python iba/app/tools/temp_2618_release_traces_test_run.py <scratch dir>")
    sys.exit(main(sys.argv[1]))
