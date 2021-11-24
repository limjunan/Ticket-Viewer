class User():
    def __init__(self, client_id, client_secret, client_url, code=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_url = client_url