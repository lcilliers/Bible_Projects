"""narrative_claim_register_import_v1_20261013.py -- escalation #2110, build steps 6 and 7: the
register's recorded history into iba.db.

Specification sec6 (approved 2026-10-13): `_analytics/essay/spirit_soul_body/wa-essay-narrative-
record-db-specification-v1-20261013.md`. The #2000 pattern: scripts write a PREVIEW and a REVIEW
LIST; nothing is written to iba.db before the researcher approves; then the approved preview is
imported as it stands.

  --preview (default, read-only on iba.db)
      R1  claim register v1 -> v51, each pair compared: the original claims as first recorded and
          every later edit to them, before and after, dated by the version
      R2  the 53 dated sections of v51: one update each; every table line accounted for -- a line
          that names an original claim is attached to it, every other line is a recorded change to
          the narrative held for the R0 correlation (claims are read chapter by chapter later)
      R3  the narrative index: chapters, the per-version notes, the Structure log, the text blocks
      R5  the imputed-readings audit (#1921, 88 edits) and the register's Correction section
      R6  digest sec4: the new areas introduced at the 2026-09-30 reset
      plus the current sections (headings) of the 33 chapter files and the current citations
  --apply --preview-file <json>   (build step 7, after approval; refuses a second run)

Writes nothing but the preview files in --preview. Usage:
    python -m iba.app.migration.narrative_claim_register_import_v1_20261013 [--preview] [--out-dir DIR]
    python -m iba.app.migration.narrative_claim_register_import_v1_20261013 --apply --preview-file <json>
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import sqlite3
import sys

from iba.app.lib import narrativeregister as nr
from iba.app.lib.cfg import Cfg

ROOT = pathlib.Path(__file__).resolve().parents[3]
_cfg = Cfg()
NARR = ROOT / _cfg.setting("narrative.copy_source_dir")      # the chapter files (config, not a literal)
_cfg.close()
ESSAY = NARR.parent                                          # the register, audit and digest beside it
REGISTER_GLOB = "wa-essay-spirit-soul-body-claim-register-v*-*.md"
INDEX = NARR / "00-index-and-status-v1-20260930.md"
AUDIT = ESSAY / "wa-essay-narrative-imputed-readings-audit-v1-20261001.md"
DIGEST = ESSAY / "wa-essay-spirit-soul-body-digest-v1-20260930.md"
STAMP = "v1-20261013"
NL = chr(10)
CLAIM_ID = re.compile(r"^(?:I|K|\d{1,2})-\d{1,2}$")
VERDICTS = ["Stands", "Widened", "Restated", "Withdrawn", "Held", "Added", "New", "Removed", "Corrected"]


# ── markdown helpers ───────────────────────────────────────────────────────────────────────────
def cells(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", s)]


def is_sep(line: str) -> bool:
    return bool(re.fullmatch(r"\s*\|[\s:|-]+\|\s*", line))


def unbold(s: str) -> str:
    return re.sub(r"\*\*(.+?)\*\*", r"\1", s or "").strip()


def file_date(name: str) -> str | None:
    m = re.search(r"-(\d{4})(\d{2})(\d{2})\.md$", name)
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else None


def file_v(name: str) -> int | None:
    m = re.search(r"-v(\d+)-\d{8}\.md$", name)
    return int(m.group(1)) if m else None


# ── R1: the claim register versions ────────────────────────────────────────────────────────────
def register_versions() -> list[tuple[int, pathlib.Path]]:
    files = list(ESSAY.glob(REGISTER_GLOB)) + list((ESSAY / "archive").glob(REGISTER_GLOB))
    out = sorted({(file_v(f.name), f) for f in files if file_v(f.name)}, key=lambda x: x[0])
    return out


def original_claims(text: str) -> dict[str, dict]:
    """claim id -> {chapter, original, verdict_cell, evidence, newch} from the chapter tables
    (every table with the header '# | Original claim | Verdict | Evidence and restatement | New ch')."""
    out: dict[str, dict] = {}
    chapter = None
    in_table = False
    for line in text.splitlines():
        h = re.match(r"^## (.+)$", line)
        if h:
            chapter = h.group(1).strip()
            in_table = False
            continue
        if line.startswith("| # | Original claim"):
            in_table = True
            continue
        if in_table and line.startswith("|"):
            if is_sep(line):
                continue
            c = cells(line)
            if len(c) >= 5 and CLAIM_ID.match(c[0]):
                out[c[0]] = {"chapter": chapter, "original": c[1], "verdict_cell": c[2],
                             "evidence": c[3], "newch": c[4]}
        elif in_table and not line.strip().startswith("|"):
            in_table = False
    return out


def parse_verdict(cell: str) -> tuple[str | None, str | None, str | None]:
    """'**Restated** (location) / **Held** (catalogue)' -> ('Restated', 'Held', 'Restated (location) / Held (catalogue)')."""
    found = [v for v in re.findall(r"\*\*([A-Za-z]+)\*\*", cell or "") if v in VERDICTS]
    if not found:
        found = [v for v in VERDICTS if re.search(rf"\b{v}\b", cell or "")][:1]
    main = found[0] if found else None
    part = found[1] if len(found) > 1 else None
    return main, part, (unbold(cell) if part else None)


def claim_text(c: dict) -> str:
    """The claim's own wording at that version (review list explains): a Restated claim is its
    correction (the evidence-and-restatement cell); every other verdict keeps the original wording."""
    main, _, _ = parse_verdict(c["verdict_cell"])
    return unbold(c["evidence"]) if main == "Restated" else unbold(c["original"])


def version_notes(text: str) -> dict[int, tuple[str, str]]:
    """'(v51: 2026-10-13, note; v50: 2026-10-12, note; ...' on the **Date:** line -> {51: (date, note)}."""
    line = next((l for l in text.splitlines() if l.startswith("**Date:**")), "")
    out = {}
    parts = re.split(r"(?:\(|;\s)(?=v\d+:\s)", line)
    for p in parts:
        m = re.match(r"v(\d+):\s*(\d{4}-\d{2}-\d{2})?,?\s*(.*)$", p.strip())
        if m:
            out[int(m.group(1))] = (m.group(2) or "", m.group(3).rstrip(") ").strip())
    return out


def r1_history(versions) -> tuple[dict[str, list[dict]], dict[str, dict], dict[int, set[str]], list[str]]:
    texts = {v: f.read_text(encoding="utf-8") for v, f in versions}
    notes = version_notes(texts[versions[-1][0]])
    hist: dict[str, list[dict]] = collections.defaultdict(list)
    first_seen: dict[str, dict] = {}
    sections_by_version: dict[int, set[str]] = {}
    review: list[str] = []
    prev: dict[str, dict] = {}
    for v, f in versions:
        t = texts[v]
        sections_by_version[v] = {h for h in re.findall(r"^## (.+)$", t, re.M)}
        cur = original_claims(t)
        date = notes.get(v, ("", ""))[0] or file_date(f.name)
        note = notes.get(v, ("", ""))[1]
        for cid, c in cur.items():
            if cid not in prev:
                vm, vp, vs = parse_verdict(c["verdict_cell"])
                first_seen[cid] = {"version": v, **c}
                hist[cid].append({"change_date": date, "change_kind": "claim created",
                                  "claim_after": claim_text(c), "verdict_after": vm,
                                  "note": f"as first recorded in claim register v{v}: verdict cell "
                                          f"{unbold(c['verdict_cell'])!r}; evidence {unbold(c['evidence'])!r}; "
                                          f"new ch {c['newch']!r}",
                                  "basis": "recorded", "provenance": f.name, "register_version": v})
                continue
            p = prev[cid]
            if p == c:
                continue
            pv, cv = parse_verdict(p["verdict_cell"])[0], parse_verdict(c["verdict_cell"])[0]
            base = {"change_date": date, "basis": "recorded", "register_version": v,
                    "provenance": f"{versions[[x[0] for x in versions].index(v) - 1][1].name} -> {f.name}",
                    "version_note": note}
            if pv != cv or p["verdict_cell"] != c["verdict_cell"]:
                hist[cid].append({**base, "change_kind": "verdict changed", "verdict_before": pv,
                                  "verdict_after": cv,
                                  "note": f"verdict cell: {unbold(p['verdict_cell'])!r} -> {unbold(c['verdict_cell'])!r}"})
            if claim_text(p) != claim_text(c) or p["evidence"] != c["evidence"] or p["original"] != c["original"]:
                hist[cid].append({**base, "change_kind": "claim restated", "claim_before": claim_text(p),
                                  "claim_after": claim_text(c),
                                  "note": "evidence and restatement cell changed" if p["evidence"] != c["evidence"]
                                  else "original wording cell changed"})
            if p["newch"] != c["newch"]:
                hist[cid].append({**base, "change_kind": "renumbered" if v == 7 else "edited",
                                  "note": f"New ch: {p['newch']} -> {c['newch']}"})
            if p["chapter"] != c["chapter"]:
                review.append(f"{cid}: its essay chapter heading changed in v{v}: {p['chapter']!r} -> {c['chapter']!r}")
        for cid in prev:
            if cid not in cur:
                review.append(f"{cid}: present in v{v - 1} but missing from v{v} (kept from its last version)")
                cur[cid] = prev[cid]
        prev = cur
    return hist, prev, sections_by_version, review


# ── R2: the dated sections of the current register ──────────────────────────────────────────────
def dated_sections(text: str) -> list[dict]:
    out = []
    blocks = re.split(r"^(?=## )", text, flags=re.M)
    for b in blocks:
        h = re.match(r"^## (.+)$", b, re.M)
        if not h:
            continue
        title = h.group(1).strip()
        dm = re.search(r"\((\d{4}-\d{2}-\d{2})(?:,\s*([^)]*))?\)\s*$", title)
        if not dm:
            continue
        out.append({"heading": title, "date": dm.group(1), "refs_text": dm.group(2) or "",
                    "body": b[h.end():].strip("\n")})
    return out


def strand_of(title: str) -> str | None:
    m = re.match(r"Strand updates — ([^:(]+?)(?:[,:(]|$)", title)
    return m.group(1).strip() if m else None


def refs_of(s: str) -> list[dict]:
    out = []
    for m in re.finditer(r"#(\d{3,5})", s):
        out.append({"kind": "escalation", "value": m.group(1)})
    for m in re.finditer(r"\bOT-(\d+)(?:\.(\d+))?(?:/(\d+))?(?:/(\d+))?", s):
        out.append({"kind": "thread item" if m.group(2) else "thread",
                    "value": f"OT-{m.group(1)}" + (f".{m.group(2)}" if m.group(2) else "")})
        for extra in (m.group(3), m.group(4)):
            if extra:
                out.append({"kind": "thread", "value": f"OT-{extra}"})
    seen, uniq = set(), []
    for r in out:
        k = (r["kind"], r["value"])
        if k not in seen:
            seen.add(k)
            uniq.append(r)
    return uniq


_CH_RX = re.compile(r"^\s*(?:Ch(?:apter)?s?\.?\s*)?(\d{1,2}(?:\.\d{1,2})?)\b")
_CH_ALL = re.compile(r"(?<![\d.:§])(\d{1,2}(?:\.\d{1,2})?)(?:\s?[–-]\s?(\d{1,2}(?:\.\d{1,2})?))?(?![\d:])")


def chapter_of(where: str) -> str | None:
    m = _CH_RX.match(unbold(where).replace("*", ""))
    return m.group(1) if m else None


def chapters_in(where: str) -> list[str]:
    """Every chapter a 'Where'/'Section' cell names, ranges expanded: 'Ch 7, 9, 11, 13; 10.1, 10.5–10.9'
    -> 7, 9, 11, 13, 10.1, 10.5, 10.6, 10.7, 10.8, 10.9 (spec test 6.5). Only the cell's leading
    chapter list is read -- the text after the first word that is not a number or 'Ch' is a heading."""
    s = unbold(where).replace("*", "")
    head = re.match(r"^\s*(?:(?:Ch(?:apter)?s?\.?|§|and|,|;|\s|\d{1,2}(?:\.\d{1,2})?|[–-])+)", s)
    out: list[str] = []
    for a, b in _CH_ALL.findall(head.group(0) if head else ""):
        if b and "." in a and "." in b and a.split(".")[0] == b.split(".")[0]:
            out += [f"{a.split('.')[0]}.{i}" for i in range(int(a.split(".")[1]), int(b.split(".")[1]) + 1)]
        elif b and "." not in a and "." not in b:
            out += [str(i) for i in range(int(a), int(b) + 1)]
        else:
            out += [x for x in (a, b) if x]
    return list(dict.fromkeys(out))


def chapter_now(no: str, date: str, refs: list[dict]) -> str:
    """A chapter number written in a dated section, in today's numbering (spec test 6.6). The register
    note: dated sections 'keep the numbering in force on their date'. Two renumberings:
      #1920 (2026-10-01): 10.3-10.9 -> 10.4-10.10; 13 (Made new) -> 14; 14 -> 15 -- sections before it
          (#1918, #1919) use the old numbers;
      #1936 (2026-10-02): 09 -> 02; 02-08 -> 03-09 -- every section dated before 2026-10-02.
    Ch 13 written between #1920 and #1982 (2026-10-07) is the retired 'Under God's anger'."""
    escs = [int(r["value"]) for r in refs if r["kind"] == "escalation"]
    pre1920 = date <= "2026-10-01" and escs and max(escs) < 1920
    if pre1920:
        m = re.fullmatch(r"10\.(\d+)", no)
        if m and 3 <= int(m.group(1)) <= 9:
            no = f"10.{int(m.group(1)) + 1}"
        elif no in ("13", "14"):
            no = str(int(no) + 1)
    elif no == "13" and date < "2026-10-07":
        return "13 (retired: Under God's anger)"
    if date < "2026-10-02" and re.fullmatch(r"\d{1,2}", no) and 2 <= int(no) <= 9:
        no = "2" if int(no) == 9 else str(int(no) + 1)
    return no.zfill(2) if re.fullmatch(r"\d", no) else no


def parse_update(sec: dict, first_version: int | None) -> dict:
    body = sec["body"]
    lines = body.splitlines()
    prose, tables, cur_header, table_lines = [], [], None, 0
    for l in lines:
        if l.lstrip().startswith("|"):
            table_lines += 1
            if is_sep(l):
                continue
            c = cells(l)
            if cur_header is None:
                cur_header = c
                tables.append({"header": c, "rows": []})
            else:
                tables[-1]["rows"].append(c)
        else:
            cur_header = None
            prose.append(l)
    text = "\n".join(prose).strip()
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]

    def para(rx):
        hits = [p for p in paras if re.search(rx, p)]
        return "\n\n".join(hits) or None

    instr = re.findall(r"(?:Researcher|researcher)[^*\n]{0,80}?\*\"([^\n]+?)\"\*", text)
    qm = re.search(r"(\d+)\s+(?:quote[sd]?|quotations?)(?: parts)?(?: checked)?[^.\n]{0,40}?(\d+)\s+failures?", text)
    files = re.findall(r"`([^`]+\.(?:md|csv|json))`", text)
    scripts = re.findall(r"`([^`]+\.py)`", text)
    change_lines = []
    for t in tables:
        hdr = [unbold(h) for h in t["header"]]
        for row in t["rows"]:
            first = unbold(row[0]) if row else ""
            entry = {"header": hdr, "cells": row}
            ids = [x.strip() for x in re.split(r"[,;]|\band\b", first) if x.strip()]
            if ids and all(CLAIM_ID.match(x) for x in ids):      # one or several original claims
                entry.update({"kind": "original claim", "claim_ref": ids[0], "claim_refs": ids})
            else:
                written = chapters_in(first)
                refs = refs_of(sec["refs_text"] + " " + sec["heading"])
                entry.update({"kind": "narrative change", "where": first, "chapter_no": chapter_of(first),
                              "chapters_as_written": written,
                              "chapters_now": [chapter_now(x, sec["date"], refs) for x in written]})
            change_lines.append(entry)
    return {
        "key": f"R2:{sec['heading']}", "source": "R2", "update_date": sec["date"], "title": sec["heading"],
        "strand": strand_of(sec["heading"]), "refs": refs_of(sec["refs_text"] + " " + sec["heading"]),
        "researcher_instruction": "\n".join(dict.fromkeys(instr)) or None,
        "method": para(r"\brule \d+\b|\bmethod\b|by role|weave, don't fit"),
        "source_files": list(dict.fromkeys(files)), "scripts": list(dict.fromkeys(scripts)),
        "claims_changed_note": para(r"(?i)original claims? (?:changed|touched)|no original claim"),
        "not_woven_note": para(r"(?i)not woven|kept out|held, not woven"),
        "structure_change": None, "structure_reason": None,
        "quote_parts": int(qm.group(1)) if qm else None, "quote_failures": int(qm.group(2)) if qm else None,
        "quote_note": para(r"(?i)quote") if qm else None,
        "notes": body.strip() or None, "legacy_register_version": first_version,
        "provenance": "claim register v51 (dated section)", "table_lines": table_lines,
        "header_shapes": [" · ".join(unbold(h) for h in t["header"]) for t in tables],
        "change_lines": change_lines,
    }


