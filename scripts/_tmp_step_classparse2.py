"""Parse STEP FrontController and AbstractAjaxController to understand routing."""
import struct, os, re

def read_utf8_strings(class_bytes):
    if class_bytes[:4] != b'\xca\xfe\xba\xbe':
        return []
    pos = 8
    constant_pool_count = struct.unpack('>H', class_bytes[pos:pos+2])[0]
    pos += 2
    strings = []
    i = 1
    while i < constant_pool_count:
        tag = class_bytes[pos]
        pos += 1
        if tag == 1:
            length = struct.unpack('>H', class_bytes[pos:pos+2])[0]
            pos += 2
            s = class_bytes[pos:pos+length].decode('utf-8', errors='replace')
            strings.append(s)
            pos += length
        elif tag in (7, 8, 16, 19, 20):
            pos += 2
        elif tag in (9, 10, 11, 12, 17, 18):
            pos += 4
        elif tag in (3, 4):
            pos += 4
        elif tag in (5, 6):
            pos += 8
            i += 1
        elif tag == 15:
            pos += 3
        else:
            break
        i += 1
    return strings

framework_dir = r"C:\Program Files (x86)\STEP\step-web\WEB-INF\classes\com\tyndalehouse\step\rest\framework"

for fname in sorted(os.listdir(framework_dir)):
    fpath = os.path.join(framework_dir, fname)
    with open(fpath, 'rb') as f:
        data = f.read()
    strings = read_utf8_strings(data)
    
    # All strings, unfiltered - we want to see URL patterns, error messages, etc.
    interesting = [s for s in strings if (
        2 < len(s) < 120
        and not s.startswith('(')
        and not s.startswith('[')
        and '\n' not in s
    )]
    
    print(f"\n=== {fname} ===")
    for s in interesting[:60]:
        print(f"  {repr(s)}")

# Also look at the Guice module that registers the REST routes
print("\n\n=== Guice StepServletModule ===")
guice_dir = r"C:\Program Files (x86)\STEP\step-web\WEB-INF\classes\com\tyndalehouse\step\guice"
for fname in sorted(os.listdir(guice_dir)):
    if '$' in fname:
        continue
    fpath = os.path.join(guice_dir, fname)
    with open(fpath, 'rb') as f:
        data = f.read()
    strings = read_utf8_strings(data)
    interesting = [s for s in strings if (
        2 < len(s) < 120
        and not s.startswith('(')
        and not s.startswith('[')
        and '\n' not in s
        and not s.startswith('Lcom/')
        and not s.startswith('Ljava/')
    )]
    print(f"\n--- {fname}")
    for s in interesting[:50]:
        print(f"  {repr(s)}")
