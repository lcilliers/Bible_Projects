"""Try correct STEP search formats for Strong's number lookup.

From StepRequest.class analysis:
  - controller 'search' routes to SearchController
  - methods: suggest, masterSearch, getSubjectVerses, getExactForms
  - SearchController fields: searchService, suggestionService, subjectEntries, bibleInformationService
  - SearchController strings: 'search', 'input', 'context', 'referencesOnly'

The STEP URL format is: ?q=version=ESV_th@strong=H8057
So for masterSearch the args should likely be: strong=H8057|version=ESV_th (pipe-separated tokens)
"""
import requests, json

base = 'http://localhost:8989'
strong = 'H8057'

def probe(ep, label=''):
    r = requests.get(f'{base}{ep}', timeout=20)
    body = r.text
    is_error = 'errorMessage' in body
    has_hits = len(body) > 300 and not is_error
    tag = '*** OK ***' if has_hits else ('=ERROR=' if is_error else '  empty?')
    print(f'\n{tag} [{label}]')
    print(f'  {ep}')
    print(f'  Status:{r.status_code}  Len:{len(body)}')
    print(f'  Body: {body[:600]}')

# masterSearch with different arg formats
probe(f'/rest/search/masterSearch/strong={strong}|version=ESV_th', 'search q-style')
probe(f'/rest/search/masterSearch/strong={strong}|version=ESV_th|context=0', 'search q-style+ctx')
probe(f'/rest/search/masterSearch/strong%3D{strong}|version%3DESV_th', 'search encoded')

# Maybe the argument is just the search query string
probe(f'/rest/search/masterSearch?q=strong%3D{strong}%7Cversion%3DESV_th', 'search ?q=')
probe(f'/rest/search/masterSearch?input=strong%3D{strong}%7Cversion%3DESV_th', 'search ?input=')

# Try the passage search with THOT (tagged Hebrew OT) for Strong search
probe(f'/rest/bible/getStrongNumbersAndSubjects/{strong}/THOT', 'getStrongNumbersAndSubjects THOT')
probe(f'/rest/bible/getStrongNumbersAndSubjects/{strong}/ESV_th', 'getStrongNumbersAndSubjects ESV_th')
probe(f'/rest/bible/getStrongNumbersAndSubjects/{strong}/OHB', 'getStrongNumbersAndSubjects OHB')

# getBibleText to see actual tagged text with strongs
probe(f'/rest/bible/getBibleText/ESV_th/Gen.1.4', 'getBibleText Gen 1:4')

# Check module getInfo with all possible arg patterns
# Pattern: rest/module/getInfo/version/reference/vocabIdentifiers/morphIdentifiers/userLanguage
probe(f'/rest/module/getInfo/ESV_th//{strong}//', 'getInfo 5 args')
probe(f'/rest/module/getInfo/ESV_th//{strong}//en', 'getInfo 5 args + lang')
probe(f'/rest/module/getInfo/THOT//{strong}//en', 'getInfo THOT')
