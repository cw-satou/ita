from flask import render_template
from pjmanagement import app
from pjmanagement.model import PjmData

# "/" にアクセスしたときの処理
@app.route("/")
def show_list():
    # プロジェクトデータのリストを取得
    pj1 = PjmData() # データ：1件目
    pj1.pjname="Alpha"
    pj1.status="進行中"
    pj1.manager="John"

    pj2 = PjmData() # データ：2件目
    
    pj3 = PjmData() # データ：3件目
    
    pj4 = PjmData() # データ：4件目

    pjmdata_list = [ pj1 ]

    # 取得したデータをテンプレートに渡して一覧を表示
    return render_template('list.html', pjmdata_list=pjmdata_list)
