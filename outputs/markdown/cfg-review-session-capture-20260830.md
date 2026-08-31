# Session capture — the cfg per-table review debate, 2026-08-30

Full working record of one session's arc, kept because the thinking in it — not just its
conclusions — is worth having on file. Referenced from escalation #1235.

## 1. The catch that reframed the whole review

Working escalation #1128 (per-table cfg purpose/success review), `cfg_quality_check`'s
`genuinely-inner-being` row (phenomenon.set) was cleared as "correctly excluded — reasonableness,
no mechanical check possible, no gap." Researcher's direct challenge: *"I also do not see anywhere
what would actually be checked, how is inner-being defined... I specifically asked that the configs
should include specific portions of the prose which defines this... So I assume that the module
does not check if a phenomenon is inner being relevant, and would not know how to do it."*

Checked live: `cfg_prose_concept.inner_being_definition` exists — Chapter 1's actual definition,
created 2026-08-18 (escalation #714) explicitly to be *"the canonical reference, not a restated
rule text."* It is never read by any code anywhere in the app — grepped the whole repo, zero hits
outside its own migration. The module doesn't just lack a mechanical check (expected, a genuine
reading judgement); it has no live connection to the authoritative definition at all, despite one
existing for exactly this purpose. **The methodological error this exposed:** "no mechanical check
possible" had been treated as sufficient for "correctly excluded." It isn't — a second test is
needed (is there even a live definition wired in for the judgement to be made against), and one
row failed it while eight similar rows didn't.

## 2. "Are you prepared to certify this?"

Researcher's follow-up question, verbatim, after the above: *"Are you prepared to certify that you
have done the job properly?"* Answer given: no — not a hedge, a real no. The failure wasn't one
wrong row, it was a hole in the test being applied across the whole review, and there was no way to
know how many other "passed" rows shared it without re-tracing each one the way this one just got
traced. Committed to a corrected, five-part test (exists-where-expected / actually-consumed /
referential-integrity-of-content / cross-table-consistency / value-accuracy) — but this itself was
then challenged as too mechanical (see §3).

## 3. "Your steps a-e is pure mechanical, divorced from reality"

Researcher's sharper correction: a uniform checklist applied identically to every table, regardless
of what kind of thing the table governs, repeats the exact error just found — it tests structure,
not substance. *"if it is to control reporting - then does it ask the right questions for a report:
layout, content, headers, location etc; if it controls quality: does it include all the primary
areas that defines quality, (and pure existence is the lowest form of quality check); if
interpretation: does it have a frame of reference, is it clear, what else does it relate to."*

Corrected method: classify each table by the *domain* it governs first, derive independently from
that table's own governing source material what a complete picture would need to contain, and only
then compare the live config against that independently-derived standard — never against itself.
Demonstrated on `phenomenon.set`: read `WA-passage-read-guidance-v1.5` cold, derived six primary
quality dimensions the method itself names, checked the five existing `cfg_quality_check` rows
against that list. Five matched. One — whether a phenomenon's stated-vs-inferred status is recorded
*honestly* — had no check of any kind, mechanical or attestation. Existence of the schema column
(`phenomenon.status`) had been silently mistaken for coverage of this.

## 4. The `cfg_setting` challenge

Researcher: *"I am amazed that you left settings out. I would even be amazed if you come up with a
definition that let it feel as if settings really fulfill its purpose, and it not confusing."*
Investigated `cfg_setting` (169 rows, 21 `module` values) directly rather than leave the earlier
placeholder standing. Found it is not one coherent thing: (a) genuine standalone project-wide
policy with no dedicated table, and (b) subsystem tuning, some of which duplicates a dedicated
table's own jurisdiction. Concrete proof: `report.word` is a live row in *both* `cfg_report`
(`naming_scheme`, `archive_dir`) and `cfg_setting` (`report.output_dir`, `report.output_pattern`),
and a *third* mechanism, `governance.oneoff_report_*`, covers the same ground again — three
mechanisms, one concern, no reconciling rule anywhere. Written up in both tables' entries in
`cfg-table-purpose-success-review-v1-20260830.md`.

## 5. The programme-diagnosis tangent, and its correction

Asked to read the programme prose and IBA objectives and diagnose, structurally, why the programme
has stalled/reset repeatedly over eight months. Produced
`programme-control-gap-diagnosis-v1-20260830.md`: six candidate control gaps (no pilot-before-scale
gate, no method-version data stamping, no check-set completeness discipline, no reconciliation
governance between parallel mechanisms, no deliverable-path to the actual defined unit of success,
no pace/scope forecasting), grounded in the prose's own admissions (two live analytical mechanisms
"not yet reconciled"; no mechanism producing a per-word study at all; 49 of 18,558 passages debated
after eight months).

