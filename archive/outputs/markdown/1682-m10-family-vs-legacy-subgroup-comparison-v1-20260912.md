# M10: new gloss-based families vs legacy `cluster_subgroup` — comparison

**Status:** investigation only, read-only, no changes made. Requested this chat turn, ties directly
into escalation #1683 ("M10's 32 legacy characteristic rows vs Window 2") and #1690 (family design,
now blocked on #1683 — see `iba/docs/1682-cluster-reading-data-model-v1-20260911.md` §2).

## 1. Headline counts

| | Count |
|---|---|
| New (process-b) families | 15 buckets (14 + SUNDRY), 165 strongs total |
| Legacy `cluster_subgroup` rows for M10 | 34 (`M10-A`..`M10-X`, `M10b-A`..`F`, `M10c-A`..`E`) |
| Legacy active `mti_term_subgroup` memberships | 125 rows, 88 distinct strongs |
| Strongs in **both** | 59 |
| Strongs in **new families only** | 106 |
| Strongs in **legacy subgroups only** | 29 |

The legacy split is a genuine **many-to-many**: 125 memberships over 88 strongs means several
strongs sit in more than one legacy subgroup at once (e.g. a strong tagged both "Sin as committed
act" and "Wilful sinning"). The new families are strictly **one strong, one family** (process b's
own rule) — a structurally different shape, not just a different label set, confirming the
researcher's own read that the two groupings are "neither scientific nor precise" and don't line
up cleanly.

## 2. Cross-tab — for each new family, which legacy subgroup(s) do its strongs currently sit in?

| New family | strongs | have a legacy placement | legacy subgroup(s) hit (count of strongs each) |
|---|---|---|---|
| A_destroy | 31 | 7 | M10-H:3, M10-BND:4 |
| B_sin | 14 | 12 | M10-V:8, M10-W:5, M10-N:3, M10-T:3, M10-J:2, M10-L:2, M10-M:2, M10-O:2, M10-U:2, M10-C:2, M10-K:1, M10-P:1, M10-X:1 |
| C_adultery | 9 | 0 | *(none)* |
| D_crime_injustice | 14 | 10 | M10-I:6, M10-D:2, M10-E:1, M10-T:1 |
| E_corruption_perversion | 21 | 10 | M10-H:9, M10-BND:1 |
| F_violence_wound | 19 | 0 | *(none)* |
| G_transgression | 8 | 6 | M10-F:6, M10-J:1, M10-Q:1, M10-T:1, M10-W:1 |
| H_guilt | 7 | 3 | M10-D:3 |
| I_strife | 9 | 0 | *(none)* |
| J_unfaithfulness | 8 | 6 | M10-G:3, M10-F:1, M10-H:1, M10-S:1 |
| K_error_deception | 8 | 1 | M10-S:1 |
| L_defilement | 3 | 1 | M10-H:1 |
| M_cruelty | 4 | 0 | *(none)* |
| N_hypocrisy | 1 | 1 | M10-S:1 |
| SUNDRY | 9 | 2 | M10-D:1, M10-W:1 |

**Reading it:** no new family maps cleanly onto one legacy subgroup, or vice versa — every family
with any legacy overlap at all is scattered across 2+ old subgroup codes, and `B_sin` alone (a
*lexical* grouping) touches 13 of the 34 *characteristic*-based subgroups. This is direct, concrete
evidence for what the researcher's naming note predicted: family and `cluster_subgroup`/
`characteristic` are "different grains of the same concept," not interchangeable, and "the
contextual analysis of the terms will cause meaning to cross boundaries" — confirmed, not just
anticipated.

## 3. The 29 "legacy only" strongs — not a uniform gap, three distinct causes

| Cause | Count | What it means |
|---|---|---|
| `mti_terms.delete_flagged=1` | 10 | Correctly excluded from the new reading — these are dead rows, not a gap |
| Live in `mti_terms` (M10), but `cluster_strong` (iba.db, the *current* authoritative M-code assignment process (a) actually reads from) now has them under **`M10c`** | 9 | `cluster.M10c` itself is marked `status='Merged into M10 (2026-06-23)'` — the merge decision was recorded at the cluster-catalogue level in June, but the underlying `cluster_strong` rows for these 9 strongs were never actually migrated to `cluster_code='M10'`. Process (a)'s reading is correct against the CURRENT `cluster_strong` data; the merge is what's incomplete. |
| Live in `mti_terms` (M10), but `cluster_strong` now has them under **`M58`** | 10 | `M58` has no row at all in the `cluster` catalogue table (see §4) — these strongs were reallocated away from M10 into a cluster that isn't itself registered. |

None of the 29 represent a defect in process (a)/(b) — they're all correctly reflecting the CURRENT,
live `cluster_strong` assignment. The gap is entirely upstream: `mti_terms.cluster_code` (used by
the legacy `cluster_subgroup`/characteristic model) is stale relative to `cluster_strong` (the
current M-code source of truth), by at least these 19 strongs' worth.

## 4. A separate, bigger finding surfaced while checking this: 51 of 99 live `cluster_strong` codes have no `cluster` table row at all

Checked corpus-wide while chasing `M58`: **37 of them are M-codes** (`M32`, `M48`–`M84`) with real,
non-trivial row counts (`M55`: 72 rows, `M72`: 54, `M73`: 51 — not edge cases). CLAUDE.md's own
directory map only documents `M01`–`M46`/`FLAG`/`T2`. The other **14 are T-codes** (`T3`–`T15`,
some very large — `T3`: 2,586 rows, `T8`: 1,787) — these are very likely a deliberate, separately-
tracked classification (escalation #1606's own T-code sweep work references exactly this T3–T15
range as an active, known scheme), **not** the same kind of gap as the unregistered M-codes, and
not asserted as a defect here.

**Not resolved here — flagged as its own item, since it's well outside this comparison's scope**:
should `M48`–`M84` (and `M32`) be registered in the `cluster` table per `governance.tables`
("each table [cluster row] in the project must be listed... with a proper use text"), or is there a
reason a chunk of live M-codes were never catalogued there? Filed as a new escalation rather than
investigated further here.

## 5. What this means for #1683 / #1690

Concrete evidence, not just the structural collision already flagged: the 34 legacy `M10`
subgroups and the 15 new families disagree almost everywhere they overlap (§2), and the legacy
data itself is already partly stale against the *current* cluster-strong assignment, independent of
the family-vs-characteristic method question (§3). Both point the same way — the legacy
`cluster_subgroup` rows for M10 are not a safe base to extend or reconcile against; reproducing
under the new method (as the researcher already judged for the old `finding`-family tables) looks
like the lower-risk path here too, but that's the researcher's call on #1683, not concluded here.
