from flask import Flask, render_template, redirect
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
        
        redirect('/index')

    return render_template('authenticate.html', form=authenticationForm, title='Authentication')

@app.route("/index",methods=['POST', 'GET'])
def index():
    return render_template('index.html', title='Index')

if __name__ == '__main__':
    app.run(debug=True)