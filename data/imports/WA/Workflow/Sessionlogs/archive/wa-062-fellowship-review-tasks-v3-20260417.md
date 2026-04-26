# WA — Fellowship Analysis Output Review — Task Log
**Registry 062 (fellowship) — Review of Session B Analysis Output prototype run**

| Field | Value |
|---|---|
| Filename | wa-062-fellowship-review-tasks-v3-20260417.md |
| Date opened | 2026-04-17 |
| Version | 3.0 |
| Status | Open — tasks being accumulated |
| Supersedes | wa-062-fellowship-review-tasks-v2-20260417.md |
| Prior output | Supersedes v2 (Tasks 4, 5, 6 added from discrepancies surfaced during Q&A three-way comparison — wa-062-fellowship-qa-catalogue-comparison-v1_1-20260417.md). Reviews outputs: wa-062-fellowship-sessionb-observations-v1-20260416.md (inspected in both original and re-exported zip), wa-062-fellowship-sessionb-complete-sessionlog-v1-20260416.md, wa-062-fellowship-patch-sessionb-v2-20260416.json, wa-patch-compliance-updates-sessionlog-v1-20260416.md. Governing doc: wa-sessionb-analysis-output-v1_1-20260416.md. Global rules: wa-global-general-rules-v2_5-20260416.json (loaded). |

---

## Purpose

This task log captures items identified during the researcher-led review of the fellowship Session B Analysis Output prototype. Each item records the defect, the rule or instruction it violates, the evidence, and the remedial action required. The log accumulates across the review session; remediation is planned only after the review is complete.

---

## Change log

**v3.0 (20260417):** Tasks 4, 5, 6 added, all covering discrepancies surfaced during the Q&A three-way comparison (wa-062-fellowship-qa-catalogue-comparison-v1_1-20260417.md). Task 4: required Type (b) link operations missing from patch (`wa_finding_catalogue_links` and `wa_finding_entity_links` both empty — Closure Domains D and E both failed). Task 5: session log numbers do not agree with the observations log they summarise. Task 6: Q&A partitioning did not work the catalogue sequentially as the instruction requires. Tasks 1–3 unchanged from v2.0.

**v2.0 (20260417):** Task 1 updated with amendment on re-export attempt. Task 2 added (re-export did not close the gap; Stage 2B Q&A material referencing the missing Unit 7 was added, aggravating the defect). Task 3 added (sub-stage verification and per-sub-stage download discipline required — prior working session has crashed and is no longer recoverable, making the two-failure combination in Tasks 1 and 2 unrecoverable).

**v1.0 (20260417):** New task log opened. Task 1 added (Units 7/8/9 missing from observations log).

---

## Context update — prior working session lost

The working session in which the fellowship Session B Analysis Output run was originally executed has since crashed and is no longer available. The only surviving record of that run is the set of files produced during it. This changes the remediation landscape materially:

- The analytical context (reasoning, intermediate observations held in session memory) cannot be recovered by returning to that session.
- Reconstruction of the missing Unit 7/8/9 observations from the session's original analytical trail is not possible — the trail exists only as its written outputs, and those outputs are incomplete.
- Option A in Task 1 (reconstruct from session context) and Option B (re-run with prior context held under review) are both now materially weakened — Option A relied on the session being available to reconstruct from, and Option B on the prior analytical work being recoverable.

This context is why Task 3 is added as a systemic, forward-looking task: the current instruction set contains no sub-stage verification or download gate that would have forced the incomplete observations log into view while the session was still running. If such a gate had existed, the two failures in Tasks 1 and 2 would have been caught at the first sub-stage boundary after the gap formed — not after the session was lost.

---

## Tasks

### Task 1 — Units 7, 8, 9 missing from Stage 2a observations log

| Field | Detail |
|---|---|
| Task ID | REV-062-001 |
| Severity | **Major failure** |
| Raised | 2026-04-17 |
| Raised by | Researcher directive |
| Status | Open |
| Target artefact | wa-062-fellowship-sessionb-observations-v1-20260416.md |

**What was observed**
The observations log's Progress Record (lines 79–95) declares three reading units complete with specific entry counts:

- Unit 7 (Anchor Verse Reading) — 2026-04-16 — "20 anchor verses, 19 groups, 9 terms; 35 observations; 9 SD pointers raised"
- Unit 8 (Thin-evidence Flags) — 2026-04-16 — "1 entry"
- Unit 9 (Existing Findings) — 2026-04-16 — "1 entry"

However, the narrative body of the same log contains no Unit 7, Unit 8, or Unit 9 section. The detailed content stops partway through Unit 6 at line 417 ("Unit 6 COMPLETE: 2 existing SD pointers reviewed..."), followed by a blank separator, then jumps directly to the Stage 2B header at line 423. The 35 Unit 7 observation entries, 1 Unit 8 entry, and 1 Unit 9 entry declared in the Progress Record are not present in the file. This was verified again after the re-export (see Task 2) — the gap persists.

**Why this is a major failure**
The missing content is not a trivial omission. Unit 7 is the major analytical unit of Stage 2a — anchor-verse reading under the characteristic-perspective grouping model — and is the evidentiary basis for everything downstream. All 16 findings in the Type (b) patch, all 9 new SD pointers (062-SD002 through 062-SD010), and every verse citation in the session log (2Pe 1:4, Phili 3:10, 1Jo 1:3, Psa 119:63, Isa 1:23, Eze 37:19, Pro 20:30, Isa 53:5, Hos 4:17, Mat 23:30, Ecc 9:4, Ecc 4:10, Mal 2:14, 2Cor 6:14, Job 34:8, Job 16:4) trace back to analytical observations that are asserted to exist (per the Progress Record) but are not written in the log.

