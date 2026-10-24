"""config_alignment_2268_v1_20261024.py -- escalation #2268: the config alignment change set, sections 2 to 7
(outputs/escalation/2268-config-alignment-change-set-v1-20261024.md), approved by the researcher 2026-10-24:
"#2268 approved: apply change set sections 2 to 7, tested on a copy first, then live."

Rows that live code still reads are not changed here; they change with the build that changes the code (B:62):
reading.output_dir, report.cluster_folder_naming_convention and a reading_index exclusion (build B7); the
lexical.llm_* family, the Stage 1 batch caps, report.stage1_coverage_validation_pattern,
cluster.recording_similarity_threshold and ib_observation.meaning_source_aliases (build B3); the reading_strand
enums (build B8); the worked-examples table (build B10, a schema change); the style guide setting (work unit W-2);
the passage method's work packages, steps and method.* path settings (build B12: retiring a work package also moves
its PS script to archive/ and retires its on-fail, report and write-grant rows). The passage method rules and
quality checks retire here.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path) in the same
transaction. Refuses to run twice (its run_id in cfg_change_detail).

Usage:
    python iba/app/migration/config_alignment_2268_v1_20261024.py [--db PATH] [--dry-run]
"""
import argparse
import datetime
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2268-CONFIG-ALIGNMENT-20261024"
MODULE = "config_alignment_2268_v1_20261024"
SRC = "#2268 change set v1 (outputs/escalation/2268-config-alignment-change-set-v1-20261024.md), rulings R1 to R19"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class Refused(Exception):
    pass


# ── §2 behaviour rules ─────────────────────────────────────────────────────────────────────────────
REWORD = {
    37: "New analytical work is derived from the config rows that govern it, never from a prior run's unreviewed "
        "output used as an implicit template -- an unreviewed pass may itself be wrong, and copying its shape "
        "propagates the error silently.",
    69: "Observation, claim and narrative text states what a cited verse or passage says, and may set related verses "
        "side by side. It never joins verses into a pattern, mechanism, division of labour or \"what this shows\" that "
        "no verse states, and never uses an uncounted most/often/always. A new insight found while writing goes to an "
        "observation first, not into prose. A researcher \"not in the way you portrayed it\" means withdraw the "
        "portrayal. When in doubt: quote, and stop.",
    71: "Before any query for a reading, use what is already gathered: the scope's collation (0.GAP pre) comes first. "
        "The verse to M-code link is verse_lexical.strong joined to cluster_strong (cluster_code LIKE 'M%', "
        "deleted=0), read with ONE set-based query over the verse set, never a per-verse loop and never a pass over "
        "every cluster. Results already recorded (observations, claims, faces) are gathered, not re-derived. A query "
        "that does not return within seconds means the approach is wrong: stop and re-plan, do not wait it out.",
    72: "The study's primary focus is the human inner being (HIB). Each verse read is routed by what it shows, and the "
        "route is recorded in its observation. (A) Other beings in their own right: a word used of God, angels, other "
        "spirits or nature (non-HIB) is routed to Ch 13 \"Other beings\" (13.1 Divine, 13.2 Angels, 13.3 Other "
        "spirits, 13.4 Nature), read for what the verses say that being is and does; for God, also how his character "
        "passed to the HIB through creation in his image, held open (#1984). (B) Another being interacting with the "
        "HIB is fully in HIB scope. A verse may take A and B, described from different angles. (C) A verse with no "
        "inner-being and no other-being bearing is still assessed and recorded as data, and does not enter the "
        "narrative.",
    89: "How the meaning or application of the same word or concept changes in different circumstances is a key "
        "discovery and is built upon, never set aside. Every reading records each word's face in its observation, "
        "with the circumstance that differs and why (the ledger face and the catalogue's term for it are one concept). "
        "A word's meaning is never taken from its cluster tag, since a tag shows one face only. Ch 11 section 4 "
        "('What changes the character') is the cross-cutting account the faces feed.",
    92: "Items are not held unnecessarily: verses or items that bear on the scope are read while the reading is open. "
        "A gap that stays unresolved, or needs further work, goes to an open item, not parked behind another step.",
    93: "When a scope includes M47 (inner seat) words, its verses are checked for dropped observations by word, not by "
        "citation (a narrative citation is verse-level, not word coverage); a dropped one is a 0.GAP pre gap.",
    94: "Before a scope is set, the glosses of its theme are scanned across all cluster codes, M and T alike (phase "
        "0.C): words for the theme may sit in T-codes that no earlier reading pulled (e.g. the dead/die words, G3498 "
        "nekros and 16 others).",
    95: "A scope's verse sets come only through the app's raw layer and the scope resolver (Verse-Scope.ps1), never "
        "through an inline STEP call.",
    109: "A question a verse reading could answer is answered by reading the verses, never passed to the researcher.",
    110: "For every term in a verse read, verse_lexical.surface is analysed per Strong's first: the surface shows the "
         "different interpretations of the root that the gloss or suffix alone can miss. Surface variants and related "
         "terms found are recorded in observations.",
    114: "Study work runs in phases: the scope with its objective (0.C); the gaps recorded for it (0.GAP pre), processed "
         "into the tables before the next gate; the verses read in context (D4 observe); then the claims finalised "
         "and the gaps rechecked against them (0.GAP post), and the narrative written. Claims and narrative are done "
         "only from the tables (observations, faces, claims and their sources, read through the app for the scope in "
         "hand), never from memory or recollection of earlier readings or of the conversation. A session may break "
         "between phases.",
}
REPLACE_IN = {   # (rule id, field): [(old, new)] -- the rest of the text stands
    (70, "rule_text"): [("A strand or unit that finds a word associated with another cluster records that "
                         "association in its ledger, for cross-cluster analysis.",
                         "A reading that finds a word associated with another cluster records that association in "
                         "an observation (the term's cluster relation), for cross-cluster analysis.")],
    (74, "rule_text"): [("A thread is not worked as a task: it moves only when a strand reaches it (focused capture, "
                         "rule 84).",
                         "A thread is not worked as a task: its items are matched when a reading opens on a scope, "
                         "and settled in the reading's claim step."),
                        ("Items are what a strand, task or reading is matched against",
                         "Items are what a task or reading is matched against"),
                        ("Before every unit pull of a strand, the threads that bear on it are matched (Escalation.ps1 "
                         "-Action Match -Cluster .. -Strong .. -Verse ..; -For nnnn records the match); held items and "
                         "researcher questions are raised as threads at every ledger approval (Escalation.ps1 -Action "
                         "Raise -Type thread).",
                         "Before a reading opens, the threads that bear on its scope are matched (Escalation.ps1 "
                         "-Action Match -Cluster .. -Strong .. -Verse ..; -For nnnn records the match); gaps that stay "
                         "unresolved or need further work are raised as open items (Open-Item.ps1).")],
    (116, "rule_text"): [("Study work starts by reading each verse in its passage and letting it say what it says.",
                          "Study work starts by reading each verse in its passage, with all its observations already "
                          "recorded read into focus, and letting it say what it says.")],
    (13, "rule_text"): [("(prose + analytic findings)", "(prose only: the programme and glossary prose)"),
                        ("(process control + the entire base data layer)",
                         "(process control, base data and all analysis tables)")],
}
ENFORCED = {
    7: "No live call site after #2268 R3c (the API generator steps retired); applies to any future API call.",
    8: "No live call site after #2268 R3c (the API generator steps retired); applies to any future API call.",
    9: "No live call site after #2268 R3c (the API generator steps retired); applies to any future API call.",
    67: "Delivered at session start (rule 81) and at first use of sqlite (cfg_rule_scope).",
    77: "Checked at the reading's claim step: the 0.GAP post gap types claim_without_observation and "
        "citation_without_record (reading.gap_types).",
}
RETIRE_RULES = [68, 73, 84, 85, 86, 87, 88, 90, 91]
NEW_SCOPES = [(r, "ps", "Reading.ps1") for r in (69, 70, 71, 72, 89, 92, 93, 94, 95, 109, 110)] + \
             [(r, "ps", "Verse-Scope.ps1") for r in (94, 95)]

