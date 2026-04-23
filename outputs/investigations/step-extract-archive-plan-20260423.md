# STEP Extract Archive Plan — Dry Run

**Generated:** 2026-04-23 07:42
**Source folder:** `data\exports\STEP Extracts`
**Archive target:** `data\exports\archive\STEP Extracts`

This plan is produced by `scripts/_audit_step_extract_archiving.py`. **No files have been moved.** Review, then execute by passing `--apply` to the script.

## Summary

| Metric | Count |
|---|---:|
| Groups (unique word+registry+scope) | 189 |
| Latest files kept in place | 189 |
| Older files to archive | 219 |
| Singletons (no siblings; unchanged) | 6 |
| Files that did not match expected pattern | 6 |

## Files that did not match the expected pattern

The following filenames did not match `{stem}_{YYYYMMDD}[_v{n}].json`. They will be ignored by an --apply run. Spot-check these.

- `term_G4893.json`
- `term_H2534.json`
- `term_H2734.json`
- `wa-112-mind-final-20260328.json`
- `wa-182-soul-final-20260328.json`
- `wa-registry-clustering-input-20260327.json`

## Proposed moves

### `Soul_182_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\Soul_182_full_20260324.json` | → | `data\exports\archive\STEP Extracts\Soul_182_full_20260324.json` | superseded by Soul_182_full_20260404_v1.json |
| `data\exports\STEP Extracts\Soul_182_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\Soul_182_full_20260328_v1.json` | superseded by Soul_182_full_20260404_v1.json |
| `data\exports\STEP Extracts\Soul_182_full_20260328_v2.json` | → | `data\exports\archive\STEP Extracts\Soul_182_full_20260328_v2.json` | superseded by Soul_182_full_20260404_v1.json |
### `abomination_1_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\abomination_1_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\abomination_1_full_20260328_v1.json` | superseded by abomination_1_full_20260330_v1.json |
### `agony_2_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\agony_2_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\agony_2_full_20260328_v1.json` | superseded by agony_2_full_20260330_v1.json |
### `ambition_3_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\ambition_3_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\ambition_3_full_20260328_v1.json` | superseded by ambition_3_full_20260330_v1.json |
### `anger_4_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\anger_4_full_20260324.json` | → | `data\exports\archive\STEP Extracts\anger_4_full_20260324.json` | superseded by anger_4_full_20260330_v1.json |
| `data\exports\STEP Extracts\anger_4_full_20260325.json` | → | `data\exports\archive\STEP Extracts\anger_4_full_20260325.json` | superseded by anger_4_full_20260330_v1.json |
### `anguish_5_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\anguish_5_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\anguish_5_full_20260328_v1.json` | superseded by anguish_5_full_20260330_v1.json |
### `anointing_6_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\anointing_6_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\anointing_6_full_20260328_v1.json` | superseded by anointing_6_full_20260331_v1.json |
### `anxiety_7_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\anxiety_7_full_20260325.json` | → | `data\exports\archive\STEP Extracts\anxiety_7_full_20260325.json` | superseded by anxiety_7_full_20260331_v1.json |
### `appetite_8_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\appetite_8_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\appetite_8_full_20260328_v1.json` | superseded by appetite_8_full_20260331_v1.json |
### `authority_197_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\authority_197_full_20260326.json` | → | `data\exports\archive\STEP Extracts\authority_197_full_20260326.json` | superseded by authority_197_full_20260405_v1.json |
| `data\exports\STEP Extracts\authority_197_full_20260326_v2.json` | → | `data\exports\archive\STEP Extracts\authority_197_full_20260326_v2.json` | superseded by authority_197_full_20260405_v1.json |
| `data\exports\STEP Extracts\authority_197_full_20260326_v3.json` | → | `data\exports\archive\STEP Extracts\authority_197_full_20260326_v3.json` | superseded by authority_197_full_20260405_v1.json |
| `data\exports\STEP Extracts\authority_197_full_20260326_v4.json` | → | `data\exports\archive\STEP Extracts\authority_197_full_20260326_v4.json` | superseded by authority_197_full_20260405_v1.json |
| `data\exports\STEP Extracts\authority_197_full_20260326_v5.json` | → | `data\exports\archive\STEP Extracts\authority_197_full_20260326_v5.json` | superseded by authority_197_full_20260405_v1.json |
### `awe_11_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\awe_11_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\awe_11_full_20260328_v1.json` | superseded by awe_11_full_20260331_v1.json |
### `being_211_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\being_211_full_20260327_v1.json` | → | `data\exports\archive\STEP Extracts\being_211_full_20260327_v1.json` | superseded by being_211_full_20260405_v1.json |
### `bitterness_13_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\bitterness_13_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\bitterness_13_full_20260328_v1.json` | superseded by bitterness_13_full_20260331_v1.json |
### `blessing_194_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\blessing_194_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\blessing_194_full_20260328_v1.json` | superseded by blessing_194_full_20260404_v1.json |
### `blindness (spiritual)_207_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\blindness (spiritual)_207_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\blindness (spiritual)_207_full_20260328_v1.json` | superseded by blindness (spiritual)_207_full_20260405_v1.json |
### `boastfulness_15_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\boastfulness_15_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\boastfulness_15_full_20260328_v1.json` | superseded by boastfulness_15_full_20260405_v1.json |
### `boldness_16_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\boldness_16_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\boldness_16_full_20260328_v1.json` | superseded by boldness_16_full_20260331_v1.json |
### `bondage_17_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\bondage_17_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\bondage_17_full_20260328_v1.json` | superseded by bondage_17_full_20260331_v1.json |
### `brokenness_18_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\brokenness_18_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\brokenness_18_full_20260328_v1.json` | superseded by brokenness_18_full_20260331_v1.json |
### `calling_19_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\calling_19_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\calling_19_full_20260328_v1.json` | superseded by calling_19_full_20260331_v1.json |
### `character_20_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\character_20_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\character_20_full_20260328_v1.json` | superseded by character_20_full_20260331_v1.json |
### `comfort_192_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\comfort_192_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\comfort_192_full_20260328_v1.json` | superseded by comfort_192_full_20260404_v1.json |
### `compassion_23_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\compassion_23_full_20260326_v1.json` | → | `data\exports\archive\STEP Extracts\compassion_23_full_20260326_v1.json` | superseded by compassion_23_full_20260331_v1.json |
| `data\exports\STEP Extracts\compassion_23_full_20260326_v2.json` | → | `data\exports\archive\STEP Extracts\compassion_23_full_20260326_v2.json` | superseded by compassion_23_full_20260331_v1.json |
### `condemnation_24_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\condemnation_24_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\condemnation_24_full_20260328_v1.json` | superseded by condemnation_24_full_20260331_v1.json |
### `conscience_26_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\conscience_26_full_20260325.json` | → | `data\exports\archive\STEP Extracts\conscience_26_full_20260325.json` | superseded by conscience_26_full_20260402_v1.json |
| `data\exports\STEP Extracts\conscience_26_full_20260331_v1.json` | → | `data\exports\archive\STEP Extracts\conscience_26_full_20260331_v1.json` | superseded by conscience_26_full_20260402_v1.json |
### `consciousness_27_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\consciousness_27_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\consciousness_27_full_20260328_v1.json` | superseded by consciousness_27_full_20260405_v1.json |
### `consecration_28_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\consecration_28_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\consecration_28_full_20260328_v1.json` | superseded by consecration_28_full_20260331_v1.json |
### `contempt_190_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\contempt_190_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\contempt_190_full_20260328_v1.json` | superseded by contempt_190_full_20260404_v1.json |
### `contentment_29_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\contentment_29_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\contentment_29_full_20260328_v1.json` | superseded by contentment_29_full_20260331_v1.json |
### `corruption_31_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\corruption_31_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\corruption_31_full_20260328_v1.json` | superseded by corruption_31_full_20260331_v1.json |
### `counsel_32_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\counsel_32_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\counsel_32_full_20260328_v1.json` | superseded by counsel_32_full_20260402_v1.json |
### `courage_33_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\courage_33_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\courage_33_full_20260328_v1.json` | superseded by courage_33_full_20260331_v1.json |
### `covenant_34_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\covenant_34_full_20260326_v1.json` | → | `data\exports\archive\STEP Extracts\covenant_34_full_20260326_v1.json` | superseded by covenant_34_full_20260331_v1.json |
| `data\exports\STEP Extracts\covenant_34_full_20260326_v2.json` | → | `data\exports\archive\STEP Extracts\covenant_34_full_20260326_v2.json` | superseded by covenant_34_full_20260331_v1.json |
| `data\exports\STEP Extracts\covenant_34_full_20260326_v3.json` | → | `data\exports\archive\STEP Extracts\covenant_34_full_20260326_v3.json` | superseded by covenant_34_full_20260331_v1.json |
| `data\exports\STEP Extracts\covenant_34_full_20260326_v4.json` | → | `data\exports\archive\STEP Extracts\covenant_34_full_20260326_v4.json` | superseded by covenant_34_full_20260331_v1.json |
### `covetousness_35_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\covetousness_35_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\covetousness_35_full_20260328_v1.json` | superseded by covetousness_35_full_20260331_v1.json |
### `craving_193_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\craving_193_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\craving_193_full_20260328_v1.json` | superseded by craving_193_full_20260404_v1.json |
### `deadness_210_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\deadness_210_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\deadness_210_full_20260328_v1.json` | superseded by deadness_210_full_20260405_v1.json |
### `debauchery_39_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\debauchery_39_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\debauchery_39_full_20260328_v1.json` | superseded by debauchery_39_full_20260331_v1.json |
### `deceit_40_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\deceit_40_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\deceit_40_full_20260328_v1.json` | superseded by deceit_40_full_20260331_v1.json |
### `defilement_41_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\defilement_41_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\defilement_41_full_20260328_v1.json` | superseded by defilement_41_full_20260331_v1.json |
### `delight_42_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\delight_42_full_20260326_v1.json` | → | `data\exports\archive\STEP Extracts\delight_42_full_20260326_v1.json` | superseded by delight_42_full_20260331_v1.json |
| `data\exports\STEP Extracts\delight_42_full_20260326_v2.json` | → | `data\exports\archive\STEP Extracts\delight_42_full_20260326_v2.json` | superseded by delight_42_full_20260331_v1.json |
### `desire_43_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\desire_43_full_20260325.json` | → | `data\exports\archive\STEP Extracts\desire_43_full_20260325.json` | superseded by desire_43_full_20260402_v1.json |
### `despair_44_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\despair_44_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\despair_44_full_20260328_v1.json` | superseded by despair_44_full_20260331_v1.json |
### `devotion_46_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\devotion_46_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\devotion_46_full_20260328_v1.json` | superseded by devotion_46_full_20260331_v1.json |
### `dignity_47_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\dignity_47_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\dignity_47_full_20260328_v1.json` | superseded by dignity_47_full_20260331_v1.json |
### `diligence_48_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\diligence_48_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\diligence_48_full_20260328_v1.json` | superseded by diligence_48_full_20260331_v1.json |
### `discernment_49_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\discernment_49_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\discernment_49_full_20260328_v1.json` | superseded by discernment_49_full_20260331_v1.json |
### `disobedience_50_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\disobedience_50_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\disobedience_50_full_20260328_v1.json` | superseded by disobedience_50_full_20260331_v1.json |
### `distress_51_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\distress_51_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\distress_51_full_20260328_v1.json` | superseded by distress_51_full_20260401_v1.json |
### `division_52_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\division_52_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\division_52_full_20260328_v1.json` | superseded by division_52_full_20260401_v1.json |
### `dominion_199_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\dominion_199_full_20260326.json` | → | `data\exports\archive\STEP Extracts\dominion_199_full_20260326.json` | superseded by dominion_199_full_20260405_v1.json |
| `data\exports\STEP Extracts\dominion_199_full_20260326_v2.json` | → | `data\exports\archive\STEP Extracts\dominion_199_full_20260326_v2.json` | superseded by dominion_199_full_20260405_v1.json |
### `doubt_191_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\doubt_191_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\doubt_191_full_20260328_v1.json` | superseded by doubt_191_full_20260404_v1.json |
### `dread_53_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\dread_53_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\dread_53_full_20260328_v1.json` | superseded by dread_53_full_20260401_v1.json |
### `endurance_55_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\endurance_55_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\endurance_55_full_20260328_v1.json` | superseded by endurance_55_full_20260401_v1.json |
### `energy_200_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\energy_200_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\energy_200_full_20260328_v1.json` | superseded by energy_200_full_20260405_v1.json |
### `envy_56_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\envy_56_full_20260325.json` | → | `data\exports\archive\STEP Extracts\envy_56_full_20260325.json` | superseded by envy_56_full_20260401_v1.json |
### `evil_57_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\evil_57_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\evil_57_full_20260328_v1.json` | superseded by evil_57_full_20260401_v1.json |
### `experience_58_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\experience_58_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\experience_58_full_20260328_v1.json` | superseded by experience_58_full_20260401_v1.json |
### `faith_59_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\faith_59_full_20260326_v1.json` | → | `data\exports\archive\STEP Extracts\faith_59_full_20260326_v1.json` | superseded by faith_59_full_20260401_v1.json |
| `data\exports\STEP Extracts\faith_59_full_20260326_v2.json` | → | `data\exports\archive\STEP Extracts\faith_59_full_20260326_v2.json` | superseded by faith_59_full_20260401_v1.json |
### `faithfulness_60_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\faithfulness_60_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\faithfulness_60_full_20260328_v1.json` | superseded by faithfulness_60_full_20260401_v1.json |
### `fear_61_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\fear_61_full_20260324.json` | → | `data\exports\archive\STEP Extracts\fear_61_full_20260324.json` | superseded by fear_61_full_20260401_v1.json |
| `data\exports\STEP Extracts\fear_61_full_20260325.json` | → | `data\exports\archive\STEP Extracts\fear_61_full_20260325.json` | superseded by fear_61_full_20260401_v1.json |
### `fellowship_62_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\fellowship_62_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\fellowship_62_full_20260328_v1.json` | superseded by fellowship_62_full_20260413_v1.json |
| `data\exports\STEP Extracts\fellowship_62_full_20260401_v1.json` | → | `data\exports\archive\STEP Extracts\fellowship_62_full_20260401_v1.json` | superseded by fellowship_62_full_20260413_v1.json |
### `flesh_185_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\flesh_185_full_20260326.json` | → | `data\exports\archive\STEP Extracts\flesh_185_full_20260326.json` | superseded by flesh_185_full_20260404_v1.json |
| `data\exports\STEP Extracts\flesh_185_full_20260326_v2.json` | → | `data\exports\archive\STEP Extracts\flesh_185_full_20260326_v2.json` | superseded by flesh_185_full_20260404_v1.json |
### `foolishness_63_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\foolishness_63_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\foolishness_63_full_20260328_v1.json` | superseded by foolishness_63_full_20260401_v1.json |
### `forgiveness_64_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\forgiveness_64_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\forgiveness_64_full_20260328_v1.json` | superseded by forgiveness_64_full_20260401_v1.json |
### `generosity_65_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\generosity_65_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\generosity_65_full_20260328_v1.json` | superseded by generosity_65_full_20260401_v1.json |
### `gentleness_66_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\gentleness_66_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\gentleness_66_full_20260328_v1.json` | superseded by gentleness_66_full_20260401_v1.json |
### `gladness_186_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\gladness_186_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\gladness_186_full_20260328_v1.json` | superseded by gladness_186_full_20260404_v1.json |
### `goodness_67_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\goodness_67_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\goodness_67_full_20260328_v1.json` | superseded by goodness_67_full_20260401_v1.json |
### `grace_68_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\grace_68_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\grace_68_full_20260328_v1.json` | superseded by grace_68_full_20260401_v1.json |
### `gratitude_69_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\gratitude_69_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\gratitude_69_full_20260328_v1.json` | superseded by gratitude_69_full_20260401_v1.json |
### `greed_70_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\greed_70_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\greed_70_full_20260328_v1.json` | superseded by greed_70_full_20260401_v1.json |
### `grief_71_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\grief_71_full_20260325.json` | → | `data\exports\archive\STEP Extracts\grief_71_full_20260325.json` | superseded by grief_71_full_20260401_v1.json |
### `groaning_72_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\groaning_72_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\groaning_72_full_20260328_v1.json` | superseded by groaning_72_full_20260401_v1.json |
### `guilt_73_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\guilt_73_full_20260325.json` | → | `data\exports\archive\STEP Extracts\guilt_73_full_20260325.json` | superseded by guilt_73_full_20260402_v1.json |
### `hardness_74_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\hardness_74_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\hardness_74_full_20260328_v1.json` | superseded by hardness_74_full_20260401_v1.json |
### `hatred_75_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\hatred_75_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\hatred_75_full_20260328_v1.json` | superseded by hatred_75_full_20260401_v1.json |
### `heart_183_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\heart_183_full_20260325.json` | → | `data\exports\archive\STEP Extracts\heart_183_full_20260325.json` | superseded by heart_183_full_20260404_v1.json |
| `data\exports\STEP Extracts\heart_183_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\heart_183_full_20260328_v1.json` | superseded by heart_183_full_20260404_v1.json |
### `holiness_76_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\holiness_76_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\holiness_76_full_20260328_v1.json` | superseded by holiness_76_full_20260401_v1.json |
### `honesty_77_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\honesty_77_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\honesty_77_full_20260328_v1.json` | superseded by honesty_77_full_20260401_v1.json |
### `hope_78_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\hope_78_full_20260325.json` | → | `data\exports\archive\STEP Extracts\hope_78_full_20260325.json` | superseded by hope_78_full_20260401_v1.json |
### `humility_80_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\humility_80_full_20260325.json` | → | `data\exports\archive\STEP Extracts\humility_80_full_20260325.json` | superseded by humility_80_full_20260401_v1.json |
| `data\exports\STEP Extracts\humility_80_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\humility_80_full_20260328_v1.json` | superseded by humility_80_full_20260401_v1.json |
### `hypocrisy_81_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\hypocrisy_81_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\hypocrisy_81_full_20260328_v1.json` | superseded by hypocrisy_81_full_20260401_v1.json |
### `idolatry_83_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\idolatry_83_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\idolatry_83_full_20260328_v1.json` | superseded by idolatry_83_full_20260401_v1.json |
### `image_201_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\image_201_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\image_201_full_20260328_v1.json` | superseded by image_201_full_20260405_v1.json |
### `imagination_85_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\imagination_85_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\imagination_85_full_20260328_v1.json` | superseded by imagination_85_full_20260401_v1.json |
### `impurity_86_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\impurity_86_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\impurity_86_full_20260328_v1.json` | superseded by impurity_86_full_20260401_v1.json |
### `indignation_87_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\indignation_87_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\indignation_87_full_20260328_v1.json` | superseded by indignation_87_full_20260401_v1.json |
### `iniquity_89_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\iniquity_89_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\iniquity_89_full_20260328_v1.json` | superseded by iniquity_89_full_20260402_v1.json |
### `innocence_90_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\innocence_90_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\innocence_90_full_20260328_v1.json` | superseded by innocence_90_full_20260402_v1.json |
### `insight_91_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\insight_91_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\insight_91_full_20260328_v1.json` | superseded by insight_91_full_20260402_v1.json |
### `integrity_92_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\integrity_92_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\integrity_92_full_20260328_v1.json` | superseded by integrity_92_full_20260402_v1.json |
### `intention_93_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\intention_93_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\intention_93_full_20260328_v1.json` | superseded by intention_93_full_20260402_v1.json |
### `intercession_94_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\intercession_94_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\intercession_94_full_20260328_v1.json` | superseded by intercession_94_full_20260402_v1.json |
### `jealousy_96_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\jealousy_96_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\jealousy_96_full_20260328_v1.json` | superseded by jealousy_96_full_20260402_v1.json |
### `joy_97_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\joy_97_full_20260325.json` | → | `data\exports\archive\STEP Extracts\joy_97_full_20260325.json` | superseded by joy_97_full_20260402_v1.json |
### `justice_98_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\justice_98_full_20260326_v1.json` | → | `data\exports\archive\STEP Extracts\justice_98_full_20260326_v1.json` | superseded by justice_98_full_20260402_v1.json |
| `data\exports\STEP Extracts\justice_98_full_20260326_v2.json` | → | `data\exports\archive\STEP Extracts\justice_98_full_20260326_v2.json` | superseded by justice_98_full_20260402_v1.json |
### `kindness_99_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\kindness_99_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\kindness_99_full_20260328_v1.json` | superseded by kindness_99_full_20260402_v1.json |
### `knowledge_100_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\knowledge_100_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\knowledge_100_full_20260328_v1.json` | superseded by knowledge_100_full_20260402_v1.json |
### `likeness_209_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\likeness_209_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\likeness_209_full_20260328_v1.json` | superseded by likeness_209_full_20260405_v1.json |
### `longing_102_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\longing_102_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\longing_102_full_20260328_v1.json` | superseded by longing_102_full_20260402_v1.json |
### `love_103_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\love_103_full_20260323.json` | → | `data\exports\archive\STEP Extracts\love_103_full_20260323.json` | superseded by love_103_full_20260402_v1.json |
| `data\exports\STEP Extracts\love_103_full_20260324.json` | → | `data\exports\archive\STEP Extracts\love_103_full_20260324.json` | superseded by love_103_full_20260402_v1.json |
| `data\exports\STEP Extracts\love_103_full_20260325.json` | → | `data\exports\archive\STEP Extracts\love_103_full_20260325.json` | superseded by love_103_full_20260402_v1.json |
| `data\exports\STEP Extracts\love_103_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\love_103_full_20260328_v1.json` | superseded by love_103_full_20260402_v1.json |
### `loyalty_104_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\loyalty_104_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\loyalty_104_full_20260328_v1.json` | superseded by loyalty_104_full_20260405_v1.json |
### `lust_105_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\lust_105_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\lust_105_full_20260328_v1.json` | superseded by lust_105_full_20260402_v1.json |
### `malice_189_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\malice_189_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\malice_189_full_20260328_v1.json` | superseded by malice_189_full_20260404_v1.json |
### `meaning_107_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\meaning_107_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\meaning_107_full_20260328_v1.json` | superseded by meaning_107_full_20260402_v1.json |
### `meditation_108_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\meditation_108_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\meditation_108_full_20260328_v1.json` | superseded by meditation_108_full_20260402_v1.json |
### `meekness_109_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\meekness_109_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\meekness_109_full_20260328_v1.json` | superseded by meekness_109_full_20260405_v1.json |
### `memory_110_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\memory_110_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\memory_110_full_20260328_v1.json` | superseded by memory_110_full_20260402_v1.json |
### `mercy_111_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\mercy_111_full_20260326_v1.json` | → | `data\exports\archive\STEP Extracts\mercy_111_full_20260326_v1.json` | superseded by mercy_111_full_20260402_v1.json |
| `data\exports\STEP Extracts\mercy_111_full_20260326_v2.json` | → | `data\exports\archive\STEP Extracts\mercy_111_full_20260326_v2.json` | superseded by mercy_111_full_20260402_v1.json |
| `data\exports\STEP Extracts\mercy_111_full_20260326_v3.json` | → | `data\exports\archive\STEP Extracts\mercy_111_full_20260326_v3.json` | superseded by mercy_111_full_20260402_v1.json |
### `might_198_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\might_198_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\might_198_full_20260328_v1.json` | superseded by might_198_full_20260405_v1.json |
### `mind_112_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\mind_112_full_20260327_v1.json` | → | `data\exports\archive\STEP Extracts\mind_112_full_20260327_v1.json` | superseded by mind_112_full_20260402_v1.json |
### `mourning_113_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\mourning_113_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\mourning_113_full_20260328_v1.json` | superseded by mourning_113_full_20260402_v1.json |
### `name_204_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\name_204_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\name_204_full_20260328_v1.json` | superseded by name_204_full_20260405_v1.json |
### `obedience_114_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\obedience_114_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\obedience_114_full_20260328_v1.json` | superseded by obedience_114_full_20260402_v1.json |
### `passion_115_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\passion_115_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\passion_115_full_20260328_v1.json` | superseded by passion_115_full_20260402_v1.json |
### `patience_116_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\patience_116_full_20260325.json` | → | `data\exports\archive\STEP Extracts\patience_116_full_20260325.json` | superseded by patience_116_full_20260402_v1.json |
### `peace_117_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\peace_117_full_20260325.json` | → | `data\exports\archive\STEP Extracts\peace_117_full_20260325.json` | superseded by peace_117_full_20260402_v1.json |
### `perverseness_120_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\perverseness_120_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\perverseness_120_full_20260328_v1.json` | superseded by perverseness_120_full_20260402_v1.json |
### `power_196_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\power_196_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\power_196_full_20260328_v1.json` | superseded by power_196_full_20260405_v1.json |
### `praise_121_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\praise_121_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\praise_121_full_20260328_v1.json` | superseded by praise_121_full_20260402_v1.json |
### `pray_212_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\pray_212_full_20260325.json` | → | `data\exports\archive\STEP Extracts\pray_212_full_20260325.json` | superseded by pray_212_full_20260405_v1.json |
| `data\exports\STEP Extracts\pray_212_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\pray_212_full_20260328_v1.json` | superseded by pray_212_full_20260405_v1.json |
### `prayer_122_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\prayer_122_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\prayer_122_full_20260328_v1.json` | superseded by prayer_122_full_20260402_v1.json |
### `pride_123_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\pride_123_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\pride_123_full_20260328_v1.json` | superseded by pride_123_full_20260402_v1.json |
### `prophecy_124_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\prophecy_124_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\prophecy_124_full_20260328_v1.json` | superseded by prophecy_124_full_20260403_v1.json |
### `purity_125_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\purity_125_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\purity_125_full_20260328_v1.json` | superseded by purity_125_full_20260403_v1.json |
### `purpose_126_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\purpose_126_full_20260326_v1.json` | → | `data\exports\archive\STEP Extracts\purpose_126_full_20260326_v1.json` | superseded by purpose_126_full_20260403_v1.json |
| `data\exports\STEP Extracts\purpose_126_full_20260326_v2.json` | → | `data\exports\archive\STEP Extracts\purpose_126_full_20260326_v2.json` | superseded by purpose_126_full_20260403_v1.json |
### `reasoning_127_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\reasoning_127_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\reasoning_127_full_20260328_v1.json` | superseded by reasoning_127_full_20260403_v1.json |
### `rebellion_128_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\rebellion_128_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\rebellion_128_full_20260328_v1.json` | superseded by rebellion_128_full_20260403_v1.json |
### `recognition_129_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\recognition_129_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\recognition_129_full_20260328_v1.json` | superseded by recognition_129_full_20260405_v1.json |
### `reconciliation_130_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\reconciliation_130_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\reconciliation_130_full_20260328_v1.json` | superseded by reconciliation_130_full_20260412_v1.json |
| `data\exports\STEP Extracts\reconciliation_130_full_20260403_v1.json` | → | `data\exports\archive\STEP Extracts\reconciliation_130_full_20260403_v1.json` | superseded by reconciliation_130_full_20260412_v1.json |
### `rejection_131_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\rejection_131_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\rejection_131_full_20260328_v1.json` | superseded by rejection_131_full_20260403_v1.json |
### `rejoicing_132_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\rejoicing_132_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\rejoicing_132_full_20260328_v1.json` | superseded by rejoicing_132_full_20260403_v1.json |
### `renewal_134_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\renewal_134_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\renewal_134_full_20260328_v1.json` | superseded by renewal_134_full_20260403_v1.json |
### `repentance_135_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\repentance_135_full_20260325.json` | → | `data\exports\archive\STEP Extracts\repentance_135_full_20260325.json` | superseded by repentance_135_full_20260403_v1.json |
### `resentment_205_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\resentment_205_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\resentment_205_full_20260328_v1.json` | superseded by resentment_205_full_20260405_v1.json |
### `resolve_137_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\resolve_137_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\resolve_137_full_20260328_v1.json` | superseded by resolve_137_full_20260405_v1.json |
### `reverence_138_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\reverence_138_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\reverence_138_full_20260328_v1.json` | superseded by reverence_138_full_20260405_v1.json |
### `righteousness_139_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\righteousness_139_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\righteousness_139_full_20260328_v1.json` | superseded by righteousness_139_full_20260403_v1.json |
### `seeking_140_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\seeking_140_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\seeking_140_full_20260328_v1.json` | superseded by seeking_140_full_20260403_v1.json |
### `self-control_142_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\self-control_142_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\self-control_142_full_20260328_v1.json` | superseded by self-control_142_full_20260403_v1.json |
### `sensuality_144_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\sensuality_144_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\sensuality_144_full_20260328_v1.json` | superseded by sensuality_144_full_20260405_v1.json |
### `shame_146_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\shame_146_full_20260325.json` | → | `data\exports\archive\STEP Extracts\shame_146_full_20260325.json` | superseded by shame_146_full_20260403_v1.json |
### `sin_147_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\sin_147_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\sin_147_full_20260328_v1.json` | superseded by sin_147_full_20260403_v1.json |
### `sincerity_148_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\sincerity_148_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\sincerity_148_full_20260328_v1.json` | superseded by sincerity_148_full_20260403_v1.json |
### `slander_149_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\slander_149_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\slander_149_full_20260328_v1.json` | superseded by slander_149_full_20260403_v1.json |
### `sloth_208_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\sloth_208_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\sloth_208_full_20260328_v1.json` | superseded by sloth_208_full_20260405_v1.json |
### `sorcery_150_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\sorcery_150_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\sorcery_150_full_20260328_v1.json` | superseded by sorcery_150_full_20260403_v1.json |
### `sorrow_151_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\sorrow_151_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\sorrow_151_full_20260328_v1.json` | superseded by sorrow_151_full_20260403_v1.json |
### `spirit_184_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\spirit_184_full_20260325.json` | → | `data\exports\archive\STEP Extracts\spirit_184_full_20260325.json` | superseded by spirit_184_full_20260404_v1.json |
### `strength_187_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\strength_187_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\strength_187_full_20260328_v1.json` | superseded by strength_187_full_20260405_v1.json |
### `strife_152_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\strife_152_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\strife_152_full_20260328_v1.json` | superseded by strife_152_full_20260403_v1.json |
### `stubbornness_153_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\stubbornness_153_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\stubbornness_153_full_20260328_v1.json` | superseded by stubbornness_153_full_20260403_v1.json |
### `submission_155_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\submission_155_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\submission_155_full_20260328_v1.json` | superseded by submission_155_full_20260403_v1.json |
### `suffering_214_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\suffering_214_full_20260411_v1.json` | → | `data\exports\archive\STEP Extracts\suffering_214_full_20260411_v1.json` | superseded by suffering_214_full_20260411_v3.json |
| `data\exports\STEP Extracts\suffering_214_full_20260411_v2.json` | → | `data\exports\archive\STEP Extracts\suffering_214_full_20260411_v2.json` | superseded by suffering_214_full_20260411_v3.json |
### `surrender_156_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\surrender_156_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\surrender_156_full_20260328_v1.json` | superseded by surrender_156_full_20260403_v1.json |
### `temptation_157_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\temptation_157_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\temptation_157_full_20260328_v1.json` | superseded by temptation_157_full_20260403_v1.json |
### `terror_158_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\terror_158_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\terror_158_full_20260328_v1.json` | superseded by terror_158_full_20260403_v1.json |
### `testimony_159_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\testimony_159_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\testimony_159_full_20260328_v1.json` | superseded by testimony_159_full_20260403_v1.json |
### `thought_160_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\thought_160_full_20260326_v1.json` | → | `data\exports\archive\STEP Extracts\thought_160_full_20260326_v1.json` | superseded by thought_160_full_20260403_v1.json |
| `data\exports\STEP Extracts\thought_160_full_20260326_v2.json` | → | `data\exports\archive\STEP Extracts\thought_160_full_20260326_v2.json` | superseded by thought_160_full_20260403_v1.json |
| `data\exports\STEP Extracts\thought_160_full_20260326_v3.json` | → | `data\exports\archive\STEP Extracts\thought_160_full_20260326_v3.json` | superseded by thought_160_full_20260403_v1.json |
### `transformation_202_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\transformation_202_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\transformation_202_full_20260328_v1.json` | superseded by transformation_202_full_20260405_v1.json |
### `transgression_162_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\transgression_162_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\transgression_162_full_20260328_v1.json` | superseded by transgression_162_full_20260403_v1.json |
### `treachery_203_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\treachery_203_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\treachery_203_full_20260328_v1.json` | superseded by treachery_203_full_20260405_v1.json |
### `trust_163_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\trust_163_full_20260326_v1.json` | → | `data\exports\archive\STEP Extracts\trust_163_full_20260326_v1.json` | superseded by trust_163_full_20260404_v1.json |
| `data\exports\STEP Extracts\trust_163_full_20260326_v2.json` | → | `data\exports\archive\STEP Extracts\trust_163_full_20260326_v2.json` | superseded by trust_163_full_20260404_v1.json |
| `data\exports\STEP Extracts\trust_163_full_20260403_v1.json` | → | `data\exports\archive\STEP Extracts\trust_163_full_20260403_v1.json` | superseded by trust_163_full_20260404_v1.json |
### `truthfulness_164_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\truthfulness_164_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\truthfulness_164_full_20260328_v1.json` | superseded by truthfulness_164_full_20260403_v1.json |
### `unbelief_165_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\unbelief_165_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\unbelief_165_full_20260328_v1.json` | superseded by unbelief_165_full_20260403_v1.json |
### `understanding_166_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\understanding_166_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\understanding_166_full_20260328_v1.json` | superseded by understanding_166_full_20260403_v1.json |
### `unity_167_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\unity_167_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\unity_167_full_20260328_v1.json` | superseded by unity_167_full_20260403_v1.json |
### `uprightness_168_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\uprightness_168_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\uprightness_168_full_20260328_v1.json` | superseded by uprightness_168_full_20260403_v1.json |
### `vulnerability_206_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\vulnerability_206_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\vulnerability_206_full_20260328_v1.json` | superseded by vulnerability_206_full_20260405_v1.json |
### `weakness_170_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\weakness_170_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\weakness_170_full_20260328_v1.json` | superseded by weakness_170_full_20260403_v1.json |
### `weeping_188_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\weeping_188_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\weeping_188_full_20260328_v1.json` | superseded by weeping_188_full_20260404_v1.json |
### `whoredom_171_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\whoredom_171_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\whoredom_171_full_20260328_v1.json` | superseded by whoredom_171_full_20260403_v1.json |
### `wickedness_172_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\wickedness_172_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\wickedness_172_full_20260328_v1.json` | superseded by wickedness_172_full_20260403_v1.json |
### `will_173_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\will_173_full_20260326_v1.json` | → | `data\exports\archive\STEP Extracts\will_173_full_20260326_v1.json` | superseded by will_173_full_20260404_v1.json |
| `data\exports\STEP Extracts\will_173_full_20260326_v2.json` | → | `data\exports\archive\STEP Extracts\will_173_full_20260326_v2.json` | superseded by will_173_full_20260404_v1.json |
| `data\exports\STEP Extracts\will_173_full_20260326_v3.json` | → | `data\exports\archive\STEP Extracts\will_173_full_20260326_v3.json` | superseded by will_173_full_20260404_v1.json |
### `wisdom_174_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\wisdom_174_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\wisdom_174_full_20260328_v1.json` | superseded by wisdom_174_full_20260404_v1.json |
### `wonder_175_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\wonder_175_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\wonder_175_full_20260328_v1.json` | superseded by wonder_175_full_20260404_v1.json |
### `word_registry_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\word_registry_full_20260325.json` | → | `data\exports\archive\STEP Extracts\word_registry_full_20260325.json` | superseded by word_registry_full_20260326.json |
### `worship_176_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\worship_176_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\worship_176_full_20260328_v1.json` | superseded by worship_176_full_20260404_v1.json |
### `worth_177_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\worth_177_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\worth_177_full_20260328_v1.json` | superseded by worth_177_full_20260405_v1.json |
### `wrath_178_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\wrath_178_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\wrath_178_full_20260328_v1.json` | superseded by wrath_178_full_20260404_v1.json |
### `yearning_179_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\yearning_179_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\yearning_179_full_20260328_v1.json` | superseded by yearning_179_full_20260404_v1.json |
### `yielding_180_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\yielding_180_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\yielding_180_full_20260328_v1.json` | superseded by yielding_180_full_20260404_v1.json |
### `zeal_181_full`

| Source | → | Target | Reason |
|---|:---:|---|---|
| `data\exports\STEP Extracts\zeal_181_full_20260328_v1.json` | → | `data\exports\archive\STEP Extracts\zeal_181_full_20260328_v1.json` | superseded by zeal_181_full_20260404_v1.json |
