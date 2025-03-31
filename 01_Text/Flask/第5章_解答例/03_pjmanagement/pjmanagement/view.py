from flask import render_template
from pjmanagement import app
from pjmanagement.model import PjmData

# "/" にアクセスしたときの処理（プロジェクト一覧を表示）
@app.route("/")
def show_list():
    # プロジェクトデータのリストを取得
    pj1 = PjmData() # データ：1件目
    pj1.pjname="Alpha"
    pj1.status="進行中"
    pj1.manager="John"

    pj2 = PjmData() # データ：2件目
    pj2.pjname="Beta"
    pj2.status="完了"
    pj2.manager="Mark"
    
    pj3 = PjmData() # データ：3件目
    pj3.pjname="Gamma"
    pj3.status="開始前"
    pj3.manager="Amy"
    
    pj4 = PjmData() # データ：4件目
    pj4.pjname="Delta"
    pj4.status="進行中"
    pj4.manager="Mike"

    pjmdata_list = [ pj1, pj2, pj3, pj4 ]

    # 取得したデータをテンプレートに渡して一覧を表示
    return render_template('list.html', pjmdata_list=pjmdata_list)
