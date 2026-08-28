"""folderpurpose.py — the `folder_purpose` reference table: seed/refresh from a live directory
scan (Method A), cross-check against `cfg_setting` `*_dir`/`*_path` values (Method B), and hand-edit
`type`/`status`/`usage_description` (Method C).

Escalation #971 (`iba/docs/folder-purpose-governance-plan-v5-20260828.md` and successors). Reference/
data table, like `books` (`bible_research.db`) — registered once in `cfg_table`/`cfg_column`
(`folder_purpose_build_v1_20260828.py`), but its rows are maintained directly here, not through
`configmaint.propose` per change (that gate governs `cfg_*` rule tables; this is project-structure
fact, the same category `books` is).

Directory-walk logic here deliberately mirrors `manifest.py`'s own scan (same `manifest.skip_dirs`
exclusions, same project root) rather than importing it, because this module walks *directories*
(one row per folder) where `manifest.py` walks *files* (one row per file) — different unit, same
tree, same exclusions.
"""

from __future__ import annotations

import datetime
import os
import pathlib
import sqlite3

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[3]  # iba/app/lib/ -> iba/app -> iba -> repo root

_SKIP_DIRS_DEFAULT = [".git", "__pycache__", "venv", ".venv", "env", "node_modules",
                      ".claude", ".idea", ".vscode", ".pytest_cache", ".mypy_cache", ".ruff_cache"]


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# Method A — manifest validate: seed/refresh disk-derived columns from a live scan
# ---------------------------------------------------------------------------

def _scan_folders(skip_dirs: set[str]) -> dict[str, dict]:
    rows: dict[str, dict] = {}
    for dirpath, dirnames, filenames in os.walk(PROJECT_ROOT):
        dirnames[:] = sorted(d for d in dirnames if d not in skip_dirs)
        rel = pathlib.Path(dirpath).relative_to(PROJECT_ROOT).as_posix()
        rel = "" if rel == "." else rel
        exts: dict[str, int] = {}
        latest_mtime = None
        for fn in filenames:
            fp = pathlib.Path(dirpath) / fn
            ext = fp.suffix.lower() or "(none)"
            exts[ext] = exts.get(ext, 0) + 1
            try:
                mt = fp.stat().st_mtime
            except OSError:
                continue
            if latest_mtime is None or mt > latest_mtime:
                latest_mtime = mt
        rows[rel] = {
            "folder_path": rel,
            "top_level_root": rel.split("/", 1)[0] if rel else "(repo root)",
            "depth": 0 if rel == "" else rel.count("/") + 1,
            "parent_path": "" if "/" not in rel else rel.rsplit("/", 1)[0],
            "direct_file_count": len(filenames),
            "direct_subfolder_count": len(dirnames),
            "recursive_file_count": 0,  # filled below
            "top_ext_direct": ", ".join(f"{e}:{c}" for e, c in
                                        sorted(exts.items(), key=lambda kv: -kv[1])[:5]),
            "last_modified_direct": (
                datetime.datetime.fromtimestamp(latest_mtime, tz=datetime.timezone.utc)
                .strftime("%Y-%m-%dT%H:%M:%SZ") if latest_mtime else None),
        }
    paths = list(rows.keys())
    all_direct_total = sum(r["direct_file_count"] for r in rows.values())
    for p in paths:
        if p == "":
            rows[p]["recursive_file_count"] = all_direct_total
            continue
        prefix = p + "/"
        total = rows[p]["direct_file_count"]
        for q in paths:
            if q != p and q.startswith(prefix):
                total += rows[q]["direct_file_count"]
        rows[p]["recursive_file_count"] = total
    return rows


