from flask import Flask, render_template
from flask.templating import render_template
import requests

from forms import AuthenticationForm

app = Flask(__name__)

# secret key for CSRF protection
app.config['SECRET_KEY'] = 'b8aZENDESKffba7ea03b21aZENDESK93'

# main application route
@app.route("/")
def authenticate():
    authenticationForm = AuthenticationForm()
    return render_template('authenticate.html', form=authenticationForm)

@app.route("/index")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)