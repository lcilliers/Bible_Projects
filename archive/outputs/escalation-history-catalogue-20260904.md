# Escalation history records inserted 2026-09-03, related to "catalogue"

> Extracted from `iba.db`'s `escalation_history` table. Filter: effective insert timestamp
> (`COALESCE(raised_at, answered_at)`) falls on 2026-09-03 (the day before today, 2026-09-04),
> AND at least one of `short_description` / `context` / `comment` / `tried` / `resolution`
> contains the case-insensitive substring "catalogue". 15 rows matched, listed chronologically.
> Two are folder-path matches only (`Workflow/Catalogue/...`, the project's observation-question-
> catalogue extracts folder) rather than substantive catalogue-content discussion — flagged inline
> where that's the case; everything else is substantively about the catalogue (wa_obs_question_catalogue
> / tier-catalogue work).

---

## #1377 v22 — 2026-09-03T04:08:00Z
state: completed · next_action: approved · assigned_to: Claude · originator: Claude

File rename per governance (escalation-tied working files carry their escalation-id prefix,
researcher instruction 2026-09-03). Current filenames listed (1377-vocabulary-glossary-seed-v1/v2,
1377-vocabulary-mechanism-design-v1, 1377-glossary-mechanism-design-v1, etc.). **Also fixed the
live `cfg_column.use` text (`bible_research.wa_obs_question_catalogue`) that had baked in a
since-renamed path.**

---

## #1007 v22 — 2026-09-03T04:08:13Z
state: closed · next_action: review · assigned_to: Researcher · originator: Claude

File rename per governance, same trigger as #1377 v22. Current filenames: 1007-tier-catalogue-scope-focus-v1/v2
(archived), -v3, 1007-tier-catalogue-iba-raw-data-mapping-v1 (archived)/v2, 1007-word-term-lexical-source-v1,
1007-tier-catalogue-word-term-lexical-v1, 1007-tier-catalogue-word-term-lexical-reclassification-review-v1.
**Also fixed 2 live `cfg_column.use` rows (`bible_research.wa_obs_question_catalogue.scope` and
`.source`) that had baked in since-renamed paths** from the 2026-08-31 `configmaint.propose` run
(that run's own audit-log row in `cfg_change_detail` left untouched — accurate record of what was
actually applied at the time).

---

## #1375 v6 — 2026-09-03T07:31:22Z
state: in-progress · next_action: review · assigned_to: Claude · originator: Claude

"Re-validated live per your ask: `cfg_column.use` for (bible_research, wa_obs_question_catalogue,
scope) still holds the Scope-focus classification text exactly as approved and applied. No drift,
nothing further for me to do here — over to you for final close."

---

## #1427 v1 — 2026-09-03T07:36:31Z
state: raised · next_action: review · assigned_to: Researcher · originator: Claude · type: issue

**"cfg\_\* is structurally coherent, but has findings needing your judgement"** — a `configmaint`
coherence-check report (full report: `outputs\configs\CONFIG-REPORT-v371-20260903.md`). Catalogue
appears within its findings, not as the report's own subject: escalation-tied files not carrying
their escalation-id prefix included several `Workflow/Catalogue/...` and catalogue-named docs
(e.g. `1376-characteristic-tables-cross-db-inventory-v2-20260901.md` header naming #1007). Headline
tally: 1 orphan config, 2 settings needing justification, 1 stale-doc finding, 5 unregistered
project scripts, 1 zero-usage utility module, 1 hand-rolled versioning script, 1 PS-worksheet drift
finding, **41 behaviour rules not mechanically enforced**, 1 PS script bypassing `run.py`, 27
escalation-tied files without their id prefix, 3 config rows with unresolved hedge phrases.

---

## #1375 v8 — 2026-09-03T07:48:29Z
state: re-assigned · next_action: ready_for_approval · assigned_to: Researcher · originator: Claude

Resolution: "Re-validated live per your ask: `cfg_column.use` for (bible_research,
wa_obs_question_catalogue, scope) still holds the Scope-focus classification text exactly as
approved and applied. No drift. Nothing further outstanding."

---

## #1383 v8 — 2026-09-03T09:45:31Z
state: re-assigned · next_action: ready_for_approval · assigned_to: Researcher · originator: Claude

*(Match is a folder-path mention only — `Workflow/Catalogue/1383-verse-lexical-window1-validation-applied-v1-20260903.md`
— not catalogue-content discussion.)* Test run complete: John 1:1-5 + Gal 5:16-17 added; full run
filed with all 5 passages (19 verses), checklist applied per verse. Real findings: a second
confirmed Hebrew narrative chain (Exod 14:31); the chain test's blind spot at genre pivots (Exod
15:1/15:2); 6 confirming cross-verse pronoun/entity resolution instances; 2 Greek idioms found
(Gal 5:16 ou-mē, Gal 5:17 ho-ean); a recurring verse-level rhetorical-structure gap with no
checklist slot (confirmed in 3/5 passages) → spun off as #1443; 5 more live H0853 role-bug
instances. Also separately escalated (not worked around silently): #1441 (824 verses' worth of
verse_lexical rows pointing at soft-deleted spans).

