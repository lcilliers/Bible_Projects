"""stepapi.py — the three STEP calls. Governed by config, fully.

Everything the code reads is config: the connection, the routes, the cap, the
forward-walk bounds, the particle pattern, the canonical book order, and the shape of
STEP's interlinear HTML. Nothing is hard-coded — the earlier 'facts vs rules' line
(keeping book order and the HTML pattern in code) was my judgement call; the
researcher's principle is stronger and simpler: if the code reads it, it is config.
Both now live in config/reference.json -> cfg_book_order / cfg_setting.

Each call takes an open Cfg so its reads are traced with the rest.
"""

from __future__ import annotations

import re

import requests

from .cfg import Cfg


class StepUnavailable(RuntimeError):
    pass


def _canon_key(osis: str, book_idx: dict[str, int]) -> tuple:
    parts = osis.split(".")
    book = book_idx.get(parts[0], 999)
    ch = int(re.sub(r"\D.*", "", parts[1]) or 0) if len(parts) > 1 else 0
    vs = int(re.sub(r"\D.*", "", parts[2]) or 0) if len(parts) > 2 else 0
    return (book, ch, vs)


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
        # book order and the span-HTML pattern now come from config, not the code
        self.book_idx = cfg.book_order()
        self.span_re = re.compile(cfg.setting("step.span_html"))

    def _get(self, path: str) -> dict:
        r = requests.get(f"{self.base}/{path.lstrip('/')}", timeout=self.timeout)
        r.raise_for_status()
        d = r.json()
        if "errorMessage" in d:
            raise RuntimeError(f"STEP error for {path!r}: {d['errorMessage']}")
        return d

    def _route(self, api: str, **kw) -> str:
        return self.cfg.route(api).format(version=self.version, **kw)

    def up(self) -> dict:
        """A KNOWN-ANSWER preflight. Not 'did something answer 200' — 'did STEP return the
        EXPECTED data'. A stale/degraded/untagged server that still answers the port FAILS
        this and cannot report up. Returns the evidence it checked, so 'up' is a fact, not a
        claim; raises StepUnavailable with the specific reason on any miss."""
        # Fallback defaults corrected 2026-07-29 (were "" / 1 — vacuous no-ops that would have
        # silently defeated this whole probe if the cfg_setting rows were ever lost; the DB's
        # real, deliberately-set values are "God" / 1000, confirmed live during this session's
        # own `Start-Iba.ps1` run against H0430/2088 verses). Kept byte-identical to the DB so a
        # missing row degrades to the SAME check, not a weaker one.
        probe = self.cfg.setting("step.probe_strong", "H0430")
        want_gloss = self.cfg.setting("step.expect_gloss_contains", "God")
        min_verses = int(self.cfg.setting("step.expect_min_verses", 1000))

        # every network touch here is wrapped — a server that dies on the SECOND call is
        # 'not reachable', never an uncaught crash that init can't tell from 'up'.
        try:
            d = self._get(self._route("call2_getInfo", strong=probe))
            vocabs = d.get("vocabInfos") or []
            if not vocabs or not vocabs[0].get("stepGloss"):
                raise StepUnavailable(
                    f"STEP answered but returned no lexicon for {probe} under {self.version!r} "
                    f"— the module looks wrong or untagged.")
            gloss = vocabs[0].get("stepGloss", "")
            resolved = vocabs[0].get("strongNumber", probe)
            if want_gloss and want_gloss.lower() not in gloss.lower():
                raise StepUnavailable(
                    f"STEP answered but the known answer is WRONG: {probe} glossed "
                    f"{gloss!r}, expected to contain {want_gloss!r}. Stale or wrong module.")
            total = self._get(self._route("call3_strong", strong=resolved)).get("total", 0)
        except requests.RequestException as e:
            raise StepUnavailable(f"STEP not reachable at {self.base} ({type(e).__name__}).") from e

        if total < min_verses:
            raise StepUnavailable(
                f"STEP answered but returned only {total} verses for {resolved} "
                f"(expected >= {min_verses}) — the module is NOT TAGGED / not fully loaded.")
        return {"base": self.base, "version": self.version, "probe": probe,
                "resolved": resolved, "gloss": gloss, "verses": total}

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
            frontier = max(rows, key=lambda it: _canon_key(it.get("osisId") or it.get("key", ""), self.book_idx))
            nxt = (frontier.get("osisId") or "").split("!")[0]
            if not nxt or nxt == start:
                break
            start = nxt
        return total, list(seen.values())

    def parse_spans(self, preview: str) -> list[dict]:
        """One row per HTML <span> TAG, not per code (corrected 2026-07-25 — see
        migration/rebuild_span_combined_units.py). STEP tags a span with the FULL set
        of source-language codes it aligned to that one rendering unit — e.g.
        strong='G1722 G0054' on "purity" (the preposition ἐν fused with its noun for
        this one English word), or a Hebrew word's root plus its attached prefix/
        suffix particles. Confirmed against a live STEP re-fetch: this combination is
        in STEP's own source HTML, not introduced downstream — splitting it into one
        row per code (the old behaviour) misattributed the OTHER codes' surface text
        onto the code that has none of its own, and broke the particle off from the
        word it's semantically bound to. strong_variant and morph_code now keep the
        tag's full space-separated code/morph list together; position is the running
        TAG index (not code index). is_particle is 1 only if EVERY code in the tag is
        a particle (a tag mixing a content word with attached particles is not itself
        a pure particle)."""
        out, pos = [], 0
        for morph_list, strong_list, surface in self.span_re.findall(preview):
            codes = strong_list.split()
            out.append({
                "position": pos, "surface": surface.strip(), "strong_variant": strong_list.strip(),
                "morph_code": morph_list.strip(),
                "is_particle": 1 if codes and all(self.is_particle(c) for c in codes) else 0})
            pos += 1
        return out



def strip_html(html: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()
