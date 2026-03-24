#!/usr/bin/env python3
"""
word_study_extract.py
─────────────────────
Step 1 — STEP data pull for a word study.

Queries STEP only.  No DB reads.  No DB writes.
Replaces the three-script pipeline (_discover_word_terms.py,
_apply_term_decisions.py, _extract_word_terms.py) in a single pass.

Produces:
  data/discovery/{word}_step_data_{YYYYMMDD}.json   — full term + verse data
  data/discovery/{word}_step_data_{YYYYMMDD}.md     — summary table

Usage:
  python scripts/word_study_extract.py --word soul
  python scripts/word_study_extract.py --word soul --anchors H5315G,G5590G
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

from analytics.db_client import get_connection as _db_connect
from analytics.step_client import StepClient
from engine.span_filter import apply_span_filter

# ── Constants ──────────────────────────────────────────────────────────────

PARTICLE_CEILING = 1000   # vocab_count threshold for G4 exclusion
CONTEXT_WINDOW   = 5      # words of ESV text to capture before/after target_word

# Hebrew codes whose root relationship to the anchor cluster is positively
# confirmed from external analysis (consonant matching etc.).
_CONFIRMED_HEBREW_ROOTS: frozenset[str] = frozenset(["H5314"])

_PREFIX_RE = re.compile(r"^[HG]9\d{3}")


# ── Utilities ──────────────────────────────────────────────────────────────

def _lookup_registry_id(word: str) -> str:
    """Return the word_registry.id for the given English word as a zero-padded
    3-digit string (e.g. 182 → '182', 4 → '004').  Returns '000' if the word
    is not found in the registry (e.g. first run before registration).
    """
    try:
        conn = _db_connect()
        row  = conn.execute(
            "SELECT id FROM word_registry WHERE word = ? COLLATE NOCASE",
            (word,),
        ).fetchone()
        conn.close()
        if row:
            return f"{row['id']:03d}"
    except Exception as exc:
        p(f"[warn] Registry lookup failed: {exc} — using '000'")
    return "000"


def p(msg: str = "") -> None:
    print(msg, flush=True)


def _is_particle_code(code: str) -> bool:
    return bool(_PREFIX_RE.match(code))


def _language(code: str) -> str:
    return "Greek" if code.startswith("G") else "Hebrew"


def _is_proper_noun(gloss: str, medium_def: str) -> bool:
    """Heuristic proper-noun detection matching get_related_term_cluster logic."""
    return bool(
        re.search(
            r"\bproper noun\b|\bpersonal name\b|\bplace name\b",
            medium_def,
            re.IGNORECASE,
        )
        or (
            gloss
            and gloss[0].isupper()
            and len(gloss.split()) == 1
            and gloss not in ("I", "A")
        )
    )


def _context_words(esv_text: str, target_word: str, n: int = CONTEXT_WINDOW) -> tuple[str, str]:
    """Return (context_before, context_after) — up to n words around target_word."""
    if not target_word or not esv_text:
        return "", ""
    idx = esv_text.find(target_word)
    if idx == -1:
        return "", ""
    before_tokens = esv_text[:idx].split()
    after_tokens  = esv_text[idx + len(target_word):].split()
    return " ".join(before_tokens[-n:]), " ".join(after_tokens[:n])


def _testament_coverage(verse_list: list[dict]) -> str | None:
    testaments = {v["testament"] for v in verse_list}
    if testaments == {"OT"}:
        return "OT_only"
    if testaments == {"NT"}:
        return "NT_only"
    if testaments:
        return "both"
    return None


# ── Phase 1+2: Anchor detection + cluster discovery (single pass) ──────────

def build_clusters(
    client: StepClient,
    word: str,
    explicit_anchors: list[str] | None,
) -> tuple[list[str], list[tuple[str, dict]]]:
    """Detect anchors and fetch all term clusters in one pass.

    For explicit anchors: fetch cluster for each given code.
    For auto-detect: run English text search, then fetch cluster for each
    candidate code (skipping any already covered by an earlier cluster).

    Returns:
        anchor_codes  — ordered list of resolved primary codes
        clusters      — list of (primary_code, cluster_dict) in the same order
    """
    if explicit_anchors:
        p(f"[discover] Explicit anchors: {explicit_anchors}")
        candidates = explicit_anchors
    else:
        p(f"[discover] Auto-detecting anchors via text search for '{word}'...")
        tally = client.get_strongs_for_word(word)
        if not tally:
            p("  ERROR: no Strong's codes found from text search. Is STEP running?")
            sys.exit(1)
        candidates = [item["strong"] for item in tally
                      if not _is_particle_code(item["strong"])]
        p(f"  Text search returned {len(tally)} codes "
          f"({len(candidates)} after particle filter)")

    anchor_codes:    list[str]               = []
    clusters:        list[tuple[str, dict]]  = []
    seen_primaries:  set[str]                = set()
    seen_codes:      set[str]                = set()

    for code in candidates:
        if code in seen_codes:
            p(f"  [{code}] Already covered by a previous cluster — skipping.")
            continue

        p(f"  [{code}] Fetching cluster...")
        cluster      = client.get_related_term_cluster(code)
        primary_code = cluster.get("primary_code", code)

        if primary_code in seen_primaries:
            p(f"    Resolved to {primary_code} (already collected) — skipping.")
            for c in cluster.get("all_codes", []):
                seen_codes.add(c)
            continue

        seen_primaries.add(primary_code)
        for c in cluster.get("all_codes", []):
            seen_codes.add(c)

        n_sub = len(cluster.get("sub_glosses", []))
        n_rel = len(cluster.get("related_terms", []))
        p(f"    primary={primary_code}  sub_glosses={n_sub}  related_terms={n_rel}")

        anchor_codes.append(primary_code)
        clusters.append((primary_code, cluster))

    p(f"  Anchors resolved: {anchor_codes}")
    return anchor_codes, clusters


# ── Phase 3: Build flat terms list ─────────────────────────────────────────

def _make_term_entry(
    code:          str,
    section_type:  str,   # "primary" / "sub_gloss" / "related_term"
    parent_code:   str,
    vocab:         dict,
    cluster_is_proper: bool = False,
) -> dict | None:
    """Build a complete pre-filter term entry from a get_vocab_info result."""
    if not vocab:
        return None
    gloss      = vocab.get("gloss", "")
    medium_def = vocab.get("medium_def", "")
    is_proper  = cluster_is_proper or _is_proper_noun(gloss, medium_def)

    return {
        "code":               code,
        "gloss":              gloss,
        "transliteration":    vocab.get("transliteration", ""),
        "script_form":        vocab.get("hebrew_unicode", ""),
        "language":           vocab.get("language", _language(code)),
        "vocab_count":        vocab.get("occurrence_count", 0),
        "medium_def":         medium_def,
        "lsj_entry":          vocab.get("lsj_entry", ""),
        "short_def_mounce":   vocab.get("short_def_mounce", ""),
        "related_words":      vocab.get("related_words", []),
        "raw_related_numbers": vocab.get("raw_related_numbers", ""),
        "freq_list":          vocab.get("freq_list", ""),
        "is_proper_noun":     is_proper,
        "is_sub_gloss":       (section_type == "sub_gloss"),
        "step_parent_code":   parent_code,
        "step_section_type":  section_type,
        # Filter phase fills these in:
        "decision_group":     None,
        "action":             None,
        "decision_reason":    None,
        "verses_fetched":     False,
        "verse_count":        None,
        "testament_coverage": None,
        "meaning_numbered":   vocab.get("meaning_numbered", False),
        "causative_form_present": vocab.get("causative_form_present", False),
        "data_quality_flags": [],
        "quality_flag_detail": {},
        "verses":             [],
    }


def build_terms_list(client: StepClient, clusters: list[tuple[str, dict]]) -> list[dict]:
    """Iterate all clusters and build the flat list of per-term dicts.

    For the primary code, uses primary_vocab directly (already a full
    get_vocab_info result).  For sub_glosses and related_terms, calls
    get_vocab_info to retrieve the richer field set (lsj_entry, freq_list,
    related_words etc.) not retained in _term_entry.
    """
    terms: list[dict] = []
    seen:  set[str]   = set()

    for primary_code, cluster in clusters:
        # ── Primary ───────────────────────────────────────────────────────
        pv   = cluster.get("primary_vocab", {})
        code = cluster.get("primary_code", primary_code)
        if code and code not in seen:
            seen.add(code)
            entry = _make_term_entry(code, "primary", primary_code, pv)
            if entry:
                terms.append(entry)

        # ── Sub-glosses ───────────────────────────────────────────────────
        for sg in cluster.get("sub_glosses", []):
            code = sg.get("code", "")
            if not code or code in seen:
                continue
            seen.add(code)
            vocab = client.get_vocab_info(code)
            if not vocab:
                continue
            entry = _make_term_entry(
                code, "sub_gloss", primary_code, vocab,
                cluster_is_proper=sg.get("is_proper_noun", False),
            )
            if entry:
                terms.append(entry)

        # ── Related terms ─────────────────────────────────────────────────
        for rt in cluster.get("related_terms", []):
            code = rt.get("code", "")
            if not code or code in seen:
                continue
            seen.add(code)
            vocab = client.get_vocab_info(code)
            if not vocab:
                continue
            entry = _make_term_entry(
                code, "related_term", primary_code, vocab,
                cluster_is_proper=rt.get("is_proper_noun", False),
            )
            if entry:
                terms.append(entry)

    return terms


# ── Phase 4: Filter logic F1–F5 ────────────────────────────────────────────

def _root_confirmed(code: str, script_form: str) -> bool:
    """Return True if root relationship to anchor cluster is positively confirmed."""
    # Greek: script_form contains ψ (psi — marks psuchē-family compound)
    if code.startswith("G") and "ψ" in script_form:
        return True
    # Hebrew: code is in the manually confirmed root set
    if code in _CONFIRMED_HEBREW_ROOTS:
        return True
    return False


def _root_confirmation_reason(code: str, script_form: str) -> str:
    if code.startswith("G") and "ψ" in script_form:
        return f"script_form '{script_form}' contains ψ (psuchē compound)"
    if code in _CONFIRMED_HEBREW_ROOTS:
        return f"{code} is in the confirmed-root set"
    return "unknown"


def apply_filters(
    terms:            list[dict],
    anchor_codes:     list[str],
    particle_ceiling: int,
) -> None:
    """Assign decision_group, action, decision_reason in-place for every term."""
    anchor_set = set(anchor_codes)

    for t in terms:
        code        = t["code"]
        parent      = t["step_parent_code"]
        section     = t["step_section_type"]
        vocab_count = t["vocab_count"]
        is_proper   = t["is_proper_noun"]
        script_form = t["script_form"]

        # F1: proper noun → G3
        if is_proper:
            t["decision_group"]  = "G3"
            t["action"]          = "exclude"
            t["decision_reason"] = "F1: is_proper_noun=true"
            continue

        # F2: vocab_count > ceiling → G4
        if vocab_count > particle_ceiling:
            t["decision_group"]  = "G4"
            t["action"]          = "exclude"
            t["decision_reason"] = (
                f"F2: vocab_count {vocab_count} > particle_ceiling {particle_ceiling}"
            )
            continue

        # F3: primary code whose parent is NOT in anchor list → G4
        if section == "primary" and parent not in anchor_set:
            t["decision_group"]  = "G4"
            t["action"]          = "exclude"
            t["decision_reason"] = (
                f"F3: section_type=primary, parent {parent} not in anchor list"
            )
            continue

        # F4: parent in anchors AND section is primary or sub_gloss → G1
        if parent in anchor_set and section in ("primary", "sub_gloss"):
            t["decision_group"]  = "G1"
            t["action"]          = "include"
            t["decision_reason"] = (
                f"F4: parent {parent} in anchor list, section_type={section}"
            )
            continue

        # F5: parent in anchors AND section is related_term → G2 or G2r
        if parent in anchor_set and section == "related_term":
            if _root_confirmed(code, script_form):
                t["decision_group"]  = "G2"
                t["action"]          = "include"
                t["decision_reason"] = (
                    f"F5a: parent {parent} in anchor list, section_type=related_term, "
                    f"root confirmed ({_root_confirmation_reason(code, script_form)})"
                )
            else:
                t["decision_group"]  = "G2r"
                t["action"]          = "include"
                t["decision_reason"] = (
                    f"F5b: parent {parent} in anchor list, section_type=related_term, "
                    "root NOT confirmed"
                )
                detail = (
                    f"Root family of {code} ('{t['gloss']}') not confirmed from STEP "
                    "data alone. Root consonants may not match the anchor cluster root."
                )
                t["data_quality_flags"].append("NOTE_ON_ROOT_FAMILY")
                t["quality_flag_detail"]["NOTE_ON_ROOT_FAMILY"] = detail
            continue

        # F3x: parent NOT in anchors AND section is related_term or sub_gloss → G5
        if parent not in anchor_set and section in ("related_term", "sub_gloss"):
            t["decision_group"]  = "G5"
            t["action"]          = "exclude"
            t["decision_reason"] = (
                f"F3x: parent {parent} not in anchor list, section_type={section}"
            )
            continue

        # Fallback (should not be reached)
        t["decision_group"]  = "G5"
        t["action"]          = "exclude"
        t["decision_reason"] = (
            f"Fallback: unmatched filter — section={section}, parent={parent}"
        )


# ── Phase 5: Verse fetching + span filter ──────────────────────────────────

def fetch_verses(
    client:        StepClient,
    terms:         list[dict],
    terms_by_code: dict[str, dict],
) -> None:
    """Fetch verses and apply span filter for every included term (in-place)."""
    for t in terms:
        if t["action"] != "include":
            continue

        code = t["code"]
        p(f"  [{code}] Fetching verses...")
        records, html_map = client.get_verse_records_with_html(code)

        t["verses_fetched"] = True
        t["verse_count"]    = len(records)

        verse_list: list[dict] = []

        for rec in records:
            osis_id = rec["osisId"]
            html    = html_map.get(osis_id, "")

            span_result  = apply_span_filter(html, code)
            target_word  = span_result["target_word"] or rec.get("target_word", "")
            span_code    = span_result.get("span_code_found")
            span_matched = span_result["match"]

            # Resolve span_label_found from terms array
            span_label: str | None = None
            if span_code and span_code in terms_by_code:
                span_label = terms_by_code[span_code].get("gloss")

            ctx_before, ctx_after = _context_words(rec["esv_text"], target_word)

            verse_list.append({
                "osisId":            osis_id,
                "ref":               rec["ref"],
                "book_code":         rec["book_code"],
                "chapter":           rec["chapter"],
                "verse_num":         rec["verse_num"],
                "esv_text":          rec["esv_text"],
                "target_word":       target_word,
                "testament":         rec["testament"],
                "fetched_under_code": code,
                "preview_html":      html,
                "span_strong_match": 1 if span_matched else 0,
                "span_code_found":   span_code,
                "span_label_found":  span_label,
                "context_before":    ctx_before,
                "context_after":     ctx_after,
            })

        t["verses"]            = verse_list
        t["testament_coverage"] = _testament_coverage(verse_list)

        # Quality flags
        if t["verse_count"] == 0:
            t["data_quality_flags"].append("NO_VERSES")
            t["quality_flag_detail"]["NO_VERSES"] = (
                f"No verses returned by STEP for {code} despite inclusion in cluster."
            )
        elif verse_list and all(v["span_strong_match"] == 0 for v in verse_list):
            t["data_quality_flags"].append("SPAN_RESOLUTION_CONFLICT")
            t["quality_flag_detail"]["SPAN_RESOLUTION_CONFLICT"] = (
                f"All {len(verse_list)} verses for {code} have span_strong_match=0. "
                "Possible false positives from STEP search."
            )

        p(f"    → {t['verse_count']} verses, coverage: {t['testament_coverage']}, "
          f"flags: {t['data_quality_flags'] or 'none'}")


# ── Phase 6: Build meta block ──────────────────────────────────────────────

def build_meta(
    word:             str,
    anchor_codes:     list[str],
    terms:            list[dict],
    particle_ceiling: int,
    step_version:     str,
) -> dict:
    groups: dict[str, int] = {}
    for t in terms:
        g = t["decision_group"] or "?"
        groups[g] = groups.get(g, 0) + 1

    return {
        "english_anchor":        word,
        "generated":             date.today().isoformat(),
        "step_version":          step_version,
        "anchor_codes":          anchor_codes,
        "particle_ceiling":      particle_ceiling,
        "total_terms_evaluated": len(terms),
        "summary_by_group":      groups,
        "include_codes":         [t["code"] for t in terms if t["action"] == "include"],
        "exclude_codes":         [t["code"] for t in terms if t["action"] == "exclude"],
    }


# ── Output writers ─────────────────────────────────────────────────────────

def write_json(output: dict, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    p(f"[output] JSON written → {path}")


def write_md(data: dict, path: str) -> None:
    """Write a researcher-readable summary table."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    meta  = data["meta"]
    terms = data["terms"]

    lines = [
        f'# Word Study Extract — "{meta["english_anchor"]}"',
        "",
        f"Generated: {meta['generated']}  |  STEP version: `{meta['step_version']}`",
        f"Anchors: {', '.join(meta['anchor_codes'])}",
        f"Total terms evaluated: {meta['total_terms_evaluated']}",
        "",
        "## Summary by decision group",
        "",
        "| Group | Action | Count |",
        "|-------|--------|-------|",
    ]
    action_map = {"G1": "include", "G2": "include", "G2r": "include",
                  "G3": "exclude", "G4": "exclude",  "G5": "exclude"}
    for group, count in sorted(meta["summary_by_group"].items()):
        action = action_map.get(group, "?")
        lines.append(f"| {group} | {action} | {count} |")

    lines += [
        "",
        "## Include codes",
        "",
        ", ".join(f"`{c}`" for c in meta["include_codes"]) or "_(none)_",
        "",
        "## Exclude codes",
        "",
        ", ".join(f"`{c}`" for c in meta["exclude_codes"]) or "_(none)_",
        "",
        "## Term table",
        "",
        "| code | lang | section_type | parent | group | action | gloss "
        "| verse_count | testament | flags |",
        "|------|------|-------------|--------|-------|--------|-------|"
        "------------|-----------|-------|",
    ]

    for t in terms:
        flags = ", ".join(t["data_quality_flags"]) if t["data_quality_flags"] else ""
        vc    = str(t["verse_count"]) if t["verse_count"] is not None else "—"
        tc    = t["testament_coverage"] or "—"
        lines.append(
            f"| {t['code']} | {t['language']} | {t['step_section_type']} "
            f"| {t['step_parent_code']} | {t['decision_group']} | {t['action']} "
            f"| {t['gloss']} | {vc} | {tc} | {flags} |"
        )

    lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    p(f"[output] Markdown written → {path}")


