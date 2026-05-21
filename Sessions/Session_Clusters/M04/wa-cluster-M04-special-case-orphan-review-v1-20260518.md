# M04 special-case orphan review — researcher decision required

**Date:** 2026-05-18
**Purpose:** Four M04 verse_context rows are orphans (point to soft-deleted `wa_verse_records`). The audit's "missing Pass A meanings" check classified them generically; on inspection each one needs a specific disposition. The 15 other stale orphans were soft-deleted under approved cleanup patch `PATCH-20260518-M04-REPAIR-STALE-ORPHAN-CLEANUP-V1` — this document covers the remaining 4.

**Status:** Awaiting your marked-up decisions before CC builds the special-case patch.

---

## How to use this document

For each case, the proposed action is shown plus the alternatives. Mark your decision in the **Decision** block and add free-text notes if you want to override or amend.

After you save your decisions, ping me ("M04 special-case review marked") and I'll build a single patch covering all 4 cases.

---

## Case A — Dan 1:10 (vc=23405, H1524A gil)

**Verse text:** *"and the chief of the eunuchs said to Daniel, 'I fear my lord the king, who assigned your food and your drink; for why should he see that you were in worse condition than the youths who are of your own age? So you would endanger my head with the king.'"*

**Current state:**

- vc=23405 — is_relevant=1 — assigned to M04-A (Exultation in YHWH) / VCG M04-A-VCG-03
- vr=11725 — delete_flagged=1 (soft-deleted)
- analysis_note — NULL

**Diagnosis:** The verse semantically describes Daniel's fear of the king ("I fear my lord the king"). gil (joy/rejoice) does not appear to have any inner-joy sense in this verse; the STEP extraction appears to have surfaced gil here without an inner-joy ground. No other terms (in any cluster) occur in Dan 1:10 in the DB. Per v2_5 §18.2, ROUTE-TO-CLUSTER requires the target cluster to have a term at the same verse — there is no M01 (Fear) term at Dan 1:10, so a verse-level route to M01 is not eligible. The verse content semantically belongs to fear; an M01 ingest pass would need to add a fear-term extraction at Dan 1:10 for the verse to appear in M01's analysis.

### Proposed action — SET-ASIDE in M04 + research flag for M01 ingest

- UPDATE vc=23405 SET `is_relevant=0`, `set_aside_reason='gil reference at Dan 1:10 — verse describes Daniel's fear of the king ("I fear my lord"), not joy/rejoicing. STEP surfaced gil but no inner-joy sense is evidenced in the verse content. Verse semantically belongs to fear register (M01) but no fear-cluster term currently has an entry at Dan 1:10 — would need M01 ingest pass to add one.'`
- INSERT a `wa_session_research_flags` row: `flag_code='M01_INGEST_CANDIDATE'`, `description='Dan 1:10 — Daniel-chief-eunuchs fear-of-king scene; expressed in English with "fear" verb. No M01 term currently extracted at this verse. Consider adding ya.re or pa.chad as STEP extraction in future M01 ingest pass.'`, `priority='advisory'`, `session_target='M01-ingest'`

### Alternatives

- **HOLD** — leave as orphan (status quo); revisit later. Not recommended — leaves an analytically empty vc row.
- **RESTORE vr + KEEP in M04-A** — restore vr=11725 and treat as inner-joy (override). Not recommended — the verse doesn't evidence joy.

### Decision

```
Decision: _[SET-ASIDE+FLAG  /  HOLD  /  RESTORE+KEEP-M04  /  OTHER]_
Notes:
```

---

## Case B — Psa 81:2 (vc=28388, H5273A na.im)

**Verse text:** *"Raise a song; sound the tambourine, the sweet lyre with the harp."*

**Current state:**

- vc=28388 — is_relevant=1 — assigned to M04-J (Pleasantness and Relational Delight) / VCG M04-J-VCG-02
- vr=4368 — delete_flagged=1 (soft-deleted)
- analysis_note — NULL

**Diagnosis:** Researcher direction (2026-05-18): "the meaning of the verse is misplaced." na.im at Psa 81:2 functions as a descriptor of the lyre's tonal quality ("sweet lyre"), not as an inner-being state. The verse's joy/praise register sits in surrounding verbs ("sing aloud", "shout for joy") which are carried by other terms (other vc rows in M04 cover those). na.im here is the instrument-quality adjective.

### Proposed action — SET-ASIDE in M04 with §4.5.1 evidence-based reason

- UPDATE vc=28388 SET `is_relevant=0`, `set_aside_reason='na.im used as descriptive of a musical instrument ("sweet lyre") at Psa 81:2, not inner-being content — outside M04 inner-being scope. The verse-level joy register sits in the surrounding "sing/shout/blow the trumpet" context (carried by other terms, e.g. ranan / shir), but na.im here is the instrument-quality adjective.'`
- vr=4368 stays soft-deleted (no need to restore — na.im doesn't enter the cluster's analytical corpus via this verse)

### Alternatives

- **RESTORE + KEEP** — restore vr and keep as relevant (treat "sweet lyre" as inner-being). Not recommended — verse doesn't evidence an inner state via na.im.

### Decision

```
Decision: _[SET-ASIDE-WITH-REASON  /  RESTORE+KEEP  /  OTHER]_
Notes:
```

---

## Case C — 2Sa 23:1 (vc=28385, H5273A na.im)

