# VE / narration — iteration-2 action register (living)

> **One living register** for the fixes/decisions arising from verse-by-verse review of the mechanical rebuild + narration. Update **in place** (add examples, change status, close items) — do not spawn parallel docs. Detail for the first example is in [wa-ve-narration-feedback-vc1630-20260615.md](wa-ve-narration-feedback-vc1630-20260615.md). Started 2026-06-15 from vc=1630 (2Sa 1:9).
>
> Nothing in the data has changed from this review yet — these are queued actions awaiting researcher direction / more examples.
>
> **➤ Categorised synthesis (overnight digest, 2026-06-15): [wa-ve-corrective-actions-analysis-20260615.md](wa-ve-corrective-actions-analysis-20260615.md)** — every action sorted into error corrections · rule changes · VE extensions · new VEs (+ data-integrity, study-level), with the meta-pattern, dependency sequence, and the morning's decisions.

## Status key
`DECISION` = needs researcher design call · `READY` = agreed, implement on go · `INVESTIGATE` = data check first · `DONE`

## Open design decisions (block the related actions)
- **D-A — object/target.** Relational ("directed for …") has no object. Add a **new VE "object/target"** (the node the term acts on), or fold the object into VE13? → *pending*
- **D-D — the read VEs (9 purpose · 10 typology · 11 immediate-response · 12 produces-effect).** These were excluded from the mechanical batch, so the narration loses real content (vc=14782: "bowed faces to the ground" / "prostration"). The values **still exist in the soft-deleted `l2_api` findings** for the ~8,174 verses that got a read. Decide: **(a)** recover VE9–12 from the soft-deleted `l2_api` findings (cheap, but only the 8,174 read verses; ~22k M-cluster units never got a read), **(b)** re-read all, **(c)** mechanical proxy (e.g. the coordinated clause after the term as the response). Also requires extending the narration composer to render VE9–12. → *pending*
- **D-C — VE1 sense source (FOUNDATIONAL).** The stored sense (`ve_lexical` VE1, from `wa_verse_term_links.step_subgloss_label`) is actually STEP's **uniform short `gloss`** (H8312 → "anxiety" on *every* occurrence; `step_subgloss_code` is just the bare Strong's, no sense-split). This is **the exact uniform-gloss error 01b §1e warned against** (the *pneuma* mistake). STEP actually offers: `gloss` (short, uniform) · `medium_def` (fuller meaning, "disquieting thoughts, thoughts") · and the **per-occurrence `target_word`** (Psa 139:23 "thoughts", Psa 94:19 "cares") which varies correctly across occurrences. Decide the sense source: **(a)** `target_word` (true per-occurrence ESV rendering), **(b)** `medium_def` (fuller lemma meaning), or **(c)** `target_word` anchored to `medium_def`. → *pending — affects VE1 + the 30,571 persisted narration findings*
- **D-B — the "how"/qualifier-predicate.** Qualifiers of the term that aren't tagged terms are uncaptured — both the **governing predicate / "how"** ("anguish *seized* me") and the **quantifier / intensity / "how much"** ("cares *are many*"). Only analysed terms get spans, so these are absent from the DB. Capture by (i) re-parsing STEP's full verse HTML for the span's governing predicate/modifier, (ii) treat as a read field, or (iii) leave `UNRESOLVED`? → *pending*

## Action items

