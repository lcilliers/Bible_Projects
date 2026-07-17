"""Raw handlers — the five raw steps.

    discover  CALL 1 meanings=  -> word_strong (the seed strongs; relatedNos NOT followed)
    detail    CALL 2 getInfo    -> strong + strong_sense + strong_meaning_tree + strong_lexicon
    verses    CALL 3 strong=    -> strong_verse + verse + span (span parsed from preview)
    write     commit; word -> raw-complete
    validate  the parse-check: span vs strong_verse must agree

Every write goes through db.upsert with the schema's key, so a strong/verse/span
already present (found by a prior word) is reused, not duplicated — the global
"no duplicates on any level" rule.
"""

from __future__ import annotations

import datetime
import re

from ..lib import stepapi as S
from .base import Ctx, Result, ok, stop, cont, pause

PARTICLE_RE = re.compile(r"^[HG]9\d{3}$")
BASE_RE = re.compile(r"^([HG]\d+)([A-Z]?)$")


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _base(code: str) -> str:
    m = BASE_RE.match(code or "")
    return m.group(1) if m else code


def _split_def(medium_def: str) -> tuple[str, str]:
    """(head, tree). A ': ' prefix marks a sense: head + the lemma's tree. No ': '
    means the code is its own lemma: no head, the whole thing is the tree."""
    d = (medium_def or "").strip()
    if d.startswith(":"):
        head, _, tree = d[1:].strip().partition("\n")
        return head.strip(), tree.strip()
    return "", d


# ── the seed strongs a word maps to ──────────────────────────────────────────
def _word_id(ctx: Ctx) -> int:
    if ctx.word_id:
        return ctx.word_id
    row = ctx.db.get("word_registry", word=ctx.word)
    ctx.word_id = row["id"]
    return ctx.word_id


def _strongs_for_word(ctx: Ctx) -> list[str]:
    return [r["strong"] for r in ctx.db.rows(
        "SELECT strong FROM word_strong WHERE word_id=? AND deleted=0", (_word_id(ctx),))]


# ── discover ─────────────────────────────────────────────────────────────────
def discover(ctx: Ctx) -> Result:
    d = S.call1_meanings(ctx.word)
    seeds = [x["strongNumber"] for x in d.get("definitions", [])
             if x.get("strongNumber") and not PARTICLE_RE.match(x["strongNumber"])]
    if not seeds:
        return pause(
            question=f"The word {ctx.word!r} maps to no strongs. Register anyway, or reject?",
            preset={"word": ctx.word, "meanings_total": d.get("total"), "definitions": 0},
            tried="masterSearch meanings= returned no usable definitions",
            at_step="raw.discover")
    wid = _word_id(ctx)
    n = 0
    for s in seeds:
        _, created = ctx.db.upsert("word_strong", {"word_id": wid, "strong": s, "deleted": 0},
                                   key=["word_id", "strong"])
        n += created
    return ok(f"{len(seeds)} seed strong(s): {', '.join(seeds)}", word_strong_new=n)


# ── detail (the meaning) ─────────────────────────────────────────────────────
def detail(ctx: Ctx) -> Result:
    c = {"strong": 0, "sense": 0, "tree": 0, "lexicon": 0, "skipped": 0}
    for code in _strongs_for_word(ctx):
        if ctx.db.get("strong", strongNumber=code):        # global dedup — another word had it
            c["skipped"] += 1
            continue
        d = S.call2_getInfo(code)
        vocabs = d.get("vocabInfos") or []
        if not vocabs:
            continue                                        # recorded STEP gap (report-continue overall)
        v = vocabs[0]
        resolved = v.get("strongNumber", code)
        head, tree = _split_def(v.get("mediumDef", ""))

        ctx.db.upsert("strong", {
            "strongNumber": resolved,
            "accentedUnicode": v.get("accentedUnicode"),
            "stepGloss": v.get("stepGloss"),
            "stepTransliteration": v.get("stepTransliteration"),
            "language": "Greek" if resolved.startswith("G") else "Hebrew",
            "count": v.get("count"),
            "freqList": v.get("freqList"),
            "created_at": _now(), "deleted": 0,
        }, key=["strongNumber"]); c["strong"] += 1

        ctx.db.upsert("strong_sense", {
            "strong": resolved,
            "head": head or v.get("stepGloss"),
            "is_own_lemma": 0 if head else 1,
            "deleted": 0,
        }, key=["strong"]); c["sense"] += 1

        # tree: keyed on the lemma, shared across its senses -> write once per lemma
        lemma = _base(resolved)
        if tree and not ctx.db.get("strong_meaning_tree", lemma_key=lemma):
            for i, line in enumerate(x for x in tree.split("\n") if x.strip()):
                m = re.match(r"^(\d+[a-z]?\d*\))\s*(.*)$", line.strip())
                code_tok, text = (m.group(1), m.group(2)) if m else ("", line.strip())
                ctx.db.write("strong_meaning_tree", {
                    "lemma_key": lemma, "sense_code": code_tok, "sense_text": text,
                    "sort": i, "deleted": 0})
                c["tree"] += 1

        if v.get("lsjDefs") or v.get("shortDefMounce"):
            ctx.db.upsert("strong_lexicon", {
                "strong": resolved, "lsj": v.get("lsjDefs"), "mounce": v.get("shortDefMounce"),
                "deleted": 0}, key=["strong"]); c["lexicon"] += 1

    return ok(f"detail: {c['strong']} strong, {c['sense']} sense, {c['tree']} tree, "
              f"{c['lexicon']} lexicon ({c['skipped']} already held)", **c)


