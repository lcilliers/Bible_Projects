# Verse-analysis Report Architecture — Reframe (working register)

- **Type:** living register · opened 2026-06-30 · **status: OPEN for researcher markup**
- **Why:** the four report definitions (Fanout / _STATE / Verse_observation / Stream_observations) do not yet serve the purpose. Researcher diagnosis: *the fanout method ran to a standstill largely because it was never properly built out.* This register works the reframe through to a coherent, DB-grounded architecture, lists the open decisions, and is the single source the four definition docs will be rewritten from.
- **Rule:** one living doc; decisions logged at the bottom; no parallel docs. The four `wa-report-def-*` files stay frozen until the decisions here are settled.

---

## 1. The diagnosis (from the researcher's comments)
The old fanout failed because it tried to be everything at once and held volatile content:
- it mixed **static lexicon** with **findings/observations/interpretations** — so it went stale the moment any finding changed (cumbersome to keep current);
- it was **hard to read** (codes vs text, over-technical), **incomplete** (extracts without base data), **not referenceable**, **not cross-indexed**, and **didn't pull related verses**;
- you **couldn't tell where a datapoint came from**.

The fix is **separation of concerns**: each report has one sharp job, and the volatile content is pulled *by index at read time*, never baked into a static file.

## 2. What the DB already gives us (grounding — verified 2026-06-30)
| Asset | Table | Rows | Use in the reframe |
|---|---|---|---|
| Evidence index (verse → evidence) | `verse_evidence_index` | 804,805 | the **index backbone**. Types: `lexical` 424k · `span` 306k · `unit` 43k · `finding_verse` 32k. **No logos/chat type yet.** |
| Lemma by verse | `verse_term_index` | 275,593 | related-verse discovery by shared Strong's |
| Full morphology by verse | `verse_span_index` | 305,961 | the Fanout's morphology block; carries `reference`, `surface`, `morph_code`, `stem`, `language`, `strongs`, `primary_strong` |
| Digested findings | `finding` | 435k VERSE | the meaning evidence; already indexed (`finding_verse` / `lexical`) |
| Characteristic grouping | `characteristic` | 199 | the **grouping between cluster (too coarse) and term (too narrow)** — matches the researcher's instinct |
| Observations | `ib_observation` | 81 | the study's captured observations; `operation` = current free-text stream; `provenance` already records `claude-chat` (×2), `mechanical`, `researcher`, `convergence`, … |
| Verse roles | `verse_analysis_progress` | 33 | markers: `Analysis in progress`, `Observation cross referenced`, `Analysed (unit Mark 7:21-23)` — note the **passage unit** already appears here |

**Two facts that drive decisions below:** (a) logos/chat content is **not in the DB** as evidence — only as a provenance label — so indexing it is a real build; (b) the `characteristic` table is the natural home for the "stream/track" grouping.

## 3. The reframed architecture — four reports, layered
Each report has one job and a clean IN/OUT boundary.

### 3.1 FANOUT — static lexicon substrate for a **passage**
- **Is:** the raw, stable lexical picture for a passage (a verse-group; a single verse when no passage applies). The spans and their morphology **by verse**, plus **the related verses discovered by morphology**, with **every datapoint carrying its source reference** (table + key) back to the DB.
- **Includes:** verse text + neighbour window (with `wa_verse_records`/verse reference as the DB anchor); morphology for all spans in the passage (`verse_span_index`); references of **similar verses by morphology** (`verse_term_index`); section headers naming their **source table**.
- **Excludes (hard rule):** findings, observations, ve narrations, logos, AI-chat — *no volatile or interpreted content.* This is what keeps the fanout stable and cheap to keep current.
- **Anchor recursion:** when a related span points to a verse that has **no anchor yet**, an anchor verse must be designated so its fanout can be built in turn (see DEC-3).
- **Versioned** (`-vN`, bump-on-change). Because content is static lexicon, versions move rarely.

### 3.2 PASSAGE_OBSERVATION — the working / review document *(renamed from Verse_observation)*
- **Is:** the digested, **index-driven** picture for a passage: **all observations by characteristic** for the passage, **plus all DB evidence** (findings, logos, chats, lexical) for **every verse in the passage** — assembled from `verse_evidence_index`/`verse_term_index`, **not full-text scans**.
- **Role:** this is the **working document the researcher reviews and comments on**; each comment then either becomes a **DB entry** or is **written back into the report**. It is the round-trip surface between reading and the DB (see DEC-6).
- **Depends on:** the logos/chat indexing build (DEC-5) for the logos/chat portion; observations-by-characteristic depends on DEC-4.

