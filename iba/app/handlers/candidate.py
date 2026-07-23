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
import json
import pathlib
import re

from .base import Ctx, Outcome, ok, fail, escalate
from ..lib import escalation as esc, reportkit, valuequality as vq


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _base(ctx: Ctx, code: str) -> str:
    m = re.match(ctx.cfg.setting("candidate.lemma_base_pattern", r"^([HG]\d+)([A-Z]?)$"), code or "")
    return m.group(1) if m else (code or "")


def _may(ctx: Ctx, writer: str, table: str):
    if table not in ctx.cfg.may_write(writer):
        raise PermissionError(f"write-grant violation: {writer!r} may not write {table!r}")


def _set_decision(ctx: Ctx, lemma_key: str, decision: str, layer: str, now: str,
                  strong_variant: str | None = None, sense_seq: int = 0):
    """strong_variant defaults to lemma_key itself — 'this row applies to the whole base lemma,
    no sub-strong split decided yet' (found 2026-07-22: candidate_seed had no way to give ONE
    base lemma multiple clean, single-concept tags, one per sub-strong sense — 173 base lemmas
    have sub-lettered strong variants with genuinely different glosses). Dedup is now
    (lemma_key, strong_variant, sense_seq) — sense_seq defaults to 0 (the only/first sense);
    seed()'s bulk net-matching always targets sense_seq=0, it never creates a second sense — only
    candidate.load's dual-concept split does that."""
    variant = strong_variant or lemma_key
    if ctx.db.get("candidate_seed", lemma_key=lemma_key, strong_variant=variant, sense_seq=sense_seq):
        ctx.db.update("candidate_seed", {"lemma_key": lemma_key, "strong_variant": variant,
                                        "sense_seq": sense_seq},
                      decision=decision, layer=layer, assessed_at=now)
    else:
        ctx.db.write("candidate_seed", {
            "lemma_key": lemma_key, "strong_variant": variant, "sense_seq": sense_seq,
            "decision": decision, "layer": layer,
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
    # KNOWN LIMITATION (flagged 2026-07-22, sense_seq's own design doc): a span carries no signal
    # for WHICH sense applies when (lemma_key, strong_variant) has more than one sense_seq row
    # (candidate.load's dual-concept split, #228) — word-sense disambiguation from verse context
    # is out of scope here. Deterministic choice: order sense_seq DESC so the dict comprehension's
    # last write is sense_seq=0 (the original/default sense), which therefore always wins a
    # collision — every span stamps with the base sense unless/until real per-verse
    # disambiguation is built.
    cand = {(r["lemma_key"], r["strong_variant"]): r for r in ctx.db.rows(
        "SELECT lemma_key, strong_variant, tag, layer FROM candidate_seed "
        "WHERE decision='candidate' AND deleted=0 ORDER BY sense_seq DESC")}

    # clean re-derivation: drop the book's stamps, then restamp
    ctx.db.conn.execute(
        "DELETE FROM span_candidate WHERE span_id IN "
        "(SELECT sp.id FROM span sp JOIN verse v ON v.id=sp.verse_id WHERE v.osisId LIKE ?)", (like,))
    now = _now()
    n = 0
    for s in spans:
        full = s["sv"]
        lk = _base(ctx, full)
        # prefer an exact sub-strong-variant row (a deliberate split concept) over the base row
        cs = cand.get((lk, full)) or cand.get((lk, lk))
        if cs:
            ctx.db.write("span_candidate", {
                "span_id": s["span_id"], "lemma_key": lk, "candidate_tag": cs["tag"],
                "seed_source": cs["layer"], "set_at": now, "deleted": 0})
            n += 1
    return ok(f"{n} candidate span(s) stamped over {len(spans)} span(s) in {book}",
              span_candidate=n, spans_scanned=len(spans))


# ── validate (standalone, on-demand — NOT part of the seed/set sequence) ─────
# Extended 2026-07-21: originally checked span_candidate.candidate_tag only (a hand-rolled regex,
# never declared in config). Found that day the SAME shape of dirt exists upstream, unchecked, in
# candidate_seed.tag (the seed decision itself) and lemma_inventory.gloss (the independent
# substrate candidate_seed is built from, and what cfg_candidate_rule's synonym rule matches
# against) — candidate_seed.tag is a verbatim copy of gloss/seed_word at migration time, so a
# dirty gloss is upstream of a dirty seed tag, not just a mirror of it. All three now go through
# ONE engine (lib/valuequality.find_value_quality_findings), reading cfg_column.expectation —
# no more hand-rolled regex per table. This is the seed's proper quality report (previously it had
# none at all): the researcher could not see candidate_seed/lemma_inventory dirt anywhere.
#
# Also kept from the original finding: 17.7% of span_candidate rows have a null tag (normal —
# _set_decision() never sets one; only the historical import_seed.py migration did) and 52.3% have
# a lemma_key with no strong row yet (also normal — strong only grows per registered word). Neither
# is a hard-blocking rule — both are a researcher judgement call, so both stay in the ESCALATE
# path, same as the value-quality findings. Standalone (its own work package, run when the
# researcher actually wants the picture), one escalation per invocation covering everything found
# — not one per row, not repeated every book build.
def _category(value: str) -> str:
    """Cheap grouping for the worklist — which shape of dirt, not a full taxonomy."""
    if ":" in value:
        return "colon (dual-gloss)"
    if "/" in value:
        return "slash (alt-gloss)"
    if "(" in value or ")" in value:
        return "parenthetical"
    return "other"


def _finding_section(f: "vq.ValueFinding") -> list[str]:
    if not f.violations:
        return [f"clean — 0/{f.total} violate `{f.rule}`.", ""]
    by_cat: dict[str, int] = {}
    for v, n in f.samples:
        by_cat[_category(v)] = by_cat.get(_category(v), 0) + n
    L = [f"**{f.violations}/{f.total}** row(s) violate `{f.rule}`, by category (of the samples "
         f"shown below): " + ", ".join(f"{k} {v}" for k, v in sorted(by_cat.items(), key=lambda t: -t[1])),
         "", "| value | rows |", "|---|---:|"]
    L += [f"| {v!r} | {n} |" for v, n in f.samples]
    L.append("")
    return L


def _write_quality_report(ctx: Ctx, sc_null: int, sc_tag: "vq.ValueFinding", seed_null: int,
                          seed_tag: "vq.ValueFinding", orphan_rows: list,
                          gloss: "vq.ValueFinding") -> pathlib.Path:
    """Persist the current findings — per the researcher's 2026-07-21 ruling that a quality check's
    output must persist to a report file like every other report in the app (report.py/
    validation.py/cfgreport.py), not live only in a terminal print + an escalation row. Now covers
    span_candidate (the stamp), candidate_seed (the seed decision), and lemma_inventory (the
    independent substrate) — the seed's own report the researcher asked for, not just the stamp's."""
    path = pathlib.Path(ctx.cfg.setting("candidate.quality_report_path",
                                       "iba/app/reports/candidate-quality.md"))
    orphan_sorted = sorted(orphan_rows, key=lambda r: -r["n"])
    intro = [
        f"> Generated {_now()} by `candidate.validate`. Read-only findings, not a gate. Covers the "
        f"stamp (`span_candidate`), the seed decision (`candidate_seed`), and the independent "
        f"substrate (`lemma_inventory`) — one worklist, not three separate checks.", "",
        f"- `span_candidate.candidate_tag` null: **{sc_null}** row(s)",
        f"- `candidate_seed.tag` null (candidate rows only): **{seed_null}** row(s)",
        f"- `lemma_key` with no `strong` row: **{sum(r['n'] for r in orphan_rows)}** row(s) across "
        f"{len(orphan_rows)} lemma(s)",
    ]
    sections = {
        "span_tag": _finding_section(sc_tag),
        "seed_tag": _finding_section(seed_tag),
        "gloss": _finding_section(gloss),
        "orphan_lemmas": (
            ["| lemma_key | rows |", "|---|---:|"]
            + [f"| {r['lk']} | {r['n']} |" for r in orphan_sorted] + [""]),
    }
    L = reportkit.render_scaffold(ctx.db.conn, "candidate.validate", sections, intro=intro)
    reportkit.write_csv_pairing(ctx.db.conn, "candidate.validate", path.parent / "export")
    reportkit.write_report(ctx.db.conn, "candidate.validate", path, L)
    return path


def validate(ctx: Ctx) -> Outcome:
    findings = {f.table: f for f in vq.find_value_quality_findings(ctx.cfg)
               if f.table in ("span_candidate", "candidate_seed", "lemma_inventory")}
    sc_tag = findings["span_candidate"]
    seed_tag = findings["candidate_seed"]
    gloss = findings["lemma_inventory"]

    sc_null = ctx.db.rows("SELECT COUNT(*) n FROM span_candidate WHERE candidate_tag IS NULL "
                         "AND deleted=0")[0]["n"]
    seed_null = ctx.db.rows("SELECT COUNT(*) n FROM candidate_seed WHERE decision='candidate' "
                           "AND tag IS NULL AND deleted=0")[0]["n"]

    orphan_rows = ctx.db.rows(
        "SELECT sc.lemma_key AS lk, COUNT(*) n FROM span_candidate sc WHERE sc.deleted=0 "
        "AND NOT EXISTS (SELECT 1 FROM strong s WHERE s.strongNumber = sc.lemma_key) "
        "GROUP BY sc.lemma_key")
    orphan_n = sum(r["n"] for r in orphan_rows)
    orphan_lemmas = len(orphan_rows)

    report_path = _write_quality_report(ctx, sc_null, sc_tag, seed_null, seed_tag, orphan_rows, gloss)

    total_findings = sc_null + sc_tag.violations + seed_null + seed_tag.violations + orphan_n + gloss.violations
    if not total_findings:
        return ok(f"span_candidate/candidate_seed/lemma_inventory: no null tags, no messy tags/"
                 f"glosses, every lemma_key resolves to strong — report written to {report_path}")

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision = answered["answer"]
        if decision == "approve":
            return ok(f"acknowledged: {sc_null} null stamp tag(s), {sc_tag.violations} messy stamp "
                      f"tag(s), {seed_null} null seed tag(s), {seed_tag.violations} messy seed "
                      f"tag(s), {gloss.violations} messy gloss(es), {orphan_n} row(s) "
                      f"({orphan_lemmas} lemma(s)) with no strong entry yet — researcher confirmed "
                      f"this is the known/expected state; full detail in {report_path}",
                      sc_null_tags=sc_null, sc_messy_tags=sc_tag.violations, seed_null_tags=seed_null,
                      seed_messy_tags=seed_tag.violations, gloss_messy=gloss.violations,
                      orphan_lemma_rows=orphan_n)
        if decision == "reject":
            return fail("findings-rejected",
                       "researcher flagged these findings as needing action, not acknowledgement",
                       sc_null_tags=sc_null, sc_messy_tags=sc_tag.violations, seed_null_tags=seed_null,
                       seed_messy_tags=seed_tag.violations, gloss_messy=gloss.violations,
                       orphan_lemma_rows=orphan_n)
        return fail("needs-revision", f"researcher comment: {answered['comment'] or '(none)'}")

    return escalate(
        "needs-review",
        question=(f"Candidate quality findings across the stamp, the seed decision, and the "
                 f"independent substrate: {sc_null} null / {sc_tag.violations} messy "
                 f"span_candidate.candidate_tag; {seed_null} null / {seed_tag.violations} messy "
                 f"candidate_seed.tag (the seed's own worklist — see the report's category "
                 f"breakdown); {gloss.violations} messy lemma_inventory.gloss (upstream of the "
                 f"seed tag AND matched by cfg_candidate_rule's synonym rule); {orphan_n} row(s) "
                 f"across {orphan_lemmas} lemma(s) whose lemma_key has no strong entry yet. None of "
                 f"this is new — it reflects the ongoing seed()/import_seed migration state — but "
                 f"it's your call whether it's acceptable as-is or needs action via "
                 f"`candidate.curate` (see the curation method doc). Full detail (every distinct "
                 f"value, every lemma) written to {report_path}."),
        preset={"sc_null_tags": sc_null, "sc_messy_tags": sc_tag.violations,
               "seed_null_tags": seed_null, "seed_messy_tags": seed_tag.violations,
               "seed_messy_sample": seed_tag.samples, "gloss_messy": gloss.violations,
               "orphan_lemma_rows": orphan_n, "orphan_lemmas": orphan_lemmas,
               "orphan_sample": [dict(r) for r in orphan_rows[:20]], "report_path": str(report_path)},
        tried="checked candidate_tag/tag/gloss null+format (via the generic value-quality engine) "
              "and lemma_key/strong resolution against live data — approve to acknowledge as "
              "known/acceptable, reject to flag for action, or revise with a comment on what to check")


# ── curate (standalone, on-demand — the ongoing add/correct/remove utility) ──
# configmaint.propose deliberately never touches DATA tables (candidate_seed, lemma_inventory) —
# it is restricted to cfg_* (see handlers/configmaint.py's CFG_TABLES). candidate_seed still needs
# a governed, single-row, approval-gated way to correct a wrong tag, reject a lemma, split a base
# lemma into per-sub-strong concept rows, or remove an invalid row once written — seed() only ever
# sets tag/decision on FIRST insert (_set_decision), never revises an existing row. This is that
# path: same shape as configmaint.propose (check -> escalate representative payload -> three-way
# approve/reject/revise -> apply), scoped to one (lemma_key, strong_variant) row.
#
# Field:
#   tag / decision  — correct the row for (LemmaKey, StrongVariant or default=LemmaKey).
#   split           — ADD a new row for a specific sub-strong variant (StrongVariant required,
#                     Value = its own clean tag) — one concept, one row, per the researcher's
#                     2026-07-22 tag-cleanliness principle. Copies layer/registry_match from the
#                     base row; the base row's own tag is untouched (correct it separately if it
#                     also needs to change now the lemma is split).
#   delete          — soft-delete the row for (LemmaKey, StrongVariant or default=LemmaKey).
#
# Adding a brand-new candidate LEMMA (not yet in candidate_seed at all) is still the existing
# cfg_candidate_rule 'accept' route via configmaint.propose + a candidate.seed re-run — curate
# corrects/splits/removes rows that already exist, it does not seed a lemma from nothing.
def curate(ctx: Ctx) -> Outcome:
    lemma_key = ctx.params["LemmaKey"]
    fld = ctx.params["Field"]
    variant = ctx.params.get("StrongVariant") or lemma_key
    value = ctx.params.get("Value")
    question = ctx.params.get("Question",
                              f"candidate_seed[{lemma_key}/{variant}].{fld} -> {value!r} — approve?")

    if fld not in ("tag", "decision", "split", "delete"):
        return fail("invalid-proposal", f"Field must be tag/decision/split/delete, got {fld!r}")

    # KNOWN GAP (named 2026-07-22, candidate.load's design doc): curate() has no -SenseSeq param,
    # so it only ever targets sense_seq=0 — correcting a sense_seq>0 row (created by a
    # candidate.load dual-concept split with no distinct sub-strong) isn't supported yet.
    row = None
    base_row = None
    if fld == "split":
        if not ctx.params.get("StrongVariant"):
            return fail("invalid-proposal",
                       "split needs -StrongVariant (the specific sub-lettered strong this new "
                       "row is for, e.g. H0639G)")
        if not value:
            return fail("invalid-proposal", "split needs -Value (the new row's clean, "
                       "single-concept tag)")
        if ctx.db.get("candidate_seed", lemma_key=lemma_key, strong_variant=variant, sense_seq=0):
            return fail("invalid-proposal", f"candidate_seed[{lemma_key}/{variant}] already "
                       f"exists — use Field=tag to correct it, not split")
        base_row = ctx.db.get("candidate_seed", lemma_key=lemma_key, strong_variant=lemma_key, sense_seq=0)
        if not base_row:
            return fail("invalid-proposal",
                       f"no base candidate_seed row for lemma_key {lemma_key!r} to split from")
    else:
        row = ctx.db.get("candidate_seed", lemma_key=lemma_key, strong_variant=variant, sense_seq=0)
        if not row:
            return fail("invalid-proposal",
                       f"no candidate_seed row for ({lemma_key}, {variant}) — add the lemma first "
                       f"via cfg_candidate_rule 'accept' + a candidate.seed re-run, or use "
                       f"Field=split to add a new sub-strong variant row")
        if fld == "decision":
            valid = set(ctx.cfg.enum("candidate_decision"))
            if value not in valid:
                return fail("invalid-proposal",
                           f"decision {value!r} not in enum.candidate_decision {sorted(valid)}")

    _may(ctx, "candidate.curate", "candidate_seed")

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision = answered["answer"]
        now = _now()
        if decision == "approve":
            if fld == "split":
                ctx.db.write("candidate_seed", {
                    "lemma_key": lemma_key, "strong_variant": variant, "decision": "candidate",
                    "layer": base_row["layer"], "registry_match": base_row["registry_match"],
                    "tag": value, "assessed_at": now, "deleted": 0})
                return ok(f"approved and applied: split candidate_seed[{lemma_key}] -> new row "
                         f"for variant {variant} with tag {value!r}",
                         lemma_key=lemma_key, strong_variant=variant, tag=value)
            if fld == "delete":
                ctx.db.update("candidate_seed", {"lemma_key": lemma_key, "strong_variant": variant},
                             deleted=1, assessed_at=now)
                return ok(f"approved and applied: soft-deleted candidate_seed[{lemma_key}/{variant}]",
                         lemma_key=lemma_key, strong_variant=variant)
            ctx.db.update("candidate_seed", {"lemma_key": lemma_key, "strong_variant": variant},
                         assessed_at=now, **{fld: value})
            return ok(f"approved and applied: candidate_seed[{lemma_key}/{variant}].{fld} "
                     f"{row[fld]!r} -> {value!r}",
                     lemma_key=lemma_key, strong_variant=variant, field=fld, value=value)
        if decision == "reject":
            return fail("change-rejected",
                       f"proposal rejected: candidate_seed[{lemma_key}/{variant}].{fld}")
        return fail("needs-revision", f"researcher comment: {answered['comment'] or '(none)'}")

    if fld == "split":
        detail = (f"NEW row candidate_seed[{lemma_key}/{variant}]: tag={value!r} (split off the "
                 f"base row, which keeps its own tag {base_row['tag']!r} unless corrected "
                 f"separately)")
    elif fld == "delete":
        detail = (f"candidate_seed[{lemma_key}/{variant}]: SOFT-DELETE (deleted=1) — current "
                 f"tag={row['tag']!r}, decision={row['decision']!r}, layer={row['layer']!r}")
    else:
        detail = f"candidate_seed[{lemma_key}/{variant}]: {fld} currently {row[fld]!r} -> proposed {value!r}"

    return escalate(
        "needs-approval",
        question=f"{question}\n\n{detail}",
        preset={"lemma_key": lemma_key, "strong_variant": variant, "field": fld, "value": value},
        tried="single-row correction/split/delete on candidate_seed — approve to apply, reject to "
              "decline, or revise with a comment on what to check")


# ── load (none; JSON-batch create/update/validate — the missing "add a batch of words, from
# outside the app" mode configuration_maintenance's propose can't provide, since propose never
# touches data tables). Design: iba/docs (plan) melodic-foraging-bunny — approved 2026-07-22.
#
# Unlike curate() (single-row, approval-gated, candidate.curate's whole reason to exist),
# load() follows seed()'s precedent: a clean item auto-loads, no per-item approval. Only
# EXCEPTIONS (duplicate / format failure / no lemma match / gloss mismatch) are held back —
# and even those are WRITTEN into candidate_seed (decision='exception'), not just reported, so
# they are inspectable in the table itself. One escalation for the whole run, only if any
# exception rows remain unresolved after this run's own pass.
#
# The input JSON never names a lemma_key — only an English `word` and a `reason`. Finding which
# lemma(s)/strong_variant(s) the word maps to, preferring a sub-lettered variant's OWN gloss over
# the collapsed base-lemma gloss when one matches, is this function's job.
def _split_concepts(ctx: Ctx, word: str) -> list[str]:
    """Mechanical split only — on a configured delimiter (':' or '/'), never a semantic guess
    about which half is 'correct'. Each piece is validated/loaded independently."""
    delim = ctx.cfg.setting("candidate.concept_delimiter_pattern", r"[:/]")
    if not re.search(delim, word or ""):
        return [word]
    parts = [p.strip() for p in re.split(delim, word) if p.strip()]
    return parts or [word]


def _format_violation(ctx: Ctx, word: str, clean_re: "re.Pattern", max_words: int,
                      translit_re: "re.Pattern") -> str | None:
    """First format rule `word` fails, or None if clean. Every pattern/threshold is config —
    see candidate.tag_clean_pattern (reused), candidate.tag_max_words, candidate.transliteration_pattern."""
    if not word:
        return "blank word"
    if not clean_re.match(word):
        return "special characters (fails candidate.tag_clean_pattern)"
    if len(word.split()) > max_words:
        return f"more than {max_words} word(s) — looks like a sentence, not a concept"
    if translit_re.match(word.lower()) and " " not in word:
        return "looks like a bare transliteration, not an English gloss (candidate.transliteration_pattern)"
    return None


def _resolve_lemma(ctx: Ctx, word: str) -> tuple[str | None, str | None, str | None]:
    """Derive (lemma_key, strong_variant, gloss_used) for an English word — no lemma_key in the
    input, this is the tool's own job. Tries a direct/synonym match against lemma_inventory.gloss
    (same substring mechanism as seed()'s curated cfg_candidate_rule 'synonym' kind — reused, not
    duplicated), then prefers a sub-lettered strong VARIANT's own gloss over the base lemma's
    collapsed gloss when one matches (the researcher's 2026-07-22 rule: pull the variant gloss,
    never the lemma gloss, when a variant exists). Returns (None, None, None) if nothing matches.

    FIXED 2026-07-22 (found by testing, not by inspection): raw substring containment
    (`w in gloss or gloss in w`) is unsafe when either side is short — gloss 'I' matched inside
    'hearing', gloss 'word' matched inside the test nonsense-word 'zzznotarealword'. Matching is
    now WORD-BOUNDARY bounded (`\\bword\\b`), and an EXACT match on an existing candidate_seed.tag
    is tried FIRST — this word is a real Strong's already-loaded synonym-shaped tag, this word
    duplicates a real existing candidate.load bug found: 'hearing' re-resolved to a different,
    wrong lemma (H0589, gloss 'I') instead of recognising H8085's existing tag='hearing' row as
    the same word."""
    w = word.strip().lower()

    # exact match against an EXISTING candidate_seed.tag first — if this word is already
    # someone's tag, THAT is the right lemma; prevents a second, wrong lemma_key being resolved
    # for a word that's already correctly seeded (the 'hearing' bug).
    existing = ctx.db.rows(
        "SELECT lemma_key, strong_variant FROM candidate_seed WHERE deleted=0 AND lower(tag)=?", (w,))
    if existing:
        r = existing[0]
        base_row = ctx.db.get("strong", strongNumber=r["strong_variant"])
        return r["lemma_key"], r["strong_variant"], (base_row["stepGloss"] if base_row else None)

    syn = [s.lower() for s in ctx.cfg.candidate_rules("synonym") if s]
    w_re = re.compile(r"\b" + re.escape(w) + r"\b")
    exact_lemma = None
    partial_lemma = None
    for r in ctx.db.rows("SELECT lemma_key, gloss FROM lemma_inventory WHERE deleted=0"):
        gloss = (r["gloss"] or "").lower()
        if not gloss:
            continue
        if gloss == w:
            exact_lemma = r["lemma_key"]
            break
        if partial_lemma is None and w_re.search(gloss):
            partial_lemma = r["lemma_key"]
        elif partial_lemma is None and any(
                s and re.search(r"\b" + re.escape(s) + r"\b", gloss) and
                re.search(r"\b" + re.escape(s) + r"\b", w) for s in syn):
            partial_lemma = r["lemma_key"]
    lemma_key = exact_lemma or partial_lemma
    if not lemma_key:
        return None, None, None

    # prefer a sub-lettered variant's OWN gloss (LIKE 'BASE_' matches exactly one trailing char,
    # the shape candidate.lemma_base_pattern strips) over the collapsed base lemma
    for r in ctx.db.rows(
            "SELECT strongNumber, stepGloss FROM strong WHERE strongNumber LIKE ? AND deleted=0",
            (lemma_key + "_",)):
        vgloss = (r["stepGloss"] or "").lower()
        if vgloss and (vgloss == w or w_re.search(vgloss)):
            return lemma_key, r["strongNumber"], r["stepGloss"]

    base_row = ctx.db.get("strong", strongNumber=lemma_key)
    return lemma_key, lemma_key, (base_row["stepGloss"] if base_row else None)


def _step_status(ctx: Ctx, lemma_key: str) -> str:
    """Read-only STEP cross-reference — NEVER writes to `strong` (raw.detail's job, its own
    grant). in_strong / step_no_verses / not_in_step / step_has_verses_pending."""
    if ctx.db.get("strong", strongNumber=lemma_key):
        return "in_strong"
    try:
        info = ctx.step.call2_getInfo(lemma_key)
    except Exception:
        return "not_in_step"
    if not (info.get("vocabInfos") or []):
        return "not_in_step"
    total = ctx.step._get(ctx.step._route("call3_strong", strong=lemma_key)).get("total", 0)
    return "step_has_verses_pending" if total > 0 else "step_no_verses"


def _ib_referent(ctx: Ctx, gloss: str | None) -> str:
    """Informational, not a gate — config-driven via two new cfg_candidate_rule kinds
    (Cfg.candidate_rules(kind) is fully generic, no code change needed for new kinds)."""
    if not gloss:
        return "characteristic"
    g = gloss.lower()
    if any(s.lower() in g for s in ctx.cfg.candidate_rules("body-part")):
        return "body_part"
    if any(s.lower() in g for s in ctx.cfg.candidate_rules("other-being")):
        return "other_being"
    return "characteristic"


def _write_exception(ctx: Ctx, key: str, variant: str, sense_seq: int, word: str, reason: str,
                     note: str, now: str) -> None:
    if ctx.db.get("candidate_seed", lemma_key=key, strong_variant=variant, sense_seq=sense_seq):
        ctx.db.update("candidate_seed", {"lemma_key": key, "strong_variant": variant,
                                        "sense_seq": sense_seq},
                     decision="exception", layer="batch-load", tag=word, assessed_at=now)
    else:
        ctx.db.write("candidate_seed", {
            "lemma_key": key, "strong_variant": variant, "sense_seq": sense_seq,
            "decision": "exception", "layer": "batch-load", "registry_match": None,
            "tag": word, "assessed_at": now, "deleted": 0})


def _process_item(ctx: Ctx, word: str, reason: str, sense_seq: int, clean_re, max_words,
                  translit_re, now: str, c: dict) -> None:
    violation = _format_violation(ctx, word, clean_re, max_words, translit_re)
    if violation:
        # no real lemma_key resolvable pre-format -- use an UNRESOLVED: placeholder, distinct and
        # inspectable (FKs are declared but never hard-enforced in this app, per BUILD.md D1)
        placeholder = f"UNRESOLVED:{word or '(blank)'}"
        _write_exception(ctx, placeholder, placeholder, sense_seq, word, reason,
                         f"format: {violation}", now)
        c["exceptions"] += 1
        return

    lemma_key, variant, gloss = _resolve_lemma(ctx, word)
    if not lemma_key:
        placeholder = f"UNRESOLVED:{word}"
        _write_exception(ctx, placeholder, placeholder, sense_seq, word, reason,
                         "no lemma_inventory/strong match found", now)
        c["exceptions"] += 1
        return

    if ctx.db.get("candidate_seed", lemma_key=lemma_key, strong_variant=variant, sense_seq=sense_seq):
        # per the approved plan: a true duplicate writes NOTHING and touches NOTHING — the
        # existing row is the record; only report the collision. (FIXED 2026-07-22, found by
        # testing: this used to call _write_exception, which — because the row already exists —
        # took its UPDATE branch and overwrote the pre-existing legitimate row's decision/tag.
        # That's real data corruption on every duplicate, the same class of mistake as the
        # revalidation bug earlier this session, caught before it ran over the full seed.)
        c["duplicates"] = c.get("duplicates", 0) + 1
        c.setdefault("duplicate_samples", []).append(f"{word!r} -> existing candidate_seed[{lemma_key}/{variant}/{sense_seq}]")
        return

    w = word.strip().lower()
    w_re = re.compile(r"\b" + re.escape(w) + r"\b")
    gloss_match = bool(gloss) and (gloss.lower() == w or w_re.search(gloss.lower()))
    if gloss and not gloss_match:
        _write_exception(ctx, lemma_key, variant, sense_seq, word, reason,
                         f"cross-reference mismatch: strong gloss {gloss!r} does not relate to {word!r}", now)
        c["exceptions"] += 1
        return

    status = _step_status(ctx, lemma_key if variant == lemma_key else variant)
    referent = _ib_referent(ctx, gloss)
    ctx.db.write("candidate_seed", {
        "lemma_key": lemma_key, "strong_variant": variant, "sense_seq": sense_seq,
        "decision": "candidate", "layer": "batch-load", "registry_match": None, "tag": word,
        "step_status": status, "ib_referent_type": referent, "assessed_at": now, "deleted": 0})
    c["loaded"] += 1


def _revalidate_existing(ctx: Ctx, clean_re, max_words, translit_re, now: str, c: dict) -> None:
    """Mechanical-only revalidation of every existing row — re-derive step_status/ib_referent_type
    (cheap, deterministic) and flag a NEWLY-failing format as an exception. Does NOT attempt to
    fix tag CONTENT (curation doc §7: no principled way to mechanically decide "hearing" vs
    "obey") — that still needs a human read via candidate.curate."""
    for r in ctx.db.rows(
            "SELECT lemma_key, strong_variant, sense_seq, tag, decision FROM candidate_seed "
            "WHERE deleted=0 AND decision != 'exception'"):
        tag = r["tag"] or ""
        violation = _format_violation(ctx, tag, clean_re, max_words, translit_re) if tag else None
        base_row = ctx.db.get("strong", strongNumber=r["strong_variant"]) or \
                   ctx.db.get("strong", strongNumber=r["lemma_key"])
        gloss = base_row["stepGloss"] if base_row else None
        status = _step_status(ctx, r["strong_variant"])
        referent = _ib_referent(ctx, gloss)
        if violation:
            ctx.db.update("candidate_seed",
                          {"lemma_key": r["lemma_key"], "strong_variant": r["strong_variant"],
                           "sense_seq": r["sense_seq"]},
                          decision="exception", assessed_at=now)
            c["exceptions"] += 1
        ctx.db.update("candidate_seed",
                     {"lemma_key": r["lemma_key"], "strong_variant": r["strong_variant"],
                      "sense_seq": r["sense_seq"]},
                     step_status=status, ib_referent_type=referent)


def load(ctx: Ctx) -> Outcome:
    _may(ctx, "candidate.load", "candidate_seed")

    input_file = ctx.params.get("InputFile")
    items = []
    if input_file:
        data = json.loads(pathlib.Path(input_file).read_text(encoding="utf-8"))
        items = data.get("items", [])

    clean_re = re.compile(ctx.cfg.setting("candidate.tag_clean_pattern", r"^[A-Za-z][A-Za-z' -]*$"))
    max_words = int(ctx.cfg.setting("candidate.tag_max_words", 5))
    translit_re = re.compile(ctx.cfg.setting("candidate.transliteration_pattern",
                                             r"^(?=.*[a-z])[a-z]{2,10}$"))
    now = _now()
    c = {"loaded": 0, "exceptions": 0, "split_items": 0, "duplicates": 0, "duplicate_samples": []}

    for item in items:
        word = (item.get("word") or "").strip()
        reason = item.get("reason", "")
        parts = _split_concepts(ctx, word)
        if len(parts) > 1:
            c["split_items"] += 1
        for seq, part in enumerate(parts):
            _process_item(ctx, part, reason, seq, clean_re, max_words, translit_re, now, c)

    _revalidate_existing(ctx, clean_re, max_words, translit_re, now, c)

    exceptions_open = ctx.db.rows(
        "SELECT COUNT(*) n FROM candidate_seed WHERE decision='exception' AND deleted=0")[0]["n"]
    report_path = pathlib.Path(ctx.cfg.setting("candidate.load_report_path",
                                               "iba/app/reports/candidate-load.md"))
    sample = ctx.db.rows(
        "SELECT lemma_key, strong_variant, sense_seq, tag, layer FROM candidate_seed "
        "WHERE decision='exception' AND deleted=0 ORDER BY assessed_at DESC LIMIT 20")
    dup_lines = "\n".join(f"- {d}" for d in c["duplicate_samples"][:20])
    intro = [
        f"> Generated {now}. {c['loaded']} item(s) loaded from this run's input "
        f"({c['split_items']} split on a concept delimiter). {c['duplicates']} duplicate(s) "
        f"skipped — NOT written or touched, the existing row is already the record. "
        f"{exceptions_open} exception row(s) open in candidate_seed (decision='exception') — "
        f"every one written into the table, not just reported here.",
    ]
    sections = {
        "duplicates": [dup_lines or "(none)"],
        "exceptions": [
            "| lemma_key | strong_variant | sense_seq | tag | layer |", "|---|---|---|---|---|",
        ] + [f"| {r['lemma_key']} | {r['strong_variant']} | {r['sense_seq']} | "
             f"{r['tag']!r} | {r['layer']} |" for r in sample],
    }
    all_exceptions = ctx.db.rows(
        "SELECT * FROM candidate_seed WHERE decision='exception' AND deleted=0 "
        "ORDER BY assessed_at DESC")
    L = reportkit.render_scaffold(ctx.db.conn, "candidate.load", sections, intro=intro)
    reportkit.write_csv_pairing(ctx.db.conn, "candidate.load", report_path.parent / "export",
                                row_filter={"candidate_seed": all_exceptions})
    reportkit.write_report(ctx.db.conn, "candidate.load", report_path, L)

    if exceptions_open == 0:
        return ok(f"candidate.load: {c['loaded']} item(s) loaded clean, {c['duplicates']} "
                  f"duplicate(s) skipped untouched, seed list is clear", **c)

    return escalate(
        "needs-review",
        question=(f"candidate.load: {c['loaded']} item(s) loaded clean this run, "
                  f"{c['duplicates']} duplicate(s) skipped untouched; "
                  f"{exceptions_open} exception row(s) now sit in candidate_seed "
                  f"(decision='exception') needing a researcher read — format "
                  f"failures, unresolved lemma matches, or a cross-reference mismatch against "
                  f"STEP's own gloss. Full list: {report_path}."),
        preset={"loaded": c["loaded"], "exceptions_open": exceptions_open,
               "sample": [dict(r) for r in sample], "report_path": str(report_path)},
        tried="format/derivation/duplicate/cross-reference checks applied per item, all "
              "config-driven; approve to acknowledge (leave exceptions for candidate.curate "
              "later), reject to flag for immediate action, or revise with a comment",
        **c)
