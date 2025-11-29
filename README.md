<!-- generated-by:readmeai -->

# 概要

- Reactorパターンの実装サンプルプロジェクト
- 非同期I/Oをselectorsモジュールとカスタムイベントハンドラで実現するエコーサーバを例としている
- Reactorパターンについては、以下
    - [【Reactor】実装要件から選択するデザインパターン：「並行処理」「イベント処理」](https://qiita.com/OrangeJuice652/items/64a128e5b9449d13f0c3)

# ファイル一覧

| ファイル | 説明 |
|---|---|
| reactor.py | Reactorパターンのコアロジックを実装 |
| main.py | Reactorパターンのサンプル実行エントリポイント |
| eventhandler/i_event_handler.py | イベントハンドラのインターフェースを定義 |
| eventhandler/listener_socket.py | 新規接続を監視し、接続があったらEchoSocketを生成するイベントハンドラ |
| eventhandler/echo_socket.py | クライアントからのデータを受信し、同じデータを返送するイベントハンドラ |

# 使用方法

- Python 3.12以上が必要
- リポジトリをクローンしてディレクトリに移動する
    - `git clone git@github.com:OrangeJuice652/ReactorPatternSample.git`
    - `cd ReactorPatternSample`
- （任意）仮想環境を作成して有効化する
    - `python -m venv .venv`
    - `source .venv/bin/activate`
- 環境変数を設定する
    - `export SOCKET_HOST=localhost`
    - `export SOCKET_PORT=8888`
- サーバを起動する
    - `python main.py`
- クライアントから接続し、データを送信するとエコー応答が返ってくる