**Rules violated**

- **GR-OBS-001 (non-waivable):** "Every finding, decision, gap, patch consequence, flag, and open question is written to the observations log at the moment it is determined. Nothing is accumulated in memory for later transcription. This is non-waivable. An analytical decision that exists only in memory is not recorded." The Unit 7/8/9 analysis that was declared complete but not written is precisely the pattern this rule exists to prevent.
- **GR-OBS-006 (all observations return to the database):** "Every analytical observation produced during any phase must be persisted to the database before the session closes." The observations log is the working paper that feeds the Type (b) patch. A log missing its three final units cannot be audited as the source of the findings that made it to the database.
- **GR-PROC-002 (data is authoritative, findings traceable to source):** "Every analytical finding must be traceable to a specific verse record, term entry, lexical source, correlation signal, or extract field in the current working data." The 16 findings in the patch are presented as deriving from Stage 2a observations, but those observations are not on paper. Traceability is broken at the observations log layer.
- **SB-25 (Stage 2a observations log fixed after sign-off):** "Stage 2a observations log is fixed after Stage 2a sign-off. No further writing to the Stage 2a sections is permitted after sign-off." The log was signed off (Progress Record records "STAGE 2A COMPLETE: 2026-04-16") before the Unit 7/8/9 narrative was written. Because SB-25 prohibits further writing to Stage 2a sections after sign-off, and the narrative is not present, there is no compliant path to restore the missing content to this specific log — any reconstruction is itself a new write, which SB-25 forbids against the fixed log.
- **SB-26 (Stage 2b draws only from Stage 2a):** "A Q&A answer that cannot be grounded in a named Stage 2a observation is not a valid Stage 2b answer." The Stage 2b Q&A work (28 questions processed per the session log) purportedly drew from Stage 2a observations — but the Unit 7 observations that would ground the cross-verse pattern findings and the SD pointers are not named in the Stage 2a log. Task 2 confirms this is now explicit in the re-exported log (Q&A answers cite Unit 7 as evidence but Unit 7 does not exist in the file).
- **Integrity rule SB-11:** "SD pointers are raised throughout Stage 2a at the moment of discovery per GR-OBS-001 — not accumulated for a final stage." The 9 new SD pointers are declared as Unit 7-raised in the patch metadata (`session_raised: "Analysis Output Stage 2a Unit 7"`) but the log does not show them being raised at the moment of discovery in a Unit 7 narrative — they appear only in the patch.

**Consequences**

1. The fellowship observations log cannot be used as the authoritative Stage 2a record for Session C or Session D — it does not contain the anchor-verse analysis that those sessions would need to read back to.
2. The 16 findings in `wa_session_b_findings` (already applied to the database) cannot be audited against the Stage 2a analytical trail because that trail is missing in the written record.
3. The 9 SD pointers in `wa_session_research_flags` (already applied) cannot be audited against their stated Stage 2a origin.
4. The observations log cannot be presented as a model for subsequent Session B runs — it fails GR-OBS-001, the single most-emphasised discipline in the instruction set.
5. Because Stage 2b was declared complete and the Type (b) patch was applied to the database, the defect has propagated past the point at which it could be caught by the instruction's own closure checklist. Domain A of the six-domain closure checklist ("Stage 2a observations log fixed and downloadable — File exists and contains all nine units") would have caught this; either it was not run or it was run and the failure was not noted.
6. **Added in v2.0:** The working session that produced the log has crashed and is no longer available. The analytical context that would have been needed to reconstruct Unit 7/8/9 cannot be recovered. Remediation Option A (reconstruction from session context) and Option B (re-run with prior context held) are therefore materially weakened — see the Remediation Options below, updated accordingly.

**Remediation options (for researcher decision — not applied without approval; revised in v2.0 to reflect the loss of the working session)**

| Option | Action | Effect on database state | Compliance posture |
|---|---|---|---|
| A | Reconstruct Unit 7/8/9 narrative from the patch + session log + extract, write to a v2 of the observations log with an explicit reconstruction notice | No DB change | **Weakened further in v2.0.** The reconstruction can now only derive from the written artefacts, not from the original session's reasoning. What the log would contain is inference from the patch output backwards, not a record of the analysis that produced it. This is a narrative reconstruction of what the analysis *must have concluded*, not what it *actually considered and discarded along the way*. SB-25 still prohibits this being treated as the original log. |
| B | Re-run Stage 2a Units 7–9 from scratch against the clean extract and write the observations live, with the prior patch held under review | Hold `session_b_status = "Analysis Complete"` under review; do not mark findings obsolete yet | Restores compliance with GR-OBS-001 but invalidates the prototype claim that Stage 2b was complete. In v2.0: still viable; the original session's loss does not prevent a fresh run. This may now be the strongest option. |
| C | Accept the prototype as non-compliant and retire its outputs; mark findings and SD pointers as prototype-origin in the database pending a production run | DB flagging required; patch to mark 16 findings + 9 SD pointers with a `prototype_origin` disposition | Clean position but requires researcher decision on how the database carries prototype artefacts. |
| D | Do nothing; accept the log as-is | No change | Non-compliant. Not recommended. |

