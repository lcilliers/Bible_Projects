"""reportkit.py — shared report scaffold (title/ToC/sections/footer) + archive-on-write, reading
`cfg_report`/`cfg_report_section`/`cfg_report_csv_table`. Every report generator calls
`render_scaffold()` instead of hand-building headings, and `write_report()` instead of writing the
file directly, so titles/headings/ToC/footer live in config and a previous version is archived,
never overwritten.

Read-only against `cfg_*`. The caller owns its section CONTENT and, where a report has its own
inclusion toggle (`report.show_*`/`validation.show_*`), which sections to pass;
`cfg_report_section.include` is the gate for reports without a toggle of their own.
"""

from __future__ import annotations

import datetime
import json
import pathlib
import re
import sqlite3
import time


def _setting(conn: sqlite3.Connection, key: str, default=None):
    """Same read semantics as `lib/cfg.py:Cfg.setting` (inactive=0, JSON-decoded), kept here so this
    module depends only on the stdlib and a bare `sqlite3.Connection`."""
    r = conn.execute("SELECT value FROM cfg_setting WHERE key=? AND inactive=0", (key,)).fetchone()
    return json.loads(r["value"]) if r else default


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
            L.append(f"- [{label}](#{anchor(s['heading'])})")
        for k in extra_keys:
            L.append(f"- {k}")
        L.append("")

    # an explicit `<a id="...">` before each heading, so ToC links resolve the same in every Markdown
    # renderer (their own slug rules differ)
    for s in present:
        L.append(f'<a id="{anchor(s["heading"])}"></a>')
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


def anchor(heading: str) -> str:
    """GitHub-style heading slug, public so a generator building its own in-body sub-ToC uses the same
    rule."""
    text = heading.lstrip("#").strip().lower()
    out = ["-" if ch in (" ", "-", "_") else ch for ch in text if ch.isalnum() or ch in " -_"]
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


def archive_before_write(path: pathlib.Path, archive_dir: str = "archive") -> None:
    """If `path` already exists, move it to `path.parent/archive_dir/{stem}-{stamp}{suffix}` first
    (shared by `write_report`, `_write_csv`, `export_tables_csv.export`), so a regenerate never destroys
    the prior snapshot. The move retries briefly on a transient lock (#1320); a file held open for
    longer still raises PermissionError, recorded by run.py's crash handler."""
    if not path.exists():
        return
    adir = path.parent / archive_dir
    adir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    target = adir / f"{path.stem}-{stamp}{path.suffix}"
    attempts = 3
    for i in range(attempts):
        try:
            path.replace(target)
            return
        except PermissionError:
            if i == attempts - 1:
                raise
            time.sleep(0.3)


_VERSIONED_RE_TMPL = r"^{stem}-v(\d+)-\d{{8}}{suffix}$"


def _versioned_rx(stem: str, suffix: str) -> re.Pattern:
    return re.compile(_VERSIONED_RE_TMPL.format(stem=re.escape(stem), suffix=re.escape(suffix)))


def next_versioned_path(path: pathlib.Path, archive_dir: str = "archive") -> pathlib.Path:
    """`{stem}-v{n}-{date}{suffix}`: n = 1 + the highest version found for this stem in `path.parent`
    and `path.parent/archive_dir`, so numbering is monotonic over the report's lifetime. A plain-named
    file (no `-v<n>-`) is not counted."""
    stem, suffix = path.stem, path.suffix
    rx = _versioned_rx(stem, suffix)
    candidates = list(path.parent.glob(f"{stem}-v*{suffix}")) if path.parent.exists() else []
    adir = path.parent / archive_dir
    if adir.exists():
        candidates += list(adir.glob(f"{stem}-v*{suffix}"))
    versions = [int(m.group(1)) for m in (rx.match(f.name) for f in candidates) if m]
    n = max(versions, default=0) + 1
    stamp = datetime.datetime.now().strftime("%Y%m%d")
    return path.parent / f"{stem}-v{n}-{stamp}{suffix}"


def _archive_prior_versions(path: pathlib.Path, archive_dir: str) -> None:
    """Moves any already-versioned live file for this stem into `archive_dir`, name unchanged (it
    already carries its version and date). A plain-named file is left alone. The live folder holds at
    most one current file per report; the lineage lives in `archive_dir`."""
    rx = _versioned_rx(path.stem, path.suffix)
    if not path.parent.exists():
        return
    for f in path.parent.glob(f"{path.stem}-v*{path.suffix}"):
        if rx.match(f.name):
            adir = path.parent / archive_dir
            adir.mkdir(parents=True, exist_ok=True)
            f.replace(adir / f.name)


