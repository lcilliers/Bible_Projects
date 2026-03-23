"""
word_export.py
──────────────
Reusable utility: export all data for a single word/registry to a structured
dict (which callers can serialise to JSON).

Usage (as library):
    from analytics.word_export import export_word
    from analytics.db_client import get_connection
    data = export_word(get_connection(), registry_id=182)

Usage (CLI):
    python scripts/export_word_json.py --registry=182 --out=data/exports/

JSON structure
──────────────
{
  "_export":  { word, registry, scope, exported_at, schema_version },
  "registry": { ...word_registry fields },
  "files":    [ ...wa_file_index rows ],
  "run_history": [ ...word_run_state rows ],
  "cross_registry_links": [ ...wa_cross_registry_links + type_code ],
  "statistics": {
      term_count, verse_count, flag_count,
      terms_by_language, verses_by_testament, span_match_distribution
  },
  "terms": [
    {
      "_meta": { "empty_tables": [...] },
      ...wa_term_inventory fields,
      "meaning_parsed": {
          ...wa_meaning_parsed fields,
          "senses": [ ...wa_meaning_sense rows ],
          "stems":  [ ...wa_meaning_stem rows ]
      },
      "lsj_parsed":   { ...wa_lsj_parsed row },
      "quality_flags": [ { flag_code, flag_group, description, detail } ],
      "phase2_flags":  [ { flag_code, description } ],
      "related_words": [ ...wa_term_related_words rows ],
      "root_family":   [ ...wa_term_root_family rows ],
      "mti": {
          ...mti_terms row,
          "cross_refs": [ ...mti_term_cross_refs rows ],
          "flags":      [ { flag_code } ]
      },
      "verses": [ ...wa_verse_records rows ]
    }
  ]
}
"""

from __future__ import annotations

from datetime import datetime, timezone


# ── helpers ───────────────────────────────────────────────────────────────────

def _row(r) -> dict | None:
    """Convert a sqlite3.Row (or None) to a plain dict."""
    return dict(r) if r else None


def _rows(rs) -> list[dict]:
    """Convert a list of sqlite3.Row objects to plain dicts."""
    return [dict(r) for r in rs]


# ── main export function ───────────────────────────────────────────────────────

