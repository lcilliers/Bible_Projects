"""Raw handlers — interpreters, not deciders. Every rule is read from config:

  - the seed filter (particle pattern)          cfg discovery.particle_pattern (via Step)
  - whether to follow relatedNos                cfg discovery.follow_related
  - what to do on a zero-strongs word           cfg raw.zero_strongs_action
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

from .base import Ctx, Outcome, ok, fail
from ..lib.stepapi import StepUnavailable, preview_to_text

# Fallback only: the real value is `cfg_setting raw.strong_base_pattern` (module `raw`).
_BASE_RE_FALLBACK = r"^([HG]\d+)([A-Z]?)$"


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _base(code: str, base_pattern: str = _BASE_RE_FALLBACK) -> str:
    m = re.match(base_pattern, code or "")
    return m.group(1) if m else code


def _write(ctx: Ctx, writer: str, table: str, row: dict, upsert=True):
    """Write a row, ENFORCING the write grant from config: the writer (an api, a step,
    or 'run') must be granted this table (cfg_write_grant). Every write is config-governed."""
    if table not in ctx.cfg.may_write(writer):
        raise PermissionError(f"write-grant violation: {writer!r} may not write {table!r} "
                              f"(cfg_write_grant). This is a config-governed control.")
    return ctx.db.upsert(table, row) if upsert else (ctx.db.write(table, row), True)


def _split_def(ctx: Ctx, medium_def: str) -> tuple[str, str]:
    marker = ctx.cfg.required_setting("meaning.head_marker")
# STEP's mediumDef sometimes separates tree lines with '<br>' / '<BR>' instead of a newline:
# normalised (case-insensitive) to \n first, so the head/tree split works.
    d = re.sub(r"<br\s*/?>", "\n", (medium_def or ""), flags=re.IGNORECASE).strip()
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
    # relatedNos expansion is not built: following it fails loudly rather than silently doing nothing
    if ctx.cfg.setting("discovery.follow_related", False):
        return fail("follow-related-not-built",
                   "discovery.follow_related is true, but relatedNos expansion was never "
                   "implemented — set it back to false, or implement the expansion before relying "
                   "on it (see handlers/raw.py:discover)")
    if not seeds:
        # word registration is researcher-instructed: the zero-strongs case is config-driven
        # (raw.zero_strongs_action, default 'reject')
        action = ctx.cfg.required_setting("raw.zero_strongs_action")
        if action == "reject":
            return fail("zero-strongs",
                       f"{ctx.word!r} maps to no strongs (raw.zero_strongs_action=reject)")
        return ok(f"{ctx.word!r} maps to no strongs — proceeding per "
                 f"raw.zero_strongs_action=proceed", word_strong_new=0)
    wid = _word_id(ctx)
    n = sum(_write(ctx, "call1_meanings", "word_strong",
                   {"word_id": wid, "strong": s, "deleted": 0})[1] for s in seeds)
    return ok(f"{len(seeds)} seed strong(s): {', '.join(seeds)}", word_strong_new=n)


# ── detail (the meaning) ─────────────────────────────────────────────────────
def write_tree_rows(ctx: Ctx, lemma: str, strong_variant: str, tree: str, c: dict) -> None:
    """Write strong_meaning_tree rows for ONE exact code (`strong_variant`), separately from
    detail_one, so a sibling's own tree text can be re-fetched and written on its own."""
    for i, line in enumerate(x for x in tree.split("\n") if x.strip()):
        m = re.match(r"^(\d+[a-z]?\d*\))\s*(.*)$", line.strip())
        sc, txt = (m.group(1), m.group(2)) if m else ("", line.strip())
        _write(ctx, "call2_getInfo", "strong_meaning_tree",
               {"lemma_key": lemma, "sense_code": sc, "sense_text": txt, "sort": i,
                "strong_variant": strong_variant, "deleted": 0}, upsert=False)
        c["tree"] += 1