def seed_from_scan(cfg) -> dict:
    """Method A. Full reconciliation against the live tree: inserts new folders, marks
    status='deleted' for folders no longer on disk (never physically removed), refreshes every
    existing row's disk-derived columns. Never touches type/status(other than 'deleted')/
    usage_description/manifest_category/manifest_currency/governed_by_setting — those are Method
    B's or Method C's, not Method A's."""
    conn: sqlite3.Connection = cfg.conn
    skip_dirs = set(cfg.setting("manifest.skip_dirs", _SKIP_DIRS_DEFAULT))
    scanned = _scan_folders(skip_dirs)
    now = _now()

    existing = {r["folder_path"]: dict(r) for r in
               conn.execute("SELECT * FROM folder_purpose")}

    # manifest_category/manifest_currency computed from the SAME classify_category()/
    # compute_currency() folder_purpose's own lookup falls back to (Part D, BUILD.md §191) —
    # recomputed on every Seed, new row or refreshed, so a manifest.py rule change propagates
    # here automatically instead of needing a separate one-off backfill script re-run by hand
    # (found live 2026-08-28: the first Seed after this function was written never set these two
    # columns for new rows at all — only a one-time manual script had; fixed here, the real "keep
    # it maintained" gap, not just the one-off data it happened to leave behind).
    from . import manifest as manifest_mod

    new_count = 0
    refreshed_count = 0
    deleted_count = 0

    for path, s in scanned.items():
        probe = (path + "/x") if path else "x"
        cat = manifest_mod.classify_category(probe)
        cur = manifest_mod.compute_currency(probe)
        if path not in existing:
            conn.execute(
                "INSERT INTO folder_purpose (folder_path, top_level_root, depth, parent_path, "
                "direct_file_count, recursive_file_count, direct_subfolder_count, top_ext_direct, "
                "last_modified_direct, manifest_category, manifest_currency, added_at) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                (s["folder_path"], s["top_level_root"], s["depth"], s["parent_path"],
                 s["direct_file_count"], s["recursive_file_count"], s["direct_subfolder_count"],
                 s["top_ext_direct"], s["last_modified_direct"], cat, cur, now))
            new_count += 1
        else:
            conn.execute(
                "UPDATE folder_purpose SET top_level_root=?, depth=?, parent_path=?, "
                "direct_file_count=?, recursive_file_count=?, direct_subfolder_count=?, "
                "top_ext_direct=?, last_modified_direct=?, manifest_category=?, "
                "manifest_currency=?, "
                "status=CASE WHEN status='deleted' THEN NULL ELSE status END "
                "WHERE folder_path=?",
                (s["top_level_root"], s["depth"], s["parent_path"], s["direct_file_count"],
                 s["recursive_file_count"], s["direct_subfolder_count"], s["top_ext_direct"],
                 s["last_modified_direct"], cat, cur, path))
            refreshed_count += 1

    for path in existing:
        if path not in scanned:
            conn.execute("UPDATE folder_purpose SET status='deleted' WHERE folder_path=?", (path,))
            deleted_count += 1

    conn.commit()
    return {"scanned_at": now, "total_on_disk": len(scanned), "new": new_count,
           "refreshed": refreshed_count, "marked_deleted": deleted_count}


# ---------------------------------------------------------------------------
# Method B — configmaint cross-check: sync governed_by_setting, enforce the invariant
# ---------------------------------------------------------------------------

def normalize_setting_value(raw: str) -> str | None:
    """Returns a lowercase folder-path candidate, or None if the value isn't plausibly a bare
    folder path at all (a JSON list like manifest.skip_dirs, or a prose/policy sentence like
    governance.engineering_documentation_folder's value — both matched by the key-name LIKE filter
    in cross_check_settings but neither is a path to check)."""
    val = raw.strip('"') if isinstance(raw, str) else raw
    if not isinstance(val, str) or not val or val.startswith("["):
        return None
    norm = val.replace("\\", "/").strip("/")
    if not norm or " " in norm or "{" in norm or len(norm) > 80 or norm.count("/") > 6:
        return None  # not a plausible bare path — a sentence or a {template} pattern, not a folder
    last_seg = norm.rsplit("/", 1)[-1]
    if "." in last_seg and len(last_seg.split(".")[-1]) <= 5:
        norm = norm.rsplit("/", 1)[0] if "/" in norm else ""
    return norm.lower() if norm else None