# ── §3 settings ────────────────────────────────────────────────────────────────────────────────────
GAP_TYPES = {
    "term_cluster": ("recording", ["cluster_strong"], "A term in scope with no cluster (term-cluster). Route it to the "
                     "cluster assignment's recovery (Cluster-Assign.ps1) and name the row, or give the reason."),
    "meaning_missing": ("recording", ["strong_meaning_tree", "strong_lexicon"], "A term in scope with no meaning in "
                        "one of the three sources (meaning tree; for Greek, Mounce and LSJ). Pull it through the spine "
                        "route and name the row, or give the reason it is not needed."),
    "base_missing": ("recording", ["span", "strong"], "A verse or term in scope with a missing base datum (span, "
                     "Strong's). Route it to its recovery (New-Word, raw.backfill_meaning, the spine); never work round it."),
    "term_reading_missing": ("recording", ["ib_observation"], "A term in a verse of the scope with no term reading "
                             "result: meaning in context, surface variants, related terms. Record it as an observation, "
                             "measured against what is expected, not by presence."),
    "read_in_files_only": ("recording", ["ib_observation"], "A verse an earlier study file reads (its lines are given) "
                           "with no observation in the tables. Gather the reading into an observation, or give the "
                           "reason the file's reading holds nothing."),
    "face_not_gathered": ("recording", ["ib_observation", "reading_strand_hit"], "A face recorded for a word occurrence "
                          "(the ledger faces) that the observation record does not hold. Gather it."),
    "open_item": ("recording", ["ib_observation", "escalation_thread_item_response"], "An open item that matches the "
                  "scope: read for what it asks, and record what the reading found. It is settled at the claim step."),
    "not_read": ("recording", ["ib_observation"], "A verse in scope with no observation for an M-code in focus, or for "
                 "a T-code found relevant. Read it in its passage with all its observations in focus, and record the "
                 "observations the scope's objective calls for."),
    "observation_part_missing": ("recording", ["ib_observation"], "An observation missing one of its parts (face, "
                                 "role, operation, parties, route, home: reading.observation_parts), or holding one "
                                 "that is not what the verse shows. Presence of something that is not the right thing "
                                 "is not a resolved gap."),
    "observation_unsupported": ("recording", ["ib_observation"], "An observation the verse no longer supports. "
                                "Soft-delete it with the reason."),
    "observed_no_claim": ("synergy", ["narrative_claim", "ib_observation"], "An observation no current claim rests on: "
                          "carry it by a claim, or dispose of it with a reason. Checked against the claims (0.GAP post)."),
    "claim_not_told": ("synergy", ["narrative_claim_telling"], "A current claim no block tells: tell it in a block that "
                       "fits its chapter's story, or hold it with a reason."),
    "claim_without_observation": ("synergy", ["narrative_claim_source"], "A claim resting on verses only, with no "
                                  "observation behind it: give it its observation source."),
    "citation_without_record": ("synergy", ["ib_observation", "narrative_claim"], "A verse cited in a block with no "
                                "observation and no claim behind it: record them."),
}