def detail_one(ctx: Ctx, code: str, c: dict, origin: str = "word") -> None:
    """Fetch + write the meaning for ONE strong (call2), so a strong can be added to a word without
    re-pulling the word's other strongs.

    The tree write is keyed on the exact code (lemma_key, strong_variant): a sibling skips only if
    its own row exists, so homonym siblings (e.g. H3581A/H3581B) each keep their own tree text.

    `origin` ('word' | 'backfill') is stamped on the `strong` row at creation: 'word' from
    `detail()`, 'backfill' from `backfill_meaning_for()`. On an existing row, 'backfill' is upgraded
    to 'word' when a word claims the code; never the reverse."""
    greek = ctx.cfg.required_setting("language.greek_prefix")
    existing = ctx.db.get("strong", strongNumber=code)
    if existing:
        # _write(..., upsert=True) only dedups (it never updates an existing key), so the upgrade is a
        # direct UPDATE with the same grant check
        if origin == "word" and existing["origin"] == "backfill":
            if "strong" not in ctx.cfg.may_write("call2_getInfo"):
                raise PermissionError(
                    "write-grant violation: 'call2_getInfo' may not write 'strong'")
            ctx.db.update("strong", {"strongNumber": code}, origin="word")
            c["origin_upgraded"] = c.get("origin_upgraded", 0) + 1
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
        "count": v.get("count"), "freqList": v.get("freqList"), "origin": origin,
        "created_at": _now(), "deleted": 0}); c["strong"] += 1
    _write(ctx, "call2_getInfo", "strong_sense", {
        "strong": resolved, "head": head or v.get("stepGloss"),
        "is_own_lemma": 0 if head else 1, "deleted": 0}); c["sense"] += 1
    lemma = _base(resolved, ctx.cfg.setting("raw.strong_base_pattern", _BASE_RE_FALLBACK))
    if tree and not ctx.db.get("strong_meaning_tree", lemma_key=lemma, strong_variant=resolved):
        write_tree_rows(ctx, lemma, resolved, tree, c)
    if v.get("lsjDefs") or v.get("shortDefMounce"):
        _write(ctx, "call2_getInfo", "strong_lexicon", {
            "strong": resolved, "lsj": v.get("lsjDefs"),
            "mounce": v.get("shortDefMounce"), "deleted": 0}); c["lexicon"] += 1


def detail(ctx: Ctx) -> Outcome:
    c = {"strong": 0, "sense": 0, "tree": 0, "lexicon": 0, "skipped": 0, "no_vocab": 0}
    for code in _strongs_for_word(ctx):
        detail_one(ctx, code, c, origin="word")
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
            "text": preview_to_text(r.get("preview")),
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


# ── related (scoped to THIS word's own strongs) ─────────────────────────────────────────────────
# The new-word chain's strong_related fetch: `lexicon.fetch_related_for` with the same writer grant
# ('lexicon.related' -> 'strong_related'), `clear_first=False` (append, never wiping another word's
# codes). Not `lexicon.related` itself, which makes one STEP call per strong row in the whole DB.
def related(ctx: Ctx) -> Outcome:
    codes = _strongs_for_word(ctx)
    # "0 strong_related rows" = "needs fetching", as in lexicon.validate (a code with no relatedNos
    # looks the same as never fetched)
    missing = [c for c in codes if ctx.db.count("strong_related", strong=c, deleted=0) == 0]
    if not missing:
        return ok(f"0 of {len(codes)} strong(s) needed a related-terms fetch — already covered")
    try:
        ctx.step.up()
    except StepUnavailable as e:
        return fail("unreachable", str(e))
    from .lexicon import fetch_related_for
    counts = fetch_related_for(ctx, missing, clear_first=False)
    return ok(f"related: {counts['strong_related']} row(s) across {counts['strongs_checked']} "
             f"strong(s) newly fetched ({counts['none_related']} with none, "
             f"{counts['errors']} fetch error(s))", **counts)


