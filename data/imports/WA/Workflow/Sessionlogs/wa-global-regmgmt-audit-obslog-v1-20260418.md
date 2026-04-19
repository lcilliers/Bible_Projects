# WA Reference Audit — Registry Management Guide — Observations Log

**Filename:** wa-global-regmgmt-audit-obslog-v1-20260418.md
**Version:** v1
**Date:** 2026-04-18
**Session type:** Reference audit — registry management guide v5_9
**Governing rules:** wa-global-general-rules-v2_11-20260418.json; wa-global-flags-v1_4-20260418.md
**Previous output reference:** wa-global-ref-consistency-obslog-v1-20260418.md (FLAG-012 session — 10 documents swept; registry management guide deferred due to absence from Project Files, tracked as FLAG-015)

---

## Purpose

Complete the reference audit for the final document outstanding: **wa-registry-management-guide-v5_9-20260414.md**. Align references to other instruction files per GR-REF-001 and GR-REF-002. Check that all referenced global rules resolve correctly. Identify global rules that should additionally be referenced in the management guide. Complete three flags:

- **FLAG-012** — partial resolution: registry management guide was excluded from original sweep; complete the sweep now (retroactive close-out).
- **FLAG-014** — check whether legacy references of the two forms surfaced during original sweep (`WA-PipelineStatusReview-v2-20260330`; "DataPrep" terminology) also appear in the registry management guide; progress this flag.
- **FLAG-015** — confirm document is now present in Project Files; execute the equivalent FLAG-012 sweep on it; resolve flag.

---

## Session entries

### O-001 — Session start confirmations (2026-04-18)

- Global rules loaded per GR-LOAD-001 v3_0: wa-global-general-rules-v2_11-20260418.json — 59 rules (36 active), 14 categories.
- Global flags loaded: wa-global-flags-v1_4-20260418.md — 8 open, 5 resolved, 1 obsolete, 0 standing.
- Cadence discipline M1+M4 active.
- Registry management guide confirmed present at `/mnt/project/wa-registry-management-guide-v5_9-20260414.md` (50,612 bytes). FLAG-015 gate condition cleared — the file is available for the sweep.

### O-002 — Task scope acknowledgement

Researcher task:
1. Align references in the registry management guide to the files currently in Project Files, following GR-REF-001 and GR-REF-002.
2. Verify every referenced global rule (GR-* rule ID) resolves correctly against the active rules in v2_11.
3. Identify global rules that *should* be referenced in the management guide but currently are not.
4. Complete the three flags (FLAG-012, FLAG-014, FLAG-015).

Scope boundary: the task is a reference audit on a single document. It is not a full content audit of the guide. Analytical findings that surface during the read (e.g. scope creep, duplicated content) will be noted but not actioned unless they bear on the reference discipline.

---

## Findings

### O-003 — Project Files inventory (state check, 2026-04-18)

Project Files contents confirmed:

- wa-global-general-rules-v2_11-20260418.json
- wa-global-flags-v1_4-20260418.md
- wa-reference-v5_6-20260418.md
- wa-patch-instruction-v2_1-20260418.md
- wa-directive-instruction-v1_1-20260418.md
- wa-claudecode-instruction-v4_1-20260418.md
- wa-versecontext-instruction-v2_8-20260418.md
- wa-dimensionreview-instruction-v3_3-20260418.md
- wa-sessionb-analysis-readiness-v1_6-20260418.md
- wa-sessionb-analysis-output-v1_1-20260418.md
- wa-sessionc-instruction-v1_5-20260418.md
- wa-sessiond-orientation-v3_2-20260418.md (also legacy v3_1 present)
- wa-registry-management-guide-v5_9-20260414.md
- database-schema-v3_9_0-20260416.json

Consequence for audit: every `[current]` pointer in the updated guide will resolve against this list.

### O-004 — Reference inventory in v5_9 (cross-document references)

Raw inventory of all references to other documents in the guide:

