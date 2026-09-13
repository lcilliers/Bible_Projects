# Escalation #1690 — `cluster_subgroup`/`cluster_subgroup_strong` (replacing family) — columns + governing rules

**Status:** design proposal, decision_required. The fresh tables are built with the SAME shape as
the ones being renamed to `zz_legacy_*` (no reason to invent a competing shape when reverting to
the concept). Restructured this round to match #1691/#1692's LLM-session/table-update-procedure
split, per the researcher's instruction — process (b) (family/subgroup assignment) is itself an
LLM session with no DB access, same as process (c)/(d)/(e).

**Renamed, 2026-09-13 — researcher's own words:** the membership table is `cluster_subgroup_strong`,
not `mti_term_subgroup` (more descriptive, matches the "descriptive nomenclature, not invented
codes" convention).

**★ DB FORK, 2026-09-13 — SUPERSEDES the location/precondition stated below when first written.**
Both `cluster_subgroup` and `cluster_subgroup_strong` are new tables **in `iba.db`, not
`bible_research.db`.** SQLite doesn't enforce foreign keys across attached databases — only
same-file FKs are real — so `cluster_code REFERENCES cluster(cluster_code)` and the strong-level FK
(§1) both need same-database targets to mean anything. See escalation #737 (left open, not
realigned, per the researcher's own sequencing decision) and #1682's own banner for the full
reasoning. **Consequence: the legacy-rename precondition is GONE** — the legacy `cluster_subgroup`/
`mti_term_subgroup` tables stay in `bible_research.db`, untouched, no longer occupying names the new
`iba.db` tables would collide with. Whether they still get renamed to `zz_legacy_*` is now a #1683
disposition question on its own timeline, not a build precondition here. **No step in this design —
process (b) or the table-update procedure (#1693) — may read or write `bible_research.db` at all.**

## 1. Columns — final list as decided so far

```sql
CREATE TABLE cluster_subgroup (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,  -- assigned by TABLE UPDATE PROCEDURE
    cluster_code        TEXT NOT NULL REFERENCES cluster(cluster_code),
    subgroup_code       TEXT NOT NULL,   -- the family's own code, e.g. "H_guilt", "FLAG" -- FLAG
                                             is expected to repeat across clusters (one per
                                             cluster), see §3 item 3 -- the sole exception to
                                             "unlikely but not impossible" cross-cluster reuse
    label               TEXT NOT NULL,   -- REQUIRED -- see §2 item 1, a real gap in process (b)
    core_description    TEXT,
    sort_order          INTEGER DEFAULT 0,
    status              TEXT,            -- subgroup-level lifecycle, cfg_enum-governed -- see §3a
                                             (distinct from #1697's cluster-level status; this is a
                                             fresh, empty table -- no legacy data to collide with)
    version             TEXT,
    source              TEXT,
    notes               TEXT,
    delete_flagged      INTEGER DEFAULT 0,
    created_at          TEXT,
    last_updated_date   TEXT,
    UNIQUE (cluster_code, subgroup_code)
)

CREATE TABLE cluster_subgroup_strong (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,  -- assigned by TABLE UPDATE PROCEDURE
    strong              TEXT NOT NULL REFERENCES strong(strongNumber),  -- was mti_term_id/mti_terms.id
                                    -- changed 2026-09-13 (DB fork): mti_terms is bible_research.db-
                                    -- only and itself messier (only 2,730/7,861 rows genuinely
                                    -- one-per-Strong's); iba.strong is the clean, live, same-database
                                    -- anchor, matching the pattern iba.cluster_strong already uses
    cluster_subgroup_id INTEGER NOT NULL REFERENCES cluster_subgroup(id),
    placement_note      TEXT,   -- REQUIRED for FLAG placements (the reason, see §3 item 3); OPTIONAL
                                    but available for any ordinary placement too, to capture whatever
                                    observation the LLM made while assigning that strong (§2 item g)
    delete_flagged      INTEGER NOT NULL DEFAULT 0,
    created_at          TEXT NOT NULL,
    last_updated_date   TEXT NOT NULL,
    UNIQUE (strong)   -- TIGHTENED from the legacy (mti_term_id, cluster_subgroup_id) --
                          enforces "one strong, one family" structurally, see §4 item 2
)
```

| Column | Usage |
|---|---|
| `cluster_code` | required, singular — a family is structurally one-cluster-only by construction; now a REAL, enforced FK (`iba.db`, same database, DB fork 2026-09-13) |
| `subgroup_code` | the family's stable code, unique per `(cluster_code, subgroup_code)` — expected to repeat as `"FLAG"` across clusters, never otherwise (researcher's own confirmation, §3 item 3) |
| `label` | short human title — **not currently produced, see §2 item 1** |
| `core_description` | one sentence on the family's shared commonality |
| `sort_order`/`version`/`source`/`notes` | reused as-is, same as the legacy table (descriptive `source` values, not invented short codes) |
| `status` | subgroup's own lifecycle, `cfg_enum`-governed — proposed values + gating rule at §3a. Distinct from `iba.cluster.status` (#1697) — that's a different table, a coarser grain, and its own separate enum; this row previously conflated the two, corrected 2026-09-13 |
| `strong` | the Strong's code, resolved to `strong.strongNumber` in `iba.db` (was `mti_term_id`/`mti_terms.id`) — real, same-database FK, an upgrade over both the original free-text proposal and the `mti_terms`-based one |
| `placement_note` | free text — **required** for `FLAG` placements (the signpost's rationale, §3 item 3); **optional but available for any ordinary placement**, to capture whatever observation the LLM made while assigning that strong (§2 item g) |

## 2. The LLM session (process b) — what it must produce

**Full governing rules, researcher's own instruction, 2026-09-13 (a–g), integrated with what was
already resolved (1–3, kept and cross-referenced rather than duplicated):**

a. **Full-cluster read before any assignment.** All `gloss` and `surface` values for every strong in
   the cluster must be read FIRST, before subgroup assignment begins for any of them — not a
   streaming process that assigns strongs one at a time as they're read.
b. **Subgroups are meaning-based, not surface-similar.** Grouped on actual shared meaning, not on
   strongs whose glosses merely look alike or share superficial wording.
c. **Maximum 10 subgroups per cluster — `FLAG` excluded from this cap, confirmed.** A cluster's real
   (non-`FLAG`) subgroups top out at 10; `FLAG` is a signpost bucket, not a subgroup competing for
   that budget — consistent with its exclusion from every other subgroup-count mechanism already in
   this design (the status rollup, §3a; the reading-input exclusion, item (f)/§3 item 3).
d. **`label` must be true to the subgroup's essence, not a word list.** Not an enumeration of the
   subgroup's member glosses — a label that names what the subgroup actually IS. Sharpens item 1
   below (which flags that no label is produced at all today) with what a correct one must contain
   once it is.
e. **A subgroup may legitimately hold exactly one strong**, if that strong's meaning is genuinely
   unique and doesn't fit any other subgroup — a singleton subgroup is a valid outcome, not a sign
   of a mis-grouping needing correction.
f. **`FLAG` conditions, precise list** (sharpens item 3 below): a strong is assigned to `FLAG` when
   it (i) has no inner-being implication, (ii) actually belongs to another cluster, or (iii) has
   some other anomaly preventing assignment — always with the reason recorded in `placement_note`.
g. **`placement_note` is not `FLAG`-only.** Any observation arising from a subgroup assignment — not
   just a `FLAG` placement's reason — is captured in `placement_note`. Revises §1's column
   description (below): required content for `FLAG` placements, optional but available for any
   ordinary placement too.

Previously resolved, kept for reference:

1. **A real `label` per family — not currently produced.** Process (b)'s JSON today leaves
   `family_label` always empty; `cluster_subgroup.label` is `NOT NULL`. This is a change the
   generation script needs, not a naming pick — see (d) above for what a correct one must contain.
2. Every strong placed in exactly one family (already process (b)'s own rule, now given a
   structural backstop by `cluster_subgroup_strong`'s tightened `UNIQUE(strong)`, §4 item 2).
3. A strong that doesn't fit any real family is signposted to `"FLAG"` (§3 item 3, now confirmed;
   conditions sharpened at (f) above) — the LLM writes this the same way it writes any other family
   placement, just under that special code, and **must record the reason for the FLAG assignment in
   `placement_note`** (g) — required content in the output JSON, not added later by a human.

## 3. The table-update procedure — what it must do

1. Assigns `cluster_subgroup.id` and `cluster_subgroup_strong.id` — the LLM never sees these.
2. Resolves each strong to its canonical `iba.strong.strongNumber` row (confirms it exists; not a
   bare, unchecked text code).
3. **CONFIRMED, researcher's own words, 2026-09-13 — FLAG subgroup mechanism.** Every cluster may
   have its own `subgroup_code="FLAG"` under that SAME cluster (e.g. M10's own FLAG bucket) — never
   a placement under a separate `cluster_code='FLAG'` cluster, which would itself already be a
   reallocation, the opposite of a signpost. Governing rules, verbatim in substance:
   - FLAG is for strongs that (a) have errors, (b) clearly belong to another cluster, or (c) must
     be re-allocated to a T-code.
   - Corrective action for a FLAG placement is to re-allocate the strong or resolve the underlying
     issue — FLAG is a signpost, not a resolution in itself (matches the earlier "signpost, not
     action it" framing from the naming-conventions review).
   - **FLAG members are never included in the next reading action for that subgroup** — the
     table-update procedure (or process (a)'s input assembly) must exclude `subgroup_code='FLAG'`
     strongs from the reading-stage input it hands to the LLM. New operational rule, not previously
     captured in #1691's process-(a) input spec — cross-reference for #1691 to pick up.
   - The FLAG membership **and its reason** must appear in process (b)'s own output JSON —
     `placement_note` is where that reason lives (§1).
4. Enforces `UNIQUE(strong)` on `cluster_subgroup_strong` — a term already placed elsewhere
   gets rejected or requires an explicit re-placement decision, not a silent second row.
5. **★ NEW, 2026-09-13 — see #1697 (`iba.cluster.status` lifecycle, part of the same sign-off
   pack):** process (b) must not run at all unless `cluster.status='ready_for_subgroup_allocation'`
   — a hard precondition, not advisory. On successful completion of this procedure's writes here,
   `cluster.status` advances to `ready_for_reading`. Full rule (including the `strongs_reassigned`
   reset triggered by any `cluster_strong` change) at #1697, not restated here.
6. **★ NEW, 2026-09-13 — see §3a below.** Assigns `cluster_subgroup.status='allocated'` when a fresh
   subgroup row is created; advances it per §3a's rule as reading/answer complete for that subgroup.

## 3a. `cluster_subgroup.status` — proposed values + gating rule (researcher-approved this round)

This table's own lifecycle, one grain finer than #1697's cluster-level status — a subgroup/family
is read and answered independently of its siblings (#1691 §2's own "each stage independently
re-runnable... for a single family/subgroup on its own"), so it needs its own progress marker,
distinct from `iba.cluster.status`.

| ordinal | value | meaning |
|---|---|---|
| 1 | `allocated` | just created by process (b); no reading has happened yet |
| 2 | `ready_for_reading` | precondition met for the reading stage (process c) to run against this subgroup |
| 3 | `ready_for_answer` | reading complete for this subgroup; awaiting the answer stage (process d) |
| 4 | `answer_complete` | answer complete; this subgroup's observations are eligible input whenever synthesis runs (synthesis is cross-family, #1691, so this subgroup has no "ready_for_synthesis" gate of its own the way a cluster does) |
| 5 | `completed` | this subgroup's reading+answer work is done; nothing further expected from it on its own |
| 6 | `re_read_needed` | this subgroup's own analogue to #1697's `strongs_reassigned` — set when `cluster_subgroup_strong` membership changes for this subgroup (a strong added/removed) while it's anywhere past `ready_for_reading`, since existing reading/answer observations may now rest on a stale membership list |
| — | *(`NULL`)* | the `FLAG` subgroup never enters this lifecycle — permanently excluded from reading (§3 item 3) — so it simply carries no status rather than an invented "not applicable" value |

Gating rule, mirroring #1693's cluster-level check/advance (#1697): the table-update procedure must
confirm `cluster_subgroup.status` matches what the requested stage needs before running it (reading
needs `ready_for_reading`, answer needs `ready_for_answer`), and advance it to the next value on
that stage's successful write — same shape as §3 item 5's cluster-level rule, one grain down.

**RESOLVED, researcher's own instruction, 2026-09-13 — cluster status is a rollup over this table,
not a redundant independent check.** `cluster.status` can only progress past `ready_for_reading`/
`ready_for_observations`/`ready_for_synthesis` once **every** subgroup in that cluster (excluding
the never-progressing `FLAG` one) has itself reached the matching level here. The actual per-run
precondition for reading/answer is this table's `status`, checked per-subgroup; `cluster.status` is
the aggregate reflection of that, recomputed (not just checked once) whenever a subgroup's status
changes — including regressing the cluster's rollup if a subgroup falls back to `re_read_needed`.
Full rule at #1697 §3.

## 4. Confirmed this round / already resolved

1. `label`'s `NOT NULL` gap — identified, needs a process-(b) generation-script fix, not a schema
   change.
2. `cluster_subgroup_strong`'s uniqueness constraint tightened to `UNIQUE(strong)` — answers
   the original "should one-strong-one-family be structural" question: yes.
3. A family is structurally single-cluster by construction (`cluster_code` required, singular) —
   researcher confirms this is expected ("unlikely, but not impossible" that the same subgroup
   concept recurs across clusters) with exactly one designed exception: `"FLAG"`, which is expected
   on every cluster.
4. **FLAG signposting mechanism (was §5 item 1) — RESOLVED**, see §3 item 3.
5. Table naming — `cluster_subgroup_strong` (was `mti_term_subgroup`), researcher's own rename,
   2026-09-13.
6. **DB location — REVERSED, 2026-09-13 (DB fork).** Both tables are new, in **`iba.db`**, not
   `bible_research.db` — corrects this doc's own earlier statement, made the same day before the
   fork; see the banner at the top of this document and #737/#1682 for the full reasoning. The
   `strong` FK (§1) replaces `mti_term_id`/`mti_terms.id` accordingly.

## 5. Still not settled

1. Family re-grouping/versioning if M10's families are ever re-derived — `version`/`status` exist
   as a starting point, not designed further than that. `status` no longer has the collision problem
   this item once flagged (§7 item 3, revised) — it's now a clean question purely about design, not
   about avoiding a data clash.
2. Table name — settled per §4 item 5. DB location — settled per §4 item 6.
3. §7's cluster/strong reassignment impact tracking — separate, not-yet-designed, not a blocker to
   finalizing this document.

## 6. What "finalized" would mean

**Revised 2026-09-13 (DB fork) — no legacy-table rename precondition.** Fresh
`characteristic`/`characteristic_subgroup`/`cluster_subgroup`/`cluster_subgroup_strong` tables are
created directly **in `iba.db`** per the DDL in §1, registered in `cfg_table`/`cfg_column` — nothing
in `bible_research.db` needs to move, rename, or even be touched first, since the fresh tables no
longer share a database (or a name) with the legacy 6. The table-update-procedure responsibilities
in §3 become part of #1693's full spec, same as #1691/#1692. §7 (cluster/strong reassignment impact
tracking) remains a separate, not-yet-designed requirement, not a blocker here.

## 7. New requirement — cluster/strong reassignment impact tracking — items 3/4 now resolved via #1697

**★ RESOLVED, 2026-09-13 — see #1697** (`iba.cluster.status` lifecycle enum + gating rule,
raised directly by the researcher this same session, part of the same sign-off pack). Item 3 below
is answered: the dedicated column gets built, named `status`, cfg_enum-governed. Item 4's flag
mechanism is answered too: `status='strongs_reassigned'` IS the flag — set automatically whenever
`cluster_strong` changes while the cluster isn't sitting at `ready_for_subgroup_allocation`. What
item 4 also asked for — a routine that, given the flag, considers existing `ib_observation` rows
and recommends a course of action — is **not** resolved by #1697; that routine's own logic remains
undesigned, #1697 only builds the flag it would read. Original framing kept below for record.

Researcher's own framing, verbatim in substance, 2026-09-13: strong membership in a *cluster* can
change over time, and that can invalidate existing *subgroup* membership derived from it. This has
wider implications than this document's own scope, recorded here because it originates from this
table's design review:

1. **New strong added to base data** → it must be assigned a cluster, and that must flag the
   cluster as changed and needing its subgroup determination (process b) rerun.
2. **Strong reallocated to a different cluster** → both the source and destination cluster's
   subgroup membership may be affected; this must be flagged so the impact on each can be assessed.
3. **Checked live, 2026-09-13, per the researcher's own instruction — REVISED after the DB fork:**
   does `cluster` have a `status` (or similar) field usable for this flag? The relevant table is now
   **`iba.cluster`** (the DB fork, banner above) — checked, and it has **no `status` column at all**,
   only `cluster_code`/`short_name`/`description`/`gloss`/`deleted`. There is no collision to avoid
   here (that was specific to `bible_research.db.cluster`'s own, different, frozen `status` column,
   irrelevant to this build now). A fresh, dedicated column can be added cleanly to `iba.cluster` —
   still an open design choice (name, and whether it belongs on `cluster` itself or a small separate
   tracking table), just no longer a values-collision question.
4. The flag triggers a **manual** resubmission of process (b) (subgroup generation) — not automatic
   — because a strong's cluster change may or may not actually change any subgroup determination.
   **A new routine is needed to assess the impact**: given the flag, it considers any existing
   `ib_observation` rows related to the affected strong and recommends a course of action, so the
   researcher isn't left re-running everything blind. This routine is completely undesigned —
   not proposed here, flagged for its own design pass (candidate for a dedicated escalation, same
   pattern as #1695 for the synergy stage, if the researcher wants it split out).
