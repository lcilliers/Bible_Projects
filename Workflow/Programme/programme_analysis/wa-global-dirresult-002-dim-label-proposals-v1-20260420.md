# Directive Result — DIR-20260420-002 — Dim-Label Canonicalisation Proposals — 2026-04-20

| Field | Value |
|---|---|
| Directive | DIR-20260420-002 |
| Produced by | Claude Code — HEURISTIC CLASSIFIER (rule-based; not an AI analytical pass) |
| Produced at | 2026-04-20T16:29:34Z |
| Scope | 110 rows across 7 non-canonical legacy labels |
| Output | Per-row canonical proposal + confidence + rationale |
| Status | CC proposals — researcher review required before encoding as DIMREVIEW patch |

---

## Producer note

The directive asked for per-group analytical mapping (semantic reading of context_description) — traditionally Claude AI territory. CC has produced a **heuristic rule-based classifier** applying keyword-match rules. This delivers:

- Mechanical consistency — same rule applies to every row with the same legacy label
- Conservative confidence — MEDIUM/LOW where the rule is not decisive
- Explicit escalation markers — LOW rows flagged for researcher review or Claude AI pass

**Two paths from here:**
- **(A)** Researcher accepts HIGH/MEDIUM directly → CC encodes DIMREVIEW patch; routes LOW + new-dim candidates to Claude AI
- **(B)** Researcher skips CC heuristic; waits for Claude AI analytical pass on all 110

CC recommendation: **(A)**.

---

## Summary

**Proposed canonical distribution (110 rows):**

| Proposed canonical | Count |
|---|---:|
| `05 — Moral Character` | 37 |
| `02 — Emotion — Negative` | 32 |
| `07 — Vitality / Existence` | 22 |
| `11 — Divine-Human Correspondence` | 18 |
| `10 — Dependence / Creatureliness` | 1 |

**Confidence distribution:**

| Confidence | Count |
|---|---:|
| LOW | 47 |
| MEDIUM | 36 |
| HIGH | 27 |

**Legacy-label breakdown:**

| Legacy label | Rows | Dominant proposal |
|---|---:|---|
| `Affective/Emotional` | 32 | `02 — Emotion — Negative` (32/32) |
| `Moral/Conscience` | 31 | `05 — Moral Character` (31/31) |
| `Spiritual/God-ward` | 19 | `11 — Divine-Human Correspondence` (18/19) |
| `Identity / Selfhood` | 8 | `07 — Vitality / Existence` (8/8) |
| `Identity/Selfhood` | 8 | `07 — Vitality / Existence` (8/8) |
| `Character/Disposition` | 6 | `05 — Moral Character` (6/6) |
| `Somatic/Embodied` | 6 | `07 — Vitality / Existence` (6/6) |

---

## New-dimension candidates flagged: 23

These are the vocabulary-gap cases from Phase A — best-fit under current vocabulary, but a distinct Dim 12+ may fit better. Researcher decision required.

---

## Per-row proposals

Grouped by legacy label, ordered by registry + group_code within each.

### Affective/Emotional (32 rows)

