"""
step_client.py
──────────────
Client for the locally-running STEP Bible instance (localhost:8989).

Discovered REST API (STEP v26.1.2, Tomcat embedded):
  - Vocab/lexicon:  GET /rest/module/getInfo/{version}//{strong}//
  - Verse search:   GET /rest/search/masterSearch/strong={strong}|version={version}
                    Results capped at 60; use canonical section ranges for overflow.

Configuration via environment (.env):
  STEP_LOCAL_URL   — default: http://localhost:8989
  STEP_VERSION     — default: ESV_th   (tagged Hebrew; ESV text + Strong's)
  STEP_TIMEOUT     — default: 30 (seconds)

Non-canonical STEP Strong's (G9559, G9073, G6347, H9001, H9002 etc.):
  Vocab data is returned but verse search yields 0 results — these are
  STEP-internal SEMR numbers not used in verse tagging.
"""

import os
import re
from html import unescape
from typing import Optional

import requests

try:  # canonical morph parser (H4: morph at the source) — resolve in both script + engine contexts
    from morph_util import morph_for_span, morph_stem
except ImportError:
    from analytics.morph_util import morph_for_span, morph_stem

try:
    from dotenv import load_dotenv
    _ROOT = os.path.join(os.path.dirname(__file__), "..")
    load_dotenv(os.path.join(_ROOT, ".env"))
except ImportError:
    pass


# Canonical OT/NT ranges for verse pagination (60-result cap workaround).
_CANON_RANGES = [
    ("Torah",     "Gen.1.1-Deut.34.12"),
    ("History",   "Josh.1.1-Esth.10.3"),
    ("Poetry",    "Job.1.1-Song.8.14"),
    ("Prophets",  "Isa.1.1-Mal.4.6"),
    ("NT",        "Matt.1.1-Rev.22.21"),
]

# Sub-ranges used when a parent section returns total > 60.
# Each parent maps to ~equal halves that keep most word studies under the cap.
_CANON_SUBSPLITS: dict[str, list[tuple[str, str]]] = {
    "Torah":    [("Torah_A",    "Gen.1.1-Lev.27.34"),    ("Torah_B",    "Num.1.1-Deut.34.12")],
    "History":  [("History_A",  "Josh.1.1-2Chr.36.23"),  ("History_B",  "Ezra.1.1-Esth.10.3")],
    "Poetry":   [("Poetry_A",   "Job.1.1-Ps.150.6"),     ("Poetry_B",   "Prov.1.1-Song.8.14")],
    "Prophets": [("Prophets_A", "Isa.1.1-Dan.12.13"),    ("Prophets_B", "Hos.1.1-Mal.4.6")],
    "NT":       [("NT_A",       "Matt.1.1-Acts.28.31"),  ("NT_B",       "Rom.1.1-Rev.22.21")],
}

# OSIS book codes that belong to the New Testament.
_NT_BOOKS = frozenset([
    "Matt", "Mark", "Luke", "John", "Acts",
    "Rom", "1Cor", "2Cor", "Gal", "Eph", "Phil", "Col",
    "1Thess", "2Thess", "1Tim", "2Tim", "Titus", "Phlm",
    "Heb", "Jas", "1Pet", "2Pet", "1John", "2John", "3John", "Jude", "Rev",
])


