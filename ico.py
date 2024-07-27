import os
from PIL import Image

def convert_to_ico(directory):
    # 指定されたディレクトリ内のすべてのファイルをループ
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # 画像ファイルのフルパスを取得
            file_path = os.path.join(directory, filename)
            
            # 画像を開く
            with Image.open(file_path) as img:
                # ICOファイル名を作成（元のファイル名 + .ico）
                ico_filename = os.path.splitext(filename)[0] + '.ico'
                ico_path = os.path.join(directory, ico_filename)
                
                # 画像をリサイズ（必要な場合）
                img.thumbnail((256, 256))  # ICOの最大サイズは通常256x256
                
                # ICOとして保存
                img.save(ico_path, format='ICO')
                print(f'{filename} を {ico_filename} に変換しました。')

# スクリプトを実行
if __name__ == "__main__":
    # 変換したい画像があるディレクトリのパスを入力してください
    directory_path = input("画像が含まれるディレクトリのパスを入力してください: ")
    convert_to_ico(directory_path)