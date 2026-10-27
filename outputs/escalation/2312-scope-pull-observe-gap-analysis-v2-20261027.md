# 2312: the scope, the 0.GAP pre pull and the observe step, against the root escalations (v2, 2026-10-27)

Version 2 carries your answers to v1's decisions (chat 2026-10-27, verbatim in #2312). v1 is in `outputs/escalation/archive/`. All figures are read-only queries on iba.db at 2026-10-27. Nothing has been built or changed.

## 1. Your answers, as I take them

| v1 | Your answer | What it settles |
|---|---|---|
| D1 | "word" always means the surface with its embedded Strong, never the word registry. verse_lexical, surface_subgroup, cluster_subgroup and cluster_strong give a clean path from any verse to its surfaces, Strongs, subgroups and clusters. There are clear rules on which surfaces get observations; for each surface the new rules define the observations; only the surface's missing observations are added. | The unit is the surface occurrence in the verse. Coverage is per surface and per required observation, not "any node on the word". |
| D2 | Use the observation definition agreed in preparation; do not rework it here. | I evaluate against the agreed rules (§3), not new ones. |
| D3 | See D1 and D2. | Open items are pulled by the verse through the same path (§2). This is my reading; confirm. |
| D4 | Observe is about understanding the surfaces of the verse, not synergy or the story. | The single Observe of B1, completed. #2275 v2's two layers do not stand as designed. |
| D5 | The ledgers were turned into observations in a day; why are they not in observations? | Answered in §4. |
| D6 | not answered | still open (§6) |
| D7 | Correct: the face components are gathered in this phase, the face story is built in the claims. | `face_not_gathered` and `term_reading_missing` stay in 0.GAP pre. |

## 2. The path from a verse, and what the scope JSON holds today (checked)