# ── R3: the narrative index ────────────────────────────────────────────────────────────────────
def chapter_archive() -> dict[str, list[tuple[int, pathlib.Path]]]:
    """slug (file stem without its number prefix) -> [(version, path)] across current and archive."""
    out: dict[str, list] = collections.defaultdict(list)
    for f in list(NARR.glob("*.md")) + list((NARR / "archive").glob("*.md")):
        fv = nr.file_version(f.name)
        if not fv or f.name.startswith("00-index"):
            continue
        slug = re.sub(r"^\d{2}(?:-\d{2})?-", "", fv[0])
        out[slug].append((fv[1], f, fv[0][:2]))
    out = {k: sorted(set(v)) for k, v in out.items()}
    # a retitled chapter continues its versions under a new stem (Ch 11 Patterns of the inner life v30
    # -> Other sides of the inner being v31, #1998): an orphan series is joined to the current series
    # with the same number prefix whose first version follows its last
    current = {re.sub(r"^\d{2}(?:-\d{2})?-", "", nr.file_version(f.name)[0])
               for f in NARR.glob("*.md") if nr.file_version(f.name) and not f.name.startswith("00-index")}
    for orphan in [k for k in out if k not in current]:
        last_v, _, prefix = out[orphan][-1]
        for k in current:
            if out.get(k) and out[k][0][2] == prefix and out[k][0][0] == last_v + 1:
                out[k] = sorted(out[orphan] + out[k])
    return {k: [(v, f) for v, f, _ in vals] for k, vals in out.items()}


