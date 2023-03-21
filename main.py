from windows_scancode_map import WindowsScancodeMapClass
import sys
import argparse


def interactive_windows_scancode_map():
    # インスタンス化
    interactive = WindowsScancodeMapClass()

    # 管理者権限の確認
    print('本プログラムは管理者権限が必要です')
    print('権限がある確認します')
    interactive.check_Administrator_authority()
    print('========================================')

    # レジストリの確認
    exist_value = False
    print('以下のレジストリが設定されているか確認しますか? y/n(Enterでキャンセル)')
    print('key_path:', interactive.key_path)
    print('key_name:', interactive.key_name)
    control = input()
    if control == 'y':
       exist_value = interactive.reg_QueryValue()
    print('========================================')

    # レジストリ値の保存
    if (exist_value == True):
        print('レジストリを設定ファイルに保存しますか? y/n(Enterでキャンセル)')
        control = input()
        if control == 'y':
            interactive.seav_Value()
        print('========================================')

    # ロード
    print('設定ファイルをロードしますか? y/n (Enterでキャンセル)')
    control = input()
    if control == 'y':
        interactive.load_value()
    print('========================================')

    # 書き込み
    if (interactive.hold_key_value):
        print('以下の内容でレジストリに値を上書き書き込みしますか? y/n (Enterでキャンセル)')
        print('key_path:', interactive.key_path)
        print('key_name:', interactive.key_name)
        print('key_data:', interactive.hold_key_value)
        control = input()
        if control == 'y':
            interactive.reg_SetValue()
        print('========================================')

    print('以下のレジストリを削除して初期状態に戻しますか? y/n(Enterでキャンセル)')
    print('key_path:', interactive.key_path)
    print('key_name:', interactive.key_name)
    control = input()
    if control == 'y':
        interactive.reg_DeleteValue()
    print('========================================')

    print('終了です')
    print('設定変更を有効化するにはWindowsを再起動してください')

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.parse_args()


    # 対話型のスキャンコード変更ユーティリティを呼び出す
    interactive_windows_scancode_map()
    # sys.exit()


# 実行ファイル化
# pyinstaller CapsLock_change.py --onefile
