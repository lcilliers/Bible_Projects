# Catalogue `scope` reclassification + wording review — #1383's Stage-1 lexical answer surface

**Escalation:** #1444 v3 ("Update the scope to align with the work in 1383 and other predecessor
escalations"). **Instruction, verbatim, this chat turn:** "bring scope column in catalogue up te
date with word/term (lexical) for every question answered by the new lexical defined in 1383, also
check the wording of the question to ensure it is clear and say exactly what is meant."

**Source material used** — the already-reviewed, confirmed determinations from #1383, not
re-derived: `1383-verse-lexical-stage1-catalogue-field-mapping-v1-20260903.md` (which questions
Stage 1's lexical build answers, and how), `1383-catalogue-finishing-and-config-not-code-audit-v1-20260903.md`
(confirmed-mechanical vs. genuinely-hybrid questions, and 4 already-proposed wording splits),
`1383-catalogue-review-note-writeback-proposal-v1-20260904.md` (the condensed 27-code list).
Cross-checked against the LIVE `wa_obs_question_catalogue` (126 active rows, current `scope`/
`question_text` as of 2026-09-04, after the 55-row `deleted=1` cleanup earlier this session).

**Nothing in this document has been written to the table yet** — same "recommendation, not a
silent decision" discipline #1383 used throughout. One real tension surfaced below needs your call
before any of it is applied.

---

## 1. The tension this cross-check surfaced — needs your decision before I write anything

`scope`'s existing definition (`cfg_column.use`, escalation #1007) is a **subject-matter** bucket:
what the question is fundamentally *about* (vocabulary vs. relational vs. verse-literary vs.
faculty-engagement, etc.) — `1007-tier-catalogue-scope-focus-v3` moved `T6.4` into Word/term
(lexical) with the reasoning "that's a lexical question about terms, not a relational question."

#1383's field-mapping document instead classifies by **answering mechanism**: which stage/field
answers each question, regardless of what it's about. Several questions #1383 shows are now
mechanically answered by the `verse_lexical` build are **not, by subject matter, questions about a
word or term** — they're about a characteristic's relation to God, or the verse's literary form:

| Code | What it's actually about (subject matter) | What answers it now (#1383) |
|---|---|---|
| `T0.1.1` | Whether the characteristic is predicated of God — a **divine-relation** fact | `party_kind` join (`verse_lexical`) |
| `T4.1.1` / `T4.2.1` | Direction of a God↔person relation — a **relational** fact | Same `party_kind` join |
| `T7.2.2` | The verse's **literary form** (genre) | `passage.genre` field |

Your instruction says to set scope to Word/term (lexical) "for every question answered by the new
lexical" — read literally, that moves these three subject areas into the lexical bucket too, which
would make `scope` mean "what Stage 1's `verse_lexical` build answers" rather than "what the
question is about." That's a real, usable redefinition (the escalation is literally named
"verse-lexical Window 1," so "the new lexical" plausibly means the whole Stage-1 infrastructure,
not narrowly vocabulary) — but it is a redefinition, and I'm not applying it silently.

**Two ways to resolve it — tell me which:**

- **(A) Mechanism-based** (your instruction, read literally): move every §1–4 field-mapping-answered
  code into `Word/term (lexical)`, regardless of subject matter. `scope` becomes "which stage/
  mechanism answers this," and its name stops being literally accurate for non-vocabulary codes
  moved in under it.
- **(B) Subject-matter-preserved** (narrower): only move codes into `Word/term (lexical)` that are
  BOTH Stage-1-answered AND actually about a word/term/vocabulary fact. `T0.1.1`/`T4.1.1`/`T4.2.1`/
  `T7.2.2` stay in their current subject-matter buckets (`Verse-context` / `The verse`) — their
  Stage-1-answered status gets recorded some other way (e.g. the not-yet-built `answered_by` column
  from the finishing doc §1), not by relocating them out of the bucket that correctly describes
  what they're about.

I'd lean toward (B) — it keeps `scope` doing one job (subject-matter) and lets a second, separate
mechanism (`answered_by`, already proposed and specified, just not built) carry "how it's answered"
— but this is your categorisation system and genuinely your call. **Section 2 below is written so
either reading can be applied directly once you pick.**

---

## 2. Every code cross-checked, with the scope move each reading implies

