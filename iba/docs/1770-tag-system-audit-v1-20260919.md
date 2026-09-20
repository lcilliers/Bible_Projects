# `ib_observation.tag` — full system audit

Built per your instruction on escalation #1770: *"Restart the whole concept of tagging... create a
new md with an extract of every tag in enums, every tag mention in the code, every usage config for
tag management and every piece of code that setup tag operations for llm."* Everything below is
read live from the running system today (2026-09-19), not from memory or from the design docs cited
— those are cross-referenced for history, not treated as current truth.

**Related prior work, not superseded by this doc, worth reading alongside it:**
[`iba/docs/1706-tag-taxonomy-consolidation-v1-20260917.md`](1706-tag-taxonomy-consolidation-v1-20260917.md)
did a full consolidation pass 2 days ago and is where the current 21-value list actually came from.
This audit's job is different: show what's *actually live in code* today, which has already drifted
from that design in at least one place (§4).

---

## 1. Every tag in `cfg_enum` (group `ib_observation.tag`) — 21 registered values

| ordinal | value | active | live observation count (all stages) |
|---|---|---|---|
| 0 | `instance-meaning` | **inactive** | 0 |
| 1 | `verse-grouping` | active | 19 |
| 2 | `difference-inference` | active | 54 |
| 3 | `surface-gloss-divergence` | active | 197 |
| 4 | `no-human-context` | active | 14 |
| 5 | `cross-cluster-significance` | **inactive** | 0 |
| 6 | `data-error` | active | 0 |
| 7 | `alternative-meaning` | active | 19 |
| 8 | `could-not-resolve` | active | 37 |
| 9 | `answered-no-flag` | active | 4,356 |
| 10 | `tightly-related` | active | 330 |
| 11 | `no-direct-connection` | active | 313 |
| 12 | `qualifier-for-term` | active | 80 |
| 13 | `no-impact` | active | 458 |
| 14 | `not-related-to-meaningful-word` | active | 834 |
| 15 | `sole-mcode-in-verse` | active | 156 |
| 16 | `cluster-pole-negative` | active | 8 |
| 17 | `cluster-pole-positive` | active | 5 |
| 18 | `attested-pre-nt` | active | 141 |
| 19 | `nt-coinage` | active | 1 |
| 20 | `needs_adjacent_verse_context` | active | 24 |

