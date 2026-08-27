# Related-activity summary — mockup

> Built from live data (183 escalations, all states), not synthetic. Goal: would a rollup at the
> top of the list/history report actually make the sprawl more legible, or just move the bulk up
> a level? Short answer, found while building this: **the literal ask (group by exact
> `related_activity` text) has real value but also a real flaw — it fragments your biggest threads
> instead of revealing them.** Both shown below, plus what a fix would cost.

## Mockup 1 — exact-match grouping (literally what was asked)

**183 escalations, 49 distinct `related_activity` strings.**

| related_activity | items | total versions |
|---|---:|---:|
| escalation-cli-crash | 31 | 70 |
| configmaint.validate | 29 | 79 |
| configmaint.propose | 27 | 70 |
| *(none)* | 19 | 57 |
| test.step | 11 | 26 |
| escalation-module-rebuild-20260820 | 7 | 44 |
| Not related | 6 | 17 |
| escalation-redesign-followups-20260820 | 6 | 23 |
| escalation-utility-refinement, related #753 | 3 | 18 |
| prose.import_chapter | 3 | 6 |
| Prose management root | 2 | 37 |
| escalation-module-rebuild-20260820, spawned from #767 | 2 | 8 |
| *(38 more, every one a singleton — 1 item each)* | 38 | ~170 |

**This alone is already useful** — the top 5 rows tell you immediately that ~117 of 183
escalations (64%) sit in 5 buckets that are almost certainly operational noise (crash
self-logging, routine config-propose approvals, ad-hoc test scaffolding), not substantive threads.
A reader could skip straight past them to the real work below.

**Two fully expanded, to show what "short description per branch" looks like in practice:**

### `escalation-cli-crash` — 31 items, 70 versions
```
#2 (closed)     escalation CLI crashed: short_description is 90 chars, over...
#3 (closed)     escalation CLI crashed: short_description is 63 chars, over...
#765 (withdraw) escalation CLI crashed: next_action='ready_for_approval' re...
#769 (withdraw) escalation CLI crashed: an update carrying comment/context/...
#772 (withdraw) escalation CLI crashed: short_description is 64 chars, over...
#788 (completed) escalation CLI crashed: short_description is 981 chars, ov...
... (25 more, same shape)
```
**Not actually useful at the branch level** — every one of the 31 reads "escalation CLI crashed:
<some validation message>". Reading all 31 titles adds almost nothing over the row's own "31
items" count; the count alone already says "this is noise, don't open it."

### `escalation-module-rebuild-20260820` — 7 items, 44 versions
```
#4  (completed) escalation cfg_table.use text still describes retired design
#5  (completed) escalation id sequence collides with escalations_old
#6  (completed) Escalation rebuild follow-ups outstanding, per #753
#761 (completed) -AnsweredBy required friction in researcher's own terminal
#762 (completed) Explicit -State loses to assignee_changed in update()
#763 (completed) from_id built immutable, contradicting recorded instruction
#764 (completed) Recently-resolved table had no short_description column
```
**Genuinely useful** — 7 distinct, meaningful sub-topics, readable as a map of the whole rebuild
effort in 7 lines instead of opening 7 separate multi-version tables.

**So the value is real but uneven** — it's exactly the noisiest, most auto-generated groups where
branch-level detail adds least, and exactly the substantive groups where it adds most. A blanket
"always list every branch" would still bury the 7 good lines under the 31 near-duplicate ones from
the row above it.

## The flaw, found building this — exact-match fragments your biggest threads

The `escalation-module-rebuild-20260820` row above says "7 items" — **but it isn't 7, it's 17.**
Checked directly: 9 more escalations carry `related_activity` starting with the identical prefix
but a different free-text tail, so exact-match treats each as its own unrelated group of 1:

```
escalation-module-rebuild-20260820                                        7 items, 44 versions
escalation-module-rebuild-20260820, spawned from #767                     2 items,  8 versions
escalation-module-rebuild-20260820, found raising #767                    1 item,  11 versions  (#768, just closed)
escalation-module-rebuild-20260820, found while answering #794            1 item,  12 versions
escalation-module-rebuild-20260820 (related, not a subtask -- see #6)     1 item,   8 versions
escalation-module-rebuild-20260820 -- spawned from #8's own investi...    1 item,   6 versions
escalation-module-rebuild-20260820 (found reviewing D1's dry-run JS...    1 item,   6 versions
escalation-module-rebuild-20260820, #753's own still-open core ques...    1 item,   7 versions
escalation-module-rebuild-20260820, found investigating #784/#787         1 item,   4 versions
escalation-module-rebuild-20260820, prompted by #795's two self-fou...    1 item,   2 versions
```
**Real total: 17 items, 108 versions** — the actual biggest thread in the whole table, and exact
grouping shows you 10 separate small rows instead of the one that matters. A crude fix (group by
the text before the first comma/dash/paren instead of the full string) recovers this one
correctly:

| prefix group | items | versions |
|---|---:|---:|
| escalation-cli-crash | 31 | 70 |
| configmaint.validate | 29 | 79 |
| configmaint.propose | 27 | 70 |
| *(none)* | 19 | 57 |
| **escalation-module-rebuild-20260820** | **17** | **108** |
| test.step | 11 | 26 |

...but it does **not** fix the other big one. The whole prose-management saga you closed out
today (#784 → #829 → #831/#832/#835 → #836 → #890 → #908) never shares a common prefix at all —
each escalation wrote its own descriptive sentence:

```
Prose management root                                                (#784)
prose-management-iba-first-layer, spawned from #784                  (#829)
prose-management-iba-add-edit-layer, builds on #829... spawned #784  (#831)
prose_section data-hygiene, found auditing #829, spawned from #784   (#832)
prose-quality-flag-fix-utility, ...designed at #829, spawned #829/#833  (#835)
prose-change-log-design, spawned from #829 sec 6a...                 (#836)
prose-management-add-edit-rules, replaces rejected #831/#835/#832... (#890)
prose-functionality-test, builds on #829/#890                        (#908)
```
No text-matching heuristic — exact or prefix — will ever unify these; they're related by
**meaning** (`from_id` chains and `#NNN` mentions inside the free text), not by shared wording.
That's a fundamentally different, better-grounded kind of grouping — and the pieces already exist:
`_find_missing_link`/`_find_incoherent_link` already parse `#NNN` mentions out of `related_activity`
for the coherence checks; a real "cluster" view would walk `from_id` children plus those `#NNN`
mentions transitively, the same graph `write_history_report` already builds for the D15 checks, just
reported as groups instead of exceptions.

## Where this leaves it

Three real options, increasing cost and correctness:

1. **Exact-match** (what was literally asked) — cheap, already demonstrated above, real value for
   spotting noise clusters, but silently under-counts your real threads (the module-rebuild case).
2. **Prefix heuristic** — one extra line of string-splitting, fixes the module-rebuild case, still
   misses anything (like prose-management) that isn't textually consistent.
3. **Graph-based** (`from_id` + `#NNN` mentions, transitively) — correct for both cases shown here,
   reuses machinery that already exists for D15, but is a real small build, not a report tweak.

Nothing built into the actual report yet — this is the mockup, for you to react to before I touch
`write_list_report()`.