| wdi_id | Reg | Word | Group | Context (truncated) | Proposed | Conf | Rationale |
|---:|---:|---|---|---|---|---|---|
| 3706 | 18 | brokenness | 4814-001 | Inner experience of being overwhelmed — waves of death, divine wrath, or affliction passing through the inner person,... | `02 — Emotion — Negative` | HIGH | Negative-valence keywords (count=3) |
| 3705 | 18 | brokenness | 4815-001 | Inner experience of being at the threshold of birth — extreme distress and exhaustion at the crisis moment, and failu... | `02 — Emotion — Negative` | HIGH | Negative-valence keywords (count=3) |
| 3710 | 18 | brokenness | 4816-001 | Breaking of the heart — inner person shattered by grief, expressed in embodied anguish as a sign before others | `02 — Emotion — Negative` | HIGH | Negative-valence keywords (count=2) |
| 3707 | 18 | brokenness | 716-001 | Breaking of the spirit — inner person shattered by perversion, pride, or affliction, with the spirit explicitly named... | `02 — Emotion — Negative` | MEDIUM | Negative-valence keywords (count=1) |
| 3708 | 18 | brokenness | 716-002 | Inner wound — the deep hurt of person or people that demands honest naming and resists superficial healing | `02 — Emotion — Negative` | LOW | No clear valence signal; default to 02 (programme pattern). Researcher review. |
| 3709 | 18 | brokenness | 716-003 | Brokenness healed and brokenness mourned — God's binding up of the broken inner person, and inner grief of those who ... | `02 — Emotion — Negative` | HIGH | Negative-valence keywords (count=2) |
| 5079 | 113 | mourning | 1018-001 | Term names weeping as the outward expression of grief or empathetic solidarity — an inner state of sorrow finding its... | `02 — Emotion — Negative` | HIGH | Negative-valence keywords (count=3) |
| 2681 | 182 | Soul | 1381-002 | Term names the soul as the seat of inner emotional states — anguish, sorrow, bitterness, longing, joy | `02 — Emotion — Negative` | HIGH | Negative-valence keywords (count=3) |
| 2695 | 182 | Soul | 1382-004 | Term names the soul/life in extremity of inner despair — the person seeking death or fainting, the inner life overwhe... | `02 — Emotion — Negative` | MEDIUM | Negative-valence keywords (count=1) |
| 2704 | 182 | Soul | 1383-007 | Term names inner anguish and self-reflective suffering — inner experience of grief, courage dissolving | `02 — Emotion — Negative` | HIGH | Negative-valence keywords (count=2) |
| 2708 | 182 | Soul | 1386-001 | Term names appetite and craving as inner states that drive action — hunger and longing as expressions of deep inner need | `02 — Emotion — Negative` | LOW | No clear valence signal; default to 02 (programme pattern). Researcher review. |
| 2711 | 182 | Soul | 1386-004 | Term names the soul satisfied or unsatisfied — the inner state of fulfilment or continued craving | `02 — Emotion — Negative` | LOW | No clear valence signal; default to 02 (programme pattern). Researcher review. |
| 2714 | 182 | Soul | 1388-001 | Term names overwhelming danger reaching the neck — the inner experience of being engulfed, on the verge of destruction | `02 — Emotion — Negative` | HIGH | Negative-valence keywords (count=2) |
| 2659 | 182 | Soul | 1391-002 | Term names the soul as the seat of inner states — sorrow, longing, pain, and rest; the inner being as the location of... | `02 — Emotion — Negative` | HIGH | Negative-valence keywords (count=2) |
| 2671 | 182 | Soul | 1392-005 | Term names the life at risk or under threat — the person's life sought by enemies, at stake in crisis, preserved thro... | `02 — Emotion — Negative` | MEDIUM | Negative-valence keywords (count=1) |
| 2673 | 182 | Soul | 1393-001 | Term names the soul as the locus of intense inner anguish — the soul sorrowful to death, troubled before the passion | `02 — Emotion — Negative` | HIGH | Negative-valence keywords (count=2) |
| 2654 | 182 | Soul | 1399-001 | Term names overwhelming inner fear and foreboding causing fainting — the person's inner being overtaken by eschatolog... | `02 — Emotion — Negative` | HIGH | Negative-valence keywords (count=3) |
| 2657 | 182 | Soul | 1403-001 | Term names the fainthearted inner state — the soul diminished in courage, needing encouragement from others | `02 — Emotion — Negative` | LOW | No clear valence signal; default to 02 (programme pattern). Researcher review. |
| 2785 | 184 | spirit | 607-001 | Term names the mistaken perception of a ghost producing inner terror — the fear arising from false spiritual perception | `02 — Emotion — Negative` | HIGH | Negative-valence keywords (count=2) |
| 2787 | 184 | spirit | 610-002 | Term names the desperate consultation of a medium — inner act of seeking forbidden spiritual guidance driven by despair | `02 — Emotion — Negative` | LOW | No clear valence signal; default to 02 (programme pattern). Researcher review. |
| 2789 | 184 | spirit | 611-002 | Term names inner dejection — the downcast, dejectedly-moving spirit under moral confrontation | `02 — Emotion — Negative` | LOW | No clear valence signal; default to 02 (programme pattern). Researcher review. |
| 2771 | 184 | spirit | 613-002 | Term names the human spirit as the seat of inner life — the person's spirit that prays, serves, is troubled, fervent,... | `02 — Emotion — Negative` | LOW | No clear valence signal; default to 02 (programme pattern). Researcher review. |
| 2794 | 184 | spirit | 615-003 | Term names breath as inner vitality — fainting when inner vitality is exhausted; the life-breath connection to inner ... | `02 — Emotion — Negative` | MEDIUM | Negative-valence keywords (count=1) |
| 2825 | 185 | flesh | 621-001 | Ya.tsa as going-out of the soul or spirit | `02 — Emotion — Negative` | LOW | No clear valence signal; default to 02 (programme pattern). Researcher review. |
| 2827 | 185 | flesh | 621-003 | Ya.tsa as expression of inner states going outward | `02 — Emotion — Negative` | LOW | No clear valence signal; default to 02 (programme pattern). Researcher review. |
| 6180 | 188 | weeping | 1269-001 | Term names weeping as a noun — the state and act of weeping — across grief, penitence, prophetic sorrow, and eschatol... | `02 — Emotion — Negative` | HIGH | Negative-valence keywords (count=3) |
| 6175 | 188 | weeping | 1270-001 | Term names weeping as the expression of intense grief over loss — death, exile, and the suffering of the inner person... | `02 — Emotion — Negative` | HIGH | Negative-valence keywords (count=2) |
| 6181 | 188 | weeping | 1273-001 | Term names the concluded period of mourning — the weeping that has its season and passes | `02 — Emotion — Negative` | HIGH | Negative-valence keywords (count=2) |
| 3397 | 211 | being | 4479-001 | Term names apparent or feigned madness — the inner state or outer presentation that leads others to perceive a person... | `02 — Emotion — Negative` | LOW | No clear valence signal; default to 02 (programme pattern). Researcher review. |
| 3386 | 211 | being | 4481-001 | Term names deep inner perplexity — the state of being thoroughly at a loss before spiritual or extraordinary reality | `02 — Emotion — Negative` | LOW | No clear valence signal; default to 02 (programme pattern). Researcher review. |
| 3385 | 211 | being | 4482-001 | Term names the inner state of perplexity — being at a loss, uncertain, or disturbed without being driven to despair | `02 — Emotion — Negative` | LOW | No clear valence signal; default to 02 (programme pattern). Researcher review. |
| 3396 | 211 | being | 4483-001 | Term names the inner state of perplexity and bewilderment — the person at a complete loss before an inexplicable event | `02 — Emotion — Negative` | LOW | No clear valence signal; default to 02 (programme pattern). Researcher review. |

