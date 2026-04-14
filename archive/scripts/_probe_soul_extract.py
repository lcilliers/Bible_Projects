"""Probe script — gather real STEP data for soul JSON example in design doc."""
import re, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from analytics.step_client import StepClient
from engine.span_filter import apply_span_filter

c = StepClient()

# ── H5315G — nephesh ─────────────────────────────────────────────────────────
vh = c.get_vocab_info('H5315G')
print("=== H5315G vocab ===")
print("gloss:", vh['gloss'])
print("transliteration:", vh['transliteration'])
print("script_form:", vh['hebrew_unicode'])
print("occurrence_count:", vh['occurrence_count'])
print("medium_def[:200]:", vh['medium_def'][:200])
print("meaning_numbered:", vh['meaning_numbered'])
print("causative_form_present:", vh['causative_form_present'])
print("related_words:", vh['related_words'][:3])

# ── H5314 — napash (root, G2 example) ────────────────────────────────────────
print("\n=== H5314 vocab ===")
vroot = c.get_vocab_info('H5314')
print("gloss:", vroot['gloss'])
print("transliteration:", vroot['transliteration'])
print("occurrence_count:", vroot['occurrence_count'])
print("medium_def[:200]:", vroot['medium_def'][:200])

# ── H5315G verses — find Gen.34.3 ────────────────────────────────────────────
print("\n=== H5315G verses ===")
records, html_map = c.get_verse_records_with_html('H5315G')
print("total verse count:", len(records))

v = next(x for x in records if x['osisId'] == 'Gen.34.3')
html = html_map['Gen.34.3']
print("osisId:", v['osisId'])
print("ref:", v['ref'])
print("esv_text:", v['esv_text'])
print("target_word:", v['target_word'])
print("testament:", v['testament'])

# span details
pairs = re.findall(r"strong='([^']+)'[^>]*>([^<]+)<", html)
print("span pairs:", pairs[:8])
res = apply_span_filter(html, 'H5315G')
print("span_filter result:", res)

# context
plain = re.sub(r'^\S+ \d+:\d+ ', '', v['esv_text'])
words = plain.split()
idx = next((i for i, w in enumerate(words) if 'soul' in w.lower()), None)
if idx is not None:
    print("context_before:", ' '.join(words[max(0, idx-5):idx]))
    print("context_after:",  ' '.join(words[idx+1:idx+6]))

# ── H5314 verses ─────────────────────────────────────────────────────────────
print("\n=== H5314 verses ===")
r2, h2 = c.get_verse_records_with_html('H5314')
print("total verse count:", len(r2))
if r2:
    v2 = r2[0]
    print("first osisId:", v2['osisId'], "ref:", v2['ref'])
    print("target_word:", v2['target_word'])

# ── G5590G — psuchē ─────────────────────────────────────────────────────────
print("\n=== G5590G vocab ===")
vg = c.get_vocab_info('G5590G')
print("gloss:", vg['gloss'])
print("transliteration:", vg['transliteration'])
print("script_form:", vg['hebrew_unicode'])
print("occurrence_count:", vg['occurrence_count'])
print("lsj_entry[:120]:", vg['lsj_entry'][:120])
print("short_def_mounce:", vg['short_def_mounce'])

# ── G4151 — pneuma (G5 example — related term, parent not anchor) ─────────────
print("\n=== G4151 vocab ===")
vp = c.get_vocab_info('G4151')
print("gloss:", vp['gloss'])
print("occurrence_count:", vp['occurrence_count'])
