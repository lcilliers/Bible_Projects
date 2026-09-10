"""Lexicon-parsed-layer handlers (L2b — see migration/bootstrap_lexicon_parsed_layer.py) —
interpreters, config-governed, same shape as handlers/raw.py and handlers/candidate.py.

Three steps, work package `lexicon-parse` (standalone, not chained — each invoked independently):
  parse    — strong_meaning_tree + strong_lexicon -> strong_meaning_parsed/strong_lsj_parsed/
             strong_mounce_parsed, via lib.lexiconparse (the corrected 2026-07-25 parse rules).
             No network. Global scope: a full clear-and-rebuild every run, not per-word incremental
             — there is no natural dedup key on a parsed-sense table (matches strong_meaning_tree's
             own no-unique-key shape), and a clear-rebuild is what guarantees the parsed layer
             always reflects the CURRENT parsing rules against the current raw data, the same
             reasoning this session's span rebuild used (migration/rebuild_span_combined_units.py).
  related  — strong -> strong_related, one live STEP getInfo call per row (relatedNos). Also a
             full clear-and-rebuild (STEP's answer can change; there's no reason to keep a stale
             fetch around once a fresh one succeeds).
  validate — read-only coverage + value-quality check across all 4 tables, persists a report every
             run (governance.reports_must_persist), escalates only if findings exist.
"""

from __future__ import annotations

import datetime
import pathlib
import re

from .base import Ctx, Outcome, ok, fail, escalate
from ..lib import escalation as esc, lexiconparse, reportkit, valuequality as vq
from ..lib.stepapi import StepUnavailable


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _may(ctx: Ctx, writer: str, table: str):
    if table not in ctx.cfg.may_write(writer):
        raise PermissionError(f"write-grant violation: {writer!r} may not write {table!r}")


_BASE_RE = re.compile(r"^([HG]\d+)([A-Z]*)$")


def _base(code: str) -> str:
    m = _BASE_RE.match(code)
    return m.group(1) if m else code


def _derived_variant_rows(conn) -> list[tuple]:
    """Escalation #1655, researcher ruling verbatim 2026-09-10: "every parse must support the
    strong table code, if STEP does not return a result for the variant, then A NOTE MUST BE IN
    parse to the effect, and the lemma level can be used in parse as the derived value."

    For every live `strong` code that still has no exact-variant `strong_meaning_parsed` row
    after the normal per-variant rebuild (i.e. `strong_meaning_tree` never had a row for this
    EXACT code — checked live, confirmed against STEP directly for the whole corpus at the time
    this was built: true STEP-side absence, not an unfetched gap), derive its parse coverage from
    whatever senses already exist under its own base lemma, copied verbatim with a `note` marking
    them as derived, not variant-specific. Skipped entirely for a lemma with nothing at all —
    that's the accepted anomaly (`spine-extended-meaning-accepted-anomaly`), not fixable here."""
    live_codes = {r[0] for r in conn.execute("SELECT strongNumber FROM strong WHERE deleted=0")}
    have_variant = {r[0] for r in conn.execute(
        "SELECT DISTINCT strong_variant FROM strong_meaning_parsed WHERE deleted=0")}
    gaps = sorted(live_codes - have_variant)

    rows = []
    for code in gaps:
        lemma = _base(code)
        lemma_rows = conn.execute(
            "SELECT sort, sense_code, gloss, verse_refs, row_type FROM strong_meaning_parsed "
            "WHERE lemma_key=? AND deleted=0 ORDER BY sort, id", (lemma,)).fetchall()
        if not lemma_rows:
            continue
        note = (f"derived from lemma {lemma} — STEP returned no result for the exact code "
               f"{code} (escalation #1655)")
        for sort, sense_code, gloss, verse_refs, row_type in lemma_rows:
            rows.append((lemma, code, sort, sense_code, gloss, verse_refs, note, row_type))
    return rows


