# stl imports
from urllib.parse import urljoin
import requests

# third party imports
from flask import session

class API_URL:

    def getSubdomainURL(subdomain):
        return f'https://{ subdomain }.zendesk.com'

    def checkAPIState(base_url):
        response = requests.get(base_url)
        if response.ok:
            return response
        else:
            return None