| ID | Source | Issue | Class | Action | Status |
|---|---|---|---|---|---|
| A1 | vc=1630, 2670 | transliteration shown alone (`ne.phesh(M25)`; `qe.rev`/`sha.a`/`tan.chum`) — **confirmed pervasive** (every multi-compound verse) | render | co-term renders with gloss: `ne.phesh "soul: life" (M25)` — VE3 value + narration + all outputs ([[feedback_translit_always_with_gloss]]) | READY |
| A2 | vc=1630, 14779 | location missed though seat-term present (1630); **AND location false-positive — "spirit"=ghost not the spirit-seat** (14779) | VE5 logic | VE5 adds co-occurring **constitutional-seat TERMS** as signals (strong's→seat map: H5315/H5315H→soul, H3820/H3824→heart, H7307→spirit, …) — **but must be SENSE-gated** (assign only when the seat term's per-occurrence sense IS the seat; pneuma="apparition/wind"≠spirit-seat). **Depends on D-C.** Also drop the English-word scan that caused the homograph | READY (now blocked on D-C) |
| A3 | vc=1630 | relational = bare preposition, no object | VE13 / new VE | per **D-A**: relational = direction + object; drop object-less bare prepositions | DECISION |
| A4 | vc=1630, 2670 | qualifier/predicate of the term absent — the "how" ("anguish *seized*…") **and** the intensity/"how much" ("cares *are many*") | data + design | per **D-B**: capture the governing predicate + quantifier/intensity qualifiers | DECISION |
| A5 | vc=1630 | legit T2 qualifier (`od` "still lingers") soft-deleted | data integrity | check why active T2 qualifier occurrences are soft-deleted (od: 170 active / 306 soft-del); is the web being thinned? | INVESTIGATE |
| A9 | vc=14779 | **emergent characteristic completely missed** — the inner being's capacity to *perceive (apparent) spiritual phenomena* ("thought they saw a spirit") is a distinct capability; the model flattens it to "perception faculty" and loses (i) the **object** of perception (a spirit/apparition) and (ii) that the object **caused** the fear | study / characteristic-model | the perceived-object + its supernatural nature must be capturable (ties to **D-A** object/target + the cause side); flag "perception of the spiritual" as a candidate characteristic for the synthesis layer. Note: dokeō "thought" = a *believed/mistaken* perception (it was the risen Jesus) | OPEN (study-level) |
| A8 | vc=14782 | response/effect missing from narration — "bowed faces to the ground" lost | read VEs (9–12) | per **D-D**: populate VE9–12 (recover from soft-deleted `l2_api` and/or read) + extend narration composer to render them. vc=14782 old read had VE11="bowing faces to the ground", VE12="prostration before the angelic men" (recoverable) | DECISION |
| A7 | vc=2671 | **VE1 sense = uniform short gloss, not per-occurrence** (H8312 "anxiety" on both verses; real per-occ = "thoughts"/"cares") — the 01b §1e *pneuma* error repeated | **FOUNDATIONAL re-source** | per **D-C**: re-derive VE1 sense from `target_word` (±`medium_def`); then regenerate the narration findings. Affects VE1 + all 30,571 narration findings | DECISION |
| A6 | vc=2671 | suspected verse↔term mislink (H8312 "not in" Psa 139:23) | data integrity | **RESOLVED — no mislink.** STEP confirms H8312 in Psa 139:23 + 94:19 (its only 2 occ); ESV renders it "thoughts". Sampled DB-vs-STEP check (25 terms) = **0 db-not-step mismatches**. Sub-finding: some terms show STEP>DB (e.g. blasfēmeō 11 vs 34) = OWNER/XREF soft-delete or coverage gap — opposite direction, lesser; full sweep available on request | VERIFIED |

## Further verse reviews — add examples here

> As you review more verses, drop them in this table; recurring patterns escalate an action or open a new one.

| vc / ref | term | observation | maps to action |
|---|---|---|---|
| 1630 / 2Sa 1:9 | sha.vats "agony" | (the worked example above) | A1–A5 |
| 2670 / Psa 94:19 | sar.ap.pim "anxiety" | (a) 3 compound co-terms shown without gloss — qe.rev "entrails: inner parts" (T2), sha.a "to delight" (M04), tan.chum "consolation" (M05); (b) "the cares **are many**" — the intensity/quantifier qualifier not captured ("many" is not a tagged term) | A1 (pervasive), A4 (intensity qualifier) |
| 2671 / Psa 139:23 | sar.ap.pim "anxiety" | (a) suspected mislink → **RESOLVED, correctly linked** (STEP confirms H8312 in 139:23 + 94:19; ESV "thoughts"); (b) **wrong sense** — stored "anxiety" is STEP's uniform short gloss; real per-occurrence is "thoughts" / fuller meaning "disquieting thoughts"; sample shows this is systematic | A6 (VERIFIED), A7 (DECISION) |
| 14782 / Luk 24:5 | emfobos "afraid" | the **effect of the fear** — "bowed their faces to the ground" — missing from narration (read VEs 9–12 not built); old read had it (VE11 "bowing faces", VE12 "prostration"), recoverable from soft-deleted l2_api | A8 (DECISION) |
| 14779 / Luk 24:37 | emfobos "afraid" | (a) location=**spirit is FALSE** — "spirit"=ghost not the seat (pneuma here = "apparition"; came from English-word scan; pneuma term soft-deleted); (b) the spirit-ghost is the **object/cause** of the fear; (c) **"perceiving a spirit" = a distinct inner-being characteristic, completely missed** | A2 (sense-gate), D-A (object), A9 (new characteristic) |
| | | | |

## Batching note
A1 + A2 are deterministic re-derivations (cheap; ve_lexical + narration findings rebuild from primary inputs). Recommend implementing them in **one combined re-run** once you've gathered more examples, so we regenerate once rather than per-fix.