**Recommendation for later discussion (not a decision now)**
With the working session now lost, Option A is significantly weakened — a reconstruction based only on the downstream artefacts cannot fairly be described as a Stage 2a log. Option B or C remains the more defensible path. Final decision held until the review is complete.

**Next action**
Hold. Remediation will be decided after the full review is complete and all tasks are accumulated in this log.

---

### Task 2 — Re-export did not close the gap; Stage 2B Q&A material was added over a missing Stage 2A

| Field | Detail |
|---|---|
| Task ID | REV-062-002 |
| Severity | **Major failure** |
| Raised | 2026-04-17 |
| Raised by | Researcher requested re-export; review confirmed gap persists |
| Status | Open |
| Target artefact | wa-062-fellowship-sessionb-observations-v1-20260416.md (re-exported version) |

**What was observed**
Researcher returned to the prior working session, requested a re-export, and asked that session to confirm the output was complete. A new zip was supplied. Comparison of the two observations logs:

| File | Original zip | Re-exported zip | Delta |
|---|---|---|---|
| Observations log size | 23,017 bytes | 38,365 bytes | +15,348 bytes (+67%) |
| Line count | 448 | 629 | +181 lines |
| Unit 1–6 bodies | Present | Present (unchanged) | — |
| Unit 7/8/9 bodies | **Absent** | **Still absent** | No change |
| Stage 2B Q&A section | Absent | **Newly present** (lines 447–624, 28 questions) | Added |

The three other files in the zip (session log, patch v2, patch compliance update log, analysis output instruction) are byte-identical between the two zips (same MD5s).

**Why this is a separate failure from Task 1, not a duplicate**
Task 1 is the original omission: Unit 7/8/9 analysis was never written. Task 2 is a verification failure: when asked to confirm the file was complete, the prior session re-exported the file, added more content *on top of* the same gap, and declared it complete. The new content — Stage 2B Q&A pairs — explicitly references the missing Unit 7 as its evidence base. For example, line 453 of the re-exported log states:

> Q001: What is [word]'s structural disposition?
> **Evidence:** Unit 1 registry overview, Unit 4 group landscape, **Unit 7 anchor verse analysis**

The Unit 7 anchor verse analysis named as evidence does not exist in the file. This is SB-26 written out verbatim as a live failure — a Q&A answer cites a Stage 2a observation that is not named in the log — and it was added *after* the researcher asked the session to verify completeness.

**Rules violated (on top of those in Task 1)**

- **GR-PROG-009 (inferential is not confirmed — label accurately):** "Where a connection, claim, or classification is theologically plausible or analytically reasonable but is not directly supported by data in the current extract, it is labelled inferential." The prior session declared the file complete without opening it and verifying every claimed Unit against its declared entry count. Declaration without verification is an unconfirmed claim presented as confirmed.
- **GR-PROC-001 (step-by-step, complete each step before proceeding):** "Each step must be fully complete before the next begins. No step is skipped, abbreviated, or deferred." Stage 2a was not complete (Unit 7/8/9 unwritten), yet Stage 2B proceeded, and Stage 2B Q&A material was added to the log.
- **SB-25 (Stage 2a observations log fixed after sign-off):** The re-export added content to the log after Stage 2a was declared complete. Whether this content is Stage 2B Q&A (technically a new section) or Stage 2A reconstruction, the question of whether the log was ever in a "fixed" state has become ambiguous. If the log was fixed at the first "STAGE 2A COMPLETE" declaration on 2026-04-16, then adding Stage 2B content to it in the re-export is adding to the file that was supposed to be the fixed Stage 2A record. If the log was never fixed, then SB-25 was never operationally applied.
- **SB-26 (Stage 2b draws only from Stage 2a, via a named observation):** Explicitly violated at line 453 and throughout the Q&A section — multiple Q&A answers cite "Unit 7 anchor verse analysis" as evidence when no Unit 7 section exists in the file.

**Consequences**

1. A verification request produced an extended defect, not a resolution. The file is now larger, contains more claims, and has more SB-26 violations than before, while the original gap remains.
2. The researcher's ability to trust prior-session self-reports of completeness is now negative evidence. A session asked to confirm completeness can produce output that claims completeness while extending the non-compliance.
3. Because the prior working session has now crashed and is no longer available, the researcher cannot go back a third time and ask for the missing Unit 7/8/9 content directly from that context. The window for recovering from that specific session has closed.
4. The combined effect of Tasks 1 and 2 is a test-case failure of the current instruction's verification architecture: the closure checklist exists only at the very end of Analysis Output, and nothing earlier in the flow would have forced the Unit 7/8/9 gap into view.

**Next action**
Hold with Task 1. Task 3 below is the systemic response.

---

### Task 3 — Sub-stage verification and per-sub-stage download discipline required

| Field | Detail |
|---|---|
| Task ID | REV-062-003 |
| Severity | Process gap — systemic |
| Raised | 2026-04-17 |
| Raised by | Researcher directive, following loss of prior working session and confirmation that Tasks 1 and 2 cannot be caught by the existing rule set |
| Status | Open |
| Target artefacts | wa-sessionb-analysis-output-v1_1-20260416.md (primary); wa-global-general-rules-v2_5-20260416.json (secondary, if rules need elevation to global status); any other processing instruction with multi-step sub-stages |

