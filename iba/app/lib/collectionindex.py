"""collectionindex.py -- the index of the surfaces of each collection and their subgroups (escalation #2503; design outputs/escalation/2463-collection-subgroup-index-design-v1-20261114.md).

Two tables. `collection_subgroup` is a group of surfaces inside one collection (a concept the researcher forms in the layer 1 reading: starting, weighing, meditation ...). `collection_subgroup_surface` is the index: one live
row for each member surface of each confirmed collection, with its subgroup and a state: unplaced (in the index, no group yet), placed, isolated (no inner-being role: bound to its partner or excluded).

The members are the surfaces of a collection by the one rule of the evidence report (lib/collectionevidence.py): a surface with a link of its own in a member tier is read by it, one without through its base term;
only confirmed collections. A row has strong NULL when it stands for the whole surface; a surface split between groups (one surface with two senses, such as `thoughts` as a plan and as a thought) has one row for each
Strong's code it carries in the verses and none for the whole surface. Nothing is guessed: the fill is mechanical, a placement is the researcher's instruction with a reason, and every change but the fill is a surface_event.
The tunable values are in cfg_setting (collection.member_tiers, collection.index_check_name, surfaces.exports_root); the code holds none.
"""
from __future__ import annotations

import collections

from . import collectionevidence as ev

NOW = "strftime('%Y-%m-%dT%H:%M:%SZ','now')"
BY = "collection-index"


class IndexError_(Exception):
    """A usage problem; routed as 'refused' and nothing is written."""


def member_tiers(cfg) -> list:
    t = cfg.setting("collection.member_tiers")
    if not t:
        raise IndexError_("cfg_setting collection.member_tiers is missing")
    return list(t)


def members(conn, tiers) -> tuple[dict, dict]:
    """(term id -> collection id, collection id -> name) of the confirmed collections, by the evidence report's rule. A term reached by two collections is kept with the lower collection id
    and listed by check() as a conflict."""
    terms, of_base = ev._terms(conn)
    own = ev._own_terms(conn, tiers)
    cols = {r[0]: r[1] for r in conn.execute("SELECT id, name FROM collection WHERE deleted=0 AND status='confirmed'")}
    reach, conflicts = {}, collections.defaultdict(set)
    for cid, tid in conn.execute(f"SELECT collection_id, term_id FROM collection_link WHERE deleted=0 AND tier IN ({','.join('?' * len(tiers))}) ORDER BY collection_id", list(tiers)):
        if cid not in cols:
            continue
        for sid in [s for s in of_base.get(tid, []) if s not in own] + ([tid] if tid in terms else []):
            if sid in reach and reach[sid] != cid:
                conflicts[sid].update((reach[sid], cid))
            reach.setdefault(sid, cid)
    return reach, cols, conflicts


def _collection(conn, name) -> tuple[int, str]:
    r = conn.execute("SELECT id, name FROM collection WHERE deleted=0 AND status='confirmed' AND lower(name)=?", ((name or "").strip().lower(),)).fetchone()
    if r is None:
        raise IndexError_(f"{name!r} is not a confirmed collection")
    return r[0], r[1]


def _event(conn, run_id, kind, sid, action, field, before, after, reason):
    conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) VALUES (?,?,?,?,?,?,?,?,?,?)",
                 (kind, sid, action, field, before, after, BY, reason, run_id, BY))


# ══ the fill ═════════════════════════════════════════════════════════════════════════════════════
def fill(conn, cfg, run_id: str, dry: bool = False) -> dict:
    """One live row (collection, term) for each member surface of a confirmed collection; a live row whose surface is no longer a member of that collection is retired (soft delete, with an event).
    A surface split by Strong's code keeps its rows while it stays a member. Idempotent."""
    reach, cols, _ = members(conn, member_tiers(cfg))
    expected = {(cid, tid) for tid, cid in reach.items()}
    live = collections.defaultdict(list)
    for rid, cid, tid, strong in conn.execute("SELECT id, collection_id, term_id, strong FROM collection_subgroup_surface WHERE deleted=0"):
        live[(cid, tid)].append((rid, strong))
    add = sorted(expected - set(live))
    retire = [(rid, key) for key, rows in live.items() if key not in expected for rid, _ in rows]
    out = {"expected": len(expected), "live": sum(len(v) for v in live.values()), "add": len(add), "retire": len(retire)}
    if dry:
        return out
    for cid, tid in add:
        conn.execute("INSERT INTO collection_subgroup_surface (collection_id, term_id, strong, subgroup_id, state, reason, run_id, created_by) VALUES (?,?,NULL,NULL,'unplaced','index fill',?,?)",
                     (cid, tid, run_id, BY))
    for rid, (cid, tid) in retire:
        conn.execute(f"UPDATE collection_subgroup_surface SET deleted=1, updated_at={NOW}, run_id=?, reason='the surface is no longer a member of this collection' WHERE id=?", (run_id, rid))
        _event(conn, run_id, "collection_subgroup_surface", rid, "index_retire", "deleted", "0", "1", f"collection {cols.get(cid, cid)}: the surface left the collection")
    return out


