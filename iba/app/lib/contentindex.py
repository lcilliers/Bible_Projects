"""contentindex.py — file-content concordance search (round 2, governance-alignment register item
#6 / escalation #691). Built on top of `manifest.py` (round 1): `file_manifest` is the coverage
baseline this cross-checks against, so no `.md` file with real content silently falls outside
search.

**Predefined-key concordance, NOT free-text FTS** (researcher, 2026-08-15: "the search keys will
be predefined" / "we can use DB tables (e.g. strong numbers and gloss) as the keys"). Three key
sources, all already inside `iba.db` — no cross-database read (researcher's own framing: "IBA App
is the engine for all processing related tables... research_db will be used for analytic
findings"):

  - `strong.strongNumber` — e.g. `H2734` (15,293 rows)
  - `strong.stepGloss` — the English gloss text (9,165 distinct values, measured live)
  - `word_registry.word` — the project's own English-word list (180 rows, measured live)

**Matching is tokenize + n-gram + set lookup, NOT a giant regex alternation** — tested live before
committing to this design: compiling a single `re` alternation over the ~9,300 gloss+word keys
hung outright (catastrophic cost at this pattern count, confirmed by direct measurement, not
assumed from theory). Every gloss is at most 6 words (measured: 5,725 single-word, down to 3
six-word glosses, nothing longer) — so each line's words are tokenized once, then checked as
1..6-word windows against a lowercased key set, which is O(line length) and independent of key
count. Strong's numbers get a separate, simpler regex-extract + set-membership pass (fixed shape,
`[HG]\\d{4,5}[A-Z]?`, no tokenization needed).

**Incremental, per the researcher's own flow** ("search must search the file metadata, and then
the content, and then update the index... result will include the file reference and location"):
`search()` runs an mtime-based incremental `refresh()` first — only `.md` files new/changed since
`content_index_scan`'s last pass are re-scanned — then queries the now-current index, then returns
hits enriched with `file_manifest`'s own metadata alongside the content hit's file path and line
number. `rebuild()` (a full rescan, clearing both tables first) exists separately for the explicit
full-reindex case, same split as `manifest.py`'s `rebuild()`.

Scope: `.md` files only, project-wide, including `archive/` — reads `file_manifest` (built by
`manifest.rebuild`) as the file list rather than re-walking the tree itself, so manifest and
content-index coverage can never silently diverge.
"""

from __future__ import annotations

import csv
import datetime
import pathlib
import re
import sqlite3

from . import reportkit

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[3]  # lib/ -> app -> iba -> repo root

_STRONG_RE = re.compile(r"\b([HG]\d{4,5}[A-Z]?)\b")
_TOKEN_RE = re.compile(r"[A-Za-z']+")
_MAX_NGRAM = 6  # longest gloss is 6 words, measured live 2026-08-17 — see module docstring

# Found live 2026-08-17, before the first real rebuild ran: a 50-file sample produced 19,118 hits
# (382/file) — checked why, not assumed acceptable. strong.stepGloss genuinely carries single-word
# glosses for Hebrew/Greek conjunctions/particles ('and', 'or', 'not', 'this', 'that', 'with',
# 'for', 'as', 'so', 'if', 'no', 'i', 'on' all confirmed present) — real STEP data, not an error,
# but useless as SEARCH KEYS: virtually every line of English prose contains them, defeating the
# concordance's actual purpose (finding meaningful term occurrences, not every file in the
# project). Excluded from 1-WORD key matching only — a multi-word gloss/phrase containing one of
# these is unaffected, already specific enough on its own.
_STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "so", "as", "of", "to", "in", "on", "at", "by",
    "for", "with", "from", "into", "onto", "upon", "over", "under", "about", "not", "no", "nor",
    "is", "are", "was", "were", "be", "been", "being", "do", "does", "did", "have", "has", "had",
    "i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them", "this", "that",
    "these", "those", "my", "your", "his", "its", "our", "their", "who", "what", "when", "where",
    "why", "how", "all", "any", "each", "few", "more", "most", "some", "such", "than", "then",
    "there", "here", "up", "down", "out", "off", "again", "further", "once", "own", "same", "too",
    "very", "just", "will", "would", "shall", "should", "can", "could", "may", "might", "must",
}


