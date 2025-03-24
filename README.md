プロジェクトの内容を分析し、適切な README.md を作成します。



# Markdown Translation Tool

このツールは英語のMarkdownファイルを日本語に変換するためのPythonスクリプトセットです。

## 概要

このプロジェクトは以下の機能を提供します：

1. 英語のMarkdownファイルから翻訳用のベースCSVファイルを作成
2. 翻訳済みのCSVファイルを使用して、英語のMarkdownを日本語に変換

## ファイル構成

- `base_csv_creator.py`: 英語のMarkdownファイルから翻訳用ベースCSVを作成
- `main.py`: 翻訳済みCSVを使用して日本語版Markdownを生成
- `chap23_en.md`: 翻訳対象の英語Markdownファイル
- `base_csv.csv`: 生成される翻訳用ベースCSVファイル
- `translations.csv`: 実際の翻訳データを含むCSVファイル（手動で編集）
- `chap23_ja.md`: 生成される日本語版Markdownファイル

## 使用方法

### 1. 翻訳用CSVの作成

```bash
python base_csv_creator.py
```

このコマンドは `chap23_en.md` を読み込み、以下の形式で `base_csv.csv` を生成します：
```
english,japanese
line1,line1
line2,line2
```

### 2. 翻訳データの準備

1. 生成された `base_csv.csv` を `translations.csv` としてコピー
2. `translations.csv` の `japanese` 列に適切な日本語訳を入力

### 3. 日本語版Markdownの生成

```bash
python main.py
```

このコマンドは `translations.csv` の翻訳データを使用して `chap23_ja.md` を生成します。

## 特徴

- 空行は自動的にスキップされます
- 最長マッチングを採用し、部分一致による誤訳を防止します
- UTF-8エンコーディングを使用し、日本語を適切に処理します
- 変換処理中にスキップされた行は報告されます

## 注意事項

- 翻訳前に必ず `translations.csv` の内容を確認してください
- Markdown形式は保持されますが、画像パスなどは必要に応じて手動で調整してください
- 変換結果は必ず目視で確認することを推奨します

## 動作要件

- Python 3.x
- 標準ライブラリのみを使用（追加のパッケージは不要）
- PyPDF2 (PDFファイル処理が必要な場合)

### PyPDF2のインストール

```bash
pip install PyPDF2
```

PyPDF2は、PDF処理が必要な場合にのみインストールしてください。