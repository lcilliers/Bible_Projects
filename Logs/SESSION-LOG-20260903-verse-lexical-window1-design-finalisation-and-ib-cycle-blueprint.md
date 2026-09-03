# Session log — 2026-09-03 (session 3) — verse-lexical Window 1 design finalisation + the IB analytical cycle blueprint

## Scope, one line

Corrected and finished the Window 1 (Stage 1, lexical) design/propose document through direct
researcher review (objective, methodology, schema, passage determination, catalogue configuration),
ran a real validation pass on 5 passages, built and proved a drift-mitigation method, checked the
design against Window 2's live schema and the full observation-question catalogue, and — at the
researcher's explicit request — wrote a full-cycle blueprint (every stage, Base substrate through
Publishing) that now anchors the study going forward. Three unrelated cfg_behaviour_rule cleanups
closed at the start of the session (carried over from the previous session's open judgement calls).

## Escalations touched, by id, with outcome

- **#1437** `never-write-via-adhoc-tool` rule removal — **completed**. Researcher decision
  (verbatim: "remove this rule, I will recreate it when the issue re-appears"), applied via
  Config-Maintenance.ps1 propose/apply, verified live.
- **#1438** `writes-must-be-replayable` rule removal — **completed**, same shape, same researcher
  session.
- **#1439** self-correctable crash (Config-Maintenance `-Title` over the 60-char limit) —
  **completed**, resolved directly, no researcher input needed (my own input error).
- **#1440** `consolidation-doc-must-be-load-bearing-or-retired` rule removal — **completed**, same
  shape as #1437/#1438.
- **#1441** `verse_lexical` FK orphan (824 verses point at soft-deleted `span` rows, found live
  pulling John 1:5's data) — **raised, still open**. Root-fix scope (repoint by position vs.
  re-run `lexical.build`) not yet decided — Group B, deferred by researcher instruction until
  Group A (the build-blocking items) closed.
- **#1442** same-root verb/noun pair sharing one English gloss (`epithumeō`/`epithumia`, Gal
  5:16-17) — **raised, still open**. Deferred with #1441 (Group B).
- **#1443** recurring verse-structure finding with no checklist slot (merism/chiasm/parallelism) —
  **raised, then a proposed resolution filed**: split into Stage-1-detect (new `structural_pattern`
  note_type, in the schema now) vs. Stage-2-interpret (parked). `ready_for_approval`, awaiting
  researcher confirmation to close.
- **#1383** "Approve verse-lexical Window 1 enrichment design/propose" — the main thread, **v1
  through v21 today**, still open, `ready_for_approval`, assigned Researcher. Carries, in full
  chronological order: the objective correction, the pre-build validation test plan, the actual
  5-passage/19-verse test run, a real self-caught drift/selective-attention correction and the
  resulting mechanical/judgement method, the check against Window 2's live schema, the full
  181-question catalogue coverage check (including the T0.2.1 behaviour-synthesis class,
  ~85 questions), the full-cycle blueprint, the confirmed build sequence, six researcher
  corrections (A1–A6) applied directly to the design doc, the passage-determination gap fix, and
  the catalogue-finishing/config-not-code specification. Not yet approved for build.

## Files created

- `Workflow/Catalogue/1383-verse-lexical-window1-validation-applied-v1-20260903.md`
- `iba/docs/1383-verse-lexical-window1-validation-test-plan-v1-20260903.md`
- `iba/docs/1383-verse-lexical-window1-validation-calibration-v1-20260903.md`
- `iba/docs/1383-verse-lexical-window1-method-and-drift-mitigation-v1-20260903.md`
- `iba/docs/1383-verse-lexical-window1-capture-design-vs-study-purpose-v1-20260903.md`
- `iba/docs/1383-verse-lexical-window1-catalogue-question-coverage-v1-20260903.md`
- `iba/docs/1383-ib-analytical-cycle-status-and-blueprint-v1-20260903.md`
- `iba/docs/1383-verse-lexical-stage1-catalogue-field-mapping-v1-20260903.md`
- `iba/docs/1383-catalogue-finishing-and-config-not-code-audit-v1-20260903.md`

