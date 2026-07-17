"""Raw handlers — interpreters, not deciders. Every rule is read from config:

  - the seed filter (particle pattern)          cfg discovery.particle_pattern (via Step)
  - whether to follow relatedNos                cfg discovery.follow_related
  - the meaning head/tree split marker          cfg meaning.head_marker
  - the Greek prefix                            cfg language.greek_prefix
  - which API may write which table (may_source) cfg may_source — ENFORCED at write
  - the dedup key on every table                cfg unique_key (via Db.upsert)
  - the fail conditions (zero/shortfall/...)     named here, resolved to a path by cfg_on_fail
  - the status a step sets                       cfg_status_flow

The handler contains no path decisions, no dedup keys, no filter constants.
"""

from __future__ import annotations

import datetime
import re

from .base import Ctx, Outcome, ok, fail, escalate

BASE_RE = re.compile(r"^([HG]\d+)([A-Z]?)$")


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _base(code: str) -> str:
    m = BASE_RE.match(code or "")
    return m.group(1) if m else code


def _write(ctx: Ctx, api: str, table: str, row: dict, upsert=True):
    """Write a row, ENFORCING may_source from config: the api must be permitted to
    source this table. This is the control that was documented and never enforced."""
    if table not in ctx.cfg.may_source(api):
        raise PermissionError(f"may_source violation: api {api!r} may not write {table!r} "
                              f"(cfg_api_source). This is a config-governed control.")
    return ctx.db.upsert(table, row) if upsert else (ctx.db.write(table, row), True)


def _split_def(ctx: Ctx, medium_def: str) -> tuple[str, str]:
    marker = ctx.cfg.setting("meaning.head_marker", ": ")
    d = (medium_def or "").strip()
    if d.startswith(marker.strip()):
        head, _, tree = d[len(marker.strip()):].strip().partition("\n")
        return head.strip(), tree.strip()
    return "", d


def _word_id(ctx: Ctx) -> int:
    if ctx.word_id:
        return ctx.word_id
    ctx.word_id = ctx.db.get("word_registry", word=ctx.word)["id"]
    return ctx.word_id


def _strongs_for_word(ctx: Ctx) -> list[str]:
    return [r["strong"] for r in ctx.db.rows(
        "SELECT strong FROM word_strong WHERE word_id=? AND deleted=0", (_word_id(ctx),))]


# ── discover ─────────────────────────────────────────────────────────────────
def discover(ctx: Ctx) -> Outcome:
    d = ctx.step.call1_meanings(ctx.word)
    seeds = [x["strongNumber"] for x in d.get("definitions", [])
             if x.get("strongNumber") and not ctx.step.is_particle(x["strongNumber"])]
    # relatedNos: only if config says to follow it (it says no)
    if ctx.cfg.setting("discovery.follow_related", False):
        pass  # would expand here; config disables it
    if not seeds:
        return escalate("zero-strongs",
                        question=f"{ctx.word!r} maps to no strongs. Register anyway, or reject?",
                        preset={"word": ctx.word, "meanings_total": d.get("total")},
                        tried="masterSearch meanings= returned no usable definitions")
    wid = _word_id(ctx)
    n = sum(_write(ctx, "call1_meanings", "word_strong",
                   {"word_id": wid, "strong": s, "deleted": 0})[1] for s in seeds)
    return ok(f"{len(seeds)} seed strong(s): {', '.join(seeds)}", word_strong_new=n)


