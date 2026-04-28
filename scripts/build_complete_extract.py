"""
build_complete_extract.py
─────────────────────────
Comprehensive registry extract: every piece of data connected to a word,
organised in layers from registry meta through to Session D synthesis.

Produces: data/exports/wa-{NNN}-{word}-complete-{YYYYMMDD}.json

Usage:
  python scripts/build_complete_extract.py --registry=187
  python scripts/build_complete_extract.py --registry=187 --out=data/exports/
"""

import argparse
import json
import os
import sqlite3
from datetime import date, datetime, timezone

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "bible_research.db")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "exports", "Session C")

SCRIPT_VERSION = "1.2"


# ── helpers ──────────────────────────────────────────────────────────────────

def _row(r) -> dict | None:
    return dict(r) if r else None


def _rows(rs) -> list[dict]:
    return [dict(r) for r in rs]


def _in_sql(ids: list) -> str:
    if not ids:
        return "(NULL)"
    return "({})".format(",".join("?" * len(ids)))


def _chunked_query(conn, sql_template: str, ids: list, extra_params: list | None = None) -> list:
    """Execute a query with IN-clause, chunking if >900 params."""
    if not ids:
        return []
    results = []
    chunk_size = 900
    for i in range(0, len(ids), chunk_size):
        chunk = ids[i:i + chunk_size]
        sql = sql_template.format(_in_sql(chunk))
        params = chunk + (extra_params or [])
        results.extend(conn.execute(sql, params).fetchall())
    return results


# ── correlation queries (per-registry) ───────────────────────────────────────

