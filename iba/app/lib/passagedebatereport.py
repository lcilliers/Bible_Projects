"""passagedebatereport.py — registers the passage-debate method (`WA-passage-read-guidance` +
`WA-interpretation-questions`, see `iba/docs/`) as a real report step (`report.passage_debate`),
matching the pattern `versespanmeaningreport.py` set for `report.verse_span_meaning`.

**What this mechanises, and what it deliberately does not.** The debate itself — applying the
Q1-Q10 interrogative to a verse, deciding what's stated vs inferred, naming an operation's
subject/source/target — is analytical work an AI does against the method docs, not something a
DB-driven renderer can produce (same boundary CLAUDE.md draws everywhere else: Claude Code is the
DB/mechanical engine, Claude AI/the researcher is the analytical layer). What this module DOES
mechanise is everything the corpus review (`iba/app/reports/dan-debate-method-assessment-
20260727.md`) found was going wrong for reasons that have nothing to do with interpretation:
the base extract not being checked for first, the current method-doc version not being resolved
from a stable source, the Subject/Operation/Source/Target parts drifting into free prose instead
of an extractable block, and inconsistent file naming/versioning. All of that is now enforced by
the scaffold this module writes, not left to memory.

Reads `method.passage_read_guidance_path` / `method.interpretation_questions_path` (module
`method`, new — the CURRENT version of each doc, config-driven per `governance.
rules_must_be_config_driven` rather than a citation an AI has to remember or a debate's own
front-matter asserting a version that was never bumped on disk, which is exactly the gap the
corpus review found: every debate cited "v1.1" of the read guidance when no such file existed).

Output path/naming reuses `report.verse_analysis_output_dir` (the extract and its debate live in
the same book folder) + a new `report.passage_debate_naming_pattern` (module `report`, stable
scheme — `reportkit.write_report` archives the prior version on regenerate, same as
`report.verse_span_meaning`; no `-vN-`/date in the name itself, unlike the ad-hoc convention the
four hand-authored debates used before this was registered — see BUILD.md for the reconciliation
note on those four pre-existing files).
"""

from __future__ import annotations

import datetime
import pathlib
import sqlite3

from . import passagetrack, reportkit
from .versespanmeaningreport import (detect_verse_gaps, fetch_verses, gap_note,
                                     merge_verses_and_gaps, parse_chapters, parse_range,
                                     _range_str)


class BaseExtractMissing(Exception):
    """The verse_lexical data this range's debate depends on has not been built yet. Was a
    filesystem check against report.verse_span_meaning's MD output (extract_path.exists()) —
    swapped 2026-08-05 to a DB check against verse_lexical, the mechanical-lexical replacement
    (report.verse_span_meaning is retired; see t1-t3-design-decisions-20260805.md — "T1-T3" there
    is this table's original dev-only name, retired in favour of "the lexical" per the
    researcher's own terminology, same day). Digesting the full analytic method (HIB/phenomenon/
    operation) into this scaffold is separate follow-on work — see
    debate-analytic-process-digest-20260805.md — this change only swaps the existence gate."""


class MethodDocMissing(Exception):
    """A method.* cfg_setting points at a file that isn't on disk."""


def _method_doc(cfg, key: str) -> pathlib.Path:
    raw = cfg.setting(key)
    if not raw:
        raise MethodDocMissing(f"{key!r} has no cfg_setting value — run the bootstrap migration")
    path = pathlib.Path(raw)
    if not path.exists():
        raise MethodDocMissing(f"{key!r} points to {path} which does not exist on disk — "
                               f"the config is stale relative to iba/docs/")
    return path


def _phenomena_block(v: dict) -> list[str]:
    """Phase 1 scaffold, per verse: heading, quoted text, and an empty phenomena-register slot —
    one entry per inner being present, with its textual warrant and stated-vs-inferred status,
    written BEFORE any operation (`WA-passage-read-guidance-v1.5` Phase 1, steps 1-3b)."""
    return [f"### {v['reference']}", "", f"> {v['text'] or ''}", "",
        "**Phenomena identified (Phase 1).** <!-- for EVERY inner being present (read-guidance "
        "step 2 note (f): every human is a presumptive candidate; note (b)/(d): an in-scope "
        "non-human), isolate the phenomenon — a state, disposition, or characteristic of that "
        "party's inner life, which may be hidden behind a stated act or a refrained-from act "
        "(step 3 note (e)) — and record, per inner being, its own entry: the phenomenon; the "
        "specific textual warrant that grounds it (the verb, clause, or stated silence, step 3b); "
        "and whether it is stated or inferred (Q3). \"No phenomenon found, silent\" (Part B.4) is "
        "a valid entry, not an omission. Do NOT draft an operation here — operations are Phase 2 "
        "(see this verse's entry under 'Per-verse operations' below), written only once this "
        "register is complete for the WHOLE debated range. -->", ""]


