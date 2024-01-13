from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import urllib.parse
import os
import auth
import requests

load_dotenv()
app = FastAPI()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
matt_code = os.getenv("MATT_CODE")
access_token = os.getenv("ACCESS_TOKEN")

scope = "wow.profile"

authorization_base_url = "https://oauth.battle.net/authorize"
redirect_uri = "http://localhost:8000/callback"
token_uri = "https://us.battle.net/oauth/token"

if client_id is None:
    raise ValueError("CLIENT_ID environment variable is not set")


@app.get("/login")
async def login():
    # Define the parameters
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": scope,
        "state": auth.generate_state_string(length=16),
    }

    # Construct the authorization URL
    url = f"{authorization_base_url}?{urllib.parse.urlencode(params)}"

    # Redirect the user to the authorization URL
    return RedirectResponse(url=url)


@app.get("/callback")
async def callback(code: str = Query(None)):
    if not code:
        raise HTTPException(status_code=400, detail="Missing authorization code")

    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret,
    }

    try:
        response = requests.post(token_uri, data=token_data)
        response.raise_for_status()
        access_token_data = response.json()
        return access_token_data
    except requests.RequestException as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@app.get("/listchars")
async def get_characters():
    if not access_token:
        raise HTTPException(
            status_code=401, detail="Unauthorized, please generate a code"
        )

    uri = "https://us.api.blizzard.com/profile/user/wow"

    request_data = {
        "access_token": access_token,
        "region": "us",
        "namespace": "profile-us",
        "locale": "en_US",
    }

    url = f"{uri}?{urllib.parse.urlencode(request_data)}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        chardata = response.json()
        return chardata
    except requests.RequestException as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@app.get("/listgear")
async def list_gear(charname: str = Query(None, description="Character name")):
    if charname is None:
        raise HTTPException(status_code=400, detail="Missing query parameter 'param'")

    if not access_token:
        raise HTTPException(
            status_code=401, detail="Unauthorized, please generate a code"
        )

    uri = f"https://us.api.blizzard.com/profile/wow/character/lightbringer/{charname}/equipment"

    request_data = {
        "access_token": access_token,
        "region": "us",
        "namespace": "profile-us",
        "locale": "en_US",
    }

    url = f"{uri}?{urllib.parse.urlencode(request_data)}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        chardata = response.json()
        return chardata
    except requests.RequestException as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@app.get("/checkquest")
async def check_quest(charname: str):
    if charname is None:
        raise HTTPException(status_code=400, detail="Missing query parameter 'param'")

    if not access_token:
        raise HTTPException(
            status_code=401, detail="Unauthorized, please generate a code"
        )

    uri = f"https://us.api.blizzard.com/profile/wow/character/lightbringer/{charname}/quests/completed"

    request_data = {
        "access_token": access_token,
        "region": "us",
        "namespace": "profile-us",
        "locale": "en_US",
    }

    url = f"{uri}?{urllib.parse.urlencode(request_data)}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        chardata = response.json()
        return chardata
    except requests.RequestException as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
