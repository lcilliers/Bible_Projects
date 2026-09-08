# Session log — 2026-09-08

**Scope, one line:** Closed escalation #1598 (M/T-code cluster reallocation) end to end — the
untagged content-strong pool went from ~7,810–8,268 down to **0**, every M/T-code cluster got a
final sweep, two live Layer-1 mechanisms were discovered mid-session (`resolved_sense` already
retired 2026-09-07; `party_kind`/`is_negator` still live-computed from T4/T5/T7/T8/T9 membership),
a reusable candidate-generation tool was built and its real limits documented, and a governance
note was filed so Layer 2 treats T2 membership correctly. Closed out with a full cluster overview
report and all four pending config approvals applied.

---

## Escalations touched

**Completed, applied and verified live:**
- **#1598** (M/T-code cluster reallocation) — the parent thread for the whole session. Phases A
  through O applied and individually verified against the live DB after each run:
  - **A–F** (carried in from before this session's detailed transcript): T2/T3 pool triage, verb
    screening against the standing rule ("a verb only moves to T3 when not tied to a specific
    characteristic"), the faculty-ontology catalogue investigated and retired by researcher verdict
    (unrelated to cluster tagging, same escalation thread).
  - **G** (1,621 inserts) — party_kind coverage gap closed for proper nouns: 2,648 of 2,651
    untagged proper nouns had no T4/5/7/8/9-tagged sibling, meaning `party_kind` computed `NULL`
    on every live build for David, Moses, Aaron, Solomon, and a YHWH variant (`H3069`, 306
    occurrences) despite the architecture being designed to compute it deterministically.
    Classified via STEP's own TIP biographical-marker text in `strong_meaning_parsed` ("living at
    the time of..." = person, "deity" = divine, "An angel called" = angelic), not gloss keywords.
  - **H** (796 inserts) — remaining proper-noun population (places → T10, collectives → T11, a new
    **T15 Calendar** cluster for Hebrew month names, named objects → T12).
  - **I** (242 inserts) — T10's own family-expansion candidates individually gloss-checked (296
    raw, 54 excluded as coincidental `strong_related` hits or genuine ambiguity); demonyms
    redirected from their place-of-origin to T11 per the Philistine/Jew precedent.
  - **J** (186 inserts) — T8/T11 family-expansion, deduped (227 raw candidates overlapped both
    buckets); resolved 33 Matthew-1-genealogy names with no lexicon row via `verse_lexical.surface`
    instead of leaving them unclassified.
  - **K** (60 inserts) — all remaining verbs (`morph_code` V/HV/AV) → T3.
  - **L** (78 inserts) — body-part gloss scan, 72 → T14, 6 redirected off coincidental hits.
  - **M** (517 inserts) — natural-world (→T13) and object (→T12) gloss scans, run together (2
    codes hit both vocabularies, resolved to the specific sense present).
  - **N** (17 inserts) — direct gloss-to-M-code-description matching over the adjective remainder;
    low yield (17/630) confirmed the residual is genuinely non-thematic, not under-mined.
  - **O** (4,294 inserts) — final sweep, researcher decision: route the genuine non-thematic
    residual into the existing **T2** bucket rather than invent a new catch-all code.
  - Untagged pool: 0. Full counts in `iba/docs/1598-cluster-overview-report-v1-20260908.md`.
- **#1601, #1603** — 2 self-correctable `Config-Maintenance.ps1` call-shape mistakes (wrong
  `cfg_utility` column names; a title over the 60-char limit), both caught immediately, fixed on
  the next attempt, closed same-turn.
- **#1599, #1600, #1602, #1604** — the 4 config proposals raised over the session (register
  `apply_1598_phase_a_reallocation_v1_20260908.py`, `apply_1598_cluster_batch.py`,
  `clusterfamilyscan.py`; add `cfg_method_rule` `t2-supplementary-not-blanket-irrelevant` for
  `lexical.enrich`). All approved by the researcher this session, applied (re-ran
  `configmaint.propose` with each `-RunId`), verified live, and closed (`-NeedsFollowup 0`).

**Reassigned to the researcher, awaiting their decision (not blocking, not this session's to
resolve):**
- **#1533** — dangling-FK repair plan filed; the researcher's own call is 22 orphaned
  `wa_prose_section_citations` rows (drop vs. check backups first).
- **#1591** — attempted to independently reproduce the 192-row alignment-defect set to propose a
  repair; none of the reproduction heuristics tried matched the population the researcher already
  confirmed by hand. Needs the original row-list/query or a steer on detection criteria.

**Still open, not touched this session (out of scope):**
- `H5799` (Azazel) — STEP's own TIP text calls it "A male deity/angel," a genuine T7/T9 type
  ambiguity, deferred to the researcher, not decided.
