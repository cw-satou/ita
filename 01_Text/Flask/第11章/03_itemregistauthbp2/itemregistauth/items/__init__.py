from flask import Blueprint

# "items" という名前の Blueprint を作成
# __name__ は現在のモジュール名を指定
# 'templates' フォルダをこの Blueprint のテンプレートフォルダとして設定
items_bp = Blueprint('items', __name__, template_folder='templates')

# Blueprint に関連付けられたルート処理をインポート
# .views モジュール内の処理を item_views として利用
from .views import view as item_views
