from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import WeeklyCharProgress
from oauth.models import UserAuthDetails

import requests
import urllib.parse

mattsub = "52039343"
api_base_url = "https://us.api.blizzard.com"
profile_url_endpoints = {
    "profile_summary": "/profile/user/wow",  # returuns a list of characters
    "mount_summary": "/profile/user/wow/collections/mounts",  # returns a list of mounts
    "pet_summary": "/profile/user/wow/collections/pets",  # returns a list of pets
    "completed_quests": "/profile/user/wow/quests/completed",  # returns a list of completed quests
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

@login_required
def check_weekly_quests(request):
    charname = request.GET.get("character", None)
    realm = request.GET.get("realm", "lightbringer")
    request_data = get_auth_token(request)
    query_result = WeeklyCharProgress(
        char_name=charname,
        superbloom=False,
        rep_weekly=False,
        dream_seeds=False,
        raidfinder_1=False,
        raidfinder_2=False,
        raidfinder_3=False,
        raidfinder_4=False,
    )
    uri = f"https://us.api.blizzard.com/profile/wow/character/{realm}/{charname}/quests/completed"
    url = f"{uri}?{urllib.parse.urlencode(request_data)}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        questdata = response.json()
        for quest in questdata["quests"]:
            if quest["id"] == 78319:
                query_result.dream_seeds = True
            if quest["id"] == 78821:
                query_result.rep_weekly = True
            if quest["id"] == 78444:
                query_result.superbloom = True
        query_result.save()
        progress = [WeeklyCharProgress.objects.filter(char_name=charname).latest("id")]
        #return HttpResponse(progress_object)
        return render(request, "weekly/index.html", {"progress": progress})


    except requests.RequestException as e:
        return HttpResponse(f"Uh-oh, we hit error {e.response.status_code}", str(e))


def get_quests(request):
    charname = request.GET.get("character", None)
    id = int(request.GET.get("id", None))
    realm = request.GET.get("realm", "lightbringer")
    uri = f"https://us.api.blizzard.com/profile/wow/character/{realm}/{charname}/quests/completed"
    request_data = get_auth_token(request)

    url = f"{uri}?{urllib.parse.urlencode(request_data)}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        chardata = response.json()
        for quest in chardata["quests"]:
            if quest["id"] == id:
                return JsonResponse(quest)
        return JsonResponse(chardata)
    except requests.RequestException as e:
        return HttpResponse(f"Uh-oh, we hit error {e.response.status_code}", str(e))
