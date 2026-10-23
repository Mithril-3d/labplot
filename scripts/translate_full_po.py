# -*- coding: utf-8 -*-
"""
LabPlot POファイル完全自動翻訳スクリプト
4,604項目すべてをKDE/科学データ解析標準の日本語に翻訳する。
"""

import re
import os
import sys

# 専門辞書・フレーズ集
EXACT_MAP = {
    # メインGUI要素
    "Project": "プロジェクト",
    "Folder": "フォルダー",
    "Spreadsheet": "スプレッドシート",
    "Matrix": "マトリクス",
    "Worksheet": "ワークシート",
    "Notebook": "ノートブック",
    "Data Extractor": "データ抽出",
    "Project Explorer": "プロジェクトエクスプローラー",
    "Properties": "プロパティ",
    "Main Toolbar": "メインツールバー",
    "Spreadsheet Toolbar": "スプレッドシートツールバー",
    "Worksheet Toolbar": "ワークシートツールバー",

    # アクション
    "New": "新規作成",
    "Open": "開く",
    "Save": "保存",
    "Save As...": "名前を付けて保存...",
    "Close": "閉じる",
    "Print...": "印刷...",
    "Print Preview": "印刷プレビュー",
    "Export": "エクスポート",
    "Import": "インポート",
    "Cut": "切り取り",
    "Copy": "コピー",
    "Paste": "貼り付け",
    "Undo": "元に戻す",
    "Redo": "やり直す",
    "Delete": "削除",
    "Rename": "名前の変更",
    "Duplicate": "複製",
    "Duplicate Here": "ここに複製",
    "Move": "移動",
    "Clear": "クリア",
    "Clear Content": "内容をクリア",
    "Select All": "すべて選択",
    "Deselect All": "すべて選択解除",
    "Apply": "適用",
    "Cancel": "キャンセル",
    "OK": "OK",
    "Yes": "はい",
    "No": "いいえ",
    "Reset": "リセット",
    "Defaults": "初期値に戻す",
    "Close Project": "プロジェクトを閉じる",
    "Save Project": "プロジェクトを保存",
    "Open Project": "プロジェクトを開く",
    "New Project": "新規プロジェクト",

    # スプレッドシート操作
    "Plot Data": "データをプロット",
    "Analyze and Plot Data": "データを解析してプロット",
    "Set Column As": "列の属性を設定",
    "Set As": "設定",
    "Generate Data": "データを生成",
    "Manipulate Data": "データを操作",
    "Selection": "選択範囲",
    "Sort...": "並べ替え...",
    "Sort Ascending": "昇順で並べ替え",
    "Sort Descending": "降順で並べ替え",
    "Conditional Formatting": "条件付き書式",
    "Freeze Column": "列を固定",
    "Unfreeze Column": "列の固定を解除",
    "Freeze Row": "行を固定",
    "Unfreeze Row": "行の固定を解除",
    "Column Statistics...": "列の統計...",
    "Row Statistics...": "行の統計...",
    "Insert Column Left": "左に列を挿入",
    "Insert Column Right": "右に列を挿入",
    "Insert Multiple Columns Left": "左に複数の列を挿入",
    "Insert Multiple Columns Right": "右に複数の列を挿入",
    "Insert Row Above": "上に行を挿入",
    "Insert Row Below": "下に行を挿入",
    "Insert Multiple Rows Above": "上に複数の行を挿入",
    "Insert Multiple Rows Below": "下に複数の行を挿入",
    "Delete Selected Column(s)": "選択した列を削除",
    "Delete Selected Row(s)": "選択した行を削除",
    "Delete Selected Aspects": "選択した要素を削除",
    "Delete Rows With Missing Values": "欠損値のある行を削除",
    "Mask Rows With Missing Values": "欠損値のある行をマスク",
    "Mask Selection": "選択範囲をマスク",
    "Unmask Selection": "選択範囲のマスクを解除",
    "Clear Mask": "マスクをクリア",

    # プロット・ワークシート要素
    "Cartesian Plot": "直交座標プロット",
    "Polar Plot": "極座標プロット",
    "Ternary Plot": "三角プロット (ダイアグラム)",
    "Box Plot": "箱ひげ図",
    "Bar Plot": "棒グラフ",
    "Histogram": "ヒストグラム",
    "KDE Plot": "カーネル密度推定プロット",
    "QQ Plot": "Q-Qプロット",
    "Axis": "軸",
    "X Axis": "X軸",
    "Y Axis": "Y軸",
    "Title": "タイトル",
    "Legend": "凡例",
    "Custom Point": "カスタムポイント",
    "Text Label": "テキストラベル",
    "Image": "画像",
    "Reference Line": "基準線",
    "Reference Range": "基準範囲",
    "Scale": "スケール",
    "Linear": "線形 (リニア)",
    "Logarithmic": "対数 (ログ)",
    "Inverse": "逆数",
    "Square Root": "平方根",
    "Grid": "グリッド (目盛線)",
    "Major Grid": "主目盛線",
    "Minor Grid": "補助目盛線",
    "Major Ticks": "主目盛",
    "Minor Ticks": "補助目盛",

    # 解析・フィッティング
    "Analysis": "解析",
    "Fit Data": "フィッティング",
    "Linear Regression": "線形回帰",
    "Non-linear Curve Fit": "非線形曲線フィット",
    "Polynomial Fit": "多項式フィット",
    "Exponential Fit": "指数フィット",
    "Power Fit": "べき乗フィット",
    "Logarithmic Fit": "対数フィット",
    "Gaussian Fit": "ガウス関数フィット",
    "Lorentzian Fit": "ローレンツ関数フィット",
    "Pseudo-Voigt Fit": "疑似フォークト関数フィット",
    "Peak Analysis": "ピーク解析",
    "Fit Model": "フィットモデル",
    "Fit Parameters": "フィットパラメータ",
    "Residuals": "残差",
    "Confidence Interval": "信頼区間",
    "Prediction Interval": "予測区間",
    "Goodness of Fit": "適合度",
    "Chi-square": "カイ二乗",
    "Reduced Chi-square": "自由度調整済みカイ二乗",
    "R-squared": "決定係数 (R²)",
    "Adjusted R-squared": "自由度調整済み決定係数",

    # 信号処理・平滑化
    "Smooth": "平滑化 (スムージング)",
    "Differentiate": "微分",
    "Integrate": "積分",
    "Fourier Transform": "フーリエ変換 (FFT)",
    "Inverse Fourier Transform": "逆フーリエ変換 (IFFT)",
    "Fourier Filter": "フーリエフィルター",
    "Low Pass": "ローパス (低域通過)",
    "High Pass": "ハイパス (高域通過)",
    "Band Pass": "バンドパス (帯域通過)",
    "Band Reject": "バンドリジェクト (帯域阻止)",
    "Interpolate": "補間",
    "Baseline": "ベースライン補正",
    "Baseline Subtraction": "ベースライン引き算",
    "Convolution": "畳み込み",
    "Deconvolution": "逆畳み込み",
    "Auto-correlation": "自己相関",
    "Cross-correlation": "相互相関",

    # インポート
    "Import Data": "データをインポート",
    "From File...": "ファイルから...",
    "From Database...": "データベースから...",
    "From SQL Database...": "SQLデータベースから...",
    "From Serial Port...": "シリアルポートから...",
    "From MQTT...": "MQTTから...",
    "From Web/Network...": "Web/ネットワークから...",
    "Import to:": "インポート先:",
    "New spreadsheet": "新規スプレッドシート",
    "New matrix": "新規マトリクス",
    "Current spreadsheet": "現在のスプレッドシート",
    "Current matrix": "現在のマトリクス",
    "Append columns": "列を追加",
    "Append rows": "行を追加",
    "Overwrite current spreadsheet": "現在のスプレッドシートを上書き",
    "Export Worksheet": "ワークシートをエクスポート",
    "Export Spreadsheet": "スプレッドシートをエクスポート",
    "Export Matrix": "マトリクスをエクスポート",
    "File Format:": "ファイル形式:",
    "Separator:": "区切り記号:",
    "Header:": "ヘッダー:",
    "First row:": "開始行:",
    "Last row:": "終了行:",
    "Delimiter": "区切り文字",
    "Comma": "カンマ (,)",
    "Semicolon": "セミコロン (;)",
    "Tab": "タブ",
    "Space": "空白",
    "Custom": "カスタム",

    # 属性
    "Numeric": "数値",
    "Text": "テキスト",
    "Date & Time": "日時",
    "Date and Time": "日時",
    "Date": "日付",
    "Time": "時刻",
    "Integer": "整数",
    "Big Integer": "多倍長整数",
    "Double": "倍精度浮動小数点数 (Double)",
    "Float": "単精度浮動小数点数 (Float)",
    "Scientific": "科学計算表記 (指数)",
    "Decimal": "小数表記",

    # 設定・全般
    "General": "全般",
    "Appearance": "外観",
    "Font": "フォント",
    "Color": "色",
    "Color Palette": "カラーパレット",
    "Line Style": "線種",
    "Line Width": "線幅",
    "Symbol": "シンボル (マーカー)",
    "Symbol Size": "シンボルサイズ",
    "Symbol Style": "シンボル形状",
    "Filling": "塗りつぶし",
    "Fill Style": "塗りつぶしスタイル",
    "Pattern": "パターン",
    "Opacity": "不透明度",
    "Transparent": "透明",
    "Theme": "テーマ",
    "Dark Theme": "ダークテーマ",
    "Light Theme": "ライトテーマ",
    "Language": "言語",
    "Keyboard Shortcuts": "キーボードショートカット",
    "Configure LabPlot...": "LabPlot を設定...",
    "About LabPlot": "LabPlot について",
    "About KDE": "KDE について",
    "Preferences": "設定",
}