Researcher's correction, on two points: (1) factual — the "only six books read" figure was read off
the *current* debate pipeline's own stats and wrongly generalised to the programme's whole
book-by-book history; "almost the entire Old Testament" has in fact been read under prior method
generations, which the diagnosis never checked. (2) substantive, and sharper: all six items in the
diagnosis are facets of one root, not independent gaps — *"every one of the five methods that did
not make it... has the same root: how to read/digest, reliably and consistently, what verses say
about the inner being... every tested method in prototyping failed because the same process could
not be repeated with the same rigour, consistency and compliance."* IBA itself — the whole app,
config-governed, everything captured in structured databases — is the programme's own,
already-executed architectural answer to exactly that root cause, not a missing control to be
newly recommended. Confirmed directly in the prose's own words (`prog_disc_tools`): *"the programme
continued to wrestle with consistency and repeatability [and] the tool set migrated... to the
concept of a integrated Inner Being Application."*

The sharpened, corrected diagnostic point, reached jointly: the missing thing is not a bigger pilot
or more forward coverage — there has been plenty of that, across five method generations. It's a
demonstrated *repetition* test: has any method version ever been run twice, independently, on the
same material, and shown to converge on the same reading? That specific test — as distinct from
procedural repeatability (does the same discipline fire every time, which IBA does genuinely fix)
— had not been confirmed to have been run. Researcher noted a live escalation is already working the
analytic-arc redefinition and has already reached the same "book-by-book is not the right
organising method" conclusion independently, with more ground truth than this diagnosis had. Agreed
this tangent, however useful as a conversation, adds nothing further to the cfg-table validation
work and was closed without further action on the diagnosis document.

## 6. The uncaptured-analytics-domain observation

Researcher, closing: the cfg review so far (prose, passage, hib, phenomenon, operation) covers only
the newest layer of the current debate pipeline. The much larger accumulated analytical learning —
clusters, dimensions, the observation-question catalogue, characteristics, movement/process theory,
non-human-being handling — has never been normalised into config at all, because IBA has only just
started pulling that whole layer in. Confirmed live: `cfg_method_rule`/`cfg_quality_check` cover
exactly five steps, all from the current debate pipeline; `cluster.assign`/`cluster.validate` are
live, active, running code with **zero** rows in either table; the 2026-08-13 correction ("no bulk
keyword-crossmatch, must be verse-context-grounded") is enforced in neither code nor config;
dimension assignment and the catalogue don't even have a registered `cfg_step` yet; `cfg_enum` has
exactly one group (`hib_kind`) for this entire domain. Proposed, without deciding: this content
likely maps onto the same four existing mechanism-shapes (`cfg_method_rule` for process discipline,
`cfg_quality_check` for per-decision judgement tests, `cfg_prose_concept` for definitional grounding,
`cfg_enum` for controlled vocabulary) rather than needing a new one — but untested, and the
researcher was explicit that this is deliberately left open rather than designed now: *"we will put
[these] through several rounds of testing when we start with building out the analysis... instead
of trying to revisit these considerations in isolation we will refine it while doing the work and
using it."*

## 7. Closing actions taken this session (researcher's four-part direction)

1. Final, standalone purpose/success text proposed for every table whose original text was found
   shallow — 17 `cfg_table_purpose` updates plus the 2 direct config-content fixes below, all via
   `configmaint.propose`, all pending researcher approval (see escalation #1235 for run ids).
2. This document.
3. The two clear, provable, config-only fixes from this session proposed for approval:
   `linkage-genuinely-registered`'s `test_kind` corrected `existence` → `reasonableness`; a new
   `cfg_quality_check` row added for `phenomenon.set` (`stated-or-inferred-honestly-assigned`).
   Fixes requiring a code change rather than a config value (the `hib.set` set-aside cross-check;
   wiring `genuinely-inner-being` to its prose definition; the `cfg_write_grant` scope question on
   `cfg_change_detail`/`cfg_change_log`) remain on their own escalations (#1235, #1146) as
   decision-required, not silently written.
4. The cluster/dimension/catalogue/characteristic domain, and the report/`cfg_setting` jurisdiction
   overlap, are deliberately left untouched pending the analysis-build work itself — noted, not
   fixed, per the researcher's explicit direction above.
