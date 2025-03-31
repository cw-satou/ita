from flask import render_template, request, redirect
from userupdate import app, db
from userupdate.mst_user import mstUser

# '/users' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/users', methods=['GET'])
def users():
    # すべてのユーザーを取得
    mst_users = db.session.query(mstUser).all()
    # ユーザー一覧ページを表示
    return render_template('user-list.html', users=mst_users)

# '/users/confirm' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/users/confirm', methods=['POST'])
def users_confirm():
    id = request.form['id']  # フォームからIDを取得
    name = request.form['name']  # フォームからユーザー名を取得
    email = request.form['email']  # フォームからメールアドレスを取得
    phone = request.form['phone']  # フォームから電話番号を取得
    user = { 
        'id': id,
        'name': name,
        'email': email,
        'phone': phone,
    }
    # 確認ページを表示
    return render_template('user-confirm.html', user=user)

# ① ユーザー情報編集フォームを表示
# 指定されたIDのユーザー情報を編集する処理（GETメソッドのみ許可）
# @app.route('/users/edit/<id>', methods=['GET'])

# ② ユーザー情報を更新し、一覧を表示（POSTメソッドのみ許可）
# 指定されたIDのユーザー情報を更新する処理
# @app.route('/users/update', methods=['POST'])