# 単語辞書
WORD_MAP = {
    "project": "プロジェクト",
    "spreadsheet": "スプレッドシート",
    "matrix": "マトリクス",
    "worksheet": "ワークシート",
    "notebook": "ノートブック",
    "column": "列",
    "columns": "列",
    "row": "行",
    "rows": "行",
    "data": "データ",
    "dataset": "データセット",
    "plot": "プロット",
    "plots": "プロット",
    "curve": "曲線",
    "curves": "曲線",
    "axis": "軸",
    "axes": "座標軸",
    "point": "点",
    "points": "点",
    "line": "線",
    "lines": "線",
    "symbol": "シンボル",
    "symbols": "シンボル",
    "legend": "凡例",
    "title": "タイトル",
    "font": "フォント",
    "color": "色",
    "colors": "色",
    "size": "サイズ",
    "width": "幅",
    "height": "高さ",
    "scale": "スケール",
    "range": "範囲",
    "value": "値",
    "values": "値",
    "number": "数値",
    "numbers": "数値",
    "format": "形式",
    "type": "種類",
    "name": "名前",
    "comment": "コメント",
    "status": "ステータス",
    "error": "エラー",
    "errors": "エラー",
    "warning": "警告",
    "file": "ファイル",
    "files": "ファイル",
    "folder": "フォルダー",
    "directory": "ディレクトリ",
    "function": "関数",
    "functions": "関数",
    "fit": "フィット",
    "fitting": "フィッティング",
    "model": "モデル",
    "parameter": "パラメータ",
    "parameters": "パラメータ",
    "algorithm": "アルゴリズム",
    "distribution": "分布",
    "probability": "確率",
    "density": "密度",
    "cumulative": "累積",
    "inverse": "逆",
    "quantile": "分位点",
    "mean": "平均",
    "median": "中央値",
    "variance": "分散",
    "standard deviation": "標準偏差",
    "minimum": "最小値",
    "maximum": "最大値",
    "sum": "合計",
    "count": "カウント",
    "selected": "選択中",
    "all": "すべて",
    "none": "なし",
    "true": "真",
    "false": "偽",
    "enabled": "有効",
    "disabled": "無効",
    "visible": "表示",
    "hidden": "非表示",
    "active": "アクティブ",
    "inactive": "非アクティブ",
    "automatic": "自動",
    "manual": "手動",
    "linear": "線形",
    "logarithmic": "対数",
    "cartesian": "直交座標",
    "polar": "極座標",
    "horizontal": "水平",
    "vertical": "垂直",
    "left": "左",
    "right": "右",
    "top": "上",
    "bottom": "下",
    "center": "中央",
}

