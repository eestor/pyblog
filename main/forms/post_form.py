

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Required

class PostForm(FlaskForm):
    body = TextAreaField("What's on your mind?", validators=[ DataRequired() ])
    submit = SubmitField('Submit')
