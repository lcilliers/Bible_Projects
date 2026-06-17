# VE engine — rule-compliance & scope audit (01b spec vs live build) — v1 — 2026-06-17

**Prefix:** wa · **Document type:** Compliance audit · **Status:** findings for decision. No code/DB change made.

**Why this exists.** The researcher challenged the corpus-rollout plan with four questions that exposed it as premature. This audit answers them by reading the live engine source (`_ve_engine_v2.py`) against the **settled** 01b v2 spec (§4 item catalogue · §5 C-decisions · P1–P9) and the live `ve_lexical` data. **Headline: the live engine is iteration-1 seed — roughly half the §4 rules are stubbed, deferred-to-read, or unimplemented. The API reads are not "enhancing" a complete mechanical layer; they are doing the PRIMARY work for four fields because the mechanical rule is a stub.**

---

## 1. Direct answers to the four questions

### Q1 — "23,000 unique verses but 40,000 valences? Are we doing duplicate processing?"
**Partly yes.** 40,739 units (term-in-verse) span only **18,966 distinct verses** (~2.15 inner-being terms per verse) — of 23,318 canonical verses. The duplication is of three kinds:
- **Per-term re-read (the big one).** A field whose package submits *every unit* (valence: `where=None`; divine-involvement: all rows) re-sends the **same verse text once per term in it** — ~21,800 of valence's 40,739 submissions re-read a verse already sent for another term. The *question* differs per term, but the verse payload repeats. **Fix: batch by verse** (send a verse's morphology once, ask about all its inner-being terms together) — large token saving, no loss.
- **T2 scope (≈25%).** 10,168 of the 40,739 units are **T2** (qualifiers/references — "never analysed standalone", memory [[feedback_t2_reference_flag_reclassify]]). Reading valence/divine/etc. for T2 units is likely wasteful or wrong. **Decide: exclude T2 from the reads** (cuts valence from 40,739 → ~30,571).
- **True dup units:** only **296** (reference, mti_term_id) pairs map to >1 unit — small, but worth a dedup check.

So valence at 40,739 is **over-scoped on two axes** (per-term repetition + T2). Real valence need after batching-by-verse and excluding T2 is far smaller.

### Q2 — "Have all the rule updates been applied? I'd expect more than a few fixes. How do we confirm completeness/compliance?"
**No — not applied.** The engine is explicitly "iteration-1 seed" (its own docstring). The compliance matrix (§2) shows **~10 of the §4 rules are partial/stub/missing**, and **4 of the 5 read fields exist only because the mechanical rule is a stub** (§3). The "few fixes" (I1–I3) from the M01 review were real but were the tip — they came from one characteristic's *data*, not from auditing the engine against the spec. **Completeness/compliance is confirmed by the matrix in §2 as a living checklist + the engine's own read-back audit (founded + coverage loop-until-dry, 01b §6b) run to convergence per cluster.** Neither has been run as an acceptance gate yet.

### Q3 — "Is location the only field with unresolved items?"
**No.** Unresolved/placeholder states across the corpus:
| field | unresolved token | count | what it means |
|---|---|---|---|
| object-type | `thing/abstract` (the lump) | **14,055** | mechanical can't split thing/abstract/situation/threat |
| cause | `pending-read` | **9,813** | mechanical detects a causal marker, defers resolution |
| **type** | `UNRESOLVED` | **1,897** | term has no POS in the measure layer (morph gap) — *not* an API-read item; a backfill |
| location | `UNRESOLVED` | 1,532 | spirit/breath seat ambiguity |

`type=UNRESOLVED` (1,897) is a **measure-layer coverage gap** (missing morphology), not something the planned reads touch — it would silently stay unresolved.

### Q4 — implicit: is the rollout as planned sound?
**No — resequence.** Running expensive API reads to populate divine/valence/object-type/cause *before* implementing their (largely deterministic) mechanical rules means **paying the API to do work a fixed rule should do** — violates P1 (mechanical-first) and §6 cost. The reads should handle only the genuine residue *after* the mechanical rules are brought to spec.

---

## 2. Compliance matrix — 01b §4 item × live engine

Status: ✅ to spec · ◐ partial/seed · ⛔ stub or unimplemented.

| # | item | 01b rule (settled) | live engine (`_ve_engine_v2.py`) | status |
|---|---|---|---|---|
| 1 | sense | record **BOTH** target_word AND lemma `medium_def` (Q2, P9) | records target_word **only** (medium_def dropped, ln 164) | ◐ missing medium_def |
| 2 | type | POS-only (C-1) | POS map, else UNRESOLVED (ln 167) | ✅ (1,897 UNRESOLVED = morph gap) |
| 3 | compound | role(s) per co-term; **one co-term may carry MULTIPLE roles** (C-4/C-6) | exactly **one** role, cluster-derived (T2→qualifier else seat→co-seated else partner, ln 178) | ◐ single-role only; no object-of/cause-of |
| 5 | location | **always** sense-gated (C-2); dedup simple values (P3) | sense-gate **only** G4151/H7307; **no dedup** (triple-heart, ln 182-191) | ◐ I1 + C-2 partial |
| 6 | origin | within-person · received · generational · **giver→received (C-5)** | **only** 'from'-prep→received (ln 271) | ⛔ 3 of 4 rules + C-5 missing |
| 7 | faculty | R1 term-lemma **+ R2 co-occurring faculty-lemma** | **R1 only**; `FACULTY_LEMMA` list is **dead code** for assignment (used only in audit, ln 313) | ⛔ R2 unimplemented |
| 8 | divine-involvement | full role taxonomy: agent·possessor·giver·object·addressee·none (C-3) | **only** `present` / `agent/subject` (ln 239-245) | ⛔ stub — read does the rest |
| 11 | immediate-response | coordinated reaction verb | implemented, light (ln 292) | ◐ seed |
| 12 | **produces-effect** | result-clause effect (Q13, included) | **not emitted — 0 rows in DB** | ⛔ missing entirely |
| 13 | relational | {direction → object}; expectation test | preposition text only, no object, no NONE/UNRESOLVED (ln 265) | ◐ crude |
| N1 | object/object-type | governed head noun; type incl. **group**; thing/abstract split | raw surface word (determiner leak, I3); type **lumps** thing/abstract (14,055); no group (ln 100-105, 203-229) | ◐ I3 + lump |
| N2 | cause | causal-clause subject / perception object | detect→`pending-read` (defers to read); perception case only (ln 280) | ◐ detect-and-defer |
| N4 | intensity | intensifier lemmas | 5-entry seed list (ln 40) | ◐ seed |
| — | valence | term-inherent ∪ context; **VALIDATED 2026-06-17:** only *prohibition (’al/mē)→forbidden* is mechanical (93%); *commanded/righteous/neutral* are interpretive | now: term-inherent ∪ prohibition→forbidden (added) | ◐ **resolved-as-designed** — forbidden mechanical; rest legitimately read (NOT a stub) |
| — | experiencer | possessor/subject person | implemented (ln 208-237) | ✅ |
| — | mode | column | emitted, skipped to column | ✅ |
| — | lexical_note | audit founded+coverage | implemented (ln 304-318) | ✅ |