| # | Location | Current text | Type | Disposition |
|---|---|---|---|---|
| 1 | L9 (Filename field) | `wa-registry-management-guide-v5.9-20260414.md` | Self (filename) | Dot-version violates GR-FILE-003 v3_0. Will become `v5_10` on bump. |
| 2 | L10 (Supersedes field) | `WA-Registry-Management-Guide-v5.8-20260412.md` | Provenance | Capital WA and dot format both pre-current; per GR-REF-002 provenance retains specific version — format will be normalised to lowercase+underscore on the v5_10 Supersedes line pointing to v5_9. |
| 3 | L13 (Not covered) | `WA-VerseContext-Instruction-v2.6-20260414` | Operational | Stale (current is v2_8). Migrate to `wa-versecontext-instruction [current]`. |
| 4 | L13 (Not covered) | `WA-SessionB-Instruction-v4.8-20260414` | Operational | **Retired document** per FLAG-003. Replace with two documents: `wa-sessionb-analysis-readiness [current]` and `wa-sessionb-analysis-output [current]`. |
| 5 | L19 (Change Control v5_9 row) | `wa-global-general-rules-v2-20260414.json` | Provenance (describes a historical v5_9 action) | Leave — historical accuracy. |
| 6 | L35 (Governing Rules body) | `wa-global-general-rules-v2-20260414.json` | **Operational** (governing-rules pointer) | Migrate to `wa-global-general-rules [current]`. |
| 7 | L86 (§2 body) | `WA-Reference Section 4.3` | Operational | Migrate to `wa-reference [current] §4.3`. |
| 8 | L288 (§5.2 body) | `WA-SessionB-Instruction-v4.7` | Operational | Retired document. Replace with reference to the two successor documents or recast the sentence. |
| 9 | L696 (§8 terminology) | `WA-Reference Section 16` | Operational | Migrate to `wa-reference [current] §16`. |
| 10 | L731 footer | `WA-Registry-Management-Guide-v5.8` provenance line | Provenance | Retain as historical footer. |
| 11 | L733 footer | `WA-Registry-Management-Guide-v5.8` provenance line | Provenance | Retain as historical footer. |
| 12 | L735 footer | `WA-Registry-Management-Guide-v5.7` provenance line | Provenance | Retain as historical footer. |

### O-005 — GR rule ID citations in v5_9 — resolution check against v2_11

The guide cites two GR rule IDs: `GR-DATA-008` (at L20 and L39) and `GR-FILE-009` (at L19).

- **GR-FILE-009** — resolves correctly. Active rule in v2_11, subject "Compact date format in filenames". No action.
- **GR-DATA-008** — **does NOT resolve.** This rule ID does not appear in the v2_11 rules array and is not present in any of the three addendums (addendum_instructions, addendum_patch_directive, addendum_reference). Searches against the full v2_11 JSON for rule-text matching the concept ("engine-derived Phase 1 fields are stale — use live queries for current counts") return no candidate absorbing rule.

Consequence: the "per GR-DATA-008" citation at L39 is a dangling reference. The substantive guidance at L39 ("phase1_term_count, phase1_verse_count, unique_term_count, shared_term_count, term_sharing_ratio reflect Phase 1 state only and are not updated by later pipeline stages — use live queries against wa_term_inventory for current counts") is valuable content in its own right — it concerns field-level meaning, which is squarely within this guide's authority as the registry reference document.

**Judgement call (under researcher authorisation):** remove the dangling `GR-DATA-008` citation at L39 and at L20 (change-control row); retain the substantive guidance inline without a rule-ID pointer. The guide owns this content; no rule pointer is needed. Logged for researcher visibility.

### O-006 — Missing GR rule citations that should appear in the guide

Rules that govern content already present in the guide but are not currently cited:

