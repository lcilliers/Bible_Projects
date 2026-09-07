# Phase 11 design decisions — explained with real examples

**Purpose:** before CC builds the `cluster_finding` loader, three design choices need researcher input. This document shows the actual finding text from M01, what each option does to that text in the database, and what a Session C reader sees later.

---

## Background: what Phase 11 does

CC reads the 4-part Phase 9 consolidated findings document and creates one `cluster_finding` row per (prompt × scope) cell. A row carries:

- `obs_id` — the prompt (e.g. T2.1.1)
- `cluster_code` — `M01`
- `cluster_subgroup_id` — A, B, C, D, E, F, G, BOUNDARY, or NULL for CLUSTER scope
- `finding_text` — the paragraph AI wrote
- `outcome_code` — E, S, or G
- `version` — `v1-20260516`

This is the database-canonical form of M01's analytical output. Session C reads from `cluster_finding` to write the cluster's published chapter, and Session D reads from it to do cross-cluster work.

The 4-part document is parser-safe **except** for 38 marker patterns AI invented when answering the prompts more precisely than the canonical scheme allows. Those 38 are the source of all three decisions below.

---

## Decision 1 — How to handle VCG-level scope markers

### The actual problem (real M01 example)

Prompt T2.1.1 — "Is this characteristic explicitly located at the spirit level in the verse evidence?"

AI's findings for this prompt (verbatim):

| Scope marker as written | Outcome | Finding (abridged) |
|---|---|---|
| `[A]` | S | M01-A has no verse explicitly at spirit level. |
| `[B, C, D, E-VCG-01/03/04/05, F]` | S | These sub-groups + most of E are silent at spirit level. |
| `[E-VCG-02]` | E | M01-E-VCG-02 is the most explicit spirit-level location (Isa 66:2 anchor)... |
| `[G]` | E | M01-G-VCG-01 contains the most explicit negative spirit-level location (2Ti 1:7)... |
| `[CLUSTER]` | E | Only two places in 941 verses have explicit spirit-level location: Isa 66:2 (E-VCG-02) and 2Ti 1:7 (G-VCG-01)... |

**The issue with the marker scheme:**

Sub-group E (M01-E "Trembling / Fear Made Somatic") has 6 VCGs. For the question "is it at spirit level?":
- 5 of the 6 VCGs (E-VCG-01, E-VCG-03, E-VCG-04, E-VCG-05, E-VCG-06) → silent.
- 1 of the 6 (E-VCG-02, the "trembling-at-God's-word" VCG containing Isa 66:2) → **yes, explicitly spirit-level.**

The schema as written gives one row per (prompt × scope). Scope = sub-group letter. So for sub-group E there is **one** row — but the truthful answer is **mixed**.

AI invented `[E-VCG-02]` to record the mixed answer truthfully. That's analytically right. But the schema doesn't have a slot for VCG-level scope.

### The three options — with what gets stored and what Session C reads

#### Option A — Roll up to parent letter, accept the conflict

Two rows for sub-group E under prompt T2.1.1:

| obs_id | scope | outcome | finding_text |
|---|---|---|---|
| T2.1.1 | E | S | (from `[B,C,D,E-VCG-01/03/04/05,F]`) "Acute fear, terror-as-force, dismay, somatic trembling (except E-VCG-02), and anticipatory dread are not explicitly located at the spirit level in any verse in these sub-groups." |
| T2.1.1 | E | E | (from `[E-VCG-02]`) "M01-E-VCG-02 contains the cluster's most explicit spirit-level location. Isa 66:2 (anchor)..." |

**Database consequence:** the UNIQUE constraint `(obs_id, cluster_code, cluster_subgroup_id, version)` is **violated** — two rows would have the same key. The loader would either error or one row would overwrite the other.

**Session C consequence:** if loader errors, Phase 11 fails until human intervention. If loader overwrites, one analysis disappears silently. **Not viable as-is** — would require relaxing the UNIQUE constraint to `(obs_id, cluster_code, cluster_subgroup_id, outcome_code, version)`, which is a schema change.

#### Option B — Add a `vcg_scope` column to cluster_finding

Schema migration: `cluster_finding` gets a new nullable column `vcg_scope TEXT`. UNIQUE constraint extended to include `vcg_scope`. Then:

| obs_id | scope | vcg_scope | outcome | finding_text |
|---|---|---|---|---|
| T2.1.1 | E | NULL | S | (from `[B,C,D,...,F]`, applies to E generally minus E-VCG-02) "Acute fear, terror-as-force..." |
| T2.1.1 | E | M01-E-VCG-02 | E | (from `[E-VCG-02]`) "M01-E-VCG-02 contains the cluster's most explicit spirit-level location..." |

**Database consequence:** schema migration (1 column add, 1 constraint change). All loader logic now needs to track vcg_scope. Future Session C queries get an extra filter.

**Session C consequence:** the chapter writer can query "spirit-level findings" and see *exactly* which sub-group AND which VCG. Highest analytical fidelity. The cost is durable schema complexity for what may be a small number of prompts where the precision matters.

