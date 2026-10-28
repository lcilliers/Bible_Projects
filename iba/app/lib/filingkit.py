"""filingkit.py — the project-wide filing utility: naming-shape, same-day `-v{n}` versioning, and
archive-before-overwrite, for any writer (#863/#971/#992). Implements the `filing` behaviour class
rules (`naming-shape`, `snapshot-vs-living-document`, `archiving-trigger`), so every report/output
writer calls one function instead of imitating the shape. `reportkit.oneoff_path()` delegates here
for `governance.oneoff_*`-configured callers; `versioned_path()` serves a caller with its own
directory, naming and archive dir.
"""

from __future__ import annotations

import datetime
import pathlib
import re


def cluster_folder_name(conn, cluster_code: str) -> str:
    """The folder name of a cluster under _analytics/Clusters by cfg_setting report.cluster_folder_name_rule (the machine form of
    report.cluster_folder_naming_convention): the pattern {cluster_code} - {slug} of the cluster's short_name, lowercased, & and
    other punctuation dropped, spaces as single hyphens (M21 - fasting-piety). Every output relating to a cluster is filed in that
    folder (#2328)."""
    from .cfg import Cfg
    rule = Cfg.on(conn).required_setting("report.cluster_folder_name_rule")
    row = conn.execute("SELECT short_name FROM cluster WHERE cluster_code=? AND coalesce(deleted,0)=0", (cluster_code,)).fetchone()
    if row is None:
        raise ValueError(f"cluster {cluster_code!r} is not a live cluster: no folder name")
    name = row[0] or ""
    if rule["ampersand_to_space"]:
        name = name.replace("&", " ")
    if rule["lowercase"]:
        name = name.lower()
    if rule["drop_other_punctuation"]:
        name = re.sub(r"[^A-Za-z0-9\s-]", "", name)
    slug = re.sub(r"\s+", rule["word_separator"], name.strip())
    return rule["pattern"].replace("{cluster_code}", cluster_code).replace("{slug}", slug)


def versioned_path(cfg, topic: str, out_dir: str | pathlib.Path | None = None,
                   ext: str | None = None, naming_pattern: str | None = None,
                   archive_dir: str | None = None) -> pathlib.Path:
    """The path for a versioned, archived write. `cfg` is a `lib.cfg.Cfg` (or anything with
    `.setting(key, default)`) — only used for the `governance.oneoff_*` FALLBACK defaults below,
    never required to be meaningful for a caller that passes its own `out_dir`/`naming_pattern`/
    `archive_dir` explicitly.

    Same-day version bump on collision (`filing.naming-shape`/`filing.snapshot-vs-living-document`):
    a second call for the same topic on the same day gets `-v2`, a third `-v3`, and so on.
    Archive-before-write (`filing.archiving-trigger`): whatever is currently live for this exact
    topic-day is moved into `archive_dir` first — the live folder holds exactly the newest version,
    the full lineage is in `archive_dir`, nothing silently lost or overwritten.

    Every parameter beyond `cfg`/`topic` is optional and falls back to the same
    `governance.oneoff_*` settings `reportkit.oneoff_path()` already used — so `oneoff_path(cfg,
    topic, ext)` is now exactly `versioned_path(cfg, topic, ext=ext)`, no behaviour change for any
    existing caller."""
    out_dir = pathlib.Path(out_dir if out_dir is not None else
                           cfg.required_setting("governance.oneoff_report_dir"))
    pattern = naming_pattern or cfg.required_setting("governance.oneoff_report_naming_pattern")
    fmt = ext or cfg.required_setting("governance.oneoff_report_format")
    adir_name = archive_dir if archive_dir is not None else \
        cfg.required_setting("governance.oneoff_report_archive_dir")
    slug = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")
    stamp = datetime.datetime.now().strftime("%Y%m%d")
    name = pattern.format(topic=slug, YYYYMMDD=stamp, format=fmt)
    stem, _, extension = name.rpartition(".")

    live_matches = [out_dir / name] if (out_dir / name).exists() else []
    if out_dir.exists():
        live_matches += sorted(out_dir.glob(f"{stem}-v*.{extension}"))
    if not live_matches:
        return out_dir / name

    adir = out_dir / adir_name
    adir.mkdir(parents=True, exist_ok=True)
    for f in live_matches:
        f.replace(adir / f.name)

    rx = re.compile(rf"^{re.escape(stem)}-v(\d+)\.{re.escape(extension)}$")
    candidates = (list(out_dir.glob(f"{stem}-v*.{extension}")) if out_dir.exists() else []) + \
                list(adir.glob(f"{stem}-v*.{extension}"))
    versions = [int(m.group(1)) for m in (rx.match(f.name) for f in candidates) if m]
    n = max(versions, default=1) + 1
    return out_dir / f"{stem}-v{n}.{extension}"
