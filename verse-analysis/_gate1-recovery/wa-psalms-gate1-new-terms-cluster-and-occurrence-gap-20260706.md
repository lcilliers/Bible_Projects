# Psalms Gate-1 new terms — cluster assignment + occurrence gaps

> Raised in response to the researcher's two questions after the Psalms Gate-1 completion:
> 1. *"For the new terms added, did you check in STEP to identify other verses for the same term that should be added to the verse-record?"*
> 2. *"Did you auto-assign the new verses to clusters — if not, these terms risk being excluded when we get back to cluster work?"*
>
> **Honest answer: no to both.** This note states the verified exposure and the recommended fix. Nothing is written to the cluster model yet — slotting a term into a cluster is an analytical call I should not impute. Date: 2026-07-06. Scope: the 97 gate1 terms (79 newly registered + 17 reactivated + H6199).

---

## Question 1 — other occurrences of these terms (the "STEP" question)

**Fact:** the 97 terms have **2,684 occurrences across the whole OT** but only **445 are in the verse-record** — a gap of **2,239**. Largest: H5046 *to tell* 324→12, H5800 *to forsake* 193→21, H2451 *wisdom* 145→7, H6419 *to pray* 74→4, H5641 *to hide* 74→23.

**Two points:**

1. **STEP is not needed** — every occurrence of every term is already in the master index (`verse_span_index`). A STEP pull would only re-fetch what the DB already holds (and risks the 60-cap truncation). So the "other verses" are known, in-DB, now.

2. **But they should NOT be bulk-added to the verse-record — and this is by design, not an oversight.** The verse-record is the **characteristic** record (the reviewed inner-being cut). A term is characteristic in *some* verses and qualifier/standalone in others — decided by reading the verse in context (Step c). Adding all 2,239 occurrences would (a) re-flood the curated table and (b) assert "characteristic" for occurrences never read. Those occurrences earn a verse-record **when their own book is role-reassessed** (Steps b/c), exactly as Psalms just did.

