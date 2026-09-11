# Cluster Reading — process specification v1

> Status: **proposal, under live review** — drafted from the researcher's own process notes
> (escalation #1682, filed verbatim in `outputs/escalation/1682-escalation-history-v1-20260911.md`),
> formalized by Claude for confirmation, then refined in place against the H_guilt/SUNDRY test run
> (round 1) per the researcher's review comments (round 2, this revision). Edited in situ per the
> project's review-cycle convention — not re-versioned until approved. Supersedes the ad hoc method
> used in #1680 (M10's first 14-family pass, `_analytics/Clusters/m10-family-*-20260911.*`) — that
> pass is retained as historical, superseded material, not as a template.
>
> **Round 2 changes (this revision), from the researcher's review of the H_guilt/SUNDRY test:**
> a new read rule for surface-vs-gloss divergence (§2, process c); a redesigned, structured trace
> schema that ties a verse to a specific observation explicitly instead of a flat semicolon-joined
> string (§3); a mandatory per-strong verification check, run and recorded before a family's output
> is considered complete (§2, §3); and an explicit morph-consideration rule, since round 1 barely
> used `span.morph` despite carrying it in every occurrence (§2).
>
> **Open assumptions this draft resolves that the researcher's notes left implicit** — flagged here
> so they can be corrected before the full method is trusted, not discovered after a large rerun:
> 1. "vw_strong_meaning_raw... (3 meaning rows)" is read as: **one consolidated row per source**
>    (`strong_meaning_tree`, `strong_lexicon.lsj`, `strong_lexicon.mounce`) — up to 3 total per
>    strong, with `strong_meaning_tree`'s own multiple sense-code sub-rows concatenated into that
>    one source's text (in `ord` sequence), not 3 arbitrary raw rows.
> 2. "span.surface, span.morph, verse.text" is read at **occurrence granularity** (one entry per
>    `span` row, i.e. per position a strong occurs in a verse) rather than deduplicated to one entry
>    per distinct verse — confirmed necessary live: some strongs occur twice in the same verse
>    (e.g. G0094 in one verse, G0264 in four separate verses), and de-duplicating to unique verse
>    text (the #1680 method) silently drops that.
> 3. Process (a)'s JSON is assembled **once, for the whole cluster** (it is a deterministic data
>    pull, not an LLM step) — the "always by family, never as a full cluster" rule in the
>    researcher's notes applies explicitly to process (c), and by clear implication to how process
>    (b)'s output is consumed, not to the mechanical assembly step itself.

## 1. Scope

Cluster reading runs **for one cluster** (e.g. `M10`), against **all strongs in that cluster by
default**, or a researcher-supplied subset. Nothing else is in scope for this spec — this is the
read/synergy/output process only, not a cluster-assignment audit (data errors *found* while reading
are flagged per §4, not corrected here).

## 2. Pipeline — three separate processes, never combined

Processes (a), (b), (c) are **always run as separate steps**. Process (c) is **always run per
family** — one LLM pass per family, never the whole cluster in one pass.

### Process (a) — assemble the base JSON (deterministic, scripted, no LLM)

For every strong in scope, assemble:

1. **Occurrences** (one entry per `span` row — every occurrence, not deduplicated by verse):
   `cluster_code`, `strong`, `stepGloss`, `osisId`, `reference`, `verse.text`, `span.surface`,
   `span.morph_code`.
2. **Meaning** (one entry per source present, up to 3):
   `source` (`strong_meaning_tree` | `strong_lexicon.lsj` | `strong_lexicon.mounce`), `text` —
   `strong_meaning_tree`'s sense-coded sub-rows concatenated in `ord` order into that one source's
   text; `lsj`/`mounce` are already one row each in `vw_strong_meaning_raw`.

Output: **Json A**, one file per cluster (all strongs in scope). Query pattern:

```sql
-- occurrences
SELECT sp.strong_variant AS strong, s.stepGloss, v.osisId, v.reference, v.text AS verse_text,
       sp.surface AS span_surface, sp.morph_code AS span_morph
FROM span sp
JOIN verse v ON v.id = sp.verse_id
JOIN strong s ON s.strongNumber = sp.strong_variant
WHERE sp.strong_variant IN (<strongs in scope>) AND sp.deleted = 0 AND v.deleted = 0
ORDER BY sp.strong_variant, v.id, sp.position;

-- meaning (aggregate strong_meaning_tree rows per strong before emitting)
SELECT strong, source, sense_code, raw_text, ord
FROM vw_strong_meaning_raw
WHERE strong IN (<strongs in scope>)
ORDER BY strong, source, ord;
```

### Process (b) — family assignment (LLM reasoning over Json A, no scripting)

The LLM reads Json A (gloss + meaning per strong; occurrence text as needed) and places **every**
strong into exactly one family of like-meaning strongs.

- **No strong is ignored.** A strong that doesn't fit a coherent family goes into a mandatory
  **`SUNDRY`** family, explicitly for strongs earmarked for later analysis — not folded into a
  forced family and not silently dropped. (The #1680 pass's four one-member "families" and its two
  homonym-noise strongs should all have landed in `SUNDRY` under this rule, not been written up as
  if they were ordinary families.)
- Output: **Json B** — `{"cluster_code": ..., "families": [{"family_id", "family_label", "strongs": [...]}, ..., {"family_id": "SUNDRY", "strongs": [...]}]}`. Every strong in Json A appears in exactly one family's `strongs` list.

### Process (c) — cluster reading by family (LLM reasoning, one run per family)

Input: Json A filtered to that family's strongs (occurrences + meaning) + the family's entry from
Json B. **Never the whole cluster in one pass.**

Objective (verbatim from the researcher): *synergise the similar and different contextual meaning
of terms in verses, highlighting the nuances and describing the actual meaning* — linking and
interpreting the STEP meaning **across all three meaning sources** in the context of the verses,
grouping verses with similar meaning where appropriate.

**Read rules (checklist, apply every run):**

- [ ] Read **all three meaning sources in full** for every strong — never dump raw text unread,
  never skip a source. Compare that reading against the verse context.
- [ ] **Scan every verse occurrence** — no sampling, regardless of strong or family size. A high
  occurrence count is never a reason to sample or silently drop instances.
- [ ] Similar verses **may be grouped** where their meaning is genuinely alike — but grouping does
  not excuse skipping any instance; every instance is still accounted for.
- [ ] **Every instance states what it is** — a positive reading, not only a contrast with other
  instances.
- [ ] The aim is **not** a single distilled meaning. Show what the verse's meaning could be or is
  likely to be, **including alternative candidate meanings** where the data supports more than one
  reading.
- [ ] An observed **difference or a specific inference** is recorded as its **own, separate**
  observation — not folded silently into the main per-instance reading.
- [ ] **A difference between `span.surface` (the actual English rendering in that verse) and the
  strong's `stepGloss` (its catalogue gloss) is itself a subject of observation, tagged
  `surface-gloss-divergence`, and must be explored** — not merely noted in passing. State what the
  divergence suggests about that specific occurrence's sense (a shift in register, a distinct
  sub-sense, a translator's smoothing choice), not just that it occurred. (Found live in round 1
  without a rule for it: H0816 rendered as "condemned," "ruined," and "suffer" in different verses,
  not just "guilty" — each of those was a real, distinct-sense finding, not an incidental footnote.)
