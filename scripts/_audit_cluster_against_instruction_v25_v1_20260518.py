"""Audit a cluster against v2_5 instruction compliance.

Read-only. Produces a markdown compliance report at:
  Sessions/Session_Clusters/{code}/WA-{code}-audit-against-v25-v1-{date}.md

Usage:
  python scripts/_audit_cluster_against_instruction_v25_v1_20260518.py --cluster M02
  python scripts/_audit_cluster_against_instruction_v25_v1_20260518.py --cluster M04

Implements the v2_5 §17.3 check list and the §17.3.1/.3.2 verdict
(surgical / phase-restart / mixed) per the instruction.

This is a first-cut implementation. Soft / pattern-based checks surface
data for researcher review; hard / SQL-based checks are definitive.
"""

from __future__ import annotations
import argparse
import os
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

DB_PATH = Path("database/bible_research.db")
INSTRUCTION = "wa-sessionb-cluster-instruction-v2_5-20260518"
SCRIPT_VERSION = "v1"
TODAY = datetime.now().strftime("%Y%m%d")

# -----------------------------------------------------------------------------
# Audit check configuration
# -----------------------------------------------------------------------------

# Forbidden grounds keywords (§4.5.1). A set_aside_reason matching any of these
# is flagged for researcher review — they may indicate the bias §2.8 targets.
# These are soft patterns: a match is an advisory flag, not a definitive
# violation. The researcher reads the specific reason and verse-meaning context
# to confirm.
FORBIDDEN_GROUNDS_PATTERNS = [
    (r"\bnot\s+god[- ]directed\b", "FB1: not God-directed"),
    (r"\bno\s+clear\s+vertical\b", "FB2: no clear vertical framing"),
    (r"\blacks?\s+theolog", "FB3: lacks theological"),
    (r"\bno\s+(?:clear|spiritual)\s+theological\b", "FB4: no clear theological"),
    (r"\bno\s+spiritual\s+(?:category|framing|content)\b", "FB5: no spiritual category"),
    (r"\btoo\s+mundane\b", "FB6: too mundane"),
    (r"\btoo\s+circumstantial\b", "FB7: too circumstantial"),
    (r"\btoo\s+(?:negative|corrupt)\s+to\s+be\b", "FB8: too negative/corrupt to be inner being"),
    (r"\bbodily\s+rather\s+than\s+spiritual\b", "FB9: bodily rather than spiritual"),
    (r"\bsensory\s+rather\s+than\s+spiritual\b", "FB10: sensory rather than spiritual"),
    (r"\bphysical\s+rather\s+than\s+spiritual\b", "FB11: physical rather than spiritual"),
    (r"\bnot\s+spiritual\b", "FB12: not spiritual"),
]

# Terse / suspicious set_aside_reason values that warrant researcher review.
# These aren't forbidden per se but they don't articulate a specific
# evidence-based reason; under v2_5 §4.5.1 the valid reasons cite a specific
# ground.
TERSE_REASONS = {
    "physical_only",
    "no_inner_being",
    "out of scope",
    "not relevant",
    "not applicable",
}

# Register-family keywords scanned in Pass A meanings (verse_context.analysis_note)
# of BOUNDARY-sub-group verses. Significant cohorts here indicate inner-being
# register families that v2_5 §1.1 brings into scope but the cluster's
# sub-group structure didn't accommodate — §8.4.1 violation.
REGISTER_FAMILY_KEYWORDS = {
    "horizontal_relational": [
        "parental", "parent", "marital", "spouse", "between people",
        "neighbour", "neighbor", "horizontal", "human-to-human",
        "between persons", "interpersonal",
    ],
    "material_sensory": [
        "luxury", "feast", "sensory", "delicate", "pampered", "refined",
        "dainty", "material delight", "wealth", "comfort-orientation",
        "indulgence", "abundance",
    ],
    "corrupt_illicit": [
        "predatory", "predator", "lustful", "lust", "envy", "covetous",
        "illicit", "corrupt joy", "seductress", "corrupt delight",
        "carnal", "wicked man",
    ],
    "circumstantial_situational": [
        "cheerful heart", "good news", "circumstance", "circumstantial",
        "situational", "good report",
    ],
    "obedience_fitting": [
        "pleasing god", "doing what pleases", "obedience", "what is acceptable",
        "pleases the father",
    ],
    "judgment_evaluative": [
        "evaluat", "judge as good", "seemed good", "consider good",
        "consider pleasing",
    ],
}

# Volume thresholds for verdict heuristic. Above threshold = blocking (recommends
# phase-restart); below = advisory (surgical fix). Researcher overrides.
VOLUME_THRESHOLDS = {
    "BOUNDARY_PENDING_BLOCKING": 5,
    "FORBIDDEN_SETASIDE_BLOCKING": 10,
    "TERSE_REASONS_BLOCKING": 20,
    "BOUNDARY_PARKING_BLOCKING": 10,
    "EVIDENCE_GROUNDING_BLOCKING": 5,
    "COMPLETENESS_BLOCKING": 5,
    "REGISTER_FAMILY_BLOCKING": 8,  # >= 8 verses of a missing register = blocking
    "PIPELINE_INCOMPLETE_BLOCKING": 1,  # any pipeline-incomplete row = blocking
    "STATUS_SUFFIX_BLOCKING": 1,  # status flag = blocking by definition
}

# Corpus-fraction thresholds for determining bounded vs systemic scope of a
# corrective action. If affected entities exceed CORPUS_FRACTION_SYSTEMIC of
# the relevant denominator, the action is flagged as systemic (cluster-wide).
CORPUS_FRACTION_SYSTEMIC = 0.50  # >50% = systemic

# -----------------------------------------------------------------------------
# Canonical corrective-action cascade
# -----------------------------------------------------------------------------
# Any verse-level structural change in a cluster cascades through up to 5
# steps. Each error type enters the cascade at a specific step. Items that
# start at later steps skip earlier ones.

CANONICAL_CASCADE = [
    {"step": 1, "phase": "Phase 2", "label": "Pass A meaning — author verse_context.analysis_note"},
    {"step": 2, "phase": "Phase 5/6", "label": "Sub-group review — fit existing sub-group OR propose new"},
    {"step": 3, "phase": "Phase 7", "label": "VCG review — fit existing VCG in target sub-group OR create new (with anchor)"},
    {"step": 4, "phase": "Phase 9/11", "label": "Findings review — does the verse confirm / extend / contradict an existing finding, or open a new one"},
    {"step": 5, "phase": "Session C", "label": "Publication review — re-publish any chapter whose cited findings substantively changed"},
]

