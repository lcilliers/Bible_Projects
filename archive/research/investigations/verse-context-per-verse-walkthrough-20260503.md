# Verse Context — Per-Verse Walk-through

**Source:** [wa-versecontext-instruction-v3_10-20260425.md](../../Workflow/Instructions/wa-versecontext-instruction-v3_10-20260425.md) (2,178 lines, the operative governing document).

This brief reduces the instruction to its operative answer to your question — *what should happen with each verse?* — with all the discriminations the instruction makes.

---

## The framing rule

**Every active OWNER verse, for every active OWNER term, must produce one explicit `verse_context` row.** No row = not analysed = pending (§3.2b post-M39). The classifier is never allowed to silently skip a verse — even a verse with no inner-being content must produce a set-aside row with a recorded reason.

The atomic unit is the **(mti_term_id, verse_record_id) pair.** That pair determines whether the patch operation is `insert` (no prior row) or `update` (revising existing) — §3.2 v3_5 A-06.

---

## The decision flow per verse

```
                ┌─────────────────────────────────────┐
                │  Read the verse — full ESV text +    │
                │  target_word + span_strong_match     │
                │  + any prior verse_context state     │
                └──────────────────┬───────────────────┘
                                   │
                                   ▼
                ┌─────────────────────────────────────┐
                │  Apply §3 governing filter:          │
                │  Does THIS TERM, in THIS VERSE,      │
                │  engage the inner being?              │
                └──────────────────┬───────────────────┘
                                   │
                ┌──────────────────┴───────────────────┐
                │                                       │
              YES                                     NO
                │                                       │
                ▼                                       ▼
     ┌──────────────────┐                  ┌──────────────────────┐
     │  is_relevant=1   │                  │   is_relevant=0      │
     │                  │                  │   group_id=NULL      │
     │  Group it (§6.2  │                  │   is_anchor=0        │
     │  Step 3)         │                  │   is_related=0       │
     │                  │                  │                      │
     │  Possibly anchor │                  │  set_aside_reason    │
     │  (§4, §6.2 Step 4)│                  │  from controlled     │
     │                  │                  │  vocabulary          │
     │  Possibly dual-  │                  │                      │
     │  context (§6.2   │                  │  Notes if 'wrong_    │
     │  Step 5)         │                  │  face' or 'other'    │
     └──────────────────┘                  └──────────────────────┘
```

---

## Filter rules — what passes (§3.1)

A verse passes when the term's specific use engages one or more of:

- An **internal state** — emotion, feeling, disposition, attitude
- A **capacity of the inner life** — will, intention, thought, belief, desire
- A **relational orientation** — how the person is oriented toward God, others, or themselves inwardly
- A **moral or character quality** of the whole person
- A **spiritual characteristic** — responsiveness to God, spiritual condition, worship disposition

> ⚠ Apply the filter to the term's **specific use in this verse** — not to the verse's general theme. A verse about covenant renewal may use the term in a purely legal sense with no inner-being engagement for this specific term. **Filter at term level, not verse level.**

---

## Filter rules — what doesn't pass (§3.2 + controlled set-aside vocabulary)

| Reason value | Meaning |
|---|---|
| `no_inner_being` | The term carries no inner-being content here. Verse may have inner-being content elsewhere; this term doesn't carry it. |
| `physical_only` | The term names a physical process, body part, or material object. |
| `spatial_only` | The term is locational/geographical. |
| `wrong_face` | Verse has inner-being content but **a different term carries it** (§3.6) — set-aside for this term, but the verse remains analytically relevant elsewhere. |
| `other` | None of the above; `notes` must explain. |

**Mandatory rule:** every `is_relevant=0` row must carry a non-NULL `set_aside_reason` from this vocabulary. Pre-VCB-031 set-asides without a reason are a known programme-wide gap.

---

## Special-case branches in the filter (§3.3–§3.6)

### §3.3 Borderline retention
Where the filter decision is genuinely uncertain → **retain** (`is_relevant=1`) and record the uncertainty in `notes`. Don't stop mid-term; resolve at term-close or session-close.

### §3.4 Expressions as inner-being evidence
Where the term names a human act of expression (cry, call, groan, gesture), the filter is satisfied if the act plausibly originates in an inner state. The inner state need not be named explicitly; the force/character of the expression implies its inner origin.

### §3.5 Grammatical and functional particles
Pronouns, particles, conjunctions, adverbs, etc. require **explicit assessment** of how the particle functions in the specific verse — not merely whether the verse contains inner-being content.

A particle **passes** if it:
- **Directs** inner-being content (interrogative pronouns framing inner-life questions)
- **Intensifies** an inner-being state or act
- **Qualifies the scope** of an inner-being condition
- **Discloses an inner orientation** through how it frames inner-being content

A particle **does not pass** if it is:
- Purely syntactic (grammatical requirement only)
- Social register / politeness
- Temporal connector
- Procedural filler

**The test:** Remove the particle mentally. Does the inner-being content change in how it engages the inner being? If yes → passes. If no → set aside.