# ── lexical (verse_lexical, scoped to THIS word's own verses -- the chain's closing step) ────────
# Runs last in the chain (after lexicon.parse + raw.write + raw.validate), so it reads the fresh
# parsed layer and the validated span set. `lib.lexical.build_for_verse_ids` is identity-stable:
# unchanged verses write nothing, changed ones are corrected in place.
def lexical(ctx: Ctx) -> Outcome:
    if "verse_lexical" not in ctx.cfg.may_write("lexical.build"):
        raise PermissionError("write-grant violation: 'lexical.build' may not write 'verse_lexical'")

    codes = _strongs_for_word(ctx)
    if not codes:
        return ok("0 verse(s) to build — word has no strongs")
    verse_ids = [r["verse_id"] for r in ctx.db.rows(
        "SELECT DISTINCT sv.verse_id FROM strong_verse sv WHERE sv.strong IN ({}) "
        "AND sv.deleted=0".format(",".join("?" * len(codes))), codes)]
    if not verse_ids:
        return ok("0 verse(s) to build — word has no strong_verse rows yet")

    # Layer 1 has no STEP dependency (#1706)
    from ..lib import lexical as lexlib
    try:
        totals = lexlib.build_for_verse_ids(ctx.db.conn, verse_ids)
    except lexlib.NotReady as e:
        return fail("lexical-not-ready", str(e), unready_codes=e.codes)
    ctx.db.conn.commit()
    removed_note = (f", {totals['removed_with_live_notes']} with live notes now dangling"
                    if totals["removed_with_live_notes"] else "")
    return ok(f"{totals['verses']} verse(s), {totals['spans']} span(s), {totals['codes']} "
             f"code(s) resolved ({totals['inserted']} inserted, {totals['updated']} updated, "
             f"{totals['unchanged']} unchanged, {totals['removed']} removed{removed_note})",
             **totals)


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
    # check 1: the parse-check -- span recovers strong_verse. span.strong_variant can hold more than
    # one code (a combined unit in STEP's HTML, e.g. "G1722 G0054"): a code counts as recovered if it
    # is one whitespace-delimited token in some span row for that verse.
    code_verses: dict[str, set] = {}
    for r in ctx.db.rows("SELECT verse_id, strong_variant FROM span WHERE deleted=0"):
        for tok in (r["strong_variant"] or "").split():
            code_verses.setdefault(tok, set()).add(r["verse_id"])

    mism = []
    for code in _strongs_for_word(ctx):
        asserted = {r["verse_id"] for r in ctx.db.rows(
            "SELECT verse_id FROM strong_verse WHERE strong=? AND deleted=0", (code,))}
        parsed = code_verses.get(code, set())
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


# ── reconcile (cluster-assign every one of the word's own codes, ordinal 7) ───────────────────
# Runs last in the new-word chain (after raw.validate): strongreconcile.reconcile() once per this
# word's own codes.
def reconcile(ctx: Ctx) -> Outcome:
    from ..lib import strongreconcile
    tallies: dict[str, int] = {}
    unclassified: list[str] = []
    for code in _strongs_for_word(ctx):
        r = strongreconcile.reconcile(ctx, code)
        tallies[r["status"]] = tallies.get(r["status"], 0) + 1
        if r["status"] == "unclassified":
            unclassified.append(code)
    parts = ", ".join(f"{k}: {v}" for k, v in sorted(tallies.items()))
    msg = f"{len(_strongs_for_word(ctx))} strong(s) cluster-reconciled — {parts}"
    # strong-cluster sync must be guaranteed (#1606): reconcile() itself never escalates (it also runs
    # inside DB-wide sweeps), so this step names the condition when codes come back unclassified and
    # cfg_on_fail decides the path
    if unclassified:
        return fail("unclassified", msg + f" — {len(unclassified)} strong(s) got no cluster "
                    f"assignment at all (no HIGH-confidence precedent match): "
                    f"{', '.join(unclassified)}", **tallies, unclassified_codes=unclassified)
    return ok(msg, **tallies)


# ── backfill (book/range; meaning ONLY, no verses) ────────────────────────────────────────────
# A "(not yet registered)" span is often a supporting term that matters for reading a passage. The
# backfill pulls meaning progressively, per passage, and persists it (no full-Bible pull, no
# re-hitting STEP on every report). A `strong` row with no `strong_verse` row means "meaning pulled,
# verses not". Reuses detail_one().
def _verse_range_filter(osis_id: str, book: str, lo_ch: int, hi_ch: int,
                        verse_lo: int | None, verse_hi: int | None) -> bool:
    parts = (osis_id or "").split(".")
    if len(parts) != 3 or parts[0] != book or not parts[1].isdigit() or not parts[2].isdigit():
        return False
    ch, vn = int(parts[1]), int(parts[2])
    if not (lo_ch <= ch <= hi_ch):
        return False
    if verse_lo is not None and not (verse_lo <= vn <= verse_hi):
        return False
    return True


