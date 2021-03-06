'''
    Main application code
'''

# third party imports
from flask import Flask, render_template, redirect, request, session, flash, url_for

# local imports
from forms import AuthenticationForm
from api_auth import *
from ticket_handler import *
from constants import *

app = Flask(__name__)

# secret key for CSRF protection
app.config['SECRET_KEY'] = 'b8aZENDESKffba7ea03b21aZENDESK93'

# main application route
@app.route("/", methods=['POST', 'GET'])
def authenticate():

    # form to get required user information for API authentication
    authenticationForm = AuthenticationForm()

    if authenticationForm.validate_on_submit(): # when form is submitted

        # authentication data is stored in session 
        session['client_id'] = authenticationForm.client_id.data
        session['client_secret'] = authenticationForm.client_secret.data
        session['client_url'] = authenticationForm.client_url.data

        # error handling for down api
        if ApiAuthentication.checkAPIState(ApiAuthentication.getSubdomainURL(session['client_url'])) is None:
            flash('<b>Error</b></br> Either the API is down, or you could not be authenticated', 'error')
            return render_template('authenticate.html', form=AuthenticationForm(), title='Authentication')

        # get authorization code
        authorizationCode = ApiAuthentication.getAuthorizationCode(session['client_id'],
                                                session['client_url'])
        return authorizationCode
        
    if request.args.get('code'): # when authorization code is get

        # get access token
        accessToken = ApiAuthentication.getAccessToken(request.args.get('code'),
                            session['client_id'],
                            session['client_secret'],
                            session['client_url'])
        
        # access token error handling
        if accessToken.ok:
            accessTokenJSON = accessToken.json()
            session['access_token'] = accessTokenJSON['access_token']
            return(redirect(url_for('listTickets')))
        else:
            flash('<b>Error</b></br> Invalid client secret', 'error')
            return render_template('authenticate.html', form=AuthenticationForm(), title='Authentication')

    return render_template('authenticate.html', form=authenticationForm, title='Authentication')

# list tickets route
@app.route('/index')
def listTickets():

    # access token error handling
    try:
        session['access_token']
    except KeyError:
        flash('<b>Error</b></br> Invalid access token', 'error')
        return redirect(url_for('authenticate'))     

    
    # retrieve ticket count 
    ticket_count = TicketHandler.getTicketCount(session['access_token'], session['client_url'])
    if ticket_count: # ticket count error handling
        session['ticket_count'] = ticket_count
    else:
        flash('<b>Error</b></br> Unable to retrieve ticket count', 'error')

    # pagination when retrieving tickets
    if request.args.get('next'):
        # store current page to redirect back from ticket
        session['current_page'] = request.args.get('next')
        tickets = TicketHandler.getTickets(session['access_token'], session['client_url'], next=request.args.get('next'))
    elif request.args.get('prev'):
        # store current page to redirect back from ticket
        session['current_page'] = request.args.get('prev')
        tickets = TicketHandler.getTickets(session['access_token'], session['client_url'], prev=request.args.get('prev'))
    else:
        tickets = TicketHandler.getTickets(session['access_token'], session['client_url'])
    
    # tickets error handling
    if tickets:
        if ticket_count > Constants.ITEMS_PER_PAGE: # pagination when more tickets than items per page
            return render_template('index.html', title='Index', tickets=tickets['tickets'], 
                                    next=tickets['links']['next'], prev=tickets['links']['prev'],
                                    ticket_count=ticket_count)
        else:
            return render_template('index.html', title='Index', tickets=tickets['tickets'])
    else:
        flash('<b>Error</b></br> Tickets retrieval not successful', 'error')
        return redirect(url_for('authenticate'))

# individual ticket route
@app.route('/ticket', methods=['POST', 'GET'])
def displayTicket():
    # indiv ticket error handling
    try:
        session['access_token']
    except KeyError:
        flash('<b>Error</b></br> Invalid access code', 'error')
        return redirect(url_for('authenticate'))
        
    ticketid = request.args.get('ticketid')
    ticket = TicketHandler.getTicket(ticketid, session['access_token'], session['client_url'])
    if ticket:
        print(ticket)
        return render_template('ticket.html', ticket=ticket, title='ticket')
    else:
        flash('<b>Error</b></br> Ticket not found', 'error')
        return redirect(url_for('authenticate'))

# 404 page not found route
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)