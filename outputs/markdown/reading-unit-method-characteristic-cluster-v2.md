# Reading method v2 — the growing Inner-Being Concordance

> Supersedes / extends `reading-unit-method-characteristic-cluster-v1.md`.
> v1 gave the **front-end**: screen a chapter → distil chars → group verses into
> characteristic clusters. v2 adds the **back-end the researcher asked for
> (2026-07-19):** a persistent, progressively-growing **concordance of the inner
> being** that every chapter reading draws from and writes back to — so learning
> persists, discovery is cumulative, and lexical analysis is retained as a
> deliverable. **Design proposal for discussion — nothing built.**
>
> **Refinement (2026-07-19, same day):** grain **decided = per meaning-in-context**
> (not per registry word). Two additions folded in below — how the concordance handles
> the fact that **many Strong's flow into each other** (§ The Strong↔sense flow), and a
> **no-near-duplicates consolidation discipline** (§ Consolidation), which also governs
> collating past findings in.

## The principles this must honour (researcher, 2026-07-19)

1. **Progressive learning & discovery, not stereotyping.** John 1's "4 characteristics"
   are *evidence from one chapter*, never a template to stamp onto the rest of the
   Bible. Every chapter is screened and distilled afresh from its own text; new
   characteristics may emerge anywhere.
2. **Learning must persist.** When an assessment needs adjustment (and it will), the
   correction is captured and carried forward — it changes how the next reading is
   done, rather than being lost in chat.
3. **A concordance of the inner being that grows.** The persistent home of everything
   learned about each characteristic, taken further with each chapter.
4. **Prior findings visible on re-read.** When we read the 4 characteristics in John 1,
   and later meet them again in John 3, the accumulated concordance entry is *in view*.
5. **Lexical analysis is retained** — built in as one of the deliverables of reading a
   chapter, not discarded in favour of the new segmentation.

## The shift in one line

**v1:** the reading unit is a characteristic cluster *within a chapter*.
**v2:** the reading unit is a characteristic cluster, read **against that
characteristic's entire prior concordance** — and its reading **grows the concordance**.
The chapter is where reading happens; the **concordance is where knowledge lives.**

## What the concordance is (one entry per characteristic)

The IBA db today has **no reading/output layer** — only inputs (spans, candidates,
lexicon, the 178-word registry). The concordance is that missing layer. Each entry —
keyed on a characteristic (meaning-in-context, linked to the registry word where one
fits) — accumulates five things:

| Facet | What it holds | Grows by |
|---|---|---|
| **Working definition** | the characteristic's sense as currently understood; status *emerging / established / under-revision* | revised as evidence accrues |
| **Occurrences** | every verse + span where it was read (a true concordance list) | one per reading |
| **Findings** | observations about what it *does* — movements, associations, seats, expressions, tensions | appended; **adjustments are new revisions, never overwrites** |
| **Lexical profile** | the lemmas / Strong's / senses / morphology that realise it, with glosses | ← the lexical deliverable, folded in per chapter |
| **Relations** | links to other characteristics — co-occurs / welds / triggers / opposes (e.g. perception→faith at Jn 1:50) | one per observed pairing |

**Persistence of learning lives in "Findings" + "Definition":** a correction is a
*revision record* that supersedes but does not erase its predecessor, so the reasoning
trail survives and the current view is always the latest revision.

## The reading loop (v2) — per characteristic cluster

The v1 four-step screen still runs first (no-chars → not-about-human → distil →
cluster). What changes is what happens **inside each cluster**:

```
for each characteristic cluster in the chapter:
  1. LOAD  its concordance entry — definition, prior findings, lexis, relations.
  2. READ  the new verses FRESH for their own witness (find the gems; the prior
           entry must NOT pre-decide what the text says).
  3. RECONCILE the fresh read against the entry: confirm / extend / adjust /
           contradict — each becomes a finding (adjustments as revisions).
  4. LEXICAL analysis of the cluster's spans (the retained discipline) → the
           ve-lexical dimensions + the entry's lexical profile.
  5. WRITE BACK occurrences, findings, lexis, relations. The entry is now richer.
```

Step 2-before-1-informs-2 resolves the tension with *"read each chapter as if the
first"*: the **text** is read fresh; the **concordance** enters only at reconciliation,
as the thing the fresh reading confirms or revises.

## "What comes out, and how it's captured" (your open question)

**Out of reading one chapter:**
- a **screen record** per verse (kept / screened + why) — the funnel is auditable;
- per characteristic cluster: **new occurrences**, a **fresh reading reconciled to prior
  findings**, a **lexical analysis** (dimensions + realisations), and any **relations**;
- a chapter roll-up: which characteristics were present, which **emerged new**, which
  were **adjusted**.

**Captured as:** updates to the concordance entries (the five facets), with findings and
definitions **versioned** so adjustments persist. Nothing important lives only in chat
or in a one-off document.

## Worked shape — "Perception / knowing" across John

- **After John 1:** definition ≈ *the inner act of seeing/recognising that opens onto
  trust*; occurrences v10, 26, 31, 33, 37, 39, 40, 46, 47, 48, 50; findings incl.
  *"perception is the gateway char — it co-fires with faith (v50) and moral discernment
  (v47)"*; lexis {G1492 see/perceive, G1097 know, G0191 hear}; relations
  perception→faith, perception→moral-character.
