"""taggingguidance.py — the one shared source of `ib_observation.tag` definitions for every
LLM-calling generator stage (#1836, #1770). `cfg_column.use` for `ib_observation.tag` says the enum is
shared across all stages; this module renders that shared definition set, so every active tag reaches
the model with a real definition.

The definitions are `cfg_setting ib_observation.tag_guidance` ({tag: definition}); which tags a stage
may not offer is `cfg_setting ib_observation.tag_stage_excluded` ({stage: [tag, ...]}) (#2207).
`verse-grouping` and `difference-inference` compare a strong's occurrences across several verses, so
they are not offered to `verse-reading` (Stage 1), which sees one verse at a time.
`alternative-meaning` and `surface-gloss-divergence` are distinct concepts, and their definitions keep
them apart.
"""

from __future__ import annotations

from .cfg import Cfg


def tag_guidance(cfg: Cfg) -> dict[str, str]:
    return cfg.required_setting("ib_observation.tag_guidance")


def tags_for_stage(cfg: Cfg, stage: str, tag_values: list[str]) -> list[str]:
    """Intersects the live `cfg_enum` list (still the source of truth for what's ACTIVE) with the tags
    that have a definition, less this stage's exclusions -- never invents a tag `cfg_enum` doesn't
    have, only narrows which of the active ones this stage's prompt actually offers."""
    excluded = set(cfg.required_setting("ib_observation.tag_stage_excluded").get(stage, []))
    allowed = set(tag_guidance(cfg)) - excluded
    return [t for t in tag_values if t in allowed]


def guidance_block(cfg: Cfg, tag_values: list[str]) -> str:
    """Renders the standard '`tag` is a categorisation value, not just a peculiarity flag' framing plus
    one definition line per tag in `tag_values` that has a definition. A tag without one is omitted,
    never crashing the prompt build."""
    guidance = tag_guidance(cfg)
    lines = "\n".join(f"  - {t}: {guidance[t]}" for t in tag_values if t in guidance)
    return (
        f"`tag` is a categorisation value, not just a peculiarity flag -- it must let someone "
        f"later FILTER and find trends across the whole corpus without re-reading every obs_text. "
        f"Prefer the most specific tag that actually matches (check every observation against this "
        f"list before reaching for a generic one):\n{lines}\n"
        f"NEVER use the literal string `none` -- it is not a registered tag and will be rejected; "
        f"if there is truly nothing to report, pick the specific tag above that names WHY (most "
        f"often `not-related-to-meaningful-word` or `no-impact`), never a bare negation.")
