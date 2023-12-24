# کتاب خانه های استفاده شده

from flask import Flask , flash , redirect , url_for

from flask_wtf.csrf import CSRFProtect



from flask_login import LoginManager

#فایل ها

from blueprints.admin import app as admin

from blueprints.user import app as user

from blueprints.general import app as general

from config import SQLALCHEMY_DATABASE_URI , SECRET_KEY

from extentions import db

from models.user import User

#رجیستر ها

app = Flask(__name__)

app.register_blueprint(admin)

app.register_blueprint(user)

app.register_blueprint(general)

# کد ها

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

app.config["SECRET_KEY"] = SECRET_KEY

db.init_app(app)

csrf = CSRFProtect(app)

login_manager = LoginManager()

login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()

@login_manager.unauthorized_handler
def unauthorized ():
    flash (' وارد حساب کاربری خود شوید ')
    return redirect(url_for('user.login'))


with app.app_context():
    db.create_all()

app.run(debug=True)