# デバッグモードを有効にする設定
DEBUG = True

# アプリケーションのセッション管理や暗号化に使用する秘密鍵
SECRET_KEY = 'secret key'

# SQLAlchemyでPostgreSQLデータベースへの接続設定を記述
# フォーマット: 'postgresql+psycopg2://ユーザー名:パスワード@ホスト名:ポート/データベース名'
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost:5432/sampledb'
