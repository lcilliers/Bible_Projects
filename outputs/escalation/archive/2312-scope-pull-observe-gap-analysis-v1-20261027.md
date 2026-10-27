# 2312: the scope, the 0.GAP pre pull and the observe step, against the root escalations (v1, 2026-10-27)

Researcher, chat 2026-10-27: 0.GAP pre is cleared of document reading. It pulls into the scope JSON all the existing observations for the verses in the scope, and all the open items for those verses; the search criterion is the verse, and what comes back may cross several subgroups of the verse (not filtered by subgroup). The updated JSON passes to the next phase, which checks the observations for any missing and generates them. That step is not synergy: it is only completing the observations. Check this against the proposed build, validate for missing concepts, then complete the build of these three steps.

All figures are read-only queries on iba.db at 2026-10-27. Nothing has been built or changed.

## 1. What I read

Read in full: `2268-analytic-process-and-reading-plan-v2` (the plan), `2273-2274-reading-phases-and-observation-record-design-v6` (B1, B2), `2275-progressive-reading-design-v2` and `2275-scope-json-contents-v1`; the escalation comments of #2275, #2276, #2278, #2280, #2296; the code in `iba/app/lib/reading.py` (open, observe, `_focus`, `_findings_on`, `_item_subgroups`), `iba/app/lib/versecollate.py` and `escalation.match_open_items`. Not read: `2228-reading-process-design-v2`, `2286-build-plan-v4`, the #2268 rulings review. Where they matter I rely on the plan, which states it carries their rulings.

## 2. The three steps, as you state them and as built

| Step | You state | As built (checked) | Fit |
|---|---|---|---|
| 0.C scope | verses with an objective | `Reading.ps1 -Step Open` keeps the verses, writes the collation (the scope JSON) and `<label>-gaps.json`; `-Objective` required | fits |
| 0.GAP pre: pull the observations | all existing observations for the verses, by verse, across subgroups | the collation pulls only observations with status `draft`; the observe step pulls every status except withdrawn | **partly** (§3.1) |
| 0.GAP pre: pull the open items | all open items for the verses, by verse | the collation matches open items by verse (scope items), and also by cluster, Strong's and strand code | **partly** (§3.2); the pulled items do not reach the observe JSON (§3.3) |
| Observe: complete the observations | check for missing observations and generate them | the observe JSON has a slot per word in focus; the Observe gate wants a node of this reading on each | **partly** (§3.4, §3.5) |

Not filtered by subgroup: confirmed. Neither pull filters by subgroup. The scope's home may be a subgroup (B:120), but it does not restrict what is pulled. Since #2310 each open item also shows the subgroups it reaches.

## 3. Missing concepts and gaps

### 3.1 The pull of existing observations is split and the first pull is short
- Collation (the scope JSON): status `draft` only. Live observations reached through a node: draft 15,118, open 53, resolved 84, silent 27. So **164 are missed** by the collation. The observe step does pull them.
- This is #2276 (B4), on hold. Two pulls of the same thing also breaks RO5 (gather once): the later phase should read what 0.GAP pre gathered.

### 3.2 What "all the open items for those verses, by verse" does today
- 296 open items, all of kind `scope`, each with its own verses; they match by verse only. That fits your rule.
- The code also matches items of kind cluster, Strong's and strand by the codes of the words in the verse, which pulls them into every verse that has such a word. None is open now (the six cluster items were closed yesterday), so today it makes no difference.

### 3.3 Open items are not in the observe JSON
The observe JSON carries per verse the passage, the findings in focus and the words, plus the scope's claims. It does not carry the open items for the verse. Open items are gathered in 0.GAP pre and shown at the Gather step, and matched again at Synergy. Your statement puts them in the JSON that passes to the observe step. This is a missing link.