**§5 conflict decisions:** C-1 ✅ · C-2 ◐ (spirit only) · C-3 ⛔ (crude) · C-4/C-6 ◐ (single role) · C-5 ⛔ (not done).
**Principles:** P1 ◐ (4 fields lean on read, not mechanical) · P3 ⛔ (location dedup) · P5 ◐ (only cause/valence use the expectation test) · P9 ◐ (sense missing medium_def; some cites carry bare Strong's) · P7 ✅.

---

## 3. The key structural finding — reads compensate for stubs

What the **mechanical engine** actually produces (source=`v2_engine_iter1`), vs the spec value space:

| field | mechanical values produced | spec value space | the read is… |
|---|---|---|---|
| divine-involvement | `present` 9,795 · `agent/subject` 1,963 | agent·possessor·giver·object·addressee·none | **doing the primary classification** |
| valence | `sinful` 484 · `righteous` 332 | +commanded·forbidden·neutral | **doing the primary classification** |
| object-type | `thing/abstract` 14,055 (lump) · person · God · spiritual-being | +situation·thing·abstract·threat·group | **splitting a lump the rule should split** |
| cause | `pending-read` 9,813 (defer) | the eliciting node | **doing the primary resolution** |

This is the crux: the corpus reads are **not enhancements** — for these four fields the mechanical layer is a stub and the API is doing work that is **substantially deterministic** (valence imperative/prohibition = morphology; divine role = morphology + lemma position; object-type group/situation = lemma class). Paying API for it is both a P1 violation and an avoidable cost.

---

## 4. How we confirm completeness & compliance (the method, going forward)

1. **This matrix (§2) is the compliance checklist** — every §4 item must reach ✅ (to-spec) or a *documented, decided* ◐ before a field is considered done. Re-run after each engine change.
2. **The engine's own read-back audit (01b §6b)** — founded (every value cites a present measure) + coverage (every content word accounted) — run **to convergence (loop-until-dry)** per cluster. An audit pass surfacing *no new* coverage gaps = that cluster's lexical is complete. This is the per-verse completeness gate the spec already designed; it has not been run as an acceptance criterion.
3. **Value-space conformance check** — each field's stored values ⊆ its spec value space (catches stubs like `present`/`thing-abstract` that aren't in the spec).
4. **Scope conformance** — units processed = intended scope (M-cluster vs T2 decision; no XREF/dup double-count).

---

## 5. Revised sequencing (supersedes the rollout-plan v1)

The rollout-plan v1 (`wa-ve-corpus-rollout-plan-v1-20260617.md`) is **paused** — it rolls out reads over a non-compliant engine. Proposed order instead:

- **Phase 0 — Engine compliance alignment (mechanical, no API).** Implement to spec the stub/missing rules: valence context (imperative/prohibition), divine role taxonomy, object-type split + group, origin (within-person/generational/C-5), faculty R2, compound multi-role, location dedup + full sense-gate, produces-effect (VE12), sense medium_def. Expand the seed lists. Each → re-run M01 + the compliance matrix + read-back audit. *This is the "more than a few fixes" you expected.*
- **Phase 1 — Base rerun corpus-wide** on the compliant engine (deterministic; preserves existing reads).
- **Phase 2 — Reads, rescoped to the genuine residue only.** After Phase 0, most of divine/valence/object-type resolve mechanically; the API read handles only what stays UNRESOLVED/ambiguous (far smaller than 77,900 items), **batched by verse**, **excluding T2** (pending decision). Cost falls by a large factor.
- Per-phase self-audit + confirmation before proceeding, as requested.

---

## 6. Decisions needed
1. **Adopt Phase 0 (engine alignment) before any reads?** (recommended — else we pay API for deterministic work.)
2. **T2 scope** — exclude T2 units from reads? (cuts ~10,168.)
3. **Batch reads by verse** (not per unit)? (cuts the per-term repetition.)
4. Priority order for the Phase-0 rule fixes (suggest: the four stubs first — valence, divine, object-type, cause — since they gate the biggest read costs).

*Source: `_ve_engine_v2.py`, `_apply_generate_ve_lexical_v2.py`, `01b-VE-field-reliability-and-rules.md`, live `ve_lexical`. Read-only audit.*
