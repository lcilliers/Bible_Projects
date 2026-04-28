# wa-prose-draft-029-validation-standard-v1-20260421

> Framework B Soul Word Analysis Programme — Draft Prose Body
> Target section_type_id: 29 (`prog_validation_standard`)
> Target label: Programme — Document Validation Standard
> Session reference: prose
> Session date: 2026-04-21
> Previous output: wa-prose-records-list-v1-20260421
> Governed by: wa-directive-instruction-v1_2-20260421 §10.4 (post-directive PROSE patch pattern); wa-patch-instruction-v2_3-20260421 §3

---

## Change Control — v1

| Change | Section |
|---|---|
| New document. First-pass draft of the `prog_validation_standard` prose body, authored from memory per researcher direction in message 4 of session `prose`. Confidence markers applied inline. | All |

---

## Drafting notes — read first

This draft is authored **from memory**. Per researcher direction (session `prose`, message 4), the wa-reference document is retired; the prose bodies must consolidate its content. This first pass is my memory of the validation standard's substance, with confidence markers so the researcher can identify where gaps or reconstructions need source verification.

Confidence markers used:
- **[M]** — confident from memory; operational use in the programme is remembered.
- **[M?]** — partially reconstructed; the content is plausible but I would want source verification before finalising.
- **[GAP]** — I know something belongs here but cannot recall it specifically; source needed to complete.

The draft below is the proposed body text for the `prose_section` row. Heading, word count, and metadata for the PROSE patch are in the §Patch record envelope section at the end.

---

## Proposed heading

`Document Validation Standard`

---

## Proposed body (draft v1 — memory-first)

### What this standard governs

Every document produced in the programme — instruction, extract, directive, patch, observations log, session log, analytical brief, prose body — reaches points at which its completeness matters. These points are called **inflection points**. An inflection point is a handover: a document passes from one activity to another, one session to another, or one pair of hands (researcher, Claude AI, Claude Code) to another. The validation standard specifies what completeness means at an inflection point, how gaps are treated when completeness cannot be achieved, how consistency across documents is maintained, and how patches are gated before application. **[M]**

### Inflection-point completeness

A document is not validated as "finished"; it is validated as **complete at its current inflection point**. Completeness is relative to what the next activity requires, not to some absolute end-state. The same document may be complete for handover to Session B analysis and incomplete for Session C publication — and both judgements are correct. **[M]**

The completeness test at an inflection point is a specific list of questions the document must be able to answer. If the document answers them, it has passed the inflection point. If it does not, it has failed — and the gap is recorded as described below. **[M]**

*[GAP — wa-reference §18 likely specified a named list of inflection points by document type (e.g. Session A extract at handover to Verse Context; Verse Context batch at handover to Dimension Review; Dimension Review output at handover to Session B; Session B brief at handover to Session C). I recall the framing but cannot reconstruct the enumeration. Source needed.]*

### Gap status discipline

A gap is a known incompleteness. It has a status; it does not hide. Every gap encountered in a document — content missing, source to be supplied, decision pending, question awaiting researcher direction — is named explicitly and tagged with a status drawn from a controlled set. **[M]**

The controlled set of gap statuses covers at minimum:

- **Open** — the gap exists, no work has yet been done on it.
- **Under review** — work is in progress; a decision or source is expected.
- **Accepted as-is** — the gap is known and the researcher has decided not to close it at this inflection point; the document passes despite it.
- **Resolved** — the gap has been closed; the content is in place. (A gap marked resolved is not deleted from the trail — the history of what was once open remains in the observations log for audit.) **[M]**

*[M? — I am confident "Open", "Under review", "Resolved" are the operational statuses. "Accepted as-is" is my reconstruction of how deliberate-non-closure was handled; the exact label may differ. Source needed.]*

A document containing an unstated gap — content missing without acknowledgement — has not passed validation, even if every other completeness test is met. Unstated gaps are the failure mode the discipline exists to prevent: they produce confident-looking documents with invisible holes. **[M]**

### Cross-document consistency

Programme documents reference each other. An instruction cites global rules; a patch cites the instruction under which it was produced; an extract cites its source-of-truth table. When any referenced document is updated, every document that cites it is at risk of drift. **[M]**

The cross-document consistency standard has two components:

1. **Pointer-not-copy discipline** — operational cross-references use the `[current]` token (GR-REF-002) rather than a pinned version. This means a document citing `wa-patch-instruction [current]` reads the current version automatically; no stale pin needs maintenance. Provenance references — citing the exact version that produced a patch or a decision — continue to use a pinned version (e.g. `produced_by: wa-sessionb-analysis-readiness-v1_6`). **[M]**

