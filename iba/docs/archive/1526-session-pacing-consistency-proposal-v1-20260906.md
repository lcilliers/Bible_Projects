# Session pacing + cross-session consistency — a proposal

- **filename:** 1526-session-pacing-consistency-proposal-v1-20260906.md
- **date:** 2026-09-06
- **escalation:** #1526
- **status:** Proposal, not built. Answers this escalation's own scope: does a Very-Large cluster
  need a sub-batching/consistency design before submission, and how should the untested
  session-throughput estimate get calibrated.

---

## The actual problem, restated precisely

A cluster's verse-set is read verse-by-verse, in bounded sessions (not bulk). For a Very-Large
cluster (9 of them, ~80–183 sessions at my own unverified 20-verse estimate — `737-cluster-size-
theory-and-assessment-v1-20260906.md`), that's potentially weeks of sittings. The risk isn't
whether any one session is done well — it's whether **session 80's judgement on an ambiguous case
matches session 3's**, with nothing currently designed to make that checkable.

## Proposal

**1. Don't design for Very-Large clusters first — calibrate on a smaller one.**
No session-throughput number exists yet because the method has never run for real. Rather than
design a consistency mechanism against a guessed number, the first real submission (whichever
cluster that ends up being) should be treated explicitly as the calibration run: record actual
verses-per-session as it happens, and let that — not my 15–30 guess — set the real number before
any Very-Large cluster is attempted at all.

**2. A minimal consistency record, kept per cluster, not per session.**
Two lightweight things, not a new subsystem:
- **A read-log**: which verses have been given a full debate pass, in which session, so a later
  session (or a different sitting days later) knows what's already covered — this is already
  implied by the proposal's Step 3b (folding prior findings back in), just needs to be the
  mechanism that makes Step 3b possible across sessions, not only across clusters.
- **A calibration note**: whenever a genuinely novel judgement call is made that isn't already
  settled by the catalogue or the method docs (an ambiguous HIB attribution, a borderline
  phenomenon classification), it gets written down at the point it's made — not reconstructed
  later from memory. A later session facing the same kind of case looks this up before deciding
  fresh. This is the actual mechanism that prevents drift; without it, consistency depends on
  recalling every prior judgement call from memory, which won't hold across dozens of sessions.

**3. Sequencing: Very-Large clusters wait until the mechanism has been tested at smaller scale.**
Not a permanent exclusion — just don't make the first test of the consistency mechanism also the
longest-running cluster. A Medium cluster run start-to-finish first would prove the read-log +
calibration-note mechanism actually holds together across multiple sessions before committing to
one that needs 80+.

## What this does not do

Doesn't touch #737's cluster-based methodology (unchanged), doesn't invent a verse-per-session
number as fact (explicitly deferred to real measurement), doesn't propose any DB schema — the
read-log/calibration-note could be as simple as fields on the existing `verse_lexical_note`/
`passage`-successor tables once #737's schema-location question is settled, or a flat file per
cluster; that's an implementation detail for whichever of #737's open items resolves first, not
designed here.