### 3.3 CHARACTERISTIC_OBSERVATION — narrative rollup *(renamed from Stream_observations)*
- **Is:** all observations for **one characteristic** collated **across all verses**, **converted to a narrative**. The place a focus point is actually seen.
- **Grouping:** the `characteristic`, not the free-text stream (DEC-4).
- Living page, regenerated on demand.

### 3.4 _STATE — mission control (unchanged)
- The whole-study single page; already DB-generated and serving. No change beyond linking out to the three reports above once they exist.

## 4. Naming changes proposed
- `Verse_observation` → **Passage_observation** (the unit is a passage).
- `Stream_observations` → **Characteristic_observations** ("stream/track" retired as a pervasive new concept; the grouping is the characteristic).
- Fanout and _STATE keep their names.

## 5. Open design decisions (please mark up — recommendation given, but your call)

- **DEC-1 · What delimits a passage?** A passage is sometimes a verse-group (Mark 7:21-23), sometimes a single verse. *Recommendation:* a passage is an **explicit declared unit** (stored once, e.g. in `verse_analysis_progress` or a small `passage` table); absent a declaration, the unit is the single verse. *Open:* who declares it and how (manual vs morphology-suggested)?

- **DEC-2 · Related-verses-by-morphology rule.** What makes another verse "related" for the fanout? *Recommendation:* the floor is **shared primary Strong's (lemma)** via `verse_term_index`; optionally tighten by stem. *Caveat to accept explicitly:* this is an **index, not a census** — it leaks (homonyms, orphans) and is not provably complete. Do we (a) accept the lemma floor and flag completeness as known-partial, or (b) add a second discovery channel?

- **DEC-3 · "Anchor verse" — definition + mechanism.** *Proposed:* an anchor verse is the verse designated as the analytical owner of a span/lemma occurrence. When the fanout reaches a related occurrence whose verse has no anchor, we **register it as a pending anchor** (in `verse_analysis_progress`) so its own fanout can be built. *Open:* auto-register pending anchors, or queue for researcher approval?

- **DEC-4 · Stream → characteristic.** Adopt the `characteristic` table (199 rows) as the grouping for observations. *Requires:* mapping each `ib_observation.operation` value (ruthlessness, cruelty, heart…) to a `characteristic` (id), or replacing `operation` with a `characteristic_id` FK. *Open:* map existing free-text now, or run them in parallel until the mapping is verified? And do the 8 current streams map cleanly onto existing characteristics, or are new characteristic rows needed?

- **DEC-5 · Logos/chat indexing build.** Logos and AI-chat extracts are **not in the DB** (only a provenance tag). To put them in Passage_observation they must be **ingested and indexed** (new `verse_evidence_index` types `logos`/`chat`, or a `contributor_evidence` table, with a keyword index). *Open:* where do the current logos/chat extracts physically live (which markdown), and is the ingestion in scope now or deferred (Passage_observation ships findings+lexical first, logos/chat second)?

- **DEC-6 · Review-comment round-trip.** Passage_observation is the comment surface; responses become DB entries or are written back. *Open:* where do comments live — a DB `review_comment` table keyed to verse/observation (durable, queryable), or inline in the report doc (simpler, but text that can rot)? *Recommendation:* DB-backed comments, rendered into the report, resolved back to the DB — consistent with "all work in the DB."

- **DEC-7 · Readability rules (all reports).** Plain language; **every code shown with its gloss/translit** (never a bare code); text-first, codes in parentheses. Adopt as a presentation standard?

- **DEC-8 · Source-reference on every datapoint.** Each line/section cites its **source table + key** so any datapoint can be traced back and corrected. Adopt as a hard rule across all four reports?

## 6. Sequence once decisions land
1. Rewrite the four `wa-report-def-*` docs from this register (clean, no open questions).
2. Build in dependency order: **Fanout** (lexicon only — smallest, unblocks reading) → **Characteristic_observation** (needs DEC-4) → **Passage_observation** (needs DEC-4 + DEC-5 + DEC-6) → _STATE link-out.
3. Pilot on one passage (Exo 1:13 or Lev 25:43, which already have the most data) before scaling.

## 7. Decision log
- 2026-06-30 — register opened from the researcher's comments on the four definition docs. DB grounding verified (§2). Awaiting researcher markup of DEC-1…DEC-8.
- 2026-06-30 — **researcher resolved DEC-1…DEC-8** (comments §below). Resolutions recorded in §8; prerequisite rebuilds in §9; remaining open items in §10. Next: update the three specs + produce a sample report for each (researcher item 11).

