# wa-global-ref-consistency-obslog-v1-20260418

> Programme-wide reference consistency check — observations log
> Version: v1 | Date: 20260418 | Scope: programme-level inconsistency check and cross-reference update
> Prior output reference: none (new session task)

---

## Governing rules in force

- **GR-OBS-001** — continuous write; log authoritative; substantive chat output also appears here
- **GR-OBS-003** — session log produced separately at session close
- **GR-OBS-004** — this obs log version-increments at named boundaries (new session / named batch), not every file save
- **GR-REF-001** — single-authority content referencing: pointer not copy, versioned references, single authoritative document per content type, consistency check at version bumps, documents stay within named scope
- **GR-REF-002** — `[current]` token for operational cross-references; specific versions reserved for provenance (Supersedes, observation log, `_patch_meta.produced_by`)
- **GR-CAD-001** — self-check before every substantive response; `present_files` after every substantive write
- **GR-HF-001** — restrained help-forward: complete the instruction and stop
- **FLAG-010** — post-GR-v2_8 instruction audit is an Open blocking gate on new word analysis. This task is not new word analysis; not blocked.
- **FLAG-012** (Open, sequenced after FLAG-013) — cross-instruction reference cleanup sweep under GR-REF-002
- **FLAG-013** (Open, sequenced first) — document_discipline category classification review

## Relationship to FLAG-012 / FLAG-013

The researcher task described here — *"check for programme-wide inconsistencies and update cross-references"* — overlaps with but is narrower than FLAG-012. Reading the instruction literally, the immediate task is to (a) check whether WA-Reference's list of instruction documents correlates with Project Files, and (b) surface inconsistencies for the researcher. It is not yet the full corpus sweep described by FLAG-012, which remains gated behind FLAG-013. Findings below are recorded as candidates for the FLAG-012 sweep when it runs.

---

## O-001 — Session start

- **Time:** 2026-04-18, session start
- **Instruction:** "Check for programme wide inconsistencies, and update cross references throughout. Note the cross reference rule in global rules. Startup the obslog and check in references if the project file instructions correlate with the list in the references."
- **Scope taken:** (a) open this obs log, (b) correlate WA-Reference §1.4 (Instruction Documents list) against Project Files, (c) flag inconsistencies. Full FLAG-012 corpus sweep NOT taken — that remains gated by FLAG-013.
- **Files read for this check:** `wa-reference-v5_6-20260418.md` (§1.3, §1.4, §12 Patch Index), directory listing of `/mnt/project/`, header of `wa-patch-instruction-v2_0-20260418.md`.

---

## O-002 — §1.4 Instruction Documents correlation with Project Files

### Method

Enumerated the eleven patterns in WA-Reference §1.4 (lines 91–103) and compared each to the `wa-*.md` files in `/mnt/project/`.

### Result

**Ten of eleven §1.4 patterns have a matching file in Project Files:**

| §1.4 pattern stem | Project Files match | Status |
|---|---|---|
| `wa-reference` | `wa-reference-v5_6-20260418.md` | match |
| `wa-patch-instruction` | `wa-patch-instruction-v2_0-20260418.md` | match |
| `wa-directive-instruction` | `wa-directive-instruction-v1_0-20260418.md` | match |
| `wa-claudecode-instruction` | `wa-claudecode-instruction-v4_0-20260418.md` | match |
| `wa-versecontext-instruction` | `wa-versecontext-instruction-v2_7-20260414.md` | match |
| `wa-dimensionreview-instruction` | `wa-dimensionreview-instruction-v3_2-20260417.md` | match |
| `wa-sessionb-analysis-readiness` | `wa-sessionb-analysis-readiness-v1_5-20260416.md` | match |
| `wa-sessionb-analysis-output` | `wa-sessionb-analysis-output-v1-20260416.md` | match |
| `wa-sessionc-instruction` | `wa-sessionc-instruction-v1_4-20260414.md` | match (under construction — FLAG-001) |
| `wa-sessiond-orientation` | `wa-sessiond-orientation-v3_1-20260414.md` | match |
| **`wa-registry-management-guide`** | **ABSENT** | **inconsistency** |

### Finding F-001 — `wa-registry-management-guide` is listed in §1.4 but not present in Project Files

