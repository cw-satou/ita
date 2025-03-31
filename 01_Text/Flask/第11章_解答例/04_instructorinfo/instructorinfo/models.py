from datetime import datetime
from functools import wraps

from flask import flash, redirect, session, url_for
from instructorinfo import db

# 分野情報（fields）を表すデータベースモデル
class FieldEntity(db.Model):
    __tablename__ = 'fields'  # テーブル名を指定

    # 分野ID（主キー、オートインクリメント）
    field_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # 分野名（20文字以内、一意制約あり、NULL不可）
    field_name = db.Column(db.String(20), unique=True, nullable=False)

# 講師情報（instructors）を表すデータベースモデル
class InstEntity(db.Model):
    __tablename__ = 'instructors'  # テーブル名を指定

    # 講師ID（主キー、オートインクリメント）
    instructor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # 氏名（20文字以内、NULL不可）
    full_name = db.Column(db.String(20), nullable=False)
    
    # ビジネスネーム（20文字以内、一意制約あり、NULL不可）
    business_name = db.Column(db.String(20), unique=True, nullable=False)
    
    # 分野ID（外部キー、fieldsテーブルのfield_idを参照）
    field_id = db.Column(db.Integer, db.ForeignKey('fields.field_id'))
    
    # 経験（100文字以内）
    experience = db.Column(db.String(100))
    
    # 登録日時（デフォルトで現在の日時を設定）
    regist_date = db.Column(db.DateTime, default=datetime.now)

    @staticmethod
    def set_searchKey_text(keyword):
        # 検索キーワードの有無に応じて表示する文字列を設定
        if keyword:  # キーワードが入力されている場合
            searchKey = f"キーワード: {keyword}"
        else:  # キーワードが未入力の場合
            searchKey = "全て表示"
        return searchKey

# スタッフ情報（staff）を表すデータベースモデル
class StaffEntity(db.Model):
    __tablename__ = 'staff'  # テーブル名を指定

    # スタッフID（主キー、オートインクリメント）
    staff_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # ログインID（20文字以内、一意制約あり、NULL不可）
    login_id = db.Column(db.String(20), unique=True, nullable=False)
    
    # パスワード（20文字以内、NULL不可）
    login_password = db.Column(db.String(20), nullable=False)
    
    # スタッフ名（20文字以内、NULL不可）
    staff_name = db.Column(db.String(20), nullable=False)

# ログイン認証を行うデコレーター関数
def is_login(view):
    @wraps(view)  # 関数のメタデータを維持
    def inner(*args, **kwargs):
        loginStaff = session.get('staff_name')  # セッションからログイン中のスタッフ名を取得
        if not loginStaff:  # ログインしていない場合
            flash("ログインしてください")  # フラッシュメッセージを設定
            return redirect(url_for('login'))  # ログインページへリダイレクト
        return view(*args, **kwargs)  # ログイン済みの場合は元のビュー関数を実行
    return inner  # 内部関数を返す