def gap_types_json():
    return json.dumps({k: {"phase": p, "records_in": r, "guide": g} for k, (p, r, g) in GAP_TYPES.items()},
                      ensure_ascii=False)


SETTINGS_UPDATE = {
    "ib_observation.tag_stage_excluded": {"use": "per stage, the tags it may not offer (lib/taggingguidance.tags_for_stage)"},
    "escalation.worked_strand_escalations": {
        "use": "#2173 P5 T-d: per cluster, the escalations whose readings worked it (formerly its strand). A cluster "
               "counts as worked only when every listed escalation is completed (read from state at audit time)."},
}
SETTINGS_NEW = {
    "reading.whole_cluster_reading_start": (
        "\"A cluster is not read whole by default. A scope on a cluster starts with an overview of its subgroups and "
        "the spread of its verses, from which the scope is segmented.\"",
        "#2268 R2 (researcher: whole_cluster_reading_start): how a reading on a cluster starts (phase 0.C)", "reading"),
    "reading.observation_parts": (
        "[\"face\", \"role\", \"operation\", \"parties\", \"route\", \"home\"]",
        "#2268 R13a: the parts every verse observation holds, per M-code in focus and per T-code found relevant", "reading"),
    "glossary.currency_check": (
        "[\"role\", \"characteristic\", \"operation\", \"M-Code cluster\", \"T2\", \"T3\", \"inner being\"]",
        "#2268 R9, P33: the glossary terms the controlled values point to; each must exist and be current in the "
        "programme glossary (prose_section); the check is build B10", "behaviour"),
}
SETTINGS_RETIRE = ["strand_reading.output_dir"]

# ── §4 enums ───────────────────────────────────────────────────────────────────────────────────────
NEW_ENUMS = {
    "observation_role": ["characteristic", "qualifier", "standalone"],
    "observation_route": ["A", "B", "C"],
    "observation_disposition": ["told", "claim", "held", "data", "context", "withdrawn"],
}

# ── §5 method rules ────────────────────────────────────────────────────────────────────────────────
M = []   # (step, key, text, source, active)


def m(step, key, text, source, active=1):
    M.append((step, key, text, source, active))


m("reading.open", "RM-01 web-scope-objective", "The inner being is a web of interrelated activity. A reading takes one "
  "scope with a clear objective, and the fan-out follows from what it finds. Cluster codes are anchors, not goals.", "B:84 (R2)")
m("reading.open", "RM-02 objective-defines-home", "A scope's objective defines the home of what it records (RO10). A "
  "verse may come into several scopes from different angles (a cluster group, an open item), each adding the "
  "observations its objective calls for.", "R14, R16")
m("reading.open", "RM-03 no-whole-cluster", "A cluster is not read whole by default: a scope on a cluster starts from "
  "an overview that segments it (cfg_setting reading.whole_cluster_reading_start).", "R2")
m("reading.open", "RM-04 gather-not-redo", "Work already done is gathered, not redone, unless there is reason to "
  "believe it is incomplete or needs revision.", "R2")
RO = {
    "RO1 verse-text-once": ("reading.record", "Verse text and passage are read only in D4 observe, once per verse per reading."),
    "RO2 observations-into-focus": ("reading.record", "When a verse is read, all its observations already recorded are "
                                    "read into focus, and the scope's objective is evaluated against them; the "
                                    "observations the objective calls for, and that are missing, are added."),
    "RO3 gather-not-redo": ("reading.open", "Work already done is gathered, not redone, unless it is incomplete or needs "
                            "revision; a re-read or re-run happens only for a recorded gap."),
    "RO4 base-data-in-scope-and-gap-only": ("reading.open", "Base data is read only in 0.C and 0.GAP pre. A missing or "
                                            "poor base datum is a gap routed to its recovery, never worked round or "
                                            "silently ignored."),
    "RO5 gather-once": ("reading.open", "0.GAP pre reads each table once for the scope and writes the gathered set; the "
                        "later phases read what it gathered, not the tables again."),
    "RO6 tables-only-before-d4": ("reading.open", "D1 to D3 read table data only: no base data tables, no verse text."),
    "RO7 gap-post-with-claims": ("reading.check", "0.GAP post is done inside the claim step, from the same read as the "
                                 "claims."),
    "RO8 no-whole-cluster": ("reading.open", "A cluster is not read whole by default; an overview segments it."),
    "RO9 narrate-from-tables": ("reading.apply", "Narration reads claims and observations; it quotes verse text from the "
                                "verse table (quote-checked) and does not re-read the verse in context."),
    "RO10 objective-is-home": ("reading.open", "A scope's objective defines the home of the observations it records."),
    "RO11 one-row-per-code": ("reading.record", "One observation row per M-code, or relevant T-code, in focus, with no "
                              "duplicate rows; an observation applying to several verses or terms carries several nodes."),
    "RO12 gaps-into-tables-before-gate": ("reading.check", "A scope's gap JSON records the gaps as they are found and is "
                                          "processed into the tables as soon as its phase completes, before the next "
                                          "gate. Gaps are processed for the scope only."),
}
for k, (step, text) in RO.items():
    m(step, k, text, "#2268 plan v2 section 5 (R3d, R13 to R16)")