The path you describe is in the tables: `verse_lexical` (the surface occurrence: verse, position, surface, Strong, morph) to `cluster_strong` (the Strong's clusters) to `surface_subgroup` (cluster, Strong, surface to subgroup) to `cluster_subgroup`. #2295 built a resolver that answers this occurrence-shaped.

The collation (`iba/app/lib/versecollate.py`), the scope JSON today, does **not** use it. Its words are `verse_lexical` joined to `cluster_strong` for M-codes only, with surface, Strong and cluster. So the scope JSON has no subgroup per surface, and no T-coded or untagged surface at all.

So the pull from a verse is:
- surfaces: every `verse_lexical` row of the verse, each with its clusters and its subgroup by `surface_subgroup`, and its occurrence id;
- observations: every non-withdrawn observation with a node on the verse, each node with its surface occurrence (`ib_node.verse_lexical_id` is set on 54,239 of 68,969 nodes), role and subgroup;
- open items: matched through the verse and its surfaces (a scope item by its verses; an item of kind cluster, Strong's or strand through the surfaces' clusters and Strongs).

Not filtered by subgroup; the subgroups of each surface and item are shown.

## 3. The agreed definition of what a surface needs (D2; read, not changed)

From plan #2268 v2 §3 and §4, design #2273/#2274 v6 §1, `cfg_setting reading.observation_parts` and the method rules on `reading.observe`:
- **Which surfaces** (RG-03, RG-07, RG-22, RG-23, RG-24): every M-coded surface, and every T-coded surface found relevant; content words are read even with no cluster tag; operations (T3), movement, negators, connectives, body parts, places, objects, nature are read; function words get no observation of their own, except negators and connectives; a T2 word is read as the qualifier of what it binds to; five listed strongs are never a characteristic. This is the definition; today's `reading.focus_words` (M-codes, T2, T5 and the five) is narrower than it.
- **What each surface needs:** its **role** in the verse (RG-03, a node role), its **face** (RG-09: how it appears here, why it differs from its other occurrences), and the **term reading result** (meaning in context, surface variants, related terms; RW-02, kind `term`). Findings of the other kinds (party with route, statement, link, use, qualification) are recorded where the verse shows them (RG-17: nothing forced to fit); a surface with no inner-being bearing gets a `silence` finding with its reason (RW-11 names missing data as a gap).
- **Limit of this reading:** the rules do not list, per kind of surface, the required set as one table. The set above (role, face, term result for every surface in focus; the rest as the verse shows) is my reading of them. Please confirm it, or point me to the place in preparation that states the set (Q1).

## 4. D5: the ledger faces (checked, not assumed)

You are largely right: the observations exist. They are not linked, and not all are faces.
- 4,239 ledger strand hits carry a face. 3,068 of them (72%) have a live observation with a node on the same verse and Strong: 2,436 from the strand-reading stage (the key statements), 2,453 from the prior-capture (#2305; some hits have both), 9 from verse-reading.
- Only 959 of the 4,239 have an observation of kind `face`; the rest sit in other kinds (mostly key-statement and statement).
- **1,171 hits (28%) have no observation on that verse and Strong.**
- The link is missing: `reading_strand_hit.observation_id` is set on 111 hits (all origin-of-thought) and on none of the anger, fear and life-death hits (4,122 faces), so the pre gap `face_not_gathered` would flag all of them.
- Limit: I matched on verse and Strong, not on the surface occurrence; where a Strong occurs twice in a verse a match may be to the other occurrence. I have not read the observations to judge that they say what the hit's face says.

So the gather in 0.GAP pre has two jobs (D7): link each hit to the observation that already holds its face (3,068 candidates, to be checked per occurrence), and write the face finding for the hits that have none (1,171 candidates). No rebuild of the ledgers.

## 5. The build, revised (after your answers; still to be approved)

| Part | Change |
|---|---|
| P1 | Scope JSON (`versecollate`): per verse, every surface occurrence with its clusters and subgroup (through `surface_subgroup`), its occurrence id, and whether it is in focus by the agreed rules (§3); every non-withdrawn observation with its nodes, each node's surface occurrence, role and subgroup (closes #2276, B4); the observe step reads this pulled set (RO5) |
| P2 | Open items per verse in the scope JSON, matched as in §2, each with the subgroups it reaches |
| P3 | `reading.focus_words` restated to the agreed definition (§3); config through `apply_logged` |
| P4 | Observe JSON: per surface in focus, the observations it already has (role, face, term, other kinds) and the ones missing; only the missing ones are slots to fill. The Observe gate checks each surface in focus for role, face and term finding (or `silence` with a reason), counting an existing node on that surface occurrence |
| P5 | Gather in 0.GAP pre: link hits to their existing face observations, write face findings for the rest (§4); `face_not_gathered` measured per occurrence |
| P6 | The two-layer design of #2275 v2 is not built; #2275's non-superseded parts (retiring the API steps) stay for you to rule |
| P7 | Test on a copy (B:97): three verses (one with observations in two subgroups of the same cluster; one with a repeated Strong; one with a T-coded and an untagged content word); each gate refuses while a required observation is missing; results here and on #2276, #2280; BUILD.md, USER-GUIDE.md |

## 6. Still to be answered

| # | Question |
|---|---|
| Q1 | Is "role, face and term result for every surface in focus; other kinds as the verse shows; silence with a reason" the agreed set (§3)? If preparation states the set elsewhere, where? |
| Q2 | An existing node counts for a surface occurrence by `verse_lexical_id` (54,239 nodes). For the other 14,730 nodes (10,179 name a verse and no word): (a) count them for a surface only when verse, Strong and surface match and the match is unique in the verse; the rest do not count; (b) they do not count until given an occurrence by a separate cleanup item |
| Q3 | D3 as read in §1: is open-item matching through the verse's surfaces, clusters and Strongs right? |
| Q4 | D6 (v1): 63 live observations have no node and cannot be reached from a verse: leave them with the limit stated in the JSON, or a cleanup item? |
| Q5 | The two readings of D5 gather in §4 (link, then write the rest): is that the gather you meant? |

## 7. Limits
- Q1 to Q5 recommendations are not given where I have no basis; the §3 reading of the definition is mine and inferential.
- I have not run Open or Observe on a real scope; the account of the scope JSON is from the code (`versecollate.py`) and the #2275 scope-json account.
- #2228 design v2, #2286 build plan v4 and the #2268 rulings review were not read in full.