### §3.6 Wrong-face set-asides
The verse has genuine inner-being content, but **a different term in the verse carries it** — not the term being classified. Pattern: the term being classified passes the general "is the verse inner-being?" test but fails the specific "does this term carry that content?" test.

**Patch treatment:**
- `is_relevant=0`, `group_id=NULL`
- `set_aside_reason='wrong_face'`
- `notes`: identify the term that carries the content + its registry, e.g. `"wrong_face: inner-being content carried by lev (H3820A, Reg 183)"`

This preserves the cross-registry analytical signal: a future vertical pass / Session B can query `WHERE set_aside_reason = 'wrong_face' AND mti_term_id = ?` to find verses where the term is present but the content lives elsewhere.

### §3.2c Cluster-treatment discipline (added v3_10)
For homogeneous blocks (e.g. 45 sacrificial-formula uses of *ta.mim*; ~30 Pauline thanksgiving openings of *eucharisteō*), **cluster-level reasoning is permitted**, but:

1. **Read every verse in the cluster** — homogeneity must be established by reading, not assumed.
2. **Document the homogeneity finding** before applying it (verse list + shared syntactic role + shared semantic content + shared filter direction).
3. **Each verse still gets its own `verse_context` row** — cluster-treatment governs the *reasoning*, not the row count.
4. **Any verse departing from the cluster pattern gets individual treatment.**

Cluster-treatment is a documentation efficiency, not a coverage shortcut.

---

## If the verse passes — grouping (§6.2 Step 3)

**Question for each relevant verse:** does this verse engage the same inner-being characteristic through this term as verses already assigned to a group?

- Yes → assign to that group
- No → check existing groups first; create a new group only if no existing group fits

### Characteristic-perspective grouping model

Groups are formed from the perspective of the **inner-being characteristic** the verse cluster is primarily about — not from the perspective of what the term does.

- **Characteristic terms** (e.g. *lev* heart, *nephesh* soul, *pistis* faith) — name an inner-being state directly; their groups are naturally characteristic-centred.
- **Property terms** (e.g. *shama* hear/listen, *ozen* ear, *akoē* hearing) — describe how characteristics operate; can serve different characteristics across the term's corpus.

For property terms, the group description must name the **characteristic served**, not just the term's function.

### Well-formed `context_description` (one sentence max)

Names the inner-being characteristic + the term's role (seat / expression / channel / mechanism / obstacle / counterpart):

✓ "Term names the inner seat of the emotion of fear — the place where fear arises and is registered" (characteristic: fear; role: seat)
✓ "Term serves as the channel through which faith arrives — hearing as the mechanism of faith reception" (characteristic: faith; role: channel)
✓ "Term expresses the stubbornness of the heart — refusal to hear as the outward form of inner resistance" (characteristic: stubbornness; role: expression)

Avoid (term-centric):

✗ "Term describes an act of refusing to listen" — names what the term does
✗ "Term is used when God addresses people" — describes context
✗ "Term indicates active, engaged hearing" — describes the term's behaviour

### When a new group is warranted

A new group requires **material difference**:
1. A different inner-being characteristic is the primary subject
2. The term serves the same characteristic in a distinguishably different role (seat vs channel vs expression)
3. The same characteristic appears in a materially different orientation (toward God vs against God; positive vs negative register)

Soft cap: at 5+ groups for a single term, **pause and assess consolidation** before adding more.

---

## If the verse passes — anchor designation (§6.2 Step 4 + §4)

Designate **1–2 anchor verses per group** that meet:

- Make the contextual meaning evident **without requiring surrounding context**
- The term's inner-being function is **unambiguous** in the verse
- **Stand alone as evidence** — does not depend on adjacent passages

**Hard rule (R4):** every term must have at least one active anchor across all its groups before Session B can proceed. Claude Code enforces this in the completion check.

If no clear anchor exists (all verses contextually dependent), designate the **least dependent** one as the anchor and note the limitation. Never leave a group anchorless.

**Quantity:** 1–2 per group. Where two are designated, they represent distinct aspects. Don't designate more than 2 unless a third genuinely adds something.

---

## Dual-context (§6.2 Step 5)

Where a verse plainly operates at **two distinct inner-being levels through the same term**, assign to **two groups** — emit two `verse_context` rows for the same `verse_record_id` + `mti_term_id`, each with a different `group_id`. UNIQUE constraint allows this: `(verse_record_id, mti_term_id, group_id)`.

Record the dual-context reason in `notes` on **both** rows.

This is the exception, not the norm.

---

## Logical consistency rules (§2.3)

Any classification must satisfy:

| Rule | Condition |
|---|---|
| **R1** | `is_relevant=0` → `group_id=NULL`, `is_anchor=0`, `is_related=0` |
| **R2** | `is_anchor=1` → `is_relevant=1`, `is_related=0`, `group_id NOT NULL` |
| **R3** | `is_related=1` → `is_relevant=1`, `group_id` references a group with at least one active anchor |
| **R4** | Every term must have at least one active anchor before Session B may proceed |

