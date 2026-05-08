# Cluster Ecosystem Overview — report design

**Date:** 2026-05-04
**Status:** DESIGN PROPOSAL — awaiting researcher approval before build
**Author:** Claude Code
**Companion:** [Workflow/Sessionlogs/wa-sessionlog-term-anchor-reset-v1-20260504.md](../../Workflow/Sessionlogs/wa-sessionlog-term-anchor-reset-v1-20260504.md)

---

## 1. Purpose

Make the newly-built term-anchor cluster ecosystem (2,491 OWNER terms → 55 Hebrew + 33 Greek top-level clusters, 134 recursive leaves) legible as a single navigable picture. Answer the questions a researcher arriving cold will ask first:

1. What clusters exist? How big? How healthy?
2. How does the new structure differ from the old registry/dimension structure?
3. Where are the gaps (unclassified verses, FLAG terms, isolated singletons)?
4. Where do clusters cross language (Hebrew ↔ Greek) and where don't they?
5. What needs a researcher decision next?

## 2. Scope decision (recommend Option a)

| Option | Form | Pros | Cons |
|---|---|---|---|
| **(a) Overview + on-demand drill-downs** | One overview `.md` (this report) + a generator that writes per-cluster `.md` on request | Navigable; cheap to build; per-cluster pages built only where actually needed | No deep cluster pages day-one |
| (b) Full ecosystem package | Overview + 88 per-cluster files + 5 sub-reports in a directory | Comprehensive | ~100 files; many will be reference-only and rarely read; expensive to keep current |
| (c) Single mega-report | Everything in one `.md` | One file to read | ~80–100 pp markdown — unusable for navigation |

**Recommendation: Option (a).** Build the overview now. Build the per-cluster drill-down generator now (cheap). Generate per-cluster pages on demand.

**Output naming (per `wa-reference [current]`):**
- Overview: `outputs/markdown/wa-cluster-ecosystem-overview-v1-20260504.md`
- Per-cluster (when generated): `outputs/markdown/clusters/wa-cluster-{H001|G001}-v1-20260504.md`

## 3. Data sources

Inputs (no DB writes; read-only assembly):

| Source | Role |
|---|---|
| `outputs/markdown/wa-term-anchor-20260504.json` | Canonical anchor: per-term cluster_id, bucket, attachment_affinity, cluster_label |
| `outputs/markdown/wa-term-anchor-20260504-clusters.md` | Cluster theme-word labels (already generated) |
| `outputs/markdown/wa-term-anchor-20260504-flags.md` | FLAG bucket (24 terms) |
| `outputs/markdown/wa-term-anchor-validate-20260504.json` | Cluster quality (TIGHT/MODERATE/LOOSE), recursive sub-cluster results, unclassified-verse coverage |
| `outputs/markdown/term-clusters-crosslang-20260504.json` | Hebrew ↔ Greek cluster bridges |
| `outputs/markdown/term-mounce-bridges-20260504.json` | Mounce-derived NT cross-cluster signal |
| `outputs/markdown/term-cluster-assessment-20260504.json` | Registry-vs-cluster alignment (the diagnosis that drove the pivot) |
| `database/bible_research.db` | OWNER-term verse counts, root-family membership, mti_terms metadata, legacy registry, legacy `verse_context_group` for overlay |

## 4. Report structure (sections in build order)

### §A. Executive snapshot (1 page)

A single landing block. Headline numbers, no tables longer than 8 rows.

- Total OWNER terms anchored: 2,491
- Bucket distribution: T1 / T2 / FLAG / EXTRACTION-NOISE counts (single 4-row table)
- Cluster catalogue: 55 H + 33 G top-level → 79 H + 55 G recursive leaves
- Verse coverage: classified % / unclassified pair count / distinct unclassified verses
- Quality (top-level, T1-only): TIGHT / MODERATE / LOOSE counts (Hebrew + Greek separately)
- Cross-language bridges: count of H clusters with a G partner; count of G clusters with an H partner; orphan counts
- Top 3 open researcher-decision items

**Why this section:** so the report stands alone — a researcher reading just §A walks away with a true mental model.

### §B. Cluster catalogue — master table

The single most-referenced section. One row per top-level cluster, both languages in one sortable table (or two adjacent tables — Hebrew, then Greek).

**Columns (per cluster):**