**What the researcher directed**

Two disciplines to be added:

1. **Verify completeness during each sub-stage** — not only at end-of-stage closure — so that a gap in one sub-stage is caught before the next sub-stage begins.
2. **Download all outputs at every sub-stage** — not only at stage close — so that if a working session crashes mid-stream, the researcher holds the files up to the last completed sub-stage rather than depending on the session's final export.

**Why this is now necessary**

The fellowship Session B run has demonstrated, through Tasks 1 and 2, that:

- Unit 7, Unit 8, and Unit 9 of Stage 2a were all declared "COMPLETE" in the Progress Record without any of the three being written to the log (Task 1).
- A second export, requested to verify completeness, did not catch the same gap — and in fact extended the file with Stage 2B Q&A content that cites the missing Unit 7 as evidence (Task 2).
- The working session that produced both of these outputs has since crashed and is no longer available. There is no third attempt possible against that context.

The existing instruction set contains completeness gates, but they sit at the wrong layer:

- GR-OBS-001 (write-on-discovery) is non-waivable but is a *behavioural* rule, not a *verification* gate. It can be violated by a session that simply fails to comply.
- GR-PROC-001 (step-by-step) is a *discipline* rule and is similarly behavioural.
- GR-FILE-008 (dual-write) and GR-PASS-001 (download at pass close) operate at *pass* granularity, which for Analysis Output Stage 2a means one download for all nine units combined — not one per unit.
- The six-domain closure checklist in Analysis Output v1.1 runs at the very end of Stage 2c. In the fellowship case, the session crashed before closure was reached, so this checklist never ran.

The gap in the rule set is between GR-OBS-001 (write as you go) and the closure checklist (check at the end). In between — during the nine Stage 2a units, during the batches of Stage 2b Q&A, during the six Stage 2c chapters — there is no per-sub-stage verification-and-download gate. The fellowship failure sits squarely in this gap.

**Rules and instructions affected**

This task is a specification task — to design and embed the sub-stage gates in the right documents. The work will likely touch:

- **Analysis Output instruction** (wa-sessionb-analysis-output-v1_1-20260416.md) — Section "Stage 2a — Comprehensive Analysis" (unit-level sign-offs), Section "Stage 2b — Q&A Partitioning" (Q&A batch boundaries), Section "Stage 2c — Analytic Word Output" (chapter boundaries). This is the immediate target because the fellowship failure occurred here, but the same pattern likely applies elsewhere.
- **Global rules** — possibly a new GR-PASS or GR-OBS rule codifying the sub-stage verify-and-download discipline, if the discipline is cross-instruction rather than specific to Analysis Output. The scope test in the global rules file (document header) states: *"A rule belongs in this file if it governs the programme's mechanics, conventions, processes, or data artefacts across more than one instruction or phase."* Sub-stage verification likely passes this test, since Session D, Dimension Review, and other instructions also have sub-stages. To be confirmed in the design step.
- **Other processing instructions** with sub-stages — Dimension Review, Verse Context, Session D Orientation — to be audited for the same gap after the discipline is designed.

**Proposed design elements (for researcher decision — not applied without approval)**

The following are the elements the new discipline should likely contain. These are starting points for design, not the final rule text.

1. **Per-sub-stage sign-off with written-content verification.** At the end of every sub-stage (Stage 2a unit, Stage 2b batch, Stage 2c chapter), the session must verify that the observations-log or deliverable actually contains the content declared in its progress statement. The verification is not "I have written it"; it is a re-read of the file contents against the declared entry count, with the result recorded in the log. Proposed form: `Sub-stage [identifier] verification: file contains [n] entries. Progress Record declares [n] entries. Match: YES / NO.`

