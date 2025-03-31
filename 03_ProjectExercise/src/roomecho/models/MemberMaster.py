from functools import wraps
from flask import flash, redirect, session, url_for
from roomecho import db

# 会員マスター
# 会員情報のマスターテーブル

class MemberMaster(db.Model):
    __tablename__ = 'member_master'
    
    # 会員ID（自動採番）
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # 会員名
    member_name = db.Column(db.String(30), nullable=False)
    
    # 住所
    address = db.Column(db.String(254), nullable=False)
    
    # 電話番号
    phone_number = db.Column(db.String(15), nullable=False)
    
    # メールアドレス（一意制約）
    email = db.Column(db.String(254), nullable=False)
    
    # パスワード
    password = db.Column(db.String(10), nullable=False)

    def is_login(view):
        @wraps(view)
        def inner(*args, **kwargs):
            login = session.get('loginId')
            if not login:
                flash("ログインしてください。")
                return redirect(url_for('member.login'))
            return view(*args, **kwargs)
        return inner
