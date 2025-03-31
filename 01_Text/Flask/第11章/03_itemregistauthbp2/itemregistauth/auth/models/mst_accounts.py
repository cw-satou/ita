from functools import wraps
from flask import flash, redirect, session, url_for
from itemregistauth import db  # データベースオブジェクトをインポート

# ユーザーアカウント情報を管理するモデルクラス
class Mst_account(db.Model):
    __tablename__ = 'account'  # 使用するテーブル名を指定

    # ユーザーID（主キー、文字列型、最大255文字）
    user_id = db.Column(db.String(255), primary_key=True)
    
    # パスワード（必須、文字列型、最大255文字）
    password = db.Column(db.String(255), nullable=False)

# ログイン認証を行うデコレーター
def is_login(view):
    @wraps(view)  # 元の関数の情報（関数名やドキュメント）を保持するデコレーター
    def inner(*args, **kwargs):
        # セッションからログイン情報を取得
        login = session.get('loggedInUser')

        # ログインしていない場合はログインページへリダイレクト
        if not login:
            flash("ログインしてください。")  # ログインを促すメッセージを表示
            return redirect(url_for('login'))  # ログインページへ遷移

        # ログイン済みの場合は元のビュー関数を実行
        return view(*args, **kwargs)
    
    return inner  # 内部関数を返す（デコレーターとして適用）
