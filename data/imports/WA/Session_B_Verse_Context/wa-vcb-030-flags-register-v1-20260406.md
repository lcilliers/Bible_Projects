# wa-vcb-030-flags-register-v1-20260406.md

**Framework B — Soul Word Analysis Programme**
**Verse Context — Batch VCB-030 — Deferred Flags Register**
**Version: v1 | Date: 2026-04-06 | Governing instruction: WA-VerseContext-Instruction-v2.4-20260403.md**

Observations file at time of this register: `wa-vcb-030-term-observations-v1.8-20260406.md`
All 9 terms classified. 12 flags accumulated. Resolution required before patch construction.

---

## Summary table

| Flag | Term | Verse | Type | Claude AI recommendation |
|---|---|---|---|---|
| DF-001 | H3513H 1864 | 1Sa 5:11 (143648) | Borderline relevance | **Retain** in Group D |
| DF-002 | H3513I 1867 | All 2 verses | All-verses-fail | **Confirm AVF** |
| DF-003 | H3513J 1866 | Isa 59:1 (143679) | Borderline relevance | **Set aside** |
| DF-004 | H3514 1865 | Pro 27:3 (143927) | Borderline relevance | **Set aside** (lean) |
| DF-005 | H3514 1865 | All 4 verses | Provisional AVF | **Confirm AVF** if DF-004 set aside; withdrawn if retained |
| DF-006 | H3517 1869 | Exo 14:25 (143930) | All-verses-fail | **Confirm AVF** |
| DF-007 | H3519 1861 | Est 5:11 (143709) | Borderline relevance | **Set aside** |
| DF-008 | H3519 1861 | Isa 10:18 (143749) | Borderline relevance | **Set aside** (lean) |
| DF-009 | H3519 1861 | Isa 66:12 (143780) | Borderline relevance | **Set aside** |
| DF-010 | H3519 1861 | Isa 35:2 (143762) | Borderline — dual clause | Second clause in Group A; **set aside first clause** (lean) |
| DF-011 | H3520A 1868 | Psa 45:13 (143929) | Borderline relevance | **Retain** in Group A (lean) |
| DF-012 | H3520B 1870 | Psa 45:13 (143932) | Borderline relevance | **Retain** in Group A (lean) |

---

## Flag detail

---

### DF-001 — Borderline relevance
**Term:** H3513H ka.ved (to honor: heavy) | mti_id: 1864 | Registry 15

**The verse:**
vid 143648 | 1Sa 5:11:
*"They sent therefore and gathered together all the lords of the Philistines and said, 'Send away the ark of the God of Israel, and let it return to its own place, that it may not kill us and our people.' For there was a deathly panic throughout the whole city. The hand of God was very heavy there."*

**Question:** Does *ka.ved* ("the hand of God was very heavy") itself carry inner-being engagement, or is the inner-being content (panic) in adjacent text and carried by a different term?

**Option A — Retain in Group D:** *ka.ved* names the divine weight that produces the inner experience of terror. The heaviness of God's hand is the cause; the panic is the named effect. Both are present in the same verse. The term participates in the inner-being condition.
**Patch consequence:** vid 143648 inserted as `is_relevant = 1, is_related = 1` in group 1864-004.

**Option B — Set aside:** The term describes the external action of divine pressure; the inner state (panic) is named separately by a different word. Apply the term-level filter strictly: *ka.ved* here refers to a physical/spatial metaphor of weight, and the inner state is adjacent, not term-carried.
**Patch consequence:** vid 143648 inserted as `is_relevant = 0, group_id = null`.

**Claude AI assessment:** Retain (Option A). The verse pairs the divine weight and the inner panic in a single sentence; the weight is what *produces* the named inner state. The parallel verse 1Sa 5:6 — "the hand of the Lord was heavy against the people of Ashdod, and he terrified and afflicted them" — is already in Group D and uses the same construction. Consistent treatment argues for retention.

→ **Your decision:**

---

### DF-002 — All-verses-fail
**Term:** H3513I ka.ved (to honor: many) | mti_id: 1867 | Registry 15

**All 2 verses individually inspected:**
vid 143676 | Nah 3:15: *"Multiply yourselves like the locust; multiply like the grasshopper!"* — target: Multiply. Military numerical command.
vid 143677 | Pro 8:24: *"When there were no depths I was brought forth, when there were no springs abounding with water."* — target: abounding. Physical abundance at creation.

**Finding:** Both verses use *ka.ved* in its quantitative/numerical sense (many, abundant). No inner-being engagement in either.

**Option A — Confirm AVF:** No verse_context records inserted for H3513I. Term proceeds to Session B with no anchor.
**Option B — Override:** Researcher sees inner-being engagement Claude AI has missed; specify which verse and why.

