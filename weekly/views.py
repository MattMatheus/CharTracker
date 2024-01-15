from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import WeeklyCharProgress
from oauth.models import UserAuthDetails

import requests
import urllib.parse

mattsub = "52039343"
api_base_url = "https://us.api.blizzard.com"
profile_url_endpoints = {
    "profile_summary": "/profile/user/wow", #returuns a list of characters
    "mount_summary": "/profile/user/wow/collections/mounts", #returns a list of mounts
    "pet_summary": "/profile/user/wow/collections/pets", #returns a list of pets
    "completed_quests": "/profile/user/wow/quests/completed", #returns a list of completed quests    
}


def index(request):
    weekly_char_progresses = WeeklyCharProgress.objects.all()
    context = {"weekly_char_progresses": weekly_char_progresses}
    authinfo = UserAuthDetails.objects.get(sub=mattsub)
    return HttpResponse(authinfo.sub)
    # return render(request, "weekly/index.html", context)
    

def get_auth_token(request):
    authinfo = UserAuthDetails.objects.get(sub=mattsub)
    request_data = {
        "access_token": authinfo.token,
        "region": "us",
        "namespace": "profile-us",
        "locale": "en_US",
    }
    return request_data


def check_weekly_quests(request):
    charname = request.GET.get("character", None)
    realm = request.GET.get("realm", "lightbringer")
    request_data = get_auth_token(request)
    quest_list = [78319, 78821, 78444]
    progress = WeeklyCharProgress
    uri = f"https://us.api.blizzard.com/profile/wow/character/{realm}/{charname}/quests/completed"
    
    

def get_quests(request):
    charname = request.GET.get("character", None)
    uri = f"https://us.api.blizzard.com/profile/wow/character/lightbringer/{charname}/achievements/statistics"
    authinfo = UserAuthDetails.objects.get(sub=mattsub)

    request_data = {
        "access_token": authinfo.token,
        "region": "us",
        "namespace": "profile-us",
        "locale": "en_US",
    }

    url = f"{uri}?{urllib.parse.urlencode(request_data)}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        chardata = response.json()
        return JsonResponse(chardata)
    except requests.RequestException as e:
        return HttpResponse(f"Uh-oh, we hit error {e.response.status_code}", str(e))
