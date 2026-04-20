"""
build_dimension_extract.py
──────────────────────────
Constructs data extracts for the Dimension Review stage.

Three extract types:
  1. Cluster extract (--cluster C01) — primary session input for Claude AI
  2. Group verification extract (--group-verify 112-003) — verse text for description correction
  3. Existing pointers extract (--pointers C01) — pre-existing Session B/D pointers

Output: data/exports/dimension_review/

Usage:
  python scripts/build_dimension_extract.py --cluster C01
  python scripts/build_dimension_extract.py --group-verify 112-003
  python scripts/build_dimension_extract.py --pointers C01
"""
import argparse
import json
import os
import sqlite3
from datetime import date

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "exports", "dimension_review")


def build_cluster_extract(conn, cluster: str, today: str) -> str:
    """Build the cluster extract per Section 9.1."""

    # Cluster registries
    regs = conn.execute("""
        SELECT wr.no as registry_no, wr.word, wr.cluster_assignment,
               wr.verse_context_status, wr.session_b_status, wr.source_list
        FROM word_registry wr
        WHERE wr.cluster_assignment = ? AND wr.phase1_status != 'Excluded'
        ORDER BY wr.no
    """, (cluster,)).fetchall()

    # Per-registry group counts
    cluster_registries = []
    for r in regs:
        counts = conn.execute("""
            SELECT COUNT(*) as total,
                SUM(CASE WHEN dimension IS NOT NULL THEN 1 ELSE 0 END) as classified,
                SUM(CASE WHEN dimension IS NULL THEN 1 ELSE 0 END) as unclassified
            FROM wa_dimension_index
            WHERE owning_registry_no = ? AND delete_flagged = 0
        """, (r["registry_no"],)).fetchone()

        cluster_registries.append({
            "registry_no": r["registry_no"],
            "word": r["word"],
            "cluster_assignment": r["cluster_assignment"],
            "verse_context_status": r["verse_context_status"],
            "session_b_status": r["session_b_status"],
            "source_list": r["source_list"],
            "total_groups": counts["total"] or 0,
            "classified_groups": counts["classified"] or 0,
            "unclassified_groups": counts["unclassified"] or 0,
        })

    # All groups for this cluster.
    # Post-DBR (M25, 2026-04-19): 8 columns dropped from wa_dimension_index
    # (mti_term_id, group_code, strongs_number, transliteration, gloss, language,
    # owning_registry_word, context_description). Recovered via joins to
    # verse_context_group, mti_terms, and word_registry.
    groups_rows = conn.execute("""
        SELECT wdi.id, wdi.verse_context_group_id,
               vcg.group_code,
               wdi.owning_registry_no,
               wr.word AS owning_registry_word,
               wdi.cluster_assignment,
               vcg.mti_term_id,
               mt.strongs_number, mt.transliteration, mt.gloss, mt.language,
               vcg.context_description,
               wdi.dimension, wdi.dimension_confidence,
               wdi.manual_override, wdi.anchor_count, wdi.related_count,
               wdi.set_aside_count, wdi.total_verse_count, wdi.delete_flagged,
               wdi.notes, wdi.last_modified, wdi.dominant_subject
        FROM wa_dimension_index wdi
        JOIN verse_context_group vcg ON vcg.id = wdi.verse_context_group_id
        LEFT JOIN mti_terms mt ON mt.id = vcg.mti_term_id
        LEFT JOIN word_registry wr ON wr.no = wdi.owning_registry_no
        WHERE wdi.cluster_assignment = ? AND wdi.delete_flagged = 0
        ORDER BY wdi.owning_registry_no, vcg.group_code
    """, (cluster,)).fetchall()

    groups = []
    empty_anchor_groups = []
    for g in groups_rows:
        gd = dict(g)
        vcg_id = g["verse_context_group_id"]

        # Anchor verses
        anchors = conn.execute("""
            SELECT vc.verse_record_id, b.name as book, vr.chapter, vr.verse_num as verse,
                   vr.verse_text
            FROM verse_context vc
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
            LEFT JOIN books b ON b.id = vr.book_id
            WHERE vc.group_id = ? AND vc.is_anchor = 1 AND vc.delete_flagged = 0
            ORDER BY b.book_order, vr.chapter, vr.verse_num
        """, (vcg_id,)).fetchall()

        # Related verses
        related = conn.execute("""
            SELECT vc.verse_record_id, b.name as book, vr.chapter, vr.verse_num as verse,
                   vr.verse_text
            FROM verse_context vc
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
            LEFT JOIN books b ON b.id = vr.book_id
            WHERE vc.group_id = ? AND vc.is_related = 1 AND vc.is_anchor = 0
                  AND vc.delete_flagged = 0
            ORDER BY b.book_order, vr.chapter, vr.verse_num
        """, (vcg_id,)).fetchall()

        gd["anchor_verses"] = [dict(r) for r in anchors]
        gd["related_verses"] = [dict(r) for r in related]

        # Root family data
        root = conn.execute("""
            SELECT rf.root_code, rf.root_language, rf.root_gloss
            FROM wa_term_root_family rf
            JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id AND ti.delete_flagged = 0
            WHERE ti.strongs_number = ? LIMIT 1
        """, (g["strongs_number"],)).fetchone()
        gd["root_code"] = root["root_code"] if root else None
        gd["root_language"] = root["root_language"] if root else None
        gd["root_gloss"] = root["root_gloss"] if root else None

        if not anchors:
            empty_anchor_groups.append(g["group_code"])

        groups.append(gd)

    result = {
        "extract_meta": {
            "extract_type": "dimension_review_cluster",
            "cluster": cluster,
            "produced_date": today,
            "produced_by": "Claude Code \u2014 WA-DimensionReview-Instruction-v1.9-2026-04-09",
            "governing_instruction": "WA-DimensionReview-Instruction-v1.9-2026-04-09",
            "row_count": len(groups),
        },
        "cluster_registries": cluster_registries,
        "groups": groups,
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    filename = f"wa-dim-{cluster}-extract-{today}.json"
    out_path = os.path.join(OUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Written: {out_path}")
    print(f"Cluster: {cluster}")
    print(f"Registries: {len(cluster_registries)}")
    print(f"Groups: {len(groups)}")
    if empty_anchor_groups:
        print(f"  WARNING: {len(empty_anchor_groups)} groups with empty anchor_verses: {empty_anchor_groups[:5]}")
    return out_path


def build_group_verify_extract(conn, group_code: str, today: str) -> str:
    """Build the group verification extract per Section 9.2."""

    # Get group info
    vcg = conn.execute("""
        SELECT vcg.id, vcg.group_code, vcg.mti_term_id, vcg.context_description, vcg.notes,
               mt.strongs_number, mt.transliteration
        FROM verse_context_group vcg
        JOIN mti_terms mt ON mt.id = vcg.mti_term_id
        WHERE vcg.group_code = ?
    """, (group_code,)).fetchone()

    if not vcg:
        print(f"ERROR: group_code '{group_code}' not found")
        return ""

    # Get owning registry (post-DBR: group_code + owning_registry_word
    # no longer direct columns on wa_dimension_index — join through
    # verse_context_group and word_registry).
    di = conn.execute("""
        SELECT wdi.owning_registry_no, wr.word AS owning_registry_word
        FROM wa_dimension_index wdi
        JOIN verse_context_group vcg ON vcg.id = wdi.verse_context_group_id
        LEFT JOIN word_registry wr ON wr.no = wdi.owning_registry_no
        WHERE vcg.group_code = ? AND wdi.delete_flagged = 0
    """, (group_code,)).fetchone()

    group = {
        "id": vcg["id"],
        "group_code": vcg["group_code"],
        "mti_term_id": vcg["mti_term_id"],
        "strongs_number": vcg["strongs_number"],
        "transliteration": vcg["transliteration"],
        "owning_registry_no": di["owning_registry_no"] if di else None,
        "owning_registry_word": di["owning_registry_word"] if di else None,
        "current_description": vcg["context_description"],
        "notes": vcg["notes"],
    }

    # Get anchor verses
    anchors = conn.execute("""
        SELECT vc.verse_record_id, b.name as book, vr.chapter, vr.verse_num as verse,
               vr.verse_text, vc.is_anchor, vc.is_related
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        LEFT JOIN books b ON b.id = vr.book_id
        WHERE vc.group_id = ? AND vc.is_anchor = 1 AND vc.delete_flagged = 0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, (vcg["id"],)).fetchall()

    # Get related verses
    related = conn.execute("""
        SELECT vc.verse_record_id, b.name as book, vr.chapter, vr.verse_num as verse,
               vr.verse_text, vc.is_anchor, vc.is_related
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        LEFT JOIN books b ON b.id = vr.book_id
        WHERE vc.group_id = ? AND vc.is_related = 1 AND vc.is_anchor = 0 AND vc.delete_flagged = 0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, (vcg["id"],)).fetchall()

    result = {
        "extract_meta": {
            "extract_type": "group_description_verification",
            "group_code": group_code,
            "produced_date": today,
        },
        "group": group,
        "anchor_verses": [dict(r) for r in anchors],
        "related_verses": [dict(r) for r in related],
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    filename = f"wa-dim-{group_code}-grpverify-{today}.json"
    out_path = os.path.join(OUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Written: {out_path}")
    print(f"Group: {group_code}")
    print(f"Anchors: {len(anchors)}, Related: {len(related)}")
    return out_path


def build_existing_pointers_extract(conn, cluster: str, today: str) -> str:
    """Build the existing pointers extract per Section 9.3."""

    # Get registry ids for this cluster
    reg_ids = [r[0] for r in conn.execute("""
        SELECT id FROM word_registry
        WHERE cluster_assignment = ? AND phase1_status != 'Excluded'
    """, (cluster,)).fetchall()]

    if not reg_ids:
        print(f"No registries for cluster {cluster}")
        return ""

    placeholders = ",".join("?" for _ in reg_ids)

    # Session B findings
    findings = conn.execute(f"""
        SELECT finding_id, registry_id, finding_type, finding, raised_date, session_b_instruction
        FROM wa_session_b_findings
        WHERE registry_id IN ({placeholders})
        ORDER BY finding_id
    """, reg_ids).fetchall()

    # Session D pointers
    pointers = conn.execute(f"""
        SELECT flag_label, registry_id, flag_code, description, session_target, raised_date
        FROM wa_session_research_flags
        WHERE registry_id IN ({placeholders}) AND session_target = 'D'
        ORDER BY flag_label
    """, reg_ids).fetchall()

    result = {
        "extract_meta": {
            "extract_type": "existing_pointers",
            "cluster": cluster,
            "produced_date": today,
        },
        "session_b_findings": [dict(r) for r in findings],
        "session_d_pointers": [dict(r) for r in pointers],
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    filename = f"wa-dim-{cluster}-existing-pointers-{today}.json"
    out_path = os.path.join(OUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Written: {out_path}")
    print(f"Cluster: {cluster}")
    print(f"Session B findings: {len(findings)}")
    print(f"Session D pointers: {len(pointers)}")
    return out_path


def build_rootfamily_extract(conn, cluster: str, today: str) -> str:
    """Build the root family cluster extract per Section 9.4."""

    # Step 1: Find root codes with at least one term in this cluster
    root_codes = [r[0] for r in conn.execute("""
        SELECT DISTINCT rf.root_code
        FROM wa_term_root_family rf
        JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id AND ti.delete_flagged = 0
        JOIN wa_file_index fi ON fi.id = ti.file_id
        JOIN word_registry wr ON wr.id = fi.word_registry_fk
        WHERE wr.cluster_assignment = ?
    """, (cluster,)).fetchall()]

    if not root_codes:
        print(f"No root families for cluster {cluster}")
        return ""

    roots_out = []
    total_groups = 0
    cross_count = 0

    for rc in root_codes:
        # All terms in this root (including other clusters)
        terms = conn.execute("""
            SELECT DISTINCT ti.strongs_number, mt.transliteration, mt.gloss, mt.language,
                wr.no as reg_no, wr.word as reg_word, wr.cluster_assignment
            FROM wa_term_root_family rf
            JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id AND ti.delete_flagged = 0
            JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
              AND mt.status IN ('extracted', 'extracted_thin') AND mt.delete_flagged = 0
            JOIN wa_file_index fi ON fi.id = ti.file_id
            JOIN word_registry wr ON wr.id = fi.word_registry_fk
            WHERE rf.root_code = ?
            ORDER BY wr.no, ti.strongs_number
        """, (rc,)).fetchall()

        if not terms:
            continue

        root_meta = conn.execute(
            "SELECT root_language, root_gloss FROM wa_term_root_family WHERE root_code = ? LIMIT 1",
            (rc,),
        ).fetchone()

        in_cluster_regs = sorted(set(t["reg_no"] for t in terms if t["cluster_assignment"] == cluster))
        all_clusters = set(t["cluster_assignment"] for t in terms if t["cluster_assignment"])
        is_cross = len(all_clusters) > 1

        # Groups + anchor verses for all terms in root.
        # Post-DBR (M25): group_code, context_description, strongs_number,
        # transliteration, gloss, owning_registry_word moved out of
        # wa_dimension_index — recovered via joins.
        groups = []
        for t in terms:
            grp_rows = conn.execute("""
                SELECT vcg.group_code, vcg.context_description,
                    di.dimension,
                    di.dimension_confidence, di.dominant_subject, di.manual_override,
                    di.owning_registry_no,
                    wr.word AS owning_registry_word,
                    di.cluster_assignment,
                    di.verse_context_group_id,
                    mt2.strongs_number, mt2.transliteration, mt2.gloss
                FROM wa_dimension_index di
                JOIN verse_context_group vcg ON vcg.id = di.verse_context_group_id
                JOIN mti_terms mt2 ON mt2.id = vcg.mti_term_id
                LEFT JOIN word_registry wr ON wr.no = di.owning_registry_no
                WHERE mt2.strongs_number = ? AND di.delete_flagged = 0
                ORDER BY vcg.group_code
            """, (t["strongs_number"],)).fetchall()

            for g in grp_rows:
                anchors = conn.execute("""
                    SELECT vc.verse_record_id, b.name as book, vr.chapter,
                           vr.verse_num as verse, vr.reference, vr.verse_text
                    FROM verse_context vc
                    JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
                    LEFT JOIN books b ON b.id = vr.book_id
                    WHERE vc.group_id = ? AND vc.is_anchor = 1 AND vc.delete_flagged = 0
                    ORDER BY b.book_order, vr.chapter, vr.verse_num
                """, (g["verse_context_group_id"],)).fetchall()

                groups.append({
                    "group_code": g["group_code"],
                    "context_description": g["context_description"],
                    "strongs_number": g["strongs_number"],
                    "transliteration": g["transliteration"],
                    "gloss": g["gloss"],
                    "registry_no": g["owning_registry_no"],
                    "registry_word": g["owning_registry_word"],
                    "cluster_assignment": g["cluster_assignment"],
                    "dimension": g["dimension"],
                    "dimension_confidence": g["dimension_confidence"],
                    "dominant_subject": g["dominant_subject"],
                    "manual_override": g["manual_override"],
                    "anchor_verses": [dict(a) for a in anchors],
                })

        if is_cross:
            cross_count += 1
        total_groups += len(groups)

        roots_out.append({
            "root_code": rc,
            "root_language": root_meta["root_language"] if root_meta else None,
            "root_gloss": root_meta["root_gloss"] if root_meta else None,
            "in_cluster_registries": in_cluster_regs,
            "cross_registry": is_cross,
            "term_count": len(terms),
            "group_count": len(groups),
            "terms": [{
                "strongs_number": t["strongs_number"],
                "transliteration": t["transliteration"],
                "gloss": t["gloss"],
                "language": t["language"],
                "reg_no": t["reg_no"],
                "reg_word": t["reg_word"],
                "cluster_assignment": t["cluster_assignment"],
                "in_current_cluster": t["cluster_assignment"] == cluster,
            } for t in terms],
            "groups": groups,
        })

    result = {
        "extract_meta": {
            "extract_type": "dimension_review_rootfamily",
            "cluster": cluster,
            "produced_date": today,
            "produced_by": "Claude Code \u2014 WA-DimensionReview-Instruction-v1.9-2026-04-09",
            "governing_instruction": "WA-DimensionReview-Instruction-v1.9-2026-04-09",
            "root_count": len(roots_out),
            "group_count": total_groups,
            "cross_registry_root_count": cross_count,
        },
        "roots": roots_out,
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    filename = f"wa-dim-{cluster}-rootfamily-{today}.json"
    out_path = os.path.join(OUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    fsize = os.path.getsize(out_path)
    print(f"Written: {out_path}")
    print(f"Cluster: {cluster}")
    print(f"Roots: {len(roots_out)} ({cross_count} cross-registry)")
    print(f"Groups: {total_groups}")
    print(f"Size: {fsize / 1024:.0f} KB")
    return out_path


def _current_dimension_vocab(conn) -> set:
    """Return current §7.7 dimension vocabulary — sourced from wa_dimension_index
    rows that have been reviewed under the current instruction version (i.e.
    dimension_confidence = 'CLAUDE_AI' AND labels that match the known current set).

    Current v3.11.0 vocabulary (from wa-reference-v5_7 / prior DimReview v3.3):
    these are the labels the instruction's §7.7 catalogue defines.
    """
    return {
        "Emotion — Positive", "Emotion — Negative",
        "Cognition", "Volition",
        "Moral Character", "Relational Disposition",
        "Vitality / Existence", "Attentiveness / Awareness",
        "Agency / Power", "Dependence / Creatureliness",
        "Divine-Human Correspondence",
        "Transformation",
    }


def run_cluster_prechecks(conn, cluster: str) -> dict:
    """Run DV-1..DV-5 pre-checks on a cluster and return structured results.

    - DV-1 dimension-vocabulary vintage (current vs legacy per registry)
    - DV-2 manual-override lock distribution per registry
    - DV-3 dominant_subject='NONE' literal-string count
    - DV-4 rootfamily false-positive candidates (root_language IS NULL AND root_gloss IS NULL)
    - DV-5 flags file reference (resolved [current] path)
    """
    current_vocab = _current_dimension_vocab(conn)

    # Per-registry breakdown
    regs = conn.execute("""
        SELECT wr.id, wr.no, wr.word, wr.dim_review_status,
               wr.session_b_status, wr.verse_context_status
          FROM word_registry wr
         WHERE wr.cluster_assignment = ? AND wr.phase1_status != 'Excluded'
         ORDER BY wr.no
    """, (cluster,)).fetchall()

    per_registry = []
    for r in regs:
        # All active dim_index rows for this registry
        dim_rows = conn.execute("""
            SELECT dimension, dimension_confidence, manual_override, dominant_subject
              FROM wa_dimension_index
             WHERE owning_registry_no = ? AND delete_flagged = 0
        """, (r["no"],)).fetchall()
        total = len(dim_rows)
        current_count = sum(1 for d in dim_rows if d["dimension"] in current_vocab)
        legacy_count = sum(1 for d in dim_rows
                           if d["dimension"] not in current_vocab and d["dimension"])
        null_count = sum(1 for d in dim_rows if d["dimension"] is None)
        mo_locked = sum(1 for d in dim_rows if (d["manual_override"] or 0) == 1)
        mo_open = sum(1 for d in dim_rows if (d["manual_override"] or 0) == 0)
        none_literal = sum(1 for d in dim_rows if d["dominant_subject"] == "NONE")

        # Legacy-label histogram for this registry
        from collections import Counter
        legacy_hist = Counter(
            d["dimension"] for d in dim_rows
            if d["dimension"] and d["dimension"] not in current_vocab
        )

        per_registry.append(dict(
            registry_no=r["no"],
            word=r["word"],
            dim_review_status=r["dim_review_status"],
            session_b_status=r["session_b_status"],
            verse_context_status=r["verse_context_status"],
            total_groups=total,
            dimension_current_vocab=current_count,
            dimension_legacy_vocab=legacy_count,
            dimension_null=null_count,
            manual_override_locked=mo_locked,
            manual_override_open=mo_open,
            dominant_subject_none_literal=none_literal,
            legacy_label_histogram=dict(legacy_hist),
        ))

    # Programme-wide rootfamily false-positive check for this cluster
    roots_suspect = conn.execute("""
        SELECT DISTINCT rf.root_code
          FROM wa_term_root_family rf
          JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id
          JOIN wa_file_index fi ON fi.id = ti.file_id
          JOIN word_registry wr ON wr.id = fi.word_registry_fk
         WHERE wr.cluster_assignment = ?
           AND rf.delete_flagged = 0
           AND rf.root_language IS NULL
           AND rf.root_gloss IS NULL
    """, (cluster,)).fetchall()
    suspect_roots = [r["root_code"] for r in roots_suspect]

    # Flags file resolution — find highest-numbered wa-global-flags-v*-*.md
    import glob
    flags_candidates = sorted(glob.glob(os.path.join(
        os.path.dirname(__file__), "..",
        "data", "imports", "WA", "Workflow", "Framework_B", "Session_B",
        "wa-global-flags-v*.md"
    )))
    flags_resolved = os.path.basename(flags_candidates[-1]) if flags_candidates else None

    # Target vs excluded registries (target = DR status NULL)
    targets = [r for r in per_registry if r["dim_review_status"] in (None, "")]
    completed = [r for r in per_registry if r["dim_review_status"] == "Complete"]

    return dict(
        cluster=cluster,
        per_registry=per_registry,
        targets=targets,
        completed_registries=completed,
        flags_file_resolved=flags_resolved,
        rootfamily_suspect_roots=suspect_roots,
        current_vocab_set=sorted(current_vocab),
    )


def build_handoff_document(conn, cluster: str, today: str,
                           prechecks: dict, overrides: list | None = None) -> str:
    """Author the handoff kickoff .md for a DimReview batch.

    Filename: wa-dim-{cluster}-handoff-kickoff-v1-{today}.md
    Target dir: data/imports/WA/Session_B_Dimension_Review/
    """
    out_dir = os.path.join(
        os.path.dirname(__file__), "..",
        "data", "imports", "WA", "Session_B_Dimension_Review"
    )
    os.makedirs(out_dir, exist_ok=True)
    # Compact YYYYMMDD per docs/file-organisation-rules.md §Date format
    compact_today = today.replace("-", "")
    filename = f"wa-dim-{cluster}-handoff-kickoff-v1-{compact_today}.md"
    path = os.path.join(out_dir, filename)

    targets = prechecks["targets"]
    completed = prechecks["completed_registries"]
    total_target_groups = sum(t["total_groups"] for t in targets)

    lines = []
    lines.append(f"# {cluster} Dimension Review — Handoff Kickoff — {today}\n")

    # Header metadata
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f"| Cluster | {cluster} |")
    lines.append("| Purpose | Kickoff DimReview on target registries (dim_review_status = NULL) |")
    lines.append("| Primary audience | Claude AI (DimReview analyst) |")
    lines.append("| Governing instruction | `wa-dimensionreview-instruction [current]` |")
    lines.append(f"| Produced by | Claude Code (`build_dimension_extract.py --bundle`) |")
    lines.append(f"| Produced date | {today} |")
    lines.append("| Status | **READY FOR CLAUDE AI** — pre-checks run; awaiting researcher handoff signal |")
    lines.append("")
    lines.append("---\n")

    # 1. Scope
    lines.append("## 1. Scope\n")
    if targets:
        lines.append(f"**Target registries** ({len(targets)} — dim_review_status = NULL):\n")
        lines.append("| Reg | Word | OWNER terms | XREF terms | Active groups | VC | SB status |")
        lines.append("|---:|---|---|---|---:|---|---|")
        for t in targets:
            # Supplement with term counts for header
            reg_id = conn.execute("SELECT id FROM word_registry WHERE no = ?", (t["registry_no"],)).fetchone()["id"]
            own = conn.execute("""
                SELECT COUNT(*) FROM wa_term_inventory ti
                 WHERE ti.term_owner_type='OWNER' AND ti.delete_flagged=0
                   AND ti.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk=?)
            """, (reg_id,)).fetchone()[0]
            xref = conn.execute("""
                SELECT COUNT(*) FROM wa_term_inventory ti
                 WHERE ti.term_owner_type='XREF' AND ti.delete_flagged=0
                   AND ti.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk=?)
            """, (reg_id,)).fetchone()[0]
            lines.append(f"| {t['registry_no']} | {t['word']} | {own} | {xref} | "
                         f"{t['total_groups']} | {t['verse_context_status']} | {t['session_b_status']} |")
        lines.append("")
        lines.append(f"**Total target groups:** {total_target_groups}.\n")
    else:
        lines.append("_No target registries (all cluster members are DR=Complete)._\n")

    if completed:
        lines.append(f"**Already-reviewed registries** ({len(completed)} — included in cluster extract as cross-registry context; NOT review targets):\n")
        lines.append("| Reg | Word | DR status |")
        lines.append("|---:|---|---|")
        for c in completed:
            lines.append(f"| {c['registry_no']} | {c['word']} | {c['dim_review_status']} |")
        lines.append("")
    lines.append("---\n")

    # 2. Inputs
    lines.append("## 2. Inputs — extract files\n")
    lines.append(f"Generated {today} against schema v3.11.0 (post-M31). All land in `data/exports/dimension_review/`.\n")
    lines.append("| File | Purpose |")
    lines.append("|---|---|")
    lines.append(f"| `wa-dim-{cluster}-extract-{today}.json` | Cluster extract — primary Phase A/B input |")
    lines.append(f"| `wa-dim-{cluster}-existing-pointers-{today}.json` | Existing Session B findings + Session D pointers |")
    lines.append(f"| `wa-dim-{cluster}-rootfamily-{today}.json` | Root-family map (supporting Phase A cluster-coherence) |")
    lines.append("")
    if prechecks["flags_file_resolved"]:
        lines.append(f"**GR-LOAD-001 compliance:** Load the flags file "
                     f"`data/imports/WA/Workflow/Framework_B/Session_B/"
                     f"{prechecks['flags_file_resolved']}` at session start before doing any analytical work.\n")
    else:
        lines.append("**GR-LOAD-001:** _No `wa-global-flags-v*.md` found in the workflow directory._ Load whatever the researcher provides at session start.\n")
    lines.append("---\n")

    # 3. Pre-checks
    lines.append("## 3. Pre-checks (DV-1..DV-5) — run at build time\n")
    lines.append("These are computed from the live DB at bundle-build time so Claude AI has the data-quality picture before analytical work begins.\n")

    # DV-1 vocabulary vintage
    lines.append("### DV-1 Dimension vocabulary vintage\n")
    lines.append("Current §7.7 catalogue assumed (`wa-reference-v5_7` + DimReview instruction): "
                 f"{len(prechecks['current_vocab_set'])} dimensions (" +
                 ", ".join(prechecks['current_vocab_set'][:6]) + ", …).\n")
    lines.append("| Reg | Word | Groups | Current vocab | Legacy vocab | NULL | Legacy labels present |")
    lines.append("|---:|---|---:|---:|---:|---:|---|")
    for r in prechecks["per_registry"]:
        legacy_labels = "; ".join(f"{k}={v}" for k, v in sorted(r["legacy_label_histogram"].items())) or "—"
        lines.append(
            f"| {r['registry_no']} | {r['word']} | {r['total_groups']} | "
            f"{r['dimension_current_vocab']} | {r['dimension_legacy_vocab']} | "
            f"{r['dimension_null']} | {legacy_labels[:140]} |"
        )
    lines.append("")
    total_legacy = sum(r["dimension_legacy_vocab"] for r in prechecks["per_registry"])
    total_current = sum(r["dimension_current_vocab"] for r in prechecks["per_registry"])
    total_null = sum(r["dimension_null"] for r in prechecks["per_registry"])
    if total_legacy > 0:
        lines.append(f"**Cluster vintage warning:** {total_legacy} of "
                     f"{total_legacy + total_current + total_null} active groups carry "
                     "**legacy-vocabulary** dimension labels. See OT-DBR-015 for programme-wide remediation. "
                     "Dimension assignments on target-registry groups should use current vocabulary only; "
                     "legacy-labelled neighbours are usable as analytical context but not as format precedent.\n")

    # DV-2 manual-override locks
    lines.append("### DV-2 Manual-override lock distribution\n")
    lines.append("| Reg | Word | MO locked | MO open | DR-8 friction at Phase C |")
    lines.append("|---:|---|---:|---:|---|")
    for r in prechecks["per_registry"]:
        friction = "LIKELY — bulk unlock required" if r["manual_override_locked"] > 10 else "minimal"
        if r["dim_review_status"] == "Complete":
            friction = "n/a (already Complete)"
        lines.append(
            f"| {r['registry_no']} | {r['word']} | {r['manual_override_locked']} | "
            f"{r['manual_override_open']} | {friction} |"
        )
    lines.append("")
    locked_targets = sum(r["manual_override_locked"] for r in targets)
    if locked_targets > 0:
        lines.append(f"**DR-8 authorisation note:** {locked_targets} target-registry groups carry `manual_override=1`. "
                     "Phase C must either (a) operate only on `manual_override=0` groups, or (b) obtain researcher "
                     "authorisation for bulk unlock. The handoff's researcher-directed DR status change from NULL → "
                     "Complete IMPLIES bulk unlock authorisation but Claude AI should confirm at Phase C startup.\n")

    # DV-3 dominant_subject NONE
    lines.append("### DV-3 `dominant_subject = 'NONE'` literal-string count (OT-DBR-012)\n")
    total_none = sum(r["dominant_subject_none_literal"] for r in prechecks["per_registry"])
    lines.append(f"Cluster total: **{total_none}**.\n")
    if total_none > 0:
        lines.append("| Reg | Word | NONE literals |")
        lines.append("|---:|---|---:|")
        for r in prechecks["per_registry"]:
            if r["dominant_subject_none_literal"] > 0:
                lines.append(f"| {r['registry_no']} | {r['word']} | {r['dominant_subject_none_literal']} |")
        lines.append("")
        lines.append("These rows are OT-DBR-012 candidates — literal `'NONE'` should be HUMAN/GOD/etc. Handle during Phase B as QA-REVIEW + Phase C reassignment.\n")
    else:
        lines.append("_No literal `'NONE'` rows in this cluster. OT-DBR-012 does not apply here._\n")

    # DV-4 rootfamily quality
    lines.append("### DV-4 Rootfamily rows with incomplete metadata (OT-DBR-016)\n")
    if prechecks["rootfamily_suspect_roots"]:
        lines.append(f"Roots with `root_language IS NULL AND root_gloss IS NULL` in this cluster: "
                     f"**{len(prechecks['rootfamily_suspect_roots'])}**.\n")
        lines.append("These rows fall into two categories — triage visually:")
        lines.append("- **Legitimate roots with incomplete metadata** (e.g. `LEV`, `KARDIA`, `PSUCHĒ`, `SARX` — well-known lexical roots). Record as OT-DBR-016 data-completeness items; usable analytically.")
        lines.append("- **String-match artefacts** (e.g. pronoun-skeleton matches across unrelated terms). Exclude from cross-registry analysis.")
        lines.append("")
        lines.append("| Root code |")
        lines.append("|---|")
        for rc in prechecks["rootfamily_suspect_roots"]:
            lines.append(f"| `{rc}` |")
        lines.append("")
        lines.append("Additional false-positives may exist WITH populated language/gloss (e.g. homonym coincidences). DV-4 does not catch those — Phase A semantic inspection remains the definitive test.\n")
    else:
        lines.append("_No rootfamily rows in this cluster with NULL language AND NULL gloss._\n")

    # DV-5 flags file (already handled above)
    lines.append("### DV-5 Flags file\n")
    lines.append(f"Resolved: `{prechecks['flags_file_resolved'] or '—'}` (see §2 above).\n")

    lines.append("---\n")

    # 4. Work to perform (stable)
    lines.append("## 4. Work to perform — Phases A, B, C\n")
    lines.append("Per `wa-dimensionreview-instruction [current]`. High-level:\n")
    lines.append("- **Phase A** — Cluster coherence (all cluster registries read; reassignment proposals if needed)")
    lines.append("- **Phase B** — Per-registry quality sweep (review targets only — see §5 override if narrowed)")
    lines.append("- **Phase C** — Per-registry dimension assignments + DIMREVIEW patches\n")

    lines.append("---\n")

    # 5. Instruction overrides
    lines.append("## 5. Instruction overrides (declared)\n")
    if overrides:
        for o in overrides:
            lines.append(f"- **Override:** {o}")
        lines.append("")
    else:
        lines.append("_No overrides declared for this batch._ If the researcher narrows Phase B scope at session time, Claude AI should log it as `[INSTRUCTION-NOTE]` in the observations log and this handoff should be regenerated with the override captured.\n")
    lines.append("---\n")

    # 6. Gotchas
    lines.append("## 6. Gotchas and cautions\n")
    lines.append("- **OT-DBR-009 `mti_terms` duplication** — designed, not executed. Extract uses canonical rows; flag any reference to deprecated rows.")
    lines.append("- **Evidence flag vocabulary (M29 live)** — use `VERSE_EVIDENCE_*` codes; legacy names (NO_VERSES, SMALL_VERSE_SAMPLE, THIN_DATA, HIGH_FREQUENCY_ANCHOR, PH2_VOLUME_LIMITATION) deprecated.")
    lines.append("- **Coverage flags are informational only** — never gate analytical processing.")
    lines.append("- **Q-COV catalogue questions** — if a group's term carries a VERSE_EVIDENCE_* flag and the dimension call depends on evidence Q-COV would surface, raise an SD pointer citing the Q-COV code rather than assigning on thin grounds.")
    lines.append("")
    lines.append("---\n")

    # 7. Hand-back
    lines.append("## 7. Hand-back to CC\n")
    lines.append("- Phase C produces a DIMREVIEW patch per target registry. Naming: `PATCH-YYYYMMDD-DIMREVIEW-{cluster}-REG{NNN}-V1.json`.")
    lines.append(f"- Observations log: `wa-dim-{cluster}-observations-v{{version}}-{today}.md`.")
    lines.append("- CC receives patches, applies via `apply_session_patch.py`, stamps `dim_review_status = Complete` per registry.\n")
    lines.append("---\n")
    lines.append(f"*End of handoff kickoff — {today}*")

    content = "\n".join(lines) + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written handoff: {path}")
    return path


def build_bundle(conn, cluster: str, today: str,
                 overrides: list | None = None) -> dict:
    """Produce the full DimReview bundle: 3 JSON extracts + pre-check handoff."""
    print(f"=== Building bundle for {cluster} ({today}) ===")
    build_cluster_extract(conn, cluster, today)
    build_existing_pointers_extract(conn, cluster, today)
    build_rootfamily_extract(conn, cluster, today)
    prechecks = run_cluster_prechecks(conn, cluster)
    handoff_path = build_handoff_document(conn, cluster, today, prechecks, overrides)
    return dict(
        cluster=cluster,
        handoff_path=handoff_path,
        prechecks_summary=dict(
            targets=len(prechecks["targets"]),
            completed=len(prechecks["completed_registries"]),
            target_total_groups=sum(t["total_groups"] for t in prechecks["targets"]),
            legacy_vocab_groups=sum(r["dimension_legacy_vocab"] for r in prechecks["per_registry"]),
            current_vocab_groups=sum(r["dimension_current_vocab"] for r in prechecks["per_registry"]),
            manual_override_locked_targets=sum(r["manual_override_locked"] for r in prechecks["targets"]),
            dominant_subject_none_total=sum(r["dominant_subject_none_literal"] for r in prechecks["per_registry"]),
            rootfamily_suspect_roots=len(prechecks["rootfamily_suspect_roots"]),
            flags_file_resolved=prechecks["flags_file_resolved"],
        ),
    )


def main():
    parser = argparse.ArgumentParser(description="Build Dimension Review extracts")
    parser.add_argument("--cluster", help="Build cluster extract for given cluster (e.g. C01)")
    parser.add_argument("--rootfamily", help="Build root family extract for given cluster")
    parser.add_argument("--group-verify", help="Build group verification extract for given group_code")
    parser.add_argument("--pointers", help="Build existing pointers extract for given cluster")
    parser.add_argument("--bundle", help="Build full bundle (3 JSONs + handoff kickoff) for cluster")
    parser.add_argument("--override", action="append", default=[],
                        help="Instruction override text to include in handoff §5 (may repeat)")
    args = parser.parse_args()

    if not any([args.cluster, args.group_verify, args.pointers, args.rootfamily, args.bundle]):
        parser.print_help()
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    today = date.today().isoformat()

    if args.bundle:
        summary = build_bundle(conn, args.bundle, today, overrides=args.override or None)
        print()
        print(f"Bundle summary for {summary['cluster']}:")
        for k, v in summary['prechecks_summary'].items():
            print(f"  {k}: {v}")

    if args.cluster:
        build_cluster_extract(conn, args.cluster, today)
    if args.rootfamily:
        build_rootfamily_extract(conn, args.rootfamily, today)
    if args.group_verify:
        build_group_verify_extract(conn, args.group_verify, today)
    if args.pointers:
        build_existing_pointers_extract(conn, args.pointers, today)

    conn.close()


if __name__ == "__main__":
    main()
