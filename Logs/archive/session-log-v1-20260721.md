# IBA Session Log — v1, 2026-07-21

**Topic:** From the v2 concordance plan's open questions, through a documentation-synthesis failure and
its correction, to an approved-pending **Application Design v1** — the build specification for the IBA
app, grounded against the actual built app rather than assumed from documents.

**Outcome:** ✅ `iba-application-design-v1-20260721.md` drafted (12 sections, config principles a–k
restated as the governing north star) and **revised same day** against the researcher's review comments.
Six of eight original open items resolved; **5 items remain open**, the key one being §11 item 1
(**`char_key` normalisation** — is base-lemma+gloss a sufficient dedup/identity key). Researcher will
do research/prototyping on the open items before the design document work resumes.

---

## 1. Trigger

Continuing from `iba-application-plan-v2-20260720.md`'s "spiderweb, not one concordance" pivot (§13) and
its process-loop consolidation (§14). Asked to prepare a DB-schema-change plan capturing the design
elements from four same-day documents (the plan, `iba-process-loop-steps-to-flesh-out-v1-20260720.md`,
`iba-operation-ruleset-v1-20260720.md`, `iba-config-rules-for-process-loop-v1-20260720.md`).

## 2. The rework failure, and the correction

Produced `iba-db-schema-change-plan-v1-20260720.md` by synthesising across those four documents — but
the researcher had, in a separate channel/session, already resolved most of the config-rules doc's D1–D6
questions, and that resolution was never written to any file I could find (checked `iba/logs/`,
`Workflow/Sessionlogs/`, grepped the whole `iba/` tree). The document I produced treated already-settled
questions as open. Researcher's verdict: *"you cannot recover from the point that you lost… it seems to
unpick your brain, versus doing it myself is a much larger exercise… you steal my tokens because of all
the rework you force me to do."**

**Correction, saved to memory** (`feedback_iba_no_synthesis_small_units_only`): on IBA planning work, do
not independently synthesise/interpret across documents — work in small, explicitly-directed units, and
check whether something was already resolved elsewhere before treating it as open. The researcher then
began manually reconstructing the plan themselves rather than trust further synthesis.

## 3. V3 — the researcher's own reconstructed baseline

Researcher assembled `iba-application-plan-v3-reconstructed.md` by hand from prior documents — trimmed
to the essentials (context, the IBA App rules, the PS/Python/configurator framework, the high-level
schema as actually built, and empty "Detail App design" headers: Configurations / Utilities / User
Interaction / Validation and errors / Operation Modules) — explicitly to serve as **input and framework**
for the next planning phase, not to be second-guessed.

## 4. The Step 1/2/3 instruction

Researcher's instructions for the Application Design work:
1. **Step 1** — rewrite the Application Design document as one integrated blueprint, organising (not
   inventing) the thinking already collated across several separately-prepared design documents, extracted
   as five snippets to `scratchpad_tmp/`. Must be granular enough to tick off compliance paragraph by
   paragraph. Explicitly invited: system-design judgement on feasibility/gaps/dependencies, bounded by
   V3's rules and objectives. **Must be approved before proceeding.**
2. **Step 2** — list the gaps between the current build and the approved design.
3. **Step 3** — create the missing schemas and close the gaps.

## 5. Precedence + build-grounding pass

