from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("../config.py")

db = SQLAlchemy()
db.init_app(app)

from .staff import staff_bp
from .member import member_bp

app.register_blueprint(staff_bp, url_prefix='/staff')
app.register_blueprint(member_bp, url_prefix='/member')

# エラーハンドラ登録
from .view import register_error_handlers
register_error_handlers(app)