def parse_index(text: str) -> dict:
    chapters, structure, blocks = [], [], []
    sec = None
    buf: list[str] = []
    for line in text.splitlines():
        h = re.match(r"^## (.+)$", line)
        if h:
            if sec is not None:
                blocks.append((sec, "\n".join(buf).strip()))
            sec, buf = h.group(1).strip(), []
            continue
        buf.append(line)
    if sec is not None:
        blocks.append((sec, "\n".join(buf).strip()))
    notes = []
    for heading, body in blocks:
        tlines = [l for l in body.splitlines() if l.lstrip().startswith("|")]
        if tlines and cells(tlines[0])[:2] == ["#", "File"]:
            for l in tlines[2:]:
                chapters.append(cells(l))
            rest = "\n".join(l for l in body.splitlines() if not l.lstrip().startswith("|")).strip()
            if rest:
                notes.append({"heading": heading, "text": rest})
        elif tlines and cells(tlines[0])[:4] == ["Date", "Strand", "Change", "Reason"]:
            for l in tlines[2:]:
                structure.append(cells(l))
            rest = "\n".join(l for l in body.splitlines() if not l.lstrip().startswith("|")).strip()
            if rest:
                notes.append({"heading": heading, "text": rest})
        else:
            notes.append({"heading": heading, "text": body})
    head = text.split("\n## ", 1)[0].strip()
    if head:
        notes.insert(0, {"heading": "(index opening)", "text": head})
    return {"chapters": chapters, "structure": structure, "notes": notes}


