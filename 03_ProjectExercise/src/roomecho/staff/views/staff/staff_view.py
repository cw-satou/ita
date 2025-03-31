import os
from flask import render_template, request, redirect, url_for, flash, session
from roomecho import db
from roomecho.staff import staff_bp
from roomecho.models.StaffMaster import StaffMaster


# スタッフ一覧画面
@staff_bp.route("/staffs", methods=["GET"])
@StaffMaster.is_login
def staff_list():
    # データベースからスタッフ情報を取得し、スタッフID順に並べる
    staffs = db.session.query(StaffMaster).order_by("staff_id").all()
    # スタッフ一覧画面を表示
    return render_template("staff/staff-list.html", staffs=staffs)


# スタッフ情報登録画面
@staff_bp.route("/staff/add", methods=["GET", "POST"])
@StaffMaster.is_login
def staff_add():
    # フォームデータを初期化
    staff = StaffMaster()
    staff.staff_id = ""
    staff.account_name = ""
    staff.staff_name = ""
    staff.division_name = ""
    staff.password = ""
    err_flag = False
    err_account_name = ""
    err_staff_name = ""
    err_division_name = ""
    err_password = ""

    if request.method == "GET":
        # スタッフ情報登録画面を表示
        return render_template("staff/staff-add.html", staff=staff)

    if request.method == "POST":
        # フォームデータを取得
        staff.staff_id = request.form["staff_id"]
        staff.account_name = request.form["account_name"]
        staff.staff_name = request.form["staff_name"]
        staff.division_name = request.form["division_name"]
        staff.password = request.form["password"]

        # 入力チェック
        if not request.form["account_name"]:
            err_flag = True
            err_account_name = "[アカウント名]を入力してください"

        if len(request.form["account_name"]) > 15:
            err_flag = True
            err_account_name = "[アカウント名]は15文字以内で入力してください"

        if not request.form["staff_name"]:
            err_flag = True
            err_staff_name = "[スタッフ名]を入力してください"

        if len(request.form["staff_name"]) > 30:
            err_flag = True
            err_staff_name = "[スタッフ名]は30文字以内で入力してください"

        if not request.form["division_name"]:
            err_flag = True
            err_division_name = "[所属名]を入力してください"

        if len(request.form["division_name"]) > 30:
            err_flag = True
            err_division_name = "[所属名]は30文字以内で入力してください"

        if not request.form["password"]:
            err_flag = True
            err_password = "[パスワード]を入力してください"

        if len(request.form["password"]) > 10:
            err_flag = True
            err_password = "[パスワード]は10文字以内で入力してください"

        # エラーがあったら編集画面に戻る
        if err_flag:
            return render_template(
                "staff/staff-add.html",
                staff=staff,
                err_account_name=err_account_name,
                err_staff_name=err_staff_name,
                err_division_name=err_division_name,
                err_password=err_password,
            )

        # 新しいスタッフ情報をデータベースに追加
        staff = StaffMaster(
            account_name=request.form["account_name"],
            staff_name=request.form["staff_name"],
            division_name=request.form["division_name"],
            password=request.form["password"],
        )
        db.session.add(staff)
        db.session.commit()

        # 登録完了画面を表示
        return render_template(
            "staff/staff-add-comp.html",
            staff=staff,
            err_account_name=err_account_name,
            err_staff_name=err_staff_name,
            err_division_name=err_division_name,
            err_password=err_password,
        )


# スタッフ情報変更画面
@staff_bp.route("/staff/<staff_id>/edit", methods=["GET", "POST"])
@StaffMaster.is_login
def staff_edit(staff_id):
    # 指定されたスタッフIDの情報を取得
    staff = db.session.query(StaffMaster).get(staff_id)

    if request.method == "GET":
        return render_template("staff/staff-edit.html", staff=staff)

    if request.method == "POST":
        # フォームデータを取得
        staff.staff_id = staff_id
        staff.account_name = request.form["account_name"]
        staff.staff_name = request.form["staff_name"]
        staff.division_name = request.form["division_name"]
        err_flag = False
        err_account_name = ""
        err_staff_name = ""
        err_division_name = ""
        err_password = ""

        # 入力チェック
        if not request.form["account_name"]:
            err_flag = True
            err_account_name = "[アカウント名]を入力してください"

        if len(request.form["account_name"]) > 15:
            err_flag = True
            err_account_name = "[アカウント名]は15文字以内で入力してください"

        if not request.form["staff_name"]:
            err_flag = True
            err_staff_name = "[スタッフ名]を入力してください"

        if len(request.form["staff_name"]) > 30:
            err_flag = True
            err_staff_name = "[スタッフ名]は30文字以内で入力してください"

        if not request.form["division_name"]:
            err_flag = True
            err_division_name = "[所属名]を入力してください"

        if len(request.form["division_name"]) > 30:
            err_flag = True
            err_division_name = "[所属名]は30文字以内で入力してください"

        # エラーがあったら編集画面に戻る
        if err_flag:
            return render_template(
                "staff/staff-edit.html",
                staff=staff,
                err_account_name=err_account_name,
                err_staff_name=err_staff_name,
                err_division_name=err_division_name,
                err_password=err_password,
            )

        # 該当するレコードがあったらデータを更新
        if staff:
            staff.account_name = request.form["account_name"]
            staff.staff_name = request.form["staff_name"]
            staff.division_name = request.form["division_name"]
            db.session.commit()

        # 更新完了画面を表示
        return render_template(
            "staff/staff-edit-comp.html",
            staff=staff,
            err_account_name=err_account_name,
            err_staff_name=err_staff_name,
            err_division_name=err_division_name,
            err_password=err_password,
        )


# スタッフ情報削除確認画面
@staff_bp.route("/staff/<staff_id>/del", methods=["GET", "POST"])
@StaffMaster.is_login
def staff_del(staff_id):
    # 削除対象のレコードを取得
    staff = db.session.query(StaffMaster).get(staff_id)

    if request.method == "GET":
        # スタッフ情報削除確認画面を表示
        return render_template("staff/staff-del.html", staff=staff)

    if request.method == "POST":
        # 該当するレコードがあったらデータを削除
        if staff:
            db.session.delete(staff)
            db.session.commit()

        # 削除完了画面を表示
        return render_template("staff/staff-del-comp.html", staff=staff)
