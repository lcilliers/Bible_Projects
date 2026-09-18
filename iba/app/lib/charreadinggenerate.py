"""charreadinggenerate.py — the LLM-calling half of `cluster.reading` (the `char-reading` stage,
process (c), escalation #1706 Phase F stage 3, built 2026-09-18). Sibling to `subgroupgenerate.py`/
`versereadinggenerate.py`, same separation: this module only assembles the payload and calls the
API; `recordingpass.py` is the only thing that ever writes `ib_observation`/`ib_node` (single-writer
principle, checklist rule 0.1).

**Scope grain: per-subgroup, never the whole cluster** (`#1682` §2 rule 1 / checklist §2 rule 1) —
one LLM call per `cluster_subgroup`, given that subgroup's own member strongs. Genuinely different
work from Stage 1 (`verse-reading`, per-verse across a cluster) and Stage 2 (`char-subgroup`,
whole-cluster placement): this stage reads EVERY occurrence of every subgroup member strong across
the whole corpus (checklist §2 rule 3, "no sampling"), not just the verses a single batch happens to
cover, so it can synergise the similar and different contextual meaning of the subgroup's OWN
member strongs against each other — the comparison Stage 1's single-verse view structurally cannot
make and Stage 2's placement-only pass does not attempt.

**What this stage does NOT do, to avoid duplicating Stage 1's own ground:** Stage 1 already answers
`M0.1`/`M0.5` (including the `M0.5.11` per-occurrence surface/gloss divergence question) for every
occurrence, per verse. This stage does not re-ask those; it is given Stage 1's own observations as
grounding and focuses on what only a subgroup-grain view adds — comparing member strongs against
EACH OTHER (tags `tightly-related`/`no-direct-connection`, already registered), grouping genuinely
similar verses across a strong's own occurrence set (`verse-grouping`), and per-strong completeness
(checklist §2 rule 10) verified by CODE after the write, not trusted from an LLM self-report (an
improvement on the original 2026-09-11 spec's LLM-self-reported `strong_checks`, consistent with the
single-writer/never-trust-the-model discipline `recordingpass.py` already established for
`question_code`/`tag`/`obs_text`).

**Role-driven-walk — deliberately NOT structurally forced.** Checklist §2 rule 14 named this a hard
gate; that was superseded 2026-09-17 (recorded at `#1706` v32, confirmed closed 2026-09-18 against
three stale docs) — the researcher's actual resolution is question-driven catalogue expansion
(`M0.6.5`), not an imposed mechanical structure. No forced-walk logic is built here, matching how
Stage 1/2 were also built without it.
"""

from __future__ import annotations

import json
import re

from .narrativegenerate import ApiKeyMissing, ApiCallFailed  # noqa: F401 -- re-exported
from .lexicalenrichgenerate import call_api, log_usage  # reuse, don't duplicate
from .lexicalenrichgenerate import CostCapExceeded, BadModelResponse  # noqa: F401 -- re-exported
from .versereadinggenerate import _meaning_sources  # reuse, don't duplicate


_JSON_FENCE_RE = re.compile(r"```(?:json)?\s*(\{.*\})\s*```", re.DOTALL)

_MAX_OCCURRENCES_PER_STRONG = 60  # checklist §2 rule 3 says "no sampling" -- never a silent
# truncation. A strong past this cap is SPLIT into multiple reading calls by
# _partition_occurrences_by_surface (escalation #1761, researcher's own rule, 2026-09-18: "if we
# have a strong that have more than 100 occurrences of the same SURFACE and no multi cluster
# occurance, then it can be capped. if the strong has different SURFACEs for the verses then each
# SURFACE instance can be batched separately" -- H3034 checked live, 114 occurrences across 23
# distinct surfaces, no single surface >60, so it needs splitting, not a raised cap), never a
# refusal and never a drop.


class MultipleOverCapStrongs(Exception):
    """More than one member strong of the same subgroup exceeds the cap simultaneously -- not yet
    designed (the split-by-surface mechanism assumes exactly one strong needs partitioning, with
    every other member strong's full profile riding along unpartitioned in every resulting batch).
    Raised rather than guessing a packing order across two independently-oversized strongs."""


