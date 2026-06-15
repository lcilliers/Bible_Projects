"""softdelete.py — shared soft-delete integrity helpers (hardening H1-H3, H5, 2026-06-15).

ONE cascade path for the whole engine, so the fragilities found on 2026-06-15 cannot recur:
- H1 cascade_delete_registry  — excluded/removed registry ⇒ its entire downstream soft-deleted.
- H3 cascade_delete_terms     — a soft-deleted term ⇒ its verses → verse_context → findings follow.
- H2 reconcile_delete_flags   — status='delete' implies delete_flagged=1 (with the cascade).
- H5 integrity_violations     — assert the invariants after an audit.

All functions soft-delete (delete_flagged=1) only rows currently active, and cascade downstream.
They do NOT commit — the caller owns the transaction.
"""


def _ph(ids):
    return ",".join("?" * len(ids))


def _active(cur, table, where, params):
    return [r[0] for r in cur.execute(
        f"SELECT id FROM {table} WHERE {where} AND COALESCE(delete_flagged,0)=0", params)]


def _flag(cur, table, ids, value):
    n = 0
    for i in range(0, len(ids), 400):
        ch = ids[i:i + 400]
        cur.execute(f"UPDATE {table} SET delete_flagged=? WHERE id IN ({_ph(ch)})", [value] + ch)
        n += cur.rowcount
    return n


def _verse_downstream(cur, verse_ids):
    """active verse_context + finding ids hanging off the given verses."""
    vc, fnd = [], []
    for i in range(0, len(verse_ids), 400):
        ch = verse_ids[i:i + 400]
        vc += _active(cur, "verse_context", f"verse_record_id IN ({_ph(ch)})", ch)
    for i in range(0, len(vc), 400):
        ch = vc[i:i + 400]
        fnd += _active(cur, "finding", f"verse_context_id IN ({_ph(ch)})", ch)
    return vc, fnd


def cascade_delete_verses(conn, verse_ids):
    """Soft-delete verses + their verse_context + findings. Returns counts per table."""
    cur = conn.cursor()
    verse_ids = [v for v in verse_ids if v is not None]
    if not verse_ids:
        return {}
    vc, fnd = _verse_downstream(cur, verse_ids)
    return {"wa_verse_records": _flag(cur, "wa_verse_records", verse_ids, 1),
            "verse_context": _flag(cur, "verse_context", vc, 1),
            "finding": _flag(cur, "finding", fnd, 1)}


def cascade_delete_terms(conn, mti_term_ids):
    """Soft-delete the terms' verses (+context+findings), any findings directly on the terms, and the mti rows."""
    cur = conn.cursor()
    mti_term_ids = [m for m in mti_term_ids if m is not None]
    if not mti_term_ids:
        return {}
    vr = []
    for i in range(0, len(mti_term_ids), 400):
        ch = mti_term_ids[i:i + 400]
        vr += _active(cur, "wa_verse_records", f"mti_term_id IN ({_ph(ch)})", ch)
    out = cascade_delete_verses(conn, vr)
    fnd = []
    for i in range(0, len(mti_term_ids), 400):
        ch = mti_term_ids[i:i + 400]
        fnd += _active(cur, "finding", f"mti_term_id IN ({_ph(ch)})", ch)
    out["finding"] = out.get("finding", 0) + _flag(cur, "finding", fnd, 1)
    out["mti_terms"] = _flag(cur, "mti_terms", mti_term_ids, 1)
    return out


def cascade_delete_registry(conn, registry_id):
    """H1 — soft-delete a registry's ENTIRE downstream: term_inventory, verses(+context+findings),
    owned mti_terms (+their downstream). For wherever phase1_status becomes 'Excluded'."""
    cur = conn.cursor()
    fids = [r[0] for r in cur.execute("SELECT id FROM wa_file_index WHERE registry_id=?", (registry_id,))]
    ti, vr = [], []
    for fid in fids:
        ti += _active(cur, "wa_term_inventory", "file_id=?", (fid,))
        vr += _active(cur, "wa_verse_records", "file_id=?", (fid,))
    mti = _active(cur, "mti_terms", "owning_registry_fk=?", (registry_id,))
    out = cascade_delete_verses(conn, vr)
    out["wa_term_inventory"] = _flag(cur, "wa_term_inventory", ti, 1)
    for k, v in cascade_delete_terms(conn, mti).items():
        out[k] = out.get(k, 0) + v
    return out


def reconcile_delete_flags(conn):
    """H2 — any mti_terms with status='delete' but delete_flagged=0 are made consistent (flag + cascade).
    Returns the count of terms reconciled."""
    cur = conn.cursor()
    ids = _active(cur, "mti_terms", "status='delete'", ())
    if ids:
        cascade_delete_terms(conn, ids)
    return len(ids)


def integrity_violations(conn, excluded_ids=None):
    """H5 — return a dict of invariant violations (all should be 0 after a clean audit)."""
    cur = conn.cursor()
    if excluded_ids is None:
        excluded_ids = [r[0] for r in cur.execute("SELECT id FROM word_registry WHERE phase1_status='Excluded'")]
    eph = _ph(excluded_ids) if excluded_ids else "NULL"
    v = {}
    v["active_verse_null_mti_nonexcluded"] = cur.execute(
        f"""SELECT COUNT(*) FROM wa_verse_records vr LEFT JOIN wa_file_index fi ON vr.file_id=fi.id
            WHERE COALESCE(vr.delete_flagged,0)=0 AND vr.mti_term_id IS NULL
              AND (fi.registry_id IS NULL OR fi.registry_id NOT IN ({eph}))""", excluded_ids).fetchone()[0]
    v["status_delete_not_flagged"] = cur.execute(
        "SELECT COUNT(*) FROM mti_terms WHERE status='delete' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    if excluded_ids:
        fids = [r[0] for r in cur.execute(f"SELECT id FROM wa_file_index WHERE registry_id IN ({eph})", excluded_ids)]
        fph = _ph(fids) if fids else "NULL"
        v["active_verse_under_excluded"] = cur.execute(
            f"SELECT COUNT(*) FROM wa_verse_records WHERE file_id IN ({fph}) AND COALESCE(delete_flagged,0)=0",
            fids).fetchone()[0] if fids else 0
    else:
        v["active_verse_under_excluded"] = 0
    return v
