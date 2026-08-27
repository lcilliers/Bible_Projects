# `from_id` data-quality audit

> You're right that `related_activity` is only a label — the real relationship is `from_id`, and
> you noted it's not well used. Checked live, not assumed. 3 real gaps found and fixed; everything
> else below is either confirmed correct or a structural limit already documented at #768/§56, not
> a new bug.

## Overall usage (183 escalations)

| state | count | % |
|---|---:|---:|
| `from_id` set to a real parent | 47 | 26% |
| `from_id = -1` ("checked, no parent found") | 81 | 44% |
| `from_id` NULL (never even checked) | 55 | 30% |

30% of the table was never even given the `-1` sentinel — genuinely unchecked, not "checked and
found nothing."

## Fixed — 3 clear, single, unambiguous gaps

Method: of the 55 NULL rows, checked which ones name an explicit `#NNN` **in their own
`related_activity` field** (not `comment` — that's far noisier, full of quoted crash tracebacks and
migration-note boilerplate that produced false matches on a first pass). 10 do. Of those 10, 3 name
exactly one parent, plainly:

| # | `related_activity` said | Fixed to |
|---|---|---:|
| #828 | "prompted by #795's two self-found build gaps" | `from_id = 795` |
| #836 | "spawned from #829 sec 6a (D7 elevated)" | `from_id = 829` |
| #854 | discovery involved 5 items, but its own disposition is explicit: "fold into #831's build, not a standalone fix" | `from_id = 831` |

Applied via `-Action Correction` (all 3 confirmed live afterward).

## Not fixed, and correctly so — 7 multi-reference cases

The other 7 of the 10 name *more than one* prior escalation in their own `related_activity`
(`"spawned from #829/#833"`, `"fix depends on #881/#882"`, etc.) — `from_id` is a single `INTEGER`
column, structurally incapable of holding more than one parent. This is the exact same finding
already investigated and documented for #768 (`GOVERNANCE.md` §56): #790, #835, #851, #855, #859,
#867, #908. Nothing to fix here without widening `from_id` itself to something multi-valued — a
real schema question, not a data-entry gap, and out of scope for this audit.

## Checked, not a bug — 4 `-1` sentinels that also carry a `#NNN` reference

#736/#737/#738/#739 all carry `from_id = -1` *and* a `#NNN` mention in `related_activity` — looked
like the `-1` check might have been wrong. It wasn't: every one of those references
`escalations_old #NNN` — the **retired, pre-rebuild** numbering scheme, a different table
entirely. `-1` ("no parent found in the current system") is the correct answer; the named parent
genuinely doesn't exist in the live `escalation` table. No action.

## Checked, not a bug — 2 cases where `from_id` doesn't match `related_activity`'s own refs

- **#786** — `from_id=784`, but `related_activity` separately flags *"likely duplicate of #739"*.
  Not a conflict: `from_id` records the real structural parent (Prose management root); the #739
  mention is a distinct duplicate-risk flag, not a competing parent claim.
- **#890** — `from_id=784` (root of the whole prose-management effort), while `related_activity`
  names its immediate predecessors (#829/#831/#832/#835). Both are true — this is the same
  single-vs-multi-parent limitation as the 7 cases above, just visible from the other side (a real
  `from_id` was set, but to a different level of the chain than the narrative text emphasizes).
  Not incorrect, just not the only defensible choice — I set it when raising #890 this session.

## What this confirms about the earlier grouping mockup

`from_id` alone still wouldn't fully solve the fragmentation shown in the related-activity mockup
— 7+ of the real "multi-parent" cases above are exactly the ones a single-`from_id` graph walk
still can't unify (e.g. #908 → both #829 and #890 are true parents, but only one can be `from_id`).
A correct graph view needs both `from_id` **and** the `#NNN` mentions in `related_activity`,
walked together — which is what the existing D15 checks (`_find_incoherent_link`) already do for
coherence, just not yet reported as a grouping.
