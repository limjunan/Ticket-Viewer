from flask import Flask, render_template, redirect, request, session, flash
from forms import AuthenticationForm
from api_auth import *

app = Flask(__name__)

# secret key for CSRF protection
app.config['SECRET_KEY'] = 'b8aZENDESKffba7ea03b21aZENDESK93'

# main application route
@app.route("/", methods=['POST', 'GET'])
def authenticate():
    authenticationForm = AuthenticationForm()

    if authenticationForm.validate_on_submit():
        authorizationCode = getAuthorizationCode(authenticationForm)
        return authorizationCode
        
    if request.args.get('code'):
        code = request.args.get('code')
        return getTickets(code)

    return render_template('authenticate.html', form=authenticationForm, title='Authentication')

if __name__ == '__main__':
    app.run(debug=True)