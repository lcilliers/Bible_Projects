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

## Recommendation
Do step 1 (933 clean) now if approved; investigate step 2 (the 1,504, almost certainly a sub-entry match artefact + some mislabels) before deciding; surface step 3 (119) for a call. Then proceed to the VE/lexical build keyed on `verse_context_id`.
