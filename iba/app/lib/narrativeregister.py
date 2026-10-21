"""narrativeregister.py -- the narrative claim register in iba.db (escalation #2110).

Specification: `_analytics/essay/spirit_soul_body/wa-essay-narrative-record-
db-specification-v1-20261013.md`. A **claim** is a statement derived from sources that goes beyond
their mere text, held in its own wording; the **narrative** is the story, recorded here only as the
**passages** that tell claims; claims and passages are joined many to many. Every change keeps its
before and after: the history triggers (cfg_trigger, `trg_narrative_*`) write
`narrative_claim_change` rows on any edit, direct or through this module; this module then marks
the rows it caused as `basis='recorded'` with its own provenance (and the update, for Record).

Parts:
  references   parse_refs()      chapter/register references -> verse rows (alias map in config)
  chapters     parse_chapter()   a chapter file -> sections and passages (paragraphs, bullets, rows)
  actions      add_claim, edit, tell, untell, withdraw, edit_note, add_chapter, edit_chapter,
               edit_section, record   (chapters: #2155, the chapter table is the authority)
  read-only    find, history, check
  publishing   export            the three fixed-name files (spec sec8)

Every action validates first and raises Refused before any write; a refusal inside a write is
rolled back to the action's savepoint, so a refusal writes nothing (spec sec5, test plan sec4).
Write grants: each write goes through _w(), which checks the step's cfg_write_grant rows.
"""
from __future__ import annotations

import dataclasses
import datetime
import json
import pathlib
import re
import sqlite3

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[3]
PUBLISHED_HEADER = ("*Published from iba.db on {date}. Edit the register in the database "
                    "(`Narrative-Register.ps1`); changes made only in this file are not kept.*")


class Refused(Exception):
    """A usage refusal: the action wrote nothing. Routed to cfg_on_fail condition 'refused'."""


# ══ helpers ═════════════════════════════════════════════════════════════════════════════════════
def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _today() -> str:
    return _now()[:10]


def _check_enum(allowed: list[str], value: str | None, what: str) -> None:
    if value is not None and value not in allowed:
        raise Refused(f"{what} {value!r} is not one of {allowed}")


class Writer:
    """Write access for one step: every write checks that step's cfg_write_grant rows."""

    def __init__(self, conn: sqlite3.Connection, step: str, who: str):
        self.conn, self.step, self.who = conn, step, who
        self.allowed = {r[0] for r in conn.execute(
            "SELECT table_name FROM cfg_write_grant WHERE writer=? AND database='iba' AND inactive=0",
            (step,))}
        self.unresolved: list[str] = []        # references written that match no verse (#2134)

    def _grant(self, table: str) -> None:
        if table not in self.allowed:
            raise PermissionError(f"write-grant violation: {self.step!r} may not write {table!r}")

    def insert(self, table: str, row: dict) -> int:
        self._grant(table)
        row = {**row}
        row.setdefault("created_by", self.who)
        cols = list(row)
        cur = self.conn.execute(
            f'INSERT INTO "{table}" ({",".join(chr(34) + c + chr(34) for c in cols)}) '
            f'VALUES ({",".join("?" * len(cols))})', [row[c] for c in cols])
        return cur.lastrowid

    def update(self, table: str, where: dict, sets: dict) -> int:
        self._grant(table)
        s = ", ".join(f'"{k}"=?' for k in sets)
        w = " AND ".join(f'"{k}"=?' for k in where)
        return self.conn.execute(f'UPDATE "{table}" SET {s} WHERE {w}',
                                 list(sets.values()) + list(where.values())).rowcount

    def move_passages(self, from_section: int, to_section: int) -> int:
        """The current passages of one section row move to another (a heading renamed)."""
        self._grant("narrative_passage")
        return self.conn.execute("UPDATE narrative_passage SET section_id=? WHERE section_id=? AND "
                                 "last_version IS NULL", (to_section, from_section)).rowcount

    def note_unresolved(self, vx: "VerseIndex", row: dict, where: str) -> None:
        """Keep a reference just written that matches no verse, for the output and the escalation."""
        if row.get("source_kind", "verse") == "verse" and unresolved(vx, row.get("ref_normalised") or "",
                                                                    row.get("verse_id")):
            self.unresolved.append(f"{where}: '{row.get('ref_as_written')}' read as {row.get('ref_normalised')}")

    def mark_changes(self, since_id: int, provenance: str, **extra) -> int:
        """Mark the change rows the triggers wrote during this action as recorded by the tool."""
        self._grant("narrative_claim_change")
        sets = {"basis": "recorded", "provenance": provenance, "created_by": self.who, **extra}
        s = ", ".join(f'"{k}"=?' for k in sets)
        return self.conn.execute(
            f"UPDATE narrative_claim_change SET {s} WHERE id > ? AND basis='direct edit' "
            f"AND created_by='trigger'", list(sets.values()) + [since_id]).rowcount


def _max_change_id(conn) -> int:
    return conn.execute("SELECT COALESCE(MAX(id), 0) FROM narrative_claim_change").fetchone()[0]


def _atomic(conn: sqlite3.Connection, fn):
    """Run fn() inside a savepoint; a Refused (or any error) rolls back to it and re-raises."""
    conn.execute("SAVEPOINT narrative_register")
    try:
        result = fn()
    except BaseException:
        conn.execute("ROLLBACK TO narrative_register")
        conn.execute("RELEASE narrative_register")
        raise
    conn.execute("RELEASE narrative_register")
    return result


# ══ references (build step 3; test plan sec3) ═══════════════════════════════════════════════════
@dataclasses.dataclass
class Ref:
    as_written: str            # the reference text as it stands
    normalised: str            # verse.reference form: '1Sa 24:5', or 'Isa 1' for a whole chapter
    verse_id: int | None
    kind: str                  # 'verse' | 'whole chapter'
    start: int = 0             # offset in the parsed text


class VerseIndex:
    """The verse table, read once: reference -> id, and each book's chapter/verse layout."""

    def __init__(self, cfg):
        conn = cfg.conn
        self.alias = dict(cfg.setting("narrative.book_alias_map"))
        self.ids: dict[tuple[str, int, int], int] = {}
        self.last_verse: dict[tuple[str, int], int] = {}
        self.max_chapter: dict[str, int] = {}
        self.osis: dict[str, str] = {}
        self.no_chapter: set[str] = set()      # single-chapter books: verse.reference is 'Obd 12'
        for vid, ref, osis in conn.execute(
                "SELECT id, reference, osisId FROM verse WHERE deleted=0"):
            m = re.fullmatch(r"(\S+) (?:(\d+):)?(\d+)", ref or "")
            o = re.fullmatch(r"[^.]+\.(\d+)\.(\d+)", osis or "")
            if not m or not o:
                continue
            b, c, v = m.group(1), int(o.group(1)), int(o.group(2))
            if m.group(2) is None:
                self.no_chapter.add(b)
            self.ids[(b, c, v)] = vid
            self.last_verse[(b, c)] = max(self.last_verse.get((b, c), 0), v)
            self.max_chapter[b] = max(self.max_chapter.get(b, 0), c)
            if osis:
                self.osis.setdefault(b, osis.split(".")[0])
        order = {r[0]: r[1] for r in conn.execute("SELECT book, ordinal FROM cfg_book_order")}
        self.book_rank = {b: order.get(o, 999) for b, o in self.osis.items()}

    def book(self, token: str) -> str | None:
        return self.alias.get(token.lower().replace(" ", "").replace(".", ""))

    def single_chapter(self, code: str) -> bool:
        return code in self.no_chapter or self.max_chapter.get(code, 0) == 1

    def ref(self, code: str, c: int, v: int) -> str:
        """verse.reference form: '1Sa 24:5'; 'Jude 6' for a single-chapter book."""
        return f"{code} {v}" if code in self.no_chapter else f"{code} {c}:{v}"

    def sort_key(self, normalised: str):
        m = re.fullmatch(r"(\S+) (\d+)(?::(\d+))?", normalised)
        if not m:
            return (999, 0, 0, normalised)
        return (self.book_rank.get(m.group(1), 999), int(m.group(2)), int(m.group(3) or 0), "")


_BOOK = r"(?P<book>Song\sof\s(?:Songs|Solomon)|(?:[123]\s?)?[A-Z][a-z]+)\.?"
_PART = r"\d+(?::\d+)?(?:\s?[–-]\s?\d+(?::\d+)?)?"
# a list or chain part must not be the numeral of the next book ('Jam 1:2, 1 John 3:20'), nor a
# narrative section pointer ('Deuteronomy 28:65-67; 10.1' is Deu 28:65-67 and section 10.1, #2136)
_BODY = rf"(?P<body>{_PART}(?:(?:,\s?|;\s)(?:{_PART})(?![A-Za-z\d]|\s[A-Z][a-z]|\.\d))*)"
_REF_RX = re.compile(rf"(?<![\w.]){_BOOK}\s{_BODY}(?![\d:])")
_FOLLOW_CV = re.compile(r"\((?P<body>\d+:\d+(?:\s?[–-]\s?\d+(?::\d+)?)?(?:,\s?\d+(?::\d+)?)*)\)")
_FOLLOW_V = re.compile(r"\((?:v\.?\s?|vv\.?\s?)?(?P<body>\d+(?:\s?[–-]\s?\d+)?(?:,\s?\d+)*)\)")


def unresolved(vx: VerseIndex, normalised: str, verse_id: int | None) -> bool:
    """A reference that matches no verse row: a verse with no verse_id, or a whole chapter the book
    does not have. An unresolved reference in the narrative is an error and raises an escalation
    (#2134)."""
    if verse_id is not None:
        return False
    m = re.fullmatch(r"(\S+) (\d+)", normalised)
    return not (m and m.group(1) not in vx.no_chapter and (m.group(1), int(m.group(2))) in vx.last_verse)


def raise_unresolved(cfg, db, w: Writer) -> int:
    """One escalation for the unresolved references a write action recorded (#2134)."""
    from . import escalation as esc
    return esc.raise_new(
        cfg, db, short_description="Unresolved verse references in the narrative register",
        source=f"narrativeregister ({w.step})", etype="issue",
        comment=(f"{w.step} wrote {len(w.unresolved)} reference(s) that match no verse row. Researcher, "
                 f"2026-10-13 (#2134), verbatim: \"if the narrative have unresolved references then there "
                 f"is an error and an escalation should be created resolve it.\" Correct each one in its "
                 f"chapter file or claim source (or the reference parser, if it misread the text), then "
                 f"record again:\n" + "\n".join(f"- {u}" for u in w.unresolved)),
        context="iba/app/lib/narrativeregister.py (parse_refs, unresolved); the rows are in "
                "narrative_citation / narrative_claim_source with verse_id NULL; "
                "Narrative-Register.ps1 -Action Check lists every current one",
        assigned_to="Claude", resolution_kind="self_correctable", originator=w.who)