2. **Change-control propagation** — when a governing document is versioned, its dependants are reviewed. A document that cites an updated governing rule is examined for consistency, not silently assumed to still comply. Drift that would have been invisible becomes visible through the review. **[M]**

*[GAP — wa-reference §18 likely specified concrete review triggers (e.g. when global rules increment, review all instructions citing the touched rule; when an instruction increments its major version, review all extracts produced under the prior major). I recall the principle, not the exact triggers. Source needed.]*

### Dry-run gate (patch self-check)

No patch is applied to the database without passing self-check first. This is the operational face of the validation standard at the most consequential inflection point — the moment before a DB mutation. **[M]**

Self-check is specified in wa-patch-instruction [current] §7 and carries forward the same principle: the patch is validated against the standard before it is presented for researcher approval, not after. Self-check covers at minimum: filename pattern compliance (GR-FILE-007, GR-FILE-009); `_patch_meta` required fields per patch type; `session_b_status` correct for the patch type (§3.4); `total_operations` matches `operations.length`; each operation well-formed per its type; patch-specific validation (e.g. coverage, anchor integrity, R1–R4 rules for PREANALYSIS and SESSIONB patches). **[M]**

The term **dry-run** refers to the self-check running as a simulation before the applicator touches the DB — the patch is validated as if it were to be applied, without the actual application. If the dry-run fails any check, the patch does not proceed to researcher approval; Claude AI corrects and re-runs self-check. **[M?]**

*[M? — I am confident about the self-check mechanics. The specific term "dry-run gate" is something I associate with wa-reference §18 but I am not certain it was the exact phrase used. If the source used a different term, substitute.]*

### The standard as cultural, not merely procedural

The validation standard exists because the programme's outputs compound. An error at one inflection point propagates forward — a missing gap in a Session A extract reappears as a confident but wrong count in a Session B brief, and as a published inaccuracy in a Session C word study. The discipline is not bureaucracy; it is the mechanism by which the programme's integrity is preserved across thousands of handovers between activities, sessions, and documents. **[M]**

The standard applies to every document type without exception. Sessions end with session logs; session logs are validated. Patches carry self-checks; self-checks are validated. Even this prose record will be validated at its inflection point — insertion into `prose_section` — via the completion confirmation queries of the underlying directive and the applicator validation of the PROSE patch. The discipline is recursive. **[M]**

---

## Body word count (approximate)

Approximately 720 words excluding headings. `word_count` field on the `prose_section` row will be calculated by the PROSE patch applicator or supplied in the patch record (`word_count: 720` — to be validated at patch time).

---

## Confidence summary for researcher

| Marker | Count | Note |
|---|---|---|
| [M] | 13 sentences/clauses | Confident from memory |
| [M?] | 3 sentences/clauses | Partially reconstructed — verification recommended |
| [GAP] | 2 substantive gaps | Source needed to close |

The two [GAP] items are:
1. Named list of inflection points by document type (under "Inflection-point completeness").
2. Concrete review triggers for change-control propagation (under "Cross-document consistency").

Both can be closed by access to the retired wa-reference §18, or by researcher description.

---

## Patch record envelope (for PROSE patch construction — after body approval)

This section is not part of the prose body. It captures the fields needed when the PROSE patch is constructed, per wa-patch-instruction-v2_3 §3 and v1_2 directive §10.4.

| Field | Value |
|---|---|
| `table` | `prose_section` |
| `operation` | `insert` |
| `registry_id` | `null` (requires schema enablement directive applied first) |
| `section_type_id` | `29` (from extract; `prog_validation_standard`) |
| `heading` | `Document Validation Standard` |
| `body` | (approved body text from §Proposed body above) |
| `word_count` | (calculated from approved body) |
| `status` | `draft` |
| `version` | `1` |
| `author` | `claude_ai` |
| `source_file` | `wa-prose-draft-029-validation-standard-v1-20260421.md` |
| `metadata_json` | `{"confidence_markers": true, "gaps": 2, "reconstructions": 3}` (optional — aids audit) |

---

## What the researcher needs to decide

1. **Body approved as-is / with edits / rejected.** Edits can be tracked by appending a v2 of this draft file with change notes.
2. **Close the two [GAP]s** — either supply wa-reference §18 content, or describe the missing content, or accept the prose as-is with a note in `metadata_json`.
3. **Confirm the three [M?] reconstructions** — either validate the reconstructed labels and term (particularly "Accepted as-is" status label and "dry-run gate" term), or correct them.
4. **Authorship decision — one record per type or split.** My judgement: one record. Split only if the body becomes unwieldy, which at ~720 words it is not. Proceed unless overridden.

---

*wa-prose-draft-029-validation-standard-v1-20260421 | First draft, memory-first per session `prose` message 4*
