# 2236 — Open items: design v2, and the tool

Escalation: #2236 v3. Status: the design as built, on your decisions of 2026-10-23 (verbatim on #2236
v3). The review and v1 are in `outputs/escalation/2236-open-items-review-and-design-v1-20261023.md`,
kept as the review.

## 1. What an open item is

A pointer from the analysis in hand to related work that does not interrupt it. It states **what to
read for** and **why it is open**, it is scoped to specific verses, and it is cleared at some point. An
item without a clear purpose is refused.

## 2. Its parameters

| Parameter | Required | Holds |
|---|---|---|
| **Thread** | yes | The purpose of the read the item belongs to. A thread is defined by that purpose, neither by topic nor by origin (your D2), and states it in its title and description. |
| **Origin** | yes | The escalation of the analysis that raised it. |
| **Anchor** | yes | Where in that analysis: `strong:H3708A`, `verse:Ecc 7:9`, `observation:12478`, `claim:C-330` or `block:10.1 / The bosom`. |
| **Source terms** | for a cluster item | The source analysis's strong(s) (bare codes decomposed, B:113). |
| **Target** | yes | Either a **target cluster with its target term(s)** (strongs from that cluster), so the item reads "cluster xx for source strong xx and how it interacts with the related term xxx", or **verses**. |
| **Target verses** | computed | For a cluster item, the verses holding a source term *and* a target term; else the verses given. At most `open_item.max_verses` (200). A wider item is refused and must be **split into separate items, one purpose each** (your D3). |
| **Read for** | yes | What the reading is to look for. |
| **Why** | yes | Why it is an open item: what the origin found that leaves it open. |
| **Comes back when** | yes | The trigger: the target cluster or strand being worked, a chapter or block, or a researcher event. |

**Matching.** A worded item matches a scope only on its **target verses**, never on a whole cluster.
Its target cluster is its *home*: `Open-Item.ps1 -Action Due -Cluster M58` lists the items that come
back when M58 is worked. An item not yet reworded matches as today until it is.

**Clearing** is as today (closed with the answer, withdrawn, superseded, forward), through
`Escalation.ps1`, or at a reading's gate 2 (#2228 design v2).

## 3. The tool: `Open-Item.ps1` (through `run.py`, work package `open-item`)

| Action | Does |
|---|---|
| `Add` | `-Thread OT-nn -Origin <id> -Anchor <kind:value>`, then `-Source <strongs> -TargetCluster Mxx -TargetTerms <strongs>` or `-Verse "<refs>"`, then `-ReadFor "…" -Why "…" -ComesBackWhen "…"`. Refused on a missing part, an unresolved target, over 200 verses, or the same target with the same read-for on the thread. |
| `Reword` | `-Item OT-nn.n` with the same parameters. The item is rewritten in place. Its earlier wording goes to the item's history as a response, so the live row holds only the current wording (rule 96). |
| `Split` | `-Item OT-nn.n -File <items.json>`. Several new items replace one wide item, which is recorded superseded by them. |
| `Due` | the worded items whose home is the given cluster, strand or chapter. |
| `Review` | the stragglers report (your D4): items not yet worded, worded items older than `open_item.review_age_days` (60), and threads with no open item left. The report goes to `open_item.output_dir`. |
| `File` | `Add`, `Reword` and `Split` also take one JSON of many actions, so a thread's items are reworded in one call. |

**Schema.** `escalation_thread_item` gains `origin_escalation_id`, `anchor`, `source_terms`,
`target_cluster`, `target_terms`, `read_for`, `why`, `comes_back_when`, `target_verses` (the count) and
`worded_at` (when it was worded to these rules; NULL means not yet). The new table
`escalation_thread_item_verse` holds the item's target verses. `escalation.match_open_items` matches a
worded item on these verses.

## 4. Rewording the 323 existing items (your D5)

Thread by thread, each in one `-File` call:
1. **Written lists.** Where the target is already written down (OT-103's face-combination CSV, OT-97's
   triage CSV, the verse lists in OT-105 and OT-106 notes), the items are reworded from that source
   as source term × target term.
2. **By reading the origin.** The other items are reworded after reading the thread's origin.
3. **Closing.** Items that serve no purpose are withdrawn with the reason, and duplicates are
   superseded by the one kept.

Each thread's rewording is a record (the JSON applied, and the item histories). The `Review` report
before and after shows what is left.
