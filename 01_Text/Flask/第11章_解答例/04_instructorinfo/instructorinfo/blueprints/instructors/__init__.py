from flask import Blueprint

# "instructors" という名前の Blueprint を作成
# __name__ は現在のモジュールを示す
# template_folder='templates/instructors' で講師関連のテンプレートフォルダを指定
instructors_bp = Blueprint('instructors', __name__, template_folder='templates/instructors')

# 講師関連のルート処理をインポート
from . import view as instructors_view