RG = [
    ("RG-01 read-outward", "Read outward from the verse, not inward from the scope's question. First record everything "
     "the verse carries, each with where it bears (chapter, thread, signpost); answer the scope's question last. A verse "
     "often has two or three significances, and none is dropped.", "role guide v2 4.0"),
    ("RG-02 passage-and-genre", "Read the verse in its passage and genre; name the speaker; explore figures for what "
     "they say about the inner being; take paired and opposite acts together. Restating a verse is not reading it.",
     "role guide v2 4.1; B:91"),
    ("RG-03 role-per-occurrence", "Find the main inner-being operation, and give every M-coded word, and every T-code "
     "word found relevant, its role (cfg_enum observation_role): characteristic, qualifier / process-element, or "
     "standalone. The role comes from this verse, never from the cluster tag.", "role guide v2 4.2"),
    ("RG-04 qualifier-binding", "A qualifier gets no own account from the verse: it is recorded with what it gives the "
     "characteristic it binds to (a measure, strengthening, ground, cause, object, setting, bait) and as an "
     "interrelationship. A qualifier whose usage varies across contexts may earn its own reading later.",
     "role guide v2 2, 4.3"),
    ("RG-05 relational-and-pointer", "Record how the M-code words work together (a relational observation). Record any "
     "pointer outside the verse separately, without resolving it inline.", "role guide v2 4.4; checklist 0.5a"),
    ("RG-06 parties-and-route", "Record the parties: who bears the act, who causes it, who is acted on (source, target, "
     "impact, purpose), and the route (cfg_enum observation_route). A non-human being is never itself a HIB; a "
     "collective stays one HIB; an implied party is named as referential, never asserted.",
     "role guide v2 4.5; method rules 1 to 4 (passage, retired)"),
    ("RG-07 every-row", "Read the T3 operations, movement and force, negators (a refusal is an act), connectives, body "
     "parts, places, objects and nature for what they carry here; read every row, untagged ones too.", "role guide v2 4.6"),
    ("RG-08 the-original", "For every word that names an inner or bodily act, look at the original: the root's range in "
     "all three meaning sources read together, never one picked and the others dropped; the ESV renderings across its "
     "verses; whether the English adds or hides; the literal sense beside the rendering. Where more than one reading is "
     "open, record each, and mark the choice 'I read'.",
     "role guide v2 4.6a; method rules 42, 43, 70, 88, 92, 113"),
    ("RG-09 face", "Record each word's face: how it appears here, the circumstance, why it differs from its other "
     "occurrences, and where the sense departs from the general gloss.", "role guide v2 4.7; B:89; R18"),
    ("RG-10 never-not-x", "Never close a verse or item on 'not X'. A role label is never a verdict; the close records "
     "what the verse is. Silence about the inner being is a finding, recorded as data with its reason.",
     "role guide v2 4.9; method rules 18, 91"),
    ("RG-11 hidden-behind-act", "A phenomenon hidden behind a stated or refrained act may be named, with the verb, "
     "clause or stated silence that grounds it, and whether it is stated or read.", "method rules 14, 15"),
    ("RG-12 not-literary-pattern", "A literary or structural pattern is not an inner-being observation: log it as an "
     "open question instead. A human/divine comparison is recorded only where the text's own wording anchors it.",
     "method rules 16, 23"),
    ("RG-13 source-vs-enablement", "Keep the source of an interior state apart from the source of an enablement to act.",
     "method rule 21"),
    ("RG-14 morph-read", "Morph is read, not carried: where occurrences of a word show different stems or voices, record "
     "whether the subject does, undergoes or causes the act.", "method rule 95"),
    ("RG-15 difference-own-observation", "A difference, or a specific inference, is its own observation, never folded "
     "into another.", "method rule 93"),
    ("RG-16 homonym-and-data-error", "A word that is only a homonym or a name, with no meaningful context, is recorded "
     "as such (tag no-human-context) and left. Data errors found while reading are flagged (tag data-error), not fixed "
     "in the reading.", "method rules 97, 98"),
    ("RG-17 catalogue-as-prompts", "The question catalogue's questions are prompts for the areas to explore. A question "
     "that does not apply is not answered, and no answer is manufactured beyond what the verse shows.", "R15, R17"),
    ("RG-18 faculty-last", "Faculty (heart, soul, spirit, mind) is reflected on at the end, over the scope, not per word.",
     "role guide v2 2, 5.5"),
    ("RG-19 trial-first", "Before reading the whole scope, read a few verses and have them checked.", "role guide v2 5.6"),
]
for k, t, s in RG:
    m("reading.record", k, t, s)
RW = [
    ("RW-01 changed-only-by-reading", "No observation is changed except by a reading, and every change is recorded with "
     "its reason. An observation no longer supported by the verse is soft-deleted, with the reason.", "R6, R15 (B:68 retired)"),
    ("RW-02 observation-parts", "Per M-code in focus, and per T-code found relevant, the verse's observations hold the "
     "parts in cfg_setting reading.observation_parts (face, role, operation, parties, route, home). The term reading "
     "results (meaning in context, surface variants, related terms) are observations too.", "R13a"),
    ("RW-03 no-duplicates-multi-node", "One observation row per M-code or relevant T-code in focus, with no duplicate "
     "rows; an observation applying to several verses or terms carries several nodes.", "R16"),
    ("RW-04 concise-verse-specific", "Observation text is concise and tied to this verse's content, never a restatement "
     "of the word's dictionary sense. A transliteration is never given without its gloss.", "method rules 108 to 111, 119, 120"),
    ("RW-05 span-grounded", "An observation about a word can be answered only by consulting this occurrence's verse, "
     "span and morph.", "method rules 112, 121"),
    ("RW-06 resolved-fresh-on-evidence", "Verse references are resolved fresh at write time, never taken from the text "
     "written. Relations are recorded only on evidence.", "checklist 0.5, 0.8"),
    ("RW-07 flags-carried", "A flag raised in reading (needs adjacent context, a pointer) states its reason and what the "
     "follow-up must establish, and is carried to an open item, not resolved inline. Can't-resolve is recorded, never "
     "guessed (tag could-not-resolve).", "method rules 74, 104, 116; checklist 0.5a, 0.5b, 0.6"),
    ("RW-08 slants-own-rows", "Where the evidence points to more than one reading, each is its own observation with its "
     "own evidence.", "method rule 102"),
    ("RW-09 reread-builds-on-prior", "A re-read includes the observations already recorded for the verse, so the reading "
     "sees prior findings and builds on them.", "method rule 99; RO2"),
    ("RW-10 disposition-in-tables", "Where a verse ends up is recorded in the tables as an observation disposition "
     "(cfg_enum observation_disposition: told, claim, held, data, context, withdrawn).", "R5"),
    ("RW-11 missing-is-named", "Missing data in the base extract is named as a gap, never substituted from memory or "
     "outside knowledge.", "method rule 37; RO4"),
]
for k, t, s in RW:
    m("reading.record", k, t, s)
