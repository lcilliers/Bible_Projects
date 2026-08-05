# Should `report.verse_span_meaning`'s output be captured in the DB, and named in the v4 instruction?

Researcher questions, 2026-08-05. Facts checked live against `iba.db` + `BUILD.md` + the v3/v4
docs; recommendation only — no schema, config, or doc change made.

## What's actually true right now

- **No table for this exists.** `iba.db`'s live table list has nothing shaped like the old
  programme's `ve_lexical`/`finding` — no per-span or per-verse T1-T5 reading is stored anywhere.
  Output is MD files only (`iba/app/verse-analysis/{Book}/*-verse-span-meaning.md`).
- **This gap is not new to v4 — it's never been closed.** Even the older, now-superseded
  three-phase method (`candidate`/`passage`) only ever tracked the *debate document's* status
  (`passage.debate_status`: `scaffold`/`filled`) in DB — never the base lexical reading's actual
  content. `BUILD.md` §53 (2026-07-30) built `passage.debate_sync` specifically to keep that status
  flag honest, and even that is a flag, not the reading itself.
- **The researcher already flagged this, in writing, twice.** v3 and v4's own `_meta.status`
  both say: `"test-draft, not written to DB (destination tables not yet defined per researcher
  Q7)"`. The 2026-08-03 Obadiah session log confirms Q7 was answered live that day: destination
  tables were considered and deliberately left undefined, not overlooked.
- **v4 already states the DB-search goal, unmet.** v4 line 14: this instruction exists partly "to
  allow matching and searching on verse contents in the DB via the verse lexical." An MD-only
  output cannot do that — nothing is queryable.
- **v4 names the raw tables but not the mechanism.** v4's "Input this technique assumes" section
  lists the 12 raw tables and says meaning is "extracted by analysing the parsed tables" — but
  doesn't name `report.verse_span_meaning` / `lib/versespanmeaningreport.py:meaning_for_code` as
  *the* registered mechanism that does this (with its exact-variant → base-fallback →
  ambiguity-check → STEP-live-resolve logic from the last exchange). Right now that's implicit
  knowledge, not a stated step.

## a) Should the output be captured in the DB?

**Yes — recommend it, but scope it to the T1-T5 reading only, and only once that shape is
settled.** Reasons:

- It's the base evidence every later step (T6-T9 stamps, and whatever movement-analysis layer
  comes after) depends on. Right now nothing stops it being silently re-derived differently on a
  later pass — no persisted row to check a new pass against, no way to detect drift between two
  readings of the same verse. That's a structural gap of exactly the kind the closure diagnosis
  named ("looks promising, then drifts away... cannot handle the complexities").
- v4's own "Self checking" section already assumes a check *against something* — right now that
  something is only the same chat's own working memory, not a durable record.
- **Caution, not a reason to skip it:** don't design the table before T1-T5's field shape is
  actually settled in v4 (still draft). Building schema ahead of a stabilized method is exactly the
  failure mode named elsewhere in this project's history (dropped D10/D12/D13, retired
  `session_d_*`, retired C-code scaffolding) — throwaway tables from designing too early. The v4
  JSON sample already sketches the shape (`t1_t5.reading`, `t1_t5.flags[]` per verse) — that's the
  right starting point once v4's T1-T5 section itself stops changing.

## b) Should this be fundamentally part of the verse-lexical instruction?

**Yes — name it as an explicit precursor step, not an implicit assumption.** Concretely: v4 should
state, as its own numbered step (a "Step 0" before T1), that the per-span meaning table is produced
by running `report.verse_span_meaning` (or whatever supersedes it) over the passage first, and that
T1 reads *that* output — not that T1 silently assumes some unnamed derivation happened. This
matches the project's own standing rule (`governance.rules_must_be_config_driven` /
`governance.past_precedent_investigation_signals_missing_config`, both from this same app's
history): a process rule this central shouldn't live only as an implicit assumption in prose.

## What I have not done

No DB schema, no config row, no edit to v4 itself — this is a judgement call on study
methodology and the researcher is rewriting v4 by hand in deliberately small steps. Flagging back
for a decision rather than drafting a "Step 0" or a table schema unprompted.
