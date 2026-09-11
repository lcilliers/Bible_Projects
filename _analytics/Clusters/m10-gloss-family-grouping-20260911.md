# M10 cluster — stepGloss family grouping

> Generated 2026-09-11, in support of escalation #1680 (Revise meaning-distillation method, post
> parse-table retirement). Source data only — no external lexical judgement, no other DB columns
> consulted. Query run against `iba.db`:
>
> ```sql
> select cs.strong, s.stepGloss from cluster_strong cs
> inner join strong s on cs.strong = s.strongNumber
> where cs.cluster_code = 'M10'
> group by cs.strong;
> ```
>
> 165 distinct `strong` rows returned. Grouping below is by **gloss text alone** (surface meaning
> of the English `stepGloss` string) — it is not a claim about semantic domain, root family, or
> any existing cluster/characteristic structure; it is exactly what the instruction asked for:
> family-of-gloss buckets over this query's own data, nothing brought in from outside it.

## Method note

This is an LLM read of 165 gloss strings, not a mechanical/deterministic classification — flag
accordingly if this feeds anything downstream that expects deterministic output. A few glosses are
compound ("iniquity: guilt", "sin: sin offering") and were placed under their head noun (iniquity,
sin) rather than split. Two rows are almost certainly homograph collisions unrelated to the
cluster's actual theme (a Hebrew/Greek letter name and a place name, both surfacing as "Sin") —
called out separately rather than folded into the "sin" family, since counting them there would
misrepresent the family's size.

## Family counts (165 total)

| Family | Count | Description |
|---|--:|---|
| A — Destroy / Destruction / Devastation | 31 | to destroy, destruction, to devote/destroy, be desolate: destroyed |
| E — Corruption / Perversion / Twisting | 24 | to corrupt, corruption, to pervert, perversity, perversion, to twist (incl. idiomatic "to twist: dance/anticipate") |
| F — Violence / Crushing / Wounding / Injury | 19 | violence, to crush, crushing, to wound, injury, to suffer injury |
| B — Sin (general) / Sinner / Sinful | 14 | to sin, sin, sinful, sinner, sin offering, sin: punishment, to lead into sin |
| D — Crime / Injustice / Iniquity | 14 | crime, unjust, unjust-gain, injustice, iniquity (incl. "iniquity: crime/guilt/punishment") |
| I — Strife / Contention / Battle / Fight | 10 | strife, contention, battle, fight |
| C — Adultery / Sexual sin | 9 | adultery, to commit adultery, sexual sin, to sin sexually, sexual sinner |
| G — Transgression / Trespass | 8 | to transgress, transgression, transgressor, trespass |
| J — Unfaithfulness / Treachery / Apostasy / Revolt | 8 | apostasy, ungodliness, be ungodly, to act treacherously, be unfaithful, unfaithfulness, degenerate, revolt |
| K — Error / Deception / Enticement | 8 | error, to entice |
| H — Guilt / Guiltiness | 7 | be guilty, guilt [offering], guilty, guiltiness, to lift: guilt |
| L — Defilement / Vileness / Lewdness | 3 | defilement, vileness, lewdness |
| M — Cruelty / Ruthlessness | 4 | cruel, ruthless |
| N — Hypocrisy | 1 | to join hypocrisy |
| O — Atonement (outlier) | 1 | atonement — a remedy for sin, not sin itself; flagged as a possible cluster-membership oddity |
| P — Staggering (outlier) | 1 | staggering — unclear fit with the rest of the cluster |
| Q — Generic "to commit" (ambiguous) | 1 | gloss too bare to place confidently (likely truncated from a compound like "to commit adultery/iniquity") |
| R — Homograph noise ("Sin" as name, not sin) | 2 | Hebrew/Greek letter name and a place name, both stepGloss'd "Sin"/"Sin/Shin" — not the moral-failure sense |

## Full membership by family

### A — Destroy / Destruction / Devastation (31)
G0622, G0684, G0853, G1311, G2506, G3645, G4485, G5351,
H0007, H0008, H0010, H0012, H0013, H2254B, H2255, H2256D, H2475, H2717B, H2763A, H4277, H4889,
H4892, H5642B, H6789, H6979C, H6986, H6987, H8045, H8046, H8074G, H8399

### B — Sin (general) / Sinner / Sinful (14)
G0264, G0265, G0266, G0268, G7292,
H2398, H2399, H2400, H2401, H2403A, H2403B, H2403H, H2403I, H2408

### C — Adultery / Sexual sin (9)
G3429, G3430, G3431, G4202, G4203, G4205, H5003, H5004, H5005

### D — Crime / Injustice / Iniquity (14)
G0092, G0094, G4467,
H1215, H2248, H5758, H5760, H5766A, H5766B, H5767, H5771G, H5771H, H5771I, H5932

### E — Corruption / Perversion / Twisting (24)
G1294, G5356, G6882, G7946,
H0444, H2017, H2342J, H2342K, H3891, H3943, H4297, H4893B, H5557, H5753A, H5753B, H5791, H6127,
H6140, H6617, H7806, H7844, H8308, H8397, H8419

### F — Violence / Crushing / Wounding / Injury (19)
G2352, G3039, G5135,
H1500, H1792, H1794, H1795, H1854, H2115, H2555, H3807, H4272, H5142, H6094, H6481, H7533, H7602B,
H7701, H8428

### G — Transgression / Trespass (8)
G3845, G3847, G3848, G3900, G8634, H5674D, H6586, H6588

### H — Guilt / Guiltiness (7)
G1777, H0816, H0817, H0818, H0819, H2054, H5375J

### I — Strife / Contention / Battle / Fight (10)
G0073, G3859, H4066, H4079, H4090, H4421, H4683, H4695, H7379, H8409

### J — Unfaithfulness / Treachery / Apostasy / Revolt (8)
G0646, G0763, G0764, H0898, H4603, H4604, H5494, H5627

### K — Error / Deception / Enticement (8)
G0051, G1185, G4106, H4879, H6601B, H7691, H8417, H8442

### L — Defilement / Vileness / Lewdness (3)
G8327, H2149, H5040

### M — Cruelty / Ruthlessness (4)
H0393, H0394, H0395, H6184

### N — Hypocrisy (1)
G4942

### O — Atonement — outlier (1)
H3725

### P — Staggering — outlier (1)
H6330

### Q — Generic "to commit" — ambiguous (1)
H4560

### R — Homograph noise (2)
G21497 (gloss "Sin/Shin" — the Hebrew letter name), H5512B (gloss "Sin" — likely the place name,
Strong's H5512, not the moral-failure sense)

## Observations for #1680

- The M10 cluster is dominated by three big families — **Destroy (31)**, **Corruption/Perversion
  (24)**, **Violence/Crush/Wound (19)** — together 74 of 165 codes (45%). If M10's characteristic
  label presumes a narrower "sin/transgression" core, these three families are a large adjacent
  mass worth checking against the cluster's actual definition.
- Two rows (R) look like straightforward homograph noise unrelated to the cluster theme and are
  candidates for a `cluster_strong` review, not a gloss-grouping nuance.
- One row (Q, H4560 "to commit") is too bare to classify without more context than this query
  supplies — flagged rather than guessed into a family.
- One row (O, H3725 "atonement") reads as the remedy for the cluster's theme rather than an
  instance of it — worth a second look at why it's tagged to M10 at all.

This is gloss-text grouping only; it says nothing about whether these codes are correctly
*assigned* to M10 in the first place — that's a separate question from the one asked.