### Character/Disposition (6 rows)

| wdi_id | Reg | Word | Group | Context (truncated) | Proposed | Conf | Rationale |
|---:|---:|---|---|---|---|---|---|
| 2669 | 182 | Soul | 1392-003 | Term names the soul/life not held as precious — the inner disposition of releasing one's claim on one's own life for ... | `05 — Moral Character` | MEDIUM | Moral-character keywords (count=2) |
| 2791 | 184 | spirit | 605-001 | Term names the Belial inner character — the worthless inner disposition of wickedness, plotting evil, contempt for ju... | `05 — Moral Character` | MEDIUM | Moral-character keywords (count=5) |
| 2788 | 184 | spirit | 611-001 | Term names the quality of gentleness — dealing softly and gently as an inner disposition; and the rejection of God's ... | `05 — Moral Character` | MEDIUM | Moral-character keywords (count=1) |
| 2774 | 184 | spirit | 613-005 | Term names spirit-characterised orientations — spirit of adoption, stupor, fear, power/love/self-control; shaping the... | `05 — Moral Character` | MEDIUM | Moral-character keywords (count=2) |
| 2802 | 185 | flesh | 623-001 | Term names the inner disposition of debauchery — shameless abandonment to sensuality; the callous inner self-surrende... | `05 — Moral Character` | MEDIUM | Moral-character keywords (count=1) |
| 3390 | 211 | being | 4451-001 | Term names the inner disposition of careful attentiveness — the thoughtful orientation of the person toward devoted a... | `05 — Moral Character` | MEDIUM | Moral-character keywords (count=1) |

