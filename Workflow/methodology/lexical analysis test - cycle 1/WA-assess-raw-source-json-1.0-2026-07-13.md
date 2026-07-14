# WA — Assessment of the Raw Source Layer (family JSON)

**File:** WA-assess-raw-source-json-1.0-2026-07-13.md
**Date:** 2026-07-13
**Version:** 1.0
**Author:** le Roux Cilliers
**Input:** `psalms__grace-mercy-compassion.json` (generated 2026-07-12; 101 KB; 11 ib_char items, 13 passages, 16 lexicals, 176 ve_lexical rows). One of 46.
**Prior outputs:** E1 (`inner-seat`), `other-uncategorised`, E4 preliminary, session log v1.1.

---

## Summary answer

**(a) Yes — introduce it. It is not noise. But as a projection, not raw.** It carries the three things the narrative corpus lacks entirely: **lemma**, **verse-level reference**, and **explicit edge states**.

**(b) Several things are missing — and one of them overturns a conclusion I drew in E1.** See §2.

**(c) Seven suggestions, one of which is free.** See §4.

---

## 1. (a) Would it help — or is it noise?

**It helps, and it is decisive on the three limitations I have been flagging all session.**

| Limitation of the narrative corpus | Does the JSON fix it? |
|---|---|
| No lemma. Nothing is a lexical finding. | **Yes.** `char_key: "H2603:generou"` — Strong's on every reading. |
| References are passage ranges (mean 9 verses). | **Yes.** `passage_ref: "Psa 37:14-40"` **but** `reference: "Psa 37:21"`. **The verse-level reference exists.** |
| No edge states — the movement model has to be inferred from prose. | **Yes.** A 16-slot `dimension_frame`: sense, type, source, seat, bearer, operation, target, manner, intensity, specifier, effect, coupling, prohibition, discovery, role, locus. |

**The single most consequential line in the whole file** is `reference: "Psa 37:21"` sitting beside `passage_ref: "Psa 37:14-40"`. The narrative was written at passage level and emitted the passage range. **The verse was known all along.** The range-reference problem in `psalms_story_combined.md` is not a limitation of the underlying analysis — it is a **pure emission loss**, and it is recoverable for free.

**But raw, it is too heavy.** This file is 101 KB for a *small* family (16 lexicals). Of its content, **2,802 words are `passage_text`** — full ESV passages I can read from Scripture without being handed them, and the bulk of the weight. And 176 dimension rows for 16 lexicals is an 11:1 explosion. Scaled across 46 families and ~2,048 readings, the raw set would be several megabytes and unusable in context.

**What I would want instead:** a **flattened projection** — one row per `reading_id`, sixteen dimension columns, plus lemma, verse reference, anchor/duplicate flag. `passage_text` dropped. That would be roughly 2,048 rows, entirely tractable, and would let every observation in every exploration be bound to a **verse and a lemma** for the first time.

---

## 2. (b) What is missing — including one thing that changes an earlier conclusion

### 2.1 The good news: E1's headline finding is **confirmed at source**

In E1 I raised, as the top referral candidate, whether the narratives' repeated *"the psalm does not tell us where inside a person this sits"* (132 of 167 sections) was a **reader determination** or a **template default**. I said E1's headline finding rested on it.

**It is a reader determination.**

`seat` (dimension 104) in this family: **16 of 16 lexicals carry `value: "none"`, `resolution: "none"`, `item_type: "flag"`.** And the file's own `reading_note` is explicit: *value "none" = reader found none; present:false = no row recorded.*

So the seat was **looked for, on every reading, and explicitly found absent.** The refusal to localise is recorded evidence, not a formatting artefact. **E1 §2 stands — at least for this family.** It should now be checked across the other 45, and it is a one-command check.

### 2.2 The bad news: five dimensions were **never recorded at all** — including two the narratives claim silence on

| Dimension | value | "none" | **present:false (no row)** |
|---|---|---|---|
| 103 source | 0 | 0 | **16** |
| 109 **intensity** | 0 | 0 | **16** |
| 110 specifier | 0 | 0 | **16** |
| 111 **effect** | 0 | 0 | **16** |
| 113 prohibition | 0 | 0 | **16** |

By the file's own rule, `present:false` means **no row was recorded** — which is *not* the same as the reader finding nothing. It is the absence of reading.

**Now set that beside the narratives.** Every one of the 167 `inner-seat` sections closes with *"the psalm does not tell us how strong it was, or how it finally turned out."* That is a claim about **intensity** and **effect**. At source, intensity and effect were **never recorded**.

