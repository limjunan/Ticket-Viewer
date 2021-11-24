from flask import Flask, render_template, redirect
from user import User
import requests

from forms import AuthenticationForm

app = Flask(__name__)

# secret key for CSRF protection
app.config['SECRET_KEY'] = 'b8aZENDESKffba7ea03b21aZENDESK93'

# main application route
@app.route("/", methods=['POST', 'GET'])
def authenticate():
    authenticationForm = AuthenticationForm()

    if authenticationForm.validate_on_submit():
        user = User(authenticationForm.client_id.data, authenticationForm.client_secret.data, 
                    authenticationForm.client_url.data)
        
        redirect(f'https://{user.client_url}.zendesk.com/oauth/authorizations/new?response_type=code&redirect_uri=http://127.0.0.1:5000&client_id={user.client_id}&scope=read')

    return render_template('authenticate.html', form=authenticationForm, title='Authentication')

@app.route("/index",methods=['POST', 'GET'])
def index():
    return render_template('index.html', title='Index')

if __name__ == '__main__':
    app.run(debug=True)