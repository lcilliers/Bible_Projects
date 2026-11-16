# Collection index check

Generated 2026-11-15T05:07:25Z by run RUN-20261115_050725_027-COLLECTIONBUILD (`Collection-Build.ps1 -Action IndexCheck`, escalation #2503). Read-only on the tables. Counts: {'index rows': 3437, 'unplaced': 3437, 'placed': 0, 'isolated': 0, 'subgroups': 0}.

## member-with-no-index-row: 0

a member surface of a confirmed collection with no live row in the index (run Index).

## index-row-of-a-surface-that-left: 0

a live index row whose surface is no longer a member of that collection (run Index).

## surface-in-two-collections: 0

a surface reached by more than one confirmed collection (a surface is in exactly one, B:129).

## duplicate-live-row: 0

two live rows for the same (collection, surface, Strong's code).

## split-rule-broken: 0

a surface with a row for the whole surface and a row for a Strong's code (the rows are all whole or all by code).

## placement-does-not-agree: 0

a placed row with no live subgroup of its own collection, or an unplaced or isolated row with a subgroup.

## shared-flag-without-a-second-link: 0

a live member link flagged shared whose term has no second live member link (the flag may be stale; not changed here).

## node-group-does-not-agree: 0

live nodes whose subgroup_id differs from the group their surface is placed in (run Collection-Build.ps1 -Action NodeGroups).

