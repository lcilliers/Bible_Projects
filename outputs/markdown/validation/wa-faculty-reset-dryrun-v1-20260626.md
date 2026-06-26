# Faculty reset — dry-run (verse-grounded) — variants A & B

- **File:** wa-faculty-reset-dryrun-v1-20260626.md · read-only, no DB write.
- Map: 1717 lemmas (751 monovalent, 151 polyvalent seats, 815 no-faculty).
- Units in scope (clustered, non-deleted): **42731**.

## Coverage / over-fire comparison

| metric | CURRENT (lemma) | A (term-only) | B (verse-scan) | C (faculty-word + seat-inherit) |
|--------|----------------:|--------------:|---------------:|--------------------------------:|
| units carrying a faculty | 19712 | 12058 | 25155 | 17161 |
| units with 0 faculties | 23019 | 30673 | 17576 | 25570 |
| units with 1 faculties | 13633 | 12058 | 18087 | 12429 |
| units with 2 faculties | 4631 | 0 | 5993 | 4551 |
| units with 3 faculties | 186 | 0 | 982 | 134 |
| units with 4 faculties | 1121 | 0 | 93 | 40 |
| units with 5 faculties | 0 | 0 | 0 | 7 |
| units with 6 faculties | 141 | 0 | 0 | 0 |

- max faculties/unit — CURRENT=6 A=1 B=4 C=5
- A value distribution: {'affect': 5379, 'moral_evaluation': 2566, 'volition': 1762, 'cognition': 1403, 'perception': 435, 'memory': 282, 'conscience': 224, 'relational_capacity': 5, 'agency': 2}
- B value distribution: {'affect': 12830, 'moral_evaluation': 7233, 'volition': 5305, 'cognition': 3962, 'perception': 2422, 'memory': 939, 'conscience': 678, 'relational_capacity': 14, 'agency': 8}
- C value distribution: {'affect': 8425, 'volition': 3991, 'moral_evaluation': 3420, 'cognition': 3284, 'perception': 1518, 'relational_capacity': 612, 'conscience': 489, 'memory': 304, 'creativity': 70, 'agency': 15}

## Sample verses (the diagnostic cases)

- **Gen 6:5** ra.ah (H7451I) — own=['moral_evaluation'] | CURRENT=['moral_evaluation'] | A=['moral_evaluation'] | B=['cognition', 'moral_evaluation', 'volition'] | **C=['moral_evaluation']**
- **Gen 6:5** kol (H3605) — own=[] | CURRENT=[] | A=[] | B=['cognition', 'moral_evaluation', 'volition'] | **C=[]**
- **Gen 6:5** ra.ah (H7200G) — own=[] | CURRENT=['cognition', 'perception', 'volition'] | A=[] | B=['cognition', 'moral_evaluation', 'volition'] | **C=[]**
- **Heb 9:14** katharizō (G2511) — own=[] | CURRENT=[] | A=[] | B=[] | **C=[]**
- **Mat 5:8** katharos (G2513) — own=[] | CURRENT=[] | A=[] | B=[] | **C=[]**
- **Eze 36:25** tum.ah (H2932) — own=[] | CURRENT=[] | A=[] | B=[] | **C=[]**
- **Gen 6:5** a.dam (H0120G) — own=[] | CURRENT=['volition'] | A=[] | B=['cognition', 'moral_evaluation', 'volition'] | **C=[]**
- **Heb 9:14** suneidesis (G4893) — own=['conscience', 'moral_evaluation'] | CURRENT=['conscience', 'moral_evaluation'] | A=[] | B=[] | **C=['conscience', 'moral_evaluation']**
- **Gen 6:5** ye.tser (H3336) — own=['volition'] | CURRENT=['volition'] | A=['volition'] | B=['cognition', 'moral_evaluation', 'volition'] | **C=['volition']**
- **Gen 6:5** ma.cha.sha.vah (H4284) — own=['cognition'] | CURRENT=['cognition'] | A=['cognition'] | B=['cognition', 'moral_evaluation', 'volition'] | **C=['cognition']**
- **Psa 51:10** ta.hor (H2889) — own=[] | CURRENT=[] | A=[] | B=[] | **C=[]**
- **Eze 36:25** ta.hor (H2889) — own=[] | CURRENT=[] | A=[] | B=[] | **C=[]**
- **Eze 36:25** ta.her (H2891) — own=[] | CURRENT=[] | A=[] | B=[] | **C=[]**
- **Gen 6:5** raq (H7535) — own=[] | CURRENT=[] | A=[] | B=['cognition', 'moral_evaluation', 'volition'] | **C=[]**
- **Heb 9:14** latreuō (G3000) — own=[] | CURRENT=[] | A=[] | B=[] | **C=[]**
- **Deu 6:5** ne.phesh (H5315G) — own=['affect', 'volition'] | CURRENT=['affect', 'volition'] | A=[] | B=[] | **C=['affect', 'volition']**
- **Mat 5:8** kardia (G2588) — own=['affect', 'cognition', 'volition', 'conscience', 'perception', 'moral_evaluation'] | CURRENT=['affect', 'cognition', 'conscience', 'moral_evaluation', 'perception', 'volition'] | A=[] | B=[] | **C=[]**
- **Deu 6:5** le.vav (H3824) — own=['cognition', 'conscience', 'perception', 'volition'] | CURRENT=['cognition', 'conscience', 'perception', 'volition'] | A=[] | B=[] | **C=['affect', 'volition']**
- **Psa 51:10** qe.rev (H7130H) — own=[] | CURRENT=[] | A=[] | B=[] | **C=[]**
- **Heb 9:14** pneuma (G4151G) — own=['affect', 'cognition', 'perception', 'volition'] | CURRENT=['affect', 'cognition', 'perception', 'volition'] | A=[] | B=[] | **C=['conscience', 'moral_evaluation']**
- **Deu 6:5** me.od (H3966) — own=[] | CURRENT=[] | A=[] | B=[] | **C=[]**
- **Heb 9:14** nekros (G3498) — own=[] | CURRENT=['affect'] | A=[] | B=[] | **C=[]**
- **Gen 6:5** lev (H3820A) — own=['cognition', 'conscience', 'perception', 'volition'] | CURRENT=['cognition', 'conscience', 'perception', 'volition'] | A=[] | B=['cognition', 'moral_evaluation', 'volition'] | **C=['cognition', 'moral_evaluation', 'volition']**
- **Psa 51:10** lev (H3820A) — own=['cognition', 'conscience', 'perception', 'volition'] | CURRENT=['cognition', 'conscience', 'perception', 'volition'] | A=[] | B=[] | **C=[]**

## Note
- A is fully defensible (every value = a monovalent word explicitly in the verse). Seats end EMPTY (their faculty is a reading = inferred = deferred).
- B rescues seats by reading the verse, but attributes any co-present monovalent faculty to the unit without proving binding (ceiling). Higher coverage, some noise.