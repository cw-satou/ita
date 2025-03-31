from flask import Blueprint

# "items" という名前の Blueprint を作成
# __name__ は現在のモジュール名を指定
# 'templates/items' をこの Blueprint のテンプレートフォルダとして設定
items_bp = Blueprint('items', __name__, template_folder='templates/items')

# Blueprint に関連付けられたルート処理をインポート
# view.py 内の処理をこの Blueprint に含めることで、機能を分割し整理
from . import view as items_view
