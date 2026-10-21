# Two-narrative rollout method — base source → reading + story, per family, per book (v1, 2026-07-12)

> **Authoritative, preserved process** for producing the two-narrative deliverable across the remaining books. Proven end-to-end on **Psalms (46/46 families, 2,048 records)**. This generalises that run so any book can be rolled out the same way. Companion voice spec: [`wa-narrative-style-instruction-v1-20260702.md`](wa-narrative-style-instruction-v1-20260702.md). Method substrate: [`wa-verse-analysis-method-v1-20260702.md`](wa-verse-analysis-method-v1-20260702.md) + the ve-lexical catalogue. Worked completion + lessons: `Workflow/Sessionlogs/wa-session-log-20260712-psalms-narratives-rollout-complete.md`.

## 0. What this produces

For each **family** in a book, one deliverable file pair keyed by anchor reading:

- `…/<book>/_narratives/<book>__<family>__narratives.json` — the transport (DB-bound).
- `…/<book>/_narratives/<book>__<family>__narratives.md` — the readable rendering.

Each **record** = one **anchor reading** and carries **two narratives**:

- **`narrative`** — the RAW / analytical read. Walks every dimension 101–116 (incl. absences), traces source→operation→target→coupling→effect, keeps the lens on the human inner-being process, reads descent at full weight. May use study terms / dimension labels. This is what a reviewer backtracks.
- **`story`** — the SAME content retold as flowing prose for a **general English reader**. Vivid, plain, **zero study jargon** (no dimension numbers, no `ve_lexical`/`ib_char`/`coupling`/`locus`/`bearer`/`from_span`/`to_span`/`internal:`/`external:`, no Hebrew transliterations). It must say what `narrative` says, only plainly.

Both narratives are required on every record. **The full record contract lives inside each base source at `meta.WORK_CONTRACT.output.record_shape`** — that embedded contract is authoritative; this doc is the operating procedure around it.

## 1. The three stages

### Stage A — Build the base source (deterministic; a script, no AI)

One base source per family, in passage-node form, with the **WORK_CONTRACT embedded in `meta`** (objective, `narrative_directives` 1–10, `dimension_frame` 101–116, `worklist`, `reading_map`, `scope_counts`, completeness + backtracking rules). Each `passages[].lexicals[]` row = one reading carrying its `dimensions[]` (values; `present:false` = no row; value `"none"` = reader explicitly found none) and `ve_lexical_ids`. Anchor/dedup is applied here: identical structured readings collapse to one anchor; repeats carry `same_as`; `meta.reading_map` surfaces each item's distinct readings.

```
python scripts/_produce_family_passage_base_source_v2_20260712.py --book <book_id> --family <slug>
python scripts/_produce_family_passage_base_source_v2_20260712.py --book <book_id> --all
```

**Generalising beyond Psalms:** the generator already takes `--book <book_id>` and reads `ib_characteristic WHERE book_scope=<book_id>`. Before the first non-Psalms run, parameterise its two Psalms-hardcoded lines: the `OUT` directory (`verse-analysis/psalms/_base-sources`) and `meta.('book','Psalms')` — drive both from `--book` (map book_id→name via the `books` table, and a per-book output root `verse-analysis/<book>/…`). Keep the same file/folder shape per book.

### Stage B — Generate the two narratives (AI; one worker per family)

**One subagent per family.** Give it the base source path and tell it to obey the embedded `meta.WORK_CONTRACT` exactly. The subagent reads the base source (+ the voice spec + one completed family as a template) and writes the `…__narratives.json` file. Nothing else.

Non-negotiable prompt clauses (these were learned the hard way — see §4):
- **"You are ONE worker. Do NOT spawn or wait for any other agents. You personally read the file and write the output."**
- Granularity: **one record per ANCHOR reading** (a `lexicals[]` row without `same_as`/`duplicate`); duplicates are cross-referenced in `recurrences`, never re-narrated. Record count MUST equal `meta.scope_counts.distinct_readings`.
- Interpret **every** dimension incl. absences; **silence is evidence**. Trace the full process. Keep the inner-being lens. **No valence bias** — read descent at full weight. Ground every claim; cite `ve_lexical_id`s; no imported theology.
- Write **UTF-8**, straight ASCII quotes/punctuation. Do NOT run the renderer or git.
- Self-check before finishing (count, coverage, both narratives, citations, no jargon), then report the record count + `distinct_readings` + file path in a short message.