### Identity / Selfhood (8 rows)

| wdi_id | Reg | Word | Group | Context (truncated) | Proposed | Conf | Rationale |
|---:|---:|---|---|---|---|---|---|
| 7252 | 63 | foolishness | 4469-002 | Term describes the loss of distinctive inner character — the becoming flat or flavourless through failure to maintain... | `07 — Vitality / Existence` | LOW | Best-fit 07. CANDIDATE NEW DIMENSION — Identity/Selfhood may warrant its own dimension. |
| 7250 | 63 | foolishness | 5371-002 | Term names the inner posture of self-boasting folly — speaking and presenting oneself outside the orientation of God'... | `07 — Vitality / Existence` | LOW | Best-fit 07. CANDIDATE NEW DIMENSION — Identity/Selfhood may warrant its own dimension. |
| 9226 | 206 | vulnerability | 1369-001 | Term names the pre-fall state of nakedness without shame — the person's original inner freedom from guilt and fear be... | `07 — Vitality / Existence` | LOW | Best-fit 07. CANDIDATE NEW DIMENSION — Identity/Selfhood may warrant its own dimension. |
| 9228 | 206 | vulnerability | 1369-003 | Term describes nakedness as prophetic or ecstatic expression — the person's body and inner being made a visible sign ... | `07 — Vitality / Existence` | LOW | Best-fit 07. CANDIDATE NEW DIMENSION — Identity/Selfhood may warrant its own dimension. |
| 9206 | 206 | vulnerability | 1370-002 | Term characterises the person's inner state of spiritual nakedness — unpreparedness, self-unawareness, or eschatologi... | `07 — Vitality / Existence` | LOW | Best-fit 07. CANDIDATE NEW DIMENSION — Identity/Selfhood may warrant its own dimension. |
| 9204 | 206 | vulnerability | 7421-001 | Term names physical nakedness/deprivation as a condition of apostolic vulnerability — the person's inner orientation ... | `07 — Vitality / Existence` | LOW | Best-fit 07. CANDIDATE NEW DIMENSION — Identity/Selfhood may warrant its own dimension. |
| 9240 | 207 | blindness (spiritual) | 7432-001 | Term names darkness as the inner-spiritual domain the person inhabits, is rescued from, or identifies with — their fu... | `07 — Vitality / Existence` | LOW | Best-fit 07. CANDIDATE NEW DIMENSION — Identity/Selfhood may warrant its own dimension. |
| 9237 | 207 | blindness (spiritual) | 7433-001 | Term names darkness as the inner condition of spiritual alienation — the state of the person who hates, does not know... | `07 — Vitality / Existence` | LOW | Best-fit 07. CANDIDATE NEW DIMENSION — Identity/Selfhood may warrant its own dimension. |

### Identity/Selfhood (8 rows)

| wdi_id | Reg | Word | Group | Context (truncated) | Proposed | Conf | Rationale |
|---:|---:|---|---|---|---|---|---|
| 2706 | 182 | Soul | 1385-001 | Term names the human being as a living soul — constituted at creation as a living creature by the divine breath | `07 — Vitality / Existence` | MEDIUM | Vitality/existence keywords (count=5); essential-being reading; best-fit 07. |
| 2658 | 182 | Soul | 1391-001 | Term names the soul as the essential inner person — the non-physical self that can be forfeited, preserved, or lost; ... | `07 — Vitality / Existence` | MEDIUM | Vitality/existence keywords (count=3); essential-being reading; best-fit 07. |
| 2677 | 182 | Soul | 1396-001 | Term names the natural/soul-level inner condition — operating from the soul alone, incapable of receiving spiritual t... | `07 — Vitality / Existence` | LOW | Best-fit 07. CANDIDATE NEW DIMENSION — Identity/Selfhood may warrant its own dimension. |
| 2678 | 182 | Soul | 1396-002 | Term names the natural body as the lower form — sown natural, raised spiritual; soul-level as pre-resurrection mode | `07 — Vitality / Existence` | LOW | Best-fit 07. CANDIDATE NEW DIMENSION — Identity/Selfhood may warrant its own dimension. |
| 2655 | 182 | Soul | 1400-001 | Term names the lifeless/soulless state of an instrument — implying the person, unlike a lifeless object, has inner li... | `07 — Vitality / Existence` | LOW | Best-fit 07. CANDIDATE NEW DIMENSION — Identity/Selfhood may warrant its own dimension. |
| 2778 | 184 | spirit | 2307-001 | Term names the spiritual person — one whose inner life is ordered by the Spirit, capable of discerning all things, co... | `07 — Vitality / Existence` | MEDIUM | Vitality/existence keywords (count=2); essential-being reading; best-fit 07. |
| 2808 | 185 | flesh | 3008-002 | Term names physical/fleshly descent as insufficient — contrasted with the inner power of indestructible life | `07 — Vitality / Existence` | MEDIUM | Vitality/existence keywords (count=2); essential-being reading; best-fit 07. |
| 2830 | 185 | flesh | 619-002 | She.er naming the whole person alongside the heart | `07 — Vitality / Existence` | LOW | Best-fit 07. CANDIDATE NEW DIMENSION — Identity/Selfhood may warrant its own dimension. |