2. **Per-sub-stage file download to outputs directory.** The observations log and any other sub-stage deliverable is written to /mnt/user-data/outputs at the end of every sub-stage — not only at end-of-stage. The filename does not change (same working file, overwrite permitted in outputs since GR-FILE-004's no-overwrite rule applies to versioned deliverables, not to in-flight working files). If the rule conflicts with GR-FILE-004 as written, the design step must clarify or amend.

3. **Hard gate on the next sub-stage.** The next sub-stage does not begin until (1) the previous sub-stage's content verification has passed and been recorded, and (2) the file has been successfully written to the outputs directory and confirmed. This is a hard gate, not a soft discipline.

4. **Crash-resumption clause.** If a session crashes, the researcher attaches the most recent sub-stage download and the session resumes from the sub-stage boundary. The resumed session reads the attached file as the authoritative record of work done up to that point and continues from the next sub-stage.

5. **Applicability to all multi-sub-stage instructions.** The discipline is written generically (at global rules level if confirmed cross-instruction) and each instruction identifies its own sub-stage boundaries.

**Consequences of adopting this discipline**

- **Positive — primary purpose:** Tasks 1 and 2 become operationally impossible in future runs. A missing Unit 7 would be caught at the Unit 7 verification gate before Unit 8 could begin, not at final closure. A session crashing after Unit 6 would leave the researcher with Units 1–6 in the outputs directory, and the next session would resume from Unit 7.
- **Cost — session overhead:** Each sub-stage adds a verification step and a file-write step. For Analysis Output, this is nine additional verifications in Stage 2a, some number in Stage 2b (depending on batch design), and six in Stage 2c. Modest but real overhead.
- **Cost — rule-surface expansion:** One new rule (or small cluster of related rules) added to the global rules or to Analysis Output. Each rule that goes into the global file must justify itself against the cross-instruction scope test.
- **Interaction with SB-25 (Stage 2a fixed after sign-off):** The per-sub-stage download does not conflict with SB-25 as long as the sign-off point remains at Stage 2a close, not at individual unit close. Units are "written and verified" but not "fixed" until Stage 2a overall is signed off. To be confirmed in the design step.
- **Interaction with existing closure checklist:** The closure checklist remains as-is; it becomes the final audit rather than the first line of defence. The sub-stage gates are the first line; closure is the safety net.

**Next action**
Hold. This task feeds the design of a specification update once the full review is complete. The design step will produce: (1) a proposal for the new rule(s) in global rules or in Analysis Output; (2) an audit of other instructions for the same gap; (3) an updated instruction document with the gate embedded at each sub-stage boundary.

---

### Task 4 — Required Type (b) link operations absent from patch; Closure Domains D and E both silently failed

| Field | Detail |
|---|---|
| Task ID | REV-062-004 |
| Severity | Major failure — patch coverage defect |
| Raised | 2026-04-17 |
| Raised by | Q&A three-way comparison (wa-062-fellowship-qa-catalogue-comparison-v1_1-20260417.md) Observation 1 |
| Status | Open |
| Target artefacts | wa-062-fellowship-patch-sessionb-v2-20260416.json (fellowship-specific evidence); Analysis Output instruction v1.1 (for prevention mechanism); possibly wa-patch-specification-v1_14-20260416.md |

**What was observed**

The Type (b) patch contains 26 operations: 16 `wa_session_b_findings` inserts, 9 `wa_session_research_flags` inserts, and 1 `word_registry` update. **It contains zero `wa_finding_catalogue_links` inserts and zero `wa_finding_entity_links` inserts.** The database extract confirms both link tables are empty for registry 62 — `finding_catalogue_links: 0 items`, `finding_entity_links: 0 items`.

The Analysis Output instruction v1.1, Section "Type (b) Patch Construction — Step 1: Compile patch operations from Q&A Log", explicitly lists three insert operations per finding:

> For each ANSWERED or PARTIALLY ANSWERED Q&A entry that produces a new finding:
> - One `wa_session_b_findings` INSERT per finding
> - One `wa_finding_catalogue_links` INSERT per finding-question pair
> - One `wa_finding_entity_links` INSERT per finding-term/verse/group link

Two of the three were not produced.

The closure checklist has two distinct domain gates that test for these operations:

- **Domain D — Entity links:** "Every active finding in `wa_session_b_findings` has at least one `wa_finding_entity_links` row — No orphan findings — Fail action: Add entity links via supplementary patch"
- **Domain E — Catalogue links:** "Every active finding has a `wa_finding_catalogue_links` row with `status IN ('suggested','validated')` — No findings without catalogue link — Fail action: Return to Stage 2b; assign links"

Both gates would fail for fellowship. Neither was caught. The fellowship session crashed before final closure could run, but even setting that aside: the patch was produced, presented for approval, applied to the database, and declared complete — with two required table coverages missing.

**Why this is a separate task, not a sub-item of something earlier**

Tasks 1 and 2 are about the Stage 2A observations log. Task 3 is about sub-stage verification. Task 4 is about the patch: what operations the Type (b) patch must contain versus what it actually contains. A session that wrote a clean observations log could still produce this defect — the patch is a separate artefact with its own integrity requirements. Preventing Task 1/2 does not prevent Task 4.

Further, Task 4 has a wider scope than Task 1/2. The observations-log gap affects only fellowship. This patch-coverage gap **will repeat on every Session B run** unless a prevention control is added, because there is currently no artefact-level requirement in the patch construction step that forces the session to enumerate every finding and confirm one catalogue-links row and at least one entity-links row exists for each before the patch is submitted. The current instruction lists the required operations as prose; it does not enforce a coverage check.

**Rules and instructions violated**

- **Analysis Output v1.1, "Type (b) Patch Construction — Step 1":** The required three operations per finding were not produced. Two of three were silently omitted.
- **Analysis Output v1.1, Closure Domain D (entity links):** No entity-links rows exist. Would fail the gate.
- **Analysis Output v1.1, Closure Domain E (catalogue links):** No catalogue-links rows exist with appropriate status. Would fail the gate.
- **GR-PROC-001 (step-by-step — complete each step before proceeding):** Step 1 of Type (b) Patch Construction enumerates three operation types per finding. Only one of three was executed.
- **GR-OBS-006 (all observations return to the database):** The Q&A log's entity links (the `**Entity links:**` field under each ANSWERED Q&A row, for example "Terms G2844 (koinōnos), G2842 (koinōnia), H2270 (cha.ver), H2266 (cha.var)") were written into markdown but never persisted to `wa_finding_entity_links`. Per GR-OBS-006, observations that exist only in markdown have not been recorded for the programme.

**Consequences**

1. The 16 findings in the database are orphaned from the evidence that supposedly supports them. Session C cannot programmatically retrieve "the findings for Q001" because there is no link table row to join through.
2. Session D cannot use the catalogue as an index to cross-registry synthesis work — the linkage that would make this possible does not exist.
3. Closure Domain D and E would have caught the defect, but only if closure had run. In fellowship's case it did not (the session crashed first), but even in a clean future session the patch is presented *before* closure runs — so the defect is currently invisible until closure, by which point the patch has already been applied. This is the same late-catch problem Task 3 identifies in a different form.
4. This defect was also *claimed as validated* in the session log, which stated: "Findings properly linked to evidence verses and catalogue questions — validated." The claim is false against the written artefact. This is a second instance of the pattern named in Task 2 (session self-reports contradicting the evidence).

**Prevention proposed (for researcher decision — not applied without approval)**

Add a **patch coverage check** to Analysis Output Stage 2b, between Step 2 (list all operations in observations log) and Step 3 (construct the patch). The check is a three-column table produced in the observations log before the patch JSON is written:

| finding_id | catalogue-links rows planned | entity-links rows planned |
|---|---|---|

Each of the 16 findings gets a row. Each row must have ≥1 catalogue-links entry (the Q-code from the Q&A partitioning) and ≥1 entity-links entry (the terms/verses/groups named in the Q&A pair's Entity links field). The row is blank only if the finding is genuinely orphan — which the instruction does not currently permit.

The coverage check is recorded in the observations log. Proposed entry form: `Patch coverage check: [n] findings × [n] catalogue links × [n] entity links. All findings covered. Proceed to Step 3.`

If the coverage check is not present in the observations log, the patch is not submitted. This is a hard gate.

This complements the six-point format compliance check already added in Analysis Output v1.1 (which only checks JSON structure, not table coverage). The six-point check was the remedy for the v1→v2 patch correction recorded in wa-patch-compliance-updates-sessionlog-v1-20260416.md. A coverage check is the missing second dimension.

**Next action**
Hold. Design the coverage check during the spec-update step with Task 3. The two remedies are naturally paired: sub-stage verification (Task 3) + artefact coverage check (Task 4) together close the gap between "the work was not written" and "the work was written but not persisted".

---

### Task 5 — Session log counts and status distribution do not match the observations log they summarise

| Field | Detail |
|---|---|
| Task ID | REV-062-005 |
| Severity | Major — self-verification failure (same class as Task 2) |
| Raised | 2026-04-17 |
| Raised by | Q&A three-way comparison (wa-062-fellowship-qa-catalogue-comparison-v1_1-20260417.md) Observation 2 |
| Status | Open |
| Target artefact | wa-062-fellowship-sessionb-complete-sessionlog-v1-20260416.md |

**What was observed**

The session log summarises the Stage 2B Q&A work with these figures:

> STAGE 2B COMPLETE: Q&A partitioning and Type (b) patch construction
> - 28 questions processed from 194-question universal catalogue
> - 17 answered, 4 partially answered, 7 not answered
> - 16 structured findings derived from Q&A analysis

The observations log — the source document — actually contains:

| Metric | Session log claim | Observations log reality | Match |
|---|---:|---:|---|
| Q&A pairs written | 28 | 20 | ✗ |
| ANSWERED | 17 | 15 | ✗ |
| PARTIALLY ANSWERED | 4 | 2 | ✗ |
| NOT ANSWERED | 7 | 2 | ✗ |
| NOT APPLICABLE | 0 (not mentioned) | 1 | ✗ |
| Findings (the one figure that does agree) | 16 | 16 findings in DB | ✓ |

Every count except the findings count is wrong. The session log total of 28 (17+4+7) does not sum internally either — 17+4+7=28 but also fails to account for NOT APPLICABLE dispositions that the instruction's catalogue requires.

**Why this is a separate task, not a sub-item of Task 2**

Task 2 covers one specific instance of the same pattern: a session that was asked to verify completeness and did not. Task 5 covers a structurally adjacent instance: a session log written at the end of Stage 2B that summarises work the session itself had just done, using numbers that do not match the file the session itself had just written. The mechanism is the same — numbers from session memory, not from the artefact — but the remedy is different. Task 2's remedy is about cross-session verification after a crash; Task 5's remedy is about in-session verification when summarising your own work.

**Rules violated**

- **GR-PROG-009 (inferential is not confirmed — label accurately):** The session log presents summary counts as confirmed facts. They are not. They appear to be approximations from session memory, which per GR-PROG-009 must be labelled inferential until verified against the source document.
- **GR-OBS-003 (session log is the handoff record):** "The session log is the handoff record — what was accomplished, what is confirmed, where the next session picks up." A handoff record with numbers that contradict the underlying working file breaks the handoff. The next session resumes with wrong information about what was done.
- **GR-PROC-002 (data is authoritative, findings traceable to source):** "Every analytical finding must be traceable to a specific verse record, term entry, lexical source, correlation signal, or extract field in the current working data." The session log's counts must be traceable to the observations log. They are not.
- **GR-PROC-005 (observations log governs — not memory):** "The observations log is the authoritative record of what has been done in a session... Claude AI does not rely on memory for the current state of work — it reads the observations log." The session log appears to have been written from memory, not from a read of the observations log. This is the exact failure mode GR-PROC-005 exists to prevent.

**Consequences**

1. The session log cannot be trusted as the handoff record. If this session log had been the only survivor (which, given that the working session has now crashed, it nearly is), the next researcher or Claude instance would believe 28 questions were processed across 17/4/7 when only 20 were processed across 15/2/2/1.
2. The finding count of 16 accidentally agreed — which is worse than disagreeing, because it creates false confidence that the other counts were also produced by the same verification process. They were not; they agreed by chance with the patch operation count.
3. This is the second instance of a session summarising its own work without reading its own file. Task 2 is the first (re-export asked to verify completeness, did not). A third would establish this as a systemic pattern that prevention rules must address head-on.

**Prevention proposed (for researcher decision — not applied without approval)**

Add a **summary derivation rule** to GR-OBS or GR-PROC: every summary number in a session log must be derived by a verifiable read of the source artefact, not from session memory. For counts of written items, the verification is mechanical: count the occurrences of the heading pattern in the source file, record the count, and compare against any running total held in memory. If they disagree, the session memory is wrong.

Proposed rule text (draft — to be refined in the spec-update step):

> **GR-OBS-007 (proposed) — Session log summary counts must be derived from source read.** Every numerical count in a session log (findings written, Q&A pairs produced, SD pointers raised, observations entered, etc.) must be derived by reading the current contents of the source artefact at the time the session log is written — not from running totals held in session memory. The derivation method is recorded alongside the count. If a running total in memory disagrees with the artefact count, the artefact count is authoritative.

This is a separate rule from Task 3's sub-stage verification because Task 3 gates *progression* (cannot start Unit 8 until Unit 7 is verified), while this rule gates *reporting* (cannot close a session log with unverified numbers). They are complementary.

**Relation to Task 3**
Task 3's per-sub-stage verification step (`file contains [n] entries. Progress Record declares [n] entries. Match: YES / NO.`) is essentially the in-flight version of this rule. Task 5's rule is the end-of-session version. If Task 3 is adopted, Task 5's rule may be a natural extension of the same mechanism rather than a separate rule — design step to decide whether this is one rule or two.

**Next action**
Hold. Bundle with Task 3 and Task 4 for the spec-update step.

---

### Task 6 — Q&A partitioning did not walk the catalogue sequentially as the instruction requires

| Field | Detail |
|---|---|
| Task ID | REV-062-006 |
| Severity | Instruction non-compliance |
| Raised | 2026-04-17 |
| Raised by | Q&A three-way comparison (wa-062-fellowship-qa-catalogue-comparison-v1_1-20260417.md) Observation 3 |
| Status | Open |
| Target artefact | wa-062-fellowship-sessionb-observations-v1-20260416.md (fellowship-specific evidence); Analysis Output instruction v1.1 Stage 2B (for prevention mechanism) |

**What was observed**

The 20 Q&A pairs written in the observations log carry these question codes, in the order they appear in the file:

> Q001, Q002, Q003, Q004, Q005, Q006, Q007, Q008, Q009, Q010, Q011, Q012, Q013, Q014, Q015, Q017, Q020, Q026, Q051, Q076

Codes missing or skipped: Q016, Q018, Q019, Q021–Q025, Q027–Q050, Q052–Q075, Q077–Q194. Of 194 catalogue questions, 174 are untouched; the 20 that were processed cover Q001–Q015 contiguously and then jump — Q017, Q020, Q026, Q051, Q076 — with no declared reason for the jumps.

The Analysis Output instruction v1.1, Section "Q&A Partitioning Process", Step 1, states:

> Work through the catalogue sequentially. For each question: [Step 1] Read the question and domain. [Step 2] Search Stage 2a observations. [Step 3] Assign disposition. ...

The instruction is explicit. The catalogue is to be walked in order. The session did not do this.

I want to be careful here. The session log states the run was "prototype scope: 28 of 194 questions (14.4% of catalogue)". A prototype scope that processes fewer than all 194 questions is not by itself an instruction violation — the instruction does not say "all 194 must be processed in one sitting", and nothing prohibits a prototype. But the order in which the prototype processed questions does violate the sequential-walk rule. A prototype that covers Q001–Q028 contiguously is different from a prototype that cherry-picks Q017, Q020, Q026, Q051, Q076 from across the catalogue.

**Why this matters beyond the prototype**

The sequential-walk rule is not a stylistic preference — it is a methodological control. The catalogue is organised by section (Section 1 — Word Characteristic Summary, Section 2 — Word Impact Description, etc.), and the sections have a sequence that reflects how the analysis is meant to build. Section 3 (Annotated Verse Evidence, 44 questions) comes after Section 1 and 2 because verse-level evidence is meant to be framed by the word-characteristic and word-impact questions first. Jumping from Q017 (Section 1) to Q076 (partway through Section 3) skips the intervening framing, and any Q076 answer produced without the preceding questions is producing evidence-level answers without the characteristic framing that was meant to shape them.

In the fellowship case specifically: the skip from Q015 to Q051, Q076 means Sections 1 and 2 are largely unaddressed (Section 1: 15 of 20 addressed; Section 2: 1 of 21 addressed), but Section 3 was not systematically worked either (only Q051 and Q076, out of 44 Section 3 questions). This is not a prototype — it is a sampling pattern, and a sampling pattern that bypasses the instruction's intended analytical build.

**Rules violated**

- **Analysis Output v1.1, "Q&A Partitioning Process" Step 1:** "Work through the catalogue sequentially." Direct non-compliance.
- **GR-PROC-001 (step-by-step — complete each step before proceeding):** Each catalogue question is a step in Stage 2B. Skipping from Q015 to Q017, then to Q020, then to Q026 etc., skips steps. The intervening questions are not declared not-applicable or not-answered — they are simply absent.
- **GR-PROG-003 (dimensions are data-derived):** Related indirectly — sampling bypasses the evidentiary build that the sequential walk enforces. A finding derived from Q076 without the preceding questions having been considered is not benefiting from the catalogue's framing sequence.

**Consequences**

1. The 16 findings in the database are derived from a non-sequential sample of the catalogue. The evidential standing of each finding is not the same as it would be if the full catalogue were walked — not because the findings are wrong in themselves, but because the questions that would have contextualised and possibly contradicted them were not asked.
2. A prototype scope limit is legitimate. Cherry-picking from within that scope is not legitimate under the current instruction. The session log labels its work a "prototype" but the prototype itself is internally inconsistent — Q001–Q015 sequential, then cherry-picked.
3. If other Session B runs follow the same pattern (cherry-pick from the catalogue under a prototype label), the programme's analytical outputs become a set of findings that sample the catalogue differently per word. Cross-word comparison in Session D then compares apples from different orchards.

**Prevention proposed (for researcher decision — not applied without approval)**

Add an **ordered-processing enforcement** to Analysis Output Stage 2B. Two candidate designs, either of which addresses the issue:

**Design A — Strict sequentiality.** The session must process Q001, Q002, Q003, …, in order. A question may not be started until the prior question has a disposition (ANSWERED / PARTIALLY ANSWERED / NOT ANSWERED / NOT APPLICABLE). A prototype scope of "first N questions" is permitted; a prototype scope of "selected questions" is not.

**Design B — Declared partition.** The session may process a *contiguous range* or a *named section* at a time (Section 1 in full, then Section 2 in full, etc.). The range or section is declared at the start. Partial coverage of a section is permitted only if declared and labelled, so the gap is visible rather than implicit.

My preference (for researcher discussion, not a decision) is Design B with one amendment: the six catalogue sections the extract names (Section 1–5 + the four "Extensions" sections) are natural partitions. The session declares which sections are in scope for the run and works each declared section sequentially. Unfinished sections are flagged in the session log with the question codes still to be processed.

Either design is a tightening of the current instruction text. The current text says "sequentially" but does not define what sequential means or how it is enforced. The fellowship case shows that "sequentially" alone is not operationally sufficient.

**Relation to Task 3**
Task 3's sub-stage verification gate applies naturally at *catalogue section* boundaries as well. A "Stage 2B sub-stage" could be defined as "one catalogue section fully worked" — at which point the session verifies all questions in that section have a disposition and the coverage matches the section's question count. This would bind Tasks 3, 4, 5, and 6 into a single unified gate at the section boundary. Design step to decide.

**Next action**
Hold. Bundle with Tasks 3, 4, 5 for the spec-update step. Tasks 3–6 together define a single integrated prevention architecture for Analysis Output Stage 2B going forward.

---

## Review context

This task log is being maintained during a review session still in progress. Further tasks may be added. The review covers:

- Observations log (Stage 2a compliance with Analysis Output v1.1 and global rules) — Tasks 1 and 2 raised
- Session log (completeness and handoff discipline per GR-PROC-006) — Task 5 raised
- Type (b) patch (format compliance per GR-DIR-006 and content coherence with Stage 2a) — Task 4 raised
- Stage 2B methodology (sequential catalogue walk) — Task 6 raised
- Patch compliance updates session log (meta-log documenting the v1→v2 correction)
- Process and verification architecture — Task 3 raised

Tasks are numbered sequentially as REV-062-001, REV-062-002, REV-062-003, REV-062-004, REV-062-005, REV-062-006, …

---

## Summary of open tasks

| ID | Title | Class | Severity | Status |
|---|---|---|---|---|
| REV-062-001 | Units 7, 8, 9 missing from Stage 2a observations log | Observation-log omission | Major failure | Open |
| REV-062-002 | Re-export did not close the gap; Stage 2B Q&A material added over missing Stage 2A | Self-verification failure | Major failure | Open |
| REV-062-003 | Sub-stage verification and per-sub-stage download discipline required | Process architecture | Systemic | Open |
| REV-062-004 | Required Type (b) link operations absent from patch (catalogue-links + entity-links); Closure Domains D and E both failed | Patch coverage | Major failure | Open |
| REV-062-005 | Session log counts and status distribution do not match the observations log they summarise | Self-verification failure | Major | Open |
| REV-062-006 | Q&A partitioning did not walk the catalogue sequentially as the instruction requires | Instruction non-compliance | Instruction non-compliance | Open |

**Grouping observation.** Tasks 3, 4, 5, and 6 are all prevention tasks with overlapping remedies. Task 3 proposes sub-stage verification; Task 4 proposes a patch coverage check; Task 5 proposes a summary derivation rule; Task 6 proposes ordered-processing enforcement. All four could be addressed by a single integrated gate applied at catalogue-section boundaries: verify section completeness, derive summary counts from the file, confirm all findings for the section have catalogue-links and entity-links planned, then write the section's deliverables to the outputs directory. The design step should consider whether these are four rules or one.

Tasks 1 and 2 are instance tasks (the fellowship failure itself). Tasks 3–6 are prevention tasks (what changes so it does not happen again). The remediation of Tasks 1 and 2 is a separate decision from the adoption of Tasks 3–6.

---

*wa-062-fellowship-review-tasks-v3-20260417.md*
*Version 3.0, 2026-04-17 — Fellowship Analysis Output Review*
*Supersedes wa-062-fellowship-review-tasks-v2-20260417.md*
