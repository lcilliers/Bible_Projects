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
import json
import pathlib
import re
import sqlite3
import time


def _setting(conn: sqlite3.Connection, key: str, default=None):
    """Same read semantics as `lib/cfg.py:Cfg.setting` (inactive=0 filter, JSON-decoded value) —
    duplicated narrowly here rather than importing `Cfg` itself, since `reportkit.py` is
    deliberately dependency-light (stdlib + a bare `sqlite3.Connection`, no app-object coupling)."""
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

    # `<a id="...">` immediately before each heading, not a bare "## Heading" left to the
    # viewer's own auto-slugger — found 2026-08-09 (researcher: ToC links don't work, "in all of
    # the reports in the app") that different Markdown renderers (GitHub / VS Code preview /
    # Obsidian / pandoc) slug punctuation-heavy headings differently from `anchor()` above (this
    # app's own collapsing of "--" into "-" is not universal — GitHub's own slugger, for one,
    # does NOT collapse), so a ToC link computed here was never guaranteed to land on the heading
    # a renderer actually generated. An explicit anchor sidesteps the whole class of mismatch —
    # every renderer that runs raw HTML in Markdown (near-universal) resolves it identically.
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
    """GitHub-style heading slug — good enough for this app's own ToC links. Public (not just
    `render_scaffold`'s own internal use) since a generator building its OWN in-body sub-ToC
    (e.g. `wordregistryspanreport.py`'s per-cluster links, cfg_report_section being too static
    to represent dynamic per-run structure) needs the exact same slugging rule, not a second
    hand-written copy of it."""
    text = heading.lstrip("#").strip().lower()
    out = ["-" if ch in (" ", "-", "_") else ch for ch in text if ch.isalnum() or ch in " -_"]
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


def archive_before_write(path: pathlib.Path, archive_dir: str = "archive") -> None:
    """If `path` already exists, move it to `path.parent/archive_dir/{stem}-{stamp}{suffix}` first
    — shared by every report/export writer (`write_report`, `_write_csv`, `export_tables_csv.export`)
    so a regenerate never silently destroys the prior snapshot (researcher's 2026-07-22 instruction,
    extended 2026-07-23 to CSV exports — escalation #273 found this convention only covered .md
    report writes, not the CSV pairing or the table-export dump, both of which were silently
    overwriting on every run with no prior version kept).

    Retries the move a few times on a transient lock (escalation #1320, 2026-08-31: crashed
    uncaught -- #1307/#1308 -- the moment `path` happened to be open in another process, e.g.
    Excel, at exactly the wrong instant; the #1314 fix reduced how often this *particular* CSV
    write ran, it never made the write itself resilient). A short, bounded retry only helps a
    genuinely transient hold (an editor's brief save-lock); a file left open for the run's whole
    duration still surfaces the same PermissionError after the retries, uncaught exactly as
    before -- run_step()'s existing crash handler (run.py) still records it as a real, visible
    escalation. Not a silent swallow, just a chance for a moment's contention to clear."""
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
    """`{stem}-v{n}-{date}{suffix}` — n = 1 + the highest version number found for this exact stem,
    scanning BOTH `path.parent` (the current live one, if any) AND `path.parent/archive_dir` (every
    superseded one) — version numbers stay monotonic across a report's whole lifetime even though
    `write_report` archives every prior version out of the live folder (below). Not date-scoped, so
    it keeps climbing across any gap in time, never resets, never collides. A caller's pre-existing
    *plain*-named file (from before this setting existed) is untouched by this scan — it doesn't
    match the `-v<n>-` pattern, so numbering starts fresh at 1 rather than trying to detect and
    continue an unversioned lineage."""
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
    """Moves any already-versioned file currently live for this stem into `archive_dir`, keeping
    its own version-numbered filename exactly as-is (no re-stamping — the name already carries its
    own version + date, that IS its archive identity). Leaves a pre-existing *plain*-named file
    (legacy, pre-dating this setting) untouched — same non-interference `next_versioned_path`
    already documents. Researcher, 2026-08-05: "as long as the archiving runs alongside the
    versioning" — the live folder holds at most one current file per report; the full lineage lives
    in `archive_dir`, nothing is ever silently lost."""
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
    """`report.version_on_regenerate` (module `report`, app-wide — governs every report writer
    uniformly, not a per-step convention): when true (the default since 2026-08-05), archiving and
    versioning both run, together — researcher, 2026-08-05: "as long as the archiving runs alongside
    the versioning, as it should." Any already-versioned file currently live for this stem is moved
    into `cfg_report.archive_dir` first (`_archive_prior_versions`, name unchanged — it's already
    self-describing), THEN the new content is written under a freshly incremented version
    (`next_versioned_path`, which counts archived versions too, so numbering stays monotonic). When
    false, falls back to the pre-2026-08-05 behaviour: archive the existing file (if any), then
    overwrite the same plain path (researcher's 2026-07-22 instruction) — kept as the opt-out, not
    removed.

    **Also refreshes the plain-named `path` even when versioning is on — fixed 2026-08-17,
    escalation #702 — but only for `cfg_report.naming_scheme='stable'` reports.**
    `_archive_prior_versions`/`next_versioned_path` both deliberately ignore a pre-existing
    plain-named file "untouched by this scan" — true, but the consequence went unnoticed for 12
    days: `CONFIG-REPORT.md`, the fixed filename `GOVERNANCE.md`/`USER-GUIDE.md` tell every reader
    to check, silently froze at whatever content existed the moment versioning was turned on
    (2026-08-05) and was never touched again — every regenerate since only added a new `-vNNN-`
    file alongside it. The researcher found this by hitting stale, wrong orphan-config findings
    live. Both purposes are real and not in tension for a *stable* report: versioning preserves
    history (`archive_dir`), the plain name is what every doc and habit actually checks — so both
    get written for those.

    **naming_scheme='dated' reports skip the plain-name write entirely — fixed 2026-08-26,
    escalation #857.** A "dated" report (per-id/per-run snapshots like `escalation.history`, or a
    `{word}`/`{strong}`-keyed report) has no fixed name anything else links to — `naming_scheme`
    already documented this distinction (PLAN-reports-config-governance-v1-20260722.md §6:
    'stable' (fixed filename) | 'dated' (versioned filename per report)) but `write_report()` never
    actually read the column, so every regenerate produced BOTH the versioned file AND a redundant,
    never-linked plain-named duplicate (`857-escalation-history.md` sitting alongside
    `857-escalation-history-v3-20260826.md` with identical content — found live, researcher
    instruction this escalation). For `naming_scheme='dated'`: only the freshly versioned file is
    written; a stale plain-named file left over from before this fix is archived (not silently
    deleted) the first time the report regenerates, same as any other superseded version."""
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
            if path.exists():  # stale pre-fix plain-named duplicate -- archive it, don't leave it
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


