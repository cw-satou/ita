from datetime import datetime
from instructioninfo import app

# 分野（フィールド）を表すエンティティクラス
class FieldEntity:
    def __init__(self, field_id: int, field_name: str):
        self.field_id = field_id  # 分野ID
        self.field_name = field_name  # 分野名

# 講師（インストラクター）を表すエンティティクラス
class InstEntity:
    def __init__(self, instructor_id: int, full_name: str, business_name: str, field_id: int, experience: str, regist_date: datetime):
        self.instructor_id = instructor_id  # 講師ID
        self.full_name = full_name  # 氏名
        self.business_name = business_name  # 会社名または事業名
        self.field_id = field_id  # 関連する分野のID
        self.experience = experience  # 経験の詳細
        self.regist_date = regist_date  # 登録日

# 講師リストを取得し、それぞれの分野情報を付加したリストを作成
def get_instList():
    field_entities = get_field_entities()  # 分野情報を取得
    inst_entities = get_inst_entities()  # 講師情報を取得
    # 各講師に対応する分野を見つけてタプルにしてリスト化
    instList = [(inst, next(field for field in field_entities if field.field_id == inst.field_id)) for inst in inst_entities]
    return instList

# 分野情報を取得（未設定の場合は初期データを作成）
def get_field_entities():
    field_entities = app.config['FIELDS']  # 設定から分野情報を取得
    if not field_entities:  # データが存在しない場合は初期データを作成
        field_entities = [
            FieldEntity(1, "プログラミング"),
            FieldEntity(2, "データサイエンス"),
            FieldEntity(3, "AI開発"),
        ]
        app.config['FIELDS'] = field_entities  # 設定に保存
    return field_entities

# 講師情報を取得（未設定の場合は初期データを作成）
def get_inst_entities():
    inst_entities = app.config['INSTRUCTORS']  # 設定から講師情報を取得
    if not inst_entities:  # データが存在しない場合は初期データを作成
        inst_entities = [
            InstEntity(1, "山田 太郎", "Yamada Tech", 1, "PythonとDjangoを5年間経験", datetime(2023, 1, 15)),
            InstEntity(2, "佐藤 花子", "Sato AI Lab", 2, "機械学習と統計分析を10年間経験", datetime(2022, 10, 20)),
            InstEntity(3, "田中 健", "Tanaka Software", 3, "深層学習とNLPの研究経験8年", datetime(2021, 5, 10)),
        ]
        app.config['INSTRUCTORS'] = inst_entities  # 設定に保存
    return inst_entities

# 指定されたIDの講師情報を取得
def get_inst_entity_by_id(instructor_id: int):
    inst_entities = app.config['INSTRUCTORS']  # 設定から講師情報を取得
    for inst in inst_entities:
        if inst.instructor_id == int(instructor_id):  # 指定されたIDと一致する講師を検索
            return inst
