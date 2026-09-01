# Characteristic-related tables — full inventory across both databases

> Escalation #1007 (adjacent). v2 — supersedes
> [`characteristic-tables-cross-db-inventory-v1-20260901.md`](archive/characteristic-tables-cross-db-inventory-v1-20260901.md)
> (archived). Adds: the programme's own definition of a characteristic, an expanding terminology
> glossary, the real Model A cluster-assignment algorithm (traced to the actual code and its
> session log, not summarised from memory), and your own annotations on what each model was
> actually trying to do and why it didn't finish.
>
> **Framing, stated plainly and not resolved here:** this document is not a decision about what a
> characteristic *should* be. Three prior attempts to distill "the characteristics of the HIB"
> exist, unfinished and unreconciled, plus one abandoned earlier attempt. This is the observation
> stage — the aspects a consistent result will eventually have to deal with: (a) no uniform
> understanding yet of the terminology used to derive and describe results, (b) the methods used
> to reach observations were loosely described and changed over time, producing inconsistencies
> and missed connections between what should have been comparable work.

## Define a characteristic

The programme's own working definition — `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260827.md`,
chapter 1, "Defining Inner Being" (the section `cfg_prose_concept.inner_being_definition` points
to) — verbatim:

> **Inner-being characteristics are the non-physical, internal states, capacities, and expressions
> that constitute a person's invisible life — encompassing how a person thinks, feels, chooses,
> relates, and orients themselves toward meaning, others, and God.**

Explicitly a *working* definition, not a theological claim — "an evaluative filter... a formula
that could be applied to any word in the English language and return a reliable yes-or-no on
whether its meaning qualifies as inner-being content." Three decisions are embedded in it:

1. **Non-physical test** — a bodily process or external behaviour only qualifies when it is
   Scripture's language *for* an internal state (weeping-as-grief qualifies; walking-as-locomotion
   doesn't).
2. **Internal test** — states originating within the person, with the boundary deliberately left
   porous: inner states can be *caused* by external agents (God, other people, spiritual forces)
   without that causation disqualifying them.
3. **Operational range** — thinks, feels, chooses, relates, orients: "not five sealed domains but
   five dimensions of a single integrated life."

Spirit and soul are deliberately held together under "inner being," with the soul/spirit split
itself left as one of the programme's own research questions, not a premise: *"All soulish
characteristics are inner-being characteristics; not all inner-being characteristics are
soulish... Whether a given word belongs primarily to the soul domain, primarily to the spirit
domain, or to the boundary between them is one of the research questions the programme is
designed to answer."* Governing inclusion rule: borderline words are **included, not excluded** —
"the cost of over-inclusion is visible and recoverable; the cost of silent omission is invisible
and not recoverable."

