# Layer 1/2 column map — open items action plan

- **filename:** 1607-open-items-action-plan-v1-20260909.md
- **date:** 2026-09-09
- **escalation:** #1607
- **source:** every item below is pulled from the open-decisions register (§3) of
  [`1607-layer1-layer2-six-point-column-map-v1-20260909.md`](1607-layer1-layer2-six-point-column-map-v1-20260909.md) —
  read that doc's own column entry for full detail; this file is for deciding + planning the action,
  not re-arguing the finding.
- **How to use this file:** review mode — add your decision/notes directly under each item's
  **Researcher decision** line, and the action, timing, or corrections under **Action** if it differs
  from what's drafted. Edited in place, round by round; not versioned until you say it's done.

---

## D1 — `role` storage shape

**What needs deciding:** how the complete cluster_code set gets stored on the row (denormalized
comma/JSON list — same shape already used ad hoc to check the 96 multi-code strongs), and how a
NULL-membership (zero cluster_code at all — 107 strongs / 108,163 rows today) gets flagged as an
*error*, not a quiet absence indistinguishable from "checked, has none."

**Options on the table:**
- Storage: comma-list vs. JSON array (both already used informally elsewhere in this project).
- Error marker: a dedicated flag column, vs. treating a genuinely-checked NULL as itself the error
  signal (needs a way to distinguish "not yet checked" from "checked, found nothing" if so).

**Researcher decision:**
>  Role is almost the validator that the base data is ready for lexical analysis.  It can be approached in two ways: a) validate before any analysis start b) pre-validate before any run starts for the scope of the run.  I prefer b)
> if role is null for any word in the span for the scope the validation fails and the run does not proceed.
> I do not see a role value being more than 3 or 4 cluster codes. the storage option should be consistent for all columns. I would suggest we use json as a standard, it is easy pass it through to the next layer, and I assume one can easily use it in reporting and queries (although you will need to teach me how). 
> if base data change for a cluster, then it invalidates or affects all the downstream work. 
> the current 500k rows, plus the deleted rows are all redundant. there is no sense in trying to patch it. effectively all lexicals will be redone.

**Action:**
> build pre-validator routine, with quality check and failure message.  processing gated.
> confirm json is best format
> soft delete all current lexicals before first actual run starts.

**Status:** Open

---

## D2 — `status`'s meaning-readiness source table — SUPERSEDED, gated on #1613

**What needs deciding:** once `status` becomes `Meaning Ready` / `Meaning to be pulled` / `Meaning
not applicable` (T2), which table backs "meaning is available" — the same source-table question
`resolved_sense` needed (now answered: `strong_meaning_parsed.gloss`) but not yet confirmed for
`status` specifically. May be the same table, may not.

**Options on the table:**
- `strong_meaning_parsed` (same table `resolved_sense` now uses) — readiness = "does a row exist
  here."
- A different/earlier table (`strong.stepGloss`, `strong_sense.head`) — readiness = "does *any*
  gloss exist," a lower bar than `resolved_sense`'s own source.

