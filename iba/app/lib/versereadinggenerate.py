"""versereadinggenerate.py — the LLM-calling half of `lexical.meaning` (word-level) and
`lexical.relational` (the verse-reading stage, #1706, #1860), against ib_observation/ib_node.
`call_api`/`parse_response`/`log_usage` are reused from `lexicalenrichgenerate.py`; the payload
assembly and prompts are this module's.

**Scope: per-cluster, pre-subgroup.** The caller resolves a cluster's strongs
(`lexicalscope.resolve_strongs`); this module reads Layer 1 (`verse_lexical`, with its `role`
array) for those verses, in caller-capped batches, never a full cluster in one call.

**Cluster-agnostic, per verse.** Every M-code word in a verse has the same status: each question
family is answered for every M-code strong present, and "already answered" means already answered
for that verse (`_verse_cluster_agnostic_coverage`), so a later cluster's pass does not re-derive a
fully read verse. Word-level answers (M0.1/M0.5) are grounded in each occurrence (#1849).

**Progressive relational reading.** `M0.6.5` (one characteristic's vantage on the others) and
`M0.6.6` (the whole M-code network of the verse, #1819) each get their own prior-context stream
of earlier passes' answers for the same verse, to build on rather than duplicate. Relational
questions also receive the committed word-level findings (`_word_level_findings`) alongside the
raw lexicon.

**Role-annotated word list.** Every live `verse_lexical` row of each verse is included with its
full `role` array, unwired role tags included (cfg_method_rule role-list-includes-unwired-tags).

**Catalogue linkage.** The prompts embed the live question text from `wa_obs_question_catalogue`
at call time, never a second copy.

**Output** is a flat list of observations; `lib/recordingpass.py` is the only thing that turns it
into DB rows. This module never writes to the database.
"""

from __future__ import annotations

import json
import re

from .lexicalenrichgenerate import _api_key, ApiKeyMissing, ApiCallFailed  # noqa: F401 -- re-exported
from .lexicalenrichgenerate import call_api, log_usage  # reuse, don't duplicate
from .lexicalenrichgenerate import CostCapExceeded, BadModelResponse  # noqa: F401 -- re-exported
from . import stage1coverage
from .taggingguidance import tags_for_stage, guidance_block


_JSON_FENCE_RE = re.compile(r"```(?:json)?\s*(\{.*\})\s*```", re.DOTALL)
_JSON_BARE_RE = re.compile(r"(\{.*\})", re.DOTALL)
_WORD_LEVEL_QUESTION_PREFIXES = ("M0.1", "M0.5")


def parse_response(text: str) -> dict:
    """This stage's own shape ({"observations": [...]}), not lexicalenrichgenerate.parse_response's
    {"notes"/"remove"}. Same fence-handling and error discipline, different required key."""
    candidate = text.strip()
    m = _JSON_FENCE_RE.search(candidate)
    if m:
        candidate = m.group(1)
    try:
        # strict=False: obs_text may contain raw control characters (an unescaped newline) (#1826)
        parsed = json.loads(candidate, strict=False)
    except json.JSONDecodeError as e:
        # fallback (#1866): a prose preamble before a bare JSON object -- retry once on the first '{'
        # through the last '}'; if that fails too, the original error is raised
        bare = _JSON_BARE_RE.search(text.strip())
        if bare is None:
            raise BadModelResponse(f"model reply is not valid JSON: {e} -- first 300 chars: {text[:300]!r}")
        try:
            parsed = json.loads(bare.group(1), strict=False)
        except json.JSONDecodeError:
            raise BadModelResponse(f"model reply is not valid JSON: {e} -- first 300 chars: {text[:300]!r}")
    if "observations" not in parsed:
        raise BadModelResponse(f"model reply has no 'observations' key: {list(parsed.keys())}")
    return parsed


def _meaning_sources(conn, strong: str) -> dict:
    """The 3 sources, read as complementary (rule read-3-sources-complementary): whichever have
    content for this exact strong_variant; an empty source is left out of the dict."""
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


