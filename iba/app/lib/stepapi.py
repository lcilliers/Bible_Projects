"""stepapi.py — the three STEP calls. Governed by config.

Everything that is a CHOICE is read from the config store (cfg): the connection, the
routes, the cap, the particle pattern, the forward-walk bounds. The only things
hard-coded are FACTS that are not choices: the canonical book order (a property of the
canon) and the shape of STEP's interlinear HTML (a property of STEP). A fact is not a
rule; a rule is not a fact.

Each call takes an open Cfg so its reads are traced with the rest.
"""

from __future__ import annotations

import re

import requests

from .cfg import Cfg

# ── FACTS (not config) ───────────────────────────────────────────────────────
# The shape of STEP's HTML span. Not a choice — it is how STEP formats its output.
SPAN_RE = re.compile(r"<span[^>]*\bmorph='([^']*)'[^>]*\bstrong='([^']*)'[^>]*>([^<]*)</span>")
# Canonical OSIS book order. Not a choice — it is the order of the canon.
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
_OSIS_IDX = {b: i for i, b in enumerate(_OSIS_ORDER)}


class StepUnavailable(RuntimeError):
    pass


class Step:
    """A STEP session governed by a config handle. All choices come from cfg."""

    def __init__(self, cfg: Cfg):
        self.cfg = cfg
        self.base = cfg.connection("base_url").rstrip("/")
        self.version = cfg.connection("version")
        self.timeout = int(cfg.connection("timeout_seconds"))
        self.cap = int(cfg.setting("step.cap", 60))
        self.walk_start = cfg.setting("step.walk_start", "Gen.1.1")
        self.walk_end = cfg.setting("step.walk_end", "Rev.22.21")
        self.walk_max = int(cfg.setting("step.walk_max_iter", 400))
        self.particle_re = re.compile(cfg.setting("discovery.particle_pattern", r"^[HG]9\d{3}$"))

    def _get(self, path: str) -> dict:
        r = requests.get(f"{self.base}/{path.lstrip('/')}", timeout=self.timeout)
        r.raise_for_status()
        d = r.json()
        if "errorMessage" in d:
            raise RuntimeError(f"STEP error for {path!r}: {d['errorMessage']}")
        return d

    def _route(self, api: str, **kw) -> str:
        return self.cfg.route(api).format(version=self.version, **kw)

    def up(self) -> None:
        try:
            d = self._get(self._route("call2_getInfo", strong="H0430"))
        except requests.RequestException as e:
            raise StepUnavailable(f"STEP not reachable at {self.base} ({type(e).__name__}).") from e
        vocabs = d.get("vocabInfos") or []
        if not vocabs or not vocabs[0].get("stepGloss"):
            raise StepUnavailable(f"STEP up but no lexicon for the probe under {self.version!r}.")
        resolved = vocabs[0].get("strongNumber", "H0430")
        total = self._get(self._route("call3_strong", strong=resolved)).get("total", 0)
        if total < 1:
            raise StepUnavailable("STEP up but the module is NOT TAGGED.")

    def is_particle(self, code: str) -> bool:
        return bool(self.particle_re.match(code))

    def call1_meanings(self, word: str) -> dict:
        return self._get(self._route("call1_meanings", word=word))

    def call2_getInfo(self, strong: str) -> dict:
        return self._get(self._route("call2_getInfo", strong=strong))

    def call3_strong(self, strong: str) -> tuple[int, list[dict]]:
        route = self.cfg.route("call3_strong")
        first = self._get(route.format(version=self.version, strong=strong))
        total = first.get("total", 0)
        if total == 0:
            return 0, []
        if total <= self.cap:
            return total, first.get("results", [])
        seen: dict[str, dict] = {}
        start, end = self.walk_start, self.walk_end
        for _ in range(self.walk_max):
            d = self._get(route.format(version=self.version, strong=strong) + f"|reference={start}-{end}")
            rows = d.get("results", [])
            if not rows:
                break
            for it in rows:
                oid = it.get("osisId") or it.get("key", "")
                if oid and oid not in seen:
                    seen[oid] = it
            if d.get("total", 0) <= len(rows):
                break
            frontier = max(rows, key=lambda it: _canon_key(it.get("osisId") or it.get("key", "")))
            nxt = (frontier.get("osisId") or "").split("!")[0]
            if not nxt or nxt == start:
                break
            start = nxt
        return total, list(seen.values())

    def parse_spans(self, preview: str) -> list[dict]:
        """One row per CODE. A surface word maps to N codes; each is a row at its own
        running position; particles fall out as their own rows."""
        out, pos = [], 0
        for morph_list, strong_list, surface in SPAN_RE.findall(preview):
            strongs = strong_list.split()
            morphs = morph_list.split()
            for i, code in enumerate(strongs):
                out.append({
                    "position": pos, "surface": surface.strip(), "strong_variant": code,
                    "morph_code": morphs[i] if i < len(morphs) else None,
                    "is_particle": 1 if self.is_particle(code) else 0})
                pos += 1
        return out


def _canon_key(osis: str) -> tuple:
    parts = osis.split(".")
    book = _OSIS_IDX.get(parts[0], 999)
    ch = int(re.sub(r"\D.*", "", parts[1]) or 0) if len(parts) > 1 else 0
    vs = int(re.sub(r"\D.*", "", parts[2]) or 0) if len(parts) > 2 else 0
    return (book, ch, vs)


def strip_html(html: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()
