"""surface_cycle_schema_2361_v1_20261106.py -- escalation #2361, stage 1a: the tables and the config of the surface cycle.

Design v3 (outputs/escalation/2361-surface-cycle-registration-design-v3-20261106.md), the researcher's rulings of 2026-11-06:
extend or re-grain existing tables, repeat no data, document every table and column so the cycle is unambiguous.

  RE-GRAINED   surface_pair_verdict (0 rows, never written) becomes surface_term, one row per distinct surface text. The old
               table's config rows, enums and grant are retired and the physical table dropped (refused if it holds a row).
  RETIRED      surface_subgroup.surface_group (empty in every row, read by no routine): it would repeat the group of
               surface_term on every pair. Config row and enums removed, physical column dropped.
  EXTENDED     run (settings_snapshot, counts), run_batch (model_role, model, calls, secs), file_manifest (module, run_id,
               sha256, analytic_status, migrated_from). Columns added with ALTER TABLE and registered in cfg_column.
  NEW (data)   surface_derivation, collection, collection_link, collection_listing, surface_flag, surface_event,
               surface_eval_case, ai_call.
  NEW (config) cfg_base_construct, cfg_ai_prompt, cfg_ai_model (rule tables, with their cfg_table_purpose rows).
Every cfg_* write goes through configmaint.apply_logged(); the physical tables are built from their cfg_column rows
(lib/db.table_ddl). A named rollback snapshot is taken before a live apply. Idempotent. One transaction. Writes no data row.

Usage:
    python iba/app/migration/surface_cycle_schema_2361_v1_20261106.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import table_ddl  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2361-SURFACE-CYCLE-SCHEMA-20261106"
MODULE = "surface_cycle_schema_2361_v1_20261106"
SOURCE = "escalation #2361, design v3 of 2026-11-06 (the researcher's rulings of 2026-11-06)"
FILLED = ("the stage 1b loader (iba/app/migration/archive/surface_cycle_load_2361_v1_20261106.py) for the recorded work of "
          "2026-10-31 to 2026-11-05; after that the step of the module named in the column note (stages 2 to 5 of #2361)")
NOW = "(strftime('%Y-%m-%dT%H:%M:%SZ','now'))"
WHO = "who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool)"

# ---- enums (cfg_enum name -> values, each value defined in the note of the column that uses the enum) ----------------
ENUMS = {
    "surface_cycle_module": ["group", "structure", "ai_base", "resolve", "collection"],
    "ai_role": ["judge", "embed", "embed_fast", "quick", "reviewer"],
    "surface_term.form": ["word", "phrase"],
    "surface_term.origin": ["surface", "computed"],
    "surface_term.surface_group": ["behaviour", "inner_being_state", "being", "other"],
    "surface_term.group_state": ["unjudged", "judged", "failed", "corrected", "confirmed"],
    "surface_term.base_source": ["structure", "sibling", "ollama", "own", "researcher"],
    "surface_term.base_state": ["out_of_scope", "phrase_not_tested", "unmatched", "matched_structure", "matched_sibling",
                                "lead_only", "ai_answered", "ai_none", "ai_failed", "resolved_own", "resolved", "flagged",
                                "confirmed"],
    "surface_term.collection_state": ["untouched", "placed", "set_aside", "listed_only", "shared"],
    "surface_derivation.method": ["structure", "sibling", "ollama", "own", "researcher"],
    "surface_derivation.kind": ["inflection", "derivation", "lead_opposite", "lead_other", "lead_starts_with", "own"],
    "cfg_base_construct.direction": ["same", "candidate"],
    "collection.status": ["indicative", "confirmed", "merged", "retired"],
    "collection_link.tier": ["core", "synonym", "opposite", "possible_opposite", "associated", "set_aside"],
    "collection_listing.kind": ["synonym", "opposite"],
    "collection_listing.outcome": ["bound", "refused", "not_in_pool", "unjudged"],
    "surface_subject_kind": ["surface_term", "surface_derivation", "collection", "collection_link"],
    "surface_flag.kind": ["possible_opposite", "meaning_shift", "held_pair", "ai_failed", "ai_none", "ai_disagrees",
                          "possessive", "structure_conflict", "junk_surface", "other"],
    "surface_flag.status": ["open", "settled"],
    "surface_event.action": ["confirm", "correct", "move", "remove", "merge", "retire", "reopen", "set_tier", "set_group",
                             "set_base", "mark_deleted"],
    "surface_eval_case.source": ["researcher", "claude", "prototype"],
    "surface_eval_case.standing": ["provisional", "confirmed"],
    "ai_call.outcome": ["answered", "refused", "failed", "halted"],
    "cfg_ai_prompt.status": ["draft", "active", "retired"],
    "cfg_ai_model.status": ["active", "retired"],
    "file_manifest.analytic_status": ["live", "regenerable"],
}


def c(name, typ, use, *, pk=0, nn=0, dflt=None, fk=None, exp=None):
    return {"name": name, "type": typ, "use": use, "pk": pk, "nn": nn, "dflt": dflt, "fk": fk, "exp": exp}


def tail(prefix):
    """The columns every data table of the cycle ends with."""
    return [
        c("run_id", "TEXT", "the run that wrote the row (run.run_id); for a row loaded from a recorded file, the load run. "
          "Navigate: run, then run_batch for the batch, then ai_call for the model calls"),
        c("created_at", "TEXT", "when (ISO-8601 UTC)", nn=1, dflt=NOW),
        c("updated_at", "TEXT", "when last changed (ISO-8601 UTC)"),
        c("created_by", "TEXT", WHO, nn=1, dflt="'direct edit'"),
        c("deleted", "INTEGER", "soft delete, version-aware as in verse_lexical: 1 when the row is no longer the current one "
          "(superseded, removed or junk); nothing in this cycle is ever physically deleted", nn=1, dflt="0"),
        c("load_ref", "TEXT", "for a row loaded from a recorded file of the prototyping work: the file and line it came from "
          "(for example collection/import/judge-v4-20261105.jsonl#17); NULL for a row made by a step. Answers: where did "
          "this value come from"),
    ]


def pk():
    return c("id", "INTEGER", "surrogate PK", pk=1, nn=1)


# ---- the tables --------------------------------------------------------------------------------------------------------
# name -> dict(category, grain, use, cols, unique, indexes, purpose, success)
T = {}

T["surface_term"] = dict(
    category="data", grain="one row per distinct English surface text, and per computed base word",
    use=("Module 0-5 hub of the surface cycle (#2361). The one table that holds what is judged about a surface TEXT: its group "
         "(module 1), its base (modules 2 to 4) and, as a base, its state in the collections (module 5). The surface text is "
         "lower-cased and trimmed, the same key as verse_lexical.surface and surface_subgroup.surface, so those join to this "
         "table by text; nothing here is repeated on a (Strong's code, surface) pair, because the judgements are made on the "
         "text alone (ruling of 2026-11-02). A base is itself a row (base_id points to a row of this table), so there is no "
         "separate base table. Re-grained from the empty surface_pair_verdict. Everything the models decided is inferential "
         "(B:4) until its state is confirmed. Read it with Surface-* show steps; the evidence is in surface_derivation and "
         "ai_call"),
    cols=[
        pk(),
        c("surface", "TEXT", "the English surface text, lower-cased and trimmed, exactly as verse_lexical.surface and "
          "surface_subgroup.surface carry it; unique among live rows. For origin computed, a base word made by the structure "
          "module from sibling roots (for example adulter) that is not itself a surface of the corpus", nn=1),
        c("form", "TEXT", "word (one word) or phrase (more than one word). A phrase is not tested by the structure or base "
          "modules and is assigned to collections last (ruling D2)", nn=1, exp="enum.surface_term.form"),
        c("origin", "TEXT", "surface (found in the corpus text) or computed (a base word the structure module computed that "
          "is not a surface); a computed term is never in verse_lexical", nn=1, dflt="'surface'",
          exp="enum.surface_term.origin"),
        c("surface_group", "TEXT", "Module 1 of 5, group: the current group of the surface, resolved from the live decisions "
          "(ai_call, surface_event) by the order in cfg_setting surfaces.group_resolve_order. behaviour and inner_being_state "
          "are the study of the inner being (collection a: bases and collections are built for them); being is the entities "
          "(collection b); other is everything else (collection c); b and c stay untouched until the researcher assesses "
          "them. NULL until judged. Inferential (B:4) until group_state is confirmed",
          exp="enum.surface_term.surface_group"),
        c("group_reason", "TEXT", "Module 1 of 5: the judge's one-line reason for the current group, or the reason of a "
          "correction or of the researcher"),
        c("group_judged_by", "TEXT", "Module 1 of 5: what decided the current group: the model name with its tag as in "
          "cfg_ai_model at the time, rule:<name> for a rule, or researcher. The call is ai_call where "
          "subject_kind = surface_term and subject_id = this id"),
        c("group_state", "TEXT", "Module 1 of 5, the state of the group: unjudged (no answer yet); judged (the judge answered); "
          "failed (tried, no usable answer, tried again by the next run); corrected (changed after judging by a correction "
          "step or rule, see surface_event); confirmed (the researcher confirmed it)", nn=1, dflt="'unjudged'",
          exp="enum.surface_term.group_state"),
        c("base_id", "INTEGER", "Module 4 of 5, resolve: points to surface_term.id, a row of THIS table: the term that is "
          "this surface's base (sins to sin). A surface that is its own base points to itself. NULL until resolved and for a "
          "phrase. Navigate: the evidence for the base is surface_derivation where term_id = this id; the surfaces that share "
          "this base are the rows whose base_id is the same; the collections of a base are collection_link where "
          "term_id = the base's id", fk="surface_term.id"),
        c("base_source", "TEXT", "Module 4 of 5: what kind of evidence made the current base: structure (a construct of "
          "cfg_base_construct), sibling (roots that share a computed base), ollama (the AI base), own (no other evidence: the "
          "surface is its own base), researcher (set by hand). Resolved by the order in cfg_setting "
          "surfaces.base_resolve_order. NULL while base_id is NULL", exp="enum.surface_term.base_source"),
        c("base_state", "TEXT", "Modules 2 to 4, the state of the base work: out_of_scope (the group is being or other, or the "
          "surface is not yet judged into the study); phrase_not_tested (a phrase, assigned last); unmatched (in scope, no "
          "evidence yet); matched_structure (a construct matched a base); matched_sibling (roots share a computed base); "
          "lead_only (only a lead, such as a possible opposite, no accepted base); ai_answered (the AI gave a base); ai_none "
          "(the AI said it has no base of the same root meaning); ai_failed (tried, no usable answer); resolved_own (no "
          "evidence, so it is its own base); resolved (a base is resolved from evidence); flagged (an open surface_flag "
          "needs the researcher); confirmed (the researcher confirmed the base)", nn=1, dflt="'out_of_scope'",
          exp="enum.surface_term.base_state"),
        c("collection_state", "TEXT", "Module 5 of 5, collect: the state of this term AS A BASE in the collections: untouched "
          "(in no collection and not listed), placed (a live collection_link of tier core, synonym or opposite), set_aside "
          "(the model listed it for a collection and the judge would not bind it), listed_only (only an associated or "
          "possible-opposite link), shared (placed in two or more collections: the exception). NULL when the term is not a "
          "base. Written in the same transaction as the link that changes it and proved equal to collection_link by the "
          "check step", exp="enum.surface_term.collection_state"),
    ] + tail("surface_term"),
    unique=["surface"], indexes=[("idx_surface_term_base_id", ["base_id"]), ("idx_surface_term_group", ["surface_group"]),
                                 ("idx_surface_term_base_state", ["base_state"])],
)

T["surface_derivation"] = dict(
    category="data", grain="one piece of evidence for the base of one surface (append-only)",
    use=("Modules 2 and 3 of 5, structure and AI base (#2361): the evidence from which the base of a surface is resolved. One "
         "row for a construct that matched, a sibling group, an AI answer, the 'own' default or a researcher's setting, and "
         "for each lead (a possible opposite). A new run adds rows and flips the superseded ones to deleted = 1; nothing is "
         "overwritten. base-resolve reads the live accepted rows to set surface_term.base_id. Navigate: term_id to the "
         "surface, base_term_id to its base, ai_call_id to the model call"),
    cols=[
        pk(),
        c("term_id", "INTEGER", "points to surface_term.id: the surface this evidence is about", nn=1, fk="surface_term.id"),
        c("method", "TEXT", "what produced the evidence: structure (a construct rule), sibling (roots sharing a computed "
          "base), ollama (the AI base), own (the default), researcher", nn=1, exp="enum.surface_derivation.method"),
        c("evidence", "TEXT", "the identity of the evidence: the cfg_base_construct.id for structure (for example C04), the "
          "sibling group (S0003) for sibling, the ai_call id for ollama, a note for researcher"),
        c("kind", "TEXT", "inflection (only the ending changes), derivation (a different form with the same root meaning), "
          "lead_opposite (a negating prefix or suffix: a possible opposite, never accepted as a base), lead_other (another "
          "prefix kept as a lead), lead_starts_with (the surface starts with another surface), own (the surface is its own "
          "base)", nn=1, exp="enum.surface_derivation.kind"),
        c("base_word", "TEXT", "the base word the evidence points to, as text (it may not yet be a surface_term row)", nn=1),
        c("base_term_id", "INTEGER", "points to surface_term.id: the base as a term, once the term exists (a computed base "
          "gets a term of origin computed); NULL until then", fk="surface_term.id"),
        c("accepted", "INTEGER", "1 when this evidence is used to make the base, 0 for a lead or for evidence the resolve "
          "order did not use", nn=1, dflt="0"),
        c("ai_call_id", "INTEGER", "points to ai_call.id: the model call behind an ollama row; NULL for the other methods",
          fk="ai_call.id"),
    ] + tail("surface_derivation"),
    unique=None, indexes=[("idx_surface_derivation_term", ["term_id"]), ("idx_surface_derivation_base_word", ["base_word"]),
                          ("idx_surface_derivation_method", ["method"])],
)

T["collection"] = dict(
    category="data", grain="one row per collection (a seed word and the bases gathered round it)",
    use=("Module 5 of 5, collect (#2361): a collection of bases of like meaning, named for its core word, built progressively "
         "(ruling D3). It is the finer step before a concept: collection.concept_id points to concept.id and is NULL until "
         "the rollup of collections into concepts, which will replace concept_subgroup. The members are collection_link rows. "
         "The named opposite pole of the core word (a helper list) is held in the pole_* columns. Provisional until "
         "status is confirmed; inferential (B:4)"),
    cols=[
        pk(),
        c("core_term_id", "INTEGER", "points to surface_term.id: the base that is the seed (core) of the collection; unique "
          "among live collections", nn=1, fk="surface_term.id"),
        c("name", "TEXT", "the collection's name, normally its core word", nn=1),
        c("status", "TEXT", "indicative (made by a run, not reviewed), confirmed (the researcher confirmed it), merged (merged "
          "into merged_into_id, which holds its members), retired (no longer used)", nn=1, dflt="'indicative'",
          exp="enum.collection.status"),
        c("merged_into_id", "INTEGER", "points to collection.id: the collection this one was merged into; NULL otherwise",
          fk="collection.id"),
        c("concept_id", "INTEGER", "points to concept.id: the concept this collection rolls up into; NULL until the rollup of "
          "collections into concepts (ruling D1), which replaces concept_subgroup", fk="concept.id"),
        c("pole_word", "TEXT", "the opposite pole of the core word, as the model named it (love: hate); NULL when none"),
        c("pole_of_pole", "TEXT", "the model's answer when asked for the opposite of the pole; a pole is reciprocal when it "
          "comes back to the core word or a synonym of it"),
        c("pole_reciprocal", "INTEGER", "1 when the pole of the pole returns to the core word, 0 when not, NULL when there is "
          "no pole. An opposite joins the collection only when this is 1 and the wording judge agrees"),
        c("pole_real_word", "INTEGER", "1 when the pole is a real English word (in the ESV vocabulary or confirmed by the "
          "dictionary check), 0 when not (for example dispray), NULL when there is no pole"),
    ] + tail("collection"),
    unique=["core_term_id"], indexes=[("idx_collection_concept", ["concept_id"])],
)

T["collection_link"] = dict(
    category="data", grain="one row per (collection, term) placement or listing",
    use=("Module 5 of 5, collect (#2361): where a base stands in a collection and why. The tier says how it relates: core (the "
         "seed), synonym, opposite (confirmed by two judges), possible_opposite and associated (listed apart for the "
         "researcher, not members), set_aside (the model listed it and the judge would not bind it). A change is a new row; "
         "the row it replaces gets deleted = 1 and superseded_by_id, as in verse_lexical, so the history can be read. A term "
         "live in two collections is the exception and is flagged shared. Navigate: collection_id to the collection, term_id "
         "to the base and its surfaces, ai_call_id to the judgement"),
    cols=[
        pk(),
        c("collection_id", "INTEGER", "points to collection.id", nn=1, fk="collection.id"),
        c("term_id", "INTEGER", "points to surface_term.id: the base placed or listed (a base is a term)", nn=1,
          fk="surface_term.id"),
        c("tier", "TEXT", "core (the seed), synonym (means the same as the core word, judged against the core word only), "
          "opposite (the other pole, accepted only when the wording judge and the named-pole judge agree), possible_opposite "
          "(one judge only: for the researcher, not a member), associated (the same matter seen from another side: listed "
          "apart, not a member), set_aside (listed by the model, not bound by the judge: studied separately)", nn=1,
          exp="enum.collection_link.tier"),
        c("superseded_by_id", "INTEGER", "points to collection_link.id: the row that replaced this one; NULL for a live row "
          "and for a removal with no replacement", fk="collection_link.id"),
        c("shared", "INTEGER", "1 when the term is live in two or more collections (the exception, counted in the tally)",
          nn=1, dflt="0"),
        c("ai_call_id", "INTEGER", "points to ai_call.id: the judgement that put the term here; NULL for the core row and "
          "for a researcher's setting", fk="ai_call.id"),
        c("reason", "TEXT", "the judge's short reason, or the researcher's"),
    ] + tail("collection_link"),
    unique=["collection_id", "term_id"], indexes=[("idx_collection_link_term", ["term_id"]),
                                                   ("idx_collection_link_tier", ["tier"])],
)

T["collection_listing"] = dict(
    category="data", grain="one row per word the model listed for a collection",
    use=("Module 5 of 5, collect (#2361): a helper list. When a collection is started the model is asked to list the synonyms "
         "and the opposites of its core word; each listed word is kept here with what became of it, so a word the pool does "
         "not hold, or that the judge refused, is visible and can be revisited. Navigate: collection_id to the collection, "
         "term_id to the word as a term when it is one"),
    cols=[
        pk(),
        c("collection_id", "INTEGER", "points to collection.id", nn=1, fk="collection.id"),
        c("word", "TEXT", "the word as the model listed it, lower-cased", nn=1),
        c("kind", "TEXT", "synonym or opposite: which list of the model it came from", nn=1,
          exp="enum.collection_listing.kind"),
        c("term_id", "INTEGER", "points to surface_term.id: the word as a base term; NULL when the pool holds no such word",
          fk="surface_term.id"),
        c("outcome", "TEXT", "bound (it became a member), refused (the judge would not bind it), not_in_pool (no such base in "
          "the study), unjudged (not yet put to the judge)", nn=1, dflt="'unjudged'", exp="enum.collection_listing.outcome"),
        c("ai_call_id", "INTEGER", "points to ai_call.id: the call that listed the word", fk="ai_call.id"),
    ] + tail("collection_listing"),
    unique=["collection_id", "word", "kind"], indexes=[("idx_collection_listing_term", ["term_id"])],
)

T["surface_flag"] = dict(
    category="data", grain="one row per exception to settle later",
    use=("Support for all modules (#2361): an item the work met and did not settle, for the researcher or a later run: a "
         "possible opposite found among the AI bases, a meaning-shifted derivation, a held pair, a failed or 'none' AI "
         "answer, a possessive base, a disagreement between the structure and the AI base. Thousands of per-item flags do "
         "not belong in the escalation table; where a flag needs a decision it carries the escalation id, and an escalation "
         "carries counts and a path, never the list (B:40). Settling a flag sets status settled and writes a surface_event"),
    cols=[
        pk(),
        c("subject_kind", "TEXT", "which table subject_id points into: surface_term, surface_derivation, collection or "
          "collection_link", nn=1, exp="enum.surface_subject_kind"),
        c("subject_id", "INTEGER", "the id of the row in the table named by subject_kind", nn=1),
        c("kind", "TEXT", "the kind of exception: possible_opposite (a negating prefix or suffix on an accepted AI base), "
          "meaning_shift (the base's meaning has moved), held_pair (a base held back from a repoint), ai_failed, ai_none, "
          "ai_disagrees (the AI base differs from the structure base), possessive (a possessive form kept apart from its "
          "base), structure_conflict, junk_surface, other", nn=1, exp="enum.surface_flag.kind"),
        c("note", "TEXT", "what was seen, in a line"),
        c("status", "TEXT", "open (not settled) or settled", nn=1, dflt="'open'", exp="enum.surface_flag.status"),
        c("escalation_id", "INTEGER", "the escalation.id of the item that carries the decision, when one was raised; NULL "
          "otherwise (not a foreign key: escalation keeps a row per version)"),
    ] + tail("surface_flag"),
    unique=["subject_kind", "subject_id", "kind"], indexes=[("idx_surface_flag_status", ["status"])],
)

T["surface_event"] = dict(
    category="data", grain="one row per revision of a surface, base, collection or link (append-only)",
    use=("Support for all modules (#2361): the record of every revision, so the work can be revisited and every change "
         "traced: who or what changed which value, from what to what, and why. Written in the same transaction as the "
         "change, by the researcher's edit steps and by a module that corrects its own earlier result. Follows the "
         "convention of the other change tables (ib_observation_change, narrative_claim_change). Read with show -Explain"),
    cols=[
        pk(),
        c("subject_kind", "TEXT", "which table subject_id points into", nn=1, exp="enum.surface_subject_kind"),
        c("subject_id", "INTEGER", "the id of the changed row in the table named by subject_kind", nn=1),
        c("action", "TEXT", "what was done: confirm, correct, move, remove, merge, retire, reopen, set_tier, set_group, "
          "set_base or mark_deleted", nn=1, exp="enum.surface_event.action"),
        c("field", "TEXT", "the column that changed, when one did"),
        c("value_before", "TEXT", "the value before the change, as text"),
        c("value_after", "TEXT", "the value after the change, as text"),
        c("by", "TEXT", "who or what made the change: Researcher, Claude, or the step name", nn=1),
        c("reason", "TEXT", "why, in the researcher's or the tool's words"),
    ] + tail("surface_event"),
    unique=None, indexes=[("idx_surface_event_subject", ["subject_kind", "subject_id"])],
)

T["surface_eval_case"] = dict(
    category="data", grain="one row per method test case",
    use=("Support for all modules (#2361): the cases a prompt, a threshold or a model is tested against (for example the 53 "
         "opposite pairs, the true and false synonym pairs, the researcher's human-test labels). They come from the "
         "prototyping and are IN-PROGRESS work that may not reflect the ultimate decision (the researcher, 2026-11-06): every "
         "case is provisional until the researcher confirms it, a report says 'against provisional cases', and they inform "
         "a comparison and never gate, activate or decide anything. Results of a test are ai_call rows of a run of kind eval"),
    cols=[
        pk(),
        c("module", "TEXT", "which module the case tests", nn=1, exp="enum.surface_cycle_module"),
        c("step", "TEXT", "which step or question inside the module (for example synonym, opposite, pole)", nn=1),
        c("a", "TEXT", "the first word, or the surface tested", nn=1),
        c("b", "TEXT", "the second word of a pair; NULL when the case has one word"),
        c("expected", "TEXT", "the answer the case expects (for example synonym, opposite, distinct, or a group)", nn=1),
        c("source", "TEXT", "where the case came from: researcher (the researcher's own label), claude, or prototype (made "
          "during the prototyping)", nn=1, exp="enum.surface_eval_case.source"),
        c("standing", "TEXT", "provisional (in-progress work, the default) or confirmed (the researcher confirmed the case)",
          nn=1, dflt="'provisional'", exp="enum.surface_eval_case.standing"),
        c("note", "TEXT", "where the case is from or what it shows"),
    ] + tail("surface_eval_case"),
    unique=["module", "step", "a", "b"], indexes=[],
)

T["ai_call"] = dict(
    category="data", grain="one row per call to a model on the server (append-only)",
    use=("Support for all modules (#2361): the record of every use of zeta-assist (the Ollama server), so the use is visible, "
         "controlled and reproducible: which role and model, with the digest in force, which prompt version, which options "
         "(temperature, seed, context), the request and the answer, the outcome and the time. The only route to the server "
         "is lib/aiclient.py, which refuses a model or prompt that is not active and writes this row. The replay step "
         "re-sends request and compares; the compare step ranks prompt versions. Navigate: run_id to run, batch_id to "
         "run_batch, model_id to cfg_ai_model, prompt_id to cfg_ai_prompt, subject_kind and subject_id to the row judged"),
    cols=[
        pk(),
        c("batch_id", "INTEGER", "points to run_batch.id: the batch (cycle control) the call was made in; NULL for a single "
          "call", fk="run_batch.id"),
        c("module", "TEXT", "the module that made the call", nn=1, exp="enum.surface_cycle_module"),
        c("step", "TEXT", "the step inside the module (for example group, synonym, opposite, pole, score, listing)", nn=1),
        c("role", "TEXT", "the role asked for at the time (judge, embed, embed_fast, quick, reviewer); a role resolves to a "
          "model in settings, so a model is replaced in one place", nn=1, exp="enum.ai_role"),
        c("model_id", "INTEGER", "points to cfg_ai_model.id: the model that answered", nn=1, fk="cfg_ai_model.id"),
        c("model_digest", "TEXT", "the digest of the model at the time of the call, as the server reported it: the same name "
          "can be a different model after a pull"),
        c("prompt_id", "INTEGER", "points to cfg_ai_prompt.id: the exact prompt version used (its key, version, text and hash "
          "come from there); NULL for a call that has no prompt, such as an embedding", fk="cfg_ai_prompt.id"),
        c("options", "TEXT", "JSON of the options sent: temperature, seed, context size, format, reasoning on or off"),
        c("request_hash", "TEXT", "hash of the prompt with its variables filled in: two calls with the same request_hash, "
          "model digest and options should give the same answer (the reproducibility test)"),
        c("subject_kind", "TEXT", "which table subject_id points into", exp="enum.surface_subject_kind"),
        c("subject_id", "INTEGER", "the id of the row the call judged; NULL when it judged none (a listing of words)"),
        c("request", "TEXT", "the full request sent"),
        c("answer", "TEXT", "the full answer received"),
        c("result", "TEXT", "the usable value read from the answer (a group, a relation, a base word, a tier); NULL when the "
          "answer was not usable"),
        c("score", "REAL", "a number the answer gave (the closeness score), when the step asks for one"),
        c("via", "TEXT", "how a result was reached when more than one route exists (for example quick, score 8)"),
        c("outcome", "TEXT", "answered (a usable answer), refused (the tool's own check refused the answer), failed (no "
          "answer: error or timeout), halted (the run stopped after the set number of failures in a row)", nn=1,
          exp="enum.ai_call.outcome"),
        c("error", "TEXT", "the error, when the outcome is failed or refused"),
        c("tokens_in", "INTEGER", "prompt tokens the server counted"),
        c("tokens_out", "INTEGER", "answer tokens the server counted"),
        c("secs", "REAL", "seconds the call took"),
    ] + tail("ai_call"),
    unique=None, indexes=[("idx_ai_call_module_step", ["module", "step"]), ("idx_ai_call_prompt", ["prompt_id"]),
                          ("idx_ai_call_subject", ["subject_kind", "subject_id"]), ("idx_ai_call_run", ["run_id"])],
)

T["cfg_base_construct"] = dict(
    category="rule", grain="one row per construct rule of the word-structure matching",
    use=("Module 2 of 5, structure (#2361): the rules by which a surface is matched to a base by its shape: remove an ending "
         "(sins to sin), restore an e (abased to abase), undouble a consonant (begged to beg), remove a prefix. direction "
         "same means the base has the same meaning (accepted); candidate means the match is only a lead (a negating prefix: "
         "a possible opposite) and is never accepted as a base. Rebuilt from the recorded control of 2026-11-04 (79 rules) "
         "because the code that made it was never kept; the structure module applies exactly these rows"),
    cols=[
        c("id", "TEXT", "the construct's id as recorded (C01 for an ending, P79 for a prefix)", pk=1, nn=1),
        c("kind", "TEXT", "the kind of change in words (plural or 3rd person, past tense or participle, negating prefix, "
          "negating suffix, other prefix, and so on); the kinds negating prefix and negating suffix are what flag a possible "
          "opposite", nn=1),
        c("direction", "TEXT", "same (the base keeps the meaning, accepted) or candidate (only a lead, never a base)", nn=1,
          exp="enum.cfg_base_construct.direction"),
        c("strip", "TEXT", "the ending removed from the surface; empty when none", nn=1, dflt="''"),
        c("add", "TEXT", "the text added after removing the ending (for example e); empty when none", nn=1, dflt="''"),
        c("undouble", "INTEGER", "1 when a doubled final consonant is reduced to one (begg to beg)", nn=1, dflt="0"),
        c("strip_prefix", "TEXT", "the prefix removed from the front of the surface; empty when none", nn=1, dflt="''"),
        c("description", "TEXT", "the rule in words", nn=1),
        c("example", "TEXT", "an example (sins > sin)"),
        c("inactive", "INTEGER", "1 when the rule is switched off", nn=1, dflt="0"),
    ],
    unique=None, indexes=[],
    purpose=("The construct rules of the word-structure matching, in config, so the module that matches a surface to a base by "
             "its shape is driven by rows and a rule can be amended or switched off without a code change (#2361)."),
    success=("Applying the rows to the recorded input list reproduces the recorded result exactly: 1,386 hits, the status "
             "counts of both control versions, 681 unmatched single words, 47 sibling groups and 26 bases outside the list; "
             "every row is applied by the structure module and no construct is held anywhere else."),
)

T["cfg_ai_prompt"] = dict(
    category="rule", grain="one row per version of a prompt (append-only)",
    use=("Support for all modules (#2361): every prompt put to a model, with every version, so prompts can change all the "
         "time and it stays known which worked best. A change is a NEW version (never an edit): the old one is retired. "
         "cfg_setting holds only which version is active for a prompt_key; a call can use only an active version "
         "(lib/aiclient.py). ai_call.prompt_id points here, so every answer is tied to the exact text. The compare step ranks "
         "versions by their calls and the provisional evaluation cases"),
    cols=[
        pk(),
        c("prompt_key", "TEXT", "the prompt's name, module.step (for example collection.synonym, group.word)", nn=1),
        c("version", "INTEGER", "1, 2, 3 ... within the prompt_key", nn=1),
        c("text", "TEXT", "the full prompt text, with its {variables}", nn=1),
        c("hash", "TEXT", "hash of the text: the same hash is the same prompt", nn=1),
        c("role", "TEXT", "the model role the prompt is written for", nn=1, exp="enum.ai_role"),
        c("purpose", "TEXT", "what the prompt asks, in a line", nn=1),
        c("expected_output", "TEXT", "the shape of a usable answer (for example JSON with relation synonym|opposite|distinct)"),
        c("status", "TEXT", "draft (being tried), active (the one in use for its prompt_key), retired (kept for history and "
          "comparison)", nn=1, dflt="'draft'", exp="enum.cfg_ai_prompt.status"),
        c("parent_id", "INTEGER", "points to cfg_ai_prompt.id: the version this one was changed from; NULL for the first",
          fk="cfg_ai_prompt.id"),
        c("change_note", "TEXT", "what was changed and why, in a line", nn=1),
        c("created_by", "TEXT", "who made the version: Claude or Researcher", nn=1),
        c("created_at", "TEXT", "when (ISO-8601 UTC)", nn=1, dflt=NOW),
        c("activated_at", "TEXT", "when it became the active version; NULL while draft"),
    ],
    unique=["prompt_key", "version"], indexes=[],
    purpose=("The versioned register of every prompt the app puts to a local model, so the use of zeta-assist is controlled "
             "and reproducible and the best prompt can be told (#2361)."),
    success=("Every ai_call that used a prompt points to a row here; no prompt text is held in code or only in a setting; each "
             "prompt_key has at most one active version; and the compare step can rank the versions of a key."),
)

T["cfg_ai_model"] = dict(
    category="rule", grain="one row per (model on the server, role it serves)",
    use=("Support for all modules (#2361): the models on zeta-assist and what each is for. A module asks for a role (judge, "
         "embed, embed_fast, quick, reviewer); settings say which model serves the role; this table documents the model "
         "(size, digest, purpose) and whether it may be used. ai_call.model_id points here. The server and the way to reach "
         "it stay in cfg_setting modules ollama and surface_judge (B:124)"),
    cols=[
        pk(),
        c("name", "TEXT", "the model name with its tag as the server lists it (qwen3:30b, qwen3-embedding:latest)", nn=1),
        c("parameters", "TEXT", "the size as the server reports it (30.5B, 7.6B)"),
        c("digest", "TEXT", "the digest the server reported when the row was made; ai_call.model_digest holds the digest at "
          "each call"),
        c("role", "TEXT", "the role this row records the model for", nn=1, exp="enum.ai_role"),
        c("purpose", "TEXT", "what the model is used for in this role", nn=1),
        c("route_setting", "TEXT", "the cfg_setting key that names how the server is reached (ollama.host)"),
        c("status", "TEXT", "active (may be used) or retired (kept for history)", nn=1, dflt="'active'",
          exp="enum.cfg_ai_model.status"),
        c("pulled_on", "TEXT", "when the model was pulled to the server (date)"),
        c("inactive", "INTEGER", "1 when the row is switched off", nn=1, dflt="0"),
    ],
    unique=["name", "role"], indexes=[],
    purpose=("The register of the models on zeta-assist and their roles, so that which model does what is documented and a "
             "model can be replaced in one place (#2361)."),
    success=("Every model that answers a call is a row here with the role it served; a call to a model that is not an active "
             "row is refused; and the digest of each call is recorded."),
)

# ---- extensions of existing tables (column added, no new table) ---------------------------------------------------------
EXT = {
    "run": [
        c("settings_snapshot", "TEXT", "JSON of the settings and the prompt versions in force when the run started, so the "
          "run can be repeated and compared (the surface cycle, #2361); NULL for runs of other work"),
        c("counts", "TEXT", "JSON of what the run produced (rows written by table, calls made, failures) (#2361); NULL for "
          "runs of other work"),
    ],
    "run_batch": [
        c("model_role", "TEXT", "for a batch of model calls: the role asked for (judge, embed, ...) (#2361)",
          exp="enum.ai_role"),
        c("model", "TEXT", "for a batch of model calls: the model that answered, with its tag (#2361)"),
        c("calls", "INTEGER", "for a batch of model calls: how many calls were made (#2361)"),
        c("secs", "REAL", "for a batch of model calls: seconds taken; cost_usd stays 0 for a local model (#2361)"),
    ],
    "file_manifest": [
        c("module", "TEXT", "for a working file of the surface cycle: the module it belongs to (#2361); NULL for any other "
          "file", exp="enum.surface_cycle_module"),
        c("run_id", "TEXT", "for a working file of the surface cycle: the run that wrote it (#2361); NULL otherwise"),
        c("sha256", "TEXT", "for a working file of the surface cycle: its checksum when registered (#2361); NULL otherwise"),
        c("analytic_status", "TEXT", "for a working file of the surface cycle: live, or regenerable (a cache the tool rebuilds "
          "and that is never an input) (#2361); NULL otherwise", exp="enum.file_manifest.analytic_status"),
        c("migrated_from", "TEXT", "for a working file that was moved: the path it had before (#2361); NULL otherwise"),
    ],
}


def cfg_col(table, ordinal, col):
    return {"database": "iba", "table_name": table, "name": col["name"], "ordinal": ordinal, "type": col["type"],
            "is_pk": col["pk"], "notnull": col["nn"], "is_unique": 0, "dflt": col["dflt"], "fk": col["fk"],
            "use": col["use"], "expectation": col["exp"], "source": SOURCE, "filled_by": FILLED, "inactive": 0}


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    # 1. retire surface_pair_verdict (0 rows) and the unread surface_subgroup.surface_group
    if has("SELECT 1 FROM cfg_table WHERE database='iba' AND name='surface_pair_verdict'"):
        for (n,) in conn.execute("SELECT name FROM cfg_column WHERE table_name='surface_pair_verdict'").fetchall():
            ops.append(("cfg_column", "delete", {"table_name": "surface_pair_verdict", "name": n}, {}))
        for (col_,) in conn.execute("SELECT col FROM cfg_unique WHERE table_name='surface_pair_verdict'").fetchall():
            ops.append(("cfg_unique", "delete", {"table_name": "surface_pair_verdict", "col": col_}, {}))
        for (iname,) in conn.execute("SELECT DISTINCT name FROM cfg_index WHERE table_name='surface_pair_verdict'").fetchall():
            for (icol,) in conn.execute("SELECT col FROM cfg_index WHERE table_name='surface_pair_verdict' AND name=?",
                                        (iname,)).fetchall():
                ops.append(("cfg_index", "delete", {"table_name": "surface_pair_verdict", "name": iname, "col": icol}, {}))
        ops.append(("cfg_write_grant", "delete", {"writer": "migration", "table_name": "surface_pair_verdict",
                                                  "database": "iba"}, {}))
        ops.append(("cfg_table", "delete", {"database": "iba", "name": "surface_pair_verdict"}, {}))
    for ename in ("surface_pair_verdict.pair_kind", "surface_pair_verdict.surface_group", "surface_pair_verdict.use",
                  "surface_subgroup.surface_group"):
        for (v,) in conn.execute("SELECT value FROM cfg_enum WHERE name=?", (ename,)).fetchall():
            ops.append(("cfg_enum", "delete", {"name": ename, "value": v}, {}))
    if has("SELECT 1 FROM cfg_column WHERE table_name='surface_subgroup' AND name='surface_group'"):
        ops.append(("cfg_column", "delete", {"table_name": "surface_subgroup", "name": "surface_group"}, {}))
    # 2. enums
    for ename, values in ENUMS.items():
        for i, v in enumerate(values):
            if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", ename, v):
                ops.append(("cfg_enum", "insert", {}, {"name": ename, "value": v, "ordinal": i, "inactive": 0}))
    # 3. the new tables: cfg_table, cfg_column, cfg_unique, cfg_index, cfg_write_grant, cfg_table_purpose
    rule_writers = [w for (w,) in conn.execute(
        "SELECT writer FROM cfg_write_grant WHERE table_name='cfg_candidate_rule' AND inactive=0").fetchall()]
    for t, d in T.items():
        if not has("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", t):
            ops.append(("cfg_table", "insert", {}, {"database": "iba", "name": t, "grain": d["grain"], "use": d["use"],
                                                    "inactive": 0, "category": d["category"]}))
            for i, col in enumerate(d["cols"]):
                ops.append(("cfg_column", "insert", {}, cfg_col(t, i, col)))
            for i, ucol in enumerate(d["unique"] or []):
                ops.append(("cfg_unique", "insert", {}, {"database": "iba", "table_name": t, "col": ucol, "ordinal": i}))
            for iname, icols in d["indexes"]:
                for i, icol in enumerate(icols):
                    ops.append(("cfg_index", "insert", {}, {"table_name": t, "name": iname, "col": icol, "ordinal": i}))
            writers = ["migration"] + (rule_writers if d["category"] == "rule" else [])
            for w in dict.fromkeys(writers):
                ops.append(("cfg_write_grant", "insert", {}, {"writer": w, "table_name": t, "database": "iba", "inactive": 0}))
            if d["category"] == "rule":
                ops.append(("cfg_table_purpose", "insert", {}, {"table_name": t, "kind": "purpose", "text": d["purpose"]}))
                ops.append(("cfg_table_purpose", "insert", {}, {"table_name": t, "kind": "success", "text": d["success"]}))
    # 4. extensions: cfg_column rows for the added columns
    for t, cols in EXT.items():
        top = conn.execute("SELECT COALESCE(MAX(ordinal),-1) FROM cfg_column WHERE table_name=?", (t,)).fetchone()[0]
        for col in cols:
            if not has("SELECT 1 FROM cfg_column WHERE table_name=? AND name=?", t, col["name"]):
                top += 1
                ops.append(("cfg_column", "insert", {}, cfg_col(t, top, col)))
    # 5. a setting read by the loader (the groups of each collection a, b, c)
    if not has("SELECT 1 FROM cfg_setting WHERE key='surfaces.scope_groups'"):
        ops.append(("cfg_setting", "insert", {}, {
            "key": "surfaces.scope_groups", "module": "surfaces", "inactive": 0,
            "value": json.dumps({"a": ["behaviour", "inner_being_state"], "b": ["being"], "c": ["other"]}),
            "use": "which surface groups make up each collection of surfaces (#2361): a = behaviour and inner_being_state (the "
                   "study of the inner being: bases and collections are built for these), b = being (entities), c = other. "
                   "Read to decide base_state out_of_scope; the scope of a surface is not stored, it follows from its group"}))
    # 6. the migration's own utility row
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "purpose": f"ONE-OFF migration -- escalation #2361 stage 1a: the tables and config of the surface cycle (re-grain of "
                       f"surface_pair_verdict, extensions of run, run_batch, file_manifest, eleven new tables); run_id {RUN_ID}.",
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def physical(conn, cfg):
    """Drop the retired objects and build the new ones, from the (already written) cfg rows."""
    live = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    if "surface_pair_verdict" in live:
        n = conn.execute("SELECT count(*) FROM surface_pair_verdict").fetchone()[0]
        if n:
            raise RuntimeError(f"surface_pair_verdict holds {n} row(s): refused to drop it")
        conn.execute("DROP TABLE surface_pair_verdict")
    cols = {r[1] for r in conn.execute("PRAGMA table_info(surface_subgroup)")}
    if "surface_group" in cols:
        for (iname,) in conn.execute("SELECT name FROM sqlite_master WHERE type='index' AND tbl_name='surface_subgroup' "
                                     "AND sql LIKE '%surface_group%'").fetchall():
            conn.execute(f'DROP INDEX "{iname}"')
        conn.execute("ALTER TABLE surface_subgroup DROP COLUMN surface_group")
    for t, d in T.items():
        if t not in live:
            create_sql, index_sql = table_ddl(cfg, t)
            conn.execute(create_sql)
            for sql in index_sql:
                conn.execute(sql)
    for t, cols_ in EXT.items():
        have = {r[1] for r in conn.execute(f'PRAGMA table_info("{t}")')}
        for col in cols_:
            if col["name"] not in have:
                conn.execute(f'ALTER TABLE "{t}" ADD COLUMN "{col["name"]}" {col["type"]}')


def verify(conn):
    """Every registered column exists, and no table of the cycle holds a row."""
    bad = []
    for t in T:  # a new table: the physical columns are exactly the registered ones
        have = [r[1] for r in conn.execute(f'PRAGMA table_info("{t}")')]
        want = [r[0] for r in conn.execute("SELECT name FROM cfg_column WHERE table_name=? AND inactive=0 ORDER BY ordinal", (t,))]
        if sorted(have) != sorted(want):
            bad.append(f"{t}: physical {sorted(set(have) ^ set(want))}")
    for t, cols_ in EXT.items():  # an existing table: each added column exists and is registered
        have = {r[1] for r in conn.execute(f'PRAGMA table_info("{t}")')}
        reg = {r[0] for r in conn.execute("SELECT name FROM cfg_column WHERE table_name=? AND inactive=0", (t,))}
        for col in cols_:
            if col["name"] not in have or col["name"] not in reg:
                bad.append(f"{t}.{col['name']}: physical {col['name'] in have}, registered {col['name'] in reg}")
    if "surface_group" in {r[1] for r in conn.execute("PRAGMA table_info(surface_subgroup)")}:
        bad.append("surface_subgroup.surface_group still exists")
    if conn.execute("SELECT 1 FROM sqlite_master WHERE name='surface_pair_verdict'").fetchone():
        bad.append("surface_pair_verdict still exists")
    for t in T:
        n = conn.execute(f'SELECT count(*) FROM "{t}"').fetchone()[0]
        if n and t not in ("cfg_base_construct", "cfg_ai_prompt", "cfg_ai_model"):
            bad.append(f"{t} holds {n} row(s)")
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        kinds = {}
        for t, op, _, _ in ops:
            kinds[(t, op)] = kinds.get((t, op), 0) + 1
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        for (t, op), n in sorted(kinds.items()):
            print(f"  {t} {op}: {n}")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2361-schema', named=True)}")
    try:
        conn.execute("SAVEPOINT surface_cycle_schema")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        physical(conn, cfg)
        bad = verify(conn)
        if bad:
            raise RuntimeError("verification failed: " + "; ".join(bad))
        conn.execute("RELEASE surface_cycle_schema")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO surface_cycle_schema")
        conn.execute("RELEASE surface_cycle_schema")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); tables built: {list(T)}; columns added to: {list(EXT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
