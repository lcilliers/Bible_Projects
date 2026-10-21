# Verse-lexical Window 1 — pre-build validation test plan (v1)

**Filename:** 1383-verse-lexical-window1-validation-test-plan-v1-20260903.md
**Escalation:** #1383
**Stage:** the validation gate itself — the step between DESIGN/PROPOSE and TEST-PLAN/BUILD-PLAN,
per #1379 v7's own recorded "next session" sequence: (1) run the checklist on more practical
example verses/passages, (2) do a deep-dive manual analysis of the same passages to verify the
checklist's results against it, (3) only then move to build. **This document is that plan**, not
yet run.
**Not to be confused with** §9 of `1383-verse-lexical-enrichment-design-propose-v1-20260903.md`
("Test plan") — that one tests the BUILT schema/handler once it exists (post-build functional
correctness). This one tests the METHOD — whether the checklist itself, as currently written, is
sound enough to build a schema and `lexical.enrich` handler around — before schema is committed to.

---

## 1. Is the checklist complete? No.

The checklist (`1379-verse-lexical-enrichment-checklist-v1-20260902.md`) labels itself, in its own
header: "**Status:** PROTOTYPE — being test-driven... before any schema/code work starts... not
treated as closed." Its own closing section, "Open items this checklist does not resolve," names
four items, none struck through, none resolved:

1. **Genre sourcing** (CRITICAL, blocks the process gate) — #1383's design proposes *where* genre
   would live (`passage.genre`, free text) but not *how* it gets determined beyond "manually, as
   part of the read" — no controlled vocabulary, no worked heuristic beyond the three verses tried.
2. Whether the logical/causal-connective item (surfaced by Hos 2:4) is a permanent addition —
   #1383 §4 answers this as a design decision, but it has not been re-tested against a fresh verse
   since being added.
3. The `H0853` direct-object-marker role-classification question — same status: answered as a
   design/code decision in #1383 §4, not yet re-verified against a fresh verse.
4. **Greek/NT equivalents** for the chain/sequencing test and the `H9xxx` role heuristic — never
   tested. All three verses run so far (Dan 1:8, Ps 25:2, Hos 2:4) are Hebrew/OT. Deliberately
   parked, not a gap to close this round — see §6 below.

**Coverage run so far, exactly:** 3 verses, all Hebrew, all Old Testament, all treated as isolated
single verses. **Zero passages** (in the `verse_id`-plural, multi-verse-block sense #1379 v7 itself
defines) have ever been run through the checklist — the "one integrated read per verse/**passage
block**" model, self-determining sequential boundaries, and the 20-verse cap are all v7-stage
decisions that have never actually been exercised against real data.

## 2. What this validation phase must actually test, and why the existing 3 verses don't cover it

| Gap | Why the existing 3 test verses don't close it |
|---|---|
| A genuine multi-verse **passage block** (not a single verse) | Hos 2:4 sits inside a registered 23-verse passage, but the checklist was run on verse 2:4 alone, per the applied doc's own scope — the passage-block mechanics (self-determining boundary, one read spanning several verses, handoff to the next block) were never actually exercised. |
| A genre never tried: **law/instruction** | Legacy `bible_research.db.verse.genre` buckets: prophetic (Hos 2:4 ✓), narrative (Dan 1:8 ✓), poetic/wisdom (Ps 25:2 ✓), **law/narrative (untested)**, epistle / gospel-narrative (NT — parked, §6). |
| A **genre-boundary** case, on purpose | The John 1:5 finding that established "genre is a passage property" was itself a boundary case (a hymnic insert inside gospel-narrative). The checklist has never been run across an actual narrative→poetry (or similar) seam to see whether the self-determining-boundary logic actually lands the split in the right place by hand. |
| A second, structurally different wisdom/poetic sample | Ps 25 is an acrostic lament — long, one register throughout. A short, aphoristic wisdom couplet is a different shape (dense, idiom-heavy, two tightly-bound clauses) and exercises the idiom/combined-span test differently. |

## 3. Proposed test set — 3 passages, all Hebrew/OT — **recommendation for your confirmation, not decided**

