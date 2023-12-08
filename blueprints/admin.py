# کتاب خانه ها 
import os
from flask import Blueprint , session , request , abort , redirect , render_template , flash , url_for 
#فایل ها 
from models.article import Article
from models.exprience import Experience
from models.news import News
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