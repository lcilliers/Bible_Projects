# Your config-management expectations (a-g) against the project's own written history

> Requested 2026-07-29: were expectations (a)-(g) already established (in `BUILD.md`/
> `GOVERNANCE.md`/`USER-GUIDE.md`/memory), or are they new? Read `GOVERNANCE.md` in full (1162
> lines), the relevant `BUILD.md` sections (§9, §14, §15D, §23, §31), `USER-GUIDE.md`, and this
> assistant's own persistent memory. Every quote below is sourced with a file/section/date —
> nothing asserted from recollection alone.

## The short answer

**Every one of the seven expectations is already on record — several as the project's own
self-imposed standing rules, one of them (value-quality ≠ structural validation) already learned
from a near-identical incident 8 days before the passage hodgepodge, and one specific gap (a) named
in writing as a known, deliberately-deferred risk 6 days before it nearly caused a real mistake
(escalation #334, 2026-07-29). This was not a case of unstated or unclear expectations. It was a
case of documented rules — some self-imposed by the app's own governance record — not being
carried forward into the passage-config work.**

---

## (a) Every active config used in a routine / no config silently governs nothing

**Already documented, and the specific gap already named.** `GOVERNANCE.md` §15D (2026-07-23):

> "**Deliberately not built:** `inactive` only excludes a row from `configmaint.validate`'s checks —
> it does not stop `run.py`'s dispatcher from actually executing a deactivated step... Blocking
> execution outright is a different, not-yet-made decision... not assumed here, **flagged for
> whenever the actual replacement system is being designed.**"

This is verbatim the mechanism behind escalation #334 (2026-07-29): `Set-Candidates.ps1 -Book Obad`
nearly ran despite its work package being `inactive=1`, because nothing stops it. §15D named this
risk in writing on 2026-07-23 and explicitly deferred it to "whenever the actual replacement system
is being designed" — the passage repurposing (§28, 2026-07-27) *was* that replacement system being
designed, and the deferred check was not revisited then.

## (b) No hardcoded logic that should be config-driven

**Already the project's central, repeated organising principle**, stated as early as `GOVERNANCE.md`
§1 (2026-07-17): *"The rules ARE the config... The code decides nothing."* And directly generalised
by the researcher, `GOVERNANCE.md` §16 (2026-07-26 — **the same day** the passage system was
retired):

> *"ALL rules must be config driven. NO rules should be specified only in Governance or Build or
> Memory or User Guide that is not in the config."*

§16 was written in direct response to a concrete violation found that day (`step.required_for_runs`
existing only as hardcoded `init.py` logic + prose). The gap analysis found the same shape of
violation again in `run.py`'s `PATH_EXIT` dict and in `lib/cfgquality.py`'s own hardcoded completeness
lists — the standard was already stated in the clearest possible terms; it wasn't re-applied to the
validator's own code, or to `run.py`, when this was written.

## (c) Every table-writing routine has the full standard config bundle (column controls, processing rules, validation, error handling/notification, reporting)

**Already built as a stated goal, in stages, with the researcher naming the exact bundle.**
`GOVERNANCE.md` §13 (2026-07-22) quotes the researcher directly:

> *"the need for, the type of, and the location of the report is config driven for ALL reports... the
> content of the report is also config driven... run completion, and exception notification... all
> need to be config driven."*

This produced `cfg_report`/`cfg_report_section`/`cfg_report_csv_table`/`cfg_on_fail.route`/
`cfg_work_package.complete_message` — real infrastructure built specifically to make this bundle
checkable. But the *check* that every routine actually has the full bundle was never built as a
completeness sweep — only the two narrow, hardcoded lists (`REPORT_STEPS`,
`QUALITY_CHECK_REPORT_PATH`) exist, which the gap analysis showed miss 11 active steps (no
`cfg_on_fail`) and 6 (no `cfg_report`).

## (d) Every utility routine is fully governed by config

**Already the founding principle for "utilities" specifically** — `GOVERNANCE.md` §9A's title:
*"the utility that governs the governor"* — `configuration_maintenance` was built in the first place
because *"until 2026-07-21 it didn't exist as a registered utility — `cfgload.py`/`cfgcheck.py`/
`cfgreport.py` were standalone scripts nothing else in the app knew about."* The same gap was found
and fixed again for `report.py`/`validation.py` (§9C) and `log-retention`/`export_tables_csv` (§13).
**The pattern of finding one more ungoverned utility and registering it has recurred at least three
times already** — it was never turned into a standing completeness check (a registry of *all*
utilities to test against), so it can keep recurring instead of being closed once.

## (e) Structurally complete, not duplicated, not conflicting

**Already stated as an explicit requirement**, `GOVERNANCE.md` §13.9.1 (researcher, 2026-07-22,
quoted in §13's ownership-ledger section): *"must not conflict with each other."* The response built
was an ownership ledger (one table, "config item governs exactly one thing") — a *design*
discipline, not a *checked* one. The gap analysis's two found conflicts (`passage.review_over`
code-default `5` vs. DB value `10`; `step.expect_min_verses` code-default `1` vs. **active** DB
value `1000`) are exactly the class of conflict §13.9.1 asked to prevent, found live, never
mechanically checked for.

## (f) Cross-references between configs are not broken or incoherent

**Directly the same discipline behind the FK/PK/enum checks already built** (`GOVERNANCE.md` §9A,
2026-07-21 review pass — global step-name uniqueness, orphan detection). The principle was already
established and partially built; it was simply not extended to the other cross-reference shapes
(`cfg_write_grant.writer`, `cfg_column.filled_by`) that the gap analysis found unchecked — the same
"found one, should generalise, didn't" pattern as (d).

## (g) The config text is behaviourally live (changing it would change processing)

**Already the project's own standing "proof of life" test**, stated outright in `GOVERNANCE.md` §4:

> *"Proofs it is real, not decorative... A rule change in the DB changes behaviour, no code touched."*

And demonstrated as the actual bar to clear in §16's `step.required_for_runs` fix: *"Flip it to
`false` and both actually respond... which is this project's own standing proof-of-life test for
'is this a real rule or decorative.'"* The bar was named and demonstrated on one setting. It was
never turned into a check run against *every* setting — which is exactly why `passage.cross_chapter`
(found live, still true today: read, but the code's own comment admits it can't deliver true
chapter-boundary crossing) sits in a state the project's own standard says should not be allowed to
persist unexamined.

---

## Memory: this exact category of failure was already recorded — 8 days before it recurred

`feedback_structural_validation_is_not_value_quality_validation` (this assistant's own persistent
memory, written 2026-07-21, i.e. **8 days before** this session's passage findings):

> *"Treating 'a validate step exists and reports clean' as 'this data is trustworthy' is a category
> error... On audit, EVERY validate step in the app (`configmaint.validate`, `candidate.validate`,
> `passage.validate`, `validation.py`) checked structure only; none checked value quality."*

That memory's own **"How to apply"** line: *"When auditing one table/column for this reason, audit
the pattern across the whole schema in the same pass... Do not stop at the first instance found."*
The passage hodgepodge is the same pattern recurring in the same module (`passage.validate`) that
memory names by name — not a new failure mode, a repeat of an already-recorded one.

## `GOVERNANCE.md`'s own currency rule was not honoured for the passage work

`GOVERNANCE.md` §8 states a rule the researcher had approved and applied as `cfg_setting` rows
(escalations #238/#239, both **LIVE**): *"any governance/config-rule change must be set in `cfg_*`
first, then `GOVERNANCE.md` updated to reflect it, same unit of work."* `BUILD.md` correctly
recorded the passage-system retirement (§23, 2026-07-26), repurposing (§28, 2026-07-27), and
reactivation (§31, 2026-07-28) — all real `cfg_*` rule changes. **`GOVERNANCE.md` has no
corresponding entry for any of them** — its last section (§16) is dated 2026-07-26, *earlier the
same day* as §23's retirement, and nothing after it exists. The rule this file states about its own
currency was not applied to itself for exactly the body of work under review here. (§8 does note
honestly that nothing *enforces* this — it's a stated standard, not a checked one — which is itself
the same category of gap as everything above.)

`USER-GUIDE.md` §8 still shows `passage.build`("recomputes this book's passages from
`span_candidate`") as live, current example output — unchanged since before the 2026-07-26
retirement.

---

## Conclusion

None of (a)-(g) is a new bar. Each maps onto a standard the project already wrote down for
itself — several in the researcher's own words, one already relearned once in memory, one already
named as a known deferred risk that then materialised almost exactly as predicted (#334). The
gap was not in what was expected; it was in carrying an already-established standard forward
consistently into a fast-moving piece of work (the passage method's three rewrites in four days,
2026-07-26 to 2026-07-29) instead of treating each of those standards as a checklist to run before
calling that work done.
