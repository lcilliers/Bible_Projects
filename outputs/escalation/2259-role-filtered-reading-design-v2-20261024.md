# #2259 The rules that govern a word's role, and what is not joined up (v2)

**Date:** 2026-10-24 · **Escalation:** #2259, raised from #2161 (M72 Authority & Dominion) · **Supersedes:** `archive/2259-role-filtered-reading-design-v1-20261024.md` · **Status:** a rules map for your review. Nothing has been built and no config has been changed.

Researcher, chat 2026-10-24 (verbatim): *"before I approve I first need to get a handle on the rules that is governing and applying.  your comments in the document seems as if you there are something missing.  I thought that the ib_observation process does exactly what you now describe as new rules."*

## 0. Correction to v1

**You are right, and v1 was wrong.** v1 said no table records a word's role and proposed a new table and a new rule. I had checked only the reading process (`Reading.ps1`, #2228), not the ib_observation process itself.

The ib_observation process, Stage 1 verse-reading, already does this: every occurrence of every M-code word, verse by verse, including the word's role in the verse. Its two steps are live in `cfg_step`. The new table and the new rule in v1 are withdrawn.

What is really missing is narrower, and is in §3.

## 1. The rules that govern the role (all live, from the tables)

### The principle

| Rule | What it says |
|---|---|
| **`cfg_behaviour_rule` 73** *read-verse-by-role-of-each-mcode-word* (general) | An M-code tag does not make a word the verse's characteristic. Each word's role (characteristic, qualifier / process-element, standalone) is decided per occurrence, against the verse's main inner-being operation. A qualifier gets no account of its own from that verse. Guide: `Workflow/Instructions/wa-verse-reading-by-role-guide-v2-20261019.md`. |
| **`cfg_behaviour_rule` 68** *stage1-corrections-only-via-real-rerun* | Stage 1 observations are corrected only by a real re-run. |

### The ib_observation process, Stage 1 verse-reading (per cluster, in two steps)

| Step (`cfg_step`, live) | What it answers, per occurrence (`wa_obs_question_catalogue`) | Method rules (`cfg_method_rule`) |
|---|---|---|
| **`lexical.meaning`** (`iba\app\ps\VerseReading.ps1 -ClusterCode Mxx`) | M0.1 what the word is and means in this occurrence; M0.5 its root and lexical sense here, and where it diverges (M0.5.11) | 70 three meaning sources; 71 the role-annotated word list carries every T2 to T15 role tag; 72 per cluster; 73 M0.1/M0.5; 75 small batches, cost shown before any API call; 108, 111, 112 verse-specific, glossed, span-grounded |
| **`lexical.relational`** (`iba\app\ps\RelationalReading.ps1 -ClusterCode Mxx`) | **M0.6.5** the word's role toward the other M-code words in the verse (causes, enables, intensifies, blocks, responds to, stands in tension; same or different party); M0.6.6 the whole network; **M0.7.1 to 16** whether the word states or implies a purpose or effect for the person (*"otherwise record none"*); **M0.8.1** whether a T2/T3 supporting word is a characteristic in its own right; **D7.7.1** who initiates an operation word, toward whom | 113 to 121 as above; 122 the relational family; **125 readiness gate**: refused unless every M-code word in the verse has its word-level observation; 123 cluster status advances when every live strong has one |

### The tags that carry the judgement (`cfg_setting ib_observation.tag_guidance`)

- `qualifier-for-term`: the word modifies another word's act or quality, rather than naming a disposition in its own right.
- `no-human-context`: a homonym or proper name with no context to analyse. Earmarked and left.
- `tightly-related`: a substantive link to another M-code word.
- `no-direct-connection`: other M-code words are present, but this one does not connect to them.
- `sole-mcode-in-verse`: no other M-code word is in the verse.
- `elevation-candidate`, and others.

So the role you describe (focus, supportive, not related) is recorded word by word in Stage 1, through these answers and tags.

## 2. Where M72 stands in that process

| Fact (live) | Value |
|---|---|
| `cluster.status` of M72 | `t_cluster_assignment_completed` (ordinal 2). **Stage 1 has not been run for M72.** |
| Clusters Stage 1 has been run for | M67 (2,891 verse-reading observations), M83 (1,275), M49 (639); a handful elsewhere |
| M72 verses with a Stage 1 observation on an M72 word | 9 of 3,972 |

## 3. What is not joined up

1. **The reading process does not use Stage 1.**
   - The #2228 design (`outputs/escalation/2228-reading-process-design-v2-20261023.md`) and `iba/app/lib/reading.py` do not mention Stage 1, M0.6.5, M0.7 or rule 73.
   - Gate 1 asks for an observation per verse, written in the session, not for Stage 1's per-word answers.
   - Gate 2 asks that every observation be carried by a claim, held or silent, with no regard to a word's role.

   So the order you set, with the ib_observation process first and the deeper reading filtered on role, is not how the reading runs now.
2. **Stage 1 has no single "not inner-being related" answer.** A "king" used only as a designation would show as M0.7.1 *none*, M0.6.5 *no-direct-connection*, and perhaps `no-human-context` for a name. Whether that combination is a clear enough signal for the filter, or whether Stage 1 needs one answer for it, is your call.

## 4. What this means for #2161

The order would be:
1. Stage 1 for M72 (`lexical.meaning`, then `lexical.relational`), run on the #2161 items one at a time.
2. The deeper reading of each item through `Reading.ps1`, on the verses whose M72 words have an inner-being role.

Running Stage 1 is a cost decision. It makes live API calls over up to 3,972 verses, in small batches, and the step shows the cost before any call (method rule 75).

## 5. Questions for you

| | Question | Your answer |
|---|---|---|
| Q1 | Is §1 the rule set you had in mind: Stage 1 as *the* ib_observation process, with rule 73 governing role? | |
| Q2 | Should the reading process (#2228) take Stage 1 as its first step, with gate 2 filtered on the Stage 1 role answers (§3.1)? | |
| Q3 | Is M0.7.1 *none* together with M0.6.5 *no-direct-connection* enough to mark a word "not inner-being related", or should Stage 1 give that answer itself (§3.2)? | |
