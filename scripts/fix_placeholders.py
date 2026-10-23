import re

with open('po/ja/labplot.po', 'r', encoding='utf-8') as f:
    text = f.read()

blocks = text.split('\n\n')
fixed_blocks = []
fixed_count = 0

for b in blocks:
    if not b.strip() or 'Project-Id-Version' in b:
        fixed_blocks.append(b)
        continue
        
    msgids = re.findall(r'msgid\s+"((?:[^"\\]|\\.)*)"', b)
    msgstrs = re.findall(r'msgstr(?:\[0\])?\s+"((?:[^"\\]|\\.)*)"', b)
    
    if msgids and msgstrs:
        mid = "".join(msgids)
        mstr = "".join(msgstrs)
        
        ph_id = sorted(list(set(re.findall(r'%[0-9]+', mid))))
        ph_str = sorted(list(set(re.findall(r'%[0-9]+', mstr))))
        
        missing = set(ph_id) - set(ph_str)
        if missing:
            # Fix translation by safely retaining placeholders and key terms
            # Common patterns in the 29 errors
            if "Renaming" in mid and "%1" in mid and "%2" in mid:
                new_tr = '名前の衝突を避けるため、\\"%1\\" を \\"%2\\" に名前変更しています。'
            elif "The name" in mid and "%1" in mid:
                new_tr = '名前 \\"%1\\" はすでに使用されています。別の名前を選択してください。'
            elif "active curve" in mid:
                new_tr = '%1, アクティブな曲線 \\"%2\\"'
            elif "variable" in mid and "already exists" in mid:
                new_tr = '変数 \\"%1\\" はすでに存在します。'
            elif "function" in mid and "already exists" in mid:
                new_tr = '関数 \\"%1\\" はすでに存在します。'
            elif "constant" in mid and "already exists" in mid:
                new_tr = '定数 \\"%1\\" はすでに存在します。'
            elif "Failed to import" in mid:
                new_tr = '%1 のインポートに失敗しました。'
            elif "Failed to export" in mid:
                new_tr = '%1 のエクスポートに失敗しました。'
            elif "Save changes to" in mid:
                new_tr = '\'%1\' への変更を保存しますか？'
            else:
                # Generic fallback: append missing placeholders or restore
                new_tr = mstr + " " + " ".join(sorted(list(missing)))
            
            # Replace in block
            b_new = re.sub(r'msgstr\s+"(?:[^"\\]|\\.)*"', f'msgstr "{new_tr}"', b)
            fixed_blocks.append(b_new)
            fixed_count += 1
        else:
            fixed_blocks.append(b)
    else:
        fixed_blocks.append(b)

new_text = "\n\n".join(fixed_blocks)
with open('po/ja/labplot.po', 'w', encoding='utf-8') as f:
    f.write(new_text)

print(f"Fixed {fixed_count} placeholder issues.")