**What this definition does not yet give you** (worth naming, since it's exactly your observation):
a definition of *what counts as one characteristic versus two*, or *how characteristics relate to
each other as a set* — it tells you whether a word is in scope, not how to group, name, or bound
the individual characteristics once several words are in scope together. That is precisely the gap
Models A–C below are three different, unreconciled attempts to close.

## Terminology (growing list — add to this as it's used)

| Term | As used in this study |
|---|---|
| **inner-being characteristic** | The programme's own filter-concept, defined above — what qualifies a word for the registry at all. |
| **HIB** | Human Inner Being — a named or implicit *human* narrative subject (`iba.db hib`). By explicit rule, a non-human being can never be registered as a HIB. |
| **phenomenon** | IBA's live term for a characteristic *in operation* — one HIB's state/disposition, evidenced in one verse (`iba.db phenomenon`). Not a catalog entry; a per-occurrence reading. |
| **operation** | The movement/behaviour registered against one phenomenon — what it does, where it comes from, where it goes (`iba.db operation`). |
| **cluster** | A top-level thematic grouping, keyed on an M-code (or T2/T3/FLAG) — the coarsest grain in both databases. |
| **cluster_code** | The stable string key for a cluster (e.g. `M04`, `T3`, `FLAG`) — shared vocabulary between `bible_research.db` and `iba.db`, migrated once, not live-synced. |
| **characteristic** (Model A sense) | A named, hand-defined trait belonging to a cluster — an abstract catalog entry, not tied to a verse (`bible_research.db characteristic`). |
| **family** (Model B sense) | `ib_characteristic`'s own grouping concept — e.g. `humility-lowliness-contrition` — derived **by book**, not by cluster. |
| **cluster_subgroup / characteristic_subgroup** | An abandoned attempt at sub-dividing a cluster into finer groupings — built on **lemma**, not **span** (your account) — 17/49 clusters only. |
| **T2 (Supplementary)** | Strong's codes assigned to a cluster process but carrying no inner-being relation — the clean "not IB" bucket. |
| **T3 (Operations)** | Strong's codes for a human operation/movement (see, give, make, take, bow, look…) not tied to one cluster, OR that apply across many — "not by definition HIB related, but could be related to the meaning" at verse level (your framing). Distinct from T2: T3 is IB-adjacent action, not IB-absent. |
| **FLAG** | Flagged for review — deliberately rare, never assigned from its own worked-example gloss list (that list is an uncertainty bag, not a signal). |
| **HIGH / MEDIUM / LOW** | Confidence tiers from the Model A cluster-allocation process (below) — HIGH = automatable precedent match, MEDIUM/LOW = judgment-tier, researcher/LLM-reviewed. |
| **edge (T3 + one cluster)** | A rare pairing where an operation is tagged T3 but still carries a likely cluster — not the default; most operations either belong cleanly to one cluster or go fully to T3. |
| **descriptor** | A T2 item that reads as inner-being content but "pairs with something else and is rarely analysed alone" (beauty, courage, mockery, comfort…) — deliberately left in T2 unless it has a direct single-cluster relation. |

---

## Inventory

| Table | DB | Rows | Grain — one row per… | Status |
|---|---|---|---|---|
| `cluster` | bible_research | 49 | top-level thematic cluster (M-code, or T2/T3/FLAG) | live |
| `characteristic` | bible_research | 277 | a named trait belonging to a cluster (catalog entry) | live, partial (35/49 clusters) |
| `characteristic_subgroup` | bible_research | 146 | characteristic ↔ cluster_subgroup link | live, abandoned mid-way |
| `cluster_subgroup` | bible_research | 175 | a sub-division of a cluster | live, partial (17/49 clusters), lemma-based |
| `cluster_observation` | bible_research | 276 | a write-on-discovery note against a cluster/characteristic | live |
| `cluster_finding` | bible_research | 19,997 | a catalogue-prompted finding against a cluster/characteristic | **inactive** — migrated into `finding` |
| `finding` (level=`CLUSTER`) | bible_research | 21,898 (17,662 with `characteristic_id`) | the live successor of `cluster_finding` | live |
| `ib_characteristic` | bible_research | 1,634 | a distinct sense of a Hebrew lemma, as read in one book | live, narrow (Psalms + Proverbs only) |
| `ib_characteristic_legacy` | bible_research | 29 | superseded pre-meaning-keyed version of the above | frozen backup |
| `hib` | iba | 63 | a Human Inner Being identified in a book's scope | live |
| `verse_hib` | iba | 485 | a HIB present/candidate in one verse | live |
| `hib_referent_option` | iba | 5 | one candidate referent-reading for an ambiguous HIB | live, minimal |
| `phenomenon` | iba | 177 (121 live) | a HIB's characteristic/state/disposition in one verse — **this is what IBA calls a phenomenon** | live, narrow (Daniel only) |
| `operation` | iba | 177 (121 live) | the movement/behaviour registered for one phenomenon | live, narrow (Daniel only) |
| `operation_party` | iba | 250 | one source/target of an operation | live, narrow (Daniel only) |
| `cluster` | iba | 51 | top-level thematic cluster — migrated copy of bible_research's | live |
| `cluster_strong` | iba | 7,609 | a Strong's code assigned to a cluster | live |
| `wa_dimension_index` | bible_research | 3,509 | a verse_context_group's assignment to one of 20 retired "dimensions" | **retired** |
| `ve_dimension_scoreboard` | bible_research | 18 | rule-validation verdict for one of 18 VE-lexical dimensions | **retired**, all FAILED/IN-PROGRESS |
| `wa_dim_review_cluster_log` | bible_research | 6 | a completed dimension-review pass over one C-code cluster | **retired**, 6/22 ever finished |
| `wa_session_b_dimensions` | bible_research | 2 | a Session B per-word dimensional flag | **retired**, abandoned near-immediately |
| `prose_section_dimension_link` | bible_research | 0 | declared prose↔dimension link | **retired**, never used |

---

## Model A — the cluster (`cluster` → `cluster_strong`/`characteristic`)

**What it is.** All Strong's codes split into ~47 named inner-being groups (48 `M`-coded rows,
counting `M10`/`M10b`/`M10c` as one thematic slot and no `M40`), plus **three** non-IB codes —
not two, correcting v1's oversimplification: **T2** (Supplementary — no inner-being relation at
all), **T3** (Operations — a human action/movement not tied to one cluster, but still potentially
meaning-relevant at verse level, your point exactly), and **FLAG** (rare, genuinely undetermined).

