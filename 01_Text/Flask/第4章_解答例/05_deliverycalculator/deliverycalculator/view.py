from flask import render_template, request
from deliverycalculator import app

# '/input' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/input', methods=['GET'])
def input():
    # 料金計算用の入力フォームを表示
    return render_template('calculate.html')

# '/calculate' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/calculate', methods=['POST'])
def calculate():
    # 入力エラーがあるかを判定するフラグ
    errflg = False

    # フォームのデータを取得
    length = request.form['length'] # タテの入力値
    width = request.form['width']   # ヨコの入力値
    height = request.form['height'] # 高さの入力値
    weight = request.form['weight'] # 重量の入力値
    coupon = request.form.get('coupon') # クーポンの有無
    length_err = '' # タテのエラーメッセージ
    width_err = ''  # ヨコのエラーメッセージ
    height_err = '' # 高さのエラーメッセージ
    weight_err = '' # 重量のエラーメッセージ

    # 各入力値のバリデーション（未入力チェック）
    if not length:
        errflg = True
        length_err = 'タテは必須です'
    if not width:
        errflg = True
        width_err = 'ヨコは必須です'
    if not height:
        errflg = True
        height_err = '高さは必須です'
    if not weight:
        errflg = True
        weight_err = '重量は必須です'

    # 入力エラーがある場合、再度入力フォームを表示
    if errflg:
        return render_template(
            'calculate.html', 
            length=length, length_err=length_err, 
            width=width, width_err=width_err, 
            height=height, height_err=height_err, 
            weight=weight, weight_err=weight_err,
            coupon=coupon
        )

    # 料金を計算する関数を呼び出し
    price = price_calc(length, width, height, weight, coupon)

    # 計算結果を表示するテンプレートをレンダリング
    return render_template('calculate-result.html', price=price)

# 料金計算を行う関数
def price_calc(length, width, height, weight, coupon):
    # 文字列の入力値を数値（intまたはfloat）に変換
    length_int = int(length)   # タテの長さ
    width_int = int(width)     # ヨコの長さ
    height_int = int(height)   # 高さ
    weight_float = float(weight) # 重量
    use_coupon = False

    # クーポンの有無を判定（'true'ならクーポン適用）
    if coupon == 'true':
        _coupon = True

    # 荷物の合計サイズを計算（タテ＋ヨコ＋高さ）
    totalSize = length_int + width_int + height_int

    # 配送料金を決定
    if totalSize <= 60 and weight_float <= 1:
        price = 660
    elif totalSize <= 80 and weight_float <= 2:
        price = 880
    elif totalSize <= 100 and weight_float <= 5:
        price = 1320
    elif totalSize <= 200 and weight_float <= 10:
        price = 3080
    else:
        return -1  # 規定サイズを超えている場合

    # クーポン適用時、料金を10%割引
    if use_coupon:
        price *= 0.9  # 10% 割引

    return price  # 計算された料金を返す
