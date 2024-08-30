# Bocco-emo

## 環境構築

1. ルート配下に`.env` fileを作成する

2. `.env` file内に以下を追加する (hoge内には任意のキーやトークンを入れる)

    ``` zsh
    REFRESH_TOKEN=hoge
    OPENAI_API_KEY=hoge
    ```

3. ターミナル内で以下のコマンドを動かす
    - Mac, Linux

    ``` zsh
    python3 -m venv .venv
    . .venv/bin/activate
    ```

    - Windows

    ``` powershell
    python -m venv .venv
    .venv\Scripts\activate
    ```

4. [ngrok](https://ngrok.com/)の設定をする
   1. 上のリンクにアクセスしてSign Upをする（無料）
   2. インストールする
      - Mac

       ``` zsh
       brew install ngrok/ngrok/ngrok
       ngrok config add-authtoken $TOKEN    # Dashboardのsetupのところにあるコマンドをそのままコピーする
       ```

       - Windows

        ``` powershell
        choco install ngrok    # chocoがなければFileを直接ダウンロードする
        ngrok config add-authtoken $TOKEN    # Dashboardのsetupのところにあるコマンドをそのままコピーする
        ```

5. 必要なパッケージをインストールする

   ``` zsh
   pip install -r requirements.txt
   ```

6. ngrokでサーバーを立ち上げる

   ``` zsh
   ngrok http http://localhost:8080
   ```

7. `main.py`を動かす

   ``` zsh
   python main.py
   ```

    > [!WARNING]
    > WebhookのURLがFowardingしているURLに設定できているかチェック！

## 開発手順

### Boccoの機能周り

1. 使用する機能に関わるAPIをBoccoの開発ドキュメントから確認
2. エンドポイントとヘッダー、データ（POST/PUT）を確認
3. `api_query.py`で必要な変数周りの確認
4. `bocco_tools.py`に実装
5. `main.py`で導入して動作確認
