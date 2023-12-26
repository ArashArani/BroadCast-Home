# کتاب خانه ها 

from flask import Blueprint , request , render_template 

#فایل ها

from models.product import *


app = Blueprint('general',__name__)


@app.route('/')
def main():
    search = request.args.get('search',None)
    products = Product.query.filter(Product.active == 1)
    products = products.order_by(func.random()).all()
    
    return render_template('main.html' , products = products )

@app.route('/product/<int:id>/<name>')
def product(id,name):
    product = Product.query.filter(Product.id == id).filter(Product.name == name).filter(
        Product.active == 1).first_or_404()
    another_products = Product.query.filter(Product.name.like(f'%{product.name[0:3]}%')).order_by(func.random()).limit(3).all()
    return render_template('/product.html' , product = product ,another_products = another_products)



@app.route('/about')
def about():
    return render_template('/about.html')

@app.app_errorhandler(404)
def page_not_found(error):
    return render_template('/404.html'), 404