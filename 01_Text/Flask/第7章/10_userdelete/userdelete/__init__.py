from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flaskアプリのインスタンスを作成
app = Flask(__name__)

# 設定を外部ファイルから読み込む
app.config.from_pyfile('../config.py')

# SQLAlchemyのインスタンスを作成
db = SQLAlchemy()

# データベースのモデル定義を読み込み
import userdelete.mst_user

# SQLAlchemyとFlaskアプリケーションの紐付け
db.init_app(app)

# 画面の処理（ビュー）を読み込む
import userdelete.view