def _build_keys(cfg) -> tuple[set[str], dict[int, dict[str, list[tuple[str, str]]]]]:
    """Returns (strong_number_set, ngram_key_map). `ngram_key_map[n]` maps a lowercased n-word
    phrase to every (key_type, original_key_value) it matches — a gloss and a word can share text,
    both are kept, not collapsed."""
    conn: sqlite3.Connection = cfg.conn
    strong_numbers = {r[0] for r in conn.execute(
        "SELECT strongNumber FROM strong WHERE deleted=0 AND strongNumber IS NOT NULL")}

    ngram_map: dict[int, dict[str, list[tuple[str, str]]]] = {n: {} for n in range(1, _MAX_NGRAM + 1)}

    def _add(key_type: str, value: str) -> None:
        value = (value or "").strip()
        if not value:
            return
        words = value.lower().split()
        n = len(words)
        if n < 1 or n > _MAX_NGRAM:
            return
        if n == 1 and words[0] in _STOPWORDS:
            return
        ngram_map[n].setdefault(" ".join(words), []).append((key_type, value))

    # T2-assigned strongs excluded, researcher 2026-08-17: "gloss for any T2 cluster terms can be
    # excluded" — T2 is cluster's own "landing zone for codes not included in analysis" (per
    # cluster.use), so its glosses are noise for a study-focused concordance. Filtered by STRONG,
    # not by gloss text: a gloss shared between a T2 strong and a real-cluster strong (both can
    # exist — 30 strongs carry both, measured live) still gets indexed via the real-cluster one.
    for (gloss,) in conn.execute(
            "SELECT DISTINCT stepGloss FROM strong WHERE deleted=0 AND stepGloss IS NOT NULL "
            "AND stepGloss != '' AND strongNumber NOT IN "
            "(SELECT strong FROM cluster_strong WHERE cluster_code='T2' AND deleted=0)"):
        _add("gloss", gloss)
    for (word,) in conn.execute("SELECT word FROM word_registry WHERE deleted=0"):
        _add("word", word)

    return strong_numbers, ngram_map


def _scan_lines(text: str, strong_numbers: set[str],
                ngram_map: dict[int, dict[str, list[tuple[str, str]]]]
                ) -> list[tuple[str, str, int, str]]:
    """Returns [(key_type, key_value, line_number, snippet), ...] for every match in `text`."""
    hits: list[tuple[str, str, int, str]] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        snippet = line.strip()
        if not snippet:
            continue
        for m in _STRONG_RE.finditer(line):
            code = m.group(1)
            if code in strong_numbers:
                hits.append(("strong", code, lineno, snippet[:200]))
        words = _TOKEN_RE.findall(line.lower())
        if not words:
            continue
        for n in range(1, min(_MAX_NGRAM, len(words)) + 1):
            bucket = ngram_map[n]
            if not bucket:
                continue
            for i in range(len(words) - n + 1):
                phrase = " ".join(words[i:i + n])
                for key_type, key_value in bucket.get(phrase, ()):
                    hits.append((key_type, key_value, lineno, snippet[:200]))
    return hits


def _exclude_patterns(cfg) -> list[str]:
    """Active `cfg_content_index_exclude` patterns — a file path or folder prefix. Empty table =
    exclude nothing (the default is "include all .md except", per the researcher's own framing,
    2026-08-17 — found live that some generated dumps produce pathological hit density)."""
    conn: sqlite3.Connection = cfg.conn
    return [r[0] for r in conn.execute(
        "SELECT pattern FROM cfg_content_index_exclude WHERE inactive=0")]


def _size_override_patterns(cfg) -> list[str]:
    """Active `cfg_content_index_size_override` patterns — a file matching one is included even
    if it's at/above `content_index.exclude_size_threshold_bytes`. "Manually released if needed"
    (researcher, 2026-08-17)."""
    conn: sqlite3.Connection = cfg.conn
    return [r[0] for r in conn.execute(
        "SELECT pattern FROM cfg_content_index_size_override WHERE inactive=0")]


def _eligible_md_files(cfg) -> list[tuple[str, str]]:
    """[(path, modified_at), ...] for every `.md` row in `file_manifest` — the coverage baseline
    (see module docstring) — minus anything matching an active `cfg_content_index_exclude`
    pattern, minus anything at/above `content_index.exclude_size_threshold_bytes` (default 50MB)
    unless it matches an active `cfg_content_index_size_override` pattern. A file with no
    `file_manifest` row (manifest.rebuild hasn't run, or it was excluded there) is out of scope
    here too, by design — content-index coverage never exceeds manifest coverage."""
    conn: sqlite3.Connection = cfg.conn
    patterns = _exclude_patterns(cfg)
    threshold = cfg.setting("content_index.exclude_size_threshold_bytes", 52428800)
    overrides = _size_override_patterns(cfg)
    rows = conn.execute(
        "SELECT path, modified_at, size_bytes FROM file_manifest WHERE lower(path) LIKE '%.md' "
        "ORDER BY path")
    out = []
    for p, m, size_bytes in rows:
        if any(p.startswith(pat) for pat in patterns):
            continue
        if size_bytes >= threshold and not any(p.startswith(pat) for pat in overrides):
            continue
        out.append((p, m))
    return out


