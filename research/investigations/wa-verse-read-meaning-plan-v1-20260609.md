# Verse-read = meaning process — assembly + division of labour (v1)

> Plan for the L2 "verse read" that derives **meaning per term-in-verse**, mechanical-first, AI where the
> mechanical outcome is inadequate. Builds on the rolled-out 5 mechanical fields (sense-branch · kind · mode ·
> co-occurrence · location), the verse-complete writer, the typed-relationship ontology, and the read-dedup.
> Governing memories: term-corpus-anchors-meaning · phase-a-light-meaning-at-vcg · l2-mechanical-api-triage ·
> clarifications-reusable-but-state-not-induce · ontology-typed-relationships · l2-writer-verse-complete.

---

## 0. The unit and the principle

- **Unit of the read = the VERSE** (read once), producing **per-term-in-verse meaning findings**
  (verse-complete — every in-scope term in the verse is resolved in the one read, each saved to its own
  cluster; augments + corrects existing findings).
- **Meaning is derived by reading the actual verse in context, term-corpus-anchored** — never cold
  per-verse, never term-uniform. The mechanical fields are the *scaffold + triage input*, not the meaning.
- **Mechanical is the default; AI is the exception.** Triage decides per verse. State-not-induce: if the
  verse doesn't resolve a field, it is **STATED silent/unresolved**, never guessed.

---

## 1. Data assembly — what CC builds (all from the DB, no AI)

For each verse, CC assembles a **read packet** (one packet covers all in-scope terms in that verse):

| block | content | source |
|---|---|---|
| **Verse** | reference · full verse_text · context_before/after | `wa_verse_records` |
| **Terms-in-verse** | for each in-scope term: strongs · transliteration · gloss + **all sense options** · morph_code + stem · the mechanical **sense-branch** chosen · the 5 mechanical field values | `mti_terms`, `wa_meaning_sense`, `verse_context`, existing l2 findings |
| **Relational context** | co-occurring terms + their clusters in this verse · **sibling spans** (span-pairing) · the typed-thing candidates | `verse_context` co-occurrence array, span links |
| **Corpus anchor** | a small sample of the term's other verses for the same sense (so the read is corpus-anchored, not cold) | `verse_context` for (term, sense) |
| **Existing findings** | old Session-B findings + new l2 findings already at this verse — to **augment/correct**, not duplicate | `finding` + `finding_verse_link` |
| **Fields to fill** | the verse-grounded tier fields (the extraction record: sense · type · mode · location · origin · faculty · attributed-to-God · produces · response · direction · co-occurrence) | catalogue refit (.1 verse-grounded subset) |

Assembly is **two-tier** (from the read-dedup):
- **Tier A — per (term, sense):** the *invariant* meaning (base sense, nature, faculty). ~1,940 (term,sense)
  groups; read **once**, applied to all member verses. **93% of reads saved.**
- **Tier B — per verse:** the *context* fields + the **typed relationship** `A[type] —rel[effect]→ B[type]`.
  Read once per verse, written for all its terms.

---

## 2. What CC handles itself (mechanical — no AI, no cost)

1. **Sense-branch** from morph→stem→BDB (already backfilled & applied).
2. **The 5 solid fields** — kind · mode · co-occurrence array · location · lexical sense (already rolled out).
3. **Read-once dedup** — compute Tier-A invariant fields once per (term, sense), fan out to members.
4. **Triage** — judge the adequacy of the mechanical outcome → **ACCEPT / ESCALATE / RESEARCHER**.
5. **DB writes** — verse-complete, idempotent de-dup, each term to its own cluster; **STATE silent/unresolved**
   where the verse doesn't resolve a field.
6. **Batch assembly + result application** — build the AI batches, parse AI returns into findings.

**Triage = ACCEPT (mechanical, most verses)** when the outcome is simple/clean: single clean sense, no
interaction, no ambiguity. **ESCALATE (→ AI)** on any adequacy signal:
- unresolved multi-sense / **broad-gloss polysemy** (pneuma wind/breath/spirit; the >100 suspect groups)
- shade / valence ambiguity the corpus doesn't settle
- interacting term array / type conflict in the verse
- homonym · sibling-span pairing · relevance doubt
**RESEARCHER** when CC genuinely cannot judge adequacy.

---

## 3. What goes to AI (the ESCALATE set only — the exception)

AI receives the **read packet** (verse + corpus-anchored term context) and returns, **for the escalated
term-in-verse**:
- the **resolved sense** (picks the branch the mechanical pass left ambiguous)
- the **verse meaning** read in context (compound/interacting verses)
- the **typed relationship** `A[type] —rel[effect]→ B[type]` (the ontology prize — the differential of impact)
- **faculty (T3)** where lexical meaning is ambiguous (held from the mechanical rollout)
- any **reusable clarification** it applies (disambiguation rule that reads a present signal — never induced)

**AI channel:** **chat batches by default** (one-shot read/classify, cheaper, fits the small-chunks
preference); **API only** for atomic high-volume that won't fit a chat batch. Researcher gate for the
unjudgeable.

---

## 4. Sequence + review gates

