from urllib import parse
from flask import Flask
import requests


CALLBACK_ROUTE = '/oauth/callback'


class DiscordAuth:
    def __init__(
        self,
        scope='identify',
    ):
        self.redirect_uri = None
        self.client_id = None
        self.client_secret = None
        self.scope = scope

        self.base_url = "https://discord.com"
        self.access_token_url = f'{self.base_url}/api/oauth2/token'
        self.authorize_url = f'{self.base_url}/oauth2/authorize'
        self.api_base_url = f'{self.base_url}/api/v10'

    def init_app(self, app: Flask):
        self.redirect_uri = (
            app.config['FULL_URL']
            + CALLBACK_ROUTE
        )
        self.client_id = app.config['DISCORD_CLIENT_ID']
        self.client_secret = app.config['DISCORD_SECRET_KEY']
        self.oauth_url = self.generate_oauth_url()

    def generate_oauth_url(self):
        params = {
            'scope': self.scope,
            'client_id':  self.client_id,
            'redirect_uri': self.redirect_uri,
            'response_type': 'code'
        }
        return f'{self.authorize_url}?{parse.urlencode(params)}'

    def access_token(self, code):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        r = requests.post(self.access_token_url, data=data, headers=headers)
        r.raise_for_status()
        return r.json()['access_token']

    def get_current_user(self, token):
        header = {
            'User-Agent': 'crater-baiter v0',
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        r = requests.get(self.api_base_url + '/users/@me', headers=header)
        return r.json()
