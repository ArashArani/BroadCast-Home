# کتاب خانه های استفاده شده

from flask import Flask 


#فایل ها
from blueprints.admin import app as admin
from blueprints.user import app as user
from blueprints.general import app as general


#رجیستر ها
app = Flask(__name__)

app.register_blueprint(admin)
app.register_blueprint(user)
app.register_blueprint(general)


# کد ها



app.run(debug=True)