"""
span_filter.py
──────────────
Span-based verse filtering (§5.2, v4).

STEP masterSearch preview HTML contains inline <span> tags:
    <span morph='HVqp3ms' strong='H7442B H9001'>sang</span>

The filter rule:
  - If the queried Strong's appears in the span's strong= attribute → STORE (match=1)
  - If only related/sibling forms appear → DISCARD (match=0, increment filtered count)

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


def apply_span_filter(html: str, queried_strong: str) -> dict:
    """Apply the span filter to a single verse's preview HTML.

    Returns:
        {
          "match":       True | False,   # verse should be stored
          "target_word": str,            # span text for the matching span ('' if none)
        }
    """
    spans = _parse_spans(html)
    for numbers, text in spans:
        # Ignore spans that are purely grammatical prefix codes.
        content_numbers = [n for n in numbers if not _PREFIX_CODES.match(n)]
        if queried_strong in content_numbers:
            return {"match": True, "target_word": text}
    return {"match": False, "target_word": ""}


def filter_verse_records(raw_records: list[dict], queried_strong: str,
                          raw_html_map: dict[str, str]) -> dict:
    """Filter a list of verse records by span confirmation.

    Args:
        raw_records:    List of verse dicts from step_client.get_verse_records().
                        Each must have 'osisId' key.
        queried_strong: The resolved Strong's number actually searched.
        raw_html_map:   Dict mapping osisId → raw preview HTML string.
                        (step_client must supply this; see notes below.)

    Returns:
        {
          "stored":   [list of verse dicts with span_strong_match=1 and target_word set],
          "filtered": [list of verse dicts with span_strong_match=0],
          "conflict": bool  — True if stored is empty after filtering,
        }

    Notes:
        step_client.get_verse_records() already extracts target_word from spans.
        For the filter we need the raw HTML. The step_client should be extended
        (or called differently) to also return the preview HTML per verse.
        This function accepts the html_map as a separate argument to keep
        concerns separated.
    """
    stored = []
    filtered = []

    for record in raw_records:
        osis_id = record.get("osisId", "")
        html = raw_html_map.get(osis_id, "")

        if not html:
            # No HTML available — default to storing with match=None (will trigger WR-20).
            record = {**record, "span_strong_match": None, "target_word": record.get("target_word", "")}
            stored.append(record)
            continue

        result = apply_span_filter(html, queried_strong)
        enriched = {
            **record,
            "span_strong_match": 1 if result["match"] else 0,
            "target_word": result["target_word"] or record.get("target_word", ""),
        }
        if result["match"]:
            stored.append(enriched)
        else:
            filtered.append(enriched)

    conflict = len(stored) == 0 and len(filtered) > 0
    return {"stored": stored, "filtered": filtered, "conflict": conflict}