- [ ] **`span.morph` must be actively read, not merely carried.** Where occurrences of the same
  strong show different stems/voices (e.g. Qal vs. Niphal vs. Hiphil in Hebrew; active vs. passive
  vs. middle in Greek), check whether that variation is meaning-relevant — does the subject *do* the
  action, *have it done to them*, or *cause another to do it*? Where it is relevant, record it as its
  own `difference-inference` observation citing the specific morph codes; where a family's read
  shows no morph-driven distinction worth recording, that absence is itself worth a one-line note
  (`morph-reviewed, no distinction found`) rather than silence — round 1 produced 49 observations
  citing `span_surface` divergence and content but not one that engaged `span.morph` at all, which
  is not evidence that morph was irrelevant, only that it was not actually checked.
- [ ] **Verify traceability per strong, not only per family, before that strong's reading is
  considered done.** After drafting observations for a strong, enumerate its occurrences from Json A
  and confirm every one is cited in at least one observation's `traces.occurrences` for that strong
  (see the structured trace schema in §3). Record the result as a `strong_checks` entry (§3) —
  this is a required output, not an optional sanity check the author may skip. (Round 1 only caught
  its own 7 missing verses via a post-hoc script run at the end of the whole family, not as a
  per-strong gate — the missed verses were a genuine near-miss the process should not depend on
  remembering to check for.)
