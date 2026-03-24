"""
audit_word.py (v2)
──────────────────
AUDIT_WORD mode — redesigned steps Pre-A1 through A10.

Input: Step 1 JSON file produced by scripts/word_study_extract.py
       data/discovery/{registry_no:03d}_{word}_step_data_{YYYYMMDD}.json
       The latest file for the word is auto-selected unless --extract-file given.

Key behaviours
──────────────
• Auto-approve by default — all INSERT / UPDATE / SET delete_flagged actions
  are applied without per-item gates. Use --interactive to enable the gate.
• STALE fields are updated automatically in auto mode.
• Quality flags (wa_data_quality_flags) are FULLY RESET and re-derived from
  STEP data each run. Phase 2 flags (wa_term_phase2_flags) are NOT touched.
• No rows are physically deleted — deletions are flagged with delete_flagged=1.
  A separate ARCHIVE mode performs actual deletion.
• word_registry.last_automation_run is set to 'AUDITED' on completion.
• word_run_state.approved_by is set to 'PROVISIONAL' (audit is not full sign-off).

Steps
─────
  Pre-A1  Lock sentinel + open run log
  A1      Registry display + CONFIRM prompt
  A2      DB snapshot (Word Extract Report) + structural completeness check
  A3      Load + validate latest Step 1 JSON
  A4      Build gap report (Term / Related / Verse / VTL streams)
  A5      Display gap report (+ interactive approve gate if --interactive)
  A6      Apply changes (all streams, one transaction per stream)
  A7      Meaning handler (parse from JSON; migrate ~33 legacy term-field records)
  A8      Quality flag full reset + re-derive from STEP data
  A9      Audit checks WR-01–WR-20 + write word_run_state (PROVISIONAL)
  A10     Registry + file index update, close run, set last_automation_run = 'AUDITED'
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys
from datetime import datetime, timezone
from typing import Any

_ROOT = os.path.join(os.path.dirname(__file__), "..")
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from .constants import EXPECTED_SCHEMA_VERSION, LOCK_SENTINEL, AUDITED_SENTINEL
from .db import get_schema_version, get_book_id
from .audit import run_audit
from .flag_engine import run_flag_engine
from .meaning_parser import run_parser_for_file
from .run_log import (
    make_run_id, open_run, close_run,
    write_word_run_state, upsert_checkpoint,
)

_DISCOVERY_DIR = os.path.join(_ROOT, "data", "discovery")
_SEP = "═" * 66


# ─────────────────────────────────────────────────────────────────────────────
# Utility helpers
# ─────────────────────────────────────────────────────────────────────────────

def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _norm(s: Any) -> str:
    """Normalise a text value for comparison: collapse whitespace."""
    if s is None:
        return ""
    return " ".join(str(s).split()).strip()


def _cov(testaments: set) -> str | None:
    """Compute testament_coverage label."""
    if not testaments:
        return None
    if testaments == {"OT"}:
        return "OT_only"
    if testaments == {"NT"}:
        return "NT_only"
    return "both"


def _box(title: str, lines: list[str]) -> None:
    print(f"╔{_SEP}")
    print(f"║  {title}")
    print(f"╠{_SEP}")
    for ln in lines:
        print(f"║  {ln}")
    print(f"╚{_SEP}")


# ─────────────────────────────────────────────────────────────────────────────
# File discovery
# ─────────────────────────────────────────────────────────────────────────────

def _find_latest_extract(registry_id_int: int, word: str) -> str | None:
    """Return path to the most recent Step 1 JSON for this word, or None."""
    reg_no     = str(registry_id_int).zfill(3)
    word_lower = word.lower().replace(" ", "_")
    # Prefer registry-prefixed naming: 182_soul_step_data_20260323.json
    files = sorted(glob.glob(
        os.path.join(_DISCOVERY_DIR, f"{reg_no}_{word_lower}_step_data_*.json")
    ))
    if not files:
        # Fall back to legacy naming: soul_step_data_20260323.json
        files = sorted(glob.glob(
            os.path.join(_DISCOVERY_DIR, f"{word_lower}_step_data_*.json")
        ))
    return files[-1] if files else None


# ─────────────────────────────────────────────────────────────────────────────
# DB snapshot loader
# ─────────────────────────────────────────────────────────────────────────────

def _load_snapshot(conn, file_ids: list[int], registry_id_int: int) -> dict:
    """Read all 16 affected tables into memory. Returns keyed snapshot dict."""
    fid_ph = ",".join("?" * len(file_ids))

    # ── Terms ────────────────────────────────────────────────────────────────
    term_rows = conn.execute(
        f"SELECT * FROM wa_term_inventory WHERE file_id IN ({fid_ph})", file_ids
    ).fetchall()
    terms_by_id      = {r["id"]: dict(r) for r in term_rows}
    terms_by_strongs = {}
    for r in term_rows:
        key = r["strongs_number"] or r["term_id"]
        if key:
            terms_by_strongs[key] = dict(r)

    term_ids = list(terms_by_id.keys())
    ti_ph    = ",".join("?" * len(term_ids)) if term_ids else "NULL"

    # ── Related words ─────────────────────────────────────────────────────────
    related_by_ti: dict[int, list] = {}
    if term_ids:
        for r in conn.execute(
            f"SELECT * FROM wa_term_related_words WHERE term_inv_id IN ({ti_ph})", term_ids
        ).fetchall():
            related_by_ti.setdefault(r["term_inv_id"], []).append(dict(r))

    # ── Root family ───────────────────────────────────────────────────────────
    root_by_ti: dict[int, list] = {}
    if term_ids:
        for r in conn.execute(
            f"SELECT * FROM wa_term_root_family WHERE term_inv_id IN ({ti_ph})", term_ids
        ).fetchall():
            root_by_ti.setdefault(r["term_inv_id"], []).append(dict(r))

    # ── Phase 2 flags ─────────────────────────────────────────────────────────
    p2flags_by_ti: dict[int, list] = {}
    if term_ids:
        for r in conn.execute(
            f"SELECT * FROM wa_term_phase2_flags WHERE term_inv_id IN ({ti_ph})", term_ids
        ).fetchall():
            p2flags_by_ti.setdefault(r["term_inv_id"], []).append(dict(r))

    # ── Quality flags ─────────────────────────────────────────────────────────
    qflag_rows = conn.execute(
        f"SELECT * FROM wa_data_quality_flags WHERE file_id IN ({fid_ph})", file_ids
    ).fetchall()

    # ── Cross-registry links ──────────────────────────────────────────────────
    xlink_rows = conn.execute(
        f"SELECT * FROM wa_cross_registry_links WHERE file_id IN ({fid_ph})", file_ids
    ).fetchall()

    # ── MTI terms ─────────────────────────────────────────────────────────────
    mti_rows = conn.execute(
        "SELECT * FROM mti_terms WHERE owning_registry = ?", (str(registry_id_int),)
    ).fetchall()
    mti_by_strongs = {r["strongs_number"]: dict(r) for r in mti_rows if r["strongs_number"]}
    mti_ids = [r["id"] for r in mti_rows]
    mti_ph  = ",".join("?" * len(mti_ids)) if mti_ids else "NULL"

    # ── MTI flags ─────────────────────────────────────────────────────────────
    mti_flags_by_id: dict[int, list] = {}
    if mti_ids:
        for r in conn.execute(
            f"SELECT * FROM mti_term_flags WHERE mti_term_id IN ({mti_ph})", mti_ids
        ).fetchall():
            mti_flags_by_id.setdefault(r["mti_term_id"], []).append(dict(r))

    # ── MTI cross-refs ────────────────────────────────────────────────────────
    mti_xrefs_by_id: dict[int, list] = {}
    if mti_ids:
        for r in conn.execute(
            f"SELECT * FROM mti_term_cross_refs WHERE mti_term_id IN ({mti_ph})", mti_ids
        ).fetchall():
            mti_xrefs_by_id.setdefault(r["mti_term_id"], []).append(dict(r))

    # ── Meaning parsed ────────────────────────────────────────────────────────
    mp_by_ti: dict[int, dict] = {}
    mp_ids: list[int] = []
    if term_ids:
        mp_rows = conn.execute(
            f"SELECT * FROM wa_meaning_parsed WHERE term_inv_id IN ({ti_ph})", term_ids
        ).fetchall()
        mp_by_ti = {r["term_inv_id"]: dict(r) for r in mp_rows}
        mp_ids   = [r["id"] for r in mp_rows]

    mp_ph = ",".join("?" * len(mp_ids)) if mp_ids else "NULL"
    sense_count = (conn.execute(
        f"SELECT COUNT(*) AS c FROM wa_meaning_sense WHERE parsed_meaning_id IN ({mp_ph})", mp_ids
    ).fetchone()["c"] if mp_ids else 0)
    stem_count = (conn.execute(
        f"SELECT COUNT(*) AS c FROM wa_meaning_stem WHERE parsed_meaning_id IN ({mp_ph})", mp_ids
    ).fetchone()["c"] if mp_ids else 0)

    # ── LSJ parsed ────────────────────────────────────────────────────────────
    lsj_by_ti: dict[int, dict] = {}
    if term_ids:
        for r in conn.execute(
            f"SELECT * FROM wa_lsj_parsed WHERE term_inv_id IN ({ti_ph})", term_ids
        ).fetchall():
            lsj_by_ti[r["term_inv_id"]] = dict(r)

    # ── Verse records ─────────────────────────────────────────────────────────
    vr_rows = conn.execute(
        f"SELECT * FROM wa_verse_records WHERE file_id IN ({fid_ph})", file_ids
    ).fetchall()
    vr_by_ti_ref: dict[tuple, dict] = {}
    vr_by_id: dict[int, dict] = {}
    for r in vr_rows:
        vr_by_ti_ref[(r["term_inv_id"], r["reference"])] = dict(r)
        vr_by_id[r["id"]] = dict(r)

    vr_ids = list(vr_by_id.keys())
    vr_ph  = ",".join("?" * len(vr_ids)) if vr_ids else "NULL"

    # ── Verse term links ──────────────────────────────────────────────────────
    vtl_by_key: dict[tuple, dict] = {}
    if vr_ids:
        for r in conn.execute(
            f"SELECT * FROM wa_verse_term_links WHERE verse_id IN ({vr_ph})", vr_ids
        ).fetchall():
            vtl_by_key[(r["verse_id"], r["term_inv_id"])] = dict(r)

    return {
        "terms_by_id":      terms_by_id,
        "terms_by_strongs": terms_by_strongs,
        "term_ids":         term_ids,
        "related_by_ti":    related_by_ti,
        "root_by_ti":       root_by_ti,
        "p2flags_by_ti":    p2flags_by_ti,
        "qflags":           [dict(r) for r in qflag_rows],
        "xlinks":           [dict(r) for r in xlink_rows],
        "mti_by_strongs":   mti_by_strongs,
        "mti_ids":          mti_ids,
        "mti_flags_by_id":  mti_flags_by_id,
        "mti_xrefs_by_id":  mti_xrefs_by_id,
        "mp_by_ti":         mp_by_ti,
        "mp_ids":           mp_ids,
        "sense_count":      sense_count,
        "stem_count":       stem_count,
        "lsj_by_ti":        lsj_by_ti,
        "vr_by_ti_ref":     vr_by_ti_ref,
        "vr_by_id":         vr_by_id,
        "vr_ids":           vr_ids,
        "vtl_by_key":       vtl_by_key,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Display helpers
# ─────────────────────────────────────────────────────────────────────────────

def _display_registry_row(row: dict) -> None:
    lines = [
        f"{k:<28}: {v}"
        for k, v in row.items()
        if v is not None and k not in ("notes",)
    ]
    _box(f"Registry Entry — {row.get('word','?')}  "
         f"(id={row.get('id')}  no={row.get('no')})", lines)


def _display_word_extract_report(snapshot: dict, file_ids: list[int]) -> None:
    p2 = sum(len(v) for v in snapshot["p2flags_by_ti"].values())
    rw = sum(len(v) for v in snapshot["related_by_ti"].values())
    rf = sum(len(v) for v in snapshot["root_by_ti"].values())
    mf = sum(len(v) for v in snapshot["mti_flags_by_id"].values())
    mx = sum(len(v) for v in snapshot["mti_xrefs_by_id"].values())
    vtl_note = "  ← will be populated in A6" if not snapshot["vtl_by_key"] else ""
    lines = [
        f"wa_file_index           : {len(file_ids)} row(s)",
        f"wa_term_inventory       : {len(snapshot['terms_by_id'])} row(s)",
        f"wa_term_related_words   : {rw} row(s)",
        f"wa_term_root_family     : {rf} row(s)",
        f"wa_term_phase2_flags    : {p2} row(s)  [NOT touched by audit]",
        f"wa_data_quality_flags   : {len(snapshot['qflags'])} row(s)  [will be RESET in A8]",
        f"wa_cross_registry_links : {len(snapshot['xlinks'])} row(s)  [read-only, FK verified]",
        f"mti_terms               : {len(snapshot['mti_by_strongs'])} row(s)",
        f"mti_term_flags          : {mf} row(s)  [read-only]",
        f"mti_term_cross_refs     : {mx} row(s)  [read-only]",
        f"wa_meaning_parsed       : {len(snapshot['mp_by_ti'])} row(s)",
        f"wa_meaning_sense        : {snapshot['sense_count']} row(s)",
        f"wa_meaning_stem         : {snapshot['stem_count']} row(s)",
        f"wa_lsj_parsed           : {len(snapshot['lsj_by_ti'])} row(s)",
        f"wa_verse_records        : {len(snapshot['vr_by_id'])} row(s)",
        f"wa_verse_term_links     : {len(snapshot['vtl_by_key'])} row(s){vtl_note}",
    ]
    _box("WORD EXTRACT REPORT", lines)


# ─────────────────────────────────────────────────────────────────────────────
# Gap report builder
# ─────────────────────────────────────────────────────────────────────────────

# STEP-owned term fields compared for STALE_TERM: (db_column, json_field)
_TERM_STALE_FIELDS: list[tuple[str, str]] = [
    ("transliteration",   "transliteration"),
    ("step_search_gloss", "gloss"),
    ("occurrence_count",  "vocab_count"),
    ("lsj_entry",         "lsj_entry"),
    ("short_def_mounce",  "short_def_mounce"),
]

# STEP-owned verse fields compared for STALE_VERSE: (db_column, json_field)
_VERSE_STALE_FIELDS: list[tuple[str, str]] = [
    ("verse_text",        "esv_text"),
    ("target_word",       "target_word"),
    ("span_strong_match", "span_strong_match"),
    ("context_before",    "context_before"),
    ("context_after",     "context_after"),
]

# VTL span fields compared for STALE_VTL: (vtl_column, json_field)
_VTL_STALE_FIELDS: list[tuple[str, str]] = [
    ("step_subgloss_code",  "span_code_found"),
    ("step_subgloss_label", "span_label_found"),
    ("span_strong_match",   "span_strong_match"),
    ("target_word",         "target_word"),
]


def _build_gap_report(snapshot: dict, include_terms: list[dict]) -> dict:
    """Compare JSON include_terms against DB snapshot across all streams."""
    include_codes = {t["code"] for t in include_terms}

    gap: dict[str, list] = {
        "NEW_TERM":        [],
        "STALE_TERM":      [],
        "MISSING_MTI":     [],
        "DB_ONLY_TERM":    [],
        "MISSING_RELATED": [],
        "ORPHAN_RELATED":  [],
        "MISSING_VERSE":   [],
        "ORPHAN_VERSE":    [],
        "STALE_VERSE":     [],
        "MISSING_VTL":     [],
        "STALE_VTL":       [],
        "MISSING_ROOT":    [],
    }

    terms_by_strongs = snapshot["terms_by_strongs"]
    related_by_ti    = snapshot["related_by_ti"]
    mti_by_strongs   = snapshot["mti_by_strongs"]
    vr_by_ti_ref     = snapshot["vr_by_ti_ref"]
    vtl_by_key       = snapshot["vtl_by_key"]
    root_by_ti       = snapshot["root_by_ti"]

    for jt in include_terms:
        code = jt["code"]
        ti   = terms_by_strongs.get(code)

        if ti is None:
            gap["NEW_TERM"].append({"code": code, "term_rec": jt})
            continue

        ti_id = ti["id"]

        # ── STALE_TERM: compare STEP-owned fields ─────────────────────────────
        changes = []
        for db_field, json_field in _TERM_STALE_FIELDS:
            db_val   = ti.get(db_field)
            json_val = jt.get(json_field)
            if db_field == "occurrence_count":
                if (db_val or 0) != (json_val or 0):
                    changes.append({"field": db_field, "old": db_val, "new": json_val})
            else:
                if _norm(db_val) != _norm(json_val):
                    changes.append({"field": db_field, "old": db_val, "new": json_val})
        if changes:
            gap["STALE_TERM"].append({"code": code, "ti_id": ti_id, "changes": changes})

        # ── MTI check ─────────────────────────────────────────────────────────
        if code not in mti_by_strongs:
            gap["MISSING_MTI"].append({"code": code, "ti_id": ti_id})

        # ── Root family check ─────────────────────────────────────────────────
        if not root_by_ti.get(ti_id):
            gap["MISSING_ROOT"].append({"ti_id": ti_id, "code": code})

        # ── Related words ─────────────────────────────────────────────────────
        db_rw_strongs   = {r["strongs_number"] for r in related_by_ti.get(ti_id, [])
                           if r.get("strongs_number")}
        json_rw_strongs = {r["strong"] for r in jt.get("related_words", []) if r.get("strong")}

        for strong in json_rw_strongs - db_rw_strongs:
            jrw = next((r for r in jt.get("related_words", []) if r["strong"] == strong), {})
            gap["MISSING_RELATED"].append({
                "ti_id": ti_id, "code": code,
                "strong": strong, "gloss": jrw.get("gloss", ""),
                "translit": jrw.get("translit", ""),
            })
        for rw in related_by_ti.get(ti_id, []):
            if rw.get("strongs_number") and rw["strongs_number"] not in json_rw_strongs:
                gap["ORPHAN_RELATED"].append({
                    "ti_id": ti_id, "rw_id": rw["id"],
                    "strong": rw["strongs_number"],
                })

        # ── Verse stream ──────────────────────────────────────────────────────
        json_refs = {v["ref"] for v in jt.get("verses", [])}
        db_refs   = {
            ref for (tid, ref), vr in vr_by_ti_ref.items()
            if tid == ti_id and not vr.get("delete_flagged")
        }

        for jv in jt.get("verses", []):
            ref = jv["ref"]
            vr  = vr_by_ti_ref.get((ti_id, ref))

            if vr is None:
                gap["MISSING_VERSE"].append({
                    "ti_id": ti_id, "code": code, "ref": ref, "verse_rec": jv,
                })
            else:
                if vr.get("delete_flagged"):
                    # Previously flagged — treat as missing (unflag + update)
                    gap["MISSING_VERSE"].append({
                        "ti_id": ti_id, "code": code, "ref": ref, "verse_rec": jv,
                    })
                    continue

                vr_id = vr["id"]

                # STALE_VERSE: compare STEP fields
                vchanges = []
                for db_f, jf in _VERSE_STALE_FIELDS:
                    dv   = vr.get(db_f)
                    jval = jv.get(jf)
                    if db_f == "span_strong_match":
                        if (dv or 0) != (jval or 0):
                            vchanges.append({"field": db_f, "old": dv, "new": jval})
                    else:
                        if _norm(dv) != _norm(jval):
                            vchanges.append({"field": db_f, "old": dv, "new": jval})
                if vchanges:
                    gap["STALE_VERSE"].append({
                        "ti_id": ti_id, "code": code, "ref": ref,
                        "vr_id": vr_id, "changes": vchanges,
                    })

                # VTL check
                vtl = vtl_by_key.get((vr_id, ti_id))
                span_data = {
                    "span_code_found":  jv.get("span_code_found"),
                    "span_label_found": jv.get("span_label_found"),
                    "span_strong_match": jv.get("span_strong_match"),
                    "target_word":      jv.get("target_word"),
                }
                if vtl is None:
                    gap["MISSING_VTL"].append({
                        "vr_id": vr_id, "ti_id": ti_id,
                        "code": code, "ref": ref, "span_data": span_data,
                    })
                else:
                    vtl_changes = []
                    for vtl_f, jf in _VTL_STALE_FIELDS:
                        dv   = vtl.get(vtl_f)
                        jval = jv.get(jf)
                        if vtl_f == "span_strong_match":
                            if (dv or 0) != (jval or 0):
                                vtl_changes.append({"field": vtl_f, "old": dv, "new": jval})
                        else:
                            if _norm(dv) != _norm(jval):
                                vtl_changes.append({"field": vtl_f, "old": dv, "new": jval})
                    if vtl_changes:
                        gap["STALE_VTL"].append({
                            "vtl_id": vtl.get("id"), "vr_id": vr_id,
                            "ti_id": ti_id, "changes": vtl_changes,
                        })

        # ORPHAN_VERSE: in DB (active), not in JSON
        for ref in db_refs - json_refs:
            vr = vr_by_ti_ref.get((ti_id, ref))
            if vr:
                gap["ORPHAN_VERSE"].append({
                    "ti_id": ti_id, "code": code, "ref": ref, "vr_id": vr["id"],
                })

    # ── DB_ONLY_TERM: in DB but not in JSON include_codes ────────────────────
    for strongs, ti in snapshot["terms_by_strongs"].items():
        if strongs not in include_codes and not ti.get("delete_flagged"):
            vc = sum(
                1 for (tid, _), vr in snapshot["vr_by_ti_ref"].items()
                if tid == ti["id"] and not vr.get("delete_flagged")
            )
            gap["DB_ONLY_TERM"].append({
                "code":  strongs,
                "ti_id": ti["id"],
                "verse_count": vc,
                "gloss": ti.get("step_search_gloss", "") or ti.get("word_analysis_gloss", ""),
            })

    return gap


# ─────────────────────────────────────────────────────────────────────────────
# Gap report display
# ─────────────────────────────────────────────────────────────────────────────

def _display_gap_report(gap: dict, word: str, json_date: str) -> None:
    all_ok = all(not v for v in gap.values())
    lines = [
        f"Word: {word}   JSON date: {json_date}",
        "",
        "── STREAM 1 ─── TERMS ───────────────────────────────",
        f"  NEW_TERM        : {len(gap['NEW_TERM'])}",
        f"  STALE_TERM      : {len(gap['STALE_TERM'])}",
        f"  MISSING_MTI     : {len(gap['MISSING_MTI'])}",
        f"  DB_ONLY_TERM    : {len(gap['DB_ONLY_TERM'])}",
        f"  MISSING_ROOT    : {len(gap['MISSING_ROOT'])}  [info only — no auto-fix]",
        "",
        "── STREAM 1b ─── RELATED WORDS ──────────────────────",
        f"  MISSING_RELATED : {len(gap['MISSING_RELATED'])}",
        f"  ORPHAN_RELATED  : {len(gap['ORPHAN_RELATED'])}",
        "",
        "── STREAM 2 ─── VERSE RECORDS ───────────────────────",
        f"  MISSING_VERSE   : {len(gap['MISSING_VERSE'])}",
        f"  ORPHAN_VERSE    : {len(gap['ORPHAN_VERSE'])}",
        f"  STALE_VERSE     : {len(gap['STALE_VERSE'])}",
        "",
        "── STREAM 2b ─── VERSE_TERM_LINKS ───────────────────",
        f"  MISSING_VTL     : {len(gap['MISSING_VTL'])}",
        f"  STALE_VTL       : {len(gap['STALE_VTL'])}",
        "",
        ("✓ All streams clean — no changes required." if all_ok else
         f"Total changes: {sum(len(v) for v in gap.values())} item(s) across all streams."),
    ]

    # Detail for key categories (first 5 items each)
    if gap["STALE_TERM"]:
        lines.append("")
        lines.append("  STALE_TERM detail:")
        for item in gap["STALE_TERM"][:5]:
            for ch in item["changes"][:2]:
                lines.append(
                    f"    {item['code']:12} {ch['field']}: "
                    f"{str(ch['old'])[:25]!r} → {str(ch['new'])[:25]!r}"
                )
        if len(gap["STALE_TERM"]) > 5:
            lines.append(f"    ... ({len(gap['STALE_TERM']) - 5} more STALE_TERM)")

    if gap["DB_ONLY_TERM"]:
        lines.append("")
        lines.append("  DB_ONLY_TERM (will be flagged for deletion):")
        for item in gap["DB_ONLY_TERM"]:
            lines.append(
                f"    {item['code']:12} ({item.get('gloss',''):<20}) "
                f"{item['verse_count']} verse(s)"
            )

    if gap["MISSING_VERSE"]:
        lines.append("")
        lines.append("  MISSING_VERSE (sample):")
        for item in gap["MISSING_VERSE"][:5]:
            lines.append(f"    {item['code']:12} {item['ref']}")
        if len(gap["MISSING_VERSE"]) > 5:
            lines.append(f"    ... ({len(gap['MISSING_VERSE']) - 5} more)")

    _box("GAP REPORT", lines)


# ─────────────────────────────────────────────────────────────────────────────
# Interactive gate
# ─────────────────────────────────────────────────────────────────────────────

def _interactive_gate(gap: dict) -> dict[str, bool]:
    """Print approve/skip prompts for each non-empty gap category."""
    approvals: dict[str, bool] = {}
    print(f"\n{'─'*68}")
    print("  REVIEW GATE — approve/skip per category  (Enter = Yes)")
    print(f"{'─'*68}")
    prompts = [
        ("STALE_TERM",      f"Update {len(gap['STALE_TERM'])} STALE_TERM record(s)?"),
        ("DB_ONLY_TERM",    f"Flag {len(gap['DB_ONLY_TERM'])} DB_ONLY_TERM for deletion?"),
        ("MISSING_MTI",     f"Insert {len(gap['MISSING_MTI'])} MISSING_MTI row(s) into mti_terms?"),
        ("MISSING_RELATED", f"Insert {len(gap['MISSING_RELATED'])} MISSING_RELATED word(s)?"),
        ("ORPHAN_RELATED",  f"Flag {len(gap['ORPHAN_RELATED'])} ORPHAN_RELATED for deletion?"),
        ("MISSING_VERSE",   f"Insert {len(gap['MISSING_VERSE'])} MISSING_VERSE record(s)?"),
        ("ORPHAN_VERSE",    f"Flag {len(gap['ORPHAN_VERSE'])} ORPHAN_VERSE for deletion?"),
        ("STALE_VERSE",     f"Update {len(gap['STALE_VERSE'])} STALE_VERSE record(s)?"),
        ("MISSING_VTL",     f"Insert {len(gap['MISSING_VTL'])} MISSING_VTL link(s)?"),
        ("STALE_VTL",       f"Update {len(gap['STALE_VTL'])} STALE_VTL link(s)?"),
        ("NEW_TERM",        f"Insert {len(gap['NEW_TERM'])} NEW_TERM record(s)?"),
    ]
    any_non_zero = False
    for key, label in prompts:
        if not gap[key]:
            approvals[key] = False
            continue
        any_non_zero = True
        ans = input(f"  {label:<58} [Y/n]: ").strip().lower()
        approvals[key] = ans in ("", "y", "yes")
    if not any_non_zero:
        print("  (all gap lists are empty)")
    print(f"{'─'*68}\n")
    return approvals


def _auto_approve(gap: dict) -> dict[str, bool]:
    """Auto-approve all non-empty categories."""
    return {k: bool(v) for k, v in gap.items() if isinstance(v, list)}


# ─────────────────────────────────────────────────────────────────────────────
# Apply changes — sub-helpers
# ─────────────────────────────────────────────────────────────────────────────

def _refresh_related_words(conn, ti_id: int, jt: dict,
                            now: str, errors: list[str]) -> None:
    """Delete all existing related_words for this term and re-insert from JSON."""
    try:
        conn.execute("DELETE FROM wa_term_related_words WHERE term_inv_id = ?", (ti_id,))
        for rw in jt.get("related_words", []):
            conn.execute(
                "INSERT INTO wa_term_related_words "
                "(term_inv_id, strongs_number, gloss, transliteration) VALUES (?, ?, ?, ?)",
                (ti_id, rw.get("strong"), rw.get("gloss"), rw.get("translit")),
            )
    except Exception as exc:
        errors.append(f"refresh_related_words ti={ti_id}: {exc}")


def _insert_new_term(conn, jt: dict, file_id: int, str_reg: str,
                     now: str, today: str, counts: dict,
                     errors: list[str]) -> int | None:
    """Insert NEW_TERM into wa_term_inventory + wa_term_related_words + mti_terms.
    Returns new term_inv_id, or None on failure."""
    code = jt["code"]
    lang = "Hebrew" if code.startswith("H") else "Greek"
    try:
        conn.execute(
            """INSERT INTO wa_term_inventory
                   (file_id, language, term_id, strongs_number,
                    transliteration, step_search_gloss, word_analysis_gloss,
                    occurrence_count, meaning, meaning_numbered,
                    lsj_entry, short_def_mounce, last_changed)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                file_id, lang, code, code,
                jt.get("transliteration"), jt.get("gloss"), jt.get("gloss"),
                jt.get("vocab_count"),
                jt.get("medium_def") or None,
                1 if jt.get("meaning_numbered") else 0,
                jt.get("lsj_entry") or None,
                jt.get("short_def_mounce") or None,
                now,
            ),
        )
        new_ti_id = conn.execute("SELECT last_insert_rowid() AS r").fetchone()["r"]
        counts["total_terms_new"] = counts.get("total_terms_new", 0) + 1

        for rw in jt.get("related_words", []):
            conn.execute(
                "INSERT INTO wa_term_related_words "
                "(term_inv_id, strongs_number, gloss, transliteration) VALUES (?, ?, ?, ?)",
                (new_ti_id, rw.get("strong"), rw.get("gloss"), rw.get("translit")),
            )
        conn.execute(
            """INSERT INTO mti_terms
                   (strongs_number, transliteration, gloss, language,
                    owning_registry, owning_word, extraction_date)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                code, jt.get("transliteration"), jt.get("gloss"), lang,
                str_reg, jt.get("gloss", ""), today,
            ),
        )
        return new_ti_id
    except Exception as exc:
        errors.append(f"NEW_TERM insert {code}: {exc}")
        return None


def _rederive_testaments(conn, ti_ids) -> None:
    """Recompute wa_term_inventory.testament for each term from confirmed active verses."""
    for ti_id in ti_ids:
        testaments = {
            r["testament"]
            for r in conn.execute(
                """SELECT DISTINCT testament FROM wa_verse_records
                   WHERE term_inv_id = ? AND span_strong_match = 1
                     AND (delete_flagged = 0 OR delete_flagged IS NULL)""",
                (ti_id,),
            ).fetchall()
        }
        tc = _cov(testaments)
        if tc:
            conn.execute(
                "UPDATE wa_term_inventory SET testament = ? WHERE id = ?", (tc, ti_id)
            )
    conn.commit()


# ─────────────────────────────────────────────────────────────────────────────
# A6 — Apply all approved changes
# ─────────────────────────────────────────────────────────────────────────────

def _apply_changes(
    conn,
    snapshot: dict,
    include_terms: list[dict],
    gap: dict,
    approvals: dict[str, bool],
    file_ids: list[int],
    registry_id_int: int,
    run_id: str,
    counts: dict,
    errors: list[str],
) -> None:
    """Apply all approved INSERT / UPDATE / SET delete_flagged operations."""
    primary_fid = file_ids[0]
    str_reg     = str(registry_id_int)
    now         = _now()
    today       = _today()

    # Build quick lookups from JSON
    jt_by_code: dict[str, dict] = {t["code"]: t for t in include_terms}
    jv_lookup:  dict[tuple, dict] = {}  # (code, ref) → verse_record
    for jt in include_terms:
        for jv in jt.get("verses", []):
            jv_lookup[(jt["code"], jv["ref"])] = jv

    # ── Stream 1: STALE_TERM update ──────────────────────────────────────────
    if approvals.get("STALE_TERM"):
        for item in gap["STALE_TERM"]:
            jt    = jt_by_code[item["code"]]
            ti_id = item["ti_id"]
            try:
                conn.execute(
                    """UPDATE wa_term_inventory SET
                           transliteration     = ?,
                           step_search_gloss   = ?,
                           word_analysis_gloss = ?,
                           occurrence_count    = ?,
                           lsj_entry           = ?,
                           short_def_mounce    = ?,
                           last_changed        = ?
                       WHERE id = ?""",
                    (
                        jt.get("transliteration"),
                        jt.get("gloss"),
                        jt.get("gloss"),
                        jt.get("vocab_count"),
                        jt.get("lsj_entry") or None,
                        jt.get("short_def_mounce") or None,
                        now, ti_id,
                    ),
                )
                # Refresh related words whenever term fields are updated
                _refresh_related_words(conn, ti_id, jt, now, errors)
            except Exception as exc:
                errors.append(f"STALE_TERM update {item['code']}: {exc}")

    # ── Stream 1: DB_ONLY_TERM → set delete_flagged ──────────────────────────
    if approvals.get("DB_ONLY_TERM"):
        for item in gap["DB_ONLY_TERM"]:
            try:
                conn.execute(
                    "UPDATE wa_term_inventory SET delete_flagged = 1 WHERE id = ?",
                    (item["ti_id"],),
                )
                # Cascade: root_family rows for this term
                conn.execute(
                    "UPDATE wa_term_root_family SET delete_flagged = 1 WHERE term_inv_id = ?",
                    (item["ti_id"],),
                )
            except Exception as exc:
                errors.append(f"DB_ONLY_TERM flag {item['code']}: {exc}")

    # ── Stream 1b: ORPHAN_RELATED → set delete_flagged ───────────────────────
    if approvals.get("ORPHAN_RELATED"):
        for item in gap["ORPHAN_RELATED"]:
            try:
                conn.execute(
                    "UPDATE wa_term_related_words SET delete_flagged = 1 WHERE id = ?",
                    (item["rw_id"],),
                )
            except Exception as exc:
                errors.append(f"ORPHAN_RELATED flag rw_id={item['rw_id']}: {exc}")

    # ── Stream 1b: MISSING_RELATED insert ────────────────────────────────────
    if approvals.get("MISSING_RELATED"):
        for item in gap["MISSING_RELATED"]:
            ti = snapshot["terms_by_strongs"].get(item["code"])
            if not ti:
                continue
            try:
                conn.execute(
                    "INSERT OR IGNORE INTO wa_term_related_words "
                    "(term_inv_id, strongs_number, gloss, transliteration) "
                    "VALUES (?, ?, ?, ?)",
                    (ti["id"], item["strong"], item.get("gloss"), item.get("translit")),
                )
            except Exception as exc:
                errors.append(f"MISSING_RELATED insert {item['strong']}: {exc}")

    # ── Stream 1: MISSING_MTI insert ─────────────────────────────────────────
    if approvals.get("MISSING_MTI"):
        for item in gap["MISSING_MTI"]:
            ti   = snapshot["terms_by_id"].get(item["ti_id"]) or {}
            code = item["code"]
            lang = "Hebrew" if code.startswith("H") else "Greek"
            try:
                conn.execute(
                    """INSERT OR IGNORE INTO mti_terms
                               (strongs_number, transliteration, gloss, language,
                                owning_registry, owning_word, extraction_date)
                           VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (
                        code,
                        ti.get("transliteration"),
                        ti.get("step_search_gloss") or ti.get("word_analysis_gloss"),
                        lang, str_reg,
                        ti.get("step_search_gloss") or code,
                        today,
                    ),
                )
            except Exception as exc:
                errors.append(f"MISSING_MTI insert {code}: {exc}")

    # ── Stream 1: NEW_TERM insert ─────────────────────────────────────────────
    new_ti_map: dict[str, int] = {}  # code → new ti_id (for verse inserts below)
    if approvals.get("NEW_TERM"):
        for item in gap["NEW_TERM"]:
            jt = item["term_rec"]
            new_ti_id = _insert_new_term(
                conn, jt, primary_fid, str_reg, now, today, counts, errors
            )
            if new_ti_id:
                new_ti_map[jt["code"]] = new_ti_id

    conn.commit()
    upsert_checkpoint(conn, run_id, "VOCAB_STREAM", "complete",
                      rows_written=len(gap["STALE_TERM"]) + len(new_ti_map))

    # ── Stream 2: MISSING_VERSE insert ────────────────────────────────────────
    if approvals.get("MISSING_VERSE"):
        for item in gap["MISSING_VERSE"]:
            jv    = item["verse_rec"]
            ti_id = item["ti_id"] or new_ti_map.get(item["code"])
            if not ti_id:
                errors.append(f"MISSING_VERSE: no ti_id for {item['code']} {item['ref']}")
                continue
            ti      = snapshot["terms_by_id"].get(ti_id) or {}
            book_id = get_book_id(conn, jv.get("book_code", ""))
            if book_id is None:
                errors.append(
                    f"MISSING_VERSE: unknown book {jv.get('book_code')!r} ({item['ref']})"
                )
                continue
            try:
                conn.execute(
                    """INSERT INTO wa_verse_records
                           (file_id, term_inv_id, term_id, transliteration,
                            book_id, reference, chapter, verse_num, testament,
                            translation, verse_text, target_word,
                            span_strong_match, context_before, context_after,
                            created_at)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'ESV', ?, ?, ?, ?, ?, ?)""",
                    (
                        primary_fid, ti_id,
                        ti.get("term_id") or item["code"],
                        ti.get("transliteration"),
                        book_id, jv["ref"],
                        jv.get("chapter"), jv.get("verse_num"), jv.get("testament"),
                        jv.get("esv_text", ""), jv.get("target_word"),
                        jv.get("span_strong_match"),
                        jv.get("context_before"), jv.get("context_after"),
                        now,
                    ),
                )
                new_vr_id = conn.execute(
                    "SELECT last_insert_rowid() AS r"
                ).fetchone()["r"]
                # Immediately create the VTL row for this new verse
                conn.execute(
                    """INSERT OR IGNORE INTO wa_verse_term_links
                           (verse_id, term_inv_id, step_subgloss_code,
                            step_subgloss_label, span_strong_match, target_word)
                       VALUES (?, ?, ?, ?, ?, ?)""",
                    (
                        new_vr_id, ti_id,
                        jv.get("span_code_found"),
                        jv.get("span_label_found"),
                        jv.get("span_strong_match"),
                        jv.get("target_word"),
                    ),
                )
                counts["total_verses_inserted"] += 1
            except Exception as exc:
                errors.append(f"MISSING_VERSE insert {item['ref']}: {exc}")

    # ── Stream 2: STALE_VERSE update ─────────────────────────────────────────
    if approvals.get("STALE_VERSE"):
        for item in gap["STALE_VERSE"]:
            jv = jv_lookup.get((item["code"], item["ref"]), {})
            try:
                conn.execute(
                    """UPDATE wa_verse_records SET
                           verse_text        = ?,
                           target_word       = ?,
                           span_strong_match = ?,
                           context_before    = ?,
                           context_after     = ?,
                           updated_at        = ?
                       WHERE id = ?""",
                    (
                        jv.get("esv_text"), jv.get("target_word"),
                        jv.get("span_strong_match"),
                        jv.get("context_before"), jv.get("context_after"),
                        now, item["vr_id"],
                    ),
                )
                counts["total_verses_updated"] = counts.get("total_verses_updated", 0) + 1
            except Exception as exc:
                errors.append(f"STALE_VERSE update {item['ref']}: {exc}")

    # ── Stream 2: ORPHAN_VERSE → set delete_flagged ───────────────────────────
    if approvals.get("ORPHAN_VERSE"):
        for item in gap["ORPHAN_VERSE"]:
            try:
                conn.execute(
                    "UPDATE wa_verse_records SET delete_flagged = 1 WHERE id = ?",
                    (item["vr_id"],),
                )
                counts["total_verses_filtered"] = counts.get("total_verses_filtered", 0) + 1
            except Exception as exc:
                errors.append(f"ORPHAN_VERSE flag {item['ref']}: {exc}")

    # ── Stream 2b: MISSING_VTL insert ────────────────────────────────────────
    if approvals.get("MISSING_VTL"):
        for item in gap["MISSING_VTL"]:
            sd = item["span_data"]
            try:
                conn.execute(
                    """INSERT OR IGNORE INTO wa_verse_term_links
                           (verse_id, term_inv_id, step_subgloss_code,
                            step_subgloss_label, span_strong_match, target_word)
                       VALUES (?, ?, ?, ?, ?, ?)""",
                    (
                        item["vr_id"], item["ti_id"],
                        sd.get("span_code_found"),
                        sd.get("span_label_found"),
                        sd.get("span_strong_match"),
                        sd.get("target_word"),
                    ),
                )
            except Exception as exc:
                errors.append(
                    f"MISSING_VTL insert vr={item['vr_id']} ti={item['ti_id']}: {exc}"
                )

    # ── Stream 2b: STALE_VTL update ──────────────────────────────────────────
    if approvals.get("STALE_VTL"):
        for item in gap["STALE_VTL"]:
            ti = snapshot["terms_by_id"].get(item["ti_id"])
            vr = snapshot["vr_by_id"].get(item["vr_id"])
            jv: dict = {}
            if ti and vr:
                code = ti.get("strongs_number") or ti.get("term_id", "")
                jv   = jv_lookup.get((code, vr.get("reference", "")), {})
            try:
                conn.execute(
                    """UPDATE wa_verse_term_links SET
                           step_subgloss_code  = ?,
                           step_subgloss_label = ?,
                           span_strong_match   = ?,
                           target_word         = ?
                       WHERE id = ?""",
                    (
                        jv.get("span_code_found"),
                        jv.get("span_label_found"),
                        jv.get("span_strong_match"),
                        jv.get("target_word"),
                        item["vtl_id"],
                    ),
                )
            except Exception as exc:
                errors.append(f"STALE_VTL update id={item['vtl_id']}: {exc}")

    conn.commit()
    upsert_checkpoint(conn, run_id, "VERSE_STREAM", "complete",
                      rows_written=counts["total_verses_inserted"],
                      rows_filtered=counts.get("total_verses_filtered", 0))
    upsert_checkpoint(conn, run_id, "VTL_STREAM", "complete",
                      rows_written=len(gap["MISSING_VTL"]))

    # ── Stream 3: Testament re-derivation per term ────────────────────────────
    all_ti_ids = list(snapshot["terms_by_id"].keys()) + list(new_ti_map.values())
    _rederive_testaments(conn, all_ti_ids)

    # ── Verify ────────────────────────────────────────────────────────────────
    for fid in file_ids:
        at = conn.execute(
            "SELECT COUNT(*) AS c FROM wa_term_inventory WHERE file_id = ? "
            "AND (delete_flagged = 0 OR delete_flagged IS NULL)", (fid,)
        ).fetchone()["c"]
        ft = conn.execute(
            "SELECT COUNT(*) AS c FROM wa_term_inventory "
            "WHERE file_id = ? AND delete_flagged = 1", (fid,)
        ).fetchone()["c"]
        av = conn.execute(
            "SELECT COUNT(*) AS c FROM wa_verse_records WHERE file_id = ? "
            "AND (delete_flagged = 0 OR delete_flagged IS NULL)", (fid,)
        ).fetchone()["c"]
        vtl_n = conn.execute(
            "SELECT COUNT(*) AS c FROM wa_verse_term_links vtl "
            "JOIN wa_verse_records vr ON vr.id = vtl.verse_id WHERE vr.file_id = ?",
            (fid,),
        ).fetchone()["c"]
        print(
            f"     [A6 VERIFY] file_id={fid}"
            f"  terms_active={at} (+{ft} delete_flagged)"
            f"  verses_active={av}"
            f"  vtl={vtl_n}"
        )


