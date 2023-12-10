# کتاب خانه ها 

from flask import Blueprint , request , render_template , redirect , flash , url_for

from flask_login import current_user , login_user , login_required

from passlib.hash import sha256_crypt

#فایل ها 

from models.user import User

from extentions import db

from models.product import Product

from models.cart import Cart

from models.cart_item import CartItem

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




@app.route('/user/dashboard' , methods=['GET' ,'POST'])
@login_required
def dashboard():
    if request.method == 'GET':
        flash(' با موفقیت وارد شدید ')
        return render_template('user/dashboard.html')
    else: 
        username = request.form.get('username', None)
        phone = request.form.get('phone', None)
        address = request.form.get('address', None)
        email = request.form.get('email',None)
        first_name = request.form.get('first_name',None)
        last_name = request.form.get('last_name',None)

        if current_user.username != username:
            user = User.query.filter(User.username == username ).first()
            if user != None:
                flash(' نام کاربری دیگری انتخاب کنید ')
                return redirect('/user/dashboard')
            else:
                current_user.username = username
        if current_user.phone != phone:
            user = User.query.filter(User.phone==phone).first()
            if user != None:
                flash("این شماره قبلا در سایت ثبت شده")
                return redirect('/user/dashboard')
            else :
                current_user.phone = phone

        if current_user.email != email:
            user = User.query.filter(User.email==email).first()
            if user != None:
                flash("این ایمیل قبلا در سایت ثبت شده")
                return redirect('/user/dashboard')
            else :
                current_user.email = email
        current_user.address = address
        current_user.first_name = first_name
        current_user.last_name = last_name

        db.session.commit()
        flash(' تغییرات با موفقیت ثبت شد ')
        return redirect('/user/dashboard')

@app.route('/user/dashboard/chenge-password',methods =["POST","GET"])
@login_required
def chenge_password():
    if request.method == 'GET':
        return render_template('user/chenge-password.html')
    else :
        old_password = request.form.get('old_password',None)
        new_password1 = request.form.get('new_password1',None)
        new_password2 = request.form.get('new_password2',None)

        if (sha256_crypt.verify(old_password , current_user.password)) and new_password1 == new_password2:
            current_user.password = sha256_crypt.encrypt(new_password1)
            db.session.commit()
            flash('رمز با موفقیت تغییر کرد')
            return redirect('/user/dashboard')
        elif new_password1 != new_password2 :
            flash('رمز جدیدهای جدید باهم مطابقت ندارند ')
            return redirect('/user/dashboard')
        elif sha256_crypt.verify(old_password) != True:
            flash('رمز عبور قدیمی شما درست نیست')
            return redirect('/user/dashboard')
        else:
            flash('بعذا تلاش کنید')
            return redirect('/user/dashboard')



@app.route('/add-to-cart' , methods=['GET'])
@login_required
def add_to_cart():
    id = request.args.get('id')
    product = Product.query.filter(Product.id==id).first_or_404()
    cart=current_user.carts.filter(Cart.status == 'pending').first()
    if cart == None:
        cart = Cart()
        current_user.carts.append(cart)
        db.session.add(cart)
    cart_item = cart.cart_items.filter(CartItem.product == product).first()
    if cart_item == None :
        item = CartItem(quantity=1)
        item.price = product.price
        item.cart = cart
        item.product = product
        db.session.add(item)
    else :
        cart_item.quantity += 1
    db.session.commit()
    flash(' با موفقیت به سبد خرید اضافه شد')

    return redirect('/user/dashboard/cart')



@app.route('/remove-from-cart' , methods=['GET'])
@login_required
def remove_from_cart():
    id = request.args.get('id')
    cart_item = CartItem.query.filter(CartItem.id==id).first_or_404()
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
    else:
        db.session.delete(cart_item)

    db.session.commit()
    flash(' با موفقیت از سبد خرید حذف شد ')

    return redirect('/user/dashboard/cart')


@app.route('/user/dashboard/cart' , methods=['GET'])
@login_required
def cart():
    cart = current_user.carts.filter(Cart.status == 'pending').first()
    return render_template('user/cart.html', cart=cart)