# ── Argument parsing ───────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Word study STEP extract — Step 1 (no DB).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python scripts/word_study_extract.py --word soul\n"
            "  python scripts/word_study_extract.py --word soul --anchors H5315G,G5590G\n"
            "\n"
            "Output file naming: {registry_no:03d}_{word}_step_data_{YYYYMMDD}.json/.md\n"
            "  registry_no is looked up from word_registry.id (0-padded to 3 digits).\n"
            "  Falls back to '000' if the word is not yet registered in the DB.\n"
        ),
    )
    parser.add_argument("--word",     required=True,
                        help="English word to study (e.g. soul)")
    parser.add_argument("--anchors",  default=None,
                        help="Comma-separated anchor Strong's codes "
                             "(auto-detected from text search if omitted)")
    parser.add_argument("--ceiling",  type=int, default=PARTICLE_CEILING,
                        help=f"vocab_count ceiling for particle exclusion "
                             f"(default {PARTICLE_CEILING})")
    return parser.parse_args()


# ── Main ───────────────────────────────────────────────────────────────────

def main() -> None:
    args  = parse_args()
    word  = args.word.lower()
    ceiling = args.ceiling

    explicit_anchors = (
        [c.strip() for c in args.anchors.split(",") if c.strip()]
        if args.anchors else None
    )

    today       = date.today().strftime("%Y%m%d")
    registry_no = _lookup_registry_id(word)
    output_dir  = os.path.join(_ROOT, "data", "discovery")
    stem        = f"{registry_no}_{word}_step_data_{today}"
    json_path   = os.path.join(output_dir, f"{stem}.json")
    md_path     = os.path.join(output_dir, f"{stem}.md")

    client = StepClient()
    p(f"[init] STEP version:  {client.version}")
    p(f"[init] Word:          {word}")
    p(f"[init] Registry no:   {registry_no}")
    p(f"[init] Ceiling:       {ceiling}")
    p()

    # ── Phase 1+2: Anchors + cluster discovery ────────────────────────────
    p("=== Phase 1/2: Anchor detection + cluster discovery ===")
    anchor_codes, clusters = build_clusters(client, word, explicit_anchors)
    p(f"  Clusters found: {len(clusters)}")
    p()

    # ── Phase 3: Build flat terms list ────────────────────────────────────
    p("=== Phase 3: Building term records ===")
    terms = build_terms_list(client, clusters)
    p(f"  Total terms discovered: {len(terms)}")
    p()

    # Build lookup used for span_label_found resolution in Phase 5
    terms_by_code: dict[str, dict] = {t["code"]: t for t in terms}

    # ── Phase 4: Apply decision filters ──────────────────────────────────
    p("=== Phase 4: Applying decision filters (F1–F5) ===")
    apply_filters(terms, anchor_codes, ceiling)
    for t in terms:
        p(f"  {t['code']:12s}  {t['step_section_type']:12s}  "
          f"→ {t['decision_group']:3s}  {t['decision_reason'][:72]}")
    p()

    # ── Phase 5: Fetch verses for included terms ──────────────────────────
    p("=== Phase 5: Fetching verses (included terms only) ===")
    fetch_verses(client, terms, terms_by_code)
    p()

    # ── Phase 6: Build output and write files ─────────────────────────────
    p("=== Phase 6: Writing output files ===")
    meta     = build_meta(word, anchor_codes, terms, ceiling, client.version)
    output   = {"meta": meta, "terms": terms}
    write_json(output, json_path)
    write_md(output, md_path)
    p()

    # ── Summary ───────────────────────────────────────────────────────────
    p("=== Complete ===")
    p(f"  Terms evaluated:  {meta['total_terms_evaluated']}")
    p(f"  Include / Exclude: "
      f"{len(meta['include_codes'])} / {len(meta['exclude_codes'])}")
    for group, count in sorted(meta["summary_by_group"].items()):
        action = "include" if group in ("G1", "G2", "G2r") else "exclude"
        p(f"  {group}: {count:3d}  ({action})")
    p(f"  JSON  → {json_path}")
    p(f"  MD    → {md_path}")


if __name__ == "__main__":
    main()
