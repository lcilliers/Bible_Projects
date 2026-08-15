# Prose Edit — Programme — Chapter 5

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 38 -->
<!-- PROSE_SECTION_TYPE: prog_doc_impl_alignment -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Documentation–implementation alignment -->
<!-- PROSE_SORT_ORDER: 110 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose_ch5-obslog-v1_0-20260423.md -->

## Documentation–implementation alignment

The programme's rules, its database schema, its instruction documents, and the prose that describes the work are four surfaces that must stay in alignment for the record to be trustworthy. The alignment is not a state the programme can declare once and rely on thereafter. Rules are added; schema evolves through migrations; instructions are revised; documentation catches up, sometimes after a lag. At any moment, small mismatches between these surfaces are present — a rule that names a field the schema has since renamed, a slot description that references a concept the instructions have moved past, a schema column whose authority has not been explicitly ruled on. The standing governance principle is that these mismatches are named, not hidden.

Two kinds of mismatch illustrate the shape.

**Rule-to-schema audit gaps.** The field-authority rules (sub-section on record consistency with sources) name two fields as authoritative against their redundant equivalents: `mti_term_flags` for somatic classification, with `wa_term_inventory.somatic_link` as deprecated; and `god_as_subject` as error-prone and verification-required. The programme's schema carries other overlapping fields whose authority has not been explicitly ruled on. The question — which field wins when two hold the same information — is sound in principle; the answer for every overlapping case is not fully documented. The gap is a governance item, not a defect of the rules already in force.

**Documentation-to-documentation drift.** The prose corpus and its governing instruction documents are authored in parallel over sessions spanning months. A prose_section_type description may name a concept ("dry-run gate assessment" was one such case at the time this chapter was drafted) that is not grounded in the instruction corpus — either because the concept was proposed and not documented, or because it was documented in an earlier version and did not survive into current practice. When the drift is noticed, it is resolved by one of three routes: the concept is traced to documentation that exists but had not been read at the time of the observation, and the prose is corrected to cite it; the concept is retired from the referring document because no supporting documentation exists; or the concept is documented forward, so that the referring document becomes grounded.

The three routes generalise to the standing mechanism. Where a mismatch between surfaces is detected, the question asked is not "which surface is right?" but "which resolution route is warranted here?" A rule that names a field the schema has renamed resolves by either renaming the field back through a migration or amending the rule to match the schema's current name. A slot description that references an absent concept resolves by editing the description or by documenting the concept. A prose passage that describes an operational mechanism that the instruction corpus does not document resolves by either adding the instruction or revising the prose. The resolution is explicit; it is recorded in the obslog; the surfaces come back into alignment through a traceable change on one side or the other.

The principle's reverse is what it rules out. The programme does not tolerate silent drift: a rule that is contradicted by the schema is not left unreconciled on the assumption that both sides will correct over time; a slot description whose vocabulary is not grounded is not quietly ignored. The mismatch is the governance surface — the point at which the programme's self-description meets its actual state — and keeping the surfaces aligned is the discipline that makes the programme's audit trail mean what it claims to mean.

Two specific governance items stand open at the time this chapter was drafted: the per-field audit of authority status across the schema, and the review of slot descriptions and rule text for vocabulary not grounded in current documentation. Both are named as follow-up work. The alignment principle is the basis on which they will be resolved when the work is scheduled.

---
