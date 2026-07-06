# Gate-1 onboarding audit — reconciliation report

> Stamp: `anchor_note='gate1-onboard-2026'`. Baseline = pre-onboarding census. Live = current DB.

## Global deltas (baseline → live)

| metric | baseline | live | delta |
|---|---:|---:|---:|
| word_registry | 219 | 220 | +1 |
| file_index | 211 | 268 | +57 |
| mti_active | 2437 | 2533 | +96 |
| mti_all | 7616 | 7704 | +88 |
| inv_owner | 3648 | 3735 | +87 |
| inv_active | 6851 | 6938 | +87 |
| vr_active | 60472 | 63051 | +2579 |
| vc_active | 43155 | 50542 | +7387 |
| gate1_stamped | 0 | 96 | +96 |

## Collateral check (existing data integrity)

- gate1-stamped active terms (live): **96**
- non-gate1 active terms (live): 2437  vs baseline active 2437  →  **delta +0**
- ✅ NO collateral — existing terms preserved

### Per-registry active-term change (existing registries only; drops = collateral)

- ✅ no existing registry lost active terms

## Additions itemised — 96 terms across 52 registries

| registry | strong | gloss | cluster | status | active? | verse-records |
|---|---|---|---|---|---|---:|
| agony (2) | H2427A | agony | M03 | extracted_thin | yes | 6 |
| anguish (5) | H2342I | to twist: writh in pain | M03 | extracted | yes | 20 |
| betrayal (12) | H5800A | to leave: forsake | M20 | extracted | yes | 188 |
| bitterness (13) | H2556A | to leaven | — | extracted | yes | 6 |
| blessing (194) | H0835 | blessed | M39 | extracted | yes | 42 |
| contempt (190) | H3887 | to mock | M08 | extracted | yes | 27 |
| contempt (190) | H3932 | to mock | M08 | extracted | yes | 18 |
| contempt (190) | H3933 | derision | M08 | extracted | yes | 7 |
| contempt (190) | H7047 | derision | M08 | extracted | yes | 3 |
| contentment (29) | H7646 | to satisfy | M46 | extracted | yes | 93 |
| contrition (30) | H1793A | contrite | M11 | extracted | yes | 2 |
| corruption (31) | H0444 | to corrupt | M10 | extracted | yes | 3 |
| covetousness (35) | H1214I | to cut off: to gain | M29 | extracted | yes | 9 |
| craving (193) | H6770 | to thirst | M29 | extracted | yes | 10 |
| deceit (40) | H2665 | plot | M14 | extracted | yes | 1 |
| deceit (40) | H3576 | to lie | M14 | extracted | yes | 16 |
| deceit (40) | H3577 | lie | M14 | extracted | yes | 31 |
| deceit (40) | H6601B | to entice | — | extracted | yes | 23 |
| deceit (40) | H7723G | vanity: false | M14 | extracted | yes | 25 |
| delight (42) | H6149 | to please | M04 | extracted | yes | 8 |
| desire (43) | H3970 | desire | M29 | extracted | yes | 1 |
| disobedience (50) | H7683 | to go astray | M30 | extracted | yes | 4 |
| disobedience (50) | H7686 | to wander | M30 | extracted | yes | 19 |
| disobedience (50) | H8582 | to go astray | M30 | extracted | yes | 45 |
| distress (51) | H6323 | to distract | — | extracted | yes | 1 |
| distress (51) | H6817 | to cry | — | extracted | yes | 53 |
| distress (51) | H6962 | to loath | M06 | delete | yes | 6 |
| doubt (191) | H5640A | to close | — | extracted | yes | 13 |
| doubt (191) | H5641 | to hide | M20 | extracted | yes | 80 |
| doubt (191) | H7279 | to grumble | M20 | extracted | yes | 7 |
| evil (57) | H2154 | wickedness | M27 | extracted | yes | 27 |
| foolishness (63) | H0981 | to speak rashly | — | extracted | yes | 3 |
| foolishness (63) | H6612A | simple | M16 | extracted | yes | 18 |
| gentleness (66) | H6039 | affliction | M24 | delete | yes | 1 |
| grief (71) | H8428 | to wound | M03 | extracted | yes | 1 |
| heart (183) | H5036 | foolish | M16 | delete | yes | 18 |
| hope (78) | H3684 | fool | M16 | delete | yes | 69 |
| hope (78) | H3689 | loin | — | extracted | yes | 13 |
| humility (80) | H8217 | low | M09 | extracted | yes | 16 |
| hypocrisy (81) | H2611 | profane | — | extracted | yes | 13 |
| longing (102) | H3642 | to pine | M29 | extracted | yes | 1 |
| longing (102) | H6165 | to long for | M29 | extracted | yes | 2 |
| longing (102) | H8373 | to long for | M29 | extracted | yes | 2 |
| love (103) | H2898 | love | T2 | extracted | yes | 31 |
| mourning (113) | H7908 | bereavement | M03 | extracted | yes | 3 |
| obedience (114) | H5341 | to watch | M30 | extracted | yes | 62 |
| peace (117) | H1747 | silence | — | extracted | yes | 4 |
| perverseness (120) | H6141 | twisted | M14 | extracted | yes | 11 |
| praise (121) | H7321 | to shout | M22 | extracted | yes | 40 |
| pray (212) | H6419 | to pray | M21 | extracted | yes | 82 |
| prayer (122) | H8605 | prayer | M21 | extracted | yes | 70 |
| pride (123) | H6277 | arrogant | M08 | extracted | yes | 4 |
| pride (123) | H7342I | broad: arrogant | — | extracted | yes | 2 |
| pride (123) | H7426 | be exalted | M08 | extracted | yes | 6 |
| purity (125) | H1249 | pure | M12 | extracted | yes | 7 |
| purity (125) | H1252 | cleanness | M12 | extracted | yes | 5 |
| purity (125) | H1305 | to purify | M12 | extracted | yes | 16 |
| purity (125) | H2135 | to clean | M12 | extracted | yes | 8 |
| rebellion (128) | H4784 | to rebel | M30 | extracted | yes | 44 |
| rejection (131) | H2186A | to reject | M06 | extracted | yes | 19 |
| rejection (131) | H3988A | to reject | M06 | extracted | yes | 67 |
| rejection (131) | H5010 | to disown | M06 | extracted | yes | 2 |
| rejoicing (132) | H5937 | to exult | M04 | extracted | yes | 16 |
| rejoicing (132) | H5970 | to rejoice | M04 | extracted | yes | 8 |
| rejoicing (132) | H7832 | to laugh | M04 | extracted | yes | 36 |
| salvation (220) | H3468 | salvation | M38 | extracted | yes | 35 |
| salvation (220) | H4190 | salvation | M38 | extracted | yes | 1 |
| salvation (220) | H5826 | to help | M38 | extracted | yes | 77 |
| salvation (220) | H8668G | deliverance: salvation | M38 | extracted | yes | 21 |
| shame (146) | H5949 | wantonness | — | delete | yes | 24 |
| shame (146) | H7045 | curse | — | delete | yes | 33 |
| strife (152) | H4066 | strife | M02 | extracted | yes | 10 |
| strife (152) | H7283 | to throng | — | extracted | yes | 1 |
| strife (152) | H7853 | to oppose | M06 | extracted | yes | 6 |
| surrender (156) | H8444 | outgoing | — | delete | yes | 23 |
| temptation (157) | H0974 | to test | M35 | extracted | yes | 28 |
| temptation (157) | H5254G | to test | M35 | extracted | yes | 30 |
| terror (158) | H1161 | terror | M01 | extracted | yes | 2 |
| testimony (159) | H5046 | to tell | M42 | extracted | yes | 345 |
| weakness (170) | H0536 | weak | M24 | extracted | yes | 1 |
| weakness (170) | H2489 | helpless | M24 | extracted | yes | 2 |
| weakness (170) | H3021 | be weary/toil | M24 | extracted | yes | 25 |
| weakness (170) | H5848C | to enfeeble | M24 | extracted | yes | 11 |
| weakness (170) | H6199 | destitute | M24 | extracted | yes | 1 |
| weakness (170) | H7326 | be poor | M24 | extracted | yes | 24 |
| whoredom (171) | H5003 | to commit adultery | M10 | extracted | yes | 26 |
| wickedness (172) | H2149 | vileness | M10 | extracted | yes | 1 |
| wickedness (172) | H2555 | violence | M27 | extracted | yes | 59 |
| wickedness (172) | H6231 | to oppress | — | extracted | yes | 35 |
| wickedness (172) | H8496 | oppression | — | extracted | yes | 4 |
| wisdom (174) | H2451 | wisdom | M15 | extracted | yes | 145 |
| wisdom (174) | H4148G | discipline | M15 | extracted | yes | 29 |
| worth (177) | H3365 | be precious | M29 | extracted | yes | 11 |
| worth (177) | H3368 | precious | M29 | extracted | yes | 36 |
| wrath (178) | H5359 | vengeance | M02 | extracted | yes | 17 |
| wrath (178) | H5360 | vengeance | M02 | extracted | yes | 22 |

**Totals:** 96 terms, 2579 verse-records.