# Map each error type to its cascade entry point and metadata. Used by
# compute_corrective_actions() to produce the per-error action plan.
#
# Fields:
#   label          — human-readable error type
#   entry_step     — step in CANONICAL_CASCADE where corrective work begins (0 = informational, no DB action)
#   skip_to_final  — True if cascade may short-circuit (e.g. verse confirmed as legitimate set-aside)
#   default_scope  — bounded | bounded-systemic | systemic
#   action_pattern — short description of the corrective action template
#   notes          — discipline reminders
ERROR_TYPE_CASCADES = {
    "missing_pass_a_meaning": {
        "label": "Verse missing Pass A meaning",
        "entry_step": 1,
        "skip_to_final": True,
        "default_scope": "bounded",
        "action_pattern": "Run Phase 2 Pass A on the affected vc_ids → cascade through 2/3/4/5 as needed",
        "notes": "Cascade may short-circuit at step 1 if the verse turns out to be a legitimate set-aside (no inner-being state). Otherwise full cascade applies.",
    },
    "missing_subgroup": {
        "label": "Verse missing sub-group assignment (cluster_subgroup_id IS NULL)",
        "entry_step": 2,
        "skip_to_final": False,
        "default_scope": "bounded",
        "action_pattern": "Review analysis_note vs existing sub-groups; assign to fit OR propose new sub-group; cascade through 3/4/5",
        "notes": "Pass A meaning already exists. Sub-group decision drives Phase 7 + Phase 9/11 follow-on.",
    },
    "missing_vcg": {
        "label": "Verse missing VCG assignment (group_id IS NULL)",
        "entry_step": 3,
        "skip_to_final": False,
        "default_scope": "bounded",
        "action_pattern": "Review meaning + sub-group placement vs existing VCGs; assign or create new VCG (with anchor)",
        "notes": "Sub-group placement already exists. VCG-level analysis only.",
    },
    "missing_anchor": {
        "label": "Term lacks active anchor (R4 violation)",
        "entry_step": 3,
        "skip_to_final": False,
        "default_scope": "bounded",
        "action_pattern": "Designate one relevant verse of the term as is_anchor=1",
        "notes": "Surgical — no cascade beyond Phase 7 anchor flag.",
    },
    "ut_verse": {
        "label": "UT verse — no verse_context row exists for the (verse_record_id, mti_term_id) pair",
        "entry_step": 1,
        "skip_to_final": True,
        "default_scope": "bounded",
        "action_pattern": "Run Phase 1 classification (relevant / set_aside / borderline); if relevant, Phase 2 + cascade",
        "notes": "Phase 1 classifier per §4.2 with v2_5 in-scope examples.",
    },
    "forbidden_setaside": {
        "label": "set_aside_reason matches §4.5.1 forbidden grounds",
        "entry_step": 1,
        "skip_to_final": True,
        "default_scope": "bounded",
        "action_pattern": "RESCUE candidate review — re-classify each as relevant under v2_5 §1.1 scope; if rescued, run Pass A + cascade. If confirmed set-aside, rewrite reason with §4.5.1-valid ground.",
        "notes": "Strong RESCUE candidates — the original reason is bias-flagged.",
    },
    "terse_setaside": {
        "label": "Terse set_aside_reason lacks specific evidence ground (e.g. 'physical_only')",
        "entry_step": 1,
        "skip_to_final": True,
        "default_scope": "bounded",
        "action_pattern": "Researcher reviews each: confirm with proper §4.5.1 evidence-based reason (no cascade) OR RESCUE → relevant + cascade",
        "notes": "Terse values may be legitimate but lack the verse-specific rationale §4.5.1 requires.",
    },
    "boundary_parking": {
        "label": "STAYS-verdict term with verses parked in {code}-BOUNDARY (§8.4.1)",
        "entry_step": 2,
        "skip_to_final": False,
        "default_scope": "bounded",
        "action_pattern": "PROMOTE-TO-SUBGROUP per §18.2 — move verse to fitting substantive sub-group; cascade through 3/4/5",
        "notes": "Existing sub-group structure can absorb these (term already has substantive sub-group home).",
    },
    "register_family": {
        "label": "Register-family cohort in BOUNDARY needing substantive sub-group (§1.1, §8.4.1)",
        "entry_step": 2,
        "skip_to_final": False,
        "default_scope": "bounded-systemic",
        "action_pattern": "Group affected verses by register family → design new sub-group(s) per §8.4 → PROMOTE the cohort → Phase 7 VCG design for new sub-group → Phase 9 findings for new sub-group → Session C publication review",
        "notes": "Multi-phase cascade per cohort. Existing M{NN}-A through M{NN}-J sub-groups remain untouched; this adds new sub-groups for the missing register families.",
    },
    "boundary_pending": {
        "label": "BOUNDARY_DECISION_PENDING flag — needs §11A disposition",
        "entry_step": 2,
        "skip_to_final": True,
        "default_scope": "bounded",
        "action_pattern": "Phase 8.5 §11A disposition: SET-ASIDE, ROUTE-TO-CLUSTER, or PROMOTE-TO-SUBGROUP per verse; cascade per disposition",
        "notes": "Each verse gets one of three dispositions; cascade depth depends on outcome.",
    },
    "placeholder_finding": {
        "label": "Placeholder cluster_finding row ('[Sub-group not separately addressed]')",
        "entry_step": 4,
        "skip_to_final": False,
        "default_scope": "bounded",
        "action_pattern": "Either: revise finding_text with substantive evidence (read sub-group verses, author) OR change finding_status to 'silent' with explicit silence rationale",
        "notes": "No verse impact. Phase 9 micro-pass on the affected finding rows only.",
    },
    "ungrounded_finding": {
        "label": "cluster_finding row with no verse / VCG / anchor reference in finding_text",
        "entry_step": 4,
        "skip_to_final": False,
        "default_scope": "bounded",
        "action_pattern": "Read finding's source verses, add explicit verse references to finding_text. If genuinely a cluster-synthesis without specific verses, add sub-group references at minimum.",
        "notes": "Phase 9 §15.2 check 1 compliance. No verse impact.",
    },
    "completeness_gap": {
        "label": "Catalogue prompt × scope cell missing cluster_finding row (§15.2 check 2)",
        "entry_step": 4,
        "skip_to_final": False,
        "default_scope": "bounded",
        "action_pattern": "Phase 9 micro-pass: author E (with verse evidence) / S (silent with rationale) / G (gap) for each missing cell; INSERT cluster_finding row",
        "notes": "Phase 9 cell-by-cell completion. Researcher may opt to filter to v2_5 T0–T7 prompts if catalogue includes legacy codes.",
    },
    "status_suffix": {
        "label": "cluster.status carries post-closure suffix (e.g. 'Terms Added')",
        "entry_step": 0,
        "skip_to_final": True,
        "default_scope": "informational",
        "action_pattern": "Umbrella signal — the underlying PIPELINE-INCOMPLETE items are the real corrective actions. Once they resolve, clear the suffix via a closure-re-attestation directive.",
        "notes": "Not a separate corrective action; resolves automatically when pipeline-completeness gaps close.",
    },
}

# Status-string patterns indicating known post-closure state that requires audit.
# These are researcher conventions appended to `cluster.status` after closure
# (e.g. "Analysis Completed (Terms Added)" or "(Verses Added)") to signal that
# the cluster has accumulated work that hasn't been processed through the v2_5
# pipeline.
STATUS_SUFFIX_PATTERNS = [
    (r"\(terms?\s+added\)", "post-closure terms added"),
    (r"\(verses?\s+added\)", "post-closure verses added"),
    (r"\(reset\)", "post-closure reset"),
    (r"\(re-?examination\)", "post-closure re-examination"),
    (r"\(amended\)", "post-closure amended"),
]

# Verse-reference regex used for evidence-grounding check. Matches "Gen 1:1",
# "1Co 13:4", "Psa 23:1-5", VCG codes "M01-E-VCG-02", and anchor markers "[A]".
VERSE_REF_RE = re.compile(
    r"\b(?:Gen|Exo|Lev|Num|Deu|Jos|Jdg|Rut|1Sa|2Sa|1Ki|2Ki|1Ch|2Ch|Ezr|Neh|Est|Job|Psa|Pro|Ecc|Sng|Isa|Jer|Lam|Eze|Dan|Hos|Joe|Amo|Oba|Jon|Mic|Nah|Hab|Zep|Hag|Zec|Mal|Mat|Mar|Luk|Joh|Act|Rom|1Co|2Co|Gal|Eph|Phi|Col|1Th|2Th|1Ti|2Ti|Tit|Phm|Heb|Jas|1Pe|2Pe|1Jo|2Jo|3Jo|Jud|Rev)\s+\d+:\d+",
    re.IGNORECASE,
)
VCG_CODE_RE = re.compile(r"M\d+-[A-Z]-VCG-\d+", re.IGNORECASE)


# -----------------------------------------------------------------------------
# Checks
# -----------------------------------------------------------------------------


