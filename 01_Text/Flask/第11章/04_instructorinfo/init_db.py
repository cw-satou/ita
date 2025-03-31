from instructorinfo import app, db
from instructorinfo.models import FieldEntity, InstEntity, StaffEntity

# アプリケーションのコンテキスト内でデータベースを操作
with app.app_context():

    # すべてのテーブルを削除（データベースの初期化）
    db.drop_all()

    # データベースの全テーブルを作成
    db.create_all()

    # 分野情報（fields）の初期データを追加
    initial_fields = [
        FieldEntity(field_name="プログラミング"),  # プログラミング関連の分野
        FieldEntity(field_name="IT基礎"),         # ITの基礎知識を扱う分野
        FieldEntity(field_name="情報処理試験対策"), # 情報処理試験対策を扱う分野
        FieldEntity(field_name="ビジネス"),        # ビジネススキルを扱う分野
    ]
    db.session.bulk_save_objects(initial_fields)  # 一括でデータを登録

    # 講師情報（instructors）の初期データを追加
    initial_instructors = [
        InstEntity(full_name="宮本龍之介", business_name="ryu", field_id=1, experience="Java C# VB"),
        InstEntity(full_name="田中花子", business_name="hana", field_id=2, experience="ネットワーク データベース"),
        InstEntity(full_name="佐藤春樹", business_name="haruki", field_id=1, experience="HTML CSS JS"),
        InstEntity(full_name="鈴木悠太", business_name="yuta", field_id=3, experience="基本情報 応用情報"),
        InstEntity(full_name="高橋真理子", business_name="takamari", field_id=4, experience="マナー プレゼンテーション"),
        InstEntity(full_name="伊藤涼子", business_name="ryoko", field_id=2, experience="コンピュータ基礎 アルゴリズム"),
        InstEntity(full_name="渡辺勇気", business_name="yuuki", field_id=2, experience="アルゴリズム データベース"),
        InstEntity(full_name="小林健二", business_name="kobaken", field_id=1, experience="JS Java Python"),
        InstEntity(full_name="加藤あゆみ", business_name="ayu", field_id=4, experience="ライティング マナー"),
        InstEntity(full_name="山本直樹", business_name="nao", field_id=1, experience="Python JS"),
    ]
    db.session.bulk_save_objects(initial_instructors)  # 一括でデータを登録

    # スタッフ情報（staff）の初期データを追加
    initial_staff = [
        StaffEntity(login_id="manager01", login_password="sec01", staff_name="管理一花"),  # 管理者アカウント
        StaffEntity(login_id="manager02", login_password="sec02", staff_name="管理二郎"),  # 管理者アカウント
        StaffEntity(login_id="staff01", login_password="pass01", staff_name="スタッフ一夫"),  # スタッフアカウント
        StaffEntity(login_id="staff02", login_password="pass02", staff_name="スタッフ二美"),  # スタッフアカウント
        StaffEntity(login_id="staff03", login_password="pass03", staff_name="スタッフ三郎"),  # スタッフアカウント
    ]
    db.session.bulk_save_objects(initial_staff)  # 一括でデータを登録

    # データベースに変更を反映
    db.session.commit()

    # 初期化完了メッセージを出力
    print("Database initialized.")
