from flask import Flask

# Flaskアプリのインスタンスを作成
app = Flask(__name__)

# 設定を外部ファイルから読み込む
app.config.from_pyfile('../config.py')

# 画面の処理（ビュー）を読み込む
import errorhandling.view