- **Observation:** §1.4 row 11 (line 103) lists the registry management guide as a standard instruction document. No file matching this pattern exists in `/mnt/project/`.
- **Interpretation:** Two possibilities — (i) the document exists outside Project Files (in the wider workspace) and has simply not been attached to this session; (ii) the document has been retired or renamed and §1.4 is stale. This cannot be determined from what is in the session.
- **Further evidence:** §12 Patch Index cites `wa-registry-management-guide v5_9` as governing document for the CLUSTERING patch type. If the file exists at v5_9 elsewhere, that citation is live; if it has been retired, §12 carries a second stale reference.
- **Decision:** record as researcher question — see chat alert.

### Finding F-002 — files present in Project Files that are not in §1.4

Two `wa-*.md` files sit in Project Files that §1.4 does not list:

| File in Project Files | Status against §1.4 |
|---|---|
| `wa-global-flags-v1_3-20260418.md` | Correctly covered by §1.3 "Programme-Level Files" (pattern `wa-global-flags-v{n}-{YYYYMMDD}.md`). **No inconsistency.** |
| `wa-patch-specification-v1_14-20260416.md` | **Not listed in either §1.3 or §1.4.** |

- **On `wa-patch-specification-v1_14`:** Per the header of `wa-patch-instruction-v2_0-20260418.md` (line 5 and line 935 footer), the patch specification is *formally superseded* by the patch instruction: `"Supersedes: wa-patch-specification-v1_14-20260416.md + patch-related sections of wa-sessionb-cc-instructions-v3_6-20260416.md (§4, §15, §16)"`. The specification is no longer an active instruction document.
- **Consequence:** WA-Reference §1.4 correctly omits it. Its continued presence in Project Files is a file-management question (legacy / archive / retained for transition), not a reference inconsistency. No update to §1.4 required for this file.
- **Finding classification:** no action on the reference; flag only for researcher visibility that the file is still sitting in Project Files.

---

## O-003 — §12 Patch Index versioned cross-references — audit

### Method

§12 (Patch Index) contains a table with inline versioned references to seven instruction documents. Each was compared against the file present in Project Files.

### Result

| §12 cites | Project Files actual | Status |
|---|---|---|
| `wa-sessionb-analysis-readiness (when finalised)` | v1_5 present | no version cited — informational, matches |
| `wa-sessionb-analysis-output (when finalised)` | v1 present | no version cited — informational, matches |
| `wa-versecontext-instruction v2_7` | v2_7 | match |
| `wa-sessiond-orientation v3_0` | **v3_1** | **STALE** |
| `wa-registry-management-guide v5_9` | **ABSENT from PF** | **cannot verify; see F-001** |
| `wa-patch-instruction v2_0` | v2_0 | match |

### Finding F-003 — §12 references `wa-sessiond-orientation v3_0`; Project Files has v3_1

- **Observation:** Line in §12 patch-type table cites `v3_0`. Project Files contains `wa-sessiond-orientation-v3_1-20260414.md`.
- **Classification:** operational cross-reference (running-text lookup pointing the reader to a governing instruction). Per **GR-REF-002**, operational references should use `[current]` rather than a specific version.
- **Consequence:** this is exactly the pattern FLAG-012 exists to sweep. It is not acceptable to silently update `v3_0 → v3_1` because GR-REF-002 directs operational references to `[current]` instead of any specific version. Updating to `v3_1` would create exactly the same staleness bow-wave at the next v3_2 bump.
- **Proposed correction (for researcher decision):** replace `v3_0` with `[current]` in §12. Preserve any provenance/Supersedes references to `v3_0` unchanged.

### Finding F-004 — §12 references `wa-registry-management-guide v5_9`; document absence (see F-001)

- **Observation:** §12 cites `v5_9`. No file with that stem exists in Project Files.
- **Classification:** same operational-reference category as F-003. Cannot be resolved until F-001 is answered (does the document exist outside PF, or has it been retired?).
- **Contingent correction:**
  - If document exists: change citation to `[current]` per GR-REF-002.
  - If document retired: remove the row or mark the CLUSTERING patch type governing instruction as `— (retired; see [new location])`.

---

## O-004 — Summary of findings for chat alert

Four findings total. One pure-absence inconsistency (F-001), one informational non-inconsistency (F-002), two stale/un-verifiable §12 references (F-003, F-004).

All three substantive findings (F-001, F-003, F-004) require a **researcher decision** before §1.4 or §12 can be updated. GR-REF-002 sweep guidance says the sweep should run *after* FLAG-013 is resolved — so even the mechanical fix for F-003 may not be the right thing to do today. The researcher should decide whether to:

