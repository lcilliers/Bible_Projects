# Prose Edit — Programme — Chapter 5

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 36 -->
<!-- PROSE_SECTION_TYPE: prog_patch_failure_protocol -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Patch and directive failure protocol -->
<!-- PROSE_SORT_ORDER: 108 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose_ch5-obslog-v1_0-20260423.md -->

## Patch and directive failure protocol

Patches and directives are the two channels by which changes reach the database. The two-AI division, described in the sub-section of Chapter 3, sets out how a patch or directive is authored, reviewed, and applied under normal conditions. The failure protocol describes what happens when a patch or directive does not apply cleanly.

Three failure modes the protocol covers: **rejection**, where the operational agent declines to apply a patch because it violates a schema constraint or a controlled-vocabulary check; **mid-pool failure**, where a batch of rows is being applied and a row fails partway through, leaving the pool in a partially-applied state; and **post-application error**, where the patch applied cleanly but the result is wrong on analytical review and must be reversed.

**Rejection.** A patch that violates a constraint — an off-vocabulary dimension label, a foreign-key miss, a missing required field — does not enter the database. The operational agent returns the rejection with the constraint that failed. The patch is revised or withdrawn; the database state is unchanged; the obslog records the rejection and the revision. No partial effect is produced.

**Mid-pool failure.** Batch operations that apply many rows as a single transactional pool are subject to mid-pool failure: the pool begins to apply, a row partway through fails a constraint, and the transaction is rolled back or committed partially. The discipline is that pool applications are atomic — either every row applies or none does. A pool that cannot be atomic is split into smaller atomic units. Recovery from a partial application is through backup restoration of the affected rows, not through ad-hoc correction of the rows that succeeded while the rest failed.

**Post-application error.** A patch that applied cleanly but is found on review to have recorded the wrong analytical content is reversed through a second patch — a failure patch that supersedes the first, preserving the history through the supersede chain rather than overwriting the original record. For row-level analytical content, the soft-delete discipline and the supersede-only lifecycle described elsewhere in this chapter do the reversal work: the first patch's rows are marked superseded or delete-flagged, the correcting patch's rows are applied, and the audit trail carries both.

The protocol's governing principle is that no failure leaves the database in an inconsistent state. Rejection changes nothing. Mid-pool failure restores to the last known good state. Post-application error is reversed through a second reviewed patch, and both patches are preserved in the history. The cost of maintaining this discipline is higher than the cost of accepting ad-hoc fixes in the short term, and lower than the cost of a database whose current state cannot be trusted to reflect a sound sequence of reviewed changes.

---
