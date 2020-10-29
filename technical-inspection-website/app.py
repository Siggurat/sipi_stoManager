from flask import Flask
from flask_security import SQLAlchemyUserDatastore, Security

from config import Configuration
from extensions import db, admin
from models import CarBrand, CarModel, Status, Application, User, Role
from admin import AdminView

app = Flask(__name__)
app.config.from_object(Configuration)

db.init_app(app)

# Flask admin

admin.init_app(app)

admin_views = [
    AdminView(CarBrand, db.session),
    AdminView(CarModel, db.session),
    AdminView(Status, db.session),
    AdminView(Application, db.session)
]

admin.add_views(*admin_views)

# Flask security

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

app.secret_key = 'Super secret key'

# Flask mail
# !!!
# Uncomment if you want to use it
# !!!
# mail.init_app(app)