def _build_correlations(conn, registry_no: int, registry_id: int,
                        file_ids: list, ti_strongs: list, mti_ids: list) -> dict:
    """Build the 5 correlation signals filtered to a single registry."""

    # Signal 1: XREF term sharing — other registries sharing Strong's numbers
    xref_pairs = _rows(conn.execute("""
        SELECT w2.no AS reg, w2.word, w2.cluster_assignment AS cluster,
               COUNT(DISTINCT a.strongs_number) AS shared_term_count,
               GROUP_CONCAT(DISTINCT a.strongs_number) AS shared_strongs
        FROM wa_term_inventory a
        JOIN wa_term_inventory b ON a.strongs_number = b.strongs_number
            AND a.file_id != b.file_id
            AND a.delete_flagged = 0 AND b.delete_flagged = 0
        JOIN wa_file_index fi1 ON fi1.id = a.file_id AND fi1.word_registry_fk = ?
        JOIN wa_file_index fi2 ON fi2.id = b.file_id
        JOIN word_registry w2 ON w2.id = fi2.word_registry_fk AND w2.no != ?
        GROUP BY w2.no
        HAVING shared_term_count >= 1
        ORDER BY shared_term_count DESC
    """, (registry_id, registry_no)).fetchall())
    for p in xref_pairs:
        if p.get("shared_strongs"):
            p["shared_strongs"] = p["shared_strongs"].split(",")

    # Signal 2: Verse co-occurrence (OWNER terms in same verse reference)
    cooccur_pairs = _rows(conn.execute("""
        SELECT w2.no AS reg, w2.word, w2.cluster_assignment AS cluster,
               COUNT(DISTINCT vr1.reference) AS shared_verse_count
        FROM wa_verse_records vr1
        JOIN wa_term_inventory ti1 ON ti1.id = vr1.term_inv_id
            AND ti1.delete_flagged = 0 AND ti1.term_owner_type = 'OWNER'
        JOIN wa_file_index fi1 ON fi1.id = ti1.file_id AND fi1.word_registry_fk = ?
        JOIN wa_verse_records vr2 ON vr1.reference = vr2.reference
            AND vr1.id != vr2.id AND vr2.delete_flagged = 0
        JOIN wa_term_inventory ti2 ON ti2.id = vr2.term_inv_id
            AND ti2.delete_flagged = 0 AND ti2.term_owner_type = 'OWNER'
        JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
        JOIN word_registry w2 ON w2.id = fi2.word_registry_fk AND w2.no != ?
        WHERE vr1.delete_flagged = 0
        GROUP BY w2.no
        HAVING shared_verse_count >= 3
        ORDER BY shared_verse_count DESC
    """, (registry_id, registry_no)).fetchall())

    # Signal 3: Dimension profile similarity (CLAUDE_AI reviewed only)
    # Build target registry's dimension profile
    target_dims = {}
    for r in conn.execute("""
        SELECT dimension, COUNT(*) AS cnt
        FROM wa_dimension_index
        WHERE owning_registry_no = ? AND dimension_confidence = 'CLAUDE_AI'
            AND delete_flagged = 0 AND dimension IS NOT NULL
        GROUP BY dimension
    """, (registry_no,)):
        target_dims[r["dimension"]] = r["cnt"]

    dim_pairs = []
    if target_dims:
        # Find other registries with overlapping CLAUDE_AI dimensions
        other_profiles: dict[int, dict] = {}
        for r in conn.execute("""
            SELECT owning_registry_no, dimension, COUNT(*) AS cnt
            FROM wa_dimension_index
            WHERE dimension_confidence = 'CLAUDE_AI' AND delete_flagged = 0
                AND dimension IS NOT NULL AND owning_registry_no != ?
            GROUP BY owning_registry_no, dimension
        """, (registry_no,)):
            other_profiles.setdefault(r["owning_registry_no"], {})[r["dimension"]] = r["cnt"]

        reg_lookup = {}
        for r in conn.execute("SELECT no, word, cluster_assignment FROM word_registry"):
            reg_lookup[r["no"]] = {"word": r["word"], "cluster": r["cluster_assignment"]}

        for other_reg, other_dims in other_profiles.items():
            shared = set(target_dims.keys()) & set(other_dims.keys())
            if len(shared) >= 2:
                overlap = [{"dimension": d,
                            "count_target": target_dims[d],
                            "count_other": other_dims[d]} for d in sorted(shared)]
                info = reg_lookup.get(other_reg, {})
                dim_pairs.append({
                    "reg": other_reg, "word": info.get("word", "?"),
                    "cluster": info.get("cluster", "?"),
                    "shared_dimension_count": len(shared),
                    "overlap": overlap,
                })
        dim_pairs.sort(key=lambda x: x["shared_dimension_count"], reverse=True)

    # Signal 4: Root family connections — shared etymological roots
    root_codes = set()
    if file_ids:
        for r in _chunked_query(
            conn,
            "SELECT DISTINCT root_code FROM wa_term_root_family WHERE term_inv_id IN "
            "(SELECT id FROM wa_term_inventory WHERE file_id IN {} AND delete_flagged = 0)",
            file_ids,
        ):
            root_codes.add(r["root_code"])

    root_families = []
    if root_codes:
        placeholders = ",".join("?" * len(root_codes))
        for r in conn.execute(f"""
            SELECT rf.root_code, rf.root_gloss,
                   COUNT(DISTINCT wr.no) AS reg_count,
                   GROUP_CONCAT(DISTINCT wr.no) AS reg_nos,
                   GROUP_CONCAT(DISTINCT wr.word) AS words,
                   GROUP_CONCAT(DISTINCT wr.cluster_assignment) AS clusters
            FROM wa_term_root_family rf
            JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id AND ti.delete_flagged = 0
            JOIN wa_file_index fi ON fi.id = ti.file_id
            JOIN word_registry wr ON wr.id = fi.word_registry_fk
            WHERE rf.root_code IN ({placeholders})
            GROUP BY rf.root_code
            HAVING reg_count >= 2
            ORDER BY reg_count DESC
        """, list(root_codes)):
            clusters = r["clusters"].split(",") if r["clusters"] else []
            root_families.append({
                "root_code": r["root_code"],
                "root_gloss": r["root_gloss"],
                "registry_count": r["reg_count"],
                "registry_nos": [int(x) for x in r["reg_nos"].split(",")] if r["reg_nos"] else [],
                "words": r["words"].split(",") if r["words"] else [],
                "cross_cluster": len(set(clusters)) > 1,
            })

    # Signal 5: Shared anchor verses — other words also anchoring on same verse
    shared_anchors = []
    if mti_ids:
        shared_anchors = _rows(conn.execute("""
            SELECT vr1.reference,
                   w2.no AS reg, w2.word, w2.cluster_assignment AS cluster,
                   vcg1.group_code AS target_group, vcg2.group_code AS other_group
            FROM verse_context vc1
            JOIN wa_verse_records vr1 ON vr1.id = vc1.verse_record_id
            JOIN wa_term_inventory ti1 ON ti1.id = vr1.term_inv_id
                AND ti1.term_owner_type = 'OWNER'
            JOIN wa_file_index fi1 ON fi1.id = ti1.file_id
                AND fi1.word_registry_fk = ?
            JOIN verse_context_group vcg1 ON vcg1.id = vc1.group_id
            JOIN verse_context vc2 ON vc1.verse_record_id != vc2.verse_record_id
            JOIN wa_verse_records vr2 ON vr2.id = vc2.verse_record_id
                AND vr2.reference = vr1.reference AND vr2.id != vr1.id
            JOIN wa_term_inventory ti2 ON ti2.id = vr2.term_inv_id
                AND ti2.term_owner_type = 'OWNER'
            JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
            JOIN word_registry w2 ON w2.id = fi2.word_registry_fk AND w2.no != ?
            JOIN verse_context_group vcg2 ON vcg2.id = vc2.group_id
            WHERE vc1.is_anchor = 1 AND vc2.is_anchor = 1
                AND vc1.delete_flagged = 0 AND vc2.delete_flagged = 0
            ORDER BY vr1.reference
        """, (registry_id, registry_no)).fetchall())

    return {
        "xref_sharing": xref_pairs,
        "verse_cooccurrence": cooccur_pairs,
        "dimension_overlap": dim_pairs,
        "root_families": root_families,
        "shared_anchor_verses": shared_anchors,
    }


