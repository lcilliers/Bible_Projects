"""Inspect STEP JAR to find REST controller class paths and URL patterns."""
import zipfile, re

jar_path = r"C:\Program Files (x86)\STEP\step-server-26.1.2.jar"

with zipfile.ZipFile(jar_path, 'r') as zf:
    names = zf.namelist()

# Filter for REST/controller/resource classes
rest_classes = [n for n in names if re.search(r'rest|controller|Controller|Resource', n) and n.endswith('.class')]
print(f"REST/controller classes: {len(rest_classes)}")
for c in sorted(rest_classes)[:60]:
    print(f"  {c}")

# Also look for any .properties files that might have URL config
props = [n for n in names if n.endswith('.properties') or n.endswith('.yaml') or n.endswith('.yml')]
print(f"\nConfig files: {len(props)}")
for p in props[:30]:
    print(f"  {p}")

# Look for any jersey/resteasy config
jersey = [n for n in names if re.search(r'jersey|resteasy|javax.ws|jax-?rs', n, re.I)]
print(f"\nJAX-RS config: {len(jersey)}")
for j in jersey[:20]:
    print(f"  {j}")

# Look for Guice module classes
guice_modules = [n for n in names if 'module' in n.lower() and n.endswith('.class')]
print(f"\nGuice module classes: {len(guice_modules)}")
for g in guice_modules[:30]:
    print(f"  {g}")

# Read the main manifest
with zipfile.ZipFile(jar_path, 'r') as zf:
    try:
        manifest = zf.read('META-INF/MANIFEST.MF').decode('utf-8', errors='replace')
        print(f"\n--- MANIFEST.MF ---\n{manifest[:500]}")
    except:
        pass