Current `scope` and `question_text` pulled live; "Stage-1 status" is #1383's own confirmed
determination (field-mapping doc §1–5); "Under (A)" / "Under (B)" state what `scope` becomes.

| Code | obs_id | Current scope | Stage-1 status (per #1383) | Under (A) | Under (B) |
|---|---|---|---|---|---|
| `T0.1.1` | 224 | Verse-context | Fully mechanical, confirmed non-hybrid | → Word/term (lexical) | unchanged (Verse-context) |
| `T4.1.1` | 324 | Verse-context | Fully mechanical, confirmed non-hybrid | → Word/term (lexical) | unchanged |
| `T4.2.1` | 328 | Verse-context | Fully mechanical, confirmed non-hybrid | → Word/term (lexical) | unchanged |
| `T7.2.2` | 404 | The verse | Mechanical **for its genre half only** — see §3, wording issue | → Word/term (lexical) | unchanged |
| `T1.4.1` | 245 | Verse-context | Mechanical **for its grammatical/stem-form half only** — see §3 | → Word/term (lexical) | unchanged |
| `T0.1.2` | 225 | Other non-human beings | Mechanical **raw-fact half only**; already has a proposed a/b split (finishing doc §2) not yet applied | → Word/term (lexical) once split | unchanged |
| `T4.3.1` | 332 | Verse-context | Mechanism designed, **human-name lexicon not built** — not answerable yet | not moved yet (pre-build item) | not moved yet |
| `T4.4.1` | 336 | Verse-context | Same — lexicon not built | not moved yet | not moved yet |
| `T4.6.1` | 344 | Verse-context | Same — angelic lexicon not built | not moved yet | not moved yet |
| `T4.6.2` | 345 | Other non-human beings | Mechanical half needs angelic lexicon (not built); proposed a/b split not yet applied | not moved yet | not moved yet |
| `T4.6.3` | 346 | Other non-human beings | Same status/split as `T4.6.2` | not moved yet | not moved yet |
| `T7.1.1` | 393 | **Word/term (lexical)** | Stage-1 rollup, confirmed working | already correct | already correct |
| `T7.1.2` | 394 | **Word/term (lexical)** | Stage-1 rollup, confirmed working | already correct | already correct |
| `T7.1.8` | 400 | **Word/term (lexical)** | Stage-1 rollup, confirmed working | already correct | already correct |
| `T7.1.9` | 401 | **Word/term (lexical)** | Stage-1 rollup, confirmed working | already correct | already correct |
| `T7.1.10` | 402 | **Word/term (lexical)** | Union of the above rollups | already correct | already correct |
| `T1.1.2` | 237 | **Word/term (lexical)** | Stage-1 rollup, confirmed working | already correct | already correct |
| `T6.4.1` | 379 | **Word/term (lexical)** | Stage-1 supplies the raw pull; characteristic-attribution needs Stage 2 (two-stage, partial) | already correct, note partial | already correct, note partial |
| `T6.4.2` | 380 | **Word/term (lexical)** | Same two-stage partial status | already correct, note partial | already correct, note partial |
| `T7.1.3` | 395 | **Word/term (lexical)** | NOT a Stage-1 rollup — property of `strong_meaning_tree` directly; Stage 1 draws on it, doesn't derive it | already correct (subject matter), not Stage-1-mechanical | already correct |
| `T7.1.4`–`T7.1.7` | 396–399 | **Word/term (lexical)** | Real, unowned gaps — need judgement beyond a rollup; flagged for a follow-on wording split (finishing doc §3), not done | already correct, not Stage-1-mechanical | already correct |
| `T6.1.1` | 369 | Characteristic relational | Stage 1 supplies the raw pull only; full per-characteristic attribution needs Stage 2 — subject matter is relational, not lexical | unchanged (not a word/term subject) | unchanged |
| `T6.1.2` | 370 | Characteristic relational | Genuinely Stage 2 (T0.2.1-class) — no Stage-1 answer at all | unchanged | unchanged |
| `T7.2.1` | 403 | The verse | Sentence-role half is Stage-1-ish (`morph_code`); argument half is a real, unowned gap | unchanged (subject = verse-literary) | unchanged |
| `T7.2.3` | 405 | The verse | Real, unowned gap — no Stage-1 field answers this | unchanged | unchanged |

**Net effect:**
- **(A)**: 6 scope changes now (`T0.1.1`, `T4.1.1`, `T4.2.1`, plus `T7.2.2`/`T1.4.1`/`T0.1.2` once
  their wording splits below are applied — the split-off mechanical half moves, the interpretive
  half stays put), 5 more (`T4.3.1`/`T4.4.1`/`T4.6.1`/`T4.6.2a`/`T4.6.3a`) deferred until their
  lexicons are built.
- **(B)**: 0 scope changes — every code already in `Word/term (lexical)` stays there and is
  confirmed correct; the Stage-1-answered status of the rest is recorded via wording/`answered_by`
  instead of a scope move.

---

## 3. Wording review — "does the question say exactly what is meant"

Checked every one of the 27 codes' live `question_text` against what #1383 actually determined
answers it. Three categories:

### 3a. Already identified and specified by #1383 — not re-derived, just carried forward

- **4 splits proposed, not yet applied** (finishing doc §2): `T0.1.2` → `T0.1.2a`/`T0.1.2b`;
  `T4.6.2` → `T4.6.2a`/`T4.6.2b`; `T4.6.3` → `T4.6.3a`/`T4.6.3b`. (`T6.1.1`/`T6.1.2` were checked
  and found NOT to need a split — already single-purpose, the earlier session error was pairing
  them, not their wording.)
- **1 in-place wording fix proposed, not yet applied** (finishing doc §3): `T7.2.1` — add an
  explicit (a)/(b) split inside the existing question text (sentence-role vs. argument-role),
  no new code.
- **`T7.1.4`–`T7.1.7`**: flagged as needing the same treatment as a **follow-on batch**, explicitly
  not attempted in that pass.

### 3b. New — found by this cross-check, not previously flagged

- **`T7.2.2`** — "What literary form carries the primary verse evidence..., **and what does that
  form require for responsible interpretation?**" The first clause is Stage-1-mechanical
  (`passage.genre`); the second is an interpretive/hermeneutical judgement Stage 1 does not answer
  — same bundling pattern as the four splits #1383 already caught. **Proposed split** (matching
  their style):
  - `T7.2.2a` (mechanical): "What literary form carries the primary verse evidence (narrative,
    psalm, wisdom, prophecy, epistle, apocalyptic)?" — `passage.genre`, direct read.
  - `T7.2.2b` (interpretive): "What does that literary form require for responsible
    interpretation?" — stays wherever `T7.2.2` currently sits (Stage 2 or later).
