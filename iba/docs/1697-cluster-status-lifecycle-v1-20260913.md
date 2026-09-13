# Escalation #1697 — `iba.cluster.status` — lifecycle enum + gating rule

**Status:** design proposal, decision_required. Nothing built. Part of the sign-off pack with
#1690/#1691/#1692/#1693/#1696 (per #1682's banner) — none of the six build until all six are
signed off together.

**Origin:** raised directly by the researcher this chat turn, on top of #1690 §7's finding that
`iba.cluster` has no `status` column at all (checked live, 2026-09-13). This is the design for that
column — and it turns out to be exactly the mechanism #1690 §7 flagged as needed but undesigned:
a way to know when a strong's cluster reassignment invalidates downstream subgroup/reading work.

## 1. The column

```sql
ALTER TABLE cluster ADD COLUMN status TEXT;   -- cfg_enum-governed, see §2
```

Single column on `iba.cluster` (100 live rows today). Not a separate tracking table — the
researcher's own instruction was to add the column directly.

## 2. The enum — researcher's own words, verbatim order

| ordinal | value | researcher's own wording |
|---|---|---|
| 1 | `strong_assignment_in_progress` | "strong assignment in progress" |
| 2 | `t_cluster_assignment_completed` | "T-cluster assignment completed" |
| 3 | `ready_for_subgroup_allocation` | "ready for subgroup allocation" |
| 4 | `ready_for_reading` | "ready for reading" |
| 5 | `ready_for_observations` | "ready for observations" |
| 6 | `ready_for_synthesis` | "ready for synthesis" |
| 7 | `completed` | "completed" |
| 8 | `strongs_reassigned` | "strongs re-assigned" |

Snake_case values proposed here for `cfg_enum` storage, matching this project's existing enum
convention (e.g. `behaviour_rule_enforcement_status`) — the researcher's own wording (middle
column) is the authority on meaning; confirm or correct the exact value spellings before building.

