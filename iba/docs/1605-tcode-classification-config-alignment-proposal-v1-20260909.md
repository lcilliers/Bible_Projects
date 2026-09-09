# T-code / cluster-classification config alignment — full proposal

- **filename:** 1605-tcode-classification-config-alignment-proposal-v1-20260909.md
- **date:** 2026-09-09
- **escalations covered:** #1605 (its resolution is gated on this), spawned from #1592
- **purpose:** one consolidated, complete picture of every config row AND every `verse_lexical`
  column that derives (or, per yesterday's redesign, will derive) data from the clusters —
  `is_negator`, `party_kind`, `role`, `status`, plus `cluster`/`cluster_strong`/
  `cfg_lexical_code_class` themselves — what's NEW, what CHANGES, what STAYS, what RETIRES, and the
  open decisions that need your call before anything is applied. Nothing in this document has been
  written to the DB yet.

**Why this document exists:** the last three chat turns corrected each other in place (T4 missing
from my own listing twice, T5/T6 existence in doubt, then my own restatement of `party_kind`'s
source dropping T4 a *third* time). You asked, rightly, for one document instead of more scattered
chat claims. §1 below resolves the specific thing you flagged — it was not a real data conflict.

---

## 0. The thing you flagged, resolved

You quoted my own claim back: *"`is_negator`/`party_kind` ... real, live source is `cluster_strong
WHERE cluster_code='T5'` / `IN ('T7','T8','T9')`"* — and said that looked like it might mean the
source data itself still conflicts. Checked directly against the live code
(`iba/app/lib/lexical.py:240-274`, `load_code_classes` / `_PARTY_CLASS_TO_KIND`), not restated from
memory:

```python
_CLUSTER_CODE_TO_CLASS = {
    "T5": "negator", "T4": "party_adversarial", "T7": "party_divine",
    "T8": "party_human", "T9": "party_angelic",
}
...
_PARTY_CLASS_TO_KIND = {"party_divine": "divine", "party_human": "human",
                        "party_angelic": "non_human", "party_adversarial": "non_human"}
```

**`party_kind`'s real, live source is `cluster_strong WHERE cluster_code IN ('T4','T7','T8','T9')`
— I had dropped T4 from my own restatement.** This is not a data conflict — the code has been
correct and self-consistent the whole time, and its own docstring (lines 247-261) already carries
the full researcher-verdict correction, dated 2026-09-05, in detail. The conflict was purely in
documentation: the stale `cfg_column.use` text (§2 below) *also* drops `party_adversarial`/T4 from
its own list — so the live code, the stale governance text, and my restatement of the fix all
independently under-counted the same thing, three separate times, never the underlying data. `T6`
(Connective) is confirmed **deliberately excluded** from this lookup entirely — it feeds a
different mechanism (`verse_lexical_note`'s `connective` note_type, Layer 2), not
`is_negator`/`party_kind` at all.

Live counts, for grounding (verse_lexical, deleted=0):

| Column | Value | Rows |
|---|---|---|
| `is_negator` | 1 | 8,527 |
| `is_negator` | NULL | 536,045 |
| `party_kind` | divine | 12,075 |
| `party_kind` | human | 5,311 |
| `party_kind` | non_human | 496 |
| `party_kind` | NULL | 526,690 |

Distinct strongs per source cluster_code (live, `deleted=0`): T4=6, T5=7, T6=6, T7=44, T8=1,787,
T9=6.

---

## 1. NEW — doesn't exist in config today

### 1.0 `role` — the central redesign, not yet built, missing from the first draft of this proposal

This was the real gap — `role` is the column #1605 is fundamentally about (the multi-cluster-code
conflict is a `role` question), and it derives from clusters more directly than anything else in
this document, yet it was left out. Checked the live code, not carried over from yesterday's chat:

**Live today, confirmed (`classify_role`, `lib/lexical.py:84-93`):** `role` is computed purely from
`morph_code`/the strong's own H/G prefix — `_GREEK_FUNCTION_TAGS = ("PREP","PRT","CONJ","ART")` for
Greek, an `H9xxx`-range regex (plus an explicit exception set) for Hebrew. **Zero cluster reference
anywhere in its computation.** Not cluster-derived at all, currently — matches its own live
`cfg_column.use` text exactly (checked, accurate, no drift): *"'content' (independent lexical item)
or 'function' (grammatical formative...)"*.

**Corrected, researcher instruction verbatim, 2026-09-09** (supersedes the "single scalar value"
framing below, which was too narrow — trying to align the new design with the old content/function
shape instead of stating it on its own terms): *"Role is the primary source for stating each word in
the verse, from the span, using the span strong, to the cluster or clusters that the strong belongs
to. Having more than one is not an error. This membership has various implications. if it is a
M-code it is likely to be a char. if it has multiple M-codes, then the meaning of the word need to
be resolved in Layer 2 by considering both options. if it is a M-code + T-code then there is tight
connection which need to be read in layer 2 together. if it is a T-code then the type of T-code has
a material impact on its treatment in Layer 2. Layer 1 has only one task. To accurately and
completely determine which codes in the clusters is linked to the strong. No find is an error and
must not silently be ignored."*

**What this settles, restated to make sure it's captured right:**
- `role` is not a single scalar picking one cluster_code — it's **the complete set** of cluster_code
  values the strong belongs to, found and recorded in full. This directly settles the "priority pick
  vs. multi-valued" open question from yesterday's §9.2/§9.5 — **multi-valued, complete enumeration,
  nothing dropped.**
- Multiple memberships (dual-M, M+T, or otherwise) are **not an error at any point** — not a Layer 1
  data-quality problem, not something #1605 needs to "resolve" by picking a winner.
- Layer 1's ONLY job here is **accurate, complete discovery** of cluster membership. The
  *implications* of what's found (single-M → likely characteristic; multi-M → Layer 2 weighs both
  senses; M+T → read together as a tight connection; pure T → treatment depends on which T-code) are
  **Layer 2's job to act on**, not Layer 1's job to pre-resolve or collapse.

**Question 1 answered, researcher instruction verbatim, 2026-09-09:** *"T2 for the purposes of role
in layer 1 is treated exactly the same. it is not ignored but stated."* Settled — T2 is not a special
case at the Layer 1 recording level; every finding, T2 included, is simply stated like any other
cluster_code. §5.0 is not fully resolved by this alone (it was about which *combinations* are
by-design vs. need data reconciliation, a slightly different question), but it does settle that
Layer 1 itself must never special-case or suppress T2 — carried into §5.0 as evidence, not treated as
closing it outright.

**A second requirement added, researcher instruction verbatim, 2026-09-09, not in the first draft of
this section:** *"I also note you did not include the error check on null. no cluster = no strong and
therefore incomplete on the foundation."* — a strong carrying **zero** cluster_code membership at all
is not a quiet default, it's a foundational data gap that must be surfaced as an error, every time.

Checked live, to ground this rather than leave it abstract: **107 distinct strongs (108,163
verse_lexical rows, live, `deleted=0`) currently have NO live `cluster_strong` row at all** —
`vl_strongs - cs_strongs`, exact match, not base-stripped since both tables carry the specific
(suffixed) code. **100% of those rows are `role='function'`.** Sampled: almost entirely Greek
prepositions/conjunctions/adverbs — `G0575` "away from" (606 rows), `G1519` "toward" (1,603 rows),
`G1893` "since" (25 rows), `G1854` "out/outside(r)" (60 rows), etc. — real, frequent function words,
not edge cases. **This is a different, smaller residual pool than #1598's own leftover 4,155 common
nouns + 2,651 proper nouns** (that pool is content-shaped; this one is 100% function-shaped) — worth
naming as its own gap, not assumed already covered by #1598's closure.

**Storage/mechanism, not decided:** "the complete set of cluster_code values, found and stated in
full, with a NULL-set itself flagged as an error" naturally means `role` becomes a denormalized list
(comma/JSON, same shape already used to check the 96 multi-code strongs), with an explicit
error/incompleteness marker (a flag, or NULL treated as itself the error signal rather than a
tolerated absence) rather than a bare NULL indistinguishable from "checked, has none." Not proposed
here — a build-time question once the rest of this section is confirmed.

**Proposed disposition, unchanged in substance:** still not rewriting `role`'s `cfg_column.use` or
building this yet — record the confirmed design (multi-valued, complete, T2 included, NULL-set is an
error) as a `cfg_method_rule` (step=`lexical.build`) once storage shape and §5.0 are settled, then
update `cfg_column.use` and the code together, in the same unit of work, when it's actually built.

### 1.1 Lexical readiness validation check — formalizes §1.0's NULL-check as a whole-pipeline gate

**Researcher instruction, verbatim, 2026-09-09:** *"the lexical readiness validation check is: all
verses in iba.verse has a span, every strong in the span is in iba.strong and every strong has at
lease 1 cluster allocation. this should be built into the config."* Three legs, checked live against
the actual data rather than left as a definition on paper:

| Leg | Definition | Live result |
|---|---|---|
| 1 | Every `verse` has ≥1 live `span` | **PASS — 0 missing.** All 29,759 live verses have ≥1 span. |
| 2 | Every `strong_variant` code referenced in a live `span` resolves to a live `strong` row | **FAIL — 409 distinct codes** referenced in spans have no `strong` row at all (e.g. `G0007G`, `G0010`, `G0084`...). A different, upstream grain from the already-known 559 `verse_lexical.status='unregistered'` rows (CA-2) — this one is pre-Layer-1, counted in distinct codes, not built rows. |
| 3 | Every live `strong` has ≥1 live `cluster_strong` allocation | **FAIL — 109 of 15,293** live `strong` rows have zero cluster allocation. Reconciles exactly with §1.0's 107: of the 109, **107 already occur in built `verse_lexical` rows** (the same 107 found there), **2 are onboarded but never yet reached a build** (a `strong` row exists, no span/verse_lexical activity yet). |

This is the correct frame for §1.0's NULL-check — not a `role`-only concern, but the third leg of a
formal three-stage completeness gate for the whole base-data-through-classification chain. Leg 1 is
already fully met; legs 2 and 3 are real, quantified, live gaps.

**Proposed for config:** a `cfg_method_rule` (work_package likely `lexical` or a shared
`readiness`/`base-data` scope — not decided here) stating the three-leg definition verbatim, plus —
per `governance.reports_must_persist` — an actual runnable check that persists its result to a
config-defined report path, not just a rule description. Building the runnable check itself is a
separate task from registering the rule; not proposed as code in this document.

**Escalation #1606 raised, 2026-09-09** — where this gets coded and where corrective action for
legs 2/3's live failures gets decided; carries the leg-2/leg-3 findings above in its own context so
they don't need re-deriving there.

### 1.2 A gap the redesign surfaces: `T6` has no Layer 1 surfacing column at all

Checked, not previously noted: `T4`/`T5`/`T7`/`T8`/`T9` are each denormalized onto `verse_lexical`
via `party_kind`/`is_negator` — Layer 2 gets that classification for free just by reading the row.
**`T6` (Connective) has no equivalent column.** The `connective` `note_type` (Layer 2,
`verse_lexical_note`) has to be independently re-derived by the LLM from scratch every time, with no
lexicon assist — confirmed live: **zero references to `cluster_strong`/`cluster_code` anywhere in
`lexicalenrich.py` or `lexicalenrichgenerate.py`.** Not a defect in either module — `T6` was simply
never wired up the way `T4/T5/T7-9` were. Candidate fix (not decided here): a mechanical
`is_connective` column, same pattern as `is_negator`, sourced from `cluster_strong WHERE
cluster_code='T6'` (6 live strongs) — cheap, same shape as the rest of this document's §2 fixes, but
new rather than a correction, so flagged here rather than folded into §2.

**T4/T5/T6 membership review, researcher-driven, 2026-09-09** — full listing exported:
[`outputs/t4-t9-cluster-membership-20260909.csv`](../../outputs/t4-t9-cluster-membership-20260909.csv)
(1,856 rows, T4-T9). Spot-checking T4 against words a researcher would expect to find there surfaced
a real gap, confirmed 3 for 3, not a one-off:

| Strong | Gloss | Found at | Finding |
|---|---|---|---|
| `H7451H` | bad: evil | M58 (Wickedness) only | Never touched T4 |
| `H7307G` | spirit | M47 (Inner Seat) only | Never touched T4; co-occurs with `H7451H` in exactly 1 live verse, Judg.9.23 ("an evil spirit between Abimelech and the leaders of Shechem") |
| `H3049` | spiritist (necromancer/medium) | T2 (Supplementary) only | **Fixed live, 2026-09-09** — moved to T4 (`cluster_strong` id 17225), its T2 row (id 15622) retired the same turn: *"H3049 should definitely be added to T4"*, then *"there is no reason for multi membership. T4 only is fine. we must not abuse multi membership — multi membership must [have] a really good reason."* Corrected from an initial (wrong) additive fix — see the principle below. |

**Root cause, not three unrelated misses:** `H3049`'s own T2-allocation rationale (escalation #1598
Phase O, the pool-closing sweep) names exactly which buckets were checked before defaulting to T2 —
*"T3/T7-T15/M-code sweeps"*. **T4, T5, and T6 are not in that list.** The sweep that closed the
untagged pool never actually checked candidacy against the three finer party/negator/connective
buckets at all — every word now sitting in T2 has never been evaluated against T4/T5/T6, not just
the handful spot-checked here.

**Corrective action recorded on escalation #1606, 2026-09-09** (researcher instruction verbatim:
*"add to the actions for the cleanup to redo T2 sweep for T4, T5, and T6"*): redo the pool-closing
sweep, scoped specifically to check every live T2-tagged strong against T4/T5/T6 membership — same
method #1598 used, extended to the three codes it skipped. Distinct from #1606's leg-2/leg-3
base-data gaps (missing `strong` rows, zero-cluster strongs) — this is a T2-pool re-classification
pass over data that already exists, not a base-data gap.

**A general allocation principle, stated the same turn, not scoped to `H3049` alone:** *"there is no
reason for multi membership. T4 only is fine. we must not abuse multi membership — multi membership
must [have] a really good reason."* Recorded here because it recalibrates something already written
in this document, not left standing uncorrected:

- §1.0's "having more than one [cluster_code] is not an error" is still right about **Layer 1's
  discovery job** — find and state every real membership, never suppress one. It does not mean
  **allocation** should default to stacking tags. `H3049`'s corrected fix is the model: T4 alone,
  once T4 is confirmed correct, not T2+T4 side by side.
- **This bears directly on §5.0 and the 37 T2-vs-M-code strongs already in #1605** — this document
  had been treating most of the 37 as "record both, let Layer 2 read them together," on the strength
  of the earlier "M+T = tight connection" framing. Under this principle, the default should likely
  flip: **resolve to one code unless there's a specific, stated reason for two**, the same way
  `H3049`'s T2 tag turned out to be a default-closure artifact, not an independently-justified second
  fact. Not silently re-decided here — flagged so §5.0/§5.1 get revisited under the corrected
  principle rather than carrying the old framing forward.

**T2 resweep for T4/T5/T6 — run, 2026-09-09** (researcher instruction: proceed, then find other
allocation anomalies and redo the T2 scan). Scoped by morph shape, not the raw 6,374-strong T2 pool:
49 Greek (CONJ/PRT) + 73 Hebrew (HT*/HC*/AC*) = **122 checked individually against T5/T6's own live
definitions** — pronouns, interrogatives, interjections, and demonstratives sharing the same morph
tags were rejected, not swept in wholesale. Applied live: **42 → T6 (6 → 48 members)**, **4 → T5 (7
→ 11)**, each superseding (not coexisting with) its T2 row, per the principle above. Includes
`H0834A` — the Hebrew relative particle "which," 5,448 occurrences — now T6, not T2. T4 untouched by
this batch: CONJ/PRT/particle morphology doesn't match T4's noun-shaped membership (named beings),
confirmed rather than assumed not to be a gap here.

**6 left flagged, not auto-decided** (genuinely ambiguous — T2 stays until you call it): Greek
`G0302` "if" (an — a modal particle, not a standalone conjunction), `G1223` "through/because of"
(dia — primarily a preposition), `G0687` "no?" (mēti — interrogative-negative particle); Hebrew
`H0637` "also" (additive adverb vs. coordinating), `H0371` "isn't?" (interrogative-negative),
`H2098` "this" (HTr-tagged but demonstrative-shaped).

**Other allocation anomalies from today's session, per your instruction — one resolved, two still
open, not silently decided:** `H3049` is closed (above). `H7451H`/`H7307G` (found earlier this
section, never given an explicit decision the way `H3049` got) remain open — still just M58/M47,
never added to T4. And #1605's own namesake list — **the original 37 T2-vs-M-code strongs** — was
flagged against this same no-unjustified-multi-membership principle but not yet re-run; a larger,
separate re-evaluation, not attempted in this batch.

**Round 2, 2026-09-09** — researcher instruction verbatim: *"I think the six can also be added. these
words all trigger that layer to must look further for any related words/activity."* All 6 applied to
T6, superseding their T2 rows. **T6: 6 → 48 → 54.** This also clarifies T6's real scope going
forward, worth carrying into its `cluster.description` at some point (not done here): not limited to
strict clause-linking grammar — a word that triggers Layer 2 to look for related words/activity
qualifies, even where its own part of speech is a preposition/particle/interrogative rather than a
conjunction proper.

Full trail: escalation #1606.

### 1.3 A method rule stating the preliminary-allocation / reach-back principle

**Your instruction, verbatim, this session:** *"the allocation is preliminary... it is quite
possible, and expected that the in-context evaluation of the strong's allocation is worth a deeper
look. When that occurs, it is not an error of allocation, it is an opportunity for expanded
interpretation, and should trigger a reach back into the base data to get the full meaning analysis
of the word."*

Nothing in config states this today as a general principle. The closest existing thing is
`cfg_method_rule` id 64 (`t2-supplementary-not-blanket-irrelevant`, escalation #1598, already live
— see §3) — but that rule is scoped narrowly to "is a T2-tagged code relevant in this verse," a
relevance question. Your instruction is broader: it's a **sense-selection** question — when a
strong's live `cluster_strong` allocation (M-code, T-code, or a dual/conflicting combination of
either) doesn't fit a specific verse-occurrence, Layer 2 doesn't silently pick a winner or flag a
data error — it reaches back into the full base lexical/meaning data for that occurrence.

**Proposed new `cfg_method_rule`** (step=`lexical.enrich`, generalizes rule 64's philosophy rather
than duplicating it):

> `rule_key`: `cluster-allocation-is-preliminary-triggers-reach-back`
> `rule_text`: A strong's live `cluster_strong` cluster_code assignment (M-code, T-code, or more
> than one of either) is a preliminary, candidate classification, not a final resolution. When
> Layer 2's in-context reading finds a specific verse-occurrence doesn't fit the strong's default
> allocation — including a strong carrying two or more live cluster_code values simultaneously —
> that is NOT treated as an allocation error to silently reconcile or a data-quality flag to
> resolve by picking one code. It is evidence the word may carry a richer or different sense in
> that specific context, and MUST trigger a reach-back into the strong's full base meaning data
> (`strong_meaning_parsed`/`strong_sense`/etc., the same stores `resolved_sense` draws from) for
> that occurrence's own analysis, recorded as a Layer 2 note — never a silent Layer 1 reallocation.
> Generalizes `t2-supplementary-not-blanket-irrelevant` (#1598) from a T2-relevance question to
> every preliminary cluster allocation.
> `source_doc`: escalation #1605, 2026-09-09, researcher instruction verbatim.

### 1.4 `cluster_code` as a registered `cfg_enum`

No `cfg_enum` group for the cluster_code taxonomy exists today (checked — no `cluster` or
`cluster_code`-named group in the 40 live groups). Proposed: register one, values = the 95 live
codes' short identifiers (M01...M80-ish range, T2...T15, FLAG — exact list generated from live
`cluster` at apply time, not hand-typed), each carrying a one-line pointer to where its full
definition lives (`cluster.description`) rather than duplicating the prose. This is the controlled-
vocabulary registration `governance.project_lookups_and_naming_convensions` calls for — distinct
from, and does not re-open, the settled question of where *per-strong* classification data lives
(§4).

### 1.5 Glossary entries for T5–T15

Confirmed live: `prose.glossary` (`glossary_programme`) has cluster-code entries for **T2, T3, T4
only**. T5–T15 have zero coverage. Plan unchanged from last turn: add all 11, each disambiguated
against the Verse Reading Technique (T1–T9) and Tier Catalogue (T0–T7) schemes per the existing
T1/T4 disambiguation pattern, via `Prose.ps1` export → edit → import → apply (not a direct DB
write).

---

## 2. CHANGES — exists, but wrong or stale

### 2.1 `cfg_column`: `verse_lexical.is_negator`

**Current (wrong):** *"1 if strong is in `cfg_lexical_code_class` WHERE `class='negator'` AND
`active=1`, else NULL..."*
**Proposed:** *"1 if strong's base code is in `cluster_strong` WHERE `deleted=0` AND
`cluster_code='T5'`, else NULL (never 0 — NULL means 'not in the T5 lexicon', a preliminary
classification per `cluster-allocation-is-preliminary-triggers-reach-back`, §1.3). Computed
unconditionally for every code (`mechanical-columns-run-on-every-code-no-selection`, rule 47,
unaffected)."*

### 2.2 `cfg_column`: `verse_lexical.party_kind`

**Current (wrong, and under-counts even on its own stale terms — drops `party_adversarial`/T4):**
*"'divine'/'human'/'non_human' — set ONLY when this code IS ITSELF a name (`cfg_lexical_code_class`
class IN party_divine/party_human/party_angelic)..."*
**Proposed:** *"'divine'/'human'/'non_human' — set ONLY when this code IS ITSELF a name in
`cluster_strong` (`deleted=0`, `cluster_code` IN T4/T7/T8/T9 → party_adversarial/divine/human/
angelic, T4 and T9 both collapsing to 'non_human'; see #1605/CA-15 on the finer T4-vs-T9 distinction
being collapsed at this mapping step, not yet surfaced separately). A pronoun's own party_kind is
NOT stored here — derives via its `entity_link` note's `target_verse_lexical_id`. Preliminary
classification per `cluster-allocation-is-preliminary-triggers-reach-back`, §1.3."*

### 2.3 `cfg_table`: `iba.cluster`

**Current (stale count):** *"...T2 is the landing zone for codes not included in analysis; FLAG is
unresolved/needs-review; M01-M46 are the named inner-being characteristics."*
**Proposed:** *"...80 live M-codes (M01+) are the named inner-being characteristics; FLAG is
unresolved/needs-review; T2–T15 (14 codes) are the non-M-code axis — T2 (excluded/supplementary)
and T3 (Operations) sit closest to the thematic axis, T4–T14 are an explicitly orthogonal
referent-identity axis that can coexist with an M-code assignment by design, T15 is a closed
non-analytic list (Hebrew calendar months). All cluster_code allocation, M or T, is a preliminary
candidate classification (`cluster-allocation-is-preliminary-triggers-reach-back`) — the full,
current definition of each code lives in this table's own `description` column, not restated here."*

### 2.4 `cfg_method_rule` id 46: `lexical-code-class-lookup-not-hardcoded`

**Current (wrong mechanism):** *"Every code-classification lexicon (negator, connective-type,
party_kind's divine/human/angelic classes) is a queried row in `cfg_lexical_code_class`, never a
hardcoded list/dict in a handler..."*
**Proposed:** *"Every code-classification lexicon (negator=T5, party_adversarial/divine/human/
angelic=T4/T7/T8/T9) is a queried row in `cluster_strong` (filtered by `cluster_code`), never a
hardcoded list/dict — `_CLUSTER_CODE_TO_CLASS` in `lib/lexical.py` names which codes map to which
class, the strong-to-class DATA itself is never hardcoded. `cfg_lexical_code_class` is superseded
(§4) — architecture correction, researcher verdict 2026-09-05, BUILD.md #228/#229. A code absent
from the relevant cluster_code is reported UNCLASSIFIED/NULL — never guessed, never silently
defaulted, and per `cluster-allocation-is-preliminary-triggers-reach-back` (§1.3), NULL/absent is
itself a preliminary state, not necessarily a permanent one."*

---

## 3. STAYS — governance already correct, included for completeness, not touched

- `cfg_method_rule` id 47 `mechanical-columns-run-on-every-code-no-selection` — already correctly
  names `is_negator`/`party_kind` as unconditional, every-code computations. Unaffected by the
  source-table fix.
- `cfg_method_rule` id 44 `language-testament-derivation`, id 45 `h0853-function-word-exception`,
  id 48 `narrative-morph-hebrew-only` — unrelated columns, unaffected, listed for completeness since
  they sit in the same `lexical.build` rule set.
- `cfg_method_rule` id 64 `t2-supplementary-not-blanket-irrelevant` (escalation #1598,
  2026-09-08) — already live, already states the same underlying philosophy for the T2-relevance
  case specifically. §1.3's new rule generalizes it; it is not superseded or duplicated, both stay
  active.
- `cluster_strong.confidence` / `.alt_clusters` / `.review_flag` / `.rationale` — already correctly
  documented in `cfg_column` as the per-allocation-pass provenance/confidence/candidate-alternatives
  mechanism. This is arguably already the DB-level home for "preliminary" — §1.3's rule makes the
  *behavioural* consequence explicit (reach back to base data) rather than adding new columns.
- `cluster_strong.operation` (1 if T3 Operations candidate) — checked live: **not read anywhere**
  in `iba/app/lib/*.py` or `iba/app/handlers/*.py` (grep returned nothing). Apparently dead, same
  shape as `cfg_lexical_code_class`, but a separate finding — noted here since you asked for
  everything related, not folded into this proposal's action list; worth its own look if it's truly
  unused.
- Live `T6` description (Connective) already correctly states it stays one bucket by design (not
  split into causal/coordinating/purpose) — confirmed against the code, which deliberately excludes
  T6 from `load_code_classes` (§0). No change needed to `cluster.description` for T6 itself.
- **`resolved_sense`'s M-code gate (`load_mcode_strongs`, `cluster_strong WHERE cluster_code LIKE
  'M%'`) is still called on every build (`lib/lexical.py:476/526/550`) but does nothing** — its own
  in-code comment says so plainly: superseded 2026-09-07 by #1575 (`resolve_code()` no longer writes
  `resolved_sense` for ANY word, so the M-code gate has nothing left to gate), *"threaded
  through/loaded (harmless, unused here) rather than ripped out of every call site — a smaller,
  separate cleanup if it's ever a problem."* Already self-documented, not hidden — noted here as
  another cluster-derived computation, currently vestigial, not actioned in this proposal.
- **`status`'s `cfg_column.use` is currently accurate, not stale** — live text describes
  `'resolved'`/`'unregistered'` (does a `strong` row exist), which matches current live behaviour
  exactly; `status` is **not cluster-derived today**. Yesterday's Round 1 instruction proposed
  redefining it to "meaning-data readiness" (Meaning Ready / Meaning to be pulled / Meaning not
  applicable), the third value keyed on **T2 membership** specifically — which, like `role`, is
  designed-but-not-built and would make `status` cluster-derived once it lands. Its own source-table
  question (§9.5 Q3 of the 1592-1595 doc: "ready against which table(s)?") is still open and isn't
  re-decided here — flagged so it isn't lost, same treatment as `role` in §1.0.

## 4. RETIRE — superseded, not just old

- **`cfg_table` row `cfg_lexical_code_class`** — its `use` text claims it's *"queried by
  `lexical.build`/`lexicalenrich.py`, never hardcoded"* — confirmed false, dead code. Mark
  `inactive=1`; correct `use` text to state superseded-by-`cluster_strong`, with the reason
  (researcher verdict 2026-09-05: assigning a strong's special status is cluster territory, not cfg
  territory — full record BUILD.md #228/#229) preserved on the row, not deleted.
- **`cfg_column` rows for `cfg_lexical_code_class.class`** and the two stale rows on
  `verse_lexical.is_negator`/`.party_kind` referencing it — the `verse_lexical` two get corrected
  text (§2.1/§2.2, not retired, since the *columns* are live); the `cfg_lexical_code_class.class`
  row itself retires alongside its parent table.
- **`cfg_enum` group `lexical_code_class`** (7 values: `negator`, `connective_causal`,
  `connective_coordinating`, `connective_purpose`, `party_divine`, `party_human`, `party_angelic`)
  — mark every row `inactive=1`. Confirmed concretely, not just by the old ruling: the
  `connective_*` 3-way split was never built (live `T6` is one bucket, checked directly against
  `cluster.description` and the code's own exclusion of T6 from `load_code_classes`), so this enum
  doesn't even accurately describe the rejected design it came from, let alone the live one.

---

## 5. Open decisions — need your call, not decided here

### 5.0 The coexistence-scope question — still open, gates `role`'s build (§1.0)

Raised two turns ago, not yet answered directly: your rule *"co-existence should only be allowed
between M and T2 and between M-codes where the meaning literally can fall in different M-code
clusters"* — read literally, this allows only **M+T2** and **M+M**, putting every M+T4/T5/T6/T7-T14
combination into "sort out." Read as shorthand for "M+T-code broadly," it leaves the #1598-approved
referent-identity axis (T4/T7-T14, explicitly "orthogonal, can coexist" in their own live
`cluster.description`) alone, and scopes "sort out" to T-only combinations with no M present at all
(`T7+T8`, `T13+T14`, `T2+T3`, etc. — real, found in the corpus). This still matters concretely: it's
the one input `role`'s build (§1.0) and the final shape of #1605's own strong-list both need before
either can be finished, not a side detail.

### 5.1 The ~14 no-rationale strongs in #1605's 37

Per §1.3's new principle, most of the 37 T2-vs-M-code strongs plausibly resolve as "record + Layer
2 reach-back," not a reconciliation task. But ~14 of them (G1414, G1415, G1654, G2900, G2999, G5400,
G5591, H3027W, H4751, H7293, and a few more from the full list in the prior document) carry **no
rationale at all on either the T2 or the M-code row** — pure `old-system-migration` carry-over, both
facts asserted with zero reasoning behind either. Does your preliminary/reach-back principle cover
these too (treat as legitimate dual-sense candidates, record + flag for Layer 2 like the other ~23),
or do these specifically need a first-pass sanity check (are both tags even real, or is one simply
migration noise) before they're trusted enough to hand to Layer 2 at all?

### 5.2 T4's collapse into `non_human` alongside T9 (CA-15, restated) — CLOSED, 2026-09-09

**Researcher instruction, verbatim:** *"you are perfectly right, there is a duplication. However, I
saw party_kind to be a separate signal. there are a number of questions in the catalogue that is
specifially around divine impact on the char. by retaining party_kind as an additional focussed
signal, it will immediately escalate the divine questions into focus."*

**Decision: `party_kind` STAYS**, not merged into `role`/retired despite the confirmed overlap with
`role`'s complete cluster_code enumeration (§1.0) — deliberately kept as a fast, dedicated trigger
signal for the catalogue's divine-impact-on-characteristic questions, a different job from `role`'s
general complete-membership readout. This also resolves the T4-vs-T9 collapse question directly: the
coarse divine/human/non_human grain is fine precisely because `party_kind`'s real purpose is a fast
divine-detection trigger, not a full referent-identity readout — when the finer T4-vs-T9 distinction
is actually needed, Layer 2 pulls it from `role` (once built), not from `party_kind`. **Not yet
done:** `party_kind`'s `cfg_column.use` text (already flagged wrong-source-table in CA-6/§2.2) should
gain this rationale when that text gets corrected, same unit of work as CA-6, not applied here.

---

## 11. §5 status, 2026-09-09 — all three open decisions closed

- **§5.1 (the ~10 no-rationale strongs) — CLOSED, confirmed live.** All 10 (`G1414, G1415, G1654,
  G2900, G2999, G5400, G5591, H3027W, H4751, H7293`) now carry exactly one live cluster_code each,
  individually sanity-checked during #1605's rounds 1-3 (2026-09-09), not blanket-trusted or
  blanket-flagged. `H7293` ("Rahab") is the one exception with two live codes (M08+T11) — a real
  per-item call (Rahab-as-Egypt-byname, T11's own worked example), not a rubber-stamp.
- **§5.0 (coexistence-scope) — CLOSED**, confirmed by the same evidence: of the 37, 36/37 resolved to
  a single live thematic code; the one exception (`H7293`) is M+T11, the referent-identity axis
  coexisting by design. Reading: **T2 never survives alongside anything else** (retired in favour of
  the real code, or left standing alone = genuinely non-analytic); **T7–T14 keeps coexisting with
  M/other T7–T14, by design**; **M+M** remains permitted per §1.0 when genuinely justified (untested
  by this batch, no live counterexample found).
  - **New gap found scanning the live table beyond the 37** (not part of #1605's original scope,
    which was T2-vs-M specifically): 13 strongs carry a live M+T3 or T2+T3 combination. **Researcher
    verdict, verbatim, 2026-09-09: "the M+T3 is perpectly normal, accept as is, it will be subject to
    context validation when the verse comes into focus."** 12 of 13 (G2373, G2647, G2919, G3618,
    G4994, G5607, H1777, H3513H, H3513I, H3513J, H7665, H8199) need no action — confirmed by-design,
    same shape as the T7-T14 axis (a word can be both a characteristic and a generic operation).
  - **`H3477H` (the 13th, T2+T3) — investigated, not yet resolved.** Live gloss is "Jashar" (the Book
    of Jashar, a proper-noun reference — Josh.10.13, 2Sam.1.18), **not "upright"** — a same-root
    homonym-suffix collision with the real "upright" words, which the row's own `cluster_strong`
    rationale had already flagged as a risk ("translit-only precedent (homonym risk)"). The real
    Hebrew "upright/uprightness" words (`H3477G`, `H3477I`, `H3476`, `H4339`, `H5229`, `H3483`,
    `H6968`) are all already live-tagged M12 (Justice) — nothing missing there. Disposition for
    `H3477H` itself (T3-only vs. something else) still pending researcher confirmation.
- **§5.2 — CLOSED**, see above.

Recorded on escalation #1607 (the six-point Layer 1/2 column review this proposal feeds into) rather
than #1605 itself, which was approved and closed 2026-09-09T10:53:31Z before this round of
closures — #1605's own scope (the 37 T2-vs-M strongs) is unaffected, fully resolved as recorded there.

---

## 6. What happens next

Two tracks, not one, now that `role`/`status` are in scope:

- **Buildable now, independent of §5.0:** §2 (the four corrected texts), §4 (retire
  `cfg_lexical_code_class` + its enum), §1.3 (the new preliminary/reach-back rule), §1.4 (`cluster_code`
  enum), §1.5 (glossary T5–T15). Pending your confirmation on §5.1/§5.2, I run these as one
  `Config-Maintenance.ps1 -Step Propose` batch (approval-gated regardless), then the glossary entries
  via `Prose.ps1`.
- **Blocked on §5.0:** `role`'s actual redesign (§1.0) and the final #1605 strong-list can't be
  finished until the coexistence-scope question is answered — building either now risks the same
  kind of rework this document itself was written to stop. §1.2 (`is_connective`) and `status`'s
  redesign (§3) are candidate follow-ons, not proposed for this batch.

Per-column validation (the six-point template from two turns ago) starts only after both tracks
close, per your own sequencing instruction.