| Rule | Relevance | Action |
|---|---|---|
| GR-DATA-001 (active terms filter `AND mt.status IN ('extracted','extracted_thin')`) | §6a.3 Mechanism 2 & 3 queries; §6b.2 detection query; §6c.1 VCB-scope query — all use this filter | Add citation where the filter first appears (§6a.3 intro) and where the query is defined in §6c.1 |
| GR-FILE-001 through GR-FILE-009 (file naming) | §9 File Naming Reference — currently cites no GR rules; §9 is programme-specific application of these rules | Add "governed by GR-FILE-001 through GR-FILE-009; see wa-reference [current] §1 for the full pattern catalogue" pointer at §9 intro |
| GR-REF-001 Discipline 5 (scope statement) | Whole-document scope — every document freshly swept under FLAG-012 now includes a Document Scope section | Add Document Scope section after header per pattern |
| GR-REF-002 (current-version reference convention) | Applies to every operational cross-reference in this document | Implicit through use of `[current]`; named in Change Control note |
| Delete-flagged pattern (formerly GR-OBS-005, now migrated to ADD-PATCHDIR-004) | §2a, §3a.2 per-field behaviour table, §6a, §6b all reference `delete_flagged` as the no-physical-delete mechanism | Rule migrated; do not cite obsolete rule ID. Retain descriptive language. Noted for visibility only. |

### O-007 — Legacy-reference check (FLAG-014 context)

FLAG-014 raised two legacy reference types found during the original sweep:

1. `WA-PipelineStatusReview-v2-20260330` — searched in the guide: **not present**. No action needed for this document.
2. "DataPrep" terminology — searched in the guide:

| Location | Context | Action |
|---|---|---|
| L28 (Change Control v5.8 row) | Historical change note describing v5.8: "DataPrep-Instruction removed (retired)" | Historical — leave. |
| L29 (Change Control v5.8 row) | Historical change note describing v5.8 DataPrep gate removal | Historical — leave. |
| L137 (§3.1 `Ready for Analysis` status definition) | "Legacy status — no longer used in active pipeline (DataPrep step retired)" | Current-state text: "DataPrep" functions as a retirement marker for readers familiar with the former vocabulary. Acceptable. Leave. |
| L731, L733 (footer) | Historical footers recording what v5.8 did | Historical — leave. |