**Not yet confirmed, flagged not assumed:** whether ordinals 1–2 (`strong_assignment_in_progress`,
`t_cluster_assignment_completed`) describe the `cluster_strong` population phase (candidate-code
assignment, T-code triage, #1606/#1694's own work) as distinct from ordinals 3–7 (the cluster-
reading pipeline this session's #1690–1693 design covers) — read that way here since it fits the
existing project shape, but not stated explicitly by the researcher and worth confirming.

## 3. The gating rule

**RESOLVED, researcher's own instruction, 2026-09-13 — cluster status is a ROLLUP over subgroup
status, not an independent per-stage gate.** Reading/answer run per-subgroup (#1690 §3a, #1691 §2),
so `cluster.status` for the reading/observations/synthesis span reflects what *every* subgroup in
that cluster has collectively reached — it doesn't gate an LLM session directly the way
`cluster_subgroup.status` does.

1. **Reassignment reset.** Whenever a strong is re-assigned to or from a cluster (a `cluster_strong`
   change) **while that cluster's `status` is anything other than `ready_for_subgroup_allocation`**,
   the cluster's `status` must be reset to `strongs_reassigned`. (If the cluster is already sitting
   at `ready_for_subgroup_allocation` — i.e. nothing downstream has consumed the membership yet —
   a reassignment doesn't need to interrupt anything, since subgroup allocation hasn't run against
   stale data yet.) This one is genuinely cluster-level — `cluster_strong` membership, not a
   subgroup concern.
2. **`ready_for_subgroup_allocation` → `ready_for_reading`** — a direct, cluster-grain transition:
   process (b) runs once per cluster, and the table-update procedure advances `cluster.status` on
   its successful write, same as before. Not a rollup (nothing to roll up yet — subgroups don't
   exist until process (b) creates them).
3. **`ready_for_reading` → `ready_for_observations` → `ready_for_synthesis` → `completed` — ROLLUP,
   not a single write.** The cluster only advances past a level once **every one of its subgroups**
   (`cluster_subgroup` rows for that `cluster_code`) has itself reached the matching level:
   `ready_for_observations` requires every subgroup at `ready_for_answer` or beyond (§1690 §3a);
   `ready_for_synthesis` requires every subgroup `answer_complete` or beyond; `completed` requires
   every subgroup `completed` **and** the cross-family synthesis stage itself having run for that
   cluster (synthesis isn't subgroup-scoped, #1691, so this last leg has no subgroup rollup input
   the way the first two do — it's the cluster's own event). **`subgroup_code='FLAG'` is excluded
   from this rollup** — it carries no status and never enters the lifecycle (#1690 §3a), so
   including it would deadlock every cluster's rollup permanently.
4. **The rollup is recomputed on every subgroup status change, not just checked at advance-time.**
   A subgroup falling back to `re_read_needed` (its own membership-change reset, #1690 §3a) means
   the cluster no longer genuinely satisfies "all subgroups at X" for whatever level it had rolled
   up to — the cluster-level status regresses with it, mechanically, not just held stale at its last
   computed value.

This directly resolves #1690 §7 item 4's "a new routine is needed to assess the impact" — the
`strongs_reassigned` status itself *is* the flag that routine was going to need to look for; whether
a further routine still needs to interpret *what to do* once a cluster lands in `strongs_reassigned`
(re-run subgroup allocation automatically vs. surface it for manual resubmission, #1690 §7 item 4's
own "manual resubmission" framing) is not re-litigated here — the flag mechanism is what's being
built, not that routine's own logic.

## 4. Cross-document impact — noted on each design doc this round

This status/gating mechanism touches every stage #1690–1693 define, so a pointer to this escalation
has been added to each:

- **#1690** (`cluster_subgroup`/`cluster_subgroup_strong`) — process (b) checks
  `cluster.status='ready_for_subgroup_allocation'` before running (cluster-grain, §3 item 2); its
  own §3a defines `cluster_subgroup.status`, the table this escalation's rollup (§3 item 3) actually
  reads from.
- **#1691** (`ib_observation`) — reading/answer/synthesis's *real* precondition is
  `cluster_subgroup.status` (#1690 §3a), since those stages run per-subgroup — `cluster.status`'s
  `ready_for_reading`/`ready_for_observations`/`ready_for_synthesis` values are the rolled-up
  reflection of that, not an independent gate an LLM session checks directly.
- **#1692** (`ib_node`) — no direct gating role (rows are derived from `ib_observation`, not
  independently staged), noted for completeness only.
- **#1693** (table-update procedure) — implements both levels: the subgroup-level precondition
  CHECK/ADVANCE (#1690 §3a) on every reading/answer write, and the rollup recompute (§3 item 3-4
  above) that decides whether `cluster.status` itself also advances or regresses as a consequence.

## 5. Still open — not decided here

1. Exact `cfg_enum` value spellings (§2) — confirm or correct.
2. Whether ordinals 1–2 belong to the `cluster_strong` assignment phase or something else (§2).
3. What "ready for observations" precisely gates — presumed the answer stage (process d), not
   confirmed.
4. Whether landing in `strongs_reassigned` triggers anything automatic, or is purely a manual-
   resubmission signal for the researcher (#1690 §7 item 4) — the flag exists either way; this is
   about what reads it.
5. Initial backfill — 100 live `iba.cluster` rows today have no status. What do they start at?
   (Likely `strong_assignment_in_progress` or `t_cluster_assignment_completed` for most, but real
   values need checking against `cluster_strong`'s actual state per cluster, not assumed.)

## 6. What "finalized" would mean

Once §5 is resolved and the sign-off pack (#1690/#1691/#1692/#1693/#1696/#1697) is approved as a
set: the `ALTER TABLE` in §1 executes, the enum is registered in `cfg_enum`, `cfg_column` gets the
new column's `use` text, and #1693's procedure spec gains the precondition-check/postcondition-
advance logic described in §3–4.
