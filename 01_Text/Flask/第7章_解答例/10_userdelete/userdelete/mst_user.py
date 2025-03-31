from userdelete import db

# ユーザー情報を管理するモデルクラス（データベースの `users` テーブルと対応）
class mstUser(db.Model):
    # テーブル名を明示的に指定（デフォルトではクラス名がそのままテーブル名になる）
    __tablename__ = 'users'

    # ユーザーID（主キー、オートインクリメント）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 名前（最大50文字、NULL禁止）
    name = db.Column(db.String(50), nullable=False)

    # メールアドレス（最大50文字、NULL禁止）
    email = db.Column(db.String(50), nullable=False)

    # 電話番号（最大15文字、NULL許可）
    phone = db.Column(db.String(15))