**Claude AI assessment:** Confirm AVF. Both uses are purely quantitative/physical with no inner-being faculty, state, or orientation engaged.

→ **Your decision:**

---

### DF-003 — Borderline relevance
**Term:** H3513J ka.ved (to honor: dull) | mti_id: 1866 | Registry 15

**The verse:**
vid 143679 | Isa 59:1:
*"Behold, the Lord's hand is not shortened, that it cannot save, or his ear dull, that it cannot hear;"*

**Question:** The term *ka.ved* is applied to God's ear (negated — God's ear is *not* dull). The immediate context of Isa 59 is human sin as the barrier to relationship with God. Does the term — as applied to God's ear in negation — engage the human inner being indirectly through the contrast it implies?

**Option A — Set aside:** The term applies to God's ear, not a human faculty. The filter asks about the inner being of the human person. God's attributes fall outside scope.
**Patch consequence:** vid 143679 inserted as `is_relevant = 0`.

**Option B — Retain:** The negation implies a corresponding positive — it is human sin/inner condition, not God's capacity, that prevents the relationship. The term illuminates the relational dynamic between human inner condition and divine responsiveness.
**Patch consequence:** vid 143679 inserted as `is_relevant = 1, is_related = 1` in group 1866-001 (or a new group if the context is judged materially different).

**Claude AI assessment:** Set aside (Option A). The term-level filter must apply to the term's specific use — here it describes God's attribute, not the human inner being. The inner-being content of Isa 59 is carried by the surrounding verses, not by this term in this verse.

→ **Your decision:**

---

### DF-004 — Borderline relevance
**Term:** H3514 ko.ved (heaviness) | mti_id: 1865 | Registry 15

**The verse:**
vid 143927 | Pro 27:3:
*"A stone is heavy, and sand is weighty, but a fool's provocation is heavier than both."*

**Question:** The noun *ko.ved* applies to the physical heaviness of stone in the first clause. The proverb's conclusion — that a fool's provocation outweighs both — carries inner-being content (the moral/relational weight of provocation). Does *ko.ved* carry that inner-being content through the comparison, or does it apply only to the stone?

**Option A — Set aside:** *ko.ved* in this verse applies to the stone's physical weight. The moral weight is in the second clause; the term itself is not the vehicle of the inner-being content. Mental-removal test: remove *ko.ved* from "a stone is heavy" — the proverb's inner-being conclusion remains intact.
**Patch consequence:** vid 143927 set aside → confirms AVF for H3514 (DF-005 applies).

**Option B — Retain:** The physical heaviness of the stone is the *comparator* through which the inner-being weight of provocation is measured. The term carries the standard of weight against which the moral weight is defined; the comparison is the meaning-unit, not the individual clauses.
**Patch consequence:** vid 143927 inserted as `is_relevant = 1`, anchor of a new group for H3514 describing the moral/relational weight of a fool's provocation.

**Claude AI assessment:** Lean toward set aside (Option A). The mental-removal test is the operative test here: *ko.ved* applies to the stone; the inner-being weight of the proverb is in the second clause and is not carried by this term. However, the reading in Option B is linguistically defensible — the proverb is a single semantic unit. This is a genuine borderline.

→ **Your decision:**

---

### DF-005 — Provisional all-verses-fail (contingent on DF-004)
**Term:** H3514 ko.ved (heaviness) | mti_id: 1865 | Registry 15

This flag is contingent on DF-004:
- **If DF-004 → Set aside (Option A):** Confirm AVF for H3514. All 4 verses fail. No verse_context records inserted.
- **If DF-004 → Retain (Option B):** DF-005 is withdrawn. H3514 has 1 relevant verse and 1 group.

No separate decision required — follows from DF-004.

→ **Resolved by DF-004 decision.**

---

### DF-006 — All-verses-fail
**Term:** H3517 ke.ve.dut (heaviness) | mti_id: 1869 | Registry 15

**The verse:**
vid 143930 | Exo 14:25:
*"clogging their chariot wheels so that they drove heavily. And the Egyptians said, 'Let us flee from before Israel, for the Lord fights for them against the Egyptians.'"*

**Finding:** *ke.ve.dut* describes the mechanical/physical difficulty of driving the chariots (wheels clogged → movement heavy). The Egyptians' inner response (recognition of divine action, decision to flee) is in the following clause, carried by different terms and the narrative act of speech.

**Option A — Confirm AVF:** No verse_context records inserted. Term proceeds to Session B with no anchor.
**Option B — Override:** The term names the condition that immediately produces the inner recognition — the physical heaviness is functionally inseparable from the inner realisation it triggers.

**Claude AI assessment:** Confirm AVF (Option A). The physical-mechanical use is clear; the inner-being content is carried by adjacent text. The term-level filter must apply at term level.

→ **Your decision:**

---

### DF-007 — Borderline relevance
**Term:** H3519 ka.vod (glory) | mti_id: 1861 | Registry 15