**Consequence, and I want it stated bluntly:** E1's silence finding must be **split in two**.

- **Seat-silence: evidenced.** A reader looked and found none, 16 times out of 16.
- **Intensity-silence and effect-silence: NOT evidenced.** There is no row. The narrative's confident *"does not tell us how strong it was, or how it finally turned out"* is, on this evidence, **a template default asserting a silence that was never actually tested.**

That is the referral candidate resolving — half in favour of the finding, half against it. I would rather find this now than after building on it.

### 2.3 `direction` exists as a field and is **null in all 176 rows**

Every dimension row carries a `direction` slot. **It is populated zero times.**

E4's preliminary finding — from `seeking-inquiring`, `lifting-bearing`, `being-heard-listening` — is that direction may not be one edge among many but **the edge that determines what the movement is**. The schema already has the slot. Nothing is in it.

`target` (107) is populated 15 of 16 — but a target is not a direction. `target: "generosity"` at `[Psa 37:21]` names *what* but not *toward whom or what the movement runs*, and there is no **object-kind** classification (God / person / self / thing / abstraction / null) anywhere in the frame.

### 2.4 Missing from the dimension frame altogether

Measured against the movement model:

| Movement-model edge | In the 16-slot frame? |
|---|---|
| antecedent / cause | `source` (103) — **but present:false in all 16** |
| operation / how | `operation` (106) ✓ |
| object / target | `target` (107) ✓ |
| **observed object-kind** | **absent** |
| manner / intensity | `manner` (108) ✓; `intensity` (109) **never recorded** |
| produces / effect | `effect` (111) **never recorded** |
| **immediate-response** | **absent from the frame** |
| **transition / becomes** | **absent from the frame** |
| relational-web / binding | `coupling` (112) ✓ — but see §2.6 |
| **direction** | field exists, **never populated** |

### 2.5 No morphology, and no Hebrew

`char_key` gives the **lemma** (H2603) and nothing more. There is **no morphological parse** — no stem, no form, no person. The reset specification calls for grounding on *lemma **and morph***. Morph is absent.

There is also **no Hebrew text anywhere**. `passage_text` is English. Transliterations (*chen*, *techinnah*, *chus*, *chanan*, *racham*) appear only **buried inside the free-text `discovery` field** — as prose, not as data.

### 2.6 Data-quality fault: `coupling` and `locus` are **swapped in 10 of 16 rows**

The controlled vocabulary (`internal:ib-state`, `external:god`) belongs in one field; free-text pairings in the other. They are inverted in ten readings:

| reference | coupling (112) | locus (116) | |
|---|---|---|---|
| Psa 37:21 | `generous-and-gives` | `internal:ib-state` | ✓ correct |
| Psa 45:2 | `the graciousness for which God blessed him` | `internal:ib-state` | ✓ |
| Psa 55:1 | `twinned with the prayer` | `external:god` | ✓ |
| Psa 72:13 | `paired with saving their lives` | `internal:ib-state` | ✓ |
| **Psa 102:14** | `internal:ib-state` | `paired with holding her stones dear` | ✗ **swapped** |
| **Psa 103:13** | `internal:ib-state` | `paired with God's compassion…` | ✗ |
| **Psa 109:12** ×2, **109:16**, **112:4** ×2, **112:5**, **116:1**, **130:2** | controlled vocab | free text | ✗ |
| Psa 140:6 | `voice-pleas` | `internal:ib-state` | ✓ |
| Psa 141:5 | `rebuke-is-kindness` | `internal:ib-state` | ✓ |

Ten of sixteen. Mechanical, detectable, fixable — and it would silently corrupt any query on either field.

### 2.7 `discovery` (114) is populated 16/16 — but appears to be doing a different job

The discovery-lookout is meant to answer: *what does this verse imply about the inner being that current considerations do NOT capture?*

What is actually in the field is the verse quotation plus a gloss — e.g. *"'GRACE (chen) is poured upon your lips' — the king's gracious, winsome speech; chen = favour/charm…"* `[Psa 45:2]`. That is a **sense/seed** for the narrative, not a discovery lookout. It reads as though the field has been repurposed. **The lookout may not be running at all**, and if it is not, nothing in the pipeline is catching what the frame fails to see.

### 2.8 One lemma is fragmented into three characteristics by its **English gloss**

`H2603` appears as **three separate `char_key`s**: `H2603:pity`, `H2603:generou`, `H2603:dealsgenerously`.

