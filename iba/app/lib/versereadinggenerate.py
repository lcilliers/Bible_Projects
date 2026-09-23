"""versereadinggenerate.py — the LLM-calling half of `lexical.meaning` (the `verse-reading` stage,
escalation #1706 Phase C, 2026-09-17). Sibling to `lexicalenrichgenerate.py`, not a modification of
it — that module targets the retired `lexical.enrich`/`verse_lexical_note` shape; this one targets
the live `ib_observation`/`ib_node` architecture. `call_api`/`parse_response`/`log_usage` are
reused directly (imported, not duplicated) since the API-calling mechanics don't change between the
two; `assemble_batch_package`/`_instructions` are new, because the payload shape and the task itself
are different.

**Scope grain: per-cluster, pre-subgroup** (`#1711` v11) — the caller resolves a cluster's strongs
via `lexicalscope.resolve_strongs(cluster_code=...)`, this module reads Layer 1 (`verse_lexical`,
already rebuilt with the `role` JSON array) for those verses and batches them the same
`passage.max_verses`-sized way `lexicalenrichgenerate.py` already does — never a full-cluster push
in one call (`project_api_reads_budget_bounded_small_batches`).

**Progressive, relational, front-loaded — redesign #1723, 2026-09-17, researcher's own correction:**
*"verse-reading is not just about the cluster word, it is about the M-code words. This verse will
be read by 7 clusters. The previous observation for this word will be available to llm
progressively in each cluster and each cluster must not re-invent or duplicate but must see [if]
the focus change."* Full design capture:
`iba/docs/1706-progressive-relational-verse-reading-v1-20260917.md`. Two mechanisms, both live here:

1. **Front-loaded word-level battery (`M0.1`/`M0.5`).** The FIRST cluster-pass to touch a verse
   answers the word-level battery for EVERY M-code strong present in that verse, not just its own
   home strong(s) — `_strongs_needing_battery` checks live which M-code strongs in this batch's
   verses do NOT yet have any `stage='verse-reading'` `M0.1`/`M0.5` observation, and only those are
   included in `meaning_sources_by_strong` for the LLM to answer. A later cluster's pass over the
   same verse finds these already covered and never re-asks — cheaper AND richer per the
   researcher's own reasoning (effort shifts to the relational question instead).
2. **Relational, progressive `M0.6.5`.** Answered ONLY for the pass's own home strong(s), fed
   whatever `M0.6.5` observations already exist for the SAME verse (from earlier cluster-passes,
   any strong) as `prior_relational_context` — the LLM is instructed to build on that, not
   duplicate it, and the focus naturally shifts pass to pass (`M67`'s pass asks what role
   earnestness plays across the other M-codes; a later `M03` pass, seeing `M67`'s own answer, asks
   what role godly grief played FOR earnestness instead — same verse, different vantage point).
   Order-independent by construction: whichever cluster's pass runs first just finds no prior
   context and starts the chain; nothing requires a specific sequence.
3. **Whole-network, progressive `M0.6.6`** (added `#1819`, 2026-09-21, researcher instruction:
   "rich/comprehensive understanding of the context of the verse in relation to all the M-code
   strongs in the verse"). Same per-pass, progressive-build mechanism as `M0.6.5`, but a genuinely
   different question and its OWN separate prior-context stream (`prior_network_context_by_verse`,
   never merged with `M0.6.5`'s own chain): `M0.6.5` is one characteristic's own vantage on the
   others; `M0.6.6` synthesises the WHOLE M-code network the verse depicts in one place, something
   no single `M0.6.5` pass (by design, single-vantage) ever produces on its own. `M0.6.5` was also
   enriched the same session with explicit relation-type vocabulary (cause/enable/intensify/block/
   respond-to/tension, same-party-vs-different-party) so its own answers are systematic rather than
   an unguided narrative.

**The role-annotated word list — the actual design output of `#1706`'s role-data-presentation
doc, built here for real.** For every verse in a batch, every live `verse_lexical` row (not just
the cluster's own member strongs) is included, each carrying its full `role` array
(`cluster_strong.cluster_code` values — M-codes AND role-T-codes together) — deliberately including
the currently mechanically-unwired role tags (`T2`/`T6`/`T10`-`T15`), per the registry-construction
principle `cfg_method_rule` `role-list-includes-unwired-tags` states: over-inclusion is
recoverable, silent omission is not. This is what lets the LLM answer `D7.7` (does an
operation-tagged word relate to a party-tagged word in this verse) without a second query round-trip.

**Catalogue linkage** (`cfg_method_rule` `answers-M0.1-M0.5-D7.7`, now also `M0.6.5`/`M0.6.6`): the
system prompt embeds the live question text for `M0.1.1`-`M0.1.3` (Name and Naming), `M0.5.1`-
`M0.5.11` (Lexical and Semantic Analysis, now including the `#1723` alternative-meaning question),
`D7.7.1` (operation-anchored permeability), `M0.6.5` (relational, single-vantage), and `M0.6.6`
(whole-network synthesis, `#1819`) pulled from `wa_obs_question_catalogue` at call time — not a
second copy of the wording that could drift from the live catalogue, same discipline
`lexicalenrichgenerate.py`'s own docstring already established for `cfg_method_rule`.

**Output shape is `ib_observation`/`ib_node`, not `lexicalenrich.enrich_passage`'s old note shape.**
The model returns a flat list of observations; the recording pass (`iba/app/lib/recordingpass.py`,
built alongside this module) is the ONLY thing that ever turns this into DB rows — this module never
writes to the database itself, matching the single-writer principle (checklist rule 0.1).
"""