def check_boundary_pending(conn, code):
    """Check 1: BOUNDARY_DECISION_PENDING flags raised by closure."""
    rows = conn.execute(
        """
        SELECT rf.id, wr.word AS registry_word, rf.strongs_reference,
               rf.description, rf.raised_date
        FROM wa_session_research_flags rf
        LEFT JOIN word_registry wr ON wr.no = rf.registry_id
        WHERE rf.flag_code = 'BOUNDARY_DECISION_PENDING'
          AND COALESCE(rf.resolved, 0) = 0
          AND rf.description LIKE ? || '%'
        ORDER BY rf.id
        """,
        (f"{code} closure",),
    ).fetchall()
    return {
        "code": "AUDIT-V25-BOUNDARY-PENDING",
        "title": "BOUNDARY_DECISION_PENDING flags unresolved",
        "section_ref": "§11A (Phase 8.5) + §15.2 check 8",
        "count": len(rows),
        "items": [
            {
                "id": r["id"],
                "registry": r["registry_word"],
                "strongs": r["strongs_reference"],
                "description": (r["description"] or "")[:200],
            }
            for r in rows
        ],
        "blocking_threshold": VOLUME_THRESHOLDS["BOUNDARY_PENDING_BLOCKING"],
        "restart_from_phase": "8.5",
    }


def check_forbidden_setaside(conn, code):
    """Check 2: set_aside_reason matching forbidden-grounds patterns (§4.5.1)."""
    rows = conn.execute(
        """
        SELECT vc.id AS vc_id, vc.verse_record_id, mt.strongs_number,
               mt.transliteration, vr.reference, vc.set_aside_reason
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE mt.cluster_code = ?
          AND vc.is_relevant = 0
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND vc.set_aside_reason IS NOT NULL
        """,
        (code,),
    ).fetchall()

    matches = []
    for r in rows:
        reason = (r["set_aside_reason"] or "").lower()
        hit_labels = []
        for pattern, label in FORBIDDEN_GROUNDS_PATTERNS:
            if re.search(pattern, reason, re.IGNORECASE):
                hit_labels.append(label)
        if hit_labels:
            matches.append({
                "vc_id": r["vc_id"],
                "reference": r["reference"],
                "strongs": r["strongs_number"],
                "transliteration": r["transliteration"],
                "reason": r["set_aside_reason"],
                "matched": hit_labels,
            })

    return {
        "code": "AUDIT-V25-FORBIDDEN-SETASIDE",
        "title": "set_aside_reason matches §4.5.1 forbidden grounds",
        "section_ref": "§4.5.1 (forbidden grounds for SET_ASIDE)",
        "count": len(matches),
        "items": matches[:50],  # cap list length in report; full count above
        "items_total": len(matches),
        "blocking_threshold": VOLUME_THRESHOLDS["FORBIDDEN_SETASIDE_BLOCKING"],
        "restart_from_phase": "1",
        "note": "Pattern-based scan; researcher should read each flagged reason in context.",
    }


def check_terse_setaside(conn, code):
    """Check 2b: terse set_aside_reason values lacking specific evidence ground."""
    rows = conn.execute(
        """
        SELECT vc.set_aside_reason, COUNT(*) AS n
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code = ?
          AND vc.is_relevant = 0
          AND COALESCE(vc.delete_flagged, 0) = 0
        GROUP BY vc.set_aside_reason
        """,
        (code,),
    ).fetchall()
    terse_hits = []
    for r in rows:
        reason = (r["set_aside_reason"] or "").strip().lower()
        if reason in TERSE_REASONS:
            terse_hits.append({
                "reason": r["set_aside_reason"],
                "count": r["n"],
            })
    total = sum(h["count"] for h in terse_hits)
    return {
        "code": "AUDIT-V25-TERSE-SETASIDE",
        "title": "Terse set_aside_reason values lack specific ground",
        "section_ref": "§4.5.1 (valid SET_ASIDE reasons require specific evidence ground)",
        "count": total,
        "items": terse_hits,
        "blocking_threshold": VOLUME_THRESHOLDS["TERSE_REASONS_BLOCKING"],
        "restart_from_phase": "1",
        "note": "Terse values like 'physical_only' are borderline. Each verse should carry a verse-specific evidence rationale.",
    }


def check_boundary_parking_residue(conn, code):
    """Check 3: verses of STAYS-verdict terms parked in BOUNDARY sub-group (§8.4.1).

    Term verdict inferred from current state:
      - Term has ALL verses in BOUNDARY → BOUNDARY-verdict (correct parking).
      - Term has SOME verses in non-BOUNDARY sub-groups → STAYS-verdict;
        any of its verses parked in BOUNDARY is a §8.4.1 violation.
    """
    # Get all terms in the cluster and tally their verse placements
    rows = conn.execute(
        """
        SELECT vc.mti_term_id, mt.strongs_number, mt.transliteration,
               cs.subgroup_code,
               COUNT(*) AS n
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        LEFT JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        WHERE mt.cluster_code = ?
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged, 0) = 0
        GROUP BY vc.mti_term_id, cs.subgroup_code
        """,
        (code,),
    ).fetchall()

    by_term = defaultdict(lambda: {"strongs": None, "translit": None, "subgroups": {}})
    for r in rows:
        by_term[r["mti_term_id"]]["strongs"] = r["strongs_number"]
        by_term[r["mti_term_id"]]["translit"] = r["transliteration"]
        by_term[r["mti_term_id"]]["subgroups"][r["subgroup_code"] or "<NULL>"] = r["n"]

    boundary_code = f"{code}-BOUNDARY"
    violations = []
    for term_id, info in by_term.items():
        sgs = info["subgroups"]
        in_boundary = sgs.get(boundary_code, 0)
        in_substantive = sum(n for sg, n in sgs.items() if sg != boundary_code and sg != "<NULL>")
        if in_boundary > 0 and in_substantive > 0:
            # STAYS-verdict (has substantive home) with verses parked in BOUNDARY
            violations.append({
                "term_id": term_id,
                "strongs": info["strongs"],
                "transliteration": info["translit"],
                "in_substantive": in_substantive,
                "parked_in_boundary": in_boundary,
                "subgroups": dict(sgs),
            })

    total_parked = sum(v["parked_in_boundary"] for v in violations)
    return {
        "code": "AUDIT-V25-BOUNDARY-PARKING",
        "title": "BOUNDARY parking-lot residue (STAYS-verdict terms with verses in BOUNDARY)",
        "section_ref": "§8.4.1 (BOUNDARY is not a parking lot)",
        "count": total_parked,
        "items": violations,
        "term_count": len(violations),
        "blocking_threshold": VOLUME_THRESHOLDS["BOUNDARY_PARKING_BLOCKING"],
        "restart_from_phase": "5",
    }


def check_evidence_grounding(conn, code):
    """Check 5: cluster_finding E-coded rows lacking verse references in text."""
    rows = conn.execute(
        """
        SELECT cf.id, cf.obs_id, oc.question_code, cf.finding_status,
               cs.subgroup_code, cf.finding_text
        FROM cluster_finding cf
        LEFT JOIN wa_obs_question_catalogue oc ON oc.obs_id = cf.obs_id
        LEFT JOIN cluster_subgroup cs ON cs.id = cf.cluster_subgroup_id
        WHERE cf.cluster_code = ?
          AND COALESCE(cf.delete_flagged, 0) = 0
          AND cf.finding_status IN ('finding', 'cluster_synthesis')
        """,
        (code,),
    ).fetchall()

    ungrounded = []
    for r in rows:
        text = r["finding_text"] or ""
        has_verse_ref = bool(VERSE_REF_RE.search(text))
        has_vcg_ref = bool(VCG_CODE_RE.search(text))
        has_anchor_bracket = bool(re.search(r"\[A\]|\[B\]|\[C\]|\[D\]|\[E\]|\[F\]|\[G\]|\[CLUSTER\]", text))
        if not (has_verse_ref or has_vcg_ref or has_anchor_bracket):
            ungrounded.append({
                "id": r["id"],
                "question_code": r["question_code"],
                "subgroup": r["subgroup_code"],
                "finding_status": r["finding_status"],
                "text_head": text[:160],
            })

    return {
        "code": "AUDIT-V25-EVIDENCE-GROUNDING",
        "title": "cluster_finding E-coded rows with no verse / VCG / anchor reference",
        "section_ref": "§15.2 check 1 (evidence-grounding)",
        "count": len(ungrounded),
        "items": ungrounded[:30],
        "items_total": len(ungrounded),
        "blocking_threshold": VOLUME_THRESHOLDS["EVIDENCE_GROUNDING_BLOCKING"],
        "restart_from_phase": "9",
        "checked_total": len(rows),
    }


