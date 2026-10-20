"""spine.py -- the base-data spine check (governance.base_data_spine; cfg_method_rule
spine-verse-span-strong-sync-fatal; escalation #1613, researcher ruling 2026-09-10). Extended
2026-10-20, escalation #2173 P3, so the check does what its name says:

  1. span -> strong     every Strong's code a live span names is a live `strong` row (as before)
  2. verse <-> span     every live span belongs to a live verse; every live verse has live spans.
                        A verse with no `verse` row at all is a gap by design
                        (governance.verse_gap_by_design) and is never looked for.
  3. strong -> cluster  every strong a live span names resolves through cluster_strong to a live
                        cluster (governance.base_data_spine as extended 2026-09-21, #1807/#1810 --
                        stated since then, checked by nothing until now)
  4. strong -> meaning  researcher, 2026-10-20 (Q1, verbatim): "you need to check that each strong
                        have its meaning, the three tables are the extracts from STEP, so it is not
                        about which table, it depend on what the STRONG has in step. parsed table
                        stay retired. the check is done directly to the three core meaning
                        tables." Local gaps are found in strong_sense (no live row or an empty
                        head), strong_meaning_tree (no live row with text for the exact code) and
                        strong_lexicon (for the languages in spine.meaning_lexicon_languages: no
                        live row, or an empty lsj or mounce). For those codes only, STEP is asked
                        (call2_getInfo, split exactly as raw.detail_one splits it): content in STEP
                        that the table lacks is FATAL; STEP holding nothing is a gap by design,
                        listed as such. If STEP cannot be asked, the gaps are reported unverified
                        (FATAL: the check could not complete).

The parse tables stay retired (removed from this check 2026-09-11, #1681/#1684/#1686).

compute() is shared with session-close (SC2, which reports FATAL findings first and blocks the
commit until each is fixed or carried). check() is the stand-alone step (Spine-Check.ps1): it
persists the report every run and escalates only on a FATAL finding.
"""

from __future__ import annotations

import datetime
import pathlib
import types

from .base import Ctx, Outcome, ok, escalate, fail
from ..lib import escalation as esc, reportkit


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _rows(conn, sql, args=()):
    return conn.execute(sql, args).fetchall()


def compute(cfg, conn, step=None) -> dict:
    """All spine findings. `step` is a stepapi.Step (or None to skip asking STEP)."""
    live_strong = {r[0] for r in _rows(conn, "SELECT strongNumber FROM strong WHERE deleted=0")}
    span_codes: set[str] = set()
    for r in _rows(conn, "SELECT strong_variant FROM span WHERE deleted=0 AND strong_variant IS NOT "
                         "NULL AND strong_variant != ''"):
        span_codes.update(r[0].split())
    desync = sorted(span_codes - live_strong)

    span_no_verse = [r[0] for r in _rows(conn,
        "SELECT s.id FROM span s WHERE s.deleted=0 AND NOT EXISTS (SELECT 1 FROM verse v WHERE "
        "v.id=s.verse_id AND v.deleted=0) ORDER BY s.id")]
    verse_no_span = [r[0] for r in _rows(conn,
        "SELECT v.osisId FROM verse v WHERE v.deleted=0 AND NOT EXISTS (SELECT 1 FROM span s "
        "WHERE s.verse_id=v.id AND s.deleted=0) ORDER BY v.id")]

    clustered = {r[0] for r in _rows(conn,
        "SELECT cs.strong FROM cluster_strong cs JOIN cluster c ON c.cluster_code=cs.cluster_code "
        "AND c.deleted=0 WHERE cs.deleted=0")}
    no_cluster = sorted((span_codes & live_strong) - clustered)

    lex_langs = set(cfg.required_setting("spine.meaning_lexicon_languages"))
    lang = {r[0]: r[1] for r in _rows(conn, "SELECT strongNumber, language FROM strong WHERE deleted=0")}
    has_sense = {r[0] for r in _rows(conn, "SELECT strong FROM strong_sense WHERE deleted=0 AND "
                                           "COALESCE(TRIM(head),'')<>''")}
    has_tree = {r[0] for r in _rows(conn, "SELECT DISTINCT strong_variant FROM strong_meaning_tree "
                                          "WHERE deleted=0 AND COALESCE(TRIM(sense_text),'')<>''")}
    lex = {r[0]: (bool((r[1] or "").strip()), bool((r[2] or "").strip())) for r in _rows(
        conn, "SELECT strong, lsj, mounce FROM strong_lexicon WHERE deleted=0")}
    gaps: dict[str, list[str]] = {}
    for code in sorted(live_strong):
        g = []
        if code not in has_sense:
            g.append("strong_sense")
        if code not in has_tree:
            g.append("strong_meaning_tree")
        if lang.get(code) in lex_langs:
            l = lex.get(code)
            if l is None:
                g += ["strong_lexicon.lsj", "strong_lexicon.mounce"]
            else:
                if not l[0]:
                    g.append("strong_lexicon.lsj")
                if not l[1]:
                    g.append("strong_lexicon.mounce")
        if g:
            gaps[code] = g

    meaning_fatal: list[dict] = []
    by_design: list[dict] = []
    unverified: list[dict] = []
    step_error = None
    if gaps and step is not None:
        from . import raw as raw_mod
        split_ctx = types.SimpleNamespace(cfg=cfg)
        for code, g in gaps.items():
            try:
                v = (step.call2_getInfo(code).get("vocabInfos") or [None])[0]
            except Exception as exc:          # STEP down mid-run: the rest stay unverified
                step_error = f"{type(exc).__name__}: {exc}"
                unverified.append(dict(code=code, tables=g))
                continue
            head, tree = raw_mod._split_def(split_ctx, (v or {}).get("mediumDef", ""))
            step_has = {
                "strong_sense": bool((head or (v or {}).get("stepGloss") or "").strip()),
                "strong_meaning_tree": bool((tree or "").strip()),
                "strong_lexicon.lsj": bool(((v or {}).get("lsjDefs") or "").strip()),
                "strong_lexicon.mounce": bool(((v or {}).get("shortDefMounce") or "").strip()),
            }
            lacking = [t for t in g if step_has.get(t)]
            nothing = [t for t in g if not step_has.get(t)]
            if lacking:
                meaning_fatal.append(dict(code=code, tables=lacking))
            if nothing:
                by_design.append(dict(code=code, tables=nothing))
    elif gaps:
        unverified = [dict(code=c, tables=g) for c, g in gaps.items()]
        step_error = "STEP was not asked"

    fatal = (len(desync) + len(span_no_verse) + len(verse_no_span) + len(no_cluster)
             + len(meaning_fatal) + len(unverified))
    return dict(desync=desync, span_no_verse=span_no_verse, verse_no_span=verse_no_span,
                no_cluster=no_cluster, meaning_fatal=meaning_fatal, meaning_by_design=by_design,
                meaning_unverified=unverified, step_error=step_error, fatal_count=fatal,
                strongs_checked=len(live_strong), span_codes=len(span_codes))