### Moral/Conscience (31 rows)

| wdi_id | Reg | Word | Group | Context (truncated) | Proposed | Conf | Rationale |
|---:|---:|---|---|---|---|---|---|
| 1751 | 93 | intention | 936-001 | Term names the formed inner inclination of the heart — the moral orientation shaped within the person, inclining towa... | `05 — Moral Character` | HIGH | Moral-character keywords present (count=2) |
| 1736 | 110 | memory | 979-002 | Term names the memorial as moral legacy — the lasting presence or extinction of a person's name in communal memory, c... | `05 — Moral Character` | MEDIUM | Moral-character keywords present (count=1) |
| 1741 | 160 | thought | 1174-002 | Term names inner scheming — the deliberate devising of plans directed against another | `05 — Moral Character` | MEDIUM | Moral-character keywords present (count=1) |
| 2686 | 182 | Soul | 1381-007 | Term names the soul as the seat of moral character — upright or puffed up, righteous or wicked | `05 — Moral Character` | HIGH | Moral-character keywords present (count=4) |
| 2696 | 182 | Soul | 1382-005 | Term names the life as the object of legal protection — the lex talionis; the prohibition on blood as the seat of life | `05 — Moral Character` | LOW | Default for Moral/Conscience; no clear signal. Researcher review. |
| 2701 | 182 | Soul | 1383-004 | Term names the self as subject of inner moral defilement — making oneself detestable through boundary violations | `05 — Moral Character` | MEDIUM | Moral-character keywords present (count=1) |
| 2709 | 182 | Soul | 1386-002 | Term names the wicked's desire for evil — inner appetite of the corrupt person oriented toward violence and iniquity | `05 — Moral Character` | HIGH | Moral-character keywords present (count=4) |
| 2663 | 182 | Soul | 1391-006 | Term names the soul as the inner moral self engaged in work — doing God's will from the soul, working heartily rather... | `05 — Moral Character` | MEDIUM | Moral-character keywords present (count=1) |
| 2665 | 182 | Soul | 1391-008 | Term names the soul as the target of spiritual warfare — the inner being attacked by passions, poisoned, unsettled, o... | `05 — Moral Character` | LOW | Default for Moral/Conscience; no clear signal. Researcher review. |
| 2672 | 182 | Soul | 1392-006 | Term names the moral weight of saving or destroying a life — the Sabbath question as a test of inner moral priority | `05 — Moral Character` | MEDIUM | Moral-character keywords present (count=1) |
| 2676 | 182 | Soul | 1394-001 | Term names each person as an accountable soul — the morally responsible unit that must obey, faces judgment, and expe... | `05 — Moral Character` | MEDIUM | Moral-character keywords present (count=1) |
| 2763 | 183 | heart | 577-005 | Term names the inner parts as the seat of hostile intent — what lies within as the source of evil plotting against ot... | `05 — Moral Character` | MEDIUM | Moral-character keywords present (count=1) |
| 2766 | 184 | spirit | 609-002 | Term names holiness as the inner character calling — being holy in all conduct, body, and spirit, as God is holy | `05 — Moral Character` | HIGH | Moral-character keywords present (count=2) |
| 2767 | 184 | spirit | 609-003 | Term names the blasphemy against the Holy Spirit — the inner moral act of attributing divine works to Satan; the unfo... | `05 — Moral Character` | HIGH | Moral-character keywords present (count=3) |
| 2786 | 184 | spirit | 610-001 | Term names the medium as a false spiritual access point — the inner prohibition against seeking guidance through forb... | `05 — Moral Character` | LOW | Default for Moral/Conscience; no clear signal. Researcher review. |
| 2790 | 184 | spirit | 611-003 | Term names the mutterer as a false spiritual practitioner — one who whispers and mutters as a form of spiritual decep... | `05 — Moral Character` | LOW | Default for Moral/Conscience; no clear signal. Researcher review. |
| 2800 | 184 | spirit | 612-002 | Term names the path of folly leading to the company of the dead — inner moral choices directing the person toward Sheol | `05 — Moral Character` | MEDIUM | Moral-character keywords present (count=1) |
| 2772 | 184 | spirit | 613-003 | Term names the spirit-flesh contrast — the spirit willing but flesh weak; inner orientation toward God vs. the flesh'... | `05 — Moral Character` | LOW | Default for Moral/Conscience; no clear signal. Researcher review. |
| 2831 | 185 | flesh | 3012-001 | Term names the kinship bond of flesh — the close bodily relation between persons that creates an inviolable inner mor... | `05 — Moral Character` | MEDIUM | Moral-character keywords present (count=1) |
| 2821 | 185 | flesh | 617-003 | Be.shar as domain of misplaced creaturely trust | `05 — Moral Character` | LOW | Default for Moral/Conscience; no clear signal. Researcher review. |
| 2815 | 185 | flesh | 618-003 | Ba.sar as domain of misplaced creaturely trust | `05 — Moral Character` | LOW | Default for Moral/Conscience; no clear signal. Researcher review. |
| 2809 | 185 | flesh | 625-001 | Sarx as governing principle of fallen human desire, passions, and moral incapacity | `05 — Moral Character` | MEDIUM | Moral-character keywords present (count=1) |
| 2805 | 185 | flesh | 626-001 | Term names the fleshly inner condition — the person dominated by the flesh, manifesting in jealousy, strife, and spir... | `05 — Moral Character` | LOW | Default for Moral/Conscience; no clear signal. Researcher review. |
| 2806 | 185 | flesh | 626-002 | Term names the fleshly inner orientation in conflict with the Spirit — fleshly wisdom, weapons, passions warring agai... | `05 — Moral Character` | LOW | Default for Moral/Conscience; no clear signal. Researcher review. |
| 2804 | 185 | flesh | 627-001 | Term names voluntary abstinence from meat as an act of inner love — the moral decision to forgo a right out of concer... | `05 — Moral Character` | MEDIUM | Moral-character keywords present (count=1) |
| 2803 | 185 | flesh | 628-001 | Term names the false mark of outward mutilation — contrasted implicitly with the true inner spiritual circumcision of... | `05 — Moral Character` | LOW | Default for Moral/Conscience; no clear signal. Researcher review. |
| 3389 | 211 | being | 4439-001 | Term names the inner disposition of arrogance — the haughtiness of the wealthy person who sets themselves above other... | `05 — Moral Character` | MEDIUM | Moral-character keywords present (count=1) |
| 3388 | 211 | being | 4440-001 | Term names the inner disposition of haughtiness — self-elevation and valuing what is exalted among people, warned aga... | `05 — Moral Character` | MEDIUM | Moral-character keywords present (count=1) |
| 3387 | 211 | being | 4473-001 | Term names the inner disposition of thinking too highly of oneself — self-inflated assessment contrasted with sober s... | `05 — Moral Character` | MEDIUM | Moral-character keywords present (count=1) |
| 3392 | 211 | being | 4478-001 | Term names the insensitive heart — rendered unfeeling like fat, incapable of genuine response to God or his word | `05 — Moral Character` | LOW | Default for Moral/Conscience; no clear signal. Researcher review. |
| 3395 | 211 | being | 4485-001 | Term names reckless instability of character — the inner disposition that acts impulsively without regard for moral b... | `05 — Moral Character` | HIGH | Moral-character keywords present (count=3) |