def check_completeness(conn, code):
    """Check 6: prompt × scope cells with no cluster_finding row."""
    # Get all active sub-groups for the cluster + the CLUSTER scope
    sub_rows = conn.execute(
        """
        SELECT id, subgroup_code FROM cluster_subgroup
        WHERE cluster_code = ? AND COALESCE(delete_flagged, 0) = 0
        ORDER BY sort_order
        """,
        (code,),
    ).fetchall()
    subgroups = [(r["id"], r["subgroup_code"]) for r in sub_rows]

    # Get all catalogue prompts (active)
    prompt_rows = conn.execute(
        """
        SELECT obs_id, question_code FROM wa_obs_question_catalogue
        WHERE COALESCE(deleted, 0) = 0
        ORDER BY question_code
        """,
    ).fetchall()
    prompts = [(r["obs_id"], r["question_code"]) for r in prompt_rows]

    # Get existing cluster_finding cells (obs_id, cluster_subgroup_id)
    cf_rows = conn.execute(
        """
        SELECT DISTINCT obs_id, cluster_subgroup_id FROM cluster_finding
        WHERE cluster_code = ? AND COALESCE(delete_flagged, 0) = 0
        """,
        (code,),
    ).fetchall()
    existing = set((r["obs_id"], r["cluster_subgroup_id"]) for r in cf_rows)

    expected_cells = 0
    missing = []
    for obs_id, qcode in prompts:
        for sg_id, sg_code in subgroups:
            expected_cells += 1
            if (obs_id, sg_id) not in existing:
                missing.append({"obs_id": obs_id, "question_code": qcode, "subgroup": sg_code})
        # CLUSTER scope (cluster_subgroup_id = NULL)
        expected_cells += 1
        if (obs_id, None) not in existing:
            missing.append({"obs_id": obs_id, "question_code": qcode, "subgroup": "CLUSTER"})

    return {
        "code": "AUDIT-V25-COMPLETENESS",
        "title": "Catalogue prompt × scope cells with no cluster_finding row",
        "section_ref": "§15.2 check 2 (completeness)",
        "count": len(missing),
        "items": missing[:20],
        "items_total": len(missing),
        "blocking_threshold": VOLUME_THRESHOLDS["COMPLETENESS_BLOCKING"],
        "restart_from_phase": "9",
        "expected_cells": expected_cells,
        "found_cells": len(existing),
    }


def check_status_suffix(conn, code, cluster_meta):
    """Check 0: cluster.status carries a post-closure suffix (e.g. 'Terms Added').

    Researcher convention appends a parenthetical suffix to `cluster.status`
    after closure when terms/verses have been added but not yet processed. The
    presence of such a suffix is itself a blocking signal — the cluster is not
    cleanly Analysis Completed.
    """
    status = (cluster_meta.get("status") or "").lower()
    matches = []
    for pattern, label in STATUS_SUFFIX_PATTERNS:
        if re.search(pattern, status, re.IGNORECASE):
            matches.append(label)
    return {
        "code": "AUDIT-V25-STATUS-SUFFIX",
        "title": "cluster.status carries a post-closure suffix indicating un-processed additions",
        "section_ref": "§2.6 (status discipline) + cluster.status conventions",
        "count": len(matches),
        "items": [{"suffix": m} for m in matches],
        "raw_status": cluster_meta.get("status"),
        "blocking_threshold": VOLUME_THRESHOLDS["STATUS_SUFFIX_BLOCKING"],
        "restart_from_phase": "1",
        "note": "Suffix indicates post-closure work that has not been folded through the pipeline. The pipeline-completeness check (§AUDIT-V25-PIPELINE-INCOMPLETE) will name the affected terms/verses.",
    }


def check_pipeline_completeness(conn, code):
    """Pipeline-completeness check.

    For every active relevant `verse_context` row in the cluster, verify the
    minimum v2_5 pipeline outputs are present:

    - `analysis_note` populated (Phase 2 Pass A)
    - `cluster_subgroup_id` populated (Phase 6 routing)
    - `group_id` populated (Phase 7 VCG assignment)

    Also check:
    - Every term has at least one is_anchor=1 row (R4 anchor gate, §10.6)
    - No UT verse_records remain for the cluster's terms (Phase 1 ran)

    Pipeline gaps indicate post-closure additions weren't carried through.
    """
    items = []

    # 1. Missing Pass A meanings on is_relevant rows
    rows = conn.execute(
        """
        SELECT vc.id, vc.verse_record_id, mt.id AS term_id,
               mt.strongs_number, mt.transliteration, vr.reference
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE mt.cluster_code = ?
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND (vc.analysis_note IS NULL OR vc.analysis_note = '')
        """,
        (code,),
    ).fetchall()
    for r in rows:
        items.append({
            "category": "missing_pass_a_meaning",
            "vc_id": r["id"],
            "term_id": r["term_id"],
            "strongs": r["strongs_number"],
            "transliteration": r["transliteration"],
            "reference": r["reference"],
            "phase_owner": "2",
        })

    # 2. Missing cluster_subgroup_id on is_relevant rows
    rows = conn.execute(
        """
        SELECT vc.id, vc.verse_record_id, mt.id AS term_id,
               mt.strongs_number, mt.transliteration, vr.reference
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE mt.cluster_code = ?
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND vc.cluster_subgroup_id IS NULL
        """,
        (code,),
    ).fetchall()
    for r in rows:
        items.append({
            "category": "missing_subgroup",
            "vc_id": r["id"],
            "term_id": r["term_id"],
            "strongs": r["strongs_number"],
            "transliteration": r["transliteration"],
            "reference": r["reference"],
            "phase_owner": "6",
        })

    # 3. Missing group_id on is_relevant rows (no VCG assignment)
    rows = conn.execute(
        """
        SELECT vc.id, vc.verse_record_id, mt.id AS term_id,
               mt.strongs_number, mt.transliteration, vr.reference
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE mt.cluster_code = ?
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND vc.group_id IS NULL
        """,
        (code,),
    ).fetchall()
    for r in rows:
        items.append({
            "category": "missing_vcg",
            "vc_id": r["id"],
            "term_id": r["term_id"],
            "strongs": r["strongs_number"],
            "transliteration": r["transliteration"],
            "reference": r["reference"],
            "phase_owner": "7",
        })

    # 4. Terms without an active anchor (R4 violation)
    rows = conn.execute(
        """
        SELECT mt.id AS term_id, mt.strongs_number, mt.transliteration,
               SUM(CASE WHEN vc.is_relevant=1 THEN 1 ELSE 0 END) AS rel,
               SUM(CASE WHEN vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0 THEN 1 ELSE 0 END) AS anchors
        FROM mti_terms mt
        LEFT JOIN verse_context vc ON vc.mti_term_id = mt.id AND COALESCE(vc.delete_flagged,0)=0
        WHERE mt.cluster_code = ? AND COALESCE(mt.delete_flagged,0)=0
        GROUP BY mt.id
        HAVING rel > 0 AND (anchors IS NULL OR anchors = 0)
        """,
        (code,),
    ).fetchall()
    for r in rows:
        items.append({
            "category": "missing_anchor",
            "vc_id": None,
            "term_id": r["term_id"],
            "strongs": r["strongs_number"],
            "transliteration": r["transliteration"],
            "reference": None,
            "phase_owner": "7",
            "extra": f"relevant verses={r['rel']}, anchor count={r['anchors']}",
        })

    # 5. UT verses (wa_verse_records with no verse_context row for the term)
    rows = conn.execute(
        """
        SELECT vr.id AS vr_id, vr.reference, mt.id AS term_id,
               mt.strongs_number, mt.transliteration
        FROM wa_verse_records vr
        JOIN mti_terms mt ON mt.id = vr.mti_term_id
        LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id AND vc.mti_term_id = mt.id
        WHERE mt.cluster_code = ?
          AND COALESCE(vr.delete_flagged, 0) = 0
          AND vc.id IS NULL
        """,
        (code,),
    ).fetchall()
    for r in rows:
        items.append({
            "category": "ut_verse",
            "vc_id": None,
            "term_id": r["term_id"],
            "strongs": r["strongs_number"],
            "transliteration": r["transliteration"],
            "reference": r["reference"],
            "phase_owner": "1",
            "extra": f"vr_id={r['vr_id']}",
        })

    # Aggregate by term and by category
    by_term = defaultdict(lambda: defaultdict(int))
    by_category = Counter()
    for item in items:
        by_category[item["category"]] += 1
        key = (item["term_id"], item["strongs"], item["transliteration"])
        by_term[key][item["category"]] += 1

    return {
        "code": "AUDIT-V25-PIPELINE-INCOMPLETE",
        "title": "Pipeline-completeness gaps (Phase 1/2/6/7 outputs missing on relevant verses)",
        "section_ref": "§4 (Phase 1) + §5 (Phase 2) + §9 (Phase 6) + §10 (Phase 7)",
        "count": len(items),
        "items": items[:50],  # cap in report
        "items_total": len(items),
        "by_category": dict(by_category),
        "by_term": [
            {
                "strongs": k[1],
                "transliteration": k[2],
                "term_id": k[0],
                "gaps": dict(v),
            }
            for k, v in sorted(by_term.items(), key=lambda kv: -sum(kv[1].values()))
        ],
        "blocking_threshold": VOLUME_THRESHOLDS["PIPELINE_INCOMPLETE_BLOCKING"],
        # Earliest phase among gaps: Phase 1 if any UT verse; otherwise the
        # earliest among 2, 6, 7. The script picks the earliest applicable phase.
        "restart_from_phase": "1" if by_category.get("ut_verse", 0) > 0 else (
            "2" if by_category.get("missing_pass_a_meaning", 0) > 0 else (
                "6" if by_category.get("missing_subgroup", 0) > 0 else (
                    "7" if (by_category.get("missing_vcg", 0) > 0 or by_category.get("missing_anchor", 0) > 0) else None
                )
            )
        ),
    }


