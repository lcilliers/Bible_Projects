# Phase G — party_kind coverage gap (escalation #1598)

## Why this batch exists

Prompted by your question: does the untagged pool matter beyond M-code characteristic tagging?
Checking the live code turned up something the earlier "coverage looks fine" answer (verse-level
check) completely missed: `T4`/`T5`/`T7`/`T8`/`T9` feed two live, deterministic Layer 1 columns —
`is_negator` and `party_kind` — computed on **every** `lexical.build`/`lexical.run` from
`cluster_strong` membership (`iba/app/lib/lexical.py:331-345`). Membership inherits across
same-base variants (a tagged sibling covers the whole base), so I sized the *actual* gap after
accounting for that inheritance rather than the raw untagged-pool count.

**Result: 2,648 of the pool's 2,651 proper nouns have no tagged sibling at all.** Their
`party_kind` computes `NULL` on every build, right now — not a future risk, live wrong output.
The list is dominated by exactly the names you'd expect to matter: David (1,061 occ.), Moses
(759), Saul, Jacob, Aaron, Solomon, Abraham, Joseph, Joshua, Samuel — and one divine-name variant,
`H3069` "YHWH/God" (306 occ.), sitting with zero party classification.

## Method

Not gloss-keyword matching (the method that produced ~20% false positives earlier this
escalation). `strong_meaning_parsed`'s first (lowest sort/id) row for a proper-noun entry is
STEP's own TIP (person/place identity) text, and it carries a structural marker, not just prose:

- `"... living at the time of ..."` / `"only mentioned at ..."` / `"first mentioned at ..."` →
  an **individual** biographical entry (person)
- `"A location ..."` → a **place**
- `"... deity ..."` (any case) → **divine**
- `"An angel called ..."` → **angelic**
- `"People from/who/descended ..."`, `"A group ..."`, `"Ancestors of ..."`, `"Scribal group ..."`,
  `"Combined with ..."`, `"Name of the [Nth] month"`, or a bare etymology gloss
  (`Gilead = "rocky region"`) → **not an individual party** (tribal/collective, calendar, or
  place-etymology entry)

Every one of the 51 items that didn't match any rule was read individually, not sampled — the
full tail is below in "Excluded, verified."

## Counts

| Bucket | Count | Routed to |
|---|---:|---|
| Individual person | 1,594 | T8 (Party-Human) |
| Divine (true God + named pagan deities) | 26 | T7 (Party-Divine) |
| Angelic | 1 (Gabriel, H1403) | T9 (Party-Angelic) |
| **Total in this batch** | **1,621** | |
| Place (real, just not a party candidate — T10-eligible later) | 742 | not included |
| Month names / collectives / tribes / etymology-only / named objects | 51 | not included |
| No `strong_meaning_parsed` row at all — can't classify by this method | 233 | not included, separate follow-up |
| Deferred — genuinely ambiguous | 1 (`H5799` Azazel — STEP itself says "deity/angel") | not included, your call |

## Two corrections made mid-build (both caught before finalizing, not after)

- `H5522` "A **male deity** ... Sikkuth" was initially swept into PERSON because the classifier's
  first version keyed on the bare word "male." Fixed by keying on the word "deity" directly —
  surfaced 26 pagan-deity entries that had been sitting unclassified (Dagon, Bel, Chemosh,
  Nergal, Tammuz, etc.), all now routed to T7 alongside the one true-God variant.
- `H8640` "A **Cushite** king" was missed because "Cushite" wasn't in an early demonym whitelist.
  Fixed by dropping the whitelist approach entirely in favour of the biographical-marker signal
  above, which needs no per-demonym maintenance and also caught a source-data typo ("A **piest**
  living...", `H4641L`) that a whitelist never would have.

## What this does NOT cover

- **233 no-gloss items** — no `strong_meaning_parsed` row exists, so this method has nothing to
  key on. Separate follow-up, not silently dropped.
- **742 places** — real, correctly excluded from this batch (places don't feed `party_kind`;
  T10 is a lower-priority, non-urgent bucket).
- **`H5799` (Azazel)** — STEP's own TIP text calls it "A male deity/angel," a genuine type
  ambiguity, not a lexicon-level fact like the rest of this batch. Your call, not mine.

## To apply

```
python -m iba.app.migration.apply_1598_cluster_batch --payload iba/docs/1598-phase-g-party-gap-classification-v1-20260908.json
```

1,621 inserts (1,594 T8 / 26 T7 / 1 T9). After this lands, a `lexical.run` rebuild over any verse
containing one of these names will produce the correct `party_kind` for the first time.
