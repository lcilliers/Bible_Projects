# #2448 — Reading opened on a collection: change list and test plan (design v2)

Status: design for the researcher's approval (B:105). Nothing is built. It follows design v1 (`2448-reading-by-collections-design-v1-20261110.md`), approved as recommended on 2026-11-10 (C1 to C7). Facts are from reads of `iba/app/lib/reading.py`, `iba/app/lib/versescope.py`, `iba/app/handlers/reading.py`, `iba/app/ps/Reading.ps1` and `iba.db` on 2026-11-10.

## A finding that changes C1
The `reading` table declares `home_cluster TEXT NOT NULL` with a foreign key to `cluster(cluster_code)`. A collection reading has no home cluster, so "leave `home_cluster` empty" (C1 A) is not possible as it stands: SQLite cannot drop a NOT NULL, so the table has to be rebuilt (new table, copy of the 10 rows, rename) by a migration script under `iba/app/migration/`, the app's established route for a schema change (the guide names migrations for config work in Developer Mode; configmaint changes rows only, never DDL).

**C1 (revised).**
- A (recommended): a migration rebuilds `reading` with `home_cluster` nullable and a new `collection_id INTEGER` (foreign key to `collection(id)`), plus a check that exactly one of the two is set. It registers the new column in `cfg_column` and runs once, then moves to `iba/app/migration/archive/`. The same unit adds the migration's `cfg_utility` row.
- B: no schema change: a collection reading stores its collection's id in `request` (JSON) and the home cluster of its first member's cluster; weaker, and a column that lies.
Question for you: may I run this migration in standard mode, as you allowed for the phrase step (it is a one-off script, not a config row)? Recommended: yes.

## Change list (as approved in v1, with C1 revised)
1. **Schema (C1 A):** the migration above.
2. **Scope (C2):** `iba/app/lib/versescope.py`: a selector `collection` (`Resolver.collection`): the verses of the occurrences of the surfaces that are live members of the named collection (tiers of `collection.export_tiers` plus `phrase`, joined through `verse_lexical.surface`); refuses a collection not `confirmed`, a retired or merged one, and one with no engagement observation.
3. **Open (C1, C6):** `iba/app/lib/reading.py` `open_`: `-Collection <name>` instead of `-Subgroup` (exactly one of the two); `collection_id` written, `home_cluster` NULL; the scope JSON names the collection; folder by C5. `-Subgroup` stays accepted until the cluster rules are retired (C7).
4. **Observe (C3):** `reading.observe` puts in hand, per verse, the engagement observations of the collection's surfaces (stage `engagement`: role, face) with the verse and passage; the verse is read first (B:116); Record is unchanged.
5. **Gaps (C4):** `reading.gap_types` (setting) gets the gap type `collection_unengaged` (a member surface with no engagement assessment in a verse of the scope) in place of `term_cluster` for a collection reading; `cfg_enum reading_gap_type` is changed with it.
6. **Files (C5):** `reading.output_dir` accepts a `{collection_folder}` pattern: `_analytics/Collections/{collection}/<label>/`; `out_dir()` in `lib/reading.py` resolves it.
7. **PS entry:** `iba/app/ps/Reading.ps1` takes `-Collection`; the `Reading` tab of `iba/docs/ps tools worksheet.xlsx` gets the column.
8. **Config, each through `configmaint.propose` (approval each):** the settings and enum values above; the cluster rules left for R2 A (below).
9. **R2 A, retire from the reading path:** behaviour rules 117 (subgroups-are-surface-groups), 118 (surface-mapping-conditions), 120 (scope-home-and-multiplicity) and 121 (reading-recorded-per-occurrence) are rewritten for collections in the same unit; 89, 94 and 115 and the 22 `cfg_method_rule` rows that mention clusters are listed row by row for your decision before any is changed (not decided here).
10. **Documents (R3 A):** a governance rule row quoting your words verbatim; `GOVERNANCE.md`, `USER-GUIDE.md` (Reading section) and BUILD.md updated in the same unit.

## Test plan (B:46), run on a scratch copy of `iba.db` before the live run
| # | Case | Expect |
|---|---|---|
| T1 | open on a confirmed, engaged collection | reading row with `collection_id`, no `home_cluster`; scope JSON lists the verses of its member surfaces |
| T2 | open with both `-Subgroup` and `-Collection`, or neither | refused, nothing written |
| T3 | open on a collection not `confirmed`, retired, merged, or unknown | refused, nothing written |
| T4 | open on a collection with no engagement observation | refused, naming the gap |
| T5 | a phrase-tier member's verses | included in the scope |
| T6 | Observe on the opened reading | per verse, the engagement observations of the collection's surfaces and the passage |
| T7 | a member surface with no assessment in a scope verse | gap `collection_unengaged` named in `Check` |
| T8 | an existing cluster reading (10 rows) | account, observe and check unchanged |
| T9 | the migration run twice | second run changes nothing; the 10 old rows kept byte for byte |
| T10 | real data: one engaged collection | verse count equals the count of verses of its member surfaces computed independently by SQL |
Results go into the build's escalation resolution, not only claimed (B:46).

## Order of work and what you approve
Approve: this change list with C1 revised (A, run in standard mode: yes or no), and the order: (1) migration, (2) scope and open, (3) observe and gaps, (4) files and PS entry, (5) config rows and rules, (6) documents, (7) pilot on one engaged collection (C6). I build step by step and bring each config row to you as I have with the phrase step. Nothing is built before your approval.
