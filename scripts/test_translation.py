# -*- coding: utf-8 -*-
"""
LabPlot POファイル全4,604項目の完全日本語化スクリプト
"""

import re
import os
import sys

# 翻訳辞書
DICTIONARY = {
    # 頻出語・動詞
    "Add": "追加",
    "Append": "追加",
    "Apply": "適用",
    "Calculate": "計算",
    "Cancel": "キャンセル",
    "Change": "変更",
    "Clear": "クリア",
    "Close": "閉じる",
    "Configure": "設定",
    "Copy": "コピー",
    "Create": "作成",
    "Cut": "切り取り",
    "Delete": "削除",
    "Deselect": "選択解除",
    "Duplicate": "複製",
    "Edit": "編集",
    "Execute": "実行",
    "Export": "エクスポート",
    "Extract": "抽出",
    "Filter": "フィルター",
    "Find": "検索",
    "Fit": "フィット",
    "Generate": "生成",
    "Help": "ヘルプ",
    "Hide": "非表示",
    "Import": "インポート",
    "Insert": "挿入",
    "Load": "読み込み",
    "Lock": "ロック",
    "Manipulate": "操作",
    "Mask": "マスク",
    "Move": "移動",
    "Open": "開く",
    "Paste": "貼り付け",
    "Pause": "一時停止",
    "Plot": "プロット",
    "Print": "印刷",
    "Quit": "終了",
    "Redo": "やり直す",
    "Refresh": "更新",
    "Reload": "再読み込み",
    "Remove": "削除",
    "Rename": "名前の変更",
    "Replace": "置換",
    "Reset": "リセット",
    "Save": "保存",
    "Search": "検索",
    "Select": "選択",
    "Set": "設定",
    "Shift": "シフト",
    "Show": "表示",
    "Smooth": "平滑化",
    "Sort": "並べ替え",
    "Split": "分割",
    "Start": "開始",
    "Stop": "停止",
    "Transform": "変換",
    "Undo": "元に戻す",
    "Unlock": "ロック解除",
    "Unmask": "マスク解除",
    "Update": "更新",
    "View": "表示",
    "Zoom": "ズーム",

    # 名詞・概念
    "Action": "アクション",
    "Algorithm": "アルゴリズム",
    "Alignment": "配置",
    "All": "すべて",
    "Amplitude": "振幅",
    "Analysis": "解析",
    "Angle": "角度",
    "Appearance": "外観",
    "Application": "アプリケーション",
    "Area": "面積",
    "Aspect": "要素 (アスペクト)",
    "Aspect Ratio": "アスペクト比",
    "Axes": "座標軸",
    "Axis": "軸",
    "Background": "背景",
    "Baseline": "ベースライン",
    "Border": "境界線",
    "Box": "ボックス",
    "Canvas": "キャンバス",
    "Cartesian": "直交座標",
    "Center": "中央",
    "Channel": "チャンネル",
    "Color": "色",
    "Color Map": "カラーマップ",
    "Column": "列",
    "Columns": "列",
    "Comment": "コメント",
    "Component": "コンポーネント",
    "Condition": "条件",
    "Configuration": "設定",
    "Connection": "接続",
    "Constant": "定数",
    "Coordinate": "座標",
    "Count": "カウント (数)",
    "Curve": "曲線 (カーブ)",
    "Custom": "カスタム",
    "Data": "データ",
    "Database": "データベース",
    "Dataset": "データセット",
    "Date": "日付",
    "DateTime": "日時",
    "Default": "デフォルト",
    "Degree": "度",
    "Delimiter": "区切り文字",
    "Description": "説明",
    "Destination": "出力先",
    "Device": "デバイス",
    "Dimension": "次元",
    "Direction": "方向",
    "Directory": "ディレクトリ",
    "Distance": "距離",
    "Document": "ドキュメント",
    "Domain": "定義域",
    "Duration": "期間",
    "Element": "要素",
    "Error": "エラー",
    "Error Bar": "エラーバー",
    "Equation": "方程式",
    "Event": "イベント",
    "Example": "例",
    "Expression": "式",
    "Factor": "係数",
    "File": "ファイル",
    "Filename": "ファイル名",
    "Filter": "フィルター",
    "Fitting": "フィッティング",
    "Font": "フォント",
    "Format": "形式 (フォーマット)",
    "Formula": "数式",
    "Fourier": "フーリエ",
    "Frequency": "周波数",
    "Function": "関数",
    "Grid": "グリッド (目盛線)",
    "Header": "ヘッダー",
    "Height": "高さ",
    "Histogram": "ヒストグラム",
    "History": "履歴",
    "Image": "画像",
    "Index": "インデックス",
    "Information": "情報",
    "Input": "入力",
    "Integration": "積分",
    "Intensity": "強度",
    "Interval": "区間",
    "Iteration": "反復回数",
    "Label": "ラベル",
    "Layout": "レイアウト",
    "Legend": "凡例",
    "Length": "長さ",
    "Level": "レベル",
    "Line": "線",
    "List": "リスト",
    "Logarithm": "対数",
    "Magnitude": "マグニチュード",
    "Margin": "余白",
    "Marker": "マーカー",
    "Mask": "マスク",
    "Matrix": "マトリクス",
    "Maximum": "最大値",
    "Mean": "平均値",
    "Median": "中央値",
    "Menu": "メニュー",
    "Message": "メッセージ",
    "Method": "手法",
    "Minimum": "最小値",
    "Mode": "モード",
    "Model": "モデル",
    "Name": "名前",
    "Network": "ネットワーク",
    "Noise": "ノイズ",
    "None": "なし",
    "Number": "数値",
    "Offset": "オフセット",
    "Operation": "操作",
    "Option": "オプション",
    "Order": "次数 / 順序",
    "Origin": "原点",
    "Output": "出力",
    "Package": "パッケージ",
    "Page": "ページ",
    "Parameter": "パラメータ",
    "Path": "パス",
    "Peak": "ピーク",
    "Pen": "ペン",
    "Period": "周期",
    "Phase": "位相",
    "Pixel": "ピクセル",
    "Plot": "プロット",
    "Point": "点",
    "Polynomial": "多項式",
    "Position": "位置",
    "Precision": "精度",
    "Prefix": "接頭辞",
    "Preset": "プリセット",
    "Preview": "プレビュー",
    "Process": "プロセス",
    "Project": "プロジェクト",
    "Property": "プロパティ",
    "Quality": "品質",
    "Range": "範囲",
    "Ratio": "比率",
    "Region": "領域",
    "Regression": "回帰",
    "Resolution": "解像度",
    "Result": "結果",
    "Root": "根 / ルート",
    "Rotation": "回転",
    "Row": "行",
    "Rows": "行",
    "Sample": "サンプル",
    "Scale": "スケール",
    "Script": "スクリプト",
    "Segment": "セグメント",
    "Selection": "選択範囲",
    "Separator": "区切り記号",
    "Series": "シリーズ (系列)",
    "Server": "サーバー",
    "Shape": "形状",
    "Shift": "シフト",
    "Signal": "信号",
    "Size": "サイズ",
    "Source": "ソース (音源/情報源)",
    "Spectrum": "スペクトル",
    "Speed": "速度",
    "Spreadsheet": "スプレッドシート",
    "Standard": "標準",
    "Standard Deviation": "標準偏差",
    "Statistics": "統計",
    "Status": "ステータス",
    "Step": "ステップ",
    "Style": "スタイル",
    "Suffix": "接尾辞",
    "Summary": "要約",
    "Surface": "曲面",
    "Symbol": "シンボル",
    "Table": "テーブル",
    "Target": "対象",
    "Template": "テンプレート",
    "Text": "テキスト",
    "Theme": "テーマ",
    "Thickness": "太さ",
    "Threshold": "しきい値",
    "Time": "時間",
    "Title": "タイトル",
    "Toolbar": "ツールバー",
    "Tooltip": "ツールチップ",
    "Total": "合計",
    "Trend": "トレンド",
    "Type": "種類",
    "Unit": "単位",
    "Value": "値",
    "Variable": "変数",
    "Variance": "分散",
    "Version": "バージョン",
    "Weight": "重み",
    "Width": "幅",
    "Window": "ウィンドウ",
    "Worksheet": "ワークシート",
    "Zero": "ゼロ",

    # 形容詞・状態
    "Active": "アクティブ",
    "Ascending": "昇順",
    "Automatic": "自動",
    "Available": "利用可能",
    "Bold": "太字",
    "Bottom": "下",
    "Busy": "処理中",
    "Cartesian": "直交",
    "Center": "中央",
    "Centered": "中央揃え",
    "Circular": "円形",
    "Classic": "クラシック",
    "Close": "近い",
    "Completed": "完了",
    "Constant": "一定",
    "Continuous": "連続",
    "Current": "現在の",
    "Custom": "カスタム",
    "Dark": "ダーク",
    "Descending": "降順",
    "Disabled": "無効",
    "Empty": "空",
    "Enabled": "有効",
    "Equal": "等しい",
    "Exact": "完全一致",
    "Exponential": "指数関数的",
    "False": "偽 (False)",
    "Fast": "高速",
    "First": "最初",
    "Fixed": "固定",
    "Flat": "フラット",
    "Full": "完全",
    "Global": "グローバル",
    "Horizontal": "水平",
    "Inactive": "非アクティブ",
    "Initial": "初期",
    "Invalid": "無効",
    "Inverse": "逆",
    "Italic": "斜体 (イタリック)",
    "Last": "最後",
    "Left": "左",
    "Light": "ライト",
    "Linear": "線形",
    "Local": "ローカル",
    "Logarithmic": "対数",
    "Manual": "手動",
    "Maximum": "最大",
    "Middle": "中央",
    "Minimum": "最小",
    "Missing": "欠損",
    "Next": "次へ",
    "Normal": "標準",
    "Numeric": "数値",
    "Open": "開いている",
    "Parallel": "平行",
    "Partial": "部分",
    "Perpendicular": "垂直",
    "Polar": "極座標",
    "Previous": "前へ",
    "Random": "ランダム",
    "Ready": "準備完了",
    "Relative": "相対",
    "Right": "右",
    "Scientific": "科学計算",
    "Selected": "選択中",
    "Simple": "シンプル",
    "Single": "単一",
    "Smooth": "平滑",
    "Solid": "実線",
    "Static": "静的",
    "Top": "上",
    "True": "真 (True)",
    "Uniform": "一様",
    "Unique": "一意",
    "Unknown": "不明",
    "Valid": "有効",
    "Vertical": "垂直",
    "Visible": "表示",
}

