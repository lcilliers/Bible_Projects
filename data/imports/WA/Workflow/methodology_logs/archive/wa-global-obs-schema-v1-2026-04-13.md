# WA Global — Observations Schema Proposal

**Filename:** wa-global-obs-schema-v1-2026-04-13.md
**Date:** 2026-04-13
**Version:** 1.0
**Previous output ref:** wa-global-general-rules-v1-2026-04-13.json
**Status:** Design proposal. Not yet implemented. For researcher review before schema work begins.

## Change note

Version 1.0. Initial proposal. Shape of tables specified by researcher (2026-04-13) in the compassion audit session. Depth: Option (ii) — core tables plus supporting structure, concept visible, not full DDL.

\---

## 1\. Purpose

This document specifies the schema for the `Proj\_observations` table and its entity-index tables. These tables become the authoritative analytical store for the Framework B Soul Word Analysis programme. Every (b) entity-linked analytical observation produced by Session B, Session C, or Session D is written to this store. The markdown observations log becomes a session narrative; the database holds the analytical content.

The schema supports reproducibility: a word study for any registry can be produced by reading observations keyed to that registry and the entities owned by it (terms, verses, groups, dimensions, roots) and rendering them into prose per the Session C rule (GR-OBS-006).

\---

## 2\. Scope

This schema holds category (b) observations from the three-category model (GR-OBS-002):

> \*\*(b)\*\* Entity-linked observation — recorded in Proj\_observations with a key to one or more entities (verse, term, registry, group, dimension, xref, root).

It does **not** hold:

* **(a) Dropped items** — superlatives, impression-making statements. These have no database home.
* **(c) Forward pointers** — Session B and Session D pointers already live in existing tables (`wa\_session\_b\_findings`, `session\_d.sd\_pointer\_flags`, `session\_research\_flags`). They remain there. When a pointer is resolved, the resolution produces a (b) observation in `Proj\_observations` that references the pointer record via `related\_obser\_id`.
* **Session management records** — patch history, instruction change logs, session progress narratives. These live elsewhere (`patch\_history`, instruction documents, session logs).

\---

## 3\. Core table — `Proj\_observations`

One row per analytical observation. This is the analytical content.

|Field|Type|Notes|
|-|-|-|
|`id`|INTEGER PK|Stable identifier.|
|`obser\_desc`|TEXT|The analytical comment. Plain prose. The substantive content.|
|`delete`|INTEGER (0/1)|Obsolete marker. 0 = active; 1 = obsolete. Obsolete observations are retained for audit, not destroyed.|
|`study\_segment`|TEXT|Section-level linking. Identifies which derived-output segment this observation belongs to. Controlled vocabulary — see Section 7.|

### Supporting metadata fields (recommended additions)

The shape you specified is the minimum. I recommend these additional fields for audit and reproducibility, but they are additive — if you prefer the minimum shape only, these can be held in a sibling table.

|Field|Type|Notes|
|-|-|-|
|`origin\_session`|TEXT|Session that produced this observation. E.g. "Session B Pass 1", "Session B Dimension Review", "Session C", "Session D".|
|`origin\_registry\_id`|INTEGER FK|The registry whose session produced this observation. Not the same as the entity the observation is keyed to — a Session D observation about Reg 23 may originate from the C17 cluster synthesis session.|
|`origin\_instruction\_version`|TEXT|The instruction document version under which the observation was produced. E.g. "WA-SessionB-Instruction-v4.7".|
|`created\_date`|DATE|Date the observation was written.|
|`obsolete\_reason`|TEXT|If `delete` = 1, the reason this observation is obsolete.|
|`obsolete\_date`|DATE|If `delete` = 1, the date it was marked obsolete.|
|`superseded\_by\_id`|INTEGER FK|If `delete` = 1 and a newer observation replaces this one, the id of the replacement. Self-referential FK to `Proj\_observations.id`.|

### Design notes on `Proj\_observations`

