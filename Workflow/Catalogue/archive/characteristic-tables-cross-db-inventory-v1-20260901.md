# Characteristic-related tables — full inventory across both databases

> Escalation #1007 (adjacent). Every table in `bible_research.db` and `iba.db` that represents,
> classifies, or links to an inner-being **characteristic** — what IBA itself calls a
> **phenomenon**. Not one mechanism duplicated in two places: **three genuinely distinct models**,
> from three different eras, plus one fully retired fourth. None of the three live ones is bridged
> to either of the others — no foreign key, no shared surrogate key. The only thing they share is
> the `cluster_code` label vocabulary (M01–M47, FLAG, T2), and even that is a one-time migrated
> copy in `iba.db`, not a live sync.

## Inventory

| Table | DB | Rows | Grain — one row per… | Status |
|---|---|---|---|---|
| `cluster` | bible_research | 49 | top-level thematic cluster (M-code) | live |
| `characteristic` | bible_research | 277 | a named trait belonging to a cluster (catalog entry) | live, partial (35/49 clusters) |
| `characteristic_subgroup` | bible_research | 146 | characteristic ↔ cluster_subgroup link | live |
| `cluster_subgroup` | bible_research | 175 | a sub-division of a cluster | live, partial (17/49 clusters) |
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
| `cluster` | iba | 51 | top-level thematic cluster (M-code) — migrated copy of bible_research's | live |
| `cluster_strong` | iba | 7,609 | a Strong's code assigned to a cluster | live |
| `wa_dimension_index` | bible_research | 3,509 | a verse_context_group's assignment to one of 20 retired "dimensions" | **retired** |
| `ve_dimension_scoreboard` | bible_research | 18 | rule-validation verdict for one of 18 VE-lexical dimensions | **retired**, all FAILED/IN-PROGRESS |
| `wa_dim_review_cluster_log` | bible_research | 6 | a completed dimension-review pass over one C-code cluster | **retired**, 6/22 ever finished |
| `wa_session_b_dimensions` | bible_research | 2 | a Session B per-word dimensional flag | **retired**, abandoned near-immediately |
| `prose_section_dimension_link` | bible_research | 0 | declared prose↔dimension link | **retired**, never used |

---

## Model A — bible_research.db, the M-code catalog (`cluster` → `characteristic`)

