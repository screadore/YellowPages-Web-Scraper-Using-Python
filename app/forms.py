from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FieldList, FormField
from wtforms.validators import InputRequired, Optional


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    submit = SubmitField('Login')

# Implemented manual validation instead, until validation for FieldList solution is found
class ScrapeForm(FlaskForm):
    search_terms = FieldList(StringField('Term: ', [Optional(strip_whitespace=True)]), min_entries=1, max_entries=10)
    search_locations = FieldList(StringField('Location: ', [InputRequired(message='Please enter a search location.')]), min_entries=1, max_entries=10)