- (a) apply the `[current]` treatment to §12 now as a targeted fix (i.e. run this narrow slice of FLAG-012 ahead of FLAG-013 resolution); or
- (b) hold all §12 edits until FLAG-013 completes and FLAG-012 runs as the full corpus sweep.

No patch or directive has been drafted. No WA-Reference edit has been produced. Awaiting researcher decision.

---

## O-005 — Researcher response and authorisation

- **Time:** 2026-04-18, turn 2
- **Researcher confirmed:**
  - Task was handled as intended; no drift.
  - F-001: registry management guide is *now in project files* (see contradictory finding in O-006 below).
  - F-002: later patch file version exists (i.e. patch-specification is legitimately stale; retained understanding is correct).
  - Raised a question: does Claude AI automatically read the latest version, or must stale documents be removed to avoid confusion?
  - Flag file rename to be reflected in WA-Reference.
  - Cross-references in files to be dealt with as part of this task (not deferred).
- **Researcher authorisation granted:** Update WA-Reference to refer to all current programme files. Adopt GR-REF-002 `[current]` for operational cross-references. Work through all programme files and reset cross-references to new naming conventions and `[current]` without returning for confirmation on each fix. Surface at the end only items that cannot be resolved.
- **Answer recorded:** Claude AI does not automatically prefer the newer version when two versions are present in Project Files. Both are equally visible; which one is used depends on which is opened or cited in memory. The safer practice is removal of superseded files from the active workspace. GR-REF-002's `[current]` token mitigates — but does not fully solve — the risk, because it resolves at read time only when referring documents actually use the token. Documents still citing a specific version of a superseded target remain stale until they are updated.
- **Scope taken for this batch:** Full programme-wide reference sweep — this is effectively the work described by FLAG-012, running ahead of FLAG-013 on researcher direction. FLAG-013 (document_discipline category classification review) is not resolved by this batch; its status is a direction/principle call and will be surfaced at session close.

---

## O-006 — Registry Management Guide still not visible in /mnt/project/

- **Observation:** Researcher stated the missing document "is now in project files." Directory scan of `/mnt/project/` at turn 2 shows the same twelve files as at turn 1; `find /mnt -name "*registry-management*"` returns zero matches; `/mnt/user-data/uploads/` is empty.
- **Possible causes:** upload did not complete, upload was to a different project than this chat, or delivery to the file-system backing this session has not refreshed.
- **Decision:** proceed with the ten active instruction documents I *can* see. Record `wa-registry-management-guide` as an **unresolved item** for the researcher at session close. Where other documents reference it, apply `[current]` per GR-REF-002 — the token will resolve correctly whenever the file becomes visible, so the references themselves can be updated cleanly even without the target document in view.
- **Impact on batch:** minimal. The sweep in other documents can proceed; one output (`wa-registry-management-guide` itself updated to reference current peers) will not be produced this session.

---

## O-007 — Full cross-reference scan completed

A systematic scan of every `wa-*.md` file in `/mnt/project/` for versioned cross-references was performed. Findings by document are summarised in the table below (full per-line classification retained in working scripts).

**Files needing a minor version bump:**

| File | Current | Next | Notes |
|---|---|---|---|
| wa-reference | v5_6 | v5_7 | Frontmatter scope statement, §12 patch index, (add registry-mgmt-guide row if visible) |
| wa-patch-instruction | v2_0 | v2_1 | Frontmatter, scope pointers, §12-equivalent patch-index rows |
| wa-directive-instruction | v1_0 | v1_1 | Frontmatter + scope pointers only |
| wa-claudecode-instruction | v4_0 | v4_1 | Frontmatter, scope pointers, §3/§6/§8-area in-text pointers |
| wa-versecontext-instruction | v2_7 | v2_8 | Header "Governing rules" row (stale "v2"); Companion documents row (retired filenames) |
| wa-dimensionreview-instruction | v3_2 | v3_3 | Header "Governing rules" row (very stale "v1-2026-04-13"); Companion documents row |
| wa-sessionb-analysis-readiness | v1_5 | v1_6 | L10 governing rules row (stale v2_5). Already uses `[current]` in several places — a precedent. |
| wa-sessionb-analysis-output | v1 | v1_1 | Governing rules frontmatter reference |
| wa-sessionc-instruction | v1_4 | v1_5 | L9 governing rules (stale "v2") |
| wa-sessiond-orientation | v3_1 | v3_2 | Governing rules pointer in header; Companion documents row |

