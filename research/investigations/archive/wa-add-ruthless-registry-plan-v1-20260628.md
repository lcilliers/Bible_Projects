# Plan — add "Ruthless(ness)" to the registry and bring it fully into the study

- **File:** research/investigations/wa-add-ruthless-registry-plan-v1-20260628.md · 2026-06-28 · Author: Claude Code.
- **Origin:** researcher direction on `wa-perek-ruthlessness-registry-exclusion-20260628.md` — cruelty is an IB-relevant characteristic missing from the registry; add it via the documented new-word path and catch up all constructs.
- **Status:** PLAN — for confirmation. Nothing registered/extracted yet. STEP server must be running for Stages 2/4.

## A. The documented new-word path (from the instructions, reread)
1. `python -m engine.engine --register --word="…" --source="Programme Addition"` → creates the `word_registry` row (`origin=programme_addition`).
2. `python scripts/_discover_word_terms.py --english ruthless` → STEP term map + **triage table** (`research/discovery/`). **Read-only, no DB writes.**
3. **Researcher triages** the term table (include/exclude each Strong's).
4. `python scripts/_apply_term_decisions.py` → applies the include/exclude decisions to the term inventory.
5. `python -m engine.engine --mode=audit_word --registry=N` → extracts verses (STEP), creates the file_index stub, syncs DB, runs the audit.
6. **Verse Context** — classify the new verses (`wa-versecontext-instruction`).
7. **Cluster assignment** — C-code + M-code.
8. **Newer constructs (NOT in old docs — see §C):** spans/morphology, gloss, ve_lexical, verse-read findings.

## B. Decision points (need your call before/at each stage)
1. **Word label.** Registry words are mostly nouns (fear, wrath, dominion). Use **"Ruthlessness"** (noun) rather than "Ruthless"? *(recommend: Ruthlessness)*
2. **Strong's anchors.** To be surfaced by Stage 2 discovery and triaged by you. Expected candidates: `perek` H6531 (harsh treatment), `arits` H6184 (ruthless/violent one), `akzar(i)` H393/H394 (cruel), `chamas` H2555 (violence) — you decide the boundary.
3. **Cluster assignment — the big one.** Options:
   - (a) **new cluster** "Cruelty / Ruthlessness" (new M-code, e.g. M48) — cruelty is distinct from Strength/Dominion; *(recommend)*
   - (b) fold into **M23 Strength/Dominion** (but M23 is "not started");
   - (c) a C-code only.
4. **ve_lexical / lexical method.** Under the RESET the lexical method changed. For the new word's verses, do we run the **legacy VE lexical** (to match existing rows like Lev 25:43's) or the **reset lexical**? *(This affects consistency — recommend deciding before Stage 8.)*
5. **Corpus growth.** The STEP pull will add new verses for any anchor not already in the corpus — this grows the verse index (ties to the earlier corpus-completeness thread). Confirm that's intended.

## C. Newer-constructs catch-up (the gap your note flagged)
The new-word docs predate these; population path to confirm during execution:
- **spans / morphology** (`verse_span_index` ← `verse_morphology`): mechanical, from the STEP morphology pull for the new verses.
- **gloss / transliteration**: from STEP/`mti_terms` at extraction.
- **ve_lexical** (normalised lexical values): requires the lexical-analysis step (legacy VE or reset — Decision B4).
- **verse-read findings** (`finding`, L=VERSE): the per-verse meaning, as exists for the digested words.
- **`verse_analysis_progress` / `ib_observation`**: link the new verses into the live verse-fanout method too.
→ **Deliverable:** once proven, **update `wa-registry-management-guide`** with a "new-word: constructs catch-up" section so the path is documented (your point that registry management must address the new constructs).

## D. Proposed sequencing (mapped to your steps a–e)
| your step | plan stages | output | gate |
|---|---|---|---|
| a) reread instructions | ✅ done | this plan | — |
| b) add Ruthless | A1 register · A2 discover | registry row + triage table | STEP up; label confirmed (B1) |
| c) terms/verses/relationships/cluster | A3 triage · A4 apply · A5 extract · A6 VC · A7 cluster | terms in inventory, verses extracted, cluster assigned | your triage (B2); cluster decision (B3) |
| d) catch-up constructs | C: spans, gloss, ve_lexical, findings | constructs populated | lexical-method decision (B4) |
| e) confirm completeness | structural-completeness audit vs a digested word (e.g. compare to a comparable registry) | completeness report | — |

## E. Prerequisites & safety
- **STEP server** running at `http://localhost:8989` (Stages 2, 5).
- **DB backup** before Stage 5 (first DB write) — engine auto-backs-up; confirm.
- Stages 1–4 are reversible (single registry row + read-only discovery + inventory rows). Stage 5 onward writes verses — run `--dry-run` first.

## F. What I can execute immediately on your go-ahead
- **Stage A1 + A2** (register "Ruthlessness" + run read-only STEP discovery → triage table) — needs only B1 (label) confirmed and STEP up. This produces the term table for your triage (B2), after which we proceed stage-by-stage with checkpoints.
