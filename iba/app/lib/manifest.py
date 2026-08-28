"""manifest.py — the project-wide file manifest: rebuild and search.

Ported from `scripts/build_file_manifest.py` (a standalone main-repo script — filename/path
metadata only, never file *content*) per the researcher's 2026-08-15 instruction that manifest
build/update/search must be governed IBA App functionality, with rules and a user guide, not a
standalone script nothing else knows about. The manifest still indexes the WHOLE project tree, not
`iba/` only — the governing MECHANISM moves into IBA; the TARGET doesn't shrink (per the
researcher's own framing: "IBA App is the engine for all processing related tables").

Category/type/currency classification and the date/registry/version/cluster/word extraction
patterns below are project-naming FACTS — how files across this repo's actual history have been
named — not policy decisions anyone proposes to change via `configmaint.propose`. That's the same
distinction the STEP client config (`iba/config/utility/step.json`) draws between "facts" (code:
canon order, response field names) and "choices" (config: base_url, timeouts) — so these stay in
code, ported near-verbatim from the working script. What genuinely IS a decision — which
directories/extensions to skip during a scan — is `cfg_setting`, per
`governance.rules_must_be_config_driven`.

This module is the baseline for `contentindex.py` (round 2, file-content concordance search): the
manifest's `file_manifest` table is the authoritative "what files exist" list that the content
index is cross-checked against, so no file with real content silently falls outside search
coverage.

Writes to the `file_manifest` table in THIS app's own DB (`iba.db`) — not the loose JSON file
`scripts/build_file_manifest.py` produces. That script and `database/file_manifest.json` are
superseded once this ships (their logic lives here now), not run in parallel.
"""

from __future__ import annotations

import datetime
import os
import pathlib
import re
import sqlite3

from . import reportkit

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[3]  # iba/app/lib/ -> iba/app -> iba -> repo root

# ---------------------------------------------------------------------------
# Project-naming facts (ported from scripts/build_file_manifest.py — see module docstring)
# ---------------------------------------------------------------------------

_DATE_COMPACT = re.compile(r'(\d{4})(\d{2})(\d{2})')
_DATE_HYPHEN = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
_REG_PATTERNS = [
    re.compile(r'(?:^|[-_])(\d{3})[-_]'),
    re.compile(r'registry[_-]?(\d+)', re.I),
    re.compile(r'reg[_-]?(\d{3})', re.I),
    re.compile(r'[-_](\d{1,3})[-_](?:full|report|complete|owner)', re.I),
]
_VERSION_RE = re.compile(r'-v(\d+(?:\.\d+)?)')
_VCB_RE = re.compile(r'vcb[_-]?(\d{3})', re.I)
_CLUSTER_RE = re.compile(r'(?:^|[-_])(c\d{2})(?:[-_]|$)', re.I)
_WORD_FROM_WA = re.compile(r'wa-\d{3}-([a-z]+)')
_WORD_FROM_UNDERSCORE = re.compile(r'^([a-z]+)_\d+')
_WORD_FROM_LONG = re.compile(r'(?:registry|reg)\d+-([a-z]+)', re.I)

# Evaluated top-to-bottom; first match wins. An `archive/` segment anywhere overrides to "archived"
# regardless of this table (checked first in compute_currency).
_CURRENCY_RULES = [
    ("sessions-v2/", "current"), ("workflow/", "current"), ("research/", "current"),
    ("docs/", "current"), ("outputs/", "current"), ("scripts/", "current"),
    ("engine/", "current"), ("database/", "current"), ("data/", "current"), ("iba/", "current"),
    # 2026-08-28 (escalation #971/#976) — folders this week's reorg created, same reasoning as
    # classify_category()'s matching addition just above.
    ("_analytics/", "current"), ("_raw_data/", "current"), ("memory/", "current"),
    ("sessions/session_clusters", "cross-reference"), ("sessions/", "cross-reference"),
    ("logs/", "historical"), ("backups/", "backup"),
]


