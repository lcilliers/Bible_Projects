"""escalationcontext.py -- what every open escalation points to (#2173 P1): the files linked in any
open escalation are read, at their latest version.

For every OPEN escalation (cfg_enum escalation_state_open: raised, in-progress, re-assigned --
parked items are read when they are taken up; threads are audited by threadaudit.py), it collects
every file path named in any version's comment, tried, short_description, context or resolution,
resolves each to the newest live version of that file (same base name, highest -vN, outside an
archive folder) and writes one report section per escalation. Findings, by escalation:

  * missing  -- no live version of the named file exists anywhere (the escalation points at nothing)
  * bare     -- a bare filename with no folder (cfg_escalation rule 7 full_path_file_references);
                resolved where the name is unique, still reported so the reference gets fixed

A path that names an older or archived version is resolved to the current one and said so (that is
information for the reader, not a finding). Read-only.
"""

from __future__ import annotations

import datetime
import pathlib
import re

from . import escalation as esc, reportkit

_FIELDS = ("short_description", "comment", "tried", "context", "resolution")
_VER_RE = re.compile(r"^(?P<base>.+?)-v(?P<n>\d+)(?:-(?P<date>\d{8}))?$")
_SKIP_DIRS = {".git", "archive", "node_modules", "__pycache__", "backups", ".claude", ".venv", "venv"}


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _repo_root() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parents[3]


class _Names:
    """One walk of the repo (archive folders excluded): file name -> repo-relative paths."""

    def __init__(self, root: pathlib.Path):
        self.root = root
        self.by_name: dict[str, list[str]] = {}
        for p in self._walk(root):
            self.by_name.setdefault(p.name.lower(), []).append(p.relative_to(root).as_posix())

    def _walk(self, d: pathlib.Path):
        try:
            entries = list(d.iterdir())
        except OSError:
            return
        for e in entries:
            if e.is_dir():
                if e.name.lower() not in _SKIP_DIRS:
                    yield from self._walk(e)
            elif e.is_file():
                yield e


def _split_version(stem: str) -> tuple[str, int | None]:
    m = _VER_RE.match(stem)
    return (m.group("base"), int(m.group("n"))) if m else (stem, None)


def _latest_in(folder: pathlib.Path, base: str, suffix: str) -> pathlib.Path | None:
    """Newest -vN of `base` in `folder` (not its archive), or the unversioned file itself."""
    if not folder.is_dir():
        return None
    best, best_n = None, -1
    for f in folder.iterdir():
        if not f.is_file() or f.suffix.lower() != suffix.lower():
            continue
        b, n = _split_version(f.stem)
        if b.lower() != base.lower():
            continue
        n = n if n is not None else 0
        if n > best_n:
            best, best_n = f, n
    return best


def extract_paths(text: str, exts: list[str]) -> list[str]:
    """Every file reference in free text: a run of path characters ending in a known extension.
    Paths may hold spaces (`_analytics/Clusters/M07 - shame-confusion/...`), so a candidate keeps
    its leading words and resolve() trims them until the path exists."""
    if not text:
        return []
    ext_alt = "|".join(re.escape(e.lstrip(".")) for e in exts)
    rx = re.compile(r"(?P<p>[A-Za-z]:[\\/][^`'\"*|<>;\n]*?\.(?:" + ext_alt + r")"
                    r"|[^\s`'\"*|<>;(),\[\]]*(?:[\\/][^`'\"*|<>;\n\\/]*?)*\.(?:" + ext_alt + r"))"
                    r"(?![A-Za-z0-9])", re.IGNORECASE)
    out = []
    for m in rx.finditer(text):
        p = m.group("p").strip().strip(".,:")
        if p.lower().startswith(("http://", "https://")) or len(p) < 4:
            continue
        out.append(p)
    return out


def resolve(raw: str, root: pathlib.Path, names: _Names) -> dict:
    """{'named', 'resolved', 'status', 'note'} for one raw reference.
    status: current | newer | archived | bare | missing."""
    p = raw.replace("\\", "/")
    rp = str(root).replace("\\", "/").rstrip("/") + "/"
    if p.lower().startswith(rp.lower()):
        p = p[len(rp):]
    while p.startswith("./"):
        p = p[2:]
    words = p.split(" ")
    cands = [" ".join(words[i:]) for i in range(len(words))]
    bare = "/" not in p
    for cand in cands:
        cpath = root / cand
        parts = pathlib.PurePosixPath(cand).parts
        folder = cpath.parent
        archived = "archive" in [x.lower() for x in parts[:-1]]
        if archived:   # the live folder is the one above the archive segment
            idx = [x.lower() for x in parts[:-1]].index("archive")
            folder = root.joinpath(*parts[:idx]) if idx else root
        base, n = _split_version(cpath.stem)
        latest = _latest_in(folder, base, cpath.suffix) if not bare else None
        if latest is None and cpath.is_file() and not archived:
            latest = cpath
        if latest is not None:
            rel = latest.relative_to(root).as_posix()
            if archived:
                return dict(named=raw, resolved=rel, status="archived",
                            note="named an archived copy; the live file is used")
            if rel.lower() != cand.lower():
                return dict(named=raw, resolved=rel, status="newer",
                            note="a newer version than the one named exists")
            return dict(named=raw, resolved=rel, status="current", note="")
    # by file name anywhere (a bare name, or a path whose folder moved)
    name = pathlib.PurePosixPath(p).name
    base, _ = _split_version(pathlib.PurePosixPath(name).stem)
    suffix = pathlib.PurePosixPath(name).suffix.lower()
    hits = names.by_name.get(name.lower(), [])
    if not hits:   # any version of the same base name
        for nm, paths in names.by_name.items():
            b, _ = _split_version(pathlib.PurePosixPath(nm).stem)
            if b == base.lower() and nm.endswith(suffix):
                hits.extend(paths)
    if hits:
        folders = {pathlib.PurePosixPath(h).parent.as_posix() for h in hits}
        if len(folders) == 1:
            folder = root / folders.pop()
            latest = _latest_in(folder, base, suffix) or root / hits[0]
            rel = latest.relative_to(root).as_posix()
            if bare:
                return dict(named=raw, resolved=rel, status="bare",
                            note="bare filename (rule 7); resolved by its unique name")
            return dict(named=raw, resolved=rel, status="newer",
                        note="the named folder does not hold it; found by name")
        return dict(named=raw, resolved=None, status="bare" if bare else "missing",
                    note=f"name found in {len(folders)} folders: "
                         + "; ".join(sorted(folders)[:4]))
    return dict(named=raw, resolved=None, status="missing", note="no live version exists")


