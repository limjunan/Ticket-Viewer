from os import access
from flask import Flask, render_template, redirect, request, session, flash
from flask.helpers import url_for
from user import User
import requests, json


from forms import AuthenticationForm

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

        # get oauth code
        redirect_url = f'https://{ session["client_url"] }.zendesk.com/oauth/authorizations/new?response_type=code&redirect_uri=http://127.0.0.1:5000&client_id={ session["client_id"]}&scope=read'
        return redirect(redirect_url)
        

    if request.args.get('code'):
        
        code = request.args.get('code')
        # get oauth access token
        redirect_url = f'https://{ session["client_url"] }.zendesk.com/oauth/tokens'
        headers={ 'Content-Type': 'application/json'}
        data={"grant_type": "authorization_code",
            "code": code,
            "client_id": session["client_id"],
            "client_secret": session["client_secret"],
            "redirect_uri": "http://127.0.0.1:5000",
            "scope": "read" }

        accessToken = requests.post(redirect_url, headers=headers, data=json.dumps(data))
        accessToken = accessToken.json()
        
        if 'access_token' in accessToken:
            access_token = accessToken['access_token']

            # get tickets information json
            redirect_url = f'https://{ session["client_url"] }.zendesk.com/api/v2/tickets.json'
            headers={'Authorization': f'Bearer {access_token}'}
            tickets = requests.get(redirect_url, headers=headers)
            ticketsJSON = tickets.json()
            return render_template('index.html', title='Index', tickets = ticketsJSON['tickets'])
        elif 'error' in accessToken:
            flash(f'ERROR: { accessToken["error"] }', 'error')

    return render_template('authenticate.html', form=authenticationForm, title='Authentication')

if __name__ == '__main__':
    app.run(debug=True)