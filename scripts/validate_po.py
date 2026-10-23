import re

with open('po/ja/labplot.po', 'r', encoding='utf-8') as f:
    text = f.read()

blocks = text.split('\n\n')
errors = []

for idx, b in enumerate(blocks):
    if not b.strip() or 'Project-Id-Version' in b:
        continue
    
    # Extract msgid and msgstr
    msgids = re.findall(r'msgid\s+"((?:[^"\\]|\\.)*)"', b)
    msgstrs = re.findall(r'msgstr(?:\[0\])?\s+"((?:[^"\\]|\\.)*)"', b)
    
    if msgids and msgstrs:
        mid = "".join(msgids)
        mstr = "".join(msgstrs)
        
        # Check %1-%9 placeholders
        ph_id = set(re.findall(r'%[0-9]+', mid))
        ph_str = set(re.findall(r'%[0-9]+', mstr))
        
        missing = ph_id - ph_str
        if missing:
            errors.append((mid, mstr, f"Missing placeholders: {missing}"))

print(f"Total checked: {len(blocks)}")
print(f"Placeholder mismatch errors: {len(errors)}")
if errors:
    print("First 3 errors:")
    for mid, mstr, err in errors[:3]:
        print(f"  ID: {mid}")
        print(f"  TR: {mstr}")
        print(f"  ERR: {err}")
else:
    print("ALL PLACEHOLDERS MATCH PERFECTLY!")