# 頻出プレースホルダー構文パターン
PATTERN_RULES = [
    (r"^Add (.*)$", lambda m: f"{translate_phrase(m.group(1))} を追加"),
    (r"^Remove (.*)$", lambda m: f"{translate_phrase(m.group(1))} を削除"),
    (r"^Delete (.*)$", lambda m: f"{translate_phrase(m.group(1))} を削除"),
    (r"^Insert (.*)$", lambda m: f"{translate_phrase(m.group(1))} を挿入"),
    (r"^Create (.*)$", lambda m: f"{translate_phrase(m.group(1))} を作成"),
    (r"^Select (.*)$", lambda m: f"{translate_phrase(m.group(1))} を選択"),
    (r"^Clear (.*)$", lambda m: f"{translate_phrase(m.group(1))} をクリア"),
    (r"^Show (.*)$", lambda m: f"{translate_phrase(m.group(1))} を表示"),
    (r"^Hide (.*)$", lambda m: f"{translate_phrase(m.group(1))} を非表示"),
    (r"^Enable (.*)$", lambda m: f"{translate_phrase(m.group(1))} を有効化"),
    (r"^Disable (.*)$", lambda m: f"{translate_phrase(m.group(1))} を無効化"),
    (r"^Export (.*)$", lambda m: f"{translate_phrase(m.group(1))} をエクスポート"),
    (r"^Import (.*)$", lambda m: f"{translate_phrase(m.group(1))} をインポート"),
    (r"^Load (.*)$", lambda m: f"{translate_phrase(m.group(1))} を読み込み"),
    (r"^Save (.*)$", lambda m: f"{translate_phrase(m.group(1))} を保存"),
    (r"^Plot (.*)$", lambda m: f"{translate_phrase(m.group(1))} をプロット"),
    (r"^(.*) Options$", lambda m: f"{translate_phrase(m.group(1))} のオプション"),
    (r"^(.*) Settings$", lambda m: f"{translate_phrase(m.group(1))} の設定"),
    (r"^(.*) Properties$", lambda m: f"{translate_phrase(m.group(1))} のプロパティ"),
    (r"^Properties of (.*)$", lambda m: f"{translate_phrase(m.group(1))} のプロパティ"),
    (r"^Number of (.*)$", lambda m: f"{translate_phrase(m.group(1))} の数"),
    (r"^(.*) failed$", lambda m: f"{translate_phrase(m.group(1))} に失敗しました"),
    (r"^Failed to (.*)$", lambda m: f"{translate_phrase(m.group(1))} に失敗しました"),
    (r"^Cannot (.*)$", lambda m: f"{translate_phrase(m.group(1))} できません"),
    (r"^Could not (.*)$", lambda m: f"{translate_phrase(m.group(1))} できませんでした"),
]

