from userregist import app, db
from userregist.mst_user import mstUser

with app.app_context():

    # 既存の `users` テーブルを削除（初期化するため）
    db.drop_all()
    
    # 新しく `users` テーブルを作成
    db.create_all()

    # 初期データをデータベースに追加
    initial_users = [
        mstUser(name='仮名田 美羽', email='testA@exsample.com', phone='09000011111'),
    ]
    db.session.bulk_save_objects(initial_users)  # 初期データを一括登録
    db.session.commit()  # データベースに変更を反映

    print('Database initialized.')  # 初期化完了メッセージを出力
