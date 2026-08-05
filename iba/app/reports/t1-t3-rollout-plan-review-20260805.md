# Reviewing the a-e rollout plan against today's findings

Researcher's proposed steps, annotated — not a rewrite, flags only.

## a) Define and create schema

Split this into two moments, not one: **spec the field shape first, against real messy verses**,
*then* cut DDL. Today's Dan 8:1 illustration only worked because it was checked against actual data
(the Niphal-participle case, the article+noun case) — a schema designed on paper first, without
that check, risks the exact trap this whole redesign exists to fix (§ the D10/D12/D13,
`session_d_*`, C-code precedent — schema built ahead of a settled method, then abandoned). Concretely:
spec the fields against a handful of deliberately hard verses (Dan 8 has multi-stem verbs, Jonah 3
has dense 3-4-code compounds, 2Cor 6:6 has a content-empty function-word component) *before*
writing `CREATE TABLE`.

Also a process fact, not a preference: this app's schema is itself config-governed
(`cfg_table`/`cfg_column`), and every past schema addition (`passage.verse_span_meaning_path` etc.)
went through `configmaint.propose` → approve → apply, not a raw migration script. Same path applies
here.

## b) Adjust the script, target the DB

Worth deciding explicitly, not by default: does the MD file stay as a *generated view* off the new
DB table (DB is the source of truth, MD is a render), or do both get written independently? Two
independently-written representations of the same reading is itself a disconnected-parts risk —
the same shape of problem as everything found today, just one level up. Recommend DB as sole source
of truth, MD regenerated from it.

## c) Run a test

Pick the test range for its difficulty, not its convenience — Dan 8 (multi-stem verbs, several
4-code compounds) or Jonah 3 (near-every-span compound, Hebrew construct chains) exercise the actual
fix; a simple low-compound passage would pass without proving anything (structural pass ≠ value
quality — same standing distinction as everywhere else in this project).

## d) Backfill already-completed books

One open question worth deciding, not defaulting past: the existing **filled** `passage_debate`
documents (Hosea, Daniel, Obadiah, Jonah, Joel, Micah — the "most complete body of work" per the
closing log) were built on the *old*, incomplete extract. Backfilling the extract underneath them
doesn't automatically mean those debates were wrong — but it does mean their raw material has
changed. Worth an explicit decision: are those debates re-checked against the fixed extract, or
left as historical/out of scope? Either is defensible; leaving it undecided by default isn't.

## e) Run across all books

This step is bigger than it looks, and worth sizing before committing to it as one action.
Measured earlier this session: `strong`-table coverage is ~90-100% through most of the OT but
**24.8% in Matthew** — running the fixed script "across all books" means the auto-backfill path
(`raw.backfill_meaning_for`) firing live STEP calls for tens of thousands of previously-unregistered
Greek codes, not just re-rendering existing data. That's a materially larger, slower, STEP-load-
heavier operation than a)-d) combined, and fits the project's own standing rule on API work: bounded
batches with a checkpoint, not a full-corpus push in one call. Recommend staging this by book or
by testament, not as a single "run it all" step.