- [ ] A strong that is exclusively a homonym/name with **no meaningful context for a human reader**
  (e.g. a place name or letter name colliding with the family's English gloss) is **earmarked as
  such and left there — no further analysis** attempted on it.
- [ ] **Cross-family observations, anomalies, open questions, and pointers to other clusters** are
  produced as an **additional, separate** synergy pass — clearly separated from the per-family
  reading, not threaded informally through it.
- [ ] **Data errors** (e.g. a wrong `cluster_strong` membership, a broken span/verse link) are
  flagged **separately** from meaning observations — their own row, per §4.

## 3. Output

**One JSON per cluster family** (not per strong, not per cluster) is the standard, required
output. Filed under `_analytics/Clusters/` per
`cfg_setting.report.cluster_path`/`cluster.quality_report_path`.

**Round 2 correction: MD is not a standard output.** Round 1/early round 2 rendered a `.md`
companion from every family JSON. Researcher's call on inspecting both: the JSON is good; the MD
is fine for a human skimming one family, but it is not a good input document for the next phase
(a downstream findings table needs the structured record, not prose paragraphs with an embedded
trace string) — producing it as a matter of course would just be a second artifact to keep in sync
for no downstream purpose. **MD generation is now ad hoc, on request, for inspection only** —
`temp_1682_render_family_md.py` still exists and still works against the current JSON schema, but
running it is no longer a required step of process (c), and its output is not filed as a
deliverable alongside the JSON.

Every substantive statement is a **recordable observation** — a discrete record, not prose the
reader has to mine for findings.

**Trace schema, round 2 — structured, occurrence-level, not a flat string.** Round 1's
`traces.verse` was a single string, or (for a grouped observation) several verse IDs joined with
`"; "` — this was flagged as too weak to mechanically tie a verse to a specific observation: parsing
a semicolon-joined string to verify coverage is fragile, and it dropped `span.surface`/`span.morph`
at exactly the point (grouped verses) where a reader most needs to see whether the group is really
uniform. Round 2 replaces it with `traces.occurrences`, always an array (one element for a
single-verse observation, several for a genuinely grouped one), each element carrying the specific
occurrence's own surface and morph so morph stays visible at the point of citation, not only in
Json A:

```json
{
  "tag": "<see tag taxonomy below>",
  "statement": "<the observation, stated positively>",
  "traces": {
    "cluster": "M10",
    "family": "H_guilt",
    "strong": "H0816",
    "occurrences": [
      {"verse": "Lev.4.13", "span_surface": "guilt", "span_morph": "HVqq3cp"}
    ],
    "meaning_source": "strong_meaning_tree",
    "related_cluster": null,
    "related_family": null
  }
}
```

A grouped observation (several verses sharing one reading) lists every one of them as its own
element of `occurrences` — grouping the *statement*, never the *trace*:

```json
"occurrences": [
  {"verse": "Lev.4.13", "span_surface": "guilt", "span_morph": "HVqq3cp"},
  {"verse": "Lev.4.22", "span_surface": "guilt", "span_morph": "HVqq3ms"},
  {"verse": "Lev.4.27", "span_surface": "guilt", "span_morph": "HVqq3ms"}
]
```

- Not every observation connects to every trace field — but **where a trace exists, it must be
  recorded**, not left off for tidiness.
- `meaning_source` is carried for **citation/authorship attribution** back to STEP's own sources.
- Data-error observations use `tag: "data-error"` and are kept in their **own section/rows**, never
  mixed into the meaning-observation rows.

### Per-strong verification block (round 2, required)

Each family's output JSON carries a top-level `strong_checks` array, one entry per strong in the
family, generated by mechanically diffing that strong's `traces.occurrences` (across all
observations) against its full occurrence list in Json A — **not eyeballed, actually computed**:

```json
"strong_checks": [
  {"strong": "H0816", "occurrence_count": 30, "traced_count": 30, "missing_verses": []}
]
```

A family's output is not complete while any `missing_verses` is non-empty — either add the missing
observation(s) or, if a gap is deliberate (e.g. a strong earmarked `no-human-context` before any
per-verse reading), say so explicitly in that strong's own observations rather than leaving a bare
gap in the check.

### Initial tag taxonomy (will develop; each tag traces to a read rule above)