# ── main extract function ────────────────────────────────────────────────────

def build_complete_extract(conn, registry_no: int, owner_only: bool = False) -> dict:
    """Build the complete extract dict for a single registry.

    Args:
        owner_only: If True, exclude XREF terms and their verses/contexts.
    """

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # ── LAYER 0: Registry & Meta ─────────────────────────────────────────────

    reg = _row(conn.execute(
        "SELECT * FROM word_registry WHERE no = ?", (registry_no,)
    ).fetchone())
    if not reg:
        raise ValueError(f"No word_registry entry for no={registry_no}")

    word = reg["word"]
    registry_id = reg["id"]  # internal id (usually == no, but not guaranteed)

    schema_ver = conn.execute(
        "SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1"
    ).fetchone()
    schema_ver = schema_ver["version_code"] if schema_ver else "unknown"

    cluster = reg.get("cluster_assignment")
    cluster_log = _row(conn.execute(
        "SELECT * FROM wa_dim_review_cluster_log WHERE cluster = ?",
        (cluster,)
    ).fetchone()) if cluster else None

    # ── File index ───────────────────────────────────────────────────────────

    files = _rows(conn.execute(
        "SELECT * FROM wa_file_index WHERE word_registry_fk = ? ORDER BY part_number",
        (registry_id,),
    ).fetchall())
    file_ids = [f["id"] for f in files]

    # ── Run history & patch history ──────────────────────────────────────────

    run_history = _rows(conn.execute(
        """SELECT wrs.*, erl.started_at AS run_started, erl.completed_at AS run_completed,
                  erl.outcome AS run_outcome
           FROM word_run_state wrs
           LEFT JOIN engine_run_log erl ON erl.run_id = wrs.run_id
           WHERE wrs.registry_id = ?
           ORDER BY erl.started_at DESC""",
        (registry_no,),
    ).fetchall())

    patch_history = _rows(conn.execute(
        """SELECT run_id, mode, started_at, completed_at, outcome, error_detail
           FROM engine_run_log
           WHERE mode = 'SESSION_PATCH'
           AND (target_registry_ids = ? OR target_registry_ids = ? OR run_id LIKE ?)
           ORDER BY started_at""",
        (str(registry_no), registry_no, f"%-{registry_no:03d}-%"),
    ).fetchall())

    # ── LAYER 1: Terms ───────────────────────────────────────────────────────

    ti_rows_all = _rows(_chunked_query(
        conn,
        "SELECT * FROM wa_term_inventory WHERE file_id IN {} ORDER BY strongs_number",
        file_ids,
    )) if file_ids else []

    if owner_only:
        ti_rows = [t for t in ti_rows_all if t.get("term_owner_type") != "XREF"]
    else:
        ti_rows = ti_rows_all

    ti_ids = [t["id"] for t in ti_rows]
    ti_strongs = [t["strongs_number"] for t in ti_rows]

    # meaning_parsed
    mp_rows = _rows(_chunked_query(
        conn, "SELECT * FROM wa_meaning_parsed WHERE term_inv_id IN {}", ti_ids,
    )) if ti_ids else []
    mp_by_ti = {r["term_inv_id"]: r for r in mp_rows}
    mp_ids = [r["id"] for r in mp_rows]

    # meaning_sense
    sense_by_mp: dict[int, list] = {}
    for r in _chunked_query(
        conn, "SELECT * FROM wa_meaning_sense WHERE parsed_meaning_id IN {} ORDER BY sort_order",
        mp_ids,
    ):
        sense_by_mp.setdefault(r["parsed_meaning_id"], []).append(dict(r))

    # meaning_stem
    stem_by_mp: dict[int, list] = {}
    for r in _chunked_query(
        conn, "SELECT * FROM wa_meaning_stem WHERE parsed_meaning_id IN {}", mp_ids,
    ):
        stem_by_mp.setdefault(r["parsed_meaning_id"], []).append(dict(r))

    # lsj_parsed
    lsj_by_ti: dict[int, dict] = {}
    for r in _chunked_query(
        conn, "SELECT * FROM wa_lsj_parsed WHERE term_inv_id IN {}", ti_ids,
    ):
        lsj_by_ti[r["term_inv_id"]] = dict(r)

    # quality_flags
    dqf_by_ti: dict[str, list] = {}
    for r in _chunked_query(
        conn,
        """SELECT f.term_id, ft.flag_code, ft.flag_group, ft.description AS flag_type_description,
                  f.description AS detail, f.last_changed
           FROM wa_data_quality_flags f
           JOIN wa_quality_flag_types ft ON ft.id = f.flag_id
           WHERE f.file_id IN {}
           ORDER BY ft.flag_group, ft.flag_code""",
        file_ids,
    ):
        dqf_by_ti.setdefault(r["term_id"], []).append({
            "flag_code": r["flag_code"], "flag_group": r["flag_group"],
            "description": r["flag_type_description"], "detail": r["detail"],
            "last_changed": r["last_changed"],
        })

    # phase2_flags
    p2f_by_ti: dict[int, list] = {}
    for r in _chunked_query(
        conn,
        """SELECT p.term_inv_id, ft.flag_code, ft.description AS type_description,
                  p.description AS instance_description, p.source, p.raised_date
           FROM wa_term_phase2_flags p
           JOIN phase2_flag_types ft ON ft.id = p.flag_id
           WHERE p.term_inv_id IN {}
           ORDER BY ft.flag_code""",
        ti_ids,
    ):
        p2f_by_ti.setdefault(r["term_inv_id"], []).append({
            "flag_code": r["flag_code"], "description": r["type_description"],
            "detail": r["instance_description"], "source": r["source"],
            "raised_date": r["raised_date"],
        })

    # related_words
    rw_by_ti: dict[int, list] = {}
    for r in _chunked_query(
        conn,
        "SELECT * FROM wa_term_related_words WHERE term_inv_id IN {} ORDER BY strongs_number",
        ti_ids,
    ):
        rw_by_ti.setdefault(r["term_inv_id"], []).append(dict(r))

    # root_family
    rf_by_ti: dict[int, list] = {}
    for r in _chunked_query(
        conn, "SELECT * FROM wa_term_root_family WHERE term_inv_id IN {}", ti_ids,
    ):
        rf_by_ti.setdefault(r["term_inv_id"], []).append(dict(r))

    # ── LAYER 2: MTI Terms ───────────────────────────────────────────────────

    mti_rows_raw = []
    if ti_strongs:
        mti_rows_raw = _rows(_chunked_query(
            conn,
            "SELECT * FROM mti_terms WHERE strongs_number IN {} "
            "ORDER BY CASE WHEN owning_registry_fk = ? THEN 0 ELSE 1 END, strongs_number",
            ti_strongs, [registry_id],
        ))
    # Deduplicate: first match per strongs wins (registry-matched first)
    mti_by_strongs: dict[str, dict] = {}
    for r in mti_rows_raw:
        if r["strongs_number"] not in mti_by_strongs:
            mti_by_strongs[r["strongs_number"]] = r

    mti_ids = [r["id"] for r in mti_by_strongs.values()]

    # mti cross_refs
    mti_xref_by_mti: dict[int, list] = {}
    for r in _chunked_query(
        conn, "SELECT * FROM mti_term_cross_refs WHERE mti_term_id IN {}", mti_ids,
    ):
        mti_xref_by_mti.setdefault(r["mti_term_id"], []).append(dict(r))

    # mti flags
    mti_flags_by_mti: dict[int, list] = {}
    for r in _chunked_query(
        conn,
        """SELECT mf.mti_term_id, ft.flag_code
           FROM mti_term_flags mf
           JOIN phase2_flag_types ft ON ft.id = mf.flag_id
           WHERE mf.mti_term_id IN {}""",
        mti_ids,
    ):
        mti_flags_by_mti.setdefault(r["mti_term_id"], []).append({"flag_code": r["flag_code"]})

    # ── LAYER 3: Verses ──────────────────────────────────────────────────────

    vr_by_ti: dict[int, list] = {}
    for r in _chunked_query(
        conn,
        """SELECT * FROM wa_verse_records WHERE term_inv_id IN {}
           ORDER BY testament, book_id, chapter, verse_num""",
        ti_ids,
    ):
        vr_by_ti.setdefault(r["term_inv_id"], []).append(dict(r))

    all_verse_ids = [v["id"] for vlist in vr_by_ti.values() for v in vlist]

    # verse-term links
    vtl_by_verse: dict[int, list] = {}
    try:
        for r in _chunked_query(
            conn,
            """SELECT vtl.verse_id, vtl.term_inv_id, vtl.step_subgloss_code,
                      vtl.step_subgloss_label, vtl.span_strong_match, vtl.target_word,
                      ti.strongs_number, ti.step_search_gloss
               FROM wa_verse_term_links vtl
               JOIN wa_term_inventory ti ON ti.id = vtl.term_inv_id
               WHERE vtl.verse_id IN {}
               ORDER BY vtl.verse_id, vtl.step_subgloss_code""",
            all_verse_ids,
        ):
            vtl_by_verse.setdefault(r["verse_id"], []).append({
                "term_inv_id": r["term_inv_id"],
                "strongs_number": r["strongs_number"],
                "step_subgloss_code": r["step_subgloss_code"],
                "step_subgloss_label": r["step_subgloss_label"],
                "span_strong_match": r["span_strong_match"],
                "target_word": r["target_word"],
            })
    except Exception:
        pass

    # Verse reference lookup (for enriching verse_context layer)
    verse_ref_map: dict[int, str] = {}
    for vlist in vr_by_ti.values():
        for v in vlist:
            verse_ref_map[v["id"]] = v.get("reference", "")

    # ── LAYER 4: Verse Context ───────────────────────────────────────────────

    # Context groups
    vcg_rows = _rows(_chunked_query(
        conn,
        "SELECT * FROM verse_context_group WHERE mti_term_id IN {} ORDER BY group_code",
        mti_ids,
    )) if mti_ids else []
    vcg_by_id: dict[int, dict] = {g["id"]: g for g in vcg_rows}

    # Context records
    vc_rows = _rows(_chunked_query(
        conn,
        """SELECT vc.*, vcg.group_code
           FROM verse_context vc
           LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id
           WHERE vc.mti_term_id IN {}
           ORDER BY vc.mti_term_id, COALESCE(vc.group_id, 999999), vc.verse_record_id""",
        mti_ids,
    )) if mti_ids else []

    # Organise: group contexts by group_id
    vc_by_group: dict[int, list] = {}
    vc_unassigned: list[dict] = []
    for vc in vc_rows:
        gid = vc.get("group_id")
        classification = "anchor" if vc.get("is_anchor") else (
            "related" if vc.get("is_related") else (
                "set_aside" if not vc.get("is_relevant") else "relevant"))
        vc["_classification"] = classification
        vc["verse_reference"] = verse_ref_map.get(vc.get("verse_record_id"), "")
        if gid:
            vc_by_group.setdefault(gid, []).append(vc)
        else:
            vc_unassigned.append(vc)

    # Build groups with nested contexts and counts
    vc_groups_out = []
    for g in vcg_rows:
        gid = g["id"]
        contexts = vc_by_group.get(gid, [])
        active_contexts = [c for c in contexts if not c.get("delete_flagged")]
        g["classification_counts"] = {
            "anchor": sum(1 for c in active_contexts if c["_classification"] == "anchor"),
            "related": sum(1 for c in active_contexts if c["_classification"] == "related"),
            "set_aside": sum(1 for c in active_contexts if c["_classification"] == "set_aside"),
            "relevant": sum(1 for c in active_contexts if c["_classification"] == "relevant"),
        }
        g["contexts"] = contexts
        vc_groups_out.append(g)

    # ── LAYER 5: Dimension Index ─────────────────────────────────────────────

    dim_rows = _rows(conn.execute(
        """SELECT * FROM wa_dimension_index
           WHERE owning_registry_no = ? AND delete_flagged = 0
           ORDER BY group_code""",
        (registry_no,),
    ).fetchall())

    # ── LAYER 6: Session B ───────────────────────────────────────────────────

    sb_dimensions = _row(conn.execute(
        "SELECT * FROM wa_session_b_dimensions WHERE registry_id = ?",
        (registry_no,),
    ).fetchone())

    sb_findings = _rows(conn.execute(
        "SELECT * FROM wa_session_b_findings WHERE registry_id = ? ORDER BY finding_id",
        (registry_no,),
    ).fetchall())

    # ── LAYER 7: Session D & Research Flags ──────────────────────────────────

    research_flags = _rows(conn.execute(
        "SELECT * FROM wa_session_research_flags WHERE registry_id = ? ORDER BY flag_label",
        (registry_no,),
    ).fetchall())

    sd_pointers = [f for f in research_flags if f.get("flag_code") == "SD_POINTER"]

    # Session D runs involving this registry
    sd_runs_out = []
    try:
        sd_runs = _rows(conn.execute(
            "SELECT * FROM session_d_runs ORDER BY run_date"
        ).fetchall())
        for run in sd_runs:
            scope = run.get("registries_in_scope", "")
            try:
                scope_list = json.loads(scope) if scope else []
            except (json.JSONDecodeError, TypeError):
                scope_list = []
            if registry_no in scope_list or str(registry_no) in scope_list:
                run_id = run.get("run_id")
                verse_links = _rows(conn.execute(
                    "SELECT * FROM session_d_verse_links WHERE run_id = ?", (run_id,)
                ).fetchall())
                term_links = _rows(conn.execute(
                    "SELECT * FROM session_d_term_links WHERE run_id = ?", (run_id,)
                ).fetchall())
                observations = _rows(conn.execute(
                    "SELECT * FROM session_d_observations WHERE run_id = ?", (run_id,)
                ).fetchall())
                run["verse_links"] = verse_links
                run["term_links"] = term_links
                run["observations"] = observations
                sd_runs_out.append(run)
    except Exception:
        pass  # Session D tables may not exist

    # ── LAYER 8: Cross-Registry Links ────────────────────────────────────────

    cross_links = _rows(_chunked_query(
        conn,
        """SELECT crl.*, ct.type_code, ct.description AS link_type_description
           FROM wa_cross_registry_links crl
           JOIN wa_crosslink_type ct ON ct.id = crl.connection_type_id
           WHERE crl.file_id IN {}
           ORDER BY crl.linked_word""",
        file_ids,
    )) if file_ids else []

    # ── LAYER 9: Correlations (per-registry) ───────────────────────────────

    correlations = _build_correlations(conn, registry_no, registry_id, file_ids,
                                       ti_strongs, mti_ids)

    # ── Assemble Terms ───────────────────────────────────────────────────────

    terms_out = []
    for ti in ti_rows:
        ti_id = ti["id"]
        term_id = ti.get("term_id")
        strong = ti.get("strongs_number")

        mp = mp_by_ti.get(ti_id)
        if mp:
            mp_out = dict(mp)
            mp_out["senses"] = sense_by_mp.get(mp["id"], [])
            mp_out["stems"] = stem_by_mp.get(mp["id"], [])
        else:
            mp_out = None

        lsj_out = lsj_by_ti.get(ti_id)
        dqf_out = dqf_by_ti.get(term_id, [])
        p2f_out = p2f_by_ti.get(ti_id, [])
        rw_out = rw_by_ti.get(ti_id, [])
        rf_out = rf_by_ti.get(ti_id, [])

        # Verses with term_links
        vr_out = []
        for v in vr_by_ti.get(ti_id, []):
            vd = dict(v)
            vd["term_links"] = vtl_by_verse.get(v["id"], [])
            vr_out.append(vd)

        # MTI entry
        mti_entry = mti_by_strongs.get(strong)
        if mti_entry:
            mti_out = dict(mti_entry)
            mti_out["cross_refs"] = mti_xref_by_mti.get(mti_entry["id"], [])
            mti_out["flags"] = mti_flags_by_mti.get(mti_entry["id"], [])
        else:
            mti_out = None

        term_out = dict(ti)
        term_out["_active"] = not ti.get("delete_flagged", 0)
        term_out["meaning_parsed"] = mp_out
        term_out["lsj_parsed"] = lsj_out
        term_out["quality_flags"] = dqf_out
        term_out["phase2_flags"] = p2f_out
        term_out["related_words"] = rw_out
        term_out["root_family"] = rf_out
        term_out["mti"] = mti_out
        term_out["verses"] = vr_out
        terms_out.append(term_out)

    # ── Statistics ────────────────────────────────────────────────────────────

    active_terms = [t for t in ti_rows if not t.get("delete_flagged")]
    all_verses = [v for vlist in vr_by_ti.values() for v in vlist]
    active_verses = [v for v in all_verses if not v.get("delete_flagged")]

    lang_counts: dict[str, int] = {}
    for t in ti_rows:
        lang = t.get("language") or "unknown"
        lang_counts[lang] = lang_counts.get(lang, 0) + 1

    testament_counts: dict[str, int] = {}
    span_counts: dict[str, int] = {"match": 0, "no_match": 0, "no_html": 0}
    for v in all_verses:
        t = v.get("testament") or "unknown"
        testament_counts[t] = testament_counts.get(t, 0) + 1
        sm = v.get("span_strong_match")
        if sm == 1:
            span_counts["match"] += 1
        elif sm == 0:
            span_counts["no_match"] += 1
        else:
            span_counts["no_html"] += 1

    active_vc = [c for c in vc_rows if not c.get("delete_flagged")]

    statistics = {
        "term_count": len(ti_rows),
        "active_term_count": len(active_terms),
        "owner_term_count": sum(1 for t in active_terms if t.get("term_owner_type") == "OWNER"),
        "xref_term_count": sum(1 for t in active_terms if t.get("term_owner_type") == "XREF"),
        "verse_count": len(all_verses),
        "active_verse_count": len(active_verses),
        "terms_by_language": lang_counts,
        "verses_by_testament": testament_counts,
        "span_match_distribution": span_counts,
        "quality_flag_count": sum(len(v) for v in dqf_by_ti.values()),
        "phase2_flag_count": sum(len(v) for v in p2f_by_ti.values()),
        "meaning_parsed_count": len(mp_rows),
        "lsj_parsed_count": len(lsj_by_ti),
        "root_family_count": sum(len(v) for v in rf_by_ti.values()),
        "related_word_count": sum(len(v) for v in rw_by_ti.values()),
        "mti_term_count": len(mti_by_strongs),
        "cross_registry_link_count": len(cross_links),
        "verse_term_link_count": sum(len(v) for v in vtl_by_verse.values()),
        "research_flag_count": len(research_flags),
        "verse_context_group_count": len(vcg_rows),
        "verse_context_record_count": len(vc_rows),
        "anchor_verse_count": sum(1 for c in active_vc if c.get("is_anchor")),
        "related_verse_count": sum(1 for c in active_vc if c.get("is_related") and not c.get("is_anchor")),
        "set_aside_verse_count": sum(1 for c in active_vc if not c.get("is_relevant")),
        "dimension_index_count": len(dim_rows),
        "session_b_finding_count": len(sb_findings),
        "session_d_pointer_count": len(sd_pointers),
        "session_d_run_count": len(sd_runs_out),
        "correlation_xref_pair_count": len(correlations.get("xref_sharing", [])),
        "correlation_cooccurrence_pair_count": len(correlations.get("verse_cooccurrence", [])),
        "correlation_dimension_pair_count": len(correlations.get("dimension_overlap", [])),
        "correlation_root_family_count": len(correlations.get("root_families", [])),
        "correlation_shared_anchor_count": len(correlations.get("shared_anchor_verses", [])),
    }

    # ── Final document ───────────────────────────────────────────────────────

    scope = "owner_only" if owner_only else "complete"

    return {
        "_export": {
            "word": word,
            "registry": registry_no,
            "scope": scope,
            "exported_at": now_utc,
            "schema_version": schema_ver,
            "export_script_version": SCRIPT_VERSION,
        },
        "registry": reg,
        "cluster_log": cluster_log,
        "files": files,
        "run_history": run_history,
        "patch_history": patch_history,
        "terms": terms_out,
        "verse_context": {
            "groups": vc_groups_out,
            "unassigned": vc_unassigned,
        },
        "dimension_index": dim_rows,
        "session_b": {
            "dimensions": sb_dimensions,
            "findings": sb_findings,
        },
        "session_d": {
            "sd_pointer_flags": sd_pointers,
            "runs": sd_runs_out,
        },
        "correlations": correlations,
        "cross_registry_links": cross_links,
        "session_research_flags": research_flags,
        "statistics": statistics,
    }


