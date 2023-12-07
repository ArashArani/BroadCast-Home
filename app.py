# کتاب خانه های استفاده شده

from flask import Flask 

from flask_sqlalchemy import SQLAlchemy

#فایل ها
from blueprints.admin import app as admin
from blueprints.user import app as user
from blueprints.general import app as general
from config import SQLALCHEMY_DATABASE_URI , SECRET_KEY
from extentions import db

#رجیستر ها
app = Flask(__name__)

app.register_blueprint(admin)
app.register_blueprint(user)
app.register_blueprint(general)

# کد ها

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

app.config["SECRET_KEY"] = SECRET_KEY

with app.app_context():
    db.create_all()

app.run(debug=True)