#### Option C — Roll up to parent letter, merge into one row, keep VCG specificity in the body

One row for sub-group E under T2.1.1:

| obs_id | scope | outcome | finding_text |
|---|---|---|---|
| T2.1.1 | E | E | "**Mixed:** E-VCG-02 is the most explicit spirit-level location in the cluster (Isa 66:2 anchor — trembling-at-God's-word located in the spirit). E-VCG-01, E-VCG-03, E-VCG-04, E-VCG-05, E-VCG-06: silent at spirit level (somatic trembling not located at spirit level). [merged from AI's [E-VCG-02] E and [B,C,D,E-VCG-01/03/04/05,F] S]" |

The loader concatenates the two AI blocks. The outcome code is the "most positive" available (E beats S beats G, since E is evidenced).

**Database consequence:** no schema change. UNIQUE constraint satisfied. One row per (prompt × sub-group). Loader gets merge logic for these 38 cases.

**Session C consequence:** writer sees one finding for "M01-E spirit-level" that explicitly names which VCG carries the answer. Less queryable (can't filter by VCG) but the analytical content is preserved in the text. The "outcome code" loses some precision (it's E because part of E is E — a Session C writer reading just the code might miss that most of E is silent).

#### Recommendation: Option C

- **No schema change** — keeps the cluster_finding schema as designed.
- **No data loss** — the analytical precision AI captured stays in the text.
- **One row per scope** — preserves the UNIQUE constraint and the Phase 9 §12.4 discipline "one block per (prompt × scope)".
- **Acceptable tradeoff** — Session C / Session D won't be able to filter by VCG, but **they could still grep the body text** for "E-VCG-02" if they need precise routing.

Option B is worth it ONLY if you expect to query the cluster_finding table programmatically by VCG. For a publication-oriented use case where Session C writes a chapter from the findings, the text is what matters and Option C is sufficient.

The 38 affected prompts/scopes (~5% of the 720 cells) would carry a small "merged" marker in their text. All other 682 cells need no special handling.

---

## Decision 2 — How to handle cross-cluster axis markers

### The actual problem (real M01 example)

Prompt T6.6.2 — "What does the shared anchor reveal about the relationship between the two characteristics?"

AI's findings (verbatim):

| Scope marker | Outcome | Finding (abridged) |
|---|---|---|
| `[A/Love]` | E | 1Jo 4:18's shared anchor between M01 and a Love cluster reveals that fear and love are constitutively related... mutually exclusive in completion, mutually implicating in incompletion. |
| `[A/Wisdom]` | E | Pro 1:7's shared anchor between M01 and Wisdom reveals that these characteristics are constitutively linked... foundational/fruit relationship. |
| `[CLUSTER]` | E | Shared anchors reveal that M01 is structurally central in the programme's inner-being landscape: multiple characteristics have foundational/structural relationships with fear. |

**The issue with the marker scheme:**

The prompt asks about relationships *between M01 and other clusters*. The natural answer names the pair: "M01 ↔ Love" or "M01 ↔ Wisdom". AI used `[A/Love]` and `[A/Wisdom]` to express this — non-canonical but analytically correct.

There are only 2 such markers in the entire 720-cell corpus.

### The two options

#### Option α — Convert to `[CLUSTER]` with cross-cluster axis named in body

One row per cross-cluster pair, scope = `CLUSTER`:

| obs_id | scope | outcome | finding_text |
|---|---|---|---|
| T6.6.2 | CLUSTER | E | "**M01 ↔ Love pair:** 1Jo 4:18's shared anchor reveals that fear and love are constitutively related — mutually exclusive in completion, mutually implicating in incompletion." |
| T6.6.2 | CLUSTER | E | "**M01 ↔ Wisdom pair:** Pro 1:7's shared anchor reveals these characteristics are constitutively linked — foundational/fruit relationship." |
| T6.6.2 | CLUSTER | E | (AI's original CLUSTER row about M01's structural centrality) |

**Database consequence:** three CLUSTER rows for the same prompt under M01 — UNIQUE constraint same as Decision 1 (need to relax to allow multiple CLUSTER rows, OR merge into one). Cleaner to merge.

#### Option β — Merge into one CLUSTER row

One row for prompt T6.6.2 scope CLUSTER:

| obs_id | scope | outcome | finding_text |
|---|---|---|---|
| T6.6.2 | CLUSTER | E | "M01 is structurally central in the programme's inner-being landscape. **M01 ↔ Love pair (1Jo 4:18 shared anchor):** fear and love are constitutively related — mutually exclusive in completion, mutually implicating in incompletion. **M01 ↔ Wisdom pair (Pro 1:7 shared anchor):** these characteristics are constitutively linked — foundational/fruit relationship. [merged from AI's [A/Love] E + [A/Wisdom] E + [CLUSTER] E]" |

#### Recommendation: Option β (merge)

Same logic as Option C in Decision 1. Only 2 markers affected. The "shared anchor" relationships are exactly the kind of cross-cluster finding T6.6 is designed to capture, and they're already saying "M01 has these external links". Merging into one CLUSTER row preserves the analytical content without inventing schema for 2 prompts.

