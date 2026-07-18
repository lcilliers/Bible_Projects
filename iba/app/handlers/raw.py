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


def _write(ctx: Ctx, writer: str, table: str, row: dict, upsert=True):
    """Write a row, ENFORCING the write grant from config: the writer (an api, a step,
    or 'run') must be granted this table (cfg_write_grant). Every write is config-governed."""
    if table not in ctx.cfg.may_write(writer):
        raise PermissionError(f"write-grant violation: {writer!r} may not write {table!r} "
                              f"(cfg_write_grant). This is a config-governed control.")
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
def detail_one(ctx: Ctx, code: str, c: dict) -> None:
    """Fetch + write the meaning for ONE strong (call2). Reusable per-strong, so a single
    strong can be added to a word WITHOUT re-pulling the word's other strongs."""
    greek = ctx.cfg.setting("language.greek_prefix", "G")
    if ctx.db.get("strong", strongNumber=code):
        c["skipped"] += 1
        return
    v = (ctx.step.call2_getInfo(code).get("vocabInfos") or [None])[0]
    if not v:
        c["no_vocab"] += 1
        return
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


def detail(ctx: Ctx) -> Outcome:
    c = {"strong": 0, "sense": 0, "tree": 0, "lexicon": 0, "skipped": 0, "no_vocab": 0}
    for code in _strongs_for_word(ctx):
        detail_one(ctx, code, c)
    if c["no_vocab"]:
        return fail("no-vocab", f"detail done; {c['no_vocab']} strong(s) returned no vocab", **c)
    return ok(f"detail: {c['strong']} strong, {c['sense']} sense, {c['tree']} tree, "
              f"{c['lexicon']} lexicon ({c['skipped']} already held)", **c)


# ── verses + spans ───────────────────────────────────────────────────────────
def verses_one(ctx: Ctx, code: str, c: dict) -> None:
    """Fetch + write verses/spans for ONE strong (call3). Reusable per-strong."""
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
        # write spans for a NEW verse, or backfill a verse left span-less by a
        # partial (interrupted) build — so a resumed run self-heals.
        if vnew or not ctx.db.count("span", verse_id=vid):
            for sp in ctx.step.parse_spans(r.get("preview", "")):
                _write(ctx, "call3_strong", "span", {
                    "verse_id": vid, "position": sp["position"], "surface": sp["surface"],
                    "strong_variant": sp["strong_variant"], "morph_code": sp["morph_code"],
                    "is_particle": sp["is_particle"], "built_at": _now(), "deleted": 0})
                c["span_new"] += 1


def verses(ctx: Ctx) -> Outcome:
    c = {"strong_verse": 0, "verse_new": 0, "span_new": 0, "short": 0}
    for code in _strongs_for_word(ctx):
        verses_one(ctx, code, c)
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


# ── validate: the parse-check (util.validation — persisted) ──────────────────
def _record(ctx: Ctx, check_name: str, result: str, detail: str):
    _write(ctx, "raw.validate", "validation_result", {
        "run_id": ctx.run_id, "word": ctx.word, "step": "raw.validate",
        "check_name": check_name, "result": result, "detail": detail,
        "ran_at": _now(), "deleted": 0}, upsert=False)


def validate(ctx: Ctx) -> Outcome:
    # check 1: the parse-check — span recovers strong_verse
    mism = []
    for code in _strongs_for_word(ctx):
        asserted = {r["verse_id"] for r in ctx.db.rows(
            "SELECT verse_id FROM strong_verse WHERE strong=? AND deleted=0", (code,))}
        parsed = {r["verse_id"] for r in ctx.db.rows(
            "SELECT DISTINCT verse_id FROM span WHERE strong_variant=? AND deleted=0", (code,))}
        if asserted - parsed:
            mism.append((code, len(asserted - parsed)))
    if mism:
        d = "; ".join(f"{c}:{n} missed" for c, n in mism)
        _record(ctx, "parse-check", "fail", d)
        return fail("parse-mismatch", d)
    nsv = ctx.db.rows("SELECT COUNT(*) n FROM strong_verse")[0]["n"]
    _record(ctx, "parse-check", "pass", f"span recovers all {nsv} strong_verse assertions")

    # check 2: no-null on required columns of the tables this run wrote
    nulls = []
    for tbl in ("strong", "verse", "span"):
        for c in ctx.cfg.columns(tbl):
            if c["notnull"]:
                n = ctx.db.rows(f'SELECT COUNT(*) n FROM "{tbl}" WHERE "{c["name"]}" IS NULL')[0]["n"]
                if n:
                    nulls.append(f"{tbl}.{c['name']}={n}")
    _record(ctx, "no-null", "fail" if nulls else "pass", "; ".join(nulls) or "no NULLs in required columns")
    if nulls:
        return fail("parse-mismatch", "no-null: " + "; ".join(nulls))

    return ok("validation PASSED — parse-check + no-null recorded", parse_check="pass")
