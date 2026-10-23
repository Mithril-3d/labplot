import re

with open('po/ja/labplot.po', 'r', encoding='utf-8') as f:
    text = f.read()

blocks = text.split('\n\n')
total = 0
translated = 0
untranslated = 0
empty_samples = []

for b in blocks:
    if 'msgid ' in b and 'Project-Id-Version' not in b:
        total += 1
        if 'msgid_plural' in b:
            m = re.search(r'msgstr\[0\]\s+"([^"]*)"', b)
            if m and m.group(1):
                translated += 1
            else:
                untranslated += 1
                empty_samples.append(b)
        else:
            m = re.search(r'msgstr\s+"([^"]*)"', b)
            if m and m.group(1):
                translated += 1
            else:
                # check multiline
                lines = b.split('\n')
                capture = False
                buf = []
                for l in lines:
                    if l.startswith('msgstr '):
                        capture = True
                        buf.append(l[7:].strip('"'))
                    elif capture and l.startswith('"'):
                        buf.append(l.strip('"'))
                    elif capture and not l.startswith('"'):
                        break
                val = "".join(buf)
                if val:
                    translated += 1
                else:
                    untranslated += 1
                    empty_samples.append(b)

print(f"Total entries: {total}")
print(f"Translated: {translated} ({translated/total*100:.2f}%)")
print(f"Untranslated: {untranslated} ({untranslated/total*100:.2f}%)")

if empty_samples:
    print(f"\nRemaining empty sample (1 of {len(empty_samples)}):")
    print(empty_samples[0])
