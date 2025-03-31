from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# アプリケーションの設定を外部ファイルから読み込む
# "../config.py" にはデータベースの接続情報やその他の設定が記載されている
app.config.from_pyfile("../config.py")

# SQLAlchemyのインスタンスを作成
db = SQLAlchemy()

# Flaskアプリケーションとデータベースを関連付け
db.init_app(app)

# 認証機能（auth）を担当するBlueprintをインポート
from .blueprints.auth import auth_bp

# 講師管理機能（instructors）を担当するBlueprintをインポート
from .blueprints.instructors import instructors_bp

# 認証用のBlueprintをアプリケーションに登録
# '/auth' をURLの先頭部分として使用
app.register_blueprint(auth_bp, url_prefix='/auth')

# 講師管理用のBlueprintをアプリケーションに登録
# '/instructors' をURLの先頭部分として使用
app.register_blueprint(instructors_bp, url_prefix='/instructors')
