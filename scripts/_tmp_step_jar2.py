"""Inspect step-core JAR for REST endpoint paths and controller classes."""
import zipfile, re

jar_path = r"C:\Program Files (x86)\STEP\step-web\WEB-INF\lib\step-core-26.1.2.jar"

with zipfile.ZipFile(jar_path, 'r') as zf:
    names = zf.namelist()

print(f"Total entries: {len(names)}")

# REST/controller classes
rest_classes = sorted([n for n in names if re.search(r'rest|controller|Controller|Resource|endpoint', n, re.I) and n.endswith('.class')])
print(f"\nREST/controller classes: {len(rest_classes)}")
for c in rest_classes[:80]:
    print(f"  {c}")

# Guice module classes
guice_modules = sorted([n for n in names if 'module' in n.lower() and n.endswith('.class')])
print(f"\nGuice module classes: {len(guice_modules)}")
for g in guice_modules[:30]:
    print(f"  {g}")

# All class file paths (abbreviated to find package structure)
all_classes = sorted(set(['/'.join(n.split('/')[:4]) for n in names if n.endswith('.class')]))
print(f"\nTop-level packages (depth 4):")
for pkg in all_classes[:40]:
    print(f"  {pkg}")