**The verse:**
vid 143709 | Est 5:11:
*"And Haman recounted to them the splendor of his riches, the number of his sons, all the promotions with which the king had honored him, and how he had advanced him above the officials and the servants of the king."*

**Question:** *ka.vod* here names Haman's splendour/wealth, which he recounts with evident pride. The inner-being content (pride, boastfulness, self-regard) is present in the passage — but is it carried by *ka.vod* or by the act of recounting?

**Option A — Set aside:** The term names the material splendour that Haman possesses. The inner-being content (his pride in it) is carried by the narrative act (recounting) and the context of Esther 5, not by *ka.vod* as used here.
**Patch consequence:** vid 143709 set aside.

**Option B — Retain in Group D2:** The splendour Haman recounts is precisely the outer expression of his inner self-regard. *Ka.vod* names the object of his boastfulness; the term and the inner state are inseparable in context.
**Patch consequence:** vid 143709 inserted as `is_relevant = 1, is_related = 1` in group 1861-005.

**Claude AI assessment:** Set aside (Option A). The term-level filter requires that *ka.vod* itself carries the inner-being engagement. Here it names the material wealth/status; the pride belongs to the framing of the passage. Note: this verse is highly relevant to the registry word "boastfulness" — but inner-being engagement through *this term in this verse* is what the filter tests.

→ **Your decision:**

---

### DF-008 — Borderline relevance
**Term:** H3519 ka.vod (glory) | mti_id: 1861 | Registry 15

**The verse:**
vid 143749 | Isa 10:18:
*"The glory of his forest and of his fruitful land the Lord will destroy, both soul and body, and it will be as when a sick man wastes away."*

**Question:** *Ka.vod* here refers to Assyria's territorial glory (forests, fruitful land). The verse is part of a judgment oracle against Assyrian pride. Does the term carry the inner-being dimension of national pride/self-regard, or does it apply to physical/territorial assets?

**Option A — Set aside:** The term applies to forests and fruitful land — physical/territorial assets. The pride of Assyria is carried by the surrounding oracle, not by this specific use of *ka.vod*.
**Patch consequence:** vid 143749 set aside.

**Option B — Retain in Group D2:** In the context of Isa 10's judgment on Assyrian arrogance, the glory of Assyria's land is the expression of its inner national pride. The physical assets and the inner pride are treated as a unity in the oracle.
**Patch consequence:** vid 143749 inserted as `is_relevant = 1, is_related = 1` in group 1861-005.

**Claude AI assessment:** Lean set aside (Option A). The term applies to forests and land; the pride is in the oracle's framing. Compare vid 143748 (Isa 10:16 — "under his glory a burning will be kindled"), which was retained in Group D2 because it more directly addresses Assyria's self-regarded glory. DF-008 is more externally physical.

→ **Your decision:**

---

### DF-009 — Borderline relevance
**Term:** H3519 ka.vod (glory) | mti_id: 1861 | Registry 15

**The verse:**
vid 143780 | Isa 66:12:
*"For thus says the Lord: 'Behold, I will extend peace to her like a river, and the glory of the nations like an overflowing stream; and you shall nurse, you shall be carried upon her hip, and bounced upon her knees.'"*

**Question:** *Ka.vod* here refers to "the glory of the nations" flowing to Israel — in context, the wealth/resources of the nations. Is this material abundance, or does it carry the inner-being dimension of honour/dignity flowing from the nations to Israel?

**Option A — Set aside:** The image is material — wealth flowing like an overflowing stream. The inner-being dimension of national dignity or honour is not the focus here.
**Patch consequence:** vid 143780 set aside.

**Option B — Retain in Group D2:** The "glory of the nations" flowing to Israel is an eschatological reversal of honour — the relational-social standing of the nations is redirected toward God's people. The inner-being dimension of communal honour/dignity is present.
**Patch consequence:** vid 143780 inserted as `is_relevant = 1, is_related = 1` in group 1861-005.

**Claude AI assessment:** Set aside (Option A). The dominant image is material (river/stream of wealth); the eschatological honour dimension, while present in the broader passage, is not the primary semantic function of *ka.vod* in this specific verse.

→ **Your decision:**

---

### DF-010 — Borderline dual-clause
**Term:** H3519 ka.vod (glory) | mti_id: 1861 | Registry 15

**The verse:**
vid 143762 | Isa 35:2:
*"it shall blossom abundantly and rejoice with joy and singing. The glory of Lebanon shall be given to it, the majesty of Carmel and Sharon. They shall see the glory of the Lord, the majesty of our God."*

**Question:** The verse contains two distinct uses:
1. "The glory of Lebanon" — the natural beauty/splendour of Lebanon given to the restored land
2. "They shall see the glory of the Lord" — theophanic divine glory (clearly relevant, already in Group A)