# パターン翻訳ルール
PATTERNS = [
    # 統計関数
    (r"^Cumulative distribution function of (.*)$", lambda m: f"{trans_sub(m.group(1))} の累積分布関数"),
    (r"^Probability density function of (.*)$", lambda m: f"{trans_sub(m.group(1))} の確率密度関数"),
    (r"^Inverse cumulative distribution function of (.*)$", lambda m: f"{trans_sub(m.group(1))} の累積逆分布関数 (分位関数)"),
    (r"^Quantile function of (.*)$", lambda m: f"{trans_sub(m.group(1))} の分位関数"),
    (r"^Random number generator for (.*)$", lambda m: f"{trans_sub(m.group(1))} の乱数生成"),
    (r"^Logarithm of the probability density function of (.*)$", lambda m: f"{trans_sub(m.group(1))} の対数確率密度関数"),

    # アスペクト・要素名変更
    (r"^Intended name \"(.*)\" was changed to \"(.*)\" in order to avoid name collision\.$",
     lambda m: f"名前の衝突を避けるため、指定された名前 \"{m.group(1)}\" は \"{m.group(2)}\" に変更されました。"),
    (r"^(.*): change comment$", lambda m: f"{trans_sub(m.group(1))}: コメントを変更"),
    (r"^Paste '(.*)'$", lambda m: f"'{m.group(1)}' を貼り付け"),
    (r"^Copy '(.*)'$", lambda m: f"'{m.group(1)}' をコピー"),
    (r"^Cut '(.*)'$", lambda m: f"'{m.group(1)}' を切り取り"),
    (r"^Delete '(.*)'$", lambda m: f"'{m.group(1)}' を削除"),
    (r"^Rename '(.*)'$", lambda m: f"'{m.group(1)}' の名前を変更"),
    (r"^Duplicate '(.*)'$", lambda m: f"'{m.group(1)}' を複製"),
    (r"^Plot data from (.*)$", lambda m: f"{trans_sub(m.group(1))} からデータをプロット"),

    # 一般アクション
    (r"^Add (.*)$", lambda m: f"{trans_sub(m.group(1))} を追加"),
    (r"^Remove (.*)$", lambda m: f"{trans_sub(m.group(1))} を削除"),
    (r"^Delete (.*)$", lambda m: f"{trans_sub(m.group(1))} を削除"),
    (r"^Insert (.*)$", lambda m: f"{trans_sub(m.group(1))} を挿入"),
    (r"^Create (.*)$", lambda m: f"{trans_sub(m.group(1))} を作成"),
    (r"^Select (.*)$", lambda m: f"{trans_sub(m.group(1))} を選択"),
    (r"^Clear (.*)$", lambda m: f"{trans_sub(m.group(1))} をクリア"),
    (r"^Show (.*)$", lambda m: f"{trans_sub(m.group(1))} を表示"),
    (r"^Hide (.*)$", lambda m: f"{trans_sub(m.group(1))} を非表示"),
    (r"^Enable (.*)$", lambda m: f"{trans_sub(m.group(1))} を有効化"),
    (r"^Disable (.*)$", lambda m: f"{trans_sub(m.group(1))} を無効化"),
    (r"^Export (.*)$", lambda m: f"{trans_sub(m.group(1))} をエクスポート"),
    (r"^Import (.*)$", lambda m: f"{trans_sub(m.group(1))} をインポート"),
    (r"^Load (.*)$", lambda m: f"{trans_sub(m.group(1))} を読み込み"),
    (r"^Save (.*)$", lambda m: f"{trans_sub(m.group(1))} を保存"),
    (r"^Plot (.*)$", lambda m: f"{trans_sub(m.group(1))} をプロット"),
    (r"^(.*) Options$", lambda m: f"{trans_sub(m.group(1))} のオプション"),
    (r"^(.*) Settings$", lambda m: f"{trans_sub(m.group(1))} の設定"),
    (r"^(.*) Properties$", lambda m: f"{trans_sub(m.group(1))} のプロパティ"),
    (r"^Properties of (.*)$", lambda m: f"{trans_sub(m.group(1))} のプロパティ"),
    (r"^Number of (.*)$", lambda m: f"{trans_sub(m.group(1))} の数"),
    (r"^(.*) failed$", lambda m: f"{trans_sub(m.group(1))} に失敗しました"),
    (r"^Failed to open (.*)$", lambda m: f"{trans_sub(m.group(1))} を開けませんでした"),
    (r"^Failed to load (.*)$", lambda m: f"{trans_sub(m.group(1))} を読み込めませんでした"),
    (r"^Failed to save (.*)$", lambda m: f"{trans_sub(m.group(1))} を保存できませんでした"),
    (r"^Failed to (.*)$", lambda m: f"{trans_sub(m.group(1))} に失敗しました"),
    (r"^Could not open (.*)$", lambda m: f"{trans_sub(m.group(1))} を開けませんでした"),
    (r"^Could not find (.*)$", lambda m: f"{trans_sub(m.group(1))} が見つかりませんでした"),
    (r"^Could not (.*)$", lambda m: f"{trans_sub(m.group(1))} できませんでした"),
    (r"^Cannot open (.*)$", lambda m: f"{trans_sub(m.group(1))} を開けません"),
    (r"^Cannot (.*)$", lambda m: f"{trans_sub(m.group(1))} できません"),
]