def _word_level_findings(conn, verse_refs: list[str]) -> dict[str, dict[str, list[dict]]]:
    """`lexical.relational`'s primary grounding (#1860): committed (non-withdrawn) M0.1/M0.5
    `ib_observation` rows for this exact verse+strong. Returns {verse_osis: {strong: [{question_code,
    obs_text}]}}. Sent alongside `meaning_sources_by_strong` (the raw lexicon), never instead of it.
    Matches on `ib_node.verse_reference` (osisId text)."""
    if not verse_refs:
        return {}
    ph = ",".join("?" * len(verse_refs))
    rows = conn.execute(
        f"SELECT n.verse_reference, n.strong, o.question_code, o.obs_text "
        f"FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id "
        f"WHERE o.stage='verse-reading' AND o.status != 'withdrawn' "
        f"AND (o.question_code LIKE 'M0.1%' OR o.question_code LIKE 'M0.5%') "
        f"AND n.verse_reference IN ({ph}) ORDER BY n.strong, o.question_code",
        verse_refs).fetchall()
    out: dict[str, dict[str, list[dict]]] = {}
    for r in rows:
        out.setdefault(r["verse_reference"], {}).setdefault(r["strong"], []).append(
            {"question_code": r["question_code"], "obs_text": r["obs_text"]})
    return out


def _strongs_needing_battery(conn, m_code_strongs: set[str]) -> set[str]:
    """Not called (superseded by per-verse coverage, #1849). Answered whether any word-level
    observation existed anywhere for a strong."""
    if not m_code_strongs:
        return set()
    ph = ",".join("?" * len(m_code_strongs))
    covered = {r[0] for r in conn.execute(
        f"SELECT DISTINCT strong FROM ib_observation WHERE stage='verse-reading' "
        f"AND strong IN ({ph}) AND (question_code LIKE 'M0.1%' OR question_code LIKE 'M0.5%')",
        tuple(m_code_strongs))}
    return m_code_strongs - covered


def _prior_relational_context(conn, verse_refs: list[str]) -> dict[str, list[dict]]:
    """Existing M0.6.5 observations for verses in this batch, keyed by verse osisId, so a later pass
    builds on an earlier one's relational finding. Order-independent: the first pass finds nothing.
    Matches on `ib_node.verse_reference` (that table has no `verse_id`)."""
    return _prior_context_for_question(conn, verse_refs, "M0.6.5")


def _prior_network_context(conn, verse_refs: list[str]) -> dict[str, list[dict]]:
    """Existing M0.6.6 observations for verses in this batch (#1819): the same progressive mechanism
    as `_prior_relational_context`, as a separate stream (single vantage vs. whole network)."""
    return _prior_context_for_question(conn, verse_refs, "M0.6.6")


