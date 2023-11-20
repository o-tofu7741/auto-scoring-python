# auto-scoring-python
manaba上で提出されたjava,jarファイルの内容と実行結果を1つにまとめるツール

## 使い方
1. 対象のフォルダ構造が、下記のような、全体フォルダ/学生フォルダ/課題ファイルの構成の時に利用可能
```
report01-hoge-huga   //全体フォルダ
    |-0001           //学生フォルダ
    |    |-a.java    //課題ファイル
    |    |-b.jar
    |
    |-0002...
```
2. 対象の全体フォルダに下記の形式のsettigns.jsonを配置
```
settings.json
{
  "tasks": [
    {
      "name": "a.java"
      "input": "aaaa"   //標準入力がある場合は指定
    },
    {
      "name": "b.jar"
      "args": "bbbbb"  //実行時引数がある場合は記載
    },...
}
```
| キー名(変更不可) | 値 |
|---| --- |
|tasks| 課題を全て格納したリスト|
|name| 課題ファイル名|
|input|標準入力, 省略可|
|args|実行時引数, 省略可|
3. main.pyを実行し、settings.jsonのファイルが配置された全体フォルダを指定
4. result.txtが対象全体フォルダに置かれます
