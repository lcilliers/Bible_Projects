# Session log — 2026-09-07 (afternoon/evening session)

**Scope, one line:** Built `lexical.run` (the cluster/strong/word/verse-list front door for Window 1,
replacing the stale book/range model), folded an LLM-calling routine into its Layer 2 path, ran it
for real against cluster M10c, then — at the researcher's direction — turned to a genuine, evidence-
grounded validation of Layer 1's own mechanical columns (`party_kind`, `role`, `gloss_consistent_in_
verse`, `surface`). That validation surfaced real, concrete defects in columns previously assumed
sound. The researcher closed the session at that point, naming this a recurring pattern over the
past months and stating the month-long lexical line of work has not produced value — logged
honestly below, not smoothed over.

---

## Escalations touched

**Completed, applied and verified live:**
- **#1549** (Reopen build lexical.notes) — the parent thread for all of today's build work. `lexical.
  run` built, config applied, tested live on real clusters (M67, M10c). `lexical.notes`'s role was
  folded into `lexical.run`'s own Layer 2 path (auto-LLM by default, `-SuppressNotes`/`-NoAutoLLM`
  opt-outs) per direct researcher instruction. Completed.
- **#1554–#1559** — the `lexical.run` config batch (step, 2 write grants, cap setting, `cfg_utility`
  registration). All approved and applied.
- **#1563/#1564** — notes-output-pattern setting + `cfg_step.does` update reflecting the folded-in
  notes behaviour. Approved and applied.
- **#1565** — `lexical` added as a valid `cfg_setting.module` value. Approved and applied.
- **#1576–#1586** — the Layer-2-LLM config batch (model, API URL/version, token ratio, output cap,
  input/output rates, `lexical.llm_max_cost_per_batch` cost cap, usage-log path, `cfg_utility`
  registration for `lexicalenrichgenerate.py`, `cfg_step.does` update). All approved and applied.
- **#1550, #1553, #1557, #1561, #1562, #1566–#1574, #1587** — 21 self-correctable items, all closed.
  Mostly my own `Config-Maintenance.ps1` call-shape mistakes (PowerShell quoting, a title over the
  60-char limit, a `cfg_utility.module` uniqueness collision) caught immediately by the coherence
  check, no partial writes in any case; two (#1561/#1562) were deliberate live tests of the cap and
  bare-strong-code guards firing exactly as designed, not bugs.
- **#1551/#1552** — the original (Book/Range-scoped) `lexical.notes` config proposal, superseded
  before approval once the researcher corrected the input model mid-session.

**Genuinely resolved but flagged as a routing mistake worth naming:** none this session beyond what's
in BUILD.md's own entries — the `#1554`→`completed` self-correction from an omitted `-State` flag
(covered in-turn, not carried forward as an open item).

**Still open, carried into next session:**
- **#1560** — 3 `cluster_strong` rows (T7/T8) carry a bare strong code that can never match a real
  verse; needs the researcher's call on which suffixed variant(s) each should map to.
- **#1575** — `resolved_sense` root-cause diagnosed, then removed corpus-wide (`resolve_code()` no
  longer writes it at all, for any code) per direct researcher instruction this session. **Applied,
  verified live (0/544,572 rows non-null), but not yet formally approved/closed** — `ready_for_
  approval`, assigned to Researcher.
