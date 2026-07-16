"""
step_client.py
──────────────
Client for the locally-running STEP Bible instance.

CONFIGURATION LIVES IN `iba/config/utility/step.json`, not here.
The base URL, the version, the timeout, every API route, the 60-cap and the
pagination parameters are read from that file at construction. Nothing STEP-related
is read from the environment: STEP is ALWAYS the local server, never the web
(researcher ruling 2026-07-16), so the connection is not environment-dependent.

This module holds only FACTS — the canon's book order, STEP's response field names,
and how to parse its HTML. Those are not decisions anyone makes. Choices live in
the json; facts live here.

`check.step.up` is enforced: the server is probed before the first request of every
process, and a failure raises StepUnavailable rather than degrading. An untagged
module answers a Strong's search with zero results and no error, so the probe checks
for TAGGING, not merely for a response.

Non-canonical STEP Strong's (G9559, H9001 …): vocab data is returned but verse
search yields 0 results — STEP-internal SEMR numbers not used in verse tagging.
See `options.limits.exclude_strongs_pattern`.
"""

import json
import pathlib
import re
import sys
from html import unescape
from typing import Optional

import requests

try:  # canonical morph parser (H4: morph at the source) — script + engine contexts
    from morph_util import morph_for_span, morph_stem
except ImportError:
    from analytics.morph_util import morph_for_span, morph_stem


CONFIG_PATH = (pathlib.Path(__file__).resolve().parents[2]
               / "iba" / "config" / "utility" / "step.json")

# Canonical OSIS book order (Gen→Rev). A FACT, not a setting — it drives the
# cap-proof forward-walk (_paginate_all), which needs only the *order* to find the
# frontier verse; no per-book chapter/verse counts required.
_OSIS_ORDER = [
    "Gen", "Exod", "Lev", "Num", "Deut", "Josh", "Judg", "Ruth",
    "1Sam", "2Sam", "1Kgs", "2Kgs", "1Chr", "2Chr", "Ezra", "Neh", "Esth",
    "Job", "Ps", "Prov", "Eccl", "Song",
    "Isa", "Jer", "Lam", "Ezek", "Dan", "Hos", "Joel", "Amos", "Obad",
    "Jonah", "Mic", "Nah", "Hab", "Zeph", "Hag", "Zech", "Mal",
    "Matt", "Mark", "Luke", "John", "Acts",
    "Rom", "1Cor", "2Cor", "Gal", "Eph", "Phil", "Col",
    "1Thess", "2Thess", "1Tim", "2Tim", "Titus", "Phlm",
    "Heb", "Jas", "1Pet", "2Pet", "1John", "2John", "3John", "Jude", "Rev",
]
_OSIS_IDX = {name: i for i, name in enumerate(_OSIS_ORDER)}
_NT_BOOKS = frozenset(_OSIS_ORDER[_OSIS_IDX["Matt"]:])


class StepUnavailable(RuntimeError):
    """check.step.up failed. The run stops here — a raw process without its source
    is not a slow run, it is a wrong one."""


def load_step_config(path: pathlib.Path = CONFIG_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))["options"]


