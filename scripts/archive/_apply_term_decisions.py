"""
_apply_term_decisions.py
────────────────────────
Reads a Phase 1 term_map JSON (output of _discover_word_terms.py) and applies
three programmatic filters to assign every term a decision group and action.

The two structural fields that the triage document encodes only in Markdown
headers — step_parent_code and step_section_type — are present in the JSON
as the cluster they belong to.  This script makes them explicit on every term.

Decision groups (from the analysis):
  G1  — Soul sub-glosses        (H5315G–N, G5590G–K)             → include
  G2  — Soul root-family        (H5314, G5590 compounds)          → include
  G2r — Soul STEP-related, root unverified  (H5317 etc.)          → review
  G3  — Proper nouns            (is_proper_noun = True)           → exclude
  G4  — Grammatical particles   (vocab_count > PARTICLE_CEILING
                                  or parent_code is particle primary)  → exclude
  G5  — Lexically distant noise (low-freq, non-soul parent)       → exclude

Primary soul anchors (only these parent clusters survive Filter 2):
  H5315G — nephesh (Hebrew soul)
  G5590G — psuchē  (Greek soul)

Filter logic (mechanical, no semantic interpretation):
  F1  is_proper_noun = True  → G3, exclude
  F2  parent_code NOT IN soul_anchors AND vocab_count > PARTICLE_CEILING → G4, exclude
  F3  parent_code NOT IN soul_anchors AND is not a primary code itself → G5, exclude
  F4  parent_code IN soul_anchors AND is_sub_gloss = True  → G1, include
  F5  parent_code IN soul_anchors AND is_sub_gloss = False → verify root family:
        - Greek:  script_form contains ψυχ (ψ) → G2, include (compound confirmed)
        - Hebrew: known verbal root H5314 → G2, include
        - Other:  root unverifiable from JSON alone → G2r, review

The generated JSON is structured for direct consumption by the audit-mode
decision engine.

Usage:
  python scripts/_apply_term_decisions.py --input research/discovery/soul_term_map_20260323.json
  python scripts/_apply_term_decisions.py --input research/discovery/soul_term_map_20260323.json --ceiling 1000
"""

import argparse
import json
import os
import re
import sys
from datetime import date

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

# ── Configuration ─────────────────────────────────────────────────────────

# Primary soul-concept anchor codes.  Only terms in these parent clusters
# are candidates for include.  All other parent clusters → G4/G5.
SOUL_ANCHOR_PARENTS: set[str] = {"H5315G", "G5590G"}

# Terms with vocab_count above this ceiling are grammatical particles —
# no genuine inner-being concept occurs > 1000 times in the Hebrew/Greek corpus.
PARTICLE_CEILING: int = 1000

# Hebrew codes under H5315G relatedNos whose root family is CONFIRMED
# (share the NPŠ root: nāphash = to breathe/refresh, the verbal root of nephesh).
# All others listed as related in STEP require researcher root-verification.
_CONFIRMED_HEBREW_ROOT_FAMILY: set[str] = {"H5314"}

# Greek: root-family membership is confirmed when the script_form contains ψυχ
# (the ψ character), which positively identifies a psuchē compound.
_GREEK_SOUL_ROOT_CHAR: str = "ψ"


# ── Decision logic ────────────────────────────────────────────────────────

def _verify_root_family(term: dict) -> tuple[bool, str]:
    """Return (is_confirmed, note) for a related term under a soul anchor.

    Confirmation rules (mechanical, no semantic judgement):
      - Greek:  script_form contains the ψ (psi) character → psuchē compound confirmed
      - Hebrew: code is in _CONFIRMED_HEBREW_ROOT_FAMILY (H5314, verified NPŠ root)
      - Else:   unverifiable from JSON fields alone → requires researcher review
    """
    code        = term.get("code", "")
    script_form = term.get("script_form", "")

    if code.startswith("G") and _GREEK_SOUL_ROOT_CHAR in script_form:
        return True, "Greek ψυχή compound (ψ in script_form confirmed)"
    if code in _CONFIRMED_HEBREW_ROOT_FAMILY:
        return True, "confirmed NPŠ verbal root (nāphash = to take breath)"
    return False, (
        f"root-family unverifiable from JSON: STEP relatedNos lists {code} as "
        f"related but root consonants require external verification "
        f"(see wa_term_root_family table when available)"
    )


