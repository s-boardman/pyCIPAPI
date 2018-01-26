"""Objects for authenticating with the GEL CIP API."""

from __future__ import print_function
import requests
from auth_credentials import auth_credentials


# get an authenticated session
class AuthenticatedSession(requests.Session):
    def __init__(self):
        requests.Session.__init__(self)
        self.authenticate()

    def authenticate(self):
        cip_auth_url = 'https://cipapi.genomicsengland.nhs.uk/api/2/get-token/'
        try:
            token = (self.post(
                        cip_auth_url, data=(auth_credentials))
                     .json()['token'])
            self.headers.update({"Authorization": "JWT " + token})
        except KeyError:
            print('Authentication Error')
        return self


# need a method to refresh the token after 30 mins
