---
name: project_location_seat_engine_fixed
description: "location seat-assignment was a stub (8 lemmas, gloss-gate); now full inventory + per-occurrence surface gate; VE field rules must check lexical completeness"
metadata: 
  node_type: memory
  type: project
  originSessionId: d51a2ae4-3564-40b3-84fd-2dc7fed902d8
---

2026-06-18 (researcher caught it): the `location` (constitutional-seat) field was badly under-assigning — only spirit=28, mind/conscience/inward-parts=0. Two defects in `scripts/_ve_engine_v2.py` (the single source of truth; `_apply_generate_ve_lexical_v2.py` imports `eng.derive`):
1. **SEAT was an 8-lemma stub** ("01b iteration-1; expand later") — missing mind (nous/dianoia/phren), conscience (suneidesis + Hebrew kilyah "reins"), inward-parts/viscera (qereb/me'eh/splanchna/kabed), Aramaic ruach H7308 + libbah H3826, neshamah, she'er.
2. **The spirit gate tested the lemma's DICTIONARY GLOSS** (which lists every sense), so ruach/pneuma self-tripped "wind/breath" on every occurrence → spirit never assigned mechanically.

**Fix:** full seat inventory + a `seat_level(st, surface)` resolver gating on the **per-occurrence surface** — `verse_morphology.surface` IS the ESV word in the verse (e.g. ruach → "Spirit"/"mind"/"wind"), so the per-occurrence sense was always available. Corpus rerun preserved all reads. Results: spirit 28→263, mind 0→109, conscience 0→149, inward-parts 0→171, flesh −31 (meat/kin dropped), 342 UNRESOLVED (qereb 'among/midst' → location read, still pending).

**Leveling decisions (mine, reasoned):** mind = Greek only (Hebrew mind = leb→heart); kilyah → conscience (the inner self God tests, Ps 7:9); qereb/me'eh/splanchna/kabed → inward-parts; womb (racham/rechem) excluded (it's the compassion STATE or literal childbirth). cheq H2436 "bosom" flagged for researcher (mostly physical).

**Why / how to apply (GOVERNING):** a prior "full audit" missed this because it checked engine COMPLIANCE, not LEXICAL COMPLETENESS. Every VE field with a seed/signal list (faculty, divine, intensifier, perception, causal, origin, valence…) is suspect the same way — audit each against the actual lexicon, and gate ambiguous lemmas on the per-occurrence surface, never the dictionary gloss. Standing guard added: `scripts/_check_ve_seat_completeness.py` (flags any seat-denoting corpus lemma not in SEAT) — run it after engine changes.

**2026-06-19 follow-through (DONE):** generalised the completeness audit to ALL hand-seeded lists — `scripts/_check_ve_signal_lists.py` diffs DIVINE/SPIRIT_BEINGS/PERCEPTION/COGNITION/INTENSIFIER/CAUSAL against canonical lemmas, gated on corpus presence (flags only members both missing AND present as tagged units). Closed the corpus-present gaps (DIVINE +H3069/H433/H3050/H5945/G5547; PERCEPTION +shama H8085/nabat H5027/azan H238; COGNITION +bin H995; INTENSIFIER +gadol H1419), then full base rerun — all 65,966 API reads preserved, only divine surfaced new readable residue (+432, $0.18); object-type/cause/location new residue was entirely T2 (reader correctly T2-EXCLUDED — never fix T2 verses); valence gap-units had no active verse record (unreadable). Net: 0 active readable non-T2 residue. Run both `_check_*` scripts after any engine signal-list edit, then base-rerun. See [[project_ve_lexical_normalisation_and_groundings]], [[feedback_lexical_review_is_insight_coverage_not_stats]]. Regenerated extracts (M02) reflect the fix; M01 by-characteristic JSON predates it.
