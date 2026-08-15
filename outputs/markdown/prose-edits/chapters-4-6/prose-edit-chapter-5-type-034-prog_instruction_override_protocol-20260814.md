# Prose Edit — Programme — Chapter 5

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 37 -->
<!-- PROSE_SECTION_TYPE: prog_instruction_override_protocol -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Instruction override and cross-document reference discipline -->
<!-- PROSE_SORT_ORDER: 109 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose_ch5-obslog-v1_0-20260423.md -->

## Instruction override and cross-document reference discipline

The programme's instruction corpus — global rules, instruction documents, and the prose that describes the programme — evolves over the life of the work. Rules are added; instructions are revised; documents supersede prior versions. Two disciplines keep the corpus consistent under this evolution: the instruction override protocol, which governs how researcher direction reaches the rule set; and the cross-document reference discipline, which governs how pointers between documents stay valid as the documents are revised.

**Instruction override.** The researcher's in-session direction is authoritative. When the researcher corrects a rule's application, adjusts a procedure, or issues a direction that differs from what an instruction document currently says, the direction takes immediate effect for the session it is issued in, regardless of whether the rule file has been updated to reflect it. Researcher authority does not wait on document revision; it propagates into the rule set through a defined sequence.

The sequence runs through four places. The direction is first captured in the **observations log** of the session it is issued in — verbatim, at the moment it is received, as the obslog discipline requires. It appears again in the **session log** as part of the closing state — the override is carried across the session boundary as an explicit item the next session needs to know about. From the session log, the override is authored into a change to the **rule registry** (`wa_rule_registry` for direct rule amendments) or the **addendum registry** (`wa_addendum_registry` for annotations, migrations in progress, or items that modify how an existing rule applies) as a patch or directive through the operational agent. Once the registry change is applied and the extract regenerated, the override is retired from its temporary status: it is no longer an override, it is the rule.

The `migration_status` field on the addendum registry carries the in-flight state — an addendum recorded but not yet migrated into a rule is governance in transition. An addendum whose migration is complete is reflected in the rule text itself, and the addendum may be marked obsolete through `obsolete` and `obsolete_reason` so the retirement is visible in the audit trail. The principle: no override stays an override indefinitely. Either it is absorbed into the rule set, or it is withdrawn, or it remains open as an acknowledged addendum until the next opportunity for absorption.

**Cross-document reference discipline.** Documents in the programme refer to other documents — rules cite other rules; instructions cite global rules and other instructions; prose cites instructions, schema, and earlier prose. The discipline that keeps these references valid under revision rests on five sub-disciplines set out in the global rules.

*Pointer, not copy.* When document A needs content owned by document B, A references B with a pointer — document name, version or `[current]` token, section number — and does not re-state B's content inline. The re-statement creates duplication; duplication drifts; drift produces the inconsistencies the discipline exists to prevent.

*Versioned references.* Cross-references carry either a specific version string (for provenance — Supersedes fields, obslog entries, patch metadata) or the `[current]` token (for operational references that should self-resolve to the latest version available). Un-versioned references are the primary mechanism by which stale pointers accumulate and are not permitted.

*Single authoritative document per content type.* Each content type has exactly one owning document. The content-authority map — controlled vocabulary to `wa-reference`; schema to `wa-reference`; file-naming conventions to global rules; patch format to `wa-patch-instruction`; directive format to `wa-directive-instruction`; operational routines for the operational agent to `wa-claudecode-instruction` — is authoritative. Content that cannot be assigned to an owning document is the signal that either a new document is needed or the content does not belong in the programme.

*Consistency check at version bumps.* When a document bumps its version, the documents that reference it are checked for staleness: a search for the old version string surfaces every reference that needs updating. The check is a named step in the version-bump workflow and is the authoring responsibility of the author producing the bump.

*Documents stay within their named content type.* Each document's scope is explicitly named in its opening section. Content that belongs to another document's scope is moved or replaced with a pointer. Creep — drift of content out of a document's named scope — is the authorship failure mode that the discipline actively resists.

**The `[current]` convention.** Operational cross-references between instruction documents use a `[current]` token that resolves to the highest-numbered version present in the project's primary workspace at the time the referring document is read. The token inverts the staleness-detection mechanism: references self-resolve against current state rather than requiring every referring document to be updated at every routine version bump of every target document. Specific version strings are reserved for the provenance trail — Supersedes fields, obslog entries, patch `_patch_meta.produced_by` fields, change-control notes, external references to archived versions.

The two disciplines together describe how the instruction corpus stays consistent: overrides reach the rules through a traceable sequence; references between documents stay valid through pointers, versioning, single authority, and consistency checks. Neither is a one-time exercise; both are the ongoing authorship pattern the programme follows every time a rule changes or a document is revised.

---
