# Registry grounding — does every anchor word have a related term?

> READ-ONLY (`scripts/_assess_registry_grounding.py`). Tests each registry word against its OWN terms (`strongs_list`/`phase1_term_count`), not the cluster-keyword vocabulary. GROUNDED-LEXICAL = has terms + word is a keyword · GROUNDED-COGNATE = has terms but the word isn't the gloss token (relates via cognate/synonym) · EMPTY = no terms. No DB writes.

**215 registry rows · GROUNDED-LEXICAL 164 · GROUNDED-COGNATE 21 · EMPTY 30.**

## EMPTY — registry words with NO terms (the real gap; your expectation breaks here)

| # | word |
|---|---|
| 9 | assent |
| 10 | awareness |
| 12 | betrayal |
| 14 | blamelessness |
| 21 | commitment |
| 22 | communion |
| 25 | conformity |
| 36 | cowardice |
| 37 | darkening |
| 38 | deadness |
| 45 | determination |
| 54 | emotion |
| 79 | hopelessness |
| 82 | identity |
| 84 | image of god |
| 88 | ingratitude |
| 95 | intuition |
| 101 | laziness |
| 106 | manipulation |
| 118 | personality |
| 119 | personhood |
| 133 | reliability |
| 136 | resentment |
| 141 | self-awareness |
| 143 | sensitivity |
| 145 | sexuality |
| 195 | spiritual powers |
| 154 | stupor |
| 161 | transformation |
| 169 | vulnerability |

## GROUNDED-COGNATE — has related terms, but the anchor word isn't the gloss token

| anchor word | related term(s) — why it didn't surface as the keyword |
|---|---|
| **anointing** | G0218 aleifō = to anoint; G0220 aleimma = an anointing |
| **boastfulness** | H3515 ka.ved = heavy; H3513G ka.ved = to honor: honour |
| **brokenness** | H7667 she.ver = breaking; H0226G ot = sign: miraculous |
| **consciousness** | G4893 suneidesis = conscience; G4894 suneidō = be aware |
| **consecration** | H5145G ne.zer = consecration: Nazirite vow; H6942G qa.dash = to consecrate: consecate |
| **deadness** | G3498 nekros = dead; H4191 mut = to die |
| **division** | H5921A al = upon; H4256 ma.cha.lo.qet = division |
| **loyalty** | H2616B cha.sad = to shame; H2617A che.sed = kindness |
| **meaning** | G1411 dunamis = power; G1412 dunamoō = to empower |
| **might** | H6696A tsur = to confine; H5810 a.zaz = be strong |
| **recognition** | G4894 suneidō = be aware; G2589 kardiognōstēs = heart-knower |
| **resentment** | G3709 orgē = wrath; G3710 orgizō = to anger |
| **seeking** | H1245 ba.qash = to seek; G2212 zēteō = to seek |
| **sloth** | H7496 re.pha.im = shade; H6103 ats.lah = sluggishness |
| **sorcery** | G5331 farmakeia = sorcery; H3784 ka.shaph = to practice sorcery |
| **surrender** | H3318G ya.tsa = to come out: come; H0859A at.tah = you [m.s.] |
| **vulnerability** | H6168 a.rah = to uncover; H6174 a.rom = naked |
| **whoredom** | H8457 taz.nut = fornication; H2183 ze.nu.nim = fornication |
| **will** | G2372 thumos = wrath; H2087 za.don = arrogance |
| **worth** | H2063 zot = this; H3660 ke.ne.ma = thus |
| **yearning** | H4261 mach.mad = desire; H2550 cha.mal = to spare |

## Duplicate registry rows

- **deadness** — rows [38, 210]
- **resentment** — rows [136, 205]
- **transformation** — rows [161, 202]
- **vulnerability** — rows [169, 206]
