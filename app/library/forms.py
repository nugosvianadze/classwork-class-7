from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import data_required


class ReviewCreateForm(FlaskForm):
    name = StringField('Name', validators=[data_required()])
    review = TextAreaField('Review', validators=[data_required()])
    submit = SubmitField('Submit')
