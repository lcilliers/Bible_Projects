# Session log — 2026-07-29 — Obadiah (book 4) complete; retired-work-package guardrail gap found and escalated

Continues the book-by-book passage-debate campaign ([[project_iba_book_by_book_debate_phase]])
straight after the prior session's close-out (`SESSION-LOG-20260729-session-close.md`, commit
`1e7ba3ce`). Researcher picked Obadiah next — a single-chapter book — deliberately out of
`cfg_book_order` canonical sequence (Joel 28, Amos 29, Obad 30).

## What this session covered, in order

1. **`Start-Iba.ps1` startup** — config loaded (`app-0.1.0+e87758c7ee38`), STEP tagged and probed
   OK, orientation docs and current governance rules surfaced normally.

2. **Guardrail incident: attempted to run a retired work package.** Before confirming Obadiah's
   base layer needed rebuilding, I inferred from `USER-GUIDE.md` §8 prose (not from config) that
   `Set-Candidates.ps1`/`Build-Passages.ps1` were the correct per-book prerequisite, and attempted
   to run `Set-Candidates.ps1 -Book Obad`. The researcher stopped the tool call and asked why I
   wanted to run "this retired process." Checking `cfg_work_package` directly showed
   `set-candidates`/`build-passages` both carry `inactive=1` — retired in favour of the current
   verse-first pipeline (`verse-analysis-report` → `passage-debate-report` → `whole-book-read`,
   confirmed via `cfg_step`). The doc (§8) is stale and was not corrected this session.

3. **Deeper guardrail finding, on the researcher's follow-up ("did you not run the configs on
   startup").** Traced why nothing stopped the attempted run: `Cfg.sequence()`
   (`iba/app/lib/cfg.py:115`) selects `cfg_step` by `work_package` name with no `inactive` filter;
   `iba/app/run.py` never queries `cfg_work_package` at all before dispatching a step; the
   `Set-Candidates.ps1` wrapper only checks config-loaded/data-tables-exist, not whether its own
   work package is active. The *only* place `inactive` is read anywhere in the codebase is
   `configmaint.py`, and only to exclude inactive rows from its own coherence report — not a
   runtime execution gate. So a retired work package can currently be run in full, writing data,
   indistinguishable from an active one.

4. **Escalation raised per the researcher's explicit three-part instruction** (self, not via
   `Escalation.ps1 -Action Raise`'s researcher-initiated shape misused — the researcher directed
   the exact content): `MANUAL-20260729_122829_764060`. Records the evidence above plus the
   required fix, verbatim: (a) full config must be read/verified at app startup, not partially;
   (b) `run.py` must consult `cfg_work_package`/`cfg_step` and refuse before dispatch when
   `inactive=1`; (c) a single config-driven mechanism must guarantee `deleted=1`/`inactive=1` rows
   are never processed by any query across any table, replacing today's one-off, handler-specific
   check in `configmaint.py`. Logged as a design/code gap awaiting scoping — **not fixed this
   session**, per the researcher's own instruction to raise it as an escalation rather than patch
   it silently.

5. **Obadiah (book 4) run end-to-end**, once the correct (active) pipeline was confirmed:
   - `VerseSpanMeaning-Report.ps1 -Book Obad -Chapters 1 -BookLabel Obadiah` → base extract,
     245/245 non-particle spans covered, one detected verse gap (`Obad 1:19`, by design).
   - `PassageDebate-Report.ps1 -Book Obad -Chapters 1 -BookLabel Obadiah` → scaffold, then filled
     by hand across all 20 present verses, applying `WA-passage-read-guidance-v1.4` +
     `WA-interpretation-questions-v1.3` verse by verse (operations, Q1-Q11, decisions).
   - `passage.debate_status` resynced `scaffold` → `filled` by calling `passagetrack.record_debate`
     directly (same pattern as `migration/backfill_passage_tracking_daniel.py`) — **not** by
     re-running `PassageDebate-Report.ps1`, which always writes a fresh blank scaffold and would
     have destroyed the filled content (same documented risk as Daniel/Jonah/Joel, `BUILD.md`
     §30).
   - `WholeBookRead-Report.ps1 -Book Obad -BookLabel Obadiah` → gathered the single passage, then
     hand-resolved every item, including real cross-book comparison against Joel (already
     complete) rather than only deferring it.

