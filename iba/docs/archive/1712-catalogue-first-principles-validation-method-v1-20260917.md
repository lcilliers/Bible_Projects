# Re-deriving the catalogue from the study's actual goal — a method, not another fix

**New thread, split from #1706.** Per researcher instruction, 2026-09-17: *"I think for the first
time you are realising that your previous affirmations that the catalogue is complete... [is] far
from accurate and thorough. To me, that lies at the heart of why role could never really settle
down, because we did not properly think through what it is supposed to do. And this goes for more
than role. What do you suggest we do so you can truly think it through, starting with the end goal:
understanding how the behaviours and characteristics of the inner being work → the questions should
purpose all the dimensions necessary to arrive at that understanding → the questions should be
supported by understanding the data → the pipeline is the process of moving from the base data to
the observations to the answers to questions to the synergy of it all and back to understanding how
the inner being works as described by the Bible."*

## 0. Owning the actual mistake, plainly

You're right, and it's worth naming precisely rather than glossing past. `#1704`'s "Phase 1 is now
genuinely exhaustive" and "zero genericity found anywhere" claims, and my own role-driven-walk
gather today, all checked the catalogue's **internal coherence** — does every existing question have
a wired mechanism, does every existing note_type have a config row — never its **external
adequacy** — does the set of existing questions actually cover what the programme's own stated goal
requires. Those are different questions, and answering the first one confidently reads exactly like
answering the second, which is how "complete" got said when it wasn't. Role kept resurfacing because
it was being treated as a wiring problem (how do we connect T-codes to existing questions) rather
than checked against whether the existing question set was ever derived from what the goal actually
needs in the first place.

## 1. What the end goal actually says — read fresh, not cited from memory

Went to `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260827.md` — chapters 0-3,
the part of the prose you've confirmed reviewed and final (chapters 4-6 describe the older
registry-era architecture and are explicitly superseded by the cluster model). Two passages are
directly load-bearing for this exact question:

**The definition itself, with its operational range** (Chapter 1, "Defining Inner Being"):
*"Inner-being characteristics are the non-physical, internal states, capacities, and expressions
that constitute a person's invisible life — encompassing how a person thinks, feels, chooses,
relates, and orients themselves toward meaning, others, and God."* Five dimensions — think, feel,
choose, relate, orient (toward meaning/others/God) — *"not five sealed domains but five dimensions
of a single integrated life."*

**The permeability clause — this is where "role" actually lives in the programme's own definition**,
not as an implementation detail: *"inner states can be caused by external agents, including God,
other people, and spiritual forces, and the programme's analysis expects and examines that
permeability."* Role — who or what a characteristic is acting in relation to, or being acted on by —
isn't a technical add-on to wire into existing questions after the fact. It's named, explicitly, in
the programme's own working definition of what must be examined. That's very likely why it never
settled: it was being fitted into the existing T0-T7 structure as a mechanism problem, when the
structure itself should have been checked against this clause from the start.

**The method's own governing principle** (Chapter 2, "Research method"): *"Categories are not
imposed on the data; they emerge from it. Dimensions of the inner being are identified by reading
the verses and asking what the verses engage. A category that cannot be grounded in verse evidence
is not a category the programme uses."* This is the test the T0-T7 tier structure itself has never
actually been run through — it's been treated as settled scaffolding to audit *against*, not a
thing to validate.

## 2. The method — your own chain, made into concrete steps

Your framing is already the right shape; this section just turns it into a sequence with a clear
"what output, checked how" per step:

**Step A — confirm the goal-anchor.** §1 above is my reading of Chapters 0-3 as the current,
authoritative statement of what "understanding how the inner being works" means. Needs your
confirmation before anything is built on it — this is the one step where getting the anchor wrong
would make everything downstream wrong too.

**Step B — independently derive the required dimensions/questions, BEFORE looking at the existing
catalogue.** Work from the definition itself (the 5 operational dimensions + the permeability
clause) and ask: to understand how a characteristic manifests across *this*, what distinct questions
must be asked of the evidence? This has to happen with the existing T0-T7 catalogue deliberately not
open alongside it — anchoring on what already exists is exactly the failure mode being corrected.
Output: a goal-derived dimension/question list, produced independent of the current catalogue.

**Step C — for each goal-derived question, work out what data must exist to answer it.** Not "what
data happens to exist in `cluster_strong`," but "what would a question like this actually need
surfaced, given what a verse/passage contains." This is where role data gets its proper grounding —
derived from the permeability clause's own demand, not from an inventory of what columns already
exist.

