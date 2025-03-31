from functools import wraps
from flask import flash, redirect, session, url_for
from roomecho import db

# スタッフマスター
# スタッフ情報のマスターテーブル

class StaffMaster(db.Model):
    __tablename__ = 'staff_master'
    
    # スタッフID（自動採番）
    staff_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # アカウント名（一意制約）
    account_name = db.Column(db.String(15), nullable=False)
    
    # スタッフ名
    staff_name = db.Column(db.String(30), nullable=False)
    
    # 所属名（"フロント部門"、"客室部門"等）
    division_name = db.Column(db.String(30), nullable=False)
    
    # パスワード
    password = db.Column(db.String(10), nullable=False)

    def is_login(view):
        @wraps(view)
        def inner(*args, **kwargs):
            login = session.get('loginId')
            if not login:
                flash("ログインしてください。")
                return redirect(url_for('staff.login'))
            return view(*args, **kwargs)
        return inner
