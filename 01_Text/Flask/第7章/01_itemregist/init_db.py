from itemregist import app, db
from itemregist.mst_item import mstItem

# アプリケーションのコンテキスト内でデータベース操作を実行
with app.app_context():
    # 既存の `items` テーブルを削除（初期化するため）
    db.drop_all()

    # 新しく `items` テーブルを作成
    db.create_all()

    # 初期化完了のメッセージを出力
    print('Database initialized.')
