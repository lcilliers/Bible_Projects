# Flag Management — current status (escalation #833)

**Stage: explore.** Per the researcher's confirmed cycle (#833 v2): explore → propose/design →
approve → build → test → approve. This document is the explore stage only — no design decisions,
no proposal, nothing built. Scope, per instruction: every flag-related table **and** the ad-hoc
flag-shaped columns found while sweeping both databases, not narrowed to prose or to dedicated
tables alone.

---

## 1. Full inventory — both databases swept directly, not assumed from prior documents

### 1.1 Dedicated flag-tables (all in `bible_research.db`; `iba.db` has none)

| Table | Rows | `cfg_table` state | What it is |
|---|---:|---|---|
| `wa_quality_flag_types` | 29 codes, 7 groups | active | Data-quality/research flag vocabulary. Only 7/29 codes ever raised, all fully automated (§2). |
| `wa_data_quality_flags` | 19,866 | **inactive=1** — `cfg_table.use`: *"no resolution or soft-delete column, so it is an append-only log with no lifecycle"* | Instances of the above, term/file-scoped. |
| `wa_session_research_flags` | 715 | active | Researcher-facing queue with a real `resolved`/`resolved_date` lifecycle (200 closed/515 open) — real vocabulary drift though (§2). |
| `phase2_flag_types` | 25 codes | active | **Different purpose** — content classification about a term (e.g. `GOD_AS_SUBJECT`), not a "needs attention" signal. Named for completeness. |
| `mti_term_flags` | 1,005 | inactive=1 | Junction, `phase2_flag_types` → `mti_terms`. 994/1,005 rows use just 2 of 25 codes. |
| `wa_term_phase2_flags` | 1,570 | inactive=1 | Same vocabulary, different junction. 1,092 rows are one bulk patch. |
| `wa_flag_type_question_link` | 12 | active | Maps 4 flag types to catalogue questions. Static since April 2026. |

*(Full schema/content detail for the top 3: `iba/docs/prose-management-iba-first-layer-proposal-v4-20260823.md` §1.4 — not reproduced here, referenced.)*

### 1.2 Ad-hoc flag-shaped **columns** — found by sweeping every column name across both DBs, not limited to dedicated tables

This is new since the §1.4 audit, which only looked at dedicated flag tables. A full column sweep
(`%flag%` against every table in both databases) surfaces a second, entirely separate population —
inline signal columns bolted directly onto core analytical tables, each invented independently:

