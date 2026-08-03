# WA — Verse Reading Technique: Base Lexical Reading (v3)

**Filename:** WA-verse-reading-technique-v3-2026-08-03.md
**Date timestamp:** 2026-08-03
**Previous outputs referenced:** supersedes `WA-verse-reading-technique-v1 and V2 and also various prototyping documents


**Version:** 3 — **Final** The researcher manually rewritten this version from other documents to consolidate and normalize the different guidances and instructions.

## Why this exists, and what it does not cover

This document is the canonical instruction for verse reading to create the base lexical reading of a verse. covers one thing: reading a verse's clauses closely enough, from their actual lexical and grammatical data, to establish what each clause actually says — before any question of inner-being phenomena, states, or movements is asked. That later question is a separate step, done separately, once the base reading below is complete for the verse.

This instruction is there to block verse reading in any other way, to prevent verse context drift, prevent reading the standard english translations from the verse table, prevent using matching and searching on verse contents outside of the verse lexical. Any deviation from reading the verse context from the lexical is a direct and serious violation of the IBA App governance.

## Raw data

The raw data for the reading of the verses are in the combination of the following DB tables
(verified 2026-08-03 direct against `iba/app/db/iba.db`; names corrected from the original draft,
which used hyphenated/mixed-case forms that don't match the live schema):

 - verse
 - lemma_inventory
 - span
 - strong
 - strong_lexicon
 - strong_lsj_parsed
 - strong_meaning_tree
 - strong_mounce_parsed
 - strong_related
 - strong_sense
 - strong_verse

**Not in the original list, exists live, relevance unconfirmed:** `strong_meaning_parsed` — a
distinct table from `strong_meaning_tree`, present in the schema. Not added to the list above
pending confirmation of what it holds and whether this reading needs it.

**Input this technique assumes.** The verse-lexical is explicitly based in every span in the verse, the meaning of which is extracted by analysing the parsed tables, which in turn is based on the raw STEP data to derive the meaning per-clause row: `# | surface |
strong | morph | particle | meaning` — where `meaning` carries the stepGloss and related contextual meaning.

---

## The technique, step by step

The technique has two distinct parts:
- the lexical meaning of the verse (T1 - T3)
- the inner being relevance of the words

### lexical meaning

Steps T1 - T3 determined the lexical meaning of every span in the verse within context of the verse and passage

#### T1 — Work from the row, not the gloss
The unit of analysis is the row (surface + strong + morph + full meaning_tree/stepGloss), not the English translation printed above the table. The translation orients the reader; it is not the
evidence. 

- Do not extract English clauses from it and match them against a checklist of keywords.
- Do not dilute reading rows or compromise quality
- Do not skip, ignore, or bypass rows
- Read the row in the context of the nearby rows, do not simply read a row in isolation

#### T2 — Pull the full lexical range before assigning a sense
Read the word's entire meaning_tree entry for its Strong's code(s), not just the stepGloss or the one sense the English translation happens to use. Record explicitly when:
- a sense the English translation does not use is already a standing member of the word's own lexical range — this is **stated via the lexicon**, not inferred from metaphor or surrounding   imagery; say so, rather than treating it as an inference;
- the range is genuinely ambiguous across senses that matter for this verse — name the live senses and reason which is operative here, rather than silently picking one.

#### T3 — Let morph decide voice, person, and aspect — never the English word order or tense
Read the morph code for every verb before deciding tense or voice:
- perfect vs. imperfect vs. participle carry different aspectual force (a passive **participle**
  is a durative/ongoing condition — "is, continually" — not a future event); check this against
  the tense the English translation happens to use, and correct the reading where they diverge;
- person/number (1cp, 3ms, 2mp, etc.) decides who the grammatical subject actually is — do not
  infer this from an English pronoun alone;
- voice (Qal active / Niphal / Pual / Hiphil / passive participle) decides whether the clause's
  grammatical subject is the one acting or the one acted upon.
### T4 — Referent cruxes: name every grammatically live reading, adopt one explicitly, keep the rest on record
When a pronoun or unnamed party is genuinely ambiguous (e.g. "we" in Obad 1 — several readings are
all grammatically live), do not silently resolve it and do not default to the most obvious English
reading:
1. enumerate every reading that is grammatically or contextually live;
2. give the textual grounds for each;
3. adopt one explicitly, stating why, and flag whether the choice is a directed/researcher call or
   this pass's own default;
4. keep the rejected alternatives on record, not just the winner.
### T5 — Record the genre-conventional elements of the verse or passage as an observation. This may be elements expected but textually absent. Do not pass over these elements silently.


T1 - T5 must be completed for all the verses in the passage before the next steps

### Human Inner being relevance

Inner being relevance is NOT the full analysis of the inner being processes. It is merely the preliminary identification of key elements of the words in relation to the inner being.

### T6 - Stamp every word that explicitly points to a human being with *IB*
### T7 — Stamp every word (the noun) that is the causing action as *Agent*. Note that a *IB* can be a *Agent* for another *IB*.
### T8 - Stamp every word that relates to any *IB* in the verse with *Process*. This includes words meant for state/condition/faculty words tied to an IB 
### T9 - Stamp every action word (the verb) with *action*.

A word can carry multiple stamps.  The stamps is indicative, and preliminary, not conclusively.
Separating and distinguising the movement elements such as causing action and resulting condition is not part of the verse lexical and meaning. It will follow later in the study.
Do not perform further analysis to determine which *IB* is affected by which *Agent* and relates to a *process*. Stamping simply highlight words that may have specific relevance in later analysis.
Other non-human beings is likely to the stamped as *agent*. Only human being words is stamped *IB*

## Self checking

Before closing a verse or passage confirm that T1 - T9 for every verse received due consideration and have literally been complied with.

This check is about the intelligent reading of the verse itself; it does not extend to, and is not a check on, any phenomenon or movement judgment — those are a separate step's output, checked there.

Output:

MD - for the narrative of the verse reading (create the MD for the passage by verse)
Json - for the database entry to capture the work in the DB: sample layout below

"_meta": {
    "technique_doc": "iba/docs/WA-verse-reading-technique-v3-2026-08-03.md",
    "source_extract": "", (as per the chat where the source for the verses are specified)
    "status": "test-draft, not written to DB (destination tables not yet defined per researcher Q7)",
    "field_shape": "per technique doc Output section -- each component captured as a loose node",
    "phase_gating": "T1-T5 completed for the whole passage before T6-T9 began, per the technique doc"
  },
  "verses": [
    {
      "osisId": "",
      "t1_t5": {
        "reading": "", (reading of the whole verse meaning after applying t1_t5)
        "flags": [
          {
            "target": "",
            "readings": "" (reading to flag detail)
          }      
      },
      "t6_t9_stamps": [
        {"surface": "", "stamps": [""]}    
      ]
    },

