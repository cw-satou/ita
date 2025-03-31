from flask import Flask

# Flaskアプリのインスタンスを作成
app = Flask(__name__)

# 画面の処理（ビュー）を読み込む
from . import view
