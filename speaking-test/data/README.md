# dataディレクトリ

* クイズのデータをまとめておくディレクトリです
* データ構造は以下のとおりです

    ``` json
    {
      "id": "2",
      "category": 1,
      "quiz": "What is your favorite artist?",
      "time": 15,
      "thinking": 5,
      "image": {
        "path": "2.png",
        "width": 600,
        "height": 450
      },
      "next": "explanation"
    }
    ```

  * id(string): 問題のIDです。とりあえず1から順に振ってください。
  * category(number): 問題が大問のどれに属するかを書きます。
  * quiz(string): 問題を書きます。
  * time(number): 制限時間を書きます。
  * thinking(任意, number): 考える時間を設けるときにその制限時間を書きます。
  * image(任意):
    * path(string): 写真のファイル名を書きます。（ファイルは`/public/images`に入れてください）
    * width(number): 写真の横幅を書きます(単位：px)
    * height(number): 写真の縦幅を書きます(単位：px)
  * next(string): 次のパスを書きます
    * 数字のみ: 次に考える時間がない場合のパス
    * 数字/thinking: 次に考える時間がある場合のパス
    * `explanation`: 次が説明画面の場合
    * `complete`:次が終了画面の場合
