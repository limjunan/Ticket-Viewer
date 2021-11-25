from flask import session, redirect, flash, render_template
import requests, json

def getAuthorizationCode(authenticationForm):
    session['client_id'] = authenticationForm.client_id.data
    session['client_secret'] = authenticationForm.client_secret.data
    session['client_url'] = authenticationForm.client_url.data

    # get oauth code
    redirect_url = f'https://{ session["client_url"] }.zendesk.com/oauth/authorizations/new?response_type=code&redirect_uri=http://127.0.0.1:5000&client_id={ session["client_id"]}&scope=read'
    return redirect(redirect_url)

def getTickets(code):
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