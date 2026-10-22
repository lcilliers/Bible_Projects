# 2228 — Why a subset forces a rebuild (v2)

Escalation: #2228 (from #2172). Status: diagnosis for your decision; nothing is built.
v1 (`outputs/escalation/archive/2228-subset-rebuild-diagnosis-v1-20261022.md`) is replaced. It
looked only at the reading code and missed the boat. Your correction, verbatim:

> "It looks like you are not looking at all at work already done in the _analytics folder, and
> rereading of anything should be restricted to items that have not been read or need a revised
> reading, and the scope of the analysis is determined by what it requested, this could be a variety
> of things, by cluster, for a set of verses, for a single verse, for a open item, for a specific
> claim"

## What an analysis must do (your three points)

1. **Start from the work already done.** That means the tables and the readings, ledgers and pulls
   in `_analytics`.
2. **Read only what is unread, or what needs a revised reading.** Everything else is reused.
3. **Take its scope from the request.** The request can be a cluster, a set of verses, a single
   verse, an open item or a specific claim.

## How the present build measures against them

Checked in the code (`iba/app/lib/strandreading.py`) and in iba.db, with the anger strand as the
case.

| Point | What the build does | Fact |
|---|---|---|
| 1. Work already done | Context reads only tables: the strand's hits, `verse_meta`, observations in `ib_observation`, and matched open items. It reads nothing in `_analytics`. The October readings reach a strand only as an open-item note naming the file (OT-108.3 to .9). | `_analytics` holds 2,449 live `.md` files. Catch-up B brought in 691 October ledger rows. The prose readings of 6 to 19 October are not in the tables. |
| 1. Work already done | What October already did is kept only as a note. Each row's October disposition (W woven, RS, NS, H, D) is in `revisit_note`. The status stays `draft`, so Derive must dispose of it again. | All 352 anger observations are `draft`. 326 carry an October disposition: W (to weave) 179, D (stays in data) 128, NS 12, RS 2, H 1, "data" 4. The 26 added today have none. W was a proposal, not a record that the weave was done. |
| 2. Read only the unread | Coverage is tracked per verse (`verse_meta.status`) and per hit (a face). Map and Derive have no such state: a block mapped, or an observation disposed, before this build counts as not done. | Anger: 892 of 892 hits faced and every verse `analysed`. Still, 178 blocks would have to be mapped and 352 observations disposed, from nothing. |
| 2. A revised reading | There is no trigger for one. Nothing marks a reading as needing revision: a new verse in scope, a quotation corrected, a claim changed, a researcher correction. | none |
| 3. Scope from the request | The only scope is a strand, a word family. Every step takes `-Strand` and nothing else. A cluster is reached only as a strand's home. A verse set, a single verse, an open item or a claim cannot be the request. | Recording 26 inner-seat rows on 43 verses led to a gate over 178 blocks. |
| 3. Scope from the request | An observation belongs to one strand, through its hits. The inner-seat rows are about the heart, soul and spirit, but they are grounded only on the anger words, so a request about the heart or M47 would not find them. | The 146 life-death faces on soul, spirit and heart words are in no strand. |

So the build re-creates, inside one strand, what the project already has across the tables and
`_analytics`. It cannot be asked a narrower question.

## What the right shape needs (for your decision; not designed in detail)

1. **The request defines the scope.** A cluster, a verse set, a verse, an open item or a claim
   resolves to the verses, observations, claims, blocks and open items it touches. The strand is
   one kind of request, not the container.
2. **What is known comes first, from both places.**
   - From the tables: the observations, claims, tellings and items on that scope.
   - From `_analytics`: the readings, ledgers and pulls that name its verses. This needs an index
     of which file reads which verse; none exists today.
3. **Each element carries a state.** A verse read (and in which respect), an observation disposed,
   a claim checked, a block mapped against a version. Work done earlier is entered once as its
   real state, not as `draft`.
4. **Only the gap is worked.** Unread, or needing revision, with a named trigger. The account and
   any gate cover the request's scope, not the whole strand.
5. **An observation is grounded on every inner word it speaks of,** so any request that touches
   those words finds it.

**Before any design,** Claude would first map what already exists: the analytic tables
(`ib_observation`, `ib_node`, `verse_meta`, the claims register and tellings, `reading_strand*`,
`escalation_thread_item`), and the kinds of work in `_analytics` and how each names its verses.
That shows which parts of the five already exist and need joining, and which do not exist.

## Decision

| | Your choice | Comment |
|---|---|---|
| Is this the right statement of what an analysis must do? | | |
| Next: the map of what exists (tables and `_analytics`), then a design for your review? | | |