The verse has already been partially assigned (second clause → Group A). The question is whether the first clause ("glory of Lebanon") warrants:
(a) setting aside the first clause, with only the second clause relevant;
(b) treating the whole verse as dual-context (Groups A and D2);
(c) treating the whole verse as Group A only, with the Lebanon glory as a comparator for the divine glory.

**Option A — Set aside first clause; second clause only in Group A:** The glory of Lebanon is natural beauty applied to the restored land — no direct inner-being engagement. The theophanic second clause is what carries the inner-being content.
**Patch consequence:** vid 143762 inserted once as `is_relevant = 1, is_anchor = 0, is_related = 1` in group 1861-001 (Group A). No set-aside record needed since the verse is relevant overall — only the second clause drives the classification.

**Option B — Dual-context (Groups A and D2):** The glory of Lebanon represents the restored honour/dignity of the land and its people — a communal inner identity dimension — and the divine glory is the theophanic source. Assign to both groups.
**Patch consequence:** vid 143762 inserted twice — once in Group A (is_related = 1) and once in Group D2 (is_related = 1), with dual-context note.

**Option C — Group A only, whole verse:** The Lebanon glory is a rhetorical intensifier for the divine glory; treat as a single theophanic image.
**Patch consequence:** Same as Option A.

**Claude AI assessment:** Option A (or C — functionally identical for the patch). The glory of Lebanon is natural beauty/fertility; the inner-being engagement of the verse is entirely in the second clause. The whole verse enters as Group A related, driven by the second clause. No dual-context warranted.

→ **Your decision:**

---

### DF-011 — Borderline relevance
**Term:** H3520A ka.vod (glorious) | mti_id: 1868 | Registry 15

**The verse:**
vid 143929 | Psa 45:13:
*"All glorious is the princess in her chamber, with robes interwoven with gold."*

**Question:** *Ka.vod* here describes the princess's visible splendour and magnificence. This is a royal wedding psalm. Does the term engage the inner being — the person's dignity, worth, or relational position — or does it describe only visible, material adornment?

**Option A — Retain in Group A (1868-001):** The princess's glory in the context of a royal marriage covenant carries the inner dimension of dignified personhood and relational honour. The setting (inner chamber, awaiting the king) suggests the whole-person dignity of the bride, not merely her garments.
**Patch consequence:** vid 143929 inserted as `is_relevant = 1, is_related = 1` in group 1868-001.

**Option B — Set aside:** The term describes visible adornment (robes of gold). The inner being of the princess is not what the term names here; it names her external appearance.
**Patch consequence:** vid 143929 set aside.

**Claude AI assessment:** Lean retain (Option A). The royal wedding context involves relational covenant and honour bestowed on a person. The whole-person dignity dimension is present even in the description of adornment. Section 3.3 (borderline — retain) applies. However, this is genuinely uncertain.

→ **Your decision:**

---

### DF-012 — Borderline relevance
**Term:** H3520B ke.vud.dah (riches) | mti_id: 1870 | Registry 15

**The verse:**
vid 143932 | Psa 45:13:
*"All glorious is the princess in her chamber, with robes interwoven with gold."*

**Question:** Same verse as DF-011, different term (H3520B, gloss "riches"). Here *ke.vud.dah* carries the sense of "rich garments / splendour of wealth." Does the material richness of the robes engage the inner being, or is it purely external adornment?

This flag parallels DF-011 exactly. If DF-011 is retained, DF-012 should follow the same decision for consistency (same verse, parallel terms). If DF-011 is set aside, DF-012 should also be set aside.

**Option A — Retain in Group A (1870-001):** Same grounds as DF-011. The rich garments are part of the whole-person dignity of the bride in a covenantal context.
**Patch consequence:** vid 143932 inserted as `is_relevant = 1, is_related = 1` in group 1870-001.

**Option B — Set aside:** The term names material richness of garments only.
**Patch consequence:** vid 143932 set aside.

**Claude AI assessment:** Follow DF-011 decision for consistency. Lean retain (Option A).

→ **Your decision (follows DF-011):**

---

## How to respond

For each flag, record your decision using the option letter, or provide an override instruction. The simplest format:

```
DF-001: A
DF-002: A (confirm AVF)
DF-003: A
DF-004: A
DF-005: follows DF-004
DF-006: A (confirm AVF)
DF-007: A
DF-008: A
DF-009: A
DF-010: A
DF-011: A
DF-012: follows DF-011
```

Or override any with your own reasoning. After decisions are received, the observations file will be updated (v1.9), the patch will be constructed, and any Session B flags will be documented.

---

*wa-vcb-030-flags-register-v1-20260406.md | VCB-030 — 12 deferred flags for researcher resolution | Observations file: wa-vcb-030-term-observations-v1.8-20260406.md*
