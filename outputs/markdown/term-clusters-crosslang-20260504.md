# Hebrew/Greek cluster cross-language alignment

**Generated:** 2026-05-04T10:00:45Z
**Hebrew clusters analysed:** 80
**Greek clusters analysed:** 40

## Method

Each cluster's centroid is computed in the **semantic-only vector space** (weighted root + gloss + meaning). Co-occurrence vectors are excluded because they're language-locked (Hebrew/Greek share no verses). Cosine similarity between Greek and Hebrew centroids quantifies lexical-semantic alignment. Theme-word overlap quantifies shared vocabulary.

Verdict scale:
- **ALIGNED** — top-1 similarity ≥ 0.55 AND ≥ 1 shared theme word
- **PARTIAL** — 0.40 ≤ top-1 < 0.55, OR sim high but no shared theme
- **ORPHAN** — top-1 < 0.40 (no close Hebrew counterpart)

## Greek → Hebrew verdicts

| Verdict | Count |
|---|---|
| ALIGNED | 6 |
| PARTIAL | 29 |
| ORPHAN | 5 |

## Hebrew → Greek verdicts

| Verdict | Count |
|---|---|
| ALIGNED | 10 |
| PARTIAL | 61 |
| ORPHAN | 9 |

## Greek clusters — ALIGNED

### Greek C9 (n=32) → Hebrew C4 (sim=0.64, shared=2)