def check_register_families_in_boundary(conn, code):
    """Soft check: scan BOUNDARY Pass A meanings for §1.1 register-family keywords.

    Significant cohorts indicate inner-being register families that v2_5
    brings into scope but the cluster's substantive sub-groups don't cover —
    a §8.4.1 / Phase 5 design defect.
    """
    rows = conn.execute(
        """
        SELECT vc.id, mt.strongs_number, mt.transliteration, vc.analysis_note,
               vr.reference
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE cs.cluster_code = ? AND cs.subgroup_code = ?
          AND vc.is_relevant = 1 AND COALESCE(vc.delete_flagged, 0) = 0
          AND vc.analysis_note IS NOT NULL
        """,
        (code, f"{code}-BOUNDARY"),
    ).fetchall()

    family_hits = defaultdict(list)
    for r in rows:
        note = (r["analysis_note"] or "").lower()
        for family, kws in REGISTER_FAMILY_KEYWORDS.items():
            for kw in kws:
                if kw in note:
                    family_hits[family].append({
                        "vc_id": r["id"],
                        "reference": r["reference"],
                        "strongs": r["strongs_number"],
                        "translit": r["transliteration"],
                        "matched_keyword": kw,
                        "note_head": (r["analysis_note"] or "")[:140],
                    })
                    break  # one keyword hit per family per verse

    families = []
    for family, hits in family_hits.items():
        # Deduplicate by vc_id
        seen = set()
        uniq = []
        for h in hits:
            if h["vc_id"] not in seen:
                seen.add(h["vc_id"])
                uniq.append(h)
        families.append({
            "family": family,
            "count": len(uniq),
            "samples": uniq[:5],
        })
    families.sort(key=lambda f: f["count"], reverse=True)
    total = sum(f["count"] for f in families)
    return {
        "code": "AUDIT-V25-REGISTER-FAMILIES",
        "title": "Inner-being register families detected in BOUNDARY (§1.1 scope) without substantive sub-group home",
        "section_ref": "§1.1 + §8.4.1",
        "count": total,
        "items": families,
        "boundary_verse_count": len(rows),
        "blocking_threshold": VOLUME_THRESHOLDS["REGISTER_FAMILY_BLOCKING"],
        "restart_from_phase": "5",
        "note": "Keyword-based scan of Pass A meanings. A significant cohort suggests Phase 5 sub-group design did not accommodate this register family.",
    }


# -----------------------------------------------------------------------------
# Corrective-actions plan
# -----------------------------------------------------------------------------


def _estimate_work(count):
    """Qualitative work estimate by item count."""
    if count == 0:
        return "none"
    if count <= 10:
        return "small"
    if count <= 100:
        return "medium"
    if count <= 500:
        return "large"
    return "very large"


def _map_finding_to_error_types(finding):
    """Map a check finding to error_type keys for corrective-action grouping.

    Returns a list of (error_type, items_or_count) tuples.
    """
    code = finding["code"]
    items = finding.get("items", []) or []

    if code == "AUDIT-V25-STATUS-SUFFIX":
        return [("status_suffix", items)]
    if code == "AUDIT-V25-PIPELINE-INCOMPLETE":
        # Bucket items by category
        by_cat = defaultdict(list)
        for it in finding.get("items", []):
            by_cat[it["category"]].append(it)
        # Categories already align with error_type keys
        out = []
        for cat in ("ut_verse", "missing_pass_a_meaning", "missing_subgroup", "missing_vcg", "missing_anchor"):
            if cat in by_cat:
                out.append((cat, by_cat[cat]))
        # Use full totals from by_category where items list was truncated
        by_cat_total = finding.get("by_category", {})
        if by_cat_total and finding.get("items_total", 0) > len(finding.get("items", [])):
            # The items list was capped; rebuild from totals
            out = []
            for cat in ("ut_verse", "missing_pass_a_meaning", "missing_subgroup", "missing_vcg", "missing_anchor"):
                if by_cat_total.get(cat, 0) > 0:
                    out.append((cat, by_cat.get(cat, [])))  # sample list (possibly truncated)
        return out
    if code == "AUDIT-V25-BOUNDARY-PENDING":
        return [("boundary_pending", items)]
    if code == "AUDIT-V25-FORBIDDEN-SETASIDE":
        return [("forbidden_setaside", items)]
    if code == "AUDIT-V25-TERSE-SETASIDE":
        return [("terse_setaside", items)]
    if code == "AUDIT-V25-BOUNDARY-PARKING":
        return [("boundary_parking", items)]
    if code == "AUDIT-V25-EVIDENCE-GROUNDING":
        # Heuristic: if text head matches placeholder pattern, mark placeholder; else ungrounded
        placeholder, ungrounded = [], []
        for it in items:
            head = (it.get("text_head") or "").lower()
            if "not separately addressed" in head or "see cluster-level finding" in head:
                placeholder.append(it)
            else:
                ungrounded.append(it)
        # The items list was capped at 30; need to scale by full count
        out = []
        total = finding.get("items_total", 0)
        if total > len(items):
            # Can't split totals reliably; report under ungrounded with note
            ungrounded_count = total
            out = [("ungrounded_finding", items)]  # samples; total recorded separately
        else:
            if placeholder:
                out.append(("placeholder_finding", placeholder))
            if ungrounded:
                out.append(("ungrounded_finding", ungrounded))
        return out
    if code == "AUDIT-V25-COMPLETENESS":
        return [("completeness_gap", items)]
    if code == "AUDIT-V25-REGISTER-FAMILIES":
        # Items here is a list of {family, count, samples}
        # Aggregate into one register_family action
        return [("register_family", items)]
    return []