| Column | Source | Notes |
|---|---|---|
| `cluster_id` | anchor JSON | `H001`..`H055`, `G001`..`G033` |
| `label` | anchor clusters md | Top theme words, e.g. "turn/aside/angry" |
| `T1_terms` | anchor JSON | Primary characteristic count |
| `T2_terms` | anchor JSON | Secondary attachment count |
| `total_terms` | sum | T1 + T2 |
| `total_verses` | DB join on `wa_verse_term_links` | Distinct verses any cluster term appears in |
| `unclassified_pairs` | validate JSON | Pairs not yet group-classified |
| `unclassified_pct` | derived | Unclassified / cluster total pairs |
| `tightness` | validate JSON | TIGHT / MODERATE / LOOSE (top-level) |
| `recursive_leaves` | validate JSON | How many sub-clusters after recursive split |
| `dominant_legacy_registry` | DB | Registry that contributes most OWNER terms (and its %) |
| `crosslang_partner` | crosslang JSON | Other-language cluster_id (or "—" if orphan) |

**Sort:** by `total_verses` desc by default (heaviest clusters first).

**Filters offered as appendix tables:** unclassified-pct desc, tightness=LOOSE first, no crosslang_partner.

### §C. Bucket inventory

Each bucket gets a short subsection with its full term list (or count + anchor-md link if the list is large).

- **T1 (1,752)** — link to catalogue (already covered in §B); brief note on what makes a term T1.
- **T2 (491)** — counts per cluster of how many T2 terms are attached; top-10 clusters by T2 count.
- **FLAG (24)** — full table reproduced from `wa-term-anchor-20260504-flags.md`, with the three theme groups identified in the session log §2.7 (beloved-family, judgment-family, theological anchors) called out.
- **EXTRACTION-NOISE (37)** — full list with Strong's, gloss, why excluded.
- **QUALIFIER (0)** — note the bucket exists and was used in 5-way clustering but didn't survive into final structure; explain rationale.

### §D. Cross-language ecology

What's been built: `term-clusters-crosslang-20260504.json` has cluster-pair affinities. This section makes them legible.

Sub-sections:

1. **Bridged H↔G pairs** — table: H_cluster | H_label | G_cluster | G_label | bridge_strength | example shared root or Mounce link.
2. **Hebrew-only clusters (no G partner)** — what's distinctive about them; expected (e.g., OT-only theological vocabulary like "covenant-loyalty" subsenses)?
3. **Greek-only clusters (no H partner)** — distinctive NT theological vocabulary that has no OT counterpart (Christ-titles, ekklesia, etc.).
4. **Mounce bridges as quality indicator** — count and listing of Mounce-derived links per cluster.

### §E. Legacy-registry overlay

The bridge from the old model to the new — answers "what happened to my registries?"

For each of the 184 OWNER-bearing registries (the ones with terms that survived into clustering):

| Column | Notes |
|---|---|
| `registry_id` | R001..R214 |
| `english_word` | from `word_registry` |
| `OWNER_terms` | count of OWNER terms in this registry |
| `clusters_touched` | distinct cluster_ids across this registry's terms |
| `dominant_cluster` | cluster_id holding the most OWNER terms |
| `dominant_pct` | % of registry's OWNER terms in dominant cluster |
| `verdict` | one of: **CONSOLIDATED** (≥80% in one cluster), **SPLIT** (50–80% in one), **FRAGMENTED** (<50% in one) |

Plus three call-out sub-tables:
- **CONSOLIDATED registries (≥80%)** — registries that survived the pivot intact; minimal disruption to legacy work
- **SPLIT registries (50–80%)** — registries where one cluster is dominant but a second cluster takes a meaningful slice; legacy Session B work needs review
- **FRAGMENTED registries (<50%)** — these are the registries the assessment showed as "miscut"; legacy work is materially affected

Counts already known from `term-cluster-assessment`: ~76/120 clusters cross-cut 3+ registries → expect majority of registries to be SPLIT or FRAGMENTED.

### §F. Quality dashboard

What's been built: `term-cluster-quality-v2-20260504.json` per language. This section reproduces those tables and adds context.

| Sub-section | Contents |
|---|---|
| Top-level quality | Hebrew: 13 TIGHT / 33 MOD / 9 LOOSE. Greek: 4 TIGHT / 19 MOD / 10 LOOSE |
| After recursive sub-clustering | Hebrew: 28 TIGHT / 51 MOD / 0 LOOSE leaves. Greek: 13 TIGHT / 42 MOD / 0 LOOSE leaves. **All LOOSE resolved** |
| Recursive depth distribution | How many top-level clusters needed sub-clustering, and to what depth |
| Worst-quality top-level clusters | Listed with diagnostic — usually high-frequency stems that mix unrelated meanings |
| Frequency-artifact watch | Currently 0; explanation of what would put a cluster here |