---

## #1443 v1 — 2026-09-03T10:37:17Z
state: raised · next_action: review · assigned_to: Researcher · originator: Claude · type: issue

**"Recurring verse-structure finding has no checklist slot."** *(Match is a folder-path mention —
`Workflow/Catalogue/1383-verse-lexical-window1-validation-applied-v1-20260903.md`.)* Found in 3+
of 5 passages: Deut 6:7's four-infinitive merism, Prov 3:5-6's antithetic parallelism, Gal 5:17's
chiasm, John 1:4's life/light paired image. None of the checklist's current per-code items has a
slot for a verse-level rhetorical-structure fact spanning multiple codes/positions. Needs a
decision: new checklist item, out of Window-1 scope, or something else.

---

## #1383 v12 — 2026-09-03T11:47:48Z
state: re-assigned · next_action: ready_for_approval · assigned_to: Researcher · originator: Claude

**Measured the enriched Window-1 design against the observation-question catalogue**
(`wa_obs_question_catalogue`, 239 active rows). Filed:
`iba/docs/1383-verse-lexical-window1-catalogue-question-coverage-v1-20260903.md`. Every one of 22
questions (Word/term-lexical + The verse scopes) checked. Headline: most catalogue questions ask
about a characteristic's whole vocabulary arc across every verse and both Testaments — a different
grain than Window 1's single-verse scope. Results: 9 answerable via an aggregation/rollup layer
Window 1's design already supports; 1 answered directly today (T7.2.2, genre); 1 partial (T7.2.1);
3 have an existing owner elsewhere (glossary work / base lexicon); **4 real gaps with no current
owner**: T7.2.3 (argument/premise-conclusion structure), T7.2.4 (contextual setting), T7.1.4
(disposition-vs-act distinctions), T7.1.5 (structural-opposite/antonym terms); 2 correctly out of
Window-1's grain (T7.2.5/6). 3 open items for the researcher.

---

## #1383 v13 — 2026-09-03T12:11:31Z
state: re-assigned · next_action: ready_for_approval · assigned_to: Researcher · originator: Claude

Added the remaining questions to the same coverage document — **all 181 active catalogue rows now
covered** (corrected live count: 181, not 126; a separate 58 rows are active but soft-deleted, not
counted). Biggest new finding: 26 of the remaining 159 (T2.1.1/T2.7.1/T2.9.1/T2.10.1 + all 22
T3.1.1-T3.11.2 faculty-engagement pairs) ask about a controlled list with **no structured field
anywhere in the live pipeline**; `bible_research.db.lemma_faculty_map` is the wrong grain and
itself uncontrolled free text (36 distinct values, no enum, 815/1717 empty). Good news: ~9
Verse-context questions already answerable today via Window 2's existing
operation/operation_party schema. Fixed own transcription error (T2.7.1/T2.10.1 dual-scope
listing, corrected to The HIB only). Revised tally: ~15 aggregation-answerable, ~9 answerable
today, ~30 real unowned gaps, remainder out of single-verse grain.

---

## #1383 v14 — 2026-09-03T12:18:09Z
state: re-assigned · next_action: ready_for_approval · assigned_to: Researcher · originator: Claude

Applied the researcher's correction on T0.1.1 (God-mention/attribution is directly derivable from
lexical data via a small divine-name code lexicon + Window 1's existing entity-linking — doesn't
need to wait on Window 2's manual `operation_party.kind`). Same correction applied to
T4.1.1/T4.2.1, and partially to T4.3.1/T4.4.1/T4.6.1 (needs a slightly larger human/angelic-party
lexicon, not yet built). Revised counts: **~20 answerable via Window-1-alone mechanical
aggregation** (up from ~15). Document updated in place:
`iba/docs/1383-verse-lexical-window1-catalogue-question-coverage-v1-20260903.md`.

---

## #1383 v15 — 2026-09-03T12:35:48Z
state: re-assigned · next_action: ready_for_approval · assigned_to: Researcher · originator: Claude

Applied the researcher's T0.2.1 ruling systematically across the whole catalogue (new section 7).
Criterion: only a small % of verses directly state something on point; the real answer comes from
observing behaviour across multiple/all related verses — not derivable at Level 1 or Level 2 (both
single-verse grain). Re-split every question previously parked as "out of grain": mechanical
rollup vs genuine behaviour-pattern judgement. Result: **~85 of the 181 active questions are
T0.2.1-class** — the single largest bucket in the catalogue. ~7 hybrids caught and split
(T0.1.2/T4.6.2/T4.6.3, T6.1.1 vs T6.1.2). New open item filed for a not-yet-designed Level 3
characteristic-synthesis stage.

