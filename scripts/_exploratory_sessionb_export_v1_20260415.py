"""
_exploratory_sessionb_export_v1_20260415.py
────────────────────────────────────────────
EXPLORATORY — NOT YET PRODUCTION.

Implements wa-global-sessionb-export-spec-v1.1-20260415.json for a single
registry. Derived from analytics/word_export.py; extended to cover all spec
sections including post-2026-04-15 schema additions:
  - session_b_findings (all 20 fields incl. 9 lifecycle + status + term_id)
  - wa_finding_entity_links (junction table, with delete_flagged)
  - wa_finding_catalogue_links (finding-to-question mapping)
  - wa_obs_question_catalogue (observation question catalogue)
  - wa_term_phase2_flags (with delete_flagged, obsolete_reason)
  - verse_context_groups with dimension_assignment, anchor_verses, related_verses
  - set_aside_verses
  - wa_session_b_dimensions (consistency check target)
  - dimension_review_log
  - deleted_terms (separate section)
  - session_research_flags split by session_target with category lookup
  - correlation_signals (per-registry slice derived from programme extract)
  - statistics block — all fields from spec + catalogue counts

Usage:
    python scripts/_exploratory_sessionb_export_v1_20260415.py --registry=23 \
        --out=data/exports/sessionb_spec_v1_1/

Governed by: wa-global-sessionb-export-spec-v1_1-20260415.json
Feeds back to Claude AI for interactive spec refinement — do not incorporate
into apply_session_patch or production pipelines without review.
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "bible_research.db"
DEFAULT_OUT = PROJECT_ROOT / "data" / "exports" / "sessionb_spec_v1_1"
CORR_FILE = PROJECT_ROOT / "data" / "exports" / "session_d" / "wa-correlations-2026-04-09.json"


# ── helpers ──────────────────────────────────────────────────────────────────

def _row(r): return dict(r) if r else None
def _rows(rs): return [dict(r) for r in rs]
def _in_clause(ids):
    if not ids:
        return "(NULL)", []
    return "({})".format(",".join("?" * len(ids))), list(ids)


# ── main ─────────────────────────────────────────────────────────────────────

def build_export(conn: sqlite3.Connection, registry_no: int, export_version: int = 1) -> dict:
    """Build a Session B v5.0 spec-compliant export for one registry."""

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    today = datetime.now(timezone.utc).strftime("%Y%m%d")

    # ──────────────────────────────────────────────────────────────────────────
    # 1. registry + meta
    # ──────────────────────────────────────────────────────────────────────────
    reg = _row(conn.execute(
        "SELECT * FROM word_registry WHERE no = ?", (registry_no,)
    ).fetchone())
    if not reg:
        raise ValueError(f"No word_registry entry for no={registry_no}")

    registry_id = reg["id"]
    word = reg["word"]

    schema_ver_row = conn.execute(
        "SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1"
    ).fetchone()
    schema_ver = schema_ver_row["version_code"] if schema_ver_row else "unknown"

    meta = {
        "export_version": export_version,
        "export_date": today,
        "registry_no": registry_no,
        "word": word,
        "scope": "full",
        "schema_version": schema_ver,
        "instruction_version": "exploratory-sessionb-export-spec-v1.1-20260415",
        "generated_at": now_utc,
        "generator": "scripts/_exploratory_sessionb_export_v1_20260415.py",
    }

    # ──────────────────────────────────────────────────────────────────────────
    # 2. file_index
    # ──────────────────────────────────────────────────────────────────────────
    files = _rows(conn.execute(
        "SELECT * FROM wa_file_index WHERE word_registry_fk = ? ORDER BY part_number",
        (registry_id,)
    ).fetchall())
    file_ids = [f["id"] for f in files]
    file_ids_sql, file_ids_params = _in_clause(file_ids)

    # ──────────────────────────────────────────────────────────────────────────
    # 3. terms: active + deleted
    # ──────────────────────────────────────────────────────────────────────────
    all_ti_rows = []
    if file_ids:
        all_ti_rows = _rows(conn.execute(
            f"SELECT * FROM wa_term_inventory WHERE file_id IN {file_ids_sql} ORDER BY strongs_number",
            file_ids_params
        ).fetchall())

    ti_ids = [t["id"] for t in all_ti_rows]
    ti_strongs = list({t["strongs_number"] for t in all_ti_rows if t["strongs_number"]})
    ti_ids_sql, ti_ids_params = _in_clause(ti_ids)
    strongs_sql, strongs_params = _in_clause(ti_strongs)

    # mti_terms lookup (prefer rows owned by this registry)
    mti_by_strongs = {}
    if ti_strongs:
        for r in conn.execute(
            f"SELECT * FROM mti_terms WHERE strongs_number IN {strongs_sql} "
            "ORDER BY CASE WHEN owning_registry_fk = ? THEN 0 "
            "              WHEN owning_registry = ? THEN 0 "
            "              ELSE 1 END",
            strongs_params + [registry_id, str(registry_no)]
        ).fetchall():
            if r["strongs_number"] not in mti_by_strongs:
                mti_by_strongs[r["strongs_number"]] = dict(r)
    mti_ids = [m["id"] for m in mti_by_strongs.values()]
    mti_ids_sql, mti_ids_params = _in_clause(mti_ids)

    # meaning_parsed
    mp_by_ti = {}
    if ti_ids:
        for r in conn.execute(
            f"SELECT * FROM wa_meaning_parsed WHERE term_inv_id IN {ti_ids_sql}",
            ti_ids_params
        ).fetchall():
            mp_by_ti[r["term_inv_id"]] = dict(r)
    mp_ids = [m["id"] for m in mp_by_ti.values()]
    mp_ids_sql, mp_ids_params = _in_clause(mp_ids)

    # meaning_sense
    sense_by_mp = {}
    if mp_ids:
        for r in conn.execute(
            f"SELECT * FROM wa_meaning_sense WHERE parsed_meaning_id IN {mp_ids_sql} ORDER BY sort_order",
            mp_ids_params
        ).fetchall():
            sense_by_mp.setdefault(r["parsed_meaning_id"], []).append(dict(r))

    # meaning_stem
    stem_by_mp = {}
    if mp_ids:
        for r in conn.execute(
            f"SELECT * FROM wa_meaning_stem WHERE parsed_meaning_id IN {mp_ids_sql}",
            mp_ids_params
        ).fetchall():
            stem_by_mp.setdefault(r["parsed_meaning_id"], []).append(dict(r))

    # lsj_parsed
    lsj_by_ti = {}
    if ti_ids:
        for r in conn.execute(
            f"SELECT * FROM wa_lsj_parsed WHERE term_inv_id IN {ti_ids_sql}",
            ti_ids_params
        ).fetchall():
            lsj_by_ti[r["term_inv_id"]] = dict(r)

    # quality flags (engine-derived, by term strongs)
    dqf_by_term = {}
    if file_ids:
        for r in conn.execute(
            f"""SELECT f.term_id, ft.flag_code, ft.flag_group, ft.description AS flag_desc,
                       f.description AS detail, f.last_changed
                FROM wa_data_quality_flags f
                JOIN wa_quality_flag_types ft ON ft.id = f.flag_id
                WHERE f.file_id IN {file_ids_sql}""",
            file_ids_params
        ).fetchall():
            dqf_by_term.setdefault(r["term_id"], []).append({
                "flag_code": r["flag_code"], "flag_group": r["flag_group"],
                "description": r["flag_desc"], "detail": r["detail"],
                "last_changed": r["last_changed"]
            })

    # phase2 flags (by ti_id) — includes SC-02 fields: delete_flagged, obsolete_reason
    p2f_by_ti = {}
    if ti_ids:
        for r in conn.execute(
            f"""SELECT p.term_inv_id, p.flag_id, ft.flag_code, ft.description AS type_desc,
                       p.description AS instance_desc, p.source, p.raised_date,
                       p.delete_flagged, p.obsolete_reason
                FROM wa_term_phase2_flags p
                JOIN phase2_flag_types ft ON ft.id = p.flag_id
                WHERE p.term_inv_id IN {ti_ids_sql}""",
            ti_ids_params
        ).fetchall():
            p2f_by_ti.setdefault(r["term_inv_id"], []).append({
                "flag_id": r["flag_id"], "flag_code": r["flag_code"],
                "description": r["instance_desc"] or r["type_desc"],
                "source": r["source"], "raised_date": r["raised_date"],
                "delete_flagged": r["delete_flagged"],
                "obsolete_reason": r["obsolete_reason"],
            })

    # mti_term_flags
    mti_flags_by_mti = {}
    if mti_ids:
        for r in conn.execute(
            f"""SELECT mf.mti_term_id, mf.flag_id, ft.flag_code, ft.description
                FROM mti_term_flags mf
                JOIN phase2_flag_types ft ON ft.id = mf.flag_id
                WHERE mf.mti_term_id IN {mti_ids_sql}""",
            mti_ids_params
        ).fetchall():
            mti_flags_by_mti.setdefault(r["mti_term_id"], []).append({
                "flag_id": r["flag_id"], "flag_code": r["flag_code"],
                "description": r["description"],
            })

    # related words
    rw_by_ti = {}
    if ti_ids:
        for r in conn.execute(
            f"SELECT * FROM wa_term_related_words WHERE term_inv_id IN {ti_ids_sql}",
            ti_ids_params
        ).fetchall():
            rw_by_ti.setdefault(r["term_inv_id"], []).append({
                "gloss": r["gloss"], "transliteration": r["transliteration"],
                "strongs_number": r["strongs_number"], "relationship_note": r["relationship_note"]
            })

    # mti_term_cross_refs
    mti_xref_by_mti = {}
    if mti_ids:
        for r in conn.execute(
            f"SELECT * FROM mti_term_cross_refs WHERE mti_term_id IN {mti_ids_sql}",
            mti_ids_params
        ).fetchall():
            mti_xref_by_mti.setdefault(r["mti_term_id"], []).append(dict(r))

    # root family
    rf_by_ti = {}
    if ti_ids:
        for r in conn.execute(
            f"SELECT * FROM wa_term_root_family WHERE term_inv_id IN {ti_ids_sql}",
            ti_ids_params
        ).fetchall():
            rf_by_ti.setdefault(r["term_inv_id"], []).append(dict(r))

    # Partition into active / deleted
    active_terms = []
    deleted_terms = []

    for ti in all_ti_rows:
        ti_id = ti["id"]
        strong = ti["strongs_number"]
        mti_entry = mti_by_strongs.get(strong) or {}
        is_deleted = ti.get("delete_flagged") == 1 or (mti_entry.get("status") == "delete")

        mp = mp_by_ti.get(ti_id)
        if mp:
            mp_out = dict(mp)
            mp_out["senses"] = sense_by_mp.get(mp["id"], [])
            mp_out["stems"] = stem_by_mp.get(mp["id"], [])
        else:
            mp_out = None

        term_record = dict(ti)
        term_record.update({
            "mti_term_id": mti_entry.get("id"),
            "mti_status": mti_entry.get("status"),
            "mti_gloss": mti_entry.get("gloss"),
            "owning_registry_no": mti_entry.get("owning_registry"),
            "owning_registry_word": mti_entry.get("owning_word"),
            "quality_flags": dqf_by_term.get(ti.get("term_id") or strong, []),
            "phase2_flags": p2f_by_ti.get(ti_id, []),
            "mti_flags": mti_flags_by_mti.get(mti_entry.get("id"), []),
            "related_words": rw_by_ti.get(ti_id, []),
            "mti_cross_refs": mti_xref_by_mti.get(mti_entry.get("id"), []),
            "meaning_parse": {
                "wa_meaning_parsed": mp_out,
                "wa_meaning_sense": (mp_out or {}).get("senses", []) if mp_out else [],
                "wa_meaning_stem": (mp_out or {}).get("stems", []) if mp_out else [],
            },
            "root_family": rf_by_ti.get(ti_id, []),
            "lsj_parse": lsj_by_ti.get(ti_id),
        })

        if is_deleted:
            deleted_terms.append({
                "term_inv_id": ti_id,
                "strongs_number": strong,
                "transliteration": ti.get("transliteration"),
                "gloss": mti_entry.get("gloss") or ti.get("step_search_gloss"),
                "mti_status": mti_entry.get("status"),
                "delete_flagged": ti.get("delete_flagged"),
                "term_owner_type": ti.get("term_owner_type"),
                "phase2_flags": p2f_by_ti.get(ti_id, []),
            })
        else:
            active_terms.append(term_record)

    # ──────────────────────────────────────────────────────────────────────────
    # 4. verse_records_summary (per-term aggregates; do NOT pull full verses here)
    # ──────────────────────────────────────────────────────────────────────────
    verse_summary = []
    if ti_ids:
        for r in conn.execute(
            f"""SELECT ti.strongs_number,
                       SUM(CASE WHEN vr.delete_flagged = 0 THEN 1 ELSE 0 END) AS total_verse_records,
                       SUM(CASE WHEN vr.span_strong_match = 1 THEN 1 ELSE 0 END) AS span_match_count,
                       SUM(CASE WHEN vr.delete_flagged = 1 THEN 1 ELSE 0 END) AS delete_flagged_count,
                       GROUP_CONCAT(DISTINCT b.name) AS book_coverage
                FROM wa_term_inventory ti
                LEFT JOIN wa_verse_records vr ON vr.term_inv_id = ti.id
                LEFT JOIN books b ON b.id = vr.book_id
                WHERE ti.id IN {ti_ids_sql}
                GROUP BY ti.strongs_number""",
            ti_ids_params
        ).fetchall():
            verse_summary.append(dict(r))

    # ──────────────────────────────────────────────────────────────────────────
    # 5. verse_context_groups (OWNER terms with dimension + anchor/related verses)
    # ──────────────────────────────────────────────────────────────────────────
    # Find mti_term_ids owned by THIS registry (for OWNER VC work)
    owner_mti_ids = []
    for m in mti_by_strongs.values():
        if m.get("owning_registry_fk") == registry_id or m.get("owning_registry") == str(registry_no):
            owner_mti_ids.append(m["id"])
    owner_sql, owner_params = _in_clause(owner_mti_ids)

    vc_groups = []
    if owner_mti_ids:
        group_rows = _rows(conn.execute(
            f"""SELECT vcg.id AS group_id, vcg.mti_term_id, vcg.group_code,
                       vcg.context_description, vcg.notes, vcg.delete_flagged,
                       vcg.vertical_pass_flag,
                       wdi.id AS dim_id, wdi.dimension, wdi.dimension_confidence,
                       wdi.manual_override, wdi.dominant_subject, wdi.notes AS dim_notes,
                       wdi.anchor_count, wdi.related_count, wdi.set_aside_count,
                       wdi.total_verse_count, wdi.last_modified AS dim_last_modified
                FROM verse_context_group vcg
                LEFT JOIN wa_dimension_index wdi ON wdi.verse_context_group_id = vcg.id
                WHERE vcg.mti_term_id IN {owner_sql}
                  AND vcg.delete_flagged = 0
                ORDER BY vcg.group_code""",
            owner_params
        ).fetchall())

        group_ids = [g["group_id"] for g in group_rows]
        group_sql, group_params = _in_clause(group_ids)

        # Load all verses for these groups in one pass, then split by anchor/related
        verses_by_group = {}
        if group_ids:
            for r in conn.execute(
                f"""SELECT vc.id AS vc_id, vc.group_id, vc.verse_record_id, vc.mti_term_id,
                           vc.is_anchor, vc.is_relevant, vc.is_related,
                           vc.notes AS vc_notes, vc.set_aside_reason, vc.vertical_pass_flag,
                           vc.delete_flagged,
                           vr.reference, vr.verse_text, vr.target_word, vr.span_strong_match
                    FROM verse_context vc
                    LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
                    WHERE vc.group_id IN {group_sql} AND vc.delete_flagged = 0""",
                group_params
            ).fetchall():
                verses_by_group.setdefault(r["group_id"], []).append(dict(r))

        for g in group_rows:
            gid = g["group_id"]
            verses = verses_by_group.get(gid, [])
            anchors = [v for v in verses if v["is_anchor"] == 1]
            related = [v for v in verses if v["is_related"] == 1]
            vc_groups.append({
                "group_id": gid,
                "mti_term_id": g["mti_term_id"],
                "group_code": g["group_code"],
                "context_description": g["context_description"],
                "notes": g["notes"],
                "delete_flagged": g["delete_flagged"],
                "vertical_pass_flag": g["vertical_pass_flag"],
                "dimension_assignment": {
                    "dimension_index_id": g["dim_id"],
                    "dimension": g["dimension"],
                    "dimension_confidence": g["dimension_confidence"],
                    "manual_override": g["manual_override"],
                    "dominant_subject": g["dominant_subject"],
                    "notes": g["dim_notes"],
                    "anchor_count": g["anchor_count"],
                    "related_count": g["related_count"],
                    "set_aside_count": g["set_aside_count"],
                    "total_verse_count": g["total_verse_count"],
                    "last_modified": g["dim_last_modified"],
                } if g["dim_id"] else None,
                "anchor_verses": [
                    {
                        "verse_context_id": v["vc_id"],
                        "verse_record_id": v["verse_record_id"],
                        "mti_term_id": v["mti_term_id"],
                        "reference": v["reference"],
                        "verse_text": v["verse_text"],
                        "target_word": v["target_word"],
                        "span_strong_match": v["span_strong_match"],
                        "is_anchor": v["is_anchor"],
                        "is_relevant": v["is_relevant"],
                        "is_related": v["is_related"],
                        "notes": v["vc_notes"],
                        "set_aside_reason": v["set_aside_reason"],
                        "vertical_pass_flag": v["vertical_pass_flag"],
                        "delete_flagged": v["delete_flagged"],
                    } for v in anchors
                ],
                "related_verses": [
                    {
                        "verse_context_id": v["vc_id"],
                        "verse_record_id": v["verse_record_id"],
                        "reference": v["reference"],
                        "verse_text": v["verse_text"],
                        "target_word": v["target_word"],
                        "notes": v["vc_notes"],
                    } for v in related
                ],
            })

    # ──────────────────────────────────────────────────────────────────────────
    # 6. set_aside_verses (OWNER terms, is_relevant=0)
    # ──────────────────────────────────────────────────────────────────────────
    set_aside = []
    if owner_mti_ids:
        for r in conn.execute(
            f"""SELECT vc.id AS vc_id, mt.strongs_number, vc.mti_term_id,
                       vr.reference, vr.verse_text, vc.set_aside_reason, vc.notes
                FROM verse_context vc
                JOIN mti_terms mt ON mt.id = vc.mti_term_id
                LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
                WHERE vc.mti_term_id IN {owner_sql}
                  AND vc.is_relevant = 0 AND vc.delete_flagged = 0""",
            owner_params
        ).fetchall():
            set_aside.append({
                "verse_context_id": r["vc_id"],
                "strongs_number": r["strongs_number"],
                "mti_term_id": r["mti_term_id"],
                "reference": r["reference"],
                "verse_text": r["verse_text"],
                "set_aside_reason": r["set_aside_reason"],
                "notes": r["notes"],
            })

    # ──────────────────────────────────────────────────────────────────────────
    # 7. session_b_findings (all rows incl. deleted)
    # ──────────────────────────────────────────────────────────────────────────
    findings = _rows(conn.execute(
        "SELECT * FROM wa_session_b_findings WHERE registry_id = ? ORDER BY finding_id",
        (registry_id,)
    ).fetchall())

    # ──────────────────────────────────────────────────────────────────────────
    # 8. finding_entity_links for findings in this registry
    # ──────────────────────────────────────────────────────────────────────────
    finding_ids = [f["id"] for f in findings]
    finding_sql, finding_params = _in_clause(finding_ids)
    finding_links = []
    if finding_ids:
        finding_links = _rows(conn.execute(
            f"SELECT * FROM wa_finding_entity_links WHERE finding_id IN {finding_sql}",
            finding_params
        ).fetchall())

    # ──────────────────────────────────────────────────────────────────────────
    # 8b. finding_catalogue_links (finding-to-question mapping, SC-04)
    # ──────────────────────────────────────────────────────────────────────────
    catalogue_links = []
    if finding_ids:
        catalogue_links = _rows(conn.execute(
            f"""SELECT fcl.*, oq.question_code, oq.section, oq.question_text,
                       oq.scope AS question_scope, oq.source_word
                FROM wa_finding_catalogue_links fcl
                JOIN wa_obs_question_catalogue oq ON oq.obs_id = fcl.question_id
                WHERE fcl.finding_id IN {finding_sql} AND fcl.delete_flagged = 0""",
            finding_params
        ).fetchall())

    # ──────────────────────────────────────────────────────────────────────────
    # 8c. observation_question_catalogue (SC-03)
    #     Two views: registry-scoped (this word's questions) and master (full 194)
    # ──────────────────────────────────────────────────────────────────────────
    obs_registry = _rows(conn.execute(
        """SELECT * FROM wa_obs_question_catalogue
           WHERE deleted = 0
             AND source_registry_no = ?
           ORDER BY obs_id""",
        (registry_id,)
    ).fetchall())

    obs_master = _rows(conn.execute(
        """SELECT * FROM wa_obs_question_catalogue
           WHERE deleted = 0
           ORDER BY obs_id"""
    ).fetchall())

    # ──────────────────────────────────────────────────────────────────────────
    # 9. session_b_dimensions (consistency check)
    # ──────────────────────────────────────────────────────────────────────────
    sb_dims = _rows(conn.execute(
        "SELECT * FROM wa_session_b_dimensions WHERE registry_id = ?",
        (registry_id,)
    ).fetchall())

    # ──────────────────────────────────────────────────────────────────────────
    # 10. session_research_flags split by session_target + category lookup
    # ──────────────────────────────────────────────────────────────────────────
    raw_flags = _rows(conn.execute(
        """SELECT srf.*, qft.category, wr.word AS cross_registry_word
           FROM wa_session_research_flags srf
           LEFT JOIN wa_quality_flag_types qft ON qft.flag_code = srf.flag_code
           LEFT JOIN word_registry wr ON wr.id = srf.cross_registry_id
           WHERE srf.registry_id = ?
           ORDER BY srf.flag_label""",
        (registry_id,)
    ).fetchall())
    sb_flags = [f for f in raw_flags if f.get("session_target") == "B"]
    sd_pointers = [f for f in raw_flags if f.get("session_target") == "D"]
    other_flags = [f for f in raw_flags if f.get("session_target") not in ("B", "D")]

    # ──────────────────────────────────────────────────────────────────────────
    # 11. dimension_review_log
    # ──────────────────────────────────────────────────────────────────────────
    dim_log = None
    cluster = reg.get("cluster_assignment")
    if cluster:
        dim_log = _row(conn.execute(
            "SELECT * FROM wa_dim_review_cluster_log WHERE cluster = ?", (cluster,)
        ).fetchone())

    # ──────────────────────────────────────────────────────────────────────────
    # 12. cross_registry_links (Session A era)
    # ──────────────────────────────────────────────────────────────────────────
    cross_links = []
    if file_ids:
        cross_links = _rows(conn.execute(
            f"""SELECT crl.*, ct.type_code, ct.description AS link_type_description
                FROM wa_cross_registry_links crl
                JOIN wa_crosslink_type ct ON ct.id = crl.connection_type_id
                WHERE crl.file_id IN {file_ids_sql}
                ORDER BY crl.linked_word""",
            file_ids_params
        ).fetchall())

    # ──────────────────────────────────────────────────────────────────────────
    # 13. correlation_signals (per-registry slice from programme-wide extract)
    # ──────────────────────────────────────────────────────────────────────────
    correlations = {
        "source": "external file (programme-wide extract)",
        "path": str(CORR_FILE.relative_to(PROJECT_ROOT)) if CORR_FILE.exists() else None,
        "slice": None,
    }
    if CORR_FILE.exists():
        try:
            with open(CORR_FILE, "r", encoding="utf-8") as f:
                corr_data = json.load(f)
            correlations["source_metadata"] = corr_data.get("_extract_meta")
            # ranked_pairs: top-N pairs across all signals — filter to those touching this registry
            ranked = corr_data.get("ranked_pairs", [])
            reg_ranked = [p for p in ranked if p.get("reg1") == registry_no or p.get("reg2") == registry_no]
            # signals: dict of signal_type -> list of pairs (or dict). Slice each list to pairs touching this registry.
            signals = corr_data.get("signals", {})
            reg_signals = {}
            for sig_name, sig_data in signals.items():
                if isinstance(sig_data, list):
                    reg_signals[sig_name] = [
                        p for p in sig_data
                        if p.get("reg1") == registry_no or p.get("reg2") == registry_no
                        or p.get("registry_no") == registry_no
                    ]
                elif isinstance(sig_data, dict):
                    reg_signals[sig_name] = sig_data.get(str(registry_no))
            correlations["slice"] = {
                "ranked_pairs": reg_ranked,
                "signals": reg_signals,
            }
            correlations["slice_counts"] = {
                "ranked_pairs": len(reg_ranked),
                **{k: (len(v) if isinstance(v, list) else 0) for k, v in reg_signals.items()},
            }
        except Exception as e:
            correlations["error"] = str(e)

    # ──────────────────────────────────────────────────────────────────────────
    # 14. patch_history (engine_run_log + word_run_state)
    # ──────────────────────────────────────────────────────────────────────────
    engine_runs = _rows(conn.execute(
        """SELECT erl.run_id, erl.mode, erl.started_at, erl.completed_at, erl.outcome,
                  erl.total_terms_new, erl.total_verses_inserted, erl.error_detail
           FROM engine_run_log erl
           WHERE erl.target_registry_ids = ? OR erl.target_registry_ids = ?
              OR erl.run_id LIKE ?
           ORDER BY erl.started_at DESC LIMIT 50""",
        (str(registry_no), registry_no, f"%-{registry_no:03d}-%")
    ).fetchall())

    word_states = _rows(conn.execute(
        """SELECT run_id, phase_reached, audit_result, audit_detail, stop_reason,
                  researcher_approved, approved_at
           FROM word_run_state
           WHERE registry_id = ?
           ORDER BY id DESC LIMIT 50""",
        (str(registry_no),)
    ).fetchall())

    # ──────────────────────────────────────────────────────────────────────────
    # 15. statistics — all 24 from spec
    # ──────────────────────────────────────────────────────────────────────────
    def count_sql(sql, params=()):
        r = conn.execute(sql, params).fetchone()
        return r[0] if r else 0

    # god_as_subject consistency counts: compare wa_term_inventory vs mti_term_flags
    gas_inv = 0
    gas_mti = 0
    som_inv = 0
    som_mti = 0
    if ti_ids:
        gas_inv = count_sql(
            f"SELECT COUNT(*) FROM wa_term_inventory WHERE id IN {ti_ids_sql} AND god_as_subject = 1 AND delete_flagged = 0",
            ti_ids_params
        )
        som_inv = count_sql(
            f"SELECT COUNT(*) FROM wa_term_inventory WHERE id IN {ti_ids_sql} AND somatic_link = 1 AND delete_flagged = 0",
            ti_ids_params
        )
    # FIX (DIR-008): use owning_registry_fk on mti_terms rather than mti_ids
    # collected via the inventory join. The inventory-based filter undercounted
    # because mti_terms with owning_registry_fk = N can exist without a
    # corresponding wa_term_inventory row in this registry's file_index slice
    # (verified against compassion: inventory join returned 4, owning_registry_fk
    # returned 9 — DIR-007 Q3 result).
    gas_mti = count_sql(
        """SELECT COUNT(*) FROM mti_term_flags mf
           JOIN phase2_flag_types ft ON ft.id = mf.flag_id
           JOIN mti_terms mt ON mt.id = mf.mti_term_id
           WHERE mt.owning_registry_fk = ? AND ft.flag_code = 'GOD_AS_SUBJECT'""",
        (registry_id,)
    )
    som_mti = count_sql(
        """SELECT COUNT(*) FROM mti_term_flags mf
           JOIN phase2_flag_types ft ON ft.id = mf.flag_id
           JOIN mti_terms mt ON mt.id = mf.mti_term_id
           WHERE mt.owning_registry_fk = ? AND ft.flag_code = 'SOMATIC_INNER_LINK'""",
        (registry_id,)
    )

    # Counts for groups
    active_group_count = 0
    groups_no_dim = 0
    groups_automated = 0
    groups_no_dom_subj = 0
    if owner_mti_ids:
        active_group_count = count_sql(
            f"""SELECT COUNT(*) FROM verse_context_group
                WHERE mti_term_id IN {owner_sql} AND delete_flagged = 0""",
            owner_params
        )
        groups_no_dim = count_sql(
            f"""SELECT COUNT(*) FROM verse_context_group vcg
                LEFT JOIN wa_dimension_index wdi ON wdi.verse_context_group_id = vcg.id
                WHERE vcg.mti_term_id IN {owner_sql} AND vcg.delete_flagged = 0
                  AND (wdi.dimension IS NULL OR wdi.id IS NULL)""",
            owner_params
        )
        groups_automated = count_sql(
            f"""SELECT COUNT(*) FROM verse_context_group vcg
                JOIN wa_dimension_index wdi ON wdi.verse_context_group_id = vcg.id
                WHERE vcg.mti_term_id IN {owner_sql} AND vcg.delete_flagged = 0
                  AND wdi.dimension_confidence = 'AUTOMATED'""",
            owner_params
        )
        groups_no_dom_subj = count_sql(
            f"""SELECT COUNT(*) FROM verse_context_group vcg
                LEFT JOIN wa_dimension_index wdi ON wdi.verse_context_group_id = vcg.id
                WHERE vcg.mti_term_id IN {owner_sql} AND vcg.delete_flagged = 0
                  AND (wdi.dominant_subject IS NULL)""",
            owner_params
        )

    total_anchor = sum(len(g["anchor_verses"]) for g in vc_groups)
    total_related = sum(len(g["related_verses"]) for g in vc_groups)

    statistics = {
        "active_owner_term_count": len([t for t in active_terms if t.get("term_owner_type") == "OWNER"]),
        "active_xref_term_count": len([t for t in active_terms if t.get("term_owner_type") == "XREF"]),
        "null_owner_type_count": len([t for t in active_terms if not t.get("term_owner_type")]),
        "deleted_term_count": len(deleted_terms),
        "total_anchor_verses": total_anchor,
        "total_related_verses": total_related,
        "total_set_aside_verses": len(set_aside),
        "active_group_count": active_group_count,
        "groups_without_dimension": groups_no_dim,
        "groups_at_automated_confidence": groups_automated,
        "groups_without_dominant_subject": groups_no_dom_subj,
        "terms_without_meaning_parse": len([t for t in active_terms if not t.get("parsed_meaning_id")]),
        "terms_without_mti_cross_refs": len([t for t in active_terms if not t.get("mti_cross_refs")]),
        "active_session_b_findings": len([f for f in findings if f.get("delete_flag") == 0]),
        "thin_evidence_findings": len([f for f in findings if f.get("thin_evidence") == 1]),
        "session_b_flags_unresolved": len([f for f in sb_flags if f.get("resolved") == 0]),
        "sd_pointers_raised": len(sd_pointers),
        "phase2_flags_total": sum(len(t.get("phase2_flags", [])) for t in active_terms),
        "god_as_subject_inventory_count": gas_inv,
        "god_as_subject_mti_flag_count": gas_mti,
        "somatic_link_inventory_count": som_inv,
        "somatic_link_mti_flag_count": som_mti,
        "session_b_dimensions_rows": len(sb_dims),
        "root_family_gap_count": len([
            t for t in active_terms
            if t.get("term_owner_type") == "OWNER" and not t.get("root_family")
        ]),
        "phase2_flags_deleted": sum(
            1 for t in active_terms
            for f in t.get("phase2_flags", []) if f.get("delete_flagged") == 1
        ),
        "catalogue_questions_master": len(obs_master),
        "catalogue_questions_registry": len(obs_registry),
        "catalogue_links_total": len(catalogue_links),
        "catalogue_links_validated": len([l for l in catalogue_links if l.get("status") == "validated"]),
        "findings_with_term_id": len([f for f in findings if f.get("term_id") is not None]),
        "findings_by_status": {
            s: len([f for f in findings if f.get("status") == s])
            for s in sorted({f.get("status") for f in findings})
        },
    }

    # ──────────────────────────────────────────────────────────────────────────
    # Assemble full export
    # ──────────────────────────────────────────────────────────────────────────
    return {
        "meta": meta,
        "registry": reg,
        "file_index": files,
        "terms": {
            "active_terms": active_terms,
            "deleted_terms": deleted_terms,
        },
        "verse_records_summary": verse_summary,
        "verse_context_groups": vc_groups,
        "set_aside_verses": set_aside,
        "session_b_findings": findings,
        "finding_entity_links": finding_links,
        "finding_catalogue_links": catalogue_links,
        "observation_question_catalogue": {
            "_meta": {
                "description": "Observation-Question Master Catalogue and registry-scoped subset",
                "master_catalogue": (
                    "wa_obs_question_catalogue — all active questions across all source words. "
                    "Each question has a question_code (Q001–Q147 universal, plus word-specific "
                    "prefixed by source initial: F-nnn forgiveness, L-nnn love, M-nnn mercy, "
                    "C-nnn compassion). scope='universal' questions apply to every word; "
                    "scope='word_specific' were formulated for one word but may transfer."
                ),
                "registry_questions": (
                    "Subset of master_catalogue where source_registry_no matches this registry. "
                    "These are the word-specific questions originating from this word's analysis. "
                    "Empty for registries whose words have not yet been through Session B."
                ),
                "finding_catalogue_links": (
                    "wa_finding_catalogue_links — many-to-many junction linking "
                    "wa_session_b_findings.id to wa_obs_question_catalogue.obs_id. "
                    "coverage (FULL/PARTIAL) indicates how completely a finding addresses "
                    "its linked question. status tracks the mapping lifecycle: "
                    "suggested → validated → rejected."
                ),
            },
            "master_catalogue": obs_master,
            "registry_questions": obs_registry,
        },
        "session_b_dimensions": sb_dims,
        "session_research_flags": {
            "session_b_flags": sb_flags,
            "sd_pointers": sd_pointers,
            "other_flags": other_flags,
        },
        "dimension_review_log": dim_log,
        "cross_registry_links": cross_links,
        "correlation_signals": correlations,
        "patch_history": {
            "engine_runs": engine_runs,
            "word_run_states": word_states,
        },
        "statistics": statistics,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--registry", type=int, required=True)
    p.add_argument("--out", type=str, default=str(DEFAULT_OUT))
    p.add_argument("--version", type=int, default=1)
    args = p.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    export = build_export(conn, args.registry, args.version)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    word = export["meta"]["word"]
    date = export["meta"]["export_date"]
    fname = f"wa-{args.registry:03d}-{word}-sessionb-export-v{args.version}-{date}.json"
    out_path = out_dir / fname

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(export, f, indent=2, ensure_ascii=False)

    stats = export["statistics"]
    print(f"Written: {out_path}")
    print(f"Size:    {out_path.stat().st_size:,} bytes")
    print()
    print("Statistics snapshot:")
    for k, v in stats.items():
        print(f"  {k:40s} {v}")
    print()
    counts = {
        "active_terms": len(export["terms"]["active_terms"]),
        "deleted_terms": len(export["terms"]["deleted_terms"]),
        "vc_groups": len(export["verse_context_groups"]),
        "session_b_findings": len(export["session_b_findings"]),
        "finding_entity_links": len(export["finding_entity_links"]),
        "finding_catalogue_links": len(export["finding_catalogue_links"]),
        "obs_catalogue_master": len(export["observation_question_catalogue"]["master_catalogue"]),
        "obs_catalogue_registry": len(export["observation_question_catalogue"]["registry_questions"]),
        "cross_registry_links": len(export["cross_registry_links"]),
        "session_b_flags": len(export["session_research_flags"]["session_b_flags"]),
        "sd_pointers": len(export["session_research_flags"]["sd_pointers"]),
    }
    print("Section counts:")
    for k, v in counts.items():
        print(f"  {k:40s} {v}")


if __name__ == "__main__":
    main()