# ─────────────────────────────────────────────────────────────────────────────
# A7 — Meaning handler
# ─────────────────────────────────────────────────────────────────────────────

def _run_meaning_handler(conn, include_terms: list[dict], file_ids: list[int]) -> int:
    """Parse meanings from JSON; NULL legacy meaning fields once parsing succeeds."""
    # Build vocab_map from current JSON data (preferred over stale DB meaning field)
    vocab_map: dict[str, dict] = {}
    for jt in include_terms:
        md = jt.get("medium_def") or ""
        if md:
            vocab_map[jt["code"]] = {"medium_def": md}

    # Also include DB terms not in JSON (DB_ONLY terms may still have meaning text)
    fid_ph = ",".join("?" * len(file_ids))
    for row in conn.execute(
        f"SELECT strongs_number, term_id, meaning FROM wa_term_inventory "
        f"WHERE file_id IN ({fid_ph}) AND meaning IS NOT NULL",
        file_ids,
    ).fetchall():
        code = row["strongs_number"] or row["term_id"]
        if code and code not in vocab_map:
            vocab_map[code] = {"medium_def": row["meaning"]}

    parsed = 0
    for fid in file_ids:
        result = run_parser_for_file(conn, fid, vocab_map)
        parsed += result.get("parsed", 0)

    # Set parsed_meaning_id on each term
    for fid in file_ids:
        for row in conn.execute(
            "SELECT ti.id AS ti_id, mp.id AS mp_id "
            "FROM wa_term_inventory ti "
            "JOIN wa_meaning_parsed mp ON mp.term_inv_id = ti.id "
            "WHERE ti.file_id = ?",
            (fid,),
        ).fetchall():
            conn.execute(
                "UPDATE wa_term_inventory SET parsed_meaning_id = ? WHERE id = ?",
                (row["mp_id"], row["ti_id"]),
            )

    # Migrate legacy: NULL out meaning fields where parsing succeeded
    migrated = 0
    for fid in file_ids:
        for row in conn.execute(
            "SELECT ti.id AS ti_id, ti.strongs_number, mp.id AS mp_id "
            "FROM wa_term_inventory ti "
            "JOIN wa_meaning_parsed mp ON mp.term_inv_id = ti.id "
            "WHERE ti.file_id = ? AND ti.meaning IS NOT NULL",
            (fid,),
        ).fetchall():
            sense_ct = conn.execute(
                "SELECT COUNT(*) AS c FROM wa_meaning_sense WHERE parsed_meaning_id = ?",
                (row["mp_id"],),
            ).fetchone()["c"]
            if sense_ct > 0:
                conn.execute(
                    "UPDATE wa_term_inventory "
                    "SET meaning = NULL, meaning_numbered = NULL WHERE id = ?",
                    (row["ti_id"],),
                )
                print(
                    f"     [MIGRATED] {row['strongs_number']} — "
                    f"meaning → wa_meaning_parsed id={row['mp_id']}"
                )
                migrated += 1

    conn.commit()
    if migrated:
        print(f"     [A7] {migrated} legacy meaning record(s) migrated to meaning tables.")
    return parsed