class StepClient:
    """Client for the locally-installed STEP Bible REST API.

    Exposes two primary methods for Session A word-analysis use:
      - ``get_vocab_info(strong)``   — lexical data (gloss, definition, related)
      - ``get_verse_records(strong)`` — all ESV verse occurrences, fully paginated
      - ``extract_word_data(strong)`` — complete structured package for both
    """

    def __init__(self) -> None:
        self.base = os.getenv("STEP_LOCAL_URL", "http://localhost:8989").rstrip("/")
        self.version = os.getenv("STEP_VERSION", "ESV_th")
        self.timeout = int(os.getenv("STEP_TIMEOUT", "30"))

    # ── Internal helpers ───────────────────────────────────────────────────

    def _get_json(self, path: str) -> dict:
        url = f"{self.base}/{path.lstrip('/')}"
        r = requests.get(url, timeout=self.timeout)
        r.raise_for_status()
        d = r.json()
        if "errorMessage" in d:
            raise RuntimeError(f"STEP error for {path!r}: {d['errorMessage']}")
        return d

    @staticmethod
    def _strip_html(html: str) -> str:
        """Remove HTML tags and collapse whitespace."""
        text = re.sub(r"<[^>]+>", " ", html)
        text = re.sub(r"\s+", " ", text).strip()
        return unescape(text)

    @staticmethod
    def _strip_html_preserve_newlines(html: str) -> str:
        """Strip HTML; convert <br> variants to newlines before removing tags."""
        text = re.sub(r"<br\s*/?>", "\n", html, flags=re.IGNORECASE)
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r" +", " ", text)
        text = re.sub(r"\n +", "\n", text)
        return unescape(text).strip()

    @staticmethod
    def _target_word_in_span(html: str, strong: str) -> str:
        """Return the ESV word(s) whose <span> carries the given Strong's number."""
        # Each span may carry multiple Strong's: strong='H8057 H9003 H9031'
        hits = re.findall(
            r"<span[^>]*\bstrong=['\"]([^'\"]+)['\"][^>]*>([^<]+)<",
            html,
        )
        words = [word.strip() for strongs, word in hits if strong in strongs.split()]
        return ", ".join(words) if words else ""

    @staticmethod
    def _parse_osisid(osisid: str) -> tuple[str, int, int]:
        """Parse 'Gen.31.27' → ('Gen', 31, 27). Single-chapter book returns chapter=1."""
        parts = osisid.split(".")
        book = parts[0]
        if len(parts) == 3:
            return book, int(parts[1]), int(parts[2])
        # Unexpected format — return safe defaults
        return book, 0, 0

    def _search_range(self, strong: str, ref_range: Optional[str] = None) -> dict:
        query = f"strong={strong}|version={self.version}"
        if ref_range:
            query += f"|reference={ref_range}"
        return self._get_json(f"rest/search/masterSearch/{query}")

    def _text_search_range(self, english_word: str, ref_range: Optional[str] = None) -> dict:
        query = f"version={self.version}|text=+{english_word}"
        if ref_range:
            query += f"|reference={ref_range}"
        return self._get_json(f"rest/search/masterSearch/{query}")

    def _resolved_strong(self, strong: str) -> str:
        """Return the Strong's number STEP actually uses for verse tagging.

        Some base numbers (e.g. H0157, H2428) resolve to suffixed variants
        (H0157G, H2428A) in STEP's lexicon and verse tagging.  This method
        does a lightweight vocab lookup to get the canonical form.
        """
        try:
            d = self._get_json(f"rest/module/getInfo/{self.version}//{strong}//")
            vocabs = d.get("vocabInfos", [])
            if vocabs:
                return vocabs[0].get("strongNumber", strong)
        except Exception:
            pass
        return strong

    # ── Public API — vocab ─────────────────────────────────────────────────

    def get_vocab_info(self, strong: str) -> dict:
        """Return lexical data for a Strong's number.

        Returns a dict with keys:
          strong_number       — resolved STEP identifier (may differ from input)
          language            — 'Hebrew' or 'Greek' (derived from strong_number prefix)
          hebrew_unicode      — accented script form (Hebrew or Greek)
          transliteration     — STEP romanisation (e.g. 'sim.chah')
          gloss               — primary English gloss (= step_search_gloss)
          occurrence_count    — token count (integer; NOT verse count)
          medium_def          — multi-line definition (HTML stripped, newlines preserved)
          meaning_numbered    — True if medium_def contains numbered sub-senses (1), 1a)…)
          causative_form_present — True if medium_def names Hiphil or Piel stem
          lsj_entry           — LSJ dictionary text, HTML stripped (Greek only; '' for Hebrew)
          short_def_mounce    — Mounce short definition (Greek only; '' for Hebrew)
          related_words       — list of {strong, form, gloss, translit}
          raw_related_numbers — comma-separated related Strong's string
          freq_list           — raw frequency distribution string from STEP

        Notes:
          - occurrence_count_qualifier ('about') is NOT available from the API.
          - also_spelled is NOT available from the API (STEP UI only).
          - Both fields remain null / unset and must be filled from the source file.
        """
        d = self._get_json(f"rest/module/getInfo/{self.version}//{strong}//")
        vocabs = d.get("vocabInfos", [])
        if not vocabs:
            return {}
        v = vocabs[0]

        related = []
        for r in v.get("relatedNos", []):
            related.append({
                "strong":   r.get("strongNumber", ""),
                "form":     r.get("matchingForm", ""),
                "gloss":    r.get("gloss", ""),
                "translit": r.get("stepTransliteration", ""),
            })

        # Normalise medium_def: convert <br> to newlines first, then strip tags
        raw_def = v.get("mediumDef", "") or ""
        medium_def = self._strip_html_preserve_newlines(raw_def)

        resolved_strong = v.get("strongNumber", strong)
        language = "Greek" if resolved_strong.startswith("G") else "Hebrew"

        # Derived boolean flags from the definition text
        meaning_numbered = bool(re.search(r"\b1[a-z]?\)", medium_def))
        causative_form_present = bool(
            re.search(r"\b(Hiphil|Piel)\b", medium_def, re.IGNORECASE)
        )

        # Greek-only fields
        lsj_raw = v.get("lsjDefs", "") or ""
        lsj_entry = self._strip_html_preserve_newlines(lsj_raw) if lsj_raw else ""
        short_def_mounce = v.get("shortDefMounce", "") or ""

        return {
            "strong_number":           resolved_strong,
            "language":                language,
            "hebrew_unicode":          v.get("accentedUnicode", ""),
            "transliteration":         v.get("stepTransliteration", ""),
            "gloss":                   v.get("stepGloss", ""),
            "occurrence_count":        v.get("count", 0),
            "medium_def":              medium_def,
            "meaning_numbered":        meaning_numbered,
            "causative_form_present":  causative_form_present,
            "lsj_entry":               lsj_entry,
            "short_def_mounce":        short_def_mounce,
            "related_words":           related,
            "raw_related_numbers":     v.get("rawRelatedNumbers", ""),
            "freq_list":               v.get("freqList", ""),
        }

    # ── Public API — verse search ──────────────────────────────────────────

    def get_verse_records(self, strong: str) -> list[dict]:
        """Return all ESV verse records containing the given Strong's number.

        Each record is a dict:
          osisId, ref, esv_text, target_word,
          testament ('OT' or 'NT'), book_code, chapter (int), verse_num (int)

        Handles the 60-result cap via two layers of canonical section splits:
          Layer 1 — five canonical sections (Torah / History / Poetry / Prophets / NT)
          Layer 2 — halved sub-sections when a layer-1 section total > 60

        All results are deduplicated by osisId and sorted canonically.
        Non-canonical STEP internals return an empty list.
        """
        resolved = self._resolved_strong(strong)
        # First call (no range): reveals total; reuse results if total <= 60
        first = self._search_range(resolved)
        total = first.get("total", 0)

        if total == 0:
            return []

        if total <= 60:
            raw_results = first.get("results", [])
        else:
            seen: dict[str, dict] = {}
            for section, ref_range in _CANON_RANGES:
                d = self._search_range(resolved, ref_range)
                section_total = d.get("total", 0)
                if section_total > 60:
                    # Layer 2: halve the section
                    for _subsect, subrange in _CANON_SUBSPLITS.get(section, []):
                        sd = self._search_range(resolved, subrange)
                        for item in sd.get("results", []):
                            if item["osisId"] not in seen:
                                seen[item["osisId"]] = item
                else:
                    for item in d.get("results", []):
                        if item["osisId"] not in seen:
                            seen[item["osisId"]] = item
            raw_results = list(seen.values())

        records = []
        for item in raw_results:
            html = item.get("preview", "")
            osisid = item["osisId"]
            book_code, chapter, verse_num = self._parse_osisid(osisid)
            testament = "NT" if book_code in _NT_BOOKS else "OT"
            morph_code = morph_for_span(html, resolved)   # H4: morph parsed at the source, not dropped
            records.append({
                "osisId":     osisid,
                "ref":        item["key"],
                "esv_text":   self._strip_html(html),
                "target_word": self._target_word_in_span(html, resolved),
                "testament":  testament,
                "book_code":  book_code,
                "chapter":    chapter,
                "verse_num":  verse_num,
                "morph_code": morph_code,
                "stem":       morph_stem(morph_code),
            })

        records.sort(key=lambda r: r["osisId"])
        return records

    def get_verse_records_with_html(self, strong: str) -> tuple[list[dict], dict[str, str]]:
        """Like get_verse_records() but also returns raw preview HTML per verse.

        Returns:
            (records, html_map)
            records  — same list as get_verse_records()
            html_map — dict mapping osisId → raw preview HTML string
                       (used by engine/span_filter.py for span confirmation)

        Base-fallback: if a code with a letter suffix (e.g. H7965H) returns
        very few results, automatically retries with the numeric base (H7965).
        This handles consolidated/family codes where STEP's verse search uses
        only the sub-gloss forms (H7965A..H7965F) in practise.
        """
        import re as _re
        resolved = self._resolved_strong(strong)
        first = self._search_range(resolved)
        total = first.get("total", 0)

        # Base-fallback: if code has a letter suffix and returns <= 5 verses,
        # try the base number (strip trailing letter), then base+'A' (first sub-gloss).
        # If either returns substantially more verses, use it instead.
        # Example: H7965H → H7965 (0 results) → H7965A (148 results).
        if total <= 5:
            _base_m = _re.match(r'^([HG]\d+)[A-Za-z]$', resolved)
            if _base_m:
                base_code = _base_m.group(1)
                for try_code in [base_code, base_code + 'A']:
                    base_first = self._search_range(try_code)
                    base_total = base_first.get("total", 0)
                    if base_total > total:
                        resolved = try_code
                        first    = base_first
                        total    = base_total
                        break

        if total == 0:
            return [], {}

        if total <= 60:
            raw_results = first.get("results", [])
        else:
            seen: dict[str, dict] = {}
            for section, ref_range in _CANON_RANGES:
                d = self._search_range(resolved, ref_range)
                section_total = d.get("total", 0)
                if section_total > 60:
                    for _subsect, subrange in _CANON_SUBSPLITS.get(section, []):
                        sd = self._search_range(resolved, subrange)
                        for item in sd.get("results", []):
                            if item["osisId"] not in seen:
                                seen[item["osisId"]] = item
                else:
                    for item in d.get("results", []):
                        if item["osisId"] not in seen:
                            seen[item["osisId"]] = item
            raw_results = list(seen.values())

        records = []
        html_map = {}
        for item in raw_results:
            html = item.get("preview", "")
            osisid = item["osisId"]
            book_code, chapter, verse_num = self._parse_osisid(osisid)
            testament = "NT" if book_code in _NT_BOOKS else "OT"
            html_map[osisid] = html
            morph_code = morph_for_span(html, resolved)   # H4: morph at the source (parity with get_verse_records)
            records.append({
                "osisId":      osisid,
                "ref":         item["key"],
                "esv_text":    self._strip_html(html),
                "target_word": self._target_word_in_span(html, resolved),
                "testament":   testament,
                "book_code":   book_code,
                "chapter":     chapter,
                "verse_num":   verse_num,
                "morph_code":  morph_code,
                "stem":        morph_stem(morph_code),
            })

        records.sort(key=lambda r: r["osisId"])
        return records, html_map

    # ── Public API — full extraction ───────────────────────────────────────

    def get_strongs_for_word(self, english_word: str) -> list[dict]:
        """Return all Strong's numbers that tag the given English word in ESV text.

        Uses STEP's text search (``text=+{word}``), which returns verses whose ESV
        text contains the English word with full Strong's span tagging.  The span
        that wraps the matching English word carries the Strong's number(s) for that
        translation choice.

        Two-level canonical pagination (identical to ``get_verse_records``) handles
        the 60-result cap.  Grammar-particle codes (H9xxx / G9xxx) are excluded.
        Suffix variants (H5315G → H5315) are merged into their base numbers.

        Returns a list of ``{"strong": str, "count": int}`` dicts sorted by
        ``count`` descending.  ``count`` is the number of unique verses where
        the English word is tagged with that Strong's number.

        Example::

            client.get_strongs_for_word("soul")
            # → [{"strong": "H5315", "count": 148}, {"strong": "G5590", "count": 31}, …]
        """
        # Regex to match <span strong='...'> that contains the English word.
        span_pat = re.compile(
            r"<span[^>]*\bstrong=['\"]([^'\"]+)['\"][^>]*>([^<]+)<",
            re.IGNORECASE,
        )
        word_pat = re.compile(r"\b" + re.escape(english_word) + r"\b", re.IGNORECASE)

        seen: dict[str, str] = {}   # osisId → preview html (dedup verses)

        def _collect(d: dict) -> None:
            for item in d.get("results", []):
                osis = item.get("osisId") or item.get("key", "")
                if osis not in seen:
                    seen[osis] = item.get("preview", "")

        # Same two-level pagination as get_verse_records.
        first = self._text_search_range(english_word)
        total = first.get("total", 0)

        if total <= 60:
            _collect(first)
        else:
            for section, ref_range in _CANON_RANGES:
                d = self._text_search_range(english_word, ref_range)
                section_total = d.get("total", 0)
                if section_total > 60:
                    for _subsect, subrange in _CANON_SUBSPLITS.get(section, []):
                        _collect(self._text_search_range(english_word, subrange))
                else:
                    _collect(d)

        # Count how many verses tag the English word with each base Strong's.
        tally: dict[str, int] = {}
        for html in seen.values():
            for span_m in span_pat.finditer(html):
                strongs_attr, word_text = span_m.group(1), span_m.group(2)
                if not word_pat.search(word_text):
                    continue
                for s in strongs_attr.split():
                    # Skip grammar-particle internal codes (H9xxx / G9xxx)
                    if not re.match(r"^[HG]\d{4}", s) or re.match(r"^[HG]9", s):
                        continue
                    base = re.sub(r"[A-Z]+$", "", s)  # H5315G → H5315
                    tally[base] = tally.get(base, 0) + 1

        return [
            {"strong": s, "count": c}
            for s, c in sorted(tally.items(), key=lambda x: -x[1])
        ]

    def get_verse_records_by_english(self, english_word: str) -> list[dict]:
        """Return all ESV verse records where the given English word appears.

        Each record has the same fields as ``get_verse_records()`` plus:
          tagging_strongs — list of base Strong's numbers (e.g. 'H5315', 'G5590')
                            whose span in the verse HTML wraps the matching word.
                            Grammar-particle codes (H9xxx / G9xxx) are excluded.
                            Sub-gloss suffixes are stripped (H5315G → H5315).

        Two-level canonical pagination handles the 60-result cap, identical to
        the Strong's-based search.

        This corresponds to STEP's "English word search" entry point — it finds
        every verse where the ESV uses this word, regardless of which underlying
        Hebrew/Greek term is tagged, and reports which term(s) drove each
        translation choice.
        """
        span_pat = re.compile(
            r"<span[^>]*\bstrong=['\"]([^'\"]+)['\"][^>]*>([^<]+)<",
            re.IGNORECASE,
        )
        word_pat = re.compile(r"\b" + re.escape(english_word) + r"\b", re.IGNORECASE)

        seen: dict[str, dict] = {}  # osisId → raw result item (dedup)

        def _collect(d: dict) -> None:
            for item in d.get("results", []):
                osis = item.get("osisId") or item.get("key", "")
                if osis not in seen:
                    seen[osis] = item

        first = self._text_search_range(english_word)
        total = first.get("total", 0)

        if total <= 60:
            _collect(first)
        else:
            for section, ref_range in _CANON_RANGES:
                d = self._text_search_range(english_word, ref_range)
                section_total = d.get("total", 0)
                if section_total > 60:
                    for _subsect, subrange in _CANON_SUBSPLITS.get(section, []):
                        _collect(self._text_search_range(english_word, subrange))
                else:
                    _collect(d)

        records = []
        for osisid, item in seen.items():
            html = item.get("preview", "")
            book_code, chapter, verse_num = self._parse_osisid(osisid)
            testament = "NT" if book_code in _NT_BOOKS else "OT"

            # Collect base Strong's numbers from spans that wrap the English word.
            tagging_strongs: list[str] = []
            for span_m in span_pat.finditer(html):
                strongs_attr, word_text = span_m.group(1), span_m.group(2)
                if not word_pat.search(word_text):
                    continue
                for s in strongs_attr.split():
                    if not re.match(r"^[HG]\d{4}", s) or re.match(r"^[HG]9", s):
                        continue
                    base = re.sub(r"[A-Z]+$", "", s)   # H5315G → H5315
                    if base not in tagging_strongs:
                        tagging_strongs.append(base)

            records.append({
                "osisId":          osisid,
                "ref":             item["key"],
                "esv_text":        self._strip_html(html),
                "target_word":     english_word,
                "testament":       testament,
                "book_code":       book_code,
                "chapter":         chapter,
                "verse_num":       verse_num,
                "tagging_strongs": tagging_strongs,
            })

        records.sort(key=lambda r: r["osisId"])
        return records

    # ── Public API — meaning-based term discovery ─────────────────────────

    def get_meaning_terms(self, english_word: str) -> dict:
        """Return STEP's curated list of terms whose meaning relates to a word.

        Uses the ``meanings=`` search parameter, which maps to STEP's
        ``ORIGINAL_MEANING`` search type.  This is the data shown in STEP's
        **Related words** panel — a lexically curated set of Hebrew/Greek
        terms whose meaning encompasses the English concept, regardless of
        how the ESV translates each occurrence.

        This is fundamentally different from ``get_strongs_for_word()``, which
        only finds codes where the ESV uses the literal English word.  For
        example, ``meanings=anger`` returns H2734 (חָרָה, "to be incensed")
        which the ESV never translates as "anger" but which is semantically
        central to the concept.

        Returns a dict:
          definitions       — list of term dicts, each with:
                                strongNumber, matchingForm, stepTransliteration,
                                gloss, type ('word'/'verb'), popularity (str)
          strong_highlights — list of Strong's codes (same terms, flat list)
          total_verses      — total verse count from the search

        Example::

            client.get_meaning_terms("anger")
            # → {"definitions": [...37 terms...],
            #    "strong_highlights": ["H0644", "H2734", ...],
            #    "total_verses": 687}
        """
        d = self._get_json(
            f"rest/search/masterSearch/version={self.version}"
            f"|meanings={english_word}"
        )
        return {
            "definitions":       d.get("definitions", []),
            "strong_highlights": d.get("strongHighlights", []),
            "total_verses":      d.get("total", 0),
        }

    # ── Public API — full extraction ───────────────────────────────────────

    def extract_word_data(self, strong: str) -> dict:
        """Return a complete structured data package for Session A.

        Keys:
          strong         — the requested Strong's number
          vocab          — output of get_vocab_info()
          verse_records  — output of get_verse_records()
          verse_count    — number of unique verses returned
          testament      — 'OT', 'NT', or 'both' (derived from verse_records)
          notes          — list of warning strings (e.g. non-canonical Strong's)
        """
        notes = []
        vocab = self.get_vocab_info(strong)

        if not vocab:
            notes.append(f"No vocab data found for {strong}")
            return {
                "strong": strong, "vocab": {}, "verse_records": [],
                "verse_count": 0, "testament": None, "notes": notes,
            }

        resolved = vocab["strong_number"]
        if resolved != strong:
            notes.append(f"Strong's {strong} resolved to {resolved} in STEP")

        verse_records = self.get_verse_records(strong)
        vc = len(verse_records)
        oc = vocab.get("occurrence_count", 0)

        if vc == 0 and oc > 0:
            notes.append(
                f"Verse search returned 0 results despite occurrence_count={oc}. "
                "This may be a non-canonical STEP internal Strong's number."
            )
        elif abs(vc - oc) > 5:
            notes.append(
                f"Verse count ({vc} verses) vs occurrence count ({oc} tokens). "
                "Multiple occurrences in a single verse are counted once here."
            )

        # Derive testament coverage
        testaments = {r["testament"] for r in verse_records}
        if testaments == {"OT"}:
            testament = "OT"
        elif testaments == {"NT"}:
            testament = "NT"
        elif testaments:
            testament = "both"
        else:
            testament = None

        return {
            "strong":        strong,
            "vocab":         vocab,
            "verse_records": verse_records,
            "verse_count":   vc,
            "testament":     testament,
            "notes":         notes,
        }

    # ── Public API — term discovery (Phase 1) ─────────────────────────────

    def get_related_term_cluster(self, strong: str) -> dict:
        """Return the full term cluster for a Strong's number — all sub-glosses
        and semantically related terms as defined by STEP's ``relatedNos`` field.

        This is a **read-only discovery method** — it never touches the database
        and performs no extraction.  It is the foundation of Phase 1 term mapping.

        Algorithm:
          1. Resolve the input code and fetch its vocab.
          2. Collect all codes from ``relatedNos`` (siblings + relatives).
          3. Separately enumerate sub-gloss siblings — codes sharing the same
             numeric base with a single letter suffix (e.g. H5315G … H5315N).
          4. Union (2) and (3), then fetch vocab + verse_count for every code.
          5. Return a structured dict separating sub-glosses from related terms.

        Returns a dict:
          primary_code    — the resolved Strong's code fetched first
          primary_vocab   — vocab dict for the primary code (from get_vocab_info)
          sub_glosses     — list of term_entry dicts for sibling sub-glosses
                            (same numeric base, letter suffix; e.g. H5315G–H5315N)
          related_terms   — list of term_entry dicts for other related codes
                            (different numeric base or no suffix relationship)
          all_codes       — flat list of all Strong's codes in the cluster

        Each term_entry dict:
          code            — Strong's code (e.g. H5315H)
          gloss           — STEP stepGloss
          transliteration — STEP romanisation
          script_form     — accentedUnicode (Hebrew/Greek script)
          vocab_count     — occurrence count across all STEP versions
          verse_count     — verse count in ESV_th (from search API)
          medium_def      — stripped multi-line definition
          is_sub_gloss    — True if same numeric base as primary_code
          is_proper_noun  — True if mediumDef or gloss suggests a name/place
          notes           — list of warning strings

        Proper-noun detection: if the gloss is title-cased and the definition
        contains 'proper noun', 'name', or starts with a capital; also flags
        H/G codes known to be grammar particles (H9xxx / G9xxx).
        """
        # ── Step 1: resolve primary code and fetch vocab ──────────────────
        primary_vocab = self.get_vocab_info(strong)
        if not primary_vocab:
            return {
                "primary_code":  strong,
                "primary_vocab": {},
                "sub_glosses":   [],
                "related_terms": [],
                "all_codes":     [],
            }
        primary_code = primary_vocab["strong_number"]

        # Numeric base: strip trailing letter(s) — H5315G → H5315, G5590G → G5590
        base_match = re.match(r'^([HG]\d+)[A-Za-z]+$', primary_code)
        numeric_base = base_match.group(1) if base_match else primary_code

        # ── Step 2: collect related codes from relatedNos ─────────────────
        related_codes: set[str] = set()
        for rw in primary_vocab.get("related_words", []):
            code = rw.get("strong", "").strip()
            if code and code != primary_code:
                related_codes.add(code)

        # ── Step 3: collect all sub-glosses via probing (G → N) ──────────
        # STEP's relatedNos often lists siblings, but probe explicitly to catch any gaps.
        for suffix in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            candidate = f"{numeric_base}{suffix}"
            if candidate == primary_code:
                continue   # already have primary
            if candidate in related_codes:
                continue   # already collected
            # Probe: if STEP returns a vocabInfo for this code, it exists.
            try:
                d = self._get_json(
                    f"rest/module/getInfo/{self.version}//{candidate}//"
                )
                vis = d.get("vocabInfos", [])
                if vis and vis[0].get("strongNumber") == candidate:
                    related_codes.add(candidate)
                else:
                    # No more sub-glosses — stop probing this family
                    break
            except Exception:
                break

        # ── Step 4: fetch vocab + verse_count for every related code ──────
        def _term_entry(code: str) -> dict:
            entry_notes: list[str] = []
            # Skip grammar-particle internal codes
            if re.match(r'^[HG]9', code):
                return {}
            try:
                v = self.get_vocab_info(code)
            except Exception as exc:
                return {"code": code, "notes": [str(exc)]}
            if not v:
                return {"code": code, "notes": ["no vocab data"]}

            # Verse count
            try:
                sd = self._search_range(code)
                vc = sd.get("total", 0)
            except Exception:
                vc = 0
                entry_notes.append("verse search failed")

            gloss = v.get("gloss", "")
            medium_def = v.get("medium_def", "")

            # Is this code a sub-gloss of our primary numeric base?
            code_base_m = re.match(r'^([HG]\d+)[A-Za-z]+$', code)
            code_base = code_base_m.group(1) if code_base_m else code
            is_sub = code_base == numeric_base

            # Proper-noun detection (heuristic)
            is_proper = bool(
                re.search(r'\bproper noun\b|\bpersonal name\b|\bplace name\b',
                          medium_def, re.IGNORECASE)
                or (gloss and gloss[0].isupper() and len(gloss.split()) == 1
                    and gloss not in ("I", "A"))
            )

            return {
                "code":            code,
                "gloss":           gloss,
                "transliteration": v.get("transliteration", ""),
                "script_form":     v.get("hebrew_unicode", ""),
                "vocab_count":     v.get("occurrence_count", 0),
                "verse_count":     vc,
                "medium_def":      medium_def,
                "is_sub_gloss":    is_sub,
                "is_proper_noun":  is_proper,
                "notes":           entry_notes,
            }

        sub_glosses: list[dict] = []
        related_terms: list[dict] = []

        for code in sorted(related_codes):
            entry = _term_entry(code)
            if not entry:
                continue
            if entry.get("is_sub_gloss"):
                sub_glosses.append(entry)
            else:
                related_terms.append(entry)

        # Sort sub-glosses by code, related terms by verse_count desc
        sub_glosses.sort(key=lambda e: e["code"])
        related_terms.sort(key=lambda e: -e.get("verse_count", 0))

        all_codes = [primary_code] + [e["code"] for e in sub_glosses] + \
                    [e["code"] for e in related_terms]

        return {
            "primary_code":  primary_code,
            "primary_vocab": primary_vocab,
            "sub_glosses":   sub_glosses,
            "related_terms": related_terms,
            "all_codes":     all_codes,
        }
