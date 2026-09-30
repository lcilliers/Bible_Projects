# Reset corpus sweep — outcome + honest assessment (for the researcher's decision)

- **File:** wa-reset-sweep-outcome-and-honest-assessment-v1-20260626.md · **2026-06-26 · Author:** Claude Code.
- **What you asked for:** apply yesterday's work to the engine, run it through all the verses, update the lexicals. **Done.** This is the outcome + an honest read of what it does and does **not** fix — written so you can apply your mind when you're back.

## 1. What was done

- **Wired** the 7 new reset fields into the runner (`_apply_generate_ve_lexical_v2.py`, `VE_MAP` ve_nr 23–29): `from-source · instrument · purpose · quality-bearer · operation · isolable · discovery`; extended the narration template; bumped the run stamp to today.
- **Ran the live sweep over the whole corpus:** 42,076 units → **40,308 generated** (1,768 T2-grammatical units correctly skipped), **452,885 `ve_lexical` rows**, **31,908 `l2_meaning` narrations regenerated**.
- The stored lexicals now reflect yesterday's fixed engine (object-fidelity, from-source, tense, quality-bearer, operation, instrument, purpose, adjacency, discovery-lookout) — previously they were the pre-reset 2026-06-16 values.

## 2. It was done safely (all-in-DB rule honoured)

- Fresh backup before the write: `backups/bible_research_pre-reset-sweep_20260626.db` (+ yesterday's KEEP milestone backup, + NAS).
- **Read-API "light-read" overlays fully preserved** — valence 30571 · divine-involvement 14646 · object-type 12104 · cause 7743 · location 1336, **all unchanged**. The sweep did **not** clobber the human/API read work.
- **Faculty-map preserved** (26,386) with **0 true duplicates**; +2,819 v2 faculty rows are gap-fill on terms the map doesn't cover.
- `l2_meaning` active count stable (32,005; old soft-deleted, reversible).
- **Integrity check = the before-start baseline exactly** (231,890 rows, 0 orphans, only the pre-existing known nulls). No new corruption.

## 3. What it genuinely improved (real, visible)

The fidelity fixes and new fields now show in the meanings. Examples from the regenerated `l2_meaning`:

- **Heb 9:14** *katharizō* → "…**from works, by means of Spirit, in order to serve God**" — the binding/agent/purpose the pilot flagged as *missing* is now captured (instrument=Spirit, from-source=works, purpose=serve God).
- **Mat 5:8** *katharos* → "as a quality… **describing heart**" — the quality-bearer (pure→heart) is captured.
- **Eze 36:25** *ta.hor* → "…**from idols, uncleannesses… describing water**" — from-source + quality-bearer captured; the defilement content (idols) disambiguates the *moral* sense.

New-field coverage corpus-wide: from-source 8,831 · purpose 6,338 · quality-bearer 2,088 · instrument 715 · operation 634 · isolable 5,399 (verses that must be read with a neighbour) · discovery 40,308 (one lookout per unit).

## 4. The honest limits — what this does NOT fix (this is the part for your decision)

You said the lexical work looks less reliable than you'd hoped. The sweep **does not change that fundamental ceiling** — it sharpens the mechanical edges; it does not give the engine *understanding*. Concretely, the same regenerated meanings still show:

- **Faculty over-firing:** Mat 5:8 *kardia* → "engaging the affect, cognition, volition, conscience, perception, moral_evaluation faculty" — i.e. *everything*. The lemma-map gives the heart every faculty; it is not verse-discriminating.
- **Object mis-grabs on adjectives:** Mat 5:8 *katharos* "acting on God" — a quality doesn't act on an object; the mechanical grab over-reaches.
- **Residue the engine can't bind:** Heb 9:14 still drops "blood" to the discovery-lookout (it's governed by a preposition the engine doesn't mechanise) — the lookout *flags* it honestly, but the engine can't *resolve* it.
- **Figurative + distributed meaning remain mechanically invisible** — exactly the Psa 24:4 lesson. "Clean hands = conduct" and "the outcome is in the next verse" are not, and cannot be, mechanical.

**The mechanical pass is a *scaffold of edges*, not a verse understanding.** That was always the design (breadth-mechanical + depth-on-demand), but the sweep makes the ceiling concrete and visible so you can judge it on real data.

## 5. For your decision — framing, not a recommendation you didn't ask for

You floated doing the verse studies in Logos. Two honest observations to feed that decision:

1. **The mechanical layer and a Logos study are not either/or.** The lexicals now give you, for every verse, a *structured starting frame* (seats, co-terms, from-source, purpose, the discovery-gap list of what's unaccounted) that a Logos exegesis can start *from* rather than from blank. The scaffold's value is as an index/prompt into the deep study, not as the finished understanding.
2. **The real cost question is the genuine-Logos count, which I still haven't measured** (figurative + theologically-loaded are mechanically invisible). If you want, before you decide, I can build the figurative-candidate proxy (somatic body-part term co-occurring with an inner-being term) to put a *real* number on how many verses truly need the deep treatment — so the 2–3-year fear is tested against data, not the inflated 48%.

## 6. Files / provenance

- Runner: `scripts/_apply_generate_ve_lexical_v2.py` (VE_MAP + narrate extended; faculty-map preservation added).
- Engine: `scripts/_ve_engine_v2.py` (narration extended with the new fields).
- Tracker log: `wa-reset-rollout-db-concern-tracker-v1-20260625.md` (interval row 2026-06-26).
- Backup: `backups/bible_research_pre-reset-sweep_20260626.db`.
- ve_nr 23–29 tiers are **PROVISIONAL** best-fit — please confirm or correct the tier assignments.
