"""Read STEP controller .class files and extract string constant pool entries
to discover available REST method names."""
import struct, os, re

def read_utf8_strings(class_bytes):
    """Extract all CONSTANT_Utf8 strings from a .class file constant pool."""
    # Check magic number
    if class_bytes[:4] != b'\xca\xfe\xba\xbe':
        return []
    
    # Skip magic (4) + minor_version (2) + major_version (2)
    pos = 8
    constant_pool_count = struct.unpack('>H', class_bytes[pos:pos+2])[0]
    pos += 2
    
    strings = []
    i = 1
    while i < constant_pool_count:
        tag = class_bytes[pos]
        pos += 1
        if tag == 1:  # CONSTANT_Utf8
            length = struct.unpack('>H', class_bytes[pos:pos+2])[0]
            pos += 2
            s = class_bytes[pos:pos+length].decode('utf-8', errors='replace')
            strings.append(s)
            pos += length
        elif tag in (7, 8, 16, 19, 20):  # 2-byte index
            pos += 2
        elif tag in (9, 10, 11, 12, 17, 18):  # 4-byte
            pos += 4
        elif tag in (3, 4):  # int/float
            pos += 4
        elif tag in (5, 6):  # long/double (takes 2 slots)
            pos += 8
            i += 1  # long/double take 2 constant pool slots
        elif tag == 15:  # MethodHandle
            pos += 3
        else:
            break  # unknown tag, stop
        i += 1
    return strings

classes_dir = r"C:\Program Files (x86)\STEP\step-web\WEB-INF\classes\com\tyndalehouse\step\rest\controllers"

for fname in sorted(os.listdir(classes_dir)):
    if '$' in fname:
        continue  # skip inner classes
    fpath = os.path.join(classes_dir, fname)
    with open(fpath, 'rb') as f:
        data = f.read()
    strings = read_utf8_strings(data)
    
    # Filter for interesting strings: method-like, not just type descriptors
    interesting = [s for s in strings if (
        len(s) > 3 and len(s) < 80
        and not s.startswith('(')
        and not s.startswith('[')
        and not s.startswith('com/')
        and not s.startswith('java/')
        and not s.startswith('javax/')
        and not s.startswith('org/')
        and '/' not in s
        and not s.startswith('Ljava')
        and not s.startswith('Lcom')
    )]
    
    print(f"\n=== {fname} ===")
    for s in interesting[:40]:
        print(f"  {repr(s)}")