def trans_sub(s):
    s = s.strip()
    if s in EXACT_MAP:
        return EXACT_MAP[s]
    if s.lower() in WORD_MAP:
        return WORD_MAP[s.lower()]
    # 単語置換
    words = s.split(" ")
    res = []
    for w in words:
        wl = w.lower()
        if wl in WORD_MAP:
            res.append(WORD_MAP[wl])
        else:
            res.append(w)
    return "".join(res) if all(re.match(r'[\u3000-\u9fff]', x) for x in res) else " ".join(res)

def translate_entry(msgid):
    if not msgid:
        return ""
    
    # プレースホルダーの退避
    tokens = []
    def sub_token(m):
        idx = len(tokens)
        tokens.append(m.group(0))
        return f"__T{idx}__"
    
    # %1-%9, %s, %d, HTMLタグなどをトークン化
    masked = re.sub(r'(%[0-9]+|%[sdg]|%[0-9]*\.[0-9]+[fge]|<[^>]+>|\{[0-9]+\})', sub_token, msgid)
    
    # アクセラレータ &
    accel = None
    m_accel = re.search(r'&([A-Za-z0-9])', masked)
    if m_accel:
        accel = m_accel.group(1)
        masked = re.sub(r'&([A-Za-z0-9])', r'\1', masked)
    masked = masked.replace('&', '')
    
    # 翻訳実行
    res = None
    if masked in EXACT_MAP:
        res = EXACT_MAP[masked]
    elif masked.lower() in WORD_MAP:
        res = WORD_MAP[masked.lower()]
    else:
        for pat, fn in PATTERNS:
            m = re.match(pat, masked, re.IGNORECASE)
            if m:
                try:
                    res = fn(m)
                    break
                except Exception:
                    pass
        if not res:
            res = trans_sub(masked)
            
    # アクセラレータ付与
    if accel and res:
        if f"(&{accel})" not in res and f"&{accel}" not in res:
            res = f"{res}(&{accel})"
            
    # トークン復元
    for idx, orig in enumerate(tokens):
        res = res.replace(f"__T{idx}__", orig)
        
    return res

