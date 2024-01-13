from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import WeeklyCharProgress
from oauth.models import UserAuthDetails

import requests
import urllib.parse

mattsub = "52039343"


def index(request):
    weekly_char_progresses = WeeklyCharProgress.objects.all()
    context = {"weekly_char_progresses": weekly_char_progresses}
    authinfo = UserAuthDetails.objects.get(sub=mattsub)
    return HttpResponse(authinfo.sub)
    # return render(request, "weekly/index.html", context)


def get_quests(request):
    charname = request.GET.get("character", None)
    uri = f"https://us.api.blizzard.com/profile/wow/character/lightbringer/{charname}/quests"
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
        return HttpResponse(e.response.status_code, str(e))