### 3.4 What counts as an observation already covering a word
This is the concept the plan leaves open.
- The Observe gate (B1, `check`) wants a **node of this reading** on every word in focus (design v6 §4). Of 68,969 nodes, 0 carry a `reading_id` (the four published readings pre-date it). Taken literally, every word of every verse is "missing" however many observations exist (15,282 live observations reach a verse).
- You said existing work is used, not redone (plan P-3, RO3; #2275 R1: a correct older observation is confirmed, not written again).
- Data that limits what an existing observation can cover: 10,179 nodes name a verse and no word, so they cannot cover a word; 63 live observations have no node at all (char-answers 43, char-reading 13, char-subgroup 5, verse-reading 2), so a pull by verse never reaches them.

### 3.5 Which words need an observation (words in focus)
- As built (`reading.focus_words`): every M-coded word, the 5 non-characteristic strongs, and T2 (qualifiers) and T5 (negators) words except function words by morph.
- The plan (#2268 §2 R2, RG-03, RG-07, RG-22) and #2275 v2 say content words of every kind are read: operations (T3), connectives (T6), parties (T7 to T9), body parts (T14), places, objects, nature. Those T-codes are not in focus today, so completing the observations would not look at them.

### 3.6 Two designs of the observe step
The built B1 has Gather, Observe, Record. #2275 v2 (awaiting your approval since 2026-10-25) replaces Gather and Observe by a Lexical layer and a Characteristic layer, each with its own gate, and turns the pre gaps into inputs in the scope JSON. Your three steps match the single Observe of B1 more than the two layers of #2275. Both cannot stand.

### 3.7 Pre-gap types that remain
After #2310 the pre types are term_cluster, meaning_missing, base_missing, term_reading_missing, face_not_gathered, open_item. Base-data gaps stay (RO4). `term_reading_missing` overlaps with the observe step's term and face findings. `face_not_gathered`: of 4,480 ledger strand hits, 4,239 have a face and only 111 are linked to an observation (B8, #2280, on hold), so about 4,128 faces would be flagged as gaps in every scope that has strand hits.

## 4. Decisions (nothing is built until you answer)

| # | Question | Options |
|---|---|---|
| D1 | When does an existing observation cover a word, so the observe step generates nothing for it? | (a) any live observation with a node on that word, in any stage, counts as done; the step generates only what is missing; a re-read that finds one wrong withdraws it with a reason (recommended, inferential: it is P-3 and RO3); (b) as built: every word in focus needs a node of this reading, existing observations given a node on confirmation |
| D2 | Which words are in focus? | (a) as built (M-coded, T2, T5, the 5 strongs); (b) every content word of the verse per RG-03, RG-07, RG-22, function words left out by morph, negators and connectives kept (recommended, inferential: it is the plan's R2) |
| D3 | Open items pulled by verse only? | (a) as now: scope items by verse, other kinds by their code; (b) by verse only, any other kind must be given verse scope when raised (matches your statement; no effect on the 296 open now) |
| D4 | Which observe design stands? | (a) B1's single Observe, completed (recommended: it is your three steps); (b) #2275 v2's Lexical and Characteristic layers |
| D5 | Ledger faces (about 4,128 not linked to an observation) | (a) build B8 (#2280) in this set, so faces are observations before the pull; (b) leave them as the pre gap `face_not_gathered`, settled at Gather |
| D6 | Observations with no node (63) and nodes with no word (10,179) | (a) leave, state the limit in the JSON; (b) give each a verse and word by a separate cleanup item |
| D7 | `term_reading_missing` stays a 0.GAP pre gap, or moves into the observe step where its findings (face, term) are written? | (a) stays; (b) moves to the observe step |

## 5. The build I would make after your answers

| Part | Change |
|---|---|
| P1 | `versecollate`: observations of every status except withdrawn, each with kind, stage, nodes with role, cluster and subgroup code (closes #2276, B4); the observe step reads this pulled set, not the tables again (RO5) |
| P2 | open items per verse in the scope JSON and the observe JSON, with the subgroups each reaches; matching as D3 |
| P3 | the words in focus as D2; coverage as D1; the Observe gate checks exactly that |
| P4 | D4, D5, D6, D7 as decided |
| P5 | test on a copy (B:97): a three-verse trial with one verse carrying observations in two subgroups, one with scope open items, one with a word having only a verse-level node; each gate refuses while gaps stand; results recorded here and on #2276 |
| P6 | BUILD.md, USER-GUIDE.md, config rows through `apply_logged` in the same unit |

## 6. Limits
- D1 to D7 recommendations are mine and inferential; they rest on the plan's rules, not on a test.
- I have not run `Reading.ps1 -Step Open` or `Observe` on a real scope to see the JSON; the account of what they pull is from the code.
- Escalations #2228 design v2, #2286 build plan v4 and the rulings review were not read in full (§1).