def export_word(conn, registry_id: int) -> dict:
    """Build and return the full export dict for a single registry entry.

    Args:
        conn:           Open database connection (read-only queries only).
        registry_id:    word_registry.no value (e.g. 182 for Soul).

    Returns:
        A plain dict ready for json.dumps().

    Raises:
        ValueError: if registry_id does not exist in word_registry.
    """

    # ── word_registry ─────────────────────────────────────────────────────────
    reg = _row(conn.execute(
        "SELECT * FROM word_registry WHERE no = ?", (registry_id,)
    ).fetchone())
    if not reg:
        raise ValueError(f"No word_registry entry for no={registry_id}")

    word = reg["word"]

    # ── schema version ────────────────────────────────────────────────────────
    schema_ver = conn.execute(
        "SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1"
    ).fetchone()
    schema_ver = schema_ver["version_code"] if schema_ver else "unknown"

    # ── wa_file_index (all file parts for this registry) ─────────────────────
    files = _rows(conn.execute(
        "SELECT * FROM wa_file_index WHERE word_registry_fk = ? ORDER BY part_number",
        (registry_id,),
    ).fetchall())
    file_ids = [f["id"] for f in files]

    if not file_ids:
        file_ids_sql = "(NULL)"
    else:
        file_ids_sql = "({})".format(",".join("?" * len(file_ids)))

    # ── word_run_state ────────────────────────────────────────────────────────
    run_history = _rows(conn.execute(
        """SELECT wrs.*, erl.started_at AS run_started, erl.completed_at AS run_completed,
                  erl.outcome AS run_outcome
           FROM word_run_state wrs
           LEFT JOIN engine_run_log erl ON erl.run_id = wrs.run_id
           WHERE wrs.registry_id = ?
           ORDER BY erl.started_at DESC""",
        (registry_id,),
    ).fetchall())

    # ── wa_cross_registry_links ───────────────────────────────────────────────
    cross_links = _rows(conn.execute(
        """SELECT crl.*, ct.type_code, ct.description AS link_type_description
           FROM wa_cross_registry_links crl
           JOIN wa_crosslink_type ct ON ct.id = crl.connection_type_id
           WHERE crl.file_id IN {}
           ORDER BY crl.linked_word""".format(file_ids_sql),
        file_ids,
    ).fetchall()) if file_ids else []

    # ── wa_term_inventory (all terms for this word) ───────────────────────────
    ti_rows = _rows(conn.execute(
        "SELECT * FROM wa_term_inventory WHERE file_id IN {} ORDER BY strongs_number".format(
            file_ids_sql),
        file_ids,
    ).fetchall()) if file_ids else []

    ti_ids       = [t["id"]             for t in ti_rows]
    ti_strongs   = [t["strongs_number"] for t in ti_rows]

    if not ti_ids:
        ti_ids_sql     = "(NULL)"
        strongs_sql    = "(NULL)"
    else:
        ti_ids_sql     = "({})".format(",".join("?" * len(ti_ids)))
        strongs_sql    = "({})".format(",".join("?" * len(ti_strongs)))

    # ── bulk-fetch all child data ─────────────────────────────────────────────

    # wa_meaning_parsed
    mp_rows = _rows(conn.execute(
        "SELECT * FROM wa_meaning_parsed WHERE term_inv_id IN {}".format(ti_ids_sql),
        ti_ids,
    ).fetchall()) if ti_ids else []
    mp_by_ti   = {r["term_inv_id"]: r for r in mp_rows}
    mp_ids     = [r["id"] for r in mp_rows]
    mp_ids_sql = "({})".format(",".join("?" * len(mp_ids))) if mp_ids else "(NULL)"

    # wa_meaning_sense
    sense_by_mp: dict[int, list] = {}
    if mp_ids:
        for r in conn.execute(
            "SELECT * FROM wa_meaning_sense WHERE parsed_meaning_id IN {} ORDER BY sort_order".format(mp_ids_sql),
            mp_ids,
        ).fetchall():
            sense_by_mp.setdefault(r["parsed_meaning_id"], []).append(dict(r))

    # wa_meaning_stem
    stem_by_mp: dict[int, list] = {}
    if mp_ids:
        for r in conn.execute(
            "SELECT * FROM wa_meaning_stem WHERE parsed_meaning_id IN {}".format(mp_ids_sql),
            mp_ids,
        ).fetchall():
            stem_by_mp.setdefault(r["parsed_meaning_id"], []).append(dict(r))

    # wa_lsj_parsed
    lsj_by_ti: dict[int, dict] = {}
    if ti_ids:
        for r in conn.execute(
            "SELECT * FROM wa_lsj_parsed WHERE term_inv_id IN {}".format(ti_ids_sql),
            ti_ids,
        ).fetchall():
            lsj_by_ti[r["term_inv_id"]] = dict(r)

    # wa_data_quality_flags (joined with flag types)
    dqf_by_ti: dict[int, list] = {}
    if ti_ids:
        for r in conn.execute(
            """SELECT f.term_id, ft.flag_code, ft.flag_group, ft.description AS flag_type_description,
                      f.description AS detail, f.last_changed
               FROM wa_data_quality_flags f
               JOIN wa_quality_flag_types ft ON ft.id = f.flag_id
               WHERE f.file_id IN {}
               ORDER BY ft.flag_group, ft.flag_code""".format(file_ids_sql),
            file_ids,
        ).fetchall():
            dqf_by_ti.setdefault(r["term_id"], []).append({
                "flag_code":        r["flag_code"],
                "flag_group":       r["flag_group"],
                "description":      r["flag_type_description"],
                "detail":           r["detail"],
                "last_changed":     r["last_changed"],
            })

    # wa_term_phase2_flags (joined with phase2_flag_types)
    p2f_by_ti: dict[int, list] = {}
    if ti_ids:
        for r in conn.execute(
            """SELECT p.term_inv_id, ft.flag_code, ft.description
               FROM wa_term_phase2_flags p
               JOIN phase2_flag_types ft ON ft.id = p.flag_id
               WHERE p.term_inv_id IN {}
               ORDER BY ft.flag_code""".format(ti_ids_sql),
            ti_ids,
        ).fetchall():
            p2f_by_ti.setdefault(r["term_inv_id"], []).append({
                "flag_code":    r["flag_code"],
                "description":  r["description"],
            })

    # wa_term_related_words
    rw_by_ti: dict[int, list] = {}
    if ti_ids:
        for r in conn.execute(
            "SELECT * FROM wa_term_related_words WHERE term_inv_id IN {} ORDER BY strongs_number".format(ti_ids_sql),
            ti_ids,
        ).fetchall():
            rw_by_ti.setdefault(r["term_inv_id"], []).append(dict(r))

    # wa_term_root_family
    rf_by_ti: dict[int, list] = {}
    if ti_ids:
        for r in conn.execute(
            "SELECT * FROM wa_term_root_family WHERE term_inv_id IN {}".format(ti_ids_sql),
            ti_ids,
        ).fetchall():
            rf_by_ti.setdefault(r["term_inv_id"], []).append(dict(r))

    # mti_terms (lookup by strongs_number; one row per strong)
    mti_by_strongs: dict[str, dict] = {}
    if ti_strongs:
        for r in conn.execute(
            "SELECT * FROM mti_terms WHERE strongs_number IN {}".format(strongs_sql),
            ti_strongs,
        ).fetchall():
            mti_by_strongs[r["strongs_number"]] = dict(r)

    mti_ids     = [r["id"] for r in mti_by_strongs.values()]
    mti_ids_sql = "({})".format(",".join("?" * len(mti_ids))) if mti_ids else "(NULL)"

    # mti_term_cross_refs
    mti_xref_by_mti: dict[int, list] = {}
    if mti_ids:
        for r in conn.execute(
            "SELECT * FROM mti_term_cross_refs WHERE mti_term_id IN {}".format(mti_ids_sql),
            mti_ids,
        ).fetchall():
            mti_xref_by_mti.setdefault(r["mti_term_id"], []).append(dict(r))

    # mti_term_flags (joined with phase2_flag_types for flag_code)
    mti_flags_by_mti: dict[int, list] = {}
    if mti_ids:
        for r in conn.execute(
            """SELECT mf.mti_term_id, ft.flag_code
               FROM mti_term_flags mf
               JOIN phase2_flag_types ft ON ft.id = mf.flag_id
               WHERE mf.mti_term_id IN {}""".format(mti_ids_sql),
            mti_ids,
        ).fetchall():
            mti_flags_by_mti.setdefault(r["mti_term_id"], []).append({"flag_code": r["flag_code"]})

    # wa_verse_records
    vr_by_ti: dict[int, list] = {}
    if ti_ids:
        for r in conn.execute(
            """SELECT * FROM wa_verse_records WHERE term_inv_id IN {}
               ORDER BY testament, book_id, chapter, verse_num""".format(ti_ids_sql),
            ti_ids,
        ).fetchall():
            vr_by_ti.setdefault(r["term_inv_id"], []).append(dict(r))

    # ── statistics ────────────────────────────────────────────────────────────
    verse_count = sum(len(v) for v in vr_by_ti.values())
    flag_count  = sum(len(v) for v in dqf_by_ti.values())

    lang_counts: dict[str, int] = {}
    for t in ti_rows:
        lang = t.get("language") or "unknown"
        lang_counts[lang] = lang_counts.get(lang, 0) + 1

    testament_counts: dict[str, int] = {}
    span_counts: dict[str, int] = {"match": 0, "no_match": 0, "no_html": 0}
    for vlist in vr_by_ti.values():
        for v in vlist:
            t = v.get("testament") or "unknown"
            testament_counts[t] = testament_counts.get(t, 0) + 1
            sm = v.get("span_strong_match")
            if sm == 1:
                span_counts["match"] += 1
            elif sm == 0:
                span_counts["no_match"] += 1
            else:
                span_counts["no_html"] += 1

    statistics = {
        "term_count":              len(ti_rows),
        "verse_count":             verse_count,
        "quality_flag_count":      flag_count,
        "phase2_flag_count":       sum(len(v) for v in p2f_by_ti.values()),
        "terms_by_language":       lang_counts,
        "verses_by_testament":     testament_counts,
        "span_match_distribution": span_counts,
        "meaning_parsed_count":    len(mp_rows),
        "lsj_parsed_count":        len(lsj_by_ti),
        "root_family_count":       sum(len(v) for v in rf_by_ti.values()),
        "related_word_count":      sum(len(v) for v in rw_by_ti.values()),
        "mti_term_count":          len(mti_by_strongs),
        "cross_registry_link_count": len(cross_links),
    }

    # ── assemble terms ────────────────────────────────────────────────────────
    _TERM_LEVEL_TABLES = [
        "meaning_parsed", "lsj_parsed", "quality_flags", "phase2_flags",
        "related_words", "root_family", "mti", "verses",
    ]

    terms_out = []
    for ti in ti_rows:
        ti_id   = ti["id"]
        term_id = ti.get("term_id")          # strongs string used as FK in dqf
        strong  = ti.get("strongs_number")

        # meaning_parsed (with senses + stems nested)
        mp = mp_by_ti.get(ti_id)
        if mp:
            mp_out = dict(mp)
            mp_out["senses"] = sense_by_mp.get(mp["id"], [])
            mp_out["stems"]  = stem_by_mp.get(mp["id"], [])
        else:
            mp_out = None

        # lsj
        lsj_out = lsj_by_ti.get(ti_id)

        # quality flags — wa_data_quality_flags uses term_id (the strongs string)
        dqf_out = dqf_by_ti.get(term_id, [])

        # phase2 flags
        p2f_out = p2f_by_ti.get(ti_id, [])

        # related words
        rw_out = rw_by_ti.get(ti_id, [])

        # root family
        rf_out = rf_by_ti.get(ti_id, [])

        # mti
        mti_entry = mti_by_strongs.get(strong)
        if mti_entry:
            mti_id  = mti_entry["id"]
            mti_out = dict(mti_entry)
            mti_out["cross_refs"] = mti_xref_by_mti.get(mti_id, [])
            mti_out["flags"]      = mti_flags_by_mti.get(mti_id, [])
        else:
            mti_out = None

        # verses
        vr_out = vr_by_ti.get(ti_id, [])

        # _meta: empty tables
        empty: list[str] = []
        if mp_out is None:       empty.append("meaning_parsed")
        if not mp_out or not mp_out.get("senses"): empty.append("meaning_senses")
        if not mp_out or not mp_out.get("stems"):  empty.append("meaning_stems")
        if lsj_out is None:      empty.append("lsj_parsed")
        if not dqf_out:          empty.append("quality_flags")
        if not p2f_out:          empty.append("phase2_flags")
        if not rw_out:           empty.append("related_words")
        if not rf_out:           empty.append("root_family")
        if mti_out is None:      empty.append("mti")
        if mti_out and not mti_out.get("cross_refs"): empty.append("mti_cross_refs")
        if mti_out and not mti_out.get("flags"):      empty.append("mti_flags")
        if not vr_out:           empty.append("verses")

        term_out = dict(ti)
        term_out["_meta"]          = {"empty_tables": empty}
        term_out["meaning_parsed"] = mp_out
        term_out["lsj_parsed"]     = lsj_out
        term_out["quality_flags"]  = dqf_out
        term_out["phase2_flags"]   = p2f_out
        term_out["related_words"]  = rw_out
        term_out["root_family"]    = rf_out
        term_out["mti"]            = mti_out
        term_out["verses"]         = vr_out

        terms_out.append(term_out)

    # ── final document ────────────────────────────────────────────────────────
    return {
        "_export": {
            "word":           word,
            "registry":       registry_id,
            "scope":          "full",
            "exported_at":    datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "schema_version": schema_ver,
        },
        "registry":             reg,
        "files":                files,
        "run_history":          run_history,
        "cross_registry_links": cross_links,
        "statistics":           statistics,
        "terms":                terms_out,
    }