from __future__ import annotations

import json
import re

from .narrativegenerate import _api_key, ApiKeyMissing, ApiCallFailed  # noqa: F401 -- re-exported
from .lexicalenrichgenerate import call_api, log_usage  # reuse, don't duplicate
from .lexicalenrichgenerate import CostCapExceeded, BadModelResponse  # noqa: F401 -- re-exported
from . import stage1coverage
from .taggingguidance import TAG_GUIDANCE, tags_for_stage, guidance_block  # noqa: F401 -- TAG_GUIDANCE re-exported, other stages import it from here for backward compat


_JSON_FENCE_RE = re.compile(r"```(?:json)?\s*(\{.*\})\s*```", re.DOTALL)
_WORD_LEVEL_QUESTION_PREFIXES = ("M0.1", "M0.5")


def parse_response(text: str) -> dict:
    """This stage's own shape ({"observations": [...]}), not lexicalenrichgenerate.parse_response's
    {"notes"/"remove"} shape -- reusing that function would validate for the wrong keys and accept
    a malformed reply. Same fence-handling/error discipline, different required key."""
    candidate = text.strip()
    m = _JSON_FENCE_RE.search(candidate)
    if m:
        candidate = m.group(1)
    try:
        # strict=False: found live 2026-09-21, escalation #1826 -- the LLM's own obs_text
        # legitimately contains raw control characters (an unescaped newline inside a long
        # answer) that json.loads' strict mode rejects outright; Python's own documented
        # leniency for exactly this case, not custom sanitization.
        parsed = json.loads(candidate, strict=False)
    except json.JSONDecodeError as e:
        raise BadModelResponse(f"model reply is not valid JSON: {e} -- first 300 chars: {text[:300]!r}")
    if "observations" not in parsed:
        raise BadModelResponse(f"model reply has no 'observations' key: {list(parsed.keys())}")
    return parsed


def _meaning_sources(conn, strong: str) -> dict:
    """The 3 sources, read as complementary (rule `read-3-sources-complementary`) -- never picking
    one and dropping the others. Returns whichever of the 3 actually have content for this exact
    strong_variant; a source with nothing for this code is simply absent from the dict, not sent as
    an empty/null key (same "don't pay for nothing" discipline `lexicalenrichgenerate._lean_code`
    already established)."""
    out: dict = {}
    tree_rows = conn.execute(
        "SELECT sense_code, sense_text FROM strong_meaning_tree "
        "WHERE strong_variant=? AND deleted=0 ORDER BY sort", (strong,)).fetchall()
    if tree_rows:
        out["strong_meaning_tree"] = [
            {"sense_code": r["sense_code"], "sense_text": r["sense_text"]} for r in tree_rows]
    lex = conn.execute(
        "SELECT lsj, mounce FROM strong_lexicon WHERE strong=? AND deleted=0", (strong,)).fetchone()
    if lex:
        if lex["lsj"]:
            out["strong_lexicon.lsj"] = lex["lsj"]
        if lex["mounce"]:
            out["strong_lexicon.mounce"] = lex["mounce"]
    return out


def _role_word(row, home_cluster: str) -> dict:
    roles = json.loads(row["role"]) if row["role"] else []
    return {
        "strong": row["strong"],
        "surface": row["surface"],
        "morph_code": row["morph_code"],
        "cluster_codes": roles,
        "is_home_cluster": home_cluster in roles,
    }


