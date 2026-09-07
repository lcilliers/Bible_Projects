# M10b prep — Phase 1 (UT verse review) — 2026-05-25

**Cluster:** M10b — Wickedness, Evil and Abomination
**Status:** `Not started` → start Phase 1 (UT review)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_8-20260519` §4
**Reference impl:** `scripts/_apply_m10_ut_review_via_api_20260522.py`

## 1. Term universe (17 terms, 537 verses)

| Strong | Translit | Lang | Total V | UT | VC rows | Relevant | Gloss |
|---|---|---|---|---|---|---|---|
| H7563 | ra.sha | Heb | 180 | 3 | 177 | 177 | wicked |
| H8441 | to.e.vah | Heb | 112 | **87** | 25 | 25 | abomination |
| G4190 | ponēros | Gre | 71 | 10 | 61 | 61 | evil/bad |
| H0205G | a.ven | Heb | 66 | 0 | 71 | 71 | evil: trouble (the *evil-character* sub-entry) |
| H8251 | shiq.quts | Heb | 26 | **22** | 4 | 4 | abomination |
| H7455 | ro.a | Heb | 19 | 5 | 28 | 28 | evil |
| G0987 | blasfēmeō | Gre | 11 | 0 | 11 | 11 | to blaspheme |
| G2549 | kakia | Gre | 11 | 0 | 11 | 11 | evil |
| H7562 | re.sha | Heb | 9 | 0 | 9 | 9 | wickedness |
| G0093 | adikia | Gre | 9 | 2 | 7 | 7 | unrighteousness |
| G4189 | ponēria | Gre | 7 | 0 | 7 | 7 | evil |
| G0946 | bdelugma | Gre | 6 | 3 | 3 | 3 | abomination |
| G2555 | kakopoios | Gre | 5 | 0 | 5 | 5 | wrongdoing |
| G0824 | atopos | Gre | 2 | 2 | 0 | 0 | wrong |
| G0947 | bdeluktos | Gre | 1 | 0 | 1 | 1 | abominable |
| G5337 | faulos | Gre | 1 | 0 | 1 | 1 | evil |
| H4849 | mir.sha.at | Heb | 1 | 0 | 1 | 1 | wickedness |
| **TOTAL** | | | **537** | **134** | **422** | **422** | |

**Inherited:** 422 verse_context rows already exist (all `is_relevant=1`) — these were classified under the pre-split M10 cluster and travelled with the terms when the split moved them into M10b on 2026-05-22. **They will not be re-classified by Phase 1** (§4.1 only acts on UT pairs).

**UT load:** 134 verses across 7 terms (10 terms have UT=0). Two terms account for 81% of the UT load: to.e.vah (87) and shiq.quts (22).

## 2. Cluster scope (proposed system-prompt domain block)

**M10b owns the CHARACTER of evil** — what kind of person, being, conduct, or thing is named when the term is used. M10b sits between two siblings:

- **M10 (Sin/Guilt/Transgression)** — owns the *act/state/experience* of moral failure. If a verse evidences something *done* (a sinful act, a guilty state, a transgression, an iniquitous deed), it belongs to M10, not M10b.
- **M10c (Defilement/Impurity)** — owns the *ritual/cultic uncleanness* register. If a verse evidences something *rendered unclean by contact* (corpses, leprosy, menstruation, ritual taboo), it belongs to M10c, not M10b.

M10b owns the verse when its content names:

1. **A wicked person** (ra.sha, mir.sha.at as collective, kakopoios) — the agent's *moral character*.
2. **Evil as the abstract nature of conduct or being** (kakia, ponēria, ponēros, faulos, re.sha, ro.a, adikia, atopos) — what kind of conduct this is, not what specific act was done.
3. **Trouble/iniquity as the character of evildoing** (a.ven H0205G — distinct from a.ven H0205H which stayed in M10 for moral-collapse state).
4. **Abomination** (to.e.vah, shiq.quts, bdelugma, bdeluktos) — what is named as *detestable to God or to the moral order* (idolatry, sexual perversion, false weights, hypocritical worship). This is the moral-character side of abomination, not the ritual-defilement side.
5. **Blasphemy as character expression** (blasfēmeō — moved here from M10's act-of-sin track) — speech that *characterises* the speaker as evil-towards-God, distinct from the act of blasphemy itself (which M10 still owns via blasfēmia/blasfēmos).

## 3. Disambiguation hot-spots (UT-relevant)

These are the judgement calls the API classifier will be asked to make. **Confirm/redirect the calls before I encode them in the system prompt.**

### to.e.vah (87 UT verses — the largest cohort)

`to.e.vah` is the OT's master abomination word. Three overlapping uses:

- **Idolatry as abomination** — Deu 7:25, 2Ki 21:11 etc. ("the abominations of the nations"). **M10b-relevant** — names idolatry as character of evil.
- **Sexual perversion / moral violation as abomination** — Lev 18:22, 20:13 etc. **M10b-relevant** — names the conduct's moral character.
- **Dietary/ritual taboo as abomination** — Deu 14:3, Lev 11 ("you shall not eat any abominable thing"). **Boundary with M10c** — these are ritual-purity rules. Proposed call: SET_ASIDE → M10c, because the register is dietary/cultic-clean rather than moral-character.
- **Lying-lips / false-weights as abomination to YHWH** — Pro 11:1, 12:22 etc. **M10b-relevant** — names character of evil conduct.

### shiq.quts (22 UT verses)

Almost always names **idols themselves as abominations** ("the abominations of Ammon"). M10b-relevant — names the idol's character-of-evil; not ritual cleanness register.

### bdelugma (3 UT verses)

Greek `bdelugma` parallels to.e.vah. Usually idolatry / "abomination of desolation." M10b-relevant in idolatry-character sense.

### atopos (2 UT verses)

Lit. "out of place" → "improper, wrong." Acts 28:6 (Paul not affected by the viper — "no harm came to him, nothing *atopos*") and similar. **Boundary call** — does this verse evidence moral-character evil, or just "amiss"? Proposed: classify per verse; many *atopos* uses are unlikely to evidence moral-character content (set_aside likely).

### ponēros (10 UT verses)

Standard Greek "evil." Verses evidencing the *character* of someone or something as evil are M10b-relevant. Verses where ponēros qualifies an *act* without character framing should default to M10b (consistent with the split's logic that ponēros lives in M10b, not M10).

### adikia (2 UT verses)

Lit. "unrighteousness." Sits on the M10 ↔ M10b boundary: M10b owns *unrighteousness as character*; M10 owns *injustice as committed act* (and uses adikēma for the act-form). For the 2 UT verses, judge per content.

### ra.sha (3 UT verses) — small UT cohort because the bulk is already classified

The wicked person. Default M10b-relevant for any inner-being-bearing context.

### ro.a (5 UT verses)

Lit. "evil/badness/disposition." The character side of evil. M10b-relevant when evidencing evil-as-character; set_aside when used of physical badness (rotten fruit, wasted condition) without moral content.

## 4. Forbidden grounds (§4.5.1 — global)

Per the instruction, SET_ASIDE may NOT use:

- "Not God-directed" / "no vertical framing"
- "Lacks theological depth"
- "Inner state too mundane / circumstantial"
- "Too negative / too corrupt"
- "Bodily/sensory rather than spiritual"

For M10b specifically, the cluster is **about** negative character — so the "too negative" trap is especially likely. CC will scan the API output for these grounds and reject.

Valid SET_ASIDE for M10b:

- "No inner-being state evidenced — verse describes external events / list / ritual procedure only."
- "Term here means X (literal, non-moral sense) — outside M10b evil-character scope."
- "Out-of-scope by design — belongs to M10 (act-of-failure) or M10c (ritual defilement)."

## 5. Outputs (canonical filenames)

- VCNEW patch: `Sessions/Session_Clusters/M10b/wa-cluster-M10b-patch-vcnew-utreview-api-v1-20260525.json`
- Review doc: `Sessions/Session_Clusters/M10b/wa-cluster-M10b-ut-verse-review-api-v1-20260525.md`
- Raw API responses: `Sessions/Session_Clusters/M10b/wa-cluster-M10b-ut-api-raw-responses-v1-20260525.json`
- Obslog: `Sessions/Session_Clusters/M10b/wa-cluster-M10b-obslog-phase1-ut-v1-20260525.md`

## 6. Cost estimate

- 134 verses across 7 terms with UT > 0; one API call per term (the largest is to.e.vah at 87 verses — well under the 50-chunk threshold? No — the M10 script uses CHUNK_SIZE=50, so to.e.vah will split into 2 chunks). Plus shiq.quts at 22 (1 chunk).
- Estimated total API calls: ~9 (7 terms + 2 chunks for to.e.vah). System prompt cached after first call.
- Model: `claude-sonnet-4-6` (same as M10 reference impl).

## 7. Questions before I execute

1. **Is the cluster-scope domain in §2 correct?** Specifically the M10/M10b/M10c split rules and the abomination-vs-defilement boundary for to.e.vah's dietary verses.
2. **Confirm the inherited 422 rows are LEFT AS-IS.** Phase 1 only handles UT (134). If you want the inherited classifications re-evaluated under M10b's narrower scope, that's a different (much larger) operation and would need separate planning.
3. **Any specific verses or judgement-calls** you want flagged or pre-decided before the API runs?

## 8. Next steps after approval

1. Clone `_apply_m10_ut_review_via_api_20260522.py` → `_apply_m10b_ut_review_via_api_20260525.py` with M10b system prompt and canonical filenames.
2. Run with `--dry-run` to confirm UT load picks up exactly 134 verses.
3. Run live (API).
4. Apply VCNEW patch via `apply_session_patch.py`.
5. Verify post-state per §4.6 (vc_completed flip; anchor rule; no forbidden grounds).
6. Write obslog.
