"""
apply_session_patch.py
──────────────────────
Generic applicator for Session B/C/D/DimensionReview JSON patches.

Handles operation types:
  - update_mti_status     → UPDATE status on mti_terms by strongs_number
  - update_registry       → UPDATE fields on word_registry by registry_no
  - bulk_update_note      → Bulk UPDATE mti_terms by filter or strongs list
  - bulk_update_mti_status → Bulk set status on multiple terms
  - bulk_confirm_candidate_delete → Confirm candidate_delete as delete
  - restore_delete_flagged → Restore incorrectly delete-flagged terms
  - insert (wa_session_research_flags) → Research flag inserts
  - insert (wa_session_b_dimensions)   → Session B dimensional profile
  - insert (wa_session_b_findings)     → Session B key findings (all 20 fields, DIR-008 + SC-01)
  - update (wa_session_b_findings)     → Update finding lifecycle fields (DIR-008 + SC-01)
  - supersede_finding                  → Atomic insert new + mark old superseded (DIR-008)
  - insert_finding_entity_link         → Insert into wa_finding_entity_links (DIR-008)
  - insert (wa_obs_question_catalogue) → Catalogue question inserts (single or rows-array)
  - insert (wa_finding_catalogue_links) → Finding-to-question links (single or rows-array)
  - update (wa_dimension_index)        → Dimension review updates
  - update (verse_context_group)       → Group description corrections
  - registry_note / schema_investigation_note → Documentation only
  - bulk_update           → Generic bulk update on any table

Supported patch types (in _patch_meta.patch_type):
  - PREANALYSIS        → Pre-analysis classification patch
  - SESSIONB           → Analysis completion patch
  - SESSIONB_FINDINGS  → Session B Stage 2 pass-close patch (findings + entity links only). Carries session_b_status: null. (DIR-008)
  - SESSIOND           → Session D discovery JSON patch
  - CLUSTERING         → Cluster assignment patch
  - DIMREVIEW          → Dimension review patch (wa_dimension_index updates + B/D pointers)
  - DIMREVIEW-GRPDESC  → Group description correction (verse_context_group + dimension_index sync)
  - CATALOGUE_POPULATION → Catalogue question population (wa_obs_question_catalogue inserts)

Supported tables:
  - mti_terms              → MTI status, reconciled flag, status_note
  - wa_session_research_flags → Phase 2 research flag inserts
  - wa_session_b_dimensions → Session B dimensional profiles
  - wa_session_b_findings  → Session B key findings (20 fields incl. status, term_id)
  - wa_finding_entity_links → Junction table — finding-to-entity links (DIR-008)
  - wa_dimension_index     → Dimension review updates
  - verse_context_group    → Group description corrections
  - word_registry          → registry notes, anchor_verses, last_changed

Safety:
  - Transaction-wrapped: all-or-nothing
  - Idempotency: refuses patches already applied (by patch_id in engine_run_log)
  - Validates registry_id, strongs_numbers, flag_label uniqueness before applying
  - Dimension review: protects manual_override=1 rows from unintended modification
  - Entity links: validates finding_id exists or is resolvable from prior op in same patch

Usage:
  python scripts/apply_session_patch.py <patch_file> [--dry-run]
"""

__version__ = "20260416"

import argparse
import json
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH      = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
ARCHIVE_DIR  = os.path.join(os.path.dirname(__file__), "..", "archive", "patches")


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ─────────────────────────────────────────────────────────────────────────────
# Same-patch resolution registry (DIR-008)
# ─────────────────────────────────────────────────────────────────────────────
# Maps finding_id (TEXT label, e.g. "023-F006") → wa_session_b_findings.id (INT)
# for findings inserted earlier in the current patch. Allows
# insert_finding_entity_link operations to reference findings created in the
# same patch via finding_id_ref. Cleared per-patch in apply_patch().
_inserted_findings_by_label: dict[str, int] = {}


def _record_inserted_finding(op: dict, new_id: int) -> None:
    """Stash the new id so later ops in this patch can resolve by label."""
    label = op.get("record", {}).get("finding_id") or op.get("record", {}).get("flag_label")
    # supersede_finding nests the new finding under "new_finding"
    if not label and "record" in op and "new_finding" in op["record"]:
        nf = op["record"]["new_finding"]
        label = nf.get("finding_id") or nf.get("flag_label")
    if label:
        _inserted_findings_by_label[label] = new_id


def _resolve_inserted_finding(label: str) -> int | None:
    """Resolve a finding label to its inserted id within the current patch."""
    return _inserted_findings_by_label.get(label)


