"""wholebookread.py — registers the whole-book-read step (`report.whole_book_read`) as a real
report generator, matching the pattern `passagedebatereport.py` set for `report.passage_debate`.

**Why this exists.** Every passage-debate document defers its "Emergent questions log" to "the
whole-book read" — a phrase repeated across all sixteen Daniel debates — but until now no such
step existed anywhere in `cfg_work_package`; the deferral had nowhere to land. At least one
Daniel EQ was in fact answered several chapters later (Dan 2's "does coerced worship ever reveal
genuine disposition?" answered at Dan 3:28) with no step ever formally closing that loop; it only
surfaced because all sixteen files were read by hand in one sitting for an unrelated task.

**What this mechanises, and what it deliberately does not** (same boundary
`passagedebatereport.py`'s own docstring draws, and the same reasoning applies here): gathering
every filled debate for a book, extracting each one's "Emergent questions" and "Passage-level
linkages" sections, and laying them out together in one scaffold IS mechanised — that's plumbing,
not judgment. Deciding whether/how a given emergent question actually got resolved by a later
passage is NOT mechanised; the scaffold leaves that as prose for the researcher/AI to write, the
same way `passagedebatereport.py` leaves Observation/Operation/Decision content unfilled.

**Heading drift is real, not hypothetical — confirmed twice, not just anticipated.** Reading all
sixteen Daniel files directly found real inconsistency: most files head their closing sections
"## Emergent questions log" / "## Passage-level linkages (Q7)"; `WA-dan-2-1-16-debate` instead uses
"## Emergent-questions log" / "## Linkages surfaced (and non-linkages)"; `WA-dan-1-1-7-debate` uses
the SINGULAR "## Passage-level linkage (stated once — Q7)" (found only on the first real run
against Daniel, after the first two variants were already handled — see BUILD.md §32); the exact
parenthetical after "Emergent questions log" varies file to file too (some say "not merged across
passages," others "not merged with other passages' logs," others "filed against this passage
only"). `_extract_section` below matches on a tolerant PREFIX of the heading line, not the full
heading text, and captures everything up to the next `##`-level heading (or end of file) — a file
whose heading doesn't match any known pattern gets an explicit "NOT FOUND" marker in the output,
never a silent gap. Given three distinct variants found across sixteen files in one book, more
should be expected, not treated as exhausted — the NOT-FOUND path is the actual safety net here,
not the pattern list.
"""

from __future__ import annotations

import datetime
import pathlib
import re
import sqlite3

from . import passagetrack, reportkit

# Known-historical tolerant variants — kept because past debate files were genuinely written with
# these headings (see module docstring). NOT the single source of truth for "what heading does
# report.passage_debate write today" — that's `cfg_report_section.heading` (step
# 'report.passage_debate', section_key 'emergent'/'linkages'), read live in `_heading_pattern()`
# below and always folded in as an extra alternative. Found 2026-07-29: before this fix, these two
# were the ONLY source of truth for what this reader accepts — a `configmaint.propose` change to
# `report.passage_debate`'s own heading config could silently desync this reader from its writer,
# the same failure shape BUILD.md §33 already hit once by hand.
_EQ_HEADING_FALLBACK = r"^##\s+Emergent[- ]questions?\s+log"
_LINKAGE_HEADING_FALLBACK = r"^##\s+(Passage-level linkages?|Linkages surfaced)"
NEXT_H2_RE = re.compile(r"^##\s+\S", re.MULTILINE)


def _heading_pattern(conn: sqlite3.Connection, section_key: str, fallback: str) -> re.Pattern:
    """The live `cfg_report_section.heading` for `report.passage_debate`/`section_key`, folded in
    as an extra alternative alongside the known-historical fallback pattern — so a future change to
    that heading's config can never silently stop matching here."""
    row = conn.execute(
        "SELECT heading FROM cfg_report_section WHERE step='report.passage_debate' "
        "AND section_key=?", (section_key,)).fetchone()
    branches = [fallback]
    if row and row["heading"]:
        literal = re.sub(r"^#+\s*", "", row["heading"]).strip()
        if literal:
            branches.append(r"^##\s+" + re.escape(literal))
    return re.compile("(?:" + ")|(?:".join(branches) + ")", re.IGNORECASE | re.MULTILINE)


class NoDebatesFound(Exception):
    """No `debate_status='filled'` passage row exists yet for this book — nothing to gather."""


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _extract_section(text: str, heading_re: re.Pattern) -> str | None:
    """Everything between a heading matching `heading_re` (exclusive of the heading line itself)
    and the next `##`-level heading (or end of file). `None` if `heading_re` doesn't match at
    all — the caller is responsible for surfacing that as a NOT-FOUND, not skipping silently."""
    m = heading_re.search(text)
    if not m:
        return None
    body_start = text.index("\n", m.end()) + 1 if "\n" in text[m.end():] else len(text)
    nxt = NEXT_H2_RE.search(text, body_start)
    body = text[body_start: nxt.start() if nxt else len(text)]
    return body.strip("\n ")


