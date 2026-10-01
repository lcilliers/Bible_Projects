# Handoff — build the change-of-character layer for the thought strand (v1)

**Date:** 2026-10-01 · **For:** a new chat · **Escalation:** #1919 (approved, needs follow-up, assigned to Claude)
**Researcher, verbatim:** *"approve 1 2 3 4, proceed with the build in a new chat."*

## Start here (read in this order)

1. `origin-of-thought-change-of-character-v1-20261001.md` (this folder). This is the **approved proposal**. §2 is a first inventory; §3 lists the factors to test; §4 is what was approved.
2. `origin-of-thought-observation-ledger-v1-20260930.md` (this folder): the 40 woven observations, plus OT-H2 (to be reopened).
3. `origin-of-thought-discussion.md` (this folder):
   - §6.1: one word covers craft, plot and God's plan; *dialogismos* is inner reasoning and outward quarrel; Acts 17:29.
   - §9: the earlier synthesis.
   - §11: the six flows. **Flows 3 and 5 must be woven.**
4. The narrative: `_analytics/essay/spirit_soul_body/inner-being-narrative/`. Start with `00-index-and-status-v1-20260930.md`: its rules, the "How later work updates this" section, and the Structure log.
5. The method: `_analytics/essay/spirit_soul_body/wa-essay-narrative-weave-method-and-ch10-structure-v1-20260930.md`.
6. CLAUDE.md banners: "Weave, don't fit" (#1918) and "Change of character is a key discovery" (#1919). Memory: `project_change_of_character_key_discovery`, `feedback_weave_not_fit_narrative`.

## What was approved (the four decisions)

1. **Method.** Every strand ledger gets a **"Change of character"** section. For each word or concept with more than one face, record:
   - the faces and their verses
   - the circumstances that differ: who thinks · toward or against whom · joined with what · heart state · alone or with counsel · setting · what follows or comes back · narrative context
   - why, stated by the verse or as a labelled reading

   Words are pulled **by word across all clusters, never by cluster**.
2. **Narrative.** Each operation section (10.x) gets a passage on **when this activity changes character, and why**. **Ch 11 §4** ("One word, opposite values") grows into the cross-cutting account of what governs change. It stays open for later strands.
3. **Reopen OT-H2.** Weave discussion §11:
   - **flow 3**, thoughts acting on the self: Job 20:2; Dan 7:28
   - **flow 5**, consequences returning to the one who devised: Est 9:25; Ps 10:2; Jer 6:19; Pro 21:5

   These go into 10.3 and 10.0.
4. **Build.** Complete the change-of-character section for **every** thought word, then weave it in.

## Steps

1. **Data (read-only, iba.db).** For each thought word, pull every occurrence across clusters and read each verse. Words:
   - *ḥāšav* H2803 (all variants) · *maḥăšāvāh* H4284 · *mᵊzimmāh* H4209 · *yēṣer* H3336 · *hāgāh* H1897 · *dāmāh* H1819
   - *raʿyôn* H7476 · *śarʿappîm* H8312 · *śᵉʿippîm* H5587 · *rēaʿ* H7454 · *ʿaštût* H6248
   - *logizomai* G3049 · *logismos* G3053 · *dialogizomai* G1260 · *dialogismos* G1261 · *dianoia* G1271 · *noēma* G3540 · *enthymēsis* G1761 · *dianoēma* G1270

   Existing pulls are `strong-thought.csv` (255 rows) and `open-thread-words-pull-v1-20260930.csv`. Fill gaps from `span` ⋈ `verse` (match `strong_variant` as a space-delimited token). Read the surrounding passage where the narrative context decides the face, as in Jer 18:11–18.
2. **Ledger.** Add the "Change of character" section to the ledger (version-bump it to v2, archive v1). Every face of every word gets a row. Also reopen OT-H2 there. Treat the factors in proposal §3 as hypotheses: record where the verses confirm, refine or contradict them.
3. **Weave**, following the weaving method:
   - 10.3 and 10.0 (change-of-character passage; flows 3 and 5)
   - 10.4, 10.1, 10.2, 10.6, 10.8 and 10.9 where the faces touch them
   - Ch 11 §4 (cross-cutting account)
   - Ch 12 and 13 if faces touch them

   Use version bumps (`-v3-` for files already at v2; v2 for 10.3 and 10.4), with prior versions to `archive/`.
4. **Records:**
   - claim register → v3 (add a strand-update section)
   - index Structure log + version map
   - ledger "woven — where"
   - #1919 updated with what was done

## Rules that apply (do not skip)

- **Chapter text:** first person, plain, no project terms (no cluster, Strong's number, ledger or strand in chapter files). Hebrew and Greek words always with a gloss. Claude's readings are marked "I read this as…".
- **Quotes:** every quotation checked mechanically against the ESV in iba.db `verse` (book codes such as `Psa`, `1Cor`, `Phili`, `Jam`; ~1.3k verses are missing, #1891).
- **Weave, don't fit.** Never drop a face because another face of the word is already in the text. If a face has no home, the structure changes, and that goes to the researcher.
- **Never set discussion findings aside as "superseded" without asking.**
- **Phenomenon-level, emergent:** account for every verse read. Factors are tested, not imposed.
- **No AskUserQuestion.** Judgement calls go to an `.md` file and an escalation, in plain chat.
- Open iba.db read-only (`file:...?mode=ro`).

## Done when

- [ ] Every thought word has its faces recorded, with verses, circumstances and why.
- [ ] Flows 3 and 5 are woven.
- [ ] 10.3, 10.0 and Ch 11 §4 carry the change-of-character account. The other touched sections are updated.
- [ ] All quotes ESV-checked. Coverage check: every face is woven somewhere.
- [ ] Register, index Structure log and ledger are updated. #1919 is updated, then set ready_for_approval.

## State at handoff

- **Uncommitted** work from this session: the change-of-character proposal, this handoff, and the CLAUDE.md / index / memory entries. Last commit: `02970b1e`.
- Narrative state: Part 10 woven with the thought strand (#1918, approved and completed).