def size_profile(cfg) -> list[dict]:
    """Every `.md` file in `file_manifest`, largest first — file name, folder, size — for visual
    review before adding anything to `cfg_content_index_exclude`. Read-only, no exclusions applied
    here (this is the tool for DECIDING exclusions, so it must show everything, excluded or not)."""
    conn: sqlite3.Connection = cfg.conn
    rows = conn.execute(
        "SELECT path, size_bytes FROM file_manifest WHERE lower(path) LIKE '%.md' "
        "ORDER BY size_bytes DESC")
    out = []
    for path, size_bytes in rows:
        folder, _, name = path.rpartition("/")
        out.append({"path": path, "folder": folder or ".", "name": name or path,
                   "size_bytes": size_bytes, "size_mb": round(size_bytes / (1024 * 1024), 2)})
    return out


def write_size_profile_report(cfg, rows: list[dict]) -> pathlib.Path:
    path = pathlib.Path(cfg.required_setting("content_index.size_profile_report_path"))
    total_mb = sum(r["size_mb"] for r in rows)
    lines = ["# Content-index .md size profile", "",
            f"> {len(rows)} `.md` file(s) in `file_manifest`, {total_mb:.1f} MB total. Largest "
            f"first — for deciding what to add to `cfg_content_index_exclude` "
            f"(`Config-Maintenance.ps1 -Step Propose -Table cfg_content_index_exclude -Op insert "
            f"...`). No exclusions applied here — this shows everything.", ""]
    lines += _tbl(["size (MB)", "folder", "file"],
                 [[r["size_mb"], r["folder"], r["name"]] for r in rows])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _index_file(cfg, rel_path: str, strong_numbers: set[str],
                ngram_map: dict[int, dict[str, list[tuple[str, str]]]], now: str) -> int:
    conn: sqlite3.Connection = cfg.conn
    full = PROJECT_ROOT / rel_path
    try:
        text = full.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return 0
    hits = _scan_lines(text, strong_numbers, ngram_map)
    conn.execute("DELETE FROM content_index WHERE file_path=?", (rel_path,))
    conn.executemany(
        "INSERT OR IGNORE INTO content_index (key_type, key_value, file_path, line_number, "
        "snippet, indexed_at) VALUES (?,?,?,?,?,?)",
        [(kt, kv, rel_path, ln, sn, now) for kt, kv, ln, sn in hits])
    return len(hits)


def rebuild(cfg) -> dict:
    """Full rescan — clears content_index and content_index_scan first, re-indexes every eligible
    .md file from scratch. Use refresh() for the normal incremental path; this is the explicit
    full-reindex case (key vocabulary changed materially, or recovering from a corrupt index)."""
    conn: sqlite3.Connection = cfg.conn
    strong_numbers, ngram_map = _build_keys(cfg)
    files = _eligible_md_files(cfg)
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    conn.execute("DELETE FROM content_index")
    conn.execute("DELETE FROM content_index_scan")
    total_hits = 0
    for rel_path, modified_at in files:
        total_hits += _index_file(cfg, rel_path, strong_numbers, ngram_map, now)
        conn.execute(
            "INSERT INTO content_index_scan (file_path, mtime, scanned_at) VALUES (?,?,?)",
            (rel_path, modified_at, now))
    conn.commit()
    return {"scanned_at": now, "files_scanned": len(files), "total_hits": total_hits}


def refresh(cfg) -> dict:
    """Incremental — only .md files new or changed (by file_manifest.modified_at) since this
    file's last content_index_scan pass. Called automatically by search() (see module docstring's
    "metadata, then content, then update the index" flow) so the index is never stale at query
    time; also callable directly."""
    conn: sqlite3.Connection = cfg.conn
    known = {r[0]: r[1] for r in conn.execute("SELECT file_path, mtime FROM content_index_scan")}
    files = _eligible_md_files(cfg)
    changed = [(p, m) for p, m in files if known.get(p) != m]
    if not changed:
        return {"files_scanned": 0, "total_hits": 0, "unchanged": len(files)}

    strong_numbers, ngram_map = _build_keys(cfg)
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    total_hits = 0
    for rel_path, modified_at in changed:
        total_hits += _index_file(cfg, rel_path, strong_numbers, ngram_map, now)
        conn.execute(
            "INSERT INTO content_index_scan (file_path, mtime, scanned_at) VALUES (?,?,?) "
            "ON CONFLICT(file_path) DO UPDATE SET mtime=excluded.mtime, scanned_at=excluded.scanned_at",
            (rel_path, modified_at, now))
    conn.commit()
    return {"files_scanned": len(changed), "total_hits": total_hits,
           "unchanged": len(files) - len(changed)}


