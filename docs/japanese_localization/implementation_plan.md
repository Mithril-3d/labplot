# 実装計画: LabPlot 日本語ローカライズ

## 1. 目的とスコープ
LabPlot の日本語翻訳辞書 `po/ja/labplot.po` に存在する 4,604 項目の未翻訳メッセージを一括で高品質な自然な日本語に翻訳し、日本語環境で直感的に操作できる状態にする。

## 2. 翻訳対象の分析
- **対象ファイル**: `po/ja/labplot.po` (約27,600行、全4,604エントリ)
- **現在の翻訳状況**:
  - 総項目数: 4,604 項目
  - 翻訳済み: 0 項目 (0.0%)
  - 未翻訳: 4,604 項目 (100.0%)
- **主要なカテゴリ**:
  1. メニューバー・ツールバー・コンテキストメニュー（例: File, Edit, Spreadsheet, Plot Data, Set Column As）
  2. スプレッドシート操作・列操作（例: Insert Column Left, Delete Selected Column(s), Sort Ascending）
  3. グラフ・ワークシート（例: Cartesian Plot, Curve, Axis, Legend, Title, Bar Plot, Histogram）
  4. データ解析・フィッティング（例: Linear Regression, Peak Analysis, Fourier Transform, Smooth, Differentiation）
  5. インポート・エクスポート（例: CSV, FITS, HDF5, NetCDF, MQTT, Serial Port）
  6. ダイアログ・設定・エラーメッセージ

## 3. 実装アプローチ

### 3.1 記号・構文保護の原則
GNU gettext / Qt i18n のルールに厳密に準拠し、以下の要素を絶対に破損させない：
- **引数プレースホルダー**: `%1`, `%2`, `%3` 等の位置・形式を維持。
- **ショートカット用アクセラレータ**: `&File` → `ファイル(&F)` のように、英語キーを残しつつ括弧書きで付与、または適切に引き継ぐ。
- **リッチテキスト・HTMLタグ**: `<b>`, `<i>`, `<code>`, `<br/>`, `<p>` 等をそのまま維持。
- **エスケープシーケンス**: `\n`, `\t`, `\"` の正確な保持。
- **gettext複数形（Plural-Forms）**: 日本語は `nplurals=1; plural=0;` のため単一の `msgstr[0]` 形式に従う。

### 3.2 用語統一基準（KDE / 科学データ解析準拠）
- **Spreadsheet**: スプレッドシート
- **Worksheet**: ワークシート
- **Matrix**: 行列 / マトリクス
- **Plot**: プロット / 描画
- **Column / Row**: 列 / 行
- **Fit / Fitting**: フィッティング / 適合
- **Peak Analysis**: ピーク解析
- **Baseline**: ベースライン
- **Smooth**: 平滑化 / スムージング
- **Fourier Transform**: フーリエ変換
- **Ascending / Descending**: 昇順 / 降順
- **Mask / Unmask**: マスク / マスク解除

### 3.3 翻訳実行メカニズム
Pythonスクリプトを用いて、専門用語・UI動詞・フレーズ辞書を構築し、文脈と文法に応じた正確な翻訳を全項目に適用。

## 4. 検証手順
1. **構文検証**: 生成した `labplot.po` のヘッダー、エスケープ、クォーテーションの構文エラーがないか確認。
2. **統計検証**: Pythonスクリプトで未翻訳項目（`msgstr ""`）が0件になっていることを確認。
3. **リモート反映**: フォーク先リポジトリ（origin master）にコミット・プッシュし、GitHub Actions でのビルド成立を確認。