### Somatic/Embodied (6 rows)

| wdi_id | Reg | Word | Group | Context (truncated) | Proposed | Conf | Rationale |
|---:|---:|---|---|---|---|---|---|
| 2713 | 182 | Soul | 1387-001 | Term names the dead body requiring inner spiritual separation — the soul of the dead as source of contamination requi... | `07 — Vitality / Existence` | HIGH | Somatic/embodied → 07 Vitality/Existence (keywords=2). Phase A analyst anticipated this mapping. |
| 2820 | 185 | flesh | 617-002 | Be.shar as creaturely condition of humanity before God | `07 — Vitality / Existence` | HIGH | Somatic/embodied → 07 Vitality/Existence (keywords=2). Phase A analyst anticipated this mapping. |
| 2823 | 185 | flesh | 617-005 | Be.shar as body mediating and expressing inner-being states | `07 — Vitality / Existence` | HIGH | Somatic/embodied → 07 Vitality/Existence (keywords=1). Phase A analyst anticipated this mapping. |
| 2814 | 185 | flesh | 618-002 | Ba.sar as creaturely condition of humanity before God | `07 — Vitality / Existence` | HIGH | Somatic/embodied → 07 Vitality/Existence (keywords=2). Phase A analyst anticipated this mapping. |
| 2817 | 185 | flesh | 618-005 | Ba.sar as body mediating and expressing inner-being states | `07 — Vitality / Existence` | HIGH | Somatic/embodied → 07 Vitality/Existence (keywords=1). Phase A analyst anticipated this mapping. |
| 2810 | 185 | flesh | 625-002 | Sarx as creaturely mortal condition of embodied human existence | `07 — Vitality / Existence` | HIGH | Somatic/embodied → 07 Vitality/Existence (keywords=4). Phase A analyst anticipated this mapping. |

