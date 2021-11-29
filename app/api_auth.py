'''
    All API Authentication functions will be stored here
'''

# third party imports
from flask import redirect

# stl imports
import requests, json

class ApiAuthentication:
    # this class defines all authentication related functions

    def getSubdomainURL(subdomain):
        return f'https://{ subdomain }.zendesk.com'

    def checkAPIState(base_url):
        # check if API or subdomain is active
        try:
            response = requests.get(base_url, timeout=10)
        except requests.exceptions.ConnectionError:
            return None

        if response.ok:
            return response
        else:
            return None

    def getAuthorizationCode(client_id, client_url):
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

