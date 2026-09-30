# Gap-closure design — every unanswerable/incomplete question, a concrete recommendation each

> Escalation #1806 (the original ask this whole thread traces back to), researcher instruction this chat, verbatim: "you need now to focus on all the questions that is either not answerable, or have incomplete data for answering, and have every question supported in a design suggestion on how we going to close the gap." Covers all 31 currently-unanswerable questions (27 `STRUCTURALLY-UNREACHABLE` + 4 `EXCLUDED-SCIENCE-EXTRACT`, per `pipeline-wiring-audit-20260921-v4`) plus the one known incomplete-DATA blocker (a whole subgroup unable to complete Stage 3, not a placement problem). **Design only — nothing in this document has been applied.**

## Summary — 5 categories, by what it actually takes to close each

| category | count | what it takes | risk |
|---|---|---|---|
| A — re-scope 6, then one dynamic Stage-1 rule | 16 | 1 code change + 6 DB re-scopes | LOW — same shape as D7.7.1's existing pinned treatment |
| B — re-scope only, no code change | 4 | 4 DB re-scopes | LOW — mechanical, matches sibling precedent for 3 of 4 |
| C — new Stage-1 dynamic/pinned question | 2 | 1 code change (prefix + pin list) | LOW — same mechanism M0.6.5/M0.6.6 already use |
| D — needs the not-yet-built Synergy/cluster-level stage | 5 | real new build — a stage that doesn't exist yet | HIGH — scope/cost of a new stage, not a tweak |
| E — already designed on #1805, pending approval | 4 | apply the existing #1805 v5 proposal | LOW — design done, just needs a decision |

## Category A — 16 questions: re-scope 6 mis-tagged ones, then one dynamic Stage-1 rule

All 16 are genuinely **per-verse** questions (their own wording says "this verse"/"In this verse") — the natural home is Stage 1 (`verse-reading`), which already reads every verse once per cluster pass. 10 already carry `scope='Verse-context'` but nothing selects that scope; 6 are mis-tagged `Word/term (lexical)` despite being worded identically to the Verse-context ones (a real catalogue data error, not a wording problem — their text already reads correctly).

**Fix:** (1) re-scope the 6 mis-tagged rows to `Verse-context`. (2) One code change in `versereadinggenerate.py`: extend the Stage 1 selection query to also select `scope='Verse-context'` dynamically (matching how Stage 4 already selects its own 4 scopes dynamically) — a catalogue change alone then makes a 17th Verse-context question reachable automatically, no further code edits. Answered the same way `D7.7.1` already is: only for the calling cluster's own home strong(s), once per verse, no front-loading, no progressive prior-context chain needed (these aren't word-level facts, and none of them depend on a prior pass's own finding the way `M0.6.5`/`M0.6.6` do).

**Named tradeoff, not hidden:** this adds up to 16 more questions to every Stage 1 call — Stage 1 is already 71% of cost/80% of time (Finding 13). Real cost increase, offset by: these are all genuinely new coverage (currently 0 answered), and Finding 13's own fix (the home-strong skip-check) doesn't apply here since these aren't word-level questions needing only one answer ever — each verse's own answer is expected to differ.

| code | current scope | action | text (truncated) |
|---|---|---|---|
| D10.1.1 | Verse-context | no change | Does this verse state any purpose, role, or effect... |
| D10.2.1 | Verse-context | no change | What first/most immediate inner-being response... |
| D10.3.1 | Verse-context | no change | What does the characteristic produce over time... |
| D10.4.1 | Verse-context | no change | Does the characteristic produce transformation... |
| D10.5.1 | Verse-context | no change | Does this verse describe a sequence of inner states... |
| D10.6.1 | Verse-context | no change | By what mechanism does the characteristic produce change... |
| D3.1.1 | Verse-context | no change | In what distinct mode(s) does the characteristic operate... |
| D6.1.1 | Verse-context | no change | At which constitutional level(s)... |
| D7.5.1 | Verse-context | no change | Where does this verse say the characteristic originates... |
| F0.1.1 | Verse-context | no change | Does the characteristic engage any inner-being faculty... |
| D5.2.1 | Word/term (lexical) | RE-SCOPE -> Verse-context | In this verse, does the characteristic operate in the person's movement toward God... |
| D7.1.1 | Word/term (lexical) | RE-SCOPE -> Verse-context | In this verse, does the characteristic operate from God toward the human person... |
| D7.2.1 | Word/term (lexical) | RE-SCOPE -> Verse-context | In this verse, is the characteristic extended by one person toward another... |
| D7.3.1 | Word/term (lexical) | RE-SCOPE -> Verse-context | In this verse, is the characteristic taken up by a person from another... |
| D7.4.1 | Word/term (lexical) | RE-SCOPE -> Verse-context | In this verse, does the characteristic operate in relation to other spiritual beings... |
| D7.6.1 | Word/term (lexical) | RE-SCOPE -> Verse-context | In this verse, is the characteristic predicated of God or otherwise related to God... |

## Category B — 4 questions: re-scope only, no code change needed

Already worded as characteristic-level aggregates ("Across the characteristic's verses ..."/"At the characteristic level...") despite carrying a scope Stage 4 doesn't select. 3 of 4 have a direct sibling in the SAME question family already live at the target scope — re-scoping to match is not a guess, it's aligning with an established precedent in the same component. Once re-scoped, Stage 4's own dynamic scope-driven query picks them up automatically — zero code change.