* **One observation per analytical comment.** Do not bundle multiple distinct comments into one row. Splitting them supports precise obsolescence marking and precise reuse.
* **`obser\_desc` is free prose.** No controlled vocabulary. The content is whatever the analytical comment says. A comment about H2347 *chus* appearing most often in prohibition contexts is written as prose: "H2347 *chus* appears in 16 of 24 verses in judicial-prohibition contexts (group 3182-002). The withholding of pity is the term's most frequent frame in the corpus."
* **`delete` field is the obsolete marker.** Following GR-OBS-005, observations are never destroyed. Wrong, stale, or superseded observations are flagged obsolete. The `obsolete\_reason` records why and the `superseded\_by\_id` links to the replacement when one exists.
* **`study\_segment` declares the rendering target.** Following GR-OBS-006, this is how observations link to reader-facing prose. The writer of Section 4 RACHAM family declares a set of observations whose `study\_segment` matches that section, and renders from them. See Section 7 for the controlled vocabulary.

\---

## 4\. Entity index tables — `obser\_\[entity]\_index`

One table per entity type. Each row links an observation to one entity instance. An observation about a single entity has one index row. An observation about a relationship between two entities has two index rows (one per entity), linked by sharing the same `obser\_id`.

Entity types (one table each):

|Table|Links to|Purpose|
|-|-|-|
|`obser\_verse\_index`|`verse\_context`|Observations about a specific verse.|
|`obser\_term\_index`|`wa\_term\_inventory` (including delete-status)|Observations about a specific term. Per GR-OBS-004, delete-status terms are permitted.|
|`obser\_registry\_index`|`word\_registry`|Observations about a whole registry. Registry-level syntheses (e.g. "the four-root-family structure of the compassion vocabulary") live here.|
|`obser\_group\_index`|`verse\_context\_group`|Observations about a verse context group.|
|`obser\_dimension\_index`|`wa\_dimension\_index`|Observations about a dimension assignment. The reasoning for why group 1613-001 is "Relational Disposition / GOD" lives here.|
|`obser\_xref\_index`|correlation partner record|Observations about a cross-registry relationship. E.g. "Compassion and Mercy share 38 terms, the connection runs through the ELEEIN and SPLANCHN families."|
|`obser\_root\_index`|root\_family (by `root\_code`)|Observations about a root family. E.g. "The RACHAM family connects compassion and love through shared womb-root vocabulary." Per researcher direction 2026-04-13, root is a first-class entity.|

### Shape (common to all entity index tables)

|Field|Type|Notes|
|-|-|-|
|`id`|INTEGER PK|Stable identifier for this link row.|
|`obser\_id`|INTEGER FK|References `Proj\_observations.id`.|
|`\[entity]\_id`|INTEGER FK|References the entity record. Field name varies per table: `verse\_id`, `term\_id`, `registry\_id`, `group\_id`, `dimension\_id`, `xref\_id`, `root\_id`.|
|`related\_obser\_id`|INTEGER FK nullable|Optional reference to another observation. Used for (i) pointer resolution (the new (b) observation points at the pointer it resolves), (ii) supersession (the new observation points at the one it replaces), (iii) reasoning chains (an observation that builds on an earlier one).|

### Design notes on the index tables

* **Multi-entity observations use multiple index rows.** An observation about the Compassion↔Love RACHAM root connection writes one row in `Proj\_observations`, and two rows in `obser\_root\_index` (keyed to RACHAM for Reg 23 and for Reg 103), or alternatively one row in `obser\_xref\_index` (keyed to the Compassion↔Love xref). The choice depends on what the observation is *about* — if it is about the root, key to root; if it is about the registry pair, key to the xref. If it is about both, write both.
* **`related\_obser\_id` is the supersession/resolution/chain link.** Per GR-OBS-005, it is used when:

  * A (b) observation resolves a (c) pointer — the observation's index row references the pointer record id.
  * A new observation supersedes an older obsoleted one — the index row references the older observation id.
  * One observation builds on another — the index row references the foundation observation.

  The field is on the index, not on `Proj\_observations` itself, because the relationship may be entity-specific. An observation that supersedes an older one for one entity but stands independently for another entity can record this cleanly.

* **The `obser\_xref\_index` and `obser\_root\_index` link to entities that are not fully first-class in the current schema.** Correlation xrefs are currently held in `correlations.xref\_sharing` (a derived view); root families are held in `correlations.root\_families` and in `wa\_term\_inventory.root\_family` (a JSON sub-field). Implementing the schema will require promoting these to first-class tables with stable ids, or keying the index tables to a composite id (e.g. `(owner\_registry\_id, partner\_registry\_id)` for xref; `root\_code` string for root). I recommend promoting both to first-class tables with stable ids as part of the implementation — this is a clean-up the programme needs regardless.

  \---

  ## 5\. Relationship to existing pointer tables

  Pointers are not moved into `Proj\_observations`. They remain in their existing tables:

