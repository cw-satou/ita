from datetime import datetime
from flask import render_template, request, redirect, url_for, get_flashed_messages
from instructioninfo import app
from .models import InstEntity, get_instList, get_field_entities, get_inst_entities, get_inst_entity_by_id

# 講師の一覧を表示する
@app.route('/inst')
def show_inst_list():
    instList = get_instList()  # 講師のリストを取得
    flash_messages = get_flashed_messages()  # 画面に表示するメッセージを取得
    return render_template('inst-list.html', instList=instList, messages=flash_messages, searchKey="全て表示")

# 新しい講師を登録する
@app.route('/inst/create', methods=['GET', 'POST'])
def create_inst():
    fieldList = get_field_entities()  # 分野（職種）のリストを取得
    if request.method == 'POST':  # フォームが送信されたときの処理
        inst_entities = get_inst_entities()  # 既存の講師リストを取得
        # 現在の最大IDを取得し、1を加えて新しい講師のIDを作成
        instructor_id = max(inst_entities, key=lambda inst: inst.instructor_id).instructor_id + 1
        full_name = request.form['fullName']  # フォームから氏名を取得
        business_name = request.form['businessName']  # フォームから事業名を取得
        field_id = int(request.form['fieldId'])  # フォームから職種のIDを取得
        experience = request.form['experience']  # フォームから経験内容を取得
        # 新しい講師データを作成
        new_instructor = InstEntity(instructor_id, full_name, business_name, field_id, experience, datetime(2023, 1, 15))
        inst_entities.append(new_instructor)  # リストに追加
        return redirect(url_for('show_inst_list'))  # 登録後に講師一覧へ戻る
    return render_template('inst-regist.html', fieldList=fieldList)  # フォームを表示

# 登録をキャンセルし、一覧画面へ戻る
@app.route('/inst/cancel', methods=['POST'])
def cancel():
    return redirect(url_for('show_inst_list'))

# 指定された講師の情報を更新する
@app.route('/inst/update/<int:instructor_id>', methods=['GET', 'POST'])
def update_inst(instructor_id):
    fieldList = get_field_entities()  # 分野のリストを取得
    instList = get_instList()  # 講師のリストを取得
    for instInfo in instList:
        if instInfo[0].instructor_id == instructor_id:  # 指定されたIDの講師を探す
            if request.method == 'POST':  # フォームが送信されたときの処理
                entry = instInfo[0]
                entry.full_name = request.form['fullName']  # 氏名を更新
                entry.business_name = request.form['businessName']  # 事業名を更新
                entry.field_id = int(request.form['fieldId'])  # 職種を更新
                entry.experience = request.form['experience']  # 経験内容を更新
                return redirect(url_for('show_inst_list'))  # 更新後に一覧画面へ戻る
            return render_template('inst-update.html', instEntity=instInfo, fieldList=fieldList)  # 更新フォームを表示

# 指定された講師を削除する
@app.route('/inst/delete/<int:instructor_id>', methods=['POST'])
def delete_inst(instructor_id):
    inst_entities = get_inst_entities()  # 既存の講師リストを取得
    inst = get_inst_entity_by_id(instructor_id)  # 削除対象の講師を取得
    inst_entities.remove(inst)  # リストから削除
    return redirect(url_for('show_inst_list'))  # 削除後に一覧画面へ戻る
