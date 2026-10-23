import re
from collections import Counter

with open('po/ja/labplot.po', 'r', encoding='utf-8') as f:
    text = f.read()

msgids = re.findall(r'msgid\s+"((?:[^"\\]|\\.)*)"', text)
words = Counter()
for m in msgids:
    if not m or m == 'Project-Id-Version':
        continue
    tokens = re.findall(r'[a-zA-Z]+', m)
    for t in tokens:
        words[t.lower()] += 1

with open('top_words.txt', 'w', encoding='utf-8') as out:
    for w, c in words.most_common(100):
        out.write(f"{w}: {c}\n")

print("Top 100 words written to top_words.txt")