def _verse_cluster_agnostic_coverage(conn, verse_refs: list[str]) -> dict[str, dict[str, set[str]]]:
    """Per-verse, cluster-agnostic coverage (#1824, #1849): every M-code strong in the verse is
    treated the same, and "already answered" means answered for this verse, for every question family
    (M0.6.5, M0.6.6, D7.7.1, M0.7.1-16, M0.1.x/M0.5.x). Returns {verse_osis: {strong: {question_code
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


def _scan_verses(conn, cluster_code: str, verse_ids: list[int]) -> dict:
    """Shared verse/role scan used by both `assemble_word_level_batch_package` and
    `assemble_relational_batch_package` (#1860), so they agree on what a verse and a role-bearing
    word are."""
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
    # T2/T3-tagged words with no M-code role: the M0.8.1 elevation-candidate population (#1836)
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

    return {
        "verse_by_id": verse_by_id, "roles_by_verse": roles_by_verse,
        "cluster_member_strongs": cluster_member_strongs,
        "all_m_code_strongs": all_m_code_strongs,
        "elevation_candidates_by_verse": elevation_candidates_by_verse,
    }


def _build_verses_out(verse_ids: list[int], scan: dict, include_elevation: bool) -> list[dict]:
    verse_by_id, roles_by_verse = scan["verse_by_id"], scan["roles_by_verse"]
    elevation_candidates_by_verse = scan["elevation_candidates_by_verse"]
    verses_out = []
    for vid in verse_ids:
        v = verse_by_id.get(vid)
        if v is None:
            continue
        verse_entry = {
            "verse": v["osisId"], "text": v["text"], "roles_in_verse": roles_by_verse.get(vid, [])}
        if include_elevation and vid in elevation_candidates_by_verse:
            verse_entry["elevation_candidate_words"] = sorted(elevation_candidates_by_verse[vid])
        verses_out.append(verse_entry)
    return verses_out


def _apply_already_covered(conn, verses_out: list[dict], force: bool) -> dict:
    """Folds each verse's per-verse coverage (`_verse_cluster_agnostic_coverage`) into its own dict,
    so the LLM sees what is already answered for that verse. Shared by both assemblies."""
    already_covered = {} if force else _verse_cluster_agnostic_coverage(
        conn, [v["verse"] for v in verses_out])
    for v in verses_out:
        covered = already_covered.get(v["verse"], {})
        if covered:
            v["already_covered"] = {s: sorted(qs) for s, qs in covered.items()}
    return already_covered


def _build_checklist(conn, cluster_code: str, verse_ids: list[int], already_covered: dict,
                     family: str) -> list[dict]:
    """The expected (verse, strong, question_code) set this batch should attempt for `family`, from
    `stage1coverage.expected_nodes()`, filtered against `already_covered`."""
    expected_all = stage1coverage.expected_nodes(conn, cluster_code, verse_ids, family)
    checklist_items = []
    for r in expected_all:
        covered_qs = already_covered.get(r["verse_reference"], {}).get(r["strong"], set())
        if r["question_code"] in covered_qs:
            continue
        checklist_items.append({
            "verse": r["verse_reference"], "strong": r["strong"],
            "question_code": r["question_code"]})
    return checklist_items


def _cost_estimate(ctx, instructions: str, content: str) -> dict:
    chars_per_token = float(ctx.cfg.setting("lexical.llm_chars_per_token", 4))
    est_input_tokens = int((len(instructions) + len(content)) / chars_per_token)
    max_output_tokens = int(ctx.cfg.setting("lexical.llm_max_output_tokens", 8000))
    rate_in = float(ctx.cfg.setting("lexical.llm_rate_input_per_million", 3.00))
    rate_out = float(ctx.cfg.setting("lexical.llm_rate_output_per_million", 15.00))
    est_cost = (est_input_tokens / 1_000_000 * rate_in) + (max_output_tokens / 1_000_000 * rate_out)
    return {"est_input_tokens": est_input_tokens, "max_output_tokens": max_output_tokens,
           "est_cost_usd": round(est_cost, 4)}


def assemble_word_level_batch_package(ctx, cluster_code: str, verse_ids: list[int],
                                      force: bool = False) -> dict:
    """`lexical.meaning`'s package (#1860): M0.1 (Name and Naming) + M0.5 (Lexical and Semantic
    Analysis). One chunk, capped by the caller. Never calls the network: returns the package plus a
    pre-call cost estimate.

    `force` (a -Force reconciliation rerun): skips the `already_covered` filter (the checklist is the
    full expected set) and omits each verse's `already_covered` field."""
    conn = ctx.db.conn
    scan = _scan_verses(conn, cluster_code, verse_ids)
    verses_out = _build_verses_out(verse_ids, scan, include_elevation=False)
    all_m_code_strongs = scan["all_m_code_strongs"]

    meaning_by_strong = {s: _meaning_sources(conn, s) for s in sorted(all_m_code_strongs)}
    already_covered = _apply_already_covered(conn, verses_out, force)
    checklist_items = _build_checklist(conn, cluster_code, verse_ids, already_covered, "word_level")

    questions = conn.execute(
        "SELECT question_code, question_text FROM wa_obs_question_catalogue "
        "WHERE deleted=0 AND (question_code LIKE 'M0.1%' OR question_code LIKE 'M0.5%') "
        "ORDER BY question_code").fetchall()
    question_texts = [{"question_code": q["question_code"], "question_text": q["question_text"]}
                      for q in questions]

    tag_values = tags_for_stage(ctx.cfg, "verse-reading", [r["value"] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='ib_observation.tag' AND inactive=0 "
        "ORDER BY ordinal")])

    rules = conn.execute(
        "SELECT rule_key, rule_text FROM cfg_method_rule WHERE step='lexical.meaning' "
        "AND active=1 ORDER BY ordinal").fetchall()
    rules_text = "\n".join(f"- {r['rule_key']}: {r['rule_text']}" for r in rules)

    instructions = _word_level_instructions(
        cluster_code, question_texts, tag_values, rules_text,
        [v["verse"] for v in verses_out], sorted(all_m_code_strongs), len(checklist_items), ctx.cfg)
    content = json.dumps({"cluster_code": cluster_code, "verses": verses_out,
                          "meaning_sources_by_strong": meaning_by_strong,
                          "expected_items": checklist_items},
                         ensure_ascii=False)
    cost = _cost_estimate(ctx, instructions, content)

    return {
        "instructions": instructions, "content": content, "verse_ids": verse_ids,
        "cluster_code": cluster_code, "verse_count": len(verses_out),
        "cluster_member_strong_count": len(scan["cluster_member_strongs"]),
        "word_battery_strong_count": len(all_m_code_strongs),
        "expected_item_count": len(checklist_items),
        "model": ctx.cfg.required_setting("lexical.llm_model"), **cost,
    }