**Files NOT edited (intentional):**

- `wa-patch-specification-v1_14-20260416.md` — formally superseded by `wa-patch-instruction v2_0`. Retired; left as historical artefact.
- `wa-global-general-rules-v2_11-20260418.json` — primary governing document; the `[current]` rule is defined here. May need v2_12 at close to record sweep completion (assessed at close).
- `wa-global-flags-v1_3-20260418.md` — active register. Will be updated to v1_4 at close.

**Files that cannot be updated this session (not present):**

- `wa-registry-management-guide-v{?}` — see O-006.

---

## O-008 — Execution order

1. WA-Reference first (authority document for §1.3, §1.4, §12).
2. Nine remaining instruction documents, any order.
3. Global Flags v1_3 → v1_4 recording FLAG-012 resolution and FLAG-013 status question.
4. Assess whether Global Rules needs v2_12.
5. Session log at close.
6. Unresolved items surfaced.

---

## O-009 through O-019 — Per-document edits

### O-009 — Edit 1: wa-reference v5_6 → v5_7 — COMPLETE

- **Output:** `wa-reference-v5_7-20260418.md` (dual-written, presented)
- **Changes applied:**
  - Frontmatter title, version, Supersedes, Governed-by updated
  - Scope statement (5 pointers to NOT-authoritative-documents) → all `[current]`
  - §12 Patch Index: 8 operational references updated to `[current]` (including stale `v3_0` → `[current]` for sessiond, and `v5_9` for registry-management-guide)
  - v5_7 Change Control entry added above retained v5_6 block
- **Provenance preserved:** Supersedes header correctly points to `wa-reference-v5_6-20260418.md`
- **Residual-ref scan:** clean — no operational versioned cross-references remain
- **Unresolved:** §1.4 row for `wa-registry-management-guide` kept as-is (pattern only; file still not in PF per O-006)

### O-010 — Edit 2: wa-patch-instruction v2_0 → v2_1 — COMPLETE

- **Output:** `wa-patch-instruction-v2_1-20260418.md` (dual-written)
- **Changes applied:**
  - Frontmatter: title, version, Supersedes layered (v2_0 → v2_1; prior supersessions preserved in note)
  - Scope statement (5 pointers) → `[current]`
  - §1.3 inline references to directive instruction (2 occurrences) → `[current]`
  - §1.4 Per-rule pointer to `wa-global-general-rules-v2_11 GR-PROG-005` → `[current]` (rule ID preserved)
  - §2 inline "Per wa-reference v5_6 §1.5" → `[current]`
  - §3, §4, §A.0 inline wa-reference pointers (5 occurrences) → `[current]`
  - §12 Verse Context section "Governed by" pointer → `[current]`
  - Appendix A.3 patch-type governing-document table: 5 operational refs → `[current]` (includes stale `v3_0`, `v5_9`, and 3x `v2_7`)
  - Footer Supersedes line updated to reflect v2_1
  - v2_1 Change Control entry added above retained v2_0 block
- **Provenance preserved:** v2_0 Supersedes line (listing wa-patch-specification v1_14 and wa-sessionb-cc-instructions v3_6 sections) retained in Change Control table for history; `_patch_meta.produced_by` field illustration at L145 retained as specific version (it is a provenance field per GR-REF-002)
- **Residual-ref scan:** clean — grep for non-provenance operational versioned refs returns zero
- **Count:** 17 operational references migrated to `[current]`; 4 provenance references preserved

### O-011 — Edit 3: wa-directive-instruction v1_0 → v1_1 — COMPLETE

- **Output:** `wa-directive-instruction-v1_1-20260418.md` (dual-written)
- **Changes applied:**
  - Frontmatter: title, version, Supersedes, Governed-by → `[current]`
  - Scope statement (4 pointers) → `[current]`
  - §1 role/method selection inline refs (3 occurrences of `wa-patch-instruction v2_0`; 1 of `global rules v2_11`) → `[current]`
  - §4 completion confirmation inline ref → `[current]`
  - §6 completion-confirmation parallel reference → `[current]`
  - §7 self-check inline rule reference → `[current]` (where applicable)
  - Footer superseded-by line updated to reflect v1_1
  - v1_0 Change Control retained below for provenance
