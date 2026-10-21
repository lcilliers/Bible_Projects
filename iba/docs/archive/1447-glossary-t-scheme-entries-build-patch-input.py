"""Builds the prose_section INSERT patch for escalation #1447's glossary fix (full scope,
researcher instruction v4: "all the variants of T1-T9 must be documented in the glossary").
Run once to emit the patch JSON; the patch itself is what actually gets applied
(scripts/apply_session_patch.py), not this generator.
"""
import datetime
import json

NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
AUTHOR = "claude_code"

# ── [VRT] Verse Reading Technique v4 — T1-T9, verbatim from
# iba/docs/WA-verse-reading-technique-v4-2026-08-05.md ──────────────────────────────────────
VRT = [
    ("T1", "Work from the row, not the gloss",
     "The unit of analysis is the row (surface + strong + morph + full meaning_tree/stepGloss), "
     "not the English translation printed above the table. The translation orients the reader; "
     "it is not the evidence. Do not extract English clauses and match them against a keyword "
     "checklist; do not dilute or compromise reading quality; do not skip, ignore, or bypass "
     "rows; read each row in the context of the nearby rows, not in isolation."),
    ("T2", "Pull the full lexical range before assigning a sense",
     "Read the word's entire meaning_tree entry for its Strong's code(s), not just the stepGloss "
     "or the one sense the English translation happens to use. Record explicitly when a sense "
     "the English translation does not use is already a standing member of the word's own "
     "lexical range (stated via the lexicon, not inferred from metaphor/imagery), and when the "
     "range is genuinely ambiguous across senses that matter for this verse (name the live "
     "senses and reason which is operative, rather than silently picking one)."),
    ("T3", "Let morph decide voice, person, and aspect",
     "Read the morph code for every verb before deciding tense or voice -- never the English "
     "word order or tense. Perfect vs. imperfect vs. participle carry different aspectual force "
     "(a passive participle is a durative/ongoing condition, not a future event) -- check this "
     "against the English translation's own tense and correct where they diverge. Person/number "
     "decides the actual grammatical subject, never inferred from an English pronoun alone. "
     "Voice decides whether the subject acts or is acted upon."),
    ("T4", "Referent cruxes",
     "When a pronoun or unnamed party is genuinely ambiguous (several readings all grammatically "
     "live), do not silently resolve it and do not default to the most obvious English reading: "
     "enumerate every grammatically/contextually live reading; give the textual grounds for "
     "each; adopt one explicitly, stating why and whether the choice is a directed/researcher "
     "call or this pass's own default; keep the rejected alternatives on record, not just the "
     "winner."),
    ("T5", "Genre-conventional elements",
     "Record the genre-conventional elements of the verse or passage as an observation -- "
     "including elements expected by the genre but textually absent. Do not pass over these "
     "elements silently."),
    ("T6", "Stamp human-being words (IB)",
     "Stamp every word that explicitly points to a human being with IB. Other non-human beings "
     "are more likely to be stamped Agent (T7) -- only human-being words are stamped IB."),
    ("T7", "Stamp causing-action words (Agent)",
     "Stamp every word (the noun) that is the causing action as Agent. Note that an IB (T6) can "
     "itself be an Agent for another IB."),
    ("T8", "Stamp inner-being-related words (Process)",
     "Stamp every word that relates to any IB in the verse with Process -- including state/"
     "condition/faculty words tied to an IB."),
    ("T9", "Stamp action-verb words (Action)",
     "Stamp every action word (the verb) with Action."),
]
VRT_TAIL = (" A word can carry multiple stamps; stamps (T6-T9) are indicative and preliminary, "
           "not conclusive -- they do not determine which IB is affected by which Agent, or how "
           "it relates to a Process (that follows later in the study).")

# ── [TC] Tier catalogue T0-T7 — verbatim section titles from
# Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md (obs_ids confirmed live-matching
# wa_obs_question_catalogue, checked 2026-09-04) ────────────────────────────────────────────
TC = [
    ("T0", "Divine Image and Created Design",
     "God-relation (is the characteristic predicated of God, in what relation), created purpose "
     "(what it leads the person to be/do/become), image-bearer expression (what aspect of divine "
     "likeness it instantiates), typological significance."),
    ("T1", "Definition",
     "Name and naming, kind (act/disposition/condition/quality), boundary (structural opposite, "
     "what it excludes), modes of operation, immediate response, sustained effect, conditions of "
     "reception."),
    ("T2", "Constitutional Location and Boundaries",
     "Spirit-level location (spirit/soul/heart/mind/body), body-direction where a body link "
     "exists, origin/source, constitutional movement across levels."),
    ("T3", "The Inner Faculties",
     "Perception, cognition, memory, affect, creativity, volition, agency, moral evaluation, "
     "conscience, conscientiousness, relational capacity -- does the characteristic engage each "
     "faculty, and how."),
    ("T4", "Relational Interfaces",
     "Divine interface both directions (God-to-human, human-to-God), human interface (giving/"
     "receiving/boundaries), spiritual-beings interface (angelic/adversarial)."),
    ("T5", "Formative and Developmental Dimension",
     "Nature of transformation, sequence of inner states, mechanism of change, suffering/"
     "affliction, formation/sanctification, eschatological trajectory."),
    ("T6", "Structural Relationships with Other Characteristics",
     "Co-occurrence, sequential relationships, causal/constitutive relationships, vocabulary/"
     "root sharing, distinctions from the nearest neighbouring characteristic."),
    ("T7", "Evidential and Methodological Foundation",
     "Lexical and semantic analysis (primary terms, grammatical/semantic range, vocabulary arc), "
     "verse and literary interpretation (sentence/argument function, genre)."),
]