def compute_corrective_actions(findings, cluster_meta, conn, code):
    """Produce a corrective-action plan: per error type, the cascade entry
    point, affected count, sample entities, scope, and estimated work.
    """
    # Aggregate count per error type. We use the finding's reported "count"
    # not the items list length (items list may be truncated for the report).
    aggregated = defaultdict(lambda: {"count": 0, "samples": [], "extra": {}})

    for f in findings:
        if f["count"] == 0:
            continue
        mappings = _map_finding_to_error_types(f)
        if f["code"] == "AUDIT-V25-PIPELINE-INCOMPLETE":
            # Use by_category for the actual counts
            by_cat = f.get("by_category", {})
            for etype, sample_items in mappings:
                aggregated[etype]["count"] += by_cat.get(etype, 0)
                aggregated[etype]["samples"].extend(sample_items[:10])
        elif f["code"] == "AUDIT-V25-EVIDENCE-GROUNDING":
            # Split placeholder vs ungrounded
            items = f.get("items", [])
            total = f.get("items_total", 0)
            placeholder_in_samples = sum(1 for it in items if "not separately addressed" in (it.get("text_head") or "").lower())
            ungrounded_in_samples = len(items) - placeholder_in_samples
            if placeholder_in_samples + ungrounded_in_samples > 0:
                ratio_placeholder = placeholder_in_samples / max(1, placeholder_in_samples + ungrounded_in_samples)
                est_placeholder = int(round(total * ratio_placeholder))
                est_ungrounded = total - est_placeholder
            else:
                est_placeholder = 0
                est_ungrounded = total
            if est_placeholder > 0:
                aggregated["placeholder_finding"]["count"] = est_placeholder
                aggregated["placeholder_finding"]["samples"].extend(
                    [it for it in items if "not separately addressed" in (it.get("text_head") or "").lower()][:10]
                )
                aggregated["placeholder_finding"]["extra"] = {"estimation_note": f"Estimated split from sample of {len(items)} (placeholder ratio {ratio_placeholder:.0%})"}
            if est_ungrounded > 0:
                aggregated["ungrounded_finding"]["count"] = est_ungrounded
                aggregated["ungrounded_finding"]["samples"].extend(
                    [it for it in items if "not separately addressed" not in (it.get("text_head") or "").lower()][:10]
                )
        elif f["code"] == "AUDIT-V25-REGISTER-FAMILIES":
            aggregated["register_family"]["count"] = f["count"]
            # Items is a list of family records
            aggregated["register_family"]["samples"] = f.get("items", [])[:20]
        else:
            for etype, sample_items in mappings:
                aggregated[etype]["count"] += f["count"]
                aggregated[etype]["samples"].extend(sample_items[:10] if isinstance(sample_items, list) else [])

    # Compute corpus denominators for scope determination
    corpus = {
        "relevant_vc_total": conn.execute(
            "SELECT COUNT(*) FROM verse_context vc JOIN mti_terms mt ON mt.id=vc.mti_term_id "
            "WHERE mt.cluster_code=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0",
            (code,),
        ).fetchone()[0],
        "term_count": conn.execute(
            "SELECT COUNT(*) FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
            (code,),
        ).fetchone()[0],
        "setaside_total": conn.execute(
            "SELECT COUNT(*) FROM verse_context vc JOIN mti_terms mt ON mt.id=vc.mti_term_id "
            "WHERE mt.cluster_code=? AND vc.is_relevant=0 AND COALESCE(vc.delete_flagged,0)=0",
            (code,),
        ).fetchone()[0],
        "cluster_finding_total": conn.execute(
            "SELECT COUNT(*) FROM cluster_finding WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
            (code,),
        ).fetchone()[0],
    }

    actions = []
    for etype, data in aggregated.items():
        if etype not in ERROR_TYPE_CASCADES:
            continue
        meta = ERROR_TYPE_CASCADES[etype]
        count = data["count"]
        # Determine scope: if count >= CORPUS_FRACTION_SYSTEMIC of relevant
        # denominator, mark as systemic; else default per meta.
        scope = meta["default_scope"]
        ratio = None
        denominator_label = None
        if etype in ("missing_pass_a_meaning", "missing_subgroup", "missing_vcg", "ut_verse", "missing_anchor", "boundary_parking", "register_family", "boundary_pending"):
            denom = corpus["relevant_vc_total"] or 1
            denominator_label = "relevant verses"
            ratio = count / denom
        elif etype in ("forbidden_setaside", "terse_setaside"):
            denom = corpus["setaside_total"] or 1
            denominator_label = "set-aside verses"
            ratio = count / denom
        elif etype in ("placeholder_finding", "ungrounded_finding"):
            denom = corpus["cluster_finding_total"] or 1
            denominator_label = "cluster_finding rows"
            ratio = count / denom
        elif etype == "completeness_gap":
            denominator_label = "expected cells"
            # Already known from check
            ratio = None
        # Systemic upgrade rule
        if ratio is not None and ratio >= CORPUS_FRACTION_SYSTEMIC:
            scope = "systemic"
        actions.append({
            "error_type": etype,
            "label": meta["label"],
            "entry_step": meta["entry_step"],
            "skip_to_final": meta["skip_to_final"],
            "action_pattern": meta["action_pattern"],
            "notes": meta["notes"],
            "count": count,
            "scope": scope,
            "ratio": ratio,
            "denominator_label": denominator_label,
            "estimated_work": _estimate_work(count),
            "samples": data["samples"][:8],
            "extra": data.get("extra", {}),
        })

    # Sort by entry_step (earliest cascade entry first), then by count desc
    actions.sort(key=lambda a: (a["entry_step"], -a["count"]))

    # Compute overall verdict from the action set
    if not actions:
        verdict_label = "COMPLIANT"
        verdict_recommendation = "No corrective actions needed. Cluster is aligned with v2_5."
    elif any(a["scope"] == "systemic" for a in actions):
        # At least one action is systemic — recommends phase-restart for that
        # scope but still bounded for others
        verdict_label = "SYSTEMIC"
        systemic_actions = [a for a in actions if a["scope"] == "systemic"]
        verdict_recommendation = (
            f"{len(systemic_actions)} systemic action(s) affect >{int(CORPUS_FRACTION_SYSTEMIC*100)}% of cluster scope. "
            "Bounded fixes are insufficient; consider phase-restart on the affected scope. Other actions are bounded surgical."
        )
    elif any(a["scope"] == "bounded-systemic" for a in actions):
        verdict_label = "BOUNDED-SYSTEMIC"
        verdict_recommendation = (
            "All actions are bounded but at least one requires new structural elements (sub-groups, VCGs). "
            "Existing cluster structure remains intact. Cluster status does not change."
        )
    else:
        verdict_label = "BOUNDED-FIXES"
        verdict_recommendation = (
            "All actions are bounded surgical fixes. Existing cluster structure remains intact. "
            "Cluster status does not change (§17.5)."
        )

    return {
        "label": verdict_label,
        "recommendation": verdict_recommendation,
        "actions": actions,
        "corpus": corpus,
    }


# -----------------------------------------------------------------------------
# Verdict computation
# -----------------------------------------------------------------------------