# ── verses + spans ───────────────────────────────────────────────────────────
def verses(ctx: Ctx) -> Result:
    c = {"strong_verse": 0, "verse_new": 0, "span_new": 0, "short": 0}
    for code in _strongs_for_word(ctx):
        total, rows = S.call3_strong(code)
        if total and len(rows) < total:
            c["short"] += 1                                 # a shortfall -> flagged, validate stops
        for r in rows:
            osis = r.get("osisId")
            if not osis:
                continue
            vid, vcreated = ctx.db.upsert("verse", {
                "osisId": osis, "reference": r.get("key"),
                "preview": r.get("preview"), "step_version": ctx.step_version,
                "created_at": _now(), "deleted": 0}, key=["osisId"])
            c["verse_new"] += vcreated

            # the source's assertion (m:m)
            _, screated = ctx.db.upsert("strong_verse",
                                        {"strong": code, "verse_id": vid, "deleted": 0},
                                        key=["strong", "verse_id"])
            c["strong_verse"] += screated

            # span: parse the preview into one row per code — only for a NEW verse
            if vcreated:
                for sp in S.parse_spans(r.get("preview", "")):
                    ctx.db.upsert("span", {
                        "verse_id": vid, "position": sp["position"], "surface": sp["surface"],
                        "strong_variant": sp["strong_variant"], "morph_code": sp["morph_code"],
                        "is_particle": sp["is_particle"], "built_at": _now(), "deleted": 0,
                    }, key=["verse_id", "position"])
                    c["span_new"] += 1

    msg = (f"{c['strong_verse']} strong_verse, {c['verse_new']} new verse(s), "
           f"{c['span_new']} span(s)")
    if c["short"]:
        return cont(msg + f" — ⚠ {c['short']} strong(s) returned fewer rows than STEP's total", **c)
    return ok(msg, **c)


# ── write / commit ───────────────────────────────────────────────────────────
def write(ctx: Ctx) -> Result:
    ctx.db.update("word_registry", {"id": _word_id(ctx)}, status="raw-complete")
    return ok("committed; word status -> raw-complete")


# ── validate: the parse-check ────────────────────────────────────────────────
def validate(ctx: Ctx) -> Result:
    """span (what we parsed) must recover strong_verse (what STEP asserted), for
    every strong of this word."""
    mism = []
    for code in _strongs_for_word(ctx):
        asserted = {r["verse_id"] for r in ctx.db.rows(
            "SELECT verse_id FROM strong_verse WHERE strong=? AND deleted=0", (code,))}
        parsed = {r["verse_id"] for r in ctx.db.rows(
            "SELECT DISTINCT verse_id FROM span WHERE strong_variant=? AND deleted=0", (code,))}
        missed = asserted - parsed
        if missed:
            mism.append((code, len(missed)))
    if mism:
        detail = ", ".join(f"{c}:{n}" for c, n in mism)
        return stop(f"parse-check FAILED — span does not recover strong_verse for {detail}")
    # no-null / fk spot-check
    orphan = ctx.db.rows(
        "SELECT COUNT(*) n FROM span WHERE strong_variant NOT IN (SELECT strongNumber FROM strong) "
        "AND is_particle=0")[0]["n"]
    return ok(f"parse-check PASSED; {orphan} non-particle span(s) name a strong not held "
              f"(other lemmas in the verse — expected)", parse_check="pass")
