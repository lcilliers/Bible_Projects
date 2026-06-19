# Capturing the new findings in the DB without losing information — design proposal · 2026-06-19

**Context.** The new M02 (and M01) findings are richer than the flat `cluster_finding` row. Goal: capture
**everything of value** into the DB so that essays and stories can later be generated from findings. This doc
inventories what's in the new findings, maps each part to the DB, and proposes a capture model. **Nothing is
built yet — this is for your steer.**

## 1. What the new M02 findings actually contain (information inventory)

Three distinct grains in `Sessions-v2/M02-Anger/findings/`:

| Grain | Source | Unit |
|---|---|---|
| **G1 — characteristic × question** | the 7 `…cN-…-tieranalysis` files | one finding per (characteristic, tier-question): prose answer to each of the 126 questions, per characteristic |
| **G2 — cluster-wide synthesis** | `wa-m02-cluster-findings-v1_0` | F1, F2… synthesis points spanning the whole cluster, each tagged Observation / Interpretation / Flag, with "guide: T0,T4"-style tier hints (not tied to one question) |
| **G3 — characteristic definitions** | `wa-m02-ve-characteristics-v1_0` | the 7 characteristics themselves → the `characteristic` table (the separate (a) task) |

Each **G1/G2 finding** carries, beyond the prose:
- **(B) question link** — the tier code(s) it answers (G1: one; G2: several "guide" tiers)
- **(C) characteristic link** — which characteristic (G1: one; G2: cluster-wide / NULL)
- **(D) status** — `finding` · `silent` · `gap` · and the G2 labels `Observation` / `Interpretation` / `Flag`, plus an **inferential vs confirmed** mark
- **(E) verse citations** — the verses that ground the claim (e.g. Pro 15:18; Mar 3:5)
- **(F) pointers / cross-refs** — "belongs with C2 on verse-confirmation", "pointer: C2", "compound with M03", boundary caveats, researcher DEC decisions
- **(G) Evidence Base appendix** (v1_1) — per-field distributions + verse lists + co-occurrence web

## 2. What is genuinely new vs regenerable

- **(G) Evidence Base is regenerable** — it is a re-presentation of `ve_lexical` (already in the DB: object,
  divine_involvement, intensity, immediate_response, relational, valence, co-occurrence) + verse_text. **Do not
  store it as findings** — regenerate on demand for the essay pipeline. Storing it would duplicate ve_lexical
  and go stale.
- **Genuinely new = the findings themselves (A) + their metadata (B–F).** That is what must be captured.

## 3. What the DB already offers (two finding stores)

| | `cluster_finding` | `finding` (+ children) |
|---|---|---|
| characteristic link | **yes** (`characteristic_id`) | no column |
| question link | **yes** (`obs_id`, one) | `finding_question_link` (many) |
| status | `finding/silent/gap/cluster_synthesis` | `finding_status` |
| free type slot | **`finding_type` (unused — all NULL)** | — |
| verse citations | none | `finding_citation`, `finding_verse_link` |
| supersession / justification | no | `supersedes_id`, `justified_by_finding_id` |

**Key realisation:** `finding_citation` is **generic** — its keys are `(source_table, source_id, citation_type,
citation_value)`. So it can attach citations to **`cluster_finding` rows** (`source_table='cluster_finding'`,
`source_id=cf.id`) **with no schema change** — for verses *and* pointers *and* science-lens refs.

## 4. Proposed capture model (recommended: extend `cluster_finding`, reuse generic citations)

Capture each G1/G2 finding as **one `cluster_finding` row**, and attach its citations/pointers via the existing
generic `finding_citation`:

- **(A) prose** → `cluster_finding.finding_text`
- **(B) question** → `obs_id` (G1: the one question; G2: the *primary* guide-tier question, with extra tiers as
  `citation_type='guide_tier'` rows)
- **(C) characteristic** → `characteristic_id` (G1: set; **G2 cluster-synthesis: NULL** + `finding_status='cluster_synthesis'`)
- **(D) status** → `finding_status` (`finding`/`silent`/`gap`/`cluster_synthesis`); **`finding_type`** carries the
  G2 label (`observation`/`interpretation`/`flag`) and an `inferential` mark; `needs_research` flags gaps/caveats
- **(E) verse citations** → `finding_citation(source_table='cluster_finding', source_id=cf.id, citation_type='verse', citation_value='Pro 15:18', position=n)`
- **(F) pointers** → `finding_citation(… citation_type='pointer', citation_value='C2' | 'M03' | 'DEC-2')`
- **provenance** → `source_file`, `version` (already there)

**Why this path:** it loses nothing; `cluster_finding` is the existing catalogue-prompted home and the *only*
store with `characteristic_id` (essential for M02's characteristic×question grain); `finding_type` is free for
the labels; citations/pointers ride the generic `finding_citation` with **zero schema change**. It also handles
**both grains we already have** — M01's question-level-collated findings (`characteristic_id` NULL) and M02's
per-characteristic findings (`characteristic_id` set) — in one model.

### The alternative (for the record)

**Path B — consolidate onto the universal `finding` store** (M55 direction): richer native links + supersession,
but it has **no `characteristic_id`** (would need a column or a finding↔characteristic link table) and means
migrating/reconciling the ~20k existing `cluster_finding` rows. Cleaner long-term, materially bigger change.
My recommendation is **Path A now**; revisit Path B as a deliberate consolidation later if wanted.

## 5. How this serves essay / story generation

With the model above, the essay pipeline can query:
- **by characteristic** (all findings for C1) or **by tier/question** (all characteristics on T3.4) or **by
  cluster synthesis** (the F-points) — `cluster_finding` filtered on `characteristic_id` / `obs_id` / status;
- **ground every claim in verses** — join `finding_citation` (verse) to cite chapter-and-verse in the prose;
- **weave cross-threads** — follow `pointer` citations (C1↔C2, M02↔M03) to connect related findings;
- **exclude/needle** — drop `silent`, surface `inferential`/`flag` for caution, pull `interpretation` for the
  argumentative spine and `observation` for the evidential body.

## 6. Open decisions for you

1. **Path A vs Path B** (recommend **A** — extend `cluster_finding` + generic citations).
2. **Citations granularity** — store every cited verse per finding (rec), or only the anchor verses?
3. **Evidence Base** — confirm it stays *regenerable from ve_lexical*, not stored as findings (rec).
4. **G2 cluster-synthesis question link** — keep the "guide tiers" as `guide_tier` citation rows (rec), or leave
   cluster-synthesis findings unlinked to questions?
5. **M01/M02 consistency** — M01's new findings are question-level-collated (173, one per question); M02's are
   per-characteristic (7×~126). Both fit the model; confirm we keep both grains rather than forcing one.

Once you steer §6, I'll build a parser + reviewed JSON patch (dry-run → review → apply), starting with M02.