|Existing table|Purpose|Interaction with observations|
|-|-|-|
|`wa\_session\_b\_findings`|Session B findings raised during analysis. Includes DIM-23-001 (dimension review finding) and similar.|When a Session B finding is resolved, the resolution writes a new (b) observation to `Proj\_observations` and the index row's `related\_obser\_id` points at the `wa\_session\_b\_findings` record. The finding is marked resolved.|
|`session\_d.sd\_pointer\_flags`|Session D pointers raised by Session B for cross-registry synthesis. SD-001 through SD-025+ for compassion.|Pointers remain unresolved until Session D runs. When Session D resolves a pointer, it writes a new (b) observation with `origin\_session = 'Session D'` and links via `related\_obser\_id`.|
|`session\_research\_flags`|General research flags. Overlaps with sd\_pointer\_flags.|Same pattern as above.|

A pointer that is prematurely treated as a settled conclusion (e.g. SD-019 in the compassion word study) is restored by: (i) the (b) observation that treated it as settled is obsoleted (`delete` = 1, `obsolete\_reason` = 'pointer premature closure'), (ii) the pointer record is marked unresolved, (iii) a new (b) observation is added that acknowledges the pointer as genuinely open. This is exactly the correction pattern the compassion audit needs.

\---

## 6\. `study\_segment` controlled vocabulary

The `study\_segment` field declares which derived-output segment an observation belongs to. This is the Option 2 section-level linking per GR-OBS-006. The vocabulary is controlled but extensible.

### Proposed initial vocabulary

**Word study sections (reader-facing output):**

* `word\_study\_section\_1\_characteristic` — Section 1: The Characteristic
* `word\_study\_section\_2\_how\_it\_works` — Section 2: How It Works
* `word\_study\_section\_3\_verses` — Section 3: The Verses (verse annotations)
* `word\_study\_section\_4\_vocabulary` — Section 4: The Vocabulary (root-family descriptions)
* `word\_study\_section\_5\_connections` — Section 5: Connections and Research Pointers

**Sub-segments for Section 4 (one per root family):**

* `word\_study\_section\_4\_\[root\_code]` — e.g. `word\_study\_section\_4\_racham`, `word\_study\_section\_4\_chesed`, `word\_study\_section\_4\_splanchn`, `word\_study\_section\_4\_eleein\_chus`, `word\_study\_section\_4\_path`

**Sub-segments for Section 5 (one per connection):**

* `word\_study\_section\_5\_\[partner\_reg]` — e.g. `word\_study\_section\_5\_reg\_111\_mercy`, `word\_study\_section\_5\_reg\_103\_love`

**Analytical brief sections (internal, Session D handoff):**

* `brief\_section\_2\_meaning\_findings`
* `brief\_section\_3\_divine\_dimension`
* `brief\_section\_4\_somatic\_signature`
* `brief\_section\_5\_spirit\_soul\_body`
* `brief\_section\_6\_session\_c\_corrections`
* `brief\_section\_7\_correlation\_connections`
* `brief\_section\_8\_cross\_word\_questions`
* `brief\_section\_9\_open\_items`

**Other:**

* `unassigned` — the observation has not yet been assigned to a segment. This is a temporary state during Session B pass work, before the writer decides where it lands.
* `cross\_segment` — the observation applies to multiple segments and is used by rendering in more than one place.

### Design notes on `study\_segment`

* **The caveat from researcher direction (2026-04-13):** "Something valuable may lie outside the declared boundaries. Too much structure too early blocks creative thinking." The `study\_segment` value is the writer's declaration of where this observation belongs, not a rigid constraint. Writers may identify insights that do not yet have a segment, and a new segment value can be added to the vocabulary as needed.
* **One observation can belong to multiple segments.** If it does, set `study\_segment = 'cross\_segment'` and use the index table to record the details (or use the metadata to list applicable segments — this is an implementation choice).
* **Rendering checks the segment declaration.** When Session C renders Section 4 RACHAM family, it reads observations with `study\_segment = 'word\_study\_section\_4\_racham'` (and cross-segment observations that apply). Rendering that introduces a claim not present in the declared set is a violation of GR-OBS-006 and should trigger a gap-filling patch.