## 8. Resolved decisions (2026-06-30)
- **DEC-1 — Passage = a group label on the verse record.** Add a grouping column to `wa_verse_records` (e.g. value `Exo 1:1-14`); every member verse carries the same label → easy pairing. **Delimiting happens *during* fanout reading** — the researcher decides then whether a group should split into separate fanouts. **Driver:** the verses that form the *end-to-end story for the characteristic*.
- **DEC-2 — Related verses = `verse_term_index` (shared primary lemma); anomalies accepted.** No second channel; the index leak is a known, accepted limit.
- **DEC-3 — Anchor verse: fanout-triggered.** Use an existing anchor where one exists; else one is chosen (as before). **The fanout itself triggers the process:** when it raises a missing anchor and cannot auto-select, a checking-possibilities step runs. **An anchor may later change — the repercussions of a change must be understood and handled** (downstream rebuilds of dependent fanouts/links).
- **DEC-4 — Adopt `characteristic` as the grouping; embed it into the fanout build.** Retire free-text "stream/track". **Prerequisite: rebuild the affected tables** (see §9). Other rebuilds may also be pending.
- **DEC-5 — External extracts (Logos / AI-chat / other): full-capture + portion-index.** These corroborating documents are *not* DB-shaped (not single-element, inconsistent refs). **Capture them in full in secured folders.** Then **index/cross-reference *portions* of them to the corpus (verses + keywords)** — retrieval must be by **index, never a scan of all documents**. Volume is small now but expected to grow substantially. The evidence index (§comment 1) is extended to include these external extracts.
- **DEC-6 — Comments route by kind.** A comment about a **verse or characteristic** → becomes an **observation or finding** (DB). A comment about **process/workflow** → filed to the appropriate `Workflow/` folder. No separate comment table.
- **DEC-7 — Readability adopted** (codes always with gloss; text-first). Researcher will add more presentation comments later.
- **DEC-8 — Source-reference: selective, not blanket.** Tracing every datapoint can overwhelm. Apply where it is *appropriate* (to be pinned per report section), not universally.

## 9. Prerequisite rebuilds (before the characteristic-grouped reports can generate)
1. **`wa_verse_records` grouping column** (DEC-1) — add `verse_group` (or similar); back-fill nothing until reading assigns groups.
2. **Stream → characteristic mapping** (DEC-4) — map the 8 current `ib_observation.operation` values onto `characteristic` rows (match existing of the 199, or add new), then switch observations to a `characteristic_id`. Run old + new in parallel until verified.
3. **Term → characteristic path** (DEC-4) — confirm/derive `primary_strong → characteristic` (via `mti_term_subgroup → cluster_subgroup → characteristic_subgroup → characteristic`) so the fanout build can embed it per span.
4. **External-extract store + portion-index** (DEC-5) — secured folder for full docs + an index table linking doc-portions to `verse_id`/keywords + new `verse_evidence_index` evidence type.
5. **Rebuild audit** — enumerate any *other* pending rebuilds the above expose (flagged by researcher; to be listed before building).

## 10. Remaining open items
- **#12 — Fanout related-verse visualisation.** The list of verses carrying the primary lemmas needs the right visual treatment (esp. high-frequency lemmas like `abad` = 260 vs `perek` = 6). To be worked in the Fanout sample.
- **DEC-7 — further presentation rules** (researcher, later).
- **DEC-8 — where source-referencing is appropriate** (to pin per section).
- **_STATE** — researcher will reconsider once the other three settle.

Researcher comments.
Thanks for this document and the summary, it makes it easier to think it through.
1. Evidence index:  this should include the external extracts dumped into the corpus via logos bible research, Chat or other means.
2. DEC-5 Unstructured reports/extracts: These reports will mostly not be about one single element, have proper references, or be consistent in the same way that the DB expect - these are documents that corroborate or add to the corpus findings. The must be captured in full in folders to secure the docs. I am not sure how to ease relevance for specific observations or findings, but somehow we must get a method to index or cross reference portions of it in the corpus. This cannot depend on a scan of all the documents. I know there are now only a few, but I expect that it would increase substantially.
3. DEC-1  I suggest we add a column in verse-record that can serve as the grouping (perhaps something like Exo 11-14) and each member of the group carries the grouping. This allows for easy paring. Delimiting will take place during fanout reading. At this point I will make the decision of a verse group should be split into separate fanouts.  The main driver for it is the verses forms the end to end story for the characteristic.
4. Dec-2 Agree - verse term index and accept that there will be anomolies.
5. Dec-3 Agree, in some cases an anchor verse already exists, if not it should be chosen, similar to the process it was chosen in the past. Agree with your process. on the open question.  I was expecting the fanout to trigger this process. for instance, when the fanout raise a missing anchor, and cannot select one, then we go through a process of checking possibilities.  Be aware that the Anchor may change, repercussions of this must be understood.
6. DEC-4 yes switch the characteristic and imbed this table into the fanout build.  Rebuild of current tables for it is a prerequisite (there may be other rebuilds also pending.)
7. DEC-6  Comments about verses or characteristics becomes observations or findings; comments about process or workflow is filed to the folders in workflow where it belongs.
8. DEC-7 agree, I want to make more comments on presentation. later.
9. DEC-8 this can become overwelming.  lets think about where it is appropriate.
10. I will think through _state when the other reports settled down
11. Update the specs and produce a sample report for the three reports.
12. the fanout must deal with the list of verses that carries the primary lemmas, but I am concerned about it - need more thought to get the visualisation correct.  


