# Session Log — 2026-08-03 — Verse-reading technique consolidated to v3 (Final) and test-run end to end on Obadiah 1:1-21

## Reason for closing

Researcher will clear context, re-introduce `WA-verse-reading-technique-v3` fresh, and direct
further tests from there. Closing here to hand off cleanly at that boundary.

## What was done, in order

1. **Ran `Start-Iba.ps1`**, confirmed config/DB/STEP live, per session-start convention.
2. **Researcher stated four staging principles** for driving the inner-being study through the DB,
   arrived at independently this session: (a) verse reading must be lexical, not a gloss/paraphrase
   reading; (b) determining human-being candidates for study is complex, not a quick scan; (c) an
   inner-being operation must be studied in isolation, subject fixed first, never contaminated by
   other subjects in the same passage; (d) the process must never run as a single pipeline — the
   main cause of drift. A three-step plan followed: step 1 capture a per-verse lexical reading in
   the DB (format undecided); step 2 categorise human beings present per passage; step 3 describe
   each human's inner-being process, scattered through the passage, in isolation. Each step gated
   by the researcher's own manual verification — no automatic chaining between steps.
3. **Drafted a step-1 format** using Obad 1:1 as a worked example against the existing
   `report.verse_span_meaning` extract, then extended it to the full Obad 1:1-21 (verse 19 skipped,
   `governance.verse_gap_by_design`). Filed as `iba/app/reports/verse-reading-step1-format-
   draft-20260803.md` and `iba/app/reports/verse-reading-step1-output-obad-1-1-21-DRAFT-
   20260803.md`. Surfaced real cross-verse findings (a pronoun-referent-naming pattern dominant
   across the passage; a 2mp/2ms number shift at v16; a 3ms/2ms suffix mismatch at v3; two distinct
   lexical entries for "Esau" — person vs. place — kept apart; v20's "host" not matching its own
   cited lexical range).
4. **Researcher's quality check exposed real gaps** in that first pass: morph was not
   systematically used (a genuine anomaly at v13 was missed); the STEP data's own `variant`
   (specifically resolved) vs. `base ... fallback` (undisambiguated) distinction was not tracked,
   so several citations were presented as resolved when they were actually generic; the reading's
   prose tracked the ESV's own word order too closely rather than being built independently from
   the lexical spans. Acknowledged plainly, not minimised.
5. **Discussed how to get consistent quality**, given the drift found. Rejected "just run each
   verse as a separate session" as neither necessary nor sufficient on its own. Proposed instead:
   separate what's mechanical (strong/morph/variant-status extraction — should eventually be a
   deterministic script, not sustained manual diligence) from what needs judgment (the actual
   reading — should run in small, self-audited batches with the audit shown, not trusted silently).
   Not built this session; recorded as the direction, not yet implemented.
6. **Extracted every existing verse-reading instruction** from memory, governance, `BUILD.md`, and
   `iba/docs/` before any further design work, per the researcher's direct instruction — surfaced
   that `WA-verse-reading-technique-v2-2026-08-03.md` **already existed**, drafted in a session
   earlier the same day (before this session's context was cleared), DRAFT/unconfirmed, and **not
   config-registered** (no `method.verse_reading_technique_path` setting, unlike its two companion
   docs, both of which are registered and both of which fail loudly if their file goes missing).
   Also surfaced `WA-passage-read-guidance-v1.5` and `WA-interpretation-questions-v1.4` (both
   config-registered, revised 2026-08-02 after an Amos 1-3 phenomenon/movement drift diagnosis, with
   the same three-phase separation discipline the researcher had just independently re-derived for
   the verse-reading step). Filed as `iba/app/reports/verse-reading-instructions-extract-
   20260803.md`, explicitly excluding memory entries confirmed to belong to the separate
   `bible_research.db` programme rather than this app.
7. **Researcher manually rewrote the technique doc as v3 ("Final")**, consolidating the scattered
   guidance found in step 6 plus prior prototyping into one document: T1-T3 lexical-sense/morph
   rules unchanged in substance; T4 (referent cruxes) and T5 (genre-conventional absences) carried
   over from v2; v2's separate "causing action vs. resulting condition" and "unstated agent recorded
   as open" rules dropped (confirmed deliberate — deferred to later movement analysis, not part of
   base reading); a new second part added — T6-T9, lightweight "stamps" (*IB* = human only, *Agent*
   = the doer noun (human or non-human), *Process* = state/condition/faculty words tied to an IB,
   *action* = the verb) — explicitly preliminary, not analysis, and gated to run only after T1-T5 is
   complete for the *whole* passage, mirroring the phase-separation already in the guidance docs.
   Added a "Raw data" section naming the underlying DB tables.