| tag | read rule it implements |
|---|---|
| `instance-meaning` | every instance states what it is |
| `alternative-meaning` | showing likely-or-possible readings, not one distilled meaning |
| `verse-grouping` | similar verses grouped by shared meaning |
| `difference-inference` | a difference or specific inference, recorded separately (morph-driven ones included) |
| `surface-gloss-divergence` | a `span.surface` vs. `stepGloss` mismatch, explored, not just noted |
| `no-human-context` | homonym/name earmark, no further analysis |
| `cross-family` | cross-family observation, anomaly, open question, or cluster pointer |
| `data-error` | a data-quality issue found while reading, unrelated to meaning |

## 4. Data-error flags

Any data-quality issue noticed while reading (wrong cluster membership, a span/verse integrity
problem, a meaning source that looks corrupted) is recorded as a `tag: "data-error"` observation in
that family's output, in a clearly separate section — it is not chased down or fixed as part of
this process; it is a flag for a separate escalation.

## 4A. Process (d) — catalogue question-answering by family (round 3, added 2026-09-11)

**Purpose:** test whether process (c)'s output is a sound base for the characteristic work, by
actually answering the T0–T5 catalogue questions (`wa_obs_question_catalogue`, `status='active'
AND deleted=0 AND tier IN ('T0','T1','T2','T4','T5')` — 64 questions; T3 fully retired, T6/T7
deliberately out of scope for this round) against one family's process-(c) JSON at a time. Always
run **per family**, same discipline as process (c) — never the whole cluster in one pass.