Next round of comments:
looking at the fanout example. If I get this report cold, as is - I will not discover a fraction of the observations that came out of Exo 1:13 previously.  The real value was in reading verses that had no direct reference. If I remember correctly those came out of the logos and chat reports. how will those verses become part of the fanout. Should they be part of the fanout. There is something missing, not sure what.

---

## 11. The missing channel — conceptual relatedness (CC response, 2026-06-30)
**The researcher is right: a cold lexical fanout loses most of the value.** Empirical proof (verified): the structured lexical web for `perek` H6531 contains exactly one related term — `pa.ro.khet` "curtain" (H6532), a spelling-neighbour. There is **no lexical path** from ruthlessness to Gen 6:5 ("evil thoughts of the heart", *machashavah* H4284) or Jer 17:9 (deceitful/incurable heart) — yet those produced the richest observations (#42, #109, #110). They came from **Logos / AI-chat conceptual inference**, and were never captured as first-class links — so a re-read goes cold.

**"Related verses" has three channels; the fanout currently has only A:**
- **A — same lemma** (`verse_term_index`): exact recurrences. *perek* → 6 verses. ✓ present.
- **B — related lemma** (`wa_term_related_words`, STEP relatedNos): lexical neighbours. *perek* → only "curtain". **Proven near-useless for conceptual reach.**
- **C — conceptual cross-reference** (Logos / AI-chat / scholarship / researcher): cross-vocabulary leaps. *perek* → Gen 6:5, Jer 17:9. **Where the value was. Not derivable from any index.**

### DEC-9 (PROPOSED — awaiting researcher confirmation)
1. **Relatedness becomes a stored, provenance-tagged verse-to-verse link** — a `verse_relatedness` store: `from_verse · to_verse · channel(A/B/C) · concept/keyword · provenance(logos|chat|scholarship|researcher) · source-portion pointer`.
2. **The fanout's "related verses" section draws from all three channels**, each tagged by channel + provenance + pointer. A captured channel-C link makes a cold fanout list Gen 6:5 ("conceptual source: heart's evil, from chat/logos → read"). **They belong in the fanout as links with provenance, NOT as imported meaning** (meaning stays in observations).
3. **DEC-5's portion-index IS channel C.** The primary value of a Logos/chat doc is the verse cross-references it asserts; indexing a contributor doc = extracting those links. DEC-5 and this missing channel are one build.

### The honest limit (consistent with the 2026-06-30 close-down reckoning)
The fanout can *hold and replay* channel-C links cheaply, but **producing** them — the conceptual leap — is contributor/human work, not auto-derivable. This names a workflow step not previously explicit: a **conceptual-expansion pass** per anchor verse (Logos relatedNos deeper + AI-chat conceptual pass + researcher reading) whose *output* is captured as channel-C links + portion-indexed evidence. The fanout accumulates; the pass fills it. A never-expanded verse has a lexically-complete but conceptually-thin fanout until the pass runs. Judgement stays with the researcher/contributors; the fanout ensures the discovered links are never lost to a cold re-read.

### Impact on prior decisions (if DEC-9 confirmed)
- **Fanout spec §3.3** changes from single-channel (lexical) to **three-channel related-verses**.
- **§9 prerequisite rebuilds** gains: the `verse_relatedness` store (merged with the DEC-5 portion-index — same build).
- **#12 visualisation** now spans three channels (lexical sets can stay collapsed by count; channel-C links are few and always shown — they are the point).
- **DEC-3 anchor recursion** now fires from channel-C targets too (a conceptual verse with no anchor → candidate).