\---

## 7\. Worked example — compassion material

To make the shape concrete, here are three observations drawn from the compassion material, shown as they would appear in the new schema.

### Example 1 — A per-term sense-structure observation (Pass 1 Term 13)

**Source (observations log Pass 1 Term 13):** "G4697 splanchnizō appears 12 times in the Gospels. In the one unambiguous human use (Luke 10:33, the Good Samaritan), compassion is the defining quality of the person who correctly answers 'who is my neighbour?'"

**`Proj\_observations` row:**

```
id: 1001
obser\_desc: "G4697 splanchnizō appears 12 times in the Gospels. In 10 of 12 occurrences the subject is Jesus or a parabolic figure representing God (the king in Matt 18:27, the father in Luke 15:20). The one unambiguous human use is Luke 10:33 (the Good Samaritan), where compassion is the defining quality of the person who correctly answers 'who is my neighbour?'"
delete: 0
study\_segment: word\_study\_section\_4\_splanchn
origin\_session: Session B Pass 1
origin\_registry\_id: 23
origin\_instruction\_version: WA-SessionB-Instruction-v4.7
created\_date: 2026-04-11
```

**`obser\_term\_index` row:**

```
id: 5001
obser\_id: 1001
term\_id: \[the wa\_term\_inventory id for G4697 OWNER in Reg 23]
related\_obser\_id: NULL
```

### Example 2 — A correlation-mechanism observation (Pass 6 / Brief Section 7)

**Source (brief Section 7 row for Desire):** "Desire shares 3 terms with compassion through RACHAM/CHESED vocabulary overlap with C04." *This is the factually incorrect version.*

**Correct version after JSON verification:** "Desire and Yearning each share 3 terms with compassion: H2551 *chem.lah*, H2550 *cha.mal*, and H4263 *mach.mal*. The shared vocabulary is the CHEMLAH sparing/compassion root, not RACHAM and not CHESED."

**Corrected `Proj\_observations` row:**

```
id: 1042
obser\_desc: "Compassion (Reg 23) shares three terms with both Desire (Reg 43) and Yearning (Reg 179): H2551 chem.lah (compassion), H2550 cha.mal (to spare), and H4263 mach.mal (compassion). The shared root is CHEMLAH (sparing/compassion), which emphasises restraint on behalf of the other. This is a root-level overlap between the compassion cluster and the C04 desire cluster. The mechanism is not RACHAM (womb) or CHESED (covenantal loyalty)."
delete: 0
study\_segment: word\_study\_section\_5\_reg\_43\_desire
origin\_session: Session B Pass 6
origin\_registry\_id: 23
origin\_instruction\_version: WA-SessionB-Instruction-v4.7
created\_date: 2026-04-13
```

**`obser\_xref\_index` rows:**

```
id: 6001
obser\_id: 1042
xref\_id: \[the xref record for Reg 23 ↔ Reg 43]
related\_obser\_id: NULL

id: 6002
obser\_id: 1042
xref\_id: \[the xref record for Reg 23 ↔ Reg 179]
related\_obser\_id: NULL
```

**`obser\_root\_index` row:**

```
id: 7001
obser\_id: 1042
root\_id: \[the root\_family record for CHEMLAH]
related\_obser\_id: NULL
```

**Obsoleting the incorrect version:** The previous (b) observation that asserted the RACHAM/CHESED mechanism is marked obsolete and superseded by this one:

```
id: 998  (the old observation)
delete: 1
obsolete\_reason: "Factually incorrect. Shared root is CHEMLAH, not RACHAM or CHESED. Verified against wa-023-compassion-complete-2026-04-13-v1.json correlations.xref\_sharing for Reg 43 and Reg 179."
obsolete\_date: 2026-04-13
superseded\_by\_id: 1042
```

### Example 3 — A pointer-resolution observation that restores an open pointer

**Source:** SD-019 (Isa 54:8 temporal asymmetry question) was prematurely treated as settled in the word study. The correction: obsolete the settled-claim observation, mark SD-019 as unresolved, and add a new observation that acknowledges the pointer as open.

**Obsoleting the settled-claim observation:**

