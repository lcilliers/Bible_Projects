# Faculties (T3.1–T3.11) — why they exist, traced through three method generations

- **filename:** 1598-phase-d-faculties-provenance-v1-20260908.md
- **date:** 2026-09-08
- **escalation:** #1598 (Phase D — faculties)
- **researcher instruction, verbatim:** *"lets focus on the faculties. start with figuring out why
  the faculty questions in the questions-catalogue even exist."*

## The 11 faculties, as the catalogue actually defines them (verbatim, `T3.x.1`'s own text)

| # | Component | Defined as (verbatim from the live catalogue question) |
|---|---|---|
| T3.1 | **Perception** | "the inner senses (hearing, sight, taste, touch, smell) and spiritual discernment" |
| T3.2 | **Cognition** | "knowing, understanding, discerning" |
| T3.3 | **Memory** | "the holding and retrieving of inner-being reality across time" |
| T3.4 | **Affect** | "feeling and emotional experience" |
| T3.5 | **Creativity** | "imagination and the capacity to originate" |
| T3.6 | **Volition** | "the capacity to choose" |
| T3.7 | **Agency** | "the capacity to act, initiate, and make happen" |
| T3.8 | **Moral Evaluation** | "the capacity to assess against a standard of right, wrong, good, and true" |
| T3.9 | **Conscience** | "the acute inner witness of sin, guilt, and conviction" |
| T3.10 | **Conscientiousness** | "the integrated response of moral awareness, volition, and action" |
| T3.11 | **Relational Capacity** | "the constitutional equipment for genuine connection with another person" |