# ── parse (global; no network) — also called directly by handlers/raw.py:backfill_meaning ────
def rebuild_parsed_tables(ctx: Ctx) -> dict:
    """The full parse rebuild, factored out so raw.backfill_meaning can call it directly after
    pulling new raw meaning, instead of the researcher having to remember a separate manual
    lexicon.parse re-run every time (found 2026-07-25: exactly this was missed once already).

    Escalation #1655 (2026-09-10): after the normal per-variant rebuild, adds a standing
    lemma-derived-with-note fallback pass (`_derived_variant_rows`) so every live `strong` code
    ends up with SOME `strong_meaning_parsed` coverage — variant-specific where STEP has it,
    lemma-derived-and-noted where it genuinely doesn't. Matches `strong`'s own grain (the same
    grain `span` uses) rather than silently leaving STEP-empty variants with zero parse rows."""
    _may(ctx, "lexicon.parse", "strong_meaning_parsed")
    _may(ctx, "lexicon.parse", "strong_lsj_parsed")
    _may(ctx, "lexicon.parse", "strong_mounce_parsed")

    meaning = lexiconparse.meaning_tree_rows(ctx.cfg)
    lsj = lexiconparse.lsj_rows(ctx.cfg)
    mounce = lexiconparse.mounce_rows(ctx.cfg)

    ctx.db.conn.execute("DELETE FROM strong_meaning_parsed")
    ctx.db.conn.executemany(
        'INSERT INTO strong_meaning_parsed ("lemma_key","strong_variant","sort","sense_code",'
        '"gloss","verse_refs","note","row_type","deleted") VALUES (?,?,?,?,?,?,?,?,0)', meaning)

    derived = _derived_variant_rows(ctx.db.conn)
    ctx.db.conn.executemany(
        'INSERT INTO strong_meaning_parsed ("lemma_key","strong_variant","sort","sense_code",'
        '"gloss","verse_refs","note","row_type","deleted") VALUES (?,?,?,?,?,?,?,?,0)', derived)

    ctx.db.conn.execute("DELETE FROM strong_lsj_parsed")
    ctx.db.conn.executemany(
        'INSERT INTO strong_lsj_parsed ("strong","sense_label","gloss","note","row_type",'
        '"deleted") VALUES (?,?,?,?,?,0)', lsj)

    ctx.db.conn.execute("DELETE FROM strong_mounce_parsed")
    ctx.db.conn.executemany(
        'INSERT INTO strong_mounce_parsed ("strong","mounce_parsed","row_type","deleted") '
        'VALUES (?,?,?,0)', mounce)

    ctx.db.conn.commit()
    return {"strong_meaning_parsed": len(meaning) + len(derived), "strong_lsj_parsed": len(lsj),
           "strong_mounce_parsed": len(mounce), "strong_meaning_parsed_derived": len(derived)}


def parse(ctx: Ctx) -> Outcome:
    counts = rebuild_parsed_tables(ctx)
    return ok(f"parsed: {counts['strong_meaning_parsed']} strong_meaning_parsed "
             f"({counts['strong_meaning_parsed_derived']} lemma-derived, escalation #1655), "
             f"{counts['strong_lsj_parsed']} strong_lsj_parsed, "
             f"{counts['strong_mounce_parsed']} strong_mounce_parsed row(s) — built {_now()}",
             **counts)


# ── related (one live STEP call per strong row) — also called directly by raw.backfill_meaning ─
def fetch_related_for(ctx: Ctx, codes: list[str], clear_first: bool) -> dict:
    """STEP getInfo -> strong_related for exactly `codes`. clear_first=True wipes the whole table
    first (lexicon.related's own full-rebuild use); False just appends (raw.backfill_meaning's
    use, for codes that are brand new and so cannot already have a row to collide with)."""
    _may(ctx, "lexicon.related", "strong_related")

    rows = []
    errors = 0
    none_related = 0
    for code in codes:
        try:
            info = ctx.step.call2_getInfo(code)
            vocabs = info.get("vocabInfos") or []
            related_list = vocabs[0].get("relatedNos", []) if vocabs else []
        except Exception:
            errors += 1
            continue
        if not related_list:
            # a real, completed fetch that genuinely found nothing — still write a row (empty
            # related_strong) so this is distinguishable from "never attempted"/an error, which
            # validate()'s coverage check (NOT EXISTS ... WHERE strong=?) relies on.
            none_related += 1
            rows.append((code, "", "", "", ""))
            continue
        for r in related_list:
            rows.append((code, r.get("strongNumber", ""), r.get("matchingForm", ""),
                        r.get("stepTransliteration", ""), r.get("gloss", "")))

    if clear_first:
        ctx.db.conn.execute("DELETE FROM strong_related")
    ctx.db.conn.executemany(
        'INSERT INTO strong_related ("strong","related_strong","related_form",'
        '"related_transliteration","related_gloss","deleted") VALUES (?,?,?,?,?,0)', rows)
    ctx.db.conn.commit()

    return {"strong_related": len(rows), "strongs_checked": len(codes),
           "none_related": none_related, "errors": errors}


def related(ctx: Ctx) -> Outcome:
    try:
        ctx.step.up()
    except StepUnavailable as e:
        return fail("unreachable", str(e))

    strongs = [r["strongNumber"] for r in ctx.db.rows(
        "SELECT strongNumber FROM strong WHERE deleted=0 ORDER BY strongNumber")]
    counts = fetch_related_for(ctx, strongs, clear_first=True)

    return ok(f"related: {counts['strong_related']} row(s) across {counts['strongs_checked']} "
             f"strong(s) ({counts['none_related']} with no related numbers, "
             f"{counts['errors']} fetch error(s))",
             **counts)


# ── validate (read-only; coverage + value quality; always persists a report) ─────────────────
def _finding_section(f: "vq.ValueFinding") -> list[str]:
    if not f.violations:
        return [f"clean — 0/{f.total} violate `{f.rule}`.", ""]
    L = [f"**{f.violations}/{f.total}** row(s) violate `{f.rule}` in `{f.table}.{f.column}`.", "",
         "| value | rows |", "|---|---:|"]
    L += [f"| {v!r} | {n} |" for v, n in f.samples]
    L.append("")
    return L