def extract_date(filename: str) -> str | None:
    m = _DATE_HYPHEN.search(filename)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = _DATE_COMPACT.search(filename)
    if m:
        y, mo, d = m.group(1), m.group(2), m.group(3)
        if 2025 <= int(y) <= 2030 and 1 <= int(mo) <= 12 and 1 <= int(d) <= 31:
            return f"{y}-{mo}-{d}"
    return None


def extract_registry(filename: str) -> int | None:
    for pat in _REG_PATTERNS:
        m = pat.search(filename)
        if m:
            val = int(m.group(1))
            if 1 <= val <= 300:
                return val
    return None


def extract_version(filename: str) -> str | None:
    m = _VERSION_RE.search(filename)
    return m.group(1) if m else None


def extract_vcb_batch(filename: str) -> int | None:
    m = _VCB_RE.search(filename)
    return int(m.group(1)) if m else None


def extract_cluster(filename: str) -> str | None:
    m = _CLUSTER_RE.search(filename)
    return m.group(1).upper() if m else None


def extract_word(filename: str) -> str | None:
    m = _WORD_FROM_WA.search(filename)
    if m:
        return m.group(1)
    m = _WORD_FROM_UNDERSCORE.search(filename)
    if m:
        return m.group(1)
    m = _WORD_FROM_LONG.search(filename)
    if m:
        return m.group(1).lower()
    return None


def compute_currency(rel_path: str) -> str:
    p = rel_path.replace("\\", "/").lower()
    if p.startswith("archive/") or "/archive/" in p:
        return "archived"
    for prefix, status in _CURRENCY_RULES:
        if p.startswith(prefix):
            return status
    return "other"


def classify_category(rel_path: str) -> str:
    parts = rel_path.replace("\\", "/").lower()
    if parts.startswith("archive/"):
        # Stripped-prefix reclassification, not a fresh hand-enumerated rule per archive
        # subfolder (added 2026-08-28, escalation #971/#976/pathaudit) — the 2026-08-27 reorg
        # (~7,900 files renamed into archive/ subfolders, researcher's own framing) made the old
        # 4 hand-picked archive/{scripts,logs,docs,patches} rules stale by construction: any NEW
        # archive subfolder fell straight through to 'other' with no rule ever written for it.
        # Reclassifying by what the content WOULD be outside archive/ is the general fix; the 4
        # original rules still apply first since they're literal prefix matches checked below,
        # this is only the fallback for everything they don't already catch.
        inner = classify_category(parts[len("archive/"):])
        if inner != "other":
            return inner
    if parts.startswith("iba/"):
        return "iba"
    if parts.startswith("sessions-v2"):
        return "cluster"
    if parts.startswith("workflow"):
        return "workflow"
    if parts.startswith("research/investigations"):
        return "investigation"
    if parts.startswith("scripts/"):
        return "script"
    if parts.startswith("engine/"):
        return "code"
    if parts.startswith("sessions/"):
        return "session"
    if parts.startswith("backups/"):
        return "backup"
    if parts.startswith("data/imports/wa/patches") or parts.startswith("archive/patches"):
        if parts.endswith(".json"):
            return "patch"
        elif "directive" in parts:
            return "directive"
        return "patch"
    if parts.startswith("data/imports"):
        return "import"
    if parts.startswith("data/exports"):
        return "export"
    if parts.startswith("research/discovery"):
        return "discovery"
    if parts.startswith("research/"):
        return "investigation"  # 2026-08-28: research/{templates,notes,projects,reports} etc. —
        # smaller, less-formal siblings of research/investigations, same category
    if parts.startswith("data/schema"):
        return "schema"
    if parts.startswith("archive/scripts"):
        return "script"
    if parts.startswith("archive/logs"):
        return "log"
    if parts.startswith("archive/docs"):
        return "doc"
    if parts.startswith("outputs/reports"):
        return "report"
    if parts.startswith("outputs"):
        return "report"
    if parts.startswith("docs"):
        return "doc"
    if parts.startswith("logs"):
        return "log"
    # 2026-08-28 (escalation #971/#976) — folders created/populated by this week's reorg that
    # simply didn't exist when this function was last written, found live via folder_purpose's
    # own census: _analytics/ (6,577 files, per-word/per-book/per-cluster analysis OUTPUT, closest
    # existing category is 'report'), _raw_data/ (1,033 files, raw imported source data, same
    # concept 'import' already names for data/imports), memory/ (project memory mirror, markdown
    # facts, closest existing category is 'doc').
    if parts.startswith("_analytics"):
        return "report"
    if parts.startswith("_raw_data"):
        return "import"
    if parts.startswith("memory"):
        return "doc"
    return "other"