**Step D — map the pipeline stages against Step C's requirements.** Base data → verse-reading →
char-reading/subgroup → char-answers → synergy — confirm each stage actually produces what Step C
said is needed, closing the loop back to the goal (this is literally your own chain's last arrow).

**Step E — gap analysis, existing vs. required.** Only now compare Step B's independently-derived
list against the live `wa_obs_question_catalogue` (T0-T7, 92 questions) and the live pipeline. Three
outcomes per item: **covered** (a real match), **gap** (goal needs it, catalogue doesn't have it —
`T3` is very likely one of these), **excess** (catalogue has it, but it doesn't trace back to a
goal-derived requirement — worth checking rather than assuming away, e.g. some of `T7.3`'s Science
tier or `T0.3`'s Image-Bearer questions may or may not trace cleanly). This step produces the actual,
evidenced completeness claim — the one `#1704` never had, because it never ran Step B first.

## 3. Why this is a new thread, not another `#1706` round

`#1706` is a build proposal for the lexical stack (Phases A-F). This is a prior, foundational
question — whether the catalogue those phases answer *into* is itself validated against the
programme's own goal. Getting Step E's answer might reshape parts of `#1706`'s own scope (e.g. if
`T3` needs real new questions authored, that's new content `verse_meaning`/`char-reading` would need
to answer into) — so it's upstream of that build, not a parallel track, and deserves its own
escalation rather than being buried as another version of an already-23-version thread.

## 4. Step B — done, two independent derivations, both catalogue-blind

Given the demonstrated risk of me anchoring on my own prior conclusions, Step B was run twice: my
own reading of the full Chapters 0-3 text, and a genuinely blind second pass — a fresh agent given
only the raw prose excerpt (definition, permeability clause, the six scientific fields, the three
methodological principles quoted in §1), no access to this project's files, the existing catalogue,
or any escalation history. **Neither saw the other's answer before producing its own.** They
converged on the same ~12-dimension structure, independently derived from the same clauses:

1. **Cognitive** (thinks) — perception, belief, judgment, reasoning tied to the characteristic.
2. **Affective** (feels) — the felt, experiential quality; transient vs. settled.
3. **Volitional** (chooses) — will, decision, agency, resolve.
4. **Relational — horizontal** (relates, to other people) — direction, and the relational act that results.
5. **Orientational** (orients, toward meaning/God) — the person's fundamental Godward/meaning-directed stance.
6. **Spirit/soul locus** — where on the soul-function/spirit-function spectrum the characteristic sits (a research question per the definition, not a premise).
7. **Permeability / external causation** — the definition's own named axis: is the state caused by God, another person, a spiritual force, or self-generated? **This is where "role" actually lives.**
8. **Embodied expression** — the non-physical test applied: does a bodily/behavioural marker function as *expression* of the state, or is it unrelated material fact?
9. **Physiological substrate & generational transmission** (neuroscience + physiology/epigenetics) — bodily/neural mechanism; inheritance across generations.
10. **Developmental/formational trajectory** (developmental & cognitive psychology) — growth, regression, discipline, correction over time.
11. **Innate endowment vs. acquisition** (genetics/evolutionary biology) — built into human nature vs. shaped by experience/formation.
12. **Social/behavioural manifestation** (behavioural science) — observable social consequence, cooperative or competitive.

Every dimension traces to a specific clause: 1-5 to the definition's own five-part operational
range, 6 to the spirit/soul boundary being named an open research question, 7 to the permeability
clause specifically, 8 to the non-physical test, 9-12 to the four remaining scientific fields (soul
operations/psychology is already covered by 1-3, so it isn't a 13th — checked for overlap, not
just appended).

## 5. First look against the live catalogue — preliminary, not yet the real Step E

Steps C (what data each dimension needs) and D (pipeline mapping) haven't been run yet, so this
isn't the rigorous gap analysis §2 describes — but laying dimensions 1-12 next to the live T0-T7
tiers already shows real structure worth flagging now rather than sitting on:

- **Dimension 7 (permeability) maps to `T4`** — but `T4` is scoped narrowly as bilateral
  "interface" (divine↔human, human↔human exchange), not the full party-kind sweep + T3
  action-word-driven reading the role-driven-walk design wanted. This is very likely *why* role
  never settled: the catalogue's own existing attempt at this dimension undersells what the
  definition's permeability clause actually asks for.
- **Dimensions 1-4 (cognitive/affective/volitional/relational) have no separate tiers at all** —
  they appear to be compressed into the single, recently-authored `T2.11` (Faculty Engagement)
  question, asked once at the end of a read. Whether that consolidation is a deliberate, correct
  design choice or an under-scoping of four dimensions that each need real per-verse investigation
  is exactly the kind of question Step C/D should settle, not something to assume either way here.
- **Dimensions 9-12 (the four science-derived ones) are nominally present** (`T7.3`, 4 questions)
  but thin relative to four distinct dimensions.
- **`T7.1`/`T7.2` (lexical/verse-literary) aren't "dimensions of the inner being" in this derivation
  at all** — they read as evidence-gathering/linguistic-method questions, a different *kind* of
  catalogue content than 1-12, mixed into the same T0-T7 numbering without being distinguished as
  such.
- **Dimension 11 (innate vs. acquired) has partial existing coverage** — `T0.2` ("Created Purpose")
  already asks whether a characteristic "belongs to created design, to the fallen condition, or
  both," a real if narrower version of the same question.

## 6. Steps C and D — checked against live data, not asserted

Per your instruction: every claim below was checked against the live database before being written
down. Where I found real, substantial, usable data, I say so and give the number. Where a mechanism
turned out not to exist, I checked that it doesn't exist (grep'd `cfg_step`, queried row counts) —
not "probably isn't built."

