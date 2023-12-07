# کتاب خانه ها 

from flask import Blueprint

app = Blueprint('general',__name__)

@app.route('/')
def general():
    return ' general '