8. **Seven clarifying questions raised before testing**, covering: the status of the two dropped v2
   rules; whether non-human beings get stamped *IB* or something else; whether *Agent* targets the
   doer or the verb; how broad *Process* is meant to be; whether stamps can stack on one word; the
   input mechanics (rendered extract file vs. querying `iba.db`'s raw tables directly — flagged
   against the standing rule of no direct SQL to `iba.db` outside a defined operation); and whether
   the listed table names were verified. **Researcher answered all seven inline** in the document
   itself and edited the doc accordingly (T7/T9 clarified as noun-vs-verb; T8 broadened explicitly;
   the human-only/non-human-as-Agent split made explicit; the deferred-to-movement-analysis note
   added).
9. **Verified the doc's table list directly against the live `iba/app/db/iba.db` schema** — a
   read-only `sqlite_master` table-name listing only, no data queried, consistent with the no-ad-hoc
   -SQL rule while fulfilling the researcher's explicit instruction to verify and correct. Corrected
   hyphenated/mixed-case names (`lema inventory`, `Strong-Lsj-parsed`, etc.) to the actual schema
   (`lemma_inventory`, `strong_lsj_parsed`, etc.); flagged `strong_meaning_parsed` as present in the
   live schema but absent from the doc's list, relevance unconfirmed.
10. **Ran the full test**: Obad 1:1-21 against v3's T1-T9, phase-gated as specified (T1-T5 for every
    verse across the whole passage before T6-T9 began for any verse), using the existing
    `report.verse_span_meaning` extract as the lexical basis per the researcher's own Q6 answer
    (valid for already-processed books; direct-from-tables sourcing is the target for books not yet
    run, a separate build decision, not solved here). Produced `iba/app/reports/verse-reading-v3-
    test-obad-1-1-21-20260803.md` (narrative) and the matching `.json` (component nodes, per the
    doc's "not yet finalised" output instruction). Genuine anomalies surfaced and recorded, not
    smoothed over: v3's 3ms/2ms suffix mismatch, v13's 2fp verb against an otherwise-uniform 2ms
    passage, v16's 2mp verb, a fully-enumerated v11 "his" referent crux (three candidates, one
    adopted, two kept on record), v20's H2426 lexicon-vs-translation mismatch, three stamps flagged
    uncertain rather than silently resolved (v9 Teman, v20 "this host", v21 "Mount Esau").
11. **Reported one judgment call and one honest limitation** rather than letting either pass
    silently: (a) T4 was applied with two tiers — full multi-candidate enumeration only for genuine
    referential cruxes (v1 "we", v11 "his"), a lighter "open naming gap" note for the passage's many
    simply-unnamed-but-grammatically-clear 2ms addressees — a defensible reading of T4, not
    confirmed by the researcher as the only correct one; (b) the test's own self-check was a single
    retrospective pass over the finished output, not a live per-verse gate applied while writing —
    the same structural condition that caused the drift found in step 4, not yet eliminated by
    sharper rules alone.
12. **Researcher noted the comments** and made further edits to `WA-verse-reading-technique-v3`
    (adding a concrete JSON output sample drawn from the actual test output).

## State at close

- `iba/docs/WA-verse-reading-technique-v3-2026-08-03.md`: current, researcher-marked **Final**,
  all seven clarifying questions answered inline, table names verified against the live schema,
  concrete JSON sample added. **Not config-registered** — no `method.verse_reading_technique_path`
  setting exists; not created this session, left as an open item rather than added silently.
- Test output on file: `iba/app/reports/verse-reading-v3-test-obad-1-1-21-20260803.md` + `.json` —
  filed as test-draft, **not written to any DB table** (destination tables for this reading's output
  are confirmed not yet defined, per the researcher's own Q7 answer).
- Earlier same-session artifacts (`verse-reading-step1-format-draft`, `verse-reading-step1-output-
  obad-1-1-21-DRAFT`, `verse-reading-instructions-extract`) kept on file as the record of how v3 was
  arrived at — superseded in purpose, not deleted.
- No DB writes, no config changes, no code changes this session. One read-only schema
  introspection (table names only) against `iba.db`, explicitly researcher-instructed.
- Pre-existing uncommitted modifications to Daniel/Hosea/Obadiah verse-analysis files, an
  `.obsidian/` folder, and a Hosea PDF were present in the working tree at session start and are
  **not touched by this session's commit** — they predate this session and belong to a different
  unit of work.

## Open items, unresolved

- Whether/how to mechanise the strong/morph/variant-status extraction (proposed step 5) — not built.
- Whether `WA-verse-reading-technique-v3` should be `cfg_setting`-registered, and against which
  step — not decided; its two companion docs are registered, this one still isn't.
- `strong_meaning_parsed`'s relevance to this reading — unconfirmed.
- The self-check-is-retrospective-not-live gap named in step 11(b) — not structurally fixed.
- Whether the six already-completed books need re-reading under v3 — the researcher's call, not
  decided here (same open item carried from the prior verse-reading-technique session).

## Next session

Researcher will clear, re-introduce `WA-verse-reading-technique-v3` fresh, and direct further
tests. Do not assume the outcome of those tests or pre-empt which passage comes next.
