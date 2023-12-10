# کتاب خانه ها 

from flask import Blueprint , session , request , abort , redirect , render_template , flash , url_for 

#فایل ها 

from models.article import Article

from models.exprience import Experience

from models.news import News

from models.product import Product

from models.user import User

from config import ADMIN_USERNAME , ADMIN_PASSWORD

from extentions import db

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
    return render_template('/admin/dashboard.html')

@app.route('/admin/dashboard/article',methods = ["POST","GET"])
def articles ():
    if request.method == "GET":
        articles = Article.query.all()
        return render_template("/admin/articles.html", articles = articles)
    else :
        name = request.form.get("name",None)
        description = request.form.get("description",None)
        file = request.files.get('cover',None)
        active = request.form.get('active', None)
        a = Article(name = name , description = description )
        if active == None :
            a.active = 0
        else :
            a.active = 1

        db.session.add(a)
        db.session.commit()

        file.save(f'static/covers/article/{a.id}.jpg') 
        flash('مقاله جدید با موفقیت اضافه شد ')
        return redirect('/admin/dashboard')

@app.route('/admin/dashboard/edit-article/<id>' , methods = ["GET","POST"])
def edit_article(id):
    article = Article.query.filter(Article.id == id).first_or_404()
    if request.method == "GET":
        return render_template("/admin/edit-article.html", article = article)
    else :
        name = request.form.get("name",None)
        description = request.form.get("description",None)
        active = request.form.get("active",None)
        file = request.files.get('cover', None)

        article.name = name
        article.description = description
        if active == None :
            article.active = 0
        else :
            article.active = 1
        
        if file.filename != "":
            file.save(f'static/covers/article/{article.id}.jpg')
        db.session.commit()
        flash(' وضعیت مقاله با موفقیت تغییر کرد ')
        return redirect('/admin/dashboard/article')



@app.route('/admin/dashboard/experience',methods = ["POST","GET"])
def experience ():
    if request.method == "GET":
        experiences = Experience.query.all()
        return render_template("/admin/experiences.html", experiences = experiences)
    else :
        name = request.form.get("name",None)
        description = request.form.get("description",None)
        file = request.files.get('cover',None)
        active = request.form.get('active', None)
        e = Experience(name = name , description = description )
        if active == None :
            e.active = 0
        else :
            e.active = 1

        db.session.add(e)
        db.session.commit()


        file.save(f'static/covers/experience/{e.id}.jpg')
        flash('پروژه جدید با موفقیت اضافه شد ')
        return redirect('/admin/dashboard')

@app.route('/admin/dashboard/edit-experience/<id>' , methods = ["GET","POST"])
def edit_experience(id):
    experience = Experience.query.filter(Experience.id == id).first_or_404()
    if request.method == "GET":
        return render_template("/admin/edit-experience.html", experience = experience)
    else :
        name = request.form.get("name",None)
        description = request.form.get("description",None)
        active = request.form.get("active",None)
        file = request.files.get('cover', None)

        experience.name = name
        experience.description = description
        if active == None :
            experience.active = 0
        else :
            experience.active = 1
        
        if file.filename != "":
            file.save(f'static/covers/experience/{experience.id}.jpg')
        db.session.commit()
        flash(' وضعیت پروژه با موفقیت تغییر کرد ')
        return redirect('/admin/dashboard/experience')




@app.route('/admin/dashboard/news',methods = ["POST","GET"])
def news ():
    if request.method == "GET":
        news = News.query.all()
        return render_template("/admin/newsses.html", news = news)
    else :
        name = request.form.get("name",None)
        description = request.form.get("description",None)
        file = request.files.get('cover',None)
        active = request.form.get('active', None)
        n = News(name = name , description = description )
        if active == None :
            n.active = 0
        else :
            n.active = 1

        db.session.add(n)
        db.session.commit()


        file.save(f'static/covers/news/{n.id}.jpg')
        flash('خبر جدید با موفقیت اضافه شد ')
        return redirect('/admin/dashboard')

@app.route('/admin/dashboard/edit-news/<id>' , methods = ["GET","POST"])
def edit_news(id):
    news = News.query.filter(News.id == id).first_or_404()
    if request.method == "GET":
        return render_template("/admin/edit-news.html", news = news)
    else :
        name = request.form.get("name",None)
        description = request.form.get("description",None)
        active = request.form.get("active",None)
        file = request.files.get('cover', None)

        news.name = name
        news.description = description
        if active == None :
            news.active = 0
        else :
            news.active = 1
        
        if file.filename != "":
            file.save(f'static/covers/news/{news.id}.jpg')
        db.session.commit()
        flash(' وضعیت خبر با موفقیت تغییر کرد ')
        return redirect('/admin/dashboard/news')


@app.route('/admin/dashboard/product',methods = ["POST","GET"])
def product():
    if request.method == "GET":
        product = Product.query.all()
        return render_template("/admin/products.html", product = product)
    else:
        name = request.form.get("name",None)
        description = request.form.get("description",None)
        file = request.files.get('cover',None)
        quantity = request.form.get('quantity', None)
        price = request.form.get('price',None)
        active = request.form.get("active",None)
        p = Product(name = name , description = description ,price=price , quantity = quantity)

        if active != None:
            p.active = 1
        else:
            p.active = 0
        

        db.session.add(p)
        db.session.commit()


        file.save(f'static/covers/product/{p.id}.jpg')
        flash('محصول جدید با موفقیت اضافه شد ')
        return redirect('/admin/dashboard')


@app.route('/admin/dashboard/edit-product/<id>' , methods = ["GET","POST"])
def edit_product(id):
    product = Product.query.filter(Product.id == id).first_or_404()
    if request.method == "GET":
        return render_template("/admin/edit-product.html", product = product)
    else :
        name = request.form.get("name",None)
        description = request.form.get("description",None)
        quantity = request.form.get('quantity', None)
        price = request.form.get('price',None)
        active = request.form.get('active',None)
        file = request.files.get('cover', None)

        product.name = name
        product.description = description
        product.quantity = quantity
        product.price = price

        if active != None :
            product.active = 1
        else:
            product.active = 0            
        
        if file.filename != "":
            file.save(f'static/covers/product/{product.id}.jpg')
        db.session.commit()
        flash(' وضعیت محصول با موفقیت تغییر کرد ')
        return redirect('/admin/dashboard/product')

@app.route('/admin/dashboard/user',methods=["GET"])
def user():
    user = User.query.all()
    return render_template('/admin/user.html',user=user)

@app.route('/admin/dashboard/user/<id>' , methods = ["GET"])
def user_info(id):
    user = User.query.filter(User.id == id).first_or_404()
    return render_template('/admin/user-info.html', user = user)