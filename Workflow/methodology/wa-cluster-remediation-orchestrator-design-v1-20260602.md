# Cluster remediation orchestrator — design

**Living document · Doc version 1 · 2026-06-02.** Pairs with the playbook
`wa-cluster-remediation-playbook-v1-20260601.md` and the auditor
`scripts/audit_cluster_v1_20260601.py`. Implements the playbook's "one loop, one
handler per aspect" as a **single packaged command** that remediates one cluster
end-to-end.

## MODEL REVISION — A6/A7/D2 are a comment→findings evaluation (researcher, 2026-06-02)

The "dispositions / adoption" framing was too narrow. A6 gating flags, A7 stray
Session-B findings and D2 pointers are all the **same operation**: their full text
(`description` / `finding`) is analytical raw material to be **evaluated into
findings**, not cleared away. Decisions taken this session:

1. **Per-affected-cluster seeding.** A comment creates a finding in **each** cluster
   it links to (comment-centric, multi-cluster). Each seeded finding is then reviewed
   in the light of *that* cluster's own analysis when its turn comes. We do NOT attempt
   programme-wide inter-cluster resolution now — the full data will never fit one AI
   context. Seed, then validate per cluster.
2. **Session D is moot.** It will in practice never run; many `SD_POINTER`s were a way
   to defer work ("pass the buck"). The DB already holds enough to resolve them now in
   Session-B / cluster analytics and produce proper findings that reach the cluster
   narrative. **There is no "route to Session D" outcome.** `session_target=D` pointers
   are mined for findings like everything else.
3. **AI-evaluated, interactive — not mechanical.** Each comment is understood on its
   underlying data through researcher↔AI debate to the right conclusion. This is NOT a
   fit-all auto-classifier. CC prepares the data package and writes the agreed findings
   as patches; the `"approved": true` gate becomes the researcher's sign-off on the
   proposed findings.

**Resulting outcomes per comment:** `create finding(s)` (one per affected cluster) |
`set aside non-evidenced` (still recorded as informing — not deletion). The two
handlers DISPOSITIONS (A6/A7) and ADOPTION (D2) therefore **merge** into one
`COMMENT_EVALUATION` handler. Caveat: if an affected cluster is already closed
(M10b/M10c), a new finding there is flagged for re-open/review rather than silently
written. Build the finding-writer only after the first interactive batches settle the
pattern (do not pre-automate an analytical step).

**Applier (built 2026-06-02):** `scripts/_apply_comment_findings_v1_20260602.py` —
reads an approved spec (`new_findings` → INSERT cluster_finding; `new_flags` → INSERT
reciprocal pointer; `fold_findings` → close the source SB finding). Never edits existing
findings (separate concepts = separate findings). First run: M38 comment 33
(`DIM-039-001`, salvation × debauchery) → 2 standalone M38-A findings + M28 reciprocal.

**RULE — verse-change → revalidation (researcher 2026-06-02).** reset-if-complete was
built for *pointer* assignment; it must also cover *verse-data* changes. A **material**
verse change — verse-record deletion, meaning/keyword change, is_relevant/anchor
re-classification — invalidates findings resting on it, so if it touches an
`Analysis Complete` cluster that cluster resets to `Ready for re-analysis`. *Identity-
preserving* changes (e.g. re-pointing `verse_record_id` to a surviving duplicate during
the dedup-ghost repair) do NOT reset. The dedup-ghost repair
(`_repair_dedup_ghost_verses_v1`) and the auditor's VRACT guard (B1a/B1b/B2 exclude
verses whose verse-record is soft-deleted) implement the data side; verse-changing
appliers carry the reset rule.

**RULE — reciprocal pointers must be `SD_CLUSTER`, not `SD_POINTER`.** A reciprocal queued
for another cluster (via `cluster_link`) must use a **non-A6-gating** code. `SD_POINTER` is
an A6 gating code; since registries feed multiple clusters (reg 39 → both M38 and M28), a
`SD_POINTER` reciprocal would re-gate the *source* cluster's A6. `SD_CLUSTER` still surfaces
as the target's D2 pointer but does not gate A6 anywhere. Each evaluated comment also
**verse-checks the nature** of the relationship (co-occurrence vs lexical/structural) — the
finding must state which (M38 33: 0 verse overlap → lexical, not a verse-pattern).

## Aim (researcher directive, 2026-06-02)

> "Building the remedial script for reuse on a single cluster, with all the remedial
> actions included… a master remedial orchestrator, calling individual processes when
> needed, but it comes as a package and operates as a package. We continue to select
> clusters in order of complexity, and in that way build out the remedial process."

So: **one orchestrator per cluster**, dispatching to the individual handler scripts,
producing the per-cluster audit + remediation log automatically. Built out
incrementally — each cluster, taken in complexity order, adds whatever handler it is
the first to require. The orchestrator is the package; the handlers are its parts.

## The command

```
python scripts/_remediate_cluster_v1_20260602.py --cluster CODE [--apply] [--close]
```

- **default DRY-RUN** — audits, dispatches every handler in dry-run, reports the plan;
  writes nothing.
- `--apply` — runs the mechanical handlers live and applies any present spec files.
- `--close` — after a clean re-audit, calls `_close_cluster_analysis_v1 --apply`.
- Always (re)writes the per-cluster audit + a remediation log into the cluster folder.

## The loop it runs (identical for every cluster)

