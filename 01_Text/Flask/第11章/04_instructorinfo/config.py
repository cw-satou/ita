# デバッグモードを有効にする（エラーの詳細を表示）
DEBUG = True

# データベースの接続情報（PostgreSQL を使用）
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost:5432/sampledb'

# SQLAlchemy の変更監視機能を無効化（パフォーマンス向上のため）
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SQLクエリをログに出力するかどうか（開発時のデバッグ用）
SQLALCHEMY_ECHO = False  # True にすると実行される SQL がログに表示される

# Flaskアプリケーションのセッションで使用する秘密鍵（セッションの暗号化などに使用）
SECRET_KEY = 'secret key'
