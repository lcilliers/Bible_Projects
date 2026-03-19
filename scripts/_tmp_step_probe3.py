"""Test STEP REST endpoints based on discovered routing:
  rest/<controller>/<method>/<args>
  
Controller names & methods found from class parsing:
  bible: getBibleText, getStrongNumbersAndSubjects, getText, getBibleByVerseNumber
  module: getInfo, getAllModules, full-vocab (vocabIdentifiers), analysis
  search: suggest, masterSearch, getSubjectVerses, getExactForms
"""
import requests, json

base = 'http://localhost:8989'
strong = 'H8057'  # simkhah - gladness
version = 'ESV_th'
version2 = 'THOT'

def probe(ep, label=''):
    r = requests.get(f'{base}{ep}', timeout=15)
    body = r.text
    ct = r.headers.get('Content-Type','?')
    is_error = 'errorMessage' in body
    print(f'\n{"=ERROR=" if is_error else "*** OK ***"} {label or ep}')
    print(f'  Status: {r.status_code}  CT: {ct[:50]}')
    print(f'  Body ({len(body)} chars): {body[:500]}')

# BibleController methods  
probe(f'/rest/bible/getStrongNumbersAndSubjects/{strong}/{version}', 'bible.getStrongNumbersAndSubjects')
probe(f'/rest/bible/getStrongNumbersAndSubjects/{strong}', 'bible.getStrongNumbersAndSubjects (no ver)')
probe(f'/rest/bible/getText/{version}/Gen.1.1/{strong}', 'bible.getText')
probe(f'/rest/bible/getBibleText/{version}/Gen.1.1', 'bible.getBibleText')

# ModuleController methods
probe(f'/rest/module/getInfo/{version}/{version}/H8057///en', 'module.getInfo explicit')
probe(f'/rest/module/getInfo/{version}//{strong}///', 'module.getInfo (vocab)')
probe(f'/rest/module/getInfo/ESV_th//H8057///', 'module.getInfo ESV_th')

# Search methods from the constant pool
probe(f'/rest/search/masterSearch/{strong}|version=ESV_th', 'search.masterSearch')
probe(f'/rest/search/getExactForms/{strong}', 'search.getExactForms')

# External V1 controller (there was an external package)
probe(f'/rest/external/v1/strong/{strong}', 'external.v1.strong')
probe(f'/rest/external/search?strong={strong}&version=ESV', 'external search')
