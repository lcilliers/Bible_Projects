"""filingkit.py — the project-wide filing utility: naming-shape, same-day `-v{n}` versioning, and
archive-before-overwrite, for ANY writer, not just `iba/app/reports/`.

Escalation #863/#971/#992. `iba/docs/file-naming-and-location-governance-plan-v1-20260826.md` §2
scoped this: `reportkit.oneoff_path()`'s own logic (same-day `-v{n}` bump, archive-before-write,
collision handling) is already a correct implementation of the `filing` behaviour class's rules
(`naming-shape`, `snapshot-vs-living-document`, `archiving-trigger` — `cfg_behaviour_rule`, class
`filing`) — this generalises it rather than inventing new machinery, so every future report/output
writer project-wide (IBA or main-project side) has a single function to call instead of hand-
imitating the shape. `reportkit.oneoff_path()` now delegates here instead of duplicating the logic
— one implementation, two entry points (the original for backward compatibility with every existing
`governance.oneoff_*`-configured caller, this one for a caller that wants its own directory/naming/
archive-dir instead of the `iba/app/reports/`-side defaults).
"""

from __future__ import annotations

import datetime
import pathlib
import re


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
                           cfg.setting("governance.oneoff_report_dir", "iba/app/reports/"))
    pattern = naming_pattern or cfg.setting("governance.oneoff_report_naming_pattern",
                                            "{topic}-{YYYYMMDD}.{format}")
    fmt = ext or cfg.setting("governance.oneoff_report_format", "md")
    adir_name = archive_dir if archive_dir is not None else \
        cfg.setting("governance.oneoff_report_archive_dir", "archive")
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