def _assign_decision(
    term: dict,
    parent_code: str,
    section_type: str,       # 'sub_gloss' | 'related_term' | 'primary'
    particle_ceiling: int,
) -> tuple[str, str, str]:
    """Return (decision_group, action, reason) for one term."""
    code       = term.get("code", "")
    vocab_cnt  = term.get("vocab_count", 0)
    is_proper  = term.get("is_proper_noun", False)

    # F1 — proper noun
    if is_proper:
        return "G3", "exclude", "proper noun (name/place)"

    # Whether this term's parent chain is a soul-concept anchor
    soul_parent = (parent_code in SOUL_ANCHOR_PARENTS)

    # F2 — high-frequency grammatical particle (regardless of parent)
    if vocab_cnt > particle_ceiling:
        return "G4", "exclude", f"grammatical particle (vocab_count={vocab_cnt} > {particle_ceiling})"

    # F3 — primary code of a non-soul cluster (particle/grammar entry)
    if section_type == "primary" and not soul_parent:
        return "G4", "exclude", "non-soul cluster primary — particle/grammar code"

    # F4/F5 — terms under a soul anchor parent
    if soul_parent:
        if section_type in ("sub_gloss", "primary"):
            return "G1", "include", "soul sub-gloss (same lemma, translational variant)"
        else:
            # related_term under a soul parent — verify root family
            confirmed, note = _verify_root_family(term)
            if confirmed:
                return "G2", "include", note
            else:
                return "G2r", "review", note

    # F3 extended — related terms under a non-soul parent
    return "G5", "exclude", f"lexically distant (parent cluster {parent_code} not a soul anchor)"


# ── Core processor ────────────────────────────────────────────────────────

