from itemregistauth import app, db
from itemregistauth.auth.models.mst_accounts import Mst_account
from itemregistauth.items.models.mst_items import Mst_items

# アプリケーションのコンテキスト内でデータベースを操作
with app.app_context():

    # すべてのテーブルを削除
    db.drop_all()

    # データベースの全テーブルを作成
    db.create_all()

    # 商品データを登録
    initial_items = [
        Mst_items(name='みかん', price=100),  # 商品「みかん」を登録
        Mst_items(name='りんご', price=120),  # 商品「りんご」を登録
    ]
    db.session.bulk_save_objects(initial_items)  # 一括保存

    # アカウントデータを登録
    initial_accounts = [
        Mst_account(user_id='sato', password='pass001'),   # アカウント「sato」を登録
        Mst_account(user_id='suzuki', password='pass002'), # アカウント「suzuki」を登録
        Mst_account(user_id='tanaka', password='pass003'), # アカウント「tanaka」を登録
    ]
    db.session.bulk_save_objects(initial_accounts)  # 一括保存

    # データベースに変更を反映
    db.session.commit()

    # 初期化完了メッセージを出力
    print("Database initialized.")