**The actual assignment logic — traced to the real code, not summarised from memory.**
`iba/app/lib/clusterassign.py` implements the one deterministic tier of a documented, reusable
method (`iba/docs/cluster assignment process/wa-global-cluster-alloc-sessionlog-v1_0-20260811.md`,
the 1,612-Strong's-code allocation pass of 2026-08-11):

- **Evidence used: `strong.stepGloss` (English gloss) + transliteration + frequency count only —
  no verse layer at all.** Explicit caveat in the session log itself: *"Clusters remain a
  convenience of arrangement, not a claim about the inner-being system."*
- **Three precedent signals**, each an *exact* (not substring) gloss/translit match:
  **P1** — the gloss already matches an existing `cluster_strong`-labelled Strong's.
  **P2** — the gloss exactly matches a term in `cluster.gloss`'s own worked-example list.
  **P3** — the *transliteration* matches a `cluster.gloss` term (demoted to review, not automated
  — Hebrew/Greek homographs like *nasa* collide across senses).
- **Confidence tiers:** **HIGH** = a single-cluster P1/P2 match (`clusterassign.py`'s own scope —
  the only tier ever auto-applied without a researcher decision). **MEDIUM** = precedent-conflict
  or a profile-score suggestion — accepted by the researcher as "a likely bucket... not a final
  decision." **LOW** = no precedent at all — resolved by a manual semantic pass (operation→cluster-
  or-T3; non-operation→IB-cluster only where the gloss transparently denotes IB, else T2).
- **A TF-IDF "profile" scorer was tried for HIGH and explicitly rejected** — too noisy on short
  glosses (mis-fired "brother"→Deceit; missed "to sanctify" on zero token overlap). Kept only as a
  sorting aid for the MEDIUM pile, never a decision-maker.
- **The T3 edge rule** (evolved through debate, then corrected by the researcher): a verb with a
  *direct* meaning-relation to a cluster stays in that cluster (to love → M05, not T3); **T3 is
  only for operations whose cluster genuinely can't be determined, or that apply across many** —
  "edge" (tagged T3 but still carrying a likely cluster) is rare, not a default.
- **Known pitfalls, recorded so a future pass doesn't repeat them:** the `FLAG` gloss list is an
  uncertainty bag, never a positive signal for voting; substring matching creates false positives
  (`ill` inside k**ill**/f**ill**); a Strong's code can legitimately carry more than one prior
  cluster row (must iterate per instance, not per code, or 21 get silently dropped); seat words
  (heart/soul/spirit/mind/flesh/conscience) always → `M47`, never `T2`.
- **Result of that one pass** (1,612 codes): T2 522 · T3 291 · IB clusters 790 · FLAG 9.

**What Model A never finished — your account.** `cluster_subgroup`/`characteristic_subgroup` were
an attempt at sub-dividing a cluster into finer groupings (only 17/49 clusters ever subdivided),
abandoned because the sub-grouping was built on **lemma**, not **span** — consistent with the live
data (`cluster_subgroup` rows are hand-authored labels/descriptions, e.g. M06 split into
Hatred/Contempt/Abhorrence/Cruelty/Reproach, with no span-level grounding visible in the row
itself). **If revisited, this sub-group mechanism could become the actual basis for characteristic
groupings** — which would mean the characteristic questions can only be properly analysed *after*
every cluster has gone through sub-grouping, and the subgroup data itself would need re-deriving
against the current lexicals, since the prior lexicals it was built on "had fundamental flaws"
(your words) — not merely re-labelled, re-derived.

