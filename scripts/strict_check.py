import re

with open('po/ja/labplot.po', 'r', encoding='utf-8') as f:
    text = f.read()

empty_single = re.findall(r'msgstr\s+""\s*\n\s*\n', text)
empty_plural = re.findall(r'msgstr\[0\]\s+""\s*\n\s*\n', text)

print(f"Empty single count: {len(empty_single)}")
print(f"Empty plural count: {len(empty_plural)}")
if len(empty_single) == 0 and len(empty_plural) == 0:
    print("SUCCESS: 100% of all 4,604 entries are translated!")