RC = [
    ("cluster.read", "RC-01 read-all-before-placing", "For a cluster, every member word's glosses and surfaces are read "
     "before any is placed in a subgroup.", "method rule 78"),
    ("cluster.read", "RC-02 subgroup-shape", "Subgroups group by shared meaning, not similar wording; at most 10 real "
     "subgroups, FLAG excluded; a label names the essence, not a word list; a singleton is valid; each word sits in "
     "exactly one subgroup.", "method rules 79 to 82, 86"),
    ("cluster.read", "RC-03 flag-with-reason", "A word goes to FLAG only with a reason (no inner-being implication, "
     "belongs to another cluster, another anomaly); any placement may carry a note.", "method rules 83, 84"),
    ("cluster.read", "RC-04 anchor-by-reading", "A subgroup's anchor verse is the one that best shows its shared "
     "characteristic, chosen by reading, not by a count.", "method rule 85"),
    ("cluster.read", "RC-05 every-occurrence", "Read every occurrence; grouping similar verses never excuses skipping "
     "one.", "method rules 89, 90"),
    ("cluster.read", "RC-06 compare-words", "Compare the subgroup's words against each other: where they share meaning "
     "and where they diverge.", "method rule 94"),
    ("word.read", "RC-07 every-occurrence-cited", "Every occurrence of a word read in D1 is cited by at least one "
     "observation, checked after the write.", "method rule 96"),
]
for step, k, t, s in RC:
    m(step, k, t, s, active=0)   # their steps are built by B3; activated then
RN = [
    ("RN-01 narrative-is-claudes", "Programme prose (the DB prose store) is the researcher's, and Claude writes it only "
     "on instruction. The narrative is written by Claude from the claims, to the narrative style rows, with no approval "
     "before publishing; the researcher reads the published chapters in context and corrects through Claude.", "R4; B:85"),
    ("RN-02 blocks-fit-the-story", "The narrative is Inner Being in Operation, kept as blocks in iba.db "
     "(governance.narrative_home). Each block fits the flow and context of its chapter's story, and the chapters follow "
     "a story. A chapter's purpose (narrative_chapter) is read before material is placed in it.", "R4; B:86"),
    ("RN-03 original-adjusts", "The original adjusts to the new, not the reverse; each unfounded claim is checked and "
     "restated; each later reading adds to the narrative. The researcher's own pictures are not narrative terms: the "
     "verses' own phrases are used.", "B:86"),
    ("RN-04 chapter-text", "Quote wording is checked against the ESV text in iba.db. Science chapters come later. The "
     "Spirit's own acts are placed in 13.1; Jesus's own acts get their 13.1 face, and Ch 10 keeps the human side.", "B:87"),
    ("RN-05 weave-not-fit", "A reading's claims are woven into the narrative knowing more is to come, never fitted where "
     "they support the current story; 'does not fit' means the structure must change. A key characteristic gets its "
     "own Ch 10 sub-chapter, with its angles woven into the chapters they belong to.", "B:88"),
    ("RN-06 one-account-per-phenomenon", "A phenomenon gets one account: what Scripture says it is, its forms from the "
     "words themselves, and why they differ. Other sections carry only what belongs to their activity and point back "
     "to it. Saying what a verse means in its setting is required; verses are not listed. Readings beyond what a verse "
     "states are marked 'I read'.", "B:90"),
    ("RN-07 narration-probes", "Narration is from the inner being's workings: probe (compare, ask why, ask what lies "
     "behind it, whether a relationship makes a difference); explore figures; never restate a verse as narration.", "B:91"),
]
for k, t, s in RN:
    m("reading.apply", k, t, s)

KEEP_METHOD = {44, 45, 46, 47, 48, 68, 69, 126}
REHOME = {77: "cluster.assign"}
RETIRE_METHOD_STEPS = ("lexical.meaning", "lexical.relational", "cluster.subgroup", "cluster.reading", "cluster.answer",
                       "hib.set", "phenomenon.set", "operation.set", "closing.set", "passage.build")

