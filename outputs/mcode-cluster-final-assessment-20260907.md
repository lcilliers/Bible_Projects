# M-Code Cluster Membership — Final Assessment for Reading Analysis

*Prepared 2026-09-07. Queried live against `iba.db` (`strong`, `cluster`, `cluster_strong`, `strong_verse`). Prior cluster work referenced: escalations #1525 (cluster conflict resolution, completed), #1523 (assignment exceptions, in-progress/kept open), #1526 (reading strategy vs cluster size, in-progress), #1006 (cluster analysis framework, completed — confirmed no single load engine exists). No open escalation covered this specific four-part review; raised as **#1546** to track it.*

---

## (a) Is every strong assigned to a cluster, except backfill-status strongs?

**Partially true — confirmed for `word`-origin strongs, but `backfill`-origin coverage is far from all-or-nothing.**

`strong.origin` has exactly two values, confirmed live:

| origin | live strongs | with ANY cluster_strong assignment | without one |
|---|---|---|---|
| `word` | 4,776 | **4,776 (100%)** | 0 |
| `backfill` | 10,517 | 2,548 (24%) | **7,969 (76%)** |

So: every `word`-origin strong (a strong reached via direct study-word discovery) does have a cluster assignment — your expectation holds exactly there. But `backfill`-origin strongs aren't uniformly *un*assigned either — roughly a quarter (2,548) already carry one, likely picked up incidentally through the sibling-conflict backfill process referenced in #1523 (829 backfill strongs flagged there for "already-active or already-clustered sibling"). The clean version of your expectation is: **100% of `word`-origin strongs are covered; `backfill`-origin coverage is partial and not yet a deliberate, completed pass.**

Of the 4,776 `word`-origin strongs, cluster assignments split: 2,294 to an M-code, 2,524 to a T-code, 22 to FLAG (a strong can carry more than one — see (b)).

---

## (b) Strongs assigned to more than one cluster

**Within M-code: zero — re-verified live, matches #1525's own closing claim exactly.** No strong carries two different M-code assignments.

**Across M-code and T-code/FLAG: 79 strongs carry both** — a real, unreconciled pattern, not noise. Breaking down by which classification pass produced which side:

| Count | M-code source | T/FLAG code | T/FLAG source |
|---|---|---|---|
| 20 | `llm-allocation-v1_3` (2026-08-11) | T2 | `heuristic-family-grouping-v1` (2026-09-05) |
| 11 | `old-system-migration` | T2 | `heuristic-family-grouping-v1` |
| 10 | `old-system-migration` | T2 | `old-system-migration` |
| 9 | `auto-precedent` | T2 | `heuristic-family-grouping-v1` |
| 7 | `heuristic-family-grouping-v1` | T2 | `old-system-migration` |
| 7 | `heuristic-family-grouping-v1` | T3 | `llm-reassignment-v1_1` (2026-08-11) |
| 4 | `old-system-migration` | FLAG | `old-system-migration` |
| 3+2+1+1+1 | (smaller mixes) | FLAG/T3/T7/T8 | various |

**The reason, concretely:** in 40 of the 79 cases (the top three rows), a strong already had a genuine, substantive M-code allocation from an earlier pass (LLM allocation, auto-precedent, or the old system), and the *later* `heuristic-family-grouping-v1-20260905` pass then *also* tagged the same strong into T2 — whose own stated rationale is **"no inner-being significance -- place/person name, body part, divine/idol reference, or generic human-relational term."** That's a direct contradiction: the same strong is on record as both "has real inner-being significance, belongs in M-code X" and "has no inner-being significance, park it." The heuristic pass appears to have run without checking for a pre-existing M-code assignment. A further 10 cases show the *old system itself* carrying this same self-contradiction pre-dating any of this session's work. This is the same shape of conflict #1525 spent most of its 17 versions resolving — but #1525's own scope, confirmed from its resolution text, was M-code-vs-M-code conflicts specifically; this M-code-vs-T/FLAG shape was never in scope there and has never been reconciled.