def _write_report(ctx: Ctx, no_lsj: int, no_mounce: int, no_related: int,
                  findings: list["vq.ValueFinding"]) -> pathlib.Path:
    path = pathlib.Path(ctx.cfg.required_setting("lexicon.quality_report_path"))
    intro = [
        f"> Generated {_now()} by `lexicon.validate`. Read-only findings, not a gate. Covers "
        f"strong_meaning_parsed/strong_lsj_parsed/strong_mounce_parsed/strong_related together.",
        "",
        f"- `strong_lexicon` rows with no `strong_lsj_parsed` output: **{no_lsj}**",
        f"- `strong_lexicon` rows with no `strong_mounce_parsed` output: **{no_mounce}**",
        f"- `strong` rows with no `strong_related` fetch attempted yet: **{no_related}**",
    ]
    sections = {
        "summary": [f"{f.violations}/{f.total} violate `{f.rule}` in `{f.table}.{f.column}`"
                   for f in findings] or ["no value-quality findings"],
        "coverage": [
            f"strong_lexicon rows with no strong_lsj_parsed output: {no_lsj}",
            f"strong_lexicon rows with no strong_mounce_parsed output: {no_mounce}",
            f"strong rows with no strong_related row at all (fetch never run, or STEP had none): {no_related}",
        ],
        "value_quality": [line for f in findings for line in _finding_section(f)] or ["(none)"],
    }
    L = reportkit.render_scaffold(ctx.db.conn, "lexicon.validate", sections, intro=intro)
    reportkit.write_csv_pairing(ctx.db.conn, "lexicon.validate", path.parent / "export")
    path = reportkit.write_report(ctx.db.conn, "lexicon.validate", path, L)
    return path


def validate(ctx: Ctx) -> Outcome:
    no_lsj = ctx.db.rows(
        "SELECT COUNT(*) n FROM strong_lexicon sl WHERE sl.deleted=0 AND NOT EXISTS "
        "(SELECT 1 FROM strong_lsj_parsed p WHERE p.strong = sl.strong)")[0]["n"]
    no_mounce = ctx.db.rows(
        "SELECT COUNT(*) n FROM strong_lexicon sl WHERE sl.deleted=0 AND NOT EXISTS "
        "(SELECT 1 FROM strong_mounce_parsed p WHERE p.strong = sl.strong)")[0]["n"]
    no_related = ctx.db.rows(
        "SELECT COUNT(*) n FROM strong s WHERE s.deleted=0 AND NOT EXISTS "
        "(SELECT 1 FROM strong_related r WHERE r.strong = s.strongNumber)")[0]["n"]

    findings = [f for f in vq.find_value_quality_findings(ctx.cfg)
               if f.table in ("strong_meaning_parsed", "strong_lsj_parsed", "strong_mounce_parsed",
                              "strong_related")]

    report_path = _write_report(ctx, no_lsj, no_mounce, no_related, findings)

    value_violations = sum(f.violations for f in findings)
    total_findings = no_lsj + no_mounce + no_related + value_violations
    if not total_findings:
        return ok(f"strong_meaning_parsed/strong_lsj_parsed/strong_mounce_parsed/strong_related: "
                 f"full coverage, no value-quality findings — report written to {report_path}")

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision, comment = answered["next_action"], answered["comment"]
        # escalation #798/#799 SS4: decision_required now resolves via Update()'s manual
        # vocabulary (approved) not AnswerRun's dispatcher vocabulary (approve).
        if decision in ("approve", "approved"):
            return ok(f"acknowledged: {no_lsj} strong_lexicon row(s) with no lsj parse, {no_mounce} "
                      f"with no mounce parse, {no_related} strong row(s) with no related fetch, "
                      f"{value_violations} value-quality violation(s) — researcher confirmed known/"
                      f"acceptable; full detail in {report_path}",
                      no_lsj=no_lsj, no_mounce=no_mounce, no_related=no_related,
                      value_violations=value_violations)
        if decision == "reject":
            return fail("findings-rejected",
                       "researcher flagged these findings as needing action, not acknowledgement",
                       no_lsj=no_lsj, no_mounce=no_mounce, no_related=no_related,
                       value_violations=value_violations)
        return fail("needs-revision", f"researcher comment: {comment or '(none)'}")

    return escalate(
        "needs-review",
        question=(f"Lexicon-parse coverage/value-quality findings: {no_lsj} strong_lexicon row(s) "
                 f"with no strong_lsj_parsed output, {no_mounce} with no strong_mounce_parsed "
                 f"output, {no_related} strong row(s) with no strong_related fetch attempted yet, "
                 f"{value_violations} value-quality violation(s) across the 4 tables. Approve to "
                 f"acknowledge as current/known state, reject to flag for action (most likely "
                 f"re-running lexicon.parse/lexicon.related), or revise with a comment. Full "
                 f"detail: {report_path}."),
        preset={"no_lsj": no_lsj, "no_mounce": no_mounce, "no_related": no_related,
               "value_violations": value_violations, "report_path": str(report_path)},
        tried="coverage check (LEFT JOIN / NOT EXISTS against strong_lexicon and strong) + "
              "lib.valuequality's generic notblank/nohtml/pattern engine on the 4 parsed tables",
        resolution_kind="decision_required")
