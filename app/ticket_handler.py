# stl imports
import requests

class TicketHandler:
    # this class defines all ticket related functions

    def getTickets(access_token, client_url, prev=None, next=None):
        # get tickets information json
        if next:
            redirect_url = next
        elif prev:
            redirect_url = prev
        else:
            redirect_url = f'https://{ client_url }.zendesk.com/api/v2/tickets.json?page[size]=25'
        headers={'Authorization': f'Bearer { access_token }'}
        tickets = requests.get(redirect_url, headers=headers)
        if tickets.ok:
            ticketsJSON = tickets.json()
            return ticketsJSON
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

    def getTicketCount(access_token, client_url):
        # get ticket count
        redirect_url = f'https://{ client_url }.zendesk.com/api/v2/tickets/count.json'
        headers={'Authorization': f'Bearer { access_token }'}
        ticket_count = requests.get(redirect_url, headers=headers)
        if ticket_count.ok:
            return ticket_count.json()['count']['value']
        else:
            return None