def chapter_rows(index: dict, archive: dict, cfgo) -> tuple[list[dict], list[str]]:
    rows, review = [], []
    order = 0
    for c in index["chapters"]:
        no, filecell, replaces, built, state = (c + [""] * 5)[:5]
        order += 1
        fm = re.search(r"`([^`]+\.md)`", filecell)
        notes = re.search(r"\((v\d+:.*)\)\s*$", filecell)
        st = unbold(state).split(" ")[0].strip("*").lower()
        st = "deferred" if "deferred" in state.lower() else ("draft + held" if "held" in state.lower() else st)
        if no in ("—", "-", ""):
            no = "science"
        elif re.fullmatch(r"\d", no):
            no = no.zfill(2)
        elif re.fullmatch(r"\d{2}", no):
            pass
        if fm:
            f = fm.group(1)
            fv = nr.file_version(f)
            text = (NARR / f).read_text(encoding="utf-8") if (NARR / f).is_file() else ""
            title = re.sub(r"^[\d.]+\s*", "", (re.search(r"^# (.+)$", text, re.M) or [None, ""])[1]).strip()
            if not (NARR / f).is_file():
                review.append(f"index row {no}: file {f} is not on disk")
            rows.append({"chapter_no": no, "title": title or f, "reading_order": order, "file_stem": fv[0],
                         "current_version": fv[1], "current_file": f, "state": st or "draft",
                         "replaces_original": unbold(replaces) or None, "built_from": unbold(built) or None,
                         "inactive": 0, "version_notes": notes.group(1) if notes else None})
        else:
            title = unbold(re.sub(r"\(.*\)$", "", filecell)).strip().strip("*") or no
            rows.append({"chapter_no": no, "title": title, "reading_order": order,
                         "file_stem": "part-10" if no == "10" else no, "current_version": None,
                         "current_file": None, "state": st or "draft", "replaces_original": unbold(replaces) or None,
                         "built_from": unbold(built) or None, "inactive": 0, "version_notes": None})
            review.append(f"index row {no!r} ({title}) has no chapter file; imported as a chapter row "
                          f"with no file (state {st or 'draft'})")
    return rows, review


def r3_versions(chapters: list[dict], archive: dict) -> list[dict]:
    """One entry per (chapter, version) note in the index File column, with the file's date."""
    out = []
    for ch in chapters:
        if not ch["version_notes"]:
            continue
        slug = re.sub(r"^\d{2}(?:-\d{2})?-", "", ch["file_stem"])
        dates = {v: file_date(p.name) for v, p in archive.get(slug, [])}
        for part in re.split(r";\s(?=v\d+:)", ch["version_notes"]):
            m = re.match(r"v(\d+):\s*(.*)$", part.strip())
            if m:
                v = int(m.group(1))
                out.append({"chapter_no": ch["chapter_no"], "version": v, "date": dates.get(v),
                            "note": m.group(2).strip(), "refs": refs_of(m.group(2))})
    return out


_STOP = {"the", "and", "for", "with", "from", "into", "this", "that", "new", "strand", "updates", "read",
         "role", "group", "item", "verses", "verse", "section", "sections", "chapter"}


def _words(s: str) -> set[str]:
    words = {w for w in re.findall(r"[a-z0-9×]+", (s or "").lower().replace("*", ""))
             if len(w) > 2 and w not in _STOP}
    return words | {f"group-{g}" for g in re.findall(r"group ([A-G])\b", s or "")}


# ── sections and citations of the current files ─────────────────────────────────────────────────
def current_sections(chapters: list[dict], archive: dict) -> list[dict]:
    out = []
    for ch in chapters:
        if not ch["current_file"]:
            continue
        slug = re.sub(r"^\d{2}(?:-\d{2})?-", "", ch["file_stem"])
        first: dict[str, int] = {}
        for v, p in archive.get(slug, []):
            _, secs, _ = nr.parse_chapter(p.read_text(encoding="utf-8"))
            for s in secs:
                first.setdefault(s.heading, v)
        _, secs, _ = nr.parse_chapter((NARR / ch["current_file"]).read_text(encoding="utf-8"))
        for s in secs:
            out.append({"chapter_no": ch["chapter_no"], "heading": s.heading, "level": s.level,
                        "ordinal": s.ordinal, "parent_ordinal": secs[s.parent].ordinal if s.parent is not None else None,
                        "first_version": first.get(s.heading, ch["current_version"])})
    return out


def current_citations(chapters: list[dict], vx, conn) -> list[dict]:
    out = []
    for ch in chapters:
        if not ch["current_file"]:
            continue
        _, secs, ps = nr.parse_chapter((NARR / ch["current_file"]).read_text(encoding="utf-8"))
        seen = set()
        for p in ps:
            for r in nr.parse_refs(p.text, vx):
                key = (secs[p.section].heading, r.normalised)
                if key in seen:
                    continue
                seen.add(key)
                vt = conn.execute("SELECT text FROM verse WHERE id=?", (r.verse_id,)).fetchone() if r.verse_id else None
                out.append({"chapter_no": ch["chapter_no"], "heading": secs[p.section].heading,
                            "section_ordinal": secs[p.section].ordinal,
                            "verse_id": r.verse_id, "ref_as_written": r.as_written, "ref_normalised": r.normalised,
                            "kind": r.kind, "quoted": int(nr.quoted(p.text, vt[0] if vt else None)),
                            "first_version": ch["current_version"]})
    return out


# ── R5, R6 ─────────────────────────────────────────────────────────────────────────────────────
def r5_audit() -> dict:
    text = AUDIT.read_text(encoding="utf-8")
    rows = []
    in_edits = False
    for l in text.splitlines():
        if l.startswith("| # | File | Kind | Before | After"):
            in_edits = True
            continue
        if in_edits and l.startswith("|") and not is_sep(l):
            c = cells(l)
            if len(c) >= 5 and c[0].isdigit():
                rows.append({"kind": "narrative change", "where": c[1], "audit_kind": c[2],
                             "before": c[3], "after": c[4], "header": ["#", "File", "Kind", "Before", "After"],
                             "cells": c})
    return {"key": "R5:imputed-readings-audit", "source": "R5", "update_date": "2026-10-01",
            "title": "Narrative audit — imputed readings removed (#1921)", "strand": None,
            "refs": [{"kind": "escalation", "value": "1921"}],
            "researcher_instruction": "you are bordering on imputing meaning that is not supported by the verses. "
                                      "don't drive synergy and phantom observations into the findings. Rather "
                                      "allow scripture to speak for itself.",
            "method": "Workflow/Instructions/wa-inner-being-narrative-style-guide-v1-20261001.md §1, §2, §8.2",
            "source_files": [str(AUDIT.relative_to(ROOT)).replace("\\", "/")], "scripts": [],
            "claims_changed_note": None, "not_woven_note": None, "structure_change": None,
            "structure_reason": None, "quote_parts": None, "quote_failures": None, "quote_note": None,
            "notes": text.split("## Every edit")[0].strip(), "legacy_register_version": None,
            "provenance": AUDIT.name, "table_lines": len(rows), "header_shapes": ["# · File · Kind · Before · After"],
            "change_lines": rows}


