import re
from flask import render_template, request, redirect, url_for, flash, session
from roomecho import db
from roomecho.member import member_bp
from roomecho.models.MemberMaster import MemberMaster

# 会員情報変更
@member_bp.route("/memberadd", methods=["GET", "POST"])
def member_add():
    if request.method == "GET":
        member = MemberMaster
        member.member_name = ""
        member.email = ""
        member.phone_number = ""
        member.address = ""
        return render_template(
            "member/member-add.html",
            member=member,
            err_flag=False,
            err_member_name="",
            err_email="",
            err_phone_number="",
            err_address="",
            err_password="",
            err_password_confirm="",
        )

    if request.method == "POST":
        err_flag = False
        err_member_name = ""
        err_email = ""
        err_phone_number = ""
        err_address = ""
        err_password = ""
        err_password_confirm = ""

        # 入力チェック
        # 会員名が空の場合
        if not request.form["member_name"]:
            err_flag = True
            err_member_name = "[会員名]を入力してください"

        # 会員名が30文字を超える場合
        if len(request.form["member_name"]) > 30:
            err_flag = True
            err_member_name = "[会員名]は30文字以内で入力してください"

        # メールアドレスが空の場合
        if not request.form["email"]:
            err_flag = True
            err_email = "[メールアドレス]を入力してください"

        # メールアドレスが254文字を超える場合
        if len(request.form["email"]) > 254:
            err_flag = True
            err_email = "[メールアドレス]は254文字以内で入力してください"

        # メールアドレスの形式が正しくない場合
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern=pattern, string=request.form["email"]):
            err_flag = True
            err_email = "[メールアドレス]はメールアドレスの形式で入力してください"

        # 電話番号が空の場合
        if not request.form["phone_number"]:
            err_flag = True
            err_phone_number = "[電話番号]を入力してください"

        # 電話番号が10文字から11文字の範囲外の場合
        if (
            len(request.form["phone_number"]) < 10
            or len(request.form["phone_number"]) > 11
        ):
            err_flag = True
            err_phone_number = "[電話番号]は10文字～11文字以内で入力してください"

        # 住所が空の場合
        if not request.form["address"]:
            err_flag = True
            err_address = "[住所]を入力してください"

        # 住所が254文字を超える場合
        if len(request.form["address"]) > 254:
            err_flag = True
            err_address = "[住所]は254文字以内で入力してください"

        # パスワードが空の場合
        if not request.form["password"]:
            err_flag = True
            err_password = "[パスワード]を入力してください"

        # パスワードが254文字を超える場合
        if len(request.form["password"]) > 254:
            err_flag = True
            err_password = "[パスワード]は254文字以内で入力してください"

        # 確認用パスワードが空の場合
        if not request.form["password_comfirm"]:
            err_flag = True
            err_password_comfirm = "[確認用パスワード]を入力してください"

        # 確認用パスワードが254文字を超える場合
        if len(request.form["password_comfirm"]) > 254:
            err_flag = True
            err_password_comfirm = "[確認用パスワード]は254文字以内で入力してください"

        # パスワードと確認用パスワードが一致しない場合
        if request.form["password"] != request.form["password_comfirm"]:
            err_flag = True
            err_password_comfirm = (
                "[確認用パスワード]には[パスワード]と同じものを入力してください"
            )

        # エラーがあったら編集画面に戻る
        if err_flag:
            member.password = ""
            return render_template(
                "member/member-add.html",
                member=member,
                err_member_name=err_member_name,
                err_email=err_email,
                err_phone_number=err_phone_number,
                err_address=err_address,
                err_password=err_password,
                err_password_comfirm=err_password_comfirm,
            )

        # 会員データを登録
        member = MemberMaster()
        member.member_name = request.form["member_name"]
        member.email = request.form["email"]
        member.phone_number = request.form["phone_number"]
        member.address = request.form["address"]
        member.password = request.form["password"]
        db.session.add(member)
        db.session.commit()

        return redirect(url_for("member.login"))


# 会員情報変更
@member_bp.route("/edit", methods=["GET", "POST"])
@MemberMaster.is_login
def member_edit():
    user_id = session["loginId"]
    if request.method == "GET":
        member = db.session.query(MemberMaster).get(user_id)
        err_flag = False
        err_member_name = ""
        err_email = ""
        err_phone_number = ""
        err_address = ""

        return render_template(
            "member/member-edit.html",
            member=member,
            err_member_name=err_member_name,
            err_email=err_email,
            err_phone_number=err_phone_number,
            err_address=err_address,
        )

    if request.method == "POST":
        member = MemberMaster()
        member.user_id = user_id,
        member.member_name = request.form["member_name"]
        member.email = request.form["email"]
        member.phone_number = request.form["phone_number"]
        member.address = request.form["address"]
        err_flag = False
        err_member_name = ""
        err_email = ""
        err_phone_number = ""
        err_address = ""

        # 入力チェック
        # 会員名が空の場合
        if not request.form["member_name"]:
            err_flag = True
            err_member_name = "[会員名]を入力してください"

        # 会員名が30文字を超える場合
        if len(request.form["member_name"]) > 30:
            err_flag = True
            err_member_name = "[会員名]は30文字以内で入力してください"

        # メールアドレスが空の場合
        if not request.form["email"]:
            err_flag = True
            err_email = "[メールアドレス]を入力してください"

        # メールアドレスが254文字を超える場合
        if len(request.form["email"]) > 254:
            err_flag = True
            err_email = "[メールアドレス]は254文字以内で入力してください"

        # メールアドレスの形式が正しくない場合
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern=pattern, string=request.form["email"]):
            err_flag = True
            err_email = "[メールアドレス]はメールアドレスの形式で入力してください"

        # 電話番号が空の場合
        if not request.form["phone_number"]:
            err_flag = True
            err_phone_number = "[電話番号]を入力してください"

        # 電話番号が10文字から11文字の範囲外の場合
        if len(request.form["phone_number"]) < 10 or len(request.form["phone_number"]) > 11:
            err_flag = True
            err_phone_number = "[電話番号]は10文字～11文字以内で入力してください"

        # 住所が空の場合
        if not request.form["address"]:
            err_flag = True
            err_address = "[住所]を入力してください"

        # 住所が254文字を超える場合
        if len(request.form["address"]) > 254:
            err_flag = True
            err_address = "[住所]は254文字以内で入力してください"

        # エラーがあったら編集画面に戻る
        if err_flag:
            member.password = ""
            return render_template(
                "member/member-edit.html",
                member=member,
                err_member_name=err_member_name,
                err_email=err_email,
                err_phone_number=err_phone_number,
                err_address=err_address,
            )

        # 変更対象のレコードを取得
        member = db.session.query(MemberMaster).get(user_id)

        # 該当するレコードがあったらデータを更新
        if member:
            member.member_name = request.form["member_name"]
            member.address = request.form["address"]
            member.phone_number = request.form["phone_number"]
            member.email = request.form["email"]
            db.session.commit()

        return render_template("member/member-edit-comp.html", member=member)


# 会員退会画面
@member_bp.route("/<user_id>/del", methods=["GET", "POST"])
@MemberMaster.is_login
def member_del(user_id):
    member = db.session.query(MemberMaster).get(user_id)
    if request.method == "GET":
        return render_template("member/member-del.html", member=member)

    if request.method == "POST":
        # 該当するレコードがあったらデータを更新
        if member:
            db.session.delete(member)
            db.session.commit()
        return render_template("member/member-del-comp.html", member=member)
