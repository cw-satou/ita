from itemregistauth import app, db
from itemregistauth.mst_item import mstItem
from itemregistauth.mst_account import mstAccount

# Flaskアプリのコンテキスト内でデータベースを操作
with app.app_context():

    # 既存のテーブル（items, account）を削除
    db.drop_all()   

    # 新しくテーブルを作成
    db.create_all()

    # 商品データの登録
    initial_items = [
        mstItem(name='みかん', price=100),
        mstItem(name='りんご', price=120),
    ]

    # アカウントデータの登録
    initial_accounts = [
        mstAccount(user_id='sato', password='pass001'),
        mstAccount(user_id='suzuki', password='pass002'),
        mstAccount(user_id='tanaka', password='pass003'),
    ]

    # 商品データをデータベースに一括登録
    db.session.bulk_save_objects(initial_items)

    # アカウントデータをデータベースに一括登録
    db.session.bulk_save_objects(initial_accounts)

    # データの変更を確定（コミット）
    db.session.commit()

    # 初期化完了メッセージを出力
    print('Database initialized.')
