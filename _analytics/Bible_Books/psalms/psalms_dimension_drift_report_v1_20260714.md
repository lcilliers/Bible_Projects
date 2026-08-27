# Dimension reader-drift diagnostic — Psalms

Book split into 6 chapter-bands (1-25, 26-50, 51-75, 76-100, 101-125, 126-150). Source: `reread-psalms-2026`.
**DRIFT-SUSPECT** = a common value (>=5% overall) is **0% in some band** or in <= 4 of 6 bands. This is a **screen, not a verdict**: absence-in-a-band can be reader-drift (the label left the reader's vocabulary) OR genuine text-silence (the section doesn't discuss it). Confirm each against an a-priori test — e.g. `type=action` at 0% across 25 consecutive psalms is *impossible as a text property*, so `type` is confirmed reader-drift; a `bearer=the wicked` gap may be a real thematic section boundary. **READ-GRADE** = common values span the book. **N/A** = free-text dimension (not testable this way).

| dim | ve | verdict | drift evidence |
|---|---|---|---|
| sense | 101 | N/A | free-text (bespoke prose per occurrence) |
| type | 102 | **DRIFT-SUSPECT** | `action` 0%→50% (5/6 bands); `status` 0%→47% (5/6 bands); `state` 0%→21% (5/6 bands); `disposition` 0%→25% (4/6 bands) |
| source | 103 | N/A | free-text (bespoke prose per occurrence) |
| seat | 104 | READ-GRADE |  |
| bearer | 105 | READ-GRADE |  |
| operation | 106 | N/A | free-text (bespoke prose per occurrence) |
| target | 107 | **DRIFT-SUSPECT** | `none` 0%→37% (4/6 bands) |
| manner | 108 | N/A | free-text (bespoke prose per occurrence) |
| intensity | 109 | READ-GRADE |  |
| specifier | 110 | READ-GRADE |  |
| effect | 111 | READ-GRADE |  |
| coupling | 112 | N/A | free-text (bespoke prose per occurrence) |
| prohibition | 113 | N/A | free-text (bespoke prose per occurrence) |
| reading | 114 | N/A | free-text (bespoke prose per occurrence) |
| role | 115 | READ-GRADE |  |
| locus | 116 | **DRIFT-SUSPECT** | `external:god` 0%→46% (5/6 bands) |
| device | 117 | READ-GRADE |  |
| direction | 118 | READ-GRADE |  |

## Band-rate detail (drift-suspect dimensions)

### type (102)

| value | 1-25 | 26-50 | 51-75 | 76-100 | 101-125 | 126-150 |
|---|---|---|---|---|---|---|
| action | 0% | 22% | 50% | 49% | 38% | 24% |
| status | 0% | 23% | 47% | 10% | 10% | 3% |
| state | 14% | 7% | 0% | 18% | 17% | 21% |
| disposition | 2% | 0% | 0% | 14% | 25% | 8% |
| affect | 44% | 28% | 0% | 0% | 0% | 24% |
| faculty | 0% | 0% | 0% | 9% | 10% | 3% |
| volition | 24% | 14% | 0% | 0% | 0% | 6% |
| cognition | 16% | 6% | 0% | 0% | 0% | 8% |

### target (107)

| value | 1-25 | 26-50 | 51-75 | 76-100 | 101-125 | 126-150 |
|---|---|---|---|---|---|---|
| none | 0% | 21% | 37% | 3% | 6% | 0% |
| God's word | 0% | 0% | 0% | 0% | 13% | 0% |
| God | 0% | 2% | 8% | 6% | 1% | 1% |
| to God | 0% | 1% | 7% | 4% | 2% | 2% |
| the LORD | 0% | 0% | 0% | 1% | 4% | 4% |
| the psalmist | 0% | 0% | 3% | 0% | 3% | 0% |
| before God | 0% | 0% | 1% | 4% | 1% | 1% |
| in God | 0% | 2% | 3% | 2% | 0% | 0% |

### locus (116)

| value | 1-25 | 26-50 | 51-75 | 76-100 | 101-125 | 126-150 |
|---|---|---|---|---|---|---|
| internal:ib-state | 100% | 79% | 42% | 52% | 53% | 78% |
| external:god | 0% | 12% | 41% | 46% | 45% | 22% |
| external:person | 0% | 3% | 11% | 2% | 2% | 0% |
| internal:heart | 0% | 0% | 6% | 0% | 0% | 0% |
| internal:seat | 0% | 6% | 0% | 0% | 0% | 0% |
| internal:spirit | 0% | 0% | 1% | 0% | 0% | 0% |
