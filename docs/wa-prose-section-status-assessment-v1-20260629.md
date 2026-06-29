# prose_section — status assessment

- **File:** docs/wa-prose-section-status-assessment-v1-20260629.md · 2026-06-29 · read-only assessment.
- **Question (researcher):** what is the state of the prose store, and *when do we "shake it out"* for the fan-out method? Stated lean: *"perhaps first do more work just using `_STATE`."*
- **Source:** live query of `prose_section` / `prose_section_type` / `prose_section_fts`.

## 1. Headline
- **396 active sections · ~1,683,834 words** · 0 deleted. Status: **279 approved · 106 draft · 11 archived**.
- **The mechanism is excellent and fully reusable. The content is entirely legacy-method.** Newest substantive content 2026-06-21 (cluster-findings synthesis); nothing in the store was written for the verse-fanout method.

## 2. What's in it (by stage)
| stage | sections | ~words | newest | what it is |
|---|---|---|---|---|
| **session_a** | 120 | ~910k | 2026-05-02 | per-word STEP/word-data dumps (the bulk; raw legacy material) |
| **findings** | 136 | ~473k | 2026-06-21 | characteristic + cluster syntheses (`cf_char_synth` 124, `cf_cluster_synth` 11) |
| **session_c** | 43 | ~234k | 2026-05-27 | Session C v2 chapters (per-cluster publication drafts) |
| **essay** | 11 | ~34k | 2026-06-20 | **cluster essays** (general-reader products — M01–M09, polished) |
| **programme** | 61 | ~33k | 2026-04-29 | programme/governance prose (mission, scope, method, instructions) |
| **session_b** | 25 | 0 | 2026-04-28 | Stage-2c headings (empty bodies) |

## 3. The mechanism — KEEP (it is exactly what the story layer needs)
`prose_section` is a mature, well-built store:
- **Typed** (`prose_section_type` — code/label/lifecycle/source_stage/chapter_no/sort_order).
- **Versioned in place** — `supersedes_id` / `superseded_by_id` proven in the data (e.g. M05 essay: 2 archived → 1 approved). Prose evolves with history, not by spawning files.
- **Full-text searchable** (`prose_section_fts`, FTS5).
- **Status workflow** (draft → approved → archived; author / approved_by / approved_at).
- **Linkable** (cluster_code 190 · characteristic_id 124 · registry_id 145).

This is precisely the engine the **STORY layer (D2)** would ride on — nothing new needs building structurally; only **new section types** for the new unit of work.

## 4. The content — legacy-method; superseded structure, transferable substance
- The content is organised by the **pre-RESET frame** — M-clusters, characteristics, **tiers T0–T7**. That frame is **CLOSED** (the 2026-06-25 RESET: characteristics → movements/emergence). So the prose's *structure* is superseded.
- But the prose is **not junk**: it is high-quality, evidence-grounded writing (e.g. M06 *"The Two Edges of Hatred"*, M01 *"The Many Faces of a Single Trembling"*). It is **already-digested legacy insight** — the same asset the fan-out already mines (the Lev 25:43 raw pull used the M01-A characteristic definition; the M06 hatred material bears on the ruthlessness track).
- **So treat it as a mineable asset, not a migration target.** Do not rewrite or restructure it into the new model; pull from it when a fan-out track needs what a cluster already digested.

## 5. Relevance to the fan-out method
- **As a source:** the cluster essays + syntheses are pre-written digests of the old method, keyed by M-cluster — directly minable per track (M06→ruthlessness, M01→fear-of-god, M08→pride, M16→folly, etc.). This already happens informally; the FTS makes it searchable.
- **As a template:** the mechanism *is* the model for the new STORY layer — when revived, the fan-out story is just new section types in the same store.

## 6. When to "shake it out" — recommendation: NOT YET (confirms the researcher's lean)
**Defer the prose revival. Keep working with `_STATE` and let observations accumulate.** Reasons:
- The story layer earns its keep only once there is **a story to tell** — i.e. a track/focus-point that has *converged* into something worth a readable digest. We are mid-fan-out; most tracks are still WIP.
- Building the readable layer now would add complexity during a reduction — the opposite of the goal.

**The trigger to revive (proposed):** when the **first focus point converges** — a candidate is the **ruthlessness** track once Eze 34:4 + the heart (#42) + cohabitation (#108) land, and "what the absence of the fear of God lets emerge" is ready to be *narrated*. At that point:
1. add new section types — `track_story` (focus-point narrative), `verse_reading`, and the contributor-source types `src_logos` / `src_aichat`;
2. write the first track story there (DB-canonical, versioned), **leaving all legacy prose untouched** (it stays a mineable asset, clearly a different stage);
3. never migrate the 1.68M legacy words wholesale — mine, don't move.

**Until then:** `_STATE.md` is the control surface; `ib_observation` is the atom store; the prose store sits as a legacy asset + the proven engine waiting for its first fan-out story.

## 7. Decision
- **D2 (revive prose) — DEFERRED** by researcher ("first do more work using `_STATE`"). Re-open at the convergence trigger (§6). Mechanism confirmed sound; no action on the store now; **do not delete** the legacy content.