def compute_verdict(findings):
    """Compute audit verdict per v2_5 §17.3.1.

    Each check has a blocking threshold and a restart_from_phase.
    - All check counts below threshold → SURGICAL verdict.
    - Any check count above threshold → PHASE-RESTART (from earliest affected phase).
    - Mix → MIXED verdict listing items per category.
    """
    PHASE_ORDER = ["1", "2", "3", "5", "6", "7", "8.5", "9", "10", "11", "12"]

    blocking_items = []
    advisory_items = []
    for f in findings:
        if f["count"] == 0:
            continue
        if f["count"] >= f["blocking_threshold"]:
            blocking_items.append(f)
        else:
            advisory_items.append(f)

    if not blocking_items and not advisory_items:
        return {
            "level": "COMPLIANT",
            "recommendation": "No non-compliance findings. Cluster is aligned with v2_5.",
            "restart_from": None,
            "blocking_findings": [],
            "advisory_findings": [],
        }

    if not blocking_items:
        return {
            "level": "SURGICAL",
            "recommendation": "Surgical fix directives apply. Cluster stays Analysis Completed.",
            "restart_from": None,
            "blocking_findings": [],
            "advisory_findings": advisory_items,
        }

    # Find earliest restart-from-phase among blocking findings
    earliest = None
    for f in blocking_items:
        rfp = f["restart_from_phase"]
        if rfp is None:
            continue
        if earliest is None or PHASE_ORDER.index(rfp) < PHASE_ORDER.index(earliest):
            earliest = rfp

    level = "PHASE-RESTART" if not advisory_items else "MIXED"
    return {
        "level": level,
        "recommendation": (
            f"Restart from Phase {earliest}. Blocking findings cannot be repaired surgically. "
            "Advisory findings can be handled as surgical fixes either during the restart or before it."
        ) if earliest else "Mixed verdict; researcher decides path per blocking findings list.",
        "restart_from": earliest,
        "blocking_findings": blocking_items,
        "advisory_findings": advisory_items,
    }


# -----------------------------------------------------------------------------
# Report writer
# -----------------------------------------------------------------------------