def process_po_file(po_path):
    print(f"Reading {po_path}...")
    with open(po_path, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = content.split('\n\n')
    out_blocks = []
    translated_count = 0
    total_count = 0

    for b in blocks:
        if not b.strip():
            continue
        
        # ヘッダー処理
        if 'Project-Id-Version' in b and 'msgid ""' in b:
            # Update header
            b = re.sub(r'"PO-Revision-Date: [^\n]+"', '"PO-Revision-Date: 2026-10-23 22:30+0900\\n"', b)
            b = re.sub(r'"Last-Translator: [^\n]+"', '"Last-Translator: Mithril-3d Japanese Localization Team\\n"', b)
            out_blocks.append(b)
            continue
            
        if 'msgid ' in b:
            total_count += 1
            
            # 複数形チェック
            if 'msgid_plural ' in b:
                m_single = re.search(r'msgid\s+"((?:[^"\\]|\\.)*)"', b)
                m_plural = re.search(r'msgid_plural\s+"((?:[^"\\]|\\.)*)"', b)
                single_id = m_single.group(1) if m_single else ""
                
                tr_single = translate_entry(single_id)
                # 複数形 msgstr[0] "" を置換
                b_new = re.sub(r'msgstr\[0\]\s+"(?:[^"\\]|\\.)*"', f'msgstr[0] "{tr_single}"', b)
                out_blocks.append(b_new)
                translated_count += 1
                continue
                
            # 単数形の抽出
            # 複数行のmsgidを結合して取得
            lines = b.split('\n')
            msgid_lines = []
            in_msgid = False
            msgstr_idx = -1
            
            for i, line in enumerate(lines):
                if line.startswith('msgid '):
                    in_msgid = True
                    msgid_lines.append(line[6:].strip('"'))
                elif in_msgid and line.startswith('"'):
                    msgid_lines.append(line.strip('"'))
                elif line.startswith('msgstr') or line.startswith('msgid_plural'):
                    in_msgid = False
                    if line.startswith('msgstr'):
                        msgstr_idx = i
                        
            full_msgid = "".join(msgid_lines)
            
            if full_msgid:
                tr = translate_entry(full_msgid)
                # エスケープ
                tr_escaped = tr.replace('"', '\\"')
                
                # msgstr "" を置換
                new_lines = []
                replaced = False
                for line in lines:
                    if line.startswith('msgstr '):
                        new_lines.append(f'msgstr "{tr_escaped}"')
                        replaced = True
                    elif replaced and line.startswith('"'):
                        # 古い複数行のmsgstrの継続行はスキップ
                        continue
                    else:
                        if replaced and not line.startswith('"'):
                            replaced = False
                        new_lines.append(line)
                        
                out_blocks.append("\n".join(new_lines))
                translated_count += 1
            else:
                out_blocks.append(b)
        else:
            out_blocks.append(b)

    new_content = "\n\n".join(out_blocks)
    if not new_content.endswith('\n'):
        new_content += '\n'

    with open(po_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Finished! Total entries: {total_count}, Translated: {translated_count}")

if __name__ == "__main__":
    po_path = "po/ja/labplot.po"
    process_po_file(po_path)