- **Provenance preserved:** directive-template illustration at L183–184 (Produced by / Governed by example) — these are illustrative field values for the artefact, parallel to `_patch_meta.produced_by` which GR-REF-002 explicitly excludes from `[current]` treatment
- **Count:** 12 operational references migrated to `[current]`; 1 illustrative-template value preserved

### O-012 — Edit 4: wa-claudecode-instruction v4_0 → v4_1 — COMPLETE

- **Output:** `wa-claudecode-instruction-v4_1-20260418.md` (dual-written)
- **Changes applied:**
  - Frontmatter: title, version, Supersedes (layered), Governed-by → `[current]`
  - Scope statement (5 pointers) → `[current]`
  - Governing Rules table (5 rule-pointer rows in §Governing Rules) → `[current]`
  - §2 Data Foundation Pipeline inline refs → `[current]`
  - §3 Implementation Tasks inline refs → `[current]`
  - §4 JSON Export Workflow inline refs → `[current]`
  - §5 Programme State Queries inline ref → `[current]`
  - §6 Verse Context Operations: inline reference to versecontext-instruction → `[current]`; patch-format cross-ref → `[current]`
  - §8 Periodic Review Support / §9 Re-run Requirements: REPAIR and cluster/pool references → `[current]`
  - Footer Supersedes line updated to reflect v4_1
  - v4_0 Change Control retained below for provenance
- **Provenance preserved:** 3 inline references in the retained v4_0 Change Control (L65–67) describing what was moved from/to at the v4_0 consolidation — these are historical descriptions of the v4_0 event and legitimately stay with specific versions
- **Count:** 40 operational references migrated to `[current]`; 3 provenance references preserved
- **Residual-ref scan:** clean

### O-013 — Edit 5: wa-versecontext-instruction v2_7 → v2_8 — COMPLETE

- **Output:** `wa-versecontext-instruction-v2_8-20260418.md` (dual-written)
- **Scope note:** this was the most outdated document in the corpus — dotted versions (`v2.7`), mixed-case filenames, references to retired documents (DataPrep, Registry-Management-Guide-v5.4, etc.). Per researcher instruction ("reset cross-references to the new naming conventions and `[current]`"), the sweep covered both version token migration AND retired-document redirection.
- **Changes applied:**
  - Filename/title: `WA-VerseContext-Instruction-v2.7-20260414.md` → `wa-versecontext-instruction-v2_8-20260418.md` (GR-FILE-003/-007/-009 compliance)
  - Header Document table: Filename, Supersedes, Companion documents all updated
  - Companion documents row: replaced legacy list (WA-VerseContext-SetupInstruction-v1.1 │ WA-Reference-v5.5 │ WA-VerseContext-ImpactStudy-v3 │ WA-SessionB-Instruction-v4.8 │ patch_specification-v1.10) with current peers — wa-reference, wa-patch-instruction, wa-dimensionreview-instruction, wa-sessionb-analysis-readiness, wa-sessionb-analysis-output all as `[current]`
  - Change note rewritten for v2_8; v2_7 and v2_6 notes retained below for provenance
  - Governing Rules section: governing file reference → `[current]`; stale "State aloud" example sentence replaced with reference to GR-LOAD-001
  - Body: §1457 DataPrep gate check reference → `wa-sessionb-analysis-readiness [current]` Section 4.1
  - Body: §1543, §1548 `WA-Registry-Management-Guide-v5.4 Section 7` → `wa-registry-management-guide [current] Section 7`
  - Body: §1552-1554 stage-instruction table — three retired document rows replaced with current instruction names (Analysis Readiness, Analysis Output; Extraction row marked retired)
  - Footer: v2_8 supersedes line prepended; historical v2.2 footer retained for provenance
- **Provenance preserved:** five `"produced_by": "WA-VerseContext-Instruction-v1.8"` entries inside JSON template examples (lines ~394, ~837, ~1142, ~1565, ~1621) — these illustrate provenance fields per GR-REF-002 and are legitimately specific-version
- **Residual-ref scan:** clean for all retired-doc operational references

**New unresolved item for researcher attention:**

- Line 1331 contains a reference to `WA-PipelineStatusReview-v2-20260330 Section 3.2` ("Full patch specification"). This document is not present in the current corpus and has no obvious successor. Left as-is; flagged here for researcher review. Possible resolutions: (a) retarget to current patch instruction if content was absorbed; (b) remove the reference if the pipeline review process is retired; (c) restore the document if still operational.
- The term "DataPrep" remains in body prose (lines 45, 70, 809, 1265, 1455, 1457, 1469, 1540, 1556) as a stage name/concept rather than a document reference. Per GR-REF-002 scope (operational cross-references to documents), these are out of scope for this sweep. A separate terminology pass may be warranted — flagged for researcher decision.