def translate_phrase(text):
    text = text.strip()
    if not text:
        return ""
    if text in DICTIONARY:
        return DICTIONARY[text]
    
    # 単語ごとの置換（複合語）
    words = text.split(" ")
    translated_words = []
    for w in words:
        if w in DICTIONARY:
            translated_words.append(DICTIONARY[w])
        else:
            translated_words.append(w)
    return " ".join(translated_words)

def translate_msgid(msgid):
    if not msgid:
        return ""
    
    # 1. プレースホルダーとHTMLタグの退避
    tokens = []
    def save_token(match):
        idx = len(tokens)
        tokens.append(match.group(0))
        return f"__TK{idx}__"
    
    # %1-%9, %s, %d, {0}, <tag> などを退避
    pattern = r'(%[0-9]+|%[sdg]|%[0-9]*\.[0-9]+[fge]|<[^>]+>|\{[0-9]+\})'
    masked = re.sub(pattern, save_token, msgid)
    
    # 2. アクセラレータ & の検出
    accel = None
    m_accel = re.search(r'&([A-Za-z0-9])', masked)
    if m_accel:
        accel = m_accel.group(1)
        masked = re.sub(r'&([A-Za-z0-9])', r'\1', masked)
    masked = masked.replace('&', '')
    
    # 3. 辞書引き
    translated = None
    from translate_po_core import EXACT_TRANSLATIONS, WORD_REPLACEMENTS
    if masked in EXACT_TRANSLATIONS:
        translated = EXACT_TRANSLATIONS[masked]
    elif masked in DICTIONARY:
        translated = DICTIONARY[masked]
    else:
        # パターンルール
        for pat, func in PATTERN_RULES:
            m = re.match(pat, masked, re.IGNORECASE)
            if m:
                try:
                    translated = func(m)
                    break
                except Exception:
                    pass
        
        if not translated:
            # フレーズ置換
            temp = masked
            for p, r in WORD_REPLACEMENTS:
                temp = re.sub(p, r, temp, flags=re.IGNORECASE)
            if temp != masked:
                translated = temp
            else:
                translated = translate_phrase(masked)

    # 4. アクセラレータの適用
    if accel and translated:
        if f"(&{accel})" not in translated and f"&{accel}" not in translated:
            translated = f"{translated}(&{accel})"
            
    # 5. トークンの復元
    for idx, orig in enumerate(tokens):
        translated = translated.replace(f"__TK{idx}__", orig)
        
    return translated

print("Testing translation:")
test_samples = [
    "&File", "Plot Data", "Analyze and Plot Data", "Set Column As",
    "Delete Selected Column(s)", "Insert Column Left", "Insert %1 Columns",
    "Properties of %1", "Failed to open file %1", "Linear Regression",
    "Peak Analysis", "Smooth", "Fourier Transform", "Sort Ascending"
]
for s in test_samples:
    print(f"  {s} -> {translate_msgid(s)}")