**The abstract type, not a per-occurrence token.** `characteristic` holds a *named trait with a
prose definition*, scoped to a cluster — not tied to any specific verse or Strong's code. Real
example (M04, Exultation/Excitement's cluster):

```
id=1  cluster_code=M04  char_seq=1  short_name='Exultation'
  definition: "The soul's active, surging, triumphant inner state directed at what is
  glorious or transcendent — above all at God. ... Distinguished from Joy by intensity
  and directedness..."
id=2  cluster_code=M04  char_seq=2  short_name='Joy'
id=3  cluster_code=M04  char_seq=3  short_name='Gladness'
```

Three sibling traits, hand-defined and hand-distinguished from each other in prose — this is a
**taxonomy of concepts**, built top-down. `characteristic_subgroup` links a characteristic to the
`cluster_subgroup`(s) that carry it (near 1:1 in practice — 145 distinct sub-groups over 146 rows).
`cluster_observation` and `cluster_finding` (now migrated into `finding`, level=`CLUSTER`) are
where evidence and notes get attached back to a `characteristic_id` — `finding`'s own numbers
confirm this: 17,662 of its 21,898 `CLUSTER`-level rows carry a `characteristic_id`; **zero**
`VERSE` or `GLOBAL`-level findings do — this linkage is cluster-scoped by design, never used at
the individual-verse grain.

**Coverage:** only 35 of 49 clusters have any `characteristic` row at all (53 backfilled from
sub-groups, 78 added later as explicitly provisional exemplars); only 17 of 49 have a
`cluster_subgroup`.

## Model B — bible_research.db, the meaning-keyed index (`ib_characteristic`)

**A different grain again — not the abstract type, not a per-verse token, but a per-*sense*-per-*book* aggregate.** Real examples:

```
code='psa-H0034-needy'      name='needy'      family='humility-lowliness-contrition'
  cluster='M24' cluster_all='M24(Weakness)' instance_count=8
code='psa-H0014-submit'     name='submit'     family='humility-lowliness-contrition'
  cluster='M29' cluster_all='M29(Desire)' instance_count=1
```

One row = one distinct English reading of one Hebrew lemma, as it actually occurs across a book
— `H0034` ("needy") gets its own row keyed `psa-H0034-needy`, aggregating all 8 of its Psalms
occurrences into `instance_count=8`, with columns for `stems`, `morph_codes`, `esv_words`,
`lexical_gloss`, `key_span_id` — a genuine attempt at grounding characteristics in the actual
lexical/span data, built directly in `bible_research.db` before `iba.db` existed. **Confined to
Psalms (877 rows) and Proverbs (757 rows) only** — never extended further. `ib_characteristic_legacy`
(29 rows) is its own frozen predecessor, richly hand-authored (`gist`, `colour_range`, `junctions`,
`open_questions` all populated) in a shape the live table declares but leaves 100% NULL — the two
tables represent two different design iterations of the *same* idea, not a current/historical pair
that stayed in sync.

## Model C — iba.db, the live debate pipeline (`hib` → `phenomenon` → `operation`)

**This is what "IBA calls phenomena."** The genuine per-occurrence token: one `phenomenon` row per
HIB per verse per passage. Verified worked example, Dan 1:8 ("Daniel resolved that he would not
defile himself…"):

```
hib id=47 label='Daniel' kind='named_individual'
phenomenon id=100 hib_id=47 verse_id=13044
  description: "Daniel's own deliberate resolve of will not to defile himself with the
  king's food and wine — a fixed inner purpose, not a passing preference."
  textual_warrant: '"Daniel resolved [...H7760A sim ... H3820A leb...]"'
  status='stated'
operation id=159 phenomenon_id=100 process='emerge'
  operation_party: source(kind='self', detail="Daniel's own will/resolve"),
                   target(kind='object_situation', detail="the king's food and the wine")
```

No `short_name`, no catalog entry, no `cluster_code` anywhere in this chain — a phenomenon is
identified **by free-text description against a specific HIB in a specific verse**, not named from
a controlled vocabulary of characteristics the way Model A's `characteristic.short_name` is. This
is the richest, most current design (real textual warrant, source/target structure, referent
tracking via `hib_referent_option`) — and the narrowest in coverage: **121 live rows, one book
(Daniel)**, confirmed live this session.

`iba.db` also carries its own `cluster`/`cluster_strong` (51/7,609 rows) — a **migrated copy** of
`bible_research.db`'s `cluster` table (2026-08-11, per its own `cfg_table` note) plus a direct
Strong's-code-to-cluster link. This is coarser than Model A: it stops at the *cluster* level and
has no equivalent of `characteristic` (no sub-cluster trait subdivision at all in `iba.db`).

## Model D (retired) — the "dimension" layer

Five tables, every one explicitly marked retired in its own `cfg_table` description: a 20-dimension
verse-context classification (`wa_dimension_index`, 3,509 rows, last touched 2026-05-02), an
18-dimension rule-validation scoreboard that never once passed (`ve_dimension_scoreboard`, 8
FAILED / 10 IN-PROGRESS), a completion log that covers 6 of the 22 clusters it was meant to review
(`wa_dim_review_cluster_log`), a 2-row Session B remnant (`wa_session_b_dimensions`), and a declared
but never-populated prose link table (`prose_section_dimension_link`, 0 rows). Superseded by the
M-code cluster/finding model (Model A). Included here for completeness, not because any of it is a
live input.

---

## What does NOT connect

- **No foreign key or shared surrogate key between any of Model A, B, or C.** `characteristic.id`,
  `ib_characteristic.id`, and `phenomenon.id` are three independent integer sequences in (mostly)
  two different physical database files — even within `bible_research.db`, Model A and Model B
  were never linked to each other (checked: neither table references the other's id or code).
- **`cluster_code` is the one shared vocabulary**, and even that's asymmetric: Model A's 49
  clusters are the source; `ib_characteristic.cluster`/`cluster_all` (Model B) and `iba.db`'s
  `cluster`/`cluster_strong` (Model C's neighbour) both reference the *same code strings*, but
  `iba.db`'s copy was a one-time migration, not a live foreign key back to `bible_research.db` —
  the two files can drift with no mechanism to notice.
- **Coverage doesn't overlap in a way that would let you cross-check one model against another
  even informally**: Model A spans 35/49 clusters programme-wide; Model B is Psalms+Proverbs only;
  Model C is Daniel only. There is no book or cluster where all three have real data to compare.

## What this means for the catalogue `source` work

None of these three "characteristic" tables is a candidate `source` for the tier-catalogue
questions currently scoped `Characteristic (HIB behaviour)`/`Characteristic relational`/`The HIB` —
they hold *researcher-authored analytical content* (definitions, aggregated readings, debate-digest
phenomena), not raw base data the way `verse_lexical`/`strong_meaning_parsed` are. Where a question
in those buckets is answerable at all, the right `source` framing is "derived from reading the base
extract and recording the analytical judgment into `characteristic`/`ib_characteristic`/`phenomenon`
(researcher/AI-authored content, not a raw-data lookup)" — worth stating explicitly rather than
leaving it implied, since it's a different *kind* of source than the lexical-layer ones already
written up.