**`cfg_column.use` for `ib_observation.tag`** (corrected 2026-09-17, escalation #1706): *"enum,
cfg_enum-governed (ib_observation.tag) — shared across all stages, not partitioned per stage; most
tags apply wherever the relevant condition arises... ib_observation is one unified record set
populated across stages, not fragmented enum groups per stage."* This is the stated design intent.
§3 below shows the code does not actually implement it as one unified thing.

## 2. Live usage by stage (7,046 total observations)

| stage | tag | count |
|---|---|---|
| verse-reading | answered-no-flag | 3,726 |
| verse-reading | not-related-to-meaningful-word | 802 |
| verse-reading | no-impact | 453 |
| verse-reading | tightly-related | 310 |
| verse-reading | no-direct-connection | 282 |
| verse-reading | surface-gloss-divergence | 177 |
| verse-reading | sole-mcode-in-verse | 156 |
| verse-reading | attested-pre-nt | 137 |
| verse-reading | qualifier-for-term | 78 |
| verse-reading | alternative-meaning | 16 |
| verse-reading | difference-inference | 9 |
| verse-reading | cluster-pole-negative | 6 |
| verse-reading | could-not-resolve | 5 |
| verse-reading | cluster-pole-positive | 4 |
| char-answers | answered-no-flag | 630 (**84.2%** of char-answers' 748 rows) |
| char-answers | could-not-resolve | 32 |
| char-answers | not-related-to-meaningful-word | 31 |
| char-answers | needs_adjacent_verse_context | 24 |
| char-answers | no-human-context | 14 |
| char-answers | no-direct-connection | 13 |
| char-answers | no-impact | 3 |
| char-answers | alternative-meaning | 1 |
| char-reading | difference-inference | 37 |
| char-reading | tightly-related | 20 |
| char-reading | verse-grouping | 19 |
| char-reading | surface-gloss-divergence | 19 |
| char-reading | no-direct-connection | 18 |
| char-reading | no-impact | 2 |
| char-reading | alternative-meaning | 2 |
| char-reading | cluster-pole-negative | 1 |
| char-subgroup | difference-inference | 8 |
| char-subgroup | attested-pre-nt | 4 |
| char-subgroup | qualifier-for-term | 2 |
| char-subgroup | surface-gloss-divergence | 1 |
| char-subgroup | nt-coinage | 1 |
| char-subgroup | not-related-to-meaningful-word | 1 |
| char-subgroup | cluster-pole-positive | 1 |
| char-subgroup | cluster-pole-negative | 1 |

`data-error` and `instance-meaning`/`cross-cluster-significance` (the 2 inactive values): 0 live
rows anywhere.

## 3. Every piece of code that sets up tag operations for the LLM

Four independent generator modules, each building its OWN `tag_values` list and its OWN guidance
text — this is the concrete evidence behind §1's "shared, unified" design intent not actually being
implemented as one thing:

| module | stage(s) | how it gets `tag_values` | how it explains tags to the model |
|---|---|---|---|
| `versereadinggenerate.py` (`_instructions`, line 216, 284) | verse-reading | own query: `SELECT value FROM cfg_enum WHERE name='ib_observation.tag' AND inactive=0` | **owns `TAG_GUIDANCE`** (line 258) — a dict with real definitions for 8 tags (see §3a) |
| `charanswergenerate.py` (`_instructions`, line 123, 177) | char-answers | same query, own call site | imports and reuses `versereadinggenerate.TAG_GUIDANCE` (fixed 2026-09-18, escalation #1770 v3 — **this fix is the one you sent back for revision**) + 3 char-answers-specific behavioural sentences (`needs_adjacent_verse_context`/`could-not-resolve`/`answered-no-flag`) |
| `charreadinggenerate.py` (`_instructions`, line 179, 259) | char-reading | same query, own call site | **does NOT use `TAG_GUIDANCE` at all** — a third, separate, hand-written prose block (line 283-294) explaining 9 tags in its own words: `tightly-related`, `no-direct-connection`, `verse-grouping`, `difference-inference`, `surface-gloss-divergence`, `no-human-context`, `data-error`, `could-not-resolve`, `needs_adjacent_verse_context` |
| `subgroupgenerate.py` (`_instructions`, line 107, 131) | char-subgroup | same query, own call site | **zero guidance** — line 163 is a bare `Valid tag values: {tag_values}` with no explanation of any of them |

**`recordingpass.py` — the only write-time enforcement**, `_validate_tag` (line 172): checks the
model's returned `tag` is a real, active `cfg_enum` value for `ib_observation.tag` — rejects an
invalid/inactive tag outright. This is enforcement of *validity*, not of *correct choice* — it
cannot catch a model picking `answered-no-flag` when a more specific tag genuinely applied.

### 3a. `TAG_GUIDANCE` (`versereadinggenerate.py`, the one real shared dict) — full contents

| tag | guidance text given to the model |
|---|---|
| `qualifier-for-term` | the word functions as a MODIFIER (manner, intensifier, or other state/measure/intensity enhancer) of another word's action or quality, rather than naming a disposition/operation/quality in its own right |
| `no-impact` | the occurrence's surface form/stepGloss carries no distinguishing nuance beyond the term's base sense — a real 'no divergence' finding, not an absence of an answer |
| `not-related-to-meaningful-word` | the sub-question's target item genuinely does not exist or apply for this term/verse — a real negative finding, not a shrug |
| `sole-mcode-in-verse` | no other M-code characteristic co-occurs in this verse at all |
| `cluster-pole-negative` | this term occupies the negative/negligent pole of a dual-natured cluster |
| `cluster-pole-positive` | this term occupies the positive/virtuous pole of a dual-natured cluster |
| `attested-pre-nt` | the term is attested in classical/pre-NT Greek or Hebrew usage |
| `nt-coinage` | the term has no attestation before the NT period |

### 3b. Tags with NO definition anywhere in code (not in `TAG_GUIDANCE`, not in either hand-written block)

- **`alternative-meaning`** — registered, live (19 uses), never explained to the model anywhere.
- **`instance-meaning`** — inactive, 0 live rows. Per `1706-progressive-relational-verse-reading-v1-20260917.md` line 180: *"`instance-meaning` is currently a tag, but it's actually a window"* — flagged there as a category-confusion candidate for retirement. Its inactive status may already reflect that, but nothing records the decision explicitly.
- **`cross-cluster-significance`** — inactive, 0 live rows, but this is the SAME tag escalation #1768 found missing: a front-loaded observation (written by cluster A's pass for a strong that actually belongs to cluster B) should get this tag and doesn't, because it's off. `cfg_method_rule` #105 (`cross-family-flagging-out-of-scope-this-build`) independently confirms: *"Its own tag value is not yet chosen... inventing one here would bake a design decision into a code build."* So this tag exists, is the obvious candidate, and is switched off pending a decision that was deliberately deferred.

## 4. Config governing tag management

- **`cfg_enum` group `ib_observation.tag`** — §1 above, the vocabulary itself.
- **`cfg_column` `ib_observation.tag`** — §1 above, the "unified, shared" design statement.
- **`cfg_method_rule`** rows that govern individual tags' meaning/usage (none of these are wired
  into any prompt text — they live only in the method-rule table, read by a human, not by code):
  - `#97 homonym-no-context-earmarked-and-left` — defines `no-human-context`.
  - `#98 data-errors-flagged-separately` — defines `data-error`.
  - `#104 adjacent-context-flagged-not-fetched-answer` / `#74 needs-adjacent-verse-context-applies-here` — define `needs_adjacent_verse_context`, across 2 separate rule rows for 2 different stages.
  - `#105 cross-family-flagging-out-of-scope-this-build` — the `cross-cluster-significance`
    deferral (§3b).
- **`cfg_behaviour_rule` `test-plan-per-module-utility`** (id 46) — applies to any future change
  here: a test plan covering every meaningful interaction/parameter combination, run after build,
  results recorded in the escalation resolution — not just asserted.
- **No `cfg_setting` governs tag behaviour directly** — no threshold, no per-stage tag allowlist, no
  config-driven mapping from stage to its own valid tag subset. Every stage currently pulls the
  SAME full active-tag list (`WHERE inactive=0`, no stage filter) and it's each module's own prompt
  prose, not config, that steers the model toward stage-appropriate tags.

## 5. What this adds up to (observations, not recommendations — you asked for the extract, not a fix)

1. The stated design ("one unified, shared enum, most tags apply wherever the condition arises") and
   the actual code (4 independent guidance implementations, one with zero guidance, one that just
   got built-then-reverted) are not the same thing today.
2. `answered-no-flag` dominance (84.2% in char-answers, 76.5% overall in verse-reading) tracks
   closely with which tags have NO explanation reaching the model: `alternative-meaning` is real,
   live, and completely undefined; several char-reading-only tags never reach char-answers or
   char-subgroup's prompts at all since each module queries independently with no stage-scoping.
3. `cross-cluster-significance` sits inactive, already correctly identified in #1768 as the missing
   piece for cross-cluster signposting, and independently already flagged as deliberately deferred
   in `cfg_method_rule` #105 — this is a decided-but-unresolved gap, not an unknown one.
4. No config artifact currently enforces *which* tags are valid for *which* stage — `_validate_tag`
   only checks a tag exists and is active, globally, regardless of stage.

Nothing built or changed by this audit. Waiting on your direction for what "restart from scratch"
should actually produce.