def r6_digest() -> dict:
    text = DIGEST.read_text(encoding="utf-8")
    m = re.search(r"^## 4\..*?(?=^## 5\.)", text, re.M | re.S)
    body = m.group(0).strip() if m else ""
    items = re.findall(r"^\d+\.\s+(.+)$", body, re.M)
    return {"key": "R6:digest-4", "source": "R6", "update_date": "2026-09-30",
            "title": "Reset: what the latest findings add that the original never had (digest §4)",
            "strand": "inner seat (M47)", "refs": [], "researcher_instruction": None, "method": None,
            "source_files": [str(DIGEST.relative_to(ROOT)).replace("\\", "/")], "scripts": [],
            "claims_changed_note": None, "not_woven_note": None,
            "structure_change": "the narrative regenerated as chapter files (2026-09-30 reset)",
            "structure_reason": None, "quote_parts": None, "quote_failures": None, "quote_note": None,
            "notes": body, "legacy_register_version": None, "provenance": f"{DIGEST.name} §4",
            "table_lines": 0, "header_shapes": [],
            "change_lines": [{"kind": "narrative change", "where": "(reset)", "area": i, "header": [], "cells": [i]}
                             for i in items]}


# ── preview ────────────────────────────────────────────────────────────────────────────────────
def build_preview() -> tuple[dict, list[str]]:
    cfgo = Cfg()
    conn = cfgo.conn
    vx = nr.VerseIndex(cfgo)
    review: list[str] = []
    versions = register_versions()
    hist, last, sections_by_version, rv = r1_history(versions)
    review += rv
    v51_path = versions[-1][1]
    v51 = v51_path.read_text(encoding="utf-8")
    # claims
    claims = []
    for cid, c in last.items():
        vm, vp, vs = parse_verdict(c["verdict_cell"])
        status = {"Withdrawn": "withdrawn", "Held": "held"}.get(vm, "current")
        if vp == "Held" and vm != "Held":
            review.append(f"{cid}: split verdict {vs!r} -- imported as verdict {vm}, part_verdict {vp}, "
                          f"status {status}")
        newchs = [x.strip() for x in re.split(r"[,;]", unbold(c["newch"])) if x.strip() and x.strip() not in ("—", "-")]
        srcs = []
        for txt, note in ((c["original"], "cited by the original essay"), (c["evidence"], "evidence (claim register)")):
            for r in nr.parse_refs(unbold(txt), vx, follow_ons=True):
                srcs.append({"source_kind": "verse", "verse_id": r.verse_id, "ref_as_written": r.as_written,
                             "ref_normalised": r.normalised, "note": note})
        ptr = re.findall(r"\((?:[^()]*?)((?:dep|[A-H]|SC|U\d|F|B)\s*§[\d.]+[^()]*)\)", c["evidence"])
        if ptr:
            srcs.append({"source_kind": "study file", "source_text": "; ".join(ptr),
                         "note": "M47 reading pointers (register header: dep = depiction v1; A-H = batch files; "
                                 "SC = spirit classification)"})
        claims.append({"claim_ref": cid, "origin": "original essay", "original_chapter": c["chapter"],
                       "original_wording": unbold(c["original"]), "claim_text": claim_text(c),
                       "verdict": vm, "part_verdict": vp, "part_scope": vs, "status": status, "i_read": 0,
                       "main_chapter_no": newchs[0] if newchs else None, "new_ch": unbold(c["newch"]),
                       "evidence": unbold(c["evidence"]), "sources": srcs, "history": hist[cid]})
    # updates
    secs = dated_sections(v51)
    first_v = {}
    for s in secs:
        first_v[s["heading"]] = next((v for v, hs in sorted(sections_by_version.items()) if s["heading"] in hs), None)
        if first_v[s["heading"]] is None:
            review.append(f"section {s['heading']!r}: its heading is not found verbatim in any version before "
                          f"v51 (renamed later?) -- legacy_register_version left empty")
    updates = [parse_update(s, first_v[s["heading"]]) for s in secs]
    # index
    index = parse_index(INDEX.read_text(encoding="utf-8"))
    archive = chapter_archive()
    chapters, rv = chapter_rows(index, archive, cfgo)
    review += rv
    chapters.append({"chapter_no": "13", "title": "Under God's anger", "reading_order": 0,
                     "file_stem": "13-under-gods-anger", "current_version": 10, "current_file": None,
                     "state": "draft", "replaces_original": None, "built_from": None, "inactive": 1,
                     "version_notes": None})
    review.append("old Ch 13 *Under God's anger* (folded into 10.13, #1977; the number reused for *Other "
                  "beings*, #1982) is added as a retired chapter row (inactive 1), so history can point to it")
    versions_r3 = r3_versions(chapters, archive)
    by_date_refs = collections.defaultdict(list)
    for u in updates:
        by_date_refs[u["update_date"]].append(u)
    r3_new: dict[tuple, dict] = {}
    r3_links = []
    for vn in versions_r3:
        refs = {(r["kind"], r["value"]) for r in vn["refs"]}
        match = [u for u in by_date_refs.get(vn["date"], []) if refs & {(r["kind"], r["value"]) for r in u["refs"]}]
        if len(match) > 1:            # several sections share date and refs: the words of the note decide
            want = _words(vn["note"])
            scored = sorted(((len(want & _words(u["title"])), u["key"]) for u in match), reverse=True)
            if scored[0][0] > 0 and (len(scored) == 1 or scored[0][0] > scored[1][0]):
                match = [u for u in match if u["key"] == scored[0][1]]
        if len(match) == 1:
            r3_links.append({**vn, "update_key": match[0]["key"]})
            continue
        key = (vn["date"], tuple(sorted(refs)), vn["note"] if not refs else "")
        u = r3_new.get(key)
        if u is None:
            u = {"key": f"R3:{vn['date']}:{len(r3_new)}", "source": "R3", "update_date": vn["date"] or "",
                 "title": vn["note"][:120], "strand": None, "refs": vn["refs"], "researcher_instruction": None,
                 "method": None, "source_files": [], "scripts": [], "claims_changed_note": None,
                 "not_woven_note": None, "structure_change": None, "structure_reason": None,
                 "quote_parts": None, "quote_failures": None, "quote_note": None, "notes": None,
                 "legacy_register_version": None, "provenance": f"{INDEX.name}, File column version notes",
                 "table_lines": 0, "header_shapes": [], "change_lines": [], "chapter_versions": []}
            r3_new[key] = u
            if len(match) > 1:
                review.append(f"Ch {vn['chapter_no']} v{vn['version']} ({vn['date']}): {len(match)} register "
                              f"sections share its date and refs -- kept as its own update")
        u["chapter_versions"].append({"chapter_no": vn["chapter_no"], "version": vn["version"], "note": vn["note"]})
        r3_links.append({**vn, "update_key": u["key"]})
    for vn in versions_r3:
        if not vn["date"]:
            review.append(f"Ch {vn['chapter_no']} v{vn['version']}: no file of that version on disk, so no date")
    structure = []
    for row in index["structure"]:
        date, strand, change, reason = (row + [""] * 4)[:4]
        structure.append({"key": f"R3S:{date}:{len(structure)}", "source": "R3 structure log",
                          "update_date": date, "title": f"Structure: {unbold(change)[:100]}", "strand": strand,
                          "refs": refs_of(strand + " " + change), "researcher_instruction": None, "method": None,
                          "source_files": [], "scripts": [], "claims_changed_note": None, "not_woven_note": None,
                          "structure_change": unbold(change), "structure_reason": unbold(reason),
                          "quote_parts": None, "quote_failures": None, "quote_note": None, "notes": None,
                          "legacy_register_version": None, "provenance": f"{INDEX.name}, Structure log",
                          "table_lines": 1, "header_shapes": ["Date · Strand · Change · Reason"], "change_lines": []})
    r5 = r5_audit()
    r6 = r6_digest()
    sections = current_sections([c for c in chapters if not c["inactive"]], archive)
    cites = current_citations([c for c in chapters if not c["inactive"]], vx, conn)
    all_updates = updates + list(r3_new.values()) + structure
    known_esc = {r[0] for r in conn.execute("SELECT id FROM escalation")}
    known_alias = {r[0] for r in conn.execute("SELECT alias FROM escalation WHERE alias IS NOT NULL")}
    refs_missing = sorted({(r["kind"], r["value"], u["title"][:80]) for u in all_updates for r in u["refs"]
                           if not ((r["kind"] == "escalation" and int(r["value"]) in known_esc) or
                                   (r["kind"] != "escalation" and r["value"].split(".")[0] in known_alias))})
    cfgo.close()
    # correction section's 34 removals: prose bullets only -- R4 reconstructs before/after
    corr = next((u for u in updates if u["title"].startswith("Correction")), None)
    if corr:
        n = len(re.findall(r"^- \*\*", corr["notes"] or "", re.M))
        review.append(f"Correction section: its 34 removals are listed as prose (by chapter, {n} bullets), with no "
                      f"before/after; R4 (the archive comparison, with each chapter's R0 batch) supplies them")
    preview = {
        "meta": {"escalation": 2110, "built": nr._now(), "register_versions": [v for v, _ in versions],
                 "register_current": v51_path.name,
                 "refs_missing": [{"kind": k, "value": v, "update": t} for k, v, t in refs_missing]},
        "chapters": chapters, "sections": sections, "index_notes": index["notes"],
        "claims": claims, "updates": updates + list(r3_new.values()) + structure + [r5, r6],
        "chapter_version_links": r3_links, "citations": cites,
    }
    return preview, review


