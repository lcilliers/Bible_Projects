# Verse-lexical Window 1 checklist — applied to the validation test set

> Escalation #1383. Step 1 of the pre-build validation plan
> (`iba/docs/1383-verse-lexical-window1-validation-test-plan-v1-20260903.md`): Claude runs the full
> checklist (`iba/docs/1379-verse-lexical-enrichment-checklist-v1-20260902.md`) against 5 passages
> — Deut 6:4-9, Prov 3:5-6, Exod 14:31-15:3, John 1:1-5, Gal 5:16-17 — as one integrated read per
> passage block, per the researcher's own v7 process correction. Greek passages (John, Gal) added
> to the set per direct researcher instruction (2026-09-03), superseding this document's own
> earlier assumption that Greek/NT stayed parked this round. All data pulled live from `iba.db`
> (`verse`/`span`/`verse_lexical`/`strong`/`strong_related`), 2026-09-03. Per the researcher's
> chosen review mode: this document is the full checklist run, filed for the researcher's own
> independent read-and-cross-check next — not yet reviewed.

---

## Passage 1 — Deuteronomy 6:4–9 (the Shema + instruction)

**Gate — genre/language/testament, determined as this read's own first move.** Legal/paraenetic
instruction: second-person direct address, imperative and volitive verbs throughout (love, teach,
talk, bind, write), no narrative frame. Hebrew, OT. **First test of an untested legacy-genre
bucket** (law/narrative) and the **first real multi-verse passage-block test** — six verses, one
integrated read, boundary self-determined at the unit the instruction itself marks off (v4's
opening "Hear, O Israel" through v9's closing "your gates" is one complete rhetorical unit; v10
begins a new topic, "And when the LORD your God brings you into the land..." — checked live, a
clean, uncontested boundary).

### Deut 6:4 — *Hear, O Israel: the LORD our God, the LORD is one.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | Hear | H8085G | HVqv2ms | content |
| 1 | Israel | H3478 | HNpl | content |
| 2 | LORD | H3068G | HNpt | content |
| 3 | God | H0430G | HNcmpc | content |
| 4 | LORD | H3068G+H9025 | HNpt+HSp1bp | content+function |
| 5 | one | H0259 | HNcfsa | content |

**Idiom test.** Negative — no compound span diverges from a literal reading here.
**Pronoun/entity.** `H9025` ("our," pos4) — 1cp, resolves same-verse to the speaking community
implied by the imperative addressee ("Israel," pos1) — Moses addressing the nation, standard for
this genre; recorded resolved, not a genuine crux.
**Noun.** `H0430G`/pos3 and `H3068G`/pos2,4 are the two divine names in apposition — not a
relational-target pair in the checklist's sense (no second party being addressed by the noun),
recorded as a naming/identity construction, distinct from the relational and severity sub-cases.
**Chain/sequencing.** Not applicable — no verb form in this verse; `HVqv2ms` (pos0) is an
imperative, not narrative. Checked, confirmed empty (inert for this test, not a gap).
**Logical/causal.** None present.
**Related words.** `H8085G` ("hear") — large related family, almost entirely proper names sharing
the root (Ishmael, Shema, Shimei, etc.) — mechanically coincidental, no genuine-concept cluster
worth flagging beyond the root itself. Recorded, sorting confirms the checklist's own caution about
this step (a name-heavy root family produces mostly noise) rather than adding a new finding.
**Polarity.** None.
**Data-quality (same code/different gloss).** `H3068G` occurs at pos2 and pos4, identical code and
gloss. Checked — no collision.
**Inert.** None flagged separately this verse — every code above carries content weight or a
resolved possessive.

### Deut 6:5 — *You shall love the LORD your God with all your heart and with all your soul and with all your might.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | love | H0157G | HVqq2ms | content |
| 1 | LORD | H3068G+H0853 | HNpt+HTo | content+content |
| 2 | God | H0430G | HNcmpc | content |
| 3 | all | H3605+H9003+H9021 | HNcmsc+HR+HSp2ms | content+func+func |
| 4 | heart | H3824 | HNcmsc | content |
| 5 | all | H3605+H9003+H9002+H9021 | " | content+func×3 |
| 6 | soul | H5315G | HNcfsc | content |
| 7 | all | H3605+H9003+H9002+H9021 | " | content+func×3 |
| 8 | your | H9021 | HSp2ms | function |
| 9 | might | H3966 | HAcmsc | content |

**Role-classification bug, second live instance.** `H0853` (pos1) is the direct-object marker
again (LORD is the object of "love"), classified `role=content` by the live heuristic — same gap
`#1383`'s design already found and root-fixes (§4). Confirms the fix's scope live, does not add a
new finding.
**Idiom test.** Negative — "with all your X" (pos3/5/7) is a literal construct chain (all + in +
your), not idiomatic; the triad heart/soul/might is a well-known set phrase in translation but each
component reads compositionally from its own code, no combined-span divergence.
**Purposeful classification — noun (severity/quality).** `H3605` ("all," ×3) modifies the intensity
of each following noun (heart/soul/might) without naming a second party — a severity/quality
modifier by the checklist's own definition, not a relational target. Recorded as such, three times,
same pattern each time — mechanically visible from the repeated `H3605+H9003` shape.
**Chain/sequencing.** Not applicable (imperative verb, no narrative morph).
**Related words.** `H0157G` ("love") — related family is same-root love/friend/beloved terms, a
clean cluster, no sorting surprises. `H3824` ("heart") — related family spans genuine
same-concept synonyms (`H3820A`/`H3825`/`H3826`, all "heart") **and** two homonym-looking outliers
sharing the *lb* root shape but unrelated in sense (`H3823B` "to bake," `H3834` "cake") — a real
coincidental case, sorted out explicitly rather than assumed related, the exact discipline the
checklist's related-words step exists to enforce. `H5315G` ("soul") — clean same-concept cluster
(life/person/appetite senses of the same lexeme), no coincidental cases.
**Polarity.** None. **Data-quality.** No same-code/different-gloss collisions found (H3605 recurs
three times, identical gloss each time). **Inert.** `H9003`/`H9002` (×3 each) — pure grammatical
prefixes (in, and), contribute nothing beyond binding; checked, confirmed empty each time.

### Deut 6:6 — *And these words that I command you today shall be on your heart.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | these | H0428+H9009 | HTm+HTd | content+func |
| 1 | words | H1697G+H9009+H1961 | HNcmpa+HTd+HVqq3cp | content+func+content |
| 2 | I | H0595 | HPp1bs | content |
| 3 | command | H6680+H0834A | HVprmsc+HTr | content+content |
| 4 | today | H3117G+H9009+H9031 | HNcmsa+HTd+HSp2ms | content+func+func |
| 5 | on | H5921A | HR | content |
| 6 | your | H9021 | HSp2ms | function |
| 7 | heart | H3824 | HNcmsc | content |

