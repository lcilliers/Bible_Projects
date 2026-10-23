"""readingindex.py -- the cluster reading index (escalation #2228 tool 2; design
outputs/escalation/2228-cluster-reading-index-design-v1-20261023.md, approved 2026-10-23 with a guard on
time and size).

Reads the study files under the folders in reading_index.roots (archive/ folders skipped) once, and records
for every verse reference in them the file, the heading section and the line where it stands:
reading_file, reading_section, reading_ref. Afterwards "what do the files say about these verses" is a query,
not a read of the files.

- References by narrativeregister.parse_refs over the whole file, so a follow-on takes its book from the
  reference before it; bare follow-ons '(220)' are not taken (mostly word counts). Each reference keeps how
  it was found: explicit (a book named), follow-on c:v, follow-on v.
- A whole-chapter reference is kept as a chapter (book, chapter), not spread over its verses.
- A reference that resolves to nothing is kept with its reason; the files are never edited.
- Incremental: a file is read again only when its sha256 changes; its earlier rows are kept, marked
  deleted (no physical delete). A file gone or archived is marked removed and its rows deleted. A build stops between files once reading_index.max_seconds is
  passed; the next build carries on.
"""
from __future__ import annotations

import bisect
import datetime
import hashlib
import pathlib
import re
import time

from . import narrativeregister as nr
from .manifest import in_archive

HEAD = re.compile(r"^(#{1,4}) +(.*?)\s*$", re.M)
CLUSTER_DIR = re.compile(r"^([MT]\d+[a-z]?) - ")
EXPLICIT = re.compile(r"\s*(?:Song|(?:[123]\s?)?[A-Z][a-z])")


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def files_in_roots(root: pathlib.Path, roots: list[str]) -> list[str]:
    """Every .md file under the roots, as repo-relative posix paths, archive/ folders left out."""
    out = []
    for r in roots:
        base = root / r
        if base.is_dir():
            out += [p.relative_to(root).as_posix() for p in base.rglob("*.md")]
    return sorted(p for p in set(out) if not in_archive(p))


def line_kind(line: str) -> str:
    s = line.lstrip()
    if s.startswith("#"):
        return "heading"
    if s.startswith("|"):
        return "table row"
    if re.match(r"([-*+]|\d+[.)])\s", s):
        return "bullet"
    return "paragraph"


def found_by(as_written: str) -> str:
    if EXPLICIT.match(as_written):
        return "explicit"
    return "follow-on c:v" if ":" in as_written else "follow-on v."


def _reason(vx: nr.VerseIndex, normalised: str, kind: str) -> str | None:
    """Why a reference resolves to nothing, or None when it resolves."""
    m = re.fullmatch(r"(\S+) (\d+)(?::(\d+))?", normalised)
    if not m:
        return "not a reference the verse table knows"
    book, ch = m.group(1), int(m.group(2))
    if kind == "whole chapter":
        return None if (book, ch) in vx.last_verse else "the book has no such chapter"
    if vx.single_chapter(book) and m.group(3) is None:
        ch, v = 1, int(m.group(2))
    else:
        v = int(m.group(3))
    last = vx.last_verse.get((book, ch))
    if last is None:
        return "the book has no such chapter"
    if v > last:
        return "verse past the end of the chapter"
    return "no verse row (by design: governance.verse_gap_by_design)"


def parse_file(text: str, vx: nr.VerseIndex) -> tuple[list[dict], list[dict]]:
    """(sections, refs) for one file. Section 0 is the opening before the first heading."""
    heads = list(HEAD.finditer(text))
    line_starts = [0] + [i + 1 for i, ch in enumerate(text) if ch == "\n"]
    lines = text.split("\n")

    def line_no(offset: int) -> int:
        return bisect.bisect_right(line_starts, offset)

    sections, stack = [{"ordinal": 0, "level": 0, "heading": "(opening)", "path": "", "line_start": 1}], []
    for i, h in enumerate(heads, start=1):
        level = len(h.group(1))
        while stack and stack[-1][0] >= level:
            stack.pop()
        path = " > ".join(t for _, t in stack)
        stack.append((level, h.group(2)))
        sections.append({"ordinal": i, "level": level, "heading": h.group(2), "path": path,
                         "line_start": line_no(h.start())})
    for i, s in enumerate(sections):
        s["line_end"] = sections[i + 1]["line_start"] - 1 if i + 1 < len(sections) else len(lines)
    starts = [0] + [h.start() for h in heads]
    refs = []
    for r in nr.parse_refs(text, vx, bare_follow_ons=False):
        sec = bisect.bisect_right(starts, r.start) - 1
        ln = line_no(r.start)
        m = re.fullmatch(r"(\S+) (\d+)(?::\d+)?", r.normalised)
        refs.append({"section": sec, "verse_id": r.verse_id,
                     "book": m.group(1) if m else None, "chapter": int(m.group(2)) if m and r.kind == "whole chapter" else None,
                     "ref_as_written": r.as_written, "ref_normalised": r.normalised, "kind": r.kind,
                     "found_by": found_by(r.as_written), "line_no": ln, "line_kind": line_kind(lines[ln - 1]),
                     "reason": None if r.verse_id else _reason(vx, r.normalised, r.kind)})
    return sections, refs