def classify_type(filename: str, category: str, rel_path: str) -> str:
    fn = filename.lower()
    rp = rel_path.replace("\\", "/").lower()

    if category == "iba":
        if "/migration/" in rp:
            return "iba-migration"
        if "/ps/" in rp:
            return "iba-ps-script"
        if "/handlers/" in rp:
            return "iba-handler"
        if "/lib/" in rp:
            return "iba-lib"
        if "/config/" in rp:
            return "iba-config"
        if "/reports/" in rp or "/export/" in rp:
            return "iba-report"
        if "/verse-analysis/" in rp:
            return "iba-verse-analysis"
        if fn == "governance.md":
            return "iba-governance"
        if fn == "build.md":
            return "iba-build-log"
        if "user-guide" in fn:
            return "iba-user-guide"
        if "session-log" in fn:
            return "iba-session-log"
        return "iba-other"

    if category == "patch":
        if "preanalysis" in fn:
            return "preanalysis-patch"
        if "analysis" in fn and "pre" not in fn:
            return "analysis-patch"
        if "repair" in fn:
            return "repair-patch"
        if "dim" in fn:
            return "dimension-patch"
        return "patch"
    if category == "directive":
        return "cc-directive"
    if category == "import":
        if "observations" in fn:
            return "observations"
        if "session-log" in fn or "sessionlog" in fn or "session_log" in fn:
            return "session-log"
        if "instruction" in fn:
            return "instruction"
        if "flag" in fn:
            return "flags"
        if fn.endswith(".json"):
            return "session-a-data"
        return "import"
    if category == "export":
        if "step extracts" in rp or "step_extracts" in rp:
            return "step-extract"
        if "session c" in rp or "session_c" in rp:
            return "owner-only-extract" if ("owner_only" in fn or "owner-only" in fn) else "complete-extract"
        if "verse_context" in rp:
            return "vc-batch-extract"
        if "dimension_review" in rp:
            return "dim-extract"
        if "session_d" in rp:
            return "sd-pointers"
        return "export"
    if category == "discovery":
        return "discovery-json" if fn.endswith(".json") else "discovery-summary"
    if category == "report":
        if "programme" in rp:
            return "programme-report"
        if "words" in rp:
            return "word-report"
        return "report"
    if category == "investigation":
        return "investigation"
    if category == "schema":
        return "ddl" if fn.endswith(".sql") else "schema-snapshot"
    if category == "doc":
        if "architecture" in fn:
            return "architecture"
        if "organisation" in fn or "organization" in fn:
            return "org-rules"
        if "interaction" in fn:
            return "interaction-prefs"
        return "doc"
    if category == "log":
        return "session-log"
    return "other"


# ---------------------------------------------------------------------------
# Config-driven scan settings (decisions — cfg_setting, not facts)
# ---------------------------------------------------------------------------

_SKIP_DIRS_DEFAULT = [".git", "__pycache__", "venv", ".venv", "env", "node_modules",
                      ".claude", ".idea", ".vscode", ".pytest_cache", ".mypy_cache", ".ruff_cache"]
_EXCLUDE_EXTS_DEFAULT = [".pyc", ".pyo", ".pyd", ".tmp", ".swp", ".lock"]