def build_decisions(data: dict, particle_ceiling: int) -> dict:
    """Transform a term_map JSON into a term_decisions JSON."""

    anchor      = data["meta"]["english_anchor"]
    step_ver    = data["meta"]["step_version"]
    generated   = date.today().isoformat()

    # We'll collect one flat record per term, enriched with decision fields.
    # Also build three separate lookup tables: by group.
    all_terms: list[dict] = []
    groups: dict[str, list[str]] = {
        "G1": [], "G2": [], "G2r": [], "G3": [], "G4": [], "G5": [],
    }
    group_labels = {
        "G1":  "Soul sub-glosses (include)",
        "G2":  "Soul root-family related terms (include)",
        "G2r": "Soul STEP-related, root unverified (review)",
        "G3":  "Proper nouns (exclude)",
        "G4":  "Grammatical particles (exclude)",
        "G5":  "Lexically distant / noise (exclude)",
    }

    for cluster_entry in data["clusters"]:
        parent_code = cluster_entry["cluster"]["primary_code"]
        cl          = cluster_entry["cluster"]
        pv          = cl["primary_vocab"]

        # ── Primary code itself ─────────────────────────────────────────
        prim_term = {
            "code":            parent_code,
            "gloss":           pv.get("gloss", ""),
            "transliteration": pv.get("transliteration", ""),
            "script_form":     pv.get("hebrew_unicode", ""),
            "language":        pv.get("language", ""),
            "vocab_count":     pv.get("occurrence_count", 0),
            "verse_count":     pv.get("verse_count", 0),
            "medium_def":      pv.get("medium_def", ""),
            "is_sub_gloss":    False,
            "is_proper_noun":  False,
            "notes":           [],
        }
        grp, action, reason = _assign_decision(
            prim_term, parent_code, "primary", particle_ceiling
        )
        prim_term.update({
            "step_parent_code":  parent_code,
            "step_section_type": "primary",
            "decision_group":    grp,
            "action":            action,
            "decision_reason":   reason,
        })
        all_terms.append(prim_term)
        groups[grp].append(parent_code)

        # ── Sub-glosses ─────────────────────────────────────────────────
        for sg in cl.get("sub_glosses", []):
            grp, action, reason = _assign_decision(
                sg, parent_code, "sub_gloss", particle_ceiling
            )
            record = dict(sg)
            record.update({
                "step_parent_code":  parent_code,
                "step_section_type": "sub_gloss",
                "decision_group":    grp,
                "action":            action,
                "decision_reason":   reason,
            })
            all_terms.append(record)
            groups[grp].append(sg["code"])

        # ── Related terms ───────────────────────────────────────────────
        for rt in cl.get("related_terms", []):
            grp, action, reason = _assign_decision(
                rt, parent_code, "related_term", particle_ceiling
            )
            record = dict(rt)
            record.update({
                "step_parent_code":  parent_code,
                "step_section_type": "related_term",
                "decision_group":    grp,
                "action":            action,
                "decision_reason":   reason,
            })
            all_terms.append(record)
            groups[grp].append(rt["code"])

    # ── Summary counts ────────────────────────────────────────────────────
    include_terms  = [t for t in all_terms if t["action"] == "include"]
    review_terms   = [t for t in all_terms if t["action"] == "review"]
    exclude_terms  = [t for t in all_terms if t["action"] == "exclude"]
    include_codes  = [t["code"] for t in include_terms]
    review_codes   = [t["code"] for t in review_terms]
    total_include_verses = sum(t.get("verse_count", 0) for t in include_terms)
    total_review_verses  = sum(t.get("verse_count", 0) for t in review_terms)

    # De-dupe across sub-gloss overlaps is not done here (requires verse pull)
    # — verse de-dup happens in Phase 2. We can still compute an upper-bound.
    summary = {
        "total_terms_evaluated":  len(all_terms),
        "total_include":          len(include_terms),
        "total_exclude":          len(exclude_terms),
        "by_group": {
            grp: {
                "label": group_labels[grp],
                "count": len(codes),
                "codes": codes,
            }
            for grp, codes in groups.items()
        },
        "include_codes":                    include_codes,
        "review_codes":                     review_codes,
        "verse_count_sum_include_before_dedup": total_include_verses,
        "verse_count_sum_review_before_dedup":  total_review_verses,
        "note_on_dedup": (
            "verse_count sums are pre-dedup upper bounds. "
            "Verses tagged by multiple sub-glosses will be counted once in Phase 2. "
            "review codes require researcher root-verification before promotion to include."
        ),
    }

    return {
        "meta": {
            "english_anchor":  anchor,
            "generated":       generated,
            "step_version":    step_ver,
            "particle_ceiling": particle_ceiling,
            "soul_anchor_parents": sorted(SOUL_ANCHOR_PARENTS),
            "schema_version":  "1.0",
            "purpose": (
                "Audit-mode input: term-level decisions derived by programmatic "
                "filtering from Phase 1 term_map. No semantic interpretation applied. "
                "Drives Phase 2 verse extraction."
            ),
        },
        "summary":        summary,
        "terms":          all_terms,
    }


# ── Markdown writer ────────────────────────────────────────────────────────