**First, a discovery that reframes several of the dimensions below**: the "T-codes" this whole
thread has been discussing turn out to be **two completely different numbering schemes that happen
to share the same prefix** — a real, previously uncaught source of confusion, not just a naming
nit:

- The **catalogue's tiers** (`T0`–`T7` in `wa_obs_question_catalogue`) are sections of
  characteristic-level questions (T0 = Divine Nature, T4 = Divine/Human Interface, T7 = Lexical/
  Verse/Science, etc.).
- The **role-classification clusters** (`cluster.cluster_code` values `T2`–`T15`, a *separate* set
  of 14 clusters, checked live) are: `T2` Supplementary, `T3` Operations, `T4` **Adversarial**
  (Satan specifically), `T5` Negator, `T6` Connective, `T7` **Party-Divine**, `T8` Party-Human, `T9`
  Party-Angelic, `T10`–`T15` referent-identity (places/corporate/objects/natural-world/body-parts/
  calendar).

Catalogue-`T4` and role-cluster-`T4` are **not the same thing** — catalogue-T4's "Divine Interface"
content actually corresponds to role-clusters `T7`/`T8` (Divine/Human), while catalogue-T4.6
("Spiritual Beings") corresponds to role-clusters `T4`/`T9` (Adversarial/Angelic). Every escalation
in this thread, including my own, has been saying "T4" and meaning whichever scheme was in mind at
the time, without ever stating this collision explicitly. Below, role-cluster codes are always
written as `role-T#` to keep the two apart.

### Dimension-by-dimension, checked