def _partition_occurrences_by_surface(occurrences: list[dict], cap: int) -> list[list[dict]]:
    """Groups occurrences by their own `surface` value, then greedily first-fits whole surface-
    groups into partitions each <= cap occurrences -- NEVER splits one surface's own occurrences
    across two partitions (the researcher's own rule: 'each SURFACE instance can be batched
    separately'). Groups are considered largest-first so the partition count stays close to
    minimal, rather than literally one partition per distinct surface string (most subgroups have
    several surfaces with only 1-2 occurrences each -- forcing those into their own call each would
    be wasteful and was never what the rule asked for). A single surface whose own count exceeds
    the cap gets an oversized partition of its own (still not sampled -- surfaced as an unusually
    large single-surface group rather than silently capped)."""
    groups: dict[str, list[dict]] = {}
    for occ in occurrences:
        groups.setdefault(occ["surface"], []).append(occ)
    ordered = sorted(groups.values(), key=len, reverse=True)

    partitions: list[list[dict]] = []
    for group in ordered:
        for p in partitions:
            if len(p) + len(group) <= cap:
                p.extend(group)
                break
        else:
            partitions.append(list(group))
    return partitions


def parse_response(text: str) -> dict:
    """This stage's own shape ({"observations": [...]}) -- same as Stage 1's, no `strong_checks`
    key expected from the model: completeness is computed by code after the write (see module
    docstring), not self-reported."""
    candidate = text.strip()
    m = _JSON_FENCE_RE.search(candidate)
    if m:
        candidate = m.group(1)
    try:
        parsed = json.loads(candidate)
    except json.JSONDecodeError as e:
        raise BadModelResponse(f"model reply is not valid JSON: {e} -- first 300 chars: {text[:300]!r}")
    if "observations" not in parsed:
        raise BadModelResponse(f"model reply has no 'observations' key: {list(parsed.keys())}")
    return parsed


def _full_occurrences(conn, strong: str) -> list[dict]:
    """Every occurrence of this strong, corpus-wide, NOT deduplicated by verse (checklist §2 rule
    3) -- the same span-level grain #1682's original process (c) spec required, confirmed live
    necessary there (some strongs occur twice in the same verse)."""
    rows = conn.execute(
        "SELECT v.osisId AS verse, v.text AS verse_text, vl.surface, vl.morph_code "
        "FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id "
        "WHERE vl.strong=? AND vl.deleted=0 AND v.deleted=0 ORDER BY v.id, vl.position",
        (strong,)).fetchall()
    return [{"verse": r["verse"], "verse_text": r["verse_text"], "surface": r["surface"],
            "morph_code": r["morph_code"]} for r in rows]


def _strong_reading_profile(conn, strong: str) -> dict:
    row = conn.execute(
        "SELECT stepGloss, stepTransliteration FROM strong WHERE strongNumber=?", (strong,)
    ).fetchone()
    verse_reading_obs = [
        {"question_code": r["question_code"], "tag": r["tag"], "obs_text": r["obs_text"]}
        for r in conn.execute(
            "SELECT question_code, tag, obs_text FROM ib_observation "
            "WHERE strong=? AND stage='verse-reading' ORDER BY id", (strong,))]
    subgroup_obs = [
        {"tag": r["tag"], "obs_text": r["obs_text"]}
        for r in conn.execute(
            "SELECT tag, obs_text FROM ib_observation "
            "WHERE strong=? AND stage='char-subgroup' ORDER BY id", (strong,))]
    prior_reading_obs = [
        {"question_code": r["question_code"], "tag": r["tag"], "obs_text": r["obs_text"]}
        for r in conn.execute(
            "SELECT question_code, tag, obs_text FROM ib_observation "
            "WHERE strong=? AND stage='char-reading' ORDER BY id", (strong,))]
    return {
        "gloss": row["stepGloss"] if row else None,
        "transliteration": row["stepTransliteration"] if row else None,
        "occurrences": _full_occurrences(conn, strong),
        "meaning_sources": _meaning_sources(conn, strong),
        "verse_reading_observations": verse_reading_obs,
        "char_subgroup_observations": subgroup_obs,
        "prior_char_reading_observations": prior_reading_obs,  # checklist §2 rule 17: re-read
                                                                # includes existing rows, empty on
                                                                # a first run
    }