class StepClient:
    """Client for the locally-installed STEP Bible REST API.

    Primary methods:
      - ``get_vocab_info(strong)``    — lexical data (gloss, definition, related)
      - ``get_verse_records(strong)`` — all ESV verse occurrences, fully paginated
      - ``extract_word_data(strong)`` — complete structured package for both
    """

    def __init__(self, config: Optional[dict] = None) -> None:
        opts = config or load_step_config()
        conn = opts["connection"]
        self.base = conn["base_url"].rstrip("/")
        self.version = conn["version"]
        self.timeout = int(conn["timeout_seconds"])

        self.apis = opts["apis"]
        limits = opts["limits"]
        self.cap = int(limits["result_cap"])
        self.canon_start = limits["pagination"]["canon_start"]
        self.canon_end = limits["pagination"]["canon_end"]
        self.max_iterations = int(limits["pagination"]["max_iterations"])
        self.base_fallback_threshold = int(limits["base_fallback_threshold"])
        self.subgloss_suffixes = limits["subgloss_probe_suffixes"]
        self.exclude_strongs = re.compile(limits["exclude_strongs_pattern"])

        self.multi_code_policy = opts["multi_code"]["policy"]
        self._preflight_done = False
        self._in_preflight = False

    # ── Routes (verbatim from config; formatted, never composed) ────────────

    def _route(self, api: str, ranged: bool = False, **kw) -> str:
        spec = self.apis[api]
        key = "route_ranged" if ranged else "route"
        if key not in spec:
            raise KeyError(f"api {api!r} has no {key} in step.json")
        return spec[key].format(version=self.version, **kw)

    # ── check.step.up ───────────────────────────────────────────────────────

    def preflight(self) -> None:
        """Prove the local server is up AND answering with the tagged module.

        Runs once per client, before the first request. Raises StepUnavailable on
        any failure — the rule is stop, not degrade (researcher ruling 2026-07-16).
        """
        chk = next(c for c in _checks() if c["id"] == "check.step.up")
        probe = chk["probe"]
        strong = probe["strong"]
        self._in_preflight = True
        try:
            # 1. REACHABLE + 2. VERSION ACCEPTED
            try:
                d = self._get_json(self._route("module.getInfo", strong=strong))
            except requests.RequestException as exc:
                raise StepUnavailable(
                    f"STEP is not reachable at {self.base} ({exc.__class__.__name__}). "
                    f"Start the local server and re-run."
                ) from exc
            vocabs = d.get("vocabInfos") or []
            if not vocabs or not vocabs[0].get("stepGloss"):
                raise StepUnavailable(
                    f"STEP answered at {self.base} but returned no lexicon entry for the "
                    f"probe {strong} under version {self.version!r}. The version is not "
                    f"present or not answering."
                )
            # STEP's verse search answers only on the RESOLVED code: a base number
            # returns 0 and no error (H0430 -> 0, H0430G -> 2088). Searching the
            # unresolved code would read as an untagged module and halt every raw run
            # on a healthy server.
            resolved = vocabs[0].get("strongNumber", strong)
            # 3. TAGGED — the discriminator. An untagged module returns 0 here too,
            #    well-formed and without error, and every Strong's in the study
            #    would silently vanish.
            total = self._get_json(
                self._route("search.masterSearch.strong", strong=resolved)
            ).get("total", 0)
            if total < probe["expect_verse_total_min"]:
                raise StepUnavailable(
                    f"STEP is up at {self.base} and version {self.version!r} answers, but a "
                    f"Strong's search for the probe {strong} (resolved: {resolved}) returned "
                    f"{total} verses. The module is NOT TAGGED — it will return "
                    f"correct-looking text carrying none of the Strong's numbers or "
                    f"morphology the study depends on."
                )
        finally:
            self._in_preflight = False
        self._preflight_done = True

    # ── Internal helpers ───────────────────────────────────────────────────

    def _get_json(self, path: str) -> dict:
        if not self._preflight_done and not self._in_preflight:
            self.preflight()
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
        """Parse 'Gen.31.27' → ('Gen', 31, 27)."""
        parts = osisid.split(".")
        book = parts[0]
        if len(parts) == 3:
            return book, int(parts[1]), int(parts[2])
        return book, 0, 0

    def _search_range(self, strong: str, ref_range: Optional[str] = None) -> dict:
        if ref_range:
            return self._get_json(self._route("search.masterSearch.strong", ranged=True,
                                              strong=strong, range=ref_range))
        return self._get_json(self._route("search.masterSearch.strong", strong=strong))

    def _text_search_range(self, english_word: str, ref_range: Optional[str] = None) -> dict:
        if ref_range:
            return self._get_json(self._route("search.masterSearch.text", ranged=True,
                                              text=english_word, range=ref_range))
        return self._get_json(self._route("search.masterSearch.text", text=english_word))

    @staticmethod
    def _canon_key(osis_id: str) -> tuple:
        """Canonical sort key (book_order, chapter, verse) from an osisId like
        'Prov.28.1' (sub-verse markers such as '!a' are tolerated)."""
        parts = osis_id.split(".")
        book = parts[0]
        ch = int(re.sub(r"\D.*", "", parts[1]) or 0) if len(parts) > 1 else 0
        vs = int(re.sub(r"\D.*", "", parts[2]) or 0) if len(parts) > 2 else 0
        return (_OSIS_IDX.get(book, 999), ch, vs)

    def _paginate_all(self, search_fn, query: str) -> list[dict]:
        """Cap-proof pagination over STEP's result cap, for any masterSearch.

        `search_fn(query, ref_range=None)` is `_search_range` (Strong's) or
        `_text_search_range` (English text). STEP caps every response at
        `options.limits.result_cap` rows but reports the true `total`. We forward-walk
        the canon: query `<frontier>-{canon_end}`, absorb the rows, advance the frontier
        to the canonically-last verse seen, repeat until the remainder fits one page.
        The frontier needs canonical *order* only — no versification map.

        Self-validates against `total` and warns on any shortfall, so a truncation can
        never again be silent. (check.step.cap-exhausted makes that shortfall a halt;
        it is not enforced here — see the note in the module docstring's config file.)
        """
        first = search_fn(query)
        total = first.get("total", 0)
        if total == 0:
            return []
        if total <= self.cap:
            return first.get("results", [])
        seen: dict[str, dict] = {}
        start, end = self.canon_start, self.canon_end
        for _ in range(self.max_iterations):
            d = search_fn(query, f"{start}-{end}")
            rows = d.get("results", [])
            remaining_total = d.get("total", 0)
            if not rows:
                break
            for it in rows:
                osis = it.get("osisId") or it.get("key", "")
                if osis and osis not in seen:
                    seen[osis] = it
            if remaining_total <= len(rows):
                break  # everything from `start` onward fits this page
            frontier = max(rows, key=lambda it: self._canon_key(
                it.get("osisId") or it.get("key", "")))
            nxt = (frontier.get("osisId") or "").split("!")[0]
            if not nxt or nxt == start:
                break  # no forward progress — stop rather than loop
            start = nxt
        if len(seen) < total:
            print(f"[step_client] WARNING: pagination collected {len(seen)} of "
                  f"{total} reported results for {query!r} — possible truncation.",
                  file=sys.stderr)
        return list(seen.values())

    def _resolved_strong(self, strong: str) -> str:
        """Return the Strong's number STEP actually uses for verse tagging.

        Some base numbers (H0157, H2428) resolve to suffixed variants (H0157G, H2428A).

        ⚠ options.multi_code.policy = 'primary_only' — this returns vocabInfos[0] and
        silently DROPS lettered siblings. ruach H7307 keeps H7307G (194) and drops
        H7307H (137) + H7307I (7). Every multi-code term under-pulls. The resolution
        rule is a RECONCILE decision in step.json, not an implementation detail.
        """
        try:
            d = self._get_json(self._route("module.getInfo", strong=strong))
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
          meaning_numbered    — True if medium_def contains numbered sub-senses
          causative_form_present — True if medium_def names Hiphil or Piel stem
          lsj_entry           — LSJ dictionary text, HTML stripped (Greek only)
          short_def_mounce    — Mounce short definition (Greek only)
          related_words       — list of {strong, form, gloss, translit}
          raw_related_numbers — comma-separated related Strong's string
          freq_list           — raw frequency distribution string from STEP

        Notes:
          - occurrence_count_qualifier ('about') is NOT available from the API.
          - also_spelled is NOT available from the API (STEP UI only).
        """
        d = self._get_json(self._route("module.getInfo", strong=strong))
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

        raw_def = v.get("mediumDef", "") or ""
        medium_def = self._strip_html_preserve_newlines(raw_def)

        resolved_strong = v.get("strongNumber", strong)
        language = "Greek" if resolved_strong.startswith("G") else "Hebrew"

        meaning_numbered = bool(re.search(r"\b1[a-z]?\)", medium_def))
        causative_form_present = bool(
            re.search(r"\b(Hiphil|Piel)\b", medium_def, re.IGNORECASE)
        )

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

        Each record: osisId, ref, esv_text, target_word, testament ('OT'/'NT'),
        book_code, chapter (int), verse_num (int), morph_code, stem.

        The result cap is handled by the forward-walk (_paginate_all), which
        self-validates against STEP's reported total. Results are deduplicated by
        osisId and sorted canonically. Non-canonical STEP internals return [].
        """
        resolved = self._resolved_strong(strong)
        first = self._search_range(resolved)
        if first.get("total", 0) == 0:
            return []

        raw_results = self._paginate_all(self._search_range, resolved)

        records = []
        for item in raw_results:
            html = item.get("preview", "")
            osisid = item["osisId"]
            book_code, chapter, verse_num = self._parse_osisid(osisid)
            morph_code = morph_for_span(html, resolved)   # H4: morph at the source
            records.append({
                "osisId":      osisid,
                "ref":         item["key"],
                "esv_text":    self._strip_html(html),
                "target_word": self._target_word_in_span(html, resolved),
                "testament":   "NT" if book_code in _NT_BOOKS else "OT",
                "book_code":   book_code,
                "chapter":     chapter,
                "verse_num":   verse_num,
                "morph_code":  morph_code,
                "stem":        morph_stem(morph_code),
            })

        records.sort(key=lambda r: r["osisId"])
        return records

    def get_verse_records_with_html(self, strong: str) -> tuple[list[dict], dict[str, str]]:
        """Like get_verse_records() but also returns raw preview HTML per verse.

        Returns (records, html_map); html_map maps osisId → raw preview HTML
        (used by engine/span_filter.py for span confirmation).

        Base-fallback: a suffixed code returning <= options.limits.base_fallback_threshold
        verses is retried against its numeric base, then base+'A'. Handles consolidated
        family codes where STEP's verse search uses only the sub-gloss forms in practice
        (H7965H → H7965 → H7965A: 0 → 148 results).
        """
        resolved = self._resolved_strong(strong)
        first = self._search_range(resolved)
        total = first.get("total", 0)

        if total <= self.base_fallback_threshold:
            base_m = re.match(r"^([HG]\d+)[A-Za-z]$", resolved)
            if base_m:
                base_code = base_m.group(1)
                for try_code in [base_code, base_code + "A"]:
                    base_first = self._search_range(try_code)
                    base_total = base_first.get("total", 0)
                    if base_total > total:
                        resolved, first, total = try_code, base_first, base_total
                        break

        if total == 0:
            return [], {}

        raw_results = self._paginate_all(self._search_range, resolved)

        records = []
        html_map = {}
        for item in raw_results:
            html = item.get("preview", "")
            osisid = item["osisId"]
            book_code, chapter, verse_num = self._parse_osisid(osisid)
            html_map[osisid] = html
            morph_code = morph_for_span(html, resolved)
            records.append({
                "osisId":      osisid,
                "ref":         item["key"],
                "esv_text":    self._strip_html(html),
                "target_word": self._target_word_in_span(html, resolved),
                "testament":   "NT" if book_code in _NT_BOOKS else "OT",
                "book_code":   book_code,
                "chapter":     chapter,
                "verse_num":   verse_num,
                "morph_code":  morph_code,
                "stem":        morph_stem(morph_code),
            })

        records.sort(key=lambda r: r["osisId"])
        return records, html_map

    # ── Public API — English-text discovery ───────────────────────────────

    def _tagging_strongs(self, html: str, word_pat: re.Pattern) -> list[str]:
        """Base Strong's numbers whose span wraps the matching English word."""
        span_pat = re.compile(
            r"<span[^>]*\bstrong=['\"]([^'\"]+)['\"][^>]*>([^<]+)<", re.IGNORECASE)
        out: list[str] = []
        for m in span_pat.finditer(html):
            strongs_attr, word_text = m.group(1), m.group(2)
            if not word_pat.search(word_text):
                continue
            for s in strongs_attr.split():
                if not re.match(r"^[HG]\d{4}", s) or self.exclude_strongs.match(s):
                    continue
                base = re.sub(r"[A-Z]+$", "", s)   # H5315G → H5315
                if base not in out:
                    out.append(base)
        return out

    def get_strongs_for_word(self, english_word: str) -> list[dict]:
        """Return all Strong's numbers that tag the given English word in ESV text.

        DISCOVERY ONLY — search.masterSearch.text has an empty `may_source` in
        step.json: an English-text hit is not an original-language occurrence, so
        this may propose Strong's numbers to investigate but must never produce a
        raw verse record (check.step.api-fit).

        Returns [{"strong": str, "count": int}, …] sorted by count desc, where count
        is the number of unique verses tagging the English word with that Strong's.
        """
        word_pat = re.compile(r"\b" + re.escape(english_word) + r"\b", re.IGNORECASE)
        seen: dict[str, str] = {}
        for item in self._paginate_all(self._text_search_range, english_word):
            osis = item.get("osisId") or item.get("key", "")
            if osis and osis not in seen:
                seen[osis] = item.get("preview", "")

        tally: dict[str, int] = {}
        for html in seen.values():
            for base in self._tagging_strongs(html, word_pat):
                tally[base] = tally.get(base, 0) + 1

        return [{"strong": s, "count": c}
                for s, c in sorted(tally.items(), key=lambda x: -x[1])]

    def get_verse_records_by_english(self, english_word: str) -> list[dict]:
        """Return all ESV verse records where the given English word appears.

        Same fields as get_verse_records() plus `tagging_strongs`. DISCOVERY ONLY —
        see get_strongs_for_word().
        """
        word_pat = re.compile(r"\b" + re.escape(english_word) + r"\b", re.IGNORECASE)
        seen: dict[str, dict] = {}
        for item in self._paginate_all(self._text_search_range, english_word):
            osis = item.get("osisId") or item.get("key", "")
            if osis and osis not in seen:
                seen[osis] = item

        records = []
        for osisid, item in seen.items():
            html = item.get("preview", "")
            book_code, chapter, verse_num = self._parse_osisid(osisid)
            records.append({
                "osisId":          osisid,
                "ref":             item["key"],
                "esv_text":        self._strip_html(html),
                "target_word":     english_word,
                "testament":       "NT" if book_code in _NT_BOOKS else "OT",
                "book_code":       book_code,
                "chapter":         chapter,
                "verse_num":       verse_num,
                "tagging_strongs": self._tagging_strongs(html, word_pat),
            })

        records.sort(key=lambda r: r["osisId"])
        return records

    # ── Public API — meaning-based term discovery ─────────────────────────

    def get_meaning_terms(self, english_word: str) -> dict:
        """Return STEP's curated list of terms whose MEANING relates to a word.

        STEP's Related-words panel (ORIGINAL_MEANING search). Fundamentally different
        from get_strongs_for_word(), which only finds codes where the ESV uses the
        literal English word: meanings=anger returns H2734 (charah, 'to be incensed'),
        which the ESV never renders as 'anger' but which is central to the concept.

        DISCOVERY ONLY — empty `may_source` in step.json.

        Returns: definitions (term dicts), strong_highlights (flat code list),
        total_verses.
        """
        d = self._get_json(self._route("search.masterSearch.meanings", text=english_word))
        return {
            "definitions":       d.get("definitions", []),
            "strong_highlights": d.get("strongHighlights", []),
            "total_verses":      d.get("total", 0),
        }

    # ── Public API — full extraction ───────────────────────────────────────

    def extract_word_data(self, strong: str) -> dict:
        """Return a complete structured data package.

        Keys: strong, vocab, verse_records, verse_count, testament, notes.
        """
        notes = []
        vocab = self.get_vocab_info(strong)

        if not vocab:
            notes.append(f"No vocab data found for {strong}")
            return {"strong": strong, "vocab": {}, "verse_records": [],
                    "verse_count": 0, "testament": None, "notes": notes}

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

        testaments = {r["testament"] for r in verse_records}
        if testaments == {"OT"}:
            testament = "OT"
        elif testaments == {"NT"}:
            testament = "NT"
        elif testaments:
            testament = "both"
        else:
            testament = None

        return {"strong": strong, "vocab": vocab, "verse_records": verse_records,
                "verse_count": vc, "testament": testament, "notes": notes}

    # ── Public API — term discovery (Phase 1) ─────────────────────────────

    def get_related_term_cluster(self, strong: str) -> dict:
        """Return the full term cluster for a Strong's number — all sub-glosses and
        semantically related terms as defined by STEP's ``relatedNos``.

        Read-only discovery: never touches the database, performs no extraction.

        Returns: primary_code, primary_vocab, sub_glosses, related_terms, all_codes.
        Each term entry: code, gloss, transliteration, script_form, vocab_count,
        verse_count, medium_def, is_sub_gloss, is_proper_noun, notes.
        """
        primary_vocab = self.get_vocab_info(strong)
        if not primary_vocab:
            return {"primary_code": strong, "primary_vocab": {}, "sub_glosses": [],
                    "related_terms": [], "all_codes": []}
        primary_code = primary_vocab["strong_number"]

        base_match = re.match(r"^([HG]\d+)[A-Za-z]+$", primary_code)
        numeric_base = base_match.group(1) if base_match else primary_code

        related_codes: set[str] = set()
        for rw in primary_vocab.get("related_words", []):
            code = rw.get("strong", "").strip()
            if code and code != primary_code:
                related_codes.add(code)

        # relatedNos often lists siblings, but probe explicitly to catch gaps.
        for suffix in self.subgloss_suffixes:
            candidate = f"{numeric_base}{suffix}"
            if candidate == primary_code or candidate in related_codes:
                continue
            try:
                d = self._get_json(self._route("module.getInfo", strong=candidate))
                vis = d.get("vocabInfos", [])
                if vis and vis[0].get("strongNumber") == candidate:
                    related_codes.add(candidate)
                else:
                    break   # no more sub-glosses in this family
            except Exception:
                break

        def _term_entry(code: str) -> dict:
            entry_notes: list[str] = []
            if self.exclude_strongs.match(code):
                return {}
            try:
                v = self.get_vocab_info(code)
            except Exception as exc:
                return {"code": code, "notes": [str(exc)]}
            if not v:
                return {"code": code, "notes": ["no vocab data"]}

            try:
                vc = self._search_range(code).get("total", 0)
            except Exception:
                vc = 0
                entry_notes.append("verse search failed")

            gloss = v.get("gloss", "")
            medium_def = v.get("medium_def", "")

            code_base_m = re.match(r"^([HG]\d+)[A-Za-z]+$", code)
            code_base = code_base_m.group(1) if code_base_m else code

            is_proper = bool(
                re.search(r"\bproper noun\b|\bpersonal name\b|\bplace name\b",
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
                "is_sub_gloss":    code_base == numeric_base,
                "is_proper_noun":  is_proper,
                "notes":           entry_notes,
            }

        sub_glosses: list[dict] = []
        related_terms: list[dict] = []
        for code in sorted(related_codes):
            entry = _term_entry(code)
            if not entry:
                continue
            (sub_glosses if entry.get("is_sub_gloss") else related_terms).append(entry)

        sub_glosses.sort(key=lambda e: e["code"])
        related_terms.sort(key=lambda e: -e.get("verse_count", 0))

        return {
            "primary_code":  primary_code,
            "primary_vocab": primary_vocab,
            "sub_glosses":   sub_glosses,
            "related_terms": related_terms,
            "all_codes": ([primary_code] + [e["code"] for e in sub_glosses]
                          + [e["code"] for e in related_terms]),
        }


def _checks() -> list[dict]:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))["checks"]
