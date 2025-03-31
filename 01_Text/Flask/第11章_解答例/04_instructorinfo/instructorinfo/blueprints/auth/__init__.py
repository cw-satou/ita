from flask import Blueprint

# "auth" という名前の Blueprint を作成
# __name__ は現在のモジュールを示す
# template_folder='templates/auth' で認証用のテンプレートフォルダを指定
auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')

# 認証関連のルート処理をインポート
from . import view as auth_view