**The real, nameable debt this exposes → cross-book backlog.** These 97 terms are *newly recognised* as inner-being characteristics. In books already read under the **old** method (Genesis/Exodus/Leviticus narratives, etc.) the term wasn't even in the registry, so its characteristic occurrences there were almost certainly missed. The per-book corrective pipeline will catch them **only because every book is being redone**. **Flagged:** if any already-"done" book is *not* re-run under the new method, these terms' occurrences there stay missing. (Recorded against the standing plan's assumption that every book is reprocessed.)

---

## Question 2 — cluster assignment (the exclusion risk — CONFIRMED REAL)

**Fact:** of the 97 terms, **94 have no `cluster_code` and 0 are in `mti_term_subgroup`** (the M:N junction the cluster model actually enumerates from — verified: e.g. M15 Wisdom draws its terms via `mti_term_subgroup → cluster_subgroup`). The 3 with a legacy `cluster_code` (H2898→T2, H6039→M24, H6231→T2) **still have no junction row**, so even they are effectively unattached.

**→ As it stands, prayer, wisdom, salvation, desire etc. are invisible to the cluster model and would be silently dropped when cluster work resumes.** The researcher's concern is exactly right.

Note this is compounded by **OT-DBR-009**: the 17 reactivated terms lost their cluster junctions entirely when they were over-deleted (every row, incl. deleted duplicates, has 0 subgroup links). So the dedup didn't just delete terms — it severed their cluster membership.

### Proposed cluster mapping (for confirmation — NOT yet written)

Most map cleanly to an existing M-code cluster. **`?` = low confidence, needs the contextual read to confirm.** Grouped by proposed target:

| Cluster | Terms (strong · gloss) |
|---|---|
| **M21 Prayer** | H8605 prayer · H6419 to pray |
| **M38 Salvation** | H3468 salvation · H8668 deliverance · H4190 salvation · H5826 to help? |
| **M39 Blessing** | H0835 blessedness/ʼashrê · H2898 goodness |
| **M46 Abundance** | H7646 to satisfy |
| **M14 Deceit** | H7723 vanity/false · H3576 to lie · H3577 lie · H2665 plot · H6141 twisted? · H2611 profane? |
| **M42 Speech** | H5046 to tell · H1747 silence · H0981 to speak rashly |
| **M27 Evil** | H2555 violence · H8496 oppression · H6231 to oppress · H5949 wantonness? |
| **M35 Testing** | H0974 to test · H5254 to test |
| **M06 Hate** | H2186 to reject · H3988 to reject · H6962 to loathe · H7853 to oppose · H7854 Satan? · H5010 to disown? |
| **M04 Joy** | H5937 to exult · H5970 to rejoice · H7832 to laugh · H6149 to please? |
| **M24 Weakness** | H5848 to faint · H3021 be weary · H2489 helpless · H7326 be poor · H6039 affliction · H6199 destitute · H0536 weak |
| **M15 Wisdom** | H2451 wisdom · H4148 discipline/musar? |
| **M16 Folly** | H5036 foolish · H3684 fool · H6612 simple |
| **M08 Pride** | H3932 to mock · H3887 to mock · H3933 derision · H7047 derision · H6277 arrogant · H7426 be exalted? · H7342 broad? |
| **M29 Desire** | H8373 to long for · H6165 to long for · H6770 to thirst · H3970 desire · H3368 precious? · H3365 be precious? · H1214 to cut off (covet)? |
| **M12 Purity** | H2135 to clean · H1305 to purify · H1252 cleanness · H1249 pure |
| **M03 Grief** | H2342 to writhe · H2427 agony · H7908 bereavement · H8428 to wound? · H3642 to pine? |
| **M02 Anger** | H5360 vengeance? · H5359 vengeance? · H4066 strife |
| **M30 Obedience** | H4784 to rebel · H5341 to keep/watch? · H8582 to go astray? · H7686 to wander? · H7683 to go astray? |
| **M22 Praise** | H7321 to shout |
| **M11 Repentance** | H1793 contrite |
| **M20 Doubt** | H5641 to hide? · H5800 to forsake? · H7279 to grumble? |
| **M01 Fear** | H1161 terror |
| **M10 / M10b / M10c Sin/Wickedness/Defilement** | H5003 to commit adultery · H0444 to corrupt? · H2556 to leaven? · H2149 vileness? |
| **M09 Humility** | H8217 low |
| **M47 Constitution** | H3689 loin/reins (seat)? |
| **Uncertain — needs read** | H6817 to cry · H6601 to open wide · H6323 to distract · H5640 to close · H7283 to throng · H8444 outgoing |

---

## Recommended fix (two parts)

**Part A — remove the silent-exclusion risk NOW (safe, mechanical, reversible).**
Raise a `GATE1_CLUSTER_PENDING` research flag (`wa_session_research_flags`) on each of the 97 terms (strongs_reference + description + unresolved), and keep this register as the authoritative list. Then a term cannot be silently dropped: any cluster-rework audit that checks unresolved flags / this register surfaces all 97. *No cluster membership is asserted — this only guarantees they are seen.*

**Part B — do the actual assignment as a reviewed step (analytical).**
Two options:
- **B1 (assign now):** you confirm/correct the mapping above; I write the `mti_term_subgroup` junction rows (into the right *sub-group*, not just cluster_code). Fastest guarantee of inclusion.
- **B2 (assign during cluster rework):** leave assignment to each cluster's rework, when the term's occurrences are read in that cluster's context and membership *emerges* (truest to the RESET method). Part A's flag/register carries them safely until then.

**My recommendation:** **Part A now** + **B2** (assign during rework), because membership should be validated by the read, not imputed — but with the flag/register guaranteeing they are never lost. If you'd rather lock it in immediately, confirm the mapping and I'll execute B1.

*Filed 2026-07-06. Exposure figures reproducible from `mti_terms` (anchor_note LIKE 'gate1-psalms-2026%') joined to `verse_span_index` / `mti_term_subgroup`.*