Filed `iba-app-design-precedence-and-structure-v1-20260721.md` first (per the researcher's "push findings
to a .md, do not reply in chat" instruction): established a chronology across the five snippets + V3 +
the actual build to resolve conflicts by precedence rather than by asking. Directly inspected the built
app rather than assuming:
- `iba/app/BUILD.md`, `iba/app/GOVERNANCE.md` — confirmed the DB is genuinely fresh-built from STEP
  (never migrated from the old DB), and that **GOVERNANCE.md itself already names the central
  unresolved seam**: the app runs on a lightweight, built `cfg_*` store while the elaborate designed
  `iba/config/*.json` configurator is not loadable and nothing reads it.
- Live `iba/app/db/iba.db` queried directly — 34 tables, exact `cfg_step`/`cfg_setting`/`cfg_on_fail`/
  `cfg_write_grant` contents, exact row counts (178 words, 534,075 spans, 18,571 passages at 1.56
  verses/passage average — the fragmentation the plan's movement-segment critique already named).

## 6. Application Design v1 — first draft

Filed `iba-application-design-v1-20260721.md`: 12 sections (Overview, Architecture, Configurator,
Utilities, DB/schema, User Interaction, Operation Modules, Validation, Outputs/Products, Governance,
Open Decisions, Compliance Checklist), every claim tagged **[BUILT]**/**[DESIGNED]**/**[OPEN]** against
the live app. §0 restated the plan's config principles as the governing standard everything else is
evaluated against.

## 7. Researcher's design-review comments — and the revision

Comments filed to `scratchpad_tmp/comments app design v1.txt`; the document was revised in place
(not re-versioned — still the same live review draft) against each:

| item | resolution |
|---|---|
| **The identity gap** (§5.4) | Resolved as a **prose architecture** — checked the old DB's actual `prose_section`/`prose_section_type` schema (via `iba/config/DBSchema/DBSchema.json`) and proposed a minimal `prose_type`/`prose` pair carrying only the *proven* core (status/version/supersedes-revision-chain/author), explicitly **omitting** `prose_section_dimension_link`/`prose_section_finding_link`/citations — all three built, 0 or near-0 rows, abandoned in the old DB, now the standing cautionary example against carrying over unconfirmed old-build constructs. Identity closes via a `char_key`-keyed many-to-one join (`verse_meaning`, and the same pattern extended to `verse_operation` per the researcher's own instruction), not a new surrogate entry table. |
| **Two-configurator convergence** (§3.3) | Resolved: the built lightweight `cfg_*` wins. The researcher is "highly suspicious" of `iba/config/*.json` — a partially-successful, noisy attempt to gather old-system rules, over-complex and hard to maintain. Its remaining use: one completeness-check pass against the real build, **then archive** ("stop the bleeding on this noise") — that audit has not been run yet; carried to Step 2. |
| **D2 (`body_type` mechanics)** | Elaborated as a concrete proposal at the researcher's explicit invitation: sibling columns on `operation`'s existing argument slots (`source_body_type`/`target_body_type`/etc.), not a static `span` property, since the same lemma's body_type is contextual to the argument role it fills. |
| **D4 (register vs cluster)** | Deferred by design, not stuck — wait until the concordance has real content before choosing its organising grouping. |
| **D5 (reconcile/consolidate/refine-rule)** | Process context added (populate from the old DB once baseline is built, then reconcile per book as the study proceeds) — the structural question (own work package vs steps) stays explicitly open, on purpose. |
| **operation_type #7/8/9** | Resolved — all three real and distinct: `has-status` = the verse declares the IB's state; `interacts-with` = cause-and-effect between characteristics; `co-exists-with` = same-context mention with no evidence of impact. |
| **"Interactive feedback"** | Resolved as a mapping onto the already-built `escalation` table + `run.state` pause/resume — not a new mechanism; the app does not use chat. |
| **Config 5-column shape** | Walked back from an invented column proposal to "deliberately unfixed — clarify empirically once real data/testing surfaces the need." |
| general | Added a guardrail note (not everything from the old build transitions; a proven-abandoned old table is evidence *against* copying, not a template) and a requirement that `BUILD.md` carry a maintained run-command list. |

§11 (Open Decisions) cut from 8 to 5 items; nothing resolved was left dangling outside it (researcher's
explicit instruction: an unresolved point not in the open list is a defect in the document).

## 8. Open items carried forward (§11 of the design document)

1. **`char_key` normalisation** — ★ the key question (researcher's own flag) — whether base-lemma+gloss
   is a sufficient join key for the `verse_meaning`/`verse_operation` dedup index, or a stronger identity
   mechanism is needed once real near-duplicates are seen.
2. **Old registry migration** — whether the old DB's 6 months of registry curation should still be
   imported, beyond the fresh-build-from-STEP path already taken.
3. **D5's mechanical question** — reconcile/consolidate/refine-rule as own work packages or steps inside
   `analyse-characteristic` — deliberately deferred.
4. **Config 5-column shape** — deliberately unfixed, pending real data/testing.
5. **D4's eventual grouping** — register/cluster/other, deferred until the concordance has content.

## 9. Next steps

Researcher will do research and prototyping to clear their thinking on the open items — **§11 item 1
(`char_key` normalisation) is the key one** — before the design document work resumes. Session cleared
after this log to avoid token drift; resume by reading this log + `iba-application-design-v1-20260721.md`
+ `iba-app-design-precedence-and-structure-v1-20260721.md`.

## 10. Key files

- Design document (live, revised): `iba/docs/iba-application-design-v1-20260721.md`
- Precedence/build-grounding: `iba/docs/iba-app-design-precedence-and-structure-v1-20260721.md`
- Researcher's baseline: `iba/docs/iba-application-plan-v3-reconstructed.md`
- Researcher's review comments: `scratchpad_tmp/comments app design v1.txt`
- Superseded rework (not to repeat): `iba/docs/iba-db-schema-change-plan-v1-20260720.md`
- Memory: `feedback_iba_no_synthesis_small_units_only`