def _insert_finding(conn: sqlite3.Connection, rec: dict, meta: dict | None) -> int:
    """Insert a wa_session_b_findings row supporting all 18 fields. Returns new id.

    Mandatory: finding_id, registry_id, finding_type, finding, raised_date,
    session_b_instruction. Lifecycle fields default sensibly:
      - delete_flag → 0
      - thin_evidence → 0
      - everything else → NULL.
    """
    finding_id = rec.get("finding_id") or rec.get("flag_label")
    registry_id_val = rec.get("registry_id") or rec.get("registry_no")
    finding_type = rec.get("finding_type") or rec.get("cluster") or "DIMENSION_REVIEW"
    finding = rec.get("finding") or rec.get("description")
    raised_date = (
        rec.get("raised_date") or rec.get("created_date")
        or (meta or {}).get("produced_date", _now()[:10])
    )
    instruction = (
        rec.get("session_b_instruction") or rec.get("source_instruction")
        or (meta or {}).get("produced_by", "unknown")
    )
    cur = conn.execute(
        """INSERT INTO wa_session_b_findings
           (finding_id, registry_id, file_id, finding_type, finding,
            anchor_verses, raised_date, session_b_instruction,
            pass_ref, study_segment, delete_flag, obsolete_reason, obsolete_date,
            superseded_by_id, related_finding_id, resolution_note, thin_evidence,
            status, term_id)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            finding_id,
            registry_id_val,
            rec.get("file_id"),
            finding_type,
            finding,
            rec.get("anchor_verses"),
            raised_date,
            instruction,
            rec.get("pass_ref"),
            rec.get("study_segment"),
            rec.get("delete_flag", 0),
            rec.get("obsolete_reason"),
            rec.get("obsolete_date"),
            rec.get("superseded_by_id"),
            rec.get("related_finding_id"),
            rec.get("resolution_note"),
            rec.get("thin_evidence", 0),
            rec.get("status", "pending"),
            rec.get("term_id"),
        ),
    )
    return cur.lastrowid


def _validate(conn, patch: dict) -> list[str]:
    """Pre-flight validation. Returns list of error strings (empty = OK)."""
    errors = []
    meta = patch.get("_patch_meta", {})

    # Check registry exists (registry_id in patches refers to word_registry.no)
    reg_id = meta.get("registry_id")
    if reg_id:
        row = conn.execute("SELECT id, word FROM word_registry WHERE no = ?", (reg_id,)).fetchone()
        if not row:
            errors.append(f"Registry no={reg_id} not found in word_registry")

    # Check patch_id not already applied
    patch_id = meta.get("patch_id")
    if patch_id:
        existing = conn.execute(
            "SELECT 1 FROM engine_run_log WHERE run_id = ?", (patch_id,)
        ).fetchone()
        if existing:
            errors.append(f"Patch {patch_id} already applied (found in engine_run_log)")

    # Require session_b_status in _patch_meta — except for exempt patch types
    patch_type = meta.get("patch_type", "")
    pid = meta.get("patch_id", "")
    # Detect exempt type from patch_id (covers DIFFERENTIAL and other sub-types)
    sb_exempt_types = ("CLUSTERING", "SESSIOND", "VERSECONTEXT", "VCGROUP", "VCVERSE", "REPAIR", "DIMREVIEW", "DIM-", "DIMGRPDESC", "SESSIONB_FINDINGS", "CATALOGUE")
    is_exempt = any(patch_type.startswith(t) for t in sb_exempt_types) if patch_type else False
    if not is_exempt:
        for token in sb_exempt_types:
            if token in pid:
                is_exempt = True
                break
    # Also exempt VCB-prefixed patches (Verse Context batches)
    if not is_exempt and "VCB" in pid:
        is_exempt = True
    sb_status = meta.get("session_b_status")
    if not sb_status and not is_exempt:
        errors.append("_patch_meta.session_b_status is required (e.g. 'Pre-Analysis Complete', 'Analysis Complete')")

    for op in patch.get("operations", []):
        op_id = op.get("op_id", "?")
        table = op.get("table", "")
        operation = op.get("operation", "")

        # Validate mti_terms updates: check strongs exists (flexible FK match)
        if table == "mti_terms" and operation == "update":
            match = op.get("match", {})
            strongs = match.get("strongs_number")
            if strongs:
                row = conn.execute(
                    "SELECT id FROM mti_terms WHERE strongs_number = ?",
                    (strongs,),
                ).fetchone()
                if not row:
                    errors.append(f"{op_id}: mti_terms row not found: {strongs}")

        # Validate update_evidential_status: check term_inv_id exists and status is valid
        if operation == "update_evidential_status":
            tid = op.get("term_inv_id")
            if tid:
                row = conn.execute(
                    "SELECT id FROM wa_term_inventory WHERE id = ?", (tid,)
                ).fetchone()
                if not row:
                    errors.append(f"{op_id}: wa_term_inventory id={tid} not found")
            ev_status = (op.get("set") or {}).get("evidential_status")
            valid_ev = {"confirmed", "plausible", "uncertain", "instrumental", "relational_only"}
            if ev_status and ev_status not in valid_ev:
                errors.append(f"{op_id}: invalid evidential_status '{ev_status}' (valid: {valid_ev})")

        # Validate research flag inserts: check label uniqueness
        if table in ("wa_phase2_flags", "wa_session_research_flags") and operation == "insert":
            rec = op.get("record", {})
            label = rec.get("flag_label")
            if label:
                existing = conn.execute(
                    "SELECT 1 FROM wa_session_research_flags WHERE flag_label = ?", (label,)
                ).fetchone()
                if existing:
                    errors.append(f"{op_id}: flag_label '{label}' already exists in wa_session_research_flags")

        # Validate wa_dimension_index updates: check id exists, manual_override protection, dominant_subject values
        if table == "wa_dimension_index" and operation == "update":
            match = op.get("match", {})
            di_id = match.get("id")
            set_vals = op.get("set", {})
            if di_id:
                row = conn.execute(
                    "SELECT id, manual_override FROM wa_dimension_index WHERE id = ?", (di_id,)
                ).fetchone()
                if not row:
                    errors.append(f"{op_id}: wa_dimension_index id={di_id} not found")
                elif row["manual_override"] == 1:
                    if "manual_override" not in set_vals:
                        errors.append(
                            f"{op_id}: wa_dimension_index id={di_id} has manual_override=1 — "
                            f"cannot update without explicit manual_override in set fields"
                        )
            # Validate dominant_subject values (DR-12)
            ds = set_vals.get("dominant_subject")
            if ds is not None:
                valid_ds = {"GOD", "HUMAN", "OTHER_HUMAN", "UNSEEN", "NONE"}
                if ds not in valid_ds:
                    errors.append(f"{op_id}: invalid dominant_subject '{ds}' (valid: {valid_ds})")

        # Validate wa_session_b_findings inserts: finding_id uniqueness
        if table == "wa_session_b_findings" and operation == "insert":
            rec = op.get("record", {})
            fid = rec.get("finding_id")
            if fid:
                existing = conn.execute(
                    "SELECT 1 FROM wa_session_b_findings WHERE finding_id = ?", (fid,)
                ).fetchone()
                if existing:
                    errors.append(f"{op_id}: finding_id '{fid}' already exists in wa_session_b_findings")

        # Validate word_registry updates
        if table == "word_registry" and operation == "update":
            match = op.get("match", {})
            reg_match_id = match.get("id")
            if reg_match_id:
                row = conn.execute("SELECT id FROM word_registry WHERE id = ?", (reg_match_id,)).fetchone()
                if not row:
                    errors.append(f"{op_id}: word_registry id={reg_match_id} not found")

    return errors


def _resolve_group_id(raw_id: str, counts: dict, conn, op_id: str):
    """Resolve a group_code string or placeholder to an integer group id.

    Handles:
      - Direct group_code (e.g. '235-001') from _group_code_map or DB lookup
      - Placeholder 'integer_id_NNN_NNN' pattern → converted to group_code 'NNN-NNN'
    Returns integer id or None on failure.
    """
    group_code_map = counts.get("_group_code_map", {})

    # Handle integer_id_ placeholder pattern (e.g. 'integer_id_235_001' -> '235-001')
    if raw_id.startswith("integer_id_"):
        parts = raw_id[len("integer_id_"):]
        # Convert underscore-separated to dash-separated group_code
        # Pattern: integer_id_{mti_id}_{serial} -> {mti_id}-{serial}
        segments = parts.split("_")
        if len(segments) >= 2:
            gc = f"{segments[0]}-{segments[1]}"
            if gc in group_code_map:
                return group_code_map[gc]
            existing = conn.execute(
                "SELECT id FROM verse_context_group WHERE group_code = ?", (gc,)
            ).fetchone()
            if existing:
                return existing[0]
        print(f"  {op_id}: [ERROR] Cannot resolve placeholder '{raw_id}'")
        return None

    # Direct group_code lookup
    if raw_id in group_code_map:
        return group_code_map[raw_id]

    # DB lookup
    existing = conn.execute(
        "SELECT id FROM verse_context_group WHERE group_code = ?", (raw_id,)
    ).fetchone()
    if existing:
        return existing[0]

    print(f"  {op_id}: [ERROR] Cannot resolve group_code '{raw_id}' to integer id")
    return None


def _apply_operation(conn, op: dict, counts: dict, meta: dict | None = None) -> None:
    """Apply a single operation."""
    op_id     = op.get("op_id", "?")
    table     = op.get("table", "") or op.get("target_table", "")
    operation = op.get("operation", "")

    if operation == "update_mti_status":
        # Two sub-formats:
        #   (a) Pre-analysis: strongs_number at top level, set dict with status fields
        #   (b) v5 format: strongs_number + new_status at top level (no set dict)
        strongs  = op.get("strongs_number")
        set_vals = dict(op.get("set", {}))
        # v5 format: new_status at top level
        if not set_vals and op.get("new_status"):
            set_vals = {"status": op["new_status"]}
        if not strongs or not set_vals:
            counts["skipped"] = counts.get("skipped", 0) + 1
            return
        # Filter to valid mti_terms columns
        valid_cols = {
            r[1] for r in conn.execute("PRAGMA table_info(mti_terms)").fetchall()
        }
        dropped = [k for k in set_vals if k not in valid_cols]
        for k in dropped:
            del set_vals[k]
        if not set_vals:
            counts["skipped"] = counts.get("skipped", 0) + 1
            return
        set_vals["last_changed"] = _now()
        set_clauses = ", ".join(f"{k} = ?" for k in set_vals)
        params = list(set_vals.values()) + [strongs]
        conn.execute(
            f"UPDATE mti_terms SET {set_clauses} WHERE strongs_number = ?",
            params,
        )
        counts["mti_status_updated"] = counts.get("mti_status_updated", 0) + 1
        status = set_vals.get("status", "?")
        print(f"  {op_id}: mti_terms STATUS {strongs} -> {status}")

    elif operation == "update_registry":
        # Canonical format: registry_no + set dict
        # Also accepts registry_id as alias for registry_no
        reg_no   = op.get("registry_no") or op.get("registry_id")
        set_vals = dict(op.get("set", {}))
        if not reg_no or not set_vals:
            counts["skipped"] = counts.get("skipped", 0) + 1
            return
        valid_cols = {
            r[1] for r in conn.execute("PRAGMA table_info(word_registry)").fetchall()
        }
        dropped = [k for k in set_vals if k not in valid_cols]
        for k in dropped:
            del set_vals[k]
        if not set_vals:
            counts["skipped"] = counts.get("skipped", 0) + 1
            return
        set_clauses = ", ".join(f"{k} = ?" for k in set_vals)
        params = list(set_vals.values()) + [reg_no]
        conn.execute(
            f"UPDATE word_registry SET {set_clauses} WHERE no = ?",
            params,
        )
        counts["registry_updated"] = counts.get("registry_updated", 0) + 1
        print(f"  {op_id}: word_registry UPDATE reg {reg_no} ({', '.join(set_vals.keys())})")

    elif operation == "bulk_update_note":
        # Two sub-formats:
        #   (a) filter-based: filter string describes criteria, apply to matching rows
        #   (b) bulk_strongs: explicit list of strongs_numbers to update
        set_vals = dict(op.get("set", {}))
        valid_cols = {
            r[1] for r in conn.execute("PRAGMA table_info(mti_terms)").fetchall()
        }
        dropped = [k for k in set_vals if k not in valid_cols]
        for k in dropped:
            del set_vals[k]
        set_vals["last_changed"] = _now()

        updated = 0
        xref_exceptions = op.get("xref_exceptions", {})

        if "bulk_strongs" in op:
            # Format (b): explicit strongs list
            for strongs in op["bulk_strongs"]:
                s = dict(set_vals)
                # Apply xref exception if present
                if strongs in xref_exceptions:
                    xref_status = xref_exceptions[strongs].split(" — ")[0] if " — " in xref_exceptions[strongs] else xref_exceptions[strongs]
                    s["status"] = xref_status
                    s["exclusion_reason"] = xref_exceptions[strongs]
                sc = ", ".join(f"{k} = ?" for k in s)
                conn.execute(
                    f"UPDATE mti_terms SET {sc} WHERE strongs_number = ?",
                    list(s.values()) + [strongs],
                )
                updated += 1

        elif "filter" in op:
            # Format (a): filter-based — parse the filter string
            # Expected: "registry_no=N AND delete_flagged=1 AND mti_status IS NULL"
            filt = op["filter"]
            reg_no = None
            if "registry_no=" in filt:
                import re as _re
                m = _re.search(r"registry_no=(\d+)", filt)
                if m:
                    reg_no = int(m.group(1))
            if reg_no:
                # Find all mti_terms for this registry with delete_flagged terms and NULL status
                rows = conn.execute(
                    """SELECT m.id FROM mti_terms m
                       JOIN wa_term_inventory ti ON ti.strongs_number = m.strongs_number
                       JOIN wa_file_index fi ON fi.id = ti.file_id
                       WHERE fi.word_registry_fk = ?
                       AND ti.delete_flagged = 1
                       AND m.status IS NULL""",
                    (reg_no,),
                ).fetchall()
                for row in rows:
                    sc = ", ".join(f"{k} = ?" for k in set_vals)
                    conn.execute(
                        f"UPDATE mti_terms SET {sc} WHERE id = ?",
                        list(set_vals.values()) + [row["id"]],
                    )
                    updated += 1

        counts["bulk_note_updated"] = counts.get("bulk_note_updated", 0) + updated
        print(f"  {op_id}: mti_terms BULK {updated} row(s) -> {set_vals.get('status', '?')}")

    elif operation == "bulk_update_mti_status":
        # Two sub-formats:
        #   (a) {status, terms: [{strongs_number, term_inv_id}]}
        #   (b) {new_status, term_inv_ids: [int, ...]}  (v5 format)
        bulk_status = op.get("status") or op.get("new_status")
        terms_list = op.get("terms", [])
        term_inv_ids = op.get("term_inv_ids", [])
        if not bulk_status or (not terms_list and not term_inv_ids):
            counts["skipped"] = counts.get("skipped", 0) + 1
            return
        now_ts = _now()
        updated = 0
        if term_inv_ids:
            # v5 format: look up strongs from term_inv_id
            for tid in term_inv_ids:
                row = conn.execute(
                    "SELECT strongs_number FROM wa_term_inventory WHERE id = ?", (tid,)
                ).fetchone()
                if row:
                    conn.execute(
                        "UPDATE mti_terms SET status = ?, last_changed = ? WHERE strongs_number = ?",
                        (bulk_status, now_ts, row["strongs_number"]),
                    )
                    updated += 1
        else:
            for t in terms_list:
                strongs = t.get("strongs_number")
                if not strongs:
                    continue
                conn.execute(
                    "UPDATE mti_terms SET status = ?, last_changed = ? WHERE strongs_number = ?",
                    (bulk_status, now_ts, strongs),
                )
                updated += 1
        counts["mti_status_updated"] = counts.get("mti_status_updated", 0) + updated
        print(f"  {op_id}: mti_terms BULK STATUS {updated} row(s) -> {bulk_status}")

    elif operation in ("schema_investigation_note", "registry_note"):
        # Documentation-only — no DB action, just log it
        print(f"  {op_id}: [NOTE] {op.get('description', '')[:80]}")
        return

    elif operation in ("bulk_confirm_candidate_delete", "bulk_confirm_delete_flagged", "bulk_update_none_to_delete"):
        # Two sub-formats:
        #   (a) filter-based: filter string with registry_no=N
        #   (b) v5.1 format: term_inv_ids array + new_status
        term_inv_ids = op.get("term_inv_ids", [])
        new_status = op.get("new_status", "delete")
        now_ts = _now()

        if term_inv_ids:
            # v5.1 format: look up strongs from term_inv_ids
            updated = 0
            for tid in term_inv_ids:
                row = conn.execute(
                    "SELECT strongs_number FROM wa_term_inventory WHERE id = ?", (tid,)
                ).fetchone()
                if row:
                    conn.execute(
                        "UPDATE mti_terms SET status = ?, last_changed = ? WHERE strongs_number = ?",
                        (new_status, now_ts, row["strongs_number"]),
                    )
                    updated += 1
            counts["mti_status_updated"] = counts.get("mti_status_updated", 0) + updated
            print(f"  {op_id}: mti_terms BULK CONFIRM {updated} row(s) -> {new_status}")
        else:
            # Legacy filter-based format
            set_vals = dict(op.get("set", {}))
            valid_cols = {
                r[1] for r in conn.execute("PRAGMA table_info(mti_terms)").fetchall()
            }
            dropped = [k for k in set_vals if k not in valid_cols]
            for k in dropped:
                del set_vals[k]
            set_vals["last_changed"] = now_ts

            filt = op.get("filter", "")
            reg_no = None
            import re as _re
            m = _re.search(r"registry_no=(\d+)", filt)
            if m:
                reg_no = int(m.group(1))
            if not reg_no:
                counts["skipped"] = counts.get("skipped", 0) + 1
                return

            if operation == "bulk_confirm_candidate_delete":
                condition = "m.status = 'candidate_delete'"
            elif operation == "bulk_update_none_to_delete":
                condition = "m.status IS NULL"
            else:
                condition = "m.status IS NULL"
            rows = conn.execute(
                f"""SELECT m.id FROM mti_terms m
                    JOIN wa_term_inventory ti ON ti.strongs_number = m.strongs_number
                    JOIN wa_file_index fi ON fi.id = ti.file_id
                    WHERE fi.word_registry_fk = ?
                    AND {condition}
                    {"AND ti.delete_flagged = 1" if operation == "bulk_confirm_delete_flagged" else ""}""",
                (reg_no,),
            ).fetchall()
            seen = set()
            updated = 0
            for row in rows:
                if row["id"] in seen:
                    continue
                seen.add(row["id"])
                sc = ", ".join(f"{k} = ?" for k in set_vals)
                conn.execute(
                    f"UPDATE mti_terms SET {sc} WHERE id = ?",
                    list(set_vals.values()) + [row["id"]],
                )
                updated += 1
            counts["bulk_note_updated"] = counts.get("bulk_note_updated", 0) + updated
            print(f"  {op_id}: mti_terms BULK CONFIRM {updated} row(s) -> {set_vals.get('status', '?')}")

    elif table == "mti_terms" and operation == "update":
        match    = op["match"]
        set_vals = dict(op["set"])
        strongs  = match.get("strongs_number")
        owning_fk = match.get("owning_registry_fk")
        # If owning_registry_fk is in match, also set it on the row if currently NULL
        if owning_fk and "owning_registry_fk" not in set_vals:
            current = conn.execute(
                "SELECT owning_registry_fk FROM mti_terms WHERE strongs_number = ?",
                (strongs,),
            ).fetchone()
            if current and current[0] is None:
                set_vals["owning_registry_fk"] = owning_fk
                set_vals["owning_registry"] = str(owning_fk)
        set_clauses = ", ".join(f"{k} = ?" for k in set_vals)
        params = list(set_vals.values()) + [strongs]
        conn.execute(
            f"UPDATE mti_terms SET {set_clauses} WHERE strongs_number = ?",
            params,
        )
        counts["mti_terms_updated"] = counts.get("mti_terms_updated", 0) + 1
        print(f"  {op_id}: mti_terms UPDATE {strongs}")

    elif operation == "restore_delete_flagged":
        # Restore terms that were incorrectly marked delete_flagged
        term_inv_ids = op.get("term_inv_ids", [])
        if not term_inv_ids:
            counts["skipped"] = counts.get("skipped", 0) + 1
            return
        restored = 0
        for tid in term_inv_ids:
            conn.execute(
                "UPDATE wa_term_inventory SET delete_flagged = 0 WHERE id = ?",
                (tid,),
            )
            restored += 1
        counts["restored"] = counts.get("restored", 0) + restored
        print(f"  {op_id}: wa_term_inventory RESTORE delete_flagged on {restored} term(s)")

    elif operation == "update_evidential_status":
        tid = op.get("term_inv_id")
        set_vals = op.get("set", {})
        ev_status = set_vals.get("evidential_status")
        ret_note = set_vals.get("retention_note")
        if not tid:
            counts["skipped"] = counts.get("skipped", 0) + 1
            return
        conn.execute(
            "UPDATE wa_term_inventory SET evidential_status = ?, retention_note = ? WHERE id = ?",
            (ev_status, ret_note, tid),
        )
        counts["evidential_updated"] = counts.get("evidential_updated", 0) + 1
        strongs = op.get("strongs_number", "?")
        print(f"  {op_id}: wa_term_inventory EVIDENTIAL {strongs} -> {ev_status}")

    elif table == "wa_session_b_dimensions" and operation == "insert":
        rec = op["record"]
        conn.execute(
            """INSERT INTO wa_session_b_dimensions
               (registry_id, file_id, relational_environment, relational_environment_note,
                spirit_soul_body, spirit_soul_body_note, inner_operations, inner_operations_note,
                being, being_note, raised_date, session_b_instruction)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                rec.get("registry_id"),
                rec.get("file_id"),
                rec.get("relational_environment", 0),
                rec.get("relational_environment_note"),
                rec.get("spirit_soul_body", 0),
                rec.get("spirit_soul_body_note"),
                rec.get("inner_operations", 0),
                rec.get("inner_operations_note"),
                rec.get("being", 0),
                rec.get("being_note"),
                rec.get("raised_date", _now()[:10]),
                rec.get("session_b_instruction", "WA-SessionB-Extraction-Instruction-v5"),
            ),
        )
        counts["dimensions_inserted"] = counts.get("dimensions_inserted", 0) + 1
        print(f"  {op_id}: wa_session_b_dimensions INSERT reg={rec.get('registry_id')}")

    elif table == "wa_session_b_findings" and operation == "insert":
        new_id = _insert_finding(conn, op["record"], meta)
        counts["findings_inserted"] = counts.get("findings_inserted", 0) + 1
        # Stash the inserted id so subsequent ops in the same patch can resolve
        # finding_id references (e.g. insert_finding_entity_link).
        _record_inserted_finding(op, new_id)
        finding_id = op["record"].get("finding_id") or op["record"].get("flag_label")
        print(f"  {op_id}: wa_session_b_findings INSERT {finding_id} (id={new_id})")

    elif table == "wa_session_b_findings" and operation == "update":
        rec = op["record"]
        # Identify target row by finding_id (TEXT, unique) or by id (INTEGER PK)
        target_id = rec.get("id")
        finding_id = rec.get("finding_id")
        if not target_id and not finding_id:
            raise ValueError(f"{op_id}: wa_session_b_findings update requires id or finding_id")
        if target_id:
            where_sql = "id = ?"
            where_params = [target_id]
        else:
            where_sql = "finding_id = ?"
            where_params = [finding_id]
        # Allowed update fields (everything except id, finding_id, registry_id, raised_date)
        allowed = {
            "file_id", "finding_type", "finding", "anchor_verses", "session_b_instruction",
            "pass_ref", "study_segment", "delete_flag", "obsolete_reason", "obsolete_date",
            "superseded_by_id", "related_finding_id", "resolution_note", "thin_evidence",
            "status", "term_id",
        }
        set_parts = []
        set_vals = []
        for k, v in rec.items():
            if k in allowed:
                set_parts.append(f"{k} = ?")
                set_vals.append(v)
        if not set_parts:
            raise ValueError(f"{op_id}: wa_session_b_findings update has no updatable fields")
        sql = f"UPDATE wa_session_b_findings SET {', '.join(set_parts)} WHERE {where_sql}"
        cur = conn.execute(sql, set_vals + where_params)
        if cur.rowcount == 0:
            raise ValueError(f"{op_id}: no wa_session_b_findings row matched {where_sql}={where_params}")
        counts["findings_updated"] = counts.get("findings_updated", 0) + 1
        print(f"  {op_id}: wa_session_b_findings UPDATE rows={cur.rowcount}")

    elif operation == "supersede_finding":
        # Atomic: insert new finding, then mark original as superseded.
        rec = op["record"]
        original_id = rec.get("original_finding_id")
        obsolete_reason = rec.get("obsolete_reason")
        obsolete_date = rec.get("obsolete_date") or _now()[:10]
        new_finding = rec.get("new_finding")
        if not (original_id and obsolete_reason and new_finding):
            raise ValueError(
                f"{op_id}: supersede_finding requires original_finding_id, obsolete_reason, new_finding"
            )
        # Verify original exists
        orig = conn.execute(
            "SELECT id FROM wa_session_b_findings WHERE id = ?", (original_id,)
        ).fetchone()
        if not orig:
            raise ValueError(f"{op_id}: supersede_finding original_finding_id={original_id} not found")
        # Insert new finding
        new_id = _insert_finding(conn, new_finding, meta)
        # Update original
        conn.execute(
            """UPDATE wa_session_b_findings
               SET delete_flag = 1, superseded_by_id = ?, obsolete_reason = ?, obsolete_date = ?
               WHERE id = ?""",
            (new_id, obsolete_reason, obsolete_date, original_id),
        )
        counts["findings_superseded"] = counts.get("findings_superseded", 0) + 1
        counts["findings_inserted"] = counts.get("findings_inserted", 0) + 1
        _record_inserted_finding(op, new_id)
        print(f"  {op_id}: supersede_finding original={original_id} new_id={new_id}")

    elif operation == "insert_finding_entity_link" or (
        table == "wa_finding_entity_links" and operation == "insert"
    ):
        rec = op["record"]
        # Resolve finding_id: either explicit integer OR a finding_id_ref pointing
        # to a finding inserted earlier in the same patch (similar to group_code resolution
        # in VERSECONTEXT patches per patch spec §3.1).
        finding_id_int = rec.get("finding_id")
        ref_label = rec.get("finding_id_ref") or rec.get("finding_label_ref")
        if not finding_id_int and ref_label:
            finding_id_int = _resolve_inserted_finding(ref_label)
        if not finding_id_int:
            raise ValueError(
                f"{op_id}: insert_finding_entity_link requires finding_id (integer) "
                "or finding_id_ref (label of finding inserted in same patch)"
            )
        # Verify finding exists
        exists = conn.execute(
            "SELECT 1 FROM wa_session_b_findings WHERE id = ?", (finding_id_int,)
        ).fetchone()
        if not exists:
            raise ValueError(
                f"{op_id}: insert_finding_entity_link finding_id={finding_id_int} not found"
            )
        entity_type = rec.get("entity_type")
        entity_id = rec.get("entity_id")
        entity_strongs = rec.get("entity_strongs")
        raised_date = rec.get("raised_date") or _now()[:10]
        if not entity_type:
            raise ValueError(f"{op_id}: insert_finding_entity_link requires entity_type")
        delete_flagged = rec.get("delete_flagged", 0)
        conn.execute(
            """INSERT INTO wa_finding_entity_links
               (finding_id, entity_type, entity_id, entity_strongs, raised_date, delete_flagged)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (finding_id_int, entity_type, entity_id, entity_strongs, raised_date, delete_flagged),
        )
        counts["entity_links_inserted"] = counts.get("entity_links_inserted", 0) + 1
        print(f"  {op_id}: wa_finding_entity_links INSERT finding={finding_id_int} type={entity_type}")

    elif table in ("wa_phase2_flags", "wa_session_research_flags") and operation == "insert":
        rec = op["record"]
        # Map DIMREVIEW field names to table schema (fallback to correct names)
        registry_id_val = rec.get("registry_id") or rec.get("registry_no")
        flag_code = rec.get("flag_code") or ("SD_POINTER" if rec.get("session_target") == "D" else "SB_FINDING")
        conn.execute(
            """INSERT INTO wa_session_research_flags
               (registry_id, file_id, flag_code, flag_label, strongs_reference,
                cross_registry_id, priority, session_target,
                description, session_raised, raised_date, resolved)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                registry_id_val,
                rec.get("file_id"),
                flag_code,
                rec.get("flag_label"),
                rec.get("strongs_reference"),
                rec.get("cross_registry_id"),
                rec.get("priority", "MEDIUM"),
                rec.get("session_target", "D"),
                rec.get("description"),
                rec.get("session_raised", (meta or {}).get("produced_by", "unknown")),
                rec.get("raised_date", (meta or {}).get("produced_date", _now()[:10])),
                rec.get("resolved", 0),
            ),
        )
        counts["research_flags_inserted"] = counts.get("research_flags_inserted", 0) + 1
        print(f"  {op_id}: wa_session_research_flags INSERT {rec.get('flag_label', '?')}")

    elif table == "verse_context_group" and operation == "insert":
        rec = op["record"]
        # Accept group_code or group_id as the code field (Claude AI uses either)
        group_code = rec.get("group_code") or rec.get("group_id")
        conn.execute(
            """INSERT INTO verse_context_group
               (mti_term_id, group_code, context_description, notes, delete_flagged, vertical_pass_flag)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (
                rec.get("mti_term_id"),
                group_code,
                rec.get("context_description"),
                rec.get("notes"),
                rec.get("delete_flagged", 0),
                rec.get("vertical_pass_flag", 0),
            ),
        )
        new_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
        # Store group_code → integer id mapping for verse_context inserts in same patch
        if "_group_code_map" not in counts:
            counts["_group_code_map"] = {}
        counts["_group_code_map"][group_code] = new_id
        counts["vc_groups_inserted"] = counts.get("vc_groups_inserted", 0) + 1
        print(f"  {op_id}: verse_context_group INSERT {group_code} -> id={new_id}")

    elif table == "verse_context_group" and operation == "update":
        match = op["match"]
        set_vals = dict(op["set"])
        set_clauses = ", ".join(f"{k} = ?" for k in set_vals)
        where_clauses = " AND ".join(f"{k} = ?" for k in match)
        params = list(set_vals.values()) + list(match.values())
        conn.execute(
            f"UPDATE verse_context_group SET {set_clauses} WHERE {where_clauses}",
            params,
        )
        counts["vc_groups_updated"] = counts.get("vc_groups_updated", 0) + 1
        print(f"  {op_id}: verse_context_group UPDATE id={match.get('id', '?')}")

    elif table == "verse_context" and operation == "insert":
        rec = op["record"]
        # Resolve group_id: accept group_id (int or string) or group_code as fallback
        group_id = rec.get("group_id")
        if group_id is None and rec.get("group_code"):
            group_id = rec["group_code"]
        if isinstance(group_id, str):
            group_id = _resolve_group_id(group_id, counts, conn, op_id)
            if group_id is None:
                counts["errors"] = counts.get("errors", 0) + 1
        try:
            conn.execute(
                """INSERT INTO verse_context
                   (verse_record_id, mti_term_id, group_id, is_anchor, is_relevant, is_related, notes, delete_flagged,
                    vertical_pass_flag, set_aside_reason)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    rec.get("verse_record_id"),
                    rec.get("mti_term_id"),
                    group_id,
                    rec.get("is_anchor", 0),
                    rec.get("is_relevant", 0),
                    rec.get("is_related", 0),
                    rec.get("notes"),
                    rec.get("delete_flagged", 0),
                    rec.get("vertical_pass_flag", 0),
                    rec.get("set_aside_reason"),
                ),
            )
            counts["vc_inserts"] = counts.get("vc_inserts", 0) + 1
        except Exception as e:
            if "UNIQUE constraint" in str(e):
                print(f"  {op_id}: [SKIP] Duplicate verse_context — vr={rec.get('verse_record_id')} mti={rec.get('mti_term_id')} grp={group_id}")
                counts["vc_skipped_dupes"] = counts.get("vc_skipped_dupes", 0) + 1
            else:
                raise

    elif table == "verse_context" and operation == "update":
        match = op["match"]
        set_vals = dict(op["set"])
        # Resolve group_id if it's a group_code string
        if "group_id" in set_vals and isinstance(set_vals["group_id"], str):
            resolved = _resolve_group_id(set_vals["group_id"], counts, conn, op_id)
            if resolved is not None:
                set_vals["group_id"] = resolved
            else:
                counts["errors"] = counts.get("errors", 0) + 1
        set_clauses = ", ".join(f"{k} = ?" for k in set_vals)
        where_clauses = " AND ".join(f"{k} = ?" for k in match)
        params = list(set_vals.values()) + list(match.values())
        conn.execute(
            f"UPDATE verse_context SET {set_clauses} WHERE {where_clauses}",
            params,
        )
        counts["vc_updated"] = counts.get("vc_updated", 0) + 1
        print(f"  {op_id}: verse_context UPDATE id={match.get('id', '?')}")

    elif table == "wa_term_inventory" and operation == "update":
        match    = op["match"]
        set_vals = dict(op["set"])
        valid_cols = {
            r[1] for r in conn.execute("PRAGMA table_info(wa_term_inventory)").fetchall()
        }
        dropped = [k for k in set_vals if k not in valid_cols]
        for k in dropped:
            del set_vals[k]
        if dropped:
            print(f"  {op_id}: [NOTE] Dropped non-existent columns: {dropped}")
        if not set_vals:
            counts["skipped"] = counts.get("skipped", 0) + 1
            return
        set_clauses = ", ".join(f"{k} = ?" for k in set_vals)
        where_clauses = " AND ".join(f"{k} = ?" for k in match)
        params = list(set_vals.values()) + list(match.values())
        conn.execute(
            f"UPDATE wa_term_inventory SET {set_clauses} WHERE {where_clauses}",
            params,
        )
        counts["term_inv_updated"] = counts.get("term_inv_updated", 0) + 1
        print(f"  {op_id}: wa_term_inventory UPDATE id={match.get('id', '?')} {list(set_vals.keys())}")

    elif table == "wa_term_phase2_flags" and operation == "update":
        match    = op["match"]
        set_vals = dict(op["set"])
        valid_cols = {
            r[1] for r in conn.execute("PRAGMA table_info(wa_term_phase2_flags)").fetchall()
        }
        dropped = [k for k in set_vals if k not in valid_cols]
        for k in dropped:
            del set_vals[k]
        if dropped:
            print(f"  {op_id}: [NOTE] Dropped non-existent columns: {dropped}")
        if not set_vals:
            counts["skipped"] = counts.get("skipped", 0) + 1
            return
        set_clauses = ", ".join(f"{k} = ?" for k in set_vals)
        where_clauses = " AND ".join(f"{k} = ?" for k in match)
        params = list(set_vals.values()) + list(match.values())
        cur = conn.execute(
            f"UPDATE wa_term_phase2_flags SET {set_clauses} WHERE {where_clauses}",
            params,
        )
        if cur.rowcount == 0:
            raise ValueError(f"{op_id}: no wa_term_phase2_flags row matched {match}")
        counts["phase2_flags_updated"] = counts.get("phase2_flags_updated", 0) + 1
        print(f"  {op_id}: wa_term_phase2_flags UPDATE {match} {list(set_vals.keys())}")

    elif table == "word_registry" and operation == "update":
        match    = op["match"]
        set_vals = dict(op["set"])
        # Filter out columns that don't exist on word_registry
        valid_cols = {
            r[1] for r in conn.execute("PRAGMA table_info(word_registry)").fetchall()
        }
        dropped = [k for k in set_vals if k not in valid_cols]
        for k in dropped:
            del set_vals[k]
        if dropped:
            print(f"  {op_id}: [NOTE] Dropped non-existent columns: {dropped}")
        set_clauses = ", ".join(f"{k} = ?" for k in set_vals)
        where_clauses = " AND ".join(f"{k} = ?" for k in match)
        params = list(set_vals.values()) + list(match.values())
        conn.execute(
            f"UPDATE word_registry SET {set_clauses} WHERE {where_clauses}",
            params,
        )
        counts["registry_updated"] = counts.get("registry_updated", 0) + 1
        print(f"  {op_id}: word_registry UPDATE id={match.get('id', '?')}")

    elif operation == "bulk_update":
        records = op.get("records", [])
        for rec in records:
            # Support two formats:
            # Format A: {match: {...}, set: {...}}
            # Format B: {strongs_number: "...", field1: val1, ...}  (flat, key is strongs_number)
            if "match" in rec and "set" in rec:
                match_vals = rec["match"]
                set_vals   = rec["set"]
            else:
                # Flat format: strongs_number is the match key, everything else is SET
                rec_copy = dict(rec)
                strongs  = rec_copy.pop("strongs_number", None)
                if not strongs:
                    continue
                match_vals = {"strongs_number": strongs}
                set_vals   = rec_copy
            if not set_vals:
                continue
            set_clauses   = ", ".join(f"{k} = ?" for k in set_vals)
            where_clauses = " AND ".join(f"{k} = ?" for k in match_vals)
            params = list(set_vals.values()) + list(match_vals.values())
            conn.execute(
                f"UPDATE {table} SET {set_clauses} WHERE {where_clauses}",
                params,
            )
        counts["bulk_updates"] = counts.get("bulk_updates", 0) + len(records)
        print(f"  {op_id}: {table} BULK_UPDATE {len(records)} row(s)")

    elif table == "wa_dimension_index" and operation == "update":
        match = op["match"]
        set_vals = dict(op["set"])
        di_id = match.get("id")
        # Safety: verify manual_override protection was already validated
        set_clauses = ", ".join(f"{k} = ?" for k in set_vals)
        params = list(set_vals.values()) + [di_id]
        conn.execute(
            f"UPDATE wa_dimension_index SET {set_clauses} WHERE id = ?",
            params,
        )
        counts["dim_index_updated"] = counts.get("dim_index_updated", 0) + 1
        if set_vals.get("manual_override") == 1:
            counts["dim_anchored"] = counts.get("dim_anchored", 0) + 1
        if set_vals.get("dominant_subject") is not None:
            counts["dominant_subject_assigned"] = counts.get("dominant_subject_assigned", 0) + 1
        gc = op.get("description", "")[:60]
        print(f"  {op_id}: wa_dimension_index UPDATE id={di_id} -> {set_vals.get('dimension', '?')} {gc}")

    elif table == "wa_dim_review_cluster_log" and operation == "insert":
        rec = op["record"]
        conn.execute(
            """INSERT INTO wa_dim_review_cluster_log
               (cluster, completed_date, instruction_version,
                registry_count, group_count, anchored_count, notes)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                rec.get("cluster"),
                rec.get("completed_date"),
                rec.get("instruction_version"),
                rec.get("registry_count", 0),
                rec.get("group_count", 0),
                rec.get("anchored_count", 0),
                rec.get("notes"),
            ),
        )
        counts["cluster_stamps_inserted"] = counts.get("cluster_stamps_inserted", 0) + 1
        print(f"  {op_id}: wa_dim_review_cluster_log INSERT cluster={rec.get('cluster')}")

    elif table == "wa_obs_question_catalogue" and operation == "insert":
        # Supports both single-record and rows-array format
        rows_list = op.get("rows", [])
        if not rows_list and op.get("record"):
            rows_list = [op["record"]]
        inserted = 0
        for rec in rows_list:
            conn.execute(
                """INSERT INTO wa_obs_question_catalogue
                   (question_code, section, source_word, source_registry_no,
                    question_text, pattern_type, scope, status, deleted,
                    date_added, catalogue_version)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    rec.get("question_code"),
                    rec.get("section"),
                    rec.get("source_word"),
                    rec.get("source_registry_no"),
                    rec.get("question_text"),
                    rec.get("pattern_type"),
                    rec.get("scope", "universal"),
                    rec.get("status", "active"),
                    rec.get("deleted", 0),
                    rec.get("date_added"),
                    rec.get("catalogue_version"),
                ),
            )
            inserted += 1
        counts["catalogue_inserted"] = counts.get("catalogue_inserted", 0) + inserted
        first_code = rows_list[0].get("question_code", "?") if rows_list else "?"
        print(f"  {op_id}: wa_obs_question_catalogue INSERT {inserted} row(s) ({first_code})")

    elif table == "wa_finding_catalogue_links" and operation == "insert":
        # Supports both single-record and rows-array format
        rows_list = op.get("rows", [])
        if not rows_list and op.get("record"):
            rows_list = [op["record"]]
        inserted = 0
        for rec in rows_list:
            finding_id_int = rec.get("finding_id")
            # Allow finding_id_ref resolution (same pattern as entity links)
            ref_label = rec.get("finding_id_ref") or rec.get("finding_label_ref")
            if not finding_id_int and ref_label:
                finding_id_int = _resolve_inserted_finding(ref_label)
            if not finding_id_int:
                raise ValueError(
                    f"{op_id}: wa_finding_catalogue_links insert requires finding_id"
                )
            conn.execute(
                """INSERT INTO wa_finding_catalogue_links
                   (finding_id, question_id, coverage, status, pattern_type,
                    mapped_date, validated_date, validated_by, session_b_note, delete_flagged)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    finding_id_int,
                    rec.get("question_id"),
                    rec.get("coverage"),
                    rec.get("status", "suggested"),
                    rec.get("pattern_type"),
                    rec.get("mapped_date"),
                    rec.get("validated_date"),
                    rec.get("validated_by"),
                    rec.get("session_b_note"),
                    rec.get("delete_flagged", 0),
                ),
            )
            inserted += 1
        counts["catalogue_links_inserted"] = counts.get("catalogue_links_inserted", 0) + inserted
        print(f"  {op_id}: wa_finding_catalogue_links INSERT {inserted} row(s)")

    else:
        print(f"  {op_id}: [SKIP] Unsupported operation: {operation} on {table}")
        counts["skipped"] = counts.get("skipped", 0) + 1


def _log_patch(conn, patch_id: str, meta: dict, counts: dict) -> None:
    """Record the patch application in engine_run_log."""
    conn.execute(
        """INSERT INTO engine_run_log
           (run_id, mode, target_registry_ids, started_at, completed_at, outcome, error_detail)
           VALUES (?, 'SESSION_PATCH', ?, ?, ?, 'COMPLETE', ?)""",
        (
            patch_id,
            str(meta.get("registry_id", "")),
            _now(),
            _now(),
            json.dumps(counts),
        ),
    )


def _export_sessiond_pointers(registry_no: int, word: str, patch_id: str) -> str | None:
    """Export SD_POINTER flags for a registry as a Session D pointers report."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """SELECT id, registry_id, file_id, flag_code, flag_label,
                  strongs_reference, cross_registry_id, priority,
                  session_target, description, session_raised,
                  raised_date, resolved, resolved_date, resolved_note
           FROM wa_session_research_flags
           WHERE registry_id = ? AND flag_code = 'SD_POINTER'
           ORDER BY flag_label""",
        (registry_no,),
    ).fetchall()
    conn.close()

    if not rows:
        return None

    date_str = _now()[:10].replace("-", "")
    report = {
        "_report_meta": {
            "report_type": "sessiond_pointers",
            "registry_id": registry_no,
            "word": word,
            "produced_date": _now()[:10],
            "source_patch": patch_id,
            "pointer_count": len(rows),
        },
        "pointers": [dict(r) for r in rows],
    }

    out_dir = os.path.join(os.path.dirname(__file__), "..", "data", "exports", "session_d")
    os.makedirs(out_dir, exist_ok=True)
    filename = f"wa-{registry_no}-{word}-sessiond-pointers-{date_str}.json"
    out_path = os.path.join(out_dir, filename)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2, ensure_ascii=False, default=str)
    return out_path


def apply_patch(patch_path: str, dry_run: bool = False) -> dict:
    """Apply a Session B/C/D patch file. Returns counts dict."""
    with open(patch_path, encoding="utf-8") as f:
        patch = json.load(f)

    meta      = patch.get("_patch_meta", {})
    patch_id  = meta.get("patch_id", os.path.basename(patch_path))
    ops       = patch.get("operations", [])
    sb_status = meta.get("session_b_status")

    print(f"\n{'=' * 60}")
    print(f"  SESSION PATCH: {patch_id}")
    print(f"  Registry: {meta.get('registry_id')}  |  Word: {meta.get('word')}")
    print(f"  Operations: {len(ops)}  |  {'DRY RUN' if dry_run else 'LIVE'}")
    print(f"{'=' * 60}\n")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    # Validate
    errors = _validate(conn, patch)
    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(f"  - {e}")
        conn.close()
        return {"status": "FAILED", "errors": errors}

    if dry_run:
        print("[DRY RUN] Validation passed. No changes applied.")
        conn.close()
        return {"status": "DRY_RUN", "operations": len(ops)}

    # Pre-patch backup
    try:
        backup_dest = shutil.copy2(
            DB_PATH,
            os.path.join(ARCHIVE_DIR, "..", "..", "backups",
                         f"bible_research_backup_{_now()[:19].replace('-','').replace(':','').replace('T','_')}_{patch_id}.db"),
        )
        print(f"  [BACKUP] {os.path.basename(backup_dest)}")
    except Exception as exc:
        print(f"  [WARN] Pre-patch backup failed: {exc}")

    # Apply all operations in a single transaction
    counts: dict = {}
    # Clear the per-patch finding-id resolution registry (DIR-008)
    _inserted_findings_by_label.clear()
    try:
        for op in ops:
            _apply_operation(conn, op, counts, meta)
        _log_patch(conn, patch_id, meta, counts)
        # Update session_b_status on the registry (skip for exempt types)
        patch_reg_id = meta.get("registry_id")
        patch_type = meta.get("patch_type", "")
        sb_skip_types = ("CLUSTERING", "SESSIOND", "VERSECONTEXT", "VCGROUP", "VCVERSE", "DIMREVIEW", "SESSIONB_FINDINGS", "CATALOGUE")
        if patch_reg_id and sb_status and patch_type not in sb_skip_types:
            conn.execute(
                "UPDATE word_registry SET session_b_status = ? WHERE no = ?",
                (sb_status, patch_reg_id),
            )
        conn.commit()
    except Exception as exc:
        conn.rollback()
        print(f"\nERROR: {exc}\nTransaction rolled back. No changes applied.")
        conn.close()
        return {"status": "FAILED", "error": str(exc)}

    conn.close()

    # Archive the patch file on success
    archive_path = None
    try:
        os.makedirs(ARCHIVE_DIR, exist_ok=True)
        dest = os.path.join(ARCHIVE_DIR, os.path.basename(patch_path))
        shutil.move(patch_path, dest)
        archive_path = dest
    except Exception as exc:
        print(f"  [WARN] Could not archive patch: {exc}")

    # Post-apply integrity: verify context_description sync for DIMREVIEW-GRPDESC patches
    if "DIMGRPDESC" in patch_id or (patch_type and "GRPDESC" in patch_type):
        conn2 = sqlite3.connect(DB_PATH)
        conn2.row_factory = sqlite3.Row
        mismatches = conn2.execute("""
            SELECT di.id, di.group_code, di.context_description as di_desc,
                   vcg.context_description as vcg_desc
            FROM wa_dimension_index di
            JOIN verse_context_group vcg ON vcg.id = di.verse_context_group_id
            WHERE di.context_description != vcg.context_description
            AND di.delete_flagged = 0 AND vcg.delete_flagged = 0
        """).fetchall()
        if mismatches:
            print(f"\n  [INTEGRITY] {len(mismatches)} context_description mismatches found:")
            for m in mismatches[:5]:
                print(f"    di.id={m['id']} ({m['group_code']}): di!=vcg")
        else:
            print(f"\n  [INTEGRITY] context_description sync verified — all matched")
        conn2.close()

    # Export Session D pointers report if any SD_POINTER flags were inserted
    sd_report_path = None
    if counts.get("research_flags_inserted", 0) > 0 and sb_status in ("Analysis Complete", "Session B Complete"):
        patch_reg_id = meta.get("registry_id")
        patch_word = meta.get("word", "unknown")
        if patch_reg_id:
            sd_report_path = _export_sessiond_pointers(patch_reg_id, patch_word, patch_id)

    print(f"\n{'-' * 60}")
    print(f"  PATCH APPLIED: {patch_id}")
    for k, v in counts.items():
        print(f"    {k}: {v}")
    if archive_path:
        print(f"    archived: {archive_path}")
    if sd_report_path:
        print(f"    session_d_report: {sd_report_path}")
    print(f"{'-' * 60}\n")

    return {"status": "COMPLETE", "sd_report": sd_report_path, **counts}


def main():
    parser = argparse.ArgumentParser(description="Apply a Session B/C/D JSON patch")
    parser.add_argument("patch_file", help="Path to the patch JSON file")
    parser.add_argument("--dry-run", action="store_true", help="Validate without applying")
    args = parser.parse_args()

    if not os.path.exists(args.patch_file):
        print(f"ERROR: File not found: {args.patch_file}")
        sys.exit(1)

    result = apply_patch(args.patch_file, dry_run=args.dry_run)
    if result.get("status") == "FAILED":
        sys.exit(1)


if __name__ == "__main__":
    main()