## Files changed

- `.claude/commands/start-project.md` — the unenforced-config summary was still describing the
  pre-#1388 enum vocabulary; corrected to name all 7 live `behaviour_rule_enforcement_status`
  values.
- `iba/docs/1383-verse-lexical-enrichment-design-propose-v1-20260903.md` — the main design/propose
  document, revised through ~10 rounds this session: Objective rewritten (§1), schema extended
  (§5 — 3 more mechanical columns, `party_kind`, `structural_pattern`, `cfg_lexical_code_class`,
  the FK-link deferral, passage determination added as §5.4), config plan updated (§6).

## Decisions — researcher's own vs. self-correctable

**Researcher's own decisions** (recorded verbatim in the escalations, not inferred): removing
cfg_behaviour_rule ids 12/30/35; the objective in the design doc was wrong and needed re-grounding
in the full document chain; the applied-checklist document showed selective attention/"proving the
checklist" bias, not neutral evaluation — redo the method, not the passages; stop creating
fragmenting escalations, define the reusable method instead; the Movements-reset framing is still
the live hypothesis; the Level 2 two-pass split (describe, then integrate) and its input-assembly
redefinition (characteristic-composed, not passage-sequential); the confirmed build sequence
(Layer 1 → base-layer fixes → full-Bible run); all of A1–A6 and C.10–C.12 (six direct corrections
to the design, including retracting one of my own over-strong recommendations on the FK link and
splitting #1443); catalogue authority confirmed, plus the wording/split/narration-column/glossary/
config-not-code work ordered as part of finishing this build.

**Self-correctable, closed directly**: #1439's crash (my own input error); a duplicate-listing
error caught before finalizing the full-catalogue document (T2.7.1/T2.10.1 wrongly listed under two
scopes); a verse-count typo in the validation test plan; and the `resolved_sense` "major red flag" —
investigated properly at the researcher's push, found to be a false alarm caused by my own
display-truncation code all session, retracted with full live evidence (99.999% of 551,797 rows
carry genuine per-stem narrowing).

## Open items carried into the next session

1. **#1383 — not yet approved for build.** Waiting on: confirmation of the catalogue split wording
   and clarity fixes (`1383-catalogue-finishing-and-config-not-code-audit` §2–3); resolution of the
   open cross-database question from A3 (does `phenomenon`/`operation`'s eventual findings home
   belong in `iba.db` or `bible_research.db` — parked, not decided); whether the whole blueprint/
   Stage-2 material should split into its own escalation (blueprint §9/§10, item 1).
2. **Group B** (#1441, #1442) — deferred by researcher instruction, not yet picked up.
3. **#1443** — proposed resolution filed, needs a confirm-to-close.
4. **Build items now concretely scoped but not started**: `cfg_lexical_code_class` (new table);
   `party_human`/`party_angelic` lexicons (not seeded — nothing depending on them is answerable
   yet); the `H0853` role fix; the `answered_by` catalogue column (needs a new one-off migration,
   Developer Mode or explicit go-ahead); the 4 catalogue-question splits (need `cataloguewrite.py`
   extended for INSERT, or another path); the glossary entries listed in the catalogue-finishing
   document §5 (not written).
5. **Stage 2's own design cycle** (blueprint §4/§9, item 2) — relation-signal mechanics, the pointer
   mechanism, whatever schema Pass 2a/2b write to — explicitly scoped as its own later design cycle,
   not started.
6. **Start here next session**: `iba/docs/1383-ib-analytical-cycle-status-and-blueprint-v1-20260903.md`
   for the overall map, then escalation #1383's own history (v1–v21) for the detailed trail — every
   correction and its resolution is recorded there in order, not just in this chat.

## Git state

Confirmed live (not asserted) after this log was written — see the commit this session performs
immediately after, same unit of work per `governance.session_log_triggers_commit`.
