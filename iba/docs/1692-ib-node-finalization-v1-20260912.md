# Escalation #1692 — `ib_node` (was trace) — columns + governing rules, for final sign-off

**Status:** consolidation for review, decision_required. Nothing built. Same structure as
#1691's own consolidation, per the researcher's LLM-session/table-update-procedure split — an
`ib_node` row **never exists at LLM-generation time**; it is created entirely by the table-update
procedure, from the node segments an observation carries in its JSON.

**DB location, 2026-09-13 (DB fork, #737/#1682/#1690/#1691): `ib_node` lives in `iba.db`.** Already
consistent with this doc's own design — every reference here (`observation_id`/
`traced_observation_id` → `ib_observation`, `verse_reference` resolved fresh against
`iba.db.verse.reference`) was already same-database or `iba.db`-targeted; no columns changed by the
fork. **No step of this pipeline may read or write `bible_research.db`.**

**Note re: #1697** (`iba.cluster.status` lifecycle, same sign-off pack) — `ib_node` has no direct
gating role in that mechanism: rows here are derived entirely from `ib_observation` at write time,
not independently staged per cluster. Noted for completeness only, nothing in this document changes.

**Guiding principle, researcher's own words, 2026-09-14:** *"ib-node is likely the most important
table in the entire study. This node table is the nerve of all observations, all findings, the
knowledge web of the study. It ties together, and allows discovery through a network of relations.
Given that the inner being is one large system of interconnected behaviours and operations the
ib_node is the hub of the interconnected reference points."* This governs how the open items below
are read: `ib_node` is not a bookkeeping/audit table, it is the study's actual relational substrate
— design and validation decisions here should be weighed against "does this keep the network
navigable and evidence-based," not just "is this normalized correctly." The corresponding
responsibility on the write side (#1693 must "record correctly, maintain appropriately, verify and
validate on every turn, and self check as a matter of primary accountability" — researcher's own
words) is recorded at #1693 directly, not duplicated here.

## 1. Columns — final list as decided so far

```sql
CREATE TABLE ib_node (   -- name confirmed by researcher, resolves the old #1691/#1692 concatenation question
    id                     INTEGER PRIMARY KEY,   -- assigned by the TABLE UPDATE PROCEDURE only
    observation_id         INTEGER NOT NULL REFERENCES ib_observation(id),  -- real id: both sides are
                                                     this new schema, no cross-db/legibility reason
                                                     to denormalize this one
    cluster_code           TEXT NOT NULL,          -- CLARIFIED 2026-09-14 (§4 item 2): a VALUE, not
                                                     an id, but NOT always a copy of the parent
                                                     observation's own cluster -- it is THE cluster
                                                     this particular row references. Ordinarily
                                                     that equals the observation's own cluster
                                                     (same-cluster grounding); if the observation
                                                     touches MULTIPLE clusters, one row per cluster
                                                     is created, each carrying a different value here
    cluster_subgroup_code  TEXT NULL,               -- was `family_key`; same rule as cluster_code --
                                                     THE subgroup this row references (usually the
                                                     observation's own, but a different one, or
                                                     several via several rows, when the observation
                                                     genuinely touches another subgroup)
    strong                 TEXT NULL,               -- denormalized copy
    verse_reference        TEXT NULL,               -- resolved FRESH against iba.db.verse.reference
                                                     at load time, never trusted from the LLM's JSON
                                                     directly (escalation #1693's own fix) -- set
                                                     only when grounded in a verse
    surface                TEXT NULL,               -- was `span_surface`; matches span.surface
    morph_code              TEXT NULL,              -- was `span_morph`; matches span.morph_code
    question_code           TEXT NULL,               -- NEW, 2026-09-14: catalogue-question grounding
                                                     -- added to the element list below; same
                                                     -- unresolved cross-database status as
                                                     -- ib_observation.question_code (#1691 §7a) --
                                                     -- restore as an FK once #1696 lands the
                                                     -- catalogue into iba.db
    traced_observation_id   INTEGER NULL REFERENCES ib_observation(id),  -- set when grounded in ANOTHER
                                                     observation instead of a verse -- real id, same
                                                     reasoning as `observation_id`
    source_stage             TEXT NOT NULL,         -- 'reading' | 'answer' | 'synthesis'
    seq                       INTEGER NOT NULL,     -- SHARPENED 2026-09-14, see §4 item 1: a
                                                     -- plain per-observation ordinal -- ties
                                                     -- together every ib_node row that shares one
                                                     -- observation_id, in reading order, when that
                                                     -- order is meaningful (e.g. 3 strongs within
                                                     -- one span, cited in the order they occur).
                                                     -- NOT a compound "observation_id-seq" string --
                                                     -- observation_id is already its own column;
                                                     -- the natural key is the PAIR, not one field
    created_at                 TEXT NOT NULL,
    CHECK: at least one of (strong, verse_reference, cluster_subgroup_code, cluster_code,
           question_code, traced_observation_id) IS NOT NULL  -- widened 2026-09-14, replaces the
           old exactly-one-of-two CHECK, see §4 item 2/3
    UNIQUE (observation_id, seq)  -- NEW 2026-09-14, see §4 item 1 -- the real natural key for
           ordering/uniqueness within one observation
)
```