**Idiom test.** Negative. **Pronoun.** `H0595` ("I," pos2) — 1cs, resolves same-verse to the
speaker of the whole address (Moses, consistent with pos0's imperatives) — recorded resolved.
**Noun.** `H1697G` ("words," pos1) is what pos3's "command" governs (its object) — a
relational-target reading, resolved same-verse. **Verb.** `H6680` ("command," pos3) — triggered by
nothing preceding (opens its own clause); impacts `H1697G` (its object, "these words"). `H1961`
("shall be," pos1, bundled into the "words" span as a relative-clause verb — HVqq3cp, "words that
are") is a copular/existential use, not itself chain-triggered.
**Chain/sequencing.** Not applicable — `HVqq3cp` and `HVprmsc` are non-narrative (participle,
perfect-relative), no wayyiqtol present.
**Related words.** `H1697G`/`H3824` already characterised above (heart) or straightforward
(word/speech family, no surprises).
**Data-quality — genuine finding.** `H0834A` (pos3, "which/that") is the SAME code (`H0834A`) that
the original Dan 1:8 pass flagged for a same-code/different-gloss collision. Here it carries only
its relative-particle sense ("that I command"), no collision within this verse — but its
cross-verse polysemy (relative, causal, locative, per its own multi-sense gloss) is worth noting as
a standing candidate for the idiom/context-sensitivity discipline generally, not a new finding this
pass. **Inert.** `H9009` (×2, the definite article) and `H5921A`'s own grammatical binding —
checked, confirmed empty of independent content.

### Deut 6:7 — *You shall teach them diligently to your children, and shall talk of them when you sit in your house, and when you walk by the way, and when you lie down, and when you rise.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | diligently | H8150 | HVpq2ms | content |
| 1 | children | H1121A+H9005+H9038 | HNcmpc+HR+HSp3mp | content+func+func |
| 2 | talk | H1696G+H9021 | HVpq2ms+HSp2ms | content+func |
| 3 | sit | H3427+H9003×2+H9038 | HVqcc+HR+HR+HSp3mp | content+func×3 |
| 4 | house | H1004B+H9003+H9041 | HNcmsc+HR+HSp2ms | content+func×2 |
| 5 | walk | H1980I+H9003+H9002+H9021 | HVqcc+HR+HC+HSp2ms | content+func×3 |
| 6 | way | H1870L+H9003+H9041 | HNcbsa+HRd+HSp2ms | content+func×2 |
| 7 | lie down | H7901G+H9002+H9003 | HVqcc+HC+HR | content+func×2 |
| 8 | you | H9041 | HSp2ms | function |
| 9 | rise | H6965B+H9003+H9002+H9041 | HVqcc+HR+HC+HSp2ms | content+func×3 |

**Idiom test.** `H8150` (pos0), lit. "to sharpen," here does the work of "teach diligently" — a
genuine divergence between the literal root sense and the combined idiomatic reading, the exact
shape of finding the idiom test exists to catch (compare Dan 1:8's "heart"-inside-"resolved").
Flagged as a real idiom instance, not folded silently into the plain gloss.
**Verb — chain by adjacent clause type.** Four infinitive-construct verbs in a row (sit/walk/lie
down/rise, `HVqcc` throughout) — a classic **merism** (a totalizing "whenever you do anything, at
any time" construction via two contrasting pairs: sit/walk = stationary/moving, lie down/rise =
sleep/wake). Not a narrative chain (no wayyiqtol — these are infinitives, temporal clauses, not
sequenced past-tense action) — recorded as a distinct connective/rhetorical pattern the existing
checklist item set does not yet name (neither "narrative chain" nor "logical/causal" fits a merism
cleanly) — flagged as a candidate for the researcher's reconciliation pass, not silently forced into
an existing bucket.
**Related words.** `H1121A` ("children") already characterised (Hos 2:4 pass) — same large,
mostly-proper-name family, sorted the same way. `H1980I` ("walk") — clean same-root motion-verb
family, no surprises.
**Data-quality.** `H9003` recurs 7 times across this verse in different spans, always the same
grammatical binding sense — checked, no collision (this is expected high recurrence for a
frequent function-word, not itself a finding).
**Inert.** All `H9002`/`H9003`/`H9005` instances — confirmed grammatical-only.

### Deut 6:8 — *You shall bind them as a sign on your hand, and they shall be as frontlets between your eyes.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | bind | H7194 | HVqq2ms | content |
| 1 | sign | H0226H+H9005+H9038 | HNcfsa+HR+HSp3mp | content+func×2 |
| 2 | on | H5921A | HR | content |
| 3 | hand | H3027G | HNcbsc | content |
| 4 | be | H1961 | HVqq3cp | content |
| 5 | frontlets | H2903+H9005+H9021 | HNcfpa+HR+HSp2ms | content+func×2 |
| 6 | between | H0996G | HAcmsc | content |
| 7 | your | H9021 | HSp2ms | function |
| 8 | eyes | H5869A | HNcfdc | content |

**Idiom test.** Negative — "sign on your hand" and "frontlets between your eyes" are each literal,
compositional readings (the historical practice of tefillin is a real-world referent, not a
lexical idiom hiding inside the span).
**Noun — severity/relational.** `H0226H` ("sign") and `H2903` ("frontlets") are both governed
objects of the two clauses (what gets bound, what serves as frontlets) — relational-target
readings, both resolved same-verse (bound to "them," `H9038`, referring back to v6's "words").
Note: `H9038` ("them," pos1) is a **cross-verse pronoun reference** — its antecedent ("these
words," Deut 6:6 pos1) is NOT in this verse's own data. Per the checklist's own same-verse-only
rule, this is correctly **unresolved from Deut 6:8 alone** — but because this passage is being read
as one integrated six-verse block (not verse-by-verse in isolation), the antecedent IS available
within the *passage's* own data, just not this *verse's*. **This is exactly the kind of case the
passage-block model exists to handle better than isolated single-verse Window 1 reads did** — flagged
here as a concrete, positive illustration of why the passage-scoped read matters, not a gap.
**Related words.** `H0226H` ("sign") — small, clean family (mark/sign/consent), no surprises.
`H2903` ("frontlets") — **no related rows at all** (checked live, `strong_related` empty for this
code) — recorded as a genuine negative result, not an omission.
**Chain/logical.** Not applicable. **Data-quality.** No collisions. **Inert.** `H9005` (×2, "to/for")
confirmed grammatical-only.

### Deut 6:9 — *You shall write them on the doorposts of your house and on your gates.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | write | H3789 | HVqq2ms | content |
| 1 | on | H5921A+H9038 | HR+HSp3mp | content+func |
| 2 | doorposts | H4201 | HNcfpc | content |
| 3 | house | H1004B | HNcmsc | content |
| 4 | your | H9021 | HSp2ms | function |
| 5 | gates | H8179G+H9003+H9002+H9021 | HNcmpc+HR+HC+HSp2ms | content+func×3 |

**Same cross-verse-pronoun pattern as v8** — `H9038` ("them," pos1) resolves to "these words" only
at the passage level, not within v9 alone. Second confirming instance in the same passage, not a
new finding, but strengthens the v8 observation rather than being a one-off.
**Idiom/related/data-quality/inert.** All negative/clean — no new items this verse.

### Passage 1 — summary

- **First real passage-block test, and it worked as designed**: two genuine cross-verse pronoun
  references (v8 `H9038`, v9 `H9038`) that a strict single-verse read would have to mark
  `unresolved`, but the integrated six-verse block read resolves cleanly and correctly — direct,
  positive evidence for the v7 process correction (one integrated read per block, not isolated
  verses).
- **New idiom instance**: `H8150` ("sharpen" → "teach diligently"), Deut 6:7.
- **New pattern not yet named by the checklist**: the four-infinitive merism (sit/walk/lie
  down/rise) — not narrative chain, not logical/causal. Left for the researcher's reconciliation
  pass, not forced into an existing bucket.
- **`H0853` role-bug**: one more live instance (Deut 6:5), confirms scope, no new information.
- **Boundary**: v4-v9 held as a clean, self-contained unit; v10 opens a new topic. No boundary
  ambiguity in this passage (contrast with Passage 3 below).

---

## Passage 2 — Proverbs 3:5–6 (aphoristic wisdom couplet)

**Gate.** Wisdom/aphoristic, imperative + consequence, second-person address — structurally
different from Ps 25:2's lament-acrostic (already-tested poetic/wisdom sample): tight, two-verse,
antithetic-parallel unit, not an extended prayer. Hebrew, OT.
**Boundary check (this passage's own point of stress).** Is 2 verses a legitimate block on its own,
or does the self-determining read want to pull in v7 ("Be not wise in your own eyes...")? Checked
v7 live: same imperative-address register, thematically continuous (still "trust/don't rely on
self" material) — **a real judgement call, not a clean-cut boundary like Passage 1's**. Recorded
honestly: v5-6 form one complete couplet (command + its own result clause, "and he will make
straight your paths" closes the thought), but v7 could defensibly be folded in as the same
rhetorical unit continues. Left as-is (2 verses, per the confirmed test set) rather than expanded
unilaterally — this ambiguity is itself useful data for the researcher's review, not resolved here.

### Prov 3:5 — *Trust in the LORD with all your heart, and do not lean on your own understanding.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | Trust | H0982 | HVqv2ms | content |
| 1 | LORD | H3068G+H0413 | HNpt+HR | content+content |
| 2 | all | H3605+H9003 | HNcmsc+HR | content+func |
| 3 | heart | H3820A | HNcmsc | content |
| 4 | not | H0408+H9021 | HTn+HSp2ms | content+func |
| 5 | lean | H8172 | HVNj2ms | content |
| 6 | on | H0413 | HR | content |
| 7 | understanding | H0998+H9021+H9002 | HNcfsc+HSp2ms+HC | content+func×2 |

**Idiom test.** Negative on the individual spans; but the **verse-level antithetic pairing itself**
(trust-in-LORD // do-not-lean-on-your-own-understanding) is the real rhetorical unit — a structural
observation the checklist's per-code items don't have a slot for (same gap class as Passage 1's
merism finding).
**Verb.** `H0982` ("trust") — same code as Ps 25:2's pos1, already-characterised related family
(security/confidence cluster, clean). Object = `H0413`+LORD (relational target, resolved
same-verse). `H8172` ("lean," Niphal jussive) — negated by `H0408` (pos4); its "object" (what NOT
to lean on) is `H0998` ("understanding," pos7) via the second `H0413` (pos6) — resolved same-verse.
**Related words.** `H0998` ("understanding") — related family is overwhelmingly proper names built
on the same root (Bunah, Jabin, etc.) plus the genuine-concept sibling `H0995`/`H0999`
("understand"/"understanding") and, interestingly, `H1004B` ("house") — **checked, this is a
coincidental homograph** (a different root that happens to share consonants in this list), not a
real semantic link — sorted out explicitly, the same discipline as Deut 6:5's `H3824`/"bake" case.
**Polarity.** `H0408` (pos4) — same negator code as Ps 25:2's two instances; consistent with the
already-recorded cross-verse negator-family note.
**Data-quality/Inert.** No collisions; `H9003` (pos2) confirmed grammatical-only.

### Prov 3:6 — *In all your ways acknowledge him, and he will make straight your paths.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | In | H9003 | HR | function |
| 1 | all | H3605 | HNcmsc | content |
| 2 | ways | H1870G | HNcmpc | content |
| 3 | acknowledge | H3045+H9021 | HVqv2ms+HSp2bs | content+func |
| 4 | he | H1931 | HPp3ms | content |
| 5 | straight | H3474+H9033+H9002 | HVpi3ms+HSp3ms+HC | content+func×2 |
| 6 | your | H9021 | HSp2ms | function |
| 7 | paths | H0734 | HNcfpc | content |

**Idiom test.** Negative on the individual spans.
**Pronoun.** `H1931` ("he," pos4) — 3ms, resolves same-verse... **but the real referent is
theological, not grammatical**: the natural antecedent is "the LORD" from v5 (cross-verse again,
same pattern as Deut 6:8-9), not any 3ms noun within v6 itself. Checked v6 alone: no 3ms noun
present at all — this pronoun is **unresolvable from v6's own data**, correctly flagged
`unresolved` under the strict single-verse rule, and correctly **resolved at the passage level**
(v5's `H3068G`) under the integrated-block read — a third confirming instance of the same
passage-block value already seen twice in Passage 1. `H9033` ("him," pos5, 3ms) — same subject,
same resolution.
**Verb.** `H3045` ("acknowledge," lit. "know") — imperative, same root family as the checklist's
"knowledge" cluster (clean, no surprises). `H3474` ("make straight") — subject is the resolved "he"
above; object is "your paths" (`H0734`, pos7) — resolved same-verse once the passage-level subject
resolution is accepted.
**Related words.** `H1870G` ("ways") — same root family as Deut 6:7's `H1870L` ("way," already
noted) — a genuine cross-passage lexical link (same lemma, different sense-application: Deut 6:7's
literal "the road," Prov 3:6's figurative "conduct/ways of life") — worth recording as evidence
that the related-word step surfaces real connections even across this test set's own passages, not
just within one.
**Data-quality/Inert.** No collisions; `H9003` (pos0) grammatical-only, `H9002` (pos5)
grammatical-only.

### Passage 2 — summary

- **Fourth cross-verse-pronoun instance** (`H1931`/`H9033` "he/him" → v5's "the LORD"), reinforcing
  the passage-block finding from Passage 1 on a completely different genre/structure.
- **A genuine, honestly-recorded boundary judgement call** (does the block properly end at v6, or
  continue to v7?) — the first time this validation run has hit real boundary ambiguity, useful
  precisely because it did NOT resolve cleanly like Passage 1.
- **Structural finding not covered by any per-code checklist item**: verse-level antithetic
  parallelism (trust-vs-lean) — same gap class as Passage 1's merism.

---

## Passage 3 — Exodus 14:31–15:3 (the genre seam: narrative into the Song of the Sea)

**Gate.** This is the deliberate stress test. v14:31 opens as narrative (third person, past
action). v15:1 is the pivot ("Then Moses and the people of Israel sang this song to the LORD,
saying..."). v15:2-3 is direct quoted poetry (first-person praise, no narrative frame). **Hebrew,
OT.**

### Exod 14:31 — *Israel saw the great power that the LORD used against the Egyptians, so the people feared the LORD, and they believed in the LORD and in his servant Moses.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | Israel | H3478 | HNpl | content |
| 1 | saw | H7200G | **HVqw3ms** | content |
| 2 | great | H1419A+H9009 | HAafsa+HTd | content+func |
| 3 | power | H3027H+H9009+H0853 | HNcbsa+HTd+HTo | content+func+content |
| 4 | LORD | H3068G | HNpt | content |
| 5 | used | H6213A+H0834A | HVqp3ms+HTr | content+content |
| 6 | Egyptians | H4714G+H9003 | HNpl+HR | content+func |
| 7 | people | H5971A+H9009 | HNcmsa+HTd | content+func |
| 8 | feared | H3372H | **HVqw3mp** | content |
| 9 | LORD | H3068G+H0853 | HNpt+HTo | content+content |
| 10 | believed | H0539 | **HVhw3mp** | content |
| 11 | LORD | H3068G+H9003 | HNpt+HR | content+func |
| 12 | servant | H5650+H9023 | HNcmsc+HSp3ms | content+func |
| 13 | Moses | H4872+H9002+H9003 | HNpm+HC+HR | content+func×2 |

**Chain/sequencing — genuine positive Hebrew narrative case, the first beyond Dan 1:8 in this
project's own record.** Three wayyiqtol forms in sequence: `H7200G` "saw" (`HVqw3ms`) →
`H3372H` "feared" (`HVqw3mp`) → `H0539` "believed" (`HVhw3mp`) — a textbook narrative chain
(see→fear→believe), morphologically unambiguous. **This closes the residual gap the Ps 25:2/Hos 2:4
pass explicitly flagged** ("neither test verse is narrative prose... needs a genuine positive
Hebrew narrative case beyond Dan 1:8") — confirmed here, live, on fresh data.
**Role-bug, third and fourth live instances.** `H0853` at pos3 and pos9 — both direct-object
markers, both classified `content` by the live heuristic. Two more confirming instances in one
verse.
**Idiom test.** Negative — each span reads compositionally.
**Verb — triggered-by/impacts, full chain.** "saw" opens (untriggered), impacts "power" (its
object, marked by `H0853`). "feared" is triggered by "saw" (the chain), impacts nothing further
explicit (intransitive). "believed" is triggered by "feared," impacts "the LORD... and his servant
Moses" (a double object, via two `H9003`-marked phrases).
**Related words.** `H3372H` ("fear") and `H0539` ("believe/faithful," root of "amen") both have
large, thematically central families — not pulled in full here (out of scope for this validation
pass's depth) but flagged as strong candidates for a full pull once this method reaches scale.
**Data-quality.** No same-code/different-gloss collisions (H3068G recurs 3× in this verse alone,
identical gloss each time). **Inert.** `H9009` (×2, article), `H9003` (×2, prepositional prefix)
confirmed grammatical-only.

### Exod 15:1 — *Then Moses and the people of Israel sang this song to the LORD, saying, "I will sing to the LORD, for he has triumphed gloriously; the horse and his rider he has thrown into the sea.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | Moses | H4872 | HNpm | content |
| 1 | people | H1121G+H9002 | HNcmpc+HC | content+func |
| 2 | Israel | H3478 | HNpl | content |
| 3 | sang | H7891+H0227A | **HVqi3ms**+HD | content+content |
| 4 | song | H7892B+H9009+H0853 | HNcfsa+HTd+HTo | content+func+content |
| 5 | LORD | H3068G+H9005+H2063+H9009 | HNpt+HR+HTm+HTd | content+func+content+func |
| 6 | saying | H0559+H0559 | **HVqw3mp**+HVqcc | content+content |
| 7 | sing | H7891 | HVqc1cs | content |
| 8 | LORD | H3068G+H9005 | HNpt+HR | content+func |
| 9 | for | H3588A | HTc | content |
| 10 | triumphed | H1342 | HVqaa | content |
| 11 | gloriously | H1342 | HVqp3ms | content |
| 12 | horse | H5483M | HNcmsa | content |
| 13 | rider | H7392 | HVqrmsc | content |
| 14 | thrown | H7411A+H9023 | HVqp3ms+HSp3ms | content+func |
| 15 | sea | H3220G+H9003 | HNcmsa+HRd | content+func |

**The pivot itself, examined directly — a genuine, live, evidenced finding about the chain test's
own limits.** "Sang" (pos3, `H7891`) carries morph `HVqi3ms` — **Qal IMPERFECT, not wayyiqtol** —
paired with `H0227A` ("then," *az*). This is the classical Biblical Hebrew **`az` + imperfect**
construction used to open elevated/poetic narrative (the same construction that opens the Song of
Deborah, Judg 5:1, and several other embedded poems) — it functions as a past-narrative report
("then Moses... sang") but its morphology does **not** carry the wayyiqtol marker the chain test
looks for. **The chain test, run mechanically on this verse alone, would report a negative/no-fire
result at exactly the point a human reader would call this "the next event in the story."**
However: `H0559` ("saying," pos6) — the verse's OTHER verb — **does** carry `HVqw3mp` (a true
wayyiqtol, bundled with a second, infinitive-construct occurrence of the same code, the standard
Hebrew "and-they-said-saying" double-verb quotative frame). **So the chain test's mechanical signal
does still fire on this verse — just on the second verb, not the one a reader would naturally point
to first.** This is exactly the kind of finding this validation phase exists to surface: the test
is not wrong, but a naive "does this verse contain a wayyiqtol, yes/no" read could miss that the
*narratively primary* verb of the pivot line uses a different, non-wayyiqtol narrative-opening
form. Recorded as a genuine checklist refinement candidate — the chain test may need to explicitly
name the `az`-imperfect construction as an ADDITIONAL narrative-sequencing signal alongside
wayyiqtol, not assume wayyiqtol is the only positive case — left for the researcher's
reconciliation call, not decided unilaterally here.
**Role-bug, fifth instance.** `H0853` at pos4 (song is the object of "sang/saying").
**Idiom test.** `H0559`+`H0559` (pos6) is itself a compound-span idiom — two occurrences of "to
say" bundled as one span, the standard Hebrew quotative frame ("and he said, saying") that
English naturally drops one half of — flagged as a real idiom-shaped finding, the second one this
run (after Deut 6:7's `H8150`).
**Related words.** `H3588A` ("for," pos9) — same code already characterised in the Hos 2:4 pass
(causal-connective family); this instance is worth a is-it-a-logical-connective check (see below).
**Logical/causal — genuine second instance.** `H3588A` (pos9, "for/because") links "I will sing"
to its ground/reason ("for He has triumphed gloriously") — the same causal-connective shape Hos 2:4
surfaced, confirming it as a recurring, real pattern (not a one-off), strengthening #1383 §4's
decision to fold it in permanently.
**Data-quality.** `H3068G` recurs at pos5, 8 — identical gloss both times, no collision. `H1342`
occurs at pos10 (`HVqaa`, infinitive absolute) and pos11 (`HVqp3ms`, perfect) — **same code,
different morph, classic Hebrew infinitive-absolute + finite-verb intensifying construction**
("triumphed, he has triumphed" → "triumphed gloriously") — not a data-quality collision (the gloss
is consistent), but a genuine idiom-adjacent finding worth noting alongside the pos6 case: this
verse alone contributes two Hebrew doubled-verb intensification/quotative idioms, both correctly
readable from the row data once you know to look for the pattern.

### Exod 15:2 — *The LORD is my strength and my song, and he has become my salvation; this is my God, and I will praise him, my father's God, and I will exalt him.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | LORD | H3050 | HNpm | content |
| 1 | strength | H5797 | HNcmsc | content |
| 2 | song | H2176+H9002+H9020 | HNcfsc+HC+HSp1bs | content+func×2 |
| 3 | become | H1961 | **HVqw3ms** | content |
| 4 | salvation | H3444+H9005×2+H9030 | HNcfsa+HRd+HR+HSp1bs | content+func×3 |
| 5 | this | H2088 | HTm | content |
| 6 | God | H0410G | HNcmsc | content |
| 7 | praise him | H5115A+H9020 | HVhu1cs+HSp1bs | content+func |
| 8 | father's | H0001G | HNcmsc | content |
| 9 | God | H0430G+H9033 | HNcmpc+HSp3ms | content+func |
| 10 | I | H9020 | HSp1bs | function |
| 11 | exalt | H7311A | HVpu1cs | content |
| 12 | him | H9033 | HSp3ms | function |

**A genuine, real nuance for the "is genre a clean binary" question this passage was chosen to
test.** `H1961` (pos3, "has become") carries `HVqw3ms` — **wayyiqtol, inside the Song itself**,
which is otherwise pure first-person praise poetry with no other narrative-morph verbs anywhere in
this or the next verse. This is a known feature of archaic Hebrew poetry (the Song of the Sea is
among the oldest strata of Biblical Hebrew and retains some vestigial narrative-style forms inside
what is structurally a hymn) — **directly relevant to the researcher's own framing that genre is a
passage property, not a per-morph one**: if the chain test were applied per-code rather than
informed by the passage's own already-determined genre, this single wayyiqtol would incorrectly
suggest "narrative sequencing" is happening inside a verse that is, as a whole, unambiguously
poetic praise addressed to God in first person. **Confirms, with real evidence, that genre
determination has to be a whole-passage judgement the read makes first (per the v7 process
correction) and the chain test has to be read in light of it — not the reverse.**
**Idiom test.** Negative on other spans. **Pronoun.** `H9020` ("my," ×3: pos2, 7, 10) and `H9030`
("me," pos4) — all 1cs, resolve same-verse to the speaker (consistent throughout the Song).
`H9033` ("him," ×2: pos9, 12) — 3ms, resolves same-verse to "God" (pos6/9, both `H0410G`/`H0430G`)
— the addressee shifts from direct address ("LORD," pos0, vocative-adjacent) to third-person
praise ("I will praise him... I will exalt him") within the same verse, mechanically visible and
correctly trackable from morph alone.
**Related words.** Not pulled in full for this verse's remaining content words (out of scope depth
for this validation pass, consistent with Exod 14:31's note).
**Data-quality.** `H0430G` recurs (Deut 6:4's "God" code) — consistent gloss, no collision across
this test set's own passages either. **Inert.** `H9002`/`H9005` confirmed grammatical-only.

### Exod 15:3 — *The LORD is a man of war; the LORD is his name.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | LORD | H3068G | HNpt | content |
| 1 | man | H0376G | HNcmsc | content |
| 2 | war | H4421 | HNcfsa | content |
| 3 | LORD | H3068G | HNpt | content |
| 4 | name | H8034+H9023 | HNcmsc+HSp3ms | content+func |

**Idiom test.** Negative. **Noun.** `H0376G` ("man") construct-bound to `H4421` ("war") — a
severity/quality-modifier reading ("man OF war," characterising what kind of man), not a relational
target — same category as Hos 2:4's "children of whoredom," a direct structural echo across two
different test verses in two different sessions, worth noting as continuity evidence for this
checklist item's own reliability. **Pronoun.** `H9023` ("his," pos4) — 3ms, resolves same-verse to
"the LORD" (pos3), the nearest antecedent, and to the discourse-level subject of the whole Song —
both readings agree here, no genuine ambiguity. **Chain/logical/related/data-quality/inert.** No
narrative morph (pure nominal-clause poetry, no verbs at all in this verse — a genuinely inert
verse for the chain test, worth recording as such rather than silently skipping it). No collisions.

### Passage 3 — summary

- **Closes the single biggest residual gap from the original two-verse pass**: a genuine positive
  Hebrew narrative chain (Exod 14:31, three wayyiqtol verbs), confirming the chain test works on
  real narrative prose beyond Dan 1:8.
- **The genre-seam stress test produced real, structured findings, not a clean pass-or-fail**:
  - The pivot verse (15:1) uses `az`+imperfect for its primary narrative verb, not wayyiqtol — the
    chain test still fires (on the verse's second verb), but on a different word than intuition
    would point to. Concrete refinement candidate for the checklist.
  - A wayyiqtol form appears **inside** the poem proper (15:2) — direct evidence that per-morph
    signals must be read in light of a passage-level genre call, not treated as sufient on their
    own, i.e. exactly the case for the researcher's "one integrated read, genre first" model.
- **Two more Hebrew doubled-verb idioms** found (15:1's "said, saying" quotative frame; "triumphed,
  he has triumphed" intensifier) — a positive result for the idiom test's value on real narrative
  material.
- **Two more `H0853` role-bug instances**, bringing this run's live total to 5.

---

## Passage 4 — John 1:1–5 (Johannine Prologue opening) — first Greek/NT test

**Gate.** Hymnic/theological prose, not narrative, despite sitting inside a gospel book — the exact
mismatch the researcher's own prior finding (#1379 v6) already established for this verse range at
the abstract level; **this pass is the first time the underlying verse_lexical row data has
actually been pulled for it.** Greek, NT.
**Boundary — an honest correction to this document's own framing.** This passage was originally
selected as a "genre-boundary stress test" on the assumption that vv1-5 themselves span a seam.
Checked directly against the actual text and standard structural reading: **they do not.** vv1-5
are one continuous hymnic unit (the "Word" strophe); the real prose/hymn boundary in John 1 sits
between v5 and v6, where narrative resumes ("There was a man sent from God, whose name was John").
This passage doesn't reach that boundary. **Recorded honestly rather than forcing a boundary claim
the data doesn't support** — the genuine genre-boundary evidence in this validation run comes from
Passage 3, not this one. This passage's real value is being the first Greek/NT test, per the
researcher's direct instruction, and reinforcing the existing genre-mismatch finding with real row
data for the first time.

**A live data-integrity finding, not part of the checklist itself, surfaced while pulling this
passage's data — filed as its own escalation (#1441), not worked around silently:** John 1:5's 9
live `verse_lexical` rows all point at `span` rows that are themselves soft-deleted (a stale
foreign-key leftover from an old span rebuild) — the live, current spans for this verse have zero
`verse_lexical` rows joined to them. The actual code/morph/role data is intact on the deleted-span
rows, so this verse's checklist entry below is still complete and accurate, but any ordinary query
joining only to live spans would silently return nothing for this verse. Confirmed live: this
affects 824 verses project-wide (13,621 rows), not unique to John 1:5.

### John 1:1 — *In the beginning was the Word, and the Word was with God, and the Word was God.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | In | G1722 | PREP | function |
| 1 | beginning | G0746 | N-DSF | content |
| 2 | was | G1510 | V-IAI-3S | content |
| 3 | Word | G3056 | N-NSM | content |
| 4 | and | G2532 | CONJ | function |
| 5 | Word | G3056 | N-NSM | content |
| 6 | was | G1510 | V-IAI-3S | content |
| 7 | with | G4314 | PREP | function |
| 8 | God | G2316 | N-ASM-T | content |
| 9 | and | G2532 | CONJ | function |
| 10 | Word | G3056 | N-NSM | content |
| 11 | was | G1510 | V-IAI-3S | content |
| 12 | God | G2316 | N-NSM-T | content |

**Chain/sequencing — not applicable, no Greek equivalent exists yet.** Recorded as
`not_supported_this_language`, per #1383 §3.G's own recommendation, rather than silently treated as
"checked, negative" (that phrasing is reserved for a real test that fires empty; this is a test
that doesn't exist yet for this language).
**Idiom test.** Negative on individual spans — this is famously dense THEOLOGY, not lexical idiom;
nothing here hides a divergent combined sense the way Dan 1:8's "resolved" did.
**Noun — a genuinely interesting classification case.** `G3056` ("Word," ×3, pos3/5/10) recurs
identically each time — a clean data-quality check (confirmed, no collision) — but its
*referential* behaviour across the verse is itself a Window-1-relevant fact: same code, same
morph, but the entity it names shifts rhetorical position each time (subject of "was" → object of
"was with" → predicate of "was God"). This is exactly the kind of same-code-recurrence-with-shifting-
role pattern the existing checklist doesn't have a dedicated slot for (distinct from the Hos
2:4-style "H1121A recurs, no drift" case, where the role stayed constant) — flagged as a candidate
refinement, not resolved here.
**Entity-linking.** `G2316` ("God," pos8/12) — pos8 carries morph-tag suffix `-T` (a step-specific
"Titus/theological" marker on the accusative form) not present on pos12's nominative form — worth
noting as a live example of Greek morph-tag granularity the Hebrew-side checklist items were never
designed against (case-and-article-sensitive distinctions with no Hebrew parallel).
**Related words.** `G3056` — related family includes genuine same-concept siblings (`G3051`
"oracles," `G3050` "spiritual" adjacent) and clearly coincidental root-shares (`G0945` "to babble,"
`G4180` "wordiness") — sorted, same discipline as the Hebrew-side finds. `G2316` ("God") — a large
compound-word family (God-hating, God-fighting, God-breathed, etc.) — genuinely related by
morphological composition, not coincidental, a different shape of "related" than the Hebrew root-
family cases (Greek compounding vs. Hebrew triliteral-root sharing) — worth flagging as a
methodological note for how "related word" should be read differently by language, once Greek
scales up.
**Polarity/data-quality/inert.** No negation present. `G2532` (×2, "and") confirmed
grammatical-only.

### John 1:2 — *He was in the beginning with God.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | He | G3778 | D-NSM | content |
| 1 | was | G1510 | V-IAI-3S | content |
| 2 | in | G1722 | PREP | function |
| 3 | beginning | G0746 | N-DSF | content |
| 4 | with | G4314 | PREP | function |
| 5 | God | G2316 | N-ASM-T | content |

**Pronoun.** `G3778` ("He/this," pos0) — resolves same-verse-and-passage to "the Word" (John
1:1's `G3056`) — a genuine test of the pronoun-resolution rule on Greek data for the first time:
resolves cleanly, at the passage level (same pattern already seen repeatedly on the Hebrew side in
Passages 1-2), not within v2 alone (v2 has no explicit noun of its own for "He" to agree with) —
**sixth confirming instance of the passage-block pronoun-resolution value this run has now found**,
and the first on Greek data specifically.
**Everything else** (idiom, chain, related, polarity, data-quality, inert) — same pattern as v1,
no new findings; `G0746`/`G2316`/`G1722`/`G4314` all recur with identical glosses, checked, no
collisions.

### John 1:3 — *All things were made through him, and without him was not any thing made that was made.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | All | G3956 | A-NPN | content |
| 1 | made | G1096 | V-2ADI-3S | content |
| 2 | through | G1223 | PREP | function |
| 3 | him | G0846 | P-GSM | content |
| 4 | and | G2532 | CONJ | function |
| 5 | without | G5565 | PREP | function |
| 6 | him | G0846 | P-GSM | content |
| 7 | not | G3761 | CONJ-N | function |
| 8 | any thing | G1520 | A-NSN | content |
| 9 | made | G1096 | V-2ADI-3S | content |
| 10 | that | G3739 | R-NSN | content |
| 11 | made | G1096 | V-2RAI-3S | content |

**Pronoun.** `G0846` (×2, pos3/6, "him") — resolves same-verse-and-passage to "the Word"/"God"
(the same chain established in vv1-2) — resolved.
**Polarity — first Greek negation instance.** `G3761` (pos7, "not/nor") negates "any thing made" —
a double-negative-shaped construction in the Greek ("without him was not anything made") — flagged
structurally, not sorted further this pass.
**Idiom test.** Negative on individual spans; the verse's own chiastic doubling ("was made... that
was made") is a rhetorical-repetition structure, not a lexical idiom hiding inside one span —
`G1096` (×3: pos1, 9, 11) recurring with two different morph tags (`V-2ADI-3S` twice, `V-2RAI-3S`
once — aorist-passive vs. perfect-active-parsed forms of the same lemma) is a genuine
data-quality-adjacent, same-code-different-morph case, the Greek-side counterpart to Exod 15:1's
Hebrew infinitive-absolute finding — recorded, not a collision (different tense-forms are expected
variation, not an error), but worth the same "same code, watch the morph" discipline.
**Related/data-quality/inert.** No new findings beyond the above.

### John 1:4 — *In him was life, and the life was the light of men.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | In | G1722 | PREP | function |
| 1 | him | G0846 | P-DSM | content |
| 2 | was | G1510 | V-IAI-3S | content |
| 3 | life | G2222 | N-NSF | content |
| 4 | and | G2532 | CONJ | function |
| 5 | life | G2222 | N-NSF | content |
| 6 | was | G1510 | V-IAI-3S | content |
| 7 | light | G5457 | N-NSN | content |
| 8 | men | G0444 | N-GPM | content |

**Idiom test.** Negative on individual spans — "life"/"light" as a paired image is a
theological/rhetorical move at the verse level, not a hidden combined-span sense.
**Related words.** `G2222` ("life") — related family is a clean same-concept cluster (`G2198` "to
live," the `G5590` "soul" family) — genuinely load-bearing for an inner-being-adjacent study (life
↔ soul, the same shape of finding Hos 2:4's compassion↔womb pull produced on the Hebrew side).
`G5457` ("light") — small, clean family (`G5461` "to illuminate" only).
**Data-quality.** `G2222` recurs (pos3/5), identical gloss, no collision — same pattern as `G3056`
in v1, another same-code-shifting-rhetorical-role case (subject → predicate).

### John 1:5 — *The light shines in the darkness, and the darkness has not overcome it.* (data recovered from the orphaned-span rows — see escalation #1441)

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | light | G5457 | N-NSN | content |
| 1 | shines | G5316 | V-PAI-3S | content |
| 2 | in | G1722 | PREP | function |
| 3 | darkness | G4653 | N-DSF | content |
| 4 | and | G2532 | CONJ | function |
| 5 | darkness | G4653 | N-NSF | content |
| 6 | not | G3756 | PRT-N | function |
| 7 | overcome | G2638 | V-2AAI-3S | content |
| 8 | it | G0846 | P-ASN | content |

**Genre gate, re-confirmed on the actual verse this project's prior finding was built around.**
Consistent with #1379 v6's own conclusion: this verse is hymnic/theological, part of the same
prologue strophe as vv1-4, not narrative — the legacy `bible_research.db` book-level tag
("gospel-narrative") remains confirmed too coarse for this stretch, now backed by the actual row
data rather than the verse text alone.
**Pronoun.** `G0846` ("it," pos8) — resolves same-verse to "the light" (pos0, `G5457`) — the
grammatical object of "overcome" — resolved.
**Polarity.** `G3756` (pos6, "not") negates "overcome" — the second Greek negation this run,
structurally simple (single negator, unlike Gal 5:16's double-negator case below).
**Idiom test.** Negative. **Related words.** `G4653` ("darkness") — related family is a clean
same-concept cluster (dark/darkness/to darken), no surprises. `G5316` ("shines") — related family
includes `G5318` ("clear/plain") and `G5457` itself ("light") — a genuine, direct lexical
connection between "shines" and "light" as used in this very verse, mechanically surfaced.
**Data-quality.** `G4653` recurs (pos3/5) with different case-morph (`N-DSF` vs `N-NSF` — dative
vs. nominative, "in the darkness" vs. "the darkness [itself]") — not a collision, expected
case-inflection variation, same discipline as `G1096`/`G2222` above.

### Passage 4 — summary

- **First Greek/NT data actually pulled and checklist-tested.** Confirms: pronoun resolution works
  the same way on Greek data (2 clean passage-level resolutions, `G3778`→Word, `G0846`→light); the
  idiom/related-words/data-quality/inert tests all transfer directly; polarity found 2 real
  instances; the chain/sequencing test correctly has nothing to test against (recorded
  `not_supported_this_language`, not silently skipped).
- **A live data-integrity bug found and escalated** (#1441, John 1:5's orphaned span links,
  affecting 824 verses project-wide) — not worked around silently.
- **This document's own original framing corrected**: vv1-5 do not span a genre boundary; the real
  boundary is v5→v6, outside this passage. Recorded honestly.
- **Two candidate checklist refinements**: same-code-recurrence-with-shifting-rhetorical-role
  (`G3056`, `G2222`) as its own observable pattern; Greek "related word" families skew toward
  compound-morphology relationships rather than Hebrew's root-sharing, worth a language-aware note
  once this scales.

---

## Passage 5 — Galatians 5:16–17 (epistle, exhortative/argumentative prose)

**Gate.** Epistle — argumentative prose, direct address ("I say"), antithetical structure (Spirit
vs. flesh). Greek, NT. Untested legacy-genre bucket for this run (epistle), and thematically
central to the whole IBA project (inner-being conflict language).

### Gal 5:16 — *But I say, walk by the Spirit, and you will not gratify the desires of the flesh.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | But | G1161 | CONJ | function |
| 1 | say | G3004G | V-PAI-1S | content |
| 2 | walk | G4043 | V-PAM-2P | content |
| 3 | Spirit | G4151G | N-DSN | content |
| 4 | and | G2532 | CONJ | function |
| 5 | not | G3756+G3361 | PRT-N+PRT-N | function+function |
| 6 | gratify | G5055 | V-AAS-2P | content |
| 7 | desires | G1939 | N-ASF | content |
| 8 | flesh | G4561 | N-GSF | content |

**Idiom test — a genuine, load-bearing finding.** Pos5 is a **compound span carrying two distinct
negator codes** (`G3756` "ou" + `G3361` "mē") on what English renders as one word, "not." This is
the classic Koine Greek **οὐ μή (ou mē) emphatic-negation construction** — "certainly not / by no
means," grammatically stronger than either negator alone. **This is exactly the idiom test's job**:
a combined span whose meaning is not simply the sum of its parts read separately — the single
strongest idiom-test finding of this whole validation run, on Greek data, the first language this
particular idiom-shape has been tested against.
**Polarity.** The `ou mē` construction above IS this verse's polarity finding — recorded once,
correctly not double-counted as two separate negations.
**Verb — triggered by/impacts.** `G4043` ("walk," imperative) opens the exhortation; governed
object is "by the Spirit" (`G4151G`, dative of means). `G5055` ("gratify," lit. "finish/complete")
— negated by the `ou mē` compound; its object is "the desires of the flesh" (`G1939`+`G4561`,
construct-genitive).
**Noun — relational vs. severity.** `G1939` ("desires") construct-bound to `G4561` ("flesh") — a
severity/quality reading (what KIND of desires — fleshly ones), not a relational target, same
category as Deut 6:5's "all your heart" triad and Hos 2:4's "children of whoredom" — fourth
confirming instance of this pattern across the whole run, now on Greek data too.
**Related words.** `G4151G` ("Spirit") — related family includes `G4152`/`G4153`
("spiritual"/"spiritually") — clean same-concept cluster, directly relevant to inner-being
vocabulary. `G4561` ("flesh") — small, clean family (`G4559`/`G4560`, "fleshly").
**Chain/sequencing.** Not applicable (no Greek equivalent). **Data-quality/inert.** No collisions;
`G1161`/`G2532` confirmed grammatical-only.

### Gal 5:17 — *For the desires of the flesh are against the Spirit, and the desires of the Spirit are against the flesh, for these are opposed to each other, to keep you from doing the things you want to do.*

| pos | surface | code | morph | role |
|---|---|---|---|---|
| 0 | For | G1063 | CONJ | function |
| 1 | desires | G1937 | V-PAI-3S | content |
| 2 | flesh | G4561 | N-NSF | content |
| 3 | against | G2596 | PREP | function |
| 4 | Spirit | G4151G | N-GSN | content |
| 5 | and | G1161 | CONJ | function |
| 6 | Spirit | G4151G | N-NSN | content |
| 7 | against | G2596 | PREP | function |
| 8 | flesh | G4561 | N-GSF | content |
| 9 | for | G1161 | CONJ | function |
| 10 | these | G3778 | D-NPN | content |
| 11 | opposed | G0480 | V-PNI-3S | content |
| 12 | each other | G0240 | C-DPN | content |
| 13 | to | G2443 | CONJ | function |
| 14 | doing | G4160G | V-PAS-2P | content |
| 15 | things | G3778+G1437 | D-APN+COND | content+content |
| 16 | want | G2309 | V-PAS-2P | content |

**Idiom test — second finding.** Pos15's compound (`G3778`+`G1437`, "this/these" + "if/ever") is
the Greek indefinite-relative idiom **ὅσα ἐάν / ἃ ἐάν** ("whatever things") — a combined sense not
recoverable by reading either code alone (`G1437` alone is a plain conditional "if," not
"whatever") — same idiom-test shape as pos5 in v16, the second Greek idiom this run has found.
**Chiastic structure — a real finding, no checklist slot.** "Desires of flesh against Spirit... /
desires of Spirit against flesh" is an exact chiasm (`G4561`+`G4151G` then `G4151G`+`G4561`,
mirrored) — the same class of verse-level rhetorical-structure finding already flagged in Passage
2 (antithetic parallelism) and Passage 4 (life/light pairing) — a recurring gap across every
passage in this run, worth treating as a real, cross-language, cross-genre pattern for the
reconciliation pass, not a one-off.
**Noun — relational.** `G4561`/`G4151G`, each time, is the relational target the other party's
"desire" is directed against (`G2596`, "against") — resolved same-verse, both directions.
**Pronoun.** `G3778` ("these," pos10) — resolves same-verse to the two just-named parties
(flesh-desire and Spirit-desire) — resolved. `G3778`+`G1437` (pos15) — its referent ("the things you
want to do") is generic/non-specific by the construction's own grammar, not a resolvable antecedent
— correctly not flagged unresolved (there is no missing antecedent to find; the indefinite is the
point).
**Data-quality.** `G4561` and `G4151G` each recur twice with mirrored case-morphs (nominative vs.
genitive, matching the chiasm) — not a collision, confirms the structural finding above rather than
being a separate item.
**Related words.** `G1937` ("desires," a different lemma from v16's `G1939` despite the same
English gloss — checked live, genuinely two distinct Greek roots both glossed "desire" in
translation) — **a real same-English-gloss/different-Greek-lemma finding**, the inverse of the
usual same-code/different-gloss check, and a case this checklist's current data-quality item
doesn't explicitly cover (it checks same-CODE-different-gloss; this is different-code-same-gloss) —
flagged as a genuine candidate addition for the reconciliation pass.
**Chain/inert.** Not applicable / no new findings.

### Passage 5 — summary

- **Two genuine Greek idioms found** (the `ou mē` emphatic double-negative, v16; the `ho ean`
  indefinite-relative, v17) — the idiom test transfers cleanly to Greek and finds real,
  non-obvious combined-span meanings, same value as the Hebrew-side finds.
- **A recurring cross-passage structural gap, now confirmed in 3 of 5 passages** (Passage 2's
  antithetic parallelism, Passage 4's life/light pairing, this passage's exact chiasm) — worth
  treating as its own checklist item candidate in the reconciliation pass, not three unrelated
  one-offs.
- **A genuine new data-quality-adjacent finding**: different Greek lemmas sharing one English
  gloss (`G1937` vs `G1939`, both "desire") — the inverse case of the existing same-code-check,
  not yet covered by any current item.

---

## What this run adds, across all 5 passages — for the researcher's reconciliation pass

Per the validation test plan's own methodology (§4), every item below needs sorting into
**checklist gap** / **genuine judgement call** / **checklist correct** — none pre-decided here:

1. **Cross-verse pronoun/entity resolution via the passage-block read** — 6 confirming instances
   across 3 different passages and both languages (Deut 6:8-9 ×2, Prov 3:6, John 1:2/1:5, Gal
   5:17) — the single strongest, most repeated result of this whole run, directly validating the
   v7 "one integrated read per passage" process correction with real data, not just the design
   argument for it.
2. **A second confirmed positive Hebrew narrative chain** (Exod 14:31) — closes the residual gap
   the original two-verse pass flagged.
3. **The chain test's blind spot at genre pivots**: `az`+imperfect (Exod 15:1) carries real
   narrative force but not the wayyiqtol morph the test looks for; a wayyiqtol can appear *inside*
   poetry (Exod 15:2) without the passage being narrative. Both argue for genre-first,
   passage-level reading exactly as already decided — but suggest the chain test's own rule may
   need an explicit `az`+imperfect clause added.
4. **Verse-level rhetorical/structural patterns with no current checklist slot**: merism (Deut
   6:7), antithetic parallelism (Prov 3:5-6), chiasm (Gal 5:17), paired-image juxtaposition (John
   1:4) — four instances, different languages, different genres — a real, recurring gap class, not
   a one-off.
5. **Greek/NT confirmed workable for every existing test** except chain/sequencing (no equivalent
   built, correctly recorded `not_supported_this_language` each time, not silently skipped) — 2
   genuine Greek idioms found, related-words and pronoun-resolution both transfer directly.
6. **Two data-quality-adjacent refinements**: same-code-recurrence-with-shifting-rhetorical-role
   (`G3056`, `G2222`, `H1121A`-style but now cross-language); different-lemma-same-English-gloss
   (`G1937`/`G1939`) — the inverse of the existing same-code check.
7. **A sixth live `H0853` role-bug instance count** (5 in this run alone, on top of the original
   Hos 2:4 find) — confirms scope, no new information, strengthens the case for #1383 §4's
   root-fix.
8. **A live data-integrity bug found and escalated separately** (#1441) — not a checklist finding,
   but surfaced by this same data-pull discipline.
9. **One honest self-correction**: Passage 4 does not actually span a genre boundary as originally
   framed — recorded rather than forced.
10. **One genuine, unresolved boundary judgement call** (Passage 2, does the block end at v6 or
    extend to v7) — the first real boundary ambiguity this run has hit, useful precisely because it
    didn't resolve cleanly.
