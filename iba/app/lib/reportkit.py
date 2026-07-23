"""reportkit.py — shared report scaffold (title/ToC/sections/footer) + archive-on-write, reading
`cfg_report`/`cfg_report_section`/`cfg_report_csv_table`. Every report generator calls
`render_scaffold()` instead of hand-building `"## N. Title"` lines, and `write_report()` instead of
`path.write_text()` directly, so titles/headings/ToC/footer live in config (PLAN-reports-config-
governance-v1-20260722.md) and a previous version is archived, never silently overwritten.

Read-only against `cfg_*` (no writes here — that's `configmaint.propose`'s job, per the write-grant
table). `render_scaffold`'s caller stays responsible for its own section CONTENT (the SQL, the
numbers) and, where a report already has its own inclusion toggle (`report.show_*`/
`validation.show_*`), for deciding which sections to pass in at all — `cfg_report_section.include`
is the fallback gate for reports that have no toggle of their own, not a second gate on top.
"""

from __future__ import annotations

import datetime
import pathlib
import re
import sqlite3


def render_scaffold(conn: sqlite3.Connection, step: str, sections: dict[str, list[str]],
                    intro: list[str] | None = None, **title_vars) -> list[str]:
    """sections: {section_key: [body lines, no heading]} — only the keys the caller wants shown.
    intro: lines placed after the title, before the table of contents (e.g. a blockquote + a
    summary table) — the same "> Generated ..." preamble every report already has.
    title_vars: substituted into cfg_report.title via str.format (e.g. word=word, book=book)."""
    rep = conn.execute("SELECT title, show_toc, footer_text FROM cfg_report WHERE step=?",
                       (step,)).fetchone()
    if rep is None:
        raise ValueError(f"reportkit.render_scaffold: no cfg_report row for step {step!r} — "
                         f"seed it in a migration before wiring the generator to call this")
    title = rep["title"].format(**title_vars) if title_vars else rep["title"]

    secs = conn.execute(
        "SELECT ordinal, section_key, heading, toc_label, include FROM cfg_report_section "
        "WHERE step=? ORDER BY ordinal", (step,)).fetchall()
    known_keys = {s["section_key"] for s in secs}
    present = [s for s in secs if s["section_key"] in sections and s["include"]]
    extra_keys = [k for k in sections if k not in known_keys]  # safety net, not expected in use

    L = [f"# {title}", ""]
    if intro:
        L += intro
        L.append("")

    if rep["show_toc"] and (present or extra_keys):
        L.append("## Contents")
        L.append("")
        for s in present:
            label = s["toc_label"] or s["heading"].lstrip("#").strip()
            L.append(f"- [{label}](#{_anchor(s['heading'])})")
        for k in extra_keys:
            L.append(f"- {k}")
        L.append("")

    for s in present:
        L.append(s["heading"])
        L.append("")
        L += sections[s["section_key"]]
        if L and L[-1] != "":
            L.append("")
    for k in extra_keys:
        L += sections[k]
        if L and L[-1] != "":
            L.append("")

    if rep["footer_text"]:
        L.append("")
        L.append(rep["footer_text"])

    return L


def _anchor(heading: str) -> str:
    """GitHub-style heading slug — good enough for this app's own ToC links."""
    text = heading.lstrip("#").strip().lower()
    out = ["-" if ch in (" ", "-", "_") else ch for ch in text if ch.isalnum() or ch in " -_"]
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


def write_report(conn: sqlite3.Connection, step: str, path: pathlib.Path,
                 lines: list[str]) -> pathlib.Path:
    """Archive the existing file (if any) to cfg_report.archive_dir before writing the new content
    — a regenerate never silently destroys the prior snapshot (researcher's 2026-07-22 instruction)."""
    rep = conn.execute("SELECT archive_dir FROM cfg_report WHERE step=?", (step,)).fetchone()
    archive_dir = (rep["archive_dir"] if rep else None) or "archive"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        adir = path.parent / archive_dir
        adir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        path.replace(adir / f"{path.stem}-{stamp}{path.suffix}")
    text = "\n".join(lines)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")
    return path


