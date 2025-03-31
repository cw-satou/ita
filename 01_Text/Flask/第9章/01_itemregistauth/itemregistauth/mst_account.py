from functools import wraps
from flask import flash, redirect, session, url_for
from itemregistauth import db

# ユーザーアカウント用のモデルクラス
class mstAccount(db.Model):
    __tablename__ = 'account'  # テーブル名を指定（デフォルトではクラス名がテーブル名になる）

    # user_idカラム: 主キー（ユーザーID）、文字列型、最大長255
    user_id = db.Column(db.String(255), primary_key=True)

    # passwordカラム: 必須、文字列型、最大長255
    password = db.Column(db.String(255), nullable=False)

# ログイン認証のデコレータ
def is_login(view):
    @wraps(view)  # 元の関数のメタデータ（関数名やdocstringなど）を維持するデコレータ
    def inner(*args, **kwargs):
        # ログインしているかをセッション情報から確認
        login = session.get('loggedInUser')  # セッションに格納されているログイン情報を取得

        if not login:  # ログインしていない場合
            flash(['I01'])  # ログインを促すメッセージを表示
            return redirect(url_for('login'))  # ログインページにリダイレクト

        return view(*args, **kwargs)  # ログイン済みの場合は元のビュー関数を実行
    return inner  # 内部関数を返す（デコレータとして使用）
