# テキストファイルの中のパターンを置換するプログラム

import os, sys

def edit_text():
    file_path = input("txtファイルのパスを入力してください> ")

    # ファイルが存在しないか、txtファイルでないときはプログラムを終了する。
    if not os.path.isfile(file_path):
        print("ファイルが存在しません。")
        sys.exit()
    elif not file_path.endswith('.txt'):
        print("txtファイルではありません。")
        sys.exit()

    # 置換したい文字列と置換後の文字列の入力を受ける。
    pattern_1 = input("変更したい文字列パターンを入力してください> ")
    pattern_2 = input("変更後の文字列パターンを入力してください> ")

    # ファイルを読み込んで、実際に置換を行う。
    with open(file_path, 'r') as f:
        text = f.read()

    text = text.replace(pattern_1, pattern_2)

    with open(file_path, 'w') as f:
        f.write(text)

if __name__ == '__main__':
    edit_text()