from flask import render_template, request
from userregist import app, db
from userregist.mst_user import mstUser

# 'input' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/input', methods=['GET'])
def input():
    # user-input.html をレンダリングして表示
    return render_template('user-input.html')

# '/register' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/register', methods=['POST'])
def register():
    # フォームから送信されたデータを取得
    name = request.form['name']  # ユーザー名
    email = request.form['email']  # メールアドレス
    phone = request.form['phone']  # 電話番号

    # ユーザーデータをデータベースに登録
    mst_users = mstUser(name=name, email=email, phone=phone)  # 新しいユーザーインスタンスを作成
    db.session.add(mst_users)  # ユーザー情報をデータベースに追加
    db.session.commit()  # データベースに変更を反映

    # 登録済みのすべてのユーザーデータを取得
    mst_users = db.session.query(mstUser).all()

    # ユーザーリストをHTMLテンプレートに渡して表示
    return render_template('user-result.html', users=mst_users)

# '/display' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/display', methods=['GET'])
def display():
    # 登録済みのすべてのユーザーデータを取得
    mst_users = db.session.query(mstUser).all()
    # ユーザーリストをHTMLテンプレートに渡して表示
    return render_template('user-result.html', users=mst_users)