- **`T1.4.1`** — "In what distinct mode(s) does the characteristic operate within the inner person
  in this verse — **including its grammatical/stem form and the manner of functioning**?" Same
  bundling: "grammatical/stem form" is a direct `morph_code` read; "manner of functioning" needs
  the fuller single-verse behavioural read that the rest of `Verse-context` bucket questions do.
  **Proposed split:**
  - `T1.4.1a` (mechanical): "What is the grammatical/stem form of the characteristic's primary term
    in this verse?" — `verse_lexical.morph_code`, direct read.
  - `T1.4.1b` (unchanged scope): "In what distinct mode(s) does the characteristic operate within
    the inner person in this verse — the manner of its functioning?" — stays `Verse-context`.

### 3c. Checked, no issue found

`T0.1.1`, `T4.1.1`, `T4.2.1` — confirmed by #1383 as *fully* mechanical once corrected, "not
actually hybrid" (finishing doc §2); their current single-clause wording already says exactly what
it means, no split needed. `T4.3.1`/`T4.4.1`/`T4.6.1` — single mechanical questions, wording is
already precise; they're blocked on an unbuilt lexicon, not on unclear wording. `T7.1.1`/`T7.1.2`/
`T7.1.8`/`T7.1.9`/`T7.1.10`/`T1.1.2`/`T6.4.1`/`T6.4.2`/`T7.1.3`/`T6.1.2`/`T7.2.3` — each is already
a single, clearly-scoped question; no conflation found.

---

## 4. What can actually execute now vs. what needs a build item

Same constraint #1383 already established: `obs_catalogue.update` is UPDATE-by-`obs_id` only, **no
INSERT** — so a wording *edit in place* (`T7.2.1`) is executable right now via the registered tool;
creating any **new** `question_code` row (`T0.1.2a/b`, `T4.6.2a/b`, `T4.6.3a/b`, and my two new
proposals `T7.2.2a/b`, `T1.4.1a/b`) needs a one-off migration script, which needs Developer Mode or
your explicit go-ahead (this session is confirmed not in Developer Mode).