### O-014 — Edit 6: wa-dimensionreview-instruction v3_2 → v3_3 — COMPLETE

- **Output:** `wa-dimensionreview-instruction-v3_3-20260418.md` (dual-written)
- **Scope note:** document was severely outdated — governing-rules pointer cited `v1-2026-04-13` (5 major versions behind current v2_11); Companion documents row listed documents retired long ago (WA-SessionB-Instruction-v4.8, patch_specification-v1.10, WA-Registry-Management-Guide-v5.8, WA-SessionD-Orientation-v3.0, WA-VerseContext-Instruction-v3.1). Same approach as Edit 5: version sweep + retired-document redirection.
- **Changes applied:**
  - Title banner: `Version 3.2 | 20260417` → `Version 3_3 | 20260418` (GR-FILE-003 underscored convention)
  - Header table: Filename, Supersedes, Governing rules, Companion documents all refreshed
  - Governing rules: `wa-global-general-rules-v1-2026-04-13.json` → `wa-global-general-rules [current]` with GR-LOAD-001 reference
  - Companion documents row: legacy list (6 retired docs) → current corpus (7 active docs, all `[current]`)
  - v3_3 Change note prepended; v3.2/v3.1/v3.0 notes retained for provenance
  - §5.3 body reference: `WA-VerseContext-Instruction-v3.1` VCB re-run pointer → `[current]`
  - §6.6 Phase B.5 reference → `[current]`
  - §6.7 return instruction template: Instruction version line, VCB re-run trigger → `[current]`
  - §8 startup protocol: `State: *"Global rules wa-global-general-rules-v2-20260414.json loaded."*` → generic reference to GR-LOAD-001 confirmation format
  - §11 CC directive metadata example: `Governing instruction` line → `[current]`
  - §11 body note on DIMREVIEW session_b_status: exception reference `patch_specification-v1.10` → `wa-patch-instruction [current]`
  - §16 patch-index table: two rows (DIMREVIEW, DIMREVIEW-GRPDESC) → `[current]`
  - Footer superseded-by line refreshed; historical v3.2 footer retained
- **Provenance preserved:** JSON template illustrations of `produced_by`, `instruction_version`, `dim_review_version` fields (lines ~849, ~931, ~961) — these are database/artefact provenance fields per GR-REF-002 and legitimately stay specific-version as illustrative examples
- **Count:** 10 operational references migrated to `[current]`; 3 provenance field illustrations preserved
- **Residual-ref scan:** clean for operational references

### O-015 — Edit 7: wa-sessionb-analysis-readiness v1_5 → v1_6 — COMPLETE

- **Output:** `wa-sessionb-analysis-readiness-v1_6-20260418.md` (dual-written)
- **Scope note:** This document was partly ahead of the curve — it already used `v[current]` in several attachment-instruction places (§What to Attach, §Sub-process paths). It had some specific-version stragglers and retired-document references.
- **Changes applied:**
  - Version banner: `Version 1.5 | 20260416` → `Version 1_6 | 20260418`
  - Filename and Supersedes rows refreshed
  - Companion documents row: stale `wa-global-general-rules-v2_5-20260416.json` and retired `wa-sessionb-cc-instructions` / `wa-patch-specification` replaced with current corpus (wa-global-general-rules, wa-reference, wa-dimensionreview-instruction, wa-versecontext-instruction, wa-claudecode-instruction, wa-patch-instruction, wa-directive-instruction) — all `[current]`
  - Governing Rules section: stale version pointer + stale State-aloud example → `[current]` + GR-LOAD-001 reference
  - §What to Attach at Session Start: `wa-global-general-rules-v2_2-20260415.json` → `[current]`; retired `wa-sessionb-cc-instructions` → `wa-claudecode-instruction [current]`
  - §Step 1.4 patch construction: retired `wa-patch-specification` → `wa-patch-instruction [current]`
  - v1_6 Change Log entry prepended; v1_5 retained below for provenance
  - Footer file line updated
- **Provenance preserved:** `wa-global-sessionb-instruction-v5_0-20260415.md` reference in "prior version history" note — legitimately specific-version
- **Residual-ref scan:** clean for operational references