def _module_setting_tables(conn: sqlite3.Connection) -> list[str]:
    """Every per-module settings table shaped like cfg_setting (key/value/use/inactive) but scoped
    to one module — cfg_prose, cfg_passage, and any future one (governance.module.config) —
    discovered live, not hardcoded, so a new module table is picked up automatically rather than
    silently missed the way cfg_prose was found to be missed live, 2026-08-28 (researcher: "I
    notice there are folders which I would have expected to have config-governed entries")."""
    tables = [r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'cfg_%'")]
    shaped = []
    for t in tables:
        if t == "cfg_setting":
            continue
        cols = {r[1] for r in conn.execute(f'PRAGMA table_info("{t}")')}
        if {"key", "value", "use", "inactive"}.issubset(cols):
            shaped.append(t)
    return shaped


def location_settings(conn: sqlite3.Connection) -> list[tuple[str, str, str]]:
    """Every (table, key, raw_value) triple, across cfg_setting AND every per-module table shaped
    like it, whose key name looks location-shaped (dir/path/folder). Shared enumeration step for
    Method B (cross_check_settings, below) and cfgquality.find_unresolvable_location_settings —
    one source of truth for "what counts as a location reference", so the two checks can't drift
    apart on which settings they even consider."""
    rows = [("cfg_setting", r["key"], r["value"]) for r in conn.execute(
        "SELECT key, value FROM cfg_setting "
        "WHERE key LIKE '%dir%' OR key LIKE '%path' OR key LIKE '%folder%'")]
    for table in _module_setting_tables(conn):
        rows += [(table, r["key"], r["value"]) for r in conn.execute(
            f'SELECT key, value FROM "{table}" '
            f"WHERE (key LIKE '%dir%' OR key LIKE '%path' OR key LIKE '%folder%') AND inactive=0")]
    return rows


def cross_check_settings(cfg) -> dict:
    """Method B. Re-derives governed_by_setting for every row from every live config-value table
    — cfg_setting AND every per-module table shaped like it (cfg_prose, cfg_passage, ... —
    config-side truth, can change with no file moving, so this can't be Method A's job. Pre-fills
    type='operations'/status='authoritative' for any row that has a governed_by_setting and no
    type/status yet (the unambiguous case — a folder some config table already names is, by
    definition, in operational system use). Returns anomalies: rows with type='operations' and no
    governed_by_setting (the invariant the researcher stated), and settings pointing at a folder
    with no folder_purpose row at all."""
    conn: sqlite3.Connection = cfg.conn
    rows = [(key, value) for _table, key, value in location_settings(conn)]
    governed: dict[str, list[str]] = {}
    for key, value in rows:
        norm = normalize_setting_value(value)
        if norm is not None:
            governed.setdefault(norm, []).append(key)

    # folder_path is stored with its actual on-disk casing; cfg_setting values are matched
    # case-insensitively (NTFS is case-preserving but case-insensitive) via this lowercase index.
    by_lower = {r["folder_path"].lower(): r["folder_path"] for r in
               conn.execute("SELECT folder_path FROM folder_purpose")}

    updated = 0
    prefilled = 0
    matched_lower: set[str] = set()
    for lower_path, keys in governed.items():
        actual_path = by_lower.get(lower_path)
        if actual_path is None:
            continue
        matched_lower.add(lower_path)
        joined = "; ".join(sorted(keys))
        row = conn.execute("SELECT governed_by_setting, type, status FROM folder_purpose "
                          "WHERE folder_path=?", (actual_path,)).fetchone()
        if row["governed_by_setting"] != joined:
            conn.execute("UPDATE folder_purpose SET governed_by_setting=? WHERE folder_path=?",
                        (joined, actual_path))
            updated += 1
        if row["type"] is None and row["status"] is None:
            conn.execute(
                "UPDATE folder_purpose SET type='operations', status='authoritative', "
                "last_reviewed_at=? WHERE folder_path=?", (_now(), actual_path))
            prefilled += 1
    conn.commit()

    anomaly_no_setting = [r["folder_path"] for r in conn.execute(
        "SELECT folder_path FROM folder_purpose WHERE type='operations' "
        "AND (governed_by_setting IS NULL OR governed_by_setting='') "
        "AND (manifest_category IS NULL OR manifest_category NOT IN ('iba','code','script'))")]
    anomaly_no_row = sorted(p for p in governed if p not in matched_lower)

    return {"checked_at": _now(), "governed_by_setting_updated": updated,
           "type_status_prefilled": prefilled,
           "anomaly_operations_without_setting": anomaly_no_setting,
           "anomaly_setting_without_folder_row": anomaly_no_row}


# ---------------------------------------------------------------------------
# Method C — table editor: hand-set type/status/usage_description
# ---------------------------------------------------------------------------

def set_purpose(cfg, folder_path: str, type_: str | None = None, status: str | None = None,
               usage_description: str | None = None) -> dict:
    conn: sqlite3.Connection = cfg.conn
    row = conn.execute("SELECT 1 FROM folder_purpose WHERE folder_path=?", (folder_path,)).fetchone()
    if not row:
        raise ValueError(f"no folder_purpose row for {folder_path!r} — run seed_from_scan first")
    valid_type = cfg.enum("folder_purpose_type")
    valid_status = cfg.enum("folder_purpose_status")
    if type_ is not None and type_ not in valid_type:
        raise ValueError(f"type must be one of {valid_type}, got {type_!r}")
    if status is not None and status not in valid_status:
        raise ValueError(f"status must be one of {valid_status}, got {status!r}")
    sets, params = [], []
    if type_ is not None:
        sets.append("type=?"); params.append(type_)
    if status is not None:
        sets.append("status=?"); params.append(status)
    if usage_description is not None:
        sets.append("usage_description=?"); params.append(usage_description)
    if not sets:
        raise ValueError("set_purpose needs at least one of type/status/usage_description")
    sets.append("last_reviewed_at=?"); params.append(_now())
    params.append(folder_path)
    conn.execute(f"UPDATE folder_purpose SET {', '.join(sets)} WHERE folder_path=?", params)
    conn.commit()
    return dict(conn.execute("SELECT * FROM folder_purpose WHERE folder_path=?",
                            (folder_path,)).fetchone())


def list_rows(cfg, type_: str | None = None, status: str | None = None,
             top_level_root: str | None = None) -> list[dict]:
    conn: sqlite3.Connection = cfg.conn
    where, params = [], []
    if type_:
        where.append("type=?"); params.append(type_)
    if status:
        where.append("status=?"); params.append(status)
    if top_level_root:
        where.append("top_level_root=?"); params.append(top_level_root)
    sql = "SELECT * FROM folder_purpose"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY folder_path"
    return [dict(r) for r in conn.execute(sql, params)]


def show(cfg, folder_path: str) -> dict | None:
    conn: sqlite3.Connection = cfg.conn
    row = conn.execute("SELECT * FROM folder_purpose WHERE folder_path=?", (folder_path,)).fetchone()
    return dict(row) if row else None


# ---------------------------------------------------------------------------
# Method D — auto-assess: fill type/status wherever determinable from the disk/config facts
# Methods A/B already gathered, only leaving genuinely ambiguous rows for a human. Researcher,
# 2026-08-28: "where the folder_purpose_type can be determined by you, you must fill and maintain
# it. the folder_purpose_status status must be assessed by you and filled, only prompting me if
# you are unsure."
# ---------------------------------------------------------------------------

_RECENT_DAYS = 90  # a folder touched more recently than this reads as actively maintained


# manifest_category values that mean "this is where SOURCE CODE lives" — genuinely operational,
# but never a write-DESTINATION, so cross_check_settings' invariant ("no folder used by the
# system without a governed_by_setting") must not expect a setting to point at one of these.
# Corrected 2026-08-28: the first version of this function put 'workflow'/'session'/'log'/
# 'patch'/'directive'/'import' in the same 'operations' bucket as these — live-checked and found
# wrong: 27 iba/ subfolders and 5 scripts/ subfolders (source code, no output path to govern)
# tripped the invariant as false anomalies the moment CrossCheck ran against them for real.
_CODE_CATEGORIES = frozenset({"iba", "code", "script"})


def _assess_type(row: dict) -> str | None:
    if row["governed_by_setting"]:
        return "operations"  # a live cfg_setting writes here — unambiguous
    path = row["folder_path"].lower()
    if path == "archive" or path.startswith("archive/") or "/archive/" in path or \
       row["manifest_currency"] in ("archived", "backup"):
        return "archive"
    cat = row["manifest_category"]
    if cat in _CODE_CATEGORIES:
        return "operations"  # source code — operational apparatus, never a write destination
    if cat in ("report", "doc", "investigation", "discovery", "export", "workflow", "session",
              "log", "patch", "directive", "import"):
        # Produced/process content: analysis output (report/doc/investigation/discovery/export)
        # and process-adjacent data (workflow/session/log/patch/directive/import) read the same
        # way here — neither is source code, and without a governing setting there's no evidence
        # either is an active system write-destination, so both default to 'results' rather than
        # a mis-implied 'operations'.
        return "results"
    return None  # cat is 'other' (or unset) — genuinely ambiguous, left for a human


def _assess_status(row: dict, type_: str | None) -> str | None:
    if row["governed_by_setting"]:
        return "authoritative"  # a live setting names it — that IS its correct, current home
    if type_ == "archive":
        return "authoritative"  # correctly filed as archive is archive's whole job
    if row["recursive_file_count"] == 0:
        return "stale"  # empty tree, nothing to be authoritative or mixed about
    if type_ is None:
        return None  # can't assess status sensibly without knowing what the folder is FOR
    if row["last_modified_direct"]:
        try:
            mtime = datetime.datetime.strptime(row["last_modified_direct"], "%Y-%m-%dT%H:%M:%SZ")
            age_days = (datetime.datetime.now(datetime.timezone.utc)
                       - mtime.replace(tzinfo=datetime.timezone.utc)).days
            if age_days <= _RECENT_DAYS:
                return "authoritative"
        except ValueError:
            pass
    # A pure container (files only in subfolders, none direct) with a clear type but no direct
    # mtime to judge recency by — read as authoritative rather than stale; it's a passthrough
    # structural folder, not itself aging content.
    if row["direct_file_count"] == 0 and row["recursive_file_count"] > 0:
        return "authoritative"
    return "stale"  # has direct content, clearly categorised, but not touched in 90+ days


_ASSESS_TYPE_VALUES = {"archive", "operations", "results"}
_ASSESS_STATUS_VALUES = {"authoritative", "stale"}  # the only two _assess_status ever returns —
# 'mixed'/'reallocate'/'deleted' are Method C's/Method A's own job, never Method D's


def auto_assess(cfg) -> dict:
    """Method D. Fills type/status for every row still missing either, using only Methods A/B's
    own gathered facts (governed_by_setting, manifest_category/currency, file counts, mtime) —
    never guesses at 'mixed'/'reallocate' (those need real content judgement, not metadata) or at
    a category-less ('other') folder's type. usage_description and last_reviewed_at are left for
    a human via Method C — this only fills the two structured fields that ARE determinable.

    Validates its own literal vocabulary against the live cfg_enum before writing anything —
    escalation #977's actual gap, found fixing it: `_assess_type`/`_assess_status`'s hardcoded
    `return` strings were never checked against `cfg.enum()` at all (unlike `set_purpose()`, which
    does), so a drifted or mistyped literal here would have written silently. Fails loudly instead
    (raises), once per call, not per row — cheaper and catches the same class of bug
    `find_folderpurpose_ps_validateset_drift` now catches for the PS front door's own copy.
    Returns {"assessed": N, "left_uncertain": [folder_path, ...]}."""
    conn: sqlite3.Connection = cfg.conn
    live_type = set(cfg.enum("folder_purpose_type"))
    live_status = set(cfg.enum("folder_purpose_status"))
    if not _ASSESS_TYPE_VALUES <= live_type:
        raise ValueError(f"auto_assess's own type vocabulary {_ASSESS_TYPE_VALUES} is not a "
                        f"subset of live cfg_enum folder_purpose_type {live_type} — fix "
                        f"_assess_type before running")
    if not _ASSESS_STATUS_VALUES <= live_status:
        raise ValueError(f"auto_assess's own status vocabulary {_ASSESS_STATUS_VALUES} is not a "
                        f"subset of live cfg_enum folder_purpose_status {live_status} — fix "
                        f"_assess_status before running")

    rows = [dict(r) for r in conn.execute(
        "SELECT * FROM folder_purpose WHERE type IS NULL OR status IS NULL")]
    assessed = 0
    uncertain = []
    for row in rows:
        type_ = row["type"] or _assess_type(row)
        status = row["status"] or _assess_status(row, type_)
        if type_ is None and status is None:
            uncertain.append(row["folder_path"])
            continue
        sets, params = [], []
        if type_ and not row["type"]:
            sets.append("type=?"); params.append(type_)
        if status and not row["status"]:
            sets.append("status=?"); params.append(status)
        if not sets:
            uncertain.append(row["folder_path"])
            continue
        sets.append("last_reviewed_at=?"); params.append(_now())
        params.append(row["folder_path"])
        conn.execute(f"UPDATE folder_purpose SET {', '.join(sets)} WHERE folder_path=?", params)
        assessed += 1
        if type_ is None or status is None:
            uncertain.append(row["folder_path"])  # partially filled, still needs the other field
    conn.commit()
    return {"assessed": assessed, "left_uncertain": sorted(set(uncertain))}