Consequence for FLAG-014: the "DataPrep" persistence in this guide is localised to historical change notes (correct use) and one current-state line where it functions as a retirement marker. No migration needed in the registry management guide. The FLAG-014 open action concerning "DataPrep" persistence in versecontext instruction body prose (per the flag's raising note) remains unchanged by this audit.

### O-008 — Other structural/format issues surfaced during read-through

- **L1–L9 header format.** Filename field (L9) uses `v5.9` dot-format; GR-FILE-003 v3_0 requires underscore. The new version filename will be `wa-registry-management-guide-v5_10-20260418.md`.
- **Document scope section missing.** All four primary documents swept under FLAG-012 (wa-reference, wa-patch-instruction, wa-directive-instruction, wa-versecontext-instruction at minimum) now carry a "Document scope" section per GR-REF-001 Discipline 5. The registry management guide lacks one. Add it.
- **Section numbering gap.** §7 jumps directly from §6c.3 to §7.1 (no §7 parent heading) and §7a follows §7.2. Not a reference-audit issue but noted for researcher visibility — not actioned in this sweep.

### O-009 — Decisions made under researcher authorisation

1. Remove dangling `GR-DATA-008` citation at L20 and L39; retain substantive text inline.
2. Add Document Scope section per GR-REF-001 Discipline 5 pattern.
3. Migrate six operational cross-references (items 3, 4, 6, 7, 8, 9 in O-004) to `[current]` form.
4. Retain provenance references in header Supersedes and in historical footers (items 2, 5, 10, 11, 12 in O-004).
5. Retire `WA-SessionB-Instruction-v4.7/4.8` references by pointing to the two successor documents.
6. Add GR-DATA-001 citation at §6a.3 and §6c.1.
7. Add "governed by GR-FILE-001 through GR-FILE-009" pointer at §9 intro; point to `wa-reference [current] §1`.
8. Bump version to v5_10-20260418. Underscore format in filename. Add v5_10 Change Control row naming all of the above.
9. Update flags file: FLAG-012 retroactively extended to cover this 11th document; FLAG-014 updated with the guide check outcome; FLAG-015 → Resolved.

---

## Decisions log

| ID | Decision | Basis |
|---|---|---|
| D-001 | Remove dangling GR-DATA-008 citation (2 instances). Retain substantive guidance inline. | Rule not present in v2_11 rules or addendums; guide owns field-meaning content. |
| D-002 | Add Document Scope section per GR-REF-001 Discipline 5. | Pattern established by all four FLAG-012-swept primary documents; rule applies to every document. |
| D-003 | Bump to v5_10; filename uses underscore format. | GR-FILE-003 v3_0 required format. |
| D-004 | SessionB-Instruction-v4.7/v4.8 reference retired in favour of two successor documents. | FLAG-003 resolved by retirement of former document; wa-sessionb-analysis-readiness and wa-sessionb-analysis-output are successors. |
| D-005 | Add GR-DATA-001, GR-FILE-001 through GR-FILE-009, GR-REF-001 Discipline 5 citations. | Rules cover content already present but uncited. |
| D-006 | FLAG-012 retroactively extended to close registry management guide; FLAG-014 closed for this document; FLAG-015 resolved. | Scope of sweep now covers all 11 documents, including the previously-missing guide. |

---

## Next steps at session close

1. Produce wa-registry-management-guide-v5_10-20260418.md with all O-009 changes applied.
2. Produce wa-global-flags-v1_5-20260418.md reflecting D-006.
3. Produce session log.
4. Dual-write per GR-FILE-008; present_files per GR-CAD-001.

---

### O-010 — Guide v5_10 produced (2026-04-18)

File written: `wa-registry-management-guide-v5_10-20260418.md` in working dir and /mnt/user-data/outputs/ per GR-FILE-008.

Changes applied (mapped to O-009 items):

1. **O-009.1 — Dangling GR-DATA-008 removed.** Removed at §Governing Rules body (former L39) and at v5_9 Change Control row (former L20). Substantive guidance retained inline: "Use live queries against `wa_term_inventory` for current counts."
2. **O-009.2 — Document scope section added.** New section after header. Lists what the guide is authoritative for; lists what the guide points to with `[current]` pointers. References GR-REF-001 Discipline 5 and GR-REF-001 Discipline 1.
3. **O-009.3 — Six operational cross-references migrated to `[current]`:**
   - Header "Not covered" row: `WA-VerseContext-Instruction-v2.6-20260414` → `wa-versecontext-instruction [current]`; `WA-SessionB-Instruction-v4.8-20260414` → `wa-sessionb-analysis-readiness [current]` and `wa-sessionb-analysis-output [current]`.
   - §Governing Rules body: `wa-global-general-rules-v2-20260414.json` → `wa-global-general-rules [current]`.
   - §2 dimensions field: `WA-Reference Section 4.3` → `wa-reference [current] §4.3`.
   - §5.2 body: `WA-SessionB-Instruction-v4.7` → `wa-sessionb-analysis-readiness [current]` (Stage 1) + `wa-sessionb-analysis-output [current]` (Stages 2–3).
   - §8 Anchor verse definition: `WA-Reference Section 16` → `wa-reference [current] §16`.
   - §8 Patch definition: added pointer to `wa-patch-instruction [current]`.
4. **O-009.4 — Provenance references retained.** Header Supersedes: `wa-registry-management-guide-v5_9-20260414.md` (normalised to lowercase+underscore). v5_9 Change Control historical row retained with its v2-global-rules reference as historical provenance. Historical footer lines preserved.
5. **O-009.5 — retired SessionB references redirected** (see item 3 above).
6. **O-009.6 — GR-DATA-001 citation added** at §6a intro and §6a.3 intro (before the SQL queries); at §6b.2 root cause paragraph where the filter's operational role is explained; at §6c intro; at §6c.1 description paragraph. Four citations.
7. **O-009.7 — GR-FILE-001 through GR-FILE-009 pointer added** at §9 File Naming Reference intro with pointer to `wa-reference [current] §1` for the full pattern catalogue.
8. **O-009.8 — v5_10 Change Control row added** naming all changes; filename migrated to underscore format.
9. **Additional touches made during edit** (all within the reference-alignment scope):
   - "Governed by" row added to document header metadata table (was missing).
   - §3.1 Verse Context Reset — "pool-based Session B" text removed, replaced with "cluster-order Session B" to match the retired-pools reality (this was a latent inconsistency the reference alignment surfaced; correction is a minor terminology fix, not an architecture decision).
   - §6.9 heading "Pool Processing Readiness (Stage 2)" → "Cluster-Order Processing Readiness (Stage 2)" for the same reason.
   - §7a retired-pools section — text retained as-is (it is already a retirement notice).
   - §8 Pool, Pool/cluster batch, Pool analysis dataset definitions — added "Retired (see §7a)" marker to each. Definitions retained for continuity of reference.
   - §8 Session B definition — "Now operates on pool/cluster batches, not isolated words" text corrected to "Operates on individual registries in cluster order — see §5.2" to match current architecture.
   - §8 Verse Context Reset definition — "pool-based Session B" → "cluster-order Session B".
   - Footer lines: added a new v5_9 footer line (for continuity), retained v5.8 and v5.7 lines.

**Compliance check:**
- GR-REF-001 Discipline 1 (pointer not copy): no re-statement of content from pointed-to documents.
- GR-REF-001 Discipline 3 (single authoritative document): this guide explicitly disclaims authority for schema, file naming catalogue, patch format, directive format, CC routines, and stage-specific procedure — all pointed to their authoritative homes.
- GR-REF-001 Discipline 5 (scope statement): new Document scope section names the guide's authoritative scope.
- GR-REF-002: all operational cross-references use `[current]`; provenance references retain specific versions.
- GR-FILE-003 v3_0: filename uses underscore version format `v5_10`.
- GR-FILE-007: filename fully lowercase.
- GR-FILE-009: filename uses compact date 20260418.

### O-011 — Flag updates to be applied in v1_5

| Flag | From | To | Rationale |
|---|---|---|---|
| FLAG-012 | Resolved (10 docs) | Resolved (11 docs) — extended | Registry management guide added to the sweep retroactively; v5_9 → v5_10 produced per the FLAG-012 pattern. |
| FLAG-014 | Open | Open — partially progressed | Check against registry management guide complete: "DataPrep" persistence is contained in historical change notes and one retirement marker (acceptable); `WA-PipelineStatusReview-v2-20260330` not present in the guide. FLAG-014 remains open for the other documents where the "DataPrep" terminology concern was raised. Updated description to record this guide's clearance. |
| FLAG-015 | Open | **Resolved** | Document is now present in Project Files; FLAG-012 sweep equivalent applied; references migrated to `[current]`. |

### O-012 — Flags file v1_5 produced (2026-04-18)

File written: `wa-global-flags-v1_5-20260418.md` in working dir and /mnt/user-data/outputs/ per GR-FILE-008.

Changes applied:

- **FLAG-012** description extended to document tranche 2 (the 11th document — registry management guide). Tranche 1 resolution text preserved; tranche 2 table added showing v5_9 → v5_10 with the 6 refs + Document Scope + GR-DATA-001 citations.
- **FLAG-014** description extended with a "Update 2026-04-18 (registry management guide check)" paragraph recording: `WA-PipelineStatusReview-v2-20260330` not present in the guide; "DataPrep" persistence clearance (historical change notes acceptable, one retirement marker in §3.1 acceptable). Flag remains Open for the versecontext instruction.
- **FLAG-015** moved Open → Resolved. Resolution paragraph added recording the resolution action (tranche 2 sweep + v5_10 production). Status flag line updated. Session record reference added.
- Summary table updated: Open 8 → 7; Resolved 5 → 6; total unchanged at 14.
- Change from v1_4 paragraph rewritten at top.
- Change register has new v1_5 entry; all prior entries preserved.

**Compliance check:**
- GR-FILE-003 v3_0: filename uses underscore version format `v1_5`.
- GR-FILE-007: filename fully lowercase.
- GR-FILE-009: filename uses compact date 20260418.
- GR-FILE-004 (obsolete — but new file rather than overwrite anyway): new versioned file produced; v1_4 preserved for audit.
- GR-REF-002: operational references in the flags file use `[current]` where applicable (the body is mostly flag narrative, not cross-references; internal references to other flag documents are provenance — dated and versioned correctly).
