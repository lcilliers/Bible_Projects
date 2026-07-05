---
name: project_leviticus_terminology_study
description: "ACTIVE (2026-07-05): Leviticus studied as a TERMINOLOGY problem (not ritual walkthrough), corpus-native in DB. Researcher's method: understand the state/concept terms first (clean/unclean/holy/sin/bless/curse/redeem); open question = are atonement-RITUAL words even inner-being? Coding->ve_lexical, observations->finding (evidenced), questions->catalogue. Infra + pilot DONE; next = code all 688 verse-record verses then Phase B discoveries."
metadata: 
  node_type: memory
  type: project
  originSessionId: e329ee73-1887-4b36-811c-8be854369e50
---

**The pivot (researcher, 2026-07-05):** don't walk Leviticus's rituals/prescriptions. Treat it as a **terminology problem** — code the *state/concept* words, then run interpretations as **discoveries**. Hold open the real question: **are the atonement-ritual words even inner-being words?** (Data says: likely NOT — kaphar literally = "to cover" = the reset MECHANISM; the inner-being terminology is the STATE it resets, clean/sin borne by the nephesh.)

**Four grounded findings (from the term-map alone):** (a) **clean/unclean (tame/taher) is the master axis** — a STATE, not a ritual (~95+69 verse-hits); (b) **atonement = kaphar "cover"** — mechanism, not inner-being; the cleansing word is a *different* term (taher); 16:30 shows the relation (atone→cleanse→clean-from-sin); (c) **the "heart" (levav) is nearly absent — 3 verses** — Leviticus works in STATES borne by *nephesh*, not a deliberating heart (a shift from Gen/Exod); (d) the state attaches to *nephesh + basar (flesh)* → reset is bodily.

**Researcher's driving questions (extensible):** why necessary to clean · where "unclean" comes from · why COVER not scrub · IB-desire vs external vs prerequisite · does awareness come in · past-only or forward.

**★ DISCIPLINE (researcher correction 2026-07-05): keep the two phases STRICTLY separate.** The questions are a **PREPARATORY input ONLY** — their sole job is to ensure the DIMENSION SET will COVER them (so the evidence exists once coding is done). **Phase A (ve-lexical coding) is PURE, NEUTRAL capture — NO findings, NO observations, NO cross-tabs, NO answering during coding.** Answering happens ONLY in Phase B (a separate pass over the completed corpus). Do NOT bake analysis/synergy into the coding — that risks coding TOWARD an expected answer (eisegesis). Each question = a Phase-B filter/cross-tab over the coded dimensions; the coding just records what each verse shows on each indicator.

**Requirements (researcher):** in DB · discoverable as part of the corpus · searchable · ALL observations evidenced · extendable for new questions · cover ALL verse-record verses (688). **Met with ZERO new tables.**

**The corpus data model (3 layers):**
- **Coding -> `ve_lexical`** (the items-in-verse EAV table): one row per (occurrence, dimension, value), `ve_label`=dimension, `value`=value, `source_provenance='leviticus-lexical-v1'`. **Reuses existing dims** ve101 sense/102 type/103 source/105 bearer/106 operation/107 target/111 effect/115 role/116 locus **+ new** ve201 axis/202 polarity/203 source_domain/204 reset/205 purpose/206 driver/207 person_role/208 awareness/209 temporal/210 transmissibility/211 coverage. **Extensible** = new dimension is just a new ve_label->ve_nr (no migration). **Span-keyed** via verse_span_index (key each occ to verse_span_id; verses lacking verse_context still keyed by span-anchor -> COMPLETE coverage).
- **Observations -> `finding`** (level GLOBAL/VERSE, cluster_code M12 clean/M10 sin/M11 atone/M22 holy/M47 self -> discoverable under the cluster model), **evidenced via `finding_verse_link`** (role SUPPORT) — no finding without evidence. finding_citation is CHECK-constrained to cluster sources, so Strong's go in the finding_value text.
- **Questions -> `wa_obs_question_catalogue`** (scope 'leviticus', LEV-CLN-01..06, extensible), linked to findings via **`finding_question_link`** (coverage answers/partial). A question's answer = its linked evidenced findings.

**Infrastructure (built + proven):** `scripts/_apply_lev_study_v1_20260705.py` — subcommands `--seed-questions`, `--load-coding <json>`, `--load-findings <json>`, `--live`; idempotent by provenance; keying + span-anchor fallback. Coding/finding JSONs in `verse-analysis/leviticus/_coding/` and `_discoveries/`. Design docs in `verse-analysis/leviticus/_reports/` (verse-records listing, terminology-orientation, coding-schema, corpus-datamodel). **Pilot done (CODING ONLY):** Lev 11:24-28 carcass-contact -> 108 ve_lexical rows (0 miss). The premature discovery-finding I created in the pilot was REMOVED per the discipline above — coding produces NO findings. (`--load-findings` in the loader is a Phase-B tool, unused during coding.)

**NEXT:** get researcher calibration on the pilot's coding depth, then **Phase A = code all 688 verse-record verses** (chapter by chapter, produce coding JSON -> load; ritual-only verses get `coverage='ritual-no-ib-span'` so completeness is provable), then **Phase B = discoveries** per axis (clean/unclean first) as evidenced findings answering the catalogue questions. Related: [[project_ve_lexical_is_verse_first]], [[reference_analysis_rules_finding_lifecycle]], [[feedback_all_study_work_in_db]].
