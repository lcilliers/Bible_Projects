# Stage 1 (`lexical.meaning`) — full prompt visibility, real example

Real payload assembled live from `M67` (no API call), 2 of the 3 verses shown for length. This is
exactly what the model receives — nothing paraphrased.

## The instructions (system/task prompt)

```
You are producing verse-reading observations for cluster M67, the pre-subgroup Layer 2 pass
(`lexical.meaning`). You are given, per verse: the verse's own base text, and `roles_in_verse` --
every role-bearing word in that verse (not just this cluster's own member strongs), each carrying
`cluster_codes` (the full set of M-code and role-T-code tags that word carries) and
`is_home_cluster` (true if this word belongs to the cluster you're reading). You are also given
`meaning_sources_by_strong` -- for every strong that IS a member of this cluster, its entries from
up to 3 sources (strong_meaning_tree, strong_lexicon.lsj, strong_lexicon.mounce); read all that are
present as complementary evidence, never picking one and ignoring the others.

Method rules governing this task:
- read-3-sources-complementary
- role-list-includes-unwired-tags
- per-cluster-scope-not-subgroup
- answers-M0.1-M0.5-D7.7
- needs-adjacent-verse-context-applies-here
- cost-bounded-small-batches
- cluster-status-2to3-transition-verse-reading-complete
- strongs-reassigned-detection

Answer these catalogue questions, for every cluster-member strong they apply to:
- D7.7.1: Where this verse contains an action or movement word tagged as an Operation..., what is
  that word's relation to the parties present -- who initiates it and toward whom is it directed?
- M0.1.1: What is the characteristic called in the programme, and what does the name signal?
- M0.1.2: What do the primary Hebrew and Greek terms show at the definitional level?
- M0.1.3: What directional, relational, or constitutional implication does the name carry?
- M0.5.1: What are the primary Hebrew and Greek terms, and what do their root meanings show?
- M0.5.2: What is the grammatical range of the primary term, and what does that show?
- M0.5.3: What is the semantic range of the primary term?
- M0.5.4: Does the vocabulary distinguish disposition vs act, received vs given, condition vs
  quality?
- M0.5.5: Does the vocabulary include a term for the structural opposite?
- M0.5.6: Does the vocabulary include a person-type term (one who habitually exercises this)?
- M0.5.7: Does the vocabulary include a supplication/seeking term?
- M0.5.8: What does the OT/NT vocabulary relationship show about continuity or development?
- M0.5.9: Is there a term newly coined in the NT period?
- M0.5.10: What does the full vocabulary arc show about the complete semantic range?

Valid tag values: [instance-meaning, verse-grouping, difference-inference,
surface-gloss-divergence, no-human-context, cross-cluster-significance, data-error,
alternative-meaning, could-not-resolve, answered-no-flag]

STRICT BOUNDARIES:
- Every `verse` you write must be one of the ones given.
- Every `strong` must be a cluster member (for M0.1/M0.5); D7.7 draws from roles_in_verse.
- Respond with ONLY JSON: {"observations": [{"strong", "question_code", "tag", "obs_text",
  "meaning_source", "occurrences": [{"verse", "surface", "morph_code"}]}]}
```

## The data (real M67 content, 2 of 3 verses)

```json
{
  "cluster_code": "M67",
  "verses": [
    {
      "verse": "2Pet.1.8",
      "text": "For if these qualities are yours and are increasing, they keep you from being ineffective or unfruitful in the knowledge of our Lord Jesus Christ.",
      "roles_in_verse": [
        {"strong": "G1063", "surface": "For", "cluster_codes": ["T6"], "is_home_cluster": false},
        {"strong": "G0692", "surface": "ineffective", "cluster_codes": ["M67", "T2"], "is_home_cluster": true},
        {"strong": "G1922", "surface": "knowledge", "cluster_codes": ["M15"], "is_home_cluster": false},
        {"strong": "G2962G", "surface": "Lord", "cluster_codes": ["M72", "T7"], "is_home_cluster": false}
        // ... every role-bearing word in the verse, 17 total
      ]
    },
    {
      "verse": "2Cor.7.11",
      "text": "For see what earnestness this godly grief has produced in you, but also what eagerness to clear yourselves, what indignation, what fear, what longing, what zeal, what punishment! At every point you have proved yourselves innocent in the matter.",
      "roles_in_verse": [
        {"strong": "G4710", "surface": "earnestness", "cluster_codes": ["M67"], "is_home_cluster": true},
        {"strong": "G0024", "surface": "indignation", "cluster_codes": ["M02"], "is_home_cluster": false},
        {"strong": "G5401", "surface": "fear", "cluster_codes": ["M01"], "is_home_cluster": false},
        {"strong": "G1972", "surface": "longing", "cluster_codes": ["M18"], "is_home_cluster": false},
        {"strong": "G2205", "surface": "zeal", "cluster_codes": ["M18"], "is_home_cluster": false}
        // ... 30 total
      ]
    }
  ],
  "meaning_sources_by_strong": {
    "G0692": {
      "strong_meaning_tree": ["idle, lazy; useless, ineffective; careless", "...2Pet.1.8...ineffective..."],
      "strong_lexicon.lsj": "full classical LSJ entry, ~2000 chars, Greek + citations",
      "strong_lexicon.mounce": "idle, lazy; useless, ineffective; careless"
    },
    "G4710": {
      "strong_meaning_tree": ["hurry, haste; earnestness, diligence, zeal...", "...2Cor.7.11,12;8.16;8.7..."],
      "strong_lexicon.lsj": "full classical LSJ entry, ~3500 chars",
      "strong_lexicon.mounce": "hurry, haste; earnestness, diligence, zeal, eagerness earnest"
    }
  }
}
```

## One structural observation, worth flagging before you dig in

The 14 catalogue questions (`M0.1.1`–`M0.5.10`) are almost entirely **about the word in general**
— its name, root meaning, grammatical range, semantic range, structural opposite, OT/NT
continuity — not about **what this specific verse is doing with it**. Every one of those is
answerable straight from the lexicon entries in `meaning_sources_by_strong`, without engaging the
verse text at all. Only `D7.7.1` (operation-party relation) is inherently verse-specific.

Given the model is asked the *same 14 word-level questions* against *every verse* a strong occurs
in, defaulting to "recite the lexicon" rather than "interpret this particular occurrence" is the
easier, lower-effort path the prompt itself doesn't push back against — which may be exactly what's
producing the flat `instance-meaning`/`answered-no-flag` pattern you and I both found in the tag
distribution. Not a diagnosis, just what the actual prompt structure suggests is worth checking
against your own read of the CSV.
