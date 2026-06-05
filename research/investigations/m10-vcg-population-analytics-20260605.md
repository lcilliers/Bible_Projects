# M10 — VCG / sub-group population analytics

> Read-only, 2026-06-05. Feasibility check for the new VCG approach (read the **actual verses** of a
> group together, not the derived meaning or just the anchor). Question: are the populations too large?

**M10 total** is_relevant active verses: **1320**

## Sub-groups (the population read together to (re)form VCGs)

- 22 sub-groups. sizes: min 5 · median 34.0 · mean 60 · p90 112 · **max 205**

| Sub-group | Label | Verses |
|---|---|---|
| M10-V | Sin as divine record | 205 |
| M10-E | Iniquity as accumulated moral crime | 162 |
| M10-F | Transgression / rebellion as deliberate  | 147 |
| M10-T | Sin as universal condition | 112 |
| M10-G | Faithlessness / treachery as covenant-br | 101 |
| M10-J | Wilful sinning | 98 |
| M10-D | Guilt as inner-being state | 97 |
| M10-I | Injustice as moral failure of right cond | 72 |
| M10-H | Perversion / moral corruption as inner i | 64 |
| M10-C | The sinner as moral character | 64 |
| M10-W | Forgiveness sought and received | 34 |
| M10-L | Confession | 34 |
| M10-R | Sinful speech | 22 |
| M10-P | Contagious sin | 19 |
| M10-N | Refusal to repent | 18 |
| M10-K | Unintentional sinning | 18 |
| M10-O | Habitual defection | 14 |
| M10-U | Sin as enslaving power | 9 |
| M10-Q | Political revolt | 9 |
| M10-X | Generational sin | 8 |
| M10-M | Conscience suppression | 8 |
| M10-S | Specialised sinful mechanisms | 5 |

## VCGs (current grouping granularity)

- 68 VCGs. sizes: min 1 · median 16.5 · mean 19.4 · p90 33 · **max 113**

**VCG size histogram:**

- 1-5 verses: 7 VCGs
- 6-15 verses: 26 VCGs
- 16-30 verses: 25 VCGs
- 31-50 verses: 7 VCGs
- 51-100 verses: 2 VCGs
- 101+ verses: 1 VCGs

**Largest VCGs:**

| VCG | Verses |
|---|---|
| M10-V-VCG-05 | 113 |
| M10-T-VCG-03 | 68 |
| M10-G-VCG-01 | 57 |
| M10-V-VCG-04 | 46 |
| M10-T-VCG-02 | 39 |
| M10-G-VCG-02 | 34 |
| M10-F-VCG-09 | 34 |
| M10-I-VCG-02 | 33 |
| M10-V-VCG-01 | 32 |
| M10-J-VCG-01 | 32 |
| M10-E-VCG-05 | 30 |
| M10-C-VCG-01 | 30 |

## Feasibility read

- Sub-groups > 100 verses (heavy to read whole): **5** of 22.
- VCGs > 50 verses: **3** of 68.
- A verse text averages ~30–60 words; reading N verses together ≈ N×~45 words.
  Largest sub-group (205 verses) ≈ ~9,225 words to read at once.

## Verdict — not too large

**The "read the actual verses together" VCG approach is feasible for M10** (and M10 is among the *densest*
clusters at 1,320 verses, so this is close to a worst case).

- **At VCG level:** trivial — median **16.5** verses, 96% are ≤50, only one outlier at 113. Reading a VCG's
  actual verse texts together is a small task.
- **At sub-group level** (the population you'd read to *re-form* VCGs from actual verses): the largest is
  **205 verses ≈ ~9k words ≈ ~12–15k tokens** — comfortably one analytical pass. p90 is 112. Five sub-groups
  exceed 100 verses; all still readable whole.
- **Whole-cluster** (1,320 verses ≈ ~60k words ≈ ~80k tokens): heavy but possible in a large-context model
  *if ever needed* — but unnecessary; the **sub-group is the natural read-unit**, and it's well within range.

**Implication:** population size is **not** a blocker. Optional splits to keep reads small: **M10-V**
("Sin as divine record", 205) and its **M10-V-VCG-05** (113). Since M10 is near the upper bound, most other
clusters will be lighter still.
