from itemdelete import app, db
from itemdelete.mst_item import mstItem

# アプリケーションのコンテキスト内でデータベース操作を実行
with app.app_context():
    # 既存の `items` テーブルを削除（初期化するため）
    db.drop_all()

    # 新しく `items` テーブルを作成
    db.create_all()

    # 商品データの登録（リスト形式で複数の商品をまとめて登録）
    initial_items = [
        mstItem(name='えんぴつ', price=100),
        mstItem(name='けしごむ', price=150),
        mstItem(name='色えんぴつ 赤', price=200),
    ]

    # データベースに商品データを一括で保存
    db.session.bulk_save_objects(initial_items)
    db.session.commit()  # 変更を確定

    # 初期化完了のメッセージを出力
    print('Database initialized.')