---

## (c) Does cluster-level analysis make sense? (M-code only, per your scope)

**Mostly yes, with one concrete, evidenced exception found, not a general problem.**

80 M-code clusters, sized 2 to 138 members (mean 37.9, median 28) — a reasonable spread, not dominated by one catch-all bucket. Spot-checked three, from small to large:

- **M67 (Sloth & Diligence, 2 members)** — `oknēros`/"lazy", `spoudē`/"diligence". Tight, coherent antonym pair.
- **M10c (Defilement & Impurity, 20 members)** — entirely defilement/impurity/uncleanness terms, a clean, distinct domain from its neighbour M10 (verified earlier this session, in escalation #1535's own investigation).
- **M24 (Fainting/despair/weariness/toil, 138 members — the largest M-code cluster)** — the large majority genuinely fit a broad-but-real "worn down / afflicted / distressed" domain (weariness, toil, affliction, anguish, sluggishness). But a distinct sub-group of **~8-10 plunder/seize/harm terms** — `harpagē`/"plunder", `harpazō`/"to seize", `sunarpazō`/"to seize", `baz`/`bizzah`/"plunder", `chataph`/"to seize", `qamat`/"to seize", `meshissah`/"plunder", `skulon`/"plunder", `adikeō`/`kakoō`/"to harm" — don't fit that theme; they're about actively inflicting/taking, not experiencing distress. That looks like member drift into the largest, most "absorbent" cluster rather than a genuine semantic fit.

**Read together with the size distribution:** the one clear coherence problem found sits in the single largest cluster, which fits a plausible general risk (a big cluster is easier to drift into) but isn't evidence the whole taxonomy has this issue — the two much smaller clusters checked were both clean. Recommend a targeted pass over the handful of largest clusters (M24, M23, M03, M18, M01 — all 100+ members) specifically, rather than a full 80-cluster audit, before treating cluster-level analysis as safe to proceed on for all of them.

---

## (d) Verses per strong per M-code cluster — where volume is a problem

2,149 (cluster, strong) pairs with at least one verse. Median 5 verses/strong (the typical case is entirely tractable to read individually). But a real long tail:

| Verse-count band | Pairs |
|---|---|
| 1–5 | 1,117 |
| 6–20 | 532 |
| 21–50 | 279 |
| 51–100 | 111 |
| 101–500 | 103 |
| 500+ | 7 |

**The 7 extreme outliers** (each a single Strong's number carrying several hundred to nearly a thousand verses on its own):

| Cluster | Strong | Word | Verses |
|---|---|---|---|
| M42 | H1696G | speak | 971 |
| M41 | H8085G | hear | 904 |
| M15 | H3045 | know | 874 |
| M65 | H1697G | word | 825 |
| M36 | H5650 | servant | 715 |
| M23 | G2192 | have | 615 |
| M47 | H3820A | heart | 550 |

These are exactly the kind of extremely high-frequency, semantically-broad terms where reading every occurrence individually is unlikely to be the right strategy — and they directly ground the question already raised in escalation #1526 (do many of these verses converge on the same conclusion, justifying an anchor-verse/similarity-based approach rather than one-by-one reading). 110 pairs total exceed 100 verses; those are the practical candidates for a different reading strategy, not just the top 7.

---

## Summary / recommended next steps

1. **(a)** No action needed — `word`-origin coverage is complete. Whether to deliberately extend clustering to more `backfill`-origin strongs is a separate scope decision, not a defect.
2. **(b)** The 79 M-vs-T/FLAG conflicts are a real, well-evidenced gap in #1525's otherwise-thorough conflict resolution — recommend a follow-on pass specifically for this shape.
3. **(c)** Cluster-level analysis is reasonable to proceed on for most M-code clusters; recommend re-checking the ~5 largest ones for drift before relying on cluster-level coherence uniformly.
4. **(d)** The 110 cluster-strong pairs over 100 verses are the concrete list to hand to #1526's anchor-verse/similarity investigation as its starting evidence base.
