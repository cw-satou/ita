from productorder import app, db
from productorder.mst_users2 import mstUsers2  # ユーザー情報を管理するテーブルのモデルをインポート

# Flaskアプリのコンテキスト内でデータベースを操作
with app.app_context():

    # 既存のテーブル（users2）を削除
    db.drop_all()

    # 新しくusers2テーブルを作成
    db.create_all()

    # ユーザーデータの登録（初期データ）
    initial_items = [
        mstUsers2(id='user01', name='Mike', password='12345', email='user01@example.com', phone='09000111111'),
        mstUsers2(id='user02', name='Kerry', password='67890', email='user02@example.com', phone='09000112222'),
        mstUsers2(id='user03', name='Ashly', password='12312', email='user03@example.com', phone='09000113333'),
    ]
    
    # ユーザーデータをデータベースに一括登録
    db.session.bulk_save_objects(initial_items)

    # データの変更を確定（コミット）
    db.session.commit()

    # 初期化完了メッセージを出力
    print('Database initialized.')