### §G. Coverage backlog

The unclassified-verse work-list. Already built in `wa-term-anchor-validate-20260504.md` §B; this section reproduces the top-15 work-list and adds rough effort estimation.

| Cluster | Lang | Label | Unclassified pairs | Distinct verses | Suggested batch size |
|---|---|---|---|---|---|
| H028 | H | turn/aside/angry | 937 | 883 | 1 batch of 50 verses × 17 runs |
| H019 | H | truth/rule/delight | 502 | 497 | 10 runs |
| ... | | | | | |

Plus a footer:
- Total backlog: 6,897 pairs / 5,753 distinct verses
- Estimated cost at 50 verses/run, ~$X/run on Sonnet 4.6 (cost model TBD per session log §4 open item)

### §H. Co-occurrence map (optional — flag for decision)

The co-occurrence vector built today (`term-cooccurrence-vectors-20260504.npz`) lets us identify which clusters share verses most heavily — i.e., clusters that "talk about the same things". This would be a new analytical lens not yet exposed.

| Section | Contents |
|---|---|
| Top-20 cluster pairs by shared-verse count | "Clusters that overlap most" |
| Isolated clusters (low cross-cluster sharing) | "Topically distinct" |
| Bridge clusters (high cross-cluster sharing) | These are candidate cross-cutting analytical themes |

**Decision flag:** include §H in v1, or defer to v2 once the unclassified-pair backlog is cleared (because co-occurrence numbers will shift as classification fills in)? Recommend **defer** — co-occurrence on a 79%-classified base would mislead.

### §I. Decision queue

Researcher-facing punch list in priority order. Sourced from session log §4:

1. FLAG-bucket review (24 terms) — three theme groups in §C
2. Recursive-leaf freeze decision (top-level vs leaves as canonical)
3. Top-3 unclassified-pair clusters (H028 / H019 / H034 = 1,918 pairs / 28% of backlog)
4. Cost model for verse classification at scale
5. Schema decision: `cluster_id` as a column on `mti_terms` or a sibling table?
6. Instruction-doc rewrite list (4 docs, all describing the OLD model)

## 5. Build approach

**Generator script (single file, ~400 lines):**

`scripts/_exploratory_cluster_ecosystem_overview_v1_20260504.py`

- Read the 7 input files in §3
- Assemble a single in-memory model (dict of clusters with all their attributes)
- Render each section §A–§I to one master `.md` file
- Optional `--per-cluster` flag emits drill-down `.md` files for each cluster (Option (a) on-demand generator)

Read-only — no DB writes; safe to run anytime as the canonical state evolves. Output is regenerable from inputs, so versioning rule: bump filename version (`-v1` → `-v2`) on each material structural change to the report itself, not on every run.

**Estimated output size (overview):** 8–12 pages of markdown, ~3,000–5,000 words. Comparable to `wa-term-anchor-validate-20260504.md` × 4.

**Estimated build time:** ~30 min for the script; ~10 sec to run; tweakable templates for each section.

## 6. What this report is NOT

To stay focused — explicit non-goals:

- **Not a per-verse classification tool** — that's the brief-verse-router work.
- **Not an instruction-doc replacement** — the docs in §I.6 still need to be rewritten by the researcher to formalise the new pipeline.
- **Not a DB migration plan** — schema changes (e.g., `cluster_id` columns) are out of scope; flagged for separate decision.
- **Not analytical commentary** — this is structural reference, not interpretation. "Cluster H028 means X theologically" belongs in Session C/D output, not here.

## 7. Decisions sought from the researcher

To finalise this design before build:

1. **Scope:** approve Option (a), or prefer (b) or (c)?
2. **§H Co-occurrence map:** include in v1, or defer until backlog cleared?
3. **§E Legacy-registry verdict thresholds:** ≥80% / 50–80% / <50% — keep as-is, or shift?
4. **Cluster sort default in §B:** by total_verses desc, by T1_terms desc, or by cluster_id?
5. **Per-cluster drill-down generator:** build alongside overview now, or defer until you decide it's needed?
6. **One overview vs Hebrew + Greek split:** single doc covering both, or two parallel docs (one per language)?

Once these are decided I'll build the script and the overview in one pass.
