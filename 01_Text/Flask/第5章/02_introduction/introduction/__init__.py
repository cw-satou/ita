from flask import Flask

# Flaskアプリのインスタンスを作成
app = Flask(__name__)

# 設定ファイル（config.py）を読み込む
app.config.from_pyfile("../config.py")

# アプリケーションのルートURLを設定
# 例えば '/intro' に設定すると、すべてのルートが '/intro' から始まる
app.config['APPLICATION_ROOT'] = '/intro'

# 画面の処理（ビュー）を読み込む
from . import view