- 233 strongs (a subset of Phase O's T2 population) have no `strong_meaning_parsed` row at all —
  structurally homed now, but a STEP backfill decision is open if richer classification is ever
  wanted.

## Files created or changed

- `iba/app/lib/clusterfamilyscan.py` (new) — candidate-generation via `strong_related`, proper-noun
  filtered. Validated: reliable for place/party/collective candidates (T10's Phase I batch, 82%
  genuine hit rate), unreliable for M-code thematic fit (M08 sample: ~10-15% genuine) — documented
  in the module's own docstring so the scope limit isn't rediscovered the hard way next time.
- `iba/app/migration/apply_1598_cluster_batch.py` (new) — the reusable, parameter-driven runner
  behind every Phase A–O batch (`new_clusters`/`inserts`/`relocations`/`removals`, idempotent).
- `iba/app/migration/apply_1598_phase_a_reallocation_v1_20260908.py` (new) — the Phase A one-off.
- `iba/docs/1598-*.json` (Phases A–O payloads, ~25 files) and `1598-phase-d-faculties-provenance`,
  `1598-phase-e-final-sweep-tracker`, `1598-phase-g-party-gap-classification`,
  `1598-cluster-reallocation-scope-and-method` (the method/tracking docs written alongside).
- `iba/docs/1598-cluster-overview-report-v1-20260908.md` (new) — full cluster overview: every
  M-code + T-code with member and unique-verse counts, coverage stats, the method-arc summary, open
  items.
- `iba/docs/1592-1595-window1-cross-pipeline-methodical-analysis-v1-20260908.md` — §5.2 (Faculty
  domain) marked RETIRED, cross-referenced to the Phase D provenance doc.
- `iba/app/db/iba.db` — `cluster_strong` grew by ~7,800 live rows across Phases G–O; 3 new clusters
  created (T15 Calendar; T10/T11/T12/T13/T14 already existed from earlier session work, not new
  here); `cfg_utility` gained 3 rows; `cfg_method_rule` gained 1 row (`lexical.enrich`,
  `t2-supplementary-not-blanket-irrelevant`).
- `outputs/configs/CONFIG-REPORT*.md`, `outputs/escalation/escalation-list*.md` — auto-regenerated
  by every `configmaint.propose` apply and `Escalation.ps1` write this session (routine, not
  hand-edited).

## Decisions made

**Researcher's own decisions (not self-correctable):**
- Confirmed the untagged-pool coverage check (verse-level: 26,726 of 26,727 verses containing an
  untagged word already have another word the cluster model touches) as reassuring, then
  immediately caught that it didn't address the T-code party/negator mechanism at all — pushed
  back on my first pass, which was correct and reframed the whole second half of the escalation.
- **"proceed methodically until all the unclassified strongs all have a home in clusters"** — the
  standing mandate for Phases G onward.
- Accepted the pivot from M-code family-expansion (too noisy) to T-code structural homes (verbs →
  T3, body-parts/nature/objects → T14/T13/T12) once the M08 sample showed the real hit rate.
- **"I will accept 2... make a big note for layer 2 to intelligently look at setting T2 aside, a
  T2 that gets meaning in context need attention"** — directly produced the `cfg_method_rule` filed
  as #1604.
- **"proceed to T2"** — closed the final generic-vocabulary residual into the existing T2 bucket
  rather than a new catch-all code.
- Approved all four pending config proposals (#1599/#1600/#1602/#1604) this session.

**Claude's own self-correctable fixes:**
- 2 `Config-Maintenance.ps1` call-shape mistakes (#1601, #1603), both caught and fixed same-turn.
- Mid-batch corrections caught before finalizing, not after: `H5522` "male deity" swept in on the
  bare word "male," fixed by keying on "deity" directly (surfaced 26 previously-hidden pagan-deity
  entries); `H8640` "Cushite king" missed by an early demonym whitelist, fixed by switching to the
  biographical-marker signal, which also caught a source-data typo ("A piest living...").
- Two genuine misclassifications caught mid-review in the T10/T12/T13 gloss scans (a "spear"
  riding a coincidental root-share with "camp"; three "Field of Blood" place-compounds riding
  "blood") — corrected before the batch was finalized, not after.

## Open items carried into next session

1. **#1533, #1591** — both reassigned to the researcher this session with a concrete ask each
   (a data-loss judgment call; a defect-set reproduction gap). Neither is Claude's to progress
   further until answered.
2. **`H5799` (Azazel)** and **233 no-lexicon-row strongs** — both flagged in §"Still open" above,
   neither blocking, neither decided.
3. **Next session's stated direction** (researcher, this session's close): *"we will continue with
   the lexical re-alignment to fully use the work we just did"* — i.e. Window 1/Layer 2's own
   consumption of the now-complete cluster scaffold (`party_kind`/`is_negator`/T2-relevance) is the
   explicit next thread, not a new cluster-tagging pass.

## Git state

- Branch: `main`, up to date with `origin/main`.
- Commit: `2379ef2462fbd3125da10a1367b661d5d7c12186`, 2026-09-08T14:58:12+01:00, "session 20260908:
  escalation #1598 closed -- M/T-code untagged pool 0 (was ~7,810-8,268)" — 44 files changed.
- Pushed: confirmed (`569f58b7..2379ef24 main -> main`).
- `git status` after push: `nothing to commit, working tree clean`.
