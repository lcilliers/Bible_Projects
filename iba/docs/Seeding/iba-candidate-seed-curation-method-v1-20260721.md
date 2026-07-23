# candidate_seed curation method — v1

> 2026-07-21, extended 2026-07-22. Companion to
> [`iba-candidate-seed-quality-findings-v1-20260721.md`](iba-candidate-seed-quality-findings-v1-20260721.md)
> (the investigation that found the gap),
> [`iba-db-review-response-run-escalation-candidate_seed-v1-20260722.md`](iba-db-review-response-run-escalation-candidate_seed-v1-20260722.md)
> (the researcher's table-by-table review + the tag-cleanliness principle stated below), and
> `iba/app/GOVERNANCE.md` (the config chain this method is governed by). Read this before touching
> a `candidate_seed` row by hand.

## 1. What this method is for

`candidate_seed` (L4b — the over-inclusive candidate assessment) previously had **no way to
correct itself**. `candidate.seed()` (the maintenance step, `Set-Candidates.ps1`) only ever sets
`tag`/`decision` on a row's **first insert** — it never revises an existing row. Once a bad value
was written (mostly at the one-off `import_seed.py` migration, verbatim from the old inventory's
raw `gloss`), there was no governed path to fix it. `configmaint.propose` (the config-change tool)
deliberately cannot help: it is restricted to `cfg_*` tables, never data tables like
`candidate_seed`.

This method is the missing piece: how to see what's wrong (§2), what a clean tag actually means
(§3), how to correct/split/remove one row (§4-§5), and how to add or remove a whole lemma (§6) —
with everything approval-gated, per the same standing rule as every other data judgement call in
this app (never silent).

## 2. Seeing what's wrong — the worklist, not a verdict

Run the standalone quality check:

```powershell
.\iba\app\ps\Candidate-Quality.ps1
```

`candidate.validate` now scans **three** tables through one generic engine
(`iba/app/lib/valuequality.py`, reading `cfg_column.expectation`) and writes one report,
`iba/app/reports/candidate-quality.md`:

- `span_candidate.candidate_tag` — the stamp, as before.
- `candidate_seed.tag` — the seed decision itself. **This is the seed's own report** — before
  2026-07-21 it had none.
- `lemma_inventory.gloss` — the independent substrate `candidate_seed` and `cfg_candidate_rule`'s
  `synonym` rule are built from. Dirt here is upstream of a dirty seed tag, not just a mirror of it.

Each section groups its messy values by **category** (colon dual-gloss, slash alt-gloss,
parenthetical, other) with full counts — a worklist to work through at your own pace, not a
one-time escalation that scrolls away. The escalation itself just asks "is this the known state" —
approve to acknowledge, reject to flag for action, revise with a comment. **Acknowledging the
escalation does not fix anything** — it only confirms you've seen the current picture. Actually
fixing a value is §4.

The per-word (`validation-{word}.md`) and per-book (`validation-book-{book}.md`) reports also carry
a "6. Value quality" section — the same engine, scoped to that word's strongs/spans or that book's
verses, so a reviewer sees it without running the standalone check.

## 3. The tag-cleanliness principle (the researcher's rule, 2026-07-22 — read this first)

A seed tag must be:

1. **A single concept per row.** `"to call:call to"` and `"will/desire"` are TWO concepts — two
   rows, not one. See §5 for what to do when the concept split maps onto distinct sub-strongs.
2. **Searchable as it would actually appear in verse text.** `"to trust (in)"` fails this — `"(in)"`
   is not a real, matchable token.
3. **Never a sentence.** `"be at rest / settle (shakan - and be at rest)"` is a sentence with a
   transliteration folded in — not a tag.
4. **Never a transliteration.** Transliterations are for the `strong.stepTransliteration` field,
   always shown with its gloss (see `feedback_translit_always_with_gloss`) — never bare as a tag.
5. **Never carry special characters.** `` `Terror on Every Side` `` — backticks, brackets, or other
   punctuation surviving from the source text are not a clean label.
6. **Stripped to the word that carries the actual inner-being sense** — surplus words dropped.
7. **Never blank.** A `decision='candidate'` row with no tag is a straight fail, not a pending
   state — see §5's disposition (already applied to the 280 rows found this way).

## 4. Correcting, splitting, or removing one row — `candidate.curate`

`Field` is `tag` | `decision` | `split` | `delete`, all single-row, approval-gated, same shape as
`configmaint.propose` (check → escalate a representative before/after diff → three-way
approve/reject/revise → apply):

```powershell
# correct a wrong tag:
.\iba\app\ps\Candidate-Curate.ps1 -LemmaKey H8085 -Field tag -Value "hearing" `
    -Question "Replace the raw dual-gloss 'to hear: hear' with a clean IB label."

# reject a lemma (soft, reversible — stays in candidate_seed, just no longer a candidate):
.\iba\app\ps\Candidate-Curate.ps1 -LemmaKey H2000 -Field decision -Value rejected -Question "..."

# split a base lemma into a per-sub-strong concept row (see §5):
.\iba\app\ps\Candidate-Curate.ps1 -LemmaKey H0639 -StrongVariant H0639G -Field split -Value "anger" `
    -Question "H0639 covers face/nose/anger across sub-strongs -- split H0639G off as 'anger'."

# remove an invalid row entirely (soft-delete, deleted=1):
.\iba\app\ps\Candidate-Curate.ps1 -LemmaKey G0112 -Field delete `
    -Question "No tag, no registry_match -- an invalid row (rule 7 above)."
```

`-StrongVariant` (optional on `tag`/`decision`/`delete`, **required** on `split`) targets a
specific sub-lettered row; omit it to target the base row (`strong_variant = LemmaKey`). First call
escalates and pauses (exit code 2):

```powershell
.\iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <run_id> -Decision Approve
.\iba\app\ps\Candidate-Curate.ps1 -RunId <run_id> -LemmaKey H8085 -Field tag -Value "hearing"
```

`tag`/`decision`/`delete` require the `(LemmaKey, StrongVariant)` row to already exist —
`candidate.curate` corrects/splits/removes, it does not seed a lemma from nothing. Adding a
brand-new candidate lemma is §6.

## 5. Sub-strong splitting — why `strong_variant` exists

Confirmed 2026-07-22: `candidate_seed.lemma_key` is base-only by design (`candidate.
lemma_base_pattern` strips the sub-letter on purpose) — but **173 of 3,178 base lemma_keys have
multiple sub-lettered `strong` variants with genuinely different glosses** (e.g. `G0769G`
"weakness: weak" vs `G0769H` "weakness: ill"; `H0639G` "anger" vs `H0639H` "nose" vs `H0639I`
"face"). One row per base lemma could never satisfy rule 1 above for these — the tag was forced to
either pick one sense arbitrarily or cram several into one dirty string.

`candidate_seed.strong_variant` (added 2026-07-22, `migration/add_candidate_seed_strong_variant.py`)
fixes this: it defaults to `lemma_key` itself (the row applies to the whole base lemma, no split
decided yet — true for every pre-existing row), or names a specific sub-letter code when the lemma
has been split. The dedup key is now `(lemma_key, strong_variant)`, so one base lemma can carry
several clean, single-concept rows. `candidate.set` (the stamping step) prefers an exact
`strong_variant` match for a span's actual code, falling back to the base row — so splitting a
lemma takes effect on the next `Set-Candidates.ps1` run for any affected book, no other step needed.

Use `Field=split` (§4) to add a variant row; the base row's own tag is untouched by a split (correct
it separately with `Field=tag` if the remaining, unsplit senses need their own clean label too, or
`Field=delete` it if every sense has now been split out).

## 6. Adding or removing a whole lemma — the existing `cfg_candidate_rule` route

Whole-lemma accept/reject already exists and works today (`handlers/candidate.py:seed`'s
`cfg.candidate_rules("accept"/"reject")`) — it was simply never documented as the researcher-facing
add/remove path. It is a `cfg_*` table, so it goes through `configmaint.propose`:

```powershell
# add H1234 as a forced candidate (no tag yet — follow with candidate.curate to set one):
.\iba\app\ps\Config-Maintenance.ps1 -Step Propose -Table cfg_candidate_rule -Op insert `
    -Set '{"kind":"accept","value":"H1234"}' -Question "..."

# force-reject a lemma the independent net wrongly picked up:
.\iba\app\ps\Config-Maintenance.ps1 -Step Propose -Table cfg_candidate_rule -Op insert `
    -Set '{"kind":"reject","value":"H1234"}' -Question "..."
```

Then re-run the seed step so the rule actually takes effect:

```powershell
.\iba\app\ps\Set-Candidates.ps1 -Book <any book>   # candidate.seed runs global, book is just the
                                                     # trigger — see Set-Candidates.ps1's docstring
```

A freshly-accepted lemma has `tag=NULL` (the accept route only decides candidacy, not the label) —
set its tag with `candidate.curate` (§4).

There is also `kind="synonym"` — a curated gloss-substring rule (`cfg_candidate_rule` insert with
`kind":"synonym"`), which marks EVERY lemma whose `lemma_inventory.gloss` contains that substring.
Broader-reaching than `accept`/`reject`; use with care, and re-run `Candidate-Quality.ps1`
afterward to see what it swept in.

## 7. The re-establishment pass — status

There is no automated bulk cleanup for TAG CONTENT — every data judgement call in this app
escalates to the researcher, and there is no principled way to mechanically decide "hearing" vs
"to hear" vs "obey" for `H8085` without reading it. **Done already (2026-07-22):** the one rule that
*was* mechanical and unambiguous — rule 7 in §3, a `decision='candidate'` row with a blank tag is a
straight fail — was applied: **280 rows soft-deleted**
(`migration/delete_blank_tag_candidates.py`, all `layer='ib-judgement'`; 168 of them also had a
blank `registry_match`, the "false row" case). What's left needs a human read, same as always:

1. Run `Candidate-Quality.ps1`, open `iba/app/reports/candidate-quality.md`.
2. Work the `candidate_seed.tag` section's category tables, top-of-frequency first. For each:
   - a genuine single concept, just messily formatted → `-Field tag`.
   - two-or-more concepts mapping to distinct sub-strongs → `-Field split` per concept (§5).
   - two-or-more concepts NOT distinguishable by sub-strong (same `strong_variant`, genuinely
     dual-sense in context) → an open question, same shape as §8 — raise it
     (`Escalation.ps1 -Action Raise`) rather than guessing.
   - shouldn't be a candidate at all → `-Field decision -Value rejected`.
3. Re-run `Candidate-Quality.ps1` periodically to watch the messy-tag count fall — it is not a
   gate, so there's no deadline; work through it at whatever pace fits alongside other cluster work.

Nothing here touches `span_candidate` directly — `Set-Candidates.ps1`'s next book run re-derives
the stamp from the now-corrected `candidate_seed` automatically (`candidate.set` re-stamps clean on
every run, preferring an exact `strong_variant` match, §5).

## 8. Open issues (not actioned — tracked, not guessed at)

- **Dual-characteristic overlap** (raised 2026-07-22): a lemma whose seed match spans two valid IB
  concepts at once (e.g. a term meaning both "spirit" and, idiomatically, "anger") raises a real
  question about how `candidate.set`'s stamp should represent a verse where both readings are live
  — a sub-strong split (§5) only helps when the senses map to distinct Strong's codes; it does not
  help when ONE code genuinely carries both senses in context. Logged as escalation `#228`
  (`Escalation.ps1 -Action List` to see it) — no action taken, no automatic resolution assumed.