def collect(cfg, db, eid: int | None = None) -> list[dict]:
    """[{escalation, refs: [{named, field, version, resolved, status, note}], findings}] for every
    open escalation, or for escalation `eid` alone in any state (read when it is taken up, #2209)."""
    root = _repo_root()
    exts = cfg.required_setting("escalation.context_file_extensions")
    names = _Names(root)
    open_s = esc.state_group(db, "open")
    ph = ",".join("?" * len(open_s))
    out = []
    rows = (db.rows("SELECT * FROM escalation WHERE id=?", (eid,)) if eid is not None else
            db.rows(f"SELECT * FROM escalation WHERE state IN ({ph}) AND type != 'thread' "
                    f"ORDER BY id", open_s))
    for e in rows:
        seen: dict[str, dict] = {}
        for h in db.rows("SELECT * FROM escalation_history WHERE escalation_id=? ORDER BY version",
                         (e["id"],)):
            for f in _FIELDS:
                for raw in extract_paths(h[f] or "", exts):
                    r = resolve(raw, root, names)
                    key = (r["resolved"] or r["named"]).lower()
                    if key in seen:
                        seen[key]["where"].append(f"{f} v{h['version']}")
                        continue
                    r["where"] = [f"{f} v{h['version']}"]
                    seen[key] = r
        refs = list(seen.values())
        for r in refs:
            if r["resolved"]:
                f = root / r["resolved"]
                st = f.stat()
                r["size"] = st.st_size
                r["modified"] = datetime.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M")
        findings = [r for r in refs if r["status"] in ("missing", "bare")]
        out.append(dict(escalation=e, refs=refs, findings=findings))
    return out


def write_report(cfg, db, path: pathlib.Path, eid: int | None = None
                 ) -> tuple[pathlib.Path, list[dict]]:
    items = collect(cfg, db, eid)
    n_find = sum(len(i["findings"]) for i in items)
    L = [f"> Generated {_now()} by `Escalation.ps1 -Action Context` (#2173 P1). Every file named "
         f"in any field of any version of each open escalation (raised, in-progress, "
         f"re-assigned), resolved to its latest live version. **Read the resolved file**, not the "
         f"one named. Findings: `missing` = no live version exists (the escalation points at "
         f"nothing); `bare` = a bare filename (cfg_escalation rule 7).", "",
         f"- {'escalation #' + str(eid) if eid is not None else 'open escalations: ' + str(len(items))}; "
         f"findings: **{n_find}**", ""]
    sections: dict[str, list[str]] = {"items": []}
    body = sections["items"]
    for i in items:
        e = i["escalation"]
        body += [f"### #{e['id']} -- {e['short_description']}", "",
                 f"state `{e['state']}`, next action `{e['next_action']}`, assigned "
                 f"{e['next_action_assigned_to']}", ""]
        if not i["refs"]:
            body += ["_names no file (nothing to read)._", ""]
            continue
        body += ["| named | where named | read this (latest live) | status | size / changed |",
                 "|---|---|---|---|---|"]
        for r in i["refs"]:
            size = f"{r.get('size', '')} B, {r.get('modified', '')}" if r["resolved"] else "--"
            status = r["status"] if r["status"] not in ("missing", "bare") else f"**{r['status']}**"
            note = f" -- {r['note']}" if r["note"] else ""
            body.append(f"| `{r['named']}` | {', '.join(r['where'][:4])}"
                        f"{' …' if len(r['where']) > 4 else ''} | "
                        f"{'`' + r['resolved'] + '`' if r['resolved'] else '--'} | {status}{note} | "
                        f"{size} |")
        body.append("")
    L2 = reportkit.render_scaffold(db.conn, "escalation.context", sections, intro=L)
    out = reportkit.write_report(db.conn, "escalation.context", path, L2)
    return out, items