### O-016 — Edit 8: wa-sessionb-analysis-output v1 → v1_1 — COMPLETE

- **Output:** `wa-sessionb-analysis-output-v1_1-20260418.md` (dual-written)
- **Scope note:** This document was already using `-v[current]` notation throughout, but with a non-canonical form (hyphen + `v` + `[current]` + file extension). GR-REF-002 canonical form is just `[current]` after the document name. Normalised throughout. Two real retirement transitions: `wa-sessionb-cc-instructions` → `wa-claudecode-instruction`; `wa-patch-specification` → `wa-patch-instruction`.
- **Changes applied:**
  - Version banner: `Version 1.0 | 20260416 | Status: Draft` → `Version 1_1 | 20260418 | Status: Active`
  - Filename, Supersedes (layered) rows refreshed
  - Companion documents row: retired `wa-sessionb-cc-instructions`, `wa-patch-specification` replaced with `wa-claudecode-instruction`, `wa-patch-instruction`; added `wa-reference`, `wa-directive-instruction`, `wa-sessionc-instruction`; `wa-global-sessionc-prose-rule` kept (still active document, not retired)
  - Governing Rules section: `-v[current].json` form normalised → `[current]`; stale State-aloud example replaced with GR-LOAD-001 reference
  - Pipeline Position box: Analysis Readiness reference normalised to `[current]`
  - §What to Attach at Session Start: Global rules form normalised; retired `wa-sessionb-cc-instructions` → `wa-claudecode-instruction [current]`
  - §Stage 2c three separate references to `wa-global-sessionc-prose-rule-v[current].md` → `wa-global-sessionc-prose-rule [current]` (form normalisation only — document itself remains)
  - Footer paired-with line normalised; footer filename line refreshed
  - Change Log section inserted (v1 had no change log; banner noted "takes effect from v1.1"; v1_1 is that moment)
- **Provenance preserved:** Supersedes layered reference to `wa-global-sessionb-instruction-v5_0-20260415.md` retained in Supersedes row as provenance
- **Residual-ref scan:** clean (single instance of `-v[current]` in the v1_1 Change Log entry itself — legitimate, describing what was changed)

### O-017 — Edit 9: wa-sessionc-instruction v1_4 → v1_5 — COMPLETE

- **Output:** `wa-sessionc-instruction-v1_5-20260418.md` (dual-written)
- **Scope note:** simplest sweep in the batch. Document only references governing rules; no sibling instruction cross-references.
- **Changes applied:**
  - Banner: `Instruction v1.4 | 20260414` → `Instruction v1_5 | 20260418`
  - Governing Rules section: stale `wa-global-general-rules-v2-20260414.json` → `[current]`; State-aloud example → GR-LOAD-001 reference
  - v1_5 Change Log entry prepended; v1.4 entry retained for provenance
- **FLAG-001 note:** This instruction remains flagged as "under construction" pending completion of Analysis Readiness and Analysis Output. The reference sweep does not resolve FLAG-001 — content completeness is a separate question from reference hygiene. FLAG-001 stays Open.
- **Residual-ref scan:** clean

### O-018 — Edit 10: wa-sessiond-orientation v3_1 → v3_2 — COMPLETE

- **Output:** `wa-sessiond-orientation-v3_2-20260418.md` (dual-written)
- **Scope note:** Legacy document pattern (dotted version `v3.1`, mixed-case filename, retired-companion references). Same full treatment as versecontext (Edit 5) and dimensionreview (Edit 6).
- **Changes applied:**
  - Filename/title: `WA-SessionD-Orientation-v3.1-20260414.md` → `wa-sessiond-orientation-v3_2-20260418.md`
  - Version banner: `Version 3.1 | 20260414` → `Version 3_2 | 20260418`
  - Header table: Filename, Supersedes, Change note, Companion documents all refreshed
  - Companion documents: retired `WA-SessionB-Instruction-v4.8`, `WA-Registry-Management-Guide-v5.8`, `WA-Reference-v5.5`, `patch_specification-v1.10` replaced with current corpus (wa-sessionb-analysis-readiness, wa-sessionb-analysis-output, wa-registry-management-guide, wa-reference, wa-patch-instruction, wa-dimensionreview-instruction) — all `[current]`
  - Governing Rules section: stale `wa-global-general-rules-v2-20260414.json` → `[current]`; State-aloud example → GR-LOAD-001
  - Footer: v3_2 superseded-by line prepended; historical v3.1 footer retained
