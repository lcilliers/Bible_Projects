"""taggingguidance.py — the one shared source of `ib_observation.tag` definitions for every
LLM-calling generator stage (#1836, #1770). `cfg_column.use` for `ib_observation.tag` says the enum is
shared across all stages; this module is that shared definition set, so every active tag reaches the
model with a real definition.

Definitions are sourced, in priority order, from (1) the tag taxonomy consolidation doc
(`iba/docs/1706-tag-taxonomy-consolidation-v1-20260917.md`), (2) `cfg_method_rule` rows defining a
tag's meaning (`no-human-context` #97, `data-error` #98, `needs_adjacent_verse_context` #74/#104),
(3) how a tag is used live, where neither exists. `alternative-meaning` (more than one candidate
reading where the data supports more than one) and `surface-gloss-divergence` (span.surface vs
stepGloss, a form-level fact) are distinct concepts, and their definitions keep them apart.

**Stage scoping** (`STAGE_TAGS`): `verse-grouping` and `difference-inference` compare a strong's
occurrences across several verses, so they are not offered to `verse-reading` (Stage 1), which sees
one verse at a time. A plain Python allowlist.
"""

from __future__ import annotations

TAG_GUIDANCE: dict[str, str] = {
    "qualifier-for-term": (
        "the word functions as a MODIFIER (manner, intensifier, or other state/measure/intensity "
        "enhancer) of another word's action or quality, rather than naming a disposition/operation/"
        "quality in its own right -- e.g. an adverb qualifying HOW an operation is performed, or an "
        "adjective qualifying another M-code noun (\"godly\" qualifying \"grief\")."),
    "no-impact": (
        "the occurrence's surface form/stepGloss carries no distinguishing nuance beyond the "
        "term's base sense -- a real 'no divergence' finding, not an absence of an answer. "
        "Contrast `alternative-meaning` (a real divergence IS found) and `surface-gloss-divergence` "
        "(the surface FORM itself, not just the sense, diverges from the dictionary gloss)."),
    "not-related-to-meaningful-word": (
        "the sub-question's target item (a contrast, a related word-form, a co-occurring item the "
        "question asks you to identify) genuinely does not exist or apply for this term/verse -- a "
        "real negative finding, not a shrug."),
    "sole-mcode-in-verse": (
        "no other M-code characteristic co-occurs in this verse at all -- distinct from "
        "`no-direct-connection`, which means other M-codes ARE present but unrelated to this one."),
    "tightly-related": (
        "this term's own role connects SUBSTANTIVELY to another M-code term present in the same "
        "scope -- a real causal/enabling/response/tension link, or the two share the same acting "
        "party -- not just topical co-presence in the same list or catalogue."),
    "no-direct-connection": (
        "other M-code term(s) ARE present in this scope, but this term's own role does not "
        "meaningfully connect to them (no causal link, no shared party, no real interaction) -- "
        "distinct from `sole-mcode-in-verse`, where nothing else is present to connect to at all."),
    "cluster-pole-negative": (
        "this term occupies the negative/negligent pole of a dual-natured cluster (e.g. idleness "
        "within a sloth-vs-diligence cluster)."),
    "cluster-pole-positive": (
        "this term occupies the positive/virtuous pole of a dual-natured cluster (e.g. diligence/"
        "zeal within a sloth-vs-diligence cluster)."),
    "attested-pre-nt": (
        "the term is attested in classical/pre-NT Greek or Hebrew usage, not coined in the NT "
        "period."),
    "nt-coinage": (
        "the term (or this specific sense of it) has no attestation before the NT -- a NT-period "
        "coinage or semantic innovation."),
    "alternative-meaning": (
        "this SPECIFIC occurrence genuinely supports MORE THAN ONE plausible reading/sense, and "
        "the data does not clearly settle which -- real ambiguity, not just a divergence from the "
        "usual sense (that's `surface-gloss-divergence` when it's the FORM, or a plain substantive "
        "answer when the sense is clear but simply different from elsewhere). State both/all "
        "candidate readings in `obs_text`, not just one."),
    "surface-gloss-divergence": (
        "this occurrence's actual surface form (`span.surface`, the inflected text as it appears) "
        "diverges from its `stepGloss` dictionary-standard rendering in a way worth noting -- a "
        "form-level fact (e.g. an idiomatic rendering, a metaphorical extension the standard gloss "
        "doesn't capture), not a claim of multiple valid readings (`alternative-meaning`)."),
    "no-human-context": (
        "this strong is exclusively a homonym or proper name with no meaningful context for a "
        "human reader to analyse -- earmark it as such and stop; do not force an analysis where "
        "none is genuinely available (cfg_method_rule 'homonym-no-context-earmarked-and-left')."),
    "data-error": (
        "a data-quality issue noticed while reading (wrong cluster/subgroup membership, a broken "
        "span/verse link, a corrupted meaning source) -- flag it here, in its own section; never "
        "chase it down or fix it as part of this task (cfg_method_rule 'data-errors-flagged-"
        "separately')."),
    "verse-grouping": (
        "several of THIS strong's own occurrences, across different verses, share one genuinely "
        "alike reading -- group them under one finding rather than repeating the same point per "
        "verse. Requires visibility across a strong's full occurrence set; not meaningful at a "
        "single-verse grain."),
    "difference-inference": (
        "a specific inference or distinction drawn from comparing THIS strong's own occurrences "
        "against EACH OTHER (morph-driven distinctions included -- e.g. whether a stem/voice "
        "variation across occurrences is meaning-relevant). Requires visibility across a strong's "
        "full occurrence set; not meaningful at a single-verse grain."),
    "could-not-resolve": (
        "a genuine 'couldn't resolve' case -- state in `obs_text` what signal suggests it should "
        "be resolvable with further analysis, never a bare flag with no reason."),
    "needs_adjacent_verse_context": (
        "this verse's own content is insufficient and an adjacent/surrounding verse would help -- "
        "state explicitly in `obs_text` what's outstanding and what the follow-up cross-check needs "
        "to establish. Resolution happens in a later analytic pass, never fetched ad hoc here."),
    "elevation-candidate": (
        "this T2/T3-tagged (non-M-code) word's role in THIS verse suggests it names a distinct "
        "inner-being characteristic in its own right, not just a supporting role -- state the "
        "reason in `obs_text` (M0.8.1 only; escalation #1836). A later, separate process reviews "
        "elevation candidates for actual cluster promotion -- this tag only surfaces the "
        "candidate, it does not itself change any cluster/role assignment."),
    "answered-no-flag": (
        "a genuinely plain, substantive answer that matches none of the other tags and has nothing "
        "else worth categorising (e.g. a straightforward root-meaning or primary-term "
        "identification) -- a LAST RESORT, not a default. Check every observation against the "
        "other tags above before reaching for this one."),
}