# ── §6 quality checks (all 18 passage checks retire; 21 on reading.check) ─────────────────────────────
QC = [
    ("is-genuinely-human", "Does each party recorded as a human inner being refer to a human, not a non-human being "
     "described in human terms, a place, an object or an abstraction?", "reasonableness"),
    ("verse-actually-supports-it", "Does the verse's own text (its lexical rows, not the English gloss) support what "
     "the observation records?", "reasonableness"),
    ("genuinely-inner-being", "Is each observation about the inner being's state, disposition, operation or "
     "interrelationship, not an outward fact restated with no interior content?", "reasonableness"),
    ("not-a-literary-pattern", "Is each observation per verse, not a textual or structural pattern presented as one?",
     "non_existence"),
    ("warrant-is-specific", "Does each hidden phenomenon name the verb, clause or stated silence in this verse that "
     "grounds it?", "existence"),
    ("full-lexical-range", "Does each word's reading draw on its full range in the three meaning sources and its sense "
     "in this context, not a generic label?", "reasonableness"),
    ("stated-or-read-honest", "Is basis 'stated' given only where the verse states it, and 'read' ('I read') "
     "everywhere else?", "reasonableness"),
    ("parties-not-invented", "Are source and target parties named or clearly identifiable in the verse or passage, not "
     "invented to complete the shape?", "non_existence"),
    ("missing-data-named", "Is data recorded as missing genuinely absent from the tables, and not substituted from "
     "memory or outside knowledge?", "non_existence"),
    ("every-word-has-role", "Has every M-coded word, and every T-code word found relevant, been given a role?", "existence"),
    ("observation-parts-held", "Does every observation hold its parts (reading.observation_parts), each what the verse "
     "shows?", "existence"),
    ("home-follows-objective", "Is every observation homed by the scope's objective (RO10)?", "existence"),
    ("bindings-relations-pointers", "Are qualifier bindings and relational observations recorded, and pointers kept "
     "separate?", "existence"),
    ("prior-observations-used", "Were the verse's earlier observations read into focus and built on, not re-derived?",
     "reasonableness"),
    ("i-read-marked-no-imputed-pattern", "Is every reading beyond the verse marked 'I read', with no pattern no verse "
     "states?", "reasonableness"),
    ("parties-and-route-recorded", "Are the parties and the route recorded for every verse read?", "existence"),
    ("no-duplicate-rows", "Is there no duplicate observation row for the same verse, code and finding?", "non_existence"),
    ("claim-rests-on-observations", "Does every claim the reading touched rest on observations, not on verses alone?",
     "existence"),
    ("block-fits-chapter-story", "Does every rewritten block fit its chapter's story and the narrative style rows?",
     "reasonableness"),
    ("gap-resolved-by-expectation", "Is every gap resolved against what is expected, not by the presence of a row?",
     "reasonableness"),
    ("unresolved-gap-has-item", "Does every gap left unresolved, or needing further work, have an open item?", "existence"),
]

# ── §7 control map, tables, columns, status flows, concept pointers ──────────────────────────────────
CONTROL = {
    "study_method": {"home": "cfg_method_rule (steps reading.open, reading.record, reading.check, reading.apply; "
                             "word.read and cluster.read when built), cfg_quality_check (reading.check), cfg_setting "
                             "reading.*, with cfg_prose_concept pointers to the glossary. The narrative style guide "
                             "(narrative.inner_being_style_guide_path) stays a Workflow file until it is carried in "
                             "(#2268 W-2).",
                     "description": "How study work is done (reading, recording, claims, narration), held as config "
                                    "rows (#2268 R1). A Workflow file is the authority only for the programme and "
                                    "inner-being definitions, through cfg_prose_concept."},
    "study_state": {"home": "escalation (reading escalations and type=thread items), the reading and reading_verse "
                            "tables, narrative_chapter, the narrative claim register tables, the narrative's blocks "
                            "(narrative_section.block_text; governance.narrative_home)"},
    "study_output": {"home": "_analytics/ (cluster folders per report.cluster_folder_naming_convention; the exported "
                             "narrative chapters in _analytics/essay/spirit_soul_body/inner-being-narrative/); "
                             "outputs/reading/ (each reading's gap, collation and synergy JSON) until build B7 moves "
                             "readings under their home cluster's folder (#2268 R7)"},
}
TABLE_USE = {
    ("iba", "ib_observation"): "One observation: a finding from a reading, with its text, meaning, parts and status, "
                               "grounded through ib_node on verses, strongs, subgroups, clusters or other observations. "
                               "Written by reading.record and reading.apply, and enhanced by observation_enhancer.apply. "
                               "It also holds gathered rows: the September catalogue work (stages verse-reading, "
                               "char-*, from the retired API steps) and the October ledger work (stage strand-reading). "
                               "Status meanings are by stage (cfg_status_flow, #2268 R14).",
    ("iba", "ib_node"): "The grounding of every observation: one row per verse, term, cluster, subgroup, question or "
                        "other observation it rests on. An observation applying to several verses or terms carries "
                        "several nodes (#2268 R16).",
    ("iba", "wa_obs_question_catalogue"): "The question catalogue (116 rows), migrated from bible_research.db "
                                          "2026-09-16 (#1696). Its questions are prompts for the areas a reading "
                                          "explores, never questions to be answered by force (#2268 R17). "
                                          "ib_observation.question_code and ib_node.question_code refer to it; the "
                                          "foreign key is a design point.",
}
COLUMN_USE = {
    ("ib_node", "source_stage"): "the stage of the observation this node grounds (the ib_observation.stage values)",
    ("ib_observation", "stage"): "cfg_enum ib_observation.stage: verse-reading, char-subgroup, char-reading, "
                                 "char-answers, char-synergy (the September catalogue stages, API, retired); "
                                 "strand-reading (the October ledger work, gathered); reading (written by a reading "
                                 "from #2268 on). Status meanings are by stage (#2268 R14).",
    ("verse_meta", "status"): "cfg_enum verse_meta_status (exclude/citated/analysed). Set by a reading (analysed at its "
                              "observe gate, citated when a rewritten block cites the verse) or by VerseMeta.ps1 -Step "
                              "SetStatus. NULL = not yet set.",
    ("ib_observation", "question_code"): "the catalogue question the observation was prompted by "
                                         "(wa_obs_question_catalogue, in iba.db); the foreign key is a design point",
    ("ib_node", "question_code"): "the catalogue question this grounding answers to "
                                  "(wa_obs_question_catalogue, in iba.db); the foreign key is a design point",
    ("ib_observation", "setting"): "the setting the observation reads the verse in: who speaks, the verses around "
                                   "it, the genre",
    ("ib_observation", "meaning"): "what the verse means in its setting, for the inner being",
    ("ib_observation", "implication"): "what it implies for the inner being",
    ("ib_observation", "run_id"): "the run that wrote or last changed the row (a reading, an import, the enhancer)",
    ("ib_observation", "revisit_note"): "the disposition note: the claim, item or reason; for a gathered row, its "
                                        "source note",
}
STATUS_FLOW = [
    ("ib_observation.catalogue", "draft", "the API recording pass (retired, #2268 R3c): written, not yet looked at", 0),
    ("ib_observation.catalogue", "resolved", "cleared for inclusion in analysis (#1782); no live writer", 1),
    ("ib_observation.catalogue", "withdrawn", "the recording pass on a re-run (B:68, retired); a reading (RW-01)", 2),
    ("ib_observation.reading", "draft", "recorded by a reading (reading.record) or gathered from the ledgers; not yet "
                                        "through claims", 0),
    ("ib_observation.reading", "resolved", "the reading's claim step: carried by a current claim", 1),
    ("ib_observation.reading", "open", "the reading's claim step: held on an open item", 2),
    ("ib_observation.reading", "silent", "the reading's claim step: assessed, data, not for the narrative", 3),
    ("ib_observation.reading", "withdrawn", "a reading: no longer supported, or replaced (supersedes), with the reason "
                                            "(RW-01)", 4),
]
CONCEPTS = [
    ("glossary_role", 1066, "role", "The role of a word in a verse: characteristic, qualifier / process-element, "
     "standalone (cfg_enum observation_role). Glossary entry is in the Contentious glossary, awaiting the researcher."),
    ("glossary_characteristic", 1047, "characteristic", "Characteristic: known by inference from what the inner being "
     "does; never a lemma, gloss or tag."),
    ("glossary_operation", 1048, "operation", "Operation: what an inner-being activity is doing and how, to or from "
     "others."),
    ("glossary_m_code_cluster", 1043, "M-Code cluster", "M-code cluster: a loose analytical grouping of Strong's codes; "
     "an anchor, not a goal."),
    ("glossary_t2", 1046, "T2", "T2: Strong's codes with no direct inner-being connotation, read as qualifiers."),
    ("glossary_t3", 1069, "T3", "T3: inner-being operations not tied to one cluster."),
]


