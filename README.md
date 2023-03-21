# gi

## 目的

pythonを利用してScancodeMapのレジストリ編集を行う。

ScancodeMapとはスキャンコードレベルでキーの置換を行うレジストリであり、
ソフトの常駐など不要なことや、日本語語キーボードのCapsLockキーといった
特殊なキーの置換などが行える。

## 注意

- 実行には管理者権限が必要です
- 設定反映には再起動が必要です

## 利用法1 対話型モードについて

以下の流れで設定を行う

1. 設定ファイルを用意する
2. 管理者権限で起動する
3. 対話型で設定を行う
   1. 現状のレジストリの確認
   2. 現状のレジストリの保存
   3. 設定ファイルのロード
   4. 読み込んだレジストリの書き込み
   5. リセットを行うための削除

実行する場合は[y]を入力しEnterを押すことで進む。
[n]や無入力の場合は実行を行わない。

## 将来的な追加機能
- 対話モードでのキー指定による置換設定の追加
- オプション引数による引数モードの追加
- 引数モードでのキー指定の設定