| code | current scope | target scope | why |
|---|---|---|---|
| D5.1.1 | Word/term (lexical) | Other non-human beings | matches its own follow-up D5.1.2's scope |
| D7.4.2a | Word/term (lexical) | Other non-human beings | matches its own follow-up D7.4.2b's scope |
| D7.4.3a | Word/term (lexical) | Other non-human beings | matches its own follow-up D7.4.3b's scope |
| M0.6.2 | The verse | Characteristic (HIB behaviour) | best-fit judgement call, no direct sibling precedent within M0.6 -- flagged, not asserted as certain |

## Category C — 2 questions: new Stage-1 question, same mechanism as M0.6.5/M0.6.6

| code | mechanism | why it fits |
|---|---|---|
| M0.4.1 | dynamic Stage 1 (extend M0.1%/M0.5% prefix match to include M0.4%) | per-occurrence, morph-based (span.morph_code, already-parsed, already in Stage 1's roles_in_verse payload) -- no new data needed |
| M0.6.1 | pinned Stage 1 (same treatment as M0.6.5/M0.6.6/D7.7.1) | genuinely per-verse literary-function question, same component (M0.6) as the already-pinned M0.6.5/M0.6.6 |

## Category D — 5 questions: genuinely need a stage that doesn't exist yet

Both sub-groups need visibility NO current stage's payload provides — re-scoping alone would make Stage 4 *attempt* these with the wrong data, producing shallow or wrong answers (the exact failure this whole session has been finding elsewhere, not something to repeat here on purpose).

- **`X0.4.1`–`X0.4.3`** (cross-characteristic vocabulary sharing) need OTHER clusters' own gloss/root data for comparison. Checked live: `charanswergenerate.py`'s payload only ever includes the CALLING cluster's own subgroup data — never another cluster's. `X0.1.1`/`X0.2.1`/`X0.5.1` (same X0 family, already reachable) get away with their narrower co-occurrence framing because Stage 1's own `M0.6.5`/`M0.6.6` findings (which directly discuss "other M-code characteristics present") already give Stage 4 some indirect signal — vocabulary-level comparison has no equivalent indirect source.
- **`M0.6.3`/`M0.6.4`** ("the primary anchor verse" for the WHOLE characteristic) need visibility across every one of a characteristic's subgroups at once — Stage 4 is deliberately subgroup-scoped (per-subgroup call, own member strongs only), so even re-scoping wouldn't supply the cross-subgroup comparison the question actually asks for.

Confirmed live: no `char-synergy`/synergy stage is registered anywhere in `cfg_step` — this was named in the original `#1682` process spec and every stage-generator module's own docstring as planned, never built. Closing this category is real, scoped, future build work (a genuine 5th stage, its own payload design, its own cost budget) — not something to fold into this pass. Flagged, not designed further here.

| code | question (truncated) |
|---|---|
| X0.4.1 | Which vocabulary terms does this characteristic share with OTHER characteristics programme-wide? |
| X0.4.2 | Does the sharing extend to root-level architecture across characteristics? |
| X0.4.3 | What does the vocabulary sharing show about the conceptual relationship? |
| M0.6.3 | Does any verse function as the primary anchor across the WHOLE characteristic? |
| M0.6.4 | What does the primary anchor verse show that no other verse shows? |

## Category E — 4 questions: already designed, on escalation #1805, pending your decision

Not re-derived here. Source data exists (`Workflow/Sciences/science_files/`, 99 files, 1:1 cluster coverage verified `BUILD.md` #269) and each file already carries a dedicated "prompt reference notes" section pre-written for these exact 4 questions. Proposed build (escalation #1805 v5): read the file, extract that section into Stage 4's payload as a new field, lift the science-extract exclusion filter per-cluster once present. One open design choice named there (filename-match vs. a registered mapping) — your call.

| code | what it needs |
|---|---|
| D9.1.1 | neuroscience/physiology mechanism, per the cluster's science-extract file |
| D9.2.1 | generational transmission, per the cluster's science-extract file |
| D11.2.1 | genetics/innate-endowment, per the cluster's science-extract file |
| D12.1.1 | behavioural-science social expression, per the cluster's science-extract file |

## Incomplete data (distinct from unanswerable) — `M83/A_general_seeking`

Not a placement problem — a genuine execution blocker for an already-reachable subgroup. Its 2 member strongs (`G2212`=116, `H1245`=225 corpus occurrences) both individually exceed Stage 3's 60-occurrence cap at once — `charreadinggenerate.py`'s own `MultipleOverCapStrongs` exception exists for exactly this and states plainly it is "not yet designed" (Finding 11/#1806). Affects all 52 Stage-4 questions for this ONE subgroup (328 of M83's 496 verses, 66%) — every question is correctly WIRED for it, but it can never be reached because Stage 3 can't process it. Fix candidate (not designed in detail here): extend `_partition_occurrences_by_surface`'s splitting logic to handle 2+ simultaneously-over-cap strongs, not just the single-strong case it handles today — a packing-order design question, your call on the approach.

## What this document does NOT do

Nothing here has been applied. Categories A/B/C are mechanical/low-risk and could be built quickly once confirmed; Category D is a real, separate, larger build (a genuine 5th pipeline stage) that deserves its own scoping pass, not a rushed addition here; Category E already has its own decision pending on #1805; the `M83` cap-strong blocker needs a packing-order design decision before any code is touched.
