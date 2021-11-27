# third party imports
from flask import Flask, render_template, redirect, request, session, flash, url_for

# local imports
from forms import AuthenticationForm
from api_auth import *
from ticket_handler import *
from api_url import *
from constants import *

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

        # error handling for down api
        if API_URL.checkAPIState(API_URL.getSubdomainURL(session['client_url'])) is None:
            flash('ERROR: API is down', 'error')
            return render_template('authenticate.html', form=AuthenticationForm(), title='Authentication')

        authorizationCode = ApiAuthentication.getAuthorizationCode(session['client_id'],
                                                session['client_url'])
        return authorizationCode
        
    if request.args.get('code'):
        accessToken = ApiAuthentication.getAccessToken(request.args.get('code'),
                            session['client_id'],
                            session['client_secret'],
                            session['client_url'])
        
        if accessToken.ok:
            accessTokenJSON = accessToken.json()
            session['access_token'] = accessTokenJSON['access_token']
            return(redirect(url_for('listTickets')))
        else:
            flash('ERROR: invalid client secret', 'error')
            return render_template('authenticate.html', form=AuthenticationForm(), title='Authentication')

    return render_template('authenticate.html', form=authenticationForm, title='Authentication')

@app.route('/index')
def listTickets():

    # retrieve ticket count 
    ticket_count = TicketHandler.getTicketCount(session['access_token'], session['client_url'])
    if ticket_count:
        session['ticket_count'] = ticket_count
    else:
        flash('ERROR: unable to retrieve ticket count', 'error')

    # pagination
    if request.args.get('next'):
        tickets = TicketHandler.getTickets(session['access_token'], session['client_url'], next=request.args.get('next'))
    elif request.args.get('prev'):
        tickets = TicketHandler.getTickets(session['access_token'], session['client_url'], prev=request.args.get('prev'))
    else:
        tickets = TicketHandler.getTickets(session['access_token'], session['client_url'])

    if tickets:
        if ticket_count > Constants.items_per_page:
            return render_template('index.html', title='Index', tickets=tickets['tickets'], 
                                    next=tickets['links']['next'], prev=tickets['links']['prev'],
                                    ticket_count=ticket_count)
        else:
            return render_template('index.html', title='Index', tickets=tickets['tickets'])
    else:
        flash('ERROR: Tickets retrieval not successful', 'error')
        return redirect(url_for('authenticate'))


@app.route('/ticket', methods=['GET', 'POST'])
def displayTicket():
    if session['access_token']:
        ticketid = request.args.get('ticketid')
        ticket = TicketHandler.getTicket(ticketid, session['access_token'], session['client_url'])
        if ticket:
            return render_template('ticket.html', ticket=ticket, title='ticket')
        else:
            flash('ERROR: access code', 'error')
            return redirect(url_for('authenticate'))
    else:
        flash('ERROR: access code', 'error')
        return redirect(url_for('authenticate'))


if __name__ == '__main__':
    app.run(debug=True)