One Hebrew lemma. Three characteristics. The split is driven by the **English rendering**, not by anything in the Hebrew. That is gloss-driven fragmentation — and it is precisely the move the reset was called to eliminate (*"what a word does, not what it names"*; *"never the English string alone"*). It also has a direct downstream effect: it will inflate any count of distinct characteristics, and it will scatter one lemma's readings across the family.

### 2.9 `type` (102) = `"volition"`

A one-word classification, populated 16/16. It is worth asking whether this is an **observation** or a **faculty bin under a new name**. The retired intrinsic-faculty field is supposed to be gone. `type: volition` may be it, returning.

### 2.10 No cross-family view

Each JSON is scoped to one family. A verse's readings under *other* families are not visible from within it. The binding-web — cluster boundaries collapsing per-verse at the moment of focus — **cannot be assembled from these files as they stand.** It needs a verse-keyed view across all 46.

---

## 3. What this data would let the explorations do that they currently cannot

- **Bind every observation to a verse.** `Psa 37:21`, not `Psa 37:14-40`.
- **Bind every observation to a lemma.** For the first time, a lexical finding becomes possible.
- **Test the E4 hypothesis properly.** With `target` + a populated `direction` + an object-kind, the claim that *direction constitutes the movement* becomes checkable rather than argued.
- **Distinguish real silence from unrecorded silence** — which, as §2.2 shows, the narrative layer currently conflates, and got wrong.
- **Detect the seat=none pattern across all 46 families in one query** — the strongest finding of the session, currently resting on one family and one theme.

---

## 4. (c) Suggestions

**Free, and I would do it first:**

1. **Emit `reference` (the verse) into the narrative markdown, not `passage_ref` (the range).** The data exists. This alone removes the largest stated limitation on every exploration to date.

**Cheap and high-value:**

2. **Populate `direction`.** The slot is already in the schema, null in all 176 rows. Add **object-kind** alongside `target` (God / another person / self / thing / abstraction / null).
3. **Fix the `coupling` ↔ `locus` swap** (10 of 16 rows here; check all 46).
4. **Split `present:false`.** It currently conflates *not applicable*, *not read*, and *not yet reached*. At minimum, distinguish **not-read** from **read-and-unresolvable** — the three-state model (resolved / NONE-silent / UNRESOLVED) has no representation for UNRESOLVED, and UNRESOLVED is exactly the state that five of the sixteen dimensions are actually in.

**Needs a decision, not just a patch:**

5. **`source`, `intensity`, `effect`, `specifier`, `prohibition` were never recorded.** Either they are read (and the narratives' claims about intensity and effect become evidenced), or they are formally declared out of scope (and the narratives must **stop asserting silence** on them). The present position — narrating a silence that was never tested — is the worst of both.
6. **`H2603` split three ways by English gloss.** Decide whether the unit is the **lemma** or the **gloss**. If the lemma, these collapse to one characteristic with three senses. This affects every count in the programme.
7. **Ask CC for a verse-keyed projection across all 46 families** — one row per `reading_id`: `verse_ref, lemma, char_key, ib_char, family, cluster, anchor, sense, type, source, seat, bearer, operation, target, manner, intensity, specifier, effect, coupling, prohibition, discovery, role, locus`. Drop `passage_text`. That is the artefact I would want in front of me, and it makes the whole corpus tractable at once.

---

## 5. Referral candidates raised

1. **Is `seat: "none"` universal across all 46 families, or specific to `grace-mercy-compassion`?** One query. It is the highest-value check available right now.
2. **Is `type` (102) a faculty bin under another name?** §2.9.
3. **Is the discovery-lookout actually running,** or has field 114 been repurposed as a sense/seed? §2.7.
4. **Were `source`/`intensity`/`effect` never recorded in *any* family, or only this one?** Determines whether E1's declared-silence closers are evidenced anywhere.

---

## 6. What I have and have not done

- **Read in full:** the complete `meta` block including the WORK_CONTRACT and its ten narrative directives; the `dimension_frame`; the `reading_map`; `scope_counts`; and all 16 lexicals × 16 dimensions (256 rows, 176 present).
- **Not done:** I have seen **one of 46 files**. Every count and every fault above is from this family alone. Whether the swapped fields, the unrecorded dimensions, the null `direction` and the gloss-fragmented lemma are **systemic or local, I cannot say** — and I am not going to assume, having already made exactly that mistake once today.

---

## Change control

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-13 | First issue. Assessment of `psalms__grace-mercy-compassion.json`. Confirms E1's seat-silence finding at source; **overturns** E1's intensity/effect-silence finding (never recorded); identifies null `direction`, absent morph, swapped coupling/locus, gloss-fragmented lemma. |
