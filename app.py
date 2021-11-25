from os import access
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
        session['client_id'] = authenticationForm.client_id.data
        session['client_secret'] = authenticationForm.client_secret.data
        session['client_url'] = authenticationForm.client_url.data
        authorizationCode = getAuthorizationCode(session['client_id'],
                                                 session['client_url'])
        return authorizationCode
        
    if request.args.get('code'):
        accessToken = getAccessToken(request.args.get('code'),
                             session['client_id'],
                             session['client_secret'],
                             session['client_url'])
        if accessToken.status_code == 200:
            return render_template('index.html', title='Index', tickets = getTickets(accessToken, session['client_url']))
        else:
            flash(f'ERROR { accessToken["error"] }: { accessToken["error_description"] }', 'error')
            return render_template('authenticate.html', form=AuthenticationForm(), title='Authentication')

    return render_template('authenticate.html', form=authenticationForm, title='Authentication')

if __name__ == '__main__':
    app.run(debug=True)