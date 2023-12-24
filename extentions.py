from flask_sqlalchemy import SQLAlchemy

import time

from flask_wtf import FlaskForm

from wtforms import SelectField, StringField, SubmitField

from wtforms.validators import DataRequired


db = SQLAlchemy()


def get_current_time():
    return round(time.time())


class CategoryForm(FlaskForm):
    category = SelectField('Category', choices=[], coerce=int)
    new_category = StringField('New Category')
    submit = SubmitField('Upload')


class EditForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    course = StringField('Course', validators=[DataRequired()])
    video_url = StringField('Video URL', validators=[DataRequired()])
    submit = SubmitField('Update')
