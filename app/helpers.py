import requests

from requests.auth import HTTPBasicAuth

OAUTH_URL = "https://us.battle.net/oauth/token"


def get_access_token(client_id, client_secret):
    data = {"grant_type": "client_credentials"}
    response = requests.post(OAUTH_URL, data=data, auth=(client_id, client_secret))
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception("Failed to retrieve access token")


def get_authorized_scope(client_id, client_secret):
    code = get_access_token(client_id, client_secret)
    print(code)
    data = {
        "redirect_uri": "http://localhost/success",
        "scope": "wow.profile",
        "grant_type": "authorization_code",
        "code": code,
    }
    response = requests.post(
        OAUTH_URL, auth=HTTPBasicAuth(client_id, client_secret), data=data
    )
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(
            f"Failed to retrieve access token with authorization code: {response.text}"
        )