def gather_book(conn: sqlite3.Connection, book: str) -> list[dict]:
    """One entry per filled debate for `book`, in reading order — each carrying its own EQ text
    (or None) and linkages text (or None), read straight off disk. Raises `NoDebatesFound` if
    the book has no filled debate yet."""
    rows = passagetrack.all_debated_ranges(conn, book)
    if not rows:
        raise NoDebatesFound(
            f"no debate_status='filled' passage row exists for book {book!r} — run at least one "
            f"report.passage_debate pass and fill it in before a whole-book read makes sense")
    eq_re = _heading_pattern(conn, "emergent", _EQ_HEADING_FALLBACK)
    linkage_re = _heading_pattern(conn, "linkages", _LINKAGE_HEADING_FALLBACK)
    out = []
    for r in rows:
        path = pathlib.Path(r["debate_path"])
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        out.append({
            "ref": r["ref"],
            "path": r["debate_path"],
            "exists": path.exists(),
            "eq": _extract_section(text, eq_re) if text else None,
            "linkages": _extract_section(text, linkage_re) if text else None,
        })
    return out


def _render(book: str, entries: list[dict]) -> dict[str, list[str]]:
    total_files = len(entries)
    coverage = [
        f"- **{total_files}** filled debate(s) gathered for `{book}`, in reading order:",
        "",
    ] + [f"  1. `{e['ref']}` — `{e['path']}`" for e in entries]

    carried: list[str] = []
    not_found: list[str] = []
    for e in entries:
        carried += [f"### {e['ref']}", ""]
        if not e["exists"]:
            carried += ["*(file not found on disk at the recorded path — nothing to carry "
                       "forward from this range until it's regenerated)*", ""]
            not_found.append(f"- `{e['ref']}` (`{e['path']}`) — file missing on disk")
            continue
        if e["eq"] is None:
            carried += ["**Emergent questions.** NOT FOUND — verify heading (see this file's "
                       "own closing sections manually).", ""]
            not_found.append(f"- `{e['ref']}` — no \"Emergent questions log\" heading matched")
        elif e["eq"]:
            carried += ["**Emergent questions (as filed).**", "", e["eq"], ""]
        else:
            carried += ["**Emergent questions.** Section found, empty — none filed.", ""]
        if e["linkages"] is None:
            carried += ["**Passage-level linkages.** NOT FOUND — verify heading (see this file's "
                       "own closing sections manually).", ""]
            not_found.append(f"- `{e['ref']}` — no \"Passage-level linkages\" heading matched")
        elif e["linkages"]:
            carried += ["**Passage-level linkages (as filed).**", "", e["linkages"], ""]
        else:
            carried += ["**Passage-level linkages.** Section found, empty — none filed.", ""]
        carried += ["**Resolution.** <!-- fill in — for each item above: does a later passage in "
                   "this book answer it, contradict it, or does it stay open past this book? "
                   "Point back to the specific verse/passage that resolves it, if any -->", ""]

    not_found_lines = (not_found if not_found else
                       ["None — every gathered file's Emergent-questions and "
                        "Passage-level-linkages sections were found by heading."])

    closing = ["<!-- fill in — once every item above has a Resolution, a short closing synthesis: "
              "what recurred across the whole book, what never resolved, what's left genuinely "
              "open past the last chapter -->"]

    return {"coverage": coverage, "carried_forward": carried,
           "not_found": not_found_lines, "closing": closing}


def write_scaffold(cfg, book: str, book_label: str | None = None) -> pathlib.Path:
    conn: sqlite3.Connection = cfg.conn
    entries = gather_book(conn, book)
    folder = book_label or book

    output_dir = pathlib.Path(cfg.required_setting("report.verse_analysis_output_dir"))
    pattern = cfg.required_setting("report.whole_book_read_naming_pattern")
    filename = pattern.format(book=book.lower())
    path = output_dir / folder / filename

    intro = [
        f"> Generated {_now()} by `report.whole_book_read`. Gathers every filled "
        f"`report.passage_debate` output for `{book}` — plumbing only; the resolutions below are "
        f"for the researcher/AI to write, not generated.",
    ]
    sections = _render(book, entries)
    L = reportkit.render_scaffold(conn, "report.whole_book_read", sections, intro=intro,
                                  book=book_label or book)
    path = reportkit.write_report(conn, "report.whole_book_read", path, L)
    return path
