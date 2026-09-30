# Reading-unit reframe: the characteristic cluster as the unit of deep reading

> Design note + John 1 demonstration. Direction set by the researcher (2026-07-19).
> **Provisional — the characteristic/qualifier split (Step 3) is a first pass for
> validation, not a settled call.** Source: `iba.db` (`verse`, `span`,
> `span_candidate`, `candidate_seed.registry_match`).

## The reframe

Today the reading unit is the **passage** = a maximal run of *consecutive* verses
(`verse.passage_id`). The new direction makes the reading unit a **cluster of verses
grouped around a real characteristic** — which need **not be consecutive**, and a verse
may belong to **more than one** cluster. Deep reading then happens *per characteristic*,
over the verses that characteristic actually touches, rather than top-to-bottom over a
block of text.

## The pipeline (4 steps)

1. **Screen out verses with no chars.** No candidate-char span → nothing for the
   inner-being study to read. Set aside.
2. **Screen out verses whose chars are not about a human being.** Two ways a char
   fails this: (a) it is the **divine name / a divine referent** (God, Lord — the
   *arena*, not a human trait); (b) the **verse has no human** at all (human-presence
   screen), so no char in it can be about a human. Set aside.
3. **Distil the surviving chars into two kinds:** the ones that **are a
   characteristic** (a movement/faculty/trait of the inner being) versus the ones
   that **describe or qualify** one (a seat, an expression, a status, a gift, an
   evaluation).
4. **Group verses around each real characteristic** → that cluster is the **unit of
   deep reading**. Qualifiers ride along inside those verses; a verse with two
   characteristics joins two clusters.

## John 1 — the funnel

| Step | Result | Count |
|---|---|---|
| Verses in chapter (IBA set) | — | 50 |
| **1 · no chars** | 3, 4, 8, 9, 20, 21, 22, 24, 25, 27, 28, 30, 35, 41, 44, 45 | **16 out** |
| **2 · chars not about a human** | 1, 2, 5 (no human) · 18, 34, 36, 49, 51 (only "God") | **8 out** |
| **Survive to reading** | 6, 7, 10, 12, 13, 14, 15, 16, 17, 19, 23, 26, 29, 31, 32, 33, 37, 38, 39, 40, 42, 43, 46, 47, 48, 50 | **26** |

So **half the chapter (24 of 50 verses) never reaches deep reading** — it is either
char-free or arena-only. That is the first payoff of the method: it concentrates
effort on the 26 verses that actually carry a human inner-being signal.

## Step 3 — characteristic vs qualifier (survivors)

Grounded in `candidate_seed.registry_match` (the registry word each char matched),
then sorted into the two kinds:

### Real characteristics (4)
| Characteristic | Registry matches | Verses |
|---|---|---|
| **Perception / knowing** | knowledge, understanding | 10, 26, 31, 33, 37, 39, 40, 46, 47, 48, 50 |
| **Faith / trust** | faith | 7, 12, 50 |
| **Volition / desire** | desire | 13, 38, 43 |
| **Moral character** | integrity, deceit, guilt | 23, 29, 47 |

### Qualifiers / describers
| Kind | Registry matches | Verses |
|---|---|---|
| Expression (call / name) | calling, name | 6, 12, 15, 23, 42, 48 |
| Expression (witness) | testimony | 7, 19 |
| Divine gift | grace | 14, 16, 17 |
| Divine agent (Spirit) | holiness (Holy Spirit) | 32, 33 |
| Seat (body / flesh) | flesh | 13, 14 |
| Status (authority) | strength | 12 |
| Evaluation (good) | generosity | 46 |

**John 1's human inner life distils to four characteristics** — *knowing, believing,
willing, moral character* — with everything else acting to express, seat, qualify, or
gift them. Perception dominates (11 of the 26 verses), massed in the disciple-calling.

## Step 4 — the reading units

**UNIT 1 · Perception / knowing** — v10, 26, 31, 33, 37, 39, 40, 46, 47, 48, 50
*(riding qualifiers: the Spirit v32-33, the calling of disciples, "good" v46)*
**UNIT 2 · Faith / trust** — v7, 12, 50 *(riders: name & authority v12, witness v7)*
**UNIT 3 · Volition / desire** — v13, 38, 43 *(rider: "will of the flesh" v13)*
**UNIT 4 · Moral character** — v23, 29, 47 *(sin of the world v29; no deceit v47)*

**Joint verses (belong to two units):**
- **v50** — Perception **+** Faith ("*I saw* you… do you *believe*?"). The climactic
  moment where seeing produces trust.
- **v47** — Perception **+** Moral character ("Jesus *saw*… no *deceit*").

## The residual the method exposes: qualifier-only verses

Eight survivors carry **only qualifier chars, no real characteristic**:
**v6, 14, 15, 16, 17, 19, 32, 42** (e.g. v14 flesh+grace; v16-17 grace; v32 Spirit;
v6/15/42 naming/crying/calling). They pass Screen 2 but anchor no unit at Step 4.
This is a **design decision you need to make:**
- **(a)** attach each to the nearest characteristic unit as context (v32 Spirit → the
  Perception unit; v14-17 grace → wherever grace-received is read), or
- **(b)** treat "qualifier-only" as its own read (what does the expression/seat/gift
  do when no characteristic is named?), or
- **(c)** tighten Screen 2 so a verse must carry a *real characteristic* (not just any
  non-divine char) to survive — which would move these 8 into the screened-out set.

## Design decisions for your steer
1. **Characteristic vs qualifier is provisional.** Biggest calls: is **grace** a human
   characteristic or a divine gift (I put it as qualifier/gift)? Is the **Holy Spirit**
   ever a human char (I put it as divine agent)? Is **authority/"right"** a
   characteristic or a status (qualifier)? Is **"good"** (v46) a moral characteristic
   or a bare evaluation?
2. **Qualifier-only verses** — handle via (a), (b), or (c) above.
3. **Divine-name auto-screen** — should God/Lord (`tag=None`, `ib-judgement`) be
   suppressed as a standing span-level rule, so they never reach Step 3?
4. **Unit granularity** — keep Perception & Understanding as one characteristic, or
   split? Merge Faith into Perception where they co-fire (v50), or keep joint verses
   as explicit links?

## If validated — what operationalizing takes (not yet built)
- A reusable screen/report script (`build_reading_units_<book>_<ch>`) that runs the
  4 steps from the DB and emits the unit list + a residual report.
- A `char_role` classification (characteristic | qualifier) on the char/registry
  layer — the one genuinely new piece of data the method needs.
- A visual: the John 1 heat map recoloured by screen status + reading-unit membership.
