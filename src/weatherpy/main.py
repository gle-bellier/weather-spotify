from infos import client_id, secret_key
import requests
import base64
import datetime
from urllib.parse import urlencode


class SpotifyAPI(object):
    URL = 'https://accounts.spotify.com/api/token'
    METHOD = "POST"

    def __init__(self, client_id, secret_key):
        super().__init__()
        self.access_token = None
        self.access_token_expires = datetime.datetime.now()
        self.access_token_expired = True
        self.client_id = None
        self.secret_key = None
        self.client_cred = base64.b64encode(
            (f"{client_id}:{secret_key}").encode())

    def get_token_headers(self):
        return {"Authorization": f"Basic {self.client_cred.decode()}"}

    def get_token_data(self):
        return {"grant_type": "client_credentials"}

    def get_auth(self):

        r = requests.post(self.URL,
                          data=self.get_token_data(),
                          headers=self.get_token_headers())
        valid_response = r.status_code in range(200, 299)
        if not valid_response: raise Exception("Authentication failed")
        else:
            data = r.json()

            self.access_token = data["access_token"]
            expires_in = data["expires_in"]
            self.access_token_expires = datetime.datetime.now(
            ) + datetime.timedelta(seconds=expires_in)

            self.access_token_expired = self.access_token_expires < datetime.datetime.now(
            )
            return True

    def get_access_token(self):
        token = self.access_token
        if self.access_token_expires < datetime.datetime.now():
            self.get_auth()
            return self.get_access_token()
        elif token == None:
            self.get_auth()
            return self.get_access_token()
        return token

    def search(self, query, search_type="artist"):
        self.get_access_token()
        headers = {"Authorization": f"Bearer {self.access_token}"}
        endpoint = "https://api.spotify.com/v1/search"

        data = urlencode({"q": query, "type": search_type.lower()})
        lookup_url = f"{endpoint}?{data}"

        r = requests.get(lookup_url, headers=headers)
        if not r.status_code in range(200, 299):
            return {}
        return r.json()


API = SpotifyAPI(client_id, secret_key)
print(API.search("Time", search_type="Track"))
print(API.access_token)