def _expand(vx: VerseIndex, code: str, body: str, ctx_ch: int | None) -> tuple[list[tuple[str, int | None, str]], int | None]:
    """body like '24:5', '2:20–22, 29', '11:1–4; 12:9', '2:17–3:2', '6', '8–9', '1'.
    ctx_ch: the chapter in force before body (for a bare follow-on). Returns
    ([(normalised, verse_id, kind)], last chapter)."""
    out: list[tuple[str, int | None, str]] = []
    ch = ctx_ch
    single = vx.single_chapter(code)
    first = True
    for sep, part in re.findall(r"(^|,\s?|;\s)(" + _PART + r")", body):
        part = part.replace(" ", "")
        a, b = re.split(r"[–-]", part, maxsplit=1) if re.search(r"[–-]", part) else (part, "")
        if ":" in a:
            c1, v1 = (int(x) for x in a.split(":"))
            ch = c1
            if not b:
                out.append(_one(vx, code, c1, v1))
            elif ":" in b:                      # across chapters: 2:17–3:2
                c2, v2 = (int(x) for x in b.split(":"))
                out.extend(_span(vx, code, c1, v1, c2, v2))
                ch = c2
            else:
                out.extend(_span(vx, code, c1, v1, c1, int(b)))
        else:
            n1 = int(a)
            n2 = int(b) if b else None
            plain_chapter = (first and ctx_ch is None) or sep.startswith(";")
            if single and (ch is None or plain_chapter):
                ch = 1
                out.extend(_span(vx, code, 1, n1, 1, n2 or n1))
            elif plain_chapter or ch is None:
                for c in range(n1, (n2 or n1) + 1):
                    out.append((f"{code} {c}", None, "whole chapter"))
                ch = n2 or n1
            else:
                out.extend(_span(vx, code, ch, n1, ch, n2 or n1))
        first = False
    return out, ch


def _one(vx: VerseIndex, code: str, c: int, v: int):
    return (vx.ref(code, c, v), vx.ids.get((code, c, v)), "verse")


def _span(vx: VerseIndex, code: str, c1: int, v1: int, c2: int, v2: int):
    rows = []
    for c in range(c1, c2 + 1):
        lo = v1 if c == c1 else 1
        hi = v2 if c == c2 else max(vx.last_verse.get((code, c), v1 if c == c1 else 0), lo)
        for v in range(lo, hi + 1):
            rows.append(_one(vx, code, c, v))
    return rows


def parse_refs(text: str, vx: VerseIndex, follow_ons: bool = True) -> list[Ref]:
    """Every verse reference in `text` (a passage or a source list), expanded to one Ref per verse.
    A capitalised word that is not a book alias is not a reference and is skipped. Bare follow-ons
    in parentheses -- '(8:12)', '(5)' -- take book (and chapter) from the reference before them in
    the same text (test plan 3.9, 3.10)."""
    hits: list[tuple[int, int, str, list]] = []          # (start, end, as_written, rows)
    last_book, last_ch, last_end = None, None, -1
    events = []
    for m in _REF_RX.finditer(text):
        code = vx.book(m.group("book"))
        if code:
            events.append(("ref", m.start(), m.end(), m, code))
    if follow_ons:
        for rx, kind in ((_FOLLOW_CV, "cv"), (_FOLLOW_V, "v")):
            for m in rx.finditer(text):
                events.append((kind, m.start(), m.end(), m, None))
    events.sort(key=lambda e: e[1])
    taken: list[tuple[int, int]] = []
    for kind, s, e, m, code in events:
        if any(a <= s < b for a, b in taken):
            continue
        if kind == "ref":
            rows, last_ch = _expand(vx, code, m.group("body"), None)
            last_book = code
        elif last_book is None:
            continue
        elif kind == "cv":
            rows, last_ch = _expand(vx, last_book, m.group("body"), last_ch)
        else:
            if last_ch is None:
                continue
            rows, last_ch = _expand(vx, last_book, m.group("body"), last_ch)
        taken.append((s, e))
        hits.append((s, e, m.group(0).strip("()"), rows))
    out: list[Ref] = []
    for s, e, written, rows in hits:
        for normalised, vid, k in rows:
            out.append(Ref(written, normalised, vid, k, s))
    return out


_QUOTE_RX = re.compile(r"[\"“]([^\"”]{6,}?)[\"”]")


def _words(s: str) -> list[str]:
    return re.findall(r"[a-z']+", s.lower().replace("’", "'"))


def quoted(passage: str, verse_text: str | None) -> bool:
    """True when a quotation in the passage carries the verse's words: a run of 4 words (or the
    whole quotation, if shorter and at least 2 words) found in the verse text (test plan 3.15)."""
    if not verse_text:
        return False
    vw = " " + " ".join(_words(verse_text)) + " "
    for q in _QUOTE_RX.findall(passage):
        w = _words(q)
        if len(w) < 2:
            continue
        n = min(4, len(w))
        for i in range(0, len(w) - n + 1):
            if " " + " ".join(w[i:i + n]) + " " in vw:
                return True
    return False


# ══ chapter files ═══════════════════════════════════════════════════════════════════════════════
@dataclasses.dataclass
class Section:
    heading: str
    level: int
    ordinal: int
    parent: int | None          # index into the section list


@dataclasses.dataclass
class Passage:
    section: int                # index into the section list
    ordinal: int
    text: str


_FILE_RX = re.compile(r"^(?P<stem>.+)-v(?P<v>\d+)-(?P<d>\d{8})\.md$")


def file_version(name: str) -> tuple[str, int] | None:
    m = _FILE_RX.match(name)
    return (m.group("stem"), int(m.group("v"))) if m else None