Claude Code enforces R1–R4 at patch validation. Violations are pre-submission failures.

---

## Re-evaluation: what's added when prior records exist

When the term has prior `verse_context` records, the classifier declares **RE-EVALUATION posture** and:

1. **Reviews every prior classification** — does not assume correctness
2. **Revises** where clearly warranted (revision criteria in §6.2 Step 2)
3. **Runs the re-evaluation self-check** at term-close — arithmetic balance: confirmed + revised_relevant + revised_group = total active verses
4. **Runs the orphan-group check** — every pre-existing active group must be retained-with-verses, dissolved, or carried-without-verses-with-reason; **no silent pass-through**

> v3_10 halt-resolution discipline: "Halt is *stop-and-investigate*, not *stop-and-walk-away*." When a term is halted partway through a prior session, every previously-pending verse must be read, filtered, and given an explicit `verse_context` row. Implicit set-aside (no row) is the original prior-session error and must not be repeated.

---

## What the classifier produces alongside the per-verse rows

Per term:

1. **Classification block** in observations file (machine-parseable; structured `{mti_id}-{serial}` group codes)
2. **Re-evaluation self-check statement** (if RE-EVALUATION)
3. **Orphan-group check statement** (if RE-EVALUATION)
4. **Patch-routing class** at session-close: NEW-ONLY / REVISE-ONLY / MIXED / NO-CHANGE (§6.3 Step 3)

Per session (up to 4 patches per §7.9):

1. **VCNEW** — first-time classifications (insert ops)
2. **VCREVISE** — revisions to existing classifications (update ops); empty-ops VCREVISE confirms "no-change" terms
3. **VCSBFLAGS** — Session B observations raised while reading
4. **VCSDPOINTERS** — cross-registry pointers raised while reading

Each patch carries `_patch_meta.terms_covered` and (for VCNEW/VCREVISE) `input_versions` map for the A-03 version gate.

---

## What the classifier does NOT do

Per §0:

- **Analyse the meaning** of terms in depth — that is Session B
- **Draw conclusions** about the word being studied — that is Session B
- **Produce cross-registry synthesis** — that is Session D
- **Assign evidential status** — that is Session B
- **Classify XREF terms directly** — XREF status is derived from OWNER (§0.2)
- **Advance `word_registry.verse_context_status`** — that's a CC-side derived aggregation
- **Re-render any artefact** — Claude Code's job

---

## In-session resolution before flagging (added v3_10)

A flag is for findings **the classifier cannot resolve by reading**. Findings the classifier *can* resolve by reading must be resolved in-session.

- Use reading to answer: "Does this verse fit existing group X or warrant new group Y?" — read the verse against the group descriptions and members.
- Reserve flags for: decisions with broad implications, programme-vocabulary boundaries, cross-registry findings, factual ambiguities only the researcher can resolve.

> The principle: a flag means "I cannot answer this without you." If the classifier can answer it by reading, the flag is the wrong instrument; the answer is.

---

## End-state for a correctly-processed verse

After classification, every active OWNER verse for an active OWNER term has exactly one (or two, in dual-context) `verse_context` rows where:

- All four of `is_relevant`, `is_anchor`, `is_related`, `group_id` are populated according to R1–R4
- If `is_relevant=0`: `set_aside_reason` is from the controlled vocabulary; `notes` may carry detail (mandatory for `wrong_face` and `other`)
- If `is_relevant=1`: `group_id` points to an active group with at least one anchor; the group's `context_description` names the inner-being characteristic served and the term's role in that service
- The row's audit trail (operation `insert`/`update` driven by row presence at `(mti_term_id, verse_record_id)`) is preserved through the four-patch model

**Coverage metric:** a term is at coverage when `classified_rows + explicit_set_aside_rows = total_active_verses`. Pending = `verses without any row at all`. The classifier is responsible for ensuring no verse remains pending.

---

## Diagnostic implications (for the cleanup in flight)

The above is the rule book. Today's diagnostic finds large gaps against it:

| Diagnostic | Count | Gap against rule |
|---|---:|---|
| `is_relevant=0` rows with `set_aside_reason=NULL` (legacy "muddled") | 1,043 vc rows + 4,365 wider | Violates §3.2 mandatory-reason rule |
| OWNER `wa_verse_records` with no `verse_context` row | 18,034 | §3.2b — these count as **pending**, not set-aside; the verses were never analysed |
| Anchors on grammatical-noise Strong's (pre-Tier 1 cleanup) | 246 | Violates §3.5 — particle assessment was structural rather than functional |
| Anchors on homonym-mistarget Strong's (pre-homonym cleanup) | 35 | Violates §3 — filter was applied to verse theme, not term's specific use |

Today's cleanup patches re-aligned the data to the rule book in three respects: noise anchors removed, homonym-mistarget terms excluded with `set_aside_reason='no_inner_being'`, and reversibility preserved through audit-trail notes.

The remaining gap (the **18,034 unclassified verses**) is the structural backlog the v3_10 instruction assumes will be addressed by the new verse interpretation routing.