def assemble_subgroup_packages(ctx, cluster_code: str, subgroup_row: dict,
                               member_strongs: list[str]) -> list[dict]:
    """One or more reading-call payloads for this subgroup -- never calls the network itself,
    returns each package plus its own pre-call cost estimate. Normally a single-element list (the
    whole subgroup, one call, unchanged from the original design). If exactly one member strong's
    occurrence count exceeds `_MAX_OCCURRENCES_PER_STRONG`, that strong's occurrences are split by
    surface (`_partition_occurrences_by_surface`) into multiple packages -- every OTHER member
    strong's FULL profile rides along unpartitioned in every one of them, so cross-strong
    comparison (this stage's whole point) stays intact; only the over-cap strong's own occurrence
    list is partial per package, and the prompt says so explicitly (`partial_note`). Raises
    `MultipleOverCapStrongs` if more than one member strong is over cap at once (not yet designed)."""
    conn = ctx.db.conn

    strong_profiles = {s: _strong_reading_profile(conn, s) for s in sorted(member_strongs)}
    over_cap = [s for s, p in strong_profiles.items()
               if len(p["occurrences"]) > _MAX_OCCURRENCES_PER_STRONG]
    if len(over_cap) > 1:
        raise MultipleOverCapStrongs(
            f"{cluster_code}/{subgroup_row['subgroup_code']}: {len(over_cap)} member strongs "
            f"exceed the cap simultaneously ({over_cap}) -- splitting is only designed for exactly "
            f"one over-cap strong per subgroup")

    rules = conn.execute(
        "SELECT rule_key, rule_text FROM cfg_method_rule WHERE step='cluster.reading' "
        "AND active=1 ORDER BY ordinal, rule_key").fetchall()
    rules_text = "\n".join(f"- {r['rule_key']}: {r['rule_text']}" for r in rules)

    tag_values = [r["value"] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='ib_observation.tag' AND inactive=0 "
        "ORDER BY ordinal")]

    chars_per_token = float(ctx.cfg.setting("lexical.llm_chars_per_token", 4))
    max_output_tokens = int(ctx.cfg.setting("lexical.llm_max_output_tokens", 40000))
    rate_in = float(ctx.cfg.setting("lexical.llm_rate_input_per_million", 3.00))
    rate_out = float(ctx.cfg.setting("lexical.llm_rate_output_per_million", 15.00))
    model = ctx.cfg.required_setting("lexical.llm_model")

    def _build(batch_profiles: dict, batch_label: str, batch_key: str, partial_note: str | None
              ) -> dict:
        instructions = _instructions(cluster_code, subgroup_row, rules_text, sorted(member_strongs),
                                     tag_values, partial_note)
        content = json.dumps({
            "cluster_code": cluster_code, "subgroup_code": subgroup_row["subgroup_code"],
            "label": subgroup_row["label"], "core_description": subgroup_row["core_description"],
            "anchor_verse_reference": subgroup_row["anchor_verse_reference"],
            "strongs": batch_profiles,
        }, ensure_ascii=False)
        est_input_tokens = int((len(instructions) + len(content)) / chars_per_token)
        est_cost = (est_input_tokens / 1_000_000 * rate_in) + (max_output_tokens / 1_000_000 * rate_out)
        return {
            "instructions": instructions, "content": content, "cluster_code": cluster_code,
            "subgroup_code": subgroup_row["subgroup_code"], "strong_count": len(member_strongs),
            "occurrence_count": sum(len(p["occurrences"]) for p in batch_profiles.values()),
            "batch_label": batch_label, "batch_key": batch_key,
            "est_input_tokens": est_input_tokens, "max_output_tokens": max_output_tokens,
            "est_cost_usd": round(est_cost, 4), "model": model,
        }

    if not over_cap:
        return [_build(strong_profiles, "1/1", "full", None)]

    over_strong = over_cap[0]
    full_occurrences = strong_profiles[over_strong]["occurrences"]
    partitions = _partition_occurrences_by_surface(full_occurrences, _MAX_OCCURRENCES_PER_STRONG)

    packages = []
    for idx, partition in enumerate(partitions, start=1):
        surfaces_in_partition = sorted({occ["surface"] for occ in partition})
        partial_note = (
            f"{over_strong} has {len(full_occurrences)} total occurrences, too many for one call "
            f"-- split by surface form into {len(partitions)} reading passes (never splitting one "
            f"surface's own occurrences across passes). This is pass {idx}/{len(partitions)}, "
            f"covering only the surface form(s) {surfaces_in_partition} ({len(partition)} of "
            f"{over_strong}'s {len(full_occurrences)} total occurrences). Other passes cover its "
            f"remaining surface forms separately -- do not assume you are seeing this strong's "
            f"complete occurrence list; every OTHER member strong in this package IS complete.")
        batch_profiles = dict(strong_profiles)
        batch_profiles[over_strong] = {**strong_profiles[over_strong], "occurrences": partition}
        packages.append(_build(
            batch_profiles, f"{idx}/{len(partitions)}",
            f"{over_strong}:{'|'.join(surfaces_in_partition)}", partial_note))
    return packages