# ══ groups and placements (each on the researcher's instruction, with a reason) ═══════════════════
def make_group(conn, run_id: str, collection: str, name: str, reason: str, dry: bool = False) -> dict:
    cid, cname = _collection(conn, collection)
    name = (name or "").strip()
    if not name:
        raise IndexError_("-Name is required: the name of the subgroup")
    if not (reason or "").strip():
        raise IndexError_("-Reason is required: why the subgroup is made (the researcher's instruction, quoted, with the escalation id)")
    if conn.execute("SELECT 1 FROM collection_subgroup WHERE collection_id=? AND deleted=0 AND lower(name)=?", (cid, name.lower())).fetchone():
        raise IndexError_(f"collection {cname} already has a subgroup {name!r}")
    if dry:
        return {"collection": cname, "name": name, "id": None}
    gid = conn.execute("INSERT INTO collection_subgroup (collection_id, name, status, note, run_id, created_by) VALUES (?,?,'indicative',?,?,?)", (cid, name, reason.strip(), run_id, BY)).lastrowid
    _event(conn, run_id, "collection_subgroup", gid, "subgroup_make", None, None, name, reason.strip())
    return {"collection": cname, "name": name, "id": gid}


def _codes(conn, surface: str) -> list:
    return [r[0] for r in conn.execute("SELECT DISTINCT strong FROM verse_lexical WHERE deleted=0 AND strong IS NOT NULL AND lower(trim(surface))=? ORDER BY strong", (surface,))]


def place(conn, run_id: str, collection: str, group: str | None, surfaces: list, strong: str | None, reason: str, isolate: bool = False, dry: bool = False) -> dict:
    """Place surfaces of a collection in one of its subgroups (or isolate them: no inner-being role). With `strong` only that sense of the surface is placed; the surface is then split into one row for
    each Strong's code it carries in the verses (the other codes stay unplaced), as the design requires."""
    cid, cname = _collection(conn, collection)
    if not (reason or "").strip():
        raise IndexError_("-Reason is required: why (the researcher's instruction, quoted, with the escalation id)")
    gid = None
    if isolate:
        if group:
            raise IndexError_("-Isolate takes no -Name: an isolated surface is in no subgroup")
    else:
        g = conn.execute("SELECT id FROM collection_subgroup WHERE collection_id=? AND deleted=0 AND lower(name)=?", (cid, (group or "").strip().lower())).fetchone()
        if g is None:
            raise IndexError_(f"collection {cname} has no subgroup {group!r}: make it first (-Name with no -Surface)")
        gid = g[0]
    names = [s.strip().lower() for s in surfaces if s and s.strip()]
    if not names:
        raise IndexError_("-Surface is required: one or more surfaces of the collection, separated by a comma")
    done, plan = [], []
    for s in names:
        t = conn.execute("SELECT id FROM surface_term WHERE deleted=0 AND surface=?", (s,)).fetchone()
        rows = conn.execute("SELECT id, strong FROM collection_subgroup_surface WHERE deleted=0 AND collection_id=? AND term_id=?", (cid, t[0] if t else -1)).fetchall()
        if not rows:
            raise IndexError_(f"{s!r} is not in the index of collection {cname} (run Index to fill it, or the surface is not a member)")
        split = any(r[1] for r in rows)
        if strong:
            codes = _codes(conn, s)
            if strong not in codes:
                raise IndexError_(f"{s!r} has no occurrence with Strong's code {strong!r} (it carries {', '.join(codes) or 'none'})")
        elif split:
            raise IndexError_(f"{s!r} is split by Strong's code in collection {cname}: name the sense with -Strong")
        plan.append((s, t[0], rows, split))
    if dry:
        return {"collection": cname, "placed": len(plan), "group": group}
    for s, tid, rows, split in plan:
        if strong and not split:     # split the whole-surface row into one row for each code
            whole = rows[0][0]
            conn.execute(f"UPDATE collection_subgroup_surface SET deleted=1, updated_at={NOW}, run_id=?, reason='split by Strong code' WHERE id=?", (run_id, whole))
            for code in _codes(conn, s):
                conn.execute("INSERT INTO collection_subgroup_surface (collection_id, term_id, strong, subgroup_id, state, reason, run_id, created_by) VALUES (?,?,?,NULL,'unplaced','split by Strong code',?,?)",
                             (cid, tid, code, run_id, BY))
            _event(conn, run_id, "collection_subgroup_surface", whole, "subgroup_place", "strong", None, "split", f"{s}: split by Strong's code before placing {strong}")
        target = conn.execute("SELECT id, subgroup_id, state FROM collection_subgroup_surface WHERE deleted=0 AND collection_id=? AND term_id=? AND strong IS ?", (cid, tid, strong)).fetchone()
        state = "isolated" if isolate else "placed"
        conn.execute(f"UPDATE collection_subgroup_surface SET subgroup_id=?, state=?, reason=?, updated_at={NOW}, run_id=? WHERE id=?", (gid, state, reason.strip(), run_id, target[0]))
        _event(conn, run_id, "collection_subgroup_surface", target[0], "subgroup_isolate" if isolate else "subgroup_place", "subgroup_id", f"{target[2]}:{target[1]}", f"{state}:{gid}",
               f"{s}{' (' + strong + ')' if strong else ''}: {reason.strip()}")
        done.append(s)
    return {"collection": cname, "placed": len(done), "group": group}