| # | Reference | Verses | Why this one |
|---|---|---|---|
| 1 | **Deuteronomy 6:4–9** (the Shema + instruction) | 6 | Untested legacy genre bucket (law/instruction); a real, self-contained multi-verse passage — first actual test of the passage-block/self-determining-boundary/one-integrated-read model; well-known enough that a manual cross-check is fast to do well. |
| 2 | **Proverbs 3:5–6** | 2 | Untested wisdom texture (aphoristic couplet, not lament); dense idiom test ("lean not on your own understanding" — construct/idiom-heavy); smallest possible passage, a good boundary case in the other direction (is 2 verses enough to register as its own block, or does the self-determining logic want to pull in 3:7 too?). |
| 3 | **Exodus 14:31–15:3** | 4 | Deliberately spans a genre seam — v14:31 is narrative resolution ("Israel saw... believed"), v15:1 is the pivot line ("Then Moses and the Israelites sang..."), v15:2–3 is the Song of the Sea itself (poetry). Stress-tests whether the self-determining-boundary read actually detects the shift and where it lands the split, the same shape of question the John 1:5 case raised, on purpose this time rather than by accident. |

All three checked live: verses exist in `iba.db`, none currently belongs to an active (non-deleted)
registered `passage` row — genuinely fresh test material, not overlapping Hos 2:4's existing
passage.

**If any of these three isn't the right choice** (a better-known law text, a different wisdom
couplet, a cleaner genre-seam example) — say so; the exact selection is the one open judgement call
in this document.

## 4. Methodology — per passage, same three-step shape each time

1. **Claude runs the full checklist** against the passage as a single integrated read (per the v7
   process model — genre/language/testament determined as that read's own first move, not
   pre-supplied), and files an applied doc in the same shape as
   `1379-verse-lexical-enrichment-applied-ps25-2-hos2-4-v1-20260902.md` — every checklist item,
   per code, with the reasoning shown, not just the conclusion.
2. **You do an independent read of the same passage** and check it against what the checklist
   produced — anything it missed, got wrong, or where your own read reaches a different
   conclusion. (If you'd rather I show you the checklist's output first and you critique it
   line-by-line, rather than reading the passage cold yourself first, say so — both are genuine
   ways to satisfy "verify the checklist's results against it," and which one you want is your
   call, not mine to assume.)
3. **Reconcile every divergence**, sorted into exactly one of three buckets, same discipline the
   checklist already uses for `unresolved`/`unclassified`:
   - **Checklist gap** — a real miss or wrong rule. Checklist gets corrected in place (same as the
     Hos 2:4 connective-item addition), and the correction is dated and attributed to this pass.
   - **Genuine judgement call, no single right answer** — flagged explicitly as such (matching the
     "related-word sorting" and "cohabitation"-style contested-entry precedent elsewhere in this
     project), not silently resolved either direction.
   - **Checklist correct** — confirms the item as-is; no change.

## 5. Explicitly out of scope this phase

**Greek/NT.** All three candidate passages are Hebrew/OT, on purpose. The Greek/NT gap (chain-test
equivalent, `H9xxx`-style role heuristic, and the researcher's own broader 2026-09-02 note that
`verse_lexical` "does not work for large parts of the NT") stays parked, per direct researcher
instruction already on record in #1379 — not silently re-opened by this validation round, and not
a blocker for closing it.

## 6. Exit criteria

This phase is done, and the schema/build content in §5–§9 of
`1383-verse-lexical-enrichment-design-propose-v1-20260903.md` is ready to be resubmitted for
approval, when:

- All 3 passages above (or your substituted set) have an applied doc and a reconciliation pass.
- The passage-block/self-determining-boundary/one-integrated-read model has been exercised at
  least once for real, not just decided on paper.
- Every reconciliation item lands in one of the three buckets in §4 — no item left uncategorised.
- Any checklist corrections from this pass are folded into
  `1379-verse-lexical-enrichment-checklist-v1-20260902.md` itself before the schema design is
  treated as final (the schema in §5 is built to match the checklist's *current* item set —
  `verse_lexical_note.note_type`'s 11 values — so a checklist correction that adds/removes an item
  type may require a matching, small schema-doc update, not just a checklist-doc update).

A small number of items landing in "genuine judgement call, no single right answer" is an expected,
healthy outcome (the checklist already carries several by design — related-word sorting, e.g.) —
not a sign the phase failed.

## 7. Open items requiring your answer before this plan starts

1. **Passage selection (§3)** — confirm the three above, or substitute.
2. **Reconciliation mode (§4 step 2)** — you read each passage cold first, or you critique my
   checklist output directly? Either is fine; state which.
3. Anything else about scope or method you want changed before this runs.
