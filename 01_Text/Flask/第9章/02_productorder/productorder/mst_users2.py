from functools import wraps
from flask import flash, redirect, session, url_for
from productorder import db

# ユーザ情報を管理するモデルクラス

class mstUsers2(db.Model):
# テーブル名の指定（クラス名とは異なる名前を使いたい場合に明示的に指定）
    __tablename__ = 'users2'

    # 主キーとしてidを定義
    id = db.Column(db.String(6), primary_key=True)

    # 必須項目としてname、password、emailを定義
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    # 任意項目としてphoneを定義
    phone = db.Column(db.String(15))

# ログイン認証のデコレータ
def is_login(view):
    @wraps(view)  # 元の関数のメタデータを保つためのデコレータ
    def inner(*args, **kwargs):
        # ログインしていない場合はログインページに遷移させる
        login = session.get('loggedInUser')  # セッションに格納されているログイン情報を取得
        if not login:  # ログインしていない場合
            flash('ログインしてください。')  # ログインを促すメッセージを表示
            return redirect(url_for('login'))

        return view(*args, **kwargs)  # ログイン済みの場合は元のビュー関数を実行
    return inner  # 内部関数を返す
