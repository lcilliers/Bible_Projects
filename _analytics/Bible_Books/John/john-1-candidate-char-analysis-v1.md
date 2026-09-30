# John 1 — candidate-char analysis (the 57 chars)

> Companion to `span-heatmap-john-1-v1.html` and `john-1-human-presence-screen-v1.md`.
> Focus: the **57 candidate-char spans** of John 1. Restricted to **human-present
> verses** (the screen removes flagged verses 1, 2, 3, 5), then read purely off the
> chars themselves — type, part-of-speech, repetition, adjacency, co-occurrence.
> Source: `iba.db` → `span_candidate` ⋈ `span` ⋈ `verse`.

## 1. The funnel — how many unique chars

| Stage | Spans | Unique (lemma) | Unique (sense-tag) |
|---|---|---|---|
| All candidate-char spans, John 1 | 57 | 25 | 22 |
| In **human-present** verses (drop v1,2,3,5) | 53 | 24 | 22 |
| **Minus the divine name** (God G2316 ×10, Lord G2962 ×1) | **42** | **22** | **21** |

**Headline: ~21 unique inner-being characteristics, in 42 occurrences.**

### The biggest purely-from-the-chars deduction: divine-name contamination
- **14 of the 57 raw chars are the divine name** — `God` (G2316) ×13 and `Lord`
  (G2962) ×1. Every one carries **`candidate_tag = None`** and was seeded by
  **`ib-judgement`**. By the study's own *God-is-arena* rule these are the arena,
  **not** a human inner-being characteristic, and should be screened out at the
  span level (not just the verse level).
- In John 1 the **`ib-judgement` seeder produced *only* the divine name** — no
  genuine IB find. Every one of the 42 real IB chars came from **`registry-direct`**.
  `read-emergent` contributed nothing here. That is a seeder-quality signal worth
  carrying to other chapters.

## 2. Type profile (42 IB chars)

| Type | Spans | Unique lemmas | Members |
|---|---|---|---|
| **Perception / cognition** | 13 | 4 | see/perceive/understand (G1492 ×8), know (G1097 ×2), know (G6063 ×1), hear (G0191 ×2) |
| Moral quality | 7 | 4 | grace (G5485 ×4), good, sin, deceit |
| Spirit / flesh (seat) | 5 | 2 | spirit (G4151 ×3), flesh (G4561 ×2) |
| Speech / vocal | 5 | 5 | voice, cry, cry out, call ×2 |
| Naming / witness | 4 | 2 | name ×2, testimony/witness ×2 |
| Volition / desire | 4 | 3 | will ×2, decide, seek |
| Faith / trust | 3 | 1 | believe/trust (G4100 ×3) |
| Authority / power | 1 | 1 | right/authority (G1849) |

**Perception/cognition dominates (31% of all IB chars).** John 1 is, in its inner-being
vocabulary, a drama of **seeing and knowing** — concentrated in the disciple-calling
half (v31–v50: know, see, saw recur eight times).

## 3. Movement vs seat (part of speech)

- **22 verbs · 19 nouns · 1 adjective.**
- Verbs = the inner being **in motion** (perceiving, believing, willing, seeking,
  calling, crying). Nouns = **faculties / qualities / seats** (grace, flesh, spirit,
  name, testimony, will, voice, sin, deceit, authority).
- The near-even, verb-leaning split fits the *characteristics → movements* frame:
  John 1 shows the inner being **acting** about as much as it names its parts.

## 4. Close to another char — adjacency & co-occurrence

**Adjacent welds** (consecutive word positions — the strongest "close" signal):
- **will + flesh** (v13, "the will of the flesh") — volition seated directly in a
  bodily seat. A volition↔seat weld.
- **voice + one crying** (v23) — a speech doublet ("the voice of one crying out").

**Recurrent pairings across a verse** (co-activation):
- **Perception is the gateway char.** It co-occurs with faith (saw+believe, v50),
  with moral judgement (saw+deceit, v47; good+see, v46), and with itself
  (know+see, v48). Seeing/knowing is what most often triggers a second char.
- **Perception + Spirit** (v33 — see+Spirit adjacent; the verse runs know→see→Spirit
  ×2): a *spiritual-perception* cluster.
- **Faith → name → authority** (v12: believed · name · right): the reception-of-Christ
  chain — trust, in his name, granted authority to become children of God.
- **Flesh → grace** (v14: flesh · grace) — the incarnation hinge (Word became flesh,
  full of grace).

**Repetition = intensity / theme marker:**
- **grace ×4**, clustered v14–17 ("grace upon grace", v16) — the prologue's thematic centre.
- **perception verbs ×13**, spread v10 → v50 but massed in the calling narrative.
- spirit ×3, believe ×3, flesh ×2, will ×2, name ×2, witness ×2.

## 5. Narrative shift in char type

The char *type* tracks the two halves of the chapter:
- **Prologue + Baptist witness (v6–34):** reflective/theological vocabulary — grace,
  flesh, spirit, will, faith, naming, witness.
- **Calling of the first disciples (v35–51):** active vocabulary — perception
  (see/know/saw) and speech (call), as Jesus *sees* Nathanael and disciples *follow*.

## Open calls for validation
- Should the **divine-name spans** (God/Lord, `tag=None`, `ib-judgement`) be
  auto-suppressed as a standing span-level screen, given they are arena not char?
- v3 / v18 human-presence borderlines (see the screen doc) do not affect these 42
  (v3 has no chars; v18's two chars are both `God`, already excluded).
