# Bocco-emo

## 環境構築

1. リポジトリをクローンする

    ``` zsh
    git clone https://github.com/social-robotics-lab/bocco-emo.git
    ```

2. ルート配下に`.env` fileを作成する
3. `.env` file内に以下を追加する (hoge内には任意のキーやトークンを入れる)

    ``` zsh
    REFRESH_TOKEN=hoge
    OPENAI_API_KEY=hoge
    ```

4. ターミナル内で以下のコマンドを動かす
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

5. 必要なパッケージをインストールする

   ``` zsh
   pip install -r requirements.txt
   ```

6. `main.py`を動かす

   ``` zsh
   python main.py
   ```
