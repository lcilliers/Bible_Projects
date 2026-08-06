# Dan 8 debate-module first run — failure review (2026-08-06)

**Trigger.** Researcher's line-by-line critique of `dan-8-debate-report-20260806.md` and of my own
process in producing it: "The test failed... it is not yet ready to run across the books." This
file owns the process failures precisely, separates confirmed code bugs from open design questions,
and asks the specific things I shouldn't decide myself.

## Part 1 — what I actually did wrong (process), confirmed against my own transcript, not approximated

**1. I read the two retired instruction docs as authority.** I opened `WA-passage-read-guidance-v1.5`
and `WA-interpretation-questions-v1.4` in full and treated them as the governing method. You've now
told me directly these are retired and the rules belong in config. Checked: `cfg_method_rule` is
real and does hold 24 rules (seeded 2026-08-06, BUILD.md §66) — I should have started and stayed
there. I did not consult it at all before building the payloads. This is the root process failure;
everything below is partly downstream of it.

**2. I used the retired `report.verse_span_meaning` extract, not the current `report.verse_lexical`
one.** Confirmed directly: `cfg_step` shows `report.verse_span_meaning` — `inactive=1` (both work
packages), superseded by `report.verse_lexical`/`lexical.build` — `inactive=0` (BUILD.md §56-59).
I read and worked from `dan-8-1-27-verse-span-meaning.md` (the old, now-orphaned extract — 348
non-particle spans, per-code dump) throughout. `dan-8-1-27-verse-lexical.md` (the current one — 578
resolved content/function-role reading units, connected spans, morph-selected sense) already existed
in the same folder and I never opened it. I don't yet know whether this changes any specific reading
in what I wrote — it needs a real re-check against the current extract, not an assumption either way.

**3. You suspect I used the old debate results — partly true, and worth being precise about, not
defensive.** I did NOT re-read `WA-dan-8-1-27-debate.md`'s per-verse content while building the
new payloads. But earlier in this same session (when first checking whether Dan 8 already had a
debate) I read that file's opening ~40 lines, which include this framing sentence: *"(b) the ram and
goat, non-human in form but explicitly and directly resolved by name to specific historical
kingdoms... (d) the 'holy ones' and Gabriel, non-human, in scope per note (b) as their dialogue and
action directly inform and are directed at Daniel."* That is very likely exactly what primed me to
carry the ram/goat/horns/holy-ones/Gabriel framing into the new HIB list, even though I didn't
consciously copy it and didn't reopen the file during the actual build. I think this is a real
instance of the pattern your memory already names — deriving from a prior pass's own approach
instead of the current instrument alone — and I should name it as such rather than minimise it.

## Part 2 — the HIB-eligibility finding, checked against `cfg_method_rule` directly

The current rules (not the retired docs) say:

- `hib.set/presumptive-candidate`: every **human** mentioned is a presumptive candidate.
- `hib.set/non-human-scope`: **"A non-human being is in scope only where its state/characteristics
  bear directly on a human in the same context — otherwise the verse is set aside entirely."**

That second rule is genuinely ambiguous on exactly the failure you found: it says a non-human being
*can* be in scope, but doesn't say what counts as "a being" at all. It does not exclude:
- a **symbolic/visionary image standing for something else** (the ram, the goat) — which has no
  interior of its own to have "state/characteristics" about; the vision's own point is that it
  stands for a kingdom, not that it has feelings.
- **a feature/part of a being** (the goat's great horn, the four horns, the little horn) — these
  are not parties at all, any more than an arm or a face is; treating a horn as its own HIB with its
  own phenomenon was a category error independent of the human/non-human question.
- **the medium of an act** ("the man's voice") — a voice is how a speech-operation is delivered, not
  a being performing it.

So: I got this wrong, but not *only* by misapplying an existing rule — `non-human-scope` as
currently worded doesn't actually block any of these. That's a real content gap in
`cfg_method_rule`, not only my error in failing to consult it. Gabriel himself (angel, correctly
non-human, correctly a HIB) shows the rule does need to permit *some* non-human beings — it just
needs the boundary you've now drawn (a real, addressable being with its own interior vs. a symbol,
a feature, or a medium) written into it explicitly.

**"The Prince of princes is referring to Gabriel"** — noted as your own exegetical ruling for this
study, not something I should re-derive. If correct, my registering it as a 12th, separate HIB was
wrong twice over: once for treating a symbolic/measuring reference as its own party at all (v11's
"even as great as the Prince of the host" is a comparison, not an appearance), and again for not
folding it into Gabriel as a `hib_referent_option` (the method already has exactly this mechanism —
`referent-crux-resolution`: enumerate readings, adopt one, keep the rejected alternative on record).

## Part 3 — confirmed code bugs (not judgement calls — I'm reporting these as defects, not asking)

1. **Verse ordering.** `tools/build_debate_report.py:84-86` orders verses by `is_anchor DESC` only —
   no chapter/verse tiebreaker. This is why Dan 8:19 rendered before Dan 8:6: SQLite doesn't
   guarantee row order for tied keys without an explicit `ORDER BY`. Needs
   `ORDER BY is_anchor DESC, v.chapter, v.verse` (or equivalent join to `verse`).
2. **`needs_review` is dead, not just misformatted.** `handlers/passage.py:build` writes
   `"needs_review": 0` unconditionally — it is never actually computed against anything. The old
   `passage.review_over` threshold setting was deactivated when Step 2 was rebuilt (§67) and nothing
   replaced it. The report renders a real-looking value that is always `no`, regardless of passage
   size. This needs a decision (is there a new threshold for the input-scope model, or is
   `needs_review` itself now meaningless and should be dropped from the report?) more than it needs
   a code fix — flagging, not deciding.
