# ■1.概要

## (1)目的

フォルダ内の画像ファイル(pngもしくはjpeg)をフォルダアイコン用の拡張子icoファイルに変換。

## (2)動作環境

- Windows11
- Python 3.12.x
- Pillowがインストールされていること

# ■2.使用方法

(1)ico.pyがあるフォルダで以下のコマンドを実行。

他のフォルダから実行する場合は、ico.pyが格納されているフォルダのフルパスを指定。

```jsx
python ico.py
```

(2)コマンド実行後に対話が始まるため、変換対象のファイルが格納されているフォルダのフルパスを入力。

```jsx
画像が含まれるディレクトリのパスを入力してください: <変換対象ファイルが格納されているフォルダのフルパス>

#結果
<元のファイル名.png(もしくはjpg)> を <ファイル名>.ico に変換しました。
```