**Verse text:** *"Now these are the last words of David: The oracle of David, the son of Jesse, the oracle of the man who was raised on high, the anointed of the God of Jacob, the sweet psalmist of Israel:"*

**Current state:**

- vc=28385 — is_relevant=1 — assigned to M04-J (Pleasantness and Relational Delight) / VCG M04-J-VCG-01 (Divine pleasantness and worship pleasantness)
- vr=4364 — delete_flagged=1 (soft-deleted)
- analysis_note — NULL

**Diagnosis:** Researcher direction (2026-05-18): "the word na.im is used to describe David's character — it is scribing someone's inner being." Per v2_5 §1.1, descriptions of human inner character (David as "the sweet psalmist") are in scope. The current vc assignment to M04-J is correct; only the orphan-vr situation needs fixing.

**Cross-reference:** the sibling 2Sa 1:23 ("Saul and Jonathan, beloved and lovely") is already live and processed in M04-J. Other na.im verses (Psa 16:6, Psa 133:1, Pro 22:18, Song 1:16, etc.) are all in M04-J. Restoring 2Sa 23:1 brings it into the same family.

### Proposed action — RESTORE vr + author Pass A meaning

- UPDATE vr=4364 SET `delete_flagged=0` (restore)
- vc=28385 stays as-is (is_relevant=1, M04-J / VCG-01, no Pass A meaning yet)
- Subsequent step: run Pass A on vc=28385 (the existing API script will pick it up automatically once vr is live, since `vc.analysis_note IS NULL` + `vr.delete_flagged=0`)

### Alternatives

- **SET-ASIDE** — treat na.im here as descriptive of David's role-title not inner-character. Not recommended — researcher already judged this inner-being content.

### Decision

```
Decision: _[RESTORE+PASSA  /  SET-ASIDE  /  OTHER]_
Notes:
```

---

## Case D — Ezr 6:16 (vc=23418, H2304 ched.vah)

**Verse text:** *"And the people of Israel, the priests and the Levites, and the rest of the returned exiles, celebrated the dedication of this house of God with joy."*

**Current state:**

- vc=23418 — is_relevant=1 — assigned to **M04-C (NT Joy in Christ and the Spirit)** / VCG M04-C-VCG-01
- vr=11626 — delete_flagged=1 (soft-deleted)
- analysis_note — NULL

**Diagnosis:** The current M04-C assignment is wrong — Ezr 6:16 is OT (post-exilic) corporate celebration of temple dedication; M04-C is for NT-distinctive joy in Christ. Researcher direction (2026-05-18): "Ezr 6:16 part of M04, should be assigned to sub group celebrating God's presence with joy."

**Two candidate sub-groups fit the description:**

| Sub-group | Label | Why it fits |
|---|---|---|
| **M04-A** | Exultation in YHWH: Vertical Rejoicing Directed Toward God | "celebrating God's presence" reads vertically — rejoicing in God as object |
| **M04-B** | Communal and Festive Rejoicing: Gladness in Worship, Feast, and Celebration | Temple-dedication is a communal festive event — matches "celebration" label closely |

**Existing `mti_term_subgroup` links for H2304 ched.vah:**

- M04-A — link exists (placement: secondary)
- M04-C — link exists (placement: primary) ← current
- M04-B — **no link exists** (would need INSERT mti_term_subgroup)

### Proposed action — RESTORE vr + RE-ASSIGN sub-group + author Pass A meaning

- UPDATE vr=11626 SET `delete_flagged=0` (restore)
- UPDATE vc=23418 SET `cluster_subgroup_id = <chosen_id>`, `group_id = NULL` (VCG will be re-assigned in Phase 7 step)
- If choice is M04-B: INSERT mti_term_subgroup (mti=356, cluster_subgroup_id=89, placement_note='[primary, audit-fix 2026-05-18] Ezr 6:16 corporate temple-dedication joy')
- Subsequent step: Pass A meaning for vc=23418; VCG assignment in step 5 of cascade (Phase 7-equivalent)

### Decision

```
Decision: _[M04-A  /  M04-B  /  OTHER]_
Notes:
```

---

## Methodological observation — tov set-aside verses inform word meaning

**Raised by researcher 2026-05-18 (after seeing the Step 2 review list):**

> "The 15 set aside no inner being verses are all H2896A. What is interesting, that it is set aside because the verse show no inner being relevance. However, the verses demonstrate what the word actually mean, and it is used in many other places (500+ times). The question is whether the real meaning and operations of H2896A was fully captured by setting aside these 15 verses."

(Saved as memory item [`feedback_setaside_verses_inform_word_meaning.md`](../../../../C:/Users/lerouxc/.claude/projects/g--My-Drive-Bible-study-projects/memory/feedback_setaside_verses_inform_word_meaning.md).)

**Programme-level open question** — not blocking on the 4 special cases above but worth tracking:

- Cluster analysis carves verses by inner-being relevance; the set-aside corpus carries the word's semantic range that informs how the inner-being subset reads.
- Currently set-aside reasons live only in `verse_context.set_aside_reason` text — not in a structured form a word study can aggregate.
- The Step 2 review of 75 terse tov set-asides will produce evidence-based per-verse reasons that contribute to tov's semantic profile.
- Consider: a Session C word-study panel for H2896A tov that aggregates ALL 500+ occurrences (in-cluster + set-aside + out-of-cluster) and shows how the meaning spreads across senses.

This is captured for tracking but does not change the special-case dispositions above.

---

*End of review document. Mark your decisions and ping me to process.*