def compute_strong_checks(conn, member_strongs: list[str],
                          source_stage: str = "char-reading") -> list[dict]:
    """Checklist §2 rule 10, code-computed AFTER the recording-pass write, not LLM-self-reported
    (see module docstring) -- diffs each member strong's FULL occurrence list against what
    `ib_node` actually traced for it at the given stage. A non-empty `missing_verses` is a real,
    load-time-visible completeness gap, matching checklist rule 0.7 ("a gap is a load-time finding,
    not silently accepted") -- surfaced to the caller for the run's own outcome message, never
    silently swallowed. `source_stage` parameterized (not hardcoded) so Stage 4
    (`charanswergenerate.py`) can reuse this exact function for its own completeness check rather
    than duplicating it."""
    out = []
    for strong in member_strongs:
        all_verses = {r["verse"] for r in _full_occurrences(conn, strong)}
        traced_verses = {r["verse_reference"] for r in conn.execute(
            "SELECT DISTINCT verse_reference FROM ib_node "
            "WHERE strong=? AND source_stage=?", (strong, source_stage))}
        missing = sorted(all_verses - traced_verses)
        out.append({"strong": strong, "occurrence_count": len(all_verses),
                   "traced_count": len(all_verses) - len(missing), "missing_verses": missing})
    return out


def _instructions(cluster_code: str, subgroup_row: dict, rules_text: str,
                  member_strongs: list[str], tag_values: list[str],
                  partial_note: str | None = None) -> str:
    partial_block = f"\n\nIMPORTANT -- PARTIAL OCCURRENCE COVERAGE THIS PASS: {partial_note}\n" \
                    if partial_note else ""
    return (
        f"You are producing char-reading observations (process c) for subgroup "
        f"{subgroup_row['subgroup_code']!r} of cluster {cluster_code} -- \"{subgroup_row['label']}\""
        f" ({subgroup_row['core_description']}). This subgroup's own member strongs are "
        f"{member_strongs}. You are given, per strong: gloss/transliteration, EVERY occurrence "
        f"corpus-wide (verse text, surface, morph_code -- not deduplicated, no sampling), all "
        f"present meaning sources (read as complementary evidence, never picking one and dropping "
        f"the others), its own Stage 1 (verse-reading) observations already captured (real "
        f"grounding -- do not re-derive or duplicate these, build on them), its Stage 2 "
        f"(char-subgroup) placement observations, and any of its own prior char-reading "
        f"observations (if this is a re-read).{partial_block}\n\n"
        f"Method rules governing this task:\n{rules_text}\n\n"
        f"YOUR ACTUAL JOB, distinct from Stage 1's per-verse reading: synergise the similar and "
        f"different contextual meaning of THIS SUBGROUP'S OWN member strongs against EACH OTHER "
        f"-- where do {member_strongs} genuinely share meaning, and where do they diverge, given "
        f"everything you've read? Stage 1 already covers per-occurrence surface/gloss divergence "
        f"for each strong on its own; your value here is the cross-strong comparison within this "
        f"one subgroup, and any strong-level pattern only visible from its FULL occurrence list "
        f"(e.g. a strong rendered three different ways across its occurrences, or a occurrence-"
        f"group that shares one distinct sense).\n\n"
        f"Valid `tag` values: {tag_values}\n"
        f"Prefer `tightly-related`/`no-direct-connection` for a cross-strong-within-subgroup "
        f"comparison (this subgroup's own core task); `verse-grouping` where several of a strong's "
        f"OWN occurrences share one genuinely alike reading; `difference-inference` for a specific "
        f"inference or distinction (morph-driven ones included -- check whether stem/voice "
        f"variation across a strong's occurrences is meaning-relevant); `surface-gloss-divergence` "
        f"only for a NEW divergence pattern not already covered by this strong's own Stage 1 "
        f"observations; `no-human-context` for a homonym/name with no meaningful context (earmark "
        f"and stop, no forced analysis); `data-error` for a data-quality issue noticed while "
        f"reading (own section, never chased down here); `could-not-resolve`/"
        f"`needs_adjacent_verse_context` per their existing definitions (state the reason in "
        f"obs_text, never a bare flag).\n\n"
        f"STRICT BOUNDARIES — do not exceed this task:\n"
        f"- Every `strong` value you write must be one of {member_strongs}.\n"
        f"- Every `verse` value in `occurrences` must be one you were actually given for that "
        f"strong -- do not cite a verse outside its own given occurrence list.\n"
        f"- Do not answer catalogue questions here (`question_code` should be null for essentially "
        f"all of these observations) -- that is process (d)'s job, a later stage. Leave "
        f"`question_code` null unless an observation genuinely IS a direct answer to an already-"
        f"live catalogue question.\n"
        f"- Do not add fields beyond the shape below, no prose before or after the JSON.\n\n"
        "Respond with ONLY a JSON object, no other text, shaped exactly:\n"
        '{"observations": [{"strong": "...", "question_code": null, "tag": "...", '
        '"obs_text": "...", "meaning_source": "..." or null, "occurrences": [{"verse": "...", '
        '"surface": "...", "morph_code": "..."}]}]}'
    )
