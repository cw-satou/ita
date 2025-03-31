from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flaskアプリのインスタンスを作成
app = Flask(__name__)

# 設定ファイル（config.py）を読み込む
app.config.from_pyfile("../config.py")

# データベース操作用のSQLAlchemyオブジェクトを作成
db = SQLAlchemy()

# アプリケーションとデータベースを連携
db.init_app(app)

# 画面の処理（ビュー）を読み込む
from . import view