**Greek theme:** desire(3), will(2), anger(2), ignorant(1), brotherhood(1), praise(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C4 (n=39) | 0.64 | desire, innocent | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |
| 2 | C54 (n=46) | 0.6372 | — | distress(4), compassion(3), pain(3), disease(2), evil(2), cruel(1) |
| 3 | C63 (n=22) | 0.6263 | — | firebrand(1), trust(1), silence(1), vexed(1), joy(1), burning(1) |

### Greek C8 (n=31) → Hebrew C58 (sim=0.6347, shared=1)

**Greek theme:** peace(2), without(1), anxiety(1), unchangeable(1), endure(1), openness(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C58 (n=26) | 0.6347 | peace | peace(6), medium(1), strong(1), trust(1), unite(1), terror(1) |
| 2 | C29 (n=24) | 0.6268 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 3 | C75 (n=62) | 0.625 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |

### Greek C18 (n=22) → Hebrew C4 (sim=0.6172, shared=1)

**Greek theme:** sin(2), able(2), good(1), cause(1), charge(1), sinful(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C4 (n=39) | 0.6172 | sin | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |
| 2 | C29 (n=24) | 0.6089 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 3 | C58 (n=26) | 0.568 | — | peace(6), medium(1), strong(1), trust(1), unite(1), terror(1) |

### Greek C12 (n=28) → Hebrew C75 (sim=0.6144, shared=1)

**Greek theme:** hell(2), plan(2), good(1), choose(1), sense(1), hearing(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C75 (n=62) | 0.6144 | choose | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 2 | C29 (n=24) | 0.5839 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 3 | C4 (n=39) | 0.5787 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |

### Greek C11 (n=20) → Hebrew C29 (sim=0.5967, shared=1)

**Greek theme:** quiet(2), foolish(2), understanding(2), worthy(1), unwise(1), judge(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C29 (n=24) | 0.5967 | shame | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 2 | C58 (n=26) | 0.5956 | — | peace(6), medium(1), strong(1), trust(1), unite(1), terror(1) |
| 3 | C42 (n=17) | 0.5952 | foolish | folly(3), fool(2), foolish(2), ish(1), bitterness(1), hatred(1) |

### Greek C27 (n=22) → Hebrew C29 (sim=0.5748, shared=1)

**Greek theme:** shameful(1), ashamed(1), interpreter(1), interpret(1), assembly(1), praise(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C29 (n=24) | 0.5748 | seek | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 2 | C75 (n=62) | 0.5661 | seek | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 3 | C4 (n=39) | 0.5485 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |

## Greek clusters — PARTIAL

### Greek C28 (n=32) → Hebrew C29 (sim=0.6761, shared=0)

**Greek theme:** holiness(3), joy(1), choose(1), sin(1), lawlessness(1), disobey(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C29 (n=24) | 0.6761 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 2 | C4 (n=39) | 0.6465 | sin | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |
| 3 | C75 (n=62) | 0.6116 | choose | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |

### Greek C1 (n=24) → Hebrew C63 (sim=0.6418, shared=0)

**Greek theme:** fight(1), discouraged(1), sect(1), mute(1), terrified(1), trembling(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C63 (n=22) | 0.6418 | — | firebrand(1), trust(1), silence(1), vexed(1), joy(1), burning(1) |
| 2 | C54 (n=46) | 0.6295 | — | distress(4), compassion(3), pain(3), disease(2), evil(2), cruel(1) |
| 3 | C75 (n=62) | 0.626 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |

### Greek C3 (n=33) → Hebrew C29 (sim=0.6398, shared=0)

**Greek theme:** dwell(2), groan(2), holiness(1), indulgence(1), deprivation(1), incorruptibility(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C29 (n=24) | 0.6398 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 2 | C75 (n=62) | 0.6288 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 3 | C4 (n=39) | 0.6249 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |

### Greek C15 (n=28) → Hebrew C4 (sim=0.6384, shared=0)

**Greek theme:** evil(3), quarrel(2), hypocrisy(2), unrighteousness(1), impurity(1), become(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C4 (n=39) | 0.6384 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |
| 2 | C54 (n=46) | 0.6323 | evil | distress(4), compassion(3), pain(3), disease(2), evil(2), cruel(1) |
| 3 | C12 (n=16) | 0.6073 | — | disheartened(2), humble(2), contempt(1), greatness(1), vexation(1), intestine(1) |

### Greek C30 (n=24) → Hebrew C54 (sim=0.6382, shared=0)

**Greek theme:** indignation(1), rest(1), faint(1), seize(1), torment(1), doubt(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C54 (n=46) | 0.6382 | — | distress(4), compassion(3), pain(3), disease(2), evil(2), cruel(1) |
| 2 | C63 (n=22) | 0.6255 | — | firebrand(1), trust(1), silence(1), vexed(1), joy(1), burning(1) |
| 3 | C75 (n=62) | 0.6041 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |

### Greek C2 (n=33) → Hebrew C75 (sim=0.6343, shared=0)

**Greek theme:** praise(2), covenant(2), marvel(2), name(2), renew(1), reconcile(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C75 (n=62) | 0.6343 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 2 | C29 (n=24) | 0.6067 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 3 | C58 (n=26) | 0.5955 | — | peace(6), medium(1), strong(1), trust(1), unite(1), terror(1) |

### Greek C24 (n=34) → Hebrew C29 (sim=0.6317, shared=0)

**Greek theme:** joy(3), love(2), heart(2), kind(2), goodness(1), holy(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C29 (n=24) | 0.6317 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 2 | C58 (n=26) | 0.6298 | — | peace(6), medium(1), strong(1), trust(1), unite(1), terror(1) |
| 3 | C75 (n=62) | 0.6275 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |

### Greek C6 (n=21) → Hebrew C29 (sim=0.6257, shared=0)

**Greek theme:** pray(2), petition(1), listen(1), charity(1), intercession(1), long(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C29 (n=24) | 0.6257 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 2 | C75 (n=62) | 0.6099 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 3 | C58 (n=26) | 0.5927 | long | peace(6), medium(1), strong(1), trust(1), unite(1), terror(1) |

### Greek C35 (n=25) → Hebrew C29 (sim=0.6243, shared=0)

**Greek theme:** quiet(2), good(1), beloved(1), uncondemned(1), rekindle(1), disobedience(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C29 (n=24) | 0.6243 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 2 | C63 (n=22) | 0.6045 | — | firebrand(1), trust(1), silence(1), vexed(1), joy(1), burning(1) |
| 3 | C54 (n=46) | 0.6023 | — | distress(4), compassion(3), pain(3), disease(2), evil(2), cruel(1) |

### Greek C34 (n=50) → Hebrew C75 (sim=0.6242, shared=0)

**Greek theme:** quarrel(3), false(2), good(1), praise(1), schismatic(1), intemperate(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C75 (n=62) | 0.6242 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 2 | C63 (n=22) | 0.6117 | — | firebrand(1), trust(1), silence(1), vexed(1), joy(1), burning(1) |
| 3 | C4 (n=39) | 0.6103 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |

### Greek C10 (n=15) → Hebrew C29 (sim=0.6212, shared=0)

**Greek theme:** holy(1), place(1), harm(1), true(1), perplexed(1), oppress(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C29 (n=24) | 0.6212 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 2 | C4 (n=39) | 0.6063 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |
| 3 | C75 (n=62) | 0.5818 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |

### Greek C36 (n=29) → Hebrew C54 (sim=0.6181, shared=0)

**Greek theme:** thought(3), anguish(2), innocent(1), merciless(1), senseless(1), untrustworthy(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C54 (n=46) | 0.6181 | — | distress(4), compassion(3), pain(3), disease(2), evil(2), cruel(1) |
| 2 | C58 (n=26) | 0.6089 | — | peace(6), medium(1), strong(1), trust(1), unite(1), terror(1) |
| 3 | C29 (n=24) | 0.6057 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |

### Greek C38 (n=13) → Hebrew C54 (sim=0.6153, shared=0)

**Greek theme:** deceit(1), dishonor(1), willed(1), give(1), desire(1), lordship(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C54 (n=46) | 0.6153 | — | distress(4), compassion(3), pain(3), disease(2), evil(2), cruel(1) |
| 2 | C4 (n=39) | 0.6049 | desire | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |
| 3 | C63 (n=22) | 0.5954 | — | firebrand(1), trust(1), silence(1), vexed(1), joy(1), burning(1) |

### Greek C4 (n=19) → Hebrew C29 (sim=0.6143, shared=0)

**Greek theme:** release(3), change(1), tolerance(1), get(1), back(1), indecency(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C29 (n=24) | 0.6143 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 2 | C4 (n=39) | 0.611 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |
| 3 | C54 (n=46) | 0.595 | — | distress(4), compassion(3), pain(3), disease(2), evil(2), cruel(1) |

### Greek C0 (n=23) → Hebrew C4 (sim=0.6141, shared=0)

**Greek theme:** clean(2), purity(1), purify(1), purification(1), pure(1), shame(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C4 (n=39) | 0.6141 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |
| 2 | C29 (n=24) | 0.5628 | shame | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 3 | C12 (n=16) | 0.5622 | — | disheartened(2), humble(2), contempt(1), greatness(1), vexation(1), intestine(1) |

### Greek C32 (n=32) → Hebrew C4 (sim=0.6079, shared=0)

**Greek theme:** weak(2), call(2), sister(1), distressed(1), anoint(1), anointing(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C4 (n=39) | 0.6079 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |
| 2 | C75 (n=62) | 0.6067 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 3 | C54 (n=46) | 0.606 | — | distress(4), compassion(3), pain(3), disease(2), evil(2), cruel(1) |

### Greek C5 (n=19) → Hebrew C75 (sim=0.6063, shared=0)

**Greek theme:** impartial(1), renewal(1), merciless(1), sufficiency(1), abominable(1), image(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C75 (n=62) | 0.6063 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 2 | C58 (n=26) | 0.6047 | — | peace(6), medium(1), strong(1), trust(1), unite(1), terror(1) |
| 3 | C29 (n=24) | 0.6025 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |

### Greek C13 (n=28) → Hebrew C75 (sim=0.5991, shared=0)

**Greek theme:** stumbling(4), weak(2), block(2), bold(1), not(1), weakness(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C75 (n=62) | 0.5991 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 2 | C44 (n=25) | 0.5985 | — | devise(2), wicked(2), god(1), prevail(1), defend(1), honor(1) |
| 3 | C63 (n=22) | 0.5982 | — | firebrand(1), trust(1), silence(1), vexed(1), joy(1), burning(1) |

### Greek C22 (n=17) → Hebrew C35 (sim=0.5965, shared=0)

**Greek theme:** good(2), anointing(2), pure(1), true(1), dishonour(1), slander(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C35 (n=24) | 0.5965 | — | bitterness(2), cheerful(1), silence(1), shine(1), prune(1), confidence(1) |
| 2 | C12 (n=16) | 0.5942 | — | disheartened(2), humble(2), contempt(1), greatness(1), vexation(1), intestine(1) |
| 3 | C54 (n=46) | 0.5867 | — | distress(4), compassion(3), pain(3), disease(2), evil(2), cruel(1) |

### Greek C16 (n=24) → Hebrew C75 (sim=0.5943, shared=0)

**Greek theme:** power(2), active(2), make(2), struggle(1), unbelief(1), chosen(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C75 (n=62) | 0.5943 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 2 | C68 (n=22) | 0.583 | — | strength(2), meditation(2), anxiety(1), crush(1), enrage(1), pour(1) |
| 3 | C16 (n=37) | 0.5701 | power | strength(12), strong(3), mighty(2), power(2), man(1), burst(1) |

### Greek C7 (n=16) → Hebrew C29 (sim=0.5839, shared=0)

**Greek theme:** worry(2), eager(1), expectation(1), hope(1), expect(1), devout(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C29 (n=24) | 0.5839 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 2 | C75 (n=62) | 0.5796 | bless | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 3 | C58 (n=26) | 0.571 | — | peace(6), medium(1), strong(1), trust(1), unite(1), terror(1) |

### Greek C26 (n=12) → Hebrew C54 (sim=0.5791, shared=0)

**Greek theme:** without(1), falling(1), plunder(1), weakness(1), control(1), merciful(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C54 (n=46) | 0.5791 | — | distress(4), compassion(3), pain(3), disease(2), evil(2), cruel(1) |
| 2 | C4 (n=39) | 0.529 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |
| 3 | C29 (n=24) | 0.5102 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |

### Greek C19 (n=22) → Hebrew C54 (sim=0.5613, shared=0)

**Greek theme:** rub(2), darkness(2), darken(2), boasting(1), sound(1), nakedness(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C54 (n=46) | 0.5613 | — | distress(4), compassion(3), pain(3), disease(2), evil(2), cruel(1) |
| 2 | C4 (n=39) | 0.5562 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |
| 3 | C75 (n=62) | 0.5555 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |

### Greek C39 (n=22) → Hebrew C29 (sim=0.5584, shared=0)

**Greek theme:** idol(2), necessary(1), wrong(1), domineer(1), timid(1), temple(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C29 (n=24) | 0.5584 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 2 | C75 (n=62) | 0.5551 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 3 | C4 (n=39) | 0.5275 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |

### Greek C21 (n=10) → Hebrew C54 (sim=0.5565, shared=0)

**Greek theme:** braggart(1), unholy(1), blasphemous(1), compassionate(1), slanderous(1), minded(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C54 (n=46) | 0.5565 | — | distress(4), compassion(3), pain(3), disease(2), evil(2), cruel(1) |
| 2 | C12 (n=16) | 0.5454 | — | disheartened(2), humble(2), contempt(1), greatness(1), vexation(1), intestine(1) |
| 3 | C63 (n=22) | 0.5411 | — | firebrand(1), trust(1), silence(1), vexed(1), joy(1), burning(1) |

### Greek C23 (n=15) → Hebrew C29 (sim=0.5352, shared=1)

**Greek theme:** command(2), unclean(1), throw(1), away(1), ordinance(1), edict(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C29 (n=24) | 0.5352 | shame | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 2 | C75 (n=62) | 0.5294 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 3 | C4 (n=39) | 0.5239 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |

### Greek C14 (n=19) → Hebrew C29 (sim=0.5106, shared=0)

**Greek theme:** ruler(2), causer(1), irrevocable(1), beginning(1), founder(1), first(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C29 (n=24) | 0.5106 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 2 | C75 (n=62) | 0.4963 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 3 | C72 (n=15) | 0.4937 | — | height(2), contempt(1), exult(1), queen(1), arrogant(1), arrogance(1) |

### Greek C17 (n=21) → Hebrew C4 (sim=0.4854, shared=0)

**Greek theme:** test(6), tempt(4), testing(3), temptation(2), rejoice(1), tested(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C4 (n=39) | 0.4854 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |
| 2 | C63 (n=22) | 0.4649 | — | firebrand(1), trust(1), silence(1), vexed(1), joy(1), burning(1) |
| 3 | C29 (n=24) | 0.4561 | — | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |

### Greek C31 (n=21) → Hebrew C58 (sim=0.4128, shared=0)

**Greek theme:** love(5), loving(5), controlled(2), not(1), greedy(1), sober(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C58 (n=26) | 0.4128 | — | peace(6), medium(1), strong(1), trust(1), unite(1), terror(1) |
| 2 | C75 (n=62) | 0.4112 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 3 | C63 (n=22) | 0.4063 | — | firebrand(1), trust(1), silence(1), vexed(1), joy(1), burning(1) |

## Greek clusters — ORPHAN

### Greek C29 (n=16) → Hebrew C4 (sim=0.3916, shared=0)

**Greek theme:** just(2), crime(1), unjust(1), opponent(1), justice(1), righteousness(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C4 (n=39) | 0.3916 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |
| 2 | C29 (n=24) | 0.3889 | justice, righteousness | keep(4), justice(2), righteousness(2), seek(1), profane(1), begin(1) |
| 3 | C44 (n=25) | 0.3618 | opponent | devise(2), wicked(2), god(1), prevail(1), defend(1), honor(1) |

### Greek C33 (n=7) → Hebrew C72 (sim=0.3206, shared=2)

**Greek theme:** reign(2), kingdom(1), palace(1), kingly(1), royal(1), queen(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C72 (n=15) | 0.3206 | kingdom, queen | height(2), contempt(1), exult(1), queen(1), arrogant(1), arrogance(1) |
| 2 | C64 (n=24) | 0.2987 | — | consecration(3), pillar(1), leader(1), terebinth(1), flask(1), mix(1) |
| 3 | C75 (n=62) | 0.2812 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |

### Greek C20 (n=13) → Hebrew C75 (sim=0.3118, shared=0)

**Greek theme:** deliver(3), gift(3), free(2), give(2), repay(1), pay(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C75 (n=62) | 0.3118 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 2 | C4 (n=39) | 0.2786 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |
| 3 | C37 (n=17) | 0.2783 | — | pour(2), contribution(2), arches(1), length(1), judge(1), set(1) |

### Greek C37 (n=8) → Hebrew C30 (sim=0.3089, shared=0)

**Greek theme:** slave(4), enslave(3), slavery(1), female(1), fellow(1)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C30 (n=16) | 0.3089 | — | refuse(2), deer(1), beloved(1), pure(1), defile(1), unclean(1) |
| 2 | C22 (n=9) | 0.2919 | — | found(1), longing(1), story(1), torment(1), rule(1), guard(1) |
| 3 | C4 (n=39) | 0.2899 | — | sin(8), guilty(2), offering(2), ransom(2), innocent(2), iniquity(2) |

### Greek C25 (n=9) → Hebrew C75 (sim=0.2876, shared=0)

**Greek theme:** remembrance(4), remember(3), remind(2)

Top 3 Hebrew matches:

| Rank | Hebrew C | sim | shared themes | Hebrew theme |
|---|---|---|---|---|
| 1 | C75 (n=62) | 0.2876 | — | seek(2), rule(2), prolong(1), dismay(1), choose(1), trust(1) |
| 2 | C58 (n=26) | 0.286 | — | peace(6), medium(1), strong(1), trust(1), unite(1), terror(1) |
| 3 | C37 (n=17) | 0.2843 | — | pour(2), contribution(2), arches(1), length(1), judge(1), set(1) |

## Hebrew clusters with no close Greek counterpart (ORPHAN)

Count: 9

| Hebrew C | n | top sim to Greek | Hebrew theme |
|---|---|---|---|
| C10 | 18 | 0.3045 (G C5) | hand(17), palm(1) |
| C20 | 11 | 0.2261 (G C23) | reckon(5), appointment(1), punishment(1), deposit(1), oversight(1), precept(1) |
| C24 | 10 | 0.373 (G C32) | master(4), rule(2), mistress(1), delight(1), maiden(1), abomination(1) |
| C71 | 10 | 0.3171 (G C2) | serve(4), service(4), work(2) |
| C25 | 10 | 0.3269 (G C34) | call(4), encounter(3), assembly(1), chosen(1), proclamation(1) |
| C69 | 9 | 0.2901 (G C8) | living(2), live(2), alive(1), kinsfolk(1), thing(1), community(1) |
| C66 | 9 | 0.3486 (G C22) | glorious(1), riches(1), rank(1), row(1), anointed(1), division(1) |
| C78 | 9 | 0.2812 (G C34) | end(4), perfection(2), consumption(1), failing(1), limit(1) |
| C46 | 7 | 0.3212 (G C22) | honor(3), heaviness(2), liver(1), glory(1) |