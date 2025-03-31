from flask import render_template, request
from deliverycalculator import app

# '/input' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/input', methods=['GET'])
def input():
    # 配送料金計算の入力フォームを表示する処理を記載する
    return

# '/calculate' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/calculate', methods=['POST'])
def calculate():
    # フォームから受け取ったデータを元に、配送料金を計算する処理を記載する
    return

# 料金計算メソッド
def price_calc(form):
    # フォームのデータを取得し、適切な型に変換
    length = int(form['length'])  # 荷物の長さ（cm）
    width = int(form['width'])  # 荷物の幅（cm）
    height = int(form['height'])  # 荷物の高さ（cm）
    weight = float(form['weight'])  # 荷物の重さ（kg）

    # クーポンの有無を判定（'true'の場合は適用）
    if form['coupon'] == 'true':
        coupon = True
    else:
        coupon = False

    # 料金を計算し、priceに格納する
    # 例えば、規定サイズ外（大きすぎる荷物）の場合は -1 を返す処理を追加予定

    price = 0  # 料金の計算ロジックをここに実装する
    return price  # 計算された料金を返す