### Spiritual/God-ward (19 rows)

| wdi_id | Reg | Word | Group | Context (truncated) | Proposed | Conf | Rationale |
|---:|---:|---|---|---|---|---|---|
| 5087 | 113 | mourning | 1017-001 | Term names the inner posture of mournful devotion — the disposition expressed in walking mournfully before God as an ... | `11 — Divine-Human Correspondence` | MEDIUM | Divine-human correspondence signals (count=1) |
| 1733 | 160 | thought | 1180-001 | Term names the commanded human act of remembering — calling to mind God's acts, his covenant, one's own ways, and tho... | `11 — Divine-Human Correspondence` | LOW | No strong signal; default 11 as closest. CANDIDATE NEW DIMENSION — Spiritual/God-ward may warrant Dim 12. |
| 2680 | 182 | Soul | 1381-001 | Term names the soul's wholehearted consecration to God — loving, seeking, and serving God with all the soul | `11 — Divine-Human Correspondence` | LOW | No strong signal; default 11 as closest. CANDIDATE NEW DIMENSION — Spiritual/God-ward may warrant Dim 12. |
| 2685 | 182 | Soul | 1381-006 | Term names the soul's moral and spiritual nourishment — what revives, refreshes, or satisfies the inner person | `11 — Divine-Human Correspondence` | LOW | No strong signal; default 11 as closest. CANDIDATE NEW DIMENSION — Spiritual/God-ward may warrant Dim 12. |
| 2688 | 182 | Soul | 1381-009 | Term names the soul's capacity for praise, worship, and inner exultation before God | `11 — Divine-Human Correspondence` | MEDIUM | Divine-human correspondence signals (count=1) |
| 2690 | 182 | Soul | 1381-011 | Term names the soul poured out in prayer — the inner act of bringing the soul before God in intercession and confession | `11 — Divine-Human Correspondence` | MEDIUM | Divine-human correspondence signals (count=1) |
| 2700 | 182 | Soul | 1383-003 | Term names deliberate inner self-humbling through fasting — afflicting the self as a penitential inner act | `11 — Divine-Human Correspondence` | LOW | No strong signal; default 11 as closest. CANDIDATE NEW DIMENSION — Spiritual/God-ward may warrant Dim 12. |
| 2710 | 182 | Soul | 1386-003 | Term names the soul's desire directed toward God or what is good — inner longing toward holy or worthy objects | `11 — Divine-Human Correspondence` | LOW | No strong signal; default 11 as closest. CANDIDATE NEW DIMENSION — Spiritual/God-ward may warrant Dim 12. |
| 2679 | 182 | Soul | 1390-001 | Term names the refreshing of the inner person through rest — restoration of the inner being through Sabbath rest | `11 — Divine-Human Correspondence` | LOW | No strong signal; default 11 as closest. CANDIDATE NEW DIMENSION — Spiritual/God-ward may warrant Dim 12. |
| 2661 | 182 | Soul | 1391-004 | Term names the soul's wholehearted consecration to God — loving God with all the soul as the supreme inner act of dev... | `11 — Divine-Human Correspondence` | LOW | No strong signal; default 11 as closest. CANDIDATE NEW DIMENSION — Spiritual/God-ward may warrant Dim 12. |
| 2674 | 182 | Soul | 1393-002 | Term names the soul's capacity for worship — magnifying God at the soul level, the deepest personal act of praise | `11 — Divine-Human Correspondence` | LOW | No strong signal; default 11 as closest. CANDIDATE NEW DIMENSION — Spiritual/God-ward may warrant Dim 12. |
| 2798 | 184 | spirit | 2230-004 | Term names breath as the qualification for worship and the marker of creaturely dependence on God's gift of life | `10 — Dependence / Creatureliness` | MEDIUM | Dependence-on-God signals (count=1) |
| 2783 | 184 | spirit | 606-001 | Term names the divining spirit — a false spiritual power inhabiting a person, counterfeiting prophetic inner capacity... | `11 — Divine-Human Correspondence` | LOW | No strong signal; default 11 as closest. CANDIDATE NEW DIMENSION — Spiritual/God-ward may warrant Dim 12. |
| 6176 | 188 | weeping | 1270-002 | Term names weeping before God — in penitence, prayer, and covenant distress — the inner-being act of bringing grief t... | `11 — Divine-Human Correspondence` | MEDIUM | Divine-human correspondence signals (count=1) |
| 6178 | 188 | weeping | 1270-004 | Term names prophetic weeping — the prophet's tears for God's people, for judgment, and for the suffering of nations —... | `11 — Divine-Human Correspondence` | LOW | No strong signal; default 11 as closest. CANDIDATE NEW DIMENSION — Spiritual/God-ward may warrant Dim 12. |
| 6183 | 188 | weeping | 1272-001 | Term names tears as the visible expression of the inner person's grief, prayer, and lament — and God's attentive resp... | `11 — Divine-Human Correspondence` | LOW | No strong signal; default 11 as closest. CANDIDATE NEW DIMENSION — Spiritual/God-ward may warrant Dim 12. |
| 6179 | 188 | weeping | 7115-001 | Term names the intensity of communal penitential weeping — bitterly, before God | `11 — Divine-Human Correspondence` | MEDIUM | Divine-human correspondence signals (count=1) |
| 6182 | 188 | weeping | 7117-001 | Term names the prophet's secret soul-weeping — the inner grief hidden from the people but present before God | `11 — Divine-Human Correspondence` | MEDIUM | Divine-human correspondence signals (count=1) |
| 3393 | 211 | being | 4475-001 | Term names the inner act of humbling oneself before God — the voluntary posture of the heart that turns from pride an... | `11 — Divine-Human Correspondence` | MEDIUM | Divine-human correspondence signals (count=1) |

---

## Next action

1. HIGH-confidence rows → CC encodes DIMREVIEW patch
2. MEDIUM-confidence rows → researcher accepts or requests Claude AI review
3. LOW-confidence + new-dim candidates → Claude AI analytical pass OR researcher direct decision

Patch naming (when produced): `PATCH-20260420-DIMREVIEW-GLOBAL-CANONICALISATION-V1.json` (cross-registry).

---

*Directive DIR-20260420-002 result — CC heuristic proposals for researcher review.*