def plan(conn) -> list[tuple]:
    ops = []
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    # §2
    for rid, text in REWORD.items():
        ops.append(("cfg_behaviour_rule", "update", {"id": rid}, {"rule_text": text}))
    for (rid, field), pairs in REPLACE_IN.items():
        text = one(f"SELECT {field} FROM cfg_behaviour_rule WHERE id=?", rid)[0]
        for old, new in pairs:
            if old not in text:
                raise Refused(f"B:{rid} {field}: expected text not found: {old[:60]}...")
            text = text.replace(old, new)
        ops.append(("cfg_behaviour_rule", "update", {"id": rid}, {field: text}))
    for rid, text in ENFORCED.items():
        ops.append(("cfg_behaviour_rule", "update", {"id": rid}, {"enforced_by": text}))
    for rid in RETIRE_RULES:
        ops.append(("cfg_behaviour_rule", "update", {"id": rid}, {"active": 0}))
        for (sid,) in conn.execute("SELECT id FROM cfg_rule_scope WHERE rule_ref=? AND inactive=0", (f"B:{rid}",)):
            ops.append(("cfg_rule_scope", "update", {"id": sid}, {"inactive": 1}))
    for rid, kind, value in NEW_SCOPES:
        if not one("SELECT 1 FROM cfg_rule_scope WHERE rule_ref=? AND scope_kind=? AND scope_value=? AND inactive=0",
                   f"B:{rid}", kind, value):
            ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": f"B:{rid}", "scope_kind": kind,
                                                         "scope_value": value, "inactive": 0}))
    # §3
    ops.append(("cfg_setting", "update", {"key": "governance.scope_iba_db"}, {"value": json.dumps(
        "The iba_db is the home for all project process control, base data and analysis tables, including all related "
        "tables from STEP through Strongs, verses, meaning, lexicals, observations, claims and the narrative.")}))
    tg = json.loads(one("SELECT value FROM cfg_setting WHERE key='ib_observation.tag_guidance'")[0])
    tg = json.loads(tg) if isinstance(tg, str) else tg
    tg["key-statement"] = ("a statement of what the verse says about the inner being, with its parts (setting, meaning, "
                           "implication, chain, parties, basis): the October ledger form, gathered work")
    ops.append(("cfg_setting", "update", {"key": "ib_observation.tag_guidance"}, {
        "value": json.dumps(tg, ensure_ascii=False),
        "use": "the definition of each ib_observation.tag value, given to every reading (#2207, #2268)"}))
    for k, s in SETTINGS_UPDATE.items():
        ops.append(("cfg_setting", "update", {"key": k}, s))
    ops.append(("cfg_setting", "update", {"key": "reading.gap_types"}, {
        "value": gap_types_json(),
        "use": "the reading's gap types (cfg_enum reading_gap_type, #2268 R13): each one's phase (recording: the gap "
               "JSON before claims; synergy: checked against the claims), the table(s) it records into, and its guide. "
               "A gap is measured against what is expected; presence of something that is not the right thing is not a "
               "resolved gap."}))
    for k, (v, use, mod) in SETTINGS_NEW.items():
        if not one("SELECT 1 FROM cfg_setting WHERE key=?", k):
            ops.append(("cfg_setting", "insert", {}, {"key": k, "value": v, "use": use, "module": mod, "inactive": 0}))
    for k in SETTINGS_RETIRE:
        ops.append(("cfg_setting", "update", {"key": k}, {"inactive": 1}))
    # §4
    if not one("SELECT 1 FROM cfg_enum WHERE name='ib_observation.stage' AND value='reading'"):
        n = one("SELECT max(ordinal) FROM cfg_enum WHERE name='ib_observation.stage'")[0] or 0
        ops.append(("cfg_enum", "insert", {}, {"name": "ib_observation.stage", "value": "reading", "ordinal": n + 1,
                                               "inactive": 0}))
    old_gaps = {r[0] for r in conn.execute("SELECT value FROM cfg_enum WHERE name='reading_gap_type'")}
    for i, v in enumerate(GAP_TYPES):
        if v in old_gaps:
            ops.append(("cfg_enum", "update", {"name": "reading_gap_type", "value": v}, {"ordinal": i, "inactive": 0}))
        else:
            ops.append(("cfg_enum", "insert", {}, {"name": "reading_gap_type", "value": v, "ordinal": i, "inactive": 0}))
    for v in sorted(old_gaps - set(GAP_TYPES)):
        ops.append(("cfg_enum", "update", {"name": "reading_gap_type", "value": v}, {"inactive": 1}))
    for name, values in NEW_ENUMS.items():
        for i, v in enumerate(values):
            if not one("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", name, v):
                ops.append(("cfg_enum", "insert", {}, {"name": name, "value": v, "ordinal": i, "inactive": 0}))
    # §5
    for (mid, step) in conn.execute("SELECT id, step FROM cfg_method_rule WHERE active=1").fetchall():
        if mid in REHOME:
            ops.append(("cfg_method_rule", "update", {"id": mid}, {"step": REHOME[mid]}))
        elif step in RETIRE_METHOD_STEPS and mid not in KEEP_METHOD:
            ops.append(("cfg_method_rule", "update", {"id": mid}, {"active": 0}))
    nid = one("SELECT max(id) FROM cfg_method_rule")[0]
    for i, (step, key, text, source, active) in enumerate(M):
        if not one("SELECT 1 FROM cfg_method_rule WHERE rule_key=?", key):
            nid += 1
            ops.append(("cfg_method_rule", "insert", {}, {"id": nid, "step": step, "rule_key": key, "rule_text": text,
                                                          "source_doc": f"{source}; {SRC}", "enforced_by": None,
                                                          "ordinal": i, "active": active}))
    # §6
    for (qid,) in conn.execute("SELECT id FROM cfg_quality_check WHERE active=1").fetchall():
        ops.append(("cfg_quality_check", "update", {"id": qid}, {"active": 0}))
    qid = one("SELECT max(id) FROM cfg_quality_check")[0]
    for i, (key, q, kind) in enumerate(QC):
        if not one("SELECT 1 FROM cfg_quality_check WHERE step='reading.check' AND check_key=?", key):
            qid += 1
            ops.append(("cfg_quality_check", "insert", {}, {"id": qid, "step": "reading.check", "check_key": key,
                                                            "question": q, "test_kind": kind, "required": 1,
                                                            "enforced_by": None, "ordinal": i, "active": 1}))
    # §7
    for kind, s in CONTROL.items():
        ops.append(("cfg_control_home", "update", {"kind": kind}, s))
    for (db, name), use in TABLE_USE.items():
        ops.append(("cfg_table", "update", {"database": db, "name": name}, {"use": use}))
    for (t, col), use in COLUMN_USE.items():
        if not one("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", t, col):
            raise Refused(f"cfg_column iba.{t}.{col} not found")
        ops.append(("cfg_column", "update", {"database": "iba", "table_name": t, "name": col}, {"use": use}))
    for ent, status, set_by, ordn in STATUS_FLOW:
        if not one("SELECT 1 FROM cfg_status_flow WHERE entity=? AND status=?", ent, status):
            ops.append(("cfg_status_flow", "insert", {}, {"entity": ent, "status": status, "set_by": set_by,
                                                          "ordinal": ordn, "inactive": 0}))
    for key, pid, term, desc in CONCEPTS:
        if not one("SELECT 1 FROM cfg_prose_concept WHERE concept_key=?", key):
            ops.append(("cfg_prose_concept", "insert", {}, {
                "concept_key": key, "chapter": 1, "section_hint": f"Programme glossary: '{term}' (prose_section {pid})",
                "description": desc, "source": "#2268 R9 (glossary canonical; controlled values point to it)",
                "added_at": NOW}))
    # self-registration
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2268: the config alignment change set, sections 2 to 7; "
                       f"run_id {RUN_ID}. inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID} is in cfg_change_detail)")
        return 0
    try:
        ops = plan(conn)
    except Refused as exc:
        print(f"REFUSED, nothing written: {exc}")
        return 2
    counts = {}
    for t, op, _, _ in ops:
        counts[f"{t} {op}"] = counts.get(f"{t} {op}", 0) + 1
    summary = ", ".join(f"{k} {v}" for k, v in sorted(counts.items()))
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s): {summary}")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail): {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
