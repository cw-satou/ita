from ItemRegist.__init__ import create_app
from ItemRegist.database import db

# Flaskアプリケーションを生成
app = create_app()

# アプリケーションのコンテキスト内で操作を実行
with app.app_context():
    # データベース内にモデルに基づくテーブルを作成
    db.create_all()
    
    # サンプルデータの登録などは行わず、初期化メッセージを表示
    print("Database initialized.")