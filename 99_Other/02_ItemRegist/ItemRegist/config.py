import os  # osモジュールをインポート（環境変数やファイル操作に利用）

# 開発環境用の設定クラス
class DevelopmentConfig:
    # デバッグモードを有効にする（開発時にエラーの詳細を表示）
    DEBUG = True

    # SQLAlchemyでPostgreSQLデータベースへの接続設定を記述
    # フォーマット: 'postgresql+psycopg2://ユーザー名:パスワード@ホスト名:ポート/データベース名'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost:5432/sampledb'
    
    # SQLAlchemyがモデルの変更をトラッキングしないようにする設定（パフォーマンス向上）
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SQLAlchemyのSQL文をコンソールに表示するかどうか（Trueなら表示）
    SQLALCHEMY_ECHO = False

    # Flaskアプリケーションのセッションで使用する秘密鍵（セッションの暗号化などに使用）
    SECRET_KEY = 'ItemRegist'

# 開発環境設定をConfigという名前でエクスポート
Config = DevelopmentConfig
