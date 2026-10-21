"""
span_filter.py
──────────────
Span-based verse filtering (§5.2, v4).

STEP masterSearch preview HTML contains inline <span> tags:
    <span morph='HVqp3ms' strong='H7442B H9001'>sang</span>

The filter rule:
  - If the queried Strong's, OR any sub-gloss of its numeric base, appears in a span's
    strong= attribute → STORE (match=1). This means H7965H matches H7965A..H7965F.
  - Spans containing only grammatical prefix codes (H9xxx / G9xxx) are ignored.

Also extracts target_word from the matching span text.
Used in: S3 (GAP_FILL), N8 (NEW_WORD), A6 / A3a (AUDIT_WORD).
"""

import re
from html import unescape


# Grammatical prefix codes that are never the target term.
_PREFIX_CODES = re.compile(r"^[HG]9\d{3}")


def _parse_spans(html: str) -> list[tuple[list[str], str]]:
    """Return list of (strong_numbers, span_text) from preview HTML."""
    hits = re.findall(
        r"<span[^>]*\bstrong=['\"]([^'\"]+)['\"][^>]*>(.*?)</span>",
        html,
        re.IGNORECASE | re.DOTALL,
    )
    result = []
    for raw_strongs, raw_text in hits:
        numbers = raw_strongs.split()
        text = re.sub(r"<[^>]+>", "", raw_text).strip()
        text = unescape(text)
        result.append((numbers, text))
    return result


def _base_prefix(queried_strong: str) -> str | None:
    """Return the numeric base of a Strong's code (e.g. 'H7965' from 'H7965H').

    Returns None if the code has no letter suffix or has no recognisable prefix.
    """
    m = re.match(r'^([HG]\d+)[A-Za-z]$', queried_strong)
    return m.group(1) if m else None


def apply_span_filter(html: str, queried_strong: str) -> dict:
    """Apply the span filter to a single verse's preview HTML.

    Matches if the queried Strong's number OR any sub-gloss with the same
    numeric base (e.g. H7965A satisfies H7965H) appears in a span.

    Returns:
        {
          "match":          True | False,
          "target_word":    str,         # span text for the first matching span ('' if none)
          "span_code_found": str | None, # the specific Strong's code from the matching span
        }
    """
    spans    = _parse_spans(html)
    base     = _base_prefix(queried_strong)   # e.g. 'H7965' or None

    for numbers, text in spans:
        content = [n for n in numbers if not _PREFIX_CODES.match(n)]
        if queried_strong in content:
            return {"match": True, "target_word": text, "span_code_found": queried_strong}
        if base:
            for n in content:
                if n.startswith(base):
                    return {"match": True, "target_word": text, "span_code_found": n}

    return {"match": False, "target_word": "", "span_code_found": None}


def filter_verse_records(raw_records: list[dict], queried_strong: str,
                          raw_html_map: dict[str, str]) -> dict:
    """Filter a list of verse records by span confirmation.

    Args:
        raw_records:    List of verse dicts from step_client.get_verse_records().
                        Each must have 'osisId' key.
        queried_strong: The resolved Strong's number actually searched.
        raw_html_map:   Dict mapping osisId → raw preview HTML string.

    Returns:
        {
          "stored":   [list with span_strong_match=1 and target_word set],
          "filtered": [list with span_strong_match=0],
          "conflict": bool  — True if stored is empty but filtered is not,
        }
    """
    stored   = []
    filtered = []

    for record in raw_records:
        osis_id = record.get("osisId", "")
        html    = raw_html_map.get(osis_id, "")

        if not html:
            stored.append({
                **record,
                "span_strong_match": None,
                "target_word": record.get("target_word", ""),
            })
            continue

        result = apply_span_filter(html, queried_strong)
        enriched = {
            **record,
            "span_strong_match": 1 if result["match"] else 0,
            "target_word": result["target_word"] or record.get("target_word", ""),
            "span_code_found": result.get("span_code_found"),
        }
        if result["match"]:
            stored.append(enriched)
        else:
            filtered.append(enriched)

    conflict = len(stored) == 0 and len(filtered) > 0
    return {"stored": stored, "filtered": filtered, "conflict": conflict}