- **Reading John 3 next:** the entry is loaded first. "You must be *born again*… we
  speak of what we *know*" (Jn 3) is read fresh, then reconciled — does perception still
  gate faith? Does Nicodemus' *not-knowing* extend the definition (perception's
  failure)? New lexis/senses fold in; the entry is *taken further*, not restarted.

That progression — same characteristic, deeper each chapter — is the whole point.

## Progressive, not stereotyping — the guardrails

- Each chapter **re-runs the screen from its own text**; the concordance never
  pre-selects verses.
- The **char-vs-qualifier classification is itself a concordance output**, revisable:
  grace / Spirit / authority were provisional in v1 — after N more chapters the evidence
  may re-judge them, and that judgement is stored, not hardcoded.
- **New characteristics emerge freely**; the 178-word registry is a starting index, not
  a closed set.

## Where it lives & prior art

- A new **concordance layer in the IBA db** (characteristic entry · occurrence · finding
  [revisioned] · lexis · relation). Designed to grow; no chapter's shape is baked in.
- **Prior art to reuse, not reinvent:** the main `bible_research.db` already has
  `ib_characteristic` (keyed on meaning-in-context) and `ve_lexical` (the dimension
  store). The concordance is the IBA-native, growth-first realisation of that idea; the
  lexical deliverable should reuse the ve-lexical dimension discipline rather than a new
  scheme.

## The Strong↔sense flow — the hard problem, and how the concordance absorbs it

The data proves the flow runs **both ways** (`strong_meaning_tree`):
- **One Strong → many senses:** `G1492` bundles *"know / recognise / realise /
  possess-information"* in a single lexicon entry.
- **Many Strongs → one sense:** five different lemmas all collapse to *"strife,
  contention"*; four to *"strength"*.

So **a Strong's number can never be the unit of identity** — it is too coarse in one
direction and too fragmented in the other. The resolution is to stop asking Strongs to
carry boundaries at all, via a **three-layer model:**

1. **Occurrence (facts).** Each read span → `(verse, Strong, morph, lexicon-sense-code,
   meaning-in-context judged from the verse)`. The Strong is just *one attribute* of an
   occurrence, never its key.
2. **Concordance entry (identity = meaning-in-context).** An entry gathers occurrences
   that share a meaning-in-context. It therefore links to **many Strongs** (as
   evidence), and any one Strong appears in **many entries** — a clean many-to-many,
   mediated by the occurrence layer, with **no forced partition of Strongs**.
3. **Neighbourhood (soft edges).** Entries connect to *adjacent* entries by
   **"flows-into / borders"** edges — a graph, not a merge. `perceive-recognise` borders
   `perceive-understand` borders `discernment`.

**Why this dissolves your unknown:** "many Strongs flow into each other" is only a
problem if a Strong defines a boundary. Here it never does — identity is the
meaning-in-context, evidenced by (not defined by) Strongs, and the *flow itself is
recorded as a border edge* rather than forcing a decision. `strong_meaning_tree` (which
already fans a Strong into senses and already shows cross-Strong sense-sharing) becomes
the **scaffold** that proposes the initial neighbourhood graph — not the authority over
meaning-in-context.

## Consolidation — no near-duplicates (and how past findings collate in)

Fine grain (meaning-in-context) *will* generate near-duplicate entries — two readings of
"perceive that recognises" phrased slightly differently. The discipline, applied on
**every write, including migrating legacy findings in:**

1. **Match on write.** Fingerprint the proposed entry (registry word + Strong set +
   lexicon sense-codes + gloss terms) and search existing entries; surface near-matches.
2. **A *considered* decision — never silent** (you said these "need to be considered"):
   **attach-as-evidence** to an existing entry · **merge** two entries · or **keep
   distinct but link as neighbour**.
3. **Merge =** union of occurrences / lexis / relations; findings combined with the
   revision trail; the losing entry becomes an **alias / redirect** (never deleted — old
   citations still resolve).
4. **"Keep distinct + neighbour link" is the release valve.** When two senses are close
   but you're *not ready to decide*, record a border edge instead of forcing the call —
   then revisit. This is exactly the answer to "I don't yet know how to deal with that":
   **you don't have to decide up front; you record adjacency and consolidate later.**
5. **Periodic consolidation pass** over tight neighbourhoods (researcher, or an LLM judge
   proposing) — continuous, not one-time. This is where progressive learning tightens the
   concordance over time.

**The key insight: de-duplication and the Strong-flow are the same mechanism** — both
are handled by identity-as-meaning-in-context + soft neighbour edges + a considered
merge/attach/link decision + periodic consolidation. You never have to get the
boundaries right first; the structure lets them stay provisional and improve.

## Open questions for you

1. ~~Grain of an entry~~ — **decided: per meaning-in-context.**
2. **Fresh-vs-prior** — is "read fresh, reconcile after" the right guard, or do you want
   prior findings visible *during* the read?
3. **Lexical deliverable depth** — full ve-lexical dimensions per cluster, or a lighter
   per-characteristic lexical profile to start, deepening later?
4. **Who runs consolidation** — you decide every merge, or an LLM judge proposes and you
   approve the non-obvious ones?
5. Scope of first build — model the concordance on **John only** (chs 1–3) to test growth
   *and* the consolidation loop before touching other books?
