import requests

def getTickets(access_token, client_url):
    # get tickets information json
    redirect_url = f'https://{ client_url }.zendesk.com/api/v2/tickets.json'
    headers={'Authorization': f'Bearer { access_token }'}
    tickets = requests.get(redirect_url, headers=headers)
    ticketsJSON = tickets.json()
    return ticketsJSON['tickets']

def getTicket(ticket_id, access_token, client_url):
    # get ticket information json
    redirect_url = f'https://{ client_url }.zendesk.com/api/v2/tickets/{ticket_id}.json'
    headers={'Authorization': f'Bearer { access_token }'}
    tickets = requests.get(redirect_url, headers=headers)
    ticketsJSON = tickets.json()
    return ticketsJSON['ticket']
