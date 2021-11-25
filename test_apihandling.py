from api_auth import *
import unittest

class testAPIHandling(unittest.TestCase):
     def test_getAuthCode(self):
         self.assertTrue(getAuthorizationCode(client_id, subdomain))
        

if __name__ == '__main__':
    subdomain = input('Your subdomain: ')
    client_id = input('Your OAUTH ID: ')
    client_secret = input('Your OAUTH secret: ')
    unittest.main()
