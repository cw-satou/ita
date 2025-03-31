from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# 設定ファイル（config.py）を読み込む
# これにはデータベース接続情報やアプリの設定が含まれる
app.config.from_pyfile("../config.py")

# SQLAlchemyのインスタンスを作成（データベース操作用）
db = SQLAlchemy()

# アプリケーションとSQLAlchemyを連携
db.init_app(app)

# 認証機能（auth）を担当するBlueprintをインポート
from .auth import auth_bp

# 商品管理機能（items）を担当するBlueprintをインポート
from .items import items_bp

# 認証用のBlueprintをアプリケーションに登録
# URLの先頭が '/auth' になる
app.register_blueprint(auth_bp, url_prefix='/auth')

# 商品管理用のBlueprintをアプリケーションに登録
# URLの先頭が '/items' になる
app.register_blueprint(items_bp, url_prefix='/items')
