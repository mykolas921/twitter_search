import base64
import requests

from django.conf import settings

from .exceptions import TwitterAuthError

base_url = 'https://api.twitter.com/'

def get_access_token():
  auth_url = f'{base_url}oauth2/token'

  # Setup access credentials
  consumer_key = settings.TWITTER_CONSUMER_KEY
  consumer_secret = settings.TWITTER_CONSUMER_SECRET

  # Get the Access Token
  key_secret = f'{consumer_key}:{consumer_secret}'.encode('ascii')
  b64_encoded_key = base64.b64encode(key_secret)
  b64_encoded_key = b64_encoded_key.decode('ascii')

  auth_headers = {
    'Authorization': f'Basic {b64_encoded_key}',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
  }

  auth_data = {
    'grant_type': 'client_credentials'
  }

  auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

  if auth_resp.status_code == 200:
    return auth_resp.json()['access_token']
  else:
    raise TwitterAuthError("Twitter Auth Failed!", auth_resp.json(), status_code=auth_resp.status_code)
