# کتاب خانه ها 

from flask import Blueprint

#فایل ها 

from models.user import User


app = Blueprint('user',__name__)

@app.route('/user/login')
def user():
    return ' user '