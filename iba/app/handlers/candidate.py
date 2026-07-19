"""Candidate-characteristic handlers (span L4b) — interpreters, config-governed.

Two steps:
  seed — refresh candidate_seed over the INDEPENDENT lemma_inventory. Candidacy is
         meaning-based only: the migrated independent net (gloss/synonym/IB-judgement/
         read-emergent) plus the editable cfg_candidate_rule inputs. Registry coverage
         (word_strong) is NOT a candidacy route — it is recorded as registry_match, the
         double control (a candidate with registry_match NULL = a candidate MISSING a
         registry word). Over-inclusive by design; the lexical stage is the real test.
  set  — stamp span_candidate on a book's spans whose base-Strong's is a candidate.

Every choice is config: the lemma-base pattern (candidate.lemma_base_pattern), the editable
meaning-net inputs (cfg_candidate_rule: synonym/accept/reject), the write grants.
"""

from __future__ import annotations

import datetime
import re

from .base import Ctx, Outcome, ok, fail


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _base(ctx: Ctx, code: str) -> str:
    m = re.match(ctx.cfg.setting("candidate.lemma_base_pattern", r"^([HG]\d+)([A-Z]?)$"), code or "")
    return m.group(1) if m else (code or "")


def _may(ctx: Ctx, writer: str, table: str):
    if table not in ctx.cfg.may_write(writer):
        raise PermissionError(f"write-grant violation: {writer!r} may not write {table!r}")


def _set_decision(ctx: Ctx, lemma_key: str, decision: str, layer: str, now: str):
    if ctx.db.get("candidate_seed", lemma_key=lemma_key):
        ctx.db.update("candidate_seed", {"lemma_key": lemma_key},
                      decision=decision, layer=layer, assessed_at=now)
    else:
        ctx.db.write("candidate_seed", {
            "lemma_key": lemma_key, "decision": decision, "layer": layer,
            "registry_match": None, "tag": None, "assessed_at": now, "deleted": 0})


# ── seed (global; maintenance over the migrated substrate) ───────────────────
def seed(ctx: Ctx) -> Outcome:
    inv = {r["lemma_key"]: r["gloss"] for r in ctx.db.rows(
        "SELECT lemma_key, gloss FROM lemma_inventory WHERE deleted=0")}
    if not inv:
        return fail("no-inventory", "lemma_inventory is empty — run the seed migration first")
    _may(ctx, "candidate.seed", "candidate_seed")
    now = _now()
    c = {"match_updates": 0, "synonym": 0, "accepted": 0, "rejected": 0}

    # config meaning-net (the editable, INDEPENDENT inputs — all gloss/meaning-based):
    # synonyms (gloss contains a curated synonym), accept (force a lemma candidate),
    # reject (force a lemma out). These MAY create candidacy; word_strong may not.
    syn = [s.lower() for s in ctx.cfg.candidate_rules("synonym")]
    if syn:
        for lk, gloss in inv.items():
            if gloss and any(s in gloss.lower() for s in syn):
                _set_decision(ctx, lk, "candidate", "curated-synonym", now); c["synonym"] += 1
    for lk in ctx.cfg.candidate_rules("accept"):
        if lk in inv:
            _set_decision(ctx, lk, "candidate", "ib-judgement", now); c["accepted"] += 1
    for lk in ctx.cfg.candidate_rules("reject"):
        if lk in inv:
            _set_decision(ctx, lk, "rejected", "ib-judgement", now); c["rejected"] += 1

    # registry coverage = the DOUBLE-CONTROL ONLY. word_strong co-occurrence NEVER makes a
    # lemma a candidate — that is the explicitly-rejected 'LORD->lust' route (registry lists
    # validate, they do not impute). It only records, on an already-independent candidate,
    # which registry word carries its base-Strong's (else NULL = a candidate missing a
    # registry word: the completeness signal).
    cover: dict[str, str] = {}
    for r in ctx.db.rows(
        "SELECT wr.word AS word, ws.strong AS strong FROM word_strong ws "
        "JOIN word_registry wr ON wr.id = ws.word_id WHERE ws.deleted=0 AND wr.deleted=0"):
        cover.setdefault(_base(ctx, r["strong"]), r["word"])
    for r in ctx.db.rows("SELECT lemma_key, registry_match FROM candidate_seed "
                         "WHERE decision='candidate' AND deleted=0"):
        lk = r["lemma_key"]; word = cover.get(lk)
        if r["registry_match"] != word:
            ctx.db.update("candidate_seed", {"lemma_key": lk}, registry_match=word, assessed_at=now)
            c["match_updates"] += 1

    total = ctx.db.rows("SELECT COUNT(*) n FROM candidate_seed "
                        "WHERE decision='candidate' AND deleted=0")[0]["n"]
    missing = ctx.db.rows("SELECT COUNT(*) n FROM candidate_seed WHERE decision='candidate' "
                          "AND registry_match IS NULL AND deleted=0")[0]["n"]
    return ok(f"seed: {total} candidate lemma(s), {missing} without a registry word "
              f"(candidate missing registry words); {c['match_updates']} match update(s), "
              f"+{c['synonym']} synonym, +{c['accepted']} accept, {c['rejected']} reject",
              candidate_total=total, missing_registry_words=missing, **c)


# ── set (book; stamp span_candidate) ─────────────────────────────────────────
def set(ctx: Ctx) -> Outcome:
    book = ctx.params["Book"]
    like = f"{book}.%"
    spans = ctx.db.rows(
        "SELECT sp.id AS span_id, sp.strong_variant AS sv FROM span sp "
        "JOIN verse v ON v.id = sp.verse_id "
        "WHERE v.osisId LIKE ? AND sp.deleted=0 AND v.deleted=0", (like,))
    if not spans:
        return fail("no-spans", f"book {book!r} has no spans — build its words first")

    _may(ctx, "candidate.set", "span_candidate")
    cand = {r["lemma_key"]: r for r in ctx.db.rows(
        "SELECT lemma_key, tag, layer FROM candidate_seed WHERE decision='candidate' AND deleted=0")}

    # clean re-derivation: drop the book's stamps, then restamp
    ctx.db.conn.execute(
        "DELETE FROM span_candidate WHERE span_id IN "
        "(SELECT sp.id FROM span sp JOIN verse v ON v.id=sp.verse_id WHERE v.osisId LIKE ?)", (like,))
    now = _now()
    n = 0
    for s in spans:
        lk = _base(ctx, s["sv"])
        cs = cand.get(lk)
        if cs:
            ctx.db.write("span_candidate", {
                "span_id": s["span_id"], "lemma_key": lk, "candidate_tag": cs["tag"],
                "seed_source": cs["layer"], "set_at": now, "deleted": 0})
            n += 1
    return ok(f"{n} candidate span(s) stamped over {len(spans)} span(s) in {book}",
              span_candidate=n, spans_scanned=len(spans))
