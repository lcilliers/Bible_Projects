# #1995 redraft: reading a verse by the role of each M-coded word

**Date:** 2026-10-11 · **Escalation:** #1995 (raised from #1993) · **Status:** draft for the researcher's review, edited in place per round. Nothing is proposed or applied.

## 1. The instruction (researcher, chat 2026-10-11, verbatim)

> *"1995 was supposed to create a behaviour rule that will remind you to carefully structure the reading of a verse to not get confused between a support M-code and the M-code characteristic that it describes. this would expected your awareness of the role of the M-Codes and structure the reading around it."*

> *"you need to integrate the terminology with the existing terminology in the study, we are not defining new concepts."*

## 2. The study's existing terms this rule rests on

No new concept is defined here. The rule applies terms the study already has:

| Term | Where it is defined | What it says |
|---|---|---|
| **inner being** | glossary (prose 1089); `cfg_prose_concept inner_being_definition` | The governing question: what Scripture reveals about the **characteristics, operations and interrelationships** of the human inner being. |
| **characteristic** | glossary (1047) | Inner-being behaviour. Its composition is **not predefined**; it is known only by inference from behaviour. The lemma, gloss or surface word is **not** a characteristic. |
| **M-code cluster** | glossary (1043); rule 70 | An analytical grouping of Strong's by shared characteristics, and a **loose association**. Cluster codes are anchor points, not goals (#1900). |
| **role** | glossary (1066); verse-analysis method §13 | Each word in a verse has a role: **characteristic** (it behaves as a characteristic of the inner being), **qualifier / process-element** (it binds to a characteristic and gives it value or context in place), or **standalone**. Role is **per occurrence**: the same lemma can be the characteristic in one verse and a qualifier in another (§14, Psa 1:1). |
| **qualifier, no own rollup** | method §13b | A qualifier gives value to its binding pair in place and does not get its own verse rollup. Exception: a qualifier whose usage varies across contexts may earn its own verses later. |
| **operation** | glossary (1048) | What an inner-being activity is doing and how, including to or from others. |
| **T2 / T3** | glossary (1046, 1069) | T2 holds Strong's that only qualify another inner-being term. T3 holds operations not tied to one cluster. |
| **change of character** | #1919 | Each word's faces, the circumstances that differ, and why. |
| **main IB operation** | researcher, 2Pe 2:13 (#1993) | *"The main IB operation of this verse is to suffer … counting it pleasure is the measurement of the reveling."* |

## 3. What went wrong, in these terms

In a strand pull, every verse arrives because of its M-coded word. The error was treating that M-code tag as if it made the word the verse's **characteristic**. The study already says the tag is a loose grouping and the role is decided per occurrence. In 2Pe 2:13 the M18 word "pleasure" has the role of **qualifier** (it measures M28 "revel"). Read as an M18 characteristic, it produced a delight account that the verse does not carry. #1995 v1 fixed the outcome but left out the M-code and role structure that prevents the error.

## 4. The worked case, by role

These are the M-coded words in 2Pe 2:13 (live: `verse_lexical` → `cluster_strong`):

| Word (ESV) | Strong's | M-code | Role in this verse |
|---|---|---|---|
| wrongdoing | G0093 | M58 Wickedness | **characteristic**: the main IB operation is suffering the wage of wrongdoing. |
| revel | G5172 | M28 Envy & Greed | **characteristic** acting with it: what they give themselves to. |
| deceptions | G0539 | M14 Deceit & Falsehood | **qualifier**: it strengthens the reveling ("reveling in their deceptions"). |
| pleasure | G2237 | M18 Desire & Longing | **qualifier**: the measure of the reveling ("count it pleasure"). |
| count | G2233 | M72 Authority & Dominion | **qualifier**: the reckoning that makes it a measure. The tag fits loosely here; under rule 70 the association is recorded, not re-tagged. |

The qualifier bindings (M18 measures M28; M14 strengthens M28) are themselves **interrelationships** of the inner being. They are recorded as such, not dropped.

## 5. Draft rule text (for review)

- **class:** `llm_output`
- **rule_key:** `read-verse-by-role-of-each-mcode-word`
- **rule_text:**

> A strand pulls verses by its M-code, but an M-code tag does not make a word the verse's characteristic. Cluster allocation is a loose association (rule 70), and a word's **role** is decided per occurrence (verse-analysis method §13; glossary *role*). Before reading a verse for a strand:
>
> 1. List every M-coded word in it, with one set-based query (rule 71).
> 2. From the verse in its passage, find the **main IB operation**. Decide which M-coded word or words are in the role of **characteristic**, and which are **qualifiers / process-elements** bound to it (measure, strengthening, ground, object, setting and the like).
> 3. Only then read the strand's own M-code word, in the role it has there.
>
> If the strand's word is a qualifier in this verse:
> - It is read and carried as a qualifier of that characteristic. It does not get its own account from this verse (method §13b).
> - The verse's home follows the characteristic.
> - The binding is recorded as an interrelationship, and as a face of the word (#1919).
>
> A qualifier whose usage varies across contexts may still earn its own reading later (§13b exception).
>
> Existing narrative is not audited for this in a dedicated pass. Placements are corrected in each strand's read-back, as the verse's characteristic M-code comes into focus.

- **source:**
  - researcher, 2026-10-09 on 2Pe 2:13 (#1993, verbatim as in v1), with *"no, we are not redoing it now …"*
  - researcher, 2026-10-11, the two statements in §1
- **enforced_by:** applied when reading strand verses (`context_delivered`).
  - memory `feedback_entry_word_is_not_the_main_operation`, to be reworded in these terms
  - record `m18-group-B-correction-reread-v1-20261009.md`

## 6. For the researcher

1. Is this the right reading of your instruction, with the existing **role** terms (characteristic / qualifier-process-element / standalone)?
2. Once the text is agreed: I would withdraw #1995 v1 and re-propose it with this text through `Config-Maintenance.ps1 -Step Propose`, unless you want it revised in place.
