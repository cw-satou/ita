from datetime import datetime
from functools import wraps

from flask import flash, redirect, session, url_for
from instructorinfo import db

# 分野（フィールド）情報を管理するデータベースモデル
class FieldEntity(db.Model):
    __tablename__ = 'fields'  # テーブル名を 'fields' に設定

    # 分野ID（主キー、自動インクリメント）
    field_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 分野名（最大20文字、ユニーク制約あり、NULL禁止）
    field_name = db.Column(db.String(20), unique=True, nullable=False)

# 講師情報を管理するデータベースモデル
class InstEntity(db.Model):
    __tablename__ = 'instructors'  # テーブル名を 'instructors' に設定

    # 講師ID（主キー、自動インクリメント）
    instructor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 氏名（最大20文字、NULL禁止）
    full_name = db.Column(db.String(20), nullable=False)

    # 事業所名（最大20文字、ユニーク制約あり、NULL禁止）
    business_name = db.Column(db.String(20), unique=True, nullable=False)

    # 分野ID（外部キー: 'fields' テーブルの 'field_id' に紐づく）
    field_id = db.Column(db.Integer, db.ForeignKey('fields.field_id'))

    # 経験（最大100文字、NULL許可）
    experience = db.Column(db.String(100))

    # 登録日（デフォルトで現在日時を設定）
    regist_date = db.Column(db.DateTime, default=datetime.now)

    # 検索キーワードを設定するメソッド
    @staticmethod
    def set_searchKey_text(keyword):
        if keyword:  # キーワードが入力されている場合
            searchKey = f"キーワード: {keyword}"
        else:  # キーワードが未入力の場合
            searchKey = "全て表示"
        return searchKey

# スタッフ情報を管理するデータベースモデル
class StaffEntity(db.Model):
    __tablename__ = 'staff'  # テーブル名を 'staff' に設定

    # スタッフID（主キー、自動インクリメント）
    staff_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # ログインID（最大20文字、ユニーク制約あり、NULL禁止）
    login_id = db.Column(db.String(20), unique=True, nullable=False)

    # ログインパスワード（最大20文字、NULL禁止）
    login_password = db.Column(db.String(20), nullable=False)

    # スタッフ名（最大20文字、NULL禁止）
    staff_name = db.Column(db.String(20), nullable=False)

# ログイン認証を行うデコレーター
def is_login(view):
    @wraps(view)  # 元の関数の情報（関数名やドキュメント）を保持するデコレーター
    def inner(*args, **kwargs):
        # セッションからログインスタッフ情報を取得
        loginStaff = session.get('staff_name')

        # ログインしていない場合はログイン画面へリダイレクト
        if not loginStaff:
            flash("ログインしてください")  # ログインを促すメッセージを表示
            return redirect(url_for('login'))  # ログインページへ遷移

        # ログイン済みの場合は元のビュー関数を実行
        return view(*args, **kwargs)
    
    return inner  # 内部関数を返す（デコレーターとして適用）
