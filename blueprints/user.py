# کتاب خانه ها 

from flask import Blueprint , request , render_template , redirect , flash , url_for

from flask_login import current_user , login_user 

from passlib.hash import sha256_crypt

#فایل ها 

from models.user import User

from extentions import db

#کد ها 


app = Blueprint('user',__name__)

@app.route('/user/login' , methods=['GET','POST'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect('/user/dashboard')
        return render_template('user/login.html')
    else:
        register = request.form.get('register', None)
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        password2 = request.form.get('password2', None)
        if register != None :
            user = User.query.filter(User.username == username ).first()
            if user != None:
                flash(' نام کاربری دیگری انتخاب کنید ')
                return redirect('/user/login')
            
            user = User(username = username , password = sha256_crypt.encrypt(password))

            if password == password2 :
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect ('/user/dashboard')
            else:
                flash('رمز عبور مطابقت ندارد')
                return redirect('/user/login')
            
        
        else:
            user = User.query.filter(User.username == username ).first()
            if user == None:
                flash(' نام کاربری یا رمز اشتباه است ')
                return redirect(url_for('user.login'))
            if sha256_crypt.verify( password , user.password  ):
                login_user(user)
                return redirect('/user/dashboard')
            else :
                flash(' نام کاربری یا رمز اشتباه است ')
                return redirect('/user/login')




@app.route('/user/dashboard')
def dash():
    return "Dashboard"