def backfill_meaning_for(ctx: Ctx, book: str, lo_ch: int, hi_ch: int,
                         verse_lo: int | None, verse_hi: int | None) -> dict:
    """The core of raw.backfill_meaning, shared with report.verse_span_meaning's
    `report.auto_backfill_before_render`. Raises StepUnavailable (uncaught) if STEP is down and there
    is something to backfill; callers decide how to report it."""
    rows = ctx.db.rows(
        "SELECT v.osisId AS osis_id, sp.strong_variant AS sv FROM span sp "
        "JOIN verse v ON v.id = sp.verse_id "
        "WHERE v.osisId LIKE ? AND sp.deleted=0 AND v.deleted=0", (f"{book}.%",))
    codes: set[str] = set()
    for r in rows:
        if not _verse_range_filter(r["osis_id"], book, lo_ch, hi_ch, verse_lo, verse_hi):
            continue
        for code in (r["sv"] or "").split():
            codes.add(code)

    missing = sorted(c for c in codes if not ctx.db.get("strong", strongNumber=c))
    if not missing:
        return {"distinct_codes": len(codes), "missing_before": 0,
                "strong": 0, "sense": 0, "tree": 0, "lexicon": 0, "skipped": 0, "no_vocab": 0,
                "strong_meaning_parsed": 0, "strong_lsj_parsed": 0, "strong_mounce_parsed": 0,
                "strong_related": 0, "strongs_checked": 0, "none_related": 0, "errors": 0,
                "reconcile_tallies": {}}

    ctx.step.up()  # StepUnavailable propagates — caller decides how to report it

    c = {"strong": 0, "sense": 0, "tree": 0, "lexicon": 0, "skipped": 0, "no_vocab": 0}
    for code in missing:
        detail_one(ctx, code, c, origin="backfill")

    # keep the downstream layers in sync as part of this method; imported here to avoid a clash with
    # the local `c["lexicon"]` counter
    from .lexicon import fetch_related_for, rebuild_parsed_tables
    parsed_counts = rebuild_parsed_tables(ctx)
    related_counts = fetch_related_for(ctx, missing, clear_first=False)

    # cluster-assign the newly backfilled codes: a code created here passes through no later
    # per-word chain, so reconcile() runs inline
    from ..lib import strongreconcile
    reconcile_tallies: dict[str, int] = {}
    for code in missing:
        r = strongreconcile.reconcile(ctx, code)
        reconcile_tallies[r["status"]] = reconcile_tallies.get(r["status"], 0) + 1

    return {"distinct_codes": len(codes), "missing_before": len(missing), **c,
           **parsed_counts, **related_counts, "reconcile_tallies": reconcile_tallies}


def backfill_meaning(ctx: Ctx) -> Outcome:
    book = ctx.params["Book"]
    range_spec = ctx.params.get("Range")  # "chapter:verse-verse", e.g. "1:1-7"; omit for whole book
    if range_spec:
        ch, sep, vspec = range_spec.partition(":")
        if not sep:
            return fail("invalid-range", f"-Range needs chapter:verse[-verse], e.g. 1:1-7 (got {range_spec!r})")
        vlo_s, _, vhi_s = vspec.partition("-")
        lo_ch = hi_ch = int(ch)
        verse_lo, verse_hi = int(vlo_s), int(vhi_s or vlo_s)
    else:
        lo_ch, hi_ch, verse_lo, verse_hi = 1, 999, None, None

    try:
        result = backfill_meaning_for(ctx, book, lo_ch, hi_ch, verse_lo, verse_hi)
    except Exception as e:
        return fail("unreachable", f"STEP is not reachable — cannot backfill meaning: {e}")

    if not result["missing_before"]:
        return ok(f"{book} {range_spec or '(whole book)'}: every span's strong already has a "
                 f"strong row — nothing to backfill", checked=result["distinct_codes"], missing=0)

    tallies = ", ".join(f"{k}: {v}" for k, v in sorted(result["reconcile_tallies"].items()))
    msg = (f"{book} {range_spec or '(whole book)'}: {result['distinct_codes']} distinct strong(s) "
          f"referenced, {result['missing_before']} were unregistered — pulled meaning (not "
          f"verses) for {result['strong']} ({result['no_vocab']} returned no vocab from STEP); "
          f"parsed layer rebuilt ({result['strong_meaning_parsed']} meaning / "
          f"{result['strong_lsj_parsed']} lsj / {result['strong_mounce_parsed']} mounce rows); "
          f"relatedNos fetched for the {result['missing_before']} newly-registered strong(s) "
          f"({result['strong_related']} related row(s), {result['errors']} fetch error(s)); "
          f"cluster-reconciled ({tallies or 'nothing to reconcile'}).")
    # same guarantee as strong.reconcile (#1606): this is the only point a backfill-discovered code
    # passes through
    unclassified_n = result["reconcile_tallies"].get("unclassified", 0)
    if unclassified_n:
        return fail("unclassified", msg + f" — {unclassified_n} strong(s) got no cluster "
                    f"assignment at all, needs classification before this book's data is trusted "
                    f"complete.", **result)
    return ok(msg, **result)