def counts(p: dict) -> dict:
    up = p["updates"]
    lines = [cl for u in up for cl in u["change_lines"]]
    r2 = [u for u in up if u["source"] == "R2"]
    return {
        "chapters": len(p["chapters"]), "chapters_active": sum(1 for c in p["chapters"] if not c["inactive"]),
        "sections": len(p["sections"]), "index_notes": len(p["index_notes"]), "claims": len(p["claims"]),
        "claim_history_rows": sum(len(c["history"]) for c in p["claims"]),
        "claim_sources": sum(len(c["sources"]) for c in p["claims"]),
        "updates": len(up), "updates_R2": len(r2), "R2_table_lines": sum(u["table_lines"] for u in r2),
        "R2_data_rows": sum(len(u["change_lines"]) for u in r2),
        "R2_header_shapes": len({h for u in r2 for h in u["header_shapes"]}),
        "change_lines_original_claim": sum(1 for l in lines if l["kind"] == "original claim"),
        "change_lines_narrative": sum(1 for l in lines if l["kind"] == "narrative change"),
        "citations": len(p["citations"]),
        "citations_no_verse_row": sum(1 for c in p["citations"] if c["verse_id"] is None),
        "by_verdict": dict(collections.Counter(c["verdict"] for c in p["claims"])),
        "by_status": dict(collections.Counter(c["status"] for c in p["claims"])),
    }