**Researcher decision (pre-#1613, kept for the record — flagged as not reliable as-is, 2026-09-09):**
> layer 1 informs, layer 2 decide the action to be taken
> meaning readiness is only applicable for M-codes. To
> layer 1 check if strongs in role each have a meaning layer. I may be wrong, but in my mind is that it has a parse table reference, if not the status change to meaning incomplete.

**Researcher note, 2026-09-09:** *"D2 is gated on this [#1613] because I just discovered that D2
would have not got the correct data, or made the correct assessment."* Correct — this decision's own
"check if it has a parse table reference" test is exactly the check that would have gone wrong: run
against `strong_meaning_parsed` alone (the table D3/`resolved_sense` settled on), it would have
wrongly marked the 45 Greek strongs that have real `strong_lsj_parsed`/`strong_mounce_parsed` data
but no `strong_meaning_parsed` row as "meaning incomplete," when real meaning data exists for them
elsewhere. Same root cause as D3, same fix needed before this can be built correctly.

**Action:**
> Superseded by #1613 — hold until the base-data normalisation work settles which table(s) a
> readiness check should actually test against.

**Status:** On hold — gated on #1613

---

## D3 — `resolved_sense` truncation boundary — SUPERSEDED, gated on #1613

**What needs deciding:** the 100-character cap is settled; the cut rule isn't. Two live samples cut
mid-word under a flat 100-char cut (`"...to u"`, `"...to spe"`).

**Options on the table:**
- Hard cut at exactly 100 characters, regardless of where it lands.
- Cut at the last complete `;`-boundary clause at-or-under 100 (cleaner, but length then varies row
  to row).

**Investigating this surfaced a bigger, prior problem, 2026-09-09:** `resolved_sense`'s already-
settled source (#1605 §9.1/§9.3: `strong_meaning_parsed.gloss` only) was decided without full
visibility into the base-data meaning layer — checked live, **45 Greek strongs have real lexicon
data in `strong_lsj_parsed`/`strong_mounce_parsed` but no `strong_meaning_parsed` entry at all**,
so they'd get `resolved_sense=NULL` under the current design, not by rule, just by the source's own
blind spot. Escalation **#1613** raised to normalise the base-data meaning layer properly before
this gets built — the truncation-boundary question here is premature until #1613 settles what the
actual source/coverage should be.

**Researcher decision:**
>

**Action:**
> Superseded by #1613 — hold this item until the base-data normalisation work settles the real
> source/coverage question; the truncation format is a smaller decision that fits inside whatever
> #1613 lands on, not a separate track.

**Status:** On hold — gated on #1613

---

## D4 — `pairing` format (was `ambiguity_note`) — CLOSED, 2026-09-09: no Layer 1 column

**What needs deciding:** same-span scope is settled; the value *shape* isn't. Three candidates,
costed against real spans in the source map:

| Option | What it stores | Cost |
|---|---|---|
| 1 — sibling ordinals | comma-list of other `code_ordinal`s in the span | Free — grouping already exists |
| 2 — sibling code+role list | comma-list of `strong (role)` for each sibling | Cheap — one join, self-contained |
| 3 — interpreted binding | free text naming the grammatical relationship | Real build — needs a new prefix/suffix morph-code attachment lexicon that doesn't exist yet |

**Researcher decision:**
> retracted - dropped

**Claude — tested against 4 real live examples, 2026-09-09:** first split the T6 pool by shape —
**60.5% of live T6 occurrences (32,142/53,116) are already prefix/suffix-bound** (share a span with
a sibling code, e.g. Hebrew waw-conjunctive riding on its host word) — these need **no new
mechanism at all**, they're already the existing same-span multiterm case. Only the remaining
**39.5% (20,974) are standalone tokens** (own span, own position) — this is where the new coupling
idea actually applies. Tested it against 4 real standalone cases:

- **`H0834A` "which/that," Job 22:15, pos.3** — a relative particle. Its antecedent is the
  immediately preceding content word ("way," pos.2) — clean, purely positional, **evident from
  Hebrew word order alone, no interpretation needed. Works exactly as described.**
- **`G2532` "and," 1Tim.1:5, pos.8 and pos.11** — coordinates a 3-item noun list (heart / conscience /
  faith). Mechanically fine (preceding + following content span, evident from word order) — but
  **"conscience" sits between two separate `G2532` couplings** (heart-conscience, conscience-faith),
  so a single content word can need **more than one pairing at once**. Bears directly on the format
  question above — a single pointer/value won't hold this, whichever format is chosen needs to allow
  a list.
- **`G1063` "for," Matt.6:34, pos.7** — a **causal clause connector**, not a word-to-word coupling —
  it links the whole preceding clause to the whole following clause ("do not be anxious... FOR
  sufficient for the day is its own trouble"). **A nearest-word rule breaks down here**: the nearest
  content words on either side (pos.6 "anxious," pos.8 "itself"/pos.9 "Sufficient") aren't
  meaningfully "the two things being coupled" — the real coupling is between clauses, which isn't
  recoverable from position alone without clause-boundary logic, which is exactly the kind of
  extrapolation the instruction says Layer 1 must NOT do.

**So: it works cleanly for word-scoped T6 members (relative particles, short-range list
coordinators) — real, mechanical, contributes something Layer 2 currently has to re-derive from
scratch every time. It does not reduce cleanly for clause-scoped T6 members (causal/purpose/temporal/
conditional connectors — `G1063`/`G2443`/`G3752`/`G1437`/etc., a meaningful share of the 55-member
T6 pool) without either (a) accepting a coupling that names the whole preceding/following span run
rather than one word, a bigger Layer 1 build, or (b) leaving those particular T6 members without a
Layer 1 `pairing` value at all and letting Layer 2 handle clause-scoped connectives separately.**
Worth deciding which, rather than assuming one mechanical rule covers all 55 T6 members uniformly.

**Researcher decision, 2026-09-09:** *"I partially agree, by adding the role t6 explicitely in
layer 1, the expectation is that layer 2 will consider every t6 word, and not cherry pick a few and
drop other silently. the pairing column does not add any further benefit."*

**Resolution:** `pairing` is **dropped as a Layer 1 column** — confirmed no benefit beyond what
Layer 2's own verse-context read already does (per the 11 live `connective`-note test cases above),
so nothing is lost moving it entirely to Layer 2. **The coverage question is answered a different
way than a per-note_type trigger:** once `role` (D1) lists T6 explicitly and completely for every
code — with a NULL/missing membership treated as an error, not a silent absence — Layer 2 has no
cover for silently skipping a T6-tagged word the way the current 11-notes-out-of-53,116-occurrences
pattern does today. **This is the same mechanism that should close D9's own coverage gap** — once
`role` reliably lists T3 (operation-verb) membership the same way, Layer 2 is expected to consider
`verb_argument` for every T3-tagged code, not attempt it opportunistically. Cross-referencing, not
duplicating: D9's "trigger condition" sub-question is likely answered by D1's completeness mandate
directly, not a separate mechanism — worth confirming when D9 is worked.

**Action:**
> Remove `pairing`/`ambiguity_note` from the Layer 1 build plan. `verse_lexical` keeps its existing
> `ambiguity_note` column only until the rename/retirement is actually built — no further design work
> needed on format/scope. Layer 2's `connective` note_type (and `verb_argument`, D9) inherit the real
> completeness obligation once `role` (D1) is built and enforced.

**Status:** CLOSED — no Layer 1 column; coverage handled via `role`'s completeness mandate (D1),
carried into Layer 2's own note-type coverage obligation (also relevant to D9).

---

## D5 — `narrative_morph` Greek signal

**What needs deciding:** what the Greek equivalent of the Hebrew wayyiqtol/az-imperfect flag should
actually capture. No mechanism proposed yet — Greek's own narrative-sequencing signal is more the
aorist/imperfect/historical-present distinction *in context* than a single morph-code flag, so this
needs your steer before any design, not just a decision between options.

**Researcher decision / steer:**
>

**Action:**
>

**Status:** Open — needs direction, not just a choice

---

## D6 — `updated_at` "required" scope

**What needs deciding:** you called this column required this session. Two different things that
could mean:

- Every future *correction* sets it — already true today, mechanically, in `write_readings_for_span`.
  No behaviour change needed.
- Every row carries a non-NULL value, including on first INSERT — a real behaviour change (currently
  only 20.9% of rows are non-NULL, because INSERT never populates it).

**Researcher decision:**
>

**Action:**
>

**Status:** Open

---

## D7 — `verse_lexical_note.passage_id`

**What needs deciding:** drop the column, or repurpose it. Live: 0/173 rows carry a non-NULL value —
every Layer 2 write happens in the verse-scoped mode #1451 made the default, so the column's stated
purpose ("denormalized, matches phenomenon's own precedent") no longer describes anything the
pipeline actually does.

**Options on the table:**
- Drop it (clean, matches current reality).
- Repurpose it for something real, once passage-scoped Layer 2 processing (if it ever returns) needs
  it again.

**Researcher decision:**
>

**Action:**
>

**Status:** Open

---

## D8 — `verse_lexical_note.evidence_text`

**What needs deciding:** the single largest concrete defect in the whole map — 0/173 rows have ANY
value, ever, across every note_type. Practice has informally folded evidence into `value_text`
instead.

**Options on the table:**
- Enforce as a required field (a write-time gate — the enriching LLM call must populate it going
  forward).
- Formally merge into `value_text` — stop pretending it's a separate fact, since practice already
  treats it as one.

**Researcher decision:**
>

**Action:**
>

**Status:** Open — high priority (Window 2 synthesis currently has no way to audit any finding's
grounding without this)

---

## D9 — `verb_argument` trigger condition + T7–T14 wiring

**What needs deciding:** the one live example (Gen, "gave") works, but nothing in code triggers a
`verb_argument` note, and nothing connects its resolved target back to the T7–T14 referent-identity
tags — the exact payoff this session's T-code tagging work was building toward.

**Sub-decisions, in build order:**
1. Fix the two field docs (`target_verse_lexical_id`/`related_verse_lexical_ids`) to name the
   agent/trigger and recipient/impact uses — small, no judgement needed, can happen regardless of 2/3.
2. Register `verb_argument`/`compound_unit` in `note_type`'s doc-string — same, small.
3. Decide the trigger condition — which T3 (operation-verb) rows should get a `verb_argument`
   attempted, and how that interacts with `role`'s complete cluster-set once D1 is built.
4. Wire the mechanism to check the T7–T14 tag on the resolved target row.

**Researcher decision:**
>

**Action:**
>

**Status:** Open — 1/2 are buildable now; 3/4 need your call first

---

## D10 — `H3477H` disposition

**What needs deciding:** carried from before the column map — live gloss is "Jashar" (Book of Jashar,
proper-noun reference, Josh.10.13/2Sam.1.18), not "upright" as first read. Currently T2+T3 live
(the one unresolved case from the 13-strong M+T3/T2+T3 scan).

**Options on the table:**
- T3-only (Objects — a book/document reference), matching the disposition already applied to the
  rest of that batch.
- Something else, if you see a better fit once the correct gloss is in view.

**Researcher decision:**
>

**Action:**
>

**Status:** Open

---

## D11 — `gloss_consistent_in_verse` grain mismatch: promote to `span`, not `verse_lexical`

**What needs deciding, raised 2026-09-09 (researcher's own header/detail design read):** the
redefined "combined sense of every code in the span" is a **span-level** fact — it's computed by
looking across *all* of a span's sibling code-rows, not owned by any one of them — the same
conceptual grain as `surface`/`position` (both already correctly live on `span`, denormalized down).
Unlike `surface`, though, the current design would write an *identical computed* value onto every
one of a multi-code span's N `verse_lexical` rows redundantly, rather than being sourced from one
true row — the "outlier" case the researcher named: a header-shaped fact with nowhere but the detail
table to live in today's schema.

**Contrast, confirmed same session:** `pairing` (D4) is NOT the same shape — each code's own binding
to its siblings genuinely differs per row, so it correctly stays a detail-level (`verse_lexical`)
fact.

**Options on the table:**
- Add `span.gloss_consistent` (or similar) as a real span-level column — one row, one value, for
  both single-code spans (68.5% of live spans) and multi-code spans (31.5%) alike, no repetition.
  `verse_lexical` keeps `gloss_consistent_in_verse` as a pure denormalized copy-down (or drops it
  entirely and Layer 2 joins to `span` directly).
- Leave it on `verse_lexical`, accept the repeated-identical-value pattern as intentional (matches no
  existing convention in this schema — `surface`/`position` are copy-downs of a value that's
  genuinely a property of the span itself, not a roll-up computed from children).

**Researcher decision:**
>

**Action:**
>

**Status:** Open

---

## D12 — `language`: verse-level fact sourced at code-level, no verse-level anchor in `iba.db`

**What needs deciding, raised 2026-09-09 (extending the same header/detail check to the rest of the
column list, per researcher's own prompt "are there any other columns that run the same risk"):**
`language` is conceptually a **verse-level** invariant (a verse is Hebrew, Greek, or — rarely,
Daniel/Ezra — Aramaic; it doesn't switch mid-verse) but is sourced from `strong.language`, a
**per-code** table, with no `iba.db`-side verse-level table/column to check it against or derive it
from. This is a real, not just theoretical, gap:

- **`testament` does NOT have this problem** — checked same pass — it's derived fresh from
  `cfg_book_order` (a proper book/verse-level reference table) each time, not denormalized from any
  per-code source. 0/verses show mixed testament, and there's no path for it to happen. No action
  needed on `testament`.
- **`genre` is the same class of problem, more severe** — checked same pass: `genre`/`testament`
  columns exist on `verse` only in **`bible_research.db`** (a different database entirely), not
  `iba.db.verse` (which has no `language`/`testament`/`genre` columns at all — just
  `osisId`/`preview`/`text`/`reference`). `bible_research.db.verse.genre` was explicitly rejected as
  a Layer 2 source already ("too coarse," #1451) — so `genre` currently has **no verse-level home
  anywhere in `iba.db`**, the root cause CA-11 named without fully explaining it. Not a new item —
  cross-referencing CA-11/CA-12 here since it's the same shape of gap as `language`, surfaced by the
  same check.
- **`language` — checked live, corpus-wide: 1 of 29,754 verses has mixed-language codes.**
  `John.1.18` (`verse_id` 22839): 14 live codes, 13 Greek, and one `H5207` ("Son," Hebrew) sitting
  among them, morph-tagged `N-NSM`, surface "Son." **This is very likely a genuine data bug, not a
  legitimate exception** — `H5207` is a Hebrew Strong's number; the Greek word for "son" (huios) is
  `G5207` — same digits, wrong language prefix. John 1:18's byzantine/majority-text variant reading
  does use "Son" (huios) at this position, so a real `G5207` belongs here; `H5207` looks like a
  transposed-prefix mis-tag, not a real Hebrew intrusion into a Greek verse.

**Options on the table:**
- Fix `H5207`→`G5207` at `John.1.18` directly (self-correctable once confirmed — small, concrete).
- Decide whether `language` should be validated as verse-invariant going forward (a check that would
  have caught this on write), the same way `testament`'s book-level derivation already guarantees
  consistency by construction.
- Separately, decide whether `iba.db` needs a genuine verse-level analytical anchor at all (extending
  `verse` itself, or a companion table) so verse-level facts (`language`-consistency, and eventually
  `genre` per CA-11) have a real home instead of being denormalized from a per-code table or left
  homeless — a bigger, standing question this specific bug just makes concrete.

**Researcher decision:**
> does the presence in memory of language and testament make any difference on how and what are being decided by layer 2.
> Is this a validator : for instance - strong references cannot be mixed, morph works differently, is there anything else that is dependent on it.

**Claude — checked the actual code, both questions, 2026-09-09:**

**Does `language` make a difference to Layer 2? Yes, confirmed, one live rule:**
`language`/`testament` ARE included in every code's own JSON payload sent to the LLM
(`handlers/lexical.py:_notes_payload_dict`, not filtered by `_lean_code`'s trimming). One live
`cfg_method_rule` (`lexical.enrich`) makes this a real, DIFFERENT-judgement-per-language input, not
just inert context: **`related-word-sorting-language-aware`** — *"Sorting a related_word pull into
same-concept/genuine-relative/coincidental is judged differently by language: Hebrew families skew
toward root-sharing; Greek families skew toward compound-morphology relationships."* A second rule,
`one-integrated-read-genre-first`, names "Genre/language/testament" as the read's own first
orienting move for the block — real, though it doesn't itself specify what differs.

**Is it a validator — "morph works differently," "strong references cannot be mixed"?**
"Morph works differently" is real, but **doesn't actually depend on the stored `language` column**
— `classify_role` and stem/voice selection (`_stem_for`) both branch on **the strong code's own
prefix letter** (`strong_code.startswith("H"/"G")`), re-derived fresh every time, not on
`verse_lexical.language`. So those two mechanisms would work correctly even if `language` were
wrong.

**One place genuinely IS gated by the stored value, not the code's own prefix:**
`_narrative_morph_for`: `if language != "Hebrew" or not morph_slice...: return None`. This reads the
*stored* `language`, not the code's prefix — so a Hebrew code with a wrongly-stored `language`
(NULL or "Greek") would silently get skipped, no error, nothing surfaced.

**"Strong references cannot be mixed" — checked, this is NOT currently validated anywhere.** No
code checks span/verse-level language consistency at all — which is exactly how the John.1.18/
`H5207` case (D12's live finding above) went undetected: nothing was watching for it. So today,
`language` is real, live-consumed data (Layer 2's related-word judgement, Layer 1's
`narrative_morph` gate) with **zero validation behind it** — not a validator itself, but something
that arguably should be validated, precisely because at least one real mechanism silently trusts it.

**Action:**
> 

**Status:** Open

---

## D13 — new `iba.db` verse-level base-data table (raised 2026-09-09, follows from D12)

**What's being proposed:** a new companion table to `verse` collating verse-level facts once, at the
right grain, instead of denormalizing-from-code (`language`) or leaving them homeless (`genre`,
CA-11). Genuinely greenfield — checked `cfg_table`, nothing already fills this role.

**Confirms this is a real, previously-hit problem, not just a hunch — `BUILD.md` #205
(2026-08-29):** building `finding_verse_index`, **`books.abbreviation` (`bible_research.db`) and
`iba.verse.reference`'s own book-prefix were found to genuinely disagree on some books** (`1Co` vs
`1Cor`, confirmed live) — resolved at the time by crosswalking on **canonical position**
(`books.book_order - 1 == cfg_book_order.ordinal`) rather than string-matching either database's own
abbreviation scheme, specifically to sidestep the mismatch rather than fight it. This is exactly the
class of bug a standardized, single-sourced reference on a verse-level table would prevent at the
root, not work around per-consumer.

**What `bible_research.db.verse` already carries, as a candidate list** (it already solved this
problem once, for its own database — worth checking against, not copying blind, since some of it may
not translate or may already exist differently in `iba.db`):

| Column | Candidate for `iba.db`? |
|---|---|
| `book_id` (numeric FK) | Maybe — `iba.db` currently keys books by `cfg_book_order.book` (text code), not a numeric id; a numeric id would only help if something needs it, not decided here |
| `chapter`, `verse_num` | Likely yes — parsed once from `osisId`, removes any future need to re-parse it ad hoc |
| `testament` | Yes — already correctly derivable (`cfg_book_order`), just currently recomputed per `verse_lexical` row rather than fixed once per verse |
| `genre` | **RETIRED, 2026-09-09, researcher verdict (see below) — no role in this study's lexical analysis. Column left in place, `inactive=1` in `cfg_column`, not dropped.** |
| `passage_id`, `is_passage_anchor` | **Settled, researcher instruction:** map via the existing `verse_passage` junction (`verse_id` unique — "one passage per verse", 25,690 live rows) to `iba.passage` — not built fresh. Usage not yet known; explicitly deferred until inner-being analysis work resumes, not a blocker to building the column. |
| `process_marker` | **Yes, likely the right home for CA-12** (`passage.lexical_complete_at`, already found orphaned by #1451 with nowhere to live) — a verse-level processing/completion stamp is the natural grain for "has this verse's Layer 1/2 work been done," not a passage-level one |
| `reference` (human-readable) | Yes, but **derived FROM `osisId` + `cfg_book_order` at write time, never independently typed or pulled a second time from STEP** — this is the actual fix for the #205-class bug: one canonical source, not two systems each producing their own string |

**New candidate, not from the old system, raised by D12's own finding:** a **`language`** column,
fixed once per verse (from the verse's own text/book, not denormalized from a per-code `strong`
table) — this is the direct fix for D12's open items: gives `narrative_morph` a real, validated gate
instead of a silently-trusted per-code copy, and would have caught the John.1.18/`H5207` case at
write time rather than leaving it undetected indefinitely.

**Open, not decided:**
1. Exact column list — the table above is a checked, non-blind starting point, not a final proposal.
2. Table name/shape — a genuine `iba.db.verse_meta` companion table (1:1 with `verse`), vs. adding
   columns directly to `verse` itself.
3. ~~Whether `genre` starts fresh or reconsiders the rejected `bible_research.db` source as a coarse
   seed.~~ **CLOSED 2026-09-09 — genre retired entirely, see below.**
4. How `reference` gets generated (which book-abbreviation convention becomes canonical for
   `iba.db` — its own `cfg_book_order.book` codes, matching `osisId`, is the obvious candidate,
   already internally consistent — checked live, 66/66 `osisId` book-prefixes match
   `cfg_book_order.book` exactly, no drift found within `iba.db` itself; the #205 mismatch was
   specifically cross-database, not internal).

**Researcher decision:**
> Create the table; one-off populate from the different sources; validate it; integrate into
> configs (cfg_table/cfg_column); auto-update whenever `iba.verse` records change (not a one-time
> snapshot); `passage_id` maps via `verse_passage` to `iba.passage` (see table above). Usage not
> yet known — will matter again for inner-being analysis work, not a blocker to building it now.

**Action:**
> Built and verified live on **#1608** (2026-09-09): `verse_meta` table (13 columns), 29,759/29,759
> verses populated, 4 auto-sync triggers (each live-tested before commit), `cfg_table`/`cfg_column`/
> `cfg_utility` registered, validation clean (one real finding: John.1.18's `H5207` outlier,
> surfaced not auto-fixed, tracked on D12). Table name settled as `verse_meta` (not `verse_meta`
> vs. extending `verse` — went with a companion table). `genre`/`lexical_complete_at` given a real
> home, deliberately left NULL — no fresh-vs-reimport call needed yet since nothing populates them
> this pass. Full build record on #1608's own resolution.

**Status:** Built, ready for your review — #1608

**`genre` RETIRED, 2026-09-09, researcher verdict, verbatim:** *"Our focus on genre is noise. It
really only is relevant in passage reading, and in this study, the reason for reading wider than
the current verse context is to resolve the 'reach' of the operation of a characteristic. We are
reading to find something specific, and not to understand an entire passage. so in terms of the
lexical analysis, it is pure verse focussed — especially seeing that the char movement is not under
consideration, even in layer 2 analysis. When we proceed to window 2, and start to focus on char
reading, then the reading process will first read the char and its movements. when it cannot close a
movement, it will progressively start the access the lexicals for verses around it in a discovery
process. So my feeling is we can record this conclusion and remove genre from the considerations, it
has no real meaning or role."*

**Applied live:**
- `verse_meta.genre` — **dropped outright** (`ALTER TABLE ... DROP COLUMN`), per follow-up
  instruction: *"you can remove the columns from the verse-meta table."* Its `cfg_column` row was
  deleted, not left inactive (an inactive row for a column that no longer physically exists is its
  own coherence violation). Script: `iba/app/migration/drop_verse_meta_genre_column_v1_20260909.py`.
  `verse_meta` now has 12 columns.
- `passage.genre` — left **`inactive=1`**, not dropped (the researcher named `verse-meta`
  specifically; `passage` is older, more consequential infrastructure).
- `cfg_method_rule` id 53 (`genre-manual-this-round`, `lexical.enrich`) — fully superseded,
  `active=0`.
- `cfg_method_rule` id 49 (`one-integrated-read-genre-first`, `lexical.enrich`) — **edited, not
  retired** (language/testament are still real "first move" facts): genre removed from its text,
  old wording preserved inline in the row itself.
- `bible_research.db.verse.genre`'s own `cfg_column` row untouched — it's a real, populated column
  in a different database, just never consumed here; nothing to retire on that side.

Not touched, out of scope for this verdict: `passage.suggest_boundary`'s
`proxy-signals-not-genre-determination` rule (names a legacy genre tag as one of several boundary-
suggestion signals, but its own text is explicit that this is passage-*segmentation*, not genre
determination — a different mechanism, not re-examined here).

---

## E1 — Small config-currency fixes (batch, no judgement needed)

**What this is:** `cfg_column.use` text drift already confirmed against live code — CA-3
(`resolved_sense`), CA-5 (`is_negator`), CA-6 (`party_kind`), CA-7 (`updated_at` never registered at
all), plus two found building the map: `note_type`'s doc-string (missing `verb_argument`/
`compound_unit`) and the `target_verse_lexical_id`/`related_verse_lexical_ids` doc text (undocumented
`verb_argument` use). None of these change behaviour — they correct governance text to match what the
code already does.

**Proposed action:** run as one `Config-Maintenance.ps1 -Step Propose` batch, same batch already
scoped in #1605 §6 — approval-gated regardless, but no design judgement required to approve.

**Researcher decision:**
>

**Action:**
>

**Status:** Open — ready to run on your go-ahead

---

## E2 — Rebuild currency (operational, not a design decision)

**What this is:** `is_negator`/`party_kind` (and `role`, once D1 lands) are build-time snapshots of
`cluster_strong`, not live-derived. 15 strongs / 316 live `verse_lexical` rows are already stale
relative to today's own T4/T5/T7/T9 cluster additions from this session's T2-resweep and #1606's
completeness work.

**What needs deciding:** when to run a `verse_lexical` rebuild to pick up today's cluster changes —
now, or bundled with whichever of D1–D9 lands first (since several of them change what a rebuild
produces anyway, a rebuild now would need repeating).

**Researcher decision:**
>

**Action:**
>

**Status:** Open — timing question, not a design one