def assemble_relational_batch_package(ctx, cluster_code: str, verse_ids: list[int],
                                      force: bool = False) -> dict:
    """`lexical.relational`'s package (#1860): M0.6.5, M0.6.6, D7.7.1, M0.7.1-16, M0.8.1. The caller
    (`handlers/lexical.py:relational`) must already have passed
    `stage1coverage.missing_word_level_coverage`; this function does not re-check it.
    `word_level_findings_by_verse` (the primary grounding) is sent alongside
    `meaning_sources_by_strong` (the raw lexicon), never one instead of the other."""
    conn = ctx.db.conn
    scan = _scan_verses(conn, cluster_code, verse_ids)
    verses_out = _build_verses_out(verse_ids, scan, include_elevation=True)
    all_m_code_strongs = scan["all_m_code_strongs"]
    verse_refs = [v["verse"] for v in verses_out]

    meaning_by_strong = {s: _meaning_sources(conn, s) for s in sorted(all_m_code_strongs)}
    word_level_findings = _word_level_findings(conn, verse_refs)
    prior_relational = _prior_relational_context(conn, verse_refs)
    prior_network = _prior_network_context(conn, verse_refs)
    already_covered = _apply_already_covered(conn, verses_out, force)
    checklist_items = _build_checklist(conn, cluster_code, verse_ids, already_covered, "relational")

    questions = conn.execute(
        "SELECT question_code, question_text FROM wa_obs_question_catalogue "
        "WHERE deleted=0 AND (question_code LIKE 'M0.7%' "
        "OR question_code IN ('D7.7.1', 'M0.6.5', 'M0.6.6', 'M0.8.1')) "
        "ORDER BY question_code").fetchall()
    question_texts = [{"question_code": q["question_code"], "question_text": q["question_text"]}
                      for q in questions]

    tag_values = tags_for_stage(ctx.cfg, "verse-reading", [r["value"] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='ib_observation.tag' AND inactive=0 "
        "ORDER BY ordinal")])

    rules = conn.execute(
        "SELECT rule_key, rule_text FROM cfg_method_rule WHERE step='lexical.relational' "
        "AND active=1 ORDER BY ordinal").fetchall()
    rules_text = "\n".join(f"- {r['rule_key']}: {r['rule_text']}" for r in rules)

    instructions = _relational_instructions(
        cluster_code, question_texts, tag_values, rules_text,
        verse_refs, sorted(all_m_code_strongs), len(checklist_items), ctx.cfg)
    content = json.dumps({"cluster_code": cluster_code, "verses": verses_out,
                          "meaning_sources_by_strong": meaning_by_strong,
                          "word_level_findings_by_verse": word_level_findings,
                          "prior_relational_context_by_verse": prior_relational,
                          "prior_network_context_by_verse": prior_network,
                          "expected_items": checklist_items},
                         ensure_ascii=False)
    cost = _cost_estimate(ctx, instructions, content)

    return {
        "instructions": instructions, "content": content, "verse_ids": verse_ids,
        "cluster_code": cluster_code, "verse_count": len(verses_out),
        "cluster_member_strong_count": len(scan["cluster_member_strongs"]),
        "expected_item_count": len(checklist_items),
        "model": ctx.cfg.required_setting("lexical.llm_model"), **cost,
    }


_RESPONSE_SHAPE = (
    "Respond with ONLY a JSON object, no other text, shaped exactly:\n"
    '{"observations": [{"strong": "...", "question_code": "..." or null, "tag": "...", '
    '"obs_text": "...", "meaning_source": "...", "meaning_keywords": ["...", "..."] or null, '
    '"occurrences": [{"verse": "...", "surface": "...", "morph_code": "..."}]}]}'
)


