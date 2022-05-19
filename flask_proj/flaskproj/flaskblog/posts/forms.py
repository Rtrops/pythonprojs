from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    updated_date = DateField('Date Updated',  default=datetime.utcnow)
    submit = SubmitField('Post')
