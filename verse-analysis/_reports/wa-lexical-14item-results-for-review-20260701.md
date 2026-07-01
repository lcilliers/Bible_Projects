# Lexical derivation — all 14 items, results for review (2026-07-01, overnight)

- **For:** researcher morning review. **Harness:** `scripts/_probe_lexical_derivation_all14_v6_20260701.py` (read-only). **Companion:** `wa-lexical-item-derivation-validation-v1-20260701.md` (rounds 1-6).
- **What was done:** wired up all 14 dimensions for every term in a passage; iterated the rules (presence-test + focal-operation filter + argument parsing); then tested on 4 fresh passages across genres.

## 1. Per-item status (across all tested verses)
| dim / item | status | note |
|---|---|---|
| **D1 identity** (sense+type) | ✅ reliable | correct everywhere |
| **D2 source** | ✅ narrative / ⚠ poetry | dread→ruthlessness, anger→provoke ✓; noise across independent aphorisms |
| **D3 seat/bearer** | ✅ seat reliable | soul, heart, construct-chain ✓. **bearer (who) not yet derived** — gap |
| **D4 operation** | ✅ reliable | actions = self; manner-nouns = "(qualifies) verb"; status/quality = NONE |
| **D5 target** | ⚠ partial | fires via the `HTo` object-marker; plausible but word-order imperfect (Hebrew object can precede verb) |
| **D6 manner (+intensity)** | ✅ reliable | be-perek → manner-of; intensity via me'od/kol |
| **D7 process** | ✅ narrative / ❌ poetry | the escalation chain (afflict→oppress→enslave→embitter) ✓; meaningless across a Proverbs chapter |
| **D8 effect** | ✅ narrative / ⚠ poetry | enslave→bitter ✓; over-fires between unrelated adjacent aphorisms |
| **D9 coupling** | ✅ reliable | morphological weld only (no explosion) |
| **D10 prohibition** (valence remnant) | ⚠ | fires on neg particle by proximity; sometimes over-fires |
| **D11 discovery** | ✅ (separate) | the span-completeness pre-pass (untagged spans) — not in this per-term deriver |
| **D12 hidden** | — dropped | (researcher) |
| **D13 cohabitation** | ✅ implicit | = the passage's co-terms (no separate item) |
| **D14 passage** | ✅ | the consecutive run |

## 2. The narrative win — it works (Exo 1:7-14, the ruthlessness/enslavement)
```
Exo 1:13  ruthlessly (perek, M06)
   D2 source   = dread(H6973)@Exo 1:12        the driver
   D4 operation= (qualifies) work(H5647)
   D6 manner   = manner-of work(H5647)
   D9 coupling = welds work(H5647) as manner
Exo 1:13  work/enslave        D8 effect = bitter(marar,Piel)@Exo 1:14 ; D5 target = lives
D7 process (passage) = enemies → afflict → oppressed → bitter
```
And it **generalised** to other narratives:
- **Gen 4:4-23** (Cain): `D7 process = angry → fell → angry → fallen → cursed`; `desire` → manner-of crouching; `sin` → prohibition ("you must rule over it"). ✓
- **1Sa 1:1-20** (Hannah): `D7 process = provoke → provoke → wept → weep → wept → bitterly`; `provoke` → source=anger. ✓ — the emotional arc comes through.

## 3. The finding that needs YOUR decision — GENRE
The consecutive-run passage is right for **narrative** but **over-groups poetry/wisdom**, where consecutive verses are **independent units**:
- **Pro 15:1-33** — a 33-verse "passage" of unrelated aphorisms. Cross-verse items fire between verses that have nothing to do with each other (`breaks`@15:4 → source=`evil`@15:3; 8 spurious effects). Tightening the window to ±1 verse did **not** fix it — the verses genuinely aren't a unit.
- **Psa 34:1-22** — `process = fear → hate` across 22 verses (meaningless); parallel praise verbs all get effect=magnify.

**The per-verse items (sense, type, seat, operation, manner, coupling) are fine in poetry.** Only the **cross-verse items (D2 source, D7 process, D8 effect)** break — because they assume a connected narrative.

### Options (your call)
1. **Genre-flag passages** — mark narrative vs poetry/wisdom (by book, or a Hebrew accentuation/paragraph signal); run cross-verse items **only in narrative**. *(Cleanest.)*
2. **Poetry = singletons** — in wisdom/poetic books, treat each verse as its own passage regardless of consecutiveness (cross-verse items off).
3. **Require a grammatical cross-verse link** — only fire source/effect when a real syntactic connector spans the boundary (hard; partial).

My recommendation: **(1) or (2)** — a simple book-genre flag (Torah/History = narrative; Psalms/Proverbs/Job wisdom = per-verse) gets 90% of it cheaply, refined later.

## 4. Where it stands
- **Ready:** the per-verse items derive reliably across all genres; the narrative cross-verse movement (the study's core "how the inner being operates") derives correctly and generalises.
- **Needs a decision:** genre handling for cross-verse items (§3) — this is the one real blocker before a batch trial.
- **Known smaller gaps:** D5 target word-order; D3 bearer not derived; D10 prohibition proximity; the AFFECT/VICE cluster set is a seed to firm up.

**Suggested next step after your review:** pick a genre option, then run the batch trial (OQ5 sequence) on a set of narrative passages first (where it's solid), and treat wisdom/poetry per-verse.