def write_csv_pairing(conn: sqlite3.Connection, step: str, out_dir: pathlib.Path,
                      row_filter: dict[str, list[sqlite3.Row]] | None = None) -> list[pathlib.Path]:
    """For every table registered in cfg_report_csv_table for `step`, write out_dir/{table}.csv —
    verbatim, every column. `row_filter`, when given, supplies pre-filtered rows for a table_name
    (word/book-scoped reports pass their own already-queried, already-filtered rows here instead of
    a full-table dump — see cfg_report_csv_table.join_note for what each report's slice is).
    A `cfg_*`-family wildcard row (table_name starting with 'cfg_') expands to every live cfg_* table."""
    tables = conn.execute(
        "SELECT table_name FROM cfg_report_csv_table WHERE step=? ORDER BY table_name",
        (step,)).fetchall()
    if not tables:
        return []
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[pathlib.Path] = []
    for row in tables:
        name = row["table_name"]
        if name.endswith("*"):
            prefix = name[:-1]
            for t in conn.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE ? "
                    "ORDER BY name", (prefix + "%",)):
                written.append(_dump_table(conn, t["name"], out_dir))
            continue
        if row_filter and name in row_filter:
            written.append(_dump_rows(row_filter[name], name, out_dir))
        else:
            written.append(_dump_table(conn, name, out_dir))
    return written


def _dump_table(conn: sqlite3.Connection, table: str, out_dir: pathlib.Path) -> pathlib.Path:
    cols = [d[0] for d in conn.execute(f'SELECT * FROM "{table}" LIMIT 0').description]
    rows = conn.execute(f'SELECT * FROM "{table}"').fetchall()
    return _write_csv(out_dir / f"{table}.csv", cols, [[r[c] for c in cols] for r in rows])


def _dump_rows(rows: list[sqlite3.Row], table: str, out_dir: pathlib.Path) -> pathlib.Path:
    cols = list(rows[0].keys()) if rows else []
    return _write_csv(out_dir / f"{table}.csv", cols, [[r[c] for c in cols] for r in rows])


def oneoff_path(cfg, topic: str, ext: str | None = None) -> pathlib.Path:
    """Phase 2 of PLAN-reports-config-governance-v1-20260722.md §5 — the path for a one-off
    ("investigatory") report: no `cfg_step`, so no `cfg_report` row to key off, but the
    folder/naming still comes from config (`governance.oneoff_*`), not a literal string a future
    migration/investigation script hardcodes. `cfg` is a lib.cfg.Cfg (or any object with
    .setting(key, default)).

    Same-day version bump on collision, per the Bible-study side's own established convention
    (docs/file-organisation-rules.md §2.3) rather than inventing a new one for this app — a second
    call for the same topic on the same day gets `-v2`, a third `-v3`, and so on."""
    out_dir = pathlib.Path(cfg.setting("governance.oneoff_report_dir", "iba/app/reports/"))
    pattern = cfg.setting("governance.oneoff_report_naming_pattern", "{topic}-{YYYYMMDD}.{format}")
    fmt = ext or cfg.setting("governance.oneoff_report_format", "md")
    slug = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")
    stamp = datetime.datetime.now().strftime("%Y%m%d")
    name = pattern.format(topic=slug, YYYYMMDD=stamp, format=fmt)

    path = out_dir / name
    if not path.exists():
        return path
    stem, _, extension = name.rpartition(".")
    n = 2
    while True:
        candidate = out_dir / f"{stem}-v{n}.{extension}"
        if not candidate.exists():
            return candidate
        n += 1


def _write_csv(path: pathlib.Path, cols: list[str], rows: list[list]) -> pathlib.Path:
    import csv
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(rows)
    return path