def _checklist_boilerplate(expected_item_count: int) -> str:
    return (
        f"`expected_items` IS THE AUTHORITATIVE CHECKLIST -- read it before writing anything. It "
        f"lists, pre-computed from live data, EXACTLY the {expected_item_count} (verse, strong, "
        f"question_code) triples this batch must answer -- every population/gating rule described "
        f"below has ALREADY been applied to build this list. Do not re-derive the population "
        f"yourself from the prose rules -- they explain WHY each entry is there, `expected_items` "
        f"is the authoritative WHAT. Your `observations` array MUST contain exactly one entry per "
        f"`expected_items` triple: same count, same (strong, question_code) pairs for the correct "
        f"verse -- no fewer (a triple you skip is a real gap, even one you judge inapplicable: "
        f"answer it with the question's own 'record none'/could-not-resolve convention instead of "
        f"omitting it) and no more (never add a (verse, strong, question_code) combination not "
        f"listed in `expected_items`).\n\n")


def _word_level_instructions(cluster_code: str, questions: list[dict], tag_values: list[str],
                             rules_text: str, verse_refs: list[str],
                             all_m_code_strongs: list[str], expected_item_count: int, cfg) -> str:
    """`lexical.meaning`'s prompt (#1860): M0.1 (Name and Naming) + M0.5 (Lexical and Semantic
    Analysis)."""
    q_text = "\n".join(f"- {q['question_code']}: {q['question_text']}" for q in questions)
    tag_guidance_text = guidance_block(cfg, tag_values)
    return (
        f"You are producing word-level verse-reading observations for cluster {cluster_code}, "
        f"the pre-subgroup Layer 2 word-level pass (`lexical.meaning` -- the relational half of "
        f"this stage is a SEPARATE step, `lexical.relational`, run only after this one has fully "
        f"covered a verse). You are given, per verse: the verse's own base text, `roles_in_verse` "
        f"-- every role-bearing word in that verse, each carrying `cluster_codes` (the full set of "
        f"M-code and role-T-code tags) -- and, per verse where applicable, `already_covered` -- "
        f"{{strong: [question_codes]}} already live for THAT verse (any pass) -- do not re-answer "
        f"a strong+question pair already listed there. You are also given "
        f"`meaning_sources_by_strong` for {all_m_code_strongs} (every M-code strong in this batch, "
        f"not just this cluster's own member strongs). Read all present meaning sources as "
        f"complementary evidence, never picking one and ignoring the others.\n\n"
        + _checklist_boilerplate(expected_item_count) +
        f"Method rules governing this task:\n{rules_text}\n\n"
        f"M0.1/M0.5 (word-level battery): answer for EVERY M-code strong present in "
        f"`roles_in_verse` for each verse, EXCEPT any (strong, question_code) pair already listed "
        f"in that verse's own `already_covered` (skip those, another pass already answered them "
        f"for this exact verse). SPAN-GROUNDED, NOT GENERIC (researcher, 2026-09-23): your answer "
        f"must be resolvable ONLY by looking at THIS occurrence's own surface/morph_code within "
        f"THIS verse -- if you could answer it identically without ever reading the verse (a bare "
        f"dictionary fact about the lemma), you have answered the wrong question. Two genuinely "
        f"different occurrences of the same strong may legitimately produce the same or different "
        f"answers; that is decided by what each occurrence actually shows, never assumed either "
        f"way in advance. ACTIVELY ENGAGE WITH THE SURFACE FORM (researcher, 2026-09-23): "
        f"`surface` and `morph_code` are given for THIS occurrence, not as bookkeeping -- if this "
        f"word's actual rendering/inflection here is not the term's most typical or expected form, "
        f"that is a real signal, not noise: a translator chose that specific rendering because the "
        f"verse's own context called for it. Treat a marked or unusual surface form as a direct "
        f"prompt to look harder at what THIS context is doing differently, the same way M0.5.11 "
        f"already asks you to notice when an occurrence's sense diverges from the term's usual "
        f"one -- the surface form is often the visible trace of exactly that divergence, not a "
        f"separate fact to ignore while answering the meaning question.\n\n"
        f"Answer these catalogue questions:\n{q_text}\n\n"
        f"Valid `tag` values: {tag_values}\n"
        f"{tag_guidance_text}\n\n"
        f"STRICT BOUNDARIES — do not exceed this task:\n"
        f"- You are given exactly {len(verse_refs)} verse(s), listed at the end of this message. "
        f"Every `verse` value you write MUST be one of exactly those.\n"
        f"- Every `strong` value you write must be any M-code strong actually present in that "
        f"verse's own `roles_in_verse` (any `cluster_codes` entry starting with \"M\") -- minus "
        f"whatever that verse's own `already_covered` already lists.\n"
        f"- `question_code` MUST be the exact, specific leaf code (e.g. \"M0.1.2\", \"M0.5.7\") — "
        f"NEVER a bare component code (\"M0.1\", \"M0.5\" are not valid, will be rejected, and "
        f"waste your own output). One observation per specific sub-question.\n"
        f"- If a genuine 'couldn't resolve' case arises, use tag `could-not-resolve` and state in "
        f"`obs_text` what signal suggests it should be resolvable with further analysis. If the "
        f"verse's own content is insufficient and an adjacent verse would help, use tag "
        f"`needs_adjacent_verse_context` and state explicitly in `obs_text` what's outstanding and "
        f"what the follow-up cross-check needs to establish (never a bare flag with no reason).\n"
        f"- Leave `meaning_keywords` null -- M0.1/M0.5 identity is resolved structurally (same "
        f"verse + same question_code = same fact, by construction), never by keyword matching.\n"
        f"- Do not add fields beyond the shape below, no prose before or after the JSON.\n\n"
        f"Verses in this batch: {verse_refs}\n\n" + _RESPONSE_SHAPE
    )


