from os import access
from urllib import parse
from flask import Flask, render_template, redirect, request, session, flash, url_for
from forms import AuthenticationForm
from api_auth import *
from ticket_handler import *
from urllib.parse import unquote, unquote_plus, parse_qs
from json import dumps

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
            accessTokenJSON = accessToken.json()
            session['access_token'] = accessTokenJSON['access_token']
            return(redirect(url_for('listTickets')))
        else:
            flash('ERROR: invalid client secret', 'error')
            return render_template('authenticate.html', form=AuthenticationForm(), title='Authentication')

    return render_template('authenticate.html', form=authenticationForm, title='Authentication')

@app.route('/index')
def listTickets():
    tickets = getTickets(session['access_token'], session['client_url'])
    return render_template('index.html', title='Index', tickets=tickets)

@app.route('/ticket', methods=['GET', 'POST'])
def displayTicket():
    if session['access_token']:
        ticketid = request.args.get('ticketid')
        print('         ',ticketid)
        ticket = getTicket(ticketid, session['access_token'], session['client_url'])
        return render_template('ticket.html', ticket=ticket, title='ticket')
    else:
        flash('ERROR: access code', 'error')
        return redirect(url_for('authenticate'))


if __name__ == '__main__':
    app.run(debug=True)