| # | Dimension | Data / mechanism that would answer it | Checked live | Verdict |
|---|---|---|---|---|
| 7 | Permeability (role) | `role-T7`/`role-T8`/`role-T4`/`role-T9` (Divine/Human/Adversarial/Angelic party tags) on strongs co-occurring with an M-code word in the same verse | **Real, substantial.** Of 24,649 verses carrying an M-coded characteristic strong: `role-T7` (Divine) present in **34.9%**, `role-T8` (Human) in **33.8%**, `role-T4`+`role-T9` (Adversarial/Angelic) in **1.9%** combined, `role-T3` (Operations) in **85.8%**. This is real, usable, already-tagged data — not a gap in the base layer. | **Data is practical and available.** The gap is entirely at the catalogue/pipeline layer (catalogue-T4 too narrow, catalogue has no T3 tier at all) — §5's finding stands, sharpened: it's not "no data," it's "real data with nowhere in the catalogue built to receive it." |
| 3 | Volitional / `role-T3` Operations specifically | `role-T3` tag | **Real, dominant.** 2,574 strongs tagged, present in **85.8%** of M-verses — the single most common role tag after the miscellaneous `role-T2` bucket. | **Practical.** Confirms #1704/#1705's own emphasis on T3 was justified by the actual data density, not just argument. |
| — | `role-T2` "Supplementary" — checked because its own name explains nothing | 6,244 strongs, by far the largest role-cluster, **zero rationale on any sampled row**, glosses with no coherent pattern ("shortness," "oil," "delicacy," "razor," "memorial") | Present in **99.5%** of M-verses — so common it can't discriminate anything on its own. | **Not usable as a dimension signal as currently defined.** This isn't one of the 12 goal-dimensions and shouldn't be treated as if it quietly covers one; if it has a real purpose it needs a real description, or it's dead weight in the role scheme. Flagging, not assuming either way. |
| 1, 2, 4, 5 | Cognitive, Affective, Relational, Orientational | No dedicated structural tag exists for any of these (checked: none of the 14 role-clusters represent "mental process," "emotion," "interpersonal act," or "God-ward stance" as such) | N/A — these are answered by direct LLM reading of the existing base text (span/gloss/meaning-source data), same mechanism `reading`'s already-exercised tags (`instance-meaning`, `alternative-meaning`) already use | **Practical, but currently only reached through one consolidated question (`T2.11`)**, asked once at the end of a subgroup's read, not per-verse. Whether that consolidation is adequate or under-scoped is a real open question — not resolved here, since it's a design call about grain, not a data-availability question. |
| 6 | Spirit/soul locus | `M47` cluster membership (spirit/soul/heart/mind, already identified at #1704 v12) | **Real** — 38 strongs, existing cluster, catalogue's own `T2.1` already asks the right question against it | **Practical, already reasonably well-covered.** |
| 8 | Embodied expression (non-physical test) | The reading stage's own `surface-gloss-divergence` tag | **Real, already exercised** — 32 occurrences in the M10 prototype (#1691 §5) | **Practical, already covered** — this dimension doesn't need new work, it already has a working, real mechanism; I missed this the first time through and it's worth saying so plainly. |
| 10 | Developmental/formational | Catalogue's `T5` tier (Nature of Transformation, Sequence, Mechanism of Change) | **Real** — 5 live questions, directly on-target wording | **Practical, already covered.** |
| 11 | Innate vs. acquired | Catalogue's `T0.2` ("Created Purpose": created design vs. fallen condition vs. undetermined) | **Real but partial** — covers the theological half of the question, not the "heritability of temperament" scientific half | **Half-practical from Scripture alone**; the other half needs the science-pass mechanism (see below). |
| 9, 12 (science half) | Physiological substrate/generational transmission; social-behavioural science cross-check | The programme's own documented "science pass" (Chapter 2, "Science in action": 3-question structure, curated reference shelf, 6 fields, deliberately no separate database) | **Checked live: this mechanism has zero footprint in the current pipeline.** `grep`'d `cfg_step`/`cfg_setting` for anything science/reference-shelf-related — nothing. It's fully specified in the prose, for the old Session A-D word-by-word architecture, and was never rebuilt for the cluster/IBA model. | **Not a data problem — a whole mechanism that was never migrated.** This is the single largest, most concrete gap this exercise has found: not a missing tag or a missing tier, a missing *stage* of the pipeline. |

### Step D — pipeline mapping, given the above

- Dimensions **1, 2, 4, 5, 6, 7, 8, 10** (the biblically-derived ones): all answerable from base
  data already in `iba.db` (span/strong/lexicon/`cluster_strong` role tags), through the
  `verse-reading`/`char-reading`/`char-answers` stages this session has already been scoping under
  `#1706`. No new base-data collection is needed — the gap is catalogue/question-design, not data.
- Dimension **3** rides on the same base data, already dense (85.8% coverage) — same pipeline home.
- Dimension **11** splits: its Scripture half belongs in the same pipeline as the others; its
  scientific half does not belong there at all.
- Dimensions **9 and 12's science half** belong to a *separate* mechanism this programme has already
  designed on paper (Chapter 2) but never built for the current architecture — not a `verse-reading`/
  `char-reading` question, a different pipeline stage entirely, closer in shape to the existing
  `narrativegenerate.py` LLM-calling pattern than to the lexical stack.

## 7. What this means, plainly

Most of what this thread has been circling — role never settling, the catalogue's completeness
being asserted rather than checked — traces to two concrete, now-checked causes: (1) the catalogue's
`T4` tier was always narrower than the base data (which is real and substantial) could support, and
`T3` had no tier at all despite being the single densest role signal in the corpus; (2) a whole
documented mechanism (the science pass) was never carried over into the current pipeline, so four of
the twelve goal-dimensions have been silently unanswerable from the day the cluster model replaced
the old architecture. Neither of these is a "go figure out what to do" gap — they're specific,
locatable, checked findings with a clear next step each: author real `T3`-anchored catalogue content
(not a rigid schema, per #1705's own caution — just a real question home), decide whether `role-T2`
needs a real definition or should be retired, and decide whether/how to rebuild the science-pass
mechanism for the current architecture.