def write_preview(out_dir: pathlib.Path) -> None:
    preview, review = build_preview()
    c = counts(preview)
    preview["meta"]["counts"] = c
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"wa-essay-narrative-register-import-preview-{STAMP}"
    jpath = out_dir / f"{stem}.json"
    jpath.write_text(json.dumps(preview, ensure_ascii=False, indent=1), encoding="utf-8")
    md = [f"# Narrative claim register: import preview ({STAMP})", "",
          f"**Escalation:** #2110 · **Built:** {preview['meta']['built']} by "
          f"`iba/app/migration/narrative_claim_register_import_v1_20261013.py --preview` · "
          f"**Data:** `{jpath.name}` (the file that is imported, unchanged, after approval)", "",
          "Nothing is written to iba.db until you approve this preview (spec §6, *Review and import*).", "",
          "## Counts", "", "| | |", "|---|---|"] + [f"| {k} | {v} |" for k, v in c.items()]
    md += ["", "## Chapters", "", "| # | Title | File | State | Inactive |", "|---|---|---|---|---|"]
    for ch in preview["chapters"]:
        md.append(f"| {ch['chapter_no']} | {ch['title']} | {ch['current_file'] or '—'} | {ch['state']} | {ch['inactive']} |")
    md += ["", "## Original claims, with their recorded history", ""]
    cur_ch = None
    for cl in preview["claims"]:
        if cl["original_chapter"] != cur_ch:
            cur_ch = cl["original_chapter"]
            md += [f"### {cur_ch}", ""]
        md.append(f"**{cl['claim_ref']}** · {cl['verdict']}{' / ' + cl['part_verdict'] if cl['part_verdict'] else ''}"
                  f" · status {cl['status']} · main chapter {cl['main_chapter_no'] or '—'} · "
                  f"{len(cl['sources'])} source row(s)")
        md.append(f"- original: {cl['original_wording']}")
        md.append(f"- claim (as imported): {cl['claim_text']}")
        for h in cl["history"]:
            bits = [h["change_kind"], h["change_date"], f"v{h.get('register_version')}"]
            md.append(f"  - {' · '.join(str(b) for b in bits)}"
                      + (f": verdict {h.get('verdict_before')} → {h.get('verdict_after')}" if h["change_kind"] == "verdict changed" else "")
                      + (f": {h['note']}" if h["change_kind"] in ("renumbered", "edited") else ""))
        md.append("")
    md += ["## Updates", "", "| Source | Date | Title | Refs | Table lines | Original-claim lines | Narrative-change lines |",
           "|---|---|---|---|---|---|---|"]
    for u in preview["updates"]:
        oc = sum(1 for l in u["change_lines"] if l["kind"] == "original claim")
        md.append(f"| {u['source']} | {u['update_date']} | {nr._cell(u['title'])} | "
                  f"{', '.join(r['value'] for r in u['refs']) or '—'} | {u['table_lines']} | {oc} | "
                  f"{len(u['change_lines']) - oc} |")
    (out_dir / f"{stem}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    rl = [f"# Narrative claim register: import review list ({STAMP})", "",
          f"Goes with `{stem}.md` / `.json`. Escalation #2110, spec §6 *Review and import*: the correlation "
          "lists, changes found only by comparison, chapter numbers mapped across the 2026-10-02 renumbering, "
          "references that could not be resolved, and the Tally recount. **Each item is for your review; the "
          "import takes the preview as it stands unless you direct otherwise.**", "",
          "## 1. How the import maps the register", "",
          "- **Claim wording.** An original claim's `claim_text` is its *Evidence and restatement* cell when the "
          "verdict is Restated (the correction is what the narrative now says), and its original wording for every "
          "other verdict. The original wording is kept in `original_wording`; the full cells of each version stay in "
          "the 'claim created' and change rows. The R0 reading may restate a claim in its own plain wording; that "
          "is then a logged change.",
          "- **Status.** Withdrawn → `withdrawn`; Held → `held`; every other verdict → `current`. A split verdict "
          "(Restated / Held) is `current`, with the second verdict in `part_verdict`.",
          "- **in_narrative** is 0 for every claim at import: no passage is linked until the R0 batches read the "
          "chapters. `Check` will list current claims with no telling until then.",
          "- **Main chapter** is the first chapter named in *New ch* (already in the 2026-10-02 numbering in v51).",
          "- **Sources:** every verse reference in the original claim and in the evidence cell (one row per verse), "
          "and the M47 reading pointers (dep, A–H, SC) as one *study file* row.",
          "- **Register lines that do not name an original claim** (the narrative's own statements a strand "
          "changed, and the 88 audit edits) cannot be attached to a claim yet: the claims they concern are found in "
          "R0. They are imported with their update and kept in the preview JSON for the correlation; nothing is "
          "dropped.", "",
          f"## 2. Tally recount", "",
          f"The register's Tally gives 15 + 8 + 37 + 15 + 11 = 86, counting part-held claims twice. The import "
          f"finds **{c['claims']} claim rows**: " + ", ".join(f"{k} {v}" for k, v in c["by_verdict"].items())
          + f". By status: " + ", ".join(f"{k} {v}" for k, v in c["by_status"].items()) + ".", "",
          f"## 3. R2 accounted for", "",
          f"{c['updates_R2']} dated sections; {c['R2_table_lines']} table lines ({c['R2_data_rows']} data rows, the "
          f"rest headers and separators); {c['R2_header_shapes']} header shapes. Every data row is in the preview: "
          f"{c['change_lines_original_claim']} name an original claim (attached), the rest are narrative changes "
          f"held for R0.", "",
          f"The {c['change_lines_original_claim']} lines that name an original claim (the *# · Before (verdict) · "
          f"Evidence now read · Now* tables) are carried by R1: the register version that added the section is "
          f"the version in which the claim's cells changed, so the change row holds the cells before and after, "
          f"and the section's full text (tables included) is kept verbatim in the update's notes.", "",
          "**Spec §1 facts, re-measured.** The specification gave 551 table lines in 16 header shapes for the "
          f"dated sections; the sections hold {c['R2_table_lines']} table lines in {c['R2_header_shapes']} shapes "
          "(the 7 lines of the Tally are not in a dated section). It gave 33 chapter files and 323 headings: both "
          "counts included the index (00-index), so there are 32 chapter files with 315 headings, and 347 section "
          "rows with each chapter's opening.", "",
          "## 4. Items found while building the preview", ""]
    rl += [f"- {x}" for x in review]
    rl += ["", "## 5. References with no verse row (citations)", "",
           "Kept with `verse_id` NULL, never dropped. Whole-chapter references (e.g. *Psalm 23*) are among them.", ""]
    nov = collections.Counter((x["ref_normalised"], x["kind"]) for x in preview["citations"] if x["verse_id"] is None)
    rl += [f"- {r} ({k}) ×{n}" for (r, k), n in sorted(nov.items())]
    rl += ["", "## 6. Index version notes linked to updates (R3)", "",
           "| Ch | v | Date | Note | Update |", "|---|---|---|---|---|"]
    for l in preview["chapter_version_links"]:
        rl.append(f"| {l['chapter_no']} | {l['version']} | {l['date'] or '—'} | {nr._cell(l['note'][:140])} | {l['update_key'][:60]} |")
    lines = [(u, l) for u in preview["updates"] for l in u["change_lines"] if l["kind"] == "narrative change"]
    multi = [(u, l) for u, l in lines if len(l.get("chapters_as_written", [])) > 1]
    rl += ["", "## 7. Multi-chapter cells, split one row per chapter (test 6.5)", "",
           f"{len(multi)} register lines name more than one chapter. In the correlation each counts once per "
           f"chapter (today's numbering).", "", "| Update | Where | Chapters (today) |", "|---|---|---|"]
    rl += [f"| {nr._cell(u['title'][:70])} | {nr._cell(l['where'][:80])} | {', '.join(l['chapters_now'])} |"
           for u, l in multi]
    mapped = [(u, l) for u, l in lines if l.get("chapters_as_written") and
              [x.zfill(2) if re.fullmatch(r"\d", x) else x for x in l["chapters_as_written"]] != l["chapters_now"]]
    rl += ["", "## 8. Chapter numbers mapped across the renumberings (test 6.6)", "",
           f"{len(mapped)} register lines were written in older numbering (#1920 on 2026-10-01: 10.3–10.9 → "
           f"10.4–10.10, 13 → 14, 14 → 15; #1936 on 2026-10-02: 9 → 2, 2–8 → 3–9; Ch 13 between #1920 and "
           f"#1982 is the retired *Under God's anger*).", "", "| Date | Update | As written | Today |", "|---|---|---|---|"]
    rl += [f"| {u['update_date']} | {nr._cell(u['title'][:60])} | {', '.join(l['chapters_as_written'])} | "
           f"{', '.join(l['chapters_now'])} |" for u, l in mapped]
    rl += ["", "## 9. Escalations and threads named but not found (test 6.10)", ""]
    rl += [f"- {m['kind']} {m['value']} (in: {m['update']})" for m in preview["meta"]["refs_missing"]] or \
          ["None: every escalation and thread named in the updates exists in the escalation table."]
    (out_dir / f"wa-essay-narrative-register-import-review-list-{STAMP}.md").write_text("\n".join(rl) + "\n", encoding="utf-8")
    print(json.dumps(c, ensure_ascii=False, indent=1))
    print(f"wrote {jpath}")


