from flask import Blueprint

staff_bp = Blueprint('staff', __name__, template_folder='templates')

from .views.login import staff_login_view
from .views.member import staff_member_view
from .views.menu import staff_menu_view
from .views.staff import staff_view
