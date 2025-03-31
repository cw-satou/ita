from flask import render_template, request,session
from rockpaperscissor import app
import random

# @app.route('/start', methods=['GET'])
# def start():
    # セッション情報を削除
    # 結果をセッションに初期値として記録
    # game.htmlを初期表示

# @app.route('/play', methods=['POST'])
# def play():
    # フォームから送信されたデータを取得
    # 勝敗を決める
    # セッションに格納されたじゃんけんの結果を更新
    # game.htmlを勝敗結果として表示

# @app.route('/finish', methods=['POST'])
# def finish():
    # セッションから勝敗情報を取得する
    # セッション情報を削除
    # セッションから取得した情報でresult.htmlを表示