- **Provenance preserved:** v3.1 historical change note in the Change note cell; historical v3.1 footer
- **Residual-ref scan:** clean

### O-019 — Instruction corpus sweep COMPLETE

All ten programme instruction documents have been edited, dual-written, and presented:

| # | Original | New | Scope |
|---|---|---|---|
| 1 | wa-reference-v5_6 | v5_7 | targeted GR-REF-002 (9 ops refs, 1 flag-file pointer stale) |
| 2 | wa-patch-instruction-v2_0 | v2_1 | targeted GR-REF-002 (17 ops refs) |
| 3 | wa-directive-instruction-v1_0 | v1_1 | targeted GR-REF-002 (12 ops refs) |
| 4 | wa-claudecode-instruction-v4_0 | v4_1 | targeted GR-REF-002 (40 ops refs) |
| 5 | wa-versecontext-instruction-v2_7 | v2_8 | full — legacy filename + companion docs + body retired refs |
| 6 | wa-dimensionreview-instruction-v3_2 | v3_3 | full — legacy governing rules (v1-2026-04-13!) + companion docs + body refs |
| 7 | wa-sessionb-analysis-readiness-v1_5 | v1_6 | targeted + retired companion doc replacements |
| 8 | wa-sessionb-analysis-output-v1 | v1_1 | normalise `-v[current]` → `[current]` + retired companion docs |
| 9 | wa-sessionc-instruction-v1_4 | v1_5 | header only (no sibling-instruction cross-refs) |
| 10 | wa-sessiond-orientation-v3_1 | v3_2 | full — legacy filename + companion docs |

**Cumulative operational references migrated to `[current]`:** approximately 130+
**Cumulative provenance references correctly preserved:** approximately 25 (Supersedes, produced_by, instruction_version fields, change log historical entries)

### O-020 — Edit 11: wa-global-flags v1_3 → v1_4 — COMPLETE

- **Output:** `wa-global-flags-v1_4-20260418.md` (dual-written)
- **Changes applied:**
  - Header metadata, summary table, change-from-v1_3 narrative refreshed
  - **FLAG-012 moved Open → Resolved** — sweep executed in this session; full edit table added to the flag entry for audit
  - **FLAG-013 updated** — Status remains Open; sequencing note added explaining that FLAG-012 ran first per researcher direction (a direction call, not a rule change). The logical rationale that FLAG-013 findings might require a re-sweep remains valid but is lower-cost than delaying FLAG-012.
  - **FLAG-014 added Open** — records the two legacy references in versecontext that could not be mechanically migrated (WA-PipelineStatusReview L1331; "DataPrep" terminology persistence in body prose)
  - **FLAG-015 added Open** — records the registry-management-guide not visible in Project Files despite researcher-reported upload
  - Change register updated for v1_4
- **Flag counts at v1_4:** 8 Open | 5 Resolved | 1 Obsolete | 0 Standing | Total 14

### O-021 — Session close

- **Time:** 2026-04-18, session close
- **Session log produced:** `wa-global-ref-consistency-session-log-v1-20260418.md` (per GR-OBS-003)
- **Total outputs produced this session:** 13 files
  - 1 × WA-Reference v5_7
  - 9 × other instruction documents (minor version bumps)
  - 1 × Global Flags v1_4
  - 1 × Observations log (this file)
  - 1 × Session log (handoff)
- **Work remaining (captured in flags for next session):**
  - FLAG-013 — document_discipline classification review
  - FLAG-014 — PipelineStatusReview reference and DataPrep terminology
  - FLAG-015 — registry management guide visibility
  - FLAG-010 — broader post-GR-v2_8 instruction audit (blocking gate on new word analysis; partially addressed by FLAG-012 resolution but not fully — the audit scope is broader than references)
- **No researcher decisions deferred.** All items raised in session were resolved or captured as flags.

---

## Change register

- **v1 (2026-04-18):** File created. Full session task recorded: §1.4 correlation check → researcher-authorised full programme-wide GR-REF-002 sweep (effectively FLAG-012) → 10 instruction documents edited and version-bumped → global flags updated to v1_4 recording resolutions and new items → session log produced. 22 obs log entries (O-001 through O-021). All outputs dual-written per GR-FILE-008; all substantive writes followed by `present_files` per GR-CAD-001.
