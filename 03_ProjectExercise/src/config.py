# デバッグモードの設定
# True: 有効、False: 無効
DEBUG = True

# PostgreSQLデータベース接続のベースURI（データベース作成用）
SQLALCHEMY_DATABASE_BASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost:5432'

# PostgreSQLデータベース接続のベースURI
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost:5432/roomecho'

# アプリケーションの秘密鍵
SECRET_KEY = 'secretkey'