def write_enriched_triage(data: dict, decisions: dict, output_path: str) -> None:
    """Write an enriched triage .md that now includes step_parent_code,
    step_section_type, decision_group, and suggested_action columns."""

    anchor    = decisions["meta"]["english_anchor"]
    generated = decisions["meta"]["generated"]
    step_ver  = decisions["meta"]["step_version"]
    ceiling   = decisions["meta"]["particle_ceiling"]
    summary   = decisions["summary"]

    lines: list[str] = []
    lines.append(f'# Term Decisions — "{anchor}"')
    lines.append(f"")
    lines.append(f"Generated: {generated}  |  STEP version: `{step_ver}`  "
                 f"|  Particle ceiling: {ceiling}")
    lines.append(f"")
    lines.append(
        "This is an **auto-decided** triage.  Every decision was derived from "
        "programmatic filters — no semantic interpretation applied.  "
        "Researcher override: replace `action` value as needed before Phase 2."
    )
    lines.append(f"")

    # Summary table
    lines.append(f"## Decision Summary")
    lines.append(f"")
    lines.append(f"| Group | Label | Count |")
    lines.append(f"|-------|-------|-------|")
    for grp in ("G1", "G2", "G3", "G4", "G5"):
        info = summary["by_group"][grp]
        lines.append(f"| {grp} | {info['label']} | {info['count']} |")
    lines.append(f"")
    lines.append(
        f"**Include total:** {summary['total_include']} terms  "
        f"|  verse_count sum (pre-dedup): **{summary['verse_count_sum_include_before_dedup']}**"
    )
    lines.append(f"")

    header = (
        "| code | lang | decision_group | action | gloss | translit | "
        "verse_count | vocab_count | parent_code | section_type | reason |"
    )
    sep = (
        "|------|------|----------------|--------|-------|----------|"
        "------------|-------------|-------------|--------------|--------|"
    )

    # Group terms by decision_group for display
    for grp in ("G1", "G2", "G2r", "G3", "G4", "G5"):
        grp_terms = [t for t in decisions["terms"] if t["decision_group"] == grp]
        if not grp_terms:
            continue
        info = summary["by_group"][grp]
        lines.append(f"## {grp}: {info['label']}")
        lines.append(f"")
        lines.append(header)
        lines.append(sep)
        for t in grp_terms:
            # Truncate reason for table width
            reason = t.get("decision_reason", "")[:60]
            lines.append(
                f"| {t['code']} | {t.get('language','')[:6]} | {grp} | "
                f"**{t['action']}** | {t.get('gloss','')} | "
                f"{t.get('transliteration','')} | "
                f"{t.get('verse_count',0)} | {t.get('vocab_count',0)} | "
                f"{t.get('step_parent_code','')} | {t.get('step_section_type','')} | "
                f"{reason} |"
            )
        lines.append(f"")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


# ── Entry point ────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Apply programmatic term decisions to a Phase 1 term_map JSON"
    )
    parser.add_argument("--input", required=True,
                        help="Path to term_map JSON (output of _discover_word_terms.py)")
    parser.add_argument("--ceiling", type=int, default=PARTICLE_CEILING,
                        help=f"Vocab count ceiling for particle exclusion (default: {PARTICLE_CEILING})")
    args = parser.parse_args()

    input_path = args.input
    if not os.path.isabs(input_path):
        input_path = os.path.join(_ROOT, input_path)
    if not os.path.exists(input_path):
        print(f"ERROR: input file not found: {input_path}")
        sys.exit(1)

    with open(input_path, encoding="utf-8") as f:
        data = json.load(f)

    anchor    = data["meta"]["english_anchor"]
    today_str = date.today().strftime("%Y%m%d")
    out_dir   = os.path.dirname(input_path)

    print(f"Processing: {anchor}")
    decisions = build_decisions(data, args.ceiling)

    # Write decisions JSON
    json_path = os.path.join(out_dir, f"{anchor}_term_decisions_{today_str}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(decisions, f, ensure_ascii=False, indent=2)
    print(f"Decisions JSON: {json_path}")

    # Write enriched triage markdown
    md_path = os.path.join(out_dir, f"{anchor}_term_decisions_{today_str}.md")
    write_enriched_triage(data, decisions, md_path)
    print(f"Decisions MD:   {md_path}")

    # Print summary to console
    s = decisions["summary"]
    print()
    print(f"  Total evaluated: {s['total_terms_evaluated']}")
    print(f"  Include: {s['total_include']}  |  Review: {len(s['review_codes'])}  |  Exclude: {s['total_exclude']}")
    print()
    for grp in ("G1", "G2", "G2r", "G3", "G4", "G5"):
        info = s["by_group"][grp]
        print(f"  {grp:<4}  {info['label']:48s}  {info['count']:3d} terms")
    print()
    print(f"  Verse count sum — include (pre-dedup): {s['verse_count_sum_include_before_dedup']}")
    print(f"  Verse count sum — review  (pre-dedup): {s['verse_count_sum_review_before_dedup']}")
    print()
    print("Include codes:")
    for code in s["include_codes"]:
        term = next(t for t in decisions["terms"] if t["code"] == code)
        print(f"  {code:10s}  {term.get('gloss',''):30s}  {term['verse_count']} verses")
    if s["review_codes"]:
        print()
        print("Review codes (root-family unverified — researcher decision required):")
        for code in s["review_codes"]:
            term = next(t for t in decisions["terms"] if t["code"] == code)
            print(f"  {code:10s}  {term.get('gloss',''):30s}  {term['verse_count']} verses")


if __name__ == "__main__":
    main()