# ── detail (the meaning) ─────────────────────────────────────────────────────
def detail(ctx: Ctx) -> Outcome:
    greek = ctx.cfg.setting("language.greek_prefix", "G")
    c = {"strong": 0, "sense": 0, "tree": 0, "lexicon": 0, "skipped": 0, "no_vocab": 0}
    for code in _strongs_for_word(ctx):
        if ctx.db.get("strong", strongNumber=code):
            c["skipped"] += 1
            continue
        v = (ctx.step.call2_getInfo(code).get("vocabInfos") or [None])[0]
        if not v:
            c["no_vocab"] += 1
            continue
        resolved = v.get("strongNumber", code)
        head, tree = _split_def(ctx, v.get("mediumDef", ""))

        _write(ctx, "call2_getInfo", "strong", {
            "strongNumber": resolved, "accentedUnicode": v.get("accentedUnicode"),
            "stepGloss": v.get("stepGloss"), "stepTransliteration": v.get("stepTransliteration"),
            "language": "Greek" if resolved.startswith(greek) else "Hebrew",
            "count": v.get("count"), "freqList": v.get("freqList"),
            "created_at": _now(), "deleted": 0}); c["strong"] += 1

        _write(ctx, "call2_getInfo", "strong_sense", {
            "strong": resolved, "head": head or v.get("stepGloss"),
            "is_own_lemma": 0 if head else 1, "deleted": 0}); c["sense"] += 1

        lemma = _base(resolved)
        if tree and not ctx.db.get("strong_meaning_tree", lemma_key=lemma):
            for i, line in enumerate(x for x in tree.split("\n") if x.strip()):
                m = re.match(r"^(\d+[a-z]?\d*\))\s*(.*)$", line.strip())
                sc, txt = (m.group(1), m.group(2)) if m else ("", line.strip())
                _write(ctx, "call2_getInfo", "strong_meaning_tree",
                       {"lemma_key": lemma, "sense_code": sc, "sense_text": txt,
                        "sort": i, "deleted": 0}, upsert=False); c["tree"] += 1

        if v.get("lsjDefs") or v.get("shortDefMounce"):
            _write(ctx, "call2_getInfo", "strong_lexicon", {
                "strong": resolved, "lsj": v.get("lsjDefs"),
                "mounce": v.get("shortDefMounce"), "deleted": 0}); c["lexicon"] += 1

    if c["no_vocab"]:
        return fail("no-vocab", f"detail done; {c['no_vocab']} strong(s) returned no vocab", **c)
    return ok(f"detail: {c['strong']} strong, {c['sense']} sense, {c['tree']} tree, "
              f"{c['lexicon']} lexicon ({c['skipped']} already held)", **c)


# ── verses + spans ───────────────────────────────────────────────────────────
def verses(ctx: Ctx) -> Outcome:
    c = {"strong_verse": 0, "verse_new": 0, "span_new": 0, "short": 0}
    for code in _strongs_for_word(ctx):
        total, rows = ctx.step.call3_strong(code)
        if total and len(rows) < total:
            c["short"] += 1
        for r in rows:
            osis = r.get("osisId")
            if not osis:
                continue
            vid, vnew = _write(ctx, "call3_strong", "verse", {
                "osisId": osis, "reference": r.get("key"), "preview": r.get("preview"),
                "step_version": ctx.step.version, "created_at": _now(), "deleted": 0})
            c["verse_new"] += vnew
            c["strong_verse"] += _write(ctx, "call3_strong", "strong_verse",
                                        {"strong": code, "verse_id": vid, "deleted": 0})[1]
            if vnew:
                for sp in ctx.step.parse_spans(r.get("preview", "")):
                    _write(ctx, "call3_strong", "span", {
                        "verse_id": vid, "position": sp["position"], "surface": sp["surface"],
                        "strong_variant": sp["strong_variant"], "morph_code": sp["morph_code"],
                        "is_particle": sp["is_particle"], "built_at": _now(), "deleted": 0})
                    c["span_new"] += 1
    msg = f"{c['strong_verse']} strong_verse, {c['verse_new']} new verse(s), {c['span_new']} span(s)"
    if c["short"]:
        return fail("shortfall", msg + f" — {c['short']} strong(s) short of STEP's total", **c)
    return ok(msg, **c)


# ── write ────────────────────────────────────────────────────────────────────
def write(ctx: Ctx) -> Outcome:
    for r in ctx.cfg.conn.execute(
            "SELECT status FROM cfg_status_flow WHERE entity='word' AND set_by LIKE '%raw.write%'"):
        ctx.db.update("word_registry", {"id": _word_id(ctx)}, status=r["status"])
        return ok(f"committed; word status -> {r['status']}")
    return ok("committed")


# ── validate: the parse-check ────────────────────────────────────────────────
def validate(ctx: Ctx) -> Outcome:
    mism = []
    for code in _strongs_for_word(ctx):
        asserted = {r["verse_id"] for r in ctx.db.rows(
            "SELECT verse_id FROM strong_verse WHERE strong=? AND deleted=0", (code,))}
        parsed = {r["verse_id"] for r in ctx.db.rows(
            "SELECT DISTINCT verse_id FROM span WHERE strong_variant=? AND deleted=0", (code,))}
        if asserted - parsed:
            mism.append((code, len(asserted - parsed)))
    if mism:
        return fail("parse-mismatch",
                    "; ".join(f"{c}:{n} missed" for c, n in mism))
    return ok("parse-check PASSED; span recovers strong_verse for every strong", parse_check="pass")
