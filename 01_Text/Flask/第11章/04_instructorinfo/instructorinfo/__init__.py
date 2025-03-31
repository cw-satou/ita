from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# 設定ファイル（config.py）を読み込む
# これにはデータベース接続情報などが含まれる
app.config.from_pyfile("../config.py")

# SQLAlchemyのインスタンスを作成（データベース操作用）
db = SQLAlchemy()

# アプリケーションとSQLAlchemyを連携
db.init_app(app)

# ルート処理（view）をインポート
from . import view

# データベースモデル（models）をインポート
from . import models