---

## #1383 v16 — 2026-09-03T13:42:39Z
state: re-assigned · next_action: ready_for_approval · assigned_to: Researcher · originator: Claude

Filed the full IB-analytical-cycle blueprint requested: `iba/docs/1383-ib-analytical-cycle-status-and-blueprint-v1-20260903.md`.
Restates **the catalogue's real role (areas-to-cover measure, not a per-characteristic grid)** per
the reset precedent. Stage-by-stage status table ties every stage to its owning document/
escalation. 4 open items filed, including whether this exceeds #1383's original Window-1 scope.

---

## #1383 v18 — 2026-09-03T14:49:02Z
state: re-assigned · next_action: ready_for_approval · assigned_to: Researcher · originator: Claude

Worked through the researcher's A1-A6 answers and applied them to the actual design documents. A6:
own false alarm corrected (resolved_sense narrowing verified genuine at 551,797-row scale). Real
surface/grain/sense rules found live in `bible_research.db`'s glossary. A1: full checklist-item-to-
schema mapping done; found a real gap ("verb triggered-by/impacts" has no clean single home). 3
mechanical-layer proofs promoted into real `verse_lexical` columns. A3: FK link to
phenomenon/operation deferred. A4: #1443 resolved (split into Stage-1 DETECT vs Stage-2
INTERPRET). **C.12 (the field-by-field catalogue mapping) starting as its own document.**

---

## #1383 v19 — 2026-09-03T14:51:08Z
state: re-assigned · next_action: ready_for_approval · assigned_to: Researcher · originator: Claude

**C.12 done**: `iba/docs/1383-verse-lexical-stage1-catalogue-field-mapping-v1-20260903.md` — every
Stage-1-answerable catalogue question mapped to its exact field/derivation. Found: `party_kind`
added to `verse_lexical` schema (4 catalogue questions share one join mechanism); 3 lexicons
confirmed needed this increment (connective-type prototyped, divine-name verified, human/angelic-
name designed not built); one place the earlier coverage claim was too strong (T6.4.1/T6.1.1 need
Stage 2's own characteristic-linkage). Open question for the researcher: should this mapping be
written into `wa_obs_question_catalogue`'s own `review_note` field per question_code (a real
content patch via `scripts/apply_session_patch.py`), or is the document itself sufficient?

---

## #1383 v21 — 2026-09-03T15:04:33Z
state: re-assigned · next_action: ready_for_approval · assigned_to: Researcher · originator: Claude

**Catalogue authority confirmed and recorded.** Filed:
`iba/docs/1383-catalogue-finishing-and-config-not-code-audit-v1-20260903.md` — checked
`obs_catalogue.update` (cataloguewrite.py, #1007) live before planning: it's a real,
already-registered UPDATE-by-obs_id tool, usable directly for wording fixes; no INSERT path, and
the session wasn't in Developer Mode, so 4 real question-splits (T0.1.2, T4.6.2, T4.6.3;
T6.1.1/T6.1.2 turned out to be un-pairing only) are specified as build items, not attempted blind.
Own drift-mitigation script's hardcoded lexicons corrected to design as one new table
(`cfg_lexical_code_class`), not code constants. Status table: negator/connective/divine-name
seeded and verified live; human-name/angelic-name not built (blocks T4.3.1/T4.4.1/T4.6.1,
T4.6.2/T4.6.3). Glossary gap list filed. Waiting on researcher confirmation of split wording
before applying via `obs_catalogue.update`.

---

## Summary

| Escalation | Rows this date | Core subject |
|---|---|---|
| #1377 | 1 | Vocabulary/glossary file rename; incidental catalogue column fix |
| #1007 | 1 | Tier-catalogue file renames + `wa_obs_question_catalogue` column fixes |
| #1375 | 2 | `wa_obs_question_catalogue.scope` column-text validation |
| #1427 | 1 | cfg_* coherence report (catalogue mentioned within findings) |
| #1383 | 9 | Verse-lexical Window 1 design — catalogue-question coverage mapping is the dominant thread this date (v12-v21) |
| #1443 | 1 | Spun off from #1383's catalogue-coverage work — verse-structure checklist gap |

**14 of 15 rows are substantively about the observation-question catalogue** (`wa_obs_question_catalogue`,
tier-catalogue restructuring, or the catalogue-question-coverage mapping exercise); 2 rows (#1383
v8, #1443 v1) matched only via the `Workflow/Catalogue/` folder path in a filename, not catalogue
content itself.
