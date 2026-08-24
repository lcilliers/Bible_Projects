> **Superseded by [prose-change-log-design-v4-20260824.md](prose-change-log-design-v4-20260824.md).**
> Kept on disk for history only.

# Prose change log design — versioning integrity (#836)

Supersedes: [prose-change-log-design-v2-20260824.md](prose-change-log-design-v2-20260824.md) (v1/v2
kept on disk for history). New this round: §0 — the researcher's scale/perspective correction
(2026-08-24) and what it concretely changes in the still-open items from v2. Sections 1–9 are v2
unchanged; §10 (still-open) is superseded by this round's §0d.

Status: still **design/analysis only**. §0 sharpens two of v2's open recommendations and adds one
new source of change and one new forward-looking concern — none of it forces a final decision by
itself; the researcher's own read on §0d's questions is asked for directly.

---

## 0. Scale and perspective correction (researcher, 2026-08-24)

**The researcher's framing, read back to confirm understanding:** today's prose activity (1,040
`prose_section` rows, 91 ever superseded) is an early, small-scale experiment — **not** a preview of
what the design needs to hold up under. Prose will be actively worked **from now until the last essay
is published or generated — realistically years away.** The editing effort ahead is not primarily
about fact-correction; it's a **large editorial-readiness effort**: style, readability, nuance, reader
preference, on top of the fact-accuracy concern this design has focused on so far. And the underlying
fact base feeding that editorial work is itself large: **~40,000 verses, 66 Bible books, 50 clusters,
roughly 4,000 relevant word-phrases/characteristics**, all generating observations and findings from
multiple angles — with essays likely composed as **short extracts drawn from many of those angles**,
not one section written once and left alone.

**What this concretely changes in v2's still-open items:**

### 0a. §6 (bulk/retention options) — Option A's case strengthens materially

v2 framed today's ~1 MB of superseded-row bloat as "not yet a large problem... worth designing
against the trend." That was already a hedge toward Option A (move prior-version text out of the
live, search-indexed table), but stated cautiously because the only evidence was a small, early
dataset. Given §0's framing — years of sustained editing, across a fact base ~40x larger by book
count alone (66 books vs. the handful represented in 1,040 rows today) before even accounting for
cluster/characteristic multiplicity, *plus* a style/readability editing pass layered on top of
fact-correction edits (§0b) — the growth-in-edit-churn assumption v2 treated as a future risk should
be treated as the **expected case**, not a tail scenario. This makes Option A (current-state table
stays lean; prior full text lives in a separate, non-search-indexed log/archive) the working
assumption to design toward, rather than one of three open options weighed evenly. Still the
researcher's call to confirm (§0d).

### 0b. §5 (sources of change) — a fifth source, likely the volume-dominant one

v2 named four sources (multi-table edit script, flag-driven fix, direct update, findings generator).
§0's framing surfaces a fifth that doesn't fit any of them: **pure editorial/stylistic revision** — a
change made not because any fact, finding, or flag changed, but because an editor (Claude AI or the
researcher) is improving style, readability, nuance, or reader-fit on a section that is already
factually correct. Once the "huge editorial-readiness effort" phase §0 describes is underway, this is
plausibly the **most frequent** source of change, not a minor one — and unlike the other four, it has
no upstream data event to point back to as "the reason." The change-log's reason/change-type
vocabulary (an item already flagged open in v2 §10) needs a first-class value for this — "stylistic
pass," or similar — not a generic "other," since it's likely to be the majority case, not the
exception.

### 0c. §2 item 3 / §6's FTS finding — essay composition raises the stakes on joint-change visibility

v2's §2 item 3 asked whether changes need to be linkable "when one editorial action touches both
tables at once." §0's essays-as-short-extracts-from-many-angles model raises a related but larger
question: if a single underlying finding or observation feeds short extracts placed into *several*
essay sections — potentially across different books/clusters — then a change to that one upstream
fact could, in principle, need to ripple into *many* prose sections, not just the two-table case v2
considered. This is **not** something this item needs to solve — tracing prose back to the
findings/characteristics that grounded it is exactly the citation/traceability territory #829 D5/D6
already deferred to a future index/Concordance table, out of scope here. It's noted here only as a
constraint on *this* design: whatever "bundled-with" or grouping concept the change-log ends up using
(v1 §2 item 5) should not be built in a way that silently assumes one editorial session touches at
most a small, fixed number of sections — the real future shape may be much larger fan-out, even
though building the fan-out *mechanism* itself stays out of scope for now.

### 0d. Two direct questions back to the researcher

1. **§6 retention** — given the above, should Option A be treated as decided (not just leaning), so
   the next round can design its actual shape, rather than continuing to weigh it against B/C?
2. **§5's fifth source** — confirm the "stylistic/editorial pass" reading is right, and whether it
   should be folded into the design now (as a first-class change-reason value) or noted as a forward
   placeholder the way "findings generators" already is (v2 §5's last row) — i.e., real and expected,
   but not yet operationally defined enough to build against today.

No other changes to v2's content — §§1–9 stand as filed. This round is a scope/perspective
correction, not a re-derivation.