def write_report(conn: sqlite3.Connection, step: str, path: pathlib.Path,
                 lines: list[str]) -> pathlib.Path:
    """`report.version_on_regenerate` (app-wide, default true): prior versioned files are archived
    (`_archive_prior_versions`) and the new content is written under the next version
    (`next_versioned_path`). When false: archive the existing file (if any), then overwrite the plain
    path.

    With versioning on, `cfg_report.naming_scheme` decides the plain name:
      - 'stable' (a fixed filename others link to, e.g. CONFIG-REPORT.md): the plain-named `path` is
        also refreshed with the same content (#702).
      - 'dated' (per-id/per-run snapshots): only the versioned file is written; a leftover plain-named
        file is archived the first time the report regenerates (#857)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    rep = conn.execute("SELECT archive_dir, naming_scheme FROM cfg_report WHERE step=?",
                       (step,)).fetchone()
    archive_dir = (rep["archive_dir"] if rep else None) or "archive"
    dated = bool(rep and rep["naming_scheme"] == "dated")
    text = "\n".join(lines)
    if not text.endswith("\n"):
        text += "\n"
    if _setting(conn, "report.version_on_regenerate", True):
        _archive_prior_versions(path, archive_dir)
        versioned_path = next_versioned_path(path, archive_dir)
        versioned_path.write_text(text, encoding="utf-8")
        if dated:
            if path.exists():  # leftover plain-named file: archive it
                adir = path.parent / archive_dir
                adir.mkdir(parents=True, exist_ok=True)
                stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                path.replace(adir / f"{path.stem}-{stamp}{path.suffix}")
        else:
            path.write_text(text, encoding="utf-8")  # keep the fixed name current, see docstring
        return versioned_path
    else:
        archive_before_write(path, archive_dir)
        path.write_text(text, encoding="utf-8")
        return path


def write_csv_pairing(conn: sqlite3.Connection, step: str, out_dir: pathlib.Path,
                      row_filter: dict[str, list[sqlite3.Row]] | None = None) -> list[pathlib.Path]:
    """For every table registered in cfg_report_csv_table for `step`, write out_dir/{table}.csv,
    verbatim, every column. `row_filter` supplies pre-filtered rows for a table_name (word/book-scoped
    reports pass their own slice; see cfg_report_csv_table.join_note). A `cfg_*` wildcard row expands
    to every live cfg_* table."""
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


_STEM_VERSION_RE = re.compile(r"^(.*)-v(\d+)(\.[^.]+)$")


def _stem_and_version(path: pathlib.Path) -> tuple[str, int]:
    """(base-stem+ext, version) for any file in a one-off report's lineage: `{stem}.ext` (implicit 1)
    and `{stem}-v{n}.ext` share a base key. Shared by `oneoff_path`,
    `cfgquality.find_report_version_clutter` and any cleanup sweep."""
    m = _STEM_VERSION_RE.match(path.name)
    if m:
        return m.group(1) + m.group(3), int(m.group(2))
    return path.name, 1


def group_oneoff_versions(out_dir: pathlib.Path) -> dict[str, list[tuple[int, pathlib.Path]]]:
    """Every file directly in `out_dir` (not recursive), grouped by base stem as `(version, path)`
    lists. A group of more than one means several versions are live at once."""
    groups: dict[str, list[tuple[int, pathlib.Path]]] = {}
    if not out_dir.exists():
        return groups
    for f in out_dir.iterdir():
        if not f.is_file():
            continue
        base, ver = _stem_and_version(f)
        groups.setdefault(base, []).append((ver, f))
    return groups


def archive_oneoff_clutter(out_dir: pathlib.Path, archive_dir: str = "archive") -> list[str]:
    """For every lineage in `out_dir` with more than one live version, archive all but the highest.
    Returns the archived filenames. Used by `oneoff_path` on every call."""
    adir = out_dir / archive_dir
    archived: list[str] = []
    for base, items in group_oneoff_versions(out_dir).items():
        if len(items) <= 1:
            continue
        items.sort(key=lambda t: t[0])
        for ver, f in items[:-1]:
            adir.mkdir(parents=True, exist_ok=True)
            f.replace(adir / f.name)
            archived.append(f.name)
    return archived


def oneoff_path(cfg, topic: str, ext: str | None = None) -> pathlib.Path:
    """The path for a one-off ("investigatory") report, which has no `cfg_step`/`cfg_report` row:
    folder and naming come from config (`governance.oneoff_*`). `cfg` is a lib.cfg.Cfg (or any object
    with .setting(key, default)). Same-day version bump and archive-before-write are
    `lib/filingkit.versioned_path()`; this is a thin wrapper for existing call sites."""
    from . import filingkit
    return filingkit.versioned_path(cfg, topic, ext=ext)


def _write_csv(path: pathlib.Path, cols: list[str], rows: list[list]) -> pathlib.Path:
    import csv
    archive_before_write(path)
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(rows)
    return path