# ── apply (build step 7, after approval) ───────────────────────────────────────────────────────
def apply(preview_file: pathlib.Path, db_path: pathlib.Path) -> None:
    data = json.loads(preview_file.read_text(encoding="utf-8"))
    cfgo = Cfg(db_path)
    conn = cfgo.conn
    conn.isolation_level = None
    if conn.execute("SELECT COUNT(*) FROM narrative_claim").fetchone()[0]:
        cfgo.close()
        raise SystemExit("refused: narrative_claim already has rows -- the import runs once")
    w = nr.Writer(conn, "migration", "migration")
    conn.execute("BEGIN")
    try:
        ch_id = {}
        for c in data["chapters"]:
            ch_id[(c["chapter_no"], c["inactive"])] = w.insert("narrative_chapter", {
                k: c[k] for k in ("chapter_no", "title", "reading_order", "file_stem", "current_version",
                                  "current_file", "state", "replaces_original", "built_from", "inactive")})
        sec_id = {}
        for s in data["sections"]:
            cid = ch_id[(s["chapter_no"], 0)]
            parent = sec_id.get((s["chapter_no"], s["parent_ordinal"])) if s["parent_ordinal"] is not None else None
            sec_id[(s["chapter_no"], s["ordinal"])] = w.insert("narrative_section", {
                "chapter_id": cid, "heading": s["heading"], "level": s["level"], "parent_section_id": parent,
                "ordinal": s["ordinal"], "first_version": s["first_version"]})
        for i, n in enumerate(data["index_notes"], 1):
            w.insert("narrative_index_note", {"heading": n["heading"], "text": n["text"] or "(empty)", "ordinal": i})
        upd_id = {}
        for u in data["updates"]:
            row = {k: u[k] for k in ("title", "strand", "researcher_instruction", "method",
                                     "claims_changed_note", "not_woven_note", "structure_change",
                                     "structure_reason", "quote_parts", "quote_failures", "quote_note", "notes",
                                     "legacy_register_version")}
            row["update_date"] = u["update_date"] or "unknown"
            row["source_files"] = NL.join(u["source_files"]) or None
            row["scripts"] = NL.join(u["scripts"]) or None
            links = [l for l in data["chapter_version_links"] if l["update_key"] == u["key"]]
            if links:      # the index's per-version notes, marked as added from the index (R3)
                row["notes"] = ((row["notes"] or "") + NL + NL + "[Chapter versions, from the narrative index] " +
                                "; ".join(f"{l['chapter_no']} v{l['version']}: {l['note']}" for l in links)).strip()
            if u["update_date"]:
                row["created_at"] = f"{u['update_date']}T00:00:00Z"
            row["created_by"] = "migration"
            upd_id[u["key"]] = w.insert("narrative_update", row)
            for r in u["refs"]:
                w.insert("narrative_update_ref", {"update_id": upd_id[u["key"]], "kind": r["kind"],
                                                  "value": r["value"]})
        ver_upd = {}
        for u in data["updates"]:
            if u["legacy_register_version"]:
                ver_upd.setdefault(u["legacy_register_version"], []).append(upd_id[u["key"]])
        for c in data["claims"]:
            hist = c["history"]
            created = hist[0]
            since = nr._max_change_id(conn)
            cid = w.insert("narrative_claim", {
                "claim_ref": c["claim_ref"], "origin": c["origin"], "claim_text": created.get("claim_after") or c["claim_text"],
                "i_read": c["i_read"], "verdict": created.get("verdict_after"), "original_chapter": c["original_chapter"],
                "original_wording": c["original_wording"],
                "main_chapter_id": ch_id.get(((c["main_chapter_no"] or "").zfill(2) if c["main_chapter_no"] and "." not in c["main_chapter_no"] else c["main_chapter_no"], 0)),
                "status": "current", "created_at": f"{created['change_date']}T00:00:00Z"})
            conn.execute("UPDATE narrative_claim_change SET basis='recorded', provenance=?, note=?, created_by='migration' "
                         "WHERE id > ? AND claim_id=?", (created["provenance"], created["note"], since, cid))
            for s in c["sources"]:
                w.insert("narrative_claim_source", {"claim_id": cid, **{k: s.get(k) for k in (
                    "source_kind", "verse_id", "ref_as_written", "ref_normalised", "source_text", "note")}})
            for h in hist[1:]:
                since = nr._max_change_id(conn)
                if h["change_kind"] == "verdict changed":
                    conn.execute("UPDATE narrative_claim SET verdict=? WHERE id=?", (h["verdict_after"], cid))
                elif h["change_kind"] == "claim restated":
                    conn.execute("UPDATE narrative_claim SET claim_text=? WHERE id=?", (h["claim_after"], cid))
                else:
                    w._grant("narrative_claim_change")
                    conn.execute("INSERT INTO narrative_claim_change (claim_id, change_date, change_kind, note, basis, "
                                 "provenance, created_by) VALUES (?,?,?,?,?,?,'migration')",
                                 (cid, h["change_date"], h["change_kind"], h["note"], "recorded", h["provenance"]))
                ups = ver_upd.get(h.get("register_version"), [])
                conn.execute("UPDATE narrative_claim_change SET change_date=?, change_kind=?, basis='recorded', "
                             "provenance=?, note=COALESCE(?, note), update_id=?, created_by='migration' WHERE id > ? "
                             "AND claim_id=?", (h["change_date"], h["change_kind"], h["provenance"],
                                                (h.get("note") or "") + (f" | version note: {h['version_note']}" if h.get("version_note") else ""),
                                                ups[0] if len(ups) == 1 else None, since, cid))
            final_status = c["status"]
            if final_status != "current":
                since = nr._max_change_id(conn)
                conn.execute("UPDATE narrative_claim SET status=? WHERE id=?", (final_status, cid))
                conn.execute("UPDATE narrative_claim_change SET basis='recorded', provenance=?, created_by='migration', "
                             "change_date=? WHERE id > ? AND claim_id=?",
                             (f"status from verdict {c['verdict']} (claim register {data['meta']['register_current']})",
                              next((h["change_date"] for h in reversed(hist) if h.get("verdict_after") == c["verdict"]),
                                   created["change_date"]), since, cid))
            conn.execute("UPDATE narrative_claim SET part_verdict=?, part_scope=? WHERE id=?",
                         (c["part_verdict"], c["part_scope"], cid))
        for x in data["citations"]:
            w.insert("narrative_citation", {
                "chapter_id": ch_id[(x["chapter_no"], 0)], "section_id": sec_id.get((x["chapter_no"], x["section_ordinal"])),
                "verse_id": x["verse_id"], "ref_as_written": x["ref_as_written"], "ref_normalised": x["ref_normalised"],
                "quoted": x["quoted"], "first_version": x["first_version"]})
        n = conn.execute("SELECT COUNT(*) FROM narrative_claim").fetchone()[0]
        if n != len(data["claims"]):
            raise RuntimeError(f"claim count {n} != preview {len(data['claims'])}")
        conn.execute("COMMIT")
        print(f"imported: {n} claims, {len(data['updates'])} updates, {len(data['chapters'])} chapters, "
              f"{len(data['sections'])} sections, {len(data['citations'])} citations")
    except Exception:
        conn.execute("ROLLBACK")
        raise
    finally:
        cfgo.close()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--preview", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--preview-file")
    ap.add_argument("--db", default=str(ROOT / "iba/app/db/iba.db"))
    ap.add_argument("--out-dir", default=str(ESSAY))
    a = ap.parse_args()
    if a.apply:
        if not a.preview_file:
            raise SystemExit("--apply needs --preview-file (the approved preview JSON)")
        apply(pathlib.Path(a.preview_file), pathlib.Path(a.db))
    else:
        write_preview(pathlib.Path(a.out_dir))
    return 0


if __name__ == "__main__":
    sys.exit(main())