# ─────────────────────────────────────────────────────────────────────────────
# A8 — Quality flag reset
# ─────────────────────────────────────────────────────────────────────────────

def _reset_quality_flags(conn, file_ids: list[int], registry_id_int: int) -> int:
    """Delete ALL quality flags for this file and re-derive from STEP data.
    Phase 2 flags (wa_term_phase2_flags) are NOT touched."""
    fid_ph = ",".join("?" * len(file_ids))
    conn.execute(
        f"DELETE FROM wa_data_quality_flags WHERE file_id IN ({fid_ph})", file_ids
    )
    conn.commit()

    total = 0
    for fid in file_ids:
        result = run_flag_engine(conn, fid, registry_id_int)
        total += result.get("flags_written", 0)
    return total


# ─────────────────────────────────────────────────────────────────────────────
# Main entry point
# ─────────────────────────────────────────────────────────────────────────────

def run_audit_word(
    conn,
    registry_id: int,
    dry_run: bool = False,
    interactive: bool = False,
    extract_file: str | None = None,
    skip_span_backpop: bool = False,   # deprecated; retained for CLI compat
) -> dict:
    """Execute AUDIT_WORD mode for a single registry entry.

    Args:
        conn:          Open database connection.
        registry_id:   word_registry.no for the target word.
        dry_run:       Show gap report only — no DB writes.
        interactive:   Enable per-category review gate (A5).
        extract_file:  Explicit path to Step 1 JSON; bypasses auto-select.
    """
    run_id  = make_run_id("AUDIT_WORD")
    errors: list[str] = []
    counts: dict = {
        "words_attempted":     1,
        "words_complete":      0,
        "words_stopped":       0,
        "total_terms_new":     0,
        "total_terms_xref":    0,
        "total_verses_inserted": 0,
        "total_verses_updated":  0,
        "total_verses_filtered": 0,
        "total_meanings_parsed": 0,
        "errors": errors,
    }

    def _stop(msg: str) -> dict:
        counts["words_stopped"] = 1
        errors.append(msg)
        print(f"\n  [STOP] {msg}")
        # Clear lock
        try:
            conn.execute(
                "UPDATE word_registry SET last_automation_run = NULL WHERE no = ?",
                (registry_id,),
            )
            conn.commit()
        except Exception:
            pass
        if not dry_run:
            try:
                close_run(conn, run_id, "STOPPED", counts)
            except Exception:
                pass
        return {
            "outcome": "STOPPED", "run_id": run_id,
            "audit_result": "STOP", "details": errors,
        }

    # ── Print run header ──────────────────────────────────────────────────────
    print(f"\n{'═'*68}")
    print(f"  AUDIT_WORD  |  run_id: {run_id}")
    mode_label = "DRY-RUN" if dry_run else ("INTERACTIVE" if interactive else "AUTO-APPROVE")
    print(f"  Registry:   {registry_id}  |  Mode: {mode_label}")
    print(f"{'═'*68}")

    # ── Pre-A1: Lock sentinel + open run ──────────────────────────────────────
    lock_row = conn.execute(
        "SELECT last_automation_run FROM word_registry WHERE no = ?", (registry_id,)
    ).fetchone()
    if lock_row and lock_row["last_automation_run"] == LOCK_SENTINEL:
        ans = input(
            f"  [LOCK] IN_PROGRESS sentinel is set. Override and continue? [y/N]: "
        ).strip().lower()
        if ans not in ("y", "yes"):
            return {
                "outcome": "ABORTED", "run_id": run_id,
                "audit_result": "ABORTED", "details": ["Stale lock not overridden."],
            }

    conn.execute(
        "UPDATE word_registry SET last_automation_run = ? WHERE no = ?",
        (LOCK_SENTINEL, registry_id),
    )
    conn.commit()

    if not dry_run:
        open_run(conn, run_id, "AUDIT_WORD", [registry_id])

    # ── A1: Registry display + CONFIRM ───────────────────────────────────────
    print("\nA1  Registry confirmation...")
    reg_row = conn.execute(
        "SELECT * FROM word_registry WHERE no = ?", (registry_id,)
    ).fetchone()
    if not reg_row:
        return _stop(f"A1: No word_registry row for no={registry_id}")

    word     = reg_row["word"]
    reg_dict = dict(reg_row)
    _display_registry_row(reg_dict)

    notes = reg_row["notes"]
    if notes:
        print(f"\n  ┌─ REGISTRY NOTES ──────────────────────────────────────────")
        for ln in notes.splitlines():
            print(f"  │  {ln}")
        print(f"  └──────────────────────────────────────────────────────────\n")

    # Look up file_index: try registry_id (as used by import) first, then id FK
    fi_rows = conn.execute(
        "SELECT id FROM wa_file_index WHERE registry_id = ?",
        (str(registry_id),),
    ).fetchall()
    if not fi_rows:
        fi_rows = conn.execute(
            "SELECT id FROM wa_file_index WHERE word_registry_fk = ?",
            (reg_row["id"],),
        ).fetchall()
    if not fi_rows:
        # Also try with the word_registry.id value in case no/id differ
        fi_rows = conn.execute(
            "SELECT id FROM wa_file_index WHERE registry_id = ?",
            (str(reg_row["id"]),),
        ).fetchall()

    if not fi_rows:
        return _stop(
            f"A1: No wa_file_index rows for registry {registry_id}. "
            "Run --mode=new_word first."
        )
    file_ids = [r["id"] for r in fi_rows]
    print(f"     Word: {word}  |  file_id(s): {file_ids}")

    confirm = input(
        f"\n  Type CONFIRM to proceed with audit of '{word}' (registry {registry_id}): "
    ).strip()
    if confirm != "CONFIRM":
        conn.execute(
            "UPDATE word_registry SET last_automation_run = NULL WHERE no = ?",
            (registry_id,),
        )
        conn.commit()
        print("  Audit aborted by researcher.")
        return {
            "outcome": "ABORTED", "run_id": run_id,
            "audit_result": "ABORTED", "details": ["Confirmation not given."],
        }

    # ── A2: DB snapshot + structural check ───────────────────────────────────
    print("\nA2  Loading DB snapshot (Word Extract Report)...")
    schema_ver = get_schema_version(conn)
    if schema_ver != EXPECTED_SCHEMA_VERSION:
        return _stop(
            f"A2: Schema version mismatch — found {schema_ver!r}, "
            f"expected {EXPECTED_SCHEMA_VERSION!r}. Run: python -m engine.engine --migrate"
        )

    snapshot = _load_snapshot(conn, file_ids, registry_id)
    _display_word_extract_report(snapshot, file_ids)

    # Structural completeness check
    exempt = {"COVERED", "REPLACED", "SPECIAL_HANDLING"}
    reg_status = (reg_row["phase1_status"] or "").strip().upper()
    if reg_status not in exempt:
        stop_reasons = []
        if not snapshot["terms_by_id"]:
            stop_reasons.append("wa_term_inventory is empty")
        if not snapshot["vr_by_id"]:
            stop_reasons.append("wa_verse_records is empty")
        if not snapshot["mti_by_strongs"]:
            stop_reasons.append("mti_terms is empty")
        if stop_reasons:
            return _stop(
                f"A2: Structural data missing: {'; '.join(stop_reasons)}. "
                "Run --mode=new_word or check source data."
            )

    # ── A3: Load Step 1 JSON ──────────────────────────────────────────────────
    print("\nA3  Loading Step 1 extract JSON...")
    if extract_file:
        json_path = extract_file
    else:
        # reg_row["id"] is the registry number used in filenames
        json_path = _find_latest_extract(reg_row["id"], word)

    if not json_path or not os.path.exists(json_path):
        return _stop(
            f"A3: Step 1 JSON not found for {word!r}. "
            f'Run: python scripts/word_study_extract.py --word "{word}"'
        )

    try:
        with open(json_path, encoding="utf-8") as fh:
            extract_json = json.load(fh)
    except Exception as exc:
        return _stop(f"A3: Cannot load JSON from {json_path}: {exc}")

    meta         = extract_json.get("meta", {})
    anchor_word  = meta.get("english_anchor", "")
    include_codes = meta.get("include_codes", [])

    if anchor_word.lower() != word.lower():
        return _stop(
            f"A3: JSON english_anchor {anchor_word!r} ≠ registry word {word!r}"
        )
    if not include_codes:
        return _stop("A3: JSON has no include_codes — re-run word_study_extract.py")

    include_terms = [
        t for t in extract_json.get("terms", []) if t.get("action") == "include"
    ]
    json_date = meta.get("generated", "unknown")

    print(f"     File     : {os.path.basename(json_path)}")
    print(f"     Generated: {json_date}")
    print(
        f"     Anchors  : {', '.join(meta.get('anchor_codes', []))}"
        f"  |  Include: {len(include_codes)}  Exclude: {len(meta.get('exclude_codes', []))}"
    )
    sbg = meta.get("summary_by_group", {})
    print(f"     Groups   : {' '.join(f'{k}:{v}' for k, v in sbg.items())}")
    print("     [NOTE] Using cached JSON — no STEP API calls. term_fetch_log not written.")

    if not dry_run:
        for stream in ("VOCAB_STREAM", "VERSE_STREAM", "VTL_STREAM", "MEANING_STREAM"):
            upsert_checkpoint(conn, run_id, stream, "pending")

    # ── A4: Build gap report ──────────────────────────────────────────────────
    print("\nA4  Building gap report...")
    gap = _build_gap_report(snapshot, include_terms)

    # ── A5: Display gap report + optional interactive gate ────────────────────
    print("\nA5  Gap report:")
    _display_gap_report(gap, word, json_date)

    if dry_run:
        print("\n  [DRY-RUN] Gap report complete. No DB writes performed.")
        conn.execute(
            "UPDATE word_registry SET last_automation_run = NULL WHERE no = ?",
            (registry_id,),
        )
        conn.commit()
        return {
            "outcome": "DRY_RUN", "run_id": run_id,
            "audit_result": "DRY_RUN", "details": gap,
        }

    if interactive:
        approvals = _interactive_gate(gap)
        if not any(approvals.values()):
            print("  No changes approved. Clean exit.")
            conn.execute(
                "UPDATE word_registry SET last_automation_run = NULL WHERE no = ?",
                (registry_id,),
            )
            conn.commit()
            close_run(conn, run_id, "APPROVED_NONE", counts)
            return {
                "outcome": "APPROVED_NONE", "run_id": run_id,
                "audit_result": "APPROVED_NONE", "details": gap,
            }
    else:
        approvals = _auto_approve(gap)
        n_cats = sum(1 for v in approvals.values() if v)
        print(f"\n     [AUTO-APPROVE] {n_cats} non-empty category(ies) will be applied.")

    # ── A6: Apply changes ─────────────────────────────────────────────────────
    print("\nA6  Applying changes...")
    _apply_changes(
        conn, snapshot, include_terms, gap, approvals,
        file_ids, registry_id, run_id, counts, errors,
    )
    print(
        f"     A6  verses_inserted={counts['total_verses_inserted']}"
        f"  verses_updated={counts.get('total_verses_updated', 0)}"
        f"  verses_flagged={counts['total_verses_filtered']}"
    )

    # ── A7: Meaning handler ───────────────────────────────────────────────────
    print("\nA7  Meaning handler...")
    parsed = _run_meaning_handler(conn, include_terms, file_ids)
    counts["total_meanings_parsed"] = parsed
    upsert_checkpoint(conn, run_id, "MEANING_STREAM", "complete", rows_written=parsed)
    fid_ph = ",".join("?" * len(file_ids))
    mp_ct = conn.execute(
        f"SELECT COUNT(*) AS c FROM wa_meaning_parsed mp "
        f"JOIN wa_term_inventory ti ON ti.id = mp.term_inv_id "
        f"WHERE ti.file_id IN ({fid_ph})",
        file_ids,
    ).fetchone()["c"]
    print(f"     A7: {parsed} term(s) parsed.  [VERIFY] wa_meaning_parsed: {mp_ct} rows")

    # ── A8: Quality flag full reset ───────────────────────────────────────────
    print("\nA8  Quality flag reset (full reset — re-derive from STEP data)...")
    flag_ct = _reset_quality_flags(conn, file_ids, registry_id)
    upsert_checkpoint(conn, run_id, "FLAG_STREAM", "complete", rows_written=flag_ct)
    print(f"     A8: {flag_ct} quality flag(s) written.  Phase 2 flags NOT touched.")

    # ── A9: Audit checks ──────────────────────────────────────────────────────
    print("\nA9  Running audit checks (WR-01–WR-20)...")
    audit_result = run_audit(conn, file_ids[0], registry_id)
    for check in audit_result["checks"]:
        if check["result"] != "PASS":
            print(f"     {check['result']:6}  {check['check']}: {check['detail']}")

    write_word_run_state(
        conn, run_id, registry_id, word,
        "AUDIT_WORD_A9",
        audit_result["result"],
        {c["check"]: {"r": c["result"], "d": c["detail"]}
         for c in audit_result["checks"]},
        audit_result.get("stop_reason"),
    )
    # Mark as PROVISIONAL — full researcher sign-off is a separate step
    conn.execute(
        "UPDATE word_run_state SET approved_by = 'PROVISIONAL' "
        "WHERE run_id = ? AND registry_id = ?",
        (run_id, str(registry_id).zfill(3)),
    )
    conn.commit()

    a9_p = sum(1 for c in audit_result["checks"] if c["result"] == "PASS")
    a9_r = sum(1 for c in audit_result["checks"] if c["result"] == "REVIEW")
    a9_s = sum(1 for c in audit_result["checks"] if c["result"] == "STOP")
    print(f"     A9: {audit_result['result']}  ({a9_p} PASS  {a9_r} REVIEW  {a9_s} STOP)")

    if audit_result["result"] == "STOP":
        ans = input(
            "\n  Audit result is STOP. Proceed to registry update (A10)? [y/N]: "
        ).strip().lower()
        if ans not in ("y", "yes"):
            close_run(conn, run_id, "STOPPED", counts)
            conn.execute(
                "UPDATE word_registry SET last_automation_run = NULL WHERE no = ?",
                (registry_id,),
            )
            conn.commit()
            return {
                "outcome": "STOPPED", "run_id": run_id,
                "audit_result": "STOP", "details": errors,
            }

    # ── A10: Registry + file index update ────────────────────────────────────
    print("\nA10 Updating word registry and file index...")

    # Testament coverage per file
    for fid in file_ids:
        testaments = {
            r["testament"]
            for r in conn.execute(
                "SELECT DISTINCT testament FROM wa_verse_records "
                "WHERE file_id = ? AND span_strong_match = 1 "
                "AND (delete_flagged = 0 OR delete_flagged IS NULL)",
                (fid,),
            ).fetchall()
        }
        conn.execute(
            "UPDATE wa_file_index SET testament_coverage = ? WHERE id = ?",
            (_cov(testaments), fid),
        )

    # strongs_list: sorted by verse count desc
    sl_rows = conn.execute(
        f"SELECT term_id, COUNT(*) AS cnt FROM wa_verse_records "
        f"WHERE file_id IN ({fid_ph}) AND span_strong_match = 1 "
        f"AND (delete_flagged = 0 OR delete_flagged IS NULL) "
        f"GROUP BY term_id ORDER BY cnt DESC",
        file_ids,
    ).fetchall()
    strongs_list = json.dumps(
        [{"strong": r["term_id"], "count": r["cnt"]} for r in sl_rows]
    )

    # Counts (active only)
    verse_count = conn.execute(
        f"SELECT COUNT(*) AS c FROM wa_verse_records "
        f"WHERE file_id IN ({fid_ph}) AND span_strong_match = 1 "
        f"AND (delete_flagged = 0 OR delete_flagged IS NULL)",
        file_ids,
    ).fetchone()["c"]
    term_count = conn.execute(
        f"SELECT COUNT(*) AS c FROM wa_term_inventory "
        f"WHERE file_id IN ({fid_ph}) "
        f"AND (delete_flagged = 0 OR delete_flagged IS NULL)",
        file_ids,
    ).fetchone()["c"]

    # Notes: append audit summary (do not replace existing notes)
    old_notes    = (reg_row["notes"] or "").rstrip()
    anomaly_note = ""
    if errors:
        anomaly_note = (
            f"\n[ANOMALY {_today()}] {len(errors)} error(s): "
            f"{'; '.join(errors[:3])}"
        )
    audit_note = (
        f"\n[AUDIT {_today()}] result={audit_result['result']}"
        f"  terms={term_count}  verses={verse_count}"
        f"  run_id={run_id}"
    )
    new_notes = (old_notes + anomaly_note + audit_note).strip()

    # phase1_status
    final_status = (
        "Complete"
        if audit_result["result"] in ("PASS", "REVIEW") or term_count == 0
        else "In Progress"
    )

    conn.execute(
        """UPDATE word_registry SET
               phase1_status       = ?,
               phase1_term_count   = ?,
               phase1_verse_count  = ?,
               last_automation_run = ?,
               automation_run_id   = ?,
               strongs_list        = ?,
               notes               = ?
           WHERE no = ?""",
        (
            final_status, term_count, verse_count,
            AUDITED_SENTINEL,    # ← 'AUDITED' sentinel, not a datetime
            run_id,
            strongs_list,
            new_notes,
            registry_id,
        ),
    )
    conn.commit()

    counts["words_complete"] = 1
    close_run(conn, run_id, "COMPLETE", counts)

    vtl_final = conn.execute(
        f"SELECT COUNT(*) AS c FROM wa_verse_term_links vtl "
        f"JOIN wa_verse_records vr ON vr.id = vtl.verse_id "
        f"WHERE vr.file_id IN ({fid_ph})",
        file_ids,
    ).fetchone()["c"]

    _box(
        "AUDIT_WORD COMPLETE",
        [
            f"Word       : {word}  (registry {registry_id})",
            f"Run ID     : {run_id}",
            f"Result     : {audit_result['result']}",
            f"Terms      : {term_count}  (active)",
            f"Verses     : {verse_count}  (span-confirmed, active)",
            f"VTL rows   : {vtl_final}",
            f"Meanings   : {parsed} parsed",
            f"Flags      : {flag_ct} quality flags",
            f"Errors     : {len(errors)}",
            f"Status     : {final_status}",
        ],
    )

    return {
        "outcome":      "COMPLETE",
        "run_id":       run_id,
        "audit_result": audit_result["result"],
        "details": {
            "verses_inserted": counts["total_verses_inserted"],
            "verses_updated":  counts.get("total_verses_updated", 0),
            "verses_flagged":  counts["total_verses_filtered"],
            "meanings_parsed": parsed,
            "errors":          errors,
        },
    }