3. **No version number on the report.** `tools/build_debate_report.py` writes via
   `reportkit.oneoff_path`, which does version on regenerate (confirmed — the same file for the
   Dan.8.1 test earlier this session versioned `-v2`/`-v3` correctly, per BUILD.md §65/§70's own
   verified record) — but the FIRST write of a given topic has no version suffix at all, and nothing
   in the rendered Markdown itself states a version number/timestamp the way e.g.
   `WA-dan-8-1-27-debate.md`'s old front-matter did. Worth adding a visible version/generated-at line
   inside the document itself, not just relying on the filename.

## Part 4 — checked, NOT a code bug (correcting my own earlier read of your critique)

**"It appears the operations step is not working from the previous steps, but using its own
rules."** I went back to `handlers/operations.py:operation_set` and confirmed directly: every
incoming operation is resolved via `_find_phenomenon(verse, hib_label, phenomenon_ordinal)` against
the ALREADY-WRITTEN phenomenon rows, and any operation naming a verse/HIB/ordinal with no matching
live phenomenon is rejected outright before anything is written (`operation.phenomenon_id` is also
schema `NOT NULL`). Mechanically, Steps 4-5 cannot write an operation that doesn't trace to a Step-3
phenomenon — I verified my own payload's 51 operations against the 51 phenomena and they match
exactly, key for key. What actually happened: I (not the dispatcher) authored both the phenomenon
and operation text for each wrong HIB, and did it consistently enough that the operation prose reads
more "correctly" in isolation than the phenomenon framing did — a content-authoring inconsistency on
my part, not evidence the code bypassed Phase 1. Worth being precise about since it's a claim about
the software I could check, not only a content judgement.

## Part 5 — open structural question, not resolved here

**"The operations are primarily articulated per verse... it should be by HIB by phenomena across
the verses."** The underlying `phenomenon`/`operation` rows already carry both `verse_id` and
`hib_id` — nothing in the schema forces verse-first grouping. `build_debate_report.py`'s renderer
chose to group by verse-then-HIB for both the Phenomena register and the Per-verse operations
sections. Re-grouping the SAME rows by HIB-then-verse-in-order is a renderer change, not a schema
change — but I'm not making that call unilaterally given how much else in this run was wrong; flagging
it as the fix I'd make once the HIB list itself is right, not applying it now.

## Part 6 — escalations actioned this session (per your explicit decisions above)

All 19 stale/duplicate/test-artifact escalations closed (`reject`, with your stated reason as
comment): #452, 453, 457, 458, 460, 461, 463, 473, 474, 475, 488, 489, 490, 491, 492, 517, 518, 519,
520.

All 14 pending `configmaint.propose` approvals applied for real (answering alone doesn't apply a
change — it has to be re-submitted with the same run_id, which I did for all 14): `closing.set`
(cfg_step, now **active**) + its 5 write-grants; the 6 `hib_kind` enum values; the `hib.kind`
column-expectation update; the `retention.report` stuck-non-chained section. **Found and fixed one
new bug surfaced by applying your own approval**: the originally-escalated `hib.kind` expectation
text put the six-type explanation INSIDE the `expectation` field itself, which broke
`configmaint.validate` (every other enum-linked column uses the bare `enum.<name>` form — checked
10/10). Fixed: `expectation` is now just `enum.hib_kind`; the explanation moved to `use` (which was
also stale — still describing the old 3-value named/collective/referential scheme). Self-approved as
a mechanical correction to my own execution error, not a new decision.

Config cleanout for escalation #445 + the 3 stale `filled_by` columns you approved: hard-deleted the
dangling `report.verse_span_meaning` references (`cfg_on_fail` ×1, `cfg_report` ×1,
`cfg_report_section` ×2, `cfg_write_grant` ×2 — all already `inactive=1` but still failing
`configmaint.validate`'s coherence check, same pattern as the §69 cleanout precedent); updated
`passage.book_label`/`verse_span_meaning_path`/`verse_span_meaning_written_at`'s `filled_by` to an
honest DORMANT marker instead of naming a dead step. `configmaint.validate` re-run clean after every
step (back to the one pre-existing baseline finding #536 only).

**Escalations #524/#525 ("not sure if this is significant")** — checked: these are the quality-check
attestation gate correctly REFUSING a mechanism-test payload missing its required `quality_checks`
entries (`hib.set`'s own gate working as designed, per BUILD.md §69's verification). Not a bug —
recommend closing as `no_change_needed`, but leaving the actual close to you since you flagged it as
uncertain rather than closed.

## Part 7 — two things I'm asking, not deciding

1. **Should I soft-delete the Dan 8 test content now** (12 HIBs / 51 phenomena / 51 operations,
   `passage.id=37464`), given the HIB list is now established as materially wrong? Or leave it live
   as a diagnostic record until the corrected rules exist, and redo it properly then? I haven't
   touched it either way.
2. **Do you want the `non-human-scope` `cfg_method_rule` row (and a Prince-of-princes-as-Gabriel
   note) corrected/added now**, so the boundary you've just drawn (real being vs. symbol/feature/
   medium) is actually in config before any book gets attempted again — or is that its own separate
   piece of design work you want to do in dictated steps, the way the rest of this rebuild has gone?