```
1. AUDIT      import audit_cluster(); snapshot the failing aspects        (baseline)
2. DISPATCH   for each failing aspect, in canonical order A→D:
                 - MECH/auto handler  -> run inline (no content decision)
                 - SPEC handler       -> if the cluster's spec file exists, apply it;
                                         else emit a worklist/template and mark the
                                         aspect REQUIRES-INPUT (halt that aspect only)
3. RE-AUDIT   import audit_cluster() again; record which aspects flipped PASS
4. REPORT     write per-cluster audit + remediation log (baseline, handlers run,
                 results, residuals, verdict)
5. CLOSE      if gate-clean AND --close -> _close_cluster_analysis_v1 --apply
```

**Core principle — mechanical runs, analytical surfaces.** Handlers that are
deterministic (re-derive from existing data) run automatically. Handlers that need a
*content decision* (which flag to set aside, which finding to extend, which finding a
pointer is adopted into) NEVER guess: the orchestrator emits the per-aspect worklist
as a spec template and stops on that aspect, for the researcher/CC to fill, then
re-run. This is "surface, don't perform" + "no fabrication" enforced structurally.
The auditor is the acceptance test — an aspect is "done" only when the re-audit flips.

## Handler registry (aspect → handler)

| Aspect (fail) | Handler | Type | Script | Status |
|---|---|---|---|---|
| **B6 / B7** citations | citation extractor (re-derives `finding_citation` from text) | MECH/auto | `_extract_finding_citations_v1_20260525.py --cluster CODE --live` | **have** |
| **B7** residual (genuinely-uncited anchor) | finding-text citation extension | SPEC | `_apply_finding_citation_extension_v1_20260602.py` | **have** |
| **A6 / A7** gating flags / stray SB | pointer/finding dispositions (set_aside / resolve / fold) | SPEC | `_apply_pointer_dispositions_v1_20260601.py` | **have** |
| **D2** unallocated pointers | pointer-adoption (adopt flag into a finding + xref + close) | SPEC | `_apply_pointer_adoption_v1_…` | **TO BUILD (M38)** |
| **A2** nonsense/gap (advisory) | review — recorded no-op (false positives) | DISP/no-op | (handled in dispositions file as `review`) | **have** |
| **A4 / A5** BOUNDARY | boundary disposition (set-aside / route / promote) | SPEC | `_apply_boundary_disposition_v1_…` | to build (first heavy cluster: M06/M15) |
| **B1a / B1b** meanings / keywords | Phase-A re-run (meaning+keyword emission) package | SPEC/AI | `_apply_phasea_backfill_v1_…` | to build (M08/M09 force it) |
| **B2** grouping | assign subgroup+group to ungrouped is_relevant | SPEC | `_apply_grouping_v1_…` | to build (M20) |
| **B3** char links | link unlinked sub-group → characteristic | SPEC→MECH | `_apply_char_subgroup_link_v1_…` | to build |
| **B5** VCG anchor | designate ≥1 anchor per anchorless VCG | SPEC | `_apply_vcg_anchor_v1_…` | to build |
| **C1** old-format VCG dissolution | mechanical soft-delete of inherited VCGs (v2_9+ Phase 8) | MECH/auto | confirm existing Phase-8 script | to confirm |
| **D1** new terms to place | differential placement + Phase A–D for new terms | SPEC/AI | `_apply_term_placement_v1_…` | to build |

## Build-out roadmap (complexity order)

| # | Cluster | Gate fails | First requires (new build) | Reuses |
|--:|---|--:|---|---|
| ✅ | M10c | (closed) | — (extractor, dispositions) | — |
| ✅ | M10b | (closed) | citation-extension applier | extractor, dispositions |
| **→** | **M38** | **3** (A6,A7,B7;+B6) | **orchestrator skeleton + D2 pointer-adoption** | extractor, dispositions, extension |
| | M08 | 4 | B1a/B1b Phase-A backfill | + orchestrator |
| | M09 | 4 | — (reuses) | all above |
| | M20 | 4 | B2 grouping, C1 dissolution, D1 placement | all above |
| | M07 | 5 | B3 char-link | all above |
| | M01, M02 | 5 | A5 boundary disposition | all above |
| | M10, M03, M04, M06, M15, M26, M39, M46 | 5–7 | (mostly reuse; M06/M15 boundary; heavy B1b) | all above |

Each row is one cluster through the orchestrator; the "first requires" column is the
only *new* code that row forces. By M20 the orchestrator dispatches the full set.

## Packaged outputs (per cluster, automatic)

- `Sessions/Session_Clusters/{CODE}/wa-cluster-{CODE}-audit-v1-{date}.md` — re-audit.
- `Sessions/Session_Clusters/{CODE}/wa-cluster-{CODE}-remediation-log-v1-{date}.md` —
  baseline → handlers run → results → residuals (REQUIRES-INPUT) → verdict.
- Any spec templates the orchestrator emitted for REQUIRES-INPUT aspects.

## Next step (M38)

1. Build the orchestrator skeleton dispatching the 3 existing handlers + emitting
   templates for A6/A7 (dispositions) and D2 (adoption).
2. Run it dry on M38: extractor clears B6 and collapses B7 (45 → small residual);
   A6/A7/D2 surface as REQUIRES-INPUT with templates.
3. Build the **D2 pointer-adoption** applier (4 items on M38 — small first instance).
4. Fill the A6/A7 dispositions + D2 adoption specs (content evaluation, CC), apply,
   re-audit, close. M38 becomes the 3rd cluster through the loop and the first to run
   on the packaged orchestrator.
```
