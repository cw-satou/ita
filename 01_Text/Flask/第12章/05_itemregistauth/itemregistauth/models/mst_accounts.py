from functools import wraps
from flask import flash, redirect, session, url_for
from itemregistauth import db  # データベースオブジェクトをインポート

# ユーザーアカウント用のモデルクラス
class Mst_account(db.Model):
    __tablename__ = 'account'  # テーブル名を指定

    # ユーザーID（主キー、文字列型、最大255文字）
    user_id = db.Column(db.String(255), primary_key=True)
    
    # パスワード（必須、文字列型、最大255文字）
    password = db.Column(db.String(255), nullable=False)

# ログイン認証のデコレータ
def is_login(view):
    @wraps(view)  # 元の関数のメタデータを保持
    def inner(*args, **kwargs):
        # セッションからログイン情報を取得
        login = session.get('loggedInUser')
        
        # ログインしていない場合、ログインページへリダイレクト
        if not login:
            flash("ログインしてください。")  # メッセージを表示
            return redirect(url_for('login'))  # ログインページへ遷移

        return view(*args, **kwargs)  # ログイン済みの場合は元の関数を実行
    return inner  # 内部関数を返す