def _relational_instructions(cluster_code: str, questions: list[dict], tag_values: list[str],
                             rules_text: str, verse_refs: list[str],
                             all_m_code_strongs: list[str], expected_item_count: int, cfg) -> str:
    """`lexical.relational`'s prompt (#1860): M0.6.5, M0.6.6, D7.7.1, M0.7.1-16, M0.8.1. Every verse in
    scope has passed the readiness gate; its word-level findings are given as
    `word_level_findings_by_verse`."""
    q_text = "\n".join(f"- {q['question_code']}: {q['question_text']}" for q in questions)
    tag_guidance_text = guidance_block(cfg, tag_values)
    return (
        f"You are producing relational verse-reading observations for cluster {cluster_code}, "
        f"the pre-subgroup Layer 2 relational pass (`lexical.relational` -- the word-level half of "
        f"this stage, `lexical.meaning`, has ALREADY run for every verse in this batch; its "
        f"committed findings are your primary grounding). You are given, per verse: the verse's "
        f"own base text, `roles_in_verse` -- every role-bearing word in that verse, each carrying "
        f"`cluster_codes` (the full set of M-code and role-T-code tags) and `is_home_cluster` "
        f"(true if this word belongs to cluster {cluster_code} -- informational only: every "
        f"question here is answered for every M-code word in the verse regardless) -- "
        f"`word_level_findings_by_verse` -- the COMMITTED M0.1/M0.5 findings for each M-code "
        f"strong in this verse (from `lexical.meaning`) -- your PRIMARY grounding for what each "
        f"word actually means here, read before reasoning about its relations -- "
        f"`meaning_sources_by_strong` -- the raw lexicon (strong_meaning_tree/lsj/mounce) for the "
        f"same strongs, complementary evidence alongside the committed findings, never a "
        f"substitute for them -- `prior_relational_context_by_verse` -- any M0.6.5 relational "
        f"findings ALREADY recorded for these verses by an earlier pass, any cluster -- "
        f"`prior_network_context_by_verse` -- any M0.6.6 whole-network findings already recorded "
        f"(a SEPARATE stream from M0.6.5's own chain) -- and, per verse where applicable, "
        f"`already_covered` -- {{strong: [question_codes]}} already live for THAT verse (any "
        f"pass) -- do not re-answer a strong+question pair already listed there: a later cluster's "
        f"pass over a verse another pass already fully read must not re-derive it.\n\n"
        + _checklist_boilerplate(expected_item_count) +
        f"Method rules governing this task:\n{rules_text}\n\n"
        f"- M0.6.5 (relational), M0.6.6 (whole-network), and D7.7.1 (operation-permeability): "
        f"answer for EVERY M-code strong present in `roles_in_verse` for each verse (cluster-"
        f"agnostic, NOT restricted to this cluster's own home strong(s)), EXCEPT any (strong, "
        f"question_code) pair already listed in that verse's own `already_covered`. For M0.6.5: if "
        f"`prior_relational_context_by_verse` already has an entry for this verse (from any "
        f"strong), your answer for a NEW strong MUST build on it where relevant -- add THIS word's "
        f"own vantage point, never repeat what's already there; with no prior entry, start the "
        f"relational chain. For M0.6.6: the same progressive rule applies against "
        f"`prior_network_context_by_verse` instead -- extend or correct an existing sketch of the "
        f"verse's whole M-code network with what THIS word's own membership in it adds, never "
        f"restate it unchanged; record none for a word that is the verse's only M-code element "
        f"(still answer it, the finding is just \"none\", never skip the question entirely). "
        f"D7.7.1: record none if no operation-tagged (role-T3) word is present in the verse at all "
        f"-- the question's only actual gate; do not additionally require a specifically "
        f"party-coded (T4/T7/T8/T9) word, the live tagging for that is sparse and would wrongly "
        f"exclude real cases (e.g. a plain T2-tagged \"God\" or \"others\" is still a real party "
        f"for this question's purposes).\n"
        f"- M0.7.1-16 (verse substantiation, `#1806`, 2026-09-21): answer for EVERY M-code strong "
        f"present in `roles_in_verse` for each verse -- the SAME population as M0.6.5/M0.6.6/"
        f"D7.7.1 above -- EXCEPT any (strong, question_code) pair already listed in that verse's "
        f"own `already_covered`. These questions are deliberately written about \"[this word]\", "
        f"never about \"the characteristic\" -- you are not told, and must not assume, which "
        f"cluster's pass is asking; answer purely from what the word and its relationships in the "
        f"verse actually show. The same word can genuinely behave differently verse to verse, so a "
        f"strong already having M0.7 answers from OTHER verses is never itself a reason to skip "
        f"THIS verse. But THIS verse+strong+question, once genuinely answered (by any pass), is "
        f"settled -- `already_covered` is what tells you that, not your own judgement.\n"
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
        f"- Every `strong` value you write for M0.6.5/M0.6.6/D7.7.1/M0.7.1-16 must be any M-code "
        f"strong actually present in that verse's own `roles_in_verse` -- minus whatever that "
        f"verse's own `already_covered` already lists. D7.7.1 only applies when an operation-"
        f"tagged (role-T3) word is actually present in the verse -- no additional party-tag "
        f"requirement. For M0.8.1, `strong` must be one of that verse's own "
        f"`elevation_candidate_words` ONLY (never an M-code strong) -- if a verse has no "
        f"`elevation_candidate_words` field, do not answer M0.8.1 for it at all.\n"
        f"- `question_code` MUST be the exact, specific leaf code (e.g. \"M0.6.5\", \"M0.7.3\") — "
        f"NEVER a bare component code. One observation per specific sub-question.\n"
        f"- If a genuine 'couldn't resolve' case arises, use tag `could-not-resolve` and state in "
        f"`obs_text` what signal suggests it should be resolvable with further analysis. If the "
        f"verse's own content is insufficient and an adjacent verse would help, use tag "
        f"`needs_adjacent_verse_context` and state explicitly in `obs_text` what's outstanding and "
        f"what the follow-up cross-check needs to establish (never a bare flag with no reason).\n"
        f"- For M0.7.1-16 ONLY, also fill `meaning_keywords`: 2-5 short key terms/concepts "
        f"capturing the core of your answer (e.g. [\"conditional-change\", \"unfruitful-to-"
        f"fruitful\"], not full phrases) -- used downstream to recognise when two occurrences "
        f"genuinely show the same finding (escalation #1824), separate from your own obs_text "
        f"wording. Leave `meaning_keywords` null for every other question type (M0.6.5/M0.6.6/"
        f"D7.7.1/M0.8.1) -- their identity is resolved structurally (same verse + same "
        f"question_code = same fact, by construction), never by keyword matching.\n"
        f"- Do not add fields beyond the shape below, no prose before or after the JSON.\n\n"
        f"Verses in this batch: {verse_refs}\n\n" + _RESPONSE_SHAPE
    )