**Major findings from the Obadiah debate:**
- **The book's clearest Q12 (divine-mirroring) material found so far in the campaign**: vv15-16
  pair two CONSECUTIVE, explicit lex-talionis constructions sharing identical verbs between Edom's
  own past act and the LORD's repayment — "as you have done, it shall be done to you" (v15,
  H6213A both times) and "as you have drunk... so all the nations shall drink" (v16, H8354 both
  times). Denser than Joel's own clearest instance ("sold," H4376, 3:3-8, one pairing).
- **A four-stage escalation of Edom's own complicity** (vv11-14): stood aloof (passive) → gloated/
  rejoiced/boasted (emotional) → entered and looted (active theft) → ambushed fugitives and
  betrayed survivors (active violence) — directly grounds the totality of the judgment that
  follows, and v18's "no survivor for the house of Esau" verbally reverses v14's own charge.
- **Two distinct inner-being faculties (understanding, then courage) named as failing in direct
  succession** (vv7-9) — not seen paired this way in Joel; carried forward as its own emergent
  question.
- **The divine-possessive pattern** ("my people" v13, "my holy mountain" v16) recurs across both
  books read so far; unlike Joel's own three-stage deepening (prophet's voice → narrator's third
  person → God's own quoted speech), Obadiah's instances sit at Joel's deepest register from their
  first occurrence, because almost the whole book is already cast as the LORD's own direct speech.
- An omission — Edom merely "standing aloof" (v11) rather than acting — is explicitly judged
  morally equivalent to active plunder ("you were like one of them"), raising a new emergent
  question about whether this instrument's operation-model needs its own category for omissions.

## Not re-run

Per the same documented risk noted for every prior book this campaign: `PassageDebate-Report.ps1`
and `WholeBookRead-Report.ps1` both always write a fresh blank scaffold on invocation. Neither was
re-run against Obadiah after filling; `passage.debate_status` was synced by calling
`passagetrack.record_debate` directly instead (see item 5 above).

## Artifacts this session

- `iba/app/verse-analysis/Obadiah/obad-1-verse-span-meaning.md` — base extract (new).
- `iba/app/verse-analysis/Obadiah/WA-obad-1-debate.md` — filled passage debate, all 20 present
  verses (new).
- `iba/app/verse-analysis/Obadiah/WA-obad-whole-book-read.md` — filled whole-book read (new).
- Escalation `MANUAL-20260729_122829_764060` — retired-work-package/`deleted`-row enforcement gap,
  open, awaiting the researcher's scoping of the code fix.

## State at handoff

- **Obadiah (book 4)**: fully complete — base extract, one passage debate (the whole book, single
  chapter), whole-book read resolved, matching Jonah/Joel's completion shape.
- **Guardrail gap**: found, escalated, **not fixed**. This is the next task: fix `run.py` (and the
  `.ps1` wrappers as needed) to refuse dispatch against an `inactive=1` work package/step, verify
  `Start-Iba.ps1`'s config read is genuinely complete, and land a single, config-driven
  `deleted=1`/`inactive=1` exclusion mechanism usable by every table query, not just
  `configmaint.py`'s own report.
- **Working tree**: `iba/app/verse-analysis/Obadiah/` untracked, not yet committed as of this log
  being written (commit happens immediately after this log, per `governance.session_log_triggers_commit`).
- **Books complete in the book-by-book phase**: Daniel (book 1, with the open whole-book-read
  caveat noted 2026-07-29), Jonah (book 2), Joel (book 3), Obadiah (book 4). Next book selection
  is the researcher's own call.

## Nothing else pending

No open config proposals from this session. One open escalation (`MANUAL-20260729_122829_764060`)
is the explicitly agreed next task, not an oversight.