# ── CLI ──────────────────────────────────────────────────────────────────────

def _next_version(out_dir: str, prefix: str) -> int:
    """Find the next version number for files matching prefix in out_dir."""
    if not os.path.isdir(out_dir):
        return 1
    existing = [f for f in os.listdir(out_dir) if f.startswith(prefix) and f.endswith(".json")]
    if not existing:
        return 1
    versions = []
    for f in existing:
        # Extract vN from filename like wa-062-fellowship-complete-2026-04-13-v2.json
        stem = f.rsplit(".json", 1)[0]
        parts = stem.rsplit("-v", 1)
        if len(parts) == 2 and parts[1].isdigit():
            versions.append(int(parts[1]))
        else:
            versions.append(1)  # unversioned file counts as v1
    return max(versions) + 1


def _write_extract(data: dict, registry_no: int, out_dir: str) -> None:
    """Write extract to JSON and print summary. Auto-versions per registry per day."""
    word = data["_export"]["word"]
    scope = data["_export"]["scope"]
    today = date.today().isoformat()
    prefix = f"wa-{registry_no:03d}-{word}-{scope}-{today}"
    os.makedirs(out_dir, exist_ok=True)
    version = _next_version(out_dir, prefix)
    filename = f"{prefix}-v{version}.json"
    data["_export"]["version"] = version
    out_path = os.path.join(out_dir, filename)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    fsize = os.path.getsize(out_path)
    stats = data["statistics"]

    print(f"Written: {out_path}")
    print(f"Registry: {registry_no} ({word})  Scope: {scope}")
    print(f"Size: {fsize / 1024:.0f} KB")
    print(f"Terms: {stats['active_term_count']} active "
          f"({stats['owner_term_count']} OWNER, {stats['xref_term_count']} XREF)")
    print(f"Verses: {stats['active_verse_count']} active")
    print(f"Verse Context: {stats['verse_context_group_count']} groups, "
          f"{stats['anchor_verse_count']} anchors")
    print(f"Dimension Index: {stats['dimension_index_count']} rows")
    print(f"Session B findings: {stats['session_b_finding_count']}")
    print(f"Session D pointers: {stats['session_d_pointer_count']}")
    print(f"Research flags: {stats['research_flag_count']}")
    print(f"Cross-registry links: {stats['cross_registry_link_count']}")
    print(f"Correlations: XREF={stats['correlation_xref_pair_count']}, "
          f"co-occur={stats['correlation_cooccurrence_pair_count']}, "
          f"dim={stats['correlation_dimension_pair_count']}, "
          f"root={stats['correlation_root_family_count']}, "
          f"anchors={stats['correlation_shared_anchor_count']}")


def main():
    parser = argparse.ArgumentParser(
        description="Build comprehensive registry extract (all DB layers)")
    parser.add_argument("--registry", type=int, required=True,
                        help="word_registry.no value (e.g. 187 for strength)")
    parser.add_argument("--out", metavar="DIR", default=OUT_DIR,
                        help=f"Output directory (default: {OUT_DIR})")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--owner-only", action="store_true",
                       help="Produce OWNER-only extract (exclude XREF terms and their verses)")
    group.add_argument("--complete-only", action="store_true",
                       help="Produce complete extract only (include all terms)")
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Default: produce both versions
    variants = []
    if args.owner_only:
        variants = [True]
    elif args.complete_only:
        variants = [False]
    else:
        variants = [True, False]  # owner_only first (smaller), then complete

    for owner_only in variants:
        try:
            data = build_complete_extract(conn, args.registry, owner_only=owner_only)
        except ValueError as exc:
            print(f"ERROR: {exc}")
            conn.close()
            return
        _write_extract(data, args.registry, args.out)
        if len(variants) > 1:
            print()

    conn.close()


if __name__ == "__main__":
    main()
