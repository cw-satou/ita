from flask import request, render_template
from werkzeug.exceptions import HTTPException

def register_error_handlers(app):
    @app.errorhandler(Exception)
    def show_system_error_page(error):
        if isinstance(error, HTTPException):
            status = error.code
        else:
            status = 500  # 通常の例外なら500とみなす

        message = str(error)
        if request.path.startswith("/staff"):
            return render_template("common/staff-error.html", status = status, message = message), status
        else:
            return render_template("common/member-error.html", status = status, message = message), status