# #1770's audit: verse-grouping/difference-inference are inherently cross-occurrence (comparing a
# strong's OWN occurrences against each other across MULTIPLE verses) -- meaningless at Stage 1's
# single-verse grain. Every other active tag applies wherever its own condition can arise,
# regardless of stage (matches cfg_column.use's own stated design intent for the enum as a whole).
_CROSS_OCCURRENCE_ONLY = {"verse-grouping", "difference-inference"}

STAGE_TAGS: dict[str, set[str]] = {
    "verse-reading": set(TAG_GUIDANCE) - _CROSS_OCCURRENCE_ONLY,
    "char-subgroup": set(TAG_GUIDANCE),
    "char-reading": set(TAG_GUIDANCE),
    "char-answers": set(TAG_GUIDANCE),
}


def tags_for_stage(stage: str, tag_values: list[str]) -> list[str]:
    """Intersects the live `cfg_enum` list (still the source of truth for what's ACTIVE) with this
    stage's own applicability allowlist -- never invents a tag `cfg_enum` doesn't have, only narrows
    which of the active ones this stage's prompt actually offers."""
    allowed = STAGE_TAGS.get(stage, set(TAG_GUIDANCE))
    return [t for t in tag_values if t in allowed]


def guidance_block(tag_values: list[str]) -> str:
    """Renders the standard '`tag` is a categorisation value, not just a peculiarity flag' framing plus
    one definition line per tag in `tag_values` that has a definition. A tag without one is omitted,
    never crashing the prompt build."""
    lines = "\n".join(f"  - {t}: {TAG_GUIDANCE[t]}" for t in tag_values if t in TAG_GUIDANCE)
    return (
        f"`tag` is a categorisation value, not just a peculiarity flag -- it must let someone "
        f"later FILTER and find trends across the whole corpus without re-reading every obs_text. "
        f"Prefer the most specific tag that actually matches (check every observation against this "
        f"list before reaching for a generic one):\n{lines}\n"
        f"NEVER use the literal string `none` -- it is not a registered tag and will be rejected; "
        f"if there is truly nothing to report, pick the specific tag above that names WHY (most "
        f"often `not-related-to-meaningful-word` or `no-impact`), never a bare negation.")