def _strongs_needing_battery(conn, m_code_strongs: set[str]) -> set[str]:
    """RETIRED 2026-09-23 -- no longer called. Was #1723's front-loading skip ("any observation
    exists anywhere = covered, never ask again"), which is exactly the generic-answer pattern the
    researcher's 2026-09-23 correction rules out (an answer that can be resolved without looking at
    THIS verse/span/morph). Left in place, unused, rather than deleted -- the "any observation
    exists" query shape may still be useful reference for a genuinely different question family
    later; nothing in this module calls it any more (see the caller's own note where it used to be
    invoked)."""
    if not m_code_strongs:
        return set()
    ph = ",".join("?" * len(m_code_strongs))
    covered = {r[0] for r in conn.execute(
        f"SELECT DISTINCT strong FROM ib_observation WHERE stage='verse-reading' "
        f"AND strong IN ({ph}) AND (question_code LIKE 'M0.1%' OR question_code LIKE 'M0.5%')",
        tuple(m_code_strongs))}
    return m_code_strongs - covered


def _prior_relational_context(conn, verse_refs: list[str]) -> dict[str, list[dict]]:
    """#1723 progressive relational reading: existing M0.6.5 observations already recorded for
    verses in this batch, keyed by verse osisId -- fed to the LLM so a later cluster-pass builds on
    an earlier one's relational finding instead of re-deriving or duplicating it. Order-independent:
    whichever pass runs first simply finds nothing here and starts the chain. Matches on
    `ib_node.verse_reference` (osisId text) -- that table has no `verse_id` column."""
    return _prior_context_for_question(conn, verse_refs, "M0.6.5")


def _prior_network_context(conn, verse_refs: list[str]) -> dict[str, list[dict]]:
    """#1819 whole-network relational reading: existing M0.6.6 observations already recorded for
    verses in this batch -- same progressive mechanism as `_prior_relational_context`, but its own
    separate stream, not merged with M0.6.5's own chain. M0.6.5 is one characteristic's vantage on
    the others; M0.6.6 is a synthesis of the whole verse's M-code network -- conflating the two
    prior-context feeds would blur what "build on this" means for each."""
    return _prior_context_for_question(conn, verse_refs, "M0.6.6")


def _verse_cluster_agnostic_coverage(conn, verse_refs: list[str]) -> dict[str, dict[str, set[str]]]:
    """#1824 v14, researcher correction 2026-09-22, verbatim: "verse reading is supposed to be
    agnostic to cluster definition. every M-code word has the same status in the verse and need
    to be treated the same." M0.6.5/M0.6.6/D7.7.1 were wrongly restricted to "this cluster's own
    home strong(s)" -- the same home-strong scoping this module already dropped for M0.1/M0.5
    (front-loaded, #1723). Corrected to match: every M-code strong in the verse, not just the
    pass's own -- and M0.7 (already cluster-agnostic by population, #1806) folded into the SAME
    front-loading check here too (#1824 v18): a later cluster's pass touching an already-fully-
    read verse must not re-derive M0.7 for it either.

    2026-09-23 correction, researcher verbatim: "Every word observation answer must be at span
    (word in verse context) level. Saying that you can resolve the observation question without
    looking at the verse/span/morph means it is a generic answer." M0.1/M0.5 joined this SAME
    per-verse (never globally-once) front-loading check on that date -- `_strongs_needing_battery`
    and its "word-invariant fact, answered once ever" premise are RETIRED for these codes (this
    docstring's own prior claim that M0.1/M0.5 are word-invariant was the defect being corrected,
    not a reason to keep treating them differently from the other four). "Already answered" now
    means "already answered FOR THIS VERSE" for all five question families uniformly -- M0.6.5,
    M0.6.6, D7.7.1, M0.7.1-16, and M0.1.x/M0.5.x. Returns {verse_osis: {strong: {question_code
    already live for that verse+strong, any cluster's pass}}}."""
    if not verse_refs:
        return {}
    ph = ",".join("?" * len(verse_refs))
    rows = conn.execute(
        f"SELECT n.verse_reference, n.strong, o.question_code "
        f"FROM ib_node n JOIN ib_observation o ON o.id = n.observation_id "
        f"WHERE o.stage='verse-reading' AND o.status != 'withdrawn' "
        f"AND (o.question_code IN ('M0.6.5', 'M0.6.6', 'D7.7.1', 'M0.8.1') "
        f"OR o.question_code LIKE 'M0.7%' "
        f"OR o.question_code LIKE 'M0.1%' OR o.question_code LIKE 'M0.5%') "
        f"AND n.verse_reference IN ({ph})", verse_refs).fetchall()
    out: dict[str, dict[str, set[str]]] = {}
    for r in rows:
        out.setdefault(r["verse_reference"], {}).setdefault(r["strong"], set()).add(r["question_code"])
    return out


def _prior_context_for_question(conn, verse_refs: list[str], question_code: str
                                ) -> dict[str, list[dict]]:
    if not verse_refs:
        return {}
    ph = ",".join("?" * len(verse_refs))
    rows = conn.execute(
        f"SELECT DISTINCT o.cluster_code, o.strong, o.obs_text, n.verse_reference "
        f"FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id "
        f"WHERE o.stage='verse-reading' AND o.question_code=? "
        f"AND n.verse_reference IN ({ph}) ORDER BY o.created_at",
        (question_code, *verse_refs)).fetchall()
    by_verse: dict[str, list[dict]] = {}
    for r in rows:
        by_verse.setdefault(r["verse_reference"], []).append(
            {"from_cluster": r["cluster_code"], "about_strong": r["strong"], "finding": r["obs_text"]})
    return by_verse