def _cluster(rel: str, roots: list[str]) -> str | None:
    for r in roots:
        prefix = r.rstrip("/") + "/"
        if rel.startswith(prefix):
            first = rel[len(prefix):].split("/")[0]
            m = CLUSTER_DIR.match(first)
            return m.group(1) if m else None
    return None


def _retire_rows(w, fid: int) -> None:
    w.update("reading_ref", {"file_id": fid, "deleted": 0}, {"deleted": 1})
    w.update("reading_section", {"file_id": fid, "deleted": 0}, {"deleted": 1})


def build(cfg, w, root: pathlib.Path) -> str:
    """Index new and changed files, mark removed ones; stops between files after reading_index.max_seconds.
    `w` is a narrativeregister.Writer for the step (its write grants are checked on every insert/update)."""
    conn = cfg.conn
    roots = list(cfg.required_setting("reading_index.roots"))
    max_seconds = float(cfg.required_setting("reading_index.max_seconds"))
    t0 = time.monotonic()
    vx = nr.VerseIndex(cfg)
    on_disk = files_in_roots(root, roots)
    known = {r["path"]: r for r in conn.execute("SELECT id, path, sha256, removed FROM reading_file")}
    done = unchanged = 0
    left = []
    for i, rel in enumerate(on_disk):
        data = (root / rel).read_bytes()
        sha = hashlib.sha256(data).hexdigest()
        row = known.get(rel)
        if row and row["sha256"] == sha and not row["removed"]:
            unchanged += 1
            continue
        if time.monotonic() - t0 > max_seconds:
            left = on_disk[i:]
            break
        text = data.decode("utf-8", errors="replace").replace("\r\n", "\n")   # as a text read sees the file
        sections, refs = parse_file(text, vx)
        name = pathlib.PurePosixPath(rel).name
        imported = conn.execute("SELECT count(*) FROM ib_observation WHERE revisit_note LIKE ?",
                                (f"%{name}%",)).fetchone()[0]
        fields = {"cluster": _cluster(rel, roots), "size_bytes": len(data), "sha256": sha, "indexed_at": _now(),
                  "sections": len(sections), "refs": len(refs), "imported_observations": imported, "removed": 0}
        if row:
            fid = row["id"]
            _retire_rows(w, fid)            # soft delete: the earlier reading of the file stays as history
            w.update("reading_file", {"id": fid}, fields)
        else:
            fid = w.insert("reading_file", {"path": rel, **fields})
        sec_ids = [w.insert("reading_section", {"file_id": fid, **s}) for s in sections]
        for r in refs:
            w.insert("reading_ref", {"file_id": fid, "section_id": sec_ids[r.pop("section")], **r})
        conn.commit()                       # a build stopped at the time limit keeps what it did
        done += 1
    gone = [p for p, r in known.items() if not r["removed"] and p not in set(on_disk)]
    for p in gone:
        w.update("reading_file", {"id": known[p]["id"]}, {"removed": 1, "indexed_at": _now()})
        _retire_rows(w, known[p]["id"])
    conn.commit()
    msg = (f"{done} file(s) indexed, {unchanged} unchanged, {len(gone)} marked removed "
           f"({time.monotonic() - t0:.1f}s)")
    if left:
        msg += (f"; stopped at the time limit (reading_index.max_seconds {max_seconds:g}) with {len(left)} "
                f"file(s) still to index -- run Build again to carry on")
    return msg


