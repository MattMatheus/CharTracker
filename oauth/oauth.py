import requests
import os
import secrets
import urllib.parse

from .models import UserAuthDetails
from django.http import HttpResponse, HttpResponseRedirect
from dotenv import load_dotenv

load_dotenv(override=True)
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

authorization_base_url = "https://oauth.battle.net/authorize"
redirect_uri = "http://localhost:8000/oauth/callback"
token_base_uri = "https://us.battle.net/oauth/token"

if client_id is None:
    raise ValueError("CLIENT_ID environment variable is not set")

if client_secret is None:
    raise ValueError("CLIENT_ID environment variable is not set")


def generate_state_string(length=16):
    # Generate a secure random string of the specified length
    return secrets.token_urlsafe(length)


async def process_login(request):
    scope = "wow.profile"
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": scope,
        "state": generate_state_string(length=16),
    }

    url = f"{authorization_base_url}?{urllib.parse.urlencode(params)}"

    return HttpResponseRedirect(redirect_to=url)


def callback(request):
    code = request.GET.get("code", None)
    if not code:
        return HttpResponse("Missing authorization code", status=400)

    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret,
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    url = f"{token_base_uri}?{urllib.parse.urlencode(token_data)}"

    try:
        response = requests.post(url, data=token_data, headers=headers)
        response.raise_for_status()
        response_data = response.json()

        access_token = response_data.get("access_token")
        expires_in = response_data.get("expires_in")
        scope = response_data.get("scope")
        sub = response_data.get("sub")

        token_data = UserAuthDetails(
            token=access_token, refresh_token=expires_in, scope=scope, sub=sub
        )
        token_data.save()

        return HttpResponse(str(access_token), status=200)

    except requests.RequestException as e:
        return HttpResponse(str(e), status=500)


def purge_auth(request):
    UserAuthDetails.objects.all().delete()
    return HttpResponse("Success", status=200)
