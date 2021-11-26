# third party imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class AuthenticationForm(FlaskForm):
    client_id = StringField('Client ID: ', validators=[DataRequired()])
    client_secret = PasswordField('Client Secret: ', validators=[DataRequired()])
    client_url = StringField('Subdomain: ', validators=[DataRequired()])
    submit = SubmitField('Authenticate')