_STEM_VERSION_RE = re.compile(r"^(.*)-v(\d+)(\.[^.]+)$")


def _stem_and_version(path: pathlib.Path) -> tuple[str, int]:
    """(base-stem+ext, version) for any file in a one-off report's lineage — `{stem}.ext` (the
    first-ever version, implicit `1`) and `{stem}-v{n}.ext` both normalise to the SAME base key, so
    grouping by it finds every version of the same report regardless of which one is unversioned.
    Shared by `oneoff_path` (archives before writing), `cfgquality.find_report_version_clutter`
    (detects a regression), and any one-time cleanup sweep — one place this grouping rule lives,
    never a second hand-written copy of it (2026-08-08)."""
    m = _STEM_VERSION_RE.match(path.name)
    if m:
        return m.group(1) + m.group(3), int(m.group(2))
    return path.name, 1


def group_oneoff_versions(out_dir: pathlib.Path) -> dict[str, list[tuple[int, pathlib.Path]]]:
    """Every file directly in `out_dir` (not recursive — subdirectories like `archive/`/`export/`
    are never one-off report lineage members themselves), grouped by base stem, each entry a
    `(version, path)` list. A group of size 1 is a normal, un-cluttered report (nothing to do); a
    group of size >1 means more than one version is simultaneously "live" — exactly the gap
    `oneoff_path` had until 2026-08-08 (BUILD.md §83)."""
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
    """For every report lineage in `out_dir` with more than one version currently live, archive
    every version except the highest-numbered one. Returns the archived filenames (for a caller to
    report, never silent). Used both by the one-time retroactive sweep and, in single-lineage form,
    by `oneoff_path` itself on every call."""
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
    """Phase 2 of PLAN-reports-config-governance-v1-20260722.md §5 — the path for a one-off
    ("investigatory") report: no `cfg_step`, so no `cfg_report` row to key off, but the
    folder/naming still comes from config (`governance.oneoff_*`), not a literal string a future
    migration/investigation script hardcodes. `cfg` is a lib.cfg.Cfg (or any object with
    .setting(key, default)).

    Same-day version bump on collision, archive-before-write — full mechanics now in
    `lib/filingkit.versioned_path()` (escalation #863/#971/#992, generalised 2026-08-28 for any
    caller project-wide, not just `iba/app/reports/`); this is a thin wrapper kept for every
    existing call site, behaviourally identical to before the generalisation."""
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
