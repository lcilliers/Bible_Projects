# Analytic Event Inventory — Phase 2: Match (4-part test)

**Escalation:** #1704 · **Phase:** 2 of 3 (Discovery → Match → Corrective Actions) · **Date:** 2026-09-16

Per Phase 1's own closing instruction: match every candidate event found (Phase 1a/b/c, 17 events)
against the 4-part test — (1) proper name, (2) config definition, (3) code home, (4) purpose tying
it to catalogue question(s). Nothing re-derived from scratch: every live check below cites the
Phase 1/#1700/#1702 finding it draws from; only the T7 completion (#1700) and the 98-row live count
are freshly checked this session. **This directly answers the researcher's instruction this
session** ("1704 feeds directly into 1700 and 1702... continue with 1704 in conjunction with 1700
and 1702 to ensure that all events are identified and quantified, that all the questions are
validated") — Phase 2 is where that convergence actually happens.

**Reading the table:** ✅ = complete (all 4 parts present) · 🔧 = named + purpose clear, code/config
missing or disconnected (buildable) · ❓ = genuinely undesigned (needs a decision, not just code)

| # | Event | Name | Config | Code home | Purpose (questions fed) | Status |
|---|---|---|---|---|---|---|
| 1 | **directional-party-frame** | New this phase (#1704 Phase 1b) | None — combines two existing live mechanisms (`verb_argument` `note_type`, `party_kind`), neither wired to the other | `party_kind`: `lib/lexical.py` (live). `verb_argument`: `cfg_method_rule` id=63 (live, unused — 1 example ever, #1606/#1607) | T0.1, T2.9, T4.1–T4.5 (18 questions — largest single gap in the catalogue) | 🔧 **Highest-value, most concrete gap.** Both ingredients exist; the combining event does not. Not gated on #1705/#1711 any more (§ below) — this is a mechanical pairing, not the LLM-driving-mechanism question #1711 is about. |
| 2 | **T3-operation-surfacing** | New (#1702) | None | `cluster_strong.operation` flag exists, confirmed dead — not read anywhere in `lib/`/`handlers/` | T5.1, T5.3 (feeds #1701's process-first framing directly) | ❓ **Folded into #1701 by design, not a standalone build** (#1702 §4's own recommendation) — resolving this is resolving #1701, not a separate item. |
| 3 | **T14-body-part-surfacing** | New (#1702) | None | No `verse_lexical` column (unlike T4/T5/T7/T8/T9) | T2.7, T2.10 | 🔧 Same shape as `is_negator`/`party_kind` — a cheap boolean/lookup column, per #1702 §4 item 4's own recommendation. Buildable now, no other dependency. |
| 4 | **cross-characteristic co-occurrence** | New (#1704 Phase 1b) | None live | `_assess_cross_cluster_cooccurrence.py` — **built once, confirmed inactive since 2026-08-18** (escalation #729, zero `cfg_method` call sites) | T5.4, T6.1, T6.2, T6.3 (partial) | 🔧 **Cheapest recovery of the four highest-value gaps** — the mechanism isn't missing, it's switched off. Reactivating + registering it (per `governance.new_utility_registration_timing`) is most of the work. |
| 5 | **causal-connective detection** | New (#1704 Phase 1b) | **RESOLVED, 2026-09-16, checked live.** Per #1499's own explicit decision, closing this exact question: T6 was deliberately kept as ONE bucket ("causal/coordinating/purpose sub-typing would be 1-3 codes each, exactly the 'minute group' your test warns against; sub-type recorded in rationale instead"). Checked live: `cluster_strong.rationale` for all 95 T6 rows DOES carry the sub-type, richer than the original 3-way split — causal/coordinating/purpose/temporal/comparative/concessive/adversative/conditional/inferential/rhetorical-interrogative/relative-locative, per-strong. **The granularity survived; it's just free text, not a structured column.** | Confirmed dead per #1702 §4: **no `is_connective` column exists at all**; zero `cluster_strong` references in enrichment code. `rationale` itself is human-readable prose, not queryable (`WHERE sub_type='causal'` isn't possible against it as-is). | T6.3 specifically | 🔧 **Corrected from ❓ to 🔧** — the "did it survive" question is answered (yes). What's left is purely build work: `is_connective` column (per #1702's recommendation), and if T6.3 needs the *sub-type* mechanically (causal vs. coordinating vs. purpose), a structured column parsed once from the existing `rationale` text — not a fresh classification pass, the data already exists. |
| 6 | **purpose-clause-detection** | New (#1704 Phase 1c) | None | None — genuinely new mechanism (Hebrew lə+infinitive, Greek hina/hopos telic markers) | T0.2.1 | ❓ Undesigned, lightweight in principle (a morph/lexical pattern-match), not urgent (1 question fed). |
| 7 | **kind-classification** | New (#1704 Phase 1c) | None | None, but trivial — direct `morph_code` part-of-speech derivation | T1.2.1 | 🔧 Cheapest item on this whole list — `morph_code` is already populated for every Layer 1 row; this is a derivation, not a data-collection problem. |
| 8 | **`compound_unit`** | Exists (`note_type` ordinal) | **Undefined** — 0 `cfg_method_rule` row (#1589) | `lexicalenrich.py` accepts the value, no quality check for it | T1.2.2 | 🔧 Purpose now confirmed by this phase (T1.2.2) — #1589's gap has a real destination, not just a missing definition in the abstract. |
| 9 | **structural-opposite-term detection** | Exists conceptually, no event name | None | `related_word`/`cross_lemma_shared_gloss` note_types partially cover this | T1.3, T7.1.5 (duplicate demand — one event, two consumers) | 🔧 Reuse existing mechanism, formalize as one named event feeding two question slots. |
| 10 | **`polarity`** | Exists (`note_type` ordinal) | **Undefined** — 0 `cfg_method_rule` row (#1589) | `lexicalenrich.py` accepts the value, no quality check | T1.7 directly | 🔧 Same shape as `compound_unit` — purpose now confirmed (T1.7's blocked/distorted/resisted questions), definition still missing. |
| 11 | **post-occurrence / characteristic-level sequence** | New (#1704 Phase 1c) | None | None — a genuinely different grain (characteristic-level across verses) from `chain`/`recurrence_role_shift` (within one verse/span) | T1.5, T1.6, T5.2, T5.5 (4 consumers) | ❓ Undesigned, four consumers — worth real design attention given the fan-out, not a quick fix. |
| 12 | **future-orientation marker** | New (#1704 Phase 1c) | None | None, but lightweight — `morph_code` tense/aspect + `related_word`-shaped lexical markers | T5.6, T0.4 (partial) | ❓ New but cheap once designed — feasible from existing Layer 1 data. |
| 13 | **constitutional-level vocabulary detection** | New (#1704 Phase 1c) — **CORRECTED 2026-09-16, no longer a T-code question** | N/A — not a T-code gap | **RESOLVED, researcher correction, verified live**: spirit/soul/heart/mind is `cluster M47` ("Inner Seat," 38 strongs — `lev`/`kardia`/`nephesh`/`ruach`/etc.), not a missing T-code referent class. Mechanism = the same cross-cluster co-occurrence event as event 4, filtered for M47 co-occurrence with the verse's other M-code(s). | T2.1 | 🔧 **Corrected from ❓ to 🔧, folded into event 4** (cross-characteristic co-occurrence, reactivate `_assess_cross_cluster_cooccurrence.py`) — no longer folds into #1701, no new T-code design needed. |
| 14 | **typological-link** | New (#1704 Phase 1c) | None | None — likely needs an external cross-reference resource this project doesn't have | T0.4 | ❓ Low feasibility without new data infrastructure; lowest priority on this list. |
| 15 | **genre / contextual-setting classification** | New (#1704 Phase 1c) | None | **No data source in `iba.db`** (#1607 D12/D13 — `genre` was dropped from `verse_meta`, not built) | T7.2.2 (confirmed unexercised, #1700 T7 review), T7.2.4 | ❓ Blocked on a base-data gap (`verse_meta.genre`), not just an unwired mechanism — this is #1594's own orphaned-column finding (#1706 Phase G item 33), now confirmed to also be Vector A's T7.2.2a/2b unexercised-split root cause. |
| 16 | **anchor-verse ranking** | New (#1704 Phase 1c) | None formal | **Already in progress** at #1526 (on-hold, researcher's own instruction) | T7.2.5/2.6 | 🔧 Not a fresh gap — #1526's existing anchor-verse-by-`resolved_sense` work is this event under a different name. Confirmed by #1700's T7 review: T7.2.5/2.6 are answered well today (real synthesis, e.g. the Hos 11:8/Isa 61:3 dual-anchor reasoning) — the historical corpus already does this by hand; #1526 is about doing it mechanically/consistently. |
| 17 | **term-grain aggregation** | Not a new event — a grain correction | N/A | `related_word`/`cross_lemma_shared_gloss`/`vw_strong_meaning_raw` reads already exist | T1.1, T7.1 (both confirmed by #1700's T1/T7 reviews to be answered well today, just per-characteristic not per-term) | 🔧 Confirmed twice now (T1 and T7 both reviewed clean) — the *answers* are good, the *grain* is wrong for what a term-level catalogue slot should hold. Directly relevant to #1711 §4A's own open scope-grain question (§ below). |

## What #1700/#1702's completed work changes about this table, concretely

- **Zero genericity anywhere in the live catalogue** (#1700, all 98 questions now reviewed) means
  none of these 17 gaps are "the mechanism exists but produces bad answers" — every one is a true
  **coverage** gap (no mechanism) or **connection** gap (mechanism exists, unwired), never a
  **quality** gap. This simplifies Phase 3: every corrective action is "build" or "wire," never
  "fix the LLM's reasoning."
- **#1702's mechanism-status findings map directly onto 6 of the 17 events** (rows 1, 3, 4, 5, 7,
  10 above) — confirming the user's own framing that #1704/#1700/#1702 are one investigation, not
  three. The T-code-level view (#1702) and the question-level view (#1704/#1700) converge on the
  same gaps from opposite directions.
- **The genre gap (row 15) is now confirmed as three findings converging on one root cause**: #1594
  (orphaned `passage.genre`/`verse_meta.genre` column), #1607 D12/D13 (dropped from the Layer 1
  redesign), and #1700's T7 review (T7.2.2a/2b confirmed unexercised, zero mechanism). One fix, not
  three separate carried-forward items.
- **Row 17 (term-grain aggregation) is a direct input to #1711's still-open scope-grain question**
  (#1706 §4A item 2) — T1.1 and T7.1 both need term-level output, which only a corpus-wide (not
  per-cluster) Layer 2 pass can produce naturally. This tips the weight of that decision, though it
  doesn't fully settle it (§4A's own framing: not a free choice either way).

## Bottom line — 17 events, sorted by what's actually needed

**Buildable now, no other dependency (🔧, 10 events, corrected 2026-09-16 — causal-connective
detection AND constitutional-level vocabulary detection both moved here from ❓):**
directional-party-frame, T14-body-part-surfacing, cross-characteristic co-occurrence (reactivate —
**now also serves T2.1**, per the M47 correction), `compound_unit` (define), structural-opposite-term
detection, `polarity` (define), anchor-verse ranking (already #1526), term-grain aggregation (grain
fix, not new build), kind-classification, causal-connective detection (`is_connective` column
+ optionally parse the sub-type already recorded in `cluster_strong.rationale`).

**Genuinely undesigned, real decision needed (❓, 5 events — with researcher decisions now recorded
against all 5, see Phase 5/`1704-catalogue-content-decisions-v1-20260916.md`):**
purpose-clause-detection, post-occurrence sequence (4 consumers), future-orientation marker,
genre/contextual-setting (retired, not built — see decisions doc item 4), typological-link (dropped
— see decisions doc item 5).

**Deliberately folded into other open escalations, not standalone (1 event, corrected 2026-09-16):**
T3-operation-surfacing folds into #1701's resumption. **Constitutional-level vocabulary detection
no longer belongs here** — corrected (event 13 above) once the researcher identified it as `M47`,
an existing M-code, not a T-code gap needing #1701's own design attention.

Phase 3 (corrective actions), Phase 4 (per-question crosswalk), and Phase 5 (design deep-dives +
researcher decisions) follow.
