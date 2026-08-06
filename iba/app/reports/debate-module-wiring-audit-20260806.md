# Debate module wiring audit — why testing against Dan 8 failed (2026-08-06)

**Trigger.** Researcher: "It is evident that the iba app is not yet complete for the new debate
module... testing the new debate module failed. go back and analyse the build that was done in the
previous session [and] check the wiring."

**Method.** Read BUILD.md §61-70 in full (the entire "new debate module" build, 2026-08-05/06), then
checked every claim in it directly against the live DB (`iba/app/db/iba.db`) and `cfg_step` —
not taken on the doc's word. No code was changed in this pass; this is diagnosis only.

## Bottom line

**The wiring is real and does work — but it has never been run with real content, for Dan 8 or any
other book.** Every one of BUILD.md §61-70's "verified end-to-end" claims was a synthetic
`"(MECHANISM TEST)"` payload, deliberately cleaned up and the DB restored afterward, every single
time. That pattern is stated explicitly in the build record itself (§63: *"this session built and
proved the mechanism, not the Daniel 8 (or any other) analysis itself"*) and confirmed independently
here by direct query:

| table | live rows, whole DB (all books) |
|---|---:|
| `hib` | 0 |
| `verse_hib` | 0 |
| `phenomenon` | 0 |
| `operation` | 0 |
| `operation_party` | 0 |
| `passage` with `rule='input-scope'` (the current, non-retired passage model) | 0 |
| `passage_linkage` / `_insufficiency` / `_emergent_question` / `_validation_note` | 0 each |

So when the debate module was tested against Dan 8 this session, it correctly reported there was
nothing to show — because there genuinely is nothing there. That is not a bug in the report tool;
it is the actual, honest state of the database.

## What is actually built and active right now

Confirmed live in `cfg_step` (not just claimed in BUILD.md):

| step | work_package | inactive? |
|---|---|---|
| `hib.set` | operations-ingest | **active** |
| `phenomenon.set` | operations-ingest | **active** |
| `operation.set` | operations-ingest | **active** |
| `passage.build` | build-passages | **active** (rebuilt §67 — now "input-scope", the whole HIB-continuity sub-division algorithm from §62 is retired) |
| `closing.set` | — | **NOT REGISTERED AT ALL** — its `cfg_step`/`cfg_write_grant` proposals are still pending (see below) |
| `report.passage_debate` (legacy scaffold generator) | passage-debate-report | inactive |
| `report.passage_debate` (chained into chapter-generate) | chapter-generate | active |
| `passage.debate_sync` | passage-debate-sync | active |

`iba/app/tools/build_debate_report.py` (the DB-render tool I ran against Dan 8 in this session) is
real, correctly refuses on a legacy passage, and would work the moment a real `input-scope` passage
with real phenomena/operations exists for Dan 8. It has none to render.

## Why nothing has actually landed for Dan 8

1. **Step 2 (`passage.build`) was rebuilt mid-session (§67)** — the researcher, looking at real HIB
   distribution across four books, concluded the original HIB-continuity sub-division algorithm
   (§62) didn't correspond to anything real ("no logical breakup... more about the capacity of AI to
   read the entire chapter"). The whole algorithm was retired same-day and replaced with
   "passage = the debate's own input scope" (`-Chapters`/`-Range`, registered verbatim, no
   sub-division). So even the *shape* of a passage under the new model changed twice in one session.
2. **Every live test after that point used `Range 8:1-1`** (a single verse) or `8:1-3`, always
   against synthetic content, always cleaned up and the real legacy `Dan 8:1-27` row (`id=37425`)
   restored from backup afterward — confirmed directly: that row is still `rule=NULL` (legacy),
   `deleted=0` (live), `debate_status='filled'` — i.e. still backed by the **old** hand-filled
   markdown from 2026-07-27, never migrated.
3. **`closing.set` (Step 7 — linkages/insufficiencies/emergent questions/validation notes) cannot
   run at all** — confirmed absent from `cfg_step` entirely. Its approval batch is 6 of the 14 items
   still sitting `raised`/unanswered in `escalation` (run_ids `RUN-CLOSINGSET-STEP`,
   `RUN-CLOSINGSET-GRANT-*` ×5, escalation ids 494-499).
4. **The `hib_kind` 6-value enum is also unapproved** (6 more of the 14, ids 501-506) — the code that
   checks it (`_valid_hib_kinds`) is live and correctly *skips* the check while pending (not a
   silent pass), but it means HIB-typing has no real enforcement yet either.
5. Remaining 2 of the 14: `cfg_column` expectation update for `hib.kind` (507), and a
   `cfg_report_section` for stuck-non-chained-run monitoring (508) — both cosmetic, not blockers to
   analytical content, but still open.

Confirmed against the live `escalation` table: exactly 14 `configmaint.propose` items in state
`raised` — matches BUILD.md §70's own count exactly, so the doc's bookkeeping is accurate. (The
other ~31 `raised` rows are `configmaint.validate` advisories and report-stops from this session's
own test runs — noise §68 already diagnosed, not additional pending approvals.)

## What this means concretely for "run the debate module for Dan 8"

There is currently **no path** to a real, DB-sourced debate report for Dan 8 that doesn't start with
doing the actual analytical work — none of it can be synthesized or inferred from the old legacy
markdown file, and none of it should be, per the researcher's own repeated instruction this session
that adjudication has to be a genuine re-read, not a carry-over. Concretely, in order, all still
undone for Dan 8:

1. **Step 1** — a real `hib.set` call for Dan (or just ch. 8) — actually identify every HIB
   (inner-being referent) per the six-type scheme, for real, from the text.
2. **Step 2** — a real `passage.build -Book Dan -Chapters 8` (or narrower, if 27 verses proves
   infeasible to read as one scope — the mechanism will say so and refuse if it is).
3. **Step 3** — `phenomenon.set` for that passage.
4. **Steps 4-5** — `operation.set`.
5. **Step 6** — re-run `build_debate_report.py` — this part will then actually work, exactly as
   designed.
6. **Step 7** (`closing.set`) — blocked until you approve the 6 pending `RUN-CLOSINGSET-*` items
   (494-499). Steps 1-6 do **not** need those 6, or the `hib_kind` enum items, to proceed — both are
   independently gated already-live code, not hard prerequisites for HIB/phenomenon/operation
   writing itself.

None of that analytical work happened in the build session — it was explicitly out of scope
("built and proved the mechanism, not the analysis"). That is the actual gap, not a wiring defect.

## Open items surfaced, not decided here

- 14 `configmaint.propose` approvals waiting on you (ids 494-499, 501-508) — listed above with what
  each unblocks.
- Whether to now run the real Step 1-5 analytical pass against Dan 8, and at what scope
  (`-Chapters 8` vs. a narrower `-Range`, per Step 2's own feasibility self-assessment) — a real
  decision, not mine to default into.
