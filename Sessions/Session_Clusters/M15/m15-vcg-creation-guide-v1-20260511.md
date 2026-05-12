# Verse Context Group (VCG) creation — coherent guide

**Compiled:** 2026-05-11
**Source documents (current + lineage):**
- `Workflow/Instructions/wa-versecontext-instruction-v3_10-20260425.md` (current authoritative)
- `Workflow/archive/wa-versecontext-instruction-v3_9-20260425.md`
- `archive/Sessions/wa-versecontext-instruction-v3_5-20260424.md`
- `archive/Sessions/wa-versecontext-instruction-v3_0-20260424.md`
- `archive/Sessions/wa-versecontext-instruction-v2_8-20260418.md` (Session B restructure baseline)
- `archive/Sessions/wa-versecontext-instruction-v2.6-20260414.md` (earliest available)

The core criteria for creating a VCG have been **materially stable from v2.6 (2026-04-14) through v3_10 (2026-04-25)**. What evolved was infrastructure (batch JSON → per-term `.md`), re-evaluation discipline, and the v3_10 cluster-treatment allowance. The grouping logic itself is unchanged. This guide consolidates that stable core.

---

## 1. What a VCG is (the semantic definition)

A `verse_context_group` is a set of verses for **one term** where the verses share the same **inner-being engagement through that term**.

A VCG is NOT:
- Verses where the term simply repeats
- Verses that share a thematic context (the same story, the same book)
- Verses that share an English translation
- Verses that share a syntactic role

A VCG IS:
- Verses where the term engages **the same inner-being characteristic** (or the same characteristic in the same role / orientation / register)

The `context_description` field on each VCG is the single-sentence statement of that shared engagement.

---

## 2. The governing filter — gate for any verse to be classifiable at all

Before grouping can happen, each verse must pass the inner-being filter:

> **"Does this verse, through the use of this term, say something about the inner being — understood as the non-physical, internal states, capacities, and expressions that constitute a person's invisible life: how a person thinks, feels, chooses, relates, and orients themselves toward meaning, others, and God?"**

**What passes:**
- Internal states (emotion, feeling, disposition, attitude)
- Capacities of the inner life (will, intention, thought, belief, desire)
- Relational orientation toward God, others, or self inwardly
- Moral or character quality of the whole person
- Spiritual characteristic (responsiveness to God, spiritual condition, worship disposition)

**What does NOT pass (and is set aside, not grouped):**
- Purely physical use of the term
- Purely social or external narrative conduct with no window into inner life
- Purely positional / geographical
- "Wrong face" — inner-being content present but carried by a different term, not this one

---

## 3. The characteristic-perspective principle (the heart of the guide)

> **Groups must be formed from the perspective of the inner-being characteristic the verse cluster is primarily about — NOT from the perspective of what the term does.**
>
> _(unchanged v2.6 → v3_10)_

### The two-type distinction

| Type | Definition | Example |
|---|---|---|
| **Characteristic term** | Names an inner-being state directly | *lev* (heart) — the seat itself |
| **Property term** | Describes how a characteristic operates | *sha.ma* (to hear/listen) — a function |

**For property terms especially**, the group description must name the **characteristic being served**, not the term's function.

Worked example (verbatim from the instruction):
- Term: *sha.ma* (hear/listen) appearing in Israel's refusal to hear the prophets
- ❌ Term-centric (WRONG): "refusing to hear God"
- ✅ Characteristic-perspective (CORRECT): "heart-stubbornness expressed through refusal of God's word"

The same property term can serve different characteristics, or the same characteristic in opposite ways. The verse — and the verses it joins — determine which.

---

## 4. The grouping criterion — when a NEW group is warranted

For each verse, the core question:

> **"Does this verse engage the same inner-being characteristic through this term as verses already assigned to a group?"**

- **YES** → assign to that existing group
- **NO** → first check whether any other existing group fits; **only create a new group if no existing group fits**

A new group is warranted when:

> **The inner-being characteristic being engaged is materially different from all existing groups, OR the same characteristic is engaged in a materially different way.**

"Materially different" means the three-factor test:

1. **Different characteristic** — a different inner-being characteristic is the primary subject
2. **Different role for the same characteristic** — term serves the same characteristic but in a distinguishably different role (seat vs. channel vs. expression vs. mechanism vs. obstacle vs. counterpart)
3. **Different orientation / register for the same characteristic** — toward God vs. against God; positive vs. negative; received vs. rejected

Minor variations in emphasis, tone, or wording within the same essential engagement do **NOT** warrant a new group.

**Consolidation heuristic** _(v2.6 onward)_:

> Where 5+ groups emerge for a single term, pause and assess whether consolidation better serves the criterion before adding further groups.

---

## 5. The `context_description` — one sentence, four requirements

Every VCG carries a `context_description` (max one sentence) that must:

1. **Name the inner-being characteristic** the verses primarily engage
2. **State the term's role accurately** relative to that characteristic (seat, expression, channel, mechanism, obstacle, counterpart…)
3. **Be grounded in what the verses show** — not in prior theological knowledge or lexical assumption
4. **Be sufficient to distinguish** this group from other groups for the same term

Well-formed examples (verbatim from instruction):

- _Term names the inner seat of the emotion of fear_
- _Term serves as the channel through which faith arrives_
- _Term expresses the stubbornness of the heart_
- _Term names the cognitive capacity of the inner person_

Failure modes a `context_description` falls into when ignored:

- Describes what the **term** does, not the characteristic engaged (term-centric drift)
- Is so broad it does not distinguish this group from another for the same term
- Imports theological framing not visible in the verses themselves

