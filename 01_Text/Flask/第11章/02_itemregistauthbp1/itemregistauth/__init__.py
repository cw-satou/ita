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

# 認証機能（auth）を担当するBlueprintをインポート
from .blueprints.auth import auth_bp

# 商品関連の機能（items）を担当するBlueprintをインポート
from .blueprints.items import items_bp

# 認証用のBlueprintをアプリケーションに登録（URLの先頭が '/auth' になる）
app.register_blueprint(auth_bp, url_prefix='/auth')

# 商品管理用のBlueprintをアプリケーションに登録（URLの先頭が '/items' になる）
app.register_blueprint(items_bp, url_prefix='/items')