- **#1588** — corrects my own earlier `cfg_utility.module` naming mistake for `lexicalscope.py`
  (`verse-lexical` → `lexicalscope`, matching every other file's own convention). `ready_for_
  approval`, not yet applied.
- **#1589** — 6 of 15 live `note_types` (`idiom`, `pronoun_resolution`, `noun_relational`,
  `noun_severity`, `polarity`, `compound_unit`) have zero operational definition anywhere in
  `cfg_method_rule`. Found answering the researcher's own "map the LLM brief against the catalogue"
  request; deepened by the later evidence-supply-map work into probably the highest-value gap in the
  whole note_type catalogue (`noun_relational` in particular looks like the intended evidence-
  supplier for the entire 11-faculty question family and for constitutional-location questions).
- **#1590** — Greek `role` classification bug: the live tag for the Greek article (`G3588`) is `T`,
  not `ART` (what the code actually checks for) — misclassified `content` in all 82 live occurrences.
  Two further judgment calls named (`COND`/`I` particles). Raised at session close, parked, not
  fixed — per the researcher's decision not to pursue fixes right now.
- **#1591** — `surface` has 192 of 544,572 rows (0.035%) with real word-alignment defects, not
  benign multi-word idiom translation: a misattached phrase in `Deut.7.18`, and alignment-exhaustion
  producing empty `surface` values in `1Thess.1.1`. Also inherited by the `text_reconstructed_from_
  codes` fallback built in BUILD.md #252. Raised at session close, parked, not fixed.
- **#1533** — unrelated to this session's work throughout; touched ~15 times purely to satisfy the
  automated backlog-check hook with a one-line acknowledgement each time. Still correctly on-hold
  pending #1022, untouched in substance.

## Files created or changed

- `iba/app/lib/lexicalscope.py` (new) — selector-to-verse-id resolution (`-ClusterCode`/`-Word`/
  `-StrongList`/`-VerseList` → strong-list → verse-list via `span.strong_variant`, not `strong_verse`
  — verified live that the latter undercounts).
- `iba/app/lib/lexicalenrichgenerate.py` (new) — the LLM-calling half of `lexical.run`'s Layer 2 path:
  batches by `passage.max_verses`, assembles a lean cost-estimated package per batch, calls the
  Anthropic Messages API, parses the response, writes via the existing `lexicalenrich.enrich_passage`,
  logs real usage. Config-driven from the start (unlike its own template, `narrativegenerate.py`,
  which is flagged non-compliant for hardcoded constants).
- `iba/app/handlers/lexical.py` — new `run()` (the front door), new `_notes_payload_dict`/
  `_write_notes_payload` (the former standalone `lexical.notes` step, folded in), `notes_request`
  removed.
- `iba/app/lib/lexical.py` — `resolve_code()` no longer writes `resolved_sense` at all (escalation
  #1575); `build_for_verse()`'s now-moot M-code gate left in place, not ripped out.
- `iba/app/migration/resolved_sense_removed_v1_20260907.py` (new) — one-off, re-ran the corrected
  code against the full corpus (29,754 verses, 544,572 codes, 71,949 updated).
- `iba/app/ps/VerseLexical.ps1` — minor `-Step`/help-text updates from the earlier `lexical.notes`
  pass (superseded by the fold-in, left accurate).
- `iba/app/BUILD.md` — entries #249–#254 (the full `lexical.run` build, the `resolved_sense`
  removal, the M10c production run).
- `iba/docs/1549-window1-evidence-supply-map-v1-20260907.md` (new) — the corrected, evidence-based
  map of the 131-row `wa_obs_question_catalogue` against what Layer 1/Layer 2 can actually supply,
  after the researcher corrected an earlier wrong framing (see Decisions, below).
- `iba/app/db/iba.db` — config applied (see escalations above); 71,949 `verse_lexical` rows rebuilt
  in place; backed up first (`iba.db.pre-1575-resolved-sense-removed-20260907.bak`).
- `_analytics/lexical-extracts/*` — real test-run artefacts (M10c's Layer 1 extract + notes briefing,
  two small `lexical.run` test outputs), left in place as genuine generated output, not scratch.

## Decisions made

**Researcher's own decisions (not self-correctable):**
- The old `-Book`+contiguous-range input model for `lexical.build`/`lexical.enrich` is stale;
  replaced by cluster/strong/word/verse-list selector resolution.
- Layer 2 must call an LLM as part of the routine, not stop at a briefing pack for a human to pick
  up separately — "it must be part of the routine, rather than parking it."
- `resolved_sense` serves no purpose in `verse_lexical` and should be removed entirely, corpus-wide,
  not trimmed or redesigned — direct instruction, applied and verified same session.
- Corrected a wrong framing mid-session: Window 1 does not answer characteristic-level catalogue
  questions directly — it supplies the per-verse grammatical/relational evidence Window 2 needs to
  do that synthesis. The first evidence-map (this session) was rebuilt against the real 131-row
  catalogue once this was understood.
- Corrected a second, deeper framing: identifying which *note_type* is relevant to a question is not
  the same as working out the actual *procedure* that combines Layer 1 facts into an answer — proven
  concretely on `T0.1` against a real verse (`Zech.11.6`), which also surfaced a live `polarity`
  case (a negated characteristic occurrence) confirming #1589's severity.
- Proposed and directed the "vertical" processing approach: resolve a question's whole natural
  verse-population from Layer 1's own mechanical facts first (e.g. all 8,766 `party_kind=divine`
  verses), split by co-presence of other parties, then work the question across that population —
  rather than reading verse-by-verse across many different questions.
- Directed the pivot to a full Layer 1 column validation pass ("before we can move forward, we first
  need to move backwards") after `party_kind`'s human-detection gap surfaced. Four columns validated
  this session: `is_negator` (sound), `role` (Hebrew sound, Greek has a confirmed bug), `gloss_
  consistent_in_verse` (sound but unconsumed), `surface` (mostly sound, 192 rows with real defects).
- **Closed the session**, stating the month-long lexical line of work has produced no net value and
  is not worth continuing in its current form; explicitly named this as a recurring monthly pattern,
  not a one-off reaction.

**Claude's own self-correctable fixes** (flagged as such at the time, not researcher decisions):
- 21 `Config-Maintenance.ps1` call-shape mistakes this session (listed under escalations above),
  each caught immediately by the coherence check, none causing a partial write.
- The `lexicalenrichgenerate.py` LLM-payload optimization pass (stripped `cluster`, compacted empty
  `existing_notes`, filtered `method_rules` to the relevant step, added explicit prompt boundaries,
  fixed a completeness-rule wording bug) — done in direct response to the researcher's own "did you
  optimise the payload" question, not a unilateral improvement.

## Open items carried into next session

1. **#1560, #1575, #1588, #1589, #1590, #1591** — all await the researcher's own decision or
   approval; none require Claude-side follow-through until then.
2. **The Layer 1 column validation is roughly half done** — `status`, `ambiguity_note`, `language`,
   `testament`, `narrative_morph` were not reached before the session closed.
3. **The `noun_relational`/`polarity` definitions (#1589) are now understood to be load-bearing**,
   not peripheral — the single highest-value fix identified this session, still undecided.
4. **Whether/how the lexical-verse-analysis line of work continues at all is now genuinely open** —
   the researcher's own words at close: *"there is no reason to fix the data, even if it was right,
   it is pretty useless... that is another layer of these very large reading tasks but they cannot be
   trusted... I am done."* Also, explicitly: *"I know I say every week I had enough and walk away —
   this is a pattern over the past months."* Recorded here as fact, not interpreted or minimised —
   whether this holds as a durable direction-change or is reconsidered next session is the
   researcher's own call, not something to presume either way.

## Git state

- Branch: `main`, up to date with `origin/main`.
- Commit: `619fa0ee060a7b8ba724e9adee2dc4ef49cf121e`, 2026-09-07T19:31:25+01:00, "session 20260907
  (evening): lexical.run built and run live (M10c), Layer 1 column validation pauses the
  lexical-study line" — 43 files changed.
- Pushed: confirmed (`33492f62..619fa0ee main -> main`).
- `git status` after push: `nothing to commit, working tree clean`.
