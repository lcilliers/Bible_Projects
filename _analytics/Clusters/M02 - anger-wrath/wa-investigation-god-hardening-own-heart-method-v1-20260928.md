# Special investigation: does Scripture speak of God hardening his own heart? Method proposal (v1)

**Date:** 2026-09-28 · **Author:** Claude Code · **Status:** method proposal for researcher approval. **Not run.** Escalation #1889.
**Origin:** M02 unit 1, Psa 95:8 (`wa-cluster-M02-phenomena-v2-20260928.md` §12). Filed in the M02 folder because the question started there. **The researcher may redirect the filing**, since the question spans clusters.
**Researcher's brief (2026-09-28, verbatim):** "I think this deserves an extra check through scriptures - I thought that there are reference of God's heart, hardening - but if I am mistaken, then that is a material finding in its own right. … create an escalation for a special investigation to rule out that God hardens his heart."

## 1. The question, stated so that it can be answered either way

**Is there any text in which God's own heart (or spirit, neck or face) is hardened, made heavy or made strong in the hardening sense, whether by God himself or by anyone else?**

- **A positive result:** the texts, each read in context.
- **A negative result:** a **documented** absence, with the search shown to be complete. The brief calls this "a material finding in its own right", so the negative must be as well evidenced as a positive would be.
- **Neighbouring cases are recorded, not counted as positives:**
  - God hardening **human** hearts (Pharaoh, Sihon)
  - God's heart described with **other** words (grieved, turned, moved)
  - God **refusing** or **relenting**

  These are where the premise may have come from, and each is worth naming.

## 2. The coverage problem (found while sizing, before any search)

- **`iba.db` holds 29,760 verses. The Protestant canon has about 31,100.** Even Gen 1 is 30 of 31 verses.
- **So a negative result from `iba.db` alone would not rule anything out.**
- **Proposed:** step 5 below closes the gap against a full text. The source for the full text is the researcher's choice: STEP (`localhost:8989`), or another source the researcher names. **The size and cause of the gap should probably be its own escalation**, since it affects every "every verse" claim in the programme. It is raised in chat, not assumed.

## 3. Method (for approval)

1. **The hardening vocabulary.** Taken from `strong` in `iba.db`, sized 2026-09-28 (verse counts in brackets):
   - Hebrew:
     - *qashah* H7185 (28) / *qasheh* H7186 (36) / *qashach* H7188 (2)
     - *chazaq* H2388G/H/I/J/K (179 / 70 / 3 / 12 / 3)
     - *kaved* H3513G/H/I/J (69 / 32 / 2 / 3)
     - *amats* H0553 (41)
     - *azaz* H5810 (11)
   - Greek:
     - *sklērunō* G4645 (6) / *sklēros* G4642 (5) / *sklērokardia* G4641 (3)
     - *pōroō* G4456 (5) / *pōrōsis* G4457 (3)
   - **About 510 verses in total, 81 with a seat word in the verse.**
   - **To be confirmed by the researcher:** whether to add
     - "stiff-necked" (*qesheh oreph*: already inside H7186)
     - "fat heart" (*shamen*, Isa 6:10)
     - "heart of stone" (Eze 11:19; 36:26)
     - "shut / close" (Job 17:4)
2. **Read every hit.** For each verse, record: the hardening word · what is hardened (heart / spirit / neck / face / other) · **whose** heart it is (God / human / other) · **who** does the hardening. The side is decided by reading, not by Strong's, as in the M02 split.
3. **God's-heart texts from the other direction.** Take every verse where a seat word refers to **God** ("my heart", "his heart" with God as antecedent: Gen 6:6; 8:21; Hos 11:8; Jer 23:20; …). Read each one for any hardening, heaviness or firmness, **whatever word is used.** This catches a hardening expressed without the hardening vocabulary.
4. **The neighbouring texts** (§1): record them in their own table.
5. **Coverage check.** For the verses that are **not** in `iba.db`, run the same searches against the full text chosen in §2, and read any hits.
6. **Output:** `wa-investigation-god-hardening-own-heart-findings-v1-{date}.md` + a ledger CSV with every hit and its reading. Then #1889 goes to ready_for_approval.

## 4. Cost and size

About 510 hardening verses plus the God's-heart set (to be sized in step 3), read in the same way as the M02 verses. **One unit, with a review after it.** No API reads are needed. The coverage check depends on the §2 decision.

## 5. What is asked

1. **Approve the method**, or change it.
2. **The vocabulary additions** in step 1.
3. **The full-text source** for the coverage check, and whether the **29,760 / ~31,100 gap** should be raised as its own escalation.