def _operations_block(v: dict) -> list[str]:
    """Phase 2 scaffold, per verse: heading, quoted text, and empty Observation/Operation/
    Interrogative/Decision slots in the Subject/Operation/Source/Target shape
    (`WA-dan-2-1-16-debate` is the format standard, per the corpus review). An operation here
    must originate from a phenomenon already recorded in the phenomena register above — it may
    not identify a fresh phenomenon of its own accord (`WA-passage-read-guidance-v1.5` Phase 2;
    Part B.12)."""
    L = [f"### {v['reference']}", "", f"> {v['text'] or ''}", "",
        "**Observation.** <!-- what the text/span-data states; cite Strong's codes -->", "",
        "**Operation 1 — <!-- short label --> .** <!-- for the phenomenon already recorded in "
        "the phenomena register above; a mismatch here signals the register entry needs "
        "correcting, not a licence to invent a new phenomenon -->",
        "- **Action-type:** <!-- short, consistent, verb-based label for what was done (e.g. "
        "\"gave,\" \"summoned/complied,\" \"worshiped,\" \"renamed,\" \"bound and cast\") — "
        "recorded regardless of whether this operation's interior content is stated, inferred, "
        "or a recorded silence; a label, not a taxonomy — read-guidance step 5 note (a), "
        "interrogative Q11/B.10 -->",
        "- **Subject:** <!-- the human (or in-scope non-human, note (b)/(d)) in focus -->",
        "- **Operation:** <!-- state/status, or movement: come from/go to/impact on/emerge/"
        "go away/become evident -->",
        "- **Source:** <!-- self / another human / non-human being / object-situation; "
        "state vs enablement kept distinct, Part B.5 -->",
        "- **Target:** <!-- another operation/human/non-human/object-situation, or n/a -->", "",
        "**Interrogative — questions considered.** (`WA-interpretation-questions` Q1-Q12 — "
        "every human mentioned in this verse is a presumptive candidate, per read-guidance "
        "step 2 note (f); a candidate that resolves to nothing is recorded as an explicit "
        "silence, per Part B.4, not omitted)",
        "- Q1/Q2: <!-- focused inner being? implied interior? -->",
        "- Q3: <!-- stated or inferred -->", "- Q4: <!-- source of state vs source of enablement -->",
        "- Q5: <!-- target -->", "- Q6: <!-- state or movement -->", "- Q7: <!-- linkage, or absence surfaced -->",
        "- Q8: <!-- collective, if applicable -->", "- Q9: <!-- sufficiency -->",
        "- Q11: <!-- action-type label, independent of Q1-Q9's outcome -->",
        "- Q12: <!-- divine mirroring, only where textually anchored (Part B.11); otherwise "
        "log as an emergent question instead of asserting it -->", "",
        "**Decision.** <!-- retain / set aside as stated IB op / retain as referential aspect / "
        "recorded silence -->", ""]
    return L


