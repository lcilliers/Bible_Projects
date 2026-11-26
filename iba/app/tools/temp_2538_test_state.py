"""temp_2538_test_state.py -- the test state of the layered-reading suites, set on a COPY of iba.db (never a method of the app; #2538, BUILD.md 597).

The suites of the read commands (ReadWords, ReadSenses, ReadEnrichment, ReadStructure, ReadElements) and of the loop were written on a snapshot where their subgroup had
not yet reached the step under test. Live has moved on (every subgroup of thought is through 3.1 since 2026-11-26), so each suite puts its subgroup back, on its copy,
to "`step` not yet open": the observations written under the subgroup's rows of that step and every later step of the loop are removed through observationrecord
(nodes deleted, traces released, each change logged with the reason "test state on a copy") and those rows retired, so that the Read command opens the step again.
The researcher (2026-11-26): "Yes, fix them".
"""
import pathlib

LOOP = ["S1", "1.1", "1.2", "2.1", "3.1"]
LIVE = pathlib.Path(__file__).resolve().parents[3] / "iba" / "app" / "db" / "iba.db"
REASON = "test state on a copy"


def back_to(conn, cfg, name: str, sub: str, step: str, run_id: str = "TEST-STATE") -> str:
    """Put subgroup `sub` of collection `name` back to `step` not yet open, on the copy `conn` holds. Refuses the live database. Returns what it did."""
    from iba.app.lib import layerreading as lr, observationrecord as orec
    db = conn.execute("PRAGMA database_list").fetchone()[2]
    if pathlib.Path(db).resolve() == LIVE.resolve():
        raise SystemExit("refused: the test state is set on a copy, never the live database")
    cid, _ = lr.ci._collection(conn, name)
    gid = conn.execute("SELECT id FROM collection_subgroup WHERE collection_id=? AND lower(name)=lower(?) AND deleted=0", (cid, sub)).fetchone()
    if gid is None:
        raise SystemExit(f"no live subgroup {sub!r} in {name!r}")
    steps = LOOP[LOOP.index(step):]
    rows = conn.execute(f"SELECT id FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND deleted=0 AND state!='retired' "
                        f"AND step IN ({','.join('?' * len(steps))})", (cid, gid[0], *steps)).fetchall()
    n = 0
    for (lid,) in rows:
        for (oid,) in conn.execute("SELECT id FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{lid}:", f"layer:{lid};")).fetchall():
            for (nid,) in conn.execute("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0", (oid,)).fetchall():
                orec.delete_node(conn, nid, REASON, None, run_id, "Claude")
            orec.soft_delete_observation(conn, oid, REASON, None, run_id, "Claude")
            n += 1
        conn.execute("UPDATE collection_layer_item SET state='retired', validated=0, reason=? WHERE id=?", (REASON, lid))
    conn.commit()
    return f"{sub!r} put back to {step} not yet open on the copy ({len(rows)} rows retired, {n} observations removed)"


def in_loop(conn, cfg, name: str) -> bool:
    """True when a subgroup of the collection is still in its loop (the copy already holds a subgroup in flight)."""
    from iba.app.lib import layerloop
    return any(not g["complete"] for g in layerloop.progress(conn, cfg, name)["subgroups"])