_KEY_TYPES = {"strong", "gloss", "word"}


def search(cfg, query: str) -> tuple[list[dict], dict]:
    """`key_type:value` (`strong:H2734`, `gloss:anger`, `word:anger`) or a bare value checked
    across all three key types. Runs refresh() first (metadata -> content -> index-update, per the
    researcher's own flow), then queries, then enriches each hit with file_manifest's own metadata
    alongside the content hit's file path and line number. Returns (hits, refresh_summary)."""
    refresh_summary = refresh(cfg)
    conn: sqlite3.Connection = cfg.conn

    key_type, _, value = query.partition(":")
    key_type, value = key_type.strip().lower(), value.strip()
    if key_type not in _KEY_TYPES or not value:
        key_type, value = None, query.strip()

    sql = ("SELECT ci.key_type, ci.key_value, ci.file_path, ci.line_number, ci.snippet, "
          "fm.category, fm.file_type, fm.currency FROM content_index ci "
          "LEFT JOIN file_manifest fm ON fm.path = ci.file_path WHERE ")
    if key_type:
        sql += "ci.key_type=? AND lower(ci.key_value)=lower(?)"
        params = (key_type, value)
    else:
        sql += "lower(ci.key_value)=lower(?)"
        params = (value,)
    sql += " ORDER BY ci.file_path, ci.line_number"

    rows = [dict(r) for r in conn.execute(sql, params)]
    return rows, refresh_summary


def write_rebuild_report(cfg, path: pathlib.Path, summary: dict) -> pathlib.Path:
    intro = [f"> Full content-index rebuild — {summary['files_scanned']} `.md` file(s) scanned, "
            f"{summary['total_hits']} key occurrence(s) indexed.", ""]
    sections = {"summary": [f"- scanned_at: {summary['scanned_at']}",
                            f"- files_scanned: {summary['files_scanned']}",
                            f"- total_hits: {summary['total_hits']}"]}
    L = reportkit.render_scaffold(cfg.conn, "content_index.rebuild", sections, intro=intro)
    return reportkit.write_report(cfg.conn, "content_index.rebuild", path, L)


def _tbl(headers, rows):
    L = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for row in rows:
        L.append("| " + " | ".join(str(c).replace("|", "\\|") for c in row) + " |")
    return L


def write_search_csv(cfg, query: str, hits: list[dict]) -> pathlib.Path:
    """The FULL result set, no truncation — `write_search_report`'s markdown table caps at 500
    rows for readability (a query like `gloss:compassion` returns 23,098+), which is exactly why
    a CSV export exists: for taking a large result set into a spreadsheet for real review, not a
    quick terminal glance. Same `reportkit.oneoff_path` convention as the .md report (versioned,
    archived), `.csv` extension instead."""
    path = reportkit.oneoff_path(cfg, f"content-index-search-{query}", ext="csv")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["type", "key", "file", "line", "category", "file_type", "currency",
                         "snippet"])
        for h in hits:
            writer.writerow([h["key_type"], h["key_value"], h["file_path"], h["line_number"],
                            h.get("category") or "", h.get("file_type") or "",
                            h.get("currency") or "", h["snippet"]])
    return path


def write_search_report(cfg, query: str, hits: list[dict], refresh_summary: dict) -> pathlib.Path:
    """One-off, per-call result persistence (governance.reports_must_persist) — no `cfg_step`-keyed
    `cfg_report` row needed, matching `manifest.write_search_report`'s own precedent: path/naming/
    archiving come from `governance.oneoff_*` config via `reportkit.oneoff_path`."""
    path = reportkit.oneoff_path(cfg, f"content-index-search-{query}", ext="md")
    lines = [f"# Content-index search — `{query}`", "",
            f"{len(hits)} match(es). Index refreshed first: "
            f"{refresh_summary['files_scanned']} file(s) re-scanned "
            f"({refresh_summary.get('unchanged', 0)} unchanged, skipped).", ""]
    lines += _tbl(["type", "key", "file", "line", "category", "snippet"],
                  [[h["key_type"], h["key_value"], h["file_path"], h["line_number"],
                    h.get("category") or "", h["snippet"]] for h in hits[:500]])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path
