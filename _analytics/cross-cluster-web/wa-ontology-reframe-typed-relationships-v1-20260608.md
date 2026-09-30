# From clusters to typed relationships — ontology reframe (evidence-grounded)

> **Investigation · v1 · 2026-06-08 · CC.** The researcher's reframe after seeing the cross-cluster roll-up:
> the **cluster may not be a real object**; the primary object is **a typed *thing* → its *relationship* →
> what the relationship *does* (its effect)**, and the **differential of impact between one relationship and
> another** is the prize — not the bare fact that things relate. Things have **types** (status vs action …)
> and the type-pair changes the relationship. Grounded in three read-only verse probes
> (`scripts/_assess_relationship_probe.py`). **No DB writes; no architecture changed — this records the reframe.**

---

## 1. The reframe

- **The unit is not the cluster.** Clusters are scaffolding (every cluster touches 40–45 of 45 others; the
  strongest links are non-semantic; labels mislead). The real object is:

  > **THING_A [type] — relationship [effect] → THING_B [type]**, anchored in a verse.

- **The differential is the prize.** "A and B relate" is the weak fact. *What the relationship does*, and how
  the effect of relationship-1 **differs** from relationship-2, is the substance.
- **Things have types, and the type-pair conditions the relationship.** First cut: **status/state** (life,
  death, sin, guilt, forgiveness) vs **action** (repent, atone, love, anger) vs **quality** (living, strong).
  *action→action ≠ action→status ≠ status→status.*

## 2. Evidence — three probes

**Sin × Repentance — STATUS acted on by ACTION, one consistent effect (removal).**
- status side: `a.sham` guilt · `a.von` iniquity · `chat.tat` sin (nouns). action side: `kip.per` atone ·
  `sa.lach` forgive (verbs). Type-mix: Sin STATUS 121/ACTION 25; Repentance ACTION 107/STATUS 13.
- The relationship **does** one thing: the action **removes/covers** the status ("make atonement for [guilt]
  and he shall be forgiven"). A clean **action→status : removal**.
- Note: the cluster labelled "Repentance" is here carrying **atonement/forgiveness** terms — the label
  misleads; the terms-in-relationship are the object.

**Fear × Strength — one cluster-pair, SEVERAL different relationships (the differential, live).**
- `Eph 6:5` authority (`kurios`, status) **evokes** fear ("obey… with fear"). `2Ti 1:7` fear **vs** power
  ("not of fear **but** of power") — **opposition**. `Mat 9:8` fear as **response** to displayed authority.
- So the link **decomposes into evocation / opposition / response** — the same pair holds opposite effects.
  "Fear relates to Strength" is almost contentless; the **relationship-type differential** is the substance.

**Life × Relational — QUALITY-dominant, strong contextually, near-zero semantically** (the 211/0.03 link):
adjectival "living"; co-presence without meaning-overlap.

## 3. What the evidence confirms

1. **Things have types**, readable as a first cut from the **morph** we just backfilled (verb≈ACTION,
   noun≈STATUS, adj≈QUALITY) — *per occurrence* (fear = `fobos` status / `fobeo` action).
2. **Relationship-kind differs by the type-pair** (Sin×Repentance is uniformly status×action→removal;
   Fear×Strength is mixed and multi-typed).
3. **The differential of effect is the object — and it varies even within a single cluster-pair.**
4. **Cluster labels mislead** (M11 "Repentance"→atonement terms; M23 "Strength"→authority/lordship terms).

## 4. Implications for the methodology

- **The finding-unit becomes the typed relationship-with-effect**, verse-anchored:
  `A[type] —rel[effect]→ B[type] @verse`. The **cluster recedes to a scaffold/label.**
- **Co-occurrence (angle 1) is only a candidate-finder.** A "link" **decomposes** into several
  relationship-types via the verse read — that decomposition is the work.
- **Two taxonomies to discover from verses (emergent, not imposed):**
  - **thing-type:** status · action · quality · (likely more — agent, object/recipient, faculty, consequence).
  - **relationship-type / effect:** removal · evocation · opposition · response · sequence · intensification ·
    disposition · substitution · … (discovered, like everything, from the text).
- **Caveat on the morph lever:** POS ≈ type is *rough*. A nominalised action ("repentance", "forgiveness" as
  nouns) is grammatically a status-noun but semantically an action; an adjective can encode a state. Morph
  gives the first cut; the **semantic type needs the verse read.**

## 5. How this lands on what we've built

- The L0 morph backfill is **doubly valuable**: besides sense-resolution (S2), it supplies the **thing-type
  lever** for free.
- The co-occurrence/keyword roll-up stands, but **reinterpreted**: it locates *candidate* relationships; it
  does **not** state what they do. The three link-classes (SAME/RELATIONAL/KIN) are a first sort; the
  **RELATIONAL** class is where the typed-relationship-with-effect work concentrates.
- This refines the study's **third order of output (relationships)** and the **finding-as-universal-unit**
  principle: a finding *is* a typed relationship with an effect.

## 6. Proposed next (read-only, for review before any architecture change)

1. **Decompose a few RELATIONAL links into relationship-types** by reading a wider verse sample (e.g. take
   Fear×Strength's 92 verses and sort them into evocation / opposition / response, with the type-pair each).
   Tests whether the relationship-type taxonomy is tractable and stable.
2. **Draft the thing-type + relationship-type taxonomies** as emergent catalogues seeded from the probes.
3. Only then consider how the finding/record model should carry `type_a`, `relationship`, `effect`, `type_b`.

*The cluster was always scaffolding; this names what it was scaffolding toward — typed things and what their
relationships do.*