**So, two independent decisions, and what each unlocks:**

1. **Scope reading — (A) or (B)?** Settles section 2's table.
2. **Do you want the 5 code-splits built now** (the 3 #1383 already specified + the 2 new ones
   found here), or **just the wording tightened in place** for the pieces that don't strictly need
   a new code (`T7.2.1`'s in-place (a)/(b) fix is the only one of the 7 that doesn't need a new
   `question_code`)?

Once you answer both, I'll run the actual `obs_catalogue.update` calls (scope changes + `T7.2.1`'s
wording fix) directly — same governed path as the 55-row `deleted=1` cleanup earlier this session —
and, if you want the splits built, scope that as its own small migration item.

**Not in scope of this pass, named so it isn't silently dropped:** the `answered_by` column itself;
the glossary entries (`Layer 1`/`Layer 2`, `Stage 1`/`Stage 2`, `party_kind`, `grain` vs.
`resolved_sense`, `structural_pattern`, `cfg_lexical_code_class`) #1383's finishing doc flagged as
not yet written.

---

## 5. Researcher ruling applied (this chat turn, 2026-09-04) — resolves §1's tension

**Verbatim:** "if the question answers a inner being related point that would need the window 2
insight then the scope is not verse/term. verse/term show which questions is expected to be
answered after window 1 completed (mechanical or not — we already discounted this split). This
means the answer is somewhere between a and b."

**The rule, applied exactly:** `scope = Word/term (lexical)` means "expected to be fully answered
once Window 1 completes" — regardless of whether that answer is a bare field read or needs some
Window-1-internal judgement (a pending lexicon build counts as "expected after Window 1," not as
"needs Window 2"). If **any part** of a question's answer needs Window 2's HIB/behaviour insight,
that part does not carry the label — which is exactly why the 5 bundled questions need splitting
first: the row can't carry two different answerability statuses under one `scope` value.