def write_scaffold(cfg, book: str, lo: int, hi: int, verse_lo: int | None = None,
                   verse_hi: int | None = None, book_label: str | None = None) -> pathlib.Path:
    conn: sqlite3.Connection = cfg.conn
    guidance_path = _method_doc(cfg, "method.passage_read_guidance_path")
    interrogative_path = _method_doc(cfg, "method.interpretation_questions_path")

    range_str = _range_str(lo, hi, verse_lo, verse_hi)
    label = f"{lo}:{verse_lo}-{verse_hi}" if verse_lo is not None else f"{lo}-{hi}"
    folder = book_label or book

    output_dir = pathlib.Path(cfg.setting("report.verse_analysis_output_dir",
                                          "iba/app/verse-analysis"))

    verses = fetch_verses(conn, book, lo, hi, verse_lo, verse_hi)
    built_verse_ids = {r["verse_id"] for r in conn.execute(
        "SELECT DISTINCT verse_id FROM verse_lexical WHERE deleted=0 AND verse_id IN "
        f"({','.join('?' * len(verses))})", [v["id"] for v in verses]).fetchall()} if verses else set()
    missing = [v["reference"] for v in verses if v["id"] not in built_verse_ids]
    if missing:
        raise BaseExtractMissing(
            f"verse_lexical has no rows for {len(missing)} of {len(verses)} verse(s) in this range "
            f"({missing[0]}{' ...' if len(missing) > 1 else ''}) — run VerseLexical.ps1 for "
            f"this exact book/range first (lexical.build); the debate scaffold reads verse "
            f"text from the DB directly but the analyst's workflow depends on the resolved "
            f"lexical reading existing first")
    extract_label = "verse_lexical (DB)"

    today = datetime.date.today().isoformat()
    pattern = cfg.setting("report.passage_debate_naming_pattern", "WA-{book}-{range}-debate.md")
    filename = pattern.format(book=book.lower(), range=range_str)
    path = output_dir / folder / filename

    intro = [
        f"**Filename:** {filename}",
        f"**Date timestamp:** {today}",
        f"**Previous outputs referenced:** base data `{extract_label}`; "
        f"method `{guidance_path.name}`; interrogative `{interrogative_path.name}`.",
        "",
        "**Version:** 1.0 (auto-generated scaffold — no interpretive content yet)",
        "**Change-control note:** Generated by `report.passage_debate`. Structure only — the "
        "Observation/Operation/Interrogative/Decision content for each verse below must be filled "
        "in by applying the method + interrogative docs cited above. This file is not a finished "
        "debate until every `<!-- fill in -->` placeholder is replaced.",
    ]

    prior = passagetrack.find_prior_debate(conn, book, verses[0]["chapter"], verses[0]["verse"])
    if prior:
        continuity_line = (
            f"**Corpus-continuity check.** Immediately-adjacent prior range, found automatically: "
            f"`{prior['ref']}` — `{prior['debate_path']}`. <!-- read it in full before drafting "
            f"this debate, per the corpus review's process-gap finding; confirm here that this "
            f"was done, and note anything it carries forward (open decisions, emergent questions, "
            f"threads that bear on this range) -->"
        )
    else:
        continuity_line = (
            "**Corpus-continuity check.** No prior filled debate found for this book at or before "
            "this range — this is the first debate in the sequence (or nothing precedes it yet). "
            "Nothing to re-read."
        )

    preliminaries = [
        "**Working scope (declared as assumption, not fact).** <!-- fill in — what counts as "
        "bearing on the inner being for this passage -->", "",
        "**Reading rule applied.** <!-- fill in — e.g. [AMBIGUOUS]-span STEP-live precedence, "
        "any range-specific reading rule -->", "",
        continuity_line,
    ]

    gaps = detect_verse_gaps(verses, verse_lo)
    merged = list(merge_verses_and_gaps(verses, gaps))
    phenomena_lines: list[str] = []
    operations_lines: list[str] = []
    for ch, vn, kind, v in merged:
        if kind == "verse":
            phenomena_lines += _phenomena_block(v)
            operations_lines += _operations_block(v)
        else:
            note = gap_note(cfg, book, book_label, ch, vn)
            phenomena_lines += [note, ""]
            operations_lines += [note, ""]

    linkages = ["<!-- fill in — Q7: linkages across this passage's operations, and surfaced "
               "non-linkages -->"]
    insufficiencies = ["<!-- fill in — Q9: data the base extract does not carry, named not "
                      "filled -->"]
    emergent = ["<!-- fill in — EQ items raised by this passage (including interpretive forks, "
               "Part B.9, and any genuine literary/structural observation per Part B.12 — logged "
               "here, never built into the phenomena register or an operation as if it were "
               "their own content); filed here, resolved (if at all) at the whole-book read, not "
               "merged with other passages' logs -->"]
    validation = ["<!-- fill in — Phase 3 (`WA-passage-read-guidance-v1.5` step 6): once the "
                 "phenomena register and per-verse operations above are complete for the whole "
                 "range, reconsider — for each phenomenon, or at minimum a representative sample "
                 "spanning the range — whether it is genuinely an inner-being phenomenon (not a "
                 "textual/structural pattern mislabeled as one, Part B.12), whether its Phase 1 "
                 "justification actually warrants it from the verse's own text, and whether its "
                 "Phase 2 operation tracks faithfully back to it. Correct any failure found before "
                 "the debate is considered filled — do not merely log it for later. -->"]
    open_decisions = ["<!-- fill in — forks left to the researcher, next steps -->"]

    sections = {
        "preliminaries": preliminaries,
        "phenomena_register": phenomena_lines,
        "operations": operations_lines,
        "linkages": linkages,
        "insufficiencies": insufficiencies,
        "emergent": emergent,
        "validation": validation,
        "open_decisions": open_decisions,
    }

    L = reportkit.render_scaffold(conn, "report.passage_debate", sections, intro=intro,
                                  book=book, range=label)
    path = reportkit.write_report(conn, "report.passage_debate", path, L)
    return path