```
id: 877
obser\_desc: "Isaiah 54:8 settles the question of which impulse is more fundamental: judgment is temporary, compassion is everlasting."
delete: 1
obsolete\_reason: "Premature closure. SD-019 was raised as a Session D question by Session B Pass 3. The word study treated it as settled. Per GR-OBS-002 and GR-OBS-006, Session D questions are not settled at Session C level."
obsolete\_date: 2026-04-13
superseded\_by\_id: 1065
```

**New observation acknowledging the pointer as open:**

```
id: 1065
obser\_desc: "Isaiah 54:8 establishes a temporal asymmetry in divine inner-being: 'for a moment I hid my face from you' versus 'with everlasting love (chesed) I will have compassion (racham) on you'. A moment of anger versus everlasting love. This is evidence for the question raised in SD-019 (whether compassion is the more fundamental divine characteristic than judgment), not a resolution of it. The question remains open for Session D."
delete: 0
study\_segment: word\_study\_section\_2\_how\_it\_works
origin\_session: Session B Pass 3 (corrected 2026-04-13)
origin\_registry\_id: 23
origin\_instruction\_version: WA-SessionB-Instruction-v4.7
created\_date: 2026-04-13
```

**`obser\_verse\_index` row:**

```
id: 4501
obser\_id: 1065
verse\_id: \[the verse\_context id for Isa 54:8 under H2617B]
related\_obser\_id: \[the sd\_pointer\_flags id for SD-019]
```

**Action on `session\_d.sd\_pointer\_flags`:** SD-019 `resolved` flag is set back to 0 (reopened), with a note explaining the premature closure and the corrective observation.

\---

## 8\. What this schema does not yet specify

These are design questions that will arise during implementation. They are out of scope for this proposal but flagged for the next design pass:

1. **First-class status for xref and root entities.** Both currently live in derived tables (`correlations.xref\_sharing`, `correlations.root\_families`). The index tables need stable ids. Promoting them to first-class tables with id fields is the clean answer; using composite keys is a lighter alternative. Decision needed at implementation time.
2. **Write access discipline.** Which processes are permitted to write to `Proj\_observations` directly, and which must go through a patch? My expectation: Session B writes via patch at pass close (GR-PASS-002); Session C writes via patch when gaps are identified during writing (GR-OBS-006); Session D writes via patch when resolving pointers or identifying conflicts. No process writes directly.
3. **Query patterns.** The Session C rendering process needs to query "all observations with `study\_segment = X` for registry Y, not obsolete." The Session D conflict-detection process needs to query "all observations keyed to verse V across all registries, not obsolete, flagged where two observations make incompatible claims." Query-pattern support may need indexes or views.
4. **Migration of existing material.** The observations currently in markdown (observations logs, briefs, word studies) need to be migrated into the new tables. This is a substantial one-time task. It can be done registry by registry as each registry reaches Session B Stage 3 or Session D entry.
5. **Bundling by pass.** When Session B Pass N closes and writes its observations to the database, should the pass itself be represented as a group (a `pass\_batch` record linking all observations written in that pass), or is the origin metadata on each observation sufficient? A pass\_batch record would support "show me everything Pass 4 added" queries cleanly.

\---

## 9\. Open questions for researcher review

Before implementation begins, these need researcher decisions:

1. **Minimum shape vs. recommended metadata.** The shape specified by the researcher (2026-04-13) has four fields on `Proj\_observations`: id, obser\_desc, delete, study\_segment. Section 3 above recommends additional audit fields (origin\_session, origin\_registry\_id, origin\_instruction\_version, created\_date, obsolete\_reason, obsolete\_date, superseded\_by\_id). Which shape do you want implemented?
2. **Entity promotion for xref and root.** Both need first-class status for the index tables to key against them cleanly. Promote both as part of this implementation, or use composite keys?
3. **Pass batch table — yes or no?** Does each pass produce a batch record that groups its observations, or is per-observation origin metadata sufficient?
4. **`study\_segment` initial vocabulary — accept Section 7 as proposed, or revise?** The proposed vocabulary is derived from the word study and brief structures. If either structure changes, the vocabulary changes.
5. **Rendering-verification procedure.** Under GR-OBS-006, Session C prose must derive from (b) observations. A verification procedure is needed to check that a rendered section contains no claims not present in its declared observation set. Should this be a manual check by the writer, an automated check by a rendering tool, or both?

\---

*Produced under GR-PASS-002, GR-OBS-002, GR-OBS-005, GR-OBS-006. For researcher review before implementation.*