operations = []
op_n = 0


def add_section(heading: str, definition: str, background: str) -> None:
    global op_n
    op_n += 1
    body = f"[DEFINITION] {definition}\n\n[BACKGROUND] {background}"
    operations.append({
        "op_id": f"PROSE-INSERT-{op_n:02d}-{heading.replace(' ', '_').replace('(', '').replace(')', '')}",
        "table": "prose_section",
        "operation": "insert",
        "record": {
            "section_type_id_lookup": {"code": "glossary_programme"},
            "heading": heading,
            "body": body,
            "status": "draft",
            "author": AUTHOR,
            "metadata_json": json.dumps({"escalation": 1447, "built": NOW}),
        },
    })


# VRT entries
for code, title, text in VRT:
    definition = f"[VRT] {title} -- step {code} of the Verse Reading Technique v4 (a 9-step, T1-T9 per-verse analytical technique)."
    background = (text + VRT_TAIL + " Source: iba/docs/WA-verse-reading-technique-v4-2026-08-05.md. "
                 f"Distinct from the [TC] tier-catalogue {code} (a different, characteristic-grain "
                 "scheme -- see 'T{code} (Tier Catalogue)')."
                 .replace("{code}", code))
    if code in ("T2", "T3"):
        background += (f" Also distinct from the [CC] cluster_code {code} (a Strong's-code "
                       f"classification -- see the bare '{code}' entry).")
    add_section(f"{code} (Verse Reading Technique)", definition, background)

# TC entries
for code, title, text in TC:
    definition = f"[TC] {title} -- tier {code} of the tier catalogue (a T0-T7 characteristic-grain catalogue of observation questions)."
    background = (text + " Source: Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md "
                 "(checked live 2026-09-04, escalation #1447: its own header names it the "
                 "authoritative current question list, its obs_ids match wa_obs_question_"
                 "catalogue live today -- NOT deprecated, and its own range is T0-T7, not T0-T9, "
                 "correcting an earlier claim in iba/docs/1446-verse-word-analytic-methods-"
                 "extract-v2-20260904.md). "
                 f"Distinct from the [VRT] Verse Reading Technique {code} -- see 'T{code} "
                 "(Verse Reading Technique)'.")
    if code in ("T2", "T3"):
        background += (f" Also distinct from the [CC] cluster_code {code} -- see the bare "
                       f"'{code}' entry.")
    add_section(f"{code} (Tier Catalogue)", definition, background)

# Bare "T1" disambiguation entry -- the one genuine gap named in #1447 v2/v3 ("no T1 entry
# exists anywhere in the glossary"). T1 has no [CC] cluster_code meaning (only T2/T3 exist in
# that scheme, confirmed live) -- this entry is a pure disambiguation pointer, not a third
# definition of its own.
add_section(
    "T1",
    "Ambiguous on its own -- T1 has no [CC] cluster_code meaning (checked live: only T2/T3 "
    "exist in that scheme). Two real, unrelated meanings exist: see 'T1 (Verse Reading "
    "Technique)' (work from the row, not the gloss) and 'T1 (Tier Catalogue)' (Definition, "
    "characteristic-grain).",
    "Added per escalation #1447's own finding (v2/v3): a reader hitting bare 'T1' anywhere in "
    "the project's docs had no glossary entry to check at all, unlike T2/T3 which already had "
    "(cluster_code) entries even before this build. This entry exists to be found by that "
    "search, not to declare a third meaning.")

patch = {
    "_patch_meta": {
        "patch_id": f"PATCH-{NOW.replace('-', '').replace(':', '').replace('T', 'T').rstrip('Z')}Z-PROSE-GLOSSARY-T-SCHEME",
        "patch_type": "PROSE",
        "produced_at": NOW,
        "session_b_status": None,
        "researcher_approval": "PENDING",
        "description": (f"Insert {len(operations)} glossary entries (9 [VRT] T1-T9, 8 [TC] "
                        "T0-T7, 1 disambiguation 'T1') per escalation #1447 v4 full-scope "
                        "approval."),
    },
    "operations": operations,
    "_patch_summary": {
        "total_operations": len(operations),
        "prose_section_inserted": len(operations),
    },
}

out_path = "iba/docs/1447-glossary-t-scheme-entries-patch-v1-20260904.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(patch, f, indent=2, ensure_ascii=False)
print(f"wrote {out_path}: {len(operations)} operations")
