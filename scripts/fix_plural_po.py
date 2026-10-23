import re
from translate_full_po import translate_entry

with open('po/ja/labplot.po', 'r', encoding='utf-8') as f:
    text = f.read()

blocks = text.split('\n\n')
new_blocks = []
plural_count = 0

for b in blocks:
    if 'msgid_plural' in b:
        # Extract msgid and msgid_plural
        m_single = re.search(r'msgid\s+"((?:[^"\\]|\\.)*)"', b)
        m_plural = re.search(r'msgid_plural\s+"((?:[^"\\]|\\.)*)"', b)
        
        single_id = m_single.group(1) if m_single else ""
        plural_id = m_plural.group(1) if m_plural else ""
        
        # Translate based on plural or single
        tr = translate_entry(plural_id if plural_id else single_id)
        tr_escaped = tr.replace('"', '\\"')
        
        # Replace msgstr[0] ""
        b_new = re.sub(r'msgstr\[0\]\s+"(?:[^"\\]|\\.)*"', f'msgstr[0] "{tr_escaped}"', b)
        # In case msgstr[0] wasn't matched
        if 'msgstr[0] ""' in b_new:
            b_new = b_new.replace('msgstr[0] ""', f'msgstr[0] "{tr_escaped}"')
        new_blocks.append(b_new)
        plural_count += 1
    else:
        new_blocks.append(b)

new_text = "\n\n".join(new_blocks)
with open('po/ja/labplot.po', 'w', encoding='utf-8') as f:
    f.write(new_text)

print(f"Updated {plural_count} plural entries.")
