import winreg
import ctypes
import sys
import json

class WindowsScancodeMapClass():
    # コンストラクタ
    def __init__(self,):
        self.file_format_version = '4'
        self.key_path = r'SYSTEM\CurrentControlSet\Control\Keyboard Layout'
        self.key_name = 'Scancode Map'
        self.defolt_file_path = 'windows_scancode_map.json'
        self.hold_key_value = []
        pass

    # 
    def check_Administrator_authority(self) -> bool:
        '''
        管理者権限の確認
        '''
        self.is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        if self.is_admin == 1:
            print('管理者権限が確認できました')
            return True
        else:
            print('管理者権限が確認できませんでした')
            print('プログラムを終了します')
            input('press any key')
            sys.exit()


    def reg_QueryValue(self) -> bool:
        '''
        対象レジストリの読み出し
        '''
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, self.key_path) as key:
            try:
                byte_hold_key_value, _ = winreg.QueryValueEx(key, self.key_name)
                self.hold_key_value = list(byte_hold_key_value)
            except Exception as e:
                print('レジストリが存在しませんでした')
                return False
            else:
                print('レジストリが存在します')
                print(self.hold_key_value)
                return True


    def reg_SetValue(self, key_value=None) -> bool:
        '''
        対象レジストリに対する書き込み
        '''
        if key_value is None:
            key_value =  self.hold_key_value
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, self.key_path, access=winreg.KEY_SET_VALUE) as key:
            try:
                winreg.SetValueEx(key, self.key_name, 0, winreg.REG_BINARY, bytes(key_value))
            except Exception as e:
                print('書き込みに失敗しました')
                print('エラー:',e)
                return False
            else:
                print('書き込みに成功しました')
                return True


    def reg_DeleteValue(self) -> bool:
        '''
        対象レジストリの値の削除
        '''
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, self.key_path, access=winreg.KEY_SET_VALUE) as key:
            try:
                winreg.DeleteValue(key, self.key_name)
            except Exception as e:
                print('削除に失敗しました')
                print('エラー:',e)
                return False
            else:
                print('削除に成功しました')
                return True

    def seav_Value(self, file_path=None):
        '''
        レジストリの設定ファイルへの保存
        '''
        # デフォルト引数処理
        if file_path is None:
            file_path = self.defolt_file_path
        try:
            if (self.reg_QueryValue()):
                json_data = {'file':'windows_scancode_map',
                    'file_format_version':self.file_format_version,
                    'key_path':self.key_path,
                    'key_name':self.key_name,
                    'key_value':self.hold_key_value}

                with open(file_path, mode='w', encoding='utf-8') as f:
                    json.dump(json_data, f, indent=4, ensure_ascii=False)
            else:
                raise ValueError("QueryValue error")
        except Exception as e:
            print('保存に失敗しました')
            print('エラー:',e)
            return False
        else:
            print('保存に成功しました')
            return True

    def load_value(self, file_path=None):
        '''
        保存されたレジストリ設定ファイルのロード
        '''
        # デフォルト引数処理
        if file_path is None:
            file_path = self.defolt_file_path
        try:
            # jsonファイルをロード
            with open(file_path, mode='r', encoding='utf-8') as f:
                data = json.load(f)

            # 種別とバージョンが合致するか確認
            if (data.get('file') != 'windows_scancode_map' or data.get('file_format_version') != self.file_format_version):
                print('format error')
                return False

            self.key_path = data.get('key_path')
            self.key_name = data.get('key_name')
            self.hold_key_value =data.get('key_value')

        except Exception as e:
            print('ロードに失敗しました')
            print('エラー:',e)
            return False
        else:
            print('ロードに成功しました')
            return True


if __name__ == "__main__":
    pass




# 実行ファイル化
# pyinstaller .py --onefile