## 2. The LLM session — what it must produce for `ib_node` to be buildable

No `ib_node` row is ever written by the LLM. What the LLM DOES have to produce, on every
observation in its JSON (this is really an `ib_observation`-JSON-shape rule, repeated here because
`ib_node` is entirely derived from it): the exact node segments — verse + surface + morph, a
catalogue question, a subgroup/cluster it touches, or a reference to another observation — that
support or address that observation, per #1691 §2 item 2. **The LLM surfaces the relation; it does
not resolve or "find" the related item** (researcher's own words, 2026-09-14) — existence
validation and the actual DB linkage are the table-update procedure's job (§3), not the LLM's.
Nothing else for this table; there is nothing an `ib_node` row does that the LLM decides directly.

**New requirement, 2026-09-14 — coverage self-check.** Researcher's own words: *"it is expected
that on the completion of a sub-group reading session, every strong, and every verse in the
subgroup membership will have at least 1 row in ib_node... llm must verify that each strong and
each verse in the subgroup have been answered to."* Concretely: before a reading-stage session's
JSON is finalized, the LLM must check its own output against the subgroup's full strong/verse
membership and confirm every one of them is grounded by at least one node segment on at least one
observation — this is a generation-time self-check (part of the reading process spec, #1682), not
a new column here. The table-update procedure runs the same check again independently after
load (§3, new item below) — two checks, not one trusted blindly.

## 3. The table-update procedure — what creates and populates `ib_node`

1. **Reads each observation's node-segment citations from the JSON** and creates one `ib_node` row
   per citation, linked to whichever `ib_observation.id` the reconciliation logic (#1693) assigned that
   observation (new or existing). **Second source, added 2026-09-14 (#1691 §9 item 10):** a real
   observation captured in process (b)'s `cluster_subgroup_strong.placement_note` also promotes to
   an `ib_observation`/`ib_node` pair, under the new `stage='subgroup'` value (#1691 §1) — same
   creation mechanism, different input field. Full rule at #1693, not duplicated here.
2. **Denormalizes at write time** — `cluster_code`, `cluster_subgroup_code`, `strong` are copied
   onto the row from context, not computed by the LLM. **CLARIFIED 2026-09-14 (§4 item 2):** when
   an observation's citation names multiple items of the SAME reference type (e.g. it touches
   clusters 1, 2, and 3), the procedure creates one `ib_node` row per item, all sharing the same
   `observation_id` — not one row with several values packed in.
3. **Resolves `verse_reference` fresh against `iba.db.verse.reference`** (matched via strong +
   occurrence) rather than trusting whatever string the LLM's JSON contains — closes the
   verse-reference-consistency risk found in #1682/#1693 by construction.
4. **Assigns `id`** — the one true unique id for the citation row, same pattern as `ib_observation.id`.
5. **NEW, 2026-09-14 — validates strong/verse coverage independently of the LLM's own check.**
   After loading a reading-stage session's rows, confirms every strong and every verse in the
   target subgroup's membership is grounded by at least one `ib_node` row across that session's
   observations; a gap is a load-time finding, not silently accepted. This is the write-side half
   of the "primary accountability" principle in the banner above (verify/validate/self-check on
   every turn) — the mechanism (block the load, or load-and-flag) is not decided here.

## 4. Still not settled

1. **RESOLVED, 2026-09-14 — `seq`'s role, structure, AND value source all confirmed.** Researcher's
   own example: three `ib_node` rows tied to one observation (a span with three strongs), in a
   specific reading order — *"is this what you had in mind when you created seq?"* Yes: `seq`'s
   original job (§1: "ordering within one observation's citations") is exactly this — it ties
   together every row sharing one `observation_id`, in reading order, when that order matters.
   **Structure:** not `[observation_id]-[seq]` as a compound string — `observation_id` is already
   its own real column; the natural key is the PAIR, now a real `UNIQUE(observation_id, seq)` (§1).
   `seq` stays a plain per-observation-relative `INTEGER`.
   **Value source, researcher's own words, 2026-09-14:** *"seq is determined by the subject
   matter: if it's about span, then the position code is ideal, and if the subject matter does not
   dictate a specific useful sequence, then simply use a serial. The rule is that if ib_node refers
   to the same observation, and have multiple seq, then it should be read in sequence of the
   seq."* Confirms the recommendation above exactly: span-grounded rows derive `seq` from
   `iba.db.span.position` (closes the original Matt 5:22 idempotency defect — deterministic, not
   JSON-emission-order-dependent); every other row gets a plain ascending serial. Either way, the
   governing read-rule is the same: multiple `ib_node` rows sharing one `observation_id` are read
   in `seq` order. Nothing left open in this item.
2. **RESOLVED, 2026-09-14 — single polymorphic table, confirmed; row shape sharpened.** Researcher's
   own list of what a node can point at — "Strong, verse, span, morph, subgroup, cluster, catalogue
   question, another observation" — with the rule "the element column must be completed if the
   observation supports it, must not be completed if it does not." **Sharpened same round,
   researcher's own words:** *"a row expecting at least an observation and one other reference to
   be traceable. If the observation references multiple items of the same type (e.g. cluster 1, 2
   and 3) then a row is created, for each item referencing the same observation."* Read together:
   one row = one observation + one coherent reference (a verse occurrence's own strong+surface+
   morph travel together as that ONE reference's descriptive detail, not as separate references);
   when an observation touches several items of the SAME reference type, that's several rows, one
   per item, not several columns filled in one row. §1's CHECK is widened accordingly (was:
   exactly one of verse_reference/traced_observation_id; now: at least one of the full element
   list, per-row). No separate two-table split.
3. **PARTIALLY RESOLVED, 2026-09-14 — field list confirmed, one column added.** The researcher's
   element list above is now the authoritative field list; the one gap it exposed against the
   existing column set is `question_code` (catalogue-question grounding), added in §1. Whether
   `cluster_subgroup_code`/`cluster_code` are meant ONLY as always-filled denormalized context
   (the node's own home subgroup/cluster) or can ALSO independently name a *different*
   subgroup/cluster the observation touches (e.g. a cross-family/cross-cluster reference, matching
   the `cross-family` tag already seen at #1691 §5) is not settled by the researcher's list alone —
   flagged for confirmation, not assumed either way. The verse-text question (should `verse_text`
   itself be carried, as process (d) restores it) is unchanged, still open.
4. ~~Table name~~ — **resolved**, `ib_node` confirmed (see §1).
5. **RESOLVED, 2026-09-14 — mapping confirmed.** Researcher confirms: "subgroup, reading,
   observation, synergy" = processes b/c/d/e directly. So "observation" = the `answer` stage
   (process d) and "synergy" = the `synthesis` stage (process e) — same stages already in the
   `stage` enum, researcher's own preferred names for them, not new values. "subgroup" = process
   (b) itself, which today writes `cluster_subgroup`/`cluster_subgroup_strong` only, not
   `ib_observation`/`ib_node` — **except live evidence now shows process (b) already produces real
   observations with no home**, confirmed against an actual M10 prototype run: full detail and the
   open decision (does `stage` gain a genuine new value for process (b)'s own findings) at #1691
   §9 item 8, not duplicated here. Separately open, not decided: whether `stage`/`source_stage`'s
   actual DB values should be renamed to match the researcher's vocabulary (`answer`→`observation`,
   `synthesis`→`synergy`) — a naming question across #1691/#1692/#1693 together, raised in chat
   this turn.

## 5. What "finalized" would mean

**RESOLVED, 2026-09-14 — every §4 item now closed.** Item 1 (`seq`/uniqueness, the last real
blocker) is resolved: plain per-observation `INTEGER`, `UNIQUE(observation_id, seq)`, value from
`span.position` when span-grounded else a plain serial, read in `seq` order. Items 2, 3, and 5 were
already resolved (single polymorphic table; `question_code` added, `cluster_code`/
`cluster_subgroup_code` confirmed as true per-row references; stage-terminology mapping confirmed).
Nothing in §4 remains open. The `CREATE TABLE` in §1 is ready to register in `cfg_table`/
`cfg_column`; the table-update procedure's §3 responsibilities become part of #1693's full spec,
same as #1691's §3 — this document's own design content is complete pending the researcher's
formal sign-off (§10-equivalent, matching #1691/#1690's own "finalized" framing).
