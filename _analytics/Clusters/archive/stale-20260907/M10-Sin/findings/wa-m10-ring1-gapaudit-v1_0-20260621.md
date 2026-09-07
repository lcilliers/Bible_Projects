# WA M10 — Ring 1 Gap Audit

**File:** wa-m10-ring1-gapaudit-v1_0-20260621.md · **Version:** v1_0 · **Date:** 2026-06-21
**Audits:** `wa-m10-ring1-evidence-v1_1-20260621.json` (now v1_1) · supplements `wa-m10-ring1-evidence-digest-v1_0-20260621.md`
**Purpose:** end-of-ring completeness check — for every verse-lexical in the ring: what is missing, what was not digested, what is expected but not found. This file sets the template for the same audit on every subsequent ring.

---

## 1. NOT DIGESTED — found and fixed

**`verse_report` was omitted** (present on all 137 occurrences). It carries `target_word`, `morph` (full morphology code), and **`stem`** (verbal binyan). The stem is material for these dynamics and is now captured in evidence **v1_1**.

**Stem evidence now digested (Hebrew lemmas):**
- *a.vah* (distort) — **Hiphil 9**, Niphal 4, Qal 2, Piel 1 → dominantly **causative** ("make crooked / commit perversity"), not simple intransitive.
- *sa.laph* (subvert) — **Piel 6** → intensive/causative throughout.
- *ba.gad* (treachery) — **Qal 39** → plain active.
- *ma'al* — Qal 35 (verb) + 27 noun forms.
- *sa.rah* — noun forms (8).

This is the kind of behavioural evidence (causative vs simple) that the synthesis will need; it would have been lost without the audit.

No other lexical field was left undigested: the full key set (sense, lemma_meaning, type, valence, compound, object, object_type, experiencer, cause, cause_clause, how, divine_involvement, relational, location, intensity, immediate_response, origin, faculty) is all captured. (`mode` does not exist in the data.)

---

## 2. FIELD POPULATION — what is present vs absent (of 137)

| Field | Pop. | Read |
|---|--:|---|
| sense / lemma_meaning / type / valence | 137 | complete (every occurrence) |
| compound (touch points) | 116 | 21 occurrences have no co-term recorded |
| object / experiencer | 84 | ~61% carry a doer and an object |
| object_type | 83 | of which God/person vs abstract (the relational target) |
| cause_clause / how / cause | 42 / 31 / 25 | causal framing on a minority |
| divine_involvement / relational | 24 / 22 | God's role / direction on a minority |
| location (seat) | 20 | sparse — see §3 |
| intensity / immediate_response | 16 / 13 | sparse |
| origin | 3 | near-absent — see §3 |
| faculty | 1 | near-absent — see §3 |

---

## 3. EXPECTED BUT NOT FOUND — assessment

Three fields are near-absent where, for *inner-being dynamics*, one might expect more. Each is assessed as genuine-silence or extract-gap:

- **faculty (1/137).** Expected higher for terms billed as inner-being dynamics. **Assessment: genuine, not a gap — but with a method consequence.** For these lemmas the inner-being engagement is not carried in the `faculty` field at all; it surfaces in the **touch points** (a.vah→*lev*; sa.rah→*levav*; deleazō→*psuchē*/*epithumia*; pu.qah→*conscience*). So the audit confirms: *for Ring 1, read the faculty signal from the co-term web, not the faculty field.*
- **location (20/137), and of those ~6 are the *nephesh*-person artefact** (ma'al Levitical laws). **Genuine seatings ≈ 14**, almost all *heart*. Expected-but-absent on most occurrences = genuine (the dynamic is usually predicated without a seat).
- **origin (3/137, 2–3 spurious).** Notable expected-but-not-found: **deleazō "entice"** carries no `origin` tag, though enticement is intrinsically an external lure acting on desire — the extract encodes that relation via `object`=desire, not `origin`. Minor encoding gap; the relation is recoverable from the touch points (epithumia, pleonexia), so not lost.

**Object absent on 53/137:** for verbs of turning/distorting/breaking-faith an object ("from what / against whom") is often expected. This is a candidate extract-thinness item to watch as later rings are read; not resolved here, flagged.

---

## 4. Audit verdict for Ring 1

- One real omission (verse_report) — **fixed** in v1_1.
- No fabricated or undigested fields remain.
- Near-absent fields assessed: faculty/origin absences are genuine, with the inner-being signal living in the touch points; the *nephesh* seat artefacts remain on the CC verify list.
- Ring 1 evidence is complete and ready to feed the eventual pull-together.

**This audit becomes the standing end-of-ring step** (run on R4, R3, R2, Core in turn), and `verse_report`/stem is captured from here forward.

---

*Ring 1 gap audit complete. Evidence at v1_1. No meaning derived.*
