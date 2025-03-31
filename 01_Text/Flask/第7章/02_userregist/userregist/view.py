from flask import render_template, request, redirect
from userregist import app, db
from userregist.mst_user import mstUser

# 入力フォームを表示するルート
# ①処理を追加
# @app.route('/input', methods=['GET'])

# ユーザーデータを登録するルート
# ②処理を追加
# @app.route('/register', methods=['POST'])
# ユーザー（会員情報）をデータベースに登録する

# ③チャレンジ問題
# ユーザー情報一覧を表示する
# @app.route('/display', methods=['GET'])
# すべてのユーザー（会員情報）を取得する
