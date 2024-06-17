# Bocco-emo開発(雑談)

## 環境構築

1. ルート配下に`.env` fileを作成する
2. `.env` file内に以下を追加する (hoge内には任意のキーやトークンを入れる)

    ``` zsh
    REFRESH_TOKEN=hoge
    OPEN_AI_KEY=hoge
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

4. 必要なパッケージをインストールする

   ``` zsh
   pip install -r require.txt
   ```

5. `main.py`を動かす

   ``` zsh
   python main.py
   ```
