"""Readiness Sweep Pilot — read-only inspection for a single registry.

Implements phases R.A through R.H of wa-global-readiness-sweep-instruction-v1_0
for one --registry=N. Produces a findings report; does NOT apply patches.

Usage:
    python scripts/readiness_sweep_pilot.py --registry=62
    python scripts/readiness_sweep_pilot.py --registry=62 --report-only

Output:
    outputs/reports/wa-{nnn}-{word}-readinesssweep-pilot-{YYYYMMDD}.md
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

DB = "database/bible_research.db"

# ── Helpers ───────────────────────────────────────────────────────────────────


def scalar(conn, sql, params=()):
    row = conn.execute(sql, params).fetchone()
    return row[0] if row else None


def rows(conn, sql, params=()):
    return conn.execute(sql, params).fetchall()


def now_stamp():
    return datetime.now(timezone.utc).isoformat()


# ── Finding classification ────────────────────────────────────────────────────


class Finding:
    def __init__(self, phase, path, target, issue, action=None, sql_ref=None):
        self.phase = phase          # 'R.A' .. 'R.H'
        self.path = path            # 1 (patch), 2 (directive), 3 (defer), 4 (RD), 5 (outstanding)
        self.target = target        # e.g. 'wa_term_inventory.id=1234'
        self.issue = issue
        self.action = action
        self.sql_ref = sql_ref

    def as_md(self):
        return (
            f"- **Path {self.path}** · `{self.target}` — {self.issue}"
            + (f" → {self.action}" if self.action else "")
        )


class SweepState:
    def __init__(self, registry_no):
        self.registry_no = registry_no
        self.findings: list[Finding] = []
        self.summary: dict = {}

    def add(self, f: Finding):
        self.findings.append(f)

    def by_path(self):
        d = defaultdict(list)
        for f in self.findings:
            d[f.path].append(f)
        return d

    def by_phase(self):
        d = defaultdict(list)
        for f in self.findings:
            d[f.phase].append(f)
        return d


# ── Phase implementations ────────────────────────────────────────────────────


def phase_ra_registry(conn, state, wr):
    """Registry state checks (R.A)."""
    state.summary["word"] = wr["word"]
    state.summary["cluster_assignment"] = wr["cluster_assignment"]
    state.summary["session_b_status"] = wr["session_b_status"]
    state.summary["verse_context_status"] = wr["verse_context_status"]
    state.summary["dim_review_status"] = wr["dim_review_status"]
    state.summary["carry_forward"] = wr["carry_forward"]

    # Hard gates
    if wr["carry_forward"] != 1:
        state.add(Finding("R.A", 4, f"word_registry.no={wr['no']}",
                          f"carry_forward={wr['carry_forward']} — should be 1 for swept registries",
                          "RESEARCHER_DECISION: clarify excluded state"))

    if wr["verse_context_status"] != "Complete":
        state.add(Finding("R.A", 4, f"word_registry.no={wr['no']}",
                          f"verse_context_status={wr['verse_context_status']!r}",
                          "Hard gate — VC must be Complete before Session B proceeds"))

    if wr["dim_review_status"] != "Complete":
        state.add(Finding("R.A", 4, f"word_registry.no={wr['no']}",
                          f"dim_review_status={wr['dim_review_status']!r}",
                          "Hard gate — Dimension Review must complete"))

    if wr["session_b_status"] not in (None, "Pre-Analysis Complete", "Verse Context Reset",
                                       "Ready for Analysis", "Analysis Complete", "Session B Complete"):
        state.add(Finding("R.A", 4, f"word_registry.no={wr['no']}",
                          f"session_b_status={wr['session_b_status']!r} — unrecognised",
                          "RD: controlled vocabulary check"))

    # word_synopsis population (new M21 column)
    synopsis = wr["word_synopsis"] if "word_synopsis" in wr.keys() else None
    if synopsis is None or (isinstance(synopsis, str) and not synopsis.strip()):
        state.add(Finding("R.A", 3, f"word_registry.word_synopsis", "NULL",
                          "Deferred — researcher authors per Session A advice Q7"))

    # dimensions field
    dim = wr["dimensions"] if "dimensions" in wr.keys() else None
    if dim is None or dim == "":
        state.add(Finding("R.A", 4, "word_registry.dimensions", "NULL/empty",
                          "RD: Dimension Review may not have written registry-level dimension list"))


def phase_rb_terms(conn, state, registry_id, file_ids):
    """Term inventory checks (R.B) — uses mti_term_flags joins post-DBR."""
    if not file_ids:
        state.add(Finding("R.B", 4, f"word_registry.id={registry_id}",
                          "No file_id rows in wa_file_index for this registry",
                          "RD: registry has no ingested data"))
        return

    ph = ",".join("?" * len(file_ids))

    # Active OWNER terms
    owner_terms = rows(conn, f"""
        SELECT ti.id, ti.strongs_number, ti.language, ti.term_owner_type,
               ti.evidential_status, ti.occurrence_count, ti.delete_flagged,
               mt.id AS mti_id, mt.status AS mti_status, mt.owning_word,
               (SELECT COUNT(*) FROM mti_term_flags mtf
                 WHERE mtf.mti_term_id = mt.id AND mtf.flag_id = 1) AS god_flag,
               (SELECT COUNT(*) FROM mti_term_flags mtf
                 WHERE mtf.mti_term_id = mt.id AND mtf.flag_id IN (3,4)) AS somatic_flag
        FROM wa_term_inventory ti
        LEFT JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
          AND mt.owning_registry_fk = ?
        WHERE ti.file_id IN ({ph})
          AND ti.delete_flagged = 0
          AND ti.term_owner_type = 'OWNER'
    """, (registry_id, *file_ids))

    # XREF terms — per OT-DBR-010 fix (2026-04-19): filter to canonical row only.
    # Pre-fix, a naive strongs_number join against mti_terms duplication produced
    # spurious findings for every duplicate row. New logic: for each XREF, check
    # whether a canonical (extracted or extracted_thin) row exists in mti_terms
    # with owning_registry_fk pointing to SOME other registry. If not, the XREF
    # pointer is broken and is a Path 4 RD.
    xref_terms = rows(conn, f"""
        SELECT DISTINCT ti.id, ti.strongs_number, ti.term_owner_type,
               (SELECT 1 FROM mti_terms mt
                 WHERE mt.strongs_number = ti.strongs_number
                   AND mt.status IN ('extracted','extracted_thin')
                   AND mt.owning_registry_fk IS NOT NULL
                   AND mt.owning_registry_fk != ?
                 LIMIT 1) AS has_canonical
        FROM wa_term_inventory ti
        WHERE ti.file_id IN ({ph})
          AND ti.delete_flagged = 0
          AND ti.term_owner_type = 'XREF'
    """, (registry_id, *file_ids))

    state.summary["owner_terms"] = len(owner_terms)
    state.summary["xref_terms"] = len(xref_terms)
    state.summary["god_flagged_terms"] = sum(1 for t in owner_terms if t["god_flag"])
    state.summary["somatic_flagged_terms"] = sum(1 for t in owner_terms if t["somatic_flag"])

    # Strong's format check
    import re
    for t in owner_terms:
        if not re.match(r"^[HG]\d+[A-Z]?$", t["strongs_number"] or ""):
            state.add(Finding("R.B", 1,
                              f"wa_term_inventory.id={t['id']}",
                              f"malformed strongs_number={t['strongs_number']!r}",
                              "Path 1: correct format"))
        # Language vs prefix
        if t["strongs_number"]:
            prefix = t["strongs_number"][0]
            expected_lang = "Hebrew" if prefix == "H" else "Greek" if prefix == "G" else None
            if expected_lang and t["language"] != expected_lang:
                state.add(Finding("R.B", 1,
                                  f"wa_term_inventory.id={t['id']}",
                                  f"language={t['language']!r} vs Strong's prefix {prefix!r}",
                                  f"Path 1: set language={expected_lang!r}"))
        # mti_terms.status on OWNER should be extracted / extracted_thin
        if t["mti_status"] and t["mti_status"] not in ("extracted", "extracted_thin"):
            state.add(Finding("R.B", 4,
                              f"mti_terms.id={t['mti_id']}",
                              f"OWNER term has status={t['mti_status']!r}",
                              "RD: expected extracted/extracted_thin for live OWNER"))

    # XREF canonical-existence check (post OT-DBR-010 fix)
    for t in xref_terms:
        if not t["has_canonical"]:
            # No canonical (extracted/extracted_thin) mti_terms row exists for
            # this XREF's strongs. The cross-reference points nowhere.
            state.add(Finding("R.B", 4,
                              f"wa_term_inventory.id={t['id']}",
                              f"XREF term has no canonical mti_terms row (broken pointer)",
                              "RD: either restore canonical row, remove the XREF, or "
                              "reclassify — see OT-DBR-009 mti_terms dedup context"))

    # Three-number verse diagnostic per OWNER term
    for t in owner_terms:
        span = scalar(conn, """
            SELECT COUNT(*) FROM wa_verse_records
            WHERE term_inv_id = ? AND span_strong_match = 1
        """, (t["id"],))
        active = scalar(conn, """
            SELECT COUNT(*) FROM wa_verse_records
            WHERE term_inv_id = ? AND delete_flagged = 0
        """, (t["id"],))
        deleted = scalar(conn, """
            SELECT COUNT(*) FROM wa_verse_records
            WHERE term_inv_id = ? AND delete_flagged = 1
        """, (t["id"],))
        occ = t["occurrence_count"] or 0

        if span == 0 and active == 0 and deleted == 0 and occ > 0:
            state.add(Finding("R.B", 2,
                              f"wa_term_inventory.id={t['id']} ({t['strongs_number']})",
                              f"zero extraction (occ={occ}, no verse records)",
                              "Path 2 directive: re-extract + audit_word re-run (BLOCKED: OT-DBR-001)"))
        elif span > 0 and active == 0 and deleted == span:
            state.add(Finding("R.B", 2,
                              f"wa_term_inventory.id={t['id']} ({t['strongs_number']})",
                              f"span filter failure (span={span}, all deleted)",
                              "Path 2: re-extract + audit + VC (BLOCKED: OT-DBR-001)"))
        elif occ > 20 and active > 0 and active < occ * 0.2:
            # Check if SMALL_VERSE_SAMPLE flag already present
            has_flag = scalar(conn, """
                SELECT COUNT(*) FROM wa_data_quality_flags dqf
                JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id
                WHERE dqf.term_id = ? AND qft.flag_code = 'SMALL_VERSE_SAMPLE'
            """, (t["strongs_number"],))
            if not has_flag:
                state.add(Finding("R.B", 1,
                                  f"wa_data_quality_flags (term {t['strongs_number']})",
                                  f"small verse sample: active={active}, occ={occ}",
                                  "Path 1: INSERT SMALL_VERSE_SAMPLE quality flag"))


def phase_rc_verses(conn, state, file_ids):
    """Verse record quality (R.C)."""
    if not file_ids:
        return
    ph = ",".join("?" * len(file_ids))

    null_text = scalar(conn, f"""
        SELECT COUNT(*) FROM wa_verse_records
        WHERE file_id IN ({ph}) AND delete_flagged = 0
          AND (verse_text IS NULL OR verse_text = '')
    """, file_ids)
    null_span = scalar(conn, f"""
        SELECT COUNT(*) FROM wa_verse_records
        WHERE file_id IN ({ph}) AND delete_flagged = 0
          AND span_strong_match IS NULL
    """, file_ids)
    non_esv = scalar(conn, f"""
        SELECT COUNT(*) FROM wa_verse_records
        WHERE file_id IN ({ph}) AND delete_flagged = 0
          AND translation IS NOT NULL AND translation != 'ESV'
    """, file_ids)
    total_active = scalar(conn, f"""
        SELECT COUNT(*) FROM wa_verse_records
        WHERE file_id IN ({ph}) AND delete_flagged = 0
    """, file_ids)

    state.summary["active_verse_records"] = total_active

    if null_text > 0:
        state.add(Finding("R.C", 3, "wa_verse_records",
                          f"{null_text} active rows have NULL/empty verse_text",
                          "Deferred to Stage 2a verse reading"))
    if null_span > 0:
        state.add(Finding("R.C", 3, "wa_verse_records",
                          f"{null_span} active rows have NULL span_strong_match",
                          "Deferred — WR-20 inherited from audit history"))
    if non_esv > 0:
        state.add(Finding("R.C", 4, "wa_verse_records",
                          f"{non_esv} active rows have non-ESV translation",
                          "RD: confirm intentional or extraction anomaly"))


def phase_rd_groups(conn, state, registry_id):
    """Verse context groups (R.D)."""
    # dominant_subject lives on wa_dimension_index, not verse_context_group.
    groups = rows(conn, """
        SELECT vcg.id, vcg.group_code, vcg.context_description, vcg.mti_term_id,
               vcg.delete_flagged, wdi.dominant_subject
        FROM verse_context_group vcg
        JOIN mti_terms mt ON mt.id = vcg.mti_term_id
        LEFT JOIN wa_dimension_index wdi ON wdi.verse_context_group_id = vcg.id
          AND wdi.delete_flagged = 0
        WHERE mt.owning_registry_fk = ?
          AND vcg.delete_flagged = 0
    """, (registry_id,))

    state.summary["active_groups"] = len(groups)

    import re
    for g in groups:
        # group_code format: [mti_id]-[seq]
        if not re.match(r"^\d+-\d+$", g["group_code"] or ""):
            state.add(Finding("R.D", 1,
                              f"verse_context_group.id={g['id']}",
                              f"malformed group_code={g['group_code']!r}",
                              "Path 1: reformat"))
        # context_description present
        if not g["context_description"] or len(g["context_description"]) < 20:
            state.add(Finding("R.D", 4,
                              f"verse_context_group.id={g['id']}",
                              f"context_description too short/empty",
                              "RD: VC may need re-run"))
        # dominant_subject
        if g["dominant_subject"] == "NONE":
            state.add(Finding("R.D", 1,
                              f"verse_context_group.id={g['id']}",
                              f"dominant_subject='NONE'",
                              "Path 1: derive from context_description"))
        elif g["dominant_subject"] is None:
            state.add(Finding("R.D", 4,
                              f"verse_context_group.id={g['id']}",
                              f"dominant_subject=NULL",
                              "RD: requires verse reading to set"))

        # Anchor verse count
        anchor_count = scalar(conn, """
            SELECT COUNT(*) FROM verse_context
            WHERE group_id = ? AND is_anchor = 1 AND delete_flagged = 0
        """, (g["id"],))
        if anchor_count == 0:
            state.add(Finding("R.D", 2,
                              f"verse_context_group.id={g['id']}",
                              f"zero anchor verses",
                              "Path 2: VC anchor designation pass for this group"))


def phase_re_dimensions(conn, state, registry_id):
    """Dimension assignments (R.E) — post-DBR uses joins for derived columns."""
    # wa_dimension_index is now 15 cols; use joins to recover dropped fields
    dims = rows(conn, """
        SELECT wdi.id AS dim_id,
               vcg.group_code, vcg.context_description,
               vcg.mti_term_id, mt.strongs_number,
               wdi.dimension, wdi.dimension_confidence, wdi.dominant_subject,
               wdi.manual_override, wdi.delete_flagged
        FROM wa_dimension_index wdi
        JOIN verse_context_group vcg ON vcg.id = wdi.verse_context_group_id
        LEFT JOIN mti_terms mt ON mt.id = vcg.mti_term_id
        WHERE wdi.owning_registry_no = ?
          AND wdi.delete_flagged = 0
          AND vcg.delete_flagged = 0
    """, (registry_id,))

    state.summary["active_dimension_rows"] = len(dims)

    null_dim = sum(1 for d in dims if not d["dimension"])
    auto_conf = sum(1 for d in dims
                    if d["dimension_confidence"] in
                    ("KEYWORD_STRONG", "KEYWORD_WEAK", "ROOT_INFERRED", "UNCLASSIFIED"))
    null_manual = sum(1 for d in dims if d["manual_override"] is None)
    legacy_vocab = sum(
        1 for d in dims
        if d["dimension"] and "/" in d["dimension"] and " / " not in d["dimension"]
    )

    state.summary["null_dimension"] = null_dim
    state.summary["automated_confidence"] = auto_conf
    state.summary["legacy_vocab_labels"] = legacy_vocab

    if null_dim > 0:
        state.add(Finding("R.E", 2, "wa_dimension_index",
                          f"{null_dim} groups with NULL dimension",
                          "Path 2: Dimension Review sub-process"))
    if auto_conf > 0:
        state.add(Finding("R.E", 2, "wa_dimension_index",
                          f"{auto_conf} groups at non-reviewed confidence (KEYWORD_*/ROOT_INFERRED/UNCLASSIFIED)",
                          "Path 2: Dimension Review"))
    if null_manual > 0:
        state.add(Finding("R.E", 1, "wa_dimension_index",
                          f"{null_manual} rows have manual_override=NULL",
                          "Path 1: set to 0"))
    if legacy_vocab > 0:
        state.add(Finding("R.E", 5, "wa_dimension_index",
                          f"{legacy_vocab} rows use legacy slash-style dimension labels",
                          "Path 5 (outstanding): programme-wide vocabulary normalisation"))


def phase_rf_flags(conn, state, registry_id):
    """Flag, finding, catalogue counts (R.F). Informational."""
    state.summary["findings_active"] = scalar(conn, """
        SELECT COUNT(*) FROM wa_session_b_findings
        WHERE registry_id = ? AND delete_flag = 0
    """, (registry_id,))

    state.summary["research_flags_B_unresolved"] = scalar(conn, """
        SELECT COUNT(*) FROM wa_session_research_flags
        WHERE registry_id = ? AND session_target = 'B' AND resolved = 0
    """, (registry_id,)) or 0

    state.summary["research_flags_D_unresolved"] = scalar(conn, """
        SELECT COUNT(*) FROM wa_session_research_flags
        WHERE registry_id = ? AND session_target = 'D' AND resolved = 0
    """, (registry_id,)) or 0

    state.summary["phase2_flags_live"] = scalar(conn, """
        SELECT COUNT(*) FROM wa_term_phase2_flags wtpf
        JOIN wa_term_inventory ti ON ti.id = wtpf.term_inv_id
        WHERE wtpf.delete_flagged = 0
          AND ti.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = ?)
    """, (registry_id,)) or 0

    state.summary["catalogue_extensions"] = scalar(conn, """
        SELECT COUNT(*) FROM wa_obs_question_catalogue
        WHERE deleted = 0
          AND (source_registry_no = ?
               OR source_word = (SELECT word FROM word_registry WHERE id = ?))
    """, (registry_id, registry_id)) or 0


def phase_rg_supporting(conn, state, file_ids, registry_id):
    """Supporting term data (R.G). Check presence of meaning, roots, related."""
    if not file_ids:
        return
    ph = ",".join("?" * len(file_ids))

    owner_count = scalar(conn, f"""
        SELECT COUNT(*) FROM wa_term_inventory
        WHERE file_id IN ({ph}) AND delete_flagged = 0 AND term_owner_type = 'OWNER'
    """, file_ids)

    with_meaning = scalar(conn, f"""
        SELECT COUNT(DISTINCT ti.id) FROM wa_term_inventory ti
        JOIN wa_meaning_parsed wmp ON wmp.term_inv_id = ti.id
        WHERE ti.file_id IN ({ph})
          AND ti.delete_flagged = 0 AND ti.term_owner_type = 'OWNER'
    """, file_ids)

    state.summary["owner_with_meaning"] = with_meaning
    state.summary["owner_missing_meaning"] = owner_count - (with_meaning or 0)

    if owner_count and with_meaning < owner_count:
        state.add(Finding("R.G", 3,
                          "wa_meaning_parsed (coverage)",
                          f"{owner_count - with_meaning}/{owner_count} OWNER terms lack meaning parse",
                          "Deferred to per-word Stage 1 Step 1.3a review"))

    # Cross-registry links count (no delete_flagged column on this table)
    state.summary["cross_registry_links"] = scalar(conn, """
        SELECT COUNT(*) FROM wa_cross_registry_links
        WHERE linked_registry_id = ?
    """, (registry_id,)) or 0


def phase_rh_prose(conn, state, registry_id):
    """Prose coverage (R.H) — NEW post-DBR."""
    # Any prose rows for this registry?
    prose_count = scalar(conn, """
        SELECT COUNT(*) FROM prose_section
        WHERE registry_id = ? AND delete_flagged = 0 AND superseded_by_id IS NULL
    """, (registry_id,)) or 0

    state.summary["prose_section_count"] = prose_count

    # Session A section coverage (should be 6 types when Session A has run)
    session_a_count = scalar(conn, """
        SELECT COUNT(*) FROM prose_section ps
        JOIN prose_section_type pst ON pst.id = ps.section_type_id
        WHERE ps.registry_id = ? AND ps.delete_flagged = 0
          AND ps.superseded_by_id IS NULL
          AND pst.source_stage = 'session_a'
    """, (registry_id,)) or 0

    state.summary["session_a_sections"] = session_a_count

    if session_a_count == 0:
        state.add(Finding("R.H", 5, "prose_section (Session A)",
                          "No Session A sections generated for this registry",
                          "Path 5 (outstanding): generate_session_a_extract.py not yet built"))


# ── Main ──────────────────────────────────────────────────────────────────────


def main():
    p = argparse.ArgumentParser(description="Readiness Sweep Pilot (read-only)")
    p.add_argument("--registry", required=True, type=int,
                   help="Registry number (no, not id)")
    args = p.parse_args()

    conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row

    # Load registry
    wr = conn.execute(
        "SELECT * FROM word_registry WHERE no = ?", (args.registry,)
    ).fetchone()
    if not wr:
        print(f"Registry no={args.registry} not found")
        sys.exit(1)

    registry_id = wr["id"]
    word = wr["word"]

    # Load file_ids for this registry
    file_ids = [r[0] for r in conn.execute(
        "SELECT id FROM wa_file_index WHERE word_registry_fk = ?",
        (registry_id,)
    ).fetchall()]

    state = SweepState(wr["no"])
    state.summary["registry_id"] = registry_id
    state.summary["file_id_count"] = len(file_ids)

    # Execute phases R.A – R.H
    phase_ra_registry(conn, state, wr)
    phase_rb_terms(conn, state, registry_id, file_ids)
    phase_rc_verses(conn, state, file_ids)
    phase_rd_groups(conn, state, registry_id)
    phase_re_dimensions(conn, state, registry_id)
    phase_rf_flags(conn, state, registry_id)
    phase_rg_supporting(conn, state, file_ids, registry_id)
    phase_rh_prose(conn, state, registry_id)

    conn.close()

    # Produce report
    nnn = f"{args.registry:03d}"
    date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
    report_path = Path(
        f"outputs/reports/wa-{nnn}-{word}-readinesssweep-pilot-{date_str}.md"
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)

    L = []
    E = L.append
    E(f"# Readiness Sweep Pilot — r{args.registry:03d} {word}")
    E("")
    E(f"**Pilot run:** {now_stamp()}")
    E("**Mode:** read-only (no patches applied)")
    E(f"**Schema version:** 3.10.0 (post-DBR)")
    E(f"**Script:** scripts/readiness_sweep_pilot.py")
    E(f"**Instruction:** wa-global-readiness-sweep-instruction-v1_0-20260419.md (Active)")
    E("")
    E("---")
    E("")
    E("## Registry Summary")
    E("")
    E("| Field | Value |")
    E("| --- | --- |")
    for k, v in state.summary.items():
        E(f"| {k} | {v} |")
    E("")
    E("---")
    E("")
    E("## Findings by Path")
    E("")
    by_path = state.by_path()
    E("| Path | Count | Description |")
    E("| --- | --- | --- |")
    path_labels = {
        1: "Mechanical patch (Path 1)",
        2: "Sub-process directive (Path 2)",
        3: "Deferred to per-word Stage 1 (Path 3)",
        4: "RESEARCHER_DECISION (Path 4)",
        5: "Outstanding task — beyond CC skill (Path 5)",
    }
    for p_num in sorted(by_path.keys()):
        E(f"| {p_num} | {len(by_path[p_num])} | {path_labels.get(p_num, '?')} |")
    E("")
    total = sum(len(v) for v in by_path.values())
    E(f"**Total findings:** {total}")
    E("")
    E("---")
    E("")
    E("## Findings by Phase")
    E("")
    by_phase = state.by_phase()
    for ph in sorted(by_phase.keys()):
        E(f"### Phase {ph} — {len(by_phase[ph])} finding(s)")
        E("")
        if not by_phase[ph]:
            E("*(no issues)*")
        else:
            for f in by_phase[ph]:
                E(f.as_md())
        E("")
    E("")
    E("---")
    E("")
    E("## Next Actions")
    E("")
    p1 = len(by_path.get(1, []))
    p2 = len(by_path.get(2, []))
    p3 = len(by_path.get(3, []))
    p4 = len(by_path.get(4, []))
    p5 = len(by_path.get(5, []))
    E(f"- **Path 1 ({p1}):** build remediation patch with {p1} operations.")
    E(f"- **Path 2 ({p2}):** produce {p2} sub-process directive(s). "
      "Execution may be blocked by OT-DBR-001 (audit_word.py rewrite) if re-extraction involved.")
    E(f"- **Path 3 ({p3}):** record in outstanding tasks with DEFER_STAGE1 tag; "
      "resolved during per-word Stage 1 (v1.6).")
    E(f"- **Path 4 ({p4}):** present as RESEARCHER_DECISION block; await resolution.")
    E(f"- **Path 5 ({p5}):** append to outstanding tasks with capability statement.")
    E("")
    E("---")
    E("")
    E("*End of pilot report*")

    report_path.write_text("\n".join(L), encoding="utf-8")
    print(f"Wrote {report_path}")
    print(f"Findings: {total} ({', '.join(f'Path {k}={len(v)}' for k, v in sorted(by_path.items()))})")


if __name__ == "__main__":
    main()
