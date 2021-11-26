# stl imports
import requests

class TicketHandler:
    # this class defines all ticket related functions

    def getTickets(access_token, client_url):
        # get tickets information json
        redirect_url = f'https://{ client_url }.zendesk.com/api/v2/tickets.json'
        headers={'Authorization': f'Bearer { access_token }'}
        tickets = requests.get(redirect_url, headers=headers)
        if tickets.ok:
            ticketsJSON = tickets.json()
            return ticketsJSON['tickets']
        else:
            return None

    def getTicket(ticket_id, access_token, client_url):
        # get ticket information json
        redirect_url = f'https://{ client_url }.zendesk.com/api/v2/tickets/{ticket_id}.json'
        headers={'Authorization': f'Bearer { access_token }'}
        ticket = requests.get(redirect_url, headers=headers)
        if ticket.ok:
            ticketJSON = ticket.json()
            return ticketJSON['ticket']
        else:
            return None
