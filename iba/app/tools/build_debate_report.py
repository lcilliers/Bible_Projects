"""build_debate_report.py (standalone; reads `iba.db` broadly, writes ONLY `passage.debate_path`/
`debate_written_at`/`debate_status` on the one passage it renders — see 2026-08-06 update below) —
Step 6 (debate digest) / Step 6's own stated purpose (BUILD.md §61: "the .md document becomes a
generated extract off those DB records... never itself written to directly"): renders one
hib-continuity passage's `hib`/`phenomenon`/`operation`/`operation_party`/`passage_linkage`/
`passage_insufficiency`/`passage_emergent_question`/`passage_validation_note` rows into the exact
8-section shape `WA-interpretation-questions-v1.4` Part C specifies, plus a leading
**process-control section** (researcher, 2026-08-06: "I would expect both detail and controls
regarding each table that was updated, and that the report tells the story of the IB operations in
the chapter") — this is also B5's "working record," collapsed into a report rather than a
maintained file, exactly as `b3-b5-operations-schema-design-20260805.md` proposed ("a report, not
a file to maintain... report.passage_control").

**2026-08-06 update — no longer purely read-only.** Researcher, reviewing `configmaint.validate`'s
own stale-`filled_by` finding: `passage.debate_path`/`debate_written_at`/`debate_status` were never
written for a new-model passage at all — this tool only ever rendered a file, never recorded that
it had. Fixed: after a successful render, grant-checked (`report.debate → passage`, same principle
as every other write in this app even though there's no `Ctx`/dispatcher here) writes those three
columns. `debate_status` is computed live every call, not hand-set — `empty` (no phenomena yet),
`in-progress` (Steps 3-5 not both complete), `complete` (phase gate set and every phenomenon has an
operation) — new `enum.passage_debate_status` values alongside legacy's `scaffold`/`filled`. One
call now does what the legacy model needed two for (`report.passage_debate` + a separate
`PassageDebate-Sync.ps1` confirmation) — nothing here is a static file needing a human to confirm
they filled it in; status is recomputed from the DB fresh every regenerate.

**Why a standalone tool, not a `cfg_report`-registered `report.*` step (2026-08-06 scoping call).**
`reportkit.render_scaffold` requires a `cfg_report`/`cfg_report_section` row per section — 8+ new
config rows, each needing its own `configmaint.propose` approval cycle, on top of the write-grant
proposals `closing.set` already needed. This tool instead hand-builds Markdown; it still gets
versioning + archive-on-regenerate for free via `reportkit.write_report` (`step="report.debate"` —
already a recognised writer name, via `cfg_write_grant`, no NEW config row needed for that either).
If the researcher later wants these 8 section headings to be config-editable the way
`report.passage_debate` already is, promoting this to a registered `cfg_report` step is a small,
well-scoped follow-up, not a redesign — flagged, not built here, to keep this delivery unblocked by
an approval queue.

**Filing corrected 2026-08-08 (found live: a real book's debate reports were landing flat in
`iba/app/reports/` instead of the book-scoped folder every sibling book tool uses).** This report is
book-scoped analytical output, same class as `lexical.build`/`report.verse_span_meaning`/
`report.whole_book_read`/the narrative — not a "one-off investigatory" report (`reportkit.oneoff_path`,
what `build_verse_span_meaning_extract.py`/`build_verse_span_strongtree_extract.py` correctly use,
since THOSE really are ad-hoc extracts, not the book's filed record). Now files under the SAME
`report.verse_analysis_output_dir/<book_label or book>/` convention as every sibling tool
(`versespanmeaningreport.py`/`lexical.py`/`passagedebatereport.py`/`narrativegenerate.py`/
`wholebookread.py` all do `folder = book_label or book` inline — no shared helper existed to reuse,
so this follows the same inline shape rather than inventing a new abstraction) — takes an optional
`--book-label` the same shape as those tools' `-BookLabel`.

**Reads broadly, writes narrowly.** Every table it reads from is untouched; the only write is the
grant-checked tracking-column update on its own target passage, described above. Refuses to run
against a legacy (`rule IS NULL`) passage — this report only makes sense for a passage actually
carrying `hib`/`phenomenon`/
`operation` rows, which only a `hib-continuity` passage can have (BUILD.md §64's `_find_new_model_
passage` guard, mirrored here read-only).

Usage:
  python -m iba.app.tools.build_debate_report --book Dan --range 8:1-27 --book-label Daniel
  python -m iba.app.tools.build_debate_report --book Dan --chapters 1-3 --book-label Daniel
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

import pathlib

from iba.app.lib.cfg import Cfg
from iba.app.lib import reportkit
from iba.app.lib import passagetrack
from iba.app.lib.versespanmeaningreport import parse_chapters, parse_range


def _find_passage(conn: sqlite3.Connection, book: str, lo: int, hi: int, vlo, vhi):
    row = passagetrack.find_tracked_passage(conn, book, lo, hi, vlo, vhi)
    if row is None:
        return None, f"no tracked passage for {book} this range"
    if row["rule"] is None:
        return None, (f"passage {row['id']} ({row['ref']}) is a legacy (pre-hib-continuity) row — "
                      f"this report only renders hib-continuity passages (run Build-Passages.ps1 "
                      f"first)")
    return row, None


def _rows(conn: sqlite3.Connection, sql: str, args=()) -> list[dict]:
    return [dict(r) for r in conn.execute(sql, args).fetchall()]


def build(conn: sqlite3.Connection, book: str, lo: int, hi: int, vlo=None, vhi=None) -> list[str]:
    passage, problem = _find_passage(conn, book, lo, hi, vlo, vhi)
    if problem:
        raise ValueError(problem)
    pid = passage["id"]

    # 2026-08-06 fix (researcher, first real Dan 8 run): ORDER BY is_anchor DESC alone has no
    # tiebreaker for the non-anchor rows -- SQLite does not guarantee tie order without one, which
    # is why Dan 8:19 rendered before Dan 8:6. `verse` has no chapter/verse columns (osisId-only,
    # same as every other reader in this app -- versespanmeaningreport.fetch_verses parses it the
    # same way), so the tiebreak is done in Python after fetch, anchor still pinned first.
    vp_rows = _rows(
        conn, "SELECT vp.verse_id, vp.is_anchor, v.osisId FROM verse_passage vp "
              "JOIN verse v ON v.id = vp.verse_id WHERE vp.passage_id=? AND vp.deleted=0", (pid,))
    def _ch_vs(osis_id: str) -> tuple[int, int]:
        parts = osis_id.split(".")
        return (int(parts[-2]), int(parts[-1]))
    vp_rows.sort(key=lambda r: (0 if r["is_anchor"] else 1, *_ch_vs(r["osisId"])))
    verse_ids = [r["verse_id"] for r in vp_rows]
    verses = {r["id"]: r for r in _rows(
        conn, f"SELECT id, osisId, text FROM verse WHERE id IN "
              f"({','.join('?' * len(verse_ids))}) AND deleted=0", tuple(verse_ids))} if verse_ids else {}
    verse_order = [vid for vid in verse_ids if vid in verses]

    hibs_in_passage = {r["hib_id"] for r in _rows(
        conn, f"SELECT DISTINCT hib_id FROM verse_hib WHERE deleted=0 AND verse_id IN "
              f"({','.join('?' * len(verse_ids))})", tuple(verse_ids))} if verse_ids else set()
    hib_rows = {r["id"]: r for r in _rows(
        conn, f"SELECT id, label, kind FROM hib WHERE deleted=0 AND id IN "
              f"({','.join('?' * len(hibs_in_passage))})",
        tuple(hibs_in_passage))} if hibs_in_passage else {}

    phen_rows = _rows(
        conn, "SELECT id, verse_id, hib_id, description, textual_warrant, status, ordinal "
              "FROM phenomenon WHERE passage_id=? AND deleted=0 ORDER BY verse_id, hib_id, ordinal",
        (pid,))
    phen_by_id = {r["id"]: r for r in phen_rows}

    op_rows = _rows(
        conn, "SELECT id, phenomenon_id, process, action_type, decision, observation_text, "
              "description_text FROM operation WHERE deleted=0 AND phenomenon_id IN "
              f"({','.join('?' * len(phen_by_id)) or 'NULL'})", tuple(phen_by_id))
    op_by_phen = {r["phenomenon_id"]: r for r in op_rows}
    op_ids = [r["id"] for r in op_rows]
    parties_by_op: dict[int, list[dict]] = {}
    if op_ids:
        for r in _rows(
            conn, f"SELECT operation_id, role, kind, detail, enablement_only FROM operation_party "
                  f"WHERE deleted=0 AND operation_id IN ({','.join('?' * len(op_ids))}) "
                  f"ORDER BY operation_id, role, ordinal", tuple(op_ids)):
            parties_by_op.setdefault(r["operation_id"], []).append(r)

    linkages = _rows(
        conn, "SELECT from_operation_id, to_operation_id, note FROM passage_linkage "
              "WHERE passage_id=? AND deleted=0 ORDER BY ordinal", (pid,))
    insufficiencies = _rows(
        conn, "SELECT pi.note, v.osisId FROM passage_insufficiency pi LEFT JOIN verse v "
              "ON v.id=pi.verse_id WHERE pi.passage_id=? AND pi.deleted=0 ORDER BY pi.ordinal",
        (pid,))
    emergent = _rows(
        conn, "SELECT peq.question_text, peq.kind, v.osisId FROM passage_emergent_question peq "
              "LEFT JOIN verse v ON v.id=peq.verse_id WHERE peq.passage_id=? AND peq.deleted=0 "
              "ORDER BY peq.ordinal", (pid,))
    validation = _rows(
        conn, "SELECT finding_text, corrected, phenomenon_id FROM passage_validation_note "
              "WHERE passage_id=? AND deleted=0 ORDER BY ordinal", (pid,))
    open_decisions = passage["open_decisions_note"]

    # ── process control (researcher, 2026-08-06: "detail AND controls... tells the story") ──
    total_pairs = len(verse_ids) and len(_rows(
        conn, f"SELECT verse_id, hib_id FROM verse_hib WHERE deleted=0 AND verse_id IN "
              f"({','.join('?' * len(verse_ids))})", tuple(verse_ids)))
    phen_count = len(phen_rows)
    op_count = len(op_by_phen)
    missing_ops = phen_count - op_count
    # debate_status, 2026-08-06 (researcher: "this should now reference the new report" --
    # passage.debate_path/debate_written_at/debate_status were never written for a new-model
    # passage at all before this; the OLD scaffold/filled lifecycle needed a human to hand-fill
    # a static file and a separate PassageDebate-Sync.ps1 call to confirm it -- this report is
    # regenerated fresh from the DB every call, so status is just computed live, no sync step
    # needed. 'empty' = nothing started; 'in-progress' = some phenomena but Steps 3-5 not both
    # complete; 'complete' = phase gate set AND every phenomenon has an operation (enum.
    # passage_debate_status: empty|in-progress|complete, alongside legacy's scaffold|filled).
    if phen_count == 0:
        debate_status = "empty"
    elif passage["phenomena_complete_at"] and missing_ops == 0:
        debate_status = "complete"
    else:
        debate_status = "in-progress"

    L = [f"# Passage debate — {passage['ref']} (`{book}`, DB-generated)", "",
        f"> Generated from `iba.db` — this is a render, not a working document. Regenerate after "
        f"any `hib.set`/`phenomenon.set`/`operation.set`/`closing.set` call; never hand-edit.", "",
        "## Contents", "",
        "- [Process control](#process-control)",
        "- [Preliminaries](#preliminaries)",
        "- [Phenomena register (Phase 1)](#phenomena-register-phase-1)",
        "- [Per-verse operations (Phase 2)](#per-verse-operations-phase-2)",
        "- [Passage-level linkages (Q7)](#passage-level-linkages-q7)",
        "- [Insufficiencies register](#insufficiencies-register)",
        "- [Emergent questions log](#emergent-questions-log)",
        "- [Debate quality validation (Phase 3)](#debate-quality-validation-phase-3)",
        "- [Open decisions / next steps](#open-decisions-next-steps)", "",
    ]

    L += ["## Process control", "",
         f"| table | live rows for this passage |", "|---|---:|",
         f"| `hib` (in scope) | {len(hib_rows)} |",
         f"| `verse_hib` (control total: verse×HIB pairs) | {total_pairs} |",
         f"| `phenomenon` | {phen_count} |",
         f"| `operation` | {op_count} |",
         f"| `passage_linkage` | {len(linkages)} |",
         f"| `passage_insufficiency` | {len(insufficiencies)} |",
         f"| `passage_emergent_question` | {len(emergent)} |",
         f"| `passage_validation_note` | {len(validation)} |", "",
         f"- **Step 3 phase gate** (`passage.phenomena_complete_at`): "
         f"{'SET — ' + str(passage['phenomena_complete_at']) if passage['phenomena_complete_at'] else 'NOT SET — phenomena register incomplete, operation.set is refused'}",
         f"- **Operations completeness** (computed live, not stored): "
         f"{'complete — every phenomenon has an operation' if missing_ops == 0 else f'{missing_ops} phenomenon/phenomena still have no operation'}",
         f"- **`needs_review`**: {'yes — ' + str(passage['verse_count']) + ' verses, over review threshold' if passage['needs_review'] else 'no'}",
         f"- **Debate status**: `{debate_status}`",
         "",
    ]

    L += ["## Preliminaries", "",
         f"- **Passage:** {passage['ref']} (`passage.id={pid}`, rule=`{passage['rule']}`, "
         f"source=`{passage['source']}`)",
         f"- **Verse count:** {passage['verse_count']}",
         f"- **HIBs in scope:** " + (", ".join(f"{h['label']} ({h['kind']})"
                                              for h in hib_rows.values()) or "(none)"),
         "",
    ]

    L += ["## Phenomena register (Phase 1)", ""]
    if not phen_rows:
        L += ["(none written yet)", ""]
    else:
        for vid in verse_order:
            v_phen = [p for p in phen_rows if p["verse_id"] == vid]
            if not v_phen:
                continue
            L.append(f"### {verses[vid]['osisId']}")
            L.append("")
            for p in v_phen:
                hib = hib_rows.get(p["hib_id"])
                label = hib["label"] if hib else f"hib_id={p['hib_id']}"
                L.append(f"- **{label}** [{p['status']}]: {p['description']}")
                if p["textual_warrant"]:
                    L.append(f"  - warrant: {p['textual_warrant']}")
            L.append("")

    L += ["## Per-verse operations (Phase 2)", ""]
    if not op_rows:
        L += ["(none written yet)", ""]
    else:
        for vid in verse_order:
            v_phen = [p for p in phen_rows if p["verse_id"] == vid]
            v_ops = [(p, op_by_phen[p["id"]]) for p in v_phen if p["id"] in op_by_phen]
            if not v_ops:
                continue
            L.append(f"### {verses[vid]['osisId']}")
            L.append("")
            for p, op in v_ops:
                hib = hib_rows.get(p["hib_id"])
                label = hib["label"] if hib else f"hib_id={p['hib_id']}"
                L.append(f"**{label}** — *{op['action_type'] or '(no action-type)'}* "
                         f"[{op['decision'] or '(no decision)'}]")
                if op["observation_text"]:
                    L.append(f"- Observation: {op['observation_text']}")
                L.append(f"- Process: {op['process'] or '(none)'}")
                for party in parties_by_op.get(op["id"], []):
                    tag = "Source" if party["role"] == "source" else "Target"
                    enab = " (enablement only)" if party["enablement_only"] else ""
                    L.append(f"- {tag}: {party['kind']}"
                             f"{' — ' + party['detail'] if party['detail'] else ''}{enab}")
                if op["description_text"]:
                    L.append(f"- Description: {op['description_text']}")
                L.append("")

    L += ["## Passage-level linkages (Q7)", ""]
    if not linkages:
        L += ["No linkages recorded.", ""]
    else:
        for lk in linkages:
            L.append(f"- operation {lk['from_operation_id']} → operation {lk['to_operation_id']}: "
                     f"{lk['note']}")
        L.append("")

    L += ["## Insufficiencies register", ""]
    if not insufficiencies:
        L += ["None recorded.", ""]
    else:
        for i in insufficiencies:
            where = f" ({i['osisId']})" if i["osisId"] else ""
            L.append(f"- {i['note']}{where}")
        L.append("")

    L += ["## Emergent questions log", ""]
    if not emergent:
        L += ["None recorded.", ""]
    else:
        for e in emergent:
            where = f" ({e['osisId']})" if e["osisId"] else ""
            L.append(f"- [{e['kind']}]{where}: {e['question_text']}")
        L.append("")

    L += ["## Debate quality validation (Phase 3)", ""]
    if not validation:
        L += ["No validation pass recorded yet.", ""]
    else:
        for v in validation:
            tag = "corrected" if v["corrected"] else "noted, not yet corrected"
            phen_ref = f" (phenomenon {v['phenomenon_id']})" if v["phenomenon_id"] else ""
            L.append(f"- [{tag}]{phen_ref}: {v['finding_text']}")
        L.append("")

    L += ["## Open decisions / next steps", ""]
    L += [open_decisions or "(none recorded)", ""]

    return L, debate_status, pid


def _may_write_passage(conn: sqlite3.Connection) -> bool:
    """Grant-checked, same principle as every other write in this app (`_may`/`_grant`) even
    though this is a standalone tool with no `Ctx`/dispatcher — a write is a write."""
    return conn.execute(
        "SELECT 1 FROM cfg_write_grant WHERE writer='report.debate' AND table_name='passage' "
        "AND inactive=0").fetchone() is not None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True)
    ap.add_argument("--chapters", help="whole-chapter range, e.g. 1-3 or 1")
    ap.add_argument("--range", dest="vrange", help="single-chapter verse range, e.g. 8:1-27")
    ap.add_argument("--book-label", default=None,
                    help="human-facing subfolder name (e.g. Daniel) -- defaults to --book if omitted, "
                         "same shape as VerseLexical.ps1/-BookLabel")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    if bool(args.chapters) == bool(args.vrange):
        ap.error("give exactly one of --chapters or --range")

    cfg = Cfg()
    try:
        if args.vrange:
            ch, vlo, vhi = parse_range(args.vrange)
            lo = hi = ch
            try:
                lines, debate_status, passage_id = build(cfg.conn, args.book, lo, hi, vlo, vhi)
            except ValueError as e:
                print(f"cannot build: {e}")
                return 1
            topic = f"{args.book.lower()}-{ch}-{vlo}-{vhi}-debate-report"
        else:
            lo, hi = parse_chapters(args.chapters)
            try:
                lines, debate_status, passage_id = build(cfg.conn, args.book, lo, hi)
            except ValueError as e:
                print(f"cannot build: {e}")
                return 1
            topic = f"{args.book.lower()}-{args.chapters}-debate-report"

        if args.out:
            out_path = Path(args.out)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            text = "\n".join(lines)
            if not text.endswith("\n"):
                text += "\n"
            out_path.write_text(text, encoding="utf-8")
        else:
            # Book-scoped filing (fixed 2026-08-08) -- same convention every sibling book tool uses:
            # report.verse_analysis_output_dir/<book_label or book>/<topic>.md, versioned +
            # archived-on-regenerate by write_report (not the flat oneoff_path this used to call).
            output_dir = pathlib.Path(cfg.setting("report.verse_analysis_output_dir",
                                                   "iba/app/verse-analysis"))
            folder = args.book_label or args.book
            out_path = output_dir / folder / f"{topic}.md"
            out_path = reportkit.write_report(cfg.conn, "report.debate", out_path, lines)
        print(f"wrote {out_path}")

        # 2026-08-06: this report is no longer purely read-only -- it keeps passage.debate_path/
        # debate_written_at/debate_status current for new-model passages, the same tracking the
        # legacy report.passage_debate scaffold+PassageDebate-Sync.ps1 dance kept for old ones,
        # but in one call instead of two (nothing here is a static file needing a separate human
        # "confirm you filled it in" step -- status is recomputed from the DB every regenerate).
        if not _may_write_passage(cfg.conn):
            print("NOTE: report.debate -> passage write grant not active -- tracking columns "
                  "(debate_path/debate_written_at/debate_status) NOT updated this run.")
        else:
            import datetime
            now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            cfg.conn.execute(
                "UPDATE passage SET debate_path=?, debate_written_at=?, debate_status=? "
                "WHERE id=?", (str(out_path), now, debate_status, passage_id))
            cfg.conn.commit()
            print(f"passage {passage_id}: debate_status -> {debate_status!r}")
    finally:
        cfg.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
