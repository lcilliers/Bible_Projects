# Session Log — 2026-09-16

**Scope:** Started via `/start-project` (spine clean, 0 FATAL; STEP up; IBA READY). Took stock of
the whole lexical-stack build against #1706 and closed **Layer 1's design completely** (three items
wrongly marked open in #1706's first draft — the `role` pre-validator, soft-delete confirmation, and
JSON internal shape — were found already answered in a Sept-9/10 document I hadn't checked closely
enough; corrected, then the one genuinely remaining item, the `role` array shape, resolved live).
Then did the **deep Layer-2 review** the researcher explicitly asked for — read every pack design
doc in full (not summaries), found and reconciled the one real unaddressed tension (#1660's "bulk
lexicon join is noise" ruling vs. stage 5's design), found two genuinely dropped items from #1607's
old Layer 2 spec (`passage_id`'s fate, the `resolution_status`/"never guess" principle), and built
the **escalation register** (#1706 §8) the researcher asked for after catching a pattern of me
closing items without checking their open sub-items — which immediately surfaced the #1660 finding
as real, not hypothetical. Continued #1704 through **Phases 2–5**: corrected the note_type
completeness count (10 undefined, not 6), built the full **per-question event crosswalk** (all 100,
then 92, live questions), and produced **design deep-dives** (framework/options/pros-cons) for the
8 remaining open elements — which the researcher then worked through directly, giving real content
decisions on all 8, including a genuine correction (spirit/soul/heart/mind is `cluster M47`, not a
missing T-code) and dropping/retiring 7 catalogue questions. Closed **#1701** (new catalogue
component `T2.11` authored), **#1694** (moot — compared against the wrong, legacy database), and
**#1705**'s aftermath is now fully reconciled into #1711. Ends with escalation-backlog cleanup
(3 more items packaged for closure) and this log, per direct researcher instruction ahead of an
expected system restart.

## 1. Escalations touched, by id, with outcome

| # | Outcome this session |
|---|---|
| **#1607** | Corrected, not just reviewed: three items wrongly marked open in #1706's first draft (`role` pre-validator design, soft-delete-vs-hard-delete, D7 `passage_id`) were found already answered — two in a 2026-09-09/10 document I hadn't read closely, one via direct researcher confirmation this session (passage dropped as a reading-unit concept entirely). Still `in-progress`, correctly so — note_type `cfg_method_rule` registrations remain the real outstanding build work. |
| **#1658** | **Resolved for this pipeline.** Researcher: the assembly script reads the three meaning tables directly, no view registration needed — `#1658`'s gap simply doesn't bite this build. Stays open as a general `cfg_table` capability question, unrelated to any live need now. |
| **#1660** | Not reopened (stays `closed`), but reconciled against stage 5's design per direct researcher instruction ("approach with new eyes, think through volume and filters"). New doc, live volume numbers: corpus-wide read = 22.5M chars (~5.6M tokens); M-code-only scope = 5.15M chars (~1.3M tookens), a 78% cut, matching an existing precedent (#1527). Reconciliation: #1660 rejected undirected bulk documentation; stage 5 is directed question-answering — different in kind, and now checked, not just asserted. |
| **#1665** | Both of its 2 orphaned `cfg_enum` groups given explicit, correct disposition: `lexical_code_class` — genuine retirement candidate (mechanism already migrated to `cluster_strong`, only the enum registration is residue). `party_kind` — NOT a retirement candidate (live, essential); its gap is a validation-wiring question, a different kind of finding. Also resolved the specific question it raised about `connective_causal`/`coordinating`/`purpose` granularity — checked live, it survived in `cluster_strong.rationale` as free text, richer than the original 3-way split. |
| **#1691** | Content has been design-complete since 2026-09-14 (its own §9/10) but was never closed like its 3 pack siblings — packaged for closure (`ready_for_approval`) as session-end housekeeping. |
| **#1694** | **Closed, moot.** Original finding (37 M-codes with no `cluster` row) compared `cluster_strong` (iba.db) against `bible_research.db.cluster` — the wrong, legacy table. Re-checked directly against `iba.db.cluster`: 0 orphaned M-codes. Confirmed by the researcher: "no longer required... based on research_db that is no longer relevant." |
| **#1695** | New directional input recorded, not yet designed: synergy's own still-undefined input JSON is now expected (researcher's own words, "probably") to be the accumulated `needs_adjacent_verse_context`/`cross_family_or_cluster_flags`/pointer observations from reading and answer, not a fresh pull. Still `in-progress`, deliberately deferred. |
| **#1696** | Migration scope corrected twice this session: first widened (98→100 rows, folding in the `pattern_type` crosswalk and the new `T2.11` questions per direct instruction not to touch `bible_research.db` further), then corrected again to **92 rows** once the researcher's Phase 5 catalogue-content review dropped/retired 8 question codes. Still `re-assigned`/`ready_for_approval`, deliberately held pending #1706. |
| **#1697** | Unchanged this session (v6, `ready_for_approval`) — reviewed, no new action needed; all 5 items already resolved 2026-09-15. |
| **#1698** | Unchanged this session (v2) — reviewed, correctly deferred until the answer stage is built and tested. |
| **#1700** | **Review complete.** T7 tier finished (19 questions, 95 sampled, zero genericity — same clean result as every other tier). Confirmed live: the catalogue has exactly 98 (now 92) rows, all inside T0–T7, no live non-tier material exists. All ~440 sampled answers across the whole catalogue: zero genericity found anywhere. |
| **#1701** | **Closed content-wise** (`ready_for_approval`). New catalogue component `T2.11` "Faculty Engagement" authored (2 questions, full field set, typo fixed) per #1704 §5 decision 4 — not written to `bible_research.db`, folded into #1696's migration insert. |
| **#1702** | Its own findings (cluster T-code mechanism status) fully absorbed into #1704 Phase 1b/1c/2/4 this session — packaged for closure as session-end housekeeping, content lives on in #1704's record. |
| **#1703** | Real progress on its own open "resolution mechanism" question: researcher confirmed (via the passage-as-unit discussion) that flagged needs are resolved in a later analytic run, expected to be synergy — promoted to a cross-cutting checklist rule (§0 rule 5a), not just noted here. Real flag rate still stands, untested. |
| **#1704** | The big one this session — Phases 2 through 5 built and then substantially corrected against researcher review: **Phase 2** (event-by-4-part-test match), **Phase 3** (corrective actions, plus a Group D correction — 10 of 15 `note_type` values lack a registered `cfg_method_rule`, not 6 as originally scoped), **Phase 4** (full per-question crosswalk, all live questions, exact mechanism not category label), **Phase 5** (design deep-dives — framework/options/pros-cons for the 8 remaining open elements). Researcher then worked through all 8 directly: approved B/C/B mechanisms for 3, retired/dropped 7 question codes across genre/typological-link/T5 reframe, and delivered one real correction (spirit/soul/heart/mind is `cluster M47`, not a missing T-code — corrected Phase 2 event 13 and Phase 4's T2.1 row). One conflict flagged back to the researcher, not resolved: the future-orientation-marker mechanism's only two consumers (T5.6, T0.4) are both dropped the same turn it was approved. |
| **#1705** | No further action this session (stays `closed`) — its aftermath (no `verb_argument` model expansion) is now fully reconciled into how #1711 and #1704's `directional-party-frame` event are actually scoped. |
| **#1706** | Extensively rewritten across the whole session — the master living register. §1 corrected for real build/design status per stage; §2/§3/§4/§4A rebuilt from a full re-read of every pack design doc; new **§8 escalation register** (39 rows, every one re-checked against live content, not assumed clean from `state='completed'`); #1660 reconciliation folded in; D7/`resolution_status` findings and fixes; #1658/#1665/#1694 dispositions; the full catalogue-content-decision fallout (92-row count, `T2.1`/M47 correction, `T7.1.3` expansion). Still `in-progress`, correctly so — the pack sign-off nod and #1711's own design remain the two live action items. |
| **#1711** | Real grounding assembled and then substantially advanced: §4A's three concrete open items (stage name, scope grain, catalogue linkage), the #1660 volume reconciliation, the D7/`resolution_status` findings, the "read all three sources as complementary" governing rule, and the synergy-input directional confirmation (via #1703) all landed here. Deliberately sequenced after Layer 1 per the researcher's own instruction — reassigned to Researcher, not held under Claude. |
| **#1547** | Superseded in practice by #1682's real work weeks ago, never formally closed — packaged for closure as session-end housekeeping. |

## 2. Files created or changed

- `iba/docs/pipeline-build-stocktake-v1-20260916.md` — new. First-pass stocktake of every escalation flowing into #1706, before the deeper Layer 2 review.
- `iba/docs/1660-1711-layer2-volume-and-filter-reconciliation-v1-20260916.md` — new. Live volume numbers (corpus-wide vs. M-code-only) reconciling #1660 against stage 5's design.
- `iba/docs/ib-observation-governing-rules-checklist-v1-20260916.md` — new. Every rule governing any `ib_observation`/`ib_node`-writing stage, one checkable place, per direct researcher instruction.
- `iba/docs/1701-faculty-engagement-catalogue-addition-v1-20260916.md` — new. Full field set for the new `T2.11` catalogue component, closing #1701.
- `iba/docs/1704-analytic-event-inventory-phase2-match-v1-20260916.md` — new, corrected in place twice (note_type Group D correction; M47 correction on event 13).
- `iba/docs/1704-analytic-event-inventory-phase3-corrective-actions-v1-20260916.md` — new, Group D added.
- `iba/docs/1704-analytic-event-inventory-phase4-question-crosswalk-v1-20260916.md` — new, corrected in place per the researcher's Phase 5 content decisions (8 rows marked dropped/retired, `T2.1` and `T7.1.3` corrected).
- `iba/docs/1704-analytic-event-inventory-phase5-design-deep-dives-v1-20260916.md` — new. Framework/options/pros-cons for all 8 remaining open design elements.
- `iba/docs/1704-catalogue-content-decisions-v1-20260916.md` — new. The researcher's own decisions against all 8 Phase 5 items, verbatim, with the net effect on #1696's migration scope.
- `iba/docs/1706-lexical-stack-full-rebuild-consolidated-build-proposal-v1-20260915.md` — extensively revised throughout the session (see #1706 row above); this is the project's live master register for the whole lexical-stack rebuild.
- `iba/docs/1700-per-question-answer-quality-review-v1-20260914.md` — T7 tier findings added, review marked complete.
- `iba/docs/1700-sample-t7-v1-20260914.json` — generated by the existing `1700-sample-answers-tool-v1-20260914.py`, T7's sampled answers.
- `outputs/escalation/*`, `research/discovery/spine-check*` — regenerated reports (normal rotation from `Escalation.ps1 -Action List/Update` and `Spine-Check.ps1` runs), prior versions archived automatically.

## 3. Decisions made

**Researcher's own decisions (not self-correctable):**
- `#1706` is the correct venue for ongoing lexical-stack work, not `#1607`/`#1604` (both closed/parent-only).
- `role`'s JSON shape: bare array, not array of objects — "the column value should include the role(s) of the word in the row," a technical call left to Claude but confirmed.
- Continue `#1704` in conjunction with `#1700`/`#1702` explicitly, so events/questions/catalogue cross-entries are all correlated before `#1711` starts.
- Fold `pattern_type` and all new catalogue content into `#1696`'s migration script; do not write to `bible_research.db` again.
- Passage is dropped as a reading-unit concept entirely, replaced by the `needs_adjacent_verse_context` observation flag — "passages are no longer presented as a unit of reading."
- The "unresolved, not guessed" principle belongs at the design-principle level for every observation-writing stage, not as a ported column.
- Both flag types (adjacent-context, cross-family/cluster) are standard, cross-cutting observation rules; their follow-up happens in a later analytic run, "probably as part of synergising."
- `#1658`: no view registration needed — read the three tables directly; the three sources are complementary, never replace one with another.
- `#1701`: approved the `T2.11` "Faculty Engagement" catalogue addition as drafted (after a correction on placement — a new component, not folded into the unrelated `T2.1`).
- Phase 5, all 8 items decided directly: item 1 (B), item 2 (C), item 3 (B — flagged conflict with items 5/6), item 4 (retire, genre adds no real value), item 5 (drop `T0.4`), item 6 (C, drop `T5.4`/`T5.5`/`T5.6`, replacements next round), item 7 (**correction: spirit/soul/heart/mind is `cluster M47`, not a T-code gap** — keep `T2.1` live, use the cross-cluster co-occurrence mechanism), item 8 (B, expand `T7.1.3`'s text for idiom/analogy/implied meaning; general wording pass explicitly parked).
- Get all escalations up to date and write this session log ahead of an expected system restart.

**Claude self-correctable fixes / investigations (found and fixed directly, not researcher judgment calls):**
- Layer 1's three wrongly-flagged-open items — found already answered in a document that existed but hadn't been checked; corrected in place, not asked about.
- The note_type completeness count — verified live rather than trusted the #1589 original scope; found 10 undefined, not 6; all 15 given a proper disposition.
- The connective sub-type "did it survive migration" question — verified live in `cluster_strong.rationale`; it did, richer than expected.
- `#1694` — verified live against the correct table; confirmed moot.
- The `#1660`/stage-5 reconciliation — investigated and quantified live before presenting a recommendation, not asserted.

## 4. Open items carried into next session

- **`#1706` §7's live action items**: sign off the 6-component pack as a set; `#1711`'s own design (now well-grounded, still not started, deliberately sequenced after Layer 1).
- **The item-3 conflict** (future-orientation-marker mechanism approved, its only consumers dropped) — needs the researcher's own call: build anyway anticipating replacement questions, or hold.
- **T5's reframe** — researcher's own replacement questions for the dropped `T5.4`/`T5.5`/`T5.6` content, "next round," not yet provided.
- **Layer 1's actual build execution** (Phase A/B of #1706) — design fully closed, nothing built yet; this is the next real construction work whenever the researcher greenlights it.
- **3 escalations packaged for closure this session** (`#1691`, `#1702`, `#1547`) sitting at `ready_for_approval` — a quick nod closes them.
- **`idiom`'s own `cfg_method_rule`** and the other Group A note_type registrations (`compound_unit`, `polarity`, `chain`, `connective`, `entity_link`, `pronoun_resolution`) — designed, not yet built, real work for `#1607`.

## 5. Git state