def assemble_batch_package(ctx, cluster_code: str, verse_ids: list[int],
                           force: bool = False) -> dict:
    """One chunk (already capped to <= passage.max_verses by the caller). Never calls the network
    itself -- returns the package plus a pre-call cost estimate, same two-step separation
    `lexicalenrichgenerate.assemble_batch_package`/`call_api` already established (cost preview
    before spend, never silent).

    `force` (2026-09-22, found live testing #1832's cross-strong dedup fix): a `-Force`
    reconciliation rerun bypasses `batchcontrol.already_committed`'s content-hash skip at the
    caller level, but the `expected_items` checklist (BUILD #321) still filtered against
    `already_covered` regardless -- for a verse whose per-occurrence questions are ALL already
    live-covered (the normal target of a deliberate `-Force` rerun), that produced an EMPTY
    checklist, and the "answer exactly this list" prompt instruction correctly made the model
    write ZERO observations while the call still cost real money (confirmed live: $0.29 spent,
    0 rows written). `force=True` skips the `already_covered` filter entirely (checklist =
    the FULL expected set, not just the gap) and omits each verse's own `already_covered` field
    from the payload too, so the model isn't given contradictory "skip this" signals alongside
    "answer exactly this list"."""
    conn = ctx.db.conn
    ph = ",".join("?" * len(verse_ids))

    verse_rows = conn.execute(
        f"SELECT id, osisId, text FROM verse WHERE id IN ({ph}) AND deleted=0", verse_ids).fetchall()
    verse_by_id = {r["id"]: r for r in verse_rows}

    lex_rows = conn.execute(
        f"SELECT verse_id, strong, surface, morph_code, role FROM verse_lexical "
        f"WHERE verse_id IN ({ph}) AND deleted=0 ORDER BY verse_id, position", verse_ids).fetchall()

    roles_by_verse: dict[int, list[dict]] = {}
    cluster_member_strongs: set[str] = set()
    all_m_code_strongs: set[str] = set()
    # #1836, 2026-09-22: T2/T3-tagged words that carry NO M-code role at all -- the M0.8.1
    # elevation-candidate population. A word carrying BOTH a T-code and an M-code is already its
    # own characteristic, nothing to flag; only the T-code-only case is a genuine candidate.
    elevation_candidates_by_verse: dict[int, set[str]] = {}
    for r in lex_rows:
        roles_by_verse.setdefault(r["verse_id"], []).append(_role_word(r, cluster_code))
        roles = json.loads(r["role"]) if r["role"] else []
        if not r["strong"]:
            continue
        if cluster_code in roles:
            cluster_member_strongs.add(r["strong"])
        has_m_code = any(c.startswith("M") for c in roles)
        if has_m_code:
            all_m_code_strongs.add(r["strong"])
        elif any(c in ("T2", "T3") for c in roles):
            elevation_candidates_by_verse.setdefault(r["verse_id"], set()).add(r["strong"])

    verses_out = []
    for vid in verse_ids:
        v = verse_by_id.get(vid)
        if v is None:
            continue
        verse_entry = {
            "verse": v["osisId"], "text": v["text"], "roles_in_verse": roles_by_verse.get(vid, [])}
        if vid in elevation_candidates_by_verse:
            verse_entry["elevation_candidate_words"] = sorted(elevation_candidates_by_verse[vid])
        verses_out.append(verse_entry)

    # #1723/#1820's "once ever per strong" front-loading (2026-09-17/21) is RETIRED for M0.1/M0.5,
    # 2026-09-23 -- researcher correction, verbatim: "Every word observation answer must be at span
    # (word in verse context) level. Saying that you can resolve the observation question without
    # looking at the verse/span/morph means it is a generic answer." #1820's own finding (8 answers
    # for H3034/M0.1.1 across different verses, all restating the same claim) was read backwards at
    # the time -- that's independently-grounded convergence, exactly what SHOULD happen when the
    # same root fact holds across occurrences, and `recordingpass.py`'s dedup consolidates it into
    # one shared observation at write time. What must not happen is skipping the generation itself
    # because a strong already has an answer from a DIFFERENT occurrence -- that was never
    # confirming convergence, it was assuming it. `home_needs_battery`/`other_needs_battery` below
    # now mean "every M-code strong in scope, full stop" (every verse's own occurrence is asked);
    # the per-verse gate that actually decides whether THIS verse's copy is still needed lives in
    # `already_covered`/`checklist_items` (`_verse_cluster_agnostic_coverage`, updated same date).
    # `meaning_sources_by_strong` stays populated for EVERY M-code strong, unconditionally -- same
    # as before, just no longer gated on a battery-skip that no longer exists.
    home_needs_battery = set(cluster_member_strongs)
    other_needs_battery = all_m_code_strongs - cluster_member_strongs
    word_battery_strongs = home_needs_battery | other_needs_battery
    # Broadened to every M-code strong (was cluster_member_strongs | other_needs_battery) --
    # M0.6.5/M0.6.6/D7.7.1 now reason about EVERY M-code word in the verse (see below), not just
    # this cluster's own home strong(s), so every one of them needs meaning context available,
    # regardless of word-level battery status.
    meaning_by_strong = {s: _meaning_sources(conn, s) for s in sorted(all_m_code_strongs)}

    prior_relational = _prior_relational_context(conn, [v["verse"] for v in verses_out])
    prior_network = _prior_network_context(conn, [v["verse"] for v in verses_out])
    # #1824 v14/v18 researcher correction, 2026-09-22: M0.6.5/M0.6.6/D7.7.1/M0.7 must all be
    # cluster-agnostic -- "every M-code word has the same status in the verse and need to be
    # treated the same" -- and a later cluster's pass over an already-fully-read verse must not
    # re-derive any of them ("if the second read of the verse finds additional observations then
    # something went wrong in the first reading"). Front-load skip data (per verse, not globally
    # -- see _verse_cluster_agnostic_coverage's own docstring) folded straight into each verse's
    # own dict below so the LLM sees exactly what's already answered for THAT verse without a
    # second lookup.
    already_covered = {} if force else _verse_cluster_agnostic_coverage(
        conn, [v["verse"] for v in verses_out])
    for v in verses_out:
        covered = already_covered.get(v["verse"], {})
        if covered:
            v["already_covered"] = {s: sorted(qs) for s, qs in covered.items()}

    # Researcher instruction (prior session, re-confirmed 2026-09-22): "the expected answer for
    # each question and strong had to be pre-drafted as part of the stage 1 code" -- BUILD #315
    # diagnosed a real instruction-compliance gap (non-home M-strongs averaged 7.3/16 M0.7
    # sub-answers vs home strongs' 100%) and named the fix ("a per-strong checklist rather than a
    # prose instruction") but never built it. `stage1coverage.expected_nodes()` already computes
    # the exact (verse, strong, question_code) set this batch SHOULD attempt, using the identical
    # population/gating rules this module's own prose instructions describe -- reused here
    # directly (never a second hardcoded copy that could drift from the validator). Filtered
    # against this same `already_covered` map so the checklist only lists what THIS call must
    # still answer, matching the skip semantics the prose instructions already describe.
    expected_all = stage1coverage.expected_nodes(conn, cluster_code, verse_ids)
    checklist_items = []
    for r in expected_all:
        covered_qs = already_covered.get(r["verse_reference"], {}).get(r["strong"], set())
        if r["question_code"] in covered_qs:
            continue
        checklist_items.append({
            "verse": r["verse_reference"], "strong": r["strong"],
            "question_code": r["question_code"]})

    questions = conn.execute(
        "SELECT question_code, question_text FROM wa_obs_question_catalogue "
        "WHERE deleted=0 AND (question_code LIKE 'M0.1%' OR question_code LIKE 'M0.5%' "
        "OR question_code LIKE 'M0.7%' "
        "OR question_code IN ('D7.7.1', 'M0.6.5', 'M0.6.6', 'M0.8.1')) "
        "ORDER BY question_code").fetchall()
    question_texts = [{"question_code": q["question_code"], "question_text": q["question_text"]}
                      for q in questions]

    tag_values = tags_for_stage("verse-reading", [r["value"] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='ib_observation.tag' AND inactive=0 "
        "ORDER BY ordinal")])

    rules = conn.execute(
        "SELECT rule_key, rule_text FROM cfg_method_rule WHERE step='lexical.meaning' "
        "AND active=1 ORDER BY ordinal").fetchall()
    rules_text = "\n".join(f"- {r['rule_key']}: {r['rule_text']}" for r in rules)

    instructions = _instructions(cluster_code, question_texts, tag_values, rules_text,
                                 [v["verse"] for v in verses_out], sorted(cluster_member_strongs),
                                 sorted(home_needs_battery), sorted(other_needs_battery),
                                 sorted(all_m_code_strongs), len(checklist_items))
    content = json.dumps({"cluster_code": cluster_code, "verses": verses_out,
                          "meaning_sources_by_strong": meaning_by_strong,
                          "prior_relational_context_by_verse": prior_relational,
                          "prior_network_context_by_verse": prior_network,
                          "expected_items": checklist_items},
                         ensure_ascii=False)

    chars_per_token = float(ctx.cfg.setting("lexical.llm_chars_per_token", 4))
    est_input_tokens = int((len(instructions) + len(content)) / chars_per_token)
    max_output_tokens = int(ctx.cfg.setting("lexical.llm_max_output_tokens", 8000))
    rate_in = float(ctx.cfg.setting("lexical.llm_rate_input_per_million", 3.00))
    rate_out = float(ctx.cfg.setting("lexical.llm_rate_output_per_million", 15.00))
    est_cost = (est_input_tokens / 1_000_000 * rate_in) + (max_output_tokens / 1_000_000 * rate_out)

    return {
        "instructions": instructions, "content": content, "verse_ids": verse_ids,
        "cluster_code": cluster_code, "verse_count": len(verses_out),
        "cluster_member_strong_count": len(cluster_member_strongs),
        "word_battery_strong_count": len(word_battery_strongs),
        "front_loaded_strong_count": len(other_needs_battery),
        "home_already_settled_count": len(cluster_member_strongs) - len(home_needs_battery),
        "expected_item_count": len(checklist_items),
        "est_input_tokens": est_input_tokens, "max_output_tokens": max_output_tokens,
        "est_cost_usd": round(est_cost, 4),
        "model": ctx.cfg.required_setting("lexical.llm_model"),
    }


