# local imports
from api_auth import *
from api_url import API_URL
from ticket_handler import TicketHandler
from api_auth import ApiAuthentication

# stl imports
import unittest,json
from unittest.mock import Mock, patch

class testAPIHandling(unittest.TestCase):

    # API CHECKING UNIT TESTS (api_url.py)

    @patch('api_url.requests.get')
    def test_CheckAPIState_OK_Response(self, mock_get):
        # configure the mock to return a response with an OK status code.
        mock_get.return_value.ok = True

        response = API_URL.checkAPIState(API_URL.getSubdomainURL(subdomain))

        self.assertIsNotNone(response)

    @patch('api_url.requests.get')
    def test_CheckAPIState_NotOK_Response(self, mock_get):
        # configure the mock to return a response with an OK status code.
        mock_get.return_value.ok = False

        response = API_URL.checkAPIState(API_URL.getSubdomainURL(subdomain))

        self.assertIsNone(response)


    # TICKET HANDLER UNIT TESTS (ticket_handler.py)

    @patch('ticket_handler.requests.get')
    def test_getTickets_OK_Response(self, mock_get):
        # configure the mock to return mock tickets json
        with open("mocks/mock_tickets.json") as f:
            mock_tickets = json.load(f)

        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = mock_tickets

        response = TicketHandler.getTickets('random access token', 'random url')

        self.assertListEqual(response['tickets'], mock_tickets['tickets'])

    @patch('ticket_handler.requests.get')
    def test_getTickets_NotOK_Response(self, mock_get):
        # configure the mock to not return a response with an OK status code.
        mock_get.return_value.ok = False

        response = TicketHandler.getTickets('random access token', 'random url')

        self.assertIsNone(response)

    @patch('ticket_handler.requests.get')
    def test_getTicket_OK_Response(self, mock_get):
        # configure the mock to return mock ticket json
        with open("mocks/mock_ticket.json") as f:
            mock_ticket = json.load(f)
        
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = mock_ticket

        response = TicketHandler.getTicket('random ticket id', 'random access token', 'random url')

        self.assertListEqual(response, mock_ticket['ticket'])
    
    @patch('ticket_handler.requests.get')
    def test_getTicket_NotOK_Response(self, mock_get):
        # configure the mock to not return a response with an OK status code.
        mock_get.return_value.ok = False

        response = TicketHandler.getTicket('random ticket id', 'random access token', 'random url')

        self.assertIsNone(response)
    
    @patch('ticket_handler.requests.get')
    def test_getTicketCount_OK_Response(self, mock_get):
        # configure the mock to return mock count json
        with open("mocks/mock_count.json") as f:
            mock_count = json.load(f)
        
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = mock_count

        response = TicketHandler.getTicketCount('random access token', 'random url')

        self.assertEqual(response, mock_count['count']['value'])
    
    @patch('ticket_handler.requests.get')
    def test_getTicketCount_NotOK_Response(self, mock_get):
        # configure the mock to not return a response with an OK status code.
        mock_get.return_value.ok = False

        response = TicketHandler.getTicketCount('random access token', 'random url')

        self.assertIsNone(response)

    # API AUTHENTICATION UNIT TESTS



if __name__ == '__main__':
    subdomain = input('Your subdomain: ')
    unittest.main()