def finding_lines(f: dict) -> list[tuple[str, str]]:
    """[(stable key, text)] for every FATAL finding -- session-close uses the keys."""
    out = []
    out += [(f"SC2:desync:{c}", f"span names {c}, which has no live strong row") for c in f["desync"]]
    out += [(f"SC2:span:{i}", f"live span {i} belongs to no live verse") for i in f["span_no_verse"]]
    out += [(f"SC2:verse:{o}", f"live verse {o} has no live span") for o in f["verse_no_span"]]
    out += [(f"SC2:cluster:{c}", f"strong {c} (in a live span) has no live cluster_strong row to "
                                 f"a live cluster") for c in f["no_cluster"]]
    out += [(f"SC2:meaning:{m['code']}", f"{m['code']}: STEP holds content that "
                                         f"{', '.join(m['tables'])} lacks")
            for m in f["meaning_fatal"]]
    out += [(f"SC2:unverified:{m['code']}", f"{m['code']}: local gap in {', '.join(m['tables'])} "
                                            f"not verified against STEP ({f['step_error']})")
            for m in f["meaning_unverified"]]
    return out


def _write_report(ctx: Ctx, f: dict) -> pathlib.Path:
    path = pathlib.Path(ctx.cfg.required_setting("spine.quality_report_path"))
    fatal = finding_lines(f)
    intro = [
        f"> Generated {_now()} by `spine.check` (#1613; extended #2173 P3). Read-only. Checks: "
        f"span -> strong, verse <-> span, strong -> cluster, strong -> meaning (strong_sense, "
        f"strong_meaning_tree, strong_lexicon against what STEP holds for each local gap). The "
        f"parse tables stay retired. Every FATAL finding needs action.", "",
        f"- live strongs checked: {f['strongs_checked']}; Strong's codes named by live spans: "
        f"{f['span_codes']}",
        f"- **FATAL findings: {f['fatal_count']}**",
        f"- meaning gaps by design (STEP holds nothing more): {len(f['meaning_by_design'])}", ""]
    integ = [f"- `{k}`: {t}" for k, t in fatal] or ["_no FATAL finding_"]
    design = [f"- {m['code']}: {', '.join(m['tables'])} -- STEP holds nothing for it"
              for m in f["meaning_by_design"]] or ["_none_"]
    sections = {"summary": [f"{f['fatal_count']} FATAL finding(s); "
                            f"{len(f['meaning_by_design'])} meaning gap(s) by design"],
                "integrity": integ, "meaning_by_design": design}
    L = reportkit.render_scaffold(ctx.db.conn, "spine.check", sections, intro=intro)
    return reportkit.write_report(ctx.db.conn, "spine.check", path, L)


def check(ctx: Ctx) -> Outcome:
    f = compute(ctx.cfg, ctx.db.conn, ctx.step)
    report_path = _write_report(ctx, f)
    fatal_count = f["fatal_count"]
    if not fatal_count:
        return ok(f"spine sound: 0 FATAL findings ({len(f['meaning_by_design'])} meaning gap(s) "
                  f"by design) -- report {report_path}", fatal_count=0)

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision, comment = answered["next_action"], answered["comment"]
        if decision in ("approve", "approved"):
            return ok(f"acknowledged: {fatal_count} FATAL spine finding(s) -- researcher confirmed "
                      f"known/tracked, not fixed here; full detail in {report_path}",
                      fatal_count=fatal_count)
        if decision == "reject":
            return fail("spine-fatal-rejected",
                        "researcher flagged these FATAL spine findings as needing action",
                        fatal_count=fatal_count)
        return fail("needs-revision", f"researcher comment: {comment or '(none)'}")

    sample = "; ".join(t for _, t in finding_lines(f)[:10])
    return escalate(
        "spine-fatal-found",
        question=(f"Spine check found {fatal_count} FATAL finding(s) -- per "
                  f"governance.base_data_spine a desync is fixed on discovery, not merely "
                  f"acknowledged. First: {sample}. Approve only to acknowledge as tracked; reject "
                  f"to require a fix; revise with a comment. Full detail: {report_path}."),
        preset={"fatal_count": fatal_count, "report_path": str(report_path)},
        tried="span->strong, verse<->span, strong->cluster and strong->meaning (vs STEP) against "
              "the live spine tables (#1613, #2173 P3)",
        resolution_kind="decision_required")
