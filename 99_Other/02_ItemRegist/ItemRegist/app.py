from ItemRegist.__init__ import app  # アプリケーションインスタンスをインポート
import ItemRegist.views  # ビュー（ルーティング）を定義したモジュールをインポート

# アプリケーションのエントリポイント
if __name__ == '__main__':
    # Flask開発サーバーを起動
    app.run()
