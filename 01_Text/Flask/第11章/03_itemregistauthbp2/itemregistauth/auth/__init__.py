from flask import Blueprint

# "auth" という名前の Blueprint を作成
# __name__ は現在のモジュールを示す
# template_folder で、この Blueprint 用のテンプレートフォルダを指定
auth_bp = Blueprint('auth', __name__, template_folder='templates')

# Blueprint に関連付ける処理をインポート
# views モジュール内の処理を auth_views として使用
from .views import view as auth_views
