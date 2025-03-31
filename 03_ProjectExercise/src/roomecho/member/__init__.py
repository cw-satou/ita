from flask import Blueprint

member_bp = Blueprint('member', __name__, template_folder='templates')

from .views.login import member_login_view
from .views.menu import member_menu_view
from .views.vacancy import member_vacancy_view
from .views.bookingadd import member_bookingadd_view
from .views.member import member_view

