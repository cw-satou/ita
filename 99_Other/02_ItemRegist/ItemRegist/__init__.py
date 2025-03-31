from flask import Flask
from ItemRegist.database import db  # データベース接続オブジェクトをインポート
import ItemRegist.models  # モデルを読み込み

# Flaskアプリケーションを生成する関数
def create_app():
    app = Flask(__name__)  # Flaskインスタンスを生成

    # アプリケーションの設定を読み込み
    app.config.from_object('ItemRegist.config.Config')  # Configクラスの設定を使用

    # データベースをアプリケーションに初期化
    db.init_app(app)  # アプリケーションをデータベースに関連付け

    return app  # アプリケーションオブジェクトを返す

# アプリケーションのインスタンスを生成
app = create_app()
