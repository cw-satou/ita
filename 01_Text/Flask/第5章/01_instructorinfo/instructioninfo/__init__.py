from flask import Flask

# Flaskアプリのインスタンスを作成
app = Flask(__name__)

# 設定ファイル（config.py）を読み込む
app.config.from_pyfile("../config.py")

from . import view  # ビュー（画面処理）を読み込む

# アプリの設定情報として、INSTRUCTORS と FIELDS を空のリストで初期化
app.config['INSTRUCTORS'] = []
app.config['FIELDS'] = []