Each has exactly 3 live questions, same shape throughout: `.1` a per-verse presence-check ("does the
characteristic engage this faculty *in this verse*... record none if it does not"), `.2` a per-verse
effect-check ("how does the characteristic *affect* this faculty *in the person* here"), `.3` a
cross-verse synthesis ("across the verses, what does the pattern... indicate" — `scope='The HIB'`,
Window 2's own job, not Window 1's). 33 rows total (11 × 3), all `status='active'`, all sharing the
identical `date_added`/`catalogue_version`/`last_modified` timestamps checked in §1 below.

## The direct answer

`wa_obs_question_catalogue`'s T3.1–T3.11 rows (all 33 of them — 11 faculties × 3 questions each)
carry `date_added: 2026-04-30T06:26:11Z`. That is **before** the 2026-06-25 "Characteristics →
Movements" method reset, whose own banner (`CLAUDE.md`) states explicitly: *"the characteristic /
object-type / faculty-ontology / tier-grid / logical-unit framing is CLOSED (provenance-only)."*
**"Faculty-ontology" is named directly, by that exact word, as one of the closed framings.** The
catalogue rows were never deleted or rewritten when that reset happened — they survive as live
(`status='active'`) text from a methodology the project's own governing document says is closed.

## But it isn't simply dead legacy — it was corrected once, then abandoned twice more

Checked the full chain, not just the endpoints:

1. **Pre-2026-04-30 — the original faculty-ontology.** A fixed system of faculties (a "grid"), part
   of the closed characteristic/object-type/tier-grid framing.
2. **2026-06-25 — closed**, per the reset banner above. Not touched again in the catalogue itself.
3. **2026-08-11 — corrected, not discarded**, in `WA-inner-being-windows-register-v2.2-2026-08-11.md`:
   **`W6` "Faculty-as-observation"** is explicitly logged as **`corrected-exemplar`** — *"faculty was
   demoted from ontology to a bare per-verse question, and that correction is exactly what 'clear
   glass' looks like."* Reads: *"Whether — and which — faculty/seat a verse engages... Blind to:
   Faculty as a system (deliberately — this is the correction)."* **The T3.x catalogue wording
   already matches this corrected shape** — *"In this verse, does the characteristic engage the
   perceptive faculty... Record none if it does not"* — a bare per-verse presence-check, not a
   classification into a fixed system — even though the wording predates the correction being
   written down. This is not a coincidence worth ignoring: whoever wrote T3.x in April was already
   asking it the "clean" way; the *system* (11 fixed faculties as a checklist) is what the reset
   closed, not the *question shape*.
4. **2026-07-02 — the interim `ve_lexical` / D1–D14 dimension model is built with no faculty
   dimension at all.** Checked the full live dimension table
   (`Workflow/Catalogue/wa-ve-lexical-catalogue-v1-20260702.md`): D1 sense/type, D2 source, **D3
   seat** ("constitutional seat (heart/soul/spirit…) → term, via construct chain," marked
   `✅ reliable`), D3 bearer, D5 target, D6 manner, D8 effect, D9 coupling, D10 prohibition, D14
   passage, D7 process, D11 discovery. **`D3 seat` is a different concept from "faculty"** — seat
   is *where* (heart/soul/spirit), faculty is *what kind of mental operation* (perceiving, knowing,
   remembering, feeling, willing, acting, judging). No D-number answers the faculty question. The
   closest genuine analog (T2.1's own "constitutional level" question) has a real, `✅ reliable`,
   already-validated mechanism in `D3 seat` — the faculty family (T3.1–T3.11) has nothing.
5. **2026-08-15/17 — `ve_lexical`/D1–D14 itself is superseded** by IBA's own `verse_lexical`
   (Layer 1/Layer 2, `cluster_strong`-driven) — the entire system this session's work (#1592–#1598)
   has been built on. Faculty was not carried forward into this generation either — confirmed, no
   `note_type`, no column, no `cluster` T-code answers it.
6. **2026-09-03+ (this session's own earlier findings, #1589/#1549)** — the evidence-supply-map
   independently re-discovers the same gap from the IBA side, speculating `noun_relational`/
   `noun_severity` (two note_types with zero rule text) are "very likely" intended for T2.1/T3.x —
   never confirmed, never built.

## The honest conclusion

**Faculties are not a mystery with a hidden rationale — they are a genuinely unfinished thread that
has now outlived three successive lexical-methodology generations** (the original ontology, the
interim D1–D14 model, and the current IBA Layer 1/2 system) **without any of them actually building
the mechanism to answer it.** The catalogue rows survive purely as `active` text; nothing has ever
computed an answer to them, in any era. This is the single largest unmet evidence gap in the whole
131-row catalogue (~30 rows) not because it was overlooked once, but because it has been correctly
*named* as important at least four separate times (April 2026 catalogue write, June 2026 reset,
August 2026 window correction, September 2026 evidence-supply-map) and built exactly zero times.

## One concrete, reusable asset this trace surfaced

`D3 seat`'s own derivation method — *"constitutional seat → term, via construct chain,"* validated
`✅ reliable` in the old system — is a real precedent for how a **mechanical, construct-grammar-based**
classification can answer a question of this shape (WHERE/WHAT-KIND a characteristic's inner-being
engagement is) without needing a full LLM judgement call. Whether that construct-chain technique
transfers from the old Hebrew-morphology-parser world into IBA's own `verse_lexical` mechanism is a
real question for the next step of this work, not answered here — but it means Phase D does not have
to start from zero method-design; a validated precedent for the *seat* half of this problem already
exists, even though *faculty* itself has none.

## Researcher's verdict — retired, executed

**Researcher, verbatim, in response to this trace:** *"One version of it value could be that it
names/classifies the different operations in the inner being. it is related to, but is not the same
as characteristics which is more like behaviours. different behaviours use (operate with) different
faculties. the faculties is real (memory, perception) but is likely another name for something that
is already there but not grouped. It is not something that can be directly derived from any verse.
The terminology is foreign to the bible. it makes no difference in understanding of a verse. It may
emerge when a collection of characteristics are described in their operations, although no
individual faculty exist or operate on its own. Will it do any harm if it is not included in the
debate during characteristic analysis - I dont think so. Will the study be weakened if it is not
taken into account before the final assembly of the inner being as a whole. I dont think so. So my
verdict is it can reliably be retired from the catalogue, with any replacement to be put in its
place. what will happen, is the work we are currently doing to formalise the parties, players,
operations, movements outcomes, need to be strengthened to enrich the analysis, but as such
faculties does not play a part in it."*

**The reasoning, restated:** faculties are real but not primitive — they are a *classification of
operation-types* a behaviour/characteristic uses, likely an unlabelled regrouping of data already
captured elsewhere (party/operation/movement work), not directly readable off a verse, foreign to
the Bible's own vocabulary, and — critically — **no individual faculty exists or acts on its own**;
at most it could *emerge* from a large-enough collection of characteristics' own operations, never
be *derived* per-verse the way the catalogue's own T3.x.1 questions ask. Cost-benefit test applied
to both the per-characteristic analysis stage and the final inner-being-assembly stage: no harm
either way if omitted.

**Executed, not just recorded** (per the standing discipline against stopping at "investigated,
here's a doc"): all 33 `T3.x` rows (`obs_id` 291–323) updated live via the registered
`obs_catalogue.update` tool (`Catalogue-Update.ps1`, one row at a time — the established, ungated
discipline for this table, no bulk SQL) — `status` set to `dropped` (matching this project's own
existing convention for exactly this action, e.g. `ve_lexical`'s D10/D12/D13 "DROPPED (researcher
decision)" entries), `review_note` carries the full verdict and this document's reference, verified
live afterward: **33/33 rows now `status='dropped'`.**

**Not decided, deliberately left open:** what (if anything) replaces this in the catalogue. The
researcher named the active priority explicitly instead — strengthening the parties/players/
operations/movements/outcomes work already underway (escalation #1598's own cluster-reallocation
thread) — and faculties "does not play a part in it." No replacement item is proposed here.
