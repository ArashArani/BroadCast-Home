# کتاب خانه ها 

from flask import Blueprint , session , request , abort , redirect , render_template

#فایل ها 
from models.article import Article
from models.exprience import Experience
from models.news import News
from config import ADMIN_USERNAME , ADMIN_PASSWORD

#کد ها 


app = Blueprint('admin',__name__)


@app.before_request
def before_request():
    if session.get('admin_login', None) == None and request.endpoint != "admin.main":
        abort(403)

@app.route('/admin/login' , methods = ["POST","GET"])
def main():
    if request.method == "POST":
        username= request.form.get('username',None)
        password= request.form.get('password',None)

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD :
            session ['admin_login'] = username
            return redirect('/admin/dashboard')
        else:
            return redirect('/admin/login')
    else :
        return render_template ("/admin/login.html")


@app.route('/admin/dashboard' , methods = ["GET"])
def dashboard():
    return 'dashboard'