def _instructions(cluster_code: str, questions: list[dict], tag_values: list[str],
                  rules_text: str, verse_refs: list[str], home_strongs: list[str],
                  home_needs_battery: list[str], other_needs_battery: list[str],
                  all_m_code_strongs: list[str], expected_item_count: int) -> str:
    q_text = "\n".join(f"- {q['question_code']}: {q['question_text']}" for q in questions)
    tag_guidance_text = guidance_block(tag_values)
    word_battery_strongs = sorted(set(home_needs_battery) | set(other_needs_battery))
    # 2026-09-23: "front-loading"/"already settled, don't re-answer" RETIRED -- researcher
    # correction, verbatim: "Every word observation answer must be at span (word in verse context)
    # level. Saying that you can resolve the observation question without looking at the
    # verse/span/morph means it is a generic answer." M0.1/M0.5 now use the SAME uniform population
    # and the SAME per-verse `already_covered` gate as M0.6.5/M0.6.6/D7.7.1/M0.7 -- no separate
    # notes needed, the shared instruction text below already covers it.
    front_load_note = ""
    settled_note = ""
    return (
        f"You are producing verse-reading observations for cluster {cluster_code}, the pre-"
        f"subgroup Layer 2 pass (`lexical.meaning`). You are given, per verse: the verse's own base "
        f"text, `roles_in_verse` -- every role-bearing word in that verse, each carrying "
        f"`cluster_codes` (the full set of M-code and role-T-code tags) and `is_home_cluster` (true "
        f"if this word belongs to cluster {cluster_code} -- informational only, per #1824 v14: "
        f"M0.6.5/M0.6.6/D7.7.1 are answered for every M-code word regardless, same as M0.1/M0.5/"
        f"M0.7) -- `prior_relational_context_by_verse` -- any M0.6.5 relational findings ALREADY "
        f"recorded for these verses by an earlier pass, any cluster -- `prior_network_context_by_"
        f"verse` -- any M0.6.6 whole-network findings already recorded for these verses (a "
        f"SEPARATE stream from M0.6.5's own chain) -- and, per verse where applicable, "
        f"`already_covered` -- {{strong: [question_codes]}} already live for THAT verse "
        f"(any pass) -- do not re-answer M0.6.5/M0.6.6/D7.7.1/M0.7.1-16 for a strong+question pair "
        f"already listed there for that verse: a later cluster's pass over a verse another pass "
        f"already fully read must not re-derive it (#1824 v18) -- if you find yourself about to "
        f"answer something already listed there, skip it. You are also given `meaning_sources_by_strong` for "
        f"{all_m_code_strongs} (every M-code strong in this batch, not just this cluster's own "
        f"member strongs).{front_load_note}{settled_note} Read all present meaning "
        f"sources as complementary evidence, never picking one and ignoring the others.\n\n"
        f"`expected_items` IS THE AUTHORITATIVE CHECKLIST -- read it before writing anything. It "
        f"lists, pre-computed from live data, EXACTLY the {expected_item_count} (verse, strong, "
        f"question_code) triples this batch must answer -- every population/gating rule described "
        f"below (word-level-battery-only-for-strongs-needing-it, cluster-agnostic-relational-"
        f"questions, the D7.7.1 T3 gate, the already_covered skip) has ALREADY been applied to "
        f"build this list. Do not re-derive the population yourself from the prose rules -- they "
        f"explain WHY each entry is there, `expected_items` is the authoritative WHAT. Your "
        f"`observations` array MUST contain exactly one entry per `expected_items` triple: same "
        f"count, same (strong, question_code) pairs for the correct verse -- no fewer (a triple "
        f"you skip is a real gap, even one you judge inapplicable: answer it with the question's "
        f"own 'record none'/could-not-resolve convention instead of omitting it) and no more (never "
        f"add a (verse, strong, question_code) combination not listed in `expected_items`).\n\n"
        f"Method rules governing this task:\n{rules_text}\n\n"
        f"TWO KINDS OF QUESTION, answered the same way:\n"
        f"- M0.1/M0.5 (word-level battery): answer for EVERY M-code strong present in "
        f"`roles_in_verse` for each verse -- {word_battery_strongs} this batch -- the SAME "
        f"population as M0.6.5/M0.6.6/D7.7.1/M0.7 below, EXCEPT any (strong, question_code) pair "
        f"already listed in that verse's own `already_covered` (skip those, another pass already "
        f"answered them for this exact verse). SPAN-GROUNDED, NOT GENERIC (researcher, "
        f"2026-09-23): your answer must be resolvable ONLY by looking at THIS occurrence's own "
        f"surface/morph_code within THIS verse -- if you could answer it identically without ever "
        f"reading the verse (a bare dictionary fact about the lemma), you have answered the wrong "
        f"question. Two genuinely different occurrences of the same strong may legitimately produce "
        f"the same or different answers; that is decided by what each occurrence actually shows, "
        f"never assumed either way in advance. ACTIVELY ENGAGE WITH THE SURFACE FORM (researcher, "
        f"2026-09-23): `surface` and `morph_code` are given for THIS occurrence, not as bookkeeping "
        f"-- if this word's actual rendering/inflection here is not the term's most typical or "
        f"expected form, that is a real signal, not noise: a translator chose that specific "
        f"rendering because the verse's own context called for it. Treat a marked or unusual "
        f"surface form as a direct prompt to look harder at what THIS context is doing differently, "
        f"the same way M0.5.11 already asks you to notice when an occurrence's sense diverges from "
        f"the term's usual one -- the surface form is often the visible trace of exactly that "
        f"divergence, not a separate fact to ignore while answering the meaning question.\n"
        f"- M0.6.5 (relational), M0.6.6 (whole-network), and D7.7.1 (operation-permeability): "
        f"answer for EVERY M-code strong present in `roles_in_verse` for each verse (#1824 v14, "
        f"corrected 2026-09-22 -- these are cluster-agnostic, same population as M0.1/M0.5/M0.7, "
        f"NOT restricted to this cluster's own home strong(s)), EXCEPT any (strong, question_code) "
        f"pair already listed in that verse's own `already_covered` -- skip those, "
        f"another pass already answered them for this exact verse. For M0.6.5: if "
        f"`prior_relational_context_by_verse` already has an entry for this verse (from any "
        f"strong), your answer for a NEW strong MUST build on it where relevant -- add THIS word's "
        f"own vantage point, never repeat what's already there; with no prior entry, start the "
        f"relational chain. For M0.6.6: the same progressive rule applies against "
        f"`prior_network_context_by_verse` instead -- extend or correct an existing sketch of the "
        f"verse's whole M-code network with what THIS word's own membership in it adds, never "
        f"restate it unchanged; record none for a word that is the verse's only M-code element "
        f"(per the question's own text -- still answer it, the finding is just \"none\", never "
        f"skip the question entirely). D7.7.1: record none if no operation-tagged (role-T3) word "
        f"is present in the verse at all -- the question's only actual gate; do not additionally "
        f"require a specifically party-coded (T4/T7/T8/T9) word, the live tagging for that is "
        f"sparse and would wrongly exclude real cases (e.g. a plain T2-tagged \"God\" or "
        f"\"others\" is still a real party for this question's purposes).\n"
        f"- M0.7.1-16 (verse substantiation, `#1806`, 2026-09-21): answer for EVERY M-code strong "
        f"present in `roles_in_verse` for each verse -- the SAME population as the M0.1/M0.5 "
        f"battery, not just this cluster's own home strongs -- EXCEPT any (strong, question_code) "
        f"pair already listed in that verse's own `already_covered` (#1824 v18: another cluster's "
        f"pass already answered it for this exact verse, skip it). These questions are deliberately "
        f"written about \"[this word]\", never about \"the characteristic\" -- you are not told, "
        f"and must not assume, which cluster's pass is asking; answer purely from what the word "
        f"and its relationships in the verse actually show. Unlike M0.1/M0.5, these are NOT "
        f"settled-once-ever ACROSS DIFFERENT VERSES -- the same word can genuinely behave "
        f"differently verse to verse (the same principle M0.5.11 already applies), so a strong "
        f"already having M0.7 answers from OTHER verses is never itself a reason to skip THIS "
        f"verse. But THIS verse+strong+question, once genuinely answered (by any pass), is settled "
        f"-- `already_covered` is what tells you that, not your own judgement. A later, separate "
        f"process (not you) reconciles any residual repeated findings across occurrences -- your "
        f"job is an accurate, concise reading of THIS verse only, not deciding whether it "
        f"duplicates another.\n"
        f"- M0.8.1 (T2/T3 attention flag, `#1836`/2026-09-23 simplification, rare): answer ONLY "
        f"for a verse's own `elevation_candidate_words` list, if present (a word tagged T2 or T3 "
        f"in `roles_in_verse` but with NO M-code role at all -- do not answer this for any M-code "
        f"word). This is a plain flag, not a ruling: is this word's behavior HERE significant "
        f"enough on its own terms to deserve a closer look, independent of its current supporting "
        f"role? Most T2/T3 words are genuinely just supporting roles; record none unless the case "
        f"is real. If yes, tag `elevation-candidate` and state briefly why in `obs_text` -- this "
        f"only surfaces the word for a later human look, it never changes any cluster/role "
        f"assignment itself.\n\n"
        f"Answer these catalogue questions:\n{q_text}\n\n"
        f"Valid `tag` values: {tag_values}\n"
        f"{tag_guidance_text}\n\n"
        f"STRICT BOUNDARIES — do not exceed this task:\n"
        f"- You are given exactly {len(verse_refs)} verse(s), listed at the end of this message. "
        f"Every `verse` value you write MUST be one of exactly those.\n"
        f"- Every `strong` value you write for M0.1/M0.5/M0.6.5/M0.6.6/D7.7.1/M0.7.1-16 must "
        f"be any M-code strong actually present in that verse's own `roles_in_verse` (any "
        f"`cluster_codes` entry starting with \"M\") -- the SAME population for all of these, "
        f"regardless of home-cluster membership (#1824 v14, extended to M0.1/M0.5 2026-09-23) -- "
        f"minus whatever that verse's own `already_covered` already lists. "
        f"D7.7.1 only applies when an operation-tagged (role-T3) word is actually "
        f"present in the verse -- no additional party-tag requirement. For M0.8.1, `strong` must "
        f"be one of that verse's own `elevation_candidate_words` ONLY (never an M-code strong) -- "
        f"if a verse has no `elevation_candidate_words` field, do not answer M0.8.1 for it at "
        f"all.\n"
        f"- `question_code` MUST be the exact, specific leaf code (e.g. \"M0.1.2\", \"M0.5.7\") — "
        f"NEVER a bare component code (\"M0.1\", \"M0.5\" are not valid, will be rejected, and "
        f"waste your own output). One observation per specific sub-question — do not combine "
        f"several sub-questions' answers into a single note under one code, even for a front-"
        f"loaded strong you are covering quickly.\n"
        f"- If a genuine 'couldn't resolve' case arises, use tag `could-not-resolve` and state in "
        f"`obs_text` what signal suggests it should be resolvable with further analysis. If the "
        f"verse's own content is insufficient and an adjacent verse would help, use tag "
        f"`needs_adjacent_verse_context` and state explicitly in `obs_text` what's outstanding and "
        f"what the follow-up cross-check needs to establish (never a bare flag with no reason).\n"
        f"- For M0.7.1-16 ONLY, also fill `meaning_keywords`: 2-5 short key terms/concepts "
        f"capturing the core of your answer (e.g. [\"conditional-change\", \"unfruitful-to-"
        f"fruitful\"], not full phrases) -- used downstream to recognise when two occurrences "
        f"genuinely show the same finding (escalation #1824), separate from your own obs_text "
        f"wording. Leave `meaning_keywords` null for every other question type (M0.1/M0.5/M0.6.5/"
        f"M0.6.6/D7.7.1) -- #1832 (2026-09-22): their identity is now resolved structurally "
        f"(same verse + same question_code = same fact, by construction), never by keyword or "
        f"prose-similarity matching, so a keyword signal for these three would serve no purpose.\n"
        f"- Do not add fields beyond the shape below, no prose before or after the JSON.\n\n"
        f"Verses in this batch: {verse_refs}\n\n"
        "Respond with ONLY a JSON object, no other text, shaped exactly:\n"
        '{"observations": [{"strong": "...", "question_code": "..." or null, "tag": "...", '
        '"obs_text": "...", "meaning_source": "...", "meaning_keywords": ["...", "..."] or null, '
        '"occurrences": [{"verse": "...", "surface": "...", "morph_code": "..."}]}]}'
    )