| Table.column | Database | Rows flagged / total | `cfg_column.use` (verbatim) |
|---|---|---:|---|
| `finding.flagged_for_review` | bible_research | 471 / 438,099 | "Researcher marker that the finding needs a second look; set on only a handful of rows, the rest defaulting to 0." |
| `verse_context.flagged_for_review` | bible_research | 2,319 / 55,775 | "1 = needs review; in the sample it tracks `triage_status='ESCALATE'` one-for-one, so it appears to be a **derived duplicate** of that signal rather than an independent flag." |
| `verse_context.residue_flag` | bible_research | 0 / 55,775 | "0 in all 55,775 rows; declared but never set, so it carries no information." |
| `passage.review_flag` | bible_research | 16 / 4,296 (all `'0'`) | "Present on only the 16 single-verse emergent passages, all holding the string `'0'`. The declared type is TEXT but the content is a numeric flag, and with a single value it currently marks nothing." |
| `passage.review_flag` | — | n/a | **Does not exist** on `iba.db`'s own `passage` table — the two `passage` tables (bible_research + iba, escalation #737's on-hold migration) have diverged schemas, not just diverged data. |
| `cluster_strong.review_flag` | iba | 574 / 7,609 | "1 if this specific assignment needs researcher review before being trusted as final." — real, working, IBA-governed. |
| `session_d_observations.researcher_flag` | bible_research | 0 / 0 | Table itself is **empty** — part of the abandoned Session D workstream (matches §1.2's `wa_session_research_flags` finding that 447/715 rows there route to the same abandoned workstream). |

(`delete_flagged`/`delete_flag` columns — ~30 more hits in the sweep — are the standard soft-delete
convention, a different concept entirely; excluded from this inventory as out of scope.)

### 1.3 A third, related concept: `verse_context.triage_status`

Not a column named "flag," but `cfg_column`'s own note above ties it directly to
`flagged_for_review`: `triage_status='ESCALATE'` and `flagged_for_review=1` move together
one-for-one in the sampled data — meaning `verse_context` independently carries **two** columns for
what looks like the same signal, invented at different times. Worth carrying into the design stage
as a concrete case of exactly the drift the researcher named.

---

## 2. Flag usage by table — what each one is for, and why the shape changed over time

Added per instruction (researcher, 2026-08-23): *"Flagging has been a notoriously troublesome area
in the study over a long time. That is likely why flagging of clusters, findings and verse_context
migrated to flagging onto the record. There is also different types of uses of the flagging
method, which will explain the different tables better."* Checked directly against git history
(commit dates, not assumed) — **the hypothesis holds**. There are four distinct generations, each
one built because the previous generation's shape wasn't working:

### 2.1 The four generations, in order

| Gen | When | Commit | What changed | Why (from the commit record) |
|---|---|---|---|---|
| **1** | 2026-03-19 | `a3744cfb` "schema v3.1.0, engine build" | `wa_quality_flag_types` + `wa_data_quality_flags` built — a **dedicated flag-table pair**: a vocabulary table + an instance table, keyed to a term/file. | The original design: flags as a separate, generic evidence-log alongside the term data, not part of it. |
| **2** | 2026-03-25 to 27 | `85d9b041` "**flag system redesign**, Session B pipeline, 33 words complete" | `wa_session_research_flags` built — commit body explicitly says *"flag cleanup"* alongside it. A second, broader **dedicated flag-table**, still separate from the record, now researcher-facing with routing (`session_target`) and real usage from day one (73 flags raised in this same session). | Generation 1's automated, term/file-scoped flags weren't enough for the researcher-facing "pointer to come back to" need Session B's pipeline required — a second table, not a fix to the first. |
| **3** | 2026-06-08/09 | `43322374`/`bc83ddf3`, schema M55/M56, the `finding`/L2 verse-read rebuild | `residue_flag`, `triage_status`, `flagged_for_review` added **directly onto `verse_context`**; `flagged_for_review` added **directly onto `finding`** (a brand-new table at this same migration). Flags move **onto the record itself** for the first time. | By the L1/L2 finding-model rebuild, indirection through a separate flag-table had itself become part of the problem (per §2.2 below) — the fix was to stop pointing at a row and just mark the row. |
| **4** | 2026-08-12 | IBA migration scripts (`bootstrap_cluster_strong_evidence_columns_20260812.py` etc.) | `cluster_strong.review_flag` — same on-the-record shape as Gen 3, now finally **IBA-governed** (`cfg_column` documented, consistently INTEGER-typed, actively used). | Continues Gen 3's shape under real process control for the first time — the one flag in this whole inventory built after IBA existed to harness it. |

### 2.2 Per-table usage type — what kind of flag each one actually is

Four genuinely different *uses* hide under the single word "flag," matching the researcher's point
that this is what actually explains the proliferation of tables — a new use-case got a new table
(or column) rather than an existing mechanism being reused or fixed:

| Use type | Tables/columns | Who/what sets it | What resolves it |
|---|---|---|---|
| **A — Automated data-coverage signal.** Computed entirely by the engine from extraction stats; no human judgement in the raising. | `wa_quality_flag_types`/`wa_data_quality_flags` (the 7 populated `DATA_COVERAGE` codes) | The extraction engine, at ingest time | Never, structurally — it's a permanent observation about the data ("this term has few verses"), not a pending task. Nothing in the schema marks these resolved, and nothing needs to. |
| **B — Researcher-facing pointer/observation queue.** A note to come back to, with routing to *where* it should be picked up. | `wa_session_research_flags` | Claude, during Session B/D analysis (`session_raised`) | The researcher or a later session, via `resolved`/`resolved_date`/`resolved_note` — genuinely closable, 200/715 actually closed. |
| **C — Inline "needs a second look" marker on the record itself.** A single bit, no vocabulary, no reason-text field, no routing — the record just carries its own "look at me again" state. | `finding.flagged_for_review`, `verse_context.flagged_for_review`, `cluster_strong.review_flag`, `passage.review_flag` (intended, barely realised) | Whatever process last touched the record and had a reason to doubt it | Nothing structural — clearing the bit is presumably manual and undocumented; no code path found that flips any of these back to 0 after review. |
| **D — Content-classification tag.** Not a "needs attention" signal at all — a descriptive label about the term's own linguistic content. | `phase2_flag_types` (+ its 2 junctions) | Analyst judgement during Phase 2 triage | N/A — not meant to resolve; it's a permanent classification, same shape as use type A but human- rather than engine-applied. |
| **Dead — declared, never functioned.** | `verse_context.residue_flag`, `session_d_observations`, 22/29 `wa_quality_flag_types` codes | Nobody, ever | N/A |

Type C is the important one for the researcher's hypothesis: it is **exclusively** Gen 3/4 (the
"migrated onto the record" generations) — types A, B, and D all predate it and all live in a
separate table. The shift wasn't cosmetic — it's a real change in kind, from "a flag points at a
record" to "a record carries its own flag," and it happened specifically because types A and B
(separate-table) had their own structural problems by the time Gen 3 was built (§2.1).