## Model B — the meaning-keyed index (`ib_characteristic`)

**What it was for.** The work to reset the meaning so characteristics could be better determined —
your framing. Its grouping concept was called **`family`** (e.g. `humility-lowliness-contrition`),
distinct from Model A's `cluster`/`characteristic`. Real example:

```
code='psa-H0034-needy'   name='needy'   family='humility-lowliness-contrition'
  cluster='M24' cluster_all='M24(Weakness)' instance_count=8
```

**The key difference, and the mistake, in your account.** Model B was derived **by book**, not by
cluster (or by grouping similar Strong's together) — encouraging in its depth (real `stems`,
`morph_codes`, `esv_words`, `lexical_gloss`, `key_span_id` columns, grounding it closer to the
actual lexical data than Model A's hand-written definitions), but scoping the work by book meant
it never covered more than Psalms and Proverbs, and the organising axis itself may need
re-orienting — your open question, not resolved here.

## Model C — the live debate pipeline (`hib` → `phenomenon` → `operation`)

**Why it exists at all — your framing.** Conceptualised after recognising that the human being
does not consist of a *catalogue* of characteristics (Model A's premise) but that a HIB has
**phenomena that are characteristics in operation** — in a way that blurs the boundaries between
individual characteristics rather than sorting cleanly into named slots. This is the conceptual
break from Models A and B, not an incremental refinement of either.

Verified worked example, Dan 1:8 ("Daniel resolved that he would not defile himself…"):

```
hib id=47 label='Daniel' kind='named_individual'
phenomenon id=100 hib_id=47 verse_id=13044
  description: "Daniel's own deliberate resolve of will not to defile himself with the
  king's food and wine — a fixed inner purpose, not a passing preference."
operation id=159 phenomenon_id=100 process='emerge'
  operation_party: source(kind='self'), target(kind='object_situation', detail="the king's food and wine")
```

No `short_name`, no catalog entry, no `cluster_code` anywhere in this chain — a phenomenon is
identified by free-text description against one HIB in one verse, not named from a controlled
vocabulary the way Model A's `characteristic.short_name` is. Richest design, narrowest coverage:
**121 live rows, one book (Daniel).**

## Model D (retired) — the "dimension" layer

A very early experimental stage — your own assessment, and consistent with what the live data
shows: five tables (`wa_dimension_index`, `ve_dimension_scoreboard`, `wa_dim_review_cluster_log`,
`wa_session_b_dimensions`, `prose_section_dimension_link`), every one explicitly marked retired,
one (`ve_dimension_scoreboard`) recording that every dimension it tracked FAILED or was
IN-PROGRESS and never passed. Set aside, not carried into any of the analysis below.

---

## What does NOT connect

- **No foreign key or shared surrogate key between Model A, B, or C.** `characteristic.id`,
  `ib_characteristic.id`, and `phenomenon.id` are independent sequences; neither Model A nor Model
  B references the other's id or code, even though both live in `bible_research.db`.
- **`cluster_code` is the one shared vocabulary**, and even that's asymmetric: Model A's 49
  clusters are the source; Model B's `cluster`/`cluster_all` columns and `iba.db`'s own
  `cluster`/`cluster_strong` (migrated once, 2026-08-11) both reference the same code strings, with
  nothing to notice if the two files drift.
- **Coverage doesn't overlap enough to cross-check**: Model A spans 35/49 clusters programme-wide;
  Model B is Psalms+Proverbs only; Model C is Daniel only.

## What this means for the catalogue `source` work

None of these three "characteristic" tables is a raw-data `source` for the tier-catalogue's
characteristic-focused buckets the way `verse_lexical`/`strong_meaning_parsed` are — they hold
researcher-authored analytical content (Model A's hand-written definitions and gloss-only cluster
allocation, Model B's book-scoped meaning index, Model C's per-verse debate reading), not base
data. Where a question in those buckets is answerable at all, the right `source` framing names
which analytical layer it draws on and says so plainly, rather than implying it's a database
lookup the way the lexical-layer statements are.
