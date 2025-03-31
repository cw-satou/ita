from flask import Blueprint

# "auth" という名前の Blueprint を作成
# __name__ は現在のモジュール名を示す
# 'templates/auth' フォルダをこの Blueprint 用のテンプレートフォルダとして設定
auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')

# Blueprint に関連付けられたルートをインポート
# view.py 内の処理をこの Blueprint に含めることで、機能を分割しやすくする
from . import view as auth_view