### 2.3 What actually broke in the separate-table generations (why Gen 3 moved on-record)

Not asserted, checked against the data already gathered:

- **Indirection cost.** A record's "needs review" state, held in a different table, requires a join
  to see at query time and a delete-or-update-elsewhere to clear — `wa_data_quality_flags` has no
  resolution mechanism at all (§1.1), and nothing in the codebase was ever built to retract a flag
  once raised. On-record flags (Gen 3/4) are at least visible on the row they describe, even though
  they inherited the same missing-resolution-path problem in a new form (§2.2 type C).
- **Vocabulary sprawl outpaced use.** Gen 1 declared 29 codes across 7 conceptual groups; only 7
  were ever populated (§1.2 in the current-status detail). Gen 2 declared a real `flag_code`
  vocabulary too (21 distinct codes used) but let `priority`/`session_target` drift into inconsistent
  spellings with no CHECK constraint. Both generations over-designed the vocabulary relative to what
  was ever actually exercised.
- **Workstream dependency.** 447/715 Gen-2 rows and the entire Gen-3 `session_d_observations` table
  point at Session D, a workstream that was itself abandoned — flags don't fail in isolation; they
  fail when the process they were meant to route into stops existing.

---

## 3. What the data says, plainly

**Almost none of this is currently working as a "signal, not yet resolved" mechanism should.**
Sorted by what's actually true of each:

- **Fully dead** (declared, never populated): `wa_quality_flag_types`' 22 non-`DATA_COVERAGE` codes
  (`DATA_QUALITY`/`RESEARCHER_DECISION`/`SESSION_B`/`SESSION_D`/`SESSION_D_POINTER`/
  `STUDY_REQUIRED` — the groups closest in *name* to what a flag should be), `verse_context.
  residue_flag`, `session_d_observations` (the whole table).
- **Automated only, no human judgement ever recorded**: the 7 `wa_quality_flag_types` codes that
  *are* populated (19,866 rows) are 100% engine-computed from STEP extraction stats — the
  mechanism has never once carried a human-raised signal, despite that being the more interesting
  half of its own design.
- **Real, working, but with real defects**: `wa_session_research_flags` (genuine `resolved`
  lifecycle, but `priority`/`session_target` vocabulary drift, `cluster_link` as an unsplittable
  string, 447/715 rows pointed at an abandoned workstream); `finding.flagged_for_review` and
  `cluster_strong.review_flag` (both real, both actively set, both isolated single-column booleans
  with no vocabulary, no reason-text, no lifecycle beyond the bit itself).
