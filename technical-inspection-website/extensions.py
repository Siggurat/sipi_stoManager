from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_mail import Mail

from admin import HomeAdminView

db = SQLAlchemy()

admin = Admin(name='АвтоРусь', url='/', index_view=HomeAdminView(name='Home'))

mail = Mail()