---

## Decision 3 — How strict to be about "E entries must cite verses"

### The actual problem

The v2_1 §12.7 discipline says:

> Every E response includes specific verse reference(s) in the body.

The validator flagged **191 E entries** (out of 655 total E entries — 29%) that have no parseable verse reference. On spot-check, the 191 split into two kinds:

#### Kind 1 — Legitimately structural / definitional (most of them)

Example: T1.1.1 "How is the cluster name informative about its content?" — answered per sub-group:

> **[A]** E — M01-A is called "Reverential Fear / Fear of God as Governing Orientation." The name signals three things: (1) "reverential" — the fear is morally and relationally appropriate, not merely visceral; (2) "fear of God" — the fear is directed, relational, and object-specific; (3) "governing orientation" — the fear is not an episodic event but a sustained inner disposition that governs the whole person. The name accurately captures the dominant characteristic of the sub-group's 364 verses: a settled, life-shaping reverence toward God.

**No verse reference is needed.** The prompt is about the *label*; the answer is about the *label*. Citing a specific verse would actually be a category error.

#### Kind 2 — CLUSTER synthesis citing sub-groups (some of them)

Example: T0.1.1 [CLUSTER]:

> **[CLUSTER]** E — Across M01, fear as a human inner-being characteristic reflects and images the holiness, sovereignty, and relational depth of God. The cluster reveals that God is: (1) the supreme object of reverential fear by virtue of his holiness and incomparability (M01-A); (2) one whose presence is intrinsically overwhelming (M01-B, E); (3) sovereign over all terror as a historical instrument (M01-C); (4) the ground of inner stability whose withdrawal produces dismay (M01-D); and (5) the final judge before whom anticipatory dread is rational (M01-F). The characteristic images God not as a property God shares with the human person (God does not fear — see T0.1.2) but as the One before whom the human person rightly orients in fear.

**The CLUSTER finding cites sub-groups (M01-A, M01-B, etc.) but no specific verses.** The verses are in the sub-group rows; the CLUSTER row is summary across sub-groups. Citing each verse would duplicate them across all 189 cluster rows.

### The two options

#### Option X — Accept all 191 as-is (advisory only)

Load all 720 E/S/G cells as written. Don't enforce verse-citation at load time.

**Database consequence:** clean load, no rejections.

**Session C consequence:** chapter writer reads the findings as AI wrote them. If a finding seems ungrounded, they go to the underlying verses in the grouped report. No information is lost; the discipline becomes "verify when in doubt" rather than "enforced at load".

**Risk:** if a future cluster's AI produces sloppy E findings that genuinely lack grounding, we won't catch them at load time. We'd catch them at Session C review.

#### Option Y — Enforce + downgrade

Loader checks every E entry for verse refs (`Book C:V` pattern) or VCG codes (`M01-X-VCG-NN`). If missing, downgrades to S (silent) and logs a downgrade list.

**Database consequence:** ~191 of 655 E entries become S. Most of the downgrades are wrong (Kind 1 / Kind 2 above are legitimate E without verse refs).

**Session C consequence:** writer sees 30% of the cluster as silent where AI actually said something. Misleading.

#### Recommendation: Option X (accept as-is)

The validator's 29% flag rate is itself the signal that the rule "every E cites a verse" was too strict — it doesn't account for label-prompts (T1.1.x), cross-cluster syntheses (CLUSTER scope), or summary findings. Enforcing it would destroy correct analytical content.

Better to:
- Load as-is now.
- Note in the applied report that 191 E entries are "structural" (no specific verse cite expected) and the loader did not enforce.
- For future cluster runs, refine the §12.7 discipline to distinguish "anchoring E" (must cite) from "structural E" (label or synthesis — citation optional). v2_2 candidate.

---

## Summary of recommendations

| Decision | Recommendation | Schema change? | M01 cells affected |
|---|---|---|---|
| 1. VCG-level markers | **Option C — merge to parent letter, keep VCG specificity in body** | No | 36 cells across part2-T2 + part3-T3-T4 + part4-T5-T7 |
| 2. Cross-cluster axis markers | **Option β — merge to single CLUSTER row** | No | 2 cells (both in T6.6.2) |
| 3. Uncited E entries | **Option X — accept as-is; refine §12.7 in v2_2 later** | No | 191 E entries (advisory; no action at load time) |

**All three recommendations together:**
- No schema change.
- ~38 cells get a merge-flag note in body text.
- 191 E entries pass through with no special handling.
- Phase 11 loader can run.

---

## What I'm asking you to decide

For each decision, pick the option that fits how you intend to use the findings downstream:

- **Decision 1**: do you ever expect to query cluster_finding rows by VCG (Option B), or is the VCG specificity in the text enough for chapter-writing and cross-cluster work (Option C)?
- **Decision 2**: same question, scaled down — 2 prompts. Default β unless you object.
- **Decision 3**: do you want the load to enforce verse-citation discipline (Option Y, downgrade 191 to silent) or accept the v2_2 deferral (Option X)?

Once decided, I'll build the loader to those rules and run Phase 11.
