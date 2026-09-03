# Word/term (lexical) scope — reclassification review

> Escalation #1007. Applying your instruction (2026-09-01): the `Word/term (lexical)` bucket in
> [`1007-tier-catalogue-scope-focus-v3-20260831.md`](1007-tier-catalogue-scope-focus-v3-20260831.md) should
> only hold questions that are Strong's/meaning/span/term related **or derived** — i.e. the
> question's own subject is a lexical fact (a term, its meaning, its span/occurrence, its
> grammar). Questions that explore the **characteristic itself** move out — to
> `Characteristic (behaviour)` (how it behaves) or a new `Characteristic (what it is)` bucket
> (its identity/nature), per your framing.
>
> Worked through all 16 current members below. Most are clean either way. Two are not — they name
> "the characteristic" as the actual subject of the claim (not just using lexical data as
> evidence), and don't fit either of the two destinations you named. Flagged rather than assumed.
> **Nothing has been changed in the live doc or the DB `scope` column yet — this is the proposal.**

## Stays in Word/term (lexical) — 11

The question's own subject is the term/vocabulary itself: what it is, what it means, what forms
or vocabulary exist for it. Even where the question closes with "what does that show," what's
being shown is itself a lexical-level fact (a meaning, a semantic range), not a claim about the
characteristic's identity or behaviour.

| Code | Question | Why it stays |
|---|---|---|
| `T1.1.2` | What do the primary Hebrew and Greek terms show at the definitional level? | Directly a term/meaning fact. |
| `T6.4.1` | Which vocabulary terms does this characteristic share with others? | Computed from `cluster_strong`/`strong_related` — term-sharing fact. |
| `T6.4.2` | Does the sharing extend to root-level architecture? | Root-sharing fact, same basis. |
| `T7.1.1` | What are the primary terms, and what do their root meanings show? | Term + root-meaning fact. |
| `T7.1.3` | What is the semantic range of the primary term? | Semantic range is itself a lexical concept (`strong_meaning_parsed`/sense tree). |
| `T7.1.4` | Does the vocabulary distinguish disposition/act, received/given, condition/quality? | Vocabulary-existence fact. |
| `T7.1.5` | Does the vocabulary include a term for the structural opposite? | Vocabulary-existence fact. |
| `T7.1.6` | Does the vocabulary include a person-type term? | Vocabulary-existence fact. |
| `T7.1.7` | Does the vocabulary include a supplication/seeking term? | Vocabulary-existence fact. |
| `T7.1.9` | Is there a term newly coined in the NT period? | Still fundamentally about a term's existence, even though not DB-derivable. |
| `T7.1.10` | What does the full vocabulary arc show about the complete semantic range? | "Semantic range" is a linguistic-scope concept even in aggregate — leaning stays, but see flag below; this one is close to the line. |

## Moves to `Characteristic (what it is)` [new bucket] — 3

The question's subject is the characteristic's own identity/nature — the term data (name, root
meaning) is the *evidence*, but the claim being asked for is about the characteristic, not the
term.

| Code | Question | Why it moves |
|---|---|---|
| `T1.1.1` | What is the characteristic called, and what does the name signal about its essential nature? | "Essential nature" is a characteristic-identity claim. The name itself is `word_registry.word` (registry data, not lexical), and what it *signals* is interpretive synthesis, not a term fact. |
| `T1.1.3` | What directional, relational, or constitutional implication does the name carry? | Same pattern as `T1.1.1` — a claim about the characteristic's constitution, using the name as evidence. |
| `T7.1.8` | What does the OT/NT vocabulary relationship show about continuity or development *of the characteristic* across the Testaments? | Names "the characteristic" as the thing under discussion — a continuity/identity claim over canonical history, not a vocabulary-existence fact. |

## Flagged — doesn't fit either named destination — 2

| Code | Question | The problem |
|---|---|---|
| `T6.4.3` | What does the vocabulary sharing show about the **conceptual relationship between the characteristics**? | This is explicitly relational — it matches the existing `Characteristic relational` bucket's own definition (used to justify moving `T6.4` here from relational in the first place) better than either `behaviour` or `what it is`. Recommend: **`Characteristic relational`**, not the two you named — but flagging since you didn't mention that bucket as a destination this round. |
| `T7.1.2` | What is the grammatical range of the primary term, and what does that range show about **how the characteristic operates**? | Grammatical range itself is a lexical fact (`verse_lexical.morph_code`), but "how the characteristic operates" is explicitly a behaviour claim — same shape as the `T6.4.3` problem. Recommend: **`Characteristic (behaviour)`**. |

## Net effect if the two flags are resolved as recommended

- `Word/term (lexical)`: 16 → **11**
- `Characteristic (what it is)` [new]: **3**
- `Characteristic relational`: +1 (`T6.4.3`) → 17 → 18
- `Characteristic (HIB behaviour)`: +1 (`T7.1.2`) → 15 → 16

## What to confirm before I write anything

1. `T6.4.3` → `Characteristic relational` (not one of your two named buckets) — agree, or somewhere else?
2. `T7.1.2` → `Characteristic (behaviour)` — agree?
3. The new bucket's exact label — I used `Characteristic (what it is)` as a placeholder matching your own phrasing; confirm or give the label you want it to carry in the doc/DB.
4. `T7.1.10` — flagged as borderline in the stays-list itself; leave in lexical, or move to `what it is` alongside `T7.1.8`?