---

## 6. Anchor verses — minimum coverage

- Every group must have **at least one** active anchor verse (hard gate — `R4`, enforced by Claude Code; absolute blocker for Session B).
- 1 to 2 anchors per group is the norm; never more than 2 unless the second adds something the first does not.
- An anchor verse must:
  - Make the contextual meaning **evident without surrounding context**
  - Show the term's inner-being function **unambiguously**
  - Stand alone as evidence

Anchor verses serve two roles:
- **Efficiency** — Session B and Session D read anchors, not the full corpus; VC reduces ~133k verses to a small anchor set
- **Citation** — anchors are quoted as the evidential foundation in Session B/D narratives

---

## 7. Dual-context verses — the only legitimate doubling

A single verse may appear in two VCGs **for the same term** only when it plainly operates at two distinct inner-being levels through that term. This is the **exception, not the norm**.

When it happens:
- Two `verse_context` rows are created (the UNIQUE constraint is `(verse_record_id, mti_term_id, group_id)` — same verse permitted in two different groups, never twice in the same group)
- The reason for dual-context is recorded in the `notes` field on **both** rows

---

## 8. Cluster-treatment discipline (added in v3_10, only allowance from individual classification)

For **homogeneous blocks** where every verse uses the term in the same way (same syntactic role, semantic content, filter outcome), cluster-level reasoning is permitted **under bounded conditions**:

1. **Read every verse individually first** — homogeneity must be confirmed, not assumed
2. **Document the homogeneity finding** — which verses, what they share, the shared reasoning
3. **Each verse still gets its own `verse_context` row** — same `group_id` or `set_aside_reason`, but the row is per-verse
4. **Any verse departing from the cluster pattern receives individual treatment**

**Permitted contexts:** sacrificial/cultic formulae, epistolary/liturgical formulae, legal-categorical lists, idiomatic merism.

**Not permitted contexts:** wisdom or prophetic uses, verses with varying inner-being weight, heterogeneous narrative, any block without confirmed homogeneity.

---

## 9. Database structure (so the criteria connect to the data)

- `verse_context_group` — one row per group per term. Key fields:
  - `id` (PK; what joins point at)
  - `mti_term_id` (the term this group belongs to)
  - `group_code` — human-readable `{mti_term_id}-{serial}` (e.g. `911-003`), **never a join key**
  - `context_description` — the single-sentence statement of inner-being engagement
- `verse_context` — one row per (verse, term, group) link. UNIQUE on `(verse_record_id, mti_term_id, group_id)`.
- `mti_term_subgroup` — assigns the **term** (not the verse) to one or more cluster sub-groups (M15-A, M15-B, …). Sub-group assignment is term-level structural placement; VCG assignment is verse-level analytical grouping.

So a verse's sub-group is **inherited from its term's `mti_term_subgroup` row(s)**, and its VCG is determined by the per-verse analytical judgment.

---

## 10. Through-line — what is stable and what is variable

**Stable from v2.6 → v3_10:**
- Characteristic-perspective principle (§3)
- Three-factor "materially different" test (§4)
- One-sentence `context_description` with four requirements (§5)
- Minimum-one-anchor rule (§6)
- Dual-context as exception (§7)
- The five-group consolidation heuristic

**Evolved across versions:**
- v2.6 → v2.8: integration with global rules
- v2.8 → v3_0: input shifted from batch JSON to per-term `.md`; re-evaluation posture and orphan-group checks formalised
- v3_0 → v3_5: per-verse `insert` vs `update` row-generation rule clarified; absence-of-row treated as meaningful (not equivalent to set-aside)
- v3_9 → v3_10: cluster-treatment discipline added (§8) — the only addition that materially expands the grouping toolkit

**Vague by design (across all versions):**
- "Materially different" — never given a formulaic test. Requires expert judgment: read the verses, compare against existing groups, decide whether the characteristic engagement differs materially.

---

## 11. Diagnostic — likely failure modes when AI drifts

When AI re-derives VCGs and **leans toward the existing VCG structure rather than the verse content** (the pattern observed in M15), the likely root causes are:

1. **Term-centric grouping** — AI groups by what the term does (translation pattern, syntactic role) rather than by the characteristic engaged. Violates §3. Detectable in `context_description` that reads like a lexicon entry ("term means X, used for Y") rather than a characteristic statement ("X-characteristic engaged as Y-role").

2. **Group-count anchoring** — AI sees N existing groups and produces ~N new ones, even when the verse content would warrant consolidation or further splitting. The consolidation heuristic (§4) is meant to push against over-splitting; there is no parallel anti-anchoring rule against matching the existing count.

3. **Code-label inheritance** — AI sees existing group codes (`528-001`, `911-003`) and uses their existing semantic shape as scaffolding, even when re-doing the work. The new VCG label-naming (`VCG-A-01`) inherits the existing structure rather than starting from the verses.

4. **Implicit theological priors** — AI imports systematic-theological categories not visible in the verses themselves. Violates the "grounded in what the verses show" requirement in §5.

**To force re-derivation from the verses:** strip every existing VCG identifier and description from the input given to AI, leaving only verse text, term span, and (optionally) a prior verse-level meaning. The clean-slate JSON ([m15-clean-slate-v1-20260511.json](m15-clean-slate-v1-20260511.json)) does exactly this.

---

*Compiled from the wa-versecontext-instruction lineage (v2.6 → v3_10) plus cross-checks against wa-registry-management-guide v5_10, wa-sessionb-analysis-readiness v1_10, and wa-claudecode-instruction v4_4. Where verbatim quotation appears it is drawn from v3_10.*
