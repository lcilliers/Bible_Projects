"""strongreconcile.py — the single-strong reconciler, `reconcile(ctx, code)`: one code in, a full
classify -> exception-check -> promote-or-leave sequence out. Every strong-creation path (`new-word`,
`raw.backfill_meaning`'s auto-backfill, a DB-wide sweep) goes through it.

Never escalates itself: on a named exception shape it flags the code and does not promote, leaving
it as it was; `cluster.validate` (handlers/cluster.py) surfaces it on its own run. The promotion
cascade reuses `raw.py:verses_one()` and `lib.lexical.build_for_verse_ids()` unchanged. Meaning/parse
tables need no action on promotion.
"""

from __future__ import annotations

import datetime

from . import clusterassign
from .versespanmeaningreport import _BASE_RE_FALLBACK, _base, sibling_variant_codes
from .stepapi import StepUnavailable


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _may(ctx, writer: str, table: str) -> None:
    if table not in ctx.cfg.may_write(writer):
        raise PermissionError(f"write-grant violation: {writer!r} may not write {table!r}")


_WORD_OPTIONAL_DEFAULT = ["T2", "T3"]


def _word_optional_clusters(ctx) -> set[str]:
    """Cluster codes exempt from the 'needs a word_registry link' rule: `word_strong` exists to
    generate the verse, not to own every strong in it. T2 never promotes; T3 is not word-specific by
    nature. Only an M-cluster/FLAG classification needs a word."""
    return set(ctx.cfg.setting("cluster.assign.word_optional_clusters", _WORD_OPTIONAL_DEFAULT))


def _cluster_codes(ctx, code: str) -> set[str]:
    return {r["cluster_code"] for r in ctx.db.rows(
        "SELECT cluster_code FROM cluster_strong WHERE strong=? AND deleted=0", (code,))}


def _classify(ctx, code: str, step_gloss: str | None) -> set[str]:
    """Existing classification if any, else attempt the mechanical HIGH-precedent match and
    write it (`source='auto-precedent'`) if one resolves. Never writes a second row for the
    same (strong, cluster_code) pair — checked, not assumed."""
    existing = _cluster_codes(ctx, code)
    if existing:
        return existing
    rules = clusterassign.load_rules(ctx.cfg)
    match = clusterassign.match_precedent(ctx.db.conn, rules, step_gloss)
    if not match:
        return set()
    cluster_code, rationale = match
    _may(ctx, "cluster.assign", "cluster_strong")
    if not ctx.db.get("cluster_strong", strong=code, cluster_code=cluster_code, deleted=0):
        ctx.db.write("cluster_strong", {
            "strong": code, "cluster_code": cluster_code, "source": "auto-precedent",
            "created_at": _now(), "deleted": 0})
    return {cluster_code}


def _sibling_conflict(ctx, code: str) -> bool:
    """Q2.4.1 exception 2: a `backfill` code whose base-lemma sibling is already `word`-origin
    and/or already carries a cluster assignment. Sibling = same base lemma, per the codebase's own
    existing `sibling_variant_codes()` convention (H1234A/H1234B-style exact-variant siblings) —
    not `strong_related` (STEP's broader semantic-relation table), which is a different axis."""
    base = _base(code, _BASE_RE_FALLBACK)
    for sib in sibling_variant_codes(ctx.db.conn, base, exclude=code):
        sib_row = ctx.db.get("strong", strongNumber=sib)
        if sib_row and sib_row["origin"] == "word":
            return True
        if ctx.db.count("cluster_strong", strong=sib, deleted=0) > 0:
            return True
    return False


def _promote(ctx, code: str) -> None:
    """The Q2.4.2 cascade: a real STEP verse fetch FIRST (never derived from existing spans), the
    origin flip only AFTER that succeeds (so a STEP failure leaves the code untouched, not
    half-promoted), then extend verse_lexical to whatever verses the fetch surfaced."""
    from ..handlers import raw as raw_mod  # deferred: raw.py imports this module's caller (lexical.py)
    from . import lexical as lexlib

    c = {"strong_verse": 0, "verse_new": 0, "span_new": 0, "short": 0}
    raw_mod.verses_one(ctx, code, c)  # writer 'call3_strong' — already granted verse/span/strong_verse

    _may(ctx, "strong.reconcile", "strong")
    ctx.db.update("strong", {"strongNumber": code}, origin="word")

    verse_ids = [r["verse_id"] for r in ctx.db.rows(
        "SELECT DISTINCT verse_id FROM strong_verse WHERE strong=? AND deleted=0", (code,))]
    if verse_ids:
        _may(ctx, "lexical.build", "verse_lexical")
        # NotReady propagates uncaught on purpose: the code was just cluster-classified, so it should never
        # fire here, and if it does that is a real bug
        lexlib.build_for_verse_ids(ctx.db.conn, verse_ids)
    ctx.db.conn.commit()


def reconcile(ctx, code: str) -> dict:
    """-> {"strong", "status", "cluster_code", "exception"}. `status` is one of:
    no-strong-row | unclassified | t2-confirmed | already-active | promoted | exception |
    step-unavailable. Pure — never escalates; see module docstring."""
    result = {"strong": code, "status": None, "cluster_code": None, "exception": None}

    strong_row = ctx.db.get("strong", strongNumber=code)
    if not strong_row:
        result["status"] = "no-strong-row"
        return result

    cluster_codes = _classify(ctx, code, strong_row["stepGloss"])
    result["cluster_code"] = ",".join(sorted(cluster_codes)) or None
    non_t2 = cluster_codes - {"T2"}

    if not cluster_codes:
        result["status"] = "unclassified"
        return result
    if not non_t2:
        result["status"] = "t2-confirmed"
        return result

    # Q2.4.1 exception 1: an assignment beyond the word-optional set (T2/T3, _word_optional_clusters)
    # with no word_registry link; T3-only codes are exempt
    needs_word = bool(cluster_codes - {"T2"} - _word_optional_clusters(ctx))
    word_linked = ctx.db.count("word_strong", strong=code, deleted=0) > 0
    if needs_word and not word_linked:
        result["status"] = "exception"
        result["exception"] = "no-word"
        return result

    if strong_row["origin"] == "backfill" and _sibling_conflict(ctx, code):
        result["status"] = "exception"
        result["exception"] = "sibling-conflict"
        return result

    if strong_row["origin"] == "word":
        result["status"] = "already-active"
        return result

    try:
        _promote(ctx, code)
    except StepUnavailable:
        result["status"] = "step-unavailable"
        return result
    result["status"] = "promoted"
    return result
