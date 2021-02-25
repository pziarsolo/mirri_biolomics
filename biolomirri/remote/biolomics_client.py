
from pprint import pprint
import time
import requests
from requests_oauthlib import OAuth2Session

from oauthlib.oauth2 import BackendApplicationClient, LegacyApplicationClient
from oauthlib.oauth2.rfc6749.errors import InvalidGrantError
from biolomirri.serializers import serialize_to_biolomics

SERVER_URL = "https://webservices.bio-aware.com/mirri_test"


class _BiolomicsClient:
    def _build_headers(self):
        self.get_access_token()
        return {
            "accept": "application/json",
            "websiteId": str(self.website_id),
            "Authorization": f"Bearer {self.access_token}",
        }

    def get_detail_url(self, end_point, record_id):
        return "/".join([self.server_url, 'data', end_point, str(record_id)])

    def get_list_url(self, end_point):
        return "/".join([self.server_url, 'data', end_point])

    def get_search_url(self, end_point):
        return "/".join([self.server_url, 'search', end_point])

    def get_find_by_name_url(self, end_point):
        return "/".join([self.get_search_url(end_point), 'findByName'])

    def search(self, end_point, search_query):
        header = self._build_headers()
        url = self.get_search_url(end_point)
        response = requests.post(url, json=search_query, headers=header)
        return response

    def retrieve(self, end_point, id):
        header = self._build_headers()
        url = self.get_detail_url(end_point, id)
        response = requests.put(url, headers=header)
        return response

    def create(self, end_point, data):
        header = self._build_headers()
        url = self.get_list_url(end_point)
        response = requests.post(url, json=data, headers=header)
        return response

    def update(self, end_point, id, data):
        header = self._build_headers()
        url = self.get_detail_url(end_point, id)
        response = requests.put(url, json=data, headers=header)
        return response

    def delete(self, end_point, id):
        header = self._build_headers()
        url = self.get_detail_url(end_point, id)
        response = requests.delete(url, headers=header)
        return response

    def find_by_name(self, end_point, name):
        header = self._build_headers()
        url = self.get_find_by_name_url(end_point)
        response = requests.get(url, headers=header, params={'name': name})
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 204:
            return None
        else:
            raise RuntimeError(f"{response.status_code}: {response.text}")


class BiolomicsClientBackend(_BiolomicsClient):
    def __init__(self, server_url, client_id, client_secret, website_id=1):
        self._auth_url = server_url + "/connect/token"
        self._client_id = client_id
        self._client_secret = client_secret
        self._client = None
        self.access_token = None
        self.website_id = website_id
        self.server_url = server_url

    def get_access_token(self):
        if self._client is None:
            self._client = BackendApplicationClient(client_id=self._client_id)
            authenticated = False
        else:
            expires_at = self._client.token["expires_at"]
            authenticated = False if expires_at < time.time() else True

        if not authenticated:
            oauth = OAuth2Session(client=self._client)
            token = oauth.fetch_token(
                token_url=self._auth_url,
                client_id=self._client_id,
                client_secret=self._client_secret,
            )
            oauth.close()
            self.access_token = token["access_token"]

        return self.access_token


class BiolomicsClientPassword(_BiolomicsClient):
    def __init__(self, server_url, client_id, client_secret, username, password,
                 website_id=1):
        self._client_id = client_id
        self._client_secret = client_secret
        self._username = username
        self._password = password
        self._client = None
        self.server_url = server_url
        self._auth_url = self.server_url + "/connect/token"
        self.access_token = None
        self.website_id = website_id
        # self.get_access_token()

    def get_access_token(self):
        if self._client is None:
            self._client = LegacyApplicationClient(client_id=self._client_id)
            authenticated = False
        else:
            expires_at = self._client.token["expires_at"]
            authenticated = False if expires_at < time.time() else True

        if not authenticated:
            oauth = OAuth2Session(client=self._client)
            try:
                token = oauth.fetch_token(
                    token_url=self._auth_url,
                    username=self._username,
                    password=self._password,
                    client_id=self._client_id,
                    client_secret=self._client_secret,
                )
            except InvalidGrantError:
                oauth.close()
                raise
            self.access_token = token["access_token"]
            oauth.close()
        return self.access_token


def get_schema(url, token):
    headers = {
        "accept": "*/*",
        "websiteId": "1",
        "Authorization": f"Bearer {token['access_token']}",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"{response.status_code}: {response.text}")


class BiolomicsMirriCLientStrainMixin:
    def retrieve_strain_by_accession_number(self, accession_number):
        query = {
            "Query": [
                {
                    "Index": 0,
                    "FieldName": "Collection accession number",
                    "Operation": "TextExactMatch",
                    "Value": accession_number,
                }
            ],
            "Expression": "Q0",
            "DisplayStart": 0,
            "DisplayLength": 10,
        }

        response = self.client.search('Strains', search_query=query)
        if response.status_code == 200:
            result = response.json()
            total = result["TotalCount"]
            if total == 0:
                return None
            elif total == 1:
                return result["Records"][0]
            else:
                msg = "More than one entries for {accession_number} in database"
                raise ValueError(msg)

        else:
            raise ValueError(f"{response.status_code}: {response.text}")

    def create_strain(self, strain):
        strain_id = strain.id.strain_id
        strain_in_ws = self.retrieve_strain_by_accession_number(strain_id)
        if strain_in_ws:
            raise RuntimeError(f'{strain_id} already in DB')

        data = serialize_to_biolomics(strain, client=self)
        response = self.client.create('Strains', data=data)
        if response.status_code == 200:
            return response.json()
        else:
            msg = f"return_code: {response.status_code}. msg: {response.text}"
            raise RuntimeError(msg)

    def update_strain(self, record_id, strain):
        data = serialize_to_biolomics(strain, client=self)
        response = self.client.update('Strains', record_id, data)
        if response.status_code == 200:
            return response.json()
        else:
            msg = f"return_code: {response.status_code}. msg: {response.text}"
            raise RuntimeError(msg)

    def remove_strain(self, record_id):
        response = self.client.delete('Strains', record_id)
        if response.status_code != 200:
            error = response.json()
            # msg = f'{error["Title"]: {error["Details"]}}'
            raise RuntimeError(error)


class BiolomicsMirriCLientGrowtMediaMixin:

    def retrieve_growth_medium_by_name(self, medium_name):
        growth_medium = self.client.find_by_name('WS Growth media',
                                                 name=medium_name)
        return growth_medium


class BiolomicsMirriClient(BiolomicsMirriCLientStrainMixin,
                           BiolomicsMirriCLientGrowtMediaMixin):
    def __init__(self, server_url, client_id, client_secret, username=None,
                 password=None, website_id=1):
        if username is None or password is None:
            _client = BiolomicsClientBackend(server_url, client_id,
                                             client_secret, website_id=website_id)
        else:
            _client = BiolomicsClientPassword(server_url, client_id,
                                              client_secret, username,
                                              password, website_id=website_id)
        self.client = _client
