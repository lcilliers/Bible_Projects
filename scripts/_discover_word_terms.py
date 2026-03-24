"""
_discover_word_terms.py
───────────────────────
Phase 1 — Term Discovery (read-only, no DB writes).

Given an English anchor word, maps every Hebrew and Greek term related to it
using STEP's vocab and relatedNos data.  Produces:

  data/discovery/{word}_term_map_{YYYYMMDD}.json   — full structured term data
  data/discovery/{word}_triage_{YYYYMMDD}.md       — researcher decision table

Nothing is written to the database.  No verses are extracted.
The triage table has blank `include?` and `notes` columns for the researcher
to fill in before moving to Phase 2.

Usage:
  python scripts/_discover_word_terms.py --english soul
  python scripts/_discover_word_terms.py --english soul --no-related
"""

import argparse
import json
import os
import sys
from datetime import date

# Ensure analytics/ is importable from project root
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from analytics.step_client import StepClient


def p(msg: str = "") -> None:
    print(msg, flush=True)


# ── Helpers ────────────────────────────────────────────────────────────────


def _truncate(text: str, limit: int = 120) -> str:
    """Truncate text for display in the triage table."""
    if not text:
        return ""
    text = text.replace("\n", "  ").strip()
    if len(text) > limit:
        return text[:limit - 3] + "..."
    return text


def _language_label(code: str) -> str:
    return "Greek" if code.startswith("G") else "Hebrew"


def _is_particle(code: str) -> bool:
    """True if code is a STEP internal grammar particle (H9xxx / G9xxx)."""
    import re
    return bool(re.match(r'^[HG]9', code))


# ── Core discovery ─────────────────────────────────────────────────────────


def discover(english_word: str, include_related: bool = True) -> dict:
    """Run the full discovery pipeline for an English anchor word.

    Returns a structured dict ready for JSON serialisation.
    """
    client = StepClient()
    today = date.today().isoformat()

    p(f"[discover] English anchor: '{english_word}'")
    p(f"[discover] STEP version:   {client.version}")
    p()

    # ── Step 1: English text search → primary Strong's codes ──────────────
    p("[1/4] Running English text search to identify primary Strong's codes...")
    primary_tally = client.get_strongs_for_word(english_word)
    p(f"      Found {len(primary_tally)} candidate codes from text search")

    if not primary_tally:
        p("      ERROR: no Strong's codes found — check STEP is running and the word is correct")
        sys.exit(1)

    for item in primary_tally[:10]:
        p(f"      {item['strong']:10s}  ({item['count']} verses)")
    if len(primary_tally) > 10:
        p(f"      ... and {len(primary_tally) - 10} more")
    p()

    # ── Step 2: Fetch term clusters for each primary code ─────────────────
    p("[2/4] Fetching term clusters (sub-glosses + related terms) for each primary code...")
    p("      Note: this makes multiple API calls — allow 30–60 s for large clusters")
    p()

    clusters: list[dict] = []
    all_codes_seen: set[str] = set()     # dedup across primary codes

    for item in primary_tally:
        base_code = item["strong"]
        if _is_particle(base_code):
            p(f"      Skipping {base_code} (grammar particle)")
            continue
        if base_code in all_codes_seen:
            p(f"      Skipping {base_code} (already in a cluster)")
            continue

        p(f"  [{base_code}] Fetching cluster...")
        cluster = client.get_related_term_cluster(base_code)
        primary_code = cluster.get("primary_code", base_code)
        n_sub = len(cluster.get("sub_glosses", []))
        n_rel = len(cluster.get("related_terms", []))
        p(f"      primary={primary_code}  sub_glosses={n_sub}  related_terms={n_rel}")

        # Track all codes encountered so we don't double-fetch
        for c in cluster.get("all_codes", []):
            all_codes_seen.add(c)

        clusters.append({
            "english_anchor_code":   base_code,
            "english_anchor_count":  item["count"],
            "cluster":               cluster,
        })
        p()

    # ── Step 3: Also add primary vocab verse_count ─────────────────────────
    p("[3/4] Adding verse counts for primary codes...")
    for entry in clusters:
        pv = entry["cluster"].get("primary_vocab", {})
        base = entry["cluster"].get("primary_code", "")
        if base:
            try:
                sd = client._search_range(base)
                vc = sd.get("total", 0)
            except Exception:
                vc = 0
            pv["verse_count"] = vc
            p(f"      {base}: {vc} verses in ESV_th")
    p()

    # ── Step 4: Build the output structure ────────────────────────────────
    p("[4/4] Building output structure...")

    # Aggregate key stats
    total_sub_gloss_codes = sum(len(e["cluster"]["sub_glosses"]) for e in clusters)
    total_related_codes = sum(len(e["cluster"]["related_terms"]) for e in clusters)
    total_codes = sum(len(e["cluster"]["all_codes"]) for e in clusters)

    result = {
        "meta": {
            "english_anchor":       english_word,
            "generated":            today,
            "step_version":         client.version,
            "primary_codes_found":  len(clusters),
            "total_codes_in_map":   total_codes,
            "total_sub_gloss_codes": total_sub_gloss_codes,
            "total_related_codes":  total_related_codes,
        },
        "primary_tally":  primary_tally,
        "clusters":       clusters,
    }

    p(f"      Clusters: {len(clusters)}")
    p(f"      Total codes in map: {total_codes}  "
      f"(sub-glosses: {total_sub_gloss_codes}, related: {total_related_codes})")
    p()
    return result


