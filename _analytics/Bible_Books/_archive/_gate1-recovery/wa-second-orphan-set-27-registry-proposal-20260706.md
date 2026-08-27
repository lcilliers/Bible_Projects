# Second orphan set (27 span-orphan stubs) — registry-assignment proposal

> The 27 legacy stub `mti_terms` (2026-07-05, NULL registry, no inventory) that remain uncovered by the Psalms master-index backfill (172 characteristic spans). Same treatment as the 97: assign each to a `word_registry` home, then `audit_word --add-terms` + re-backfill. Social-category persons → **third party** per the researcher. Date: 2026-07-06. Confirm/correct, then I onboard.

## Tier 1 — CLEAR (direct existing registry)

| Strong | Gloss | → Registry |
|---|---|---|
| H0157 | to love | **love** |
| H0833 | to bless | **blessing** |
| H2449 | be wise | **wisdom** |
| H7307 | spirit | **spirit** |
| H7891 | to sing | **praise** |
| H3467 | to save | **salvation** |

## Tier 2 — PROBABLE (one reasonable home)

| Strong | Gloss | → Registry | Note |
|---|---|---|---|
| H1350 | to redeem | **salvation** | no `redemption` registry; redeem = deliverance |
| H5382 | to forget | **memory** | forgetting = memory's negative |
| H7911 | to forget | **memory** | (duplicate sense of forget) |
| H5678 | fury | **wrath** | |
| H5358 | to avenge | **wrath** | no `vengeance` registry (as with H5359/60) |
| H6973 | to loathe | **hatred** | |
| H7810 | bribe | **corruption** | |
| H7309 | relief | **comfort** | |
| H5087 | to vow | **commitment** | vs `devotion` |
| H5088 | vow | **commitment** | |
| H3238 | to oppress | **wickedness** | oppression as act |
| H3905 | to oppress | **wickedness** | |
| H3906 | oppression | **wickedness** | |

## Tier 3 — UNCERTAIN (needs your call)

| Strong | Gloss | Options |
|---|---|---|
| H0079 | to wrestle | strife / struggle — or physical (Naphtali etymology)? |
| H5319 | wrestling | strife — or physical/proper-noun? |
| H0014 | be willing | **assent** / willingness — or "consent"? |
| H2670 | free (chophshiy) | salvation (liberty/release) — or a status, not an IB state? |

## Tier 4 — THIRD PARTY (social-category persons, per researcher)

Like Satan → `spiritual powers`, these are **third parties** the inner being responds to, not IB characteristics. The classic biblical quartet of the vulnerable. **Proposal: one new registry `the afflicted`** (third-party recipients; role=reference, cluster NULL):

| Strong | Gloss |
|---|---|
| H0034 | needy |
| H0490 | widow |
| H1800 | poor |
| H3490 | orphan |

*(Alternative: home each under an existing IB concept as a reference — but a dedicated third-party category mirrors the Satan treatment and keeps them cleanly separable. Confirm the registry name `the afflicted`, or give a preferred one.)*

## What I need
1. Confirm/correct Tier 1–2 (23 terms).
2. Decide Tier 3 (4 terms) — especially H2670 *free* and the two *wrestle* senses.
3. Confirm the **third-party registry** for the vulnerable quartet (name = `the afflicted`?).

Then: REGISTER any new registry → `audit_word --add-terms` per home → re-run `_apply_master_index_backfill_v1 --book 19 --with-ambiguous` → Psalms characteristic-span miss should reach ~0. Stub cleanup: the 27 NULL-registry stub mti get reconciled/superseded during onboarding.

*Filed 2026-07-06.*