def write_report(code, findings, verdict, cluster_meta, plan=None):
    """Write the audit compliance report as markdown."""
    out_dir = Path(f"Sessions/Session_Clusters/{code}")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"WA-{code}-audit-against-v25-{SCRIPT_VERSION}-{TODAY}.md"

    lines = []
    lines.append(f"# {code} audit against {INSTRUCTION}")
    lines.append("")
    lines.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"**Script:** `scripts/_audit_cluster_against_instruction_v25_{SCRIPT_VERSION}_{TODAY}.py`")
    lines.append(f"**Instruction version checked against:** v2_5")
    lines.append(f"**Cluster status at audit time:** {cluster_meta['status']!r}")
    lines.append(f"**Cluster version:** {cluster_meta['version']!r}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # §1 — Corrective-actions plan (new structure)
    if plan is not None:
        lines.append("## §1 — Corrective-actions plan")
        lines.append("")
        lines.append(f"**Plan verdict:** `{plan['label']}`")
        lines.append("")
        lines.append(plan["recommendation"])
        lines.append("")
        lines.append("**Cluster corpus reference (denominators for scope):**")
        c = plan["corpus"]
        lines.append(f"- relevant verse_context rows: {c['relevant_vc_total']}")
        lines.append(f"- term count: {c['term_count']}")
        lines.append(f"- set-aside vc rows: {c['setaside_total']}")
        lines.append(f"- existing cluster_finding rows: {c['cluster_finding_total']}")
        lines.append("")

        if plan["actions"]:
            lines.append("### Canonical cascade")
            lines.append("")
            for step in CANONICAL_CASCADE:
                lines.append(f"{step['step']}. **{step['phase']}** — {step['label']}")
            lines.append("")
            lines.append("### Actions (sorted by cascade entry step)")
            lines.append("")
            lines.append("| # | Error type | Entry step | Count | Scope | Work | % of denominator |")
            lines.append("|---|---|---:|---:|---|---|---|")
            for idx, a in enumerate(plan["actions"], 1):
                pct = f"{a['ratio']*100:.0f}% of {a['denominator_label']}" if a["ratio"] is not None else "—"
                lines.append(f"| {idx} | `{a['error_type']}` | {a['entry_step']} | {a['count']} | {a['scope']} | {a['estimated_work']} | {pct} |")
            lines.append("")

            lines.append("### Per-action detail")
            lines.append("")
            for idx, a in enumerate(plan["actions"], 1):
                lines.append(f"#### Action {idx} — `{a['error_type']}` ({a['count']} items, {a['scope']})")
                lines.append("")
                lines.append(f"**Cascade entry:** step {a['entry_step']}")
                if a["entry_step"] > 0:
                    entry_step = next((s for s in CANONICAL_CASCADE if s["step"] == a["entry_step"]), None)
                    if entry_step:
                        lines.append(f"  ({entry_step['phase']} — {entry_step['label']})")
                lines.append("")
                lines.append(f"**Action pattern:** {a['action_pattern']}")
                lines.append("")
                lines.append(f"**Cascade steps that may apply:**")
                if a["entry_step"] == 0:
                    lines.append("  - (informational only; no cascade)")
                else:
                    for step in CANONICAL_CASCADE:
                        if step["step"] >= a["entry_step"]:
                            applies = "applies"
                            if step["step"] > a["entry_step"] and a["skip_to_final"]:
                                applies = "may apply (cascade may short-circuit)"
                            lines.append(f"  - Step {step['step']} ({step['phase']}): {step['label']} — {applies}")
                lines.append("")
                lines.append(f"**Notes:** {a['notes']}")
                lines.append("")
                if a.get("extra", {}).get("estimation_note"):
                    lines.append(f"_{a['extra']['estimation_note']}_")
                    lines.append("")
                if a["samples"]:
                    lines.append("**Sample affected entities:**")
                    for s in a["samples"][:8]:
                        if isinstance(s, dict):
                            if "family" in s:
                                # Register-family sample
                                lines.append(f"- {s['family']}: {s['count']} verses")
                            elif "reference" in s and "strongs" in s:
                                lines.append(f"- {s.get('strongs','')} {s.get('transliteration','') or s.get('translit','')} {s.get('reference') or ''} (vc={s.get('vc_id','')})")
                            elif "question_code" in s:
                                lines.append(f"- {s['question_code']} × {s.get('subgroup','')}")
                            elif "registry" in s:
                                lines.append(f"- registry={s.get('registry')} strongs={s.get('strongs')}")
                            elif "reason" in s:
                                lines.append(f"- reason={s.get('reason','')!r}")
                            elif "suffix" in s:
                                lines.append(f"- suffix={s['suffix']}")
                            else:
                                lines.append(f"- {s}")
                    lines.append("")
                lines.append("---")
                lines.append("")
        else:
            lines.append("No corrective actions to plan. Cluster is fully aligned with v2_5.")
            lines.append("")
            lines.append("---")
            lines.append("")

    # §2 — Legacy verdict (kept for backward continuity)
    lines.append("## §2 — Legacy verdict (phase-restart framing)")
    lines.append("")
    lines.append(f"**Level:** `{verdict['level']}`")
    lines.append("")
    lines.append(f"**Recommendation:** {verdict['recommendation']}")
    if verdict["restart_from"]:
        lines.append("")
        lines.append(f"**Restart-from-phase:** Phase {verdict['restart_from']}")
        lines.append("")
        lines.append("Per v2_5 §17.3.2, the cluster.status transition for this restart is:")
        transitions = {
            "1": "`Analysis Completed` → `Data - In Progress`",
            "3": "`Analysis Completed` → `Data - In Progress`",
            "5": "`Analysis Completed` → `Analysis - In Progress`",
            "7": "`Analysis Completed` → `Analysis - In Progress`",
            "8.5": "`Analysis Completed` → `Analysis - In Progress`",
        }
        lines.append(f"  {transitions.get(verdict['restart_from'], '(see §17.3.2 table)')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # §3 — Summary table
    lines.append("## §3 — Summary by check")
    lines.append("")
    lines.append("| Check code | Count | Threshold | Severity | Section |")
    lines.append("|---|---:|---:|---|---|")
    for f in findings:
        severity = "blocking" if f["count"] >= f["blocking_threshold"] else ("advisory" if f["count"] > 0 else "clean")
        lines.append(f"| `{f['code']}` | {f['count']} | {f['blocking_threshold']} | {severity} | {f['section_ref']} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # §4 — Per-check detail
    lines.append("## §4 — Per-check detail")
    lines.append("")
    for f in findings:
        lines.append(f"### {f['code']} — {f['title']}")
        lines.append("")
        lines.append(f"**Section reference:** {f['section_ref']}")
        lines.append(f"**Count:** {f['count']}")
        lines.append(f"**Blocking threshold:** {f['blocking_threshold']}")
        if f.get("restart_from_phase"):
            lines.append(f"**If blocking, restart from:** Phase {f['restart_from_phase']}")
        if f.get("note"):
            lines.append("")
            lines.append(f"_{f['note']}_")
        lines.append("")

        if f["count"] == 0:
            lines.append("No items found. Check is clean.")
            lines.append("")
            lines.append("---")
            lines.append("")
            continue

        # Code-specific rendering
        code_key = f["code"]
        if code_key == "AUDIT-V25-STATUS-SUFFIX":
            lines.append(f"Raw cluster.status: `{f['raw_status']!r}`")
            lines.append("")
            for item in f["items"]:
                lines.append(f"- Suffix detected: {item['suffix']}")
        elif code_key == "AUDIT-V25-PIPELINE-INCOMPLETE":
            lines.append(f"Total gap items: {f['items_total']}")
            lines.append("")
            lines.append("By category:")
            for cat, n in f["by_category"].items():
                lines.append(f"- {cat}: {n}")
            lines.append("")
            lines.append("By term (highest-gap-count first):")
            for term in f["by_term"][:15]:
                lines.append(f"- {term['strongs']} {term['transliteration']} (term_id={term['term_id']}): {term['gaps']}")
            lines.append("")
            lines.append(f"Sample affected items (first {len(f['items'])}):")
            for item in f["items"][:20]:
                ref = item.get("reference") or ""
                extra = f" [{item['extra']}]" if item.get("extra") else ""
                lines.append(f"- {item['category']}: {item['strongs']} {item['transliteration']} {ref} (phase owner: {item['phase_owner']}){extra}")
        elif code_key == "AUDIT-V25-BOUNDARY-PENDING":
            for item in f["items"]:
                lines.append(f"- flag id={item['id']}, registry={item['registry']!r}, strongs={item['strongs']}")
                lines.append(f"  desc: {item['description']}")
        elif code_key == "AUDIT-V25-FORBIDDEN-SETASIDE":
            lines.append(f"Total matches: {f['items_total']} (showing first {len(f['items'])})")
            lines.append("")
            for item in f["items"]:
                lines.append(f"- vc={item['vc_id']} {item['reference']} ({item['strongs']} {item['transliteration']})")
                lines.append(f"  matched: {', '.join(item['matched'])}")
                lines.append(f"  reason: {item['reason'][:180]}")
        elif code_key == "AUDIT-V25-TERSE-SETASIDE":
            lines.append("| Reason | Count |")
            lines.append("|---|---:|")
            for item in f["items"]:
                lines.append(f"| `{item['reason']}` | {item['count']} |")
        elif code_key == "AUDIT-V25-BOUNDARY-PARKING":
            lines.append(f"Terms with §8.4.1 violation: {f['term_count']}; total parked verses: {f['count']}")
            lines.append("")
            for item in f["items"]:
                lines.append(f"- {item['strongs']} {item['transliteration']} (term_id={item['term_id']})")
                lines.append(f"  substantive verses: {item['in_substantive']}; parked in BOUNDARY: {item['parked_in_boundary']}")
                lines.append(f"  sub-group distribution: {item['subgroups']}")
        elif code_key == "AUDIT-V25-EVIDENCE-GROUNDING":
            lines.append(f"Checked {f['checked_total']} E-coded cluster_finding rows; {f['count']} ungrounded.")
            lines.append("")
            for item in f["items"]:
                lines.append(f"- cf.id={item['id']} ({item['question_code']}) sg={item['subgroup']} status={item['finding_status']}")
                lines.append(f"  text head: {item['text_head']}")
        elif code_key == "AUDIT-V25-COMPLETENESS":
            lines.append(f"Expected {f['expected_cells']} cells (prompts × scopes); found {f['found_cells']}; missing {f['count']}.")
            lines.append("")
            for item in f["items"][:20]:
                lines.append(f"- {item['question_code']} × {item['subgroup']}")
            if f.get("items_total", 0) > 20:
                lines.append(f"- … and {f['items_total'] - 20} more")
        elif code_key == "AUDIT-V25-REGISTER-FAMILIES":
            lines.append(f"BOUNDARY verses scanned: {f['boundary_verse_count']}")
            lines.append("")
            for family in f["items"]:
                if family["count"] == 0:
                    continue
                lines.append(f"**{family['family']}** — {family['count']} verses")
                for s in family["samples"]:
                    lines.append(f"- vc={s['vc_id']} {s['reference']} ({s['strongs']} {s['translit']}): {s['note_head']}")
                lines.append("")
        lines.append("")
        lines.append("---")
        lines.append("")

    # §5 — Researcher next steps
    lines.append("## §5 — Researcher next steps")
    lines.append("")
    if verdict["level"] == "COMPLIANT":
        lines.append("No action required.")
    elif verdict["level"] == "SURGICAL":
        lines.append("Approve a fix list and CC will build the surgical fix directive(s) per §17.5.")
    else:
        lines.append(f"1. Review the blocking findings above and confirm or override the recommended phase restart (Phase {verdict['restart_from']}).")
        lines.append("2. If accepting the restart, CC will build a phase-restart directive per §17.3.2: backup affected rows + status transition + roll-back ops.")
        lines.append("3. If pursuing surgical fixes despite the recommendation, approve a fix list and CC will build surgical directives per §17.5 — but note the recommendation indicates the fixes will not be sufficient on their own.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*End of compliance report. Read-only audit; no DB writes were performed.*")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cluster", required=True, help="Cluster code, e.g. M02 or M04")
    args = parser.parse_args()

    code = args.cluster
    if not DB_PATH.exists():
        print(f"DB not found: {DB_PATH}", file=sys.stderr)
        sys.exit(2)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    meta_row = conn.execute(
        "SELECT status, version FROM cluster WHERE cluster_code = ?", (code,)
    ).fetchone()
    if not meta_row:
        print(f"Cluster not found: {code}", file=sys.stderr)
        sys.exit(2)
    cluster_meta = {"status": meta_row["status"], "version": meta_row["version"]}

    print(f"Auditing cluster {code} (status={cluster_meta['status']!r}) against v2_5 ...")

    findings = []
    findings.append(check_status_suffix(conn, code, cluster_meta))
    findings.append(check_pipeline_completeness(conn, code))
    findings.append(check_boundary_pending(conn, code))
    findings.append(check_forbidden_setaside(conn, code))
    findings.append(check_terse_setaside(conn, code))
    findings.append(check_boundary_parking_residue(conn, code))
    findings.append(check_evidence_grounding(conn, code))
    findings.append(check_completeness(conn, code))
    findings.append(check_register_families_in_boundary(conn, code))

    verdict = compute_verdict(findings)
    plan = compute_corrective_actions(findings, cluster_meta, conn, code)
    out_path = write_report(code, findings, verdict, cluster_meta, plan=plan)

    print(f"\nAudit complete. Report: {out_path}")
    print(f"Corrective-actions plan: {plan['label']}")
    print(f"Number of actions: {len(plan['actions'])}")
    for a in plan["actions"]:
        ratio_str = f", {a['ratio']*100:.0f}%" if a["ratio"] is not None else ""
        print(f"  - {a['error_type']}: {a['count']} items, entry step {a['entry_step']}, scope={a['scope']} ({a['estimated_work']}{ratio_str})")
    print(f"\nLegacy phase-restart verdict (informational): {verdict['level']}")
    if verdict["restart_from"]:
        print(f"  restart-from: Phase {verdict['restart_from']}")

    conn.close()


if __name__ == "__main__":
    main()
