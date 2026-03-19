"""End-to-end test of the new step_client.py."""
import sys, json
sys.path.insert(0, r"G:\My Drive\Bible_study_projects")
from analytics.step_client import StepClient

client = StepClient()

# ── Test 1: H8057 simkhah (gladness, >60 verses) ─────────────────────────────
print('=== H8057 simkhah ===')
data = client.extract_word_data('H8057')
v = data['vocab']
print(f"strong          : {v['strong_number']}")
print(f"hebrew_unicode  : {v['hebrew_unicode']}")
print(f"transliteration : {v['transliteration']}")
print(f"gloss           : {v['gloss']}")
print(f"occurrence_count: {v['occurrence_count']}")
print(f"verse_count     : {data['verse_count']}")
print(f"notes           : {data['notes']}")
print(f"\nmedium_def:\n{v['medium_def']}")
print(f"\nrelated_words ({len(v['related_words'])}):")
for r in v['related_words']:
    print(f"  {r['strong']:8s}  {r['form']:15s}  {r['translit']:12s}  {r['gloss']}")
print(f"\nFirst 5 verse records:")
for vr in data['verse_records'][:5]:
    print(f"  {vr['ref']:20s}  [{vr['target_word']}]  {vr['esv_text'][:80]}")
print(f"\nLast 5 verse records:")
for vr in data['verse_records'][-5:]:
    print(f"  {vr['ref']:20s}  [{vr['target_word']}]  {vr['esv_text'][:80]}")

# ── Test 2: Non-canonical G9559 ───────────────────────────────────────────────
print('\n\n=== G9559 (non-canonical) ===')
d2 = client.extract_word_data('G9559')
print(f"gloss      : {d2['vocab'].get('gloss')}")
print(f"verse_count: {d2['verse_count']}")
print(f"notes      : {d2['notes']}")

# ── Test 3: Multi-gloss H2428 cha.yil ────────────────────────────────────────
print('\n\n=== H2428 cha.yil ===')
d3 = client.extract_word_data('H2428')
v3 = d3['vocab']
print(f"resolved strong : {v3['strong_number']}")
print(f"gloss           : {v3['gloss']}")
print(f"occurrence_count: {v3['occurrence_count']}")
print(f"verse_count     : {d3['verse_count']}")
print(f"notes           : {d3['notes']}")
print(f"medium_def: {v3['medium_def'][:200]}")

# ── Test 4: Small word H0157 ahab (love, large registry) ─────────────────────
print('\n\n=== H0157 ahab (love) ===')
d4 = client.extract_word_data('H0157')
print(f"gloss           : {d4['vocab'].get('gloss')}")
print(f"occurrence_count: {d4['vocab'].get('occurrence_count')}")
print(f"verse_count     : {d4['verse_count']}")
print(f"notes           : {d4['notes']}")