def report(cfg, params: dict) -> tuple[list[str], str]:
    """The coverage report from the tables (read-only)."""
    conn = cfg.conn
    q = lambda sql, *a: conn.execute(sql, a).fetchall()  # noqa: E731
    live = "deleted=0 AND file_id IN (SELECT id FROM reading_file WHERE removed=0)"
    tot = q(f"SELECT count(*), sum(verse_id IS NOT NULL), sum(kind='whole chapter'), "
            f"sum(verse_id IS NULL AND kind='verse'), count(DISTINCT verse_id) FROM reading_ref WHERE {live}")[0]
    files = q("SELECT count(*), sum(refs=0), sum(imported_observations>0), max(indexed_at) FROM reading_file WHERE removed=0")[0]
    removed = q("SELECT count(*) FROM reading_file WHERE removed=1")[0][0]
    L = ["# Cluster reading index -- coverage", "",
         f"> Generated by `Reading-Index.ps1 -Step Report` from reading_file, reading_section and reading_ref "
         f"(escalation #2228). Roots: {', '.join(cfg.required_setting('reading_index.roots'))}. Last indexed "
         f"{files[3]}.", "",
         f"- **Files:** {files[0]} live ({files[1]} with no reference; {files[2]} whose rows are also in "
         f"ib_observation, imported); {removed} removed.",
         f"- **References:** {tot[0]}: {tot[1]} to a verse ({tot[4]} distinct verses), {tot[2]} to a whole "
         f"chapter, {tot[3]} to nothing.", "",
         "## By folder", "",
         "| cluster | files | sections | sections with a reference | references | to a verse | to nothing |",
         "|---|---|---|---|---|---|---|"]
    for r in q(f"""SELECT coalesce(f.cluster, '(root)') c, count(DISTINCT f.id),
                  (SELECT count(*) FROM reading_section s JOIN reading_file g ON g.id=s.file_id
                    WHERE g.removed=0 AND s.deleted=0 AND coalesce(g.cluster,'(root)')=coalesce(f.cluster,'(root)')),
                  (SELECT count(DISTINCT x.section_id) FROM reading_ref x JOIN reading_file g ON g.id=x.file_id
                    WHERE g.removed=0 AND x.deleted=0 AND coalesce(g.cluster,'(root)')=coalesce(f.cluster,'(root)')),
                  sum(f.refs),
                  (SELECT count(*) FROM reading_ref x JOIN reading_file g ON g.id=x.file_id
                    WHERE g.removed=0 AND x.deleted=0 AND x.verse_id IS NOT NULL AND coalesce(g.cluster,'(root)')=coalesce(f.cluster,'(root)')),
                  (SELECT count(*) FROM reading_ref x JOIN reading_file g ON g.id=x.file_id
                    WHERE g.removed=0 AND x.deleted=0 AND x.verse_id IS NULL AND x.kind='verse' AND coalesce(g.cluster,'(root)')=coalesce(f.cluster,'(root)'))
                  FROM reading_file f WHERE f.removed=0 GROUP BY c ORDER BY c"""):
        L.append("| " + " | ".join(str(x) for x in r) + " |")
    L += ["", "## How the references were found", "", "| found by | line kind | references |", "|---|---|---|"]
    for r in q(f"SELECT found_by, line_kind, count(*) FROM reading_ref WHERE {live} GROUP BY 1, 2 ORDER BY 1, 2"):
        L.append(f"| {r[0]} | {r[1]} | {r[2]} |")
    L += ["", "## References that resolve to nothing", "", "| reason | references |", "|---|---|"]
    for r in q(f"SELECT reason, count(*) FROM reading_ref WHERE {live} AND verse_id IS NULL AND reason IS NOT NULL "
               f"GROUP BY 1 ORDER BY 2 DESC"):
        L.append(f"| {r[0]} | {r[1]} |")
    L += ["", "| file | line | as written | read as | reason |", "|---|---|---|---|---|"]
    for r in q(f"SELECT f.path, x.line_no, x.ref_as_written, x.ref_normalised, x.reason FROM reading_ref x "
               f"JOIN reading_file f ON f.id=x.file_id WHERE f.removed=0 AND x.deleted=0 AND x.verse_id IS NULL AND x.reason IS NOT NULL "
               f"ORDER BY f.path, x.line_no"):
        L.append(f"| {r[0]} | {r[1]} | {str(r[2]).replace('|', '/')} | {r[3]} | {r[4]} |")
    L += ["", "## Files with no reference", ""]
    L += [f"- {r[0]}" for r in q("SELECT path FROM reading_file WHERE removed=0 AND refs=0 ORDER BY path")]
    return L, f"{files[0]} files; {tot[0]} references ({tot[4]} distinct verses); {tot[3]} to nothing"