### Stage C — Render, gate, commit (deterministic + a human-verifiable gate)

```
python scripts/_render_narratives_to_md_20260712.py --family <slug>          # json + passage text -> readable md
python scripts/_check_family_narratives_20260712.py --family <slug>          # the GATE (exit 0 = clean)
python scripts/_check_family_narratives_20260712.py --all                    # whole-book sweep
```

**The gate is mandatory before commit.** It checks: every anchor reading present exactly once (no missing/unknown/dup), record count == `distinct_readings`, both `narrative` and `story` non-empty, citations non-empty, and a **story jargon gate** (compound/underscore tokens + the `(101)`–`(116)` dimension-number pattern; ambiguous common words like "sense"/"effect" are deliberately NOT flagged — they occur naturally). Only after the gate passes: render is up to date, then commit the family (`.json` + `.md`) with `session YYYYMMDD: …`. **Commit incrementally, one or two families per commit** — do not batch the whole book into one commit.

(Note both Stage-C scripts are currently dated/Psalms-pathed; when generalising, either add a `--book` path root or copy them per book. Keep the gate logic identical.)

## 2. The record shape (for reference — the base source's copy is authoritative)

```json
{
  "reading_id": "H0982:trust#1", "char_key": "H0982:trust", "ib_char": "trust",
  "anchor_ref": "Psa 9:10", "passage_ref": "Psa 9:1-20",
  "narrative": "…analytical read, dimensions 101-116, cited…",
  "story": "…same content, plain English, zero jargon…",
  "citations": [7690811, 7690812],
  "recurrences": [],
  "variation_note": "…why this reading differs from the item's other readings (directive 10); '' if n/a"
}
```
Top level: `{"meta": {"family","base_source","generated","narratives_count"}, "narratives": [ … ]}`.

## 3. Model & cost guidance

- Stages A and C are **plain scripts** — zero model cost. Do them yourself, not via agents.
- Stage B is the only AI cost. The writing is analytical but **well-specified with a mechanical gate**, so it is a strong candidate for **Sonnet** rather than Opus. Recommend running the family workers on Sonnet (set `model: 'sonnet'` on the Agent call), reserving Opus only for families that fail the quality bar on review. Never use fable for this (cost).
- Scale the fan-out to concurrency limits; each family is independent. Expect a family to cost roughly proportional to its `distinct_readings` (Psalms ranged ~90k–290k tokens/family on Opus).
- **The "one worker, no spawning" clause is also a cost control** — it prevents the rogue-fragment blow-up in §4.

## 4. Known pitfalls (from the Psalms run)

1. **Agent context corruption on the largest families.** The first trust-refuge (77-reading) worker hallucinated a coordinator role, spawned 6 rogue fragment sub-agents (throwaway scratchpad files, ~900k tokens wasted), and never wrote the deliverable. Fix: the "ONE worker, do NOT spawn agents" clause up front; if a worker's final message doesn't match the task or the file is absent, **abandon it and re-dispatch a fresh clean agent** rather than resuming the confused one.
2. **Verify the file actually landed.** A worker can report success without writing the file. Always confirm the JSON exists and run the gate before believing it.
3. **Base-source data check — coupling(112)/locus(116) transposition.** In Psalms, 666/2,168 rows (all families, onset at Psa 89) had 112 and 116 swapped in the export. Narratives were unaffected (workers read by content), but **run a quick 112/116 sanity scan per book** and file any transposition as a data note (see `outputs/markdown/validation/wa-psalms-base-source-coupling-locus-transposition-v1-20260712.md`); fix at the base-source/DB level before any programmatic load.

## 5. Downstream (open loops, same for every book)

- **Narratives → DB.** The WORK_CONTRACT names the DB as the ultimate destination (JSON = transport, `.md` = view; "all study work in the DB"). A patch-to-DB step per book is outstanding — define once, reuse.
- **Cross-term / cohabitation layer.** Single-family stories are the input; the cross-term story (voice spec §3b) is built after a book's single-family narratives are complete.
