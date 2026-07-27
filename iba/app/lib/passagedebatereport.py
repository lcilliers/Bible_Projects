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

from . import reportkit
from .versespanmeaningreport import fetch_verses, parse_chapters, parse_range, _range_str


class BaseExtractMissing(Exception):
    """The verse-span-meaning extract this range's debate depends on does not exist yet."""


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


def _verse_block(v: dict) -> list[str]:
    """One verse's scaffold: heading, quoted text, and empty Observation/Operation/
    Interrogative/Decision slots in the Subject/Operation/Source/Target shape
    (`WA-dan-2-1-16-debate` is the format standard, per the corpus review)."""
    L = [f"### {v['reference']}", "", f"> {v['text'] or ''}", "",
        "**Observation.** <!-- what the text/span-data states; cite Strong's codes -->", "",
        "**Operation 1 — <!-- short label --> .**",
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
        "**Interrogative — questions considered.** (`WA-interpretation-questions` Q1-Q11 — "
        "every human mentioned in this verse is a presumptive candidate, per read-guidance "
        "step 2 note (f); a candidate that resolves to nothing is recorded as an explicit "
        "silence, per Part B.4, not omitted)",
        "- Q1/Q2: <!-- focused inner being? implied interior? -->",
        "- Q3: <!-- stated or inferred -->", "- Q4: <!-- source of state vs source of enablement -->",
        "- Q5: <!-- target -->", "- Q6: <!-- state or movement -->", "- Q7: <!-- linkage, or absence surfaced -->",
        "- Q8: <!-- collective, if applicable -->", "- Q9: <!-- sufficiency -->",
        "- Q11: <!-- action-type label, independent of Q1-Q9's outcome -->", "",
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
    extract_pattern = cfg.setting("report.verse_analysis_output_pattern",
                                  "{book}-{range}-verse-span-meaning.md")
    extract_path = output_dir / folder / extract_pattern.format(book=book.lower(), range=range_str)
    if not extract_path.exists():
        raise BaseExtractMissing(
            f"{extract_path} does not exist — run VerseSpanMeaning-Report.ps1 for this exact "
            f"book/range first (report.verse_span_meaning); the debate scaffold reads verse text "
            f"from the DB but its own base-data citation and the analyst's workflow both depend "
            f"on that extract existing first")

    verses = fetch_verses(conn, book, lo, hi, verse_lo, verse_hi)

    today = datetime.date.today().isoformat()
    pattern = cfg.setting("report.passage_debate_naming_pattern", "WA-{book}-{range}-debate.md")
    filename = pattern.format(book=book.lower(), range=range_str)
    path = output_dir / folder / filename

    intro = [
        f"**Filename:** {filename}",
        f"**Date timestamp:** {today}",
        f"**Previous outputs referenced:** base data `{extract_path.name}`; "
        f"method `{guidance_path.name}`; interrogative `{interrogative_path.name}`.",
        "",
        "**Version:** 1.0 (auto-generated scaffold — no interpretive content yet)",
        "**Change-control note:** Generated by `report.passage_debate`. Structure only — the "
        "Observation/Operation/Interrogative/Decision content for each verse below must be filled "
        "in by applying the method + interrogative docs cited above. This file is not a finished "
        "debate until every `<!-- fill in -->` placeholder is replaced.",
    ]

    preliminaries = [
        "**Working scope (declared as assumption, not fact).** <!-- fill in — what counts as "
        "bearing on the inner being for this passage -->", "",
        "**Reading rule applied.** <!-- fill in — e.g. [AMBIGUOUS]-span STEP-live precedence, "
        "any range-specific reading rule -->", "",
        "**Corpus-continuity check.** <!-- before writing this debate, read the debate(s) "
        "covering the immediately adjacent prior range in this book; note here that this was "
        "done, per the corpus review's process-gap finding -->",
    ]

    verse_lines: list[str] = []
    for v in verses:
        verse_lines += _verse_block(v)

    linkages = ["<!-- fill in — Q7: linkages across this passage's operations, and surfaced "
               "non-linkages -->"]
    insufficiencies = ["<!-- fill in — Q9: data the base extract does not carry, named not "
                      "filled -->"]
    emergent = ["<!-- fill in — EQ items raised by this passage; filed here, resolved (if at "
               "all) at the whole-book read, not merged with other passages' logs -->"]
    open_decisions = ["<!-- fill in — forks left to the researcher, next steps -->"]

    sections = {
        "preliminaries": preliminaries,
        "verses": verse_lines,
        "linkages": linkages,
        "insufficiencies": insufficiencies,
        "emergent": emergent,
        "open_decisions": open_decisions,
    }

    L = reportkit.render_scaffold(conn, "report.passage_debate", sections, intro=intro,
                                  book=book, range=label)
    reportkit.write_report(conn, "report.passage_debate", path, L)
    return path
