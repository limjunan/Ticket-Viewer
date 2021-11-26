from flask import session, redirect, flash, render_template
from forms import AuthenticationForm
import requests, json

def getAuthorizationCode(client_id, client_url):
    session['client_id'] = client_id
    session['client_url'] = client_url

    # get oauth code
    redirect_url = f'https://{ client_url }.zendesk.com/oauth/authorizations/new?response_type=code&redirect_uri=http://127.0.0.1:5000&client_id={ client_id }&scope=read'
    return redirect(redirect_url)

def getAccessToken(code, client_id, client_secret, client_url):
    # get oauth access token
    redirect_url = f'https://{ client_url }.zendesk.com/oauth/tokens'
    headers={ 'Content-Type': 'application/json' }
    data={ "grant_type": "authorization_code",
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": "http://127.0.0.1:5000",
        "scope": "read" }

    access_token = requests.post(redirect_url, headers=headers, data=json.dumps(data))
    return access_token

