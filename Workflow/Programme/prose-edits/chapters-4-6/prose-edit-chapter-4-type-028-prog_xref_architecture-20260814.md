# Prose Edit — Programme — Chapter 4

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 25 -->
<!-- PROSE_SECTION_TYPE: prog_xref_architecture -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: Ownership and cross-registry references -->
<!-- PROSE_SORT_ORDER: 25 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose-ch4-obslog-v1_0-20260423.md -->

## Ownership and cross-registry references

Inner-being vocabulary overlaps across registry words. The Hebrew *nephesh* is lexically relevant to soul, self, life, and desire. The Greek *pneuma* is relevant to spirit, breath, and mind. The programme handles this overlap through a single architectural rule — one term, one owning registry — and a companion mechanism that records the term's relevance to other registries without duplicating its classification.

Every Strong's number in the programme has exactly one OWNER registry. That registry is the term's analytical home — the place where its verses are extracted and kept active, where its verse contexts are classified, where its context groups are formed, and where its dimension-index entries live. The OWNER/XREF status of a term is carried in `wa_term_inventory.term_owner_type`, which takes the value `OWNER` or `XREF` for every inventory row.

A term may also appear as an XREF in one or more other registries. An XREF row in a registry signals that the term has analytical relevance to that registry, but does not make the term the registry's property. The verses associated with an XREF term are held with `wa_verse_records.delete_flagged = 1` — they are present in the database for completeness, but they are not the active verse set for the registry that carries the XREF. Classification, grouping, and dimension analysis are not performed on an XREF row. Session B for an XREF-holding registry accesses the term's analytical content through the OWNER's path, not through the XREF's local rows.

The canonical-row rule follows from this. `mti_terms.owning_registry_fk` points to the OWNER registry, regardless of how many other registries carry XREF rows for the same term. The field answers the question "which registry owns this term"; it does not answer "which registries reference this term". That second question is answered by `mti_term_cross_refs`, which carries one row per cross-registry reference. Each row records the term (`mti_term_id`, with ON DELETE CASCADE back to `mti_terms`), the referenced registry (`registry` and `registry_fk`), the registry's word and part, and a reference pointer to where the cross-reference appears in the programme's file-level record. Four hundred and sixty-two rows currently carry the cross-registry relationships the programme has identified.

The architecture supports a complete case that the simpler designs cannot: the **pure XREF registry** — a registry where every term in the inventory carries `term_owner_type = XREF`. Such a registry owns no terms of its own; its full analytical content is contributed by terms owned in other registries. The programme's registry construction admits these registries as legitimate, and their expected state has zero OWNER terms, zero active verses, zero verse-context groups, zero dimension-index entries, and `verse_context_status = Complete` — none of these zeros is an anomaly. Nine pure XREF registries exist in the current scope: consciousness, loyalty, meekness, recognition, resolve, reverence, sensuality, energy, and resentment.

The anomaly test that distinguishes a pure XREF registry from an actual data gap is simple: a registry with zero OWNER terms and zero XREF terms is a genuine gap requiring investigation, while a registry with zero OWNER terms and some number of XREF terms is a pure XREF registry in its correct state. The OWNER/XREF architecture exists precisely so that this distinction is expressible in the data — the absence of OWNER rows is not, by itself, a signal of incompleteness.

The practical consequence of the architecture is that a term's dimensional and analytical record lives in one place. A finding raised in the OWNER registry's Session B is the finding for that term across the programme; registries that reference the term as XREF inherit the finding through the shared `mti_term_id` path rather than producing a separate one. The programme's answer to the question "what does Scripture say about this term?" is one answer, held in the OWNER's records, referenced by the registries for which the term is relevant.

---