# ── Output writers ─────────────────────────────────────────────────────────


def write_json(data: dict, output_dir: str, word: str, today_str: str) -> str:
    path = os.path.join(output_dir, f"{word}_term_map_{today_str}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path


def write_triage_md(data: dict, output_dir: str, word: str, today_str: str) -> str:
    """Write the researcher triage markdown table."""
    path = os.path.join(output_dir, f"{word}_triage_{today_str}.md")
    anchor = data["meta"]["english_anchor"]
    generated = data["meta"]["generated"]
    step_ver = data["meta"]["step_version"]

    lines: list[str] = []
    lines.append(f'# Term Discovery Triage \u2014 "{anchor}"')
    lines.append(f"")
    lines.append(f"Generated: {generated}  |  STEP version: `{step_ver}`")
    lines.append(f"")
    lines.append(
        "Fill in the **include?** column (`yes` / `no` / `maybe`) and add "
        "notes before running Phase 2 extraction."
    )
    lines.append(f"")
    lines.append(
        "Columns: `code` | `lang` | `parent_code` | `section_type` | `gloss` | "
        "`translit` | `script` | `verse_count` | `vocab_count` | `is_proper_noun` | "
        "**`include?`** | **`notes`** | `definition (truncated)`"
    )
    lines.append(f"")

    def _row(code, lang, parent_code, section_type, gloss, translit, script,
             vc, occ, is_proper, defn):
        pn_mark = "⚑" if is_proper else ""
        include_default = "no" if is_proper else "yes"
        return (
            f"| {code} | {lang} | {parent_code} | {section_type} | "
            f"{gloss}{pn_mark} | {translit} | "
            f"{script} | {vc} | {occ} | {'yes' if is_proper else ''} | "
            f"{include_default} | | {_truncate(defn, 100)} |"
        )

    header = (
        "| code | lang | parent_code | section_type | gloss | translit | script | "
        "verse_count | vocab_count | proper_noun | include? | notes | definition |"
    )
    sep = (
        "|------|------|-------------|--------------|-------|----------|--------|"
        "------------|-------------|-------------|----------|-------|------------|"
    )

    for cluster_entry in data["clusters"]:
        cl = cluster_entry["cluster"]
        pc = cl["primary_code"]
        pv = cl["primary_vocab"]
        p_vc = pv.get("verse_count", 0)
        p_occ = pv.get("occurrence_count", 0)
        p_gloss = pv.get("gloss", "")
        p_translit = pv.get("transliteration", "")
        p_script = pv.get("hebrew_unicode", "")
        p_def = pv.get("medium_def", "")
        p_lang = _language_label(pc)

        lines.append(f"## Primary: {pc} — {p_gloss} ({p_lang})")
        lines.append(f"")
        lines.append(f"English anchor verse count (from text search): "
                     f"**{cluster_entry['english_anchor_count']}**")
        lines.append(f"")

        # ── Sub-glosses table ──────────────────────────────────────────────
        lines.append(f"### Sub-glosses of {pc}")
        lines.append(f"")
        lines.append(header)
        lines.append(sep)

        # Primary code first
        lines.append(_row(pc, p_lang, pc, "primary",
                          p_gloss, p_translit, p_script,
                          p_vc, p_occ, False, p_def))

        for sg in cl["sub_glosses"]:
            if not sg.get("code"):
                continue
            lines.append(_row(
                sg["code"],
                _language_label(sg["code"]),
                pc,
                "sub_gloss",
                sg.get("gloss", ""),
                sg.get("transliteration", ""),
                sg.get("script_form", ""),
                sg.get("verse_count", 0),
                sg.get("vocab_count", 0),
                sg.get("is_proper_noun", False),
                sg.get("medium_def", ""),
            ))

        lines.append(f"")

        # ── Related terms table ────────────────────────────────────────────
        if cl["related_terms"]:
            lines.append(f"### Related terms for {pc}")
            lines.append(f"")
            lines.append(header)
            lines.append(sep)

            for rt in cl["related_terms"]:
                if not rt.get("code"):
                    continue
                lines.append(_row(
                    rt["code"],
                    _language_label(rt["code"]),
                    pc,
                    "related_term",
                    rt.get("gloss", ""),
                    rt.get("transliteration", ""),
                    rt.get("script_form", ""),
                    rt.get("verse_count", 0),
                    rt.get("vocab_count", 0),
                    rt.get("is_proper_noun", False),
                    rt.get("medium_def", ""),
                ))

            lines.append(f"")

    # ── Summary of all codes ───────────────────────────────────────────────
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## Summary")
    lines.append(f"")
    lines.append(f"| Metric | Count |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Primary codes | {data['meta']['primary_codes_found']} |")
    lines.append(f"| Sub-gloss codes | {data['meta']['total_sub_gloss_codes']} |")
    lines.append(f"| Related term codes | {data['meta']['total_related_codes']} |")
    lines.append(f"| Total codes in map | {data['meta']['total_codes_in_map']} |")
    lines.append(f"")
    lines.append(f"*English text search found {len(data['primary_tally'])} candidate "
                 f"codes before cluster expansion.*")
    lines.append(f"")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return path


# ── Entry point ────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Phase 1 — Term Discovery: map all STEP terms for an English word"
    )
    parser.add_argument("--english", required=True,
                        help="English anchor word (e.g. 'soul')")
    parser.add_argument("--no-related", action="store_true",
                        help="Skip related terms; fetch sub-glosses only")
    parser.add_argument("--output-dir", default=None,
                        help="Output directory (default: data/discovery/ in project root)")
    args = parser.parse_args()

    word = args.english.lower().strip()
    today_str = date.today().strftime("%Y%m%d")

    output_dir = args.output_dir or os.path.join(_ROOT, "data", "discovery")
    os.makedirs(output_dir, exist_ok=True)

    p("=" * 60)
    p(f"  Term Discovery — '{word}'")
    p("=" * 60)
    p()

    data = discover(word, include_related=not args.no_related)

    # Write JSON
    json_path = write_json(data, output_dir, word, today_str)
    p(f"JSON written:   {json_path}")

    # Write triage markdown
    md_path = write_triage_md(data, output_dir, word, today_str)
    p(f"Triage written: {md_path}")

    p()
    p("Phase 1 complete.  Review the triage table, fill in include? column,")
    p("then run Phase 2 extraction for approved terms only.")
    p()


if __name__ == "__main__":
    main()
