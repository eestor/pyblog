

from flask_wtf import FlaskForm
from flask_pagedown.fields import PageDownField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    #body = StringField('Enter your comment', validators=[DataRequired()])
    body = PageDownField('Enter your comment', validators=[DataRequired()])
    submit = SubmitField('Submit')