1. **M01 (Fear) first** (active rework phase). Assemble packets → mechanical pass → triage.
2. **CC-accept** the clean majority; **batch the ESCALATE set to AI**; **researcher-gate** the unjudgeable.
3. **Two researcher review gates** bracket the AI step (before sending; after applying) — the L1/L2 cycle is
   iterative and failure-prone, verse meaning is the gravest risk.
4. Write findings (verse-complete) → **roll up** to cluster findings → review → next cluster.

---

## 5. Decisions — CONFIRMED 2026-06-09

- **D1 — AI channel = API**, used **where CC cannot do the synthesis/analysis** (not a fixed input rule —
  a judgement on whether CC can form the meaning/resolve the tier). CC attempts first; API is the fallback.
- **D2 — Faculty (T3) IN**, and written as its **own separately-identifiable verse finding**. General rule:
  **every tier element is its own finding** — individually identifiable, never bundled.
- **D3 — M01 (Fear) end-to-end first.**
- **D4 — ESCALATE + SELF-AUDIT.** Escalate on inadequacy AND, once the meaning paragraph is formed,
  **audit it back**: every finding element + tier question must be represented in the paragraph.

---

## 6. The meaning paragraph

- **Verse meaning = a prose paragraph that collates the answered tier questions into one coherent statement,
  set in the verse's context.** It is the synthesis *on top of* the tier findings — not a replacement.
- **The individual tier findings stay separately identifiable** — one `finding` per tier element per
  term-in-verse (sense · kind · mode · location · origin · faculty · attributed-to-God · produces · response
  · direction · co-occurrence …), each linked to its catalogue question.
- **Storage:** the paragraph is itself a **VERSE-level `finding`** for the term (provenance `l2_meaning`,
  its own synthesis question), distinct from the tier-element findings (`l2_mechanical` / `l2_api`).
- **Who writes it:** CC **collates** the paragraph from the findings for ACCEPT verses; **API** writes it
  where CC cannot do the contextual synthesis/analysis (ESCALATE).
- **Self-audit (per verse):** after the paragraph is formed, CC checks **every tier-element finding and tier
  question is represented** in it; gaps are flagged (and re-run / escalated), never silently dropped.

---

## 7. Process control — term by term, batched, engine-logged

**Loop shape:** outer = **TERM**; inner = the term's verses in **manageable batches**.

```
RUN (M01)                          → engine_run_log row (mode='verse_read_meaning', resume_from)
  for each TERM in M01:
    checkpoint OPEN                 → engine_stream_checkpoint (stream_name='term:<strongs>', started_at)
    for each BATCH of its verses:
      assemble packet → mechanical tier findings (separately identifiable)
      form meaning paragraph (CC collate | API where CC can't)
      per-verse SELF-AUDIT: every finding element + tier question in the paragraph?
      write findings + paragraph (verse-complete, idempotent); STATE silent where unresolved
      checkpoint UPDATE             → rows_written += , last_strong, status='in_progress'
    per-TERM SELF-AUDIT: all verses processed? all expected findings present? 
    checkpoint CLOSE               → status='complete' | 'review' , completed_at, error_detail
  RUN close                        → engine_run_log.completed_at, outcome
```

- **Timestamps** on every cycle (term + run) → completion control + a read on where processing stalls,
  falls over, or restarts.
- **Resumable:** on restart, skip terms whose checkpoint is `complete`; resume the first non-complete term
  from `last_strong` / batch offset.
- **Per-term self-audit gate:** a term is not `complete` until all its verses are processed and every
  expected tier finding (+ meaning paragraph, + self-audit pass) exists; otherwise `review`.
- **Cost:** mechanical-accept is the default and free; API only on ESCALATE / where CC cannot synthesise.

*This is expected to be the largest single task of the study — the control scaffold is built for scale,
stall-visibility, and clean resume from the start.*

---

## 8. Term-kind scoping — T2, FLAG, and the participation gate (GOVERNING, 2026-06-10)

The buckets are not characteristics. Handle by **kind of term**, not by cluster code
([[feedback_t2_reference_flag_reclassify]]).

- **M-clusters = the characteristics (the *what*)** — the only **drivers** of the verse-read.
- **T2 = a REFERENCE (qualifiers / the *how*)** — **never analysed on its own.** A T2 term is engaged only
  where an M-cluster verse uses it, and its meaning is **embedded in that cluster term's analysis, NOT
  recorded as a standalone T2 finding.** → The CC-mode must **not write T2-routed paragraphs**; instead the
  read must fold the qualifier's implication into the co-occurring characteristic's meaning (co-occurrence
  array + `compound` field + the prose, as already evidenced bidirectionally). The existing 945 standalone
  T2 paragraphs are out-of-rule → **retire (reversible) when CC-mode lands.**
- **Corroboration (verified, 1063/1063).** A T2 term is read **only** in verses that contain an inner-being
  characteristic; **never** drive T2 to interpret a qualifier's purely-physical verses.
- **Participation gate.** Within a corroborated verse, persist meanings only for terms that actually
  participate in the inner-being content; **skip bystander terms** (pure particles `et`; repeated social
  terms `am`) — ~15% self-declare "no inner faculty engaged."
- **FLAG = a holding pen, the opposite case.** A FLAG term that **carries inner-being meaning belongs in a
  CLUSTER** — it is no longer FLAG. Triage each to its home; where **no home exists, open a debate** (the
  heart/soul/flesh constitutional *seats* likely need a home of their own).
