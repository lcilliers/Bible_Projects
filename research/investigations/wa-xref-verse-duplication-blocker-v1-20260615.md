# XREF verse duplication — a blocker for the lexical/VE work

> Researcher (2026-06-15): the residual duplicate verse-records are *"not grounded — another failed attempt to soft-delete same verses due to XREF."* Correct. If the lexical analysis creates one row per span per verse, these duplicates produce **duplicate lexical/meaning records**. Must be grounded **before** the VE/lexical build. Scoped below.

## The problem
The XREF architecture says: a term is OWNER in one registry (verses active) and XREF elsewhere (verses soft-deleted). That soft-delete **failed for 2,556 active verse-records** whose term is `term_owner_type='XREF'` — they should not be active. Worse, they don't all resolve the same way:

| active XREF verse-records | count | situation | safe action |
|---|---|---|---|
| has an **active OWNER twin** (same reference+term) | **933** | true duplicate | soft-delete the XREF (OWNER remains) — **clean** |
| **no OWNER copy at all** | **1,504** | XREF is the *only* active copy; OWNER missing | **DO NOT drop** — would lose the verse. Investigate: OWNER mislabeled? OWNER under a sub-entry `term_id` the exact match missed? |
| only a **soft-deleted OWNER** | **119** | OWNER was wrongly soft-deleted | restore OWNER + drop XREF, or promote XREF to OWNER — needs a decision |

(+179 active verse-records have NULL `term_owner_type` — a separate small gap.)

## Why a blind fix is wrong
- Dropping all 2,556 loses **1,504** sole-copy verses.
- Keeping them all means the lexical build writes **duplicate meaning** for the 933 true-dups and mis-homed meaning for the rest.
- This is the same class as OT-DBR-009 (the `mti_terms` dedup) — an unresolved XREF grounding issue.

## Staged resolution (proposed)
1. **The 933 true-dups — clean, ready:** soft-delete the active XREF verse where an active OWNER twin exists (reversible, OWNER preserved). Removes the clearest duplicates immediately.
2. **The 1,504 owner-missing — investigate first:** check whether the OWNER exists under a sub-entry/variant `term_id` (the exact-match likely undercounts), or whether the `term_owner_type='XREF'` label is simply wrong for a term that only lives here. Likely a mix; resolve by re-deriving owner_type from the actual OWNER presence, not blind deletion.
3. **The 119 owner-deleted — decision:** restore the OWNER (and drop the XREF), or promote the XREF. Researcher call per pattern.
4. **Re-key option:** the only *guaranteed*-unique handle is `verse_record_id` (or `(reference, term_id, file_id)`); `verse_context` already keys off `verse_record_id`, so **the VE/lexical tables should key off `verse_context_id` / `verse_record_id`, not `(reference, term_id)`** — which sidesteps the dup at the structural level even before the data is cleaned.

## Bearing on the VE redesign
- Confirms `ve_lexical` / `verse_context` must key on **`verse_context_id`** (unique) — never `(reference, term_id)`.
- But the duplicate *verse_context* rows that would follow from duplicate *verse_records* must still be grounded, else the analysis is done twice. So: **ground the XREF verses (at least the 933 + the owner_type re-derivation) before generating lexical rows.**

## ROOT IS AT THE TERM LEVEL — the CANONICAL list (`mti_terms`), 2026-06-15
The researcher's call ("don't patch — determine what the truth should be; start with the **canonical** `mti_terms`, not the per-registry `wa_term_inventory`") is correct. Active `mti_terms` is **not grounded**:

- **active `mti_terms`: 2,619 rows / 2,565 strongs** — should be 1 row per Strong's.
- **a) NOT unique:** **30 strongs have >1 active row (54 duplicate rows)** — OT-DBR-009. Pattern (H5822 *vulture* ×4): 1 owned-but-`excluded` row + 3 orphan copies (`owning_registry_fk` NULL, status NULL).
- **b) NOT cleanly owned/marked:** **80** rows have NULL `owning_registry_fk` (no home); status = `extracted` 2,143 · `extracted_thin` 306 · **`excluded` 57** · **`candidate_delete` 22** · **None 79** · misc — so **~158 active rows carry a non-canonical status** (excluded/candidate_delete/None) yet are not soft-deleted.

(The earlier `wa_term_inventory` figures — 148 no-OWNER etc. — are the *downstream registry copies*, not the canonical truth; superseded by the above.)

**The canonical truth to establish, in order:**
1. **Unique:** exactly one active `mti_terms` row per Strong's → dedup the 30 (collapse the orphan copies; keep/define the canonical row).
2. **Owned:** every canonical row has a valid `owning_registry_fk` → resolve the 80 NULLs.
3. **Status-consistent:** an active canonical row should not be `excluded`/`candidate_delete`/None → reconcile the ~158 (soft-delete the truly excluded, or correct the status).

**The truth to establish:** every Strong's in active use has **exactly one** canonical OWNER (its single home where lexical analysis runs once); every other active occurrence is an XREF whose verses derive from / are soft-deleted in favour of the OWNER.

**Decisions needed before any fix (researcher):**
- **D-T1:** for the 123 XREF-only strongs — does an XREF-only term get **promoted to OWNER** in one registry (which?), or is "reference-only, no owner" a legitimate state with its own lexical handling?
- **D-T2:** the 22 + 3 soft-deleted-OWNER — restore the OWNER, or re-home to an active registry?
- **D-T3:** dedup the 1 double-OWNER + the 30 `mti_terms` duplicates (OT-DBR-009).

Only once each Strong's has exactly one OWNER does the **verse** owner-status become deterministically derivable (OWNER verses active, XREF soft-deleted) — and only then can the 933/1,504/119 verse split be resolved correctly rather than guessed.

## Recommendation (revised)
**Do not touch the 933 yet.** Fix the order: (1) establish the term truth — one OWNER per Strong's (D-T1/2/3) — then (2) **re-derive** verse owner-status from that truth (one mechanical pass, not three guesses), then (3) build VE/lexical keyed on `verse_context_id`. Patch-fixing the 933 first would just re-assert a grounding that the terms don't yet have.