def plain(s: str) -> str:
    """Text for matching: markdown emphasis and bullet markers removed, spaces collapsed."""
    s = re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", "", s)
    s = re.sub(r"[*_`]", "", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def anchor_of(text: str, words: int = 12) -> str:
    return " ".join(plain(text).split(" ")[:words])


def parse_chapter(text: str) -> tuple[str, list[Section], list[Passage]]:
    """(title, sections, passages). Section 0 is the opening (level 0, before the first heading).
    A passage is a paragraph, one bullet (with its continuation lines), one table data row, or one
    block quote."""
    title = ""
    sections = [Section("(opening)", 0, 0, None)]
    passages: list[Passage] = []
    cur = 0
    stack: list[int] = []
    block: list[str] = []
    counts: dict[int, int] = {}

    def add(t: str) -> None:
        t = t.strip()
        if not t:
            return
        counts[cur] = counts.get(cur, 0) + 1
        passages.append(Passage(cur, counts[cur], t))

    def flush() -> None:
        nonlocal block
        if not block:
            return
        if all(l.lstrip().startswith("|") for l in block):
            rows = [l for l in block if not re.fullmatch(r"\s*\|[\s:|-]+\|\s*", l)]
            for r in rows[1:]:          # the first row is the header
                add(r)
        elif re.match(r"\s*(?:[-*+]|\d+\.)\s", block[0]):
            item: list[str] = []
            for l in block:
                if re.match(r"\s*(?:[-*+]|\d+\.)\s", l) and item and not l.startswith("    "):
                    add("\n".join(item))
                    item = []
                item.append(l)
            add("\n".join(item))
        else:
            add("\n".join(block))
        block = []

    for line in text.splitlines():
        h = re.match(r"^(#{1,4})\s+(.*\S)\s*$", line)
        if h:
            flush()
            level = len(h.group(1))
            if level == 1 and not title:
                title = h.group(2)
                continue
            while stack and sections[stack[-1]].level >= level:
                stack.pop()
            sections.append(Section(h.group(2), level, len(sections), stack[-1] if stack else None))
            cur = len(sections) - 1
            stack.append(cur)
        elif not line.strip():
            flush()
        elif re.fullmatch(r"\s*-{3,}\s*", line):
            flush()
        else:
            block.append(line)
    flush()
    return title, sections, passages


def chapter_dir(cfg) -> pathlib.Path:
    return PROJECT_ROOT / cfg.setting("narrative.copy_source_dir")


def opens_with(text: str, opening: str) -> bool:
    """True when `text` opens with the words of `opening`, compared word by word with case,
    quotation marks, emphasis and other punctuation ignored."""
    want = re.findall(r"\w+", plain(opening).lower())
    return bool(want) and re.findall(r"\w+", plain(text).lower())[:len(want)] == want


def find_passage(passages: list[Passage], opening: str) -> list[Passage]:
    return [p for p in passages if opens_with(p.text, opening)]


# ══ lookups ═════════════════════════════════════════════════════════════════════════════════════
def _chapter(conn, no: str, required: bool = True):
    if no is None:
        if required:
            raise Refused("a chapter is required (-Chapter, e.g. 10.1 or 2)")
        return None
    no = str(no).strip()
    rows = conn.execute("SELECT * FROM narrative_chapter WHERE inactive=0 AND chapter_no IN (?, ?)",
                        (no, no.zfill(2) if "." not in no else no)).fetchall()
    if not rows:
        raise Refused(f"chapter {no!r} does not exist (active narrative_chapter rows)")
    return rows[0]


def _claim(conn, ref: str):
    if not ref:
        raise Refused("a claim is required (-Claim, e.g. C-412 or K-2)")
    r = conn.execute("SELECT * FROM narrative_claim WHERE claim_ref=?", (ref.strip(),)).fetchone()
    if r is None:
        raise Refused(f"claim {ref!r} does not exist")
    return r


def _section(conn, chapter_id: int, heading: str | None, required: bool = False):
    if not heading:
        if required:
            raise Refused("a section is required (-Section, the heading text)")
        return None
    r = conn.execute("SELECT * FROM narrative_section WHERE chapter_id=? AND heading=? AND "
                     "last_version IS NULL ORDER BY ordinal", (chapter_id, heading)).fetchone()
    if r is None:
        raise Refused(f"section {heading!r} does not exist in that chapter (current headings)")
    return r


def _chapter_file(cfg, ch) -> pathlib.Path:
    conn = cfg.conn
    p = chapter_dir(cfg) / (ch["current_file"] or "")
    if not ch["current_file"] or not p.is_file():
        raise Refused(f"chapter {ch['chapter_no']}: current file {ch['current_file']!r} is not on disk")
    return p


def _parse_sources(cfg, vx: VerseIndex, spec: str | None) -> list[dict]:
    """-Source 'Rom 7:15-21; lexical: kāʿas (anger); study file: path; science: ref'.
    Items are separated by ' | ' or ';' (a ';' inside a reference chain is kept with it)."""
    conn = cfg.conn
    if not spec:
        return []
    kinds = cfg.enum("narrative_claim_source_kind")
    out: list[dict] = []
    items = [s.strip() for s in re.split(r"\s\|\s|;(?!\s*\d)", spec) if s.strip()]
    bad = []
    for it in items:
        m = re.match(r"(?P<k>[a-z ]+):\s*(?P<t>.+)", it)
        if m and m.group("k").strip() in kinds and m.group("k").strip() != "verse":
            out.append({"source_kind": m.group("k").strip(), "source_text": m.group("t").strip()})
            continue
        if m and m.group("k").strip() == "verse":
            it = m.group("t")
        refs = parse_refs(it, vx, follow_ons=False)
        if not refs:
            bad.append(it)
        for r in refs:
            out.append({"source_kind": "verse", "verse_id": r.verse_id,
                        "ref_as_written": r.as_written, "ref_normalised": r.normalised})
    if bad:
        raise Refused(f"source(s) not understood (not a verse reference, nor kind: text with kind in "
                      f"{kinds}): {bad}")
    return out


# ══ actions ═════════════════════════════════════════════════════════════════════════════════════
def add_claim(cfg, w: Writer, p: dict) -> str:
    conn = cfg.conn
    text = (p.get("Text") or "").strip()
    if not text:
        raise Refused("-Text (the claim in its own wording) is required")
    origin = p.get("Origin") or "narrative"
    _check_enum(cfg.enum("narrative_claim_origin"), origin, "-Origin")
    _check_enum(cfg.enum("narrative_claim_verdict"), p.get("Verdict"), "-Verdict")
    if origin == "narrative" and not (p.get("BeyondText") or "").strip():
        raise Refused("-BeyondText is required: a claim must say what it adds beyond its sources "
                      "(a quotation is not a claim)")
    vx = VerseIndex(cfg)
    sources = _parse_sources(cfg, vx, p.get("Source"))
    if not sources:
        raise Refused("-Source is required: at least one source the claim rests on")
    ch = _chapter(conn, p.get("MainChapter"), required=False)
    sec = _section(conn, ch["id"], p.get("MainSection")) if ch else None
    if p.get("ClaimRef") and conn.execute("SELECT 1 FROM narrative_claim WHERE claim_ref=?",
                                          (p["ClaimRef"],)).fetchone():
        raise Refused(f"claim {p['ClaimRef']!r} already exists")

    def go():
        since = _max_change_id(conn)
        cid = w.insert("narrative_claim", {
            "claim_ref": p.get("ClaimRef") or None, "origin": origin, "claim_text": text,
            "beyond_text": p.get("BeyondText"), "i_read": 1 if p.get("IRead") in ("1", "true", "True") else 0,
            "verdict": p.get("Verdict") or ("New" if origin == "narrative" else None),
            "main_chapter_id": ch["id"] if ch else None, "main_section_id": sec["id"] if sec else None,
            "status": "current"})
        for s in sources:
            w.insert("narrative_claim_source", {"claim_id": cid, **s})
        w.mark_changes(since, "Narrative-Register.ps1 -Action AddClaim", note=p.get("Note"))
        ref = conn.execute("SELECT claim_ref FROM narrative_claim WHERE id=?", (cid,)).fetchone()[0]
        for s in sources:
            w.note_unresolved(vx, s, f"claim {ref} source")
        return ref
    ref = _atomic(conn, go)
    return f"claim {ref} added ({len(sources)} source row(s))"


def edit(cfg, w: Writer, p: dict) -> str:
    conn = cfg.conn
    c = _claim(conn, p.get("Claim"))
    sets = {}
    if p.get("Text"):
        sets["claim_text"] = p["Text"].strip()
    if p.get("BeyondText"):
        sets["beyond_text"] = p["BeyondText"].strip()
    if p.get("Verdict"):
        _check_enum(cfg.enum("narrative_claim_verdict"), p["Verdict"], "-Verdict")
        sets["verdict"] = p["Verdict"]
    if p.get("IRead") is not None:
        sets["i_read"] = 1 if p["IRead"] in ("1", "true", "True") else 0
    if p.get("Status"):
        _check_enum(cfg.enum("narrative_claim_status"), p["Status"], "-Status")
        sets["status"] = p["Status"]
    vx = VerseIndex(cfg) if p.get("Source") else None
    sources = _parse_sources(cfg, vx, p.get("Source")) if vx else []
    if not sets and not sources:
        raise Refused("nothing to change: give -Text, -BeyondText, -Verdict, -IRead, -Status or -Source")

    def go():
        since = _max_change_id(conn)
        if sets:
            w.update("narrative_claim", {"id": c["id"]}, sets)
        for s in sources:
            w.insert("narrative_claim_source", {"claim_id": c["id"], **s})
            w.note_unresolved(vx, s, f"claim {c['claim_ref']} source")
        conn.execute("UPDATE narrative_claim_change SET change_kind='claim restated' WHERE id > ? "
                     "AND claim_id=? AND change_kind='edited' AND claim_before IS NOT claim_after "
                     "AND note IS NULL", (since, c["id"]))
        w.mark_changes(since, "Narrative-Register.ps1 -Action Edit", note=p.get("Note"))
    _atomic(conn, go)
    return f"claim {c['claim_ref']} changed: {', '.join(sets) or ''}{' + sources' if sources else ''}"


def _passage_row(cfg, w: Writer | None, ch, opening: str, create: bool):
    """The narrative_passage row for the passage that opens with `opening` in the chapter's current
    file; created (with its section) when create=True and it has no row yet."""
    conn = cfg.conn
    if not opening:
        raise Refused("-Passage (the passage's opening words) is required")
    path = _chapter_file(cfg, ch)
    _, sections, passages = parse_chapter(path.read_text(encoding="utf-8"))
    found = find_passage(passages, opening)
    if not found:
        raise Refused(f"no passage in {path.name} opens with {opening!r}")
    if len(found) > 1:
        raise Refused(f"{len(found)} passages in {path.name} open with {opening!r}; give more words")
    ps = found[0]
    anchor = anchor_of(ps.text)
    row = conn.execute("SELECT * FROM narrative_passage WHERE chapter_id=? AND last_version IS NULL "
                       "AND anchor_text=?", (ch["id"], anchor)).fetchone()
    if row or not create:
        return row, ps
    sec = sections[ps.section]
    srow = conn.execute("SELECT id FROM narrative_section WHERE chapter_id=? AND heading=? AND "
                        "last_version IS NULL", (ch["id"], sec.heading)).fetchone()
    if srow is None:
        raise Refused(f"section {sec.heading!r} has no narrative_section row; run -Action Check, "
                      f"then -Action EditSection to add it")
    pid = w.insert("narrative_passage", {
        "chapter_id": ch["id"], "section_id": srow[0], "ordinal": ps.ordinal, "anchor_text": anchor,
        "passage_text": ps.text, "first_version": ch["current_version"]})
    return conn.execute("SELECT * FROM narrative_passage WHERE id=?", (pid,)).fetchone(), ps


def tell(cfg, w: Writer, p: dict) -> str:
    conn = cfg.conn
    c = _claim(conn, p.get("Claim"))
    ch = _chapter(conn, p.get("Chapter"))
    kind = p.get("Kind") or "in full"
    _check_enum(cfg.enum("narrative_telling_kind"), kind, "-Kind")
    if kind == "in part" and not (p.get("Part") or "").strip():
        raise Refused("-Part is required with -Kind 'in part': which part of the claim the passage tells")
    _chapter_file(cfg, ch)

    def go():
        since = _max_change_id(conn)
        prow, _ = _passage_row(cfg, w, ch, p.get("Passage"), create=True)
        t = conn.execute("SELECT * FROM narrative_claim_telling WHERE claim_id=? AND passage_id=?",
                         (c["id"], prow["id"])).fetchone()
        if t and t["status"] == "current":
            raise Refused(f"{c['claim_ref']} is already told in that passage (as {t['kind']!r}); one "
                          f"telling per claim and passage -- Untell it first, or change it through Record")
        if t:
            w.update("narrative_claim_telling", {"id": t["id"]},
                     {"status": "current", "kind": kind, "part_told": p.get("Part")})
        else:
            w.insert("narrative_claim_telling", {"claim_id": c["id"], "passage_id": prow["id"],
                                                 "kind": kind, "part_told": p.get("Part")})
        w.mark_changes(since, "Narrative-Register.ps1 -Action Tell", note=p.get("Note"))
        return prow["id"]
    pid = _atomic(conn, go)
    return f"{c['claim_ref']} told in Ch {ch['chapter_no']}, passage {pid} ({kind})"


def untell(cfg, w: Writer, p: dict) -> str:
    conn = cfg.conn
    c = _claim(conn, p.get("Claim"))
    ch = _chapter(conn, p.get("Chapter"))
    rows = conn.execute(
        "SELECT t.id, p.anchor_text, p.passage_text FROM narrative_claim_telling t JOIN "
        "narrative_passage p ON p.id=t.passage_id WHERE t.claim_id=? AND p.chapter_id=? AND "
        "t.status='current'", (c["id"], ch["id"])).fetchall()
    want = p.get("Passage") or ""
    if not want.strip():
        raise Refused("-Passage (the passage's opening words) is required")
    hit = [r for r in rows if opens_with(r["passage_text"], want)]
    if len(hit) != 1:
        raise Refused(f"{len(hit)} current telling(s) of {c['claim_ref']} in Ch {ch['chapter_no']} "
                      f"open with {p.get('Passage')!r}; exactly one is needed")

    def go():
        since = _max_change_id(conn)
        w.update("narrative_claim_telling", {"id": hit[0]["id"]}, {"status": "removed"})
        w.mark_changes(since, "Narrative-Register.ps1 -Action Untell", note=p.get("Note"))
    _atomic(conn, go)
    return f"{c['claim_ref']} no longer told in that passage of Ch {ch['chapter_no']}"


def withdraw(cfg, w: Writer, p: dict) -> str:
    conn = cfg.conn
    c = _claim(conn, p.get("Claim"))
    if c["status"] == "withdrawn":
        raise Refused(f"{c['claim_ref']} is already withdrawn")

    def go():
        since = _max_change_id(conn)
        w.update("narrative_claim", {"id": c["id"]}, {"status": "withdrawn"})
        w.mark_changes(since, "Narrative-Register.ps1 -Action Withdraw", note=p.get("Note"))
    _atomic(conn, go)
    return f"{c['claim_ref']} withdrawn (in_narrative follows its tellings)"


def edit_note(cfg, w: Writer, p: dict) -> str:
    conn = cfg.conn
    heading = (p.get("Heading") or "").strip()
    if not heading:
        raise Refused("-Heading is required")
    row = conn.execute("SELECT * FROM narrative_index_note WHERE heading=?", (heading,)).fetchone()
    sets = {k: v for k, v in (("text", p.get("Text")), ("ordinal", p.get("Ordinal"))) if v is not None}
    if p.get("NewHeading"):
        sets["heading"] = p["NewHeading"]
    if row is None and not p.get("Text"):
        raise Refused(f"note {heading!r} does not exist; give -Text to add it")
    if row is not None and not sets:
        raise Refused("nothing to change: give -Text, -NewHeading or -Ordinal")

    def go():
        if row is None:
            n = conn.execute("SELECT COALESCE(MAX(ordinal), 0) + 1 FROM narrative_index_note").fetchone()[0]
            w.insert("narrative_index_note", {"heading": heading, "text": p["Text"],
                                              "ordinal": int(p.get("Ordinal") or n)})
        else:
            w.update("narrative_index_note", {"id": row["id"]}, sets)
    _atomic(conn, go)
    return f"index note {heading!r} {'added' if row is None else 'changed'}"


# ── chapters (#2155: the chapter table is the authority for the chapters and their use) ─────────
# A structural change (a chapter added, moved, renamed, renumbered, retired, or its kind, purpose or
# ruling changed) writes a Structure log entry: a narrative_update row with structure_change and
# structure_reason, published in narrative-claim-changes.md. A new file version or state is not
# structural; Record logs those with the weave.
_STRUCTURAL = ("chapter_no", "title", "kind", "purpose", "purpose_ref", "reading_order", "inactive")


def _structure_entry(w: Writer, title: str, change: str, reason: str | None) -> int:
    return w.insert("narrative_update", {"update_date": _today(), "title": title,
                                         "structure_change": change, "structure_reason": reason})


def _order_after(conn, after: str, exclude_id: int | None = None) -> int:
    """The reading order a chapter placed after `after` takes."""
    a = _chapter(conn, after)
    if exclude_id is not None and a["id"] == exclude_id:
        raise Refused("-After names the chapter being moved")
    return a["reading_order"] + 1


def _make_room(w: Writer, conn, order: int) -> int:
    """Every active chapter at `order` or later moves down one place; returns how many moved."""
    rows = conn.execute("SELECT id, reading_order FROM narrative_chapter WHERE inactive=0 AND "
                        "reading_order >= ? ORDER BY reading_order DESC", (order,)).fetchall()
    for r in rows:
        w.update("narrative_chapter", {"id": r["id"]}, {"reading_order": r["reading_order"] + 1})
    return len(rows)


def _close_gap(w: Writer, conn, order: int) -> None:
    """After a chapter leaves `order`, every active chapter after it moves up one place."""
    for r in conn.execute("SELECT id, reading_order FROM narrative_chapter WHERE inactive=0 AND "
                          "reading_order > ? ORDER BY reading_order", (order,)).fetchall():
        w.update("narrative_chapter", {"id": r["id"]}, {"reading_order": r["reading_order"] - 1})


def add_chapter(cfg, w: Writer, p: dict) -> str:
    conn = cfg.conn
    no = (p.get("Chapter") or "").strip()
    missing = [n for n in ("Chapter", "Title", "Kind", "Purpose", "PurposeRef") if not p.get(n)]
    if missing:
        raise Refused(f"AddChapter needs {', '.join('-' + m for m in missing)}")
    if bool(p.get("After")) == (p.get("ReadingOrder") is not None):
        raise Refused("give one of -After <chapter> or -ReadingOrder n")
    if conn.execute("SELECT 1 FROM narrative_chapter WHERE inactive=0 AND chapter_no=?", (no,)).fetchone():
        raise Refused(f"chapter {no!r} is already used by an active chapter")
    kind, state = p["Kind"], p.get("State") or "draft"
    _check_enum(cfg.enum("narrative_chapter_kind"), kind, "-Kind")
    _check_enum(cfg.enum("narrative_chapter_state"), state, "-State")
    no_file = kind in (cfg.required_setting("narrative.chapter_kinds_without_file") or [])
    cur = p.get("CurrentFile")
    sections: list[Section] = []
    version = None
    if cur:
        path = chapter_dir(cfg) / cur
        if not path.is_file():
            raise Refused(f"-CurrentFile {cur!r} is not on disk")
        fv = file_version(cur)
        if not fv:
            raise Refused(f"-CurrentFile {cur!r} is not named <stem>-vN-YYYYMMDD.md")
        stem, version = fv
        _, sections, _ = parse_chapter(path.read_text(encoding="utf-8"))
    elif not no_file:
        raise Refused(f"-CurrentFile is required for a {kind!r} chapter (only "
                      f"{cfg.required_setting('narrative.chapter_kinds_without_file')} have no file)")
    else:
        stem = p.get("FileStem") or re.sub(r"[^a-z0-9]+", "-", f"{no} {p['Title']}".lower()).strip("-")
    order = _order_after(conn, p["After"]) if p.get("After") else int(p["ReadingOrder"])
    where = f"after {p['After']}" if p.get("After") else f"reading order {order}"

    def go():
        since = _max_change_id(conn)
        moved = _make_room(w, conn, order)
        cid = w.insert("narrative_chapter", {
            "chapter_no": no, "title": p["Title"], "reading_order": order, "file_stem": stem,
            "current_version": version, "current_file": cur, "state": state, "kind": kind,
            "purpose": p["Purpose"], "purpose_ref": p["PurposeRef"], "built_from": p.get("BuiltFrom"),
            "replaces_original": p.get("ReplacesOriginal") or "—"})
        ch = conn.execute("SELECT * FROM narrative_chapter WHERE id=?", (cid,)).fetchone()
        if sections:
            _sync_sections(conn, w, ch, sections, version)
        _structure_entry(w, f"Chapter {no} {p['Title']} added",
                         f"New chapter {no} {p['Title']} ({kind}; reading order {order}, {where}"
                         f"{'; later chapters +1' if moved else ''}). Purpose: {p['Purpose']}",
                         p.get("Note") or p["PurposeRef"])
        w.mark_changes(since, "Narrative-Register.ps1 -Action AddChapter", note=p.get("Note"))
        return moved
    moved = _atomic(conn, go)
    return (f"chapter {no} {p['Title']!r} added at reading order {order} ({kind}); "
            f"{moved} later chapter(s) moved down; {len(sections)} section row(s)")


def edit_chapter(cfg, w: Writer, p: dict) -> str:
    conn = cfg.conn
    ch = _chapter(conn, p.get("Chapter"))
    sets = {}
    for prm, col in (("NewNumber", "chapter_no"), ("Title", "title"), ("State", "state"),
                     ("CurrentFile", "current_file"), ("CurrentVersion", "current_version"),
                     ("ReadingOrder", "reading_order"), ("Inactive", "inactive"), ("Kind", "kind"),
                     ("Purpose", "purpose"), ("PurposeRef", "purpose_ref")):
        if p.get(prm) is not None:
            sets[col] = p[prm]
    if p.get("After"):
        if "reading_order" in sets:
            raise Refused("give one of -After <chapter> or -ReadingOrder n, not both")
        target = _order_after(conn, p["After"], exclude_id=ch["id"])
        if target > ch["reading_order"]:
            target -= 1                  # the gap it leaves closes first
        sets["reading_order"] = target
    _check_enum(cfg.enum("narrative_chapter_state"), sets.get("state"), "-State")
    _check_enum(cfg.enum("narrative_chapter_kind"), sets.get("kind"), "-Kind")
    if "current_file" in sets and not (chapter_dir(cfg) / sets["current_file"]).is_file():
        raise Refused(f"-CurrentFile {sets['current_file']!r} is not on disk")
    if not sets:
        raise Refused("nothing to change: give -NewNumber, -Title, -Kind, -Purpose, -PurposeRef, -State, "
                      "-CurrentFile, -CurrentVersion, -After, -ReadingOrder or -Inactive")
    structural = {k: v for k, v in sets.items() if k in _STRUCTURAL and str(ch[k]) != str(v)}

    def go():
        since = _max_change_id(conn)
        try:
            if p.get("After") and sets["reading_order"] != ch["reading_order"]:
                _close_gap(w, conn, ch["reading_order"])
                w.update("narrative_chapter", {"id": ch["id"]}, {"reading_order": -1})
                _make_room(w, conn, sets["reading_order"])
            w.update("narrative_chapter", {"id": ch["id"]}, sets)
        except sqlite3.IntegrityError as exc:
            raise Refused(str(exc)) from exc
        if structural:
            label = sets.get("chapter_no", ch["chapter_no"])
            _structure_entry(w, f"Chapter {label} changed",
                             "; ".join(f"{k}: {ch[k]!r} -> {v!r}" for k, v in structural.items())
                             + (f" (placed after {p['After']})" if p.get("After") else ""),
                             p.get("Note"))
        w.mark_changes(since, "Narrative-Register.ps1 -Action EditChapter", note=p.get("Note"))
    _atomic(conn, go)
    return (f"chapter {ch['chapter_no']} changed: {', '.join(sets)}"
            + ("; Structure log entry written" if structural else ""))


def edit_section(cfg, w: Writer, p: dict) -> str:
    conn = cfg.conn
    ch = _chapter(conn, p.get("Chapter"))
    sec = conn.execute("SELECT * FROM narrative_section WHERE chapter_id=? AND heading=? AND "
                       "last_version IS NULL", (ch["id"], p.get("Section"))).fetchone()
    sets = {}
    for prm, col in (("NewHeading", "heading"), ("Level", "level"), ("Ordinal", "ordinal"),
                     ("LastVersion", "last_version")):
        if p.get(prm) is not None:
            sets[col] = p[prm]
    if sec is None:
        if not p.get("Section") or p.get("Level") is None:
            raise Refused(f"section {p.get('Section')!r} does not exist in Ch {ch['chapter_no']}; "
                          f"give -Section and -Level to add it")

        def add():
            n = conn.execute("SELECT COALESCE(MAX(ordinal), 0) + 1 FROM narrative_section WHERE "
                             "chapter_id=?", (ch["id"],)).fetchone()[0]
            w.insert("narrative_section", {"chapter_id": ch["id"], "heading": p["Section"],
                                           "level": int(p["Level"]), "ordinal": int(p.get("Ordinal") or n),
                                           "first_version": ch["current_version"]})
        _atomic(conn, add)
        return f"section {p['Section']!r} added to Ch {ch['chapter_no']}"
    if not sets:
        raise Refused("nothing to change: give -NewHeading, -Level, -Ordinal or -LastVersion")

    def go():
        if "heading" in sets:     # a rename keeps the old row as history
            w.update("narrative_section", {"id": sec["id"]}, {"last_version": ch["current_version"]})
            new = {k: sec[k] for k in ("chapter_id", "level", "parent_section_id", "ordinal")}
            new.update({k: v for k, v in sets.items() if k != "last_version"})
            nid = w.insert("narrative_section", {**new, "first_version": ch["current_version"],
                                                 "renamed_from_id": sec["id"]})
            w.move_passages(sec["id"], nid)
        else:
            w.update("narrative_section", {"id": sec["id"]}, sets)
    _atomic(conn, go)
    return f"section {p.get('Section')!r} in Ch {ch['chapter_no']} changed: {', '.join(sets)}"


# ── Record (spec sec5.1) ────────────────────────────────────────────────────────────────────────
def _escalation_exists(conn, kind: str, value: str) -> bool:
    if kind == "escalation":
        return conn.execute("SELECT 1 FROM escalation WHERE id=?", (int(value.lstrip("#")),)).fetchone() is not None
    alias, _, item = value.partition(".")
    e = conn.execute("SELECT id FROM escalation WHERE alias=?", (alias,)).fetchone()
    if e is None:
        return False
    if kind == "thread item":
        return conn.execute("SELECT 1 FROM escalation_thread_item WHERE escalation_id=? AND item_no=?",
                            (e[0], int(item or 0))).fetchone() is not None
    return True


def record(cfg, w: Writer, p: dict) -> str:
    """One weave's whole update from a JSON file. Shape (all keys but update optional):
    {"update": {"update_date","title","strand","researcher_instruction","method","source_files":[],
                "scripts":[],"claims_changed_note","not_woven_note","structure_change",
                "structure_reason","quote_parts","quote_failures","quote_note","notes"},
     "refs": [{"kind": "escalation|thread|thread item", "value": "1998|OT-29|OT-29.1"}],
     "chapters": [{"chapter": "10.13", "from_version": 7, "to_version": 8, "file": "<new file>",
                   "renames": [{"from": "<old heading>", "to": "<new heading>"}],
                   "passages": [{"anchor": "<old opening words>", "new_anchor": "<new>"|null (removed),
                                 "to_chapter": "<chapter it moves to, for a split or merge>"}]}],
     "claims": [{"key": "n1", "new": {"text","beyond_text","origin","verdict","i_read","sources"}},
                {"ref": "C-12", "edit": {"text","verdict","status","note"}}],
     "tellings": [{"claim": "C-12"|"n1", "chapter": "10.13", "passage": "<opening words>",
                   "kind": "in full|in part|pointer", "part": "...", "action": "add|change|remove"}]}"""
    conn = cfg.conn
    fpath = pathlib.Path(p.get("File") or "")
    if not fpath.is_absolute():
        fpath = PROJECT_ROOT / fpath
    if not fpath.is_file():
        raise Refused(f"-File {p.get('File')!r} not found")
    try:
        data = json.loads(fpath.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise Refused(f"-File is not valid JSON: {exc}") from exc
    up = data.get("update") or {}
    if not up.get("title") or not up.get("update_date"):
        raise Refused("update.title and update.update_date are required")
    if conn.execute("SELECT 1 FROM narrative_update WHERE update_date=? AND title=?",
                    (up["update_date"], up["title"])).fetchone():
        raise Refused(f"already recorded: an update of {up['update_date']} titled {up['title']!r} exists")
    for r in data.get("refs", []):
        _check_enum(cfg.enum("narrative_update_ref_kind"), r.get("kind"), "refs.kind")
        if not _escalation_exists(conn, r["kind"], str(r["value"])):
            raise Refused(f"{r['kind']} {r['value']!r} does not exist")
    vx = VerseIndex(cfg)
    chapters = []
    for c in data.get("chapters", []):
        ch = _chapter(conn, c.get("chapter"))
        f = chapter_dir(cfg) / (c.get("file") or "")
        fv = file_version(f.name)
        if not f.is_file() or not fv or fv[1] != int(c.get("to_version", -1)):
            raise Refused(f"chapter {ch['chapter_no']}: file {c.get('file')!r} is not on disk or its "
                          f"version is not to_version {c.get('to_version')}")
        if ch["current_version"] is not None and int(c.get("from_version", -1)) != ch["current_version"]:
            raise Refused(f"chapter {ch['chapter_no']}: from_version {c.get('from_version')} does not "
                          f"match the register's current version {ch['current_version']}")
        chapters.append((ch, c, f))
    in_record = {ch["chapter_no"] for ch, _, _ in chapters}
    for ch, c, f in chapters:
        for x in c.get("passages", []):
            if x.get("to_chapter") and _chapter(conn, x["to_chapter"])["chapter_no"] not in in_record:
                raise Refused(f"passage '{x.get('anchor')}' moves to Ch {x['to_chapter']}, which is not "
                              f"among this record's chapters (its new file must be named too)")
    new_keys = {}
    for cl in data.get("claims", []):
        if "new" in cl:
            n = cl["new"]
            if not n.get("text"):
                raise Refused(f"claims[{cl.get('key')}].new.text is required")
            _check_enum(cfg.enum("narrative_claim_origin"), n.get("origin") or "narrative", "claims.new.origin")
            _check_enum(cfg.enum("narrative_claim_verdict"), n.get("verdict"), "claims.new.verdict")
            new_keys[cl.get("key")] = None
        else:
            _claim(conn, cl.get("ref"))
            e = cl.get("edit") or {}
            _check_enum(cfg.enum("narrative_claim_verdict"), e.get("verdict"), "claims.edit.verdict")
            _check_enum(cfg.enum("narrative_claim_status"), e.get("status"), "claims.edit.status")
    for t in data.get("tellings", []):
        if t.get("claim") not in new_keys:
            _claim(conn, t.get("claim"))
        _chapter(conn, t.get("chapter"))
        _check_enum(cfg.enum("narrative_telling_kind"), t.get("kind") or "in full", "tellings.kind")
        if t.get("action", "add") not in ("add", "change", "remove"):
            raise Refused(f"tellings.action {t.get('action')!r} must be add, change or remove")
    findings: list[str] = []

    def go():
        since = _max_change_id(conn)
        uid = w.insert("narrative_update", {
            **{k: up.get(k) for k in ("update_date", "title", "strand", "researcher_instruction", "method",
                                      "claims_changed_note", "not_woven_note", "structure_change",
                                      "structure_reason", "quote_parts", "quote_failures", "quote_note",
                                      "notes")},
            "source_files": "\n".join(up.get("source_files") or []) or None,
            "scripts": "\n".join(up.get("scripts") or []) or None})
        for r in data.get("refs", []):
            w.insert("narrative_update_ref", {"update_id": uid, "kind": r["kind"], "value": str(r["value"])})
        changed_passages: set[int] = set()
        declared: set[int] = set()            # passages the JSON names as moved or removed
        parsed = {}
        for ch, c, f in chapters:            # every chapter's sections first: a passage may move into one
            _, sections, passages = parse_chapter(f.read_text(encoding="utf-8"))
            _sync_sections(conn, w, ch, sections, c["to_version"],
                           {r["to"]: r["from"] for r in c.get("renames", [])})
            parsed[ch["chapter_no"]] = (ch, sections, passages)
        for ch, c, f in chapters:
            old_file = ch["current_file"]
            _, sections, passages = parsed[ch["chapter_no"]]
            moved = {plain(x["anchor"]).lower(): x for x in c.get("passages", [])}
            for prow in conn.execute("SELECT * FROM narrative_passage WHERE chapter_id=? AND "
                                     "last_version IS NULL", (ch["id"],)).fetchall():
                entry = next((v for k, v in moved.items() if opens_with(prow["anchor_text"], v["anchor"])), None)
                look = (entry.get("new_anchor") or entry["anchor"]) if entry else prow["anchor_text"]
                if entry and "new_anchor" in entry and entry["new_anchor"] is None and not entry.get("to_chapter"):
                    w.update("narrative_passage", {"id": prow["id"]}, {"last_version": c["from_version"]})
                    w.update("narrative_claim_telling", {"passage_id": prow["id"], "status": "current"},
                             {"status": "removed"})     # each claim it told logs 'telling removed'
                    changed_passages.add(prow["id"])
                    declared.add(prow["id"])
                    continue
                if entry and entry.get("to_chapter"):     # a split or merge: the passage keeps its row
                    tch, tsecs, tps = parsed[_chapter(conn, entry["to_chapter"])["chapter_no"]]
                    hit = find_passage(tps, look)
                    if len(hit) != 1:
                        raise Refused(f"passage '{entry['anchor']}' is not found once in Ch {tch['chapter_no']}'s "
                                      f"new file ({len(hit)} matches)")
                    ps = hit[0]
                    w.update("narrative_passage", {"id": prow["id"]}, {
                        "chapter_id": tch["id"], "section_id": _section_row_for(conn, tch["id"], tsecs[ps.section].heading),
                        "passage_text": ps.text, "anchor_text": anchor_of(ps.text), "ordinal": ps.ordinal})
                    changed_passages.add(prow["id"])
                    declared.add(prow["id"])
                    continue
                hit = find_passage(passages, look)
                if len(hit) != 1:
                    findings.append(f"Ch {ch['chapter_no']}: passage {prow['id']} ('{prow['anchor_text']}') "
                                    f"{'not found' if not hit else 'matches ' + str(len(hit)) + ' passages'} "
                                    f"in {f.name} and not accounted for in the JSON")
                    continue
                ps = hit[0]
                sets = {}
                if ps.text != prow["passage_text"]:
                    sets["passage_text"] = ps.text
                new_anchor = anchor_of(ps.text)
                if new_anchor != prow["anchor_text"]:
                    sets["anchor_text"] = new_anchor
                sec_row = _section_row_for(conn, ch["id"], sections[ps.section].heading)
                if sec_row and sec_row != prow["section_id"]:
                    sets["section_id"] = sec_row
                if sets:
                    w.update("narrative_passage", {"id": prow["id"]}, sets)
                    if "passage_text" in sets:
                        changed_passages.add(prow["id"])
            w.update("narrative_chapter", {"id": ch["id"]},
                     {"current_version": c["to_version"], "current_file": f.name})
            _sync_citations(cfg, w, vx, ch, sections, passages, c["from_version"], c["to_version"])
            conn.execute("UPDATE narrative_claim_change SET chapter_version_from=?, chapter_version_to=?, "
                         "file_before=?, file_after=? WHERE id > ? AND chapter_id=?",
                         (c["from_version"], c["to_version"], old_file, f.name, since, ch["id"]))
        for cl in data.get("claims", []):
            if "new" in cl:
                n = cl["new"]
                cid = w.insert("narrative_claim", {
                    "origin": n.get("origin") or "narrative", "claim_text": n["text"],
                    "beyond_text": n.get("beyond_text"), "i_read": int(bool(n.get("i_read"))),
                    "verdict": n.get("verdict") or "New", "status": "current"})
                new_ref = conn.execute("SELECT claim_ref FROM narrative_claim WHERE id=?", (cid,)).fetchone()[0]
                for s in _parse_sources(cfg, vx, "; ".join(n.get("sources") or [])):
                    w.insert("narrative_claim_source", {"claim_id": cid, **s})
                    w.note_unresolved(vx, s, f"claim {new_ref} source")
                new_keys[cl.get("key")] = cid
            else:
                c0 = _claim(conn, cl["ref"])
                e = cl.get("edit") or {}
                sets = {k2: e[k1] for k1, k2 in (("text", "claim_text"), ("verdict", "verdict"),
                                                   ("status", "status")) if e.get(k1)}
                if sets:
                    w.update("narrative_claim", {"id": c0["id"]}, sets)
        accounted: set[int] = set()
        for t in data.get("tellings", []):
            cid = new_keys.get(t["claim"]) or _claim(conn, t["claim"])["id"]
            ch = _chapter(conn, t["chapter"])
            prow, _ = _passage_row(cfg, w, ch, t.get("passage"), create=t.get("action", "add") != "remove")
            if prow is None:
                raise Refused(f"telling {t}: the passage has no row to remove from")
            accounted.add(prow["id"])
            cur = conn.execute("SELECT * FROM narrative_claim_telling WHERE claim_id=? AND passage_id=?",
                               (cid, prow["id"])).fetchone()
            act = t.get("action", "add")
            if act == "remove":
                if not cur:
                    raise Refused(f"telling {t}: no telling to remove")
                w.update("narrative_claim_telling", {"id": cur["id"]}, {"status": "removed"})
            elif cur:
                w.update("narrative_claim_telling", {"id": cur["id"]},
                         {"status": "current", "kind": t.get("kind") or cur["kind"],
                          "part_told": t.get("part", cur["part_told"])})
            else:
                w.insert("narrative_claim_telling", {"claim_id": cid, "passage_id": prow["id"],
                                                     "kind": t.get("kind") or "in full",
                                                     "part_told": t.get("part")})
        for pid in sorted(changed_passages - accounted - declared):
            for r in conn.execute("SELECT c.claim_ref, p.anchor_text FROM narrative_claim_telling t "
                                  "JOIN narrative_claim c ON c.id=t.claim_id JOIN narrative_passage p "
                                  "ON p.id=t.passage_id WHERE t.passage_id=? AND t.status='current'", (pid,)):
                findings.append(f"passage {pid} ('{r['anchor_text']}') changed and tells {r['claim_ref']}; "
                                f"the JSON does not account for it -- read the telling")
        claims_touched = {r[0] for r in conn.execute(
            "SELECT DISTINCT claim_id FROM narrative_claim_change WHERE id > ? AND passage_id IS NOT NULL",
            (since,))}
        for cid in sorted(claims_touched):
            others = conn.execute(
                "SELECT c.claim_ref, ch.chapter_no, s.heading FROM narrative_claim_telling t JOIN "
                "narrative_passage p ON p.id=t.passage_id JOIN narrative_chapter ch ON ch.id=p.chapter_id "
                "LEFT JOIN narrative_section s ON s.id=p.section_id JOIN narrative_claim c ON c.id=t.claim_id "
                "WHERE t.claim_id=? AND t.status='current' AND t.passage_id NOT IN (SELECT passage_id FROM "
                "narrative_claim_change WHERE id > ? AND passage_id IS NOT NULL)", (cid, since)).fetchall()
            for o in others:
                findings.append(f"{o['claim_ref']} is also told in Ch {o['chapter_no']} "
                                f"*{o['heading'] or '(opening)'}* -- read it for consistency")
        w.mark_changes(since, f"Narrative-Register.ps1 -Action Record -File {p.get('File')}",
                       update_id=uid, change_date=up["update_date"])
        return uid
    uid = _atomic(conn, go)
    return "\n  ".join([f"update {uid} recorded: {up['title']}"] + (findings or ["nothing unaccounted for"]))


def _section_row_for(conn, chapter_id: int, heading: str) -> int | None:
    r = conn.execute("SELECT id FROM narrative_section WHERE chapter_id=? AND heading=? AND "
                     "last_version IS NULL", (chapter_id, heading)).fetchone()
    return r[0] if r else None


def _sync_sections(conn, w: Writer, ch, sections: list[Section], version: int,
                   renames: dict[str, str] | None = None) -> None:
    """Headings now in the file get a row (first_version = version) if they have none; current rows
    whose heading is gone get last_version = version - 1. `renames` {new heading: old heading}: the
    new row carries renamed_from_id, and the passages under the old row follow it to the new one."""
    ids: dict[int, int] = {}
    now = set()
    renames = renames or {}
    for i, s in enumerate(sections):
        sid = _section_row_for(conn, ch["id"], s.heading)
        parent = ids.get(s.parent) if s.parent is not None else None
        if sid is None:
            old = _section_row_for(conn, ch["id"], renames[s.heading]) if s.heading in renames else None
            if s.heading in renames and old is None:
                raise Refused(f"chapter {ch['chapter_no']}: rename from {renames[s.heading]!r} -- no "
                              f"current section has that heading")
            sid = w.insert("narrative_section", {"chapter_id": ch["id"], "heading": s.heading,
                                                 "level": s.level, "parent_section_id": parent,
                                                 "ordinal": s.ordinal, "first_version": version,
                                                 "renamed_from_id": old})
            if old is not None:
                w.update("narrative_section", {"id": old}, {"last_version": version - 1})
                w.move_passages(old, sid)
        else:
            w.update("narrative_section", {"id": sid}, {"level": s.level, "ordinal": s.ordinal,
                                                         "parent_section_id": parent})
        ids[i] = sid
        now.add(sid)
    for r in conn.execute("SELECT id FROM narrative_section WHERE chapter_id=? AND last_version IS NULL",
                          (ch["id"],)).fetchall():
        if r[0] not in now:
            w.update("narrative_section", {"id": r[0]}, {"last_version": version - 1})


def _sync_citations(cfg, w: Writer, vx: VerseIndex, ch, sections, passages, from_v, to_v) -> None:
    """The chapter's citation rows brought to the new version: a citation no longer present gets
    last_version = from_v; a new one is inserted with first_version = to_v."""
    conn = cfg.conn
    want: dict[tuple, dict] = {}
    where: dict[tuple, str] = {}
    for ps in passages:
        heading = sections[ps.section].heading
        sid = _section_row_for(conn, ch["id"], heading)
        prow = conn.execute("SELECT id FROM narrative_passage WHERE chapter_id=? AND anchor_text=? AND "
                            "last_version IS NULL", (ch["id"], anchor_of(ps.text))).fetchone()
        for r in parse_refs(ps.text, vx):
            key = (sid, r.normalised)
            if key in want:
                continue
            vt = conn.execute("SELECT text FROM verse WHERE id=?", (r.verse_id,)).fetchone() if r.verse_id else None
            want[key] = {"chapter_id": ch["id"], "section_id": sid, "passage_id": prow[0] if prow else None,
                         "verse_id": r.verse_id, "ref_as_written": r.as_written, "ref_normalised": r.normalised,
                         "quoted": int(quoted(ps.text, vt[0] if vt else None)), "first_version": to_v}
            where[key] = f"Ch {ch['chapter_no']} *{heading}*"
    have = {(r["section_id"], r["ref_normalised"]): r for r in conn.execute(
        "SELECT * FROM narrative_citation WHERE chapter_id=? AND last_version IS NULL", (ch["id"],))}
    for key, r in have.items():
        if key not in want:
            w.update("narrative_citation", {"id": r["id"]}, {"last_version": from_v})
    for key, row in want.items():
        if key not in have:
            w.insert("narrative_citation", row)
            w.note_unresolved(vx, row, where[key])
        else:      # a corrected parse (#2136), or a verse since added to the verse table (#2138)
            sets = {k: row[k] for k in ("ref_as_written", "verse_id") if have[key][k] != row[k]}
            if "verse_id" in sets:
                sets["quoted"] = row["quoted"]
            if sets:
                w.update("narrative_citation", {"id": have[key]["id"]}, sets)


# ══ read-only: find, history, check ═════════════════════════════════════════════════════════════
def _told_in(conn, claim_id: int) -> list[str]:
    return [f"{r['chapter_no']} *{r['heading'] or '(opening)'}* ({r['kind']})" for r in conn.execute(
        "SELECT ch.chapter_no, s.heading, t.kind FROM narrative_claim_telling t JOIN narrative_passage p "
        "ON p.id=t.passage_id JOIN narrative_chapter ch ON ch.id=p.chapter_id LEFT JOIN narrative_section s "
        "ON s.id=p.section_id WHERE t.claim_id=? AND t.status='current' AND p.last_version IS NULL "
        "ORDER BY ch.reading_order, s.ordinal, p.ordinal", (claim_id,))]


def find(cfg, p: dict) -> tuple[list[str], list[str]]:
    """(report lines, console lines). Filters combine with AND."""
    conn = cfg.conn
    where, args, title = ["1=1"], [], []
    if p.get("Claim"):
        where.append("c.claim_ref=?"); args.append(p["Claim"]); title.append(f"claim {p['Claim']}")
    if p.get("Text"):
        where.append("(c.claim_text LIKE ? OR c.beyond_text LIKE ? OR c.original_wording LIKE ?)")
        args += [f"%{p['Text']}%"] * 3; title.append(f"text '{p['Text']}'")
    if p.get("Verdict"):
        where.append("(c.verdict=? OR c.part_verdict=?)"); args += [p["Verdict"]] * 2
        title.append(f"verdict {p['Verdict']}")
    if p.get("NotInNarrative") in ("1", "true", "True"):
        where.append("c.in_narrative=0"); title.append("not in the narrative")
    if p.get("ToldInMoreThanOne") in ("1", "true", "True"):
        where.append("(SELECT COUNT(*) FROM narrative_claim_telling t JOIN narrative_passage pp ON "
                     "pp.id=t.passage_id WHERE t.claim_id=c.id AND t.status='current' AND t.kind<>'pointer' "
                     "AND pp.last_version IS NULL) > 1")
        title.append("told in more than one place")
    if p.get("Chapter"):
        ch = _chapter(conn, p["Chapter"])
        sec_clause, sec_args = "", []
        if p.get("Section"):
            sec_clause, sec_args = " AND s.heading LIKE ?", [f"%{p['Section']}%"]
            title.append(f"section '{p['Section']}'")
        where.append("(c.main_chapter_id=? OR c.id IN (SELECT t.claim_id FROM narrative_claim_telling t "
                     "JOIN narrative_passage pp ON pp.id=t.passage_id LEFT JOIN narrative_section s ON "
                     f"s.id=pp.section_id WHERE pp.chapter_id=? AND t.status='current'{sec_clause}))")
        args += [ch["id"], ch["id"], *sec_args]; title.append(f"Ch {ch['chapter_no']}")
    elif p.get("Section"):
        raise Refused("-Section needs -Chapter")
    for prm, kind in (("Escalation", "escalation"), ("Thread", "thread")):
        if p.get(prm):
            v = str(p[prm]).lstrip("#")
            where.append("c.id IN (SELECT ch.claim_id FROM narrative_claim_change ch JOIN narrative_update_ref r "
                         "ON r.update_id=ch.update_id WHERE (r.kind=? AND r.value=?) OR (r.kind='thread item' "
                         "AND r.value LIKE ?))")
            args += [kind, v, f"{v}.%"]; title.append(f"{kind} {v}")
    cites: list[str] = []
    if p.get("Verse"):
        vx = VerseIndex(cfg)
        refs = parse_refs(p["Verse"], vx, follow_ons=False)
        if not refs:
            raise Refused(f"-Verse {p['Verse']!r} is not a reference")
        norms = [r.normalised for r in refs]
        ph = ",".join("?" * len(norms))
        where.append(f"c.id IN (SELECT claim_id FROM narrative_claim_source WHERE ref_normalised IN ({ph}))")
        args += norms; title.append(f"verse {p['Verse']}")
        for r in conn.execute(
                f"SELECT ci.ref_normalised, ch.chapter_no, s.heading, ci.quoted FROM narrative_citation ci "
                f"JOIN narrative_chapter ch ON ch.id=ci.chapter_id LEFT JOIN narrative_section s ON "
                f"s.id=ci.section_id WHERE ci.ref_normalised IN ({ph}) AND ci.last_version IS NULL "
                f"ORDER BY ch.reading_order", norms):
            cites.append(f"- {r['ref_normalised']}: Ch {r['chapter_no']} *{r['heading'] or '(opening)'}*"
                         f"{' (quoted)' if r['quoted'] else ''}")
    if len(where) == 1:
        raise Refused("give at least one filter: -Verse -Chapter [-Section] -Claim -Text -Escalation "
                      "-Thread -Verdict -NotInNarrative -ToldInMoreThanOne")
    rows = conn.execute(f"SELECT c.* FROM narrative_claim c WHERE {' AND '.join(where)} ORDER BY c.id",
                        args).fetchall()
    head = f"Narrative register search: {'; '.join(title)}"
    lines = [f"# {head}", "", f"{len(rows)} claim(s).", ""]
    if rows:
        lines += ["| Claim | Status | In narrative | Verdict | Claim | Told in |", "|---|---|---|---|---|---|"]
    console = [f"{len(rows)} claim(s)"]
    for r in rows:
        told = _told_in(conn, r["id"])
        lines.append(f"| {r['claim_ref']} | {r['status']} | {r['in_narrative']} | {r['verdict'] or ''} | "
                     f"{_cell(r['claim_text'])} | {'; '.join(told) or '—'} |")
        console.append(f"{r['claim_ref']}: {r['claim_text'][:90]}")
    if cites:
        lines += ["", "## Where the verse is cited in the narrative", ""] + cites
    return lines, console


def _cell(s: str | None) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ")


def history(cfg, p: dict) -> tuple[list[str], list[str]]:
    conn = cfg.conn
    c = _claim(conn, p.get("Claim"))
    lines = [f"# Narrative claim history: {c['claim_ref']}", "",
             f"**Claim:** {c['claim_text']}", "",
             f"Status {c['status']} · verdict {c['verdict'] or '—'} · in the narrative: "
             f"{'yes' if c['in_narrative'] else 'no'}", "",
             f"**Told in:** {'; '.join(_told_in(conn, c['id'])) or '—'}", "", "## Changes", ""]
    rows = conn.execute(
        "SELECT x.*, ch.chapter_no, s.heading, u.title AS update_title FROM narrative_claim_change x "
        "LEFT JOIN narrative_chapter ch ON ch.id=x.chapter_id LEFT JOIN narrative_section s ON "
        "s.id=x.section_id LEFT JOIN narrative_update u ON u.id=x.update_id WHERE x.claim_id=? "
        "ORDER BY x.change_date, x.id", (c["id"],)).fetchall()
    for r in rows:
        where = (f" · Ch {r['chapter_no']}" + (f" *{r['heading']}*" if r["heading"] else "")) if r["chapter_no"] else ""
        ver = (f" · v{r['chapter_version_from']} → v{r['chapter_version_to']}"
               if r["chapter_version_to"] is not None else "")
        lines.append(f"### {r['change_date']} — {r['change_kind']}{where}{ver}")
        lines.append(f"*{r['basis']}*{' · ' + r['update_title'] if r['update_title'] else ''}"
                     f"{' · ' + r['provenance'] if r['provenance'] else ''}")
        for lbl, a, b in (("Claim", r["claim_before"], r["claim_after"]),
                          ("Verdict", r["verdict_before"], r["verdict_after"]),
                          ("Passage", r["passage_before"], r["passage_after"])):
            if a is not None or b is not None:
                lines += [f"- **{lbl} before:** {a if a is not None else '—'}",
                          f"- **{lbl} after:** {b if b is not None else '—'}"]
        if r["note"]:
            lines.append(f"- **Note:** {r['note']}")
        lines.append("")
    return lines, [f"{c['claim_ref']}: {len(rows)} change row(s)"]


def check(cfg, p: dict) -> tuple[list[str], list[str]]:
    """Chapters, sections and passage anchors against the files on disk (spec sec5)."""
    conn = cfg.conn
    problems: list[str] = []
    files_text: dict[int, list[Passage]] = {}
    chs = conn.execute("SELECT * FROM narrative_chapter WHERE inactive=0 ORDER BY reading_order").fetchall()
    for ch in chs:
        path = chapter_dir(cfg) / (ch["current_file"] or "")
        if not ch["current_file"]:
            continue
        if not path.is_file():
            problems.append(f"Ch {ch['chapter_no']}: current file {ch['current_file']} is not on disk")
            continue
        fv = file_version(path.name)
        if fv and ch["current_version"] is not None and fv[1] != ch["current_version"]:
            problems.append(f"Ch {ch['chapter_no']}: current_version {ch['current_version']} but file is v{fv[1]}")
        newer = sorted((file_version(x.name)[1], x.name) for x in chapter_dir(cfg).glob(f"{ch['file_stem']}-v*.md")
                       if file_version(x.name))
        if newer and newer[-1][1] != ch["current_file"]:
            problems.append(f"Ch {ch['chapter_no']}: a newer file is on disk ({newer[-1][1]}) than the "
                            f"register's current file ({ch['current_file']}) -- record the weave")
        _, sections, passages = parse_chapter(path.read_text(encoding="utf-8"))
        files_text[ch["id"]] = passages
        headings = {s.heading for s in sections}
        for s in conn.execute("SELECT heading FROM narrative_section WHERE chapter_id=? AND last_version IS NULL",
                              (ch["id"],)):
            if s[0] not in headings:
                problems.append(f"Ch {ch['chapter_no']}: section *{s[0]}* is current in the register but "
                                f"not in {path.name}")
        reg = {s[0] for s in conn.execute("SELECT heading FROM narrative_section WHERE chapter_id=? AND "
                                           "last_version IS NULL", (ch["id"],))}
        for h in sorted(headings - reg):
            problems.append(f"Ch {ch['chapter_no']}: heading *{h}* in {path.name} has no section row")
    for prow in conn.execute("SELECT p.*, ch.chapter_no FROM narrative_passage p JOIN narrative_chapter ch "
                             "ON ch.id=p.chapter_id WHERE p.last_version IS NULL").fetchall():
        ps = files_text.get(prow["chapter_id"])
        if ps is None:
            continue
        if not find_passage(ps, prow["anchor_text"]):
            elsewhere = [conn.execute("SELECT chapter_no FROM narrative_chapter WHERE id=?", (cid,)).fetchone()[0]
                         for cid, pl in files_text.items() if cid != prow["chapter_id"] and find_passage(pl, prow["anchor_text"])]
            problems.append(f"Ch {prow['chapter_no']}: passage {prow['id']} ('{prow['anchor_text']}') is no "
                            f"longer in its chapter file" + (f" -- found in Ch {', '.join(elsewhere)}: a move "
                                                              f"to confirm" if elsewhere else ""))
    for r in conn.execute("SELECT claim_ref FROM narrative_claim WHERE status='current' AND in_narrative=0"):
        problems.append(f"claim {r[0]} is current but no current passage tells it")
    vx = VerseIndex(cfg)                  # an unresolved reference is an error (#2134)
    for r in conn.execute("SELECT ch.chapter_no, s.heading, ci.ref_as_written, ci.ref_normalised FROM "
                          "narrative_citation ci JOIN narrative_chapter ch ON ch.id=ci.chapter_id LEFT JOIN "
                          "narrative_section s ON s.id=ci.section_id WHERE ci.last_version IS NULL AND "
                          "ci.verse_id IS NULL ORDER BY ch.reading_order, s.ordinal"):
        if unresolved(vx, r["ref_normalised"], None):
            problems.append(f"Ch {r['chapter_no']} *{r['heading'] or '(opening)'}*: reference "
                            f"'{r['ref_as_written']}' read as {r['ref_normalised']} matches no verse")
    for r in conn.execute("SELECT c.claim_ref, s.ref_as_written, s.ref_normalised FROM narrative_claim_source s "
                          "JOIN narrative_claim c ON c.id=s.claim_id WHERE s.source_kind='verse' AND "
                          "s.verse_id IS NULL"):
        if unresolved(vx, r["ref_normalised"] or "", None):
            problems.append(f"claim {r['claim_ref']} source '{r['ref_as_written']}' read as "
                            f"{r['ref_normalised']} matches no verse")
    # the chapter table is the authority for the chapters (#2155)
    notices: list[str] = []
    no_file = cfg.required_setting("narrative.chapter_kinds_without_file") or []
    for ch in chs:
        if not ch["kind"] or not ch["purpose"]:
            problems.append(f"Ch {ch['chapter_no']}: no {'kind' if not ch['kind'] else 'purpose'} -- "
                            f"set it with EditChapter -Kind/-Purpose")
        if not ch["current_file"] and ch["kind"] and ch["kind"] not in no_file:
            problems.append(f"Ch {ch['chapter_no']}: a {ch['kind']!r} chapter with no current file")
        if ch["created_by"] == "direct edit":
            notices.append(f"Ch {ch['chapter_no']}: row inserted outside the tool (created_by 'direct edit')")
    for order, nos in conn.execute("SELECT reading_order, GROUP_CONCAT(chapter_no, ', ') FROM narrative_chapter "
                                   "WHERE inactive=0 GROUP BY reading_order HAVING COUNT(*) > 1"):
        problems.append(f"reading order {order} is shared by Ch {nos}")
    current = {ch["current_file"] for ch in chs if ch["current_file"]}
    for f in sorted(x.name for x in chapter_dir(cfg).glob("*.md")):
        if f not in current:
            problems.append(f"{f} is in the narrative folder but is no chapter's current file "
                            f"(it is not published)")
    # every enumerated column holds only its cfg_enum values (a direct edit is not checked on entry)
    for table, col, allowed in (
            ("narrative_chapter", "state", cfg.enum("narrative_chapter_state")),
            ("narrative_chapter", "kind", cfg.enum("narrative_chapter_kind")),
            ("narrative_claim", "origin", cfg.enum("narrative_claim_origin")),
            ("narrative_claim", "verdict", cfg.enum("narrative_claim_verdict")),
            ("narrative_claim", "part_verdict", cfg.enum("narrative_claim_verdict")),
            ("narrative_claim", "status", cfg.enum("narrative_claim_status")),
            ("narrative_claim_source", "source_kind", cfg.enum("narrative_claim_source_kind")),
            ("narrative_claim_telling", "kind", cfg.enum("narrative_telling_kind")),
            ("narrative_claim_telling", "status", cfg.enum("narrative_telling_status")),
            ("narrative_claim_change", "change_kind", cfg.enum("narrative_claim_change_kind")),
            ("narrative_claim_change", "basis", cfg.enum("narrative_change_basis")),
            ("narrative_update_ref", "kind", cfg.enum("narrative_update_ref_kind"))):
        for v, n in conn.execute(f'SELECT "{col}", COUNT(*) FROM "{table}" WHERE "{col}" IS NOT NULL '
                                 f'GROUP BY 1'):
            if v not in allowed:
                problems.append(f"{table}.{col}: {n} row(s) hold {v!r}, not one of {allowed}")
    lines = ["# Narrative register check", "", f"{len(chs)} active chapter(s) checked. "
             f"{len(problems)} finding(s).", ""] + [f"- {x}" for x in problems]
    if notices:
        lines += ["", "## Notices (history, not findings)", ""] + [f"- {x}" for x in notices]
    return lines, ([f"{len(problems)} finding(s), {len(notices)} notice(s)"] + problems[:20])


# ══ export (spec sec8) ══════════════════════════════════════════════════════════════════════════
def export(cfg) -> list[pathlib.Path]:
    conn = cfg.conn
    date = _today()
    header = PUBLISHED_HEADER.format(date=date)
    vx = VerseIndex(cfg)
    out = []
    # 1. the register
    L = ["# Narrative claim register", "", header, ""]
    chapters = conn.execute("SELECT * FROM narrative_chapter WHERE inactive=0 ORDER BY reading_order").fetchall()
    L += ["## Chapters", "",
          "What each chapter is for, from the chapter table (the authority for the chapters, #2155).", "",
          "| No. | Title | Kind | State | Purpose | Ruling |", "|---|---|---|---|---|---|"]
    for ch in chapters:
        L.append(f"| {ch['chapter_no']} | {_cell(ch['title'])} | {ch['kind'] or '—'} | {ch['state']} | "
                 f"{_cell(ch['purpose']) or '—'} | {_cell(ch['purpose_ref']) or '—'} |")
    L.append("")
    for n in conn.execute("SELECT * FROM narrative_index_note ORDER BY ordinal"):
        L += [f"## {n['heading']}", "", n["text"], ""]
    L += ["## Chapters, sections and the claims told there", ""]
    for ch in chapters:
        L += [f"### {ch['chapter_no']} — {ch['title']}", "",
              f"File `{ch['current_file'] or '—'}` (v{ch['current_version'] or '—'}) · {ch['state']}"
              f" · {ch['kind'] or '—'}", ""]
        for s in conn.execute("SELECT * FROM narrative_section WHERE chapter_id=? AND last_version IS NULL "
                              "ORDER BY ordinal", (ch["id"],)):
            told = conn.execute(
                "SELECT DISTINCT c.id, c.claim_ref, c.claim_text, t.kind, t.part_told FROM narrative_claim_telling t "
                "JOIN narrative_passage p ON p.id=t.passage_id JOIN narrative_claim c ON c.id=t.claim_id WHERE "
                "p.section_id=? AND t.status='current' AND p.last_version IS NULL ORDER BY p.ordinal, c.id",
                (s["id"],)).fetchall()
            if not told:
                continue
            L.append(f"**{s['heading']}**")
            L.append("")
            for t in told:
                others = [x for x in _told_in(conn, t["id"]) if not x.startswith(f"{ch['chapter_no']} *{s['heading']}*")]
                L.append(f"- **{t['claim_ref']}** {t['claim_text']} ({t['kind']}"
                         f"{': ' + t['part_told'] if t['part_told'] else ''})"
                         + (f" — also told in: {'; '.join(others)}" if others else ""))
            L.append("")
    L += ["## The original essay claims", ""]
    for oc in [r[0] for r in conn.execute("SELECT DISTINCT original_chapter FROM narrative_claim WHERE "
                                          "origin='original essay' ORDER BY id")]:
        L += [f"### {oc}", "", "| # | Original claim | Verdict | Claim now | Told in |", "|---|---|---|---|---|"]
        for c in conn.execute("SELECT * FROM narrative_claim WHERE origin='original essay' AND original_chapter "
                              "IS ? ORDER BY id", (oc,)):
            v = c["verdict"] or ""
            if c["part_verdict"]:
                v += f" / {c['part_verdict']} ({c['part_scope'] or ''})"
            L.append(f"| {c['claim_ref']} | {_cell(c['original_wording'])} | {_cell(v)} | {_cell(c['claim_text'])} | "
                     f"{'; '.join(_told_in(conn, c['id'])) or '—'} |")
        L.append("")
    L += ["## Claims not in the narrative", "", "| # | Claim | Status | Verdict |", "|---|---|---|---|"]
    for c in conn.execute("SELECT * FROM narrative_claim WHERE in_narrative=0 ORDER BY id"):
        L.append(f"| {c['claim_ref']} | {_cell(c['claim_text'])} | {c['status']} | {c['verdict'] or ''} |")
    L += ["", "## Tally", "", "| Origin | Verdict | Claims |", "|---|---|---|"]
    for r in conn.execute("SELECT origin, COALESCE(verdict, '—') v, COUNT(*) n FROM narrative_claim GROUP BY 1, 2 "
                          "ORDER BY 1, 2"):
        L.append(f"| {r['origin']} | {r['v']} | {r['n']} |")
    tot = conn.execute("SELECT COUNT(*), SUM(in_narrative) FROM narrative_claim").fetchone()
    L += ["", f"{tot[0]} claims; {tot[1] or 0} told in the narrative, {tot[0] - (tot[1] or 0)} not."]
    out.append(_write(cfg.setting("narrative.claim_register_path"), L))
    # 2. the change log
    L = ["# Narrative claim changes", "", header, ""]
    for u in conn.execute("SELECT * FROM narrative_update ORDER BY update_date DESC, id DESC"):
        L += [f"## {u['update_date']} — {u['title']}", ""]
        for lbl, col in (("Strand", "strand"), ("Researcher", "researcher_instruction"), ("Method", "method"),
                         ("Sources", "source_files"), ("Scripts", "scripts"),
                         ("Original claims changed", "claims_changed_note"), ("Not woven", "not_woven_note"),
                         ("Notes", "notes")):
            if u[col]:
                L.append(f"**{lbl}:** {u[col]}")
                L.append("")
        refs = [f"{r['kind']} {r['value']}" for r in conn.execute(
            "SELECT kind, value FROM narrative_update_ref WHERE update_id=? ORDER BY id", (u["id"],))]
        if refs:
            L += [f"**Refs:** {', '.join(refs)}", ""]
        if u["quote_parts"] is not None:
            L += [f"**Quote check:** {u['quote_parts']} parts, {u['quote_failures'] or 0} failures"
                  f"{'. ' + u['quote_note'] if u['quote_note'] else ''}", ""]
        L += _change_lines(conn, "x.update_id=?", (u["id"],))
    L += ["## Direct edits (no update)", ""] + _change_lines(conn, "x.update_id IS NULL", ())
    L += ["## Structure log", "", "| Date | Strand | Change | Reason |", "|---|---|---|---|"]
    for u in conn.execute("SELECT * FROM narrative_update WHERE structure_change IS NOT NULL ORDER BY update_date, id"):
        L.append(f"| {u['update_date']} | {_cell(u['strand'])} | {_cell(u['structure_change'])} | "
                 f"{_cell(u['structure_reason'])} |")
    out.append(_write(cfg.setting("narrative.claim_changes_path"), L))
    # 3. the citation index
    L = ["# Narrative citation index", "", header, ""]
    cites: dict[str, list[str]] = {}
    for r in conn.execute("SELECT ci.ref_normalised, ch.chapter_no, s.heading, ci.quoted, ci.verse_id FROM "
                          "narrative_citation ci JOIN narrative_chapter ch ON ch.id=ci.chapter_id LEFT JOIN "
                          "narrative_section s ON s.id=ci.section_id WHERE ci.last_version IS NULL ORDER BY "
                          "ch.reading_order, s.ordinal"):
        cites.setdefault(r["ref_normalised"], []).append(
            f"{r['chapter_no']} *{r['heading'] or '(opening)'}*{' (quoted)' if r['quoted'] else ''}"
            f"{' (no verse row)' if r['verse_id'] is None else ''}")
    rests: dict[str, list[str]] = {}
    for r in conn.execute("SELECT s.ref_normalised, c.claim_ref FROM narrative_claim_source s JOIN narrative_claim c "
                          "ON c.id=s.claim_id WHERE s.source_kind='verse' ORDER BY c.id"):
        rests.setdefault(r["ref_normalised"], []).append(r["claim_ref"])
    L += ["| Verse | Cited in | Claims resting on it |", "|---|---|---|"]
    for ref in sorted(set(cites) | set(rests), key=vx.sort_key):
        L.append(f"| {ref} | {'; '.join(cites.get(ref, [])) or '—'} | {', '.join(rests.get(ref, [])) or '—'} |")
    out.append(_write(cfg.setting("narrative.citation_index_path"), L))
    return out


def _change_lines(conn, where: str, args) -> list[str]:
    L = []
    for r in conn.execute(
            f"SELECT x.*, c.claim_ref, ch.chapter_no, s.heading FROM narrative_claim_change x JOIN narrative_claim c "
            f"ON c.id=x.claim_id LEFT JOIN narrative_chapter ch ON ch.id=x.chapter_id LEFT JOIN narrative_section s "
            f"ON s.id=x.section_id WHERE {where} ORDER BY x.change_date DESC, x.id", args):
        where_s = (f" · {r['chapter_no']}" + (f" *{r['heading']}*" if r["heading"] else "")) if r["chapter_no"] else ""
        L.append(f"- **{r['claim_ref']}** {r['change_kind']}{where_s} ({r['basis']}, {r['change_date']})")
        for lbl, a, b in (("claim", r["claim_before"], r["claim_after"]),
                          ("verdict", r["verdict_before"], r["verdict_after"]),
                          ("passage", r["passage_before"], r["passage_after"])):
            if (a is not None or b is not None) and a != b:
                L.append(f"  - {lbl} before: {_cell(a) if a is not None else '—'}")
                L.append(f"  - {lbl} after: {_cell(b) if b is not None else '—'}")
        if r["note"]:
            L.append(f"  - note: {_cell(r['note'])}")
    return L + [""]


def _write(rel: str, lines: list[str]) -> pathlib.Path:
    path = PROJECT_ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path