**Input:** a family's process-(c) JSON (observations + strong_checks) plus the full `verse_text`
for every distinct verse it cites (process (c)'s round-2 schema deliberately dropped `verse_text`
to keep the trace compact; process (d) needs it back for the LLM to actually read the question
against, so it is re-joined from process (a)'s JSON at this step, not re-fetched from the DB).

**Core rule — multiple slants, not one distilled answer.** A family groups several related but
distinct strongs (e.g. H_guilt's `enochos`/forensic-liability, `asham`/self-recognized-guilt,
`nasa`/guilt-bearing). Where the family's own strongs or observations point to genuinely different
answers to the same catalogue question, every distinct slant is recorded as its own entry, each
with its own evidence trail — never flattened into one "the characteristic means X" answer. A
single slant per question is the correct output only when the evidence actually is uniform, not a
default.

**Two scope levels in the catalogue itself** (from the `scope` column) govern where a slant's
evidence trail points:
- `Word/term (lexical)` and `Verse-context` — answered against specific observations/occurrences;
  the trail cites the exact verse(s)/span(s) the slant is read off.
- `Characteristic (HIB behaviour)`, `The HIB`, `Other non-human beings`, `Characteristic
  relational` — answered across the family's evidence as a whole; the trail cites which
  strong(s)/observation(s) the synthesis draws on, not just one verse.

**Output schema, one file per family** (`_analytics/Clusters/1682-test-m10-process-d-<FAMILY>-v1-*.json`):

```
{
  cluster_code, family_id, process: "1682-cluster-reading-process-d", spec_round: 1,
  catalogue_scope: "T0-T5", questions_answered: 64,
  answers: [
    {
      question_code, tier, component_code, component_title, question_text, catalogue_scope,
      slants: [
        {
          slant_label,      -- short distinguishing tag, e.g. "asham-self-recognition"
          answer,            -- the actual answer text for this slant
          strong,            -- nullable; the strong(s) this slant is grounded in
          basis: {
            occurrences: [ {verse, span_surface, span_morph, verse_text} ],  -- verse_text restored here
            observation_refs   -- which process-c observation(s) (by tag+leading text) this draws on
          }
        }, ...
      ],
      needs_adjacent_verse_context: [ {verse, why} ],   -- flagged only, not fetched, this round
      cross_family_or_cluster_flags: [ {statement, related_family, related_cluster} ]
    }, ...
  ]
}
```

**Two open defaults set this round, both reversible on researcher direction:**
1. **Adjacent-verse context is flagged, not fetched.** Where answering a question properly would
   need the surrounding verses (context a family's own occurrence-level trace doesn't carry),
   record `needs_adjacent_verse_context` with the verse and why, rather than pulling extra verses
   mid-run. Rationale: fetching ad hoc, un-scoped extra context is exactly the kind of undefined,
   per-question judgment call this whole spec exists to keep out of process (c); flagging keeps the
   scope of a single process-(d) run fixed and auditable, at the cost of a second pass later to
   resolve the flags. If this proves too limiting in practice (too many flags to be useful),
   revisit.
2. **Inter-family/inter-cluster observations are flagged, not resolved.** Where a question's answer
   would benefit from or is contested by another family's material (the existing `cross-family`
   tag/`related_family` field in process (c)'s own output is the main source of these), it is
   surfaced under `cross_family_or_cluster_flags` on the relevant question and left for a later,
   dedicated cross-family round — never silently synthesized across families inside one family's
   process-(d) run.

## 4B. Process (e) — cross-family/cross-round synthesis (round 3, added 2026-09-11)

**Purpose:** every prior process in this spec (a/b/c/d) produces claims scoped to ONE family. The
comparative work of actually reading process (d)'s output back — noticing that H_guilt shows no
constitutional-level engagement at all while B_sin shows a systemic one (mind, body, Rom 7:23),
that the T4.6 spiritual-beings pattern differs three ways across H_guilt/B_sin/G_transgression, or
that Isaiah 53:5 is independently cited by four strongs across three families — has no home in any
family's own file, and was at real risk of surviving only in chat scrollback and an escalation
comment. Process (e) exists to give this comparative layer a durable, traceable, append-only home
of its own, separate from any one family's process-(c)/(d) output.

**This is a third, structurally distinct tier, not a bigger version of (c) or (d):**
- Tier 1 (process a): raw verse/span/morph evidence — immutable, never revised.
- Tier 2 (process c/d): claims ABOUT the evidence, scoped to one family — the observations and
  slant-answers already specified above.
- Tier 3 (process e): claims ABOUT claims — comparative/synthesis findings that reference two or
  more tier-2 items (across families, across rounds, or both) and cannot be filed under any single
  family without losing the point of the finding.

**Output schema, one file per synthesis pass** (not per family —
`_analytics/Clusters/1682-test-m10-process-e-synthesis-<round-label>-v1-*.json`):

```
{
  cluster_code, process: "1682-cluster-reading-process-e", spec_round: 1,
  families_compared: [family_id, ...],
  syntheses: [
    {
      synthesis_id,       -- stable slug, referenceable by a later synthesis or revision
      statement,          -- the comparative claim itself
      status,             -- provisional | corroborated | superseded  (never silently deleted)
      supersedes,         -- nullable synthesis_id this one revises -- the superseded one stays in
                             the file, marked, not removed; history is never overwritten
      grounded_in: [ {family, question_code, process}, ... ],  -- exact process-c/d items this
                             synthesis was read off, so it can always be traced back down to tier 2
                             and from there to tier 1
      revisit_note        -- what would confirm, complicate, or overturn this once more families
                             are read; an explicit invitation to revisit, not a closed verdict
    }, ...
  ]
}
```

**Why this matters for "accumulate with grace, don't get lost, revisited from different angles"**
(researcher instruction, this chat turn): a synthesis finding is written once, and a later pass
that revisits it — from a different angle, a different family added to the comparison, or a
straightforward correction — files a NEW synthesis entry with `supersedes` pointing at the old
one's `synthesis_id`, rather than editing the old entry in place. The old entry is never deleted;
`status` changes to `superseded` but the statement and its grounding remain readable. This is the
one place in the whole spec where the round-2 "edit the spec in place, don't re-version" convention
does NOT apply to the DATA — the spec document itself is still edited in place (it describes the
process), but process (e)'s own JSON output is append-only, because losing the history of how a
comparative claim changed across revisits is exactly the failure this tier exists to prevent.

**Relationship to the findings-table design question (escalation #1682, still open):** this tier-3
distinction is a direct input to that decision — any persistent schema needs a node/table shape
that can hold a claim referencing OTHER claims (not just verses), with a non-destructive revision
mechanism (`supersedes`, not `UPDATE`). See the design doc for the current proposal.

## 5. Governance note

Process (a) is the only scripted/deterministic step. For this test run it is written as a
**temporary script** (`temp_1682_assemble_cluster_json.py`, per `governance.scripts_and_routines`'s
temp-script convention) — pending the researcher's approval of this spec, a promoted version would
be registered in `cfg_utility` (and `cfg_step`/`cfg_write_grant` if it starts writing) per
`governance.new_utility_registration_timing`, rather than staying a one-off script indefinitely.
Processes (b) and (c) are LLM reasoning steps, not code — there is nothing to register for them
beyond this spec itself.
