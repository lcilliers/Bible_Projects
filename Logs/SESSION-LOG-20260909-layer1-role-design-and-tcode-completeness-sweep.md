# Session Log — 2026-09-09

**Scope:** Recovered from the 2026-09-08 power-outage mid-session cutoff (no data loss found);
continued escalation #1592's Layer 1 (`verse_lexical`) redesign — `role`'s real design corrected to
complete multi-cluster-code enumeration with a mandatory NULL-check; formalized a three-leg lexical
readiness validation check; built and ran a full T-code completeness sweep against the T2 pool
(escalations #1605/#1606), resolving all 37 of #1605's original T2-vs-M-code conflicts item by item
with the researcher and adding real, previously-missing members to T4/T5/T6/T7/T9/T15.

## Escalations touched

- **#1592** (re-assigned, v10 → unchanged this session) — read/cross-referenced as the source of the
  Layer 1 redesign; not itself updated this session, its content superseded/extended via #1605/#1606.
- **#1605** ("37 strongs: live T2 + live M-code, unreconciled") — raised 2026-09-08 (pre-outage),
  worked to `ready_for_approval` this session: all 37 strongs resolved item-by-item with the
  researcher (`outputs/1605-37-t2-vs-m-code-review-20260909.csv`), plus the `role` redesign
  correction (multi-valued, complete enumeration, NULL-is-an-error) and the T-code config-alignment
  proposal folded into the same escalation's context trail.
- **#1606** ("Code lexical readiness check (verse/span/strong/cluster)") — raised this session, left
  `in-progress`: the three-leg readiness check (verse-has-span / span-strong-resolves / strong-has-
  cluster) defined and quantified live; the T2→T4/T5/T6 resweep (122 candidates) and the T2 full
  sweep for T7/T9/T15 both run and recorded here; large categories (T8/T10/T11/T12/T13/T14)
  deliberately not swept, redirected per researcher instruction (see Decisions).

## Files created or changed

- `iba/docs/1605-tcode-classification-config-alignment-proposal-v1-20260909.md` — new, built and
  revised in place across the session (review-mode convention, no version bumps) — the consolidated
  NEW/CHANGES/STAYS/RETIRE/open-decisions record for every config row and column touching T-code
  classification.
- `outputs/t4-t9-cluster-membership-20260909.csv` — new, full T4–T9 `cluster_strong` export (1,856
  rows at the time).
- `outputs/1605-37-t2-vs-m-code-review-20260909.csv` — new, the 37-strong review-and-decision record
  (researcher_decision/notes columns filled in via chat, applied live to the DB).
- `iba/app/db/iba.db` (`cluster_strong` table, not git-tracked) — extensive live writes, see Decisions.
- `Logs/SESSION-LOG-20260909-layer1-role-design-and-tcode-completeness-sweep.md` — this file.

## Decisions

**Researcher's own decisions (judgement calls, not self-correctable):**
1. `role`'s real design: complete, multi-valued enumeration of every cluster_code a strong carries;
   nothing dropped; a NULL-set (no cluster at all) is itself an error, not a tolerated default; T2 is
   recorded exactly like any other code, never special-cased or suppressed.
2. Multi-membership discipline: "there is no reason for multi membership... must have a really good
   reason" — corrected an initial (wrong) additive fix on `H3049` mid-session; applied as the default
   stance for the rest of the day's work (retire the superseded code, don't stack tags without cause).
3. All 37 of #1605's T2-vs-M-code strongs, decided individually across several rounds: 8 "be+action"
   verbs → T3 only; `H7293` Rahab → T11 (checked live: both occurrences use it as Egypt's byname,
   matching T11's own worked examples); 14 → M-code-only; `G1493`/`H1544` (idol/idol's-temple) → T10/
   T12 only, dropping their M55 theme tag; `G5600` → T6; remainder split M-only/T2-only. Full record
   and reasoning: the CSV above.
4. The 6 grammatically-ambiguous T2→T6 candidates from the T4/T5/T6 resweep: "these words all trigger
   that layer to must look further for any related words/activity" — added to T6 despite not being
   pure clause-linking conjunctions by strict grammar, widening T6's real scope.
5. Michael (`H4317Q`/`G3413`/`H4317M`): kept T8 *and* added T9 — "err on the side of adding it to
   angel — it allows for it to be checked out in that context" — deliberate dual-membership, the
   Bible using the same Strong's code for both ordinary human Michaels and the archangel.
6. Strategic redirect, end of session: the point of T-code completeness is not raw coverage — it's
   getting right the words whose T-code "actually triggers a special consideration... source or
   target object, or the impact of the movement." Large-category (T8/T10/T11/T12/T13/T14) keyword
   sweeping stopped on this instruction; next step is investigating `verb_argument` (the Layer 2
   mechanism meant to consume exactly this fact) rather than continuing blind completeness sweeps.

**Self-correctable fixes Claude made and closed directly (design already established, execution
only):**
- `H3049` → T4 (spiritist, found via manual T4-review, matching an already-approved pattern).
- T2→T4/T5/T6 resweep (122 candidates, morph-filtered, evidence-checked individually against each
  code's own live definition) — mechanical application of an already-agreed method.
- T15 (Ethanim), T9 (cherub/Seraph/archangel/isangelos), T7 (Almighty/Most High/El Most High) — same
  shape, direct gloss-to-definition matches, no design ambiguity.

## Open items carried into next session

- **`verb_argument`** (Layer 2 `note_type`) — investigate its actual functioning as the next step,
  as part of the column-by-column Layer 1/2 review (deferred until #1605's role redesign settled).
- **§5.0 of the config-alignment proposal** — the coexistence-scope question from earlier in the
  session is effectively superseded by the multi-membership-needs-a-reason principle and the 37-item
  resolution, but was never explicitly closed as such — worth a final confirming pass.
- **`H7451H`/`H7307G`** (evil/spirit, co-occurring in Judg.9.23) — found during the T4 review, never
  given an explicit T4 decision the way `H3049` got. Still open.
- **`H0061`** — applied M03-only per instruction, but confirmed highly polysemous (Alas/No/Well/But/
  Nevertheless across occurrences) — M03 fits only the "Alas" sense; may need a context-dependent
  mechanism once Layer 2's pairing design is built, not a single static M-code.
- **`G1415`/`H7218K`** — resolved (M23/M24 only respectively) but the researcher flagged both as
  still owing a real verse-context check ("will force context read") not yet performed.
- **Large T-code categories (T8/T10/T11/T12/T13/T14)** — not swept for T2-pool completeness this
  session; deliberately deferred pending the `verb_argument` investigation, per the strategic
  redirect above.
- **The per-column Layer 1/2 validation** (the six-point template: definition/source/soundness/
  config-currency/recorded-value/Layer-2-consumption) — still not started; explicitly sequenced to
  follow #1605/#1606 and now the `verb_argument` investigation.
- **Escalation #1606** — left `in-progress`, not closed: the readiness-check `cfg_method_rule` and
  its runnable, persisted check (per `governance.reports_must_persist`) are still not built, only
  scoped and quantified.

## Git state