**A load-bearing clarification this ruling produces, beyond §1's original tension:** the
`Verse-context` bucket (1007-v3's own definition: "a single-verse empirical reading... as opposed
to a general or cross-verse claim") is NOT itself Window 1's territory — its own worked examples
(`T3.1.1` "does the characteristic engage the perceptive faculty... in this verse") are exactly
Window 2's single-verse HIB read. `T0.1.1`/`T4.1.1`/`T4.2.1`/`T4.3.1`/`T4.4.1`/`T4.6.1` only *sat*
in `Verse-context` because their wording pattern-matched the bucket's "in this verse" rule
(1007-v3 §2) — #1383 is what discovered their actual answering mechanism is Window-1-only, contrary
to that original placement. That's the correction being applied here, not a new one.

### Applied now — live, via `obs_catalogue.update` (no Developer Mode needed)

| Code | obs_id | Change | Run ID |
|---|---|---|---|
| `T0.1.1` | 224 | scope → `Word/term (lexical)` | `RUN-20260904_165141_775-CATALOGUE-UPDATE` |
| `T4.1.1` | 324 | scope → `Word/term (lexical)` | `RUN-20260904_165146_221-CATALOGUE-UPDATE` |
| `T4.2.1` | 328 | scope → `Word/term (lexical)` | `RUN-20260904_165150_234-CATALOGUE-UPDATE` |
| `T4.3.1` | 332 | scope → `Word/term (lexical)` (mechanism designed, lexicon build pending — "expected after Window 1," not blocked on Window 2) | `RUN-20260904_165154_115-CATALOGUE-UPDATE` |
| `T4.4.1` | 336 | scope → `Word/term (lexical)`, same reasoning as `T4.3.1` | `RUN-20260904_165202_077-CATALOGUE-UPDATE` |
| `T4.6.1` | 344 | scope → `Word/term (lexical)`, same reasoning | `RUN-20260904_165205_967-CATALOGUE-UPDATE` |
| `T7.2.1` | 403 | `question_text` → the already-proposed (a)/(b) in-place wording split (finishing doc §3) — no code split, no scope change (`The verse`, unchanged: the argument-role half is a real, unowned gap, not confirmed Window-1-expected) | `RUN-20260904_165219_145-CATALOGUE-UPDATE` |

All 7 verified live post-write.

### Resolved by the ruling — no build item needed after all

**`T7.1.4`–`T7.1.7`** (finishing doc §3 had flagged these as a possible follow-on split batch,
explicitly deferred, not decided): applying the ruling directly — each question's "judgement half"
(does the vocabulary include a term of type X) is judgement about the **term family itself**
(semantic/vocabulary classification), not about the characteristic's behaviour in any verse. **No
Window 2 insight required** → these are correctly `Word/term (lexical)` as they already stand, and
**do not need a split**. This closes the open question the finishing doc left hanging.

**`T6.4.1`/`T6.4.2`**: left unchanged (already `Word/term (lexical)`, partial/two-stage caveat
noted, not re-litigated) — the raw vocabulary-sharing pull is genuinely Window 1's own output even
though full characteristic-attribution needs Stage 2's segmentation; 1007-v3's original placement
reasoning (a lexical question about terms, not a relational one) still holds for the row as a whole.

**`T6.1.1`/`T6.1.2`**: left unchanged (`Characteristic relational`) — the question is about which
*characteristics* co-occur, and "characteristic" is a Window 2 concept; the raw Strong's-code pull
being Window-1-available doesn't make the row's own actual question Window-1-answerable.

### Residual — doesn't fit the binary cleanly, flagged rather than forced

**`T7.2.2b`** (once split): "What does that literary form require for responsible interpretation?"
is not itself inner-being/HIB-related, so the ruling's stated test doesn't directly resolve it —
it's a literary-hermeneutics judgement, arguably neither Window 1 nor Window 2. Left at `The verse`
(unchanged) by default pending your call; named here rather than silently assigned either way.

## 6. Ready-to-build spec for Developer Mode — every split, fully specified

Per your instruction: preparation complete now; the actual code-split work (new `question_code`
rows — `cataloguewrite.py` has no INSERT path) waits for Developer Mode. Nothing below is executed.

| Old code (obs_id) | New code | Wording | Scope |
|---|---|---|---|
| `T0.1.2` (225) | `T0.1.2a` | "Across the characteristic's verses, is the characteristic ever predicated of God himself (not just present in a verse where God is also mentioned)?" | `Word/term (lexical)` — Window-1 rollup (`COUNT(...WHERE party_kind='divine')>0`) |
| | `T0.1.2b` | "What does the pattern of presence/absence found in T0.1.2a indicate for the characteristic's place in the human person and in the divine image?" | `Other non-human beings` (unchanged) — needs Window 2, T0.2.1-class |
| `T4.6.2` (345) | `T4.6.2a` | "Does an adversarial-being code ever appear as an acting party in a verse carrying this characteristic?" | `Word/term (lexical)` — Window-1, pending the angelic/adversarial-name lexicon build |
| | `T4.6.2b` | "What does that pattern show about the characteristic being a site of adversarial activity?" | `Other non-human beings` (unchanged) — needs Window 2 |
| `T4.6.3` (346) | `T4.6.3a` | Same split shape as `T4.6.2` (finishing doc §2 names the pattern, doesn't spell out T4.6.3's own wording — needs the actual text drafted at build time, same mechanism) | `Word/term (lexical)` |
| | `T4.6.3b` | (same, interpretive half) | `Other non-human beings` (unchanged) |
| `T7.2.2` (404) | `T7.2.2a` | "What literary form carries the primary verse evidence (narrative, psalm, wisdom, prophecy, epistle, apocalyptic)?" | `Word/term (lexical)` — direct `passage.genre` read |
| | `T7.2.2b` | "What does that literary form require for responsible interpretation?" | `The verse` (unchanged) — residual, see §5 |
| `T1.4.1` (245) | `T1.4.1a` | "What is the grammatical/stem form of the characteristic's primary term in this verse?" | `Word/term (lexical)` — direct `verse_lexical.morph_code` read |
| | `T1.4.1b` | "In what distinct mode(s) does the characteristic operate within the inner person in this verse — the manner of its functioning?" | `Verse-context` (unchanged) — needs Window 2 |

**Open build-mechanics question, named for Developer Mode, not decided here:** how the split itself
lands in the table — soft-delete the old unified code and insert two new rows (breaking any existing
`obs_id` references to it), or keep the old code active as a parent/rollup and insert two children
under it. Not a wording question, a schema/migration-design one; flagging it now so it isn't
improvised mid-build.