# ══ the checker ══════════════════════════════════════════════════════════════════════════════════
def check(conn, cfg) -> list[dict]:
    """The findings, each {key, how, cols, rows}: a rule and the rows that break it. Read-only."""
    reach, cols, conflicts = members(conn, member_tiers(cfg))
    terms = {r[0]: r[1] for r in conn.execute("SELECT id, surface FROM surface_term")}
    expected = {(cid, tid) for tid, cid in reach.items()}
    live = conn.execute("SELECT id, collection_id, term_id, strong, subgroup_id, state FROM collection_subgroup_surface WHERE deleted=0").fetchall()
    groups = {r[0]: r for r in conn.execute("SELECT id, collection_id, name, deleted FROM collection_subgroup")}
    have = {(r[1], r[2]) for r in live}
    out = []

    def add(key, how, cols_, rows):
        out.append({"key": key, "how": how, "cols": cols_, "rows": rows})
    add("member-with-no-index-row", "a member surface of a confirmed collection with no live row in the index (run Index)", ["collection", "surface"],
        [[cols[c], terms.get(t)] for c, t in sorted(expected - have)])
    add("index-row-of-a-surface-that-left", "a live index row whose surface is no longer a member of that collection (run Index)", ["row", "collection", "surface"],
        [[r[0], cols.get(r[1], r[1]), terms.get(r[2])] for r in live if (r[1], r[2]) not in expected])
    add("surface-in-two-collections", "a surface reached by more than one confirmed collection (a surface is in exactly one, B:129)", ["surface", "collections"],
        [[terms.get(t), ", ".join(sorted(cols.get(c, str(c)) for c in cs))] for t, cs in sorted(conflicts.items(), key=lambda kv: terms.get(kv[0], ""))])
    seen = collections.Counter((r[1], r[2], r[3]) for r in live)
    add("duplicate-live-row", "two live rows for the same (collection, surface, Strong's code)", ["collection", "surface", "strong", "rows"],
        [[cols.get(k[0], k[0]), terms.get(k[1]), k[2], n] for k, n in seen.items() if n > 1])
    by_surface = collections.defaultdict(list)
    for r in live:
        by_surface[(r[1], r[2])].append(r)
    add("split-rule-broken", "a surface with a row for the whole surface and a row for a Strong's code (the rows are all whole or all by code)", ["collection", "surface", "rows"],
        [[cols.get(k[0], k[0]), terms.get(k[1]), len(v)] for k, v in by_surface.items() if any(x[3] for x in v) and any(not x[3] for x in v)])
    bad = []
    for r in live:
        g = groups.get(r[4]) if r[4] else None
        if r[5] == "placed" and (g is None or g[3] or g[1] != r[1]):
            bad.append([r[0], cols.get(r[1], r[1]), terms.get(r[2]), r[5], "the subgroup is missing, deleted or in another collection"])
        elif r[5] != "placed" and r[4] is not None:
            bad.append([r[0], cols.get(r[1], r[1]), terms.get(r[2]), r[5], "a surface that is not placed has a subgroup"])
    add("placement-does-not-agree", "a placed row with no live subgroup of its own collection, or an unplaced or isolated row with a subgroup", ["row", "collection", "surface", "state", "problem"], bad)
    shared = []
    for lid, cid, tid, tier in conn.execute(f"SELECT id, collection_id, term_id, tier FROM collection_link WHERE deleted=0 AND shared=1 AND tier IN ({','.join('?' * len(member_tiers(cfg)))})", member_tiers(cfg)):
        n = sum(1 for r in conn.execute("SELECT 1 FROM collection_link WHERE deleted=0 AND term_id=? AND tier IN (%s)" % ','.join('?' * len(member_tiers(cfg))), [tid] + member_tiers(cfg)))
        if n < 2:
            shared.append([lid, conn.execute("SELECT name FROM collection WHERE id=?", (cid,)).fetchone()[0], terms.get(tid), tier])
    add("shared-flag-without-a-second-link", "a live member link flagged shared whose term has no second live member link (the flag may be stale; not changed here)", ["link", "collection", "term", "tier"], shared)
    return out


def counts(conn) -> dict:
    q = lambda s: conn.execute(s).fetchone()[0]  # noqa: E731
    return {"index rows": q("SELECT count(*) FROM collection_subgroup_surface WHERE deleted=0"), "unplaced": q("SELECT count(*) FROM collection_subgroup_surface WHERE deleted=0 AND state='unplaced'"),
            "placed": q("SELECT count(*) FROM collection_subgroup_surface WHERE deleted=0 AND state='placed'"), "isolated": q("SELECT count(*) FROM collection_subgroup_surface WHERE deleted=0 AND state='isolated'"),
            "subgroups": q("SELECT count(*) FROM collection_subgroup WHERE deleted=0")}