- **Barely used, type-inconsistent**: `passage.review_flag` (16 rows, TEXT-typed, holds only the
  string `'0'` — currently incapable of marking anything as flagged).
- **Silently duplicated**: `verse_context.flagged_for_review` vs. `triage_status='ESCALATE'`.
- **Schema-diverged across the two-database split**: `passage.review_flag` exists on one copy of
  `passage`, not the other.

**The one clean precedent**: `cluster_strong.review_flag` — IBA-governed, `cfg_column`-documented,
INTEGER-typed, actively and consistently used (574/7,609). Everything else predates IBA and shows
exactly the pattern the researcher named: real intent, no harness, drift.

---

## 4. A related historical precedent (context, not a design input)

`Workflow/Programme/Program_reports/archive/wa-global-dimreview-flag-normalisation-20260419.md`
(2026-04-19, archived) — a one-off bulk correction of `word_registry.dim_review_status` lagging
real review state (8 of 34 eligible registries corrected). Different mechanism
(`dim_review_status` is a status enum on `word_registry`, not one of the tables/columns above), but
the same underlying pattern: a status/flag field drifting out of sync with the data it's meant to
describe, caught only by a manual sweep. Not itself part of this scope — surfaced because it's the
same failure mode recurring, three months before IBA existed to catch it structurally.

---

## 5. Open questions for the design stage — named, not answered here

1. **Weight class.** The project already has one governed "something needs attention, not yet
   resolved" mechanism: **escalation** itself (`governance.escalation.scope` — *"all open items,
   discovery of anomalies, clarifications... must be recorded in escalation"*). A flag, per the
   researcher's own definition (*"a signal ... created in the process of doing something else, that
   could have an impact, but is not resolved at the moment"*), sounds lighter and higher-volume —
   e.g. 471/2,319/574 individual row-level marks vs. 833 total escalations ever raised. Does
   normalisation mean: (a) one unified mechanism (escalation subsumes flags), (b) two deliberately
   separate weight-classes (a lightweight per-row flag that can *escalate into* a full escalation
   when it needs a decision — mirroring the `resolution_kind`/`escalate_to_decision()` shape #798/
   #799 already built for a different axis), or (c) something else?
2. **Where do the dead 22 `wa_quality_flag_types` codes go** — retire outright, or are some of them
   (`RESEARCHER_DECISION`, `STUDY_REQUIRED`) actually still-needed concepts that just never got a
   working mechanism to populate them?
3. **`verse_context.flagged_for_review` vs. `triage_status`** — which is authoritative, if they're
   really duplicates?
4. **Scope of "normalise"** — does every table/column above get migrated onto one new mechanism, or
   does this stage only *design* the mechanism and register what already exists, leaving migration
   of each source as its own later step (matching how #829 handled `prose_section`'s own defects —
   registered, not all fixed in the same pass)?
5. **The two-database split** (`passage.review_flag`'s divergence is a live example) — does
   normalisation land in `iba.db` only (matching `governance.scope_iba_db`), with `bible_research.db`
   sources migrated in, or does it need to work across both during the transition?
6. **Which generation's shape is actually right, now that all four are visible (§2.1).** Gen 3/4's
   on-record shape (type C, §2.2) is the most recent and the only one continued under IBA — but it's
   also the thinnest (a bare bit, no vocabulary, no reason-text, no resolution path — it inherited
   Gen 1/2's missing-resolution problem in a new form, §2.3). Does normalising mean generalising
   type C (on-record, but properly governed this time), reviving type B's richer shape
   (`wa_session_research_flags`' vocabulary + lifecycle, fixed rather than replaced) as a
   *separate* table records point into, or a genuine third shape neither generation tried?

None of these are answered here — explore stage only, per the confirmed cycle.
