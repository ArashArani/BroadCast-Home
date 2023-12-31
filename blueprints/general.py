# کتاب خانه ها 

from flask import Blueprint , request , render_template 

#فایل ها

from models.product import *

from models.course import *

from models.exprience import *

app = Blueprint('general',__name__)


@app.route('/', methods=["GET"])
def main():
    if request.method == "GET":
        courses = Course.query.filter(Course.active==1).order_by(func.random()).limit(6).all()
        experiences = Experience.query.filter(Experience.active ==1).order_by(func.random()).limit(5).all()
    return render_template('main.html', courses = courses , experiences = experiences)

@app.route('/course/<int:id>/<name>',methods=["GET"])
def course(id,name):
    course = Course.query.filter(Course.id == id).filter(Course.name == name).filter(Course.active==1).first_or_404()
    another_course = Course.query.order_by(func.random()).limit(3).all()
    return render_template('course.html',course=course,another_course=another_course)


@app.route('/experience/<int:id>/<name>',methods=["GET"])
def experience(id,name):
    experience = Experience.query.filter(Experience.id == id).filter(Experience.name == name).filter(Experience.active==1).first_or_404()
    another_experience = Experience.query.order_by(func.random()).limit(3).all()
    return render_template('experience.html',experience=experience,another_experience=another_experience)