def _folder_purpose_lookup(cfg) -> list[tuple[str, str, str]]:
    """(folder_path, manifest_category, manifest_currency) for every folder_purpose row that has
    at least one of the two set, longest-path-first so the caller's prefix match picks the most
    specific governing row. Escalation #971 Part D: folder_purpose is the primary classification
    source once a folder is registered; classify_category()/compute_currency() below remain the
    fallback for anything not yet registered there — non-breaking by construction."""
    try:
        rows = cfg.conn.execute(
            "SELECT folder_path, manifest_category, manifest_currency FROM folder_purpose "
            "WHERE manifest_category IS NOT NULL OR manifest_currency IS NOT NULL").fetchall()
    except Exception:
        return []  # folder_purpose not built yet (pre-#971) — pure fallback, unchanged behaviour
    return sorted(((r["folder_path"], r["manifest_category"], r["manifest_currency"]) for r in rows),
                 key=lambda t: -len(t[0]))


def _scan(cfg) -> list[dict]:
    skip_dirs = set(cfg.setting("manifest.skip_dirs", _SKIP_DIRS_DEFAULT))
    exclude_exts = set(cfg.setting("manifest.exclude_exts", _EXCLUDE_EXTS_DEFAULT))
    fp_rules = _folder_purpose_lookup(cfg)
    entries = []
    for dirpath, dirnames, filenames in os.walk(PROJECT_ROOT):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for fname in filenames:
            fpath = pathlib.Path(dirpath) / fname
            ext = fpath.suffix.lower()
            if ext in exclude_exts:
                continue
            rel = fpath.relative_to(PROJECT_ROOT).as_posix()
            try:
                stat = fpath.stat()
            except OSError:
                continue
            fp_category = fp_currency = None
            rel_lower = rel.lower()
            for folder_path, fp_cat, fp_cur in fp_rules:
                prefix = folder_path.lower() + "/"
                if rel_lower.startswith(prefix):
                    fp_category, fp_currency = fp_cat, fp_cur
                    break
            category = fp_category or classify_category(rel)
            file_type = classify_type(fname, category, rel)
            currency = fp_currency or compute_currency(rel)
            entries.append({
                "path": rel, "category": category, "file_type": file_type, "currency": currency,
                "archived": 1 if currency == "archived" else 0,
                "registry": extract_registry(fname), "word": extract_word(fname),
                "cluster": extract_cluster(fname), "vcb_batch": extract_vcb_batch(fname),
                "version": extract_version(fname), "date": extract_date(fname), "ext": ext,
                "size_bytes": stat.st_size,
                "modified_at": datetime.datetime.fromtimestamp(
                    stat.st_mtime, tz=datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            })
    entries.sort(key=lambda e: e["path"])
    return entries


def rebuild(cfg) -> dict:
    """Full rescan of the whole project tree. Replaces the table's contents — this is a rebuild,
    not an incremental update (see contentindex.py for the mtime-based incremental refresh the
    content-search step relies on for its own index)."""
    conn: sqlite3.Connection = cfg.conn
    entries = _scan(cfg)
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    conn.execute("DELETE FROM file_manifest")
    conn.executemany(
        "INSERT INTO file_manifest (path, category, file_type, currency, archived, registry, "
        "word, cluster, vcb_batch, version, date, ext, size_bytes, modified_at, scanned_at) "
        "VALUES (:path,:category,:file_type,:currency,:archived,:registry,:word,:cluster,"
        ":vcb_batch,:version,:date,:ext,:size_bytes,:modified_at,:scanned_at)",
        [{**e, "scanned_at": now} for e in entries])
    conn.commit()

    by_category: dict[str, int] = {}
    by_currency: dict[str, int] = {}
    for e in entries:
        by_category[e["category"]] = by_category.get(e["category"], 0) + 1
        by_currency[e["currency"]] = by_currency.get(e["currency"], 0) + 1

    return {
        "scanned_at": now, "total": len(entries),
        "active": sum(1 for e in entries if not e["archived"]),
        "archived": sum(1 for e in entries if e["archived"]),
        "by_category": by_category, "by_currency": by_currency,
    }


_SEARCH_FIELDS = {"registry", "type", "currency", "category", "cluster", "word", "date", "archived", "ext"}


def search(cfg, query: str) -> list[dict]:
    """Field:value (`registry:68`, `type:iba-migration`, `category:iba`, `currency:archived`,
    `word:grace`, `cluster:c17`, `date:2026-08`, `archived:true`, `ext:.md`) or free-text path
    substring match. Mirrors scripts/build_file_manifest.py's search_manifest() field set, now
    against the DB table instead of a loaded JSON list."""
    conn: sqlite3.Connection = cfg.conn
    if ":" in query and not query.startswith("/"):
        field, _, value = query.partition(":")
        field, value = field.strip().lower(), value.strip().lower()
        if field in _SEARCH_FIELDS:
            col = "file_type" if field == "type" else field
            if field == "registry":
                try:
                    return [dict(r) for r in conn.execute(
                        "SELECT * FROM file_manifest WHERE registry=? ORDER BY path", (int(value),))]
                except ValueError:
                    return []
            if field == "archived":
                want = 1 if value in ("true", "1", "yes") else 0
                return [dict(r) for r in conn.execute(
                    "SELECT * FROM file_manifest WHERE archived=? ORDER BY path", (want,))]
            if field in ("currency", "cluster", "word", "ext"):
                return [dict(r) for r in conn.execute(
                    f"SELECT * FROM file_manifest WHERE lower({col})=? ORDER BY path", (value,))]
            # type/category/date: substring/prefix match, matching the script's original semantics
            op = "LIKE" if field == "date" else "LIKE"
            pat = f"{value}%" if field == "date" else f"%{value}%"
            return [dict(r) for r in conn.execute(
                f"SELECT * FROM file_manifest WHERE lower({col}) {op} ? ORDER BY path", (pat,))]
    return [dict(r) for r in conn.execute(
        "SELECT * FROM file_manifest WHERE lower(path) LIKE ? ORDER BY path", (f"%{query.lower()}%",))]


def write_rebuild_report(cfg, path: pathlib.Path, summary: dict) -> pathlib.Path:
    intro = [f"> Generated {summary['scanned_at']}. Rescans the WHOLE project tree from the repo "
            f"root (VCS/build/cache machinery excluded, per `manifest.skip_dirs`) — filename/path "
            f"metadata only, no file content read. This is the baseline the content-search index "
            f"(round 2) cross-checks coverage against."]
    cat_rows = [[cat, n] for cat, n in sorted(summary["by_category"].items(), key=lambda kv: -kv[1])]
    cur_rows = [[cur, n] for cur, n in sorted(summary["by_currency"].items(), key=lambda kv: -kv[1])]
    sections = {
        "summary": [f"- **{summary['total']}** files indexed — {summary['active']} active, "
                   f"{summary['archived']} archived"],
        "by_category": _tbl(["category", "count"], cat_rows),
        "by_currency": _tbl(["currency", "count"], cur_rows),
    }
    L = reportkit.render_scaffold(cfg.conn, "manifest.rebuild", sections, intro=intro)
    return reportkit.write_report(cfg.conn, "manifest.rebuild", path, L)


def _tbl(headers, rows):
    L = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        L.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    return L


def write_search_report(cfg, query: str, results: list[dict]) -> pathlib.Path:
    """One-off, per-call result persistence (governance.reports_must_persist) — no cfg_step-keyed
    cfg_report row needed; path/naming/archiving come from governance.oneoff_* config, per
    reportkit.oneoff_path's own doc."""
    path = reportkit.oneoff_path(cfg, f"manifest-search-{query}", ext="md")
    lines = [f"# Manifest search — `{query}`", "", f"{len(results)} match(es).", ""]
    lines += _tbl(["path", "category", "type", "currency"],
                  [[r["path"], r["category"], r["file_type"], r["currency"]] for r in results[:500]])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path
