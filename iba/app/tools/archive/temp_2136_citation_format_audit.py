"""temp_2136_citation_format_audit -- escalation #2136, one-off read-only audit (2026-10-13).

Researcher, chat 2026-10-13 (verbatim): "2136 confirm that the citation references has a
consistent format throughout the narative that is consistent with the config and verse table".

The rules checked:
- style guide (cfg_setting narrative.inner_being_style_guide_path) section 5: the full book name in
  chapter text; verse numbers alone after the first reference to a chapter; witnesses separated
  by semicolons
- cfg_setting narrative.book_alias_map: every book token is one the register can read
- the verse table: every reference resolves (narrativeregister.unresolved)

Each current chapter file (narrative_chapter.current_file) is read, never written. The report goes to
cfg_setting narrative.register_report_dir.

    python -m iba.app.tools.temp_2136_citation_format_audit
"""
from __future__ import annotations

import collections
import pathlib
import re
import sys

from ..lib import narrativeregister as nr
from ..lib.cfg import Cfg

# a book-like token followed by chapter:verse, whatever the spelling (to find what the parser skips)
_ANY_REF = re.compile(r"(?<![\w.])((?:[123]\s?)?[A-Z][a-z]+(?:\sof\s[A-Z][a-z]+)?)\.?\s(\d+:\d+)")
_HYPHEN_RANGE = re.compile(r"\d+:\d+-\d+|\(\d+-\d+\)")
_VERSE_WORD = re.compile(r"\b(?:v\.|vv\.|verses?)\s?\d+", re.I)
_BARE_CV = re.compile(r"\(\d+:\d+")
# a capitalised word before chapter:verse that is plainly prose, not a book
_NOT_BOOK = {"Chapter", "Ch", "Part", "Section", "See", "And", "In", "At", "Then", "Version"}


def main() -> int:
    cfg = Cfg()
    vx = nr.VerseIndex(cfg)
    conn = cfg.conn
    full: dict[str, str] = {}                       # code -> longest alias = the full name
    for alias, code in vx.alias.items():
        if len(alias) > len(full.get(code, "")):
            full[code] = alias
    forms: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    short_forms, unknown, orphan_fo, hyphen, verse_word, unresolved_rows = [], [], [], [], [], []
    n_named = n_follow = n_pass = 0
    d = nr.chapter_dir(cfg)
    chapters = conn.execute("SELECT chapter_no, current_file FROM narrative_chapter WHERE current_file "
                            "IS NOT NULL ORDER BY chapter_no").fetchall()
    for no, f in chapters:
        _, sections, passages = nr.parse_chapter((d / f).read_text(encoding="utf-8"))
        for ps in passages:
            n_pass += 1
            t = ps.text
            where = f"Ch {no} *{sections[ps.section].heading}*"
            first_named = None
            for m in nr._REF_RX.finditer(t):
                code = vx.book(m.group("book"))
                if not code:
                    continue
                n_named += 1
                first_named = m.start() if first_named is None else first_named
                token = m.group("book")
                forms[code][token] += 1
                if token.lower().replace(" ", "") != full[code]:
                    short_forms.append(f"{where}: '{m.group(0)}' (the full name reads as '{full[code]}')")
            for m in _ANY_REF.finditer(t):
                tok = m.group(1)
                if tok.split()[-1] in _NOT_BOOK or vx.book(tok):
                    continue
                unknown.append(f"{where}: '{m.group(0)}' ('{tok}' is not in narrative.book_alias_map)")
            for m in _BARE_CV.finditer(t):
                if first_named is None or m.start() < first_named:
                    orphan_fo.append(f"{where}: '{t[m.start():m.start() + 14]}…' comes before any named "
                                     f"reference in its paragraph, so it cites nothing")
            for r in nr.parse_refs(t, vx):
                if not re.search(r"[A-Za-z]", r.as_written):
                    n_follow += 1
                if nr.unresolved(vx, r.normalised, r.verse_id):
                    unresolved_rows.append(f"{where}: '{r.as_written}' read as {r.normalised}")
            hyphen += [f"{where}: '{m.group(0)}'" for m in _HYPHEN_RANGE.finditer(t)]
            verse_word += [f"{where}: '{m.group(0)}'" for m in _VERSE_WORD.finditer(t)]
    multi = {c: dict(v) for c, v in forms.items() if len(v) > 1}
    src_unres = [f"claim {r[0]}: '{r[1]}' read as {r[2]}" for r in conn.execute(
        "SELECT c.claim_ref, s.ref_as_written, s.ref_normalised FROM narrative_claim_source s JOIN "
        "narrative_claim c ON c.id=s.claim_id WHERE c.status='current' AND s.source_kind='verse' AND "
        "s.verse_id IS NULL").fetchall() if nr.unresolved(vx, r[2], None)]

    def block(title, rows, none="none"):
        return [f"## {title} ({len(rows)})", ""] + ([f"- {x}" for x in rows] or [f"- {none}"]) + [""]

    lines = ["# Narrative citation format audit (#2136)", "",
             f"> Read-only. {len(chapters)} current chapter files, {n_pass} paragraphs, {n_named} named "
             f"references, {n_follow} follow-on verses. Rules: style guide §5 (full book name; verse "
             f"numbers alone after the first reference to a chapter; semicolons between witnesses), "
             f"`narrative.book_alias_map`, the `verse` table.", ""]
    lines += block("Book named in a short form", short_forms)
    lines += block("Book spelled more than one way", [f"{c}: {v}" for c, v in sorted(multi.items())])
    lines += block("Book token not in the alias map (the register skips it)", unknown)
    lines += block("Follow-on before any named reference (cites nothing)", orphan_fo)
    lines += block("Range written with a hyphen, not an en dash", hyphen)
    lines += block("'v.' / 'verse' wording", verse_word)
    lines += block("Chapter references that match no verse row", unresolved_rows)
    lines += block("Current claim sources that match no verse row", src_unres)
    out = pathlib.Path(cfg.setting("narrative.register_report_dir")) / "narrative-citation-format-audit-2136.md"
    from ..lib import reportkit
    path = reportkit.write_report(conn, "temp_2136_citation_format_audit", out, lines)
    print(path)
    for ln in lines[2:]:
        if ln.startswith("## "):
            print(" ", ln[3:])
    return 0


if __name__ == "__main__":
    sys.exit(main())
